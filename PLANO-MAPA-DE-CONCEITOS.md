# Plano — mapa de conceitos por aula

Escrito depois de rodar a corrida `pato-01-lesao-celular-i` de ponta a ponta.
Não altera nada do pipeline ainda: descreve o que a corrida mostrou, o artefato
proposto, onde ele entra e que gate o tornaria obrigatório.

## 1. O que a corrida mostrou

O `release_gate.concepts[]` já é, hoje, **metade de um mapa de conceitos**. Ele
tem nós com identidade, importância, classe de retenção, âncora literal na E1,
qualidade de cobertura e os cards que atendem cada nó. Nesta aula saíram 32 nós
para 22 cards.

Faltam duas coisas, e as duas custaram trabalho manual nesta corrida:

**Faltam arestas.** O contrato sabe que `acumulo-de-calcio-citosolico` e
`cascata-isquemica-fosforilacao-oxidativa` existem, mas não sabe que o segundo é
pré-requisito do primeiro. Quem garantiu a ordem dos subtópicos da E1 e a
coerência das cadeias causais fui eu lendo, não o contrato. Um erro de ordem
passaria por todos os validadores atuais.

**O mapa nasce tarde.** Os `concepts[]` são preenchidos *depois* da autoria, para
justificar os cards que existem. Isso inverte a direção: o correto é o mapa
congelar antes e a autoria responder a ele. Enquanto for assim, o contrato
documenta decisões em vez de dirigi-las.

E há um terceiro achado, que é exatamente o pedido de manter tudo presente no
deck sem inflar o número de cards. Ao revisar o lote pronto contra a aula
inteira, **nove conceitos não apareciam em lugar nenhum do deck** — nem como
card, nem como menção em Extra:

| Conceito ausente do deck | Onde estava | Como foi fechado |
|---|---|---|
| adaptação, hipertrofia, atrofia | só na E1 | menção no Extra de `c001` |
| cinética seriada e mioglobina | só na E1 | menção no Extra de `c002` |
| hepatite aguda, tuberculose | só na E1 | menção no Extra de `c003` |
| ultraestrutura do túbulo renal | só na E1 | menção no Extra de `c004` |
| as sete causas de lesão | só na E1 | menção no Extra de `c009` |
| desprendimento dos ribossomos | só na E1 | menção no Extra de `c009` |
| radicais por falta *e* por excesso de O₂ | só na E1 | menção no Extra de `c013` |
| cálcio realimentando a permeabilidade de transição | só na E1 | menção no Extra de `c020` |
| as quatro linhas do dano de membrana | só na E1 | menção no Extra de `c021` |

Nenhum Extra passou de 100 palavras e nenhum card novo foi criado. O custo de
revisão diária não mudou; a cobertura do deck subiu de 23 para 32 conceitos.
Esse passe foi feito à mão e por leitura — é precisamente o que um mapa de
conceitos automatiza.

## 2. O artefato

Um arquivo por aula, `mapa-conceitos/<slug>.json`, com um espelho legível em
`mapa-conceitos/<slug>.md` (mesma lógica do `mapa-confusoes/`, que já existe e é
lido por humano).

```jsonc
{
  "slug": "pato-01-lesao-celular-i",
  "principio_organizador": "Até onde a célula lesada ainda volta, e o que a impede de voltar.",
  "nodes": [
    {
      "id": "falencia-da-bomba-de-sodio",
      "nome_pt": "Falência da bomba de sódio",
      "subtopico": "3.2",
      "origem": "slide 25 + transcrição",
      "importance": "nuclear",
      "retention_class": "must_recall",
      "deck_presence": "card",          // card | mencao | ausente
      "mention_host": null,              // card_key que menciona, quando deck_presence=mencao
      "e1_anchor": "Toda a alteração ultraestrutural da lesão reversível decorre…"
    }
  ],
  "edges": [
    {"from": "cascata-isquemica-fosforilacao-oxidativa",
     "to": "falencia-da-bomba-de-sodio",
     "type": "causa"},                   // causa | pre_requisito | contrasta_com | exemplifica
    {"from": "falencia-da-bomba-de-sodio",
     "to": "blebs-e-ultraestrutura-reversivel",
     "type": "causa"}
  ]
}
```

Quatro tipos de aresta bastam para esta aula e provavelmente para o ciclo
básico inteiro:

- `pre_requisito` — B não é compreensível antes de A. Governa a ordem dos
  subtópicos da E1.
- `causa` — A produz B no mecanismo. Governa as cadeias causa → mecanismo →
  consequência da prosa.
- `contrasta_com` — A e B são o par que o aluno funde. Alimenta diretamente o
  `mapa-confusoes/` e o campo `confusion_target` dos cards.
- `exemplifica` — A é caso concreto de B. Marca o material que quase sempre vira
  menção em Extra, não card.

O campo `deck_presence` é a peça nova. Ele torna explícito o princípio que hoje
só existe como intenção: **todo nó da aula precisa estar presente no deck, como
card ou como menção**, e nenhum nó pode simplesmente sumir.

## 3. Onde entra no pipeline

Entre o passo 2 e o passo 3 de `docs/canon/EXECUCAO.md` — depois da
`source_to_e1_matrix`, antes de escrever a E1:

1. inventariar fontes;
2. `source_to_e1_matrix`;
3. **`mapa-conceitos/<slug>.json` — nós e arestas, congelado**;
4. escrever a E1 na ordem topológica das arestas `pre_requisito`;
5. congelar o núcleo de retenção *a partir dos nós*, não a partir da leitura;
6. autoria;
7. validação.

