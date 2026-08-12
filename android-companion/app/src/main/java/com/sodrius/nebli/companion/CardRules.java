package com.sodrius.nebli.companion;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** Hard card-quality rules shared by runtime install gates and unit tests. */
public final class CardRules {
    // Vocabulário aceito para o modo de Image Occlusion.
    //
    // `hide_two_guess_two` é o nome canônico desde o v9. `hide_all_guess_all` é
    // o nome anterior e continua aceito como alias: com o teto de duas máscaras
    // vigente, esconder todas e cobrar todas É esconder duas e cobrar duas — os
    // dois nomes descrevem exatamente o mesmo card.
    //
    // Manter o alias não é cosmético. Renomear um token do manifesto quebra
    // toda instalação do Companion que já esteja no aparelho, e o lote inteiro
    // morre no primeiro card IO com rollback. Um nome novo entra somando-se ao
    // antigo; o antigo só sai depois que o APK do aparelho for reinstalado.
    public static final Set<String> IO_MODES = Collections.unmodifiableSet(
            new LinkedHashSet<>(Arrays.asList("hide_two_guess_two", "hide_all_guess_all")));
    // Keep both closing braces escaped. OpenJDK accepts bare `}}`, but
    // Android's regex implementation can reject it during class
    // initialization and wrap PatternSyntaxException in
    // ExceptionInInitializerError. Compile lazily so a malformed pattern can
    // never make the entire Companion class unloadable.
    private static final String CLOZE_REGEX = "\\{\\{c(\\d+)::([^}:]+)(?:::[^}]*)?\\}\\}";

    private CardRules() {}

    public static List<String> validateAuthoredCloze(
            String text,
            String extra,
            String frontLanguage,
            String extraLanguage,
            boolean atomic,
            boolean relevant,
            String clozeThreeWordReason
    ) {
        List<String> failures = new ArrayList<>();
        if (!atomic) failures.add("not_atomic");
        if (!relevant) failures.add("not_relevant");
        if (text == null || text.isBlank()) {
            failures.add("empty_text");
            return failures;
        }
        if (!"en".equalsIgnoreCase(frontLanguage)) failures.add("front_language_not_en");
        if (!"pt-br".equalsIgnoreCase(extraLanguage) && !"pt".equalsIgnoreCase(extraLanguage)) {
            failures.add("extra_language_not_pt");
        }

        Matcher m = clozePattern().matcher(text);
        int count = 0;
        int words = 0;
        while (m.find()) {
            count++;
            if (!"1".equals(m.group(1))) failures.add("authored_cloze_must_use_c1_only");
            words = Math.max(words, wordCount(m.group(2)));
        }
        if (count != 1) failures.add("authored_cloze_count_must_be_1");
        if (words < 1) failures.add("empty_cloze_answer");
        if (words > 3) failures.add("cloze_answer_over_3_words");
        if (words == 3 && (clozeThreeWordReason == null || clozeThreeWordReason.isBlank())) {
            failures.add("three_word_cloze_requires_reason");
        }

        String normalized = text.replaceAll("<[^>]+>", " ").replaceAll("\\s+", " ").trim();
        if (normalized.length() > 360) failures.add("authored_front_too_long");
        if (looksLikeEnumeration(normalized)) failures.add("possible_multi_retrieval_enumeration");
        if (extra != null && plainWordCount(extra) > 100) failures.add("extra_too_long");
        return failures;
    }

    public static List<String> validateIo(
            String mode,
            int maskCount,
            boolean masksLabelsNotStructures,
            boolean questionPreviewValidated,
            boolean answerPreviewValidated,
            boolean visualOk,
            boolean realSource,
            boolean answerLeak,
            boolean coherentSet,
            double[][] boxes
    ) {
        List<String> failures = new ArrayList<>();
        if (!IO_MODES.contains(mode)) failures.add("io_mode_unsupported:" + mode);
        if (maskCount < 1) failures.add("io_requires_mask");
        // O teto vale para qualquer um dos nomes aceitos: é a regra, não o rótulo.
        if (maskCount > 2) failures.add("hide_two_guess_two_max_two_masks");
        if (maskCount > 1 && !coherentSet) failures.add("multi_mask_io_requires_coherent_set");
        if (!masksLabelsNotStructures) failures.add("io_must_mask_answer_label_not_visual_target");
        if (!questionPreviewValidated) failures.add("question_preview_not_validated");
        if (!answerPreviewValidated) failures.add("answer_preview_not_validated");
        if (!visualOk) failures.add("visual_not_ok");
        if (!realSource) failures.add("visual_source_not_real");
        if (answerLeak) failures.add("answer_leak");
        if (boxes == null || boxes.length != maskCount) {
            failures.add("mask_geometry_count_mismatch");
        } else {
            for (int i = 0; i < boxes.length; i++) {
                double[] b = boxes[i];
                if (b == null || b.length != 4) {
                    failures.add("mask_geometry_invalid:" + i);
                    continue;
                }
                double x = b[0], y = b[1], w = b[2], h = b[3];
                if (x < 0 || y < 0 || w <= 0 || h <= 0 || x + w > 1.000001 || y + h > 1.000001) {
                    failures.add("mask_out_of_bounds:" + i);
                }
            }
        }
        return failures;
    }

    public static int clozeWordCount(String text) {
        Matcher m = clozePattern().matcher(text == null ? "" : text);
        int words = 0;
        while (m.find()) words = Math.max(words, wordCount(m.group(2)));
        return words;
    }

    public static int clozeCount(String text) {
        Matcher m = clozePattern().matcher(text == null ? "" : text);
        int count = 0;
        while (m.find()) count++;
        return count;
    }

    /** Basic-note fallback when a collection has no cloze model. */
    public static String clozeQuestion(String text) {
        if (text == null) return "";
        Matcher m = clozePattern().matcher(text);
        if (!m.find()) return text;
        return m.replaceFirst("<span class=\"cloze\">[…]</span>");
    }

    /** Shows the original sentence with the answer emphasized. */
    public static String clozeAnswer(String text) {
        if (text == null) return "";
        Matcher m = clozePattern().matcher(text);
        if (!m.find()) return text;
        String answer = m.group(2);
        return m.replaceFirst("<span class=\"cloze\"><b>" + Matcher.quoteReplacement(answer) + "</b></span>");
    }

    private static int wordCount(String s) {
        if (s == null) return 0;
        String x = s.trim().replaceAll("\\s+", " ");
        return x.isBlank() ? 0 : x.split(" ").length;
    }

    private static Pattern clozePattern() {
        return Pattern.compile(CLOZE_REGEX, Pattern.CASE_INSENSITIVE);
    }

    private static int plainWordCount(String s) {
        if (s == null) return 0;
        String x = s.replaceAll("<[^>]+>", " ").replaceAll("\\s+", " ").trim();
        return x.isBlank() ? 0 : x.split(" ").length;
    }

    private static boolean looksLikeEnumeration(String s) {
        String n = s.toLowerCase(Locale.ROOT);
        int separators = 0;
        for (char c : n.toCharArray()) if (c == ';') separators++;
        if (separators >= 2) return true;
        return n.contains("1)") && n.contains("2)") || n.contains("(1)") && n.contains("(2)");
    }
}
