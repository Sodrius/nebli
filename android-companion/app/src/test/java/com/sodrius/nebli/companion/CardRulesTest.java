package com.sodrius.nebli.companion;

import static org.junit.Assert.*;

import java.util.List;

import org.junit.Test;

public class CardRulesTest {
    @Test
    public void goodAuthoredCardPasses() {
        List<String> failures = CardRules.validateAuthoredCloze(
                "The marginal artery runs along the {{c1::colon}}.",
                "A artéria marginal acompanha a borda mesentérica do cólon.",
                "en", "pt-BR", true, true, ""
        );
        assertTrue(failures.toString(), failures.isEmpty());
        assertEquals(1, CardRules.clozeCount("The {{c1::colon}} has haustra."));
        assertEquals(1, CardRules.clozeWordCount("The {{c1::colon}} has haustra."));
    }

    @Test
    public void multipleOrLongClozesFail() {
        List<String> multiple = CardRules.validateAuthoredCloze(
                "The {{c1::colon}} has {{c1::haustra}}.", "", "en", "pt-BR", true, true, ""
        );
        assertTrue(multiple.contains("authored_cloze_count_must_be_1"));

        List<String> longAnswer = CardRules.validateAuthoredCloze(
                "The structure is {{c1::one two three four}}.", "", "en", "pt-BR", true, true, ""
        );
        assertTrue(longAnswer.contains("cloze_answer_over_3_words"));
    }

    @Test
    public void threeWordsNeedReason() {
        List<String> noReason = CardRules.validateAuthoredCloze(
                "The vessel is the {{c1::marginal artery Drummond}}.", "", "en", "pt-BR", true, true, ""
        );
        assertTrue(noReason.contains("three_word_cloze_requires_reason"));
        List<String> withReason = CardRules.validateAuthoredCloze(
                "The vessel is the {{c1::marginal artery Drummond}}.", "", "en", "pt-BR", true, true,
                "Irreducible anatomical name"
        );
        assertFalse(withReason.contains("three_word_cloze_requires_reason"));
    }

    @Test
    public void languageAndAtomicityAreHardGates() {
        List<String> failures = CardRules.validateAuthoredCloze(
                "A estrutura é o {{c1::cólon}}.", "English extra", "pt", "en", false, false, ""
        );
        assertTrue(failures.contains("not_atomic"));
        assertTrue(failures.contains("not_relevant"));
        assertTrue(failures.contains("front_language_not_en"));
        assertTrue(failures.contains("extra_language_not_pt"));
    }

    @Test
    public void basicFallbackHidesAndRevealsOnlyTarget() {
        String text = "The colon contains {{c1::haustra}}.";
        String q = CardRules.clozeQuestion(text);
        String a = CardRules.clozeAnswer(text);
        assertFalse(q.contains("{{c1::"));
        assertTrue(q.contains("[…]") || q.contains("[...]"));
        assertTrue(a.contains("haustra"));
        assertFalse(a.contains("{{c1::"));
    }

    @Test
    public void goodIoPassesAndBadGeometryFails() {
        double[][] good = new double[][]{{0.1, 0.2, 0.2, 0.08}, {0.6, 0.4, 0.15, 0.06}};
        List<String> ok = CardRules.validateIo(
                "hide_all_guess_all", 2, true, true, true, true, true, false, true, good
        );
        assertTrue(ok.toString(), ok.isEmpty());

        double[][] bad = new double[][]{{0.9, 0.2, 0.2, 0.08}};
        List<String> failures = CardRules.validateIo(
                "hide_all_guess_all", 1, true, true, true, true, true, false, true, bad
        );
        assertTrue(failures.contains("mask_out_of_bounds:0"));
    }

    @Test
    public void ioAnswerLeakAndWrongMaskPolicyFail() {
        double[][] box = new double[][]{{0.1, 0.1, 0.2, 0.1}};
        List<String> failures = CardRules.validateIo(
                "hide_all_guess_all", 1, false, true, true, true, true, true, true, box
        );
        assertTrue(failures.contains("io_must_mask_answer_label_not_visual_target"));
        assertTrue(failures.contains("answer_leak"));
    }
}
