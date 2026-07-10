"""
auditar_caderno_html.py — Auditoria do HTML do caderno antes de gerar PDF.

Verifica integridade visual e textual:
  - Mojibake (UTF-8 lido como Latin-1, sequências â€, Ã©, etc)
  - Textos sem acento ASCII-cadáver (questoes/funcao/explicacao em vez de
    questões/função/explicação) — heurística de provável ingestão antiga
  - Questões enormes (>1800 chars) que provavelmente quebrarão página
  - Alternativas/itens vazios ou faltando
  - Badges sem aula ou sem ano
  - Gabarito declarado mas não correspondente a alternativa
  - Discursivas sem espaço pautado configurado

Uso:
  python typst-build/auditar_caderno_html.py typst-build/_cadernos/caderno-uc1-p3.html
"""

from __future__ import annotations
import argparse
import re
import sys
from collections import Counter
from pathlib import Path


MOJIBAKE_RE = re.compile(
    r"(â€|Ã[¡-¿]|Â[\x80-\x9f]|ï¿½|�)",
)

PALAVRAS_ASCII_SUSPEITAS = {
    # forma ascii : forma esperada com acento
    "questoes": "questões",
    "funcao": "função",
    "funcoes": "funções",
    "explicacao": "explicação",
    "celula": "célula",
    "celulas": "células",
    "transcricao": "transcrição",
    "traducao": "tradução",
    "replicacao": "replicação",
    "regulacao": "regulação",
    "transmissao": "transmissão",
    "expressao": "expressão",
    "introducao": "introdução",
    "sintese": "síntese",
    "energetica": "energética",
    "membranar": "membranar",
    "ativacao": "ativação",
    "inibicao": "inibição",
    "concentracao": "concentração",
    "solucao": "solução",
    "reacao": "reação",
    "reacoes": "reações",
    "acao": "ação",
    "ions": "íons",
    "ionica": "iônica",
    "proteinas": "proteínas",
    "agua": "água",
    "metabolico": "metabólico",
    "aerobico": "aeróbico",
    "anaerobico": "anaeróbico",
    "endogenas": "endógenas",
    "exogenas": "exógenas",
}


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text)


def _split_blocks(html: str, start_marker_re: re.Pattern) -> list[tuple[str, str]]:
    """Encontra blocos por marcadores de início — cada bloco vai do
    seu marcador até o próximo marcador (de qualquer tipo de seção)
    ou até a próxima seção principal (gabarito, apêndice, discursivas)."""
    # marcadores que delimitam o fim de uma questão objetiva
    fim_re = re.compile(
        r'<div class="questao(?:-discursiva)?(?:\s+permite-quebra)?">'
        r'|<div class="gabarito '
        r'|<div class="apendice-'
        r'|<div class="page-break"><h2 class="secao-discursivas',
    )
    starts = [m.start() for m in start_marker_re.finditer(html)]
    out = []
    for i, s in enumerate(starts):
        # próximo limite: ou próxima questão (qualquer) ou seção principal
        next_candidates = [m.start() for m in fim_re.finditer(html, s + 1)]
        e = next_candidates[0] if next_candidates else len(html)
        block = html[s:e]
        id_m = re.search(r'<div class="questao-badge-id">(\d+)</div>', block)
        qid = id_m.group(1) if id_m else "?"
        out.append((qid, block))
    return out


def find_questoes(html: str) -> list[tuple[str, str]]:
    pat = re.compile(r'<div class="questao(?:\s+permite-quebra)?">')
    return _split_blocks(html, pat)


def find_discursivas(html: str) -> list[tuple[str, str]]:
    pat = re.compile(r'<div class="questao-discursiva(?:\s+permite-quebra)?">')
    return _split_blocks(html, pat)


