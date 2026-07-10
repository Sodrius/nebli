# Revisão didática — Gliconeogênese · Tier 2 (Sonnet/Opus baseline)

**Data:** 2026-05-25
**Resumo avaliado:** `resumos-gerados/GLICONEOGENESE.pdf` (42 páginas, gerado nesta sessão)
**Avaliador (v1):** Opus 4.7 manual (auto-revisão honesta — eu redigi esta E1)
**Rubrica:** `arquivos-trabalho/rubrica-qualidade-didatica.md` Tier 2

---

## Sumário executivo

- **Score médio Tier 2:** 3.7 / 5
- **Critérios CRÍTICOS falhando (score ≤ 2):** 0
- **Critérios CRÍTICOS apertados (score 3):** 1 (T2.7 variação de registro)
- **Critérios IMPORTANTES falhando:** 1 (T2.8 mini-resumos com fórmula variada)
- **Veredito:** o resumo passa o crivo CRÍTICO mas tem espaço claro de melhoria em variação de registro e disciplina dos mini-resumos. Não está "zuado", mas também não é exemplar.

---

## Detalhamento por critério

| # | Critério | Sev | Score | Justificativa | Exemplo literal |
|---|---|---|---|---|---|
| T2.1 | Pergunta ingênua abrindo subtópico | CRÍTICO | **4** | 10 dos 12 subtópicos abrem com pergunta plausível. 2.1, 2.2 e 3.3 são exemplares; 1.3 abre expositivamente. | 2.1: "*se a glicólise quebra glicose em piruvato, por que não rodar a mesma maquinaria ao contrário?*" ✅ vs 1.3: "Você já tem duas peças do quebra-cabeça…" ❌ |
| T2.2 | Mecanismo antes de nome técnico | CRÍTICO | **5** | Padrão consistente: "enzima que adiciona um CO₂ ao piruvato — repare no nome: ela 'carboxila'" antes de fixar "piruvato carboxilase". | 2.2: "encontra uma enzima chamada *piruvato carboxilase* — repare no nome: ela 'carboxila', ou seja, adiciona um carbono" |
| T2.3 | Pré-requisitos retomados | IMPORTANTE | **4** | Glicólise, ATP, NADH retomados em 1–2 frases sempre que reaparecem. Krebs entra sem retomada explícita em 2.2. | 2.5: "Compare com o saldo da glicólise: +2 ATP, +2 NADH para quebrar uma glicose" — retoma sem assumir. |
| T2.4 | Aprofundamento em camadas | IMPORTANTE | **4** | 2.2 e 3.3 são exemplares (porquê → mecanismo → nuance → clínica). 2.3 e 2.4 pulam camada de exceção. | 3.3 segue: porquê (hipoglicemia alcoólica) → mecanismo (NADH desloca) → nuance (sequestro indireto) → clínica (Wernicke). |
| T2.5 | Diálogo > livro-texto | CRÍTICO | **4** | Voz consistente de monitor. Marcadores frequentes ("repare", "lembra que", "veja"). Alguns parágrafos em 1.3 e 2.5 deslizam para expositivo. | 2.2: "Esse é o subtópico mais denso do resumo. Leia devagar. Vamos por partes." ✅ vs 2.5: "Agora dá para fechar a conta." (transição seca) |
| T2.6 | `#atencao-box` em voz de mecanismo | CRÍTICO | **5** | 6 atencao-boxes, todos com estrutura quebra+correção, zero vocab de prova. | "PDH desfaz carbono, PC monta carbono; PDH gera NADH, PC gasta ATP; ambas vivem na mitocôndria…" — voz pura de mecanismo. |
| T2.7 | Variação de registro | IMPORTANTE | **3** | 1.2 e 1.3 abrem ambos em registro "complementar ao subtópico anterior". 2.2 e 2.3 abrem ambos em "pergunta de enquadramento". Sem rotação clara. | 1.2: "A primeira reação do aluno…"; 1.3: "Você já tem duas peças…" — registros muito parecidos. |
| T2.8 | Mini-resumos com fórmula variada | IMPORTANTE | **3** | 9 mini-resumos no total. Fórmulas usadas: "Em uma frase:" (3x), "Se você só lembrar de uma coisa:" (2x), "O que ficou de pé:" (1x), seta X→Y→Z (1x), formato livre (2x). "Em uma frase:" repete 3x — desbalanceado. | "Em uma frase:" aparece em 1.1, 2.5 e 3.4 — alvo deveria ser 1 cada. |
| T2.9 | Conclusão integradora em 3+ camadas | IMPORTANTE | **5** | Conclusão tem 4 camadas explícitas ("Primeira camada", "Segunda camada", "Terceira camada", "Quarta camada"), cada uma costurando uma PARTE. | "*Primeira camada:* o cérebro e a hemácia não têm escolha… *Segunda camada:* a gliconeogênese não pode simplesmente rodar a glicólise ao contrário…" |

---

## Top 3 recomendações de melhoria

1. **Rotacionar registro entre subtópicos vizinhos (T2.7).** Hoje a E1 abre 4–5 subtópicos no mesmo registro "pergunta de enquadramento + você já tem duas peças". Fixar uma sequência canônica para tema novo: 1.1 enquadramento → 1.2 integração-anterior → 1.3 analogia → 2.1 enquadramento → 2.2 ponto-de-quebra → 2.3 integração-posterior, etc. Posicionar o registro no Tema Card Seção B ao lado de cada subtópico.

2. **Disciplina das fórmulas de mini-resumo (T2.8).** Criar regra: "cada fórmula só pode aparecer 2x por resumo (3x se forem >12 mini-resumos)". Adicionar validação no `precompile-check.py` (contagem de cada fórmula canônica). Exemplo de redistribuição para a gliconeogênese:
   - Trocar 1 dos 3 "Em uma frase:" por "X causa Y → consequência Z".
   - Trocar o outro por "O que ficou de pé:".

3. **Fechar a camada de exceção em 2.3 e 2.4 (T2.4).** O subtópico 2.3 (FBPase-1) e 2.4 (G6Pase) seguem mecanismo → clínica direto, sem a camada de nuance/exceção que enriquece. Adicionar ao 2.3 uma frase sobre por que a FBPase-1 não foi a solução para os outros bypasses (i.e., por que a hidrólise direta nem sempre é viável termodinamicamente). Em 2.4, mencionar que a G6Pase TEM uma análoga muscular (glicose-6-fosfato desidrogenase) que faz uma coisa COMPLETAMENTE diferente — nuance que evita confusão posterior.

---

## Observações para calibração da rubrica

- **T2.1 score 4 mas com 2 falhas evidentes** — a régua "10 de 12 subtópicos" virou score 4. Deveria ser "≥11 de 12 = 5, 9–10 = 4, 7–8 = 3"? Calibrar antes da v2.
- **T2.9 fácil de fazer 5** porque o helper `#conclusao-box` força estrutura. Talvez esse critério não diferencia bom de excelente — pode virar DESEJÁVEL.
- **Faltou critério sobre "anti-tique" (canônico 2026-05-22):** mini-resumos não devem usar piadas, mnemônicos forçados, perguntas artificiais. Adicionar T2.10?
- **Faltou critério sobre figuras integradas ao texto** — referência no parágrafo antes da figura, ou só figura solta? Hoje 5 das 9 figuras são citadas no texto antes; 4 são autônomas. Adicionar T2.11?
