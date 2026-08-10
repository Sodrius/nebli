# Nebli AnkiDroid Companion

Aplicativo Android mínimo para instalar um deck-aula diretamente na coleção já aberta pelo AnkiDroid.

## O que ele faz

- abre `*.ankidroid.json` gerado pelo `nebli-core`;
- pede a permissão oficial `com.ichi2.anki.permission.READ_WRITE_DATABASE`;
- consulta notas com o Content Provider oficial do AnkiDroid;
- cria `NEBLI::*` quando necessário;
- duplica a nota usando o mesmo `mid`, os mesmos `flds` e as mesmas tags de origem;
- acrescenta somente tags de proveniência NEBLI;
- move os cards gerados para o deck-aula;
- suspende siblings não selecionados quando o manifesto fixa ordinais;
- grava recibo local idempotente.

O aplicativo não edita, move, suspende nem apaga a nota fonte.

## Build

O workflow `.github/workflows/android-companion.yml` gera `app-debug.apk` como artifact. Localmente:

```bash
cd android-companion
gradle :app:assembleDebug
```

## Uso no tablet

1. No AnkiDroid, habilite a API/integração com outros apps e conceda a permissão quando solicitado.
2. Instale o APK do Nebli Companion.
3. Gere o manifesto com:

```bash
python flashcards/scripts/montar_deck_aula.py \
  --backend ankidroid \
  --slug <slug> \
  --deck "NEBLI::<UC>::<Prova>::<Componente>::<Aula>" \
  --curado flashcards/curadoria/<slug>-curado.json
```

4. Abra o `.ankidroid.json` no Nebli Companion.
5. O recibo exibido deve terminar com `"ok": true`.

## Limite do MVP

Este primeiro Companion instala/copia diretamente no AnkiDroid. O índice FTS local para busca semântica de todo o AnKing é a próxima camada; o protocolo já foi desenhado para ela em `docs/canon/ANKIDROID-COMPANION.md`.
