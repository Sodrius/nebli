# CLAUDE.md — NEBLI (criador de resumos FMUSP)

> **DECKS — precedência de 25/09/2026:** ler `flashcards/projeto/CALIBRACAO-2026-09-25.md` e `AUDITORIA-2026-09-25.md` depois do README. Azul (4), não rosa, é candidato pós-prova; manter é o padrão. Acervo amplo ≠ núcleo de manutenção (referência até 35/aula). No lote atual, só deck e APKG local, sem E1/guia/upload. Os estados e instruções de 23/09 abaixo são históricos quando conflitarem. Não refazer seleção de arquivos antigos nem reinstalar card explicitamente rejeitado.

> **ATUALIZAÇÃO FINAL — reinício de 23/09/2026:** Davi limpou decks intencionalmente; nunca restaurar cards/pacotes históricos para sanar pendências. Na vistoria restavam só Genética 44 + Fisiologia 45; preservar remanescentes sem pedido de excluir. Publicação agora é **um APKG comprimido da UC inteira**, atualizado pelo mesmo file_id a cada aula, sem flags no arquivo e sem alterar flags da coleção. **Rosa já sinaliza bons candidatos pós-prova; manter é o padrão, Davi decide se suspende.** AnKing Step → outros acervos disponíveis, incluindo MCAT → autoria excepcional. Ler também `flashcards/projeto/ACERVOS-REFERENCIA.md` e `PUBLICACAO-POR-UC.md`; descoberta dinâmica `python -m nebli.preflight --catalog`, empacotador `python -m nebli.package_uc`. Esta atualização prevalece sobre qualquer referência abaixo a pacote por aula, rosa só visual ou suspensão pós-prova planejada. A próxima aula será escolhida pelo usuário.

> **ROTA CANÔNICA DE DECK-AULA — v4, 23/09/2026:** ler `flashcards/projeto/README.md` → `CALIBRACAO-ESCALA-V4.md` (30 respostas recebidas) → `CONTRATO-DE-QUALIDADE.md` → `OPERACAO-CODEX-CLAUDE.md` → `EXECUCAO-DECK-AULA.md` → caso semelhante. Esses arquivos prevalecem sobre regras históricas de cards abaixo. AnKing amplo dentro do assunto antes da prova; outros acervos locais antes da autoria excepcional; manutenção menor proposta para confirmação depois. E1 explicativa + guia com vídeos/bibliografia + Anki + APKG no Drive privado. Vídeos no guia/chat, nunca nos cards. Vermelho = melhorar; laranja = pedido pendente; verde = HY literal; rosa = variante visual candidata a suspensão. Resolver pendências anteriores ao iniciar nova aula. Preservar originais, histórico e marcas pessoais. E2/E3 suspensas, sem RemNote/cota/loop absoluto Card→E1. Use `/deck-aula <nome ou link>`; é execução assistida, não CLI autônoma já concluída.

Sistema de geração de resumos autorais para FMUSP, 1º ano. Filosofia: causa → mecanismo → consequência, em prosa expositiva fluida do início ao fim. Não é livro-texto resumido, é monitor explicando — prosa narrativa contínua, não cadeia simulada de pergunta-resposta.

## Missão do NEBLI (canônica 2026-05-25)

**Apostila de extrema qualidade que leva o aluno do básico ao aprofundado.** Premissa: o aluno sabe pouco e tem dificuldade real no tema; o resumo é a ferramenta dele para aprender muito. Toda decisão editorial — voz, profundidade, jargão, figuras, distratoras — passa por esse filtro. Em conflito entre concisão e ensinar bem, ensinar bem vence.

## Diretrizes vs. exemplares (canônica 2026-05-28)

As regras deste `CLAUDE.md`, do `MEMORY.md` e dos agents em `.claude/agents/` são **diretrizes** — princípios sobre o que um resumo NEBLI faz. A **implementação canônica** dessas diretrizes vive em `EXEMPLARES.md`: cada exemplar é uma diretriz acontecendo em prosa real.

Como isso pesa na prática:

- Cumprir uma diretriz = reproduzir o *gesto* E a *voz textual* demonstrados no exemplar relevante, adaptado ao tema atual. Não é tickar item de checklist. EXEMPLARES.md é referência **dupla** (canônico 2026-05-29): gesto pedagógico (causa → mecanismo → consequência, abertura, ritmo da cadeia) E prosa modelo em si (escolha de verbo, comprimento de frase, transições, encadeamento de oração).
- Quando regra literal e exemplar divergirem, o exemplar vence — porque o exemplar é a regra implementada.
- "Aplicar o exemplar" não é copiar trecho. É entender o que ele acerta (ritmo, abertura, cadeia causal, escolha de analogia) e repetir esse acerto adaptado ao tema novo.
- Cotas técnicas (figuras, termo-notas, footnotes, paridade de distratoras) continuam como **pisos auditáveis**. A *voz* da prosa é governada pelos exemplares — não pelas regras.

Convite, não gate: essa reframe altera *como* leio o canônico, não substitui auditor técnico. Em mudanças sobre voz/fluidez, tom de convite > obrigação (ver `feedback_evitar_engessar_anti_engessamento.md`).

## Memory System

**Leitura obrigatória em TODA sessão NEBLI (sem precisar pedir):**

1. `MEMORY.md` (raiz do projeto) — Active Projects, Scheduled Tasks, **§ Diário de revisões**, Pendências, Histórico, Core Memory. Carrega automaticamente.
2. `ERROS.md` (raiz do projeto) — armadilhas técnicas (§ Erros recorrentes, 18 itens) + feedbacks de processo (§ Feedbacks F1-F9). Consultar SEMPRE antes de fechar um resumo. Não esperar Davi pedir.
3. `ROLES.md` (raiz do projeto) — papéis do pipeline (Orquestrador, Redator-E1, Questionador, Compilador, Cadernista, Flashcards, 4 Revisores). Stubs em `.claude/agents/` apontam pra cá.

**Antes de gerar qualquer resumo, aplicar o § Diário de revisões.** Entradas vivas com peso alto viram **lista de prioridades pra esta corrida**, declarada no Tema Card Seção A. Decaimento automático após 5 resumos sem reincidência.

