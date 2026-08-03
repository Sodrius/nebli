---
description: Inicia geração de um resumo NEBLI completo (Tema Card → E1 → E2/E3 → compilação → PDF)
argument-hint: <slug> <slide.pdf> [UC1|UC2]
---

Você é o **ORQUESTRADOR + REDATOR + QUESTIONADOR fundidos** (canônico 2026-05-26 — subagentes REDATOR-E1 e QUESTIONADOR estão suspensos por bug de loop; thread principal faz redação direta lendo `ROLES.md` §§ Orquestrador/Redator-E1/Questionador como referência prescritiva).

**Argumentos recebidos:** $ARGUMENTS

**Tarefa:**

1. **Validar entrada.** Parse os argumentos: `<slug>` (ex.: `bioq-17-ciclo-krebs`), `<slide.pdf>` (caminho absoluto ou relativo), `<UC>` (opcional, infere de `banco/aulas_uc01.yml` ou `banco/aulas_uc02.yml` pelo slug). Se algo faltar ou for ambíguo, pergunte com opções numeradas antes de prosseguir.

2. **Leitura canônica obrigatória** (em paralelo):
   - `C:\AI use\nebli\CLAUDE.md` — núcleo prescritivo
   - `C:\AI use\nebli\MEMORY.md` — estado vivo + **§ Diário de revisões** (obrigatório antes de gerar Tema Card)
   - `C:\AI use\nebli\ERROS.md` — § Erros recorrentes (18 itens) + § Feedbacks de processo
   - `C:\AI use\nebli\ROLES.md` — §§ Orquestrador, Redator-E1, Questionador como referência prescritiva
   - `banco/aulas_uc<N>.yml` — confirmar slug existe

3. **Limpar workspace.** `rm typst-build/etapa1.typ typst-build/etapa2.typ typst-build/etapa3.typ typst-build/resumindo.typ typst-build/main.typ` (evita contaminação do resumo anterior — `ERROS.md` erro 3).

4. **Extrair slides.** Rodar `python typst-build/extrair_slides.py <slide.pdf> <slug>` — gera `figuras/<slug>/slide-XX.png` + `MAPA_CONTEUDO.txt`.

5. **Gerar Tema Card** em `arquivos-trabalho/tema-card-<slug>.md` — Seções A (escopo), B (baseline aluno), C (profundidade + distribuição E2), D (Mapa de Confusões inicial), **Seção E (exemplares-âncora)**. Validar com Davi se houver ambiguidade (recorte slide × tema).

   *Antes de redigir o Tema Card,* dar uma passada no índice `## Quando usar` do `EXEMPLARES.md` e escolher os exemplares que vão guiar a voz deste tema. Não tem número certo — sempre as 3 universais (1, 8, 14) e quantos temáticos fizerem sentido para os gestos que o tema vai exigir (abertura, cadeia mecanística, analogia, cálculo, etc.). Para cada exemplar escolhido, anotar em 1–2 linhas: "este exemplar acerta em [gesto/ritmo/escolha]; vou usar isso em [subtópico] adaptando para [como]." Esses pares vão na **Seção E** do Tema Card. É anotação curta (5–15 linhas), não relatório.

   A Seção E serve para reabrir rapidinho ao iniciar cada PARTE da E1 — exemplar lido só uma vez no começo perde frescor conforme a redação avança.

6. **Redigir E1 (rascunho)** seguindo as regras do `redator-e1.md`. Gravar via heredoc `etapa1.typ` e `resumindo.typ`. Aplicar filtro de utilidade pedagógica de figuras (regra 15). Reportar paridade de densidade entre PARTES (regra 14).

6b. **Seleção de cards + passe de aprofundamento da E1 (CANON 2026-07-10, ANTES da E2).** Rodar a seleção de cards (passo 11a-c abaixo, com Anki vivo OU seleção offline do export) para descobrir o que o campo trata como núcleo. Depois, fazer o **passe de aprofundamento**: voltar na E1 e injetar **≈1 conteúdo extra mecanístico por subtópico** (~9-12 no total), colado a um mecanismo já aberto — o **slide regula O QUE entra, o AnKing/bibliografia regula ATÉ QUE PROFUNDIDADE**; se não há onde encaixar, não encaixa. Muitos aprofundamentos são induzidos por bons cards do AnKing (que vão pro deck-aula). Detalhe em `CLAUDE.md` § Aprofundamento da E1 + `ROLES.md` § Redator diretriz 17 + `FLASHCARDS.md` § Loop Card→E1. **Só depois de aprofundar a E1, seguir para a E2** (assim a E2 já cobra o extra). Sem Anki vivo: o aprofundamento nasce do mapa de cobertura offline + blueprint + bibliografia.

7. **Redigir E2/E3** seguindo `ROLES.md` § Questionador. Para **Q01-Q30** reportar quadro completo de ratio de paridade (gate hard banda dupla 0.80-1.25 — canônico 2026-05-29).

8. **Compilar** via `python typst-build/gerar_main.py <slug>` → `python typst-build/precompile-check.py` → `cd typst-build && typst compile --root .. --font-path ../fonts main.typ <SLUG>.pdf` → `python typst-build/auditar_pdf.py <SLUG>.pdf`.

