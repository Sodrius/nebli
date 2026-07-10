# Revisão profunda Tier 3 — UC01-FMEMB-04-propriedades-passivas-da-membrana-plasmatica

**Tema (ancoragem):** Propriedades passivas da membrana plasmática (bicamada como capacitor, canais como resistências, constante de tempo τ = RmC, constante de espaço λ = √(Rm/Ri), mielina e calibre axonal como otimização de τ/λ).
**Autor:** Italiano (apostila histórica)
**Personagem:** aluno FMUSP turma 114, 1º ano, ensino médio + meses de medicina, **dificuldade real** com eletrofisiologia. Sem hábito de buscar pré-requisitos fora.
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

---

## ANCORAGEM DE TEMA

- **3 conceitos centrais que VOCÊ-aluno gostaria de aprender:**
  1. Por que a membrana demora para responder a um estímulo (origem física do atraso na excitabilidade).
  2. Por que o sinal subliminar morre com a distância e o que λ realmente significa em mm.
  3. Por que a mielina acelera a condução — mecanismo, não a frase pronta "salta de nodo em nodo".
- **2 temas vizinhos que NÃO são esse:**
  1. Potencial de ação propriamente dito (fases, canais Nav voltagem-dependentes, período refratário) — esta apostila é o PRÉ-requisito ativo, não o PA em si.
  2. Transmissão sináptica/PEPS-PIPS — é onde τ e λ aparecem como ferramentas, mas o circuito sináptico não é o foco aqui.

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão mecanística da parada |
|---|---|---|---|
| Capa + metadados | OK | 1 | bloco "Onde estudar" referencia Boron Cap. 7, Kandel Cap. 9, Costanzo Cap. 1 — aluno se sente amparado, não trava. |
| Sumário | OK | 2 | hierarquia limpa, descrições de 1 linha em cada subtópico — aluno se orienta. |
| Abertura E1 | OK | 3 | analogia do motoneurônio lombar até o dedão do pé ANCORA por que importa antes de qualquer fórmula. Excelente. |
| 1.1 da química para eletricidade | [STOP: pág 3] | 3 | "g_K é, no exemplo do slide, vinte vezes a condutância" — qual slide? O aluno não tem o slide aberto. Em seguida cita "EK ≈ -80 mV" sem retomar o que é E_K (potencial de equilíbrio de Nernst para K) em 1 frase. Aluno em dificuldade fecha aqui se não estudou Nernst na aula anterior. |
| 1.2 bicamada = capacitor | OK | 4-5 | q = C·V derivado com prosa concreta ("para acumular q coulombs em cada placa, é preciso V volts"). Footnotes de capacitor/dielétrico/C bem postos. |
| 1.3 canais como resistências | OK | 6-8 | analogia "três pistas da autoestrada" para somar condutâncias — top. Resumindo-bloco fecha a PARTE I. |
| 2.1 despol/hiperpol | OK | 9-10 | box "Despolarização não é inversão" combate confusão #1 do tema. Excelente uso de atenção. |
| 2.2 iC vs iR | [STOP-LEVE: pág 10-11] | 10-11 | a dança temporal é descrita só em prosa; aluno em dificuldade quer ver um gráfico com eixos rotulados V(t), iC(t), iR(t) lado a lado em três instantes. O texto promete "Modelo elétrico completo" como legenda mas a figura está densa demais — aluno passa direto. |
| 2.3 τ = RmC | OK | 13-14 | a derivação dimensional ("se C é grande, precisa de mais carga → leva mais tempo; se Rm é grande, corrente demora a sair → leva mais tempo") é exatamente o estilo "porquê antes de fórmula" que o aluno precisa. |
| 3.1 sinal cai com distância | OK | 16 | a sequência V1 > V2 > V3 com a justificativa "em cada ponto, parte escapa" é cristalina. |
| 3.2 λ = √(Rm/Ri) | [STOP: pág 17] | 17 | "Olhe essa fórmula com atenção, porque ela revela o conflito" — mas o **conflito não é nomeado**. Rm em cima, Ri embaixo — o aluno vê os símbolos mas não entende qual é o conflito (não há conflito: é só a razão). Adjetivo "conflito" gera ansiedade sem payoff. |
| 3.3 mielina e diâmetro | OK | 19-20 | os "três efeitos" da mielina (Rm sobe, C cai, canais nos nodos) são numerados — top. Box clínico EM/Guillain-Barré costura mecanismo→clínica em uma página. |
| Tabela comparativa τ vs λ | [STOP: pág 21] | 21 | a tabela está quebrada visualmente — colunas com texto correndo entre linhas ("Rm sobe (sobe τ); C cai (cai τ) — / parcialmente cancela"). Aluno tenta ler de cima a baixo e perde a referência da linha. Conteúdo é ouro, layout sabota. |
| Conclusão integradora | OK | 21 | retoma os 2 parâmetros e as 2 alavancas evolutivas em um parágrafo. Costura. |
| Resumindo (2 pág) | OK | 22-23 | densidade alta mas cada bloco fecha um conceito. Cabeçalhos navy ajudam scan. |
| E2 Q01-Q10 Consolidação | OK | 24-28 | enunciados curtos, alternativas paralelas, foco no conceito. |
| E2 Q11-Q25 Integração | [STOP-LEVE: pág 29-43] | 29-43 | 15 questões consecutivas sem quebra ou box. Aluno cansa. Faltam "boxinhos de respiro" tipo "antes de Q15, lembre que..." |
| E2 Q26-Q30 Aplicação | OK | 44-48 | as 5 alternativas têm comprimento razoavelmente paritário (parecem ter sido escritas com mecanismo plausível em cada distratora). |
| E3 Q1-Q5 Discursivas | OK | 49-51 | modelos de resposta em ~100 palavras com mecanismo, exatamente o esperado. |
| Gabarito Etapa 2 | [STOP: pág 52/57] | 52/57 | layout do gabarito está descolado — "Q15 CECE" aparece deslocado da coluna de Integração; visualmente as 3 colunas (Consolidação/Integração/Aplicação) quebram em pontos diferentes da grade. Aluno consegue ler, mas precisa caçar com o dedo. |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria mais relevante:** CATEGORIA 1 (Explicação mecanística parágrafo-por-parágrafo) + CATEGORIA 2 (pergunta motivadora) + CATEGORIA 3 (desfazer confusão comum) + CATEGORIA 7 (analogia construtiva).