Regras gerais (canônico 2026-05-29 pós-faxina):
- **4 arquivos vivos no canônico:** `CLAUDE.md` (prescritivo monolítico), `MEMORY.md` (estado + diário + pendências + histórico), `ERROS.md` (armadilhas + feedbacks de processo), `ROLES.md` (papéis do pipeline). `EXEMPLARES.md` continua como lazy-load (referência dupla — gesto + voz textual).
- **Teste prescritivo vs factual:** entrada prescritiva ("sempre/nunca", "antes de X, faça Y") vive aqui no `CLAUDE.md`. Fato que pode mudar (estado de pacote visual, projeto ativo, data canônica) vive no `MEMORY.md`. Armadilha técnica recorrente vai pro `ERROS.md` § Erros recorrentes. Feedback sobre como trabalhar vai pro `ERROS.md` § Feedbacks de processo. Especificidade de papel no pipeline vai pro `ROLES.md`. Em dúvida, perguntar.
- **Quando uma decisão canônica nasce:** (a) `CLAUDE.md` se prescritiva genérica; (b) `MEMORY.md` § Histórico (linha curta) + § Pendências se ainda aberta; (c) `ERROS.md` se armadilha recorrente; (d) `ROLES.md` se afeta papel específico; (e) atualizar o stub correspondente em `.claude/agents/` se mudou frontmatter (modelo/tools/description).
- **Feedback acumulável com peso dinâmico:** quando Davi nota um problema num resumo individual (mesmo que a regra já exista), anotar em `MEMORY.md` § Diário de revisões em vez de criar regra nova.

## Preferences (resumo — perfil completo no MEMORY.md)

- Prosa expositiva precede tudo. Mecanismo antes de nomenclatura.
- Em dúvida, pergunte com opções numeradas, não texto livre.
- Plano antes de execução para qualquer tarefa não-trivial.
- Pushback construtivo > validação automática.
- **Baseline do aluno (canônico 2026-05-25, atualizado 2026-05-29):** presumir conhecimento BAIXO e dificuldade real com o assunto. O resumo abre cada conceito com **afirmação direta do mecanismo**, dá o nome técnico só DEPOIS do mecanismo entendido. Aprofundamento vem por camadas — primeiro o "porquê" cru, depois nuance/exceção/integração clínica. Nunca presumir que o aluno "já sabe" um pré-requisito sem retomar em 1–2 frases. **Sem pergunta âncora / pergunta retórica / pergunta ingênua como recurso de abertura** (canônico 2026-05-29 — substitui o antigo "ancora em pergunta ingênua plausível"). Os 5 registros de abertura canônicos são: enquadramento, integração-anterior, integração-posterior, analogia concreta, ponto-de-quebra.

## Rules globais

- **Paridade de distratoras — banda dupla (CANON 2026-05-22 → Q26-Q30 explícita 2026-05-26 → estendida a Q01-Q30 em 2026-05-29 → banda dupla 0.80-1.25 em 2026-05-29):** em **toda** questão objetiva da E2 (Q01 a Q30, sem exceção — Consolidação, Integração e Aplicação), a correta cai entre 80% e 125% da MAIOR distratora em comprimento de palavras. Gate hard de fechamento: **0.80 ≤ ratio = palavras(correta) / palavras(maior distratora) ≤ 1.25** para cada uma das 30 questões. A banda é simétrica por princípio: o tell visual opera nos dois lados — correta mais comprida que todas, ou correta visivelmente mais curta (sintoma de distratoras infladas artificialmente). **Remediação tem direção:** se a correta saiu curta (ratio < 0.80), enriquecer a CORRETA com mecanismo, não inchar distratora; se a correta saiu longa (ratio > 1.25), enriquecer DISTRATORAS com mecanismo plausível-errado, não cortar correta. Se uma distratora não tem mecanismo plausível-errado para sustentar 25-35 palavras, **trocar a distratora**, não inflá-la com prosa vazia. Procedimento operacional (ordem invertida de redação) e relatório de ratio obrigatório (Q01-Q30, com direção) vivem em `.claude/agents/questionador.md`. Implementação em `typst-build/precompile-check.py` (módulo `audit_paridade` + `audit_e2_regras_extra` cobrem as 30, banda dupla desde 2026-05-29). Mudou aqui? Atualize os 2 também.
- **Filtro de admissão para Integração na E2 (CANON 2026-05-28):** antes de redigir cada Q11-Q25, gravar em `arquivos-trabalho/integracao-mapa-<slug>.md` uma linha por questão no formato `Qxx conecta [A] + [B]` (dois domínios distintos). Se não preenche o `+`, volta para Consolidação. Gate operacional único — todas as demais alavancas (tipos de cruzamento, padrões de stem, uso do Mapa de Confusões, ângulo "Por que/Como" em Consolidação) vivem em `.claude/agents/questionador.md` § "Filtro de admissão" + § "Inspirações e sugestões" como **sugestão**, com liberdade explícita do operador. Sem cotas numéricas — convite > obrigação (ver `feedback_evitar_engessar_anti_engessamento.md`).
- **Formatos de item na E2 (CANON 2026-06-24, itens 6/9/10; atualizado 2026-07-01):** três formatos convivem nas 30 objetivas — múltipla escolha (base, 5 alternativas A-E), **Certo/Errado em ~1/3 (≈10 itens)** distribuídos pelas três categorias, e **"assinale a incorreta"** com parcimônia (2-4, stem sinalizado). **Toda questão C/E tem SEMPRE exatamente 4 itens (I-IV) — gate hard (CANON 2026-07-01)**, verificado por `precompile-check.py` (`check_ce_quatro_itens`). Detalhes operacionais em `ROLES.md` § Questionador → § Formatos de item.
- **Cobertura da E1 na E2 (CANON 2026-07-01):** **todo subtópico da E1 é testado por ≥2 questões da E2** (contagem no nível da questão; item de C/E conta para o subtópico que ele cobre). Não é gate por regex — é diretriz auditável: a sessão principal entrega no relatório de fechamento uma **tabela subtópico → questões que o cobrem**, análoga ao ratio Q01-Q30 e à tabela de figuras. Subtópico com <2 questões volta pra prancheta antes de fechar.
- **Gabarito sorteado de verdade + guarda anti-degeneração (CANON 2026-06-24, itens 5/9/17):** sortear o sinal de cada questão; nenhuma letra A-E acima de ~40%; sem corrida de 4+ iguais; C/E sem bloco longo nem CECECE. A guarda **reposiciona a correta** entre alternativas equivalentes, nunca muda qual é a correta nem engenheira a resposta para uma letra. Passada final do **revisor-gabarito (Haiku)** confere impresso==real (item 8). Detalhes em `ROLES.md` § Gabarito sorteado de verdade + § Revisor-gabarito.
- Strings YAML do Tema Card sempre acentuadas — `gerar_main.py` preserva Unicode. Escrever "Difusão", "Lipossolubilidade", "íonico" — nunca sem til.
- Gravação inicial de `.typ` SEMPRE via heredoc atômico (`cat > arquivo.typ << 'EOF' ... EOF`). Write tool trunca em `.typ` grandes com Unicode pesado. Edit tool continua válido para mudanças pontuais.
- `precompile-check.py` antes de qualquer compilação. `auditar_pdf.py` antes de mover PDF para `resumos-gerados/`. Falha em qualquer um para no ralo, COMPILADOR conserta antes.
- Comando canônico imutável de compilação: `cd typst-build && typst compile --root .. --font-path ../fonts [tema].typ [tema].pdf`. **Sem `--font-path` o auditor bloqueia** (fonte cai pra LibertinusSerif).
- Pendências de melhora vão para `MEMORY.md` § Pendências abertas ANTES de executar mudança canônica (faxina 2026-05-29 absorveu o antigo `pendências de melhora.md`).

