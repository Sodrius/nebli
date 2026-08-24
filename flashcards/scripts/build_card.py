#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build NEBLI-authored AnKingOverhaul cloze notes.

Canonical shape:
  - English Text by default, AnKing-like cloze syntax.
  - Short Extra plus explanatory image for most cards.
  - Image per subtopic/cluster, content-hashed media filename, real credit.
  - No visible "source"/course provenance in the card body.

Input JSON:
{
  "deck": "NEBLI::UC02::P3::...",
  "slug": "histo-10-tecido-nervoso",
  "images": {
     "neuron": {"file": "arquivos-trabalho/io/....png",
                 "credit": "Photo credit: OpenStax, CC BY 4.0"},
     "nerve":  {"url": "https://...jpg", "credit": "..."}
  },
  "cards": [
     {"text": "The ... {{c1::kinesin}} ...", "extra": "short why", "image": "neuron"}
  ]
}
"""
import argparse
import base64
import hashlib
import io as _io
import json
import os
import re
import sys

from nebli_anki import call
from PIL import Image

MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"
THEME_BY_SLUG = {
    "anato": "Anatomy", "biocel": "Cell Biology", "biomol": "Molecular Biology",
    "bioq": "Biochemistry", "embrio": "Embryology", "fisio": "Physiology",
    "histo": "Histology", "etim": "Etymology",
}
THEME_RE = re.compile(r"^<b>([^<.]+)\.</b>\s+")
CLOZE_RE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}")
BOLDED_CLOZE_RE = re.compile(r"<(?:b|strong)>\s*\{\{c\d+::.*?\}\}\s*</(?:b|strong)>", re.I)


def norm(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def infer_theme(slug, explicit=None):
    if explicit:
        label = explicit.strip().rstrip(".")
    else:
        label = THEME_BY_SLUG.get((slug or "").split("-", 1)[0], "")
    if not label or len(label.split()) > 2:
        raise ValueError("theme_label obrigatório, neutro e com 1–2 palavras")
    return label


def themed_text(text, label):
    if THEME_RE.match(text or ""):
        return text
    return f"<b>{label}.</b> {text.strip()}"


def validate_text_gate(text, label):
    match = THEME_RE.match(text or "")
    if not match or match.group(1) != label:
        raise ValueError("Text sem rótulo temático canônico")
    answers = CLOZE_RE.findall(text or "")
    if not answers:
        raise ValueError("Text sem cloze")
    if len(BOLDED_CLOZE_RE.findall(text or "")) != len(answers):
        raise ValueError("todo cloze deve estar em negrito")
    label_words = {x.lower() for x in re.findall(r"\w+", label)}
    answer_words = {x.lower() for a in answers for x in re.findall(r"\w+", norm(a))}
    if label_words & answer_words:
        raise ValueError("rótulo temático dá pista da resposta")
    for answer in answers:
        if len(re.findall(r"\S+", norm(answer))) > 3:
            raise ValueError("cloze com mais de 3 palavras")


def fetch_bytes(spec):
    if spec.get("file"):
        return open(spec["file"], "rb").read(), os.path.splitext(spec["file"])[1] or ".png"
    if spec.get("url"):
        import requests
        r = requests.get(spec["url"], timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        ext = os.path.splitext(spec["url"].split("?")[0])[1] or ".jpg"
        return r.content, ext
    raise ValueError("image spec needs file or url")


def store_images(images, maxw=700):
    """Store images in Anki media and return HTML snippets keyed by image id."""
    out = {}
    for key, spec in (images or {}).items():
        raw, _ext = fetch_bytes(spec)
        im = Image.open(_io.BytesIO(raw)).convert("RGB")
        if im.width > maxw:
            im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
        buf = _io.BytesIO()
        im.save(buf, "PNG")
        data = buf.getvalue()
        fn = f"{hashlib.md5(data).hexdigest()}.png"
        call("storeMediaFile", filename=fn, data=base64.b64encode(data).decode())
        width = min(im.width, 520)
        credit = spec.get("credit", "").strip()
        cred_html = f'<br><i style="font-size:10pt;">{credit}</i>' if credit else ""
        out[key] = {"img": f'<img src="{fn}" width="{width}">', "credit": cred_html, "file": fn}
    return out


def build_extra(extra_text, imginfo):
    parts = []
    if extra_text:
        parts.append(extra_text)
    if imginfo:
        src = re.search(r'\bsrc=["\']([^"\']+)', imginfo["img"], re.I)
        existing = set(re.findall(r'<img[^>]+\bsrc=["\']([^"\']+)', extra_text or "", re.I))
        if not src or src.group(1) not in existing:
            parts.append(imginfo["img"] + imginfo["credit"])
    return "<br><br>".join(parts)


def main(path, dry=False, require_images=False, canonical=False):
    with open(path, encoding="utf-8-sig") as source:
        spec = json.load(source)
    # Specs novas tornam o contrato impossível de esquecer. A opção --canonical
    # também permite auditar deliberadamente um lote antes da primeira importação.
    if canonical or spec.get("pipeline_contract") == "e1-e2-v1":
        from e1_e2_contract import validate_spec
        result = validate_spec(spec, os.path.dirname(os.path.abspath(path)))
        if result["errors"]:
            raise SystemExit("Contrato E1->card->E2 reprovado:\n- " + "\n- ".join(result["errors"]))
        for warning in result["warnings"]:
            print("AVISO contrato:", warning)
    deck, slug, cards = spec["deck"], spec["slug"], spec["cards"]
    theme = infer_theme(slug, spec.get("theme_label"))
    if require_images:
        missing = [i + 1 for i, c in enumerate(cards) if not c.get("image")]
        if missing:
            raise SystemExit(f"Cards sem image=... com --require-images: {missing}")
    imgs = {} if dry else store_images(spec.get("images"))
    if not dry:
        call("createDeck", deck=deck)
    existing = set()
    ids = call("findNotes", query=f'deck:"{deck}"') if not dry else []
    if ids:
        for n in call("notesInfo", notes=ids):
            f = n["fields"]
            if "Text" in f:
                existing.add(norm(f["Text"]["value"]))
    added = skipped = 0
    errs = []
    for c in cards:
        text = themed_text(c["text"], theme)
        validate_text_gate(text, theme)
        if norm(text) in existing:
            skipped += 1
            continue
        imginfo = imgs.get(c.get("image")) if c.get("image") else None
        extra = build_extra(c.get("extra", ""), imginfo)
        tags = ["NEBLI::" + slug, "NEBLI::neblicard-autoral", "NEBLI::en"]
        tags.append("NEBLI::image_extra" if imginfo else "NEBLI::needs_image")
        note = {
            "deckName": deck,
            "modelName": MODEL,
            "fields": {"Text": text, "Extra": extra},
            "tags": tags,
            "options": {"allowDuplicate": True},
        }
        if dry:
            added += 1
            continue
        try:
            call("addNote", note=note)
            added += 1
        except Exception as e:
            errs.append((text[:50], str(e)))
    msg = f"[{slug}] +{added} novos, {skipped} pulados, {len(errs)} erros"
    print(msg.encode("ascii", "replace").decode())
    for t, e in errs:
        if "duplicate" not in e:
            print("  ERRO:", t.encode("ascii", "replace").decode(), "::", e)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--require-images", action="store_true", help="fail if any card lacks image")
    ap.add_argument("--canonical", action="store_true", help="exige contrato E1->card->E2 e decisão visual")
    a = ap.parse_args()
    main(a.json, a.dry, a.require_images, a.canonical)
