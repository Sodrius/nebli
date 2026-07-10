# Revisão profunda Tier 3 — UC01-BIOQ-10-enzimas-i

**Tema (ancoragem):** Enzimas I — natureza proteica, sítio ativo e ajuste induzido, cofatores/coenzimas, energia de ativação e complexo ES, mecanismos catalíticos, cinética de Michaelis–Menten (KM, Vmax, kcat, kcat/KM, Lineweaver–Burk). **Inibição e regulação ficam para Enzimas II.**
**Autor:** Marisa Helena (apostila histórica capturada no pipeline NEBLI)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real com bioquímica; ensino médio + ~6 meses de medicina; sem livro-texto aberto ao lado.
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

### Âncora de tema

- **3 conceitos centrais que eu-aluno quero aprender:** (1) por que enzima acelera sem mudar equilíbrio (Ea vs ΔG); (2) o que significa KM operacionalmente e por que KM alto = afinidade baixa; (3) por que o sítio é complementar ao estado de transição, não ao substrato (Pauling).
- **2 temas vizinhos que NÃO são esse:** inibição enzimática (competitiva, não-competitiva, incompetitiva) — fica para Enzimas II; alosterismo e zimogênios — também Enzimas II.

---

## 1. Pontos de parada (simulação de leitura linha-a-linha)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Capa + nota de uso | OK | 1 | "MM rende sempre" é gancho honesto. |
| Sumário | OK | 2 | Hierarquia clara; **mas** sumário NÃO lista Etapa 4 e ela aparece como header lá na p.43 — gatilho de confusão futura. |
| 1.1 abertura ("por que é rápida") | OK | 3 | Abre com o problema cinético (fosfomonoester, 10⁸ anos vs ms). Concreto. |
| Box "Enzima não muda K, só k" | OK | 4 | Box bate na cabeça do erro mais comum logo cedo. Curto, citável. |
| Tabela EC + figura | **[STOP: pág 4]** | 4 | Header "Enzimas" + tabela de classes EC aparecem em fonte minúscula no render; aluno em dificuldade vê "muitos nomes-ase juntos" e pula. Tabela tem valor de referência mas sem ancoragem ("oxirredutase, ex: lactato desidrogenase" — eu-aluno não sei o que é desidrogenase ainda). |
| 1.2 sítio ativo | OK | 5–6 | Modelo Fischer→Koshland com box "Fischer está superado" funciona; quiralidade luva direita é boa analogia. |
| 1.3 cofatores | **[STOP leve: pág 7–8]** | 7–8 | Box pelagra é ótimo, mas a lista de vitaminas B (B3→NAD, B2→FAD, B5→CoA, B6→PLP, B1→TPP, B7→biotina) vem em um único parágrafo de 6 mapeamentos. Eu-aluno precisa de 4 leituras para fixar. Pediria tabelinha ou box. |
| 2.1 Ea vs ΔG | OK | 9–10 | Diagrama de morro/vale é literalmente o que precisa. Box "ΔG ≠ Ea" no momento exato. |
| 2.2 Pauling | OK | 11–12 | "Frase mais valiosa do capítulo" é metalinguagem que ajuda. ES vs ES‡ explicado. |
| 2.3 seis mecanismos | **[STOP: pág 13]** | 13 | Figura "Mecanismos Catalíticos" é só uma lista numerada de 1 a 6 em fonte serifada grande, sem ícones, sem mecanismo visual. **Carrega zero informação além do que o parágrafo já diz** — ocupa metade da página e cria sensação de vazio. Eu-aluno acha que perdeu uma figura "real" e procura nas páginas seguintes. |
| 3.1 hipérbole MM | OK | 16–17 | Justificativa cinética do formato hiperbólico (1ª ordem → ordem zero) está clara. |
| 3.2 KM | OK | 18 | Box "KM alto = afinidade BAIXA" no lugar certo. Hexoquinase vs glicoquinase já antecipa Carboidratos. |
| 3.3 kcat e LB | **[STOP: pág 19]** | 19 | Página com 567 palavras (densidade pico do documento; média do PDF é 277). Três fórmulas novas (kcat = Vmax/[E]t; kcat/KM; LB linearizado) em sequência, sem respiro entre elas. Aluno em dificuldade trava. |
| Conclusão integradora | OK | 22 | Faz o trabalho de fechamento + gancho para Enzimas II. |
| Resumindo (2 págs) | OK | 23–24 | Multi-coluna; densidade alta mas legível porque cada seção é fechada. |
| Etapa 2 | OK | 25–39 | Questões bem construídas. Detalhes em §3 abaixo. |
| Etapa 3 | OK | 40–42 | Modelos de resposta com mecanismo. |
| Gabarito | **[STOP: pág 43]** | 43 | **Bug visual e estrutural.** Header da página diz "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" mas o conteúdo é o gabarito da Etapa 2; e Etapa 4 foi removida do canônico em 2026-05-22. Layout do gabarito em 5 colunas está embaralhado (Q11 na col-3, Q12-Q13 na col-4/5 mas Q16-Q17 voltam ao layout esperado). Numeração da página marca "45" mas é a 43ª folha. |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria-chave:** 3.1 "Desfazer confusão comum (Enzimas I)" — o próprio EXEMPLARES já cita esta autora como referência.

