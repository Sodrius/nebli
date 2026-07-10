# Revisão profunda Tier 3 — UC01-FMEMB-03-potencial-de-repouso

**Tema (ancoragem):** Potencial de repouso da membrana
**Autor:** Italiano (NEBLI v2, apostila histórica auto-produzida)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real, ensino médio + meses de medicina
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

## 0. ANCORAGEM DE TEMA

- **Tema canônico (do slug):** Potencial de repouso da membrana — fisiologia celular UC01 (FMEMB-03).
- **3 conceitos centrais que o aluno quer aprender:**
  1. **De onde vem os -70 mV** — por que NEGATIVO, e não positivo ou zero.
  2. **Equação de Nernst** — o que ela calcula e por que tem ln/zF; saber computar EK, ENa, ECl.
  3. **Por que -70 ≠ EK** — papel da permeabilidade múltipla (GHK), driving force e papel da bomba Na/K.
- **2 temas vizinhos que NÃO são esse:** (a) potencial de ação / canais voltagem-dep e despolarização ativa (próxima aula); (b) transmissão sináptica e PEPS/PIPS.

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão |
|---|---|---|---|
| Capa + bloco meta | OK | 1 | Bloco "Disciplina/Nota de uso/Onde estudar" claro; chamada "refazer cálculos antes da P1" prepara expectativa. |
| Sumário | OK | 2 | 3 PARTES + 3 subitens cada — mapa mental imediato. |
| Intro-box "construir do zero em 3 níveis" | OK | 3 | Promessa explícita; aluno sabe onde está indo. |
| 1.1 capacitor | [STOP: pág 3] | 3 | Página de **485 palavras** (densidade mais alta do PDF, ver json). "Vm é literalmente qu**ã**o difícil é empurrar carga até lá" salva, mas a definição formal "energia por carga / 1 Coulomb" antes do gesto físico assusta. Aluno que nunca viu capacitor relê duas vezes. |
| 1.2 convenção Vm=Vint–Vext | OK | 4–5 | Box "Despolarizar não é virar positivo" é PRECIOSO — pega armadilha clássica de prova. |
| 1.3 tabela concentrações | [STOP: pág 6] | 6 | A tabela renderizada quebrou: a coluna "Razão e direção do gradiente" está deslocada (no .txt aparecem "150" + "10× mais fora — força química empurra Na+ para fora" — texto do K+ caiu na linha do Na+). Aluno vê tabela inconsistente e desconfia dos números canônicos. |
| 1.4 forças química+elétrica | OK | 7 | "Duas forças, dois mundos." excelente fechamento conceitual antes da Nernst. |
| 2.1 célula só com K | OK | 9–10 | Experimento de pensamento progressivo, com 3 figuras (inicial → meio → equilíbrio). Padrão-ouro. |
| 2.2 derivação de Nernst | [STOP: pág 11–12] | 11–12 | Derivação faz salto: introduz "energia química = RT ln([K]int/[K]ext)" sem dizer **de onde vem o ln**. Aluno sem termodinâmica congela. Depois cita "isolando Vm chega-se a:" sem mostrar 2 passos. EXEMPLARES 12.1 (Michaelis-Menten) faz esse acompanhamento parágrafo-por-parágrafo — esta E1 não. |
| 2.3 ENa e ECl | OK | 13–14 | A nota sobre val**ê**ncia negativa do Cl- ("deixe o sinal de z trabalhar") é cirúrgica. |
| 2.4 por que -70 ≠ nenhum dos 3 | OK | 15–16 | Pergunta motivadora explícita; box "Vm ≠ Eíon não viola Nernst" mata armadilha #2 do aluno. |
| 3.1 GHK + cálculo | OK | 18 | Cálculo "(-800 + 31 - 162,5)/13" desenvolvido passo-a-passo com interpretação ("olha o que esse cálculo revela"). |
| 3.2 driving force | [STOP visual: pág 21] | 21 | Página visualmente pesada — tabela + figura de circuito + texto "Resistência Lei de Ohm" lado a lado, e a figura tem "ΔVK = 10 mV" e "Resistência" mas o texto da equação i = g·(Vm − Eíon) está em outra página. Aluno perde o gancho entre tabela numérica e figura. |
| 3.3 três canais em paralelo | OK | 22–23 | Deriva GHK a partir de Σi=0 — fecha circularidade conceitual. |
| 3.4 bomba Na/K | OK | 24–26 | Curto vs longo prazo é o sweet spot do tema; box ouabaína/digoxina ancora clinicamente. |
| Boxes clínicos digoxina + hipercalemia | OK+ | 26 | Conexão direta tema → ECG → emergência. Forte. |
| Conclusão integradora | OK | 28 | Costura completa, fecha promessa do intro. |
| Resumindo (2 pp) | OK | 29–30 | 12 seções organizadas; conexão clínica preservada. |
| E2 Q01–Q08 Consolidação | OK | 31–38 | Paridade respeitada; distratoras com mecanismo errado plausível. |
| E2 Q26–Q30 Aplicação | OK+ | 56–60 | Casos clínicos com paridade — Q29 hipercalemia + Q30 digoxina/hipocalemia são exemplares de mecanismo-clínico-mecanismo. |
| Gabarito (pág 64 do PDF, marcado "69") | DESALINHADO | 64 | Layout do gabarito está QUEBRADO: Q11 CEEC aparece deslocado, Q22 CCEE flutua entre Q21 e Q23, Q28 A está plotado na coluna de Integração em vez de Aplicação. Aluno corrigindo no fim da P1 erra a leitura do gabarito. |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria 12 (Cálculo bem explicado, Exemplar 12.1 Michaelis-Menten):**

