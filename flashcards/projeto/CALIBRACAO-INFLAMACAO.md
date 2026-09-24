# Calibração real — Inflamação aguda

22/09/2026. Busca de leitura; nada aplicado ao Anki. Complementa a auditoria anterior com a restrição enfatizada pelo usuário: cobrir ESTA aula, não todo o assunto.

## Resultado

Havia candidatos úteis no próprio AnKing que não entraram na seleção inicial. Portanto, a próxima rodada não deve começar criando autorais. Também existem cards NEBLI revisados para várias lacunas. Os outros decks têm candidatos, mas alguns trazem excesso de conteúdo/clozes: não copiar indiscriminadamente para aumentar cobertura aparente.

A busca ampla por oito grupos recuperou 946 notas (não 946 cards aprovados), incluindo 727 notas AnKing e 113 de Histology. Houve falsos positivos; somente os candidatos pertinentes foram aprofundados. Evidência local em `arquivos-trabalho/auditoria-inflamacao-aguda-2026-09-22/busca-acervo.json` e consultas adicionais desta auditoria. Uma expansão por tag `*Pathoma::02_Inflammation::01_Acute_Inflammation*` retornou 110 notas; não é indicação de importar 110.

## Candidatos AnKing omitidos, realmente presentes

Pesquisar no navegador do Anki por `nid:<id>`. IDs pertencem à coleção inspecionada e não são identidade universal entre instalações.

| Nota de origem | Pergunta/recuperação | Vínculo com a aula | Decisão proposta |
|---|---|---|---|
| 1487640059152 | Liberação de ácido araquidônico e fosfolipase A2 | p. 13, figura e explicação | Candidato pertinente; selecionar clozes relevantes. |
| 1487640061733 | COX → prostaglandinas | p. 13 | Candidato direto. |
| 1487640101055 | 5-LOX → leucotrienos | p. 13 | Candidato direto. |
| 1487642661164 | Fagossomo e fusão com lisossomo | pp. 33–35 | Candidato direto. |
| 1487642714884 | Burst oxidativo e uso de O2 | p. 35 | Candidato; calibrar profundidade pela figura/fala. |
| 1487642718524 | Produto microbicida do burst | p. 35, figura | Candidato; comparar redundância com os seguintes. |
| 1487642722079 | NADPH oxidase e superóxido | p. 35, figura | Candidato de detalhe, não automaticamente obrigatório. |
| 1487642726245 | Superóxido → peróxido | p. 35, figura | Candidato de detalhe, decidir no mapa. |
| 1487642730357 | MPO e formação de HOCl | p. 35, figura | Candidato; evitar duplicar a mesma recuperação. |
| 1487642786172 | Macrófagos após neutrófilos | p. 29, curva e explicação | Candidato; conferir a janela temporal sem criar conflito artificial entre fontes. |

Essas dez notas não constavam na seleção original de 31 origens. “Encontrado” ainda não significa “aprovado para importar”: leitura de frente/verso renderizados, cloze correto, pertinência e redundância permanecem necessárias.

Outro candidato encontrado: 1545331567296 pergunta identificar abscesso como coleção localizada de pus. A mídia precisa ser inspecionada antes de aprovar identificação visual; não foi validada nesta busca. A nota 1473548771424 define abscesso pulmonar, mas seu contexto específico não deve substituir automaticamente o conceito geral.

## Outros decks e NEBLI já existente

| Origem | Candidato | Uso possível / limite |
|---|---|---|
| Histology | 1701515819045 | Cloze sobre enzimas degradadoras de MEC/colagenases; não trazer junto todos os detalhes de grânulos e membrana só por estarem na nota. |
| Histology | 1701280069196 | Histamina/permeabilidade; possui vários clozes sobre outros mediadores. Verificar se AnKing já cobre melhor; não adicionar por variedade. |
| Histology | 1701515682757 | Mecanismos dos grânulos; candidato secundário se uma recuperação relevante faltar, não pacote obrigatório. |
| Patologia antigo | 1756729011062 | Comparação dos mecanismos de permeabilidade; já tem histórico. |
| Patologia antigo | 1756729082220 | Causa da marginação; já tem histórico. |
| Patologia antigo | 1756729345752 | Destinos da inflamação; já tem histórico. |
| Patologia antigo | 1756729379882 | Flegmão versus abscesso; revisar formulação preservando o que já foi estudado. |

Não foi comprovado um bom candidato externo para cada lacuna visual/local. Uma busca sem resultado em termos específicos deve registrar “não encontrado nessas buscas”, não “não existe no AnKing”. Decks citados no mega prompt, mas não instalados/acessíveis, não contam como pesquisados.

## Exemplos de exclusão que precisam virar testes

- Chédiak-Higashi (1487642668958/1487642671204) apareceu na mesma vizinhança de fagolisossomo. A aula ensinar fagocitose NÃO obriga estudar toda essa imunodeficiência. Excluir do principal; uma ponte clínica somente se deliberadamente escolhida e adequada ao momento.
- Crohn (1482374315198) menciona flegmão/abscesso, mas pergunta qual doença inflamatória intestinal tem esses achados. NÃO cobre a distinção morfológica pedida na aula.
- Transcitose de IgA (1487117223955) não cobre transcitose vascular do edema. Termo coincidente, objetivo diferente.
- Estase em trombose, policitemia ou bile não substitui o encadeamento vascular da inflamação. A busca por `stasis` recuperou inclusive palavras como metastasis; filtragem lexical e leitura contextual são indispensáveis.
- Não expandir para granulomas, todo o complemento, farmacologia inteira dos anti-inflamatórios ou a lista completa de mediadores do Robbins.

## Ajuste na interpretação da auditoria anterior

Fagocitose, resposta linfática, cinética e padrões morfológicos não foram sugeridos só porque constam num livro: aparecem nos materiais desta aula (pp. 11, 29, 33–42). Continuam candidatos ao mapa da aula, na profundidade que o professor lhes deu.

Entretanto, “figura contém X” não impõe decorar toda a figura. Os mecanismos básicos, o detalhe enfatizado e a habilidade visual realmente ensinada são as unidades de decisão. A quantidade de cards necessária só deve ser calculada depois desse recorte.

Robbins & Cotran será referência científica e de aprofundamento do recorte; edição/capítulo integral ainda não acessados. Não marcar a revisão bibliográfica como concluída.

## Alvo da próxima calibração

Manter os bons cards do piloto, acrescentar os candidatos pertinentes, reutilizar associações existentes quando necessário e tornar visíveis as prioridades. Auditar separadamente lacunas e excessos. Só enviar para autoria um objetivo relevante sem cobertura após busca ampliada e verificação do acervo anterior.

Fontes: [material da aula](https://drive.google.com/file/d/1O5qLt4JANr93Hv7tEXeZ8TddmsiHKAjw/view); seleção em `curriculum/lessons/2026-uc03-patologia-38-inflamacao-aguda/selection.json`; coleção viva consultada por chamadas somente de leitura.
