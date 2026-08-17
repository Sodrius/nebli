from copy import deepcopy
from pathlib import Path
import sys

from conftest import lesson

SCRIPTS = Path(__file__).parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from validar_calibracao_e1 import validate_e1_calibration


def test_good_fixture_has_concrete_e1_calibration(tmp_path):
    _path, data = lesson(tmp_path)
    result = validate_e1_calibration(data)
    assert result["passed"], result["errors"]
    assert len(result["approved_uc02_exemplars"]) == 2


def test_boolean_uc02_flag_alone_no_longer_releases_e1(tmp_path):
    _path, data = lesson(tmp_path)
    bad = deepcopy(data)
    review = bad["release_gate"]["e1_review"]
    review.pop("calibration_exemplars")
    review.pop("calibration_canon")
    review.pop("calibration_summary")
    review.pop("review_passes")
    review.pop("matrix_frozen_before_drafting")
    assert review["uc02_exemplars_applied"] is True
    result = validate_e1_calibration(bad)
    assert not result["passed"]
    assert any("calibration_exemplars" in error for error in result["errors"])
    assert any("matrix_frozen_before_drafting" in error for error in result["errors"])


def test_one_exemplar_is_not_enough(tmp_path):
    _path, data = lesson(tmp_path)
    bad = deepcopy(data)
    bad["release_gate"]["e1_review"]["calibration_exemplars"] = [
        "typst-build/_par_histo-07-osseo/etapa1.typ"
    ]
    result = validate_e1_calibration(bad)
    assert not result["passed"]
    assert any("pelo menos dois" in error for error in result["errors"])
