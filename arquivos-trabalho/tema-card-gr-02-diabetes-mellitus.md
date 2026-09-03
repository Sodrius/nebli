# Tema Card — Grand Round 2 · Diabetes mellitus

## Seção A — Escopo

- **Tema:** Diabetes mellitus — do defeito de insulina às complicações de órgão-alvo
- **Slug:** `gr-02-diabetes-mellitus` (entrada `gr-02` em `banco/aulas_uc03.yml`)
- **Disciplina:** UC03 · Grand Round (integra Bioquímica/Biologia Molecular, Patologia, Imunologia e Radiologia)
- **Onde estudar:** Robbins & Cotran, *Patologia — Bases Patológicas das Doenças*, capítulo do Sistema Endócrino (§ Diabetes mellitus) · Lehninger, *Princípios de Bioquímica*, capítulo de Regulação Hormonal e Integração Metabólica · Brant & Helms, *Fundamentos de Radiologia*, capítulos de tórax cardiovascular e musculoesquelético
- **Alvo de páginas E1:** piso 2, **teto 22** — alvo real 18–21
- **`profundidade: fundo`** (Davi pediu "bem abrangente, pra aprofundarmos bem")
- **Distribuição E2:** PROFUNDO → 8 Consolidação · 17 Integração · 5 Aplicação

### Recorte slide × tema

O slide cobre **duas fontes**: o deck da aula (43 telas — definição/classificação, DM1 como jejum permanente, DM2 como resistência + falência, AGEs, complicações oculares/renais/pé, e um bloco radiológico de 12 telas) e o **caso clínico** da Dra. Sharon Admoni (homem de 26 anos, poliúria/polidipsia/perda de 3 kg, glicemia 397, HbA1c 8,8%, peptídeo C 1,32, anti-GAD65 1082, e o seguimento com insulina basal-bolus + monitorização contínua até um perfil com 97% de tempo no alvo).

**Recorte declarado:** o tema pedido é o Grand Round inteiro. Diferente de um resumo de aula única, aqui a integração multiárea **é** o conteúdo — não é vazamento de outra aula. O que fica de fora mesmo assim: física de formação da imagem (ultrassom, TC, RM) em detalhe de aula-ferramenta; farmacologia de antidiabéticos além do mecanismo que o slide cita; e o manejo terapêutico de ciclo clínico (protocolo de cetoacidose, ajuste fino de contagem de carboidratos). O caso clínico entra como **âncora**, não como aula de endocrinologia prática.

### Divergência canônica declarada

`referencias-externas/uc03/CALIBRACAO.md` § Fronteiras, item 6, diz "Grand Round não vira resumo NEBLI". Davi pediu explicitamente este resumo. A regra vale como default; o pedido explícito vence. Anotado no `banco/aulas_uc03.yml` e no `MEMORY.md` § Histórico.

### Teto histórico × degrau NEBLI (calibração UC03)

Levantamento de 19 subquestões etiquetadas `GR` (2018–2025) + 36 subquestões com conteúdo de diabetes/aterosclerose no acervo de 30 provas.

**O que a casa cobra num Grand Round** (padrão estável 2018→2025):
1. **Mecanismo único que explica achados em múltiplos órgãos** — "explique o principal mecanismo fisiopatológico que pode explicar todas essas alterações" (2024 P1, e a resposta esperada é a cadeia glicação → Schiff → Amadori → AGE, com o destino em colágeno, LDL e hemoglobina).
2. **Comparar dois cenários pelo mecanismo, apontando semelhança E diferença** — osteomielite × pneumonia pelo mesmo *S. aureus* (2024 P2); trombose por estase/hipercoagulabilidade × trombose por lesão endotelial/turbulência (2025 P4); sarampo × influenza (2025 P3).
3. **Correlacionar achado patológico + imagem + laboratório no mesmo paciente** (2019 P3, 2018 P4).
4. **Ligar estratégia terapêutica ao mecanismo fisiopatológico** (2024 P4 — antiagregante, trombolítico e stent explicados pela ativação endotelial).
5. **Explicar por que a resposta imune do caso produz o quadro observado** (2018 P3 ×3, 2019 P1/P2).
   Verbos: *explique · aponte semelhanças e diferenças · correlacione · compare do ponto de vista de mecanismos · considerando seus conhecimentos de*. Nunca "defina".

