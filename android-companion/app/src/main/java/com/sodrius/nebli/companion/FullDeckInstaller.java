package com.sodrius.nebli.companion;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.util.Base64;

import androidx.core.content.FileProvider;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.File;
import java.io.FileOutputStream;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** Installs a complete Nebli lesson: AnKing copies + authored cards + IO. */
public final class FullDeckInstaller {
    public static final String SCHEMA = "nebli-ankidroid-deck-v3";
    private static final Pattern CLOZE_TARGET = Pattern.compile("\\{\\{c(\\d+)::([^}:]+)", Pattern.CASE_INSENSITIVE);

    private final Context context;
    private final AnkiBridge anki;

    public FullDeckInstaller(Context context) {
        this.context = context;
        this.anki = new AnkiBridge(context);
    }

    public JSONObject install(JSONObject manifest) throws Exception {
        validateManifest(manifest);
        String slug = manifest.getString("lesson_slug");
        String rootDeck = manifest.getString("target_deck");
        long rootDid = anki.ensureDeck(rootDeck);
        String optionalDeck = rootDeck + "::Optional";
        long optionalDid = hasOptional(manifest.getJSONArray("cards")) ? anki.ensureDeck(optionalDeck) : -1L;

        List<Plan> plans = planAll(manifest);
        if (plans.size() != manifest.getInt("expected_card_count")) {
            throw new IllegalStateException("planned count != expected_card_count");
        }

        Set<String> neededMedia = new HashSet<>();
        for (Plan p : plans) if (p.mediaKey != null) neededMedia.add(p.mediaKey);
        Map<String, String> mediaNames = uploadMedia(manifest.optJSONArray("media"), neededMedia);

        JSONArray cardReceipts = new JSONArray();
        JSONArray errors = new JSONArray();
        List<Long> createdThisRun = new ArrayList<>();
        int installed = 0, skipped = 0, authored = 0, io = 0, copied = 0;

        try {
            for (Plan p : plans) {
                long did = "optional".equalsIgnoreCase(p.card.optString("tier")) ? optionalDid : rootDid;
                CardInstallResult r = installOne(slug, p, did, mediaNames, createdThisRun);
                cardReceipts.put(r.receipt);
                if (!r.ok) {
                    errors.put(p.cardKey + ": " + r.receipt.optJSONArray("failures"));
                    throw new IllegalStateException("card gate failed: " + p.cardKey);
                }
                installed++;
                skipped += r.skipped ? 1 : 0;
                if ("anking".equals(r.actualSource)) copied++;
                else if ("io".equals(r.actualSource)) io++;
                else authored++;
            }
        } catch (Exception e) {
            for (int i = createdThisRun.size() - 1; i >= 0; i--) {
                try { anki.deleteOwnNote(createdThisRun.get(i)); } catch (Exception ignored) {}
            }
            JSONObject receipt = baseReceipt(manifest, rootDeck);
            receipt.put("ok", false);
            receipt.put("rolled_back_new_notes", createdThisRun.size());
            receipt.put("cards", cardReceipts);
            receipt.put("errors", errors);
            receipt.put("fatal_error", e.toString());
            return receipt;
        }

        anki.selectDeck(rootDid);
        JSONObject receipt = baseReceipt(manifest, rootDeck);
        receipt.put("ok", installed == manifest.getInt("expected_card_count"));
        receipt.put("expected_card_count", manifest.getInt("expected_card_count"));
        receipt.put("installed_card_count", installed);
        receipt.put("idempotent_skips", skipped);
        receipt.put("anking_cards", copied);
        receipt.put("authored_cards", authored);
        receipt.put("io_cards", io);
        receipt.put("cards", cardReceipts);
        receipt.put("errors", errors);
        receipt.put("selected_deck", rootDeck);
        return receipt;
    }

    private List<Plan> planAll(JSONObject manifest) throws Exception {
        JSONArray cards = manifest.getJSONArray("cards");
        List<Plan> out = new ArrayList<>();
        JSONObject search = manifest.optJSONObject("search");
        for (int i = 0; i < cards.length(); i++) {
            JSONObject card = cards.getJSONObject(i);
            String source = card.getString("source").toLowerCase(Locale.ROOT);
            Plan p;
            if ("anking".equals(source)) {
                p = resolveAnking(card, search);
                if (p == null) {
                    JSONObject fallback = card.optJSONObject("fallback");
                    if (fallback == null) throw new IllegalStateException("AnKing unresolved sem fallback: " + card.optString("card_key"));
                    fallback = inheritIdentity(card, fallback);
                    p = planLocal(fallback);
                    p.resolutionStatus = "fallback_after_anking_unresolved";
                }
            } else {
                p = planLocal(card);
            }
            out.add(p);
        }
        return out;
    }

