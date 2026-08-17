#!/usr/bin/env python3
"""Valida a revisão final independente contra o hash exato do lote de cards."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from canonical_cards import ordered_card_set_sha256

REQUIRED_DIMENSIONS = {
    "learning_delta",
    "ambiguity",
    "anti_induction",
    "redundancy",
    "step1_scope",
    "visual",
}


def validate_card_review(data: dict[str, Any]) -> dict[str, Any]:
    cards = [card for card in data.get("cards", []) if isinstance(card, dict)]
    expected_hash = ordered_card_set_sha256(cards)
    release = data.get("release_gate") or {}
    review = release.get("card_review")
    errors: list[str] = []
    if not isinstance(review, dict):
        return {"passed": False, "errors": ["release_gate.card_review obrigatório"], "ordered_card_set_sha256": expected_hash}
    if review.get("reviewer_stage") != "independent":
        errors.append("card_review.reviewer_stage deve ser independent")
    if str(review.get("reviewed_card_set_sha256") or "") != expected_hash:
        errors.append("card_review.reviewed_card_set_sha256 diverge do lote atual")
    dims = review.get("reviewed_dimensions")
    if not isinstance(dims, list):
        errors.append("card_review.reviewed_dimensions deve ser lista")
    else:
        missing = sorted(REQUIRED_DIMENSIONS - {str(item) for item in dims})
        if missing:
            errors.append("card_review.reviewed_dimensions incompleto: " + ", ".join(missing))
    findings = review.get("blocking_findings")
    if not isinstance(findings, list):
        errors.append("card_review.blocking_findings deve ser lista")
    elif findings:
        errors.append("card_review.blocking_findings precisa estar vazio para liberar")
    if len(str(review.get("summary") or "").strip()) < 20:
        errors.append("card_review.summary precisa registrar a revisão final")
    return {"passed": not errors, "errors": errors, "ordered_card_set_sha256": expected_hash}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck_data", type=Path)
    args = parser.parse_args()
    data = json.loads(args.deck_data.read_text(encoding="utf-8"))
    result = validate_card_review(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
