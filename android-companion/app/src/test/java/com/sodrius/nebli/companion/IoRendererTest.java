package com.sodrius.nebli.companion;

import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;

public class IoRendererTest {
    @Test
    public void questionContainsImageAndAllMasks() {
        String html = IoRenderer.questionHtml(
                "colon.png",
                Arrays.asList(new double[]{0.1, 0.2, 0.2, 0.08}, new double[]{0.5, 0.3, 0.1, 0.06}),
                "Identify the labels."
        );
        assertTrue(html.contains("colon.png"));
        assertTrue(html.contains("Identify the labels."));
        assertEquals(2, occurrences(html, "nebli-io-mask"));
        assertTrue(html.contains("left:10.0000%"));
        assertTrue(html.contains("top:20.0000%"));
    }

    @Test
    public void answerRevealsLabelsAndCredits() {
        String html = IoRenderer.answerHtml(
                "colon.png",
                Arrays.asList("hepatic flexure", "splenic flexure"),
                "Lecture atlas"
        );
        assertTrue(html.contains("colon.png"));
        assertTrue(html.contains("hepatic flexure"));
        assertTrue(html.contains("splenic flexure"));
        assertTrue(html.contains("Lecture atlas"));
        assertFalse(html.contains("nebli-io-mask"));
    }

    @Test
    public void rendererEscapesLabelsAndPrompt() {
        String q = IoRenderer.questionHtml("x.png", Arrays.asList(new double[]{0.1, 0.1, 0.1, 0.1}), "<script>x</script>");
        String a = IoRenderer.answerHtml("x.png", Arrays.asList("<b>answer</b>"), "A&B");
        assertFalse(q.contains("<script>"));
        assertTrue(q.contains("&lt;script&gt;"));
        assertTrue(a.contains("&lt;b&gt;answer&lt;/b&gt;"));
        assertTrue(a.contains("A&amp;B"));
    }

    private int occurrences(String s, String needle) {
        int count = 0, from = 0;
        while ((from = s.indexOf(needle, from)) >= 0) {
            count++;
            from += needle.length();
        }
        return count;
    }
}
