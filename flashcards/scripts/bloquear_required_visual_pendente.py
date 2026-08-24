#!/usr/bin/env python3
"""Suspende cards required sem aprovação visual; nunca os apaga."""
from __future__ import annotations
import argparse
import datetime as dt
import json
from pathlib import Path
from nebli_anki import call

parser = argparse.ArgumentParser()
parser.add_argument("--query", default="deck:NEBLI::* -deck:NEBLI::STAGING::*")
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
q = f"{args.query} tag:NEBLI::visual_need::required -tag:NEBLI::image_status::approved"
note_ids = call("findNotes", query=q)
rows, active = [], []
for note in call("notesInfo", notes=note_ids):
    cards = call("cardsInfo", cards=call("findCards", query=f'nid:{note["noteId"]}'))
    rows.append({"note_id": note["noteId"], "model": note["modelName"],
                 "cards": [{"card_id": c["cardId"], "queue_before": c["queue"]} for c in cards]})
    active += [c["cardId"] for c in cards if c["queue"] != -1]
if active:
    call("suspend", cards=active)
if note_ids:
    call("addTags", notes=note_ids, tags="NEBLI::blocked::visual_required_pending")
payload = {"generated_at": dt.datetime.now().astimezone().isoformat(), "query": q,
           "blocked_note_ids": note_ids, "newly_suspended_card_ids": active, "rows": rows}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"notes": len(note_ids), "newly_suspended_cards": len(active)}))
