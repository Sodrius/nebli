import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_active_entrypoints_preserve_e1_first_contract():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    execution = (ROOT / "docs/canon/EXECUCAO.md").read_text(encoding="utf-8")

    for text in (agents, claude, execution):
        lowered = text.casefold()
        assert "source_to_e1_matrix" in text
        assert "antes" in lowered
        assert "e1" in lowered

    assert "pelo menos dois exemplares UC02" in agents
    assert "Nenhum card é autorado antes desse congelamento" in claude
    assert "quatro passadas" in execution
    assert "O fato de algo não merecer card nunca é razão para excluí-lo da E1" in execution


def test_v13_config_keeps_full_e1_release_gate():
    data = json.loads((ROOT / "config/pipeline.json").read_text(encoding="utf-8"))
    gate = data["e1_release_gate"]
    assert gate["required"] is True
    assert gate["require_source_to_e1_matrix_before_drafting"] is True
    assert gate["require_calibration_before_drafting"] is True
    assert gate["minimum_uc02_calibration_exemplars"] >= 2
    assert gate["require_four_pass_review"] is True
    assert gate["require_all_pages_rendered_and_visually_reviewed"] is True
    assert gate["block_unresolved_core_omissions"] is True
    assert gate["block_unresolved_beginner_gaps"] is True
    assert data["learning_delta"]["e1_must_be_frozen_first"] is True
