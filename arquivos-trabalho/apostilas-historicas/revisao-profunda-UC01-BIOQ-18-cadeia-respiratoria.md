# Revisão profunda Tier 3 — UC01-BIOQ-18-cadeia-respiratoria

**Tema (ancoragem):** Cadeia respiratória e fosforilação oxidativa
**Autor:** Marisa Helena (slides) / pipeline NEBLI (redação)
**Personagem:** aluno FMUSP 1º ano, dificuldade real (ensino médio + meses)
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

**Conceitos centrais que eu-aluno quero aprender:**
1. Por que existe a cadeia em vez de oxidar NADH direto no O₂?
2. Como o gradiente de prótons vira ATP (motor rotativo)?
3. Por que cianeto mata e DNP aquece — qual é a diferença mecanística?

**Temas vizinhos que NÃO são esse:** ciclo de Krebs em si; β-oxidação em si.

**Nota metodológica:** análise visual do PDF (T3.8) ficou parcial — `pdftoppm` disponível mas Read tool rejeitou. Avaliação visual fez triangulação a partir de (a) `estrutura.json` (palavras/imagens por página), (b) header repetido no txt, (c) layout do Resumindo extraível por colunas. Onde a evidência visual direta seria necessária, marquei [VISUAL-NA].

---

## 1. Pontos de parada (simulação aluno linha-a-linha)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Capa + meta | OK | 1 | Limpa, declara onde estudar. |
| Sumário | OK | 2 | 9 subseções nomeadas — orienta. |
| Intro-box | OK | 3 | "Metabolismo aeróbio finalmente cobra a fatura" — engancha. |
| 1.1 termodinâmica | **[STOP suave: pág 3]** | 3 | Salto "220 kJ/mol... 30 kJ/mol... 7 ATP" sem pausar em "o que é 1 kJ/mol intuitivamente". Aluno em dificuldade não tem âncora para essa grandeza. Analogia da hidrelétrica vem DEPOIS, salva — mas tarde. |
| 1.2 redox / E°` | **[STOP duro: pág 4]** | 4 | "ΔG° = -nFE°'" jogado sem reativar pré-requisito (o que é F? por que -n? o que significa F⋅V virar kJ?). Aluno fecha o PDF aqui. Os pontos de E°' escalonados (FMN, Fe-S, etc.) viram lista densa de números sem mapa visual. |
| 1.3 onde acontece | OK | 5 | Boa narrativa membrana externa/interna. Cristas com analogia 5–10× ancora bem. |
| 2.1 Cx I e II | OK | 7 | "Truque elegante" da exclusão de prótons funciona; nome formal vem DEPOIS do mecanismo (canônico NEBLI). |
| 2.2 Ciclo Q | **[STOP médio: pág 8–9]** | 8 | Analogia do "double buffer" é nerd-só-pra-quem-já-sabe-programar. Aluno de medicina não decodifica. Em seguida vem "2 QH₂ entram, 1 QH₂ sai, 1 Q sai, 2 e⁻ entregues, 4 H⁺ bombeados" — contabilidade densa sem figura passo-a-passo. |
| 2.3 Cx IV / estequiometria H | **[STOP médio: pág 10]** | 10 | "4 H⁺ removidos da matriz no total, mas só 2 atravessam como bomba; os outros 2 viraram água" — esta é exatamente a pegadinha do tema, e está explicada em 1 frase compacta. Aluno relê 3 vezes. |
| 3.1 ATP sintase | OK | 11 | O–L–T ancorado bem; "ATP não é fabricado pelo gasto, ele se forma espontâneo" é o insight certo. |
| Cálculo 3,7 H⁺/ATP | **[STOP duro: pág 12]** | 12 | "2,7 + 1 + 0,3" cai sem motivação — o 0,3 do antiporte ADP/ATP é gratuito. Aluno aceita por fé. |
| 3.2 saldo glicose | OK | 12 | Honestidade ao explicar "38 vs 30–32" como refinamento, não erro, é exemplar — ALIMENTA Phase F. |
| 3.3 inibidores/desacopl. | OK | 14–16 | DNP→hipertermia→retirada do mercado, UCP1→neonato — clínica curta e potente. |
| Conclusão integradora | OK | 17 | Três conceitos numerados. Bom fecho. |
| Faixa-resumo pág 18 | **[VISUAL-NA]** | 18 | Texto extraído sugere tabela 3×3 (Entrada/Descida/Síntese × Quem manda/Inibidor/Por que O₂). Possível corte/overflow em coluna estreita. |
| Resumindo 2 col | OK | 19 | 12 seções, ~25–40 palavras cada — dentro do canônico. |
| Q1–Q30 + Q1–Q5 disc. | OK | 20–39 | Distratoras geralmente longas e mecanísticas (ver T3.10). |

**Resumo dos STOPs:** 4 paradas (1 dura em pág 4, 1 dura em pág 12, 2 médias). A pág 4 é onde mais alunos perdem o tema permanentemente.

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria 4 (Magnitudes ancoradas e comparação externa) — ATINGIDO PARCIALMENTE.**

**Trecho do PDF (pág 3):**
> "Se NADH + ½O₂ → NAD⁺ + H₂O libera 220 kJ/mol — e a síntese de um ATP custa 30 kJ/mol —, em tese bastaria um passo único e a célula ganharia 7 ATP de uma vez."

**Comparação com padrão Categoria 4:** o exemplar canônico ancora número em comparação externa concreta (ex.: "concentração intracelular de K⁺ ≈ 140 mM, ~30× a extracelular — a mesma diferença entre água doce e água do mar"). Aqui, 220 kJ/mol e 30 kJ/mol aparecem cruas. A analogia da hidrelétrica vem 1 parágrafo depois e salva, mas a ancoragem ideal seria embutida no momento do número.

**Reescrita Categoria 4:**
> "Soltar 220 kJ/mol num átimo é como derrubar 7 ATPs de uma vez — ou, mais palpável, é a energia liberada quando você queima ~5 mg de glicose. Numa única reação, isso vira calor. A célula precisa pegar essa energia em moedas pequenas — e a maior moeda que ela troca é o ATP, a 30 kJ/mol cada. Tudo no metabolismo é a aritmética entre essas duas escalas."

**Categoria 7 (Analogia construtiva) — DUAS analogias, uma exemplar, uma problemática.**

**Trecho exemplar (pág 3):**
> "A célula transformou um penhasco numa escada com patamares, e em cada patamar há uma bomba que captura um pedacinho da energia. É a mesma lógica de uma usina hidrelétrica em cascata."

Funciona porque (a) é macroscópico, (b) é uma máquina concreta (bomba+queda), (c) o aluno já viu hidrelétrica. **ALIMENTA Phase F.**

**Trecho problemático (pág 8):**
> "Pense no ciclo Q como um double buffer: o complexo processa um elétron de cada vez para o citocromo c..."

"Double buffer" é jargão de programação. Aluno de medicina não tem esse encaixe. Cat 7 diz: "Quando a analogia mascara o mecanismo" — NÃO usar. Aqui mascara.

**Reescrita Categoria 7:**
> "Pense no ciclo Q como uma roleta de banco com duas filas: o citocromo c só atende 1 cliente por vez, mas o ubiquinol chega trazendo 2 elétrons no mesmo bolso. O Complexo III separa os dois: manda um pela fila do citocromo c e usa o segundo para 'recarregar' outro ubiquinol vazio que estava esperando — esse é reciclado e volta para a fila de novo. No saldo, 2 ubiquinóis entram, mas 1 deles é literalmente refeito dentro do complexo, e o bombeamento de prótons dobra."

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação obrigatória)

### Parágrafo fraco 1 — pág 4, ΔG° = -nFE°'

**Citação literal:**
> "A diferença é 1,14 V — equivalente a ΔG° = -2 × 96.500 × 1,14 = -220 kJ/mol."

**Diagnóstico mecanístico:** lança a equação canônica de Nernst-eletroquímica sem retomar o pré-requisito. O aluno de 1º ano viu isso uma vez em química geral, há 6 meses. Os símbolos `n`, `F`, `E°'` aparecem sem reabertura. O sinal negativo da ΔG° não é explicado (espontaneidade). O resultado parece mágico: por que multiplicar voltagem por número de Faraday dá energia?

