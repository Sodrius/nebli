# Qualidade canônica dos cards

O modo ativo aceita somente `source=authored` e `source=io`. Todo texto final é português. Um card textual contém uma recuperação independente, exatamente uma ocorrência de `c1`, resposta de uma palavra por padrão, duas quando indispensáveis e três apenas com justificativa. Deve ser respondível em até dez segundos, ter âncora literal na E1, recuperação-alvo inequívoca e Extra curto, apenas explicativo.

Bloqueiam a entrega: cloze genérico, lista, mini-resumo, definição circular, oração inteira oculta, múltiplas relações, pista gramatical, vazamento lexical, resposta visível, alternativa plausível não resolvida, duplicação funcional e recuperação do rótulo quando o mecanismo é o alvo relevante.

Bloqueiam também, por medição e não por declaração:

- frente com prosa inglesa — o idioma é medido **só na frente**, porque um Extra em português não compensa uma frente em inglês;
- resposta abstrata que serve a qualquer frase (`tempo`, `tamanho`, `arquitetura`, `probabilidade`);
- resposta que oferece alternativas (`x ou y`, `x/y`) sem `compound_answer_reason`;
- resposta cujo termo não aparece na âncora da E1: o card não estreia conteúdo;
- card cuja informação discriminante mora só no Extra, que só é lido depois de responder;
- perda de ablação que apenas reformula o próprio card;
- duas recuperações do mesmo alvo sem `derivation_rationale`;
- defeito já apontado pelo usuário e registrado em `flashcards/tests/feedback_regressions.json`.

O agente registra `semantic_review` compacto com `ambiguity`, `anti_induction` e `duplicate_check`, mais `cue_quality` com o papel do cloze e a revisão cega. Métricas objetivas e hashes são calculados pelo validador.

O núcleo de retenção é congelado antes da autoria e passa por compressão e ablação. Cada card declara o que se ganha (`memory_gain`), o que se perde sem ele (`ablation_loss`), por que não basta ficar na E1 (`why_not_e1_only`) e qual confusão ele previne (`confusion_target`). Card sem perda concreta sai. Quantidade nunca é objetivo, e o teto do lote é congelado no contrato — nunca derivado do número de cards produzidos.
