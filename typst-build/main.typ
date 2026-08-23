// ================================================================
// MAIN.TYP -- geriatria-envelhecimento-celular-tecidual | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Envelhecimento celular e tecidual",
  "Geriatria · Patologia",
  (
    ("Disciplina", "Geriatria e Patologia — Ciclo da Vida I"),
    ("Onde estudar", "Robbins, Bases Patológicas das Doenças — cap. 1 (lesão celular e envelhecimento) · Jacob Filho & Kikuchi, Geriatria e Gerontologia Básicas"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O que envelhece primeiro é a margem", (
      "1.1 Senescência e senilidade",
      "1.2 Reserva funcional e homeostenose",
      "1.3 O retrato externo da senescência",
    )),
    ("PARTE II — Os quatro motores celulares", (
      "2.1 Quatro entradas, um destino",
      "2.2 Radicais livres e dano ao DNA",
      "2.3 Telômeros e o relógio das divisões",
      "2.4 Proteínas danificadas e o freio metabólico",
    )),
    ("PARTE III — Do dano celular ao corpo do idoso", (
      "3.1 Três engrenagens em todo aparelho",
      "3.2 Pulmão e coração",
      "3.3 Cérebro e rim",
    )),
  )),
  ("Resumindo", (
    (none, (
      "Dez cápsulas de revisão rápida",
    )),
  )),
  ("Etapa 2 — 30 questões objetivas", (
    (none, (
      "Consolidação, integração e aplicação",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Cadeias mecanísticas com resposta-modelo",
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
    ("08", "CCEC"),
    ("09", "C"),
    ("10", "A"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "EECC"),
    ("13", "CEEC"),
    ("14", "B"),
    ("15", "CCEE"),
    ("16", "E"),
    ("17", "C"),
    ("18", "ECCC"),
    ("19", "A"),
    ("20", "D"),
    ("21", "CEEE"),
    ("22", "A"),
    ("23", "E"),
    ("24", "EECC"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "D"),
    ("28", "ECCE"),
    ("29", "B"),
    ("30", "C"),
  )),
))
