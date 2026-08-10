#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sqlite3
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_apkg import audit
from gate_deck_aula_completo import enforce_card_count
from index_private_apkg import build_index
from search_private_index import search_index
from validate_lesson_contract import validate


class LessonContractTests(unittest.TestCase):
    def valid_spec(self, root: Path) -> tuple[dict, Path]:
        e1 = root / "e1.typ"
        e1.write_text("Trecho literal nuclear da E1.", encoding="utf-8")
        index = root / "anking.private.sqlite"
        index.write_bytes(b"index")
        spec = {
            "pipeline_version": "e1-deck-v3", "slug": "aula-teste", "title": "Aula teste",
            "deck": "NEBLI::Aula teste", "optional_deck": "NEBLI::Aula teste::Optional",
            "status": "frozen",
            "card_budget": {"lesson_size": "small", "hard_max": 25,
                            "expected_total_cards": 1,
                            "rationale": "aula pequena", "manual_scope_review": "not_required",
                            "review_rationale": ""},
            "e1": {"path": "e1.typ", "sha256": hashlib.sha256(e1.read_bytes()).hexdigest()},
            "private_sources": {"anking_index": {
                "status": "ready", "path": index.name, "sha256": "source-sha"}},
            "concepts": [{
                "id": "1.1", "name_pt": "núcleo", "name_en": "nucleus", "subtopic": "célula",
                "origins": ["e1"], "importance": "nuclear",
                "e1_anchor": "Trecho literal nuclear da E1.",
                "step1": {"decision": "not_applicable", "same_theme": True,
                          "source_ref": "", "rationale": ""},
                "visual": {"need": "none", "role": "none", "mode": "none",
                           "task": "verbal", "status": "not_needed", "asset": None},
                "route": {"source": "anking", "coverage_quality": 3,
                          "coverage_rationale": "recordação e mecanismo",
                          "card_refs": ["card-1"], "source_guid": "guid-1",
                          "candidate_search": {"status": "complete", "anking_count": 2,
                                               "external_count": 0,
                                               "query_families": {
                                                   "pt": ["núcleo"], "en": ["nucleus"],
                                                   "mechanism_or_structure": ["cell nucleus"],
                                                   "synonyms": [], "tags_or_siblings": ["cell biology"]},
                                               "siblings_reviewed": True,
                                               "rejection_rationale": ""}},
                "tags": ["nucleo"],
            }],
            "cards": [{"id": "card-1", "concept_ids": ["1.1"], "source": "anking",
                       "format": "cloze", "retrieval_target": "identificar núcleo",
                       "generated_card_count": 1,
                       "atomicity": {"decision": "approved", "exception": "",
                                     "rationale": "uma recuperação"},
                       "text": "The structure is {{c1::nucleus}}.",
                       "cloze_exception_reason": ""}],
        }
        manifest = root / "contract.json"
        manifest.write_text(json.dumps(spec), encoding="utf-8")
        return spec, manifest

    def test_valid_contract_passes(self):
        with tempfile.TemporaryDirectory() as raw:
            spec, manifest = self.valid_spec(Path(raw))
            self.assertTrue(validate(spec, manifest)["passed"])

    def test_step1_cannot_leave_theme(self):
        with tempfile.TemporaryDirectory() as raw:
            spec, manifest = self.valid_spec(Path(raw))
            concept = spec["concepts"][0]
            concept["origins"].append("step1")
            concept["step1"] = {"decision": "incorporated", "same_theme": False,
                                "source_ref": "AnKing:guid", "rationale": "aprofundar"}
            result = validate(spec, manifest)
            self.assertFalse(result["passed"])
            self.assertTrue(any("same_theme" in error for error in result["errors"]))

    def test_legacy_outputs_are_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            spec, manifest = self.valid_spec(Path(raw))
            spec["outputs"] = {"e2": True}
            self.assertFalse(validate(spec, manifest)["passed"])

    def test_authored_gap_requires_real_search(self):
        with tempfile.TemporaryDirectory() as raw:
            spec, manifest = self.valid_spec(Path(raw))
            route = spec["concepts"][0]["route"]
            route.update(source="authored", source_guid="")
            route["candidate_search"]["rejection_rationale"] = ""
            result = validate(spec, manifest)
            self.assertTrue(any("rejeição documentada" in error for error in result["errors"]))

    def test_card_budget_is_a_hard_cap(self):
        with tempfile.TemporaryDirectory() as raw:
            spec, manifest = self.valid_spec(Path(raw))
            second = json.loads(json.dumps(spec["cards"][0]))
            second["id"] = "card-2"
            spec["cards"].append(second)
            spec["concepts"][0]["route"]["card_refs"].append("card-2")
            spec["card_budget"].update(hard_max=1, expected_total_cards=2)
            result = validate(spec, manifest)
            self.assertTrue(any("excede hard_max" in error for error in result["errors"]))

    def test_cloze_word_policy(self):
        with tempfile.TemporaryDirectory() as raw:
            spec, manifest = self.valid_spec(Path(raw))
            card = spec["cards"][0]
            card["text"] = "The artery is {{c1::left gastric}}."
            self.assertTrue(validate(spec, manifest)["passed"])
            card["text"] = "This is a {{c1::high pressure zone}}."
            result = validate(spec, manifest)
            self.assertTrue(any("3 palavras exige" in error for error in result["errors"]))
            card["cloze_exception_reason"] = "unidade fisiológica indivisível"
            self.assertTrue(validate(spec, manifest)["passed"])
            card["text"] = "This is a {{c1::physiologic lower high pressure zone}}."
            result = validate(spec, manifest)
            self.assertTrue(any("excede 3 palavras" in error for error in result["errors"]))

    def test_multiple_cloze_occurrences_are_not_atomic(self):
        with tempfile.TemporaryDirectory() as raw:
            spec, manifest = self.valid_spec(Path(raw))
            spec["cards"][0]["text"] = "{{c1::dura}}, {{c1::arachnoid}}, {{c1::pia}}"
            result = validate(spec, manifest)
            self.assertTrue(any("única ocorrência" in error for error in result["errors"]))

    def test_authored_card_requires_broad_search_families(self):
        with tempfile.TemporaryDirectory() as raw:
            spec, manifest = self.valid_spec(Path(raw))
            route = spec["concepts"][0]["route"]
            route.update(source="authored", source_guid="")
            spec["cards"][0]["source"] = "authored"
            search = route["candidate_search"]
            search["rejection_rationale"] = "candidatos tangenciais"
            search["query_families"] = {"en": ["nucleus"]}
            result = validate(spec, manifest)
            self.assertTrue(any("famílias PT e EN" in error for error in result["errors"]))

    def test_multi_label_io_requires_hide_all_guess_all_and_label_masks(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            spec, manifest = self.valid_spec(root)
            (root / "question.png").write_bytes(b"preview")
            (root / "answer.png").write_bytes(b"preview")
            card = spec["cards"][0]
            card.update(
                format="image_occlusion",
                atomicity={"decision": "exception", "exception": "coherent_visual_map",
                           "rationale": "partes do mesmo mapa anatômico"},
                io={
                    "behavior": "hide_all_guess_all",
                    "question_preview": "question.png",
                    "answer_preview": "answer.png",
                    "masks": [
                        {"label": "cervical", "box_px": [1, 1, 10, 5],
                         "covers": "answer_label"},
                        {"label": "thoracic", "box_px": [1, 8, 10, 5],
                         "covers": "answer_label"},
                    ],
                    "qa": {"masks_cover_answer_labels": True,
                           "visual_clues_remain_visible": True,
                           "all_answers_hidden": True,
                           "all_duplicate_labels_masked": True,
                           "question_preview_reviewed": True,
                           "answer_preview_reviewed": True},
                },
            )
            card.pop("text")
            self.assertTrue(validate(spec, manifest)["passed"])
            card["io"]["masks"][0]["covers"] = "visual_target"
            result = validate(spec, manifest)
            self.assertTrue(any("deve cobrir answer_label" in error for error in result["errors"]))
            card["io"]["masks"][0]["covers"] = "answer_label"
            card["io"]["behavior"] = "hide_one_guess_one"
            result = validate(spec, manifest)
            self.assertTrue(any("multi-rótulo exige hide_all_guess_all" in error
                                for error in result["errors"]))


class ApkgTests(unittest.TestCase):
    def fixture(self, root: Path, model_name: str = "Basic",
                front: str = "Portal triad / tríade portal <img src=\"image.png\">",
                back: str = "Back") -> Path:
        collection = root / "collection.anki2"
        db = sqlite3.connect(collection)
        db.executescript("""
          CREATE TABLE col (models TEXT, decks TEXT);
          CREATE TABLE notes (id INTEGER, guid TEXT, mid INTEGER, tags TEXT, flds TEXT);
          CREATE TABLE cards (id INTEGER, nid INTEGER, did INTEGER, ord INTEGER, queue INTEGER, type INTEGER);
        """)
        models = {"10": {"name": model_name, "flds": [{"name": "Front"}, {"name": "Back"}]}}
        decks = {"20": {"name": "NEBLI::Teste"}}
        db.execute("INSERT INTO col VALUES (?, ?)", (json.dumps(models), json.dumps(decks)))
        db.execute("INSERT INTO notes VALUES (?, ?, ?, ?, ?)",
                   (1, "source-guid", 10, " nucleo ", front + "\x1f" + back))
        db.execute("INSERT INTO cards VALUES (?, ?, ?, ?, ?, ?)", (2, 1, 20, 0, 0, 0))
        db.commit(); db.close()
        apkg = root / "fixture.apkg"
        with zipfile.ZipFile(apkg, "w") as package:
            package.write(collection, "collection.anki2")
            package.writestr("media", json.dumps({"0": "image.png"}))
            package.writestr("0", b"fake-image")
        return apkg

    def test_real_package_audit_and_private_index(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            apkg = self.fixture(root)
            result = audit(apkg)
            self.assertTrue(result["passed"], result)
            output = root / "anking.private.sqlite"
            indexed = build_index(apkg, output)
            self.assertEqual(indexed["notes"], "1")
            db = sqlite3.connect(output)
            self.assertEqual(db.execute("SELECT guid FROM notes").fetchone()[0], "source-guid")
            db.close()
            found = search_index(output, ["portal triad", "tríade portal"], limit_per_query=10)
            self.assertEqual(found["index_mode"], "fts5")
            self.assertEqual(found["union_count"], 1)
            self.assertEqual(set(found["results"][0]["matched_queries"]),
                             {"portal triad", "tríade portal"})
            db = sqlite3.connect(output)
            db.execute("DROP TABLE notes_fts")
            db.commit(); db.close()
            fallback = search_index(output, ["tríade portal"], limit_per_query=10)
            self.assertEqual(fallback["index_mode"], "legacy_like")
            self.assertEqual(fallback["union_count"], 1)

    def test_apkg_audit_rejects_non_atomic_cloze(self):
        with tempfile.TemporaryDirectory() as raw:
            apkg = self.fixture(
                Path(raw), model_name="Cloze",
                front="{{c1::dura}} and {{c1::pia}}",
            )
            result = audit(apkg)
            self.assertFalse(result["passed"])
            self.assertEqual(result["non_atomic_cloze_notes"], 1)

    def test_apkg_audit_ignores_auxiliary_fields_when_counting_clozes(self):
        with tempfile.TemporaryDirectory() as raw:
            apkg = self.fixture(
                Path(raw), model_name="Cloze", front="{{c1::nucleus}}",
                back="Explanation with literal {{c2::example}} markup",
            )
            result = audit(apkg)
            self.assertTrue(result["passed"], result)
            self.assertEqual(result["non_atomic_cloze_notes"], 0)

    def test_final_gate_compares_real_card_count_to_frozen_budget(self):
        package = {"passed": True, "cards": 2, "errors": [], "warnings": []}
        contract = {"expected_total_cards": 1, "card_hard_max": 1}
        result = enforce_card_count(package, contract)
        self.assertFalse(result["passed"])
        self.assertTrue(any("contrato congelou" in error for error in result["errors"]))
        self.assertTrue(any("excede hard_max" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
