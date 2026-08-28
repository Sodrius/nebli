# ROLES.md — papéis do pipeline NEBLI

**Função:** fusão dos 9 arquivos antigos em `.claude/agents/*.md` num catálogo único de papéis. Faxina canônica 2026-05-29.

**Princípio:** cada § contém **fluxo operacional, contrato I/O, prompts internos e proibições específicas** do papel. Regras genéricas do NEBLI (paridade, voz, pipeline, banco como calibração, Mapa de Confusões, figuras, footnotes) vivem em `CLAUDE.md` (núcleo prescritivo) ou `ERROS.md` (armadilhas + feedbacks). Onde há sobreposição, este arquivo cita com link em vez de copiar.

**Stubs em `.claude/agents/*.md`** preservam dispatchabilidade do `Task(subagent_type=...)` — cada stub é YAML frontmatter + 2 linhas apontando pra cá. Quando Davi disparar `Task(subagent_type="cadernista", ...)` o stub leva para § Cadernista abaixo.

**Routing canônico:**

| Papel | Executor | Modelo |
|---|---|---|
| Orquestrador + Redator-E1 + Questionador (fundidos) | Sessão principal | Opus 4.7 |
| Compilador | Sessão principal (local, nunca delegado) | — |
| Cadernista | Task subagent | Sonnet 4.6 |
| Flashcards | Sessão principal sob `/flashcards` | Opus 4.7 |
| Revisor-didático (Tier 2) | Task subagent | Sonnet 4.6 |
| Revisor-profundo (Tier 3) | Task subagent | Opus 4.7 |
| Revisor-PDF-didático | Task subagent | Sonnet 4.6 |
| Revisor-PDF-profundo | Task subagent | Opus 4.7 |

REDATOR-E1 e QUESTIONADOR como Task subagent foram suspensos em 2026-05-26 (ver `ERROS.md` § Erro 3 e F9). Permanecem aqui como **referência prescritiva** que a sessão principal lê e segue.

**Deck-aula completo no `/resumo` (CANON 2026-08-03):** toda corrida fecha o deck-aula completo e já no Anki, das 3 fontes (AnKing curado → decks externos → NEBLIcards autorais para lacuna tipo-a), com `card-mirror` rodando sempre (por ora) e gate hard de completude nuclear. Papel operacional em `.claude/commands/resumo.md` passo 11; o **Revisor-completude** (§ abaixo) audita a completude mútua E1↔cards que esse fechamento exige.

---

## § Orquestrador

Coordena a geração de um resumo NEBLI ponta a ponta. Hoje fundido com Redator-E1 e Questionador na sessão principal.

### Leitura obrigatória antes de qualquer Tema Card

1. `CLAUDE.md` (auto-carrega) — núcleo prescritivo.
2. `MEMORY.md` (auto-carrega) — estado vivo, **§ Diário de revisões obrigatório** para extrair lista de prioridades pra esta corrida.
3. `ERROS.md` — checklist técnico + feedbacks de processo.
4. `guia_editorial_UC1.csv` — profundidade esperada para o tema.
5. `banco/indice/banco_slim.json` filtrado por `aula: <slug>` — calibração (nível, jargão, armadilha).
6. `banco/aulas_uc01.yml` (41 aulas) e `banco/aulas_uc02.yml` (31 aulas) — slugs oficiais.
7. `figuras/[tema]/MAPA_CONTEUDO.txt` — existe após rodar `extrair_slides.py`.

### Fluxo canônico

0. **Limpar `typst-build/`** — mover etapas do resumo anterior para `arquivos-trabalho/etapas-anteriores/<slug-anterior>/`. Anti-contaminação de tema.
   ```bash
   SLUG_ANTERIOR=$(grep -oP '(?<=// MAIN.TYP -- )\S+' typst-build/main.typ 2>/dev/null || echo "desconhecido")
   mkdir -p arquivos-trabalho/etapas-anteriores/$SLUG_ANTERIOR
   mv typst-build/etapa{1,2,3}.typ typst-build/resumindo.typ typst-build/main.typ \
      arquivos-trabalho/etapas-anteriores/$SLUG_ANTERIOR/ 2>/dev/null || true
   ```
1. Identificar slug em `aulas_uc01.yml`/`uc02.yml`. Em ambiguidade, perguntar com opções numeradas.
2. `python3 typst-build/extrair_slides.py [slide.pdf] [slug]` → PNGs + `MAPA_CONTEUDO.txt`.
3. `python3 banco/extrair_armadilhas.py <slug>` → `arquivos-trabalho/armadilhas/<slug>.json`. Alimenta Seção D.
4. Ler `guia_editorial_UC1.csv` → profundidade (SUPERFICIAL/PADRÃO/PROFUNDO).
5. **Aplicar Diário de revisões.** Antes de gerar Tema Card, ler `MEMORY.md` § Diário de revisões. Entradas com peso alto e ainda no prazo de decaimento viram **lista de prioridades pra esta corrida**, declarada explicitamente no Tema Card.
6. Gerar Tema Card (Seções A, B, B.bis, B.ter, C, D, E). Validar com Davi antes de redigir.
7. Após aprovação: redigir E1 + Resumindo (papel Redator-E1) → E2 + E3 (papel Questionador) → COMPILADOR.

### Tema Card — estrutura obrigatória

- **Seção A** — Tema · Slug · Disciplina · Onde estudar · **Onde aprofundar (plataformas)** · Alvo de páginas E1 (piso 2, **teto 22**) · Recorte slide×tema · **Prioridades desta corrida** (do Diário de revisões).
  - **Onde aprofundar (plataformas)** (canônico 2026-06-30): bloco da capa em **2 grupos**, cada item um bullet navy. (1) **Assistir/ler** — 1 bullet com fontes de vídeo/leitura (B&B/Bootcamp, NinjaNerd, Sketchy, UWorld, Pathoma); recurso que não cobre → "não cobre" (honestidade > referência falsa). (2) **Dessuspender no AnKing v12** — 1 bullet de cabeçalho + **1 bullet por deck**, mostrando o **caminho de tag pra usar no `Browse`** (não o nome amigável) + contagem de cards, com **variedade de decks** (o conteúdo está taggeado em paralelo por vários recursos). Preencher rodando `python flashcards/scripts/buscar_tags_anking.py <termo>`; consultar/gravar em `referencias-externas/onde-aprofundar.md`. Vai pro `meta` da capa como **valor em lista** (o `gerar_main.py` renderiza bullets navy via `_esc_typst_content`, que escapa `#`/`_` das tags e preserva `*` do negrito). Exceção escopada à regra de banimento Step 1: nomes de plataforma/deck só neste bloco.
- **Seção B** — Esqueleto das 3 PARTES com subtópicos. 3 figuras planejadas por PARTE com fonte (slide-XX ou SVG novo). Cadeia multi-passo ≥5 reações = figura obrigatória.
- **Seção B.bis** — Registro de abertura por subtópico. Os 5 registros: (1) enquadramento, (2) integração-anterior, (3) integração-posterior, (4) analogia concreta, (5) ponto-de-quebra. Nenhum par vizinho compartilha registro. **Pergunta âncora/retórica banida** (canônico 2026-05-29) — substituída pelos 5 registros acima.
- **Seção B.ter** — Pré-requisitos cruzados com frase-âncora pronta. Mínimo 3 por Tema Card. Tabela: pré-requisito | frase pronta ≤25 palavras. REDATOR cola na 1ª aparição.
- **Seção C** — Distribuição da E2 baseada na profundidade do guia:
  - SUPERFICIAL: 12–13 Cons · 12–13 Int · 5 Apl
  - PADRÃO: 10 Cons · 15 Int · 5 Apl
  - PROFUNDO: 8 Cons · 17 Int · 5 Apl
  Gerar sequência completa dos 30 gabaritos por sorteio independente. **NUNCA balancear letras** — pode ter 3 A's seguidas, EEEE, CCCC.