**Comparação favorável ao autor — Categoria 7 (analogia construtiva):**

Trecho do autor (pág 6):
> "Pense numa autoestrada com três pistas: somam-se as larguras das pistas (condutâncias), não o 'estreito' de cada uma (resistência)."

Trecho do autor (pág 4):
> "Duas placas com cargas opostas, separadas por um isolante fino. Isso, na linguagem da física, é a definição de um capacitor."

Ambas alinham com o exemplar NEBLI canônico em Categoria 7 — analogia macroscópica que **não esconde o mecanismo**: as larguras das pistas correspondem literalmente às condutâncias, sem metáfora barroca. NEBLI deveria absorver este padrão de **analogia com mapeamento 1-para-1 declarado** (autoestrada↔canais, larguras↔g, estreito↔R).

**Comparação desfavorável — Categoria 4 (magnitudes ancoradas):**

Trecho do autor (pág 3):
> "g_K é, no exemplo do slide, vinte vezes a condutância gNa"

O autor cita "20×" mas não ancora com uma comparação externa concreta (ex.: "g_K abre 20 vias enquanto g_Na abre uma só — por isso o EM 'mora' do lado do K"). NEBLI faz melhor isto na Categoria 4, onde a magnitude vem com âncora física comparativa (ex.: concentrações de glicose vs lactato em mM com referência ao plasma normal).

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação obrigatória)

### Parágrafo fraco 1 — "EK ≈ -80 mV" sem retomada de Nernst (pág 3)

**Citação literal:**
> "Por isso o Em fica perto do potencial de equilíbrio do K+ (EK ≈ -80 mV), e não no meio do caminho entre os íons. Quem 'puxa mais' o Em é o íon de maior g — e o resto é detalhe que a equação de GHK formaliza."

