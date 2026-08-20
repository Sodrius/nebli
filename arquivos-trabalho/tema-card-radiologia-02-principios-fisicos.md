# TEMA CARD — Física dos métodos de imagem

## Seção A — Escopo

- **Tema:** Física dos métodos de imagem (radiografia convencional, ultrassonografia, tomografia computadorizada, ressonância magnética)
- **Slug:** `radiologia-02-principios-fisicos`
- **Disciplina:** Radiologia — Preceptoria FMUSP
- **Fonte:** três transcrições de aula anexadas por Davi
  1. *Princípios da Radiografia convencional e da Ultrassonografia* — Dr. Raphael Oliveira
  2. *Princípios da Tomografia Computadorizada* — Dr. Mauricio R. M. da Silva Filho
  3. *Princípios da Ressonância Magnética* — Dr. César (neurorradiologia)
- **Figuras:** páginas das três transcrições renderizadas a 300 dpi, recortadas (`figuras/radiologia-02-principios-fisicos/{rx-usg,tc,rm}/slide-XX.png`) + `MAPA_CONTEUDO.txt` por fonte.
- **Recorte slide × tema:** o pedido de Davi é **um capítulo generoso por exame**. As três aulas cobrem **quatro** métodos (a primeira junta RX e USG), então a E1 sai com **4 PARTES**, não 3 — desvio deliberado do default canônico, declarado aqui.
- **Alvo de páginas E1:** piso 2, teto canônico 22 — **teto elevado para ~34 páginas nesta corrida**, porque o material de entrada é de três aulas somadas e o pedido explícito é "bem aprofundado". Declarado como exceção, não como novo default.
- **Dial de profundidade:** `profundidade: fundo` (CANON 2026-07-12) — mais injeção mecanística por subtópico, blocos clínicos maiores.
- **Prioridades desta corrida** (do `MEMORY.md` § Diário de revisões + `ERROS.md`):
  1. Prosa fluida, sem empilhamento de siglas (regra editorial 3) — tema é cheio de UH, RF, T1, T2, B₀; cada sigla entra dentro de frase com sujeito+verbo+complemento.
  2. Zero pergunta âncora/retórica na abertura de subtópico (regra editorial 1).
  3. Cota de boxes: máx 1–2 `atencao-box` + `confusao-prevista` somados por PARTE (`ERROS.md` #16 / F3).
  4. `#termo-nota` sem repetir o termo na prosa (`ERROS.md` #20).
  5. Largura de figura caso a caso 40–80%, com relatório auditável no fechamento (F5).

## Seção B — Esqueleto das 4 PARTES

### PARTE I — Radiografia: a sombra que soma tudo
- 1.1 O tubo de raios X e a natureza do feixe
- 1.2 As cinco densidades radiológicas
- 1.3 Projeção: sobreposição, magnificação, PA × AP
- 1.4 Sinal da silhueta e o contraste exógeno (bário e iodo)
- 1.5 Radiação ionizante: efeito direto, indireto e proteção

Figuras planejadas: `rx-usg/slide-08` (espectro EM), `rx-usg/slide-12` (tubo + paciente + detector), `rx-usg/slide-17` (densidades no ovo), `rx-usg/slide-25` + `rx-usg/slide-33` (caixa em PA e perfil), `rx-usg/slide-35` (PA × AP no tórax), `rx-usg/slide-39` (pedra + cimento), `rx-usg/slide-41` (sinal da silhueta), `rx-usg/slide-19` (bário e angiografia).

### PARTE II — Ultrassonografia: a imagem feita de ecos
- 2.1 Onda mecânica, transdutor piezoelétrico e o eco que volta
- 2.2 Frequência do transdutor: resolução contra penetração
- 2.3 Descritores: hiperecogênico, hipoecogênico, anecogênico
- 2.4 Sombra acústica posterior e reforço acústico posterior
- 2.5 Método seccional: orientação, limites do operador e o FAST

Figuras planejadas: `rx-usg/slide-53` (transdutor), `rx-usg/slide-57` (três transdutores + imagens), `rx-usg/slide-59` (descritores), `rx-usg/slide-61` (sombra acústica), `rx-usg/slide-63` (reforço acústico), `rx-usg/slide-67` (FAST).

### PARTE III — Tomografia: densidade que vira número
- 3.1 Do feixe único ao anel helicoidal multislice
- 3.2 Voxel, dados brutos e reconstrução multiplanar
- 3.3 Unidades Hounsfield: a água como zero
- 3.4 Janela e nível: o gargalo é o olho humano
- 3.5 Contraste iodado, fases temporais e artefatos

Figuras planejadas: `tc/slide-13` (gantry real), `tc/slide-19` (single × multislice), `tc/slide-21` (helicoidal), `tc/slide-25` (axial/sagital/coronal/3D), `tc/slide-29` (voxel), `tc/slide-33` (ar/água/osso em UH), `tc/slide-35` (tabela de UH), `tc/slide-39` (janela/nível), `tc/slide-41` (três janelas do tórax), `tc/slide-45` (protocolo de fases), `tc/slide-53` (as cinco fases), `tc/slide-59` (artefato de metal), `tc/slide-71` (esteatose), `tc/slide-73` (pneumotórax), `tc/slide-69` (apendicite).

### PARTE IV — Ressonância: o sinal que o próton devolve
- 4.1 Por que hidrogênio: spin, momento magnético e prótons ímpares
- 4.2 Dentro do campo B₀: paralelo, antiparalelo e magnetização longitudinal
- 4.3 Precessão, frequência de Larmor e o pulso de radiofrequência
- 4.4 T1 e T2: dois relógios que andam em velocidades diferentes
- 4.5 Ponderação, gadolínio e o equipamento

Figuras planejadas: `rm/slide-08` (núcleo de hidrogênio), `rm/slide-06` (spin → corrente → campo), `rm/slide-14` (campo da Terra), `rm/slide-16` (paralelo × antiparalelo), `rm/slide-26` (precessão e Larmor), `rm/slide-28` (ressonância — Bloch e Purcell), `rm/slide-36` (eixos T1/T2), `rm/slide-44` (dois pulsos, dois elementos), `rm/slide-62` (T1 × T2 nas imagens de crânio), `rm/slide-64` (gadolínio–DTPA), `rm/slide-68` (magneto supercondutor), `rm/slide-12` (resumo do circuito).

## Seção B.bis — Registro de abertura por subtópico

Nenhum par vizinho compartilha registro. Pergunta âncora/retórica **banida**.

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | ponto-de-quebra |
| 1.3 | analogia concreta (a fotografia / a caixa) |
| 1.4 | integração-anterior (retoma densidades) |
| 1.5 | enquadramento |
| 2.1 | ponto-de-quebra (som não é radiação) |
| 2.2 | analogia concreta (grave atravessa parede) |
| 2.3 | integração-anterior (descritores ≠ densidades) |
| 2.4 | ponto-de-quebra (artefato que ajuda) |
| 2.5 | integração-posterior (corte antecipa TC) |
| 3.1 | integração-anterior (retoma projeção da PARTE I) |
| 3.2 | enquadramento |
| 3.3 | analogia concreta (régua com zero na água) |
| 3.4 | ponto-de-quebra (o gargalo é o olho) |
| 3.5 | integração-posterior (contraste temporal → RM) |
| 4.1 | enquadramento |
| 4.2 | analogia concreta (gota no oceano) |
| 4.3 | ponto-de-quebra (ressonância exige frequência igual) |
| 4.4 | integração-anterior (dois relógios, um evento) |
| 4.5 | integração-posterior (fecha os quatro métodos) |

## Seção B.ter — Pré-requisitos cruzados (frase-âncora pronta)

| Pré-requisito | Frase pronta (≤25 palavras) |
|---|---|
| Espectro eletromagnético | "Onda eletromagnética é energia que viaja sem precisar de meio; quanto maior a frequência, maior a energia que cada pacote carrega." |
| Número atômico e elétrons | "Quanto mais prótons um átomo tem, mais elétrons ele segura por perto — e mais ele absorve fótons que passam." |
| Onda mecânica | "Som é vibração de partículas: sem matéria para vibrar, não há som — por isso o gel entre transdutor e pele." |
| Dano ao DNA | "Quebra na dupla-fita pode ser reparada, mal reparada (mutação) ou levar a célula à morte programada." |
| Barreira hematoencefálica | "O endotélio cerebral tem junções oclusivas que impedem moléculas grandes de sair do vaso para o parênquima." |
| Terceiro espaço | "Inflamação abre o endotélio e deixa plasma vazar para o interstício — o líquido sai do vaso e fica entre os tecidos." |

## Seção C — Distribuição da E2

Perfil **PROFUNDO** (o tema é físico-mecanístico e cruza quatro métodos): **8 Consolidação · 17 Integração · 5 Aplicação**.

- Formatos: 20 múltipla escolha · **10 Certo/Errado com 4 itens cada** (Q03, Q06, Q08, Q10, Q13, Q17, Q20, Q23, Q25, Q28) · **3 "assinale a incorreta"** (Q05, Q15, Q22).
- Gabarito sorteado no YAML (Seção A do `.yml`). MC: A×4, B×4, C×4, D×4, E×4 — nenhuma letra acima de 20%, nenhuma corrida.
- C/E: 22 C e 18 E, sem bloco longo e sem CECE puro.

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** o aluno lê "radiopaco" como sinônimo de "denso em gramas por centímetro cúbico".
  **Correção:** o que atenua o feixe é sobretudo o número atômico do material somado à espessura atravessada — o cálcio atenua muito porque tem Z alto, não só porque é duro.
- **Quebra:** o aluno acha que estruturas somem no raio X por serem pequenas.
  **Correção:** somem por estarem encostadas em algo de densidade igual — o contorno existe pelo contraste com o vizinho, não pelo tamanho.
- **Quebra:** o aluno traduz descritor de ultrassom para densidade de raio X.
  **Correção:** gordura é escura no raio X e clara no ultrassom; os dois sistemas medem coisas diferentes (absorção de fóton × reflexão de onda mecânica).
- **Quebra:** o aluno acha que aumentar a frequência do transdutor melhora tudo.
  **Correção:** frequência alta dá detalhe fino mas é absorvida cedo; profundidade exige frequência baixa, ao preço da resolução.
- **Quebra:** o aluno trata sombra acústica e reforço acústico como defeitos a evitar.
  **Correção:** os dois são artefatos com valor diagnóstico — sombra sugere cálculo, reforço sugere conteúdo líquido.
- **Quebra:** o aluno acha que a tomografia "tira várias fotos" em cada plano.
  **Correção:** a aquisição é uma só, volumétrica; sagital, coronal e 3D são reconstruções do mesmo conjunto de voxels.
- **Quebra:** o aluno acha que mudar a janela muda a densidade medida.
  **Correção:** a janela só muda o mapeamento de números para tons de cinza; a unidade Hounsfield do voxel é a mesma em qualquer janela.
- **Quebra:** o aluno acha que a fase de contraste depende do tipo de contraste injetado.
  **Correção:** o contraste é o mesmo; o que muda é o instante em que se adquire a imagem em relação à injeção.
- **Quebra:** o aluno acha que a ressonância usa radiação como o raio X, só que "magnética".
  **Correção:** o pulso é radiofrequência, energia baixa demais para arrancar elétron — não há ionização nem dano ao DNA por esse mecanismo.
- **Quebra:** o aluno decora "T1 gordura branca, T2 água branca" sem o mecanismo.
  **Correção:** a gordura recupera a magnetização longitudinal depressa (T1 curto) e a água a perde devagar no plano transversal (T2 longo) — o branco vem de quem tem mais sinal no instante da leitura.
- **Quebra:** o aluno acha que o gadolínio "aparece branco" na imagem.
  **Correção:** o gadolínio não emite sinal; ele encurta o T1 do tecido onde chega, e é o tecido que passa a devolver mais sinal.

## Seção E — Exemplares-âncora

- **Categoria 1 (mecanística parágrafo a parágrafo)** — universal. Acerta em abrir com o mecanismo cru e só depois nomear. Vou usar em 1.1 (elétron → freio → fóton antes de dizer "bremsstrahlung" — que aliás nem entra), 3.3 (coeficiente de atenuação antes de "Hounsfield") e 4.3 (frequência igual antes de "Larmor").
- **Categoria 8 (`atencao-box`)** — universal. Acerta em reservar o vermelho para inversão com consequência real. Vou usar só duas vezes no resumo inteiro: coração aumentado artificialmente em AP (PARTE I) e janela que não muda o número (PARTE III).
- **Categoria 14 (siglas em footnote)** — universal. Tema com muitas siglas (UH, RF, TC, RM, USG, FAST, DTPA, BHE). Cada uma entra dentro de frase completa, nunca em rajada.
- **Categoria 7 (analogia construtiva)** — o tema é abstrato e as três aulas já trazem analogias boas do próprio professor (a caixa de pedras, a sombra da lanterna, o pião, a gota no oceano). Vou reaproveitar as do professor em vez de inventar — analogia do docente é autoridade e âncora de aula.
- **Categoria 9 (`clinica-box`)** — clínica com cadeia de 4–6 linhas: pneumonia e silhueta cardíaca, cálculo de vesícula, esteatose hepática medida em UH, realce pós-gadolínio na quebra de barreira.
- **Categoria 17 (cadência dialogal)** — leitura leve, para não deixar a física virar parede de definições.
- **Categoria 18 (quando quebrar a prosa)** — a tabela de unidades Hounsfield e a tabela comparativa dos quatro métodos entram como `table()`, caso (a) de comparativo multidimensional.