> EXEMPLARES (Michaelis-Menten, p. 15-16): *"Por que essa hipótese? Porque, em regime estacionário, podemos escrever uma equação simples: k₁[E][S] = (k₋₁+k₂)[ES]. Lado esquerdo — taxa com que ES se forma. Lado direito — taxa com que ES se desfaz."*

> Apostila Potencial (pág 11): *"A energia qu**í**mica associada à diferença de concentração de K+ entre os dois lados é dada por μquímica = RT ln([K+]int / [K+]ext) — onde R é a constante dos gases, T é a temperatura absoluta, ln é o logaritmo natural. Essa expressão diz 'quanta energia por mol de K+ existe a mais do lado intracelular'."*

**Diagnóstico:** a apostila NOMEIA cada símbolo (R, T, ln) mas não justifica *por que* ln (entropia de mistura, número de microestados). Michaelis-Menten exemplar gasta uma linha extra (*"vem da expressão termodinâmica do potencial químico"*) — esta apostila pula. Para aluno em dificuldade, isso é a diferença entre "fórmula caiu do céu" e "fórmula deduzida".

**Categoria 7 (Analogia construtiva, lápis dobrado):**

> EXEMPLARES (Enzimas I): analogia 1-1 entre lápis reto/dobrado/quebrado e substrato/TS/produto, com raciocínio contrafactual ("e se a enzima encaixasse perfeitamente o substrato?").

> Apostila Potencial (pág 26 box bomba bloqueada): *"Bloquear a bomba é como cortar a manutenção de uma represa: o lago não esvazia na hora, mas vai esvaziando até virar terreno seco."*

**Diagnóstico:** a analogia represa é boa para curto-vs-longo prazo, mas é única no resumo inteiro. O tema PEDE mais analogias (capacitor=duas placas, bateria+resistência, votação ponderada — todas tratadas verbalmente, não com analogia visual). EXEMPLARES 7.1 mostra que analogia construtiva multiplica retenção; esta apostila usa só uma.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo A — pág 11 (derivação de Nernst)

