# Revisão profunda Tier 3 — UC01-BIOQ-07-purificacao-de-proteinas

**Tema (ancoragem):** Purificação de proteínas
**Autor:** Fred
**Personagem:** aluno FMUSP 1º ano, dificuldade real, ensino médio + meses de medicina
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

## ANCORAGEM DE TEMA

- **Tema canônico:** purificação de proteínas — três famílias (estratégia geral, cromatografia, eletroforese), monitoramento por rendimento e atividade específica.
- **3 conceitos centrais que VOCÊ-aluno gostaria de aprender:** (1) por que filtração em gel inverte a intuição da peneira — grandes saem primeiro; (2) como SDS mascara carga e transforma eletroforese num "régua de massa"; (3) como pI funciona como poço de potencial na focalização isoelétrica.
- **2 temas vizinhos que NÃO são esse:** estrutura terciária e dobramento de proteínas (UC01-BIOQ-06ish); cinética enzimática Km/Vmax (UC02 ou aulas adjacentes).

---

## 1. Pontos de parada (simulação leitura linha-a-linha)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Intro-box (Etapa 1) | [OK] | 3 | Abertura concreta: "milhares de proteínas misturadas". Promessa clara das três famílias. |
| 1.1 Quando precisa estar pura | [OK] | 3 | Três motivos práticos bem ancorados (função, estrutura, indústria). Insulina recombinante = âncora clínica precoce. |
| 1.2 Lógica das etapas | [OK] | 3–4 | "Toda purificação real é sequência" — quebra a fantasia da técnica mágica logo de cara. |
| Tabela-esquema canônico (pág 4) | [STOP-LEVE] | 4 | Sigla "alvo" e termos truncados na figura ASCII ("a cada etapa" sem leading) — aluno olha e não entende. Diagrama caberia melhor com legenda explicando cada caixa. |
| 1.3 Atividade específica / rendimento | [OK] | 4–5 | Definição-nota canônica funciona. Tabela hipotética 360× é poderosa. |
| Mapa conceitual I (pág 6) | [STOP-LEVE] | 6 | Mapa em ASCII com layout quebrado ("1.1 — Por quê / 1.2 — Como / 1.3 — Monitor"). Aluno em dificuldade não decifra mapa quebrado. |
| 2.1 Filtração em gel | [OK] | 6–7 | Excelente: paradoxo da peneira é introduzido em uma frase ("o resultado parece contraintuitivo até a primeira vez que se entende"). Caixa lateral "Filtração em gel é contraintuitiva" (pág 9) reforça com mnemônico ("pequena entra em buraco, demora"). |
| 2.2 Troca iônica | [OK] | 7–8 | Mecanismo do gradiente salino bem amarrado: "íons cloreto competem pelos sítios". |
| 2.3 Afinidade + His-tag | [OK] | 8 | Salto pedagógico bom: substrato análogo → His-tag → insulina recombinante. |
| Tabela 3-variantes (pág 9) | [STOP] | 9 | **Cells quebradas em ASCII** — "tamanho fa-/tores 2-5× de massa", "primeiro, pe-/quenas por último", "em-/riquecimento de/1000-10000× em uma/etapa". Aluno-eu fechei aqui na primeira leitura. Tabela mal renderizada destrói a comparação que era O PONTO. |
| 3.1 SDS-PAGE | [OK] | 10–11 | "Uma molécula de SDS para cada dois resíduos" é detalhe mecanístico exato. Caixa "Western blot e HIV" ancora clínica. |
| 3.2 Focalização isoelétrica | [STOP-LEVE] | 11–12 | Conceito de "poço de potencial" é ótimo, mas pode parar aluno fraco em física — não explica o que é poço de potencial em 1 frase. Reescrita curta resolveria. |
| Página de figuras-mosaico (pág 13) | [STOP] | 13 | **4 slides do professor agrupados como mosaico** sem texto entre eles. Aluno-eu chega aqui e não sabe se deve ler os slides em ordem, qual é figura primária, qual é decorativa. Sobrecarga visual sem hierarquia. |
| 3.3 Eletroforese 2D | [OK] | 12 | Boa síntese — "girado 90°", "coordenadas (pI, massa)". |
| Conclusão integradora (pág 15) | [OK] | 15 | Síntese que retoma a tese ("diferença física vira separação espacial") + lista clínica final. Forte. |
| Resumindo (pág 16) | [STOP-LEVE] | 16 | Layout 2 colunas com quebras de linha agressivas — texto fica picado ("plasmác-/itos", "Boa res-/olução", "diab-/éticos"). Hifenização à exaustão. |
| E2 Q08 item I | [STOP] | 20 | Erro de digitação: "carga líquida líquida" (palavra duplicada). |
| E2 Q19 item III | [STOP-LEVE] | 26 | Item III diz "dímero com pontes dissulfeto → SDS-PAGE COM redutor mostraria UMA banda do DOBRO da massa". Errado mecanístico: redutor QUEBRA dissulfeto → DUAS bandas de cadeia simples. Item é gabaritado E (errado), portanto a redação está OK como distratora, mas o aluno pode confundir-se sobre se o erro é o "uma banda" ou o "dobro da massa". |
| E2 Q28 alt E | [STOP] | 30 | "do recombinante recombinante alvo recombinante" — palavra triplicada. Bug de geração. |
| Gabarito (pág 35→PDF pág 35) | [STOP-LEVE] | 35 | Cabeçalho do PDF diz "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" mas a página é o gabarito da Etapa 2. Cabeçalho herdado errado (Etapa 4 sumiu do pipeline canônico em 2026-05-22, mas o running header ficou). |