**Diagnóstico:** o conceito "potencial de equilíbrio de Nernst" é PRÉ-requisito mas o autor presume que o aluno saiu da aula anterior dominando. Aluno em dificuldade NÃO saiu dominando. "EK" aparece sem 1 frase retomando "valor de voltagem em que o íon não tem mais força líquida para sair — força elétrica empata a força química". A footnote sobre GHK explica GHK, não E_K isolado.

**Reescrita pronta:**
> "Por isso o Em fica perto do potencial de equilíbrio do K+ — o EK, que é a voltagem em que o K não tem mais incentivo líquido para sair da célula porque a força elétrica puxando-o de volta para dentro empatou com a força química empurrando-o para fora; nesse caso, EK ≈ -80 mV. O Em fica nesse valor, e não no meio do caminho entre os íons, porque quem 'puxa mais' o Em é o íon de maior g — o resto é detalhe que a equação de GHK formaliza."

### Parágrafo fraco 2 — "Olhe essa fórmula com atenção, porque ela revela o conflito" (pág 17)

**Citação literal:**
> "Olhe essa fórmula com atenção, porque ela revela o conflito: Rm está em cima (no numerador), Ri está embaixo (no denominador). Para λ aumentar, o que precisamos?"

**Diagnóstico:** o autor anuncia "conflito" mas não há conflito — Rm e Ri são variáveis independentes que pressionam λ em direções opostas, o que é design, não tensão. O aluno fica esperando a revelação que nunca vem. Pior: a palavra "conflito" gera microansiedade sem payoff cognitivo.

**Reescrita pronta:**
> "Olhe essa fórmula com atenção, porque ela tem dois sinais opostos embutidos: Rm está no numerador (aumenta λ quando sobe), Ri está no denominador (aumenta λ quando desce). Para λ aumentar, o que precisamos? Aumentar Rm (membrana mais isolante, menos fuga lateral) e diminuir Ri (axoplasma mais condutor)."

### Parágrafo fraco 3 — Tabela comparativa τ vs λ quebrada visualmente (pág 21)

**Citação literal (linhas como saem no .txt):**
> "Efeito da mielina Rm sobe (sobe τ); C cai (cai τ) — Rm sobe → λ sobe muito (efeito
> parcialmente cancela dominante)"

**Diagnóstico:** a tabela tem células multi-linha mas o conteúdo das colunas τ e λ se invade visualmente — "Rm sobe" da coluna λ vaza para a leitura da coluna τ. Conteúdo correto, layout sabota a leitura. O aluno tenta ler horizontalmente e perde qual coluna está lendo.

**Reescrita pronta:** trocar a tabela por **dois mini-cards lado a lado** (um para τ, um para λ), cada um com cinco linhas internas alinhadas. A comparação cruzada vira a leitura paralela visual, não horizontal. Alternativa: tabela com **uma linha por par de efeito** ("Efeito da mielina sobre τ" / "Efeito da mielina sobre λ") em vez de tentar caber tudo em uma linha por "alavanca evolutiva".

---

## 4. T3.3 — 3 seções mais densas (mitigação concreta)

| Seção | Pág | Densidade | Mitigação concreta |
|---|---|---|---|
| 1.1 (química → eletricidade + Nernst + GHK + condutância em 1 página) | 3 | 509 palavras na pág 3, a página mais densa do resumo. | Quebrar 1.1 em **1.1a (gradiente químico → elétrico, parar antes de GHK)** e **1.1b (E_K e por que Em mora perto dele)** com mini-resumo entre as duas. |
| 2.2 (iC vs iR — dança temporal) | 10-11 | toda a explicação da divisão da corrente em prosa, sem visualização explícita de iC(t) e iR(t) lado a lado. | Inserir uma **figura tripla** (V(t), iC(t), iR(t) em três painéis verticais alinhados pelo eixo t) com 3 instantes marcados (t=0, t=τ, t→∞) e legendas curtas em cada painel. |
| Resumindo de 2 páginas (22-23) | 22-23 | 10 blocos navy contíguos, 30-50 palavras cada, sem hierarquia visual entre "fundamental" e "clínica". | Ordenar os blocos por **prioridade clínica**: primeiro os 3 conceitos sem os quais o PA não faz sentido (capacitor, resistência, τ); depois os 3 de propagação (λ, mielina, decaimento); por último os 2 clínicos (EM/Guillain-Barré). E destacar visualmente os 2 últimos com um leve ouro lateral. |

