import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from nebli import anki_addon


def fake_col(decks):
    """decks: {did: (nome, filtrado?)}"""
    col = MagicMock()
    col.decks.all_names_and_ids.return_value = [SimpleNamespace(id=d, name=n) for d, (n, _) in decks.items()]
    col.decks.is_filtered.side_effect = lambda did: decks[did][1]
    col.db.scalar.return_value = 5  # há novos a reunir
    return col


class ReleaseNewTests(unittest.TestCase):
    def run_release(self, config, managed, decks):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            cfg = tmp / "anki-decks.json"
            cfg.write_text(json.dumps(config))
            (tmp / "filtrados.json").write_text(json.dumps(managed))
            col, logs = fake_col(decks), []
            with patch.object(anki_addon, "CONFIG", cfg):
                anki_addon.release_new(col, SimpleNamespace(state="deckBrowser"), tmp, logs.append)
            return json.loads(cfg.read_text()), json.loads((tmp / "filtrados.json").read_text()), col, logs

    def test_manually_deleted_filtered_deck_is_not_recreated(self):
        name = anki_addon.filtered_name("NEBLI::UC03::P2::Imunologia")
        config, managed, col, logs = self.run_release(
            {"liberar_novos": ["NEBLI::UC03::P2::Imunologia"], "treino_novos": []}, [name],
            {1: ("NEBLI::UC03::P2::Imunologia", False)})
        self.assertEqual(config["liberar_novos"], [])
        self.assertEqual(managed, [])
        col.sched.get_or_create_filtered_deck.assert_not_called()
        self.assertTrue(any("apagado à mão" in line for line in logs))

    def test_new_release_is_created_once(self):
        config, managed, col, _ = self.run_release(
            {"liberar_novos": ["NEBLI::UC03::P2::Imunologia"]}, [],
            {1: ("NEBLI::UC03::P2::Imunologia", False)})
        self.assertEqual(config["liberar_novos"], ["NEBLI::UC03::P2::Imunologia"])
        col.sched.get_or_create_filtered_deck.assert_called_once()
        self.assertEqual(managed, [anki_addon.filtered_name("NEBLI::UC03::P2::Imunologia")])


if __name__ == "__main__":
    unittest.main()
