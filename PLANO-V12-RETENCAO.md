# NEBLI — Plano v12: deck de retenção, orçamento derivado e loop de feedback

> **Documento autossuficiente.** Escrito para ser executado numa única corrida por uma sessão
> que não acompanhou a conversa de origem. Traz o contexto, o que muda, os ajustes canônicos
> exatos (arquivo, chave, valor antes → depois), a ordem de execução e o critério de aceite.
> Alvo: `pipeline_version = e1-deck-v12`.

---

## 1. Contexto — o que é o NEBLI e o que acabou de acontecer

O NEBLI é um pipeline que transforma o material de uma aula de medicina em dois artefatos: a
**E1**, apostila em Typst que ensina a aula do zero, e o **Deck-Aula**, um conjunto de cards
autorais em português instalado no AnkiDroid pelo Nebli Companion. O contrato vive em
`config/pipeline.json` e em `docs/canon/` (`EXECUCAO.md`, `E1.md`, `CARD-QUALITY.md`,
`CARDS.md`, `VISUAL-E-IO.md`, `ANKIDROID-COMPANION.md`). O modo ativo é `authored_only`: só
cards `source=authored` e `source=io`, sem busca nem cópia do AnKing.

Em 2026-08-15 rodou a aula `patologia-adaptacao-celular-acumulos` (duas transcrições em PDF do
mesmo professor, 58 slides embutidos, adaptação celular + acúmulos celulares e teciduais).
Saída: E1 de 26 páginas com 16 figuras recortadas dos slides, e deck de 25 cards — 23 cloze e
2 Image Occlusion. Todos os gates passaram: `validar_release_e1_deck`, `validar_e1_formatacao`,
`validar_deck_card_a_card` 25/25, `finalizar_entrega_canonica`.

Depois, o Davi revisou os cards no AnkiDroid, escreveu comentários no campo `NEBLI_Comentario`
e exportou a coleção. Os comentários estão congelados em
`flashcards/feedback/2026-08-15-uc03-p1-patologia.json` e reproduzidos no anexo A. **Eles
mostram que o deck passou em todos os gates e mesmo assim não serve.**

## 2. O que o Davi quer mudar, nas palavras dele

Sobre o card `c01` ("a adaptação preserva a `{{c1::viabilidade}}`"):

> há uma quantidade excessiva de cards sobre conceitos altamente genéricos, que não são da aula
> em específico e clozes que abrem espaço pra múltiplas interpretações. o objetivo dos cards é
> que cada deck diga respeito mais aos conceitos difíceis de decorar daquela aula.

Sobre o `c02` ("o que separa os desfechos é o `{{c1::tempo}}`"):

> esse tipo de card não adiciona nenhum conhecimento à minha bagagem, faz uma relação meio
> esculambanhada […] seria bom que houvesse um reestudo dos cards anking para entender o que é
> um bom card

