# TEMA CARD — Ciclo de Krebs

## Seção A — Identificação

- **Tema:** Ciclo de Krebs (ciclo do ácido cítrico / TCA) — incluindo a porta de entrada (complexo da piruvato desidrogenase, PDH) e funções anfibólicas + regulação.
- **Slug canônico:** `ciclo-krebs` (bate com `figuras/ciclo-krebs/` já extraída; aula no banco é `bioq-17-ciclo-krebs-TE-I`, mas o sufixo `TE-I` pertence à aula 18 — Cadeia Respiratória — e fica de fora aqui).
- **Disciplina:** Bioquímica — Metabolismo aeróbico de carboidratos.
- **Slide-fonte:** `slides/slides-e-resumos/B - Primeiro ano/UC01/Bioquímica/17 - Ciclo de Krebs/Ciclo de Krebs - slides.pdf` (44 slides, Profa. Marisa Helena). Extraídos em `figuras/ciclo-krebs/` com `MAPA_CONTEUDO.txt`.
- **Onde estudar:** Lehninger 7ª ed., Cap. 16 (Ciclo do ácido cítrico) — pp. 633–678 + Cap. 17.1 (funções anfibólicas) pp. 686–692.
- **Recorte slide × tema:** sem corte. Slide cobre PDH (8–17), 8 reações do ciclo (18–38), funções anfibólicas e anaplerose (39–44). **Não invade ETC** — fecha em "NADH/FADH₂ prontos para ceder elétrons à cadeia, próxima aula".
- **Alvo de páginas E1:** piso 11, teto 22. Justificativa: PDH (3 enzimas, 5 coenzimas) + 8 reações enzimáticas encadeadas + 2 figuras obrigatórias de cadeia + anaplerose + 4 quebras clínicas (beribéri, fluoracetato, von Gierke análoga em outros DBM, drenagem do OAA em jejum) — tema denso por construção.
- **Pasta de trabalho:** `typst-build/` raiz. Saída final: `resumos-gerados/CICLO-KREBS.pdf`.

## Seção B — Estrutura da E1

### PARTE I — Do piruvato ao acetil-CoA: a porta de entrada (3 subtópicos)

**1.1 — Por que o piruvato não entra direto no ciclo**
- Pergunta de abertura: "Se a glicólise terminou em piruvato, por que o ciclo de Krebs não pega o piruvato e começa?"
- Retomar pré-requisitos em 2 frases: glicólise terminou no citosol, rendeu 2 ATP líquidos + 2 NADH + 2 piruvatos por glicose; mitocôndria é o "andar de cima" onde a oxidação completa acontece.
- Piruvato precisa atravessar duas membranas: a externa (porina, livre) e a interna (transportador de monocarboxilato — exige carregador específico). Já no lúmen mitocondrial (matriz), encontra o complexo PDH.
- Por que descarboxilar antes? Para entregar um fragmento de 2 carbonos (acetil) ligado a um carregador que o sítio da citrato sintase reconhece — a coenzima A. Piruvato (3C) tem um grupo carboxila a mais; precisa ser oxidado e perder esse C como CO₂ antes de virar substrato do ciclo.
- Figuras: `slide-06.png` (glicose→piruvato→mitocôndria), `slide-07.png` (todas as enzimas do Krebs estão na mitocôndria), `slide-08.png` (descarboxilação oxidativa).

