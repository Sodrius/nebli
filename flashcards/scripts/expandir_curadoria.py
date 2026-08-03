#!/usr/bin/env python3
"""Amplia uma curadoria existente com GUIDs revisados do pool AnKing.

Uso: python expandir_curadoria.py base-slug novo-slug --deck "..." GUID:conceito ...
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("base_slug")
    ap.add_argument("new_slug")
    ap.add_argument("--deck", required=True)
    ap.add_argument("items", nargs="+")
    args = ap.parse_args()
    base = json.loads((ROOT / "flashcards" / "curadoria" / f"{args.base_slug}-curado.json").read_text(encoding="utf-8"))
    pool = json.loads((ROOT / "arquivos-trabalho" / f"anking-pool-{args.base_slug}.json").read_text(encoding="utf-8"))
    by_guid = {str(row.get("guid")): row for row in pool.get("cards", [])}
    kept = list(base.get("kept", []))
    seen = {str(row.get("guid")) for row in kept}
    for item in args.items:
        guid, concept = item.rsplit(":", 1)
        if guid in seen:
            continue
        card = by_guid.get(guid)
        if not card:
            raise SystemExit(f"GUID ausente do pool: {guid}")
        kept.append({"guid": guid, "conceito": concept, "raw0": card.get("raw0", card.get("text", ""))})
        seen.add(guid)
    out = {"slug": args.new_slug, "tag_ancora": f"NEBLI::{args.new_slug}",
           "target_deck": args.deck,
           "origem": "Curadoria AnKing ampliada, revisada por conceito antes da E1/E2.",
           "kept": kept}
    dest = ROOT / "flashcards" / "curadoria" / f"{args.new_slug}-curado.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{dest}: {len(kept)} cards AnKing curados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
