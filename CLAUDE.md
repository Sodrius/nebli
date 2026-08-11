# NEBLI — entrada canônica

O NEBLI transforma o material de uma aula em dois produtos: **E1 para aprender** e **Deck-Aula Anki para reter**. O fluxo normal é `/resumo` e termina com um manifesto único `.ankidroid.json` que o Nebli Companion instala diretamente no AnkiDroid.

E2, E3, RemNote, Drive/Colab e APKG estão fora do fluxo normal.

## Próxima sessão

Se a sessão recebeu PDFs/arquivos de uma aula e o pedido é “rode o pipeline”, leia primeiro `NEXT-SESSION.md` e execute o pipeline completo sem pedir decisões que possam ser resolvidas pelo canônico.

## Leitura obrigatória

Leia, nesta ordem:

1. `NEXT-SESSION.md` — handoff operacional e definição de pronto;
2. `MEMORY.md` — estado vivo atual;
3. `ERROS.md` — bloqueios recorrentes;
4. `config/pipeline.json` — configuração mecânica vigente;
5. `docs/canon/CARD-QUALITY.md` — hard gate de qualidade de cards;
6. `docs/canon/ANKIDROID-COMPANION.md`;
7. `docs/canon/LOCAL-DECKS-AND-MEDIA.md`;
8. `docs/canon/PIPELINE-E1-DECK.md`;
9. `docs/canon/COBERTURA-E-STEP1.md`;
10. `.claude/commands/resumo.md` — execução detalhada do pipeline.

`docs/legacy/` é histórico. Não carregar nem aplicar em corrida normal.

## Autoridade e execução

- A sessão principal executa o pipeline inteiro: fontes, cobertura, E1, seleção AnKing/decks externos, autoria, visual/IO, validação, manifesto e correções.
- Revisores podem apontar problemas depois dos artefatos completos, mas não substituem a sessão principal.
- Slides, objetivos e perguntas orientadoras definem o escopo. Step 1 aprofunda apenas o mesmo tema/mecanismo.
- Todo conteúdo cobrado por um card precisa estar ensinado e ancorado na E1.
- Ordem de fonte: **AnKing adequado → deck externo real adequado → autoral**.
- A busca da nota usa contexto; a escolha do sibling usa `expected_answers`.
  Autoral direto exige busca AnKing completa e motivo de rejeição. AnKing já
  validado usa `anking_required=true` e nunca cai silenciosamente em fallback.
- Fonte privada é somente leitura. Nunca versionar AnKing, índices privados ou mídia protegida.

## Cards — hard gates

Um card bom testa uma recuperação independente, específica e relevante. O contrato completo está em `docs/canon/CARD-QUALITY.md` e não é opcional.

Regras nucleares:

- `atomic=true` e `relevant=true` para todo card;
- não criar card só para atingir quantidade;
- contar cards Anki reais e respeitar `card_budget.hard_max`;
- autoral em inglês médico, Extra curto em português;
- autoral com exatamente um `c1`; cloze de 1 palavra por padrão, 2 quando necessário, 3 excepcionalmente com justificativa, 4+ bloqueia;
- IO somente quando a tarefa visual agrega; em conjunto coerente usar `hide_all_guess_all`;
- máscara cobre o rótulo-resposta, não a estrutura que deve ser reconhecida;
- fonte visual real, crédito, previews pergunta/resposta e ausência de vazamento são obrigatórios;
- AnKing/deck externo é copiado literalmente, preservando note type, campos, HTML, clozes, tags e mídia; sibling não selecionado fica suspenso;
- fallback validado evita curadoria manual quando a busca local é ausente/ambígua.

## Definição de pronto

A aula só fecha quando:

1. E1 cobre todo conceito nuclear;
2. todo card tem âncora E1;
3. **100% dos cards reais** passam no gate card a card;
4. `expected_card_count == validated_card_count == passed_card_count`;
5. manifesto `nebli-ankidroid-deck-v3` é gerado com nome canônico `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`;
6. o Companion consegue instalar AnKing, decks externos, autorais, mídia nova e IO diretamente no AnkiDroid;
7. qualquer falha de runtime causa rollback das notas novas;
8. o recibo final confirma `installed_card_count == expected_card_count`.

## Configuração ativa

`config/pipeline.json` deve estar em `pipeline_version=e1-deck-v8`, backend `ankidroid`, schema `nebli-ankidroid-deck-v3`, release gate `nebli-e1-deck-release-v1`, 25 novos/dia e revisão sem teto prático. Desktop/APKG só podem reaparecer como fallback emergencial se o usuário pedir explicitamente.
