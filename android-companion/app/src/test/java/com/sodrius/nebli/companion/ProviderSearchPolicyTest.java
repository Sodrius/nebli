package com.sodrius.nebli.companion;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;

public class ProviderSearchPolicyTest {
    @Test
    public void preservesSuccessfulResults() {
        List<String> found = ProviderSearchPolicy.unresolvedOnProviderFailure(
                () -> Arrays.asList("a", "b"));
        assertEquals(Arrays.asList("a", "b"), found);
    }

    @Test
    public void providerFailureBecomesUnresolvedSearch() {
        List<String> found = ProviderSearchPolicy.unresolvedOnProviderFailure(
                () -> { throw new IllegalArgumentException("unsupported Anki query"); });
        assertTrue(found.isEmpty());
    }
}
