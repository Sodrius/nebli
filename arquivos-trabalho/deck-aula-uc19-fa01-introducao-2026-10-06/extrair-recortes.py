"""Extratos verificáveis das páginas pertinentes, preservando número do PDF."""
from pathlib import Path
import fitz

here = Path(__file__).resolve().parent
sources = {
    "rang-cap2": ("rang.pdf", range(34, 46)),
    "prova-farmacodinamica": ("Todas as questões.pdf", (25, 26, 84, 85)),
    "denucci-introducao": ("DeNucci 01_vf-revisada-04102019.pdf", range(3, 6)),
}
for name, (file, pages) in sources.items():
    with fitz.open(here / "fontes" / file) as doc:
        text = "\n\n".join(f"=== PDF {page} ===\n{doc[page - 1].get_text()}" for page in pages)
    dest = here / "fontes" / f"{name}.txt"
    dest.write_text(text, encoding="utf-8")
    print(dest.name, len(text.split()))
