# Consolidações de Tags — banco NEBLI

**Gerado em:** 2026-05-13  
**Base:** `banco/indice/banco.json` (413 questões) + `banco/meta/taxonomia.md`  
**Convenção:** formato `- \`tag-antiga\` → \`tag-nova\` (razão: …, N usos)`

---

## A. Typos e variantes ortográficas

Tags com grafia incorreta encontradas no JSON mas ainda não corrigidas na taxonomia:

- `pressao-osmotika` → `pressao-osmotica` (razão: typo — 'k' espúrio, N=aparece em questões de tonicidade)
- `desequilibrio-osmotika` → `desequilibrio-osmotico` (razão: typo — mesma raiz)
- `hipertonika` → `hipertonica` (razão: typo — 'k' espúrio)
- `isosmotika` → `isosmótica` → `isosmótica` (razão: typo — adotar `isosmótica` sem acento: `isosmótica`)
- `estresse-osmotika` → `estresse-osmotico` (razão: typo — mesma raiz)
- `transmissao-sinaptca` → `transmissao-sinaptica` (razão: typo — 'i' faltando)
- `axionio` → `axonio` (razão: typo — letra extra)
- `diametro-axonial` → `diametro-axonal` (razão: typo — adjetivo incorreto)
- `folheta-beta` → `folha-beta` (razão: typo — forma canônica já em uso na taxonomia, 1 uso)
- `retículo-endoplasmático` → `reticulo-endoplasmatico` (razão: typo — acentuação residual não corrigida, pós consolidação 2026-05-05)
- `sinapse-metabotrópica` → `sinapse-metabotropica` (razão: typo — acento residual)
- `receptor-metaborotico` → `receptor-metabotropico` (razão: typo — 'o' por 'op')
- `cinética-ativacao` → `cinetica-ativacao` (razão: typo — acento residual)
- `cinética-inativacao` → `cinetica-inativacao` (razão: typo — acento residual)
- `potencial-equilibrio-ionico` → `potencial-equilibrio` (razão: typo/redundância — a tag canônica já absorveu `potencial-equilíbrio-iônico` em 2026-05-05; 1 uso residual)
- `KM` → `km` (razão: typo — caixa alta; a forma canônica é `km`, 1 uso)
- `PEPS` → `peps` (razão: typo — caixa alta; a forma canônica é `peps`, 1 uso)
- `cAMP-diesterase` → `fosfodiesterase` (razão: typo/sinônimo — nome informal, a enzima canônica é fosfodiesterase, 1 uso)
- `cAMP-permevel` → eliminar ou mapear para `camp` (razão: typo grave + significado ambíguo — provavelmente "cAMP-permeável"; substituir pelo contexto; 1 uso)
- `lutp-ltd` → `ltp-ltd` (razão: typo — 'u' espúrio)

### Tags em inglês não convertidas (residuais pós-2026-05-05)

- `gap-junction` → `juncoes-gap` (razão: inglês residual — conversão de `gap-junctions` foi feita em 2026-05-05 mas surgiu nova variante no singular)
- `gap junctions` (com espaço) → `juncoes-gap` (razão: inglês + espaço em tag; não é slug válido)
- `regulatory-volume-increase` → `regulacao-volume` (razão: inglês; criar tag `regulacao-volume` caso ainda não exista)
- `RVI` → `regulacao-volume` (razão: sigla em inglês; mesma tag-alvo acima)
- `CICR` → `liberacao-ca2-ret` ou criar `cicr` lowercase (razão: sigla — Calcium-Induced Calcium Release; se houver ≥3 questões, manter como `cicr`; caso contrário subsumível por `calcio-intracelular`)

---

## B. Sinônimos (tags com <3 usos que duplicam tags mais frequentes)

