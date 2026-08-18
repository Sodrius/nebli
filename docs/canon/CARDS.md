# Schema ativo de cards

Campos textuais informados: `card_key`, `concept_id`, `tier`, `source=authored`, `text`, `extra`, `e1_anchor`, `retrieval_target`, `semantic_review`, `authored_quality`, `cue_quality` e o contrato de ablação — `memory_gain`, `ablation_loss`, `why_not_e1_only` e `confusion_target`.

Justificativas condicionais: `three_word_cloze_reason` quando a resposta tem três palavras, `compound_answer_reason` quando a resposta traz `/` ou `ou`, `derivation_rationale` quando outro card do mesmo conjunto recupera a mesma resposta ou o mesmo alvo, `type_hint_not_needed_reason` quando a frente já entrega a categoria da resposta, e `long_front_reason` quando a frente passa do teto de estilo.

Resposta de uma palavra leva dica de tipo dentro do cloze — `{{c1::resposta::dica}}` —, para o erro nascer de não saber o conteúdo e não de não saber a categoria pedida. A dica delimita, nunca entrega: repetir a resposta ou compartilhar palavra com ela bloqueia. Expressão de duas palavras dispensa a dica, porque já nomeia a própria categoria.

Imagem em card autoral entra por `extra_images`, uma lista de objetos com `path`, `source_credit`, `cognitive_purpose`, `didactic_value_reviewed` e `alt`. A imagem precisa treinar o alvo daquele cloze; figura de tema colada em vários cards é defeito, não cobertura. O bloco renderizado vai para o verso, então uma figura que nomeia a resposta não vaza — ela só é lida depois da recuperação.

`cue_quality` traz `cloze_role` (um entre `mecanismo`, `consequencia`, `discriminador`, `valor`, `direcao`, `rotulo_especifico`), `knowledge_required`, `blind_review_passed`, `grammar_only_solvable`, `lexical_leak`, `answer_visible_elsewhere`, `plausible_alternatives` vazio, `confounders_checked` e `ambiguity_review`.

Campos IO informados: identidade, `source=io`, `e1_anchor`, `mode=hide_two_guess_two`, `prompt` em português, uma ou duas `answers`, máscaras normalizadas, `pair_rationale` para duas, `image_path`, `source_credit`, `cognitive_purpose`, `visual_review` e `visual_evidence`.

`visual_evidence` traz os dois previews renderizados com hash, `crop_ratio`, `text_scan` (`ocr` ou `manual_review`), `forbidden_terms` — que precisa listar todas as respostas — e `leaked_terms` vazio.

O contrato do lote informa `card_budget_hard_max`. Sua ausência bloqueia: o teto nunca é derivado do número de cards produzidos.

Não declarar contagem/índice de cloze, palavras, caracteres, idioma, hashes ou contagens finais: os scripts derivam esses dados.
