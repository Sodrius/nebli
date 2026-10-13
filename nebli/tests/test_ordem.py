import unittest

from nebli import ordem

A = ["NEBLI::2026-x", "NEBLI::ordem::operon-02", "NEBLI::objetivo::B-lac"]
B = ["NEBLI::2026-x", "NEBLI::ordem::operon-10"]
SHARED = ["NEBLI::2026-x", "NEBLI::2026-y", "NEBLI::ordem::imuno31-03", "NEBLI::ordem::operon-01"]


class OrdemTests(unittest.TestCase):
    def test_sorts_numerically_in_the_lesson_being_viewed(self):
        main = ordem.dominant([A, B, SHARED, []])
        self.assertEqual(main, "operon")
        got = sorted([B, [], A, SHARED], key=lambda t: ordem.sort_key(t, main))
        self.assertEqual(got, [SHARED, A, B, []])

    def test_label_shows_only_numbers_and_respects_lesson_context(self):
        self.assertEqual(ordem.label(A), "02")
        self.assertEqual(ordem.label(SHARED), "01 | 03")
        self.assertEqual(ordem.label(SHARED, "operon"), "01")
        self.assertEqual(ordem.label(SHARED, "imuno31"), "03")
        self.assertEqual(ordem.label(["NEBLI::2026-x"]), "")

    def test_check_flags_missing_shared_foreign_prefix_and_plan_gap(self):
        notes = {1: A, 2: B, 3: ["NEBLI::2026-x", "NEBLI::ordem::imuno31-03"]}
        others = {9: ["NEBLI::2026-z", "NEBLI::ordem::operon-05"]}
        plan = {"entries": [{"order": 2, "evid": "Slide 9"}, {"order": 10, "evid": "Slides 4, 6"},
                            {"order": 11, "evid": "Slide 12"}]}
        problems, warnings, main = ordem.check("NEBLI::2026-x", notes, others, plan)
        self.assertEqual(main, "operon")
        text = " ".join(problems)
        self.assertIn("sem posição", text)
        self.assertIn("fora da aula", text)
        self.assertIn("ausentes no Anki", text)
        self.assertTrue(any("recuo" in w for w in problems))

    def test_check_passes_clean_lesson(self):
        self.assertEqual(ordem.check("NEBLI::2026-x", {1: A, 2: B}, {})[0], [])

    def test_addon_sorts_browser_results_by_lesson_order(self):
        from types import SimpleNamespace as NS
        from nebli import anki_addon
        cards = [(11, " ".join(B), 0, 2), (12, " ".join(A), 1, 1), (13, " ".join(A), 0, 1), (14, "", 0, 3), (99, "x", 0, 4)]
        db = NS(all=lambda sql: cards,
                scalar=lambda sql, i: {12: 1}.get(i) if "cards" in sql else " ".join(A))
        col = NS(db=db, find_cards=lambda search, order: [14, 11, 12, 13])
        ctx = NS(order=NS(key=ordem.KEY), reverse=False, search="x", ids=None,
                 browser=NS(table=NS(is_notes_mode=lambda: False)))
        anki_addon.browser_search(col, ctx)
        self.assertEqual(ctx.ids, [13, 12, 11, 14])
        other = NS(order=NS(key="deck"), ids=None)
        anki_addon.browser_search(col, other)
        self.assertIsNone(other.ids)
        row = NS(cells=[NS(text=""), NS(text="")])
        anki_addon.browser_row(col, 12, False, row, ["question", ordem.KEY])
        self.assertEqual(row.cells[1].text, "02")


if __name__ == "__main__":
    unittest.main()
