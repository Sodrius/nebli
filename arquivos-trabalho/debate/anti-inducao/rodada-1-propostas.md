# Rodada 1 — Propostas do PROPOSITOR

> Papel: Inovador. Instinto: gerar MUITAS regras concretas e implementáveis para `lint_neblicard.py`. Não defendo status quo. Cada proposta é uma heurística barata, determinística (regex/contagem/overlap), sem chamada de LLM — isso é o que separa o linter do card-mirror. O Extra explicativo NUNCA é punido (feature deliberada, _CONTEXTO §28).
>
> Regra-mãe respeitada: cada proposta traz um exemplar/métrica real como âncora (evidence-admission).
>
> Convenção de parse assumida (todas as regras operam sobre isto):
> - `Text` = campo da frente com cloze. `stem` = Text com os spans `{{cN::...}}` removidos (o que o aluno LÊ antes de responder). `answer(N)` = conteúdo dentro de `{{cN::resposta::hint}}` (resposta, sem a hint). `hint(N)` = a parte após o 2º `::`, se existir.
> - `content_words(x)` = tokens de `x` após remover stopwords EN + pontuação. Base de stopwords pequena e fixa embutida no script.
> - Todas as regras rodam por-cloze e por-card; o card acumula flags/rejeições.

---

## P1. NAME-in-stem overlap (root-match stem↔answer)

- **Detects:** Padrão 1 (NAME-in-stem leak) + Padrão 4 (auto-entrega da sigla). O caso canônico ERRADO do _CONTEXTO §14: `O neurônio **multipolar** tem {{c1::vários dendritos...}}` — a palavra-chave da resposta (ou sua raiz) já está impressa no stem.
- **Rule (implementable):**
  1. Para cada `answer(N)`, extrair as content-words e reduzir cada uma à raiz por um stemmer barato determinístico (Porter/Snowball via `nltk`/`snowballstemmer`, ou um truncamento a 5 chars se quiser zero-dep).
  2. Fazer o mesmo com o `stem`.
  3. Se qualquer raiz de content-word de `answer(N)` (comprimento ≥4 chars, para não pegar "of"/"is") aparece no conjunto de raízes do `stem` → LEAK.
  - Pseudo: `leaked = {stem(w) for w in cw(answer)} & {stem(w) for w in cw(stem_text)}; if any(len(r)>=4 for r in leaked): flag`
- **Signal → action:** REJECT (hard gate) se a raiz compartilhada for a **head-word** da resposta (última content-word do span, heurística de núcleo em EN). FLAG se for uma content-word não-núcleo.
- **Evidence:** Nenhum dos 50 AnKing repete a raiz da resposta no stem. AK-05 pergunta "tumor from point mutation of KIT" → resposta `GIST`; a palavra "GIST"/"stromal" não está no stem. AK-29 "rate-limiting enzyme for cholesterol synthesis" → `HMG-CoA reductase`; "reductase" não vaza. O anti-exemplar do próprio _CONTEXTO é literalmente este caso.
- **Known false-positive risk:** AK-25 `Chronic primary adrenal insufficiency, also known as {{c1::Addison}} disease` — aqui "disease" fica no stem mas a resposta é "Addison", raiz distinta, então passa. Risco real: AK-33 `Reid index is > {{c1::50}}% (normal is < {{c1::40}}%)` — números, sem raiz textual, seguro. O risco genuíno é o **aposto legítimo** onde o stem repete um termo genérico da resposta (ex.: resposta `venous insufficiency ulcer` com "ulcer" já no stem em AK-44 — mas ali "ulcer" NÃO está no stem, checar). Mitigar exigindo raiz ≥4 chars e ignorando as 200 palavras médicas mais genéricas (disease, syndrome, cell, acid) via stoplist de domínio.

---

## P2. Cloze-length / dump gate (token vs frase-mecanismo)

- **Detects:** Padrão 3 (cloze-dump) + Tell nº2 (cloze de frase-mecanismo ≥5 palavras). O ideal AnKing é branco de 1–3 palavras-conteúdo (_CONTEXTO §18, §34).
- **Rule (implementable):** Para cada `answer(N)`, contar `content_words`. 
  - `cw ≤ 3` → OK.
  - `4 ≤ cw ≤ 6` → FLAG (zona cinza; pode ser nome próprio composto legítimo).
  - `cw ≥ 7` → REJECT, **exceto** se o card for reconhecido como enumeração/mnemônico multi-cloze (ver exceção abaixo).
  - Exceção anti-falso-positivo: se o card tem ≥4 clozes distintos (c1..c4) OU o span casa um padrão de "resposta canônica longa entre parênteses" (nome de doença + sigla), relaxar o teto para 8.
