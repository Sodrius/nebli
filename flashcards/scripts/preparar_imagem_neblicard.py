#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Prepara imagem de NEBLIcard no PADRAO AnKing: recorta bordas uniformes e
redimensiona para ~1080px de largura (mediana medida no deck AnKing).
Uso: python preparar_imagem_neblicard.py <slug> <slide-XX.png> [alvo_w=1080]
Emite figuras/<slug>/_neblicard/<slide>.png e imprime o caminho."""
import sys, os
from PIL import Image, ImageChops
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    return im.crop(bbox) if bbox else im

def prep(slug, slide, alvo_w=1080):
    src = os.path.join(ROOT, "figuras", slug, slide)
    im = Image.open(src).convert("RGB")
    im = trim(im)
    if im.width > alvo_w:
        h = round(im.height * alvo_w / im.width)
        im = im.resize((alvo_w, h), Image.LANCZOS)
    outdir = os.path.join(ROOT, "figuras", slug, "_neblicard")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, slide)
    im.save(out, "PNG", optimize=True)
    print("%s -> %dx%d  %s" % (slide, im.width, im.height, out))
    return out

if __name__ == "__main__":
    prep(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv)>3 else 1080)