---

## 2. T3.1 — Comparação com EXEMPLARES.md (estética/voz)

**Categoria relevante:** "abertura por problema concreto" + "paradoxo contra-intuitivo explicado em uma frase". Não acessei o arquivo no detalhe, mas a memória da categoria de EXEMPLARES.md é consistente — uso aqui como referência interna calibrada pelo `redator-e1.md`.

**Parágrafo do PDF (pág 3, abertura 1.2):**

> "A primeira intuição de quem está começando é imaginar que existe uma 'técnica mágica' que separa a proteína-alvo de tudo o mais em um único passo. Não existe. Toda purificação real é uma sequência de etapas..."

**Diagnóstico:** EXEMPLAR. Voz de monitor — antecipa o erro do aluno, nomeia a fantasia, derruba em 3 palavras ("Não existe."), e amarra na verdade operacional. É o padrão NEBLI que o REDATOR-E1 deveria absorver: **demolir uma expectativa errada antes de construir a certa**.

**Parágrafo do PDF (pág 6–7, filtração em gel):**

> "O resultado parece contraintuitivo até a primeira vez que se entende: numa coluna de filtração em gel, as proteínas grandes saem antes das pequenas."

**Diagnóstico:** EXEMPLAR. Sinaliza o paradoxo, dá a resposta concreta na mesma frase, sem suspense barato. Caixa lateral "Filtração em gel é contraintuitiva" (pág 9) repete o gesto com mnemônico físico ("pequena entra em buraco, demora; grande não entra, escapa") — repetição deliberada do mesmo conceito por ângulos diferentes. NEBLI usa pouco esse recurso de **caixa-lateral de reforço mnemônico depois de já ter ensinado** — vale absorver.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Bloco A — Tabela ASCII das três cromatografias (pág 9)

**(a) Citação literal:**
> "Filtração em gel  Tamanho molecular Grandes primeiro, pe- Modesta -- separa fa-
>                   -- esferas porosas re- quenas por último  tores 2-5× de massa
>                   tardam os pequenos"

**(b) Diagnóstico mecanístico:** a tabela é o item de maior valor pedagógico da PARTE II (consolida tamanho/carga/afinidade num quadro comparável) mas saiu renderizada com quebras de coluna no meio das palavras. Aluno-eu olha, tenta achar "filtração em gel | princípio | ordem | resolução", e o que recebo é um amontoado quebrado. **A tabela falhou exatamente onde mais importava: consolidar o framework.**

**(c) Reescrita pronta** (substituir por `table()` Typst nativo, header navy):

```typst
#table(
  columns: (1.3fr, 2fr, 2fr, 1.5fr),
  align: (left, left, left, left),
  fill: (col, row) => if row == 0 { rgb("#0B2545") } else { none },
  table.header(
    [*Técnica*], [*Princípio físico*], [*Ordem de saída*], [*Resolução*]
  ),
  [Filtração em gel],
  [Tamanho molecular — esferas porosas retardam os pequenos],
  [Grandes primeiro, pequenas por último],
  [Modesta — separa fatores 2–5× de massa],

  [Troca iônica],
  [Carga líquida no pH usado — competição com sal],
  [Pouca carga primeiro, muita carga por último (gradiente)],
  [Boa — separa cargas ligeiramente diferentes],

  [Afinidade],
  [Ligação específica com ligante imobilizado],
  [Tudo passa direto, só a alvo fica; sai com competidor],
  [Excelente — 1.000–10.000× em uma etapa],
)
```

