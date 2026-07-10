# Revisão profunda Tier 3 — UC01-BIOQ-15-introducao-ao-metabolismo

**Tema (ancoragem):** Introdução ao metabolismo (termodinâmica → ATP → redox)
**Autor:** Marisa Helena (slides de origem); apostila NEBLI redigida por Davi Sousa — observação importante: o PDF é saída do próprio pipeline NEBLI (capa "NEBLI · APOSTILA", autor identificável no rodapé "Davi Sousa — Turma 114"), não um material histórico de terceiro autor. O exercício, ainda assim, vale como auto-revisão Tier 3.
**Personagem:** aluno FMUSP 1º ano, dificuldade real, ensino médio + meses de medicina.
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

**Limitação ambiental declarada:** `pdftoppm` indisponível no host — análise visual T3.8 foi feita a partir do JSON de estrutura (média de palavras/página, imagens/página, picos) e dos artefatos textuais do .txt (mapas conceituais, headers, sínteses). Não foi possível verificar tipografia, cor e cortes diretamente no PDF renderizado.

**Ancoragem de tema (auto-cheque):**
- 3 conceitos centrais que aluno-alvo quer aprender: (i) por que ΔG decide quem rola e quem não rola; (ii) por que ATP é a moeda, mecanisticamente, e não por mágica de "ligação rica"; (iii) por que oxidar com O₂ rende tanto ATP — e como o NADH/FADH₂ ligam isso à cadeia.
- 2 temas vizinhos que NÃO são esse: cadeia respiratória detalhada (Complexos I–IV, ATP-sintase como máquina), glicólise reação-por-reação.

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão |
|---|---|---|---|
| Capa + Nota de uso | PASSA | 1 | Nota de uso é honesta e prescritiva ("ler com slide aberto"); ancoragem aceita. |
| Sumário | PASSA | 2 | 12 subseções, hierarquia clara; aluno consegue mapear o esforço. |
| 1.1 Sistema/U/q/w | PASSA com fricção | 3 | "Energia interna = poupança energética da matéria" salva. Mas convenção de sinais (q positivo entra; w positivo é feito *sobre* o sistema) é largada em uma linha — aluno reler 3× para fixar. **Não para**, mas custa. |
| 1.2 Duas leis | PASSA | 4 | Box "Entropia do sistema NÃO é entropia do universo" é movimento exemplar — pega exatamente a confusão. |
| 1.3 Entalpia/entropia | PASSA | 4–5 | A frase "Reação exotérmica não é sinônimo de espontânea" é um gancho que faz o aluno sentar de novo. |
| 1.4 ΔG = ΔH − TΔS — quatro cenários | **[STOP: pág 5]** | 5 | Os 4 cenários (ΔH<0/ΔS>0; ΔH>0/ΔS<0; misto frio; misto quente) são listados em **prosa corrida sem tabela**. Aluno em dificuldade lê 4 frases muito parecidas em sequência ("a entalpia ganha, mas se T sobe..."), embaralha qual sinal vai com qual T. Essa é a única seção da PARTE I onde uma micro-tabela 2×2 (ΔH × ΔS → T baixa / T alta / sempre / nunca) salvaria 30 segundos de releitura. |
| ΔG⁰' e log de concentrações | PASSA | 5 | A analogia "pagar com cartão de crédito sob promoção" é boa, mas seria melhor com 1 número de exemplo concreto antes de seguir para a Parte II. |
| MAPA CONCEITUAL I | PASSA-fraco | 6 | O mapa é texto ASCII no .txt; presumindo Typst, é uma caixinha-fluxo. Funciona como recapitulação, mas não acrescenta nada além do que a Síntese 1.4 já fez. |
| 2.1 Estrutura do ATP | PASSA | 7 | "α, β, γ do mais próximo da ribose para o mais externo" — boa âncora. |
| 2.2 Hidrólise — 4 razões | PASSA com fricção | 8 | As 4 razões aparecem em parágrafos separados de 5–8 linhas cada. O aluno chega ao 4º (solvatação) e já esqueceu como a 1ª (repulsão eletrostática) se conectava. Falta um **mini-resumo de 1 frase ao final** ("Some os quatro: estados muito diferentes de estabilidade — daí os 30,5 kJ/mol"). A caixa "ATP não é especial por 'ligação rica'" cobre parcialmente, mas é meta-conceito, não recapitulação mecanística. |
| 2.3 Acoplamento direto | PASSA-bem | 8–9 | Conta -30,5 + 13,8 = -16,7 é o tipo de "ver a soma" que aluno em dificuldade precisa. Excelente. |
| 2.4 Escala de moedas + tabela | PASSA | 9–10 | Tabela bem usada (caso (a) canônico). "ATP fica no meio porque precisa receber de cima e doar para baixo" — frase-âncora a copiar. |
| 3.1 Redox biológico | PASSA com fricção | 11 | As quatro formas de transferência (elétron puro, átomo H, hidreto, O₂ direto) são jogadas em **um único parágrafo denso** com a figura ao lado. Para aluno-alvo, separar em 4 frases (1 por modalidade, na ordem) seria mais limpo. |
| 3.2 Eo' e ponte para ΔG | **[STOP: pág 11]** | 11 | A equação ΔG⁰' = −n·F·ΔEo' aparece sem **um único exemplo numérico** antes da seção 3.4. Aluno-alvo lê a equação, vê F = 96,5 kJ·V⁻¹·mol⁻¹, e fecha. Não há ancoragem dimensional. O exemplo numérico só vem 1 página depois (3.4, NADH→O₂). Reorganizar: fazer o cálculo de 220 kJ/mol AQUI, na 3.2, antes do NAD/FAD. |
| 3.3 NAD⁺/FAD | PASSA-bem | 12–13 | "Bondes de elétrons" é metáfora honesta, não polui mecanismo. Diferença Eo' → Complexo I vs II → ATP rendido é cadeia causal completa. Exemplar. |
| 3.4 Por que oxidar com O₂ | PASSA | 13–14 | Conta termina em "30 ATP/glicose vs 2 ATP/glicose" — gancho clínico de hipóxia/isquemia fecha a parte. Bom. |
| Conclusão integradora | PASSA | 14 | Recapitula em 3 perguntas-mantra ("onde está o ATP? onde estão os elétrons? por que é espontâneo?"). Excelente — copiar como técnica. |
| Resumindo (2 col) | PASSA com fricção | 16 | 8 quadrículos. O quadrículo "Os 4 cenários clássicos" sofre o mesmo problema de 1.4 — texto corrido, devia ser micro-tabela ΔH×ΔS×T. |
| E2 Q01–Q10 Consolidação | PASSA | 17–21 | Tamanho das alternativas equilibrado. Distratoras com mecanismo plausível (Q01-A confunde sistema isolado/exotermicidade; Q01-D confunde 1ª lei com proibição de endotermia — armadilhas reais). |
| E2 Q11 (cálculo) | PASSA-bem | 22 | ΔH = −30 / ΔS = +50: força o aluno a aplicar a regra dos 4 cenários. Boa calibração. |
| E2 Q26–Q30 Aplicação | **PASSA com risco** | 29–31 | Q26 (CO), Q27 (cianeto), Q29 (DNP), Q30 (Complexo I) — clinicamente ricas. **Risco residual de paridade:** algumas distratoras de Q26/Q29 são curtas/secas comparadas à correta (ver §10). |
| E3 Q1–Q5 discursivas | PASSA | 32–34 | Modelos de resposta ≤100 palavras. Q5 ("identifique o erro") é exemplar de Categoria 3 (desfazer confusão). |
| Gabarito Q01–Q30 | PASSA com fricção | 35 | Layout do gabarito está embaralhado no .txt (Q06–Q07 e Q08 fora de ordem visual; numeração não-sequencial em colunas). Pode ser artefato de extração, mas vale conferir no PDF renderizado. **Sinal de alerta visual.** |

