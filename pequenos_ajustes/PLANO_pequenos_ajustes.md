# PLANO — Pequenos ajustes (Sugestões (3).pdf, 45 itens)

**Data:** 2026-06-24. **Princípio do Davi:** são *pequenas* mudanças. **Não** mexer na prosa expositiva de qualidade — ela está aprovada (item 39: "estou gostando da fluidez da prosa"). O que muda é o **aparato de decisão** ao redor: regras de E2/gabarito, anti-padrões de voz, e quando quebrar a prosa em tópico/tabela.

**Decisões já tomadas pelo Davi nesta sessão (2026-06-24):**
1. Sequência: **fechar o plano primeiro** (este doc), executar depois frente a frente.
2. Conclusão integradora (item 29): **manter, mas opcional** — default passa a ser não ter; só quando o tema integra muitas pontas.
3. Certo/Errado (item 6): **reintroduzir em ~1/3** das 30 objetivas, com gabarito C/E bem sorteado.
4. Pesquisa Mankiw/Poliedro: **feita** → `arquivos-trabalho/pesquisa-didatica/ACHADOS-topico-tabela.md`.

---

## Os 4 mecanismos de aplicação

- **(D) Edição direta** em `.md`/script/template — prescritivo, objetivo, não toca prosa.
- **(A) ANTI-EXEMPLARES.md** (arquivo novo) — par negativo do EXEMPLARES; trecho ruim + diagnóstico + reescrita boa.
- **(E) EXEMPLARES.md** — categoria/exemplar novo, alimentado pela pesquisa.
- **(L) Backlog layout** — 2 colunas, espaçamento, imagens "daqui a pouco" (Davi adiou).

---

## Bucket 1 — E2 / gabarito (mecanismo D, baixo risco)

| Item | O quê | Onde |
|---|---|---|
| 5, 8, 9, 17 | Gabarito não-sorteado / vindo errado / padrão repetido | **Revisor Haiku de gabarito** numa passada final (sugestão do próprio Davi no item 8) + regra anti-streak em `questionador.md`; checagem em `precompile-check.py` |
| 14 | Gabarito **horizontal** (1 2 3 4 5 / 6 7 8 9 10), não vertical | Helper do template Typst (`nebli_v2_apostila.typ`) + `compilador` |
| 6 | Reintroduzir **Certo/Errado em ~1/3** dos itens | `questionador.md` (taxonomia E2) + `precompile-check.py` (paridade vale só p/ múltipla escolha) |
| 10 | Liberar stem **"assinale a incorreta"** | `questionador.md` |
| 4 | Alternativas longas demais (distratora inflada) | Reforçar **direção da remediação** na banda dupla 0.80–1.25 (já existe): correta curta → enriquecer a correta; nunca inchar distratora vazia |
| 16 | Consolidação consolida / integração integra / aplicação aplica | Reforço da taxonomia + filtro de admissão (já canônico) em `questionador.md` |
| 18 | **Questões de cálculo** quando o conteúdo pede | `questionador.md` + modelo de cálculo (ver Bucket 3) |
| 25 | Tabela onde a prosa não cabe (ex.: 4 combinações lac) | Regra de tabela (ver Bucket 3) aplicada também à E2/E1 |

**Nota anti-streak (5/9/17):** nenhuma letra/{C,E} pode repetir 3× seguidas no gabarito; distribuição alvo aproximadamente uniforme entre A-E (múltipla) e ~50/50 (C/E), com sorteio real. O revisor Haiku confere: (a) gabarito impresso == gabarito real de cada questão; (b) sem streak; (c) distribuição não-degenerada.

## Bucket 2 — ANTI-EXEMPLARES.md (mecanismo A, arquivo novo)

Cria `ANTI-EXEMPLARES.md` na raiz (lazy-load, par do EXEMPLARES). Semear com os trechos reais marcados ruins:
- **Item 1** — explicação matemática feia (capturar o trecho real depois).
- **Item 27** — operon trp / lógica AND mal explicada.
- **Item 28** — atenuação do trp (parede de mecanismo sem cadeia clara).

Formato de cada anti-exemplar: `### Sintoma` (o que dói) · `### Trecho ruim` (real) · `### Diagnóstico` (por que falha) · `### Reescrita` (versão boa). Indexado por sintoma para o REDATOR consultar.

