# TEMA CARD — Regulação hormonal do metabolismo e da massa corpórea

## Seção A — Escopo

- **Tema:** Regulação da massa corpórea
- **Título de capa:** "Regulação da massa corpórea"
- **Slug:** `regulacao-massa-corporea`
- **Disciplina:** Bioquímica / Fisiologia do metabolismo (2º semestre)
- **Docente do slide:** deborah@iq.usp.br (IQ-USP) — sigla não confirmada em cronograma; **não vai ao PDF** (proibição canônica de identificar aula/bloco).
- **Onde estudar:** Lehninger, *Princípios de Bioquímica* (7ª ed.), cap. 23 — Regulação hormonal e integração do metabolismo; Stryer/Berg/Tymoczko, *Bioquímica* (7ª ed.). (Ambos aparecem no slide de fechamento do professor.)
- **Alvo de páginas E1:** piso 2, **teto 22**. Alvo desta corrida: 16–20.
- **Profundidade (dial):** `padrao` (o padrão elevado de 2026-07-12). Tema tem cadeia mecanística longa e rendimento clínico alto — aprofundar dentro do escopo do slide, sem toca de coelho.
- **Distribuição E2:** PADRÃO → 10 Consolidação · 15 Integração · 5 Aplicação.

**Recorte slide × tema.** O arquivo se chama "Regulação da massa corpórea", mas o slide 1 declara o título completo: *Regulação hormonal do metabolismo **e** da massa corpórea*. O slide abre com um bloco geral de coordenação neuroendócrina (eixo hipotálamo-hipófise, cascata hormonal, resposta adrenérgica ao estresse) e só então entra em massa corpórea (lipostática → leptina → adipocinas → circuito hipotalâmico → peptídeos gastrointestinais → farmacologia). **Decisão:** o resumo cobre os dois — a coordenação neuroendócrina entra como PARTE I porque é o alicerce mecanístico de tudo que vem depois (sem entender cascata + retroalimentação negativa, leptina vira nome solto). Slides 8 (lista de doenças endócrinas) e 5 (mapa hipófise em espanhol) ficam de fora por baixa utilidade pedagógica.

**Aula fora do banco.** Nenhuma entrada correspondente em `banco/aulas_uc01.yml` nem `aulas_uc02.yml`; UCs do 2º semestre (UC-16, UC-8) ainda não têm `aulas_ucNN.yml` nem banco de provas. Calibração vem, portanto, de: slide + bibliografia declarada (Lehninger cap. 23) + régua de profundidade do blueprint (linha vizinha `histo-05-tecido-adiposo`: leptina, UCP1/termogênese, obesidade — rendimento MÉDIO-ALTO).

**Prioridades desta corrida (do § Diário de revisões do MEMORY.md):**
1. **`2026-05-29 · biocel-07-divisao-celular` (peso alto, viva):** resumo fechado sem nenhuma figura. Aqui o risco é o inverso — o slide é quase todo visual —, mas a lição operante é a mesma: **cadeia mecanística espacial exige figura adjacente**. Vale para o eixo leptina→SNS→β3→PKA→lipólise/UCP1 e para o circuito arqueado→PVN/LHA. Meta: ≥3 figuras por PARTE, com largura deliberada caso a caso.
2. **Erro #12 (cadeia ≥4 setas sem figura)** — este tema é uma sucessão de cascatas; conferir por parágrafo.
3. **Erro #20 (`#termo-nota` com o termo repetido na prosa)** — auto-check antes de fechar.
4. **Erro #16 / F3 (excesso de caixa vermelha)** — cota 1–2 boxes de confusão por PARTE; a confusão "leptina alta = mais saciedade" vira prosa encenada + `#confusao-prevista`, não vermelho.

## Seção B — Esqueleto das PARTES