**Parágrafo HISTÓRICO (esta apostila), p.3 abertura:**
> "Comece pelo que enzima resolve. Uma reação química tem um número intrínseco: a velocidade na qual ela acontece em condições 'normais' — sem ajuda externa, em pH e temperatura fisiológicos. Para muitas reações relevantes para a vida, essa velocidade é desesperadoramente lenta. A descarboxilação de uma fosfomonoester, por exemplo, levaria centenas de milhões de anos…"

**Parágrafo EXEMPLAR (Marisa Helena, EXEMPLARES 3.1):**
> "Antes de qualquer coisa, precisamos desfazer uma confusão comum. Muitas pessoas pensam que «enzima faz reação acontecer». **Isso está errado.** Uma enzima não transforma uma reação impossível em possível — ela só torna uma reação que *já é termodinamicamente favorável* muito mais **rápida**."

**Diagnóstico:** o histórico abre pela **escala do problema** (10⁸ anos vs ms), o exemplar abre **desfazendo o erro mental**. Ambos válidos, mas a abertura por erro-mental engaja metacognição imediata ("ah, eu achava errado"); a abertura por escala exige que o aluno já se importe com a pergunta. **O histórico só nega o erro na p.4 (box "Enzima não muda K, só k"), 1.5 página depois.** Sugestão para REDATOR-E1 NEBLI: quando há confusão sistemática conhecida (e enzima como "motor mágico" é o caso paradigmático), abrir desfazendo o erro mental **antes** da escala numérica.

**Veredito:** histórico é bom, mas o exemplar Marisa Helena é melhor — e esta apostila histórica não usa o próprio padrão consagrado da autora.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo fraco 1 — Tabela EC + nomenclatura (p.4)

**Citação literal:**
> "Como existem milhares de enzimas no corpo, a comunidade científica criou um sistema de nomenclatura: a Comissão de Enzimas¹ organiza tudo em seis classes pela natureza da reação. Oxirredutases (transferem elétrons, ex: lactato desidrogenase), transferases (transferem grupos, ex: hexoquinase), hidrolases (quebram com água, ex: tripsina), liases (rompem ligação sem hidrólise nem oxidação, ex: aldolase), isomerases (rearranjam, ex: triose-fosfato isomerase) e ligases (ligam usando ATP, ex: DNA ligase)."

**Diagnóstico mecanístico:** seis classes EC despejadas em parágrafo único com exemplos que o aluno não conhece. "Lactato desidrogenase" é referência circular — eu-aluno não sei o que é desidrogenase. Sem ancoragem do tipo "(você vai ver glicolise/Krebs)", a lista é decorativa.

