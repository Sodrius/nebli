package com.sodrius.nebli.companion;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import android.content.Context;
import android.content.pm.PackageManager;
import android.net.Uri;

import androidx.test.core.app.ApplicationProvider;
import androidx.test.ext.junit.runners.AndroidJUnit4;

import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.Test;
import org.junit.runner.RunWith;

import java.util.Arrays;
import java.util.HashSet;

/** Runs on Android with the official AnkiDroid APK and its real ContentProvider. */
@RunWith(AndroidJUnit4.class)
public class AnkiDroidIntegrationTest {
    private static final String PERMISSION = "com.ichi2.anki.permission.READ_WRITE_DATABASE";

    @Test
    public void regexesExecuteOnAndroidRuntime() {
        assertEquals("tlr4 recognizes lps", Ranker.normalize(
                "TLR4 recognizes {{c1::LPS::microbial ligand}}"));
        assertEquals(1, CardRules.clozeCount("TLR4 recognizes {{c1::LPS::microbial ligand}}."));
        assertTrue(CardRules.clozeAnswer(
                "TLR4 recognizes {{c1::LPS::microbial ligand}}.").contains("LPS"));
    }

    @Test
    public void canonicalDeckIdentityIsExact() throws Exception {
        JSONObject identity = new JSONObject()
                .put("uc", "UC03")
                .put("prova", "P1")
                .put("componente", "Imunologia")
                .put("nome_curto", "Reconhecimento inato");
        assertEquals(
                "NEBLI::UC03::P1::Imunologia::Reconhecimento inato",
                FullDeckInstaller.canonicalDeckName(identity));
    }

    @Test
    public void installsAnkingCopyAndAuthoredCardThroughRealAnkiDroid() throws Exception {
        Context context = ApplicationProvider.getApplicationContext();
        assertNotNull(context.getPackageManager().getPackageInfo(AnkiBridge.ANKI_PACKAGE, 0));
        assertEquals(PackageManager.PERMISSION_GRANTED, context.checkSelfPermission(PERMISSION));

        AnkiBridge anki = new AnkiBridge(context);
        String sourceDeck = "NEBLI::CI::AnKingSource";
        long sourceDid = anki.ensureDeck(sourceDeck);
        long basicMid = anki.ensureBasicModel(sourceDid);
        String sourceFront = "Bacterial lipopolysaccharide is sensed at the plasma membrane by TLR4";
        long sourceNid = anki.insertNote(
                basicMid,
                new String[]{sourceFront, "Bacterial LPS is the ligand.", ""},
                new HashSet<>(Arrays.asList("#AK_Step1_v12", "NEBLI_CI_SOURCE")),
                sourceDid
        );

        JSONObject manifest = manifest();
        JSONObject receipt;
        try {
            receipt = new FullDeckInstaller(context).install(manifest);
            assertTrue(receipt.toString(2), receipt.getBoolean("ok"));
            assertEquals(2, receipt.getInt("installed_card_count"));
            assertEquals(2, receipt.getInt("expected_card_count"));
            assertEquals(1, receipt.getInt("anking_cards"));
            assertEquals(1, receipt.getInt("authored_cards"));
            assertEquals(sourceFront, anki.readNote(sourceNid).fields.split("\\u001f", -1)[0]);

            JSONArray cards = receipt.getJSONArray("cards");
            for (int i = 0; i < cards.length(); i++) {
                long nid = cards.getJSONObject(i).getLong("note_id");
                assertEquals(1, anki.cards(nid).size());
                anki.deleteOwnNote(nid);
            }
        } finally {
            context.getContentResolver().delete(
                    Uri.withAppendedPath(AnkiBridge.NOTES, Long.toString(sourceNid)), null, null);
        }
    }

    private static JSONObject manifest() throws Exception {
        JSONObject fallback = new JSONObject()
                .put("source", "authored")
                .put("text", "TLR4 recognizes {{c1::LPS}}.")
                .put("extra", "O TLR4 reconhece o lipopolissacarídeo bacteriano.")
                .put("front_language", "en")
                .put("extra_language", "pt-BR");

        JSONObject anking = new JSONObject()
                .put("card_key", "ci-anking")
                .put("concept_id", "ci-tlr4")
                .put("source", "anking")
                .put("query", "TLR4 lipopolysaccharide plasma membrane")
                .put("search_queries", new JSONArray()
                        .put("TLR4 lipopolysaccharide plasma membrane")
                        .put("TLR4 lipopolysaccharide"))
                .put("expected_answers", new JSONArray().put("TLR4"))
                // Deliberately wrong deck name: for AnKing this is a hint,
                // and the marker-backed unscoped pass must still find it.
                .put("source_filter", "deck:\"AnKing Step Deck\"")
                .put("atomic", true)
                .put("relevant", true)
                .put("tier", "nucleo")
                .put("fallback", fallback);

        JSONObject authored = new JSONObject()
                .put("card_key", "ci-authored")
                .put("concept_id", "ci-prr")
                .put("source", "authored")
                .put("text", "Innate immune sensing uses {{c1::PRRs}}.")
                .put("extra", "PRRs reconhecem padrões moleculares conservados.")
                .put("front_language", "en")
                .put("extra_language", "pt-BR")
                .put("anking_search_complete", true)
                .put("anking_rejection_reason", "CI authored control has no exact source card")
                .put("atomic", true)
                .put("relevant", true)
                .put("tier", "nucleo");

        return new JSONObject()
                .put("schema", FullDeckInstaller.SCHEMA)
                .put("lesson_slug", "ci-ankidroid-roundtrip")
                .put("deck_identity", new JSONObject()
                        .put("uc", "UC99")
                        .put("prova", "P1")
                        .put("componente", "Integration")
                        .put("nome_curto", "Smoke"))
                .put("target_deck", "NEBLI::UC99::P1::Integration::Smoke")
                .put("mutate_source", false)
                .put("open_ankidroid_after_install", false)
                .put("expected_card_count", 2)
                .put("search", new JSONObject()
                        .put("min_score", 0.82)
                        .put("min_margin", 0.06)
                        .put("max_candidates", 20)
                        .put("source_filter_is_hint", true)
                        .put("require_anking_marker", true))
                .put("cards", new JSONArray().put(anking).put(authored));
    }
}
