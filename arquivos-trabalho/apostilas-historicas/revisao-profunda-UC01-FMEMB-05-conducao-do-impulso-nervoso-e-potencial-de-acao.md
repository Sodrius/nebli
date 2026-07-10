# Revisão profunda Tier 3 — UC01-FMEMB-05-conducao-do-impulso-nervoso-e-potencial-de-acao

**Tema (ancoragem):** Condução do impulso nervoso e potencial de ação (Fisiologia, UC1, P2)

**3 conceitos centrais que o aluno-alvo quer aprender:**
1. Por que o sinal precisa virar PA — qual o limite físico da corrente passiva que justifica a invenção do PA.
2. Como Na voltagem e K voltagem se coreografam no tempo para gerar a forma do PA (upstroke, pico, downstroke, undershoot) — e por que os três estados do Na (fechado→aberto→inativado→fechado) são a chave.
3. Como mielina muda Rm e Cm, gera condução saltatória, e como EM/Guillain/hipocalcemia caem direto desse mecanismo.

**2 temas vizinhos que NÃO são esse:** transmissão sináptica (Ca²⁺ pré-sináptico, neurotransmissor, receptor — FMEMB-06); potencial de repouso/Nernst (FMEMB-03 — apenas recapitulado, não derivado aqui).

**Autor:** Italiano (apostila histórica antes do pipeline NEBLI atual)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real com biofísica de membrana, ensino médio + meses
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25
**PDF:** 53 páginas, 15 931 palavras, 32 imagens, média 300,6 palavras/página
**Páginas amostradas:** 1, 2, 3, 5, 7, 17, 53
**Nota metodológica:** `pdftoppm` indisponível no sandbox — análise visual feita por triangulação entre (a) JSON de estrutura com contagem de imagens por página, (b) marcações textuais (legendas das figuras preservadas no .txt, boxes nominalmente identificados, banners "RESUMINDO"/"ETAPA"), (c) distribuição densidade-palavras × imagens página-a-página.

---

