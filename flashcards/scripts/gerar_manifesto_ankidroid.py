#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gera manifesto de aula para o Nebli AnkiDroid Companion.

Modo preferido (v2): o core envia CONCEITOS, não IDs de cards. O Companion resolve
os candidatos diretamente no AnkiDroid local, aplica ranking/gates e copia apenas
os casos confiáveis para NEBLI::*.

Exemplo:
  python flashcards/scripts/gerar_manifesto_ankidroid.py \
    --slug anato-10-intestino-grosso \
    --deck "NEBLI::UC02::P3::Anatomia::Intestino grosso" \
    --conceitos arquivos-trabalho/conceitos-anato-10-intestino-grosso.json

O arquivo de conceitos pode ser:
  ["portal vein", "marginal artery of Drummond"]
ou
  {"concepts": [{"id":"c1","query":"portal vein","aliases":["hepatic portal vein"]}]}

O modo legado --curado permanece disponível e gera schema v1.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SCHEMA_V1 = "nebli-ankidroid-v1"
SCHEMA_V2 = "nebli-ankidroid-lesson-v2"


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


def _normalize_concepts(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, dict):
        data = data.get("concepts", data.get("items", []))
    if not isinstance(data, list):
        raise ValueError("arquivo de conceitos deve conter uma lista ou {'concepts': [...]} ")
    out: list[dict[str, Any]] = []
    for i, item in enumerate(data):
        if isinstance(item, str):
            q = item.strip()
            if q:
                out.append({"id": f"c{i+1:03d}", "query": q, "required": True})
            continue
        if not isinstance(item, dict):
            continue
        q = _first(item, ("query", "concept", "conceito", "text", "label"))
        if not q:
            continue
        aliases = item.get("aliases") or item.get("sinonimos") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        aliases = [str(x).strip() for x in aliases if str(x).strip()]
        out.append({
            "id": str(item.get("id") or item.get("concept_id") or f"c{i+1:03d}"),
            "query": str(q).strip(),
            "aliases": aliases,
            "required": bool(item.get("required", item.get("nuclear", True))),
        })
    if not out:
        raise ValueError("nenhum conceito válido encontrado")
    return out


def _hash_manifest(manifest: dict[str, Any]) -> str:
    canonical = json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def build_v2(args: argparse.Namespace) -> dict[str, Any]:
    data = json.loads(Path(args.conceitos).read_text(encoding="utf-8"))
    concepts = _normalize_concepts(data)
    manifest: dict[str, Any] = {
        "schema": SCHEMA_V2,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lesson_slug": args.slug,
        "target_deck": args.deck,
        "write_prefix": "NEBLI::",
        "copy_mode": "exact_fields",
        "preserve_note_type": True,
        "preserve_tags": True,
        "preserve_media_refs": True,
        "reset_scheduling": True,
        "selected_sibling_policy": "suspend_unselected",
        "mutate_source": False,
        "search": {
            "min_score": args.min_score,
            "min_margin": args.min_margin,
            "max_candidates": args.max_candidates,
            "prefer_anking": True,
            "require_anking_marker": args.require_anking_marker,
        },
        "concepts": concepts,
    }
    manifest["manifest_sha256"] = _hash_manifest(manifest)
    return manifest


def build_v1(args: argparse.Namespace) -> dict[str, Any]:
    items: list[dict[str, Any]] = []
    if args.curado:
        data = json.loads(Path(args.curado).read_text(encoding="utf-8"))
        items = [_normalize_item(x) for x in _list_from_curado(data)]
        items = [x for x in items if x]
    manifest: dict[str, Any] = {
        "schema": SCHEMA_V1,
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
    manifest["manifest_sha256"] = _hash_manifest(manifest)
    return manifest


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--deck", required=True)
    ap.add_argument("--conceitos", help="JSON com conceitos; ativa o schema v2 preferido")
    ap.add_argument("--curado", help="JSON de curadoria legada; gera schema v1")
    ap.add_argument("--out")
    ap.add_argument("--source-query")
    ap.add_argument("--min-score", type=float, default=0.82)
    ap.add_argument("--min-margin", type=float, default=0.06)
    ap.add_argument("--max-candidates", type=int, default=80)
    ap.add_argument("--require-anking-marker", action="store_true")
    args = ap.parse_args()

    if not args.deck.startswith("NEBLI::"):
        raise SystemExit("ERRO: target deck deve começar por NEBLI::")
    if args.conceitos and args.curado:
        raise SystemExit("ERRO: use --conceitos (v2) OU --curado (v1), não ambos")
    if not args.conceitos and not args.curado:
        raise SystemExit("ERRO: informe --conceitos (preferido) ou --curado")

    try:
        manifest = build_v2(args) if args.conceitos else build_v1(args)
    except (ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ERRO: {exc}") from exc

    out = Path(args.out) if args.out else Path("flashcards/manifests") / f"{args.slug}.ankidroid.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)
    print(f"schema={manifest['schema']} concepts={len(manifest.get('concepts', []))} items={len(manifest.get('items', []))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
