# Tema Card — Insuficiência Cardíaca (Caso PBL MSP4211)

## Seção A — Identidade

- **Tema:** Insuficiência Cardíaca — Caso clínico 02 (paciente masculino 64 anos, IAM jan/2025 → IC isquêmica com FE 40% em jan/2026).
- **Disciplina:** MSP4211 — Discussão Integrada de Casos I (1º ano FMUSP).
- **Slug:** `insuficiencia-cardiaca`.
- **Profundidade:** **PROFUNDO** (10 Cons · 15 Int · 5 Apl). Caso longitudinal com 12 perguntas orientadoras + 10 competências exige integração entre histologia muscular + fisiologia da bomba + eletrofisiologia + leis físicas (Frank-Starling do sarcômero + forças de Starling do capilar) + ácido-base + clínica + ética.
- **Tamanho-alvo:** piso 16, **teto 35 páginas** (excepcionalmente ampliado para 35 — autorizado por Davi 2026-05-29 dada cobertura obrigatória das 12 perguntas + 10 competências). Distribuição: PARTE 1 ≈ 10–12 pp · PARTE 2 ≈ 11–13 pp · PARTE 3 ≈ 10–12 pp · Conclusão + Resumindo ≈ 2–3 pp.
- **Onde estudar:** Guyton & Hall *Tratado de Fisiologia Médica* cap. 9 (músculo cardíaco) + cap. 22 (insuficiência cardíaca); Berne & Levy cap. ciclo cardíaco; Robbins cap. coração; Diretriz Brasileira de IC Crônica (Arq Bras Cardiol 93 supl.01); NEJM 356:1140 — "The Failing Heart: An Engine Out of Fuel".
- **Recorte slide × tema:** sem corte. Caso cobre IAM agudo (jan/2025) + IC isquêmica descompensada (jan/2026); a PARTE 3 da E1 narra exatamente essa trajetória, com as 12 perguntas como fio condutor implícito.
- **Calibração (substitui banco_slim):** as **12 perguntas orientadoras do PBL** são a régua de cobertura. Cada subtópico da E1 anota qual conjunto de perguntas ele responde; nada cai fora.
- **Pasta de trabalho:** `typst-build/` raiz. Saída: `resumos-gerados/INSUFICIENCIA-CARDIACA.pdf`.

## Seção B — Estrutura da E1

### PARTE 1 — O coração como bomba: contração, ciclo e a lei de Frank-Starling (4 subtópicos, ~10–12 pp)

**1.1 — Do sarcômero ao batimento: actina, miosina, cálcio**
- Pergunta de abertura (uma das 3 permitidas): "Por que o músculo cardíaco continua batendo a vida inteira sem aviso prévio, e o que dá força a cada batida?"
- Ultraestrutura do cardiomiócito: sarcômero como unidade contrátil (banda Z a banda Z), filamentos finos (actina + tropomiosina + troponina) e grossos (miosina com cabeças ATPásicas). Discos intercalares com junções comunicantes (gap junctions) — sincício funcional.
- Acoplamento excitação-contração: PA chega → túbulos T → canal de cálcio tipo L abre → entrada de Ca²⁺ extracelular → libera Ca²⁺ do retículo sarcoplasmático (RyR) → Ca²⁺ liga troponina C → tropomiosina sai do caminho → cabeça de miosina engata na actina → "power stroke" → ATP solta a cabeça → ciclo repete.
- Ciclo termina quando SERCA bombeia Ca²⁺ de volta ao RS (consome ATP) → troponina solta → tropomiosina volta → relaxamento.
- Justifica perguntas 6 (troponina + papel do Ca²⁺) e 7 (B3 + actina-miosina) do PBL.
- Figuras: `slide-12.png` (anatomia + cinética PA), figura externa de sarcômero (citada como referência se faltar).