**1.2 — O complexo PDH: 3 enzimas, 5 coenzimas, 1 braço móvel**
- Pergunta: "Por que um complexo gigante de 60 cópias de enzima para fazer uma única descarboxilação?"
- Resposta: porque o intermediário gerado é instável e tóxico se escapar. Manter substrato preso a um carregador (ácido lipóico) que oscila entre 3 sítios catalíticos é a solução: zero perda, zero contaminação cruzada.
- Identidade das 3 enzimas: **E1 — piruvato desidrogenase** (descarboxila o piruvato, usa TPP); **E2 — diidrolipoil transacetilase** (acopla acetil ao CoA, usa ácido lipóico); **E3 — diidrolipoil desidrogenase** (regenera o lipoamida, usa FAD e NAD⁺).
- As 5 coenzimas: TPP (de tiamina, vit B1), ácido lipóico (com braço de 1,4 nm de dissulfeto), CoA (de ácido pantotênico, B5), FAD (de riboflavina, B2), NAD⁺ (de niacina, B3). Quatro são vitamínicas — falta de vitamina = falência da entrada do ciclo.
- Saldo da reação: piruvato + CoA + NAD⁺ → acetil-CoA + CO₂ + NADH. ΔG⁰' muito negativo (~-33 kJ/mol) — **irreversível**. Marca o ponto sem retorno do metabolismo da glicose: do acetil-CoA não há volta para glicose (é o tabu do AG par).
- Figuras: `slide-09.png` (multienzima E. coli), `slide-10.png` (CoA, ligação tioéster), `slide-11.png` (E1/E2/E3), `slide-17.png` (passos da reação).

**1.3 — Beribéri: quando a vitamina B1 acaba**
- Pergunta: "O que acontece com um paciente alcoolista crônico que para de comer? Por que o cérebro é o primeiro a falhar?"
- Tiamina (B1) é cofator obrigatório da PDH e também da α-cetoglutarato desidrogenase (passo 4 do ciclo). Sem B1 → PDH para → piruvato acumula → vai pra LDH → lactato sobe → acidose láctica.
- Tecidos mais vulneráveis: os que mais dependem de glicose oxidativa. Cérebro encabeça (consome ~120 g glicose/dia).
- Apresentação clínica clássica: beribéri (úmido = cardiomegalia, edema; seco = neuropatia periférica) e Wernicke-Korsakoff (ataxia, oftalmoplegia, confusão, amnésia). Por isso, em PS, paciente etilista que chega com glicose IV recebe tiamina ANTES — glicose sem tiamina precipita Wernicke agudo.
- `#atencao-box`: confundir B1 (tiamina) com B12 (cobalamina) — efeitos clínicos diferentes, vitaminas distintas. B12 entra em metilmalonil-CoA, não em Krebs.
- Figura: `slide-13.png` (TPP), `slide-14.png` (tiamina, beribéri).

### PARTE II — As 8 reações do ciclo (4 subtópicos — coração do resumo)

**2.1 — Visão geral antes de mergulhar nas 8 reações**
- Pergunta: "Por que se chama 'ciclo'? Por que o oxaloacetato volta no final?"
- O OAA é catalítico, não consumível: cada volta começa com 4 carbonos do OAA + 2 carbonos do acetil-CoA → 6 carbonos no citrato → perde 2 como CO₂ → volta a 4 carbonos no OAA. Concentração de OAA na mitocôndria é baixíssima (~1 µM) — qualquer drenagem para anaplerose freia o ciclo.
- Saldo por volta: **3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂** (mais 1 CoA reciclada). Por glicose (2 piruvatos → 2 voltas): 6 NADH + 2 FADH₂ + 2 GTP + 4 CO₂. Somando com PDH (2 NADH adicionais) e glicólise (2 NADH + 2 ATP), o catabolismo aeróbico da glicose entrega 10 NADH + 2 FADH₂ + 4 ATP equivalentes — e só depois a cadeia respiratória traduz esses NADH/FADH₂ em ATP.
- 4 reações de oxidorredução por volta (isocitrato, α-KG, succinato, malato). 2 descarboxilações (isocitrato → α-KG e α-KG → succinil-CoA — perdem o CO₂). 1 fosforilação em nível de substrato (succinil-CoA → succinato).
- Figura obrigatória: cadeia das 8 reações com produtos numerados. Slides: `slide-18.png`, `slide-31.png`, `slide-33.png` — escolha a mais panorâmica.

