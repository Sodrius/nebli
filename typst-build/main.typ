// ================================================================
// MAIN.TYP -- anato-03-intestino-grosso-canal-anal | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Intestino grosso, reto e canal anal",
  "Anatomia do Sistema Digestório",
  (
    ("Disciplina", "Anatomia do Sistema Digestório"),
    ("Onde estudar", "Moore, Anatomia Orientada para a Clínica (6ª ed.) · Netter, Atlas de Anatomia Humana · Sobotta (23ª ed.) · Prometheus · Dangelo & Fattini"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O tubo que reabsorve", (
      "1.1 As dez partes e o trajeto",
      "1.2 Fixo e móvel: quem se torce",
      "1.3 Tênias, saculações e apêndices",
      "1.4 Quadrantes, flexuras e sulcos",
    )),
    ("PARTE II — A junção ileocecal", (
      "2.1 Ceco e válvula ileocecal",
      "2.2 Apêndice vermiforme",
      "2.3 Posição variável e McBurney",
    )),
    ("PARTE III — Reto e canal anal", (
      "3.1 Reto, flexuras e puborretal",
      "3.2 Ampola, pregas e relações",
      "3.3 Canal anal por dentro",
      "3.4 A fronteira da linha pectinada",
      "3.5 O aparelho esfincteriano",
    )),
  )),
  ("Etapa 2 — 30 objetivas", (
    (none, (
      "Consolidação, Integração e Aplicação — múltipla escolha e certo/errado",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Casos e mecanismos ancorados nas três PARTES",
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
    ("03", "E"),
    ("04", "B"),
    ("05", "ECCE"),
    ("06", "A"),
    ("07", "CCEC"),
    ("08", "D"),
    ("09", "C"),
    ("10", "EECC"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "E"),
    ("12", "B"),
    ("13", "CEEC"),
    ("14", "D"),
    ("15", "A"),
    ("16", "CCEE"),
    ("17", "C"),
    ("18", "E"),
    ("19", "ECCE"),
    ("20", "B"),
    ("21", "CCEE"),
    ("22", "D"),
    ("23", "D"),
    ("24", "CCEC"),
    ("25", "A"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "E"),
    ("27", "A"),
    ("28", "CCEC"),
    ("29", "B"),
    ("30", "C"),
  )),
))