## Pipeline legado de resumo completo: profundidade da E1 + loop Card→E1

> **Escopo legado:** esta seção governa somente o pipeline completo de criação de resumo quando ele for explicitamente solicitado. Não governa o deck-aula independente. No deck-aula atual, a seleção não precisa estar integralmente explicada na E1, E2/E3 estão suspensas e vale `flashcards/projeto/EXECUCAO-DECK-AULA.md`.

Norte: **a E1 vai sempre um degrau além do slide** — e esse aprofundamento se propaga para a E2 e para os cards. Vale para todo resumo NEBLI.

**REGRA LEGADA DO RESUMO COMPLETO — NÃO USAR NO DECK-AULA INDEPENDENTE.** Nesse fluxo antigo, um card só entrava quando o conceito estava explicado na E1. Esta exigência foi substituída, para a rota `/deck-aula`, pelo runbook novo: a E1 acompanha como guia/consulta e não precisa reproduzir todos os Extras dos cards.

**Passe de aprofundamento (≈1 injeção mecanística por subtópico, ~9-12 no total).** Depois do rascunho da E1 e da seleção de cards, voltar na E1 e injetar por subtópico 1 conteúdo extra mecanístico (1-3 frases), colado a um mecanismo que o subtópico já abriu. **Padrão de profundidade = atual + um degrau:** cada injeção carrega mais mecanismo/porquê. **Proporcionalidade:** o "≈1 por subtópico" é piso, não teto uniforme — subtópicos maiores/mais pesados recebem proporcionalmente mais (o peso do tema rege o espaço). **Regra-mestra:** o **slide regula O QUE entra** (escopo), o **AnKing/bibliografia regula ATÉ QUE PROFUNDIDADE** (calibre) — `profundidade = max(AnKing, slide/banco/bibliografia)`, tendendo ao teto do AnKing para o mesmo mecanismo. Se não há onde encaixar, não encaixa — nunca forçar toca de coelho de Step 1 que descasa do slide. **Qualidade obrigatória:** como o Davi provavelmente não viu o extra em aula, o aprofundamento tem de estar correto e bem explicado, nunca termo solto. **O CONTEÚDO nível Step 1 é muito bem-vindo — é o calibre buscado**; o que é banido no PDF é só o **vocabulário/rótulo** "Step 1/USMLE/residência" (o conteúdo entra como mecanismo/cenário clínico puro, sem citar a fonte).

**Cards induzem os aprofundamentos + ordem do pipeline (GH1).** A seleção de cards revela o que o campo trata como núcleo; boa parte dos aprofundamentos da E1 é induzida por bons cards do AnKing (que vão pro deck-aula). Por isso: **E1 rascunho → seleção de cards + passe de aprofundamento → E2/E3**, para a E2 já cobrar o extra (sobe de teto junto com a E1). Sem Anki vivo, o aprofundamento nasce do mapa de cobertura offline + blueprint + bibliografia, revalidando paridade/gabarito na E2.

**Dial por resumo — `profundidade:` na Seção A do Tema Card:** `padrao` (default já elevado) | `fundo` (um degrau acima: mais injeções por subtópico, limiar de admissão afrouxado para ~7/10, blocos clínicos e roxos maiores). Davi diz "resumo X vai fundo" → grava na Seção A. Escala a mão, sem cota rígida.

**Blocos clínicos maiores, no nível que o card do AnKing cobra.** O `#clinica-box` (azul) **(a)** torna explícito o **gancho doença↔assunto** (por que essa doença ilustra esse mecanismo) e **(b)** explica a doença na profundidade **fisiopatológica que os cards daquela aula vão cobrar** — o Davi tem base fisiológica E fisiopatológica antes do card (honra o gate: nada de card órfão). Continua "poucos e naturais"; cresce a **profundidade do gancho**, não o número de blocos (poucos cards por doença, nunca 15).

**Bloco ROXO — aprofundamento que agrega mas não foi dado em aula.** Legenda das caixas: **vermelho** = confusão de prova · **azul** = clínica · **amarelo** = confusão elaborada (Mapa de Confusões) · **roxo** = algo a mais que agrega, fora do que a aula deu. (Helper `#roxo-box` a criar no template via `frontend-design` na 1ª apostila que usar.)

**Revisor de completude MÚTUA E1↔cards (Sonnet, pré-compilação).** Audita os dois sentidos: **(a)** todo card do deck está explicado na E1? **(b)** todo subtópico da E1 tem card à altura? Nota 0-10 a cada eixo, corrige (injeta frase na E1 / adiciona card) no nível de profundidade elevado. Curadoria de card em duas camadas de julgamento: (1) bate com o que a FMUSP cobra? (mais importante) (2) cobre bem a E1 e aprofunda pra base do Step 1? Papel em `ROLES.md` § Revisor-completude.

**Índice de completude (0-10, 3 eixos) no relatório de fechamento** (auditável, convite — não gate hard; F7): **E1 × slide** (cobre tudo do slide + um tiquinho além? 0-4 falta slide · 5-7 cobre fiel · 8-9 cobre + aprofundamentos integrados; **meta 8-9**; <8 por falta de cobertura do slide volta pra prancheta) · **E2 × E1** (cada subtópico, incl. aprofundamentos, é cobrado? resume a tabela subtópico→questões; **meta ≥8**) · **Cards × E1** (os cards cobrem os subtópicos? X/Y COBERTOS num 0-10; **meta ≥7**, lacuna aponta fonte). Detalhe em `ROLES.md` § Índice de completude.

## Nomenclatura única + upload automático pro Drive (CANON 2026-07-12)

