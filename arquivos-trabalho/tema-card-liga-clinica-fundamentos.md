# Tema Card — Fundamentos do bom clínico (Liga de Clínica Médica FMUSP 2026, PDF 2/2)

## Seção A — Identidade

- **Tema:** Fundamentos do bom clínico — Sir William Osler (Arai), Uso racional do laboratório (Arnaldo), Medicina Centrada no Paciente e Bioética (Lúcia). Três palestras independentes do curso introdutório da Liga, costuradas aqui pelo eixo "como pensar, decidir e conduzir" — a moldura cognitiva e ética que envolve o raciocínio do PDF 1.
- **Disciplina:** Liga de Clínica Médica — Curso Introdutório 2026.
- **Slug:** `liga-clinica-fundamentos`.
- **Profundidade:** **PADRÃO** (10 Cons · 15 Int · 5 Apl). Conteúdo menos denso factualmente que o PDF 1, mas mais denso em conceitos e julgamento; integração natural entre as 3 PARTES pelo eixo postura/decisão/conduta.
- **Tamanho-alvo:** piso 14, **teto 24 páginas**. Distribuição: PARTE I ≈ 5–7 pp · PARTE II ≈ 7–9 pp · PARTE III ≈ 7–9 pp · Intro + Conclusão + Resumindo ≈ 2–3 pp.
- **Onde estudar:** Bryan Charles G. *Sir William Osler: An Encyclopedia*; Harrison cap. "Approach to the Patient" + "Diagnostic Imaging in Medicine"; Stewart MA. *Patient-Centered Medicine — Transforming the Clinical Method* (3ª ed.); Beauchamp TL, Childress JF. *Principles of Biomedical Ethics* (8ª ed.); Código de Ética Médica do CFM.
- **Recorte slide × tema:** Arai (16 slides) e Lúcia (20 slides) — fontes diretas. Arnaldo (.ppt, não conversível no ambiente atual) — conteúdo redigido a partir de bibliografia canônica de uso racional do laboratório (Harrison cap. específico + UpToDate). O Tema Card declara explicitamente essa fonte alternativa para transparência.
- **Calibração:** sem banco filtrado (Liga não está no `banco/aulas_uc*.yml`). Calibração feita pelo conteúdo dos 2 slides disponíveis + bibliografia padrão sobre laboratório clínico e bioética.
- **Pasta de trabalho:** `typst-build/` raiz. Saída: `resumos-gerados/LIGA-CLINICA-FUNDAMENTOS.pdf`.

## Seção B — Estrutura da E1

### Intro-box

O PDF 1 desta liga tratou de *como pensar diante de um sintoma*. Este PDF 2 trata da **moldura** que envolve esse pensamento — o **como ser** do clínico (a postura ensinada por Sir William Osler), o **como decidir** sobre o que pedir (uso racional do laboratório), e o **como conduzir** a relação com o paciente (Medicina Centrada no Paciente + os quatro princípios da bioética). As três PARTES respondem a perguntas que o raciocínio diagnóstico do PDF 1 não responde sozinho: *que tipo de médico você quer ser?*, *como evitar excesso de exames?*, *como decidir junto com um paciente que recusa o que você acha melhor?*

### PARTE I — Osler e a postura do clínico (3 subtópicos, ~5–7 pp)

**1.1 — Quem foi Osler e por que ele importa hoje** (slides 1–6 do Arai)
- Sir William Osler (1849–1919): canadense, fundador da medicina interna moderna, autor de *The Principles and Practice of Medicine* (1892, livro-texto que dominou a formação médica por 4 décadas).
- Liderou a reformulação da residência médica como conhecemos hoje (Johns Hopkins, Hospital de Toronto), instituindo o modelo de aprendizado à beira do leito (*bedside teaching*) em substituição às aulas teóricas isoladas.
- Por que importa: o aluno médico do século XXI ainda treina dentro do modelo educacional que Osler estruturou — residência médica longa, formação em hospital escola, ênfase em anamnese e exame físico antes de exames complementares.

