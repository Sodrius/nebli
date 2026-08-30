# Rubrica de qualidade — NEBLI (canônica 2026-05-25, v1)

**Propósito:** checklist obrigatório em toda geração de resumo NEBLI, em 3 tiers proporcionais à complexidade do julgamento. Versão inicial; iterar com base em baselines reais.

**Missão NEBLI que esta rubrica defende:** apostila de extrema qualidade, do básico ao aprofundado, para aluno que sabe pouco e tem dificuldade real aprender muito.

---

## Tier 1 — Completude mecânica/visual

**Modelo alvo (v2):** Ollama local `qwen2.5:7b`. Rápido, gratuito, ideal para perguntas booleanas e contagens. Critérios respondíveis com "sim/não" ou número, sem julgamento estético.

**Quando roda:** sempre, em toda geração, antes do Tier 2.

**Severidade default:** falha em Tier 1 = ERROR, bloqueia movimentação do PDF.

### T1.1 — Toda figura citada existe no disco

**Pergunta:** para cada `#figura-nebli("/figuras/X/slide-N.png", ...)` em etapa1.typ, o arquivo PNG existe?

**Falha:** ≥1 caminho quebrado.
**Bom:** 100% existem.
**Onde olhar:** regex `#figura-nebli\("(/figuras/[^"]+)"` + `os.path.exists`.

### T1.2 — Toda figura tem legenda não-vazia

**Pergunta:** `legenda:` está preenchida em todas as chamadas `#figura-nebli`?

**Falha:** ≥1 `legenda: []` ou `legenda: ""`.
**Bom:** todas com legenda ≥10 palavras explicando o que mostrar.

### T1.3 — Toda sigla usada no corpo tem `#sigla()` declarado

**Pergunta:** para cada sigla que aparece em prosa (lista canônica + detectadas), há uma declaração `#sigla("X", [...])` ANTES da 1ª aparição?

**Lista canônica de armadilhas frequentes:** NADH, NAD⁺, ADP, Pi, cAMP, AMPc, CoA, NADP⁺, FAD, FADH₂, GDP, AMP, CO₂ (este último não precisa).

**Falha:** ≥1 sigla da lista canônica aparece em prosa sem `#sigla(` declarado.
**Bom:** zero siglas sem footnote na 1ª aparição.

### T1.4 — Mapa-confusões cobre todos os subtópicos da E1

**Pergunta:** para cada `#subtopico("N.M ...")` em etapa1.typ, existe entrada `### N.M ...` em `mapa-confusoes/<slug>.md`?

**Falha:** ≥1 subtópico sem cobertura no mapa.
**Bom:** 100% cobertos.

### T1.5 — Termo-notas no alvo (6–10 por resumo)

> Alvo atualizado: `CLAUDE.md` § Footnotes e siglas e `ROLES.md` § Redator diretriz 8 dizem **6–10**, não 6–8. Vale também checar que cada `#termo-nota`/`#sigla` é declarado na **1ª aparição do termo no arquivo** — incluindo legendas de figura, células de tabela e o texto de outras footnotes (achado da corrida `imuno-06-sistema-complemento`).

**Pergunta:** `#termo-nota[...][...]` aparece quantas vezes em etapa1.typ?

**Falha:** <4 ou >12.
**Aceitável:** 4–5 ou 9–10.
**Bom:** 6–8.

### T1.6 — Tabelas bem-formadas

**Pergunta:** para cada `#table(columns: (auto, auto, ...))`, o número de células `[...]` é múltiplo do número de colunas?

**Falha:** desalinhamento ≥1.
**Bom:** todas alinhadas.

### T1.7 — Mindmap de fechamento presente e bem-formado [SUSPENSO]

> **NÃO APLICAR.** `#mindmap-fechamento` foi suspenso em 2026-05-28 e `#mapa-parte` em 2026-05-19; ambos são no-op no template. A E1 fecha na **conclusão integradora obrigatória** (`#conclusao-box`), coberta por T2.9.