Total: 2 STOPs (pág 5 — 4 cenários sem tabela; pág 11 — equação Faraday sem exemplo).

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categorias relevantes:** 1 (mecanística parágrafo-por-parágrafo), 3 (desfazer confusão), 7 (analogia construtiva), 11 (distratores mecanísticos), 12 (cálculo explicado).

### Comparação A — Caixa "ATP não é especial por causa de uma 'ligação rica'" (pág 8) vs Exemplar 3.1 ("Enzimas não fazem reação acontecer")

**Trecho do PDF (cit. literal):**
> "Ligação de alta energia" é apelido didático, não realidade física. ATP é especial porque a hidrólise leva a produtos muito mais estáveis que o reagente. Tudo — repulsão eletrostática, ressonância, ionização, solvatação — favorece o lado ADP + Pi. Quando o aluno trata a ligação como se ela "guardasse" energia internamente, perde o mecanismo. A energia está na diferença de estabilidade.

**Trecho do Exemplar 3.1:**
> Muitas pessoas pensam que «enzima faz reação acontecer». **Isso está errado.** Uma enzima não transforma uma reação impossível em possível — ela só torna uma reação que *já é termodinamicamente favorável* muito mais **rápida**.

**Veredito:** o PDF acerta o padrão (desfaz confusão explicitamente, nomeia o erro, ancora a correção em mecanismo). Empate técnico com o exemplar. A diferença: o exemplar 3.1 abre o tópico com a confusão (move mental: "eu achava errado → vou aprender o certo"); o PDF coloca a caixa **depois** de já ter explicado os 4 mecanismos. Para aluno-alvo, abrir 2.2 com a caixa-erro daria 5–10% mais aderência. Mas não é falha, é refinamento.

