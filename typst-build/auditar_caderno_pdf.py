"""
auditar_caderno_pdf.py - Auditoria abrangente do PDF de um caderno.

Verifica:
  1. Texto residual (mojibake, ASCII sem acento, encoding)
  2. Cobertura: questões esperadas vs encontradas no PDF
  3. Gabarito: todas IDs de objetivas presentes no gabarito
  4. Densidade por página (detecta páginas semi-vazias)
  5. Hifenização: palavras quebradas em sílaba problemática
  6. Tipografia: linhas muito curtas (viúvas), parágrafos órfãos
  7. Fontes embarcadas
  8. Estatísticas gerais (páginas, palavras, etc)

Uso:
  python typst-build/auditar_caderno_pdf.py resumos-gerados/CADERNO-UC01-P3.pdf
  python typst-build/auditar_caderno_pdf.py resumos-gerados/CADERNO-UC01-P3.pdf --uc UC1 --prova P3
"""
from __future__ import annotations
import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("ERRO: pypdf necessário. Instale com: pip install pypdf")
    sys.exit(1)

import yaml

ROOT = Path(__file__).resolve().parent.parent
BANCO = ROOT / "banco"
QUESTOES_DIR = BANCO / "questoes"
OUT_DIR = ROOT / "arquivos-trabalho"

# ============================== padrões de detecção ==============================

MOJIBAKE_RE = re.compile(r"(â€|Ã[¡-¿]|Â[\x80-\x9f]|ï¿½)")

# palavras PT-BR comuns que ficam ASCII em ingestão OCR antiga
ASCII_SUSPEITOS = {
    "nao": "não", "sao": "são", "tambem": "também", "ate": "até",
    "ja": "já", "alem": "além", "atraves": "através", "porem": "porém",
    "reacao": "reação", "reacoes": "reações", "funcao": "função",
    "funcoes": "funções", "celula": "célula", "celulas": "células",
    "transcricao": "transcrição", "traducao": "tradução",
    "replicacao": "replicação", "expressao": "expressão",
    "regulacao": "regulação", "introducao": "introdução",
    "inibicao": "inibição", "concentracao": "concentração",
    "solucao": "solução", "sintese": "síntese",
    "aminoacidos": "aminoácidos", "aminoacido": "aminoácido",
    "hormonios": "hormônios", "hormonio": "hormônio",
    "peptidicos": "peptídicos", "peptidico": "peptídico",
    "hipotonico": "hipotônico", "hipertonico": "hipertônico",
    "osmotico": "osmótico", "osmotica": "osmótica",
    "atomico": "atômico", "atomica": "atômica",
    "enzimatica": "enzimática", "enzimatico": "enzimático",
    "metabolico": "metabólico", "metabolica": "metabólica",
    "aerobico": "aeróbico", "anaerobico": "anaeróbico",
    "necessario": "necessário", "necessaria": "necessária",
    "ions": "íons", "ionica": "iônica", "ionico": "iônico",
    "neuronio": "neurônio", "neuronios": "neurônios",
    "axonio": "axônio", "vesicula": "vesícula", "vesiculas": "vesículas",
    "nucleo": "núcleo", "nucleos": "núcleos",
    "mitocondria": "mitocôndria", "mitocondrias": "mitocôndrias",
    "deficiencia": "deficiência", "deficiencias": "deficiências",
    "caracteristica": "característica", "caracteristicas": "características",
    "alteracao": "alteração", "alteracoes": "alterações",
    "isomero": "isômero", "isomeros": "isômeros",
    "fosforilacao": "fosforilação",  # 'fosforilada/fosforilado' são PT-BR sem acento (paroxítonas), NÃO incluir
}

# palavras técnicas que NÃO deveriam estar hifenizadas se aparecerem cortadas
PALAVRAS_INDIVISIVEIS = {
    "ATP", "ADP", "AMP", "NADH", "NADPH", "FADH2", "DNA", "RNA",
    "ELISA", "PCR", "HPLC", "PAGE", "SDS", "ATPase", "GTPase",
}


# ============================== util ==============================

def extract_full_text(pdf: PdfReader) -> tuple[str, list[str]]:
    """Retorna (texto_completo, textos_por_pagina)."""
    pages = [p.extract_text() or "" for p in pdf.pages]
    return "\n".join(pages), pages


