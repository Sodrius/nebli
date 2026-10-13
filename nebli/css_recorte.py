"""Converte o recorte de imagem feito por CSS (div com padding-bottom + img absoluta) em arquivo recortado de verdade.

Os recortes de 03–06/10 posicionam a figura inteira do livro com `left/top/width` em %, dentro de uma caixa com
`padding-bottom` em %. Davi relatou imagens que não aparecem/ficam erradas no AnkiDroid e figura "zuada" desse estilo.
Este módulo calcula o retângulo visível na figura original e grava só esse pedaço.

    python3 -m nebli.css_recorte <html-do-campo> <saida.jpg>     # (uso interno via recortar())
"""
from __future__ import annotations

import os
import re
from pathlib import Path

import fitz

MEDIA = Path(os.path.expanduser("~/Library/Application Support/Anki2/User 1/collection.media"))
BLOCO = re.compile(r'<div style="width:100%;max-width:\d+px;margin:12px auto;background:white">'
                   r'<div style="position:relative;height:0;padding-bottom:([\d.]+)%;overflow:hidden">'
                   r'<img src="([^"]+)" style="position:absolute;left:(-?[\d.]+)%;top:(-?[\d.]+)%;width:([\d.]+)%;'
                   r'[^"]*"></div></div>')


def blocos(html: str):
    return [(m.group(0), m.group(2), float(m.group(1)), float(m.group(3)), float(m.group(4)), float(m.group(5)))
            for m in BLOCO.finditer(html)]


def retangulo(pb, left, top, width, w_img, h_img):
    """Retângulo visível em pixels da figura original. Caixa: largura C=1, altura pb/100; img: largura width/100."""
    esc = (width / 100) / w_img          # caixa por pixel da imagem
    x0 = (-left / 100) / esc
    y0 = (-top / 100) / esc
    x1 = x0 + 1 / esc
    y1 = y0 + (pb / 100) / esc
    return fitz.IRect(max(0, x0), max(0, y0), min(w_img, x1), min(h_img, y1))


def recortar(src_name: str, pb, left, top, width, saida: Path, largura_max=900) -> Path:
    src = MEDIA / src_name
    tmp = saida.with_suffix(".src.png")
    if src.suffix.lower() == ".webp":
        os.system(f'sips -s format png "{src}" --out "{tmp}" >/dev/null')
        src = tmp
    pix = fitz.Pixmap(str(src))
    r = retangulo(pb, left, top, width, pix.width, pix.height)
    doc = fitz.open()
    page = doc.new_page(width=r.width, height=r.height)
    img_doc = fitz.open(str(src))
    s = img_doc[0].rect.width / pix.width
    page.show_pdf_page(page.rect, fitz.open("pdf", img_doc.convert_to_pdf()), 0, clip=fitz.Rect(r) * s)
    z = min(1, largura_max / r.width) if r.width > largura_max else 1
    out = page.get_pixmap(matrix=fitz.Matrix(z, z))
    out.save(str(saida), jpg_quality=88) if saida.suffix.lower() in (".jpg", ".jpeg") else out.save(str(saida))
    tmp.unlink(missing_ok=True)
    return saida
