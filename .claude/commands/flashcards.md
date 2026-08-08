---
description: Cura/fecha o deck-aula Anki NEBLI de uma aula existente
argument-hint: <slug>
---

`/flashcards` usa o **mesmo pipeline canônico de deck-aula** do `/resumo`; não gera mais o antigo lote fixo de 8 cards RemNote.

1. Ler `FLASHCARDS.md` e `flashcards/DECK-AULA-PIPELINE.md`.
2. Localizar a E1 existente do `<slug>`; não reescrever resumo antigo apenas para adaptar o pipeline.
3. Gerar/revisar checklist e classificar `nuclear | supporting | no_card`.
4. Para conceitos selecionados: AnKing → outros decks → autoral só para lacunas reais.
5. Fechar `matriz-deck-aula-<slug>.json`, incluindo retrieval targets e `load_profile`.
6. Com AnkiConnect, montar com `montar_deck_aula.py --manifest ...`; offline, gerar `.apkg` com exatamente o conjunto aprovado.
7. Rodar o gate com `--verify-anki` ou `--verify-apkg`, conforme o modo.
8. Confirmar 25 novos/dia no topo `NEBLI` e reportar cards por fonte + nucleares cobertos + volume.

Não usar arquivos RemNote antigos como precedente editorial. Frente/cloze autoral EN, Extra PT; visual real/IO conforme `GUIA-IMAGENS-CARDS-NEBLI.md`.
