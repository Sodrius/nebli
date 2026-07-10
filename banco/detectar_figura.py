"""
detectar_figura.py - Detecta questoes que referenciam figura/grafico/esquema
no enunciado e marca-as no frontmatter com `precisa_figura: true`.

Pipeline canonico: rodar APOS cada ingestao de novas provas.

Heuristicas de deteccao (so casa em padroes indicativos, nao em falsos
positivos como 'configuracao'):
  - "indique na figura"
  - "observe a figura"
  - "considere a figura"
  - "analise a figura"
  - "com base na figura"
  - "de acordo com a figura"
  - "conforme a figura"
  - "(figura|grafico|esquema|diagrama) (acima|abaixo|a seguir|ao lado)"
  - "figura X" onde X esta no enunciado e nao em palavra composta

Output:
  - Frontmatter da questao ganha `precisa_figura: true`
  - Se ainda nao tem `figura:`, cria placeholder vazio para Davi preencher
  - Relatorio em arquivos-trabalho/questoes-com-figura-{UC}.md com
    sugestao de candidato em banco/figuras/ baseado em fonte/prova/ano

Uso:
  python banco/detectar_figura.py --uc UC1            (dry-run)
  python banco/detectar_figura.py --uc UC1 --apply
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
QUESTOES = ROOT / "questoes"
FIGURAS = ROOT / "figuras"
OUT_DIR = ROOT.parent / "arquivos-trabalho"

FRONT_RE = re.compile(r"^(---\n)(.*?)(\n---\n)(.*)$", re.DOTALL)

INDICADORES = re.compile(
    r"\b("
    r"indique\s+na\s+figura"
    r"|observe\s+(?:a|o)\s+(?:figura|gr[aá]fico|esquema|diagrama)"
    r"|analise\s+(?:a|o)\s+(?:figura|gr[aá]fico|esquema|diagrama)"
    r"|considere\s+(?:a|o)\s+(?:figura|gr[aá]fico|esquema|diagrama)"
    r"|com\s+base\s+(?:na|no)\s+(?:figura|gr[aá]fico|esquema|diagrama)"
    r"|de\s+acordo\s+com\s+(?:a|o)\s+(?:figura|gr[aá]fico|esquema|diagrama)"
    r"|conforme\s+(?:a|o)\s+(?:figura|gr[aá]fico|esquema|diagrama)"
    r"|(?:figura|gr[aá]fico|esquema|diagrama)\s+(?:acima|abaixo|a\s+seguir|ao\s+lado)"
    r"|com\s+base\s+no\s+esquema"
    r"|na\s+(?:figura|gr[aá]fico|tabela)\s+abaixo"
    r"|representa(?:do|da)?\s+(?:no|na)\s+(?:gr[aá]fico|esquema|figura)"
    r")\b",
    re.IGNORECASE,
)


def parse(path: Path) -> tuple[dict, str, str, str, str] | None:
    text = path.read_text(encoding="utf-8")
    m = FRONT_RE.match(text)
    if not m:
        return None
    front_open, front_body, front_close, body = m.groups()
    try:
        fm = yaml.safe_load(front_body) or {}
    except yaml.YAMLError:
        return None
    return fm, front_open, front_body, front_close, body


def extrai_enunciado(body: str) -> str:
    m = re.search(r"##\s*Enunciado\s*\n(.*?)(?=\n##\s|\Z)", body,
                  re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else body


def sugerir_figura(fm: dict) -> str | None:
    """Heuristica fraca: olha 'fonte', 'prova', 'ano', 'aula' pra propor
    um arquivo em banco/figuras/."""
    fonte = str(fm.get("fonte", "")).lower()
    prova = str(fm.get("prova", "")).lower()
    ano = str(fm.get("ano", ""))
    aula = str(fm.get("aula", "")).lower()

    # Determina disciplina pelo slug da aula
    disciplinas = {
        "biocel": "biocel", "bioq": "bioquimica", "fisio": "fisiologia",
        "biomol": "biomol",
    }
    disc = None
    for prefix, label in disciplinas.items():
        if aula.startswith(prefix):
            disc = label
            break

    candidatos = []
    if FIGURAS.exists():
        for fig in FIGURAS.glob("*.png"):
            nome_low = fig.name.lower()
            score = 0
            if prova and prova in nome_low:
                score += 2
            if ano and ano in nome_low:
                score += 1
            if disc and disc in nome_low:
                score += 2
            if score > 0:
                candidatos.append((score, fig.name))
    candidatos.sort(reverse=True)
    if candidatos:
        return candidatos[0][1]
    return None


def upsert_campo_frontmatter(front_body: str, campo: str, valor: str) -> str:
    """Insere ou atualiza um campo no frontmatter YAML. Preserva ordem."""
    pat = re.compile(rf"^{re.escape(campo)}:.*$", re.MULTILINE)
    if pat.search(front_body):
        return pat.sub(f"{campo}: {valor}", front_body, count=1)
    # injeta no fim do frontmatter
    return front_body.rstrip() + f"\n{campo}: {valor}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--uc", default="UC1")
    ap.add_argument("--apply", action="store_true",
                    help="grava precisa_figura no frontmatter")
    args = ap.parse_args()

    detectadas = []
    OUT_DIR.mkdir(exist_ok=True)

    for path in sorted(QUESTOES.glob("q-*.md")):
        parsed = parse(path)
        if not parsed:
            continue
        fm, fo, fb, fc, body = parsed
        if str(fm.get("uc_origem", "")).strip() != args.uc:
            continue

        enunciado = extrai_enunciado(body)
        if not INDICADORES.search(enunciado):
            continue

        ja_marcada = fm.get("precisa_figura") is True
        figura_atual = fm.get("figura") or ""
        sugestao = sugerir_figura(fm)

        match_str = INDICADORES.search(enunciado).group(0)
        detectadas.append({
            "file": path.name,
            "id": fm.get("id", "?"),
            "aula": fm.get("aula", "—"),
            "formato": fm.get("formato", "—"),
            "trecho": match_str,
            "ja_marcada": ja_marcada,
            "figura_atual": figura_atual,
            "sugestao": sugestao or "—",
        })

        if args.apply and not ja_marcada:
            new_fb = upsert_campo_frontmatter(fb, "precisa_figura", "true")
            if not figura_atual:
                new_fb = upsert_campo_frontmatter(new_fb, "figura", '""')
            path.write_text(fo + new_fb + fc + body, encoding="utf-8")

    write_report(detectadas, args.uc, args.apply)


def write_report(detectadas, uc, applied):
    out = OUT_DIR / f"questoes-com-figura-{uc}.md"
    lines = [
        f"# Questões {uc} que referenciam figura no enunciado",
        "",
        f"Detectadas pelo `banco/detectar_figura.py`. Total: **{len(detectadas)}**.",
        "",
        f"Modo: {'APLICADO (precisa_figura: true gravado no frontmatter)' if applied else 'DRY-RUN'}",
        "",
        "## Workflow",
        "",
        "1. Para cada questão listada abaixo, abra a prova original (no scan de `banco/figuras/`).",
        "2. Recorte a figura específica e salve como `banco/figuras/q-XXXX.png`",
        "   (mesmo padrão de nome da questão).",
        "3. Edite o frontmatter da questão: `figura: q-XXXX.png`",
        "4. Re-gere o caderno: figura será embutida automaticamente.",
        "",
        "Se a questão não precisar mais de imagem (texto suficiente), edite",
        "`precisa_figura: false` e o aviso some.",
        "",
        "## Lista",
        "",
        "| ID | Arquivo | Formato | Aula | Trecho | Sugestão de candidato |",
        "|---|---|---|---|---|---|",
    ]
    for d in detectadas:
        figura_status = "✓" if d["figura_atual"] and d["figura_atual"] != '""' else "—"
        lines.append(
            f"| {d['id']} | `{d['file']}` | {d['formato']} | `{d['aula']}` | "
            f"_{d['trecho'][:50]}_ | `{d['sugestao']}` (figura: {figura_status}) |"
        )
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Relatorio: {out}")
    print(f"Detectadas: {len(detectadas)}")
    for d in detectadas:
        print(f"  {d['file']} (id={d['id']}) - trecho: '{d['trecho']}'")


if __name__ == "__main__":
    main()
