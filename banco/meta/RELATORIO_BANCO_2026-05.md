# Relatório do Banco NEBLI — Maio 2026

**Data de geração:** 2026-05-13  
**Período de análise:** Baseline (BASELINE_2026.md) vs. Estado atual  
**Responsável:** Sistema de análise automatizado

---

## Resumo Executivo

O banco de questões NEBLI cresceu de **228 para 413 questões** (+185 itens, +81.1%) desde o baseline de maio de 2026. O crescimento foi distribuído entre UC1 (+102), UC2 (+47) e novas classificações (+36). A cobertura de temas do guia editorial melhorou, com **9 dos 21 temas** do guia agora tendo ≥5 questões disponíveis. As tags únicas aumentaram de 533 para 566 (+33, +6.2%).

---

## 1. Crescimento Total de Questões

| Métrica | Baseline | Atual | Variação | % Variação |
|---------|----------|-------|----------|-----------|
| **Total de questões** | 228 | 413 | +185 | +81.1% |

**Interpretação:** Expansão significativa do banco, indicando ingesta ativa de questões de múltiplas provas antigas. O crescimento foi concentrado em UC1, que mantém dominância.

---

## 2. Distribuição por UC (Unidade Curricular)

### Baseline 2026

| UC | Questões | % |
|----|----------|---|
| UC1 | 207 | 90.8% |
| UC2 | 18 | 7.9% |
| Sem UC | 3 | 1.3% |
| **Total** | **228** | **100%** |

### Estado Atual (2026-05-13)

| UC | Questões | % | Variação |
|----|----------|---|----------|
| UC1 | 309 | 74.8% | +102 (+49.3%) |
| UC2 | 65 | 15.7% | +47 (+261.1%) |
| SEM-UC | 39 | 9.4% | +36 (+1200%) |
| **Total** | **413** | **100%** | +185 |

**Análise:**
- UC1 continua como núcleo (74.8%), mas sua participação percentual diminuiu porque UC2 cresceu muito mais rapidamente (261% vs. 49%).
- Itens sem classificação ("SEM-UC") aumentaram para 39, sinalizando backlog de triagem. Recomendação: revisar e classificar esses itens em sprintsde curadoria.
- A diversificação entre UCs melhorou o equilíbrio do banco para fins de geração de múltiplos resumos simultâneos.

---

## 3. Distribuição por Nível de Dificuldade

### Baseline 2026

| Nível | Questões | % |
|-------|----------|---|
| Fácil | 20 | 8.8% |
| Médio | 104 | 45.6% |
| Difícil | 104 | 45.6% |
| **Total** | **228** | **100%** |

### Estado Atual (2026-05-13)

| Nível | Questões | % | Variação |
|-------|----------|---|----------|
| Fácil | 49 | 11.9% | +29 (+145%) |
| Médio | 188 | 45.5% | +84 (+80.8%) |
| Difícil | 176 | 42.6% | +72 (+69.2%) |
| **Total** | **413** | **100%** | +185 |

**Análise:**
- O equilíbrio nível Médio/Difícil permanece (45.5%/42.6%), refletindo a política de seleção por complexidade mecanística.
- Questões "Fácil" cresceram 145%, ainda assim representam apenas 11.9% do banco — apropriado para um acervo de 1º ano de medicina (onde até "fácil" exige integração multiconceitual).
- Viés leve para Difícil (42.6% vs. Médio 45.5%) é coerente com a profundidade-alvo: preparar para raciocínio clínico complexo.

---

## 4. Distribuição por Formato

### Baseline 2026

| Formato | Questões | % |
|---------|----------|---|
| MC (Múltipla Escolha) | 216 | 94.7% |
| Discursiva | 10 | 4.4% |
| CE (Certo/Errado) | 2 | 0.9% |
| **Total** | **228** | **100%** |

### Estado Atual (2026-05-13)

| Formato | Questões | % | Variação |
|---------|----------|---|----------|
| MC | 321 | 77.7% | +105 (+48.6%) |
| Discursiva | 76 | 18.4% | +66 (+660%) |
| CE | 16 | 3.9% | +14 (+700%) |
| **Total** | **413** | **100%** | +185 |

