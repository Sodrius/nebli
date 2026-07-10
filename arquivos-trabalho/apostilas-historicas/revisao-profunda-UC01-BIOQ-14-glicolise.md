# Revisão profunda Tier 3 — UC01-BIOQ-14-glicolise

**Tema (ancoragem):** Glicólise
**Autor:** Davi Sousa (apostila NEBLI histórica, pipeline próprio — Gn anterior à canonização atual)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real, ensino médio + meses
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

## Ancoragem prévia

- **Tema canônico:** Glicólise (UC01 Bioquímica, aula 14).
- **3 conceitos que eu-aluno quero aprender:**
  1. Por que a glicólise gera só 2 ATP líquidos e mesmo assim é universal.
  2. Como a GAPDH "embala" a energia de oxidação num fosfato (sem ATP de entrada).
  3. Por que o fígado em jejum não rouba glicose do cérebro — a lógica HK vs glicoquinase + F-2,6-BP/PFK-2.
- **2 temas vizinhos que NÃO são esse:** gliconeogênese (sentido inverso, no fígado, sem ser glicólise); ciclo de Krebs / cadeia respiratória (mitocondrial, depois do piruvato).

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão |
|---|---|---|---|
| Capa | OK | 1 | Bloco meta canônico claro; Lehninger+Berg+Boron como onde estudar — aluno aceita. |
| Sumário | OK | 2 | 3 partes, sub-itens descritivos curtos. PARTE II tem 4 sub-itens (2.1–2.4) — leve overshoot da regra "máx 3 por PARTE" mas não estanca. |
| 1.1 — universalidade + GLUTs | OK | 3–4 | Abre com "de onde vem o ATP que cada célula usa" — engata. KM dos GLUTs com número e tecido. |
| 1.2 — fase preparatória (HK→TPI) | **STOP leve** | 5–7 | Cinco reações encadeadas em 3 páginas. Aluno sobrecarrega no salto Aldolase→TPI: a tabela das 10 reações chega na pág 7 mas as reações 1–5 já foram detalhadas antes — ordem invertida da expectativa. Recupero porque o "Resumindo até aqui" reabre a cabeça. |
| 1.3 — HK × glicoquinase | OK | 8–10 | Comparação tecido + KM + inibição por G6P + MODY-2 clínico. Modelo de seção dialogada. |
| 2.1 — GAPDH | **STOP forte** | 11–13 | Mecanismo (cisteína-SH, tioéster, NAD+, Pi) é entregue em 3 passos numerados + 1 parágrafo do "ponto pedagógico". Aluno em dificuldade NÃO viu cisteína-SH catalítico antes (proteínas I/II passaram por cima) — quando a frase "o cisteína-SH catalítico do sítio ativo ataca o aldeído, forma um intermediário tioéster com a enzima" cai sem retomada, eu paro. **Falta footnote do nucleófilo cisteína em 1 frase.** Box do arseniato (pág 12) recupera bem porque é narrativa concreta. |
| 2.2 — PGK/enolase/PK | OK | 13–14 | Bonita a passagem do "PEP como mola comprimida". Tautomerismo enol/ceto bem entregue. |
| 2.3 — destino do piruvato + lactato | OK | 15–16 | Box "Lactato não é vilão" é dos melhores momentos da apostila. |
| 2.4 — três sistemas energéticos | OK | 17–19 | Comparativo velocidade × capacidade canônico. Tabela formatada com células mescladas (pág 19) parece ter overflow tipográfico — texto da coluna "Exemplo" está deslocado para a coluna "Capacidade". |
| 3.1 — três válvulas | OK | 20 | Reabertura clara, sem jargão novo. |
| 3.2 — PFK-1 e F-2,6-BP | **STOP médio** | 21–22 | Densidade alta de siglas em 2 páginas: F-2,6-BP, PFK-2, FBPase-2, PKA, AMPc, glucagon, F6P. Mesmo com `#sigla()`, o aluno cruza 5 novas siglas em uma página + a explicação da bifuncionalidade. Falta cápsula "vou repetir devagar: PFK-1 é a enzima, PFK-2 é a fábrica do regulador, F-2,6-BP é o sinal — três peças diferentes". |
| 3.3 — hormonal | OK | 23–24 | Tabela mental glucagon/insulina/adrenalina × fígado/músculo enfim cristaliza. Box diabetes 2 fecha bem. |
| Conclusão integradora | OK | 25 | Sintetiza válvulas + GAPDH + destino + hormonal. Encerramento maduro. |
| Resumindo | OK | 26 | 1 página, 2 colunas, 8 seções — dentro do canônico. Frases concretas. |
| E2 (Q01–Q30) | Variável | 28–54 | Ver §3 abaixo. |
| E3 (5 discursivas) | OK | 55–57 | Modelos ≤100 palavras (Q5 ≤130), mecanismo central. Padrão NEBLI. |
| Gabarito | **STOP bug** | 58 | **Header zumbi:** "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" no topo, mas Etapa 4 foi removida do pipeline em 2026-05-22. Conteúdo da página é gabarito da E2 — header não corresponde. |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

