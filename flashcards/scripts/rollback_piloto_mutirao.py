#!/usr/bin/env python3
"""Restaura o estado anterior à promoção do piloto."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from nebli_anki import call


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("promotion", type=Path)
    args = parser.parse_args()
    promotion = json.loads(args.promotion.read_text(encoding="utf-8-sig"))
    before_path = Path(promotion["before_snapshot"])
    if not before_path.is_absolute():
        before_path = Path.cwd() / before_path
    before = json.loads(before_path.read_text(encoding="utf-8-sig"))

    created = promotion.get("created_note_ids", [])
    if created:
        call("deleteNotes", notes=created)
    for note in before["notes"]:
        nid = note["note_id"]
        call("updateNoteFields", note={"id": nid, "fields": note["fields"]})
        current = call("notesInfo", notes=[nid])[0].get("tags", [])
        if current:
            call("removeTags", notes=[nid], tags=" ".join(current))
        if note["tags"]:
            call("addTags", notes=[nid], tags=" ".join(note["tags"]))
    originally_suspended = {c["card_id"] for c in before["cards"] if c["queue"] == -1}
    all_original = [c["card_id"] for c in before["cards"]]
    if all_original:
        call("unsuspend", cards=all_original)
    if originally_suspended:
        call("suspend", cards=sorted(originally_suspended))
    print(json.dumps({"restored_notes": len(before["notes"]), "deleted_created_notes": len(created)}))


if __name__ == "__main__":
    main()
