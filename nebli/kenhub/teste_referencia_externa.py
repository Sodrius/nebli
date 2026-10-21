import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from nebli.kenhub import referencia_externa as ref
from nebli.kenhub import mascara
from nebli.kenhub import lote_referencia as lote


class ReferenciaExternaTests(unittest.TestCase):
    def setUp(self):
        self.cfg = json.loads(ref.CONFIG.read_text())

    def test_decisoes_aprovadas_passam(self):
        self.assertEqual(ref.config_gates(self.cfg), [])

    def test_cada_decisao_errada_reprova(self):
        cases = [
            ("deck_root", "Referências::Kenhub"),
            ("scope", ["anatomia"]),
            ("exclude", []),
            ("initial_suspension", False),
            ("content_phase_1", "quiz_textual"),
            ("visual_themes", ["ambar", "ciano"]),
            ("private_only", False),
            ("background_only_after_authentication", False),
            ("anki_write_policy", {}),
        ]
        for key, value in cases:
            bad = copy.deepcopy(self.cfg); bad[key] = value
            self.assertTrue(ref.config_gates(bad), key)

    def test_pilot_is_blocked_without_approval(self):
        with tempfile.TemporaryDirectory() as d, patch.object(ref, "PRIVATE", Path(d)), \
                patch.object(ref, "MANIFEST", Path(d) / "manifesto.json"), patch.object(ref, "STATE", Path(d) / "estado.jsonl"):
            ref.preparar()
            with self.assertRaises(SystemExit) as ctx:
                ref.piloto(["--dry-run"])
            self.assertIn("BLOQUEADO", str(ctx.exception))

    def test_both_visual_themes_exist_and_are_distinct(self):
        self.assertEqual(set(mascara.TEMAS_REFERENCIA), {"ambar", "ciano"})
        self.assertNotEqual(mascara.TEMAS_REFERENCIA["ambar"]["seta"], mascara.TEMAS_REFERENCIA["ciano"]["seta"])
        self.assertEqual(self.cfg["visual_themes"], ["ciano"])
        self.assertEqual(self.cfg["production"]["selected_theme"], "ciano")

    def test_batch_checkpoint_rejects_incomplete_and_wrong_size(self):
        unit={"slug":"u","targets":10,"built":9,"written":0,"exceptions":[],"state":"BUILT","module_order":1,"section_order":1,"unit_order":1}
        self.assertTrue(ref.checkpoint_gate({"units":[unit]}))
        good={**unit,"built":10,"state":"VERIFIED"}
        self.assertEqual(ref.checkpoint_gate({"units":[good]},final=True),[])
        self.assertTrue(ref.checkpoint_gate({"units":[good]}))
        self.assertEqual(ref.checkpoint_gate({"units":[good] * 50}), [])
        reused={**good,"built":8,"reused":2}
        self.assertEqual(ref.checkpoint_gate({"units":[reused]},final=True),[])
        written={**good,"built":9,"written":1,"exceptions":[{"reason":"sem_figura","written_id":"khref-text:u:x"}]}
        self.assertEqual(ref.checkpoint_gate({"units":[written]},final=True),[])
        missing={**good,"built":9,"written":0,"exceptions":[{"reason":"sem_figura"}]}
        self.assertTrue(ref.checkpoint_gate({"units":[missing]},final=True))

    def test_anki_write_is_one_prepared_batch(self):
        good={"prepared_outside_anki":True,"write_sessions":1,"readbacks":1,
              "per_card_calls":0,"sync":False}
        self.assertEqual(ref.anki_write_plan_gate(good), [])
        for key, value in (("prepared_outside_anki",False),("write_sessions",2),
                           ("readbacks",2),("per_card_calls",1),("sync",True)):
            bad={**good,key:value}
            self.assertTrue(ref.anki_write_plan_gate(bad), key)

    def test_written_aliases_in_same_batch_receive_every_unit_tag(self):
        stable = "khref-text:u1:arteria-x"
        aliases = lote._aliases_by_canonical([
            {"unit": "u2", "structure": "arteria-x", "canonical": stable},
            {"unit": "u3", "structure": "arteria-x", "canonical": stable},
            {"unit": "u2", "structure": "arteria-x", "canonical": stable},
        ])
        self.assertEqual(lote._unit_tags("u1", stable, aliases), [
            lote.UNIT_TAG_PREFIX + "u1",
            lote.UNIT_TAG_PREFIX + "u2",
            lote.UNIT_TAG_PREFIX + "u3",
        ])

    def test_every_unit_reconciles_targets_built_written_and_reused(self):
        good = {"slug":"u", "targets":10, "built":6, "written":1, "reused":3,
                "exceptions":[], "state":"VERIFIED", "module_order":1,
                "section_order":1, "unit_order":1}
        self.assertEqual(ref.checkpoint_gate({"units":[good]}, final=True), [])
        for field in ("built", "written", "reused"):
            bad = {**good, field: good[field] - 1}
            self.assertTrue(any("G41" in p for p in ref.checkpoint_gate({"units":[bad]}, final=True)), field)

    def test_written_fallback_is_relational_not_enumerative_and_hides_source(self):
        good = [{"stable_id":"x", "text":"A {{c1::artéria X}} passa posteriormente ao músculo Y.",
                 "extra":"Essa relação ajuda a reconhecer o vaso no corte axial."}]
        self.assertEqual(lote.written_fallback_gate(good), [])
        bad = [
            {"stable_id":"list", "text":"Estruturas: {{c1::A, B e C}}", "extra":""},
            {"stable_id":"source", "text":"A {{c1::artéria X}} passa atrás do músculo Y.",
             "extra":"Kenhub"},
            {"stable_id":"bare", "text":"{{c1::Artéria X}}", "extra":""},
        ]
        problems = lote.written_fallback_gate(bad)
        self.assertTrue(any("list" in p and "enumerativo" in p for p in problems))
        self.assertTrue(any("source" in p and "exibe Kenhub" in p for p in problems))
        self.assertTrue(any("bare" in p and "contexto relacional" in p for p in problems))

    def test_global_audit_compares_official_catalog_with_live_unit_tags(self):
        catalog = {"units":[{"slug":"u1"},{"slug":"u2"},{"slug":"u3"}]}
        live = [
            {"tags":[lote.UNIT_TAG_PREFIX + "u1", lote.UNIT_TAG_PREFIX + "u2"]},
            {"tags":[lote.UNIT_TAG_PREFIX + "u3"]},
        ]
        self.assertEqual(lote.global_catalog_live_gate(catalog, live, expected_units=3), [])
        bad_live = live + [{"tags":[lote.UNIT_TAG_PREFIX + "orfa"]}]
        problems = lote.global_catalog_live_gate(catalog, bad_live, expected_units=4)
        self.assertTrue(any("esperado 4" in p for p in problems))
        self.assertTrue(any("fora do catálogo" in p for p in problems))
        missing = lote.global_catalog_live_gate(catalog, live[:1], expected_units=3)
        self.assertTrue(any("sem tag viva" in p for p in missing))

    def test_reuse_must_point_directly_to_existing_canonical(self):
        valid = {"khref-text:origin:x"}
        good = [{"unit":"u2", "structure":"x", "canonical":"khref-text:origin:x"}]
        self.assertEqual(lote.reuse_canonical_gate(good, valid), [])
        orphan = [{"unit":"u2", "structure":"x", "canonical":"khref-text:missing:x"}]
        self.assertTrue(any("inexistente" in p for p in lote.reuse_canonical_gate(orphan, valid)))


if __name__ == "__main__":
    unittest.main()
