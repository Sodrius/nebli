# Tema Card — Genética bacteriana

## Seção A — Escopo

- **Tema:** Genética bacteriana — o genoma que se copia, se altera e circula entre células
- **Slug:** `micro-06-genetica-bacteriana` (entrada em `banco/aulas_uc03.yml`, componente Microbiologia)
- **Disciplina:** UC03 · Microbiologia (Profa. Assoc. Carla Romano Taddei, ICB II–USP)
- **Onde estudar:** Trabulsi & Alterthum, *Microbiologia*, capítulos de genética bacteriana e de elementos genéticos móveis · Murray, *Microbiologia Médica*, capítulo de genética bacteriana · Madigan (Brock), *Biology of Microorganisms*, replicação, mutação e transferência horizontal
- **Alvo de páginas E1:** piso 2, **teto 15** — alvo real 13–14 · **10 subtópicos** (3 + 3 + 4), 470–540 palavras cada, ~5.100 palavras de miolo
- **Distribuição E2:** PADRÃO → 10 Consolidação · 15 Integração · 5 Aplicação

### Teto histórico e degrau (substitui o antigo campo `profundidade:`)

- **Teto histórico desta aula** (`consultar.py --slug micro-06-genetica-bacteriana`, 6 subquestões de 2017 a 2025): o plasmídeo nomeado como *molécula de DNA circular de replicação autônoma que carreia genes de resistência*; os mecanismos de resistência que a casa cobra por escrito — β-lactamase e mutação de topoisomerase (gyrA/parC) — pedidos como explicação, não como marcação; a distinção entre **adquirir** resistência por plasmídeo e **desenvolvê-la** por mutação; e, em 2025, a leitura de sequenciamento + bioinformática para identificar espécie por gene espécie-específico e prever fenótipo de resistência (blaTEM/ROB-1, ftsI/PBP3, gyrA/parC).
- **Degrau que a E1 acrescenta:** (a) *por que* a mutação em gyrA confere resistência — a girase é a única enzima que introduz supertorção negativa gastando ATP, e é isso que a torna alvo; (b) o **integron** como plataforma de captura de cassetes, que explica por que a resistência chega em bloco e não gene a gene; (c) a **replicação por círculo rolante** na conjugação, que explica por que a doadora não perde o plasmídeo e por que a receptora vira doadora — a cinética explosiva do surto; (d) a **resposta SOS** induzida por quinolona e β-lactâmico, que aumenta a taxa de mutação e a transferência do próprio antibiótico que deveria conter a bactéria; (e) a **hemimetilação GATC** como o sinal que diz ao reparo qual fita é a nova e ao oriC que ainda não é hora de reiniciar; (f) o limite da bioinformática — gene presente não é gene expresso, e o antibiograma continua sendo a referência fenotípica.

### Hierarquia de fontes aplicada (canônico 2026-09-03)

1. **O slide guiou o fluxo** — a ordem do resumo é a das 44 telas: nucleóide e supertorção → estrutura do DNA → tamanho de genoma e plasmídeo → replicação e polimerases → mutação e mutagênicos → transformação, transposons, transdução, conjugação, recombinação → DNA recombinante → operon lac → CRISPR-Cas9.
2. **A prova indicou o quanto ir a mais** — as 6 subquestões MB do acervo fixaram o teto (plasmídeo, mecanismos de resistência, sequenciamento/bioinformática); o degrau está declarado acima.
3. **Livros e outras fontes indicaram assuntos laterais** — integron, teste de flutuação de Luria–Delbrück, conversão lisogênica e reparo por excisão entram como mecanismo lateral integrado à prosa, sem redefinir escopo.

### Recorte slide × tema

O slide é largo: gasta 10 telas (7–16) revisando **estrutura do DNA** — nucleotídeo, pareamento A=T / G≡C, ligação fosfodiéster, desnaturação/renaturação — conteúdo que o aluno já viu em Biologia Molecular.

**Recorte declarado:** a revisão de estrutura **não vira subtópico**. Entra como retomada de 2–3 frases em 1.1 (esqueleto fosfodiéster, antiparalelismo, 2 × 3 pontes de hidrogênio) e, onde ela de fato ensina algo novo, é realocada para onde rende mecanismo — **desnaturação/renaturação migra para 3.4**, porque é a base física do anelamento de *primer*, da hibridação e da PCR, e porque o número de pontes de hidrogênio explica a dependência do Tm do conteúdo GC. A tela de RNA secundário (42) entra como uma linha dentro de 3.3 (dobramento do crRNA), não como bloco. Fica de fora: farmacologia dos antimicrobianos (é a aula `micro-05`), fisiologia do crescimento (`micro-02`) e fatores de virulência (`micro-07`) — a conversão lisogênica aparece aqui como *mecanismo de transferência*, não como catálogo de toxinas.