E, sobre a aula anterior, três pedidos concretos: **imagem no Extra** ("pode ser a do slide
mesmo"), **mais conceitos por card no enunciado e no comentário** — "pra revisar melhor todo o
conteúdo da aula e permitir assuntos laterais serem cobertos sem gerar card em excesso" — e
**hide all / guess all** para listas de três.

Instrução final sobre o teto: **o teto de cards não deve ser respeitado como limite; o deck é
que deve se adequar para cobrir o que precisa ser levado como bagagem adiante**, focado em
ideias e conceitos feitos para decorar de cada aula, como o AnKing faz.

## 3. Diagnóstico

O v11 carda **a compreensão** da aula — princípio organizador, mecanismo, relação causal —
quando deveria cardar **o que precisa ser levado adiante e não se deduz na hora da revisão**.
O teto de 25 agravou: para caber, a ablação cortou o material específico (esteatose alcoólica,
calcificação metastática, melanina, antracose, glicogenoses) e manteve os cards genéricos, que
são justamente os que o Davi marcou como inúteis.

`flashcards/PESQUISA-BOM-CARD.md` já contém a dissecação de 500 cards reais do AnKing v12, e
ela contradiz o contrato atual em cinco pontos de uma vez:

| Métrica AnKing (n=500) | AnKing | Deck v11 desta aula |
|---|---|---|
| Frente, mediana de palavras | 17 | 25 a 35 |
| Cards com imagem | 47% | 0% |
| Cards com hint no cloze | 23% | 0% (proibido na prática) |
| Multi-cloze do mesmo fato | 14% | 0% (proibido) |
| Extra presente | 83%, mediana 20 palavras, anotação | 100%, prosa de monitor |
| Resposta do cloze | entidade nomeada, pode ter 5+ palavras | teto de 3 palavras |

Não é preciso baixar o AnKing v11: o dossiê do repo (`ANKING-DOSSIE-TEXTO.md`,
`ANKING-DOSSIE-IO.md`, `CARD-MIRROR-RUBRICA.md`) é a referência, e a cópia continua proibida.

---

## 4. Ajustes canônicos — arquivo por arquivo

Todos são pequenos e viram canon. Aplicar na ordem abaixo.

### 4.1 `config/pipeline.json`

| Chave | Antes | Depois |
|---|---|---|
| `pipeline_version` | `e1-deck-v11` | `e1-deck-v12` |
| `card_budget.enforce_contract_hard_max` | `true` | `false` |
| `card_budget.budget_mode` | — | `"derived_from_kernel"` (novo) |
| `card_budget.default_hard_max` | teto que bloqueia | renomear para `review_trigger`, mesmos números, sem bloquear |
| `card_budget.manual_review_above` | `25` | mantém, mas só dispara justificativa de uma linha |
| `card_budget.sanity_ranges` | faixa-alvo | vira telemetria, não gate |
| `card_budget.require_floor_per_nuclear_concept` | — | `true` (novo) |
| `card_taxonomy.retention_types` | — | lista fechada de 7 tipos (§4.2) |
| `authored_cards.max_extra_words` | `100` | `150` |
| `authored_cards.front_target_words` | — | `[12, 22]` (novo, alvo, não gate rígido) |
| `authored_cards.extra_image_required_when_visual` | — | `true` (novo) |
| `authored_cards.cloze_hint_allowed` | — | `true` (novo) |
| `authored_cards.cloze_occurrences_per_card` | `1` | remover; ver `sibling_clozes` |
| `sibling_clozes` | — | `{"allowed": true, "max": 4, "require_same_fact_rationale": true}` |
| `cloze_answer_words.hard_max` | `3` | `6`, com `require_reason_above: 3` |
| `cloze_answer_words.answer_is_single_value_token` | — | `true` (novo) |
| `image_occlusion.allow_authored_portuguese_overlay_labels` | — | `true` (novo) |
| `feedback_loop` | — | `{"required": true, "reader": "flashcards/scripts/ler_feedback_apkg.py", "block_on_unanswered": true}` |

### 4.2 `docs/canon/CARD-QUALITY.md` — reescrever o núcleo

Passa a valer, em lugar de "uma recuperação, um `c1`, resposta de uma palavra":

**a) Tipo de retenção declarado, de vocabulário fechado.** Todo card declara `retention_type`,
e a lista **não contém princípio, mecanismo geral nem relação organizativa**:

| `retention_type` | o que é | exemplo desta aula |
|---|---|---|
| `entidade_nomeada` | nome de estrutura, enzima, via, doença | tirosinase; lipase hormônio-sensível; ducto tireoglosso |
| `valor` | número, prazo, proporção, limiar | útero até 40× o volume; hemocromatose 1:200 a 1:500 |
| `discriminador` | o que separa duas entidades parecidas | distrófica × metastática; atrofia × hipoplasia |
| `associacao_clinica` | achado ligado a doença ou conduta | bronze + diabetes + arritmia = hemocromatose |
| `sequencia` | ordem que não se deduz | roxo → biliverdina → hemossiderina |
| `achado_morfologico` | o que se vê na lâmina ou na peça | citoplasma rendilhado; núcleo rechaçado à periferia |
| `eponimo_ou_coloracao` | nome de método ou de síndrome | Perls cora ferro em azul; von Gierke |

Card sem tipo válido não vira card: vira parágrafo de E1.