**1.2 — Ciclo cardíaco e bulhas (B1, B2, B3)**
- Sequência: enchimento → contração isovolumétrica → ejeção → relaxamento isovolumétrico. Quatro válvulas comandam a direção (mitral, tricúspide, aórtica, pulmonar).
- **B1** = fechamento das atrioventriculares no início da sístole (mitral + tricúspide). **B2** = fechamento das semilunares no início da diástole (aórtica + pulmonar). Bulhas são vibrações de fechamento valvar transmitidas pelo sangue parado.
- **B3** = som de enchimento ventricular rápido precoce. Quando aparece em adulto com IC, significa que o ventrículo está **rígido e cheio demais**: o sangue chegando do átrio bate em uma parede que já não relaxa direito. É o "galope" patológico.
- Mecanismo molecular do B3 patológico: sarcômero hipertrofiado e fibrótico → complacência caiu → enchimento súbito gera vibração audível. Em jovens, B3 pode ser fisiológico (parede elástica + alto fluxo), mas em adulto com FE 40% é alarme.
- Justifica pergunta 7 do PBL e parte da pergunta 1 (sinais físicos do caso).
- Figuras: `slide-10.png` (anatomia do coração com câmaras), figura externa do ciclo cardíaco (Wiggers).

**1.3 — Lei de Frank-Starling do coração (não confundir com Starling capilar!)**
- Enunciado simples: **quanto mais a fibra cardíaca for esticada antes da contração, mais força ela gera na contração seguinte** — até um ponto ótimo. Esticar demais derruba a força.
- Mecanismo molecular: alongar o sarcômero até ~2,2 µm aproxima as cabeças de miosina dos sítios de actina; sensibilidade ao Ca²⁺ aumenta; mais pontes cruzadas se formam por unidade de tempo. Acima de 2,3–2,4 µm os filamentos se afastam, sítios de ligação somem, força cai.
- Tradução clínica: **pré-carga** é o quanto a fibra é esticada antes de contrair (≈ volume diastólico final, LVEDP). Coração normal sobe na curva quando enche mais. Coração doente está em um platô achatado — encher mais não compra mais débito, só sobe a pressão venosa para trás.
- **`#atencao-box` central:** Frank-Starling do coração ≠ forças de Starling do capilar. Ambas levam o nome do mesmo fisiologista, mas tratam de coisas diferentes: aqui o estiramento do sarcômero; lá adiante (PARTE 2) o equilíbrio Pc × πp na parede do vaso. O PBL pergunta as duas separadamente — confundir = perder a defesa no GD.
- Justifica perguntas 1 e 9 do PBL.
- Figuras: `slide-14.png` (curvas Frank-Starling: normal, aumentada e diminuída contratilidade).

**1.4 — Atividade elétrica organizada: nódulos, marcapasso e ECG normal**
- Nó sinoatrial (NSA) na parede do átrio direito = marcapasso (60–100 bpm em repouso). Onda de despolarização viaja pelo átrio → atinge o nó atrioventricular (NAV) — único caminho elétrico entre átrio e ventrículo, faz um atraso ≈100 ms para que o átrio esvazie antes do ventrículo contrair. Depois desce pelo feixe de His → ramos direito/esquerdo → fibras de Purkinje → ventrículo se contrai de baixo para cima.
- ECG na superfície corporal: **onda P** = despolarização atrial; **complexo QRS** = despolarização ventricular (massa maior → amplitude maior); **onda T** = repolarização ventricular; intervalo PR = atraso AV; segmento ST = platô do PA ventricular (entrada de Ca²⁺ se equilibrando com saída de K⁺).
- A repolarização atrial fica escondida dentro do QRS (princípio V da lista do enunciado).
- Justifica metade da pergunta 8 do PBL (mecanismo do ECG normal). A outra metade — alterações no IAM — fica na PARTE 3.
- Figuras: `slide-12.png` (NSA + NAV + PA + ECG).

### PARTE 2 — Quando a bomba falha: à frente e à trás (5 subtópicos, ~11–13 pp)

**2.1 — Pré-carga, pós-carga, contratilidade e débito cardíaco**
- **DC = FC × VS** (débito = frequência × volume sistólico). VS depende de três variáveis: pré-carga, pós-carga, contratilidade.
- **Pré-carga** = estiramento da fibra antes de contrair ≈ volume diastólico final. Sobe com retorno venoso, hipervolemia, regurgitação valvar.
- **Pós-carga** = resistência que o ventrículo precisa vencer para abrir a válvula semilunar e ejetar. Sobe com hipertensão arterial, estenose aórtica, vasoconstrição sistêmica.
- **Contratilidade** (inotropismo) = força gerada para uma dada pré-carga, independente do estiramento. Sobe com simpático, adrenalina, digital; cai com isquemia, acidose, IC avançada.
- Por que a curva de Frank-Starling **desce** na IC: contratilidade reduzida → para um mesmo LVEDP, o VS é menor. O coração precisa de pressão diastólica maior para produzir o mesmo débito → sobe pressão atrial esquerda → sobe pressão venosa pulmonar → edema pulmonar.
- Justifica pergunta 9 do PBL (Frank-Starling explica os sintomas).
- Figura: `slide-14.png` (curvas SV × LVEDP).

