# Revisão profunda Tier 3 — UC01-BIOQ-05-proteinas-i

**Tema (ancoragem):** Proteínas I — da ligação peptídica aos 4 níveis hierárquicos, com o efeito hidrofóbico como motor termodinâmico do enovelamento.
**Autor:** Fred (apostila histórica, fora do pipeline NEBLI)
**Personagem:** aluno FMUSP 1º ano, dificuldade real, ensino médio + meses de medicina, não sabe procurar pré-requisito por fora.
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

### Ancoragem (3 conceitos que aluno quer aprender, 2 vizinhos NÃO-tema)
- Quero aprender: (1) o que é exatamente um "nível" hierárquico e por que são quatro; (2) o que é efeito hidrofóbico (sem decorar a palavra); (3) por que a sequência sozinha basta para definir a forma.
- NÃO é tema aqui: enovelamento patológico/chaperonas em detalhe (Proteínas II), cinética enzimática.

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão mecanística da parada (se houver) |
|---|---|---|---|
| Capa + sumário | OK | 1–2 | Capa limpa, "70% do tema" já vende a tese central. |
| Intro E1 (3 camadas) | OK | 3 | Boa promessa do arco; sigla φ/ψ aparece no sumário antes de explicada (cosmético). |
| 1.1 Ligação peptídica | OK | 3–4 | "Resíduo" introduzido com mecanismo (perdeu OH+H) — modelo de definição just-in-time. |
| 1.2 φ/ψ | **[STOP: pág 4]** | 4 | Símbolos φ/ψ aparecem no corpo, mas o texto descreve "ângulo entre Cα e N" — o aluno-alvo não sabe ler letra grega num parágrafo de prosa contínua. Sem termo-nota nem figura legendada com seta para φ e ψ, o aluno fecha o PDF. |
| 1.3 Anfinsen | OK | 5–6 | Fechamento elegante com AlphaFold. |
| 2.1 Não-covalentes | OK | 7–8 | Caixa "Ponte salina ≠ ligação peptídica" é exemplar. |
| 2.2 Efeito hidrofóbico | OK (excelente) | 9–10 | "O nome é traiçoeiro" + analogia óleo/vinagrete + topologia invertida nas proteínas de membrana. Pico de qualidade do PDF. |
| 2.3 Ponte dissulfeto | OK | 11–12 | Oxitocina/vasopressina como exemplo de "9 resíduos, anel, função distinta". |
| 3.1 α-hélice/folha-β | **[STOP: pág 13–14]** | 13–14 | Densidade de números (3,6 res/volta, 100°, n+4) chega antes da figura ser bem legendada; figuras da pág 14 vêm com legenda muito pequena (ver T3.8). Aluno em dificuldade não consegue separar "paralela vs antiparalela" só da prosa. |
| 3.2 Terciária/domínios | OK | 15–16 | Boa transição "secundária = esqueleto / terciária = Rs". |
| 3.3 Quaternária | OK | 17–18 | Box anemia falciforme excelente — uma frase, mecanismo completo. |
| Conclusão integradora | OK | 20 | Releitura compacta do arco. |
| Resumindo (2 col) | **[STOP: pág 21]** | 21 | Quebra de palavras agressiva: "satisfação→satura-/ção", "secre-/tadas", "Anfin-/sen". Layout aperta o respiro e aluno cansado pula. Conteúdo está certo, forma trai a função. |
| E2 Q01–Q30 | OK em geral | 22–37 | Ver T3.10 e §10 para problemas pontuais (paridade, "Aplicação"). |
| E3 Q1–Q5 | OK | 38–40 | Modelos de resposta são exemplares. |
| Gabarito final | **[STOP: pág 41]** | 41 | Header da página diz "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" mas conteúdo é o gabarito; e o footer numera "44" enquanto o PDF tem 41 páginas. Bug estrutural visível. Também: categoria "INTEGRAÇÃO (Q11–Q25)" no gabarito mas Q09 e Q10 estão sob "CONSOLIDAÇÃO" no corpo — conferir mais abaixo. |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria pivô:** CAT 2 (origem/pergunta motivadora) e CAT 7 (analogia construtiva).