**Reescrita pronta:**
> "Esses 1,14 V de diferença viram energia química quantificável pela equação ΔG° = −n·F·E°', onde n é o número de elétrons transferidos (aqui n=2, porque NADH cede um par) e F é a constante de Faraday (96.500 C/mol) — basicamente o fator de conversão entre voltagem e energia por mol de elétrons. O sinal negativo só está dizendo que a reação é espontânea (a energia sai). Substituindo: ΔG° = −2 × 96.500 × 1,14 = −220 kJ/mol. É essa energia, e exatamente essa, que a célula precisa capturar em pequenos saltos."

---

### Parágrafo fraco 2 — pág 8, ciclo Q em contabilidade

**Citação literal:**
> "No ciclo Q, duas moléculas de QH₂ se ligam ao Complexo III, mas em sítios diferentes. Uma libera seus 2 elétrons num caminho bifurcado: um elétron vai para o citocromo c (via citocromo c1), e o outro elétron volta dentro do complexo via citocromo b, sendo usado para reduzir outra molécula de Q de volta a QH₂. No saldo final: 2 QH₂ entram, 1 QH₂ sai (reciclado), 1 Q sai, 2 elétrons foram entregues ao citocromo c, e 4 prótons foram bombeados."

**Diagnóstico mecanístico:** o parágrafo conta 2 voltas do ciclo simultaneamente sem deixar claro que são 2 voltas. O aluno tenta encaixar "2 QH₂ entram em sítios diferentes" como se fosse uma única reação simultânea e empaca. Faltam os nomes dos sítios (Qo e Qi), que ajudariam a separar "onde elétron 1 sai" de "onde QH₂ vai ser refeito". Saldo dado de uma vez (4H⁺) sem detalhar quantos vieram da matriz vs quantos eram do próprio QH₂.

