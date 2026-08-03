#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path

from build_card import main as build_cards
from e1_card_loop import validate as validate_card_loop
from e1_e2_contract import validate_spec
from planejar_visual_aula import seed
from visual_lesson_plan import validate_plan


class E1E2ContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        (self.base / "e1.typ").write_text("A E1 explica o transporte por difusão.", encoding="utf-8")
        (self.base / "e2.typ").write_text("#termo-nota[difusão][movimento passivo]", encoding="utf-8")
        (self.base / "visual-plan.json").write_text("""{
          "visual_plan_version": "v1", "slug": "teste", "concepts": [{
            "concept_id": "1.1", "importance": "nuclear", "learning_goal": "Explicar difusão.",
            "strategy": "none", "image_role": "none", "visual_task": "Relação verbal.",
            "rationale": "Não há reconhecimento visual a testar."
          }]
        }""", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def spec(self):
        return {
            "pipeline_contract": "e1-e2-v1", "e1": {"path": "e1.typ"}, "e2": {"path": "e2.typ"}, "visual_plan": "visual-plan.json",
            "e2_coverage": [{"e2_item": "difusão", "concept_id": "1.1", "status": "covered", "rationale": "card recupera o conceito"}],
            "cards": [{
                "nebli_id": "fisio-dif-01", "concept_id": "1.1", "visual_plan_id": "1.1", "visual_plan_link": "primary", "e1_anchor": {"quote": "transporte por difusão"},
                "generation": {"mode": "authorial", "source_refs": ["E1"], "external_probe": {"queries": ["diffusion physiology"], "decision": "redação independente"}},
                "semantic_review": {"atomicity": "pass", "induction": "pass", "medical": "pass", "reviewer": "test"},
                "visual": {"visual_need": "none", "image_role": "none", "image_status": "missing", "card_mode": "explanatory_image", "placement": "extra", "visual_task": "não há relação visual recuperável"}
            }]
        }

    def test_accepts_complete_contract(self):
        self.assertTrue(validate_spec(self.spec(), self.base)["passed"])

    def test_rejects_anchor_absent_from_e1(self):
        spec = self.spec()
        spec["cards"][0]["e1_anchor"]["quote"] = "fato inexistente"
        self.assertFalse(validate_spec(spec, self.base)["passed"])

    def test_rejects_e2_without_destination(self):
        spec = self.spec()
        spec["e2_coverage"] = []
        result = validate_spec(spec, self.base)
        self.assertTrue(any("alvo E2 sem destino" in e for e in result["errors"]))

    def test_canonical_builder_runs_only_after_contract_gate(self):
        import json
        spec = self.spec()
        spec.update({"deck": "NEBLI::Teste", "slug": "fisio-teste", "theme_label": "Fisiologia"})
        spec["cards"][0]["text"] = "The process is <b>{{c1::diffusion}}</b>."
        path = self.base / "cards.json"
        path.write_text(json.dumps(spec), encoding="utf-8")
        build_cards(str(path), dry=True, canonical=True)

    def test_card_to_e1_loop_requires_real_anchor_and_emits_patch_candidate(self):
        queue = {
            "slug": "teste", "e1_file": str(self.base / "e1.typ"),
            "candidates": [
                {"concept_id": "1.1", "decision": "anchored", "rationale": "já ensinado",
                 "e1_anchor": {"quote": "transporte por difusão"}},
                {"concept_id": "1.2", "decision": "anchorable", "rationale": "aprofundamento",
                 "e1_patch": {"insert_after": "transporte", "text": "Novo detalhe.", "source_refs": ["fonte"]}}
            ]
        }
        errors, patches = validate_card_loop(queue)
        self.assertEqual(errors, [])
        self.assertEqual(len(patches), 1)

    def test_visual_plan_rejects_io_without_target(self):
        errors, _ = validate_plan({"visual_plan_version": "v1", "concepts": [{
            "concept_id": "1.1", "importance": "nuclear", "learning_goal": "Reconhecer uma estrutura.",
            "strategy": "io_required", "image_role": "recognition", "visual_task": "Identificar.",
            "rationale": "É visual.", "io": {"board_id": "x", "targets": []}
        }]})
        self.assertTrue(any("IO exige 1–4" in error for error in errors))

    def test_visual_plan_seed_separates_structure_and_mechanism(self):
        self.assertEqual(seed("1.1", "Nervo facial no corte")["strategy"], "io_required")
        self.assertEqual(seed("1.2", "Mecanismo do transporte ativo")["strategy"], "extra_recommended")


if __name__ == "__main__":
    unittest.main()
