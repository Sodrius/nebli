package com.sodrius.nebli.companion;

import java.util.LinkedHashSet;
import java.util.Locale;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** Deterministic extraction and validation of collection-local image references. */
public final class MediaRefs {
    private static final Pattern IMG = Pattern.compile(
            "<img\\b[^>]*?\\bsrc\\s*=\\s*(['\"])(.*?)\\1",
            Pattern.CASE_INSENSITIVE | Pattern.DOTALL);

    private MediaRefs() {}

    public static Set<String> images(String html) {
        Set<String> out = new LinkedHashSet<>();
        Matcher matcher = IMG.matcher(html == null ? "" : html);
        while (matcher.find()) {
            String value = decode(matcher.group(2).trim());
            String lower = value.toLowerCase(Locale.ROOT);
            if (value.isBlank() || lower.startsWith("http://") || lower.startsWith("https://")
                    || lower.startsWith("data:") || lower.startsWith("javascript:")) continue;
            out.add(value);
        }
        return out;
    }

    public static Set<String> images(AnkiBridge.CardRow row) {
        Set<String> out = images(row == null ? "" : row.question);
        if (row != null) out.addAll(images(row.answer));
        return out;
    }

    private static String decode(String value) {
        return value.replace("&amp;", "&").replace("&quot;", "\"")
                .replace("&#39;", "'").replace("%20", " ");
    }
}