**Reescrita pronta:**
> "O ciclo Q acontece em duas voltas sucessivas, e separá-las mentalmente é o segredo. **Volta 1:** um QH₂ se encaixa no sítio Qo (lado externo da membrana). Ele libera 2 H⁺ no espaço intermembranar (eis 2 prótons bombeados) e seus 2 elétrons se separam — um vai pela rota 'rápida' (citocromo c1 → citocromo c, sai do complexo); o outro vai pela rota 'lenta' (citocromo b → sítio Qi do outro lado), onde reduz uma Q oxidada à semiquinona (QH•). **Volta 2:** chega outro QH₂ no Qo, repete o mesmo passo (mais 2 H⁺ jogados fora, 1 elétron pro cit c, 1 elétron pro Qi). Mas dessa vez o elétron que chega no Qi completa a semiquinona da volta 1 — que pega 2 H⁺ da matriz e vira QH₂ de novo, reciclado. **Saldo das duas voltas:** entraram 2 QH₂, saíram 1 QH₂ (reciclado) + 1 Q, foram bombeados 4 H⁺ (2 do espaço intermembranar + 2 da matriz consumidos para recriar QH₂, que ao oxidar de novo cospe seus 2H⁺ pra fora — assim a matriz "paga" 2 H⁺ no líquido). 2 elétrons entregues ao cit c. O truque é genial: 1 Q reciclado dentro do complexo dobra a eficiência de bombeamento."

---

