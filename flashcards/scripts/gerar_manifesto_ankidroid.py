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

from card_cue_quality import (
    portuguese_front_failures,
    portuguese_text_failures,
    semantic_cue_review_failures,
)
from validar_release_e1_deck import SCHEMA as RELEASE_SCHEMA, validate_release
from canonical_cards import content_sha256, derived, ordered_card_set_sha256
from validar_deck_card_a_card import validate_card

SCHEMA_V1 = "nebli-ankidroid-v1"
SCHEMA_V2 = "nebli-ankidroid-lesson-v2"
SCHEMA_V3 = "nebli-ankidroid-deck-v3"
CARD_CONTRACT = "nebli-card-quality-v2"
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


def _validate_authored(card: dict[str, Any], where: str, *, strict: bool = False) -> None:
    if card.get("source") != "authored":
        raise ValueError(f"{where}: fallback/autoral deve ter source=authored")
    text = str(card.get("text") or "")
    extra = str(card.get("extra") or "")
    language_failures = portuguese_front_failures(text, "pt-BR")
    if language_failures:
        raise ValueError(f"{where}: " + ", ".join(language_failures))
    extra_failures = portuguese_text_failures(extra, "pt-BR", "extra")
    if extra_failures:
        raise ValueError(f"{where}: " + ", ".join(extra_failures))
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
    if len(re.sub(r"<[^>]+>", "", text)) > 360:
        raise ValueError(f"{where}: frente excede 360 caracteres")
    failures = validate_card(card)
    if failures:
        raise ValueError(f"{where}: " + ", ".join(failures))


def _validate_anking_search_evidence(card: dict[str, Any], where: str) -> None:
    if card.get("anking_search_complete") is not True:
        raise ValueError(f"{where}: exige anking_search_complete=true")
    queries = card.get("anking_search_queries")
    if not isinstance(queries, list):
        queries = []
    distinct = {str(value).strip().casefold() for value in queries if str(value).strip()}
    if len(distinct) < 3:
        raise ValueError(f"{where}: exige ao menos 3 buscas AnKing independentes")
    if card.get("anking_search_scope_expanded") is not True:
        raise ValueError(f"{where}: exige anking_search_scope_expanded=true")
    if card.get("anking_siblings_reviewed") is not True:
        raise ValueError(f"{where}: exige anking_siblings_reviewed=true")
    candidates = card.get("anking_candidates_reviewed")
    if not isinstance(candidates, int) or isinstance(candidates, bool) or candidates < 0:
        raise ValueError(f"{where}: anking_candidates_reviewed deve ser inteiro >=0")
    reason = str(card.get("anking_rejection_reason") or "").strip()
    if len(reason) < 20:
        raise ValueError(f"{where}: anking_rejection_reason precisa ser concreto")
    rejections = card.get("anking_rejections") or []
    if candidates > 0:
        if not isinstance(rejections, list) or not rejections:
            raise ValueError(f"{where}: candidatos AnKing exigem anking_rejections[]")
        for index, rejection in enumerate(rejections):
            if not isinstance(rejection, dict) or not str(rejection.get("candidate") or "").strip() \
                    or len(str(rejection.get("reason") or "").strip()) < 10:
                raise ValueError(f"{where}: anking_rejections[{index}] incompleta")


def _validate_masks(card: dict[str, Any], where: str, *, strict: bool = False) -> None:
    if card.get("source") != "io":
        raise ValueError(f"{where}: IO deve ter source=io")
    expected_mode = "hide_two_guess_two"
    if card.get("mode") != expected_mode:
        raise ValueError(f"{where}: IO deve usar {expected_mode}")
    masks = card.get("masks")
    if not isinstance(masks, list) or not masks:
        raise ValueError(f"{where}: IO sem máscaras")
    if strict and len(masks) > 2:
        raise ValueError(f"{where}: hide_two_guess_two permite no máximo 2 máscaras")
    if strict and len(masks) == 2 and not str(card.get("pair_rationale") or "").strip():
        raise ValueError(f"{where}: par IO exige pair_rationale")
    answers = card.get("answers")
    if not isinstance(answers, list) or len(answers) != len(masks):
        raise ValueError(f"{where}: answers deve corresponder exatamente às máscaras")
    if not str(card.get("source_credit") or "").strip():
        raise ValueError(f"{where}: IO exige source_credit")
    failures = validate_card(card)
    if failures:
        raise ValueError(f"{where}: " + ", ".join(failures))
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
    card: dict[str, Any], base_dir: Path, media: dict[str, dict[str, Any]], where: str,
    *, strict: bool = False,
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
    evidence: list[dict[str, Any]] = []
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
        if strict:
            if not str(item.get("cognitive_purpose") or "").strip():
                raise ValueError(f"{where}: extra_images[{i}] exige cognitive_purpose")
            if item.get("didactic_value_reviewed") is not True:
                raise ValueError(f"{where}: extra_images[{i}] exige didactic_value_reviewed=true")
        key = _embed_media_file(raw_path, base_dir, media, f"{where}.extra_images[{i}]", credit)
        keys.append(key)
        evidence.append({
            "key": key,
            "origin": "slide_or_external",
            "source_credit": credit,
            "cognitive_purpose": str(item.get("cognitive_purpose") or "").strip(),
            "didactic_value_reviewed": item.get("didactic_value_reviewed") is True,
        })
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
    card["visual_evidence"] = evidence
    card["extra"] = (str(card.get("extra") or "") + "\n" + "\n".join(blocks)).strip()
    card.pop("extra_images", None)