### PARTE I — O balanço energético e a orquestra que o comanda (4 figuras)
- **1.1** A conta que o corpo fecha todo dia — energia consumida = utilizada + armazenada; por que o estoque é feito de gordura. *(fig: slide-11, 48%)*
- **1.2** Teoria lipostática: o estoque não é só preenchido, é medido e defendido.
- **1.3** Como um hormônio comanda: cascata, amplificação e retroalimentação negativa. *(figs: slide-04 a 42%; slide-07 a 78%)*
- **1.4** Duas velocidades de resposta: catecolaminas no susto, cortisol na privação prolongada. *(fig: slide-06, 72%)*
- **1.5** O tecido adiposo entra na orquestra como glândula, não como depósito.

### PARTE II — As adipocinas: leptina, adiponectina e o freio que falha (5 figuras)
- **2.1** Leptina, produto do gene *ob* — o sinal de "há estoque". *(figs: slide-20 a 46%; slide-22 lateral a 40%)*
- **2.2** Parabiose: hormônio faltando de um lado, receptor faltando do outro. *(fig: slide-24, 66%)*
- **2.3** O braço periférico da leptina: simpático → β₃ → AMPc → PKA → lipólise e termogênese. *(fig: slide-26, 80%)*
- **2.4** Resistência à leptina — por que dar leptina não emagrece a maioria dos obesos.
- **2.5** Adiponectina e a AMPK: a adipocina que sobe quando a gordura desce. *(fig: slide-27, 74%)*

### PARTE III — O comando hipotalâmico e a doença que nasce quando ele é vencido (7 figuras)
- **3.1** O núcleo arqueado: NPY/AgRP contra POMC/CART. *(figs: slide-32 a 60%; slide-33 a 78%)*
- **3.2** Segunda ordem: α-MSH, MC4R e MCH — onde a decisão vira comportamento. *(fig: slide-34, 70%)*
- **3.3** Sinais de curto prazo do tubo digestivo: grelina, CCK, PYY e GLP-1. *(fig: slide-29, 72%)*
- **3.4** Quando o estoque adoece: hipertrofia, inflamação, lipotoxicidade e resistência à insulina. *(figs: slide-17 a 64%; slide-18 a 68%)*
- **3.5** Do circuito ao remédio: optogenética e os agonistas de GLP-1. *(figs: slide-35 a 54%; slide-38 a 58%)*

**Cadeias multi-passo que exigem figura (regra 9 + erro 12):** (a) leptina → hipotálamo → simpático → β₃ → AMPc → PKA → lipase hormônio-sensível/perilipina → ácidos graxos → UCP1 → calor (slide-26); (b) adiponectina → AMPK → fosforila ACC → ↓malonil-CoA → desbloqueia CPT-1 → β-oxidação (slide-27); (c) excesso calórico → hipertrofia → hipóxia/macrófago → TNF-α/IL-6 → serina-quinases → IRS → GLUT4 (slides 17 e 18); (d) ↑massa gorda → ↑leptina → ↓NPY/AgRP e ↑POMC → ↑α-MSH → MC4R → ↓ingestão (slide-33).

## Seção B.bis — Registro de abertura por subtópico (rotação, sem par vizinho repetido)

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | ponto-de-quebra |
| 1.3 | analogia concreta |
| 1.4 | integração-posterior |
| 1.5 | enquadramento |
| 2.1 | integração-anterior |
| 2.2 | ponto-de-quebra |
| 2.3 | enquadramento |
| 2.4 | integração-anterior |
| 2.5 | analogia concreta |
| 3.1 | integração-posterior |
| 3.2 | enquadramento |
| 3.3 | ponto-de-quebra |
| 3.4 | integração-anterior |
| 3.5 | analogia concreta |

## Seção B.ter — Pré-requisitos cruzados + frase-âncora pronta (≤25 palavras)

