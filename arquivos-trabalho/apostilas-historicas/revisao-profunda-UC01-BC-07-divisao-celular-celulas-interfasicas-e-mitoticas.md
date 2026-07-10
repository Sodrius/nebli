# Revisão profunda Tier 3 — UC01-BC-07-divisao-celular-celulas-interfasicas-e-mitoticas

**Tema (ancoragem):** Divisão celular — ciclo celular, interfase (G1/S/G2), mitose, motor CDK-ciclina, checkpoints, p53/Rb.
**Autor:** Nathalie Cella (slide-base); redação NEBLI (Davi Sousa).
**Personagem:** aluno FMUSP 1º ano, turma 114, dificuldade real, ensino médio + meses de medicina.
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo.
**Data:** 2026-05-25

## ANCORAGEM DE TEMA (declaração obrigatória)

Tema canônico: **Divisão celular — células interfásicas e mitóticas**.
3 conceitos que eu-aluno quero aprender: (a) como o ciclo "sabe" a hora de avançar; (b) por que a célula só replica o DNA UMA vez; (c) por que perder Rb ou p53 dá câncer.
2 temas vizinhos que NÃO são esse: meiose/gametogênese; replicação molecular do DNA (mecanismo da forquilha).

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Capa + sumário | OK | 1–2 | Capa limpa. Sumário lista 4 sub-itens por PARTE (canon = max 3). Não para a leitura mas trai a regra. |
| 1.1 Crescimento × divisão | OK | 3 | Abertura honesta, sem jargão, paralelo com "proliferação" funciona. |
| 1.2 Panorama G1/S/G2/M | STOP leve | 4 | Footnote "CDK²" aparece ANTES de qualquer narrativa sobre CDK. Footnote 3 (APC/C) idem. Aluno lê "CDK² APC/C³ SCF⁴" no meio do parágrafo e pensa: "para que serve isso aqui ainda?" Bloco no-context. |
| 1.3 BrdU / citometria / cdc | OK | 5–6 | História bem contada, motivação clara. |
| 1.4 Tudo-ou-nada + checkpoints | OK | 7–8 | Box "checkpoint é decisão, não peça" salva. |
| 2.1 CDK + ciclina | OK | 9 | Box "ciclina é cofator, não enzima" é exemplar. |
| 2.2 Wee1/Cdc25/CAK/CKI | **STOP forte** | 10–11 | 4 mecanismos sobrepostos em 1 página + 2 siglas (CAK, CKI) em footnote sem nunca terem aparecido no corpo. "INK4 (p15, p16, p18, p19)" e "Cip/Kip (p21, p27, p57)" — 7 proteínas novas em uma frase, aluno fecha o PDF. |
| 2.3 SCF / APC/C / UPS | OK | 12 | Tabela SCF/APC/C-Cdc20/APC/C-Cdh1 funciona como ancora. |
| 2.4 Volta inteira do ciclo | OK | 13–14 | Maior bloco mecanístico do PDF; "resumindo" no fim costura tudo. |
| 3.1 Rb/E2F/restrição | OK | 15–16 | Box "Rb INIBE E2F — fosforilação LIBERA" é didática-ouro. |
| 3.2 Pré-RC + licenciamento | OK | 17 | Box "CDK alta dispara E impede re-licenciamento" amarra o duplo papel. |
| 3.3 Mitose / SAC / separase | OK | 18–20 | Box "separase corta coesina, não cromossomo" é exemplar. |
| 3.4 p53 + dano | OK | 21–23 | Box "p53 não repara — sinaliza para parar ou morrer" + Li-Fraumeni boxado. |
| Conclusão integradora | OK | 24 | Síntese fechada bem. |
| Resumindo | OK | 25 | 1 página, 8 blocos, prosa concreta. Caber em 1 página é vitória. |
| **Pág 26** | **STOP estrutural** | 26 | Página com **8 palavras** ("RESUMINDO"). Página em branco oficial. Sinal de bug de quebra de página. |
| Etapa 2 (Q01–Q30) | STOP recorrente | 27–51 | Enunciados ok; mas o aluno que tenta conferir respostas no gabarito (p55) bate em **gabarito errado em 13 das 30 questões** (ver §11). Aluno acerta e o PDF marca como erro — perde fé na ferramenta. |
| Etapa 3 (discursivas) | OK | 52–54 | Modelos de resposta sólidos, Q5 com formato "identifique o erro" é exemplar. |
| **Pág 55 gabarito** | **STOP estrutural** | 55 | Cabeçalho diz "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" mas conteúdo é "Gabarito — Etapa 2". Etapa 4 foi removida do pipeline em 2026-05-22 (canônico) — header é fóssil. |

