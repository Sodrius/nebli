# Histórico e preservação da limpeza de 25/09/2026

Esta limpeza reduz contradições e leitura repetida; **não elimina o material de origem**. Foram preservados 17 arquivos integrais antes das alterações, com cópia byte a byte conferida por SHA-256. [Manifesto](../../backups/contexto-2026-09-25/manifest.json). O teste `test_archived_context_preserved_byte_for_byte` verifica tamanho e hash de cada um.

## Onde ficou cada tipo de informação
| Material anterior | Local de uso atual | Preservação integral |
|---|---|---|
| AGENTS / CLAUDE, blocos sobrepostos | Entrada curta → README e referências de qualidade | backups/contexto-2026-09-25/AGENTS.md e CLAUDE.md |
| README, preferências/calibrações v4 e inicial 25/09 | README + FEEDBACKS + BANDEIRAS-E-PROGRESSAO | Mesmo caminho original dentro do backup |
| Feedback espalhado, ERROS e diário MEMORY | FEEDBACKS (casos/retorno esperado) + ERROS (armadilhas técnicas) | ERROS.md e MEMORY.md integrais no backup |
| E1, voz, figuras, matemática e rigor | didatica/E1.md; EXEMPLARES, ANTI-EXEMPLARES e ajustes-finos preservados | CLAUDE/ROLES/ERROS antigos no backup |
| E2/E3, Questionador, RemNote, gates antigos | **Somente histórico**, não leitura normativa de E1 + cards | ROLES.md, CLAUDE.md e .claude/commands/resumo.md no backup |
| Cadernista e outros projetos | ROLES mantém Cadernista; MEMORY aponta planos e pendências | ROLES/MEMORY integrais no backup |
| Runbook, contrato, operação e handoff | Versões consolidadas nos mesmos caminhos ativos | Originais espelhados no backup |
| Fila/decisões de lote | Fila conserva log e propriedade; modo atual corrigido | Snapshot antes desta limpeza no backup |
| Publicação APKG e alias flashcards | Mesmos arquivos com cores/rota corrigidas | Originais no backup |

## O que foi deliberadamente substituído
- `verde = HY literal` → recomendação pessoal de manter, com justificativa de valor futuro.
- referência de até 35 verdes/aula → média desejada ~50, variável, sem cota.
- rosa como nova classificação → azul; não recolorir marcas antigas em massa.
- branco como default pela falta de HY → incerteza real documentada.
- todos AnKing pertinentes mesmo repetidos → busca ampla, seleção sem recuperação equivalente sem ganho.
- lote apenas deck/sem E1 → E1 + cards para novas execuções.
- `/resumo` com E2/E3 e limpeza do workspace → rota atual, sem apagar trabalho concorrente.
- feedback disperso que desaparece na próxima conversa → registro persistente com casos de regressão.

Não foi revogada a pausa de upload APKG. Não foram reclassificados todos os decks, eliminados todos os autorais nem descartadas pendências antigas. Não houve exclusão de cards nesta limpeza.

## Como consultar passado sem reintroduzir erro
Os backups mantêm texto e links **como eram**; referências relativas internas devem ser interpretadas a partir do caminho original no repositório. São evidência histórica, não comandos a executar. Índices v4/25 permanecem nos caminhos antigos para compatibilidade e redirecionam à política atual. V3, pilotos e recibos continuam disponíveis por investigação, não são camadas obrigatórias adicionais.

Conteúdo técnico/editorial extenso não reproduzido na entrada curta continua consultável no papel específico e no backup. Antes de retomar projeto não médico ou ferramenta antiga, ler o backlog/seção correspondente, não supor que “sumiu = resolvido”.

## Verificação e limites
Hash prova preservação dos textos, não preservação automática de todo julgamento pedagógico. A condensação foi revisada contra os pedidos e casos principais; exemplar/ajustes didáticos/fontes/recibos não foram apagados. O próximo teste real E1 + cards pelo Claude deve verificar transferência do contexto e qualidade, além dos testes estruturais locais.

Resultado desta sessão: [RELATORIO-CONSOLIDACAO-2026-09-25.md](RELATORIO-CONSOLIDACAO-2026-09-25.md).
