# Relatório de fechamento — Motilidade do Tubo Digestório (`fisio-tgi-01-motilidade`)

## Paridade de distratoras — Q01–Q30 (banda dupla 0.80 ≤ ratio ≤ 1.25)

| Q | gab | correta | distratoras | maior | ratio | status |
|---|---|---|---|---|---|---|
| 01 | B | 34 | [35, 34, 33, 31] | 35 | 0.97 | PASS |
| 02 | CECC | — | — | — | — | C/E (paridade não se aplica) |
| 03 | C | 26 | [29, 29, 25, 27] | 29 | 0.90 | PASS |
| 04 | CECC | — | — | — | — | C/E (paridade não se aplica) |
| 05 | A | 28 | [27, 23, 23, 27] | 27 | 1.04 | PASS |
| 06 | E | 30 | [24, 27, 25, 23] | 27 | 1.11 | PASS |
| 07 | E | 27 | [25, 24, 25, 25] | 25 | 1.08 | PASS |
| 08 | E | 27 | [24, 24, 27, 25] | 27 | 1.00 | PASS |
| 09 | D | 34 | [28, 29, 33, 28] | 33 | 1.03 | PASS |
| 10 | EECC | — | — | — | — | C/E (paridade não se aplica) |
| 11 | CCEC | — | — | — | — | C/E (paridade não se aplica) |
| 12 | A | 32 | [32, 30, 30, 31] | 32 | 1.00 | PASS |
| 13 | EECC | — | — | — | — | C/E (paridade não se aplica) |
| 14 | C | 27 | [28, 26, 27, 26] | 28 | 0.96 | PASS |
| 15 | A | 30 | [31, 26, 28, 26] | 31 | 0.97 | PASS |
| 16 | C | 30 | [27, 26, 26, 30] | 30 | 1.00 | PASS |
| 17 | D | 27 | [27, 22, 23, 23] | 27 | 1.00 | PASS |
| 18 | EEEC | — | — | — | — | C/E (paridade não se aplica) |
| 19 | E | 29 | [25, 24, 27, 28] | 28 | 1.04 | PASS |
| 20 | ECCE | — | — | — | — | C/E (paridade não se aplica) |
| 21 | A | 30 | [27, 24, 25, 26] | 27 | 1.11 | PASS |
| 22 | A | 30 | [31, 26, 29, 27] | 31 | 0.97 | PASS |
| 23 | D | 34 | [30, 27, 28, 27] | 30 | 1.13 | PASS |
| 24 | EEEC | — | — | — | — | C/E (paridade não se aplica) |
| 25 | B | 27 | [28, 28, 25, 25] | 28 | 0.96 | PASS |
| 26 | ECEE | — | — | — | — | C/E (paridade não se aplica) |
| 27 | D | 28 | [23, 29, 23, 23] | 29 | 0.97 | PASS |
| 28 | D | 28 | [27, 21, 24, 24] | 27 | 1.04 | PASS |
| 29 | E | 27 | [23, 25, 24, 25] | 25 | 1.08 | PASS |
| 30 | CCEC | — | — | — | — | C/E (paridade não se aplica) |

**20 MC auditadas · média 1.02 · mín 0.90 · máx 1.13 · 0 fora da banda.**
**10 C/E** (Q02, Q04, Q10, Q11, Q13, Q18, Q20, Q24, Q26, Q30), 4 assertivas I–IV cada — gate `check_ce_quatro_itens` OK.

## Tabela de figuras (11 figuras · 3–4 por PARTE)

