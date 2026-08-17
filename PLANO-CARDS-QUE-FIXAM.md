# Plano — cards que fixam o conceito, não a frase

> **Estado: fases 1–8 implementadas.** A fase 9 (regeneração das aulas) depende
> dos materiais das aulas e de um AnkiDroid real, então continua aberta. O que
> mudou está resumido em `## 7. O que foi implementado`, no fim do arquivo.


Alvo: o deck-aula parar de produzir recuperações genéricas e passar a produzir
recuperações que reconstroem o mecanismo da aula.

Base: código em `cdc3596` (HEAD de `main`, 2026-08-13) e o `.apkg` exportado em
2026-08-17.

## 0. Ler primeiro: o `.apkg` é anterior às correções

As cinco aulas do `NEBLI::UC03::P1` foram criadas **antes** do merge de #22
("Corrige formatação canônica da E1 e qualidade global dos cards"):

| Aula | Cards | Criada (BRT) |
|---|---|---|
| Bioquímica — Recombinação | 35 | 2026-08-11 13:50 |
| Imunologia — Organização do sistema imune | 20 | 2026-08-11 18:46 |
| Imunologia — Reconhecimento inato | 52 | 2026-08-12 09:14 |
| Radiologia — Princípios de RX e USG | 20 | 2026-08-13 12:27 |
| Patologia — Ferramentas do Diagnóstico | 22 | 2026-08-13 14:56 |

| Commit | Merge (BRT) |
|---|---|
| #22 qualidade de cards | 2026-08-13 16:13 |
| #23 authored-only + hash | 2026-08-13 17:46 |
| #24 rollback real | 2026-08-13 17:51 |

Nenhuma aula do lote passou pelos gates de #22/#23. **O deck é um retrato do
pipeline antigo.** Por isso este plano não usa o `.apkg` como prova de que um
defeito continua aberto — usa como *corpus de regressão* para medir os gates
atuais. Cada item abaixo foi reverificado contra o código de HEAD.

---

## 1. Estado real de cada defeito em HEAD

| # | Defeito | Status em HEAD |
|---|---|---|
| 1 | `authored_only` não bloqueava `anking`/`external_deck` na instalação | **Resolvido** por #23 |
| 2 | Idioma da frente não era medido | **Parcial** — gate existe, deixa passar 77 de 142 |
| 3 | Gate cognitivo (`cloze_role`, blind review) | **Aberto** — importado, nunca chamado |
| 4 | Teto de cards | **Parcial** — virou bloqueante, mas o default anula |
| 5 | Duplicação funcional entre cards | **Aberto** |
| 6 | IO com resposta renderizada duas vezes | **Aberto** — piorado por #22 |
| 7 | Prompt IO default em inglês | **Aberto** |
| 8 | Feedback perdido na atualização de nota | **Aberto** |
| 9 | Sem campo de comentário em card IO | **Aberto** |
| 10 | Notas sem `tier`/`concept` no AnkiDroid | **Aberto** |
| 11 | Auditoria só por coleção inteira | **Aberto** |

### 1.1 Resolvido — `authored_only` agora é enforçado

`FullDeckInstaller.java:643` rejeita qualquer `source` que não seja `authored` ou
`io`, e `:609` exige `card_source_mode=authored_only` no manifesto.
`gerar_manifesto_ankidroid.py:412` bloqueia `anking`/`external_deck` em modo
strict.

A nota `1786484788526` que está no deck UC03 com tag `NEBLI::source::anking` e
texto inglês (`What is the first step of leukocyte extravasation?`) é resíduo do
pipeline antigo. Sai na regeneração — não pede código novo.

### 1.2 Parcial — o gate de idioma existe, mas peneira grosso

`gerar_manifesto_ankidroid._validate_authored()` chama
`portuguese_front_failures()` (frente) e `portuguese_text_failures()` (Extra),
sem depender de `strict`. Isso é novo e é a correção certa: mede a frente
sozinha, então um Extra em português não mascara mais uma frente inglesa.

**O que falta.** Rodando o gate de HEAD contra as 142 frentes do lote:

```
reprovadas: 65/142
escapam:    77/142
```

