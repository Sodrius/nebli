# Cards: curadoria, autoria e cópia

## Ordem de fontes

1. AnKing curado;
2. decks externos privados (BlueLink, Dope, histologia/LLU e equivalentes);
3. card autoral para lacuna genuína.

Busca é por texto real, sinônimos EN, tags, cards irmãos e mídia — não apenas
pelo caminho de uma tag. Autoria exige candidatos e rejeições documentados.

## Cópia segura

O original é somente leitura. A cópia preserva note type, campos, HTML/CSS,
tags, mídia e crédito, recebe GUID novo e registra o GUID fonte. Colisão de mídia
é resolvida por hash; mesmo nome com bytes diferentes recebe namespace NEBLI.

## Autoral

- inglês médico natural na frente;
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