### Prioridades desta corrida (do `MEMORY.md` § Diário de revisões)

1. **Registro científico (peso alto, não decai).** Nomenclatura exata com a definição na mesma frase; quantidade sempre com unidade; filtro das três funções aplicado subtópico a subtópico.
2. **Teto de 15 páginas / 8–10 subtópicos.** O slide comporta 14 subtópicos; a alavanca 2 do `ERROS.md` F4 (fundir irmãos) fechou em 10 — estrutura do DNA fundida em 1.1 e 3.4, restrição+CRISPR fundidos em 3.3.
3. **Consolidação decoreba.** Q01–Q10 em recall direto, alternativas de 10–20 palavras.
4. **Figura obrigatória onde há coreografia espacial** (`ERROS.md` #12 e o caso `biocel-07`): forquilha, conjugação e CRISPR têm figura.

## Seção B — Esqueleto das 3 PARTES (10 subtópicos, 12 figuras)

### PARTE I — O genoma bacteriano: forma, conteúdo e cópia (3 subtópicos)

| # | Subtópico | Figuras |
|---|---|---|
| 1.1 | O nucleóide e a supertorção: 1 mm de DNA em 2 µm de célula | `slide-06` DNA × célula — 58% · `slide-05` relaxado × supertorcido com girase — 52% |
| 1.2 | Cromossomo, plasmídeo e elementos móveis: o genoma em camadas | `slide-18` cromossomo + plasmídeo — 55% · `slide-31` Tn10 — 62% · `slide-32` plasmídeo R — 60% |
| 1.3 | Replicação: uma origem, duas forquilhas e três polimerases | `slide-21` oriC — 60% · `slide-20` estrutura θ e sítios *ter* — 58% · `slide-22` forquilha e fragmentos de Okazaki — 60% + tabela nativa das polimerases |

### PARTE II — Como o genoma muda (3 subtópicos)

| # | Subtópico | Figuras |
|---|---|---|
| 2.1 | Mutação: o que muda na sequência e o que aparece no fenótipo | `slide-25` silenciosa/missense/nonsense/frameshift — 72% **obrigatória** (comparativo de 4 tipos) |
| 2.2 | Mutagênicos e reparo: o que quebra o DNA e o que conserta | `slide-26` radiação ionizante × dímero de timina — 62% |
| 2.3 | Transformação e transdução: DNA que entra sem divisão celular | `slide-29` transformação — lateral 40% · `slide-33` transdução generalizada — 55% |

### PARTE III — Trocar, regular, defender e manipular (4 subtópicos)

| # | Subtópico | Figuras |
|---|---|---|
| 3.1 | Conjugação: o contato que espalha resistência | `slide-34` F⁺ → F⁻ e formação de Hfr — 66% |
| 3.2 | Operon lac: o genoma decide o que transcrever | tabela nativa de estados regulatórios (glicose × lactose × cAMP × transcrição) |
| 3.3 | Restrição-modificação e CRISPR-Cas: o sistema imune da bactéria | `slide-44` três etapas do CRISPR — 66% |
| 3.4 | DNA recombinante e sequenciamento: ler e reescrever o genoma | `slide-37` extremidades abruptas × coesivas — lateral 42% · `slide-39` clonagem em plasmídeo — 58% |

**Conclusão integradora** (`#conclusao-box`, 4 camadas) + **Resumindo** (8 seções).

**Figuras descartadas pelo filtro de utilidade (regra 15) + orçamento de páginas:** `slide-02` (nucleóide em microscopia — a compactação já é carregada pelo `slide-06`, e a foto não acrescenta mecanismo), `slide-08`–`slide-15` (revisão de estrutura do DNA — conteúdo de pré-requisito, retomado em prosa), `slide-19` (comparação de tamanho de genoma — os números em prosa são mais legíveis que o gráfico log), `slide-23` (tabela das polimerases em imagem — substituída por tabela nativa, legível e pesquisável), `slide-30` (zona de adesão com cálcio — detalhe de protocolo, virou uma frase), `slide-35` (fotomicrografia do pili — o mecanismo está no `slide-34`), `slide-38`/`slide-40` (tabela de enzimas de restrição e mapa do pUC18 — ilegíveis no tamanho disponível; o essencial virou prosa), `slide-41` (infográfico do operon em inglês, denso demais para a página — substituído por tabela nativa), `slide-43` (seis bloqueios antifágicos — o `slide-44` carrega o mecanismo que interessa).

## Seção B.bis — Registro de abertura por subtópico

Nenhum par vizinho compartilha registro. Pergunta âncora/retórica banida.

| Subtópico | Registro |
|---|---|
| 1.1 | analogia concreta (o problema de empacotamento) |
| 1.2 | enquadramento |
| 1.3 | ponto-de-quebra (a origem única e o tempo que não fecha) |
| 2.1 | enquadramento |
| 2.2 | integração-anterior |
| 2.3 | ponto-de-quebra |
| 3.1 | integração-anterior |
| 3.2 | enquadramento |
| 3.3 | analogia concreta (memória imunológica) |
| 3.4 | integração-posterior |

## Seção B.ter — Pré-requisitos cruzados com frase-âncora pronta

| Pré-requisito | Frase pronta (≤25 palavras) |
|---|---|
| Estrutura da dupla hélice | "Duas fitas antiparalelas presas por pontes de hidrogênio: A=T com duas, G≡C com três — é por isso que região rica em AT abre primeiro." |
| Ligação fosfodiéster | "O esqueleto é açúcar-fosfato: o fosfato liga o carbono 3′ de um nucleotídeo ao 5′ do seguinte, e por isso a fita tem sentido." |
| Transcrição e tradução | "A RNA-polimerase copia a fita molde em mRNA, e o ribossomo lê esse mRNA em trincas; em bactéria as duas coisas acontecem juntas, sem núcleo." |
| Código genético degenerado | "Vários códons codificam o mesmo aminoácido, quase sempre diferindo na terceira base — é essa folga que permite mutação sem troca de aminoácido." |
| Recombinação homóloga | "Duas sequências parecidas se emparelham e trocam trechos; em bactéria quem conduz é a RecA, e é assim que DNA de fora se fixa no cromossomo." |
| Parede celular e PBP | "As proteínas ligadoras de penicilina montam a parede de peptidoglicano; o β-lactâmico se parece com o substrato delas e trava a enzima." |
| Peptidoglicano e Gram | "A parede espessa retém o cristal-violeta (Gram-positiva); a fina, entre duas membranas, não retém (Gram-negativa) — e a membrana externa filtra o que entra." |

---

## Seção C — Distribuição da E2 e termos-nota

**Taxonomia PADRÃO:** 10 Consolidação (Q01–Q10) · 15 Integração (Q11–Q25) · 5 Aplicação (Q26–Q30).
**Formatos:** 20 múltipla escolha (A–E) · **10 Certo/Errado com exatamente 4 itens (I–IV)** distribuídos pelas três categorias · 2 "assinale a incorreta" sinalizadas no stem (Q14 e Q21).

**Consolidação decoreba (CANON 2026-09-03).** Q01–Q10 cobram recall direto — qual polimerase faz o quê, qual enzima introduz supertorção negativa, o que define plasmídeo, o que flanqueia um transposon composto, qual mutagênico produz qual lesão, qual transdução carrega qual gene — com **alternativas de 10 a 20 palavras**, e a distratora sendo a entidade vizinha errada (a outra polimerase, a outra topoisomerase, o outro tipo de transdução).

**Termos-nota (piso 6–10):** nucleóide · supertorção negativa · poliamina · transposase · cassete gênico · dímero de ciclobutano-pirimidina · depurinação · competência · conversão lisogênica · replicação por círculo rolante · protospacer.

**Fronteira da aula:** não entram — espectro e farmacocinética de antimicrobianos, técnica de antibiograma e leitura de MIC (é `micro-05`), curva de crescimento (`micro-02`), catálogo de fatores de virulência (`micro-07`), genética de fungos e vírus animais.

---

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** ler "supertorção negativa" como DNA mais enrolado e mais difícil de abrir.
  **Correção:** negativa é **sub**enrolada — falta volta de hélice em relação à forma relaxada. Essa tensão é armazenada e paga a abertura das fitas na replicação e na transcrição. Por isso a girase, que introduz a torção negativa gastando ATP, é essencial; o excesso é desfeito pela topoisomerase I.
- **Quebra:** supor que o antibiótico induz a mutação que confere resistência.
  **Correção:** a mutação é anterior e aleatória; o antibiótico apenas **seleciona** o clone que já a tinha. O teste de flutuação de Luria e Delbrück mostrou isso pela variância entre culturas independentes. O que o antibiótico faz é diferente e mais sutil: quinolona e β-lactâmico disparam a resposta SOS, que eleva a taxa geral de mutação.
- **Quebra:** tratar plasmídeo e transposon como sinônimos de "DNA extra".
  **Correção:** o plasmídeo é um **replicon** — tem origem de replicação própria e se mantém sozinho. O transposon não tem origem própria: ele só persiste inserido em um replicon, e o que ele sabe fazer é mudar de endereço dentro dele ou saltar para outro.
- **Quebra:** achar que a transdução generalizada e a especializada diferem só em quantidade de gene transferido.
  **Correção:** diferem no erro que as origina. Na generalizada, a maquinaria de empacotamento do fago coloca no capsídeo um fragmento de DNA bacteriano no lugar do DNA viral, no ciclo lítico — qualquer gene pode ir. Na especializada, um prófago se excisa fora dos limites do sítio de integração e leva consigo o gene **vizinho** — só os genes adjacentes àquele sítio.
- **Quebra:** imaginar que a célula doadora perde o plasmídeo ao conjugar.
  **Correção:** a transferência é por círculo rolante — uma fita é cortada no *oriT* e passa para a receptora enquanto a fita complementar é replicada nas duas células. Doadora e receptora terminam com um plasmídeo completo cada, e a receptora passa a ser doadora. É esse detalhe que dá a cinética explosiva.
- **Quebra:** achar que Hfr transfere o cromossomo inteiro e converte a receptora em F⁺.
  **Correção:** a transferência começa no *oriT* do fator F integrado e caminha pelo cromossomo, mas o contato quase sempre se rompe antes do fim. Como a outra metade do fator F é justamente a última a passar, a receptora recebe genes cromossômicos e permanece F⁻.
- **Quebra:** ler o operon lac como se o repressor e o CAP fizessem a mesma coisa em dobro.
  **Correção:** são perguntas diferentes. O repressor responde "há lactose?" e libera o operador quando a alolactose chega. O complexo CAP–cAMP responde "falta glicose?" e só então recruta a RNA-polimerase para um promotor fraco. Transcrição máxima exige as duas respostas — sem lactose não há o que transcrever; com glicose disponível, não compensa.
- **Quebra:** tratar a enzima de restrição como se protegesse a bactéria sozinha.
  **Correção:** ela é metade de um sistema. A metiltransferase parceira metila a **mesma** sequência no cromossomo próprio, e é a marca química que diz à endonuclease o que não cortar. Sem a modificação, o sistema digeriria o próprio genoma.
- **Quebra:** entender CRISPR como enzima que corta qualquer DNA estranho.
  **Correção:** o corte é dirigido por sequência. O espaçador guardado no arranjo é transcrito em crRNA, e é o pareamento desse RNA com o alvo — mais o reconhecimento do PAM adjacente — que posiciona a Cas9. Sem espaçador correspondente, não há corte; é memória, não varredura genérica.
- **Quebra:** concluir do sequenciamento que a bactéria é resistente porque o gene está lá.
  **Correção:** o achado genotípico prevê, não mede. Gene de β-lactamase presente mas pouco expresso, ou expresso e neutralizado por inibidor, dá fenótipo sensível. A previsão orienta terapia empírica e vigilância; a medida de fenótipo continua vindo do teste de sensibilidade.

---

## Seção E — Exemplares-âncora

- **Categoria 1 (universal) — explicação mecanística parágrafo a parágrafo.** Acerta em dar a cada parágrafo uma função discreta e encadeada. Uso em 1.3 (DnaA-ATP → fusão das 13-mer AT → helicase → primase → Pol III → Pol I → ligase) e em 3.1 (relaxase corta o *oriT* → fita T passa pelo T4SS → círculo rolante nas duas células → receptora vira doadora), escrevendo cada etapa como consequência física da anterior.
- **Categoria 8 (universal) — `#atencao-box`.** Acerta em reservar o vermelho para a inversão que destrói o raciocínio. Reservo dois: (a) o antibiótico seleciona, não induz, a mutação — e o que ele induz é a resposta SOS; (b) plasmídeo é replicon, transposon não é.
- **Categoria 14 (universal) — siglas em footnote.** `#sigla` na 1ª aparição de DNA, RNA, ATP, pb, Mb, UV, SOS, PCR, T4SS, CRISPR, PAM, IS, MIC.
- **Categoria 3 — abertura por desfazer confusão comum.** Acerta em explicitar o erro mental antes de construir o certo. Uso em 1.1, onde "supertorção negativa = mais enrolado" é a concepção errada que trava toda a leitura das quinolonas.
- **Categoria 6 — organização terminológica.** Acerta em construir hierarquia explícita antes de definir termo a termo. Uso em 1.2: replicon é o guarda-chuva → cromossomo e plasmídeo são replicons → IS, transposon composto e integron são passageiros que não replicam sozinhos.
- **Categoria 9 — `#clinica-box`.** Acerta em ir até a profundidade fisiopatológica com o gancho explícito para o mecanismo do subtópico. Uso três: quinolona × girase (1.1), conversão lisogênica e a toxina Shiga (2.3), plasmídeo de carbapenemase em surto hospitalar (3.1).
- **Categoria 17 — cadência dialogal.** Marcador de progressão entre subtópicos e negrito funcional, uma ou duas manobras por subtópico, sem cota.
- **Categoria 18 — quando quebrar a prosa.** Gatilho 1 (catálogo de tipos discretos com um traço definidor) em 1.3, tabela das três DNA-polimerases; gatilho de tabela (cruzamento de duas dimensões) em 3.2, estados do operon lac. Todo o resto é prosa.
