#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Aplica o padrão canônico de negrito a cada cloze da árvore de Etimologia."""
from __future__ import annotations

import argparse
import re

from anki import call

QUERY = 'deck:"NEBLI::Etimologia"'
CLOZE_RE = re.compile(r"\{\{c\d+::.*?\}\}", re.S)


def bold_missing_clozes(text: str) -> str:
    def replace(match: re.Match) -> str:
        before = text[max(0, match.start() - 8):match.start()].casefold()
        after = text[match.end():match.end() + 9].casefold()
        if before.endswith("<b>") and after.startswith("</b>"):
            return match.group(0)
        if before.endswith("<strong>") and after.startswith("</strong>"):
            return match.group(0)
        return f"<b>{match.group(0)}</b>"
    return CLOZE_RE.sub(replace, text)


def main(apply: bool) -> int:
    ids = call("findNotes", query=QUERY)
    notes = call("notesInfo", notes=ids) if ids else []
    changes = [(n["noteId"], bold_missing_clozes(n["fields"]["Text"]["value"])) for n in notes]
    changes = [(note_id, text) for note_id, text in changes if text != next(n for n in notes if n["noteId"] == note_id)["fields"]["Text"]["value"]]
    print(f"notas na árvore: {len(notes)} | clozes a estilizar: {len(changes)}")
    if not apply:
        return 0
    actions = [{"action": "updateNoteFields", "params": {"note": {
        "id": note_id, "fields": {"Text": text}}}} for note_id, text in changes]
    for start in range(0, len(actions), 50):
        results = call("multi", actions=actions[start:start + 50])
        failures = [item for item in results if isinstance(item, dict) and item.get("error")]
        if failures:
            raise RuntimeError(f"falha ao aplicar negrito: {failures[:3]}")
    print(f"OK: {len(changes)} notas atualizadas.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    raise SystemExit(main(parser.parse_args().apply))
