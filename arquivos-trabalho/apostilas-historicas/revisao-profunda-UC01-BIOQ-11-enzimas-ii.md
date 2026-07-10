# Revisão profunda Tier 3 — UC01-BIOQ-11-enzimas-ii

**Tema (ancoragem):** Enzimas II — inibição enzimática (irreversível, competitiva, não-competitiva, acompetitiva); ambiente catalítico (pH, temperatura, alosteria sigmoide TR + MWC/KNF); estratégias regulatórias (modificação covalente reversível por fosforilação, isozimas, zimogênios). Eixo unificador: **onde liga + em qual estado da enzima → consequência em KM e Vmax**.
**Autor:** Marisa Helena (apostila histórica, UC01 Bioquímica aula 11).
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real com bioquímica enzimática; ensino médio + ~6 meses de medicina; sem livro-texto aberto ao lado; acabou de digerir Enzimas I (KM, Vmax, MM, LB) e ainda está consolidando.
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo.
**Data:** 2026-05-25

### Âncora de tema

- **3 conceitos centrais que eu-aluno quero aprender:** (1) por que o competitivo pode ser superado por [S] e o não-competitivo não — mecanismo, não decoreba; (2) por que o acompetitivo derruba **os dois** (KM e Vmax) ao mesmo tempo — Le Chatelier real, não fórmula; (3) qual é a régua única que organiza os quatro tipos (onde liga + em qual estado).
- **2 temas vizinhos que NÃO são esse:** cinética básica MM, KM/Vmax/Lineweaver-Burk do ponto de vista da derivação (isso é Enzimas I); estrutura de proteína / dobramento (isso é Proteínas I-II).

---

