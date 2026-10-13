# Melhorias pedidas por Davi — 11/10/2026 (F-20261011-CLAUDE-02)

Ordem de execução: **decks continuam primeiro** (Sonnet gera; **Opus revisa depois**, aula a aula ou em lote por UC). Os itens abaixo entram entre decks, no tamanho indicado.

| # | Pedido (literal resumido) | Estado | Como será feito |
|---|---|---|---|
| 1 | **Um só .apkg por UC no Drive** (`NEBLI - UCxx.apkg`), nenhum por matéria nem por aula; "tem que parar de upar o .apkg" | **feito 11/10** (regra) | Gate de Drive deixou de exigir `.apkg` da aula e passou a exigir o pacote da UC; `entrega --uc-apkg` regrava o pacote da UC no fim de cada deck. Os `.apkg` por aula que já estão no Drive **não foram apagados** (aguarda seu OK: ver pergunta 1). |
| 2 | Nome do deck = `aula (total\|ativos\|novos)` | **já vigente** (`nebli/rotulos.py`, add-on `nebli_decks`) | Nada a fazer; conferir só se algum ramo escapar do padrão. |
| 3 | **Add-on: clicar no deck e "fazer ele"**, sem mexer em config; liberar todos os dessuspensos de uma vez (prova); atualizar stats FSRS dos cards | pendente | Botão no menu de contexto do deck. Reaproveita `nebli.decks liberar --treino` (cram dos não suspensos, sem reagendar) e o filtrado mantido pelo `nebli_decks`; ao encerrar, recalcula o estado de memória FSRS dos cards revisados. Vai para o pacote "add-on NEBLI" (ADD-ON-NEBLI.md). Quando: depois da P2 gerada. |
| 4 | Você suspende/dessuspende por deck depois que todos existirem | sem ação | Não há quota nem distribuição por mim; todos os decks novos entram **dessuspensos** (F-20261010-CLAUDE-05). |
| 5 | **Estudo: autorais × AnKing × cards que você acerta fácil**, para extrair regras de autoria | pendente (primeira medição feita) | Primeira leitura (831 cards revisados): AnKing 447 cards, lapso/revisão 10,7%; Autoral 140 cards, 11,2%; Slide 11,1%; Histology 14,7%. Quase igual, mas os autorais são mais recentes (intervalo médio 3,8 d contra 7,1 d). Falta controlar por idade, cor e matéria e ter mais revisões. Plano: reler o histórico de revisões (`revlog`) por card, parear autorais e AnKing do mesmo assunto, listar os mais fáceis e os mais errados e extrair o que os distingue (tamanho, nº de clozes, imagem, negrito, tipo de pergunta). Saída: regras para o lint e para o `card-author`. Quando: após 2–3 semanas de revisões dos decks novos; refaço a medição com mais dados. |
| 6 | **Pesquisa ampla de ciência cognitiva para melhorar os Tabs** ("não explicam a dúvida que tenho") | pendente | (a) levantar as dúvidas reais: cards com mais lapsos, comentários e os Tabs que você leu e rejeitou; (b) pesquisar evidência (explicação elaborativa, autoexplicação, efeito de redundância, erros comuns, dica mínima antes da resposta, carga cognitiva); (c) propor o novo formato do Tab com 3 exemplos reescritos para você aprovar; (d) só então regenerar. Agente de pesquisa separado, sem tocar no Anki. Pergunta 2 abaixo. |
| 7 | Gerar com Sonnet e **revisar com Opus** | vigente a partir de agora | Cada deck fecha com gates e revisão própria; a revisão do Opus é uma passada separada e posterior (lê o deck instalado contra o material de base, procura erro científico e cobertura). Registrar "revisado pelo Opus em DD/MM" no ESTADO. |

## Respostas de Davi (F-20261011-CLAUDE-03)
1. Apagar os .apkg por aula: **sim** (feito, 29 arquivos). 2. Tab: **os dois** (causa e definição) e "indo pro lado errado" (investigar). 3. Cram: **reagenda**.

## Perguntas antigas
1. Apago do Drive os `.apkg` por aula e por matéria já enviados (mantendo `NEBLI - UCxx.apkg`)? **Suposição:** não apago nada até você dizer.
2. Para o item 6, a dúvida típica é "por que a resposta é essa" (causal) ou "o que é esse termo" (definição)? **Suposição:** as duas, com a causal primeiro.
3. Item 3: o cram deve **reagendar** pelo FSRS (conta como revisão) ou só treinar? **Suposição:** não reagenda, e o botão separado recalcula o estado FSRS.
