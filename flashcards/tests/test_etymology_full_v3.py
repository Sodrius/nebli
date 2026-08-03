import json
import re
import unittest
from collections import Counter
from pathlib import Path


ETIM = Path(__file__).resolve().parents[1] / "etimologia"


class FullDeckV3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads((ETIM / "cards" / "cards_approved_v3.json").read_text(encoding="utf-8"))
        cls.cards = cls.payload["cards"]

    def test_size_and_unique_concepts(self):
        self.assertEqual(len(self.cards), 765)
        canon = [c["canonical_form"].casefold() for c in self.cards]
        self.assertEqual([x for x, n in Counter(canon).items() if n > 1], [])

    def test_no_four_clozes(self):
        for card in self.cards:
            clozes = re.findall(r"\{\{c(\d+)::(.*?)\}\}", card["text"])
            self.assertGreaterEqual(len(clozes), 1)
            self.assertLessEqual(len(clozes), 3)
            self.assertEqual({n for n, _ in clozes}, {"1"})

    def test_extra_policy(self):
        lengths = []
        for card in self.cards:
            words = re.findall(r"\b[\wÀ-ÿ/-]+\b", card["extra"])
            lengths.append(len(words))
            self.assertLessEqual(len(words), 40)
        self.assertGreaterEqual(sum(n <= 25 for n in lengths) / len(lengths), 0.85)

    def test_unknown_terms_have_didactic_extra(self):
        tagged = [c for c in self.cards if "terminologia::didatica::termo_novo" in c["tags"]]
        self.assertGreaterEqual(len(tagged), 90)
        for card in tagged:
            self.assertGreaterEqual(len(card["extra"].split()), 7)

    def test_transfer_extras_decompose_and_interpret(self):
        for card in self.cards:
            if card["kind"] == "transfer":
                self.assertIn("+", card["extra"])
                self.assertIn("=", card["extra"])

    def test_small_greek_latin_sample(self):
        pairs = [c for c in self.cards if "forma <b>{{c1::grega}}</b>" in c["text"]]
        self.assertGreaterEqual(len(pairs), 6)
        self.assertLessEqual(len(pairs), 12)

    def test_latin_anatomical_nomenclature_module(self):
        latin = [c for c in self.cards if "terminologia::disciplina::latim_anatomico" in c["tags"]]
        self.assertEqual(len(latin), 27)
        self.assertTrue(all("terminologia::origem::latim" in c["tags"] for c in latin))

    def test_holdout_is_real_and_unseen(self):
        holdout = json.loads((ETIM / "data" / "inference_holdout_v3.json").read_text(encoding="utf-8"))
        self.assertEqual(len(holdout), 300)
        self.assertTrue(all(not row["seen_in_cards"] for row in holdout))

    def test_pilot_cards_are_rehomed(self):
        self.assertFalse(any(c["deck"].endswith("Piloto pt2") for c in self.cards))


if __name__ == "__main__":
    unittest.main()
