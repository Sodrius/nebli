package com.sodrius.nebli.companion;

import static org.junit.Assert.*;

import org.junit.Test;

public class RankerTest {
    @Test
    public void exactPhraseRanksHigh() {
        double s = Ranker.score(
                "portal vein",
                "The {{c1::portal vein}} carries nutrient-rich blood to the liver.",
                "#AK_Step1_v12",
                true
        );
        assertTrue(s >= 0.95);
    }

    @Test
    public void normalizesClozeHintAndLiteralClosingBraces() {
        assertEquals("tlr4 recognizes lps", Ranker.normalize(
                "TLR4 recognizes {{c1::LPS::microbial ligand}}"));
    }

    @Test
    public void unrelatedCardCannotCrossAutoSelectGate() {
        double s = Ranker.score(
                "marginal artery of Drummond",
                "The splenic artery follows the superior border of the pancreas.",
                "#AK_Step1_v12",
                true
        );
        // Compartilhar apenas 'artery' pode produzir algum score lexical, mas
        // deve ficar muito abaixo do gate canônico de 0.82.
        assertTrue(s < 0.50);
        assertFalse(Ranker.confident(s, 0.0, false, 0.82, 0.06));
    }

    @Test
    public void ambiguousScoresDoNotAutoSelect() {
        assertFalse(Ranker.confident(0.86, 0.84, false, 0.82, 0.06));
    }

    @Test
    public void strongExactResultCanAutoSelect() {
        assertTrue(Ranker.confident(0.94, 0.90, true, 0.82, 0.06));
    }

    @Test
    public void detectsTypicalAnKingTags() {
        assertTrue(Ranker.looksAnKing("#AK_Step1_v12::Anatomy"));
        assertTrue(Ranker.looksAnKing("AnKingOverhaul something"));
        assertFalse(Ranker.looksAnKing("NEBLI::source::copy"));
    }

    @Test
    public void realisticFortyCardBatchHasNoFalseAutoSelects() {
        for (int i = 1; i <= 40; i++) {
            String concept = "structure " + i + " portal vein";
            String good = "Clinical anatomy: structure " + i + " portal vein relationship.";
            String distractor = "Unrelated pulmonary physiology and splenic artery fact number " + i + ".";

            double best = Ranker.score(concept, good, "#AK_Step1_v12", true);
            double second = Ranker.score(concept, distractor, "#AK_Step1_v12", true);

            assertTrue("card " + i + " best score", best >= 0.82);
            assertTrue("card " + i + " distractor", second < 0.82);
            assertTrue("card " + i + " confidence", Ranker.confident(best, second, true, 0.82, 0.06));
        }
    }
}
