import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "validar_deck_card_a_card.py"
spec = importlib.util.spec_from_file_location("gate", SCRIPT)
gate = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gate)


def base(i: int, source: str) -> dict:
    return {
        "card_key": f"concept-{i:02d}:{source}",
        "concept_id": f"concept-{i:02d}",
        "source": source,
        "tier": "nucleo" if i <= 36 else "optional",
        "selected": True,
        "atomic": True,
        "relevant": True,
        "e1_anchor_ok": True,
    }


def anking_card(i: int) -> dict:
    return {
        **base(i, "anking"),
        "source_safe": True,
        "same_note_type": True,
        "same_fields": True,
        "media_ok": True,
        "sibling_policy_ok": True,
        "fallback_validated": True,
        "anking_marker_ok": True,
        "score": 0.94,
        "second_score": 0.63,
        "exact_phrase": True,
        "requires_visual": False,
    }


def external_card(i: int) -> dict:
    return {
        **base(i, "external_deck"),
        "source_safe": True,
        "same_note_type": True,
        "same_fields": True,
        "media_ok": True,
        "sibling_policy_ok": True,
        "fallback_validated": True,
        "source_filter_required": True,
        "source_filter_ok": True,
        "score": 0.91,
        "second_score": 0.62,
        "exact_phrase": True,
        "requires_visual": False,
    }


def authored_card(i: int) -> dict:
    return {
        **base(i, "authored"),
        "front_language": "en",
        "extra_language": "pt-BR",
        "cloze_count": 1,
        "cloze_index": 1,
        "cloze_words": 1,
        "extra_words": 24,
        "front_characters": 92,
        "multi_retrieval": False,
        "requires_visual": False,
        "has_extra_media": False,
    }


def io_card(i: int) -> dict:
    return {
        **base(i, "io"),
        "requires_visual": True,
        "mode": "hide_all_guess_all",
        "mask_count": 2,
        "coherent_set": True,
        "masks_labels_not_structures": True,
        "question_preview_validated": True,
        "answer_preview_validated": True,
        "visual_ok": True,
        "real_source": True,
        "source_credit_ok": True,
        "answer_leak": False,
        "mask_geometry_ok": True,
        "media_ok": True,
    }


def realistic_40_card_report() -> dict:
    cards = []
    cards.extend(anking_card(i) for i in range(1, 29))
    cards.extend(external_card(i) for i in range(29, 31))
    cards.extend(authored_card(i) for i in range(31, 37))
    cards.extend(io_card(i) for i in range(37, 41))
    return {"expected_card_count": 40, "card_budget_hard_max": 45, "cards": cards}


def test_realistic_40_card_deck_requires_40_of_40():
    result = gate.validate_report(realistic_40_card_report(), 0.82, 0.06)
    assert result["ok"] is True
    assert result["validated_card_count"] == 40
    assert result["passed_card_count"] == 40
    assert result["failed_card_count"] == 0
    assert result["within_card_budget"] is True


def test_one_bad_anking_copy_blocks_whole_realistic_deck():
    report = realistic_40_card_report()
    report["cards"][17]["same_fields"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert result["passed_card_count"] == 39
    assert "same_fields" in result["cards"][17]["failures"]


def test_missing_card_blocks_even_if_every_present_card_is_good():
    report = realistic_40_card_report()
    report["cards"].pop()
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert result["expected_card_count"] == 40
    assert result["validated_card_count"] == 39
    assert result["all_cards_validated"] is False


def test_duplicate_card_key_blocks_deck():
    report = realistic_40_card_report()
    report["cards"][1]["card_key"] = report["cards"][0]["card_key"]
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert "duplicate_card_key" in result["cards"][1]["failures"]


def test_bad_authored_cloze_blocks_card():
    report = realistic_40_card_report()
    card = report["cards"][31]
    card["cloze_words"] = 4
    card["cloze_count"] = 2
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    failures = result["cards"][31]["failures"]
    assert "cloze_words>3" in failures
    assert "cloze_count_must_be_1" in failures


def test_three_word_authored_cloze_requires_reason():
    report = realistic_40_card_report()
    report["cards"][31]["cloze_words"] = 3
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert "three_word_cloze_without_reason" in result["cards"][31]["failures"]
    report["cards"][31]["three_word_cloze_reason"] = "The anatomical name is irreducibly three words."
    assert gate.validate_report(report, 0.82, 0.06)["ok"] is True


def test_authored_extra_media_requires_source_and_cognitive_purpose():
    report = realistic_40_card_report()
    card = report["cards"][31]
    card["has_extra_media"] = True
    card["media_ok"] = True
    card["media_source_credit_ok"] = False
    card["media_cognitive_purpose_ok"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    failures = result["cards"][31]["failures"]
    assert "media_source_credit_ok" in failures
    assert "media_cognitive_purpose_ok" in failures


def test_bad_io_blocks_card_even_if_visual_ok_is_true():
    report = realistic_40_card_report()
    card = report["cards"][38]
    card["answer_leak"] = True
    card["masks_labels_not_structures"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    failures = result["cards"][38]["failures"]
    assert "answer_leak" in failures
    assert "masks_labels_not_structures" in failures


def test_io_without_source_credit_blocks():
    report = realistic_40_card_report()
    report["cards"][38]["source_credit_ok"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert "source_credit_ok" in result["cards"][38]["failures"]


def test_anking_without_validated_fallback_blocks():
    report = realistic_40_card_report()
    report["cards"][3]["fallback_validated"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert "fallback_validated" in result["cards"][3]["failures"]


def test_anking_without_marker_blocks():
    report = realistic_40_card_report()
    report["cards"][3]["anking_marker_ok"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert "anking_marker_ok" in result["cards"][3]["failures"]


def test_external_deck_uses_same_rank_and_fallback_gates():
    report = realistic_40_card_report()
    card = report["cards"][28]
    card["score"] = 0.55
    card["fallback_validated"] = False
    card["source_filter_ok"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    failures = result["cards"][28]["failures"]
    assert "local_deck_rank" in failures
    assert "fallback_validated" in failures
    assert "source_filter_ok" in failures


def test_card_budget_is_hard_gate():
    report = realistic_40_card_report()
    report["card_budget_hard_max"] = 39
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert result["within_card_budget"] is False


def test_missing_e1_anchor_blocks():
    report = realistic_40_card_report()
    report["cards"][0]["e1_anchor_ok"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert "e1_anchor_ok" in result["cards"][0]["failures"]