def _prepare_authored_anking_images(card: dict[str, Any], where: str, *, strict: bool = False) -> None:
    images = card.get("anking_images") or []
    if not isinstance(images, list):
        raise ValueError(f"{where}: anking_images deve ser lista")
    if not images:
        card.pop("anking_images", None)
        return
    refs: list[dict[str, Any]] = []
    blocks: list[str] = []
    keys: list[str] = []
    for i, raw in enumerate(images):
        if not isinstance(raw, dict):
            raise ValueError(f"{where}: anking_images[{i}] inválida")
        item = deepcopy(raw)
        key = str(item.get("key") or f"anking_image_{i+1}").strip()
        if not key or key in keys:
            raise ValueError(f"{where}: anking_images[{i}].key ausente/duplicada")
        query = str(item.get("query") or "").strip()
        queries = item.get("search_queries") or []
        if isinstance(queries, str):
            queries = [queries]
        queries = [str(value).strip() for value in queries if str(value).strip()]
        if query and query not in queries:
            queries.insert(0, query)
        if not query or len({value.casefold() for value in queries}) < 2:
            raise ValueError(f"{where}: anking_images[{i}] exige query + 2 buscas independentes")
        expected_answers = item.get("expected_answers") or []
        if isinstance(expected_answers, str):
            expected_answers = [expected_answers]
        expected_answers = [str(value).strip() for value in expected_answers if str(value).strip()]
        if not expected_answers:
            raise ValueError(f"{where}: anking_images[{i}] exige expected_answers")
        if not isinstance(item.get("media_index", 0), int) or int(item.get("media_index", 0)) < 0:
            raise ValueError(f"{where}: anking_images[{i}].media_index inválido")
        if strict:
            if not str(item.get("cognitive_purpose") or "").strip():
                raise ValueError(f"{where}: anking_images[{i}] exige cognitive_purpose")
            if item.get("didactic_value_reviewed") is not True:
                raise ValueError(f"{where}: anking_images[{i}] exige didactic_value_reviewed=true")
        item["key"] = key
        item["query"] = query
        item["search_queries"] = queries
        item["expected_answers"] = expected_answers
        item["requires_visual"] = True
        refs.append(item)
        keys.append(key)
        blocks.append(
            '<div class="nebli-extra-image"><img src="nebli-anking-media://'
            + html.escape(key, quote=True)
            + '" alt="'
            + html.escape(str(item.get("alt") or "AnKing supporting image"), quote=True)
            + '"></div><div class="nebli-source">'
            + html.escape(str(item.get("source_credit") or "AnKing local"))
            + "</div>"
        )
    card["anking_media_refs"] = refs
    card["anking_media_keys"] = keys
    extra = str(card.get("extra") or "")
    card["extra"] = extra + ("<br>" if extra else "") + "".join(blocks)
    card.pop("anking_images", None)


def _prepare_fallback(
    fallback: dict[str, Any], base_dir: Path, media: dict[str, dict[str, Any]], where: str,
    *, strict: bool = False,
) -> dict[str, Any]:
    f = deepcopy(fallback)
    source = str(f.get("source") or "").lower()
    f["source"] = source
    if source == "authored":
        _validate_authored(f, where, strict=strict)
        _embed_authored_extra_images(f, base_dir, media, where, strict=strict)
        _prepare_authored_anking_images(f, where, strict=strict)
    elif source == "io":
        _validate_masks(f, where, strict=strict)
        _embed_io_media(f, base_dir, media, where)
    else:
        raise ValueError(f"{where}: fallback deve ser authored ou io")
    return f