### Comparação B — Seção 1.4 "Quatro cenários ΔH × ΔS × T" (pág 5) vs Exemplar 12.1 (Michaelis-Menten com derivação narrada)

**Trecho do PDF (cit. literal):**
> ΔH < 0 e ΔS > 0: a reação é sempre espontânea, em qualquer temperatura. Os dois votos a favor; nada segura. ΔH > 0 e ΔS < 0 é o oposto — nunca espontânea, em nenhuma T. Os dois votos contra. Os dois casos interessantes são os mistos: quando ΔH < 0 e ΔS < 0, a reação só é espontânea em T baixa (a entalpia ganha, mas se a T sobe, o termo −TΔS vira positivo e mata ΔG); quando ΔH > 0 e ΔS > 0, a reação só é espontânea em T alta (a entropia precisa de T grande para vencer a entalpia desfavorável).

**Trecho do Exemplar 12.1 (princípio):** cálculos longos com gesto físico ganham quando cada passo tem identidade visual (numerado, isolado, com 1 linha de "o que isso significa").

**Veredito:** o PDF perde aqui. Quatro cenários simétricos comprimidos em um parágrafo de 6 linhas viram salada. Pequena tabela 2×2 ou bullets numerados (admissíveis pelo caso (a) canônico — cruzamento de 3 dimensões: sinal ΔH × sinal ΔS × T) resolveria. **Reescrita pronta:**

> Combinando os dois sinais com a temperatura, saem quatro cenários — copie esta tabela mental:
>
> | ΔH | ΔS | Espontaneidade |
> |---|---|---|
> | <0 | >0 | Sempre (em qualquer T) — ambos votam a favor |
> | >0 | <0 | Nunca — ambos votam contra |
> | <0 | <0 | Só em T **baixa** (entalpia ganha; T alta deixa −TΔS positivo e mata ΔG) |
> | >0 | >0 | Só em T **alta** (entropia precisa de T grande para vencer a entalpia ruim) |
>
> Note a simetria: quando os dois sinais "brigam", a temperatura decide quem ganha. T sempre amplifica o peso de ΔS.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Fraco 1 — Pág 11, seção 3.1: as quatro formas de transferência de elétron

**Citação literal:**
> Como elétron puro (citocromos, onde Fe³⁺ → Fe²⁺); como átomo de hidrogênio (1 H = 1 H⁺ + 1 e⁻, perdeu hidrogênio = oxidou); como íon hidreto (1 H⁻ = 1 próton + 2 elétrons — o jeito do NAD⁺ aceitar a carga em um só passo); ou pela combinação direta com oxigênio (a queima clássica).

**Diagnóstico:** quatro modalidades distintas em um único parágrafo de 4 linhas, separadas por ponto-e-vírgula. Aluno-alvo lê "íon hidreto = 1 próton + 2 elétrons" sem parar para entender por que isso resolve a oxidação em 1 passo — informação densa, sem respiração entre as modalidades. A figura "Quatro formas de transferência de elétrons" do lado ajuda parcialmente, mas o texto não a referencia ("observe a figura: na primeira modalidade...").

