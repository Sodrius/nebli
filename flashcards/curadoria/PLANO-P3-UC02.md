# PLANO — Deck-prova P3 UC02 (rodar em conversa NOVA)

> Handoff 2026-07-12. Davi pediu o **deck-prova da P3 completo, sério e organizado** — o primeiro deck "de verdade" (os anteriores foram TESTE e não contam). Rodar numa conversa separada (a de origem ficou longa). Ritmo escolhido: **curar as 8 de enfiada e entregar o P3 fechado** (menos checkpoints).

## Escopo — 8 aulas (todas com E1; imuno e depuração ficam FORA, sem resumo)
Prova pelo cronograma `cronogramas/cronograma UC2 2026 v 1 de julho.pdf` (coluna "Cai em" → P3 = Histo/Anato/Embrio; 16/jul). E1 = fonte-verdade do gate B2 (typ no workspace OU PDF no Drive/resumos-gerados).

| # | Aula | Componente (Drive) | E1 |
|---|---|---|---|
| 1 | Anatomia circ/linf I (pt1) | Anatomia / 05 | `arquivos-trabalho/etapas-anteriores/anato-05-circulatorio-linfatico-I/etapa1.typ` |
| 2 | Anatomia circ/linf I (pt2) | Anatomia / 05 | Drive PDF "Sistema circulatório e linfático pt2 - Etapas 1 a 3" (+ typ `anato-05-sistema-linfatico`) |
| 3 | Anatomia circ/linf II | Anatomia / 06 | Drive PDF "Sistema circulatório e linfático II - Etapas 1 a 3" |
| 4 | Histologia dos vasos | Bio celular/tec / 08 | `.../histo-09-vasos-sanguineos-linfaticos/etapa1.typ` |
| 5 | Tecido nervoso | Bio celular/tec / 09 | `.../histo-10-tecido-nervoso/etapa1.typ` |
| 6 | Histologia dos órgãos linfáticos | Bio celular/tec / 10 | `.../histo-11-orgaos-linfaticos/etapa1.typ` |
| 7 | Embriologia I | Bio celular/tec / 11 | resumos-gerados/"Embriologia I - Etapas 1 a 3- ML.pdf" |
| 8 | Embriologia II e III | Bio celular/tec / 12 | resumos-gerados/"Embriologia II e III - Etapas 1 a 3 - ML.pdf" |

**FORA (sem E1, ficam sem resumo por decisão do Davi):** Distúrbios da imunidade (imuno-01), Funções de depuração (bioq-25).

## Processo por aula (SÉRIO — o padrão novo)
Para cada uma: busca AnKing por conceito (`descobrir_cards_por_conceito`) → Camada 2 keep/drop (perfil decoreba onde couber) → **gate B2** contra a E1 (nada de card órfão) → **NEBLIcards indistinguíveis** pras lacunas tipo-a (rubrica `CARD-MIRROR-RUBRICA.md`: imagem-mãe de irmão + crédito casado, verso telegráfico, EN) → **Revisor-completude** (agente Sonnet, 3 notas + patches) → aplicar em `NEBLI::UC02::P3::<Componente>::<Aula>`. Carga viável por aula (banda peso×rendimento, `FLASHCARDS.md`). AnKing intocado — só cópias no NEBLI.

## Entrega
- **Um `.apkg` por aula** → sobe pra pasta da aula no Drive (`subir_drive.py`, ver `DRIVE-ESTRUTURA.md`), nomeado `<Aula>.apkg`. **Componente, não prova** (o Drive é por componente).
- **Um `P3.apkg` combinado** (o deck-prova inteiro) — o Anki é por prova; salvar o combinado onde o Davi achar (sugerir pasta `UC02/` raiz ou uma pasta "Decks Anki"). Confirmar o destino com ele.
- Reportar: completude (3 notas E1×slide, E2×E1, cards×E1) + carga por aula + o que virou NEBLIcard.

## ⚠ Achado de recon (2026-07-12) — P3 é NEBLIcard-heavy, não curadoria
Probe do AnKing pra Tecido nervoso (histologia): tipos de neurônio=0, transporte axonal=0, astrócito/BHE=1, sinapse=1, satélite=0; cobre bem só o ângulo Step-1 (crista neural=38, glia, mielina). **Conclusão:** as aulas de **histologia (vasos, nervoso, linfoide) e anatomia (circ/linf I-pt1, I-pt2, II)** têm cobertura AnKing fraca no ângulo FMUSP → o deck sério dessas é **majoritariamente NEBLIcard autoral gerado da E1** (curadoria do AnKing rende pouco). Só **Embrio I/II-III** têm boa curadoria AnKing (derivados high-yield). 

**Implicações pro processo (rodar por aula, em sessão fresca):**
1. **Recon primeiro (barato):** probe de cobertura por conceito → decide a mistura curar-vs-gerar antes de ler pools (economiza tokens).
2. **Histologia/anatomia = NEBLIcards da E1 + image occlusion dos slides** (a prova é prática — precisa de imagem real/esquema). Ver brain-dump do Davi: "atlas de anatomia pra cloze de imagem" + "puxar imagens do slide". Decidir com Davi: image occlusion do slide? deck externo de anatomia/histologia pra filtrar? cloze puro?
3. **Embrio = curadoria AnKing normal** (bem coberto).
4. Carga: NEBLIcard-heavy é autoral pesado (~25-35/aula) → orçar; não cabe em thread única.

