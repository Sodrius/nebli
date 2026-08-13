#!/usr/bin/env python3
"""Valida 100% dos cards canônicos e produz relatório ligado ao conteúdo por hash."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from canonical_cards import ACTIVE_SOURCES, CLOZE_RE, content_sha256, derived, media_hashes, normalized, ordered_card_set_sha256, referenced_media_hashes, words

GENERIC = {"coisa", "processo", "estrutura", "função", "mecanismo", "elemento", "substância"}


def _semantic_review_ok(card: dict[str, Any], failures: list[str]) -> None:
    review = card.get("semantic_review")
    if not isinstance(review, dict):
        failures.append("semantic_review_missing")
        return
    for key in ("ambiguity", "anti_induction", "duplicate_check"):
        if len(str(review.get(key) or "").strip()) < 12: failures.append(f"semantic_review.{key}")


def _authored(card: dict[str, Any], failures: list[str]) -> None:
    text, extra = str(card.get("text") or ""), str(card.get("extra") or "")
    metrics = derived(card)
    if metrics["probable_language"] != "pt-BR": failures.append("front_or_extra_not_portuguese")
    if metrics["cloze_occurrences"] != 1: failures.append("exactly_one_c1_occurrence_required")
    if metrics["cloze_indices"] != [1]: failures.append("cloze_index_must_be_c1")
    count = metrics["cloze_answer_words"][0] if metrics["cloze_answer_words"] else 0
    if count < 1 or count > 3: failures.append("cloze_answer_must_have_1_to_3_words")
    if count == 3 and not str(card.get("three_word_cloze_reason") or "").strip(): failures.append("three_word_cloze_requires_reason")
    if metrics["answer_visible"]: failures.append("lexical_leak_or_visible_answer")
    if metrics["front_characters"] > 360: failures.append("front_over_360_characters")
    if metrics["extra_words"] > 100: failures.append("extra_over_100_words")
    answers = [normalized(match.group(2)) for match in CLOZE_RE.finditer(text)]
    if any(answer in GENERIC for answer in answers): failures.append("generic_cloze")
    if answers and len(words(answers[0])) >= 3 and len(words(CLOZE_RE.sub("", text))) < 4: failures.append("whole_clause_or_definition_cloze")
    if not str(card.get("retrieval_target") or "").strip(): failures.append("retrieval_target_missing")
    if not extra.strip(): failures.append("extra_missing")
    _semantic_review_ok(card, failures)


def _io(card: dict[str, Any], failures: list[str]) -> None:
    if card.get("mode") != "hide_two_guess_two": failures.append("io_mode_must_be_hide_two_guess_two")
    masks, answers = card.get("masks"), card.get("answers")
    if not isinstance(masks, list) or not 1 <= len(masks) <= 2: failures.append("io_masks_must_be_1_or_2")
    if not isinstance(answers, list) or not isinstance(masks, list) or len(answers) != len(masks): failures.append("io_answers_must_match_masks")
    if isinstance(masks, list):
        for index, mask in enumerate(masks):
            try:
                x, y, w, h = (float(mask[k]) for k in ("x", "y", "w", "h"))
                if x < 0 or y < 0 or w <= 0 or h <= 0 or x + w > 1 or y + h > 1: failures.append(f"io_mask_out_of_bounds:{index}")
            except (KeyError, TypeError, ValueError): failures.append(f"io_mask_invalid:{index}")
    if isinstance(masks, list) and len(masks) == 2 and len(str(card.get("pair_rationale") or "").strip()) < 12: failures.append("io_pair_rationale_missing")
    for key in ("prompt", "source_credit", "cognitive_purpose"):
        if not str(card.get(key) or "").strip(): failures.append(f"io_{key}_missing")
    if not str(card.get("media_key") or card.get("image_path") or "").strip(): failures.append("io_media_missing")
    if derived({"text": str(card.get("prompt") or ""), "extra": ""})["probable_language"] != "pt-BR": failures.append("io_prompt_not_portuguese")
    if any(not str(answer).strip() for answer in answers or []): failures.append("io_empty_answer")
    review = card.get("visual_review")
    if not isinstance(review, dict): failures.append("io_visual_review_missing")
    else:
        for key in ("labels_masked_not_structures", "question_preview", "answer_preview", "legible", "no_leak", "didactic_value"):
            if review.get(key) is not True: failures.append(f"visual_review.{key}")


def validate_card(card: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for key in ("card_key", "concept_id", "tier", "source", "e1_anchor"):
        if not str(card.get(key) or "").strip(): failures.append(f"missing:{key}")
    source = str(card.get("source") or "").lower()
    if source not in ACTIVE_SOURCES: failures.append("source_not_allowed_in_authored_only")
    elif source == "authored": _authored(card, failures)
    else: _io(card, failures)
    if str(card.get("tier") or "") not in {"nucleo", "optional"}: failures.append("invalid_tier")
    return failures


def validate_report(data: dict[str, Any], *_unused: Any) -> dict[str, Any]:
    cards = data.get("cards")
    if not isinstance(cards, list): raise ValueError("entrada sem lista cards")
    expected = int(data.get("expected_card_count", len(cards)))
    hard_max = int(data.get("card_budget_hard_max", data.get("release_gate", {}).get("card_budget_hard_max", expected)))
    seen: set[str] = set(); rows = []; passed = 0
    for index, raw in enumerate(cards):
        card = raw if isinstance(raw, dict) else {}
        key = str(card.get("card_key") or f"index:{index}")
        failures = validate_card(card) if isinstance(raw, dict) else ["not_an_object"]
        if key in seen: failures.append("duplicate_card_key")
        seen.add(key); ok = not failures; passed += int(ok)
        rows.append({"card_key": key, "content_sha256": content_sha256(card), "result": "passed" if ok else "failed", "failures": failures})
    set_hash = ordered_card_set_sha256([card for card in cards if isinstance(card, dict)])
    result = {"schema": "nebli-card-validation-v2", "expected_card_count": expected, "card_budget_hard_max": hard_max, "validated_card_count": len(cards), "passed_card_count": passed, "failed_card_count": len(cards)-passed, "ordered_card_set_sha256": set_hash, "media": media_hashes(data), "cards": rows}
    result["ok"] = expected > 0 and expected == len(cards) == passed and expected <= hard_max
    return result


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("--out")
    args = ap.parse_args(); data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = validate_report(data)
    result["media"] = referenced_media_hashes([c for c in data.get("cards", []) if isinstance(c, dict)], Path(args.input).resolve().parent)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out: Path(args.out).write_text(payload, encoding="utf-8")
    print(payload, end=""); return 0 if result["ok"] else 1


if __name__ == "__main__": raise SystemExit(main())
