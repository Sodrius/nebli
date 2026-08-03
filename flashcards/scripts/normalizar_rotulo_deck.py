#!/usr/bin/env python3
"""Prefixa em inglês o campo Text de todas as notas de um deck-aula."""
import argparse, json, urllib.request

THEMES = {"bioq": "Biochemistry", "anato": "Anatomy", "biocel": "Cell Biology", "biomol": "Molecular Biology", "embrio": "Embryology", "fisio": "Physiology", "histo": "Histology", "etim": "Etymology"}

def call(action, **params):
    req = urllib.request.Request("http://localhost:8765", json.dumps({"action": action, "version": 6, "params": params}).encode(), {"Content-Type": "application/json"})
    data = json.load(urllib.request.urlopen(req, timeout=60))
    if data.get("error"): raise RuntimeError(data["error"])
    return data["result"]

ap = argparse.ArgumentParser()
ap.add_argument("deck")
ap.add_argument("--slug", required=True)
a = ap.parse_args()
label = THEMES.get(a.slug.split("-", 1)[0], "Medicine")
ids = call("findNotes", query=f'deck:"{a.deck}"')
changed = 0
for note in call("notesInfo", notes=ids) if ids else []:
    fields = note["fields"]
    if "Text" not in fields: continue
    old = fields["Text"]["value"]
    if old.lstrip().startswith("<b>"): continue
    call("updateNoteFields", note={"id": note["noteId"], "fields": {"Text": f"<b>{label}.</b> {old}"}})
    changed += 1
print(f"OK: {changed} notas receberam <b>{label}.</b>; {len(ids)} notas no deck")
