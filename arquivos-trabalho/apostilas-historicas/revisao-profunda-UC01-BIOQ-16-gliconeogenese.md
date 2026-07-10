# Revisão profunda Tier 3 — UC01-BIOQ-16-gliconeogenese

**Tema (ancoragem):** Gliconeogênese
**Autor:** Marisa Helena (declarado)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real, ensino médio + meses
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25
**Flag:** "resumo ruim"

## ANCORAGEM DE TEMA

- **Tema canônico:** Gliconeogênese — síntese hepática (e renal em jejum) de glicose a partir de lactato, glicerol e aminoácidos glicogênicos; três (quatro, com G6Pase) bypasses das reações irreversíveis da glicólise; regulação recíproca via F2,6BP; falência em Von Gierke e hipoglicemia alcoólica.
- **3 conceitos centrais que eu-aluno quero aprender:** (a) por que existem bypasses em vez de inverter a glicólise; (b) a manobra OAA→malato→OAA e o porquê dela ser "duas coisas em uma" (transporte + NADH citosólico); (c) por que o etanol em jejum faz hipoglicemia mecanisticamente.
- **2 temas vizinhos que NÃO são esse:** glicólise propriamente dita (só serve como contraste); glicogenólise/síntese de glicogênio (Von Gierke encosta mas o eixo é diferente).

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão (mecanística) |
|---|---|---|---|
| Capa + meta | OK | 1 | nenhum problema, hierarquia clara |
| Sumário | OK | 2 | promete bem o conteúdo |
| Intro (Etapa 1 abertura) | OK | 3 | abre direto na confusão certa ("glicólise de volta") — engaja |
| 1.1 termodinâmica | [STOP leve] | 3–4 | "ΔG por volta de -15 a -25 kJ/mol" aparece sem ter explicado o que ΔG significa concretamente para o aluno. Aluno em dificuldade lê "-25 kJ/mol" como número decorativo. |
| 1.1 figura "Vista geral da via" | [STOP forte] | 4 | A figura é descrita com 5 linhas de legenda densa MAS no PDF renderizado ela aparece minúscula, ocupando ~⅓ da página enquanto a legenda toma o resto. Aluno não consegue ler enzimas no diagrama. |
| 1.2 6 passos compartilhados | [STOP] | 5 | "DHAP NADH NAD" aparecem soltos no início do parágrafo sem conexão sintática — parecem rótulos de figura que vazaram para o corpo. |
| 1.3 compartimentos | [STOP forte] | 6 | **Pico de carga.** 504 palavras numa única página, ZERO figura, jargão denso (PC mitocondrial, PEPCK 50/50, FBPase-1 citosólica, G6Pase no lúmen do RE, G6PT/SLC37A4) num único respiro. Aluno fecha o PDF aqui. |
| 2.1 lactato e Cori | OK | 7–8 | retoma respiração, figura presente |
| 2.3 lançadeira malato | [STOP] | 10–11 | metáfora "dois pássaros uma pedrada" salva, mas o box "Lactato dispensa lançadeira; piruvato não" tem 6 linhas de qualificação técnica em parênteses ("a PEPCK pode ser parcialmente citosólica…") que confundem mais que esclarecem. |
| 3.1 F2,6BP | OK | 14–15 | das melhores seções do resumo — vide T3.9 |
| 3.3 Von Gierke + álcool | OK | 18–21 | box clínico bem feito; tabela de manifestações respira |
| Resumindo | OK | 23 | 9 seções, 2 colunas, ler-rápido |
| E2 Q26–Q30 (Aplicação) | [STOP analítico] | 35–38 | paridade quebrada (vide T3.10 #1) |
| Gabarito | BUG | 47 | header diz "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" mas é gabarito da Etapa 2; legacy do template antigo |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria de referência:** CATEGORIA 3 (Abertura por desfazer confusão comum) + CATEGORIA 1 (mecanística parágrafo-por-parágrafo).

**Parágrafo NEBLI (intro Etapa 1, pág 3):**
> "Gliconeogênese é a via que fabrica glicose nova a partir de moléculas que não são açúcar — lactato, glicerol, alguns aminoácidos. Ela é a contrapartida da glicólise, mas não é a mesma estrada andada para trás. Esse é o erro mais comum do aluno do primeiro ano: imaginar que basta rodar as dez reações da glicólise no sentido inverso."

**Exemplar 3.1 (Enzimas I — Marisa Helena):**
> "Antes de qualquer coisa, precisamos desfazer uma confusão comum. Muitas pessoas pensam que «enzima faz reação acontecer». **Isso está errado.** Uma enzima não transforma uma reação impossível em possível — ela só torna uma reação que já é termodinamicamente favorável muito mais rápida."

**Comparação:** o NEBLI replicou bem o movimento "desfazer confusão na abertura" — o gesto está lá ("não é a mesma estrada andada para trás"). O que o exemplar faz melhor é o **grifo terminante** ("Isso está errado.") + a **separação visual em parágrafo curto** antes de explicar o que é certo. No NEBLI, a correção vem na mesma frase corrida ("mas não é a mesma estrada…"). Aluno em dificuldade tende a passar batido.

**Reescrita inspirada no exemplar:**
> "Antes de qualquer coisa, vamos desfazer uma confusão muito comum. Quem terminou de estudar glicólise pensa: 'ok, a gliconeogênese é a glicólise andando ao contrário, certo?'. **Errado.** Três das dez reações da glicólise são termodinamicamente irreversíveis — não dá para simplesmente girar a chave. A gliconeogênese não é a glicólise de volta. É uma estrada paralela que usa as mesmas pistas onde dá (sete passos reversíveis) e constrói desvios próprios onde não dá (quatro enzimas exclusivas)."

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo A — pág 4, descrição da Vista Geral

**Citação literal:**
> "Vista geral da via. As setas azuis verticais (duplas) representam reações reversíveis — compartilhadas com a glicólise. As setas vermelhas indicam os passos irreversíveis — onde a gliconeogênese precisa de enzimas próprias. Os três desvios irreversíveis aparecem com enzimas exclusivas — PC + PEPCK (substituindo PK), FBPase-1 (substituindo PFK-1) e G6Pase (substituindo HK/GK). Para fazer uma glicose, a via consome 4 ATP + 2 GTP + 2 NADH — caro, mas necessário quando a glicemia depende disso."

**Diagnóstico mecanístico:** legenda de figura sendo usada como mini-aula. Densidade ~70 palavras descrevendo iconografia + saldo energético no mesmo bloco. No render, a figura abaixo é pequena (vide p4 visual) — aluno tenta correlacionar setas e cores na figura minúscula e desiste. A informação do "saldo 4 ATP + 2 GTP + 2 NADH" merece linha própria, não rodapé de legenda.

**Reescrita pronta:**
> "Vista geral da via (figura 1). As setas azuis duplas são as reações reversíveis — sete passos que a gliconeogênese reaproveita da glicólise. As setas vermelhas são os passos irreversíveis — onde a via constrói desvios próprios. Repare nos quatro nomes em destaque (PC, PEPCK, FBPase-1, G6Pase): são as quatro enzimas exclusivas da gliconeogênese.
>
> O saldo energético merece atenção própria: **4 ATP + 2 GTP + 2 NADH por glicose**. Lembre que a glicólise rendia 2 ATP + 2 NADH. A diferença líquida (~6 fosfatos de alta energia) é o preço da glicemia em jejum."

### Parágrafo B — pág 5, "DHAP NADH NAD" solto

**Citação literal:**
> "Há uma consequência sutil mas importante na GAPDH reversa. Na glicólise, a GAPDH oxida o G3P e produz NADH no citosol. Na gliconeogênese, a GAPDH faz o oposto — reduz o 1,3-BPG de volta a G3P, consumindo NADH citosólico. Esse detalhe parece técnico mas vai mandar na PARTE II..."
>
> [Antes desse parágrafo, no PDF, aparecem solitárias: "DHAP15 NADH16 NAD17"]

**Diagnóstico mecanístico:** três rótulos de figura ou âncoras de footnote vazaram para o corpo do texto como linha solta, sem função sintática. Aluno em dificuldade interpreta como erro de geração ou — pior — pensa que está faltando entender alguma sequência rotulada. Quebra a confiança no PDF. O parágrafo em si está bom (faz a ligação certa para 2.3), mas o lixo visual mata a leitura.

**Reescrita pronta:** remover a linha solta "DHAP NADH NAD"; mover as definições para footnotes próprias na 1ª aparição contextual. O parágrafo deve abrir direto: "Há uma consequência sutil mas importante na GAPDH reversa…".

### Parágrafo C — pág 6, parede de jargão sobre compartimentos

**Citação literal (trecho de 504 palavras numa página sem figura):**
> "Dentro do hepatócito, a via não está toda no mesmo compartimento — e isso já antecipa um problema clínico importante. A piruvato carboxilase é mitocondrial. Significa que o piruvato precisa entrar na mitocôndria para ser convertido em oxaloacetato. A PEPCK humana é cerca de metade mitocondrial e metade citosólica (depende do isoforma — em ratos a PEPCK é quase 100% citosólica; em humanos, é mais ou menos meio a meio). A FBPase-1 e a aldolase são citosólicas. E a G6Pase está no lúmen do RE — retículo endoplasmático — a glicose-6-fosfato precisa de um transportador — o G6PT — para entrar no RE, sofrer hidrólise, e a glicose livre sai por outro transportador."

**Diagnóstico mecanístico:** sete localizações subcelulares distintas (PC mit, PEPCK 50/50, FBPase-1 cito, aldolase cito, G6Pase no lúmen do RE, G6PT, transportador de glicose) num único parágrafo, sem figura de apoio, sem mini-resumo, sem aterragem. Trivia inter-espécies (rato vs humano) é ruído num resumo introdutório de gliconeogênese — aluno do 1º ano não precisa disso para entender Von Gierke depois. Pico de carga cognitiva absoluto do PDF.

**Reescrita pronta (duas frações + figura prometida):**
> "Dentro do hepatócito, a gliconeogênese não cabe num único compartimento. Vamos seguir o caminho do piruvato passo a passo (figura ao lado):
>
> 1. **Mitocôndria** — piruvato entra aqui para encontrar a piruvato carboxilase (PC). Vira oxaloacetato.
> 2. **Citosol** — o oxaloacetato (disfarçado de malato, item 2.3) é convertido em PEP pela PEPCK e segue para FBPase-1 e aldolase, todas citosólicas.
> 3. **Lúmen do retículo endoplasmático (RE)** — a glicose-6-fosfato precisa entrar no RE pelo transportador G6PT para encontrar a G6Pase, que está ancorada na face luminal. Só depois sai como glicose livre.
>
> Essa anatomia subcelular não é detalhe técnico: é o que vai explicar Von Gierke no item 3.3. Defeito em qualquer peça do sistema do RE (G6Pase ou G6PT) trava a saída da glicose para o sangue."

(Detalhe humano vs rato da PEPCK: fora. Se importar mesmo, vira footnote.)

---

## 4. T3.3 — 3 seções mais densas

| # | Seção | Pág | Sintoma | Mitigação concreta |
|---|---|---|---|---|
| 1 | 1.3 Compartimentos | 6 | 504 palavras zero figura; 7 localizações subcelulares enfileiradas | Adicionar figura esquemática de hepatócito (mit + cito + RE com setas); quebrar em lista mecanística como na reescrita acima. |
| 2 | 2.3 Lançadeira malato | 10–12 | conceito difícil + box "Lactato dispensa lançadeira" com qualificações em parêntese aninhadas | Cortar o parêntese sobre PEPCK humana parcialmente citosólica do box — vira footnote. Box deve dizer só: "lactato já trouxe NADH no citosol; piruvato puro precisa importar pela lançadeira." |
| 3 | E2 Q05/Q09/Q16/Q22 (CE julgados independentes) | 25–33 | itens densos com 25–40 palavras cada, 4 por questão = 100–160 palavras por item, tudo sem figura | Encurtar itens para 15–25 palavras com mecanismo enxuto; a paridade entre itens é OK aqui, o que pesa é o volume agregado. |

---

## 5. T3.4 — Voz fora do padrão

Citações onde a voz didática-conversacional do NEBLI quebra:

- **Pág 4:** "Mais detalhe vem em 2.3." — too telegráfico. Aluno em dificuldade quer saber se precisa segurar essa dúvida ou esquecer; reescrever: "Vamos voltar a isso com calma no item 2.3 — por enquanto, fica o gancho."
- **Pág 11:** "Dois pássaros, uma pedrada." — funciona, mas seguida de explicação técnica sem respiro; voz cai do informal para o formal sem transição.
- **Pág 13:** "É caro — mas é o custo de manter a glicemia em jejum." — frase de fechamento boa, mas a equação acima ("2 piruvato + 4 ATP + 2 GTP + 2 NADH + 6 H₂O → 1 glicose…") aparece sem qualquer onboarding: "olha essa equação? cada termo conta. Vamos somar:..." é o que faltou.
- **Pág 20 (visual):** o box "Glicólise e Gliconeogênese são processos espontâneos…" tem voz de tópico-de-prova solto, parece colado de outro documento. Frase isolada "O controle inclui regulação alostérica recíproca por nucleotídeos de adenina." sem antecedente claro do que "O controle" se refere.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** §1.3 (Compartimentos celulares), pág 6 — 504 palavras, zero figura, 7 localizações subcelulares, jargão denso (G6PT/SLC37A4 cravado no meio sem mecânica). É o ponto de não-retorno do aluno.

**3 mitigações candidatas:**

1. **Quebrar em duas páginas com figura intermediária** (esquema do hepatócito com mit + cito + RE).
2. **Adiar o detalhe da PEPCK humana 50/50** para o item 2.3 (onde a lançadeira do malato torna esse detalhe relevante).
3. **Inserir mini-resumo no meio da seção** (não só no fim) — frase-âncora curta após cada localização ("guardar: PC mora na mitocôndria; tudo mais é citosol; G6Pase é o portão de saída no RE").

**Qual escolher:** **#1 + #2 combinadas.** A figura é o item de maior alavancagem (mitiga o muro de texto E desambigua os 7 lugares); cortar o trecho rato/humano da PEPCK libera ~30 palavras para a figura sem estourar o page-budget. #3 sozinha não resolve porque o pico é visual, não conceitual.

---

## 7. T3.8 — ANÁLISE VISUAL (do PDF)

| Critério | Avaliação | Evidência |
|---|---|---|
| **Hierarquia tipográfica** | OK | Capa navy com título Merriweather grande funciona. Sumário (p2) com PARTE I/II/III em teal e itens 1.1, 1.2 em peso menor — boa hierarquia. |
| **Valor pedagógico das figuras** | MÉDIO-RUIM | Figura da pág 4 (Vista geral) **renderizou pequena** ocupando ~⅓ da página enquanto a legenda + texto comem o resto. Aluno não consegue ler enzimas no diagrama. Figura da pág 20 (ciclo de Krebs sobreposta com NADH/CO₂) é decorativa — quase nenhum aluno vai entender o que ela quer dizer ali na seção sobre etanol. |
| **Densidade visual** | RUIM em pontos | Pág 6 é muro de texto absoluto. Pág 22 (conclusão integradora) está OK porque tem respiro de parágrafo, mas a maioria das páginas 14–19 é texto corrido sem alívio gráfico. |
| **Uso de cor** | OK / propositada | Teal nos subtítulos da Etapa 1, navy nas faixas, gold no banner do Resumindo — coerente. Boxes de Von Gierke e hipoglicemia alcoólica (pág 19–21) bem destacados. |
| **Cortes / overflow** | 1 bug confirmado | Página 47 do gabarito mostra header **"ETAPA 4 — QUESTÕES DE FUNDAMENTOS"** — Etapa 4 foi removida do pipeline canônico em 2026-05-22, o header é legacy do template antigo. Bug do COMPILADOR/template, não do REDATOR. |

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### Técnica 1 — **"Mesma molécula, dois efeitos opostos coordenados"** (regulação por F2,6BP, §3.1)

**Citação literal (pág 14):**
> "E o efeito da F2,6BP nas enzimas-válvula é recíproco:
> -- Ativa a PFK-1 — ativador alostérico mais potente da glicólise. F2,6BP alta → glicólise acelera.
> -- Inibe a FBPase-1 — F2,6BP alta → gliconeogênese freia.
> [...] Uma única molécula coordena as duas vias em direções opostas — engenhoso demais para passar despercebido."

**Por que funciona:** o autor não só descreve o mecanismo regulatório; ele **enquadra a elegância**. "Uma única molécula → dois efeitos opostos coordenados" é o tipo de framing que cola na memória do aluno. A frase "engenhoso demais para passar despercebido" sinaliza ao leitor "isto é o ponto da seção".

**Quando NEBLI deveria usar (gancho para REDATOR-E1):** sempre que houver **regulação recíproca** de duas vias opostas por um único mediador, **abrir a seção dizendo o ângulo "uma molécula, dois efeitos coordenados"** antes de descrever o mecanismo. Aplicável em: glicogênio síntese/degradação (G6P / glicogênio fosforilase/sintase), lipólise/lipogênese (malonil-CoA), ciclo de Krebs vs gliconeogênese (acetil-CoA). É um padrão de abertura de seção que vale codificar.

### Técnica 2 — **Mini-resumos itálicos in-line a cada subtópico**

**Citação literal (pág 5):**
> "*Resumindo até aqui: Sete reações da glicólise são reversíveis — operam perto do equilíbrio com a mesma enzima nos dois sentidos. A gliconeogênese reaproveita essas enzimas no sentido contrário. O que determina o sentido é a concentração de substrato/produto, não a enzima. Só as quatro reações irreversíveis exigem enzimas próprias da gliconeogênese.*"

**Por que funciona:** o aluno em dificuldade, que está com cabeça pesada, **ancora a cada 600–800 palavras** sem precisar voltar e reler. O mini-resumo é a frase que ele copia no resumo dele. Visualmente destacado em itálico + recuo, é uma respiração gráfica.

**Quando NEBLI deveria usar:** isto **já está parcialmente codificado no REDATOR-E1**, mas a tipografia precisa garantir que esses mini-resumos apareçam graficamente destacados — itálico sem indentação não basta. Sugerir helper `#mini-resumo[...]` com fundo cinza-claro 5% + recuo de 1em, aplicado consistentemente. **Hoje** o resumo de gliconeogênese tem ~8 mini-resumos, todos itálicos planos — sob render eles quase desaparecem.

### Técnica 3 — **Box clínico com 4 manifestações + mecanismo de cada uma**

**Citação literal (pág 19, box Von Gierke):**
> "O paciente é geralmente uma criança com:
> • Hipoglicemia grave em jejum (fígado não exporta glicose, glicemia despenca em 3–4h sem refeição).
> • Hepatomegalia volumosa (G6P acumula no hepatócito, vira glicogênio, fígado incha).
> • Acidose lática (G6P acumulado é desviado pela glicólise → produz piruvato → LDH → lactato em excesso → cai no sangue).
> • Hipertrigliceridemia e hiperuricemia (G6P sobrando vai para via das pentoses-fosfato e biossíntese de lipídios; AMP acumula e vira ácido úrico)."

**Por que funciona:** cada manifestação clínica vem com o **mecanismo bioquímico em parênteses** logo ao lado, na mesma linha. O aluno não precisa fazer mapping mental entre "sintoma X" e "porque Y" — está na cara. É a versão mais barata e legível da regra do NEBLI "diagnóstico + mecanismo na mesma frase".

**Quando NEBLI deveria usar:** **toda vez que um box clínico listar ≥3 manifestações**, exigir que cada bullet tenha o mecanismo entre parênteses na mesma linha. Codificar isto no REDATOR-E1 como regra explícita: "box clínico = sintoma + mecanismo curto entre parêntese, nunca sintoma sozinho". Aplicável a: anemia falciforme (item 4 manifestações), MG/JNM, paciente diabético em cetoacidose, beribéri, etc.

---

## 9. T3.10 — 7 erros NEBLI (tabela de calibração)

| # | Erro | Status | Evidência |
|---|---|---|---|
| 1 | Paridade de distratoras Q26–Q30 | **PRESENTE** | Q26-B (correta) tem ~70 palavras de mecanismo (NADH↑ → piruvato→lactato + OAA→malato + paralisa PC/PEPCK + jejum sem glicogênio). Q26-A (cetoacidose alcoólica) tem ~55 palavras decentes, mas Q26-C tem ~30 palavras genéricas, Q26-D ~25 palavras claramente errada ("inibição covalente"), Q26-E ~25 palavras (hiperinsulinemia reativa). Ratio correta/menor-distratora ≈ 2.8. Falha. Mesmo padrão em Q28 (correta longa mecanística vs distratoras curtas). |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PARCIAL** | Footnotes presentes para HK, PFK-1, PK, PEP, OAA, GTP, MDH, LDH, RE, G6PT, F2,6BP, PKA, PFK-2, FBPase-2, CoA, PDH, PK-L. **Faltam ou aparecem tarde:** AMP, ADP, Pi, NADP, FAD (acidente do tema), GLUT-2 (aparece em E2 sem definição), G3P, 1,3-BPG, DHAP (aparece em rótulo solto na pág 5 antes da footnote de fato). |
| 3 | Subagentes Opus contaminados | N/A | Este PDF foi gerado antes do fix; possível artefato visível é o header "Etapa 4 — Questões de Fundamentos" no gabarito (pág 47), que é template antigo e não problema de subagente. |
| 4 | Heredoc ENAMETOOLONG | N/A | Não verificável no PDF. |
| 5 | `questao-ce` tupla | N/A | Questões CE renderizaram corretamente (Q05, Q09, Q16, Q22) — tuplas foram usadas. |
| 6 | Termo-notas abaixo do alvo | **AUSENTE** (positivo) | Termos densos com `#termo-nota` (inferido por estilo): biotina, ciclo de Cori, ciclo glicose-alanina, von Gierke, ácido graxo de cadeia par, lançadeira do malato, glicogenose, F2,6BP. ≥6, dentro do alvo. |
| 7 | Tema-card com teto E1 errado | N/A | A E1 saiu com ~21 páginas (pág 3 a 22) — dentro do teto canônico ATUAL de 22. OK. |

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)