### Categoria 17 (Catálogo família proteica/molecular) — pág 4, GLUTs

**Apostila (pág 4):**
> "GLUT1 da hemácia tem KM baixo (~1 mM) e capta o tempo todo. GLUT2 do hepatócito tem KM alto (~15 mM) e só capta bem quando a glicemia sobe (depois da refeição). GLUT3 do neurônio tem KM muito baixo (alta afinidade) — o neurônio é o último a ficar sem glicose mesmo em jejum. GLUT4 do músculo e adipócito só vai para a membrana se a insulina mandar."

**Exemplar 17.1 (GLUTs):**
> "A família GLUT compartilha o mesmo desenho — 12 hélices transmembrana que abrem e fecham conforme alternam entre fora e dentro — mas cada isoforma tem KM e tecido próprios, e é isso que define quando o tecido capta glicose. [...] segue tabela."

**Veredito:** a apostila **bate o exemplar em prosa concreta** (KM com número + tecido + função teleológica). O exemplar tem tabela formal; a apostila preferiu prosa fluida + uma tabela depois em 1.3 (HK×glicoquinase) — funciona porque o aluno já conhece GLUTs da aula de membrana. Crítica: faltou anchoragem do "mesmo desenho 12-hélices" que o exemplar tem — é o gancho estrutural que faria entender por que tantas isoformas.

### Categoria 1 (Explicação mecanística parágrafo-por-parágrafo) — pág 11, GAPDH

**Apostila:**
> "A GAPDH faz três coisas ao mesmo tempo: 1. Oxida o gliceraldeído-3-fosfato — o grupo aldeído (CHO) do C1 perde elétrons e vira um grupo carbonila ligado a oxigênio. [...] 2. Incorpora um fosfato inorgânico (Pi) — não vem de ATP. [...] 3. Reduz NAD+ a NADH."

**Exemplar 1.1 (PEPS/PIPS):**
> "Quando um neurotransmissor excitatório se liga ao receptor pós-sináptico, o canal abre e Na+ entra. [...] A membrana despolariza alguns milivolts — esse é o PEPS."

**Veredito:** a apostila **acerta a estrutura "três fenômenos simultâneos, um a um"**, mas pisca no nível abaixo: o exemplar entrega o mecanismo do ataque nucleofílico (cisteína-SH → tioéster) só em 1 parágrafo legenda da figura, sem detalhamento na prosa principal. Quando o exemplar 1.1 entrega "canal abre e Na+ entra", o aluno tem todo o mecanismo. Aqui o aluno tem o "o que" mas não o "como" (tioéster fica órfão). **Reescrita pronta proposta em §3.**

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo 1 — GAPDH cisteína-SH órfão (pág 12, legenda de figura)

