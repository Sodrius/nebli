package com.sodrius.nebli.companion;

import java.util.List;

/** Builds deterministic HTML overlays for Nebli Hide-Two/Guess-Two cards. */
public final class IoRenderer {
    private IoRenderer() {}

    public static String questionHtml(String imageFile, List<double[]> boxes, String prompt) {
        StringBuilder sb = new StringBuilder();
        if (prompt != null && !prompt.isBlank()) {
            sb.append("<div class=\"nebli-io-prompt\">").append(escape(prompt)).append("</div>");
        }
        sb.append("<div class=\"nebli-io-wrap\"><img class=\"nebli-io-img\" src=\"")
          .append(escapeAttr(imageFile)).append("\" />");
        for (double[] b : boxes) {
            sb.append("<span class=\"nebli-io-mask\" style=\"left:")
              .append(pct(b[0])).append("%;top:").append(pct(b[1]))
              .append("%;width:").append(pct(b[2])).append("%;height:").append(pct(b[3]))
              .append("%;\"></span>");
        }
        sb.append("</div>");
        return sb.toString();
    }

    public static String answerHtml(
            String imageFile, List<double[]> boxes, List<String> answers, String sourceCredit
    ) {
        StringBuilder sb = new StringBuilder();
        sb.append("<div class=\"nebli-io-wrap\"><img class=\"nebli-io-img\" src=\"")
          .append(escapeAttr(imageFile)).append("\" />");
        int count = Math.min(boxes == null ? 0 : boxes.size(), answers == null ? 0 : answers.size());
        for (int i = 0; i < count; i++) {
            double[] b = boxes.get(i);
            sb.append("<span class=\"nebli-io-answer-label\" style=\"left:")
              .append(pct(b[0])).append("%;top:").append(pct(b[1]))
              .append("%;width:").append(pct(b[2])).append("%;height:").append(pct(b[3]))
              .append("%;\">").append(escape(answers.get(i))).append("</span>");
        }
        sb.append("</div>");
        if (answers != null && !answers.isEmpty()) {
            sb.append("<div class=\"nebli-io-answers\">");
            for (String a : answers) sb.append("<div>").append(escape(a)).append("</div>");
            sb.append("</div>");
        }
        if (sourceCredit != null && !sourceCredit.isBlank()) {
            sb.append("<div class=\"nebli-source\">").append(escape(sourceCredit)).append("</div>");
        }
        return sb.toString();
    }

    public static String css() {
        return ".card{font-family:Arial,sans-serif;font-size:20px;text-align:left;color:#111;background:#fff;}"
                + ".nebli-io-prompt{margin:0 0 12px 0;font-weight:600;}"
                + ".nebli-io-wrap{position:relative;display:inline-block;max-width:100%;line-height:0;}"
                + ".nebli-io-img{display:block;max-width:100%;height:auto;}"
                + ".nebli-io-mask{position:absolute;display:block;background:#f4f4f4;border:2px solid #111;box-sizing:border-box;}"
                + ".nebli-io-answer-label{position:absolute;display:flex;align-items:center;justify-content:center;background:#fff;border:2px solid #16665f;box-sizing:border-box;color:#114f4a;font-size:clamp(10px,2.4vw,20px);font-weight:700;line-height:1.05;text-align:center;}"
                + ".nebli-io-answers{margin-top:12px;line-height:1.35;}"
                + ".nebli-extra{margin-top:14px;font-size:.88em;line-height:1.35;}"
                + ".nebli-source{margin-top:10px;font-size:.68em;opacity:.65;line-height:1.2;}";
    }

    private static String pct(double v) {
        return String.format(java.util.Locale.ROOT, "%.4f", v * 100.0);
    }

    private static String escape(String s) {
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;");
    }

    private static String escapeAttr(String s) { return escape(s); }
}
