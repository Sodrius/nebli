import copy, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from validar_ganho_aula import validate_learning_delta
from conftest import lesson


def test_e1_and_master_sheet_select_learning_gain_not_prerequisite(tmp_path):
    _, data = lesson(tmp_path)
    assert validate_learning_delta(data)["passed"]
    prior = {"concept_id":"prior-pressure","importance":"supporting","learning_role":"pre_requisito","curriculum_ref":"aula-pressao","teaching_evidence":[{"source":"master_sheet","locator":"Aula anterior — Pressão e gradientes","rationale":"A planilha mostra que pressão já foi objeto de aula anterior e aqui apenas sustenta a explicação."}],"retention_class":"e1_only","exclusion_reason":"É base para compreender a válvula, não um ganho novo da aula atual.","e1_anchor":"A pressão organiza o fluxo","coverage_quality":1,"card_keys":[],"step1":{"decision":"not_applicable"}}
    data["release_gate"]["concepts"].append(prior)
    assert validate_learning_delta(data)["passed"]
    bad = copy.deepcopy(data); stolen = copy.deepcopy(bad["cards"][0]); stolen["card_key"]="review-pressure"; stolen["concept_id"]="prior-pressure"; bad["cards"].append(stolen); bad["release_gate"]["concepts"][-1]["card_keys"]=["review-pressure"]
    failed = validate_learning_delta(bad)
    assert not failed["passed"]
    assert any("learning_role=pre_requisito não pode ter card_keys" in e for e in failed["errors"])
    assert any("não representa ganho da aula" in e for e in failed["errors"])


def test_card_eligible_concept_requires_positive_teaching_evidence(tmp_path):
    _, data = lesson(tmp_path)
    data["release_gate"]["concepts"][0]["teaching_evidence"]=[{"source":"master_sheet","locator":"Aula atual","rationale":"A planilha localiza a aula, sem provar que o material ensina esta relação."}]
    failed=validate_learning_delta(data)
    assert not failed["passed"]
    assert any("evidência positiva de ensino" in e for e in failed["errors"])
