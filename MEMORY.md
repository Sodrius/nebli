# MEMORY.md — estado vivo do NEBLI

Atualizado em 2026-08-17. Histórico e regras antigas permanecem em `docs/legacy/` e no Git.

## Estado atual

- Pipeline canônico: `e1-deck-v12`.
- Deck-Aula = núcleo mínimo de retenção, com slots prévios à busca, cards de até 10 s e revisão de compressão/ablação; detalhes deriváveis não recebem cards próprios.
- A entrega só libera com `nebli-e1-deck-release-v1`: E1 fonte/PDF congeladas,
  revisão semântica independente, core nuclear 100% coberto e todo card ligado a
  uma âncora. Para Davi aparecem somente E1/PDF e manifesto do Companion.
- E1 nunca é documento Typst autônomo: importa o template oficial, é montada por
  `main.typ` com `pagina-padrao`, capa/sumário/etapa e `resumindo.typ`, e passa
  revisão visual de todas as páginas. Redefinição local de página/parágrafo,
  clipping, overflow ou defeito visual pendente bloqueiam o release.
- Produto padrão: **E1 + Deck-Aula completo no AnkiDroid**.
- Backend normal: AnkiDroid via Nebli Companion.
- Schema final: `nebli-ankidroid-deck-v3`.
- E2, E3 e RemNote desligados.
- Retenção longitudinal: 25 novos/dia; revisões 9999/dia.
- Desktop/APKG/Drive/Colab não pertencem ao fluxo normal.
- O Nebli Companion final foi instalado e os testes reais de conexão, busca local e cópia segura no AnkiDroid passaram no tablet.

## O que o Companion final suporta

- buscar AnKing diretamente na coleção local;
- copiar AnKing com note type/campos/HTML/clozes/tags/mídia preservados;
- usar deck externo local com filtro/ranking e a mesma política de cópia segura;
- criar cards autorais diretamente no AnkiDroid;
- importar mídia nova para Extra de autorais, exigindo função cognitiva e crédito;
- criar Image Occlusion diretamente, com `hide_two_guess_two` e alvo de duas respostas coerentes por card;
- separar opcionais em `<Deck>::Optional`;
- criar o deck com nome canônico `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`;
- resetar scheduling das cópias sem alterar a fonte;
- suspender siblings não selecionados;
- instalar de forma idempotente;
- fazer rollback das notas novas em falha parcial;
- selecionar/abrir o deck correto no AnkiDroid ao concluir.

## Decisões vigentes de card

- Autoral direto: `authored_only` dispensa busca externa, e o Companion recusa
  manifesto com `source=anking`/`external_deck`.
- Um card = uma recuperação independente, específica e relevante.
- Todo card deve ter âncora literal na E1.
- Não criar cards por cota; respeitar teto congelado da aula.
- Todos os cards finais: frente, Extra, prompt e respostas de IO em português. Autorais usam exatamente um `c1` e gate universal anti-indução; rótulo estrangeiro de IO permanece coberto e recebe sobreposição em PT-BR.
- Cloze: 1 palavra por padrão; 2 quando necessário; 3 raramente e com justificativa; 4+ bloqueia.
- IO: só quando reconhecimento/localização agrega; máscara cobre o rótulo-resposta, não a estrutura; usar uma ou duas máscaras, com `pair_rationale` quando forem duas.
- Card autoral procura primeiro mídia local do AnKing; slide/externa exige rejeição documentada. Toda imagem exige propósito cognitivo, crédito e QA didático.
- AnKing/deck externo nunca é reescrito e a fonte nunca é modificada.

## Gates que medem em vez de acreditar

Desde v12, o validador não aceita declaração no lugar de evidência:

- idioma medido **só na frente** — Extra em português não compensa frente inglesa;
- `cue_quality` com papel do cloze e revisão cega, aplicado de verdade
  (a função existia e nunca era chamada);
- resposta abstrata, resposta com alternativas (`x ou y`) e termo ausente da
  âncora da E1 bloqueiam;
- card cuja informação discriminante mora só no Extra bloqueia;
- contrato de ablação por card: `memory_gain`, `ablation_loss`, `why_not_e1_only`
  e `confusion_target`; perda que só reformula o card bloqueia;
- `card_budget_hard_max` ausente bloqueia — o teto nunca deriva da contagem;
- duplicação funcional por resposta e por alvo exige `derivation_rationale`;
- IO exige `visual_evidence` com previews hasheados, `crop_ratio`, varredura de
  texto e termos proibidos cobrindo as respostas.

## Feedback do usuário

- Comentário e resposta sobrevivem à recriação da nota: `installOne` lê o
  feedback antes do delete e o recibo registra `feedback_carried`/`feedback_lost`.
- Note type IO é `NEBLI Image Occlusion v2`, com `NEBLI_Comentario`,
  `NEBLI_Resposta` e `NEBLI_Historico`.
- `ler_comentarios.py` acha comentário por campo preenchido, não só por tag, e
  **nunca apaga** o comentário ao responder.
- Todo comentário vira entrada em `flashcards/tests/feedback_regressions.json`,
  e o teste roda cada exemplo reprovado contra o gate real.

## Auditoria

- `audit_apkg.py --deck "<deck>"` audita uma aula, não a coleção.
- `apkg_utils.models_map` popula campos no schema novo do Anki; sem isso a
  auditoria era estruturalmente cega em qualquer `.apkg` recente.

## Validação

- Gate final é **card a card, sem amostragem**.
- `expected_card_count == validated_card_count == passed_card_count` e `failed_card_count == 0`.
- CI mantém regressão realista de 40 cards, mas uma aula real valida o número real do deck.
- Um único card inválido bloqueia o lote.
- O recibo do Companion precisa confirmar `installed_card_count == expected_card_count`.

## Pendência conhecida

- O deck UC03 no AnkiDroid é anterior a estes gates: frentes em inglês, clozes
  genéricos, IO com resposta duplicada e notas sem `tier`/`concept`. Regenerar
  aula por aula, começando por Radiologia (20 cards).
- O Companion foi alterado sem compilar (sem Android SDK no ambiente da
  correção). Rodar `gradle test` antes de gerar o APK.

## Próxima corrida real

A próxima sessão deve receber os PDFs/arquivos da aula, ler `NEXT-SESSION.md` e rodar `/resumo` até o fim. Não pedir curadoria manual de cards. Entregar E1/PDF e **um único manifesto `.ankidroid.json`**; o usuário apenas abre esse arquivo no Companion para instalar o deck completo.

Não há pendência de infraestrutura que justifique voltar ao índice de 6 GB, Drive/Colab ou APKG como caminho normal. Se surgir falha nova numa aula real, corrigir o pipeline canônico e registrar em `ERROS.md` antes de considerar a aula concluída.
