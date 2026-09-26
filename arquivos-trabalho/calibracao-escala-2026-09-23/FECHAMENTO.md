# Ajustes após as respostas — 23/09/2026

## Efetivamente feito

- Respostas preservadas em RESPOSTAS-ORIGINAIS; decisões em CALIBRACAO-ESCALA-V4. Entrada AGENTS/CLAUDE/MEMORY, comandos e runbook apontam para a mesma regra.
- Contrato separa qualidade de conteúdo, validade técnica, instalação, publicação e sync. E1 explicativa não é substituída por guia curto.
- Diagnóstico somente leitura implementado e testado; AnKing e os cinco acervos externos acessíveis, rota por campos/templates documentada. Não houve compra/importação de novos acervos.
- Genética e Complemento: APKGs existentes publicados e metadados privados conferidos. Recibos nas respectivas execuções. Publicação não certifica que esses decks antigos já passaram pela v4.
- Nenhuma escrita no Anki, alteração de carga diária, suspensão ou exclusão de cards nesta rodada.

## Fotografia atual

Fonte: `preflight-v4-2.json`. 332 cards / 238 notas médicas em seis aulas: Inflamação 68, Vascularização 88, Intestinos 41, Complemento 56, Genética 44, Fisiologia 35. Há 69 verdes, 1 laranja, 0 vermelhos, 0 rosas e 0 suspensos; 327 cards sem revisão registrada. Não inferir retenção.

`preflight-v4.json` é tentativa de desenvolvimento superada: a API não devolvia flags em cardsInfo e a primeira versão assumiu zero. **Não usar sua contagem de bandeiras.** A versão corrigida consulta `flag:0`…`flag:7` e a segunda leitura acima é válida. Ambas são parciais quanto ao nome do perfil: getActiveProfile não é suportado; confirmar na aplicação antes de escrever. Anki/acervos foram efetivamente acessados.

332/35 corresponde a cerca de dez dias apenas de introdução, sem descontar os cinco já iniciados nem incluir revisões futuras. Não é previsão de carga sustentada. A amostra de seis aulas não representa automaticamente todas as provas.

## Pendências explícitas para não se perderem

| Item | Estado / próximo passo |
|---|---|
| Comentário de imagem na artéria retal média | Aberto: nota 1790111511038, “poderia ter uma foto aqui”. Próxima revisão deve localizar imagem apropriada, inspecionar, aplicar/conferir na cópia e só então limpar laranja. Não foi marcado resolvido. |
| Intestinos: marcadores ilustrativos / prática | Feedback confirmado; reconferir seleção e fontes antes de editar. Não executar poda cega. |
| Clinical lateral repetido / excesso autoral | Auditoria anterior continua acionável; revisão semântica dos decks antigos não foi executada nesta consolidação. |
| Fisiologia: APKG local e vídeos nos campos | Estado histórico precisa ser reconciliado com a execução atual antes da próxima aula; não foi publicado nem editado nesta rodada. |
| Explanatory E1 existente por aula | Conferir adequação real ao recorte no próximo teste; guia publicado sozinho não comprova esta entrega. |
| Claude | Conector Drive conectado; testar upload binário e uma execução completa naquele executor. |
| Mac/Android | Sincronização e apresentação não testadas aqui. |
| Compartilhados Q18/Q22 | Uma identidade/histórico já aprovada; interface de seleções e apoio específico ainda requer explicação simples. Não duplicar/mover. |
| Pós-prova e 50 min/35 novos | Proposta confirmável; falta calibrar com uso real, sem suspensão automática. |

Próximo passo: usuário indica a aula/slide no Drive; executar o runbook com pendências anteriores visíveis e resolver o que estiver sustentado. Não escolher nova aula por conta própria. Só ampliar para lote 2–3 e depois escala maior conforme amostra, uso real e execução satisfatória no Claude.