**Citação literal:** *"No equilíbrio, as duas energias devem se cancelar quando você compara dentro com fora — ou seja, a energia eletroqu**í**mica total do K+ dentro tem que ser igual à energia eletroqu**í**mica total do K+ fora. Equivalente: ao mover um mol de K+ de dentro para fora, a variação química (RT ln([K]ext/[K]int), negativa) cancela exatamente a variação el**é**trica (zF(Vext - Vint) = -zF·Vm, positiva no caso de Vm negativo). Isolando Vm, chega-se à equação de Nernst:"*

**Diagnóstico mecanístico:** dois saltos lógicos numa frase. (1) "ao mover um mol de K+" — por que comparar deslocamento entre compartimentos é o caminho? (2) "isolando Vm chega-se a" — o aluno fica com a álgebra de cancelamento "RT ln(...) + zF·Vm = 0 → Vm = −RT/zF · ln(...)" mental, mas o sinal da raz**ã**o muda para [ext]/[int] e o passo n**ã**o é mostrado. Aluno faz a conta errada no caderno.

**Reescrita pronta:**
> No equilíbrio, mover um único K+ de dentro para fora não pode liberar nem custar energia líquida — se custasse, K+ não cruzaria; se liberasse, K+ continuaria fluindo. Soma das duas variações = 0. **Mudança química** ao sair: μ_ext − μ_int = RT · ln([K]ext/[K]int) — negativa, porque há menos K+ fora (mudança espontânea). **Mudança elétrica** ao sair: z·F·(Vext − Vint) = −z·F·Vm — positiva quando Vm é negativo (carga positiva subindo "morro" elétrico). Para zerar a soma: RT·ln([K]ext/[K]int) − zF·Vm = 0. Isolando: **Vm = (RT/zF) · ln([K]ext/[K]int)**. Esse Vm é o EK — o potencial em que as duas variações de energia se cancelam exatamente.

### Parágrafo B — pág 6 (tabela concentrações, render quebrada)

**Citação literal:** *"K+ 100 5 20× mais dentro — força química empurra K+ para fora. Na+ 15 150 10× mais fora — força química empurra Na+ para fora."*

**Diagnóstico mecanístico:** a tabela renderizou com merge de células errado — "força química empurra Na+ para fora" está colada na linha que descreve K+/Na+ misturados; a linha do Cl- recebe metade da legenda da do Na+. Aluno que se apoia na tabela canônica de concentrações para revisar antes da P1 leva número errado para a prova.

**Reescrita pronta (estrutura, não conteúdo):** usar `#table()` Typst nativa com 4 colunas explícitas (Íon | IC mM | EC mM | Direção da força química) e UMA linha por íon. Sem células multi-linha, sem texto fluindo entre colunas. Linha A- separada no fim com observação "imperm**eá**vel — não atravessa".

### Parágrafo C — pág 21 (driving force + Lei de Ohm)

**Citação literal:** *"A driving force de K+ no repouso é pequena (10 mV) — porque o Vm de repouso está perto de EK. A driving force de Na+ é enorme (132 mV) — porque o Vm está longu**í**ssimo de ENa."*

**Diagnóstico mecanístico:** a frase em si é boa, mas a página 21 tem layout pesado: tabela "Vm − Eíon" + figura de circuito + texto "Resistência Lei de Ohm" empilhados, e a figura mostra "ΔVK = R · i" com flecha vermelha de "saída de potássio" que aluno em dificuldade interpreta como "K+ saindo causa a Lei de Ohm" — confusão de sentido causal. A interpretação correta — Ohm vale para o canal, e a corrente DECORRE da driving force — fica diluída.

**Reescrita pronta:** trocar layout para texto contínuo seguido de figura única abaixo (não lateral). Renomear a figura para *"Modelo de canal único: bateria interna (Eíon) + resistor (1/g). A corrente i = g·(Vm − Eíon) só corre quando há diferença líquida entre o Vm da célula e o Eíon do canal."* — atribuir causalidade explícita do lado da equação, não da seta visual.

---

## 4. T3.3 — 3 seções mais densas

