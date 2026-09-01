# UC03 — Calibração pelas provas antigas (2015-2025)

> **Status:** CANÔNICO v1 (2026-08-27). **Escopo: só UC03.** Não altera nada de UC01, UC02, UC08,
> UC16 ou de qualquer outra UC — é um artefato de componente, ligado ao pipeline por um gatilho
> condicional ("se a aula é de UC03, leia isto").
> **Papel:** régua de profundidade, igual ao `banco/indice/banco_slim.json` e ao
> `referencias-externas/blueprint-step1.md`. Consultado durante a redação; **nada daqui vai colado
> no PDF** — nem enunciado de prova antiga, nem menção a "caiu na P2 de 2024", nem número de prova.
> **Fontes:** 30 provas da UC03 (P1-P4 de 2015, 2016, 2017, 2018, 2019, 2023, 2024, 2025 + subs de
> 2015), do Drive de provas do Davi → 650 subquestões indexadas em `provas-questoes.json`.

## O contrato em três linhas

1. **O slide manda no escopo.** A prova antiga nunca decide *o que* entra num resumo — decide só
   *até onde* aprofundar o que o slide já abriu.
2. **A prova é o piso, não o teto.** A E1 entrega o teto histórico da prova **+ um degrau** de
   mecanismo (regra de `CLAUDE.md` § Profundidade elevada). Quem só empata com a prova ficou raso.
3. **Uma aula por vez.** A prova integra por caso clínico; o resumo não integra por conta própria.
   Ver § Fronteiras.

## Como usar (o gesto, não o checklist)

Ao abrir um resumo de UC03, depois de ler o slide e antes de fechar o Tema Card:

```bash
python referencias-externas/uc03/consultar.py --listar --prova P2      # confere o slug da aula
python referencias-externas/uc03/consultar.py --slug pat-07-inflamacao-aguda
python referencias-externas/uc03/consultar.py --slug micro-05-antibioticos-resistencia --desde 2023
python referencias-externas/uc03/consultar.py --termo "operon" --completo   # busca livre
```

O script cruza `banco/aulas_uc03.yml` (área + palavras-chave da aula) com o acervo e devolve **só
as subquestões daquela aula**. Linha marcada `[eco]` = a palavra-chave apareceu apenas no gabarito;
confira antes de usar, costuma ser respingo do caso clínico vizinho.

O que fazer com o resultado, em 3 passos:

- **Seção A do Tema Card:** uma linha — "teto histórico desta aula: [o que a prova cobra]; a E1 vai
  um degrau acima em [onde]".
- **E1:** o degrau vira injeção mecanística (1-3 frases) colada a um mecanismo que o slide já
  abriu — o mesmo passe de aprofundamento do `CLAUDE.md`, agora com alvo conhecido.
- **E2/E3:** a E3 (discursiva) é o lugar natural de imitar o *verbo* da FMUSP; a E2 usa o acervo
  como fonte de distratora plausível-errada e alimenta o `mapa-confusoes/<slug>.md`.

## O DNA da prova de UC03

O acervo é notavelmente estável de 2015 a 2025 — a forma quase não mudou:

- **Prova inteira montada em casos clínicos integrados.** 3 a 7 casos por prova; cada caso abre com
  vinheta longa (idade, comorbidade, exame físico, laboratório) e **um exame de imagem**.
- **Cada subquestão é etiquetada por UMA área** — `RD` (radiologia), `PT` (patologia),
  `IM` (imunologia), `MB` (microbiologia), `BM`/`BQ`/`BQ/BM` (biologia molecular e bioquímica) —
  e é corrigida em folha separada por área. Só a questão `GR` (Grand Round) vale para todas.
  **Isso é a chave do recorte:** a prova integra o *caso*, não o *conteúdo* — cada pergunta continua
  sendo de uma aula só.
- **Tudo é discursivo** (2015-2016 ainda tinham blocos de múltipla escolha; de 2017 em diante é
  quase tudo aberto), valendo 0,2 a 1,25 ponto por subquestão.
- **Verbos dominantes:** *explique* · *descreva* · *justifique* · *considerando seus conhecimentos
  de X* · *qual o mecanismo mais provável* · *aponte as diferenças entre*. Nunca "defina".
- **O gabarito premia mecanismo, não nome.** Os espelhos aceitam sinônimos e listam alternativas
  ("ambas aceitas"), mas exigem a cadeia causal explícita. Vários trazem um bloco "Pontos adicionais
  (apenas como curiosidade, não vale para a correção)" — **é exatamente aí que mora o degrau a mais
  que a E1 do NEBLI deve entregar por padrão.**
