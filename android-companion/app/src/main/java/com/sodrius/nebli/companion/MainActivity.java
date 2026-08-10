package com.sodrius.nebli.companion;

import android.app.Activity;
import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
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
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class MainActivity extends Activity {
    private static final int OPEN_JSON = 10;
    private static final int REQ_ANKI = 11;
    private static final String ANKI_PERMISSION = "com.ichi2.anki.permission.READ_WRITE_DATABASE";
    private static final Uri NOTES = Uri.parse("content://com.ichi2.anki.flashcards/notes");
    private static final Uri DECKS = Uri.parse("content://com.ichi2.anki.flashcards/decks");
    private static final Uri SCHEDULE = Uri.parse("content://com.ichi2.anki.flashcards/schedule");
    private TextView status;
    private JSONObject pendingManifest;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(buildUi());
        if (getIntent() != null && getIntent().getData() != null) {
            tryImport(getIntent().getData());
        }
    }

    private View buildUi() {
        LinearLayout box = new LinearLayout(this);
        box.setOrientation(LinearLayout.VERTICAL);
        box.setPadding(36, 48, 36, 48);
        box.setGravity(Gravity.CENTER_HORIZONTAL);

        TextView title = new TextView(this);
        title.setText("Nebli AnkiDroid Companion");
        title.setTextSize(24f);
        box.addView(title);

        TextView desc = new TextView(this);
        desc.setText("Instala manifests NEBLI diretamente no AnkiDroid. Decks fonte são somente leitura.");
        desc.setPadding(0, 16, 0, 24);
        box.addView(desc);

        Button open = new Button(this);
        open.setText("Selecionar manifesto .json");
        open.setOnClickListener(v -> {
            Intent i = new Intent(Intent.ACTION_OPEN_DOCUMENT);
            i.addCategory(Intent.CATEGORY_OPENABLE);
            i.setType("application/json");
            startActivityForResult(i, OPEN_JSON);
        });
        box.addView(open);

        status = new TextView(this);
        status.setText("Pronto.");
        status.setTextIsSelectable(true);
        status.setPadding(0, 24, 0, 0);
        box.addView(status);

        ScrollView scroll = new ScrollView(this);
        scroll.addView(box);
        return scroll;
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == OPEN_JSON && resultCode == RESULT_OK && data != null && data.getData() != null) {
            tryImport(data.getData());
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == REQ_ANKI && pendingManifest != null) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                JSONObject m = pendingManifest;
                pendingManifest = null;
                installAsync(m);
            } else {
                status.setText("Permissão do AnkiDroid negada. Ative a API do AnkiDroid e conceda acesso.");
            }
        }
    }

    private void tryImport(Uri uri) {
        try {
            JSONObject manifest = new JSONObject(readAll(uri));
            validateManifest(manifest);
            if (checkSelfPermission(ANKI_PERMISSION) != PackageManager.PERMISSION_GRANTED) {
                pendingManifest = manifest;
                requestPermissions(new String[]{ANKI_PERMISSION}, REQ_ANKI);
                return;
            }
            installAsync(manifest);
        } catch (Exception e) {
            status.setText("Falha ao abrir manifesto: " + e.getMessage());
        }
    }

    private void installAsync(JSONObject manifest) {
        status.setText("Validando e instalando…");
        new Thread(() -> {
            JSONObject receipt;
            try {
                receipt = install(manifest);
            } catch (Exception e) {
                receipt = new JSONObject();
                try {
                    receipt.put("ok", false);
                    receipt.put("error", e.toString());
                    receipt.put("timestamp", Instant.now().toString());
                } catch (Exception ignored) {}
            }
            JSONObject finalReceipt = receipt;
            runOnUiThread(() -> status.setText(finalReceipt.toString()));
            writeReceipt(finalReceipt);
        }).start();
    }

    private JSONObject install(JSONObject manifest) throws Exception {
        validateManifest(manifest);
        ContentResolver cr = getContentResolver();
        String slug = manifest.getString("lesson_slug");
        String targetDeck = manifest.getString("target_deck");
        String sourceQuery = manifest.getString("source_query");
        long targetDid = ensureDeck(cr, targetDeck);
        JSONArray manifestItems = manifest.optJSONArray("items");
        Map<Long, Set<Integer>> selection = selectedOrdinals(manifestItems);
        boolean restrictToItems = manifestItems != null && manifestItems.length() > 0;

        int found = 0, created = 0, skipped = 0, suspended = 0;
        JSONArray errors = new JSONArray();
        String[] projection = new String[]{"_id", "guid", "mid", "tags", "flds"};

        try (Cursor c = cr.query(NOTES, projection, sourceQuery, null, null)) {
            if (c == null) throw new IllegalStateException("AnkiDroid não respondeu à query de notas");
            int idCol = c.getColumnIndexOrThrow("_id");
            int midCol = c.getColumnIndexOrThrow("mid");
            int tagsCol = c.getColumnIndexOrThrow("tags");
            int fldsCol = c.getColumnIndexOrThrow("flds");
            while (c.moveToNext()) {
                long sourceNid = c.getLong(idCol);
                if (restrictToItems && !selection.containsKey(sourceNid)) continue;
                found++;
                String provenanceTag = provenanceTag(slug, sourceNid);
                if (existsByTagInDeck(cr, provenanceTag, targetDeck)) {
                    skipped++;
                    continue;
                }

                ContentValues nv = new ContentValues();
                nv.put("mid", c.getLong(midCol));
                nv.put("flds", c.getString(fldsCol));
                nv.put("tags", mergeTags(c.getString(tagsCol), provenanceTag, "NEBLI::source::copy", "NEBLI::" + slug));
                Uri newNote = cr.insert(NOTES, nv);
                if (newNote == null || newNote.getLastPathSegment() == null) {
                    errors.put("Falha ao inserir cópia de nid=" + sourceNid);
                    continue;
                }
                long newNid = Long.parseLong(newNote.getLastPathSegment());
                Set<Integer> active = selection.get(sourceNid);
                int[] result = moveAndSuspendCards(cr, newNid, targetDid, active);
                suspended += result[1];
                created++;
            }
        }

        JSONObject receipt = new JSONObject();
        receipt.put("ok", errors.length() == 0);
        receipt.put("schema", manifest.getString("schema"));
        receipt.put("lesson_slug", slug);
        receipt.put("target_deck", targetDeck);
        receipt.put("manifest_sha256", manifest.optString("manifest_sha256", ""));
        receipt.put("source_notes_found", found);
        receipt.put("notes_created", created);
        receipt.put("notes_skipped_idempotent", skipped);
        receipt.put("cards_suspended_unselected", suspended);
        receipt.put("errors", errors);
        receipt.put("timestamp", Instant.now().toString());
        return receipt;
    }

    private int[] moveAndSuspendCards(ContentResolver cr, long newNid, long targetDid, Set<Integer> activeOrdinals) {
        Uri cards = Uri.withAppendedPath(Uri.withAppendedPath(NOTES, Long.toString(newNid)), "cards");
        int moved = 0, suspended = 0;
        try (Cursor cc = cr.query(cards, null, null, null, null)) {
            if (cc == null) return new int[]{0, 0};
            int ordCol = cc.getColumnIndexOrThrow("ord");
            while (cc.moveToNext()) {
                int ord = cc.getInt(ordCol);
                Uri card = Uri.withAppendedPath(cards, Integer.toString(ord));
                ContentValues mv = new ContentValues();
                mv.put("deck_id", targetDid);
                moved += Math.max(0, cr.update(card, mv, null, null));
                if (activeOrdinals != null && !activeOrdinals.isEmpty() && !activeOrdinals.contains(ord)) {
                    ContentValues sv = new ContentValues();
                    sv.put("note_id", newNid);
                    sv.put("ord", ord);
                    sv.put("suspended", 1);
                    suspended += Math.max(0, cr.update(SCHEDULE, sv, null, null));
                }
            }
        }
        return new int[]{moved, suspended};
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
        if (created == null || created.getLastPathSegment() == null) throw new IllegalStateException("Não foi possível criar o deck " + name);
        return Long.parseLong(created.getLastPathSegment());
    }

    private boolean existsByTagInDeck(ContentResolver cr, String tag, String deck) {
        String query = "tag:" + tag + " deck:\"" + deck.replace("\"", "") + "\"";
        try (Cursor c = cr.query(NOTES, new String[]{"_id"}, query, null, null)) {
            return c != null && c.moveToFirst();
        }
    }

    private Map<Long, Set<Integer>> selectedOrdinals(JSONArray items) {
        Map<Long, Set<Integer>> map = new HashMap<>();
        if (items == null) return map;
        for (int i = 0; i < items.length(); i++) {
            JSONObject item = items.optJSONObject(i);
            if (item == null || !item.has("source_note_id")) continue;
            long nid = item.optLong("source_note_id", -1L);
            if (nid < 0) continue;
            Set<Integer> ords = map.computeIfAbsent(nid, k -> new HashSet<>());
            JSONArray arr = item.optJSONArray("selected_ordinals");
            if (arr != null) for (int j = 0; j < arr.length(); j++) ords.add(arr.optInt(j));
        }
        return map;
    }

    private String mergeTags(String source, String... extra) {
        Set<String> tags = new HashSet<>();
        if (source != null) for (String t : source.trim().split("\\s+")) if (!t.isBlank()) tags.add(t);
        for (String t : extra) if (t != null && !t.isBlank()) tags.add(t);
        return String.join(" ", tags);
    }

    private String provenanceTag(String slug, long nid) {
        return "NEBLI::copy::" + slug.replaceAll("[^A-Za-z0-9_-]", "_") + "::nid_" + nid;
    }

    private void validateManifest(JSONObject m) throws Exception {
        if (!"nebli-ankidroid-v1".equals(m.optString("schema"))) throw new IllegalArgumentException("schema incompatível");
        String deck = m.getString("target_deck");
        if (!deck.startsWith("NEBLI::")) throw new SecurityException("write gate: target_deck fora de NEBLI::");
        if (m.optBoolean("mutate_source", true)) throw new SecurityException("manifesto tenta mutar fonte");
        if (!"exact_fields".equals(m.optString("copy_mode"))) throw new IllegalArgumentException("copy_mode deve ser exact_fields");
        if (!m.optBoolean("preserve_note_type", false)) throw new IllegalArgumentException("note type deve ser preservado");
        if (!m.has("source_query")) throw new IllegalArgumentException("source_query ausente");
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

    private void writeReceipt(JSONObject receipt) {
        try {
            File dir = new File(getFilesDir(), "receipts");
            if (!dir.exists()) dir.mkdirs();
            String slug = receipt.optString("lesson_slug", "unknown").replaceAll("[^A-Za-z0-9_-]", "_");
            File f = new File(dir, slug + "-latest.json");
            try (FileOutputStream out = new FileOutputStream(f)) {
                out.write((receipt.toString(2) + "\n").getBytes(StandardCharsets.UTF_8));
            }
        } catch (Exception ignored) {}
    }
}
