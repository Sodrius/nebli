import unittest

from nebli import lint_cards


def hard(problems):
    return [msg for level, msg in problems if level == "dura"]


class LintCardsTests(unittest.TestCase):
    def test_anking_like_card_passes(self):
        text = "Tetracyclines bind the {{c1::30S}} subunit, blocking aminoacyl-tRNA attachment"
        self.assertEqual(lint_cards.check("k", text), [])

    def test_semicolon_joining_two_facts_fails(self):
        text = "{{c1::CR1}} binds C3b; {{c2::CR3}} binds iC3b"
        self.assertTrue(any("';'" in msg for msg in hard(lint_cards.check("k", text))))

    def test_portuguese_front_fails(self):
        text = "A mucosa da parede do tubo digestório tem três camadas: {{c1::epitélio}} e lâmina própria"
        self.assertTrue(any("português" in msg for msg in hard(lint_cards.check("k", text))))

    def test_very_long_card_fails_and_long_card_warns(self):
        long = " ".join(["word"] * 26) + " {{c1::answer}}"
        very = " ".join(["word"] * 32) + " {{c1::answer}}"
        self.assertEqual(hard(lint_cards.check("k", long)), [])
        self.assertTrue(lint_cards.check("k", long))
        self.assertTrue(hard(lint_cards.check("k", very)))


if __name__ == "__main__":
    unittest.main()
