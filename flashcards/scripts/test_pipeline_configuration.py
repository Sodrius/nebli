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
        self.assertFalse(config["require_offline_apkg"])
        self.assertFalse(config["require_apkg_audit"])
        self.assertEqual(config["anki_backend"], "ankidroid")
        self.assertEqual(config["ankidroid"]["manifest_schema"],
                         "nebli-ankidroid-deck-v3")
        self.assertEqual(config["new_cards_per_day"], 25)
        self.assertTrue(config["card_budget"]["enforce_contract_hard_max"])
        self.assertEqual(config["cloze_answer_words"]["preferred"], 1)
        self.assertEqual(config["cloze_answer_words"]["hard_max"], 3)
        self.assertEqual(config["image_occlusion"]["multi_label_mode"],
                         "hide_all_guess_all")

    def test_resumo_is_the_active_entrypoint(self):
        command = (ROOT / ".claude/commands/resumo.md").read_text(encoding="utf-8")
        self.assertIn("PIPELINE-E1-DECK.md", command)
        self.assertIn("validar_deck_card_a_card.py", command)
        self.assertIn("gerar_manifesto_ankidroid.py", command)
        self.assertIn("Companion", command)
        self.assertIn("sessão principal", command.casefold())


if __name__ == "__main__":
    unittest.main()