**1.2 — Bedside teaching: "o paciente é o livro"** (slides 7–11 do Arai)
- Osler insistia que o aprendizado real da medicina ocorre à beira do leito do paciente, não na sala de aula. A frase mais citada: "*To study the phenomena of disease without books is to sail an uncharted sea, while to study books without patients is not to go to sea at all*" — estudar livros sem pacientes é não ir ao mar de jeito nenhum.
- Implicação prática contemporânea: o aluno que passa o dia em biblioteca e pula visita de enfermaria está fazendo o oposto do que Osler ensinou. A anamnese repetida (mesmo em paciente já conhecido), o exame físico cuidadoso (mesmo quando "vai pedir exame mesmo"), a conversa com a família — tudo isso é o "livro paciente" sendo lido.

**1.3 — Máximas operacionais: escuta, humildade, residência** (slides 12–16 do Arai)
- "*Listen to the patient — he is telling you the diagnosis*" (escute o paciente; ele está te dizendo o diagnóstico). Tradução prática: a anamnese bem feita resolve 70–80% dos diagnósticos clínicos, e isso ainda vale na era da tomografia.
- "*The good physician treats the disease; the great physician treats the patient who has the disease*" (o bom médico trata a doença; o ótimo médico trata o paciente que tem a doença). Antecedente direto da Medicina Centrada no Paciente da PARTE III.
- "*Equanimitas*" — equanimidade, palavra que Osler escolheu para definir a postura ideal do médico: firme sob pressão, sem agitação, sem indiferença, capaz de tomar decisão difícil com calma. É o oposto da pressa ansiosa e da apatia distante.
- Residência médica longa: para Osler, era condição estrutural — só a vivência repetida (centenas de pacientes vistos por residente em condições controladas) consolida os scripts de doença que o PDF 1 tratou.

### PARTE II — Uso racional do laboratório (4 subtópicos, ~7–9 pp)

**2.1 — Probabilidade pré-teste e a pergunta-mãe** (redigido a partir de Harrison cap. Approach to Patient + UpToDate)
- A pergunta antes de qualquer exame: *qual a probabilidade pré-teste da hipótese que esse exame vai testar?* Probabilidade pré-teste depende de epidemiologia + clínica (já discutido no PDF 1 PARTE I). Exame em paciente com probabilidade muito baixa gera muito falso-positivo; exame em paciente com probabilidade muito alta gera muito falso-negativo (e atrasa conduta).
- Regra prática: o exame "pesa" mais quando a probabilidade pré-teste está na zona intermediária (~30–70%) — é aí que o resultado pode mudar conduta.

**2.2 — Sensibilidade, especificidade e likelihood ratio na prática**
- *Sensibilidade* = proporção de pacientes com a doença em que o teste dá positivo. Teste sensível, *quando negativo*, descarta bem (mnemônico SnNout: Sensitive, Negative, rule out).
- *Especificidade* = proporção de pacientes sem a doença em que o teste dá negativo. Teste específico, *quando positivo*, confirma bem (mnemônico SpPin: Specific, Positive, rule in).
- *Likelihood ratio positivo* (LR+) = sensibilidade ÷ (1 − especificidade). Quanto o achado positivo aumenta a probabilidade pós-teste.
- *Likelihood ratio negativo* (LR−) = (1 − sensibilidade) ÷ especificidade. Quanto o achado negativo reduz a probabilidade pós-teste.
- Regra de bolso (recuperada da PARTE II do PDF 1): LR<0,1 quase exclui; LR>10 quase confirma; LR≈1 não muda nada.

**2.3 — Quando pedir, quando NÃO pedir**
- Pedir quando: (a) probabilidade pré-teste está na zona intermediária; (b) o resultado vai mudar conduta (princípio "*will it change management?*"); (c) o exame tem LR razoável para a pergunta clínica.
- *Não* pedir quando: (a) probabilidade pré-teste muito baixa em paciente sem fator de risco — risco de cascata de falsos-positivos; (b) probabilidade pré-teste já muito alta — confirme com exame que aumente certeza, não com painel exploratório; (c) o resultado não vai mudar conduta (ex.: idoso terminal com múltiplas comorbidades — TC abdominal "para investigar emagrecimento" provavelmente não modifica cuidados); (d) sob pressão familiar ou ansiedade própria — "pelo seguro" gera dano.

