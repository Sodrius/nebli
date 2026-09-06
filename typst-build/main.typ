// ================================================================
// MAIN.TYP -- biotec-02-intestinos | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Intestinos: organização, renovação e absorção",
  "Biologia Tecidual",
  (
    ("Disciplina", "Biologia Tecidual II — Sistema Digestório"),
    ("Onde estudar", "Junqueira & Carneiro, Histologia Básica, 13ª ed. — Aparelho Digestivo · Kierszenbaum, Histologia e Biologia Celular — Segmento Digestivo Inferior · Wheater's, Histologia Funcional · Sobotta, Atlas de Histologia"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#set-etapa("Sumário")
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O plano do tubo e a superfície que ele multiplica", (
      "1.1 As quatro túnicas",
      "1.2 Os quatro dobramentos",
      "1.3 Duodeno, jejuno e íleo",
    )),
    ("PARTE II — O epitélio que se refaz por inteiro toda semana", (
      "2.1 O nicho da cripta",
      "2.2 Linhagens e decisão de Notch",
      "2.3 Proliferar, migrar, morrer",
    )),
    ("PARTE III — O epitélio que absorve e o que vigia", (
      "3.1 Digestão terminal na borda em escova",
      "3.2 Lâmina própria e GALT",
      "3.3 O intestino grosso",
    )),
  )),
))

// ======= ETAPA 1 =======
// set-etapa ANTES do etapa-header: o header da pagina resolve o state antes do
// corpo dela, entao a atualizacao feita dentro de `etapa-header` (que roda
// depois do `pagebreak`) so aparece na pagina SEGUINTE. Emitindo aqui, a
// atualizacao fica no fluxo da pagina anterior e a pagina de abertura da etapa
// ja nasce com o header certo. Corrige o bug "header dessincronizado" que o
// auditar_pdf_visual bloqueia.
#set-etapa("Etapa 1 — Texto didático")
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#set-etapa("Resumindo")
#include "resumindo.typ"

// ======= ETAPA 2 =======
#set-etapa("Etapa 2 — 30 objetivas")
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#set-etapa("Etapa 3 — 5 discursivas")
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
#set-etapa("Gabarito — Etapa 2")
#gabarito-page((
  ("Consolidação (Q01–Q08)", (
    ("01", "C"),
    ("02", "A"),
    ("03", "CCEE"),
    ("04", "D"),
    ("05", "CCEC"),
    ("06", "B"),
    ("07", "ECCE"),
    ("08", "E"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "CECC"),
    ("10", "B"),
    ("11", "D"),
    ("12", "B"),
    ("13", "CCCE"),
    ("14", "C"),
    ("15", "E"),
    ("16", "B"),
    ("17", "C"),
    ("18", "CEEC"),
    ("19", "A"),
    ("20", "ECCC"),
    ("21", "D"),
    ("22", "E"),
    ("23", "C"),
    ("24", "B"),
    ("25", "ECEE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "A"),
    ("28", "EECE"),
    ("29", "E"),
    ("30", "EECC"),
  )),
))
