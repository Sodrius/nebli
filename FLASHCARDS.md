# FLASHCARDS.md — Deck Anki NEBLI

> **Função:** documento vivo de filosofia, estado e processo do deck Anki do Davi. Ler antes de qualquer sessão de curadoria de cards, escolha de tags, ou resposta às bandeiras. Detalhes técnicos (scripts, comandos, schema) vivem em `flashcards/CURADORIA-ANKING.md`; este arquivo é o **porquê e o onde estamos**.

---

## Filosofia

**Guia triplo de conteúdo:** aulas FMUSP + Step 1 USMLE + base longitudinal para residência HC.

O deck Anki não serve para aprender — o resumo NEBLI faz isso. O deck serve para **reter na memória a longo prazo** o que já foi aprendido: tanto o conteúdo da faculdade (E1, E2, E3 de cada aula) quanto o que o Step 1 exige do mesmo sistema/mecanismo. Davi pretende fazer o Step 1 daqui a alguns anos e quer acumular base ao longo da faculdade, não estudar do zero na véspera.

**Critério fundamental:** precisão sobre recall. Menos cards, exatos para o que a aula ensinou + o que o Step 1 exige do mesmo sistema. Nunca acumular vizinhos do tema. Um deck enxuto e 100% da aula vence um deck grande com ruído — porque no Anki, card errado por falta de contexto se auto-suspende e distorce o algoritmo.

**Estado do processo (2026-07-09):** estamos calibrando como o Claude cria bons decks para o Davi — no formato certo, com o conteúdo certo, no escopo certo. Cada aula curada ensina algo. ANATO-06 foi o piloto; o próximo sprint cobre bioquímica da P4. O processo é iterativo: o Davi corrige e ajusta, o Claude aprende e incorpora.

---

## Regras gerais de curadoria (canônico 2026-07-10)

Pedido de Davi. Valem para **toda** aula curada, e governam tanto a seleção de cards do AnKing quanto a geração de cards NEBLI autorais. A pasta-lar de todo o trabalho de cards é `flashcards/` (hub em `flashcards/README.md`); exemplares de card em `flashcards/EXEMPLARES-CARDS.md` e `flashcards/ANTI-EXEMPLARES-CARDS.md`; estrutura do deck-mestre em `flashcards/estrutura-deck-mestre.md`.

**R1 — Nada órfão no deck (gate duro).** Davi nunca pode, ao estudar, esbarrar num conceito, palavra, ideia ou processo que o material NEBLI não explica. Todo card do deck-aula tem de ser respondível lendo a E1 daquela aula. Se um card é high-yield mas a E1 (como foi compilada) não cobre, o problema não é do card — é da E1: ela deveria ter recebido esse conteúdo. Por isso a curadoria roda **depois da E1 rascunho e ANTES da E2**: a janela existe justamente para injetar na E1 (e, em consequência, na E2) o que os bons cards revelam ser núcleo do tema, de forma natural.

**R2 — Cards um pouco mais profundos que o slide.** O deck vai deliberadamente **um tiquinho além** do que o slide propõe. Isso pressupõe que a **E1 também vá além** — ela é redigida assumindo uma aula um pouco mais profunda do que a que os slides sugerem ter sido dada. A E1 é o teto de profundidade do card; se o card precisa de mais, a E1 sobe primeiro (loop Card→E1). O calibre continua Step 1 (ver R8), nunca Step 2, e o vocabulário Step 1/USMLE segue banido no PDF.

**R3 — Bandeira vermelha (Ctrl+1) suspende; o email dessuspende.** Confirmado. `Ctrl+1` no estudo = flag:1 + suspende na hora. Ao rodar `monitor_email_anking.py --bandeira`, o script gera a explicação, envia o email e **dessuspende** + remove a flag. Sem mudança no fluxo já documentado — reafirmado como regra.

**R4 — Triagem de admissão em 3 baldes (substitui o "critério rígido"; flexível por design).** Não se rejeita card bom; faz-se a E1 crescer até ele. Todo card do pool on-scope cai num de três baldes:
- **ANCORADO** — o conceito já está numa frase da E1 → entra direto no deck-aula.
- **ANCORÁVEL** — on-scope, aprofunda um mecanismo que a aula já abre, mas a E1 ainda não diz → entra **contanto que** a E1 receba 1–3 frases (patch do loop Card→E1) **antes de compilar**. O card "puxa" a E1 pra cima. Este é o balde generoso — é ele que dá a flexibilidade.
- **FORA** — próxima-aula (escopo de outra aula do cronograma) OU ruído/Step 2 → **drop**. Nunca deixar no limbo.

A flexibilidade vem de o balde do meio ser largo e o loop ser a válvula: em vez de um portão que barra, o pipeline garante que todo card admitido esteja ancorado na E1 no momento da compilação. Isso é o que honra R1 sem estrangular a seleção.

**R5 — "Sobra mas é bom" tem dois destinos (nunca limbo).** Um card fora da E1 atual: se é **próxima-aula ou ruído** → drop (nem deveria ter sido escolhido); se é **aprofundamento legítimo do mesmo tema** → loop Card→E1 (patch na E1 antes de compilar). A decisão é sempre uma das duas — não existe card mantido no deck sem estar ancorado.

**R6 — Cobertura é quantitativa E qualitativa.** A pergunta não é "existe um card tocando o subtópico?" e sim "os cards do subtópico, somados, reconstroem o mecanismo que a E1 ensina, a ponto de o Davi reter a longo prazo?". Rubrica por subtópico (0–3):

| Nota | Significado |
|---|---|
| 0 | nenhum card no subtópico |
| 1 | só um **conceito similar** tangenciado (um termo em comum) — o falso "forte" que o Davi sente |
| 2 | cobra o **fato central**, mas não o mecanismo/porquê |
| 3 | cobra fato **+ mecanismo/relação** — permite reconstruir a ideia de memória |

Match "forte" da aula só quando a maioria dos subtópicos está em 2–3 **e** nenhum subtópico nuclear está em 0–1. A nota Cards×E1 (0–10) do relatório de fechamento passa a ser a média dessa rubrica normalizada, não a contagem X/Y de subtópicos tocados. (Aplicado a embrio-gastrulacao-neurulacao, isso derruba o "match forte" aparente: EMT e os dois dobramentos ficam em 0, linha-primitiva-organizadora e membranas em 1.)

**R7 — Poda Step 2 já no pré-filtro.** Davi se prepara para o **Step 1**, não o Step 2. Quando as tags derem pool, remover já as notas exclusivamente Step 2 (tags `#AK_Step2_v12::`, decks de Step 2, conteúdo de manejo/tratamento clínico avançado) antes do keep/drop fino. Cai no `prefiltrar_pool.py` como blocklist adicional. Reduz o pool e o custo de tokens.

