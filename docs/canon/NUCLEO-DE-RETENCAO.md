# Núcleo de retenção do Deck-Aula

O Deck-Aula não é uma cópia atomizada da E1. A E1 ensina e cobre a aula; o deck
preserva o menor conjunto de recuperações capaz de reconstruir o que importa.
Cada card continua sendo respondível em até 10 segundos e testa uma única
operação mental.

## Planejamento antes da busca

1. Classificar cada conceito como `must_recall`, `derivable`, `e1_only` ou
   `optional`.
2. Fixar os **slots de recuperação** antes de procurar AnKing. A busca escolhe a
   melhor implementação de cada slot; a oferta de cards encontrados não aumenta
   o número de slots.
3. Preferir uma relação causal ou discriminadora que permita reconstruir vários
   detalhes a memorizar fatos vizinhos separadamente.
4. Manter respostas curtas e uma única decisão. Compressão de cobertura não
   autoriza listas, múltiplos clozes ou respostas compostas.

`must_recall` exige card próprio. `derivable` não recebe card próprio quando há
um caminho curto e explícito a partir de cards existentes; o contrato registra
`derived_from_card_keys` e `derivation_rationale`. `e1_only` permanece explicado
na E1, mas não é custo de revisão. `optional` só entra quando seu ganho supera o
custo longitudinal.

## Orçamento

Faixas padrão de planejamento, não metas:

- aula pequena: 8–12 cards; teto duro 15;
- aula média: 12–18 cards; teto duro 20;
- aula grande: 18–22 cards; teto duro 25.

Ultrapassar 25 cards exige justificar por que a aula não pode ser dividida ou
comprimida. Nunca criar cards para preencher a faixa.

## Revisão de compressão e ablação

Antes do release, para cada card:

- verificar se a resposta cabe em até 10 segundos;
- procurar duplicatas ou recuperações que possam ser reconstruídas por outra;
- simular a remoção do card e declarar qual objetivo importante deixaria de ser
  recuperável.

Se a remoção não causa perda relevante, o card sai. O release registra
`retention_kernel_review` com slots congelados antes da busca, revisão de
compressão, revisão de ablação e limite de 10 segundos.