---

## 2. T3.1 — Comparação com EXEMPLARES.md (categoria: explicação mecanística enzimática multi-camada)

Categoria relevante: **mecanismos com camadas regulatórias sobrepostas** (Wee1/Cdc25/CAK/CKI; APC/C-Cdc20 vs APC/C-Cdh1).

**Parágrafo NEBLI (p10–11, 2.2):**
> "O primeiro mecanismo, já visto, é a ciclina: sem ela, nada de quinase. O segundo é uma fosforilação ativadora feita pela CAK [...] O terceiro mecanismo é uma fosforilação inibitória, feita pela quinase Wee1 [...] O quarto mecanismo, e talvez o mais importante para a fisiologia, são as CKIs [...] A família INK4 (p15, p16, p18, p19) é específica [...] A família Cip/Kip (p21, p27, p57) [...]"

Estrutura: enumeração linear "primeiro/segundo/terceiro/quarto" + 7 proteínas novas (p15, p16, p18, p19, p21, p27, p57) atiradas em duas frases. Aluno trava em quantidade nominal.

**Parágrafo exemplar NEBLI (Etapa 1 da gliconeogênese — bypass 1):**
Estrutura típica é: declara o problema ("a célula precisa contornar uma reação irreversível"), apresenta UMA solução com nome e mecanismo ("entra a piruvato carboxilase, no espaço mitocondrial"), pergunta de transição ("mas e a 2ª reação?"), entra a 2ª enzima. Itens encadeados como capítulos de uma narrativa, não como lista enumerada.

**Veredito de comparação:** o §2.2 desta apostila quebrou o padrão NEBLI ao usar enumeração linear; deveria ter virado 4 mini-blocos com pergunta-de-transição entre cada um, OU ter cortado as 7 proteínas para apenas p21/p27 (as duas únicas que reaparecem no texto adiante).

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação completa)

### 3.2.1 — Footnotes-bloco sem contexto (p4, §1.2)

**(a) Citação literal:**
> "A fase G1 (de gap 1) é o intervalo entre a mitose anterior e o início da replicação do DNA. [...]
>
> CDK² APC/C³ SCF⁴
>
> A fase G1 é a fase mais variável em duração [...]"

**(b) Diagnóstico mecanístico:** três siglas declaradas como footnote no MEIO do §1.2 sobre fases do ciclo, sem o corpo do texto ter falado de CDK, APC/C ou SCF ainda (essas aparecem só na PARTE II, 5 páginas depois). O leitor lê a string nua "CDK² APC/C³ SCF⁴" no corpo, pula para os rodapés, lê uma definição densa de 25 palavras cada, volta — e perdeu o fio do parágrafo. Erro #2 da lista canônica (siglas sem #sigla na 1ª aparição) — mas aqui é o oposto: #sigla() ANTES da 1ª aparição mecanística no corpo.

**(c) Reescrita pronta:** mover as 3 #sigla() para a PARTE II, §2.1 onde aparecem pela primeira vez em contexto. No §1.2, apenas mencionar "um motor enzimático (que vamos detalhar adiante)" sem nomear. Footnote a regra de declaração: **sigla footnoted no momento em que entra no corpo como protagonista, não no primeiro avistamento periférico.**

### 3.2.2 — Sopa de proteínas em duas frases (p11, §2.2)

**(a) Citação literal:**
> "Existem duas famílias principais em mamíferos. A família INK4 (p15, p16, p18, p19) é específica para a G1-CDK: liga-se à CDK4/6 e impede a associação com a ciclina D. A família Cip/Kip (p21, p27, p57) tem espectro mais amplo: liga-se a complexos CDK-ciclina já formados e os inibe."

**(b) Diagnóstico:** 7 proteínas novas (p15, p16, p18, p19, p21, p27, p57) + 1 família nova (INK4, Cip/Kip) + 1 complexo (CDK4/6) introduzidos em 50 palavras. Para o aluno, isso é decoreba. Pior: só p21 e p27 reaparecem no resto do texto — as outras 5 (p15, p16, p18, p19, p57) são poluição. Erro #6 canônico (jargão acima do necessário para o aluno-alvo).