**R8 — Análise de cobertura reporta os dois eixos.** O relatório de fechamento traz, por subtópico: nota da rubrica R6 (qualitativo) + nº de cards (quantitativo) + veredito (COBERTO / RASO / LACUNA). "Todos os conceitos E de forma satisfatória" é o gate: subtópico nuclear RASO ou LACUNA volta pra prancheta (patch na E1 ou card NEBLI autoral) antes de fechar.

**R9 — Formato do card NEBLI autoral (canônico 2026-07-10).** Todo card gerado pelo NEBLI é **cloze deletion**, com **um único cloze por card** (`{{c1::...}}` — nada de c1/c2/c3 no mesmo card virando vários cards). Tem sempre uma **explicação sucinta** no campo Extra (1–2 frases, voz NEBLI, o *porquê*). E, **quando for viável conseguir**, uma **imagem** — do slide do professor ou da figura de outros cards do AnKing — para deixar o card visual. Formato e voz seguem `flashcards/EXEMPLARES-CARDS.md`.

**R10 — Menos é mais (calibre de volume).** Melhor **poucos cards com o conteúdo da aula** do que muitos cards sem relação. O ótimo (melhor dos dois mundos) é: conteúdo da aula **+ um pouco mais aprofundado**, sem exagerar ("sem ficar maluco"). Em conflito entre cobrir tudo e não inflar, cobre bem o núcleo e não força a cauda.

**R11 — Representação proporcional dos subtópicos (canônico 2026-07-10).** Subtópicos maiores/mais pesados da aula devem, de forma **natural**, aparecer proporcionalmente mais — tanto em profundidade da E1 quanto em número de cards. Não é cota rígida: é deixar o peso do tema reger o espaço que ele ocupa (o passe de aprofundamento e a seleção de cards seguem o peso do subtópico, não distribuem por igual).

**R12 — Norte de profundidade + menos atrito (feedback 2026-07-10/14).** Davi sente que **E1, E2, E3 e os cards ainda estão rasos**. O objetivo declarado é: material **mais aprofundado e com menos atrito**, para ele reter a informação aprofundada no tempo que tem até a prova **e** para o Step 1. Toda geração daqui pra frente puxa a profundidade pra cima (dentro de R2/R10 — fundo, mas não maluco) e reduz atrito (prosa fluida, card atômico com explicação e imagem). Feedback de 2026-07-14: quando a E1 não pôde ser reescrita, os cards ficaram rasos; portanto, nas próximas aulas o aprofundamento precisa acontecer **antes** de fechar cards, via loop Card→E1, não tentando compensar com card solto. Ver [[feedback-cards-e-resumos-mais-fundos]].

**R13 — Card autoral só entra se for AnKing-grade (canon 2026-07-14).** Feedback do Davi: os NEBLIcards prontos ainda parecem "cards criados pelo NEBLI", não AnKing. Correção: NEBLIcard autoral novo precisa seguir `flashcards/AUDITORIA-NEBLICARDS-ANKING-2026-07-14.md`: inglês por padrão, note type AnKingOverhaul, frente curta, cloze de 1–3 palavras no token de maior valor, mecanismo fora do stem, Extra curto em registro de nota de card, imagem quando visual, sem voz de apostila. Antes de aplicar: `lint_neblicard.py` + card-mirror quando o lote muda padrão. O aplicador preferido é `build_card.py`; `aplicar_neblicards.py` fica como compatibilidade legada sem mídia.

**R14 — Anatomia macro exige eixo peça real (canon 2026-07-14).** Deck de anatomia não fecha só com cloze/ilustração. Quando houver fonte disponível, cada aula de anatomia macro deve combinar: (1) esquema limpo para relações espaciais (Dope/Netter-style/AnKing) + (2) **foto cadavérica real em Image Occlusion** para reconhecimento de peça. Fonte primária já mapeada: `Referências Externas::University of Michigan BlueLink Atlas`, buscada por tag (`BlueLink::<Região>`, keyword não funciona). Cópias para `NEBLI::` usam `flashcards/scripts/copiar_externos_para_deck.py`, preservando original, mídia e note type. Ver `referencias-externas/DECKS-EXTERNOS-MAPA.md`.

**R15 — Referências Externas antes de autoria (canon 2026-07-14).** Quando o AnKing não cobrir um conceito que precisa de card, a próxima fonte não é automaticamente NEBLIcard autoral. Buscar primeiro nos decks externos importados, conforme `referencias-externas/GUIA-CARDS-EXTERNOS-PARA-DECK-AULA.md`: BlueLink para cadáver/IO, Dope Anatomy para atlas e relações, Histology/LLU para cortes histológicos e micrografias, Dorian/100 Concepts para correlato clínico anatômico. Card externo aprovado entra como `NEBLI::externo`, não como autoral; original externo fica intocado.

**R16 — Imagem no Extra é o default (canon 2026-07-14).** A maioria dos cards deve ter imagem na explicação, como no AnKing. Para card autoral novo, `build_card.py --require-images` vira o padrão salvo exceções explícitas (fato puramente verbal). Fonte de imagem, em ordem: imagem irmã do AnKing/external card, deck externo, internet limpa licenciada, slide do professor, Junqueira/atlas quando permitido no contexto pessoal. Os 187 autorais já existentes no Anki foram marcados `NEBLI::needs_image`; nenhum tinha imagem no Extra na auditoria de 2026-07-14.

**R16b — Imagem como intervenção cognitiva (canon 2026-07-14).** Regra refinada em `flashcards/GUIA-IMAGENS-CARDS-NEBLI.md`: não medir "tem imagem"; medir se a **necessidade visual** do card foi satisfeita. Todo card novo deve decidir `visual_need` (`required|recommended|optional|none`) e `image_role` (`recognition|localization|mechanism|comparison|schema|context|none`). A pertinência é card-específica: imagem por tema/aula/slide não conta como resolvida se não treina o alvo exato do card. Trocar "imagem por tema" por "imagem por intenção" (identificar, localizar, comparar, demonstrar mecanismo, reconhecer padrão ou fixar relação espacial). Internet pode ser usada, mas com fonte, URL, licença/uso, crédito e data; material privado entra marcado como privado, não como redistribuível. Imagem decorativa, genérica, ilegível, errada ou que entrega o cloze é bloqueio, não melhoria.

**R17 — Histologia exige par visual + conceito (canon 2026-07-14).** Para estrutura histológica, deck completo tem dois cards quando cabível: (a) identificação visual em corte/micrografia, preferencialmente IO; (b) função/origem/relação em cloze normal com imagem no Extra. Se Histology/LLU não trouxerem a estrutura, criar IO próprio sobre micrografia com `io_manual_from_image.py` (ex.: corpúsculo de Hassall no timo) e um cloze conceitual ancorado na E1. Saber a estrutura no corte é parte do conteúdo, não ilustração opcional.

