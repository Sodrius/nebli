#!/usr/bin/env python3
"""Deriva métricas e hashes dos cards canônicos sem confiar em flags manuais."""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from copy import deepcopy
from typing import Any
from pathlib import Path

CLOZE_RE = re.compile(r"\{\{c(\d+)::([^}:]+)(?:::[^}]*)?}}", re.I | re.S)
ACTIVE_SOURCES = {"authored", "io"}
LEARNING_FIELDS = {
    "card_key", "concept_id", "tier", "source", "text", "extra", "e1_anchor",
    "retrieval_target", "semantic_review", "three_word_cloze_reason", "prompt",
    "answers", "mode", "masks", "pair_rationale", "source_credit", "cognitive_purpose",
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_obj(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _plain(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text or "")


def words(text: str) -> list[str]:
    return [item for item in re.split(r"\s+", _plain(text).strip()) if item]


def normalized(text: str) -> str:
    text = unicodedata.normalize("NFKD", _plain(text)).casefold()
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def learning_payload(card: dict[str, Any]) -> dict[str, Any]:
    payload = {key: deepcopy(card[key]) for key in sorted(LEARNING_FIELDS) if key in card}
    payload["source"] = str(payload.get("source") or "").lower()
    payload["tier"] = str(payload.get("tier") or "nucleo").lower()
    return payload


def content_sha256(card: dict[str, Any]) -> str:
    return sha256_obj(learning_payload(card))


def ordered_card_set_sha256(cards: list[dict[str, Any]]) -> str:
    return sha256_obj([
        {"card_key": str(card.get("card_key") or ""), "content_sha256": content_sha256(card)}
        for card in cards
    ])


def derived(card: dict[str, Any]) -> dict[str, Any]:
    text = str(card.get("text") or "")
    extra = str(card.get("extra") or "")
    matches = list(CLOZE_RE.finditer(text))
    answers = [m.group(2).strip() for m in matches]
    visible = CLOZE_RE.sub(" ", text)
    return {
        "cloze_occurrences": len(matches),
        "cloze_indices": [int(m.group(1)) for m in matches],
        "cloze_answer_words": [len(words(value)) for value in answers],
        "front_characters": len(_plain(text)),
        "extra_words": len(words(extra)),
        "answer_visible": any(
            value and re.search(rf"(?:^| ){re.escape(value)}(?: |$)", normalized(visible))
            for value in map(normalized, answers)
        ),
        "probable_language": "en" if sum(
            token in {"the", "is", "are", "with", "when", "which", "that", "from", "into", "because"}
            for token in normalized(visible + " " + extra).split()
        ) >= 3 else "pt-BR",
    }


def media_hashes(manifest_or_deck: dict[str, Any]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for item in manifest_or_deck.get("media") or []:
        if isinstance(item, dict):
            out.append({"key": str(item.get("key") or ""), "sha256": str(item.get("sha256") or "")})
    return out


def referenced_media_hashes(cards: list[dict[str, Any]], base: Path) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for card in cards:
        raw = card.get("image_path")
        if not raw: continue
        path = Path(str(raw)); path = path if path.is_absolute() else (base / path).resolve()
        out.append({"card_key": str(card.get("card_key") or ""), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    return out