## 1. Pontos de parada (simulação linha-a-linha do aluno-alvo)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Abertura ("Imagine um neurônio sensorial no seu pé...") | SEGUE | 3 | Pergunta de partida concreta + escala humana (um metro) + nome da solução (PA) no fim do parágrafo. Engata. |
| 1.1 Recap λ e τ — "constante de espaço" sem derivar | SEGUE | 3–4 | Autor anuncia "sem refazer a derivação" e devolve a fórmula com gesto físico (`V(x) = V₀·e^(-x/λ)`, "em λ cai a 37%"). Aluno-alvo aceita por confiança. |
| 1.1 — "axônio gigante do lula, 1 mm" | SEGUE | 4 | Ancoragem comparativa concreta. Boa. |
| 1.2 — iC vs iR e τ = Rm·Cm | **[STOP curto: p.5]** | 5 | A frase "no primeiro instante quase toda a corrente vai carregar o capacitor — ou seja, im ≈ iC, e iR ≈ 0. Isso significa que nenhuma variação de potencial ocorre ainda" é contraintuitiva sem analogia. Aluno-alvo lê "se a corrente está entrando, por que Vm não muda?" e trava. Falta uma analogia mecânica (tipo "encher uma piscina com fundo furado: enquanto a água ainda está enchendo a parede, ainda não vaza pelo fundo"). |
| 1.2 — t=τ e t=3τ com legenda numérica | SEGUE | 6 | Recupera. Os dois "snapshots" (-69 mV → -60 mV) dão gesto temporal concreto. |
| 1.3 Solução: canais Na voltagem | SEGUE | 7 | "Reescrever o sinal a cada µm" é frase-síntese arquetípica. |
| 1.3 — "limiar = ponto onde Na entrando supera K saindo" + box "Limiar não é Vm de equilíbrio" | SEGUE | 9–10 | Box desfaz confusão clássica explicitamente. Forte. |
| 2.1 Canal Na — "4 domínios, S1–S6, S4 positivo" | **[STOP estrutural: p.11]** | 11 | Aqui é o STOP mais sério das primeiras 15 páginas. O aluno-alvo cai num bloco de anatomia molecular (I/II/III/IV, S1–S6, S4 com argininas e lisinas) sem ancoragem prévia. O autor passa de "imagina uma proteína que abre com voltagem" direto para "quatro domínios homólogos com seis transmembranas cada". Falta uma metáfora estrutural (tipo "imagina quatro mãos segurando o poro, cada mão com seis dedos, e o quarto dedo de cada mão é carregado positivo") antes da nomenclatura. |
| 2.1 — três estados (F→A→I→F) | SEGUE | 12 | "Aqui está a sacada que muitos alunos perdem: TRÊS estados, não dois" — chamada didática explícita ao aluno-alvo. Pedagogicamente certeira. |
| 2.1 — comporta m vs comporta h | SEGUE | 12–13 | Distinção citoplasma vs face interna fica clara. Box "Inativado ≠ fechado" também. |
| 2.2 Canal K — "10× mais lento, sem inativação" | SEGUE | 14 | Comparação direta com o Na funciona como atalho. |
| 2.3 Cinética PA passo a passo (10 frames) | SEGUE | 16–19 | **Ponto alto da apostila.** Cada frame com legenda numérica (Vm, qual canal está fazendo o quê) — coreografia rastreável momento-a-momento. Aluno consegue acompanhar mesmo com dificuldade. |
| 2.3 — pico não atinge ENa | SEGUE | 18 | "Os três coisas se equilibram momentaneamente" — desfaz outra confusão clássica. |
| Box "Na/K-ATPase NÃO faz o PA" + curiosidade <0,01% | SEGUE | 20 | Excelente: ataca a confusão metabólica clássica com número concreto que cola. |
| 3.1 Refratários absoluto e relativo | SEGUE | 21–22 | Linkagem direta com a comporta h vista em 2.1. Bem amarrada. |
| 3.2 AIS — "primeiros 20–50 µm, densidade 100–1000× maior" | SEGUE | 23–24 | Concreto, ancorado em número. |
| 3.2 Codificação por frequência | SEGUE | 24–25 | Box "Intensidade não altera amplitude" — clássica armadilha desarmada. |
| 3.3 Mielina, Rm↑ Cm↓ | SEGUE | 26–27 | Capacitor de placas paralelas (C = ε₀·A/d) **é apresentado com a mesma elegância que C1 do EXEMPLARES**: fórmula + gesto físico ("afasta as placas → d↑ → C↓"). |
| 3.3 Condução saltatória + box "saltatória não é literal" | SEGUE | 28–29 | Desfaz mito de propaganda. Forte. |
| EM, Guillain, hipocalcemia (3 boxes clínicos) | SEGUE | 29–30 | Cada síndrome ancorada no parâmetro biofísico que falhou. Pedagogia top: o aluno-alvo finalmente sente que a clínica "cai do mecanismo". |
| Conclusão integradora (PARTE I + II + III) | SEGUE | 31 | Recapitula com as três perguntas-âncora respondidas. |
| Resumindo (2 páginas, 8 seções) | SEGUE | 32–33 | Cada cápsula com sujeito+verbo+complemento, sem aglomerado de siglas. |
| Etapa 2 Q01–Q25 (Consolidação + Integração) | SEGUE | 34–51 | Distratoras mecanísticas, correta tem mecanismo, paridade razoável. |
| Etapa 2 Q26–Q30 (Aplicação) | **[STOP cognitivo a confirmar]** | 51–? | Suspeita do "erro 1 do NEBLI" — não consegui ler integralmente as discursivas no .txt, mas o padrão histórico do italiano (visto em FMEMB-02) é distratoras curtas vs correta longa em Aplicação. Investigar. |

**Total de STOPs:** 3 confirmados (1 menor em p.5, 1 estrutural em p.11, 1 cognitivo a confirmar p.51+). O PDF é robusto — STOPs são solucionáveis com 1–2 frases de analogia mecânica ou metáfora estrutural por parada.

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categorias relevantes selecionadas:** C1 (mecanismo parágrafo-por-parágrafo), C2 (pergunta motivadora), C4 (magnitudes ancoradas), C7 (analogia construtiva), C13 (boxes clínicos a partir do mecanismo).

