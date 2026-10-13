# NEBLI — instruções de entrada

Para E1, cards, Anki, curadoria e arquitetura, ler primeiro `flashcards/projeto/README.md` e seguir a ordem: `MEMORY.md`, `flashcards/projeto/FEEDBACKS.md` e, na execução, `flashcards/projeto/EXECUCAO-DECK-AULA.md`. Isso vale para mensagem comum em toda nova sessão. As respostas de calibração já estão consolidadas; não pedir que Davi reensine suas preferências.

MEMORY é a única memória normativa dos decks. O pipeline padrão é **E1 + cards**, com exceções e estado na memória/fila. UC08: `flashcards/projeto/RECONSTRUCAO-UC08.md`; fontes/modelos: `flashcards/projeto/ACERVOS-REFERENCIA.md`. E1 quando aplicável: `didatica/E1.md`. Não usar divisão de tarefas, idioma ou ritmo de handoffs antigos. E2/E3 são histórico.

Todo feedback recebido por qualquer executor vai ao registro único nesta sessão. Atualizar a preferência em seu lugar no MEMORY; não espalhar regras pela fila. Aplicar melhorias às próximas entregas; alterar deck anterior só quando Davi pedir. Demonstrar aplicação dos critérios na revisão, não apenas leitura dos arquivos.

**Como se faz um deck-aula (calibração de 02/10/2026; vale para toda sessão, de qualquer IA).** A porta de entrega é um comando só: `python3 -m nebli.gates arquivos-trabalho/<corrida>`. Ele falha se faltar evidência de qualquer passo abaixo; não entregar com FALHA nem declarar pronto sem rodá-lo.

1. **Fontes, nesta ordem, antes de escolher qualquer card:** slides (ver todas as lâminas), provas antigas, exercícios e material do CAOC no Drive montado (`~/Library/CloudStorage/GoogleDrive-dpbdes@gmail.com/Mon Drive/`); o capítulo da aula na bibliografia da UC; as aulas dos canais que Davi acompanha (transcrição lida). Listas em `flashcards/projeto/ACERVOS-REFERENCIA.md`, seção de 02/10. Registrar em `<corrida>/fontes.json`; fonte não achada é declarada com a busca feita, nunca omitida.
2. **O deck é a aula:** cobre tudo o que a aula e o capítulo ensinam sobre ela, inclusive os hormônios e a regulação do tema, e nada de fora (raras clínicas de encaixe direto). Cards na ordem dos slides (`NEBLI::ordem::<curto>-<NN>`, `evid` começando por “Slide N”).
3. **Origem dos cards:** AnKing → outros acervos → MCAT/AnatoKing/Dope → autoral por último. A busca nos externos é feita de verdade e gravada (`busca/ext.txt`). Autoral é minoria (teto 15%, F-20261003-CLAUDE-18: buscar card de tudo, autorar só o que importa e não se achou), nasce de 2–3 espelhos AnKing, é curto, uma frase que ensina o processo e oculta um nome, em inglês, sem “;” nem “:”, sem resposta óbvia pela frase.
4. **Cores:** verde = núcleo para anos; azul = necessário para a prova; rosa = útil de baixa prioridade (poucos). Total acompanha a aula; verdes dimensionados para a rotina de **40 cards novos por dia**.
5. **Depois de instalar:** Tab em 100% (`nebli.explicacoes`), ordem verificada (`nebli.ordem`), E1, quando incluída no pedido, compilada e vista página a página, tudo entregue na pasta da aula no Drive com `python3 -m nebli.entrega` (`<Aula> - E1.pdf`, `<Aula> - slides.pdf`, `<Aula>.apkg`) e relatório curto a Davi com o que não foi feito.
6. **Não afirmar o que não foi feito** (busca, leitura, teste na tela). Feedback de Davi vira regra aqui, checagem em `nebli/gates.py` ou linha no MEMORY, na mesma sessão.
7. **Tab e cloze (F-20261003-CLAUDE-17/18):** o Tab explica para quem nunca viu o tema, do básico ao avançado (150–220 palavras; gate: mediana ≥ 140); cloze fora do AnKing ≤ 3 palavras (no geral 1–2), nunca “x ou y”.

**Estado em 02/10/2026:** Davi apagou todos os decks médicos NEBLI para refazer do zero, para estudo de longo prazo. Pedido atual: **UC08 P1 primeiro → UC03 P2; somente decks, sem E1, entrega por aula revisada**, conforme bibliografia e sem extrapolar a aula. Demais provas ficam no backlog. Plano operacional: EXECUCAO-DECK-AULA §9; preferências: MEMORY. Contagens e “instalado” em documentos anteriores são históricos; cards compartilhados antigos não existem mais.

Preservar originais, estudo, edições, flags, suspensões pessoais e trabalho local não relacionado. Escrita Anki usa `nebli.decks.escrita()` e `arquivos-trabalho/ANKI-ESCRITA.lock`, conforme o roteiro. Auditoria/planejamento são somente leitura externa, salvo correção solicitada. Não restaurar artefatos limpos manualmente nem reclassificar a coleção toda.

Outras tarefas: `CLAUDE.md` e `MEMORY.md`. Regras de etimologia não governam cards médicos. Versões integrais e fila antiga em `flashcards/projeto/HISTORICO.md`; não são instruções atuais.

Pedido simples como “rode E1 + deck para <aula>” inicia o roteiro vigente completo, com os critérios consolidados de 02/10 no MEMORY; não precisa de briefing extra. Pedido explícito de E1 + deck prevalece sobre a exceção histórica de só cards da UC08. A revisão deve demonstrar aplicação com exemplos na corrida, sem declarar calibração longitudinal já aprovada.