## 1. Pontos de parada (simulação de leitura linha-a-linha)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Capa + nota de uso | OK | 1 | Nota de uso explícita ("Quem decora 'KM sobe, KM cai' sem entender por que perde questão clínica") já vacina o aluno contra o erro mais comum do tema. Excelente. |
| Sumário | OK | 2 | Hierarquia 3 PARTES × 2-4 subtópicos cabe em 1 página. **Mas** lista "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" que NÃO existe no PDF (canônico removeu em 2026-05-22) — bug herdado da apostila I. Aluno espera Etapa 4, não acha, perde confiança. |
| Intro p.3 ("Enzimas I terminou com…") | OK | 3 | Recapitula Enzimas I em 6 linhas e declara o **fio mecanístico do capítulo inteiro** (KM e Vmax, onde e em qual estado). É a melhor abertura possível para um capítulo-2-de-par. |
| 1.1 Irreversível abertura | OK | 3-4 | Pergunta operacional ("o que separa um inibidor de qualquer outra molécula que entra?") seguida de critério temporal (duração da redução de velocidade). É didaticamente impecável. |
| Box "Irreversível não é deslocável por [S]" + AAS/penicilina/AZT/DFP | OK | 4 | 4 exemplos clínicos vivos por inibidor irreversível — densidade ótima. AZT explicado por *engano molecular* ("a enzima se inativa sozinha") é um gancho memorável. |
| 1.2 Competitiva (captopril/MTX/ibuprofeno) | OK | 5 | Trio clínico fechado, leitura LB justificada por geometria. |
| 1.3 Não-competitiva | **[STOP leve: pág 6]** | 6 | "saquinavir e ritonavir" como exemplo aparece sem ancorar que são **inibidores de protease do HIV** — só na linha seguinte, fora da primeira sentença. Aluno em dificuldade lê "saquinavir liga fora do sítio catalítico" e fica boiando 1 segundo procurando o que é a droga. Falta `#sigla()` ou aposto curto. |
| 1.4 Acompetitiva + Le Chatelier | **[STOP pesado: pág 7]** | 7 | **Aqui o aluno fecha o PDF.** "Pense em Le Chatelier: E + S ⇌ ES ⇌ E + P. Se você 'remove' ES do equilíbrio (sequestrando como ES·I), o equilíbrio é puxado para frente — mais E + S vai se converter em ES para compensar a perda. Resultado: KM aparente CAI." A explicação está **correta**, mas eu-aluno não sabe traduzir "equilíbrio é puxado para frente" em "agora a enzima parece ter mais afinidade pelo substrato". A frase "Parece haver mais afinidade pelo substrato, porque o complexo ES está sendo formado mais facilmente" salva, mas vem rápido demais — 1 frase de mecanismo, 1 frase de consequência cinética, sem a ponte numérica (ex.: "antes [E·S] era 1 unidade no equilíbrio, agora é 0,7 livre + 0,3 sequestrado, mas o sistema corre para repor → mais E+S vira ES → a fração no estado ES sobe e KM aparente desce"). É **o ponto-pivô do capítulo** e merece 3-4 frases extras. |
| Tabela 4 tipos (p.7) | **[STOP visual: pág 7]** | 7 | A tabela tem **uma linha quebrada visualmente**: "Irreversível -- (sem cinética esta / cionária)" — a célula KM da linha irreversível foi cortada com hifenização horrenda no meio da palavra "estacionária". Aluno em dificuldade lê isso como bug e perde a tabela. Linha pivô do capítulo renderizada como typo. |
| Mapa conceitual PARTE I | OK estético, fraco didático | 8 | O "mapa" é três caixinhas sem setas-de-mecanismo. Diz O QUE cada inibição faz, não COMO. Decorativo. |
| 2.1 pH e T | OK | 8-9 | Pico em sino justificado por **dois resíduos com pKa opostos** — mecanismo limpo, com box "queda por pH ≠ desnaturação" no momento certo. Microambiente proteico desloca pKa é a sutileza que o slide 23 cobra; está bem colocado. |
| 2.2 Alosteria | OK forte | 10-11 | "Mesmo princípio TR da hemoglobina, agora numa enzima catalítica" é gancho com Enzimas anteriores. Vantagem da sigmoide explicada por **número concreto** (33%→50% na hipérbole vs 10%→80% na sigmoide para mesma duplicação de [S]) — é o tipo de comparação numérica que o EXEMPLARES 4.1 prescreve. |
| Box MWC vs KNF | OK | 11 | Honesto: "enzimas reais se comportam entre os dois extremos". Sem fingir que o aluno tem que escolher um. |
| Mapa conceitual PARTE II | Fraco | 11 | "pH e T" + "Alosteria" em duas caixinhas. Não desenha o vínculo conceitual entre os dois ("ambos modulam atividade sem ligar nova droga"). Texto da legenda do mapa diz isso, mas o **mapa visual** não. |
| 3.1 Fosforilação | OK | 12-13 | Quinase/fosfatase como par catalítico contínuo é a metáfora certa ("estado de fosforilação reflete o equilíbrio"). Glicogênio fosforilase ativada vs sintase inibida pela **mesma** fosforilação é o exemplo-pivô do tópico — bem escolhido. |
| Cascata AMPc-PKA p.13 | **[STOP leve: pág 13]** | 13 | "adrenalina → ativa receptor → ativa adenilil ciclase → produz cAMP → ativa PKA → fosforila fosforilase quinase → fosforila glicogênio fosforilase" — sete passos em uma linha, sem hierarquia visual. cAMP/AMPc aparece sem `#sigla()`. Aluno em dificuldade conta os passos no dedo e perde o ponto (que é amplificação). Falta a aritmética da amplificação **passo-a-passo** (1 hormônio → X cAMP → Y PKA → Z fosforilases finais). |
| Box "Fosforilação ≠ AAS" | OK | 13 | Box anti-confusão no lugar certo (covalente reversível vs covalente irreversível). |
| 3.2 Isozimas HK/GK | OK forte | 14 | "HK opera saturada o tempo todo / GK só acorda pós-prandial" é a frase-tese certa, com aritmética imediata (5 mM ÷ 0,05 mM = 100× o KM). LDH/CK como marcadores de infarto fecha com clínica. |
| 3.3 Zimogênio + pancreatite | OK | 15-16 | Pancreatite aguda + SPINK1 é a clínica que ancora o conceito. Caspases + coagulação ampliam para outros sistemas. |
| Conclusão integradora p.17 | OK forte | 17 | "AAS é covalente (irreversível), captopril compete pelo sítio (KM sobe, Vmax fica), lítio só pega ES (Vmax e KM caem juntos)" — recapitula com o fio único. Faz o que a conclusão precisa fazer. |
| Resumindo (1 pág) | OK | 18 | Caixa-de-fim em 1 página, multi-coluna densa mas legível. 8 blocos = dentro do alvo canônico (8-12). |
| Etapa 2 (Q01-Q30) | OK forte | 19-36 | Distratoras em geral com mecanismo plausível (raras curtas). Detalhes em §3 e §4. |
| Q21 SPINK1 / Q28 SPINK1 | Redundância | 31, 34 | Duas questões inteiras sobre SPINK1 (Q21 e Q28). Q21 pede "defesa fisiológica", Q28 pede "nexo fisiopatológico em neonato". Conceito é o **mesmo**. Em 30 questões, gastar 2 com SPINK1 é desperdício curricular — lítio acompetitivo merece 2, mas SPINK1 cabe em 1. |
| Etapa 3 Q1-Q5 | OK | 37-39 | Modelos de resposta com mecanismo (Le Chatelier explicitado em Q2, "MAIOR efeito clínico" em Q5). |
| Gabarito p.40 | **[STOP estrutural: pág 40]** | 40 | Bug **idêntico ao de Enzimas I**: header da página diz "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" mas o conteúdo é o gabarito da Etapa 2. Etapa 4 está no sumário (p.2) mas não existe no PDF. **Última página do PDF é a primeira que o aluno vai abrir para conferir respostas — ele lê "Etapa 4" no header, procura Etapa 4, não acha, fica em dúvida se a apostila está incompleta.** |
| Layout do gabarito | **[STOP visual: pág 40]** | 40 | 5 colunas com ordem embaralhada: Q03, Q04, Q05 na col-1 mas Q12, Q13 na col-3, Q16, Q17 na col-2, etc. Aluno procura Q11 e demora ~10s para encontrar (está logo após Q06, na col-2). Em apostila de prova, esse tempo perdido é fricção real. |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria-chave selecionada:** CATEGORIA 3 "Abertura por desfazer confusão comum" + CATEGORIA 11 "Distratores mecanísticos para objetivas".

