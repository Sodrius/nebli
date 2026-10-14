---
description: Faz o deck-aula inteiro com as preferências vigentes de Davi
argument-hint: <nome, número ou pasta da aula> [observações]
---

Argumentos: $ARGUMENTS

Faça o deck desta aula do começo à entrega, sem agente e sem pedir aprovação:

1. `ESTADO-ATUAL.md`: confira se a aula está livre e registre “Com Claude: <aula>”. Sem argumento, pegue a próxima da fila.
2. `MEMORY.md` é a regra única; leia só as entradas novas de `flashcards/projeto/FEEDBACKS.md`.
3. Execute `flashcards/projeto/EXECUCAO-DECK-AULA.md` do passo 0 ao 6 (fontes → mapa de escopo → inventário → `percurso-aula.md` com Casos de fronteira → busca → spec → `nebli.artefatos pre` → apply → suspender se aula antiga → tab → despejo lido → pos → REVISAO-DE-QUALIDADE → entrega).
4. Relate no formato do MEMORY §11, atualize o ESTADO-ATUAL e siga para a próxima aula da fila até Davi mandar parar.

Ordem e controles de qualidade (C1–C7): `flashcards/projeto/PLANO-CONTINUACAO-DECKS.md`; percurso card+Tab: `flashcards/projeto/PLANO-CARDS-TABS.md`. Refinar a forma atual dos decks, não reformular. Índice: `README.md`. Pedido explícito de “E1 + cards” inclui a E1 (`didatica/E1.md`). Observações do pedido prevalecem sobre a fila. Feedback recebido durante o trabalho: FEEDBACKS (literal) → MEMORY (regra reescrita no lugar) → aplicar já.
