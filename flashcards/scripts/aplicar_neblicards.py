#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Aplica NEBLIcards autorais (PT, craft AnKing) num deck NEBLI via AnkiConnect.
Entrada: JSON {deck, slug, cards:[{text, extra?}]}. Modelo AnKingOverhaul.
Idempotente: pula cards cujo campo Text já existe no deck (casa por texto bruto)."""
import json, sys, urllib.request, re

def call(action, **params):
    req = urllib.request.Request("http://localhost:8765",
        json.dumps({"action": action, "version": 6, "params": params}).encode(),
        {'Content-Type': 'application/json'})
    r = json.load(urllib.request.urlopen(req))
    if r.get('error'): raise RuntimeError(f"{action}: {r['error']}")
    return r['result']

MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"

def norm(s):
    return re.sub(r'<[^>]+>', '', s or '').strip()

def main(path):
    spec = json.load(open(path, encoding='utf-8'))
    deck, slug, cards = spec['deck'], spec['slug'], spec['cards']
    call("createDeck", deck=deck)
    # cards existentes no deck -> pular duplicata por texto sem tags html
    existing = set()
    ids = call("findNotes", query=f'deck:"{deck}"')
    if ids:
        for n in call("notesInfo", notes=ids):
            f = n['fields']
            if 'Text' in f:
                existing.add(norm(f['Text']['value']))
    added, skipped, errs = 0, 0, []
    for c in cards:
        if norm(c['text']) in existing:
            skipped += 1; continue
        note = {"deckName": deck, "modelName": MODEL,
                "fields": {"Text": c['text'], "Extra": c.get('extra', '')},
                "tags": ["NEBLI::"+slug, "NEBLI::neblicard-autoral"],
                "options": {"allowDuplicate": False}}
        try:
            call("addNote", note=note); added += 1
        except Exception as e:
            errs.append((c['text'][:60], str(e)))
    msg = f"[{slug}] deck='{deck}' -> +{added} novos, {skipped} pulados (ja existiam), {len(errs)} erros"
    print(msg.encode('ascii', 'replace').decode())
    dups = sum(1 for _, e in errs if 'duplicate' in e)
    other = [(t, e) for t, e in errs if 'duplicate' not in e]
    if dups: print(f"  ({dups} eram duplicatas -> ja existem, ok)")
    for t, e in other: print("  ERRO:", t.encode('ascii','replace').decode(), "::", e)
    return added

if __name__ == "__main__":
    main(sys.argv[1])