**2.2 — Remodelamento ventricular: hipertrofia, dilatação, cardiomegalia**
- Quando o coração trabalha contra carga crônica, ele remodela. Dois padrões:
  - **Hipertrofia concêntrica** (resposta à sobrecarga de pressão, ex. HAS): sarcômeros se replicam em **paralelo** → parede engrossa, câmara não dilata. Boa para vencer pós-carga, ruim para complacência (parede mais rígida).
  - **Hipertrofia excêntrica + dilatação** (sobrecarga de volume ou perda de miócitos, ex. pós-IAM): sarcômeros se replicam em **série** → câmara aumenta, parede fina relativamente. Coração entra na "câmara" da curva de Frank-Starling onde mais volume já não rende mais força.
- No paciente do caso: ictus deslocado para o 6º EICE a 2 dedos da LHE → câmara dilatada (`#atencao-box` discreto se couber). Eco mostra cardiomegalia global + dilatação apical + hipertrofia VE/AE = remodelamento misto, dirigido pela isquemia pós-IAM.
- Justifica pergunta 10 do PBL (adaptações histofuncionais + sinais radiológicos).
- Figuras: `slide-09.png` (RX com cardiomegalia), `slide-10.png` (eco com dilatação).

**2.3 — IC esquerda × IC direita: à frente e à trás**
- Princípio organizador: a IC é uma **falha de saída** — sangue se acumula **antes** do ventrículo que falhou e **falta depois**.
- **IC esquerda** → sangue se acumula no átrio esquerdo → veias pulmonares → capilar pulmonar → ele extravasa (edema pulmonar). Sintomas: **dispneia** (esforço, depois repouso), **ortopneia** (deita = sobe retorno venoso da circulação esplâncnica = piora congestão pulmonar), **dispneia paroxística noturna** (durante o sono, redistribuição lenta de volume + queda do tônus simpático), **estertores crepitantes** (alvéolos abrindo contra líquido), **tosse seca**, **cianose central** (hipoxemia por edema intersticial).
- **IC direita** → sangue se acumula no átrio direito → veia cava → sistêmico. Sintomas: **estase jugular** (pressão venosa central elevada), **hepatomegalia dolorosa** (fígado congesto, distende cápsula de Glisson), **ascite** (extravasamento na cavidade peritoneal), **edema MMII** (gravidade puxa o líquido), **nictúria** (deitar à noite reduz pressão venosa nas pernas → reabsorve edema → rim filtra mais à noite).
- No paciente do caso: tem **as duas** ao mesmo tempo (IC global) — congestão pulmonar (dispneia, ortopneia, DPN, estertores, cianose) + congestão sistêmica (estase jugular, ascite, edema MMII, nictúria, hepatomegalia, empachamento por congestão visceral). É o padrão típico da IC isquêmica avançada: começa pela esquerda, sobrecarrega o direito.
- Justifica perguntas 4 (IC esquerda × direita) e 5 (mecanismos) do PBL.
- Figuras: `slide-07.png` (estase jugular), `slide-08.png` (cianose + ascite), `slide-09.png` (Godet).

**2.4 — Forças de Starling no capilar e a formação do edema**
- **Atenção:** aqui a "lei de Starling" é outra coisa que não a do sarcômero da PARTE 1. Mesma pessoa, conceitos distintos. Esta é a equação de troca de fluido na parede capilar.
- **Equação simplificada:** fluxo = K × [(Pc − Pi) − σ(πp − πi)]. Quatro forças:
  - **Pc** (pressão hidrostática capilar) — empurra água para fora; sobe com pressão venosa elevada.
  - **πp** (pressão oncótica plasmática) — puxa água para dentro; cai em hipoalbuminemia.
  - **Pi** (pressão hidrostática intersticial) — geralmente baixa, próxima a zero.
  - **πi** (pressão oncótica intersticial) — também baixa.
- No paciente: pressão venosa central elevada (estase jugular) → Pc capilar sistêmico sobe → desequilíbrio favorece saída → edema MMII (gravidade soma na perna de pé). Mesmo mecanismo, esquerda: Pc capilar pulmonar sobe → transudato no interstício pulmonar → estertores e dispneia.
- Justifica pergunta 5a e 5b do PBL (por que IC eleva pressão venosa; como muda as forças).