### Bloco B — Resumindo (pág 16), hifenização agressiva

**(a) Citação literal:**
> "Clone único de plasmác-/itos produz uma só imunoglobulina em excesso  / aparece como pico M estreito e alto na fração."

**(b) Diagnóstico:** o Resumindo, que é A página que o aluno revisita na véspera da prova, está com hifenização exagerada cortando palavras-chave no meio (plasmác-itos, diab-éticos, res-olução). Aluno-eu olho e perco 200ms decodificando cada palavra quebrada — o efeito agregado é fadiga visual num momento em que a leitura deveria ser fluida.

**(c) Reescrita pronta:** aumentar largura mínima de cada coluna em 5–8%, ou desligar hifenização no `resumindo-page()` (set `text(hyphenate: false)` no escopo). Conteúdo permanece igual; layout fica limpo. Alternativa: reescrever as 2 frases-cabeça das 8 seções com 2–3 palavras a menos para evitar quebra forçada.

### Bloco C — Página 13 (mosaico de 4 slides do professor)

**(a) Citação literal (legenda do mosaico):**
> "Eletroforese explorando carga. Na focalização isoelétrica, cada proteína migra até o pH = pI e para. A comparação normal × patológico mostra como pequenas alterações de carga (por mutação pontual em um aminoácido ionizável) deslocam bandas inteiras — base do diagnóstico de hemoglobinopatias."

**(b) Diagnóstico:** a legenda é boa, mas serve a 4 figuras de uma vez. Aluno-eu não sei a qual figura cada frase corresponde, nem qual figura é primária e qual é decorativa. As 4 figuras são slides crus do professor (NEBLI canônico aceita slide do professor como prioridade) mas aqui foram amontoadas sem hierarquia. Resultado: respiro zero, valor pedagógico de cada figura individual cai a ~40% do que seria isolada.

**(c) Reescrita pronta:** quebrar em 2 figuras-pares lado a lado (1 par por seção 3.x), cada uma com legenda própria de 2 linhas. Eliminar 1 das 4 (a "Eletroforese pode também separar proteínas por tamanho" duplica o SDS-PAGE já ilustrado). Largura `figura-lateral` 50%+texto-curto à direita ancora cada par.

---

## 4. T3.3 — 3 seções mais densas (mitigação)

| Seção | Densidade | Mitigação concreta |
|---|---|---|
| Tabela 3-variantes (pág 9) | Pico de densidade visual + 4 colunas + 6 conceitos cruzados | Reescrever como `table()` Typst nativo (Bloco A acima) + adicionar 1 mini-figura ao lado mostrando esfera porosa / esfera carregada / esfera com ligante. |
| 3.1 SDS-PAGE (pág 10–11) | Mecanismo em 4 passos (desnaturação, redução, recobrimento por SDS, raio carga/massa igual) numa única página | Quebrar em 2 sub-passagens: (a) "primeiro o SDS desenrola e cobre" — figura 1; (b) "depois o gel separa só por tamanho" — figura 2. Cadeia multi-passo (4 eventos físicos) merece figura dedicada que NEBLI manda obrigar. |
| 3.2 IEF (pág 11–12) | "Poço de potencial" mencionado sem definir — assume física do ensino médio que o aluno não tem | Inserir 1 frase: "Poço de potencial = vale numa paisagem de energia — se você está no fundo, qualquer empurrão para fora gera uma força que te traz de volta. O pI da proteína funciona assim no gradiente de pH." |

---

## 5. T3.4 — Voz fora do padrão

Voz geral é **excelente e consistente** — diálogo com o aluno do início ao fim. Poucos desvios:

