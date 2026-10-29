# GUIA 4 — A aula: entender o que ela ensina antes de qualquer card

Os GUIAS 1–3 dizem como é um bom **card**. Este diz como é um bom **deck**: o deck é a aula, completa, na ordem e no peso que o professor deu. Leitura obrigatória inteira (gate `exemplares_lidos`, v10). Tudo aqui é fala literal de Davi (FEEDBACKS) e os decks que ele elogiou ou mandou refazer.

O pedido, nas palavras dele (29/10): **"quero que vc faça um deck completo DA AULA, sem trocar de conteúdo. para isso, precisa entender bem a aula antes, por isso o pipeline todo criado, porém muitas vezes vc nn entende"**.

## 1. As perguntas que vêm antes de tudo (E2)

"O que essa aula busca ensinar? o que o professor está ensinando com esse slide? onde ela se encaixa no todo? o que deve ser lembrado?" (F-20261022-CLAUDE-06)

1. **Qual é o assunto da aula?** É o título da aula, não o do maior bloco de lâminas. "Patologia das infecções virais" é sobre como a infecção viral aparece no tecido, para qualquer vírus. Se a resposta for o nome de uma doença, de um vírus ou de um fármaco, e a aula não se chama assim, a compreensão está errada.
2. **Onde está o princípio e onde está o exemplo?** Ler o título de cada lâmina e a fala do professor. Quando ele mesmo diz "o exemplo de", "vamos tentar transformar isso numa coisa mais palpável", "a combinação de tudo", "um caso", aquele bloco é **exemplo**: serve para ver os princípios anteriores funcionando juntos. Gate duro: lâmina com esse rótulo não pode ser marcada como princípio.
3. **O começo da aula pesa mais.** "O COMEÇO DA AULA É MAIS IMPORTANTE." Em aula de princípio geral, as primeiras lâminas são o conteúdo e o caso do fim é a aplicação. O deck tem mais cards nos blocos de princípio do que nos de exemplo (gate, sem exceção por motivo).
4. **O que do exemplo vira card?** Só o que ensina um princípio geral, escrito como princípio geral. Cada card do exemplo declara o princípio que carrega (`principios_ilustrados`). Pergunta de teste: este card serviria para entender outra infecção (ou outra doença do mesmo processo)? Se só serve para a doença do exemplo, é ficha técnica e fica de fora, ou vira uma linha de verso.
5. **Exemplo não é o mesmo que caso que resolve um problema.** Na 58, cada família de vírus resolve um problema de replicação diferente: as famílias são o conteúdo (F-20261022-CLAUDE-08). A diferença está na fala do professor. Se ele apresenta o caso para juntar o que já foi dito, é exemplo. Se cada caso traz um mecanismo novo que não apareceu antes, é conteúdo. Para tratar como conteúdo um bloco que o slide chama de exemplo, o gate exige o trecho literal da transcrição que prova isso.
6. **Completo, sem trocar de conteúdo.** Todo item que a aula ensina tem card. Nada da aula sai, e nada que não é da aula entra. O AnKing de uma doença citada não entra só porque existe ("não ficar pondo coisa específica da doença do anking no deck").

## 2. Exemplares de deck (o que Davi aprovou)

- **UC08-BC10, embriologia do digestório** ("ESSE DECK DE EMBRIO DO INTESTINO E ESTÔMAGO TÁ TOP!!!", "é referência"). Segue a aula em ordem, com cadeia causal entre os cards (rotação do estômago → fígado à direita → bolsa omental → herniação), e o verso diz por que é assim e o que causa adiante. Copiar: a sequência de cards conta a aula, e cada card puxa o próximo.
- **58 Multiplicação viral v3** (refeita depois de "sinto que vc nn entendeu bem o que era a aula"). Compreensão no nível do processo: cada família de genoma com o seu ciclo inteiro (enzima, compartimento, ordem), que é o que as provas pedem para reconstruir. Copiar: `processo` por bloco e `reconstrucoes` das provas antes de buscar.
- **57 Princípios gerais dos vírus** (modelo vivo do pipeline). O princípio de cada estrutura vem antes do exemplo, e o exemplo só vira card quando a aula pede para reconhecê-lo. A abertura histórica entra só no que define vírus.
- **Aula de princípio geral** (1791575691218, hifas crescem pela ponta): "é isso que espero: coisas que me ajudam a compreender o fenômeno como um todo, para depois aprofundar".

## 3. Anti-exemplares de deck (o que Davi mandou refazer)

- **61 Patologia da infecção viral v2 (23/10) → virou deck de hepatite.** "VIROU UM DECK DE HEPATITE, MAS ISSO ERA SÓ PARA ILUSTRAR / AJUSTA O DECK INTEIRO PARA DEIXAR DE SER DE HEPATITE E VIRAR REALMENTE DE PATOLOGIA DA INFECÇÃO VIRAL / O COMEÇO DA AULA É MAIS IMPORTANTE." O erro: as lâminas 14–29, que o professor intitula "A combinação de tudo… o exemplo da hepatite", foram marcadas como **princípio**, então o gate de exemplo ≤ princípio nunca disparou; metade do deck saiu com "hepatitis B" na frente (antígenos do HBV, anti-HBc e vacina, esteatose do HCV, hepatite A, Masson). O certo: o bloco é exemplo; dele saem os princípios gerais da patologia viral que o caso mostra (proteína viral acumulada é efeito citopático; a lesão começa onde o vírus e as células inflamatórias chegam; o linfócito mata por apoptose, a necrose recruta neutrófilo e destrói a matriz; sem arcabouço não há regeneração, há fibrose), escritos como princípio, com a hepatite como contexto ou no verso.
- **59 Patogênese da infecção viral v1 (23/10) → ficha técnica de vírus.** "ficou muito conteúdo lateral e faltou aprofundar no que realmente é o conteúdo da aula […] não pensou sobre o que é a aula." 35 notas de ficha técnica de vírus específicos tiveram de sair.
- **58 Multiplicação viral v1 (21/10) → virou clínica.** "o deck não seguiu bem a aula, se perdeu, indo para um lado muito específico / faltou explicar os princípios, virou ciclo clínico." Drogas por nome, toxicidade, covid.
- **58 v2 (22/10) → raso.** "sinto que ficou raso, faltou coisa / isso não significa que deva estourar em quantidade de cards." A compreensão ficou no título das lâminas, não no processo.
- **Inflamação granulomatosa e Edema piloto.** Excesso de especificidades de doença sem o mecanismo geral; mini-aulas de doenças.
- **Lição errada do deck 60 que não pode ser generalizada:** "reclassificar os vírus do estudo dirigido como princípio" valeu ali porque o estudo dirigido pedia cada vírus como conteúdo. Nunca reclassificar um exemplo como princípio para passar o gate: o gate existe para avisar que o deck está virando o exemplo.

## 4. Como conferir antes de entregar (E7)

- Ler só as frentes, na ordem. Elas contam o assunto da aula, ou o assunto do exemplo?
- Contar os cards por bloco: o começo da aula tem o maior peso?
- Para cada card de bloco de exemplo, tapar o nome da doença: o card ainda ensina algo de patologia geral? Se não, sai ou vai para o verso de outro.
- A frase do título da aula consegue resumir o deck inteiro?
