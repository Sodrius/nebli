#!/usr/bin/env python3
"""Valida o lote de staging sem alterar o Anki."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from lint_neblicard import lint_text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("inventory")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    data = json.loads(Path(args.inventory).read_text(encoding="utf-8-sig"))
    rows = []
    for note in data.get("notes", []):
        model = note.get("model", "")
        text = note.get("fields", {}).get("Text", "")
        # IO e prompts visuais são avaliados pelo manifesto visual, não pelo
        # linter de cloze textual.
        is_green_control = "NEBLI::mutirao_action::keep_control" in note.get("tags", [])
        if "Occlusion" in model or "IO" in model or "{{c" not in text or is_green_control:
            result = {"status": "NOT_APPLICABLE", "score": 0, "flags": []}
        else:
            result = lint_text(text)
        rows.append({
            "note_id": note["note_id"],
            "source_note_id": next((t.rsplit("::", 1)[-1] for t in note.get("tags", []) if t.startswith("NEBLI::source_note::")), None),
            "model": model,
            "front": note.get("front", ""),
            **{k: result[k] for k in ("status", "score", "flags")},
        })
    counts = Counter(row["status"] for row in rows)
    output = {"summary": dict(counts), "rows": rows}
    Path(args.output).write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output["summary"], ensure_ascii=False))
    return 1 if counts["REJECT"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