- **Seção D — Pontos de quebra do raciocínio** (4–8 itens). Voz de mecanismo, JAMAIS voz de prova. Formato:
  ```
  - Quebra: <substantivo + verbo mecanístico>
    Correção: <caminho certo, 1–2 linhas>
    (origem interna: q-XXXX)
  ```
  Vocabulário banido em qualquer lugar: "prova", "questão", "banca", "pegadinha", "cai", "caiu", "gabarito", "examinador", "enunciado", "P1/P2/P3", "FMUSP", "vestibular", "ENARE", "USMLE", "residência", "simulado".
- **Seção E — Exemplares-âncora.** Antes do Tema Card, passada no índice `## Quando usar` de `EXEMPLARES.md`. Escolher exemplares que vão guiar voz e prosa do tema. Anotar em 1–2 linhas o gesto entendido + onde aplicar. Sem teto, sem piso.

### Bloco `gabarito:` obrigatório no Tema Card inicial

YAML do Tema Card sai com bloco `gabarito:` preenchido com as 30 letras/strings sorteadas. Concatenar com `cat >>` depois é proibido (já causou YAML quebrado em 2026-05-22). Estrutura:
```yaml
gabarito:
  consolidacao:
    - ["01", "B"]
    # 10 entradas
  integracao:
    - ["11", "C"]
    # 15 entradas
  aplicacao:
    - ["26", "D"]
    # 5 entradas
```

### Pedido avulso "questões antigas de X"

Filtrar `banco_slim.json` por `aula: <slug>` → `arquivos-trabalho/questoes-de-prova/<slug>.md`. Se ≤5, imprimir no chat. **Nunca colar no PDF do resumo.**

### Proibições

- Nunca mencionar bloco/prova (P1/P2/P3), número/posição de aula, slug, turma, semestre no PDF.
- Perguntas ao usuário sempre com opções numeradas, nunca texto livre.
- Strings YAML do Tema Card sempre acentuadas — `gerar_main.py` preserva Unicode entre aspas duplas.

---

## § Redator-E1

Gera `etapa1.typ` (intro-box + 3 PARTES + conclusão integradora **obrigatória** — ver diretriz 11), `resumindo.typ` e `pre-aula.typ` (ver diretriz 18). Não gera capa, sumário, etapa-headers, nem qualquer seção fora desse escopo.

### Diretrizes 1–9 (piso técnico — imperativo)

**1. Prosa expositiva precede tudo.** Voz de monitor explicando ao vivo — prosa contínua, não diálogo simulado nem cadeia pergunta-resposta. Ferramenta pedagógica, não monitor real (sem confidências, sem auto-referência, sem familiaridade falsa). **Sem pergunta âncora / pergunta retórica / pergunta ingênua como recurso de abertura** (canônico 2026-05-29 — substitui o antigo teto de 3 perguntas). Abertura de subtópico é afirmação direta + mecanismo. Auto-check antes de fechar: `grep -cE '\?$' typst-build/etapa1.typ` — perguntas terminais devem ser raríssimas; se passar de ~3, reduzir.

Negrito didático tem cota: máx 2–3 por parágrafo, marcando o conceito que o aluno leva embora. Mini-resumo varia fórmula: "Em uma frase:", "Se você só lembrar de uma coisa:", "O que ficou de pé:" — nunca o mesmo dois seguidos.

**Nome de subtópico é descritivo e direto (item 35, 2026-06-24):** diz exatamente o que aquele trecho ensina. Metáfora no título só quando ela *informa* o conteúdo ("Tendões: a corda inextensível que entrega a força ao osso" passa porque diz o que o tendão faz); título só-poético que não revela o conteúdo, não. Em dúvida, prefira o claro ao bonito.

**2. Tamanho.** Piso 2, teto 22 páginas. Subtópico ~400 palavras. Completude > teto.

**3. Jargão controlado.** Termo técnico = etiqueta para conceito já entendido. "Ligação temporária entre o açúcar e a enzima (chamada thiohemiacetal)" — não "intermediário thiohemiacetal". Abrir cada conceito pelo mecanismo plausível, dar nome técnico DEPOIS, retomar pré-requisitos em 1–2 frases. Aprofundamento por camadas: porquê cru → nuance → exceção → clínica.

**4. Mini-resumos.** Em parágrafos >5 linhas, inserir `#mini-resumo[X causa Y → consequência Z]` no meio. Sem piadas, sem mnemônicos forçados.

**5. Resumindo junto (revisto 2026-06-24 — item 36).** Entregar `resumindo.typ` junto da E1. **Menos ideias, mais palavras por ideia, mais encadeamento.** 6–10 seções (era 8–12), cada uma ~30–45 palavras de frase encadeada causa→consequência — não fragmento nem aglomerado de sigla. É mapa de revisão rápida pra quando o aluno não lembra: só o que importa de verdade, ordenado por relevância clínica decrescente. Modelo: o "RESUMO" de fim de capítulo do Mankiw (cada item é frase inteira, sujeito+verbo+complemento) e o "Resumindo" numerado do Poliedro (título curto + 2-4 linhas de mini-prosa). Pode ocupar 1 ou 2 páginas. Assinatura: `#resumindo-page(((titulo, corpo), (titulo, corpo), ...))` — tupla dupla por seção.

**6. Resumos independentes.** Nunca referenciar outro resumo. Cross-reference só entre subtópicos do MESMO resumo. Conceito de outro resumo é pré-requisito → explicar em-linha em 1–2 frases.

**7. Figuras.** Largura 40–80% caso a caso (`CLAUDE.md` § Figuras detalha as faixas). Texto curto + figura pequena: `#figura-lateral`. Caminho com prefixo `/`. Meta mínima 3 imagens por PARTE (heurística). Prioridade: imagem do slide do professor. **Relatório auditável obrigatório no fechamento** (tabela: Figura | PARTE | Origem | Mecanismo | Largura — ver `ERROS.md` F5).

**8. Footnotes e siglas.** Sigla na 1ª aparição: `#sigla("ATP", [adenosina trifosfato — moeda energética])`. Termo técnico denso na 1ª aparição: `#termo-nota[acetilcolina][principal neurotransmissor da JNM]`. 6–10 termo-notas por resumo (não parar em 3-4).

**9. Cadeia multi-passo enzimática = figura obrigatória.** ≥5 reações encadeadas → figura, não parágrafo enfileirado.

### Diretrizes 10–15 (voz e julgamento — convite, não gate)

**10. Rotação de registros entre subtópicos vizinhos** — pelos 5 registros da Seção B.bis. Nenhum par vizinho compartilha. Sugestão forte, não gate.

**11. Conclusão integradora — OBRIGATÓRIA em toda E1 (canônico 2026-07-03 — reverte a opcionalidade de 2026-06-24/07-01, a pedido de Davi).** Toda E1 fecha no `#conclusao-box` antes do `#resumindo-page`, costurando as 3 PARTES em 4 camadas explícitas: princípio unificador → mecanismo nuclear → clínica retomada (com mecanismo, não só nome) → projeção para o próximo resumo. É gate hard do `precompile-check.py` (`>=1 #conclusao-box`). Não é redundante com o Resumindo: a conclusão argumenta e amarra em prosa; o Resumindo enumera cápsulas para revisão rápida.

**12. Clínica inline entre travessões + box só quando densa.** Inline quando caso é colateral (1-2 frases): "—a anemia falciforme nasce de uma única troca de glutamato por valina—". `#clinica-box` quando cadeia exige 4-6 linhas. Meta: ≥3 clínicas inline + 2-3 box por PARTE.

**12.5. `#confusao-prevista()` para inversões nomeáveis sem consequência letal.** Visual gold mais leve que `atencao-box` (vermelho).

**13. Default é prosa; box é exceção.** Cota máxima 1-2 `atencao-box` somados com `confusao-prevista` por PARTE. Ver `ERROS.md` F3.

**14. Paridade de densidade entre PARTES.** ~500-700 palavras por conceito novo. Desvio entre PARTES ≤ ±20%. Última 50-100 palavras de uma PARTE devem antecipar mecanisticamente a próxima.

**15. Filtro de utilidade pedagógica para figuras.** Antes de referenciar, 3 testes: (a) mecanismo não-óbvio do texto? (b) cadeia ≥5 passos? (c) autoridade do professor (slide oficial)? Documentar curadoria — figuras descartadas reportadas no fechamento.

