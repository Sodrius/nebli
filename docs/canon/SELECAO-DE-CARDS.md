# Seleção de cards — o que merece existir no Deck-Aula

Complementa `CARD-QUALITY.md`. Enquanto aquele contrato diz **como** um card
precisa ser feito, este diz **quantos** e **quais** devem existir. É hard gate.

## 1. O problema que este documento resolve

Um deck pode passar em todos os gates formais e ainda estar errado por excesso.
Cada card cobra revisão para sempre; um deck inflado rouba tempo dos cards que
importam e faz o aluno pagar diariamente por informação que ele reconstruiria
sozinho lendo a E1 uma vez.

Três causas produzem inflação, e todas já aconteceram numa corrida real:

1. **Contrato virar gerador.** Se todo conceito declarado precisa de card, o
   tamanho do deck passa a ser decidido por quanto a aula ensina.
2. **Tese virar card.** Enquadramento, motivação e justificativa são o que a E1
   faz melhor; viram cards ruins porque não decaem.
3. **Aprofundamento virar escopo.** Dar um card a cada correlação Step 1
   multiplica o deck sem aumentar a cobertura da aula.

## 2. Teto derivado do que a aula cobra

O teto **não** sai do porte da aula. Porte mede quanto a aula ensina; o deck
mede quanto ela cobra.

```
card_budget.hard_max = cards_per_objective × número de objetivos da aula
```

Com `cards_per_objective = 4`, piso de 12 e teto de 32. Objetivos são os
declarados pela própria aula (slide de objetivos, programa ou roteiro); se a
aula não declarar objetivos, usar os mecanismos nucleares da E1 no lugar.

O teto é total, **não** cota por objetivo: um objetivo que carrega metade da
aula pode levar metade dos cards, e um objetivo periférico pode levar um só. A
distribuição continua proporcional ao peso, como em `CARD-QUALITY.md` §2.

Chegar perto do teto não é meta. Ficar bem abaixo dele é resultado normal e bom.

## 3. Teste de merecimento

Antes de criar um card, as três respostas precisam ser sim:

1. **Decai?** É informação que se perde sem revisão espaçada — um nome, um valor,
   um par estrutura-função, uma correlação clínica. Não é uma tese que se
   reconstrói entendendo a aula.
2. **É cobrada?** Pertence a um objetivo ou a um mecanismo nuclear, não a uma
   frase de enquadramento.
3. **Falha sozinha?** Se o aluno errar, ele perde algo específico e nomeável —
   não "ele não entendeu a aula".

Não viram card, por definição:

- tese e motivação ("por que a recirculação existe", "por que o órgão linfoide
  concentra células");
- enquadramento e comparação de abertura ("quais sistemas incluem o exterior");
- consequência que se deduz de outro card já existente;
- conteúdo que a própria aula anuncia como pertencente à aula seguinte.

Esses conteúdos continuam na E1 e continuam no contrato de cobertura. Eles só não
viram recuperação.

## 4. Conceito coberto pode não ter card

Conceito nuclear exige **cobertura na E1** com qualidade 2 ou 3. Não exige card.

No `deck-data.json`, um conceito sem card declara:

```json
{ "concept_id": "c018", "card_keys": [], "no_card_reason": "Motivo concreto." }
```

O `no_card_reason` é obrigatório, precisa ter ao menos 20 caracteres e precisa
dizer por qual dos critérios do §3 o conceito não merece recuperação. Conceito
nuclear sem card e sem motivo bloqueia o lote — a decisão tem de ser explícita,
nunca silenciosa.

## 5. Um card por ideia, não por fato

Quando dois fatos só fazem sentido como par, existe **um** card, que cobra o
elemento discriminante; o outro lado do par aparece na pista ou no Extra.

- autoral: escrever a frase de modo que o par apareça inteiro e o cloze caia no
  lado que discrimina (por exemplo, córtex visível e medula ocultada);
- AnKing/deck externo: como a cópia é literal, não se funde nada — escolhe-se **o
  card de maior rendimento do par** e a E1 carrega o resto.

Três instâncias da mesma ideia em órgãos diferentes (área T no linfonodo, no baço
e no MALT) são uma ideia, não três cards. Escolher uma instância e tabelar o
resto na E1.

## 6. Cota de aprofundamento Step 1

O Step 1 regula profundidade, não escopo. Portanto:

- cards de aprofundamento (correlação clínica, fármaco, epônimo de doença, nome
  molecular que a aula não cita) somam no máximo **1/4 do deck**;
- cada molécula, via ou correlação recebe **no máximo um card** — uma doença não
  ganha um card para o defeito e outro para o sinal clínico;
- aprofundamento cuja molécula a aula sequer nomeia entra na E1, não no deck.

## 7. Ordem de corte quando o plano estoura o teto

Cortar nesta ordem, e registrar o corte:

1. tese, motivação e enquadramento;
2. instâncias repetidas da mesma ideia;
3. aprofundamento Step 1 acima da cota;
4. conteúdo que a aula seguinte vai cobrir;
5. fatos verdadeiros porém periféricos ao objetivo.

Nunca cortar um conceito nuclear substituindo-o por nada: se ele decai e é
cobrado, ele fica e outro sai.

## 8. Verificação antes de fechar

- `len(cards) <= cards_per_objective × objetivos`;
- todo card passa o teste de merecimento do §3;
- todo conceito sem card tem `no_card_reason`;
- nenhuma ideia aparece em dois cards por instâncias diferentes;
- cards de aprofundamento ≤ 1/4 do total;
- distribuição por objetivo revisada e proporcional ao peso da aula.
