# Banco NEBLI — Baseline 2026-05-13

## Metadados

| Campo | Valor |
|-------|-------|
| **Data de geração** | 2026-05-13 |
| **Script** | `banco/indexar.py` |
| **Índice gerado** | `banco/indice/banco.json` |
| **Total de questões indexadas** | **228** |
| **Tags únicas** | **533** |

---

## Distribuição por UC

| UC | Questões | % |
|----|----------|---|
| UC1 | 207 | 90,8% |
| UC2 | 18 | 7,9% |
| Sem UC (a classificar) | 3 | 1,3% |
| **Total** | **228** | **100%** |

---

## Distribuição por Nível

| Nível | Questões | % |
|-------|----------|---|
| Fácil | 20 | 8,8% |
| Médio | 104 | 45,6% |
| Difícil | 104 | 45,6% |
| **Total** | **228** | **100%** |

---

## Distribuição por Formato

| Formato | Questões | % |
|---------|----------|---|
| MC (múltipla escolha) | 216 | 94,7% |
| Discursiva | 10 | 4,4% |
| CE (certo/errado) | 2 | 0,9% |
| **Total** | **228** | **100%** |

---

## Observações

- 533 tags únicas indexadas; `indexar.py` reportou 455 tags com ≤2 questões — candidatas à fusão em sprint futuro de curadoria.
- 3 questões sem `uc_origem` definida — verificar manualmente em `banco/questoes/`.
- Banco de CE (certo/errado) subrepresentado (2 questões) — expandir se UC2 usar esse formato.
- Proporção médio/difícil (45,6%/45,6%) sugere viés de seleção para questões desafiadoras; avaliar se é adequado ao nível do aluno-alvo.