**2.5 — Por que o sal preocupa mais que a água livre + cascata neuro-humoral**
- Compartimentos: líquido extracelular (LEC, ~1/3 da água corporal) tem **Na⁺ como cátion dominante**; intracelular (LIC, ~2/3) tem **K⁺ dominante**. Bomba Na⁺/K⁺-ATPase mantém esse gradiente queimando ATP.
- Água atravessa membranas livremente (osmose). Sódio, na prática, não — bombas Na⁺/K⁺ contrapõem a entrada pelos canais de vazamento, tornando a membrana **funcionalmente impermeável** ao Na⁺.
- Consequência: se você bebe **água livre**, ela se distribui em todos os compartimentos (1/3 LEC + 2/3 LIC) — só 1/3 fica fora das células. Se você ingere **sal** (NaCl), ele fica preso no LEC; para manter a osmolalidade, a água é puxada do LIC para o LEC, expandindo o volume extracelular **três vezes mais** que a água livre. Na IC, esse volume extra vai direto para o capilar congesto → edema.
- Justifica pergunta 5c do PBL (ingestão de sal vs água livre na ICC).
- **Cascata neuro-humoral:** débito cai → rim percebe → **SRAA** ativa (renina → angiotensina I → ECA → angiotensina II → vasoconstrição + sede + aldosterona → reabsorção Na⁺ + H₂O) + **simpático** ativa (taquicardia + vasoconstrição + inotropismo). A curto prazo, mantém PA. A longo prazo, **piora** a IC: pós-carga sobe (parede precisa de mais força), volume sobe (pré-carga sobe além do platô), miocárdio remodela patologicamente.
- Por isso o tratamento da IC inclui **bloquear** SRAA (IECA/BRA, espironolactona) e simpático (beta-bloqueador) — você desliga o feedback que iria matar o paciente. (Mencionar de passagem, sem entrar em farmacologia avançada.)

### PARTE 3 — A causa primária e o desfecho: aterosclerose → IAM → IC isquêmica (5 subtópicos, ~10–12 pp)

**3.1 — Por que HAS + dislipidemia geram aterosclerose**
- HAS: pressão alta lesa o endotélio, principalmente em pontos de turbulência (bifurcações). Endotélio lesado expõe matriz subendotelial → adesão plaquetária + recrutamento de monócitos.
- Dislipidemia (LDL alto, HDL baixo): LDL excede a capacidade do receptor hepático → atravessa o endotélio lesado → fica retido na íntima → sofre oxidação → macrófagos engolem virando **células espumosas** → formação da estria gordurosa.
- Estria evolui para placa: macrófagos morrem, deixam um núcleo lipídico necrótico; células musculares lisas migram da média e formam capa fibrosa. Placa estável vs placa vulnerável (capa fina, núcleo grande).
- HDL faz o caminho inverso (transporte reverso de colesterol) — por isso HDL baixo é fator de risco.
- Justifica pergunta 3 do PBL (HAS + dislipidemia → aterosclerose).
- Figura: figura externa de placa aterosclerótica (slide do caso não tem; descrita por prosa).

**3.2 — Da placa ao IAM com supra de ST**
- Gatilho: placa vulnerável **rompe** (pico de pressão, estresse mecânico, inflamação local). Núcleo lipídico exposto ao sangue → cascata de coagulação dispara → **trombo** oclui a luz coronariana.
- Consequência tecidual: miócitos a jusante perdem perfusão → glicólise anaeróbica → lactato sobe, ATP cai → bomba Na⁺/K⁺ para → célula incha → necrose em 20–40 min se não reperfundir.
- **Troponina** é proteína estrutural do sarcômero (troponina T e I são cardio-específicas). Necrose libera troponina no sangue. Pico em 4–24h, normaliza em 7–14 dias. Por isso troponina **alta em jan/2025** (IAM em curso) e **normal em jan/2026** (necrose antiga, célula já se foi, sem mais liberação).
- Por isso a troponina é o biomarcador padrão: cardio-específica (CK-MB é menos específica, troponina é melhor), sensível, com janela de detecção longa.
- Justifica pergunta 6 (troponina) + pergunta 3 (aterosclerose → IAM) do PBL.

