# Estado atual

Plano [08/10](PLANO-AJUSTES-ANKI-2026-10-08.md) **aprovado** por Davi em 08/10/2026 (F-20261008-CLAUDE-01). Execução **contínua** na ordem abaixo até Davi mandar parar. Versão pré-aprovação deste arquivo: `arquivo/2026-10-08-execucao/`.

## Como usar este arquivo (toda sessão)

1. Ler **Retomar aqui**: é o ponteiro exato de onde a sessão anterior parou.
2. Abrir o `ESTADO.md` da corrida apontada (checklist detalhado da leva/aula) e continuar do primeiro item não marcado.
3. Ao concluir **cada etapa** (não só no fim da sessão): marcar no `ESTADO.md` da corrida, atualizar Retomar aqui e, se mudar de aula/leva, a Fila.
4. Ao fim de cada deck/leva: escrever no chat e em **Perguntas para Davi** as dúvidas objetivas; seguir sem esperar, com a suposição registrada.
5. Feedback novo de Davi: FEEDBACKS (literal) → MEMORY (preferência) → aplicar já; registrar em Feedback incorporado.
6. **Davi usa o Anki enquanto o executor trabalha (F-20261008-CLAUDE-02): isso não bloqueia.** Preparar fora do Anki e aplicar em lotes curtos mesmo durante a revisão dele; nunca alterar a nota em exibição (`guiCurrentCard`) nem seus irmãos (adiar só essas); não mexer na tela dele; escrita com `sync=False` enquanto ele revisa e sync quando estiver ocioso ou no fim da sessão; readback após cada lote. Protocolo `nebli.decks.escrita()`.

## Retomar aqui

- **Leva:** 1 quase concluída (08/10, ~15h10). 137 notas corrigidas, 20 cards dessuspensos, readback sem divergência; recibos em `arquivos-trabalho/leva01-2026-10-08/lotes/`. Checklist: `arquivos-trabalho/leva01-2026-10-08/ESTADO.md`.
- **Em andamento ao parar:** regeneração dos Tabs no novo estilo (prosa, sem "1) 2)") — `tab-gerar3.log`. Conferir com `python3 -m nebli.explicacoes resumo` nas aulas tocadas e rodar de novo o mesmo comando se cair.
- **Falta na leva 1:** (a) Tabs acima; (b) sync com o AnkiWeb (`ANKI-SYNC-PENDENTE` existe: chamar `nebli.decks.sync_se_ocioso`); (c) `REVISAO.md` da leva; (d) registrar no Browser real que a ordem da aula ficou padrão (mudança em `nebli/anki_addon.py`, recarrega sozinha) e perguntar a Davi se agora aparece certa.
- **Próximo:** 1b = regerar decks-aula da **UC03 P3** (aulas com slide no Drive), depois UC03 P2, UC08 P2, depois o plano. Menos autorais; dica só em poucos clozes ambíguos.
- **Pendências registradas:** cards de conexão da FI09 propostos (`proposta-conexoes-fi09-spec.py`) aguardam migração de fontes (gate); GR02 falha só no inventário atômico (leva 5); retiradas de cards (tag `NEBLI::retirado::*`) ainda não refletidas nos specs; 207 notas UC08/UC03 com imagem genérica compartilhada → revisão por aula.

## Fila da campanha (ordem do plano)

Ordem vigente (F-20261008-CLAUDE-05): 1 → 1b → 1c → 1d → demais conforme plano.

Estados: `pendente` · `preparando` · `em produção` · `em revisão` · `entregue` · `aguardando fonte` · `adequado (reaproveitar)`.