**Pergunta:** `#mindmap-fechamento(` existe em etapa1.typ com `estacoes:` contendo 3 elementos e `cartoes:` contendo 3 elementos?

**Falha:** ausente, ou contagens diferentes de 3.
**Bom:** presente, 3 estações + 3 cartões.

### T1.8 — Marcadores de negrito balanceados [novo 2026-05-25]

**Pergunta:** em cada parágrafo de etapa1.typ, o número de `*` é par (todo negrito aberto está fechado)?

**Por que importa:** bug Typst clássico — um `*` órfão escapa para o resto do parágrafo, transformando texto em itálico/negrito não-intencional. NENHUM check existente pega isso; o `precompile-check.py` só pega NULL bytes e truncamento de última linha. Quando passa pelo compilador, vira corrupção visual silenciosa.

**Falha:** ≥1 parágrafo com número ímpar de `*` (descontando `**` para markdown bold que é separadamente proibido).
**Bom:** 100% dos parágrafos com contagem par.
**Onde olhar:** iterar por parágrafos (separados por linha em branco) em etapa1.typ, etapa2.typ, etapa3.typ, resumindo.typ.

---

## Tier 2 — Didática geral

**Modelo alvo (v2):** Sonnet 4.6 via Task tool (subagente `revisor-didatico`).

**Quando roda:** sempre, em toda geração, após Tier 1 passar.

**Severidade:** CRÍTICO falha = ERROR (bloqueia). IMPORTANTE falha = WARN (passa mas reporta). DESEJÁVEL falha = INFO.

### T2.1 — Abertura de subtópico pelos 5 registros canônicos [CRÍTICO]