- **Signal → action:** REJECT em `cw ≥ 7` (single-ish cloze); FLAG em 4–6.
- **Evidence:** Distribuição real dos 50: a esmagadora maioria dos single-clozes é 1–3 content-words (AK-04 `Hiatal`, AK-08 `ipsi`, AK-30 `capillary`, AK-49 `II`). Os longos legítimos são nomes próprios canônicos: AK-26 `Developmental dysplasia of the hip (DDH)` (~4 cw), AK-24 `5-HT3 receptor antagonists (e.g., ondansetron)`. O tell nº2 do lote cego P3 marca frase-mecanismo de 5+ palavras como não-nativo.
- **Known false-positive risk:** AK-34 `No, they present as a wide QRS` (~5 cw) e AK-45 `You're not going to leave the person with enough lung` (~8 cw!) são AnKing REAIS e passariam batido do teto. Estes são cards conversacionais/explicativos — o linter os REJEITARIA erroneamente. Mitigação: a exceção de enumeração não os cobre; é o furo honesto mais grave desta regra e o Cético vai atacar aqui. Possível patch: só REJECT se o span longo também dispara P1 (overlap com stem) ou P6 (mecanismo no stem) — comprimento sozinho vira FLAG, não REJECT.

---

## P3. Sigla-com-expansão-na-mesma-frase (self-give sigla)

- **Detects:** Padrão 4 (auto-entrega da sigla) + Tell nº3 (cloze que se auto-entrega). Anti-exemplar _CONTEXTO §19: `Mucosa-associated lymphoid tissue is {{c1::MALT}}`.
- **Rule (implementable):**
  1. Detectar se `answer(N)` é uma sigla: regex `^[A-Z][A-Za-z0-9\-]{1,7}$` com ≥2 maiúsculas OU casa o padrão de acrônimo (todas iniciais maiúsculas).
  2. Extrair as iniciais da sigla (letras maiúsculas de `answer`).
  3. No `stem`, procurar uma sequência de palavras cujas **iniciais em ordem** reproduzam a sigla (`Mucosa Associated Lymphoid Tissue` → M-A-L-T). Algoritmo: sliding window sobre content-words do stem; para cada janela de tamanho = nº de letras da sigla, comparar iniciais.
  4. Match → auto-give.
- **Signal → action:** REJECT (hard). É um leak inequívoco e o algoritmo tem baixíssimo falso-positivo.
- **Evidence:** AK-05 faz o CERTO ao contrário — a expansão `Gastrointestinal stromal tumor (GIST)` está DENTRO do cloze (na resposta), não no stem. AK-26 idem: `Developmental dysplasia of the hip (DDH)` toda no cloze. O padrão nativo põe sigla+expansão juntas *na resposta*; o leak põe a expansão no *stem* e a sigla no *branco*.
- **Known false-positive risk:** Baixo. Único risco: sigla curta (2 letras) casando iniciais por acaso (ex.: resposta `II` de AK-49 casaria qualquer "I... I..."). Mitigar exigindo sigla ≥3 letras e a janela do stem ser contígua e temática. AK-31 `macrophages` não é sigla → não dispara.

---

## P4. Parêntese/aposto que entrega (parenthetical give)

- **Detects:** Padrão 2 (parêntese/aposto que entrega — "três cúspides → tricúspide").
- **Rule (implementable):**
  1. Extrair todo conteúdo entre parênteses no `stem` (fora de qualquer cloze): `\(([^)]*)\)`.
  2. Para cada parêntese, computar overlap de raízes (via P1) e overlap semântico-numérico com `answer(N)`:
     - se contém um **número por extenso ou dígito** que também é a resposta (three→tri, 3→tri) → checar tabela pequena de prefixos numéricos {mono/uni/1, bi/di/2, tri/3, tetra/quad/4, penta/5...} contra a raiz da resposta;
     - se compartilha raiz com a resposta (P1 restrito ao texto do parêntese).
  3. Qualquer match → leak via aposto.