**16. Calibração externa invisível — `blueprint-step1.md` (convite, 2026-06-30).** Antes de redigir a E1 de um slug, olhe a linha dele em `referencias-externas/blueprint-step1.md`. Se a coluna "Aprofundar na E1" tiver conteúdo E o slide já abriu aquele assunto, acrescente **1-2 frases sucintas de mecanismo** no ponto indicado — diluídas na prosa, não um bloco novo. Se a coluna marca **BAIXO** (ou está vazia), não force nada: mantém foco puro no slide. A fonte é invisível como o banco — a frase entra como mecanismo/cenário clínico puro, jamais citando "Step 1/residência/USMLE" (vocabulário banido, regra 10 detalhada). Convite, não cota: aprofundar só onde flui.

**17. Passe de aprofundamento por subtópico (loop card→E1→E2, CANON 2026-07-10).** Antes das injeções, fazer um passe leve **Fontes→E1**: comparar Tema Card/slide, banco FMUSP já filtrado e blueprint já consultado com a E1; listar ausências relevantes e incorporar somente as que pertencem ao recorte. Não criar ledger novo. Depois do rascunho da E1 e da seleção de cards (ver `FLASHCARDS.md` § Loop Card→E1), fazer um passe voltando na E1 e injetando **≈1 conteúdo extra mecanístico por subtópico** — pequeno (1-3 frases), colado a um mecanismo que o subtópico já abriu. Dá ~9-12 por resumo; a soma faz a E1 ir **um tiquinho além do slide** (o norte do Davi: aprofundar bem a base durável). Fontes do que injetar, em ordem: (a) **bons cards do AnKing** que cobrem o conceito com mais profundidade — muitos aprofundamentos são *induzidos* por esses cards, que vão para o deck-aula; (b) mapa de cobertura offline do export quando o Anki está fora; (c) `blueprint-step1.md`; (d) bibliografia do curso em `_material/` (leitura dirigida das páginas do ponto). **Regra-mestra:** o **slide regula O QUE entra** (escopo — nada fora do tema da aula), o **AnKing/bibliografia regula ATÉ QUE PROFUNDIDADE**. Se um subtópico não tem onde encaixar, não injeta. Cada injeção é prosa/mecanismo puro (vocabulário Step 1 banido no PDF). **Efeito colateral desejado:** o aprofundamento sobe também o teto da E2 — por isso o ideal é rodar este passe ANTES de redigir a E2 (E2 já cobra o extra); se a E2 já estiver escrita, atualizá-la nos pontos aprofundados revalidando paridade/gabarito. Exemplos concretos no piloto embrio-gastrulacao-neurulacao (SHH, EMT→metástase, cílios do nó→lateralidade, crista→Hirschsprung, somito→esclerótomo/miótomo/dermátomo, dobramento→frênico).

**18. "Antes da aula" — `pre-aula.typ` (CANON 2026-08-28).** Toda E1 fechada gera também a seção de abertura do PDF, que vive entre a capa e o sumário. **2 páginas de prosa contínua na voz NEBLI contando a história da aula**, 900–1100 palavras, **sem figura**, encerrando em uma linha do tipo "chegue com esse mapa na cabeça". Não é sumário executivo nem mini-E1: é a narrativa do que a aula vai fazer e em que ordem, para o aluno ler na véspera.

Os **principais termos** que o professor vai usar como se o aluno já soubesse entram em negrito dentro da prosa, cada um seguido da frase curta que o define. Nesta seção o negrito marca o termo sendo plantado, então a cota de 2–3 negritos por parágrafo da diretriz 1 **não se aplica** — 4–5 é normal.

Escrever **depois** da E1 (o pré-aula é destilado dela, inclusive dos aprofundamentos da diretriz 17) e **antes** de compilar. Gravação: `#pre-aula-page[ ... ]` em `typst-build/pre-aula.typ`, com o `#import` do template no topo como qualquer etapa. `gerar_main.py` inclui sozinho quando o arquivo existe.

**É gate hard desde 2026-08-29** (`check_pre_aula` no `precompile-check.py`): sem `pre-aula.typ` o precompile falha e não se compila. O que bloqueia: menos de 800 ou mais de 1300 palavras; bullet ou lista; figura; helper de E1 dentro da seção; qualquer interrogação; menos de 15 termos em negrito. O que apenas avisa: palavras fora de 900–1100 e negritos entre 15 e 24. Escape `--legado` só para regerar resumo histórico anterior à canonização.

### Índice de completude (CANON 2026-07-10) — 3 notas no relatório de fechamento

Junto do ratio Q01-Q30, da tabela de figuras e da tabela subtópico→questões, entregar **3 notas de 0 a 10 com 1 linha de justificativa** (auditável, não gate hard — convite):

1. **E1 × slide** — a E1 cobre tudo o que o slide traz E vai um tiquinho além (aprofundamentos colados)? Régua: 0-4 falta conteúdo do slide · 5-7 cobre o slide fielmente · 8-9 cobre tudo + aprofundamentos bem integrados · 10 raro (aprofundamento exemplar sem perder foco). **Meta 8-9.** Nota <8 por falta de cobertura do slide → volta pra prancheta.
2. **E2 × E1** — cada subtópico da E1 (incl. aprofundamentos) é cobrado? Resume num número a tabela subtópico→questões. **Meta ≥8.**
3. **Cards × E1** — os cards selecionados/curados cobrem os subtópicos da E1? Resume o X/Y COBERTOS num 0-10. **Meta ≥7** (lacunas apontam fonte). Além das notas, fechar com: **Fontes → E1: X/Y conceitos relevantes incorporados** e **E1 → cards: X/Y conceitos nucleares COBERTOS**.

O objetivo do eixo 1 é explícito: recompensar a E1 que **passa um pouco do slide**, sem virar toca de coelho. As notas orientam; a justificativa de 1 linha por eixo é o que carrega valor.

### Banco de provas é calibração invisível (regra 10 detalhada)

O resumo é leitura autônoma — leitor nunca sabe que existe banco. Seção D do Tema Card chega como insumo para distribuir `#atencao-box`. Redigir boxes pelo **mecanismo do erro**, jamais pelo rótulo de prova. Vocabulário banido (mesmo da Seção D): "prova/questão/banca/pegadinha/cai/gabarito/examinador/enunciado/P1-P3/FMUSP/vestibular/ENARE/USMLE/residência".

`#atencao-box` tem 2 movimentos no mesmo parágrafo: (a) quebra; (b) correção. Cota máxima 1-2 boxes por PARTE.

### Escrita matemática (revisto 2026-06-24 — itens 1, 18)

Matemática **nunca é parede de símbolos** (anti-padrão A1 em `ANTI-EXEMPLARES.md`). Modelo Mankiw (incidência tributária, etapas rotuladas):
1. **Montar em prosa** o que a conta representa, antes de qualquer símbolo.
2. **Etapas rotuladas** — cada passo num parágrafo curto que diz o que se faz E por quê ("Primeira etapa: …").
3. **Reler o número final em palavras** ("isso significa que metade do ATP…").
4. **Ancorar numa figura/legenda** que narra o mecanismo, quando há gráfico.

Frações conceitualmente importantes (Keq, P/F, V/Q, proporções estequiométricas) usam display math em bloco:
```
$ K_eq = ([C][D]) / ([A][B]) $
```
Razões numéricas triviais ("2/3 dos pacientes", "1/2 ATP por ciclo") ficam inline em texto normal.

### Gravação

Heredoc para `.typ` pequenos (etapa3, resumindo), Write tool para `.typ` grandes (Windows ENAMETOOLONG — ver `ERROS.md` erro 4). Edit válido para mudanças pontuais.

### Proibições absolutas

- Sem bullets no corpo (exceto 3 casos: comparativos 3+ dimensões, cronologias numéricas, critérios diagnósticos discretos).
- Sem mnemônicos forçados, sem perguntas artificiais ao leitor, sem referências a outros resumos.
- Sem mapas mentais SVG (`#mapa-parte` suspenso 2026-05-19) nem mindmap de fechamento (`#mindmap-fechamento` suspenso 2026-05-28).
- **NUNCA** escrever `#etapa-header(...)` ou `#set-etapa(...)` em `etapa1.typ`/`resumindo.typ` — duplica `pagebreak(weak: true)` e gera página em branco. Auto-fix em `auto_fix_etapas.py`, mas a regra é não incluir.