**Parágrafo do PDF (pág 9, efeito hidrofóbico):**
> "Mas o que é 'efeito hidrofóbico'? Note que o nome é traiçoeiro: ele sugere que átomos hidrofóbicos se atraem, como se houvesse uma 'força hidrofóbica' entre eles. Isso é só meia verdade. A verdade completa é a seguinte: cadeias laterais hidrofóbicas (R apolares de Val, Leu, Ile, Phe, Trp, Met) não conseguem fazer ligações de hidrogênio com a água. [...] Essa gaiola tem entropia muito baixa — as águas perdem liberdade."

**Exemplar 3.1 (EXEMPLARES.md — "Enzimas não fazem reação acontecer"):** abre desfazendo confusão direta com o aluno, depois constrói. O PDF de Fred usa o mesmo padrão ("o nome é traiçoeiro" → "só meia verdade" → mecanismo). **Equivalência:** Fred está na altura do exemplar canônico NEBLI. Esse parágrafo deve entrar como exemplar candidato para CAT 3 (desfazer confusão comum) — anotar.

**Contraste negativo (mesmo PDF, pág 4):**
> "Os ângulos dessas duas rotações têm nomes próprios: o ângulo entre Cα e N chama-se φ (phi); o ângulo entre Cα e C chama-se ψ (psi)."

Comparar com **Exemplar 7.1** (lápis dobrado e estado de transição) que sempre apresenta gesto físico antes do nome. Aqui Fred pula o gesto físico (poderia ser "imagine girar o pulso aqui e o cotovelo ali") e dá os nomes imediatamente. O aluno-alvo decora φ e ψ sem internalizar o gesto rotacional.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Fraco 1 — pág 4, definição de φ/ψ
- **Citação:** "Os ângulos dessas duas rotações têm nomes próprios: o ângulo entre Cα e N chama-se φ (phi); o ângulo entre Cα e C chama-se ψ (psi)."
- **Diagnóstico:** definição puramente verbal de dois ângulos que o aluno nunca viu. Sem analogia cinestésica (girar pulso/cotovelo), sem termo-nota, e a figura adjacente tem legenda pequena que apenas repeteo texto. Aluno em dificuldade memoriza "phi-psi" como pó de pirlimpimpim.
- **Reescrita:**
> "Imagine que cada Cα da cadeia é uma articulação. Saindo dele para trás (em direção ao N), há uma ligação que pode girar — esse giro recebe o nome de **φ (phi)**. Saindo dele para frente (em direção ao C carbonílico), há outra que também gira — esse giro é **ψ (psi)**. A ligação peptídica que vem depois é a única que NÃO gira (lembre 1.1). Então, em cada resíduo, o esqueleto tem exatamente dois 'pulsos rotativos' (φ e ψ); o terceiro ponto, a peptídica, está travado. Fixar o par (φ, ψ) de cada resíduo é, literalmente, escolher a forma final da proteína."

### Fraco 2 — pág 13, geometria da α-hélice
- **Citação:** "A α-hélice é um enrolamento da cadeia em hélice destra (gira para a direita). Os números marcantes: 3,6 resíduos por volta de hélice, com ângulo de 100° entre resíduos consecutivos. As ligações de hidrogênio acontecem entre o C=O do resíduo n e o N-H do resíduo n+4..."
- **Diagnóstico:** seis números densos (3,6 / 100° / n / n+4) em duas frases, sem o aluno ter sequer visualizado a forma. "n+4" sai antes de o aluno ter ancorado o que é "n". A figura da pág 14 vem depois, pequena, sem destaque visual da ligação H entre n e n+4.
- **Reescrita (dialogada):**
> "Imagine um saca-rolhas. A cadeia, ao formar α-hélice, se enrola exatamente assim — um espiral que avança para a direita (destrógiro). Numere os resíduos: 1, 2, 3, 4, 5... O fato curioso é que, ao dar uma volta completa do saca-rolhas, você passou por 3,6 resíduos — não 4 redondos. Por causa disso, o resíduo número 1 fica diretamente acima do número 5 no espaço (4 posições depois). E é justamente aí que aparece a ligação de hidrogênio: o C=O do resíduo 1 'estende a mão' verticalmente para baixo, encontra o N-H do resíduo 5, e a hélice se trava com essas pontes verticais. Em linguagem técnica: a ligação H acontece entre **n e n+4**, paralela ao eixo da hélice. Os grupos R, por sua vez, ficam apontando para fora do espiral — eles não participam dessa costura."