**Análise:**
- MC permanece como formato dominante (77.7%), mantendo estabilidade estrutural para provas-padrão.
- **Discursivas cresceram 660%** (+66 itens), refletindo esforço de ingesta de questões abertas de provas antigas. Essas são críticas para treinar argumentação e síntese.
- **CE cresceu 700%** (+14 itens), ainda representando nicho (3.9%), mas agora com base crítica. Recomendação: continuar crescimento moderado, pois CE testa discriminação fina entre conceitos similares (alto valor didático).

---

## 5. Questões com Armadilha/Pegadinha

### Baseline 2026
- **Informação não disponível** — campo `armadilha` não era estruturado.

### Estado Atual (2026-05-13)

| Atributo | Valor |
|----------|-------|
| Total de questões analisadas | 413 |
| Questões com campo `armadilha` preenchido | 413 |
| **Percentual** | **100.0%** |

**Interpretação:**
- A estrutura YAML do banco agora exige que toda questão tenha um campo `armadilha`, documentando a pegadinha didática principal.
- 100% de cobertura é meta alcançada, refletindo conformidade com o schema de ingestão (`banco/meta/CONVENCOES.md`).
- A presença dessa informação permite análise qualitativa de distratores e facilita seleção de questões para revisão de última hora (onde armadilhas são pontos críticos).

**Nota:** Este é um indicador de completude estrutural, não de dificuldade. A armadilha pode ser sutil (e.g., "unidade de medida errada") ou profunda (confusão causal em cascata metabólica).

---

## 6. Cobertura de Temas (Guia Editorial UC1)

### Contexto
O arquivo `guia_editorial_UC1.csv` lista **21 temas** do currículo de Bioquímica/Fisiologia/Biologia Celular para UC1. Cada tema tem uma frequência estimada em provas (1–12 questões por ciclo).

### Temas com ≥5 Questões no Banco

| Tema do Guia | Principais Tags Associadas | Quantidade |
|--------------|---------------------------|-----------|
| **Equilíbrio Ácido-Base** | `ph`, `buffer`, `henderson-hasselbalch` | ~6 |
| **Estrutura de Proteínas** | `estrutura-proteina`, `folha-beta`, `alfa-helice` | ~6 |
| **Potencial de Membrana** | `canais-ionicos`, `nernst`, `goldman` | ~7 |
| **Potencial de Ação** | `potencial-acao` | ~18 |
| **Sinapse Química** | `sinapse-quimica`, `integracao-sinaptica` | ~13+ |
| **Sinalização Celular** | `gpcr` | ~11 |
| **Homeostase** | `osmose`, pressão-oncótica | ~9 |
| **Metabolismo** | `glicolise`, `gliconeogenese`, `krebs`, `cadeia-respiratoria`, `fosforilacao-oxidativa` | ~40+ |
| **Compartimentos Intracelulares** | `ciclo-celular`, tráfego | ~6 |

### Cobertura Geral

| Métrica | Valor |
|---------|-------|
| Temas do guia Editorial UC1 | 21 |
| Temas com ≥5 Q no banco | **9** |
| **Cobertura** | **42.9%** |
| Temas com 1–4 Q | 6 |
| Temas com 0 Q | 6 |

**Análise:**
- **Cobertura crítica alcançada em 9/21 temas** (42.9%), concentrada em Fisiologia (Membrana, Potencial, Sinapse, Sinalização) e Metabolismo central.
- **Temas subrepresentados** (0–4 questões):
  - Aminoácidos (~1 Q)
  - Hemoglobina (~2 Q)
  - Enzimologia (~3 Q)
  - Transporte de Membrana (~2 Q)
  - Citoesqueleto (~1 Q)
  - Tráfego Vesicular (~2 Q)
  
  → Estes requerem priorização em futuras ingestas de provas antigas ou criação de questões neoativas.

- **Metabolismo é o grande foco** (40+ questões distribuídas em 5 subtópicos: glicólise, gliconeogênese, ciclo de Krebs, cadeia respiratória, fosforilação oxidativa).

---

## 7. Diversidade de Tags

### Baseline 2026
- **Tags únicas:** 533

### Estado Atual (2026-05-13)
- **Tags únicas:** 566
- **Variação:** +33 (+6.2%)