**Teto histórico desta aula:** a cadeia da glicação até os AGEs, nomeada por etapas, com os destinos protéicos (colágeno → cicatrização; LDL → aterosclerose; hemoglobina → HbA1c; albumina → frutosamina); a diferença DM1 × DM2 em mecanismo, clínica e forma de descompensação; necrose gangrenosa do pé como isquemia + irreversibilidade por permeabilidade de membrana; tríade de Virchow aplicada ao diabético; declaração de óbito com diabetes como causa básica.

**A E1 vai um degrau acima em:** (a) *por que* a hiperglicemia lesa **justamente** retina, glomérulo, nervo e endotélio — a captação de glicose GLUT-independente de insulina, que impede essas células de fecharem a porta; (b) as **quatro rotas** da hiperglicemia (polióis, hexosamina, PKC, AGE/RAGE) convergindo em estresse oxidativo; (c) o eixo **RAGE → NF-κB** como o que transforma dano químico em dano auto-perpetuado; (d) a leitura **quantitativa** dos exames do caso — por que peptídeo C separa DM1 de DM2 e por que frutosamina e HbA1c medem janelas de tempo diferentes; (e) por que o rim **cresce** no início da nefropatia e **encolhe** no fim, e como isso aparece na ultrassonografia.

### Prioridades desta corrida (do § Diário de revisões)

1. **Economia de palavra (F10, peso alto, 2026-08-31).** Alvo 450–550 palavras por subtópico. `fundo` sobe conteúdo, não verbosidade. Caçar: moldura antes do conteúdo, legenda que reconta o corpo, achado recontado, conclusão que reconta, duas frases onde cabe uma.
2. **Figura obrigatória mesmo quando o tema é "conceitual" (peso alto, 2026-05-29).** Aqui há slide farto — sem desculpa. Mínimo 3 por PARTE, largura deliberada caso a caso.

---

## Seção B — Esqueleto das 3 PARTES

### PARTE I — O sinal que falta: por que a glicose sobe (4 subtópicos)

| # | Subtópico | Figuras planejadas |
|---|---|---|
| 1.1 | O que a insulina manda a célula fazer | `slide-14` (eixo incretina GLP-1/CCK) — lateral 42% |
| 1.2 | Tipo 1: a ilhota destruída e o corpo em jejum permanente | `slide-12` (saudável × tipo 1 × tipo 2) — 72% |
| 1.3 | Tipo 2: resistir ao sinal antes de perder a fonte | `slide-09` (lipotoxicidade muscular) 62% + `slide-11` (defeitos multiórgão) 68% |
| 1.4 | Da glicose alta ao sintoma: diurese osmótica, catabolismo e as duas descompensações | `slide-10` (história natural DM2) 70% |

### PARTE II — Do açúcar ao dano: glicação, AGEs e as rotas que perpetuam (4 subtópicos)

| # | Subtópico | Figuras planejadas |
|---|---|---|
| 2.1 | Glicação não-enzimática: Schiff → Amadori → AGE | `slide-15` (química da glicação, reversível→fixo) — 76% **obrigatória** (cadeia multi-passo) |
| 2.2 | HbA1c e frutosamina: dois relógios, duas janelas | — (cálculo em prosa) |
| 2.3 | O que o AGE faz nas proteínas de vida longa | `slide-17` (espessamento da membrana basal glomerular) — 60% |
| 2.4 | RAGE e as outras três rotas: como o dano vira auto-perpetuado | `slide-30` (cascata metabólico→funcional→patológico→clínico) — 66% |

### PARTE III — Onde o dano aparece: órgãos-alvo e o que a imagem enxerga (4 subtópicos)