**Reescrita pronta:**
> "Há milhares de enzimas no corpo, e a Comissão Internacional¹ as organiza em seis classes pela química que fazem — vale você ter um mapa mental delas, não decorar agora. **Oxirredutases** movem elétrons (são as desidrogenases que você vai conhecer em Glicólise e Krebs); **transferases** movem um grupo químico de uma molécula para outra (hexoquinase transfere fosfato do ATP para glicose — primeiro passo da glicólise); **hidrolases** quebram ligações usando água (a tripsina do seu duodeno é uma — hidrolisa proteínas da comida); **liases** rompem ligações sem usar água (aldolase, em Glicólise); **isomerases** rearranjam átomos dentro da mesma molécula (sem perder ou ganhar nada); **ligases** unem moléculas usando ATP (DNA ligase costura DNA). Cada vez que aparecer um 'nome-ase' em outro tema, volte aqui e classifique — em três semanas você não precisa mais."

### Parágrafo fraco 2 — Lista de vitaminas B (p.7)

**Citação literal:**
> "NAD⁺/NADH, FAD/FADH₂, CoA, biotina, piridoxal-fosfato (PLP), tiamina-pirofosfato (TPP) são coenzimas clássicas. A maioria deriva de vitaminas — daí o caráter essencial dessas vitaminas na dieta. NAD⁺ vem de B3 (niacina), FAD de B2 (riboflavina), CoA de B5 (ácido pantotênico), PLP de B6, TPP de B1 (tiamina), biotina de B7."

**Diagnóstico mecanístico:** seis pares vitamina→coenzima jogados em duas frases, sem âncora visual. O aluno fecha o PDF achando que precisa decorar tabela. Carga cognitiva pico sem mitigação.

**Reescrita pronta:** transformar em micro-tabela (caso (a) da § Bullets e tabelas do CLAUDE.md — comparativo com 3+ dimensões: vitamina, nome popular, coenzima, função-uma-frase). Header navy. Ex.:

| Vitamina | Nome | Coenzima | O que faz |
|---|---|---|---|
| B1 | tiamina | TPP | descarboxilações oxidativas (Krebs) |
| B2 | riboflavina | FAD/FADH₂ | aceptor de elétrons (cadeia respiratória) |
| B3 | niacina | NAD⁺/NADH | aceptor de elétrons (metabolismo oxidativo) |
| B5 | ácido pantotênico | CoA | transporta grupos acila |
| B6 | piridoxal | PLP | reações de aminoácidos |
| B7 | biotina | biotina | carboxilação (gliconeogênese) |

A tabela troca decoreba por mapa: o aluno passa a olhar a vitamina pela função quando aparecer em outro tema.

### Parágrafo fraco 3 — Densidade pico da página 19 (kcat, kcat/KM, LB)

**Citação literal (trecho da p.19):**
> "Combinando os dois parâmetros, surge a constante mais importante da enzimologia comparativa: a eficiência catalítica kcat/KM. Ela mede a velocidade da enzima em [S] baixo (regime de primeira ordem): V0 ≈ (kcat/KM) · [E]t · [S], em [S] << KM. (…) Lineweaver e Burk (1934) tiveram a ideia de inverter a equação: 1/V0 = (KM/Vmax) · (1/[S]) + 1/Vmax."

**Diagnóstico mecanístico:** três conceitos novos não-triviais empilhados em uma única página de 567 palavras (média do PDF é 277). kcat sai → imediatamente vira kcat/KM (com nova fórmula assintótica) → imediatamente vira LB linearizado (terceira fórmula). Sem respiro entre elas, sem mini-resumo, sem figura intermediária. Aluno em dificuldade chega a kcat/KM, perde o fio, e quando bate em LB já não está absorvendo.

**Reescrita pronta:** quebrar em duas páginas. Página A: só kcat (definição, unidade, comparação com Vmax — analogia "torneiras"). Página B: kcat/KM + teto difusional + Lineweaver–Burk. Inserir mini-resumo de 2 frases ao final de cada bloco antes de avançar (padrão "Resumindo até aqui" que a apostila já usa em outros lugares — não usar aqui é incoerência interna).

---

## 4. T3.3 — 3 seções mais densas