    private Plan planLocal(JSONObject card) throws Exception {
        String source = card.getString("source").toLowerCase(Locale.ROOT);
        Plan p = new Plan(card);
        p.actualSource = source;
        if ("authored".equals(source)) {
            List<String> failures = CardRules.validateAuthoredCloze(
                    card.optString("text"), card.optString("extra"),
                    card.optString("front_language", "en"), card.optString("extra_language", "pt-BR"),
                    card.optBoolean("atomic", false), card.optBoolean("relevant", false),
                    card.optString("three_word_cloze_reason", "")
            );
            if (!failures.isEmpty()) throw new IllegalArgumentException(p.cardKey + " authored gate: " + failures);
            p.resolutionStatus = "authored";
        } else if ("io".equals(source)) {
            double[][] boxes = boxes(card.getJSONArray("masks"));
            List<String> failures = CardRules.validateIo(
                    card.optString("mode"), boxes.length,
                    card.optBoolean("masks_labels_not_structures", false),
                    card.optBoolean("question_preview_validated", false),
                    card.optBoolean("answer_preview_validated", false),
                    card.optBoolean("visual_ok", false),
                    card.optBoolean("real_source", false),
                    card.optBoolean("answer_leak", true),
                    card.optBoolean("coherent_set", boxes.length == 1),
                    boxes
            );
            if (!failures.isEmpty()) throw new IllegalArgumentException(p.cardKey + " IO gate: " + failures);
            p.mediaKey = card.getString("media_key");
            p.resolutionStatus = "io";
        } else {
            throw new IllegalArgumentException("source v3 não suportado: " + source);
        }
        return p;
    }

    private Plan resolveAnking(JSONObject card, JSONObject searchCfg) throws Exception {
        String query = card.getString("query").trim();
        JSONArray aliasesArr = card.optJSONArray("aliases");
        List<String> queries = new ArrayList<>();
        queries.add(query);
        if (aliasesArr != null) for (int i = 0; i < aliasesArr.length(); i++) {
            String a = aliasesArr.optString(i).trim();
            if (!a.isEmpty()) queries.add(a);
        }

        double minScore = searchCfg == null ? 0.82 : searchCfg.optDouble("min_score", 0.82);
        double minMargin = searchCfg == null ? 0.06 : searchCfg.optDouble("min_margin", 0.06);
        int maxCandidates = searchCfg == null ? 80 : searchCfg.optInt("max_candidates", 80);
        boolean requireMarker = searchCfg == null || searchCfg.optBoolean("require_anking_marker", true);

        Map<Long, Candidate> candidates = new LinkedHashMap<>();
        for (String q : queries) {
            for (AnkiBridge.NoteSnapshot n : anki.searchNotes(q, maxCandidates, true)) {
                boolean ankingLike = Ranker.looksAnKing(n.tags);
                if (requireMarker && !ankingLike) continue;
                Candidate c = candidates.computeIfAbsent(n.nid, ignored -> new Candidate(n));
                double s = Ranker.score(q, n.fields, n.tags, ankingLike);
                boolean exact = !Ranker.normalize(q).isEmpty() && Ranker.normalize(n.fields).contains(Ranker.normalize(q));
                if (s > c.score) { c.score = s; c.exact = exact; c.matchedQuery = q; }
            }
        }
        if (candidates.isEmpty()) return null;
        List<Candidate> ranked = new ArrayList<>(candidates.values());
        ranked.sort(Comparator.comparingDouble((Candidate c) -> c.score).reversed());
        Candidate best = ranked.get(0);
        double second = ranked.size() > 1 ? ranked.get(1).score : 0.0;
        if (!Ranker.confident(best.score, second, best.exact, minScore, minMargin)) return null;

        Integer ord = inferOrdinal(best.note, queries, minScore, minMargin);
        if (ord == null) return null;
        if (card.optBoolean("requires_visual", false) && !cardQuestionHasImage(best.note.nid, ord)) return null;

        Plan p = new Plan(card);
        p.actualSource = "anking";
        p.sourceNote = best.note;
        p.selectedOrd = ord;
        p.score = best.score;
        p.secondScore = second;
        p.exactPhrase = best.exact;
        p.resolutionStatus = "anking_resolved";
        return p;
    }