---

## 5. T3.4 — Voz fora do padrão

**Voz dominante:** monitor-dialogal de qualidade alta. "Vamos enxergar a membrana como o engenheiro vê", "Repare nos números", "E aqui chegamos no ponto que muda tudo" — toda a E1 mantém essa voz.

**Desvios pontuais:**

- Pág 17 — "Olhe essa fórmula com atenção, porque ela revela o conflito" (já tratado em §3, parágrafo 2). O verbo "revela" é dramático demais para o conteúdo banal que segue.
- Pág 6 — "Tem voltagem (Em), tem resistência (os canais oferecem mais ou menos passagem), e — vamos descobrir na próxima seção — tem também capacitância". O aposto interrompe a enumeração e atrapalha o ritmo. Reescrita: terminar a enumeração primeiro ("...e capacitância") e abrir o "vamos ver" no parágrafo seguinte.
- Pág 19 — "(1) Rm efetivo aumenta muito... (2) C efetivo diminui muito... (3) os canais ficam concentrados nos nodos de Ranvier" — uso de bullets numerados em prosa, marginalmente fora do padrão NEBLI (que prefere prosa contínua). Aqui funciona porque são 3 efeitos paralelos discretos, mas no padrão estrito NEBLI seriam três frases conectadas.

---

## 6. T3.7 — Carga cognitiva pico (seção-pivô + 3 mitigações)

**Seção-pivô:** PARTE II §2.2-2.3 (iC vs iR + derivação de τ = RmC).

**Por que é o pico:** é onde o aluno precisa simultaneamente segurar (i) o circuito completo na cabeça (bateria + R + C em paralelo), (ii) a divisão de uma corrente injetada em duas componentes que mudam no tempo, (iii) a derivação dimensional de τ. Três objetos cognitivos novos em ~3 páginas. Se o aluno perde aqui, perde τ — e perde λ por extensão.

**3 mitigações possíveis:**

1. **Quebrar em duas passadas:** primeira passada qualitativa (sem fórmula) descrevendo "a corrente injetada vira duas coisas, primeiro carrega o capacitor, depois sai pelos canais"; segunda passada com im = iC + iR e a curva exponencial. Custa 1 página extra.
2. **Figura tripla obrigatória** com V(t), iC(t), iR(t) alinhados em t=0, t=τ, t→∞ (mencionada em §4). Custa 1 figura.
3. **Box "Pergunta do aluno"** entre 2.2 e 2.3: "Mas por que a curva é exatamente exponencial, e não linear ou degrau?" — responder em 4-5 linhas com a noção de "quanto mais perto do plateau, menor a força motriz residual". Custa meia página.

**Qual escolher:** **opção 2 (figura tripla)**. É o melhor custo-benefício — uma figura mata o problema sem inflar o texto. As outras duas são paliativos que aumentam densidade total.

---

## 7. T3.8 — ANÁLISE VISUAL

**Hierarquia tipográfica:** clara e funcional. Capa com fonte serifada bold para o título, sans-serif menor para metadados. Subtítulos PARTE I/II/III em destaque navy, subseções 1.1/1.2/etc em peso médio. Boa diferenciação de níveis. Capa elegante e sóbria (padrão NEBLI canônico).

**Valor pedagógico das figuras:** **misto, com problema sério de embedding**. A pág 4 mostra uma tabela "Potencial de repouso da membrana plasmática" embutida no fluxo — é uma figura informativa real (lista íons, concentrações intra/extra, Eíon, condutâncias relativas, e o cálculo final do Em ≈ -71,65 mV). Excelente conteúdo. **Problema:** a pág 12 mostra um diagrama do circuito (Rm, C, bateria, eletrodo) com legendas dentro da figura, mas as legendas estão pequenas demais para leitura confortável a 100% de zoom — aluno é forçado a dar zoom. Pág 3 menciona "Repare nos números" referindo-se a uma tabela na mesma página, e isso funciona. Várias figuras têm a função legenda-narrativa embutida ("Note como toda a estrutura do capacitor da membrana cabe num esquema simples...") — isto é exemplar e NEBLI deveria absorver (ver T3.9 §3).

