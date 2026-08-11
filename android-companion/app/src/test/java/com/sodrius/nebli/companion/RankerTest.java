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
    public void unrelatedCardRanksLow() {
        double s = Ranker.score(
                "marginal artery of Drummond",
                "The splenic artery follows the superior border of the pancreas.",
                "#AK_Step1_v12",
                true
        );
        assertTrue(s < 0.30);
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
}