| # | Leva / aula | Escopo | Estado |
|---|---|---|---|
| 1 | Comentários médicos (88 vivos) + famílias | Ler todos (inclusive CORRIGIDO), agrupar por família, corrigir card + semelhantes, dessuspender corrigidos, `CORRIGIDO, DD, MM, YY.`; Tab dos alterados; poucos cards de conexão de exemplo; regras aprendidas → MEMORY/lint/gates | preparando |
| 1b | **UC03 P3 — regerar decks-aula** (aulas com slide no Drive) | Pedido F-20261008-CLAUDE-05: pipeline completo, menos autorais, dicas em poucos clozes ambíguos, ordem real no Browser | pendente |
| 1c | **UC03 P2 — regerar decks-aula** | idem (inclui as reconstruções Codex de Morfologia, Edema, Ambiental; GR02/PR02 preservadas e corrigidas) | pendente |
| 1d | **UC08 P2 — regerar decks-aula** (Secreção gástrica, Digestão e absorção) | idem | pendente |
| 2 | UC08 Histologia — Estrutura do estômago; Intestinos | Revisão integral por aula: cobertura vs slides/fontes, redundância, escrita, imagens, cores, ordem, Tab | pendente |
| 3 | UC08 Anatomia — Esôfago/estômago/ID; Intestino grosso/canal anal; Vascularização | idem | pendente |
| 4 | UC08 Fisiologia — Motilidade I, II; Secreção gástrica; Digestão e absorção | idem | pendente |
| 5 | UC03 GR02 (diabetes); PR02 (correlação pato-radio 2) | Preservar e corrigir | pendente |
| 6 | UC03 reconstruções: Morfologia bacteriana; Edema e congestão; Patologia ambiental; Biologia geral dos fungos | Substituir versão Codex com backup e mapa antigo→novo | pendente |
| P | Pipeline (em paralelo às levas) | Pesquisa AnKing delimitada; correção no Anki → specs (sem regressão em rebuild); gate de pacote atualizado (hash/conteúdo, não só existência); heatmap; verificação de ordem; renomeação de slides no Drive | pendente |
| 7 | Geração 2026 — UC03 (todas as aulas disponíveis) | Inventário vivo por aula → produção aula a aula | pendente |
| 8 | Geração 2026 — UC19 | idem (FA01 refazer conforme F-20261006-CODEX-04) | pendente |
| 9 | Geração 2026 — UC21 | idem | pendente |
| 10 | Geração 2026 — UC02 | idem (apostila de lâminas no Drive) | pendente |
| 11 | Geração 2026 — UC01 | idem | pendente |

Critério de conclusão (Davi): bons decks-aula **e** pipeline reproduzível que gere deck a partir do material disponível.

## Auditoria Codex — 08/10, Browse e qualidade

Auditoria concluída; **campanha/decks ainda não concluídos**. [Evidências e limites](arquivos-trabalho/auditoria-browse-2026-10-08/REVISAO.md). Recibos confirmam 137 notas corrigidas e 20 cards dessuspensos. Vivo: 1.179 cards médicos físicos. Defeitos comprovados: Edema 30/67 sem Tab; Ambiental 27 notas/36 cards com Extra genérico e duas notas literalmente duplicadas; Morfologia sem perguntas para distinções dos slides 10/37; Fungos com duas notas na posição 10. Gates de fechamento pendentes, incluindo incompatibilidade de esquema na corrida antiga de Ambiental. Não confundir todas as Tabs de estilo antigo com erro de conteúdo.

**Browse aplicado:** J alterna suspensão com foco na tabela; coluna Suspenso mantém indicação mesmo com bandeira; Ordem da aula padrão e cabeçalho coerente. 123 cards AN01 verificados na ordem das tags, captura real e teste Qt do atalho; sete testes unitários aprovados. Isso não certifica ordem pedagógica de todas as aulas. Nenhum card/conteúdo/suspensão/bandeira alterado. Fila e executor Claude preservados; incorporar achados no fechamento da leva 1 e nas reconstruções autorizadas.

## Perguntas para Davi

Nenhuma ainda. (Formato: data · deck · pergunta objetiva · suposição adotada enquanto isso.)

## Feedback incorporado nesta campanha

- 08/10 F-20261008-CLAUDE-01: plano aprovado; execução contínua; perguntas ao fim de cada deck.
- 08/10 F-20261008-CLAUDE-05: fila UC03 P3 → UC03 P2 → UC08 P2 → plano; ordem do Browser real; menos autorais; dica só em poucos clozes ambíguos.
- 08/10 F-20261008-CLAUDE-02: Davi usa o Anki durante a execução; aplicar em lotes sem tocar a nota na tela; sync só quando ocioso.

## Registro das levas

Cada leva: alcance; status; evidência (`receipt.json`, `verification.json`, `REVISAO.md`); cards corrigidos/dessuspensos (IDs no recibo); entregue em; perguntas; pendências.

_(vazio — leva 1 em preparação)_

## Inventário de referência (leitura de 08/10, antes da execução)

1.178 cards médicos, 1.025 notas, 88 comentários médicos (todos relidos vivos nesta sessão). Leitura em `arquivos-trabalho/plano-ajustes-2026-10-08/` e `arquivos-trabalho/leva01-2026-10-08/comentarios-before.json`. Não é certificação científica dos cards.
