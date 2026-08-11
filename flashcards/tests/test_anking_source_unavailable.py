"""Fonte AnKing inalcançável não pode virar evidência de busca fabricada.

A resolução AnKing do v9 depende da coleção local (AnkiDroid) ou de um índice
privado local. Quando a sessão que planeja o deck não alcança nenhum dos dois,
o canônico exige declarar a indisponibilidade — nunca declarar busca completa,
nunca planejar `source=anking` sem curadoria real.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

from validar_deck_card_a_card import validate_report  # noqa: E402
from test_release_e1_deck import (  # noqa: E402
    authored_fallback,
    canonical_data,
    run_canonical,
)

FINALIZER = Path(__file__).parents[1] / "scripts" / "finalizar_entrega_canonica.py"

UNAVAILABLE = {
    "available": False,
    "reason": (
        "Sessão remota sem coleção AnkiDroid montada e sem índice privado local; "
        "o canônico proíbe versionar AnKing no repositório."
    ),
    "checked": ["AnkiDroid ContentProvider", "índice privado local"],
}

UPGRADE_QUERIES = [
    "TLR4 lipopolysaccharide recognition",
    "TLR4 LPS innate immunity",
    "bacterial LPS pattern recognition receptor",
]


def unavailable_authored_card() -> dict:
    return {
        "card_key": "tlr4-lps",
        "concept_id": "c-tlr4",
        "tier": "nucleo",
        "atomic": True,
        "relevant": True,
        **authored_fallback(),
        "anking_search_status": "source_unavailable",
        "anking_upgrade_queries": list(UPGRADE_QUERIES),
    }


def unavailable_deck(tmp_path: Path) -> dict:
    data = canonical_data(tmp_path)
    data["anking_source_availability"] = dict(UNAVAILABLE)
    data["cards"] = [unavailable_authored_card()]
    return data


def test_declared_unavailable_source_allows_authored_card_with_upgrade_queries(tmp_path):
    proc, out = run_canonical(tmp_path, unavailable_deck(tmp_path))
    assert proc.returncode == 0, proc.stderr
    manifest = json.loads(out.read_text(encoding="utf-8"))
    assert manifest["anking_source_availability"]["available"] is False
    card = manifest["cards"][0]
    assert card["anking_upgrade_pending"] is True
    assert card["anking_upgrade_queries"] == UPGRADE_QUERIES


def test_unavailable_source_cannot_claim_completed_anking_search(tmp_path):
    data = unavailable_deck(tmp_path)
    data["cards"][0]["anking_search_complete"] = True
    proc, out = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert not out.exists()
    assert "anking_search_complete=true" in (proc.stdout + proc.stderr)


def test_unavailable_source_requires_three_upgrade_queries(tmp_path):
    data = unavailable_deck(tmp_path)
    data["cards"][0]["anking_upgrade_queries"] = ["TLR4"]
    proc, _ = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert "anking_upgrade_queries" in (proc.stdout + proc.stderr)


def test_unavailability_requires_concrete_reason_and_checked_paths(tmp_path):
    data = unavailable_deck(tmp_path)
    data["anking_source_availability"] = {"available": False, "reason": "sem AnKing"}
    proc, _ = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert "reason concreto" in (proc.stdout + proc.stderr)


def test_anking_card_is_blocked_while_source_is_unavailable(tmp_path):
    data = canonical_data(tmp_path)
    data["anking_source_availability"] = dict(UNAVAILABLE)
    proc, _ = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert "source=anking" in (proc.stdout + proc.stderr)


def _report(**overrides) -> dict:
    card = {
        "card_key": "tlr4-lps",
        "concept_id": "c-tlr4",
        "source": "authored",
        "tier": "nucleo",
        "selected": True,
        "atomic": True,
        "relevant": True,
        "e1_anchor_ok": True,
        "front_language": "en",
        "extra_language": "pt-BR",
        "cloze_count": 1,
        "cloze_index": 1,
        "cloze_words": 1,
        "extra_words": 12,
        "front_characters": 60,
        "anking_search_status": "source_unavailable",
        "anking_upgrade_queries_ok": True,
    }
    card.update(overrides)
    return {
        "expected_card_count": 1,
        "card_budget_hard_max": 25,
        "anking_source_available": False,
        "cards": [card],
    }


def test_validator_accepts_declared_unavailable_source():
    result = validate_report(_report(), 0.82, 0.06)
    assert result["ok"] is True, result["cards"]
    assert result["anking_source_available"] is False


def test_validator_still_requires_the_unavailable_marker():
    result = validate_report(_report(anking_search_status="done"), 0.82, 0.06)
    assert result["ok"] is False
    assert "anking_search_status_source_unavailable" in result["cards"][0]["failures"]


def test_validator_rejects_anking_card_when_source_is_unavailable():
    result = validate_report(_report(source="anking"), 0.82, 0.06)
    assert result["ok"] is False
    assert "anking_source_unavailable" in result["cards"][0]["failures"]


def test_finalizer_blocks_mismatch_between_deck_and_report(tmp_path):
    # deck-data não declara indisponibilidade; o relatório declara.
    deck = tmp_path / "deck-data.json"
    deck.write_text(json.dumps(canonical_data(tmp_path)), encoding="utf-8")
    report = tmp_path / "validacao-cards.json"
    report.write_text(json.dumps(_report()), encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(FINALIZER), "--slug", "reconhecimento-inato",
         "--deck-data", str(deck), "--validation-report", str(report),
         "--out-dir", str(tmp_path / "entrega")],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "fonte AnKing diverge" in (proc.stdout + proc.stderr)
