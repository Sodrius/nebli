# flashcards/ — lar do trabalho de cards NEBLI

> Hub único de tudo que é relacionado aos cards Anki. Criado 2026-07-10 a pedido de Davi; a migração física dos scripts e dados foi executada na mesma data. O **porquê e as regras** vivem em `FLASHCARDS.md` (raiz — carregado no canônico); esta pasta guarda **conhecimento, dados, scripts e planejamento** dos cards.

## Estrutura

```
flashcards/
├── README.md                 este hub
├── FLASHCARDS.md → (raiz)     filosofia + Regras gerais de curadoria R1-R8 (fica na raiz, canônico)
├── CURADORIA-ANKING.md        método técnico + comandos
├── EXEMPLARES-CARDS.md        few-shot de bons cards (forma + gesto)
├── ANTI-EXEMPLARES-CARDS.md   cards ruins / matches falsos a evitar
├── estrutura-deck-mestre.md   deck NEBLI espelhando FMUSP (UC › componente › aula)
├── anking-v12-export.txt →     mora em scripts/ (o EXPORT dos scripts aponta pra lá)
├── scripts/                   os 13 .py do pipeline de curadoria/monitor + o export bruto
├── anki-addons/               add-on Ctrl+1 (nebli_flag_suspender)
├── curadoria/                 curadoria por aula (dados): _INDEX, _TEMPLATE, <slug>.md + <slug>-curado.json
├── deck-cards/                contratos/padrão de deck por aula
└── cards-nebli/               cards autorais NEBLI por aula (fonte versionada)
```

## O que ficou FORA de flashcards/ (de propósito)

| Fica em | Por quê |
|---|---|
| `arquivos-trabalho/anking-pool-<slug>.json`, `checklist-<slug>.tsv`, `cobertura-<slug>.json` | intermediários transitórios por corrida; a pasta é compartilhada com o pipeline do resumo |
| `referencias-externas/onde-aprofundar.md` | material de **capa** (bloco "Onde aprofundar"), não do deck |
| `referencias-externas/blueprint-step1.md` | calibração de capa/redação, não do deck |
| `referencias-externas/INFRA-REMOTO.md` | infra geral (Docker/remote/scheduler), card-adjacente mas não só de card |

## Como os scripts resolvem paths (para quem for editar)
- Scripts em `flashcards/scripts/x.py`. Raiz do repo = `dirname(dirname(dirname(__file__)))` (três níveis acima).
- `EXPORT` = `dirname(__file__)/anking-v12-export.txt` (o export mora junto dos scripts).
- Dados de curadoria: `RAIZ/flashcards/curadoria/<slug>...`. Intermediários: `RAIZ/arquivos-trabalho/...`.
- Invocação (a partir da raiz do repo): `python flashcards/scripts/<script>.py ...`.

## Ordem de leitura numa sessão de cards
1. `FLASHCARDS.md` (raiz) — filosofia + Regras gerais de curadoria (R1–R8).
2. `flashcards/CURADORIA-ANKING.md` — método técnico + comandos.
3. `flashcards/EXEMPLARES-CARDS.md` + `ANTI-EXEMPLARES-CARDS.md` — antes de gerar card autoral.
4. `flashcards/estrutura-deck-mestre.md` — onde o card vai morar no Anki.

## Verificação da migração (2026-07-10)
- 13 scripts compilam; `RAIZ`/`PROJ_ROOT` resolvem para a raiz do repo; scripts offline acham os dados nos paths novos. Confirmado.
- Referências atualizadas em `CLAUDE.md`, `ROLES.md`, `FLASHCARDS.md`, `.claude/commands/resumo.md`, `INFRA-REMOTO.md`, `onde-aprofundar.md` e nos docstrings dos scripts.
