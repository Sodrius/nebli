package com.sodrius.nebli.companion;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.util.Base64;

import androidx.core.content.FileProvider;
import androidx.test.core.app.ApplicationProvider;
import androidx.test.ext.junit.runners.AndroidJUnit4;

import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.Test;
import org.junit.runner.RunWith;

import java.io.File;
import java.io.FileOutputStream;
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
    public void installsAllVisualRoutesThroughRealAnkiDroid() throws Exception {
        Context context = ApplicationProvider.getApplicationContext();
        assertNotNull(context.getPackageManager().getPackageInfo(AnkiBridge.ANKI_PACKAGE, 0));
        assertEquals(PackageManager.PERMISSION_GRANTED, context.checkSelfPermission(PERMISSION));

        AnkiBridge anki = new AnkiBridge(context);
        String sourceImage = addSourceImage(context, anki);
        String sourceDeck = "NEBLI::CI::AnKingSource";
        long sourceDid = anki.ensureDeck(sourceDeck);
        long basicMid = anki.ensureBasicModel(sourceDid);
        String sourceFront = "O lipopolissacarídeo bacteriano é reconhecido na membrana pelo TLR4 "
                + "<img src=\"" + sourceImage + "\">";
        long sourceNid = anki.insertNote(
                basicMid,
                new String[]{sourceFront, "O LPS bacteriano é o ligante.", ""},
                new HashSet<>(Arrays.asList("#AK_Step1_v12", "NEBLI_CI_SOURCE")),
                sourceDid
        );

        JSONObject manifest = manifest();
        JSONObject receipt;
        try {
            receipt = new FullDeckInstaller(context).install(manifest);
            assertTrue(receipt.toString(2), receipt.getBoolean("ok"));
            assertEquals(4, receipt.getInt("installed_card_count"));
            assertEquals(4, receipt.getInt("expected_card_count"));
            assertEquals(1, receipt.getInt("anking_cards"));
            assertEquals(2, receipt.getInt("authored_cards"));
            assertEquals(1, receipt.getInt("io_cards"));
            assertEquals(sourceFront, anki.readNote(sourceNid).fields.split("\\u001f", -1)[0]);

            JSONArray cards = receipt.getJSONArray("cards");
            for (int i = 0; i < cards.length(); i++) {
                JSONObject card = cards.getJSONObject(i);
                assertTrue(card.toString(2), card.getBoolean("media_ok"));
                long nid = card.getLong("note_id");
                assertEquals(1, anki.cards(nid).size());
                anki.deleteOwnNote(nid);
            }
        } finally {
            context.getContentResolver().delete(
                    Uri.withAppendedPath(AnkiBridge.NOTES, Long.toString(sourceNid)), null, null);
        }
    }

    private static JSONObject manifest() throws Exception {
        JSONObject fallback = withCueQuality(new JSONObject()
                .put("source", "authored")
                .put("text", "O TLR4 reconhece o {{c1::LPS}} bacteriano.")
                .put("extra", "O TLR4 reconhece o lipopolissacarídeo bacteriano.")
                .put("front_language", "pt-BR")
                .put("extra_language", "pt-BR"));

        JSONObject anking = new JSONObject()
                .put("card_key", "ci-anking")
                .put("concept_id", "ci-tlr4")
                .put("source", "anking")
                .put("validated_front", "O lipopolissacarídeo bacteriano é reconhecido na membrana pelo TLR4.")
                .put("front_language", "pt-BR")
                .put("portuguese_front_reviewed", true)
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
                .put("anking_required", true)
                .put("requires_visual", true)
                .put("fallback", fallback);

        JSONObject authoredAnkingVisual = withAnkingSearchAudit(withCueQuality(new JSONObject()
                .put("card_key", "ci-authored-anking-visual")
                .put("concept_id", "ci-prr")
                .put("source", "authored")
                .put("text", "A imunidade inata reconhece padrões por meio de {{c1::PRRs}}.")
                .put("extra", "PRRs reconhecem padrões moleculares conservados. "
                        + "<img src=\"nebli-anking-media://tlr4_visual\">")
                .put("front_language", "pt-BR")
                .put("extra_language", "pt-BR")
                .put("anking_media_refs", new JSONArray().put(new JSONObject()
                        .put("key", "tlr4_visual")
                        .put("query", "TLR4 lipopolysaccharide plasma membrane")
                        .put("search_queries", new JSONArray()
                                .put("TLR4 lipopolysaccharide plasma membrane")
                                .put("TLR4 lipopolysaccharide"))
                        .put("expected_answers", new JSONArray().put("TLR4"))
                        .put("source_filter", "deck:\"AnKing Step Deck\"")
                        .put("media_index", 0)
                        .put("cognitive_purpose", "Relacionar o PRR à localização e ao ligante bacteriano.")
                        .put("didactic_value_reviewed", true)))
                .put("atomic", true)
                .put("relevant", true)
                .put("tier", "nucleo")));

        JSONObject authoredSlideVisual = withAnkingSearchAudit(withCueQuality(new JSONObject()
                .put("card_key", "ci-authored-slide-visual")
                .put("concept_id", "ci-pamp")
                .put("source", "authored")
                .put("text", "Motivos microbianos conservados são chamados de {{c1::PAMPs}}.")
                .put("extra", "A imagem de aula ancora visualmente o padrão reconhecido. "
                        + "<img src=\"nebli-media://slide_visual\">")
                .put("front_language", "pt-BR")
                .put("extra_language", "pt-BR")
                .put("media_keys", new JSONArray().put("slide_visual"))
                .put("visual_evidence", new JSONArray().put(new JSONObject()
                        .put("key", "slide_visual")
                        .put("origin", "slide_or_external")
                        .put("source_credit", "Slide da aula — teste de integração")
                        .put("anking_visual_search_complete", true)
                        .put("anking_visual_rejection_reason", "Nenhuma imagem AnKing encontrada representava este esquema específico da aula.")
                        .put("cognitive_purpose", "Distinguir o padrão microbiano do receptor que o reconhece.")
                        .put("didactic_value_reviewed", true)))
                .put("atomic", true)
                .put("relevant", true)
                .put("tier", "nucleo")));

        JSONObject io = withAnkingSearchAudit(new JSONObject()
                .put("card_key", "ci-io-two-labels")
                .put("concept_id", "ci-io-prr-pamp")
                .put("source", "io")
                .put("mode", "hide_two_guess_two")
                .put("media_key", "slide_visual")
                .put("prompt", "Identifique os dois rótulos ocultos.")
                .put("prompt_language", "pt-BR")
                .put("portuguese_prompt_reviewed", true)
                .put("answers_language", "pt-BR")
                .put("portuguese_answers_reviewed", true)
                .put("answers", new JSONArray().put("PRR").put("PAMP"))
                .put("pair_rationale", "Os dois rótulos formam o par receptor-ligante recuperado em conjunto.")
                .put("masks", new JSONArray()
                        .put(box(0.08, 0.12, 0.22, 0.18))
                        .put(box(0.62, 0.58, 0.24, 0.18)))
                .put("masks_labels_not_structures", true)
                .put("question_preview_validated", true)
                .put("answer_preview_validated", true)
                .put("visual_ok", true)
                .put("real_source", true)
                .put("answer_leak", false)
                .put("coherent_set", true)
                .put("source_credit", "Slide da aula — teste de integração")
                .put("cognitive_purpose", "Recuperar em conjunto o receptor e seu padrão microbiano correspondente.")
                .put("didactic_value_reviewed", true)
                .put("atomic", true)
                .put("relevant", true)
                .put("tier", "nucleo"));

        JSONObject slideMedia = new JSONObject()
                .put("key", "slide_visual")
                .put("filename", "ci_slide_visual.png")
                .put("source_credit", "Slide da aula — teste de integração")
                .put("sha256", "d126d616641d42ac8b0a07ec302c9fa1ec049f86200931a0a60c8f3080284b77")
                .put("data_base64", PNG_BASE64);

        return new JSONObject()
                .put("schema", FullDeckInstaller.SCHEMA)
                .put("lesson_slug", "ci-ankidroid-roundtrip")
                .put("deck_identity", new JSONObject()
                        .put("uc", "UC99")
                        .put("prova", "P1")
                        .put("componente", "Integration")
                        .put("nome_curto", "Smoke"))
                .put("target_deck", "NEBLI::UC99::P1::Integration::Smoke")
                .put("release_gate", new JSONObject()
                        .put("schema", "nebli-e1-deck-release-v1")
                        .put("passed", true)
                        .put("nuclear_concept_count", 4)
                        .put("covered_nuclear_count", 4)
                        .put("e1_source_sha256", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                        .put("e1_pdf_sha256", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
                .put("mutate_source", false)
                .put("open_ankidroid_after_install", false)
                .put("expected_card_count", 4)
                .put("search", new JSONObject()
                        .put("min_score", 0.82)
                        .put("min_margin", 0.06)
                        .put("max_candidates", 20)
                        .put("source_filter_is_hint", true)
                        .put("require_anking_marker", true))
                .put("media", new JSONArray().put(slideMedia))
                .put("cards", new JSONArray()
                        .put(anking)
                        .put(authoredAnkingVisual)
                        .put(authoredSlideVisual)
                        .put(io));
    }

    private static JSONObject withAnkingSearchAudit(JSONObject card) throws Exception {
        return card
                .put("anking_search_complete", true)
                .put("anking_search_queries", new JSONArray()
                        .put("pattern recognition receptor innate immunity")
                        .put("PRR innate immune sensing")
                        .put("innate immunity conserved molecular patterns"))
                .put("anking_search_scope_expanded", true)
                .put("anking_siblings_reviewed", true)
                .put("anking_candidates_reviewed", 0)
                .put("anking_rejection_reason", "Busca AnKing ampla concluída; nenhum card cobria exatamente esta recuperação.");
    }

    private static JSONObject withCueQuality(JSONObject card) throws Exception {
        return card
                .put("authored_quality", new JSONObject()
                        .put("portuguese_reviewed", true))
                .put("cue_quality", new JSONObject()
                        .put("cloze_role", "rotulo_especifico")
                        .put("knowledge_required", true)
                        .put("grammar_only_solvable", false)
                        .put("lexical_leak", false)
                        .put("answer_visible_elsewhere", false)
                        .put("blind_review_passed", true)
                        .put("plausible_alternatives", new JSONArray())
                        .put("confounders_checked", new JSONArray())
                        .put("ambiguity_review", "A pista imunológica determina uma única resposta no contexto."));
    }

    private static JSONObject box(double x, double y, double w, double h) throws Exception {
        return new JSONObject().put("x", x).put("y", y).put("w", w).put("h", h);
    }

    private static String addSourceImage(Context context, AnkiBridge anki) throws Exception {
        File dir = new File(context.getCacheDir(), "nebli-media");
        assertTrue(dir.exists() || dir.mkdirs());
        File file = new File(dir, "ci_anking_visual.png");
        try (FileOutputStream out = new FileOutputStream(file)) {
            out.write(Base64.decode(PNG_BASE64, Base64.DEFAULT));
        }
        Uri uri = FileProvider.getUriForFile(context, context.getPackageName() + ".files", file);
        context.grantUriPermission(AnkiBridge.ANKI_PACKAGE, uri, Intent.FLAG_GRANT_READ_URI_PERMISSION);
        try {
            return anki.addMedia(uri, "ci_anking_visual");
        } finally {
            context.revokeUriPermission(uri, Intent.FLAG_GRANT_READ_URI_PERMISSION);
        }
    }

    private static final String PNG_BASE64 =
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Zl1sAAAAASUVORK5CYII=";
}
