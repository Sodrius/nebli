# Revisão profunda Tier 3 — UC01-FMEMB-08-sinalizacao-celular-i-e-ii

**Tema (ancoragem):** Sinalização Celular I e II — UC01 FMEMB aula 08
**Conceitos que EU-aluno gostaria de aprender:** (1) por que a célula tem quatro famílias de receptor em vez de uma só — o que cada prazo de resposta resolve; (2) como o ciclo GTP/GDP transforma binding extracelular em ativação enzimática intracelular sem o receptor "entrar"; (3) por que IP3 e DAG, vindos do mesmo PIP2 e da mesma PLC, executam coisas diferentes — e como o Ca²⁺ amarra os dois.
**Temas vizinhos que NÃO são esse:** (a) transmissão sináptica clássica (sinapse química detalhada com vesícula/SNARE) — aqui só toca tangencialmente nos receptores-canal; (b) cascata de coagulação ou cascata do complemento — também são "sinalização", mas não é o recorte.
**Autor:** Italiano (rotulagem do batch histórico — PDF datado, footer Davi Sousa)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25
**Observação operacional:** análise visual feita por inferência a partir do .txt extraído + JSON estrutural (pdftoppm presente no sistema mas indisponível para Read em sandbox; render direto do PDF bloqueado). Páginas-amostra inspecionadas: 1, 2, 4, 5, 19, 26, 48 — via .txt linha-a-linha.

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão (voz aluno) |
|---|---|---|---|
| Capa + nota de uso | PASSA | 1 | Tema na capa, contexto claro. Vou em frente. |
| Sumário | PASSA | 2 | Hierarquia das 3 PARTES legível, prazo-por-família já anunciado no subtítulo. |
| Abertura da E1 (intro-box) | PASSA | 3 | "bilhões de células precisam combinar comportamento" é um gancho que entendo. |
| 1.1 — gap, contato, parácrina, endócrina, autócrina | PASSA com nota | 3-5 | Fluido. Para um instante em "AMPc passa pela junção gap (até 1 kDa)" — não sei o que é kDa em contexto, mas a footnote 1 me salva. |
| 1.2 — quatro famílias + tabela | PASSA | 6-8 | Tabela "Família × Localização × Mecanismo × Tempo × Exemplos" é o mapa que eu queria. Aqui já entendi o esqueleto da aula. |
| 1.3 — receptores-canal | PASSA | 8-9 | NMDA como "detector de coincidência" — clic instantâneo. Boa. |
| 2.1 — ciclo GTP/GDP | **[STOP: pág 10]** | 10 | "A subunidade α tem um sítio que liga nucleotídeo de guanina: ou GDP (forma inativa) ou GTP (forma ativa)." Eu paro porque o GEF aparece embutido no texto sem o aluno-em-dificuldade saber o que é "GEF — fator de troca". O parêntese diz o que faz mas o nome vem antes do mecanismo digerido. Leio de novo, entendo, sigo — mas perdi 30 segundos. |
| 2.2 — AMPc/PKA | PASSA com nota | 11-13 | "Quatro AMPc liberam duas subunidades catalíticas — a estequiometria preserva o caráter de 'interruptor' em vez de regulação contínua." Frase ótima. Aprendi. |
| 2.3 — IP3/DAG | PASSA | 13-15 | "PKC clássica precisa de DAG E Ca²⁺ — os dois braços da via Gq convergem nela" — fixou. |
| 2.4 — Cálcio como hub | **[STOP: pág 16]** | 16 | "Subir de 100 nM para 1 µM é 'só' 0,001 mM em valor absoluto — quase nada para um íon — mas é dez vezes o basal." Eu paro porque tenho que mentalizar 100 nM, 1 µM e 1 mM ao mesmo tempo. O argumento é bom mas eu queria uma frase âncora primeiro ("o sistema lê razão, não concentração"). Quando volto a ler do começo do parágrafo, entendo. Reentrada custosa. |
| 3.1 — RTK / insulina | **[STOP: pág 18-19]** | 18-19 | A enumeração paralela das três cascatas (Ras/Raf/MEK/ERK, PI3K/Akt, PLC) num parágrafo único de 7 linhas, sem mini-resumo, é onde eu travo. Lá vêm 4 siglas novas em 2 linhas (Ras, Raf, MEK, ERK). Olho a footnote — não tem. Diferente do resto do PDF, aqui o autor abandonou a regra de explicar mecanismo antes de jargão. Levo 1 minuto para decidir se preciso decorar isso ou só guardar "RTK ativa três coisas em paralelo". |
| 3.2 — NO e esteroides | PASSA | 19-20 | Cascata NO ótima. Box do sildenafil ancora. |
| 3.3 — modulação | PASSA | 21-23 | Crosstalk + dessensibilização explicados em registro firme. |
| Conclusão integradora | PASSA | 24 | Tece as 4 famílias com prazos. Sólido. |
| Resumindo (2 págs) | PASSA com nota | 25-26 | 2 páginas em vez de 1 — sou aluno em dificuldade, prefiro 2 com respiro a 1 esmagada. Sem objeção. |
| E2 — 30 objetivas | PASSA | 27-44 | Distratoras gordas em todas as Aplicação (Q26-Q30). |
| E3 — 5 discursivas | PASSA | 45-47 | Modelos de resposta sólidos. |
| Gabarito final | **[STOP visual: pág 48]** | 48 | O gabarito vem em layout de 3 colunas com quebras estranhas ("Q15 CEEC", "Q20 A", "Q25 C" misturados com "Q29 C  Q30 B" embaixo). Não tenho certeza imediata da ordem. Se eu estou consultando rápido depois de responder, perco tempo. |