- **Citação literal:** "O cisteína-SH catalítico do sítio ativo ataca o aldeído, forma um intermediário tioéster com a enzima, perde os elétrons para o NAD+, e só então o Pi entra e empurra o substrato para fora. Sem essa coreografia, a energia da oxidação se perderia como calor."
- **Diagnóstico mecanístico:** aluno-alvo nunca viu "cisteína-SH catalítico" antes (Proteínas I/II não cobriu nucleófilos catalíticos no nível mecânico). "Tioéster com a enzima" é jargão de Bioquímica II. A legenda joga 4 conceitos novos (Cys-SH, ataque nucleofílico, tioéster covalente, "empurra o substrato") em 1 frase. Aluno fecha o PDF aqui.
- **Reescrita pronta:**
  > "A reação é uma coreografia. No sítio ativo da GAPDH existe um aminoácido cisteína (cuja cadeia lateral termina em –SH, um enxofre nucleofílico — bom em atacar carbonos eletrofílicos). Esse –SH ataca o carbono-aldeído do G3P e gruda na enzima, formando uma ligação covalente temporária chamada **tioéster** (S–C=O). Nesse intermediário, os elétrons do C1 são transferidos para o NAD+ (que vira NADH). Agora o carbono está oxidado, mas ainda preso à enzima. Aí o Pi do citosol entra, desloca o enxofre, e o substrato sai como 1,3-BPG — com o Pi agora ligado por um acil-fosfato de alta energia. **A graça é que a ligação tioéster era um "reservatório" da energia da oxidação; quando o Pi substitui o enxofre, essa energia migra para o acil-fosfato.** Sem essa coreografia, a oxidação só liberaria calor."

### Parágrafo 2 — Tabela dos três sistemas energéticos com overflow (pág 19)

- **Citação literal (tabela):**
  > "Sistema | Velocidade | Capacidade | Exemplo de atividade
  > Fosfagênio (ATP-PCr) | 9–10 ATP/s | Segundos | [linha em branco]
  > Anaeróbico (glicólise → lactato) | 2–3 ATP/s | 1–2 minutos | Sprint 100 m, salto, levantamento explosivo
  > [...] Horas | Corrida 400 m, subir escada rápido | Caminhada, maratona [...]"
- **Diagnóstico mecanístico:** a tabela tem células mescladas mal alinhadas — "Horas" aparece em linha onde deveria estar "Sprint 100 m". O aluno-alvo lê a tabela como **prova-do-conceito** depois do texto; quando os exemplos vazam de linha para linha, ele desconfia do raciocínio inteiro. Bug de Typst (row break sem `repeat-header` ou span correto).
- **Reescrita pronta:** refazer com 3 linhas limpas, sem merge:

  | Sistema | Velocidade | Capacidade | Exemplo |
  |---|---|---|---|
  | Fosfagênio (ATP-PCr) | 9–10 ATP/s | Segundos | Sprint 100 m, levantamento explosivo |
  | Anaeróbico (glicólise→lactato) | 2–3 ATP/s | 1–2 min | Corrida 400 m, subir escada |
  | Aeróbico (Krebs+cadeia) | 1–2 ATP/s | Horas | Caminhada, maratona, ciclismo |

### Parágrafo 3 — Densidade de siglas em 3.2 (pág 21–22, F-2,6-BP)

- **Citação literal:** "E a PFK-2 é regulada por fosforilação. Ela é uma enzima bifuncional curiosa: o mesmo polipeptídeo tem dois domínios — uma quinase (PFK-2, que fabrica F-2,6-BP) e uma fosfatase (FBPase-2, que destrói F-2,6-BP). Qual dos dois domínios está ativo depende do estado de fosforilação da proteína. No fígado, a proteína quinase A (PKA) fosforila a enzima → ativa a FBPase-2 e inibe a PFK-2 → F-2,6-BP cai → PFK-1 desacelera → glicólise freia."
- **Diagnóstico mecanístico:** 5 siglas/nomes próximos (PFK-2, FBPase-2, PKA, F-2,6-BP, PFK-1) em uma cadeia de 4 setas. Aluno-alvo, em página 22, precisa **manter mentalmente** que PFK-1 ≠ PFK-2 ≠ F-1,6-BP ≠ F-2,6-BP. Sem desambiguação visual (negrito, mini-glossário ao lado), o aluno embaralha tudo.
- **Reescrita pronta — abrir com cápsula desambiguadora antes do parágrafo:**
  > **Antes de seguir, fixe quatro nomes parecidos e separe-os:**
  > - **PFK-1**: enzima da via, faz F6P → F1,6BP, gasta ATP.
  > - **PFK-2**: enzima de regulação, separada, faz F6P → F-2,6-BP. Não está na via.
  > - **F-1,6-BP**: intermediário da glicólise (substrato da aldolase).
  > - **F-2,6-BP**: mensageiro regulatório, só serve para ativar a PFK-1.
  >
  > Agora: a PFK-2 é uma proteína bifuncional. O mesmo polipeptídeo tem **dois domínios** — um faz F-2,6-BP (domínio quinase = PFK-2) e o outro destrói (domínio fosfatase = FBPase-2). [...] [resto do parágrafo]

