#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copia cards de decks externos (BlueLink/Dope/Histology/LLU) para um deck NEBLI.

Uso tipico:
  python flashcards/scripts/copiar_externos_para_deck.py \
    --source BlueLink --tag "BlueLink::Heart" \
    --deck "NEBLI::UC02::P3::Anatomia::Circulatorio I" \
    --slug anato-05-circulatorio-linfatico-I --dry-run

  python flashcards/scripts/copiar_externos_para_deck.py \
    --source Dope --query 'deck:"Referencias Externas::Dope Anatomy" tag:Dope::Anatomy::Thorax' \
    --deck "NEBLI::UC02::P3::Anatomia::Circulatorio I" \
    --slug anato-05-circulatorio-linfatico-I

Principio:
  - original externo fica intocado;
  - a copia preserva note type, campos, imagens e tags de origem;
  - a copia ganha tags NEBLI::<slug>, NEBLI::externo e NEBLI::<source>;
  - o gate de conteudo continua manual/curatorial: copie so o que esta na E1.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from nebli_anki import call  # noqa: E402


def norm_html(s):
    return re.sub(r"<[^>]+>", "", s or "").replace("\u200b", "").strip()


def first_field(note):
    fields = note.get("fields", {})
    if not fields:
        return ""
    return next(iter(fields.values())).get("value", "")


def build_query(args):
    if args.query:
        return args.query
    if args.tag:
        return f'"tag:{args.tag}" OR "tag:{args.tag}::*"'
    raise SystemExit("Use --query ou --tag.")


def chunked(xs, n=100):
    for i in range(0, len(xs), n):
        yield xs[i : i + n]


def load_notes(query, limit):
    note_ids = call("findNotes", query=query)
    if limit:
        note_ids = note_ids[:limit]
    notes = []
    for chunk in chunked(note_ids):
        notes.extend(call("notesInfo", notes=chunk))
    return notes


def existing_texts(deck):
    ids = call("findNotes", query=f'deck:"{deck}"')
    out = set()
    for chunk in chunked(ids):
        for note in call("notesInfo", notes=chunk):
            out.add(norm_html(first_field(note)))
    return out


def copy_note(note, deck, tags, allow_duplicate):
    fields = {name: val["value"] for name, val in note["fields"].items()}
    note_tags = list(dict.fromkeys(note.get("tags", []) + tags))
    payload = {
        "deckName": deck,
        "modelName": note["modelName"],
        "fields": fields,
        "tags": note_tags,
        "options": {"allowDuplicate": allow_duplicate},
    }
    return call("addNote", note=payload)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="BlueLink, Dope, Histology, LLU, Dorian...")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--deck", required=True)
    ap.add_argument("--tag", help="Tag externa. Ex.: BlueLink::Heart")
    ap.add_argument("--query", help="Busca AnkiConnect completa, se tag nao bastar")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--allow-duplicate", action="store_true")
    ap.add_argument("--manifest", help="Opcional: salva ids copiados/candidatos em JSON")
    args = ap.parse_args()

    query = build_query(args)
    tags = [f"NEBLI::{args.slug}", "NEBLI::externo", f"NEBLI::{args.source}"]

    print(f"query: {query}")
    notes = load_notes(query, args.limit or None)
    print(f"candidatos: {len(notes)}")
    if not notes:
        return

    existing = existing_texts(args.deck)
    rows = []
    for note in notes:
        text = norm_html(first_field(note))
        rows.append(
            {
                "noteId": note["noteId"],
                "modelName": note["modelName"],
                "first": text[:140],
                "already_in_target": bool(text and text in existing),
                "tags": note.get("tags", []),
            }
        )

    for i, row in enumerate(rows[:30], 1):
        marker = "dup" if row["already_in_target"] else "new"
        print(f"{i:03d} [{marker}] {row['modelName']} :: {row['first']}")
    if len(rows) > 30:
        print(f"... {len(rows) - 30} restantes omitidos no preview")

    created = []
    skipped = 0
    if not args.dry_run:
        call("createDeck", deck=args.deck)
        for note, row in zip(notes, rows):
            if row["already_in_target"] and not args.allow_duplicate:
                skipped += 1
                continue
            nid = copy_note(note, args.deck, tags, args.allow_duplicate)
            created.append(nid)
        if created:
            card_ids = []
            for nid in created:
                card_ids.extend(call("findCards", query=f"nid:{nid}"))
            if card_ids:
                call("unsuspend", cards=card_ids)

    print(f"criados: {len(created)} | pulados: {skipped} | dry_run={args.dry_run}")

    if args.manifest:
        manifest = {
            "source": args.source,
            "slug": args.slug,
            "deck": args.deck,
            "query": query,
            "tags_added": tags,
            "dry_run": args.dry_run,
            "created_note_ids": created,
            "candidates": rows,
        }
        Path(args.manifest).write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"manifest -> {args.manifest}")


if __name__ == "__main__":
    main()
