#!/usr/bin/env python3
"""
NEBLI -- extrair_slides.py
Renderiza PNGs dos slides + extrai texto em MAPA_CONTEUDO.txt.

Frente B2 do plano de economia (2026-05-16):
  O REDATOR-E1 NAO tem visao. Sem mapa de conteudo, ele chuta numeros
  de slide quando referencia figuras -- bug catastrofico do #6 Acidos
  Nucleicos (11/11 figuras erradas, +80k de retrabalho).

Saida:
  figuras/[tema]/slide-XX.png    (1 por pagina, 300 dpi)
  figuras/[tema]/MAPA_CONTEUDO.txt  (texto extraido por slide)

Uso:
  python3 typst-build/extrair_slides.py SLIDE.pdf TEMA-SLUG
  python3 typst-build/extrair_slides.py slides/UC01.../13-Carboidratos.pdf carboidratos

Dependencias: pymupdf (fitz). Sem OCR -- usa o texto digital do PDF
quando ha; slides puramente visuais (sem texto extraivel) emitem
"[VISUAL -- usar slide adjacente com titulo extraivel]".
"""

import argparse
import sys
from pathlib import Path

try:
    import fitz
except ImportError:
    print("x pymupdf nao instalado. Rode: pip install pymupdf --break-system-packages", file=sys.stderr)
    sys.exit(1)


def extrair(pdf_path: Path, tema: str, figuras_root: Path, dpi: int = 300, max_chars: int = 250):
    if not pdf_path.exists():
        print(f"x PDF nao encontrado: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    out_dir = figuras_root / tema
    out_dir.mkdir(parents=True, exist_ok=True)

    mapa_lines = [
        f"# MAPA_CONTEUDO -- {tema}",
        f"# Slide-fonte: {pdf_path.name}",
        f"# Gerado por extrair_slides.py (frente B2 do plano de economia)",
        f"#",
        f"# Uso: REDATOR-E1 OBRIGATORIAMENTE consulta este arquivo antes de",
        f"# referenciar `slide-XX.png` na Etapa 1. Se um slide aparece como",
        f"# `[VISUAL -- usar adjacente]`, use o slide vizinho com texto extraivel.",
        f"",
    ]

    doc = fitz.open(str(pdf_path))
    n_total = len(doc)
    mat = fitz.Matrix(dpi / 72, dpi / 72)

    print(f"-> {n_total} paginas em {pdf_path.name}")
    print(f"-> Renderizando PNGs e extraindo texto...")

    for i, page in enumerate(doc, start=1):
        slide_id = f"slide-{i:02d}"
        png_path = out_dir / f"{slide_id}.png"
        # Render PNG
        pix = page.get_pixmap(matrix=mat)
        pix.save(str(png_path))
        # Extrai texto digital
        text = page.get_text("text").strip()
        # Limpa quebras de linha multiplas e tabs
        text = " ".join(text.split())
        if len(text) < 15:
            mapa_lines.append(f"{slide_id}: [VISUAL -- usar adjacente com titulo extraivel]")
        else:
            preview = text[:max_chars]
            if len(text) > max_chars:
                preview += "..."
            mapa_lines.append(f"{slide_id}: {preview}")

    mapa_path = out_dir / "MAPA_CONTEUDO.txt"
    mapa_path.write_text("\n".join(mapa_lines) + "\n", encoding="utf-8")

    print(f"v {n_total} PNGs em: {out_dir}/")
    print(f"v MAPA_CONTEUDO.txt em: {mapa_path}")
    print(f"-> Preview das primeiras 5 entradas:")
    for line in mapa_lines[8:13]:
        print(f"   {line}")


def main():
    parser = argparse.ArgumentParser(description="Renderiza slides + gera MAPA_CONTEUDO")
    parser.add_argument("pdf", help="Caminho do PDF do slide")
    parser.add_argument("tema", help="Slug do tema (ex: carboidratos, acidos-nucleicos)")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--figuras-root", default=None,
                        help="Pasta raiz de figuras (default: figuras/ relativa ao projeto)")
    parser.add_argument("--max-chars", type=int, default=250,
                        help="Maximo de chars por entrada no mapa")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if args.figuras_root:
        figuras_root = Path(args.figuras_root)
    else:
        # Default: figuras/ na pasta-mae do typst-build/
        figuras_root = Path(__file__).resolve().parent.parent / "figuras"

    extrair(pdf_path, args.tema, figuras_root, dpi=args.dpi, max_chars=args.max_chars)


if __name__ == "__main__":
    main()