    private Integer inferOrdinal(AnkiBridge.NoteSnapshot note, List<String> queries, double minScore, double minMargin) {
        List<OrdinalScore> fromCloze = new ArrayList<>();
        Matcher m = CLOZE_TARGET.matcher(note.fields == null ? "" : note.fields);
        while (m.find()) {
            int ord = Math.max(0, Integer.parseInt(m.group(1)) - 1);
            String answer = m.group(2);
            double best = 0.0;
            boolean exact = false;
            for (String q : queries) {
                best = Math.max(best, Ranker.score(q, answer, "", false));
                exact |= !Ranker.normalize(q).isEmpty() && Ranker.normalize(answer).contains(Ranker.normalize(q));
            }
            fromCloze.add(new OrdinalScore(ord, best, exact));
        }
        Integer clozeOrd = chooseOrdinal(fromCloze, Math.min(minScore, 0.78), minMargin);
        if (clozeOrd != null) return clozeOrd;

        List<AnkiBridge.CardRow> rows = anki.cards(note.nid);
        if (rows.size() == 1) return rows.get(0).ord;
        List<OrdinalScore> rendered = new ArrayList<>();
        for (AnkiBridge.CardRow row : rows) {
            String render = row.question + " " + row.answer;
            double best = 0.0;
            boolean exact = false;
            for (String q : queries) {
                best = Math.max(best, Ranker.score(q, render, "", false));
                exact |= !Ranker.normalize(q).isEmpty() && Ranker.normalize(render).contains(Ranker.normalize(q));
            }
            rendered.add(new OrdinalScore(row.ord, best, exact));
        }
        return chooseOrdinal(rendered, Math.min(minScore, 0.78), minMargin);
    }

    private Integer chooseOrdinal(List<OrdinalScore> scores, double minScore, double minMargin) {
        if (scores.isEmpty()) return null;
        scores.sort(Comparator.comparingDouble((OrdinalScore s) -> s.score).reversed());
        OrdinalScore best = scores.get(0);
        double second = scores.size() > 1 ? scores.get(1).score : 0.0;
        return Ranker.confident(best.score, second, best.exact, minScore, minMargin) ? best.ord : null;
    }

    private boolean cardQuestionHasImage(long nid, int ord) {
        for (AnkiBridge.CardRow r : anki.cards(nid)) {
            if (r.ord == ord) {
                String q = r.question == null ? "" : r.question.toLowerCase(Locale.ROOT);
                return q.contains("<img") || q.contains("<svg") || q.contains("image-occlusion");
            }
        }
        return false;
    }

