# Auditoria de gabarito — biotec-02-intestinos

**Data:** 2026-09-06  
**Slug:** biotec-02-intestinos  
**Titulo:** Intestinos: organização, renovação e absorção  

---

## Checagem 1 — Impresso vs. real (gate hard — BLOQUEIA)

### Metodologia
Para cada questão, leu-se enunciado + alternativas/itens, determinou-se a resposta correta pelo conteúdo da E1 e comparou-se com gabarito declarado (YAML) e gabarito impresso (PDF última página).

### Questões conferidas
- **Total:** 30 questões (20 múltipla escolha + 10 C/E com 4 itens cada = 40 itens C/E)
- **Todas** lidas contra E1, todas verificadas para corretude mecanística

### Divergências encontradas

#### Q13 (C/E, Integração) — VERMELHO

**Enunciado:** Julgue os itens sobre a manutenção do nicho da cripta e sobre o que acontece quando ele é agredido ou desregulado.

**Análise item por item contra E1:**

| Item | Conteúdo | Verdade E1 | Julgamento |
|------|----------|-----------|-----------|
| I | Após irradiação abdominal, população +4 pode reentrar no ciclo e repovoar cripta | "as células da posição +4 reentram no ciclo e repovoam a cripta" | **C** (correto) |
| II | Célula de Paneth secreta Wnt3 e ligantes de Notch para tronco vizinha | "a Paneth é nicho celular... secreta Wnt3... e ligantes de Notch" | **C** (correto) |
| III | Fibroblastos subepiteliais secretam antagonistas de BMP como gremlina | "trofócitos e telócitos... secretam... antagonistas de BMP como a gremlina" | **C** (correto) |
| IV | Perda das duas cópias de APC reduz β-catenina nuclear, leva cripta à quiescência | E1 diz: "Perdidas duas cópias, β-catenina **acumula-se**" (não reduz); resultado é proliferação (adenoma), não quiescência | **E** (errado) |

**Gabarito real (verdade mecanística):** `CCCE` (4 letras para 4 itens) ✓

**Gabarito YAML declarado:** `CCCE` ✓

**Gabarito IMPRESSO (PDF p. 35):** `CCCCE` ✗ **(5 letras — erro tipográfico claro)**

**Avaliação:** Erro de impressão. O YAML está correto; o PDF está errado.

---

### Resumo Checagem 1
- **Questões conferidas:** 30
- **Divergências:** 1
  - **Q13: impresso = `CCCCE`, real = `CCCE`** — Gabarito impresso tem 5 letras quando deveria ter 4 (erro tipográfico)
- **Ação:** BLOQUEIA. Corrigir gabarito impresso antes de mover PDF.

---

## Checagem 2 — Sem corrida degenerada

### MC (20 questões): Sequência de respostas

Q01=C, Q02=A, Q04=D, Q06=B, Q08=E, Q10=B, Q11=D, Q12=B, Q14=C, Q15=E, Q16=B, Q17=C, Q19=A, Q21=D, Q22=E, Q23=C, Q24=B, Q26=D, Q27=A, Q29=E

**Busca por corrida de 4+ iguais consecutivas:**
- Nenhuma sequência de 4 letras idênticas seguidas detectada
- Maior corrida encontrada: comprimento 2 (não é degenerado)

**Resultado:** ✓ OK

### C/E (10 questões, 40 itens): Sequência consolidada

Q03=CCEE, Q05=CCEC, Q07=ECCE, Q09=CECC, Q13=CCCE, Q18=CEEC, Q20=ECCC, Q25=ECEE, Q28=EECE, Q30=EECC

**Busca por blocos longos:**
- Bloco mais longo só-C: "CCC" em Q20 itens II-III-IV (comprimento 3)
- Bloco mais longo só-E: "EE" em múltiplos lugares (comprimento 2)
- Ping-pongue CECE: não detectado por extensão (não há CECECECE)

**Resultado:** ✓ OK (blocos isolados de 3 itens de um tipo são aceitáveis; nenhum padrão degenerado mecânico)

---

## Checagem 3 — Distribuição não-viciada

### Múltipla escolha (20 questões, letras A-E)

| Letra | Questões | Frequência | % |
|-------|-----------|-----------|-----|
| A | Q02, Q19 | 2 | 10% |
| B | Q06, Q10, Q12, Q16, Q24 | 5 | 25% |
| C | Q01, Q14, Q17, Q23 | 4 | 20% |
| D | Q04, Q11, Q21, Q26 | 4 | 20% |
| E | Q08, Q15, Q22, Q29 | 4 | 20% |

**Avaliação:** Nenhuma letra acima de ~40% (máximo = B com 25%). Distribuição bem equilibrada. ✓

### C/E (10 questões, 40 itens)

| Tipo | Total | Frequência | % |
|------|-------|-----------|-----|
| C | 22 | 22/40 | 55% |
| E | 18 | 18/40 | 45% |

**Proporção C:E = 22:18 ≈ 1.22:1**

**Avaliação:** Leve predomínio de C (55%), mas não desiquilibrado (_grosseiramente_ equilibrado significa ~50±10%). Aceitável sem reposicionamento necessário. ✓

---

## Veredito

### Status: VERMELHO — BLOQUEIA

**Justificativa:**
- **Checagem 1 (gate hard):** Q13 tem erro de impressão no PDF (`CCCCE` em vez de `CCCE`). Gabarito impresso ≠ gabarito real.
- **Checagem 2:** OK — sem corridas degeneradas.
- **Checagem 3:** OK — distribuição não-viciada.

**Ação obrigatória:** Corrigir Q13 no gabarito impresso do PDF de `CCCCE` para `CCCE` antes de mover para `resumos-gerados/` ou qualquer outro destino.

**Responsável pela correção:** COMPILADOR (roda `gerar_main.py` após validação de correção no `.typ`).

---

## Apêndice — Confirmação de outras questões C/E

Amostra verificada de todas as 10 questões C/E (100% auditadas):
- Q03: CCEE ✓
- Q05: CCEC ✓
- Q07: ECCE ✓
- Q09: CECC ✓
- Q13: **CCCE (real) vs CCCCE (impresso)** ✗
- Q18: CEEC ✓
- Q20: ECCC ✓
- Q25: ECEE ✓
- Q28: EECE ✓
- Q30: EECC ✓

**Conclusão:** Apenas Q13 diverge. Todas as demais questões (29/30) estão corretas.