### Comparação A — abertura do capítulo (CATEGORIA 3)

**Parágrafo HISTÓRICO (esta apostila, p.3):**
> "Enzimas I terminou com um quadro otimista: temos uma máquina molecular elegante… Enzimas II é o que a fisiologia e a farmacologia fazem com essa máquina. Como freá-la quando ela precisa parar (inibição), como ajustá-la conforme a célula muda (alosteria, pH), e como ligá-la e desligá-la rapidamente (modificação covalente, zimogênios, isozimas). O fio mecanístico aqui é simples e poderoso: toda manipulação enzimática mexe em duas alavancas, KM e Vmax."

**Parágrafo EXEMPLAR (Marisa Helena, EXEMPLARES 3.1):**
> "Antes de qualquer coisa, precisamos desfazer uma confusão comum. Muitas pessoas pensam que «enzima faz reação acontecer». **Isso está errado.**"

**Diagnóstico:** o histórico aqui escolhe **continuidade** ("Enzimas I terminou com X, agora vai-se a Y") em vez de **erro mental** (que seria: "Você provavelmente acha que cada tipo de inibição é uma exceção. Não. Há uma régua única: onde liga + em qual estado."). A continuidade é válida porque o capítulo é literalmente uma continuação; e a regra-régua é declarada na linha seguinte. Decisão editorial defensável. **Mas perde a chance** de vacinar contra o erro "decorei KM sobe / KM cai" — que o próprio autor cita na nota de uso da capa. Para o REDATOR-E1 NEBLI: quando o capítulo é continuação, é legítimo abrir com gancho de continuidade; mas se há **erro recorrente nominal** (e aqui há), abrir desfazendo o erro é superior.

**Veredito:** histórico é bom; exemplar ainda é melhor. Há espaço para o NEBLI escolher mais frequentemente o padrão "erro-mental" que a própria autora cunhou em Enzimas I.

### Comparação B — distratoras de Q26 (captopril/escape) vs EXEMPLARES 11

**Distratoras Q26 HISTÓRICO:**
- A) 45 palavras, mecanismo plausível ("substituir por não-competitivo" — erro real do aluno).
- B) **CORRETA**, 50 palavras.
- C) 38 palavras, mecanismo invertido (renina baixa).
- D) 35 palavras, mecanismo inventado ("captopril vira irreversível").
- E) 28 palavras, mecanismo errado mas plausível ("renina bloqueia ECA").

**Ratio correta/maior distratora:** 50/45 ≈ 1.11. **Dentro do canônico ≤ 1.25.** Paridade boa.

**EXEMPLAR 11 (padrão Q15 transporte):** distratoras de 18-24 palavras, correta 24. Esta apostila opera num registro mais longo (35-50 palavras), mas a paridade interna está respeitada. **Veredito:** alinhado com o padrão NEBLI canônico — esta apostila é uma das poucas que aplica paridade certa em Aplicação.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo fraco 1 — Le Chatelier do acompetitivo (p.7)

**Citação literal:**
> "Pense em Le Chatelier: a reação E + S ⇌ ES ⇌ E + P. Se você 'remove' ES do equilíbrio (sequestrando como ES·I), o equilíbrio é puxado para frente — mais E + S vai se converter em ES para compensar a perda. Resultado: KM aparente CAI. Parece haver mais afinidade pelo substrato, porque o complexo ES está sendo formado mais facilmente. Mas não há ganho — esse ES extra está sendo sequestrado pelo inibidor."

**Diagnóstico mecanístico:** o gesto Le Chatelier → KM cai é o pivô do capítulo (a única inibição em que **ambos** os parâmetros caem). Quatro frases dão conta da causa, mas eu-aluno precisa de uma **ponte numérica** entre "equilíbrio puxado pra frente" e "KM aparente cai". KM aparente é uma medida operacional ([S] necessária para meia-Vmax). Sem reconectar a Le Chatelier com essa definição operacional, eu-aluno aceita "KM cai" como dogma. E o último parágrafo ("não há ganho") aparece sem explicar que **Vmax também caiu** — Vmax e KM caem na mesma proporção é a frase-chave do tipo, e ela só vem 2 parágrafos abaixo, na seção "consequência das duas alavancas".

