# Tema Card — biomol-04-integracao-metabolica-i

## Seção A — Escopo

- **Tema (título da capa):** Especialização metabólica dos tecidos
- **Subtítulo:** Bioquímica
- **Slug:** `biomol-04-integracao-metabolica-i` (UC03, componente Bioquímica, código BQ/BM, conteúdo 25)
- **Fonte:** transcrição integral da aula (86 páginas; 44 imagens de slide embutidas, extraídas para `figuras/biomol-04-integracao-metabolica-i/`)
- **Onde estudar:** Lehninger — *Princípios de Bioquímica*, cap. 23 (regulação hormonal e integração do metabolismo de mamíferos) · Berg/Stryer — *Bioquímica*, cap. 27 · Marks — *Bioquímica Médica Básica*, seção IV · Devlin — cap. 20
- **Alvo de páginas E1:** piso 2, **teto 22**; alvo real 16–20 (tema denso, `profundidade: fundo`)
- **`profundidade: fundo`** — pedido explícito de Davi: *"calibrando um pouco acima do que é o nível da prova"*. Mais injeções mecanísticas por subtópico, limiar de admissão afrouxado, blocos clínicos maiores.

### Recorte slide × tema

O slide cobre **especialização por órgão/tecido** — quem guarda o quê, quem exporta o quê, e quais enzimas/transportadores tornam isso possível. O slide **não** cobre os estados alimentares (alimentado · jejum · jejum prolongado), que são a aula seguinte da mesma componente. **Fronteira declarada:** jejum e estado alimentado entram aqui só como *condição* que revela a especialização (1–2 frases), nunca como subtópico próprio com figura.

### Teto histórico e o degrau (calibração UC03, `consultar.py --slug`)

- **Teto histórico desta aula:** o acervo cobra, em prosa discursiva, *quais vias predominam no fígado e no músculo* em jejum relativo (glicogenólise → gliconeogênese por lactato/alanina/glicerol, proteólise muscular, β-oxidação), *o que acontece com carboidrato, lipídio e proteína em cada tecido* quando a razão insulina/glucagon cai, e *por que bloquear o glicerol hepático reduz a produção endógena de glicose*. Ou seja: a casa cobra **cadeia causal por tecido**, com verbo *explique · descreva · justifique*.
- **A E1 vai um degrau acima em:** (a) o *porquê cinético* de cada especialização — Km do GLUT-2 e comportamento sigmoide da glicoquinase, proteína reguladora que sequestra a glicoquinase no núcleo; (b) o *custo em ATP* dos circuitos entre tecidos (Cori, glicose-alanina) lido como transferência de carga, não como geração de energia; (c) o mecanismo do *ciclo de substrato fútil* que obriga a regulação recíproca; (d) a inversão da isoforma cardíaca da enzima bifuncional; (e) a fosforilase hepática como sensor direto de glicose e o encadeamento com a fosfatase que liga a sintase; (f) por que o fígado produz e não consome corpo cetônico; (g) por que o adipócito depende da glicólise para re-esterificar ácido graxo.
- **Contrato:** nada do acervo vai colado no PDF — nem enunciado, nem menção a prova/ano/número.

### Prioridades desta corrida (do § Diário de revisões)

1. **`biocel-07` (peso alto) — nunca fechar sem figura quando o tema tem coreografia espacial/cadeia multi-passo.** Aqui há slide farto (44 imagens): meta de ≥3 figuras por PARTE, com largura deliberada caso a caso (40–80%).
2. **ERROS #20 — `#termo-nota[X]` substitui a menção de X.** Auto-check antes de fechar a E1.
3. **ERROS #23 — gabarito C/E nasce da leitura item a item das assertivas escritas**, nunca de sorteio prévio. As sequências reais só entram no YAML depois da E2 redigida.
4. **ERROS #1 — paridade banda dupla 0.80–1.25 em Q01–Q30**, distratoras redigidas ANTES da correta.

## Seção B — Esqueleto das 3 PARTES

### PARTE I — Um corpo, muitos tecidos: quem guarda, quem gasta, quem manda (4 subtópicos)
- **1.1** Reservas desiguais: cada tecido guarda um combustível diferente — *figura: slide-05 (tabela de Cahill, 62%)*
- **1.2** A divisão do trabalho: o que cada órgão faz com o que recebe — *figura: slide-06 (mapa de órgãos, 74%)*
- **1.3** A circulação porta: por que o fígado vê tudo primeiro — *figura: slide-40 (porta + linfático destacados, lateral 42%)*
- **1.4** O painel do hepatócito: glicose-6-fosfato como encruzilhada — *figura: slide-10 (fígado e carboidratos, 66%)*

