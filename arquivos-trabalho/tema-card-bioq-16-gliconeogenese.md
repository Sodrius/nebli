# TEMA CARD — Gliconeogênese

## Seção A — Identificação

- **Tema:** Gliconeogênese (síntese hepática/renal de glicose a partir de precursores não-carboidrato)
- **Slug canônico:** `bioq-16-gliconeogenese` (UC01 — Bioquímica)
- **Disciplina:** Bioquímica — Metabolismo de carboidratos
- **Slide-fonte:** `slides/neoglicogenese_2026 (1).pdf` (51 slides, autoria Profa. Marisa). Extraídos em `figuras/gliconeogenese/`.
- **Onde estudar:** Lehninger 7ª ed. — Cap. 14.4 (Gliconeogênese) + Cap. 15.3 (Regulação por F2,6BP) — pp. 543–578.
- **Recorte slide × tema:** sem corte. Slide cobre toda a via, regulação por F2,6BP, ciclos de Cori e glicose-alanina, etanol e deficiência de G6Pase.
- **Alvo de páginas E1:** piso 9, teto 14. Justificativa: tema com cadeia enzimática longa (≥7 enzimas) + 3 ciclos integradores + 2 integrações clínicas. Não tem como ser curto sem decorar.
- **Pasta de trabalho:** `typst-build/` raiz. Saída final: `resumos-gerados/GLICONEOGENESE.pdf` (sobrescreve versão antiga já movida para backup).

## Seção B — Estrutura da E1

### PARTE I — Por que o corpo precisa fabricar glicose (3 subtópicos)

**1.1 — Quem depende OBRIGATORIAMENTE de glicose**
- Abre com pergunta: "Se você passar 16h sem comer, o que acontece com o cérebro?"
- Cérebro consome ~120 g de glicose/dia (mais da metade do estoque corporal total). Não há plano B nas primeiras 48h — só após semanas o cérebro passa a queimar cetônicos em peso.
- Hemácias só têm glicose porque não têm mitocôndria — fazem glicólise anaeróbica → exportam lactato.
- Distingue cliente obrigatório de "tecido que prefere glicose": coração e músculo PREFEREM AG em jejum; cérebro e hemácia NÃO TÊM ESCOLHA.
- Figuras: `slide-06.png` (cérebro+hemácia), `slide-02.png` (estoques).

**1.2 — Por que o glicogênio sozinho não basta**
- Glicogênio hepático = ~100 g (cerca de 16h de cérebro). Glicogênio muscular = ~400 g, mas **fica preso no músculo** (sem G6Pase).
- Distinção crítica: glicogenólise quebra estoque pré-existente (resposta de 2–16h); gliconeogênese sintetiza glicose nova (predomina após ~16h, contribui antes em fração crescente).
- Conectar com o que o aluno já sabe da aula anterior (glicogenólise): "se a gliconeogênese é tão custosa, por que o corpo gasta 6 ATP/glicose só para alimentar o cérebro? Porque a alternativa é dano neuronal."
- Figura: `slide-04.png` (cinética glicemia em jejum).

**1.3 — Onde acontece e quem são os 3 precursores**
- Fígado (ator principal) → rim (assume em jejum prolongado e acidose) → intestino (mínimo).
- 3 precursores legítimos: **lactato** (Cori, do músculo em esforço), **aminoácidos glicogênicos** (predominante alanina, do músculo em jejum), **glicerol** (da lipólise do tecido adiposo).
- Já anunciar o tabu: **ácido graxo de cadeia par NÃO faz glicose** em mamíferos. Por quê? acetil-CoA entra no Krebs e perde 2 C como CO2 antes de chegar ao OAA. Saldo zero de carbonos.
- `#atencao-box` curto: músculo armazena glicogênio para si — não exporta glicose pro sangue (falta G6Pase).
- Figuras: `slide-07.png` (fígado/rim), `slide-10.png` (definição + 3 precursores).

### PARTE II — As três pontes que driblam a glicólise (4 subtópicos — coração do resumo)

**2.1 — O problema termodinâmico: 3 portas só abrem num sentido**
- Pergunta de abertura: "Se a glicólise quebra glicose em piruvato, por que não rodar a mesma máquina ao contrário?"
- Dos 10 passos da glicólise, 7 estão perto do equilíbrio (rodam nos 2 sentidos). 3 têm ΔG muito negativo (hexoquinase, PFK-1, piruvato-quinase) → barreiras intransponíveis na célula real.
- ΔG⁰' ≠ ΔG fisiológico — explicar essa distinção em 2 frases, sem fórmula. O que importa é o ΔG nas concentrações da célula viva.
- **Conceito-chave:** "bypass" não é a mesma enzima andando para trás — é enzima DIFERENTE, mecanismo DIFERENTE, regulação DIFERENTE.
- Figuras: `slide-13.png`, `slide-25.png` (mapa dos 3 bloqueios).