**Total STOPs:** 4 (pp. 10, 16, 18-19, 48). Nenhum fechou o PDF — todos foram releitura curta, exceto p. 18-19 que custou ~1 minuto.

---

## 2. T3.1 — Comparação com EXEMPLARES.md

### Categoria 1 — Explicação mecanística parágrafo-por-parágrafo

**Exemplar NEBLI canônico (1.1, Transmissão Sináptica):**
> "Existem duas grandes famílias de receptores. Os **receptores ionotrópicos** são canais iônicos que abrem quando o neurotransmissor se liga — eles *são* o canal. A resposta é rápida (milissegundos) porque não há intermediários. Os **receptores metabotrópicos** são acoplados a proteínas G e ativam cascatas intracelulares que, eventualmente, modulam canais ou enzimas."

**Trecho equivalente neste PDF (p. 6-7):**
> "Receptores-canal (ionotrópicos) — o receptor é um canal iônico. Quando o ligante chega, o canal abre, íons passam, e a célula muda de potencial. Resposta extremamente rápida (milissegundos), sem intermediários. (...) Receptores acoplados a proteína G (GPCR, metabotrópicos) — o receptor não é canal nem enzima; ele é um intermediário que, ao receber o ligante, ativa uma proteína G na face citoplasmática da membrana."

**Veredito:** PARIDADE. Ambos abrem com "o receptor *é* o canal" e ancoram o prazo (milissegundos) ao mecanismo (ausência de intermediário). O PDF histórico vai um passo além ao explicitar amplificação como vantagem do GPCR ("um receptor ativa várias proteínas G; cada uma ativa várias enzimas") — algo que o exemplar 1.1 implicita mas não detalha. **Esse padrão deveria ser absorvido no exemplar canônico NEBLI: explicitar a aritmética da amplificação no momento da apresentação da família.**

### Categoria 6 — Organização terminológica (família com nomenclatura ramificada)

**Trecho do PDF (p. 11-12), tabela Gs/Gi/Gq:**
> "Gs (estimuladora) — Estimula adenilato ciclase — ↑AMPc — β-adrenérgicos, glucagon, ACTH, dopamina D1
> Gi (inibitória) — Inibe adenilato ciclase — ↓AMPc — α2-adrenérgico, muscarínico M2, opioides, dopamina D2
> Gq — Ativa PLC — IP3 + DAG → Ca²⁺ e ativa PKC — α1-adrenérgico, muscarínico M1/M3, angiotensina, vasopressina V1"