**R18 — Construção longitudinal Step 1 + residência HC desde o ciclo básico (canon 2026-07-14, pedido do Davi).** Cada deck-aula passa a construir três camadas sem virar três currículos nem duplicar cards: **(1) Faculdade define O QUE entra** — conteúdo da aula/E1 e da prova local; **(2) Step 1 define a profundidade do MESMO mecanismo** — causa, fisiopatologia, predição, gráfico/lab, genética, mecanismo de ação e reconhecimento visual; **(3) residência HC fornece uma ponte clínica pequena e estável** — estrutura/alteração → mecanismo → achado discriminante. No ciclo básico entram mecanismo, localização, sinal/lab esperado e morfologia funcional; ficam FORA conduta, dose, guideline, rastreamento, staging, técnica operatória e qualquer conteúdo que dependa do internato/Step 2.

**Gate E1 absoluto também para Step 1/HC.** Nada desta camada pode aparecer primeiro no deck. O fluxo é sempre: card/blueprint/prova sugere → Orquestrador julga se é o mesmo mecanismo e se vale a carga → **injeta e explica na E1 antes** → só então cria/seleciona o card → E2/E3 cobra com pista nova. A injeção na E1 não é termo solto: precisa explicar em prosa causal **base → mecanismo → achado**, geralmente em 2–5 frases no mesmo parágrafo ou em `#clinica-box` natural. Se exige abrir um tópico clínico próprio ou vários pré-requisitos laterais, é FORA. Uma bridge sem `e1_anchor` é bloqueada.

**Unidade de qualidade = cluster cognitivo seletivo.** Para apenas os mecanismos realmente nucleares, montar um `cluster_id` com em geral **2–4 cards no total, contando os bons já existentes** — nunca 2–4 cards novos obrigatórios: (a) fundamento/pré-requisito; (b) mecanismo; (c) consequência ou predição; (d) opcionalmente discriminador ou visual autêntico. Remover/substituir redundância antes de adicionar. Cada card testa um alvo inequívoco; relações com mais de um elemento só valem quando formam uma única unidade causal/estrutural coerente.

**Clinical bridge = questão de transferência com cue novo.** Cada cluster nuclear pode receber **uma** ponte de aplicação que muda a pista: o card pergunta a peça; a ponte pergunta o que acontece quando ela falha, qual estrutura explica o déficit, qual direção o lab assume ou qual imagem representa o mecanismo. A bridge não repete a frase do card e não vira vinheta longa. No piloto: 1–2 clusters por aula, 1 bridge por cluster e **máximo de 3 bridges/aula**, sem quota. Inicialmente a bridge é candidata offline; testar se rende melhor na E2/banco ou no Anki longitudinal antes de canonizar seu destino.

**Padrão linguístico pedido pelo Davi.** A frente, o cloze e a terminologia principal dos cards ficam **em inglês médico natural**, inclusive nos autorais. O `Extra` traz explicação curta em **português**, com causa → mecanismo → consequência, e traduz/desambigua os termos médicos específicos que possam gerar atrito (ex.: `compliance = complacência/distensibilidade vascular`, explicando o conceito, não só dando tradução). Não duplicar um card em PT e EN. Não usar tradução literal estranha: conferir nomenclatura em fonte médica; preservar epônimos, siglas e termos que a prática brasileira também usa. Termo óbvio ou idêntico nas duas línguas não precisa de glossário artificial.

**Rubrica de admissão da camada longitudinal — todos os gates precisam passar:**

1. **Âncora:** está explicado na E1 ou recebeu patch antes do deck?
2. **Escopo:** é o mesmo mecanismo da aula, não uma doença vizinha?
3. **Durabilidade:** continuará correto daqui a anos, sem depender de guideline?
4. **Transferência:** ajuda a prever/localizar/discriminar um achado, em vez de acrescentar trivia?
5. **Baixo custo:** é entendível com poucos pré-requisitos e não infla/redunda o cluster?
6. **Teto clínico:** termina em mecanismo → achado; não avança para manejo de Step 2/internato?

**Tipos de adição de alto valor:** mecanismo nuclear; perturbação → direção de variável; achado → estrutura/mecanismo; discriminador entre confundíveis; gráfico/laboratório com predição; pedigree/regra genética; mecanismo de ação quando a E1 abriu o alvo; micrografia/peça/imagem quando o objeto visual é o próprio cue. **Não entram:** definição nua, lista empilhada, card para cada alternativa errada, imagem decorativa, doença mencionada só porque caiu em prova, vinheta completa, conduta/dose ou duplicata FMUSP×Step1×HC do mesmo fato.

**QA obrigatório por cluster:** registrar `cluster_id`, `concept_id`, `e1_anchor`, papel (`core_atomic|application_bridge`), objetivo (`fmusp|step1|hc_base`), `cue_type`, idioma e fonte. O fechamento reporta cards reaproveitados × novos, redundâncias removidas, nº de bridges e incremento líquido. A bridge precisa de feedback que reconstrua o mecanismo, diga qual cue discriminava e por que o erro tentador falha. Flags/comentários reais pesam mais que card-mirror: vermelho diagnostica E1/card/imagem; verde vira controle positivo. Escalar só após 2–3 semanas medindo tempo, backlog, Again, retenção, flags e acerto em questões com cue novo.

Detalhe operacional destas regras e a decisão deck-AnKing vs deck-NEBLI estruturado: `flashcards/estrutura-deck-mestre.md`. **Estamos em evolução ativa do processo de cards — muitas destas regras vão mudar conforme Davi pede curadoria a cada resumo novo.**

---

## Estrutura do deck de estudo + regra do AnKing intocado (canônico 2026-07-12)

**Árvore única de estudo:** `NEBLI :: UC :: Prova :: Componente :: Aula` (ex.: `NEBLI::UC02::P4::Bioquímica::Metabolismo dos aminoácidos`). O topo `NEBLI` recebe outras UCs no futuro. Prova vem **antes** de componente — então nunca existe um "Bioquímica P1–P4" agregado (o Davi não estudaria isso; cai em provas diferentes). Uso: estudar `NEBLI` inteiro = retenção longa (FSRS, **15 novos/dia**, ~25 min/dia); abrir `NEBLI::UC02::P4` = cravar antes daquela prova. Como é subdeck aninhado, **um card mora numa aula só** e estudar qualquer pai o inclui — o mesmo card serve retenção longa E cram de prova, com um agendamento FSRS único (Custom Study aumenta novos no deck-prova sem mexer no ritmo do geral).

