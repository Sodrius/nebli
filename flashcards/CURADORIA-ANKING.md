# Curadoria AnKing v12 por aula — o método

> **Filosofia, estado atual, bandeiras e pendências:** ver `FLASHCARDS.md` (raiz do projeto). Este arquivo é o manual técnico — scripts, critérios, schema, fluxo passo a passo.

Sistema para dar a **cada aula do NEBLI** um bloco de **30–50 cards MUITO bem curados** do AnKing v12, dessuspendidos no deck do Davi e rastreados como revisão espaçada de longo prazo. Resolve o problema real do deck: *coisa demais* (patologia de Step 1 que não é a aula) e *coisa de menos* (estrutura anatômica macro que o deck mal cobre).

Estado e painel: `flashcards/curadoria/_INDEX.md`. Manifesto por aula: `flashcards/curadoria/<slug>.md` (+ `<slug>-curado.json`). Método irmão, porém grosso, para a capa do PDF: `referencias-externas/onde-aprofundar.md` (aquele lista decks; este seleciona cards).

## Por que duas camadas
Dessuspender por tag é a granularidade errada. Medição real na ANATO-06:
- `aortic` → **574 cards**, quase todos patologia (aneurisma, dissecção, estenose, sopros) — **RUÍDO** para uma aula de anatomia macro.
- `azygos` → **0 cards**; `vena cava` (frase) → **0** — o sistema ázigo e o retorno venoso nomeado quase não existem no Step 1 → **LACUNA**.
- `SketchyAnatomy::02_Thorax::03_Vasculature::02_Superior_Vena_Cava` (16) → anatomia macro de verdade → **candidata boa**.
- Mesmo a leaf `…::01_Thoracic_Aorta_&_Branches` (17) **mistura** anatomia (arco aórtico, barorreceptores) com patologia (dissecção Stanford A/B) → **IMPURA**, precisa de keep/drop card-a-card.

Logo: a tag escolhe o bairro (Camada 1, grossa); o texto real do card decide a casa (Camada 2, fina).

## Fluxo dirigido por conceito (canônico 2026-07-04)

**Ordem invertida.** O fluxo antigo era tag-first, cobertura-last: chutar keywords → ler cards → keep/drop → *só no fim* escrever o gap-analysis. Isso vazava recall (o conceito cuja keyword ninguém digitou nunca tinha tag buscada — a ANATO-06 quase perdeu a anatomia venosa dos membros e o sistema ázigo por isso) e deixava a cobertura sem prova. Agora a ordem é **checklist de conceitos → busca dirigida por cada conceito → pool amplo → matriz conceito×card**. A fonte-verdade do "conteúdo da aula" é a **E1 já redigida** (`typst-build/etapa1.typ`), complementada pela Seção B do Tema Card — é o retrato mais completo e fiel do que a aula cobre.

## Os 6 passos (por aula `<slug>`)

**1. Checklist-alvo a partir da E1 (fonte-verdade).** **O card vem da E1 redigida, NÃO do tema_card** (regra do Davi 2026-07-04: "o card não vem do tema fonte, mas sim da E1"). A E1 é o texto autoral que de fato ensina a aula; o tema_card Seção B só **complementa** se a E1 não existir ou estiver incompleta.

**Semear automático (canônico 2026-07-05):** rodar primeiro
```
python flashcards/scripts/gerar_checklist.py <slug>
```
Ele varre a E1 (cascata `typst-build/_par_<slug>/etapa1.typ` → `arquivos-trabalho/etapas-anteriores/<slug>/etapa1.typ` → `typst-build/etapa1.typ`) e extrai os conceitos que a própria aula já marcou como dignos de nota — `#termo-nota[..][..]` e `#sigla("..",[..])` — agrupados por PARTE, gravando `arquivos-trabalho/checklist-<slug>.tsv` pré-preenchido (`<id>\t<frase-alvo>\t<termo_pt|termo_en>`). Quando a sigla/termo traz o inglês (marcado "do inglês *...*" ou expansão já em inglês), o EN entra sozinho; senão fica `<EN?>`. A sessão faz então uma **passada leve**: completa os `<EN?>` (o AnKing é em inglês: "retorno venoso" → `venous_return|vena_cava|azygos`), funde redundâncias e **acrescenta subtópico que a E1 ensina mas não marcou como termo-nota**. Os termos saem da aula, não da memória do curador — é isto que fecha o vazamento de recall. Mesmo grão da tabela "Cobertura da E1 na E2", id estável por conceito (`1.1`, `2.1`…).

