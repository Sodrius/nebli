#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Hard gate card-a-card para o Deck-Aula NEBLI.

Nunca usa amostragem. Cada card real do plano final precisa ter um registro e
passar as regras aplicáveis à sua fonte. Retorna código != 0 em qualquer falha.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_MIN_SCORE = 0.82
DEFAULT_MIN_MARGIN = 0.06
PT_LANGUAGES = {"pt", "pt-br"}
CLOZE_ROLES = {
    "mecanismo", "consequencia", "discriminador", "valor", "direcao", "rotulo_especifico",
}


def _bool(card: dict[str, Any], key: str, *, default: bool | None = None) -> bool:
    if key not in card:
        return False if default is None else default
    return card.get(key) is True


def _local_rank_ok(card: dict[str, Any], min_score: float, min_margin: float) -> bool:
    if card.get("source") not in {"anking", "external_deck"}:
        return True
    score = float(card.get("score", 0.0))
    second = float(card.get("second_score", 0.0))
    exact = bool(card.get("exact_phrase", False))
    if score < min_score:
        return False
    if second <= 0.0:
        return True
    return score - second >= min_margin


def _validate_authored(card: dict[str, Any], failures: list[str]) -> None:
    if str(card.get("front_language", "")).lower() not in PT_LANGUAGES:
        failures.append("front_language_not_pt")
    if str(card.get("extra_language", "")).lower() not in {"pt", "pt-br"}:
        failures.append("extra_language_not_pt")
    if int(card.get("cloze_count", 0)) != 1:
        failures.append("cloze_count_must_be_1")
    if int(card.get("cloze_index", 0)) != 1:
        failures.append("cloze_index_must_be_c1")
    words = int(card.get("cloze_words", 0))
    if words < 1:
        failures.append("cloze_words<1")
    if words > 3:
        failures.append("cloze_words>3")
    if words == 3 and not str(card.get("three_word_cloze_reason", "")).strip():
        failures.append("three_word_cloze_without_reason")
    if int(card.get("extra_words", 0)) > 100:
        failures.append("extra_words>100")
    if int(card.get("front_characters", 0)) > 360:
        failures.append("front_characters>360")
    if _bool(card, "multi_retrieval", default=False):
        failures.append("multi_retrieval")
    for key in ("portuguese_reviewed", "knowledge_required", "blind_review_passed", "ambiguity_reviewed"):
        if not _bool(card, key):
            failures.append(key)
    for key in ("grammar_only_solvable", "lexical_leak", "answer_visible_elsewhere"):
        if _bool(card, key, default=True):
            failures.append(key)
    if str(card.get("cloze_role") or "").lower() not in CLOZE_ROLES:
        failures.append("invalid_cloze_role")
    if int(card.get("unresolved_plausible_alternatives", -1)) != 0:
        failures.append("unresolved_plausible_alternatives")
    if _bool(card, "has_extra_media", default=False):
        if not _bool(card, "media_ok"):
            failures.append("media_ok")
        if not _bool(card, "media_source_credit_ok"):
            failures.append("media_source_credit_ok")
        if not _bool(card, "media_cognitive_purpose_ok"):
            failures.append("media_cognitive_purpose_ok")
        if not _bool(card, "didactic_value_reviewed"):
            failures.append("didactic_value_reviewed")
        if not _bool(card, "anking_visual_preference_checked"):
            failures.append("anking_visual_preference_checked")
        if not _bool(card, "anking_visual_used") \
                and len(str(card.get("anking_visual_rejection_reason", "")).strip()) < 20:
            failures.append("anking_visual_preference_unresolved")


def _validate_anking_search_audit(card: dict[str, Any], failures: list[str]) -> None:
    for key in (
        "anking_search_queries_ok",
        "anking_scope_expanded",
        "anking_siblings_reviewed",
        "anking_candidates_reviewed_ok",
        "anking_rejections_ok",
    ):
        if not _bool(card, key):
            failures.append(key)


def _validate_io(card: dict[str, Any], failures: list[str]) -> None:
    if str(card.get("prompt_language", "")).lower() not in PT_LANGUAGES:
        failures.append("prompt_language_not_pt")
    if str(card.get("answers_language", "")).lower() not in PT_LANGUAGES:
        failures.append("answers_language_not_pt")
    if not _bool(card, "portuguese_prompt_reviewed"):
        failures.append("portuguese_prompt_reviewed")
    if not _bool(card, "portuguese_answers_reviewed"):
        failures.append("portuguese_answers_reviewed")
    if card.get("mode") != "hide_two_guess_two":
        failures.append("io_mode")
    mask_count = int(card.get("mask_count", 0))
    if mask_count < 1:
        failures.append("mask_count<1")
    if mask_count > 2:
        failures.append("mask_count>2")
    if mask_count > 1 and not _bool(card, "coherent_set"):
        failures.append("multi_mask_not_coherent")
    if mask_count == 2 and not str(card.get("pair_rationale", "")).strip():
        failures.append("pair_rationale_missing")
    for key in (
        "masks_labels_not_structures",
        "question_preview_validated",
        "answer_preview_validated",
        "visual_ok",
        "real_source",
        "source_credit_ok",
        "media_ok",
        "media_cognitive_purpose_ok",
        "didactic_value_reviewed",
    ):
        if not _bool(card, key):
            failures.append(key)
    if _bool(card, "answer_leak", default=True):
        failures.append("answer_leak")
    if not _bool(card, "mask_geometry_ok"):
        failures.append("mask_geometry_ok")


