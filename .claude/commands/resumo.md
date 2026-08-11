---
description: Gera E1 + Deck-Aula completo e diretamente instalável no AnkiDroid
argument-hint: <slug> <slide.pdf> [UC] [Prova] [Componente] [Nome curto]
---

# /resumo — pipeline E1 + Deck-Aula v6

Argumentos: $ARGUMENTS

A **sessão principal executa o pipeline inteiro**. Pergunte ao usuário somente se
uma ambiguidade inevitável impedir o produto correto. Não delegue redação,
curadoria, autoria, visual ou montagem; revisores podem atuar depois dos
artefatos completos, em leitura.

## 0. Carregar e obedecer o canônico

Leia `CLAUDE.md`, `MEMORY.md`, `ERROS.md`, `docs/canon/CARD-QUALITY.md`,
`docs/canon/PIPELINE-E1-DECK.md`, `docs/canon/ANKIDROID-COMPANION.md` e demais
canônicos. Confirme em `config/pipeline.json`:

- `pipeline_version=e1-deck-v7`;
- backend `ankidroid`;
- schema `nebli-ankidroid-deck-v3`;
- instalação direta de AnKing + autorais + IO;
- validação de **todo card real**, aprovação 100%;
- E2/E3/RemNote desligados;
- 25 novos/dia;
- desktop/APKG fora do fluxo normal.

Nunca leia `docs/legacy/` numa corrida normal.

## 1. Entrada, metadados e checkpoint

Resolva slug, slide, UC, prova, componente e nome curto por contexto/cronograma.
Pergunte apenas se a ambiguidade mudaria de fato o deck. Crie
`arquivos-trabalho/<slug>/CHECKPOINT.md` e mantenha fase, fontes, decisões,
pendências e próximo passo.

O deck canônico será:

`NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`

O pipeline deve preencher esses metadados no `deck-data.json`; não obrigue o
usuário a nomear manualmente no Companion.

## 2. Contrato de cobertura e orçamento

Extraia slides, objetivos e perguntas orientadoras. Crie o contrato de cobertura.
Para cada conceito registre:

- id estável;
- nome PT/EN;
- subtópico;
- origem na aula;
- importância (`nucleo`/`optional`);
- âncora E1;
- query em inglês médico e aliases;
- necessidade visual;
- **recuperação específica que o card deve testar**.

Classifique o porte, fixe `card_budget.hard_max` e congele o teto antes de fechar
cards. Não use faixas como meta de quantidade.

## 3. E1 antes dos cards

Escreva `typst-build/etapa1.typ` e `resumindo.typ`. A E1 precisa ensinar o
conteúdo antes que um card o cobre. Mecanismo antes de nomenclatura, conexão com
a aula, explicação suficiente para aluno com base inicial baixa. Não gere
E2/E3/RemNote.

Nenhum card pode introduzir aprofundamento ausente da E1. Conteúdo Step 1 aceito
entra primeiro na E1 e recebe nova âncora.

## 4. Atomizar recuperações, não apenas tópicos

Para cada conceito, decida se merece card. Hard gate:

- precisa ser cobrado/relevante para a aula;
- precisa representar uma recuperação útil;
- uma recuperação independente por card;
- sem duplicata funcional;
- `nucleo` e `optional` separados.

Se não agrega valor de recuperação, **não crie card**.

## 5. Busca AnKing primeiro

Para cada recuperação elegível:

1. gere query em inglês médico;
2. gere aliases/sinônimos úteis;
3. procure AnKing/deck externo antes de autoria;
4. não trate uma busca vazia como prova imediata de lacuna;
5. aceite AnKing somente se testar a mesma recuperação, não apenas tema vizinho;
6. quando houver siblings, planeje o sibling específico;
7. para recuperação visual, só aceite AnKing visualmente adequado.
8. incorpore na E1 o aprofundamento do candidato aceito quando ele pertencer ao
   mesmo mecanismo; só então congele a E1.

No `deck-data.json`, um card preferencialmente AnKing deve ter:

- `source: "anking"`;
- `search_queries` independentes para encontrar a nota;
- `expected_answers` para escolher o cloze/sibling;
- `must_contain`/`must_not_contain` quando houver vizinhos perigosos;
- `anking_required=true` quando a curadoria já comprovou o card adequado;
- `atomic: true`, `relevant: true`;
- `requires_visual` quando aplicável;
- **fallback validado** autoral ou IO.

O fallback cobre lacuna ou ambiguidade real. Se `anking_required=true`, falha
técnica de busca bloqueia o lote: não converter silenciosamente um AnKing já
validado em autoral.

## 6. Autorais — contrato rígido

Autoral somente para lacuna real/fallback. Obedeça `CARD-QUALITY.md`:

- frente em inglês médico natural;
- Extra curto em português;
- uma recuperação;
- exatamente **uma ocorrência de `c1`**;
- cloze preferencialmente 1 palavra;
- 2 quando necessário;
- 3 muito raramente, com justificativa em `three_word_cloze_reason`;
- 4+ bloqueia;
- sem enumerações, mini-resumos ou múltiplas decisões;
- pista inequívoca sem entregar a resposta;
- `atomic=true`, `relevant=true`.
- autoral direto registra `anking_search_complete=true` e
  `anking_rejection_reason` concreto.