**2.2 — Bypass 1: piruvato → fosfoenolpiruvato (2 passos, 2 compartimentos)** — **subtópico mais denso do resumo**
- Pergunta: "Como fazer o piruvato voltar a PEP, se a piruvato-quinase é proibida de inverter?"
- **Passo 1a: Piruvato carboxilase (mitocôndria).** Adiciona um CO2 (do bicarbonato) ao piruvato → oxaloacetato. Gasta 1 ATP. Cofator obrigatório: biotina. Ativador alostérico crítico: acetil-CoA. Interpretar essa ativação: "o corpo só paga 6 ATP para fazer glicose quando há ácido graxo sendo queimado em paralelo — é checagem de combustível disponível."
- **Passo 1b: lançadeira via malato.** OAA não atravessa a membrana mitocondrial. Mitocôndria converte OAA → malato (consome NADH mitocondrial); malato sai pro citosol; citosol converte malato → OAA (regenera NADH citosólico). Lógica dupla: transporte + entrega de poder redutor citosólico (precisaremos dele para a GAPDH reversa lá adiante).
- **Passo 1c: PEPCK (fosfoenolpiruvato carboxiquinase, citosol).** Descarboxila o OAA (libera o CO2 que tinha sido adicionado no passo 1a) e fosforila com GTP → PEP. Custo: 1 GTP.
- **Saldo do bypass 1:** 1 ATP + 1 GTP gastos por molécula de piruvato. Como precisamos de 2 piruvatos por glicose, são 2 ATP + 2 GTP = 4 fosfatos de alta energia só nessa primeira ponte.
- **Atalho do lactato:** quando o precursor é lactato (Cori), a LDH no fígado faz lactato → piruvato + NADH. Isso já entrega o NADH citosólico que a GAPDH reversa vai precisar. Dispensa o ciclo malato — a célula pode usar a PEPCK mitocondrial direto, caminho mais curto. Quando o precursor é alanina (que entra como piruvato puro), volta a precisar do ciclo do malato.
- Figura obrigatória: cadeia multi-passo piruvato → OAA → malato → OAA → PEP com indicação dos compartimentos. Slides: `slide-15.png`, `slide-17.png`, `slide-19.png`, `slide-23.png`.

**2.3 — Bypass 2: frutose-1,6-bisP → frutose-6-P**
- Pergunta: "Por que não rodar a PFK-1 ao contrário?"
- PFK-1 transferiu um fosfato do ATP para a frutose; o sentido inverso teria que sintetizar ATP a partir do fosfato preso na frutose — energeticamente proibido.
- Solução simples e barata: **frutose-1,6-bifosfatase (FBPase-1)** hidrolisa o fosfato como Pi livre (entra H2O). Não gasta ATP nem GTP — mas TAMBÉM não recupera. O fosfato escapa como inorgânico.
- **Atenção mecanística:** FBPase-1 é enzima DIFERENTE da PFK-1, com sítio catalítico diferente, regulação oposta. Não é "a PFK-1 em sentido contrário."
- Figura: `slide-26.png`, `slide-27.png`.

**2.4 — Bypass 3: glicose-6-P → glicose livre**
- Pergunta: "Já temos G6P; por que isso não basta? Por que precisa virar glicose 'livre'?"
- Glicose fosforilada não atravessa a membrana (a carga do fosfato impede). Hexoquinase fosforilou justamente para reter a glicose dentro da célula. Para EXPORTAR glicose nova ao sangue, é preciso tirar esse fosfato.
- **Glicose-6-fosfatase (G6Pase)** faz a hidrólise — só existe em **fígado, rim e enterócito**. Não está no músculo (por isso músculo nunca exporta glicose pro sangue, mesmo cheio de glicogênio).
- **Detalhe topológico importante:** G6Pase fica no lúmen do retículo endoplasmático, não no citosol. Exige transportadores (G6PT para a G6P entrar; canais para Pi e glicose saírem). Defeito em G6PT = von Gierke tipo Ib.
- Aqui já dá pra fechar a integração clínica: na deficiência de G6Pase (von Gierke), o fígado faz a via toda até G6P mas não consegue exportar — G6P acumula, desvia pra glicólise/lactato, o paciente tem hipoglicemia paradoxal com hepatomegalia e acidose láctica.
- Figura: `slide-29.png`.

