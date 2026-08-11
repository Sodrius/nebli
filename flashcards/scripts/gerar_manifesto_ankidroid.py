#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate install manifests for the Nebli AnkiDroid Companion.

Preferred mode (v3) is a COMPLETE lesson deck. The pipeline supplies the final
card plan and this script embeds any new media, validates hard card-quality
rules, computes the canonical deck name, and emits one self-contained JSON file.
The Companion then resolves AnKing/external local decks and installs validated
fallbacks whenever the local match is not trustworthy.

V2/V1 modes remain only for compatibility/tests.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import mimetypes
import re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SCHEMA_V1 = "nebli-ankidroid-v1"
SCHEMA_V2 = "nebli-ankidroid-lesson-v2"
SCHEMA_V3 = "nebli-ankidroid-deck-v3"
CARD_CONTRACT = "nebli-card-quality-v1"
CLOZE_RE = re.compile(r"\{\{c(\d+)::([^}:]+)(?:::[^}]*)?}}", re.I | re.S)


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


def _hash_obj(obj: Any) -> str:
    canonical = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _word_count(s: str) -> int:
    s = re.sub(r"<[^>]+>", " ", s or "")
    return len([x for x in re.split(r"\s+", s.strip()) if x])


def _validate_authored(card: dict[str, Any], where: str) -> None:
    if card.get("source") != "authored":
        raise ValueError(f"{where}: fallback/autoral deve ter source=authored")
    text = str(card.get("text") or "")
    extra = str(card.get("extra") or "")
    if card.get("front_language", "en").lower() != "en":
        raise ValueError(f"{where}: autoral deve estar em inglês")
    if card.get("extra_language", "pt-BR").lower() not in {"pt", "pt-br"}:
        raise ValueError(f"{where}: Extra autoral deve estar em português")
    matches = list(CLOZE_RE.finditer(text))
    if len(matches) != 1:
        raise ValueError(f"{where}: autoral deve ter exatamente um cloze")
    if matches[0].group(1) != "1":
        raise ValueError(f"{where}: autoral deve usar somente c1")
    words = _word_count(matches[0].group(2))
    if words < 1 or words > 3:
        raise ValueError(f"{where}: cloze deve esconder 1–3 palavras")
    if words == 3 and not str(card.get("three_word_cloze_reason") or "").strip():
        raise ValueError(f"{where}: cloze de 3 palavras exige justificativa")
    if _word_count(extra) > 100:
        raise ValueError(f"{where}: Extra longo demais")


def _validate_masks(card: dict[str, Any], where: str) -> None:
    if card.get("source") != "io":
        raise ValueError(f"{where}: IO deve ter source=io")
    if card.get("mode") != "hide_all_guess_all":
        raise ValueError(f"{where}: IO deve usar hide_all_guess_all")
    masks = card.get("masks")
    if not isinstance(masks, list) or not masks:
        raise ValueError(f"{where}: IO sem máscaras")
    if len(masks) > 1 and card.get("coherent_set") is not True:
        raise ValueError(f"{where}: IO multi-rótulo exige conjunto coerente")
    hard_true = (
        "masks_labels_not_structures",
        "question_preview_validated",
        "answer_preview_validated",
        "visual_ok",
        "real_source",
    )
    for key in hard_true:
        if card.get(key) is not True:
            raise ValueError(f"{where}: {key}=true é obrigatório")
    if card.get("answer_leak", True):
        raise ValueError(f"{where}: IO com vazamento de resposta")
    if not str(card.get("source_credit") or "").strip():
        raise ValueError(f"{where}: IO exige source_credit")
    for i, b in enumerate(masks):
        if not isinstance(b, dict):
            raise ValueError(f"{where}: máscara {i} inválida")
        x, y, w, h = (float(b.get(k, -1)) for k in ("x", "y", "w", "h"))
        if x < 0 or y < 0 or w <= 0 or h <= 0 or x + w > 1.000001 or y + h > 1.000001:
            raise ValueError(f"{where}: máscara {i} fora dos limites")


def _resolve_media_path(raw: Any, base_dir: Path, where: str) -> Path:
    path = Path(str(raw))
    if not path.is_absolute():
        path = (base_dir / path).resolve()
    if not path.is_file():
        raise ValueError(f"{where}: mídia inexistente: {path}")
    return path


def _embed_media_file(
    raw_path: Any,
    base_dir: Path,
    media: dict[str, dict[str, Any]],
    where: str,
    source_credit: str,
) -> str:
    path = _resolve_media_path(raw_path, base_dir, where)
    blob = path.read_bytes()
    digest = hashlib.sha256(blob).hexdigest()
    key = f"m_{digest[:20]}"
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    media.setdefault(key, {
        "key": key,
        "filename": path.name,
        "mime_type": mime,
        "sha256": digest,
        "data_base64": base64.b64encode(blob).decode("ascii"),
        "source_credit": source_credit,
    })
    return key


