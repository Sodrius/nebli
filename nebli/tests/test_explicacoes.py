import hashlib
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
            answer = ({"1": {"status": "ok", "texto": "Base: Complemento."}}, 0)
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


if __name__ == "__main__":
    unittest.main()
