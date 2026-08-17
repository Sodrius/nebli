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
                "Identifique os rótulos."
        );
        assertTrue(html.contains("colon.png"));
        assertTrue(html.contains("Identifique os rótulos."));
        assertEquals(2, occurrences(html, "nebli-io-mask"));
        assertTrue(html.contains("left:10.0000%"));
        assertTrue(html.contains("top:20.0000%"));
    }

    @Test
    public void answerShowsEachLabelExactlyOnceOverTheImage() {
        String html = IoRenderer.answerHtml(
                "colon.png",
                Arrays.asList(new double[]{0.1, 0.2, 0.2, 0.08}, new double[]{0.5, 0.3, 0.1, 0.06}),
                Arrays.asList("flexura hepática", "flexura esplênica")
        );
        assertTrue(html.contains("colon.png"));
        assertEquals(2, occurrences(html, "nebli-io-answer-label"));
        assertFalse(html.contains("nebli-io-mask"));
        // Cada resposta aparece uma única vez. A lista repetida abaixo da imagem
        // era o que produzia "light chainheavy chain" no texto plano da nota.
        assertEquals(1, occurrences(html, "flexura hepática"));
        assertEquals(1, occurrences(html, "flexura esplênica"));
        assertFalse(html.contains("nebli-io-answers"));
    }

    @Test
    public void answerNeverRendersTheSourceCredit() {
        String html = IoRenderer.answerHtml(
                "colon.png",
                Arrays.asList(new double[]{0.1, 0.2, 0.2, 0.08}),
                Arrays.asList("flexura hepática")
        );
        // O crédito continua guardado no campo Source da nota; ele apenas não é
        // lido durante a revisão.
        assertFalse(html.contains("nebli-source"));
        assertFalse(html.contains("Atlas da aula"));
    }

    @Test
    public void rendererEscapesLabelsAndPrompt() {
        String q = IoRenderer.questionHtml("x.png", Arrays.asList(new double[]{0.1, 0.1, 0.1, 0.1}), "<script>x</script>");
        String a = IoRenderer.answerHtml(
                "x.png", Arrays.asList(new double[]{0.1, 0.1, 0.1, 0.1}),
                Arrays.asList("<b>resposta</b>"));
        assertFalse(q.contains("<script>"));
        assertTrue(q.contains("&lt;script&gt;"));
        assertTrue(a.contains("&lt;b&gt;resposta&lt;/b&gt;"));
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