**Reescrita pronta:**
> A bioquímica usa quatro modalidades de transferência de elétron, e vale a pena separar uma por uma — porque cada uma vai voltar em uma via diferente.
>
> **Modalidade 1 — elétron puro:** o caso dos citocromos da cadeia respiratória. O Fe³⁺ do heme aceita 1 elétron e vira Fe²⁺, sem nenhum H acompanhando. Próton fica fora da história.
>
> **Modalidade 2 — átomo de hidrogênio inteiro** (1 H = 1 próton + 1 elétron). Quando uma molécula "perde um H", está ao mesmo tempo perdendo 1 e⁻ — isso é oxidação. É o caso do FAD aceitando 2 H inteiros.
>
> **Modalidade 3 — íon hidreto (:H⁻)** = 1 próton + **2 elétrons** num pacote único. É o truque do NAD⁺: aceita os dois elétrons de uma vez só (e sobra 1 próton solto no meio, que vai para o solvente).
>
> **Modalidade 4 — combinação direta com O₂:** a queima clássica (C–H + O₂ → C=O + H₂O). Vai aparecer no oxigênio terminal da cadeia respiratória.

### Fraco 2 — Pág 11, seção 3.2: equação de Faraday sem ancoragem numérica imediata

**Citação literal:**
> ΔG⁰' = −n · F · ΔEo'
> n é o número de elétrons transferidos; F é a constante de Faraday (96,5 kJ · V⁻¹ · mol⁻¹). O sinal negativo na frente garante que, quanto maior o ΔEo' (diferença positiva entre aceptor e doador), mais favorável a reação (ΔG mais negativa). É a ponte direta entre eletroquímica e termodinâmica.

**Diagnóstico:** equação aparece, constante é dada, mas **nenhum exemplo numérico imediato** dentro da seção 3.2. O exemplo (NADH → O₂, ΔEo' = 1,14 V, ΔG⁰' ≈ −220 kJ/mol) só aparece em 3.4, **duas páginas depois**. Aluno-alvo precisa do número para sentir o gesto físico da equação.

**Reescrita pronta:**
> ΔG⁰' = −n · F · ΔEo'
>
> *n* é o número de elétrons transferidos (geralmente 2 em bioquímica); *F* é a constante de Faraday, 96,5 kJ · V⁻¹ · mol⁻¹.
>
> Aplique uma vez para sentir o gesto: NAD⁺ doa 2 elétrons (Eo' = −0,32 V) que descem até o O₂ (Eo' = +0,82 V). ΔEo' = 0,82 − (−0,32) = 1,14 V. Logo: ΔG⁰' = −2 × 96,5 × 1,14 ≈ **−220 kJ/mol por NADH oxidado**. Esse é o tamanho do "tanque" de energia disponível por cada NADH — voltaremos a ele em 3.4 para ver quanto disso vira ATP.

### Fraco 3 — Pág 8 §3 (último parágrafo de "ATP não é especial por 'ligação rica'")

**Citação literal:**
> "Ligação de alta energia" é apelido didático, não realidade física. ATP é especial porque a hidrólise leva a produtos muito mais estáveis que o reagente. Tudo — repulsão eletrostática, ressonância, ionização, solvatação — favorece o lado ADP + Pi. Quando o aluno trata a ligação como se ela "guardasse" energia internamente, perde o mecanismo. A energia está na diferença de estabilidade.

**Diagnóstico:** o parágrafo está bem escrito, mas **vem depois** dos 4 mecanismos. Para o aluno-alvo, o melhor seria abrir 2.2 com esta caixa (move mental "vou aprender o errado primeiro") e depois desfilar os 4 mecanismos como a *correção* construtiva. É inversão de ordem pedagógica.

**Reescrita pronta:** mover esta caixa para o **início** de 2.2, antes da frase "Quando ATP + H₂O → ADP + Pi (...) libera-se ΔG⁰ = −30,5 kJ/mol". Reabrir a seção assim:
> Antes de explicar de onde vem essa energia, desfazemos uma confusão que pega 80% dos alunos. **"Ligação de alta energia" é apelido didático, não realidade física.** Ninguém guarda joule numa ligação química como se ela fosse uma mola. A energia liberada na hidrólise vem da **diferença de estabilidade entre antes e depois**: ATP é tenso; ADP + Pi é relaxado. Os quatro mecanismos abaixo explicam por que.

---

## 4. T3.3 — 3 seções mais densas (densidade de informação por mm²)

