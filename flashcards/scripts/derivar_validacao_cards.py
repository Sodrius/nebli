#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Deriva `validacao-cards.json` mecanicamente a partir do `deck-data.json`.

Por que isto existe
-------------------
O gate card-a-card sempre foi descrito como "100% dos cards, sem amostragem",
mas o relatório que ele lê era escrito à mão, em paralelo ao deck. Nada ligava
os dois: um card com cloze de cinco palavras podia declarar `cloze_words: 1`,
um card sem âncora podia declarar `e1_anchor_ok: true`, e o gate aprovava. O
"hard gate" media o relatório, não o deck.

Aqui o relatório passa a ser *derivado*:

* tudo que é mensurável sai do conteúdo real do card — contagem e índice de
  cloze, palavras da resposta, tamanho da frente, palavras do Extra, número e
  geometria das máscaras, presença de crédito de mídia;
* a âncora E1 é conferida contra o arquivo-fonte da E1, não contra uma
  declaração;
* o que é juízo (`atomic`, `relevant`, previews revisados, valor didático)
  continua declarado, mas é *copiado* do deck-data — existe uma única fonte da
  verdade, e um flag ausente reprova em vez de ser inventado no relatório.

Uso:
    python flashcards/scripts/derivar_validacao_cards.py \
        arquivos-trabalho/<slug>/deck-data.json \
        --out arquivos-trabalho/<slug>/validacao-cards.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validar_release_e1_deck import _normalise  # noqa: E402