### Comparação 1 — Abertura (C2: pergunta motivadora)

**Citação do italiano (p.3):**
> "Imagine um neurônio sensorial no seu pé. O receptor de pressão na ponta do dedo detecta que você pisou em algo, gera uma pequena despolarização, e essa informação precisa subir um metro inteiro até chegar ao encéfalo — sem perder amplitude, sem se diluir no caminho. Se o sinal viajasse simplesmente como uma corrente passiva pela membrana, ele não chegaria: a cada milímetro, a capacitância da membrana o engole e a resistência do axoplasma o vaza."

**Padrão C2 (EXEMPLARES):** pergunta concreta, com escala humana, antes da nomenclatura.

**Veredito:** italiano executa o padrão **igual ou melhor** que o exemplar — escala humana (pé→encéfalo, um metro), antagonista físico nomeado (capacitância e resistência) **antes** de dar a solução. NEBLI deveria copiar essa abertura quando o tema for "por que precisamos de X".

### Comparação 2 — Mecanismo da mielina (C1 + C7)

**Citação do italiano (p.27):**
> "Como a capacitância depende da geometria. Para um capacitor de placas paralelas, C = ε₀ · A / d, onde A é a área e d é a distância entre as placas. Quanto maior d, menor C. A mielina faz exatamente isso — afasta as placas (face citoplasmática × face externa), aumentando d e diminuindo Cm."

**Padrão C1+C7 (EXEMPLARES):** fórmula com gesto físico imediato + analogia mecânica que cola.

**Veredito:** italiano **iguala o exemplar arquetípico de C7**. A fórmula vem com a interpretação ("d↑ → C↓") na mesma frase, e a aplicação ("mielina afasta as placas") aparece **antes** de o aluno perguntar "tá, mas o que isso tem a ver com a fisiologia". REDATOR-E1 do NEBLI deveria absorver: **toda fórmula traz o gesto físico junto, no mesmo parágrafo**.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação obrigatória)

### Parágrafo fraco 1 — abertura da seção 2.1 (canal de Na, anatomia)

**(a) Citação literal (p.11):**
> "Vamos abrir o canal de Na voltagem-dependente. Estruturalmente, é uma proteína única que atravessa a membrana com quatro domínios homólogos (chamados de I, II, III e IV). Cada domínio tem seis segmentos transmembranares (S1-S6), e o S4 de cada domínio é positivamente carregado (rico em argininas e lisinas)."

**(b) Diagnóstico mecanístico:** despeja três níveis de nomenclatura (I/II/III/IV, S1–S6, S4 com arginina/lisina) **sem analogia mecânica prévia**. Aluno-alvo, que nunca viu uma proteína de canal antes, não tem onde encaixar essa hierarquia. Viola o erro #7 do NEBLI: nome técnico **depois** do mecanismo entendido.

**(c) Reescrita pronta:**
> "Vamos abrir o canal de Na voltagem-dependente. Imagina uma proteína em forma de quatro mãos fechadas em torno de um poro central — cada mão idêntica às outras três, e cada uma com seis dedos que atravessam a membrana. O dedo número 4 de cada mão é especial: ele carrega cargas positivas (resíduos de arginina e lisina), e é ele que vai sentir a voltagem. Quando a membrana está em repouso (-70 mV, interior negativo), o dedo 4 fica puxado para dentro pelo potencial negativo. Quando despolariza, o dedo 4 desliza para fora — e esse movimento mecânico abre a comporta do poro. Os anatomistas chamam as quatro mãos de domínios I, II, III e IV; e os seis dedos de segmentos S1–S6. Mas o que importa funcionalmente é o S4 — o sensor de voltagem."

### Parágrafo fraco 2 — explicação do τ = Rm·Cm em t=1τ

