# Diagnóstico do pipeline — 2026-08-12

Levantado durante a primeira corrida real do `e1-deck-v9` numa aula nova
(`imuno-01-reconhecimento-inato`). O pedido era rodar o pipeline inteiro e, no
caminho, achar o que faz o deck não sair como o Davi quer.

Os quatro problemas abaixo têm a mesma raiz: **o gate media declarações, não
conteúdo**. Todo o contrato de qualidade estava escrito em prosa e verificado
por booleanos que a própria sessão preenchia. Enquanto a sessão for quem
declara e quem é avaliado, o pipeline converge para “preencher o formulário”, e
não para “fazer um card bom” — e o deck passa em 100% dos gates sendo,
ainda assim, o deck errado.

---

## 1. O relatório card-a-card não era do deck

**O que acontecia.** `validacao-cards.json` era escrito à mão, em paralelo ao
`deck-data.json`. Os dois arquivos nunca se olhavam. O finalizador só conferia
que os `card_key` batiam. Então um card com cloze de cinco palavras podia
declarar `cloze_words: 1`; um card sem âncora podia declarar
`e1_anchor_ok: true`; um card com frente de 600 caracteres podia declarar 200.
O gate aprovava, com “100% dos cards validados, sem amostragem”, um deck que
ninguém tinha medido.

**Por que isso estraga o deck.** Não é fraude deliberada: é que, com dois
arquivos, o caminho barato é ajustar o relatório até passar, e não o card até
ficar bom. O número “52/52 aprovados” deixa de carregar informação.

**Correção.** `flashcards/scripts/derivar_validacao_cards.py`. O relatório passa
a ser derivado do deck: contagem e índice de cloze, palavras da resposta,
tamanho da frente, palavras do Extra, número e geometria de máscaras, crédito de
mídia — tudo lido do card real. A âncora E1 é conferida contra o arquivo-fonte
da E1, não contra uma declaração. O que é juízo (`atomic`, `relevant`, previews
revisados) continua declarado, mas é *copiado* do deck-data: existe uma única
fonte da verdade, e um flag ausente reprova em vez de ser inventado.

O finalizador ganhou `_crosscheck`: se o relatório afirmar sobre um card algo
que o card desmente, a entrega para. Fatos de resolução (score, note type,
sibling) ficam de fora do cross-check porque pertencem ao aparelho, não ao
plano.

---

## 2. Qualidade funcional não tinha nenhum executor

**O que acontecia.** `ERROS.md` 36–47 descreve com precisão o que é um card
ruim: cloze genérico, resposta que vaza na frente, metade de um par canônico,
enumeração disfarçada, duplicata funcional. Nada disso era verificado por
código. O gate checava um `c1`, cloze curto, Extra em português — forma. Um card
formalmente perfeito cobrando `{{c1::ativação}}` passava.

**Correção.** `flashcards/scripts/lint_qualidade_funcional.py`, chamado dentro
do gerador no caminho estrito, portanto impossível de pular. Bloqueia:

- resposta em lista de termos genéricos/previsíveis (com escape explícito por
  escrito, `generic_answer_reason`, para quando o termo comum é mesmo a resposta
  exata);
- resposta que reaparece na parte visível da frente;
- cloze que esconde mais de uma resposta (vírgula, “and”, “/”);
- frente que pede enumeração;
- padrão `X and {{c1::Y}}` sem `pair_is_unit_reason`;
- mesma resposta em dois cards do deck sem `duplicate_answer_reason`;
- frente curta demais para tornar a resposta inequívoca;
- IO com respostas repetidas ou rótulo genérico.

Efeito prático nesta aula: o lint reprovou de saída um card
(`Type I interferon ... body ache and {{c1::fever}}`) por mostrar metade do par.
Ele foi reescrito, não justificado.

---

## 3. A prioridade AnKing exigia provar uma busca impossível

**O que acontecia.** O canônico manda buscar AnKing antes de autorar, e o gate
exigia, de todo card não-AnKing, `anking_search_complete=true`, três consultas
independentes, expansão de escopo, revisão de siblings, contagem de candidatos e
motivo de rejeição. **A coleção AnKing não existe na sessão de planejamento** —
ela vive no AnkiDroid do tablet e só o Companion a enxerga. Ou seja: a única
maneira de o pipeline terminar era declarar como feita uma busca que ninguém
podia ter feito.

Havia ainda uma segunda confusão: para `source="anking"` o gate exigia `score`,
`same_note_type`, `sibling_policy_ok` e `resolved_without_fallback` **no plano**.
São todas propriedades do *resultado* da busca. No plano elas não existem.

**Por que isso estraga o deck.** Um requisito impossível não vira bloqueio: vira
declaração falsa. E, uma vez que declarar é fácil, some a diferença entre “não
havia AnKing adequado” e “ninguém procurou” — que é exatamente a diferença que
decidia se o card deveria ser autoral.

**Correção.** Procedência explícita, em `anking_search_mode`:

| modo | significado | o que o gate exige |
|---|---|---|
| `session_local` | a coleção estava ao alcance e a busca aconteceu | contrato antigo, intacto |
| `device_deferred` | a resolução roda no Companion, no aparelho | 3 consultas planejadas, `expected_answers`, fallback validado, `anking_required=false` |
| `unavailable` | nenhuma coleção ao alcance; card autoral/IO | `anking_deferral_reason` concreto (≥40 caracteres) |

Fonte local com `unavailable` é recusada — uma fonte local só faz sentido se
alguém, sessão ou Companion, for de fato procurar nela. E em `device_deferred` o
gate valida o que o plano pode provar (consulta, resposta esperada, o card que
entra se a busca falhar), deixando score e sibling para o recibo pós-instalação.

O manifesto passa a registrar a distribuição dos modos em
`search.anking_search_modes`, então o recibo mostra de onde veio cada card em
vez de todos aparecerem como “autoral após busca completa”.

---

## 4. Cobertura era presença, não profundidade

**O que continua valendo a pena olhar.** O release gate exige que todo conceito
nuclear tenha `coverage_quality>=2` e pelo menos um card — mas quem escreve os
dois números é a mesma sessão. Não há checagem de *proporção*: um conceito com
peso de meia aula e um conceito de nota de rodapé satisfazem o gate igualmente
com um card cada.

Nesta corrida isso foi resolvido à mão, distribuindo cards pelo peso real dos
slides (5 cards para o recap, 15 para famílias/ligantes, 15 para vias e
inflamassoma, 17 para efetuação e citocinas). Fica registrado como a próxima
correção mecânica candidata: mapear `objectives[]` da aula → conceitos → cards e
recusar objetivo sem cobertura, em vez de confiar na distribuição feita a olho.

---

## Regressões

`flashcards/tests/test_qualidade_funcional_e_modos.py` cobre os três problemas
corrigidos: divergência entre número declarado e card real, âncora ausente da
E1, cada uma das checagens do lint, e os três modos de procedência (incluindo a
recusa de fonte local sem busca e de busca delegada com `anking_required`).

Suíte completa: 76 testes, todos passando.