**2.4 — O paradoxo dos exames de rotina e as cascatas iatrogênicas**
- Exame "de rotina" pedido em paciente assintomático sem fator de risco específico tem probabilidade pré-teste de qualquer achado anormal próximo de zero. Mesmo com especificidade alta, valor preditivo positivo despenca em populações de baixa prevalência (teorema de Bayes na prática).
- *Cascata iatrogênica*: achado incidental (nódulo pulmonar de 4 mm "para acompanhar", microcalcificação mamária inespecífica) leva a novos exames, novas dúvidas, ansiedade, biópsias, complicações. Cada exame inicial deve ser pesado pela cadeia que ele pode iniciar.
- Recomendações mais robustas: campanha *Choosing Wisely* (sociedades de especialidade definindo "5 coisas que provavelmente não deveríamos fazer" em cada área), diretrizes baseadas em evidência, conhecimento ativo do médico sobre overuse.

### PARTE III — Medicina Centrada no Paciente e Bioética (3 subtópicos, ~7–9 pp)

**3.1 — As quatro tarefas da MCP** (slides 1–7 da Lúcia)
- O modelo de Stewart e colegas (3ª edição, *Patient-Centered Medicine*): a relação clínica ideal é estruturada em quatro tarefas paralelas, não em sequência fixa.
  - *Explorar a doença E a experiência da doença.* O clínico tradicional cobre só a doença (sintomas, exame, exames); a MCP cobre também a experiência — o que o paciente entende sobre o que está acontecendo (cognições), o que ele sente (emoções), o que ele teme (medos), o que ele espera (expectativas de conduta). FIFE em inglês: Feelings, Ideas, Function, Expectations.
  - *Compreender a pessoa inteira.* Paciente não é só corpo doente — é trabalho, família, cultura, espiritualidade, condições materiais. A síndrome nefrótica em um pintor autônomo de 55 anos tem implicações diferentes da síndrome nefrótica em um aposentado.
  - *Encontrar terreno comum sobre a conduta.* Decisão compartilhada (*shared decision-making*) — o médico apresenta opções com riscos/benefícios; o paciente decide à luz de seus valores; juntos definem o caminho. Não é "o médico oferece menu" nem "o paciente decide sozinho".
  - *Reforçar a relação clínico-paciente.* Cada consulta é construção (ou desgaste) da relação que vai sustentar adesão, retorno, confiança em decisões difíceis futuras.

**3.2 — Os quatro princípios da bioética** (slides 8–13 da Lúcia + Beauchamp & Childress)
- *Autonomia*: paciente capaz tem direito de aceitar ou recusar qualquer tratamento, mesmo que a recusa coloque a vida em risco. Operacionalizada pelo *consentimento informado* (paciente entende a informação relevante, está livre de coerção, é capaz de decidir).
- *Beneficência*: obrigação ativa de fazer o bem ao paciente — não apenas evitar dano, mas buscar benefício.
- *Não-maleficência*: *primum non nocere*. Obrigação de evitar dano. Vale especialmente em situações em que beneficência e não-maleficência conflitam (ex.: cirurgia agressiva com risco de mortalidade pode ser beneficente para sobrevida e maleficente para qualidade de vida).
- *Justiça*: distribuição equitativa de recursos limitados em saúde. Aparece quando há escassez (leitos de UTI em pandemia, transplantes, terapias caras) e quando há viés de acesso (paciente do SUS vs paciente da medicina suplementar).

**3.3 — O caso da Lúcia: autonomia em ação** (slides 14–20 da Lúcia)
- Vinheta narrativa: paciente idoso, polimórbido, com indicação de procedimento (cineangiocoronariografia, no caso descrito) — recusa por medo (vizinho morreu de complicação parecida). A equipe **não passou por cima** da recusa; fez uma "conversa estruturada": explorou os medos (FIFE), apresentou riscos reais com números, envolveu a esposa como rede de apoio, ofereceu segunda consulta para decisão. Paciente concordou após a conversa.
- O que isso ensina mecanisticamente sobre a MCP em ato:
  - *Validar o medo* (não desmerecer com "isso é raro, fica tranquilo"). O medo é a experiência da doença e precisa ser legitimado.
  - *Dar informação calibrada* — números concretos sobre risco real (não generalidades).
  - *Envolver rede de apoio* quando o paciente aceita. Família, amigo de confiança, espiritualidade — variáveis que pesam na decisão.
  - *Não impor*. Mesmo após explicação completa, recusa segue sendo respeitada — só a coação é proibida, não a tentativa de persuasão argumentada.