def _prepare_v3_card(
    raw: dict[str, Any], index: int, base_dir: Path, media: dict[str, dict[str, Any]],
    anking_source_filter: str, *, strict: bool = False,
) -> dict[str, Any]:
    card = deepcopy(raw)
    pre_embed_sha: str | None = None
    key = str(card.get("card_key") or f"card-{index+1:03d}").strip()
    concept = str(card.get("concept_id") or "").strip()
    if not concept:
        raise ValueError(f"{key}: concept_id ausente")
    card["card_key"] = key
    card["concept_id"] = concept
    card["tier"] = str(card.get("tier") or "nucleo").lower()
    if card["tier"] not in {"nucleo", "optional"}:
        raise ValueError(f"{key}: tier deve ser nucleo ou optional")

    source = str(card.get("source") or "").lower()
    card["source"] = source
    if strict and source in {"anking", "external_deck"}:
        raise ValueError(f"{key}: source={source} está suspenso no modo authored_only")
    if source in {"anking", "external_deck"}:
        if strict:
            if not str(card.get("validated_front") or "").strip():
                raise ValueError(f"{key}: validated_front em português é obrigatório")
            language_failures = portuguese_front_failures(
                str(card.get("validated_front") or ""),
                str(card.get("front_language") or ""),
            )
            if language_failures:
                raise ValueError(
                    f"{key}: cópia de deck local precisa de frente validada em português: "
                    + ", ".join(language_failures)
                )
            if card.get("portuguese_front_reviewed") is not True:
                raise ValueError(f"{key}: portuguese_front_reviewed=true é obrigatório")
        if not str(card.get("query") or "").strip():
            raise ValueError(f"{key}: card de deck local sem query")
        aliases = card.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        card["aliases"] = [str(x).strip() for x in aliases if str(x).strip()]
        search_queries = card.get("search_queries") or []
        if isinstance(search_queries, str):
            search_queries = [search_queries]
        search_queries = [str(x).strip() for x in search_queries if str(x).strip()]
        for value in [str(card["query"]).strip(), *card["aliases"]]:
            if value and value not in search_queries:
                search_queries.append(value)
        card["search_queries"] = search_queries
        if source == "anking" and not str(card.get("source_filter") or "").strip():
            card["source_filter"] = anking_source_filter
        fallback = card.get("fallback")
        if not isinstance(fallback, dict):
            raise ValueError(f"{key}: fonte local precisa fallback para garantir deck completo")
        card["fallback"] = _prepare_fallback(
            fallback, base_dir, media, f"{key}.fallback", strict=strict
        )
        expected_answers = card.get("expected_answers") or []
        if isinstance(expected_answers, str):
            expected_answers = [expected_answers]
        expected_answers = [str(x).strip() for x in expected_answers if str(x).strip()]
        if not expected_answers and card["fallback"]["source"] == "authored":
            expected_answers = [m.group(2).strip() for m in CLOZE_RE.finditer(card["fallback"]["text"])]
        if not expected_answers:
            raise ValueError(f"{key}: fonte local exige expected_answers ou fallback cloze")
        card["expected_answers"] = expected_answers
        for field in ("must_contain", "must_not_contain"):
            values = card.get(field) or []
            if isinstance(values, str):
                values = [values]
            card[field] = [str(x).strip() for x in values if str(x).strip()]
        card["anking_required"] = bool(card.get("anking_required", False))
        if strict and source == "anking" and not card["anking_required"]:
            raise ValueError(f"{key}: AnKing curado exige anking_required=true")
        if strict and source == "external_deck":
            _validate_anking_search_evidence(card, key)
        if card.get("requires_visual") is True and card["fallback"]["source"] != "io":
            raise ValueError(f"{key}: conceito visual deve ter fallback IO")
    elif source == "authored":
        if not strict:
            if card.get("anking_search_complete") is not True:
                raise ValueError(f"{key}: autoral legado exige anking_search_complete=true")
            if not str(card.get("anking_rejection_reason") or "").strip():
                raise ValueError(f"{key}: autoral legado exige anking_rejection_reason")
        _validate_authored(card, key, strict=strict)
        # O embed reescreve `extra` com o bloco <img> renderizado. Esse bloco é
        # artefato de renderização, não conteúdo revisado: se entrar no hash, o
        # manifesto diverge do deck-data validado e o finalizador reprova todo
        # card autoral com imagem.
        pre_embed_sha = content_sha256(card)
        _embed_authored_extra_images(card, base_dir, media, key, strict=strict)
        _prepare_authored_anking_images(card, key, strict=strict)
    elif source == "io":
        _validate_masks(card, key, strict=strict)
        _embed_io_media(card, base_dir, media, key)
    else:
        raise ValueError(f"{key}: source não suportado: {source}")

    card["derived"] = derived(card)
    card["content_sha256"] = pre_embed_sha if pre_embed_sha is not None else content_sha256(card)
    card["card_sha256"] = card["content_sha256"]
    return card