| Seção | Sintoma de densidade | Mitigação concreta |
|---|---|---|
| **1.4 Quatro cenários ΔH × ΔS × T** (pág 5) | 4 cenários simétricos em prosa corrida; aluno embaralha qual sinal vai com qual T. | Substituir por tabela 2×2 (ver §2 Comparação B). |
| **2.2 Quatro mecanismos da hidrólise do ATP** (pág 8) | 4 mecanismos em 4 parágrafos de 5–8 linhas cada; aluno chega ao 4º já tendo perdido o 1º. | Adicionar mini-resumo de 1 frase ao final: "Some os quatro — separação de cargas, ressonância, ionização, solvatação — e está toda a diferença de estabilidade entre ATP e ADP+Pi." Tabela compacta também ajudaria, mas pode poluir. |
| **2.4 Tabela de escala + parágrafos sobre fosfocreatina + caixa sobre suplementação + parágrafo sobre acetil-CoA** (pág 9–10) | 4 conteúdos heterogêneos (tabela, biologia muscular, clínica, química do tioéster) em 1,5 página. | Quebrar acetil-CoA em subseção 2.5 com headline próprio. A caixa de suplementação de creatina é deliciosa mas concorre com a leitura mecanística do tioéster — separar visualmente. |

---

## 5. T3.4 — Voz fora do padrão

Geralmente a voz é boa: 2ª pessoa implícita ("você fica de olho no que entra"), perguntas ingênuas plausíveis ("essa reação vai acontecer ou não?", "de onde vem tanta energia?"). Mas duas citações destoam:

- Pág 5: **"Da í saem quatro cenários clássicos que precisam estar na ponta da língua"** — clichê de cursinho. Aluno-alvo lê "ponta da língua" e sente que está em cursinho preparatório para PSC, não em ferramenta de monitor explicando. Substituir por "...quatro cenários que vale a pena memorizar visualmente — copie a tabela abaixo".
- Pág 5: **"Repare como a fórmula combina ΔH, ΔS e T num único veredito"** — usado em caixinha de destaque. "Veredito" é palavra eficiente, mas a frase é apenas recapitulação do que acabou de ser dito 3 linhas antes. Caixa redundante.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô identificada:** pág 11, transição entre 3.1 e 3.2.

Em ~15 linhas o aluno precisa absorver: (i) 4 modalidades de transferência de elétron; (ii) figura nova ao lado (4 formas); (iii) regra de vocabulário "perda H = oxidação, ganho H = redução"; (iv) abertura imediata do conceito Eo' com 4 exemplos numéricos (NAD, piruvato/lactato, citocromos, O₂); (v) equação de Faraday com constante; (vi) regra de sinal do menos-n-F. **Seis novidades em uma única página de 322 palavras.**

**3 mitigações possíveis:**

1. **Quebrar 3.1 em duas:** (a) "Oxidação é perda de elétron — vocabulário"; (b) "Quatro modalidades de transferência" como subseção própria com 1 parágrafo por modalidade (ver Fraco 1).
2. **Atrasar Eo' para 3.3:** introduzir Eo' apenas quando o NAD⁺ e o FAD chegarem (já com −0,32 V e o do FAD em contexto). 3.2 vira um interlúdio curto só com a equação de Faraday + 1 exemplo numérico (NADH→O₂).
3. **Adicionar painel de orientação no topo de 3.2:** "Nesta página você vai ver duas coisas: (a) o que é Eo'; (b) como Eo' vira ΔG via Faraday. No final, sabemos calcular quanta energia há entre dois pares redox quaisquer."

**Qual escolher:** opção **1** (quebrar 3.1 em duas). É a mais simples, não exige reescrita estrutural, ataca diretamente o pico de novidades. Opção 2 é mais profunda mas reorganiza demais. Opção 3 é band-aid.

---

## 7. T3.8 — ANÁLISE VISUAL (do JSON + .txt; PDF render indisponível)

**Dados do JSON:**
- 35 páginas, 9929 palavras, média 283,7 palavras/página.
- Apenas **5 imagens** em 35 páginas; distribuídas em pág 5, 7, 8, 11, 13 — todas na Etapa 1 (texto didático). E2/E3 sem figura alguma.
- Pico de palavras: pág 4 (510), pág 6 (433), pág 9 (437), pág 14 (425).
- Vales: pág 15 (76 — mapa conceitual III isolado), pág 35 (82 — gabarito final), pág 18 (192).