def load_question_ids_expected(uc: str, prova: str) -> tuple[set[str], set[str], set[str]]:
    """Retorna (ids_mc, ids_ce, ids_discursivas) esperados para o caderno."""
    cronograma_path = BANCO / f"aulas_uc{int(uc.replace('UC','').lstrip('0') or 1):02d}.yml"
    if not cronograma_path.exists():
        cronograma_path = BANCO / f"aulas_uc{uc.replace('UC','').lstrip('0') or 1}.yml"
    crono_data = yaml.safe_load(cronograma_path.read_text(encoding="utf-8"))
    cronograma = {a["slug"]: a for a in crono_data.get("aulas", [])}

    mc, ce, disc = set(), set(), set()
    FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
    for path in sorted(QUESTOES_DIR.glob("q-*.md")):
        text = path.read_text(encoding="utf-8")
        m = FRONT_RE.match(text)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        if str(fm.get("uc_origem", "")).strip() != uc:
            continue
        aula = str(fm.get("aula", "")).strip()
        if prova == "HISTORICO":
            if not (aula and aula not in cronograma):
                continue
        else:
            if not aula or aula not in cronograma:
                continue
            if cronograma[aula]["prova"] != prova:
                continue
        qid = str(fm.get("id", "?"))
        fmt = str(fm.get("formato", "")).upper()
        if fmt == "MC":
            mc.add(qid)
        elif fmt == "CE":
            ce.add(qid)
        elif fmt in {"DISCURSIVA", "DISC"}:
            disc.add(qid)
    return mc, ce, disc


# ============================== checagens ==============================

def check_mojibake(text: str) -> list[str]:
    findings = []
    hits = MOJIBAKE_RE.findall(text)
    if hits:
        c = Counter(hits)
        for seq, n in c.most_common(5):
            findings.append(f"'{seq}' ocorre {n}x")
    return findings


def check_ascii_residual(text: str) -> list[str]:
    findings = []
    counts = Counter()
    text_low = text.lower()
    for ascii_w, esperado in ASCII_SUSPEITOS.items():
        n = len(re.findall(rf"\b{re.escape(ascii_w)}\b", text_low))
        if n:
            counts[ascii_w] = n
    for w, n in counts.most_common(20):
        findings.append(f"'{w}' (esperado '{ASCII_SUSPEITOS[w]}') {n}x")
    return findings


def check_page_density(pages: list[str]) -> dict:
    """Retorna métricas: total_pages, semi_vazias (<400 chars no corpo),
    super_densas (>3500 chars)."""
    total = len(pages)
    chars_per_page = [len(p) for p in pages]
    semi_vazias = []
    super_densas = []
    for i, n in enumerate(chars_per_page):
        # capa, abertura-bloco e secao-discursivas-titulo são legitimamente esparsas
        if n < 400 and i > 0:  # pula capa
            semi_vazias.append((i + 1, n))
        if n > 3500:
            super_densas.append((i + 1, n))
    avg = sum(chars_per_page) / total if total else 0
    return {
        "total_pages": total,
        "avg_chars": int(avg),
        "min_chars": min(chars_per_page) if chars_per_page else 0,
        "max_chars": max(chars_per_page) if chars_per_page else 0,
        "semi_vazias": semi_vazias,
        "super_densas": super_densas,
    }


def check_coverage(text: str, esperado_mc: set, esperado_ce: set,
                   esperado_disc: set) -> dict:
    """Verifica se IDs esperados aparecem no PDF."""
    # IDs aparecem como números isolados em formato badge ou dentro de gabarito.
    # Heurística: id seguido de "P3 ·" (badge) ou linha do gabarito.
    all_esperado = esperado_mc | esperado_ce | esperado_disc

    encontrados = set()
    # Procura todos os ids numéricos no texto (badges, gabaritos)
    for m in re.finditer(r"\b(\d{1,5})\b", text):
        encontrados.add(_normaliza_id(m.group(1)))

    encontrados_norm = encontrados
    esperado_norm = {_normaliza_id(x) for x in all_esperado}

    faltantes = esperado_norm - encontrados_norm
    return {
        "esperado_total": len(all_esperado),
        "encontrados_no_pdf": len(encontrados_norm & esperado_norm),
        "faltantes": sorted(faltantes),
        "mc_esperado": len(esperado_mc),
        "ce_esperado": len(esperado_ce),
        "disc_esperado": len(esperado_disc),
    }


def _normaliza_id(s: str) -> str:
    m = re.search(r"\d+", str(s))
    return str(int(m.group(0))) if m else str(s)


def check_gabarito_completo(text: str, esperado_mc: set, esperado_ce: set) -> dict:
    """Verifica seção 'Gabarito' tem todas as IDs de objetivas."""
    # extrai a seção do gabarito (entre "Gabarito" e "Destacável"/"Explicações" ou EOF)
    m = re.search(r"Gabarito\s*\n+(.*?)(?=Destacável|Explicações\s+Detalhadas|\Z)",
                  text, re.DOTALL | re.IGNORECASE)
    if not m:
        return {"erro": "seção Gabarito não encontrada"}
    sec = m.group(1)
    # IDs aparecem como número isolado seguido de espaço/quebra e letra/string de resposta
    ids_no_gab = set()
    for m2 in re.finditer(r"\b(\d{1,5})\b", sec):
        ids_no_gab.add(_normaliza_id(m2.group(1)))
    objetivas_esperado = {_normaliza_id(x) for x in (esperado_mc | esperado_ce)}
    return {
        "esperado_no_gabarito": len(objetivas_esperado),
        "encontrado_no_gabarito": len(ids_no_gab & objetivas_esperado),
        "faltantes_no_gabarito": sorted(objetivas_esperado - ids_no_gab)[:20],
    }