**2.2 — Passos 1–4: condensação, isomerização, primeira e segunda oxidação**
- **Passo 1 — citrato sintase.** Condensa OAA (4C) + acetil-CoA (2C) → citrato (6C) + CoA livre. ΔG muito negativo (-32 kJ/mol) — irreversível, regulada por disponibilidade de OAA e por feedback de citrato/succinil-CoA/NADH.
- **Passo 2 — aconitase.** Isomeriza citrato → isocitrato via cis-aconitato (move uma hidroxila do C tercário para o C secundário). Não é redox, mas é o ponto de entrada do **fluoracetato**: pesticida (e veneno de rato 1080) que vira fluoracetil-CoA, condensa com OAA, gera fluorocitrato — análogo que inibe a aconitase em vez de ser substrato. Resultado: ciclo paralisa, citrato acumula. Toxicidade humana: dose letal 2–10 mg/kg, sintomas em 30–100 min (náusea, vômito, convulsão, parada cardíaca).
- **Passo 3 — isocitrato desidrogenase (IDH).** Primeira oxidação do ciclo: isocitrato → α-cetoglutarato (α-KG) + CO₂ + NADH. **Passo regulatório-mor:** inibida por ATP/NADH, ativada por ADP/Ca²⁺. É o "interruptor de velocidade" do ciclo.
- **Passo 4 — α-cetoglutarato desidrogenase (α-KGDH).** Segunda oxidação: α-KG → succinil-CoA + CO₂ + NADH. Mecanismo idêntico ao da PDH — mesmas 5 coenzimas, mesma arquitetura E1/E2/E3, e a tiamina aqui é a mesma. Por isso, deficiência de B1 paralisa duas etapas oxidativas (PDH e α-KGDH). Inibida por NADH e succinil-CoA; ativada por Ca²⁺.
- Figuras: `slide-19.png` (citrato sintase), `slide-20.png` (isomerização citrato), `slide-21.png` (fluoracetato/pesticida), `slide-22.png` (primeira oxidação), `slide-25.png` (segunda oxidação, semelhança com PDH).

**2.3 — Passos 5–8: GTP, terceira oxidação, hidratação, quarta oxidação**
- **Passo 5 — succinil-CoA sintetase.** Hidrólise da ligação tioéster (rica em energia) acoplada à fosforilação de GDP → GTP. Este é o ÚNICO ATP-equivalente gerado em **fosforilação em nível de substrato** dentro do ciclo. GTP é convertido em ATP por nucleosídeo difosfato quinase (`GTP + ADP → GDP + ATP`). Em alguns tecidos (músculo cardíaco), a isoforma gera ATP direto.
- **Passo 6 — succinato desidrogenase (SDH).** Terceira oxidação: succinato → fumarato + FADH₂. **Particularidade topológica:** SDH é a única enzima do ciclo **embutida na membrana mitocondrial interna** — ela É o Complexo II da cadeia respiratória. Os elétrons do FADH₂ não saem da enzima; entram direto na cadeia (UQ). Isso vale 1.5 ATP por FADH₂, contra 2.5 ATP por NADH.
- **Passo 7 — fumarase.** Hidratação estereoespecífica: fumarato + H₂O → L-malato. Não é redox, não gasta nem libera energia significativa. Importante notar a estereoquímica L (só esse enantiômero serve à próxima enzima).
- **Passo 8 — malato desidrogenase (MDH).** Quarta oxidação: malato → OAA + NADH. ΔG⁰' positivo (+30 kJ/mol) — a reação é desfavorável em equilíbrio, mas roda no sentido oxidativo porque a citrato sintase no passo seguinte consome OAA rapidamente (princípio de Le Chatelier — drenagem do produto puxa a reação).
- Figuras: `slide-26.png` (fosforilação em nível de substrato), `slide-29.png` (FAD aceita 2 elétrons), `slide-30.png`, `slide-32.png` (regeneração de OAA).

