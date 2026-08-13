# Contrato canônico de qualidade dos cards NEBLI

Este arquivo é **hard gate**. Nenhum deck-aula é concluído porque “parece bom” ou
porque a maioria dos cards passou. Cada card real do deck precisa cumprir as
regras aplicáveis e o lote só fecha com 100% de aprovação.

## 1. Princípio central: uma recuperação útil por card

Um bom card testa **uma recuperação independente, específica e relevante para a
aula**. Ele não deve funcionar como mini-resumo, lista de fatos desconexos ou
pergunta que exige várias respostas sem relação funcional entre si.

Antes de criar um card, deve existir:

1. conceito no contrato de cobertura;
2. âncora literal na E1;
3. decisão de importância (`nucleo` ou `optional`);
4. justificativa de que aquela recuperação merece existir no deck.

Se o conteúdo ainda precisa ser ensinado, ele entra primeiro na E1. O card não é
o lugar de introduzir matéria nova.

## 2. Quantidade e cobertura

- Definir e congelar `card_budget.hard_max` antes da seleção final.
- Contar **cards Anki reais**, não notas, conceitos ou linhas JSON.
- Não criar cards só para atingir uma cota.
- Não sacrificar um conceito nuclear relevante para economizar um card.
- Subtópicos recebem cards proporcionalmente à importância da aula.
- `nucleo` e `optional` não se misturam no mesmo card; opcionais vão para
  `<Deck-Aula>::Optional`.

O deck é o **núcleo de retenção**, não um espelho fato a fato da E1. Conceitos
podem ser `must_recall`, `derivable`, `e1_only` ou `optional`, conforme
`docs/canon/NUCLEO-DE-RETENCAO.md`. A cobertura completa pertence à E1; o deck
retém o conjunto mínimo capaz de reconstruir o núcleo importante.

Faixas de planejamento, não metas: pequena 8–12 (teto 15), média 12–18 (teto
20), grande 18–22 (teto 25). Mais de 25 exige revisão explícita de divisão ou
compressão da aula.

## 3. Ordem de fonte

A ordem é:

1. AnKing adequado;
2. deck externo real e superior, quando disponível;
3. autoral apenas para lacuna comprovada.

Uma busca sem resultado não comprova lacuna. Usar query em inglês médico,
sinônimos/aliases e siblings relevantes. Um candidato só entra se cobrir
**exatamente a recuperação da aula**, não apenas um tema vizinho.

Nota e sibling são decisões distintas: a nota é encontrada pelo contexto; o
sibling/cloze é escolhido pela resposta esperada. Todo autoral direto registra
`anking_search_complete=true`, no mínimo três consultas independentes, expansão
de escopo, revisão de siblings, contagem de candidatos e o motivo concreto de
rejeição de cada candidato. IO e deck externo obedecem à mesma prova de busca
AnKing, pois também são rotas posteriores na prioridade.
Se um AnKing adequado já foi validado, ele usa `anking_required=true` e uma
falha técnica bloqueia o lote em vez de instalar autoral.

Cópias AnKing/deck externo:

- só entram no deck final quando a frente renderizada já está em português;
- conteúdo didático é literal, sem reescrita;
- preservar note type, todos os campos, HTML, clozes, tags, mídia e créditos;
- criar nota independente no Deck-Aula, com scheduling novo;
- nunca alterar a nota-fonte;
- selecionar somente o sibling relevante; os demais nascem suspensos;
- se houver ambiguidade real de seleção, usar fallback validado em vez de
  escolher à força.
- se a fonte adequada estiver em inglês, usá-la como referência de conteúdo,
  profundidade e mídia; a recuperação final deve ser autoral em português.

## 4. Card autoral

O autoral existe para **lacuna real**, não para competir com um AnKing bom.

Hard rules:

- frente em português médico natural;
- `Extra` curto em português;
- uma única recuperação;
- resposta estimada em até 10 segundos;
- exatamente **uma ocorrência de cloze**;
- usar `c1`;
- resposta do cloze: **1 palavra por padrão**;
- 2 palavras quando semanticamente necessário;
- 3 palavras apenas excepcionalmente e com justificativa registrada;
- 4+ palavras bloqueia;
- evitar enumerações e frases que peçam duas decisões independentes;
- a pista deve tornar a resposta inequívoca sem entregá-la e sem permitir acerto
  apenas por gramática, sobreposição lexical ou formato;
