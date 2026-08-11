package com.sodrius.nebli.companion;

import android.app.Activity;
import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class LessonActivity extends Activity {
    private static final int OPEN_JSON = 40;
    private static final int REQ_ANKI = 41;
    private static final String PERM = "com.ichi2.anki.permission.READ_WRITE_DATABASE";
    private static final Uri NOTES = Uri.parse("content://com.ichi2.anki.flashcards/notes");
    private static final Uri DECKS = Uri.parse("content://com.ichi2.anki.flashcards/decks");
    private static final Uri SCHEDULE = Uri.parse("content://com.ichi2.anki.flashcards/schedule");
    private static final Pattern CLOZE = Pattern.compile("\\{\\{c(\\d+)::(.*?)(?:::[^}]*)?}}", Pattern.CASE_INSENSITIVE | Pattern.DOTALL);

    private TextView status;
    private EditText deckInput;
    private EditText conceptsInput;
    private JSONObject pendingManifest;
    private boolean pendingManual = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(buildUi());
        if (getIntent() != null && getIntent().getData() != null) openManifest(getIntent().getData());
    }

    private View buildUi() {
        LinearLayout box = new LinearLayout(this);
        box.setOrientation(LinearLayout.VERTICAL);
        box.setPadding(32, 44, 32, 44);
        box.setGravity(Gravity.CENTER_HORIZONTAL);

        TextView title = new TextView(this);
        title.setText("Nebli — Deck-Aula");
        title.setTextSize(24f);
        box.addView(title);

        TextView desc = new TextView(this);
        desc.setText("Resolve conceitos no AnkiDroid, seleciona candidatos com gate de confiança e copia somente para NEBLI::*.");
        desc.setPadding(0, 12, 0, 22);
        box.addView(desc);

        Button open = new Button(this);
        open.setText("Abrir manifesto da aula");
        open.setOnClickListener(v -> {
            Intent i = new Intent(Intent.ACTION_OPEN_DOCUMENT);
            i.addCategory(Intent.CATEGORY_OPENABLE);
            i.setType("application/json");
            startActivityForResult(i, OPEN_JSON);
        });
        box.addView(open);

        TextView fallback = new TextView(this);
        fallback.setText("Modo manual de teste (opcional):");
        fallback.setPadding(0, 24, 0, 6);
        box.addView(fallback);

        deckInput = new EditText(this);
        deckInput.setText("NEBLI::Deck-Aula");
        deckInput.setSingleLine(true);
        box.addView(deckInput, new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));

        conceptsInput = new EditText(this);
        conceptsInput.setHint("um conceito por linha\nex.: portal vein\nhepatic flexure\nmarginal artery of Drummond");
        conceptsInput.setMinLines(5);
        conceptsInput.setGravity(Gravity.TOP);
        conceptsInput.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_FLAG_MULTI_LINE);
        box.addView(conceptsInput, new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));

        Button build = new Button(this);
        build.setText("Montar Deck-Aula automaticamente");
        build.setOnClickListener(v -> requestOrBuildManual());
        box.addView(build);

        status = new TextView(this);
        status.setText("Pronto. O fluxo normal é abrir o manifesto gerado pelo Nebli.");
        status.setTextIsSelectable(true);
        status.setPadding(0, 24, 0, 0);
        box.addView(status);

        ScrollView scroll = new ScrollView(this);
        scroll.addView(box);
        return scroll;
    }

    private boolean hasPermission() {
        return checkSelfPermission(PERM) == PackageManager.PERMISSION_GRANTED;
    }

    private void requestOrBuildManual() {
        if (!hasPermission()) {
            pendingManual = true;
            requestPermissions(new String[]{PERM}, REQ_ANKI);
            return;
        }
        try {
            JSONObject m = manualManifest();
            runManifestAsync(m);
        } catch (Exception e) {
            status.setText("Entrada inválida: " + e.getMessage());
        }
    }

    private JSONObject manualManifest() throws Exception {
        String deck = deckInput.getText().toString().trim();
        if (!deck.startsWith("NEBLI::")) throw new IllegalArgumentException("o deck deve começar por NEBLI::");
        JSONArray concepts = new JSONArray();
        for (String line : conceptsInput.getText().toString().split("\\r?\\n")) {
            String q = line.trim();
            if (q.isEmpty()) continue;
            JSONObject c = new JSONObject();
            c.put("id", "manual-" + concepts.length());
            c.put("query", q);
            c.put("required", true);
            concepts.put(c);
        }
        if (concepts.length() == 0) throw new IllegalArgumentException("adicione ao menos um conceito");
        JSONObject m = new JSONObject();
        m.put("schema", "nebli-ankidroid-lesson-v2");
        m.put("lesson_slug", "manual");
        m.put("target_deck", deck);
        m.put("mutate_source", false);
        m.put("concepts", concepts);
        JSONObject search = new JSONObject();
        search.put("min_score", 0.82);
        search.put("min_margin", 0.06);
        search.put("max_candidates", 80);
        search.put("prefer_anking", true);
        search.put("require_anking_marker", false);
        m.put("search", search);
        return m;
    }

    private void openManifest(Uri uri) {
        try {
            JSONObject m = new JSONObject(readAll(uri));
            validateManifest(m);
            if (!hasPermission()) {
                pendingManifest = m;
                requestPermissions(new String[]{PERM}, REQ_ANKI);
                return;
            }
            runManifestAsync(m);
        } catch (Exception e) {
            status.setText("Manifesto inválido: " + e.getMessage());
        }
    }

    private void validateManifest(JSONObject m) throws Exception {
        if (!"nebli-ankidroid-lesson-v2".equals(m.optString("schema"))) throw new IllegalArgumentException("schema incompatível");
        if (!m.getString("target_deck").startsWith("NEBLI::")) throw new SecurityException("write gate: deck fora de NEBLI::");
        if (m.optBoolean("mutate_source", true)) throw new SecurityException("manifesto tenta alterar a fonte");
        JSONArray concepts = m.optJSONArray("concepts");
        if (concepts == null || concepts.length() == 0) throw new IllegalArgumentException("concepts vazio");
    }

    private void runManifestAsync(JSONObject manifest) {
        status.setText("Resolvendo conceitos no AnKing local e montando o deck…");
        new Thread(() -> {
            String message;
            JSONObject receipt;
            try {
                receipt = execute(manifest);
                message = formatReceipt(receipt);
            } catch (Exception e) {
                receipt = new JSONObject();
                try {
                    receipt.put("ok", false);
                    receipt.put("error", e.toString());
                    receipt.put("timestamp", Instant.now().toString());
                } catch (Exception ignored) {}
                message = "FALHOU: " + e.getClass().getSimpleName() + ": " + e.getMessage();
            }
            writeReceipt(receipt);
            String finalMessage = message;
            runOnUiThread(() -> status.setText(finalMessage));
        }).start();
    }

    private JSONObject execute(JSONObject manifest) throws Exception {
        ContentResolver cr = getContentResolver();
        String slug = manifest.getString("lesson_slug");
        String deck = manifest.getString("target_deck");
        JSONArray concepts = manifest.getJSONArray("concepts");
        JSONObject search = manifest.optJSONObject("search");
        if (search == null) search = new JSONObject();
        double minScore = search.optDouble("min_score", 0.82);
        double minMargin = search.optDouble("min_margin", 0.06);
        int maxCandidates = search.optInt("max_candidates", 80);
        boolean preferAnking = search.optBoolean("prefer_anking", true);
        boolean requireAnking = search.optBoolean("require_anking_marker", false);

        long did = ensureDeck(cr, deck);
        JSONArray resolved = new JSONArray();
        JSONArray unresolved = new JSONArray();
        int created = 0, reused = 0, sourceVerified = 0, suspended = 0;

        for (int i = 0; i < concepts.length(); i++) {
            JSONObject concept = concepts.getJSONObject(i);
            String id = concept.optString("id", "concept-" + i);
            String query = concept.getString("query").trim();
            List<String> variants = new ArrayList<>();
            variants.add(query);
            JSONArray aliases = concept.optJSONArray("aliases");
            if (aliases != null) for (int j = 0; j < aliases.length(); j++) {
                String a = aliases.optString(j, "").trim();
                if (!a.isEmpty()) variants.add(a);
            }

            List<Candidate> candidates = gatherCandidates(cr, variants, maxCandidates);
            if (candidates.isEmpty()) {
                unresolved.put(unresolved(id, query, "no_candidate", null));
                continue;
            }

            boolean anyAnking = false;
            for (Candidate c : candidates) if (c.ankingLike) { anyAnking = true; break; }
            List<Candidate> scoped = new ArrayList<>();
            for (Candidate c : candidates) {
                if (requireAnking && !c.ankingLike) continue;
                if (preferAnking && anyAnking && !c.ankingLike) continue;
                scoped.add(c);
            }
            if (scoped.isEmpty()) {
                unresolved.put(unresolved(id, query, "no_anking_candidate", null));
                continue;
            }

            for (Candidate c : scoped) {
                c.score = Ranker.score(query, c.fields, c.tags, c.ankingLike);
                for (String v : variants) c.score = Math.max(c.score, Ranker.score(v, c.fields, c.tags, c.ankingLike));
            }
            Collections.sort(scoped, (a, b) -> Double.compare(b.score, a.score));
            Candidate best = scoped.get(0);
            double second = scoped.size() > 1 ? scoped.get(1).score : 0.0;
            boolean exactPhrase = Ranker.normalize(best.fields).contains(Ranker.normalize(query));
            if (!Ranker.confident(best.score, second, exactPhrase, minScore, minMargin)) {
                JSONObject detail = new JSONObject();
                detail.put("best_nid", best.nid);
                detail.put("best_score", round(best.score));
                detail.put("second_score", round(second));
                unresolved.put(unresolved(id, query, "low_confidence", detail));
                continue;
            }

            NoteSnapshot sourceBefore = readNote(cr, best.nid);
            if (sourceBefore == null) {
                unresolved.put(unresolved(id, query, "source_disappeared", null));
                continue;
            }
            Set<Integer> selectedOrdinals = inferOrdinals(best.fields, query);
            if (hasMultipleClozes(best.fields) && selectedOrdinals.isEmpty()) {
                JSONObject detail = new JSONObject();
                detail.put("best_nid", best.nid);
                detail.put("best_score", round(best.score));
                unresolved.put(unresolved(id, query, "ambiguous_cloze_sibling", detail));
                continue;
            }

            CopyResult copy = copyOrReuse(cr, slug, deck, did, best, selectedOrdinals);
            NoteSnapshot sourceAfter = readNote(cr, best.nid);
            boolean sourceIntact = snapshotsEqual(sourceBefore, sourceAfter);
            if (!sourceIntact) throw new SecurityException("fonte alterada durante cópia nid=" + best.nid);
            sourceVerified++;
            created += copy.created ? 1 : 0;
            reused += copy.created ? 0 : 1;
            suspended += copy.suspended;

            JSONObject r = new JSONObject();
            r.put("concept_id", id);
            r.put("query", query);
            r.put("source_note_id", best.nid);
            r.put("copy_note_id", copy.copyNid);
            r.put("score", round(best.score));
            r.put("anking_marker", best.ankingLike);
            r.put("source_unchanged", true);
            JSONArray ords = new JSONArray();
            for (Integer ord : selectedOrdinals) ords.put(ord);
            r.put("selected_ordinals", ords);
            resolved.put(r);
        }

        JSONObject receipt = new JSONObject();
        receipt.put("ok", unresolved.length() == 0);
        receipt.put("schema", manifest.getString("schema"));
        receipt.put("lesson_slug", slug);
        receipt.put("target_deck", deck);
        receipt.put("concepts_total", concepts.length());
        receipt.put("resolved_count", resolved.length());
        receipt.put("unresolved_count", unresolved.length());
        receipt.put("notes_created", created);
        receipt.put("notes_reused_idempotent", reused);
        receipt.put("sources_verified_unchanged", sourceVerified);
        receipt.put("siblings_suspended", suspended);
        receipt.put("resolved", resolved);
        receipt.put("unresolved", unresolved);
        receipt.put("timestamp", Instant.now().toString());
        return receipt;
    }

    private List<Candidate> gatherCandidates(ContentResolver cr, List<String> queries, int max) {
        Map<Long, Candidate> unique = new HashMap<>();
        for (String q : queries) {
            if (q == null || q.trim().isEmpty()) continue;
            collect(cr, q.trim(), max, unique);
            if (unique.size() < Math.min(8, max)) {
                List<String> toks = new ArrayList<>(Ranker.tokens(q));
                toks.sort((a, b) -> Integer.compare(b.length(), a.length()));
                if (!toks.isEmpty()) collect(cr, toks.get(0), max, unique);
                if (toks.size() > 1) collect(cr, toks.get(0) + " " + toks.get(1), max, unique);
            }
            if (unique.size() >= max) break;
        }
        return new ArrayList<>(unique.values());
    }

    private void collect(ContentResolver cr, String query, int max, Map<Long, Candidate> unique) {
        try (Cursor c = cr.query(NOTES, new String[]{"_id", "mid", "tags", "flds"}, query, null, null)) {
            if (c == null) return;
            int idCol = c.getColumnIndexOrThrow("_id");
            int midCol = c.getColumnIndexOrThrow("mid");
            int tagsCol = c.getColumnIndexOrThrow("tags");
            int fieldsCol = c.getColumnIndexOrThrow("flds");
            while (c.moveToNext() && unique.size() < max) {
                String tags = c.getString(tagsCol);
                if (tags != null && tags.contains("NEBLI::source::copy")) continue;
                long nid = c.getLong(idCol);
                if (unique.containsKey(nid)) continue;
                String flds = c.getString(fieldsCol);
                unique.put(nid, new Candidate(nid, c.getLong(midCol), tags, flds, Ranker.looksAnKing(tags)));
            }
        } catch (Exception ignored) {}
    }

    private Set<Integer> inferOrdinals(String fields, String query) {
        Map<Integer, Double> scores = new HashMap<>();
        Matcher m = CLOZE.matcher(fields == null ? "" : fields);
        while (m.find()) {
            int ord = Integer.parseInt(m.group(1)) - 1;
            String answer = m.group(2);
            double s = Ranker.coverage(query, answer);
            if (Ranker.normalize(query).contains(Ranker.normalize(answer)) || Ranker.normalize(answer).contains(Ranker.normalize(query))) s = Math.max(s, 0.9);
            scores.put(ord, Math.max(scores.getOrDefault(ord, 0.0), s));
        }
        if (scores.isEmpty()) return new LinkedHashSet<>();
        if (scores.size() == 1) return new LinkedHashSet<>(scores.keySet());
        double best = -1;
        int bestOrd = -1;
        for (Map.Entry<Integer, Double> e : scores.entrySet()) {
            if (e.getValue() > best) { best = e.getValue(); bestOrd = e.getKey(); }
        }
        Set<Integer> out = new LinkedHashSet<>();
        if (best >= 0.50) out.add(bestOrd);
        return out;
    }

    private boolean hasMultipleClozes(String fields) {
        Set<Integer> ords = new HashSet<>();
        Matcher m = CLOZE.matcher(fields == null ? "" : fields);
        while (m.find()) ords.add(Integer.parseInt(m.group(1)) - 1);
        return ords.size() > 1;
    }

    private CopyResult copyOrReuse(ContentResolver cr, String slug, String deck, long did, Candidate source, Set<Integer> active) throws Exception {
        String provenance = provenanceTag(slug, source.nid);
        long copyNid = findCopyByTag(cr, provenance, deck);
        boolean created = false;
        if (copyNid < 0) {
            ContentValues nv = new ContentValues();
            nv.put("mid", source.mid);
            nv.put("flds", source.fields);
            nv.put("tags", mergeTags(source.tags, provenance, "NEBLI::source::copy", "NEBLI::" + safeTag(slug)));
            Uri inserted = cr.insert(NOTES, nv);
            if (inserted == null || inserted.getLastPathSegment() == null) throw new IllegalStateException("falha ao inserir cópia nid=" + source.nid);
            copyNid = Long.parseLong(inserted.getLastPathSegment());
            created = true;
        }
        int suspended = moveAndSetSiblingState(cr, copyNid, did, active);
        NoteSnapshot copy = readNote(cr, copyNid);
        if (copy == null || copy.mid != source.mid || !safeEquals(copy.fields, source.fields)) throw new IllegalStateException("cópia não preservou mid/flds nid=" + source.nid);
        return new CopyResult(copyNid, created, suspended);
    }

    private int moveAndSetSiblingState(ContentResolver cr, long nid, long did, Set<Integer> active) {
        Uri cards = Uri.withAppendedPath(Uri.withAppendedPath(NOTES, Long.toString(nid)), "cards");
        int suspended = 0;
        try (Cursor c = cr.query(cards, null, null, null, null)) {
            if (c == null) return 0;
            int ordCol = c.getColumnIndexOrThrow("ord");
            while (c.moveToNext()) {
                int ord = c.getInt(ordCol);
                Uri card = Uri.withAppendedPath(cards, Integer.toString(ord));
                ContentValues mv = new ContentValues();
                mv.put("deck_id", did);
                cr.update(card, mv, null, null);
                if (!active.isEmpty()) {
                    ContentValues sv = new ContentValues();
                    sv.put("note_id", nid);
                    sv.put("ord", ord);
                    boolean shouldSuspend = !active.contains(ord);
                    sv.put("suspended", shouldSuspend ? 1 : 0);
                    cr.update(SCHEDULE, sv, null, null);
                    if (shouldSuspend) suspended++;
                }
            }
        }
        return suspended;
    }

    private long ensureDeck(ContentResolver cr, String name) {
        try (Cursor c = cr.query(DECKS, new String[]{"deck_id", "deck_name"}, null, null, null)) {
            if (c != null) {
                int idCol = c.getColumnIndexOrThrow("deck_id");
                int nameCol = c.getColumnIndexOrThrow("deck_name");
                while (c.moveToNext()) if (name.equals(c.getString(nameCol))) return c.getLong(idCol);
            }
        }
        ContentValues cv = new ContentValues();
        cv.put("deck_name", name);
        Uri created = cr.insert(DECKS, cv);
        if (created == null || created.getLastPathSegment() == null) throw new IllegalStateException("não foi possível criar deck " + name);
        return Long.parseLong(created.getLastPathSegment());
    }

    private long findCopyByTag(ContentResolver cr, String tag, String deck) {
        String q = "tag:" + tag + " deck:\"" + deck.replace("\"", "") + "\"";
        try (Cursor c = cr.query(NOTES, new String[]{"_id"}, q, null, null)) {
            if (c != null && c.moveToFirst()) return c.getLong(c.getColumnIndexOrThrow("_id"));
        }
        return -1L;
    }

    private NoteSnapshot readNote(ContentResolver cr, long nid) {
        Uri note = Uri.withAppendedPath(NOTES, Long.toString(nid));
        try (Cursor c = cr.query(note, new String[]{"mid", "flds", "tags"}, null, null, null)) {
            if (c == null || !c.moveToFirst()) return null;
            return new NoteSnapshot(c.getLong(c.getColumnIndexOrThrow("mid")), c.getString(c.getColumnIndexOrThrow("flds")), c.getString(c.getColumnIndexOrThrow("tags")));
        }
    }

    private boolean snapshotsEqual(NoteSnapshot a, NoteSnapshot b) {
        return a != null && b != null && a.mid == b.mid && safeEquals(a.fields, b.fields) && safeEquals(a.tags, b.tags);
    }

    private String provenanceTag(String slug, long nid) {
        return "NEBLI::copy::" + safeTag(slug) + "::nid_" + nid;
    }

    private String safeTag(String s) {
        return (s == null ? "lesson" : s).replaceAll("[^A-Za-z0-9_-]", "_");
    }

    private String mergeTags(String source, String... extras) {
        Set<String> tags = new LinkedHashSet<>();
        if (source != null) for (String t : source.trim().split("\\s+")) if (!t.isEmpty()) tags.add(t);
        for (String t : extras) if (t != null && !t.isEmpty()) tags.add(t);
        return String.join(" ", tags);
    }

    private JSONObject unresolved(String id, String query, String reason, JSONObject detail) throws Exception {
        JSONObject o = new JSONObject();
        o.put("concept_id", id);
        o.put("query", query);
        o.put("reason", reason);
        if (detail != null) o.put("detail", detail);
        return o;
    }

    private String formatReceipt(JSONObject r) {
        if (!r.optBoolean("ok", false) && r.has("error")) return "FALHOU: " + r.optString("error");
        int total = r.optInt("concepts_total");
        int resolved = r.optInt("resolved_count");
        int unresolved = r.optInt("unresolved_count");
        return "Deck-Aula concluído.\n" +
                "Resolvidos: " + resolved + "/" + total + " | pendentes: " + unresolved + "\n" +
                "Cópias novas: " + r.optInt("notes_created") + " | reaproveitadas: " + r.optInt("notes_reused_idempotent") + "\n" +
                "Fontes verificadas intactas: " + r.optInt("sources_verified_unchanged") + "\n\n" +
                (unresolved == 0 ? "PASS: todos os conceitos foram resolvidos com gate de confiança." : "Conceitos ambíguos NÃO foram copiados. O recibo registra as pendências para o pipeline criar autorais ou refinar a busca.");
    }

    private void writeReceipt(JSONObject receipt) {
        try {
            File dir = new File(getFilesDir(), "receipts");
            if (!dir.exists()) dir.mkdirs();
            String slug = safeTag(receipt.optString("lesson_slug", "unknown"));
            File f = new File(dir, slug + "-lesson-latest.json");
            try (FileOutputStream out = new FileOutputStream(f)) {
                out.write((receipt.toString(2) + "\n").getBytes(StandardCharsets.UTF_8));
            }
        } catch (Exception ignored) {}
    }

    private String readAll(Uri uri) throws Exception {
        try (InputStream in = getContentResolver().openInputStream(uri)) {
            if (in == null) throw new IllegalArgumentException("arquivo inacessível");
            try (BufferedReader br = new BufferedReader(new InputStreamReader(in, StandardCharsets.UTF_8))) {
                StringBuilder sb = new StringBuilder();
                String line;
                while ((line = br.readLine()) != null) sb.append(line).append('\n');
                return sb.toString();
            }
        }
    }

    private static double round(double x) { return Math.round(x * 1000.0) / 1000.0; }
    private static boolean safeEquals(String a, String b) { return a == null ? b == null : a.equals(b); }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == OPEN_JSON && resultCode == RESULT_OK && data != null && data.getData() != null) openManifest(data.getData());
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode != REQ_ANKI) return;
        boolean granted = grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED;
        if (!granted) {
            pendingManifest = null;
            pendingManual = false;
            status.setText("Permissão do AnkiDroid negada.");
            return;
        }
        if (pendingManifest != null) {
            JSONObject m = pendingManifest;
            pendingManifest = null;
            runManifestAsync(m);
            return;
        }
        if (pendingManual) {
            pendingManual = false;
            requestOrBuildManual();
        }
    }

    private static class Candidate {
        final long nid;
        final long mid;
        final String tags;
        final String fields;
        final boolean ankingLike;
        double score;
        Candidate(long nid, long mid, String tags, String fields, boolean ankingLike) {
            this.nid = nid; this.mid = mid; this.tags = tags; this.fields = fields; this.ankingLike = ankingLike;
        }
    }

    private static class NoteSnapshot {
        final long mid; final String fields; final String tags;
        NoteSnapshot(long mid, String fields, String tags) { this.mid = mid; this.fields = fields; this.tags = tags; }
    }

    private static class CopyResult {
        final long copyNid; final boolean created; final int suspended;
        CopyResult(long copyNid, boolean created, int suspended) { this.copyNid = copyNid; this.created = created; this.suspended = suspended; }
    }
}
