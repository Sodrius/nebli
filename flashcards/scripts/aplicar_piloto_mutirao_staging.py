#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Materializa o manifesto do piloto em deck de staging, sem tocar nos originais."""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import json
from pathlib import Path

from nebli_anki import call


def fields_plain(note: dict) -> dict[str, str]:
    return {name: value.get("value", "") for name, value in note.get("fields", {}).items()}


def set_text(fields: dict[str, str], value: str) -> None:
    for name in ("Text", "Texto", "Front", "Question", "Pergunta", "Cloze"):
        if name in fields:
            fields[name] = value
            return
    raise RuntimeError("note type sem campo textual reconhecido")


def set_extra(fields: dict[str, str], value: str) -> None:
    for name in ("Extra", "Remarks", "Back Extra", "Explicacao", "Explicação"):
        if name in fields:
            fields[name] = value
            return


def clone_note(source: dict, deck: str, tags: list[str], text: str | None = None, extra: str | None = None) -> int:
    fields = fields_plain(source)
    if text is not None:
        set_text(fields, text)
    if extra is not None:
        set_extra(fields, extra)
    return call("addNote", note={
        "deckName": deck,
        "modelName": source["modelName"],
        "fields": fields,
        "tags": sorted(set(source.get("tags", []) + tags)),
        "options": {"allowDuplicate": True},
    })


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    deck = manifest["target_deck"]
    call("createDeck", deck=deck)

    source_ids = {n["source_note_id"] for n in manifest["notes"]}
    replacement_ids = {rid for n in manifest["notes"] for rid in n.get("replacement_note_ids", [])}
    all_ids = sorted(source_ids | replacement_ids)
    info = {n["noteId"]: n for n in call("notesInfo", notes=all_ids)}
    missing = sorted(set(all_ids) - set(info))
    if missing:
        raise RuntimeError(f"notes ausentes no Anki: {missing}")

    media_name = None
    media_path = args.manifest.parent / "assets" / "Gray770-en-1280.png"
    if media_path.exists():
        raw = media_path.read_bytes()
        media_name = hashlib.sha256(raw).hexdigest()[:32] + ".png"
        call("storeMediaFile", filename=media_name, data=base64.b64encode(raw).decode("ascii"))

    created = []
    for item in manifest["notes"]:
        sid = item["source_note_id"]
        action = item["action"]
        base_tags = ["NEBLI::mutirao_piloto", "NEBLI::staging", f"NEBLI::mutirao_action::{action}", f"NEBLI::source_note::{sid}"]
        existing = call("findNotes", query=f'tag:"NEBLI::source_note::{sid}" deck:"{deck}"')
        if existing:
            created.append({"source_note_id": sid, "action": action, "staging_note_ids": existing, "status": "existing"})
            continue
        ids = []
        if action in {"rewrite", "replace_and_rewrite"}:
            ids.append(clone_note(info[sid], deck, base_tags, item["new_text"], item["new_extra"]))
        elif action in {"keep_control", "keep_with_credit_fix"}:
            source = info[sid]
            extra = None
            if action == "keep_with_credit_fix":
                extra = ('Photo credit: BruceBlaus, "Blausen 0657 MultipolarNeuron", CC BY 3.0, via Wikimedia Commons. '
                         'https://commons.wikimedia.org/wiki/File:Blausen_0657_MultipolarNeuron.png')
            ids.append(clone_note(source, deck, base_tags, extra=extra))
        elif action == "split":
            for index, card in enumerate(item["new_cards"], 1):
                extra = card["extra"]
                if media_name:
                    extra += (f'<br><img src="{media_name}"><br>'
                              'Image: Mysid, based on Gray\'s Anatomy plate 770; public domain, via Wikimedia Commons.')
                ids.append(clone_note(info[sid], deck, base_tags + [f"NEBLI::split_part::{index}"], card["text"], extra))
        elif action == "replace":
            pass
        else:
            raise RuntimeError(f"action desconhecida: {action}")

        for rid in item.get("replacement_note_ids", []):
            replacement_tags = base_tags + ["NEBLI::reference_copy", f"NEBLI::source_real::{rid}"]
            ids.append(clone_note(info[rid], deck, replacement_tags))
        created.append({"source_note_id": sid, "action": action, "staging_note_ids": ids, "status": "created"})

    output = args.output or args.manifest.with_name("STAGING-APLICACAO-2026-07-15.json")
    payload = {"generated_at": dt.datetime.now().astimezone().isoformat(), "deck": deck, "created": created}
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)
    print(f"notes materializadas: {sum(len(x['staging_note_ids']) for x in created)}")


if __name__ == "__main__":
    main()
