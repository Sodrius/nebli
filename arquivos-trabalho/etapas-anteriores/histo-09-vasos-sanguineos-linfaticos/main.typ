// ================================================================
// MAIN.TYP -- histo-09-vasos-sanguineos-linfaticos | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Histologia dos Vasos Sanguíneos e Linfáticos",
  "Histologia",
  (
    ("Disciplina", "Histologia (UC02)"),
    ("Onde estudar", "Slides do Prof. ML (histologia do sistema circulatório) · Junqueira & Carneiro, Histologia Básica, cap. 11 · Ross & Pawlina, cap. 13"),
    ("Onde aprofundar", [
      #set par(leading: 0.6em, justify: false, first-line-indent: 0em, hanging-indent: 0.9em)
      #text(fill: navy, weight: "bold", "• ") *Assistir/ler* — NinjaNerd (Histology: Blood Vessels) · Bootcamp (Anatomy/Histology › Vasculatura) · Pathoma cap. 6 (só a patologia: aterosclerose e vasculites) · Sketchy: não cobre histologia básica \
      #text(fill: navy, weight: "bold", "• ") *Dessuspender no AnKing v12* — ordenados por completude no tema; dessuspenda de cima pra baixo: \
      #text(fill: navy, weight: "bold", "• ") *Cobre melhor* · \#FirstAid::07\_Cardiovascular::02\_Anatomy::*Blood\_Vessels — 15 cards (as 3 túnicas, artéria × veia, tipos de capilar) \
      #text(fill: navy, weight: "bold", "• ") *Complementa* · \#FirstAid::07\_Cardiovascular::03\_Physiology::20\_Capillary\_fluid\_exchange — 24 cards (troca capilar e edema) \
      #text(fill: navy, weight: "bold", "• ") *Mais distante* · \#Bootcamp::Cardiology::23\_Stable\_Angina\_and\_Atherosclerosis::02\_Atherosclerosis — 30 cards (só o gancho clínico: endotélio → aterosclerose) \
      #text(fill: navy, weight: "bold", "• ") *Mais distante* · \#FirstAid::11\_Musculoskeletal::*Vasculature::Varicose\_Veins — 6 cards (só varizes)
    ]),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O plano comum: a parede em três túnicas", (
      "O circuito e o problema que a parede resolve",
      "As três túnicas: íntima, média e adventícia",
      "O endotélio não é forro passivo",
    )),
    ("PARTE II — Da alta pressão à troca: artérias, arteríolas e capilares", (
      "Artérias elásticas e musculares: amortecer ou distribuir",
      "Arteríola e metarteríola: a torneira da pressão",
      "Capilares: onde o sangue realmente troca",
    )),
    ("PARTE III — O retorno de baixa pressão e a drenagem", (
      "Veias: muita luz, pouca parede",
      "Válvulas venosas e o retorno contra a gravidade",
      "O sistema linfático: recolher o que vazou",
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
    ("02", "CECC"),
    ("03", "A"),
    ("04", "D"),
    ("05", "ECCE"),
    ("06", "B"),
    ("07", "E"),
    ("08", "CEEC"),
    ("09", "C"),
    ("10", "A"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "ECCE"),
    ("12", "D"),
    ("13", "CECC"),
    ("14", "B"),
    ("15", "E"),
    ("16", "CECC"),
    ("17", "A"),
    ("18", "C"),
    ("19", "EECC"),
    ("20", "D"),
    ("21", "B"),
    ("22", "CCEE"),
    ("23", "E"),
    ("24", "ECEE"),
    ("25", "A"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "E"),
    ("28", "CEEC"),
    ("29", "B"),
    ("30", "D"),
  )),
))
