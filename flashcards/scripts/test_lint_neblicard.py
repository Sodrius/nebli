#!/usr/bin/env python3
import unittest

from lint_neblicard import lint_text


class LintNebliCardTests(unittest.TestCase):
    def test_rejects_multiple_cloze_indexes(self):
        result = lint_text("<b>Neurociência.</b> Axonal transport uses <b>{{c1::kinesin}}</b> forward and <b>{{c2::dynein}}</b> backward.")
        self.assertEqual(result["status"], "REJECT")
        self.assertTrue(any(flag.startswith("multiple_cloze_indexes") for flag in result["flags"]))

    def test_allows_related_spans_hidden_together(self):
        result = lint_text("<b>Anatomia.</b> The meninges are <b>{{c1::dura}}</b>, <b>{{c1::arachnoid}}</b>, and <b>{{c1::pia}}</b>.")
        self.assertNotEqual(result["status"], "REJECT")

    def test_rejects_missing_cloze(self):
        self.assertEqual(lint_text("<b>Anatomia.</b> The answer is visible.")["status"], "REJECT")

    def test_rejects_missing_theme(self):
        self.assertEqual(lint_text("The <b>{{c1::answer}}</b> is hidden.")["status"], "REJECT")

    def test_rejects_cloze_over_three_words(self):
        result = lint_text("<b>Fisiologia.</b> The result is <b>{{c1::more than three words here}}</b>.")
        self.assertEqual(result["status"], "REJECT")

    def test_rejects_cloze_without_bold(self):
        result = lint_text("<b>Anatomia.</b> The structure is {{c1::a nerve}}.")
        self.assertEqual(result["status"], "REJECT")
        self.assertIn("cloze_not_bold", result["flags"])


if __name__ == "__main__":
    unittest.main()
