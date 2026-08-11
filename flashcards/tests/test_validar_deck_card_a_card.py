import importlib.util
import json
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "validar_deck_card_a_card.py"
spec = importlib.util.spec_from_file_location("gate", SCRIPT)
gate = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gate)


def anking_card(i: int) -> dict:
    return {
        "card_key": f"concept-{i:02d}:nid-{1000+i}:ord-0",
        "concept_id": f"concept-{i:02d}",
        "source": "anking",
        "selected": True,
        "atomic": True,
        "relevant": True,
        "source_safe": True,
        "same_note_type": True,
        "same_fields": True,
        "media_ok": True,
        "sibling_policy_ok": True,
        "score": 0.94,
        "second_score": 0.63,
        "exact_phrase": True,
        "requires_visual": False,
    }


def authored_card(i: int) -> dict:
    return {
        "card_key": f"concept-{i:02d}:authored",
        "concept_id": f"concept-{i:02d}",
        "source": "authored",
        "selected": True,
        "atomic": True,
        "relevant": True,
        "source_safe": True,
        "cloze_words": 1,
        "requires_visual": False,
    }


def io_card(i: int) -> dict:
    return {
        "card_key": f"concept-{i:02d}:io",
        "concept_id": f"concept-{i:02d}",
        "source": "io",
        "selected": True,
        "atomic": True,
        "relevant": True,
        "source_safe": True,
        "requires_visual": True,
        "visual_ok": True,
    }


def realistic_40_card_report() -> dict:
    # Distribuição deliberadamente parecida com um deck-aula real:
    # maioria AnKing, poucos autorais para lacunas e poucos IO.
    cards = []
    cards.extend(anking_card(i) for i in range(1, 31))
    cards.extend(authored_card(i) for i in range(31, 37))
    cards.extend(io_card(i) for i in range(37, 41))
    return {"expected_card_count": 40, "cards": cards}


def test_realistic_40_card_deck_requires_40_of_40():
    result = gate.validate_report(realistic_40_card_report(), 0.82, 0.06)
    assert result["ok"] is True
    assert result["validated_card_count"] == 40
    assert result["passed_card_count"] == 40
    assert result["failed_card_count"] == 0


def test_one_bad_card_blocks_whole_realistic_deck():
    report = realistic_40_card_report()
    report["cards"][17]["same_fields"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert result["validated_card_count"] == 40
    assert result["passed_card_count"] == 39
    assert result["failed_card_count"] == 1
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


def test_bad_cloze_or_visual_blocks_card():
    report = realistic_40_card_report()
    report["cards"][31]["cloze_words"] = 4
    report["cards"][38]["visual_ok"] = False
    result = gate.validate_report(report, 0.82, 0.06)
    assert result["ok"] is False
    assert result["failed_card_count"] == 2