- `gradiente-ionico` → `gradientes-ionicos` (razão: sinônimo — singular/plural do mesmo conceito; `gradiente-ionico` 1 uso, `gradientes-ionicos` 2 usos)
- `calcio` → `calcio-intracelular` (razão: sinônimo/subconjunto — o único uso de `calcio` genérico se refere ao cálcio como segundo mensageiro, já coberto por `calcio-intracelular` com 7 usos; 1 uso)
- `segundo-mensageiro` → `mensageiro-celular` (razão: sinônimo — singular de `segundos-mensageiros`/`mensageiro-celular`; a tag canônica é `mensageiro-celular` com 6 usos)
- `segundos-mensageiros` → `mensageiro-celular` (razão: sinônimo — `mensageiro-celular` já é o termo canônico com 6 usos; 1 uso da variante)
- `sinalizacao-celular` → `mensageiro-celular` (razão: sinônimo funcional — em todas as questões, refere-se ao mesmo contexto de sinalização por segundos-mensageiros; 1 uso)
- `via-das-pentoses` → `via-pentoses` (razão: sinônimo — artigo desnecessário no slug; `via-pentoses` é a forma canônica com 2 usos)
- `ciclo-krebs` → `krebs` (razão: sinônimo — `krebs` é a forma canônica com 10 usos; `ciclo-krebs` é redundante)
- `cinetica-enzimatica` → `enzimologia` (razão: subconjunto — `enzimologia` cobre cinética + Km + Vmax + inibição com 10 usos; `cinetica-enzimatica` é subconjunto direto)
- `km-michaelis` → `km` (razão: sinônimo — o Km de Michaelis-Menten é o único Km no banco; `km` tem 1 uso como tag independente e aparece em `enzimologia`)
- `fosfolipidio` → `fosfolipidios` (razão: sinônimo — singular/plural; `fosfolipidios` tem 4 usos como canônico)
- `estrutura-proteica` → `estrutura-proteina` (razão: sinônimo — duas grafias para o mesmo conceito; `estrutura-proteina` tem 2 usos na taxonomia)
- `mecanorreceptor` → `receptor-mecanico` (razão: sinônimo — `receptor-mecanico` tem 2 usos na taxonomia, `mecanorreceptor` aparece no JSON como variante)
- `canais-sensiveis-estiramento` → `canais-sensiveis-tensao` (razão: sinônimo — tensão e estiramento descrevem o mesmo estímulo mecânico; `canais-sensiveis-tensao` é a forma canônica com 1 uso consolidado em 2026-05-05)
- `receptor-metabotropico` → `sinapse-metabotropica` (razão: sinônimo/subconjunto — o contexto é sempre o de sinapse química metabotrópica; `sinapse-metabotropica` tem 3 usos)
- `sinapse-ionotropica` → `sinapse-quimica` + `receptores-ionotropicos` (razão: sinônimo parcial — a tag combina dois conceitos já cobertos separadamente; separar nas duas tags canônicas)

### Sinônimos canais/voltagem (residuais da consolidação 2026-05-05)

- `canais-na` → `canais-na-voltagem` (razão: sinônimo — consolidação feita em 2026-05-05 mas tag residual ainda aparece no JSON; 8 usos na forma canônica)
- `sinapses-quimicas` → `sinapse-quimica` (razão: sinônimo — consolidação feita em 2026-05-05 mas forma plural ainda aparece; 6 usos na forma canônica)
- `sinapse-eletrica` → `sinapses-eletricas` (razão: sinônimo — singular/plural; `sinapses-eletricas` é a forma canônica com 2 usos)

---

## C. Tags muito específicas subsumedíveis por tag-pai