**b) Teste de especificidade, dois filtros obrigatórios.** *Não-dedutível*: se a resposta se
deduz do enunciado por raciocínio no momento da revisão, cai — cada card declara
`why_not_derivable` em uma linha. *Da aula*: se alguém que nunca assistiu responderia, cai — o
termo da resposta precisa ocorrer na fonte (transcrição ou slide), não só na E1.

**c) Forma.** Frente de 12 a 22 palavras, contexto suficiente, sem definição nua. Hint liberado
(`{{c1::resposta::dica}}`). Clozes irmãos de 2 a 4 quando são partes do mesmo fato ou itens de
uma lista fechada, com rationale; continua proibido empilhar fatos independentes. Resposta é um
token de valor, que pode ser entidade de várias palavras.

**d) Extra é anotação, não parágrafo.** Imagem obrigatória quando o fato é visual, reaproveitando
o recorte que a E1 já usa, com crédito. Conteúdo nos três modos do AnKing: mecanismo curto,
discriminador anti-confusão, mnemônico. Os "assuntos laterais" pedidos nos comentários entram
aqui — é o que cobre a aula inteira sem inflar o número de cards.

**e) Orçamento derivado, não teto.** O tamanho do deck é o número de itens de retenção que são,
ao mesmo tempo, de tipo válido, não-deriváveis e presentes na fonte. Entra o **piso**: todo
conceito nuclear, específico e não-derivável precisa de card; `retention_class: e1_only` deixa
de ser saída, e conceito rebaixado a `supporting` exige `e1_only_reason`.

### 4.3 `docs/canon/CARDS.md`

Campos informados passam a incluir `retention_type`, `why_not_derivable`,
`sibling_cloze_rationale` (quando houver irmãos) e `extra_images[]` com crédito e propósito.

### 4.4 `docs/canon/EXECUCAO.md`

- **Passo 0 (novo):** ler o feedback pendente da aula anterior e endereçar cada item.
- **Passo 4:** citar `precompile-check.py` antes de compilar e `auditar_pdf.py`,
  `auditar_pdf_visual.py` e `pos_pipeline_check.py` depois — o `auditar_pdf_visual` existe
  exatamente para pegar "Resumindo passando de 2 páginas" e "página com mancha < 40%", os dois
  defeitos que a última corrida caçou a olho.
- **Passo 5 (antes de congelar o núcleo):** ler a parte 1 de `PESQUISA-BOM-CARD.md` e o recorte
  do `ANKING-DOSSIE-TEXTO.md` do domínio. Calibração de rubrica; cópia segue proibida.
- **Passo 7:** após autorar, rodar o teste cego (`card_mirror_blind.py` + agente `card-mirror`)
  e registrar o número no gate.
- **Passo 9:** o recibo do Companion vira exigência da corrida seguinte.

### 4.5 `docs/canon/VISUAL-E-IO.md`

Permitir **rótulo em português desenhado por nós sobre a imagem**, com a máscara cobrindo esse
rótulo. Sem isso, patologia fica limitada às poucas lâminas que já vêm rotuladas — nesta aula,
duas em 58 slides. Continua valendo: máscara sobre rótulo, nunca sobre estrutura.

### 4.6 `docs/canon/E1.md`

Uma `clinica-box` por PARTE quando o tema permite, e uso deliberado de `figura-lateral` para
evitar rodapé vazio (páginas 5 e 24 da última corrida).

### 4.7 Documentação divergente

`MEMORY.md` diz v10 e `flashcards/DECK-AULA-PIPELINE.md` diz v9 e ainda manda buscar no AnKing
antes de autorar — regra suspensa. Sincronizar com o `config/pipeline.json` e criar
`flashcards/tests/test_versao_docs.py` que compara as versões citadas nos `.md` com a do config.

---

## 5. Código — o que alterar e o que criar

### 5.1 Validadores (alterar em conjunto, senão o manifesto rejeita o card novo)

