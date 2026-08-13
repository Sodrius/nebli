# Schema ativo de cards

Campos textuais informados: `card_key`, `concept_id`, `tier`, `source=authored`, `text`, `extra`, `e1_anchor`, `retrieval_target`, `semantic_review` e, quando aplicável, `three_word_cloze_reason`.

Campos IO informados: identidade, `source=io`, `e1_anchor`, `mode=hide_two_guess_two`, `prompt`, uma ou duas `answers`, máscaras normalizadas, `pair_rationale` para duas, `image_path`, `source_credit`, `cognitive_purpose` e `visual_review`.

Não declarar contagem/índice de cloze, palavras, caracteres, idioma, hashes ou contagens finais: os scripts derivam esses dados.