**Um nome só, que bate em tudo.** Cada aula tem um **nome curto e simples** (ex.: `Embriologia II`) que é, ao mesmo tempo: o **nome da pasta** no Drive, o nome-base do **.apkg** do deck-aula, e o nome-base do **PDF** do resumo. A pasta da aula no Drive contém **slide + resumo (PDF) + .apkg**.
- **Naming do PDF:** `<aula curta> - Etapas 1 a 3 - <sigla do prof>` (ex.: `Embriologia II - Etapas 1 a 3 - CYIY.pdf`). Sigla do docente vem do cronograma da UC.
- **Naming do deck:** `<aula curta>.apkg` (ex.: `Embriologia II.apkg`).
- O nome-curto da aula também é a folha da árvore Anki `NEBLI::UC::Prova::Componente::Aula` — Drive e Anki espelham a mesma organização.

**Upload automático (Davi só manda o slide; NEBLI organiza o resto):** quando um resumo fecha, subir **PDF + slide** pra pasta da aula (criando-a no padrão do Davi se não existir); quando um deck-aula é montado, `exportPackage` (AnkiConnect) gera o `.apkg` e sobe pra mesma pasta. Via **rclone** (instalado 2026-07-12; remote a autorizar 1×). Helper: `flashcards/scripts/subir_drive.py` (a criar; recebe slug + aula-curta + prova/componente + prof).

**Espelhar a organização do Davi para futuras UCs (obrigatório antes de qualquer upload):** estudar a fundo a estrutura atual do Drive (via `rclone tree`/`lsd`) e replicá-la **exatamente** — a árvore dele (UC › componente/prova › aula) é o template. A cada UC nova, ficar atento ao **cronograma** que o Davi mandar pra encaixar aula→prova→componente do jeito dele. Nunca impor estrutura própria; seguir a que já existe.

**Geração de deck-aula em massa (PLANEJADO — não executar ainda):** montar decks de todas as aulas passadas é plano grande, incremental (cada aula = curadoria + Revisor-completude + gate + apply), casado com o .apkg→Drive: cada aula fechada aterrissa no Drive pronta. Começar por prova quando Davi liberar.

## Routing Map (canônico revisto 2026-05-26)

**Decisão canônica 2026-05-26 — Davi suspendeu uso de subagentes REDATOR-E1 e QUESTIONADOR.** Causa: bug #3 do `ERROS.md` reincidiu (Task spawn parou sem disparar Read, simulou tool calls inline — confirmado novamente em piloto de 2026-05-28, ver `ERROS.md` F9). A **sessão principal (Claude Code, modelo Opus) atua como ORQUESTRADOR + REDATOR + QUESTIONADOR fundidos**.

| Papel | Quem executa | Função |
|---|---|---|
| ORQUESTRADOR + REDATOR + QUESTIONADOR | Sessão principal (Opus) | Tema Card, E1, Resumindo, E2 (30 questões), E3 (5 discursivas). Lê `ROLES.md` §§ Orquestrador/Redator-E1/Questionador como guia prescritivo próprio. |
| COMPILADOR | Local (Bash) | `gerar_main.py` → `auto_fix_etapas.py` → `precompile-check.py` → `typst compile` → `auditar_pdf.py` → mover PDF → `comprimir_pdf.py` (cópia leve pra `resumos-gerados/leves/`). Detalhes em `ROLES.md` § Compilador. |
| CADERNISTA | Task subagent (Sonnet) | Cadernos de questões (`pipeline_caderno.py`). Pipeline determinístico, mantido. Stub em `.claude/agents/cadernista.md` aponta pra `ROLES.md` § Cadernista. |
| Revisores Tier 2/3 (didático + profundo, internos + PDF-aware) | Task subagent | Rodam após COMPILADOR antes de mover PDF. `ROLES.md` §§ Revisor-*. |
| REVISOR-GABARITO (Haiku) | Task subagent | Passada final de conferência do gabarito da E2 (impresso==real, sem corrida, distribuição sã). `ROLES.md` § Revisor-gabarito. Novo 2026-06-24. |
| REVISOR-COMPLETUDE (Sonnet) | Task subagent | Antes de compilar: completude MÚTUA E1↔cards + profundidade (3 notas 0-10 + patches de E1 e add/drop de cards). `ROLES.md` § Revisor-completude. Novo 2026-07-12. |

`ROLES.md` §§ Redator-E1 / Questionador permanecem como **referências prescritivas** — a sessão principal lê e segue, mas não delega via Task.

COMPILADOR roda localmente, NUNCA delegado a outra sessão.

## References (lazy load — leia quando o tema exigir)

