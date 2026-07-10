# PENDENCIAS.md — ideias a planejar/executar (cards + aprofundamento + deck-mestre)

> Criado 2026-07-10. Backlog focado das ideias que o Davi despejou sobre aprofundamento da E1/E2, cards e o deck-mestre. Complementa `MEMORY.md § Pendências abertas` (que tem o backlog geral). Meta-norte declarada por Davi: **aprender e lembrar a longo prazo.**

## Já EM EXECUÇÃO (canonizado 2026-07-10)

- **Loop card→E1→E2 (aprofundamento por subtópico).** Depois de curar os cards (ou, sem Anki, do mapa de cobertura offline), voltar na E1 e injetar **1 conteúdo extra mecanístico por subtópico** (~9-12 por resumo), pequeno, colado a um mecanismo que o slide já abriu. A E2 é escrita DEPOIS, já cobrando esse extra. **Regra-mestra:** o *slide regula O QUE entra*; o *AnKing/bibliografia regula ATÉ QUE PROFUNDIDADE*. Se não há onde encaixar, não encaixa. Piloto: embrio-gastrulacao-neurulacao (esta sessão).

## A PLANEJAR MELHOR (Davi quer desenhar antes)

- **Estudo do corpus AnKing pra aprender "o bom card".** Antes de gerar card autoral, destilar de centenas de cards reais (offline, do export de 92 MB) o padrão de um bom cloze: o que esconder, o que deixar de dica, tamanho, formato, um-mecanismo-por-card. Vira referência + alimenta [[calibrar-antes-de-gerar-cards]]. **Offline, não precisa de Anki vivo.**
- **Bibliografia do curso em pasta pro Claude ler capítulos dirigidos.** Davi coloca os PDFs (Moore, Langman, Junqueira, etc.) em `_material/` + um índice `aula → capítulo/páginas`. Claude lê só as 3-5 páginas do ponto que está aprofundando (custo de token baixo — mesmo padrão da leitura dirigida de slides). Regra: leitura escopada, NUNCA despejo do livro inteiro no contexto.
- **Pesquisa ampla sobre retenção (retrieval/testing effect).** Como questões e cards fixam conteúdo e por quê (efeito de teste, dificuldade desejável, por que cloze funciona, spacing/FSRS). Vira `referencias-externas/CIENCIA-RETENCAO.md` que calibra a filosofia de card e de E2. 1× doc, custo baixo.

## PRECISA DE ANKI VIVO (fazer quando o container subir)

- **Provisionar o container Anki** (INFRA-REMOTO.md) com o perfil do Davi + login AnkiWeb. Hoje não existe container/imagem/coleção nesta máquina — bloqueia todo apply/sync. Ação do Davi (creds/perfil).
- **Add-on de dicionário médico** (tipo AMBOSS, grátis) como add-on do Anki, que ensina os termos médicos nos cards.
- **Image occlusion (cloze de imagem).** Gerar oclusões de imagem a partir de (a) atlas de anatomia, (b) imagens do slide do professor quando faltar. Foco em anatomia — AnKing é fraco em anatomia macro, e Davi tem provas práticas.
- **Decks de anatomia da internet pra filtrar.** Puxar decks de anatomia médica, filtrar pelo método de curadoria, ter conteúdo pro deck de anatomia (onde o AnKing não cobre bem).
- **Repos GitHub de card-gen.** Puxar repositórios que ensinam a gerar cards, pra preencher lacunas — só se o método atual travar.
- **Card autoral pra LACUNAS.** Depois que `verificar_cobertura` marca subtópico como LACUNA/PENDENTE-GERADO, gerar card NEBLI autoral (calibrado; incl. cloze de imagem do slide). Ordem de prioridade do Davi: (1) curar bons AnKing, (2) achar outros decks, (3) criar autoral.

## META: DECK-AULA → DECK-MESTRE (foco da sessão da tarde)

- **Gerar um "deck-aula" por aula** e **agregar num "deck-mestre"** com o acumulado de todas as aulas que Davi já teve. Objetivo: aprofundar mais E reter por mais tempo (o norte: aprender e lembrar). Definir: estrutura dos decks (filtered por tag `NEBLI::<slug>` vs deck real), como o deck-mestre acumula sem duplicar entre aulas (liga com a ideia do **ledger cumulativo** em MEMORY.md § Pendências), ritmo FSRS sustentável (X novos/dia → Y revisões).
- **Ledger cumulativo (NEBLI-monitor de verdade).** Índice do que já foi coberto por aula → não repete card entre aulas, sabe onde aprofundar, habilita fisiopatologia por camadas só quando o pré-requisito já foi estudado.

## Notas de custo (resposta ao Davi)
- Bibliografia dirigida = **barato** (lê só as páginas do ponto). Despejo de livro = caro, não fazer.
- Estudo do corpus AnKing + pesquisa de retenção = **offline, barato**, 1× cada.
- O que custa/depende de infra = tudo que precisa de Anki vivo (bloco acima).
