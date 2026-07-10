# CLAUDE.md — pasta banco/

Banco de questões NEBLI. Hoje: 413+ questões em `questoes/q-XXXX.md`.

## Antes de operar no banco

1. **`indice/banco_slim.json`** — frontmatter sem `itens` por alternativa. Use para classificação (filtro E4, busca por aula). Não ler `.md` completo de cada candidata.
2. **`aulas_uc01.yml`** — master list de aulas UC01 (41 aulas, slug canônico por aula, calendário oficial 2026 turma 114).
3. **`meta/PIPELINE.md`** e **`meta/CONVENCOES.md`** — schema, naming, fluxo de ingestão.

## Schema das questões (frontmatter YAML)

Campos canônicos: `id`, `tags`, `aula` (slug ou vazio), `nivel`, `formato` (MC/CE/discursiva), `gabarito`, `uc_origem`, `prova`, `ano`, `armadilha`, `conceito_central`, `itens` (alternativas).

### Campos de figura (canonizados 2026-05-22)

Três campos novos para questões que dependem visualmente de figura/gráfico/esquema:

- `precisa_figura: true | false` — flag. Marcada automaticamente pelo `detectar_figura.py` quando o enunciado contém padrão indicativo ("indique na figura", "observe o gráfico", "esquema abaixo", etc).
- `figura: "q-XXXX.png"` — nome do arquivo em `banco/figuras/` (caminho relativo a essa pasta). Vazio se ainda não recortada.
- `figura_descricao: "..."` — descrição textual da figura (fallback se imagem ausente, ou quando a "figura" já está embutida no enunciado como texto).

Comportamento no caderno gerado:
- Se `figura:` aponta para arquivo existente → imagem é embutida na questão.
- Se `precisa_figura: true` e `figura:` vazio → aviso visual destacado "FIGURA REFERENCIADA" no caderno, com `figura_descricao` se houver.
- Se `precisa_figura: false` → nada acontece (campo `figura_descricao` ignorado pelo caderno mas mantido como metadado).

Workflow para popular figura ausente:
1. Abre a prova original em `banco/figuras/PROVA_*.png` (scans completos).
2. Recorta a figura específica.
3. Salva como `banco/figuras/q-XXXX.png` (mesmo número da questão).
4. Edita o frontmatter: `figura: "q-XXXX.png"`.
5. Re-gera o caderno.

## Filtro E4 — UC ativa

```bash
# já classificadas
grep -l 'aula: bioq-15-glicolise' banco/questoes/*.md

# candidatas (grep amplo, ler banco_slim para decidir)
grep -l -i -E "glicolise|hexoquinase|piruvato" banco/questoes/*.md
```

Classificar autônomamente as candidatas via `banco_slim.json`. Gravar `aula: <slug>` no `.md` quando o conceito central da questão é o tema da aula.

## Atualização do banco

Provas novas:
1. Transcrever para `arquivos-trabalho/exames-transcritos/`.
2. Inserir via `banco/ingest.py` (ou manual seguindo schema).
3. Classificar `aula: <slug>` consultando `aulas_uc01.yml`.
4. **Detectar figuras: `python banco/detectar_figura.py --uc UCx --apply`**
   Marca `precisa_figura: true` em questões com referência indicativa.
   Output: `arquivos-trabalho/questoes-com-figura-UCx.md` — workflow para
   popular as figuras manualmente.
5. Regenerar índice: `python3 banco/gerar_slim.py`.

Nunca alimentar diretamente os xlsx. Fluxo: md primeiro, xlsx regenerado se preciso.
