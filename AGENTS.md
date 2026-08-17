# NEBLI — entrada universal

Este arquivo é a entrada obrigatória para qualquer agente. Não use histórico de conversa, memória pessoal, decks anteriores ou documentos legacy para completar regras do pipeline.

## Ordem obrigatória de leitura e execução

1. Leia `config/pipeline.json` — autoridade mecânica.
2. Leia `docs/canon/EXECUCAO.md` — ordem operacional e definição de pronto.
3. Leia `docs/canon/E1.md` — contrato pedagógico e visual da E1.
4. Antes de redigir a E1, execute integralmente a calibração exigida por `docs/canon/E1.md`: `EXEMPLARES.md`, `ANTI-EXEMPLARES.md`, documentos didáticos aplicáveis e pelo menos dois exemplares UC02 adequados.
5. Inventarie todas as fontes da aula e congele a matriz `source_to_e1_matrix` antes do primeiro parágrafo da E1.
6. Produza e revise a E1 em quatro passadas. A E1 precisa estar congelada e aprovada antes da seleção de cards.
7. Somente depois leia `FLASHCARDS.md` e `EXEMPLARES-CARDS.md` para construir o ganho da aula, o núcleo de retenção e os cards.
8. Gere e audite o `.apkg` conforme `CLAUDE.md`.

`docs/legacy/`, scripts históricos, `MEMORY.md`, AnKing, Companion e decks anteriores não participam de uma corrida normal.

## Separação de responsabilidades

- `docs/canon/E1.md`: como a aula é ensinada na E1.
- `EXEMPLARES.md` e `ANTI-EXEMPLARES.md`: calibração da voz e do gesto didático da E1.
- `FLASHCARDS.md`: o que merece virar card e como o card deve ser.
- `EXEMPLARES-CARDS.md`: exemplos/anti-exemplos de cards.
- `CLAUDE.md`: caminho técnico, scripts e artefatos.
- `config/pipeline.json`: invariantes mecânicos.

A política de flashcards nunca pode reduzir a cobertura da E1. Pré-requisitos, revisões e contexto podem ser excluídos do deck, mas continuam na E1 quando necessários para ensinar a aula do zero.
