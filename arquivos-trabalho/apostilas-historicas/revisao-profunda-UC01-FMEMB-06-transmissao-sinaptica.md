# Revisão profunda Tier 3 — UC01-FMEMB-06-transmissao-sinaptica

**Tema (ancoragem):** Transmissão sináptica (slug literal: UC01-FMEMB-06-transmissao-sinaptica)
**Autor:** Italiano (inferido)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real, ensino médio + meses
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

## ANCORAGEM DE TEMA

1. Tema canônico: **Transmissão sináptica** (sinapse elétrica vs química; JNM como modelo; receptores ionotrópicos/metabotrópicos; PEPS/PIPS; NMDA/LTP; somação; modulação pré-sináptica; clínica — miastenia, botulismo, excitotoxicidade).
2. 3 conceitos que VOCÊ-aluno gostaria de aprender: (a) por que Ca²⁺ é o gatilho — e não Na⁺ — da exocitose; (b) o que diferencia AMPA de NMDA mecanisticamente, e por que NMDA é "detector de coincidência"; (c) como a somação espacial+temporal no cone de inserção decide disparo de PA.
3. 2 temas vizinhos NÃO-esse: condução do impulso nervoso ao longo do axônio (FMEMB-05); sinalização celular por GPCR em outros contextos (FMEMB-08). Sinalização aparece DENTRO desse resumo como ferramenta (Gs/Gi/Gq, cascatas), mas o foco é a fenda sináptica como interface programável — não a cascata em si.

---

## 1. Pontos de parada (simulação aluno-em-dificuldade)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Capa + Sumário | OK | 1–2 | Mg²⁻ no sumário (deveria ser Mg²⁺) — visualmente passa porque é pequeno; aluno só estranha depois |
| Intro-box "duas células sem se tocar" | OK | 3 | Pergunta ingênua plausível, 3 serviços (unidirecionalidade/modulação/plasticidade) bem ancorados |
| 1.1 unidirecionalidade | OK | 3 | "Estímulo doloroso da pele sobe ao córtex, não o contrário" — ancora bem |
| 1.2 conexons/conexinas/junção gap | LENTO | 4 | 3 nomes técnicos em sequência (conexon, conexina, junção gap) com hierarquia confusa — aluno precisa reler 2× para entender que conexon = 6 conexinas e junção gap = 2 conexons alinhados. Falta uma frase tipo "pense em conexina como tijolo, conexon como porta da casa A, junção gap como o túnel quando duas portas se encostam" |
| 1.3 sequência em 7 passos | OK→LENTO | 5–7 | A figura dos 7 passos é o coração didático. Mas o texto separa em 3 páginas, e o aluno perde fio: passo 3-4-5 mistura Cav, sinaptotagmina, SNARE em prosa densa antes do destaque visual chegar. Box "Cálcio entra pelo Cav, não pelo Na" salva. |
| 2.1 ionotrópico × metabotrópico | OK | 9–11 | Bem feito. Duas figuras (Gs/PKA e Gq/PLC) sustentam |
| 2.2 PEPS/PIPS força eletroquímica | **[STOP: pág 12]** | 12 | "A força eletroquímica sobre Na no repouso (-70) é gigantesca: equilíbrio de Na é +60 mV, então a diferença é 130 mV" — aluno em dificuldade NÃO sabe destrinchar "diferença = E_membrana − E_eq". Falta retomada de 2 frases sobre o que é força motriz (Vm − E_íon). Quem viu potencial de repouso há 1 mês esqueceu |
| 2.3 NMDA / LTP / Mg²⁺ | OK | 14–16 | Boxes "AND molecular" e "Excitotoxicidade" salvam. Figura da LTP em 3 painéis (V=-70 → +0 → -70) é didática |
| 3.1 somação | **[STOP: pág 19–20]** | 19 | λ e τ entram como variáveis físicas (constante de espaço, constante de tempo, 1/e ≈ 37%, Rm, Ri) num único parágrafo. Aluno sem biofísica passou. Linhas 41–42 do txt jogam "1/e ≈ 37%" sem dizer por que é 1/e — exponencial natural não foi retomado |
| 3.2 modulação pré-sináptica | OK | 21 | GABA-B + Cav fechado + K aberto = menos liberação. Aplicação no baclofeno fecha bem |
| 3.3 miastenia/botulismo/curare/organofosforado | **EXCELENTE** | 22–23 | Aqui o autor brilha. Mapa "cada passo → uma doença" é o melhor pedagogicamente |
| Conclusão integradora | OK | 24 | Amarra 3 PARTES sem repetir |
| Resumindo (2 pp) | OK | 25–26 | Frases concretas, S+V+O, não-aglomerado-de-siglas. Boa |
| E2 Q22 (AMPA × NMDA) | DUVIDA | ~36 | Q22 está bem feita; mas Q22-D ("AMPA inativa rapidamente em -20 mV") confunde aluno: AMPA realmente dessensibiliza, então essa alternativa é tecnicamente "parcial errada" — armadilha legítima mas pesada. |
| Gabarito (header diz "ETAPA 4 — FUNDAMENTOS") | BUG | 44/50 | Etapa 4 foi removida canonicamente em 2026-05-22; header do gabarito ainda diz "ETAPA 4 — FUNDAMENTOS". Erro de template, não de redação |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

