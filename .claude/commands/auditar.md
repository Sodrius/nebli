---
description: Audita uma entrega E1 + deck-aula já produzida
argument-hint: <contrato.json> <deck.apkg>
---

# /auditar — gate final E1 + deck

Argumentos: $ARGUMENTS

Leia o contrato v3, a E1 congelada e os documentos canônicos. Não produza nem
corrija artefatos durante a revisão. Execute:

```bash
python flashcards/scripts/gate_deck_aula_completo.py \
  <contrato.json> --apkg <deck.apkg>
```

Depois renderize todos os cards autorais e de Image Occlusion, toda mídia
alterada e uma amostra estratificada das cópias reais. Classifique achados em
`BLOCK`, `FIX`, `NOTE` ou `FALSE_POSITIVE`. Verifique especialmente: cobertura
nuclear, âncoras E1, limite do Step 1, origem/GUID, mídia, máscaras, vazamento,
subdeck Optional, modelos, total real versus teto, atomicidade, clozes de 1/2/3
palavras e importabilidade. Para IO, confira que a pergunta cobre os
rótulos-resposta, mantém as estruturas visíveis e que mapas multi-rótulo usam
`hide_two_guess_two`, no máximo duas respostas e `pair_rationale` quando houver duas. A auditoria não edita; a sessão
principal aplica correções e roda o gate novamente.
