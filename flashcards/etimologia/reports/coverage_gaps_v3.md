# Auditoria adversarial de cobertura v3

- Entradas no léxico mestre: 800
- Termos de inferência efetivamente reservados: 300/300

## Resultado por eixo

| Eixo | Cobertos | Meta | Cobertura |
|---|---:|---:|---:|
| procedimentos confundiveis | 16 | 16 | 100.0% |
| sufixos menos expostos | 17 | 17 | 100.0% |
| forma estrutura anatomica | 17 | 17 | 100.0% |
| cor aparencia | 13 | 13 | 100.0% |
| curso temporal | 15 | 15 | 100.0% |
| patologia discriminadores | 10 | 10 | 100.0% |
| semiologia discriminadores | 11 | 11 | 100.0% |
| polissemia falsa segmentacao | 10 | 10 | 100.0% |
| duplas greco latinas | 12 | 12 | 100.0% |
| farmacologia linguagem | 7 | 7 | 100.0% |
| nomenclatura anatomica latina | 12 | 12 | 100.0% |

## Lacunas explícitas

### Procedimentos Confundiveis

Nenhuma lacuna no inventário mínimo.

### Sufixos Menos Expostos

Nenhuma lacuna no inventário mínimo.

### Forma Estrutura Anatomica

Nenhuma lacuna no inventário mínimo.

### Cor Aparencia

Nenhuma lacuna no inventário mínimo.

### Curso Temporal

Nenhuma lacuna no inventário mínimo.

### Patologia Discriminadores

Nenhuma lacuna no inventário mínimo.

### Semiologia Discriminadores

Nenhuma lacuna no inventário mínimo.

### Polissemia Falsa Segmentacao

Nenhuma lacuna no inventário mínimo.

### Duplas Greco Latinas

Nenhuma lacuna no inventário mínimo.

### Farmacologia Linguagem

Nenhuma lacuna no inventário mínimo.

### Nomenclatura Anatomica Latina

Nenhuma lacuna no inventário mínimo.

## Mudança de seleção

A frequência deixa de ser o principal atalho. O próximo núcleo usa `Q = 3T + 3C + 2E + 2R + F - 2O`.

- `E` premia baixa exposição: termos vistos raramente, mas cuja confusão custa rigor.
- `C` premia famílias confundíveis e polissemias.
- `O` penaliza cards isolados óbvios, como derm/o → pele.
- Termos óbvios só entram como suporte de aplicação mais difícil.

## Consequência para o deck completo

O deck não será uma lista de raízes frequentes. Será organizado em camadas: método, famílias, raízes não óbvias, aplicação inédita e limites da inferência.