**(a) Citação literal (p.6):**
> "No primeiro instante após o estímulo, quase toda a corrente vai carregar o capacitor — ou seja, im ≈ iC, e iR ≈ 0. Isso significa que nenhuma variação de potencial ocorre ainda: a corrente está separando cargas nas duas faces da membrana, mas isso por si só ainda não mudou a diferença de potencial (porque o capacitor está carregando, não foi descarregado)."

**(b) Diagnóstico mecanístico:** o autor afirma que "nenhuma variação de potencial ocorre ainda" — mas isso é factualmente impreciso e didaticamente contraintuitivo. Carregar um capacitor **é exatamente** o que muda Vm (Vm = Q/C). A frase deveria dizer "Vm sobe lentamente porque a corrente está dividida entre encher o capacitor (atrasando) e vazar pelo Rm". Como está, deixa o aluno-alvo num paradoxo: "se corrente está entrando, alguma coisa tem que mudar".

**(c) Reescrita pronta:**
> "No primeiro instante após o estímulo, quase toda a corrente entrante vai 'encher' o capacitor — ou seja, im ≈ iC, e iR ≈ 0. Isso significa que Vm sobe muito devagar no início: a corrente está sendo gasta separando cargas nas duas faces da bicamada, e cada elétron empilhado na face interna corresponde a um aumento mínimo de Vm (porque a capacitância é grande, e Vm = Q/C). Pensa numa piscina enchendo por uma mangueira fina enquanto o fundo é meio poroso: nos primeiros segundos, a água enche o volume da piscina (carrega o capacitor) mais do que vaza pelo fundo (iR). Só depois que o capacitor está parcialmente cheio é que a tensão começa a subir de forma perceptível, e a corrente passa a vazar via Rm. Esse tempo característico é o τ = Rm · Cm."

### Parágrafo fraco 3 — bloco "Hipocalcemia e sinal de Chvostek" (densidade)

**(a) Citação literal (p.30):**
> "Pacientes em hipocalcemia (após tireoidectomia, pancreatite, insuficiência renal) frequentemente desenvolvem espasmos musculares involuntários, parestesias periorais e o famoso sinal de Chvostek (contração da face ao percutir o nervo facial). O mecanismo é biofísico: o Ca²⁺ extracelular tem um efeito de 'estabilização' sobre o sensor S4 do canal de Na voltagem — chamado de efeito de screening eletrostático."

**(b) Diagnóstico mecanístico:** o box é bom no diagnóstico (4 causas listadas, 3 sintomas, mecanismo nomeado), mas o **mecanismo do screening eletrostático** é tratado como caixa-preta. Aluno-alvo lê "efeito de screening eletrostático" e fica com a sensação de que foi rótulo, não explicação. A footnote 27 expande, mas chega tarde — aluno já está atravessando para o próximo parágrafo.

**(c) Reescrita pronta:**
> "...o Ca²⁺ extracelular tem um efeito de 'estabilização' sobre o sensor S4. Pensa assim: o S4 carrega cargas positivas e fica solto quando o interior despolariza. O Ca²⁺ extracelular, sendo divalente (2+), 'gruda' eletrostaticamente no entorno da face externa da membrana e segura o S4 no lugar de repouso — funciona como um peso eletrostático que dificulta o S4 deslizar para fora. Esse 'segurar' é o que os biofísicos chamam de screening eletrostático. Quando o Ca²⁺ extracelular cai (hipocalcemia), o S4 fica sem o peso, e basta uma despolarização pequena para ele deslizar e abrir o canal Na. Resultado: o limiar desce, a membrana fica hiperexcitável — espasmos espontâneos, tetania, sinal de Chvostek."

---

## 4. T3.3 — 3 seções mais densas (palavras × imagens)