**Comparação com EXEMPLAR 17 (catálogo de família GLUTs):** mesma estrutura (família × função × isoformas × tecido), mesma economia visual. **PARIDADE forte.** O PDF inclusive faz algo que o exemplar 17 ainda não tem: a frase de fechamento "A mesma adrenalina, ligando-se a um β1 (cardíaco, Gs) acelera o coração, e a um α1 (vaso periférico, Gq) contrai o vaso. Mensageiro idêntico, receptores diferentes, proteínas G diferentes, respostas opostas" — que reaproveita a tabela em um caso clínico de comparação direta. **NEBLI deveria copiar essa técnica de "tabela + parágrafo de uso comparativo concreto" como parte do exemplar 17.**

### Onde o PDF fica ABAIXO do exemplar

**Categoria 11 — Distratores mecanísticos**: o exemplar canônico pede distratoras de 25-35 palavras com mecanismo plausível-mas-errado retirado do mapa de confusões. O PDF cumpre em 28/30 questões. As duas exceções estão na Q07 e Q11 (Consolidação) — distratoras como Q07-E ("Gi ativa a adenilato ciclase tal como Gs, e Gq inibe a fosfolipase C; nenhuma das três atua sobre o conteúdo de Ca²⁺ do retículo") são longas mas pouco verossímeis — o erro é grosseiro demais, não confunde aluno preparado. **Fica abaixo do padrão NEBLI** (que pede confusão real, ex.: "Gi inibe ciclase só sob ATP alto", não "Gi ativa ciclase").

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo 1 — Cascatas paralelas do RTK (p. 18, último parágrafo de 3.1)

**Citação literal:**
> "A partir daí, várias cascatas podem ser disparadas em paralelo, dependendo de quais adaptadoras a célula expressa: a via Ras/Raf/MEK/ERK (MAPK), associada a crescimento e divisão; a via PI3K/Akt, associada a sobrevivência e metabolismo; a via PLC, que produz IP3 e DAG (essa converge com Gq!). Um único RTK ativado pode disparar várias respostas em paralelo — por isso a sinalização por fatores de crescimento é tão rica e tão suscetível a ser sequestrada em câncer (mutações que ativam permanentemente um RTK ou um efetor do RTK estão entre as causas mais comuns de tumores sólidos)."

**Diagnóstico mecanístico:** 6 siglas novas (Ras, Raf, MEK, ERK, MAPK, Akt) entram juntas no mesmo período sem footnote nem definição inline. O aluno em dificuldade não sabe distinguir "via Ras/Raf/MEK/ERK" de "via MAPK" — são a mesma coisa (MAPK é o nome da via, Ras→Raf→MEK→ERK é a sequência), mas o texto não esclarece. Quebra a regra da própria apostila ("mecanismo antes do jargão"). Carga cognitiva pico do PDF inteiro. Sem mini-resumo de encerramento.

**Reescrita pronta:**
> "A partir daí, várias cascatas podem ser disparadas em paralelo, dependendo de quais adaptadoras a célula expressa. A mais conhecida é a cascata das **MAP-quinases (MAPK)** — uma fila de fosforilação onde uma quinase ativa a próxima: a pequena GTPase Ras dispara Raf, que ativa MEK, que ativa ERK, e ERK finalmente entra no núcleo e liga genes de proliferação. É a via clássica de crescimento e divisão. Em paralelo, o RTK pode ativar **PI3K/Akt** (cascata de sobrevivência e captação de glicose — central na ação da insulina) e a **PLC**, que produz IP3 e DAG do mesmo jeito que a Gq faria — exemplo clássico de crosstalk entre famílias. *Em resumo: um RTK fosforilado é um hub que aciona crescimento (MAPK), sobrevivência (PI3K/Akt) e cálcio (PLC) ao mesmo tempo.* Por isso a sinalização por fatores de crescimento é tão rica — e por isso mutações que travam um RTK ou um efetor a jusante (como Ras) estão entre as causas mais comuns de tumores sólidos."

### Parágrafo 2 — Magnitudes do Ca²⁺ (p. 15-16)

**Citação literal:**
> "Por que importa que o basal seja tão baixo? Porque qualquer entrada moderada de Ca²⁺ vira um pulso enorme em termos relativos. Subir de 100 nM para 1 µM é 'só' 0,001 mM em valor absoluto — quase nada para um íon — mas é dez vezes o basal, e o sistema é calibrado para essa razão. Sinal bom é razão alta sobre baixo ruído."