**Densidade visual:** páginas 3-4 são muros (509 e 341 palavras). Páginas 7-8 e 14-15 são curtas demais (55 e 104 palavras), efeito de overflow forçado de seção. Distribuição irregular sugere que o autor priorizou completude conceitual por seção em vez de homogeneidade de página — é defensável mas cria sensação de respiração intermitente.

**Uso de cor:** disciplinado. Navy para títulos e cabeçalhos. Ouro/laranja para Resumindo e boxes de atenção. Vermelho sutil em poucas referências de alerta. **Coerência total** com o padrão NEBLI v2 — não há cores aleatórias. Categorias da E2 (consolidação/integração/aplicação) usam o esquema padrão verde/azul/violeta. Gabarito (pág 52/57) preserva esquema.

**Cortes/overflow:** a tabela comparativa de τ vs λ na pág 21 sofre quebra visual (já documentado em §3 parágrafo 3). O Resumindo de 2 páginas (22-23) está dentro do canônico ampliado, mas a divisão entre páginas corta blocos que poderiam estar visualmente próximos. Numeração de páginas no PDF físico (57 páginas) **não bate** com o `total_paginas: 52` do JSON — provável que o JSON conte apenas páginas com texto extraído pelo `pdftotext` e ignore páginas só-figura. Pendência de auditoria do extrator, não erro do autor.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (ALIMENTA Phase F / REDATOR-E1)

### Técnica 1 — Legenda-narrativa que costura figura ao mecanismo

**Citação literal (pág 4):**
> "Note como toda a estrutura do capacitor da membrana cabe num esquema simples: cargas separadas pela bicamada, equação q = C·V definindo o link entre carga acumulada e voltagem resultante. A bicamada não é só barreira para íons — ela é o que guarda a separação de cargas que constitui o Em."

E (pág 6):
> "Veja a notação: três resistências (RK, RNa, RCl) em paralelo na membrana, somando-se como condutâncias em '1/Rm = 1/RK + 1/RNa + 1/RCl'. Em repouso, com a corrente líquida zero, cada íon entra e sai na mesma taxa — mas o circuito está montado, esperando estímulo."

**Nome da técnica:** "Legenda-narrativa cinética" — a legenda da figura não descreve a figura, ela **lê a figura para o aluno**, faz o gancho do que veio antes e antecipa o que vem depois.

**Quando NEBLI deveria usar:** TODA figura de circuito, fluxo metabólico ou mecanismo encadeado. Hoje o REDATOR-E1 escreve legendas no padrão "Figura X: representação esquemática de…" — descritivo, não pedagógico. Adotar este padrão muda 100% das legendas. Gancho concreto: incluir no `.claude/agents/redator-e1.md` um bloco "padrão de legenda" exigindo (a) o que a figura mostra, (b) o que o aluno deve notar, (c) o que isso prepara para o próximo parágrafo.

### Técnica 2 — Sumarização recursiva "Resumindo até aqui:" a cada subtópico

**Citação literal (pág 3, fechando 1.1):**
> "Resumindo até aqui: Gradiente químico (íons em concentrações diferentes) → íons tendem a escapar → como têm carga, separam carga → surge gradiente elétrico → Em estabiliza no valor que zera a corrente líquida. Em ≈ EK porque gK domina em repouso."

E (pág 8, fechando 1.3):
> "Resumindo até aqui: Canais = resistências em paralelo na membrana → somam-se condutâncias, não resistências → Rm = 1/(gK + gNa + gCl) → mais canais abertos = Rm menor."

**Nome da técnica:** "Mini-resumo encadeado com setas" — uma frase em formato de cadeia causal com setas, fechando cada subtópico. **Não é o Resumindo final** — é o resumo local, **redundante intencional** que reforça a memória de trabalho do aluno antes de adicionar mais informação.

