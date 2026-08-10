# MEMORY.md — estado vivo do NEBLI

Atualizado em 2026-08-10. Este arquivo contém apenas estado atual; histórico e
regras antigas estão em `docs/legacy/` e no Git.

## Projeto ativo

- Pipeline padrão E1 + deck-aula `.apkg` **rodou integralmente pela primeira vez** na aula
  `anato-intestino-grosso` (Intestino grosso, reto e canal anal — Anatomia, UC-8 Digestório,
  P1). Entrega: E1 de 17 páginas + APKG de 46 cards (11 Image Occlusion), auditado e
  renderizado em navegador.
- Leitura obrigatória do que a corrida ensinou: `RETROSPECTIVA-PROCESSO.md`.
- E2 e E3 seguem suspensas por não participarem da rotina atual de estudo.
- Retenção longitudinal: 25 novos/dia; cram pré-prova separado.

## Ferramentas que passaram a existir

- `flashcards/scripts/pdf_figura_io.py` — recorta figura do PDF de slides e monta Image
  Occlusion a partir das caixas de texto reais dos rótulos. Acabou o desenho manual de máscara.
- `flashcards/scripts/build_apkg_offline.py` — monta o `.apkg` direto em SQLite, sem Anki e
  sem AnkiConnect, lendo o `contrato-cobertura.json`. É o montador canônico.
- `flashcards/scripts/render_apkg_previews.py` — renderiza pergunta e resposta de cada card
  em Chromium. É o gate que enxerga o que o JSON não enxerga.
- Note types NEBLI: `Cloze NEBLI - Aula` (tema em campo, não no template) e
  `IO NEBLI - Image Occlusion (mapa coerente)` (imagem mascarada na frente, sem add-on).

## Decisões vigentes

- Sessão principal produz tudo; agentes apenas revisam e devolvem achados.
- Aula define o escopo; Step 1 aprofunda o mesmo mecanismo/estrutura.
- Ordem de fontes: AnKing → decks externos → autoral.
- Frente e terminologia autoral em inglês; Extra curto em português. Em IO de anatomia, os
  rótulos-resposta ficam na nomenclatura portuguesa da disciplina, que é como a prova cobra.
- Imagens: AnKing primeiro, depois decks privados; slide somente em último caso.
- Em prancha rotulada, a máscara cobre o nome da estrutura e deixa visível a explicação
  entre parênteses; rótulo rasterizado dentro da figura também precisa ser mascarado.
- Anatomia macro combina esquema de atlas e peça cadavérica real quando ambos existem.
- Entrega offline em APKG; AnkiConnect é utilitário legado, não dependência.

## Pendências bloqueantes

- **O índice privado do AnKing não atravessa para o ambiente de execução da aula.** Ele está
  íntegro no Drive (`Anking/AnKing-index-v2`, 564 MB; fonte de 5,9 GB), mas o conector do
  Drive devolve arquivo em base64 pelo contexto do modelo. Enquanto isso não for resolvido,
  toda aula sai com os cards marcados `blocked_private_index_unreachable`.
  Correção proposta: dossiê compacto de candidatos (`docs/canon/ANKING-PRIVADO.md`).
- Recuradoria da aula `anato-intestino-grosso` contra o AnKing, quando o índice estiver
  alcançável.
- Importar o APKG no AnkiDroid e conferir os 11 IO na tela do celular.