**Regra do AnKing intocado (canônico 2026-07-12, pedido do Davi):** o deck AnKing fica na coleção como **referência, 100% suspenso, nunca modificado**. O card de estudo é sempre uma **CÓPIA duplicada para a árvore NEBLI, com tudo — campos, imagem, crédito e TAGS**. Nunca taguear/mover/editar o card AnKing original (o erro antigo era pôr a tag `NEBLI::` no original, criando duplicata ativa). Prova por cronograma vem do PDF em `cronogramas/` (UC02 v1-jul: Bioquímica+Biologia Molecular = **P4/13-jul**; Histo/Anato/Embrio/Imuno = **P3/16-jul**). Organizador: `flashcards/scripts/organizar_anki_nebli.py` (move cópias curadas p/ a árvore, suspende AnKing + duplicatas + restos; reversível). **Reorganização de 2026-07-12:** só o NEBLI:: fica ativo; aminoácidos/lipídeos/biomol-25 → P4, embrio → P3. Pentoses/glicogênio/biomol-26 ficaram fora (não calibrados — "várzea"); Davi vai pedir p/ regerar o deck-prova P3 e apagar o P4 depois.

**Ritmo e cram por prova (canônico 2026-07-14, recalibrado por FSRS).** O topo `NEBLI` fica em **até 15 novos/dia** para retenção longa; revisões vencidas vêm primeiro e o teto de revisões fica alto (`9999`) para não esconder devidos. Cram não vira currículo: devidos/erros da prova entram em filtered deck com rescheduling ligado; novos vistos só por urgência entram em preview com rescheduling desligado. Gerador seguro: `flashcards/scripts/planejar_modo_prova.py`. Os scripts P3/150 são legado, agora preview por padrão e exigem `--apply` explícito. Guia: `flashcards/GUIA-RITMO-E-MODOS.md`.

## Pipeline por aula (visão geral)

**Reordenação canônica 2026-07-10 (pedido de Davi):** o ideal é a seleção de cards + o passe de aprofundamento da E1 rodarem **ANTES da E2**, para que a E2 já cobre o conteúdo extra (a E2 sobe de teto junto com a E1). Os cards do AnKing **induzem** boa parte dos aprofundamentos — e esses bons cards vão para o deck-aula. Ver `CLAUDE.md` § Aprofundamento da E1 + `ROLES.md` § Redator diretriz 17.

```
E1 rascunho
   ↓
   1. Checklist-alvo (E1 rascunho como fonte)
   2. Busca de tags (keyword-first, sweep amplo se gap) — Anki vivo OU export offline
   3. Pool + pré-filtro
   4. Matriz conceito×card (coluna "In E1?") — cards induzem candidatos a aprofundamento
   5. Passe de aprofundamento (≈1 injeção/subtópico; slide regula escopo, card/livro regula profundidade)
   ↓
E2 → E3  (já cobrando o conteúdo aprofundado)
   ↓
   6. Re-check leve: conceito só-da-E2 sem card vira LACUNA; prova de cobertura X/Y COBERTOS
   7. Compilar PDF
   8. Índice de completude no fechamento (E1×slide, E2×E1, Cards×E1 — 0 a 10)
   9. Apply no deck via AnkiConnect + sync (quando Anki vivo)
```

**Sem Anki vivo:** os passos 2-4 rodam do export (`anking-v12-export.txt`) como seleção offline; o aprofundamento nasce do mapa de cobertura + blueprint + bibliografia; o apply (passo 9) fica pendente até o Anki subir (a seleção fica pronta em `flashcards/curadoria/<slug>.md`). Foi assim no piloto embrio-gastrulacao-neurulacao (2026-07-10).

**Índice de completude Cards×E1 (0-10):** o X/Y COBERTOS da prova de cobertura vira uma das 3 notas do relatório de fechamento (ver `ROLES.md` § Índice de completude). Meta ≥7; lacuna aponta fonte.

Detalhes técnicos de cada passo em `flashcards/CURADORIA-ANKING.md`.

---

## Checklist-alvo: E1 + E2 (canônico 2026-07-09)

A fonte-verdade da checklist não é só a E1 — é E1 **mais** os conceitos testados na E2.

`gerar_checklist.py` varre o `etapa1.typ` (termos-nota + siglas) **e** o `etapa2.typ` (conceitos cobertos nas 30 questões). Cada entrada do `.tsv` tem origem marcada (`E1` ou `E2`). Conceito na E2 sem card → LACUNA de maior prioridade (a E2 testa exatamente o que precisa ser retido).

---

## Loop Card→E1 (canônico 2026-07-09)

Após construir a matriz conceito×card, a coluna **"In E1?"** classifica cada card kept:
- **Sim** — reforça algo já explicado na E1 → deck normalmente.
- **Parcial** — a E1 menciona o conceito mas sem mecanismo suficiente → considerar enriquecer 1–2 frases.
- **Não** — conceito novo que a E1 não cobre → avaliar se qualifica para patch.

### Critério de qualificação para patch na E1

Um card "não na E1" qualifica para enriquecimento da prosa se **todos** os critérios abaixo forem satisfeitos:

1. **Escopo direto:** o conceito é diretamente do tema da aula — não adjacente, não "o que vem depois".
2. **Estende um mecanismo já na E1:** aprofunda ou completa uma cadeia causal já presente (cofator não mencionado, intermediário da via pulado, aspecto Step 1 do mesmo mecanismo). Não é tópico standalone.
3. **Teste do monitor:** "se estivesse explicando essa aula ao vivo, esse conceito apareceria naturalmente no mesmo parágrafo?" → sim = qualifica.
4. **Step 1 relevante:** o conceito aparece no Step 1 para o mesmo sistema/mecanismo.

**Não qualifica (drop automático do patch, mas mantém no deck):**
- Topografia/relação anatômica que a E1 não ensina
- Complicação clínica/patologia quando a aula é anatomia/fisiologia básica
- Detalhe métrico (nível vertebral, medida) sem valor mecanístico
- Conceito que exige "falando em outra coisa..." para encaixar na E1

**Regra de profundidade (canônico 2026-07-09):** quando o card do AnKing cobrir o MESMO conceito que a E1 mas com maior profundidade mecanística, a E1 adota a profundidade maior no patch. O inverso também vale: slide mais profundo que o card não é limitado pelo card. **Profundidade = max(AnKing, slide/banco)** para o conceito em questão.

**Volume não fixo:** calibrar pela experiência. Quanto mais os cards aumentarem a eficiência do estudo, mais vale aprofundar a E1 para aumentar a cobertura; se não aumentar, não vale adicionar carga. Não há meta de 2-5 adições — há a pergunta "esse conceito merece estar na E1?"