A existência de um fallback não permite autoria preguiçosa: ele precisa ser um
bom card por si só.

## 7. Visual e IO

Defina decisão visual para cada recuperação antes de fechar o card.

Prioridade: mídia AnKing adequada → fonte externa/real adequada → slide quando é
a fonte útil da própria aula. Imagem decorativa não entra.

Para IO:

- usar apenas quando reconhecimento/localização agrega;
- `mode=hide_all_guess_all` para mapa coerente;
- máscara cobre o **rótulo-resposta**, não a estrutura;
- múltiplas máscaras somente se formarem conjunto coerente;
- coordenadas normalizadas dentro de `[0,1]`;
- `question_preview_validated=true`;
- `answer_preview_validated=true`;
- `visual_ok=true`;
- `real_source=true`;
- `answer_leak=false`;
- registrar `source_credit`;
- validar crop, legibilidade e solução.

Se um card AnKing `requires_visual=true`, seu fallback deve ser IO válido.

## 8. Construir o plano final `deck-data.json`

Crie `arquivos-trabalho/<slug>/deck-data.json` com metadados e **todos os cards
reais pretendidos**.

Estrutura mínima:

```json
{
  "metadata": {
    "uc": "UC02",
    "prova": "P3",
    "componente": "Anatomia",
    "nome_curto": "Intestino grosso"
  },
  "cards": []
}
```

Todo card tem `card_key` única, `concept_id`, `source`, `tier`, `atomic=true` e
`relevant=true`.

Conte cards reais e confirme que o total está ≤ `card_budget.hard_max`.

## 9. Validação card a card antes de empacotar

Gere `arquivos-trabalho/<slug>/validacao-cards.json` com **um registro por card
real** e rode:

```bash
python flashcards/scripts/validar_deck_card_a_card.py \
  arquivos-trabalho/<slug>/validacao-cards.json \
  --out arquivos-trabalho/<slug>/validacao-cards.result.json
```

Obrigatório:

- `validated_card_count == expected_card_count`;
- `passed_card_count == expected_card_count`;
- `failed_card_count == 0`.

Uma falha bloqueia; corrija o card e rode novamente. Não use amostragem.

## 10. Gerar o pacote único do AnkiDroid

Somente após o gate 100%:

```bash
python flashcards/scripts/gerar_manifesto_ankidroid.py \
  --slug <slug> \
  --deck-data arquivos-trabalho/<slug>/deck-data.json \
  --out flashcards/manifests/<slug>.ankidroid.json
```

O gerador v3 deve:

- derivar o nome do deck dos metadados;
- revalidar regras autorais e IO;
- rejeitar `card_key` duplicada;
- exigir fallback para AnKing;
- embutir mídia nova com SHA-256/base64;
- remover caminhos locais do manifesto;
- definir `expected_card_count` no total real;
- gerar hash de cada card e do manifesto.

Não inclua o banco/índice/mídia privada do AnKing no GitHub.

## 11. Instalação local automática

Ao abrir `<slug>.ankidroid.json` no Nebli Companion:

1. criar/reusar o deck canônico;
2. criar `::Optional` se necessário;
3. resolver todos os cards AnKing localmente;
4. copiar literal `mid/flds/tags` quando confiável;
5. suspender siblings não selecionados;
6. reler e provar fonte intacta;
7. usar fallback validado nos casos ausentes/ambíguos;
8. criar autorais diretamente no AnkiDroid;
9. importar mídia e criar IO diretamente;
10. validar render/runtime por card;
11. fazer rollback das notas novas se qualquer card falhar;
12. exigir `installed_card_count == expected_card_count`;
13. selecionar o deck raiz;
14. abrir o AnkiDroid.

Nenhuma pesquisa/seleção card a card pelo usuário é parte do fluxo normal.

## 12. Revisão independente e fechamento

Revisores podem auditar cobertura/cards/visual após os artefatos estarem
completos. A sessão principal aplica correções e repete os gates afetados.

Bloqueie se houver:

- lacuna nuclear;
- card sem âncora E1;
- card não atômico/irrelevante;
- AnKing escolhido por semelhança apenas;
- AnKing sem fallback;
- autoral ruim/cloze longo;
- IO inadequado;
- mídia quebrada;
- teto excedido;
- contagem divergente;
- fonte modificada;
- write fora de `NEBLI::*`.

## 13. Entrega

Entregue E1/PDF, `deck-data.json`, `validacao-cards.result.json`, manifesto v3 e
relatório final. Quando houver recibo do Companion, exigir contagem final exata.

Definição operacional final: o usuário abre **um arquivo** no Companion e recebe
o deck completo com o nome correto, no AnkiDroid, sem Colab/Drive/APKG e sem
curadoria manual de cards.