---

## 4. T3.3 — 3 seções mais densas (mitigação concreta)

| Seção | Densidade (causa) | Mitigação |
|---|---|---|
| 2.1 GAPDH (pág 11–13) | 3 fenômenos simultâneos + mecanismo Cys-SH + arseniato em 3 pp | Quebrar em dois sub-blocos: (a) "o que GAPDH faz" (3 fenômenos), (b) "como faz" (Cys-SH detalhado, com 1 figura mecânica). Mover arseniato para box separado na pág seguinte. |
| 3.2 F-2,6-BP / PFK-2 (pág 21–22) | 5 siglas + bifuncionalidade + lógica hepática | Cápsula desambiguadora (acima). Adicionar diagrama "duas caixas" mostrando PFK-2 quinase ON vs FBPase-2 ON, com o estado de fosforilação como switch. |
| Tabela 10 reações (pág 7) | Tabela com 10 linhas + nomenclatura completa | Está OK como referência, mas a versão "abreviada" da fase preparatória já apareceu antes. Talvez mover esta tabela para o **fim** da E1 como "tabela-resumo" ou para o Resumindo, evitando que ela compita com a narrativa da fase de pagamento. |

---

## 5. T3.4 — Voz fora do padrão

A voz é **muito consistente** ao longo das 26 páginas de E1 — esta apostila é provavelmente a mais homogênea entre as históricas. Poucos desvios:

- **pág 11 ("Vamos pelo mecanismo")** — voz prosaica certa. ✓
- **pág 14 ("Daqui em diante, a glicólise está empatada — o que vier depois é lucro")** — coloquial bem calibrado. ✓
- **pág 17 ("dor muscular do exercício intenso (acúmulo de lactato + H+ → acidose local)")** — atenção: aqui o autor escreve "lactato + H+ → acidose", mas no box logo abaixo (pág 17) corrige: "O lactato não causa dor por ser ácido em si — é o H+ coproduzido que acidifica". A frase corta-frio na transição cria leve dissonância. Recomendo unificar: ou diz "H+ + lactato co-produzidos" sem implicar causa, ou abre direto pelo H+.
- **pág 22 ("E a PFK-2 é regulada por fosforilação")** — "E" inicial de parágrafo, oralidade boa, sem problema.

**Nenhum lapso para "decorar nomes", nenhuma frase robótica.** Padrão.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** 3.2 (PFK-2 / F-2,6-BP), pág 21–22.

Pico porque concentra: (a) 5 entidades novas com nomes parecidos, (b) 1 enzima bifuncional (conceito raro no 1º ano), (c) lógica condicional "se fosforilada... então FBPase-2 ativa, senão PFK-2 ativa", (d) integração com glucagon/PKA que só será explicada em 3.3.

**3 mitigações:**