**Sub-itens:**

1. **Hierarquia tipográfica:** inferida do .txt — capa com "N E B L I · A P O S T I L A" (kerning expandido); cabeçalho de cada página com "NEBLI" + tag de seção ("ETAPA 1 — TEXTO DIDÁTICO"); subseções numeradas (1.1, 1.2, ..., 2.1, ...). Hierarquia parece consistente. Padrão NEBLI canônico.

2. **Valor pedagógico das figuras:** 5 figuras totais em 35 págs é **subdimensionado para o tema**. Meta NEBLI: ≥3 figuras por PARTE da E1 → esperado mínimo 9 figuras (PARTE I termodinâmica, PARTE II ATP, PARTE III redox). Realidade: ~1,7 figuras por PARTE. Especificamente, **PARTE I (termodinâmica) parece ter apenas 1 figura (pág 5)** — para um tema visualmente abstrato (ΔG, ΔH, T·ΔS, cenários ΔH×ΔS), seria onde mais um diagrama bem feito ajudaria. Cadeia multi-passo enzimática é regra de figura obrigatória; aqui o tema é mais conceitual, mas mesmo assim 5 figuras é pouco. **Recomendação:** adicionar diagrama dos 4 cenários (curva-eixo T no x, ΔG no y, 4 retas com sinais), diagrama de poço de energia (ATP↑, ADP+Pi↓ separados pelos 4 mecanismos visualizados como flechas), e esquema da escala de moedas (PEP → PCr → ATP → G6P como termômetro vertical).

3. **Densidade visual:** média 283,7 palavras/página é alta para apostila com missão "do básico ao aprofundado". EXEMPLARES.md sugere parágrafos curtos com respiração. Picos de 433–510 palavras (pág 4, 6, 9, 14) são páginas-muro. Pág 4 (1.2 + 1.3) é a mais densa do resumo todo — duas leis + entalpia + entropia em 510 palavras sem figura.

4. **Uso de cor:** não verificável sem render. Pelo padrão NEBLI canônico, cores por categoria em E2 (consolidação / integração / aplicação) são esperadas. .txt mostra apenas tags textuais ("Consolidação", "Integração", "Aplicação") — presumir que o Typst aplica badges coloridos canônicos.

5. **Cortes/overflow:** sinal de alerta no gabarito (pág 35): no .txt aparece embaralhado ("Q06 ECCE Q07 D | Q08 E Q09 CCEC Q10 B" com Q08 deslocado para coluna 2 mas Q06 ocupando 2 colunas). Pode ser artefato da extração, mas **vale conferir o gabarito no PDF renderizado**.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (ALIMENTA Phase F / REDATOR-E1)

### Técnica 1 — Abertura por pergunta concreta que pinta o cenário cotidiano

**Citação literal (pág 3):**
> "Como a célula 'sabe' se uma reação vai acontecer ou não? Por que a glicose, dissolvida num copo de água em cima da bancada, fica lá parada indefinidamente, mas, dentro de uma célula, vira CO₂ e água? A resposta está na termodinâmica."

**Nome da técnica:** "Abertura por contraste cotidiano duplo" — apresenta a mesma molécula em dois contextos (copo de água parado vs célula viva) e converte a pergunta abstrata ("o que é termodinâmica?") em pergunta operacional ("por que o estado A vs o estado B?").

**Quando NEBLI deveria usar:** sempre que o conceito tem versão **microscópica intuitiva** (a glicose, a proteína dobrada, o íon contra gradiente). Em vez de "vamos estudar termodinâmica", usar "a glicose no copo vs a glicose na célula — por quê?". Já é canônico (CLAUDE.md fala em "pergunta ingênua plausível"), mas este exemplar específico **com duplo contraste** é mais forte que pergunta única. Adicionar como sub-padrão ao REDATOR-E1.

### Técnica 2 — Mantra de 3 perguntas para releitura futura

**Citação literal (pág 14, conclusão integradora):**
> "Sempre que ficar perdido nos nomes das enzimas e dos intermediários, volte a três perguntas: 'onde está o ATP? onde estão os elétrons? por que isso é espontâneo?'."