- `atpase-e1e2` → `transporte-ativo-primario` (razão: subconjunto — a classificação E1/E2 é um mecanismo interno das bombas tipo P, todas cobertas por `transporte-ativo-primario` com 4 usos; 1 uso)
- `intoxicacao-digitalica` → `bomba-na-k` (razão: subconjunto — intoxicação digitálica age via inibição da Na/K-ATPase; `ouabaina` e `intoxicacao-digitalica` podem ambos ser subsumidos por `bomba-na-k` com 5 usos; 1 uso cada — ver seção Tags a preservar para decisão sobre `ouabaina`)
- `density-canais-na` → `densidade-canais` (razão: subconjunto — tag mais específica já coberta pela tag-pai; 1 uso cada; consolidar nas duas instâncias)
- `densidade-canais-na` → `densidade-canais` (razão: subconjunto — mesma situação acima; 1 uso)
- `velocidade-transmissao` → `velocidade-propagacao` (razão: subconjunto/sinônimo — no contexto do banco ambas descrevem a velocidade de condução do PA; `velocidade-propagacao` tem 1 uso como canônica; 1 uso cada)
- `propagacao-potencial` → `potencial-acao` (razão: subconjunto — a propagação é aspecto do PA; `potencial-acao` tem 8 usos; 1 uso)
- `zona-disparo` → `cone-insercao-axonio` (razão: sinônimo anatômico — zona de disparo é o cone de inserção do axônio; 1 uso cada)
- `co2-bicarbonato` → `buffers` (razão: subconjunto — o sistema CO₂/bicarbonato é o principal tampão fisiológico; `buffers` tem 2 usos; 1 uso)
- `espontaneidade-reacao` → `termodinamica` (razão: subconjunto — espontaneidade é tópico de termodinâmica química; `termodinamica` tem 1 uso, ambas com apenas 1; manter `termodinamica` como canônica)
- `constante-equilibrio` → `termodinamica` (razão: subconjunto — Keq é conceito termodinâmico; 1 uso)
- `afinidade-oxigenio` → `hemoglobina` (razão: subconjunto — afinidade do O₂ é propriedade da hemoglobina; `hemoglobina` tem 1 uso; 1 uso)
- `efeito-bohr` → `hemoglobina` (razão: subconjunto — o efeito Bohr é mecanismo da hemoglobina; 1 uso — **ver também seção Tags a preservar**)
- `modulador-alosterico` → `regulacao-metabolica` (razão: subconjunto — modulação alostérica é mecanismo de regulação; `regulacao-metabolica` tem 8 usos; 1 uso)
- `albumina` → `pressao-oncotica` (razão: subconjunto — albumina é o principal determinante da pressão oncótica; `pressao-oncotica` tem 2 usos; 1 uso)
- `edema` → `equilibrio-starling` (razão: subconjunto — edema é consequência de desequilíbrio de Starling; `equilibrio-starling` tem 2 usos; 1 uso)
- `osmolitos-organicos` → `regulacao-volume` (razão: subconjunto — osmólitos orgânicos são mecanismo de regulação de volume; criar tag `regulacao-volume` se necessário)
- `transducao` → `receptor-sensorial` (razão: subconjunto — no contexto do banco, transdução sensorial; `receptor-sensorial` tem 2 usos; `transducao` tem 2 usos — avaliar se há usos fora do contexto sensorial antes de consolidar)

### Subconjuntos no contexto de sinapses

- `acetilcolina` → `neurotransmissor` (razão: subconjunto — acetilcolina é um neurotransmissor; `neurotransmissor` tem 3 usos; `acetilcolina` tem 1 uso — **ver seção Tags a preservar**)
- `cl-permeabilidade` → `gaba-receptor` (razão: subconjunto — permeabilidade a Cl⁻ é a ação do GABA-R; `gaba-receptor` tem 1 uso; 1 uso)
- `numero-sinapses` → `integracao-sinaptica` (razão: subconjunto — número de sinapses é fator de integração; `integracao-sinaptica` tem 1 uso; 1 uso)
- `peso-sinaptico` → `integracao-sinaptica` (razão: subconjunto — peso é propriedade da integração sináptica; 1 uso)
- `transmissao-rapida` → `sinapse-quimica` (razão: subconjunto — transmissão rápida é característica da sinapse ionotrópica; 1 uso)

---

## Tags a preservar

Tags com poucos usos mas **valor pedagógico único** — não devem ser consolidadas:

