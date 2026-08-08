---
description: Inicia geração de um resumo NEBLI completo (Tema Card → E1 → E2/E3 → compilação → PDF)
argument-hint: <slug> <slide.pdf> [UC1|UC2]
---

Você é o **ORQUESTRADOR + REDATOR-E1** (canônico 2026-08-07 — QUESTIONADOR volta como subagent Sonnet, ver passo 7). Lê `ROLES.md` §§ Orquestrador/Redator-E1 como referência prescritiva própria.

**Argumentos recebidos:** $ARGUMENTS

**Tarefa:**

1. **Validar entrada.** Parse os argumentos: `<slug>` (ex.: `uc03-02-ferramentas-diagnostico-radiologico`), `<UC>` (opcional — infere de `banco/aulas_uc<NN>.yml` se existir, ou do prefixo do slug; UCs do 2º sem sem banco pegam do `cronogramas/<uc>-*.md`). **Materiais heterogêneos vivem em `slides/<slug>/`** (canon 2026-08-07): qualquer combinação de slide + `perguntas-orientadoras.txt` + `leitura-*.pdf` + `README.md`. Se a pasta não existir ou faltar material, pergunte com opções numeradas antes de prosseguir.

2. **Leitura canônica obrigatória** (em paralelo, caminhos relativos à raiz do repo):
   - `CLAUDE.md` — núcleo prescritivo
   - `MEMORY.md` — apenas estado vivo e preferências atuais; não procurar histórico de resumos ali
   - `ERROS.md` — § Erros recorrentes (18 itens) + § Feedbacks de processo
   - `ROLES.md` — §§ Orquestrador, Redator-E1, Questionador (esta última é a spec do subagent do passo 7)
   - `sobre_mim.md` — contexto do Davi (semestre, estrutura de decks, objetivos Step 1+FMUSP)
   - `banco/aulas_uc<N>.yml` (se UC01/UC02) OU `cronogramas/<uc>-*.md` (UC do 2º sem) — confirmar aula existe

3. **Limpar workspace.** `rm typst-build/etapa1.typ typst-build/etapa2.typ typst-build/etapa3.typ typst-build/resumindo.typ typst-build/main.typ` (evita contaminação do resumo anterior — `ERROS.md` erro 3).

4. **Preparar materiais.** Rodar `python typst-build/preparar_materiais.py <slug>` (canon 2026-08-07 — substitui a chamada direta ao `extrair_slides.py`). O script cataloga todo material em `slides/<slug>/`, delega slide ao `extrair_slides.py` (PNGs + `MAPA_CONTEUDO.txt`), extrai texto de PDFs de leitura, copia perguntas orientadoras e emite `arquivos-trabalho/materiais/<slug>/INDICE.md` com o **papel editorial** de cada peça. Ler o INDICE.md antes de montar o Tema Card.

5. **Gerar Tema Card** em `arquivos-trabalho/tema-card-<slug>.md` — Seções A (escopo), B (baseline aluno), C (profundidade + distribuição E2), D (Mapa de Confusões inicial), **Seção E (exemplares-âncora)**. Validar com Davi se houver ambiguidade (recorte slide × tema).

   *Antes de redigir o Tema Card,* dar uma passada no índice `## Quando usar` do `EXEMPLARES.md` e escolher os exemplares que vão guiar a voz deste tema. Não tem número certo — sempre as 3 universais (1, 8, 14) e quantos temáticos fizerem sentido para os gestos que o tema vai exigir (abertura, cadeia mecanística, analogia, cálculo, etc.). Para cada exemplar escolhido, anotar em 1–2 linhas: "este exemplar acerta em [gesto/ritmo/escolha]; vou usar isso em [subtópico] adaptando para [como]." Esses pares vão na **Seção E** do Tema Card. É anotação curta (5–15 linhas), não relatório.

   A Seção E serve para reabrir rapidinho ao iniciar cada PARTE da E1 — exemplar lido só uma vez no começo perde frescor conforme a redação avança.

