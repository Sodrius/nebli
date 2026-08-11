# Nebli AnkiDroid Companion

Aplicativo Android mínimo para instalar um deck-aula diretamente na coleção já aberta pelo AnkiDroid.

## O que ele faz

- abre `*.ankidroid.json` gerado pelo `nebli-core`;
- exige o release gate que liga o deck à E1 revisada e à cobertura nuclear;
- pede a permissão oficial `com.ichi2.anki.permission.READ_WRITE_DATABASE`;
- consulta notas com o Content Provider oficial do AnkiDroid;
- cria `NEBLI::*` quando necessário;
- duplica a nota usando o mesmo `mid`, os mesmos `flds` e as mesmas tags de origem;
- acrescenta somente tags de proveniência NEBLI;
- move os cards gerados para o deck-aula;
- suspende siblings não selecionados quando o manifesto fixa ordinais;
- resolve a nota AnKing pelo contexto e o sibling pela resposta esperada;
- trata o nome local do deck AnKing como dica, exigindo marcador de origem;
- grava recibo local idempotente com fonte real, consultas e candidatos.

O aplicativo não edita, move, suspende nem apaga a nota fonte.

## Build

O workflow `.github/workflows/android-companion.yml` gera `app-debug.apk` como artifact. Localmente:

```bash
cd android-companion
gradle :app:assembleDebug
```

## Uso no tablet

1. No primeiro uso, conceda ao Companion a permissão oficial do AnkiDroid.
2. O pipeline gera o manifesto canônico com:

```bash
python flashcards/scripts/gerar_manifesto_ankidroid.py \
  --slug <slug> \
  --deck-data arquivos-trabalho/<slug>/deck-data.json \
  --out flashcards/manifests/<slug>.ankidroid.json
```

3. Toque no `.ankidroid.json`. A instalação começa sozinha e, com o recibo
   aprovado, o AnkiDroid abre já no deck correto.

## Busca AnKing

O manifesto fornece várias `search_queries`, `expected_answers` e restrições de
contexto. No pipeline v8, todo card AnKing curado usa `anking_required=true`,
bloqueando fallback silencioso. O protocolo completo está em
`docs/canon/ANKIDROID-COMPANION.md`.
