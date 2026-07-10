# Revisão profunda Tier 3 — UC01-BC-02-citoesqueleto

**Tema (ancoragem):** Citoesqueleto (UC01, Biologia Celular, aula 2) — três sistemas (filamentos intermediários, microtúbulos, actina), suas estruturas, dinâmicas, motoras e patologias associadas.
**Autor:** múltiplos professores (apostila histórica em formato NEBLI; provavelmente saída de pipeline NEBLI anterior reusada como referência).
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real. Ensino médio + meses. Já viu organela em microscopia; nunca polimerizou nada na cabeça.
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo.
**Data:** 2026-05-25

**ANCORAGEM (3 conceitos que quero aprender):**
1. Por que polaridade do microtúbulo importa funcionalmente — não só o nome "+/–", mas o que isso permite que a célula faça.
2. Como GTP-cap controla catástrofe vs resgate — o mecanismo molecular do interruptor.
3. Diferença real entre miosina I e II — por que só a II faz contração.

**2 temas vizinhos que NÃO são esse:** matriz extracelular (colágeno, fibronectina); junções celulares como entidade independente (apenas tangenciam aqui via plectina e desmossomos).

---

## 1. Pontos de parada (simulação aluno-alvo)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Intro caixa-abertura | OK | 3 | Pergunta ingênua excelente ("redondinha como eritrócito, achatada como fibroblasto"). Aluno entra. |
| 1.1 Monômero fibroso | OK | 3 | Footnote define "monômero fibroso" na 1ª aparição. Bom. |
| 1.1 "8 protofilamentos em seção transversal" | [STOP: pág 3] | 3 | Aluno acabou de aprender que tetrâmeros se empilham e torcem — e de onde vêm 8 protofilamentos? Nem citação literal nem figura mostram contagem. Salta de "tetrâmero" para "8 protofilamentos" sem ponte. |
| 1.2 Tabela de famílias | [STOP: pág 5–6] | 5 | Tabela quebrou tipograficamente — colunas "Função característica" estão fragmentadas em meio de palavra ("Sustenta-/ta-/ção", "transmite força" cortado, "C-/élulas epiteliais"). Aluno em dificuldade reage com fadiga visual e pula. |
| 2.1 γ-tubulina / γ-TuRC | OK | 9 | Lateral-figura ajuda; analogia "ponto de partida fixo" funciona. |
| 2.2 GTP-cap mecânica | OK | 9–10 | Explicação causa→mecanismo→consequência impecável (resgate vs catástrofe). |
| 2.3 Cinesina/dineína mnemônica | OK | 11 | "Cinesina Cresce, Dineína Direto" — funciona. |
| 2.3 Axonema 9+2 | [STOP: pág 12–13] | 12 | "Dineína axonemal ancorada no microtúbulo A caminha sobre o B do dupleto vizinho" — sem figura clara em sequência ANTES do parágrafo. Aluno precisa visualizar "deslizamento → curvatura" via nexina; só recebe analogia de bastões depois. Inverter ordem (analogia primeiro, anatomia depois) salvaria. |
| 3.1 Treadmilling | OK | 14–15 | "Subunidades entram de um lado e saem do outro" — concreto. |
| 3.2 Arp2/3 + WASP + Rac/Cdc42 | [STOP: pág 16] | 16 | Cadeia de 4 entidades (Rac→WASP→Arp2/3→filamento ramificado) num parágrafo único de 5 linhas, sem desdobramento. Aluno trava no nome "WASP" sem footnote, sem motivo de aparecer. **#sigla() ausente para WASP.** |
| 3.3 Ciclo da miosina II | OK | 17 | Numeração (1)–(5) clara, embora viole regra "sem bullets". Mas comporta-se mais como cronologia mecanística — caso (c) da regra. |
| Conclusão integradora | OK | 19 | Fio condutor "dinâmica regulada a serviço da função" amarra bem. |
| E2 Q9 (gabarito) | [STOP: pág 38] | 38 | Gabarito visualmente quebrado (ver T3.8). Aluno não consegue conferir respostas com confiança. |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria mais próxima:** "Abertura por pergunta ingênua + mecanismo" e "Mecanismo antes de nomenclatura".

**Parágrafo do PDF (pág 3, abertura):**
> "Você já sabe que a membrana plasmática separa o dentro do fora. Mas, dentro da célula, quem dá forma a tudo isso? Quem decide se a célula vai ser redondinha como um eritrócito, achatada como um fibroblasto ou com longos prolongamentos como um neurônio?"