**3.3 — ECG no IAM: supradesnivelamento de ST, onda Q, T invertida — corrente de lesão**
- Por que a alteração? Miócito normal tem PA com platô (fase 2) longo e potencial de repouso estável. Miócito isquêmico vaza K⁺ (canais ATP-sensíveis abrem com queda de ATP) → potencial de repouso menos negativo + platô encurtado.
- Diferença de potencial entre miocárdio sadio e isquêmico durante a diástole gera **corrente de lesão diastólica**: vetor do sadio (mais negativo) para o isquêmico (menos negativo). O ECG registra essa corrente como **desnivelamento basal**, que aparece como supradesnivelamento de ST nas derivações que olham para a região lesada.
- Onda T invertida (isquemia subepicárdica), supra de ST (lesão transmural), onda Q patológica (necrose estabelecida em 24–48h).
- ECG do paciente em jan/2025 (Figura 1 do caso): supra de ST sugerindo IAM em parede anterior (V1–V4, baseado no comparativo com ECG normal Figura 2).
- Justifica pergunta 8 do PBL (alterações do ECG no IAM e mecanismo).
- Figuras: `slide-06.png` (ECG IAM), `slide-13.png` (ECG normal × IAM comparativo), `slide-16.png` (versão alternativa do mesmo comparativo).

**3.4 — Classificação Stevenson (quente/frio × seco/úmido) + NYHA**
- Avaliação à beira do leito sem precisar de eco:
  - **Quente vs frio:** perfusão periférica adequada (quente) ou má perfusão (frio, com TEC > 3s, extremidades pálidas/cianóticas, sonolência).
  - **Seco vs úmido:** sem (seco) ou com (úmido) congestão — estertores, estase jugular, edema, B3.
- Quatro perfis: **A** (quente/seco — compensado), **B** (quente/úmido — congesto mas perfundindo), **C** (frio/úmido — congesto e mal perfundindo, pior prognóstico), **L** (frio/seco — baixo débito sem congestão, raro).
- Paciente do caso: TEC 5s + cianose periférica + sonolência sugerem **frio**; estase + ascite + edema + estertores + B3 = **úmido** → **perfil C** (frio/úmido). Pior prognóstico, indica internação + suporte inotrópico.
- **NYHA** (classe funcional pelo grau de dispneia): I (sem limitação), II (limitação leve, atividades habituais), III (limitação importante, atividades menores que habituais), IV (sintomas em repouso). Paciente do caso, com dispneia subindo escada + ortopneia + DPN → **NYHA III–IV** (provável IV pela ortopneia + DPN).
- Justifica pergunta 2 do PBL (tipo de IC, etiologia, perfil hemodinâmico, classe NYHA).

**3.5 — Gasometrias: alcalose respiratória no IAM × acidose metabólica + hipoxemia na IC descompensada**
- **Jan/2025 (IAM):** pH 7,48, pCO₂ 32, HCO₃⁻ 21, pO₂ 98 → **alcalose respiratória**. Por quê: dor + ansiedade + estresse simpático aceleram a respiração → eliminação rápida de CO₂ → ácido carbônico cai → pH sobe. Compensação metabólica ainda não montou (HCO₃⁻ levemente baixo, mas ainda dentro da faixa).
- **Jan/2026 (IC descompensada):** pH 7,30, pCO₂ 32, HCO₃⁻ 16, pO₂ 72 → **acidose metabólica + hipoxemia**. Por quê: má perfusão tecidual → glicólise anaeróbica → lactato sobe → consome HCO₃⁻ → cai bicarbonato → pH cai. Pulmão tenta compensar baixando pCO₂ (taquipneia compensatória — FR 16 já é resposta). Hipoxemia (pO₂ 72) reflete distúrbio V/Q por edema pulmonar intersticial e shunt.
- Padrão clássico: IAM agudo dispara alcalose respiratória; IC descompensada faz acidose metabólica (com ou sem componente respiratório de fadiga).
- Justifica pergunta 11 do PBL (distúrbios das duas gasometrias).