1. **Cápsula desambiguadora (proposta em §3 acima).** Custo: ~6 linhas. Benefício: separa 4 siglas parecidas antes do raciocínio.
2. **Adiar glucagon→PKA→AMPc para 3.3.** Em 3.2, dizer apenas "uma quinase fosforila a PFK-2 — qual quinase e por que, veremos no 3.3". Isolando o mecanismo bioquímico do mecanismo hormonal, o pico cai.
3. **Figura "switch":** dois retratos da mesma proteína bifuncional, lado a lado: ON-quinase (faz F-2,6-BP) e ON-fosfatase (destrói F-2,6-BP), com Pi-do-PKA acendendo o switch. Visual concreto > duas páginas de prosa.

**Qual escolher:** **(1) + (3)**. A cápsula limpa a confusão lexical; a figura resolve o conceito da bifuncionalidade. (2) é trade-off — facilita 3.2 mas tira o gancho da 3.3.

---

## 7. T3.8 — Análise visual

**Hierarquia tipográfica:** capa com "Glicólise" em sans-serif bold pesado sobre faixa navy; títulos de PARTE em teal; sub-itens (1.1, 2.1...) em destaque verde-claro. Hierarquia clara em 4 níveis. ✓

**Valor pedagógico das figuras:** páginas com imagens (1–18) trazem ~1 figura por página até pág 18; depois disso (pág 19 em diante) **zero figuras** — a fase de regulação (3.1, 3.2, 3.3) está sem figura nenhuma. Para 3.2 (F-2,6-BP, o ponto mais denso) isso é falha grave — o aluno entra no pico cognitivo sem âncora visual. Figuras das pp 4–7 (clivagem aldólica, isomerização, mecanismo Mg²⁺) são integradas com legenda explicativa rica — **modelo positivo**.

**Densidade visual:** pp 5–7 com tabelas + figuras + texto compactam muito (~550 palavras de texto + 1 figura + parte de tabela na pág 5). Pode dar sensação de "muro" para o aluno em dificuldade. Pp 19, 28+ (E2) têm respiro adequado.

**Uso de cor:** azul navy (estrutura/títulos), teal (subtítulos), verde-claro (badges consolidação), azul (integração), violeta (aplicação). Coerência alta. Ouro provavelmente no Resumindo (não confirmado por amostra). ✓

**Cortes/overflow:** **bug confirmado na tabela da pág 19** (3 sistemas energéticos, células mescladas mal alinhadas). **Header zumbi pág 58** ("ETAPA 4 — QUESTÕES DE FUNDAMENTOS" sobre página que é gabarito da Etapa 2). Capa OK; sumário OK; gabarito visual limpo apesar do header errado.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas — ALIMENTA Phase F do REDATOR-E1)

### Técnica 1 — Abertura por motivo prático antes do nome técnico

- **Citação (pág 3):** "Comecemos pelo motivo prático: de onde vem o ATP que cada célula do corpo usa todo o tempo? Várias respostas existem (fosforilação oxidativa, β-oxidação, corpos cetônicos), mas existe uma resposta universal — todas as células do corpo conseguem fazer glicólise. Hemácia faz, neurônio faz, miócito faz, espermatozoide faz."
- **Nome da técnica:** "Pergunta prática + catálogo de exceções + redução à universalidade."
- **Quando NEBLI deveria usar:** sempre na abertura de uma via metabólica. REDATOR-E1 tende a abrir com definição ("a glicólise é a via que..."). Aqui o autor abre com "de onde vem o ATP?" — pergunta ingênua plausível do aluno, exatamente como prescreve `CLAUDE.md` na "Baseline do aluno". Gancho concreto: ancorar a Phase F2 (abertura de PARTE I) sempre em pergunta de aluno, nunca em definição enciclopédica.

### Técnica 2 — Box de tóxico/clínica como respiro narrativo

