#!/usr/bin/env python3
"""Search a local private AnKing/deck index produced by index_private_apkg.py."""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("index", type=Path)
    parser.add_argument("query", nargs="+")
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--deck")
    parser.add_argument("--model")
    args = parser.parse_args()
    terms = [term.casefold() for term in args.query if term.strip()]
    if not terms:
        parser.error("informe ao menos um termo")
    db = sqlite3.connect(args.index)
    db.row_factory = sqlite3.Row
    try:
        where = ["lower(n.searchable_text) LIKE ?" for _ in terms]
        params: list[object] = [f"%{term}%" for term in terms]
        if args.deck:
            where.append("lower(c.deck_name) LIKE ?")
            params.append(f"%{args.deck.casefold()}%")
        if args.model:
            where.append("lower(n.model_name) LIKE ?")
            params.append(f"%{args.model.casefold()}%")
        params.append(max(1, min(args.limit, 200)))
        rows = db.execute(
            "SELECT n.guid, n.model_name, n.tags, n.fields_json, n.media_json, "
            "group_concat(DISTINCT c.deck_name) AS decks "
            "FROM notes n LEFT JOIN cards c ON c.nid=n.nid WHERE " + " AND ".join(where) +
            " GROUP BY n.nid ORDER BY n.nid LIMIT ?", params,
        ).fetchall()
        output = []
        for row in rows:
            fields = json.loads(row["fields_json"])
            plain = re.sub(r"<[^>]+>", " ", " | ".join(fields))
            output.append({
                "source_guid": row["guid"], "model": row["model_name"],
                "decks": row["decks"], "tags": row["tags"],
                "preview": re.sub(r"\s+", " ", plain).strip()[:600],
                "media": json.loads(row["media_json"]),
            })
        print(json.dumps({"query": terms, "count": len(output), "results": output},
                         ensure_ascii=False, indent=2))
    finally:
        db.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
