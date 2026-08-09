# AnKing privado

O arquivo mestre vive no Google Drive e nunca é versionado. A sessão principal
baixa uma cópia de trabalho para `private-sources/` e registra nome, tamanho e
SHA-256 no checkpoint. Não enviar conteúdo, campos, mídia ou o índice ao GitHub.

## Preparação única

```bash
python flashcards/scripts/index_private_apkg.py \
  private-sources/AnKing.apkg \
  --output flashcards/private-cache/anking.private.sqlite
```

O indexador suporta pacotes Anki legados e modernos (`anki21b`/zstd). Ele lê
notas, GUIDs, note types, decks, tags e referências de mídia em um SQLite local.
O SHA-256 exibido entra em `private_sources.anking_index.sha256` do contrato.

## Busca por aula

```bash
python flashcards/scripts/search_private_index.py \
  flashcards/private-cache/anking.private.sqlite "portal triad" --limit 30
```

Buscar nome PT/EN, sinônimos, mecanismo, estrutura, tags e cards irmãos. O
contrato guarda consultas, contagens, GUIDs selecionados e motivos de rejeição;
não guarda o texto protegido dos candidatos.

Se o arquivo estiver ainda subindo, corrompido, incompleto ou sem índice, a E1
pode avançar como rascunho, mas curadoria, autoria em massa e fechamento do deck
ficam bloqueados.
