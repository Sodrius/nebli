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

from anki import call
from PIL import Image

MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"


def norm(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


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


def main(path, dry=False, require_images=False):
    spec = json.load(open(path, encoding="utf-8-sig"))
    deck, slug, cards = spec["deck"], spec["slug"], spec["cards"]
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
        text = c["text"]
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
            "options": {"allowDuplicate": False},
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
    a = ap.parse_args()
    main(a.json, a.dry, a.require_images)
