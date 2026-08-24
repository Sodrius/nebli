#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Garante o rótulo visual <b>Etimologia.</b> em toda a árvore do deck."""
from __future__ import annotations

import argparse
from pathlib import Path

from nebli_anki import call

QUERY = 'deck:"NEBLI::Etimologia"'
LABEL = "<b>Etimologia.</b> "


def chunks(items: list, size: int) -> list[list]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def main(apply: bool) -> int:
    note_ids = call("findNotes", query=QUERY)
    notes = call("notesInfo", notes=note_ids) if note_ids else []
    missing = [n for n in notes if not n["fields"]["Text"]["value"].startswith(LABEL)]
    print(f"notas na árvore: {len(notes)} | sem rótulo: {len(missing)}")
    if not apply:
        return 0
    actions = [{
        "action": "updateNoteFields",
        "params": {"note": {"id": n["noteId"], "fields": {
            "Text": LABEL + n["fields"]["Text"]["value"]}}},
    } for n in missing]
    for part in chunks(actions, 50):
        results = call("multi", actions=part)
        failures = [r for r in results if isinstance(r, dict) and r.get("error")]
        if failures:
            raise RuntimeError(f"falha ao aplicar rótulos: {failures[:3]}")
    updated = call("notesInfo", notes=[n["noteId"] for n in missing]) if missing else []
    if any(not n["fields"]["Text"]["value"].startswith(LABEL) for n in updated):
        raise RuntimeError("verificação do rótulo falhou")
    print(f"OK: rótulo aplicado a {len(missing)} notas.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    raise SystemExit(main(parser.parse_args().apply))
