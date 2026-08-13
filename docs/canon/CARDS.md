# Cards: curadoria, autoria e cópia

## Ordem de fontes

1. card AnKing/deck externo adequado cuja frente já esteja em português;
2. card autoral em português, informado por AnKing/decks externos quando a melhor fonte estiver em inglês;
3. card autoral para lacuna genuína.

Busca é por texto real, sinônimos EN, tags, cards irmãos e mídia — não apenas
pelo caminho de uma tag. Autoria exige candidatos e rejeições documentados.

## Cópia segura

O original é somente leitura. A cópia só entra se a frente já estiver em
português e preserva note type, campos, HTML/CSS, tags, mídia e crédito, recebe GUID novo e registra o GUID fonte. Colisão de mídia
é resolvida por hash; mesmo nome com bytes diferentes recebe namespace NEBLI.
Card inglês não é copiado: ele pode orientar profundidade, redação e escolha de
mídia, mas a recuperação final é autoral e revisada em português.

## Autoral

- português médico natural na frente, no Extra, no prompt e nas respostas de IO;
- uma recuperação independente por card; se a frente admite duas respostas que
  podem ser lembradas separadamente, dividir;
- um único cloze `c1` e uma única ocorrência por card;
- resposta de cloze com **1 palavra por padrão**, 2 quando formam uma unidade
  semântica natural e 3 apenas excepcionalmente, com justificativa registrada;
- quatro ou mais palavras no cloze bloqueiam o card;
- Extra curto em português: causa → mecanismo → consequência;
- fonte e âncora E1 em metadados;
- imagem somente com função cognitiva;
- sem pergunta genérica, lista longa, tautologia, indução ou voz de apostila.

## Qualidade da pista e posição do cloze

Esta regra vale para **todo card autoral**, em qualquer disciplina. A frente
precisa tornar uma resposta específica inequívoca, mas a resposta deve depender
de conhecimento médico, não de gramática, raiz lexical, sigla expandida, palavra
vizinha ou oposição óbvia.

- preferir ocultar mecanismo, consequência, discriminador, valor ou direção;
- rótulo específico só é aceitável quando a associação nominal é o próprio alvo;
- se o enunciado já expõe o mecanismo inteiro, não ocultar apenas o nome;
- revisar a frente mascarada sem ver a resposta e listar alternativas plausíveis;
- qualquer alternativa ainda defensável bloqueia o card;
- registrar confundidores próximos e por que a pista os exclui;
- o Extra explica depois da recuperação e nunca conta como cobertura do Front.

## Importância

`nucleo`, `apoio` e `opcional` são mutuamente exclusivos. O deck principal
recebe núcleo/apoio; opcionais ficam no subdeck `Optional`.

## Contrato por card e volume

O contrato contém `cards[]`, não apenas referências soltas. Cada entrada declara
`id`, conceito, origem, formato, alvo de recuperação, decisão de atomicidade e
quantos cards Anki produzirá. `route.card_refs` aponta somente para esses IDs.

O contrato também congela `card_budget.hard_max`. Somar
`generated_card_count` de `cards[]` precisa coincidir com o total do APKG e não
pode exceder o teto. O teto limita seleção e autoria; não autoriza deixar conceito
nuclear descoberto — nesse caso é o escopo que precisa ser revisto.
