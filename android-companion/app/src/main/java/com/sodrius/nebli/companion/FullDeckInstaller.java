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
import java.util.function.Consumer;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** Installs a complete Nebli lesson: local deck copies + authored cards + IO. */
public final class FullDeckInstaller {
    public static final String SCHEMA = "nebli-ankidroid-deck-v3";
    private static final Pattern CLOZE_TARGET = Pattern.compile("\\{\\{c(\\d+)::([^}:]+)", Pattern.CASE_INSENSITIVE);

    private final Context context;
    private final AnkiBridge anki;
    private final Consumer<String> progress;

    public FullDeckInstaller(Context context) {
        this(context, ignored -> {});
    }

    public FullDeckInstaller(Context context, Consumer<String> progress) {
        this.context = context;
        this.anki = new AnkiBridge(context);
        this.progress = progress == null ? ignored -> {} : progress;
    }

    public JSONObject install(JSONObject manifest) throws Exception {
        validateManifest(manifest);
        String slug = manifest.getString("lesson_slug");
        String rootDeck = manifest.getString("target_deck");
        String optionalDeck = rootDeck + "::Optional";

        // Planning is read-only. Finish it before creating decks so a malformed
        // manifest or provider search failure can never leave an empty deck.
        List<Plan> plans = planAll(manifest);
        if (plans.size() != manifest.getInt("expected_card_count")) {
            throw new IllegalStateException("planned count != expected_card_count");
        }

        long rootDid = anki.ensureDeck(rootDeck);
        long optionalDid = hasOptional(manifest.getJSONArray("cards")) ? anki.ensureDeck(optionalDeck) : -1L;

        Set<String> neededMedia = new HashSet<>();
        for (Plan p : plans) neededMedia.addAll(p.mediaKeys);
        Map<String, String> mediaNames = uploadMedia(manifest.optJSONArray("media"), neededMedia);

        JSONArray cardReceipts = new JSONArray();
        JSONArray errors = new JSONArray();
        List<Long> createdThisRun = new ArrayList<>();
        int installed = 0, skipped = 0, authored = 0, io = 0, anking = 0, external = 0;

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
                if ("anking".equals(r.actualSource)) anking++;
                else if ("external_deck".equals(r.actualSource)) external++;
                else if ("io".equals(r.actualSource)) io++;
                else authored++;
            }
        } catch (Throwable e) {
            if (e instanceof OutOfMemoryError) System.gc();
            for (int i = createdThisRun.size() - 1; i >= 0; i--) {
                try { anki.deleteOwnNote(createdThisRun.get(i)); } catch (Throwable ignored) {}
            }
            JSONObject receipt = baseReceipt(manifest, rootDeck);
            receipt.put("ok", false);
            receipt.put("rolled_back_new_notes", createdThisRun.size());
            receipt.put("cards", cardReceipts);
            receipt.put("errors", errors);
            receipt.put("fatal_error", e.getClass().getSimpleName() + ": " + e.getMessage());
            return receipt;
        }

        anki.selectDeck(rootDid);
        JSONObject receipt = baseReceipt(manifest, rootDeck);
        receipt.put("ok", installed == manifest.getInt("expected_card_count"));
        receipt.put("expected_card_count", manifest.getInt("expected_card_count"));
        receipt.put("installed_card_count", installed);
        receipt.put("idempotent_skips", skipped);
        receipt.put("anking_cards", anking);
        receipt.put("external_deck_cards", external);
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
            report("Buscando card " + (i + 1) + "/" + cards.length() + ": "
                    + card.optString("concept_id", card.optString("card_key")));
            String source = card.getString("source").toLowerCase(Locale.ROOT);
            Plan p;
            if ("anking".equals(source) || "external_deck".equals(source)) {
                boolean requireMarker = "anking".equals(source)
                        && (search == null || search.optBoolean("require_anking_marker", true));
                Resolution resolution = resolveLocalCopy(card, search, requireMarker, source);
                p = resolution.plan;
                if (p == null) {
                    if ("anking".equals(source) && card.optBoolean("anking_required", false)) {
                        throw new IllegalStateException("AnKing validado não resolvido: "
                                + card.optString("card_key") + " (" + resolution.reason + ")");
                    }
                    JSONObject fallback = card.optJSONObject("fallback");
                    if (fallback == null) {
                        throw new IllegalStateException(source + " unresolved sem fallback: " + card.optString("card_key"));
                    }
                    fallback = inheritIdentity(card, fallback);
                    p = planLocal(fallback, search);
                    p.resolutionStatus = "fallback_after_" + source + "_" + resolution.reason;
                    p.candidateCount = resolution.candidateCount;
                    p.attemptedQueries.addAll(resolution.attemptedQueries);
                }
            } else {
                p = planLocal(card, search);
            }
            out.add(p);
        }
        return out;
    }

    private Plan planLocal(JSONObject card, JSONObject search) throws Exception {
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
            p.mediaKeys.addAll(stringList(card.optJSONArray("media_keys")));
            resolveAnkingMediaRefs(p, search);
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
            p.mediaKeys.add(p.mediaKey);
            p.resolutionStatus = "io";
        } else {
            throw new IllegalArgumentException("source v3 não suportado: " + source);
        }
        return p;
    }

    private void resolveAnkingMediaRefs(Plan target, JSONObject search) throws Exception {
        JSONArray refs = target.card.optJSONArray("anking_media_refs");
        if (refs == null) return;
        for (int i = 0; i < refs.length(); i++) {
            JSONObject ref = new JSONObject(refs.getJSONObject(i).toString());
            String key = ref.getString("key");
            ref.put("card_key", target.cardKey + "::media::" + key);
            ref.put("concept_id", target.card.optString("concept_id"));
            ref.put("source", "anking");
            ref.put("requires_visual", true);
            Resolution resolution = resolveLocalCopy(ref, search, true, "anking");
            if (resolution.plan == null) {
                throw new IllegalStateException("imagem AnKing não resolvida: " + key + " (" + resolution.reason + ")");
            }
            AnkiBridge.CardRow row = cardRow(resolution.plan.sourceNote.nid, resolution.plan.selectedOrd);
            List<String> images = new ArrayList<>(MediaRefs.images(row));
            int index = ref.optInt("media_index", 0);
            if (index < 0 || index >= images.size()) {
                throw new IllegalStateException("media_index ambíguo/ausente para " + key + ": " + images.size());
            }
            target.localMediaNames.put(key, images.get(index));
            target.attemptedQueries.addAll(resolution.attemptedQueries);
        }
    }

    private Resolution resolveLocalCopy(
            JSONObject card,
            JSONObject searchCfg,
            boolean requireMarker,
            String sourceName
    ) throws Exception {
        String query = card.getString("query").trim();
        String sourceFilter = card.optString("source_filter", "").trim();
        List<String> queries = stringList(card.optJSONArray("search_queries"));
        if (queries.isEmpty()) {
            queries.add(query);
            for (String alias : stringList(card.optJSONArray("aliases"))) if (!queries.contains(alias)) queries.add(alias);
        }
        List<String> expectedAnswers = stringList(card.optJSONArray("expected_answers"));
        List<String> mustContain = stringList(card.optJSONArray("must_contain"));
        List<String> mustNotContain = stringList(card.optJSONArray("must_not_contain"));

        double minScore = searchCfg == null ? 0.82 : searchCfg.optDouble("min_score", 0.82);
        double minMargin = searchCfg == null ? 0.06 : searchCfg.optDouble("min_margin", 0.06);
        int maxCandidates = searchCfg == null ? 80 : searchCfg.optInt("max_candidates", 80);
        boolean sourceFilterIsHint = "anking".equals(sourceName)
                && (searchCfg == null || searchCfg.optBoolean("source_filter_is_hint", true));

        Map<Long, Candidate> candidates = new LinkedHashMap<>();
        List<String> discoveryQueries = new ArrayList<>(queries);
        for (String answer : expectedAnswers) if (!discoveryQueries.contains(answer)) discoveryQueries.add(answer);
        List<String> attemptedQueries = new ArrayList<>();
        for (String q : discoveryQueries) {
            collectCandidates(candidates, SearchQueryPolicy.compose(sourceFilter, q), attemptedQueries,
                    maxCandidates, requireMarker, mustContain, mustNotContain);
        }
        // The configured AnKing deck name is only a fast path. Retry without
        // it only when the scoped pass found nothing, still requiring the
        // positive AnKing marker before a note can enter the pool.
        if (sourceFilterIsHint && !sourceFilter.isEmpty() && candidates.isEmpty()) {
            for (String q : discoveryQueries) {
                collectCandidates(candidates, q, attemptedQueries,
                        maxCandidates, requireMarker, mustContain, mustNotContain);
            }
        }
        if (candidates.isEmpty()) return Resolution.unresolved("no_candidates_after_filters", 0, attemptedQueries);
        for (Candidate c : candidates.values()) {
            boolean ankingLike = Ranker.looksAnKing(c.note.tags);
            c.score = Ranker.candidateScore(queries, expectedAnswers, c.note.fields, c.note.tags, ankingLike);
            String normalizedFields = Ranker.normalize(c.note.fields);
            for (String q : queries) {
                if (!Ranker.normalize(q).isEmpty() && normalizedFields.contains(Ranker.normalize(q))) {
                    c.exact = true;
                    c.matchedQuery = q;
                    break;
                }
            }
        }
        List<Candidate> ranked = new ArrayList<>(candidates.values());
        ranked.sort(Comparator.comparingDouble((Candidate c) -> c.score).reversed());
        Candidate best = ranked.get(0);
        double second = ranked.size() > 1 ? ranked.get(1).score : 0.0;
        if (!Ranker.confident(best.score, second, best.exact, minScore, minMargin)) {
            return Resolution.unresolved("ambiguous_or_low_note_score", candidates.size(), attemptedQueries);
        }

        Integer ord = inferOrdinal(best.note, queries, expectedAnswers, minScore, minMargin);
        if (ord == null) return Resolution.unresolved("sibling_unresolved", candidates.size(), attemptedQueries);
        if (card.optBoolean("requires_visual", false) && !cardHasImage(best.note.nid, ord)) {
            return Resolution.unresolved("required_visual_missing", candidates.size(), attemptedQueries);
        }

        Plan p = new Plan(card);
        p.actualSource = sourceName;
        p.sourceNote = best.note;
        p.selectedOrd = ord;
        p.score = best.score;
        p.secondScore = second;
        p.exactPhrase = best.exact;
        p.resolutionStatus = sourceName + "_resolved";
        p.candidateCount = candidates.size();
        p.attemptedQueries.addAll(attemptedQueries);
        return Resolution.resolved(p, candidates.size(), attemptedQueries);
    }

    private void collectCandidates(
            Map<Long, Candidate> candidates,
            String ankiQuery,
            List<String> attemptedQueries,
            int maxCandidates,
            boolean requireMarker,
            List<String> mustContain,
            List<String> mustNotContain
    ) {
        if (!attemptedQueries.contains(ankiQuery)) attemptedQueries.add(ankiQuery);
        // One query can be unsupported by a provider version. Treat it as
        // unresolved so another query or the validated fallback can proceed.
        List<AnkiBridge.NoteSnapshot> found = ProviderSearchPolicy.unresolvedOnProviderFailure(
                () -> anki.searchNotes(ankiQuery, maxCandidates, true));
        for (AnkiBridge.NoteSnapshot n : found) {
            boolean ankingLike = Ranker.looksAnKing(n.tags);
            if (requireMarker && !ankingLike) continue;
            if (!Ranker.passesConstraints(n.fields, mustContain, mustNotContain)) continue;
            if (!candidates.containsKey(n.nid) && candidates.size() >= maxCandidates) continue;
            candidates.computeIfAbsent(n.nid, ignored -> new Candidate(n));
        }
    }

    private Integer inferOrdinal(
            AnkiBridge.NoteSnapshot note,
            List<String> contextQueries,
            List<String> expectedAnswers,
            double minScore,
            double minMargin
    ) {
        List<OrdinalScore> fromCloze = new ArrayList<>();
        Matcher m = CLOZE_TARGET.matcher(note.fields == null ? "" : note.fields);
        while (m.find()) {
            int ord = Math.max(0, Integer.parseInt(m.group(1)) - 1);
            String answer = m.group(2);
            double best = 0.0;
            boolean exact = false;
            List<String> targets = expectedAnswers.isEmpty() ? contextQueries : expectedAnswers;
            for (String target : targets) {
                double value = expectedAnswers.isEmpty()
                        ? Ranker.score(target, answer, "", false)
                        : Ranker.answerScore(target, answer);
                best = Math.max(best, value);
                exact |= Ranker.normalize(target).equals(Ranker.normalize(answer));
            }
            fromCloze.add(new OrdinalScore(ord, best, exact));
        }
        double ordinalMinScore = expectedAnswers.isEmpty() ? Math.min(minScore, 0.78) : 0.90;
        Integer clozeOrd = chooseOrdinal(fromCloze, ordinalMinScore, minMargin);
        if (clozeOrd != null) return clozeOrd;

        List<AnkiBridge.CardRow> rows = anki.cards(note.nid);
        if (rows.size() == 1) return rows.get(0).ord;
        List<OrdinalScore> rendered = new ArrayList<>();
        for (AnkiBridge.CardRow row : rows) {
            String render = row.question + " " + row.answer;
            double best = 0.0;
            boolean exact = false;
            for (String q : contextQueries) {
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

    private boolean cardHasImage(long nid, int ord) {
        for (AnkiBridge.CardRow r : anki.cards(nid)) {
            if (r.ord == ord) {
                return !MediaRefs.images(r).isEmpty()
                        || (r.question != null && r.question.toLowerCase(Locale.ROOT).contains("<svg"))
                        || (r.answer != null && r.answer.toLowerCase(Locale.ROOT).contains("<svg"));
            }
        }
        return false;
    }

    private CardInstallResult installOne(
            String slug, Plan p, long targetDid, Map<String, String> mediaNames, List<Long> createdThisRun
    ) throws Exception {
        JSONObject card = p.card;
        report("Instalando " + p.card.optString("concept_id", p.cardKey));
        String stableTag = "NEBLI::card::" + safe(slug) + "::" + safe(p.cardKey);
        String hash = card.optString("card_sha256", sha256(card.toString().getBytes(StandardCharsets.UTF_8)));
        String hashTag = "NEBLI::hash::" + hash.substring(0, Math.min(16, hash.length()));
        long existing = anki.findNoteByTag(stableTag);
        if (existing >= 0) {
            AnkiBridge.NoteSnapshot ex = anki.readNote(existing);
            if (ex != null && ex.tags != null && ex.tags.contains(hashTag)) {
                anki.moveCards(existing, targetDid);
                JSONObject rr = receiptBase(p, existing);
                boolean mediaOk = existingMediaOk(p, existing, mediaNames);
                rr.put("media_ok", mediaOk);
                rr.put("ok", mediaOk);
                rr.put("idempotent_skip", mediaOk);
                rr.put("failures", mediaOk ? new JSONArray() : new JSONArray().put("existing_media_not_rendered"));
                if (mediaOk) return new CardInstallResult(true, true, p.actualSource, rr);
            }
            anki.deleteOwnNote(existing);
        }

        long nid;
        JSONObject rr = receiptBase(p, -1L);
        JSONArray failures = new JSONArray();

        if ("anking".equals(p.actualSource) || "external_deck".equals(p.actualSource)) {
            AnkiBridge.NoteSnapshot before = anki.readNote(p.sourceNote.nid);
            if (before == null) throw new IllegalStateException("source note desapareceu: " + p.sourceNote.nid);
            Set<String> tags = mergeSourceTags(
                    before.tags, stableTag, hashTag, "NEBLI::source::" + p.actualSource, "NEBLI::" + safe(slug));
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
            Set<String> sourceMedia = MediaRefs.images(cardRow(before.nid, p.selectedOrd));
            Set<String> copiedMedia = MediaRefs.images(cardRow(nid, p.selectedOrd));
            boolean mediaOk = sourceMedia.equals(copiedMedia)
                    && (!card.optBoolean("requires_visual", false) || !sourceMedia.isEmpty());
            if (!sourceSafe) failures.put("source_safe");
            if (!sameType) failures.put("same_note_type");
            if (!sameFields) failures.put("same_fields");
            if (!siblingOk) failures.put("sibling_policy");
            if (!mediaOk) failures.put("media_refs_mismatch");
            rr.put("source_note_id", before.nid);
            rr.put("selected_ordinal", p.selectedOrd);
            rr.put("score", p.score);
            rr.put("second_score", p.secondScore);
            rr.put("exact_phrase", p.exactPhrase);
            rr.put("source_safe", sourceSafe);
            rr.put("same_note_type", sameType);
            rr.put("same_fields", sameFields);
            rr.put("source_media", new JSONArray(sourceMedia));
            rr.put("copied_media", new JSONArray(copiedMedia));
            rr.put("media_ok", mediaOk);
            rr.put("sibling_policy_ok", siblingOk);
        } else if ("authored".equals(p.actualSource)) {
            String text = replaceMedia(card.optString("text"), mediaNames, p.localMediaNames);
            String extra = replaceMedia(card.optString("extra"), mediaNames, p.localMediaNames);
            if (hasMediaPlaceholder(text) || hasMediaPlaceholder(extra)) {
                failures.put("authored_media_placeholder_unresolved");
            }
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
            List<AnkiBridge.CardRow> authoredRows = anki.cards(nid);
            if (authoredRows.size() != 1) failures.put("authored_generated_card_count_not_1");
            Set<String> renderedMedia = authoredRows.isEmpty()
                    ? new HashSet<>() : MediaRefs.images(authoredRows.get(0));
            Set<String> expectedMedia = new HashSet<>(p.localMediaNames.values());
            for (String mediaKey : p.mediaKeys) {
                String name = mediaNames.get(mediaKey);
                if (name != null) expectedMedia.add(name);
            }
            boolean authoredMediaOk = renderedMedia.containsAll(expectedMedia)
                    && !failures.toString().contains("authored_media_placeholder_unresolved");
            if (!authoredMediaOk) failures.put("authored_media_not_rendered");
            rr.put("cloze_words", CardRules.clozeWordCount(text));
            rr.put("media_count", p.mediaKeys.size());
            rr.put("expected_media", new JSONArray(expectedMedia));
            rr.put("rendered_media", new JSONArray(renderedMedia));
            rr.put("media_ok", authoredMediaOk);
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
                    && MediaRefs.images(rows.get(0)).contains(image)
                    && rows.get(0).answer.contains(image);
            if (!renderOk) failures.put("io_runtime_render");
            rr.put("visual_ok", renderOk);
            rr.put("media_ok", renderOk);
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
        JSONObject release = m.optJSONObject("release_gate");
        if (release == null
                || !"nebli-e1-deck-release-v1".equals(release.optString("schema"))
                || !release.optBoolean("passed", false)) {
            throw new IllegalArgumentException("manifesto sem release gate E1/deck aprovado");
        }
        int nuclear = release.optInt("nuclear_concept_count", 0);
        int coveredNuclear = release.optInt("covered_nuclear_count", -1);
        if (nuclear <= 0 || coveredNuclear != nuclear) {
            throw new IllegalArgumentException("cobertura nuclear incompleta no release gate");
        }
        if (release.optString("e1_source_sha256").length() != 64
                || release.optString("e1_pdf_sha256").length() != 64) {
            throw new IllegalArgumentException("release gate sem hashes válidos da E1");
        }
        String deck = m.getString("target_deck");
        String canonicalDeck = canonicalDeckName(m.getJSONObject("deck_identity"));
        if (!canonicalDeck.equals(deck)) {
            throw new SecurityException("target_deck não canônico; esperado " + canonicalDeck);
        }
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
            String source = c.optString("source");
            if (!"anking".equals(source) && !"external_deck".equals(source)
                    && !"authored".equals(source) && !"io".equals(source)) {
                throw new IllegalArgumentException("source v3 inválido: " + source);
            }
            if (("anking".equals(source) || "external_deck".equals(source))
                    && (c.optJSONArray("search_queries") == null || c.optJSONArray("search_queries").length() == 0)) {
                throw new IllegalArgumentException("card de fonte local sem search_queries: " + key);
            }
            if (("anking".equals(source) || "external_deck".equals(source))
                    && (c.optJSONArray("expected_answers") == null || c.optJSONArray("expected_answers").length() == 0)) {
                throw new IllegalArgumentException("card de fonte local sem expected_answers: " + key);
            }
            if ("anking".equals(source) && !c.optBoolean("anking_required", false)) {
                throw new IllegalArgumentException("AnKing curado sem anking_required=true: " + key);
            }
            if ("external_deck".equals(source) || "authored".equals(source) || "io".equals(source)) {
                validateAnkingSearchAudit(c, key);
            }
            if ("authored".equals(source)
                    && (!c.optBoolean("anking_search_complete", false)
                    || c.optString("anking_rejection_reason").isBlank())) {
                throw new IllegalArgumentException("autoral direto sem prova de busca AnKing: " + key);
            }
            if ("authored".equals(source)) validateAuthoredVisualContract(c, key);
            if ("io".equals(source)) validateIoContract(c, key);
        }
        validateMediaCatalog(m, cards);
    }

    private void validateAuthoredVisualContract(JSONObject card, String key) throws Exception {
        JSONArray embedded = card.optJSONArray("media_keys");
        JSONArray local = card.optJSONArray("anking_media_refs");
        int embeddedCount = embedded == null ? 0 : embedded.length();
        int localCount = local == null ? 0 : local.length();
        String html = card.optString("text") + " " + card.optString("extra");
        if (html.toLowerCase(Locale.ROOT).contains("<img") && embeddedCount + localCount == 0) {
            throw new IllegalArgumentException("imagem autoral sem origem declarada: " + key);
        }
        if (embeddedCount > 0) {
            JSONArray evidence = card.optJSONArray("visual_evidence");
            if (evidence == null || evidence.length() != embeddedCount) {
                throw new IllegalArgumentException("imagem autoral sem evidência visual por arquivo: " + key);
            }
            Map<String, JSONObject> byKey = new HashMap<>();
            for (int i = 0; i < evidence.length(); i++) {
                JSONObject item = evidence.getJSONObject(i);
                byKey.put(item.optString("key"), item);
            }
            for (String mediaKey : stringList(embedded)) {
                JSONObject item = byKey.get(mediaKey);
                if (item == null
                        || !"slide_or_external".equals(item.optString("origin"))
                        || !item.optBoolean("anking_visual_search_complete", false)
                        || item.optString("anking_visual_rejection_reason").trim().length() < 20) {
                    throw new IllegalArgumentException("imagem externa/slide sem rejeição visual AnKing documentada: " + key);
                }
                if (!item.optBoolean("didactic_value_reviewed", false)
                        || item.optString("cognitive_purpose").trim().length() < 10
                        || item.optString("source_credit").isBlank()) {
                    throw new IllegalArgumentException("imagem autoral sem valor didático/crédito documentado: " + key);
                }
            }
        }
        Set<String> localKeys = new HashSet<>();
        for (int i = 0; i < localCount; i++) {
            JSONObject ref = local.getJSONObject(i);
            String refKey = ref.optString("key").trim();
            JSONArray queries = ref.optJSONArray("search_queries");
            JSONArray answers = ref.optJSONArray("expected_answers");
            if (refKey.isBlank() || !localKeys.add(refKey)
                    || queries == null || queries.length() < 2
                    || answers == null || answers.length() == 0
                    || ref.optInt("media_index", -1) < 0
                    || !ref.optBoolean("didactic_value_reviewed", false)
                    || ref.optString("cognitive_purpose").trim().length() < 10) {
                throw new IllegalArgumentException("referência visual AnKing incompleta: " + key + "[" + i + "]");
            }
            if (!html.contains("nebli-anking-media://" + refKey)) {
                throw new IllegalArgumentException("imagem AnKing declarada mas não usada: " + key + "[" + refKey + "]");
            }
        }
        for (String embeddedKey : stringList(embedded)) {
            if (!html.contains("nebli-media://" + embeddedKey)) {
                throw new IllegalArgumentException("imagem embutida declarada mas não usada: " + key + "[" + embeddedKey + "]");
            }
        }
    }

    private void validateIoContract(JSONObject card, String key) throws Exception {
        JSONArray masks = card.optJSONArray("masks");
        JSONArray answers = card.optJSONArray("answers");
        int count = masks == null ? 0 : masks.length();
        if (answers == null || answers.length() != count) {
            throw new IllegalArgumentException("IO answers deve corresponder às máscaras: " + key);
        }
        if (count == 2 && card.optString("pair_rationale").trim().length() < 10) {
            throw new IllegalArgumentException("IO com duas oclusões sem justificativa do par: " + key);
        }
        if (card.optString("source_credit").isBlank()) {
            throw new IllegalArgumentException("IO sem crédito de origem: " + key);
        }
        if (!card.optBoolean("didactic_value_reviewed", false)
                || card.optString("cognitive_purpose").trim().length() < 10) {
            throw new IllegalArgumentException("IO sem valor didático documentado: " + key);
        }
    }

    private void validateMediaCatalog(JSONObject manifest, JSONArray cards) throws Exception {
        JSONArray media = manifest.optJSONArray("media");
        Map<String, JSONObject> catalog = new HashMap<>();
        if (media != null) for (int i = 0; i < media.length(); i++) {
            JSONObject item = media.getJSONObject(i);
            String key = item.optString("key").trim();
            if (key.isBlank() || catalog.put(key, item) != null) {
                throw new IllegalArgumentException("media[] com key ausente/duplicada: " + key);
            }
            if (item.optString("data_base64").isBlank() || item.optString("source_credit").isBlank()) {
                throw new IllegalArgumentException("mídia embutida sem bytes/crédito: " + key);
            }
        }
        for (int i = 0; i < cards.length(); i++) {
            JSONObject card = cards.getJSONObject(i);
            List<String> needed = stringList(card.optJSONArray("media_keys"));
            if ("io".equals(card.optString("source"))) needed.add(card.optString("media_key"));
            for (String key : needed) {
                if (!catalog.containsKey(key)) {
                    throw new IllegalArgumentException("card referencia mídia ausente: " + card.optString("card_key") + "[" + key + "]");
                }
            }
        }
    }

    private void validateAnkingSearchAudit(JSONObject card, String key) throws Exception {
        JSONArray queries = card.optJSONArray("anking_search_queries");
        if (!card.optBoolean("anking_search_complete", false)
                || queries == null || queries.length() < 3
                || !card.optBoolean("anking_search_scope_expanded", false)
                || !card.optBoolean("anking_siblings_reviewed", false)
                || card.optInt("anking_candidates_reviewed", -1) < 0
                || card.optString("anking_rejection_reason").trim().length() < 20) {
            throw new IllegalArgumentException("rota não-AnKing sem busca ampla documentada: " + key);
        }
        if (card.optInt("anking_candidates_reviewed", 0) > 0) {
            JSONArray rejected = card.optJSONArray("anking_rejections");
            if (rejected == null || rejected.length() == 0) {
                throw new IllegalArgumentException("rota não-AnKing sem rejeições dos candidatos: " + key);
            }
        }
    }

    static String canonicalDeckName(JSONObject identity) throws Exception {
        String uc = identity.optString("uc").trim();
        String prova = identity.optString("prova").trim();
        String componente = identity.optString("componente").trim();
        String aula = identity.optString("nome_curto").trim();
        if (!uc.matches("UC\\d{2,}") || !prova.matches("P\\d+")
                || componente.isBlank() || aula.isBlank()
                || componente.contains("::") || aula.contains("::")) {
            throw new IllegalArgumentException("deck_identity inválida");
        }
        return "NEBLI::" + uc + "::" + prova + "::" + componente + "::" + aula;
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
        r.put("candidate_count", p.candidateCount);
        r.put("attempted_queries", new JSONArray(p.attemptedQueries));
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
        for (int i = 0; i < cards.length(); i++) {
            JSONObject card = cards.optJSONObject(i);
            if (card != null && "optional".equalsIgnoreCase(card.optString("tier"))) return true;
        }
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
        if (a != null) for (int i = 0; i < a.length(); i++) {
            String s = a.optString(i, "").trim();
            if (!s.isEmpty()) out.add(s);
        }
        return out;
    }

    private static Set<String> mergeSourceTags(String source, String... extra) {
        Set<String> out = new HashSet<>();
        if (source != null) for (String t : source.trim().split("\\s+")) if (!t.isBlank()) out.add(t);
        for (String t : extra) if (t != null && !t.isBlank()) out.add(t.replace(' ', '_'));
        return out;
    }

    private static String replaceMedia(
            String s, Map<String, String> names, Map<String, String> localNames
    ) {
        String out = s == null ? "" : s;
        for (Map.Entry<String, String> e : names.entrySet()) out = out.replace("nebli-media://" + e.getKey(), e.getValue());
        for (Map.Entry<String, String> e : localNames.entrySet()) {
            out = out.replace("nebli-anking-media://" + e.getKey(), e.getValue());
        }
        return out;
    }

    private static boolean hasMediaPlaceholder(String value) {
        return value.contains("nebli-media://") || value.contains("nebli-anking-media://");
    }

    private boolean existingMediaOk(Plan p, long nid, Map<String, String> mediaNames) {
        AnkiBridge.CardRow row = cardRow(nid, p.selectedOrd);
        if (row == null) {
            List<AnkiBridge.CardRow> rows = anki.cards(nid);
            row = rows.size() == 1 ? rows.get(0) : null;
        }
        if (row == null) return false;
        Set<String> rendered = MediaRefs.images(row);
        if ("anking".equals(p.actualSource) || "external_deck".equals(p.actualSource)) {
            Set<String> source = MediaRefs.images(cardRow(p.sourceNote.nid, p.selectedOrd));
            return rendered.equals(source)
                    && (!p.card.optBoolean("requires_visual", false) || !source.isEmpty());
        }
        if ("authored".equals(p.actualSource)) {
            Set<String> expected = new HashSet<>(p.localMediaNames.values());
            for (String key : p.mediaKeys) {
                String name = mediaNames.get(key);
                if (name != null) expected.add(name);
            }
            return rendered.containsAll(expected);
        }
        if ("io".equals(p.actualSource)) {
            String image = mediaNames.get(p.mediaKey);
            return image != null && rendered.contains(image) && row.question.contains("nebli-io-mask");
        }
        return false;
    }

    private AnkiBridge.CardRow cardRow(long nid, int ord) {
        for (AnkiBridge.CardRow row : anki.cards(nid)) if (row.ord == ord) return row;
        return null;
    }

    private static String safe(String s) { return s.replaceAll("[^A-Za-z0-9_-]", "_"); }
    private static String safeFilename(String s) { return s.replaceAll("[^A-Za-z0-9._-]", "_"); }
    private static String stripExtension(String s) { int i = s.lastIndexOf('.'); return i > 0 ? s.substring(0, i) : s; }
    private static boolean eq(String a, String b) { return a == null ? b == null : a.equals(b); }

    private void report(String message) {
        try { progress.accept(message); } catch (RuntimeException ignored) {}
    }

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

    private static final class Resolution {
        final Plan plan;
        final String reason;
        final int candidateCount;
        final List<String> attemptedQueries;

        private Resolution(Plan plan, String reason, int candidateCount, List<String> attemptedQueries) {
            this.plan = plan;
            this.reason = reason;
            this.candidateCount = candidateCount;
            this.attemptedQueries = new ArrayList<>(attemptedQueries);
        }

        static Resolution resolved(Plan plan, int candidateCount, List<String> attemptedQueries) {
            return new Resolution(plan, "resolved", candidateCount, attemptedQueries);
        }

        static Resolution unresolved(String reason, int candidateCount, List<String> attemptedQueries) {
            return new Resolution(null, reason, candidateCount, attemptedQueries);
        }
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
        final List<String> mediaKeys = new ArrayList<>();
        final Map<String, String> localMediaNames = new LinkedHashMap<>();
        AnkiBridge.NoteSnapshot sourceNote;
        int selectedOrd = -1;
        double score = 0.0, secondScore = 0.0;
        int candidateCount = 0;
        boolean exactPhrase = false;
        final List<String> attemptedQueries = new ArrayList<>();
        Plan(JSONObject card) throws Exception { this.card = card; this.cardKey = card.getString("card_key"); }
    }

    private static final class CardInstallResult {
        final boolean ok, skipped; final String actualSource; final JSONObject receipt;
        CardInstallResult(boolean ok, boolean skipped, String actualSource, JSONObject receipt) {
            this.ok = ok; this.skipped = skipped; this.actualSource = actualSource; this.receipt = receipt;
        }
    }
}