**(c) Reescrita pronta:**
> "Existem duas famílias de CKIs em mamíferos. A primeira, chamada **INK4**, atua só sobre a G1-CDK: bloqueia o encaixe entre CDK4/6 e ciclina D, e por isso é o freio molecular do começo do ciclo. A segunda, **Cip/Kip**, tem espectro amplo — inibe vários complexos CDK-ciclina já formados, e dá dois protagonistas que vamos reencontrar adiante: **p21** (ativada pela p53 quando há dano no DNA) e **p27** (alta em G0/G1 inicial, destruída quando chegam mitógenos). p15, p18, p19 e p57 existem mas não vamos visitá-las."

Mantém o nome técnico e ancora **só** os dois que voltam.

### 3.2.3 — Tabela 2.1 quebrada (p9–10)

**(a) Citação literal (tabela tal como sai no texto extraído):**
> "Complexo | Ciclina parceira | Função principal | Quando atua
> G1-CDK | Ciclina G1 (D1, D2, D3) |  |
> G1/S-CDK | Ciclina G1/S (E) | Prepara expressão de ciclinas Meio e fim de G1
> S-CDK | Ciclina S (A) | G1/S; fosforila Rb e libera E2F"

**(b) Diagnóstico:** a tabela está com **colunas desalinhadas no PDF** — a linha de G1-CDK perdeu Função e Quando; "Prepara expressão de ciclinas Meio e fim de G1" colidiu numa célula só. O aluno tenta ler a tabela, percebe que não fecha, desiste da tabela e parte para o texto corrido — perdendo a função pedagógica da tabela. Bug de layout Typst (provável overflow de célula sem `colspan`).

**(c) Reescrita pronta:** reverter para PROSA em diálogo, exatamente como o §2.4 já faz adiante. Ou refazer a tabela com `table()` nativo `inset: 6pt, columns: (auto, auto, 1fr, auto)` — 4 colunas, larguras explícitas, conteúdo curto em cada célula (≤6 palavras). A tabela tal como está é pior que ausência de tabela.

---

## 4. T3.3 — 3 seções mais densas (com mitigação)

| Seção | Densidade | Mitigação concreta |
|---|---|---|
| §2.2 (Wee1/Cdc25/CAK/CKI/INK4/Cip-Kip) — p10–11 | Pico do PDF | Cortar lista de p15/p16/p18/p19/p57; manter p21 e p27 apenas. Quebrar em 2 sub-seções (fosforilação vs CKIs). Adicionar 1 figura: diagrama "CDK + 4 chaves em série" (ciclina, CAK+, Wee1−, CKI−). |
| §2.4 (volta inteira do ciclo em prosa) — p13–14 | Alta mas justificada | Manter; é o momento síntese. Inserir 1 figura inline mostrando as 4 ondas de ciclina sobrepostas com setas de transição. |
| §3.3 (mitose + SAC + APC/C-Cdc20 + securina + separase) — p18–20 | Alta | Inserir a sequência mecanística como uma "cadeia de 4 elos" boxada: SAC libera → APC/C-Cdc20 ativa → securina degrada → separase livre → coesina cortada → anáfase. Aluno precisa ver os elos lado-a-lado, não em prosa corrida. |

---

## 5. T3.4 — Voz fora do padrão

Não detectei rupturas de voz dentro da E1. O resumo mantém o padrão "monitor-explicando" do início ao fim, com diálogo coerente (uso de "vamos detalhar", "repare que", "vamos voltar a ela em 3.4"). Box-quadros mantêm voz pedagógica firme.

Pequena observação: o **Resumindo** (p25) usa pontos finais aglomerando 3 ideias por bloco — voz mais densa que o exemplar canônico, que prefere 1 frase com sujeito + verbo + complemento. Aceitável.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** §2.2 — Controle fino da CDK (p10–11). Concentra: (a) 4 mecanismos sobrepostos; (b) 7 proteínas novas em uma frase; (c) 2 siglas (CAK, CKI) novas; (d) introdução de p21 e p27 que voltam adiante; (e) box explicativo Wee1/Cdc25.

**3 mitigações possíveis:**
1. **Cortar metade**: tirar p15/p16/p18/p19/p57, manter só p21+p27. Reduz carga de jargão em 40% sem prejuízo mecanístico.
2. **Quebrar em 2 sub-seções**: 2.2a (CAK + Wee1/Cdc25 = fosforilação) e 2.2b (CKIs). Mesma carga, distribuída em 2 ancoras.
3. **Adicionar figura mestra**: diagrama "CDK no centro com 4 reguladores ao redor". Visual paga o preço do jargão.

