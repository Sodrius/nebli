import json
from pathlib import Path

CFG = Path(__file__).parents[2] / "config" / "pipeline.json"


def test_v13_is_apkg_and_learning_delta_is_authority():
    c = json.loads(CFG.read_text(encoding="utf-8"))
    assert c["pipeline_version"] == "e1-deck-v13"
    assert c["card_source_mode"] == "authored_only"
    assert c["anki_backend"] == "apkg"
    assert c["require_offline_apkg"] is True
    assert c["require_apkg_audit"] is True
    assert c["user_delivery"]["visible_files"] == ["e1_pdf", "apkg"]
    assert c["learning_delta"]["inputs"] == ["lesson_materials", "e1", "master_sheet"]
    assert c["learning_delta"]["forbid_prior_deck_lookup"] is True
    assert set(c["learning_delta"]["eligible_roles"]) == {"foco_novo", "relacao_nova", "aprofundamento_novo"}
    assert set(c["learning_delta"]["non_card_roles"]) == {"pre_requisito", "revisao", "contexto", "exemplo", "mencao"}
    assert c["source_priority"] == ["authored", "io"]
    assert c["image_occlusion"]["multi_label_mode"] == "hide_two_guess_two"
    assert c["authored_cards"]["language"] == "pt-BR"
    assert c["feedback"]["regressions_required_in_ci"] is True
