#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""build_card.py — cria NEBLIcards nível AnKing: INGLÊS, Extra telegráfico COM
IMAGEM (imagem-mãe reusada pelo cluster + linha de crédito), modelo AnKingOverhaul.

Padrão obrigatório (memory regras-neblicard-anking-nivel):
  - idioma EN
  - Extra = fragmento telegráfico + <img> (essencial) + <i>credit</i>
  - imagem-mãe: um arquivo por cluster, reusado; nome hasheado (assinatura AnKing)
  - crédito casado com a fonte real

Entrada JSON:
{
  "deck": "NEBLI::UC02::P3::...",
  "slug": "histo-10-tecido-nervoso",
  "images": {
     "neuron": {"file": "arquivos-trabalho/io/....png",
                "credit": "Photo credit: OpenStax, CC BY 4.0"},
     "nerve":  {"url": "https://...jpg", "credit": "..."}
  },
  "cards": [
     {"text": "The ... {{c1::kinesin}} ...", "extra": "telegraphic why", "image": "neuron"},
     {"text": "...", "extra": "...", "image": null}
  ]
}
Idempotente: pula card cujo campo Text já existe no deck.
"""
import argparse, base64, hashlib, json, os, re, sys, io as _io
from anki import call
from PIL import Image

MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"

def norm(s):
    return re.sub(r'<[^>]+>', '', s or '').strip()

def fetch_bytes(spec):
    if spec.get("file"):
        return open(spec["file"], "rb").read(), os.path.splitext(spec["file"])[1] or ".png"
    if spec.get("url"):
        import requests
        r = requests.get(spec["url"], timeout=30,
                         headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        ext = os.path.splitext(spec["url"].split("?")[0])[1] or ".jpg"
        return r.content, ext
    raise ValueError("image spec needs file or url")

def store_images(images, maxw=600):
    """Armazena cada imagem no Anki media com nome hasheado; devolve o <img>+credit."""
    out = {}
    for key, spec in (images or {}).items():
        raw, ext = fetch_bytes(spec)
        # normaliza p/ largura AnKing (<=600) e re-encoda PNG p/ hash estável
        im = Image.open(_io.BytesIO(raw)).convert("RGB")
        if im.width > maxw:
            im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
        buf = _io.BytesIO(); im.save(buf, "PNG")
        data = buf.getvalue()
        md5 = hashlib.md5(data).hexdigest()
        fn = f"{md5}.png"
        call("storeMediaFile", filename=fn, data=base64.b64encode(data).decode())
        w = min(im.width, 400)
        credit = spec.get("credit", "").strip()
        cred_html = f'<br><i style="font-size:10pt;">{credit}</i>' if credit else ""
        out[key] = {"img": f'<img src="{fn}" width="{w}">', "credit": cred_html, "file": fn}
    return out

def build_extra(extra_text, imginfo):
    parts = []
    if extra_text:
        parts.append(extra_text)
    if imginfo:
        parts.append(imginfo["img"] + imginfo["credit"])
    return "<br><br>".join(parts)

def main(path, dry=False):
    spec = json.load(open(path, encoding='utf-8'))
    deck, slug, cards = spec['deck'], spec['slug'], spec['cards']
    imgs = {} if dry else store_images(spec.get("images"))
    if not dry:
        call("createDeck", deck=deck)
    existing = set()
    ids = call("findNotes", query=f'deck:"{deck}"') if not dry else []
    if ids:
        for n in call("notesInfo", notes=ids):
            f = n['fields']
            if 'Text' in f: existing.add(norm(f['Text']['value']))
    added = skipped = 0; errs = []
    for c in cards:
        if norm(c['text']) in existing:
            skipped += 1; continue
        imginfo = imgs.get(c.get("image")) if c.get("image") else None
        extra = build_extra(c.get("extra", ""), imginfo)
        note = {"deckName": deck, "modelName": MODEL,
                "fields": {"Text": c['text'], "Extra": extra},
                "tags": ["NEBLI::" + slug, "NEBLI::neblicard-autoral", "NEBLI::en"],
                "options": {"allowDuplicate": False}}
        if dry:
            added += 1; continue
        try:
            call("addNote", note=note); added += 1
        except Exception as e:
            errs.append((c['text'][:50], str(e)))
    msg = f"[{slug}] +{added} novos, {skipped} pulados, {len(errs)} erros"
    print(msg.encode('ascii', 'replace').decode())
    for t, e in errs:
        if 'duplicate' not in e:
            print("  ERRO:", t.encode('ascii','replace').decode(), "::", e)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    main(a.json, a.dry)