- **Distribuição das 650 subquestões:** PT 195 · IM 168 · MB 134 · RD 132 · BM/BQ 58 · GR 19.
  Nas provas recentes (2023-2025, 191 subquestões) o equilíbrio é o mesmo: IM 46 · MB 43 · PT 41 ·
  RD 35 · BM 25 · GR 7. Por prova: P2 e P1 são as mais densas; P4 concentra oncologia e choque.
- **Padrão de abertura de caso que se repete em toda prova:** "qual a modalidade de exame" +
  "descreva radiologicamente o achado" — as aulas-ferramenta de imagem e de método patológico são
  cobradas nas quatro provas, sempre.

## A régua: o que significa "um degrau acima da prova"

| Nível | O que é | Onde vive |
|---|---|---|
| Piso | O fato que o gabarito exige para pontuar | Já está no slide |
| **Teto da prova** | A cadeia causal que o gabarito exige por extenso | O que a E1 tem obrigação de cobrir bem |
| **Degrau NEBLI** | O "porquê" abaixo do teto: quem sinaliza, por que essa via e não outra, o que muda quando falha, o dado quantitativo que o gabarito só cita como curiosidade | A injeção mecanística de 1-3 frases da E1 |
| Fora | Nome de estudo, epidemiologia decorada, conduta terapêutica de ciclo clínico, vocabulário Step 1/USMLE | Não entra (banimento do `CLAUDE.md` continua valendo) |

Exemplo concreto (2025 P2, complemento): o gabarito exige "CH50 normal + AH50 indetectável = defeito
de via alternativa → menos C3b → infecção por capsulados". O degrau NEBLI é explicar **por que** a
via alternativa é a que sustenta opsonização precoce (amplificação por C3b depositado, sem precisar
de anticorpo prévio) e **por que** isso pesa mais em capsulado. Não é conteúdo novo — é o mecanismo
por baixo do fato que a prova já cobra.

## Fronteiras — a regra anti-mistura

A prova de UC03 cruza áreas dentro de um mesmo caso: pielonefrite puxa radiologia + exsudato +
E. coli + antibiograma + complemento + jejum inflamatório + operon lac, tudo no mesmo paciente.
**Isso é a prova, não é a aula.** O erro fácil aqui seria escrever o resumo de "Sistema complemento"
com meia página de antibiograma porque foi assim que caiu.

Regras operacionais:

1. **O resumo cobre um slug.** Conteúdo etiquetado com outra área na prova pertence a outra aula,
   mesmo tendo aparecido no mesmo caso.
2. **Retomada, não subtópico.** Quando o mecanismo desta aula depende de algo de outra, retomar em
   1-2 frases (o `CLAUDE.md` já manda nunca presumir pré-requisito) e seguir. Se virou parágrafo com
   figura própria, invadiu a outra aula — corta.
3. **A integração tem lugar próprio:** o texto motivador do caso na E2/E3 pode ser multiárea, como
   na prova; a explicação da E1 não.