| Seção | Métrica | Pág(s) | Mitigação concreta |
|---|---|---|---|
| **3.3 kcat / kcat/KM / LB** | 567 palavras numa página + 3 fórmulas novas | 19 | Quebrar em 2 páginas (ver §3 acima). |
| **1.3 Cofatores + coenzimas + vitaminas B + grupo prostético + pelagra** | 4 conceitos novos + 6 vitaminas + caso clínico, em 2 páginas | 7–8 | Tabela de vitaminas (ver §3) + isolar pelagra em box `.clinica-box` separado. |
| **2.3 Seis mecanismos catalíticos** | 6 mecanismos em prosa contínua + figura inútil | 13–15 | Substituir figura "lista numerada" por figura mecanística real (ex.: histidina pegando próton + serina atacando carbonila + Zn²⁺ polarizando H₂O — 3 painéis). |

---

## 5. T3.4 — Voz fora do padrão NEBLI

A apostila tem voz **muito boa** na maior parte — diálogo, segundo-tom, mecanismo antes do nome. Mas alguns momentos quebram:

- **p.4:** "O sistema EC é Class.Subclass.SubSubClass.Serial — por exemplo, EC 3.4.17.1 é a carboxipeptidase A: classe 3 (hidrolase), subclasse 4 (atua em ligação peptídica), sub-subclasse 17 (metalocarboxipeptidase), série 1 (primeira catalogada)." — voz de manual técnico. O aluno não precisa decorar EC 3.4.17.1; precisa entender que **existe** um código hierárquico. Cortar o exemplo numérico ou movê-lo para footnote.
- **p.13:** "A bioquímica catalogou seis mecanismos básicos, e quase toda enzima usa combinação de dois ou três deles." — bom. Mas a transição para a lista é seca: "Catálise ácido-base. O sítio ativo tem um resíduo com pKa próximo de 7…". Faltou ponte ("Vamos ver os seis — pense em cada um como uma ferramenta no kit do sítio.").

Voz no resto está em padrão NEBLI; apenas pontos cirúrgicos quebram.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** **página 19** (3.3 — kcat + kcat/KM + LB), com 567 palavras, três fórmulas inéditas, zero figura nova, zero mini-resumo.

**3 mitigações:**
1. **Quebrar em duas páginas** com mini-resumo intermediário (descrita em §3).
2. **Reordenar:** apresentar kcat/KM ANTES do LB. Atualmente kcat → kcat/KM → LB, mas LB introduz uma terceira manipulação algébrica que distrai do insight de kcat/KM (eficiência em [S] baixo, teto difusional). Separar: kcat e kcat/KM são **significado**; LB é **técnica experimental** — mereciam blocos didáticos distintos.
3. **Figura mecanística para kcat/KM:** dois cenários lado a lado — enzima cataliticamente perfeita (cada colisão = reação) vs enzima medíocre (muitas colisões, poucas reações). O número 10⁹ M⁻¹s⁻¹ ganha gesto físico.

**Qual escolher:** **mitigação 1** (quebrar em duas páginas), porque é a única que resolve a densidade de fato — 2 e 3 melhoram pedagogia mas não reduzem palavras/página. Em segundo lugar, 3 (figura mecanística) — barato e de alto retorno.

---

## 7. T3.8 — ANÁLISE VISUAL (do PDF)

1. **Hierarquia tipográfica:** consistente em todo o PDF. Títulos navy bold (Montserrat), corpo Merriweather, mini-resumos em box verde-claro com barra navy. Header NEBLI fininho discreto. **OK**, mas dois deslizes: (a) sumário (p.2) usa hierarquia 3-níveis bem (ETAPA → PARTE → subtópico); (b) header da p.43 diz "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" mas o conteúdo é gabarito da Etapa 2 — **bug de header** (provavelmente legado do template antigo que ainda incluía Etapa 4 antes da remoção canônica 2026-05-22).

