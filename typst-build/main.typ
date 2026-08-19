// ================================================================
// MAIN.TYP -- biotec-01-tubo-digestorio-estomago | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Tubo digestório e estômago",
  "Biologia Tecidual",
  (
    ("Disciplina", "Biologia Tecidual — Sistema Digestório"),
    ("Onde estudar", "Junqueira & Carneiro · Histologia Básica (14ª ed.), cap. 15–16 · Kierszenbaum · Histologia e Biologia Celular (4ª ed.), cap. 15 · Gartner & Hiatt · Atlas Colorido de Histologia · Wheater · Histologia Funcional"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O plano comum: as quatro túnicas", (
      "1.1–1.2 Plano geral e mucosa por dentro",
      "1.3–1.4 Submucosa, muscular e os dois plexos",
      "1.5 Serosa ou adventícia",
    )),
    ("PARTE II — A entrada do tubo: da boca ao esôfago", (
      "2.1–2.2 Boca, língua e dente",
      "2.3 Glândulas salivares",
      "2.4 Esôfago — o plano em forma legível",
    )),
    ("PARTE III — O estômago: mucosa, regiões e células", (
      "3.1–3.2 Túnicas gástricas e as três regiões",
      "3.3–3.4 Eixo istmo-colo-base e os tipos celulares",
      "3.5–3.6 Célula parietal e a barreira mucosa",
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
    ("03", "CCEE"),
    ("04", "D"),
    ("05", "B"),
    ("06", "B"),
    ("07", "CCCE"),
    ("08", "A"),
    ("09", "ECCE"),
    ("10", "C"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "B"),
    ("12", "E"),
    ("13", "CCCE"),
    ("14", "D"),
    ("15", "B"),
    ("16", "ECCE"),
    ("17", "C"),
    ("18", "A"),
    ("19", "ECCC"),
    ("20", "E"),
    ("21", "D"),
    ("22", "CECC"),
    ("23", "A"),
    ("24", "D"),
    ("25", "CEEC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "ECEE"),
    ("28", "E"),
    ("29", "C"),
    ("30", "EECE"),
  )),
))