| Seção | Pág | Palavras | Imagens | Densidade | Mitigação concreta |
|---|---|---|---|---|---|
| Conclusão integradora (final E1) | 31 | 487 | 0 | **MUITO ALTA** | Quebrar em três mini-conclusões (uma por PARTE) com 1 figura-síntese central; ou aceitar 487 palavras mas inserir uma figura de "PA completo com label de cada parâmetro biofísico" como cola final visual. |
| Resumindo 1ª coluna (cápsulas 1–4) | 32 | 487 | 0 | **MUITO ALTA** | Aceitar — é Resumindo de 2 páginas (canônico 2026-05-20 pós-#27). Densidade alta aqui é função do formato. |
| Etapa 2 Q08 → Q12 (cinco questões objetivas seguidas, sem figura) | 37–39 | ~390/pág | 0 | **ALTA** | Etapa 2 é prosa pura por padrão — densidade aceita. **Não mexer.** |

**Observação:** apenas a Conclusão integradora justifica mitigação ativa. Densidade alta no Resumindo e na E2 é estrutural do formato NEBLI.

---

## 5. T3.4 — Voz fora do padrão (consistência da voz didática)

**Voz dominante:** monitor explicando ao aluno, com "vamos", "imagine", "pensa comigo", "aqui está a sacada". **Mantém a voz do início ao fim — raríssimo escape.**

**Pequenos escapes (citações):**

- p.11: *"Estruturalmente, é uma proteína única que atravessa a membrana com quatro domínios homólogos"* — voz de manual seca. Quebra com a voz coloquial do parágrafo anterior. Resolvido com a reescrita proposta em T3.2 §1.
- p.25: *"O sistema nervoso codifica intensidade em frequência — é um código digital de frequência sobre um substrato analógico de membrana."* — voz fica mais filosófica/ensaística que monitor; o aluno-alvo gosta, mas é o limite. Não muda nada — manter.
- p.31 (Conclusão): *"A grande mensagem para guardar..."* — voz didática consistente. Excelente.

**Veredito:** voz é uma das **mais consistentes** das apostilas históricas. Nada para corrigir aqui.

---

## 6. T3.7 — Carga cognitiva pico (seção-pivô + 3 mitigações)

**Seção-pivô:** §2.3 — "Cinética do PA passo a passo: a coreografia Na/K" (p.16–19).

**Por que é o pico:** o aluno precisa segurar **simultaneamente**: (a) estado dos canais Na (3 estados: F/A/I); (b) estado dos canais K (2 estados, lento); (c) valor instantâneo de Vm; (d) qual corrente está dominando; (e) onde está no gráfico tempo×Vm. Cinco variáveis temporais correlacionadas.

**Mitigações possíveis:**

1. **Manter como está** com os 10 frames numerados. **Justificativa:** o autor já fez o trabalho duro — cada frame tem uma legenda concreta com Vm exato, qual canal está fazendo o quê. É a melhor solução, e funciona.
2. **Adicionar tabela-síntese ao final da §2.3** com 5 colunas (Fase | Vm | Estado Na | Estado K | Corrente dominante) e 7 linhas (Repouso, Limiar, Upstroke, Pico, Downstroke, Undershoot, Repouso final). Custo: 1/3 de página. Ganho: aluno-alvo tem cola visual única para revisar.
3. **Adicionar figura única integrativa** com o gráfico Vm×tempo e, sobreposto em camadas de cor, a fração de canais Na em cada estado e fração de K aberto. Custo: 1 figura adicional. Ganho: gesto visual integrado.

**Qual escolher:** **Mitigação 2** (tabela-síntese). Custo baixo (1/3 de página), reaproveita o conteúdo já escrito, oferece superfície de revisão compacta. Mitigação 3 seria ouro mas exige produzir figura nova.

---

## 7. T3.8 — ANÁLISE VISUAL (do PDF, obrigatória)

**Nota:** análise feita por triangulação JSON + legendas textuais (`pdftoppm` indisponível). Onde houver inferência indireta, está marcado.

### 7.1 — Hierarquia tipográfica

Pela estrutura do .txt: 3 níveis claros — banner "NEBLI · APOSTILA" (cabeçalho), título PARTE (e.g. "PARTE I — Por que o PA existe"), subtítulos numerados (1.1, 1.2). Boxes clínicos têm título próprio em destaque (e.g. "Esclerose múltipla — quando os oligodendrócitos são atacados"). Citações de boxes "limiar não é Vm de equilíbrio" usam título-pergunta. **Hierarquia funcional**: aluno sabe sempre em que nível está. Sem evidência de mistura de níveis.

### 7.2 — Valor pedagógico das figuras

32 imagens em 53 páginas = média 0,6 figura/página. Densidade alta nas PARTES I–III (páginas 4–29), zero nas Etapas 2/3 (páginas 30–53 — só prosa de questões, esperado). Pelo .txt, **legendas são longas e mecanísticas** (e.g. p.11: "Canal de Na voltagem nos estados fechado e aberto. À esquerda, repouso (-70 mV): a comporta de ativação está fechada, o poro impermeável..."). **Figuras não são decorativas — elas carregam informação que o texto referencia explicitamente.** Padrão alto. Único alerta: figura "modelo elétrico básico da membrana" (p.5) com legenda densa precisa do parágrafo do texto pra ser entendida — coupling forte, o que é positivo para o aluno-alvo.

### 7.3 — Densidade visual (respiro × muros)

Distribuição palavras/página:
- Páginas 1–29 (E1): variam 102–500 palavras, **média 248** — respiro adequado, muito pelas 32 figuras.
- Páginas 30–53 (Resumindo + E2 + E3): variam 326–487 palavras, **média 395** — muros de prosa, esperado em questões.

**Sem evidência de mojibake.** Sem evidência de cortes de figura. O equilíbrio palavras × figuras nas páginas 1–29 é **bom para o tema**.

### 7.4 — Uso de cor

Pelo padrão NEBLI histórico e pelo banner "RESUMINDO" mencionado no .txt: **gold no Resumindo, navy nos títulos de PARTE**. Sem evidência textual de uso decorativo de cor. Esperar coerência se renderizado.

### 7.5 — Cortes/overflow

Sem evidência textual de overflow. Página 53 com 80 palavras finais sugere fim limpo (gabarito consolidado terminando sem aperto).

**Veredito visual:** APROVADO com baixa confiança em itens que dependem de render real (cores, espessura, contraste). Estrutura textual sugere apostila visualmente bem-organizada.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F do REDATOR-E1)

