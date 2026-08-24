#!/usr/bin/env python3
"""Reativa somente os cards suspensos pela dosagem IO de 2026-07-15."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from nebli_anki import call

parser = argparse.ArgumentParser()
parser.add_argument("snapshot", type=Path)
args = parser.parse_args()
data = json.loads(args.snapshot.read_text(encoding="utf-8-sig"))
ids = data.get("suspended_card_ids", [])
if ids:
    call("unsuspend", cards=ids)
print(json.dumps({"unsuspended": len(ids)}))
