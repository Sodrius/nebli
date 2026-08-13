package com.sodrius.nebli.companion;

import static org.junit.Assert.*;

import java.util.List;

import org.junit.Test;

public class CardRulesTest {
    private static List<String> validateAuthored(
            String text, String extra, String frontLanguage, String extraLanguage,
            boolean atomic, boolean relevant, String threeWordReason
    ) {
        return CardRules.validateAuthoredCloze(
                text, extra, frontLanguage, extraLanguage, atomic, relevant, threeWordReason,
                true, "rotulo_especifico", true, false, false, false, true, 0, true);
    }

    @Test
    public void goodAuthoredCardPasses() {
        List<String> failures = validateAuthored(
                "A artéria marginal acompanha o {{c1::cólon}}.",
                "A artéria marginal acompanha a borda mesentérica do cólon.",
                "pt-BR", "pt-BR", true, true, ""
        );
        assertTrue(failures.toString(), failures.isEmpty());
        assertEquals(1, CardRules.clozeCount("O {{c1::cólon}} apresenta haustrações."));
        assertEquals(1, CardRules.clozeWordCount("O {{c1::cólon}} apresenta haustrações."));
    }

    @Test
    public void multipleOrLongClozesFail() {
        List<String> multiple = validateAuthored(
                "O {{c1::cólon}} apresenta {{c1::haustrações}}.", "", "pt-BR", "pt-BR", true, true, ""
        );
        assertTrue(multiple.contains("authored_cloze_count_must_be_1"));

        List<String> longAnswer = validateAuthored(
                "A estrutura é {{c1::uma duas três quatro}}.", "", "pt-BR", "pt-BR", true, true, ""
        );
        assertTrue(longAnswer.contains("cloze_answer_over_3_words"));
    }

    @Test
    public void threeWordsNeedReason() {
        List<String> noReason = validateAuthored(
                "O vaso é a {{c1::artéria marginal Drummond}}.", "", "pt-BR", "pt-BR", true, true, ""
        );
        assertTrue(noReason.contains("three_word_cloze_requires_reason"));
        List<String> withReason = validateAuthored(
                "O vaso é a {{c1::artéria marginal Drummond}}.", "", "pt-BR", "pt-BR", true, true,
                "Nome anatômico irredutível"
        );
        assertFalse(withReason.contains("three_word_cloze_requires_reason"));
    }

    @Test
    public void languageAndAtomicityAreHardGates() {
        List<String> failures = validateAuthored(
                "The structure is the {{c1::colon}}.",
                "The extra is provided with English context.", "en", "en", false, false, ""
        );
        assertTrue(failures.contains("not_atomic"));
        assertTrue(failures.contains("not_relevant"));
        assertTrue(failures.contains("front_language_not_pt"));
        assertTrue(failures.contains("front_appears_english"));
        assertTrue(failures.contains("extra_language_not_pt"));
        assertTrue(failures.contains("extra_appears_english"));
    }

    @Test
    public void inductionReviewIsAHardGate() {
        List<String> failures = CardRules.validateAuthoredCloze(
                "A fixação imediata impede a {{c1::autólise}}.", "", "pt-BR", "pt-BR",
                true, true, "", true, "mecanismo", false, true, true, true,
                false, 2, false);
        assertTrue(failures.contains("knowledge_not_required"));
        assertTrue(failures.contains("grammar_only_solvable"));
        assertTrue(failures.contains("lexical_leak"));
        assertTrue(failures.contains("answer_visible_elsewhere"));
        assertTrue(failures.contains("blind_review_not_passed"));
        assertTrue(failures.contains("unresolved_plausible_alternatives"));
        assertTrue(failures.contains("ambiguity_not_reviewed"));
    }

    @Test
    public void basicFallbackHidesAndRevealsOnlyTarget() {
        String text = "O cólon apresenta {{c1::haustrações}}.";
        String q = CardRules.clozeQuestion(text);
        String a = CardRules.clozeAnswer(text);
        assertFalse(q.contains("{{c1::"));
        assertTrue(q.contains("[…]") || q.contains("[...]"));
        assertTrue(a.contains("haustra"));
        assertFalse(a.contains("{{c1::"));
    }

    @Test
    public void clozeWithHintAndClosingBracesParsesWithoutStaticInitializer() {
        String text = "TLR4 recognizes {{c1::LPS::microbial ligand}}.";
        assertEquals(1, CardRules.clozeCount(text));
        assertEquals(1, CardRules.clozeWordCount(text));
        assertFalse(CardRules.clozeQuestion(text).contains("{{c1::"));
        assertTrue(CardRules.clozeAnswer(text).contains("LPS"));
    }

    @Test
    public void goodIoPassesAndBadGeometryFails() {
        double[][] good = new double[][]{{0.1, 0.2, 0.2, 0.08}, {0.6, 0.4, 0.15, 0.06}};
        List<String> ok = CardRules.validateIo(
                "hide_two_guess_two", 2, true, true, true, true, true, false, true, good
        );
        assertTrue(ok.toString(), ok.isEmpty());

        double[][] bad = new double[][]{{0.9, 0.2, 0.2, 0.08}};
        List<String> failures = CardRules.validateIo(
                "hide_two_guess_two", 1, true, true, true, true, true, false, true, bad
        );
        assertTrue(failures.contains("mask_out_of_bounds:0"));
    }

    @Test
    public void ioAnswerLeakAndWrongMaskPolicyFail() {
        double[][] box = new double[][]{{0.1, 0.1, 0.2, 0.1}};
        List<String> failures = CardRules.validateIo(
                "hide_two_guess_two", 1, false, true, true, true, true, true, true, box
        );
        assertTrue(failures.contains("io_must_mask_answer_label_not_visual_target"));
        assertTrue(failures.contains("answer_leak"));
    }

    @Test
    public void hideTwoRejectsMoreThanTwoMasks() {
        double[][] boxes = new double[][]{
                {0.1, 0.1, 0.1, 0.1}, {0.3, 0.1, 0.1, 0.1}, {0.5, 0.1, 0.1, 0.1}};
        List<String> failures = CardRules.validateIo(
                "hide_two_guess_two", 3, true, true, true, true, true, false, true, boxes);
        assertTrue(failures.contains("hide_two_guess_two_max_two_masks"));
    }
}
