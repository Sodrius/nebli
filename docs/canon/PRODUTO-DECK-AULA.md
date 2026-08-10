# Produto canônico: E1 + deck-aula

Cada `/resumo` entrega:

1. `<Aula> - E1.pdf` — material para aprender, sempre entregue e apontado no
   relatório junto ao fonte `typst-build/<slug>/etapa1.typ`;
2. `<Aula>.apkg` — material para reter;
3. `relatorio-final-<slug>.json` — cobertura, fontes, visual e auditoria.

O PDF termina após E1/Resumindo. E2, E3 e RemNote estão suspensos.

## Deck

- Árvore: `NEBLI::<UC>::<Prova>::<Componente>::<Aula>` e subdeck `Optional`.
  A **UC entra como código de dois dígitos** — `UC02`, `UC08` —, nunca pelo nome por
  extenso. Nome por extenso cria um galho de topo separado e espalha a coleção; nada
  acusa erro, o deck só aparece fora do lugar. A prova é `P1`, `P2`, `P3`. Cronogramas
  às vezes sugerem outro rótulo: a convenção da coleção manda. Validado por
  `build_apkg_offline.py`, que se recusa a montar fora do padrão.
- Núcleo e apoio ficam no deck principal; aprofundamento dispensável fica
  separado e nunca recebe simultaneamente a tag `nucleo`.
- Volume proporcional ao peso da aula e limitado por `card_budget.hard_max` no
  contrato congelado. O total conta os cards Anki efetivamente gerados, inclusive
  opcionais; o montador não pode ultrapassar o teto silenciosamente.
- Faixas de sanidade, não quotas: 15–25 cards para aula pequena, 25–40 para
  média e 35–55 para grande. Mais de 60 exige revisão explícita do escopo e novo
  teto antes da montagem.
- Ritmo longitudinal: 25 novos/dia e 9999 revisões/dia.
- Cram usa busca/deck filtrado por UC, prova, componente, aula e importância.

## Definição de pronto

- todos os conceitos nucleares explicados na E1 e cobertos por card adequado;
- aprofundamento Step 1 dentro do mesmo tema;
- AnKing/decks externos consultados antes de autorar;
- necessidades visuais satisfeitas;
- originais privados intocados;
- APKG offline aberto, inspecionado e renderizado.
- total real do APKG igual ao total previsto e dentro do teto congelado.