**Diagnóstico mecanístico:** o argumento é correto e elegante, mas a montagem cognitiva exige o aluno converter 3 unidades (nM, µM, mM) no mesmo período. Para aluno em dificuldade, isso pesa. Falta a frase-âncora antes da matemática.

**Reescrita pronta:**
> "Por que importa que o basal seja tão baixo? **Porque o sistema de Ca²⁺ não lê concentração absoluta — lê razão.** Subir de 100 nM para 1 µM é um aumento de dez vezes (10×). É esse fator de dez que as proteínas-leitoras (calmodulina, troponina) usam para decidir se 'o sinal chegou'. Se o basal já fosse alto — digamos 100 µM — uma entrada extra de 1 µM seria diluída no ruído. Ao manter o basal absurdamente baixo, a célula transforma uma entrada pequena em valor absoluto (~1 µM = 0,001 mM, quase nada para um íon) num pulso enorme em valor relativo. Sinal bom é razão alta sobre baixo ruído — e a célula gasta ATP continuamente (bombas SERCA, PMCA) só para manter essa razão disponível."

### Parágrafo 3 — Diabetes tipo 2 (p. 19, box)

**Citação literal:**
> "A insulina sinaliza por receptor RTK. No tipo 2, o receptor existe e a insulina circula — em concentrações até mais altas que o normal —, mas a cascata pós-receptor responde mal. Um dos mecanismos é a fosforilação inibitória em serinas da IRS-1 (a primeira adaptadora da cascata da insulina) por outras quinases como JNK, ativadas em ambiente inflamatório (obesidade, ácidos graxos livres). Sem IRS-1 funcional, o sinal não desce até o GLUT-4, que é a peça que de fato leva a glicose para dentro da célula muscular."

**Diagnóstico mecanístico:** JNK aparece sem footnote, sem definição inline, e sem explicação de por que esta quinase específica está ativa em obesidade. "Em ambiente inflamatório" é vago — o aluno não sabe que TNF-α e IL-6 ativam JNK; pode achar que "inflamatório = neutrófilo no tecido". A frase "Sem IRS-1 funcional, o sinal não desce até o GLUT-4" usa "IRS-1" pela 2ª vez mas a 1ª aparição (IRS-1) entrou direto, sem expandir o que significa (insulin receptor substrate 1).

**Reescrita pronta:**
> "A insulina sinaliza por receptor RTK. No diabetes tipo 2, o receptor existe e a insulina circula — em concentrações até mais altas que o normal —, mas a cascata pós-receptor responde mal. O ponto de quebra é a **IRS-1 (insulin receptor substrate 1)** — a primeira proteína adaptadora que pega o sinal da cauda do receptor e o propaga pra dentro. Em obesidade, o tecido adiposo libera citocinas inflamatórias (TNF-α, IL-6) e ácidos graxos livres que ativam quinases de estresse como a **JNK** (c-Jun N-terminal kinase). A JNK fosforila a IRS-1 em serinas — e essa fosforilação em serina, em vez de ativar, *desliga* a IRS-1 para tirosinas (compete com o sítio de fosforilação ativadora). Sem IRS-1 ativa, o sinal não desce até a via PI3K/Akt — que é quem normalmente translocaria o **GLUT-4** (transportador de glicose) das vesículas intracelulares para a membrana plasmática. Resultado: insulina circulante alta, GLUT-4 parado dentro da célula, glicemia alta — a definição operacional de resistência à insulina."

---

## 4. T3.3 — 3 seções mais densas (mitigação concreta)

### Densa 1 — Tabela das 3 proteínas G + 1.5 página de detalhes (p. 11-13)
**Densidade:** introduz Gs, Gi, Gq, AMPc, GMPc, PKA, PKC, PDE, sildenafil, milrinona, teofilina em 2 páginas. **Mitigação:** quebrar 2.2 em duas sub-seções: 2.2a (AMPc/PKA — mecanismo puro) e 2.2b (Box farmacológico — sildenafil/milrinona/teofilina como aplicação derivada). Não acrescenta páginas, distribui a carga.