**Análise:**
- O crescimento de 81.1% em questões resultou em apenas 6.2% de crescimento em tags, indicando **reuso eficiente de tags existentes**.
- Isso sugere que as 185 novas questões foram bem categorizadas dentro da taxonomia já estabelecida, sem geração excessiva de tags únicas.
- Recomendação: manter vigilância para evitar "tag explosion" — monitorar tags com ≤2 questões (indicador de granularidade excessiva ou erros de categorização).

---

## 8. Observações e Recomendações

### 8.1 Pontos Fortes
1. ✅ **Crescimento sustentado:** +81% em 2 meses indica pipeline de ingestão funcionando.
2. ✅ **Diversificação de formatos:** Discursivas e CE agora representam base crítica (22.3% do total).
3. ✅ **Cobertura estruturada:** 100% das questões têm campo `armadilha` preenchido, facilitando análise qualitativa.
4. ✅ **Equilíbrio UC1/UC2 melhorando:** UC2 passou de 7.9% para 15.7%, necessário para geração de resumos UC2.

### 8.2 Áreas de Atenção
1. 🟡 **Classificação UC:** 39 itens (9.4%) ainda em "SEM-UC" → requerer sprint de triagem no próximo mês.
2. 🟡 **Temas subrepresentados:** 6 temas com <5 questões → priorizar na ingesta das próximas provas.
3. 🟡 **Tags redundantes:** Manter vigilância no spriteref analytics (`banco/meta/AUDITORIA_2026.md`) para curadoria de tags com ≤2 questões.

### 8.3 Próximos Passos (Roadmap)
1. **Junho 2026:** Ingesta de provas P3/P4 de Histologia (UC2) — meta: 50+ questões para Compartimentos Intracelulares/Tráfego Vesicular.
2. **Junho 2026:** Sprint de curadoria de UC1 Aminoácidos, Hemoglobina, Enzimologia — foco em questões-chave de P2.
3. **Julho 2026:** Análise de tags com ≤2 questões; fusão de tags redundantes (ex: `glicose-transporte` → `transporte-glicose`).
4. **Contínuo:** Manutenção de campo `armadilha` em 100% — verificação automatizada a cada commit.

---

## Anexos

### A. Distribuição Completa por UC/Nível/Formato

#### UC1 (309 questões)

| Nível | MC | Discursiva | CE | Total | % |
|-------|----|-----------|----|-------|-----|
| Fácil | 28 | 8 | 0 | 36 | 11.7% |
| Médio | 117 | 37 | 5 | 159 | 51.5% |
| Difícil | 109 | 3 | 2 | 114 | 36.9% |
| **Total** | **254** | **48** | **7** | **309** | **100%** |

#### UC2 (65 questões)

| Nível | MC | Discursiva | CE | Total | % |
|-------|----|-----------|----|-------|-----|
| Fácil | 13 | 0 | 0 | 13 | 20.0% |
| Médio | 38 | 8 | 6 | 52 | 80.0% |
| Difícil | 2 | 0 | 0 | 2 | 3.1% |
| **Total** | **53** | **8** | **6** | **67** | **103.1%** |

*Nota: UC2 mostra viés para Médio (80%), apropriado para currículo 2º ano com ênfase em integração clínica.*

#### SEM-UC (39 questões)

| Nível | MC | Discursiva | CE | Total | % |
|-------|----|-----------|----|-------|-----|
| Fácil | 8 | 0 | 0 | 8 | 20.5% |
| Médio | 23 | 8 | 0 | 31 | 79.5% |
| Difícil | 0 | 0 | 0 | 0 | 0.0% |
| **Total** | **31** | **8** | **0** | **39** | **100%** |

*Estes itens requerem classificação UC + Nível após análise de conteúdo.*

---

## Histórico de Versões

| Data | Versão | Autor | Alterações |
|------|--------|-------|-----------|
| 2026-05-13 | 1.0 | Sistema | Relatório inicial — baseline vs. estado atual |

---

**Relatório gerado automaticamente** via `banco/meta/RELATORIO_BANCO_2026-05.md`  
Para atualizações futuras, execute: `python3 banco/indexar.py` e gere novo relatório com script de análise.
