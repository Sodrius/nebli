# Calibração editorial — 02/10/2026

Experimento local de estilo, sem instalação nem certificação médica. Preferências continuam no MEMORY e o procedimento de produção no roteiro existente.

## Pergunta e separação

Avaliar se juízes sem acesso à origem encontram padrões de escrita que distinguem autorais de AnKing e se as correções se transferem para alvos novos. Autores não recebem comparadores de teste ou calibração exclusiva dos juízes. Cada juiz recebe apenas instrução, calibração e lote anônimo; chaves e resultados de outros juízes ficam com o orquestrador. O orquestrador conhece as origens; portanto o nome tecnicamente preciso é avaliação cega por avaliadores independentes, com separação autor–avaliador, não ensaio integralmente duplo-cego.

## Plano antes dos escores

- Desenvolvimento v1: 32 rascunhos existentes ancorados em trechos da referência de autoria, 32 nativos da partição native-dev, oito famílias heurísticas; 24 exemplos nativos de calibração. Um juiz de frente, outro de frente + Extra, ambos em contextos novos.
- Aprender com críticas concretas, preservando precisão/contexto/recuperação. Produzir v2 em 32 alvos de fontes já reservadas antes das críticas, sem ver comparadores. Não basta corrigir pontuação, inserir negrito ou copiar frases.
- Transferência v2 usa comparadores novos e juízes novos. Conservar todas as rodadas, inclusive as piores. Não selecionar o melhor resultado entre tentativas como se fosse validação única.
- Métricas separadas por modalidade/família: confusão, balanced accuracy, sensibilidade, especificidade, AUC e AUC invertida, Brier, contaminações e críticas qualitativas. 32 itens por origem não satisfazem o critério de equivalência prévio do card-mirror; resultado será piloto, mesmo se próximo ao acaso.
- Controles positivo (autoral antigo com falhas) e nulo (nativo × nativo com rótulos aleatórios) precisam de avaliação independente antes de certificar que o detector é adequado. Sem esses controles, não chamar baixo acerto de sucesso.
- Leitura visual/imagens e aprovação pessoal de Davi são verificações próprias; texto não as substitui. Comparações por famílias amplas podem carregar pistas de assunto e não equivalem a pareamento perfeito por tema.

## Pesquisa consultada

- scikit-learn, [Common pitfalls / data leakage](https://scikit-learn.org/stable/common_pitfalls.html): separar desenvolvimento e teste antes de aprender transformações; não decidir o método olhando o teste. Aplicação aqui: novas fontes/comparadores após revelar resultados, normalização igual nas duas origens.
- NIST, [GenAI Text-to-Text](https://ai-challenges.nist.gov/t2t): avaliação de geradores e detectores e restrição à inspeção antecipada de dados de teste. Aplicação aqui: redator sem acesso ao teste, chave separada, detector não é juiz científico.
- NIST, [AITE](https://pages.nist.gov/ai-technology-evaluation/): dados cegos e ambiente separado para reduzir contaminação. Aqui a separação é de contexto e instrução, não controle de acesso do filesystem; todos os agentes tecnicamente compartilham o workspace. Auditar leituras e reportar vazamentos.

Essas fontes fundamentam o desenho de avaliação; não demonstram eficácia deste pipeline de cards nem garantem indistinguibilidade para Davi.

## Achado durante desenvolvimento

O lote v1 preservava créditos com HTML aninhado e alt com nomes de arquivos. Juízes foram instruídos a ignorar e relataram ignorá-los, mas isso não garante cegamento perfeito. V1 permanece evidência de desenvolvimento, com essa limitação explícita. normalize_field recebeu correção simétrica v2 e dois testes de regressão (22 testes passaram). Nenhum artefato v1 foi reescrito. Marcadores de mídia e diferenças no tamanho do Extra ainda são pistas possíveis; a transferência textual precisa de leitura que as trate separadamente.

## Rodada v3 — autoral por espelhos (02/10, Claude)

Mudança de desenho: em v1/v2 o redator via o card AnKing de origem e precisava escolher outro alvo. Em v3 um agente descreve o fato em português (`v3/targets.json`), o orquestrador anexa 3 espelhos AnKing vivos (`v3/make_briefs.py`, excluindo o original, irmãos e todo o corpus de teste) e o redator (`v3/AUTHOR-PROMPT.md`) nunca vê o original. Fatos, comparadores e calibração vêm de partições não usadas em v1/v2. Figuras foram retiradas das duas origens (`v3/make_batch.py`).

| Rodada | Modo | Autorais identificados | Acurácia | AUC |
|---|---|---|---|---|
| v1 (Codex) | frente / frente + Extra | 28/32 / 32/32 | 0,94 / 1,00 | — |
| v2 (Codex) | frente / frente + Extra | 31/32 / 30/32 | 0,98 / 0,97 | 0,995 / 1,00 |
| v3 treino | frente / frente + Extra | 7/24 / 8/24 | 0,65 / 0,67 | 0,74 / 0,75 |
| v3 teste | frente / frente + Extra | 3/32 / 4/32 | 0,53 / 0,55 | 0,70 / 0,74 |
| transferência Operon, antes | frente + Extra | 24/24 | 1,00 | 1,00 |
| transferência Operon, depois | frente + Extra | 24/24 | 1,00 | 1,00 |

Entre treino e teste o prompt recebeu só a lista de pistas do treino; o teste usou fatos, comparadores e juízes novos. AUC de 0,70–0,74 mostra sinal residual de ranking, apoiado sobretudo em sujeira de marcação dos nativos (procedência, não pedagogia). 32 por origem continua piloto pelo critério do card-mirror.

A transferência falhou como teste de estilo: 24 cards de um só tema raro num lote de biologia molecular variada formam um agrupamento que o juiz separa pelo assunto e pela repetição de molde (os espelhos do operon lac no AnKing são poucos e iguais). Lição incorporada ao card-author: com poucos vizinhos, buscar espelhos pela função em outros assuntos. Um teste válido de aula precisa comparar autorais com os AnKing da mesma aula, ou ser feito por Davi.

Limites desta rodada: juízes recebem o CLAUDE.md do projeto no contexto (descreve a regra do autoral); texto sem imagem; os alvos do teste v3 são fatos que o AnKing cobre, com vizinhos próximos, cenário mais fácil que lacunas de aula.


## Fechamento da v2 e limites de uso

A previsão de frente + Extra, gravada antes do término abrupto de uma sessão de juiz, foi pontuada em 10/10 sem alterar candidatos: 30/32 autorais identificados, 32/32 AnKing identificados, acurácia balanceada 0,969. A frente sozinha teve 31/32 autorais identificados e 32/32 nativos. O controle positivo reconheceu 8/8 autorais antigos e 8/8 AnKing; controle nulo com 24 AnKing recebeu pseudorrótulos aleatórios e deu 0,50 de acurácia, mas AUC 0,31 mostra que não demonstra calibração perfeita. A v2 contém 3 candidatos experimentais com falha dura no lint atual (`reserve-006`, `013`, `029`), incluindo incerteza da fonte que vazou para a frente; nenhum pode ir ao Anki. A tentativa posterior de julgar os mesmos itens sem formatação foi montada, mas não teve previsões; não atribuir-lhe resultado. A v3 com espelhos, descrita acima, é a melhora mais promissora, porém os resultados da própria aula FI05 e da transferência Operon impedem afirmar indistinguibilidade universal. Os próximos decks aplicam espelhos por função, avaliam autoria em amostras da própria aula e dependem da revisão de recuperação/fato/cobertura.