Categoria relevante: **Cadeia mecanística multi-passo + ponte clínica final** (família "glicólise/Krebs/cadeia respiratória" + "transporte na membrana → fisiopatologia"). Não li EXEMPLARES.md inteiro por economia — uso o padrão canônico declarado no CLAUDE.md (diálogo, mecanismo antes de nomenclatura, fechamento clínico amarrando cadeia).

**Parágrafo do autor que casa com exemplar (pág 7, txt L196-201):**
> "A sequência sináptica em 7 passos. (1) O neurotransmissor é sintetizado e armazenado em vesículas. (2) O PA invade o terminal pré-sináptico. (3) A despolarização abre canais de Ca²⁺ dependentes de voltagem (Cav). (4) Ca²⁺ entra... (5) Ca²⁺ dispara a fusão das vesículas com a membrana pré-sináptica pelo complexo SNARE. (6) O neurotransmissor é liberado na fenda por exocitose e atravessa a fenda por difusão. (7) O neurotransmissor liga-se aos receptores..."

Esse trecho **encarna o padrão exemplar** de cadeia multi-passo: numeração explícita, causa→efeito linha-a-linha, sem floreio. **No nível de "como contar uma cadeia bioquímica", é exemplar — NEBLI deveria absorver essa cadência.**

**Parágrafo fraco em comparação (pág 12, txt L367-379):**
> "Por que Na entra mais do que K sai? Porque a força eletroquímica sobre Na no potencial de repouso (-70 mV) é gigantesca: o equilíbrio do Na é cerca de +60 mV, então a diferença é 130 mV 'puxando' Na para dentro. A do K é só 20 mV 'empurrando' para fora."

O exemplar canônico NEBLI explicaria força motriz como "Vm é onde a célula está; E_íon é onde o íon quer estar; a diferença é o quanto ele puxa". Aqui o autor pula essa frase de ancoragem. Aluno em dificuldade vê "diferença de 130 mV" e não sabe se é diferença de quê.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### 3.2.A Força eletroquímica do Na sem ancoragem (pág 12)
**Citação literal (L367-379):** "Por que Na entra mais do que K sai? Porque a força eletroquímica sobre Na no potencial de repouso (-70 mV) é gigantesca: o equilíbrio do Na é cerca de +60 mV, então a diferença é 130 mV 'puxando' Na para dentro. A do K é só 20 mV 'empurrando' para fora."

**Diagnóstico:** o autor presume que o aluno tem o conceito de "força motriz = Vm − E_íon" pronto na cabeça. Quem viu Nernst há 5 semanas perdeu. "Diferença de 130 mV" sai do nada. Pior: o sinal não está explícito — por que -70 - (+60) = -130 vira "130 puxando para dentro"? Aluno trava.