**3.6 — Autonomia × paternalismo e MCP — quando o paciente recusa o exame**
- Pergunta 12 do PBL e competências 8–10 do enunciado.
- **Princípio da autonomia:** todo paciente capaz tem direito de aceitar ou recusar tratamento, mesmo que a recusa coloque a vida em risco. Está no CFM, no Código de Ética Médica (art. 31, 22), e no Estatuto da Pessoa.
- **Medicina Centrada na Paciente (MCP):** quatro tarefas — explorar a doença E a experiência da doença (o que o paciente entende, sente, teme, espera); compreender a pessoa inteira; encontrar um terreno comum sobre a conduta; reforçar a relação.
- No caso: paciente recusou cineangio por medo (vizinho morreu). Recusa válida em princípio. A equipe **não passou por cima** — fez uma "conversa estruturada" + apoio da esposa (rede social) → paciente concordou. Isso é MCP impecável: validar o medo, dar informação, envolver a família, **não impor**.
- Limite da autonomia: a única exceção é situação de emergência com risco iminente de morte e paciente sem capacidade de decisão (rebaixamento, inconsciência). Nesses casos, o médico age presumindo o consentimento. Mas o caso não era essa situação — paciente lúcido, com tempo para conversa.
- **Paternalismo** = decidir pelo paciente "pelo bem dele". Postura dominante no século XX, hoje considerada ética inadequada para o paciente lúcido. A medicina contemporânea exige decisão compartilhada.
- Justifica pergunta 12 do PBL + competências 8–10.

### Conclusão integradora (4 camadas)

1. **Princípio unificador:** o coração é uma bomba; quando a bomba perde miócito (IAM), a Lei de Frank-Starling deixa de comprar mais débito ao encher mais — a curva pisa o platô. O excesso de volume escapa para trás: à frente para o pulmão (edema, dispneia), à direita para o sistêmico (estase, ascite, edema MMII). As forças de Starling do capilar **traduzem** esse excesso em líquido extravascular.
2. **Mecanismo nuclear:** IAM → necrose de parede anterior → contratilidade cai → curva Frank-Starling desce → SRAA + simpático ativam para compensar → curto prazo mantém PA, longo prazo remodela patologicamente → câmara dilata, parede hipertrofia, B3 aparece, congestão se instala.
3. **Clínica retomada:** paciente do caso é o desfecho dessa cascata em um ano: jan/2025 IAM com supra; jan/2026 IC isquêmica com FE 40%, perfil C (frio/úmido), NYHA III–IV. Bilateral (esquerda + direita), refletindo IC global avançada.
4. **Projeção:** para sair do platô, o tratamento atual desliga os feedbacks malignos (IECA + beta-bloqueador + espironolactona) e adiciona inotrópicos quando necessário. Em estudos futuros (MSP4212 e sequência), entram os dispositivos (CDI, ressincronização) e o transplante.

### Resumindo (1–2 páginas)

8–12 seções ordenadas por relevância clínica: Frank-Starling do coração · Forças de Starling capilar · Ciclo cardíaco + bulhas · Pré-carga/pós-carga/contratilidade · IC esquerda vs direita · Remodelamento e cardiomegalia · ECG no IAM · Troponina · Stevenson + NYHA · Gasometrias · Autonomia/MCP.

## Seção C — Termos-nota obrigatórios (alvo 7)

1. **pré-carga** — estiramento da fibra ventricular antes da contração, aproximado pelo volume diastólico final ou pressão diastólica final do VE.
2. **pós-carga** — resistência que o ventrículo precisa vencer para abrir a válvula semilunar; depende da pressão arterial sistêmica e do raio da câmara.
3. **contratilidade** — força gerada pelo miocárdio para uma dada pré-carga, independente do estiramento; depende de Ca²⁺ disponível e estado dos miócitos.
4. **débito cardíaco** — volume de sangue ejetado pelo ventrículo por unidade de tempo, igual a frequência cardíaca multiplicada pelo volume sistólico.
5. **complacência** — capacidade do ventrículo de aceitar volume durante a diástole sem grande aumento de pressão; cai na hipertrofia e fibrose.
6. **remodelamento ventricular** — conjunto de mudanças estruturais (hipertrofia, dilatação, fibrose) que o ventrículo sofre em resposta a sobrecarga crônica.
7. **ativação neuro-humoral** — resposta integrada do SRAA + sistema simpático à queda do débito, compensatória a curto prazo e maladaptativa a longo prazo.
8. **fração de ejeção** — fração do volume diastólico final que o ventrículo ejeta na sístole; normal 55–70%, paciente do caso 40% (ICFEr).

## Seção D — Pontos de quebra do raciocínio (insumo para boxes)