Compara favoravelmente com exemplares NEBLI (gliconeogênese, cadeia respiratória) na abertura — pergunta concreta, ancorada em coisa que aluno reconhece. **NEBLI deveria copiar esta cadência** de "Você já sabe X. Mas Y?". É o gancho mais didático do PDF.

**Parágrafo do PDF (pág 16, Arp2/3):**
> "O complexo Arp2/3 é o nucleador central: quando ativado por proteínas da família WASP (que por sua vez respondem a GTPases Rho como Rac e Cdc42), o Arp2/3 inicia novos filamentos a partir da lateral de filamentos preexistentes, em ângulo de 70°."

Falha em relação ao exemplar canônico de cadeia bioquímica: amontoa **4 nomes novos** (Arp2/3, WASP, Rac, Cdc42) numa frase só. Exemplares fortes do NEBLI desdobram cadeias multi-passo em parágrafos curtos com pergunta-de-passagem ("Mas o que liga Rac ao Arp2/3? A WASP — proteína adaptadora que..."). Aqui salta tudo de uma vez. **Erro NEBLI tipo "nomenclatura antes de mecanismo" presente.**

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo fraco #1 — Pág 16, Arp2/3/WASP/Rho
**Citação literal:**
> "O complexo Arp2/3 é o nucleador central: quando ativado por proteínas da família WASP (que por sua vez respondem a GTPases Rho como Rac e Cdc42), o Arp2/3 inicia novos filamentos a partir da lateral de filamentos preexistentes, em ângulo de 70°."

