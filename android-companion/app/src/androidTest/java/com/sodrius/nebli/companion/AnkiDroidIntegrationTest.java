package com.sodrius.nebli.companion;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import android.content.Context;
import android.content.pm.PackageManager;
import androidx.test.core.app.ApplicationProvider;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.Test;
import org.junit.runner.RunWith;

/** Golden authored-only round trip against the official AnkiDroid provider. */
@RunWith(AndroidJUnit4.class)
public class AnkiDroidIntegrationTest {
    private static final String PERMISSION = "com.ichi2.anki.permission.READ_WRITE_DATABASE";
    private static final String HASH_A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    private static final String HASH_B = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb";
    private static final String HASH_C = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc";

    @Test public void installsUpdatesAndReexecutesWithoutDuplicates() throws Exception {
        Context context = ApplicationProvider.getApplicationContext();
        assertNotNull(context.getPackageManager().getPackageInfo(AnkiBridge.ANKI_PACKAGE, 0));
        assertEquals(PackageManager.PERMISSION_GRANTED, context.checkSelfPermission(PERMISSION));
        FullDeckInstaller installer = new FullDeckInstaller(context);
        JSONObject first = installer.install(manifest());
        assertTrue(first.toString(2), first.getBoolean("ok"));
        assertEquals(3, first.getInt("installed_card_count"));
        assertEquals(3, first.getInt("expected_card_count"));
        assertEquals(2, first.getInt("authored_cards"));
        assertEquals(1, first.getInt("io_cards"));
        assertEquals("NEBLI::UC99::P1::Fisiologia::Aula sintética", first.getString("selected_deck"));

        JSONObject second = installer.install(manifest());
        assertTrue(second.toString(2), second.getBoolean("ok"));
        assertEquals(3, second.getInt("idempotent_skips"));

        JSONObject updated = manifest();
        JSONObject card = updated.getJSONArray("cards").getJSONObject(0);
        card.put("text", "O aumento da pressão mantém a {{c1::válvula}} aberta.");
        card.put("content_sha256", HASH_C).put("card_sha256", HASH_C);
        JSONObject third = installer.install(updated);
        assertTrue(third.toString(2), third.getBoolean("ok"));
        assertEquals(2, third.getInt("idempotent_skips"));
    }

    @Test public void incompatibleManifestHasFriendlyMessage() throws Exception {
        JSONObject m = manifest().put("minimum_companion_version", "9.0.0").put("minimum_companion_version_code", 900);
        try { LessonActivity.requireCompatibleCompanion(m); }
        catch (FullDeckInstaller.CompanionVersionException e) {
            assertEquals("Este manifesto exige Nebli Companion 9.0.0 ou superior.", e.getMessage()); return;
        }
        throw new AssertionError("manifesto incompatível deveria ser bloqueado");
    }

    private static JSONObject manifest() throws Exception {
        JSONObject semantic = new JSONObject()
                .put("ambiguity", "A relação causal delimita uma resposta única.")
                .put("anti_induction", "A resposta exige conhecimento do mecanismo.")
                .put("duplicate_check", "Não existe recuperação funcional duplicada.");
        JSONObject authored = new JSONObject().put("card_key", "pressao-valvula").put("concept_id", "c1")
                .put("tier", "nucleo").put("source", "authored")
                .put("text", "O aumento da pressão abre a {{c1::válvula}} de saída.")
                .put("extra", "A abertura permite o avanço sem retorno.").put("e1_anchor", "a pressão abre a válvula")
                .put("retrieval_target", "Identificar a estrutura aberta pela pressão.").put("semantic_review", semantic)
                .put("content_sha256", HASH_A).put("card_sha256", HASH_A);
        JSONObject optional = new JSONObject(authored.toString()).put("card_key", "fluxo-opcional").put("concept_id", "c3")
                .put("tier", "optional").put("text", "O fluxo resultante é {{c1::unidirecional}}.")
                .put("content_sha256", HASH_B).put("card_sha256", HASH_B);
        JSONObject visual = new JSONObject().put("labels_masked_not_structures", true).put("question_preview", true)
                .put("answer_preview", true).put("legible", true).put("no_leak", true).put("didactic_value", true);
        JSONObject io = new JSONObject().put("card_key", "io-fluxo").put("concept_id", "c2").put("tier", "nucleo")
                .put("source", "io").put("mode", "hide_two_guess_two").put("prompt", "Identifique os dois rótulos ocultos.")
                .put("answers", new JSONArray().put("entrada").put("saída")).put("masks", new JSONArray()
                        .put(new JSONObject().put("x", .1).put("y", .2).put("w", .2).put("h", .1))
                        .put(new JSONObject().put("x", .65).put("y", .2).put("w", .2).put("h", .1)))
                .put("pair_rationale", "Entrada e saída formam um par funcional coerente.").put("media_key", "golden")
                .put("source_credit", "Esquema sintético público do teste Nebli.").put("cognitive_purpose", "Reconhecer a direção do fluxo.")
                .put("visual_review", visual).put("e1_anchor", "fluxo unidirecional").put("content_sha256", HASH_C).put("card_sha256", HASH_C);
        JSONObject media = new JSONObject().put("key", "golden").put("filename", "golden.png")
                .put("source_credit", "Esquema sintético público do teste Nebli.")
                .put("sha256", "d126d616641d42ac8b0a07ec302c9fa1ec049f86200931a0a60c8f3080284b77")
                .put("data_base64", "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Zl1sAAAAASUVORK5CYII=");
        return new JSONObject().put("schema", FullDeckInstaller.SCHEMA).put("pipeline_version", "e1-deck-v11")
                .put("minimum_companion_version", "0.8.0").put("minimum_companion_version_code", 13)
                .put("required_capabilities", new JSONArray().put("authored_cards")).put("card_source_mode", "authored_only")
                .put("lesson_slug", "ci-authored-only").put("deck_identity", new JSONObject().put("uc", "UC99").put("prova", "P1").put("componente", "Fisiologia").put("nome_curto", "Aula sintética"))
                .put("target_deck", "NEBLI::UC99::P1::Fisiologia::Aula sintética").put("mutate_source", false)
                .put("open_ankidroid_after_install", false).put("expected_card_count", 3).put("ordered_card_set_sha256", HASH_A)
                .put("release_gate", new JSONObject().put("schema", "nebli-e1-deck-release-v1").put("passed", true)
                        .put("nuclear_concept_count", 2).put("covered_nuclear_count", 2).put("e1_source_sha256", HASH_A).put("e1_pdf_sha256", HASH_B))
                .put("media", new JSONArray().put(media)).put("cards", new JSONArray().put(authored).put(io).put(optional));
    }
}
