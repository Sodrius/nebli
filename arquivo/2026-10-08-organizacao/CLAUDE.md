# NEBLI — entrada de toda sessão Claude

Para qualquer pedido de deck-aula, mesmo uma mensagem comum, leia [flashcards/projeto/README.md](flashcards/projeto/README.md) e siga a ordem: [MEMORY.md](MEMORY.md) inteiro, [FEEDBACKS.md](flashcards/projeto/FEEDBACKS.md) recente/pertinente e [EXECUCAO-DECK-AULA.md](flashcards/projeto/EXECUCAO-DECK-AULA.md) para executar. MEMORY guarda o que Davi quer e por quê; não deduza preferências de um handoff antigo nem peça novamente as 100 respostas.

A entrega padrão é **E1 + cards**, salvo escopo explícito. Para UC08, recupere fontes e estado em [RECONSTRUCAO-UC08.md](flashcards/projeto/RECONSTRUCAO-UC08.md); consulte [ACERVOS-REFERENCIA.md](flashcards/projeto/ACERVOS-REFERENCIA.md) na busca. Davi continuará a produção com Claude, conforme os pedidos no chat. A memória rege idioma, irmãos, cobertura, clínica, bandeiras e revisão. Não criar regra nova por preferência editorial própria.

O resultado esperado é um deck pronto, produzido e revisado pela IA, com evidência de que cumpre os critérios. Davi estuda e comenta; não precisa certificar quantidade de cards/verdes. Dúvida nova relevante pede poucos exemplos concretos, sem reabrir preferências resolvidas. Revisão de outra IA só existe se ocorreu; não assinar por ela.

**Como se faz um deck-aula (calibração de 02/10/2026; vale para toda sessão, de qualquer IA).** A porta de entrega é um comando só: `python3 -m nebli.gates arquivos-trabalho/<corrida>`. Ele falha se faltar evidência de qualquer passo abaixo; não entregar com FALHA nem declarar pronto sem rodá-lo.

1. **Fontes, nesta ordem, antes de escolher qualquer card:** slides (ver todas as lâminas), provas antigas, exercícios e material do CAOC no Drive montado (`~/Library/CloudStorage/GoogleDrive-dpbdes@gmail.com/Mon Drive/`); o capítulo da aula na bibliografia da UC; as aulas dos canais que Davi acompanha (transcrição lida). Listas em `flashcards/projeto/ACERVOS-REFERENCIA.md`, seção de 02/10. Registrar em `<corrida>/fontes.json`; fonte não achada é declarada com a busca feita, nunca omitida.
2. **O deck é a aula:** cobre tudo o que a aula e o capítulo ensinam sobre ela, inclusive os hormônios e a regulação do tema, e nada de fora (raras clínicas de encaixe direto). Cards na ordem dos slides (`NEBLI::ordem::<curto>-<NN>`, `evid` começando por “Slide N”).
3. **Origem dos cards:** AnKing → outros acervos → MCAT/AnatoKing/Dope → autoral por último. A busca nos externos é feita de verdade e gravada (`busca/ext.txt`). Autoral é minoria (teto 15%, F-20261003-CLAUDE-18: buscar card de tudo, autorar só o que importa e não se achou), nasce de 2–3 espelhos AnKing, é curto, uma frase que ensina o processo e oculta um nome, em inglês, sem “;” nem “:”, sem resposta óbvia pela frase.
4. **Cores:** verde = núcleo para anos; azul = necessário para a prova; rosa = útil de baixa prioridade (poucos). Total acompanha a aula; verdes dimensionados para a rotina de **40 cards novos por dia**.
5. **Depois de instalar:** Tab em 100% (`nebli.explicacoes`), ordem verificada (`nebli.ordem`), E1, quando incluída no pedido, compilada e vista página a página, tudo entregue na pasta da aula no Drive com `python3 -m nebli.entrega` (`<Aula> - E1.pdf`, `<Aula> - slides.pdf`, `<Aula>.apkg`) e relatório curto a Davi com o que não foi feito.
7. **Conferência final item a item (gate duro, 02/10):** depois de instalar, listar em `<corrida>/cobertura.json` cada rótulo/estrutura dos slides, cada item do roteiro prático e cada pergunta dos exercícios com os cards que o cobrem. Item de roteiro ou exercício sem card reprova. Em anatomia, o que faltar vira oclusão do próprio slide (`python3 -m nebli.slide_io`); conferir também o Netter.
8. **Ordem estrita dos slides (gate duro, 02/10):** entradas do plano em ordem crescente de slide, sem recuo, da primeira à última lâmina; Browser e fila de novos na mesma ordem.
9. **Planejar antes, revisar depois (gates duros, 02/10):** `planejamento.json` (alvos por slide a partir de slides, bibliografia, CAOC, YouTube, material de veterano e provas) antes de montar; `revisao-final.json` depois de instalar. Ordem e estado da campanha em `flashcards/projeto/PLANO-GERACAO-ANO.md`.
10. **Todo feedback de Davi corrige os decks anteriores e vira gate duro na mesma sessão.** Dope Anatomy só sem alternativa (`sem_alternativa`); autoral não repete alvo já cobrado no deck (`duplicacao_ok`).
11. **Oclusão do slide é autoral (F-20261003-CLAUDE-13):** antes dela, procurar o alvo no AnKing e nos externos (`python3 -m nebli.io_busca`) e registrar `busca`; a máscara cobre o rótulo inteiro (`nebli.slide_io` r2; `nebli.io_refazer` para refazer notas vivas) e toda prévia é vista. Teoria do livro da UC entra na cobertura (`cobertura.json` com itens `livro`); em histologia, o deck Histology é o Junqueira em cards e vem antes de oclusão ou autoral, com identificação ≤ 25% dos cards.
12. **Comentários de Davi (F-20261003-CLAUDE-15):** antes de cada aula, `python3 -m nebli.comentarios`; cada comentário corrige o card e o padrão em todos os decks; nunca apagar comentário. Card de estrutura com figura de livro/AnKing; verso com explicação curta; revisão final card a card (`revisao-final.json` "cards").
13. **Tab e cloze (F-20261003-CLAUDE-17/18):** o Tab explica para quem nunca viu o tema, do básico ao avançado (150–220 palavras; gate: mediana ≥ 140); cloze fora do AnKing ≤ 3 palavras (no geral 1–2), nunca “x ou y”.
6. **Não afirmar o que não foi feito** (busca, leitura, teste na tela). Feedback de Davi vira regra aqui, checagem em `nebli/gates.py` ou linha no MEMORY, na mesma sessão.

