#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gera manifesto visual v3 para IO manual, sem depender do AnkiConnect.

Serve para histologia/micrografia real, onde nao ha rotulos para OCR.

Uso:
  python flashcards/scripts/io_manual_from_image.py micro.png \
    --slug histo-11-hassall \
    --header "<b>Thymus</b> - identify the highlighted structure" \
    --box "Hassall corpuscle:420,310,80,65" \
    --box "Medulla:250,220,180,140"

O preview é apenas para auditoria. A imagem limpa e as máscaras semânticas são
consumidas pelo montador offline do deck.
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
    ap.add_argument("--source-type", required=True,
                    choices=["anking", "external_deck", "institutional", "slide"])
    ap.add_argument("--source-locator", required=True)
    ap.add_argument("--credit", required=True)
    ap.add_argument("--license-status", default="private-study-use")
    ap.add_argument("--mode", default="image_occlusion",
                    choices=["image_occlusion", "image_prompt"])
    ap.add_argument("--image-role", default="recognition",
                    choices=["recognition", "localization"])
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    img = Image.open(args.image).convert("RGB")
    labels = [parse_box(b) for b in args.box]
    width, height = img.size
    for label in labels:
        x, y, w, h = label["box"]
        if not label["text"]:
            ap.error("toda máscara exige rótulo")
        if x < 0 or y < 0 or w <= 0 or h <= 0 or x + w > width or y + h > height:
            ap.error(f"máscara fora da imagem: {label['box']} em {width}x{height}")

    buf = _io.BytesIO()
    img.save(buf, "PNG")
    image_hash = hashlib.sha256(buf.getvalue()).hexdigest()
    media_name = image_hash[:32] + ".png"
    crop_png = os.path.join(args.outdir, media_name)
    preview = os.path.join(args.outdir, args.slug + "-preview.png")
    manifest_path = os.path.join(args.outdir, args.slug + "-manifest.json")
    img.save(crop_png)
    draw_preview(img, labels, preview)

    masks = []
    for index, label in enumerate(labels, start=1):
        x, y, w, h = label["box"]
        masks.append({
            "id": f"mask-{index}",
            "label": label["text"],
            "box_px": [x, y, w, h],
            "box_normalized": [round(x / width, 6), round(y / height, 6),
                               round(w / width, 6), round(h / height, 6)],
        })
    manifest = {
        "visual_contract_version": "visual-v3",
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
        "mode": args.mode,
        "role": args.image_role,
        "masks": masks,
        "asset": {
            "file": crop_png,
            "preview": preview,
            "source_type": args.source_type,
            "source_locator": args.source_locator,
            "credit": args.credit,
            "license_status": args.license_status,
            "hash": image_hash,
            "answer_leakage": False,
        },
        "qa": {
            "target_visible_without_label": None,
            "mask_matches_label": None,
            "crop_has_context": None,
            "review_status": "pending",
        },
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"manifest -> {manifest_path}")
    print(f"preview -> {preview}")
    print(f"boxes -> {len(labels)}")


if __name__ == "__main__":
    main()
