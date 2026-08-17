package com.sodrius.nebli.companion;

import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.net.Uri;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;

/** Thin wrapper over AnkiDroid's official ContentProvider contract. */
public final class AnkiBridge {
    public static final String ANKI_PACKAGE = "com.ichi2.anki";
    public static final Uri NOTES = Uri.parse("content://com.ichi2.anki.flashcards/notes");
    public static final Uri DECKS = Uri.parse("content://com.ichi2.anki.flashcards/decks");
    public static final Uri SELECTED_DECK = Uri.parse("content://com.ichi2.anki.flashcards/selected_deck");
    public static final Uri SCHEDULE = Uri.parse("content://com.ichi2.anki.flashcards/schedule");
    public static final Uri MODELS = Uri.parse("content://com.ichi2.anki.flashcards/models");
    public static final Uri MEDIA = Uri.parse("content://com.ichi2.anki.flashcards/media");

    private final Context context;
    private final ContentResolver cr;

    public AnkiBridge(Context context) {
        this.context = context.getApplicationContext();
        this.cr = this.context.getContentResolver();
    }

    public long ensureDeck(String name) {
        if (!name.startsWith("NEBLI::")) throw new SecurityException("write gate: deck fora de NEBLI::");
        try (Cursor c = cr.query(DECKS, new String[]{"deck_id", "deck_name"}, null, null, null)) {
            if (c != null) {
                int id = c.getColumnIndexOrThrow("deck_id");
                int n = c.getColumnIndexOrThrow("deck_name");
                while (c.moveToNext()) if (name.equals(c.getString(n))) return c.getLong(id);
            }
        }
        ContentValues cv = new ContentValues();
        cv.put("deck_name", name);
        Uri u = cr.insert(DECKS, cv);
        if (u == null || u.getLastPathSegment() == null) throw new IllegalStateException("não foi possível criar deck " + name);
        return Long.parseLong(u.getLastPathSegment());
    }

    public void selectDeck(long did) {
        ContentValues cv = new ContentValues();
        cv.put("deck_id", did);
        cr.update(SELECTED_DECK, cv, null, null);
    }

    public NoteSnapshot readNote(long nid) {
        Uri u = Uri.withAppendedPath(NOTES, Long.toString(nid));
        try (Cursor c = cr.query(u, new String[]{"_id", "mid", "flds", "tags"}, null, null, null)) {
            if (c == null || !c.moveToFirst()) return null;
            return new NoteSnapshot(
                    c.getLong(c.getColumnIndexOrThrow("_id")),
                    c.getLong(c.getColumnIndexOrThrow("mid")),
                    c.getString(c.getColumnIndexOrThrow("flds")),
                    c.getString(c.getColumnIndexOrThrow("tags"))
            );
        }
    }

    public List<NoteSnapshot> searchNotes(String query, int limit, boolean excludeNebliCopies) {
        List<NoteSnapshot> out = new ArrayList<>();
        // Query only IDs first. Asking the provider for every AnKing field in the
        // initial cursor can exhaust the Companion process on multi-gigabyte
        // collections before our logical candidate limit is applied.
        try (Cursor c = cr.query(NOTES, new String[]{"_id"}, query, null, null)) {
            if (c == null) return out;
            int id = c.getColumnIndexOrThrow("_id");
            int scanned = 0;
            int scanLimit = SearchQueryPolicy.scanLimit(limit);
            while (c.moveToNext() && out.size() < limit && scanned++ < scanLimit) {
                NoteSnapshot note = readNote(c.getLong(id));
                if (note == null) continue;
                if (excludeNebliCopies && note.tags != null && note.tags.contains("NEBLI::")) continue;
                out.add(note);
            }
        }
        return out;
    }

    public long findNoteByTag(String tag) {
        try (Cursor c = cr.query(NOTES, new String[]{"_id"}, "tag:" + tag, null, null)) {
            return c != null && c.moveToFirst() ? c.getLong(c.getColumnIndexOrThrow("_id")) : -1L;
        }
    }

    public long insertNote(long mid, String[] fields, Set<String> tags, long targetDid) {
        ContentValues nv = new ContentValues();
        nv.put("mid", mid);
        nv.put("flds", joinFields(fields));
        nv.put("tags", String.join(" ", tags));
        Uri newNote = cr.insert(NOTES, nv);
        if (newNote == null || newNote.getLastPathSegment() == null) throw new IllegalStateException("falha ao inserir nota");
        long nid = Long.parseLong(newNote.getLastPathSegment());
        moveCards(nid, targetDid);
        return nid;
    }