**Escolha:** combinar (1) + (3). O (2) sozinho mantém a sopa, e o (1) sozinho perde a oportunidade visual.

---

## 7. T3.8 — ANÁLISE VISUAL (do PDF)

- **Hierarquia tipográfica:** consistente. Títulos navy bold + corpo Merriweather + badges coloridos por categoria (Consolidação verde, Integração azul, Aplicação violeta). Sinaliza profundidade sem distrair. **Acerto.**

- **Valor pedagógico das figuras:** 13 imagens, 11 com legenda integrada ao texto (p3–22). Figuras dos slides do professor estão presentes e funcionam como ancora mecanística (ondas de ciclina, controle de Wee1/Cdc25, cascata Rb-E2F, transição metáfase-anáfase). Da PARTE III em diante (p23+) **as figuras desaparecem** — Etapa 2/3 não têm figura, o que é esperado. Mas dentro da E1 já há vazio: §2.2 (p10–11) sobre Wee1/Cdc25/CAK/CKI **não tem figura** apesar de ser o pico de carga cognitiva — perda. Veredito: **bom mas com lacuna localizada.**

- **Densidade visual:** páginas 4 (581 palavras), 13 (470), 16 (536), 25 (327 — Resumindo, 2 colunas) são paredes de texto. Páginas com figura respiram. **Página 26 com 8 palavras é desperdício total** (vê §11 erro estrutural). Inserir respiro melhor distribuído.

- **Uso de cor:** badges de categoria (Consolidação/Integração/Aplicação) são coerentes. Banner gold do "Resumindo" identifica. Navy + dourado + cinza é paleta limpa. **Acerto.**

- **Cortes/overflow:** tabela §2.1 (p9–10) está **claramente quebrada** — colunas desalinham e conteúdo trespassa células. É bug de compilação Typst. Único corte grave detectado.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas que ALIMENTAM Phase F do REDATOR-E1)

### Técnica 1 — Box "Confusão clássica/recorrente" com inversão explícita

**Citação literal (p15, sobre Rb-E2F):**
> "Confusão recorrente: aluno acha que Rb ativa E2F e que fosforilar Rb inativa o sistema. **Exatamente o oposto.** Rb funciona como um freio sobre E2F: enquanto Rb está hipofosforilada, ela prende E2F e impede a expressão de S. Fosforilar Rb é soltar o freio."

**Nome da técnica:** *"box de inversão de polaridade"* — declara o erro literal que o aluno faz, marca com "exatamente o oposto" e reescreve a relação. Padrão repetido em 5 box-quadros (Rb-E2F, separase-coesina, p53-reparo, Wee1-Cdc25 par antagonista, ciclina-cofator).

**Quando NEBLI deveria usar:** sempre que houver uma relação onde A inibe B e a fosforilação/proteólise INVERTE a polaridade. Especialmente útil em: PFK-1 vs F-2,6-BP, glucagon vs insulina, Gs vs Gi, sympático vs parassimpático, ATP/ADP em alostérese. **Phase F do REDATOR-E1:** após terminar uma seção com inversão de polaridade, inserir box-quadro com fórmula "Confusão recorrente: aluno acha que X. Exatamente o oposto. [reescrita]".

### Técnica 2 — Reuso narrativo do mesmo motor em escalas crescentes

**Citação literal:** o conceito "feedback positivo + tudo-ou-nada" aparece 4 vezes no PDF — primeiro genérico (§1.4 "Tudo-ou-nada"), depois Wee1/Cdc25/M-CDK (§2.2), depois Rb/E2F/ciclina E (§3.1), depois SAC/APC/C (§3.3). Cada aparição usa o MESMO esqueleto ("loop amplifica → transição vira rampa íngreme → tudo-ou-nada") mas com peças moleculares novas.

**Nome da técnica:** *"motor reaproveitado em escalas crescentes"* — uma vez ensinado o esqueleto genérico, cada aplicação específica vira reconhecimento ("a mesma coisa do tudo-ou-nada, agora com Rb-E2F") em vez de mecanismo novo. Reduz drasticamente carga cognitiva.