**2.4 — Regulação por carga energética**
- Pergunta: "Por que o ciclo desacelera depois de comer e acelera no exercício?"
- Três pontos de controle: **citrato sintase, IDH, α-KGDH**. Os três respondem ao mesmo sinal: relação NADH/NAD⁺ e ATP/ADP. Alto ATP/NADH (estado bem alimentado, mitocôndria descansada) → inibe. Alto ADP/NAD⁺ + Ca²⁺ (exercício, contração muscular libera Ca²⁺ pro citosol e matriz) → ativa.
- O Ca²⁺ é o sinal de "trabalho começou" — ele ativa IDH e α-KGDH em paralelo com a contração muscular, acoplando o suprimento mitocondrial à demanda contrátil.
- Inibição cruzada por produtos: succinil-CoA inibe citrato sintase e α-KGDH (sinaliza que o ciclo está engarrafado depois do passo 4); citrato inibe a PFK-1 na glicólise (informa que há substrato suficiente entrando, não precisa gerar mais piruvato).
- O ciclo também é freado se a cadeia respiratória parar (NADH não é reoxidado). Foi o que oligomicina e cianeto demonstram em curso: bloqueando a ATP-sintase ou o Complexo IV, o gradiente acumula, NADH/NAD⁺ explode, IDH e α-KGDH desligam, PDH desfosforila para off (kinase ativada por NADH alto). Ciclo todo para mesmo sem mexer nele diretamente.
- Figura: `slide-38.png` (visão integrada da regulação), `slide-39.png` (anfibolismo).

### PARTE III — Anfibolismo, anaplerose e integração clínica (3 subtópicos)

**3.1 — Krebs como hub: catabolismo E biossíntese**
- Pergunta: "Se o ciclo é catabólico, por que a célula tira intermediários dele para fazer outras coisas?"
- Anfibólico = serve aos dois sentidos. Intermediários são saqueados a todo instante para biossíntese:
  - **α-cetoglutarato** → glutamato (transaminação direta) → glutamina, prolina, arginina, hema (parcialmente).
  - **Oxaloacetato** → aspartato (transaminação) → asparagina, pirimidinas, gliconeogênese (sai pra PEP).
  - **Succinil-CoA** → porfirinas (heme da hemoglobina) — combinada com glicina é o primeiro passo da síntese do anel pirrólico.
  - **Citrato** → exporta para o citosol → vira acetil-CoA citosólico (substrato da síntese de ácido graxo) + OAA.
- Toda saída drena OAA (direta ou indiretamente). Se nada repuser, o ciclo morre por falta de matéria-prima para o passo 1.

**3.2 — Anaplerose: piruvato carboxilase mantém o ciclo de pé**
- Pergunta: "Como o ciclo continua se o OAA está sendo drenado o tempo todo?"
- Reação anaplerótica principal: **piruvato carboxilase** (fígado, rim) — `piruvato + HCO₃⁻ + ATP → OAA + ADP + Pi`. Enzima alostérica que é **virtualmente inativa sem acetil-CoA** — só liga quando a célula sinaliza "tem combustível, mas falta OAA pra queimar".
- Esta é a mesma enzima que a aula de gliconeogênese mostrou — agora vista do outro ângulo: lá ela serve para gerar OAA → PEP → glicose; aqui serve para repor OAA → manter Krebs rodando.
- Outras vias anapleróticas: degradação de aminoácidos glicogênicos (entram no ciclo em vários pontos), propionil-CoA da β-oxidação de AG ímpares (vira succinil-CoA).
- Aqui também o tabu se confirma: AG de cadeia par dá só acetil-CoA → consumido no ciclo, **não reabastece** carbono líquido (os 2C entram e saem como 2 CO₂). Por isso AG par não vira glicose. Glicerol e AG ímpares conseguem porque entram em pontos que aumentam o pool de OAA.
- Figuras: `slide-40.png` (regulação por acetil-CoA), `slide-41.png` (reação piruvato carboxilase).

