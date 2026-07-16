# CONTEXTO DO DEBATE — Anti-indução (semente do `lint_neblicard.py`)

> Pacote de aterramento para os 5 agentes do ringue. Regra-mãe: **toda afirmação admite exemplar ou métrica NEBLI real** (evidence-admission). Opinião sem âncora é inadmissível e o Juiz a descarta.

## A PERGUNTA DESTA CORRIDA (uma só)
**Como medir AUTOMATICAMENTE se um cloze é adivinhável sem saber a matéria (reconhecimento vs recall)?**
Saída desejada: a **spec do `lint_neblicard.py`** — um linter que roda ANTES do card-mirror, como gate de fechamento de card, e reprova cards induzíveis. Barato (regex/heurística), determinístico, auditável. O card-mirror (caro, LLM) fica só pro resíduo que passa no linter.

## POR QUE ISSO IMPORTA (medido, não opinado)
- Deck-prova P3 saiu **6/10**. Diagnóstico-mãe da auditoria card-mirror (Opus): **≈45% dos cards testam RECONHECIMENTO, não recall** — o cloze é adivinhável só lendo a frase. É a inversão do craft AnKing.
- Pergunta de ouro por card (já canônica): *"dá pra acertar o branco sem saber a matéria?"*. Se sim, reprovar.

## OS 4 PADRÕES DE LEAK JÁ IDENTIFICADOS (CARD-MIRROR-RUBRICA § Rodada P3)
1. **NAME-in-stem leak** — nome da estrutura aparece no stem (pior: em **negrito**) e o cloze apaga a *descrição*. Ler o nome entrega o branco.
   - ERRADO: `O neurônio **multipolar** tem {{c1::vários dendritos e um único axônio}}`
   - CERTO: `Which neuron has one axon + multiple dendrites? {{c1::Multipolar}}`
2. **Parêntese/aposto que entrega** — exemplos, sinônimo ou número entre parênteses no stem que dá o branco de graça (três cúspides → tricúspide).
3. **Cloze-dump** — branco de 4+ palavras-conteúdo (dump). Deveria ser 1-3 palavras atômicas, um fato por branco.
4. **Auto-entrega da sigla** — apagar sigla com a expansão visível na mesma frase (`Mucosa-associated lymphoid tissue is {{c1::MALT}}`).

## TELLS REAIS confirmados no lote cego P3-rebuild EN (2026-07-13) — o que É discriminador
- **nº1: mecanismo dentro do STEM da frente** ("sealing passively by their nest shape" DENTRO da pergunta). Nenhum dos 50 exemplares AnKing faz isso. Separador mais confiável.
- **nº2: cloze de frase-mecanismo (5+ palavras)** em vez de token.
- **nº3: cloze que se auto-entrega** (sigla+expansão na mesma frase).

## TELLS-RUÍDO — NÃO são discriminadores (AnKing real também faz). NÃO PERSEGUIR NO LINTER:
- Extra abrindo com "Thus"; crédito com DOI longa; Extra que reafirma a frente.
- **FEATURE DELIBERADA (não é defeito): Extra explicativo.** Davi já decidiu (meta-aval P3) que Extra que explica o porquê é **recurso desejado**. O linter de indução NÃO deve punir Extra explicativo — indução é sobre a FRENTE/cloze, não sobre o Extra.

## CONVENÇÕES TÉCNICAS DO CARD (pro linter parsear)
- Note type: `AnKingOverhaul`. Campos: Text (frente com cloze), Extra, selo `❖ NEBLIcard`, tag `NEBLI::gerado`.
- Cloze: sintaxe `{{c1::resposta}}` ou `{{c1::resposta::hint}}`. Multi-cloze c1/c2/c3.
- Corpo em INGLÊS.
- Cloze single ideal: branco de ~1-3 palavras no token de maior valor.

## RUBRICA DO JUIZ (0-5 por eixo, só evidência admitida)
(a) fidelidade ao exemplar AnKing · (b) valor de retenção/didática · (c) viabilidade no pipeline (é regex/heurística barata e determinística?) · (d) alinhamento ao Davi (respeita o Extra explicativo? é gate antes do card-mirror?).

## CONVERGÊNCIA (Juiz só declara "inequívoco" se as 3 baterem)
(i) top vence 2º por margem ≥ 3 pontos no placar somado; (ii) Cético sem objeção red-team sem resposta; (iii) ranking estável por 2 rodadas.

## ARQUIVOS-FONTE (leia se precisar de exemplar literal)
- `flashcards/CARD-MIRROR-RUBRICA.md` — § Rodada P3, § lote cego P3-rebuild EN, § meta hierarquia de tells.
- `flashcards/ANTI-EXEMPLARES-CARDS.md` — padrões de indução e matches falsos a evitar.
- `flashcards/ANKING-DOSSIE-TEXTO.md` — 50 cards AnKing reais (exemplares positivos: como é a frente/cloze nativo).
