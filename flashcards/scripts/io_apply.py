#!/usr/bin/env python
"""
io_apply.py — cria a nota IO no Anki a partir de um manifest do io_from_slide.py.
storeMediaFile (imagem hasheada) + addNote (note type IO-one by one).

Uso:
  python io_apply.py <manifest.json> --deck "NEBLI::UC02::P3::..." \
        --tags "NEBLI::UC02::P3::... NEBLI::gerado" [--extra "<...>"] [--dry]
"""
import argparse, base64, json, os, sys
from anki import call

MODEL = "IO-one by one (AnKing Step Deck / AnKingMed)"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--deck", required=True)
    ap.add_argument("--tags", default="NEBLI::gerado")
    ap.add_argument("--extra", default="")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()

    m = json.load(open(a.manifest, encoding="utf-8"))
    media_name = m["media_name"]
    crop_png = m["crop_png"]

    fields = {"Image": m["image_field"], "Header": m["header"],
              "I0": m["I0"], "Extra": a.extra,
              "Personal Notes": "", "Missed Questions": ""}
    tags = a.tags.split()

    print(f"deck: {a.deck}")
    print(f"model: {MODEL}")
    print(f"media: {media_name}  (n_boxes={m['n_boxes']})")
    print(f"tags: {tags}")
    if a.dry:
        print("[dry-run] nada aplicado."); return

    # garante o deck
    call("createDeck", deck=a.deck)
    # sobe a imagem
    with open(crop_png, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    call("storeMediaFile", filename=media_name, data=b64)
    note = {"deckName": a.deck, "modelName": MODEL, "fields": fields,
            "tags": tags, "options": {"allowDuplicate": False}}
    nid = call("addNote", note=note)
    print(f"nota criada: {nid}")

if __name__ == "__main__":
    main()