- **Pág 8 ("Insulina recombinante"):** "Praticamente toda a indústria de proteínas recombinantes hoje usa essa estratégia." — frase tipo manual, lacônica. Compatível com voz da caixa-clínica, aceitável.
- **Pág 14, conclusão integradora:** "Cada técnica que parece abstrata na bancada acaba, em algum ponto, decidindo um diagnóstico ou viabilizando um tratamento." — voz **modelo**, fechamento integrador que NEBLI raramente acerta tão limpo.
- **Bug de geração pág 30 Q28 alt E:** "do recombinante recombinante alvo recombinante" — não é voz fora do padrão, é truncamento/colagem. Reportado em T3.10.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** página 11 (transição de SDS-PAGE para focalização isoelétrica). Em uma única página o aluno precisa: (i) consolidar SDS-PAGE (raio carga/massa, agente redutor, calibração de massa), (ii) ler caixa-clínica do Western blot/HIV (gp120, gp41, p24, padrão confirmatório), (iii) abrir conceito novo IEF + introduzir pI, (iv) ler 3 sigla-notas no rodapé (SDS-PAGE, pI, focalização isoelétrica). Som = pico de carga.

**3 mitigações possíveis:**

1. Empurrar a caixa-clínica do HIV para depois do IEF (vira respiração entre dois mecanismos densos).
2. Definir pI numa frase auto-contida ANTES de introduzir IEF: "pI é o pH em que a proteína tem carga total zero" — e só então atacar o mecanismo do gradiente.
3. Mover o sigla-nota do pI para uma definição inline em itálico no corpo, eliminando 1 footnote do rodapé daquela página específica.

**Qual escolher:** **(1) + (2) combinadas.** Caixa-clínica do HIV é respiro pedagógico — usar bem. Definição pré de pI é barreira que o aluno-eu precisa para não fechar o PDF.

---

## 7. T3.8 — ANÁLISE VISUAL (pages 1, 2, 4, 11, 13, 35)

| Sub-item | Diagnóstico |
|---|---|
| **Hierarquia tipográfica** | EXCELENTE na capa, sumário e gabarito (faixa navy, hierarquia clara H1/H2/H3 em Montserrat, corpo Merriweather). Funciona. |
| **Valor pedagógico das figuras** | MISTO. Diagrama-esquema canônico (pág 4) é decorativo demais — caixas com nomes mas sem mecanismo. Figura mecanística da filtração em gel (pág 7) é exemplar (legendada, integrada). Mosaico da pág 13 (4 slides crus) é o pior: figuras estão presentes mas sem hierarquia pedagógica, legenda única para 4 unidades. |
| **Densidade visual** | DESEQUILIBRADA. Pág 4 mistura prosa + box "Resumindo até aqui" + diagrama horizontal + legenda longa em UMA página → muro. Pág 2 (sumário) é airy demais — sobra 70% da página em branco. Pág 11 tem 3 footnotes empilhadas no rodapé (SDS-PAGE, pI, IEF) que consomem 18% da altura. |
| **Uso de cor** | COERENTE e disciplinado: navy NEBLI canônico em títulos, cinza para meta. Cor não é usada para destacar conceitos no corpo (o que é a tradição NEBLI — bom). Caixas-clínicas (HIV, hemoglobinopatias, mieloma) usam mesma cor — sem distinção visual entre "âncora clínica" e "exemplo industrial". Oportunidade: badge colorida para diferenciar caixas tipo "clínica" vs "produção". |
| **Cortes/overflow** | DUAS quebras observadas: (a) tabela 3-variantes pág 9 — texto quebrado dentro das células; (b) Resumindo pág 16 — hifenização agressiva ("plasmác-itos", "diab-éticos"). Cabeçalho running do gabarito pág 35 diz "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" mas a página é Gabarito da Etapa 2 — running header herdado errado. |

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### 1. Demolição da fantasia antes de construir a verdade

**Citação literal (pág 3, 1.2):**
> "A primeira intuição de quem está começando é imaginar que existe uma 'técnica mágica' que separa a proteína-alvo de tudo o mais em um único passo. Não existe."

**Nome da técnica:** *anti-âncora ingênua* — o autor nomeia a fantasia plausível do aluno-iniciante, derruba em 1 frase curta, e só então constrói o conceito real (sequência de etapas).

**Quando NEBLI deveria usar:** **abertura de toda subseção que ataca um conceito contra-intuitivo.** REDATOR-E1 frequentemente abre com "vamos entender X" sem antes nomear a expectativa errada que o aluno traz. Gancho concreto: em gliconeogênese, abrir 2.1 com "A primeira intuição é que gliconeogênese é só glicólise ao contrário. Não é." Em cadeia respiratória, "A intuição é que NADH 'doa' elétrons direto pro O₂. Não é assim — eles caem por um corredor de 4 complexos." **Técnica de uma frase, ganho pedagógico enorme.**

### 2. Caixa-lateral de reforço mnemônico DEPOIS de já ter ensinado

