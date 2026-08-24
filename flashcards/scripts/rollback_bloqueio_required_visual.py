#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path
from nebli_anki import call

parser = argparse.ArgumentParser()
parser.add_argument("snapshot", type=Path)
args = parser.parse_args()
data = json.loads(args.snapshot.read_text(encoding="utf-8-sig"))
ids = data.get("newly_suspended_card_ids", [])
if ids:
    call("unsuspend", cards=ids)
notes = data.get("blocked_note_ids", [])
if notes:
    call("removeTags", notes=notes, tags="NEBLI::blocked::visual_required_pending")
print(json.dumps({"unsuspended": len(ids)}))
