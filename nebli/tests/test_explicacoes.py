import hashlib
import json
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from nebli import explicacoes


def card(text, ord_, extra=""):
    return {"cardId": 1, "note": 9, "ord": ord_, "deckName": "NEBLI::UC03::Aula (12)",
            "question": "", "answer": "",
            "fields": {"Text": {"value": text, "order": 0}, "Extra": {"value": extra, "order": 1}}}


class ExplicacoesTests(unittest.TestCase):
    TEXT = "{{c1::Tetracyclines}} bind the {{c2::30S}} subunit, blocking {{c3::aminoacyl-tRNA::what?}}"
    TAB_TEXT = ("O complemento é um conjunto de proteínas de defesa do plasma que, ativadas, marcam e destroem micróbios.\n\n"
                "C3b se liga ao micróbio e facilita sua ingestão por fagócitos, que têm receptores para ele.\n\n"
                "A opsonização liga a cascata do complemento à eliminação do micróbio; C3a, ao contrário, promove inflamação.")

    def test_coverage_rejects_pending_empty_stale_and_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = explicacoes.open_store(Path(tmp) / "cache.sqlite")
            current = card("{{c1::C3b}} opsonizes microbes", 0)
            version = explicacoes.style_version(explicacoes.STYLE.read_text())
            digest = explicacoes.card_hash([current["fields"]["Text"]["value"], ""], 0)
            with patch.object(explicacoes, "collect", return_value=[current]):
                self.assertEqual(explicacoes.cobertura("test", db=db)["faltando"], 1)
                db.execute("insert into explicacoes(card_id,hash,estilo,status,texto) values (?,?,?,?,?)",
                           (1, digest, version, "revisar", ""))
                self.assertEqual(explicacoes.summary(db=db, query="test"), 1)
                db.execute("update explicacoes set status='ok'")
                self.assertEqual(explicacoes.cobertura("test", db=db)["faltando"], 1)
                db.execute("update explicacoes set texto=?", (self.TAB_TEXT,))
                self.assertEqual(explicacoes.summary(db=db, query="test"), 0)
                db.execute("update explicacoes set texto='Básico: O complemento é defesa.'")
                self.assertEqual(explicacoes.cobertura("test", db=db)["formato_incompleto"], 1)
                db.execute("update explicacoes set texto=?", (self.TAB_TEXT,))
                db.execute("update explicacoes set estilo='old'")
                self.assertEqual(explicacoes.cobertura("test", db=db)["desatualizada"], 1)
            with patch.object(explicacoes, "collect", return_value=[]):
                self.assertEqual(explicacoes.summary(db=db, query="test"), 1)
            db.close()

    def test_each_sibling_hides_only_its_own_cloze(self):
        front, back = explicacoes.card_text(card(self.TEXT, 1))
        self.assertEqual(front, "Tetracyclines bind the [...] subunit, blocking aminoacyl-tRNA")
        self.assertEqual(back, "Tetracyclines bind the 30S subunit, blocking aminoacyl-tRNA")
        self.assertEqual(explicacoes.hidden_target(card(self.TEXT, 1)["fields"], 1), "30S")
        self.assertEqual(explicacoes.hidden_target(card(self.TEXT, 2)["fields"], 2), "aminoacyl-tRNA")

    def test_rendered_fallback_drops_anking_noise(self):
        c = {"fields": {"Header": {"value": "", "order": 0}}, "ord": 0,
             "question": "Q<br>#AK_Step1_v12::x", "answer": "Q<br>A<br>PSEUDO-FIELD #First Aid<br>421090<br>A"}
        self.assertEqual(explicacoes.card_text(c), ("Q", "Q\nA"))

    def test_hash_matches_the_addon_formula(self):
        fields = ["a", "b<br>c"]
        addon = hashlib.sha1(("\x1f".join(fields) + "\x1e2").encode("utf-8")).hexdigest()
        self.assertEqual(explicacoes.card_hash(fields, 2), addon)

    def test_resume_regenerates_changed_content_and_style(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = explicacoes.open_store(Path(tmp) / "cache.sqlite")
            current = card("{{c1::C3b}} opsonizes microbes", 0)
            answer = ({"1": {"status": "ok", "texto": self.TAB_TEXT}}, 0)
            with patch.object(explicacoes, "collect", return_value=[current]), \
                    patch.object(explicacoes, "studied_related", return_value=[]), \
                    patch.object(explicacoes, "claude", return_value=answer) as generate:
                explicacoes.generate(None, "test", db=db)
                explicacoes.generate(None, "test", db=db)
                self.assertEqual(generate.call_count, 1)
                current["fields"]["Extra"]["value"] = "Edited mechanism"
                explicacoes.generate(None, "test", db=db)
                self.assertEqual(generate.call_count, 2)
                db.execute("update explicacoes set estilo='old'")
                explicacoes.generate(None, "test", db=db)
                self.assertEqual(generate.call_count, 3)
            db.close()

    def test_connections_search_requires_actual_reviews(self):
        queries = []
        def call(action, **kwargs):
            queries.append(kwargs["query"])
            return []
        self.assertEqual(explicacoes.studied_related(call, card("", 0), "complement"), [])
        self.assertIn("prop:reps>0", queries[0])

    def test_paid_api_key_prevents_launch(self):
        with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "test"}), \
                patch.object(explicacoes.subprocess, "run") as launch:
            with self.assertRaises(RuntimeError):
                explicacoes.claude("rules", [])
            launch.assert_not_called()

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test"}), \
                patch.object(explicacoes.subprocess, "run") as launch:
            with self.assertRaises(RuntimeError):
                explicacoes.codex_cli("rules", [])
            launch.assert_not_called()

    def test_codex_backend_records_its_origin(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = explicacoes.open_store(Path(tmp) / "cache.sqlite")
            with patch.object(explicacoes, "collect", return_value=[card("{{c1::C3b}} opsonizes microbes", 0)]), \
                    patch.object(explicacoes, "studied_related", return_value=[]), \
                    patch.object(explicacoes, "codex_cli", return_value=({"1": {"status": "ok", "texto": self.TAB_TEXT}}, 0)):
                explicacoes.generate(None, "test", db=db, backend="codex")
            self.assertEqual(db.execute("select modelo from explicacoes where card_id=1").fetchone()[0], "codex-cli")
            db.close()

    def test_auto_falls_back_to_codex(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = explicacoes.open_store(Path(tmp) / "cache.sqlite")
            current = card("{{c1::C3b}} opsonizes microbes", 0)
            answer = {"1": {"status": "ok", "texto": self.TAB_TEXT}}
            with patch.object(explicacoes, "collect", return_value=[current]), \
                    patch.object(explicacoes, "studied_related", return_value=[]), \
                    patch.object(explicacoes, "claude", side_effect=RuntimeError("quota")), \
                    patch.object(explicacoes, "codex_cli", return_value=(answer, 0)):
                explicacoes.generate(None, "test", db=db)
            self.assertEqual(db.execute("select modelo from explicacoes where card_id=1").fetchone()[0], "codex-cli")
            db.close()

    def test_tab_is_running_prose_from_principle(self):
        self.assertIsNone(explicacoes.problema_estilo(self.TAB_TEXT))
        self.assertIn("rótulos", explicacoes.problema_estilo(
            "Básico: Base.\n\nExplicação: Causa.\n\nNa aula: Contexto.\n\nNão confundir: Contraste."))
        self.assertIn("um parágrafo", explicacoes.problema_estilo("O complemento opsoniza micróbios."))
        self.assertIn("lista", explicacoes.problema_estilo(self.TAB_TEXT + "\n\n- item solto"))

    def test_bad_tab_stays_pending_until_explanation_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = explicacoes.open_store(Path(tmp) / "cache.sqlite")
            db.execute("insert into explicacoes(card_id,status,texto) values (?,?,?)",
                       (1, "ok", self.TAB_TEXT))
            event = {"em": "2026-10-12 10:00:00", "evento": "tab_ruim", "card": 1,
                     "nota": 9, "explicacao": hashlib.sha256(self.TAB_TEXT.encode()).hexdigest()[:16]}
            log = Path(tmp) / "tab-log.jsonl"
            log.write_text(json.dumps(event) + "\n")
            self.assertEqual(len(explicacoes.bad_tabs(log, db)), 1)
            db.execute("update explicacoes set texto=? where card_id=1",
                       (self.TAB_TEXT + "\nUma revisão útil.",))
            self.assertEqual(explicacoes.bad_tabs(log, db), [])
            db.close()

    def test_liked_cards_toggle(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "tab-log.jsonl"
            events = [
                {"em": "2026-10-16 10:00:00", "evento": "card_gostei", "card": 1, "nota": 10},
                {"em": "2026-10-16 10:01:00", "evento": "card_gostei", "card": 2, "nota": 20},
                {"em": "2026-10-16 10:02:00", "evento": "card_gostei_desfeito", "card": 1, "nota": 10},
            ]
            log.write_text("\n".join(json.dumps(event) for event in events), encoding="utf-8")
            liked = explicacoes.liked_cards(log)
            self.assertEqual([event["card"] for event in liked], [2])


if __name__ == "__main__":
    unittest.main()