**3.3 — Por que o ciclo "para" em jejum prolongado e o que acontece depois**
- Pergunta: "Se Krebs é a usina central, por que cetoacidose acontece no jejum prolongado?"
- Resposta mecanística: em jejum, o fígado precisa fazer glicose para o cérebro (gliconeogênese). Quem fornece o esqueleto? OAA. O OAA hepático é drenado para a via gliconeogênica (vira PEP via PEPCK) — sai do ciclo, vai para a glicose nova.
- Com OAA baixo, a citrato sintase não tem com quem condensar o acetil-CoA que está chegando em torrente da β-oxidação dos AG. Acetil-CoA acumula. A mitocôndria desvia o excedente para a síntese de corpos cetônicos (acetoacetato, β-hidroxibutirato, acetona).
- Em jejum bem prolongado isso é fisiológico — o cérebro adapta os carregadores e passa a queimar corpos cetônicos como combustível principal. Mas em descompensação patológica (DM1 sem insulina, jejum + álcool), os cetônicos sobem demais e baixam o pH sanguíneo: cetoacidose.
- Aforismo dos livros: "**os ácidos graxos queimam na fogueira dos carboidratos**". Tradução mecanística: você só consegue oxidar acetil-CoA da β-oxidação até CO₂ se houver OAA suficiente — e o OAA vem, em última instância, do piruvato (i.e., dos carboidratos) via piruvato carboxilase. Sem carboidrato, sem OAA reposto, sem combustão completa → cetose.
- Encerramento que aponta para a próxima aula: todo o NADH e FADH₂ produzido aqui agora vai ceder elétrons à cadeia respiratória, onde o gradiente de prótons gera o ATP de verdade. Krebs é o moedor; ETC é a usina.
- Figuras: `slide-42.png`, `slide-43.png`, `slide-44.png` (integração final).

### Mindmap de fechamento (1 página, antes do Resumindo)

- **Mensagem-síntese:** O ciclo de Krebs oxida o acetil-CoA a 2 CO₂ guardando a energia em 3 NADH + 1 FADH₂ + 1 GTP por volta — e ainda banca biossíntese de aminoácidos e heme cedendo intermediários, desde que a anaplerose reponha o oxaloacetato.
- **3 estações (com setas, cor a→neutra-pivô→b):**
  1. **Entrada** → PDH irreversível, 5 coenzimas, perde 1 CO₂, gera 1 NADH, ata acetil ao CoA.
  2. **Oito reações** → 4 oxidações (3 NADH + 1 FADH₂), 2 descarboxilações (2 CO₂), 1 GTP (succinil-CoA sintetase), regenera OAA.
  3. **Saídas e reposição** → α-KG/OAA/succinil-CoA cedidos pra biossíntese; piruvato carboxilase (ativada por acetil-CoA) repõe OAA.
- **3 cartões:**
  - **Quem manda na velocidade:** IDH (e α-KGDH) — sinais ADP/Ca²⁺ aceleram, ATP/NADH freiam.
  - **Quando o ciclo para na clínica:** beribéri (sem B1, PDH+α-KGDH desligam) · fluoracetato (inibe aconitase) · jejum prolongado (OAA drenado, acetil-CoA vira cetônico).
  - **Por que importa para a próxima aula:** o NADH e FADH₂ daqui é o combustível literal da cadeia respiratória — só lá vira ATP.

### Resumindo (1–2 páginas, 10–12 seções, ordem clínica decrescente)

Ordem proposta:
1. PDH irreversível: porta de entrada do acetil-CoA, 5 coenzimas vitamínicas.
2. Saldo por volta (3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂) e por glicose.
3. Oito reações em 1 frase: condensação → isomerização → 2 oxidações com descarboxilação → GTP por substrato → 2 oxidações + 1 hidratação → OAA.
4. SDH = Complexo II: a única enzima do ciclo na membrana interna.
5. Reguladores-mor: IDH e α-KGDH respondem a ATP/NADH e Ca²⁺.
6. Anfibólico: α-KG, OAA e succinil-CoA cedem esqueleto para biossíntese.
7. Anaplerose: piruvato carboxilase repõe OAA (ativada por acetil-CoA).
8. Beribéri (B1): PDH e α-KGDH param, lactato sobe, Wernicke ataca SNC.
9. Fluoracetato: bloqueia aconitase, citrato acumula, ciclo trava.
10. Jejum prolongado: OAA drenado pra gliconeogênese → acetil-CoA vira cetônico.
11. Aforismo: AG queima na fogueira dos carboidratos (sem OAA, não há combustão completa).
12. Conexão com ETC: cada NADH vale ~2,5 ATP e cada FADH₂ ~1,5 ATP — feito na próxima aula.

