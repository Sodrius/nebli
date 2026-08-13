# Qualidade canônica dos cards

O modo ativo aceita somente `source=authored` e `source=io`. Todo texto final é português. Um card textual contém uma recuperação independente, exatamente uma ocorrência de `c1`, resposta de uma palavra por padrão, duas quando indispensáveis e três apenas com justificativa. Deve ser respondível em até dez segundos, ter âncora literal na E1, recuperação-alvo inequívoca e Extra curto, apenas explicativo.

Bloqueiam a entrega: cloze genérico, lista, mini-resumo, definição circular, oração inteira oculta, múltiplas relações, pista gramatical, vazamento lexical, resposta visível, alternativa plausível não resolvida, duplicação funcional e recuperação do rótulo quando o mecanismo é o alvo relevante.

O agente registra `semantic_review` compacto com `ambiguity`, `anti_induction` e `duplicate_check`. Métricas objetivas e hashes são calculados pelo validador. O núcleo de retenção é congelado antes da autoria e passa por compressão e ablação; quantidade nunca é objetivo.