    private CardInstallResult installOne(
            String slug, Plan p, long targetDid, Map<String, String> mediaNames, List<Long> createdThisRun
    ) throws Exception {
        JSONObject card = p.card;
        String stableTag = "NEBLI::card::" + safe(slug) + "::" + safe(p.cardKey);
        String hash = card.optString("card_sha256", sha256(card.toString().getBytes(StandardCharsets.UTF_8)));
        String hashTag = "NEBLI::hash::" + hash.substring(0, Math.min(16, hash.length()));
        long existing = anki.findNoteByTag(stableTag);
        if (existing >= 0) {
            AnkiBridge.NoteSnapshot ex = anki.readNote(existing);
            if (ex != null && ex.tags != null && ex.tags.contains(hashTag)) {
                anki.moveCards(existing, targetDid);
                JSONObject rr = receiptBase(p, existing);
                rr.put("ok", true);
                rr.put("idempotent_skip", true);
                rr.put("failures", new JSONArray());
                return new CardInstallResult(true, true, p.actualSource, rr);
            }
            anki.deleteOwnNote(existing);
        }

        long nid;
        JSONObject rr = receiptBase(p, -1L);
        JSONArray failures = new JSONArray();

        if ("anking".equals(p.actualSource)) {
            AnkiBridge.NoteSnapshot before = anki.readNote(p.sourceNote.nid);
            if (before == null) throw new IllegalStateException("source note desapareceu: " + p.sourceNote.nid);
            Set<String> tags = mergeSourceTags(before.tags, stableTag, hashTag, "NEBLI::source::anking", "NEBLI::" + safe(slug));
            String[] fields = before.fields == null ? new String[]{""} : before.fields.split("\u001f", -1);
            nid = anki.insertNote(before.mid, fields, tags, targetDid);
            createdThisRun.add(nid);
            Set<Integer> active = new HashSet<>(); active.add(p.selectedOrd);
            int expectedSuspended = Math.max(0, anki.cards(nid).size() - 1);
            int suspended = anki.suspendExcept(nid, active);
            AnkiBridge.NoteSnapshot afterSource = anki.readNote(before.nid);
            AnkiBridge.NoteSnapshot copy = anki.readNote(nid);
            boolean sourceSafe = afterSource != null && afterSource.mid == before.mid
                    && eq(afterSource.fields, before.fields) && eq(afterSource.tags, before.tags);
            boolean sameType = copy != null && copy.mid == before.mid;
            boolean sameFields = copy != null && eq(copy.fields, before.fields);
            boolean siblingOk = expectedSuspended == 0 || suspended >= expectedSuspended;
            if (!sourceSafe) failures.put("source_safe");
            if (!sameType) failures.put("same_note_type");
            if (!sameFields) failures.put("same_fields");
            if (!siblingOk) failures.put("sibling_policy");
            rr.put("source_note_id", before.nid);
            rr.put("selected_ordinal", p.selectedOrd);
            rr.put("score", p.score);
            rr.put("second_score", p.secondScore);
            rr.put("exact_phrase", p.exactPhrase);
            rr.put("source_safe", sourceSafe);
            rr.put("same_note_type", sameType);
            rr.put("same_fields", sameFields);
            rr.put("media_ok", true);
            rr.put("sibling_policy_ok", siblingOk);
        } else if ("authored".equals(p.actualSource)) {
            String text = replaceMedia(card.optString("text"), mediaNames);
            String extra = replaceMedia(card.optString("extra"), mediaNames);
            long clozeMid = anki.findClozeModel();
            if (clozeMid >= 0) {
                String[] names = anki.modelFields(clozeMid);
                String[] values = AnkiBridge.fieldsForModel(names, text, extra);
                nid = anki.insertNote(clozeMid, values,
                        AnkiBridge.tags(stableTag, hashTag, "NEBLI::source::authored", "NEBLI::" + safe(slug)), targetDid);
                rr.put("authored_note_mode", "native_cloze");
            } else {
                long basicMid = anki.ensureBasicModel(targetDid);
                nid = anki.insertNote(basicMid,
                        new String[]{CardRules.clozeQuestion(text), CardRules.clozeAnswer(text), extra},
                        AnkiBridge.tags(stableTag, hashTag, "NEBLI::source::authored", "NEBLI::" + safe(slug)), targetDid);
                rr.put("authored_note_mode", "basic_cloze_fallback");
            }
            createdThisRun.add(nid);
            if (anki.cards(nid).size() != 1) failures.put("authored_generated_card_count_not_1");
            rr.put("cloze_words", CardRules.clozeWordCount(text));
            rr.put("media_ok", true);
        } else if ("io".equals(p.actualSource)) {
            String image = mediaNames.get(p.mediaKey);
            if (image == null) throw new IllegalStateException("mídia IO não instalada: " + p.mediaKey);
            List<double[]> boxList = boxList(card.getJSONArray("masks"));
            List<String> answers = stringList(card.optJSONArray("answers"));
            String question = IoRenderer.questionHtml(image, boxList, card.optString("prompt", "Identify the masked labels."));
            String answer = IoRenderer.answerHtml(image, answers, card.optString("source_credit", ""));
            long ioMid = anki.ensureIoModel(targetDid);
            nid = anki.insertNote(ioMid,
                    new String[]{question, answer, card.optString("extra"), card.optString("source_credit")},
                    AnkiBridge.tags(stableTag, hashTag, "NEBLI::source::io", "NEBLI::" + safe(slug)), targetDid);
            createdThisRun.add(nid);
            List<AnkiBridge.CardRow> rows = anki.cards(nid);
            boolean renderOk = rows.size() == 1 && rows.get(0).question.contains("nebli-io-mask")
                    && rows.get(0).question.contains(image) && rows.get(0).answer.contains(image);
            if (!renderOk) failures.put("io_runtime_render");
            rr.put("visual_ok", renderOk);
            rr.put("media_ok", true);
            rr.put("mask_count", boxList.size());
        } else {
            throw new IllegalStateException("actual source desconhecida: " + p.actualSource);
        }

        rr.put("note_id", nid);
        rr.put("idempotent_skip", false);
        rr.put("failures", failures);
        rr.put("ok", failures.length() == 0);
        return new CardInstallResult(failures.length() == 0, false, p.actualSource, rr);
    }

