# PIPELINE_CADERNOS.md — Geração de cadernos de questões por UC

Pipeline recorrente para gerar PDFs editoriais ("cadernos de prova") a
partir do banco. Foi estreado em 2026-05-22 para UC01. **Reaplicar em
UC02, UC03, etc., trocando apenas o cronograma e o yaml de aulas.**

## Filosofia

- O banco (`banco/questoes/q-XXXX.md`) é a **única fonte de verdade**.
  Toda mudança canônica nas questões acontece lá; tudo o mais (slim,
  cadernos, relatórios) deriva.
- O campo `prova:` no frontmatter é **dado histórico** (qual prova
  original deu origem à questão). NÃO use para gerar cadernos atuais.
- A regra "qual prova hoje" vem de `banco/aulas_uc{N}.yml` (campo
  `prova` por slug). Este yaml reflete o cronograma vigente da UC.
- O gerador de cadernos consulta SEMPRE `aula:` (slug) → cronograma
  em runtime. Slug é a chave; cronograma é a regra externa que pode
  mudar ano a ano sem que o banco seja reescrito.

## Pré-requisitos por UC

Para gerar cadernos de uma UC nova (ex: UC02):

1. **Cronograma oficial** em `cronogramas/cronograma UC{N} {ano}.{png|pdf}`.
2. **YAML de aulas** em `banco/aulas_uc{N}.yml` com:
   - `slug` canônico por aula (padrão: `[disciplina]-[N]-[tema-curto]`)
   - Campo `prova: P1|P2|P3|P4` refletindo o cronograma vigente
   - Campo `titulo`, `ordem`, `docente`, `disciplina`
3. **Questões ingeridas** em `banco/questoes/q-XXXX.md` com:
   - `uc_origem: UC{N}`
   - `aula: <slug>` apontando para um slug do yaml acima (idealmente)
   - `formato: MC|CE|discursiva`
   - `gabarito:` no formato canônico do formato

## Sequência completa (UC01 como exemplo)

```bash
# 1. Audita gabaritos (formato, consistência, auto-correções inequívocas).
#    Saída: arquivos-trabalho/auditoria-gabaritos-UC1.md
#    Exit 2 se houver bloqueantes → corrigir antes de seguir.
python banco/auditar_gabaritos.py --uc UC1

# 2. Audita a classificação por cronograma (read-only).
#    Mostra: prontas, órfãs (→ caderno histórico), sem-aula,
#    divergências históricas.
#    Saída: arquivos-trabalho/classificacao-cronograma-UC1.md
python banco/classificar_por_cronograma.py --uc UC1

# 2b. Limpa mojibake da ingestão (sequências â€" etc).
python banco/limpar_mojibake.py --apply

# 2c. Restaura acentos PT-BR em palavras ASCII (ingestão OCR antiga).
python banco/corrigir_acentos.py --uc UC1 --apply

# 2d. Detecta questões que referenciam figura/gráfico/esquema.
#     Marca precisa_figura: true no frontmatter automaticamente.
#     Saída: arquivos-trabalho/questoes-com-figura-UC1.md (workflow
#     para popular figuras manualmente, recortando dos scans em
#     banco/figuras/PROVA_*.png).
python banco/detectar_figura.py --uc UC1 --apply

# 3. Regenera o índice slim (refletindo qualquer correção feita acima).
python banco/gerar_slim.py

# 4. Gera os cadernos HTML por prova (atualmente em desenvolvimento).
#    Cada caderno: capa + sumário + objetivas (MC+CE agrupadas
#    por aula) + discursivas no fim + gabarito consolidado +
#    apêndice de explicações.
#    Saída: typst-build/_cadernos/uc01-p1.html (e p2, p3, historico)
python typst-build/gerar_caderno.py --uc UC1 --prova P1
python typst-build/gerar_caderno.py --uc UC1 --prova P2
python typst-build/gerar_caderno.py --uc UC1 --prova P3
python typst-build/gerar_caderno.py --uc UC1 --prova HISTORICO

# 5. Renderiza HTML → PDF via motor de print (motor a definir:
#    WeasyPrint, Playwright headless ou Paged.js).
python typst-build/render_caderno.py --in typst-build/_cadernos/uc01-p1.html \
                                     --out resumos-gerados/CADERNO-UC01-P1.pdf

# 6. Auditoria do PDF final (fontes embarcadas, paths, tamanho).
python typst-build/auditar_caderno_pdf.py resumos-gerados/CADERNO-UC01-P1.pdf

# 7. Validação visual manual: abrir o PDF, conferir capa, sumário,
#    questões sem corte, gabarito, apêndice navegável.
```