### Técnica 1 — Abertura "pergunta-âncora com escala humana"

**Citação (p.3):**
> "Imagine um neurônio sensorial no seu pé... essa informação precisa subir um metro inteiro até chegar ao encéfalo — sem perder amplitude, sem se diluir no caminho. Se o sinal viajasse simplesmente como uma corrente passiva pela membrana, ele não chegaria."

**Nome da técnica:** "Pergunta-âncora com escala humana + antagonista físico nomeado".

**Quando NEBLI deveria usar:** **sempre que o tema for 'por que precisamos de X'**. Abrir com cenário concreto que o aluno consegue visualizar (pé→encéfalo, ou eritrócito→pulmão, ou estômago→duodeno), nomear o antagonista físico (capacitância, gradiente de pH, distância difusional), e só depois introduzir a solução biológica. Gancho concreto para REDATOR-E1: usar essa estrutura na intro-box dos resumos de "Transmissão sináptica", "Filtração glomerular", "Hemoglobina-O₂", "Ciclo de Krebs como fornecedor de poder redutor".

### Técnica 2 — "Toda fórmula vem com o gesto físico no mesmo parágrafo"

**Citação (p.27):**
> "C = ε₀ · A / d, onde A é a área e d é a distância entre as placas. Quanto maior d, menor C. A mielina faz exatamente isso — afasta as placas, aumentando d e diminuindo Cm."

**Nome da técnica:** "Fórmula + interpretação + aplicação biológica no mesmo parágrafo".

**Quando NEBLI deveria usar:** **em toda fórmula da apostila**. Atualmente o REDATOR-E1 às vezes apresenta fórmula com derivação separada — o italiano mostra que a sequência ótima é (1) fórmula, (2) "quanto maior X, menor Y" em 1 frase, (3) "biologicamente, isso significa que..." em 1 frase. Gancho concreto: aplicar em Henderson-Hasselbalch (pH/tampões), Michaelis-Menten (enzimas), Nernst (eletrofisiologia), van der Waals (proteínas).