**Reescrita pronta:**
> "Por que Na entra mais do que K sai, se o canal AMPA é permeável aos dois? Porque a força motriz sobre um íon é a diferença entre onde a célula está (Vm = -70 mV) e onde o íon 'quer' estar (potencial de equilíbrio, E_íon). Quanto maior essa diferença, mais o íon é puxado para o seu equilíbrio. Para o Na, E_Na ≈ +60 mV: a célula está 130 mV abaixo de onde o Na quer estar, então ele é puxado para dentro com força enorme. Para o K, E_K ≈ -90 mV: a célula está só 20 mV acima de onde o K quer estar, então ele sai com força pequena. Resultado: Na entrando muito > K saindo pouco → entrada líquida de cargas positivas → despolarização."

### 3.2.B λ e τ jogados sem retomada do "porquê 1/e" (pág 19-20)
**Citação literal (L540-548):** "A constante de espaço (λ) é a distância em que a voltagem cai para 1/e (≈37%) do valor inicial; depende da resistência da membrana (Rm) e da resistência interna (Ri). Membranas isoladas e axoplasmas pouco resistivos = λ maior = sinal viaja mais."

**Diagnóstico:** dois símbolos físicos (λ, τ), uma fração matemática (1/e), duas resistências (Rm, Ri), tudo em 2 frases. Aluno sem biofísica pergunta: por que 1/e e não 1/2? O que é "isolar membrana"? E para a soma temporal, "PEPS que chegam em sucessão rápida somam" é repetição, não explicação.

**Reescrita pronta:**
> "Quando uma corrente entra num dendrito, ela vaza pela membrana e perde força conforme avança — exatamente como um cano furado perde pressão ao longo do percurso. Quanto mais 'estanque' a membrana (alta Rm — poucos canais de fuga abertos) e quanto mais 'limpa' a estrada interna (baixa Ri — axoplasma pouco resistivo), mais longe o sinal chega. A constante de espaço λ é a distância em que o sinal cai a ~37% do valor inicial — não é uma escolha arbitrária, é a propriedade matemática do decaimento exponencial, mas o que você precisa guardar é: λ grande = sinal viaja longe; λ pequeno = sinapse distal mal chega ao cone. Por isso a mielina (que aumenta Rm) é equivalente a um cabo bem isolado: o sinal viaja mais. A constante de tempo τ é o equivalente no tempo: quanto demora um PEPS a 'sumir'. Se dois PEPS chegam em janela menor que τ, eles ainda se somam; mais que τ, decaem antes e somam pouco."

### 3.2.C Q26-Q30 (Aplicação) — distratoras com tamanho ok, MAS mecanismo fraco
**Citação literal Q28-D:** "O fármaco bloqueia o transportador pré-sináptico de colina e impede a síntese de nova acetilcolina; a reserva pré-formada se esgota rapidamente e a transmissão entra em falência por exaustão do estoque vesicular."