**Reescrita pronta:**
> "Pense em Le Chatelier numa balança: a reação E + S ⇌ ES ⇌ E + P estava num equilíbrio onde, digamos, metade da enzima existia como E livre e metade como ES. O acompetitivo aparece e sequestra parte do ES como ES·I. O sistema agora tem 'menos ES disponível para virar produto', e a reação reposta: mais E + S volta a formar ES para compensar. **Aqui está o gesto-pivô:** para chegar à mesma quantidade de ES (e portanto à mesma velocidade), agora basta menos substrato no meio. KM aparente é, por definição, a [S] que dá meia-Vmax — e essa [S] **diminuiu**, porque o sistema gera ES mais fácil. Por isso KM aparente CAI. Mas atenção: o ES extra está sendo sequestrado, não virando produto. Vmax cai junto — e **na mesma proporção** que KM. É por isso que no Lineweaver-Burk as retas ficam paralelas (a razão KM/Vmax, que é a inclinação, fica constante)."

### Parágrafo fraco 2 — Cascata AMPc-PKA em uma linha (p.13)

**Citação literal:**
> "Adrenalina chega ao hepatócito → ativa receptor → ativa adenilil ciclase → produz cAMP → ativa PKA → fosforila fosforilase quinase → fosforila glicogênio fosforilase. Cada nível multiplica o sinal por um fator. Uma molécula de adrenalina pode ativar 10⁶ moléculas de glicogênio fosforilase — a quebra de glicogênio responde em segundos a estímulos hormonais minúsculos."

**Diagnóstico mecanístico:** sete passos despejados em linha única + afirmação "10⁶" sem aritmética. cAMP, PKA, AMPc aparecem aqui pela primeira vez sem `#sigla()`. O aluno em dificuldade tem três opções: (a) decora a sequência sem entender, (b) volta para Sinalização (que ainda não viu), (c) fecha o PDF. A amplificação é o **conceito** que justifica a cascata existir — explicar 10⁶ sem mostrar **onde** cada fator vem é vender o número como mágica.

**Reescrita pronta:**
> "Para entender a amplificação, vale percorrer a cascata contando os ganhos passo-a-passo. Adrenalina (uma molécula) chega ao receptor de membrana do hepatócito; o receptor ativado, enquanto ela estiver ligada, ativa **centenas** de moléculas da adenilil ciclase¹ vizinhas — ganho ×10². Cada adenilil ciclase produz cAMP² (segundo mensageiro derivado de ATP) por minuto, dezenas de cAMP por unidade de tempo — ganho ×10. Cada cAMP ativa uma PKA³, e cada PKA fosforila **dezenas** de fosforilases quinase — ganho ×10. Cada fosforilase quinase fosforila **centenas** de glicogênio fosforilases — ganho ×10². Multiplicando: 10² × 10 × 10 × 10² ≈ 10⁶. **Uma molécula de hormônio mobiliza um milhão de enzimas finais.** A escala não é figura de retórica; é o produto cumulativo de cada degrau. Por isso a célula consegue ouvir um sinal hormonal em concentração nanomolar (10⁻⁹ M) e responder com mobilização metabólica robusta em segundos."
> (com `#sigla()` declarados para adenilil ciclase, cAMP, PKA na primeira aparição)

### Parágrafo fraco 3 — Mapas conceituais decorativos (p.8, 12, 17)

**Citação literal (PARTE I, p.8):**
> "MAPA CONCEITUAL I — Onde liga e em qual estado / 1.1 Irreversível: Covalente, inativa permanente / 1.2 Competitiva: Sítio ativo, deslocável por S / 1.3 Não-comp.: Outro sítio, sobre E ou ES // Identificar o tipo de inibição é identificar onde a droga liga e em qual estado da enzima. O resto é consequência cinética."

**Diagnóstico mecanístico:** o "mapa" é uma **lista verbal em três caixinhas**, sem setas, sem agrupamento por critério, sem mostrar o **eixo** que organiza ("onde liga" no eixo X, "qual estado" no eixo Y, com cada inibição num quadrante). Cita 3 dos 4 tipos (esqueceu a acompetitiva — provavelmente cortada por espaço). O texto da legenda diz a coisa certa ("o resto é consequência cinética"), mas o **desenho** não entrega o gesto. É decorativo, ocupa espaço, não substitui o que já está no texto.

**Reescrita pronta:** transformar em **matriz 2×2 real**, com eixo X = "onde liga" (sítio ativo / sítio diferente) e eixo Y = "qual estado" (E livre / só ES / E livre ou ES). Quatro tipos nos quatro quadrantes, com KM↑/↓ e Vmax↑/↓ em cada quadrante. **Ou** remover o mapa e usar o espaço para a tabela 4-tipos (que já existe mas está renderizada com bug de quebra-linha — ver Pontos de Parada). Em qualquer caso: **mapa conceitual sem eixo classificatório é fluff visual** — o NEBLI já abandonou mapas mentais SVG em 2026-05-19 justamente por isso.