**Estado em 02/10/2026:** Davi apagou todos os decks médicos NEBLI para refazer do zero, para estudo de longo prazo. Pedido atual (ampliado em F-20261002-CLAUDE-09): **geração em massa UC08 (P1, P2) → UC03 (P2, P3) → UC21 → UC01 e UC02; somente decks, sem E1, entrega por aula revisada, com os ajustes de cada aula aplicados também aos decks já gerados nesta campanha**, conforme bibliografia e sem extrapolar a aula. Demais provas ficam no backlog. Plano operacional: EXECUCAO-DECK-AULA §9; preferências: MEMORY. Contagens e “instalado” em documentos anteriores são históricos; cards compartilhados antigos não existem mais.

**Antes de encerrar:** registre todo feedback recebido no FEEDBACKS comum, inclusive local/positivo, atualize a preferência no MEMORY em seu lugar e o estado na fila/corrida. Reler alterações concorrentes antes de gravar/entregar. Melhorias são prospectivas; deck anterior só muda quando solicitado. Não criar outra memória/handoff nem depender da conversa privada para passar contexto ao Codex ou à próxima sessão.

Preservar originais, identidades, estudo e marcas pessoais; seguir lock, backup e readback no roteiro. Não ressuscitar apagados nem limpar o workspace compartilhado. Documentação não certifica implementação, cobertura, imagens ou sincronização remota.

## Outras rotas preservadas

- E1: `didatica/E1.md`, com suas referências de didática/voz; E2/E3 e RemNote são históricos.
- Cadernos de provas: `banco/CLAUDE.md`, `typst-build/pipeline_caderno.py` e seção Cadernista de `ROLES.md`.
- Typst: `typst-template/CLAUDE.md`, `CHEATSHEET_ARMADILHAS.md` e `TEMPLATE_API.md`.
- Site/liga/etimologia: estado e localização dos planos no MEMORY; não iniciar por inferência.
- Versões integrais de regras e decisões: [HISTORICO.md](flashcards/projeto/HISTORICO.md), somente para consulta situada.

Pedido simples como “rode E1 + deck para <aula>” inicia o roteiro vigente completo, com os critérios consolidados de 02/10 no MEMORY; não precisa de briefing extra. Pedido explícito de E1 + deck prevalece sobre a exceção histórica de só cards da UC08. A revisão deve demonstrar aplicação com exemplos na corrida, sem declarar calibração longitudinal já aprovada.