---

## § Questionador

Gera `etapa2.typ` e `etapa3.typ`. NÃO gera etapa-headers, capa, sumário, nem `etapa4.typ` (E4 removida 2026-05-22).

### Taxonomia E2 parametrizada

Distribuição da Seção C do Tema Card:
- SUPERFICIAL: 12–13 Cons · 12–13 Int · 5 Apl
- PADRÃO: 10 Cons · 15 Int · 5 Apl
- PROFUNDO: 8 Cons · 17 Int · 5 Apl

**Critério de Integração:** questão precisa cruzar ≥2 subtópicos no mecanismo de resolução. Se resolve com 1 subtópico, é Consolidação mesmo que enunciado seja longo.

**Cada categoria tem que fazer o que o nome diz (item 16, 2026-06-24):** Consolidação *consolida* (fixa um mecanismo, de preferência pelo ângulo "Por que/Como" — ver subseção abaixo); Integração *integra* (cruza dois domínios e exige raciocínio, não recall longo); Aplicação *aplica* (cenário clínico onde o conceito vira decisão). Questão que não cumpre o verbo da própria categoria está na categoria errada.

### Formatos de item (revisto 2026-06-24 — itens 6, 9, 10)

Três formatos convivem nas 30 objetivas:

- **Múltipla escolha (MC)** — formato base, 5 alternativas, banda dupla de paridade.
- **Certo/Errado (C/E)** — reintroduzido como **~1/3 das 30 (≈10 itens)**, distribuídos pelas três categorias (não só Consolidação). **Cada C/E tem SEMPRE exatamente 4 assertivas (I-IV) — gate hard do `precompile-check.py` (`check_ce_quatro_itens`), CANON 2026-07-01.** O gabarito é a sequência C/E de 4 letras. Vale a guarda anti-degeneração do § Gabarito sorteado (sem blocos longos só-C/só-E, sem CECECE — atenção: com 4 itens, evitar CECE puro e CCCC/EEEE). Paridade de comprimento **não** se aplica a C/E. Helper `#prova-ce(...)`.
- **"Assinale a incorreta"** — liberado como variante de MC quando o tema tem 4 verdades sólidas + 1 erro mecanístico fino. **Sinalizar `*incorreta*` em destaque no stem** para o aluno não ler rápido demais. Parcimônia: 2-4 das 30, não vira default.

C/E e "assinale a incorreta" sobem o teto de raciocínio sem inflar texto — boa moeda para Consolidação ativa e Integração.

**Cobertura da E1 na E2 (CANON 2026-07-01):** cada subtópico da E1 deve ser testado por **≥2 questões** da E2. Contagem no nível da questão; um item de C/E conta para o subtópico que cobre. Não há gate por regex (o mapeamento é semântico) — é diretriz auditável: no relatório de fechamento, a sessão principal entrega uma **tabela subtópico → questões que o cobrem**. Se algum subtópico ficar com <2, redistribuir/adicionar antes de fechar. Truque prático: os 4º itens de C/E são ótimos para reforçar o subtópico mais fraco sem inflar o total de questões.

**Questões de cálculo (item 18):** quando o conteúdo pede matemática (cinética enzimática, equilíbrio, estequiometria, gradientes), incluir **1-3 itens cujo mecanismo de resolução É a conta**. Distratoras = erros de cálculo plausíveis (trocou numerador/denominador, esqueceu um fator, unidade errada), nunca números aleatórios. Gabarito continua **só a letra** — sem resolução inline na questão (feedback E2 clássico). O passo-a-passo bem explicado (modelo Mankiw) vale para a E1 e para o modelo de resposta da E3, não para o corpo da E2.

### Filtro de admissão para Integração (canônico 2026-05-28)

**Gate operacional único.** Antes de redigir cada Q11-Q25, gravar em `arquivos-trabalho/integracao-mapa-<slug>.md` uma linha por questão:
```
Q11 conecta [A] + [B]
...
Q25 conecta [A] + [B]
```
Dois domínios distintos. Se não preenche o `+`, volta para Consolidação. Mapa **gravado ANTES da redação**.

### Inspirações e sugestões (bússolas, não trilhos)

**Tipos de cruzamento que funcionam:**
- Duas vias bioquímicas (Krebs × cadeia respiratória; extrínseca × intrínseca da apoptose).
- Mecanismo × técnica de bancada (PS exposta × citometria anexina V).
- Mecanismo × fenótipo experimental (knockout × resposta a droga).
- Mecanismo × tema de outra aula (apoptose × desenvolvimento neural).
- Mecanismo × farmacologia clínica (BH3-mimético × LLC).
- Mecanismo × imunologia/microbiologia (fagocitose silenciosa × IL-10/TGF-β).

**Cruzamento com outras aulas:** alavanca poderosa quando **compatível em tema E nível de complexidade**. Não cruzar câncer complexo com bioquímica básica avançada — aluno não consegue.

**Padrões de stem que abrem bem uma Integração:**
- Experimental: "Em camundongo com deleção de X, esperar-se-ia que..."
- Desenvolvimento/fenótipo: "Durante o desenvolvimento de X..."
- Cross-talk: "Em células tipo II, a sequência que liga X a Y é..."
- Comparativo: "Comparando X e Y, a diferença mecanística é..."
- Técnica clínica: "Em biópsia de..." / "Em citometria..." / "Em gasometria..."
- Cenário fisiológico: "Durante contração muscular intensa..."

Stems que puxam Consolidação (evitar com badge `integracao`): "Sobre [proteína X], é correto afirmar:" / "Qual / quantas / em qual?".

**Mapa de Confusões como semente:** confusões "duo-conceito" (necroptose × piroptose; anaplerótico × catabólico) são sementes naturais — pede ao aluno separar mecanismos vizinhos.

### Consolidação — subir um pouco a densidade cognitiva (2026-05-28)

**Sugestão de ângulo (não cota):** ao redigir cada Consolidação, testar reformulação com "Por que / Como / O que explica" e ver se mantém o mesmo fato testado com mais densidade. Mesmo conteúdo, ângulo que exige raciocínio mínimo em vez de busca em lista.

Exemplos:

| Antes (recall) | Depois (consolidação ativa) |
|---|---|
| "Qual enzima do ciclo gera FADH₂?" | "Por que a succinato DH é a única do ciclo a gerar FADH₂?" |
| "Em qual compartimento ocorrem as 8 reações?" | "Por que as 8 reações precisam ocorrer na matriz mitocondrial?" |
| "Quantos CO₂ por volta?" | "De quais carbonos vêm os 2 CO₂ liberados na primeira volta?" |
| "DISC é formado por quais componentes?" | "Por que o DISC precisa de adaptador (FADD) entre receptor e pró-caspase-8?" |

**Sugestão paralela para CE de Consolidação:** quando o tema permitir, incluir item C/E com pegadinha mecanística fina (item soa correto mas inverte sutileza).

### Aplicação (Q26–Q30)

Raciocínio clínico raso (1º semestre). Texto motivador carrega o peso quando clínica subir.

- **Q26–Q28:** cenário curto (1–3 linhas), USMLE-style.
- **Q29–Q30:** cenário clínico USMLE/Enare integrador (3–6 linhas).

**Anti-checklist do motivador:** (1) resposta literal aparece no motivador? reescrever; (2) aluno resolve sem ler? cortar; (3) >4 linhas? enxugar; (4) ensina conceito fora do resumo? cortar.

### Mapa de Confusões e paridade

**Mapa obrigatório.** Antes de redigir qualquer objetiva: ≥4 erros mecanísticos típicos por subtópico em `mapa-confusoes/<slug>.md`. Nome curto + descrição mecanística + origem.

**Paridade banda dupla 0.80-1.25 — gate hard Q01-Q30.** Ver `CLAUDE.md` § Rules globais + `ERROS.md` erro 1. Remediação direcional, ordem invertida de redação:

