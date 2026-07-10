# Revisão didática — Cadeia respiratória (Tier 2 + Tier 3 baseline manual)

**Data:** 2026-05-25 · **Avaliador:** Opus 4.7 · **Fonte:** `lixo/typst-build-par/_backup_cadeia-respiratoria_2026-05-13/etapa1.typ` (211 linhas, 13 subtópicos)

---

## Tier 2 — Score médio: 3.5 / 5 · 1 CRÍTICO falhando, 2 IMPORTANTES falhando

| # | Critério | Sev | Score | Diagnóstico | Exemplo |
|---|---|---|---|---|---|
| T2.1 | Pergunta abrindo subtópico | CRÍTICO | **2** | Só 3 de 13 subtópicos abrem com pergunta. Maioria expositiva. | 2.1: "Antes de mergulhar em cadeia respiratória, vale entender a topografia mitocondrial" ❌ vs 1.1: "Por que não usar a oxidação direta?" ✅ |
| T2.2 | Mecanismo antes de nome | CRÍTICO | **3** | Padrão misto. "Complexo I, nome formal NADH-ubiquinona oxidorredutase" usa nome primeiro. Mas analogia da escada é bem feita. | "O Complexo I, nome formal *NADH-ubiquinona oxidorredutase*, é o portal do NADH" ❌ |
| T2.3 | Pré-requisitos retomados | IMPORTANTE | **4** | NADH/FADH₂ explicados na intro; Krebs/beta-ox citados com retomada leve. | "os elétrons que você arrancou dos alimentos (sob a forma de NADH e FADH₂)" ✅ |
| T2.4 | Aprofundamento em camadas | IMPORTANTE | **5** | Exemplar. Subtópico 2.4 (Complexo III/IV) segue porquê → mecanismo → exceção (ROS) → clínica (envelhecimento). | "Por que entregar 4 elétrons de uma vez? Porque entregar 1 ou 2... geraria intermediários extremamente reativos" ✅ |
| T2.5 | Diálogo > livro-texto | CRÍTICO | **4** | Voz consistente de monitor. "Vamos aplicar com números reais", "vale a pena pensar nela com calma". | "Olhe a tabela de potenciais que aparece nos slides com este olhar" ✅ |
| T2.6 | atencao-box voz de mecanismo | CRÍTICO | **2** | **FALHA GRAVE.** O parágrafo de 1.3 usa explicitamente vocab de prova: *"o tipo de pergunta que aparece em prova — e o aluno que entende a fórmula nunca cai na armadilha"*. Viola regra 10 do REDATOR-E1 + canônico de 2026-05-22. | "que aparece em prova" + "armadilha" em 1.3 ❌❌ |
| T2.7 | Variação de registro | IMPORTANTE | **3** | 2.1, 2.2, 2.3, 2.4 abrem todos em modo expositivo-organizador ("X tem N peças, vamos olhar uma a uma"). Sem rotação. | "A cadeia respiratória tem duas portas de entrada" (2.2) + "Entre os complexos fixos, há dois transportadores" (2.3) — registro idêntico. |
| T2.8 | Mini-resumos com fórmula variada | IMPORTANTE | **3** | Tem 5+ mini-resumos mas começam todos em padrão livre — nenhum usa "Em uma frase:", "Se você só lembrar:". | Mini-resumos abrem direto na frase, sem prefixo canônico que ancora visualmente. |
| T2.9 | Conclusão integradora 3+ camadas | IMPORTANTE | (n/a) | Não li o final do arquivo nesta passagem. | — |
| T2.11 | Figuras integradas ao texto | IMPORTANTE | **4** | 2 figuras-SVG referenciadas com integração ("Olhe a tabela..."). Mas figura de "topografia mitocondrial" aparece sem chamada do parágrafo anterior. | — |
| T2.12 | Cota de antropomorfismo | DESEJÁVEL | **3** | "A vida quebrou o problema", "a natureza apertou esse passo", "a célula tem um truque genial" — usado 5+ vezes. Vira tique. | — |
| T2.14 | Cobertura da Seção D do Tema Card | CRÍTICO | (n/a) | Tema-card não acessível nesta sessão. Critério precisa de input para julgar. | — |

**Top 3 recomendações imediatas:**

1. **Reescrever o parágrafo final de 1.3** — remover "que aparece em prova" e "armadilha". Vocab de prova bloqueia movimentação do PDF pela regra 10 + check do precompile.
2. **Adicionar pergunta abrindo subtópicos 2.1–2.5** (5 subtópicos consecutivos sem pergunta). Ex.: 2.1 vira "Onde, exatamente, mora a maquinaria respiratória?"; 2.3 vira "Como os elétrons se movem entre complexos que estão fixos na membrana?".
3. **Padronizar prefixo dos mini-resumos** — rotacionar entre "Em uma frase:", "Se você só lembrar:", "O que ficou de pé:".

---

## Tier 3 — Revisão profunda

**T3.7 — Carga cognitiva pico:** subtópico **2.5 (ATP-sintase + quimiosmótica + Mitchell)** é o pivô do resumo. Densidade alta (5 conceitos novos por parágrafo: F₀, F₁, oligomicina, força próton-motriz, ciclo L/T/O) MAS com mitigação adequada (mini-resumo no fim + box clínica de oligomicina). Carga 8/10, sustentável. **Não exige fragmentação.**

**T3.4 — Voz fora do padrão:** "que aparece em prova" em 1.3 é o único caso grave detectado.

**T3.5 — Veredito:** o aluno em dificuldade conseguiria aprender muito **se o REDATOR removesse o vocab de prova de 1.3 e adicionasse perguntas abrindo a PARTE II**. Conteúdo está exemplar (T2.4 score 5); voz tropeçou em 2 pontos.

---

## Comparação com baseline da Gliconeogênese

| Métrica | Gliconeogênese | Cadeia respiratória |
|---|---|---|
| Score médio Tier 2 | 3.7 / 5 | 3.5 / 5 |
| CRÍTICOS falhando | 0 | 1 (vocab de prova em 1.3) |
| Pergunta abrindo subtópicos | 10/12 (83%) | 3/13 (23%) |
| Diálogo > livro-texto | 4 | 4 |
| Atencao-box voz mecanismo | 5 | 2 |

**Conclusão:** o resumo de gliconeogênese (gerado hoje, ORQUESTRADOR direto) saiu **superior** ao de cadeia respiratória (gerado pelo subagente da G20) — sobretudo em T2.1 (perguntas abrindo) e T2.6 (atencao-box sem prova). A nova diretriz "baseline baixo + dificuldade" + os fixes da rubrica T2.1/T2.6 são a alavanca de qualidade.

---

## Pendência para v2

A revisão precisa do tema-card para julgar T2.14. Quando v2 estiver implementada, o subagente revisor-didatico vai ler `arquivos-trabalho/tema-card-<slug>.md` automaticamente.
