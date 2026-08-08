#!/usr/bin/env python3
"""Regression tests for the selective deck-aula policy."""
from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from validate_lesson_coverage import validate, verify_apkg
from buscar_tags_lote import ler_checklist


HERE = Path(__file__).resolve().parent
GATE = HERE / "gate_deck_aula_completo.py"


class DeckAulaPolicyTests(unittest.TestCase):
    def test_checklist_requires_card_worthiness_before_search(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "check.tsv"
            path.write_text("1.1\tATP synthase\tATP synthase\tREVIEW\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                ler_checklist(path)
            path.write_text(
                "1.1\tATP synthase\tATP synthase\tnuclear\n"
                "1.2\tdetalhe\tdetail\tno_card\n",
                encoding="utf-8",
            )
            self.assertEqual(ler_checklist(path), [("1.1", "ATP synthase", "ATP synthase")])

    def _base(self, root: Path) -> dict:
        (root / "e1.typ").write_text(
            "ATP synthase uses the proton gradient.\n"
            "Cristae increase inner-membrane surface.\n"
            "The membrane also contains many transporters.\n",
            encoding="utf-8",
        )
        pool = root / "pool.json"
        pool.write_text("[]\n", encoding="utf-8")
        return {
            "lesson_pipeline": "deck-aula-v1",
            "deck_aula_gate": "v2",
            "deck": "NEBLI::UC::P1::Bioq::Aula",
            "e1": {"path": "e1.typ"},
            "e1_inventory": [
                {"id": "N1", "e1_anchor": "ATP synthase uses the proton gradient.",
                 "card_decision": "nuclear"},
                {"id": "S1", "e1_anchor": "Cristae increase inner-membrane surface.",
                 "card_decision": "supporting"},
                {"id": "X1", "e1_anchor": "The membrane also contains many transporters.",
                 "card_decision": "no_card", "decision_reason": "baixo valor isolado"},
            ],
            "facts": [{
                "id": "N1", "e1_anchor": "ATP synthase uses the proton gradient.",
                "importance": "nuclear",
                "route": {"source": "own", "card_refs": ["proton gradient"],
                          "retrieval_target": "proton gradient drives ATP synthase",
                          "coverage_quality": 2, "coverage_rationale": "recupera mecanismo central",
                          "prior_search": {"anking": "insufficient", "other_decks": "insufficient"}},
            }],
            "source_audit": {
                "pool_path": str(pool),
                "candidates_by_fact": {"N1": {"searched_tags": ["mitochondria"],
                                                "candidate_count": 2,
                                                "rejection_rationale": "candidatos cobrem patologias vizinhas"}},
            },
            "e1_enrichments": [],
            "load_profile": {"lecture_size": "small", "estimated_cards": 18},
        }

    def _gate(self, spec: dict, root: Path) -> subprocess.CompletedProcess[str]:
        manifest = root / "manifest.json"
        manifest.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
        return subprocess.run([sys.executable, str(GATE), str(manifest)],
                              text=True, capture_output=True, check=False)

    def test_supporting_may_be_skipped_and_no_card_stays_out(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            spec = self._base(root)
            result = validate(spec, root)
            self.assertTrue(result["passed"], result)
            self.assertEqual(result["supporting_skipped"], 1)
            self.assertEqual(result["no_card"], 1)

    def test_authorial_can_pass_without_global_source_quota(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            proc = self._gate(self._base(root), root)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_no_card_route_and_unreviewed_large_deck_are_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            spec = self._base(root)
            x = {
                "id": "X1", "e1_anchor": "The membrane also contains many transporters.",
                "importance": "supporting",
                "route": {"source": "anking", "card_refs": ["transporters"],
                          "retrieval_target": "membrane transporters", "coverage_quality": 1,
                          "coverage_rationale": "nomeia detalhe"},
            }
            spec["facts"].append(x)
            spec["source_audit"]["candidates_by_fact"]["X1"] = {
                "searched_tags": ["mitochondria"], "candidate_count": 1
            }
            spec["load_profile"]["estimated_cards"] = 75
            proc = self._gate(spec, root)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("no_card", proc.stdout)
            self.assertIn(">60", proc.stdout)

    def test_duplicate_retrieval_target_is_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            spec = self._base(root)
            spec["e1_inventory"][1]["card_decision"] = "nuclear"
            spec["facts"].append({
                "id": "S1", "e1_anchor": "Cristae increase inner-membrane surface.",
                "importance": "nuclear",
                "route": {"source": "anking", "card_refs": ["cristae"],
                          "retrieval_target": "proton gradient drives ATP synthase",
                          "coverage_quality": 2, "coverage_rationale": "teste"},
            })
            spec["source_audit"]["candidates_by_fact"]["S1"] = {
                "searched_tags": ["mitochondria"], "candidate_count": 1
            }
            proc = self._gate(spec, root)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("retrieval_target duplica", proc.stdout)

    def test_offline_apkg_verification_checks_refs_and_count(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            spec = self._base(root)
            spec["load_profile"]["estimated_cards"] = 1
            db = root / "collection.anki2"
            con = sqlite3.connect(db)
            con.execute("create table notes (flds text)")
            con.execute("create table cards (id integer)")
            con.execute("insert into notes values (?)", ("ATP synthase uses the proton gradient.\x1fExtra",))
            con.execute("insert into cards values (1)")
            con.commit()
            con.close()
            apkg = root / "deck.apkg"
            with zipfile.ZipFile(apkg, "w") as zf:
                zf.write(db, "collection.anki2")
            errors, count = verify_apkg(spec, apkg)
            self.assertEqual(errors, [])
            self.assertEqual(count, 1)

    def test_offline_apkg_rejects_unmanifested_note(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            spec = self._base(root)
            spec["load_profile"]["estimated_cards"] = 2
            db = root / "collection.anki2"
            con = sqlite3.connect(db)
            con.execute("create table notes (flds text)")
            con.execute("create table cards (id integer)")
            con.execute("insert into notes values (?)", ("ATP synthase uses the proton gradient.\x1fExtra",))
            con.execute("insert into notes values (?)", ("Unapproved side fact.\x1fExtra",))
            con.executemany("insert into cards values (?)", [(1,), (2,)])
            con.commit()
            con.close()
            apkg = root / "deck.apkg"
            with zipfile.ZipFile(apkg, "w") as zf:
                zf.write(db, "collection.anki2")
            errors, count = verify_apkg(spec, apkg)
            self.assertEqual(count, 2)
            self.assertTrue(any("não consta no manifesto" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