2. **Valor pedagógico das figuras:**
   - **p.4 (figura "Enzimas"):** tabela horizontal de 6 classes EC + figura/esquema lateral. No render aparece comprimida; conteúdo é referência seca (nomes-ase + exemplos). **Decorativa-tabular** — pouco valor mecanístico.
   - **p.5 (figura sítio ativo + nomenclatura "Carboxipeptidase A"):** texto colorido em vermelho/azul para destacar EC e nome sistemático — **bom contraste** com legenda separada explicando estrutura hierárquica EC. Útil.
   - **p.13 ("Mecanismos Catalíticos" — lista 1 a 6 numerada):** **figura SEM valor pedagógico**. Repete em fonte grande exatamente o que o texto adjacente diz. Aluno espera diagrama mecanístico (próton transferindo de His, intermediário covalente Ser, Zn polarizando H₂O); recebe lista numerada decorativa. Ocupa ~40% da página com zero ganho.
   - **Etapa 1 conjunta:** o PDF teve 16 figuras nas primeiras 21 páginas (cada subtópico tem 1), depois zero entre p.22 e p.43 (questões + gabarito). Esperado, mas notar: nas questões discursivas (p.40–42), uma figura de diagrama de energia ou hipérbole MM ajudaria modelo de resposta.

3. **Densidade visual / respiro:**
   - **p.4:** muro de texto com tabela. Sem respiro.
   - **p.13:** respiro **excessivo** ao redor da figura inútil (vazio embaixo da lista de mecanismos até o próximo texto).
   - **p.19:** muro denso (567 palavras + fórmulas) sem nenhum elemento visual. **Pico de densidade** do documento.
   - **p.43:** layout do gabarito desorganizado — 5 colunas com itens fora de ordem (Q01–Q05 col1–5 OK; Q06–Q08 col1–3; Q11 aparece sozinha na col3 da linha 2 de Integração com Q09–Q10 antes; Q15 EECC ao lado de Q16 E mas com Q19/Q20 numa terceira linha que mistura ordens). Difícil de usar como conferência rápida.

4. **Uso de cor:**
   - Navy (#1a3a5c-ish) para títulos, faixas, bordas de box. Box "Resumindo até aqui" verde-claro com barra navy. Box atenção em creme/âmbar. Boxes clínica em outro tom (pelagra p.7). **Consistente e propositada.**
   - p.5 vermelho/azul para destacar nomes-EC: efetivo.
   - Nenhuma cor inconsistente identificada.

5. **Cortes / overflow:**
   - **p.4 render** aparece comprimido com tabela apertada — possível overflow horizontal da tabela EC. Confirmar no PDF original.
   - **p.43 (gabarito):** layout de colunas claramente bagunçado — cells "escaparam" do grid esperado. Bug de Typst no template do gabarito.
   - Sem cortes verticais de texto detectados nos samples.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F do REDATOR-E1)

### Técnica 1 — Box "Erro do aluno" no momento exato

**Citação literal (p.18):**
> "**K_M alto = afinidade BAIXA** — Inversão clássica da P2. KM alto significa que a enzima precisa de mais substrato para chegar a Vmax/2. Mais substrato = enzima 'menos atraída' = afinidade menor. Pensar: KM alto = enzima 'exigente'. Mneumônico: KM e afinidade são inversamente proporcionais."

**Nome da técnica:** *Box de inversão clássica imediatamente após a definição operacional.*

**Quando NEBLI deveria usar:** sempre que existir uma medida cuja **direção semântica é contra-intuitiva** (KM alto = afinidade baixa; entropia alta = desordem alta mas energia livre baixa; afinidade da hemoglobina varia inversamente com P50; resistência elétrica = inverso de condutância em axônios). REDATOR-E1: definir → ancorar 1 cálculo → **box-erro** com mnemônico + ponteiro para "isso cai em P2". A apostila histórica faz isso em 3 momentos (K vs k, ΔG vs Ea, KM vs afinidade), todos no momento certo.

### Técnica 2 — Antecipação cruzada de tema futuro com par cinético

**Citação literal (p.18):**
> "Exemplo clássico que vai voltar muito: hexoquinase (no tecido periférico) tem KM para glicose ≈ 0,1 mM, glicoquinase (no fígado) tem KM ≈ 10 mM. Em [S] = 5 mM (glicemia de jejum), hexoquinase está praticamente saturada (50× KM); glicoquinase opera em meia-saturação. (…) Vai voltar em Carboidratos, Glicólise e Gliconeogênese."