| # | Subtópico | Figuras planejadas |
|---|---|---|
| 3.1 | Microangiopatia I — a retina | `slide-31` (mapa corporal das complicações) 72% + `slide-24` (retina digerida: microaneurismas) 48% |
| 3.2 | Microangiopatia II — o glomérulo, e o rim que cresce antes de encolher | `slide-33` (US renal: normal / aumentado / reduzido) — 74% |
| 3.3 | Neuropatia e pé diabético: três falhas somadas num só pé | `slide-28` (úlcera e gangrena) 55% + `slide-42` (Charcot, radiografias) 70% + `slide-43` (osteomielite, RX e RM) 70% |
| 3.4 | Macroangiopatia: aterosclerose acelerada e como se procura por ela | `slide-34` (placa estável × vulnerável → trombo) 70% + `slide-40` (AVC isquêmico na TC) 55% |

**Conclusão integradora** (`#conclusao-box`, 4 camadas) + **Resumindo** (8 seções).

---

## Seção B.bis — Registro de abertura por subtópico

Nenhum par vizinho compartilha registro. Pergunta âncora/retórica banida.

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | ponto-de-quebra |
| 1.3 | integração-anterior |
| 1.4 | analogia concreta |
| 2.1 | enquadramento |
| 2.2 | integração-posterior |
| 2.3 | ponto-de-quebra |
| 2.4 | integração-anterior |
| 3.1 | analogia concreta |
| 3.2 | enquadramento |
| 3.3 | integração-anterior |
| 3.4 | ponto-de-quebra |

---

## Seção B.ter — Pré-requisitos cruzados com frase-âncora pronta

| Pré-requisito | Frase pronta (≤25 palavras) |
|---|---|
| Receptor com atividade tirosina-quinase | "O receptor de insulina é uma enzima que se liga e se autofosforila — o sinal já nasce dentro da célula, sem segundo mensageiro." |
| Gliconeogênese | "Gliconeogênese é o fígado montando glicose nova a partir de lactato, alanina e glicerol, quando não há glicogênio de onde tirar." |
| Corpo cetônico | "Corpo cetônico é o fígado convertendo acetil-CoA em combustível ácido e solúvel, que o cérebro consegue queimar sem glicose." |
| Osmolaridade e filtração glomerular | "Filtrado glomerular é plasma sem proteína; soluto que o túbulo não reabsorve puxa água consigo e vira volume de urina." |
| Necrose por isquemia | "Sem oxigênio a célula para de fazer ATP, as bombas de membrana param, e o ponto sem volta é a membrana que deixa de reter o conteúdo." |
| Ecogenicidade | "Ecogenicidade é o quanto o tecido devolve do som que recebeu — quanto mais interfaces, mais branco na imagem." |
| Tríade de Virchow | "Trombo se forma quando falha uma de três coisas: o endotélio, o fluxo ou o equilíbrio de coagulação do sangue." |

---

## Seção C — Distribuição da E2 e termos-nota

**Taxonomia PROFUNDO:** 8 Consolidação (Q01–Q08) · 17 Integração (Q09–Q25) · 5 Aplicação (Q26–Q30).
**Formatos:** 20 múltipla escolha (A–E) · **10 Certo/Errado com exatamente 4 itens (I–IV)** distribuídos pelas três categorias · 3 "assinale a incorreta" sinalizadas no stem.

**Termos-nota obrigatórios (piso 6–10):** peptídeo C · anti-GAD65 · base de Schiff · produto de Amadori · frutosamina · diurese osmótica · hialinização arteriolar · microaneurisma · artropatia de Charcot · escore de cálcio coronariano.

**Fronteira da aula:** não entram — física do transdutor piezoelétrico, farmacologia detalhada de análogos de insulina, protocolo de reposição volêmica na cetoacidose, classificação de retinopatia por estadiamento oftalmológico.

---

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** tratar DM1 e DM2 como graus do mesmo defeito, um "mais leve" e outro "mais grave".
  **Correção:** são defeitos opostos na origem — no tipo 1 falta a fonte de insulina (ilhota destruída), no tipo 2 sobra insulina que a célula não escuta. O que os aproxima é só o resultado comum, hiperglicemia.
- **Quebra:** achar que a hiperglicemia lesa todos os tecidos igualmente.
  **Correção:** lesa preferencialmente as células que **não conseguem** regular a própria entrada de glicose — endotélio, célula mesangial, pericito, neurônio periférico, cristalino. Célula muscular fecha a porta reduzindo GLUT-4; essas não têm essa porta.