### Densa 2 — Página 19 (Cálcio como hub, 535 palavras, zero imagens conforme JSON)
**Densidade:** é a página mais densa do PDF inteiro em palavras absolutas (535) e tem zero figura. Discute 5 fontes de Ca²⁺ + calmodulina + CaMKII + LTP. **Mitigação:** inserir uma figura simples (4 setas: VDCC, NMDA, IP3R, RyR → citosol; calmodulina lendo; CaMKII executando). O autor já fez figura análoga em p. 15-16 (rotas de Ca²⁺) — replicar/expandir lá para cobrir o ponto da p. 19 que ficou textual demais.

### Densa 3 — Parágrafo das 3 cascatas RTK paralelas (p. 18, já triangulado em §3 acima)
**Mitigação:** ver reescrita do §3 parágrafo 1.

---

## 5. T3.4 — Voz fora do padrão (citações)

Voz é extremamente consistente em todo o PDF — registro dialógico, sujeito-verbo-complemento, perguntas retóricas funcionais. Encontrei **dois deslizes pontuais** para registro de livro-texto:

1. **p. 18 (cascatas RTK)** — "várias cascatas podem ser disparadas em paralelo, dependendo de quais adaptadoras a célula expressa" — voz passiva + lista enxuta, é o único parágrafo do PDF onde a voz cai para registro de manual. (Já triangulado.)

2. **p. 11, tabela Gα** — a tabela em si é boa, mas a frase que a antecede ("Existem três famílias principais de Gα, e a diferença entre elas determina toda a fisiologia da sinalização que veio adiante") é o único momento em que o autor "promete" sem reformular a partir da curiosidade do aluno. Comparar com a abertura de 2.1 ("Sai-se da família mais simples (canal) para a mais numerosa e mais farmacológica") — esta é dialógica; aquela é de prefácio.

Fora desses dois, voz canônica em 100% do PDF.

---

## 6. T3.7 — Carga cognitiva pico (seção-pivô)

**Seção-pivô:** 3.1 — RTK e o exemplo da insulina (pp. 17-19).

**Por que é o pico:** carrega simultaneamente (a) estrutura nova (dímero α₂β₂ vs dímeros induzidos), (b) novo modo de transdução (autofosforilação trans, fosfotirosina como sítio de encaixe), (c) três cascatas paralelas (MAPK, PI3K/Akt, PLC) com 6 siglas novas em 2 linhas, (d) aplicação clínica densa (diabetes tipo 2 com JNK, IRS-1, GLUT-4).

**3 mitigações possíveis:**

1. **Quebrar 3.1 em 3.1a (estrutura+dimerização+autofosforilação) e 3.1b (cascatas a jusante e clínica).** Inseri um respiro entre os dois blocos, com uma figura ou um mini-resumo explícito.

2. **Adicionar figura de cascata MAPK** (Ras → Raf → MEK → ERK) — uma única imagem resolveria 4 das 6 siglas que hoje aparecem soltas no parágrafo.

3. **Reescrever o parágrafo das cascatas (já fiz a reescrita no §3 acima)** — explicar inline o que é cada via antes de listar, fechar com frase-âncora.

**Qual escolher:** opção 3 (reescrita inline + frase-âncora) é a mais barata e a que mais respeita a arquitetura do PDF. Opção 2 (figura) é o segundo movimento se ainda assim ficar denso na revisão visual. Opção 1 (quebrar seção) só se as outras duas falharem — quebrar a seção desfaz uma boa unidade conceitual ("RTK + insulina é um pacote").

---

## 7. T3.8 — ANÁLISE VISUAL

*Análise por inferência a partir de .txt + JSON. PDF não renderizado (pdftoppm indisponível no sandbox).*

### 7.1 Hierarquia tipográfica
**Inferência (pelos marcadores do .txt):** "N E B L I" como header espaçado em toda página → footer com número de página direita; "ETAPA 1 — TEXTO DIDÁTICO" como subheader; "PARTE I/II/III" como título grande; subtópicos numerados (1.1, 1.2). **Quatro níveis hierárquicos visíveis** — adequado.

### 7.2 Valor pedagógico das figuras
JSON: 14 imagens em 48 páginas, todas concentradas nas pp. 3-23 (E1). E2/E3 sem figuras (correto — conteúdo de prova).