### Parágrafo fraco 3 — pág 12, custo 3,7 H⁺/ATP

**Citação literal:**
> "Mas é preciso somar mais 1 H⁺ para importar Pi (via simporte com H⁺) e 0,3 H⁺ para o custo do antiporte ADP/ATP — total 3,7 H⁺ por ATP entregue ao citosol."

**Diagnóstico mecanístico:** o "0,3 H⁺" é o que mais frita o aluno. De onde vem 0,3? Por que fracionário? O texto não explica que o antiporte ADP/ATP move uma carga negativa líquida pela membrana (ADP³⁻ entra, ATP⁴⁻ sai), aproveitando o ΔΨ — e que esse "consumo de ΔΨ" equivale a ~0,3 H⁺ se convertido em equivalentes de prótons. Sem isso, parece numerologia.

**Reescrita pronta:**
> "Aqui aparece um número estranho: 0,3 H⁺ a mais para o antiporte ADP/ATP. Não é meio próton físico — é o custo equivalente. O transportador troca ADP³⁻ (entra) por ATP⁴⁻ (sai), o que tira uma carga negativa líquida da matriz, ou seja, drena ΔΨ (o componente elétrico da força próton-motriz). Como ΔΨ vale ~140 mV dos 200 mV totais, o equivalente em prótons gastos é cerca de 0,3 H⁺ por ATP entregue. Some: 2,7 H⁺ (motor) + 1 H⁺ (Pi entra com 1 H⁺ acoplado) + 0,3 H⁺ (drenagem elétrica do antiporte) = 3,7 H⁺ por ATP útil no citosol."

---

## 4. T3.3 — 3 seções mais densas + mitigação

