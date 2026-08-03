# Deck longitudinal de etimologia médica — fechamento v3

## Resultado

O deck integral contém **765 notas/cards** no Anki, todos suspensos. Ele foi refeito como uma ferramenta de transferência: aprender morfemas, composição, famílias contrastivas e limites de inferência para compreender termos novos durante a graduação, e não como uma lista de definições isoladas.

A árvore `NEBLI::Etimologia` tem ainda 69 notas legadas mantidas pelo usuário; após a auditoria de 2026-07-17 e a ampliação latina, todas as 834 notas da árvore exibem o rótulo **Etimologia.**, têm clozes em negrito e respeitam os limites estruturais auditados.

## O que mudou a partir do piloto e do seu feedback

- Máximo absoluto de três clozes por nota; clozes contrastivos usam o mesmo `c1`.
- Texto limitado a 25 palavras; cloze limitado a três palavras.
- Extra geralmente até 25 palavras; teto de 40. Nesta versão, todos ficaram em até 24 palavras.
- Termos de menor exposição receberam explicação contextual e exemplo, em vez de uma glosa seca.
- Comparações grego–latim ficaram deliberadamente seletivas: há 14 notas nessa camada, sem transformar o deck em catálogo de equivalências.
- Regras e testes impedem retorno dos erros recorrentes: quatro clozes, resposta longa, Extra excessivo, termo novo sem didática e transferência sem decomposição interpretada.

## Estrutura e abrangência

| Camada | Cards |
|---|---:|
| Fundamentos de formação e decomposição | 8 |
| Famílias e contrastes | 106 |
| Morfemas em contexto | 537 |
| Testes de transferência | 100 |
| Exceções, polissemias e limites | 14 |

Além dessas camadas, há 27 cards de nomenclatura anatômica latina, em `04_Raizes_por_sistema::00_Nomenclatura_anatomica_latina`.

Os subdecks separam fundamentos; prefixos; sufixos; raízes por sistema; fisiologia e bioquímica; patologia; farmacologia; semiologia; contrastes; armadilhas; e transferência.

O léxico mestre ficou com **800 entradas**. A auditoria fechou o inventário planejado de procedimentos confundíveis, sufixos menos expostos, forma/estrutura anatômica, cor/aparência, curso temporal, patologia, semiologia, polissemia, pares greco-latinos, linguagem farmacológica e nomenclatura anatômica latina.

## Verificação

- Validador do deck: 0 erros.
- Testes automatizados: 21/21 aprovados.
- Máximo observado: 3 clozes, 17 palavras no Texto, 24 no Extra.
- Fontes e confiança: presentes em 100% das notas; confiança alta.
- Termos inéditos reservados: 300, sem aparecer em Texto ou Extra. Pelo inventário ensinado, 171 são totalmente e 99 parcialmente decomponíveis: **90% de cobertura parcial ou total estimada**.

## Anki e retirada do piloto

- 683 notas novas foram criadas (656 no núcleo inicial e 27 na camada latina).
- As 82 notas aprovadas do piloto pt2 foram integradas aos subdecks definitivos.
- As 114 notas do piloto v2 foram removidas (120 cards).
- Não restam notas com `etim_pilot_pt2` nem `etim_v2`; o subdeck de piloto também foi removido.
- Os snapshots de pré-migração continuam em `releases/` e o seu arquivo anotado `reports/pilot_cards.md` foi preservado intacto.

## O que falta fazer

A geração e a migração estão concluídas. O trabalho restante é pedagógico e deve ser guiado pelo uso real: começar a dessuspender por subdeck ou em blocos pequenos, marcar termos que ainda confundem em aula e, após algumas semanas de revisão, ajustar a seleção conforme lapsos e dúvidas recorrentes. Uma revisão externa especializada pode ser acrescentada no futuro, mas não há lacuna de geração pendente neste escopo.
