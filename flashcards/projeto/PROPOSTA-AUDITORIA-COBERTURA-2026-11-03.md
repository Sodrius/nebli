# Proposta para Davi — auditoria de cobertura da aula

**Estado: aprovada por Davi em 03/11/2026 e incorporada às etapas E2, E3 e E7 do pipeline.** Este documento conserva os exemplos e os casos de decisão da proposta. A seleção de exemplares para autorais também é regra vigente; acompanhamento em 7/14 dias e prova curta fora do baralho foram rejeitados.

## Problema que a auditoria precisa resolver

Um deck pode citar todos os títulos das lâminas e ainda não cobrar o percurso necessário para explicar a aula. Também pode ter muitos cards verdadeiros que transferem o peso do princípio para um exemplo. Os casos históricos foram MHC com nomes sem a relação via → MHC I/II → CD8/CD4; fagocitose com etapas apenas no Tab; patologia viral transformada em hepatites. As refações posteriores mudaram esses decks: os casos são testes do método, não afirmações de que as falhas continuam no Anki atual.

## Unidade de cobertura proposta

Usar uma **relação ensinável** no mapa já existente, não uma linha por título ou uma quota de cards. Cada relação precisa conter: (a) fonte e trecho ou lâmina; (b) o que Davi deve conseguir recuperar; (c) papel na aula; (d) card ou conjunto de cards que a exige. Exemplos de relações: entrada → transformação → saída; causa → consequência; etapas em ordem; A × B com o critério que separa; estrutura → função; nome ou número indispensável situado em contexto.

O papel é decidido pelo professor e pelo objetivo da aula: **princípio**, **caso que apresenta mecanismo novo**, **exemplo que aplica princípio anterior**, **repetição** ou **apoio**. Uma mesma doença pode ser conteúdo numa aula e exemplo em outra. A contagem de cards por bloco serve para alertar sobre desvio de peso, não para impor teto.

## Passagem 1: aula → cards

1. Ler lâminas e transcrição do bloco na ordem. Para cada relação que a aula ensina, escrever em uma frase o que o aluno precisa conseguir explicar, distinguir ou nomear sem material aberto. Confrontar objetivos e questões da aula, quando houver. Não deduzir a relação só do título da lâmina.
2. Localizar no plano e no deck vivo a frente que exige recuperar a relação. Registrar as chaves dos cards e o trecho exato que faz a pergunta. Se duas frentes cobrem partes complementares, explicar como juntas fecham a relação.
3. Classificar o resultado: **recuperável**, **parcial** (por exemplo, nome cobrado sem elo causal), **só explicado** (aparece no Extra/Tab, mas não é recuperado), **ausente** ou **fora deliberadamente** com motivo. O essencial da aula não recebe “coberto” por mera menção no verso/Tab.
4. Corrigir `parcial`, `só explicado` e `ausente` quando atingem um objetivo central. Primeiro procurar AnKing/acervos ou reformular card existente; autoral apenas para lacuna ou fio comprovado, seguindo o exemplar do mesmo tipo. Repetição de slide não obriga card novo se a relação já é recuperável.

## Passagem 2: cards → aula

1. Ler todas as frentes na ordem do deck, junto com sua fonte e item do mapa. Para cada card, responder: “qual relação da aula ele me obriga a lembrar?” e “por que ela merece revisão recorrente?”.
2. Marcar **no foco**, **duplicado sem ganho**, **exemplo com peso excessivo**, **detalhe de outra aula**, **informação Step pertinente que ensina o princípio**, ou **sem justificativa demonstrada**. O julgamento usa o conteúdo, não só a resposta repetida: dois cards com a mesma palavra podem testar relações diferentes.
3. Conferir o papel dos exemplos: se só juntam princípios anteriores, cobrar o princípio e deixar o caso como contexto ou apoio; se cada caso introduz mecanismo próprio pedido pelo professor, preservá-lo como conteúdo. Não reclassificar exemplo para passar gate.
4. Verificar a progressão: princípios antes de aplicações; sequência reconstruível; comparações agrupadas quando o eixo é comum; detalhes proporcionais ao peso dado na aula. Um bloco com muitos cards pede releitura, mas não falha automaticamente.

## Casos de decisão que devem ser testados antes de aprovar

| Situação | Decisão proposta |
|---|---|
| “MHC I” e “MHC II” aparecem em cards, mas nenhum liga origem do antígeno, via e célula T | Parcial; relação central ainda precisa ser recuperada. |
| Etapas da fagocitose aparecem apenas no Tab | Só explicado; se são objetivo central, trazer a relação para a frente de um card. |
| Aula de patologia viral usa hepatite para mostrar lesão, inflamação e reparo | O princípio geral precisa aparecer antes; detalhes de sorologia do vírus não ganham card por mera presença no exemplo. |
| Aula de multiplicação viral exige distinguir estratégias das famílias genômicas | Cada estratégia nova é conteúdo; não reduzir todas a um exemplo genérico. |
| AnKing não citado literalmente explica uma etapa necessária ao princípio da aula | Pode entrar, com a relação e a fonte documentadas; HY sozinho não basta. |
| Duas lâminas repetem a mesma cadeia causal | Uma recuperação adequada pode cobrir ambas; registrar o compartilhamento. |

## Registro e limite de trabalho propostos

Usar `compreensao-aula.json`, `mapa-de-profundidade.json`, `inventario.py`, `REVISAO-DE-QUALIDADE.md` e a revisão de fidelidade já existente. Acrescentar o julgamento da relação nesses artefatos, sem abrir tabela paralela permanente. Fazer as duas passagens **uma vez antes da entrega**, no deck inteiro, aproveitando a releitura que o pipeline já exige. Não criar acompanhamento posterior, amostragem em 7/14 dias, teste fora do Anki ou quota numérica. O revisor registra casos duvidosos e sua justificativa; o executor resolve antes de entregar.

## Critério de aceite proposto

Ao terminar, cada objetivo central tem pelo menos uma recuperação identificável na frente de um card ou conjunto de cards; itens de apoio/repetição têm motivo claro para não gerar novo card; cada card tem papel e fonte defensáveis; exemplos não substituem o assunto da aula. O relatório cita as lacunas e excessos realmente encontrados e as correções feitas. Aprovação de verificações automáticas, por si, não atesta esse julgamento.

**Decisão de Davi:** “ÓTIMO / gostei / pode aplicar”. As duas passagens passam a integrar E2/E3/E7 sem criar artefato paralelo; a execução e as correções precisam ser registradas nos arquivos da corrida.