**2.5 — Saldo energético consolidado**
- Tabela permitida (caso a — comparativo 3+ dimensões): para cada uma das 4 enzimas únicas da gliconeogênese, mostrar reação, cofator, compartimento, custo. Adicionar linha de saldo total.
- **Custo final por glicose (a partir de 2 piruvatos):** 4 ATP + 2 GTP + 2 NADH = 6 fosfatos de alta energia + 2 NADH.
- Comparação direta com a glicólise (que rende 2 ATP líquidos): a gliconeogênese custa 3x o que a glicólise rendeu. O corpo paga esse preço porque o cérebro não tem escolha.

### PARTE III — Substrato, regulação e clínica (4 subtópicos)

**3.1 — Cada precursor entra num ponto diferente da via**
- **Lactato (ciclo de Cori):** entra como piruvato (LDH). Caminho mais curto, neutro em NADH (a própria LDH entrega o NADH). Conecta com glicólise anaeróbica do músculo em esforço.
- **Aminoácidos glicogênicos:** maioria entra como piruvato ou intermediário do Krebs (α-cetoglutarato, succinil-CoA, fumarato, OAA). Foco em alanina (mais importante numericamente): aminotransferase converte alanina → piruvato no fígado.
- **Ciclo glicose-alanina:** veículo duplo. Músculo em jejum quebra proteína → AA livres → transamina pra alanina (que carrega o nitrogênio com segurança, sem amônia tóxica). Alanina viaja pro fígado, vira piruvato (libera o N pra ureia), piruvato vira glicose, glicose volta pro músculo. Cori transporta carbono; glicose-alanina transporta carbono **+ nitrogênio**.
- **Glicerol (substrato mais barato):** vem da lipólise do TAG no tecido adiposo. Glicerol-quinase (só fígado e rim) gasta 1 ATP → glicerol-3P; glicerol-3P-desidrogenase oxida → DHAP (triose-fosfato glicolítica). 2 glicerois fazem 1 glicose com apenas 2 ATP totais — um TERÇO do custo da via via piruvato.
- Figuras: `slide-24.png` (Cori), `slide-44.png`, `slide-46.png` (alanina).

**3.2 — F2,6BP: o interruptor mestre que muda glicólise por gliconeogênese**
- Pergunta: "Glicólise e gliconeogênese rodam ao mesmo tempo? Isso não seria um curto-circuito gastando ATP à toa?"
- Sim, seria. Esse "ciclo fútil" é evitado por regulação alostérica recíproca, e o **regulador mais potente** é a frutose-2,6-bisfosfato (F2,6BP).
- **Atenção mecanística central:** F1,6BP é INTERMEDIÁRIO da via (o substrato que a FBPase-1 hidrolisa). F2,6BP é **regulador alostérico que NUNCA entra na via**. Nomes parecidíssimos, papéis opostos. É o erro #1 do aluno.
- F2,6BP **ativa** PFK-1 (acelera glicólise) e **inibe** FBPase-1 (freia gliconeogênese).
- Quem controla o nível de F2,6BP? Uma única enzima bifuncional, PFK-2/FBPase-2, com 2 domínios catalíticos em UM polipeptídeo. Quando desfosforilada (estado alimentado, insulina), age como cinase → produz F2,6BP → glicólise ON. Quando fosforilada (jejum, glucagon → cAMP → PKA), age como fosfatase → destrói F2,6BP → gliconeogênese ON.
- Resumo do switch hormonal: insulina = alimentado = F2,6BP alto = glicólise. Glucagon = jejum = F2,6BP baixo = gliconeogênese.
- AMP entra como sinal de pobreza energética independente: ativa PFK-1, inibe FBPase-1 → reforça glicólise.
- Figuras: `slide-37.png`, `slide-38.png`, `slide-42.png`.

**3.3 — Etanol em jejum: a armadilha clínica do NADH**
- Pergunta: "Por que beber álcool em jejum derruba a glicemia e pode matar?"
- O etanol não inibe nenhuma enzima da gliconeogênese diretamente. O mecanismo é todo via NADH.
- Cada molécula de etanol oxidada (álcool desidrogenase → acetaldeído → acetato) consome 2 NAD+ e gera 2 NADH. Em ingestão moderada, isso despeja muito NADH no citosol.
- O NADH alto **desloca o equilíbrio** de duas reações reversíveis essenciais à gliconeogênese:
  - Piruvato + NADH → lactato (LDH). Sequestra o piruvato.
  - OAA + NADH → malato (MDH citosólica). Sequestra o OAA.