### Fraco 3 — pág 21, Resumindo aglomerado
- **Citação (transcrição literal do .txt como o aluno vê no PDF):** "Liga-/ções de hidrogênio ( 20 kJ/mol), pontes sali-/nas entre Rs de carga oposta (Lys/Arg/His com Asp/Glu), forças de Van der Waals entre dipolos momen-/tâneos ( 1 kJ/mol, mas valem pela quantidade)."
- **Diagnóstico:** quebras de palavra agressivas + ausência do símbolo `≈` antes de "20 kJ/mol" (perdido na transcrição/render). Resumindo vira muralha. Quatro forças citadas em uma só frase sem hierarquia visual.
- **Reescrita:** quebrar em 2 mini-blocos no Resumindo: **"Forças não-covalentes (fracas, somam-se)"** com bullets numéricos limpos (~20 / ~1 / variável), e **"Uma covalente: dissulfeto (~250 kJ/mol)"** isolada para contraste. Forçar hifenização Typst com `set par(justify: true, linebreaks: "optimized")` ou reduzir para `linebreaks: "simple"` se necessário.

---

## 4. T3.3 — 3 seções mais densas

| Seção | Sintoma | Mitigação concreta |
|---|---|---|
| 1.2 φ/ψ + Ramachandran (pág 4–5) | 3 conceitos novos sem ancoragem cinestésica (eixos rotativos + diagrama 2D + impedimento estérico). | Inserir analogia "pulsos rotativos" antes do nome φ/ψ; usar termo-nota; o diagrama de Ramachandran precisa de mini-callout com "regiões vermelhas = colisão de átomos, não 'energia ruim' abstrata". |
| 3.1 α-hélice + folha-β paralela/antiparalela (pág 13–14) | 6 números + 2 padrões + variantes paralela/antiparalela em 2 páginas. | Quebrar em sub-bloco α-hélice (com saca-rolhas) e sub-bloco folha-β (com analogia "zíper de fitas"); contrastar paralela/antiparalela com mini-tabela de 2 linhas (alinhamento das ligações H). |
| Resumindo (pág 21) | 8 cápsulas em 2 colunas com hifenizações agressivas. | Reduzir para 6 cápsulas mais respiradas; alargar coluna ou aumentar leading; remover hifenização forçada para palavras-chave (Anfinsen, dissulfeto). |

---

## 5. T3.4 — Voz fora do padrão

Fred mantém voz dialogada estável. Pequenos desvios pontuais:

- Pág 9 (excelente): "Se você precisar guardar uma única ideia desta etapa, guarde esta..." — voz de monitor, perfeita.
- Pág 13: "Os números marcantes: 3,6 resíduos por volta..." — voz vira manual técnico. Quebra o registro.
- Pág 17: "A hemoglobina é o exemplo arquetípico. Ela é um tetrâmero..." — bom retorno ao registro dialogado.

**Nenhuma quebra grave** — voz dialogada cobre ≥85% do texto. Mas o slot 3.1 cai para registro de livro-texto justamente onde o aluno mais precisa de monitor.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** **3.1 estrutura secundária (α-hélice + folha-β + prolina-quebra)**, páginas 13–14. Densidade de números, dois padrões geométricos, exceções (prolina), e ausência de figura "explicada" — figuras existem mas a legenda repete o corpo em vez de complementar.

**3 mitigações:**
1. **Saca-rolhas e zíper** — analogias cinestésicas para α-hélice (saca-rolhas destrógiro) e folha-β (zíper de fitas paralelas/antiparalelas). Custa 6–8 linhas; rende compreensão.
2. **Mini-tabela paralela vs antiparalela** — 2 linhas × 3 colunas (sentido das fitas | geometria da lig. H | estabilidade relativa). Cabe em ~6cm de altura.
3. **Termo-nota em "n+4"** — explicar inline (`#termo-nota[n+4][quatro resíduos depois ao longo da cadeia — equivalente a uma volta completa do saca-rolhas]`) na 1ª aparição.