**Quando NEBLI deveria usar:** identificar **1 motor genérico** por tema na Phase A do Tema Card e reusá-lo em pelo menos 3 lugares da E1. Para gliconeogênese: "bypass de reação irreversível" reusa em 3 bypasses. Para hemoglobina: "cooperatividade alostérica" reusa em O₂, CO₂, H⁺. **Phase F do REDATOR-E1:** ao redigir cada sub-seção, perguntar "esse motor já foi ensinado antes neste PDF? Se sim, ancorar como reconhecimento; se não, virar a aula desta sub-seção."

### Técnica 3 — Mini-resumos parciais ao final de cada sub-seção

**Citação literal (p14, fim do §2.4):**
> "Resumindo até aqui: Uma volta no ciclo, contada peça por peça: mitógenos → ciclinas D → G1-CDK → fosforila Rb → libera E2F → ciclina E → G1/S-CDK → SCF degrada p27 (ponto de restrição) → ciclina A → S-CDK replica → ciclina B → M-CDK [...]"

**Nome da técnica:** *"diagrama-em-prosa de fim de seção"* — cada sub-seção termina com uma cadeia de setas em prosa que comprime 2 páginas em 3 linhas. O aluno tem 4 oportunidades de reler "só o esqueleto" se perder o fio.

**Quando NEBLI deveria usar:** **toda** sub-seção da E1 (1.1, 1.2, ..., 3.4) com ≥1 cadeia mecanística DEVE terminar com "Resumindo até aqui: A → B → C → D" em prosa-com-setas. Não é o "Resumindo" global da p25; é o resumo-de-trecho que ancora a leitura linear. **Phase F do REDATOR-E1:** verificar que toda sub-seção fecha com esse bloco. Se a sub-seção não tem cadeia mecanística óbvia, declarar 1 frase-âncora ("Esta seção estabelece que X").

---

## 9. T3.10 — 7 erros NEBLI (calibração desta apostila)

| # | Erro | Status | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **PRESENTE (leve)** | Q26–Q30: correta com 35–55 palavras, distratoras com 25–45 — ratio ok. Mas Q29 (retinoblastoma) tem distratoras curtas (A=46pal mas D=35, E=correta=40); Q30 idem. Marginalmente dentro do canônico, mas precisa engordar as mais curtas. |
| 2 | Siglas sem #sigla() na 1ª aparição | **PRESENTE (invertido)** | Caso inverso: footnotes de CDK²/APC/C³/SCF⁴ aparecem em §1.2 (p4) ANTES de o corpo discutir mecanisticamente. NADH, ATP etc não aparecem (tema não invoca metabolismo). Casos detectados: CDK², APC/C³, SCF⁴, BrdU¹ (esse ok), CAK⁶, CKI⁷, UPS⁸, E2F⁹, Rb¹⁰, ORC¹¹, MCM¹², coesina¹³, p53¹⁴, SAC⁵. **Verificar se #sigla aparece na 1ª menção no corpo, não no 1º avistamento.** |
| 3 | Subagentes Opus falhando | **N/A** | Fix aplicado 2026-05-25; este resumo é histórico (gerado em outra sessão). Não há rastro de contaminação cruzada. |
| 4 | Heredoc ENAMETOOLONG | **N/A** | Não verificável no PDF; nenhuma evidência de truncamento (precompile-check teria pego). |
| 5 | `questao-ce` com tupla errada | **AUSENTE** | CE compilou: Q05, Q08, Q13, Q17, Q21 todas renderizam I/II/III/IV. Tuplas corretas. |
| 6 | Termo-notas abaixo do alvo (6–8) | **AUSENTE** | Contagem: 14 footnotes técnicas (CDK, APC/C, SCF, BrdU, CAK, CKI, UPS, E2F, Rb, ORC, MCM, coesina, p53, SAC). **Acima do alvo** — quase dobrado. Risco oposto: sobrecarga de termo-notas. Considerar consolidar (UPS pode ir no corpo, MCM/ORC ficam num único termo-nota "pré-RC"). |
| 7 | Tema-card com teto E1 errado | **PRESENTE (estrutural)** | E1 vai de p3 a p24 = **22 páginas**, exatamente no teto canônico. Não estouro, mas no limite. Sem espaço para uma segunda volta caso a revisão peça expansão. |

**Erros não-canônicos detectados nesta apostila** (entrar no checklist?):

