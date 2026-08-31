// ================================================================
// MAIN.TYP -- micro-02-fisiologia-crescimento-bacteriano | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Fisiologia e crescimento bacteriano",
  "Microbiologia",
  (
    ("Disciplina", "Microbiologia"),
    ("Onde estudar", "Trabulsi & Alterthum — Microbiologia (7ª ed.) · Murray — Microbiologia Médica · Microbiologia de Brock · Tortora — Microbiologia"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A aritmética de uma população que dobra", (
      "1.1 Divisão binária e tempo de geração",
      "1.2 A conta que descreve o crescimento",
      "1.3 Onde a conta deixa de valer",
      "1.4 As quatro fases da curva",
      "1.5 Como se acompanha uma cultura",
    )),
    ("PARTE II — O que ela consome e o que ela tolera", (
      "2.1 Macronutrientes da duplicação",
      "2.2 Micronutrientes e fatores de crescimento",
      "2.3 pH: o interno é que importa",
      "2.4 Temperatura: subida química, queda proteica",
      "2.5 Oxigênio: usar sem se envenenar",
    )),
    ("PARTE III — O metabolismo e o meio que o revela", (
      "3.1 Catabolismo, anabolismo e precursores",
      "3.2 Fermentação e respiração: o aceptor final",
      "3.3 O produto final transforma o meio",
      "3.4 Meio líquido, sólido, mínimo e completo",
      "3.5 Meios diferenciais e seletivos",
      "3.6 Quando o meio não resolve",
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
  ("Consolidação (Q01–Q08)", (
    ("01", "C"),
    ("02", "ECCE"),
    ("03", "B"),
    ("04", "D"),
    ("05", "CCEC"),
    ("06", "B"),
    ("07", "E"),
    ("08", "CEEC"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "D"),
    ("10", "A"),
    ("11", "ECEE"),
    ("12", "C"),
    ("13", "E"),
    ("14", "CEEC"),
    ("15", "B"),
    ("16", "D"),
    ("17", "CEEC"),
    ("18", "D"),
    ("19", "D"),
    ("20", "CCEC"),
    ("21", "C"),
    ("22", "B"),
    ("23", "CCEE"),
    ("24", "A"),
    ("25", "CECC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "E"),
    ("28", "ECCC"),
    ("29", "B"),
    ("30", "D"),
  )),
))
