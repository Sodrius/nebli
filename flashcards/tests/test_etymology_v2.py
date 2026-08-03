import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "etimologia"


class EtymologyV2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pilot = json.loads((ROOT / "cards" / "cards_pilot_v2.json").read_text(encoding="utf-8"))["cards"]
        cls.lex = json.loads((ROOT / "data" / "lexicon_master.json").read_text(encoding="utf-8"))

    def test_exact_pilot_size(self):
        self.assertEqual(sum(x["number_of_cards"] for x in self.pilot), 120)

    def test_limits(self):
        for card in self.pilot:
            visible = re.sub(r"<[^>]+>", " ", card["text"])
            self.assertLessEqual(len(re.findall(r"\S+", visible)), 18, card["uid"])
            self.assertLessEqual(len(re.findall(r"\S+", card["extra"])), 10, card["uid"])
            self.assertLessEqual(len(re.findall(r"\{\{c\d+::", card["text"])), 3, card["uid"])

    def test_coverage_destination(self):
        for row in self.lex:
            if int(row["prioridade"] or 0) >= 13:
                self.assertTrue(row["destino_pedagogico"], row["id"])

    def test_minimal_tags_and_sources(self):
        for card in self.pilot:
            self.assertLessEqual(len(card["tags"]), 4, card["uid"])
            self.assertTrue(card["source_etymology"], card["uid"])
            self.assertTrue(card["source_medical"], card["uid"])


if __name__ == "__main__":
    unittest.main()