- Limite da autonomia: emergência com risco iminente de morte e paciente sem capacidade de decisão (rebaixamento, inconsciência, intoxicação aguda). Nesse cenário, o médico age presumindo o consentimento — é a única situação em que paternalismo é eticamente aceitável.

**3.4 — Paternalismo × decisão compartilhada**
- *Paternalismo* = médico decide pelo paciente "pelo bem dele". Foi o modelo dominante no século XX (médico era figura de autoridade absoluta). Hoje, considerado eticamente inadequado para paciente lúcido — viola autonomia.
- *Decisão compartilhada* é o modelo contemporâneo: médico tem expertise técnica, paciente tem expertise sobre os próprios valores, juntos chegam à melhor decisão para *aquele paciente específico*. Exemplo: dois pacientes com mesma síndrome nefrótica e mesma indicação de imunossupressão podem decidir diferente (um aceita os efeitos colaterais para preservar função renal; outro prefere conduta conservadora porque o risco infeccioso na profissão dele é inaceitável).
- O *paternalismo bem-intencionado* ("não vou contar que é câncer porque ele vai sofrer") foi extensivamente discutido e hoje é rejeitado em quase todos os contextos — a omissão de informação relevante viola autonomia e tende a deteriorar a relação quando o paciente descobre.

### Conclusão integradora (4 camadas)

1. **Princípio unificador:** os três temas — postura do clínico (Osler), uso racional do laboratório, MCP e bioética — convergem em uma ideia: o médico não é técnico isolado aplicando algoritmo; é profissional que escuta, calibra, decide com (não por) o paciente. A excelência clínica é tanto cognitiva quanto relacional.
2. **Mecanismo nuclear:** os quatro princípios da bioética + as quatro tarefas da MCP fornecem a estrutura operacional para a conduta clínica em situações de conflito (paciente recusa, família discorda, recurso escasso, fim de vida). Não são princípios abstratos — são ferramentas de raciocínio.
3. **Clínica retomada:** o caso da Lúcia (idoso recusando cineangio) é o exemplar canônico — autonomia validada, FIFE aplicado, rede de apoio convocada, decisão compartilhada construída. Reproduzir esse gesto na prática é o conteúdo prático da PARTE III.
4. **Projeção:** os dois PDFs desta liga juntos cobrem o curso introdutório completo. O PDF 1 dá o raciocínio diagnóstico ante 3 sintomas; este PDF 2 dá a moldura cognitiva e ética. Aplicar os dois junto é exercer clínica madura.

### Resumindo (1–2 páginas)

10 seções: Quem foi Osler · Bedside teaching · Máximas operacionais (escuta, equanimitas, residência) · Probabilidade pré-teste · Sensibilidade/especificidade/LR · Quando pedir/não pedir · Cascata iatrogênica · 4 tarefas da MCP · 4 princípios da bioética · Caso da Lúcia + paternalismo × decisão compartilhada.

## Seção C — Termos-nota obrigatórios (alvo 6)

1. **bedside teaching** — modelo educacional centrado no aprendizado à beira do leito do paciente, instituído por Osler na reforma da residência médica norte-americana no final do século XIX.
2. **equanimitas** — termo que Osler escolheu para descrever a postura ideal do médico: firmeza sob pressão sem agitação nem indiferença, capacidade de decisão calma em situação difícil.
3. **valor preditivo positivo (VPP)** — probabilidade de que um teste positivo corresponda a um paciente realmente doente; depende fortemente da prevalência da doença na população testada.
4. **likelihood ratio (LR)** — razão de probabilidades; quanto um achado (positivo ou negativo) move a probabilidade pós-teste em relação à pré-teste; LR<0,1 quase exclui, LR>10 quase confirma.
5. **FIFE** — acrônimo das quatro dimensões da experiência da doença exploradas na MCP: Feelings, Ideas, Function, Expectations (sentimentos, ideias, função, expectativas).
6. **consentimento informado** — operacionalização do princípio da autonomia; paciente deve ter informação relevante, estar livre de coerção e ser capaz de decidir para que sua decisão seja considerada autônoma.

## Seção D — Pontos de quebra do raciocínio (insumo para boxes)

