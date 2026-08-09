#!/usr/bin/env python3
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class PipelineConfigurationTests(unittest.TestCase):
    def test_only_e1_and_deck_are_enabled(self):
        config = json.loads((ROOT / "config/pipeline.json").read_text(encoding="utf-8"))
        self.assertTrue(config["generate_e1"])
        self.assertTrue(config["generate_resumindo"])
        for output in ("generate_e2", "generate_e3", "generate_remnote"):
            self.assertFalse(config[output])
        self.assertTrue(config["require_offline_apkg"])
        self.assertEqual(config["new_cards_per_day"], 25)

    def test_resumo_is_the_active_entrypoint(self):
        command = (ROOT / ".claude/commands/resumo.md").read_text(encoding="utf-8")
        self.assertIn("PIPELINE-E1-DECK.md", command)
        self.assertIn("audit_apkg.py", command)
        self.assertIn("sessão principal", command.casefold())


if __name__ == "__main__":
    unittest.main()