    public int moveCards(long nid, long targetDid) {
        Uri cards = Uri.withAppendedPath(Uri.withAppendedPath(NOTES, Long.toString(nid)), "cards");
        int moved = 0;
        try (Cursor c = cr.query(cards, null, null, null, null)) {
            if (c == null) throw new IllegalStateException("não foi possível ler cards da nota " + nid);
            int ordCol = c.getColumnIndexOrThrow("ord");
            while (c.moveToNext()) {
                int ord = c.getInt(ordCol);
                Uri card = Uri.withAppendedPath(cards, Integer.toString(ord));
                ContentValues cv = new ContentValues();
                cv.put("deck_id", targetDid);
                moved += Math.max(0, cr.update(card, cv, null, null));
            }
        }
        return moved;
    }

    public int suspendExcept(long nid, Set<Integer> active) {
        if (active == null || active.isEmpty()) return 0;
        int suspended = 0;
        for (CardRow card : cards(nid)) {
            if (active.contains(card.ord)) continue;
            ContentValues cv = new ContentValues();
            cv.put("note_id", nid);
            cv.put("ord", card.ord);
            cv.put("suspended", 1);
            suspended += Math.max(0, cr.update(SCHEDULE, cv, null, null));
        }
        return suspended;
    }

    public List<CardRow> cards(long nid) {
        List<CardRow> out = new ArrayList<>();
        Uri cards = Uri.withAppendedPath(Uri.withAppendedPath(NOTES, Long.toString(nid)), "cards");
        try (Cursor c = cr.query(cards, null, null, null, null)) {
            if (c == null) return out;
            int ord = c.getColumnIndexOrThrow("ord");
            int q = c.getColumnIndex("question");
            int a = c.getColumnIndex("answer");
            int d = c.getColumnIndex("deck_id");
            while (c.moveToNext()) {
                out.add(new CardRow(c.getInt(ord), q >= 0 ? c.getString(q) : "", a >= 0 ? c.getString(a) : "", d >= 0 ? c.getLong(d) : -1L));
            }
        }
        return out;
    }

    public void deleteOwnNote(long nid) {
        NoteSnapshot n = readNote(nid);
        if (n == null) return;
        if (n.tags == null || !n.tags.contains("NEBLI::")) throw new SecurityException("rollback recusado: nota não é NEBLI");
        cr.delete(Uri.withAppendedPath(NOTES, Long.toString(nid)), null, null);
    }

    public long findClozeModel() {
        long bestId = -1L;
        int bestScore = -1;
        try (Cursor c = cr.query(MODELS, new String[]{"_id", "name", "field_names", "type"}, null, null, null)) {
            if (c == null) return -1L;
            int id = c.getColumnIndexOrThrow("_id");
            int name = c.getColumnIndexOrThrow("name");
            int fields = c.getColumnIndexOrThrow("field_names");
            int type = c.getColumnIndexOrThrow("type");
            while (c.moveToNext()) {
                if (c.getInt(type) != 1) continue;
                String f = c.getString(fields);
                if (!containsField(f, "Text")) continue;
                String n = c.getString(name);
                int score = 1;
                String low = n == null ? "" : n.toLowerCase(Locale.ROOT);
                if (low.contains("anking")) score += 10;
                if (low.contains("overhaul")) score += 4;
                if (ModelFields.supportFieldIndex(splitFields(f)) >= 0) score += 2;
                // Preferir um note type que saiba guardar comentário: sem ele o
                // feedback do usuário não tem onde morar.
                if (ModelFields.supportsFeedback(splitFields(f))) score += 6;
                if (score > bestScore) { bestScore = score; bestId = c.getLong(id); }
            }
        }
        return bestId;
    }

    public long ensureBasicModel(long defaultDid) {
        return ensureNormalModel(
                "NEBLI Basic v1",
                new String[]{"Front", "Back", "Extra"},
                "{{Front}}",
                "{{FrontSide}}<hr id=answer>{{Back}}{{#Extra}}<div class=\"nebli-extra\">{{Extra}}</div>{{/Extra}}",
                ".card{font-family:Arial,sans-serif;font-size:20px;text-align:left;color:#111;background:#fff}.nebli-extra{margin-top:14px;font-size:.88em;line-height:1.35}",
                defaultDid
        );
    }

    /**
     * Note type IO v2: igual ao v1 mais os campos de feedback.
     *
     * <p>O v1 não tinha onde comentar um card de Image Occlusion, então todo
     * defeito visual só podia ser relatado fora do Anki. Os três campos novos
     * ficam fora do template: não aparecem durante a revisão, apenas no
     * navegador e na auditoria.
     */
    public long ensureIoModel(long defaultDid) {
        return ensureNormalModel(
                "NEBLI Image Occlusion v2",
                new String[]{"Question", "Answer", "Extra", "Source",
                             ModelFields.COMMENT_FIELD, ModelFields.ANSWER_FIELD, ModelFields.HISTORY_FIELD},
                "{{Question}}",
                "{{FrontSide}}<hr id=answer>{{Answer}}{{#Extra}}<div class=\"nebli-extra\">{{Extra}}</div>{{/Extra}}",
                IoRenderer.css(),
                defaultDid
        );
    }