def _embed_io_media(card: dict[str, Any], base_dir: Path, media: dict[str, dict[str, Any]], where: str) -> None:
    raw = card.get("image_path")
    if not raw and card.get("media_key"):
        return
    if not raw:
        raise ValueError(f"{where}: IO precisa image_path ou media_key")
    credit = str(card.get("source_credit") or "").strip()
    key = _embed_media_file(raw, base_dir, media, where, credit)
    card["media_key"] = key
    card.pop("image_path", None)


def _embed_authored_extra_images(
    card: dict[str, Any], base_dir: Path, media: dict[str, dict[str, Any]], where: str
) -> None:
    images = card.get("extra_images") or []
    if isinstance(images, (str, Path)):
        images = [images]
    if not isinstance(images, list):
        raise ValueError(f"{where}: extra_images deve ser lista")
    if not images:
        card.pop("extra_images", None)
        return

    keys: list[str] = []
    blocks: list[str] = []
    for i, item in enumerate(images):
        if isinstance(item, str):
            raise ValueError(f"{where}: extra_images[{i}] deve registrar path + source_credit")
        if not isinstance(item, dict):
            raise ValueError(f"{where}: extra_images[{i}] inválido")
        raw_path = item.get("path") or item.get("image_path")
        credit = str(item.get("source_credit") or "").strip()
        alt = str(item.get("alt") or "supporting image").strip()
        if not raw_path:
            raise ValueError(f"{where}: extra_images[{i}] sem path")
        if not credit:
            raise ValueError(f"{where}: extra_images[{i}] exige source_credit")
        key = _embed_media_file(raw_path, base_dir, media, f"{where}.extra_images[{i}]", credit)
        keys.append(key)
        blocks.append(
            '<div class="nebli-extra-image"><img src="nebli-media://'
            + key
            + '" alt="'
            + html.escape(alt, quote=True)
            + '"></div><div class="nebli-source">'
            + html.escape(credit)
            + "</div>"
        )
    card["media_keys"] = keys
    card["extra"] = (str(card.get("extra") or "") + "\n" + "\n".join(blocks)).strip()
    card.pop("extra_images", None)


def _prepare_fallback(
    fallback: dict[str, Any], base_dir: Path, media: dict[str, dict[str, Any]], where: str
) -> dict[str, Any]:
    f = deepcopy(fallback)
    source = str(f.get("source") or "").lower()
    f["source"] = source
    if source == "authored":
        _validate_authored(f, where)
        _embed_authored_extra_images(f, base_dir, media, where)
    elif source == "io":
        _validate_masks(f, where)
        _embed_io_media(f, base_dir, media, where)
    else:
        raise ValueError(f"{where}: fallback deve ser authored ou io")
    return f


