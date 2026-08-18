# Visual e Image Occlusion

IO é card autoral visual. Usa `hide_two_guess_two`, uma ou duas máscaras e prefere duas quando o par é coerente. A máscara cobre o rótulo, nunca a estrutura. Prompt e respostas são portugueses; fonte e crédito são reais; coordenadas ficam entre 0 e 1.

`visual_review` confirma: `labels_masked_not_structures`, `question_preview`, `answer_preview`, `legible`, `no_leak` e `didactic_value`. Anatomia, histologia, radiologia e patologia exigem IO quando o objetivo envolve reconhecimento visual. Imagem sem tarefa cognitiva não entra.

Deck de aula cuja E1 registrou figuras não fecha inteiramente verbal. Quando o alvo do card é uma relação espacial, uma lâmina ou um ramo de fluxograma, a figura entra no Extra por `extra_images`, recortada naquele alvo — um ramo por card, nunca a mesma figura de tema repetida. Se de fato nenhum objetivo da aula envolver reconhecimento visual, a corrida declara `release_gate.visual_card_absence_rationale`; ausência silenciosa bloqueia.