Escapam justamente as frases curtas e técnicas — as mais comuns num deck médico:

- `V(D)J coding ends are joined without a homologous template by {{c1::NHEJ}}.`
- `During somatic hypermutation, AID converts cytosine into {{c1::uracil}}.`
- `Final sealing of V(D)J coding ends by NHEJ requires {{c1::ligase IV}}.`

O limiar é ≥3 palavras funcionais numa lista de 26. Uma frente inglesa de 10
palavras com dois artigos passa.

**Agravante: os dois gates discordam.** `validar_deck_card_a_card.py` — o
validador nomeado em `config/pipeline.json → final_validation.validator` — não
usa `card_cue_quality`. Ele tem o detector fraco de `canonical_cards.derived()`
(10 stopwords, sobre frente **+ Extra**), e #23 removeu o
`portuguese_front_reviewed` que #22 havia colocado. Um card pode reprovar na
geração do manifesto e passar na validação final, ou o contrário.

### 1.3 Aberto — o gate cognitivo é código morto

`card_cue_quality.semantic_cue_review_failures()` implementa o contrato real:
`cloze_role` entre os seis papéis de `config/pipeline.json`,
`blind_review_passed`, `plausible_alternatives` vazio, `lexical_leak=false`,
`ambiguity_review` com substância.

`gerar_manifesto_ankidroid.py` **importa a função na linha 30 e nunca a chama.**
`validar_deck_card_a_card.py` também não. O gate operante é
`_semantic_review_ok()`, que aprova qualquer card cujos campos `ambiguity`,
`anti_induction` e `duplicate_check` tenham 12 caracteres — três frases
quaisquer liberam o card.

É por isso que passaram 20 clozes de resposta abstrata: `time`, `size`,
`probability`, `memory`, `injury`, `replication`, `transcription`, `maturation`,
`conformation`, `receptor`, `adhesion`, `compensation`, `architecture`,
`sampling`, `sectioning`, `antibodies`, `amplitude`, `air`, `fever`, `mortality`.

Um deles é literalmente o card **reprovado** em `docs/canon/EXEMPLOS-CARDS.md`:

> canônico reprovado: `A fixação impede a autólise e preserva a {{c1::arquitetura}}`
> gerado: `Routine tissue fixation prevents autolysis and preserves {{c1::architecture}}`

A lista `GENERIC` que #23 adicionou tem 7 palavras e está em português. Além de
curta, ela é do tipo errado: bloquear vocabulário não substitui avaliar o papel
cognitivo da resposta.

### 1.4 Parcial — o teto virou bloqueante, mas se autoajusta

#23 acertou em colocar `expected <= hard_max` dentro de `result["ok"]`: antes o
orçamento era só reportado. Falta fechar o buraco do default:

```python
hard_max = int(data.get("card_budget_hard_max",
               data.get("release_gate", {}).get("card_budget_hard_max", expected)))
```

Sem o campo, o teto vira o próprio número de cards e a comparação é sempre
verdadeira. Foi assim que Reconhecimento inato instalou 52 cards com teto
canônico de 25, e Recombinação, 35.

E nada no código simula ablação — `docs/canon/NUCLEO-DE-RETENCAO.md` descreve a
revisão, mas ela é uma declaração de texto livre.

### 1.5 Aberto — duplicação funcional não é detectada

Mesma resposta cobrada duas vezes, às vezes em aulas diferentes da mesma prova:

- `electron microscopy` — `c010-morphologic-scales` e `c024-ciliary-em`;
- `constant region` — `c004-constant-effector` e `c033-class-switch`;
- `CXCL8` — `ak-il8-neutrofilo` (Organização) e `k42-cxcl8` (Reconhecimento inato);
- cisteínas das quimiocinas — `au-chemokine-families` e `k42-cisteina`,
  quase a mesma frase em duas aulas.

`duplicate_check` é texto livre preenchido pelo próprio agente. Não há comparação
de respostas normalizadas nem de `retrieval_target`, e o escopo nunca passa da
aula — os dois últimos pares cruzam aulas.

### 1.6 Aberto e piorado — Image Occlusion