**Qual escolher:** **#1 (saca-rolhas/zíper) é a maior alavanca** — entrega o gesto físico que falta. NEBLI deveria adotar como template para qualquer estrutura periódica (hélices, folhas, anéis).

---

## 7. T3.8 — ANÁLISE VISUAL (do PDF)

### Hierarquia tipográfica
- **Capa (p.1):** excelente — faixa navy + Montserrat caixa-alta espaçada para "NEBLI · APOSTILA" + Merriweather bold gigante para "Proteínas I". Hierarquia clara.
- **Sumário (p.2):** funcional, mas PARTE I/II/III em teal sobre branco sem fundo, contraste apenas tonal. Aluno escaneando rápido perde a divisão.
- **Corpo (p.4, p.14, p.19):** Merriweather corpo + títulos seção em teal médio. Bom respiro entre parágrafos. **Mapa Conceitual III** (p.19) com 3 cards coloridos (azul/areia/rosa) é exemplar — instantâneo de leitura.

### Valor pedagógico das figuras
- **p.4 (ligação peptídica):** figura tem fórmula química com "H₂O" saindo, mas legenda em fonte minúscula (~7pt) cortando palavras. Decorativa-funcional, mas legenda mal explorada.
- **p.14 (α-hélice + folha-β):** **duas figuras coladas verticalmente, ambas pequenas, legendas em fonte muito reduzida.** A figura da folha-β mostra paralela e antiparalela lado a lado mas sem rótulo claro de "qual é qual". Valor pedagógico **abaixo do esperado**.
- **p.21 (Resumindo):** sem figuras. OK para um Resumindo, mas em página de revisão um único ícone/diagrama-síntese ajudaria.
- Total: **13 imagens no PDF**, com queda de densidade radical depois da pág 18 (página 19+ tem 0 imagens em 23 páginas seguidas — todo o material de questões fica sem qualquer suporte visual).

### Densidade visual (respiro vs muros)
- p.1, p.2, p.19: respiro ótimo.
- p.13–14: **muro de texto + figuras pequenas**. Quase 700 palavras combinadas com 2 imagens espremidas.
- p.21 (Resumindo): **muro de 2 colunas com hifenizações ruins** (ver §3, Fraco 3).

### Uso de cor
- **Coerente:** teal para títulos e barras, navy para capa, gold para boxes "Resumindo até aqui", âmbar para destaques. Box "Ponte salina ≠ ligação peptídica" usa cor diferente (azul-claro) — boa diferenciação para "atenção/erro comum".
- **Mapa Conceitual** com 3 cards coloridos (azul/areia/rosa) está dentro do padrão NEBLI. Cores têm propósito.

### Cortes/overflow
- **p.41 (gabarito):** header diz **"ETAPA 4 — QUESTÕES DE FUNDAMENTOS"** mas o conteúdo é o gabarito da Etapa 2. **Bug estrutural.** Além disso, o footer numera **"44"** mas o PDF tem **41 páginas** — descalibragem entre página lógica e física.
- **Gabarito Q09–Q10:** estão visualmente sob "CONSOLIDAÇÃO (Q01–Q10)" mas o corpo classifica Q09 e Q10 como **"Integração"** (pág 25–26 do .txt). Inconsistência entre rótulos das questões e o grupo do gabarito.
- Hifenização agressiva no Resumindo (pág 21) é o pior corte visível.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas — ALIMENTA Phase F do REDATOR-E1)

### Técnica 1 — "Desfazer confusão antes de definir" (pág 9, efeito hidrofóbico)
- **Citação:** "Mas o que é 'efeito hidrofóbico'? Note que o nome é traiçoeiro: ele sugere que átomos hidrofóbicos se atraem... Isso é só meia verdade. A verdade completa é a seguinte: [...] essa gaiola tem entropia muito baixa..."
- **Nome da técnica:** "abertura por desmonte da intuição errada plausível" (variante mais agressiva de CAT 3 do EXEMPLARES).
- **Quando NEBLI deveria usar:** sempre que o nome técnico do conceito **sugere mecanismo errado** — "efeito hidrofóbico" (sugere atração), "alta energia" do ATP (sugere reservatório), "transporte ativo" (sugere algo se mover), "potencial de ação" (sugere potencialidade, não evento). Gancho concreto para REDATOR-E1: incluir bloco **"Nome traiçoeiro?"** no Tema Card Seção B quando o termo central tem essa armadilha lexical.

