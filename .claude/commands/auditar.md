---
description: Roda auditoria textual + visual em um PDF do resumos-gerados/
argument-hint: <SLUG ou caminho.pdf>
---

Argumento recebido: $ARGUMENTS

Resolva o PDF:
- Se o argumento contém `.pdf`, use literal.
- Senão, assuma `resumos-gerados/<SLUG MAIÚSCULO>.pdf` — converta o slug para maiúsculas e troque `-` por `-` (manter), ex.: `ciclo-krebs` → `resumos-gerados/CICLO-KREBS.pdf`.

Localize o `etapa2.typ` correspondente em `typst-build/etapa2.typ` (atual) ou em `arquivos-trabalho/etapas-anteriores/<slug>/etapa2.typ` (histórico).

Rode em sequência (paralelo onde possível):

1. `python typst-build/auditar_pdf.py <pdf>` — auditoria textual (acentos ≥1,5%, paths /figuras/ existem, siglas sem duplicata, Merriweather embarcado).
2. `python typst-build/auditar_pdf_visual.py <pdf> --etapa2 <etapa2.typ>` — auditoria visual (Resumindo 1-2 pgs, sumário 1 pg, páginas em branco, header sincronizado, cores E2).
3. Se PDF tiver "CADERNO" no nome: rode também `python typst-build/auditar_caderno_pdf.py <pdf>` e `python typst-build/verificar_gabarito_ordem.py --apenas <pdf>`.

Reporte ao Davi em ≤200 palavras:
- ✅ PASS / ❌ ERROR / ⚠ WARN para cada auditor
- Lista enxuta de problemas encontrados (não output bruto)
- Sugestão de próximo passo (recompilar? aceitar com warnings? bloqueia distribuição?)
