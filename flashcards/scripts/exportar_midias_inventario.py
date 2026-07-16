#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exporta mídias referenciadas por notes de um inventário, sem mutar o Anki."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path

from PIL import Image

from anki import call


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory", type=Path, required=True)
    ap.add_argument("--note-ids", required=True, help="IDs separados por vírgula")
    ap.add_argument("--output-dir", type=Path, required=True)
    args = ap.parse_args()
    wanted = {int(x.strip()) for x in args.note_ids.split(",") if x.strip()}
    data = json.loads(args.inventory.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    names = sorted({name for note in data["notes"] if note["note_id"] in wanted for name in note.get("images", [])})
    rows = []
    for name in names:
        encoded = call("retrieveMediaFile", filename=name)
        if not encoded:
            rows.append({"file": name, "status": "missing_in_anki"})
            continue
        raw = base64.b64decode(encoded)
        target = args.output_dir / name
        target.write_bytes(raw)
        try:
            with Image.open(target) as im:
                width, height, fmt = im.width, im.height, im.format
        except Exception:
            width = height = None
            fmt = None
        rows.append({
            "file": name,
            "status": "exported",
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "width": width,
            "height": height,
            "format": fmt,
        })
    index = args.output_dir / "index.json"
    index.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(index)
    print(json.dumps(rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
