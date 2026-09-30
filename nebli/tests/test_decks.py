import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from nebli import decks

DECKS = ["NEBLI", "NEBLI::UC03", "NEBLI::UC03::P2", "NEBLI::UC03::P2::Microbiologia",
         "NEBLI::UC03::P2::Microbiologia::Controle microbiológico",
         "NEBLI::UC03::P2::Microbiologia::Fisiologia bacteriana",
         "NEBLI::UC03::P2::Microbiologia::Genética bacteriana",
         "Referências::Anking Step Deck::Microbiology::Bacteria"]


class FakeAnki:
    def __init__(self, suspended, names=DECKS):
        self.suspended = dict(suspended)
        self.names = names
        self.writes = []

    def __call__(self, action, **params):
        if action == "deckNames":
            return self.names
        if action == "findCards":
            want = "-is:suspended" not in params["query"]
            return [c for c, s in self.suspended.items() if s is want]
        if action in ("suspend", "unsuspend"):
            self.writes.append((action, list(params["cards"])))
            for c in params["cards"]:
                self.suspended[c] = action == "suspend"
            return True
        if action == "areSuspended":
            return [self.suspended.get(c) for c in params["cards"]]
        if action == "sync":
            self.writes.append(("sync", None))
            return None
        raise AssertionError(action)