- **Quebra:** ler a HbA1c como "a glicemia de hoje, mais precisa".
  **Correção:** HbA1c é hemoglobina glicada acumulada ao longo da vida da hemácia — é a integral de 8 a 12 semanas de glicemia, não um ponto. Por isso pode estar alta com glicemia atual normal, e vice-versa.
- **Quebra:** imaginar que a base de Schiff e o AGE são o mesmo produto em nomes diferentes.
  **Correção:** a base de Schiff se desfaz em horas se a glicose cai; o produto de Amadori é estável em dias; o AGE com ligação cruzada é irreversível. O tempo que a glicose passa alta é o que define até onde a reação avança.
- **Quebra:** supor que o rim do diabético já começa pequeno.
  **Correção:** no início ele está **aumentado** — hiperfiltração e hipertrofia glomerular. A redução volumétrica, o afilamento cortical e a hiperecogenicidade são o estágio final, depois que a esclerose substituiu o parênquima.
- **Quebra:** explicar a úlcera do pé diabético só pela isquemia.
  **Correção:** são três falhas somadas — a neuropatia sensitiva tira o alarme da dor, a neuropatia autonômica seca a pele e abre fissuras, e a doença arterial periférica tira o aporte que cicatrizaria. A infecção entra pela porta que as três abriram.
- **Quebra:** achar que artropatia de Charcot é uma infecção óssea.
  **Correção:** Charcot é destruição **mecânica** — a articulação sem propriocepção nem dor recebe microtraumas repetidos e se desmonta. Osteomielite é infecção da medular óssea. As duas coexistem no mesmo pé e a distinção muda a conduta inteira.
- **Quebra:** tratar o escore de cálcio como exame que mostra a obstrução.
  **Correção:** o escore de cálcio quantifica **carga de placa calcificada**, sem contraste e sem mostrar a luz. Quem mostra a luz é a angiotomografia; quem mede a estenose com precisão e permite tratar é o cateterismo.

---

## Seção E — Exemplares-âncora

- **Categoria 1 (universal) — explicação mecanística parágrafo a parágrafo.** Acerta em dar a cada parágrafo uma função discreta e encadeada, e em apresentar o exemplo canônico como cadeia completa, não como nome citado. Vou usar em 2.1 (Schiff → Amadori → AGE) e em 1.2 (falta de insulina → hiperglucagonemia → lipólise → cetogênese → acidose), escrevendo cada etapa como consequência física da anterior.
- **Categoria 8 (universal) — `#atencao-box`.** Acerta em reservar o vermelho para a inversão que destrói o raciocínio. Reservo dois: (a) a insulina no DM2 pode estar **alta**, não baixa; (b) osteomielite × Charcot no mesmo pé.
- **Categoria 14 (universal) — siglas em footnote.** Uso inline de `#sigla` na primeira aparição de HbA1c, GLUT-4, AGE, RAGE, LDL, TC, RM, US, IAM.
- **Categoria 7 — analogia construtiva.** Acerta em usar analogia que carrega o mecanismo, não a aparência. Uso em 1.4 (a glicose que "puxa água" pelo túbulo como soluto não reabsorvido) e em 3.1 (a retina como tecido de altíssimo consumo servido por vasos terminais).
- **Categoria 9 — `#clinica-box`.** Acerta em ir até a profundidade fisiopatológica que a doença exige, com o gancho explícito para o mecanismo do subtópico. Uso em 1.2 (cetoacidose do caso), 3.2 (nefropatia com albuminúria) e 3.3 (úlcera plantar infectada).
- **Categoria 16 — catálogo de família.** Acerta em usar tabela quando há cruzamento de dimensões. Uso uma tabela só, em 3.4: método de imagem × o que mostra × custo (radiação/contraste/invasividade) × quando escolher.
- **Categoria 17 — cadência dialogal.** Manobras 2 (avaliação narrativa), 5 (marcador de progressão entre subtópicos) e 8 (negrito funcional). Uma ou duas por subtópico, sem cota.
- **Categoria 18 — quando quebrar a prosa.** Gatilho 3 (tabela de cruzamento) uma única vez, em 3.4. Todo o resto é prosa.