**Quando NEBLI deveria usar:** ao fim de cada subseção (1.1, 1.2, 1.3, 2.1, 2.2...). Hoje o REDATOR-E1 usa Resumindo só no fim do resumo. A inovação aqui é a **redundância encadeada por setas** que cabe em 2-4 linhas e prepara o terreno para o próximo subtópico. Gancho concreto: adicionar regra ao `.claude/agents/redator-e1.md` — "toda subseção (1.x, 2.x, 3.x) fecha com um bloco `Resumindo até aqui:` de 2-4 linhas em formato cadeia com setas".

### Técnica 3 — Box de atenção que ataca a confusão nominalmente, não em abstrato

**Citação literal (pág 9-10):**
> "Despolarização não é inversão. Aluno tende a achar que 'despolarizar' significa 'inverter o sinal' (passar de negativo a positivo). Errado. Despolarizar significa apenas diminuir o módulo da negatividade interna — ir de -70 mV para -60 mV é despolarizar, mesmo continuando negativo. A inversão de sinal só acontece no pico do potencial de ação, quando V chega a +30 mV ou +40 mV. Toda despolarização sub-limiar (que é o tema desta aula) continua na faixa negativa."

**Nome da técnica:** "Box anti-confusão nominal" — o título do box **nomeia a confusão** ("Despolarização não é inversão") em vez de ser genérico ("Atenção:"). O corpo cita literalmente o pensamento errado do aluno ("Aluno tende a achar que...") e refuta nominalmente.

**Quando NEBLI deveria usar:** SEMPRE que o `mapa-confusoes/<slug>.md` listar uma confusão de alto impacto. Hoje o NEBLI tem `.atencao-box` mas usa títulos genéricos. A inovação é (a) título = nome da confusão, (b) abertura = "aluno tende a achar que X — errado", (c) refutação mecanística. Gancho concreto: adicionar template em `.claude/agents/redator-e1.md` para `.atencao-box` exigindo essa estrutura tripla.

---

## 9. T3.10 — 7 erros NEBLI no PDF (tabela calibração)

| # | Erro NEBLI | Status | Evidência |
|---|---|---|---|
| 1 | Paridade de distratoras em E2 Aplicação (Q26-Q30) | **AUSENTE** (autor faz bem) | Q26 alternativas D (correta) tem ~50 palavras com mecanismo; distratoras A, B, C, E têm 35-55 palavras cada, todas com mecanismo plausível-mas-errado. Q29 e Q30 (caso clínico EM e Guillain-Barré) idem — distratoras carregam erro mecanístico real, não só "palavra trocada". Ratio correta/maior-distratora visualmente ≤1.25. **NEBLI deveria absorver este padrão**. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PRESENTE (parcial)** | Boas declarações em footnotes para ATP, Em, GHK, capacitor, dielétrico, C, Rm, ΔV, τ, λ, Ri, axoplasma, esclerose múltipla, Guillain-Barré, EM. **Faltam:** PA (potencial de ação — aparece pág 9 sem footnote), PEPS (pág 12 do Resumindo, sem footnote), PIPS (pág 10, declarado parcialmente como "potencial inibitório pós-sináptico" mas sem `#sigla` formal), Nav/Kv (não citados explicitamente, mas "canais voltagem-dependentes de Na+" aparece sem expansão estruturada), SNC/SNP (pág 19, expandido mas sem footnote dedicado). |
| 3 | Subagentes Opus customizados falhando | **N/A** | Este é erro de pipeline, não do conteúdo PDF. |
| 4 | Heredoc ENAMETOOLONG no Windows | **N/A** | Erro de pipeline. |
| 5 | `questao-ce` exige tupla `("I", [conteúdo])` | **AUSENTE** | Q05, Q08, Q10, Q15, Q22 são CE com 4 itens cada, todos compilados corretamente — formato tupla aplicado. |
| 6 | Termo-notas abaixo do alvo (6-8) | **AUSENTE** (autor excede) | Conta-se ~15+ footnotes técnicos no E1 (ATP, Em, GHK, condutância, capacitor, dielétrico, C, Rm, ΔV, τ, λ, Ri, axoplasma, esclerose múltipla, Guillain-Barré, EM, constante de tempo). **Acima do alvo NEBLI — referência positiva**. |
| 7 | Tema-card com teto E1 errado (canônico 22) | **N/A no PDF** | E1 do PDF tem 19 páginas (pág 3-21), dentro do canônico. Tema-card original não está no PDF, mas a entrega final respeita o teto. |