| Pré-requisito | Frase pronta a colar na 1ª aparição |
|---|---|
| Triacilglicerol como forma de estoque | "Triacilglicerol é glicerol com três ácidos graxos presos — gordura pura, sem água em volta, e por isso rende mais que o dobro de energia por grama." |
| Lipólise / lipase hormônio-sensível | "Lipólise é a quebra do triacilglicerol guardado na gota de gordura, feita por lipases que liberam ácidos graxos para o sangue." |
| Via AMPc–PKA (receptor acoplado a proteína G) | "Receptor acoplado a proteína G ativa a adenilato-ciclase, que fabrica AMPc; o AMPc solta a proteína-quinase A, que fosforila alvos e muda o comportamento da célula." |
| β-oxidação | "β-oxidação é a via mitocondrial que corta o ácido graxo de dois em dois carbonos, entregando acetil-CoA para o ciclo de Krebs." |
| Insulina e captação de glicose | "A insulina manda músculo e gordura levarem o transportador GLUT4 até a membrana; sem esse transportador na superfície, a glicose fica no sangue." |
| Retroalimentação negativa | "Retroalimentação negativa é o produto final de uma via desligando a etapa que o gerou — o mesmo princípio do termostato que corta o aquecedor." |

## Seção C — Distribuição da E2 (PADRÃO) e termos-nota obrigatórios

- **Consolidação Q01–Q10 · Integração Q11–Q25 · Aplicação Q26–Q30.**
- **Formatos:** 20 múltipla escolha + **10 Certo/Errado com exatamente 4 itens (I–IV)** — Q03, Q07, Q10 (Cons.), Q12, Q16, Q19, Q22, Q25 (Integ.), Q27, Q30 (Apl.). Duas MC no formato "assinale a **incorreta**" (Q08 e Q21), com o termo sinalizado no stem.
- **Gabarito sorteado** com guarda anti-degeneração (nenhuma letra >40%, sem corrida ≥4, nenhum padrão C/E repetido). Bloco completo no `.yml`.
- **Termos-nota nominalmente obrigatórios (alvo 6–10):** adipocina · triacilglicerol · lipólise · termogênese · parabiose · orexígeno · anorexígeno · esteatose hepática · incretina · optogenética.

## Seção D — Pontos de quebra do raciocínio (voz de mecanismo)

- **Quebra:** o aluno lê "leptina é o hormônio da saciedade" e conclui que quem tem muita leptina come pouco.
  **Correção:** a leptina informa *tamanho de estoque*, não *refeição em curso*. No obeso ela está alta e o sinal não é lido — o freio existe, o receptor é que não responde. (origem: slide 25)
- **Quebra:** tratar `ob` e `db` como dois nomes da mesma doença.
  **Correção:** `ob` não fabrica leptina (falta o ligante, e leptina de fora corrige); `db` fabrica de sobra mas não tem receptor funcional (leptina de fora não corrige nada). A parabiose separa exatamente isso. (origem: slide 23–24)
- **Quebra:** achar que a leptina só age no cérebro reduzindo apetite.
  **Correção:** o outro braço é gasto — via simpática, receptor β₃ do adipócito, AMPc, PKA, lipólise e UCP1 gerando calor. Restringir a leptina ao apetite apaga metade do mecanismo. (origem: slide 26)
- **Quebra:** supor que adipocina é sempre ruim porque obesidade é ruim.
  **Correção:** adiponectina é adipocina e cai na obesidade — quanto menos gordura, mais adiponectina, mais AMPK, mais β-oxidação. A direção do sinal depende de qual adipocina. (origem: slide 27)
- **Quebra:** confundir grelina com leptina por serem "os hormônios da fome".
  **Correção:** grelina vem do estômago vazio e sobe *antes* da refeição, ativando AgRP; leptina vem do adipócito e informa estoque acumulado ao longo de semanas. Escalas de tempo diferentes. (origem: slide 31–32)
- **Quebra:** ler AgRP como um neurotransmissor que "estimula" o MC4R.
  **Correção:** AgRP é antagonista — ocupa o MC4R e impede o α-MSH de ativá-lo. O efeito orexígeno vem de *bloquear* a saciedade, não de acionar a fome diretamente. (origem: slide 32, 34)