**Nome da técnica:** *Par cinético-fisiológico como ponte para temas futuros.*

**Quando NEBLI deveria usar:** quando dois parâmetros do tema **só fazem sentido juntos como divisão fisiológica de trabalho**. A apostila não trata isoformas como curiosidade — trata como par funcional com glicemia de jejum ancorada. REDATOR-E1: ao introduzir KM, MM, isoformas, sempre fechar com par hexoquinase/glicoquinase (ou análogo do tema: GLUT1/GLUT4, miosina rápida/lenta, hemoglobina/mioglobina). A primeira aparição já planta a semente que será colhida em 3 resumos depois.

### Técnica 3 — Box clínico isolado dentro do bloco bioquímico

**Citação literal (p.7–8):**
> "**Pelagra: deficiência de B3 quebra o ciclo NAD/NADH** — Niacina (B3) é precursora de NAD⁺. Em dieta deficiente (clássica no Brasil rural histórico — milho como base alimentar sem nixtamalização), a célula não consegue manter as concentrações de NAD⁺/NADH adequadas. A maioria das oxirredutases para de funcionar. Manifestação clínica é dramática: as quatro D — dermatite, diarreia, demência e morte. Trata-se com nicotinamida oral. Doença evitável que matou milhões no século XX."

**Nome da técnica:** *Caso clínico curto com mecanismo + escala histórica + tratamento.*

**Quando NEBLI deveria usar:** sempre que um cofator/coenzima tem doença carencial conhecida. Não é "curiosidade" — é gancho que faz a coenzima passar de abstração ("NAD" = letras) para entidade biológica viva ("sem isso a pessoa morre demente"). Padrão: **3 frases**: (1) mecanismo da deficiência, (2) manifestação clínica (com mnemônico se houver — 4Ds aqui), (3) escala + tratamento. Aplicar em B1 (beribéri), B7 (deficiência de biotina por claras cruas), Fe (anemia), Zn (acrodermatite), B12 (anemia megaloblástica + cordão posterior).

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro NEBLI | Status nesta apostila | Observação |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **AUSENTE (bom!)** | Q26–Q30 com distratoras LONGAS (30–55 palavras), correta também longa. Q28 (glicoquinase em diabético) tem 5 alternativas no padrão "muita palavra cada", paridade visual preservada. Q30 idem. **Esta apostila acerta o que o NEBLI erra cronicamente.** |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PRESENTE (parcial)** | Há footnotes para apoenzima⁵, holoenzima⁶, coenzima⁷, NAD⁸, FAD⁹, CoA¹⁰, PLP¹¹, TPP¹², grupo prostético¹³ — boa cobertura. Mas: ATP aparece (p.4 "ligases que ligam usando ATP"; p.10 "hidrólise de ATP") sem footnote. ADP, G6P, NADH (no boxe pelagra), Pi não declarados. Lista alvo do NEBLI: ATP, ADP, Pi, NADH em particular. |
| 3 | Subagentes Opus contaminados | N/A | Não testável a partir do PDF. |
| 4 | Heredoc ENAMETOOLONG | N/A | Idem. |
| 5 | `questao-ce` tupla vs lista | **AUSENTE (bom)** | Itens CE (Q15, Q18, Q22, Q23) renderizam corretamente como I/II/III/IV — implementação correta. |
| 6 | Termo-notas abaixo do alvo (alvo 6–8) | **AUSENTE (excede!)** | Conto 13 footnotes nominais no corpo (Comissão de Enzimas, chave-fechadura, ajuste induzido, estereoespecífica, apoenzima, holoenzima, coenzima, NAD, FAD, CoA, PLP, TPP, grupo prostético, estado de transição, energia de ativação, Vmax, kcat). **Bem acima do alvo NEBLI.** |
| 7 | Tema-card teto E1 errado (canônico 22) | N/A direto, mas E1 fechou em ~22 páginas (p.3 a p.22 — 20 páginas de E1 + Resumindo p.23–24). **Dentro do canônico.** |