| Tag | Usos | Razão para preservar |
|-----|------|----------------------|
| `ouabaina` | 1× | Fármaco-modelo do bloqueio de Na/K-ATPase; aparece em questões farmacológicas com nome próprio |
| `intoxicacao-digitalica` | 1× | Conexão clínica crítica (digoxina → arritmia); perder a tag quebraria buscas por contexto de uso terapêutico |
| `efeito-bohr` | 1× | Efeito nomeado com mecanismo próprio (pH ↓ → afinidade Hb ↓); pedagogicamente distinto de "hemoglobina" genérico |
| `efeito-pasteur` | 3× | Efeito nomeado historicamente importante; conexão entre metabolismo aeróbio/anaeróbio com identidade própria |
| `ciclo-cori` | 2× | Conceito de integração metabólica músculo↔fígado; não coberto por nenhuma tag mais ampla sem perda de especificidade |
| `f26bp` | 3× | Regulador-chave do switch glicólise/gliconeogênese; sem tag pai que cubra esse papel sem ser vaga demais |
| `dineina-axonemal` | 1× | Clinicamente relevante para síndrome de Kartagener/discinesia ciliar; único marcador de função ciliar no banco |
| `celulas-beta-pancreaticas` | 1× | Tecido específico com papel único na regulação da glicemia; relevante para diabetes |
| `doencas-metabolicas` | 2× | Tag de ponte clínica cross-tópica (Von Gierke, G6PD, etc.); subsumi-la em qualquer via metabólica quebraria a função de agrupamento |
| `peps` | 1× | Conceito pedagógico distinto (PEPS vs PIPS); manter ambos para questões de integração sináptica |
| `periodo-refratario-absoluto` | aparece no JSON | Clinicamente relevante para arritmias; mais específico que `periodo-refratario` (5×) |
| `periodo-refratario-relativo` | aparece no JSON | Par pedagógico do absoluto; perder a distinção elimina questões sobre modulação de frequência de disparo |
| `receptores-nmda` | aparece no JSON | Receptor com papel único na plasticidade sináptica (LTP/LTD) e na ação da ketamina; subsumi-lo em `receptores-ionotropicos` apagaria essa distinção |
| `receptores-ampa` | aparece no JSON | Par pedagógico dos NMDA; trafego de AMPARs é mecanismo do LTP; valor único |
| `ltp-ltd` | aparece no JSON | Plasticidade sináptica — conceito com relevância neurológica e farmacológica própria |
| `nadph` | 2× | Cofator com papel dual (via pentoses + glutationa + lipogênese); subsumi-lo em `via-pentoses` perderia usos em estresse oxidativo |
| `g6pd` | aparece no JSON | Anemia hemolítica por deficiência; ponto de encontro entre bioquímica e hematologia — tag clínica insubstituível |
| `p53` | 5× | Supressor tumoral com identidade pedagógica própria; subsumi-lo em `oncoproteinas` (6×) é possível mas perderia especificidade diagnóstica |
| `acetilcolina` | 1× | Neurotransmissor com farmacologia própria (anticolinérgicos, miastenia, organofosforados); manter separado de `neurotransmissor` genérico |
| `tudo-ou-nada` | aparece no JSON | Princípio fisiológico fundamental do PA; subsumi-lo em `potencial-acao` (8×) perderia questões que testam especificamente esse princípio |

---

## Notas de implementação

1. **Prioridade de correção:** Typos (seção A) > Sinônimos residuais de 2026-05-05 (seção B, última subseção) > Sinônimos novos (seção B) > Subconjuntos (seção C).
2. **Método:** Para cada consolidação, buscar no JSON por `"tag-antiga"` e substituir pela `"tag-nova"` em todas as questões afetadas, depois atualizar `taxonomia.md`.
3. **Próxima consolidação prevista:** após ~50 questões novas de UC2 (conforme pendência em `taxonomia.md`).
4. **Tags a criar (novas necessidades detectadas):**
   - `regulacao-volume` — para RVI, osmólitos orgânicos, murchamento celular
   - `periodo-refratario-absoluto` e `periodo-refratario-relativo` — como subtags de `periodo-refratario`
   - `receptor-nmda` / `receptores-nmda` — consolidar variantes de caixa