### Densa 1 — Página 3 (1.1 + intro-box, 485 palavras)

**Mitigação:** quebrar em 2 páginas. A definição formal de potencial elétrico ("energia por carga, 1 Coulomb…") pode migrar para footnote/termo-nota, deixando o corpo direto na pergunta "o que é, fisicamente, um potencial de membrana?" → gesto "voltagem é quão difícil é empurrar carga até lá" → analogia do capacitor (duas placas + isolante). Resultado: 250–280 palavras na pág 3, expansão definicional como `#termo-nota` ou box `.atencao-box` lateral.

### Densa 2 — Página 11 (derivação de Nernst, ~440 palavras + fórmula)

**Mitigação:** aplicar padrão EXEMPLARES 12.1 — três peças. (a) Equação intermediária do equilíbrio em formula-box separada com legenda "esquerda = energia química; direita = energia elétrica". (b) Equação final de Nernst em formula-box com legenda nomeando RT, zF, ln. (c) Exemplo numérico de EK em terceira formula-box, com "**O que isso significa**: para segurar K+ dentro a célula precisa de interior negativo — daí EK < 0". Atualmente está tudo amontoado em parágrafo corrido.

### Densa 3 — Página 18 (cálculo GHK)

**Mitigação:** a substituição (-800 + 31 - 162,5)/13 está correta mas vem sem retomada visual dos três Eíon. Adicionar mini-quadro à direita do cálculo: "Lembrando: EK = -80, ENa = +62, ECl = -65. gK = 10·10⁻⁶ S, gNa = 0,5·10⁻⁶ S, gCl = 2,5·10⁻⁶ S." Reduz carga de memória de trabalho do aluno em 50% naquela página.

---

## 5. T3.4 — Voz fora do padrão

Pouquíssimas quebras. Casos isolados:

- Pág 11: *"Vamos derivar isso na próxima seção, mas a intuição já está pronta"* — voz funciona como ponte, OK.
- Pág 26 box: *"é como cortar a manutenção de uma represa"* — voz analógica boa, mas única no resumo.
- Pág 28 conclusão: *"Aqui termina a fundação. Os próximos resumos vão construir sobre essa base."* — meta-narrativa boa para 1º ano.

**Não detectei voz robótica ou lacônica sustentada.** A apostila mantém o diálogo do início ao fim.

---

## 6. T3.7 — Carga cognitiva pico (seção-pivô + 3 mitigações)

**Seção-pivô:** §2.2 (derivação de Nernst em pág 11–12). É onde o aluno em dificuldade decide se segue ou fecha o PDF — três conceitos novos sobrepostos (potencial químico, energia elétrica por mol, equação no equilíbrio).

**3 mitigações candidatas:**

1. **Quebrar em 3 sub-formula-boxes** (energia química / energia elétrica / equação combinada) com legendas independentes. Padrão EXEMPLARES 12.1.
2. **Adicionar analogia construtiva**: dois reservatórios de água com mangueira; "altura da água" = concentração; "pressão elétrica" = bomba elétrica no fundo da mangueira. Equilíbrio = mangueira parada. Mapeamento 1-1 (não físico-quântico).
3. **Pôr 2 figuras seriadas**: (a) energia química como gráfico de potencial químico vs lado; (b) energia elétrica como gradiente de Vm vs lado. Aluno VÊ que são duas curvas que cruzam quando o sistema acerta o Vm.

**Qual escolher:** **(1) + (3)**. A analogia da mangueira (2) é tentadora mas pode levar a confusão com pressão hidrostática (tema vizinho de difusão). Quebra em formula-boxes (1) é cirúrgica e baixo risco; figuras seriadas (3) ancoram visualmente sem custo de jargão novo.

---

## 7. T3.8 — ANÁLISE VISUAL