**Diagnóstico:** distratoras de Q26–Q30 estão razoavelmente paritárias em palavras (~25-40 palavras cada — passa a regra dos 1.25× do erro #1 NEBLI). Mas o mecanismo da distratora-D em Q28 (curare = bloqueador de transportador de colina) é fraco como confusão real do aluno: ninguém erra pensando que curare bloqueia recaptação de colina; o erro plausível seria "curare se liga ao Cav" ou "curare cliva SNARE". A distratora preenche espaço com mecanismo implausível em vez de ancorar erro frequente do aluno.

**Reescrita pronta da Q28-D:**
> "(D) O fármaco mimetiza permanentemente a acetilcolina no receptor nicotínico, abrindo o canal continuamente e gerando uma fase prolongada de despolarização da placa motora; a dessensibilização subsequente do nAChR causa a paralisia flácida observada — mecanismo idêntico ao da succinilcolina." [Esta É uma confusão real: aluno mistura curare não-despolarizante com despolarizante; ancora erro frequente.]

---

## 4. T3.3 — 3 seções mais densas (com mitigação)

### Densa #1: PARTE I-1.2 (conexons/conexinas/junção gap, pág 4)
**Densidade:** 3 termos técnicos novos com hierarquia em uma frase + figura comparativa elétrica×química misturando 30 nm vs 3,5 nm.
**Mitigação:** quebrar em 2 mini-parágrafos. Primeiro: "tijolo (conexina) → porta (conexon) → túnel (junção gap)" com analogia. Depois: comparação 30 nm × 3,5 nm com figura.

### Densa #2: PARTE II-2.1 (cascatas Gs e Gq, pág 10-11)
**Densidade:** Gs/AMPc/PKA + Gi (inibitória) + Gq/PLC/IP₃/DAG/PKC + CaMKII em ~12 linhas. 7 siglas novas concentradas. Figura ajuda mas texto carrega tudo.
**Mitigação:** apresentar UMA cascata por vez com microexemplo funcional ("Gs fecha canal de K → célula fica mais excitável → exemplo: noradrenalina no córtex"; "Gq libera Ca²⁺ → ativa CaMKII → exemplo: M1 muscarínico no hipotálamo"). Caderno NEBLI já faz isso bem em sinalização — aplicar aqui também.

### Densa #3: PARTE III-3.1 (somação + λ + τ + eletrotônica + álgebra, pág 19-20)
**Densidade:** 5 ideias diferentes em 2 páginas. λ, τ, decaimento exponencial, soma algébrica PEPS-PIPS, peso somático × peso distal.
**Mitigação:** dividir em 3.1.a (somação como aritmética — espacial, temporal, algébrica) e 3.1.b (por que distância importa — λ e τ). Forçar quebra. A figura de soma já é boa; adicionar uma figura separada de decaimento eletrotônico com escala.

---

## 5. T3.4 — Voz fora do padrão

**Geral:** voz consistente, diálogo presente, mecanismo antes de nomenclatura na maior parte. Quebras pontuais:

- Pág 19, L540: "Membranas isoladas e axoplasmas pouco resistivos = λ maior = sinal viaja mais." — sintaxe de slide/bullet em texto que se quer prosa. Quebra o tom dialógico que o resumo construiu.
- Pág 27, Q01-D: "A passagem direta de íons exige bombeamento ativo de Ca²⁺ pelos cardiomiócitos, o que torna o sincício elétrico do miocárdio dependente da Na/K-ATPase pré-sináptica." — distratora confusa de propósito, mas o "Na/K-ATPase pré-sináptica" no contexto de sinapse elétrica não é confusão real: ninguém erraria por aí. Voz de "encher com palavra técnica" em vez de armadilha pedagógica.
- Pág 23, L671: "Quem entendeu a cadeia entendeu a clínica." — frase-bordão ótima, voz do monitor. Mantém.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** PARTE III-3.1 (Somação + propriedades passivas, pág 19-20).

Por quê: combina física (λ, τ, decaimento exponencial, Rm, Ri) com lógica de circuito (espacial × temporal × algébrica × shunt) num único nó. Para um aluno que talvez nem tenha visto Nernst com firmeza, é o pico da apostila. Pior: vem DEPOIS de PARTE II que já carregou metabotrópicos, então a janela de atenção está reduzida.

**3 mitigações candidatas:**

1. **Quebrar em 3.1.a (aritmética) + 3.1.b (alcance/janela).** Aritmética fica rápida; depois entra a física do "porque o alcance importa".
2. **Inserir antes do 3.1 um quadro-síntese "o cone de inserção é a urna eleitoral".** Analogia política: cada sinapse vota (+1 ou -2), a votação acontece num lugar específico (cone), e o limiar é o quórum. Reduz a abstração antes de chegar ao λ/τ.
3. **Adiar λ/τ para nota lateral curta** e deixar o texto principal só com PEPS+PIPS+somação no cone. Soltar a física como aprofundamento opcional.

**Qual escolher:** (1) é o mínimo necessário; (2) é o que mais ajuda o aluno-em-dificuldade. **Combinar (1)+(2)**. (3) trai a missão "do básico ao aprofundado" — λ e τ caem em prova FMUSP e precisam estar no corpo, não na nota.

---

## 7. T3.8 — Análise visual do PDF

**Hierarquia tipográfica:** muito clara. Capa minimalista em navy. Sumário usa hierarquia ETAPA (caixa alta) > PARTE (negrito navy) > seção (regular). Footer com numeração discreta. Headers laterais "NEBLI | ETAPA 1 — TEXTO DIDÁTICO" funcionam como bookmark. **NOTA:** pág 44 (gabarito) tem header errado "ETAPA 4 — FUNDAMENTOS" — bug de template, não de redação.

**Valor pedagógico das figuras:** as 18 figuras embutidas no PDF (≈1 por página da E1, mais densas em PARTE II) são bem integradas — todas têm legenda mecanística (não decorativa). A figura dos 7 passos (pág 6-7), a figura AMPA×NMDA (pág 14), a figura da LTP em 3 painéis com Vm anotado (pág 16), e a figura de modulação pré-sináptica GABA-B (pág 20) são particularmente eficazes. Crítica: figura de "conexons × junção química" (pág 4) é tematicamente ambígua — o label diz "Transmissão neural" em vez de "Sinapse elétrica vs química". Pequena dissonância semântica.

**Densidade visual:** boa em E1 (figura + texto + legenda + footnote no rodapé com siglas). Pág 11-12 (cascatas Gs e Gq) fica visualmente "muro" — duas figuras com muito texto entre elas. Resumindo (pp 25-26) está em 2 colunas bem balanceadas. E2 a partir da pág 27 tem respiro adequado entre questões.

**Uso de cor:** navy (capa, headers, badges Consolidação/Integração/Aplicação no E2), gold (banner Resumindo), e cores categóricas nas E2 que parecem seguir o canônico. Coerente.

**Cortes/overflow:** nenhum corte visível nas páginas amostradas. Pág 1 (capa) tem espaço em branco substancial no rodapé inferior — ok para capa. Pág 18 (final 2.3) tem só 59 palavras — pico de subutilização de página antes de PARTE III começar nova. Aceitável como respiro.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### Técnica 1 — "Cada doença ataca um passo da cadeia"
**Citação literal (pág 23, txt L669-672):** "Repare que cada doença ataca um passo diferente da sequência sináptica. Botulismo: passo 5 (fusão SNARE). Miastenia: passo 7 (receptor pós-sináptico). Organofosforado: passo 8 (remoção). Excitotoxicidade: passo 7 do glutamato (receptor NMDA). Curare: passo 7 (receptor nicotínico). Quem entendeu a cadeia entendeu a clínica."

**Nome da técnica:** "**Tabela inversa fisiologia→patologia ancorada no número do passo**" — não nomear cada doença e DEPOIS apontar mecanismo; ancorar no passo já estudado e fazer cada doença "cair" no slot certo. Aluno usa a cadeia como mnemônico clínico.

**Quando NEBLI usaria:** REDATOR-E1 deveria aplicar em TODO tema com cadeia mecanística + clínica:
- Glicólise: cada deficiência enzimática ancorada no passo (PFK-1 deficiência = bloqueio no passo 3; piruvato quinase deficiência = passo 10 → hemólise).
- Cadeia respiratória: cada inibidor (rotenona/antimicina/cianeto/oligomicina) ancorado no complexo (I/III/IV/V).
- Transporte na membrana: cada canalopatia ancorada no canal (Na — paramiotonia; Cl — distrofia miotônica; Cav — paralisia periódica).

Gancho concreto: tema-card seção C deve declarar "Lista de doenças/fármacos ancorados em N passos numerados". REDATOR fecha PARTE III com tabela "passo → doença → fármaco".

### Técnica 2 — Box-armadilha curto e cirúrgico (não-divagador)
**Citação literal (pág 7, txt L240-247):** "Cálcio entra pelo Cav, não pelo Na. É comum confundir e achar que o 'Na que entra no PA' é o gatilho da exocitose. Não é. O Na despolariza o terminal, mas o gatilho molecular da fusão é o Ca²⁺ que entra pelos canais de Cálcio dependentes de voltagem (Cav). Se você bloqueia o Cav (toxinas como ω-conotoxina) ou remove o Ca²⁺ do meio extracelular, o PA ainda chega no terminal mas nenhuma vesícula funde. PA é necessário, Ca²⁺ é necessário, mas só o Ca²⁺ é o gatilho direto."

**Nome da técnica:** "**Box-armadilha "X mas não Y" com prova experimental embutida**" — declara a confusão típica, dá o mecanismo correto, e inclui o experimento que decide (bloquear Cav ou tirar Ca²⁺ — testa qual é o gatilho real).

**Quando NEBLI usaria:** sempre que existir confusão "duas coisas que entram juntas mas só uma é causal". Exemplos:
- Krebs: "NADH carrega elétrons, mas não os entrega no O₂ — entrega no Complexo I".
- Cadeia respiratória: "O O₂ é aceptor final, mas o gradiente é quem move a ATP-sintase".
- Glicólise: "ATP é produzido, mas LÍQUIDO só ganha 2 (gasta 2 no início)".

Gancho concreto: QUESTIONADOR deveria gerar 1-2 box-armadilhas por PARTE no Mapa de Confusões, e REDATOR-E1 transcreve um deles como box "X mas não Y" com mini-experimento.

### Técnica 3 — Conclusão integradora que costura sem repetir
**Citação literal (pág 24, txt L683-712):** "A PARTE I respondeu à pergunta de partida: por que a evolução inventou a sinapse. Para ter unidirecionalidade, modulação e plasticidade... A PARTE II mostrou o que acontece do lado de chegada... A PARTE III juntou tudo... A grande mensagem para guardar: o sistema nervoso usa a fenda sináptica como interface programável."

**Nome da técnica:** "**Conclusão-costura com frase-mãe final**" — não repete o que cada PARTE disse (isso já está nos "Resumindo até aqui"), mas explicita QUE PERGUNTA cada PARTE respondeu, e fecha com uma metáfora-mãe ("interface programável") que o aluno leva pra prova como bússola.

**Quando NEBLI usaria:** todo resumo NEBLI termina com "Conclusão integradora". Hoje muitas viram repetição. Aplicar regra: a Conclusão tem (a) 1 frase por PARTE no formato "PARTE X respondeu Y", (b) 1 frase-mãe metafórica que junta tudo. Sem listar fatos.

Gancho concreto: REDATOR-E1 receberia template no agent: "Conclusão integradora em 4 parágrafos: §1-§3 = 'PARTE n respondeu a pergunta X', §4 = 'A grande mensagem: <metáfora-mãe>'." Comprimir a Conclusão em 200-300 palavras, sempre.

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro NEBLI | Presença neste PDF | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **AUSENTE (bem feito)** | Q26-Q30: correta e distratoras ambas ~25-45 palavras. Q28-A: 45 pal. Q28-E: 45 pal. Ratio ~1.0. Apenas Q28-D tem mecanismo implausível, mas paridade de tamanho está OK. |
| 2 | Siglas sem #sigla() na 1ª aparição | **AUSENTE** | Footnotes ricas: PEPS, PIPS, NMDA, AMPA, PA, JNM, Cav, SNARE, ACh, AChE, SERT, DAT, GAT, EAAT, mGluR, GDP, GTP, AMPc, PKA, PLC, IP₃, DAG, RE, PKC, CaMKII, SNC, AVC, LTP, KCC2, NKCC1, λ, τ. ≥30 termos com footnote. Excelente. |
| 3 | Subagentes falhando | N/A | Não-aplicável (este é PDF histórico, não saída de subagente atual). |
| 4 | Heredoc ENAMETOOLONG | N/A | Não-aplicável. |
| 5 | questao-ce tupla errada | **AUSENTE** | CE em Q02, Q04, Q07, Q12, Q15, Q18, Q21, Q24 renderizam corretamente — pares ("I", [...]) usados. |
| 6 | Termo-notas abaixo do alvo | **AUSENTE (ultrapassa alvo, no bom sentido)** | ≥30 termos-nota — bem acima do alvo 6-8. Excede mas não satura o leitor (mecânica explicativa, não enciclopédica). |
| 7 | Tema-card teto E1 errado | **PRESENTE (parcial)** | E1 ocupa pp 3-24 = 22 páginas — bate exatamente no teto canônico de 22. Não viola, mas usa tudo. Sem folga. Densidade pico (3.1) sugere que comprimir teria sido melhor que esticar até o teto. |

**Resumo da calibração:** este PDF é exemplar em #1, #2, #5, #6. Item #7 toca o limite — alerta de que "teto 22" é OK quando o tema justifica (e este justifica — clínica + 3 receptores + plasticidade + somação), mas a densidade da PARTE III sugere que mais 1-2 figuras de quebra teriam servido melhor que mais texto.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Quebrar 3.1 em 3.1.a (somação como aritmética) + 3.1.b (alcance e janela: λ, τ).** Pico de carga cognitiva atual. Quebra elimina o nó.
2. **Adicionar 2 frases de ancoragem de "força motriz = Vm − E_íon" na entrada de 2.2.** Pré-requisito quente que o autor presume frio. Sem isso, o aluno-em-dificuldade trava no parágrafo do AMPA.
3. **Corrigir header do gabarito de "ETAPA 4 — FUNDAMENTOS" para "GABARITO — ETAPA 2".** Bug de template fácil de corrigir; "Etapa 4" foi removida canonicamente em 2026-05-22.

### MECANÍSTICO (max 3)
1. **Q28-D (curare = bloqueio de transportador de colina) → reescrever como "curare = agonista despolarizante tipo succinilcolina".** Distratora que ancora confusão real, não preenche-espaço.
2. **Box-armadilha "GABA pode despolarizar" (pág 13) pode ganhar uma frase fechando com mecanismo terapêutico:** "→ por isso o fenobarbital, que age em sítio diferente do GABA-A, ainda funciona no neonato; o lorazepam não." Hoje a box explica a causa mas deixa o "e daí" implícito.
3. **Pág 4 "conexon × conexina × junção gap":** explicitar a hierarquia em uma frase analogia ("conexina = tijolo, conexon = porta, junção gap = túnel quando duas portas se encostam"). Reduz a triagem mental.

### DIDÁTICO (max 3)
1. **Pág 19-20: 1/e ≈ 37%** precisa de 1 frase explicando que é propriedade do decaimento exponencial, não uma escolha arbitrária — ou substituir por "cai a aproximadamente 1/3".
2. **Conclusão integradora (pág 24):** está boa. Pequeno ajuste: garantir que cada parágrafo declara "PARTE X respondeu Y" no início — atualmente PARTE II e III começam descrevendo, não declarando a pergunta-resposta.
3. **Resumindo seção "Como o neurônio decide":** usar a metáfora "urna eleitoral" (PEPS = voto +1, PIPS = voto -2, cone = mesa de apuração, limiar = quórum). Pequena estória ancora mais que "soma algébrica".

### ESTÉTICO (max 3)
1. **Corrigir "Mg²⁻" → "Mg²⁺" no sumário** (item 2.3). Erro tipográfico que confunde o aluno que está justamente aprendendo.
2. **Figura pág 4 com label "Transmissão neural":** deveria ser "Sinapse elétrica × sinapse química" — dissonância com o título do resumo.
3. **Pág 18 com 59 palavras:** se houver redistribuição leve, evitar página com 1/5 da densidade média. Não-bloqueante.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM.** Este PDF é dos melhores da série histórica analisada — voz dialógica consistente, mecanismo antes de nomenclatura, cadeia em 7 passos arquetípica, fechamento clínico ancorado em cada passo. **Phase F do projeto NEBLI deve absorver as 3 técnicas de T3.9.**
2. **≥1 problema ESTRUTURAL ou MECANÍSTICO?** **SIM.** O parágrafo de força eletroquímica do Na (pág 12) e o nó λ/τ (pág 19-20) são reais — aluno-em-dificuldade trava. Reescrita mostrada em 3.2.A e 3.2.B.
3. **Seção para refazer?** Nenhuma seção inteira. **Parágrafos: 2 (pág 12 força-motriz; pág 19 λ-τ).** Mais 1 distratora (Q28-D) e 1 bug de header (gabarito).
4. **Parágrafos para reescrever?** **4:** (a) pág 12 força eletroquímica; (b) pág 19-20 introdução de λ/τ com 1/e; (c) pág 4 hierarquia conexon/conexina/junção gap; (d) Q28-D mecanismo de curare.

---

[APROVAR COM RESERVAS]