### PARTE II — O fígado decide a glicemia: onde o controle mora (6 subtópicos)
- **2.1** GLUT-2 e glicoquinase: dois filtros de baixa afinidade em série — *figuras: slide-12 (Km, lateral 40%) + slide-13 (curva sigmoide × hiperbólica, 70%)*
- **2.2** Glicólise e gliconeogênese: por que as duas não podem rodar juntas — *figura: slide-14 (regulação recíproca das 4 enzimas, 62%)*
- **2.3** Frutose 2,6-bifosfato: o sinal que não é intermediário de nada — *figuras: slide-16 (cinética da fosfofrutoquinase-1, 68%) + slide-17 (enzima bifuncional, 64%)*
- **2.4** Glicogênio hepático: a fosforilase que escuta a glicose — *figuras: slide-18 (transição T/R, 62%) + slide-19 (cascata glucagon/epinefrina, 58%)*
- **2.5** Aminoácidos: o nitrogênio que precisa virar ureia — *figura: slide-23 (aminoácidos no hepatócito + alanina do músculo, 66%)*
- **2.6** Lipídios: o fígado que exporta gordura e empacota acetil-CoA — *figura: slide-25 (lipídios no hepatócito, 64%)*

### PARTE III — Os outros tecidos e o sensor que fecha o circuito (6 subtópicos)
- **3.1** Músculo esquelético: reserva própria, e o ciclo de Cori — *figura: slide-29 (fibras + fosfocreatina + Cori, 72%)*
- **3.2** A fosforilase muscular escuta outra coisa — *figuras: slide-32 (T/R por AMP/ATP/G6P, 66%) + slide-33 (sintase ativada por G6P, 56%)*
- **3.3** Coração: o consumidor aeróbio obrigatório — *figura: slide-30 (miocárdio + mitocôndrias em microscopia eletrônica, 56%)*
- **3.4** Tecido adiposo: o banco de triacilglicerol e o gerador de calor
- **3.5** Cérebro, hemácia e rim: os clientes obrigatórios da glicose — *figura: slide-38 (cérebro + PET, 60%)*
- **3.6** Pâncreas: o sensor que usa as mesmas peças do fígado — *figura: slide-43 (pâncreas, 52%)* (candidata — decidir pelo filtro de utilidade)

**Cadeia multi-passo ≥5 reações → figura obrigatória:** glicólise/gliconeogênese (slide-14 e slide-15), enzima bifuncional (slide-17), cascata do glucagon (slide-19). Todas cobertas.

## Seção B.bis — Registro de abertura por subtópico (sem par vizinho repetido)

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | analogia concreta (a orquestra e o maestro — analogia do próprio professor) |
| 1.3 | integração-posterior |
| 1.4 | ponto-de-quebra |
| 2.1 | enquadramento |
| 2.2 | ponto-de-quebra |
| 2.3 | integração-anterior |
| 2.4 | analogia concreta |
| 2.5 | integração-posterior |
| 2.6 | enquadramento |
| 3.1 | ponto-de-quebra |
| 3.2 | integração-anterior |
| 3.3 | enquadramento |
| 3.4 | analogia concreta |
| 3.5 | integração-posterior |
| 3.6 | ponto-de-quebra |

## Seção B.ter — Pré-requisitos cruzados (frase-âncora pronta, ≤25 palavras)

| Pré-requisito | Frase pronta |
|---|---|
| Glicólise | "A glicólise quebra uma glicose em dois piruvatos e rende, de saldo, dois ATP e dois NADH." |
| Gliconeogênese | "A gliconeogênese refaz glicose a partir de piruvato contornando as três reações irreversíveis da glicólise com quatro enzimas próprias." |
| Ciclo de Krebs | "O ciclo de Krebs oxida o acetil-CoA a gás carbônico e entrega elétrons à cadeia respiratória." |
| Regulação alostérica | "Regulação alostérica é a ligação de uma molécula fora do sítio catalítico que muda a forma da enzima e, com ela, sua velocidade." |
| Modificação covalente | "Modificação covalente é a adição de um fosfato pela quinase e sua remoção pela fosfatase — liga ou desliga a enzima conforme o caso." |
| β-oxidação | "A β-oxidação corta o ácido graxo de dois em dois carbonos, entregando acetil-CoA ao ciclo de Krebs." |
| Ciclo da ureia | "O ciclo da ureia recolhe a amônia tóxica da desaminação e a embala em ureia, excretável pelo rim." |

## Seção C — Profundidade e distribuição da E2

