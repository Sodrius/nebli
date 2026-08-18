#!/usr/bin/env python3
import unittest

from lint_neblicard import lint_text


class LintNebliCardTests(unittest.TestCase):
    def test_rejects_multiple_cloze_indexes(self):
        result = lint_text("<b>Neurociência.</b> Axonal transport uses <b>{{c1::kinesin}}</b> forward and <b>{{c2::dynein}}</b> backward.")
        self.assertEqual(result["status"], "REJECT")
        self.assertTrue(any(flag.startswith("multiple_cloze_indexes") for flag in result["flags"]))

    def test_rejects_multiple_related_spans_to_preserve_atomicity(self):
        result = lint_text("<b>Anatomia.</b> The meninges are <b>{{c1::dura}}</b>, <b>{{c1::arachnoid}}</b>, and <b>{{c1::pia}}</b>.")
        self.assertEqual(result["status"], "REJECT")
        self.assertTrue(any(flag.startswith("multiple_cloze_occurrences") for flag in result["flags"]))

    def test_rejects_missing_cloze(self):
        self.assertEqual(lint_text("<b>Anatomia.</b> The answer is visible.")["status"], "REJECT")

    def test_card_sem_rotulo_tematico_passa(self):
        # Rótulo temático aposentado em 2026-08-17: a ausência dele não reprova mais.
        self.assertEqual(lint_text("The <b>{{c1::answer}}</b> is hidden.")["status"], "PASS")

    def test_rejects_cloze_over_three_words(self):
        result = lint_text("<b>Fisiologia.</b> The result is <b>{{c1::more than three words here}}</b>.")
        self.assertEqual(result["status"], "REJECT")

    def test_one_word_cloze_is_preferred(self):
        result = lint_text("<b>Fisiologia.</b> The vessel is <b>{{c1::compliant}}</b>.")
        self.assertEqual(result["status"], "PASS")

    def test_two_word_cloze_is_allowed(self):
        result = lint_text("<b>Anatomia.</b> Supply comes from the <b>{{c1::left gastric}}</b> artery.")
        self.assertEqual(result["status"], "PASS")
        self.assertIn("two_word_cloze", result["flags"])

    def test_three_word_cloze_requires_manual_exception(self):
        result = lint_text("<b>Fisiologia.</b> This forms a <b>{{c1::high pressure zone}}</b>.")
        self.assertEqual(result["status"], "MIRROR")
        self.assertIn("three_word_cloze_requires_exception", result["flags"])

    def test_rejects_cloze_without_bold(self):
        result = lint_text("<b>Anatomia.</b> The structure is {{c1::a nerve}}.")
        self.assertEqual(result["status"], "REJECT")
        self.assertIn("cloze_not_bold", result["flags"])


if __name__ == "__main__":
    unittest.main()