1. **Quebrar §1.3 em duas páginas e inserir figura esquemática do hepatócito** (mit/cito/RE). Pico de carga cognitiva atual é insustentável; aluno em dificuldade abandona aqui. Maior alavancagem de qualquer mudança no resumo.
2. **Engordar distratoras Q26–Q30 para 25–35 palavras cada com mecanismo plausível-mas-errado** (regra canônica errosComuns #1). Aluno acerta Q26 hoje por exclusão visual, não por entender.
3. **Limpar o lixo do gabarito (header "Etapa 4")** — bug de template legacy. Sem isso o PDF parece inacabado.

### MECANÍSTICO (max 3)

1. **Reescrever a abertura de 2.3 com "duas funções em uma" como tese, antes da mecânica.** Hoje a tese "manobra do malato faz dois serviços simultâneos" vem no meio do parágrafo; deveria abrir a seção.
2. **Cortar o detalhe inter-espécies da PEPCK humana 50/50 da §1.3.** Não acrescenta nada à compreensão de Von Gierke nem do bypass; vira ruído. Se importar mesmo, vai para footnote do item 2.3.
3. **Adicionar mecanismo concreto à equação global (pág 13).** Hoje a equação aparece "fria"; precisa de uma frase orientando o leitor a interpretá-la termo a termo.

### DIDÁTICO (max 3)

1. **Mini-resumos in-line precisam de tipografia distinta** (fundo cinza 5% + recuo + label "Resumindo até aqui"). Hoje são itálico simples e se misturam ao corpo.
2. **Box "Lactato dispensa lançadeira" (pág 11) deve perder a parêntese técnica sobre PEPCK humana.** A mensagem do box é "lactato é mais econômico"; a qualificação técnica é footnote.
3. **Frase-âncora curta após cada nova localização subcelular na §1.3** — pelo menos enquanto a figura não chega.

### ESTÉTICO (max 3)

1. **Figura da Vista Geral (pág 4) precisa ser ampliada** para no mínimo 75% da largura útil (hoje renderiza minúscula). Aluno tem que ler nomes de enzimas no diagrama.
2. **Remover linhas órfãs "DHAP NADH NAD" da pág 5.** Lixo visual que parece bug de geração.
3. **Box da pág 20** (Glicólise/Gliconeogênese são processos espontâneos…) tem voz fora do padrão e referente ambíguo ("O controle..."). Reescrever ou remover.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **NÃO.** Ele tem técnicas excelentes isoladas (regulação recíproca como tese, mini-resumos, box clínico mecanístico) — mas a pág 6 e a paridade de Aplicação são quebras estruturais que não permitem usar este PDF como exemplar.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM.** Três estruturais + três mecanísticos identificados acima.
3. **Seção para refazer:** **§1.3 — Compartimentos celulares** (refazer com figura + quebra em duas páginas + cortar inter-espécies); secundariamente **Q26–Q30 (Aplicação E2)** com engorda de distratoras.
4. **Parágrafos para reescrever:** **3** — (a) descrição da Vista Geral pág 4, (b) parágrafo da pág 5 com "DHAP NADH NAD" + GAPDH reversa, (c) parede da pág 6 sobre compartimentos.

---

**[APROVAR COM RESERVAS]** — manter no acervo NEBLI para mineração de técnicas positivas (T3.9), MAS marcar §1.3 e Q26–Q30 como exemplos negativos de carga/paridade. Não distribuir este PDF como referência sem as três reescritas estruturais acima.

<!-- FIM-DA-REVISAO-PROFUNDA-v1 -->