Legendas extraídas pelo .txt sugerem que as figuras **estão integradas argumentativamente** ("Junções gap em ação: cada conexon é um cilindro de seis conexinas...", "Receptor de sete hélices transmembrana com a proteína G trimérica..."). Padrão é "figura ilustra o parágrafo anterior e o seguinte ancora a próxima ideia" — equivalente ao padrão NEBLI.

**Ponto fraco identificado:** p. 19 (Cálcio, 535 palavras) sem figura. É a página mais densa em palavras absolutas; mereceria diagrama das 4 fontes de Ca²⁺.

### 7.3 Densidade visual
Médias do JSON: 292 palavras/página. Páginas de E1 variam 86-535 palavras (média ~330 quando tira capa/sumário); páginas E2/E3 ~250-300. **Distribuição saudável**, mas pp. 19 (535) e 24 (410 — Conclusão integradora) são picos. Conclusão integradora densa é OK (é fechamento); p. 19 é onde o leitor já está sob carga e leva o pior pico — má distribuição.

### 7.4 Uso de cor
Inferência da nomenclatura: "Consolidação (Q01–Q12) — verde / Integração (Q13–Q25) — azul / Aplicação (Q26–Q30) — violeta" + "banner gold" no Resumindo. **Cor por categoria de questão = canônico NEBLI**. Sem indicação de outro uso decorativo de cor no corpo. Coerente.

### 7.5 Cortes/overflow
**Indicação de quebra problemática no Gabarito final (p. 48):** "Q01 B Q02 D Q03 A Q04 E Q05 CCEC / Q06 C Q07 B Q08 ECEC Q09 D Q10 A / Q11 E Q12 C / Q15 CEEC Q16 A Q17 E / INTEGRAÇÃO (Q11–Q25) Q20 A Q21 D Q22 CECE / Q25 C / Q13 B Q14 D Q29 C Q30 B / Q28 E / Q18 ECCE Q19 C". A ordem visual está embaralhada pelas colunas — Q13/Q14 aparecem depois de Q15/Q16/Q17, Q18/Q19 só no final. Aluno consultando o gabarito perde tempo. **Bug de layout do gabarito consolidado — listar em ordem sequencial Q01 → Q30 em coluna única, mesmo que ocupe 1 página inteira.**

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### Técnica 1 — "Tabela + parágrafo de uso comparativo concreto"
**Citação:**
> [Tabela Gs/Gi/Gq na p. 11-12, seguida de:] "A mesma adrenalina, ligando-se a um β1 (cardíaco, Gs) acelera o coração, e a um α1 (vaso periférico, Gq) contrai o vaso. Mensageiro idêntico, receptores diferentes, proteínas G diferentes, respostas opostas. Isso resolve uma confusão que vai aparecer várias vezes: não é o mensageiro que determina o efeito — é o conjunto receptor + proteína G da célula que recebe."

**Nome da técnica:** "Tabela-com-fechamento-clínico-comparativo".

**Quando NEBLI deveria usar:** sempre que o catálogo de família (cat. 17 do EXEMPLARES) tem isoformas com efeitos opostos no mesmo mensageiro. Hoje o exemplar 17 (GLUTs) lista mas não fecha com caso comparativo de "mesmo substrato, isoforma diferente, resposta oposta/diferente". **Gancho para REDATOR-E1:** após qualquer tabela de catálogo, redigir 2-3 frases mostrando o mesmo ligante/substrato com 2 isoformas e os 2 desfechos clínicos. É a operacionalização de "ensinar a confusão antes que ela apareça".

### Técnica 2 — "Frase-conceito que reescreve o mecanismo em uma linha"
**Citação (várias):**
> "A escolha da família é uma escolha de prazo." (p. 7)
> "A hidrólise do GTP é o relógio interno do desligamento." (p. 10)
> "Adenilato ciclase é o acelerador; PDE é o freio sempre acionado." (p. 13)
> "Calmodulina é sensor, CaMKII é enzima." (p. 16)
> "A escolha do mecanismo é a escolha do prazo da resposta." (p. 20)

**Nome da técnica:** "Frase-âncora aforística" — sentença curta (8-15 palavras) que recodifica o mecanismo num modelo cognitivo simples, sem perder rigor. Aparece tipicamente fechando uma seção ou um parágrafo denso.

