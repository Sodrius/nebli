# Produto canônico: E1 + deck-aula

Cada `/resumo` entrega:

1. `<Aula> - E1.pdf` — material para aprender, sempre entregue e apontado no
   relatório junto ao fonte `typst-build/<slug>/etapa1.typ`;
2. `<Aula>.ankidroid.json` — pacote único que instala o deck completo pelo Nebli
   Companion e termina abrindo o AnkiDroid no deck correto.

O PDF termina após E1/Resumindo. E2, E3, RemNote e APKG estão fora do fluxo
normal. Contratos, relatórios e validações são mantidos internamente, sem poluir
a entrega ao usuário.

## Deck

- Árvore: `NEBLI::<UC>::<Prova>::<Componente>::<Aula>` e subdeck `Optional`.
- Núcleo e apoio ficam no deck principal; aprofundamento dispensável fica
  separado e nunca recebe simultaneamente a tag `nucleo`.
- Volume proporcional ao peso da aula e limitado por `card_budget.hard_max` no
  contrato congelado. O total conta os cards Anki efetivamente gerados, inclusive
  opcionais; o montador não pode ultrapassar o teto silenciosamente.
- O deck preserva o núcleo mínimo de retenção; fatos deriváveis e detalhes
  `e1_only` não recebem cards próprios.
- Faixas de planejamento, não quotas: 8–12 cards para aula pequena, 12–18 para
  média e 18–22 para grande. Tetos padrão: 15, 20 e 25, respectivamente.
- Ritmo longitudinal: 25 novos/dia e 9999 revisões/dia.
- Cram usa busca/deck filtrado por UC, prova, componente, aula e importância.

## Definição de pronto

- todos os conceitos nucleares explicados na E1 e cobertos por card adequado;
- aprofundamento Step 1 dentro do mesmo tema;
- necessidades visuais satisfeitas;
- originais privados intocados;
- manifesto v3 aprovado pelo `release_gate=nebli-e1-deck-release-v1`;
- total instalado no AnkiDroid igual ao previsto e dentro do teto congelado;
- E1 fonte/PDF congeladas por hash e revisão semântica independente aprovada.
