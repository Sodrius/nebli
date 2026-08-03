# Pipeline canônico de deck-aula

## Ordem obrigatória

1. Extrair dos slides o escopo inicial e redigir a E1-base.
2. Quebrar a E1 em fatos-chave recuperáveis e criar a matriz `E1 -> fonte -> card`.
3. Buscar cada fato no AnKing do tema; selecionar card a card os que realmente carregam o mecanismo.
4. Buscar os fatos ainda descobertos nos outros decks de referência disponíveis.
5. Incorporar na E1, **antes da E2**, o aprofundamento diretamente útil encontrado nas fontes: mecanismo, contraste, exceção e correlação clínica que explica o assunto da aula.
6. Regerar a matriz a partir da E1 ampliada. Para cada fato nuclear, escolher nesta ordem: `anking`, `outro_deck`, `autoral`.
7. Só criar card autoral quando as duas buscas anteriores documentarem ausência ou cobertura insuficiente. O card autoral fecha uma lacuna específica; não duplica um card curado bom.
8. Montar o deck-aula com cópias dos cards curados e os autorais de lacuna. A E2 só é escrita depois de a matriz fechar; a E2 mede a E1 ampliada e o deck, não o slide isolado.

## Gates

- A E1 é primeiro atomizada em fatos-chave; a matriz é a fonte de verdade da completude. Não se aceita uma lista de “tópicos” ampla que esconda detalhes recuperáveis.
- Todo fato nuclear da E1 possui ao menos um card de referência ou autoral aprovado, com qualidade de cobertura `2` ou `3` em `0–3`: `0` ausente, `1` menciona mas não permite recuperar, `2` recupera o mecanismo/fato, `3` recupera e conecta mecanismo, contraste ou aplicação diretamente útil.
- Todo fato de apoio tem cobertura `>=1`; se for necessário para compreender um fato nuclear, também exige `>=2`.
- Todo card possui fato-chave e âncora na E1; não há card solto.
- Todo autoral registra as buscas negativas/insuficientes no AnKing e nos outros decks.
- Todo aprofundamento vindo dos decks tem decisão `incorporado` ou `dispensado` na E1, com justificativa; conteúdo nuclear não pode ser dispensado.
- A E2 é bloqueada até `validate_lesson_coverage.py` aprovar a matriz.
- Após a importação, o mesmo validador confirma que cada `card_ref` está realmente no deck-aula. Só então o deck recebe o status `revisável`.

O slide define o escopo. A E1 ampliada organiza a compreensão. Os cards curados são a fonte preferencial de recuperação; autoria é a camada de precisão para as lacunas reais.

## Orçamento de aprofundamento

Conteúdo de Step 1 não entra para inflar a aula. Cada acréscimo precisa marcar ao menos uma justificativa: `mecanismo_central`, `contraste_de_alto_erro`, `ponte_clinica_direta` ou `pré-requisito_imediato`. Se não puder responder “qual frase da E1 ele torna mais compreensível?”, fica fora ou vai para outra aula. A referência prática é: poucos acréscimos densos por parte, integrados à cadeia causal da aula, nunca uma segunda aula lateral sobre o mesmo sistema.

## Gate hard v2 — fechamento bloqueado
Uma aula nova não fecha com cobertura parcial. O manifesto deve declarar `deck_aula_gate: v2`, inventário atomizado com âncora literal de cada fato E1, pool AnKing consultado por fato e razão de keep/drop. Pelo menos 60% dos fatos nucleares devem entrar como cópia de card real AnKing/deck externo quando há candidatos; um card autoral só é permitido com a rejeição documentada do pool. Todo aprofundamento Step 1 selecionado deve estar na E1 antes da E2, com âncora literal. `gate_deck_aula_completo.py --verify-anki` é bloqueante para E2, PDF e .apkg; `PENDENTE-GERADO` é fila de trabalho, nunca estado de entrega.