- **Profundidade: PROFUNDO / dial `fundo`** → **8 Consolidação · 17 Integração · 5 Aplicação**
- **Formatos:** ~10 questões Certo/Errado (exatamente 4 itens I–IV cada), distribuídas pelas três categorias; 3 questões "assinale a **incorreta**" sinalizadas no stem; restante múltipla escolha A–E.
- **Paridade:** banda dupla 0.80 ≤ palavras(correta)/palavras(maior distratora) ≤ 1.25, Q01–Q30, com relatório de direção no fechamento.
- **Cálculo:** 2 itens cujo mecanismo de resolução É a conta (custo em ATP do ciclo de Cori; saldo do ciclo de substrato fútil).
- **Termos-nota nominalmente obrigatórios (6–10):** glicoquinase · ciclo de Cori · ciclo glicose-alanina · lipase hormônio-sensível · fosfocreatina · corpos cetônicos · gliceroneogênese · termogênese sem tremor.

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** tratar o glicogênio muscular como reserva do organismo.
  **Correção:** o músculo não tem glicose-6-fosfatase; a glicose-6-fosfato vinda do seu glicogênio não consegue sair da célula e é obrigada a virar ATP ali mesmo.
- **Quebra:** ler o Km alto do GLUT-2 e da glicoquinase como ineficiência.
  **Correção:** a baixa afinidade é o mecanismo do sensor — só em glicemia alta a captação hepática acelera, o que impede o fígado de roubar a glicose que o cérebro precisa.
- **Quebra:** achar que a frutose 2,6-bifosfato é intermediário da glicólise.
  **Correção:** ela não é substrato nem produto de via nenhuma; é sinal puro, fabricado e destruído por uma única enzima bifuncional cujo estado de fosforilação o glucagon controla.
- **Quebra:** supor que o ciclo de Cori gera energia para o organismo.
  **Correção:** ele consome seis ATP no fígado para devolver ao músculo uma glicose que renderá dois — transfere carga energética do fígado para o músculo, não cria energia.
- **Quebra:** imaginar que o fígado se abastece dos corpos cetônicos que fabrica.
  **Correção:** falta ao hepatócito a transferase que reativa o acetoacetato a acetoacetil-CoA; o combustível sai pronto para músculo, coração e, com dias de jejum, cérebro.
- **Quebra:** confundir "aminoácido é reserva de energia" com "proteína é depósito".
  **Correção:** não existe proteína de estoque; mobilizar aminoácido significa desmontar proteína funcional — por isso o organismo protege a massa muscular enquanto tiver alternativa.
- **Quebra:** achar que o adipócito reaproveita o próprio glicerol da lipólise.
  **Correção:** falta glicerol-quinase ao adipócito; o glicerol-3-fosfato para re-esterificar vem da glicólise ou da gliceroneogênese, e é por isso que a re-esterificação depende de glicose e insulina.
- **Quebra:** tratar a regulação da glicogênio-fosforilase como uma só, igual em todo tecido.
  **Correção:** a hepática responde à glicose livre (sensor de glicemia); a muscular responde a AMP, ATP e glicose-6-fosfato (sensor de carga energética própria), porque no músculo essas concentrações oscilam e no fígado não.

## Seção E — Exemplares-âncora

- **Cat. 1 (mecanística parágrafo-a-parágrafo, universal):** acerta ao entregar o mecanismo antes do nome e anunciar o que volta depois. Uso em 2.3 (enzima bifuncional) e 3.6 (célula β), adaptando para "a conformação muda, e só então o efeito aparece".
- **Cat. 8 (`atencao-box`/`confusao-prevista`, universal):** acerta na estrutura de dois movimentos, quebra + correção. Uso em 1.1 (glicogênio muscular), 2.1 (glicoquinase ≠ hexoquinase) e 3.1 (ciclo de Cori não gera energia).
- **Cat. 14 (footnotes, universal):** acerta ao deixar a sigla dentro de frase com sujeito e verbo. Uso ao longo da E1, com teto de siglas por parágrafo.
- **Cat. 4 (magnitudes ancoradas):** acerta ao dar a régua antes do número. Uso em 1.1 (kcal por depósito) e 3.5 (120 g de glicose/dia no cérebro; 20% do oxigênio).
- **Cat. 7 (analogia construtiva):** acerta ao usar analogia que se paga em mecanismo. Uso em 1.2 (a orquestra do próprio professor, cobrada até o fim: o maestro é hormônio, o instrumento é enzima expressa).
- **Cat. 16 (catálogo de família + tabela):** acerta ao dar o eixo organizador (Km) antes dos dados. Uso literal em 2.1 com a família GLUT.
- **Cat. 12 (cálculo bem explicado):** acerta ao montar em prosa, rotular etapas e reler o número em palavras. Uso em 3.1 (6 ATP gastos × 2 ATP rendidos no ciclo de Cori).
- **Cat. 18 (quando quebrar a prosa):** gatilho do cruzamento de 2+ dimensões. Uso em 3.5 com a tabela combustível × reserva × exporta.
- **Cat. 9 (`clinica-box`):** uso em 1.4 (von Gierke), 2.1 (glicoquinase e o limiar deslocado), 2.2 (hipoglicemia do etanol), 3.2 (McArdle).