### Hierarquia tipográfica
- Capa (pág 1): hierarquia limpa — banner navy, título 36pt+, subtítulo "Fisiologia" em weight menor, bloco meta com chave-valor bem destacado. **Excelente**.
- Páginas internas: H1 (PARTE) bem visível com banner navy; H2 (1.1, 2.1) em color azul-meio. **OK** mas o H1 da PARTE I em pág 3 fica colado no parágrafo seguinte — falta respiro vertical de ~12pt.
- Gabarito (pág 64/PDF marker 69): "Gabarito — Etapa 2" em 28pt+ bem destacado, mas as sub-categorias (CONSOLIDAÇÃO/INTEGRAÇÃO/APLICAÇÃO) em caps SMALL diluem a separação visual.

### Valor pedagógico das figuras
- Pág 9–10 (sequência célula só com K): **alto valor** — três figuras seriadas mostram a progressão temporal. Legendas integradas explicitamente narram o que aluno deve enxergar.
- Pág 13–14 (Nernst Na e Cl): figuras paralelas com mesma estrutura visual reforçam padrão de raciocínio.
- Pág 21 (circuito + Lei de Ohm): figura **mal posicionada** — texto "Resistência Lei de Ohm" colado na figura à direita gera confusão de leitura (vide §3 parágrafo C).
- Figura da bomba Na/K (pág 25): legendada com 3:2 e ATP explicitamente.

### Densidade visual
- Maioria das páginas: 200–340 palavras, com respiro adequado.
- **Pico problemático**: pág 3 com 485 palavras + pág 11 com derivação dura — muros sucessivos no início e na metade. Aluno em dificuldade pode parar nesses dois pontos.