**Quando NEBLI deveria usar:** ao final de cada subseção de mecanismo, antes do mini-resumo. Hoje o REDATOR-E1 costuma fechar com "Resumindo até aqui:" e listar 3 pontos. Faltam essas frases-âncora aforísticas *dentro* do parágrafo de transição — são o que distingue um resumo "competente" de um resumo "memorável". **Gancho concreto:** acrescentar no `.claude/agents/redator-e1.md` uma regra: "antes do mini-resumo, terminar a explicação com 1 frase-âncora aforística de ≤15 palavras que recodifique o mecanismo central da seção."

### Técnica 3 — "Box farmacológico como caso de teste do mecanismo recém-explicado"
**Citação (p. 13, box sildenafil):**
> "O sildenafil (Viagra) inibe a PDE5, isoforma da fosfodiesterase específica do GMPc no músculo liso do corpo cavernoso. Bloqueando a PDE5, o GMPc gerado pelo NO (vamos ver em 3.2) se acumula, prolongando o relaxamento muscular e a vasodilatação. **Não é um vasodilatador direto — é um inibidor do desligamento do sinal.** Mesma lógica vale para milrinona (inibidor de PDE3, usada em insuficiência cardíaca) e teofilina (inibidor inespecífico de PDEs, usada em asma)."

**Nome da técnica:** "Box farmacológico de inversão" — usa um fármaco para testar se o aluno entendeu o mecanismo. Não é "aplicação clínica genérica"; é "aqui está um caso onde o erro mais comum é confundir agonista direto com inibidor de degradação — e três fármacos do mesmo princípio".

**Quando NEBLI deveria usar:** em todo tema que tem inibidor de degradação (PDE5/sildenafil, IMAO, IECA, acetilcolinesterase). O padrão é (a) introduzir o fármaco, (b) frase-inversão que separa do agonista direto, (c) listar 2-3 outros fármacos do mesmo princípio para mostrar que é família, não exceção. **Gancho para REDATOR-E1:** o template do box `.clinica-box` ganha um sub-padrão "box-de-inversão" para inibidores.

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro | Status no PDF | Evidência |
|---|---|---|---|
| 1 | Paridade de distratoras E2 Aplicação (Q26-Q30) | AUSENTE | Q26 (NMDA/Mg²⁺) correta D: 35 palavras; distratoras 25-40 palavras com mecanismo. Q27-Q30 idem. Ratio < 1.25 em todas. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | AUSENTE (com 1 exceção) | Sistema de footnotes numerados cobre AMPc, ATP, GPCR, RTK, GTP, GDP, PEPS, PIPS, NMDA, AMPA, GABA, PKA, PDE, PLC, PIP2, IP3, DAG, PKC, CaMKII, NO, GMPc, GRK (~22 termos). **Exceção:** Ras, Raf, MEK, ERK, MAPK, Akt entram juntos na p. 18 sem footnote — ver §3 parágrafo 1. |
| 3 | Subagentes Opus customizados falhando | N/A | PDF histórico, não gerado por subagente nesta sessão. |
| 4 | Heredoc ENAMETOOLONG | N/A | PDF histórico externo. |
| 5 | `questao-ce` exige tupla | N/A | PDF já compilado; Q05/Q08/Q15/Q18/Q22 são CE e renderizaram corretamente. |
| 6 | Termo-notas abaixo do alvo (6-8) | AUSENTE | ≥22 termos com footnote — supera o alvo canônico. |
| 7 | Tema-card com teto E1 errado | N/A | Sem Tema Card; PDF histórico. |

**Síntese:** 0 erros presentes, 1 erro parcialmente presente (siglas RTK-cascata na p. 18), 5 N/A. **PDF passa o checklist canônico.**

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Quebrar a página 19 (Cálcio, 535 palavras, zero figura)** inserindo um diagrama das 4 rotas de entrada de Ca²⁺ → citosol → calmodulina → CaMKII. É a única página do PDF onde o leitor sob carga encontra zero ancoragem visual.
2. **Reordenar o Gabarito final (p. 48)** em coluna única sequencial Q01 → Q30. O layout em 3 colunas embaralhou Q13-Q14-Q15 e separou Q18-Q19 do bloco principal — bug de usabilidade do material.

