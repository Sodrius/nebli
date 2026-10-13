"""Recortes diretos das figuras da aula; coordenadas em pontos do PDF 720×540.

Nenhum título, legenda ou lista diagnóstica entra no recorte. Conferir as imagens
produzidas visualmente antes do build/instalação.
"""
from pathlib import Path
import fitz

HERE = Path(__file__).parent
DOC = fitz.open(HERE / "fontes/slides.pdf")
RECTS = {
    10: (385, 135, 685, 490),
    14: (0, 0, 720, 505),
    17: (20, 285, 360, 495),
    20: (280, 75, 635, 305),
    21: (185, 65, 500, 320),
    23: (430, 85, 700, 325),
    24: (20, 80, 700, 500),
    26: (95, 115, 610, 490),
    27: (25, 70, 385, 510),
    31: (30, 145, 535, 520),
    33: (445, 245, 705, 410),
    35: (235, 125, 685, 460),
}
OUT = HERE / "img"
OUT.mkdir(exist_ok=True)
# Na lâmina 13, os rótulos são texto vetorial sobre a foto. Extrair a imagem
# embutida preserva a histologia sem tapar partes do granuloma.
source = DOC[12].get_images(full=True)[0][0]
embedded = DOC.extract_image(source)
assert embedded["ext"] == "jpeg"
(OUT / "pt47-s13-clean.jpeg").write_bytes(embedded["image"])
source16 = DOC[15].get_images(full=True)[0][0]
embedded16 = DOC.extract_image(source16)
assert embedded16["ext"] == "jpeg"
(OUT / "pt47-s16-clean.jpeg").write_bytes(embedded16["image"])
for slide, rect in RECTS.items():
    page = DOC[slide - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=fitz.Rect(rect), alpha=False)
    pix.save(OUT / f"pt47-s{slide:02}-visual.png")
    print(slide, pix.width, pix.height)