- `typst-template/CHEATSHEET_ARMADILHAS.md` — 10 bugs Typst recorrentes. Subagente lê PRIMEIRO antes de redigir.
- `typst-template/TEMPLATE_API.md` — assinaturas dos 35 helpers (~2k tokens, substitui leitura do `.typ` inteiro).
- `typst-template/CLAUDE.md` — regras da pasta template (carregada automaticamente no Claude Code).
- `banco/CLAUDE.md` — schema do banco (carregada automaticamente no Claude Code).
- `EXEMPLARES.md` — few-shot, **referência DUPLA** (canônico 2026-05-29): gesto pedagógico E voz textual modelo. Use o índice `## Quando usar` no topo. Em conflito de voz/gesto com regra abstrata, exemplar vence.
- `mapa-confusoes/<slug>.md` — Mapa de Confusões por tema (criado/atualizado pelo Questionador).
- `referencias-externas/blueprint-step1.md` — **calibração externa invisível por aula** (canônico 2026-06-30). Tabela slug→(rendimento ALTO/MÉDIO/BAIXO, o que aprofundar em 1-2 frases na E1, ângulo de Aplicação para E2/E3, gancho clínico de residência BR). Régua de profundidade vinda do blueprint USMLE Step 1 + padrões de banca. **Espelha o papel do `banco_slim.json`: consultado durante a redação, NUNCA colado no PDF.** A fonte fica invisível — aprofundamento entra como mecanismo puro, gancho como cenário clínico puro. Vocabulário "USMLE/Step 1/residência" continua banido no PDF (ver `ROLES.md` Redator regra 10 detalhada). Foco no slide vence sempre; coluna BAIXO = "não force clínica aqui".
- `referencias-externas/onde-aprofundar.md` — **mapa slug→plataformas VISÍVEL** (canônico 2026-06-30). Irmão do blueprint, mas **inverso**: este VAI pro PDF (bloco "Onde aprofundar" da capa). 5 bullets por slug: AnKing v12 (tag exata pra dessuspender) / UWorld / Boards & Beyond / Sketchy / Pathoma. Preenchido best-effort pelo Orquestrador. Exceção escopada à regra Step 1 — nomes de plataforma só nesse bloco. Prefixo de tag v12 fica aproximado (`…::`) até Davi exportar `flashcards/scripts/anking-v12-export.txt`, quando um script troca pelo real de uma vez.
- `flashcards/projeto/README.md` + `EXECUCAO-DECK-AULA.md` + `CALIBRACAO-DECK-AULA-V3.md` — processo canônico atual de decks-aula. O antigo `FLASHCARDS.md` e seus gates não governam esta rota.
- `flashcards/CURADORIA-ANKING.md` — **método técnico de curadoria AnKing v12 por aula** (canônico 2026-07-03). Máquina de 2 camadas (tag grossa PURA/IMPURA/RUÍDO → card fino keep/drop) que dá a cada aula 30–50 cards MUITO bem curados, marcados `NEBLI::<slug>` e dessuspendidos via AnkiConnect. Gap-analysis proativo aponta a fonte do que o AnKing não cobre. Irmão FINO do `onde-aprofundar.md` (aquele lista decks na capa; este seleciona cards no deck). Estado em `flashcards/curadoria/` (`_INDEX.md` = painel/aviso vivo de dessuspendidos; `<slug>.md` + `<slug>-curado.json` por aula). Scripts em `referencias-externas/`: `extrair_cards_anking.py` (emite `raw0` = campo 1 bruto), `aplicar_curadoria_anking.py`, `zerar_deck_anking.py` (re-suspende tudo, reversível via `NEBLI::zerado::<data>`), `revisao_diaria_anking.py` + `monitor_email_anking.py` (monitor `--diario`/`--semanal`, voz NEBLI via API + Gmail SMTP). **Nota técnica:** o AnkiConnect local NÃO expõe `guid` no `notesInfo`; o apply casa card-a-card pelo **texto bruto do campo 1** (lê o pool `anking-pool-<slug>.json`), não por guid. Auto-aplicado no fim do `/resumo` (passo 11).
- `referencias-externas/INFRA-REMOTO.md` — **infra sempre-on + controle remoto** (canônico 2026-07-03). Anki headless em Docker (deck acessível sem o app aberto, sync AnkiWeb), `claude remote-control` (celular dirige a sessão no PC — cloud agents NÃO alcançam localhost/AnkiConnect), Windows Task Scheduler pros 2 emails do monitor. Segredos por env var (`GMAIL_APP_PASSWORD`, `ANTHROPIC_API_KEY`), nunca no git.
- `backups/pre-faxina-2026-05-29/` — snapshot da raiz pré-faxina (CLAUDE.md/MEMORY.md/CHANGELOG_CLAUDE.md/pendências/FILOSOFIA/ARCHIVE + 9 agents originais + 18 arquivos do memory pessoal). Acesso via Read explícito para auditoria histórica.
- `backups/planos-historicos/` — planos arquivados (PLANO_ECONOMIA_TOKENS v1+v2, PLANO_LIGA_TCP, propostas-pos-g20).

## Pipeline canônico Typst

- **Template ativo:** `typst-template/nebli_v2_apostila.typ`. Apostila brasileira, Merriweather corpo + Montserrat títulos. Detalhes do pacote visual ativo no `MEMORY.md`.
- **Template legacy:** `typst-template/nebli_v1.typ` (DejaVu). Preservado, não usar em resumos novos.
- **Pasta de trabalho por resumo:** `typst-build/` (raiz) ou `typst-build/_par_<slug>/` (pipeline paralelo). No paralelo, `gerar_main.py` grava em `typst-build/` raiz por bug — workaround documentado no `.claude/agents/compilador.md`.

## Cadernos de questões

Caderno = compilação de TODAS as questões do banco filtradas por UC + prova, numeração sequencial 1..N. **Não confundir com resumo NEBLI** (E1/E2/E3). Não tem redação autoral, não tem Resumindo, não tem footnotes. Gabarito consolidado é a última seção (apêndice de explicações foi removido em 2026-05-24).

**Comando único canônico (orquestra tudo):**

```bash
python typst-build/pipeline_caderno.py --uc UC<N> --prova <P1|P2|P3|HISTORICO>
```

Saída final em `resumos-gerados/CADERNO-UC<N>-<PROVA>.pdf` (mesmo diretório dos resumos — design tolerado).

**Pipeline interno** (cada etapa bloqueia se falhar):

1. **Cronograma:** valida em `banco/aulas_uc<N>.yml` que a prova existe. HISTORICO sempre vale (recolhe questões fora do cronograma da UC).
2. `typst-build/gerar_caderno.py` → `typst-build/_cadernos/caderno-uc<N>-<p>.typ`.
3. `typst-build/render_caderno.py` → PDF em `resumos-gerados/`. Comando Typst com `--font-path ../../fonts` obrigatório (raiz dois níveis acima por causa de `_cadernos/`).
4. `typst-build/auditar_caderno_pdf.py` → `arquivos-trabalho/auditoria-pdf-CADERNO-UC<N>-<PROVA>.md`. Bloqueia em mojibake; warnings (ascii residual, hifenização, semi-vazias) só reportam. Métrica "Cobertura X/Y" desse script está desalinhada pós-mudança de IDs sequenciais (2026-05-24) — não usar como bloqueio, ver passo 5.
5. `typst-build/verificar_gabarito_ordem.py --apenas <pdf>` → `arquivos-trabalho/verificacao-gabarito-<stem>.md`. Verifica contagem, ordem e correção do gabarito impresso vs banco. Esse é o gate real.

**Numeração sequencial 1..N** (canônico 2026-05-24): IDs do banco têm colisões em UC1 (q-0014, q-0016 etc com `id: 14` repetido). Solução: o caderno usa numeração sequencial dentro do PDF, começando em objetivas e seguindo nas discursivas. `gerar_caderno.py` injeta `_seq` em cada questão; o `verificar_gabarito_ordem.py` reconstitui o mesmo mapeamento para checar contra o banco.

**Markers de gabarito aceitos** (canônico 2026-05-25): A–Z, a–z, numerais romanos (I, II, III...), dígitos (1..99). Regex em `extrair_gabarito` foi expandida para cobrir CE com markers fora de [A-E] — q-0179 usa I-IV, q-0337 usa a-i.

**Agente:** CADERNISTA (`.claude/agents/cadernista.md`). Davi pede "faça a prova X da matéria Y" → CADERNISTA roda `pipeline_caderno.py` e reporta. COMPILADOR continua dedicado a resumos.

## Etapa 4 — Flashcards RemNote (APOSENTADO 2026-07-07)