    /** Lê o feedback de uma nota já instalada, por nome de campo. */
    public String[] readFeedback(long nid) {
        NoteSnapshot note = readNote(nid);
        if (note == null) return new String[]{"", "", ""};
        return ModelFields.readFeedback(modelFields(note.mid), splitFields(note.fields));
    }

    public long ensureNormalModel(String name, String[] fields, String qfmt, String afmt, String css, long defaultDid) {
        long existing = findModelByName(name);
        if (existing >= 0) return existing;
        ContentValues mv = new ContentValues();
        mv.put("name", name);
        mv.put("field_names", joinFields(fields));
        mv.put("num_cards", 1);
        mv.put("css", css);
        mv.put("deck_id", defaultDid);
        mv.put("sort_field_index", 0);
        Uri modelUri = cr.insert(MODELS, mv);
        if (modelUri == null || modelUri.getLastPathSegment() == null) throw new IllegalStateException("falha ao criar note type " + name);
        long mid = Long.parseLong(modelUri.getLastPathSegment());
        Uri template = Uri.withAppendedPath(Uri.withAppendedPath(modelUri, "templates"), "0");
        ContentValues tv = new ContentValues();
        tv.put("card_template_name", "Card 1");
        tv.put("question_format", qfmt);
        tv.put("answer_format", afmt);
        if (cr.update(template, tv, null, null) <= 0) throw new IllegalStateException("falha ao configurar template " + name);
        return mid;
    }

    public long findModelByName(String wanted) {
        try (Cursor c = cr.query(MODELS, new String[]{"_id", "name"}, null, null, null)) {
            if (c == null) return -1L;
            int id = c.getColumnIndexOrThrow("_id");
            int name = c.getColumnIndexOrThrow("name");
            while (c.moveToNext()) if (wanted.equals(c.getString(name))) return c.getLong(id);
        }
        return -1L;
    }

    public String[] modelFields(long mid) {
        Uri u = Uri.withAppendedPath(MODELS, Long.toString(mid));
        try (Cursor c = cr.query(u, new String[]{"field_names"}, null, null, null)) {
            if (c == null || !c.moveToFirst()) throw new IllegalStateException("note type não encontrado: " + mid);
            String s = c.getString(c.getColumnIndexOrThrow("field_names"));
            return splitFields(s);
        }
    }

    public String addMedia(Uri sourceUri, String preferredName) {
        ContentValues cv = new ContentValues();
        cv.put("file_uri", sourceUri.toString());
        cv.put("preferred_name", preferredName.replace(" ", "_"));
        Uri returned = cr.insert(MEDIA, cv);
        if (returned == null) throw new IllegalStateException("AnkiDroid recusou mídia " + preferredName);
        String p = returned.getLastPathSegment();
        if (p == null || p.isBlank()) {
            p = returned.getPath();
            if (p != null && p.startsWith("/")) p = p.substring(1);
        }
        if (p == null || p.isBlank()) throw new IllegalStateException("AnkiDroid não retornou nome da mídia");
        return p;
    }

    public static String[] fieldsForModel(String[] names, String text, String extra) {
        return ModelFields.authoredValues(names, text, extra);
    }

    public static Set<String> tags(String... tags) {
        Set<String> out = new HashSet<>();
        for (String t : tags) if (t != null && !t.isBlank()) out.add(t.replace(' ', '_'));
        return out;
    }

    private static boolean containsField(String joined, String wanted) {
        if (joined == null) return false;
        for (String f : splitFields(joined)) if (wanted.equalsIgnoreCase(f)) return true;
        return false;
    }

    private static String[] splitFields(String s) { return s == null ? new String[0] : s.split("\\u001f", -1); }
    private static String joinFields(String[] fields) { return String.join("\u001f", fields); }

    public static final class NoteSnapshot {
        public final long nid, mid;
        public final String fields, tags;
        public NoteSnapshot(long nid, long mid, String fields, String tags) {
            this.nid = nid; this.mid = mid; this.fields = fields; this.tags = tags;
        }
    }

    public static final class CardRow {
        public final int ord;
        public final String question, answer;
        public final long deckId;
        public CardRow(int ord, String question, String answer, long deckId) {
            this.ord = ord; this.question = question; this.answer = answer; this.deckId = deckId;
        }
    }
}