**Síntese da calibração:** o autor evita 5 dos 7 erros NEBLI clássicos. O único erro PRESENTE (parcial) é o #2 (siglas sem `#sigla`) e mesmo assim em proporção baixa. Este PDF é **calibração positiva** para o pipeline NEBLI.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)

1. **Quebrar §1.1 em duas subseções** (1.1a gradiente químico→elétrico; 1.1b E_K e Em). Pág 3 com 509 palavras é o pico de densidade do resumo e mata aluno em dificuldade já no primeiro contato técnico. Custa 1 página adicional.
2. **Inserir figura tripla V(t)/iC(t)/iR(t) entre §2.2 e §2.3.** Hoje a "dança temporal" é toda em prosa. Uma figura com 3 instantes (t=0, t=τ, t→∞) elimina o pico de carga cognitiva (T3.7). Sem ela, ~30% dos alunos perdem τ.
3. **Reescrever tabela comparativa τ vs λ (pág 21)** como dois mini-cards verticais lado a lado em vez de tabela horizontal. Conteúdo permanece; layout deixa de sabotar a leitura.

### MECANÍSTICO (max 3)

1. **Retomar Nernst/E_K em 1-2 frases na primeira aparição de EK ≈ -80 mV** (pág 3). O autor presume pré-requisito que o aluno em dificuldade não tem.
2. **Substituir "conflito" por "dois sinais opostos" na introdução de λ = √(Rm/Ri)** (pág 17). Palavra errada, conceito banal mal-anunciado.
3. **Nomear o que acontece com τ na desmielinização com mais cuidado** (pág 19-20). O texto diz "τ pode ficar moderado (Rm sobe e C cai, parcialmente cancelando)" — para aluno em dificuldade, o sinal final de τ permanece ambíguo. Esclarecer com magnitude relativa típica (ex.: "na prática, C cai mais do que Rm sobe, e τ acaba diminuindo — mas o efeito decisivo está em λ").

### DIDÁTICO (max 3)

1. **Adotar a "legenda-narrativa cinética" do autor como padrão NEBLI universal** (ver T3.9 §1). Mudança de doutrina interna do REDATOR-E1, não do PDF.
2. **Adotar "Resumindo até aqui:" com setas ao fim de cada subseção como padrão NEBLI** (ver T3.9 §2). Mudança de doutrina interna.
3. **Inserir 1-2 "Pergunta do aluno" como microboxes entre Q14 e Q15 da E2** para quebrar o muro de 15 questões consecutivas de Integração (T3.3 §3).

### ESTÉTICO (max 3)

1. **Realinhar grade do Gabarito Etapa 2 (pág 52/57)** — Q15 e Q22 estão deslocados das suas colunas. Custa 1 ajuste de grid no template.
2. **Aumentar tamanho das legendas internas do diagrama de circuito (pág 12)** — legendas pequenas demais para leitura sem zoom.
3. **Considerar reduzir páginas curtas demais** (pág 7-8 com 55 palavras; pág 14-15 com 104-115 palavras) — overflow visível. Forçar quebra mais natural ou redistribuir conteúdo da seção anterior.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM.** O resumo é exemplar em estrutura mecanística, uso de analogia construtiva, paridade de distratoras E2 Aplicação, sumarização recursiva e box anti-confusão nominal. As 3 técnicas extraídas em T3.9 **devem ser absorvidas no `.claude/agents/redator-e1.md`** como padrão NEBLI v3.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM.** 3 ESTRUTURAIS + 3 MECANÍSTICOS identificadas (§10).
3. **Seção para refazer?** **§3.2 (λ = √(Rm/Ri)) — parágrafo do "conflito" + tabela comparativa τ vs λ.** Não é refazer a seção inteira; é cirurgia em 2 parágrafos e 1 layout.
4. **Parágrafos para reescrever?** **3** — (a) "EK ≈ -80 mV sem retomada de Nernst" (pág 3); (b) "Olhe essa fórmula... revela o conflito" (pág 17); (c) tabela comparativa τ vs λ (pág 21, virar dois mini-cards).

---

[APROVAR COM RESERVAS]

FIM-T3