- **`flashcards/scripts/validar_deck_card_a_card.py`**
  - `exactly_one_c1_occurrence_required` → aceitar `c1..cN` (N ≤ 4) exigindo
    `sibling_cloze_rationale`; índices contíguos a partir de 1.
  - `cloze_answer_must_have_1_to_3_words` → até 6, com justificativa acima de 3.
  - `GENERIC` (hoje `coisa, processo, estrutura, função, mecanismo, elemento, substância`) vira
    blocklist de verdade **como resposta**, incluindo `viabilidade`, `tempo`, `contato`,
    `parada`, `equilíbrio`, `adaptação`. Livres no enunciado.
  - novos checks: `retention_type` no vocabulário; `why_not_derivable` não vazio; termo da
    resposta presente na fonte da aula; imagem no Extra quando
    `retention_type == achado_morfologico`.
- **`flashcards/scripts/gerar_manifesto_ankidroid.py::_validate_authored`** — hoje exige "um
  cloze", "somente c1", 1–3 palavras, Extra ≤ 100 e frente ≤ 360. Alinhar com o acima.
- **`flashcards/scripts/validar_release_e1_deck.py`** — `card_budget_hard_max` deixa de
  bloquear; entra o piso por conceito nuclear e a exigência de `e1_only_reason`; e o
  `_normalise` passa a colapsar espaço antes de pontuação (âncora que atravessa `*negrito*,`
  falha hoje e custou duas rodadas).
- **`flashcards/scripts/canonical_cards.py::LEARNING_FIELDS`** — incluir os campos novos, senão
  o `content_sha256` não cobre o que afeta aprendizagem.
- **`flashcards/scripts/card_cue_quality.py`** — aceitar hint e frente em forma de pergunta.

### 5.2 Scripts novos

- **`typst-build/extrair_slides_transcricao.py`** — recebe PDFs de transcrição, extrai as
  imagens embutidas, detecta a área útil do slide, remove faixa de título, webcam, e-mail de
  rodapé e logo, emite `slide-*.png` e o `MAPA_CONTEUDO.txt`. Foi quase metade do tempo da
  última corrida, feito em script descartável.
- **`flashcards/scripts/ler_feedback_apkg.py`** — lê `.apkg`/`.colpkg`, descomprime
  `collection.anki21b` (zstd), extrai `NEBLI_Comentario`, flags e as tags
  `NEBLI::card::<slug>::<card_key>` e `NEBLI::hash::<16 hex>`, casa com o `deck-data.json` e
  grava `flashcards/feedback/<slug>.json`. A ligação já funciona: `c01` → `b5b8df86ea055dbd`
  bate com o `content_sha256` do manifesto, então dá para saber se o card mudou depois do
  comentário.
- **`flashcards/scripts/checar_ancoras.py`** — valida as âncoras contra a E1 antes de montar o
  deck-data.
- **`.claude/hooks` (skill `session-start-hook`)** — instala `typst`, `pymupdf`, `pillow`,
  `numpy`, `zstandard` e confere as fontes. Hoje cada sessão web começa sem compilador.

### 5.3 Companion (Java)

`AnkiBridge.java::ensureIoModel` — o note type `NEBLI Image Occlusion v1` não tem
`NEBLI_Comentario` nem `NEBLI_Resposta` (o AnKingOverhaul tem). Hoje não há onde comentar card
de imagem. Adicionar os dois campos e migrar as notas já instaladas.

### 5.4 Revisão independente

`independent_review_passed` e `rendered_pdf_visual_review_passed` passam a ser assinados pelos
agentes `revisor-cobertura` e `revisor-cards-visual`. Hoje quem autora é quem assina, e o gate
não distingue — é fragilidade de honestidade, não de forma.

---

## 6. Ordem de execução, numa corrida só

1. `config/pipeline.json` (§4.1) e os cinco arquivos de `docs/canon/` (§4.2 a §4.6).
2. Validadores e `canonical_cards.py` (§5.1), com os testes de `flashcards/tests/` verdes.
3. Scripts novos (§5.2) e `test_versao_docs.py`; sincronizar `MEMORY.md` e
   `DECK-AULA-PIPELINE.md`.
