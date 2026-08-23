// ================================================================
// MAIN.TYP -- biomol-recombinacao-vdj-imunoglobulinas | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Geração de diversidade de anticorpos",
  "Biologia Molecular",
  (
    ("Disciplina", "Biologia Molecular"),
    ("Onde estudar", "Alberts · Molecular Biology of the Cell (6ª ed.), cap. 24 · Watson · Molecular Biology of the Gene (7ª ed.), cap. 12 · Krebs · Lewin's Genes XI, cap. 18"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O desafio: um repertório maior que o genoma", (
      "1.1 O que o anticorpo reconhece",
      "1.2 Onde mora a variabilidade",
      "1.3 Classe e função efetora",
      "1.4 O paradoxo e a hipótese",
    )),
    ("PARTE II — A máquina: a recombinação V(D)J", (
      "2.1 O locus em segmentos",
      "2.2 A conta da combinatória",
      "2.3 RSS e a regra 12/23",
      "2.4 As recombinases RAG cortam",
      "2.5 A junção não homóloga costura",
    )),
    ("PARTE III — Ampliar a diversidade, e pagar por ela", (
      "3.1 Diversidade juncional",
      "3.2 Exclusão alélica",
      "3.3 Hipermutação somática",
      "3.4 Mudança de classe",
      "3.5 O preço do sistema",
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
    ("03", "CEEC"),
    ("04", "D"),
    ("05", "B"),
    ("06", "ECCE"),
    ("07", "E"),
    ("08", "C"),
    ("09", "D"),
    ("10", "CCEE"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "EECC"),
    ("13", "B"),
    ("14", "E"),
    ("15", "CECC"),
    ("16", "A"),
    ("17", "C"),
    ("18", "ECEE"),
    ("19", "D"),
    ("20", "B"),
    ("21", "CCEC"),
    ("22", "D"),
    ("23", "A"),
    ("24", "EECE"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "E"),
    ("27", "ECCC"),
    ("28", "B"),
    ("29", "C"),
    ("30", "CEEE"),
  )),
))
