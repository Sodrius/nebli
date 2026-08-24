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
for row in data.get("changes", []):
    call("updateNoteFields", note={"id": row["note_id"], "fields": row["before_fields"]})
    call("removeTags", notes=[row["note_id"]], tags="NEBLI::image_deduped::2026-07-15")
print(json.dumps({"restored_notes": len(data.get("changes", []))}))
