<!-- Playbook-mestre da curadoria de cards do deck Anki do Davi.
     Este .md é o CÉREBRO da curadoria: como escolher/gerar cards para que o deck
     cubra TODO o conteúdo da E1, num padrão bom para APRENDER (não só reter).
     Irmão vivo: registro-deck.md (o que está de fato no deck agora).
     Método operacional detalhado (scripts): flashcards/CURADORIA-ANKING.md -->

# Padrão de curadoria de cards — deck Anki NEBLI

**Objetivo do Davi (2026-07-07):** o deck tem que **cobrir todo o conteúdo da E1** de cada aula, com cards num **bom padrão para aprender** — não só reter fato solto. A curadoria só do AnKing deixava buracos porque o AnKing é Step 1 (fatos isolados, em inglês) e não tem o conteúdo autoral que a E1 ensina. Este documento é o padrão que fecha esse buraco.

## As 3 decisões que governam tudo (travadas 2026-07-07)

1. **Cobertura é CONTRATO, não relatório.** Todo fato-chave da E1 termina COBERTO — por um card AnKing bom **ou** por um card autoral. "Estude pelo slide" deixa de ser destino aceitável para fato-chave. A régua é **fato-chave ≥ 1 card** (fina, não só 1 card por subtópico).
2. **Fonte híbrida.** AnKing onde existe card bom; **card autoral só nos conceitos-chave que o AnKing não cobre com qualidade**. Não é autoral em tudo — é autoral para tapar o que falta.
3. **Tudo no estilo AnKing.** Card autoral usa o mesmo note type e a mesma gramática visual do AnKing (cloze curto + campo Extra). Fica indistinguível de um card AnKing no estudo. Nada de formato inventado.

> Regra-mãe herdada: **calibrar antes de gerar** (`calibrar-antes-de-gerar-cards`). Não se inventa cloze no chute — destila-se o padrão de cards AnKing reais (§ Rubrica abaixo) e o Davi valida uma amostra antes de gerar em massa.

## O que "cobrir a E1" significa (o contrato de cobertura)

A fonte-verdade do conteúdo é a **E1 redigida** (`typst-build/_par_<slug>/etapa1.typ`), não o tema-card. Para cada aula:

1. Quebrar a E1 em **fatos-chave** (grão fino). Um "fato-chave" é uma afirmação que um card poderia testar sozinha: uma enzima e o que ela faz, um saldo, um ponto de regulação, uma consequência clínica, um contraste conceitual. Um subtópico denso gera vários fatos-chave.
2. Cada fato-chave recebe uma **fonte**: `ANKING` (há card bom) ou `AUTORAL` (não há → eu escrevo).
3. O contrato fecha quando **todo fato-chave tem ≥1 card** (AnKing ou autoral). Zero LACUNA para fato-chave. Fato periférico (vizinhança que a E1 não ensina) fica de fora — precisão continua valendo para o que **não** é da aula.

Artefato: `deck-cards/<slug>-contrato.md` — tabela `fato-chave | subtópico E1 | fonte | card(s) | status`. É o X/Y honesto, agora no nível de fato.

## Rubrica do bom card (calibrada de cards AnKing reais)

Destilado de cards reais do deck (ex. HMP shunt). Um bom card:

- **Um mecanismo por card.** Testa uma ideia, resolve em ~10–15 s. Se precisa de dois blanks independentes, provavelmente são dois cards.
- **Cloze na palavra que carrega o mecanismo**, não na decorativa. Errado esconder "cell"; certo esconder o *porquê*/o agente. Ex.: `A G6PD é o passo {{c1::limitante}} da via porque é {{c1::irreversível}} e {{c1::regulada}}` — o blank é o conceito, não o enfeite.
- **Frente = 1 frase declarativa** (estilo "One function of the [HMP] shunt is to provide [NADPH]...") **ou** pergunta curta com resposta em cloze ("What is the rate-limiting enzyme? [G6PD]").
- **Campo `Extra` carrega o "porquê"/consequência** em 1 linha — é o que transforma reter em aprender. Ex.: `Extra: sem NADPH a glutationa não recarrega → hemácia hemolisa`. Todo card autoral **precisa** de Extra com mecanismo.
- **Imagem do slide quando ela É o mecanismo** (via, cascata). Opcional.

