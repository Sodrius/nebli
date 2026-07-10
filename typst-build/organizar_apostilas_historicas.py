"""
Phase A do plano de analise das apostilas historicas.

Caminha em slides/slides-e-resumos/B - Primeiro ano/ buscando arquivos
'*Etapas 1 a 3*.pdf', copia para resumos-gerados/apostilas-historicas/ com
slug determinístico e gera INDICE.md.
"""

from __future__ import annotations
import shutil
import unicodedata
import re
from pathlib import Path

ROOT = Path(r"C:\AI use\nebli")
SRC = ROOT / "slides" / "slides-e-resumos" / "B - Primeiro ano"
DST = ROOT / "resumos-gerados" / "apostilas-historicas"

DISCIPLINA_CODE = {
    "Biologia Celular": "UC01-BC",
    "Bioquímica": "UC01-BIOQ",
    "Fisiologia de membranas": "UC01-FMEMB",
    "Biologia Celular, Tecidual e Imunologia (BMC)": "UC02-BMC",
    "Liga TCP": "LIGA-TCP",
}

def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s

def parse_aula_folder(name: str) -> tuple[str | None, str]:
    """'14 - Glicólise' -> ('14', 'Glicólise'). 'Liga TCP' -> (None, 'Liga TCP')."""
    m = re.match(r"^(\d+)(?:\s+e\s+\d+)?\s*-\s*(.+)$", name)
    if m:
        return m.group(1), m.group(2)
    return None, name

def extract_autor_e_flag(filename: str) -> tuple[str, str | None]:
    """
    'Glicólise - Etapas 1 a 3 - Marisa Helena.pdf' -> ('Marisa Helena', None)
    'Gliconeogênese - Etapas 1 a 3 - Marisa Helena - resumo ruim.pdf'
        -> ('Marisa Helena', 'resumo ruim')
    'Liga TCP - Etapas 1 a 3 - não tão bom.pdf' -> ('', 'não tão bom')
    """
    stem = Path(filename).stem
    m = re.search(r"Etapas 1 a 3\s*-\s*(.+)$", stem)
    if not m:
        return "", None
    tail = m.group(1).strip()
    flag_terms = ("ruim", "não tão bom", "nao tao bom", "fraco")
    flag = None
    parts = [p.strip() for p in tail.split(" - ")]
    autor_parts = []
    for p in parts:
        if any(t in p.lower() for t in flag_terms):
            flag = p
        else:
            autor_parts.append(p)
    autor = " - ".join(autor_parts)
    return autor, flag

def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    entries = []
    pdfs = sorted(SRC.rglob("*Etapas 1 a 3*.pdf"))
    print(f"Encontrados {len(pdfs)} PDFs.")

    for pdf in pdfs:
        rel = pdf.relative_to(SRC)
        parts = rel.parts
        if parts[0] == "Ligas":
            disciplina_raw = parts[1]
            aula_folder = None
        else:
            disciplina_raw = parts[1]
            aula_folder = parts[2] if len(parts) > 3 else None

        disc_code = DISCIPLINA_CODE.get(disciplina_raw, slugify(disciplina_raw).upper())

        if aula_folder:
            num, nome = parse_aula_folder(aula_folder)
            if num:
                slug = f"{disc_code}-{num}-{slugify(nome)}"
            else:
                slug = f"{disc_code}-{slugify(nome)}"
        else:
            slug = disc_code

        target = DST / f"{slug}.pdf"
        if target.exists():
            print(f"  skip (ja existe): {target.name}")
        else:
            shutil.copy2(pdf, target)
            print(f"  copiado: {target.name}")

        autor, flag = extract_autor_e_flag(pdf.name)
        entries.append({
            "slug": slug,
            "origem": str(pdf.relative_to(ROOT)).replace("\\", "/"),
            "autor": autor,
            "flag": flag,
            "disciplina_raw": disciplina_raw,
            "aula_folder": aula_folder,
        })

    # gera INDICE.md
    lines = [
        "# INDICE — Apostilas históricas",
        "",
        f"Total: {len(entries)} resumos copiados de `slides/slides-e-resumos/`.",
        "Originais permanecem intactos (cópia, não move).",
        "",
        "| Slug | Autor | Flag | Origem |",
        "|---|---|---|---|",
    ]
    for e in sorted(entries, key=lambda x: x["slug"]):
        flag = e["flag"] or ""
        lines.append(f"| `{e['slug']}` | {e['autor']} | {flag} | `{e['origem']}` |")
    (DST / "INDICE.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nINDICE.md gravado em {DST}.")

if __name__ == "__main__":
    main()
