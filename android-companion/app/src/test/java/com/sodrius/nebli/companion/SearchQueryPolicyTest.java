package com.sodrius.nebli.companion;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SearchQueryPolicyTest {
    @Test
    public void scopesQueryToAnKingDeck() {
        assertEquals(
                "deck:\"AnKing Step Deck\" TLR4 LPS",
                SearchQueryPolicy.compose("deck:\"AnKing Step Deck\"", "TLR4 LPS"));
    }

    @Test
    public void boundsLargeCollectionScan() {
        assertEquals(320, SearchQueryPolicy.scanLimit(80));
        assertEquals(4, SearchQueryPolicy.scanLimit(1));
        assertEquals(320, SearchQueryPolicy.scanLimit(1000));
    }
}
