# Tema Card — bioq-26-controle-hormonal

## Seção A — Escopo

- **Tema:** Controle Hormonal do Metabolismo — mecanismos de ação hormonal
- **Slug:** `bioq-26-controle-hormonal` (aula nova; não existia em `banco/aulas_uc02.yml`)
- **Disciplina:** Bioquímica (UC02) · docente DS (Profa. Deborah Schechtman, IQ-USP)
- **Slide:** `slides/mecanismos-acao-hormonal.pdf` — 56 páginas, "Controle Hormonal"
- **Alvo E1:** 16–20 páginas (tema grande: 14 subtópicos, 3 PARTES)
- **`profundidade:`** `padrao` (o novo default já elevado — CANON 2026-07-12)
- **`carga_alvo:` 60–70 cards** (peso grande + rendimento alto → banda 65–90; mirando o terço inferior porque **100% dos cards são autorais nesta corrida**, ver Restrições)
- **Recorte slide × tema:** o slide cobre (a) regulação/integração metabólica, (b) classificação e transdução, (c) insulina/glucagon/adrenalina com o glicogênio como caso-modelo, (d) tireoidianos, (e) esteroides/cortisol + disruptores. O tema pedido ("mecanismos de ação hormonal") é **exatamente esse recorte** — sem estreitar nem alargar. Metabolismo do glicogênio entra como **caso-modelo do controle recíproco**, não como aula de glicogênio.

### Prioridades desta corrida (do § Diário de revisões)

1. **`biocel-07` (peso alto, viva):** resumo sem figura. Aqui isso não pode acontecer — o slide tem 56 páginas quase todas figurais. Meta ≥3 figuras por PARTE, com largura deliberada (40–80%).
2. **R12 (norte de profundidade):** E1/E2/cards ainda rasos. Esta corrida sobe a régua: cada subtópico recebe injeção mecanística (passe de aprofundamento) **antes** de fechar cards.
3. **F9 / erro 3:** sem subagente para E1/E2. Sessão principal acumula os três papéis.

### Restrições reais desta corrida (ambiente)

- **Não há Anki vivo** (AnkiConnect ausente) e **não há coleção AnKing** no repositório — só o dossiê de 50 cards de referência (`flashcards/ANKING-DOSSIE-TEXTO.md`).
- Consequência: a camada 1 (AnKing curado) e a camada 2 (decks externos) **não podem rodar**. Todo o deck-aula é **NEBLIcard autoral** calibrado pela `CARD-MIRROR-RUBRICA.md` + `lint_neblicard.py`, entregue como **`.apkg` importável** (genanki) em vez de apply via AnkiConnect.
- O gate absoluto (card ancorado na E1) continua valendo e é o gate real desta corrida.

## Seção B — Esqueleto das 3 PARTES

### PARTE I — O sinal: o que é um hormônio e como ele chega (5 subtópicos)

- **1.1 Por que existe controle hormonal** — regulação metabólica (velocidade de reação) × integração metabólica (o organismo inteiro respondendo a fartura/jejum); as três alavancas de regulação enzimática (alostérica, covalente, expressão gênica) e onde o hormônio entra em cada uma. *Figura: slide-03 (as três alavancas), slide-08 (pontos de regulação).*
- **1.2 O que é um hormônio, e as classes químicas** — biomolécula que age longe, em baixíssima concentração, só onde há receptor; as 5 classes (peptídicos, catecolaminas, eicosanoides, esteroides, tireoidianos) e a consequência da solubilidade. *Figura: slide-09 (estruturas das 4 classes), slide-17 (tabela Lehninger 23-1).*
- **1.3 Alcance do sinal** — endócrino, parácrino, autócrino; hormônio × neurotransmissor (mesma molécula, contextos diferentes: adrenalina). *Figura: slide-10, slide-11.*
- **1.4 Receptor de alta afinidade e os tipos de transdutor** — afinidade como o que explica ação em nanomolar; os 6 transdutores (GPCR, tirosina-cinase, guanilil-ciclase, canal iônico, adesão, nuclear) e a escala de tempo de cada um. *Figura: slide-13, slide-14 (escala de tempo).*
- **1.5 Amplificação por segundos mensageiros** — a pirâmide 1 hormônio → 10² G → 10⁴ AMPc → 10⁶ moléculas de produto; por que amplificação exige desligamento rápido (GTPase, fosfodiesterase, fosfatase). *Figura: slide-16.* Aprofundamento: RIA (slide-12) como razão de a dosagem hormonal ser feita por imunoensaio.

