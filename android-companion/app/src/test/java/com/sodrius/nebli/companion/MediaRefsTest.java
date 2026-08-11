package com.sodrius.nebli.companion;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.Set;

import org.junit.Test;

public class MediaRefsTest {
    @Test
    public void extractsLocalImagesAcrossQuestionAndAnswer() {
        AnkiBridge.CardRow row = new AnkiBridge.CardRow(
                0,
                "<IMG class='x' SRC=\"front%20image.png\">",
                "<img src='back.svg'><img src=\"front%20image.png\">",
                1L);
        Set<String> refs = MediaRefs.images(row);
        assertEquals(2, refs.size());
        assertTrue(refs.contains("front image.png"));
        assertTrue(refs.contains("back.svg"));
    }

    @Test
    public void rejectsRemoteAndDataImages() {
        Set<String> refs = MediaRefs.images(
                "<img src='https://example.com/x.png'><img src='data:image/png;base64,x'>");
        assertTrue(refs.isEmpty());
        assertFalse(refs.contains("x.png"));
    }
}
