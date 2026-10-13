"""Setas e rótulos curtos sobre uma imagem, para direcionar a figura ao alvo do card (comentários de 05–08/10).

Davi: "uma boa imagem tem pouca informação, mas direcionada em específico para o card"; "faltou o cloze ter uma
seta apontando". Seta amarela com contorno preto (visível em H&E e em esquemas); rótulo opcional. Na frente, usar
seta sem rótulo quando o rótulo daria a resposta.

    python3 -m nebli.seta <entrada> <saida.png> --seta X,Y,ANG[,COMP] [--seta ...] [--rotulo X,Y,TEXTO] [--largura 900]
        X,Y: ponta da seta em pixels da entrada; ANG: direção de onde a seta vem, em graus (0 = da direita,
        90 = de baixo, 180 = da esquerda, 270 = de cima); COMP: comprimento (padrão 9% da largura).
        --recorte X0,Y0,X1,Y1 recorta antes; --largura redimensiona a saída (padrão: mantém).
"""
from __future__ import annotations

import math
import sys

import fitz

AMARELO = (1, 0.85, 0)
PRETO = (0, 0, 0)


def _arrow(shape, tip, ang, comp, esp):
    a = math.radians(ang)
    tail = fitz.Point(tip.x + comp * math.cos(a), tip.y + comp * math.sin(a))
    head = comp * 0.38
    left = fitz.Point(tip.x + head * math.cos(a + 0.45), tip.y + head * math.sin(a + 0.45))
    right = fitz.Point(tip.x + head * math.cos(a - 0.45), tip.y + head * math.sin(a - 0.45))
    base = fitz.Point(tip.x + head * 0.8 * math.cos(a), tip.y + head * 0.8 * math.sin(a))
    for cor, w in ((PRETO, esp * 2.2), (AMARELO, esp)):
        shape.draw_line(base, tail)
        shape.finish(color=cor, width=w, lineCap=1)
    shape.draw_polyline([tip, left, right, tip])
    shape.finish(color=PRETO, fill=AMARELO, width=esp * 0.6, closePath=True)


def desenhar(entrada: str, saida: str, setas: list[tuple[float, float, float, float | None]],
             rotulos: list[tuple[float, float, str]] = (), recorte=None, largura: int | None = None) -> None:
    src = fitz.open(entrada)
    px = fitz.Pixmap(entrada)
    s = src[0].rect.width / px.width  # PNG com dpi ≠ 72: página em pontos ≠ pixels
    doc = fitz.open()
    clip = fitz.Rect(*recorte) if recorte else fitz.Rect(0, 0, px.width, px.height)
    page = doc.new_page(width=clip.width, height=clip.height)
    page.show_pdf_page(page.rect, fitz.open("pdf", src.convert_to_pdf()), 0, clip=clip * s)
    shape = page.new_shape()
    esp = max(3.0, clip.width / 160)
    for x, y, ang, comp in setas:
        _arrow(shape, fitz.Point(x - clip.x0, y - clip.y0), ang, comp or clip.width * 0.09, esp)
    shape.commit()
    for x, y, texto in rotulos:
        fs = max(14, clip.width / 32)
        p = fitz.Point(x - clip.x0, y - clip.y0)
        for dx, dy in ((-1.5, 0), (1.5, 0), (0, -1.5), (0, 1.5)):
            page.insert_text(p + (dx, dy), texto, fontsize=fs, fontname="helv", color=PRETO)
        page.insert_text(p, texto, fontsize=fs, fontname="helv", color=(1, 1, 1))
    zoom = (largura / clip.width) if largura else 1
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
    if saida.lower().endswith((".jpg", ".jpeg")):
        pix.save(saida, jpg_quality=86)  # foto: JPEG leve para o celular
    else:
        pix.save(saida)


def main(argv: list[str]) -> None:
    entrada, saida = argv[0], argv[1]
    setas, rotulos, recorte, largura = [], [], None, None
    i = 2
    while i < len(argv):
        k, v = argv[i], argv[i + 1]
        if k == "--seta":
            parts = [float(p) for p in v.split(",")]
            setas.append((parts[0], parts[1], parts[2], parts[3] if len(parts) > 3 else None))
        elif k == "--rotulo":
            x, y, t = v.split(",", 2)
            rotulos.append((float(x), float(y), t))
        elif k == "--recorte":
            recorte = [float(p) for p in v.split(",")]
        elif k == "--largura":
            largura = int(v)
        i += 2
    desenhar(entrada, saida, setas, rotulos, recorte, largura)
    print(saida)


if __name__ == "__main__":
    main(sys.argv[1:])