**Nome da técnica:** "Mantra de re-orientação" — entrega ao aluno uma ferramenta meta-cognitiva explícita para usar **em qualquer aula futura** quando perder o fio. Não é só fechamento do resumo: é entrega de método.

**Quando NEBLI deveria usar:** ao final de qualquer Conclusão Integradora de tema-pilar (gliconeogênese, glicólise, cadeia, transporte, transmissão sináptica). Definir 2–4 perguntas-âncora que cubram os eixos mecanísticos centrais do tema, e oferecê-las literalmente como "mantra para outras aulas". Diferente de "Resumindo" (que sintetiza fatos) — este é "kit de sobrevivência mental" portátil. **Acionável imediato:** REDATOR-E1 ganha regra "se for tema-pilar, fechar Conclusão Integradora com 2–4 perguntas-mantra portáteis".

### Técnica 3 — Tabela quantitativa com 1 frase de interpretação imediata acima e abaixo

**Citação literal (pág 9–10, tabela de moedas energéticas):**
> [tabela com 6 compostos e ΔG⁰']
> "Repare em duas coisas. Primeiro, o ATP está no meio da escala — não no topo. Isso é proposital. Compostos acima do ATP podem doar fosfato para ele (regenerando ATP); compostos abaixo recebem fosfato dele (consumindo ATP). É exatamente porque ATP fica numa posição intermediária que ele consegue ser intermediário em todas as direções..."

**Nome da técnica:** "Tabela sanduichada por leitura guiada" — tabela é sempre acompanhada por (1) 1 frase de motivação acima ("Aqui está a escala...") e (2) 2 observações numeradas abaixo que **dirigem o olhar do aluno** para a feature não-óbvia (posição relativa do ATP, não os valores absolutos).

**Quando NEBLI deveria usar:** sempre que aparecer `#table()` no corpo (catálogos de família — GLUTs, SGLTs, hexoquinases, citocromos). Hoje o REDATOR-E1 às vezes solta a tabela e segue para o próximo conceito sem direcionar o olhar. Regra-cookie: "toda tabela tem 1 frase de contexto antes e ≥1 observação interpretativa numerada depois — nunca tabela órfã."

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro canônico | Status |
|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **PARCIAL** — Q26-A ("fosfocreatina muscular se acumula") tem 16 palavras vs correta C com 28 palavras (ratio 1,75). Q29-D ("Aumento do potencial de redução do par O₂/H₂O...") com 21 palavras vs correta E com 24 palavras (ok). Q30: distratoras balanceadas. Risco residual em Q26 e Q28. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PRESENTE-leve** — siglas declaradas: ATP, NAD⁺, FAD, AMP, ADP (footnotes 1–5 visíveis). Ausentes prováveis: **Pi** (aparece "Pi é fosfato inorgânico" em prosa, sem `#sigla`), **CoA / acetil-CoA** (aparece sem declaração formal), **FADH₂**, **NADH** (idem). Cross-check com regex grep recomendado. |
| 3 | Subagentes Opus contaminados | **N/A** — não testável a partir do PDF. Mas o resumo tem coerência temática (não copia conteúdo de cadeia respiratória vs introdução); fix 2026-05-25 parece ter funcionado neste caso. |
| 4 | Heredoc `ENAMETOOLONG` | **N/A** — pipeline produziu PDF; não houve falha de gravação. |
| 5 | `questao-ce` exige tupla | **N/A** — não testável a partir do PDF; presumir que o Typst compilou. |
| 6 | Termo-notas abaixo do alvo (6–8) | **PRESENTE** — só vi 5 footnotes explícitos no .txt (ATP, NAD⁺, FAD, AMP, ADP). Termos densos sem `#termo-nota` provável: **entalpia, entropia, energia livre de Gibbs, ressonância, tioéster, gradiente quimiosmótico, fosforilação a nível de substrato, fermentação láctica, von Cori (não usado, mas glicogenólise)**. Alvo 6–8 → entregou ~5. |
| 7 | Tema-card teto E1 errado | **N/A** parcial — E1 ocupa págs 3–14 = **12 páginas**, bem dentro do teto 22. Dimensão correta. |

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Reorganizar 3.2 ↔ 3.3:** mover o cálculo de Faraday/220 kJ por NADH para dentro de 3.2 com 1 número aplicado imediatamente. Sem exemplo numérico na seção da equação, o aluno-alvo trava. (Fraco 2 — STOP pág 11.)
2. **Quebrar 3.1 em duas subseções:** (a) vocabulário de redox (perda H = oxidação, etc.); (b) 4 modalidades de transferência, uma por parágrafo. (T3.7 — opção 1.)
3. **Adicionar mais 4 figuras na E1:** diagrama 2×2 ΔH×ΔS (PARTE I), poço energético ATP→ADP+Pi com 4 mecanismos (PARTE II), termômetro de moedas (PARTE II), esquema NADH→Complexo I→O₂ (PARTE III). 5 figuras em 14 págs de E1 é subdimensionado.

### MECANÍSTICO (max 3)
1. **Inverter ordem em 2.2:** abrir a seção com a caixa "ATP não é especial por 'ligação rica'" (move mental de desfazer confusão antes do conteúdo correto). Hoje a caixa fecha em vez de abrir. (Fraco 3 + Comparação A com Exemplar 3.1.)
2. **Adicionar exemplo numérico cotidiano em ΔG⁰' vs ΔG real:** após a equação ΔG = ΔG⁰' + RT ln([prod]/[reag]) (pág 5), inserir 1 cálculo concreto ("se a razão é 0,01 a 37°C, RT ln(0,01) ≈ −11,4 kJ/mol — o suficiente para virar +6 kJ/mol em −5,4 kJ/mol"). O exemplo existe na E3 Q4, mas o aluno-alvo precisa dele já em 1.4.
3. **Cobrir Pi, CoA, FADH₂, NADH com `#sigla()` próprio:** mesmo aparecendo na expansão de outras siglas, o aluno vê a abreviação solta no corpo. Erro #2 do checklist.

### DIDÁTICO (max 3)
1. **Substituir prosa dos 4 cenários por tabela 2×2** (pág 5). Caso (a) canônico aplicável: 3 dimensões cruzadas (ΔH × ΔS × T). (Fraco 2 da §3.)
2. **Quebrar 2.4 em 2.4 (escala/PCr) + 2.5 (acetil-CoA tioéster):** 4 conteúdos heterogêneos em 1,5 página é demais.
3. **Adicionar mini-resumo de 1 frase ao final de cada cluster de "4 razões/4 mecanismos/4 modalidades":** o leitor que chegou ao item 4 precisa do gancho da soma. Hoje a Síntese só vem no final da subseção 2.2 e 3.4, não em 2.2 §mecanismos.

### ESTÉTICO (max 3)
1. **Conferir layout do gabarito (pág 35):** no .txt aparece embaralhado (Q06–Q07–Q08 fora de ordem visual). Pode ser artefato de extração ou bug real do `#gabarito-tabela`.
2. **Reduzir densidade da pág 4 (510 palavras):** ou inserir figura, ou quebrar 1.2/1.3 em página separada. Pior página-muro do resumo.
3. **Eliminar caixa redundante de pág 5** ("Repare como a fórmula combina ΔH, ΔS e T num único veredito") — repete o que foi dito 3 linhas antes.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM** — várias técnicas exemplares (mantra de 3 perguntas, abertura por contraste cotidiano duplo, tabela sanduichada). Mesmo com 3 frações fracas, o resumo é melhor que a média NEBLI G20.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM** — 3 ESTRUTURAIS, 3 MECANÍSTICOS listados.
3. **Seção para refazer?** **3.1–3.2** (parte da PARTE III, redox). Aglomeração de novidades + equação sem ancoragem. Refazer essas duas subseções juntas, na ordem proposta (vocabulário → 4 modalidades → equação com exemplo).
4. **Parágrafos para reescrever?** **3:** (i) pág 11 — 4 modalidades (Fraco 1); (ii) pág 11 — equação de Faraday (Fraco 2); (iii) pág 5 — 4 cenários ΔH×ΔS (Fraco 2 §2).

---

[APROVAR COM RESERVAS]

**Reservas:** refazer seções 3.1–3.2 conforme recomendações estruturais 1 e 2; adicionar 4 figuras conforme estrutural 3; cobrir lacunas de `#sigla()` em Pi/CoA/NADH/FADH₂; substituir prosa dos 4 cenários por tabela 2×2. Após esses 4 ajustes, candidato a referência positiva para Phase F (extração de técnicas para REDATOR-E1).

FIM-REVISAO-PROFUNDA