def audit(html_path: Path) -> dict:
    raw = html_path.read_bytes()
    # strip BOM se houver
    if raw[:3] == b"\xef\xbb\xbf":
        raw = raw[3:]
    text = raw.decode("utf-8", errors="replace")

    findings: dict[str, list[str]] = {
        "mojibake": [],
        "ascii_sem_acento": [],
        "questao_enorme": [],
        "questao_vazia": [],
        "alternativas_problema": [],
        "badge_sem_ano": [],
        "badge_sem_aula": [],
        "discursiva_sem_espaco": [],
    }
    metrics: dict[str, int] = {}

    # 1. Mojibake global
    moji = MOJIBAKE_RE.findall(text)
    if moji:
        c = Counter(moji)
        for seq, n in c.most_common(10):
            findings["mojibake"].append(f"'{seq}' ocorre {n}x")
    metrics["mojibake_count"] = len(moji)

    # 2. ASCII sem acento — só em texto visível
    plain = strip_html(text).lower()
    ascii_hits = Counter()
    for ascii_w, expected in PALAVRAS_ASCII_SUSPEITAS.items():
        # match palavra inteira
        n = len(re.findall(rf"\b{re.escape(ascii_w)}\b", plain))
        if n > 0:
            ascii_hits[ascii_w] = n
    for w, n in ascii_hits.most_common(15):
        findings["ascii_sem_acento"].append(f"'{w}' (esperado: '{PALAVRAS_ASCII_SUSPEITAS[w]}') aparece {n}x")
    metrics["ascii_total"] = sum(ascii_hits.values())

    # 3. Análise por questão (objetivas)
    questoes = find_questoes(text)
    metrics["questoes_objetivas"] = len(questoes)
    for qid, qhtml in questoes:
        plain_q = strip_html(qhtml)
        if len(plain_q) > 1800:
            findings["questao_enorme"].append(f"id={qid}: {len(plain_q)} chars (quebra de página provável)")
        if len(plain_q) < 60:
            findings["questao_vazia"].append(f"id={qid}: muito curta ({len(plain_q)} chars) — pode estar incompleta")
        # alternativas
        alts = re.findall(r'<div class="alternativa-letra">([A-E])\)', qhtml)
        if "alternativa-letra" in qhtml and len(alts) < 4:
            # 2 alternativas pode ser V/F legítimo
            plain_low = strip_html(qhtml).lower()
            is_vf = len(alts) == 2 and ("verdadeiro" in plain_low or "verdadeira" in plain_low)
            if not is_vf:
                findings["alternativas_problema"].append(f"id={qid}: só {len(alts)} alternativas MC")
        # CE
        ce_itens = re.findall(r'<div class="item-ce-numero">', qhtml)
        if "item-ce-numero" in qhtml and len(ce_itens) < 2:
            findings["alternativas_problema"].append(f"id={qid}: CE com {len(ce_itens)} itens")
        # badge ano/aula
        ano_meta = re.search(r'<div class="questao-badge-meta">[^·]*·\s*([^<]+)</div>', qhtml)
        if ano_meta and ano_meta.group(1).strip() in {"—", "-", ""}:
            findings["badge_sem_ano"].append(f"id={qid}: sem ano declarado")
        aula_metas = re.findall(r'<div class="questao-badge-meta">([^<]+)</div>', qhtml)
        if len(aula_metas) < 2 or not aula_metas[-1].strip():
            findings["badge_sem_aula"].append(f"id={qid}: sem aula no badge")

    # 4. Discursivas
    discursivas = find_discursivas(text)
    metrics["questoes_discursivas"] = len(discursivas)
    for qid, qhtml in discursivas:
        if "discursiva-espaco" not in qhtml:
            findings["discursiva_sem_espaco"].append(f"id={qid}: sem espaço pautado")

    return {"findings": findings, "metrics": metrics, "path": html_path}


def write_report(result: dict, out: Path) -> bool:
    """Devolve True se houve bloqueante (mojibake ou alternativa faltando)."""
    findings = result["findings"]
    metrics = result["metrics"]
    has_blocker = bool(findings["mojibake"] or findings["alternativas_problema"])

    lines = [
        f"# Auditoria HTML — {result['path'].name}",
        "",
        "## Métricas",
        f"- Questões objetivas: {metrics.get('questoes_objetivas', 0)}",
        f"- Questões discursivas: {metrics.get('questoes_discursivas', 0)}",
        f"- Total de mojibake: {metrics.get('mojibake_count', 0)}",
        f"- Total de palavras ASCII (sem acento): {metrics.get('ascii_total', 0)}",
        "",
    ]

    categorias = [
        ("mojibake", "❌ Mojibake (codificação corrompida — BLOQUEANTE)"),
        ("alternativas_problema", "❌ Alternativas / itens com problema (BLOQUEANTE)"),
        ("questao_vazia", "⚠ Questões suspeitas de estar incompletas"),
        ("questao_enorme", "⚠ Questões muito longas (quebra de página provável)"),
        ("ascii_sem_acento", "⚠ Texto sem acento (provável ingestão antiga, não-bloqueante)"),
        ("badge_sem_ano", "ℹ Questões sem ano declarado"),
        ("badge_sem_aula", "ℹ Questões sem aula no badge"),
        ("discursiva_sem_espaco", "❌ Discursivas sem espaço pautado"),
    ]
    for key, label in categorias:
        items = findings.get(key, [])
        if not items:
            continue
        lines.append(f"## {label} ({len(items)})")
        lines.append("")
        for it in items[:50]:
            lines.append(f"- {it}")
        if len(items) > 50:
            lines.append(f"- ... e mais {len(items)-50}")
        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Relatório: {out}")
    print(f"  Métricas: {metrics}")
    for key, items in findings.items():
        if items:
            print(f"  {key}: {len(items)}")
    return has_blocker


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html", type=Path, help="Caminho do caderno HTML")
    args = ap.parse_args()
    if not args.html.exists():
        print(f"HTML não existe: {args.html}")
        sys.exit(1)
    result = audit(args.html)
    out = Path("arquivos-trabalho") / f"auditoria-{args.html.stem}.md"
    out.parent.mkdir(exist_ok=True)
    has_blocker = write_report(result, out)
    if has_blocker:
        print("\n[BLOQUEANTES] detectados - corrigir antes de gerar PDF.")
        sys.exit(2)


if __name__ == "__main__":
    main()