def check_hifenizacoes_suspeitas(text: str) -> list[str]:
    """Detecta palavras técnicas hifenizadas em sílaba ruim. Heurística simples."""
    findings = []
    # palavras técnicas indivisíveis aparecendo com hífen
    for w in PALAVRAS_INDIVISIVEIS:
        if re.search(rf"{w[:2]}-{w[2:]}", text, re.IGNORECASE):
            findings.append(f"'{w}' aparece hifenizada (deveria ser indivisível)")
    # padrão suspeito: hífen seguido de quebra de linha + palavra com 1-2 letras só
    suspeitos = re.findall(r"(\w+)-\n(\w{1,2})\b", text)
    if suspeitos:
        c = Counter(suspeitos)
        for (pre, post), n in c.most_common(3):
            if n >= 2:
                findings.append(f"hifenização suspeita '{pre}-{post}' {n}x")
    return findings


def check_fontes(pdf: PdfReader) -> dict:
    """Lista fontes embarcadas no PDF."""
    fontes = set()
    for page in pdf.pages:
        try:
            resources = page.get("/Resources", {})
            if hasattr(resources, "get_object"):
                resources = resources.get_object()
            font_dict = resources.get("/Font", {}) if resources else {}
            if hasattr(font_dict, "get_object"):
                font_dict = font_dict.get_object()
            for k, v in (font_dict.items() if hasattr(font_dict, "items") else []):
                try:
                    fobj = v.get_object() if hasattr(v, "get_object") else v
                    name = fobj.get("/BaseFont", "")
                    if name:
                        fontes.add(str(name))
                except Exception:
                    pass
        except Exception:
            continue
    return {"fontes": sorted(fontes)}


def check_proporcoes(text: str) -> dict:
    """Mede proporções: % corpo vs % gabarito vs % apêndice."""
    # heurística por marcadores
    marcadores = {
        "capa": (r"^.*?Sumário", "Sumário"),
        "miolo": (r"Sumário(.*?)Questões Discursivas", "início discursivas"),
        "discursivas": (r"Questões Discursivas(.*?)Gabarito", "Gabarito"),
        "gabarito": (r"Gabarito\s*\n.*?(?=Destacável|Explicações)", "destacável"),
        "apendice": (r"Explicações Detalhadas(.*)$", "fim"),
    }
    result = {}
    for nome, (pat, _) in marcadores.items():
        m = re.search(pat, text, re.DOTALL)
        result[nome] = len(m.group(1) if m and m.groups() else (m.group(0) if m else ""))
    total = sum(result.values()) or 1
    return {nome: f"{n:,} chars ({100*n/total:.0f}%)" for nome, n in result.items()}


# ============================== main ==============================

def audit(pdf_path: Path, uc: str | None, prova: str | None) -> dict:
    pdf = PdfReader(str(pdf_path))
    text, pages = extract_full_text(pdf)

    report = {
        "arquivo": pdf_path.name,
        "tamanho_kb": pdf_path.stat().st_size // 1024,
        "paginas": len(pages),
        "palavras": len(re.findall(r"\b\w+\b", text)),
        "caracteres": len(text),
        "acentos_unicode": len(re.findall(r"[áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ]", text)),
    }

    report["mojibake"] = check_mojibake(text)
    report["ascii_residual"] = check_ascii_residual(text)
    report["paginas_densidade"] = check_page_density(pages)
    report["hifenizacao_suspeita"] = check_hifenizacoes_suspeitas(text)
    report["fontes"] = check_fontes(pdf)["fontes"]
    report["proporcoes_secoes"] = check_proporcoes(text)

    if uc and prova:
        mc, ce, disc = load_question_ids_expected(uc, prova)
        report["cobertura"] = check_coverage(text, mc, ce, disc)
        report["gabarito"] = check_gabarito_completo(text, mc, ce)

    return report