- Sem piruvato disponível, a piruvato-carboxilase fica sem substrato. Sem OAA disponível, a PEPCK fica sem substrato. **Inibição indireta por roubo de matéria-prima**.
- Consequências clínicas: **hipoglicemia** (não consegue fabricar glicose nova) + **acidose láctica** (lactato acumulado) + **risco de cetoacidose** (acetil-CoA sobrando da oxidação do etanol vira corpos cetônicos).
- Figuras: `slide-47.png`, `slide-49.png`, `slide-50.png`.

**3.4 — Deficiência de G6Pase (doença de von Gierke) — integração clínica do cronograma**
- Mutação no gene G6PC → enzima G6Pase ausente ou disfuncional no fígado. Tipo Ib = defeito no transportador G6PT.
- Mecanismo: fígado faz toda a gliconeogênese e glicogenólise até G6P, mas não consegue desfosforilar. G6P acumula → desvia para 3 destinos: glicólise local (gera lactato → acidose láctica), via das pentoses (gera ribose), glicogênese (engrossa o estoque já cheio → hepatomegalia).
- Apresentação clínica clássica: lactente com hipoglicemia em jejum curto + abdome distendido (hepatomegalia) + acidose láctica + hiperuricemia (porque a via das pentoses turbinada despeja precursores de ácido úrico).
- O paradoxo que confunde o aluno: o paciente tem glicogênio em excesso E hipoglicemia. Não é falta de estoque — é falta de saída do estoque.
- Figura: `slide-29.png` (referenciada de novo) ou esquema-conceito narrado no texto.

### Mindmap de fechamento (1 página, antes do Resumindo)

- **Mensagem-síntese:** Quando o glicogênio acaba, o fígado vira fábrica de glicose: contorna 3 portas só-de-ida da glicólise gastando 6 ATP, escolhe o substrato pela situação clínica, e atende quem não tem plano B — cérebro e hemácia.
- **3 estações (com setas):**
  1. **Demanda** → cérebro 120 g/dia, hemácia anaeróbica, glicogênio só dura 16h.
  2. **Bypass** → piruvato carboxilase (mit, ATP, biotina) → PEPCK (cit, GTP) → FBPase-1 → G6Pase.
  3. **Substrato pela situação** → lactato (atalho), alanina (jejum + N), glicerol (barato).
- **3 cartões:**
  - **Custo:** 6 ATP equivalentes + 2 NADH por glicose.
  - **Switch:** F2,6BP — insulina ON, glucagon OFF.
  - **Armadilha:** músculo NÃO exporta glicose (sem G6Pase) — quem alimenta o sangue é fígado (+ rim em jejum prolongado).

### Resumindo (1–2 páginas, 8–12 seções, ordem clínica decrescente)

Ordem proposta:
1. Quem depende obrigatoriamente de glicose (cérebro, hemácia).
2. Onde acontece (fígado > rim > intestino).
3. Os 3 bypasses que contornam a glicólise.
4. Custo energético consolidado (6 ATP + 2 NADH/glicose).
5. Lactato e ciclo de Cori (caminho mais curto, neutro em NADH).
6. Alanina e ciclo glicose-alanina (carbono + nitrogênio).
7. Glicerol (substrato mais barato — 2 ATP/glicose).
8. F2,6BP como interruptor mestre (regulador, não intermediário).
9. Insulina vs glucagon na PFK-2/FBPase-2.
10. Etanol em jejum (NADH alto sequestra piruvato e OAA).
11. Von Gierke (G6Pase ausente — hipoglicemia paradoxal com hepatomegalia).
12. Regra fundamental: AG par NÃO vira glicose em mamíferos.

## Seção C — Diretrizes editoriais específicas

### Diretriz dominante (canônico 2026-05-25)

**Baseline baixo + dificuldade real.** Trate o aluno como quem está perdido neste tema. Cada subtópico abre com pergunta ingênua plausível ("se acabou o glicogênio, como o cérebro come?"). Mecanismo ANTES do nome da enzima. Pré-requisitos retomados em 1–2 frases mesmo que pareçam óbvios (jejum, ATP, irreversibilidade da glicólise, NADH como moeda redutora). Aprofundamento em camadas: porquê cru → nuance → exceção → clínica.