8. **Gabarito desalinhado com as alternativas marcadas como corretas no enunciado.** 13 de 30 questões com gabarito errado (43%). Detalhado no §11.
9. **Header de seção fóssil** ("Etapa 4 — Questões de Fundamentos" na p55 com gabarito da E2 embaixo). Etapa 4 foi removida do pipeline em 2026-05-22.
10. **Páginas em branco** (p26 com 8 palavras; p55 termina com 82 palavras + área vazia). Bug de quebra de página Typst.
11. **Tabela quebrada §2.1** (p9–10): colunas desalinham e overflow visual.
12. **Sumário com 4 sub-itens por PARTE** quando canon = max 3.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (bloqueador)

1. **CORRIGIR GABARITO DA E2.** 13 questões com gabarito errado (Q02 A não B; Q03 D não E; Q04 D não A; Q07 A não B; Q09 C não D; Q12 B não E; Q13 CECE não CEEC; Q19 D não E; Q21 CEEC não CCEC; Q22 B não A; Q23 B não C; Q24 A não B; Q25 A não E). Aluno que usa este PDF como ferramenta de estudo aprende errado. **Bloqueador absoluto.** Reescrever `verificar_gabarito_ordem.py` para resumos NEBLI (hoje só roda para cadernos).
2. **Remover header fóssil "ETAPA 4 — QUESTÕES DE FUNDAMENTOS"** da página de gabarito (p55). Substituir por "GABARITO — ETAPA 2".
3. **Corrigir bug de quebra de página** que deixa p26 com 8 palavras e p55 cortada. Provável `#pagebreak()` duplicado após "Resumindo" e antes do gabarito.

### MECANÍSTICO (prioritário)

1. **Aliviar §2.2 (p10–11)**: cortar p15/p16/p18/p19/p57; manter só p21+p27. (~40% menos jargão sem perda de mecanismo.)
2. **Reposicionar footnotes CDK²/APC/C³/SCF⁴** de §1.2 (p4) para §2.1 onde entram no corpo.
3. **Inserir figura em §2.2**: "CDK com 4 chaves em série" (ciclina, CAK+, Wee1−, CKI−). Maior dívida visual do PDF.

### DIDÁTICO

1. **Reescrever 3 parágrafos** identificados em §3 deste relatório (footnotes-bloco no §1.2; sopa de proteínas §2.2; tabela quebrada §2.1).
2. **Promover Técnica 3 (mini-resumos por sub-seção) a regra do REDATOR-E1**: TODA sub-seção termina com "Resumindo até aqui: A → B → C". Já está em ~80% das sub-seções; falta em 1.1 e 2.1.
3. **Engordar distratoras de Q29 e Q30** (Aplicação clínica) para 35–55 palavras com mecanismo plausível-mas-errado.

### ESTÉTICO

1. **Refazer tabela §2.1** com `table()` nativo, colunas explícitas, células ≤6 palavras.
2. **Reduzir sumário para 3 sub-itens por PARTE** (p2). Combinar 1.3+1.4, 2.2+2.3, 3.3+3.4 nos rótulos.
3. **Cobrir páginas-paredão** (p4=581pal, p13=470, p16=536) com inserção de figura ou quebra suave.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **NÃO** — a apostila ENSINA muito bem (mecanismo, voz, boxes de inversão, mini-resumos), mas o gabarito errado em 43% das questões objetivas é defeito fatal de produto. Aluno que confia no gabarito aprende a versão errada. Como exemplar de **redação E1**, sim — vou minerar 3 técnicas (§T3.9). Como exemplar de **produto entregue**, não.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM** — 3 ESTRUTURAIS (gabarito errado; header fóssil; quebra de página). 3 MECANÍSTICOS (sopa §2.2; footnotes deslocadas; figura ausente §2.2).
3. **Seção para refazer:** §2.2 (Controle fino da CDK) + Etapa 2 gabarito completo + página 55 cabeçalho.
4. **Parágrafos para reescrever:** **3** — (a) bloco de footnotes CDK²/APC/C³/SCF⁴ no §1.2 p4; (b) sopa INK4/Cip-Kip no §2.2 p11; (c) tabela quebrada §2.1 p9–10.

---

[APROVAR COM RESERVAS — defeito de produto (gabarito) bloqueia uso em sala; redação da E1 é exemplar de alta qualidade e alimenta Phase F do REDATOR-E1 com 3 técnicas explícitas]

<!-- FIM-REVISAO-PROFUNDA -->
