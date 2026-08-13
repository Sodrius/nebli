package com.sodrius.nebli.companion;

import java.text.Normalizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** Hard card-quality rules shared by runtime install gates and unit tests. */
public final class CardRules {
    private static final Set<String> CLOZE_ROLES = new HashSet<>(Arrays.asList(
            "mecanismo", "consequencia", "discriminador", "valor", "direcao", "rotulo_especifico"));
    private static final Set<String> ENGLISH_FUNCTION_WORDS = new HashSet<>(Arrays.asList(
            "the", "an", "is", "are", "was", "were", "by", "with", "when", "which",
            "that", "from", "into", "during", "because", "requires", "uses"));
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
            String clozeThreeWordReason,
            boolean portugueseReviewed,
            String clozeRole,
            boolean knowledgeRequired,
            boolean grammarOnlySolvable,
            boolean lexicalLeak,
            boolean answerVisibleElsewhere,
            boolean blindReviewPassed,
            int unresolvedPlausibleAlternatives,
            boolean ambiguityReviewed
    ) {
        List<String> failures = new ArrayList<>();
        if (!atomic) failures.add("not_atomic");
        if (!relevant) failures.add("not_relevant");
        if (text == null || text.isBlank()) {
            failures.add("empty_text");
            return failures;
        }
        if (!isPortugueseLanguage(frontLanguage)) failures.add("front_language_not_pt");
        if (looksEnglish(text)) failures.add("front_appears_english");
        if (!"pt-br".equalsIgnoreCase(extraLanguage) && !"pt".equalsIgnoreCase(extraLanguage)) {
            failures.add("extra_language_not_pt");
        }
        if (looksEnglish(extra)) failures.add("extra_appears_english");
        if (!portugueseReviewed) failures.add("portuguese_not_reviewed");
        if (!CLOZE_ROLES.contains(clozeRole == null ? "" : clozeRole.toLowerCase(Locale.ROOT))) {
            failures.add("invalid_cloze_role");
        }
        if (!knowledgeRequired) failures.add("knowledge_not_required");
        if (grammarOnlySolvable) failures.add("grammar_only_solvable");
        if (lexicalLeak) failures.add("lexical_leak");
        if (answerVisibleElsewhere) failures.add("answer_visible_elsewhere");
        if (!blindReviewPassed) failures.add("blind_review_not_passed");
        if (unresolvedPlausibleAlternatives != 0) failures.add("unresolved_plausible_alternatives");
        if (!ambiguityReviewed) failures.add("ambiguity_not_reviewed");

        Matcher m = clozePattern().matcher(text);
        int count = 0;
        int words = 0;
        while (m.find()) {
            count++;
            if (!"1".equals(m.group(1))) failures.add("authored_cloze_must_use_c1_only");
            words = Math.max(words, wordCount(m.group(2)));
        }
        if (count == 1 && answerAppearsInVisibleStem(text)) {
            failures.add("cloze_answer_visible_in_prompt");
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

    public static List<String> validatePortuguesePrompt(
            String prompt, String language, boolean portugueseReviewed
    ) {
        List<String> failures = new ArrayList<>();
        if (prompt == null || prompt.isBlank()) failures.add("empty_prompt");
        if (!isPortugueseLanguage(language)) failures.add("prompt_language_not_pt");
        if (looksEnglish(prompt)) failures.add("prompt_appears_english");
        if (!portugueseReviewed) failures.add("portuguese_prompt_not_reviewed");
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
        if (!"hide_two_guess_two".equals(mode)) failures.add("io_mode_must_be_hide_two_guess_two");
        if (maskCount < 1) failures.add("io_requires_mask");
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

    private static boolean isPortugueseLanguage(String language) {
        return "pt".equalsIgnoreCase(language) || "pt-br".equalsIgnoreCase(language);
    }

    private static String normalizedWords(String value) {
        String plain = value == null ? "" : value.replaceAll("<[^>]+>", " ");
        String normalized = Normalizer.normalize(plain, Normalizer.Form.NFD)
                .replaceAll("\\p{M}+", "")
                .toLowerCase(Locale.ROOT)
                .replaceAll("[^a-z0-9]+", " ")
                .trim();
        return normalized;
    }

    private static boolean looksEnglish(String value) {
        int markers = 0;
        for (String word : normalizedWords(value).split("\\s+")) {
            if (ENGLISH_FUNCTION_WORDS.contains(word)) markers++;
        }
        return markers >= 3;
    }

    private static boolean answerAppearsInVisibleStem(String text) {
        Matcher fresh = clozePattern().matcher(text == null ? "" : text);
        if (!fresh.find()) return false;
        String answer = normalizedWords(fresh.group(2));
        String stem = normalizedWords(fresh.replaceFirst(" "));
        return !answer.isBlank() && (" " + stem + " ").contains(" " + answer + " ");
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