- **Signal → action:** FLAG por padrão; REJECT se casar o mapa de prefixo numérico (é o caso canônico e determinístico).
- **Evidence:** AK-07 usa parêntese `(primitive pharynx)` que NÃO entrega o branco `thyroglossal` — parêntese legítimo. AK-13 usa `(pyrimidine synthesis)`/AK-19 idem — contexto, não give. O leak descrito no _CONTEXTO ("três cúspides → tricúspide") é exatamente o que a tabela de prefixos captura sem ambiguidade.
- **Known false-positive risk:** Parênteses de contexto/exemplo legítimos são MUITO comuns no AnKing (AK-07, AK-13, AK-19, AK-24 `(e.g., ondansetron)`, AK-40 `::drug`). A regra deve punir SÓ overlap de raiz/número com a resposta, não a mera presença de parêntese. AK-24 tem `(e.g., ondansetron)` DENTRO do cloze (resposta), não no stem → não dispara. O risco fica no parêntese de stem que casualmente contém a raiz — manter em FLAG, não REJECT, salvo o mapa numérico.

---

## P5. Answerability por baixa entropia do stem (BOLD — heurística de "cabe muita coisa?")

- **Detects:** A pergunta-mãe direta — "dá pra acertar o branco sem saber a matéria?" (_CONTEXTO §11). Recognition vs recall: um stem que *restringe demais* a resposta é adivinhável.
- **Rule (implementable):** Heurística de "gramatical forcing" — quanto o stem força a resposta por pura sintaxe/colocação, sem conhecimento:
  1. Se o cloze é **a última coisa da frase** e o stem termina numa colocação fixa que quase só admite uma classe de palavra, penalizar. Proxy determinístico: computar `blank_ratio = len(content_words(stem)) / (len(content_words(stem)) + Σ cw(answers))`. Stem muito longo com branco atômico curto no fim → forte contexto → provável recognition. `blank_ratio > 0.90` → FLAG "stem-heavy".
  2. Combinar com detector de **frase declarativa sem pergunta**: se o `stem` NÃO contém `?` E o cloze está no fim E `blank_ratio > 0.9` → o cloze provavelmente completa uma afirmação que o próprio contexto já determina → FLAG.
  3. Bônus barato: se a content-word imediatamente ANTES do cloze é um adjetivo/artigo que colige fortemente (heurística por lista de "give-collocations": "known as", "called the", "so-called", "namely", "i.e.") → REJECT (o stem anuncia a definição).
- **Signal → action:** FLAG para o blank_ratio; REJECT só para as give-collocations ("known as {{c1::...}}", "i.e., {{c1::...}}").
- **Evidence:** AK-25 `also known as {{c1::Addison}} disease` — este é AnKing REAL e usa "known as"! Logo a sub-regra 3 tem de ser calibrada: "known as X disease" é nativo quando X é um nome próprio não-derivável. O tell nº1 real (mecanismo dentro do stem) é a versão forte disto: stem que carrega o conteúdo e deixa o token trivial. Este é o proxy determinístico para o card-mirror caro.
- **Known false-positive risk:** ALTO e assumido — é a regra mais especulativa. AK-25 e AK-04 (`{{c1::Hiatal}} hernias are found in about half...`) têm blank_ratio alto e são nativos. Por isso blank_ratio fica em FLAG (nunca REJECT) e serve como *tie-breaker* que empurra o card ao card-mirror, não como gate. O Cético vai (com razão) dizer que isto quase-vira o card-mirror; contra-argumento: é barato e só sinaliza, não reprova.

---

## P6. Mecanismo-no-stem (tell nº1 — o separador mais confiável) via densidade de verbos causais

- **Detects:** Tell nº1 (mecanismo dentro do STEM da frente) — _CONTEXTO §22: "sealing passively by their nest shape DENTRO da pergunta". Descrito como o **separador mais confiável**. Nenhum dos 50 AnKing faz isso.
- **Rule (implementable):** Detectar que o STEM (não a resposta) carrega a explicação mecanística:
  1. Contar no `stem` marcadores causais/mecanísticos de uma lista fixa: `because, due to, leads to, results in, causes, via, by, so that, thereby, in order to, passively, actively, allowing, resulting, mediated by, driven by`.
  2. Contar particípios/gerúndios "-ing/-ed by" que descrevem processo no stem.
  3. Se o stem tem ≥2 marcadores causais E o cloze é curto/atômico → o card ensina o mecanismo na frente e testa um rótulo trivial → indução. Se o stem tem ≥1 marcador causal DENTRO do fragmento que precede imediatamente o cloze → forte.
