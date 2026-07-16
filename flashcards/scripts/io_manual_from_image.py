#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gera manifest IO a partir de uma imagem e caixas manuais.

Serve para histologia/micrografia real, onde nao ha rotulos para OCR.

Uso:
  python flashcards/scripts/io_manual_from_image.py micro.png \
    --slug histo-11-hassall \
    --header "<b>Thymus</b> - identify the highlighted structure" \
    --box "Hassall corpuscle:420,310,80,65" \
    --box "Medulla:250,220,180,140"

Depois:
  python flashcards/scripts/io_apply.py arquivos-trabalho/io/histo-11-hassall-manifest.json \
    --deck "NEBLI::..." --tags "NEBLI::histo-11 NEBLI::gerado"
"""
import argparse
import hashlib
import io as _io
import json
import os
from PIL import Image, ImageDraw


def parse_box(raw):
    label, coords = raw.split(":", 1)
    x, y, w, h = [int(v.strip()) for v in coords.split(",")]
    return {"text": label.strip(), "box": [x, y, w, h]}


def emit_i0(labels):
    rects = []
    for lab in labels:
        x, y, w, h = lab["box"]
        rects.append(f"[[rect0::{x},{y},{w},{h}]]")
    return "[#!occlusions " + "<br>".join(rects) + " #]<br>active"


def draw_preview(img, labels, out):
    im = img.convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    for lab in labels:
        x, y, w, h = lab["box"]
        d.rectangle([x, y, x + w, y + h], fill=(255, 90, 90, 100), outline=(210, 0, 0, 255), width=2)
        d.text((x, max(0, y - 14)), lab["text"], fill=(210, 0, 0, 255))
    im.save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--header", required=True)
    ap.add_argument("--box", action="append", required=True, help='"Label:x,y,w,h"')
    ap.add_argument("--outdir", default="arquivos-trabalho/io")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    img = Image.open(args.image).convert("RGB")
    labels = [parse_box(b) for b in args.box]

    buf = _io.BytesIO()
    img.save(buf, "PNG")
    media_name = hashlib.md5(buf.getvalue()).hexdigest() + ".png"
    crop_png = os.path.join(args.outdir, media_name)
    preview = os.path.join(args.outdir, args.slug + "-preview.png")
    manifest_path = os.path.join(args.outdir, args.slug + "-manifest.json")
    img.save(crop_png)
    draw_preview(img, labels, preview)

    manifest = {
        "slug": args.slug,
        "header": args.header,
        "image_size": img.size,
        "n_boxes": len(labels),
        "labels": labels,
        "I0": emit_i0(labels),
        "media_name": media_name,
        "image_field": f'<img src="{media_name}">',
        "crop_png": crop_png,
        "preview_png": preview,
        "mode": "manual_histology",
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"manifest -> {manifest_path}")
    print(f"preview -> {preview}")
    print(f"boxes -> {len(labels)}")


if __name__ == "__main__":
    main()