### Técnica 3 — "Box-desfaz-confusão com título-pergunta"

**Citação (p.10):**
> "**Limiar não é Vm de equilíbrio** — É comum confundir e achar que limiar é o ponto onde 'alguma coisa nova acontece' — como se fosse um valor mágico de voltagem. Não é. O limiar é o ponto onde a corrente de Na entrando supera a corrente de K saindo."

**Nome da técnica:** "Box anti-confusão com título-negação".

**Quando NEBLI deveria usar:** **sempre que houver erro conceitual recorrente sobre o tema**. A apostila tem 5 boxes desse tipo (limiar, Inativado≠Fechado, Na/K-ATPase não faz PA, Refratário não vem de ATP, Saltatória não significa pular nodos, Intensidade não altera amplitude). **Cada box ataca um erro nominalmente identificado.** Gancho concreto para REDATOR-E1: ao redigir, listar 3–5 confusões clássicas do tema (do Mapa de Confusões) e transformar cada uma num box com título-negação. O título-pergunta/negação cria *atenção dirigida* — aluno sabe imediatamente "ah, eu pensava errado isso, vou ler com cuidado".

---

## 9. T3.10 — 7 erros NEBLI (calibração no PDF do italiano)

| # | Erro NEBLI | Status no PDF | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação (correta ≤ 1,25× maior distratora) | **A CONFIRMAR** | Não consegui ler integralmente as Q26–Q30 no .txt amostrado. Q01–Q20 (Consolidação + Integração) mostram paridade boa — distratoras com 25–35 palavras de mecanismo plausível-mas-errado. Suspeita histórica do italiano em Aplicação permanece. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **AUSENTE** | Apostila histórica italiano usa footnotes numéricas, não helper `#sigla()`. PA, Cm, Rm, λ, τ, Vm, mV, ATP, Na⁺, K⁺, ENa, EK, AIS, PEPS, PIPS, TTX, EM, GBS, RM, SNC, SNP, nodos de Ranvier — **todos** com footnote de definição na 1ª aparição. ~22 termos com nota. Padrão alto. |
| 3 | Subagentes Opus contaminados / paralisia | **N/A** | Apostila histórica, não gerada via pipeline atual. |
| 4 | Heredoc atômico ENAMETOOLONG no Windows | **N/A** | Idem. |
| 5 | `questao-ce` exige tupla `("I", [conteúdo])` | **N/A** | Idem (pipeline). Q05, Q07, Q11, Q14, Q16 são CE no formato esperado pelo italiano. |
| 6 | Termo-notas abaixo do alvo (6–8/resumo) | **AUSENTE** | ~22 termos com footnote — **muito acima do alvo NEBLI**. Eventualmente excessivo para o tipo (em alguns casos um glossário inline seria mais limpo), mas erro é o oposto: italiano sobre-anota, NEBLI sub-anota. |
| 7 | Teto E1 22 páginas | **PRESENTE com folga** | E1 ocupa páginas 3–31 = **29 páginas**. Acima do teto de 22. Mas o tema (PA completo + biofísica + 3 síndromes) justifica? Argumento sim: PARTE I (3 sub-tópicos) + PARTE II (3 sub-tópicos com coreografia frame-a-frame) + PARTE III (3 sub-tópicos + 3 boxes clínicos) é volume grande. Apostila histórica do italiano sempre ocupou mais — não é defeito, é norma diferente. **Para o NEBLI atual:** se for replicar esse tema, o teto de 22 página força corte. Onde cortaria? Provavelmente: comprimir os 10 frames da §2.3 em 5–6 frames + tabela-síntese (mitigação 2 do T3.7). |

**Status agregado:** 1 erro NEBLI a confirmar (paridade Aplicação), 3 ausentes (boas notícias para calibração), 3 N/A, 1 presente justificável (teto de páginas — italiano excede mas com motivo).

---

## 10. Recomendações por hierarquia de impacto

### ESTRUTURAL (max 3)