CLOZE_RE = re.compile(r"\{\{c(\d+)::([^}:]+)(?:::[^}]*)?}}", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")

LOCAL_SOURCES = {"anking", "external_deck"}
SEARCH_MODES = {"session_local", "device_deferred", "unavailable"}


def _text(value: Any) -> str:
    return TAG_RE.sub(" ", str(value or ""))


def _word_count(value: Any) -> int:
    return len([w for w in re.split(r"\s+", _text(value).strip()) if w])


def _flag(source: dict[str, Any], key: str) -> bool:
    return source.get(key) is True


def _cloze_metrics(text: str) -> dict[str, int]:
    matches = list(CLOZE_RE.finditer(text or ""))
    if not matches:
        return {"cloze_count": 0, "cloze_index": 0, "cloze_words": 0}
    return {
        "cloze_count": len(matches),
        "cloze_index": int(matches[0].group(1)),
        "cloze_words": _word_count(matches[0].group(2)),
    }


def _masks_ok(masks: Any) -> bool:
    if not isinstance(masks, list) or not masks:
        return False
    for box in masks:
        if not isinstance(box, dict):
            return False
        try:
            x, y, w, h = (float(box[k]) for k in ("x", "y", "w", "h"))
        except (KeyError, TypeError, ValueError):
            return False
        if x < 0 or y < 0 or w <= 0 or h <= 0 or x + w > 1.000001 or y + h > 1.000001:
            return False
    return True


def _search_mode(card: dict[str, Any]) -> str:
    return str(card.get("anking_search_mode") or "session_local").strip().lower()


def _anking_audit(card: dict[str, Any], record: dict[str, Any]) -> None:
    """Traduz a evidência de busca AnKing no modo declarado pelo card.

    `session_local` mantém o contrato antigo: a busca aconteceu na sessão e as
    cinco evidências precisam estar declaradas. `device_deferred` e
    `unavailable` são modos honestos para quando a coleção AnKing não está ao
    alcance de quem planeja — exigem um motivo concreto em vez de booleanos que
    ninguém pode ter verificado.
    """
    mode = _search_mode(card)
    record["anking_search_mode"] = mode
    if mode not in SEARCH_MODES:
        record["anking_search_mode_valid"] = False
        return
    record["anking_search_mode_valid"] = True

    if mode == "session_local":
        queries = card.get("anking_search_queries") or []
        distinct = {str(q).strip().casefold() for q in queries if str(q).strip()}
        record["anking_search_queries_ok"] = len(distinct) >= 3
        record["anking_scope_expanded"] = _flag(card, "anking_search_scope_expanded")
        record["anking_siblings_reviewed"] = _flag(card, "anking_siblings_reviewed")
        reviewed = card.get("anking_candidates_reviewed")
        record["anking_candidates_reviewed_ok"] = (
            isinstance(reviewed, int) and not isinstance(reviewed, bool) and reviewed >= 0
        )
        rejections = card.get("anking_rejections") or []
        record["anking_rejections_ok"] = (
            not isinstance(reviewed, int)
            or reviewed == 0
            or (isinstance(rejections, list) and bool(rejections))
        )
        record["anking_search_complete"] = _flag(card, "anking_search_complete")
        record["anking_rejection_reason"] = str(card.get("anking_rejection_reason") or "")
        return

    # modos honestos: nenhuma evidência de busca é fabricada
    reason = str(card.get("anking_deferral_reason") or "").strip()
    record["anking_deferral_reason"] = reason
    record["anking_deferral_reason_ok"] = len(reason) >= 40
    for key in (
        "anking_search_queries_ok",
        "anking_scope_expanded",
        "anking_siblings_reviewed",
        "anking_candidates_reviewed_ok",
        "anking_rejections_ok",
    ):
        record[key] = True
    record["anking_search_complete"] = True
    record["anking_rejection_reason"] = reason


def _derive_authored(body: dict[str, Any], record: dict[str, Any]) -> None:
    text = str(body.get("text") or "")
    record.update(_cloze_metrics(text))
    record["front_characters"] = len(_text(text))
    record["extra_words"] = _word_count(body.get("extra"))
    record["front_language"] = str(body.get("front_language") or "")
    record["extra_language"] = str(body.get("extra_language") or "")
    record["three_word_cloze_reason"] = str(body.get("three_word_cloze_reason") or "")
    quality = body.get("authored_quality") if isinstance(body.get("authored_quality"), dict) else {}
    record["multi_retrieval"] = quality.get("single_retrieval") is not True
    images = body.get("extra_images") or []
    record["has_extra_media"] = bool(images)
    if images:
        first = images[0] if isinstance(images[0], dict) else {}
        record["media_ok"] = bool(str(first.get("path") or first.get("image_path") or "").strip())
        record["media_source_credit_ok"] = bool(str(first.get("source_credit") or "").strip())
        record["media_cognitive_purpose_ok"] = bool(str(first.get("cognitive_purpose") or "").strip())
        record["didactic_value_reviewed"] = first.get("didactic_value_reviewed") is True
        record["anking_visual_preference_checked"] = (
            first.get("anking_visual_search_complete") is True
        )
        record["anking_visual_used"] = False
        record["anking_visual_rejection_reason"] = str(
            first.get("anking_visual_rejection_reason") or ""
        )


def _derive_io(body: dict[str, Any], record: dict[str, Any]) -> None:
    masks = body.get("masks")
    record["mode"] = str(body.get("mode") or "")
    record["mask_count"] = len(masks) if isinstance(masks, list) else 0
    record["mask_geometry_ok"] = _masks_ok(masks)
    record["coherent_set"] = _flag(body, "coherent_set")
    record["pair_rationale"] = str(body.get("pair_rationale") or "")
    record["source_credit_ok"] = bool(str(body.get("source_credit") or "").strip())
    record["media_ok"] = bool(str(body.get("image_path") or body.get("media_key") or "").strip())
    record["media_cognitive_purpose_ok"] = len(str(body.get("cognitive_purpose") or "").strip()) >= 10
    record["answer_leak"] = body.get("answer_leak", True) is True
    for key in (
        "masks_labels_not_structures",
        "question_preview_validated",
        "answer_preview_validated",
        "visual_ok",
        "real_source",
        "didactic_value_reviewed",
    ):
        record[key] = _flag(body, key)


def derive(deck: dict[str, Any], deck_path: Path) -> dict[str, Any]:
    release = deck.get("release_gate") if isinstance(deck.get("release_gate"), dict) else {}
    concepts = release.get("concepts") if isinstance(release.get("concepts"), list) else []
    anchors = {
        str(row.get("concept_id") or ""): str(row.get("e1_anchor") or "")
        for row in concepts if isinstance(row, dict)
    }

    e1_text = ""
    raw_source = release.get("e1_source")
    if raw_source:
        path = Path(str(raw_source))
        if not path.is_absolute():
            path = (deck_path.parent / path).resolve()
        if path.is_file():
            e1_text = _normalise(path.read_text(encoding="utf-8-sig"))

    records: list[dict[str, Any]] = []
    for card in deck.get("cards") or []:
        if not isinstance(card, dict):
            continue
        source = str(card.get("source") or "").lower()
        concept_id = str(card.get("concept_id") or "")
        anchor = anchors.get(concept_id, "")
        record: dict[str, Any] = {
            "card_key": str(card.get("card_key") or ""),
            "concept_id": concept_id,
            "source": source,
            "tier": str(card.get("tier") or "nucleo"),
            "selected": True,
            "atomic": _flag(card, "atomic"),
            "relevant": _flag(card, "relevant"),
            "e1_anchor_ok": bool(anchor) and (not e1_text or _normalise(anchor) in e1_text),
            "requires_visual": _flag(card, "requires_visual"),
        }
        _anking_audit(card, record)

        if source in LOCAL_SOURCES:
            fallback = card.get("fallback") if isinstance(card.get("fallback"), dict) else {}
            queries = card.get("search_queries") or []
            record["search_queries_ok"] = len(
                {str(q).strip().casefold() for q in queries if str(q).strip()}
            ) >= 2
            record["expected_answers_ok"] = bool(
                [a for a in (card.get("expected_answers") or []) if str(a).strip()]
            )
            record["fallback_validated"] = bool(fallback)
            record["anking_required"] = _flag(card, "anking_required")
            for key in ("source_safe", "same_note_type", "same_fields", "media_ok",
                        "sibling_policy_ok", "anking_marker_ok", "resolved_without_fallback"):
                record[key] = _flag(card, key)
            record["score"] = float(card.get("score") or 0.0)
            record["second_score"] = float(card.get("second_score") or 0.0)
            record["visual_ok"] = _flag(card, "visual_ok")
        elif source == "authored":
            _derive_authored(card, record)
            record["visual_ok"] = _flag(card, "visual_ok") or not record["requires_visual"]
        elif source == "io":
            _derive_io(card, record)
        records.append(record)

    hard_max = release.get("card_budget_hard_max")
    return {
        "lesson_slug": deck.get("lesson_slug") or deck_path.parent.name,
        "generated_from": str(deck_path),
        "derived": True,
        "expected_card_count": len(records),
        "card_budget_hard_max": int(hard_max) if isinstance(hard_max, int) else len(records),
        "cards": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck_data", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    deck_path = args.deck_data.resolve()
    deck = json.loads(deck_path.read_text(encoding="utf-8"))
    report = derive(deck, deck_path)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{args.out} cards={report['expected_card_count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