#22 acrescentou os rótulos sobrepostos (`nebli-io-answer-label`) em
`IoRenderer.answerHtml()`, que era o certo, **mas não removeu a lista
`.nebli-io-answers` que já existia**. Hoje o verso mostra a resposta duas vezes:
sobre a imagem e numa lista abaixo. Em texto plano isso vira concatenação:

```
A: light chainheavy chainSlide da aula; Watson, Molecular Biology of the Gene, 7th ed.
```

O bloco `.nebli-source` também continua imprimindo o crédito na revisão, embora
ele já esteja guardado no campo `Source`. E `IoRendererTest.answerRevealsLabelsAndCredits()`
foi traduzido para português em #22 mas **continua exigindo o crédito visível** —
o teste protege o defeito.

`FullDeckInstaller.java:543` ainda tem `card.optString("prompt", "Identify the
masked labels.")`. Os 7 IO do lote caíram nesse default, o que prova que o
manifesto não trazia `prompt` — apesar de `validar_deck_card_a_card.py` listar
`io_prompt_missing` e `io_prompt_not_portuguese`.

Há ainda pares incoerentes: `Anterior/superficial` + `Patient right` — dois
rótulos sem relação funcional, contra `image_occlusion.answers_language = "pt-BR"`.

### 1.7 Aberto — o feedback morre

- `FullDeckInstaller.java:454` executa `deleteOwnNote(existing)` sempre que o hash
  muda e recria a nota do zero. Comentário, resposta, flag e histórico vão junto.
- O note type `NEBLI Image Occlusion v1` (`AnkiBridge.java:198`) tem só
  `Question`, `Answer`, `Extra`, `Source`. **Não há onde comentar um card IO.**
- `ler_comentarios.py` só enxerga notas com a tag `NEBLI_comentario::pendente`.
  Os 7 comentários reais deste `.apkg` estão em `NEBLI_Comentario` **sem** a tag —
  invisíveis ao pipeline.

Os 7 comentários, que hoje não chegam a lugar nenhum:

| Card | Comentário |
|---|---|
| `-trofia` | "trofia é desenvolvimento, não crescimento, porque atrofia não é crescimento" |
| `-filia` (eosinófilo) | "clozes com muitas palavras. conteúdo é importante, mas o card é ruim, vale reescrevê-lo" |
| `atresia` | "muito avançado com comentário fraco… poderia decompor a-tresia… o cloze também tem muitas respostas" |
| `odino-` (odinofagia) | "caard incoerente e incorret" |
| `dolico-`, `-metria`, `balan/o` | marcados sem texto |

O de `-trofia` é um erro de conteúdo apontado há semanas que continua no deck.

### 1.8 Aberto — deck instalado não é auditável

As tags gravadas em `FullDeckInstaller.java:511` são `NEBLI::card::<slug>::<id>`,
`NEBLI::hash::<16>`, `NEBLI::source::<x>` e `NEBLI::<slug>`. Não há `tier` nem
`concept_id` — `tier` só escolhe o subdeck (`:80`). Depois de instalado, não dá
para verificar no AnkiDroid se o núcleo está coberto.

`audit_apkg.py` aceita só `apkg` e `--json-out`: audita a coleção inteira. Com
547 notas (398 de Etimologia legado), os problemas das 149 notas da prova somem
na média — foi assim que a auditoria anterior devolveu "aprovado".

---

## 2. Princípio da correção

1. **O gate deixa de perguntar "o agente declarou?" e passa a perguntar "o card
   sobrevive a um teste?".** Idioma medido na frente, papel do cloze validado
   contra a frase, ablação simulada, preview de IO renderizado e conferido.
2. **Um único gate.** Hoje `gerar_manifesto_ankidroid.py` e
   `validar_deck_card_a_card.py` aplicam contratos diferentes. O segundo é o
   nomeado em `config/pipeline.json`; o primeiro é o que realmente pega inglês.
   Os dois precisam chamar o mesmo módulo.
3. **Todo comentário seu vira um teste permanente.**
4. **Um card só existe se a sua remoção causa perda nomeável.** Não é o teto que
   corta cards; é a ablação. O teto vira consequência, não meta.

---

## 3. Fases

