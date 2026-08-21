# Tema Card — Organização e funcionamento do sistema imune

## Seção A — Escopo

- **Tema:** Organização e funcionamento do sistema imune
- **Slug:** `imuno-01-organizacao-sistema-imune`
- **Disciplina:** Imunologia (aula do Prof. José Alexandre M. Barbuto)
- **Onde estudar:** Abbas, *Imunologia Celular e Molecular* caps. 1–2; Janeway, *Immunobiology* caps. 1 e 9
- **Alvo de páginas E1:** piso 2, **teto 22** — alvo 16–20
- **Profundidade:** `padrao` (já o novo default elevado)
- **Recorte slide × tema:** o slide cobre (a) papel homeostático do SI, (b) repertório clonal como "tradutor universal",
  (c) barreiras + alarme + inata, (d) órgãos primários e o estabelecimento do repertório, (e) circulação/recirculação
  linfocitária, (f) o órgão linfoide secundário destrinchado em condições estruturais, aferência, expansão regionalizada
  e eferência, (g) moléculas de adesão e quimiocinas. **Não cobre** (e a E1 não entra): estrutura molecular do TCR/BCR,
  vias de sinalização intracelular, classes de imunoglobulina em detalhe, histologia fina do timo/linfonodo.
  Recorte declarado: o tema é a **arquitetura e a logística** do sistema, não a bioquímica do reconhecimento.