- **Quebra:** imaginar que a resistência à insulina na obesidade é falta de insulina.
  **Correção:** a insulina está alta; o que falha é a transdução — ácidos graxos e citocinas ativam serina-quinases que fosforilam o IRS no resíduo errado, e o GLUT4 não chega à membrana. (origem: slides 15–18)
- **Quebra:** tomar o GLP-1 como um análogo de insulina.
  **Correção:** GLP-1 é incretina — sai do intestino e faz a célula beta secretar insulina *dependendo de glicose*, além de retardar o esvaziamento gástrico e agir no hipotálamo. Não é insulina, é o sinal que a antecede. (origem: slides 29, 31, 38)

## Seção E — Exemplares-âncora (`EXEMPLARES.md`)

- **Cat. 1 (mecanística parágrafo-por-parágrafo) — universal.** Acerta em dar uma função discreta a cada parágrafo e fechar a cadeia inteira ("glutamato liga → canal abre → Na⁺ entra → despolariza"). Vou usar isso em 2.3 e 3.4, onde a cadeia é longa: cada passo com sujeito e verbo, sem rajada de sigla.
- **Cat. 8 (`atencao-box`) — universal.** Acerta no movimento de dois tempos, quebra + correção, e no uso do caso concreto antes da regra. Vou usar em 2.4 (resistência à leptina) e 3.4 (resistência à insulina não é falta de insulina) — as duas inversões que destroem o capítulo se ficarem invertidas.
- **Cat. 14 (siglas em footnote) — universal.** Acerta na disciplina de expandir na 1ª aparição sem quebrar o ritmo. Tema com muita sigla (AgRP, POMC, MC4R, GLP-1, UCP1, AMPK, CCK, TNF-α) — todas na 1ª aparição, dentro de frase com verbo.
- **Cat. 17 (cadência dialogal) — repertório.** Acerta em variar abertura, pingar avaliação narrativa e encenar a confusão *antes* da caixa. Vou usar a manobra 3 ("À primeira vista, parece natural pensar que…") antes de cada `#confusao-prevista`, e a manobra 5 (marcador de progressão) nas transições 1.5→2.1 e 2.5→3.1.
- **Cat. 5 (refinamento histórico de teoria).** Acerta em mostrar como um modelo antigo foi corrigido por evidência. É exatamente 2.2: Coleman e a parabiose, de 1969, resolvendo por cirurgia o que a genética ainda não sabia nomear.
- **Cat. 7 (analogia construtiva).** Acerta em amarrar a analogia ao mecanismo e depois soltá-la. Vou usar em 1.3 (cascata/amplificação) e em 2.5 (AMPK como sensor de "caixa baixo").
- **Cat. 9 (`clinica-box`).** Acerta em fechar a cadeia clínica em 4–6 linhas, sem adjetivo de venda. Vou usar em 2.4 (deficiência congênita de leptina — a exceção que responde), 3.2 (mutação de MC4R) e 3.5 (agonistas de GLP-1).
- **Cat. 15 (`figura-lateral`).** Acerta quando o parágrafo é curto-médio e a figura é pequena. Uso no camundongo *ob/ob* (slide-22), com ~90 palavras ao lado.
- **Cat. 16 (catálogo de família) + Cat. 18 (quando quebrar a prosa).** Os peptídeos gastrointestinais de 3.3 são catálogo de tipos discretos com um traço definidor cada — gatilho 1 do item 18. Vira parágrafo curto + tabela enxuta + parágrafo de fechamento, não seis parágrafos gêmeos.
- **Cat. 11 + 13 (distratoras mecanísticas e motivador).** Para a E2: toda distratora descreve um mecanismo *real* deslocado de lugar; ≥1 distratora por questão rouba uma peça da correta e inverte o sinal (ex.: "adiponectina inibe a AMPK").