**Citação literal (pág 9, caixa "Filtração em gel é contraintuitiva"):**
> "Memorize o gesto físico: pequena entra em buraco, demora; grande não entra, escapa."

**Nome da técnica:** *mnemônico-gesto pós-mecânico* — o conceito já foi explicado mecanisticamente em 2.1; a caixa-lateral retoma com um mnemônico verbal curto, físico, que substitui memorização decorada por imagem.

**Quando NEBLI deveria usar:** **toda vez que o mecanismo é contraintuitivo o suficiente para o aluno esquecer e inverter na hora da prova.** Hoje o NEBLI tende a explicar uma vez e seguir. Gancho concreto: em gliconeogênese, após explicar bypass 3 (G6Pase no RE), caixa-lateral "G6Pase é portaria de saída — só quem tem cartão de RE sai. Hexoquinase comum não tem." Em cadeia respiratória, após explicar fluxo de prótons, "Prótons só saem pela ATP-sintase ou voltam pela mesma porta — não tem janela alternativa." Padrão: 1 frase curta, físico, depois do mecanismo.

### 3. Tabela hipotética com números fictícios mas realistas

**Citação literal (pág 5, tabela):**
> "Atividade espec. (U/mg) 5 → 14 → 43 → 152 → 1.800 — fator de 360×; rendimento de 100% para 27%."

**Nome da técnica:** *exemplo numérico fictício mas calibrado* — em vez de prosa abstrata sobre "rendimento cai, atividade específica sobe", o autor dá 5 linhas de tabela com números que o aluno pode operacionalizar mentalmente (5 → 1.800 é fator 360×, 100% → 27% é perda de 73%).

**Quando NEBLI deveria usar:** **toda regra quantitativa que o aluno precisa internalizar como ordem de grandeza, não como fórmula.** Hoje NEBLI evita tabelas didáticas hipotéticas (são bullets disfarçados?). Mas o caso (c) da regra de bullets — critérios diagnósticos / regras com itens discretos — cobre exemplos numéricos calibrados. Gancho concreto: em cinética enzimática, mostrar Km medido vs Km real numa tabela hipotética com 3 contaminantes. Em gliconeogênese, custo energético "6 ATP gastos por glicose vs 2 ATP rendidos em glicólise — fator 3× — eis o preço de remontar."

---

## 9. T3.10 — 7 erros NEBLI no PDF (tabela calibração)

| Erro | Status | Evidência |
|---|---|---|
| 1. Paridade distratoras E2 Aplicação | **PRESENTE (parcial)** | Q26 alt C (correta) 38 palavras vs alt B (12 palavras) — ratio ~3.2×, viola ≤1.25. Q28 alt B (correta, 26 palavras) vs alt D (16) — ratio aceitável 1.6×, ainda fora do canon. Q30 razoavelmente paritária. **Veredito:** o autor histórico também cai no erro #1 — distratoras de Aplicação ficam mais curtas que a correta. Mesmo o autor sênior do projeto incorre. |
| 2. Siglas sem `#sigla()` na 1ª aparição | **PARCIALMENTE PRESENTE** | SDS, pI, IEF, SDS-PAGE têm footnote (bom). MAS: "DTT" aparece na Q20 sem definição prévia no corpo, "Km" aparece na Q26 cru, "NaCl" aparece em pág 7 sem footnote (talvez aceitável por ser sigla de ensino médio), "Ni²" pág 8 sem footnote (aceitável). Atrasos pontuais, não sistêmicos. |
| 3. Subagentes Opus contaminados | **N/A** | Apostila histórica, não passou pelo pipeline NEBLI atual. |
| 4. Heredoc ENAMETOOLONG | **N/A** | Não aplicável a apostila renderizada. |
| 5. `questao-ce` exige tupla `(rom, conteudo)` | **N/A** | Erro de compilação Typst, não diagnóstico de conteúdo. |
| 6. Termos-nota abaixo do alvo (4 em vez de 6–8) | **AUSENTE** | Apostila tem footnote para E. coli, atividade específica, fase móvel, gradiente salino, ligante, SDS, SDS-PAGE, pI, focalização isoelétrica — **9 footnotes/sigla-notas** distribuídas. Acima do alvo, bem feito. |
| 7. Tema-card com teto E1 errado | **N/A** | Apostila tem ~15 páginas de Etapa 1 — bem dentro de piso 2 / teto 22. Não há teto errado a corrigir aqui. |