- **Prioridades desta corrida** (Diário de revisões, `MEMORY.md`):
  1. *(peso alto, 2026-05-29 · biocel-07)* figura é canônica — todo mecanismo com coreografia espacial ganha figura.
     Aqui o tema É espacial (rotas sangue→HEV→linfonodo→linfa) — cadeia de recirculação sem figura seria reincidência.
  2. Cadeia ≥4 setas sem figura adjacente (ERROS #12) — a rota do linfócito tem 5 estações; figura obrigatória.
  3. `#termo-nota` não repete o termo na prosa (ERROS #20).
  4. Cota de boxes: 1–2 vermelhos/gold por PARTE (ERROS #16 / F3).

## Seção B — Esqueleto

**PARTE I — Por que existe um sistema imune** (figuras: slide-06, slide-07, slide-09)
- 1.1 Homeostasia e o exterior — o sistema que precisa lidar com o imprevisto
- 1.2 O repertório clonal — como se constrói um receptor para "tudo"
- 1.3 Barreiras, alarme e resposta inata — o tecido pede socorro

**PARTE II — Onde as células nascem e por onde andam** (figuras: slide-10, slide-11, slide-13, slide-14)
- 2.1 Órgãos linfoides primários — gerar o repertório e podá-lo
- 2.2 Da geração ao encontro — primários, secundários e o mapa do corpo
- 2.3 Recirculação e endereçamento — HEV, adesão e quimiocinas

**PARTE III — O órgão linfoide secundário como máquina de encontro** (figuras: slide-17, slide-19, slide-20, slide-21, slide-18, slide-16)
- 3.1 Condições estruturais — fluxo contínuo e densidade celular
- 3.2 Aferência e expansão regionalizada — como a informação entra e onde cada clone cresce
- 3.3 Eferência, resposta e tolerância — o que sai e por que nem todo reconhecimento vira resposta

## Seção B.bis — Registro de abertura (rotação; pergunta âncora/retórica banida)

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | ponto-de-quebra |
| 1.3 | analogia concreta |
| 2.1 | integração-anterior |
| 2.2 | enquadramento |
| 2.3 | ponto-de-quebra |
| 3.1 | integração-anterior |
| 3.2 | analogia concreta |
| 3.3 | integração-posterior |

## Seção B.ter — Pré-requisitos cruzados (frase-âncora pronta)

| Pré-requisito | Frase pronta (≤25 palavras) |
|---|---|
| Homeostasia | "Homeostasia é a manutenção ativa das condições internas dentro de uma faixa estreita — não é imobilidade, é correção contínua de desvios." |
| Receptor de membrana | "Receptor é uma proteína que só muda de conformação diante de uma molécula de forma complementar — o que não encaixa, a célula não vê." |
| Endotélio e extravasamento | "O endotélio é a camada de células que forra o vaso por dentro; para sair do sangue, o leucócito precisa que ele mude de superfície." |
| Linfa e vaso linfático | "A linfa é o líquido que escorre do interstício para dentro de capilares linfáticos e volta ao sangue — leva com ela o que estiver no tecido." |

## Seção C — Distribuição da E2 (PADRÃO)

- 10 Consolidação (Q01–Q10) · 15 Integração (Q11–Q25) · 5 Aplicação (Q26–Q30)
- **Formatos:** 20 múltipla escolha · **10 Certo/Errado** (Q02, Q05, Q08, Q12, Q15, Q18, Q21, Q24, Q27, Q30), 4 assertivas cada · 3 no formato "assinale a **incorreta**" (Q06, Q19, Q26)
- **Gabarito sorteado** no YAML do Tema Card (bloco `gabarito:`). Distribuição MC: A5 · B4 · C4 · D3 · E4. Maior corrida = 1.
- **Termos-nota nominalmente obrigatórios (6–10):** homeostasia · antígeno · DAMP · deleção clonal · anergia clonal · vênula de endotélio alto · quimiocina · transcitose · centro germinativo · hipermutação somática

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** tratar "inata" como reconhecimento cego, sem especificidade nenhuma.
  **Correção:** a inata reconhece *padrões moleculares* conservados por receptores herdados — é específica para classes de molécula, não para moléculas individuais.
- **Quebra:** achar que a resposta imune acontece no tecido lesado.
  **Correção:** o tecido dá o alarme e recebe os efetores; o *reconhecimento clonal* que inicia a resposta adquirida acontece no órgão linfoide secundário.
- **Quebra:** confundir vênula de endotélio alto com vaso linfático.
  **Correção:** a vênula de endotélio alto é vaso *sanguíneo* — é por ela que o linfócito sai do sangue e entra no linfonodo; a linfa é a via de saída, não de entrada.
- **Quebra:** supor que o repertório é construído sob medida contra cada agressor encontrado.
  **Correção:** o repertório é gerado antes de qualquer encontro, por rearranjo somático aleatório; o antígeno apenas seleciona e expande os clones que já existiam.
- **Quebra:** ler "órgão linfoide primário" como "primeiro lugar onde a resposta acontece".
  **Correção:** primário é onde o repertório é *gerado e selecionado*; o encontro com o antígeno externo é justamente o que ali se evita.
- **Quebra:** achar que todo reconhecimento clonal produz resposta.
  **Correção:** reconhecimento sem contexto de perigo produz tolerância — anergia, deleção ou desvio regulador. Perigo é o segundo sinal.
- **Quebra:** achar que a migração do linfócito é aleatória, "vai aonde o sangue leva".
  **Correção:** é endereçada — combinações de moléculas de adesão e receptores de quimiocina definem, célula a célula, qual território ela pode entrar.

## Seção E — Exemplares-âncora

- **Categoria 1 (universal) — explicação mecanística parágrafo a parágrafo.** Acerta em encadear causa→mecanismo→consequência sem cortar para lista. Vou usar na cadeia rolamento→ativação→adesão firme→diapedese (2.3) e na cadeia aferência→encontro→expansão→eferência (PARTE III).
- **Categoria 8 (universal) — `atencao-box`.** Acerta em reservar o vermelho para inversão destruidora. Vou usar uma única vez, em 3.3 (reconhecimento ≠ resposta), que é o nó com consequência clínica real (autoimunidade).
- **Categoria 14 (universal) — siglas em footnote.** Tema pesado de sigla (DAMP, PAMP, PRR, APC, HEV, MALT, ILC, FDC). Cada uma entra dentro de frase com sujeito+verbo, nunca empilhada.
- **Categoria 4 — magnitudes ancoradas.** Acerta em transformar "aumenta a probabilidade de encontro" em número que o aluno sente. Vou usar em 3.1 com a frequência de precursores e o tempo de trânsito do linfócito pelo linfonodo.
- **Categoria 7 — analogia construtiva.** Acerta em analogia que se paga e é abandonada antes de virar muleta. Vou usar em 1.2 (repertório como conjunto de chaves feitas antes de conhecer as fechaduras) e em 3.1 (o linfonodo como ponto de encontro combinado).
- **Categoria 9 — `clinica-box`.** Acerta em cadeia de 4–6 linhas que amarra mecanismo→doença. Vou usar em 2.1 (aplasia tímica), 2.3 (defeito de adesão leucocitária) e 3.2 (asplenia e bactéria encapsulada).
