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
from index_private_apkg import build_index
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
                          "card_refs": ["guid-1"], "source_guid": "guid-1",
                          "candidate_search": {"anking_count": 2, "external_count": 0,
                                               "queries": ["nucleus"], "rejection_rationale": ""}},
                "tags": ["nucleo"],
            }],
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


class ApkgTests(unittest.TestCase):
    def fixture(self, root: Path) -> Path:
        collection = root / "collection.anki2"
        db = sqlite3.connect(collection)
        db.executescript("""
          CREATE TABLE col (models TEXT, decks TEXT);
          CREATE TABLE notes (id INTEGER, guid TEXT, mid INTEGER, tags TEXT, flds TEXT);
          CREATE TABLE cards (id INTEGER, nid INTEGER, did INTEGER, ord INTEGER, queue INTEGER, type INTEGER);
        """)
        models = {"10": {"name": "Basic", "flds": [{"name": "Front"}, {"name": "Back"}]}}
        decks = {"20": {"name": "NEBLI::Teste"}}
        db.execute("INSERT INTO col VALUES (?, ?)", (json.dumps(models), json.dumps(decks)))
        db.execute("INSERT INTO notes VALUES (?, ?, ?, ?, ?)",
                   (1, "source-guid", 10, " nucleo ", "Front <img src=\"image.png\">\x1fBack"))
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


if __name__ == "__main__":
    unittest.main()