### PARTE II — Hormônios que ficam na membrana (5 subtópicos)

- **2.1 Insulina: da pré-pró-insulina ao grânulo** — sequência-sinal, pró-insulina, pontes dissulfeto, clivagem do peptídeo C, estequiometria 1:1 (peptídeo C como marcador). *Figura: slide-22.*
- **2.2 A célula beta como sensor de glicose** — GLUT2 + glicoquinase (Km alto, sem inibição por G6P) → ATP → fecha K⁺-ATP → despolariza → Ca²⁺ voltagem-dependente → exocitose. Sulfonilureia e diazóxido como prova farmacológica do mecanismo. *Figura: slide-26, slide-25 (curvas GK × HK), slide-24 (GLUTs).*
- **2.3 O que a insulina manda fazer** — receptor tirosina-cinase → PKB → PP1 ativa → onda de **desfosforilação**; GLUT4 para a membrana; efeitos por tecido. *Figura: slide-32, slide-33.*
- **2.4 O glicogênio como caso-modelo do controle recíproco** — mesma cinase (PKA) inativa a sintase e ativa a fosforilase; mesma fosfatase (PP1) faz o inverso; regulação alostérica local (AMP, G6P, glicose) sobreposta. *Figura: slide-30, slide-31.*
- **2.5 Glucagon e adrenalina: a cascata do AMPc** — 7TM → Gs → adenilil-ciclase → AMPc → PKA → fosforilase cinase → fosforilase a; glucagon age no fígado, adrenalina no fígado e no músculo. *Figura: slide-37, slide-38, slide-41.*

### PARTE III — Hormônios que entram na célula (4 subtópicos)

- **3.1 O modo nuclear** — lipossolúvel → carreador no plasma → atravessa a membrana → receptor nuclear → elemento responsivo no DNA → transcrição; latência de horas e duração longa. *Figura: slide-15 (os 2 modos), slide-49 (dimerização + coativador).*
- **3.2 Tireoidianos: T4 como pró-hormônio** — tirosina + iodo; T4 90% da secreção mas baixa afinidade; desiodase periférica → T3 (ativo) ou rT3 (inativo); TR/RXR sobre o TRE; efeitos (metabolismo basal, coração, crescimento). *Figura: slide-42, slide-45, slide-44.*
- **3.3 Esteroides e o eixo HPA** — colesterol → pregnenolona (desmolase = passo limitante, alvo do ACTH); zonas do córtex; cortisol; receptor citoplasmático preso à HSP90; retroalimentação negativa hipotálamo-hipófise-adrenal. *Figura: slide-51, slide-50, slide-52.*
- **3.4 Cortisol na prática, Addison, Cushing e disruptores** — efeitos por tecido (gliconeogênese, resistência periférica, lipólise/redistribuição, imunossupressão); Addison (ACTH alto → hiperpigmentação) × Cushing; disruptor endócrino como mimético ou bloqueador de receptor. *Figura: slide-53, slide-54, slide-55.*

## Seção B.bis — Registro de abertura por subtópico

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | ponto-de-quebra (a solubilidade decide o resto) |
| 1.3 | analogia concreta (rádio × sussurro × bilhete pra si mesmo) |
| 1.4 | enquadramento |
| 1.5 | analogia concreta (a avalanche) |
| 2.1 | integração-anterior (retoma processamento pós-traducional) |
| 2.2 | ponto-de-quebra (a célula beta usa a própria glicólise como termômetro) |
| 2.3 | integração-posterior |
| 2.4 | enquadramento |
| 2.5 | integração-anterior (a mesma cascata, sinal oposto) |
| 3.1 | ponto-de-quebra (o receptor não está na membrana) |
| 3.2 | enquadramento |
| 3.3 | integração-anterior (colesterol da aula de lipídeos) |
| 3.4 | analogia concreta (o hormônio do jejum longo) |

Nenhum par vizinho compartilha registro.

## Seção B.ter — Pré-requisitos cruzados (frase-âncora pronta)