(a) Nível, categoria, formato.
(b) 3 confusões do Mapa → distratora-âncora + 2 secundárias.
(c) 4ª distratora como variante da âncora.
(d) **Redigir as 5 distratoras PRIMEIRO**, 25-35 palavras cada com mecanismo plausível-mas-errado.
(e) Sortear sinal (correta acima ou abaixo da média).
(f) **Só DEPOIS escrever a CORRETA**, parametrizada para entrar na banda 0.80-1.25 × maior distratora.
(g) Calcular ratio. Se fora da banda, refazer ANTES da próxima.

**Distratoras com peça roubada da correta (canônico 2026-07-09):** uma distratora pode pegar um componente real da correta e colocá-lo no papel errado — mesma enzima, cofator trocado; mesmo sinal, estrutura invertida; mesmo mecanismo, direção errada. Ex: se a correta é "enzima X inibida por Y aumenta Z", uma distratora é "enzima X ativada por Y aumenta Z" (inverte o sinal). O aluno não consegue reconhecer por padrão — precisa saber o mecanismo real. Aplicar em ≥1 distratora por questão de Consolidação/Integração onde o tema permitir.

**Distratoras que cruzam subtópicos (canônico 2026-07-09):** nas questões de Integração e Consolidação ativa, distratoras podem remeter a outro subtópico da mesma aula — misturando os conceitos de propósito. Isso força o aluno a distinguir os mecanismos entre subtópicos, não só dentro de um. Ex: em questão sobre regulação da via X, uma distratora traz o produto intermediário da via Y (que a E1 ensinou). Métrica informal: cada subtópico da E1 deveria aparecer como tema de gabarito ou de distratora em vários momentos ao longo da E2 — não só nas 2 questões que o testam diretamente.

**Relatório obrigatório no chat antes de fechar E2:** Q01–Q30, formato compacto ou em 3 blocos:
```
Q01 — correta=N₀ palavras, distratoras=[N₁,N₂,N₃,N₄], maior=Nmax, ratio=X.XX → PASS/FAIL (curta|longa)
```

### Etapa 3 — discursivas

5 questões, uma resposta-modelo por questão, um ponto mecanístico. ≤100 palavras (Q5 ≤130). Banir conectores enciclopédicos.

### Banco como calibração

Filtrar `banco/indice/banco_slim.json` por `aula: <slug>`. Ler `tags`, `conceito_central`, `armadilha`, `nivel`. Ajustar nível esperado, capturar vocabulário, alimentar Mapa de Confusões. **Nada vai pro PDF** — régua interna.

**Segunda régua — `referencias-externas/blueprint-step1.md` (convite, 2026-06-30).** Olhe a linha do slug. A coluna "Ângulo E2/E3" sugere o cenário de Aplicação calibrado (ou o texto motivador de uma Integração); a coluna "Gancho clínico BR" alimenta o Mapa de Confusões e o stem de Aplicação. **Não é cota** — no máximo 1 questão de Aplicação por resumo costuma usar o ângulo, e só quando ele realmente cruza com o conteúdo do slide. Coluna BAIXO/vazia = sem ângulo externo, a Aplicação nasce do próprio tema. Fonte invisível: o stem é cenário clínico puro, sem "Step 1/residência/USMLE" (vocabulário banido).

### Gabarito sorteado de verdade (revisto 2026-06-24 — itens 5, 9, 17)

O critério primário continua sendo o conteúdo: a correta é a correta. Mas "deixar o conteúdo decidir" sem conferir produz os sintomas que Davi sinalizou — gabarito que *parece não sorteado* (5), C/E *viciado* (9), *padrão repetido* (17). Sorteio real + guarda anti-degeneração:

- **Sortear o sinal de cada questão de verdade** — qual posição A-E recebe a correta, qual assertiva C/E é C ou E. Não cair no default cômodo de empilhar quase tudo numa letra.
- **Guarda anti-degeneração (não é balanceamento forçado):** nenhuma letra A-E passa de ~40% do total; nenhuma corrida de 4+ iguais consecutivas na ordem das questões; em C/E, sem blocos longos só-C/só-E e sem pingue-pongue mecânico CECECE. 3 iguais seguidas ainda é aceitável; 4 já reorganiza.
- **A guarda age REPOSICIONANDO a correta entre as alternativas** (que são intercambiáveis de posição), **nunca mudando qual é a correta** nem inventando resposta para caber numa letra-alvo — isso seria o "balancear" proibido.
- O **revisor-gabarito (Haiku)** confere na passada final (ver § Revisor-gabarito): impresso == correta real, sem corrida ≥4, distribuição não-degenerada.

### Cores

E2 por categoria: `#prova-consolidacao` verde, `#prova-integracao` azul, `#prova-aplicacao` violeta.

### Proibições

- Sem `#etapa-header(...)` ou `#set-etapa(...)` em `etapa2.typ`/`etapa3.typ` — `main.typ` já chama.
- Sem `etapa4.typ` (E4 removida).
- Sem tentativa de balancear letras ou C/E.
- Sem `--no-paridade` como atalho — último recurso documentado.
- Sem **engenharia da resposta para caber numa letra-alvo** (escolher a correta pela posição). Reposicionar a correta entre alternativas equivalentes para quebrar degeneração é permitido e desejável (ver § Gabarito sorteado de verdade).

---

## § Revisor-gabarito (Haiku — NOVO 2026-06-24)

Passada final de conferência do gabarito da E2, sugerida por Davi (item 8). Stub em `.claude/agents/revisor-gabarito.md` (Haiku 4.5). Roda depois de `etapa2.typ` fechado, junto/antes do `precompile-check.py`.

Três checagens:
1. **Impresso == correta real** (BLOQUEIA) — gabarito da página bate com a verdade de cada questão. Foi esse erro que marcou letra errada em 43% do UC01-BC-07.
2. **Sem corrida degenerada** — MC sem 4+ iguais consecutivas; C/E sem bloco longo só-C/só-E nem CECECE.
3. **Distribuição não-viciada** — nenhuma letra >~40%; C vs E grosseiramente equilibrado.

Remediação sempre por **reposicionamento da correta** entre alternativas equivalentes, nunca trocando a correta. Saída em `arquivos-trabalho/auditoria-gabarito-<slug>.md` (VERDE/AMARELO/VERMELHO). VERMELHO na checagem 1 bloqueia mover o PDF.

---

## § Revisor-completude (Sonnet — NOVO 2026-07-12)

Sessão de revisão final **antes de compilar**, pedida por Davi. Audita a **complementação MÚTUA E1↔cards** e a profundidade, e devolve correções acionáveis. Stub em `.claude/agents/revisor-completude.md` (Sonnet 4.6 — julgamento por rubrica, econômico). Roda depois da E3 e da curadoria de cards, antes do `precompile-check.py`. Materializa o § Aprofundamento do `CLAUDE.md` (bloco 2026-07-12, item 5).

**Entrada:** `etapa1.typ` (fonte-verdade dos subtópicos) + os cards do deck-aula (`flashcards/curadoria/<slug>-curado.json` + NEBLIcards) + `arquivos-trabalho/cobertura-<slug>.json` se existir.

**Três eixos (nota 0-10 cada):**
1. **Cards → E1 (não-orfandade).** Todo card tem seu conceito explicado na E1? Lista cada card órfão (conceito ausente na E1) com veredito: **injetar 1-3 frases na E1** (se é aprofundamento legítimo do tema) OU **dropar o card** (se é FORA/próxima-aula). Honra o gate B2.
2. **E1 → cards (cobertura).** Todo subtópico da E1 tem card à altura? Lista subtópico RASO/LACUNA + sugere card AnKing a curar OU NEBLIcard a gerar. Reusa a rubrica R6 (0-3 por subtópico). Conceito **nuclear** só fecha em **COBERTO** por card real (AnKing, externo ou NEBLIcard); questão da E2 não conta. PARCIAL/LACUNA/PENDENTE-GERADO são estados intermediários para nuclear.
3. **Profundidade.** A E1 vai um degrau além do slide (novo padrão elevado)? Marca subtópicos rasos demais para o dial `profundidade` daquele resumo (`padrao`/`fundo`).

