import sqlite3
import unittest
from types import SimpleNamespace as NS

from nebli.anki_addon import browser_row


class BrowserStatusTests(unittest.TestCase):
    def setUp(self):
        db = sqlite3.connect(":memory:")
        db.execute("create table cards (id, nid, queue, flags)")
        db.executemany("insert into cards values (?,?,?,?)", [
            (1, 10, -1, 3), (2, 10, 2, 3), (3, 20, -2, 4),
            (4, 30, -1, 0), (5, 40, -3, 5),
        ])
        self.col = NS(db=NS(
            scalar=lambda sql, *args: db.execute(sql, args).fetchone()[0],
            list=lambda sql, *args: [r[0] for r in db.execute(sql, args)],
        ))
        self.addCleanup(db.close)

    def status(self, item, note=False):
        row = NS(cells=[NS(text="")])
        browser_row(self.col, item, note, row, ["nebliSuspenso"])
        return row.cells[0].text

    def test_suspension_independent_of_flag_and_burial(self):
        self.assertEqual([self.status(i) for i in range(1, 6)],
                         ["Sim", "Não", "Não", "Sim", "Não"])

    def test_note_mode_does_not_hide_mixed_siblings(self):
        self.assertEqual(self.status(10, True), "1/2")
        self.assertEqual(self.status(20, True), "0/1")
        self.assertEqual(self.status(30, True), "1/1")
        self.assertEqual(self.status(999, True), "—")