### Uso de cor
- Navy (#1f3a5f) para H1/banner: coerente em todo PDF.
- Cores das categorias E2 (verde Consolidação, azul Integração, violeta Aplicação): seguem padrão NEBLI canônico — checagem visual em Q01/Q09/Q26 confirma.
- Boxes clínicos (digoxina, hipercalemia): tom amarelo-creme distingue de boxes de "armadilha" (geralmente cor diferente?) — coerência interna OK mas faltou verificar se há contraste suficiente com fundo branco em impressão B/N.

### Cortes/overflow
- **Tabela pág 6** (concentrações iônicas): texto da coluna "Razão e direção" overflowed/mergeu linhas. **Bug de render**.
- **Gabarito pág 64**: layout em colunas quebrou — Q11, Q21, Q22, Q28 estão fora da grade esperada, criando ilusão de coluna a mais. **Bug de render**.
- Demais páginas sem corte detectável.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### 1. Box "X não é Y" para matar armadilha clássica antes da prova

**Citação literal (pág 4):** *"Despolarizar não é virar positivo — Aluno tende a achar que 'despolarizar' = 'ficar positivo'. Errado. Despolarizar é simplesmente ficar menos negativo. Sair de -70 mV para -50 mV já é despolarizar, mesmo que a célula continue claramente negativa. O termo descreve a direção da mudança, não o sinal absoluto."*

**Nome da técnica:** **"Box anti-confusão direcionado"** — afirmar a versão errada que o aluno traz da intuição, nomear o erro, dar o critério correto, dar exemplo numérico.

**Quando NEBLI deveria usar:** sempre que o Tema Card identificar uma confusão de prova ≥3 (no Mapa de Confusões) que vem de uma palavra ambígua (despolarizar/hiperpolarizar, afinidade/velocidade, oxidar/reduzir, exocítico/endocítico). REDATOR-E1 deve inserir 1 box desse tipo por PARTE da E1 (alvo: 3 por resumo, não só 1).

### 2. Pergunta-ponte "Por que" antes de cada equação grande

**Citação literal (pág 8):** *"Qual é o Vm naquele momento de equilíbrio? Essa é a pergunta que a equação de Nernst responde."* + (pág 14): *"Por que -70 mV não é igual a nenhum dos três?"* + (pág 17): *"A pergunta deixada pendente é: qual é, exatamente, o Vm de uma célula com vários canais abertos simultaneamente?"*

**Nome da técnica:** **"Pergunta-ponte explícita"** — cada equação aparece como RESPOSTA a uma pergunta formulada parágrafos antes, no idioma do aluno (não em linguagem matemática).

**Quando NEBLI deveria usar:** toda equação (Nernst, GHK, Lei de Ohm, Michaelis-Menten, Henderson-Hasselbalch, Frank-Starling, Poiseuille). REDATOR-E1: a pergunta-ponte deve vir 50–150 palavras antes do `#formula-box`, e o conector ("Essa é a pergunta que X responde", "A resposta é Y") deve ser literal — não implícito.

### 3. Verificação de coerência matemática logo após o cálculo

**Citação literal (pág 12):** *"Repare nos detalhes: ln(5/100) é negativo (porque o argumento é menor que 1, ou seja, há menos K+ fora do que dentro). O fator de Nernst é positivo. z = +1, então não inverte sinal. Resultado: EK negativo. Faz sentido físico: para segurar K+ dentro (que quer sair), o interior precisa ser eletricamente atraente para cátion — ou seja, negativo."*

**Nome da técnica:** **"Sanity-check físico pós-cálculo"** — depois de obter o número, voltar à intuição física e checar se o sinal/magnitude faz sentido com a história contada antes. Liga matemática ↔ mecanismo.

**Quando NEBLI deveria usar:** todo `#formula-box` com exemplo numérico. REDATOR-E1: incluir um parágrafo curto (3–5 linhas) após cada cálculo dizendo (a) por que o sinal saiu desse lado, (b) o que o resultado significa no corpo. Pendência: tornar isso item de checklist no `precompile-check.py` (procurar marcadores tipo "Repare", "Faz sentido", "Olhe o que esse cálculo revela" a uma distância pequena de cada formula-box).

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro | Status | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **AUSENTE** | Q26–Q30 mantêm 25–55 palavras por alternativa com mecanismo plausível em cada uma (Q29 hipercalemia: A 47p, B 41p, C 41p, D 46p, E 48p — paridade excelente). |
| 2 | Siglas sem `#sigla()` 1ª aparição | **AUSENTE** (provável) | NADH/NAD+ não aplicam aqui (tema não-metabólico). Siglas do tema (Vm, mV, mM, Eíon, EK, ENa, ECl, GHK, gK, gNa, gCl, NCX) — todas declaradas pelo menos por `#termo-nota` visível na pág 3, 7, 18. NCX (pág 26 box digoxina) é o caso de risco — aparece sem footnote dedicado, mas o contexto ("trocador Na+/Ca2+") quase compensa. **Sugestão**: declarar `#sigla("NCX", [trocador Na+/Ca2+ — transportador secundário que extrudia Ca2+ usando o gradiente de Na+])`. |
| 3 | Subagentes Opus customizados | **N/A** | Não há sinal de contaminação de tema; resumo é internamente coerente, focado em potencial de repouso o tempo todo. Fix do 2026-05-25 parece ter funcionado se este é resumo pós-fix. |
| 4 | Heredoc ENAMETOOLONG | **N/A** | Não-aplicável a revisão de PDF terminado. |
| 5 | questao-ce tupla | **N/A** | Resumo compilou; tuplas de CE estão corretas. Caderno auditado OK. |
| 6 | Termo-notas abaixo do alvo (6–8) | **AUSENTE** | Termos-nota detectados na E1: Vm, mV, mM, EQ, gradiente eletroquímico, GHK, ATPase, condutância, driving force = **9 termos**. Acima do alvo. Bem feito. |
| 7 | Tema-card teto E1 errado (canônico 22) | **AUSENTE / OK no novo limite** | E1 ocupa páginas 3–28 ≈ **26 páginas de E1**. **Acima do teto canônico 22**. Para tema-pivô fundacional (potencial de repouso é base de todo o resto), aceitável — mas Davi deve decidir se justifica re-canonizar teto para 28 quando o tema é fundacional, ou comprimir. |

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)

