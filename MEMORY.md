# MEMORY.md — estado vivo do NEBLI

Atualizado em 2026-08-11. Histórico e regras antigas permanecem em `docs/legacy/` e no Git.

## Estado atual

- Pipeline canônico: `e1-deck-v8`.
- A entrega só libera com `nebli-e1-deck-release-v1`: E1 fonte/PDF congeladas,
  revisão semântica independente, core nuclear 100% coberto e todo card ligado a
  uma âncora. Para Davi aparecem somente E1/PDF e manifesto do Companion.
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
- criar Image Occlusion diretamente, com `hide_all_guess_all` quando aplicável;
- separar opcionais em `<Deck>::Optional`;
- criar o deck com nome canônico `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`;
- resetar scheduling das cópias sem alterar a fonte;
- suspender siblings não selecionados;
- instalar de forma idempotente;
- fazer rollback das notas novas em falha parcial;
- selecionar/abrir o deck correto no AnkiDroid ao concluir.

## Decisões vigentes de card

- Ordem: AnKing adequado → deck externo adequado → autoral.
- Um card = uma recuperação independente, específica e relevante.
- Todo card deve ter âncora literal na E1.
- Não criar cards por cota; respeitar teto congelado da aula.
- Autorais: frente em inglês médico natural, Extra curto em português, exatamente um `c1`.
- Cloze: 1 palavra por padrão; 2 quando necessário; 3 raramente e com justificativa; 4+ bloqueia.
- IO: só quando reconhecimento/localização agrega; máscara cobre o rótulo-resposta, não a estrutura; multi-rótulo coerente usa `hide_all_guess_all`.
- Fonte visual real é preferência absoluta; mídia nova exige crédito e QA.
- AnKing/deck externo nunca é reescrito e a fonte nunca é modificada.

## Validação

- Gate final é **card a card, sem amostragem**.
- `expected_card_count == validated_card_count == passed_card_count` e `failed_card_count == 0`.
- CI mantém regressão realista de 40 cards, mas uma aula real valida o número real do deck.
- Um único card inválido bloqueia o lote.
- O recibo do Companion precisa confirmar `installed_card_count == expected_card_count`.

## Próxima corrida real

A próxima sessão deve receber os PDFs/arquivos da aula, ler `NEXT-SESSION.md` e rodar `/resumo` até o fim. Não pedir curadoria manual de cards. Entregar E1/PDF e **um único manifesto `.ankidroid.json`**; o usuário apenas abre esse arquivo no Companion para instalar o deck completo.

Não há pendência de infraestrutura que justifique voltar ao índice de 6 GB, Drive/Colab ou APKG como caminho normal. Se surgir falha nova numa aula real, corrigir o pipeline canônico e registrar em `ERROS.md` antes de considerar a aula concluída.
