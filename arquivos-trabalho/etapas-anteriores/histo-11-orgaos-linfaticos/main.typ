// ================================================================
// MAIN.TYP -- histo-11-orgaos-linfaticos | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Tecido e Órgãos Linfoides: das Células à Arquitetura do Timo, Linfonodo e Baço",
  "Histologia",
  (
    ("Disciplina", "Histologia (UC02)"),
    ("Onde estudar", "Slides da aula Tecido Linfóide (UC02, Histologia, Profa. Marilene H. Lopes) · Junqueira & Carneiro, Histologia Básica, cap. Sistema Imunitário e Órgãos Linfáticos · Kierszenbaum, Histologia e Biologia Celular"),
    ("Onde aprofundar", [
      #set text(size: 7.3pt)
      #set par(leading: 0.55em, justify: false, first-line-indent: 0em, hanging-indent: 0.9em)
      #text(fill: navy, weight: "bold", "• ") *Assistir/ler* — Ninja Nerd (Lymphatic System: histology) · Boards & Beyond (Immunology › Lymph Nodes and Spleen) · Pathoma: não cobre (é patologia geral) · Sketchy: não cobre histologia pura · UWorld: ganchos clínicos (asplenia e encapsulados, DiGeorge, esferocitose) \
      #text(fill: navy, weight: "bold", "• ") *Dessuspender no AnKing v12* (decks sob \#AK\_​Step1\_​v12::​) — ordenados por completude; dessuspenda de cima pra baixo: \
      #text(fill: navy, weight: "bold", "• ") *Cobre melhor* · \#B&B::​13\_​Immunology::​01\_​Basic\_​Immunology::​05\_​Lymph\_​Nodes\_​and\_​Spleen — 45 cards (linfonodo e baço: estrutura, zonas B/T, função de filtro) \
      #text(fill: navy, weight: "bold", "• ") *Complementa* · \#FirstAid::​02\_​Immunology::​01\_​Lymphoid\_​Structures::​04\_​Spleen — 14 cards (baço: polpa branca/vermelha, PALS, asplenia) \
      #text(fill: navy, weight: "bold", "• ") *Complementa* · \#FirstAid::​02\_​Immunology::​01\_​Lymphoid\_​Structures::​05\_​Thymus — 7 cards (timo: anatomia e histologia, córtex/medula) \
      #text(fill: navy, weight: "bold", "• ") *Mais distante* · o tecido linfoide difuso/MALT, os arranjos frouxo-denso-nodular e o corpúsculo de Hassall aparecem só de raspão nos decks Step 1 — a fonte fina é o slide da Profa. Marilene + Junqueira
    ]),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — As células e a arquitetura do tecido linfoide", (
      "Primário vs secundário; as linhagens",
      "Células fixas e células livres",
      "Frouxo, denso, nodular e o MALT",
    )),
    ("PARTE II — Órgãos linfoides primários", (
      "Timo: lóbulos, córtex e medula",
      "Estroma epitelial e timócitos",
      "Barreira, Hassall e involução",
    )),
    ("PARTE III — Órgãos linfoides secundários", (
      "Linfonodo: o filtro da linfa",
      "Baço: o filtro do sangue",
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
    ("02", "D"),
    ("03", "CECC"),
    ("04", "A"),
    ("05", "C"),
    ("06", "E"),
    ("07", "ECEE"),
    ("08", "A"),
    ("09", "CCEC"),
    ("10", "C"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "E"),
    ("12", "ECCE"),
    ("13", "B"),
    ("14", "D"),
    ("15", "CEEC"),
    ("16", "A"),
    ("17", "E"),
    ("18", "EECE"),
    ("19", "C"),
    ("20", "CCEE"),
    ("21", "B"),
    ("22", "ECCC"),
    ("23", "D"),
    ("24", "A"),
    ("25", "CEEC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "E"),
    ("27", "C"),
    ("28", "CEEC"),
    ("29", "B"),
    ("30", "D"),
  )),
))
