# CLAUDE.md — pasta typst-template

Esta pasta contém o template canônico do NEBLI.

## Antes de tocar em qualquer arquivo aqui

1. **`CHEATSHEET_ARMADILHAS.md`** — 10 bugs Typst recorrentes. Leia PRIMEIRO. Resolve 90% dos problemas.
2. **`TEMPLATE_API.md`** — assinaturas dos 35 helpers + 1 exemplo cada. Substitui leitura do `.typ` inteiro.
3. **`nebli_v2_apostila.typ`** — template ATIVO (Merriweather + Montserrat). Só abrir para detalhe de implementação de helper específico.
4. **`nebli_v1.typ`** — legacy (DejaVu). Preservado, não usar em resumos novos.

## Mudanças no template canônico

- Cada mudança visual exige aprovação Davi via amostra antes/depois.
- Backup obrigatório: `cp nebli_v2_apostila.typ nebli_v2_apostila.typ.bak-AAAA-MM-DD-Ax` antes de mexer.
- Mudança testada primeiro num `_test_X.typ` em `typst-build/`, nunca direto em resumo de produção.
- Documentar no `CHANGELOG_CLAUDE.md` (raiz do projeto).

## Pacote visual ativo (v3 — 2026-05-19)

Detalhes em `../MEMORY.md` § "Identidade visual ativa". Resumo:
- Corpo Merriweather 10pt, títulos Montserrat.
- `first-line-indent: 0em` (sem indentação de primeira linha).
- `spacing: 1.2em` entre parágrafos (reduzido de 1.5em em 2026-05-28), leading 1.0em.
- Margens `top: 1.7cm, bottom: 1.8cm, left/right: 1.9cm` (verticais reduzidas em 2026-05-28).
- Negrito do corpo em preto, não navy.
- Resumindo banner gold, títulos navy 10.5pt.
- PARTE 16pt navy bold + pagebreak antes (se não primeira).

## Mapas mentais

**Suspensos** (canônico 2026-05-19, ampliado 2026-05-28). Helpers proibidos:
- `#mapa-parte` (mapa SVG de PARTE — suspenso 2026-05-19).
- `#mindmap-fechamento` (mapa mental de fechamento da E1 — suspenso 2026-05-28).

Ambos são **no-op silencioso** no template para preservar compat retroativa de resumos antigos. Resumos NOVOS não devem chamar nenhum dos dois.