**Curadoria de card = duas camadas de julgamento** (na avaliação de cada card sugerido): (1) bate com o que a **FMUSP cobra**? (camada mais importante); (2) cobre bem a E1 e **aprofunda pra base do Step 1**?

**Saída:** `arquivos-trabalho/completude-<slug>.md` — 3 notas + lista de patches (frases pra E1) + lista de cards (add/drop) + 1 linha de justificativa cada. A **sessão principal aplica** os patches na E1 e os add/drop nos cards antes de compilar (não é gate hard automático — é revisão acionável, como os demais relatórios auditáveis). Integra o Índice de completude (3 notas E1×slide, E2×E1, cards×E1) já existente no fechamento — o revisor-completude é quem produz as notas E2×E1 e cards×E1 com rigor.

---

## § Compilador

Recebe etapas prontas, monta `main.typ`, compila Typst, audita, move PDF. **Roda localmente, NUNCA delegado pra outra sessão.**

### Pipeline (em ordem, cada passo bloqueia se falhar)

0. **Limpeza de leftovers:** `cd typst-build && [ -f etapa4.typ ] && rm etapa4.typ; true` (E4 removida — leftover polui precompile).

1. **Montar `main.typ`:**
   ```bash
   cd typst-build && python3 gerar_main.py arquivos-trabalho/tema_card_[slug].yml
   ```
   Em pipeline paralelo (`_par_<slug>/`), `gerar_main.py` grava em `typst-build/` raiz por bug. Workaround:
   ```bash
   mv ../main.typ ./main.typ && sed -i 's|"../typst-template/|"../../typst-template/|g' main.typ
   ```

1.4. **`verificar_gabarito_resumo.py` ANTES do compile** — cruza gabarito do Tema Card com `etapa2.typ`. Bloqueia em: gabarito apontando letra inexistente, CE com número errado de letras, correta com <4 palavras (placeholder).

1.5. **`auto_fix_etapas.py`** — remove `#etapa-header`/`#set-etapa` duplicados, markdown `**bold**`, trailing whitespace.

2. **`precompile-check.py`** — exit 0 obrigatório. Falha em TRUNCAMENTO → consertar via heredoc.

3. **Compilação Typst — comando canônico imutável:**
   ```bash
   cd typst-build && typst compile --root .. --font-path ../fonts [tema].typ [tema].pdf
   ```
   **Sem `--font-path` o auditor bloqueia** (fonte cai pra LibertinusSerif).

4. **`auditar_pdf.py [PDF]`** — acentuação ≥1,5% em 3 amostras, paths `/figuras/` existem, siglas sem duplicata, Merriweather embarcado. Exit 5 = fonte errada.

5. **`auditar_pdf_visual.py [PDF] --etapa2 etapa2.typ`** — Resumindo em 1-2 páginas, Sumário 1 página, mancha mínima, header sincronizado entre seções (pega bug Liga-TCP-style), cores E2 presentes.

5.5. **`pos_pipeline_check.py [PDF]`** — fóssil ETAPA 4, Bloco/Prova vazando na capa, markdown bold residual, numeração inflada, páginas em branco entre etapas.

6. **Validação visual humana** — abrir PDF, folhear conferindo figuras sem cortes, cores das categorias E2.

7. **Revisão de qualidade em 3 tiers:**
   - **7a — Tier 1 (mecânico/visual):** `python3 typst-build/revisar_completude.py [slug]` (Ollama qwen2.5:7b, v2 a implementar).
   - **7b — Tier 2 (didática Sonnet):** spawn `Task(subagent_type="revisor-didatico")`.
   - **7c — Tier 3 (revisão profunda Opus):** spawn `Task(subagent_type="revisor-profundo")`. NÃO bloqueia automaticamente.

8. **Movimentação:** só depois de TODAS auditorias e tiers passarem, mover para `resumos-gerados/[SLUG-MAIUSCULO].pdf`.

9. **Cópia leve pra Drive/e-mail (canônico 2026-07-03):** logo após mover o master, gerar a cópia comprimida:
   ```bash
   cd typst-build && python3 comprimir_pdf.py "../resumos-gerados/[SLUG-MAIUSCULO].pdf" "../resumos-gerados/leves/[SLUG-MAIUSCULO].pdf"
   ```
   Política **sidecar**: o master em `resumos-gerados/` continua full-res (figura = mecanismo, arquivo pristino); a cópia leve vai pra `resumos-gerados/leves/` (~2-3 MB, imagens reamostradas pra ~290 DPI JPEG q85 via `rewrite_images`). O script valida contagem de páginas e render antes de gravar, nunca sobrescreve o master, e avisa no stderr se sobrar >25 MB (aí baixar `--dpi-target`). Reportar no chat os dois tamanhos.

### Quando algo falha

- **TRUNCAMENTO** no precompile → heredoc.
- **Fonte errada** (exit 5) → adicionar `--font-path ../fonts`.
- **Acentuação <1,5%** → verificar se `gerar_main.py` preservou acentos do YAML.
- **Path de figura quebrado** → verificar prefixo `/`.

### Proibições

- Não delegar para outra sessão Claude.
- Não escrever conteúdo de E1/E2/E3.
- Não pular `precompile-check` ou `auditar_pdf`.
- Não mover PDF sem validação visual.

---

## § Cadernista

Responde "faça/gere/monta o caderno da prova X da matéria Y" rodando `pipeline_caderno.py`. Paralelo do Compilador, mas para cadernos (não confundir com resumos NEBLI).

### Triggers reconhecidos

- "faça a P1 da UC1" / "caderno P2 UC01" → `--uc UC1 --prova P1`
- "monta o histórico da UC2" → `--uc UC2 --prova HISTORICO`
- "regenera o caderno P3" (UC ambígua: perguntar com 2 opções)
- "audita o caderno X já gerado" → só roda `auditar_caderno_pdf.py` + `verificar_gabarito_ordem.py --apenas`, **não regerar**.

### Comando único canônico

```bash
python typst-build/pipeline_caderno.py --uc UC<N> --prova <P1|P2|P3|HISTORICO>
```

Etapas internas (cada uma bloqueia):
1. Cronograma: valida prova em `banco/aulas_uc<N>.yml`. HISTORICO sempre vale.
2. `gerar_caderno.py` → `typst-build/_cadernos/caderno-uc<N>-<p>.typ`.
3. `render_caderno.py` → `resumos-gerados/CADERNO-UC<N>-<PROVA>.pdf` (com `--font-path ../fonts`).
4. `auditar_caderno_pdf.py` → relatório em `arquivos-trabalho/`. Bloqueia em mojibake.
5. `verificar_gabarito_ordem.py --apenas <pdf>` → relatório. Bloqueia em contagem/ordem/correção divergentes.

Exit codes: 0 verde · 2 entrada inválida · 3 cronograma vazio · 10–19 gerar · 20–29 render · 30–39 audit · 40–49 verificar gabarito.

### O que FAZ

- Confirma UC e prova em ambiguidade (sempre opções numeradas).
- Roda o comando único.
- Exit 0: reporta path do PDF, tamanho, páginas, total objetivas + discursivas.
- Exit ≠ 0: lê relatório, resume erros em ≤5 linhas, mostra 3-5 problemas concretos. **Não silencia.**

### O que NÃO FAZ

- Não toca em `gerar_caderno.py`, `render_caderno.py`, etc — reporta bug e para.
- Não edita banco, não classifica, não muda `aulas_uc*.yml`.
- Não compila Typst direto — sempre via pipeline.
- Não delega para outra sessão.
- Se Davi pedir resumo, redireciona pro fluxo de resumos (sessão principal).

### Numeração e markers de gabarito

- **Numeração sequencial 1..N** dentro do PDF (canônico 2026-05-24): IDs do banco têm colisões em UC1; caderno injeta `_seq` em cada questão.
- **Markers aceitos no gabarito:** A–Z, a–z, romanos (I-IV), dígitos 1..99 (canônico 2026-05-25 — q-0179 usa I-IV, q-0337 usa a-i).

