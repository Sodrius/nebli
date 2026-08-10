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

## Como o índice chega até a sessão

`flashcards/scripts/fetch_private_index.py` fala direto com a API do Drive por HTTPS,
autenticando por conta de serviço (`NEBLI_DRIVE_SA_JSON`) ou por refresh token, baixa as
partes do pacote, confere os SHA-256 do manifesto e extrai o índice em
`flashcards/private-cache/`. O arquivo vai para o disco e nunca passa pelo contexto do
modelo — que é justamente o que impede usar o conector do Drive para isso.

Passo a passo da credencial: `docs/SETUP-ANKING-DRIVE.md`. Sem ela, o script responde
`no_credential` e a corrida segue com o bloqueio registrado, nunca silenciosamente.

## Quando o índice não está no mesmo ambiente da aula

Nem sempre a sessão que produz a aula alcança os 564 MB do índice. O que precisa atravessar
não é o pacote, é a **decisão**: para cada candidato, GUID, note type, tags, primeiro campo
truncado e nomes de mídia. Isso cabe em um `anking-dossie-<slug>.json` de dezenas de KB.

O extrator roda onde o índice mora e deposita o dossiê na pasta privada; a sessão cura sobre
ele e só então puxa a mídia dos GUIDs escolhidos. O dossiê não versiona texto protegido —
ele serve para escolher e para registrar rejeição, e é descartado depois da curadoria.

Se o arquivo estiver ainda subindo, corrompido, incompleto ou sem índice, a E1
pode avançar como rascunho, mas curadoria, autoria em massa e fechamento do deck
ficam bloqueados. Aula fechada sem consulta ao índice sai com todos os cards marcados
`candidate_search.status = blocked_private_index_unreachable` e entra na fila de recuradoria.
