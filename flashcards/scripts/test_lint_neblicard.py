#!/usr/bin/env python3
import unittest

from lint_neblicard import lint_text


class LintNebliCardTests(unittest.TestCase):
    def test_rejects_multiple_cloze_indexes(self):
        result = lint_text("Axonal transport uses {{c1::kinesin}} forward and {{c2::dynein}} backward.")
        self.assertEqual(result["status"], "REJECT")
        self.assertTrue(any(flag.startswith("multiple_cloze_indexes") for flag in result["flags"]))

    def test_allows_related_spans_hidden_together(self):
        result = lint_text("The meninges are {{c1::dura}}, {{c1::arachnoid}}, and {{c1::pia}}.")
        self.assertNotEqual(result["status"], "REJECT")

    def test_rejects_missing_cloze(self):
        self.assertEqual(lint_text("The answer is visible.")["status"], "REJECT")


if __name__ == "__main__":
    unittest.main()