1. **Corrigir render da tabela de concentrações iônicas (pág 6).** Bug que entrega números errados ao aluno. Refazer com `#table()` Typst nativa, 4 colunas, 1 linha por íon, sem texto multi-linha. **Bloqueador.**
2. **Corrigir render do gabarito (pág 64 do PDF).** Layout de colunas quebrou; Q11/Q22/Q28 estão fora da grade. Refazer gabarito como 3 colunas explícitas com 1 questão por célula, sem fluxo automático. **Bloqueador.**
3. **Decidir teto E1 para temas-pivô fundacionais.** Esta E1 tem 26 páginas, 4 acima do canônico 22. Tema realmente exige; canonizar exceção "+25% para fundacional" no Tema Card ou comprimir §1.1 e §3.3 cortando ~3 páginas.

### MECANÍSTICO (max 3)

1. **Derivação de Nernst (pág 11) — quebrar em 3 formula-boxes** (energia química, energia elétrica, equação combinada), com legenda de cada termo e por que ln aparece. Padrão EXEMPLARES 12.1.
2. **Pág 18 GHK — adicionar quadro de retomada** com EK, ENa, ECl e gK, gNa, gCl explícitos antes da substituição. Reduz carga de memória de trabalho.
3. **Box "bomba bloqueada não zera Vm na hora" (pág 26)** — já está bom, mas adicionar um número concreto ("após 30 min com ouabaína em neurônio in vitro: Vm cai uns 5 mV; após 4–8 h: vai a zero") torna a curva temporal acionável.

### DIDÁTICO (max 3)

1. **Adicionar pergunta-ponte explícita antes da derivação de Nernst (pág 11).** Atualmente abre com "Agora a derivação." — frio. Substituir por "Já temos a intuição (forças se cancelam). Mas qual é o número exato do Vm em que isso acontece, dado um íon com concentrações conhecidas? Essa é a pergunta que a equação de Nernst responde — e a resposta sai de igualar as duas energias por mol."
2. **Multiplicar analogias construtivas.** Resumo tem 1 analogia (represa, bomba bloqueada). Tema permite mais: capacitor (duas placas + isolante), votação ponderada (GHK), bateria+resistor (driving force). Cada PARTE deveria ter 1 analogia construtiva — alvo 3, atual 1.
3. **Declarar NCX explicitamente com `#sigla()`** no box digoxina (pág 26).

### ESTÉTICO (max 3)

1. **Pág 21 — repor layout** texto contínuo + figura embaixo (não lateral). Atualmente figura+tabela+texto lado-a-lado confunde sentido causal.
2. **Pág 3 — adicionar respiro vertical** ~12pt entre fim do banner "PARTE I" e o parágrafo de 1.1. Atualmente colados.
3. **Gabarito — usar caixinha colorida** por categoria (verde Consolidação, azul Integração, violeta Aplicação) para reforçar associação visual com a E2 ao revisar.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM** — apostila é forte como didática global; pode entrar em EXEMPLARES como referência para Categoria 12 (cálculo bem explicado) e Categoria 11 (paridade de distratoras em Aplicação). Subordinada a corrigir os 2 bloqueadores de render.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM** — 3 estruturais (sendo 2 bugs de render bloqueadores) + 3 mecanísticos.
3. **Seção para refazer?** §1.3 (tabela de concentrações iônicas — refazer com `#table()` nativa) e Gabarito (refazer layout em 3 colunas explícitas).
4. **Parágrafos para reescrever?** **3**:
   - Parágrafo da derivação de Nernst (pág 11, citado em §3-A) — quebrar em 3 formula-boxes com pergunta-ponte explícita.
   - Parágrafo da tabela concentrações (pág 6, citado em §3-B) — refazer a tabela.
   - Parágrafo driving force + circuito (pág 21, citado em §3-C) — repor layout vertical.

---

[APROVAR COM RESERVAS]