def _prepare_v3_card(
    raw: dict[str, Any], index: int, base_dir: Path, media: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    card = deepcopy(raw)
    key = str(card.get("card_key") or f"card-{index+1:03d}").strip()
    concept = str(card.get("concept_id") or "").strip()
    if not concept:
        raise ValueError(f"{key}: concept_id ausente")
    card["card_key"] = key
    card["concept_id"] = concept
    card["tier"] = str(card.get("tier") or "nucleo").lower()
    if card["tier"] not in {"nucleo", "optional"}:
        raise ValueError(f"{key}: tier deve ser nucleo ou optional")
    if card.get("atomic") is not True:
        raise ValueError(f"{key}: atomic=true é obrigatório")
    if card.get("relevant") is not True:
        raise ValueError(f"{key}: relevant=true é obrigatório")

    source = str(card.get("source") or "").lower()
    card["source"] = source
    if source in {"anking", "external_deck"}:
        if not str(card.get("query") or "").strip():
            raise ValueError(f"{key}: card de deck local sem query")
        aliases = card.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        card["aliases"] = [str(x).strip() for x in aliases if str(x).strip()]
        fallback = card.get("fallback")
        if not isinstance(fallback, dict):
            raise ValueError(f"{key}: fonte local precisa fallback para garantir deck completo")
        card["fallback"] = _prepare_fallback(fallback, base_dir, media, f"{key}.fallback")
        if card.get("requires_visual") is True and card["fallback"]["source"] != "io":
            raise ValueError(f"{key}: conceito visual deve ter fallback IO")
    elif source == "authored":
        _validate_authored(card, key)
        _embed_authored_extra_images(card, base_dir, media, key)
    elif source == "io":
        _validate_masks(card, key)
        _embed_io_media(card, base_dir, media, key)
    else:
        raise ValueError(f"{key}: source não suportado: {source}")

    hashable = deepcopy(card)
    hashable.pop("card_sha256", None)
    card["card_sha256"] = _hash_obj(hashable)
    return card


def _canonical_deck_name(data: dict[str, Any]) -> str:
    meta = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
    parts = [
        meta.get("uc") or data.get("uc"),
        meta.get("prova") or data.get("prova"),
        meta.get("componente") or data.get("componente"),
        meta.get("nome_curto") or data.get("nome_curto") or data.get("lesson_name"),
    ]
    cleaned = [str(x).strip().replace("::", "-") for x in parts if x is not None and str(x).strip()]
    if len(cleaned) < 2:
        raise ValueError("deck-data sem metadados suficientes para nome canônico (UC/prova/componente/nome_curto)")
    return "NEBLI::" + "::".join(cleaned)


def build_v3(args: argparse.Namespace) -> dict[str, Any]:
    source_path = Path(args.deck_data)
    data = json.loads(source_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("deck-data deve ser um objeto JSON")
    raw_cards = data.get("cards")
    if not isinstance(raw_cards, list) or not raw_cards:
        raise ValueError("deck-data sem cards")
    target_deck = args.deck or data.get("target_deck") or _canonical_deck_name(data)
    if not str(target_deck).startswith("NEBLI::"):
        raise ValueError("target deck deve começar por NEBLI::")

    media: dict[str, dict[str, Any]] = {}
    cards = [
        _prepare_v3_card(x, i, source_path.parent, media)
        for i, x in enumerate(raw_cards)
        if isinstance(x, dict)
    ]
    if len(cards) != len(raw_cards):
        raise ValueError("deck-data contém card não-objeto")
    keys = [c["card_key"] for c in cards]
    if len(set(keys)) != len(keys):
        raise ValueError("card_key duplicado no deck final")

    manifest: dict[str, Any] = {
        "schema": SCHEMA_V3,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lesson_slug": args.slug,
        "target_deck": str(target_deck),
        "optional_subdeck": str(target_deck) + "::Optional",
        "expected_card_count": len(cards),
        "write_prefix": "NEBLI::",
        "mutate_source": False,
        "open_ankidroid_after_install": True,
        "card_quality_contract": CARD_CONTRACT,
        "search": {
            "min_score": args.min_score,
            "min_margin": args.min_margin,
            "max_candidates": args.max_candidates,
            "prefer_anking": True,
            "require_anking_marker": True,
            "ambiguous_policy": "use_validated_fallback",
        },
        "cards": cards,
        "media": list(media.values()),
    }
    manifest["manifest_sha256"] = _hash_obj(manifest)
    return manifest


def build_v2(args: argparse.Namespace) -> dict[str, Any]:
    data = json.loads(Path(args.conceitos).read_text(encoding="utf-8"))
    concepts = _normalize_concepts(data)
    if not args.deck:
        raise ValueError("--deck é obrigatório no modo v2")
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
    manifest["manifest_sha256"] = _hash_obj(manifest)
    return manifest


def build_v1(args: argparse.Namespace) -> dict[str, Any]:
    if not args.deck:
        raise ValueError("--deck é obrigatório no modo v1")
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
    manifest["manifest_sha256"] = _hash_obj(manifest)
    return manifest


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--deck", help="override do nome do deck; v3 normalmente deriva dos metadados")
    ap.add_argument("--deck-data", help="JSON do deck final; ativa schema v3 preferido")
    ap.add_argument("--conceitos", help="compatibilidade v2")
    ap.add_argument("--curado", help="compatibilidade v1")
    ap.add_argument("--out")
    ap.add_argument("--source-query")
    ap.add_argument("--min-score", type=float, default=0.82)
    ap.add_argument("--min-margin", type=float, default=0.06)
    ap.add_argument("--max-candidates", type=int, default=80)
    ap.add_argument("--require-anking-marker", action="store_true")
    args = ap.parse_args()

    modes = sum(bool(x) for x in (args.deck_data, args.conceitos, args.curado))
    if modes != 1:
        raise SystemExit("ERRO: informe exatamente um de --deck-data (v3), --conceitos (v2) ou --curado (v1)")
    if args.deck and not args.deck.startswith("NEBLI::"):
        raise SystemExit("ERRO: target deck deve começar por NEBLI::")

    try:
        if args.deck_data:
            manifest = build_v3(args)
        elif args.conceitos:
            manifest = build_v2(args)
        else:
            manifest = build_v1(args)
    except (ValueError, json.JSONDecodeError, OSError) as exc:
        raise SystemExit(f"ERRO: {exc}") from exc

    out = Path(args.out) if args.out else Path("flashcards/manifests") / f"{args.slug}.ankidroid.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)
    print(
        f"schema={manifest['schema']} cards={manifest.get('expected_card_count', 0)} "
        f"concepts={len(manifest.get('concepts', []))} media={len(manifest.get('media', []))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