def validate_card(card: dict[str, Any], min_score: float, min_margin: float) -> list[str]:
    failures: list[str] = []
    source = str(card.get("source", "")).lower()

    for key in ("card_key", "concept_id", "source"):
        if not card.get(key):
            failures.append(f"missing:{key}")

    for key in ("selected", "atomic", "relevant", "e1_anchor_ok"):
        if not _bool(card, key):
            failures.append(key)

    if str(card.get("tier", "")) not in {"nucleo", "optional"}:
        failures.append("invalid_tier")

    if source in {"anking", "external_deck"}:
        if str(card.get("front_language", "")).lower() not in PT_LANGUAGES:
            failures.append("front_language_not_pt")
        if not _bool(card, "portuguese_front_reviewed"):
            failures.append("portuguese_front_reviewed")
        if not _bool(card, "source_safe"):
            failures.append("source_safe")
        if not _local_rank_ok(card, min_score, min_margin):
            failures.append("local_deck_rank")
        for key in ("same_note_type", "same_fields", "media_ok", "sibling_policy_ok", "fallback_validated"):
            if not _bool(card, key):
                failures.append(key)
        for key in ("search_queries_ok", "expected_answers_ok"):
            if not _bool(card, key):
                failures.append(key)
        if source == "anking" and not _bool(card, "anking_marker_ok"):
            failures.append("anking_marker_ok")
        if source == "anking" and not _bool(card, "anking_required"):
            failures.append("anking_required")
        if source == "anking" and _bool(card, "anking_required") and not _bool(card, "resolved_without_fallback"):
            failures.append("required_anking_unresolved")
        if source == "external_deck":
            _validate_anking_search_audit(card, failures)
        if source == "external_deck" and card.get("source_filter_required") is True and not _bool(card, "source_filter_ok"):
            failures.append("source_filter_ok")
        if _bool(card, "requires_visual", default=False) and not _bool(card, "visual_ok"):
            failures.append("visual_ok")

    elif source == "authored":
        _validate_authored(card, failures)
        _validate_anking_search_audit(card, failures)
        if not _bool(card, "anking_search_complete"):
            failures.append("anking_search_incomplete")
        if not str(card.get("anking_rejection_reason", "")).strip():
            failures.append("anking_rejection_reason_missing")
        if _bool(card, "requires_visual", default=False) and not _bool(card, "visual_ok"):
            failures.append("visual_ok")

    elif source == "io":
        _validate_io(card, failures)
        _validate_anking_search_audit(card, failures)

    else:
        failures.append("unsupported_source")

    return failures


def validate_report(data: dict[str, Any], min_score: float, min_margin: float) -> dict[str, Any]:
    cards = data.get("cards")
    if not isinstance(cards, list):
        raise ValueError("relatório sem lista cards")

    expected = int(data.get("expected_card_count", len(cards)))
    hard_max = int(data.get("card_budget_hard_max", expected))
    result: dict[str, Any] = {
        "expected_card_count": expected,
        "card_budget_hard_max": hard_max,
        "validated_card_count": len(cards),
        "passed_card_count": 0,
        "failed_card_count": 0,
        "all_cards_validated": expected == len(cards),
        "within_card_budget": expected <= hard_max,
        "cards": [],
    }

    seen: set[str] = set()
    for idx, raw in enumerate(cards, 1):
        if not isinstance(raw, dict):
            failures = ["not_an_object"]
            key = f"index:{idx}"
        else:
            key = str(raw.get("card_key") or f"index:{idx}")
            failures = validate_card(raw, min_score, min_margin)
            if key in seen:
                failures.append("duplicate_card_key")
            seen.add(key)
        ok = not failures
        result["cards"].append({"card_key": key, "ok": ok, "failures": failures})
        result["passed_card_count"] += int(ok)
        result["failed_card_count"] += int(not ok)

    result["ok"] = (
        expected > 0
        and result["all_cards_validated"]
        and result["within_card_budget"]
        and result["failed_card_count"] == 0
        and result["passed_card_count"] == expected
    )
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--min-score", type=float, default=DEFAULT_MIN_SCORE)
    ap.add_argument("--min-margin", type=float, default=DEFAULT_MIN_MARGIN)
    ap.add_argument("--out")
    args = ap.parse_args()

    data = json.loads(Path(args.report).read_text(encoding="utf-8"))
    result = validate_report(data, args.min_score, args.min_margin)
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
