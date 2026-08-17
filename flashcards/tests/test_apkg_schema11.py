from pathlib import Path
import sys

from conftest import lesson

SCRIPTS = Path(__file__).parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from apkg_schema11 import normalize_apkg, validate_apkg_schema11
from exportar_apkg_canonico import export_apkg


def test_schema11_normalizer_fixes_decks_metadata_rejected_by_anki(tmp_path):
    deck_path, data = lesson(tmp_path)
    apkg = tmp_path / "raw.apkg"
    export_apkg(data, deck_path, apkg)

    # Regressão do erro visto no AnkiDroid:
    # 500: JsonError { info: "decoding decks: JsonError" }
    before = validate_apkg_schema11(apkg)
    assert before["passed"] is False
    assert any("newToday" in error or "lrnToday" in error for error in before["errors"])

    fixed = normalize_apkg(apkg)
    assert fixed["passed"], fixed["errors"]
    assert fixed["changed"] is True

    after = validate_apkg_schema11(apkg)
    assert after["passed"], after["errors"]


def test_normalizer_is_idempotent(tmp_path):
    deck_path, data = lesson(tmp_path)
    apkg = tmp_path / "twice.apkg"
    export_apkg(data, deck_path, apkg)
    assert normalize_apkg(apkg)["passed"]
    second = normalize_apkg(apkg)
    assert second["passed"]
    assert second["changed"] is False