- **Signal → action:** REJECT se ≥2 marcadores causais no stem com cloze atômico (≤3 cw); FLAG se exatamente 1.
- **Evidence:** Varredura dos 50: AnKing põe o mecanismo no **Extra** ou no **cloze**, quase nunca no stem-antes-do-branco. AK-28 `Retinal {{c1::detachment}} is due to separation...` — aqui "due to" vem DEPOIS do cloze (o mecanismo é o distrator, não a pista); o branco `detachment` vem antes de "is due to". Contraste com o anti-padrão do _CONTEXTO onde o mecanismo antecede e entrega o branco. AK-11 `oxidative burst also leads to an influx of {{c1::K+}}` — "leads to" precede o branco, mas o branco é um íon específico não-derivável do mecanismo → mostra que **1 marcador sozinho não basta** (por isso o teto é ≥2, e 1 vira FLAG).
- **Known false-positive risk:** AK-28, AK-11, AK-15 (`osmotic damage may occur when glucose... converted to sorbitol by aldose reductase` — cheio de "by/when") são nativos e têm marcadores causais no stem. Este é o risco central: o AnKing SIM usa linguagem causal no stem quando a resposta é um fato não-derivável. Mitigação obrigatória: P6 só REJECT quando **combinado com P1/P5** (mecanismo no stem E baixa entropia E/ou overlap) — sozinho é FLAG. Honestidade: distinguir "mecanismo que entrega" de "mecanismo que é contexto" é justamente o que o card-mirror LLM faz melhor; P6 é o proxy barato, aceitando recall reduzido.

---

## P7. Bold/emphasis-no-stem casando a resposta

- **Detects:** Padrão 1 na sua forma PIOR — _CONTEXTO §14: "nome da estrutura aparece no stem (pior: em **negrito**)". A ênfase visual grita o branco.
- **Rule (implementable):**
  1. No `Text` cru (antes de strip de cloze), detectar spans enfatizados: `<b>...</b>`, `<strong>`, `**...**`, `<i>` que estejam FORA de qualquer `{{cN::}}`.
  2. Para cada span enfatizado no stem, computar overlap de raízes (via P1) com cada `answer(N)`.
  3. Overlap de raiz ≥4 chars entre bold-do-stem e resposta → leak amplificado.
- **Signal → action:** REJECT. Bold no stem que casa a resposta é o pior caso nomeado explicitamente; near-zero falso-positivo porque exige ênfase E overlap.
- **Evidence:** O anti-exemplar literal do _CONTEXTO §14 (`neurônio **multipolar**` com o cloze na descrição) é exatamente isto. Nos 50 AnKing, a ênfase (quando existe, ex.: AK-10 usa itálico decorativo em "Tay's") nunca casa a raiz da resposta apagada — é decorativa/mnemônica, não uma pista do branco.
- **Known false-positive risk:** Muito baixo. Risco: bold usado para destaque didático legítimo cujo termo por acaso reaparece na resposta em outra função gramatical. Como exige overlap de raiz ≥4 chars (P1) além da ênfase, o falso-positivo é raro. Se o span enfatizado É o próprio cloze (ênfase dentro do `{{}}`), a regra ignora — só olha ênfase no stem.

---

## P8. Multi-cloze com irmão-vizinho que entrega (cross-cloze leak)

- **Detects:** Variante de Padrão 1/2 em cards multi-cloze — quando um cloze aparece ao lado de outro cloze cuja resposta (ou o texto visível quando aquele cloze está escondido) pré-determina o vizinho.
- **Rule (implementable):**
  1. Só roda em cards com ≥2 clozes.
  2. Para cada par (cN, cM), verificar se `answer(N)` e `answer(M)` compartilham raiz (P1) — respostas gêmeas costumam ser um comparativo onde ver um lado entrega o outro (hyper/normo, increase/decrease).
  3. Verificar também se o texto FIXO entre dois clozes contém uma give-collocation ("and", "or", "such as") que os funde num par óbvio de complementaridade + se as respostas são antônimos de uma lista fixa {increase/decrease, high/low, yes/no, hyper/hypo, ipsi/contra, sensitivity/specificity}.
  4. Par antônimo complementar adjacente → FLAG (o aluno acerta por eliminação/paralelismo, não por recall).
