#!/usr/bin/env python3
"""Build a local search index from a private Anki package.

The output deliberately stays outside version control. It retains enough note,
card, deck, tag and media metadata to curate real cards without loading a 6 GB
package for every lesson.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

from apkg_utils import decks_map, media_references, models_map, note_fields, open_collection


SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE notes (
  nid INTEGER PRIMARY KEY, guid TEXT NOT NULL, model_id INTEGER NOT NULL,
  model_name TEXT NOT NULL, tags TEXT NOT NULL, fields_json TEXT NOT NULL,
  searchable_text TEXT NOT NULL, media_json TEXT NOT NULL
);
CREATE TABLE cards (
  cid INTEGER PRIMARY KEY, nid INTEGER NOT NULL, deck_id INTEGER NOT NULL,
  deck_name TEXT NOT NULL, ordinal INTEGER NOT NULL, queue INTEGER NOT NULL,
  type INTEGER NOT NULL
);
CREATE INDEX notes_guid ON notes(guid);
CREATE INDEX notes_model ON notes(model_name);
CREATE INDEX cards_note ON cards(nid);
CREATE INDEX cards_deck ON cards(deck_name);
CREATE VIRTUAL TABLE notes_fts USING fts5(
  searchable_text,
  tokenize='unicode61 remove_diacritics 2'
);
"""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_index(apkg: Path, output: Path) -> dict:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    target = sqlite3.connect(output)
    try:
        target.executescript(SCHEMA)
        with open_collection(apkg) as (source, _package, media_map, member):
            models = models_map(source)
            decks = decks_map(source)
            model_names = {key: value.get("name", str(key)) for key, value in models.items()}
            deck_names = {key: value.get("name", str(key)) for key, value in decks.items()}
            note_count = 0
            for row in source.execute("SELECT id, guid, mid, tags, flds FROM notes"):
                fields = note_fields(row["flds"])
                refs = sorted(media_references(fields))
                target.execute(
                    "INSERT INTO notes VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (row["id"], row["guid"], row["mid"], model_names.get(row["mid"], str(row["mid"])),
                     row["tags"] or "", json.dumps(fields, ensure_ascii=False),
                     " \n".join(fields), json.dumps(refs, ensure_ascii=False)),
                )
                target.execute(
                    "INSERT INTO notes_fts(rowid, searchable_text) VALUES (?, ?)",
                    (row["id"], " \n".join(fields) + " \n" + (row["tags"] or "") +
                     " \n" + model_names.get(row["mid"], str(row["mid"]))),
                )
                note_count += 1
            card_count = 0
            for row in source.execute("SELECT id, nid, did, ord, queue, type FROM cards"):
                target.execute(
                    "INSERT INTO cards VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (row["id"], row["nid"], row["did"], deck_names.get(row["did"], str(row["did"])),
                     row["ord"], row["queue"], row["type"]),
                )
                card_count += 1
            metadata = {
                "format": "nebli-private-anki-index-v2-fts5",
                "source_file": apkg.name,
                "source_sha256": sha256(apkg),
                "collection_member": member,
                "notes": str(note_count),
                "cards": str(card_count),
                "media_entries": str(len(media_map)),
            }
            target.executemany("INSERT INTO metadata VALUES (?, ?)", metadata.items())
        target.commit()
    finally:
        target.close()
    return {"passed": True, "index": str(output), **metadata}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apkg", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.apkg.is_file():
        parser.error(f"APKG inexistente: {args.apkg}")
    try:
        result = build_index(args.apkg.resolve(), args.output.resolve())
    except Exception as exc:
        print(json.dumps({"passed": False, "error": str(exc)}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
