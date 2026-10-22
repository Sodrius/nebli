---
description: Faz o deck-aula inteiro com as preferências vigentes de Davi
argument-hint: <nome, número ou pasta da aula> [observações]
---

Argumentos: $ARGUMENTS

Faça o deck desta aula do começo à entrega, sem agente e sem pedir aprovação:

1. `ESTADO-ATUAL.md`: confira se a aula está livre e registre “Com Claude: <aula>”. Sem argumento, pegue a próxima da fila.
2. `MEMORY.md` é a regra única; leia só as entradas novas de `flashcards/projeto/FEEDBACKS.md`.
3. Execute o **PIPELINE DE GERAÇÃO DE DECK v5** (`flashcards/projeto/EXECUCAO-DECK-AULA.md`), etapa por etapa, sem pular: E0 abrir → E1 ler todo o material → E2 compreender a aula (`compreensao-aula.json`, resumo no chat) → E3 planejar (inventário, mapa de profundidade, escopo) → E4 buscar nos acervos → E5 montar (spec, cobertura, autorais, imagens, `artefatos pre`) → E6 instalar e ler o vivo → E7 fidelidade ao slide → E8 entregar.
4. Relate no formato do MEMORY §11, atualize o ESTADO-ATUAL e siga para a próxima aula da fila até Davi mandar parar.

Refinar a forma atual dos decks, não reformular. Índice: `README.md`. Pedido explícito de “E1 + cards” inclui a E1 (`didatica/E1.md`). Observações do pedido prevalecem sobre a fila. Feedback recebido durante o trabalho: FEEDBACKS (literal) → MEMORY (regra reescrita no lugar) → aplicar já.
