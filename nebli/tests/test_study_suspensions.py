import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
from nebli import anki_addon as addon


class StudySuspensionTests(unittest.TestCase):
    def test_restore_only_returned_cards_and_keep_active_for_restart(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'nebli-estudo-suspensos.json'
            path.write_text(json.dumps({'1': 90, '2': 90, '3': 90}))
            col = MagicMock()
            col.db.first.side_effect = [(10, 0), (90, 10), None]
            mw = SimpleNamespace(state='deckBrowser', col=col,
                                 pm=SimpleNamespace(profileFolder=lambda: directory))
            with patch.object(addon, 'LOCK', Path(directory) / 'absent.lock'):
                self.assertEqual(addon.restore_study_suspensions(mw, lambda _: None), 1)
            col.sched.suspend_cards.assert_called_once_with([1])
            self.assertEqual(json.loads(path.read_text()), {'2': 90})
            # Após apagar o filtrado, o mesmo registro sobrevive e restaura o restante.
            col.db.first.side_effect = [(10, 0)]
            with patch.object(addon, 'LOCK', Path(directory) / 'absent.lock'):
                addon.restore_study_suspensions(mw, lambda _: None)
            self.assertEqual(json.loads(path.read_text()), {})
            self.assertEqual(col.sched.suspend_cards.call_args.args[0], [2])

    def test_does_not_touch_cards_during_review(self):
        mw = SimpleNamespace(state='review', col=MagicMock())
        self.assertEqual(addon.restore_study_suspensions(mw, lambda _: None), 0)
        mw.col.sched.suspend_cards.assert_not_called()
