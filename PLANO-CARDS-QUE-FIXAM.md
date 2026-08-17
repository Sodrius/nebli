# Plano — cards que fixam o conceito, não a frase

Alvo: o deck-aula parar de produzir recuperações genéricas e passar a produzir
recuperações que reconstroem o mecanismo da aula. Diagnóstico feito sobre o
`.apkg` de 2026-08-17 (547 notas; 149 no `NEBLI::UC03::P1`) e sobre o código
atual em `flashcards/scripts` e `android-companion`.

Este plano é executável em fases independentes. Cada fase tem critério de aceite
verificável por script ou teste — nenhuma fase fecha por declaração.

---

## 1. Diagnóstico com evidência

Os defeitos abaixo foram medidos, não inferidos. Todos passaram pelos gates
atuais e chegaram ao AnkiDroid.

### 1.1 O deck inteiro saiu em inglês

| Medida | Valor |
|---|---|
| Cards textuais em `NEBLI::UC03::P1` | 142 |
| Frentes com ≥3 palavras funcionais inglesas | 103 |
| Frentes que o gate atual classificou como `pt-BR` | 94 |

`config/pipeline.json` fixa `authored_cards.language = "pt-BR"` e
`docs/canon/CARD-QUALITY.md` diz "todo texto final é português". O deck saiu com
frente em inglês e Extra em português:

> `The cause that initiates a disease is its {{c1::etiology}}.`
> Extra: `Etiologia responde ao que inicia a doença…`

**Causa.** `canonical_cards.derived()` decide idioma contando 10 stopwords sobre
`visible + extra` e só acusa inglês a partir de 3 ocorrências. Frases curtas
("Fibrosis is highlighted by {{c1::Masson trichrome}} staining.") somam 1 e
passam. `card_cue_quality.portuguese_front_failures()`, que usa uma lista maior e
analisa só a frente, existe mas **não é chamada** por
`validar_deck_card_a_card.py`.

**Por que isso destrói fixação.** Cada revisão passa a exigir uma tradução mental
antes da recuperação. O aluno treina "traduzir e reconhecer", não "recuperar o
conceito". É o defeito de maior impacto do lote.

### 1.2 Clozes genéricos: 20 cards recuperam uma palavra abstrata

`time`, `size`, `probability`, `memory`, `injury`, `replication`,
`transcription`, `maturation`, `conformation`, `receptor`, `adhesion`,
`compensation`, `architecture`, `sampling`, `sectioning`, `antibodies`,
`amplitude`, `air`, `fever`, `mortality`.

Exemplos:

- `In pulse-echo imaging, echo return {{c1::time}} determines interface depth.`
- `Disease develops when a homeostatic disturbance is not restored by {{c1::compensation}}.`
- `Routine tissue fixation prevents autolysis and preserves {{c1::architecture}}.`

