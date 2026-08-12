package com.sodrius.nebli.companion;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.Test;

import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.HashSet;
import java.util.Locale;
import java.util.Scanner;
import java.util.Set;

/**
 * O manifesto que o gerador Python produz precisa passar no gate deste build.
 *
 * Em 2026-08-12 um deck de 52 cards morreu na instalação porque o modo de IO
 * tinha sido renomeado no repo e o APK do aparelho não conhecia o nome novo. Os
 * dois lados estavam internamente coerentes e mesmo assim discordavam — não
 * havia nenhum teste em que um artefato real do gerador encontrasse o gate real
 * do Companion.
 *
 * Este é esse teste. O arquivo `golden-manifest.json` é gerado por
 * `gerar_manifesto_ankidroid.py` a partir de
 * `flashcards/tests/fixtures/contrato-companion/deck-data.json`, e o teste
 * Python `test_contrato_companion.py` garante que ele continue igual ao que o
 * gerador produz hoje. Aqui ele é submetido a `CardRules` e ao preflight de
 * contrato, exatamente como na instalação.
 */
public class GoldenManifestContractTest {

    private JSONObject golden() throws Exception {
        try (InputStream in = getClass().getClassLoader()
                .getResourceAsStream("golden-manifest.json")) {
            assertNotNull("golden-manifest.json ausente dos test resources", in);
            try (Scanner scanner = new Scanner(in, StandardCharsets.UTF_8.name())) {
                return new JSONObject(scanner.useDelimiter("\\A").next());
            }
        }
    }

    @Test
    public void everyCardOfARealGeneratedManifestPassesThisBuildsGate() throws Exception {
        JSONObject manifest = golden();
        assertEquals(FullDeckInstaller.SCHEMA, manifest.getString("schema"));

        Set<String> embeddedMedia = new HashSet<>();
        JSONArray media = manifest.optJSONArray("media");
        for (int i = 0; media != null && i < media.length(); i++) {
            embeddedMedia.add(media.getJSONObject(i).getString("key"));
        }

        JSONArray cards = manifest.getJSONArray("cards");
        assertEquals(manifest.getInt("expected_card_count"), cards.length());
        int authored = 0, io = 0;
        for (int i = 0; i < cards.length(); i++) {
            JSONObject card = cards.getJSONObject(i);
            String key = card.getString("card_key");
            String source = card.getString("source").toLowerCase(Locale.ROOT);
            if ("authored".equals(source)) {
                authored++;
                assertEquals(key + " reprovado no gate autoral",
                        "[]",
                        CardRules.validateAuthoredCloze(
                                card.optString("text"), card.optString("extra"),
                                card.optString("front_language", "en"),
                                card.optString("extra_language", "pt-BR"),
                                card.optBoolean("atomic", false),
                                card.optBoolean("relevant", false),
                                card.optString("three_word_cloze_reason", "")).toString());
            } else if ("io".equals(source)) {
                io++;
                JSONArray masks = card.getJSONArray("masks");
                double[][] boxes = new double[masks.length()][4];
                for (int m = 0; m < masks.length(); m++) {
                    JSONObject b = masks.getJSONObject(m);
                    boxes[m] = new double[]{b.getDouble("x"), b.getDouble("y"),
                            b.getDouble("w"), b.getDouble("h")};
                }
                assertEquals(key + " reprovado no gate de IO",
                        "[]",
                        CardRules.validateIo(
                                card.optString("mode"), boxes.length,
                                card.optBoolean("masks_labels_not_structures", false),
                                card.optBoolean("question_preview_validated", false),
                                card.optBoolean("answer_preview_validated", false),
                                card.optBoolean("visual_ok", false),
                                card.optBoolean("real_source", false),
                                card.optBoolean("answer_leak", true),
                                card.optBoolean("coherent_set", boxes.length == 1),
                                boxes).toString());
                assertTrue(key + ": media_key não está embutida no manifesto",
                        embeddedMedia.contains(card.getString("media_key")));
            } else {
                fail(key + ": source não coberto por este teste: " + source);
            }
        }
        assertTrue("a fixture precisa exercitar autoral e IO", authored > 0 && io > 0);
    }

    @Test
    public void preflightAcceptsTheVocabularyTheGeneratorEmitted() throws Exception {
        JSONObject manifest = golden();
        JSONObject required = manifest.getJSONObject("companion_requirements");
        assertTrue("o gerador precisa declarar o vocabulário exigido",
                CardRules.IO_MODES.contains(required.getString("io_mode_token")));
        FullDeckInstaller.checkCompanionContract(manifest);
    }

    @Test
    public void preflightRefusesAVocabularyThisBuildDoesNotSpeak() throws Exception {
        JSONObject manifest = golden();
        manifest.getJSONObject("companion_requirements")
                .put("io_mode_token", "hide_nine_guess_nine");
        try {
            FullDeckInstaller.checkCompanionContract(manifest);
            fail("um manifesto que exige vocabulário desconhecido tem de parar antes de instalar");
        } catch (IllegalArgumentException expected) {
            assertTrue("a mensagem precisa dizer o que fazer",
                    expected.getMessage().contains("Reinstale o Companion"));
        }
    }
}