6. **Redigir E1 (rascunho)** seguindo as regras do `redator-e1.md`. Gravar via heredoc `etapa1.typ` e `resumindo.typ`. Aplicar filtro de utilidade pedagógica de figuras (regra 15). Reportar paridade de densidade entre PARTES (regra 14).

6b. **Fechar o deck-aula ANTES da E2 (hard gate).** Executar integralmente `flashcards/DECK-AULA-PIPELINE.md`: (a) `gerar_checklist.py <slug>`; fundir redundâncias e classificar todo `REVIEW` em `nuclear | supporting | no_card`; (b) para os selecionados, curar AnKing card a card → procurar outros decks → autoral apenas para a lacuna restante; (c) incorporar na E1 somente aprofundamentos pequenos do mesmo mecanismo que tenham sido realmente aprovados, nunca por quota; (d) fechar `matriz-deck-aula-<slug>.json` com retrieval targets, fonte, visual e `load_profile`; (e) montar somente os cards do manifesto; (f) gate `--verify-anki` quando houver AnkiConnect ou **empacotar `.apkg` + gate `--verify-apkg` no modo offline**. **Exit != 0 bloqueia seguir para E2.**

7. **Delegar E2/E3 ao subagent QUESTIONADOR-SONNET** (canon 2026-08-07 — reverte a fusão de 2026-05-26 pra E2/E3). Chamar `Agent(subagent_type: "questionador-sonnet", ...)` com prompt curto passando: (a) `<slug>`, (b) caminho do Tema Card e da E1 já compiladas, (c) meta explícita "E2 30 obj + E3 5 discursivas, todos os gates hard do stub". O subagent (Sonnet 4.6) grava `typst-build/etapa2.typ` + `typst-build/etapa3.typ` e devolve o quadro completo de ratio Q01-Q30 (banda dupla 0.80-1.25) + tabela subtópico→questões + filtro de integração + gabarito sorteado. **Contingência F9:** se o subagent parar sem disparar tools ou "simular inline", reassumir na sessão principal (Opus) e redigir E2/E3 diretamente seguindo `ROLES.md` § Questionador.

8. **Compilar** via `python typst-build/gerar_main.py <slug>` → `python typst-build/precompile-check.py` → `cd typst-build && typst compile --root .. --font-path ../fonts main.typ <SLUG>.pdf` → `python typst-build/auditar_pdf.py <SLUG>.pdf`.

9. **Mover + compactar (CANÔNICO 2026-07-03, reforçado 2026-07-07).** Mover para `resumos-gerados/<SLUG>.pdf` APENAS se ambos auditores passarem. **Logo em seguida, SEMPRE gerar a cópia leve** (não é opcional): `cd typst-build && python comprimir_pdf.py "../resumos-gerados/<SLUG>.pdf" "../resumos-gerados/leves/<SLUG>.pdf"`. Política sidecar: o master fica full-res; a cópia leve (~2-3 MB) é a que se abre no celular / sobe pro Drive. Reportar os dois tamanhos no relatório final e, quando o Davi estiver via remote-control, enviar a cópia leve pelo chat (`SendUserFile`).

10. **Relatório final** ao Davi: manter os auditores do resumo (erros recorrentes, paridade Q01-Q30, densidade, figuras, subtópico→questões e perguntas orientadoras). Para cards, reportar: **nucleares X/Y cobertos**, cards por fonte (AnKing · outros · autorais), total real/estimado, porte da aula, redundâncias removidas e visuais required pendentes. Não há piso de cards por subtópico.

11. **Pós-fechamento do deck.** O deck já passou o hard gate no passo 6b; aqui não recurar nem acrescentar cards. Rodar `configurar_ritmo_anking.py` (25 novos/dia no topo `NEBLI`), sincronizar e exportar `.apkg` para a pasta da aula quando a infraestrutura estiver disponível. Reportar cards por fonte, nucleares X/Y, total real, porte da aula, card-mirror e sync. Cram usa temporariamente `NEBLI::<UC>::<Prova>` e depois volta ao preset normal.

Se em qualquer etapa algo falhar, pare e reporte — não improvise.