---

## 4. T3.3 — 3 seções mais densas (carga cognitiva)

### Seção densa 1 — p.19 (468 palavras, pico de densidade do PDF)

A página que abre a Etapa 2 — Q01-Q02 tendo a corrida final do "Resumindo" + transição + primeira questão num único folio. **Mitigação concreta:** quebrar página entre Resumindo (que fecha em uma página própria, 18) e Etapa 2 (começa página nova). Aqui o PDF parece já fazer isso (Resumindo p.18, Etapa 2 abre p.19), mas a página 19 contém o **Resumindo** comprimido em duas colunas + transição. Conferir se o pagebreak está antes de Q01.

### Seção densa 2 — p.7 (acompetitiva + tabela + mapa)

468 palavras de explicação Le Chatelier + tabela 4 tipos + mapa conceitual + transição PARTE II — tudo na p.7-8. **Mitigação concreta:** mover o mapa conceitual para depois da PARTE II (ou eliminá-lo), liberando espaço para reescrita longa do Le Chatelier (Parágrafo fraco 1 acima) + tabela 4 tipos em página própria com layout limpo.

### Seção densa 3 — p.13 (fosforilação + cascata + box)

437 palavras na p.7 (densidade alta mas suportável) e 334 na p.12 — o ponto pesado é a cascata AMPc-PKA em uma linha + box "fosforilação ≠ AAS" + transição para 3.2 isozimas. **Mitigação concreta:** dedicar metade da p.13 à figura cascata (numérica, com ganhos por passo) — a apostila tem 12 imagens no total, mas a cascata aparece **sem figura** (a única seção crítica do capítulo sem ilustração). Isso bate no canônico NEBLI: "cadeia multi-passo (≥5 reações) = figura obrigatória". Aqui são 7 passos, sem figura. Erro mecânico do tipo.

**Qual escolher:** **figura da cascata com aritmética visível** é o ganho de maior impacto. Resolve densidade + amplificação + ancoragem visual em um único gesto.

---

## 5. T3.4 — Voz fora do padrão

**Voz dominante:** dialógica-mecanística, com perguntas operacionais ("o que separa um inibidor de qualquer outra molécula?"). É voz NEBLI canônica.

**Citações fora do padrão (raros desvios):**

- p.5: "Note como o captopril foi desenhado para imitar a porção C-terminal do substrato natural da ECA — esse tipo de drug design por análogo estrutural é o paradigma dos inibidores competitivos." — voz de **legenda de figura**, mas aparece como parágrafo solto na p.5. Aceitável; provavelmente legenda que migrou para corpo.
- p.16: "[…] e em geral há inibidores específicos circulando para conter ativação prematura." — uso de "em geral" é vago. Voz NEBLI prefere afirmação + qualificador específico ("e a célula sintetiza inibidores específicos — SPINK1 no pâncreas, antitrombina no sangue — justamente para conter ativação prematura").
- p.17 (conclusão): "Mecanismo primeiro, nome depois — e cada nome ganha sentido como consequência do mecanismo, não como rótulo a memorizar." — voz de **manifesto pedagógico**, aparece na conclusão integradora. Ok como fechamento; mas é a única frase do PDF que sai do registro descritivo-mecanístico para meta-pedagogia. Diga-se: bem colocada.

**Veredito:** desvios são poucos e não comprometem. Voz consistente.

---

## 6. T3.7 — Carga cognitiva de pico

**Seção-pivô:** **p.7 — acompetitiva + Le Chatelier + tabela 4 tipos** (já identificada em §1 e §4). Esta é a página onde o capítulo inteiro vive ou morre: se o aluno entende o gesto Le Chatelier, ele entende a régua única do capítulo.

**3 mitigações concretas:**

1. **Reescrita do parágrafo Le Chatelier** (Parágrafo fraco 1, §3) com ponte numérica para KM operacional.
2. **Quebra de página antes da tabela 4 tipos**, com a tabela em página própria com layout limpo (sem quebra de palavra "estacionária") e a coluna "Onde liga + em qual estado" como **primeira coluna** (operacionalizando a régua única do capítulo).
3. **Mover mapa conceitual da PARTE I para o fim da PARTE I**, ou substituí-lo por **matriz 2×2 real** com eixos "onde liga" × "qual estado".

**Qual escolher:** **(1) + (3)** combinados. (1) resolve o mecanismo; (3) resolve a sistematização. (2) é cosmético — útil mas secundário.

---

## 7. T3.8 — ANÁLISE VISUAL

Análise inferida do JSON estrutural (40 páginas, 12 imagens, média 310 palavras/pág, distribuição: imagens concentradas nas páginas 4-16; páginas 17-40 zero imagens) + Pontos de Parada visuais detectados no texto extraído.