**2. Camada 1 dirigida pela checklist (grossa, recall).**
```
python flashcards/scripts/buscar_tags_lote.py arquivos-trabalho/checklist-<slug>.tsv --md
```
Roda a busca para a **união** de todos os termos de uma vez e devolve, para cada leaf-tag, **quais conceitos da checklist a motivaram** (tabela markdown colável na Camada 1 do manifesto). Conceito que não achou tag nenhuma sai listado como **LACUNA declarada** (não silêncio) → vira fonte externa no passo 4. Classificar cada leaf-tag:
- **CANDIDATA** — tem conteúdo on-topic → vai para a Camada 2 (keep/drop card-a-card).
- **RUÍDO** — patologia/fisiologia alheia ao recorte da aula → rejeita.

> **Sem atalho de tag PURA (canônico 2026-07-04).** A antiga classe PURA ("inclui a subárvore inteira sem ler") foi **abolida**: era a porta por onde entrava card que não é idealmente da aula. Agora **toda** tag candidata passa pela Camada 2 — nenhum card entra sem ser lido e casado contra a Seção B do Tema Card. Precisão > recall (ver § Critério de inclusão).

**3. Camada 2 — curadoria card-a-card (fina, TODAS as candidatas).**
```
python flashcards/scripts/extrair_cards_anking.py "<tag candidata>" --slug <slug>
python flashcards/scripts/prefiltrar_pool.py <slug>
```
`extrair_cards` gera `arquivos-trabalho/anking-pool-<slug>.json` com frente/verso legíveis (usa **cache do dia**; `--forcar` re-extrai). `prefiltrar_pool` afina o custo de tokens da Camada 2 (o único ponto onde a curadoria gasta token): emite `anking-pool-<slug>-slim.md` com **PROVÁVEIS-BONS** (só frente limpa, sem HTML, truncada — a sessão lê a fundo e marca keep/drop) e **RUÍDO-PROVÁVEL** (patologia/fora-de-escopo por blocklist — a sessão **passa o olho** e resgata falso-positivo; decisão do Davi 2026-07-05: revisar os cortados, não cortar cego). O `raw0` não entra no contexto (fica no pool cheio, que o apply usa pra casar por texto). Keep pelo **Critério de inclusão** abaixo, com motivo de 1 linha. Nenhuma tag pula esta camada.

### Critério de inclusão (rígido, canônico 2026-07-04)
**Objetivo:** o Davi usa o Anki para reter a longo prazo o que já estudou — não para acumular tudo que é vizinho ao tema. Logo: **menos cards, exatos da aula.** Precisão > recall.

**Gate de keep:** um card entra **somente se o conceito que ele testa aparece na Seção B (esqueleto de conteúdo) do Tema Card daquela aula** — `arquivos-trabalho/tema_card_<slug>.yml`. Cada card kept tem que apontar para um subtópico da E1. Se não aponta, sai.

**Vizinhança anatômica/fisiológica NÃO basta.** Motivos recorrentes de drop, mesmo quando a estrutura da aula aparece no card:
- topografia de *relação* (o que é anterior/posterior, o que comprime o quê) que a E1 não ensina;
- sistema de condução / fisiologia elétrica numa aula de anatomia macro;
- etiologia clínica (o câncer que causa X) e complicação/patologia (o derrame, a dissecção) quando a E1 ensina a anatomia, não a doença;
- detalhe métrico não-central (nível vertebral de uma bifurcação que a E1 não cita).

Na dúvida, **fora** — a lacuna vira fonte externa apontada no gap-analysis (passo 4), nunca card frouxo. Bloco menor e 100% da aula vence bloco maior com ruído.

### Perfil decoreba — metabolismo e anatomia (canônico 2026-07-04)
Aulas de **alta decoreba** (vias metabólicas, anatomia macro) pedem carinho especial: o Davi quer **reter tudo que é útil** do tema, não uma amostra. Aqui **precisão sobre a vizinhança e completude dentro do escopo não se contradizem** — são eixos diferentes. O corte agressivo continua para o que é *fora da aula* (patologia, condução, etiologia, complicação); mas *dentro da aula* **não se corta um fato-chave por ser "menor"**.