## Seção C — Diretrizes editoriais específicas

### Diretriz dominante (canônico 2026-05-25)

**Baseline baixo + dificuldade real.** O aluno chega aqui depois de glicólise/gliconeogênese — sabe que glicose vira piruvato, mas tem visão nebulosa de mitocôndria, ainda confunde NAD⁺/FAD com ATP, e nunca pensou em por que existem 5 coenzimas na PDH. Cada subtópico abre com pergunta ingênua plausível. Mecanismo antes do nome da enzima. Pré-requisitos retomados em 1–2 frases (β-oxidação, transaminação, ATP-sintase, gradiente de prótons). Aprofundamento em camadas: porquê cru → nuance → exceção → clínica.

### Voz e registros

- Diálogo do início ao fim. Variar registro entre subtópicos (≥3 dos 5 canônicos: enquadramento, integração-com-anterior, integração-com-posterior, analogia concreta moderna, ponto de quebra).
- **Subtópicos mais densos:** 1.2 (PDH com 3 enzimas e 5 coenzimas) e 2.3 (passos 5–8 incluindo SDH como Complexo II). Podem chegar a 450–500 palavras cada. Figura obrigatória da cadeia das 8 reações em 2.1 ou 2.2.
- **Tabela permitida em 2.1:** saldo por volta enzima-por-enzima (passo | substrato → produto | classe | cofator | produto carregador). Caso (a) — comparativo 3+ dimensões.
- Conclusão integradora obrigatória ao fim da PARTE III, costurando entrada (PDH), moinho (8 reações) e saídas (anfibolismo, regulação, ETC).

### Jargão controlado — siglas e termos-nota

- **Siglas via `#sigla()` na 1ª aparição:** PDH (piruvato desidrogenase), CoA (coenzima A), NAD⁺ (nicotinamida adenina dinucleotídeo), NADH, FAD (flavina adenina dinucleotídeo), FADH₂, TPP (tiamina pirofosfato), GTP (guanosina trifosfato), GDP, ATP, ADP, Pi (fosfato inorgânico), CO₂, OAA (oxaloacetato), α-KG (α-cetoglutarato), IDH (isocitrato desidrogenase), SDH (succinato desidrogenase), MDH (malato desidrogenase), α-KGDH (α-cetoglutarato desidrogenase), TCA (ácidos tricarboxílicos), ETC (cadeia respiratória), LDH (lactato desidrogenase), PFK-1, PEP, PEPCK.
- **Termos-nota via `#termo-nota[][]`:** acetil-CoA, ácido lipóico, ligação tioéster, anaplerose, beribéri, Wernicke-Korsakoff, fluoracetato, anfibólico. Alvo 6–8 — não passar.

### Figuras

- Meta: mínimo 3 imagens por PARTE; cadeia das 8 reações é **figura obrigatória** (canônico — ≥5 reações encadeadas).
- Default `#figura-nebli(..., largura: 65%)`; cadeia multi-passo `largura: 85%`; texto curto+figura média `#figura-lateral`.
- Caminhos com prefixo `/` (`/figuras/ciclo-krebs/slide-XX.png`). Validar via `MAPA_CONTEUDO.txt` antes de citar.

### Proibições inegociáveis

- Sem mapa mental SVG (`#mapa-parte` proibido).
- Sem caixa alta para ênfase.
- Zero vocab de banca/prova/cai/gabarito/pegadinha.
- Sem bullets fora dos 3 casos canônicos.
- Sem referência a outros resumos (cross-reference só intra-resumo, ex: "como vimos no 1.2 da PDH").
- Sem invadir cadeia respiratória além de "elétrons vão para a cadeia, próxima aula".