def _canonical_deck_identity(data: dict[str, Any]) -> dict[str, str]:
    meta = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
    raw = {
        "uc": meta.get("uc") or data.get("uc"),
        "prova": meta.get("prova") or data.get("prova"),
        "componente": meta.get("componente") or data.get("componente"),
        "nome_curto": meta.get("nome_curto") or data.get("nome_curto") or data.get("lesson_name"),
    }
    if any(value is None or not str(value).strip() for value in raw.values()):
        raise ValueError("deck-data sem metadados suficientes para nome canônico (UC/prova/componente/nome_curto)")
    identity = {key: re.sub(r"\s+", " ", str(value).strip().replace("::", "-")) for key, value in raw.items()}
    uc_match = re.fullmatch(r"(?i)UC\s*0*(\d+)", identity["uc"])
    prova_match = re.fullmatch(r"(?i)P\s*0*(\d+)", identity["prova"])
    if not uc_match:
        raise ValueError("metadata.uc deve seguir UCNN, por exemplo UC03")
    if not prova_match:
        raise ValueError("metadata.prova deve seguir PN, por exemplo P1")
    identity["uc"] = f"UC{int(uc_match.group(1)):02d}"
    identity["prova"] = f"P{int(prova_match.group(1))}"
    return identity


def _canonical_deck_name(identity: dict[str, str]) -> str:
    return "NEBLI::" + "::".join(
        identity[key] for key in ("uc", "prova", "componente", "nome_curto")
    )


def build_v3(args: argparse.Namespace) -> dict[str, Any]:
    source_path = Path(args.deck_data)
    data = json.loads(source_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("deck-data deve ser um objeto JSON")
    raw_cards = data.get("cards")
    if not isinstance(raw_cards, list) or not raw_cards:
        raise ValueError("deck-data sem cards")
    release_result: dict[str, Any] | None = None
    if not args.legacy_unreviewed_v3:
        release_result = validate_release(data, source_path)
        if not release_result["passed"]:
            raise ValueError("release_gate reprovado: " + "; ".join(release_result["errors"]))
    deck_identity = _canonical_deck_identity(data)
    target_deck = _canonical_deck_name(deck_identity)
    supplied_target = args.deck or data.get("target_deck")
    if supplied_target and str(supplied_target).strip() != target_deck:
        raise ValueError(f"target_deck divergente do nome canônico: esperado {target_deck}")

    media: dict[str, dict[str, Any]] = {}
    anking_source_filter = str(
        data.get("anking_source_filter") or 'deck:"AnKing Step Deck"'
    ).strip()
    cards = [
        _prepare_v3_card(
            x, i, source_path.parent, media, anking_source_filter,
            strict=release_result is not None,
        )
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
        "pipeline_version": "e1-deck-v11",
        "minimum_companion_version": "0.8.0",
        "minimum_companion_version_code": 13,
        "required_capabilities": ["authored_cards", "image_occlusion_hide_two_guess_two", "content_hash_validation", "transactional_install"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lesson_slug": args.slug,
        "deck_identity": deck_identity,
        "target_deck": str(target_deck),
        "optional_subdeck": str(target_deck) + "::Optional",
        "expected_card_count": len(cards),
        "write_prefix": "NEBLI::",
        "card_source_mode": "authored_only",
        "mutate_source": False,
        "open_ankidroid_after_install": True,
        "card_quality_contract": CARD_CONTRACT,
        "cards": cards,
        "media": list(media.values()),
    }
    manifest["ordered_card_set_sha256"] = ordered_card_set_sha256(cards)
    if release_result is not None:
        manifest["release_gate"] = {
            key: release_result[key]
            for key in (
                "schema",
                "card_budget_hard_max",
                "concept_count",
                "nuclear_concept_count",
                "covered_nuclear_count",
                "e1_source_sha256",
                "e1_pdf_sha256",
            )
        }
        manifest["release_gate"]["passed"] = True
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
    ap.add_argument(
        "--legacy-unreviewed-v3",
        action="store_true",
        help="somente migração/testes: permite deck-data antigo sem release_gate",
    )
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
