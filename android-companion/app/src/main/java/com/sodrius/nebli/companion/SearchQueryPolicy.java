package com.sodrius.nebli.companion;

/** Memory and scope limits for local AnkiDroid searches. */
public final class SearchQueryPolicy {
    private static final int MAX_SCAN = 320;

    private SearchQueryPolicy() {}

    public static String compose(String sourceFilter, String query) {
        String filter = sourceFilter == null ? "" : sourceFilter.trim();
        String term = query == null ? "" : query.trim();
        if (filter.isEmpty()) return term;
        if (term.isEmpty()) return filter;
        return filter + " " + term;
    }

    public static int scanLimit(int candidateLimit) {
        int safe = Math.max(1, candidateLimit);
        long expanded = (long) safe * 4L;
        return (int) Math.min(MAX_SCAN, expanded);
    }
}