    private Map<String, String> uploadMedia(JSONArray media, Set<String> needed) throws Exception {
        Map<String, String> out = new HashMap<>();
        if (needed.isEmpty()) return out;
        if (media == null) throw new IllegalArgumentException("manifesto requer mídia mas media[] está ausente");
        Map<String, JSONObject> byKey = new HashMap<>();
        for (int i = 0; i < media.length(); i++) {
            JSONObject m = media.getJSONObject(i);
            byKey.put(m.getString("key"), m);
        }
        File dir = new File(context.getCacheDir(), "nebli-media");
        if (!dir.exists() && !dir.mkdirs()) throw new IllegalStateException("não foi possível criar cache de mídia");
        for (String key : needed) {
            JSONObject m = byKey.get(key);
            if (m == null) throw new IllegalArgumentException("media key ausente: " + key);
            byte[] bytes = Base64.decode(m.getString("data_base64"), Base64.DEFAULT);
            String expectedSha = m.optString("sha256", "");
            if (!expectedSha.isBlank() && !expectedSha.equalsIgnoreCase(sha256(bytes))) {
                throw new IllegalArgumentException("hash de mídia inválido: " + key);
            }
            String filename = safeFilename(m.optString("filename", key + ".bin"));
            File f = new File(dir, filename);
            try (FileOutputStream fos = new FileOutputStream(f)) { fos.write(bytes); }
            Uri uri = FileProvider.getUriForFile(context, context.getPackageName() + ".files", f);
            context.grantUriPermission(AnkiBridge.ANKI_PACKAGE, uri, Intent.FLAG_GRANT_READ_URI_PERMISSION);
            try {
                String actual = anki.addMedia(uri, stripExtension(filename));
                out.put(key, actual);
            } finally {
                context.revokeUriPermission(uri, Intent.FLAG_GRANT_READ_URI_PERMISSION);
            }
        }
        return out;
    }

    private void validateManifest(JSONObject m) throws Exception {
        if (!SCHEMA.equals(m.optString("schema"))) throw new IllegalArgumentException("schema incompatível: " + m.optString("schema"));
        String deck = m.getString("target_deck");
        if (!deck.startsWith("NEBLI::")) throw new SecurityException("target_deck deve começar por NEBLI::");
        if (m.optBoolean("mutate_source", true)) throw new SecurityException("manifesto tenta mutar fonte");
        JSONArray cards = m.getJSONArray("cards");
        int expected = m.getInt("expected_card_count");
        if (expected <= 0 || cards.length() != expected) throw new IllegalArgumentException("expected_card_count deve ser o número real de cards");
        Set<String> keys = new HashSet<>();
        for (int i = 0; i < cards.length(); i++) {
            JSONObject c = cards.getJSONObject(i);
            String key = c.getString("card_key");
            if (!keys.add(key)) throw new IllegalArgumentException("card_key duplicado: " + key);
            if (c.optString("concept_id").isBlank()) throw new IllegalArgumentException("concept_id ausente: " + key);
            if (!c.optBoolean("atomic", false)) throw new IllegalArgumentException("card não atômico: " + key);
            if (!c.optBoolean("relevant", false)) throw new IllegalArgumentException("card irrelevante: " + key);
        }
    }

    public boolean shouldOpenAnki(JSONObject manifest, JSONObject receipt) {
        return receipt.optBoolean("ok", false) && manifest.optBoolean("open_ankidroid_after_install", true);
    }

    private JSONObject baseReceipt(JSONObject manifest, String targetDeck) throws Exception {
        JSONObject r = new JSONObject();
        r.put("schema", "nebli-install-receipt-v3");
        r.put("manifest_schema", manifest.getString("schema"));
        r.put("lesson_slug", manifest.getString("lesson_slug"));
        r.put("target_deck", targetDeck);
        r.put("manifest_sha256", manifest.optString("manifest_sha256", ""));
        r.put("timestamp", Instant.now().toString());
        return r;
    }

    private JSONObject receiptBase(Plan p, long nid) throws Exception {
        JSONObject r = new JSONObject();
        r.put("card_key", p.cardKey);
        r.put("concept_id", p.card.optString("concept_id"));
        r.put("planned_source", p.card.optString("source"));
        r.put("actual_source", p.actualSource);
        r.put("resolution_status", p.resolutionStatus);
        r.put("atomic", p.card.optBoolean("atomic", false));
        r.put("relevant", p.card.optBoolean("relevant", false));
        if (nid >= 0) r.put("note_id", nid);
        return r;
    }