O terceiro é literalmente o card **reprovado** em
`docs/canon/EXEMPLOS-CARDS.md` ("A fixação impede a autólise e preserva a
{{c1::arquitetura}}"), traduzido para inglês. O exemplar canônico existe e o
pipeline gerou exatamente o anti-exemplo.

**Causa.** A lista `GENERIC` em `validar_deck_card_a_card.py` tem 7 palavras, em
português, contra um deck em inglês — não podia bater em nada. E a checagem é
lista negra de vocabulário, não avaliação do papel cognitivo da resposta.

### 1.3 O gate semântico forte nunca roda

`card_cue_quality.semantic_cue_review_failures()` implementa o contrato real:
`cloze_role` entre os seis papéis permitidos, `blind_review_passed`,
`plausible_alternatives` vazio, `lexical_leak=false`, `ambiguity_review` com
substância.

`validar_deck_card_a_card.py` — o validador citado em
`config/pipeline.json → final_validation.validator` — **não importa esse módulo**.
Ele usa `_semantic_review_ok()`, que aprova qualquer card cujos campos
`ambiguity`, `anti_induction` e `duplicate_check` tenham 12 caracteres. Três
frases quaisquer liberam o card.

### 1.4 O teto de cards se ajusta ao deck

```python
hard_max = int(data.get("card_budget_hard_max", ..., expected))
```

Quando o campo não vem no JSON, o teto vira o próprio número de cards e
`expected <= hard_max` é sempre verdadeiro. Resultado no deck:

| Aula | Cards | Teto duro canônico |
|---|---|---|
| Imunologia — Reconhecimento inato | 52 | 25 |
| Bioquímica — Recombinação | 35 | 25 |
| Patologia — Ferramentas do Diagnóstico | 22 | 25 |
| Imunologia — Organização do sistema imune | 20 | 25 |
| Radiologia — Princípios de RX e USG | 20 | 25 |

Duas aulas passaram do teto — uma delas com o dobro. `docs/canon/NUCLEO-DE-RETENCAO.md`
descreve compressão e ablação, mas nada no código simula a remoção de um card.

### 1.5 Duplicação funcional não é detectada

Mesma resposta cobrada duas vezes, às vezes em aulas diferentes da mesma prova:

- `electron microscopy` — `c010-morphologic-scales` e `c024-ciliary-em`;
- `CXCL8` — `ak-il8-neutrofilo` (Organização) e `k42-cxcl8` (Reconhecimento inato);
- `constant region` — `c004-constant-effector` e `c033-class-switch`;
- cisteínas das quimiocinas — `au-chemokine-families` e `k42-cisteina`,
  praticamente a mesma frase em duas aulas.

`duplicate_check` é texto livre preenchido pelo próprio agente. Não há
comparação entre respostas normalizadas nem entre relações recuperadas.

### 1.6 Cards que cobram o rótulo, não o mecanismo

`docs/canon/CARD-QUALITY.md` bloqueia "recuperação do rótulo quando o mecanismo é
o alvo relevante". Passaram assim mesmo:

- `The cause that initiates a disease is its {{c1::etiology}}.`
- `The mechanisms by which an etiology produces disease constitute its {{c1::pathogenesis}}.`
- `A specific nucleic-acid sequence is exponentially amplified by {{c1::PCR}}.`
- `Immunohistochemistry identifies tissue proteins using specific {{c1::antibodies}}.`

E cards que descrevem o slide em vez do conteúdo:

- `Among the TLRs of the ligand table, the one still listed with an unknown ligand is {{c1::TLR10}}.`

### 1.7 Image Occlusion está quebrado nos 7 cards do lote

Todos os 7 IO saíram com o mesmo prompt, em inglês, e com a resposta colada:

```
Q: Identify the masked labels.
A: light chainheavy chainSlide da aula; Watson, Molecular Biology of the Gene, 7th ed.
```

Três defeitos somados:

1. **Prompt default vaza para o produto.** `FullDeckInstaller.java:543` usa
   `card.optString("prompt", "Identify the masked labels.")`. Os 7 cards caíram
   no default — logo o manifesto não trouxe `prompt`, apesar de
   `validar_deck_card_a_card.py` exigir `io_prompt_missing` e `io_prompt_not_portuguese`.
   O manifesto instalado não passou por esse gate.
2. **Resposta renderizada duas vezes.** `IoRenderer.answerHtml()` desenha o rótulo
   sobre a imagem *e* repete a lista em `.nebli-io-answers`. Em texto plano as
   respostas concatenam sem separador ("light chain" + "heavy chain").
3. **Crédito renderizado na revisão.** O mesmo método imprime `.nebli-source`,
   que gruda a fonte no fim da resposta. O crédito já está preservado no campo
   `Source`; não precisa aparecer durante a revisão.

Há ainda pares incoerentes: `Anterior/superficial` + `Patient right` — dois
rótulos sem relação funcional, e em inglês, contra
`image_occlusion.answers_language = "pt-BR"`.

### 1.8 `authored_only` não é enforçado na instalação

A nota `1786484788526` está no deck UC03 com a tag `NEBLI::source::anking`, o
texto original em inglês (`What is the first step of leukocyte extravasation? /
{{c1::Margination}}`) e ~15 tags AnKing herdadas. `config/pipeline.json` diz
`card_source_mode: "authored_only"` e `anking.status: "suspended"`, mas
`FullDeckInstaller.installOne()` mantém o ramo `"anking".equals(p.actualSource)`
plenamente funcional e nada o bloqueia em tempo de instalação.

### 1.9 O feedback do usuário morre

- `FullDeckInstaller.java:454` executa `anki.deleteOwnNote(existing)` sempre que o
  hash muda, e recria a nota do zero. Comentário, resposta, flag e histórico da
  nota antiga vão junto.
- O note type `NEBLI Image Occlusion v1` (`AnkiBridge.java:198`) tem apenas
  `Question`, `Answer`, `Extra`, `Source`. **Não há onde comentar um card IO.**
- `ler_comentarios.py` só enxerga notas com a tag `NEBLI_comentario::pendente`.
  Os 7 comentários reais deste `.apkg` estão em `NEBLI_Comentario` **sem** essa
  tag — invisíveis ao pipeline.
- Nenhuma das 149 notas UC03 carrega comentário: o canal existe só nas notas
  legadas de Etimologia, herdado do note type AnKing importado.

Os 7 comentários reais, que hoje não chegam a lugar nenhum:

| Card | Comentário |
|---|---|
| `odino-` (odinofagia) | "caard incoerente e incorret" |
| `atresia` | "muito avançado com comentário fraco… poderia decompor a-tresia… o cloze também tem muitas respostas" |
| `-filia` (eosinófilo) | "clozes com muitas palavras. conteúdo é importante, mas o card é ruim, vale reescrevê-lo" |
| `-trofia` | "trofia é desenvolvimento, não crescimento, porque atrofia não é crescimento" |
| `dolico-`, `-metria`, `balan/o` | marcados sem texto |

O comentário de `-trofia` é um erro de conteúdo apontado há semanas que continua
no deck.

### 1.10 O deck instalado não é auditável

As tags gravadas são `NEBLI::card::<slug>::<id>`, `NEBLI::hash::<16>`,
`NEBLI::source::<x>` e `NEBLI::<slug>`. Não há `tier`, `concept_id` nem âncora
E1 — `tier` só escolhe o subdeck (`FullDeckInstaller.java:80`). Depois de
instalado, é impossível verificar no AnkiDroid se o núcleo está coberto.

`audit_apkg.py` aceita só `apkg` e `--json-out`: audita a coleção inteira. Com
547 notas (398 delas de Etimologia legado), qualquer problema das 149 notas da
prova some na média — foi assim que a auditoria anterior devolveu "aprovado".

---

## 2. Princípio da correção

Três mudanças de fundo, das quais tudo o mais decorre:

1. **O gate deixa de perguntar "o agente declarou?" e passa a perguntar "o card
   sobrevive a um teste?".** Toda declaração booleana vira evidência derivável:
   idioma medido na frente, papel do cloze validado contra a frase, ablação
   simulada, preview de IO renderizado e conferido.
2. **Todo comentário seu vira um teste permanente.** O pipeline não deve apenas
   ler o feedback; deve mudar de forma que o mesmo defeito não passe de novo.
3. **Um card só existe se a sua remoção causa perda nomeável.** Não é o teto que
   corta cards; é a ablação. O teto vira consequência, não meta.

---

## 3. Fases

Ordem escolhida para que cada fase seja validável com o material que já existe —
o `.apkg` atual serve de corpus de regressão desde a Fase 1.

### Fase 1 — Idioma: fechar o vazamento (1 arquivo, alto impacto)

**Muda:** `flashcards/scripts/validar_deck_card_a_card.py`,
`flashcards/scripts/canonical_cards.py`.

- `_authored()` passa a chamar `card_cue_quality.portuguese_front_failures()`,
  que analisa **só a frente** (o Extra em português não pode mais mascarar uma
  frente inglesa).
- Baixar o limiar de 3 para 2 palavras funcionais e ampliar a lista com
  `of, a, an, in, to, and, for, its, can, may, does, than, both, after, before`.
- Manter a exceção legítima: termo médico inglês isolado (`hairpins`, `pre-BCR`,
  `Ku70/Ku80`) não deve reprovar uma frase portuguesa. O gate mede palavras
  funcionais, nunca termos técnicos.
- Adicionar teste com as 103 frentes inglesas reais do `.apkg` como corpus
  negativo e um corpus positivo de frentes portuguesas com termo inglês.

**Aceite:** as 142 frentes do UC03 reprovam; nenhum exemplar de
`docs/canon/EXEMPLOS-CARDS.md` reprova.

### Fase 2 — Ligar o gate cognitivo que já existe

**Muda:** `flashcards/scripts/validar_deck_card_a_card.py`,
`docs/canon/CARDS.md`.

- `validate_card()` passa a chamar
  `semantic_cue_review_failures(card, strict=True)`. O validador do
  `final_validation` e o gerador de manifesto passam a aplicar o mesmo contrato.
- `cue_quality.cloze_role` vira campo obrigatório do schema de card, restrito aos
  seis papéis já definidos em `config/pipeline.json → cue_quality.allowed_cloze_roles`.
- Substituir a lista `GENERIC` por uma regra de papel: **reprovar quando a
  resposta é um substantivo abstrato sem discriminador médico** — se a mesma
  lacuna aceita `tempo`, `duração`, `intervalo` e `atraso`, o card não fecha.
  Semear a lista com as 20 respostas genéricas reais medidas em §1.2.
- Reprovar card cuja informação discriminante está apenas no Extra (comparar
  `retrieval_target` com o que a frente sozinha permite recuperar).

**Aceite:** os 20 cards genéricos de §1.2 reprovam com motivo nomeado; um card
com resposta `discriminador` bem formada passa.

### Fase 3 — Ablação de verdade, e o teto voltando a ser teto

**Muda:** `flashcards/scripts/validar_deck_card_a_card.py`,
`flashcards/scripts/canonical_cards.py`, `docs/canon/NUCLEO-DE-RETENCAO.md`.

- `hard_max` deixa de ter default igual a `expected`. Passa a ser derivado do
  tamanho declarado da aula (`small`/`medium`/`large` →  15/20/25 de
  `config/pipeline.json → card_budget.default_hard_max`). Ausência do campo
  **bloqueia**, não libera.
- Cada card declara, e o gate confere que não são frases vazias:
  - `memory_gain` — o que passa a ser lembrado por causa dele;
  - `ablation_loss` — o que deixa de ser recuperável se ele sair;
  - `why_not_e1_only` — por que merece custo longitudinal diário;
  - `confusion_target` — qual erro ou confusão ele previne.
- `ablation_loss` que só reformula o enunciado do card reprova. A perda tem de
  citar outro conceito ou outra recuperação do contrato.
- Detector de duplicação funcional: agrupar por resposta normalizada **e** por
  `retrieval_target`; dois cards no mesmo grupo exigem `derivation_rationale`
  explícito ou um dos dois sai. Escopo da comparação = a prova inteira
  (`NEBLI::<UC>::<Prova>`), não só a aula — foi entre aulas que CXCL8 duplicou.

**Aceite:** rodar contra o UC03 atual bloqueia Reconhecimento inato (52 > 25) e
Recombinação (35 > 25), e nomeia os 4 pares duplicados de §1.5.

### Fase 4 — Consertar Image Occlusion

**Muda:** `android-companion/.../IoRenderer.java`,
`android-companion/.../FullDeckInstaller.java`,
`android-companion/.../IoRendererTest.java`.

- `answerHtml()` passa a emitir **só** a imagem com os rótulos sobrepostos.
  Remover o bloco `.nebli-io-answers` e o bloco `.nebli-source`.
- O crédito continua gravado no campo `Source` e some da revisão.
- Remover o default `"Identify the masked labels."` de `FullDeckInstaller:543`.
  Prompt ausente ou não-português **lança**, não substitui.
- `IoRendererTest.answerRevealsLabelsAndCredits()` hoje exige o comportamento
  errado (crédito visível). Reescrever para exigir:
  cada resposta aparece exatamente uma vez; `nebli-io-answers` não existe;
  `nebli-source` não aparece no HTML de revisão; `Source` continua preenchido.

**Aceite:** re-render dos 7 IO do lote produz resposta sem concatenação e sem
crédito; um manifesto sem `prompt` falha a instalação em vez de instalar em
inglês.

### Fase 5 — Preview de IO verificável

**Muda:** `flashcards/scripts/validar_deck_card_a_card.py`,
`flashcards/scripts/validar_manifesto_visual.py`, `docs/canon/VISUAL-E-IO.md`.

Hoje `visual_review` é seis booleanos que o agente escreve. Passam a ser exigidos:

- preview real de pergunta e de resposta (arquivo), com hash de cada um;
- crop utilizado e sua proporção em relação ao slide de origem — recorte
  ≥ 90% do slide reprova (IO não é "o slide inteiro com uma caixa");
- lista de termos que não podem aparecer fora das máscaras, conferida por OCR ou
  varredura de texto do recorte;
- `pair_rationale` que nomeie a relação funcional entre os dois rótulos —
  "Anterior/superficial + Patient right" reprova por par incoerente.

**Aceite:** um IO cujo título contenha a resposta é bloqueado mesmo com
`no_leak: true` declarado.

### Fase 6 — Feedback que sobrevive e vira teste

**Muda:** `android-companion/.../AnkiBridge.java`,
`android-companion/.../FullDeckInstaller.java`,
`flashcards/scripts/ler_comentarios.py`, novo
`flashcards/tests/feedback_regressions.json`.

**6a. Modelos v2 com campo de feedback.**

`NEBLI Cloze v2` e `NEBLI Image Occlusion v2`, ambos com
`NEBLI_Comentario`, `NEBLI_Resposta` e `NEBLI_Historico`. `NEBLI_Historico` não
renderiza na revisão; serve ao navegador e à auditoria.

**6b. Atualização preserva feedback.**

Antes de `deleteOwnNote()`, capturar `NEBLI_Comentario`, `NEBLI_Resposta`, flag e
histórico da nota existente e migrá-los para a nova. Melhor ainda: quando só o
conteúdo muda, **atualizar os campos** em vez de recriar a nota — preserva também
o scheduling.

**6c. Leitura sem depender de tag.**

`ler_comentarios.py` passa a varrer campos de feedback não vazios, com ou sem
`NEBLI_comentario::pendente`. Os 7 comentários deste `.apkg` precisam aparecer na
primeira execução.

**6d. Comentário vira regressão permanente.**

`flashcards/tests/feedback_regressions.json`, uma entrada por comentário:
comentário original, padrão de erro, exemplo reprovado, condição exigida depois
da correção. Semear com os padrões já observados:

`generic_cloze` · `multiple_plausible_answers` · `multi_word_cloze` ·
`missing_prerequisite` · `wrong_content` · `weak_extra` · `contrast_missing` ·
`label_instead_of_mechanism` · `duplicate_retrieval` · `answer_rendered_twice` ·
`source_visible_in_review` · `io_prompt_not_portuguese` · `io_comment_field_missing` ·
`feedback_lost_on_update` · `english_front` · `budget_overflow`

**Aceite:** o comentário de `-trofia` produz um teste que reprova
"trofia = crescimento" e exige a correção para "desenvolvimento"; o card de
`-filia` reprova por cloze multi-palavra e por dois `c1` na mesma nota.

### Fase 7 — Bloquear `anking` na instalação e identificar o deck

**Muda:** `android-companion/.../FullDeckInstaller.java`,
`android-companion/.../CardRules.java`, `flashcards/scripts/gerar_manifesto_ankidroid.py`.

- Com `card_source_mode = authored_only`, os ramos `anking` e `external_deck`
  lançam em vez de instalar. A infraestrutura fica preservada no código, atrás de
  `anking.status == "active"`, como manda `config/pipeline.json`.
- Toda nota instalada passa a receber `NEBLI::tier::nucleo` ou
  `NEBLI::tier::optional` e `NEBLI::concept::<concept_id>`.
- A nota `anking` já instalada em UC03 sai na regeneração da Fase 9.

**Aceite:** manifesto com `source=anking` falha a instalação; toda nota nova
carrega tier e concept.

### Fase 8 — Auditoria por aula, não por coleção

**Muda:** `flashcards/scripts/audit_apkg.py`.

```
audit_apkg.py arquivo.apkg --deck "NEBLI::UC03::P1::Imunologia::Reconhecimento inato"
```

Relatório com: contagem textual e IO; proporção de cards visualmente dependentes;
imagens por card; comentários e flags; campos de feedback ausentes; respostas
duplicadas; vazamento visual; clozes genéricos; frentes não-portuguesas; cards
sem tier; e ligação `concept_id` ↔ E1.

**Aceite:** rodando contra o `.apkg` atual com `--deck` da aula de Reconhecimento
inato, o relatório aponta 52 cards, os genéricos, o IO com resposta duplicada e
os comentários ausentes — em vez de "aprovado".

### Fase 9 — Piloto e regeneração

1. Regenerar **uma** aula (Radiologia — Princípios de RX e USG, 20 cards, a
   menor e mais autocontida) com todos os gates ligados.
2. Conferir no AnkiDroid: frentes em português, IO com prompt próprio e resposta
   única, tags de tier/concept presentes, comentário sobrevivendo a uma
   reinstalação.
3. Só depois regenerar Patologia, Organização, Recombinação e Reconhecimento
   inato — as duas últimas passando obrigatoriamente pela compressão da Fase 3.

---

## 4. Limpar as contradições do canônico

`config/pipeline.json` já está em `authored_only`, mas documentos ativos ainda
mandam consultar AnKing e criam ambiguidade para o agente:

- `docs/canon/E1.md` — "após a curadoria AnKing";
- `docs/canon/NUCLEO-DE-RETENCAO.md` — "fixar os slots antes de procurar AnKing";
- `docs/canon/PRODUTO-DECK-AULA.md` — "AnKing/decks externos consultados antes de
  autorar" na definição de pronto;
- `docs/canon/COBERTURA-E-STEP1.md` — AnKing como autoridade ativa de profundidade;
- `ERROS.md` — regras 5, 14–15, 46 e 48–50.

Mover essas regras para uma seção explicitamente condicional
("aplicável somente quando `anking.status = active`"). Elas descrevem um modo
suspenso, não o modo corrente. Manter o texto — apagar seria perder trabalho —
mas deixar inequívoco que não valem hoje.

---

## 5. O que este plano não faz

- Não altera a E1: os defeitos medidos estão no deck e nos gates. A E1 continua
  sendo a âncora e não perde conteúdo — vários cards cortados na Fase 3 (`e1_only`)
  permanecem explicados lá, apenas sem custo de revisão diária.
- Não reabilita AnKing nem decks externos. Preserva a infraestrutura, desliga o
  caminho.
- Não reescreve cards manualmente. Cards ruins saem por regeneração com gate
  ligado, não por curadoria manual — a curadoria manual foi justamente o que
  `AGENTS.md` descarta.
- Não muda o produto entregue: continuam sendo `E1.pdf` e um
  `.ankidroid.json`.

---

## 6. Ordem mínima se houver pouco tempo

Fases 1, 2 e 4 já mudam o que você vê no celular amanhã: cards em português,
clozes com resposta discriminante e IO legível. Fases 3 e 6 são o que impede a
reincidência. Fases 5, 7 e 8 fecham a auditoria.