**PARTE 1:**
- D1.1 — Aluno confunde Frank-Starling do coração com forças de Starling do capilar. **CONFUSÃO CENTRAL**, alertada no próprio enunciado do PBL (pergunta 3). → `#atencao-box` na seção 1.3.
- D1.2 — Aluno acha que B3 sempre é patológica. Em jovens com parede elástica e alto fluxo pode ser fisiológica; em adulto com IC é alarme. → prosa inline em 1.2.
- D1.3 — Aluno pensa que a onda T do ECG é a contração ventricular. T é repolarização, contração é QRS + ST. → prosa inline em 1.4.

**PARTE 2:**
- D2.1 — Aluno confunde **pré-carga** com **pós-carga**. Truque: pré- vem antes da contração (= enchimento), pós- vem depois (= resistência à ejeção). → prosa inline em 2.1.
- D2.2 — Aluno acha que IC esquerda só dá sintoma pulmonar e IC direita só sistêmico. Na realidade, IC esquerda crônica sobrecarrega o direito → quase sempre vira IC global. → prosa inline em 2.3.
- D2.3 — Aluno acha que beber muita água é tão ruim quanto comer sal. Não é: água livre se distribui em todo o corpo, só 1/3 fica no LEC; sal fica preso no LEC e arrasta água do LIC. → `#confusao-prevista` em 2.5.
- D2.4 — Aluno acha que ortopneia e DPN são a mesma coisa. Ortopneia = ao deitar; DPN = no meio do sono, paciente acorda. Mecanismos parcialmente sobrepostos mas distintos. → prosa inline em 2.3.

**PARTE 3:**
- D3.1 — Aluno acha que troponina normal em jan/2026 = "não tem doença cardíaca". Troponina mede **necrose ativa**; IC sem isquemia atual pode ter troponina normal mesmo com FE 40%. → prosa inline em 3.2.
- D3.2 — Aluno acha que paciente com pH 7,48 (jan/2025) tinha distúrbio mais grave que pH 7,30 (jan/2026). Na verdade, a alcalose respiratória do IAM é leve e transitória; a acidose metabólica de IC descompensada reflete hipoperfusão tecidual, é mais grave. → prosa inline em 3.5.
- D3.3 — Aluno confunde perfil hemodinâmico Stevenson com classe NYHA. Stevenson = à beira do leito agora (quente/frio + seco/úmido); NYHA = capacidade funcional no dia a dia. → prosa inline em 3.4.
- D3.4 — Aluno acha que recusa do paciente "obriga" o médico a aceitar passivamente. A MCP exige **explorar o motivo da recusa** e oferecer informação adicional + apoio social — sem violar autonomia. → tratado em 3.6 + retomado no relatório.

## Cobertura E2 (planejamento de 30 questões)

- **Consolidação (Q01–Q10):** sarcômero/Ca²⁺/troponina, ciclo cardíaco, bulhas, Frank-Starling, pré/pós-carga, contratilidade, débito, FE, NSA/NAV.
- **Integração (Q11–Q25):** todas com `Qxx conecta [A]+[B]` no `arquivos-trabalho/integracao-mapa-insuficiencia-cardiaca.md`. Ex.: Q14 = forças capilar + SRAA; Q19 = ECG IAM + corrente de lesão; Q22 = remodelamento + curva Frank-Starling; Q24 = Stevenson + gasometria.
- **Aplicação (Q26–Q30):** vinhetas clínicas estilo USMLE com paridade ratio ≤ 1.25 em **todas as 30** (canônico estendido 2026-05-29). Ordem invertida obrigatória.

## Cobertura E3 (5 discursivas)

- **D1 (≤100 pal):** "Explique o aparecimento da B3 no paciente, ligando ao sarcômero e à complacência ventricular." Cobre perg. 7 do PBL.
- **D2 (≤100):** "Compare as duas gasometrias e justifique a passagem alcalose→acidose com mecanismo." Cobre perg. 11.
- **D3 (≤100):** "Justifique o edema MMII pelas forças de Starling do capilar, dado o aumento da pressão venosa central." Cobre perg. 5a–5b.
- **D4 (≤100):** "Justifique o perfil hemodinâmico C (frio/úmido) e a classe NYHA III–IV pelos achados de exame físico do paciente." Cobre perg. 2.
- **D5 (≤130):** "Discuta autonomia × paternalismo na recusa inicial da cineangiocoronariografia, usando a abordagem da MCP." Cobre perg. 12 + competências 8–10.
