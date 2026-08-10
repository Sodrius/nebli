# AnkiDroid Companion — arquitetura canônica

Status: implementação incremental. Backend desktop permanece como fallback.

## Objetivo

O AnkiDroid instalado no tablet passa a ser simultaneamente:

1. fonte local do AnKing;
2. destino do deck-aula;
3. dono da mídia já existente na coleção.

O fluxo normal não deve exigir Drive, Colab, `.apkg` nem importação manual.

## Regra de segurança

- READ permitido em qualquer deck fonte, inclusive AnKing.
- WRITE permitido somente em decks cujo nome comece por `NEBLI::`.
- UPDATE/DELETE de notas fonte são proibidos.
- Uma instalação é idempotente por `source_note_id + source_card_ordinal + lesson_slug`.
- Falha parcial não autoriza apagar ou alterar a fonte.

## Semântica da cópia

Para cards provenientes do AnKing/deck externo:

- preservar `modelName`/note type;
- preservar todos os campos sem reescrita;
- preservar HTML, clozes e referências de mídia;
- preservar tags de origem e acrescentar apenas tags de proveniência NEBLI;
- criar uma nota nova no deck-aula;
- não carregar scheduling/history da fonte;
- irmãos não selecionados devem nascer suspensos quando o manifesto selecionar apenas um ordinal.

É proibido prefixar ou modificar `Text` em cópias AnKing. A fidelidade do conteúdo é literal.

## Manifesto

O `nebli-core` produz `flashcards/manifests/<slug>.ankidroid.json`.

Campos mínimos:

```json
{
  "schema": "nebli-ankidroid-v1",
  "lesson_slug": "anato-xx",
  "target_deck": "NEBLI::UC::P::Componente::Aula",
  "source_query": "tag:NEBLI::anato-xx",
  "write_prefix": "NEBLI::",
  "copy_mode": "exact_fields",
  "preserve_media_refs": true,
  "reset_scheduling": true,
  "items": []
}
```

`items` pode ser vazio no modo `source_query`: o Companion resolve localmente os candidatos marcados pela curadoria. Quando `items` existir, cada item deve conter `source_note_id` e, quando necessário, `selected_ordinals`.

## Índice local

O Companion mantém SQLite/FTS local apenas com metadados pesquisáveis:

- note id;
- card id + ordinal;
- deck;
- model;
- tags;
- texto normalizado dos campos;
- nomes de mídia referenciados.

Os binários de mídia permanecem no AnkiDroid. O índice é descartável e reconstruível.

## Pipeline

1. Extrair conceitos da aula.
2. Consultar o índice local do AnKing.
3. Ranquir candidatos.
4. Curar keep/drop por conceito.
5. Gerar autorais/IO somente para lacunas reais.
6. Rodar gates de atomicidade, cloze, visual e cobertura.
7. Gerar manifesto AnkiDroid.
8. Companion executa dry-run e mostra contagem prevista.
9. Companion instala em `NEBLI::*`.
10. Companion confere contagem, modelos e referências de mídia e grava recibo.

## Recibo

Após instalar, o Companion produz um recibo JSON com:

- manifesto/hash;
- notas previstas/criadas/puladas;
- cards previstos/criados/suspensos;
- referências de mídia ausentes;
- erros;
- timestamp.

Um recibo com erro é gate de falha.

## Compatibilidade

Enquanto o Companion não estiver instalado, `montar_deck_aula.py --backend desktop` mantém AnkiConnect/APKG como fallback. O backend preferido do pipeline canônico é `ankidroid`.