### Técnica 2 — "Box-frase única para clínica de alto impacto" (pág 18, anemia falciforme)
- **Citação:** "Na anemia falciforme, uma mutação substitui o glutamato 6 da β-globina por uma valina. [...] Essa 'marca hidrofóbica' exposta na superfície faz com que múltiplas hemoglobinas mutantes se grudem umas nas outras quando desoxigenadas, formando longos polímeros que distorcem a hemácia em forma de foice..."
- **Nome da técnica:** "patologia em parágrafo único com cadeia causal completa" — mutação → mudança química do R → comportamento físico → patologia macroscópica → desfecho clínico, tudo em 6–8 frases.
- **Quando NEBLI deveria usar:** SEMPRE que o tema tem 1 patologia paradigmática — `.clinica-box` deve forçar a cadeia: mutação/lesão → mecanismo molecular → mecanismo celular → fenótipo macro → clínica. Modelo bate exemplar Q15 da CAT 11. Gancho: o REDATOR-E1 já tem `.clinica-box`, mas não tem checklist de "cadeia causal completa em 1 caixa". Adicionar ao redator-e1.md como **regra-clinica-box-causal**.

### Técnica 3 — "Aviso de antemão + promessa de % de domínio" (pág 3, intro)
- **Citação:** "Um aviso de antemão: o tema é cheio de vocabulário (α-hélice, folha-β, domínio, dímero, φ/ψ...), mas o mecanismo central é simples e elegante. Se você entender que cadeias laterais hidrofóbicas fogem da água como gotas de óleo em vinagrete, **já tem 70% do enovelamento na cabeça**."
- **Nome da técnica:** "promessa de Pareto" — declarar logo na intro qual é o "70% do tema" (uma frase mecanística única).
- **Quando NEBLI deveria usar:** **toda intro de E1** deve fechar com uma promessa do tipo "se você sair sabendo X, já tem Y% do tema". Reduz ansiedade do aluno-alvo (que entra achando que precisa decorar tudo) e dá uma âncora para retornar quando ele se perder. Gancho concreto para o Tema Card: Seção A passa a exigir um campo **"frase-Pareto 70%"** que o REDATOR-E1 deve plantar na intro literal.

---

## 9. T3.10 — 7 erros NEBLI (tabela de calibração)

| # | Erro NEBLI | Status no PDF Fred | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **PRESENTE (parcial)** | Q26 (correta E, 33 palavras de mecanismo) vs distratoras A/B/C/D entre 18–23 palavras. Ratio ~1.5. Q29 (correta D, 34 palavras) vs distratoras 14–22 palavras. Ratio ~1.55–2.4. Acima do teto 1.25. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PRESENTE (não detectável no .txt — só no rendering)** | O .txt mostra "PDB" recebendo footnote 4 (bom), "ADH" footnote 6 (bom). Mas siglas químicas (`-SH`, `-OH`, `-NH`, `-COOH`, `S-S`, `C=O`, `N-H`, `kJ/mol`) aparecem dezenas de vezes sem `#sigla()`. Aluno em dificuldade ainda assim entende pelo contexto químico — falso-positivo brando. |
| 3 | Subagente Opus contaminado | **N/A** | PDF histórico, sem subagente. |
| 4 | Heredoc ENAMETOOLONG | **N/A** | Não aplicável a PDFs históricos. |
| 5 | `questao-ce` exige tupla | **AUSENTE (PDF renderizou OK)** | Os blocos CE de Q03, Q06, Q09, Q11, Q12, Q25, Q27, Q28 renderizam normalmente — Fred já usa o formato certo. |
| 6 | Termo-notas abaixo do alvo (6–8) | **PRESENTE** | Footnotes contadas no .txt: `1diagrama de Ramachandran`, `2conformação nativa`, `3ponte salina`, `4PDB`, `5ponte dissulfeto`, `6ADH`, `7α-hélice`, `8domínios` — **8 termos-nota**. Está na faixa-alvo (6–8). **Erro AUSENTE.** |
| 7 | Teto E1 = 22 páginas | **PRESENTE (estouro)** | E1 vai de pág 3 a pág 20 → **18 páginas**. Dentro do teto canônico de 22. **Erro AUSENTE em termos quantitativos**, mas no limite superior — sugere oportunidade de revisão de densidade na seção 3.1. |

