# Flashcards NEBLI — operação canônica

Este diretório contém os dados, scripts e especificações permanentes dos decks. Planos fechados, handoffs e relatórios pontuais não ficam aqui: a decisão durável é incorporada neste arquivo ou no cânone correspondente, e auditorias são regeneradas pelos scripts.

## Mapa de autoridade

- `../FLASHCARDS.md`: filosofia, regras gerais e backlog canônico.
- `CURADORIA-ANKING.md`: método técnico de curadoria e comandos.
- `PESQUISA-BOM-CARD.md`, `CARD-MIRROR-RUBRICA.md`, `EXEMPLARES-CARDS.md` e `ANTI-EXEMPLARES-CARDS.md`: especificação de fabricação e exemplos.
- `GUIA-IMAGENS-CARDS-NEBLI.md`: política visual, fontes e créditos.
- `GUIA-RITMO-E-MODOS.md`: modos de estudo e carga diária.
- `estrutura-deck-mestre.md`: árvore longitudinal do NEBLI.
- `etimologia/`: bootcamp finito de linguagem médica; plano, manifesto, schema e lote zero ativos.
- `curadoria/`, `cards-nebli/` e `deck-cards/`: fontes versionadas por aula.
- `scripts/`: automação, testes e o corpus local `anking-v12-export.txt`.
- `decks-apkg/`: entregáveis; manter pacote completo e pacotes por aula apenas enquanto ambos forem necessários.

## Pipeline atual

1. Extrair da E1 uma checklist de conceitos.
2. Buscar por conteúdo real do card, não apenas pelo caminho de tags.
3. Ler candidato por candidato e decidir `keep/drop`; a categoria PURA foi abolida.
4. Preferir AnKing e fontes externas adequadas antes de criar card autoral.
5. Aplicar o gate absoluto E1↔card: nenhum conceito órfão entra no deck-aula.
6. Produzir card autoral com `build_card.py`, validar com `lint_neblicard.py` e usar card-mirror quando o lote muda de padrão.
7. Auditar cobertura, redundância, relevância visual e crédito; relatórios são saídas regeneráveis.
8. Aplicar de forma idempotente, preferencialmente via staging e com rollback; o AnKing original permanece intocado.

## Regras duráveis de qualidade

- Inglês médico natural por padrão; uma operação de recuperação por card.
- Cloze curto no token de maior valor e Extra telegráfico, sem voz de apostila.
- Imagem específica somente quando melhora reconhecimento ou compreensão; contexto genérico não conta como fechamento visual.
- Image Occlusion usa fonte apropriada, caixas precisas e crédito real.
- Anatomia macroscópica combina esquema espacial e peça real quando houver fonte licenciada disponível.
- O loop card-mirror convergiu em glicogênio em três rodadas e transferiu para pentoses na primeira; a rubrica e o linter são os produtos permanentes desse treino.

## Estado operacional

- O deck P3/UC02 foi reconstruído, exportado e entregue; seu plano de execução foi encerrado.
- Feedback e email permanecem `preview/read-only` por padrão. Mutações exigem flags explícitas; falha de LLM ou SMTP deve preservar comentários e bandeiras.
- Ainda faltam o smoke test real do fluxo de feedback, a validação dos add-ons/hooks e a janela segura baseada no reviewer/revlog.
- Etimologia é o trabalho ativo: produzir o lote zero, validar por sete dias e só então expandir.
- A distribuição dos APKGs ainda precisa escolher entre pacote completo, pacotes individuais ou ambos fora do Git.

## Política de retenção

Manter aqui somente especificações canônicas, fontes, schemas, dados autorais, testes e scripts reutilizáveis. Remover após o fechamento: planos datados, arquivos `CONTINUAR`, logs de rodada, relatórios regeneráveis, backups intermediários e fixtures `_tmp_test`. Caches Python e saídas de build nunca são documentação.

Intermediários de corrida pertencem a `../arquivos-trabalho/`; entregáveis finais pertencem a `decks-apkg/` ou ao armazenamento externo definido para distribuição.