4. **Duas aulas irmãs no mesmo dia não viram um resumo só** (ex.: "Micoses subcutâneas" e "Ativação
   de células B" caem no mesmo dia; são dois resumos). Duas partes numeradas do mesmo tema
   (Integração metabólica I/II, Expressão gênica em eucariotos I/II) continuam separadas, cada uma
   com o seu recorte.
5. **Aulas-ferramenta são exceção controlada:** radiografia/US/TC/RM e método patológico são
   cobradas em todas as provas, então quase todo caso as toca. Ainda assim, num resumo de patologia
   a imagem entra como *achado descrito*, não como aula de física do aparelho.
6. **Grand Round não vira resumo NEBLI.** É a questão que integra tudo de propósito; serve de fonte
   para texto motivador da E3, não de tema.

## Teto por componente (o que a FMUSP cobra, com que profundidade)

**RD — Radiologia.** Sempre duas camadas: (a) *nomear a modalidade e justificar a escolha* (US não
irradia e vai ao leito; TC tem resolução e irradia; RM cara e demorada; contraste iodado vs
gadolínio), (b) *descrever o achado com o termo técnico correto* — hipo/hiperatenuante (TC),
hipo/hiperecogênico (US), hipo/hipersinal e T1 vs T2 (RM), radiopaco/radiotransparente (RX) — e o
enunciado costuma avisar "é a descrição do achado, não o diagnóstico". Também cobra o **mecanismo
de formação da imagem** (piezoelétrico, efeito Doppler, precessão de núcleos de hidrogênio).
*Degrau NEBLI:* por que o tecido gera aquele sinal — o que a densidade/impedância/tempo de
relaxamento faz com a onda.

**PT — Patologia.** A área mais cobrada. Pede tipo de morte celular + padrão morfológico (gangrena,
caseosa, liquefativa, gordurosa), reversível vs irreversível com o marcador que prova, tipo de
acúmulo e por que ele se forma, exsudato vs transudato com os mecanismos de permeabilidade, padrão
morfológico da inflamação, fase do reparo, tríade de Virchow aplicada ao paciente, tipo e fase do
choque, e a lógica sequencial da carcinogênese. Pergunta clássica: "o que você esperaria encontrar
macro e microscopicamente?".
*Degrau NEBLI:* o passo bioquímico/celular por baixo do padrão morfológico — por que aquele tecido
faz aquele padrão e não outro.

**IM — Imunologia.** Cobra o eixo inato→adaptativo por inteiro, sempre ancorado num achado
laboratorial do caso (CH50/AH50, eletroforese, IgM vs IgG, PPD, anti-DNA). Pede **cinética**
(que célula/molécula em que hora), **estrutura** (Fab/Fc, IgA secretora), **mecanismo de defeito**
(qual via está quebrada e por que dá aquela infecção) e integração com o tecido (granuloma, folículo
linfoide terciário, microambiente tumoral).
*Degrau NEBLI:* a razão da ordem — por que essa célula chega antes, por que essa citocina e não
outra, o que muda no fenótipo clínico quando o passo falha.

**MB — Microbiologia.** Estrutura → patogenicidade → laboratório → tratamento. Gram e parede,
cápsula, curva de crescimento com tempo de duplicação, fatores de virulência com efeito clínico
(superantígeno vs adesina), leitura de **antibiograma/MIC** com escolha justificada de antibiótico,
mecanismo de resistência inferido do padrão, esterilização escolhida pela característica do agente.
Em micologia: dimorfismo térmico e composição da parede; em virologia: estrutura → via de
transmissão → ciclo de multiplicação → estratégia diagnóstica.
*Degrau NEBLI:* inferência a partir da estrutura — deduzir transmissão, diagnóstico e resistência do
que a parede/genoma é, em vez de listar.

**BM/BQ — Biologia Molecular e Bioquímica.** Menos questões, mas as de maior pontuação (até 1,25).
Operon lac com genótipo e diploide parcial (fenótipo previsto na presença/ausência de IPTG),
regulação epigenética e cromatina, ncRNA/miRNA com **desenho de experimento** (gene repórter, gal4),
recombinação VDJ e hipermutação somática, integração metabólica em jejum/inflamação órgão por órgão,
oncogene vs supressor a partir de um perfil molecular, e metabolismo tumoral explicando caquexia.
*Degrau NEBLI:* o raciocínio experimental — prever o resultado antes de o gabarito dizer, e explicar
o que cada controle descarta.

---

## P1 — Ferramentas, lesão celular e reconhecimento imune

| Aula (slug) | O que já caiu (acervo) | Um degrau além, na E1 | Fica de fora (é outra aula) |
|---|---|---|---|
| `rad-01-ferramentas-diagnostico-radiologico` | Escolha da modalidade e justificativa comparativa (2025 P2/P4, 2024) | Critério de escolha como decisão: o que o método resolve e a que custo (radiação, tempo, leito) | Descrição de achado (é das aulas de método) |
| `pat-01-ferramentas-diagnostico-patologico` | Biópsia vs autópsia, laudo macro/micro, imunoistoquímica, preenchimento de declaração de óbito (2019 P1, 2016 P2) | O que cada preparo revela e o que ele destrói; por que macro e micro respondem perguntas diferentes | Interpretação da lesão em si |
| `rad-02-radiografia-ultrassonografia` | Mecanismo de formação da imagem (piezoelétrico, Doppler) e termos radiopaco/opacidade/hipo-hiperecogênico (2024 P1/P2, 2025 P2/P4) | Por que o tecido faz aquele sinal: impedância acústica, atenuação, artefato | Física de TC/RM |
| `rad-03-tomografia-computadorizada` | Modalidade, janela óssea, hipo/hiperatenuante, vidro fosco, reconstrução sagital/coronal (2024 P1/P3/P4, 2025) | Atenuação como densidade medida; por que vidro fosco ≠ consolidação | Contraste (aula própria em P3) |
| `imuno-01-organizacao-sistema-imune` | Diferença inata × adaptativa com células e moléculas do caso; onde a resposta acontece (linfonodo, região) (2024 P1/P2, 2023 P2) | Por que a arquitetura do órgão linfoide impõe a sequência do encontro antígeno-linfócito | Ativação de T e de B (aulas de P3) |
| `imuno-02-reconhecimento-inato` | Elementos da primeira linha, imunidade treinada (BCG × Spike, 2025 P2), por que a inata não faz memória (2024 P2) | Do PAMP/DAMP ao efeito: qual receptor, qual via, qual citocina, em que ordem | Complemento (aula de P2) |
| `imuno-03-reconhecimento-adaptativo` | Fab/Fc, Ig de membrana × secretada, especificidade (2024 P1/P3) | Como a estrutura vira função: por que Fc define efetor e Fab define alvo | Recombinação VDJ (é BM) |
| `imuno-04-mhc-apresentacao-antigenos` | Apresentação e reconhecimento em contexto de autoimunidade e tumor (2024) | Por que classe I e II veem compartimentos diferentes e o que isso decide na resposta | Ativação de T (P3) |
| `imuno-05-mecanismos-efetores` | Mecanismo efetor pedido dentro de caso infeccioso/tumoral (2024, 2019) | Como o efetor escolhe o alvo e por que o dano fica contido (ou não) | Hipersensibilidade (P3) |
| `biomol-01-mecanismos-acao-hormonal` | Hormônio tireoideano: vias de interação e efeitos metabólicos explicando o exame físico (2024 P1); PPAR como receptor nuclear (2024 P4) | Receptor nuclear × de membrana: latência, amplificação e duração do efeito | Regulação da massa corpórea (aula irmã) |
| `biomol-02-recombinacao-vdj` | Recombinação para formar IgG em B/plasmócito (2024 P1); hipermutação somática (2023 P1) | Por que a recombinação gera diversidade sem gerar caos: o que ancora, o que sorteia | Estrutura do anticorpo (é IM) |
| `biomol-03-regulacao-hormonal-metabolismo` | Leptina e resistência à leptina, agonista de GLP-1, obesidade como inflamação de baixo grau (2023 P1, 2024 P2) | Alça de sinal saciedade→gasto e por que o sinal alto sem resposta é o padrão da obesidade | Integração metabólica (P2) |
| `pat-02-lesao-celular-necrose-apoptose` | Mecanismo de lesão do caso, reversível × irreversível, tipo e padrão de necrose, marcador que prova (troponina, transaminase) (2024 P1, 2023 P1, 2019, 2017) | Da queda de ATP à ruptura de membrana: a ordem dos eventos e onde ainda dá para voltar | Edema (aula de P2) |
| `pat-03-acumulos-adaptacao-celular` | Tipo de acúmulo e mecanismo (esteatose, proteína no mieloma, antracose, lipofuscina); hipertrofia/atrofia/metaplasia com o gatilho (2024 P1, 2023 P1, 2016, 2015) | Por que a célula acumula em vez de degradar — entrada, síntese, exportação, digestão | Neoplasia (P4) |
| `pat-04-envelhecimento-celular-tecidual` | Senescência × senilidade dentro do caso; perda de reserva funcional; plasticidade (2024 P1, 2018 P1) | Reserva funcional como conceito quantitativo: o que cai com a idade e o que só cai com doença | Telômeros e reparo (BM, P4) |
| `pat-rad-01-correlacao-pneumonia` | Correlação achado radiológico × substrato patológico (2024 P2, 2025 P2) | Traduzir imagem em tecido: o que exatamente enche o alvéolo e produz aquela opacidade | Microbiologia do agente |

## P2 — Bacteriologia, inflamação e integração metabólica

| Aula (slug) | O que já caiu (acervo) | Um degrau além, na E1 | Fica de fora (é outra aula) |
|---|---|---|---|
| `pat-05-edema-congestao` | Exsudato × transudato com justificativa; mecanismos de aumento de permeabilidade em ordem cronológica; ascite (2025 P2, 2023 P1, 2019 P1) | Starling aplicado: qual força mudou, em que vaso, em que minuto | Inflamação aguda como padrão morfológico |
| `pat-06-patologia-ambiental` | Queima de biomassa e material particulado como causa de disfunção mucociliar e inflamação sistêmica (2025 P2, 2024 P2) | Do particulado ao macrófago alveolar hipoativo: por que a exposição crônica muda o risco de infecção | Inflamação crônica (P3) |
| `pat-07-inflamacao-aguda` | Padrão morfológico esperado (supurativa, flegmonosa, serosa), eventos vasculares e celulares passo a passo, sinais flogísticos ligados ao mecanismo (2025 P2, 2024 P2, 2023 P2, 2017 P2) | Por que o padrão morfológico é consequência do agente e do tecido, não rótulo | Mediadores em detalhe (é IM, aula irmã) |
| `imuno-06-sistema-complemento` | CH50/AH50 e leitura do defeito; via alternativa e opsonização de capsulados; consumo de C3 com C4 normal; complemento em endotélio (2025 P2, 2024 P2) | Amplificação por C3b e por que os reguladores (H/I) são o freio que falta na doença | Imunodeficiências como quadro (P3) |
| `imuno-07-inflamacao-inicio-resolucao` | Cinética de mediadores e células no edema (histamina/bradicinina → PG/LT → IL-1/TNF → lipoxinas/resolvinas); resolução como processo ativo (2025 P2, 2024 P2, 2017 P2) | Resolução como programa, não como cansaço: quem desliga o recrutamento e como | Morfologia do exsudato (é PT) |
| `micro-01-morfologia-estrutura-bacterias` | Gram e parede, lipídeo A/LPS como pista de Gram-negativo, cápsula (2025 P2, 2024 P2) | Da arquitetura da parede à consequência clínica: coloração, toxicidade e alvo de antibiótico | Patogenicidade (aula própria) |
| `micro-02-fisiologia-crescimento-bacteriano` | Curva de crescimento comparada (E. coli × M. tuberculosis), por que a cultura demora, fase de ação do bacteriostático (2025 P2, 2024 P2, 2023 P2) | Tempo de duplicação como variável clínica: o que explica lag longa e persistência | Antibiótico em si |
| `micro-04-controle-microbiologico` | Escolha de esterilização/desinfecção justificada pela característica do agente e do material (2025 P2) | Por que o alvo do método (proteína, lipídio, esporo) define nível e tempo de contato | Antibioticoterapia |
| `micro-05-antibioticos-resistencia` | Leitura de MIC/antibiograma, escolha e troca justificada, mecanismo de resistência inferido do padrão (β-lactamase, gyrA/parC), bacteriostático × bactericida, sinergismo (2025 P2, 2024 P2, 2023 P2) | Ler o padrão como assinatura: qual mecanismo produz *aquele* perfil de MIC | Genética da disseminação (aula irmã) |
| `micro-06-genetica-bacteriana` | Confirmação por amplificação/sequenciamento e busca de genes de resistência por bioinformática (2025 P2) | Como o gene chega: plasmídeo, transposon, pressão seletiva — e por que resistência espalha rápido | Mecanismo bioquímico da resistência |
| `micro-07-patogenicidade-bacteriana` | Escolher 3 fatores de virulência e ligar ao quadro; superantígeno × adesão explicando gravidade distinta (2025 P2, 2024 P2, 2023 P2) | Por que o mesmo gênero causa quadros diferentes: repertório de fator × tecido | Antibiótico e laboratório |
| `micro-08-integracao-homem-ambiente-microrganismo` | Microbiota normal × patogênico no mesmo sítio, perda de barreira (2023 P2) | Quando comensal vira patógeno: barreira, sítio e imunidade do hospedeiro | Patogenicidade intrínseca |
| `biomol-05-operon-procariotos` | Componentes regulatórios, controle com/sem substrato, repressão por catabólito, genótipo e diploide parcial com IPTG/X-Gal (2025 P2, 2024 P2, 2019 P2) | Prever fenótipo a partir do genótipo — e dizer o que cada mutação prova | Expressão em eucariotos (P3) |
| `biomol-04-integracao-metabolica-i` | Vias predominantes por órgão no jejum relativo inflamatório (2025 P2, 2024 P2) | Divisão de trabalho entre fígado, músculo, adiposo e cérebro — quem exporta o quê e por quê | Estados alimentares (aula irmã) |
| `biomol-06-integracao-metabolica-ii` | Metabolismo de carboidrato, lipídio e proteína no jejum prolongado, tecido a tecido (2024 P2, 2023 P2) | A linha do tempo do jejum e o ponto em que a cetogênese poupa proteína | Regulação hormonal (P1) |
| `pat-rad-02-correlacao-patologica-radiologica-2` | Correlação imagem × substrato (2025 P2) | Mesmo gesto da correlação 1, em outro órgão | Conteúdo das aulas correlacionadas |

## P3 — Micologia, virologia, inflamação crônica e reparo

*(Cronograma provisório — títulos vindos do calendário mensal; confirmar com Davi.)*

| Aula (slug) | O que já caiu (acervo) | Um degrau além, na E1 | Fica de fora (é outra aula) |
|---|---|---|---|
| `micro-11-micoses-sistemicas` | Contágio e população de risco (Histoplasma), dimorfismo térmico e composição da parede, cápsula de Cryptococcus e fagocitose, comparação com dermatófito (2025 P3, 2024 P3) | Da parede ao comportamento: por que o dimorfismo é condição de virulência, não curiosidade | Padrão inflamatório (é PT) |
| `micro-09-micoses-cutaneas` / `micro-10-micoses-subcutaneas` | Mecanismo patogênico das micoses superficiais, queratinólise, papel da imunossupressão (2025 P3) | Por que a profundidade da invasão muda a resposta e a recidiva | Micose sistêmica |
| `micro-13-principios-gerais-virus` | Estrutura → via de transmissão; por que vírus entérico não é envelopado (2025 P3, 2024 P3) | Envelope como restrição ambiental: o que ele permite e o que ele custa | Ciclo replicativo |
| `micro-14-multiplicacao-viral` | Ciclo completo de RNA(+), papel da RdRp, efeito citopático a partir da montagem (2025 P3, 2024 P3) | Por que a estratégia de genoma dita onde o ciclo acontece e o que a célula sofre | Patogênese sistêmica |
| `micro-15-patogenese-viral` | Contagiosidade e comportamento comparado (sarampo × influenza) (2025 P3, GR) | Da porta de entrada à viremia: o que decide tropismo e gravidade | Diagnóstico laboratorial |
| `micro-16-aspectos-praticos-virologia` | Estratégia diagnóstica escolhida pela estrutura viral (RNA, antígeno, sorologia) (2025 P3, 2024 P3) | Por que cada janela temporal pede um teste diferente | Imunidade antiviral (é IM) |
| `pat-08-inflamacao-granulomatosa` | Formação do granuloma, célula epitelioide e gigante, IFN-γ ativando macrófago; por que criptococose não faz granuloma (2024 P3, 2023 P2, 2015 P2) | Granuloma como solução de contenção: quando o organismo escolhe murar em vez de eliminar | Micologia do agente |
| `pat-10-inflamacao-cronica` | Infiltrado linfomononuclear, fibrose e remodelamento; tecido linfoide terciário (2025 P3, 2024 P3) | Por que o reparo e a inflamação coexistem na crônica, e o preço funcional disso | Reparo como processo (aula irmã) |
| `pat-11-reparo-tecidual-cicatrizacao` | Primeira × segunda intenção, fases do reparo, deiscência em imunossuprimido (2025 P3, 2019 P3) | Por que a fase inflamatória comanda o cronograma do reparo | Inflamação crônica |
| `pat-12-hemostasia-trombose` | Tríade de Virchow aplicada ao paciente, fase da hemostasia hiperativada, sangramento por falência hepática (2025 P4, 2018 P3, 2016 P2) | Endotélio como interruptor: o que o vira de anticoagulante a pró-coagulante | Embolia/infarto (aula irmã) |
| `pat-13-embolia-infarto` | Etapas da formação da lesão, infarto branco × vermelho, fatores que agravam (2025 P4, 2018 P3, 2015 P3) | Por que o mesmo êmbolo dá desfechos diferentes conforme leito e colateral | Choque (P4) |
| `pat-09-patologia-infeccao-viral` | Achado tecidual esperado na resposta ao vírus (2019 P3) | Do efeito citopático ao padrão tecidual visível | Virologia estrutural |
| `imuno-08-ativacao-linfocitos-t` | Resposta celular no linfonodo, ativação e perfil de citocina (2023 P2, 2024) | Sinal 1/2/3 como decisão: o que acontece quando falta cada um | Regulação/tolerância (P4) |
| `imuno-09-ativacao-linfocitos-b` | IgM positiva com IgG negativa e o que isso diz da fase; resposta no linfonodo (2023 P2) | Centro germinativo como oficina: por que a troca de classe muda a função | Recombinação VDJ (BM, P1) |
| `imuno-11-resposta-imune-virus-fungos` | Fatores inatos antivirais celulares e não celulares, interferon; resposta a fungo intracelular (2025 P3) | Interferon como estado celular, não como citocina isolada | Hipersensibilidade |
| `imuno-12-hipersensibilidade` | Tipo I com sensibilização e fase tardia; PPD como tipo IV; interação vírus × asma (2025 P3, 2023 P2) | Por que os quatro tipos são o mesmo maquinário aplicado a alvos diferentes | Autoimunidade (aula irmã) |
| `imuno-10-disturbios-sistema-imune` | Imunodeficiência explicando o quadro; anti-DNA/anti-SM no lúpus (2024 P3) | O que a falha revela do funcionamento normal | Complemento (P2) |
| `imuno-13-bases-imunologicas-transplantes` | Imunossupressão e cicatrização comprometida; perfusão do enxerto (2025 P3) | Por que o aloenxerto é reconhecido tão rápido | Rejeição como conduta clínica |
| `biomol-07/08-expressao-genica-eucariotos` | Alterações de cromatina esperadas para um gene repórter ser expresso; regulação transcricional × epigenética no dimorfismo fúngico (2025 P3, 2024 P3) | Cromatina como estado, e o experimento que prova o estado | Operon (procarioto, P2) |
| `biomol-09-rnas-nao-codificadores` | Como ncRNA/miRNA regulam; desenhar experimento com gene repórter/gal4 para validar (2025 P3, 2024 P3) | Desenhar o controle: o que cada braço do experimento descarta | Expressão gênica geral |
| `rad-05-contrastes-radiologicos` | Tipo de contraste e por que aquele exame o exige (angio-TC com iodado) (2025 P4) | Por que o contraste realça: cinética e onde ele se distribui | Física base da TC/RM |

## P4 — Oncologia, choque e regulação imune

*(Cronograma provisório.)*

| Aula (slug) | O que já caiu (acervo) | Um degrau além, na E1 | Fica de fora (é outra aula) |
|---|---|---|---|
| `pat-14-choque-civd` | Tipo e fase do choque com justificativa; RVP/DC/FC/PVC esperados; CIVD e petéquias/púrpuras; citocinas modulando CIVD (2025 P4, 2024 P4, 2019 P4, 2016 P2) | Por que cada tipo mexe em uma variável hemodinâmica diferente — e o que a fase muda | Hemostasia básica (P3) |
| `pat-15-epidemiologia-biologia-tumores` | Critérios de malignidade no laudo, nomenclatura, estadiamento, rastreamento e queda de incidência (2018 P4, 2017 P4, 2016 P3, 2015 P3) | O que a célula perdeu (polaridade, diferenciação, controle) e como isso vira o critério do patologista | Carcinogênese molecular |
| `pat-16-carcinogenos-fisicos-quimicos` | Identificar o agente do caso e explicar como leva ao câncer (2018 P4) | Iniciação × promoção: por que dose e tempo importam de modos diferentes | Vírus oncogênico (MB) |
| `pat-17-carcinogenese-sequencial` | KRAS→p16→TP53→SMAD4 como modelo multistep; por que o conceito importa (2025 P4, 2019 P4, 2015 P3) | Por que a ordem das mutações importa mais que o número | Genes específicos (BM) |
| `pat-18-angiogenese-metastase` | VEGF e metástase, elementos do processo invasivo, heterogeneidade molecular metástase × primário e resistência (2025 P4, 2024 P4, 2018 P4) | Cascata metastática como filtro: por que quase toda célula que sai morre | Terapia-alvo (BM) |
| `imuno-14-imunidade-mucosas` | IgA secretora e dendrítica intestinal contendo vírus entérico (2025 P3) | Por que a mucosa defende sem inflamar | Hipersensibilidade |
| `imuno-15-regulacao-sistema-imune` | Treg/Foxp3 e tolerância central × periférica (2025 P3, Nobel 2025) | Tolerância como processo ativo e contínuo | Autoimunidade (P3) |
| `imuno-16-mecanismos-escape-imune` | Microambiente tumoral imunossupressor; anti-PD-L1 e consequência clínica; imunoprivilégio quebrado (2025 P4, 2024 P4, 2024 P3) | Imunoedição: por que o tumor que aparece é o que já escapou | Terapia oncológica em detalhe |
| `biomol-10-oncogenes-genes-supressores` | Classificar genes de um perfil molecular como oncogene ou supressor com justificativa; BRAF e reparo mismatch; propor terapia-alvo plausível (2025 P4, 2024 P4, 2016 P3, 2015 P3s) | Ganho × perda de função como assimetria: por que supressor precisa de dois eventos | Carcinogênese sequencial (PT) |
| `biomol-11-metabolismo-celulas-neoplasicas` | Alterações metabólicas explicando emagrecimento/caquexia; Warburg (2025 P4, 2024 P4) | Por que a célula tumoral escolhe a via ineficiente | Nutrição clínica |
| `biomol-12-telomeros-reparo-dna` | Telomerase e imortalização; defeito de reparo mismatch como fase inicial (2024 P4, 2016 P3, 2015 P3s) | Telômero como relógio e o que a reativação compra para o tumor | Envelhecimento tecidual (PT, P1) |
| `micro-17-carcinogenos-biologicos` | HBV na carcinogênese hepática (direto e indireto); bloco objetivo sobre vírus tumorigênicos, mutagênese insercional, vacina profilática (2025 P4, 2024 P4, 2016 P3) | Por que o vírus oncogênico precisa de tempo e de um segundo evento | Carcinogênese química |

---

## Manutenção

- **Prova nova do Davi:** salvar o PDF, extrair o texto e rodar o mesmo parser que gerou a base
  (`enunciado`/`gabarito` por subquestão etiquetada). Acrescentar os itens a `provas-questoes.json`
  mantendo os campos `ano`, `prova`, `q`, `tag`, `componentes`, `enunciado`, `gabarito`, `fonte`.
- **Cronograma oficial de P3/P4:** quando a tabela da planilha for estendida, tirar
  `provisorio: true` das aulas e preencher `conteudo:` em `banco/aulas_uc03.yml`.
- **Chaves de uma aula erradas** (evidência de outra aula vazando, ou aula sem evidência que
  deveria ter): ajustar `chaves:` no YAML — é lá que mora o recorte, não aqui.
- Esta calibração é de UC03. Regra que valha para todas as UCs vai para o `CLAUDE.md`, não para cá.

## Apêndice — acervo indexado

Pasta de origem: Drive do Davi, "provas UC03" (subpastas P1/P2/P3/P4)
<https://drive.google.com/drive/folders/1u7bS8L_6iZ_kE6-OynGtepbKyLLo0SUR>.
Cronograma de 2026: planilha de agenda do Davi, aba com a tabela UC03 (Data/Horário/Local/N/C/Tema/P)
<https://docs.google.com/spreadsheets/d/1T1RZ_vpqtchmdM8U2BXYmlHk7e-Ov-iCGM51PFIEqMU>.
Os PDFs **não** são versionados aqui (≈50 MB); o que entra no repo é o índice de subquestões.

| Ano | Prova | Subquestões | Arquivo (nome normalizado; no Drive vem com acento) |
|---|---|---|---|
| 2025 | P2 | 24 | `Prova-II-UC3-2025-Final-com-Gabarito-Edisciplinas.pdf` |
| 2025 | P3 | 23 | `P3-UC3-2025-GabaritoeCriterios.pdf` |
| 2025 | P4 | 20 | `P4-UC3-2025-Final-Com-Gabarito-e-Crit-rios-1.pdf` |
| 2024 | P1 | 19 | `CasosP1-2024-Gabaritov2-2.pdf` |
| 2024 | P2 | 21 | `UC3-Prova-2-2024-Gabarito.pdf` |
| 2024 | P3 | 21 | `UC3-Prova-3-2024-Gabarito.pdf` |
| 2024 | P4 | 22 | `UC3-Prova-4-2024-Gabarito.pdf` |
| 2023 | P1 | 19 | `UC3-P1-2023-Gabarito.pdf` |
| 2023 | P2 | 22 | `UC3-Prova-2-2023-GabaritoParcial-FaltaImunoeBQ.pdf` |
| 2019 | P1 | 24 | `UC3-P1-2019-Gabarito.pdf` |
| 2019 | P2 | 23 | `UC3-P2-2019-v2.pdf` |
| 2019 | P3 | 22 | `P3-UC3-2019-V3-Final.pdf` |
| 2019 | P4 | 21 | `UC3-P4-2019-v3.pdf` |
| 2018 | P1 | 20 | `UC3-P1-2018-Gabarito.pdf` |
| 2018 | P2 | 20 | `UC3-Prova-2-2018-Gabarito-v3.pdf` |
| 2018 | P3 | 22 | `UC3-Prova-3-2018-Gabarito-v3.pdf` |
| 2018 | P4 | 16 | `UC3-Prova-4-2018-Gabarito-v3.pdf` |
| 2017 | P1 | 24 | `UC3-P1-2017-Respostas-e-Coment-rios.pdf` |
| 2017 | P2 | 21 | `UC3-P2-2017-Respostas-e-Coment-rios.pdf` |
| 2017 | P3 | 20 | `UC3-Prova-3-2017-Respostas-e-Coment-rios.pdf` |
| 2017 | P4 | 19 | `UC3-Prova-4-2017-Respostas-e-Coment-rios.pdf` |
| 2016 | P1 | 36 | `UC3-P1-2016-Gabarito.pdf` |
| 2016 | P2 | 30 | `UC3-P2-2016-Gabarito.pdf` |
| 2016 | P3 | 20 | `UC3-P3-2016-Gabarito.pdf` |
| 2015 | P1 | 20 | `UC3-P1-2015-Gabarito.pdf` |
| 2015 | P1sub | 17 | `UC3-P1-Sub-2015-Gabarito.pdf` |
| 2015 | P2 | 40 | `UC3-P2-2015-Gabarito.pdf` |
| 2015 | P2sub | 22 | `UC3-P2-Sub-2015-Gabarito.pdf` |
| 2015 | P3 | 11 | `UC3-P3-2015-Gabarito.pdf` |
| 2015 | P3sub | 11 | `UC3-P3-Sub-2015-Gabarito.pdf` |
