// ================================================================
// MAIN.TYP -- patologia-adaptacao-acumulos | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Adaptação Celular e Acúmulos",
  "Patologia",
  (
    ("Disciplina", "Patologia — Departamento de Patologia"),
    ("Onde estudar", "Robbins & Cotran, Patologia — Bases Patológicas das Doenças (10ª ed.), Cap. 1 e 2 · Brasileiro Filho, Bogliolo — Patologia (10ª ed.), Cap. 4 a 6"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A célula que se adapta", (
      "1.1 Adaptação, lesão e tipo de tecido",
      "1.2 Hipertrofia: célula maior",
      "1.3 Hiperplasia: mais células",
      "1.4 Atrofia, hipoplasia e aplasia",
      "1.5 Metaplasia: trocar de identidade",
    )),
    ("PARTE II — Acúmulos: lógica, lipídios e proteínas", (
      "2.1 As quatro rotas do acúmulo",
      "2.2 Esteatose: o balanço do hepatócito",
      "2.3 Colesterol: ateroma, xantoma, colesterolose",
      "2.4 Acúmulos proteicos e amiloide",
    )),
    ("PARTE III — Glicogênio, pigmentos e cálcio", (
      "3.1 Glicogênio: diabetes e glicogenoses",
      "3.2 Lipofuscina e melanina",
      "3.3 Hemossiderina, ferro e bilirrubina",
      "3.4 Calcificação distrófica e metastática",
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
    ("01", "D"),
    ("02", "CECC"),
    ("03", "B"),
    ("04", "E"),
    ("05", "CCEC"),
    ("06", "A"),
    ("07", "C"),
    ("08", "ECCE"),
    ("09", "E"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "CEEC"),
    ("13", "D"),
    ("14", "C"),
    ("15", "CCCE"),
    ("16", "E"),
    ("17", "A"),
    ("18", "ECCE"),
    ("19", "D"),
    ("20", "EECC"),
    ("21", "CCEE"),
    ("22", "B"),
    ("23", "E"),
    ("24", "ECCC"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "D"),
    ("28", "ECEE"),
    ("29", "A"),
    ("30", "C"),
  )),
))