1. **Inserir tabela-síntese ao final da §2.3** (Fase | Vm | Estado Na | Estado K | Corrente dominante; 7 linhas). Custo baixo, ganho grande — colapsa 4 páginas de coreografia em 1/3 de página de revisão.
2. **Quebrar §3.3 entre "biofísica da mielina" e "3 síndromes"** em duas subseções (3.3 biofísica, 3.4 síndromes). Atualmente os 3 boxes clínicos vêm coladinhos no fim da §3.3 — leitor com fadiga já chegou cansado. Subseção própria devolve a atenção.
3. **Considerar comprimir os 10 frames da §2.3 para 6 frames principais + 4 mini-frames marginais.** Reduz pressão de páginas (29→~23). Só fazer se o teto de 22 páginas for inegociável; se não, manter os 10 — é dos pontos altos da apostila.

### MECANÍSTICO (max 3)

1. **Acrescentar analogia mecânica em §1.2** (capacitor enchendo vs. piscina com fundo poroso) para resolver o STOP de p.5. Ver T3.2 §2 — reescrita pronta.
2. **Acrescentar metáfora estrutural em §2.1** ("quatro mãos com seis dedos") antes da nomenclatura I/II/III/IV + S1–S6. Ver T3.2 §1 — reescrita pronta.
3. **Expandir o mecanismo do screening eletrostático no box hipocalcemia** — atualmente está em footnote tardia. Mover 1–2 frases para o corpo do box. Ver T3.2 §3.

### DIDÁTICO (max 3)

1. **Confirmar paridade nas Q26–Q30 (Aplicação)** — se estiver desigual (correta 30+ palavras, distratoras 10–12), reescrever as 5 com mecanismo plausível-mas-errado em 25–35 palavras cada.
2. **Acrescentar 1 frase-paraquedas no início da §2.1** anunciando que o aluno vai cair em nomenclatura intensa por 1 parágrafo, depois recupera. Algo como: *"Agora vai vir uma carga de nomenclatura — não tenta decorar, só absorva a ideia de que existem 4 partes idênticas + 6 segmentos cada + 1 segmento especial. Volto pra explicar funcionalmente no próximo parágrafo."*
3. **Compactar footnotes redundantes** — ATP/Vm/mV aparecem em footnote tanto na 1ª aparição quanto reapareceriam se o resumo seguisse a regra NEBLI. Italiano sobre-anota; NEBLI define alvo de 6–8 termos densos. Em 22 termos, ~half podem migrar para footnote simples sem #termo-nota, ou serem aglutinados.

### ESTÉTICO (max 3)

1. **Validar cores das categorias** nas E2 (Consolidação / Integração / Aplicação) — pelo .txt não dá pra confirmar, mas o padrão NEBLI exige diferenciação visível. Render real necessário.
2. **Garantir respiro entre os 3 boxes clínicos finais** — EM, Guillain e Hipocalcemia em sequência (p.29–30) podem virar muro visual se as 3 caixas estiverem grudadas. Inserir 1–2 linhas de espaço entre cada.
3. **Banner "RESUMINDO" no padrão gold** — confirmar render. Estrutura textual sugere 2 páginas a duas colunas — formato canônico pós-2026-05-20.

---

## 11. Veredito acionável

1. **Aprovar como referência positiva?** **SIM, com folga.** Está entre as 3 melhores apostilas históricas do italiano vistas até agora (junto com FMEMB-02 e BIOQ-18). Voz consistente, mecanismo amarrado em camadas, clínica caindo do mecanismo, 5 boxes anti-confusão executados com técnica.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM, 3 + 3.** Lista acima.
3. **Seção para refazer?** **Nenhuma seção inteira.** §2.1 abertura precisa de reescrita de 1 parágrafo (metáfora estrutural), §1.2 precisa de 1 analogia mecânica, §3.3 hipocalcemia precisa de 2 frases extras.
4. **Parágrafos para reescrever?** **3** — todos com reescrita pronta em T3.2:
   - §1.2 p.5 — t=τ com analogia da piscina.
   - §2.1 p.11 — abertura com "quatro mãos".
   - §3.3 p.30 — screening eletrostático no corpo do box.

---

[APROVAR COM RESERVAS]
