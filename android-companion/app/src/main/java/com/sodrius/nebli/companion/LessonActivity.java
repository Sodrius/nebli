package com.sodrius.nebli.companion;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

/** Default UI: open one Nebli lesson file and finish with the complete deck selected in AnkiDroid. */
public class LessonActivity extends Activity {
    private static final int OPEN_JSON = 40;
    private static final int REQ_ANKI = 41;
    private static final String PERM = "com.ichi2.anki.permission.READ_WRITE_DATABASE";

    private TextView status;
    private JSONObject pendingManifest;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(buildUi());
        if (getIntent() != null && getIntent().getData() != null) openManifest(getIntent().getData());
    }

    private View buildUi() {
        LinearLayout box = new LinearLayout(this);
        box.setOrientation(LinearLayout.VERTICAL);
        box.setPadding(34, 48, 34, 48);
        box.setGravity(Gravity.CENTER_HORIZONTAL);

        TextView title = new TextView(this);
        title.setText("Nebli — Deck-Aula");
        title.setTextSize(25f);
        box.addView(title);

        TextView desc = new TextView(this);
        desc.setText("Um arquivo da aula → AnKing local + lacunas autorais + Image Occlusion → deck completo no AnkiDroid.");
        desc.setPadding(0, 14, 0, 24);
        box.addView(desc);

        Button install = new Button(this);
        install.setText("Instalar Deck-Aula");
        install.setOnClickListener(v -> chooseManifest());
        box.addView(install, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));

        Button diagnostic = new Button(this);
        diagnostic.setText("Diagnóstico");
        diagnostic.setOnClickListener(v -> startActivity(new Intent(this, MainActivity.class)));
        box.addView(diagnostic);

        status = new TextView(this);
        status.setText("Pronto. Se você abrir o arquivo Deck-Aula pelo Android, a instalação começa automaticamente.");
        status.setTextIsSelectable(true);
        status.setPadding(0, 28, 0, 0);
        box.addView(status);

        ScrollView scroll = new ScrollView(this);
        scroll.addView(box);
        return scroll;
    }

    private void chooseManifest() {
        Intent i = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        i.addCategory(Intent.CATEGORY_OPENABLE);
        i.setType("application/json");
        startActivityForResult(i, OPEN_JSON);
    }

    private boolean hasPermission() {
        return checkSelfPermission(PERM) == PackageManager.PERMISSION_GRANTED;
    }

    private void openManifest(Uri uri) {
        try {
            JSONObject m = new JSONObject(readAll(uri));
            if (!FullDeckInstaller.SCHEMA.equals(m.optString("schema"))) {
                throw new IllegalArgumentException("arquivo antigo/incompatível; gere novamente pelo pipeline atual");
            }
            pendingManifest = m;
            if (!hasPermission()) {
                status.setText("Conceda acesso ao AnkiDroid uma vez. Depois a instalação continua sozinha.");
                requestPermissions(new String[]{PERM}, REQ_ANKI);
                return;
            }
            runManifestAsync(m);
        } catch (Exception e) {
            pendingManifest = null;
            status.setText("Deck-Aula inválido: " + e.getMessage());
        }
    }

    private void runManifestAsync(JSONObject manifest) {
        pendingManifest = null;
        status.setText("Instalando o deck completo e validando card por card…");
        new Thread(() -> {
            JSONObject receipt;
            try {
                FullDeckInstaller installer = new FullDeckInstaller(this);
                receipt = installer.install(manifest);
            } catch (Exception e) {
                receipt = new JSONObject();
                try {
                    receipt.put("ok", false);
                    receipt.put("fatal_error", e.toString());
                    receipt.put("lesson_slug", manifest.optString("lesson_slug", "unknown"));
                } catch (Exception ignored) {}
            }
            writeReceipt(receipt);
            JSONObject finalReceipt = receipt;
            runOnUiThread(() -> {
                status.setText(formatReceipt(finalReceipt));
                if (finalReceipt.optBoolean("ok", false) && manifest.optBoolean("open_ankidroid_after_install", true)) {
                    openAnkiDroid();
                }
            });
        }).start();
    }

    private String formatReceipt(JSONObject r) {
        if (!r.optBoolean("ok", false)) {
            return "INSTALAÇÃO BLOQUEADA — nenhum lote parcial novo foi mantido.\n\n" + r.toString();
        }
        return "DECK PRONTO NO ANKIDROID\n\n"
                + r.optString("target_deck") + "\n"
                + "Cards: " + r.optInt("installed_card_count") + "/" + r.optInt("expected_card_count") + "\n"
                + "AnKing: " + r.optInt("anking_cards")
                + " | Autorais: " + r.optInt("authored_cards")
                + " | IO: " + r.optInt("io_cards") + "\n"
                + "Repetidos ignorados: " + r.optInt("idempotent_skips") + "\n\n"
                + "Validação: 100% dos cards previstos passaram.";
    }

    private void openAnkiDroid() {
        try {
            Intent launch = getPackageManager().getLaunchIntentForPackage(AnkiBridge.ANKI_PACKAGE);
            if (launch != null) {
                launch.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                startActivity(launch);
            }
        } catch (Exception ignored) {}
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == OPEN_JSON && resultCode == RESULT_OK && data != null && data.getData() != null) {
            openManifest(data.getData());
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode != REQ_ANKI) return;
        boolean granted = grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED;
        if (!granted) {
            status.setText("Sem a permissão do AnkiDroid o Nebli não consegue instalar o deck.");
            return;
        }
        if (pendingManifest != null) runManifestAsync(pendingManifest);
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
