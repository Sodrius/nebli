import hashlib
import unittest

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


if __name__ == "__main__":
    unittest.main()