| Figura | PARTE | Origem | Mecanismo que carrega | Largura |
|---|---|---|---|---|
| `fig-anatomia-tgi` | I (1.1) | slide-02 (recorte) | Onde estão as duas pontas esqueléticas e o miolo liso ao longo do tubo | 42% |
| esquema circular × longitudinal | I (1.2) | Typst nativo (novo) | Efeito geométrico oposto das duas camadas — estreitar vs encurtar | 88% |
| `fig-fasica-tonica` | I (1.3) | slide-04 (recorte) | Dissociação entre força em platô e queda de cálcio/fosforilação na contração tônica | 62% |
| `fig-esfincteres` | I (1.4) | slide-04 (recorte) | Os cinco pontos de controle e a dupla regulação do piloro | 58% |
| `fig-sne-sna` | II (2.1) | slide-02 (recorte) | Intrínseco × extrínseco, e a divisão de trabalho entre os dois plexos | 72% |
| esquema polaridade peristáltica | II (2.2) | Typst nativo (novo) | Por que o mesmo estímulo contrai atrás e relaxa à frente | 92% |
| `fig-reflexos-curto-longo` | II (2.3) | slide-03 (recorte) | Os dois arcos convergindo no mesmo neurônio motor entérico | 80% |
| `fig-juncao-neuroefetora` | III (3.1) | slide-05 (recorte) | Varicosidades sem placa motora — liberação lateral e difusa | 46% |
| `fig-calmodulina-mlck` | III (3.2) | slide-05 (recorte) | Cálcio → calmodulina → MLCK → fosforilação da cadeia leve | 80% |
| `fig-ca-contracao-relaxamento` | III (3.3) | slide-05 (recorte) | As duas metades do ciclo: entrada/extrusão de cálcio e a miosina fosfatase | 62% |
| `fig-gpcr-rhoa` | III (3.4) | slide-06 (recorte) | Os dois braços do GPCR e a convergência sobre a miosina fosfatase | 72% |

Figuras descartadas: recorte isolado do "circuito intramural" (slide-03) — redundante com `fig-reflexos-curto-longo` e com excesso de área branca. Substituído pelo esquema nativo de polaridade peristáltica, que ensina o mesmo mecanismo com melhor densidade.

## Cobertura E1 → E2 (subtópico → questões que o cobrem)

| Subtópico da E1 | Questões | N |
|---|---|---|
| 1.1 Esquelético nas pontas, liso no meio | Q01, Q21 | 2 |
| 1.2 Circular estreita, longitudinal encurta | Q03, Q05, Q19 | 3 |
| 1.3 Contração fásica e tônica (+ ondas lentas) | Q04, Q22, Q24, Q28-E | 4 |
| 1.4 Esfíncteres e a regra da distensão | Q02, Q12, Q20, Q26, Q28 | 5 |
| 2.1 Plexos mioentérico e submucoso | Q06, Q13, Q19, Q25 | 4 |
| 2.2 Reflexo curto intramural | Q07, Q11, Q05-E | 3 |
| 2.3 Reflexo longo vago-vagal | Q08, Q14, Q29 | 3 |
| 2.4 ACh, VIP, NO e o simpático | Q09, Q10, Q18, Q27 | 4 |
| 3.1 Junção neuroefetora | Q15, Q17-E | 2 |
| 3.2 Cálcio–calmodulina–MLCK | Q16, Q23, Q30 | 3 |
| 3.3 Relaxamento (extrusão + fosfatase) | Q12, Q22, Q30 | 3 |
| 3.4 Sensibilização ao cálcio | Q17, Q23, Q27-C | 3 |

Todos os 12 subtópicos com ≥2 questões. (Sufixo `-E`/`-C` = o subtópico aparece como distratora/assertiva daquela questão, não como gabarito.)

## Índice de completude (0–10)

| Eixo | Nota | Justificativa |
|---|---|---|
| **E1 × slide** | **9** | Cobre integralmente os 5 slides de conteúdo e aprofunda em cinco pontos colados ao próprio slide: os dois núcleos vagais (ambíguo × motor dorsal), as células de Cajal e as ondas lentas, a distinção muscular própria × muscular da mucosa, a via NO–GMPc–PKG detalhada, e o freio duodenal com a síndrome de dumping. |
| **E2 × E1** | **9** | Os 12 subtópicos têm 2–5 questões cada; os aprofundamentos injetados (Cajal, núcleos vagais, sensibilização) são cobrados diretamente em Q24, Q21, Q17 e Q23. |
| **Cards × E1** | **n/a** | Nesta corrida não houve etapa de cards: o AnkiConnect roda em `localhost` na máquina do Davi e não é alcançável de uma sessão remota. Fica pendente para uma corrida local. |

## Prioridades desta corrida (do § Diário de revisões)

- **2026-05-29 · biocel-07 — "sem slide ≠ sem figura" (peso alto).** Aplicada: onde o slide não cobria um mecanismo espacial (camadas circular × longitudinal; polaridade do reflexo peristáltico), foram construídos dois esquemas nativos em Typst em vez de deixar a PARTE sem figura. Nenhuma cadeia com ≥4 setas ficou sem figura adjacente.