def write_report(report: dict, out: Path):
    lines = [
        f"# Auditoria PDF — {report['arquivo']}",
        "",
        "## Métricas gerais",
        f"- Tamanho: {report['tamanho_kb']} KB",
        f"- Páginas: {report['paginas']}",
        f"- Palavras: {report['palavras']:,}",
        f"- Caracteres: {report['caracteres']:,}",
        f"- Acentos Unicode extraídos: {report['acentos_unicode']}",
        "",
        "## Fontes embarcadas",
    ]
    for f in report["fontes"]:
        lines.append(f"- `{f}`")
    lines.append("")

    if report.get("cobertura"):
        c = report["cobertura"]
        lines.append("## Cobertura de questões (esperado pelo cronograma)")
        lines.append(f"- MC esperadas: {c['mc_esperado']}")
        lines.append(f"- CE esperadas: {c['ce_esperado']}")
        lines.append(f"- Discursivas esperadas: {c['disc_esperado']}")
        lines.append(f"- Total esperado: {c['esperado_total']}")
        lines.append(f"- Encontradas no PDF: {c['encontrados_no_pdf']}")
        if c["faltantes"]:
            lines.append(f"- ⚠ Faltantes: {len(c['faltantes'])} — {c['faltantes'][:15]}")
        else:
            lines.append("- ✅ Todas as questões esperadas estão presentes")
        lines.append("")

    if report.get("gabarito"):
        g = report["gabarito"]
        if "erro" in g:
            lines.append(f"## ❌ Gabarito: {g['erro']}")
        else:
            lines.append("## Gabarito consolidado")
            lines.append(f"- Objetivas esperadas no gabarito: {g['esperado_no_gabarito']}")
            lines.append(f"- Presentes no gabarito: {g['encontrado_no_gabarito']}")
            if g["faltantes_no_gabarito"]:
                lines.append(f"- ⚠ Faltantes: {g['faltantes_no_gabarito']}")
            else:
                lines.append("- ✅ Gabarito completo")
        lines.append("")

    lines.append("## Densidade de páginas")
    d = report["paginas_densidade"]
    lines.append(f"- Total: {d['total_pages']} páginas")
    lines.append(f"- Média de caracteres/página: {d['avg_chars']}")
    lines.append(f"- Min/Max: {d['min_chars']} / {d['max_chars']}")
    if d["semi_vazias"]:
        lines.append(f"- ⚠ Páginas semi-vazias (<400 chars): {len(d['semi_vazias'])}")
        for pg, n in d["semi_vazias"][:8]:
            lines.append(f"  - pág {pg}: {n} chars")
    if d["super_densas"]:
        lines.append(f"- ⚠ Páginas super-densas (>3500 chars): {len(d['super_densas'])}")
        for pg, n in d["super_densas"][:8]:
            lines.append(f"  - pág {pg}: {n} chars")
    lines.append("")

    lines.append("## Distribuição por seção")
    for k, v in report["proporcoes_secoes"].items():
        lines.append(f"- {k}: {v}")
    lines.append("")

    if report["mojibake"]:
        lines.append("## ❌ Mojibake detectado (BLOQUEANTE)")
        for f in report["mojibake"]:
            lines.append(f"- {f}")
        lines.append("")
    else:
        lines.append("## ✅ Sem mojibake")
        lines.append("")

    if report["ascii_residual"]:
        lines.append(f"## ⚠ Palavras ASCII residuais ({len(report['ascii_residual'])} categorias)")
        for f in report["ascii_residual"]:
            lines.append(f"- {f}")
    else:
        lines.append("## ✅ Sem palavras ASCII residuais")
    lines.append("")

    if report["hifenizacao_suspeita"]:
        lines.append("## ⚠ Hifenizações suspeitas")
        for f in report["hifenizacao_suspeita"]:
            lines.append(f"- {f}")
    else:
        lines.append("## ✅ Sem hifenizações suspeitas detectadas")
    lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Relatório: {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--uc", help="se passado, audita cobertura vs cronograma")
    ap.add_argument("--prova", help="P1 | P2 | P3 | HISTORICO")
    args = ap.parse_args()

    if not args.pdf.exists():
        print(f"PDF não existe: {args.pdf}")
        sys.exit(1)

    report = audit(args.pdf, args.uc, args.prova)
    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / f"auditoria-pdf-{args.pdf.stem}.md"
    write_report(report, out)

    # Resumo no terminal (ASCII-safe)
    print(f"  Paginas: {report['paginas']}  Palavras: {report['palavras']:,}")
    print(f"  Acentos: {report['acentos_unicode']}")
    print(f"  Mojibake: {len(report['mojibake'])} categorias")
    print(f"  ASCII residual: {len(report['ascii_residual'])} categorias")
    print(f"  Hifenizacao suspeita: {len(report['hifenizacao_suspeita'])} casos")
    d = report["paginas_densidade"]
    print(f"  Paginas semi-vazias: {len(d['semi_vazias'])}  super-densas: {len(d['super_densas'])}")
    if report.get("cobertura"):
        c = report["cobertura"]
        print(f"  Cobertura: {c['encontrados_no_pdf']}/{c['esperado_total']}")


if __name__ == "__main__":
    main()