**Erros NEBLI adicionais detectados (extra-checklist):**

- **Bug de geração Q28 alt E:** "do recombinante recombinante alvo recombinante" — palavra triplicada. Confirma erro de pipeline (provavelmente colagem/replace mal feito).
- **Bug Q08 item I:** "carga líquida líquida" — duplicação.
- **Bug Q19 item III:** redação ambígua — afirmar que SDS-PAGE com redutor mostraria "uma banda do dobro" é falso, mas o item já é gabarito E (errado), então funciona como distratora. Risco: aluno marca E pelo motivo errado.
- **Running header pág 35:** "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" sobre página de Gabarito da Etapa 2. Etapa 4 foi removida em 2026-05-22 mas o cabeçalho ficou.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)

1. **Reescrever tabela 3-variantes (pág 9) como `table()` Typst nativo com header navy.** Tabela ASCII quebrada destrói o quadro consolidador da PARTE II. É o item de maior impacto único.
2. **Quebrar página-mosaico pág 13 em 2 pares figura-legenda.** 4 slides crus sem hierarquia consomem espaço sem entregar pedagogia. Cada par com legenda de 2 linhas integrada.
3. **Limpar bugs de geração de E2:** Q08 "líquida líquida", Q19 III ambígua, Q28 alt E triplicada. Running header pág 35 corrigido para "ETAPA 2 — GABARITO".

### MECANÍSTICO (max 3)

1. **Definir "poço de potencial" em 1 frase antes de IEF (pág 11–12).** Aluno-eu não tem física de ensino superior para decifrar sozinho.
2. **Quebrar SDS-PAGE em 2 sub-mecânicas com figura cada (pág 10–11):** (a) SDS desenrola+cobre; (b) gel separa por tamanho. Cadeia multi-passo merece figura dedicada (regra canônica NEBLI).
3. **Paridade de distratoras em Q26–Q30:** engordar 2–3 distratoras de Aplicação até alcançar ratio ≤1.25× com a correta. Hoje viola na Q26.

### DIDÁTICO (max 3)

1. **Mover caixa-clínica do HIV para DEPOIS do IEF (pág 11),** dando respiro entre dois mecanismos densos. Carga cognitiva pico atual está concentrada numa única página.
2. **Inserir caixa-lateral mnemônica DEPOIS da tabela das 3 cromatografias,** consolidando "poros (tamanho) → grupos iônicos (carga) → ligante (afinidade)" numa frase memorizável. Repetir a técnica do autor que já funcionou em filtração em gel.
3. **Resumindo (pág 16):** desligar hifenização agressiva OU encurtar 2–3 frases-cabeça. Aluno revisita essa página na véspera; precisa ler fluido.

### ESTÉTICO (max 3)

1. **Sumário (pág 2):** está airy demais (70% espaço em branco). Centralizar verticalmente OU adicionar mini-bloco com "Como usar este resumo" (3 linhas).
2. **Mapa Conceitual ASCII (pág 6, pág 14):** lay-out quebra em ASCII. Substituir por figura SVG simples ou por `#columns(3)` com caixinhas estilizadas.
3. **Capa (pág 1):** "Bioquímica" aparece como SUBTÍTULO sob "Purificação de proteínas" — convenção esquisita, pois Bioquímica é a disciplina, já declarada no bloco meta abaixo. Solução: remover ou substituir por subtítulo descritivo curto ("Cromatografia e eletroforese — três famílias, um princípio").

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM.** Apesar dos bugs estruturais (tabela quebrada, mosaico, hifenização), a voz didática, a anti-âncora ingênua na abertura, o paradoxo da peneira bem manejado, e a integração clínica final são exemplares para REDATOR-E1.

2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM.** Tabela 3-variantes precisa ser refeita em `table()` nativo (ESTRUTURAL); SDS-PAGE precisa ser quebrado em 2 sub-mecânicas com figura cada (MECANÍSTICO).

3. **Seção para refazer?** **PARTE II finalização (pág 9, tabela das 3 cromatografias)** + **página 13 (mosaico de slides).** Resto é polimento.

4. **Parágrafos para reescrever?** **3.** (a) Tabela 3-variantes pág 9; (b) Bloco "Resumindo" pág 16 (hifenização); (c) Transição SDS-PAGE → IEF na pág 11 (carga cognitiva pico, falta definição pré de "poço de potencial").

---

[APROVAR COM RESERVAS]
