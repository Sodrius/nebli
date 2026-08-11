package com.sodrius.nebli.companion;

import java.util.Collections;
import java.util.List;
import java.util.function.Supplier;

/** Keeps one unsupported AnkiDroid query from aborting a complete lesson. */
public final class ProviderSearchPolicy {
    private ProviderSearchPolicy() {}

    public static <T> List<T> unresolvedOnProviderFailure(Supplier<List<T>> query) {
        try {
            List<T> found = query.get();
            return found == null ? Collections.emptyList() : found;
        } catch (RuntimeException providerFailure) {
            return Collections.emptyList();
        }
    }
}
