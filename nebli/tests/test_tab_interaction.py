"""Keyboard routing and persistent feedback, without a running Anki GUI."""
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace as NS
from unittest.mock import MagicMock, patch
from nebli import explicacoes, lint_cards


class TabInteractionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name)
        note = NS(fields=['front', 'back'])
        self.mw = NS(state='review', reviewer=NS(
            state='answer', card=NS(id=1, nid=9, did=3, ord=0, note=lambda: note), web=MagicMock()))
        self.app = NS(activeWindow=lambda: self.mw, instance=lambda: MagicMock())
        qt = NS(QApplication=self.app, QEvent=NS(Type=NS(KeyPress=1)), QObject=object,
                Qt=NS(Key=NS(Key_Tab=9, Key_X=88)), QTimer=NS(singleShot=lambda _, fn: fn()))
        hooks = NS(reviewer_did_show_question=[], reviewer_did_show_answer=[])
        # Redirect USER before the add-on's startup log, without touching real user_files.
        source = Path(__file__).resolve().parents[2] / 'anki-addon/nebli_explicacoes/__init__.py'
        self.ns = {'__file__': str(self.path / '__init__.py')}
        self.patcher = patch.dict('sys.modules', {'aqt': NS(gui_hooks=hooks, mw=self.mw),
                                                'aqt.qt': qt, 'aqt.utils': NS(tooltip=MagicMock())})
        self.patcher.start()
        self.addCleanup(self.patcher.stop)
        exec(compile(source.read_text(), str(source), 'exec'), self.ns)
        self.ns['_lookup'] = lambda card: None
        self.ns['_toggle']()

    def press(self, key, repeat=False, modifiers=0):
        event = NS(type=lambda: 1, isAutoRepeat=lambda: repeat, key=lambda: key, modifiers=lambda: modifiers)
        return self.ns['_tab'].eventFilter(None, event)

    def test_x_toggles_card_like_without_closing_and_tab_only_closes(self):
        self.assertTrue(self.press(88))
        self.assertTrue(self.ns['_popup']['open'])
        self.assertTrue(self.ns['_is_liked'](1))
        self.press(9)
        self.assertFalse(self.ns['_popup']['open'])
        self.assertTrue(self.press(88))
        self.assertFalse(self.ns['_is_liked'](1))
        self.press(9)
        self.assertFalse(self.ns['_popup']['gostei'])
        self.press(88)
        self.assertTrue(self.ns['_is_liked'](1))
        self.assertEqual(len(explicacoes.liked_cards(self.path / 'user_files/tab-log.jsonl')), 1)

    def test_repeat_and_other_window_do_not_like_but_closed_popup_does(self):
        self.press(88, repeat=True)
        self.assertFalse(self.ns['_is_liked'](1))
        self.app.activeWindow = lambda: None
        self.press(88)
        self.assertFalse(self.ns['_is_liked'](1))
        self.app.activeWindow = lambda: self.mw
        self.ns['_close_popup']()
        self.assertTrue(self.press(88))
        self.assertTrue(self.ns['_is_liked'](1))
        self.mw.reviewer.card.id = 2
        self.press(88)
        self.assertTrue(self.ns['_is_liked'](2))

    def test_cancel_old_version_does_not_remove_new_version_report(self):
        log = self.path / 'log.jsonl'
        log.write_text('\n'.join(json.dumps(e) for e in [
            {'evento': 'tab_ruim', 'card': 1, 'explicacao': 'new'},
            {'evento': 'tab_ruim_desfeito', 'card': 1, 'explicacao': 'old'}]))
        db = explicacoes.open_store(self.path / 'test.sqlite')
        self.addCleanup(db.close)
        self.assertEqual(len(explicacoes.bad_tabs(log, db)), 1)

    def test_organizer_exception_is_explicit(self):
        text = ('A tríade característica da <b>inflamação crônica</b> é constituída por:<br>'
                'C {{c2::cicatriz}}<br>I {{c1::infiltrado mononuclear}}<br>D {{c2::destruição tissular}}')
        marked = '<div data-nebli-organizacao="true" data-nebli-pista="CID">' + text + '</div>'
        self.assertFalse([p for p in lint_cards.check('cid', marked) if p[0] == 'dura'])
        self.assertTrue([p for p in lint_cards.check('cid', text) if p[0] == 'dura'])
        self.assertEqual(explicacoes.hidden_target({'Text': {'value': marked}}, 1), 'cicatriz; destruição tissular')


if __name__ == '__main__':
    unittest.main()