O ganho de ordem é concreto: no passo 4, a sequência dos subtópicos deixa de ser
julgamento e passa a ser ordenação topológica com revisão humana por cima. No
passo 5, o núcleo de retenção deixa de ser "o que me pareceu importante" e passa
a ser "os nós `must_recall`, um card cada".

## 4. O gate

Um validador novo, `flashcards/scripts/validar_mapa_conceitos.py`, chamado pelo
`validar_release_e1_deck.py`. Cinco regras, todas mecânicas:

1. **Grafo válido.** Sem nó órfão, sem aresta apontando para id inexistente, e
   sem ciclo nas arestas `pre_requisito` (o ciclo denuncia uma explicação que se
   apoia em si mesma).
2. **Ordem da E1.** A ordem de aparição das âncoras no `etapa1.typ` respeita as
   arestas `pre_requisito`. Se B aparece antes de A e A é pré-requisito de B, a
   corrida trava. É o gate que hoje não existe.
3. **Presença no deck.** Todo nó tem `deck_presence` diferente de `ausente`.
   Quando é `mencao`, o `mention_host` precisa existir no lote **e** o texto do
   Extra desse card precisa conter o termo do nó. Isto é o passe manual da seção
   1 virando gate.
4. **Vizinhança do card.** Todo card `must_recall` tem seus vizinhos imediatos no
   grafo ou como card, ou mencionados no próprio Extra. Impede o card ilhado, que
   cobra um elo cuja cadeia o aluno não consegue reconstruir.
5. **Confusões cobertas.** Toda aresta `contrasta_com` tem linha correspondente
   no `mapa-confusoes/<slug>.md`. Amarra os dois mapas, que hoje vivem soltos.

A regra 3 é a que atende diretamente o pedido: um conceito não precisa de card,
mas não pode desaparecer.

## 5. O que dá para reaproveitar hoje

- Os `concepts[]` desta aula viram os `nodes` sem reescrita: os campos já batem,
  falta acrescentar `deck_presence` e `mention_host`.
- O `mapa-confusoes/pato-01-lesao-celular-i.md` já está escrito por subtópico e
  em pares `A × B`, que é literalmente a lista de arestas `contrasta_com`. A
  conversão é mecânica.
- A `source_to_e1_matrix` já dá `origem` de cada nó.

Ou seja: para esta aula, montar o mapa custa escrever as arestas e classificar a
presença de cada nó no deck. As arestas desta aula são poucas e óbvias — a
cascata isquêmica sozinha responde por um terço delas.

## 6. Risco a evitar

O risco é o mapa virar burocracia: um grafo de sessenta nós que ninguém lê e que
só serve para o validador reclamar. Duas travas contra isso:

- **Teto de nós proporcional ao peso da aula**, na mesma lógica do
  `card_budget`. Aula grande: 25 a 35 nós. Esta aula deu 32, o que sugere que a
  faixa está certa.
- **Aresta só quando ela ensina.** Ligar tudo com tudo destrói o valor. A regra
  prática: a aresta entra se a sua ausência permitiria escrever a E1 numa ordem
  errada, ou se ela nomeia uma confusão real.

## 7. Convergência com o que se publica hoje sobre gerar deck com IA

A busca confirma que o mercado resolveu a parte fácil e não a difícil.
Ferramentas como o [anki-cards-ai-generator](https://github.com/ValeriiZhyla/anki-cards-ai-generator),
o [Ankify](https://www.ankify.app/) e os [geradores de deck por PDF](https://anki-decks.com/)
fazem extração de trechos e emissão de cloze/QA em lote. Nenhuma delas modela
cobertura: o deck sai proporcional ao volume do material, não ao núcleo da aula,
e conceito que não virou card simplesmente some. O NEBLI já está à frente nisso
pelo contrato de ablação e pelo teto congelado.

A literatura vai na direção do grafo. Trabalhos de construção de grafos
educacionais com relações de pré-requisito, como o
[ACE](https://jedm.educationaldatamining.org/index.php/JEDM/article/download/737/218),
o [K12-KGraph](https://arxiv.org/html/2605.09635v1) e a
[completação de grafos curriculares com LLM](https://arxiv.org/html/2501.12300v1),
usam exatamente nós de conceito com arestas de pré-requisito validadas como DAG
— que é a regra 1 proposta aqui. O trabalho de
[inferência de pré-requisitos a partir de recursos educacionais](https://arxiv.org/pdf/1811.12640)
mostra que a extração automática é viável, mas com precisão insuficiente para
uso cego; a leitura correta para nós é gerar as arestas com modelo e revisá-las
à mão, não confiar nelas.

Do lado da qualidade do card, o estudo de
[integração de conteúdo gerado por IA no pré-clerkship](https://www.medrxiv.org/content/10.1101/2025.05.13.25327518.full.pdf)
avalia justamente os três eixos que já estão nos nossos gates: alucinação,
cobertura dos objetivos declarados e densidade de informação por card. E o
[princípio da informação mínima](https://supermemo.guru/wiki/20_rules_of_knowledge_formulation)
continua sendo a base do nosso limite de uma a duas palavras por cloze. O que a
literatura ainda não junta — e é onde o mapa de conceitos põe o NEBLI adiante —
é **usar o grafo como contrato de cobertura do deck**, com a distinção entre nó
que vira card e nó que vira menção.

## 8. Próximo passo sugerido

Rodar o mapa em modo sombra na próxima aula: produzir o
`mapa-conceitos/<slug>.json` no passo 3, escrever a E1 seguindo a ordem
topológica e rodar o validador em modo aviso, sem travar a entrega. Se as cinco
regras não gerarem falso positivo em duas aulas seguidas, promover a gate duro
em `config/pipeline.json`.