### Fase 1 — Unificar os gates e fechar o idioma

**Muda:** `flashcards/scripts/validar_deck_card_a_card.py`,
`flashcards/scripts/card_cue_quality.py`.

- `_authored()` passa a chamar `portuguese_front_failures()` em vez do detector
  de `canonical_cards.derived()`, que mede frente + Extra juntos.
- Baixar o limiar de 3 para 2 e ampliar `ENGLISH_FUNCTION_WORDS` com
  `of, a, in, to, and, for, its, can, may, does, than, both, after, before,
  without, through, occurs, contains, leaves, produces`.
- Manter a exceção legítima: termo médico inglês isolado (`hairpins`, `pre-BCR`,
  `Ku70/Ku80`) não pode reprovar frase portuguesa. Medir só palavras funcionais.
- Corpus de regressão: as 142 frentes do lote como negativas, os exemplares de
  `docs/canon/EXEMPLOS-CARDS.md` como positivas.

**Aceite:** as 142 frentes reprovam (hoje 65); nenhum exemplar canônico reprova.

### Fase 2 — Ligar o gate cognitivo que já existe

**Muda:** `flashcards/scripts/validar_deck_card_a_card.py`,
`flashcards/scripts/gerar_manifesto_ankidroid.py`, `docs/canon/CARDS.md`.

- Chamar `semantic_cue_review_failures(card, strict=True)` nos dois lugares — a
  função já está importada em `gerar_manifesto_ankidroid.py:30` e nunca é usada.
- `cue_quality.cloze_role` vira campo obrigatório do schema, restrito aos seis
  papéis de `config/pipeline.json → cue_quality.allowed_cloze_roles`.
- Substituir `GENERIC` por regra de papel: **reprovar quando a resposta é um
  substantivo abstrato sem discriminador médico** — se a lacuna aceita `tempo`,
  `duração`, `intervalo` e `atraso`, o card não fecha. Semear com as 20 respostas
  medidas em §1.3.
- Reprovar card cuja informação discriminante está só no Extra: comparar
  `retrieval_target` com o que a frente sozinha permite recuperar.

**Aceite:** os 20 cards genéricos reprovam com motivo nomeado; um card com
resposta `discriminador` bem formada passa.

### Fase 3 — Ablação de verdade, e o teto voltando a ser teto

**Muda:** `flashcards/scripts/validar_deck_card_a_card.py`,
`docs/canon/NUCLEO-DE-RETENCAO.md`.

- `hard_max` deixa de ter default igual a `expected`. Passa a derivar do tamanho
  declarado da aula (`small`/`medium`/`large` → 15/20/25 de
  `card_budget.default_hard_max`). Ausência do campo **bloqueia**.
- Cada card declara, e o gate confere que não são frases vazias:
  `memory_gain`, `ablation_loss`, `why_not_e1_only`, `confusion_target`.
- `ablation_loss` que só reformula o enunciado do card reprova: a perda precisa
  citar outro conceito ou outra recuperação do contrato.
- Detector de duplicação funcional: agrupar por resposta normalizada **e** por
  `retrieval_target`; dois cards no mesmo grupo exigem `derivation_rationale` ou
  um dos dois sai. Escopo = a prova inteira (`NEBLI::<UC>::<Prova>`), não a aula —
  foi entre aulas que CXCL8 e cisteínas duplicaram.

**Aceite:** rodar contra o lote bloqueia Reconhecimento inato (52 > 25) e
Recombinação (35 > 25) e nomeia os 4 pares duplicados de §1.5.

### Fase 4 — Consertar Image Occlusion

**Muda:** `IoRenderer.java`, `FullDeckInstaller.java`, `IoRendererTest.java`.

