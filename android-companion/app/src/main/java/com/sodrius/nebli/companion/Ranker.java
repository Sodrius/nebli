package com.sodrius.nebli.companion;

import java.text.Normalizer;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Locale;
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

    public static boolean confident(double best, double second, boolean exactPhrase, double minScore, double minMargin) {
        if (best < minScore) return false;
        if (best >= 0.96) return true;
        if (exactPhrase && best >= Math.max(0.88, minScore)) return true;
        return best - second >= minMargin;
    }

    public static boolean looksAnKing(String tags) {
        String n = normalize(tags);
        return n.contains("anking") || n.contains("ak step") || n.contains("ak step1") || n.contains("ak step2") || n.contains("ak v12");
    }
}