**PARTE I:**
- D1.1 — Aluno acha que bedside teaching é "ortodoxia antiga sem valor hoje". Falso — anamnese e exame físico continuam sendo as ferramentas que resolvem a maioria dos diagnósticos clínicos. → prosa inline em 1.2.
- D1.2 — Aluno acha que "escutar o paciente" é virtude sentimental, não técnica. Não — escutar é a técnica diagnóstica mais alta-rendimento da medicina interna. → prosa inline em 1.3.

**PARTE II:**
- D2.1 — Aluno acha que exame "extra" não pode fazer mal. Pode — cascata iatrogênica, falsos-positivos, ansiedade do paciente, complicações de exames invasivos derivados. → `#atencao-box` central da PARTE II (em 2.4).
- D2.2 — Aluno confunde sensibilidade com VPP. Sensibilidade é propriedade do teste (fixa); VPP depende da prevalência (varia). Em população de baixa prevalência, VPP despenca mesmo com teste muito sensível. → `#confusao-prevista` em 2.2.
- D2.3 — Aluno acha que LR é "estatística complexa irrelevante na prática". Não — LR é o vocabulário que traduz exame em mudança de probabilidade, e mesmo a regra de bolso sem calculadora ajuda. → prosa inline em 2.2.

**PARTE III:**
- D3.1 — Aluno acha que autonomia é "fazer o que o paciente quer". Não — autonomia exige *capacidade* de decisão + informação adequada + liberdade de coerção. Paciente confuso, intoxicado ou com depressão grave pode não ter autonomia para decidir naquele momento. → prosa inline em 3.2.
- D3.2 — Aluno trata MCP como "cordialidade" ou "marketing médico". Não — é estrutura operacional de quatro tarefas, treinável e mensurável (escalas como o Patient-Centred Communication Coding System). → prosa inline em 3.1.
- D3.3 — Aluno acha que paternalismo é simplesmente "ruim". Em emergência sem capacidade de decisão (paciente em coma), agir presumindo consentimento é a única conduta ética possível — não é paternalismo abusivo, é necessidade. → `#confusao-prevista` em 3.4.
- D3.4 — Aluno acha que "respeitar autonomia" significa não tentar convencer o paciente. Tentar convencer com argumento e dado é parte do trabalho clínico; o que viola autonomia é coação ou ocultação de informação. → `#atencao-box` central da PARTE III (em 3.3).

## Cobertura E2 (planejamento)

- **Consolidação Q01–Q10 (10):** Osler + bedside teaching + equanimitas (2), distinção sensibilidade/especificidade/VPP (3), princípios da bioética (2), tarefas da MCP (2), distinção paternalismo × decisão compartilhada (1).
- **Integração Q11–Q25 (15):** com `integracao-mapa-liga-clinica-fundamentos.md` declarando A+B em cada. Cruzamentos: epidemiologia da prevalência × VPP, máximas Oslerianas × práticas modernas de anamnese, autonomia × emergência sem capacidade, MCP × adesão terapêutica, sensibilidade × prevalência, cascata iatrogênica × princípio de não-maleficência, etc.
- **Aplicação Q26–Q30 (5):** vinhetas estilo USMLE com paridade ratio ≤ 1.25 em **todas as 30** (canônico 2026-05-29). Cenários: paciente recusa tratamento, escolha de exame em paciente de baixa probabilidade pré-teste, decisão compartilhada vs paternalismo, princípio da justiça em escassez, MCP aplicada a paciente difícil.

## Cobertura E3 (5 discursivas)

- **D1 (≤100):** "Explique por que escutar o paciente é a ferramenta diagnóstica de maior rendimento na medicina interna, ancorando-se em uma das máximas Oslerianas."
- **D2 (≤100):** "Diferencie sensibilidade, especificidade e valor preditivo positivo, e explique por que pedir exame de rotina em paciente assintomático tem baixo VPP mesmo com testes muito específicos."
- **D3 (≤100):** "Explique o conceito de cascata iatrogênica e dê um exemplo clínico de como o pedido de um exame incidental pode gerar dano ao paciente."
- **D4 (≤100):** "Diferencie autonomia, beneficência, não-maleficência e justiça como princípios da bioética, e dê um exemplo clínico em que dois desses princípios podem entrar em conflito."
- **D5 (≤130):** "Discuta o caso de um paciente idoso polimórbido que recusa um procedimento diagnóstico por medo, integrando as quatro tarefas da MCP e os princípios da bioética para justificar a conduta correta."