class DecksTests(unittest.TestCase):
    def setUp(self):
        tmp = Path(tempfile.mkdtemp())
        self.patches = [patch.object(decks, "LOCK", tmp / "ANKI-ESCRITA.lock"),
                        patch.object(decks, "OPS_DIR", tmp / "ops"),
                        patch.object(decks, "LIMITS", tmp / "anki-decks.json"),
                        patch.object(decks, "ESPERA", 0)]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in self.patches:
            p.stop()

    def test_parent_branch_covers_subdecks_and_accents_are_ignored(self):
        self.assertEqual(decks.resolve(DECKS, ["microbiologia"])[0],
                         ["NEBLI::UC03::P2::Microbiologia"])
        self.assertEqual(decks.resolve(DECKS, ["BACTERIANA"])[0], [
            "NEBLI::UC03::P2::Microbiologia::Fisiologia bacteriana",
            "NEBLI::UC03::P2::Microbiologia::Genética bacteriana"])
        self.assertEqual(decks.resolve(DECKS, ["controle microbiologico"])[0],
                         ["NEBLI::UC03::P2::Microbiologia::Controle microbiológico"])

    def test_never_reaches_anking_or_references(self):
        self.assertEqual(decks.resolve(DECKS, ["bacteria"])[0], [
            "NEBLI::UC03::P2::Microbiologia::Fisiologia bacteriana",
            "NEBLI::UC03::P2::Microbiologia::Genética bacteriana"])
        self.assertEqual(decks.resolve(DECKS, ["anking"]), ([], ["anking"]))

    def test_simulate_does_not_write(self):
        anki = FakeAnki({1: True, 2: False})
        self.assertIsNone(decks.change(anki, ["micro"], suspend=False, simulate=True))
        self.assertEqual(anki.writes, [])

    def test_unsuspend_records_ids_checks_and_syncs(self):
        anki = FakeAnki({1: True, 2: True, 3: False})
        record = decks.change(anki, ["micro"], suspend=False)
        self.assertEqual(record["card_ids"], [1, 2])
        self.assertEqual(record["estado"], "conferido")
        self.assertEqual(anki.writes, [("unsuspend", [1, 2]), ("sync", None)])
        self.assertFalse(decks.LOCK.exists())

    def test_existing_lock_blocks_before_any_write(self):
        decks.LOCK.parent.mkdir(parents=True, exist_ok=True)
        decks.LOCK.write_text('{"executor": "Codex"}', encoding="utf-8")
        anki = FakeAnki({1: True})
        with self.assertRaises(SystemExit):
            decks.change(anki, ["micro"], suspend=False)
        self.assertEqual(anki.writes, [])
        self.assertTrue(decks.LOCK.exists())

    def test_undo_restores_only_recorded_cards_still_changed(self):
        anki = FakeAnki({1: True, 2: True, 3: True})
        decks.change(anki, ["micro"], suspend=False, sync=False)
        anki.suspended[2] = True  # Davi suspendeu de novo à mão depois
        del anki.suspended[3]      # card apagado depois
        path = sorted(decks.OPS_DIR.glob("*.json"))[0]
        self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["card_ids"], [1, 2, 3])
        anki.writes.clear()
        decks.undo(anki, path, sync=False)
        self.assertEqual(anki.writes, [("suspend", [1])])

    def test_matches_canonical_name_behind_card_totals(self):
        live = ["NEBLI (5)", "NEBLI (5)::UC03 (5)", "NEBLI (5)::UC03 (5)::Microbiologia (5)",
                "NEBLI (5)::UC03 (5)::Microbiologia (5)::Antibióticos e resistência (5)"]
        self.assertEqual(decks.resolve(live, ["microbiologia"])[0], [live[2]])
        self.assertEqual(decks.resolve(live, ["(5)"]), ([], ["(5)"]))

    def test_write_refused_while_totals_stay_in_names(self):
        live = ["NEBLI (2)", "NEBLI (2)::Microbiologia (2)"]
        anki = FakeAnki({1: True, 2: True}, names=live)
        with self.assertRaises(SystemExit):
            decks.change(anki, ["micro"], suspend=False)
        self.assertEqual(anki.writes, [])
        self.assertFalse(decks.LOCK.exists())

    def test_release_goes_to_config_by_canonical_name(self):
        live = ["NEBLI (2)", "NEBLI (2)::Microbiologia (2)", "NEBLI (2)::Microbiologia (2)::A (2)"]
        anki = FakeAnki({}, names=live)
        with patch.object(decks, "count_on_click", return_value=None):
            decks.release(anki, ["micro"])
        self.assertEqual(json.loads(decks.LIMITS.read_text(encoding="utf-8")),
                         {"liberar_novos": ["NEBLI::Microbiologia"]})
        decks.release(anki, ["micro"], stop=True)
        self.assertEqual(json.loads(decks.LIMITS.read_text(encoding="utf-8")), {"liberar_novos": []})
        with patch.object(decks, "count_on_click", return_value=None):
            decks.release(anki, ["micro"], train=True)
        self.assertEqual(json.loads(decks.LIMITS.read_text(encoding="utf-8")),
                         {"liberar_novos": [], "treino_novos": ["NEBLI::Microbiologia"]})
        self.assertEqual(anki.writes, [])

    def test_reinstall_repairs_missing_config_without_overwriting_user_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            target = home / 'Library/Application Support/Anki2/addons21/nebli_decks'
            target.mkdir(parents=True)
            original_meta = '{"disabled": false, "custom": "preservar"}'
            (target / 'meta.json').write_text(original_meta)
            with patch.object(decks.sys, 'platform', 'darwin'), patch.object(Path, 'home', return_value=home):
                decks.install_addon()
                self.assertEqual(json.loads((target / 'config.json').read_text())['repo'], str(decks.ROOT))
                self.assertEqual((target / 'meta.json').read_text(), original_meta)
                (target / 'config.json').write_text('{"repo":"antigo", "opcao_pessoal":true}')
                decks.install_addon()
            self.assertEqual(json.loads((target / 'config.json').read_text()),
                             {'repo': str(decks.ROOT), 'opcao_pessoal': True})
            shortcuts = target.parent / 'nebli_atalhos'
            self.assertTrue((shortcuts / '__init__.py').exists())
            self.assertIn('asdf', (shortcuts / '__init__.py').read_text(encoding='utf-8').replace(' ', ''))

if __name__ == "__main__":
    unittest.main()