Removido do que o NEBLI faz. Não gerar RemNote-cards. Desde 23/09/2026, `/flashcards` é apenas um alias de compatibilidade que redireciona para o novo `/deck-aula`; o procedimento canônico está em `flashcards/projeto/EXECUCAO-DECK-AULA.md`.

## Estrutura de pastas

```
nebli/                            # 4 arquivos vivos no canônico, pós-faxina 2026-05-29
├── CLAUDE.md             (este arquivo — núcleo prescritivo monolítico, carrega em sessão)
├── MEMORY.md             (estado + § Diário de revisões + § Pendências + § Histórico, carrega em sessão)
├── ERROS.md              (armadilhas técnicas + feedbacks de processo, carrega em sessão)
├── ROLES.md              (papéis do pipeline — fusão dos 9 agents originais, lazy load)
├── EXEMPLARES.md         (few-shot, referência DUPLA — gesto + voz textual, lazy load com índice no topo)
├── .claude/
│   ├── agents/           (9 stubs YAML + ponteiro pra ROLES.md — preservam Task subagent_type)
│   ├── commands/         (slash commands)
│   └── settings*.json    (config Claude Code)
├── typst-template/       (CLAUDE.md + cheatsheet + API + nebli_v2)
├── typst-build/          (scripts + workspace por resumo)
├── banco/                (CLAUDE.md + 413+ questões + slim + aulas)
├── figuras/              (PNGs por tema + MAPA_CONTEUDO)
├── slides/               (entradas dos resumos)
├── resumos-gerados/      (PDFs finais)
├── arquivos-trabalho/    (temporários + relatórios + tema cards)
├── mapa-confusoes/       (mapas por slug)
├── flashcards/           (deck Anki: curadoria AnKing + NEBLIcards + scripts + gates)
├── backups/
│   ├── pre-faxina-2026-05-29/  (snapshot integral pré-faxina)
│   ├── planos-historicos/  (planos arquivados)
│   ├── tecnicos/           (.bak pré-mudanças)
│   └── operacoes-fechadas/ (operações encerradas)
├── fonts/                (Merriweather + Montserrat)
├── NEBLIcards/           (E5 legacy — vazia; substituída por flashcards/ em 2026-05-27)
├── _material/            (referência bibliográfica)
└── Inspiração de FORMA/  (referência visual)
```

## Ordem do PDF

1. **Capa:** faixa navy com tema + subtítulo (vazio ou disciplina seca); bloco meta canônico (Disciplina · Onde estudar) — canônico 2026-05-26: "Nota de uso" removida do bloco meta a pedido de Davi; **"Onde aprofundar" REMOVIDO da capa (canônico 2026-07-07, a pedido de Davi 2× — vale para todo resumo gerado a partir de agora).** `gerar_main.render_capa` filtra qualquer linha meta cujo rótulo contenha "aprofundar"; o Orquestrador não emite mais essa linha. Rodapé identificador apenas na capa ("Davi Sousa — Turma 114" / "(61) 98264-7208 · dpbdes@gmail.com · PIX: dpbdes@gmail.com"). **Proibido no PDF qualquer página:** bloco/prova (P1/P2/P3), número/posição da aula, código de slug, turma, semestre, calendário.
   - **Bloco "Onde aprofundar" — SUSPENSO 2026-07-07 (não vai mais pra capa).** Detalhe histórico do formato antigo em `MEMORY.md`/memória `onde-aprofundar-anking-capa.md`. A exceção de vocabulário Step 1 na capa caiu junto: fora da capa o banimento Step 1/USMLE segue integral (ver `ROLES.md` Redator regra 10 + `precompile-check.py`).
2. **Sumário** (1 página: máx 3 itens por PARTE da E1, descrições 3–5 palavras).
3. **Etapa 1 — texto didático** (intro-box + 3 PARTES + **conclusão integradora obrigatória** — a E1 fecha sempre no `#conclusao-box`, costurando as PARTES em 4 camadas: princípio unificador → mecanismo nuclear → clínica retomada → projeção; ver `ROLES.md` § Redator diretriz 11). **A conclusão VOLTA a ser gate do `precompile-check.py` (CANON 2026-07-03 — reverte a suspensão de 2026-07-01)** — `#conclusao-box` é exigido `>=1` em toda E1. Siglas como footnote no rodapé de cada página.
4. **Resumindo** (1 página) — logo após Conclusão integradora da E1.
5. **Etapa 2** — 30 objetivas, cores por categoria (consolidação/integração/aplicação), sem gabarito inline.
6. **Etapa 3** — 5 discursivas, modelo de resposta ≤100 palavras (Q5 ≤130).
7. **Gabarito consolidado da Etapa 2** (última seção).

(Etapa 4 removida do PDF canônico em 2026-05-22 — banco vira material de calibração, não inclusão direta. Ver § "Banco como calibração". Etapa 5 NEBLIcards permanece em standby.)

## Fluxo Cowork

**Input:** "Tema [UC/Disciplina], slides: [anexo]". Confirmar se ambíguo.

**Processamento:**
1. Ler `guia_editorial_UC1.csv` → profundidade esperada.
2. Ler `banco/indice/banco_slim.json` filtrado por `aula: <slug>` → **calibração** do nível esperado, jargão recorrente, armadilhas históricas. Banco NÃO é material de inclusão no PDF.
3. ORQUESTRADOR roda `extrair_slides.py [slide.pdf] [slug]` → PNGs + `figuras/[tema]/MAPA_CONTEUDO.txt`.
4. ORQUESTRADOR gera Tema Card (Seção A + B + C). Validar antes de redigir.
5. REDATOR-E1 gera `etapa1.typ` + `resumindo.typ`. Cita slides baseado no `MAPA_CONTEUDO`.
6. QUESTIONADOR gera `etapa2.typ` + `etapa3.typ`. Usa banco filtrado por aula como calibração (não como anexo).
6.5 **LEGADO DO RESUMO COMPLETO:** curadoria + loop Card→E1 usados apenas quando Davi solicitar esse pipeline antigo integrado. Não aplicar esta etapa ao `/deck-aula`, que segue seu runbook próprio e mantém E2/E3 suspensas.
7. COMPILADOR roda `gerar_main.py` → compila Typst → audita → move PDF para `resumos-gerados/[SLUG-MAIUSCULO].pdf` apenas se a auditoria passar.

**Recorte slide × tema:** quando o nome da aula for mais estreito/largo que o slide, declarar no Tema Card "Recorte: slide cobre X; tema pedido é Y" e validar antes.