**Extra (não nos 7 canônicos):** **Bug estrutural de header "ETAPA 4 — QUESTÕES DE FUNDAMENTOS"** na página 41 (que é o gabarito) sugere que o template ainda carrega rótulo de Etapa 4 (removida do PDF canônico em 2026-05-22). Atualizar template para `Gabarito consolidado` no cabeçalho da última seção.

---

## 10. Recomendações por hierarquia (Inovação 4)

### ESTRUTURAL (max 3)
1. **Corrigir header "ETAPA 4" no gabarito (pág 41).** É lixo de versão pré-2026-05-22, quando Etapa 4 saiu do PDF canônico. Editar template `nebli_v2_apostila.typ` para que a última seção use `Gabarito consolidado` como running header.
2. **Reconciliar agrupamento Q01–Q10 (gabarito CONSOLIDAÇÃO) com classificação real (Q09–Q10 marcadas Integração no corpo).** Decidir: ou Q09–Q10 voltam para Consolidação no corpo, ou o gabarito as desloca para o bloco INTEGRAÇÃO. Hoje há inconsistência visível.
3. **Renumerar página 41 corretamente** (footer diz "44"). Sintoma de páginas-fantasma do template (resquício de Etapa 4 + Glossário siglas removidos).

### MECANÍSTICO (max 3)
1. **Reescrever 1.2 (φ/ψ) com analogia cinestésica antes do nome** (ver §3 Fraco 1).
2. **Reescrever 3.1 com saca-rolhas (α-hélice) e zíper (folha-β)** antes dos números (ver §3 Fraco 2 e §6).
3. **Engordar distratoras de Q26 e Q29** (Aplicação) com mecanismo plausível-mas-errado de 25–35 palavras cada — usar erro #1 do checklist como guia.

### DIDÁTICO (max 3)
1. **Adicionar termo-nota inline em "n+4" e "n+3"** na seção 3.1 — o aluno vê pela 1ª vez sem ancoragem.
2. **Quebrar Resumindo em 2 páginas** ou reduzir de 8 para 6 cápsulas, eliminando hifenizações agressivas. Davi já flexibilizou para 1–2 páginas em 2026-05-20; aproveitar.
3. **Mini-tabela paralela vs antiparalela** com 2 linhas × 3 colunas em 3.1 (caso (a) do CLAUDE.md — comparativo 3 dimensões).

### ESTÉTICO (max 3)
1. **Aumentar fonte das legendas das figuras** (especialmente p.4, p.14). Hoje ~7pt; alvo 9pt.
2. **Adicionar rótulos "Paralela" e "Antiparalela" diretamente sobre as duas sub-figuras** da folha-β (pág 14).
3. **Reforçar contraste do sumário (pág 2):** PARTE I/II/III em teal sobre fundo cinza-claro ou com underline médio para escaneamento rápido.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM, com reservas.** O PDF é didaticamente forte em 2.2 (efeito hidrofóbico), no box anemia falciforme (3.3) e na intro (3) — três passagens que devem entrar como exemplares candidatos no EXEMPLARES.md (técnicas 1, 2 e 3 do T3.9).
2. **≥1 problema ESTRUTURAL/MECANÍSTICO?** **SIM.** Bug do header "ETAPA 4" na pág 41 + inconsistência Q09–Q10 + erro #1 (paridade distratoras Aplicação) presentes. Bloqueiam aprovação irrestrita.
3. **Seção para refazer?** **Seção 3.1 (estrutura secundária — α-hélice e folha-β, pp.13–14).** Reescrever com analogias cinestésicas + mini-tabela paralela/antiparalela + termo-nota em n+4. Demais seções são editar-pontual, não refazer.
4. **Parágrafos para reescrever?** **3** (já redigidos em §3):
   - 1.2 — definição de φ/ψ (pág 4)
   - 3.1 — geometria da α-hélice (pág 13)
   - Resumindo — bloco "4 não-covalentes + 1 covalente" (pág 21)

---

[APROVAR COM RESERVAS]

<!-- FIM DA REVISÃO PROFUNDA -->