| Pré-requisito | Frase pronta (≤25 palavras) |
|---|---|
| Enzima alostérica × michaeliana | "Enzima alostérica tem curva em S: responde pouco em concentração baixa e dispara numa faixa estreita — é interruptor, não torneira." |
| Km | "Km é a concentração de substrato em que a enzima trabalha à metade da velocidade máxima: Km alto significa enzima que só acelera quando o substrato sobra." |
| Fosforilação | "Fosforilar é pendurar um grupo fosfato carregado negativamente num resíduo de serina, treonina ou tirosina, mudando a forma da proteína e, com ela, sua atividade." |
| Glicogênio | "Glicogênio é a glicose guardada em polímero ramificado no fígado e no músculo; sintetizá-lo e quebrá-lo são vias distintas, com enzimas distintas." |
| Colesterol | "Colesterol é o esterol de quatro anéis da membrana; é também a matéria-prima única de todos os hormônios esteroides." |
| Transcrição | "Transcrever é copiar um trecho de DNA em RNA mensageiro; controlar quanto se transcreve é controlar quanta proteína a célula terá horas depois." |

## Seção C — Distribuição da E2

Profundidade **PADRÃO** → **10 Consolidação · 15 Integração · 5 Aplicação**.
Formatos: 20 múltipla escolha + **10 C/E (4 itens I–IV cada)** + 3 delas em modo "assinale a *incorreta*" (Q07, Q17, Q23).
Gabarito sorteado gravado no `.yml` (A4 · B4 · C4 · D4 · E4 nas 20 MC; C21/E19 nas 40 assertivas C/E; sem corrida ≥4; sem CECE puro).

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** achar que "hidrossolúvel" significa "entra fácil na célula".
  **Correção:** é o contrário — quem é hidrossolúvel viaja solto no plasma mas esbarra na membrana lipídica e precisa de receptor de superfície; quem é lipossolúvel precisa de carreador no sangue e atravessa a membrana sozinho.
- **Quebra:** tratar amplificação como "o hormônio vira muitas moléculas de hormônio".
  **Correção:** o hormônio não se multiplica; cada etapa da cascata é uma enzima que produz muitas cópias do próximo mensageiro — a amplificação está no número de eventos catalíticos, não no número de hormônios.
- **Quebra:** dizer que a insulina "abre canais de glicose".
  **Correção:** a insulina desloca vesículas com GLUT4 já prontos para a membrana; o transportador é um carreador que já existia, guardado no citoplasma.
- **Quebra:** inverter o sentido da fosforilação — "fosforilar ativa".
  **Correção:** fosforilar muda a atividade; o sentido depende da enzima. A mesma PKA fosforila a glicogênio-fosforilase (ativa) e a glicogênio-sintase (inativa).
- **Quebra:** achar que o ATP abre o canal de potássio da célula beta.
  **Correção:** o ATP **fecha** o canal K⁺-ATP; com o potássio preso dentro, a membrana despolariza e o cálcio entra.
- **Quebra:** achar que T4 é o hormônio ativo porque é o mais secretado.
  **Correção:** T4 é pró-hormônio de reserva; a desiodase periférica decide, tecido a tecido, se ele vira T3 (ativo) ou rT3 (inativo).
- **Quebra:** confundir Addison (falta cortisol) com Cushing (sobra) pela pele.
  **Correção:** a hiperpigmentação de Addison vem do **ACTH alto** — a hipófise, sem freio de cortisol, produz um precursor que também gera MSH.
- **Quebra:** esperar efeito rápido de hormônio esteroide.
  **Correção:** o esteroide muda transcrição; a resposta leva horas e dura horas a dias, enquanto a via do AMPc responde em segundos.

## Seção E — Exemplares-âncora

- **Exemplar 1 (universal — abertura por enquadramento):** acerta em não pedir licença para começar; afirma o mecanismo e só depois nomeia. Uso em 1.1 e 2.4, onde a tentação de abrir com pergunta é maior.
- **Exemplar 8 (universal — cadeia causal encadeada):** acerta no ritmo "isso acontece porque aquilo mudou"; cada frase carrega o elo seguinte. Uso na cascata do AMPc (2.5) e na secreção de insulina (2.2), que são cadeias de 5–6 passos.
- **Exemplar 14 (universal — clínica inline entre travessões):** acerta em não interromper a prosa para a clínica. Uso em sulfonilureia (2.2), hipotireoidismo (3.2) e Addison (3.4).
- **Categoria 18 (quando quebrar a prosa):** a tabela das classes de hormônio (1.2) e a comparação GLUT1–4 (2.2) são cruzamentos de 2+ dimensões — cabem em `table()`; o resto fica em prosa.