## Figuras e SVGs (resumo — detalhes no redator-e1.md)

- Meta: mínimo 3 imagens por PARTE da E1. Prioridade: imagem do slide do professor.
- **Largura variável 40–80% com análise caso a caso (canônico 2026-05-28).** Default antigo de 65% morreu — vire automatismo. Cada figura recebe largura deliberada conforme **quanto espaço o conteúdo dela merece**: 40–50% para detalhe pontual / ícone esquemático / figura que apoia prosa lateral; 55–65% para figura informativa de peso médio; 70–80% para cadeia multi-passo, mapa orientador de PARTE ou comparativo lado-a-lado que precisa ser legível de longe. Acima de 80% só se a figura **é** o mecanismo (raríssimo). Texto curto + figura pequena: `#figura-lateral`.
- REDATOR consulta `figuras/[tema]/MAPA_CONTEUDO.txt` antes de referenciar qualquer `slide-XX.png`.
- Caminho canônico: prefixo `/` (`image("/figuras/glicose/slide-08.png")`).
- Cadeia multi-passo enzimática (≥5 reações) = figura obrigatória.
- **Mapas mentais suspensos.** Helpers `#mapa-parte` (SVG, suspenso 2026-05-19) e `#mindmap-fechamento` (fechamento da E1, suspenso 2026-05-28) proibidos. Ambos são no-op silencioso no template. E1 nova termina na **conclusão integradora obrigatória** (canônico 2026-07-03 — reverte a opcionalidade de 2026-06-24/07-01); `#resumindo-page(...)` vem logo depois.
- **Bibliotecas externas de figura (canônico 2026-05-30):** quando o slide do professor não cobre bem um conceito visual (anatomia detalhada, via metabólica não vetorizada, esquema de organela), ordem recomendada de fontes: **SMART Servier Medical Art** (anatomia/farmacologia/clínica, CC-BY, PowerPoint editável) > **NIH BIOART** (celular/molecular, **domínio público**, sem atribuição) > **Reactome icon library** (vias metabólicas, CC-BY) > **SciDraw** (pontual — neurônio estilizado, figura "de pesquisa"; viés neuro-experimental). **SVG continua caso especial** e exige cuidado (ver `feedback_figuras_produtivas_svg_cuidado` no memory pessoal). Atribuição CC-BY consolidada na página de créditos no fim do PDF (helper `creditos-figuras` a criar via `frontend-design` na primeira apostila que usar).
- **Relatório auditável de figuras no fechamento da E1 (canônico 2026-05-28).** Junto do relatório de ratio Q01–Q30 (canônico 2026-05-29), a sessão principal entrega uma tabela curta com **uma linha por figura usada**:

  | Figura | PARTE | Origem (slide-XX / externa) | Mecanismo que carrega | Largura |
  |---|---|---|---|---|

  Custo ~2 minutos no fim, força a verbalizar "essa figura existe porque…" para cada uma — figura sem mecanismo verbalizável é descartada antes do auditor. Mesmo princípio operacional do ratio de distratoras: decisão tácita vira artefato explícito. Não é gate hard, é convite auditável — mas a tabela é obrigatória no relatório de fechamento.

## Bullets e tabelas

Default = prosa expositiva contínua. Bullets/tabelas só em 3 casos: (a) comparativos com 3+ dimensões que se cruzam; (b) cronologias temporais com escala numérica precisa; (c) critérios diagnósticos / regras clínicas com itens discretos. Catálogo de família/isoforma (GLUTs, SGLTs, hexoquinases, receptores adrenérgicos) cai no caso (a) — preferir `table()` nativo com header navy.

**Gatilhos detalhados (canônico 2026-06-24, itens 21/33/34/40):** a pesquisa em Mankiw + Poliedro (`arquivos-trabalho/pesquisa-didatica/ACHADOS-topico-tabela.md`) refinou *quando* quebrar a prosa, virando a Categoria 18 do `EXEMPLARES.md` ("Quando quebrar a prosa"). Três gatilhos de tópico: **(1)** catálogo de tipos discretos, cada um com 1 traço definidor (cromossomos metacêntrico/submetacêntrico…); **(2)** cadeia de premissas de um argumento lógico — o "estilo cursinho" do item 33, cada passo uma proposição independente; **(3)** resumo de fechamento em frase completa (Resumindo). Tabela: cruzamento de 2+ dimensões que se referenciam. Os exemplares concretos governam a aplicação — em conflito com esta linha, o EXEMPLARES vence.

## Footnotes e siglas

- **Termos técnicos densos:** `#termo-nota[acetilcolina][principal neurotransmissor da JNM]` na 1ª aparição. Alvo: 5–10 por resumo.
- **Siglas:** `#sigla("ATP", [adenosina trifosfato — moeda energética])` na 1ª aparição. Sem teto. Subsequentes não geram footnote.
- Glossário de siglas em página dedicada: removido do pipeline. `#glossario-siglas-page()` é no-op silencioso.

## Resumindo