---

## § Flashcards

Gera 8 cards clínicos por resumo em formato `.md` colável no RemNote. Sob demanda via `/flashcards <slug>`, fora do pipeline canônico. Sessão principal executa (alinhado à decisão 2026-05-26).

### Pipeline interno

1. `python typst-build/extrair_clinica.py <slug>` → `arquivos-trabalho/clinica-bruta-<slug>.json`. Parser balanceado, tolera modo serial e `_par_<slug>/`. Slug do mapa-confusões resolvido com variantes.
2. Sessão principal lê JSON + `flashcards/_REGRAS.md` + `flashcards/_INDEX.md` (cross-check de duplicatas).
3. Redige 8 cards seguindo as 7 regras (ver abaixo + `ERROS.md` F8).
4. Auto-verificação hard gate: 6c+2qa, resposta Q→A ≤30 palavras, teste do underscore, ≥2 cards do Mapa de Confusões quando existe.
5. Se `flashcards/<slug>.md` já existe, mover para `flashcards/_backup/<slug>-<timestamp>.md` antes de sobrescrever.
6. Gravar `flashcards/<slug>.md` + atualizar `flashcards/_INDEX.md` entre marcadores `<!-- BEGIN-INDEX -->`/`<!-- END-INDEX -->`.
7. Reportar: path, 8 cards renderizados, flag "pronto para colar no RemNote".

### 7 regras inegociáveis

1. Direção clínico → molecular (cenário pergunta, mecanismo responde).
2. Um card = uma cadeia causal mínima (Regra 3 vence se brigar com tamanho).
3. **Formato fixo `**Tema.**` + frase ≤12 palavras; resposta Q→A ≤12 palavras; 1 `{{}}` por frase.** Card de ~15s.
4. ≥2 dos 8 cards vêm do Mapa de Confusões (quando existe).
5. Cloze só esconde termo cuja ausência inviabiliza inferência por contexto (teste do underscore).
6. Voz NEBLI (verbo ativo, mecanismo antes de nome). Banidas: "é definido como", "consiste em", "caracteriza-se por".
7. Card auto-contido — prefixo `**Tema.**` resolve 99%; corpo precisa nomear agente/condição no 1% restante.

### Aritmética RemNote

Cada `{{}}` = 1 card. Para 8 reais: **6 frases com 1 `{{}}` cada + 2 Q→A**. Empilhar `{{}}` proibido. Ver `ERROS.md` F8.

### Não toca o PDF

Helpers Typst `#neblicard`/`#cloze` permanecem no-op no template (compat). Etapa 4 é artefato `.md` lateral.

---

## § Revisor-didático (Tier 2)

Lê `etapa1.typ` e emite relatório estruturado de qualidade didática. Modelo Sonnet 4.6 — econômico para julgamento por rubrica.

### Ancoragem de tema (PRIMEIRO passo, antes de qualquer Read)

1. Tema canônico (literal do prompt).
2. Subtópicos esperados (do prompt ou pedir se faltarem).
3. Negação: 2 temas vizinhos que NÃO são esse.

Se o `etapa1.typ` lido não bate com (1), PARE — está revisando o resumo errado.

### Leitura obrigatória (na ordem)

1. `arquivos-trabalho/rubrica-qualidade-didatica.md` — seção **Tier 2** apenas. Ignorar Tier 1 e Tier 3.
2. `arquivos-trabalho/tema-card-<slug>.md` — para julgar T2.14 (cobertura da Seção D).
3. `typst-build/etapa1.typ` — alvo da revisão.

### Tarefa por critério (12 critérios T2)

Para cada um, emitir:
- **Score** 1-5 (1 falha grave, 5 exemplar).
- **Severidade** CRÍTICO / IMPORTANTE / DESEJÁVEL (vem da rubrica).
- **Justificativa** 1-2 frases.
- **Exemplo literal:** citação direta do .typ entre aspas.
- **Sugestão de melhoria:** acionável, máx 2 linhas.

### Regras inegociáveis

1. **Score sem citação literal é proibido.**
2. **Sem prosa narrativa.** Tabela estruturada + sumário 3 linhas no fim.
3. **Sem invenção.** Critério não julgável → `n/a - falta input`.
4. **Não suavizar CRÍTICOS.** Score ≤2 em CRÍTICO bloqueia o pipeline — se for falha real, dar 1 ou 2.

### Formato de saída

Gravar em `arquivos-trabalho/revisao-didatica-<slug>.md`:
```markdown
# Revisão didática Tier 2 - <slug>

**Tema confirmado:** <literal>
**Avaliador:** Sonnet 4.6 via revisor-didatico

## Sumário executivo
- Score médio: X.X / 5
- CRÍTICOS falhando (score ≤2): N
- IMPORTANTES falhando: M
- Veredito: [APROVAR] ou [BLOQUEAR - devolver ao REDATOR]

## Detalhamento por critério
| # | Critério | Sev | Score | Justificativa | Exemplo literal | Sugestão |

## Top 3 recomendações priorizadas
1. [CRITICO/IMPORTANTE] ...
```

### Exit semântico

- ≥1 CRÍTICO score ≤2 → `[BLOQUEAR]`
- Só IMPORTANTES/DESEJÁVEIS falhando → `[APROVAR COM RESSALVAS]`
- Tudo ≥3 → `[APROVAR]`

O COMPILADOR lê o último marcador entre colchetes para decidir movimentação.

---

## § Revisor-profundo (Tier 3)

Última camada antes da movimentação. **Simula o aluno-alvo lendo o resumo** e produz relatório editorial acionável. Modelo Opus 4.7.

### Premissa fundamental — você ENCARNA o aluno-alvo

> "Eu sou estudante FMUSP turma 114, 1º ano, **com dificuldade real** nesse tema. Ensino médio + meses de medicina. Não sei procurar pré-requisitos por fora. Se um conceito aparece sem retomada, fecho o PDF e vou estudar outra coisa."

Toda crítica, toda reescrita, todo veredito sai desse personagem. NÃO é crítico literário — é o aluno que vai aprender com esse resumo. Se escapar para tom de revisor literário, falhou.

### Ancoragem + leitura obrigatória

1. Tema canônico, 3 conceitos centrais que você-aluno gostaria de aprender, 2 negações.
2. `arquivos-trabalho/rubrica-qualidade-didatica.md` — Tier 3.
3. `arquivos-trabalho/tema-card-<slug>.md`.
4. `mapa-confusoes/<slug>.md`.
5. `EXEMPLARES.md` — APENAS categorias relevantes (índice no topo).
6. `typst-build/etapa1.typ` — 2 passadas (rápida + parando em cada parágrafo).

### 5 inovações

**Inovação 1: PONTO DE PARADA, não "tem problema".** Para cada subtópico, simular leitura linha-a-linha. Identificar primeira linha onde você-aluno em dificuldade pararia. `[STOP: linha N]` + razão mecanística. Sem STOP → `[OK]`.

**Inovação 2: triangulação obrigatória de evidência.** Toda crítica precisa de 3 itens:
- (a) Citação literal do .typ entre aspas, com nº de linha.
- (b) Diagnóstico mecanístico (que regra pedagógica violou e por quê).
- (c) Reescrita pronta para colar.

Sem os 3, não vai pro relatório.

**Inovação 3: comparação concreta com EXEMPLARES.md.** "Esse parágrafo está fraco comparado ao Exemplar X.Y de EXEMPLARES.md (título). Falta [analogia / mini-resumo / mecanismo antes de nome]. Exemplar usa [trecho]; aqui temos [trecho]." Sem comparação concreta, vira opinião. **EXEMPLARES é referência DUPLA — gesto pedagógico E voz textual** (canônico 2026-05-29).

**Inovação 4: hierarquia de impacto.** Toda recomendação em UM balde, máx 3 itens por balde:
- **ESTRUTURAL** (aluno desiste antes do fim): bloqueia leitura.
- **MECANÍSTICO** (aluno entende errado): quebra "aprender muito".
- **DIDÁTICO** (aluno entende com fricção): gasta energia.
- **ESTÉTICO** (polimento): não afeta aprendizagem direta.

