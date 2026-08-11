package com.sodrius.nebli.companion;

import java.util.Arrays;

/** Pure field mapping kept separate from Android ContentProvider initialization. */
final class ModelFields {
    private ModelFields() {}

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
