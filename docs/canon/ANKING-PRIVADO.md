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
notas, GUIDs, note types, decks, tags e referências de mídia em um SQLite local
e cria índice FTS normalizado; a aula pesquisa o índice, não relê os 6 GB.
O SHA-256 exibido entra em `private_sources.anking_index.sha256` do contrato.

## Busca por aula

```bash
python flashcards/scripts/search_private_index.py \
  flashcards/private-cache/anking.private.sqlite \
  "tríade portal" "portal triad" "hepatic portal" --limit-per-query 30
```

Cada conceito recebe consultas independentes em PT, EN, sinônimos,
mecanismo/estrutura e tags ou cards irmãos. O buscador retorna a união
deduplicada e informa quais consultas encontraram cada GUID; uma consulta
estreita sem resultado nunca basta para declarar lacuna. Antes de autoria, o
contrato exige busca `complete`, famílias PT e EN, ao menos uma terceira família
e revisão de irmãos. Guarda consultas, contagens, GUIDs e motivos de rejeição,
mas não versiona o texto protegido dos candidatos.

Se o arquivo estiver ainda subindo, corrompido, incompleto ou sem índice, a E1
pode avançar como rascunho, mas curadoria, autoria em massa e fechamento do deck
ficam bloqueados.