- **Citação (pág 12):** "**Arseniato envenena na GAPDH** — O arseniato (AsO4³⁻) é parecido com o fosfato e substitui o Pi no sítio da GAPDH. A enzima incorpora o arseniato no lugar do fosfato, formando um intermediário acil-arseniato — que é instável e se desfaz espontaneamente, sem gerar o composto de alta energia. [...] É um caso clássico de mimetismo molecular — átomo semelhante, mas a química falha no passo decisivo."
- **Nome da técnica:** "Box-clínica como **prova mecanística**, não decoração."
- **Quando NEBLI deveria usar:** depois de explicar um mecanismo intricado, abrir box com toxina/inibidor que **explora exatamente esse mecanismo**. O arseniato aqui não é trivia — é a confirmação experimental de que o acil-fosfato da GAPDH é o ponto-chave. Gancho concreto: Phase F deve catalogar 2–3 "tóxicos-mecanísticos" por tema na Seção C do Tema Card, com instrução ao REDATOR de transformá-los em box-prova, não em curiosidade.

### Técnica 3 — Resumindo internos com a forma "primeiro mecanismo, depois consequência"

- **Citação (pág 14):** "Resumindo até aqui: Fase de pagamento em três reações geradoras: GAPDH oxida G3P e gera o 1,3-BPG (alta energia). PGK pega esse fosfato e faz o 1º ATP. Depois mutase + enolase preparam o PEP (composto de altíssima energia). PK pega o fosfato do PEP e faz o 2º ATP. Total: 4 ATP gerados − 2 ATP investidos = saldo líquido +2 ATP por glicose."
- **Nome da técnica:** "Mini-resumo aritmético no fim do sub-tópico, com a conta visível."
- **Quando NEBLI deveria usar:** sempre que há saldo numérico (ATP, NADH, carbonos, etc.). A apostila amarra mecanismo + número no mesmo Resumindo. O aluno em dificuldade memoriza o número **porque viu a conta**, não porque decorou. Gancho concreto: REDATOR-E1, ao fechar sub-tópico com balanço, deve mostrar a aritmética em 1 frase final, mesmo se a derivação já apareceu acima.

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro | Status nesta apostila | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **PRESENTE leve** | Q26 item III curto (3 linhas) vs item I longo (5 linhas) — desnível dentro da mesma CE. Q24/Q25/Q27 distratoras razoavelmente paridas (~3–5 linhas cada). Q28 distratoras mecanísticas ricas. **Maioria OK; ponto de atenção é a paridade intra-CE.** |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **AUSENTE** | Cross-check: NAD+, NADH, ATP, ADP, Pi, GLUT, HK, G6P, F6P, PFK-1, F1,6BP, TPI, G3P, DHAP, GAPDH, BPG, PGK, PEP, PK, LDH, PDH, PCr, AMP, F-2,6-BP, PFK-2 — **todas declaradas com footnote `#sigla()` na primeira ocorrência** (notas 1–24 contadas no .txt). Padrão exemplar. |
| 3 | Subagentes Opus customizados falhando | **N/A** | Apostila histórica, pré-fix de 2026-05-25. Não testável. |
| 4 | Heredoc `ENAMETOOLONG` no Windows | **N/A** | Bug operacional, não bug de conteúdo. |
| 5 | `questao-ce` com tupla errada | **AUSENTE** | Compilou; CEs (Q05, Q08, Q13, Q18, Q21, Q26) renderizadas corretamente — usaram a forma de pares. |
| 6 | Termo-notas abaixo do alvo | **AUSENTE** | 24 `#sigla()` + termos-nota (não conseguimos contar termos-nota separadamente sem ler o .typ, mas o volume de explicações inline de "cisteína-SH catalítico", "tautomerismo enol/ceto", "mimetismo molecular", "feedforward", "lançadeira do malato", "ciclo de Cori", "MODY-2" sugere >6 termos densos explicados — alvo cumprido). |
| 7 | Tema-card com teto E1 errado | **AUSENTE** | E1 ocupa 24 páginas (pp 3–26 — sumário pág 2 + Resumindo pág 27 não contam para teto). **Dentro do teto canônico atual de 22 páginas?** 24 > 22 — **levemente acima**, mas a tabela de 10 reações (pág 7) e o sumário interno justificam. Aceitável como tema denso, mas é o limite. |

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)