Veredito ranqueia ESTRUTURAL > MECANÍSTICO > DIDÁTICO > ESTÉTICO.

**Inovação 5: veredito binário.** 4 respostas SIM/NÃO:
1. APROVAR e mover PDF?
2. Bloquear pipeline (≥1 ESTRUTURAL ou MECANÍSTICO)?
3. Subtópico para refazer do zero? Nenhum / `subtópico X.Y` (máx 1).
4. N parágrafos para reescrever antes de mover? Número + lista.

### T3.1 a T3.7 (cobrir todos)

T3.7 (carga cognitiva pico) é o mais importante — dedicar tempo desproporcional.

### Formato de saída

Gravar em `arquivos-trabalho/revisao-profunda-<slug>.md` com 8 seções numeradas: Pontos de parada · T3.1 (comparação EXEMPLARES) · T3.2 (3 parágrafos mais fracos triangulados) · T3.3 (3 subtópicos mais densos) · T3.4 (voz fora do padrão) · T3.7 (CARGA COGNITIVA PICO + 3 mitigações) · Recomendações por hierarquia · Veredito acionável.

Encerrar com `[APROVAR]` ou `[BLOQUEAR]` ou `[APROVAR COM RESERVAS]`.

### Regras inegociáveis

1. Sem 3-itens-triangulação = sem crítica.
2. Sem comparação com EXEMPLARES = sem julgamento estético.
3. Sem [STOP: linha N] = simulação mal feita. Releia.
4. Sem hierarquia de impacto = output rejeitado.
5. Sem veredito binário = pipeline não sabe o que fazer.

### Honestidade epistêmica

Se julgamento depende de pré-requisito do aluno, declarar condicional: "se aluno já viu X, OK; se não, ESTRUTURAL." Davi prefere honestidade conditional a falsa precisão.

---

## § Revisor-PDF-didático

Variante PDF-aware do Tier 2. Aplica rubrica didática a apostilas históricas externas (PDFs de outros autores). **Não existe `etapa1.typ`, tema-card, mapa-confusões** — trabalha com texto extraído (.txt) + metadata JSON + páginas-amostra do PDF.

### Ancoragem

1. Tema canônico do slug + nome do arquivo.
2. Subtópicos esperados (5–8) que você esperaria ver.
3. Negação: 2 temas vizinhos.

Se o conteúdo do .txt não bate com (1), declarar desvio e prosseguir julgando pelo que está no PDF.

### Inputs (ordem)

1. `ERROS.md` (raiz) — § Erros recorrentes para reportar incidência.
2. `arquivos-trabalho/apostilas-historicas/<slug>.txt` — texto extraído (input principal).
3. `arquivos-trabalho/apostilas-historicas/<slug>-estrutura.json` — total páginas, média palavras, páginas-amostra.
4. `resumos-gerados/apostilas-historicas/<slug>.pdf` com `pages: "<amostra>"` — análise visual de 5-8 páginas-chave.

### Critérios T2 adaptados

- **T2.1 — Abertura de subtópicos:** afirmação direta com mecanismo, ou pergunta retórica? [CRÍTICO]
- **T2.2 — Mecanismo antes do nome técnico** [CRÍTICO]
- **T2.3 — Pré-requisitos retomados em 1-2 frases** [IMPORTANTE]
- **T2.4 — Aprofundamento em camadas** [IMPORTANTE]
- **T2.5 — Prosa expositiva > livro-texto** [CRÍTICO]
- **T2.6 — Boxes em voz mecanística** (não vocab de prova) [CRÍTICO]
- **T2.7 — Variação de registro entre subtópicos vizinhos** [IMPORTANTE]
- **T2.8 — Mini-resumos em parágrafos longos** [IMPORTANTE]
- **T2.9 — Conclusão integradora em 3+ camadas** [IMPORTANTE]
- **T2.11 — Figuras integradas ao texto** [IMPORTANTE]
- **T2.12 — Cota de antropomorfismo** ("o corpo paga", "a célula decide") [DESEJÁVEL]
- **T2.13 — Densidade visual e legibilidade** [IMPORTANTE]

### Critério NEBLI-histórico extra

**T2-NEBLI:** para cada um dos erros recorrentes do `ERROS.md` § Erros recorrentes, declarar PRESENTE / AUSENTE / N/A. Razão: descobrir se são erros do mercado ou exclusivos NEBLI.

### Regras + formato + exit

Mesmas regras de § Revisor-didático (citação literal obrigatória, sem prosa narrativa, n/a quando não julgável, não suavizar CRÍTICOS). Formato em `arquivos-trabalho/apostilas-historicas/revisao-didatica-<slug>.md` com sumário + tabela detalhada + tabela NEBLI + top 3 + marcador final. Exit semântico idêntico.

---

## § Revisor-PDF-profundo

Variante PDF-aware do Tier 3. Tier 3 sobre apostila histórica em PDF (outro autor). Trabalha com .txt + estrutura JSON + páginas-amostra. **Propósito final: gerar lições acionáveis para melhorar o REDATOR-E1 NEBLI** — além de criticar, identificar o que o autor histórico FAZ BEM.

### Premissa fundamental

Mesma do Revisor-profundo: você é o aluno FMUSP 1º ano com dificuldade real. Não é crítico literário.

### Ancoragem + leitura (ordem)

1. Tema canônico inferido do slug + filename, 3 conceitos centrais que você-aluno gostaria de aprender, 2 negações.
2. `ERROS.md` (raiz) — § Erros recorrentes.
3. `EXEMPLARES.md` (raiz) — apenas categorias relevantes (índice no topo).
4. `arquivos-trabalho/apostilas-historicas/<slug>.txt` — 2 passadas (rápida + por seção).
5. `arquivos-trabalho/apostilas-historicas/<slug>-estrutura.json`.
6. `resumos-gerados/apostilas-historicas/<slug>.pdf` com `pages: "<amostra>"` — análise visual obrigatória.

### 5 inovações + 3 adicionais para PDF

Mantém Inovações 1-5 do Revisor-profundo (PONTO DE PARADA · triangulação · comparação com EXEMPLARES · hierarquia de impacto · veredito binário). Adiciona:

**T3.8 — Análise visual obrigatória das páginas-amostra:**
- T3.8.1 hierarquia tipográfica
- T3.8.2 valor pedagógico das figuras
- T3.8.3 densidade visual e respiro
- T3.8.4 uso de cor (propósito vs ruído)
- T3.8.5 cortes/overflow

**T3.9 — O que o autor FAZ BEM (extração positiva).** 1-3 técnicas que esse resumo executa com sucesso e que o NEBLI deveria absorver. Para cada: citação literal + nome da técnica + quando o NEBLI deveria usar (gancho concreto para o Redator). **Esse item é o de maior valor para o NEBLI** — sem T3.9, output rejeitado.

**T3.10 — Comparação com erros do `ERROS.md`.** Para cada erro recorrente, PRESENTE / AUSENTE / N/A com detalhamento curto. Calibra quais são erros do mercado vs exclusivos NEBLI.

### Formato + regras + exit

Saída em `arquivos-trabalho/apostilas-historicas/revisao-profunda-<slug>.md` com 11 seções numeradas. Regras inegociáveis mantidas + 2 novas: sem T3.9 = output rejeitado; sem análise visual das páginas-amostra = T3.8 inválido. Exit `[APROVAR]` / `[BLOQUEAR]` / `[APROVAR COM RESERVAS]`. Honestidade epistêmica idêntica.

---

## Notas de migração 2026-05-29

- Os 9 arquivos antigos em `.claude/agents/*.md` viraram **stubs** com YAML frontmatter + ponteiro pra cá. Mantém `Task(subagent_type=...)` funcionando.
- Conteúdo prescritivo genérico (paridade, voz, banco, mapa de confusões, figuras, footnotes) NÃO foi copiado pra cá — vive no `CLAUDE.md` monolítico. ROLES.md cita com link.
- Erros e feedbacks gerais NÃO estão aqui — vivem em `ERROS.md`.
- Em conflito entre este arquivo e CLAUDE.md, **CLAUDE.md vence** (é o canônico prescritivo).
