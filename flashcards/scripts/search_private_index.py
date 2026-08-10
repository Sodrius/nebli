#!/usr/bin/env python3
"""Search a local private AnKing/deck index produced by index_private_apkg.py."""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import unicodedata
from pathlib import Path


def _tokens(value: str) -> list[str]:
    folded = unicodedata.normalize("NFKD", value.casefold())
    folded = "".join(char for char in folded if not unicodedata.combining(char))
    return re.findall(r"[^\W_]+", folded, flags=re.UNICODE)


def _has_fts(db: sqlite3.Connection) -> bool:
    return db.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='notes_fts'"
    ).fetchone() is not None


def search_index(index: Path, queries: list[str], limit_per_query: int = 30,
                 deck: str | None = None, model: str | None = None) -> dict:
    clean_queries = [query.strip() for query in queries if query.strip()]
    if not clean_queries:
        raise ValueError("informe ao menos uma consulta")
    limit_per_query = max(1, min(int(limit_per_query), 200))
    db = sqlite3.connect(index)
    db.row_factory = sqlite3.Row
    try:
        use_fts = _has_fts(db)
        aggregated: dict[int, dict] = {}
        for query in clean_queries:
            tokens = _tokens(query)
            if not tokens:
                continue
            if use_fts:
                expression = " AND ".join(f'"{token}"' for token in tokens)
                hits = db.execute(
                    "SELECT rowid AS nid, bm25(notes_fts) AS score "
                    "FROM notes_fts WHERE notes_fts MATCH ? ORDER BY score LIMIT ?",
                    (expression, limit_per_query * 5),
                ).fetchall()
            else:
                raw_tokens = re.findall(r"[^\W_]+", query.casefold(), flags=re.UNICODE)
                groups = []
                params = []
                for raw_token in raw_tokens:
                    alternatives = list(dict.fromkeys([raw_token] + _tokens(raw_token)))
                    groups.append("(" + " OR ".join(
                        "lower(searchable_text) LIKE ?" for _ in alternatives
                    ) + ")")
                    params.extend(f"%{term}%" for term in alternatives)
                where = " AND ".join(groups)
                hits = db.execute(
                    f"SELECT nid, 0.0 AS score FROM notes WHERE {where} ORDER BY nid LIMIT ?",
                    params + [limit_per_query * 5],
                ).fetchall()
            accepted = 0
            for hit in hits:
                row = db.execute(
                    "SELECT n.nid, n.guid, n.model_name, n.tags, n.fields_json, n.media_json, "
                    "group_concat(DISTINCT c.deck_name) AS decks "
                    "FROM notes n LEFT JOIN cards c ON c.nid=n.nid "
                    "WHERE n.nid=? GROUP BY n.nid", (hit["nid"],),
                ).fetchone()
                if not row:
                    continue
                if deck and deck.casefold() not in str(row["decks"] or "").casefold():
                    continue
                if model and model.casefold() not in str(row["model_name"]).casefold():
                    continue
                accepted += 1
                existing = aggregated.setdefault(row["nid"], {
                    "row": row, "matched_queries": [], "best_score": float(hit["score"]),
                })
                existing["matched_queries"].append(query)
                existing["best_score"] = min(existing["best_score"], float(hit["score"]))
                if accepted >= limit_per_query:
                    break

        output = []
        ranked = sorted(
            aggregated.values(),
            key=lambda item: (-len(item["matched_queries"]), item["best_score"], item["row"]["nid"]),
        )
        for item in ranked:
            row = item["row"]
            fields = json.loads(row["fields_json"])
            plain = re.sub(r"<[^>]+>", " ", " | ".join(fields))
            output.append({
                "source_guid": row["guid"], "model": row["model_name"],
                "decks": row["decks"], "tags": row["tags"],
                "matched_queries": item["matched_queries"],
                "preview": re.sub(r"\s+", " ", plain).strip()[:600],
                "media": json.loads(row["media_json"]),
            })
        return {
            "index_mode": "fts5" if use_fts else "legacy_like",
            "queries": clean_queries,
            "query_count": len(clean_queries),
            "union_count": len(output),
            "results": output,
        }
    finally:
        db.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("index", type=Path)
    parser.add_argument("query", nargs="+")
    parser.add_argument("--limit-per-query", type=int, default=30)
    parser.add_argument("--limit", type=int, help="alias legado de --limit-per-query")
    parser.add_argument("--deck")
    parser.add_argument("--model")
    args = parser.parse_args()
    try:
        result = search_index(
            args.index, args.query, args.limit or args.limit_per_query, args.deck, args.model
        )
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