---

## Estratégia de busca de tags (dois passes)

Para equilibrar recall e custo de tokens:

**Passe 1 (sempre):** busca por keyword da checklist (`buscar_tags_lote.py`). Rápido e barato. Se cobertura ≥ 70% dos conceitos → fecha sem passe 2.

**Passe 2 (só se cobertura < 70%):** sweep amplo sobre as subárvores do assunto (ex: toda `SketchyAnatomy::02_Thorax` para uma aula de anatomia torácica) — filtra cada LACUNA declarada contra o texto real do card. O `prefiltrar_pool.py` (blocklist de patologia, ~70% de redução de tokens) já existe e se aplica aqui. O custo extra é direcionado: só roda para os gaps reais, não para o pool inteiro.

---

## Regras de busca e admissão de cards (canônico 2026-07-11)

Substitui a "busca keyword-first" como Camada 1 padrão quando o **Anki está vivo**. Nasce do diagnóstico de que a curadoria antiga ficou ruim por **lacunas fantasma**: `buscar_tags_lote.py` casava a keyword contra o **caminho da tag** num export estático, então reparo/conjugação/mismatch davam 0 mesmo cobertos pelo AnKing.

**B1 — Buscar por CONTEÚDO, não por caminho de tag.** Camada 1 nova = `descobrir_cards_por_conceito.py <slug>`: para cada conceito da checklist, `findNotes` sobre o **texto real do card** (via AnkiConnect), coleta as tags das notas que casam e devolve as subárvores candidatas ranqueadas. Acha o card **onde ele mora** (mata a lacuna tipo-b: existe no AnKing mas fora da subárvore que o curador lembrou). Filtro IDF descarta tokens comuns (factor/base/mutation) e filtro de meta-tags tira `#Low/HighYield`, `#OME_banner`, IDs AMBOSS/NBME. **Limite conhecido:** busca por keyword sofre de **polissemia** ("repair" casa hérnia/osso) — o relatório é *recall-orientado* (candidatas), a Camada 2 (leitura card-a-card) faz a precisão. Confirmação de lacuna real = probe do **termo distintivo** (`findNotes "photolyase"` = 0 → lacuna de verdade). A busca semântica por embeddings é o conserto definitivo da polissemia (ver `flashcards/PLANO-PESQUISA-CARDS-IA.md`).

**B2 — Gate absoluto (implementa R1 como gate, canônico 2026-07-11).** Nenhum card entra no deck-aula se seu conceito não está na E1. No pipeline canônico o aprofundamento entra **pela E1** (AnKing propõe → Orquestrador injeta 1-3 frases → vira card). **Sem etapa de E1 (deck de PDF pronto): só o que já está na E1.** Ver `CLAUDE.md` § GATE ABSOLUTO DO DECK-AULA.

**B3 — Dosagem de conteúdo periférico (flexibilidade do Orquestrador).** É **responsabilidade do Orquestrador** não lotar o deck (nem a E1) com conceitos periféricos — overload de cards que o Davi não consegue aprender, ou de conteúdo na E1. Um periférico (aprofundamento que o AnKing propõe e a E1 ainda não tem) só vale a injeção-na-E1 → card quando passa nos **dois** testes:
   1. **Altamente relacionado** — nota **≥ 8 de 0 a 10** de proximidade ao conteúdo da aula. Não é "toca no tema"; é "é o mesmo mecanismo, uma camada abaixo".
   2. **Baixa carga de pré-requisito** — o Davi entende sem ter que aprender vários conceitos laterais antes. Se para encaixar o card ele precisa de scaffolding próprio (um tópico novo do zero), **não vale** — é FORA.

**B4 — Aprofundamento clínico: poucos e naturais.** Alguns (não muitos) cards de aprofundamento clínico aumentam a base do Davi e valem a pena — mas **só** quando o conteúdo caberia na E1 **de forma muito natural** (mesmo parágrafo, mesmo mecanismo). Clínica que exige seu próprio enredo é FORA. O calibre continua Step 1, nunca Step 2 (R7).

**B5 — Menos é mais, sempre (reafirma R10).** Em conflito entre cobrir a cauda periférica e não inflar, cobre bem o núcleo e para. Deck enxuto 100% ancorado na E1 vence deck grande com periferia. O Orquestrador dosa — o peso do tema (R11) rege quanto cada subtópico ocupa.

---

## NEBLIcards — cards autorais para lacunas (canônico 2026-07-11)

> Pesquisa completa (500 cards do AnKing dissecados + SuperMemo/Matuschak/Nielsen + repos de IA) em `flashcards/PESQUISA-BOM-CARD.md`. Esta seção é o essencial operacional.

**⚠ LAST RESOURCE — NÃO é o padrão.** O padrão do deck-aula é **card AnKing curado** (validado por milhões, com imagem/Extra/formato maduro). Gerar NEBLIcard é a **resposta do pipeline canônico às LACUNAS tipo-a** — conceito da E1 que o AnKing **genuinamente não tem** (confirmado por probe do termo distintivo = 0, ex.: fotoliase, resposta SOS, tautômero). Ordem sempre: **(1) card AnKing curado → (2) subtópico coberto? pronto → (3) só se resta lacuna real, gerar NEBLIcard.** Nunca gerar para o que o AnKing já cobre.

**O que a dissecação de 500 cards ensinou (destilado):**
- 100% cloze · **86% single-cloze** (atomicidade é a norma) · frente mediana **17 palavras** · **83% com Extra** (mediana 20 palavras) · 47% com imagem.
- O cloze apaga o **token de maior valor** (diagnóstico, enzima, número, direção ↑/↓), nunca enchimento.
- O **Extra carrega o PORQUÊ**: mecanismo, ou discriminador da confusão clássica, ou mnemônico.
- Contexto rico na frente (nunca definição nua) — a frase dá a pista de recuperação.

**Formato do NEBLIcard (reafirma e detalha R9):**
- Cloze, **1 por card** (`{{c1::…}}`); multi-cloze só para partes de UM fato.
- **Frente:** frase declarativa NEBLI (ou pergunta focada), ≤ ~20 palavras, com o token-chave clozado; a frase sozinha contextualiza.
- **Extra obrigatório:** 1–2 frases em **voz de monitor** (causa→mecanismo→consequência) OU discriminador. ≤ ~35 palavras. Sem Extra = card nota ≤1.
- **Imagem** do slide (`figuras/<slug>/`) quando o fato é visual.
- **Tags:** `NEBLI::<slug>` + `NEBLI::gerado` (distingue autoral de AnKing curado; auditável/reversível).
- **GATE:** o conceito TEM de estar na E1 (senão nem gerar).