9. **Mover + compactar (CANÔNICO 2026-07-03, reforçado 2026-07-07).** Mover para `resumos-gerados/<SLUG>.pdf` APENAS se ambos auditores passarem. **Logo em seguida, SEMPRE gerar a cópia leve** (não é opcional): `cd typst-build && python comprimir_pdf.py "../resumos-gerados/<SLUG>.pdf" "../resumos-gerados/leves/<SLUG>.pdf"`. Política sidecar: o master fica full-res; a cópia leve (~2-3 MB) é a que se abre no celular / sobe pro Drive. Reportar os dois tamanhos no relatório final e, quando o Davi estiver via remote-control, enviar a cópia leve pelo chat (`SendUserFile`).

10. **Relatório final** ao Davi: erros recorrentes checados (`ERROS.md` § Erros recorrentes, 18 itens), figuras descartadas pelo filtro (regra 15), **paridade Q01-Q30 em banda dupla 0.80-1.25** com direção quando FAIL, densidade por PARTE, tabela auditável de figuras (Figura | PARTE | Origem | Mecanismo | Largura), tabela subtópico→questões, e o **Índice de completude (CANON 2026-07-10) — 3 notas de 0 a 10 com 1 linha de justificativa cada: E1×slide (meta 8-9, a E1 vai um tiquinho além do slide), E2×E1 (meta ≥8), Cards×E1 (meta ≥7)** (ver `ROLES.md` § Índice de completude). Incluir literalmente: **Fontes → E1: X/Y conceitos relevantes incorporados** e **E1 → cards: X/Y conceitos nucleares COBERTOS**.

11. **Curadoria AnKing (adicionar cards ao deck).** Depois de mover o PDF, rodar o fluxo de `flashcards/CURADORIA-ANKING.md` (dirigido por conceito) para este `<slug>`:

    a. **Checklist semeada da E1.** Antes da busca, fazer um passe leve **Fontes→E1** contra Tema Card/slide, banco FMUSP já filtrado e blueprint já consultado; corrigir somente ausências relevantes dentro do recorte. `python flashcards/scripts/gerar_checklist.py <slug>` → escreve `arquivos-trabalho/checklist-<slug>.tsv` pré-preenchido (termo-notas + siglas por PARTE). Dar **uma passada leve** completando os `<EN?>` (termo em inglês, o AnKing é em inglês), fundindo redundâncias e acrescentando subtópico que a E1 ensina mas não marcou como termo-nota. Fonte-verdade = E1 redigida + Seção B do Tema Card.

    b. **Camada 1 (recall, puxa de todos os recursos).** `python flashcards/scripts/buscar_tags_lote.py arquivos-trabalho/checklist-<slug>.tsv --md` → classificar CANDIDATA/RUÍDO. Conceito sem tag sai como LACUNA declarada.

    c. **Pool + pré-filtro (menos tokens).** `extrair_cards_anking.py "<tags candidatas>" --slug <slug>` (usa cache do dia; `--forcar` re-extrai) → depois `python flashcards/scripts/prefiltrar_pool.py <slug>` → `anking-pool-<slug>-slim.md` com **PROVÁVEIS-BONS** (ler a fundo, keep/drop) e **RUÍDO-PROVÁVEL** (passar o olho, resgatar falso-positivo). Camada 2 lê o slim, não o pool cheio.

    d. **Matriz conceito×card + gap-analysis.** Cada kept aponta um id de conceito. Status por conceito: COBERTO / PARCIAL / LACUNA / **PENDENTE-GERADO** (0 card real bom → enfileirado pra card NEBLI gerado numa **sessão futura de calibração** — NÃO gerar agora, ver memória `calibrar-antes-de-gerar-cards`). Toda LACUNA/PARCIAL/PENDENTE **aponta a fonte**. Conceito **nuclear** só fecha em **COBERTO** por card real (AnKing, externo ou NEBLIcard); questão da E2 não conta, e os demais estados são intermediários para nuclear. Gravar `flashcards/curadoria/<slug>.md` + `<slug>-curado.json` (alvo 30–50; `guids_kept` pode ser `{"guid","conceito","motivo"}` pra auditar).

    e. **Prova de cobertura.** `python flashcards/scripts/verificar_cobertura_anking.py <slug>` → X/Y COBERTOS + escreve `arquivos-trabalho/cobertura-<slug>.json` (fila pendente-gerado). Corrigir se acusar erro; levar a linha pro `_INDEX.md`.

    f. **Aplicar cards reais.** `python flashcards/scripts/aplicar_curadoria_anking.py <slug>` (marca `NEBLI::<slug>`, dessuspende, atualiza `_INDEX.md`). AnkiConnect fora do ar → recibo manual, não trava.

    g. **Ritmo do deck.** `python flashcards/scripts/configurar_ritmo_anking.py` (fixa 25 novos/dia, 150 revisões/dia — idempotente).

    Reportar no fim: #cards dessuspensos + **cobertura X/Y** + **fila pendente-gerado** + lacunas→fonte. (A geração/injeção de cards cloze NEBLI fica FORA deste pipeline até a sessão de calibração.)

Se em qualquer etapa algo falhar, pare e reporte — não improvise.

### Gate deck-aula completo (obrigatório)
Antes de escrever a E2 e antes de mover o PDF, o deck-aula precisa fechar no contrato `deck-aula-v2`: E1 atomizada por âncora literal; busca AnKing card-a-card por fato; cards AnKing/external primeiro; autoria apenas com rejeição documentada; e enriquecimentos Step 1 já incorporados na E1. Rode `python flashcards/scripts/gate_deck_aula_completo.py arquivos-trabalho/matriz-deck-aula-<slug>.json --verify-anki`. Exit diferente de zero bloqueia E2, PDF e exportação. `PENDENTE-GERADO` não é estado de ship: a lacuna deve virar card e entrar no deck antes de fechar.