**Exemplo BOM (autoral, estilo AnKing):**
> Text: `NADPH and NADH differ only by a {{c1::phosphate}} group, which acts as a {{c1::tag}} enzymes read: NADPH {{c1::builds/protects (anabolic)}}, NADH {{c1::powers ATP (catabolic)}}`
> Extra: `Same redox chemistry, opposite jobs. The cell keeps NADPH/NADP+ high (ready to donate) and NAD+/NADH ~1000 (ready to accept).`

**Exemplo FRACO (evitar):**
> Text: `The pentose phosphate pathway occurs in the {{c1::cytoplasm}}` sem Extra — testa localização solta, não ensina nada. (Aceitável só se o fato-chave for mesmo "onde ocorre" e o Extra amarrar ao porquê.)

## Especificação do card autoral (para ficar idêntico ao AnKing)

- **Note type:** `AnKingOverhaul (AnKing Step Deck / AnKingMed)`.
- **Campos usados:** `Text` (o cloze) e `Extra` (o mecanismo/porquê). Demais campos vazios.
- **Deck:** `AnKing Step Deck` (mesmo dos curados, para o ritmo/ordem valerem).
- **Tags:** `NEBLI::<slug>` (âncora, igual aos curados) **+** `NEBLI::autoral` (para filtrar/auditar os que eu escrevi). Assim `tag:NEBLI::<slug>` continua sendo "tudo da aula" e `tag:NEBLI::autoral` isola os autorais.
- **Idioma:** inglês, para casar com o registro do AnKing ("tudo no estilo AnKing"). Trivial trocar para PT se o Davi quiser — é só reescrever `Text`/`Extra`.
- **Posição/ordem:** entram na mesma faixa de `due` do bloco da aula (ordem do cronograma UC — ver `ordem-cards-cronograma-uc2`).

## Processo padrão, ponta a ponta (por aula `<slug>`)

1. **Contrato de cobertura** — quebrar a E1 em fatos-chave → `deck-cards/<slug>-contrato.md`. (semente: `gerar_checklist.py`, depois refinar no grão fino).
2. **Camada 1 (AnKing, grossa)** — `buscar_tags_lote.py` acha as tags on-topic.
3. **Camada 2 (AnKing, fina)** — `extrair_cards_anking.py` + leitura card-a-card; casar cada card bom a um fato-chave (fonte=ANKING).
4. **Autoria dos buracos** — todo fato-chave ainda sem card vira card autoral (§ Rubrica + § Especificação). **Validar amostra com o Davi** antes de gerar o lote.
5. **Fechar o contrato** — todo fato-chave COBERTO (ANKING ou AUTORAL). Sem LACUNA de fato-chave.
6. **Aplicar** — curados AnKing via `aplicar_curadoria_anking.py`; autorais via `addNotes` (AnkiConnect) com o note type/tags acima. Dessuspender, sincronizar.
7. **Atualizar o registro** — `registro-deck.md` (o que está no deck agora) + `_INDEX.md` (painel da curadoria AnKing).

## Registro vivo do deck

`deck-cards/registro-deck.md` — snapshot do que está **de fato** no deck, puxado do AnkiConnect (não do que o manifesto afirma). Mostra, por aula: total de cards, ativos, novos, quantos autorais, e o status do contrato de cobertura. Atualizar sempre que aplicar/podar um bloco.

## Filtros úteis no Browse do Anki

- `tag:NEBLI::<slug>` → tudo da aula.
- `tag:NEBLI::<slug> tag:NEBLI::autoral` → só os cards que eu escrevi para a aula.
- `tag:NEBLI::autoral` → todos os autorais do deck (auditoria).
- `tag:NEBLI::<slug> is:suspended` → o que foi podado da aula.
- Podar um card: `Ctrl+J` (re-suspende, não apaga).