    private static JSONObject inheritIdentity(JSONObject parent, JSONObject fallback) throws Exception {
        JSONObject f = new JSONObject(fallback.toString());
        f.put("card_key", parent.getString("card_key"));
        f.put("concept_id", parent.getString("concept_id"));
        f.put("tier", parent.optString("tier", "nucleo"));
        f.put("atomic", parent.optBoolean("atomic", false));
        f.put("relevant", parent.optBoolean("relevant", false));
        if (!f.has("card_sha256")) f.put("card_sha256", parent.optString("card_sha256", ""));
        return f;
    }

    private static boolean hasOptional(JSONArray cards) {
        for (int i = 0; i < cards.length(); i++) if ("optional".equalsIgnoreCase(cards.optJSONObject(i).optString("tier"))) return true;
        return false;
    }

    private static double[][] boxes(JSONArray masks) throws Exception {
        double[][] out = new double[masks.length()][4];
        for (int i = 0; i < masks.length(); i++) {
            JSONObject b = masks.getJSONObject(i);
            out[i][0] = b.getDouble("x"); out[i][1] = b.getDouble("y");
            out[i][2] = b.getDouble("w"); out[i][3] = b.getDouble("h");
        }
        return out;
    }

    private static List<double[]> boxList(JSONArray masks) throws Exception {
        List<double[]> out = new ArrayList<>();
        for (double[] b : boxes(masks)) out.add(b);
        return out;
    }

    private static List<String> stringList(JSONArray a) {
        List<String> out = new ArrayList<>();
        if (a != null) for (int i = 0; i < a.length(); i++) out.add(a.optString(i));
        return out;
    }

    private static Set<String> mergeSourceTags(String source, String... extra) {
        Set<String> out = new HashSet<>();
        if (source != null) for (String t : source.trim().split("\\s+")) if (!t.isBlank()) out.add(t);
        for (String t : extra) if (t != null && !t.isBlank()) out.add(t.replace(' ', '_'));
        return out;
    }

    private static String replaceMedia(String s, Map<String, String> names) {
        String out = s == null ? "" : s;
        for (Map.Entry<String, String> e : names.entrySet()) out = out.replace("nebli-media://" + e.getKey(), e.getValue());
        return out;
    }

    private static String safe(String s) { return s.replaceAll("[^A-Za-z0-9_-]", "_"); }
    private static String safeFilename(String s) { return s.replaceAll("[^A-Za-z0-9._-]", "_"); }
    private static String stripExtension(String s) { int i = s.lastIndexOf('.'); return i > 0 ? s.substring(0, i) : s; }
    private static boolean eq(String a, String b) { return a == null ? b == null : a.equals(b); }

    private static String sha256(byte[] bytes) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] d = md.digest(bytes);
        StringBuilder sb = new StringBuilder();
        for (byte b : d) sb.append(String.format(Locale.ROOT, "%02x", b));
        return sb.toString();
    }

    private static final class Candidate {
        final AnkiBridge.NoteSnapshot note;
        double score = 0.0;
        boolean exact = false;
        String matchedQuery = "";
        Candidate(AnkiBridge.NoteSnapshot note) { this.note = note; }
    }

    private static final class OrdinalScore {
        final int ord; final double score; final boolean exact;
        OrdinalScore(int ord, double score, boolean exact) { this.ord = ord; this.score = score; this.exact = exact; }
    }

    private static final class Plan {
        final JSONObject card;
        final String cardKey;
        String actualSource;
        String resolutionStatus;
        String mediaKey;
        AnkiBridge.NoteSnapshot sourceNote;
        int selectedOrd = -1;
        double score = 0.0, secondScore = 0.0;
        boolean exactPhrase = false;
        Plan(JSONObject card) throws Exception { this.card = card; this.cardKey = card.getString("card_key"); }
    }

    private static final class CardInstallResult {
        final boolean ok, skipped; final String actualSource; final JSONObject receipt;
        CardInstallResult(boolean ok, boolean skipped, String actualSource, JSONObject receipt) {
            this.ok = ok; this.skipped = skipped; this.actualSource = actualSource; this.receipt = receipt;
        }
    }
}
