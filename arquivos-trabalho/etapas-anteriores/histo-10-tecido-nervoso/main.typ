// ================================================================
// MAIN.TYP -- histo-10-tecido-nervoso | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Tecido Nervoso: o Neurônio, a Glia e a Arquitetura do Sistema Nervoso",
  "Histologia",
  (
    ("Disciplina", "Histologia (UC02)"),
    ("Onde estudar", "Slides da aula Histofisiologia do Tecido Nervoso (UC02, Histologia) · Junqueira & Carneiro, Histologia Básica, 13ª ed., cap. Tecido Nervoso · Kierszenbaum, Histologia e Biologia Celular, 2ª ed., cap. Tecido Nervoso"),
    ("Onde aprofundar", [
      #set text(size: 7.3pt)
      #set par(leading: 0.55em, justify: false, first-line-indent: 0em, hanging-indent: 0.9em)
      #text(fill: navy, weight: "bold", "• ") *Assistir/ler* — Boards & Beyond / Bootcamp (Neuro › Cells of the Nervous System) · Ninja Nerd (Histology of Nervous Tissue) · Sketchy: não cobre histologia pura · Pathoma: não cobre (é patologia geral) · UWorld: ganchos clínicos (Guillain-Barré, esclerose múltipla, transporte axonal na raiva) \
      #text(fill: navy, weight: "bold", "• ") *Dessuspender no AnKing v12* (decks sob \#AK\_​Step1\_​v12::​) — ordenados por completude; dessuspenda de cima pra baixo: \
      #text(fill: navy, weight: "bold", "• ") *Cobre melhor* · \#FirstAid::​12\_​Neurology\_​and\_​Special\_​Senses::​02\_​Anatomy\_​and\_​Physiology::​01\_​Cells\_​of\_​the\_​nervous\_​system — \~55 cards (neurônio, astrócito, oligodendrócito, Schwann, microglia, mielina) \
      #text(fill: navy, weight: "bold", "• ") *Complementa* · \#Bootcamp::​16\_​Neuro::​01\_​Introduction\_​to\_​Neurology::​01\_​Cells\_​of\_​the\_​Nervous\_​System — 43 cards (células do tecido nervoso, visão integrada) \
      #text(fill: navy, weight: "bold", "• ") *Mais distante* · \#FirstAid::​12\_​Neurology\_​and\_​Special\_​Senses::​03\_​Pathology::​24\_​...::​Guillain-Barre\_​Syndrome — 22 cards (desmielinização do SNP) \
      #text(fill: navy, weight: "bold", "• ") *Mais distante* · \#Bootcamp::​Neurology::​10\_​Demyelinating\_​Diseases::​02\_​Multiple\_​Sclerosis — 58 cards (desmielinização do SNC)
    ]),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O neurônio: a célula que fala", (
      "De onde vêm e os tipos de neurônio",
      "O corpo celular: a fábrica do neurônio",
      "Dendritos, axônio e o transporte a longa distância",
      "A sinapse: onde o sinal passa adiante",
    )),
    ("PARTE II — A glia e a bainha de mielina", (
      "Astrócitos e a barreira hematoencefálica",
      "Oligodendrócito, Schwann e a mielina",
      "Microglia, ependimárias e células satélites",
    )),
    ("PARTE III — A arquitetura do tecido nervoso", (
      "Substância branca e substância cinzenta",
      "Córtex cerebral, cerebelo e medula espinal",
      "O nervo periférico, os gânglios e as meninges",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"

// ======= ETAPA 2 =======
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
#gabarito-page((
  ("Consolidação (Q01–Q10)", (
    ("01", "C"),
    ("02", "A"),
    ("03", "CCEC"),
    ("04", "D"),
    ("05", "B"),
    ("06", "ECCE"),
    ("07", "E"),
    ("08", "C"),
    ("09", "CEEC"),
    ("10", "A"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "EECC"),
    ("13", "B"),
    ("14", "E"),
    ("15", "CECC"),
    ("16", "A"),
    ("17", "C"),
    ("18", "ECEE"),
    ("19", "B"),
    ("20", "D"),
    ("21", "CCEE"),
    ("22", "E"),
    ("23", "A"),
    ("24", "EECE"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "CEEC"),
    ("28", "D"),
    ("29", "E"),
    ("30", "ECCE"),
  )),
))