**Diagnóstico mecanístico:** Cadeia de sinalização de 4 nós aglomerada em uma oração subordinada. Aluno em dificuldade não sabe (a) o que é GTPase Rho, (b) por que Rac/Cdc42 são GTPases especiais, (c) por que WASP fica entre eles. WASP introduzido sem footnote (#sigla ausente). Ângulo de 70° aparece como número solto sem explicação mecanística (por que 70° e não 90°? porque Arp2/3 imita estrutura de actina ao se ligar lateralmente — fica implícito).

**Reescrita pronta:**
> "Quem decide ONDE a actina ramifica? A célula precisa de um interruptor local — ativado por sinal externo, ligado lá fora. Esse interruptor vem em três níveis. Primeiro, na membrana, GTPases pequenas chamadas Rac e Cdc42 ligam-se a GTP quando o receptor sinaliza migração. Segundo, ativas, elas recrutam a WASP, uma proteína adaptadora que muda de conformação fechada para aberta. Terceiro, a WASP aberta encaixa-se no complexo Arp2/3 e o entrega à lateral de um filamento preexistente. Só então o Arp2/3 — que parece ele próprio um pedaço de dímero de actina — inicia um filamento novo a 70° do antigo. Resultado: rede ramificada, densa, que empurra a membrana para frente."

### Parágrafo fraco #2 — Pág 3, "8 protofilamentos"
**Citação literal:**
> "vários tetrâmeros se empilham lateralmente e torcem, formando o filamento maduro de 10 nm com 8 protofilamentos em seção transversal."

**Diagnóstico mecanístico:** O número 8 aparece sem derivação. Aluno acabou de aprender 2 monômeros → 1 dímero → 2 dímeros antiparalelos → 1 tetrâmero. Como se chega a 8 protofilamentos? A figura nominal (pág 4) mostra a montagem mas não explicita "olhe, 8 colunas". Para microtúbulos, o número 13 ganha tratamento "13 colunas verticais de tijolinhos" (pág 8) — para FI o número 8 fica órfão.

**Reescrita pronta:**
> "Por que 8? Imagine olhar o filamento maduro de cima, em corte transversal. Você verá 8 colunas verticais lado a lado, cada uma feita de tetrâmeros empilhados — são os 8 protofilamentos. A torção dos tetrâmeros os mantém entrelaçados como cabos de aço trançados. O número 8 não é mágico, é geometria: é quantos tetrâmeros cabem em volta uns dos outros mantendo a estabilidade."

### Parágrafo fraco #3 — Pág 14, "concentração crítica diferente para cada extremidade"
**Citação literal:**
> "Quando as concentrações de G-actina estão em um valor específico (concentração crítica diferente para cada extremidade), ocorre um fenômeno chamado treadmilling"

**Diagnóstico mecanístico:** "Concentração crítica" entra como conceito-fantasma — termo técnico denso jogado entre parênteses, sem termo-nota, sem definição operacional. Aluno-alvo não sabe que existe Cc⁺ e Cc⁻ diferentes, por que diferem, e qual valor real de G-actina permite treadmilling. Fica como sigla de capítulo perdido.

**Reescrita pronta:**
> "Treadmilling depende de uma assimetria sutil: cada extremidade tem uma concentração-limite própria — a quantidade mínima de G-actina livre que precisa estar no meio para polimerizar mais rápido do que despolimeriza. A extremidade '+' tem essa concentração crítica BAIXA (polimeriza fácil); a '–' tem ALTA (despolimeriza fácil). Existe uma janela de concentração intermediária em que a '+' ainda polimeriza enquanto a '–' já despolimeriza — é nessa janela que acontece o treadmilling. O filamento parece andar porque ganha de um lado o que perde do outro."

---

## 4. T3.3 — 3 seções mais densas (com mitigação)

| Seção | Densidade | Mitigação |
|---|---|---|
| 3.2 Arp2/3 + WASP + Rho (pág 16) | 4 entidades novas em 5 linhas | Quebrar em 3 parágrafos cronológicos (sinal → ativador → executor). Adicionar #sigla(WASP), #termo-nota[Cdc42][GTPase pequena ativada na borda celular]. |
| 1.2 Tabela de 6 famílias (pág 5–6) | 6 famílias × 4 colunas; quebra tipográfica | Reduzir para 5 famílias eliminando GFAP ou redistribuir como prosa-comparativa para evitar quebra de palavras nas colunas estreitas. |
| 2.3 Axonema 9+2 + dineína axonemal + nexina (pág 12–13) | 3 conceitos novos com mecanismo deslizamento→curvatura | Inverter ordem: começar pela analogia (bastões deslizando viram curvatura), depois nomear axonema/dineína axonemal/nexina. Adicionar 1 figura de sequência (estado 1: alinhado; estado 2: deslizado; estado 3: curvado). |

---

## 5. T3.4 — Voz fora do padrão

**Quase nada fora do padrão NEBLI.** Texto mantém diálogo do início ao fim ("Você já sabe...", "Visualize...", "Pense assim..."). Algumas micro-quedas:

- Pág 14 ("provavelmente, a proteína mais abundante das células eucarióticas — representa 5%, chega a 20%"): hedge "provavelmente" enfraquece. NEBLI canônico afirma ou nega; não estima.
- Pág 11 abertura ("Um microtúbulo polar só vira rodovia quando há veículos capazes de percorrer essa rodovia em uma direção definida"): redundância "rodovia… rodovia" — versão limpa: "Um microtúbulo polar só vira rodovia útil quando ganha veículos com direção fixa."
- Pág 17, ciclo da miosina II numerado (1)–(5) — viola regra anti-bullets, mas é caso (c) (cronologia mecanística com itens discretos). Aceitável, porém poderia virar prosa com setas "→".

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** PARTE III §3.2 (Córtex, migração e fagocitose) — pág 15–17.

**Mitigações possíveis:**
1. Dividir em 3.2a (córtex e migração) + 3.2b (fagocitose) com mini-síntese entre.
2. Adicionar diagrama de sinalização (Rac/Cdc42 → WASP → Arp2/3 → ramificação) como SVG/figura.
3. Acrescentar parágrafo-ponte de pergunta ingênua antes de Arp2/3 ("como a célula decide onde polimerizar?").

**Escolher (3) + (1).** A figura de sinalização exige tempo de produção; quebrar em 3.2a/3.2b é gratuito e abre respiro.

---

## 7. T3.8 — ANÁLISE VISUAL

PDF rendering via Read tool falhou (pdftoppm ausente). Análise feita pela extração TXT + .json:

- **Hierarquia tipográfica:** consistente. Cabeçalho "NEBLI · APOSTILA" + "ETAPA X — DESCRIÇÃO" em topo de cada página. Boa, mas o cabeçalho repetido em TODA página come ~5% do espaço vertical. NEBLI poderia ocultar nos breaks.
- **Valor pedagógico das figuras:** 12 imagens em 38 páginas (1 a cada 3 páginas) — abaixo do alvo NEBLI de 3 por PARTE da E1. As 7 figuras listadas no JSON cobrem PARTES I (pág 4, 5, 7, 8), II (pág 9, 10, 12, 13), III (pág 15, 16, 17, 18). Distribuição razoável, mas PARTE I tem 4 e PARTE III tem 4 — densas de actina recebem 4, suficiente. **Faltam:** figura do córtex celular (3.2) e figura comparativa miosina I vs II em ciclo (3.3 só tem estática).
- **Densidade visual:** páginas 6 e 11 com 289 e 417 palavras — picos. Pág 20 com 468 (Resumindo de 2 colunas, esperado). Demais ficam em 150–300 (saudável). Páginas 22–37 (E2/E3) sem nenhuma imagem por 16 páginas seguidas — bloco textual longo desestimula.
- **Uso de cor:** não verificável pelo TXT. Suposição (formato NEBLI canônico): badges de cor por categoria (consolidação/integração/aplicação) na E2. Provavelmente OK.
- **Cortes/overflow:**
  - **Pág 5–6 tabela de famílias FI:** quebra de coluna fragmentando palavras ("Sustenta-/tação", "transmite força" partido, "C-/élulas epiteliais"). Bloqueante visual para aluno em dificuldade.
  - **Pág 38 gabarito:** layout caótico no TXT (linhas Q01 D, Q06 B, etc misturadas com cabeçalhos "CONSOLIDAÇÃO/INTEGRAÇÃO/APLICAÇÃO" em ordem aparentemente embaralhada). Provavelmente 3 colunas que renderizaram em ordem de leitura errada na extração; mesmo assim sugere multi-coluna apertada. **Reorganizar gabarito em tabela 2 colunas (questão | resposta) por categoria, uma seção por bloco vertical.**

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### Técnica 1 — "Mnemônica de inversão + armadilha nomeada"
**Citação:** "Cinesina **C**resce para fora (extremidade '+'). Dineína **D**ireto pro centro (extremidade '–'). Inverter as direções é um erro clássico em questões de tráfego intracelular." (pág 11)

**Nome:** Mnemônica anti-armadilha — emparelha letra inicial com direção + nomeia explicitamente a armadilha de prova.

**Quando NEBLI deveria usar:** sempre que existe par confundível com critério arbitrário (ATP/GTP, kinesina/dineína, miosina I/II, retículo/Golgi). REDATOR-E1 ganha gancho: após introduzir o par, escrever caixa-armadilha com mnemônica de letra inicial + frase "Inverter X é o erro clássico em prova". Aplicar em cadeia respiratória (Complexo I vs II — NADH vs FADH₂), gliconeogênese (PEPCK vs PEP carboxilase).

### Técnica 2 — "Caixas de destaque com título conceitual + nomeação da confusão"
**Citação:** "**GTP nos microtúbulos, ATP na actina — nunca inverter!**" (pág 10) e "**Anel contrátil = actina + miosina II — nunca só actina**" (pág 17)

**Nome:** Caixa-confusão titulada — título da caixa é a regra que o aluno tem que internalizar, formatada com "nunca X" para gravar em memória.

**Quando NEBLI deveria usar:** REDATOR-E1 cria 2–3 caixas-confusão por resumo, sempre titulando com a regra negativa absoluta ("nunca…", "jamais…", "não confundir X com Y"). Difere da caixa-clínica e do mini-resumo: caixa-confusão alerta proativamente para armadilha de prova ANTES dela aparecer na E2.

### Técnica 3 — "Estrutura paralela tripla com fechamento integrador"
**Citação:** "Os filamentos intermediários são a infraestrutura silenciosa: cabos antiparalelos de 10 nm, sem polaridade, sem motor, sem consumo de ATP ou GTP… Os microtúbulos são as rodovias polares: 13 protofilamentos… Os filamentos de actina são os mais finos e os mais versáteis…" (Conclusão pág 19)

**Nome:** Conclusão tripla com epíteto + 1 frase mecanística por elemento.

**Quando NEBLI deveria usar:** sempre que o resumo trata 3 sistemas/processos paralelos (vias glicolítica/pentose/gliconeogênica; complexos I/II/III/IV da CR; receptores adrenérgicos α₁/α₂/β₁/β₂). REDATOR-E1 escreve cada item da conclusão com (a) epíteto/personagem ("infraestrutura silenciosa", "rodovias polares", "versáteis"), (b) 1 cláusula mecanística-chave, (c) 1 cláusula clínica ou funcional. Evita conclusão genérica tipo "vimos que…".

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro | Status | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **PRESENTE (parcial)** | Q26 correta C tem ~28 palavras; distratoras 12–24 palavras (E tem 14, A tem 12, B tem 15). Ratio ≈ 1.9. Q27, Q28, Q29, Q30 também desbalanceadas: correta sempre 2–3× maior que menor distratora. Falha o teste 1.25×. |
| 2 | Siglas sem #sigla() na 1ª aparição | **PRESENTE** | WASP (pág 16) sem footnote. ADP (pág 14) footnote na 12ª aparição. Pi (fosfato) aparece sem footnote em "P é liberado" (pág 17). cAMP aparece em Q3-E só como distratora sem definição prévia. |
| 3 | Subagentes Opus customizados | N/A | Apostila já gerada — diagnóstico de pipeline, não do PDF. |
| 4 | Heredoc ENAMETOOLONG | N/A | Idem. |
| 5 | questao-ce tupla | **AUSENTE** | CEs (Q2, Q5, Q8, Q12, Q16, Q20, Q24) renderizaram OK; sem erro de destructure. |
| 6 | Termo-notas abaixo do alvo | **AUSENTE (atinge alvo)** | Termo-notas identificados no TXT: monômero fibroso, protofilamentos, MTOC, instabilidade dinâmica, treadmilling, Arp2/3, lamelipódio, axonema, plectina, GFAP = 10 termos-nota. **Acima do alvo 6–8.** Bom. |
| 7 | Teto E1 22 páginas | **AUSENTE** | E1 ocupa pág 3–19 = 17 páginas. Dentro do teto. Resumindo em pág 20 (1 página). OK. |

**Erros NEBLI adicionais observados (não no checklist):**
- "Concentração crítica" introduzida sem termo-nota (pág 14).
- Tabela de famílias FI com quebra tipográfica (pág 5–6) — erro de layout/largura de colunas.
- Gabarito multi-coluna desorganizado (pág 38).
- Ciclo miosina II numerado (1)–(5) — caso-limite da regra anti-bullets.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Reformatar gabarito (pág 38) em tabela 2 colunas (Q | resposta) por categoria, 3 blocos verticais empilhados.** Atualmente ilegível.
2. **Reformatar tabela 1.2 (famílias FI, pág 5–6):** reduzir colunas largas/ajustar font-size para evitar quebra de palavra; ou converter para prosa-comparativa.
3. **Dividir §3.2 em 3.2a (córtex + migração) e 3.2b (fagocitose)** com mini-síntese intermediária para aliviar carga cognitiva.

### MECANÍSTICO (max 3)
1. **Reescrever cadeia Rac/Cdc42 → WASP → Arp2/3 (pág 16)** em 3 parágrafos cronológicos com perguntas-de-passagem. Adicionar #sigla(WASP) e #termo-nota[Cdc42].
2. **Derivar o número 8 (protofilamentos do FI, pág 3)** mecanisticamente — não jogar como dado.
3. **Definir "concentração crítica" (pág 14)** com termo-nota explicando que Cc⁺ < Cc⁻ é o que permite treadmilling — base bioquímica precisa estar visível, não escondida em parênteses.

### DIDÁTICO (max 3)
1. **Inverter ordem em §2.3 axonema:** analogia dos bastões deslizando ANTES da anatomia 9+2 + dineína + nexina. Aluno-alvo precisa do gancho visual primeiro.
2. **Engordar distratoras das Q26–Q30 (E2 Aplicação)** para 25–35 palavras com mecanismo plausível-mas-errado, fechando a ratio ≤ 1.25×.
3. **Substituir "provavelmente, a proteína mais abundante" (pág 14)** por afirmação seca: "A actina é a proteína mais abundante…". Hedge enfraquece voz NEBLI.

### ESTÉTICO (max 3)
1. **Reduzir cabeçalho "NEBLI · ETAPA X" em páginas de continuação** (manter na 1ª de cada etapa).
2. **Adicionar 2 figuras na PARTE III:** córtex celular (esquema) + ciclo miosina II animado em 5 estados.
3. **Espaço em branco antes/depois das caixas de destaque** ("GTP/ATP", "Anel contrátil") — atualmente parecem coladas no texto-corpo (sugerido pela extração TXT contígua).

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** SIM — abertura, mnemônicas anti-armadilha, caixas-confusão tituladas e conclusão tripla são técnicas exemplares que devem entrar no repertório do REDATOR-E1.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** SIM — 3 estruturais (gabarito, tabela FI, divisão §3.2) + 3 mecanísticos (Arp2/3-WASP-Rho, número 8, concentração crítica).
3. **Seção para refazer?** §3.2 (Córtex/migração/fagocitose, pág 15–17) — densa, com cadeia de sinalização sem desdobramento e WASP sem footnote.
4. **Parágrafos para reescrever?** 3 (listados em T3.2): §3.2 Arp2/3-WASP-Rho (pág 16), §1.1 "8 protofilamentos" (pág 3), §3.1 "concentração crítica" (pág 14).

---

[APROVAR COM RESERVAS]

<!-- TIER3_DONE -->