**Princípio anti-reconhecimento (feedback Davi 2026-07-11):** o cloze apaga a informação que **exige saber** (mecanismo, consequência, valor, discriminador), NÃO o rótulo óbvio que a frase já entrega. Teste: *"dá pra adivinhar o branco só relendo a frase?"* Se sim, mova o branco. **Mas o cloze é CURTO e único** — 1 token ou frase-curta (mediana AnKing ~1–3 palavras); direção difícil = mover o branco para o token certo, **não** apagar a oração inteira (isso perde a unicidade). Ex.: apagar `guanina`/`C→T`/`autoclivagem`, não "parear com guanina fixando A→G".

**Gate anti-indução (canônico operacional 2026-07-14).** Todo lote autoral passa por `python flashcards/scripts/lint_neblicard.py <json>` antes do card-mirror. `REJECT` volta para reescrita; `MIRROR` vai para o card-mirror; `PASS` pode seguir. O linter barra os vazamentos determinísticos: nome/rótulo no stem com descrição apagada, sigla auto-entregue, parêntese que entrega, negrito que denuncia e cloze longo/mecanismo no stem como zona cinza.

**Rubrica (0–3, entra só ≥2):** 0 ambíguo/enchimento · 1 fato nu sem contexto/sem Extra · 2 frente contextualizada + cloze no token-chave, **mas adivinhável** · 3 o cloze apaga mecanismo/consequência/discriminador (baixa adivinhabilidade) + Extra reconstrói o porquê (+ imagem se visual).

**Anti-padrões (rejeitar):** enumeração empilhada num card; definição nua; multi-fact cloze com brancos independentes; Extra que repete a frente; cloze ambíguo; conceito fora da E1; escopo Step 2.

**Quando gerar no pipeline:** Fase dedicada, NÃO no `/resumo` automático. Só após a curadoria AnKing fechar e restarem lacunas tipo-a com fonte apontada. Grava em `flashcards/cards-nebli/<slug>.json`. Ver `PESQUISA-BOM-CARD.md` Parte 4 (spec) e a fila `PENDENTE-GERADO`.

**Auditoria 2026-07-14 — rebuild obrigatório dos autorais prontos.** Os 43 autorais existentes foram auditados em `flashcards/AUDITORIA-NEBLICARDS-ANKING-2026-07-14.md`. Decisão: embrio-01, embrio-02-03 e biomol-25 precisam rebuild completo; bioq-21 e bioq-23 precisam normalização e imagem/card-mirror. Não aplicar lote antigo sem passar pelo rebuild.

**Manutenção Anki 2026-07-14.** Rodado `python flashcards/scripts/manutencao_neblicards_anki.py --apply`: removeu `Source/Fonte` visível dos NEBLIcards autorais/gerados. Depois do enriquecimento visual P3, a manutenção reconhece imagem em campos visuais (`Extra`, `Image`, `Imagem`, etc.) e deixou **187/187 autorais/gerados com `NEBLI::image_extra` e 0 com `NEBLI::needs_image`**. Atenção: 186 estão `NEBLI::image_context_needs_specific_review`, pois receberam imagem de contexto por tema; próximo passe deve trocar por imagem específica quando o card pedir reconhecimento visual fino.

**Normalização de note type legado 2026-07-14.** Rodado `python flashcards/scripts/normalizar_modelos_nebli_anking.py --apply`: o modelo legado `Cloze Medicina - Mecanismo Único` foi normalizado em 32 notas NEBLI com CSS/template AnKing-like (fonte 28px, cloze azul em negrito, Extra enxuto e imagem sem card decorativo). O padrão novo continua sendo `AnKingOverhaul`; modelo legado só é compatibilidade.

## Bandeiras

### Vermelha (flag:1) — "me explique este card"
Davi marca durante o estudo quando quer entender um card mais fundo. Claude redige **2 parágrafos em voz NEBLI** (causa→mecanismo→consequência):
- Parágrafo 1: o mecanismo do card (o que ele testa, por que é verdade)
- Parágrafo 2: contexto — por que importa, como se liga ao que o Davi estuda na aula daquele bloco `NEBLI::<slug>`

**Fluxo de suspensão (canônico 2026-07-09):** quando `--bandeira` é rodado, os cards flag:1 são **suspensos imediatamente** (saem da fila de revisão). Depois de gerar e enviar o email, a bandeira é removida e os cards são **dessuspensos** (voltam à fila). Assim o Davi lê a explicação antes de ver o card de novo.

**Modo auxiliar:** `python flashcards/scripts/monitor_email_anking.py --suspender-vermelhos` suspende os cards vermelhos na hora, sem enviar email. Útil quando o Davi marca durante o estudo e quer parquear imediatamente sem esperar a sessão com Claude.

### As 3 bandeiras = o loop de estudo → curadoria (canônico 2026-07-12, reformulado)

Com o `Ctrl+1` consertado (add-on `nebli_flag_suspender` reescrito), cada bandeira volta a ter **sentido próprio** — e as 3 são exatamente os 3 sinais que o sistema precisa pra se auto-corrigir. É a mesma máquina do **Revisor-completude** (E1↔cards), alimentada pela ponta do estudo real: um card marcado é uma falha de completude que escapou da geração.

- **🔴 Vermelha (flag:1) — "me explica/revisa esse card".** `Ctrl+1` = flag + suspende na hora. `--bandeira` gera 2 parágrafos voz-NEBLI (mecanismo + contexto), envia, dessuspende, remove a flag. Feedback 2026-07-14: vermelho também é pedido de revisão de qualidade do card; provavelmente o card está ruim, mal ancorado, raso, redundante, com cloze frouxo ou imagem inadequada. **Sinal de curadoria:** card vermelho ⇒ revisar E1 + card + imagem, não só explicar.
- **🟠 Laranja (flag:2) — "esse card faz sentido aqui?"** (canônico 2026-07-12 — substitui o "laranja=vermelha" de 2026-07-10). Davi duvida que o card pertença ao conteúdo. Claude **re-julga contra a E1**: **ANCORADO** (fica) ou **FORA** (dropa do deck + vira **anti-exemplar** em `flashcards/ANTI-EXEMPLARES-CARDS.md`, pra aprender o padrão de card-várzea). Fecha a pergunta "esse card era pra estar aqui?".
- **🟢 Verde (flag:3) — "card bom".** Vira **exemplar** em `flashcards/EXEMPLARES-CARDS.md` (forma + gesto) — os NEBLIcards futuros aprendem com o que Davi aprovou.

