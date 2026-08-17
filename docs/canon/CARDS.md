# Schema ativo de cards

Campos textuais informados: `card_key`, `concept_id`, `tier`, `source=authored`, `text`, `extra`, `e1_anchor`, `retrieval_target`, `semantic_review`, `authored_quality`, `cue_quality` e o contrato de ablação — `memory_gain`, `ablation_loss`, `why_not_e1_only` e `confusion_target`.

Justificativas condicionais: `three_word_cloze_reason` quando a resposta tem três palavras, `compound_answer_reason` quando a resposta traz `/` ou `ou`, e `derivation_rationale` quando outro card do mesmo conjunto recupera a mesma resposta ou o mesmo alvo.

`cue_quality` traz `cloze_role` (um entre `mecanismo`, `consequencia`, `discriminador`, `valor`, `direcao`, `rotulo_especifico`), `knowledge_required`, `blind_review_passed`, `grammar_only_solvable`, `lexical_leak`, `answer_visible_elsewhere`, `plausible_alternatives` vazio, `confounders_checked` e `ambiguity_review`.

Campos IO informados: identidade, `source=io`, `e1_anchor`, `mode=hide_two_guess_two`, `prompt` em português, uma ou duas `answers`, máscaras normalizadas, `pair_rationale` para duas, `image_path`, `source_credit`, `cognitive_purpose`, `visual_review` e `visual_evidence`.

`visual_evidence` traz os dois previews renderizados com hash, `crop_ratio`, `text_scan` (`ocr` ou `manual_review`), `forbidden_terms` — que precisa listar todas as respostas — e `leaked_terms` vazio.

O contrato do lote informa `card_budget_hard_max`. Sua ausência bloqueia: o teto nunca é derivado do número de cards produzidos.

Não declarar contagem/índice de cloze, palavras, caracteres, idioma, hashes ou contagens finais: os scripts derivam esses dados.
