#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gera manifesto visual v3 para IO manual, sem depender do AnkiConnect.

Serve para diagramas rotulados. A caixa deve cobrir o texto da resposta, nunca
a estrutura anatômica ou a pista morfológica que o aluno precisa reconhecer.

Uso:
  python flashcards/scripts/io_manual_from_image.py micro.png \
    --slug anato-exemplo-partes \
    --header "<b>Anatomy</b> - identify the labeled parts" \
    --label-box "Cervical part:420,310,80,20" \
    --label-box "Thoracic part:250,220,100,20" \
    --behavior hide_all_guess_all

O gerador cria preview de pergunta (rótulos cobertos) e de resposta. Ambos
precisam de revisão humana antes de o contrato marcar o IO como aprovado.
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


def draw_question_preview(img, labels, out):
    im = img.convert("RGB")
    d = ImageDraw.Draw(im)
    for lab in labels:
        x, y, w, h = lab["box"]
        d.rectangle([x, y, x + w, y + h], fill=(92, 101, 112), outline=(30, 35, 40), width=2)
    im.save(out)


def draw_answer_preview(img, labels, out):
    im = img.convert("RGB")
    d = ImageDraw.Draw(im)
    for index, lab in enumerate(labels, start=1):
        x, y, w, h = lab["box"]
        d.rectangle([x, y, x + w, y + h], outline=(0, 150, 80), width=3)
        d.text((x, max(0, y - 14)), str(index), fill=(0, 110, 55))
    im.save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--header", required=True)
    ap.add_argument("--label-box", action="append", required=True,
                    help='caixa do texto-resposta: "Label:x,y,w,h"')
    ap.add_argument("--outdir", default="arquivos-trabalho/io")
    ap.add_argument("--source-type", required=True,
                    choices=["anking", "external_deck", "institutional", "slide"])
    ap.add_argument("--source-locator", required=True)
    ap.add_argument("--credit", required=True)
    ap.add_argument("--license-status", default="private_only",
                    choices=["open_ok", "noncommercial_ok", "private_only", "internal"])
    ap.add_argument("--behavior", default="hide_all_guess_all",
                    choices=["hide_all_guess_all", "hide_one_guess_one"])
    ap.add_argument("--image-role", default="recognition",
                    choices=["recognition", "localization"])
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    img = Image.open(args.image).convert("RGB")
    labels = [parse_box(b) for b in args.label_box]
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
    question_preview = os.path.join(args.outdir, args.slug + "-question.png")
    answer_preview = os.path.join(args.outdir, args.slug + "-answer.png")
    manifest_path = os.path.join(args.outdir, args.slug + "-manifest.json")
    img.save(crop_png)
    draw_question_preview(img, labels, question_preview)
    draw_answer_preview(img, labels, answer_preview)

    masks = []
    for index, label in enumerate(labels, start=1):
        x, y, w, h = label["box"]
        masks.append({
            "id": f"mask-{index}",
            "label": label["text"],
            "box_px": [x, y, w, h],
            "covers": "answer_label",
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
        "question_preview": question_preview,
        "answer_preview": answer_preview,
        "mode": "image_occlusion",
        "behavior": args.behavior,
        "target_kind": "answer_labels",
        "mask_policy": "cover_answer_label_not_visual_target",
        "role": args.image_role,
        "masks": masks,
        "asset": {
            "file": crop_png,
            "preview": question_preview,
            "source_type": args.source_type,
            "source_locator": args.source_locator,
            "credit": args.credit,
            "license_status": args.license_status,
            "hash": image_hash,
            "answer_leakage": False,
        },
        "qa": {
            "masks_cover_answer_labels": None,
            "visual_clues_remain_visible": None,
            "all_answers_hidden": None,
            "all_duplicate_labels_masked": None,
            "question_preview_reviewed": None,
            "answer_preview_reviewed": None,
            "review_status": "pending",
        },
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"manifest -> {manifest_path}")
    print(f"question preview -> {question_preview}")
    print(f"answer preview -> {answer_preview}")
    print(f"boxes -> {len(labels)}")


if __name__ == "__main__":
    main()
