# NEBLI — entrada de toda sessão

1. Ler [README.md](README.md) e [ESTADO-ATUAL.md](ESTADO-ATUAL.md): estado real, leva e próxima ação.
2. Ler [MEMORY.md](MEMORY.md), única memória normativa, e as entradas recentes/pertinentes de [FEEDBACKS](flashcards/projeto/FEEDBACKS.md). Preferências explícitas mais recentes prevalecem; não pedir que Davi reensine a calibração.
3. Ler o [plano ativo](PLANO-AJUSTES-ANKI-2026-10-08.md). Para executar, ler [EXECUCAO-DECK-AULA](flashcards/projeto/EXECUCAO-DECK-AULA.md) e [ACERVOS-REFERENCIA](flashcards/projeto/ACERVOS-REFERENCIA.md).

## Estado e limites

Plano de 08/10 **aprovado** por Davi (F-20261008-CLAUDE-01). Execução contínua na ordem do plano até Davi mandar parar, retomando pela seção “Retomar aqui” do ESTADO-ATUAL. Codex coordena/verifica; Claude executa. Dúvidas ao fim de cada deck, no chat e no ESTADO-ATUAL, sem bloquear; feedback incorporado quando chega. **Davi usa o Anki enquanto o executor trabalha (F-20261008-CLAUDE-02): isso não bloqueia.** Preparar fora do Anki e aplicar em lotes curtos mesmo durante a revisão dele; nunca alterar a nota em exibição (`guiCurrentCard`) nem seus irmãos (adiar só essas); não mexer na tela dele; escrita com `sync=False` enquanto ele revisa e sync quando estiver ocioso ou no fim da sessão; readback após cada lote.

Entrega padrão: somente deck. Tab único com qualidade, sem variante longa/curta. Geração 2026, depois do pipeline validado: UC03 → UC19 → UC21 → UC02 → UC01. Davi decidirá depois a entrada dos decks antigos na rotina; não criar quotas/distribuição diária. E1 existente pode ser fonte; E1–E3 só sob pedido explícito.

## Execução e preservação

- Planejar com fontes reais antes de selecionar cards; explorar Outros/Materiais complementares. Material extra docente/de veteranos é essencial nas matérias anteriores. Bibliografia no Drive; conferir também `bibliografia/` quando houver cópia local.
- Revisar cobertura contra a aula, imagens renderizadas, redação AnKing, redundância, cores/HY, ordem e Tab. Poucos cards de conexão rosas somente com ganho real e construção AnKing.
- Reler todos os comentários médicos, mesmo CORRIGIDO: marcadores antigos podem corresponder a correções ruins. Após correção validada, dessuspender o card se suspenso e anexar `CORRIGIDO, DD, MM, YY.` preservando o texto. Não liberar um deck inteiro por inferência. Suspensão pós-prova é manual.
- Preservar originais, identidades/histórico compatíveis, comentários, marcas e trabalho concorrente. Escrita Anki pelo protocolo `nebli.decks.escrita()` e `arquivos-trabalho/ANKI-ESCRITA.lock`, com backup e leitura posterior. Revisão ativa de Davi não bloqueia (regra acima).
- Rodar `python3 -m nebli.gates <corrida>` na entrega e resolver falhas. Gate aprovado não comprova julgamento visual/semântico. Documentos atualizados não significam implementação. Não fabricar leitura, busca, teste ou revisão por outra IA.
- Toda leva registra o realizado, pendências e feedback aguardado em ESTADO-ATUAL; preferências vão ao MEMORY, falas ao FEEDBACKS e evidências à corrida. Reler mudanças concorrentes antes de gravar.
- Arquivar versões superadas com origem/hash em `arquivo/`; não apagar conteúdo nem ressuscitar cards/decks removidos sem escopo explícito. Não usar filas históricas como ordens atuais.

## Outras rotas

E1: `didatica/E1.md`; E2/E3: materiais preservados, somente sob pedido. Cadernos: `banco/CLAUDE.md` e `ROLES.md`. Typst: `typst-template/CLAUDE.md`. Site/liga/Etimologia: preservar, sem iniciar nesta campanha. Histórico sob consulta em `arquivo/` e `flashcards/projeto/HISTORICO.md`.