## Bucket 3 — Tópico / tabela / cálculo (mecanismo E, pós-pesquisa)

Base: `ACHADOS-topico-tabela.md`. Saídas:
- **Categoria nova no EXEMPLARES.md**: "Quando quebrar a prosa" com os 3 gatilhos de tópico (catálogo de tipos discretos; cadeia de premissas estilo cursinho; resumo em frase completa) + 1 de tabela (cruzamento 2+ dimensões). Itens 21, 33, 34, 42, 43.
- **Nota curta no CLAUDE.md § Bullets e tabelas** referenciando a categoria (sem inchar o canônico).
- **Cálculo bem explicado (itens 1, 18)**: exemplar na cat. 12 do EXEMPLARES com o modelo Mankiw (etapas rotuladas + razão de cada passo + número relido em palavras + figura que narra). Par negativo no ANTI-EXEMPLARES.
- **Resumindo (item 36)**: reforço da regra — menos ideias, mais palavras por ideia, frase encadeada, nunca empilhamento de sigla. Modelo: RESUMO do Mankiw + "Resumindo" numerado do Poliedro. Ajuste em `redator-e1.md`/`ROLES.md` + 1 exemplar.

## Bucket 4 — Prosa / estrutura (mecanismo D, pequeno)

| Item | O quê | Onde |
|---|---|---|
| 35 | Nome de subtópico **direto, não poético** (diz o que ensina) | `redator-e1.md` / `ROLES.md` |
| 29 | Conclusão integradora **opcional** (default = não ter) | `CLAUDE.md` § Ordem do PDF + `ROLES.md` |
| 36 | Resumindo mais enxuto (ver Bucket 3) | `ROLES.md` + EXEMPLARES |
| 39 | Elogio à fluidez — **preservar**, registrar como âncora | nenhuma ação; nota no MEMORY |

## Bucket 5 — Imagens (mecanismo L + E, "daqui a pouco" por decisão do Davi)

Itens 3, 7, 11, 12, 20, 26, 32, 38, 42. Frente própria, depois das 2 colunas:
- **3, 7, 20** — subir o nível: material médico real / SciDraw / bibliotecas externas (Servier, BIOART, Reactome — já no CLAUDE.md § Figuras 2026-05-30); "off slide" = produzir/buscar quando o slide não cobre bem.
- **11** — imagem em questão da E2 (pega do slide, pequena modificação).
- **12** — critério de escolha: a imagem que mais agrega + ajuste de formatação (liga com 2 colunas).
- **26, 32, 38** — figuras faltando em pontos específicos (gráfico diáuxico, etc.).
- Saída futura: seção "critério de imagem" + exemplares de uso no PDF (item 19).

## Bucket 6 — Layout / legibilidade (mecanismo L, adiado pelo Davi)

Itens 2, 19, 31, 37. **2 colunas** para matar o branco (item 2), espaço **após** parágrafo + menos entrelinha (31, 37), glossário de margem (achado Mankiw). Item 30/31 pede pesquisa de tipografia/retenção — frente separada quando o Davi quiser ampliar.

## Bucket 7 — Futuro / à parte

| Item | Status |
|---|---|
| 13 | Flashcards: mais clozes por card, só o que caiu em prova antiga — **via API daqui a alguns meses** (Davi). Backlog. |
| 41 | Split Sonnet/Opus p/ economizar token — definir quais tarefas. Decisão de arquitetura, sessão própria. |
| 15 | Base para melhorar o Mapa de Confusões — definir critério. Backlog. |

---

## Ordem de execução sugerida (quando o Davi liberar)

1. **Bucket 1** (E2/gabarito) — maior retorno, risco zero sobre a prosa. Inclui o revisor Haiku.
2. **Bucket 2** (ANTI-EXEMPLARES) — precisa o Davi apontar os trechos reais de 1/27/28.
3. **Bucket 3** (tópico/tabela/cálculo no EXEMPLARES) — pesquisa já pronta.
4. **Bucket 4** (prosa/estrutura) — edições pequenas.
5. **Buckets 5/6** (imagens + 2 colunas) — frente visual, "daqui a pouco".
6. **Bucket 7** — backlog.
