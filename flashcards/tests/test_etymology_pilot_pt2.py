import importlib.util
import re
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_etymology_pilot_pt2.py"
SPEC = importlib.util.spec_from_file_location("build_etymology_pilot_pt2", SCRIPT)
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(mod)


class PilotPt2QualityTests(unittest.TestCase):
    def test_full_validator(self):
        errors, stats = mod.validate()
        self.assertEqual(errors, [])
        self.assertEqual(stats["notes"], 82)

    def test_contrasts_recover_together(self):
        for card in mod.cards:
            nums = re.findall(r"\{\{c(\d+)::", card["text"])
            self.assertTrue(nums)
            self.assertEqual(set(nums), {"1"})
            if card["kind"] == "contrast":
                self.assertGreaterEqual(len(nums), 2)
                self.assertEqual(card["number_of_cards"], 1)

    def test_transfer_extra_decomposes_and_interprets(self):
        for card in mod.cards:
            if card["kind"] == "transfer":
                self.assertIn("+", card["extra"])
                self.assertIn("=", card["extra"])

    def test_human_review_file_is_not_generator_output(self):
        old_generator = SCRIPT.with_name("build_etymology_v2.py").read_text(encoding="utf-8")
        self.assertNotIn('(REPORTS / "pilot_cards.md").write_text', old_generator)
        annotated = mod.ETIM / "reports" / "pilot_cards.md"
        self.assertTrue(annotated.exists())
        self.assertIn("comentário", annotated.read_text(encoding="utf-8").casefold())


if __name__ == "__main__":
    unittest.main()