### MECANÍSTICO (max 3)
1. **Reescrever o parágrafo das cascatas RTK paralelas (p. 18)** — 6 siglas (Ras, Raf, MEK, ERK, MAPK, Akt) entram juntas sem footnote nem inline. É o único parágrafo do PDF que abandona a regra "mecanismo antes do jargão". Reescrita pronta no §3 acima.
2. **Expandir o box do diabetes tipo 2 (p. 19)** com a definição inline de IRS-1, JNK e a especificação de TNF-α/IL-6 como fontes da JNK inflamatória. Reescrita pronta no §3 acima.
3. **Adicionar frase-âncora antes da matemática do Ca²⁺ (p. 15-16)**: "O sistema de Ca²⁺ não lê concentração absoluta — lê razão." Reescrita no §3.

### DIDÁTICO (max 3)
1. **Inserir mini-resumo de encerramento no parágrafo de 3.1 RTK paralelas** (já parte da reescrita): "Em resumo: um RTK fosforilado é um hub que aciona crescimento (MAPK), sobrevivência (PI3K/Akt) e cálcio (PLC) ao mesmo tempo."
2. **Diversificar abertura de 2.3** para não espelhar 2.2 — começar com o problema (vaso periférico em adrenalina sobe Ca²⁺ sem AMPc) e só depois apresentar a via Gq.
3. **Acrescentar exemplo clínico integrado ao corpo da PARTE I** (não em box) — ex.: anoikis em câncer invasivo (já citado pp. 4-5, expandir 2 frases) ou histamina/edema na seção parácrina.

### ESTÉTICO (max 3)
1. **Gabarito final em coluna única** (já listado em ESTRUTURAL — overlap).
2. Sem outros achados estéticos relevantes — PDF cumpre o padrão visual do projeto.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM.** Este PDF é um dos exemplares mais fortes do batch histórico inspecionado: voz canônica em 100% do texto, mecanismo antes de jargão (com 1 exceção em p. 18), 22 termos com footnote, paridade de distratoras na E2 Aplicação cumprida, conclusão integradora em camadas. Material adequado para alimentar o EXEMPLARES.md.

2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM.** Dois mecanísticos (parágrafo das cascatas RTK e box do diabetes tipo 2) + um estrutural (gabarito final embaralhado). Nenhum bloqueia a aprovação como referência, mas todos são correções acionáveis.

3. **Seção para refazer?** **Nenhuma seção inteira.** O parágrafo das cascatas RTK paralelas (p. 18) precisa de reescrita pontual. A página 19 (Cálcio) precisa de figura adicional.

4. **Parágrafos para reescrever?** **3 parágrafos** — todos triangulados no §3:
   - p. 18, parágrafo final de 3.1 (cascatas RTK paralelas).
   - p. 15-16, parágrafo da matemática do Ca²⁺.
   - p. 19, box do diabetes tipo 2.

### Lições para o REDATOR-E1 NEBLI (Phase F)

1. **Acrescentar regra "frase-âncora aforística antes do mini-resumo"** (§8 Técnica 2).
2. **Acrescentar sub-padrão "box-de-inversão" para inibidores farmacológicos** no `.clinica-box` (§8 Técnica 3).
3. **Acrescentar à categoria 17 do EXEMPLARES.md o padrão "tabela + parágrafo de uso comparativo concreto"** (§8 Técnica 1).
4. **Atenção operacional:** sempre que uma seção introduzir ≥4 siglas novas no mesmo parágrafo, quebrar em frases curtas com inline-expand OU adicionar footnotes. A regra "mecanismo antes do jargão" é violada exatamente nas seções de cascata-com-múltiplas-quinases (vimos isso em outros temas — Krebs, gliconeogênese — não é exclusividade deste).

---

[APROVAR COM RESERVAS]

Reservas: 3 parágrafos para reescrita pontual (§3) + 1 ajuste de layout (gabarito final) + 1 figura faltante (p. 19). Nenhuma reserva é bloqueante para uso como referência positiva — todas são melhorias acionáveis que, aplicadas, elevariam o material a exemplar canônico do projeto.

--- FIM DA REVISÃO PROFUNDA TIER 3 ---