**Regra:** um card marcado (vermelho/laranja) é, no geral, um card **mal ancorado na E1**. Ao processar as bandeiras, Claude reporta quantos dos marcados não têm âncora — muitos = a E1 daquela aula precisa subir OU o deck precisa podar (violação de R1). Esse relatório volta pro Revisor-completude.

### Carga viável de cards por aula (canônico 2026-07-12)

Davi quer uma quantidade que **puxe pra cima** — sempre aprofundar um pouco mais que o professor cobra — mas **sustentável** (nunca um deck de 120 cards insustentável). Não é cota fixa; é um **alvo** que a curadoria e o Revisor-completude usam. Classificar a aula em dois eixos e derivar a banda:

- **Peso** (quantos subtópicos/mecanismos a E1 tem): pequena (~5-6) · média (~8-10) · grande (~12+, ex.: Krebs, ciclo da ureia).
- **Rendimento** (high-yield pra FMUSP + Step 1): baixo · médio · alto.

**Densidade-alvo por subtópico nuclear:** ~3-5 cards (rendimento baixo) → ~6-8 cards (rendimento alto); periféricos ganham 1-2. Bandas práticas resultantes: **pequena 25-40 · média 40-65 · grande 65-90** cards por aula. O viés "puxa pra cima" = mirar o **terço superior** da banda que ainda cabe em 15/dia (uma aula de 50 cards = ~3-4 dias de novos — sustentável). Acima de ~90 numa aula só, parar e podar redundância (R10: dois cards com info redundante = oportunidade de 1 card novo com info nova). O número entra no Tema Card (Seção A) como `carga_alvo: <n>` e o Revisor-completude sinaliza se o deck ficou abaixo (lacuna) ou muito acima (inflado).

**Sinal importante:** no geral, um card marcado (laranja/vermelha) é um card **que não foi explicado na E1**. Por isso, ao processar as bandeiras, Claude também reporta *quantos* dos marcados não têm âncora na E1 — muitos marcados = sinal de que aquela aula tem card demais sem explicação (violação de R1), e a E1 daquela aula precisa subir ou o deck precisa podar.

### Verde (flag:3) — "este é um bom card" (canônico 2026-07-10)

Davi marca verde quando um card é bom. Quando ele pedir "analisa as bandeiras que marquei", os **verdes viram exemplares**: Claude os adiciona a `flashcards/EXEMPLARES-CARDS.md` (forma + gesto). É o canal de calibração positiva — o deck aprende com o que o Davi aprovou.

### Ao analisar os laranjas/vermelhos — checar pertinência (canônico 2026-07-10)

Quando Claude for ver os cards marcados, além de explicar, **julga se cada um merecia estar ali**: era conteúdo daquela aula (ANCORADO/ANCORÁVEL) ou era card que nem deveria ter sido escolhido (FORA — próxima-aula/ruído)? Card FORA marcado vira drop + nota no anti-exemplar. Isso fecha o loop de qualidade do deck.

### Comentários diretos no card (add-on 2026-07-14)

Add-on criado e instalado localmente: `flashcards/anki-addons/nebli_card_comments/` → `%APPDATA%\Anki2\addons21\nebli_card_comments`. No reviewer, `Ctrl+Shift+C` abre uma janela para comentar o card atual. O comentário é anexado ao campo `NEBLI_Comentario`, classificado por tipo (`problema`, `qualidade`, `imagem`, `explicacao`, `escopo`, `formatacao`, `outro`) e marcado com `NEBLI_comentario::pendente`. O Claude lê depois com `python flashcards/scripts/ler_comentarios.py --sync`. Esse canal passa a ser o feedback fino de qualidade/defeito card-a-card.

**Limite AnkiDroid:** add-ons desktop não rodam no AnkiDroid. No tablet, o caminho compatível é usar flags/tags ou editar o campo sincronizado `NEBLI_Comentario`; o desktop lê isso depois via AnkiConnect quando a coleção sincronizar.

---

## Email

**Sempre sob demanda** (canônico 2026-07-07). Nada automático. Davi pede no chat → Claude roda o script.

---

### Fluxo completo — Bandeira Vermelha (flag:1) ✅ implementado

> "Quero entender esse card mais fundo."

```
Davi marca card vermelho durante o estudo
          ↓
[Opcional] "suspende meus vermelhos"
  → python monitor_email_anking.py --suspender-vermelhos
  → cards saem da fila imediatamente (não aparecem até email chegar)
          ↓
Davi pede: "manda o email da bandeira vermelha"
  → python monitor_email_anking.py --bandeira
          ↓
Script: sync AnkiConnect → coleta flag:1 → suspende (se não foram antes)
        → gera 2 parágrafos por card via claude -p (mecanismo + contexto)
        → envia email HTML para dpbdes@gmail.com
        → remove flag:1 + dessuspende os cards
          ↓
Davi lê email antes de revisar os cards
Cards voltam à fila com mecanismo entendido
```

(O formato dos 2 parágrafos do email está descrito em § Bandeiras → Vermelha.)

---

### Add-on Anki — Ctrl+1 = bandeira vermelha + suspender (canônico 2026-07-09)

O atalho `Ctrl+1` no modo revisão do Anki faz dois atos em um só: marca o card com **flag:1** (bandeira vermelha) **e** o **suspende** imediatamente. O card some da fila até o próximo `--bandeira`.

**Instalar:**
```
Copiar a pasta:
  flashcards/anki-addons/nebli_flag_suspender/

Para dentro de:
  Windows: %APPDATA%\Anki2\addons21\
  Linux/Mac: ~/.local/share/Anki2/addons21/

Reiniciar o Anki.
```

**Fluxo de uso:**
1. Durante a revisão, viu um card que quer entender a fundo → `Ctrl+1` (bandeira + suspende, avança para o próximo)
2. Quando quiser as explicações → pede no chat → Claude roda `python flashcards/scripts/monitor_email_anking.py --bandeira`
3. Email chega com 2 parágrafos por card + síntese de padrões frágeis
4. Script dessuspende automaticamente + remove a bandeira

Compatível com Anki 2.1.50+. O add-on usa `gui_hooks.main_window_did_init` para registrar o atalho de forma segura.

---

### Fluxo — Resumo de leeches (sem bandeira)

```
Davi pede: "manda o resumo de leeches"
  → python monitor_email_anking.py --semanal
  → top 10 cards com lapses>=3 nos blocos NEBLI::
  → explicação semanal com sugestão de reforço
```

---

### Custo e infraestrutura

| Item | Detalhe |
|---|---|
| **Remetente** | `dpbdes@gmail.com` via Gmail SMTP (`GMAIL_APP_PASSWORD`) |
| **Custo atual** | Gratuito — usa `claude -p` (Claude Code CLI, sem API direta) |
| **Custo futuro (API)** | ~$0.003/dia para 8 cards explicados com Sonnet 4.6 — ~$1/ano |
| **Anki** | Container Docker em localhost:8765 (AnkiConnect add-on) |
| **Sync** | Script faz sync antes de ler — puxa o que o celular subiu |