### Hierarquia tipográfica

- Capa (p.1): bloco meta canônico (Disciplina · Nota de uso · Onde estudar). Nota de uso ocupa ~50% da capa — boa decisão editorial (vacina contra erro de decoreba já na capa).
- Headers de PARTE com numeração 1.1, 1.2, 2.1 etc — hierarquia legível.
- Quebra de fonte/tamanho nos boxes de atenção (`box "Não confunda…"`) — bem demarcados.
- **Bug detectado:** tabela p.7 com hifenização "esta- / cionária" no meio da palavra na célula KM da linha "Irreversível" — quebra a leitura.

### Valor pedagógico das figuras

- 12 imagens no PDF (slides do professor + diagramas). Concentradas em PARTES I-III.
- Cada figura tem **legenda integrada** ao corpo do texto (não decorativa) — ex.: "Note como o captopril foi desenhado para imitar a porção C-terminal…" é literalmente a legenda funcionando como ancoragem do conceito.
- **Lacuna grave:** **a cascata AMPc-PKA (p.13) NÃO tem figura.** Cadeia de 7 passos textual, sem ilustração. Pelo canônico NEBLI (`cadeia multi-passo ≥5 reações = figura obrigatória`), isso é erro mecânico.
- Mapas conceituais (p.8, p.12, p.17) são figuras **decorativas** — sem eixo classificatório, sem setas-de-mecanismo. Ocupam espaço sem carregar informação além do texto. O NEBLI já aboliu esses em 2026-05-19; esta apostila histórica os mantém.

### Densidade visual (respiro vs muros)

- Distribuição de palavras por página: mediana ~340, pico 468 (p.19), vale 82 (p.40 = só gabarito).
- Páginas 19-32 (Etapa 2) têm densidade homogênea ~300 palavras + zero imagens — **muro de questões**, esperado para banco. Aceitável.
- Página 7 (acompetitiva + Le Chatelier + tabela + mapa) tem **densidade conceitual** alta sem alívio visual — é o pico real de carga cognitiva.

### Uso de cor

- Inferido: faixa navy na capa (padrão NEBLI), badges de categoria (consolidação/integração/aplicação) nas questões, banner gold no Resumindo.
- Não foi possível inspecionar paleta diretamente (ferramenta de leitura visual do PDF não disponível na sessão). Crítica baseada em inferência do template `nebli_v2_apostila.typ`.

### Cortes / overflow

- **Bug confirmado:** tabela p.7 com palavra quebrada "esta- / cionária" — cell overflow tratado por hifenização agressiva.
- **Bug confirmado:** gabarito p.40 com layout em 5 colunas com ordem embaralhada (Q11 separada de Q12; Q16/Q17 voltam ao layout esperado). Possivelmente float/wrap mal-configurado.
- Numeração: PDF tem 40 páginas físicas, mas a última página é numerada "45" (visível no extrato). Discrepância de 5 — provavelmente Etapa 4 vazia foi gerada e depois removida sem renumeração.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### Técnica 1 — **Régua única declarada na abertura e amarrada na conclusão**

**Citação literal (p.3):**
> "O fio mecanístico aqui é simples e poderoso: toda manipulação enzimática mexe em duas alavancas, KM e Vmax, e a marca de cada mecanismo é qual delas muda e em qual direção."

**Citação espelho (p.17, conclusão):**
> "Um aluno que sai daqui com esse gesto consegue ler qualquer farmacologia nova só pela cinética: AAS é covalente (irreversível), captopril compete pelo sítio (KM sobe, Vmax fica), lítio só pega ES (Vmax e KM caem juntos)…"

**Nome da técnica:** "régua única declarada-e-amarrada" — uma única pergunta organizadora (aqui: "onde liga + em qual estado") é declarada na abertura como gesto, recapitulada no fim de cada subseção (cada "Resumindo até aqui:") e amarrada na conclusão com **exemplos farmacológicos concretos diferentes dos usados no corpo**.

**Quando NEBLI deveria usar:** sempre que um capítulo tem **N sabores aparentemente independentes** (inibições, transportes de membrana, hipersensibilidades, ciclos metabólicos). O REDATOR-E1 deve declarar a régua no Tema Card Seção A como "fio único do capítulo" e o COMPILADOR deve verificar a presença da régua na **abertura + conclusão + cada Resumindo-até-aqui**. Gancho concreto para REDATOR-E1: regra inegociável nova ("toda PARTE com ≥3 subtipos exige declaração de régua única na abertura, recapitulada na conclusão integradora").

### Técnica 2 — **"Resumindo até aqui" inline + clínica imediata como ancoragem**

**Citação literal (final de 1.1, p.4):**
> "Resumindo até aqui: Irreversível = ligação covalente, inativa permanentemente aquela molécula de enzima. Recuperação clínica depende da síntese de enzima nova. Exemplos: AAS-COX, penicilina-transpeptidase, AZT-transcriptase, DFP-AChE."

