package com.sodrius.nebli.companion;

import static org.junit.Assert.assertArrayEquals;

import org.junit.Test;

public class AnkiBridgeTest {
    @Test
    public void authoredExtraUsesStandardBackExtraField() {
        assertArrayEquals(
                new String[]{"Question {{c1::answer}}", "Apoio visual", ""},
                AnkiBridge.fieldsForModel(
                        new String[]{"Text", "Back Extra", "Tags"},
                        "Question {{c1::answer}}",
                        "Apoio visual")
        );
    }

    @Test
    public void authoredExtraPrefersExactExtraField() {
        assertArrayEquals(
                new String[]{"Question {{c1::answer}}", "Apoio", ""},
                AnkiBridge.fieldsForModel(
                        new String[]{"Text", "Extra", "Back Extra"},
                        "Question {{c1::answer}}",
                        "Apoio")
        );
    }
}
