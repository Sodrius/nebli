#!/usr/bin/env python3
"""
NEBLI -- extrair_imagens_pdf.py
Extrai imagens embutidas de um PDF (anatomopatologia, respostas-do-relatorio).

Diferente do extrair_slides.py (que renderiza paginas como PNG), este extrai
as imagens originais embutidas no PDF -- macro/micro de pecas, lamina HE, IHQ.

Saida:
  figuras/<tema>/img-pNNN-NN.png         (imagens extraidas, nome=pagina-index)
  figuras/<tema>/MAPA_CONTEUDO.txt        (mapa imagem -> pagina -> texto vizinho)

Uso:
  python typst-build/extrair_imagens_pdf.py <pdf> <tema-slug>
"""
import argparse
import sys
from pathlib import Path

try:
    import fitz
except ImportError:
    print("x pymupdf nao instalado", file=sys.stderr)
    sys.exit(1)


def extrair(pdf_path: Path, tema: str, figuras_root: Path, min_size: int = 100):
    if not pdf_path.exists():
        print(f"x PDF nao encontrado: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    out_dir = figuras_root / tema
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    mapa = [
        f"# MAPA_CONTEUDO -- {tema}",
        f"# Fonte: {pdf_path.name}",
        f"# Imagens embutidas extraidas; min {min_size}px lado.",
        "",
    ]
    total = 0
    for page_idx, page in enumerate(doc, start=1):
        text = " ".join(page.get_text("text").split())[:300]
        images = page.get_images(full=True)
        if not images:
            continue
        for img_idx, img_info in enumerate(images, start=1):
            xref = img_info[0]
            try:
                base = doc.extract_image(xref)
            except Exception as e:
                continue
            img_bytes = base.get("image")
            ext = base.get("ext", "png")
            w = base.get("width", 0)
            h = base.get("height", 0)
            if w < min_size or h < min_size:
                continue
            fname = f"img-p{page_idx:03d}-{img_idx:02d}.{ext}"
            (out_dir / fname).write_bytes(img_bytes)
            mapa.append(f"{fname} ({w}x{h}) | pag {page_idx} | {text[:200]}")
            total += 1

    mapa_path = out_dir / "MAPA_CONTEUDO.txt"
    mapa_path.write_text("\n".join(mapa) + "\n", encoding="utf-8")
    print(f"v {total} imagens extraidas em {out_dir}/")
    print(f"v MAPA: {mapa_path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("tema")
    ap.add_argument("--min-size", type=int, default=100)
    ap.add_argument("--figuras-root", default=None)
    args = ap.parse_args()

    pdf_path = Path(args.pdf)
    if args.figuras_root:
        figuras_root = Path(args.figuras_root)
    else:
        figuras_root = Path(__file__).resolve().parent.parent / "figuras"
    extrair(pdf_path, args.tema, figuras_root, min_size=args.min_size)


if __name__ == "__main__":
    main()
