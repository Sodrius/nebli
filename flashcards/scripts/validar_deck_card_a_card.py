#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gate final card-a-card para decks NEBLI/AnkiDroid.

Valida o lote REAL produzido pela aula. Não trabalha por amostragem: todo card
previsto deve ter um registro em ``cards`` e todo registro precisa passar seus
gates. O processo retorna código != 0 se houver qualquer falha.

Formato mínimo do relatório:
{
  "expected_card_count": 40,
  "cards": [
    {
      "card_key": "concept-01:nid-123:ord-0",
      "concept_id": "concept-01",
      "source": "anking",
      "selected": true,
      "atomic": true,
      "relevant": true,
      "source_safe": true,
      "same_note_type": true,
      "same_fields": true,
      "media_ok": true,
      "sibling_policy_ok": true,
      "visual_ok": true,
      "score": 0.94,
      "second_score": 0.71,
      "exact_phrase": true
    }
  ]
}

Para cards autorais/IO, campos específicos de cópia AnKing podem ser omitidos,
mas os gates de atomicidade, relevância e visual continuam obrigatórios.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

DEFAULT_MIN_SCORE = 0.82
DEFAULT_MIN_MARGIN = 0.06


def _bool(card: dict[str, Any], key: str, *, default: bool | None = None) -> bool:
    if key not in card:
        if default is None:
            return False
        return default
    return card.get(key) is True


def _anking_rank_ok(card: dict[str, Any], min_score: float, min_margin: float) -> bool:
    if card.get("source") != "anking":
        return True
    score = float(card.get("score", 0.0))
    second = float(card.get("second_score", 0.0))
    exact = bool(card.get("exact_phrase", False))
    if score < min_score:
        return False
    if score >= 0.96:
        return True
    if exact and score >= max(0.88, min_score):
        return True
    return score - second >= min_margin


def validate_card(card: dict[str, Any], min_score: float, min_margin: float) -> list[str]:
    failures: list[str] = []
    source = str(card.get("source", "")).lower()

    for key in ("card_key", "concept_id", "source"):
        if not card.get(key):
            failures.append(f"missing:{key}")

    for key in ("selected", "atomic", "relevant", "source_safe"):
        if not _bool(card, key):
            failures.append(key)

    if not _anking_rank_ok(card, min_score, min_margin):
        failures.append("anking_rank")

    if source in {"anking", "external_deck"}:
        for key in ("same_note_type", "same_fields", "media_ok", "sibling_policy_ok"):
            if not _bool(card, key):
                failures.append(key)

    # visual_ok é obrigatório quando o card declara necessidade visual/IO.
    if card.get("requires_visual") or source == "io":
        if not _bool(card, "visual_ok"):
            failures.append("visual_ok")

    # Cloze autoral: máximo canônico de 3 palavras por lacuna.
    if source == "authored" and card.get("cloze_words") is not None:
        if int(card["cloze_words"]) > 3:
            failures.append("cloze_words>3")

    return failures


def validate_report(data: dict[str, Any], min_score: float, min_margin: float) -> dict[str, Any]:
    cards = data.get("cards")
    if not isinstance(cards, list):
        raise ValueError("relatório sem lista cards")

    expected = int(data.get("expected_card_count", len(cards)))
    result: dict[str, Any] = {
        "expected_card_count": expected,
        "validated_card_count": len(cards),
        "passed_card_count": 0,
        "failed_card_count": 0,
        "all_cards_validated": expected == len(cards),
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
        result["all_cards_validated"]
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
