import unittest

from nebli import rotulos


class RotulosTests(unittest.TestCase):
    def test_canonical_keeps_real_parentheses(self):
        self.assertEqual(rotulos.canonical("NEBLI (9)::Grand Round 2 (diabetes mellitus) (67)"),
                         "NEBLI::Grand Round 2 (diabetes mellitus)")
        self.assertFalse(rotulos.labeled("NEBLI::Grand Round 2 (diabetes mellitus)"))

    def test_totals_add_up_the_branch_and_go_parent_first(self):
        decks = {1: "NEBLI", 2: "NEBLI::UC03", 3: "NEBLI::UC03::Micro", 4: "NEBLI::UC03::Pato",
                 9: "Referências::AnKing"}
        steps, conflicts = rotulos.plan(decks, {3: 5, 4: 2, 9: 1000})
        self.assertEqual(steps, [(1, "NEBLI (7)"), (2, "UC03 (7)"), (3, "Micro (5)"), (4, "Pato (2)")])
        self.assertEqual(conflicts, [])

    def test_strip_and_relabel_are_idempotent_on_canonical(self):
        decks = {1: "NEBLI (3)", 2: "NEBLI (3)::A (3)"}
        self.assertEqual(rotulos.plan(decks, {2: 4}, strip=True)[0], [(1, "NEBLI"), (2, "A")])
        self.assertEqual(rotulos.plan(decks, {2: 4})[0], [(1, "NEBLI (4)"), (2, "A (4)")])

    def test_filtered_deck_shows_its_cards_without_double_counting(self):
        decks = {1: "NEBLI", 2: "NEBLI::A", 3: "NEBLI::Revisão"}
        steps, _ = rotulos.plan(decks, {2: 10}, filtered_counts={3: 4})
        self.assertEqual(steps, [(1, "NEBLI (10)"), (2, "A (10)"), (3, "Revisão (4)")])

    def test_top_level_release_deck_is_labeled_but_not_other_roots(self):
        decks = {1: "NEBLI · Microbiologia: todos os novos", 2: "Referências::AnKing", 3: "NEBLI-deck::Etimologia"}
        steps, _ = rotulos.plan(decks, {}, filtered_counts={1: 476})
        self.assertEqual(steps, [(1, "NEBLI · Microbiologia: todos os novos (476)")])

    def test_duplicate_canonical_branch_is_left_alone(self):
        decks = {1: "NEBLI (3)", 2: "NEBLI (3)::A (3)", 3: "NEBLI (3)::A", 4: "NEBLI (3)::B (1)"}
        steps, conflicts = rotulos.plan(decks, {2: 3, 4: 1})
        self.assertEqual(conflicts, ["NEBLI::A"])
        self.assertEqual([d for d, _ in steps], [1, 4])


if __name__ == "__main__":
    unittest.main()
