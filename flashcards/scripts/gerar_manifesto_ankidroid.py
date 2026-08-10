#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gera manifesto de instalação local para o Nebli AnkiDroid Companion.

O manifesto NÃO contém os 6 GB do AnKing nem copia mídia. Ele descreve o lote
curado que o Companion deve resolver diretamente na coleção do AnkiDroid.

Uso:
  python flashcards/scripts/gerar_manifesto_ankidroid.py \
    --slug anato-10-intestino-grosso \
    --deck "NEBLI::UC02::P3::Anatomia::Intestino grosso"

Opcionalmente, --curado aponta para um JSON de curadoria. O script reconhece
listas comuns (`items`, `cards`, `kept`, `guids_kept`) e transporta IDs locais
quando presentes, sem depender deles.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "nebli-ankidroid-v1"


def _list_from_curado(data: Any) -> list[dict[str, Any]]:
    if not isinstance(data, dict):
        return []
    for key in ("items", "cards", "kept", "guids_kept"):
        value = data.get(key)
        if isinstance(value, list):
            return [x for x in value if isinstance(x, dict)]
    return []


def _first(item: dict[str, Any], names: Iterable[str]) -> Any:
    for name in names:
        if name in item and item[name] not in (None, ""):
            return item[name]
    return None


def _normalize_item(item: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    note_id = _first(item, ("source_note_id", "note_id", "nid"))
    card_id = _first(item, ("source_card_id", "card_id", "cid"))
    guid = _first(item, ("source_guid", "guid"))
    ordinal = _first(item, ("ordinal", "ord"))
    concept = _first(item, ("conceito", "concept", "concept_id"))
    raw0 = _first(item, ("raw0", "text", "first_field"))

    if note_id is not None:
        out["source_note_id"] = int(note_id)
    if card_id is not None:
        out["source_card_id"] = int(card_id)
    if guid is not None:
        out["source_guid"] = str(guid)
    if ordinal is not None:
        out["selected_ordinals"] = [int(ordinal)]
    if concept is not None:
        out["concept"] = str(concept)
    if raw0 is not None:
        out["first_field_fingerprint"] = hashlib.sha256(str(raw0).encode("utf-8")).hexdigest()
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--deck", required=True)
    ap.add_argument("--curado")
    ap.add_argument("--out")
    ap.add_argument("--source-query")
    args = ap.parse_args()

    if not args.deck.startswith("NEBLI::"):
        raise SystemExit("ERRO: target deck deve começar por NEBLI::")

    items: list[dict[str, Any]] = []
    if args.curado:
        data = json.loads(Path(args.curado).read_text(encoding="utf-8"))
        items = [_normalize_item(x) for x in _list_from_curado(data)]
        items = [x for x in items if x]

    manifest = {
        "schema": SCHEMA,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lesson_slug": args.slug,
        "target_deck": args.deck,
        "source_query": args.source_query or f"tag:NEBLI::{args.slug} -deck:\"{args.deck}\"",
        "write_prefix": "NEBLI::",
        "copy_mode": "exact_fields",
        "preserve_note_type": True,
        "preserve_tags": True,
        "preserve_media_refs": True,
        "reset_scheduling": True,
        "selected_sibling_policy": "suspend_unselected",
        "mutate_source": False,
        "items": items,
    }
    canonical = json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    manifest["manifest_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    out = Path(args.out) if args.out else Path("flashcards/manifests") / f"{args.slug}.ankidroid.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)
    print(f"items={len(items)} source_query={manifest['source_query']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