- **Signal → action:** FLAG (não REJECT — é uma forma sutil de recognition, e há nativos que fazem isso deliberadamente).
- **Evidence:** AK-23 `{{c1::hyper}}calciuria and {{c1::normo}}calcemia` e AK-36 `Sensitivity: {{c1::increase}} Specificity: {{c1::decrease}} PPV: {{c1::decrease}} NPV: {{c1::increase}}` — AnKing REAL com pares antônimos complementares. Logo esta regra NÃO pode ser REJECT; é apenas um sinal fraco que soma pontos para empurrar ao card-mirror.
- **Known false-positive risk:** ALTO e reconhecido — AK-23 e AK-36 são exatamente este padrão e são nativos e bons (usam `::hint` para desambiguar, aliás). Por isso: FLAG-only, peso baixo, e isentar quando todos os clozes do par usam `::hint` (sinal de craft deliberado). Serve mais como métrica de auditoria de lote do que como gate.

---

## P9. Score composto de indução + política de gate (o "cérebro" do linter)

- **Detects:** Todos os 4 padrões + 3 tells, agregados. Resolve o problema de que nenhuma regra sozinha é confiável (P5/P6/P8 têm FP alto; P1/P3/P7 são duros).
- **Rule (implementable):** Cada regra emite `(peso, sinal)`. Score do card = soma dos pesos disparados. Pesos sugeridos (calibráveis):
  - Hard-REJECT imediato (qualquer um trava o card, score irrelevante): P3 (sigla self-give), P7 (bold+overlap), P1-headword, P4-numérico, P6 (≥2 causais + cloze atômico).
  - Soft-pontos: P1-nonhead=2, P2-flag(4–6cw)=1, P2-reject(≥7cw)=3, P4-flag=1, P5-blankratio=1, P5-collocation=3, P6-1causal=2, P8=1.
  - Política: score ≥5 → REJECT; 3–4 → **manda pro card-mirror** (não fecha nem reprova sozinho); ≤2 → passa direto (fecha). Assim o linter barato descarta o lixo óbvio (o ~45% de reconhecimento do P3) e só o resíduo cinza custa LLM.
- **Signal → action:** É a orquestração: define REJECT / SEND-TO-MIRROR / PASS.
- **Evidence:** O diagnóstico-mãe (_CONTEXTO §10) é ≈45% dos cards = reconhecimento; um gate barato que pega os casos duros (P1/P3/P7) já corta a maior fatia antes do LLM caro. O deck P3 saiu 6/10 — o objetivo do gate é subir isso sem rodar card-mirror em 100% dos cards.
- **Known false-positive risk:** O risco agregado é herdado das regras-membro; a mitigação é estrutural — **só P1/P3/P4-num/P6-forte/P7 podem REJECT sozinhas** (são as de baixo FP), e tudo que é FP-alto (P5/P6-fraco/P8/P2-longo-conversacional) só contribui pontos que, no máximo, mandam pro card-mirror — nunca reprovam um AK-45/AK-34/AK-25 sozinhas. O Cético deve verificar que nenhum dos 50 AnKing atinge score ≥5 com esta calibração (teste de regressão obrigatório: rodar o linter nos 50 do dossiê; zero REJECT esperado).

---

## Nota de fechamento (auto-red-team honesto)

- As regras **duras e seguras** (baixo FP) são P1 (headword), P3, P4-numérico, P7. Recomendo que só essas quatro sejam gate hard no dia 1.
- As **arriscadas mas valiosas** são P5 e P6 — capturam o tell nº1 (o mais discriminador) mas por proxy grosseiro; ficam como FLAG/pontos até calibradas contra os 50.
- **Teste de regressão inegociável:** rodar `lint_neblicard.py` sobre os 50 cards do `ANKING-DOSSIE-TEXTO.md`. Meta: **zero REJECT** entre os 50 nativos. Qualquer nativo reprovado = a regra que o reprovou volta pra prancheta. AK-34, AK-45, AK-25, AK-23, AK-36 são os canários (os nativos que mais parecem induzidos).
