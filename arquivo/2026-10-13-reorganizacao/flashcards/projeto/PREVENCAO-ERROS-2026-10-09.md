# Plano para os erros não voltarem — 09/10/2026 (F-20261009-CLAUDE-02/03)

Revisão de completude e fidelidade de 7 decks já feitos (Fungos, Morfologia bacteriana, Edema, Patologia ambiental, PR02, GR02, FI09).
Cada erro abaixo foi encontrado de fato; ao lado, o que impede a repetição. "Gate" = falha automática em `python3 -m nebli.gates`.

| # | Erro encontrado | Onde | Causa | Prevenção |
|---|---|---|---|---|
| 1 | Material da aula ignorado: PDFs II/III, aula de outra professora, palavras-cruzadas | Morfologia (II com respostas da lista), Edema II, Ambiental II (mudanças climáticas) | Só o slide do Drive pessoal foi aberto | **Gate `class_folder`**: `fontes.json` › `pasta_turma` (drive da turma) e todo arquivo lido ou descartado com motivo |
| 2 | Conteúdo dado sem card ("menção no verso") | Fungos (~30 ideias só no Extra), FI09 (limiar contrátil, EES, defecação voluntária) | Cobertura agrupada por lâmina contava o Extra | **`nebli.inventario`**: um item por ideia, cada um ligado ao card que o pergunta; gate `inventory` |
| 3 | Card de coisa não dada | Fungos (aflatoxina→CHC, α-amanitina), Ambiental (9 de CO, pneumoconiose), Edema (GNPE, estenose mitral), PR02 (AST/ALT, AFP) | Seleção por tema em vez de por item; HY puxava o card | **Gate `orphans`**: todo card aponta para item do material de base (conexão só declarada) |
| 4 | Material NEBLI usado como base | Edema (vinheta e GNPE vieram da apostila "etapas 1–3") | Arquivo na pasta da aula parecia exercício | Regra no MEMORY; `fontes.json` registra o que é NEBLI; E1 só confirma |
| 5 | Extra do AnKing apagado por texto genérico ou "on slide N" | Morfologia, Ambiental, Edema | `ak(..., extra=...)` substitui o Extra | Usar `extra_add`; lint já reprova metacomentário em autoral (estender ao AnKing é a próxima melhoria) |
| 6 | Card com nid AnKing e texto trocado | Morfologia (mycoplasma, ribossomo, flagelo) | `text=` sobre um `src` qualquer | Trocar para o AnKing real; texto próprio só como autoral |
| 7 | Lâmina e imagem erradas | Edema (card de histologia com o diagrama; numeração deslocada) | Numeração herdada sem ver as lâminas | Ver as lâminas (montagem) antes de numerar; gate `imagens_vistas` |
| 8 | Canal contradiz a aula | FI09 (Medicosis: onda lenta não contrai) | Extra escrito a partir do vídeo | Aula e prova prevalecem; registrar em `calibracao` |
| 9 | Teto de autorais empurrando para fora a aula | Fungos, Ambiental, FI09 | Teto de 15% sem considerar acervo inexistente | `COMPLETUDE_EXCEPTIONS` com busca registrada; o teto continua valendo onde o AnKing cobre |
| 10 | Card novo liberado em deck pós-prova | (evitado) Morfologia, Edema, Ambiental | Delta cria cards ativos | `decks.apply` suspende os novos quando o deck está suspenso |

## Sequência obrigatória por aula (resumo para o executor)
1. Pasta da turma inteira + Drive pessoal + monitoria (arquivo único por prova) + apostila de veteranos + provas + livro + canal → `fontes.json` com `pasta_turma`.
2. Ver todas as lâminas (montagem) → `inventario.py` → `python3 -m nebli.inventario <corrida>` **antes** de escolher cards.
3. Buscar no AnKing por texto e pelas tags da seção (FirstAid/NinjaNerd/Bootcamp) → outros acervos → autoral curto só para o que falta.
4. `build.py --delta` → lint → delta → suspender novos se o deck estiver suspenso → Tab → render e leitura → `nebli.inventario --instalado` → revisões → gates → .apkg.

## Pendências conhecidas (não fingidas)
- YouTube bloqueou transcrições em 09/10: Shomu (Fungos) e um canal de poluição (Ambiental) não lidos — `fontes.json` › `shomu_pendente` / `canal_pendente_0910`.
- Videoaulas assíncronas (Edema 212 MB, Ambiental 100 MB) e bibliografias complementares da Ambiental/Edema não lidas — `turma_descartados` marca PENDENTE.
- Varredura de completude das outras 8 aulas da UC08 com este mesmo procedimento.