| Seção | Densidade (sintoma) | Mitigação concreta |
|---|---|---|
| **1.2 — escala de E°' dos componentes (pág 4)** | 7 valores de E°' em série encadeada de 9 linhas sem visual. Aluno vê números pulando. | Inserir tabela vertical 2 colunas (componente \| E°') ordenada de baixo pra cima, ou figura "escada termodinâmica" com cada degrau rotulado. Texto fica como caption. |
| **Ciclo Q (2.2, pág 8–9)** | Contabilidade em duas voltas comprimida em 1 parágrafo (ver T3.2). | Reescrever em 2 voltas explícitas (rascunho na T3.2 acima) + diagrama com setas marcadas "1ª volta" e "2ª volta". |
| **Cálculo do saldo de glicose (3.2, pág 12)** | "2 + 2 + 8×2,5 + 2×1,5 + 2×(1,5 ou 2,5) = 30–32" em texto corrido. | Trazer em tabela vertical com linhas (glicólise, Krebs, NADH mit, FADH₂, NADH cit-malato, NADH cit-glicerol) e coluna "ATP". Fechar com soma destacada. |

---

## 5. T3.4 — Voz fora do padrão

**Citação 1 (pág 8):**
> "Pense no ciclo Q como um double buffer..."

Jargão de programação fora do registro do aluno de medicina. Quebra a voz de monitor-explicando.

**Citação 2 (pág 14):**
> "A enzima é grande (13 subunidades em humanos)..."

Voz neutra-de-livro-texto, sem narrativa. Compare com o parágrafo do Cx I, que abre com "é a maior das máquinas da cadeia" — bem mais NEBLI.

**Citação 3 (pág 18, faixa-resumo) [VISUAL-NA literal, mas extraído do txt]:**
> "NADH entra no I (bombeia 4 H+); FADH2 entra no II (não bombeia). Ambos terminam na CoQ."

Telegráfico ao ponto de virar lista — é faixa de síntese, justifica até certo ponto, mas perde a voz dialogada que o resto do resumo cultiva. **Avaliação:** aceitável dado o formato compactado, mas o restante do PDF mostra que dá pra ser conciso E dialogado simultaneamente.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** §1.2 (redox + ΔG°) — pág 4.

Esta é a página onde tudo se decide. Se o aluno não absorve E°' como conceito + ΔG° = −nFE°', os Complexos depois viram nomes sem contexto. É carga conceitual + carga simbólica + carga matemática num espaço de 1 página.

**3 mitigações possíveis:**

1. **Cortar o cálculo** — manter só a narrativa "diferença de potencial vira energia" sem a equação. ↓ carga, mas o aluno perde a ferramenta para reproduzir o cálculo.
2. **Cálculo em box separado** — `.atencao-box` ou caixa em destaque para a equação, explicando símbolo por símbolo (rascunho na T3.2). Texto principal narra mecanismo, box matematiza.
3. **Pré-aula em 3 frases** — antes de §1.2 abrir, mini-recapitulação de pré-requisito: "Lembrando da química geral: cada par redox tem um E°' que mede 'fome por elétrons'. Quanto mais positivo, mais 'come' elétrons. Quando dois pares se encontram, elétrons fluem do menos positivo para o mais positivo, espontaneamente — e essa diferença de fome vira energia química."

**Qual escolher:** **opção 2 (box separado)** combinada com **3 (pré-aula de 3 frases)**. É a única combinação que mantém o rigor matemático sem afogar o aluno. Cortar (opção 1) trai a missão "do básico ao aprofundado".

---

## 7. T3.8 — ANÁLISE VISUAL

[Limitação: pdftoppm bloqueado pela Read tool. Análise feita por proxy estrutural — densidade de palavras/imagens em estrutura.json + layout extraível por colunas no txt.]

**Hierarquia tipográfica** — pela estrutura: header "NEBLI ETAPA X" repetido em cada página, com subsections "PARTE I / II / III" em destaque. Sumário (pág 2) lista 9 subseções nomeadas. Hierarquia OK em 3 níveis (PARTE > subseção 1.x > parágrafo). Não há evidência de h4.

**Valor pedagógico das figuras:**
- Pág 4–16 têm 1–2 imagens cada (10 imagens nessa faixa).
- Pág 17 em diante (Conclusão integradora + Resumindo + Etapas 2/3): **ZERO imagens**.
- Etapa 1 termina com 14 imagens distribuídas em 14 páginas. Por subtópico canônico NEBLI são 3 PARTES com 3 subseções cada (9 subseções) → 14 figuras = ~1,5 por subseção. Meta canônica NEBLI é mínimo 3 por PARTE da E1 (= 9 mínimo). **ATINGE meta de 3/parte com sobra.**
- Faltam figuras nas distratoras-densas da E2 (esperado, é o canônico) e na faixa-resumo da pág 18 (também esperado).
- [VISUAL-NA] não posso julgar se as imagens TÊM legenda integrada ou se foi `#figura-nebli` solto. O texto sugere captions embutidos ("Organização da cadeia em quatro complexos. Os elétrons entram pelo Complexo I...") — bom sinal.

**Densidade visual:**
- Páginas 17 a 36 (~20 páginas) sem imagens. Murão de texto.
- Etapa 2 com 30 questões em ~15 páginas = ~2 questões/pág. Possível parede de texto sem respiro entre questões (queremos confirmar visualmente, mas estrutura sugere).
- Pág 14 cai pra 148 palavras + 2 imagens — provavelmente página com espaço em branco propositais para acomodar lançadeiras. OK.
- Pág 36 com 70 palavras — provável quebra de página fim-de-questão.

**Uso de cor:** [VISUAL-NA]. Pelo canônico NEBLI, esperamos 3 cores na E2 (Consolidação azul / Integração roxa / Aplicação laranja-vermelho). O txt mostra a categoria nominal de cada questão, mas não a cor renderizada. Faixa-resumo da pág 18 provavelmente em navy/dourado (padrão).

**Cortes/overflow:** [VISUAL-NA]. Nenhum sinal indireto no txt. As 4 distratoras de Q26-Q30 têm parágrafos de 4-6 linhas cada — não tão extensos a ponto de causar overflow.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### Técnica 1 — Honestidade pedagógica sobre divergência livro-texto

**Citação literal (pág 12):**
> "Esses são os valores modernos. Os livros mais antigos (e o próprio slide do prof) ainda trazem o 'P/O = 3 e P/O = 2', resultando no clássico saldo de 38 ATP por glicose. A discrepância não é erro — é refinamento. O 38 ignorava os custos de transporte de ADP/Pi; o 2,5/1,5 conta esses custos. Em prova, prestar atenção ao enunciado — se pedirem o valor clássico, é 38; se pedirem o moderno, é 30–32."

**Nome da técnica:** "Reconciliação de versões conflitantes do mesmo conceito" — ou, mais curto, **"refinamento, não erro"**.

**Quando NEBLI deveria usar:** sempre que o slide do professor traz valor histórico/clássico e o livro-texto moderno traz outro número, NEBLI deve (a) reportar os dois, (b) explicar o porquê da divergência, (c) dar regra de bolso "em prova, se pedirem X, é Y". Aplicável a: P/O ATP, número de cromossomos (com/sem cromátide-irmã), velocidade de PA, tempo de meia-vida farmacológica em populações diferentes, valores normais lab que variam entre serviços. Hook concreto para REDATOR-E1: adicionar regra ao redator-e1.md § "Magnitudes": "Se slide-prof e livro-texto divergem, declare a divergência, explique o porquê, e dê regra-de-prova."

### Técnica 2 — Nome técnico DEPOIS do mecanismo

**Citação literal (pág 7, abrindo Cx I):**
> "O Complexo I é a porta principal — e é a maior das máquinas da cadeia. Formado por cerca de 45 cadeias polipeptídicas, contém 1 FMN e 6–7 centros Fe-S. Recebe os elétrons do NADH na face matricial e os entrega à coenzima Q, do outro lado da membrana. Ao fazer isso, bombeia 4 prótons da matriz para o espaço intermembranar. Nome formal: NADH-coenzima Q oxidorredutase."

**Nome da técnica:** **"Nome formal ao final, como recompensa"**. O aluno entende a função antes de receber o nome técnico massudo.

**Quando NEBLI deveria usar:** **sempre** — é canônico do projeto (CLAUDE.md baseline 2026-05-25: "dá o nome técnico só DEPOIS do mecanismo entendido"). Este resumo executa isso com disciplina. Hook concreto: usar como exemplar a ser ADICIONADO à Categoria 1 do EXEMPLARES.md (Explicação mecanística parágrafo-por-parágrafo) — abertura canônica "É a porta principal — [função em 2-3 frases] — Nome formal: X."

### Técnica 3 — Clínica curta, potente, integrada (não como apêndice)

**Citação literal (pág 9):**
> "Detalhe clínico: esse mesmo citocromo c, quando vaza para o citosol via abertura do poro de permeabilidade transitória mitocondrial, dispara apoptose — sua escapada da mitocôndria é um sinal de morte celular programada."

E **pág 15-16:**
> "O cianeto merece atenção clínica especial. Bloqueia o Complexo IV → cadeia toda para → célula não consegue usar o O₂ disponível no sangue → 'hipóxia histotóxica' (o oxigênio está lá, mas a célula não pode usá-lo). É a fome energética com sangue vermelho-cereja..."

**Nome da técnica:** **"clínica injetada no parágrafo bioquímico, não em box separado"**. A clínica entra como UMA frase consequência do mecanismo recém-explicado, não como seção apartada "Aplicações clínicas".

**Quando NEBLI deveria usar:** quando a clínica deriva diretamente do mecanismo (apoptose por cit c, hipóxia histotóxica por CN⁻, hipertermia por DNP). Diferente de `.clinica-box`, que é para destaque visual em aplicação clínica de fôlego maior. Hook concreto para REDATOR-E1: criar Categoria 18 no EXEMPLARES.md — "Cláusula clínica de uma frase como consequência mecânica" — diferente da `.clinica-box` (Cat 9 do EXEMPLARES). Tem efeito de "ah, isso serve pra alguma coisa real" sem quebrar o fluxo da bioquímica.

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro | Status | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **AUSENTE** | Q26 (DNP), Q27 (UCP1 neonato), Q28 (cianeto C/E), Q29 (mitocôndria isolada 4-condições), Q30 (hipertermia maligna). Distratoras de Q26 e Q30 longas, mecanísticas, com confusões plausíveis (DNP-como-inibidor-de-Cx-IV; halotano-como-cianeto). Ratio correta/distratora estimado ≤ 1,25. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **AUSENTE (mostly)** | Auditoria por amostra: ATP, GTP, NADH, FADH₂, NAD⁺, FAD, ADP, Pi, ROS, UCP1, FMN — todas têm footnote na 1ª aparição (footnotes 1–17 visíveis). DNP recebe nota 15. CoA, GDP, cAMP, AMP, NADP⁺ — **não auditável sem grep** (não aparecem no txt nas seções amostradas, podem nem aparecer). Provável OK. |
| 3 | Subagente Opus errando tema | **N/A** | Resumo já fechado; este erro é do pipeline de geração, não detectável no produto final. (E justamente o slug aqui — cadeia respiratória — é o nome do tema-contaminação que disparou o erro #3 em 25/5; o resumo em si, porém, está sobre cadeia respiratória, então não há contaminação aqui.) |
| 4 | Heredoc `ENAMETOOLONG` Windows | **N/A** | Erro de processo de gravação, não auditável no PDF. |
| 5 | `questao-ce` formato tupla | **AUSENTE** | Q04, Q09, Q22, Q28 são C/E; renderizaram OK (texto extraído sequencial I/II/III/IV). |
| 6 | Termo-notas abaixo do alvo | **PRESENTE (leve)** | Conto no txt: `porinas`, `lançadeira de glicerol-3-fosfato`, `cristas`, `2,4-dinitrofenol (DNP)`, `UCP1`, `tecido adiposo marrom`. **6 termo-notas**. Está no piso do alvo canônico (6–8), mas dentro. Falta termos como `força próton-motriz`, `quimiosmótica`, `hipóxia histotóxica`, `rodanase` — qualquer um deles teria movido pra 7-8. |
| 7 | Tema-card teto E1 errado | **N/A** | Resumo fechado tem 17 páginas de E1 (pág 3–17 + faixa-resumo 18). Dentro de teto 22. OK. |

**Resumo:** dos 7 erros checáveis, **6 ausentes e 1 leve** (termo-notas no piso). Excelente calibração geral. Erro #1 (paridade distratoras) merece destaque positivo — é exatamente o que mais erra historicamente.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **§1.2 (redox + ΔG°) precisa de quebra estrutural.** Hoje é 1 página densa com escada de E°' embutida no parágrafo. Separar: (a) box matemático para ΔG° = −nFE°' com símbolos explicados, (b) figura/tabela vertical para a escada de E°', (c) parágrafo de pré-requisito de 3 frases antes do cálculo.
2. **Ciclo Q (§2.2) precisa de reestruturação em 2 voltas explícitas.** Hoje é 1 parágrafo contábil. Reescrever em "Volta 1 / Volta 2 / Saldo" (rascunho na T3.2 parágrafo 2). Idealmente acoplado a figura em 2 painéis. Sem isso, o conceito central do tema fica opaco.
3. **Inserir tabela de saldo de glicose (§3.2).** Linha por fonte (glicólise / Krebs / NADH mit / FADH₂ / NADH cit malato-asp / NADH cit glicerol-P) × coluna ATP, com soma final. Substitui aritmética em prosa.

### MECANÍSTICO (max 3)
1. **Custo 0,3 H⁺ do antiporte ADP/ATP precisa de mecanismo, não numerologia** (rascunho na T3.2 parágrafo 3). Sem o argumento ΔΨ → drenagem elétrica → equivalente em H⁺, o aluno só decora.
2. **Estequiometria de H⁺ no Cx IV (pág 10) precisa de mais 2 frases** distinguindo "H⁺ que viraram água" vs "H⁺ bombeados". Hoje a frase decisiva está comprimida: "4 H⁺ removidos da matriz no total — mas só 2 deles atravessam a membrana como 'bomba'; os outros 2 viraram água." Expandir em parágrafo.
3. **Lançadeira malato-aspartato precisa de "como o oxaloacetato volta"** (pág 12-13). O texto diz "o oxaloacetato volta como aspartato (via transaminação)" — uma frase. O aluno não enxerga o loop. Acrescentar nome do par α-cetoglutarato/glutamato e mostrar que sem isso a lançadeira para.

### DIDÁTICO (max 3)
1. **Substituir analogia "double buffer" (pág 8) por analogia macroscópica.** Rascunho "roleta de banco com duas filas" na T3.1.
2. **Ancorar 220 kJ/mol em escala palpável** logo na 1ª aparição (pág 3). Sugestão: "energia liberada queimando ~5 mg de glicose" ou "calor de ~50 mL de água esquentando 1 °C".
3. **Adicionar 1–2 termo-notas para chegar a 7–8** — candidatos óbvios: `força próton-motriz`, `hipóxia histotóxica`, `quimiosmótica`. Todos termos densos que o aluno de 1º ano vê pela primeira vez.

### ESTÉTICO (max 3)
1. **Páginas 17–36 sem nenhuma figura.** [VISUAL-NA confirmar], mas mesmo no canônico NEBLI a E2 sem nenhum recurso visual (faixa de cor por categoria conta, mas é embutida) cria fadiga. Considerar 1 figura motivadora por bloco de 10 questões (ex.: figurinha pequena com cianeto na faixa de Aplicação).
2. **Faixa-resumo pág 18 [VISUAL-NA]** — texto extraído sugere telegrama. Verificar se está visualmente equilibrada ou se vira "tabela seca". Se for o segundo caso, restaurar 1 frase de voz por célula (ex.: "Quem manda na velocidade: ADP — quanto mais ADP livre, mais a sintase gira").
3. **Header "NEBLI" repetido em toda página** — confirmado no txt. OK, esperado, mas chamando atenção caso o auditor visual veja repetição cansativa.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM** — com ressalva: §1.2 (redox/ΔG°) e §2.2 (ciclo Q) precisam de ajuste estrutural antes de virar exemplar. Mas as 3 técnicas extraídas em T3.9 (refinamento-não-erro / nome-formal-no-fim / clínica-uma-frase) são exemplares fortes para alimentar Phase F.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM** — 6 itens entre ESTRUTURAL+MECANÍSTICO acima. Os 3 ESTRUTURAIS são bloqueantes para o resumo virar exemplar; os 3 MECANÍSTICOS são alta prioridade.
3. **Seção para refazer?** **§2.2 (Coenzima Q, ciclo Q e citocromo c)** — completa, do "double buffer" até a contabilidade dos 4 H⁺. Rascunho de reescrita na T3.2 parágrafo 2.
4. **Parágrafos para reescrever:** **3.**
   - Pág 4 — "A diferença é 1,14 V — equivalente a ΔG° = -nFE°'..." (rascunho na T3.2-#1).
   - Pág 8 — "No ciclo Q, duas moléculas de QH₂ se ligam..." (rascunho na T3.2-#2).
   - Pág 12 — "Mas é preciso somar mais 1 H⁺ para importar Pi e 0,3 H⁺ para o antiporte..." (rascunho na T3.2-#3).

---

[APROVAR COM RESERVAS]
