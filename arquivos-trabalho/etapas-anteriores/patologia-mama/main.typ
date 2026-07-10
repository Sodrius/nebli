// ================================================================
// MAIN.TYP -- patologia-mama | Gerado por gerar_main.py (modo sem_e2)
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Patologia da mama — do nódulo ao laudo",
  "Patologia · Ciclo clínico",
  (
    ("Disciplina", "Patologia — Aparelho reprodutor feminino"),
    ("Onde estudar", "Robbins Cap. 23 + Respostas do Relatório da prof."),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Da cirurgia ao patologista", (
      "1.1 Procedimentos cirúrgicos da mama",
      "1.2 Protocolo de envio e pintura de margens",
      "1.3 Descrição macroscópica e estadiamento T",
    )),
    ("PARTE II — Carcinoma mamário invasivo", (
      "2.1 Achados macro e micro do CDI",
      "2.2 Imuno-histoquímica — RE/RP/HER2/Ki-67",
      "2.3 Subtipos moleculares e graduação",
    )),
    ("PARTE III — Pós-neoadjuvância e laudo", (
      "3.1 Mastectomia após quimioterapia neoadjuvante",
      "3.2 Resposta patológica e índice RCB",
      "3.3 Arquivamento e cadeia de custódia",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Discursivas ancoradas em imagem macro/micro do relatório",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"

// ======= ETAPA 3 =======
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"