**Nome da técnica:** "mini-resumo com pares droga-alvo nominais" — cada subseção fecha com **uma frase de mecanismo + uma frase de consequência clínica + lista nominal de 3-4 pares droga-alvo concretos**.

**Quando NEBLI deveria usar:** o REDATOR-E1 NEBLI já tem regra de "mini-resumos" mas geralmente entrega **só o mecanismo abstrato**. A novidade aqui é o **par droga-alvo nominal** (AAS-COX, penicilina-transpeptidase, AZT-transcriptase) que dá ao aluno **3 ganchos para a memória de longo prazo em 4 segundos de leitura**. Gancho concreto: regra para REDATOR-E1 ("todo mini-resumo `Resumindo até aqui:` deve terminar com ≥3 pares concreto-clínico, formato `droga-alvo` ou `condição-mecanismo`").

### Técnica 3 — **Box anti-confusão posicionado *imediatamente* depois do erro provável**

**Citação literal (p.6, depois de explicar não-competitiva):**
> "[Box] Não-competitivo NÃO é deslocável por [S] alto / Aluno tende a estender a regra do competitivo: 'se eu dou mais substrato, ganho da inibição'. Para não-competitivo é falso. Como ele liga em sítio diferente, [S] alto não o desloca, e Vmax permanece reduzido para sempre — enquanto inibidor estiver presente."

**Nome da técnica:** "box anti-extrapolação imediato" — o aluno acabou de aprender a regra X (competitivo é deslocável por [S]) e a próxima seção apresenta um caso onde X **não vale**. Em vez de deixar o aluno cair na armadilha, o autor coloca um **box explicitando o erro de extrapolação esperado** logo depois da apresentação do tipo-novo. Não é "atenção, vai cair na prova"; é "**eis o erro mental que você está prestes a cometer ao estender a regra anterior**".

**Quando NEBLI deveria usar:** sempre que um capítulo apresenta **N tipos sequencialmente** e a transição entre tipos induz a um erro de extrapolação. O REDATOR-E1 deve identificar no Tema Card Seção C os "erros de extrapolação esperados" entre subtipos consecutivos e posicionar `#armadilha-box` **imediatamente após o segundo subtipo** (não no fim da seção, não em apêndice). Gancho concreto: regra inegociável nova ("toda PARTE com ≥2 subtipos sequenciais exige ≥1 box anti-extrapolação no momento exato da transição").

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro | Status na apostila | Evidência |
|---|---|---|---|
| 1 | Paridade de distratoras em E2 Aplicação | **AUSENTE** (apostila acerta) | Q26: ratio correta/maior distratora ≈ 1.11 (≤1.25). Q27, Q30 com distratoras em 35-50 palavras, paridade respeitada. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PRESENTE** | cAMP/AMPc, PKA, ATP, ADP, Pi, NADH não recebem footnote `#sigla()` próprio na 1ª aparição (p.13 — cascata). ECA, MTX, AAS, AZT, DFP, ATP, LDH, CK, SPINK1 estão com footnote. **Faltam: cAMP/AMPc, PKA, fosforilase quinase (não tem sigla mas merece termo-nota).** |
| 3 | Subagentes Opus customizados (loops/contaminação) | **N/A** | Apostila histórica, fora do pipeline NEBLI atual. |
| 4 | Heredoc atômico `ENAMETOOLONG` no Windows | **N/A** | Pipeline de geração não inspecionado nesta revisão. |
| 5 | `questao-ce` exige tupla `("I", [conteúdo])` | **N/A (não detectado)** | CEs presentes (Q03, Q06, Q13, Q17, Q22). Como o PDF compilou e renderizou corretamente, presume-se que a tupla está no formato canônico — sem erro de runtime. |
| 6 | Termo-notas abaixo do alvo (6-8) | **AUSENTE** (apostila acerta) | Conta nos footnotes do texto extraído: 1=inibição reversível, 2=inibição irreversível, 3=AAS, 4=AZT, 5=DFP, 6=inibidor competitivo, 7=ECA, 8=MTX, 9=inibidor não-competitivo, 10=inibidor acompetitivo, 11=pH ótimo, 12=enzima alostérica, 13=sigmoide, 14=modelo concertado, 15=modelo sequencial, 16=modificação covalente reversível, 17=quinase, 18=fosfatase, 19=cascata de amplificação, 20=Isozimas, 21=LDH, 22=CK, 23=zimogênio, 24=enteroquinase, 25=caspases. **25 footnotes** — muito acima do alvo (que mistura siglas + termos-nota). Nenhum risco de subdotação. |
| 7 | Tema-card com teto E1 errado | **N/A** | Apostila histórica de outro autor; teto canônico (22 pág atual) não se aplica retroativamente. PDF tem 40 págs totais; PARTE textual (E1 + Resumindo) ocupa páginas 3-18 = **16 páginas**, dentro do canônico (piso 2, teto 22). |