## Seção D — Pontos de quebra do raciocínio

Voz de mecanismo, sem vocab de banca. Calibra `#atencao-box` da E1 e distratoras da E2.

1. **Quebra:** confundir GTP gerado no passo 5 com ATP e contar 2 ATP por volta. Succinil-CoA sintetase gera **GTP** (em alguns tecidos ATP direto, isoformas), prontamente convertido a ATP por nucleosídeo difosfato quinase — saldo equivalente é **1 ATP por volta**.
   **Correção:** 1 GTP = 1 ATP de fosforilação em nível de substrato; a maior parte do ATP do ciclo vem indireta da reoxidação dos 3 NADH + 1 FADH₂ na ETC (~10 ATP/volta).
   *(origem: q-0169, q-0288, q-0325)*

2. **Quebra:** localizar a SDH na matriz como as outras enzimas do ciclo. SDH é a **única** enzima do ciclo na membrana mitocondrial interna — ela É o Complexo II da cadeia respiratória, e por isso entrega FADH₂ direto à ubiquinona sem precisar atravessar.
   **Correção:** SDH = Complexo II. O FADH₂ não é "liberado" — é parte integrante da enzima e cede 2 elétrons à UQ. É também por isso que FADH₂ rende menos ATP (~1.5) que NADH (~2.5): entra na cadeia em ponto mais a jusante.
   *(origem: q-0157, q-0388, q-0400)*

3. **Quebra:** achar que acetil-CoA atravessa a membrana mitocondrial interna para sair pro citosol e virar AG. Acetil-CoA **não atravessa** essa membrana. O que atravessa é o **citrato** (via transportador tricarboxilato), que no citosol é clivado pela ATP-citrato liase em acetil-CoA + OAA — caminho para a síntese de AG.
   **Correção:** citrato sai, vira acetil-CoA citosólico. Acetil-CoA mitocondrial fica preso na matriz.
   *(origem: q-0312)*

4. **Quebra:** confundir os 5 cofatores da PDH com os 5 cofatores do ciclo. Os cofatores da PDH (TPP, ácido lipóico, CoA, FAD, NAD⁺) são repetidos integralmente pela α-KGDH (passo 4 do ciclo), por isso a deficiência de B1 paralisa as duas. As outras enzimas usam só NAD⁺ (IDH, MDH), FAD (SDH) ou nenhum cofator redox (citrato sintase, aconitase, fumarase).
   **Correção:** as 5 coenzimas TPP/lipóico/CoA/FAD/NAD⁺ aparecem 2 vezes no metabolismo da glicose — uma em PDH e outra em α-KGDH. Beribéri ataca os dois pontos.
   *(origem: q-0288)*

5. **Quebra:** acreditar que oligomicina/cianeto paralisam o ciclo "atacando enzima do ciclo". Eles não tocam nenhuma enzima do TCA. Bloqueiam a ATP-sintase (oligomicina) ou o Complexo IV (cianeto) — o gradiente de prótons acumula, a cadeia não consegue mais oxidar NADH, NAD⁺ desaparece, IDH e α-KGDH não têm aceptor, e a PDH é fosforilada/desligada por sinal indireto (NADH alto ativa a PDH-kinase). Resultado: ciclo travado por **falta de NAD⁺**, não por ataque direto.
   **Correção:** desacoplador (DNP) faz o oposto — colapsa o gradiente, NAD⁺ é reoxidado em torrente, ciclo e PDH disparam, consumo de O₂ sobe, mas o ATP cai porque a ATP-sintase fica sem força motriz protônica. Maior consumo de O₂ + menor ATP é a assinatura de desacoplamento.
   *(origem: q-0312, q-0325, q-0387)*