- `answerHtml()` emite **só** a imagem com os rótulos sobrepostos. Remover o
  bloco `.nebli-io-answers` (que #22 deixou para trás) e o bloco `.nebli-source`.
- O crédito continua no campo `Source` e some da revisão.
- Remover o default `"Identify the masked labels."` de `FullDeckInstaller:543`.
  Prompt ausente ou não-português **lança**, não substitui.
- Reescrever `answerRevealsLabelsAndCredits()`, que hoje protege o defeito.
  Passa a exigir: cada resposta aparece exatamente uma vez; `nebli-io-answers`
  não existe; `nebli-source` não aparece no HTML de revisão; `Source` preenchido.

**Aceite:** re-render dos 7 IO produz resposta sem concatenação e sem crédito;
manifesto sem `prompt` falha a instalação em vez de instalar em inglês.

### Fase 5 — Preview de IO verificável

**Muda:** `validar_deck_card_a_card.py`, `validar_manifesto_visual.py`,
`docs/canon/VISUAL-E-IO.md`.

`visual_review` hoje é seis booleanos que o agente escreve. Passam a ser exigidos:

- preview real de pergunta e de resposta (arquivo), com hash de cada um;
- crop e sua proporção em relação ao slide — recorte ≥ 90% do slide reprova;
- termos que não podem aparecer fora das máscaras, conferidos por varredura de
  texto do recorte;
- `pair_rationale` que nomeie a relação funcional entre os dois rótulos —
  `Anterior/superficial` + `Patient right` reprova por par incoerente.

**Aceite:** IO cujo título contenha a resposta é bloqueado mesmo com
`no_leak: true` declarado.

### Fase 6 — Feedback que sobrevive e vira teste

**Muda:** `AnkiBridge.java`, `FullDeckInstaller.java`, `ler_comentarios.py`, novo
`flashcards/tests/feedback_regressions.json`.

**6a.** `NEBLI Cloze v2` e `NEBLI Image Occlusion v2`, ambos com
`NEBLI_Comentario`, `NEBLI_Resposta` e `NEBLI_Historico`. O histórico não
renderiza na revisão; serve ao navegador e à auditoria.

**6b.** Antes de `deleteOwnNote()`, capturar comentário, resposta, flag e
histórico e migrá-los para a nota nova. Melhor: quando só o conteúdo muda,
**atualizar os campos** em vez de recriar — preserva também o scheduling.

**6c.** `ler_comentarios.py` varre campos de feedback não vazios, com ou sem a
tag `NEBLI_comentario::pendente`. Os 7 comentários deste `.apkg` precisam
aparecer na primeira execução.

**6d.** `feedback_regressions.json`, uma entrada por comentário: comentário
original, padrão de erro, exemplo reprovado, condição exigida depois da correção.
Padrões já observados:

`generic_cloze` · `multiple_plausible_answers` · `multi_word_cloze` ·
`two_clozes_same_note` · `missing_prerequisite` · `wrong_content` · `weak_extra` ·
`label_instead_of_mechanism` · `duplicate_retrieval` · `answer_rendered_twice` ·
`source_visible_in_review` · `io_prompt_not_portuguese` · `io_comment_field_missing` ·
`feedback_lost_on_update` · `english_front` · `budget_overflow`

**Aceite:** o comentário de `-trofia` produz um teste que reprova
"trofia = crescimento"; o de `-filia` reprova por cloze multi-palavra e por dois
`c1` na mesma nota.

### Fase 7 — Identidade da nota instalada

**Muda:** `FullDeckInstaller.java`.

Toda nota passa a receber `NEBLI::tier::nucleo` ou `NEBLI::tier::optional` e
`NEBLI::concept::<concept_id>`, junto das tags que já existem em `:511`.

*(O bloqueio de `anking`/`external_deck` que estava previsto aqui já foi feito
por #23 — ver §1.1.)*

**Aceite:** toda nota nova carrega tier e concept; auditoria consegue cruzar deck
instalado com contrato de cobertura.

### Fase 8 — Auditoria por aula, não por coleção

**Muda:** `audit_apkg.py`.

```
audit_apkg.py arquivo.apkg --deck "NEBLI::UC03::P1::Imunologia::Reconhecimento inato"
```

Relatório com: contagem textual e IO; proporção de cards visualmente dependentes;
imagens por card; comentários e flags; campos de feedback ausentes; respostas
duplicadas; vazamento visual; clozes genéricos; frentes não-portuguesas; cards
sem tier; ligação `concept_id` ↔ E1.

**Aceite:** com `--deck` de Reconhecimento inato, o relatório aponta 52 cards, os
genéricos, o IO com resposta duplicada e os comentários ausentes — em vez de
"aprovado".

### Fase 9 — Piloto e regeneração

1. Regenerar **uma** aula — Radiologia (20 cards, a menor e mais autocontida) —
   com todos os gates ligados.
2. Conferir no AnkiDroid: frentes em português, IO com prompt próprio e resposta
   única, tags de tier/concept, comentário sobrevivendo a uma reinstalação.
3. Só depois: Patologia, Organização, Recombinação e Reconhecimento inato — as
   duas últimas passando obrigatoriamente pela compressão da Fase 3.

---

## 4. Limpar as contradições do canônico

`config/pipeline.json` está em `authored_only` e o Companion já enforça isso, mas
documentos ativos ainda mandam consultar AnKing:

- `docs/canon/E1.md:99` — "Após a curadoria AnKing, executar o passe card → E1";
- `docs/canon/NUCLEO-DE-RETENCAO.md:12` — "fixar os slots antes de procurar AnKing";
- `docs/canon/PRODUTO-DECK-AULA.md:33` — "AnKing/decks externos consultados antes
  de autorar", na definição de pronto;
- `docs/canon/COBERTURA-E-STEP1.md:7` — AnKing como autoridade ativa de profundidade;
- `ERROS.md` — as regras de busca, cópia e resolução AnKing.

Mover para uma seção explicitamente condicional ("aplicável somente quando
`anking.status = active`"). Manter o texto — apagar seria perder trabalho — mas
deixar inequívoco que não vale hoje. Enquanto o canônico disser uma coisa e o
código outra, o agente escolhe.

---

## 5. O que este plano não faz

- Não altera a E1. Os defeitos estão no deck e nos gates. Cards cortados na
  Fase 3 (`e1_only`) continuam explicados lá, só sem custo de revisão diária.
- Não reabilita AnKing nem decks externos.
- Não reescreve cards manualmente. Card ruim sai por regeneração com gate ligado,
  não por curadoria manual — que é justamente o que `AGENTS.md` descarta.
- Não muda o produto entregue: continuam `E1.pdf` e um `.ankidroid.json`.

---

## 6. Ordem mínima se houver pouco tempo

Fases 1, 2 e 4 mudam o que você vê no celular na próxima aula: frente em
português, cloze com resposta discriminante, IO legível. Fases 3 e 6 são o que
impede a reincidência. Fases 5, 7 e 8 fecham a auditoria.

---

## 7. O que foi implementado

Fases 1–8 estão no código. A fase 9 continua aberta: regenerar uma aula exige os
materiais dela e um AnkiDroid real, que não existem nesta execução.

### Medição, antes e depois

Rodando os gates contra as 142 frentes textuais do `NEBLI::UC03::P1`:

| Gate | Antes | Depois |
|---|---|---|
| Frentes inglesas reprovadas | 65 de 142 | **142 de 142** |
| Frentes portuguesas com termo médico inglês reprovadas por engano | — | **0 de 13** |
| Clozes de resposta abstrata reprovados | 0 | **20** |

A auditoria por aula, que antes devolvia "aprovado" para a coleção inteira:

```
$ audit_apkg.py NEBLI-20260817.apkg --deck "NEBLI::UC03::P1::Radiologia::Princípios de RX e USG"
  19 frentes não estão em português
  5 clozes têm resposta abstrata
  1 cards IO repetem a resposta abaixo da imagem
  1 cards IO imprimem o crédito na resposta
  20 notas sem tag NEBLI::tier
  20 notas sem tag NEBLI::concept
```

### Por fase

**1. Idioma.** `validar_deck_card_a_card` passou a usar
`card_cue_quality.portuguese_front_failures`, que mede **só a frente**. Lista de
marcadores ampliada de 17 para 76 palavras e limiar de 3 para 2, mantendo fora
artigos e preposições portuguesas para não acusar frase correta. `CardRules.java`
recebeu a mesma lista e o mesmo limiar.

**2. Gate cognitivo.** `semantic_cue_review_failures` era importada e nunca
chamada; agora roda em `strict=True` dentro de `validate_card`, que o gerador de
manifesto também usa. A lista `GENERIC` de 7 palavras virou `ABSTRACT_ANSWERS`
bilíngue semeada com as 20 respostas medidas. Novo: `discriminator_only_in_extra`,
que reprova o card cuja informação decisiva mora no verso.

**3. Ablação e orçamento.** `card_budget_hard_max` deixou de cair para
`expected`: ausente, bloqueia. Cada card declara `memory_gain`, `ablation_loss`,
`why_not_e1_only` e `confusion_target`, e uma perda que só reformula o card
reprova. Duplicação funcional é detectada por resposta normalizada e por
`retrieval_target`.

**4. Image Occlusion.** `IoRenderer.answerHtml` perdeu a lista repetida e o bloco
de crédito — e perdeu também o parâmetro `sourceCredit`, para que o renderer não
tenha como vazar a fonte. O prompt default `"Identify the masked labels."` saiu:
prompt ausente ou inglês agora lança. `IoRendererTest.answerRevealsLabelsAndCredits`,
que exigia o crédito visível, foi substituído por dois testes que exigem o
contrário.

**5. Prova visual.** `visual_evidence` passou a ser obrigatório: dois previews
com hash, `crop_ratio` (recorte ≥ 90% do slide reprova), varredura de texto,
`forbidden_terms` cobrindo todas as respostas e `leaked_terms` vazio. Um IO com
`no_leak: true` e vazamento real agora reprova.

**6. Feedback.** `ModelFields` ganhou leitura, migração e histórico do feedback;
`installOne` lê o comentário **antes** do `deleteOwnNote` e o reescreve na nota
nova, registrando `feedback_carried`/`feedback_lost` no recibo. O note type IO
subiu para v2 com `NEBLI_Comentario`, `NEBLI_Resposta` e `NEBLI_Historico`.
`ler_comentarios.py` procura campo preenchido além da tag — e **nunca apaga o
comentário** ao responder, conforme pedido.

**7. Identidade.** Toda nota instalada recebe `NEBLI::tier::<tier>` e
`NEBLI::concept::<concept_id>`.

**8. Auditoria.** `audit_apkg.py --deck` limita o escopo a uma aula. No caminho,
apareceu um defeito maior: `apkg_utils.models_map` não populava campos no schema
novo do Anki, então a auditoria estava **estruturalmente cega** em qualquer
`.apkg` recente — nenhuma análise de campo rodava. Corrigido na raiz.

### Comentários: eram 9, não 7

A leitura por flag encontrava 7; a leitura por campo encontra **9**. Dois
comentários nunca tiveram flag e por isso eram invisíveis das duas formas.
Todos os 9 viraram entradas de `flashcards/tests/feedback_regressions.json`, e
`test_feedback_regressions.py` roda cada exemplo reprovado contra o gate real:
uma entrada que não bloqueia o próprio exemplo quebra o teste.

Três comentários geraram gates que não estavam no plano original:

- *"é horrível que haja x ou y, o certo é que haja uma palavra só"* →
  `cloze_answer_offers_alternatives`, com escape via `compound_answer_reason`
  para nome composto legítimo (RAG1/RAG2);
- *"não sei o que é evaginação sacular"* / *"não compreendi esse"* →
  `answer_not_in_e1_anchor`: o termo cobrado precisa existir na âncora da E1;
- *"não apaga eles, vai mantendo, mesmo que estejam corrigidos"* → `responder`
  preserva o comentário e acumula as respostas.

### O que não foi verificado aqui

O código Android **não foi compilado**: não há Android SDK neste ambiente.
`IoRenderer`, `CardRules` e `ModelFields` não dependem de Android e foram
compilados e exercitados por um harness próprio; `FullDeckInstaller` e
`AnkiBridge` foram alterados sem compilação. Rodar `gradle test` antes de gerar
o APK.

`NEBLI Cloze v2` não foi criado: um note type de cloze não pode ser criado de
forma confiável pelo ContentProvider do AnkiDroid. Em vez de fabricar a
capacidade, `findClozeModel` passou a **preferir** um note type que já tenha os
campos de feedback, e o recibo registra quando o feedback se perde por falta de
campo.