O que a checklist de uma via metabólica tem que capturar, quando a E1 ensina: **enzima-chave e passo limitante**, **cofatores/coenzimas**, **intermediários centrais**, **ponto de regulação** (ativadores/inibidores, hormonal), **saldo/rendimento**, e o **gancho clínico**. Cada card kept precisa carregar **mecanismo suficiente** — não só o nome do fato. Se o card do AnKing é raso demais para o fato-chave, marca-se o conceito como **PARCIAL com fonte** (não se aceita meia-informação, nem se força card frouxo). Meta de cobertura nas aulas decoreba: **alta** (poucas LACUNAS; cada conceito da E1 com ≥1 card que carrega o mecanismo).

**Ordem no manifesto** (sequência pedagógica): visão geral da via → passos na ordem da via → regulação → gancho clínico. No deck, a ordem é a **nativa do AnKing** (segue Sketchy/First Aid — decisão do Davi 2026-07-04; não reposicionar cards no Anki). A ordem documentada no manifesto serve o estudo dirigido e a conferência de completude.

**Contar por note, não por card.** Notes cloze com vários `{{cN}}` geram vários cards no deck (ex.: piloto ANATO-06 = 30 notes kept → 42 cards dessuspensos). "Menos cards" se mede no nível do note curado.

**Piloto:** ANATO-06 recurada 37→31 kept (cortados: topografia posterior/anterior do coração, irrigação dos nós SA/AV, bifurcação carotídea C4, quilotórax por lesão do ducto, síndrome VCS por câncer de pulmão).

**4. Matriz conceito×card = cobertura como métrica, não vibe.** Na leitura da Camada 2, cada card kept já anota **o(s) id(s) de conceito da checklist que ele cobre** (coluna "Conceito-alvo" obrigatória, amarrada aos ids do passo 1). Invertendo card→conceito para conceito→cards, cada conceito recebe um status:
- `COBERTO` — ≥1 card real do AnKing carrega o conceito.
- `PARCIAL` — só um aspecto; fonte externa completa o resto.
- `LACUNA` — 0 cards; cobrir por fonte externa (deck dedicado, Netter/Moore, slide).
- `PENDENTE-GERADO` — 0 card real bom, mas é conceito-chave da E1 que **merece card**: fica **enfileirado** para um card NEBLI cloze gerado numa **sessão futura de calibração**. Status terminal válido (não trava o fechamento), contado à parte de COBERTO. **NÃO gerar card agora** — a geração só acontece depois de destilar, de cards reais do AnKing, o que é um bom card, e o Davi validar esse padrão (ver memória `calibrar-antes-de-gerar-cards`). É o análogo, para o deck, do gate de cobertura da E2: todo subtópico da E1 fecha como COBERTO ou entra na fila com fonte apontada.

Em PARCIAL/LACUNA/PENDENTE-GERADO, **sempre nomear a fonte** onde completar. Regra do Davi: *sempre indicar o que falta e onde pegar*. Nunca forçar card ruim para tapar buraco. Métrica de fechamento: **X/Y conceitos COBERTOS** (+ fila pendente-gerado).

**5. Manifesto + estado + prova de cobertura.** Preencher `flashcards/curadoria/<slug>.md` (de `_TEMPLATE.md` — seção "Checklist-alvo" + matriz Camada 2 + gap-analysis por PARTE) e o gêmeo `flashcards/curadoria/<slug>-curado.json` (schema no rodapé do template). Alvo: 30–50 kept. Rodar então o validador:
```
python flashcards/scripts/verificar_cobertura_anking.py <slug>
```
Ele imprime **X/Y COBERTOS** (+ fila pendente-gerado), exige que toda a checklist tenha sido avaliada e que toda LACUNA/PARCIAL/PENDENTE-GERADO nomeie a fonte (erro trava o fechamento), grava `arquivos-trabalho/cobertura-<slug>.json` (listas por status — é o que alimenta a fila de geração futura) e devolve a linha pronta pra coluna "Cobertura AnKing" do `_INDEX.md`. É o análogo do relatório de ratio Q01-Q30: torna a cobertura um artefato explícito.

**6. Aplicar via AnkiConnect.**
```
python flashcards/scripts/aplicar_curadoria_anking.py <slug> --dry-run   # confere
python flashcards/scripts/aplicar_curadoria_anking.py <slug>            # aplica
```
Marca os notes curados com `NEBLI::<slug>`, dessuspende, e **atualiza `_INDEX.md` sozinho**. A marca persiste a escolha card-a-card na coleção: reaplicar é idempotente; `--reverter` re-suspende sem apagar.

