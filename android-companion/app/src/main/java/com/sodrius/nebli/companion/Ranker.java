package com.sodrius.nebli.companion;

import java.text.Normalizer;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Locale;
import java.util.List;
import java.util.Set;

public final class Ranker {
    private static final Set<String> STOP = new HashSet<>(Arrays.asList(
            "the","a","an","and","or","of","to","in","on","for","with","is","are","be","by","from",
            "de","da","do","das","dos","e","ou","em","no","na","nos","nas","para","com","por","um","uma"
    ));

    private Ranker() {}

    public static String normalize(String s) {
        if (s == null) return "";
        String x = s.replace('\u001f', ' ')
                .replaceAll("<[^>]+>", " ")
                .replaceAll("\\{\\{c\\d+::", " ")
                // Android rejects bare closing braces in regexes even when
                // the desktop OpenJDK used by unit tests accepts them.
                .replaceAll("::[^}]+\\}\\}", " ")
                .replace("}}", " ")
                .replace("&nbsp;", " ");
        x = Normalizer.normalize(x, Normalizer.Form.NFD).replaceAll("\\p{M}+", "");
        x = x.toLowerCase(Locale.ROOT).replaceAll("[^a-z0-9]+", " ").replaceAll("\\s+", " ").trim();
        return x;
    }

    public static Set<String> tokens(String s) {
        Set<String> out = new HashSet<>();
        String n = normalize(s);
        if (n.isEmpty()) return out;
        for (String t : n.split(" ")) {
            if (t.length() >= 2 && !STOP.contains(t)) out.add(t);
        }
        return out;
    }

    public static double coverage(String query, String text) {
        Set<String> q = tokens(query);
        if (q.isEmpty()) return 0.0;
        Set<String> t = tokens(text);
        int hit = 0;
        for (String s : q) if (t.contains(s)) hit++;
        return (double) hit / (double) q.size();
    }

    public static double score(String query, String fields, String tags, boolean ankingLike) {
        String nq = normalize(query);
        String nt = normalize(fields);
        double cov = coverage(query, fields);
        boolean phrase = !nq.isEmpty() && nt.contains(nq);
        double s = 0.78 * cov + (phrase ? 0.18 : 0.0) + (ankingLike ? 0.04 : 0.0);
        if (s > 1.0) s = 1.0;
        return s;
    }

    /** Scores note context without conflating it with the short cloze answer. */
    public static double candidateScore(
            List<String> contextQueries,
            List<String> expectedAnswers,
            String fields,
            String tags,
            boolean ankingLike
    ) {
        double context = 0.0;
        for (String query : contextQueries) {
            context = Math.max(context, score(query, fields, tags, ankingLike));
        }
        double answer = 0.0;
        for (String expected : expectedAnswers) {
            // Here `fields` is the whole note, not one extracted cloze answer.
            // Do not dilute an exact expected answer just because the note has
            // a long explanatory context around it.
            double presence = coverage(expected, fields) >= 1.0
                    ? 1.0
                    : answerScore(expected, fields);
            answer = Math.max(answer, presence);
        }
        double combined = context + 0.08 * answer;
        return Math.min(1.0, combined);
    }

    /** Scores the requested retrieval against one cloze/sibling answer. */
    public static double answerScore(String expected, String actual) {
        String ne = normalize(expected);
        String na = normalize(actual);
        if (ne.isEmpty() || na.isEmpty()) return 0.0;
        if (ne.equals(na)) return 1.0;
        if (na.contains(ne) || ne.contains(na)) return 0.95;
        Set<String> e = tokens(expected);
        Set<String> a = tokens(actual);
        if (e.isEmpty() || a.isEmpty()) return 0.0;
        int hit = 0;
        for (String token : e) if (a.contains(token)) hit++;
        if (hit == 0) return 0.0;
        double precision = (double) hit / (double) a.size();
        double recall = (double) hit / (double) e.size();
        return 2.0 * precision * recall / (precision + recall);
    }

    public static boolean passesConstraints(String fields, List<String> mustContain, List<String> mustNotContain) {
        String normalized = normalize(fields);
        for (String required : mustContain) {
            if (!normalized.contains(normalize(required))) return false;
        }
        for (String forbidden : mustNotContain) {
            String value = normalize(forbidden);
            if (!value.isEmpty() && normalized.contains(value)) return false;
        }
        return true;
    }

    public static boolean confident(double best, double second, boolean exactPhrase, double minScore, double minMargin) {
        if (best < minScore) return false;
        if (second <= 0.0) return true;
        return best - second >= minMargin;
    }

    public static boolean looksAnKing(String tags) {
        String n = normalize(tags);
        return n.contains("anking") || n.contains("ak step") || n.contains("ak step1") || n.contains("ak step2") || n.contains("ak v12");
    }
}