**Pré-requisitos para rodar:**
```bash
# Variáveis de ambiente (nunca no git)
ANTHROPIC_API_KEY=...      # se usar --cerebro api
GMAIL_APP_PASSWORD=...     # App Password do Gmail (16 chars)
```
Docker com Anki + AnkiConnect deve estar rodando.

---

## Pendências de cards

- **Sprint P4 (próximo):** curar as 6 aulas de bioquímica do P4 — `gerar_checklist.py` precisa ler E1+E2 (atualização pendente do script)
- **Rebuild NEBLIcards autorais existentes:** seguir `flashcards/AUDITORIA-NEBLICARDS-ANKING-2026-07-14.md`; prioridade: normalizar bioq-21/bioq-23, depois biomol-25, depois embrio.
- **Anatomia com cadáver:** usar `referencias-externas/DECKS-EXTERNOS-MAPA.md` + `copiar_externos_para_deck.py` para puxar BlueLink por tag (`BlueLink::Heart`, `BlueLink::SuperiorMediastinum`, etc.) para cópias no deck NEBLI; nunca depender só de cloze textual em anato macro.
- **Guia de externos obrigatório:** usar `referencias-externas/GUIA-CARDS-EXTERNOS-PARA-DECK-AULA.md` antes de autorar lacuna: AnKing → externos → autoral.
- **Imagens nos autorais já existentes:** 187/187 autorais/gerados no Anki estão com imagem reconhecida (`NEBLI::image_extra`); 186 ainda são imagem de contexto e precisam troca fina por imagem específica quando visualmente relevante.
- **Refino de imagens P3:** 187/187 autorais/gerados ja receberam imagem, mas 186 ainda precisam revisão fina (`NEBLI::image_context_needs_specific_review`) para trocar imagem de contexto por imagem específica do conceito.
- **Email de bandeira:** auditoria read-only de 2026-07-14 achou 26 vermelhos, 2 verdes e 0 comentários pendentes. O corte silencioso de 14 foi corrigido; envio agora é opt-in e falha de LLM/SMTP preserva bandeiras. Ainda falta smoke test SMTP/add-ons antes de produção. Ver `flashcards/PLANO-FEEDBACK-E-EMAIL.md`.
- **Add-ons NEBLI quebrados:** Davi relatou que os add-ons instalados não estão funcionando. Investigar perfil correto, restart do Anki, conflitos de atalho e compatibilidade dos hooks.
- **Reviewer reescondendo card antes da nota:** Davi relatou que, ao ficar lendo a explicação, o card parece voltar a esconder/revirar antes de dar nota 1-4. Auditar add-ons de auto-advance/speed focus/timer/reviewer e configurações do Anki.
- **ANATO-06 — 3 LACUNAs abertas:** anatomia venosa periférica, sistema ázigo, drenagem linfática torácica → buscar em deck Netter ou Anatomy in Clinical Context; documentar no manifesto
- **Loop card→E1 — primeiro piloto:** testar na próxima aula curada; documentar o que funcionou
- **`gerar_checklist.py` — adicionar leitura da E2:** extrair conceitos testados nas 30 questões e adicionar ao `.tsv` com origem `E2` *(já lê do Tema Card via `ler_subtopicos_card()` — pendente só a leitura de `etapa2.typ`)*
- **Cards NEBLI autorais (PENDENTE-GERADO):** só após calibrar padrão com cards reais do AnKing; não gerar ainda
- **Ctrl+1 quebrado no Anki do Davi:** o add-on `flashcards/anki-addons/nebli_flag_suspender/` não está funcionando. Contorno atual: Davi usa laranja+vermelha como equivalentes (ver § Bandeiras). Investigar por que o atalho não pega (versão do Anki? conflito de add-on? hook mudou?)
- **Add-on de tirar dúvida dentro do Anki:** pesquisar/avaliar um add-on que permita perguntar direto no Anki (LLM no card) — para o Davi resolver dúvida sem sair do estudo
- **Add-on dicionário de termos médicos (tipo AMBOSS, grátis):** pesquisar um add-on com dicionário/hover de termos médicos gratuito, para reduzir atrito no estudo
- **Pesquisa GitHub — repos de deck-aula/deck-mestre com IA:** vasculhar repositórios que ajudem o processo de criar decks de medicina com IA no Anki (geração, curadoria, image occlusion, AnkiConnect automation) — pode acelerar todo o pipeline
- **Puxar todos os cards para o deck-aula NEBLI espelhando o Drive:** organizar em pastas/subpastas como o Drive NEBLI (UC › componente › aula) para acesso fácil do Davi. Ver `flashcards/estrutura-deck-mestre.md` (Modelo B). Acesso do Claude ao Drive fica para mais adiante.
- **R7 — poda Step 2 no `prefiltrar_pool.py`:** adicionar blocklist de tags/decks Step 2 (`#AK_Step2_v12::` e afins) para remover do pool antes do keep/drop fino
- **R6 — rubrica de cobertura 0-3 na `verificar_cobertura_anking.py`:** trocar o X/Y de subtópicos tocados pela média da rubrica quali (0-3); relatório por subtópico com nota + nº cards + veredito (COBERTO/RASO/LACUNA)
- **Modelo B (deck-mestre FMUSP):** `aplicar_curadoria_anking.py` faz `changeDeck` p/ `NEBLI::UCxx::NN_Componente::PX-NN_slug` (deriva de `banco/aulas_ucNN.yml`); `reposicionar` ordena `due` por (índice-aula, índice-subtópico). Ver `flashcards/estrutura-deck-mestre.md`
- **Migração física para `flashcards/`:** `git mv` de scripts + flashcards/curadoria + addon; atualizar paths em scripts/skill `/resumo`/`CLAUDE.md`/agents; `--dry-run` antes de commitar. Passo único e testável (ver `flashcards/README.md`)
- **Cards NEBLI autorais das lacunas de processo (embrio):** EMT (1.2), dobramentos (3.2), membranas (3.3) — gerar de frases da E1 após calibrar padrão; gravar em `flashcards/cards-nebli/embrio-gastrulacao-neurulacao.json`

---

## Índice de aulas curadas

| Slug | Status | Dessuspendidos | Cobertura | Loop card→E1 | LACUNAs abertas |
|---|---|---|---|---|---|
| anato-06 | ✅ aplicado | 42 cards | 5/8 COBERTOS | pendente (pré-pipeline novo) | 3 (venosa periférica, ázigo, linfática torácica) |