**Síntese:** a apostila histórica de Marisa Helena acerta justamente os 3 erros mais recorrentes do NEBLI (paridade distratoras, termo-notas no alvo, teto E1). Confirma o status dela como referência positiva. Único ponto fraco no checklist: ATP/ADP/Pi/NADH sem `#sigla()` próprio.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Corrigir header da p.43:** "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" → "GABARITO — ETAPA 2". Etapa 4 não existe mais no canônico (2026-05-22).
2. **Corrigir layout do gabarito (p.43):** 5 colunas com cells fora de ordem. Reorganizar como grid 4-colunas alinhado por categoria, ou lista vertical limpa.
3. **Quebrar página 19 em duas:** kcat numa, kcat/KM + LB na outra. Densidade atual (567 palavras + 3 fórmulas novas) é o pico do documento e ponto de abandono.

### MECANÍSTICO (max 3)
1. **Substituir figura "Mecanismos Catalíticos" (p.13)** por figura real de 3 painéis: His pegando próton (ácido-base), Ser195 atacando carbonila (covalente), Zn²⁺ polarizando H₂O (metal). A figura atual é decorativa-lista — perdeu a chance pedagógica.
2. **Adicionar `#sigla()` para ATP, ADP, Pi, NADH** na 1ª aparição (atualmente referenciadas mas sem footnote-glossário).
3. **Reescrever parágrafo das classes EC (p.4)** com ancoragem futura: cada classe + "(você vai ver em [tema])". Versão atual lista 6 nomes-ase sem caminho de retorno.

### DIDÁTICO (max 3)
1. **Transformar lista vitaminas B → coenzimas (p.7) em tabela** (caso (a) do CLAUDE.md: comparativo 3+ dimensões). Atual: 6 mapeamentos em 2 frases de prosa.
2. **Abrir 1.1 desfazendo erro mental** ("enzima não faz reação acontecer; só acelera") **antes** da escala numérica (10⁸ anos vs ms). Padrão Marisa Helena cat. 3.1 do EXEMPLARES — a própria autora usa em outra versão.
3. **Inserir "Resumindo até aqui" entre kcat e kcat/KM**, e entre kcat/KM e LB — a apostila usa esse padrão em outros lugares e o omite justo onde mais precisa.

### ESTÉTICO (max 3)
1. **Mover exemplo numérico "EC 3.4.17.1 = carboxipeptidase A"** da p.4 para footnote ou box lateral. Aluno não precisa do código; precisa entender que existe.
2. **Comprimir tabela "Enzimas" (p.4)** ou expandir para ocupar largura útil — render mostra tabela apertada.
3. **Adicionar uma figura discreta no início da Etapa 3 (p.40)** — hipérbole MM já vista, repetida em pequeno como "lembrete visual" antes das discursivas que pedem mecanismo MM.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM.** A apostila acerta paridade-de-distratoras, termo-notas, voz dialogada com mecanismo-antes-de-nome, boxes "erro do aluno" no momento certo, antecipação cruzada de temas, e caso clínico breve com mecanismo (pelagra). É referência viva para o REDATOR-E1.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM** — 3 estruturais (header bug p.43, gabarito desorganizado, densidade pico p.19) + 3 mecanísticas (figura inútil p.13, siglas ATP/ADP/Pi/NADH, classes EC sem ancoragem).
3. **Seção para refazer integral?** **Página 19 (3.3)** — quebrar em duas páginas com mini-resumo intermediário. Nenhuma outra seção exige refatoração integral.
4. **Parágrafos para reescrever (lista):**
   - p.4: parágrafo das classes EC (reescrita pronta em §3).
   - p.7: lista vitaminas B → tabela (modelo em §3).
   - p.13: prosa + figura "lista de mecanismos" → figura mecanística + texto (§4 Mecanístico item 1).
   - p.19: bloco kcat / kcat/KM / LB → quebrar em duas páginas (§3).
   - p.43: header + grid do gabarito → correção estrutural.

---

[APROVAR COM RESERVAS]

Aprovado como referência positiva (técnicas T3.9 #1–3 vão direto para REDATOR-E1); reservas correspondem aos 3 estruturais + 3 mecanísticos da §10. Reservas são pontuais e não-bloqueantes para uso como exemplar de voz e estrutura geral.
