import unittest

from nebli import lint_cards


def hard(problems):
    return [msg for level, msg in problems if level == "dura"]


class LintCardsTests(unittest.TestCase):
    def test_source_uncertainty_cannot_be_hidden_in_front(self):
        text = "The source contrasts <b>guanfacine</b> with {{c1::clonidine}}"
        self.assertTrue(any("metacomentário de fonte" in msg
                            for msg in hard(lint_cards.check("k", text))))
        self.assertFalse(hard(lint_cards.check(
            "k", "The source of {{c1::insulin}} is the <b>pancreatic beta cell</b>")))

    def test_ions_and_eg_are_not_portuguese(self):
        self.assertFalse(lint_cards.portuguese("e.g., Na + , K + , Ca 2+ , Cl -"))
        self.assertFalse(lint_cards.portuguese("- H + + HCO 3 - → CO 2 + H 2 O (carbonic anhydrase)"))
        self.assertTrue(lint_cards.portuguese("O ferro entra na célula e sai para o sangue"))

    def test_anking_like_card_passes(self):
        text = "<b>Tetracyclines</b> bind the {{c1::30S}} subunit, blocking aminoacyl-tRNA attachment"
        self.assertEqual(lint_cards.check("k", text), [])

    def test_authored_without_bold_fails(self):
        self.assertTrue(any("sem negrito" in msg for msg in hard(lint_cards.check(
            "k", "Tetracyclines bind the {{c1::30S}} subunit"))))
        self.assertFalse(hard(lint_cards.check("k", "Tetracyclines bind the {{c1::<b>30S</b>}} subunit")))
        self.assertTrue(any("metacomentário de aula" in msg for msg in hard(lint_cards.check(
            "k", "<b>PM2.5</b> is about {{c1::three}} times the guideline shown in the lesson"))))

    def test_semicolon_joining_two_facts_fails(self):
        text = "{{c1::CR1}} binds C3b; {{c2::CR3}} binds iC3b"
        self.assertTrue(any("';'" in msg for msg in hard(lint_cards.check("k", text))))

    def test_portuguese_front_fails(self):
        text = "A mucosa da parede do tubo digestório tem três camadas: {{c1::epitélio}} e lâmina própria"
        self.assertTrue(any("português" in msg for msg in hard(lint_cards.check("k", text))))

    def test_very_long_card_fails_and_long_card_warns(self):
        long = "<b>word</b> " + " ".join(["word"] * 25) + " {{c1::answer}}"
        very = "<b>word</b> " + " ".join(["word"] * 31) + " {{c1::answer}}"
        self.assertEqual(hard(lint_cards.check("k", long)), [])
        self.assertTrue(lint_cards.check("k", long))
        self.assertTrue(hard(lint_cards.check("k", very)))

    def test_extra_prose_and_meta_are_flagged(self):
        text = "<b>Tetracyclines</b> bind the {{c1::30S}} subunit"
        prose = "The lecture lists this mechanism. " + " ".join(["word"] * 20)
        problems = lint_cards.check("k", text, prose)
        self.assertTrue(any("metacomentário" in msg for msg in hard(problems)))
        self.assertTrue(any("parágrafo" in msg for _, msg in problems))
        self.assertEqual(lint_cards.check("k", text, "- Blocks <b>aminoacyl-tRNA</b> binding"), [])

    def test_plan_authored_needs_reason_and_search(self):
        self.assertTrue(hard(lint_cards.justification({"origin": "Autoral"})))
        ok = {"origin": "Autoral", "autoria": "prova", "busca": "AnKing CH50 só LES; lacuna"}
        self.assertTrue(any("espelhos" in msg for msg in hard(lint_cards.justification(ok))))
        ok["espelhos"] = [1467772038626, 1467772044746]
        self.assertEqual(lint_cards.justification(ok), [])

    def test_this_is_can_explain_science_without_curatorial_meta(self):
        text = 'Which curves determine the <b>therapeutic index</b>? {{c1::Therapeutic and toxic}}'
        extra = '- This is a population response, not half of the maximal effect in one person.'
        self.assertFalse(hard(lint_cards.check('g-quantal', text, extra)))
        self.assertTrue(any('metacomentário' in msg for msg in hard(
            lint_cards.check('g-quantal', text, '- This card covers the population response.'))))

    def test_plan_with_authored_cards_needs_external_search_evidence(self):
        import json, tempfile
        from pathlib import Path
        entry = {"key": "k", "origin": "Autoral", "autoria": "prova", "busca": "x", "espelhos": [1, 2],
                 "fields": {"Text": "Colipase anchors {{c1::lipase}}", "Extra": ""}, "cards": [{}]}
        with tempfile.TemporaryDirectory() as d:
            plan = Path(d) / "plan.json"
            plan.write_text(json.dumps({"entries": [entry]}))
            self.assertTrue(any("busca_externos" in m for _, _, _, ps in lint_cards.from_plan(plan) for _, m in ps))
            (Path(d) / "ext.txt").write_text("busca")
            plan.write_text(json.dumps({"entries": [entry], "busca_externos": "ext.txt"}))
            self.assertFalse(any("busca_externos" in m for _, _, _, ps in lint_cards.from_plan(plan) for _, m in ps))


if __name__ == "__main__":
    unittest.main()


class CausalExtraTest(unittest.TestCase):
    def test_extra_must_teach_why(self):
        from nebli import lint_cards as l
        bad = l.check("k", "<b>Adenovirus</b> uses a terminal protein {{c1::<b>primer</b>}} linked to dCMP", "- Adenovirus uses a terminal protein primer")
        self.assertTrue(any("repete a frente" in p for _, p in bad))
        good = l.check("k", "<b>Adenovirus</b> uses a terminal protein {{c1::<b>primer</b>}} linked to dCMP", "- No 5' gap is left, so the genome is never shortened")
        self.assertFalse(any("repete a frente" in p for _, p in good))