4. Companion (§5.3) — pode ir em paralelo, não bloqueia o resto.
5. **Prova de fogo:** refazer `patologia-adaptacao-celular-acumulos` sob o v12, usando os
   comentários do anexo A como gabarito, e comparar deck a deck com o v11.

**Efeito esperado na prova de fogo:** dos 25 cards, 4 a 6 saem por serem genéricos (`c01`,
`c02` e similares) e entram algo entre 20 e 28 itens hoje jogados para `e1_only` ou nem
listados — glicogenoses e von Gierke, tetracloreto de carbono, colesterolose e vesícula em
morango, xantomas, antracose, melanina e tirosinase, mieloma, célula tubular renal, atrofia
parda, biliverdina, as quatro causas de calcificação metastática, Barrett com células
caliciformes, hiperplasia prostática após os setenta, HPV e pólipos, desequilíbrio
estrógeno-progesterona, útero 40×, caquexia e TNF, corticoide e tireoidiano contra insulina,
ducto tireoglosso. **O deck sai de 25 para algo entre 45 e 55 cards**, com frente menor, Extra
com imagem e menos card por conceito organizativo.

## 7. Critério de aceite

- Nenhum card respondível por quem não assistiu à aula.
- Todo card com `retention_type` válido e `why_not_derivable` preenchido.
- Todo conceito nuclear específico com pelo menos um card; nenhum `e1_only` sem justificativa.
- Imagem no Extra em todo card de achado morfológico.
- Frente com mediana entre 12 e 22 palavras.
- Teste cego do `card-mirror` no nível do acaso.
- Gate recusando E1 sem relatório do `auditar_pdf_visual`.
- Comentário pendente do `.apkg` bloqueando a corrida seguinte.

## 8. Decisões que dependem do Davi

1. **Flag vermelha** — assumido "revisar/explicar", conforme `auditar_feedback_anki.py`.
   `pato01-c002` e `pato01-c017` vieram com flag e sem comentário.
2. **Rótulo desenhado por nós** sobre a lâmina para destravar IO em patologia (§4.5).
3. **Metadados de deck** — `UC03 / P1` foi assumido na última corrida; a fala só confirma UC3.
   Definir a fonte de verdade (Tema Card ou cronograma) para o nome canônico do deck.

---

## Anexo A — feedback literal do `.apkg` (2026-08-15)

Congelado em `flashcards/feedback/2026-08-15-uc03-p1-patologia.json`. Oito itens em 50 notas.

| card | flag | comentário |
|---|---|---|
| `c01` (adaptação/viabilidade) | — | conceitos genéricos, não específicos da aula; cloze com múltiplas interpretações; "só ocupam espaço" |
| `c02` (tempo) | — | "não adiciona nenhum conhecimento"; "relação meio esculambanhada"; pede reestudo do AnKing |
| `pato01-c002` (função) | vermelha | sem comentário |
| `pato01-c009` (radical hidroxila) | vermelha | "seria útil uma imagem no comentário com toda a reação, pode ser a do slide mesmo" |
| `pato01-c013` (endonucleases) | — | mais temas no enunciado e no comentário; as três ações do cálcio com hide all guess all |
| `pato01-c015` (arcabouço) | — | imagens no comentário e mais conceitos por card, para cobrir assuntos laterais sem card em excesso |
| `pato01-c017` (cariorrexe) | vermelha | sem comentário |
| `pato01-c018` (necrose caseosa) | vermelha | rever o que é conceito central; mais conceitos no comentário; imagem |

## Anexo B — estado da corrida v11 (base de comparação)

- Branch `claude/nebli-pipeline-e1-quality-ojhro4`, commits `73975fb` (entrega) e `2d5bb7b`
  (feedback + plano).
- Aula em `typst-build/_par_patologia-adaptacao-celular-acumulos/`: `etapa1.typ`,
  `resumindo.typ`, `main.typ`, `deck-data.json`, `validation-report.json`, `entrega/`.
- Figuras em `figuras/patologia-adaptacao-celular-acumulos/` (PNG não versionado; o
  `MAPA_CONTEUDO.txt` sim).
- Deck instalado: `NEBLI::UC03::P1::Patologia::Adaptação Celular e Acúmulos`, 25 cards.
