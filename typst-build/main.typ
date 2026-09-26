// ================================================================
// MAIN.TYP -- bioq-24-glicogenio | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Metabolismo do glicogênio",
  "Bioquímica · Síntese, degradação e regulação",
  (
    ("Disciplina", "Bioquímica"),
    ("Onde estudar", "Lehninger Cap. 15 + slides do prof."),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A molécula e a lógica do estoque", (
      "1.1 A árvore de glicose com muitas pontas",
      "1.2 Fígado versus músculo",
      "1.3 Por que estocar como polímero",
    )),
    ("PARTE II — Quebrar e construir", (
      "2.1 Glicogenólise e fosforólise",
      "2.2 Fosfoglicomutase e o destino tecidual",
      "2.3 Glicogênese e a UDP-glicose",
    )),
    ("PARTE III — A regulação coordenada", (
      "3.1 Regulação recíproca",
      "3.2 Cascata do glucagon e adrenalina",
      "3.3 Insulina, PP1 e o sensor hepático",
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
    ("02", "B"),
    ("03", "D"),
    ("04", "CECC"),
    ("05", "A"),
    ("06", "E"),
    ("07", "CCEC"),
    ("08", "B"),
    ("09", "C"),
    ("10", "CCEC"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "B"),
    ("12", "C"),
    ("13", "CCEC"),
    ("14", "B"),
    ("15", "D"),
    ("16", "CECC"),
    ("17", "C"),
    ("18", "B"),
    ("19", "CCCE"),
    ("20", "E"),
    ("21", "C"),
    ("22", "CCEC"),
    ("23", "B"),
    ("24", "D"),
    ("25", "CCEC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "C"),
    ("28", "B"),
    ("29", "A"),
    ("30", "CCEC"),
  )),
))