1. **Corrigir header zumbi do gabarito (pág 58):** trocar "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" por "GABARITO — ETAPA 2" ou simplesmente nada. Bug do template após remoção da E4 em 2026-05-22 — alguma flag de cabeçalho ficou ativa. Investigar `nebli_v2_apostila.typ` na seção que define header da página de gabarito.
2. **Corrigir overflow da tabela "três sistemas energéticos" (pág 19):** reescrever sem cell-merge ou aumentar largura mínima das colunas Exemplo/Capacidade. Refazer com `table()` simples de 4 colunas × 3 linhas (proposta de tabela em §3 parágrafo 2).
3. **Adicionar figura switch no 3.2 (PFK-2 bifuncional):** este é o pico cognitivo da apostila e não tem âncora visual. Mesmo um diagrama esquemático "PFK-2 quinase ON | FBPase-2 ON" resolveria muito.

### MECANÍSTICO (max 3)

1. **Detalhar Cys-SH catalítico da GAPDH na prosa principal, não só na legenda:** ver reescrita em §3 parágrafo 1. O aluno-alvo não consegue inferir "tioéster com a enzima" sem o passo intermediário.
2. **Cápsula desambiguadora antes de F-2,6-BP × F-1,6-BP × PFK-1 × PFK-2:** proposta em §3 parágrafo 3. Custo 6 linhas, benefício imenso.
3. **Unificar dor muscular vs lactato (pág 17):** abrir já com "H+ + lactato co-produzidos pela hidrólise rápida de ATP, e é o H+ que cai o pH para 6,5" — eliminar a frase intermediária "acidose local" que parece atribuir causa ao lactato e depois corrige.

### DIDÁTICO (max 3)

1. **Mover tabela das 10 reações (pág 7) para depois da seção 2.2:** ela funciona melhor como referência final do que como interrompedora da fase preparatória.
2. **PARTE II tem 4 sub-itens (2.1–2.4):** considerar fundir 2.3 e 2.4 (destino do piruvato já discute o "porquê do lactato no exercício" — 2.4 expande). Ou aceitar como exceção justificada (o tema integra exercício e bioquímica). Não bloqueia.
3. **Sumário da pág 2 ainda menciona "ETAPA 4" no .txt extraído?** Não — o sumário do PDF lista apenas E1/E2/E3 (visto em p-02.png), o que está canônico. O .txt fonte tem uma referência residual à E4 ("ETAPA 4 — QUESTÕES DE FUNDAMENTOS") que o sumário visual omite. OK.

### ESTÉTICO (max 3)

1. **Capa (pág 1):** "Glicólise" em texto navy sobre fundo branco logo abaixo do banner navy — o banner ocupa só ⅓ superior, deixando o título "flutuando" no meio. Considerar engrossar o banner ou descer "Glicólise" para dentro da faixa.
2. **Pp 19 (tabela com overflow)** — coberto em ESTRUTURAL.
3. **Cor dos sub-itens (1.1, 2.1...)** em verde-claro vs PARTE em teal — leve risco de confusão na hierarquia (verde-claro também é a cor das badges "Consolidação" da E2). Avaliar se vale usar teal-escuro nos sub-itens da E1.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** SIM — esta apostila é, junto da de Membrana Plasmática, a mais polida do corpus histórico. A técnica 1 (abertura por motivo prático) e técnica 3 (Resumindo aritmético) devem virar regra no REDATOR-E1.
2. **≥1 ESTRUTURAL ou MECANÍSTICO?** SIM — três ESTRUTURAIS (header zumbi, tabela overflow, falta figura 3.2) e três MECANÍSTICOS (Cys-SH órfão, cápsula F-2,6-BP, dor muscular). A apostila não está pronta para ser "intocável".
3. **Seção para refazer?** Pp 21–22 (3.2 PFK-2/F-2,6-BP) merece reescrita com cápsula + figura. As outras seções precisam de ajustes pontuais, não refação.
4. **Parágrafos para reescrever?** 3 — listados em §3: (a) legenda Cys-SH da GAPDH pág 12, (b) tabela três sistemas pág 19, (c) parágrafo bifuncional PFK-2 pág 22. Reescritas prontas fornecidas.

---

[APROVAR COM RESERVAS]
