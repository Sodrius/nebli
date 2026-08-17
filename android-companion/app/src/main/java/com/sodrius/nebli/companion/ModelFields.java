package com.sodrius.nebli.companion;

import java.util.Arrays;

/** Pure field mapping kept separate from Android ContentProvider initialization. */
final class ModelFields {
    private ModelFields() {}

    /** Campos onde o feedback do usuário vive. Nunca renderizam na revisão. */
    static final String COMMENT_FIELD = "NEBLI_Comentario";
    static final String ANSWER_FIELD = "NEBLI_Resposta";
    static final String HISTORY_FIELD = "NEBLI_Historico";
    static final String[] FEEDBACK_FIELDS = {COMMENT_FIELD, ANSWER_FIELD, HISTORY_FIELD};

    /** True quando o note type tem onde guardar comentário e resposta. */
    static boolean supportsFeedback(String[] names) {
        return indexOf(names, COMMENT_FIELD) >= 0 && indexOf(names, ANSWER_FIELD) >= 0;
    }

    /**
     * Lê o feedback de uma nota existente a partir dos valores brutos.
     *
     * <p>Não depende da tag {@code NEBLI_comentario::pendente}: um comentário
     * escrito direto no AnkiDroid não recebe tag nenhuma, e era assim que os
     * comentários reais ficavam invisíveis ao pipeline.
     */
    static String[] readFeedback(String[] names, String[] values) {
        String[] out = new String[FEEDBACK_FIELDS.length];
        for (int i = 0; i < FEEDBACK_FIELDS.length; i++) {
            int index = indexOf(names, FEEDBACK_FIELDS[i]);
            out[i] = index >= 0 && index < values.length && values[index] != null ? values[index] : "";
        }
        return out;
    }

    /** True quando há qualquer feedback a preservar. */
    static boolean hasFeedback(String[] feedback) {
        for (String value : feedback) if (value != null && !value.isBlank()) return true;
        return false;
    }

    /**
     * Reescreve os valores da nota nova carregando o feedback da nota antiga.
     *
     * <p>Devolve os valores inalterados quando o note type de destino não tem
     * os campos — o chamador registra a perda no recibo em vez de escondê-la.
     */
    static String[] carryFeedback(String[] names, String[] values, String[] feedback) {
        if (feedback == null || !hasFeedback(feedback)) return values;
        String[] out = values.clone();
        for (int i = 0; i < FEEDBACK_FIELDS.length; i++) {
            int index = indexOf(names, FEEDBACK_FIELDS[i]);
            if (index >= 0 && index < out.length && feedback[i] != null && !feedback[i].isBlank()) {
                out[index] = feedback[i];
            }
        }
        return out;
    }

    /** Anexa uma linha ao histórico, que serve ao navegador e à auditoria. */
    static String[] appendHistory(String[] feedback, String entry) {
        String[] out = feedback.clone();
        String previous = out[2] == null ? "" : out[2];
        out[2] = previous.isBlank() ? entry : previous + "<br>" + entry;
        return out;
    }

    static String[] authoredValues(String[] names, String text, String extra) {
        String[] values = new String[names.length];
        Arrays.fill(values, "");
        int textIndex = indexOf(names, "Text");
        if (textIndex < 0) textIndex = 0;
        values[textIndex] = text == null ? "" : text;
        int extraIndex = supportFieldIndex(names);
        if (extraIndex >= 0) values[extraIndex] = extra == null ? "" : extra;
        return values;
    }

    static int supportFieldIndex(String[] fields) {
        for (String preferred : new String[]{
                "Extra", "Back Extra", "Lecture Notes", "Missed Questions", "Pathoma"
        }) {
            int index = indexOf(fields, preferred);
            if (index >= 0) return index;
        }
        return -1;
    }

    private static int indexOf(String[] fields, String wanted) {
        for (int i = 0; i < fields.length; i++) {
            if (wanted.equalsIgnoreCase(fields[i])) return i;
        }
        return -1;
    }
}
