import copy, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from canonical_cards import ordered_card_set_sha256
from validar_revisao_cards import validate_card_review
from conftest import lesson


def _approve(data):
    data["release_gate"]["card_review"]={
        "reviewer_stage":"independent",
        "reviewed_card_set_sha256":ordered_card_set_sha256(data["cards"]),
        "reviewed_dimensions":["learning_delta","ambiguity","anti_induction","redundancy","step1_scope","visual"],
        "blocking_findings":[],
        "summary":"Revisão independente do lote final sem bloqueios pendentes.",
    }


def test_review_is_bound_to_exact_card_set(tmp_path):
    _,data=lesson(tmp_path); _approve(data); assert validate_card_review(data)["passed"]
    changed=copy.deepcopy(data); changed["cards"][0]["extra"]="Mudou depois da revisão independente."
    result=validate_card_review(changed); assert not result["passed"]; assert any("diverge do lote atual" in e for e in result["errors"])


def test_blocking_finding_prevents_release(tmp_path):
    _,data=lesson(tmp_path); _approve(data); data["release_gate"]["card_review"]["blocking_findings"]=[{"card_key":"pressao-valvula","issue":"cobra revisão em vez de ganho"}]
    assert not validate_card_review(data)["passed"]