### Voz e registros

- Diálogo do início ao fim. Mecanismo > nomenclatura. Variar registro entre subtópicos (≥3 dos 5 canônicos: enquadramento, integração-com-anterior, integração-com-posterior, analogia concreta moderna, ponto de quebra).
- **Subtópico mais denso:** 2.2 (bypass 1). Pode chegar a 500 palavras; cadeia multi-passo enzimática + 2 compartimentos + escolha de substrato. Figura obrigatória. Tabela permitida em 2.5.
- Conclusão integradora obrigatória ao fim da PARTE III, costurando as 3 PARTES em 4–6 frases.

### Jargão controlado — siglas e termos-nota

- **Siglas via `#sigla()` na 1ª aparição:** PEPCK (fosfoenolpiruvato carboxiquinase), F2,6BP (frutose-2,6-bisfosfato), F1,6BP (frutose-1,6-bisfosfato), G6Pase (glicose-6-fosfatase), FBPase-1 (frutose-1,6-bisfosfatase), OAA (oxaloacetato), PEP (fosfoenolpiruvato), G6P (glicose-6-fosfato), F6P (frutose-6-fosfato), DHAP (dihidroxiacetona-fosfato), LDH (lactato desidrogenase), MDH (malato desidrogenase), PFK-1 (fosfofrutoquinase-1), PFK-2 (fosfofrutoquinase-2/bifuncional).
- **Termos-nota via `#termo-nota[][]`:** gliconeogênese, biotina, ciclo de Cori, ciclo glicose-alanina, von Gierke, ácido graxo de cadeia par (regra). Alvo 6–8 — não passar.

### Figuras

- Meta: mínimo 3 figuras por PARTE; PARTE II tem **≥4** (uma por bypass + saldo). Cadeia multi-passo piruvato→PEP é **figura obrigatória** (canônico — ≥5 reações encadeadas).
- Default `#figura-nebli(..., largura: 65%)`; cadeia multi-passo `largura: 85%`; texto curto+figura média `#figura-lateral`.
- Caminhos com prefixo `/` (`/figuras/gliconeogenese/slide-XX.png`). Validar via `MAPA_CONTEUDO.txt` antes de citar.

### Tabelas permitidas

- **2.5 — saldo enzima por enzima** (caso a: comparativo 3+ dimensões): enzima | reação | compartimento | cofator | custo.
- **3.1 — substrato por substrato** (caso a): substrato | entrada na via | passo extra | custo/glicose.
- Header navy, texto branco. Sem bullets soltos no corpo.

### Proibições inegociáveis

- Sem mapa mental SVG (`#mapa-parte` proibido).
- Sem caixa alta para ênfase.
- Zero vocab de banca/prova/cai/gabarito/pegadinha.
- Sem bullets fora dos 3 casos canônicos (tabelas comparativas, cronologias com escala numérica, critérios clínicos discretos).
- Sem referência a outros resumos (cross-reference só intra-resumo).

## Seção D — Pontos de quebra do raciocínio

Voz de mecanismo, sem vocab de banca. Calibra `#atencao-box` da E1 e distratoras da E2.

1. **Quebra:** confundir lactato com piruvato como ponto de entrada. O lactato chega ao fígado e é convertido a piruvato pela LDH, gerando NADH citosólico que dispensa o ciclo do malato.
   **Correção:** quando o precursor é lactato, o caminho é mais curto (PEPCK pode ser usada diretamente após a piruvato carboxilase, sem precisar do shuttle).
   *(origem interna: q-393, q-403, q-316, q-396)*

2. **Quebra:** tratar piruvato → PEP como reação inversa da piruvato-quinase. O caminho real é piruvato → OAA (piruvato carboxilase, mitocôndria, 1 ATP, biotina, ativador acetil-CoA) → OAA → malato → OAA citosólico → PEP (PEPCK, 1 GTP). Dois passos, dois compartimentos, dois fosfatos energéticos.
   **Correção:** o "bypass" é uma cadeia, não um único passo. A PEPCK gasta GTP, não ATP, e descarboxila o OAA (libera o mesmo CO2 que a piruvato carboxilase tinha adicionado).
   *(origem interna: q-393, q-403)*