1–2 páginas (canônico 2026-05-20 após #27 v2 — Davi flexibilizou), 2 colunas, banner gold. 8–12 seções, ~25–35 palavras cada, ordenadas por relevância clínica decrescente. Frases concretas com sujeito+verbo+complemento — nunca aglomerado de siglas. Caber em 1 página ainda é o ideal; 2 páginas é aceitável quando o tema é denso (Krebs, gliconeogênese, transmissão sináptica), evitando comprimir leading/spacing de forma agressiva.

REDATOR-E1 entrega `resumindo.typ` junto da Etapa 1. Assinatura: `#resumindo-page(((titulo, corpo), (titulo, corpo), ...))` — tupla dupla por seção.

## Verificação do PDF (resumo — detalhes no compilador.md)

- `precompile-check.py` (9 validações) antes de compilar. Exit 0 obrigatório.
- `auditar_pdf.py` antes de mover: acentuação ≥1,5%, paths `/figuras/` existem, siglas sem duplicata, Merriweather embarcado.
- **Validação visual obrigatória** (canônico 2026-05-18): abrir o PDF e conferir Resumindo em 1 página, figuras sem cortes, espaço em branco, cores das categorias, sumário em 1 página.

## Banco como calibração (canônico 2026-05-22)

O banco deixou de ser anexo do PDF (E4 foi removida). Agora é **régua de calibração** consultada pelos subagentes durante a redação, e fornecedor de **artefato avulso sob demanda**.

**Uso durante a geração de um resumo:**
- QUESTIONADOR filtra `banco_slim.json` por `aula: <slug>` antes de redigir a E2. Lê `tags`, `conceito_central`, `armadilha`, `nivel` das questões classificadas para informar profundidade, vocabulário e distratoras. Nada vai pro PDF.
- ORQUESTRADOR usa o campo `armadilha` das questões classificadas para alimentar o Mapa de Confusões antes de delegar.

**Quando Davi pedir "questões antigas de [tema]" explicitamente:**
- ORQUESTRADOR filtra o slim por `aula: <slug>` e entrega artefato avulso em `arquivos-trabalho/questoes-de-prova/<slug>.md` (ou imprime no chat se for curto). Nunca colado no PDF do resumo.

**Schema operacional:**
- Canônico: `banco/questoes/q-XXXX.md` (413+ questões com frontmatter YAML).
- Slim: `banco/indice/banco_slim.json` para classificação (não ler `.md` completo).
- Aulas: `banco/aulas_uc01.yml` (41 aulas) + `banco/aulas_uc02.yml` (31 aulas, criado 2026-05-22).
- Classificador: `banco/classifier.py` (keyword + sinônimos curados) — gera `banco/indice/classificacao_proposta.json` para revisão humana antes de gravar.
- Atualização: ingerir → classificar via `classifier.py` → revisão → aplicar → regenerar slim.

## Mapa de Confusões

Artefato versionado em `mapa-confusoes/<slug>.md`. QUESTIONADOR consulta antes de redigir distratoras e atualiza ao fim. Estrutura: ≥4 confusões por subtópico da E1, cada uma com nome curto + descrição mecanística do erro + origem (banco NEBLI #ID | livro-texto | armadilha clínica).

## Geração 20

Pipeline maduro desde 2026-05-14. Geração 20 ✅ encerrada (30/30 entre 2026-05-14 e 2026-05-21) — ver `MEMORY.md` § Active Projects. Modo "um resumo por vez" continua válido para gerações futuras: orquestrador puxa o próximo quando Davi diz "continua a operação"; resumo avulso a qualquer momento pausa e retoma.

Princípios: (1) prosa expositiva é o motor; (2) entender processos > decorar nomes; (3) taxonomia E2 parametrizada pelo guia editorial; (4) Aplicação calibrada para 1º semestre com texto motivador rico se a clínica subir.

## Atualização de regras canônicas

Quando uma regra muda (pós-faxina 2026-05-29):
1. Atualizar `CLAUDE.md` se for prescritiva genérica, `MEMORY.md` § Core Memory se for factual, `ERROS.md` se for armadilha recorrente / feedback de processo, `ROLES.md` se afeta papel específico no pipeline.
2. Entrada curta em `MEMORY.md` § Histórico de decisões canônicas na mesma sessão (sem entrada → sem canonização). Para auditoria detalhada do histórico anterior a 2026-05-22, acessar `backups/pre-faxina-2026-05-29/raiz/CHANGELOG_CLAUDE.md` via Read explícito.
3. Mover qualquer plano relacionado para `backups/planos-historicos/` quando ele virar histórico.
4. Se mudou frontmatter de um papel (modelo, tools, description), atualizar o stub em `.claude/agents/`.

## Checklist antes de mandar tema

- Slide em anexo (PDF ou foto).
- Disciplina clara (UC1, UC2, Fisiologia, etc).
- Slug da aula: confirmar qual entrada de `banco/aulas_uc01.yml` ou `banco/aulas_uc02.yml` o tema mapeia. Se ambíguo, ORQUESTRADOR pergunta no Tema Card antes de seguir.

## Considerações finais

- Ajustar a profundidade da explicação ao contexto da questão e ao grau de domínio do aluno; **presumir baixo + dificuldade real** (canônico 2026-05-25). Aluno está com dificuldade; o resumo é a ferramenta dele para sair dessa.
- Conciso, mas completo.
- Sem listas ou bullets no corpo do resumo (exceção: 3 casos da § Bullets e tabelas).
- Atualizar `MEMORY.md` § Pendências abertas antes de executar mudança canônica.
- Em conflito entre exemplar concreto e regra abstrata, **exemplar vence**.

### Três regras editoriais canônicas (atualizadas 2026-05-29)

Valem para **todo resumo NEBLI**, somando-se às demais:

1. **Pergunta âncora / pergunta retórica / pergunta ingênua BANIDAS como recurso editorial** (canônico 2026-05-29 — substitui o antigo "teto de 3 perguntas ingênuas" de 2026-05-28). Abertura de subtópico é **afirmação direta + mecanismo**. Os 5 registros canônicos de abertura: enquadramento, integração-anterior, integração-posterior, analogia concreta, ponto-de-quebra. Pergunta retórica quebra a voz expositiva — não usar. Auto-check antes de fechar a E1: `grep -cE '\?$' typst-build/etapa1.typ` — perguntas terminais devem ser raríssimas. Razão: Davi pediu remoção total do recurso após sintomas reincidentes mesmo com o teto de 3.
2. **Fluidez vence rigidez de regras.** Regras canônicas (cotas de figuras/termo-notas, 15 diretrizes do § Redator em `ROLES.md`, etc.) são **default**, não gate hard da redação. Em conflito entre cumprir checklist e manter prosa fluida de monitor, deixa de cumprir e segue o fluxo — anota a quebra no relatório. Meta-pergunta de fechamento de PARTE: "a leitura flui em voz alta?". Gates hard ficam só nos técnicos (precompile-check, auditar_pdf, paridade Q01–Q30, vocabulário banido).
3. **Prosa fluida, nunca empilhamento de siglas (canônico 2026-05-29).** A explicação é **prosa**, com **foco extremo na fluidez**. Erro comum a evitar: jogar uma rajada de siglas (ATP, NADH, FADH₂, CoA, GTP…) coladas umas nas outras como se isso fosse explicação. Sigla entra dentro de uma frase com sujeito + verbo + complemento que explica o que ela faz no mecanismo — nunca como aglomerado. Se um parágrafo virou catálogo de siglas, reescrever em prosa contínua antes de fechar. Vale para E1, Resumindo, gabarito de E2 e modelo de resposta de E3.

(Regras editoriais históricas: "figura ancorada na prosa" foi removida em 2026-05-28; "teto de 3 perguntas ingênuas" foi substituído pela proibição total em 2026-05-29. Detalhes em `MEMORY.md` § Histórico.)

### O que evitar a todo custo

- Robótico ou lacônico — sua função é explicar em prosa expositiva fluida, como monitor ensinando.
- Apresentar cálculos sem explicar o raciocínio.
- Listas no corpo do resumo (exceto os 3 casos canônicos).
- Considerar conhecimento prévio alto — partir de ensino médio + meses.
