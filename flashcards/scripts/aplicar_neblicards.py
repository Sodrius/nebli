#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Aplica NEBLIcards autorais num deck NEBLI via AnkiConnect.

Compatibilidade: aceita o schema novo do build_card.py ({cards:[text]}) e
schemas legados ({cards:[texto/front/Text]} ou {gerados:[Text]}). Para cards com
imagem e credito, prefira build_card.py, que grava midia no padrao AnKing.

Idempotente: pula cards cujo campo Text ja existe no deck.
"""
import json
import re
import sys
import urllib.request

MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"


def call(action, **params):
    req = urllib.request.Request(
        "http://localhost:8765",
        json.dumps({"action": action, "version": 6, "params": params}).encode(),
        {"Content-Type": "application/json"},
    )
    r = json.load(urllib.request.urlopen(req))
    if r.get("error"):
        raise RuntimeError(f"{action}: {r['error']}")
    return r["result"]


def norm(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def get_cards(spec):
    if "cards" in spec:
        return spec["cards"]
    if "gerados" in spec:
        return spec["gerados"]
    raise SystemExit("Formato nao reconhecido: use cards[] ou gerados[].")


def card_text(c):
    return c.get("text") or c.get("texto") or c.get("front") or c.get("Text") or ""


def card_extra(c):
    return c.get("extra") or c.get("Extra") or ""


def main(path):
    spec = json.load(open(path, encoding="utf-8-sig"))
    deck = spec.get("deck")
    slug = spec.get("slug")
    if not slug:
        raise SystemExit("Campo obrigatorio ausente: slug")
    if not deck:
        deck = f"NEBLI::{slug}"
    cards = get_cards(spec)
    call("createDeck", deck=deck)

    existing = set()
    ids = call("findNotes", query=f'deck:"{deck}"')
    if ids:
        for n in call("notesInfo", notes=ids):
            f = n["fields"]
            if "Text" in f:
                existing.add(norm(f["Text"]["value"]))

    added, skipped, errs = 0, 0, []
    for c in cards:
        text = card_text(c)
        if not text:
            errs.append(("<empty>", "missing text/texto/front/Text"))
            continue
        if norm(text) in existing:
            skipped += 1
            continue
        note = {
            "deckName": deck,
            "modelName": MODEL,
            "fields": {"Text": text, "Extra": card_extra(c)},
            "tags": ["NEBLI::" + slug, "NEBLI::neblicard-autoral"],
            "options": {"allowDuplicate": False},
        }
        try:
            call("addNote", note=note)
            added += 1
        except Exception as e:
            errs.append((text[:60], str(e)))

    msg = f"[{slug}] deck='{deck}' -> +{added} novos, {skipped} pulados, {len(errs)} erros"
    print(msg.encode("ascii", "replace").decode())
    dups = sum(1 for _, e in errs if "duplicate" in e)
    other = [(t, e) for t, e in errs if "duplicate" not in e]
    if dups:
        print(f"  ({dups} eram duplicatas -> ja existem, ok)")
    for t, e in other:
        print("  ERRO:", t.encode("ascii", "replace").decode(), "::", e)
    return added


if __name__ == "__main__":
    main(sys.argv[1])