6. **Quebra:** considerar o ciclo "fechado" em carbono e ignorar anaplerose. O ciclo é tão drenado para biossíntese (α-KG → glutamato, OAA → aspartato, succinil-CoA → heme) que precisa ser reabastecido continuamente. **Piruvato carboxilase** é a principal reposição, ativada por acetil-CoA — só liga quando há combustível esperando pra ser queimado e falta OAA.
   **Correção:** sem anaplerose, OAA cai a zero e a citrato sintase para. É por isso que dieta zero-carboidrato eventualmente cai em cetose: piruvato escassea (vem dos carboidratos), OAA não é reposto, acetil-CoA da β-oxidação vira corpo cetônico.
   *(origem: q-0211, q-0388)*

7. **Quebra:** atribuir o aforismo "AG queima na fogueira dos carboidratos" a uma exigência energética. O AG não precisa de energia do carboidrato — precisa do **OAA** que vem (em última instância) do piruvato via piruvato carboxilase. Sem OAA, o acetil-CoA da β-oxidação não tem com quem condensar e desvia para cetogênese.
   **Correção:** a "fogueira" é OAA. Sem carboidrato → sem piruvato → sem piruvato carboxilase → sem OAA → sem combustão completa do acetil-CoA.
   *(origem: integração clínica do cronograma)*

8. **Quebra:** confundir fluoracetato com inibidor reversível ou competitivo simples. Fluoracetato entra no ciclo como fluoracetil-CoA, é condensado pelo citrato sintase em fluorocitrato — esse análogo se liga firmemente ao sítio da aconitase e a inativa. Inibição "letal síntese": a toxina só é fabricada DEPOIS de entrar no ciclo (suicida).
   **Correção:** fluoracetato é exemplo clássico de **inibição por síntese letal** — a célula fabrica o próprio veneno. Citrato acumula a montante; ciclo para. Sintomas em 30–100 min, dose letal humana 2–10 mg/kg.
   *(origem: slide 21, livro-texto)*

9. **Quebra:** equiparar PDH e α-KGDH ao ponto de chamar uma de "irmã" da outra sem entender a diferença. Mesmo mecanismo, mesmas 5 coenzimas, mesma arquitetura E1/E2/E3 — mas substratos e produtos diferentes (PDH: piruvato → acetil-CoA + CO₂; α-KGDH: α-KG → succinil-CoA + CO₂). PDH é regulada por **fosforilação** (PDH-kinase desliga, PDH-fosfatase liga); α-KGDH é regulada por **alosteria** (NADH e succinil-CoA inibem; Ca²⁺ ativa).
   **Correção:** mesmo motor enzimático, regulação distinta. PDH responde a sinais hormonais (insulina/glucagon via cascata fosforilativa); α-KGDH responde a estado redox e Ca²⁺ direto.
   *(origem: q-0288)*

10. **Quebra:** contar 2 NADH na primeira volta do ciclo (esquecendo o do MDH) ou 4 NADH (contando o da PDH como se fosse do ciclo). **3 NADH** no ciclo por volta (IDH, α-KGDH, MDH); o NADH da PDH é da entrada, não do ciclo em si. Por glicose: 2 NADH da PDH + 6 NADH do ciclo (2 voltas).
   **Correção:** memorizar "3-1-1-2 por volta": 3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂.
   *(origem: q-0169, q-0288, q-0320)*

11. **Quebra:** achar que o ciclo só roda em aeróbio e que MDH é "inviável" porque a reação tem ΔG⁰' positivo. A reação roda por princípio de Le Chatelier — a citrato sintase consome OAA imediatamente, mantendo a concentração baixíssima, o que puxa a MDH no sentido oxidativo. A oxigênio importa indiretamente: sem O₂, a cadeia respiratória para, NADH não é reoxidado a NAD⁺, IDH/α-KGDH/MDH ficam sem aceptor, ciclo para por falta de NAD⁺.
   **Correção:** ciclo precisa de **NAD⁺ disponível**, e NAD⁺ só é regenerado quando a ETC funciona — daí a dependência indireta do O₂. Em hipóxia, lactato sobe (LDH regenera NAD⁺ no citosol) mas a mitocôndria fica parada.
   *(origem: q-0312, q-0325, q-0400)*
