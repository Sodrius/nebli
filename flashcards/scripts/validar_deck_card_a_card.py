#!/usr/bin/env python3
"""Valida 100% dos cards canônicos e produz relatório ligado ao conteúdo por hash."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from canonical_cards import ACTIVE_SOURCES, CLOZE_RE, content_sha256, derived, media_hashes, normalized, ordered_card_set_sha256, referenced_media_hashes, words
from card_cue_quality import (
    abstract_answer_failures,
    alternative_answer_failures,
    anchor_coverage_failures,
    discriminator_placement_failures,
    portuguese_front_failures,
    portuguese_text_failures,
    semantic_cue_review_failures,
    type_hint_failures,
)
from feedback_regressions import regression_failures

# Campos do contrato de ablação: um card só existe se a sua remoção causa perda
# nomeável. Ver docs/canon/NUCLEO-DE-RETENCAO.md.
ABLATION_FIELDS = ("memory_gain", "ablation_loss", "why_not_e1_only", "confusion_target")

# Teto de estilo da frente (config/pipeline.json → authored_cards.style_max_front_characters).
# O teto duro de 360 caracteres continua valendo; este é o limite da voz seca.
STYLE_FRONT_LIMIT = 180


def _semantic_review_ok(card: dict[str, Any], failures: list[str]) -> None:
    review = card.get("semantic_review")
    if not isinstance(review, dict):
        failures.append("semantic_review_missing")
        return
    for key in ("ambiguity", "anti_induction", "duplicate_check"):
        if len(str(review.get(key) or "").strip()) < 12: failures.append(f"semantic_review.{key}")


def _ablation_ok(card: dict[str, Any], failures: list[str]) -> None:
    for key in ABLATION_FIELDS:
        if len(str(card.get(key) or "").strip()) < 12: failures.append(f"ablation.{key}")
    loss = set(normalized(str(card.get("ablation_loss") or "")).split())
    if not loss: return
    restated = set(normalized(CLOZE_RE.sub(" ", str(card.get("text") or "")) + " " + str(card.get("retrieval_target") or "")).split())
    # Perda que só reformula o próprio card não é perda: precisa citar outra
    # recuperação ou outro conceito do contrato.
    if len(loss & restated) / len(loss) > 0.8: failures.append("ablation_loss_restates_card")


def _authored(card: dict[str, Any], failures: list[str]) -> None:
    text, extra = str(card.get("text") or ""), str(card.get("extra") or "")
    metrics = derived(card)
    # A frente é medida sozinha: um Extra em português não pode mais mascarar
    # uma frente inglesa, que foi como o lote UC03 inteiro passou.
    failures.extend(portuguese_front_failures(text, "pt-BR"))
    if extra.strip(): failures.extend(portuguese_text_failures(extra, "pt-BR", "extra"))
    if metrics["cloze_occurrences"] != 1: failures.append("exactly_one_c1_occurrence_required")
    if metrics["cloze_indices"] != [1]: failures.append("cloze_index_must_be_c1")
    count = metrics["cloze_answer_words"][0] if metrics["cloze_answer_words"] else 0
    if count < 1 or count > 3: failures.append("cloze_answer_must_have_1_to_3_words")
    if count == 3 and not str(card.get("three_word_cloze_reason") or "").strip(): failures.append("three_word_cloze_requires_reason")
    if metrics["answer_visible"]: failures.append("lexical_leak_or_visible_answer")
    if metrics["front_characters"] > 360: failures.append("front_over_360_characters")
    # Teto de estilo: o card é afirmação seca, não parágrafo de apostila (A20).
    # Acima do limite, exige justificativa escrita em vez de bloquear cego.
    if metrics["style_front_characters"] > STYLE_FRONT_LIMIT and not str(card.get("long_front_reason") or "").strip():
        failures.append(f"front_over_style_limit_{STYLE_FRONT_LIMIT}")
    if metrics["extra_words"] > 100: failures.append("extra_over_100_words")
    answers = [normalized(match.group(2)) for match in CLOZE_RE.finditer(text)]
    failures.extend(abstract_answer_failures(text))
    failures.extend(discriminator_placement_failures(card))
    failures.extend(alternative_answer_failures(card))
    failures.extend(anchor_coverage_failures(card))
    failures.extend(type_hint_failures(card))
    if answers and len(words(answers[0])) >= 3 and len(words(CLOZE_RE.sub("", text))) < 4: failures.append("whole_clause_or_definition_cloze")
    if not str(card.get("retrieval_target") or "").strip(): failures.append("retrieval_target_missing")
    if not extra.strip(): failures.append("extra_missing")
    _semantic_review_ok(card, failures)
    _ablation_ok(card, failures)
    failures.extend(semantic_cue_review_failures(card, strict=True))
    failures.extend(regression_failures(card))


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
    _io_visual_evidence(card, failures)


def _io_visual_evidence(card: dict[str, Any], failures: list[str]) -> None:
    """Exige prova renderizada, não seis booleanos que o agente escreveu.

    O IO de jejuno × íleo mostrou que `no_leak: true` convive com a resposta
    impressa no título: a declaração precisa vir acompanhada dos dois previews,
    do recorte usado e da varredura de texto que confirma a ausência de vazamento.
    """
    evidence = card.get("visual_evidence")
    if not isinstance(evidence, dict):
        failures.append("io_visual_evidence_missing")
        return
    for key in ("question_preview", "answer_preview"):
        if not str(evidence.get(key) or "").strip(): failures.append(f"visual_evidence.{key}")
        if len(str(evidence.get(f"{key}_sha256") or "").strip()) != 64: failures.append(f"visual_evidence.{key}_sha256")
    try:
        ratio = float(evidence.get("crop_ratio"))
    except (TypeError, ValueError):
        failures.append("visual_evidence.crop_ratio")
    else:
        # Recorte que é praticamente o slide inteiro não é IO: é o slide com uma
        # caixa por cima, e a resposta costuma sobrar em título ou legenda.
        if not 0 < ratio < 0.90: failures.append("io_crop_is_whole_slide")
    if str(evidence.get("text_scan") or "") not in {"ocr", "manual_review"}:
        failures.append("visual_evidence.text_scan")
    terms = evidence.get("forbidden_terms")
    if not isinstance(terms, list) or not terms:
        failures.append("visual_evidence.forbidden_terms")
    else:
        listed = {normalized(str(term)) for term in terms}
        for answer in card.get("answers") or []:
            if normalized(str(answer)) not in listed: failures.append("io_answer_not_listed_as_forbidden_term")
    leaked = evidence.get("leaked_terms")
    if not isinstance(leaked, list): failures.append("visual_evidence.leaked_terms_must_be_list")
    elif leaked: failures.append("io_answer_leaks_outside_mask")
    masks = card.get("masks")
    if isinstance(masks, list) and len(masks) == 2:
        # "Anterior/superficial" + "Patient right" passou como par: a justificativa
        # precisa dizer que relação une os dois, não repetir os rótulos.
        rationale = {word for word in normalized(str(card.get("pair_rationale") or "")).split() if len(word) >= 4}
        answers = {word for answer in card.get("answers") or [] for word in normalized(str(answer)).split()}
        if len(rationale - answers) < 3: failures.append("io_pair_rationale_only_repeats_labels")


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


def _declared_hard_max(data: dict[str, Any]) -> int | None:
    """Teto congelado do contrato. Ausente bloqueia — nunca vira `expected`."""
    for source in (data, data.get("release_gate") if isinstance(data.get("release_gate"), dict) else {}):
        value = (source or {}).get("card_budget_hard_max")
        if value is not None:
            try: return int(value)
            except (TypeError, ValueError): return None
    return None


def _duplicate_retrievals(cards: list[dict[str, Any]]) -> dict[str, list[str]]:
    """Agrupa cards que recuperam a mesma coisa, por resposta e por alvo.

    Dois cards no mesmo grupo cobram a mesma recuperação duas vezes por dia.
    Só sobrevivem os dois se um declarar `derivation_rationale`.
    """
    groups: dict[str, list[str]] = {}
    for card in cards:
        key = str(card.get("card_key") or "")
        for prefix, value in (
            ("answer", " ".join(normalized(m.group(2)) for m in CLOZE_RE.finditer(str(card.get("text") or "")))),
            ("target", normalized(str(card.get("retrieval_target") or ""))),
        ):
            if value: groups.setdefault(f"{prefix}:{value}", []).append(key)
    return {group: keys for group, keys in groups.items() if len(keys) > 1}


def validate_report(data: dict[str, Any], *_unused: Any) -> dict[str, Any]:
    cards = data.get("cards")
    if not isinstance(cards, list): raise ValueError("entrada sem lista cards")
    expected = int(data.get("expected_card_count", len(cards)))
    hard_max = _declared_hard_max(data)
    objects = [card for card in cards if isinstance(card, dict)]
    duplicates = _duplicate_retrievals(objects)
    shared = {key for keys in duplicates.values() for key in keys}
    seen: set[str] = set(); rows = []; passed = 0
    for index, raw in enumerate(cards):
        card = raw if isinstance(raw, dict) else {}
        key = str(card.get("card_key") or f"index:{index}")
        failures = validate_card(card) if isinstance(raw, dict) else ["not_an_object"]
        if key in seen: failures.append("duplicate_card_key")
        if key in shared and len(str(card.get("derivation_rationale") or "").strip()) < 12:
            failures.append("duplicate_retrieval")
        seen.add(key); ok = not failures; passed += int(ok)
        rows.append({"card_key": key, "content_sha256": content_sha256(card), "result": "passed" if ok else "failed", "failures": failures})
    set_hash = ordered_card_set_sha256(objects)
    report_failures: list[str] = []
    if hard_max is None: report_failures.append("card_budget_hard_max_missing")
    elif expected > hard_max: report_failures.append(f"card_budget_exceeded:{expected}>{hard_max}")
    result = {"schema": "nebli-card-validation-v2", "expected_card_count": expected, "card_budget_hard_max": hard_max, "validated_card_count": len(cards), "passed_card_count": passed, "failed_card_count": len(cards)-passed, "ordered_card_set_sha256": set_hash, "media": media_hashes(data), "duplicate_retrievals": duplicates, "report_failures": report_failures, "cards": rows}
    result["ok"] = expected > 0 and expected == len(cards) == passed and not report_failures
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