**Síntese:** dos 7 erros NEBLI, apenas o **#2 (siglas sem `#sigla()` na 1ª aparição)** está presente e é acionável. Os demais são ausentes (apostila acerta) ou N/A (fora do escopo).

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)

1. **Remover "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" do sumário (p.2) e do header do gabarito (p.40).** Etapa 4 foi removida do canônico em 2026-05-22; deixar referências quebra a confiança do aluno na completude da apostila. Renumerar para que a página final marque "40" e não "45".
2. **Reordenar gabarito (p.40) em 3 colunas com sequência linear** (Q01-Q10 col-1, Q11-Q20 col-2, Q21-Q30 col-3) em vez do layout 5-colunas embaralhado. Fricção de busca elimina valor da página de gabarito.
3. **Inserir figura da cascata AMPc-PKA (p.13)** com aritmética visível de amplificação. Sete passos textuais sem figura quebram o canônico "cadeia multi-passo ≥5 reações = figura obrigatória".

### MECANÍSTICO (max 3)

1. **Reescrever o parágrafo Le Chatelier do acompetitivo (p.7)** com ponte numérica explícita entre "equilíbrio puxado pra frente" e "KM aparente (= [S] para meia-Vmax) cai porque agora basta menos [S] para gerar a mesma quantidade de ES". Sem essa ponte, o gesto-pivô do capítulo vira dogma.
2. **Detalhar a aritmética da cascata AMPc-PKA (p.13)** passo-a-passo: ganho por degrau (×10² no receptor → cAMP, ×10 cAMP → PKA, ×10 PKA → fosforilase quinase, ×10² fosforilase quinase → glicogênio fosforilase). O 10⁶ não pode ser declarado como mágica; deve ser construído.
3. **Trazer Vmax e KM na mesma proporção para a frente do parágrafo acompetitivo (p.7)**, não relegada para parágrafo subsequente. A frase "Vmax e KM caem juntos, na mesma proporção" é a frase-tese do tipo e deve estar nas primeiras 4 linhas do tópico, não nas últimas.

### DIDÁTICO (max 3)

1. **Substituir mapas conceituais decorativos (p.8, 12, 17) por matriz 2×2 real** com eixo "onde liga" × "qual estado", ou remover. Mapas atuais não carregam informação além do texto — ocupam espaço.
2. **Adicionar `#sigla()` para cAMP/AMPc, PKA, ATP, ADP, NADH na 1ª aparição** (p.13 principalmente). Lista padrão de siglas que passam despercebidas (canônico erro #2).
3. **Reduzir SPINK1 de 2 questões (Q21+Q28) para 1**, liberando uma vaga para outro mecanismo subexplorado (sugestão: alostérico heterotrópico ATP/AMP — única vez que aparece é Q20). Ou um caso clínico de organofosforado mais nuançado (Q27 é OK mas só toca pralidoxima de leve).

### ESTÉTICO (max 3)

1. **Corrigir a quebra de palavra "esta- / cionária" na tabela 4-tipos (p.7).** Bug visual numa tabela-pivô.
2. **Verificar consistência da numeração de páginas** (PDF físico 40 vs marca "45"). Discrepância indica resíduo de Etapa 4 removida.
3. **Considerar pagebreak antes de Etapa 2 (p.19)** para garantir que Resumindo termina em página própria e Q01 abre em página nova. (Pode já estar ok; conferir visualmente.)

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM, com reservas.** Apostila é um dos melhores exemplos disponíveis de organização por régua única + mini-resumos + box anti-extrapolação. Técnicas T3.9 #1, #2 e #3 (régua única, par droga-alvo nominal, box anti-extrapolação imediato) merecem promoção para EXEMPLARES.md como **3 novos exemplares**.

2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM.** Três estruturais (sumário/gabarito, layout do gabarito, figura cascata ausente) e três mecanísticos (Le Chatelier sem ponte numérica, aritmética da cascata, ordem da frase-tese do acompetitivo).

3. **Seção para refazer?** **Nenhuma seção inteira.** Mas a **p.7 (acompetitiva + Le Chatelier + tabela)** precisa de reescrita parcial substancial — o Le Chatelier merece 3-4 frases extras com ponte numérica, e a tabela precisa de layout limpo. É a página-pivô do capítulo.

4. **Parágrafos para reescrever?** **3** (todos identificados em §3): (a) Le Chatelier acompetitivo p.7; (b) Cascata AMPc-PKA p.13; (c) Mapas conceituais decorativos p.8/p.12/p.17 (substituir ou remover).

---

[APROVAR COM RESERVAS]

<!-- FIM-REVISAO-PROFUNDA-UC01-BIOQ-11-ENZIMAS-II -->
