// ================================================================
// MAIN.TYP -- anato-05-circulatorio-linfatico-I | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Anatomia do Sistema Circulatório e Linfático I",
  "Anatomia",
  (
    ("Disciplina", "Anatomia (UC02)"),
    ("Onde estudar", "Slides da Profa. Katiúcia B. S. Paiva (Aula 5, Partes 1 e 2) · Moore, Anatomia Orientada para a Clínica, cap. 1 (mediastino/coração) · Netter, Atlas de Anatomia Humana (tórax) · Roteiros RT e RP da Aula 5"),
    ("Onde aprofundar", [
      #set par(leading: 0.6em, justify: false, first-line-indent: 0em, hanging-indent: 0.9em)
      #text(fill: navy, weight: "bold", "• ") *Assistir/ler* — Ninja Nerd (Heart Anatomy: chambers, valves, coronaries) · Boards & Beyond / Bootcamp (Cardiovascular › Anatomy) · Sketchy Anatomy (Thorax › Heart) · UWorld: pouca anatomia macro pura (só ganchos) · Pathoma: não cobre (é patologia) \
      #text(fill: navy, weight: "bold", "• ") *Dessuspender no AnKing v12* (decks sob \#AK\_Step1\_v12::) — ordenados por completude; dessuspenda de cima pra baixo: \
      #text(fill: navy, weight: "bold", "• ") *Cobre melhor* · \#SketchyAnatomy::02\_Thorax::02\_Heart::01\_Chambers\_of\_Heart — 33 cards (câmaras, septos, circuito D/E) \
      #text(fill: navy, weight: "bold", "• ") *Cobre melhor* · \#OME::PreClinical::Cardiac::Cardiac\_3::Anatomy\_of\_the\_Heart\_and\_Mediastinum — 28 cards (coração + mediastino + pericárdio) \
      #text(fill: navy, weight: "bold", "• ") *Complementa* · \#FirstAid::07\_Cardiovascular::02\_Anatomy::01\_Heart\_anatomy — 23 cards (anatomia + irrigação coronária + pericárdio) \
      #text(fill: navy, weight: "bold", "• ") *Complementa* · \#SketchyAnatomy::02\_Thorax::02\_Heart::02\_Coronary\_Circulation — 23 cards (coronárias e seio coronário) \
      #text(fill: navy, weight: "bold", "• ") *Mais distante* · \#FirstAid::02\_Immunology::01\_Lymphoid\_Structures::04\_Spleen — 10 cards (baço, linfoide secundário) \
      #text(fill: navy, weight: "bold", "• ") *Mais distante* · \#FirstAid::02\_Immunology::01\_Lymphoid\_Structures::05\_Thymus — 4 cards (timo, linfoide primário)
    ]),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O circuito e a bomba dentro do tórax", (
      "Para que serve e como o circuito se fecha",
      "Dois lados, dois circuitos",
      "Onde o coração mora: o mediastino",
      "A superfície do coração: faces, margens e sulcos",
      "O pericárdio: o saco que envolve e ancora",
    )),
    ("PARTE II — Por dentro do coração: câmaras, paredes e valvas", (
      "As quatro câmaras e os septos",
      "As três camadas e o aparelho interno do ventrículo",
      "Valvas atrioventriculares: tricúspide e mitral",
      "Valvas semilunares e o jogo de pressões",
      "Esqueleto fibroso e a irrigação do próprio coração",
    )),
    ("PARTE III — Os vasos, o retorno e a drenagem linfática", (
      "Os grandes vasos da base",
      "Artérias, capilares e veias: o plano dos vasos",
      "A microcirculação e a vasomotricidade",
      "As veias e o retorno de baixa pressão",
      "O sistema linfático: drenar, transportar, defender",
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
    ("01", "B"),
    ("02", "CEEC"),
    ("03", "D"),
    ("04", "A"),
    ("05", "ECCE"),
    ("06", "C"),
    ("07", "E"),
    ("08", "CCEE"),
    ("09", "B"),
    ("10", "D"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "CEEC"),
    ("12", "A"),
    ("13", "E"),
    ("14", "ECCE"),
    ("15", "C"),
    ("16", "B"),
    ("17", "CEEC"),
    ("18", "D"),
    ("19", "A"),
    ("20", "EECC"),
    ("21", "C"),
    ("22", "B"),
    ("23", "CCEE"),
    ("24", "E"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "A"),
    ("28", "CCEE"),
    ("29", "E"),
    ("30", "B"),
  )),
))