- frente enxuta; limite operacional de 360 caracteres;
- `Extra` até 100 palavras e apenas para contexto realmente útil.
- `retrieval_target` explícito;
- revisão registrada de pergunta inequívoca, português médico natural, ausência de
  duplicata funcional e Extra que apenas apoia a resposta.

### Gate universal anti-indução

Todo card autoral, independentemente da matéria, registra e passa:

1. `cloze_role`: mecanismo, consequência, discriminador, valor, direção ou
   rótulo específico;
2. `knowledge_required=true`: acertar exige o conhecimento médico-alvo;
3. `grammar_only_solvable=false`, `lexical_leak=false` e
   `answer_visible_elsewhere=false`;
4. revisão cega da frente mascarada;
5. zero alternativas semanticamente defensáveis não resolvidas;
6. lista dos confundidores próximos examinados e justificativa de unicidade.

O teste central é: se alguém consegue completar o branco apenas relendo a frase,
o cloze está no lugar errado. Mover o branco para o token de maior valor não
autoriza ocultar uma oração longa: a resposta continua curta e atômica.

### Exemplos de direção

Bom: uma relação anatômica, uma função, uma origem, uma estrutura, uma etapa
mecanística.

Ruim: “cite todas as relações”, “liste irrigação, drenagem e inervação”, cloze
que apaga uma oração inteira, ou card cujo Extra vira uma nova aula.

## 5. Imagem e Image Occlusion

Imagem só entra quando cumpre uma tarefa cognitiva. “Imagem do mesmo tema” não é
critério suficiente.

- reconhecimento/localização → preferir IO ou prompt visual;
- mecanismo → imagem pode ficar no Extra;
- conceito puramente verbal → imagem pode ser `none`;
- fonte real é preferência absoluta; visual genérico/decorativo bloqueia.
- em card autoral, procurar primeiro mídia local do AnKing; slide/fonte externa
  exige rejeição visual AnKing documentada;
- toda imagem exige crédito, propósito cognitivo e revisão explícita de valor
  didático.

Para IO:

- usar `hide_two_guess_two`, normalmente com duas respostas coerentes;
- escrever prompt e respostas finais em português e registrar revisão de ambos;
- se a imagem-fonte trouxer rótulo em outro idioma, mantê-lo coberto também na
  resposta e sobrepor a solução em português na mesma posição;
- a máscara cobre o **rótulo-resposta**, não a estrutura que o aluno deve
  reconhecer;
- no máximo duas máscaras; duas exigem `pair_rationale` e tarefa coerente;
- coordenadas devem estar dentro da imagem;
- pergunta e resposta precisam ter preview validado;
- bloquear vazamento da resposta;
- bloquear imagem ilegível, crop ruim, fonte duvidosa ou mídia quebrada;
- anatomia/histologia que exige reconhecimento não pode fechar apenas com cards
  verbais.

## 6. Relevância e atomicidade

Cada card precisa passar explicitamente:

- `relevant=true`: responde a algo que a aula realmente cobra;
- `atomic=true`: uma recuperação independente;
- âncora E1 presente;
- fonte escolhida na ordem correta;
- sem duplicata funcional de outro card do mesmo deck.

Dois cards podem tratar do mesmo conceito somente se testarem recuperações
realmente distintas e ambas justificadas.

## 7. Gate card a card

Antes da instalação, gerar um registro de validação para **cada card real**.

O gate exige:

- `expected_card_count == validated_card_count`;
- `passed_card_count == expected_card_count`;
- `failed_card_count == 0`;
- card keys únicas;
- nenhuma lacuna nuclear ignorada;
- nenhuma mídia obrigatória ausente.
- revisão de compressão e ablação aprovada para o núcleo inteiro.

Após a instalação no AnkiDroid:

- `installed_card_count == expected_card_count`;
- deck e subdeck devem ter os nomes canônicos;
- cópias AnKing devem manter fonte intacta;
- autorais precisam renderizar como uma recuperação;
- IO precisa renderizar máscara na pergunta e imagem/solução na resposta;
- qualquer falha de runtime bloqueia o lote e notas novas daquela tentativa são
  revertidas.

## 8. Definição de pronto

Um Deck-Aula só está pronto quando:

1. cobertura nuclear está fechada;
2. quantidade está dentro do contrato;
3. todos os cards passaram as regras acima;
4. o manifesto completo foi gerado;
5. o Companion instalou o total esperado em `NEBLI::*`;
6. o recibo confirma a contagem e ausência de falhas;
7. o AnkiDroid termina com o deck correto selecionado.

Executar comandos, gerar JSON ou compilar APK não é, isoladamente, definição de
pronto.