## Autoavaliação de processo/tokens (2026-07-12, pedido do Davi)
- **#1 Uma aula por contexto limpo** — curar 8 numa thread longa faz cada aula reler ~30k linhas; custo explode + context-bleed. Rodar cada aula em sessão fresca (lê só este plano + regras).
- **#2 Recon barato antes de pool** — o probe de cobertura por conceito (findNotes count) custa quase nada e evita ler pools enormes de aulas mal-cobertas.
- **#3 Histologia/anatomia FMUSP ≠ AnKing** — não gastar tokens tentando curar o que o AnKing não tem; ir direto pro NEBLIcard da E1 com imagem do slide.

## Decisões do Davi (2026-07-12) — como executar
- **Execução: uma aula por SESSÃO FRESCA** (lê só este plano + regras, não threads longas). Ordem sugerida: **Embrio I → Embrio II-III** (curadoria AnKing, fáceis, firmam o template) → **histologia (nervoso, vasos, linfoide)** com image occlusion → **anatomia (circ/linf I-pt1, I-pt2, II)** (mais autoral).
- **Cards visuais (histo/anato) = image occlusion dos slides.** Teu Anki já tem o note type **`IO-one by one (AnKing Step Deck / AnKingMed)`** com **5 exemplos** — estudar esses 5 primeiro pra aprender a estrutura. Slides em `figuras/<slug>/` ou no Drive (pasta da aula).
- **Calibrar a geração de IO via card-mirror:** gerar alguns cards de image occlusion + o discriminador tenta adivinhar qual é meu vs AnKing → calibro a geração enquanto aprendo pras próximas (mesmo loop de `CARD-MIRROR-PLANO.md`, agora pra IO).
- **Buscar decks externos + repos GitHub, generosamente** (agora e sempre que histo/anato/algo for AnKing-fraco): decks de histologia/anatomia prontos pra filtrar os bons; repos que ajudem em qualquer parte do pipeline (image occlusion, AnkiConnect automation, geração de cards). Curar o que prestar, adaptar.
- **Foco: um deck BOM** — cobrir o necessário, com qualidade. Não é volume; é o Davi conseguir estudar e passar na prova (prática + teórica) + base pro Step 1.
- Já feito nesta sessão: checklist de **Tecido nervoso** (`arquivos-trabalho/checklist-histo-10-tecido-nervoso.tsv`, 28 conceitos) + recon de cobertura AnKing (fraca no ângulo histológico).

## PROGRESSO (2026-07-12, sessão de IO) — máquina de image occlusion PRONTA
- **card-mirror endurecido para IO** (`.claude/agents/card-mirror.md` Parte B): geometria das caixas, fonte da imagem, Header, Extra, higiene de asset, protocolo de abrir a imagem.
- **Pipeline IO:** `flashcards/scripts/io_from_slide.py` (imagem limpa rotulada → OCR tesseract por+eng, upscale, clustering "um rótulo=uma caixa" → campo I0 + preview) e `io_apply.py` (storeMediaFile + addNote). Note type `IO-one by one` = **1 card revela as N oclusões uma a uma** (não N cards).
- **Loop adversarial IO convergiu em 2 rodadas** (rubrica em `flashcards/CARD-MIRROR-RUBRICA.md` § IMAGE OCCLUSION): fixes = imagem atlas EN da web + caixas OCR justas + **nome de arquivo hasheado idêntico em Image/Extra** + **Extra vazio**. Card de neurônio passou como AnKing nativo (conf 91).
- **Fonte de imagem (decisão Davi 2026-07-12):** IO usa **imagem limpa rotulada da web** (atlas/Blausen/OpenStax/Wikimedia) como DEFAULT — melhor que o slide 4-em-1 do professor. Slide só quando a figura específica dele for cobrada.
- **Dependências instaladas:** tesseract (UB-Mannheim) + `por.traineddata` em `~/tessdata` (via `TESSDATA_PREFIX`), `pytesseract`.
- **Infra observada:** o que serve `localhost:8765` nesta máquina é o **Anki DESKTOP** (não há container `anki-nebli`). Rodar `anki.exe` para subir a porta. Docker daemon separado.
- **Recon AnKing feita (contagem por área):** Embrio ~610 (curar) · histo nervoso 26-48 / vasos 32 / linfoide 15 (NEBLIcard+IO) · anato circ/linf 125 clínico Step-1 (IO dos slides/atlas).
- **1 card IO real** aplicado em `NEBLI::UC02::P3::Bio celular e tecidual::Tecido nervoso` (tag `NEBLI::io-calibracao`, nota 1783893211477).
- **FALTA:** curar as 8 aulas (recon feita; falta pool→keep/drop→gate B2→gerar→revisor-completude→apply→apkg→Drive). Meta-avaliação de modelos/processo em `arquivos-trabalho/META-AVALIACAO-P3-IO-2026-07-12.md`.

## Regras que já valem (não reabrir)
- Drive headless via rclone `nebli-drive` (refresh_token; `DRIVE-ESTRUTURA.md`).
- Profundidade elevada + dial `profundidade` + blocos clínicos maiores + bloco roxo (`CLAUDE.md` § Profundidade).
- Estrutura Anki `NEBLI::UC::Prova::Componente::Aula`; AnKing 100% suspenso como referência.
- Bandeiras (vermelha explica+suspende / laranja re-julga / verde exemplar); Ctrl+1 consertado.
