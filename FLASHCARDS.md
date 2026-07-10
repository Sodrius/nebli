# FLASHCARDS.md — Deck Anki NEBLI

> **Função:** documento vivo de filosofia, estado e processo do deck Anki do Davi. Ler antes de qualquer sessão de curadoria de cards, escolha de tags, ou resposta às bandeiras. Detalhes técnicos (scripts, comandos, schema) vivem em `flashcards/CURADORIA-ANKING.md`; este arquivo é o **porquê e o onde estamos**.

---

## Filosofia

**Guia duplo de conteúdo:** aulas FMUSP + Step 1 USMLE.

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

**R12 — Norte de profundidade + menos atrito (feedback 2026-07-10).** Davi sente que **E1, E2, E3 e os cards ainda estão rasos**. O objetivo declarado é: material **mais aprofundado e com menos atrito**, para ele reter a informação aprofundada no tempo que tem até a prova **e** para o Step 1. Toda geração daqui pra frente puxa a profundidade pra cima (dentro de R2/R10 — fundo, mas não maluco) e reduz atrito (prosa fluida, card atômico com explicação e imagem). Ver [[feedback-cards-e-resumos-mais-fundos]].

Detalhe operacional destas regras e a decisão deck-AnKing vs deck-NEBLI estruturado: `flashcards/estrutura-deck-mestre.md`. **Estamos em evolução ativa do processo de cards — muitas destas regras vão mudar conforme Davi pede curadoria a cada resumo novo.**

---

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

## Bandeiras

### Vermelha (flag:1) — "me explique este card"
Davi marca durante o estudo quando quer entender um card mais fundo. Claude redige **2 parágrafos em voz NEBLI** (causa→mecanismo→consequência):
- Parágrafo 1: o mecanismo do card (o que ele testa, por que é verdade)
- Parágrafo 2: contexto — por que importa, como se liga ao que o Davi estuda na aula daquele bloco `NEBLI::<slug>`

**Fluxo de suspensão (canônico 2026-07-09):** quando `--bandeira` é rodado, os cards flag:1 são **suspensos imediatamente** (saem da fila de revisão). Depois de gerar e enviar o email, a bandeira é removida e os cards são **dessuspensos** (voltam à fila). Assim o Davi lê a explicação antes de ver o card de novo.

**Modo auxiliar:** `python flashcards/scripts/monitor_email_anking.py --suspender-vermelhos` suspende os cards vermelhos na hora, sem enviar email. Útil quando o Davi marca durante o estudo e quer parquear imediatamente sem esperar a sessão com Claude.

### Laranja (flag:2) — EQUIVALENTE À VERMELHA (canônico 2026-07-10)

`Ctrl+1` parou de funcionar no Anki do Davi, então ele volta a usar bandeira laranja e trata **laranja = vermelha**: ambas significam "me explique este card + suspende". O `--bandeira` coleta flag:1 **e** flag:2 no mesmo fluxo (explica os 2 parágrafos, envia email, dessuspende, remove a flag).

**Sinal importante:** no geral, um card marcado (laranja/vermelha) é um card **que não foi explicado na E1**. Por isso, ao processar as bandeiras, Claude também reporta *quantos* dos marcados não têm âncora na E1 — muitos marcados = sinal de que aquela aula tem card demais sem explicação (violação de R1), e a E1 daquela aula precisa subir ou o deck precisa podar.

### Verde (flag:3) — "este é um bom card" (canônico 2026-07-10)

Davi marca verde quando um card é bom. Quando ele pedir "analisa as bandeiras que marquei", os **verdes viram exemplares**: Claude os adiciona a `flashcards/EXEMPLARES-CARDS.md` (forma + gesto). É o canal de calibração positiva — o deck aprende com o que o Davi aprovou.

### Ao analisar os laranjas/vermelhos — checar pertinência (canônico 2026-07-10)

Quando Claude for ver os cards marcados, além de explicar, **julga se cada um merecia estar ali**: era conteúdo daquela aula (ANCORADO/ANCORÁVEL) ou era card que nem deveria ter sido escolhido (FORA — próxima-aula/ruído)? Card FORA marcado vira drop + nota no anti-exemplar. Isso fecha o loop de qualidade do deck.

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

**Resultado no email:** 2 parágrafos por card em voz NEBLI:
- §1 — o que o card testa e por que é verdade (causa→mecanismo→consequência)
- §2 — contexto: por que importa, ligação com o bloco `NEBLI::<slug>` da aula

---

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
