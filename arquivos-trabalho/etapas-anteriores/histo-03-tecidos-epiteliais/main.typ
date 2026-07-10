// ================================================================
// MAIN.TYP -- histo-03-tecidos-epiteliais | Editado manualmente 2026-06-02
// Patch: capa() e sumario() estavam vazios (Tema Card usa schema antigo
// que gerar_main.py não lê). Preenchidos à mão preservando o restante.
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Tecidos epiteliais",
  "UC2 · Histologia · Aula 03",
  (
    ("Disciplina", "Histologia (UC2)"),
    ("Onde estudar", "Junqueira & Carneiro, Histologia Básica (cap. 4); Ross & Pawlina, Histologia Texto e Atlas (cap. 5)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O que torna um epitélio um epitélio", (
      "Polaridade, junções e lâmina basal",
      "Avascularidade obrigatória do folheto",
      "Origem nas três folhas embrionárias",
    )),
    ("PARTE II — Atlas de identificação", (
      "Algoritmo: camadas × forma × ápice",
      "Simples, estratificado e pseudoestratificado",
      "Especializações apicais como pistas",
    )),
    ("PARTE III — Epitélio glandular", (
      "Exócrinas: três eixos de classificação",
      "Mucoso × seroso × misto",
      "Endócrinas cordonais e foliculares",
    )),
  )),
  ("Resumindo", (
    (none, (
      "Síntese em 1–2 páginas (banner gold)",
    )),
  )),
  ("Etapa 2 — 30 objetivas", (
    (none, (
      "Consolidação (Q01–Q10), Integração (Q11–Q25), Aplicação (Q26–Q30)",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Modelos de resposta ≤100 palavras (Q5 ≤130)",
    )),
  )),
  ("Gabarito — Etapa 2", (
    (none, (
      "Consolidado ao final",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO (logo apos E1, canonico 2026-05-15) =======
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
    ("01", "A"),
    ("02", "A"),
    ("03", "C"),
    ("04", "B"),
    ("05", "B"),
    ("06", "B"),
    ("07", "A"),
    ("08", "E"),
    ("09", "A"),
    ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "A"),
    ("13", "A"),
    ("14", "A"),
    ("15", "B"),
    ("16", "B"),
    ("17", "E"),
    ("18", "E"),
    ("19", "A"),
    ("20", "E"),
    ("21", "B"),
    ("22", "E"),
    ("23", "D"),
    ("24", "B"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "E"),
    ("27", "C"),
    ("28", "A"),
    ("29", "B"),
    ("30", "D"),
  )),
))