## Critério de cada caderno

| Caderno | Regra de inclusão |
|---|---|
| `CADERNO-UC{N}-P1.pdf` | `aula in aulas_uc{N}.yml` e `aula.prova == 'P1'` |
| `CADERNO-UC{N}-P2.pdf` | idem para P2 |
| `CADERNO-UC{N}-P3.pdf` | idem para P3 |
| `CADERNO-UC{N}-HISTORICO.pdf` | `aula` declarada mas slug não está no yaml vigente |
| (fora dos cadernos) | `aula` vazia e sem palpite por tags — relatório lista para classificação manual |

Dentro de cada caderno: questões agrupadas por **aula** (na ordem do
cronograma), depois por **ano** decrescente, depois por **id**. Objetivas
(MC + CE) primeiro; discursivas em bloco unificado no fim, sem
gabarito visível. Gabarito consolidado de MC+CE em página dedicada
antes do apêndice de explicações.

## Estrutura de arquivos

```
banco/
├── auditar_gabaritos.py          # Fase 1 do pipeline
├── classificar_por_cronograma.py # Fase 2 do pipeline (read-only)
├── gerar_slim.py                 # Fase 3 do pipeline
├── aulas_uc01.yml                # Cronograma vigente UC01
├── aulas_uc02.yml                # Cronograma vigente UC02
└── questoes/q-XXXX.md            # Fonte da verdade

typst-build/
├── gerar_caderno.py              # Fase 4: banco → HTML
├── render_caderno.py             # Fase 5: HTML → PDF
├── auditar_caderno_pdf.py        # Fase 6: validação do PDF
├── _cadernos/                    # HTMLs intermediários
└── PIPELINE_CADERNOS.md          # este arquivo

arquivos-trabalho/
├── auditoria-gabaritos-UC{N}.md
└── classificacao-cronograma-UC{N}.md

resumos-gerados/
├── CADERNO-UC01-P1.pdf
├── CADERNO-UC01-P2.pdf
├── CADERNO-UC01-P3.pdf
└── CADERNO-UC01-HISTORICO.pdf
```

## Adicionando uma nova UC (checklist)

- [ ] Salvar cronograma oficial em `cronogramas/`.
- [ ] Criar `banco/aulas_uc{N}.yml` com slugs canônicos + prova vigente.
- [ ] Garantir que questões `uc_origem: UC{N}` tenham `aula:` preenchida
      (ou explicitamente vazia para casos não-classificáveis).
- [ ] Rodar `auditar_gabaritos.py --uc UC{N}` e zerar bloqueantes.
- [ ] Rodar `classificar_por_cronograma.py --uc UC{N}` e revisar
      categorias "sem-aula" e "órfã" — decidir caso a caso se vale
      classificar manualmente ou aceitar como histórico.
- [ ] Regenerar slim.
- [ ] Gerar os 4 cadernos (P1, P2, P3, HISTORICO).
- [ ] Auditar PDFs e validar visualmente.

## Estado atual do template (2026-05-22)

- Template visual: **HTML/CSS** (decisão canônica, Davi escolheu
  Claude Design para criar). Motor de render PDF: a decidir entre
  WeasyPrint, Playwright e Paged.js.
- Spec do template enviada a Claude Design: editorial sóbrio,
  paleta neutra (não-NEBLI), tipografia hierárquica, sem qualquer
  identificação de autor/instituição/marca.
- Helpers exigidos: `capa-caderno`, `sumario`, `abertura-bloco`,
  `questao-mc`, `questao-ce`, `secao-discursivas`,
  `gabarito-consolidado`, `apendice-explicacoes`.

## Decisões canônicas relevantes

- `prova:` no frontmatter = histórica de origem, não é fonte para os
  cadernos atuais (Davi, 2026-05-22).
- Discursivas vão todas para o fim de cada prova, sem gabarito visível,
  mesmo as que não têm modelo de resposta no banco (Davi, 2026-05-22).
- Órfãs (aula fora do cronograma vigente) vão para caderno-bônus
  histórico-ampliado (Davi, 2026-05-22).
- Auto-correção de gabarito é aceita; relatório fica salvo para
  auditoria posterior (Davi, 2026-05-22).
- Cadernos são publicações editoriais **anônimas**: nenhuma menção a
  pessoa, instituição, marca, NEBLI, FMUSP, contato (Davi, 2026-05-22).