> **Como o apply acha o card certo (nota técnica):** o AnkiConnect local **não expõe `guid`** no `notesInfo` (só noteId/fields/tags). Então o casamento card-a-card é feito pelo **texto bruto do campo 1** (`raw0`), lido do pool `arquivos-trabalho/anking-pool-<slug>.json`. Por isso o pool precisa existir na hora do apply (regenere com `extrair_cards_anking.py` se sumiu). Se o AnKing atualizou o texto de um card desde o export, ele não casa — o apply reporta quantos pediu × casou; perdas de 1–2 cards são normais e não afetam a cobertura.

**Zerar o deck (reconstruir do limpo):** `zerar_deck_anking.py` re-suspende TODOS os cards ativos e os marca `NEBLI::zerado::<data>` (reversível via `--reverter --data`). Use antes de reconstruir por conteúdo de prova: zerar → aplicar os blocos curados → só os curados ficam ativos.

**Ritmo do deck (passo final).** Fechado o bloco, fixar o ritmo de introdução:
```
python flashcards/scripts/configurar_ritmo_anking.py
```
Seta o grupo de opções do deck AnKing em **25 cards novos/dia** e **150 revisões/dia** (idempotente; `--dry-run` mostra antes/depois). Não importa quantos cards cada aula dessuspende — só 25 novos afloram por dia. Os 25 são introdução; as 150 revisões se preenchem conforme os blocos `NEBLI::` maturam ao longo dos dias.

## Integração ao pipeline NEBLI (auto-aplicar)
Quando o Davi pede o **pipeline completo** (`/resumo`), a curadoria é o **passo final**, depois de mover o PDF: a sessão roda o fluxo (checklist semeada → Camada 1 → pool+pré-filtro → matriz+cobertura → apply → ritmo), aplica via AnkiConnect e reporta no `_INDEX.md`. Assim, todo resumo novo já entra no deck como bloco `NEBLI::<slug>`, e o `_INDEX.md` avisa o que está dessuspendido para o Davi ajustar. Ver `/resumo` passo 11 e `ROLES.md` § Compilador. **A geração/injeção de cards cloze NEBLI (para a fila pendente-gerado) NÃO faz parte deste pipeline** — é sessão dedicada, começando pela calibração do padrão de bom card.

Se o AnkiConnect estiver fora do ar na hora, o apply cai no recibo manual (buscas prontas para o Browse) e o resumo não trava — o Davi aplica depois.

## Ciclo de monitoria (voz de monitor)
O deck não é só arquivo: é aluno sendo acompanhado. Base já pronta:
```
python flashcards/scripts/revisao_diaria_anking.py            # cards errados hoje (Again) nos blocos NEBLI::
python flashcards/scripts/revisao_diaria_anking.py --slug <slug>
```
Gera `arquivos-trabalho/errei-<data>.json` com o texto dos cards reprovados. A sessão lê e redige, em voz de monitor, a explicação de mecanismo de cada erro (causa → mecanismo → consequência), que pode ser enviada por **email diário** (Gmail) para o Davi. Extensões possíveis (a ligar sob demanda — ver menu no chat): resumo semanal de leeches, sugestão de novos blocos a dessuspender conforme o backlog esvazia, alerta se novos/dia passar de ~25, quiz de reforço dos erros recorrentes.

## Reuso
`gerar_checklist.py` (passo 1 — semeia a checklist da E1: termo-notas + siglas por PARTE) · `buscar_tags_lote.py` (Camada 1 dirigida pela checklist — recall, puxa de todos os recursos) · `buscar_tags_anking.py` (Camada 1 por termo único, base reusada pelo lote) · `extrair_cards_anking.py` (Camada 2 — pool, com cache do dia) · `prefiltrar_pool.py` (Camada 2 — pool-slim + blocklist de patologia, menos tokens) · `verificar_cobertura_anking.py` (passo 5 — prova de cobertura X/Y + `cobertura-<slug>.json`) · `aplicar_curadoria_anking.py` (passo 6) · `configurar_ritmo_anking.py` (ritmo: 25 novos/dia, 150 revisões/dia) · `revisao_diaria_anking.py` (monitor) · `dessuspender_anking.py` (dessuspensão grossa por tag, legado do lote1).