> **INVERTIDO em 2026-08-29.** A redação anterior deste critério premiava "pergunta ingênua abrindo cada subtópico". Esse recurso foi **banido** em 2026-05-29 (`CLAUDE.md` § Preferences + § Três regras editoriais, regra 1; `ERROS.md` #14). Um resumo que segue o canônico atual tirava 1 nesta rubrica. Julgar pela redação abaixo.

**Pergunta-julgamento:** a primeira sentença após cada `#subtopico(...)` é uma **afirmação direta + mecanismo**, em um dos 5 registros canônicos — enquadramento, integração-anterior, integração-posterior, analogia concreta, ponto-de-quebra?

**Falha (1–2):** subtópicos abrem por pergunta âncora/retórica/ingênua (recurso banido), ou abrem por definição de dicionário sem mecanismo ("A via alternativa é uma das três vias de ativação do complemento.").
**Aceitável (3):** maioria abre por afirmação, mas os registros se repetem entre vizinhos.
**Bom (4–5):** todas as aberturas são afirmação + mecanismo, com rotação clara de registro e nenhum par vizinho compartilhando registro (cruzar com a Seção B.bis do Tema Card).

**Onde olhar:** primeira sentença de cada `#subtopico` em etapa1.typ.

### T2.2 — Mecanismo antes de nome técnico [CRÍTICO]

**Pergunta-julgamento:** enzimas/moléculas-chave têm o "o que faz" explicado ANTES do nome técnico? Ex.: "enzima que adiciona um CO₂ ao piruvato (chamada piruvato carboxilase)" — não "a piruvato carboxilase adiciona CO₂ ao piruvato".

**Falha (1–2):** maioria das introduções começa pelo nome técnico solto.
**Aceitável (3):** padrão misto.
**Bom (4–5):** todas (ou quase) as enzimas-chave entram pelo mecanismo.

### T2.3 — Pré-requisitos retomados em 1–2 frases [IMPORTANTE]

**Pergunta-julgamento:** conceitos pré-requisito (jejum, ATP, NADH como moeda redutora, irreversibilidade da glicólise, ciclo de Krebs) são retomados em 1–2 frases quando aparecem, ou usados como se o aluno já tivesse domínio?

**Falha (1–2):** "vimos na glicólise" sem retomar; ou pula direto para uso técnico.
**Bom (4–5):** retomada explícita em pelo menos 2 dos 3 pré-requisitos centrais do tema.

### T2.4 — Aprofundamento em camadas [IMPORTANTE]

**Pergunta-julgamento:** subtópicos seguem porquê cru → nuance → exceção → clínica, ou pulam direto para detalhe avançado ou para clínica sem o porquê?

**Falha (1–2):** maioria dos subtópicos vai direto para nome + função sem o porquê básico.
**Bom (4–5):** maioria respeita a progressão de camadas.

### T2.5 — Diálogo > livro-texto [CRÍTICO]

**Pergunta-julgamento:** 3 parágrafos aleatórios do corpo soam como monitor explicando ao vivo ou como prosa de livro?

**Falha (1–2):** prosa expositiva neutra, sem voz de explicação dirigida.
**Bom (4–5):** quase todo parágrafo tem marcas de diálogo (perguntas retóricas plausíveis, "repare que", "veja", "lembra que", analogias).

### T2.6 — `#atencao-box` em voz de mecanismo [CRÍTICO]

**Pergunta-julgamento:** cada `#atencao-box` apresenta (a) a quebra mecanística + (b) a correção, sem usar vocab de prova ("pegadinha", "cai em prova", "examinador")?

**Falha (1–2):** ≥1 box usa vocab de prova, ou só descreve sem explicar a quebra mecanística.
**Bom (4–5):** todos os boxes têm a estrutura quebra+correção, voz mecanística.

### T2.7 — Variação de registro entre subtópicos vizinhos [IMPORTANTE]

**Pergunta-julgamento:** subtópicos consecutivos abrem em registros DIFERENTES dos 5 canônicos (enquadramento, integração-anterior, integração-posterior, analogia concreta, ponto-de-quebra)?

**Falha (1–2):** ≥2 pares de subtópicos vizinhos abrem no mesmo registro.
**Bom (4–5):** rotação clara de registro ao longo da E1.

### T2.8 — Mini-resumos em parágrafos longos com fórmula variada [IMPORTANTE]

**Pergunta-julgamento:** parágrafos >5 linhas têm `#mini-resumo`? A fórmula varia ("Em uma frase:", "Se você só lembrar:", "O que ficou de pé:", "X → Y → Z")?

**Falha (1–2):** parágrafos longos sem mini-resumo, ou fórmula sempre igual.
**Bom (4–5):** todo parágrafo longo tem mini-resumo, e a fórmula rotaciona.

### T2.9 — Conclusão integradora em 3+ camadas [IMPORTANTE]

**Pergunta-julgamento:** a `#conclusao-box(...)` ao fim da E1 costura PARTE I-II-III em camadas conceituais (mínimo 3), ou só lista o que apareceu?

**Falha (1–2):** lista expositiva sem costura.
**Bom (4–5):** ≥3 camadas explícitas que amarram o tema todo.

### T2.11 — Figuras integradas ao texto [IMPORTANTE, novo 2026-05-25]

**Pergunta-julgamento:** cada `#figura-nebli(...)` é referenciada explicitamente no parágrafo anterior ("repare no esquema abaixo", "veja a figura", "compare com o diagrama"), ou aparece como bloco solto que o aluno ignora?

**Por que importa:** aluno em dificuldade não processa figura autônoma. Se o parágrafo não convida o olhar, a figura vira decoração.

> **REBAIXADO a DESEJÁVEL em 2026-08-29.** A regra editorial "figura ancorada na prosa" foi **removida do canônico em 2026-05-28** (`CLAUDE.md` § Três regras editoriais, nota final). O padrão de casa passou a ser **legenda autossuficiente que carrega o mecanismo** — é assim que os resumos aceitos desde então foram escritos. Julgar a *legenda*: ela nomeia o mecanismo que a figura carrega, ou só rotula o que se vê? Convite no parágrafo anterior continua bem-vindo, mas a ausência dele não é mais falha.

**Falha (1–2):** maioria das figuras aparece sem chamada do texto anterior.
**Aceitável (3):** metade das figuras tem referência.
**Bom (4–5):** quase todas as figuras (≥80%) têm chamada explícita no parágrafo anterior, e a legenda complementa o texto em vez de repeti-lo.

### T2.12 — Cota de antropomorfismo [DESEJÁVEL, novo 2026-05-25]

**Pergunta-julgamento:** expressões "o corpo paga", "a célula decide", "o fígado escolhe" são usadas com moderação (máx 3x por PARTE), ou viraram tique?

**Por que importa:** antropomorfismo é didático na 1ª aparição, vira ruído na 5ª. Em vez disso, alternar com "essa síntese custa", "a regulação dispara", "o substrato exige".

**Falha (1–2):** ≥4x por PARTE, ou mesma expressão antropomórfica recorrente.
**Bom (4–5):** ≤3x por PARTE, variando entre antropomorfismo, voz passiva e voz mecanística.

### T2.14 — Cobertura da Seção D do Tema Card [CRÍTICO, novo 2026-05-25]

**Pergunta-julgamento:** cada quebra de raciocínio listada na Seção D do Tema Card (`arquivos-trabalho/tema-card-<slug>.md`) virou pelo menos 1 `#atencao-box` OU 1 frase explícita de "atenção mecanística" na E1?

**Por que importa:** a Seção D é o ponto onde o ORQUESTRADOR curou as armadilhas históricas do banco + Lehninger. Se o REDATOR ignora, todo esse trabalho de curadoria é perdido. Critério fecha o ciclo curadoria → redação que vem falhando em vários resumos.

**Falha (1–2):** <50% das quebras da Seção D foram cobertas na E1.
**Aceitável (3):** 50–75% cobertas.
**Bom (4–5):** ≥80% das quebras viraram atencao-box ou ênfase mecanística explícita; as não-cobertas têm justificativa (ex.: quebra pertence a um pré-requisito não-detalhado neste resumo).

**Onde olhar:** lista numerada da Seção D do Tema Card vs grep `#atencao-box(` + análise dos parágrafos próximos a "Atenção:" / "Repare que" no etapa1.typ.

---

## Tier 3 — Revisão profunda

**Modelo alvo (v2):** Opus 4.7 via Task tool (subagente `revisor-profundo`).

**Quando roda (canônico 2026-05-25):** SEMPRE — em toda geração de resumo, após Tier 1 e Tier 2 passarem. Davi decidiu que Opus entra no pipeline padrão, não fica como opcional. Custo aceitável dado o ganho pedagógico.

**Saída:** análise editorial em prosa rica, com sugestões concretas de reescrita.

### T3.1 — Comparação com exemplar canônico

Identificar a categoria mais relevante de `EXEMPLARES.md` para este tema e comparar 2–3 parágrafos do resumo com o exemplar. Onde está abaixo do padrão? Por quê?

### T3.2 — 3 parágrafos mais fracos

Citação literal + diagnóstico do que está fraco + sugestão de reescrita (texto pronto para colar).

### T3.3 — 3 subtópicos mais densos onde o aluno trava

Identificar subtópicos onde o conteúdo é objetivamente denso (≥4 conceitos novos por parágrafo) e propor mini-resumo extra, figura adicional, ou fragmentação em sub-subtópicos.

### T3.4 — Voz fora do padrão

Listar qualquer parágrafo com auto-referência ("eu também demorei"), familiaridade falsa ("se ainda tá confuso é normal"), jargão sem etiqueta, ou voz acadêmica neutra.

### T3.5 — Veredito final

1 parágrafo: o aluno em dificuldade real conseguiria aprender muito com este resumo? Sim / não / em parte. 1–2 razões.

### T3.7 — Detecção de carga cognitiva pico [novo 2026-05-25, estrutural]

**O que produz:** identifica O SUBTÓPICO ONDE O ALUNO EM DIFICULDADE PROVAVELMENTE DESISTE. Calcula densidade = (conceitos novos introduzidos no subtópico) × (profundidade técnica de cada conceito) ÷ (mini-resumos + figuras no subtópico).

**Diagnóstico esperado:** 1 subtópico-pivô com nota de carga cognitiva + 3 mitigações concretas:
1. Fragmentar em 2 sub-subtópicos visualmente distintos (com sub-cabeçalho)?
2. Adicionar mini-resumo no meio do parágrafo mais denso?
3. Adicionar figura esquemática nova (SVG ou referência adicional ao slide-fonte)?

**Por que importa:** é a alavanca direta da missão NEBLI. O resumo pode ter score 4 em tudo mas se um subtópico só tem carga 10/10 sem mitigação, o aluno em dificuldade fecha o PDF ali. T3.7 é o critério que defende a continuidade da leitura.

---

## Implementação futura (v2 — não nesta sessão)

### Tier 1 — Script `typst-build/revisar_completude.py`

- Pure Python para os checks objetivos. Não precisa de LLM para T1.1, T1.2, T1.3, T1.4, T1.5, T1.6, T1.7 — tudo regex/contagem/`os.path.exists`.
- Ollama entra opcionalmente para validar legendas (T1.2 estendido: a legenda DESCREVE de fato o que está na imagem? Comparação texto vs OCR/visão da imagem). Roda só se `--com-ollama` for passado.
- Exit code 0 (tudo ok), 1 (≥1 ERROR), 2 (só warnings).
- Bloqueia movimentação do PDF se exit ≠ 0.

### Tier 2 — Subagente `.claude/agents/revisor-didatico.md`

- Sonnet 4.6.
- Recebe via prompt: o conteúdo de `etapa1.typ` + esta rubrica (Tier 2 só) + lista de subtópicos.
- ANCORAGEM DE TEMA obrigatória no topo (mesma defesa contra contaminação dos outros agents).
- Saída em JSON estruturado:
  ```json
  {
    "criterio": "T2.1",
    "score": 1-5,
    "severidade": "CRITICO|IMPORTANTE|DESEJAVEL",
    "justificativa": "1-2 frases",
    "exemplo_literal": "citação do .typ",
    "sugestao": "reescrita opcional"
  }
  ```
- Agregador Python converte JSON em markdown legível em `arquivos-trabalho/revisao-didatica-<slug>.md`.

### Tier 3 — Subagente `.claude/agents/revisor-profundo.md`

- Opus 4.7.
- Slash command `/revisar-profundo <slug>` dispara.
- Sem rubrica fechada — instrução aberta com os 5 itens do Tier 3.
- Saída em markdown editorial em `arquivos-trabalho/revisao-profunda-<slug>.md`.

### Integração no pipeline (`compilador.md`)

Novo passo 5.5 entre `auditar_pdf_visual.py` e movimentação:

```bash
# Tier 1 — sempre roda
python3 typst-build/revisar_completude.py [slug]
# Se exit ≠ 0, parar.

# Tier 2 — sempre roda (Sonnet via Task)
# Spawn subagent revisor-didatico via Task tool, esperar saída
# Se CRÍTICO falhou, parar. Se IMPORTANTE, reportar e seguir.
```

Tier 3 NÃO entra aqui. Só roda quando Davi pede explicitamente.

---

## Princípios editoriais (canônicos)

1. **Cada critério é respondível olhando 1–2 trechos do .typ.** Sem perguntas vagas.
2. **Severidade reflete impacto na missão.** CRÍTICO = trai a missão "aluno em dificuldade aprende". IMPORTANTE = qualidade comprometida. DESEJÁVEL = polimento.
3. **Tier proporcional ao modelo.** Não pedir Opus para coisas que Sonnet resolve; não pedir Sonnet para coisas que `os.path.exists` resolve.
4. **Sempre exemplo literal.** Score sem citação do trecho é proibido (vira opinião sem evidência).