3. **Quebra:** atribuir a hipoglicemia alcoólica a inibição direta de enzimas da gliconeogênese. Etanol não bloqueia enzima nenhuma — gera muito NADH ao ser oxidado, e esse NADH desloca o equilíbrio para LDH (piruvato → lactato) e MDH (OAA → malato).
   **Correção:** inibição indireta por roubo de substrato. Sem piruvato e sem OAA disponíveis no citosol, a piruvato carboxilase e a PEPCK ficam sem matéria-prima. Resultado clínico: hipoglicemia + acidose láctica.
   *(origem interna: q-280)*

4. **Quebra:** acreditar que ácidos graxos de cadeia par podem gerar glicose. Em mamíferos, acetil-CoA entra no Krebs e perde 2 carbonos como CO2 antes de chegar ao OAA — saldo líquido de carbono = 0.
   **Correção:** só glicerol (entra como DHAP) e fração marginal dos AG de cadeia ímpar (via propionil-CoA → succinil-CoA) contribuem para a gliconeogênese. AG par é tabu.
   *(origem interna: q-287, q-314)*

5. **Quebra:** confundir F1,6BP (intermediário da via, substrato da FBPase-1) com F2,6BP (regulador alostérico, nunca entra na via). Nomes parecidíssimos, papéis opostos.
   **Correção:** F1,6BP carrega 2 fosfatos da via metabólica e é hidrolisada pela FBPase-1 a F6P + Pi. F2,6BP é puro sinal, produzida pela enzima bifuncional PFK-2/FBPase-2 fora da via — ativa PFK-1 e inibe FBPase-1.
   *(origem interna: q-310)*

6. **Quebra:** interpretar custo da gliconeogênese a partir de glicerol como igual ao do piruvato. Glicerol custa 1 ATP por molécula (glicerol-quinase); 2 glicerois fazem 1 glicose → 2 ATP/glicose, contra 6 ATP/glicose pela via do piruvato.
   **Correção:** glicerol é o substrato mais barato em mamíferos. Quase um terço do custo do piruvato.
   *(origem interna: q-313)*

7. **Quebra:** considerar o ciclo de Cori "neutro" em ATP (só carbono). Cori é neutro em NADH, mas energeticamente assimétrico em ATP: músculo gera 2 ATP por glicólise anaeróbica; fígado gasta 6 ATP para refazer a glicose. O ciclo transfere o ônus energético para o fígado (aeróbico).
   **Correção:** Cori é neutro em poder redutor (NADH), não em moeda energética. O músculo "explora" o fígado.
   *(origem interna: q-316, q-396)*

8. **Quebra:** equiparar Cori e ciclo glicose-alanina. Ambos enviam carbono ao fígado, mas só a alanina carrega nitrogênio (grupo amino) — o que protege o músculo da toxicidade da amônia livre, transferindo para o fígado a tarefa de fazer ureia.
   **Correção:** Cori transporta carbono; glicose-alanina transporta carbono + nitrogênio.
   *(origem interna: q-394, q-389)*

9. **Quebra:** acreditar que músculo faz gliconeogênese. Músculo não tem G6Pase — não consegue exportar glicose. Faz só glicólise (Cori) ou exporta alanina.
   **Correção:** quem alimenta o sangue é fígado e, em jejum prolongado/acidose, rim. Música muscular = consumo local de G6P (glicogênio próprio ou via Cori indireto).
   *(origem interna: q-386, q-389, q-390, q-391, q-394)*

10. **Quebra:** confundir custo com saldo na contagem energética. A gliconeogênese gasta 4 ATP + 2 GTP + 2 NADH para sintetizar 1 glicose a partir de 2 piruvatos. Os 2 NADH consumidos pela GAPDH reversa são custo adicional, mas não contam como ATP no cálculo simplificado de "6 ATP equivalentes".
   **Correção:** quando se diz "custa 6 ATP por glicose", a conta é 2 ATP (piruvato carboxilase) + 2 GTP (PEPCK) + 2 ATP (fosfoglicerato-quinase reversa). NADH conta separadamente.
   *(origem interna: q-319, q-396)*

11. **Quebra:** atribuir hipoglicemia em von Gierke a falta de glicogênio. O paciente tem glicogênio EM EXCESSO (hepatomegalia clássica) — o problema é não conseguir converter G6P em glicose livre por ausência de G6Pase.
   **Correção:** hipoglicemia paradoxal — estoque cheio, saída entupida. G6P se acumula e desvia para glicólise local (lactato → acidose láctica), via das pentoses (hiperuricemia) e glicogênese (mais hepatomegalia).
   *(origem interna: q-310, integração clínica do cronograma)*
