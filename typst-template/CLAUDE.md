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

## Pacote visual ativo (v4 — 2026-09-07)

Detalhes em `../MEMORY.md` § "Identidade visual ativa". Resumo:
- **Corpo Merriweather 8,5pt** (era 10pt até 2026-09-07), títulos Montserrat. Amostra antes/depois de 4 graus aprovada por Davi; ver `../CLAUDE.md` § Tipografia compacta.
- `first-line-indent: 0em` (sem indentação de primeira linha).
- `spacing: 0.90em` entre parágrafos (1.5em → 1.2em em 2026-05-28 → 0.90em em 2026-09-07), **leading 0.60em** (era 1.0em).
- **Todo o fluxo de corpo escalado por 0,85 na mesma passada** — caixas, alternativas da E2, modelo da E3, legendas, footnotes, sumário, Resumindo e "Antes da aula". Mexer no corpo sem mexer nesses inverte a hierarquia: eles ficam maiores que o texto.
- PARTE 14pt (era 16), subtópico 10pt (era 11), legenda de figura 8pt (era 9,5), footnote 7,2pt (era 8,5).
- Margens `top: 1.7cm, bottom: 1.8cm, left/right: 1.9cm` (verticais reduzidas em 2026-05-28).
- Negrito do corpo em preto, não navy.
- Resumindo banner gold, títulos de seção navy 9,5pt e corpo 8,2pt em 2 colunas.
- PARTE com pagebreak antes (se não primeira) — tamanho na linha acima.
- **"Antes da aula" (`#pre-aula-page`, canônico 2026-08-28):** faixa **teal** (a capa é navy, o Resumindo é gold), corpo 9pt (era 10.5pt), leading 0.66em, margens laterais 2.2cm. Fica entre capa e sumário, 2 páginas, sem figura. A faixa teal é o sinal visual de que a seção vem ANTES do material, não dentro dele.

## Mapas mentais

**Suspensos** (canônico 2026-05-19, ampliado 2026-05-28). Helpers proibidos:
- `#mapa-parte` (mapa SVG de PARTE — suspenso 2026-05-19).
- `#mindmap-fechamento` (mapa mental de fechamento da E1 — suspenso 2026-05-28).

Ambos são **no-op silencioso** no template para preservar compat retroativa de resumos antigos. Resumos NOVOS não devem chamar nenhum dos dois.
