# sobre_mim.md — Davi Sousa, aluno FMUSP

> **Função:** arquivo vivo com contexto pessoal de estudo do Davi. **Carrega em toda sessão NEBLI**, como `CLAUDE.md`/`MEMORY.md`/`ERROS.md`/`ROLES.md`. Fatos que mudam com o tempo (semestre em curso, decks/UCs ativos, objetivos de médio prazo) vivem aqui — é o "raio-X" do momento pra decisão editorial e de curadoria.
>
> **Diferença de escopo:** `MEMORY.md § Active Projects` cobre estado do repositório e do pipeline; `sobre_mim.md` cobre o **estudante e seus objetivos**. Um informa "o que o NEBLI está fazendo agora"; o outro informa "para quem, com qual horizonte, dentro de qual organização".

---

## Identidade e contato

- **Nome:** Davi Sousa
- **Turma:** 114 (FMUSP), Turma B na subdivisão A/B do 2º ano
- **Email:** dpbdes@gmail.com
- **Telefone:** (61) 98264-7208 · PIX: dpbdes@gmail.com

---

## Onde o material mora (fontes canônicas, ler antes de qualquer decisão de organização)

- **Pasta-raiz do Drive (Medicina):** `https://drive.google.com/drive/folders/1D9cPEn40EQl7sKx1z8KIZZ7lzBqFa5_8`
  - ID: `1D9cPEn40EQl7sKx1z8KIZZ7lzBqFa5_8`
  - Dono: `dpbdes@gmail.com` · Filhos canônicos: `Cronogramas/`, `Resumos e exercícios/`, `Para não compartilhar/`
  - Estrutura de upload de resumo/slide/`.apkg` em `referencias-externas/DRIVE-ESTRUTURA.md`; UCs novas replicam o padrão que já existe pra UC01/UC02.
- **Planilha mestra (fonte-verdade viva do cronograma):** `https://docs.google.com/spreadsheets/d/1AJx4unhfGmEl_4dqhO7OTpVhZ0TFAR5QgTorfmxSess/edit`
  - ID: `1AJx4unhfGmEl_4dqhO7OTpVhZ0TFAR5QgTorfmxSess` · Nome: `2026 - Matérias e Mês`
  - Cobre **UC03 · UC04 · UC07 · UC08 · UC16 · UC19 · UC21-DIC · UC30** numa grade única (2 abas: por-UC + mensal).
  - Ler via `mcp__Google_Drive__read_file_content` **antes de gerar resumo ou canonizar mudança de calendário**. Digests em `cronogramas/*.md` são snapshots — quando divergir da planilha, planilha vence.
- **Moodle FMUSP (`edisciplinas.usp.br`):** contém o material da UC03 e provavelmente outras. **Fora do meu alcance direto** (SSO USP). Fluxo por ora: Davi baixa o material no tablet, sobe pra pasta correspondente do Drive, eu leio via MCP. Automação (`moodle-sync.py` no PC do Davi) está no backlog.

---

## Como o semestre está organizado (2º semestre 2026 — canônico 2026-08-07)

Cursando **três UCs em paralelo**:

| UC | Assunto | Provas | Fonte-verdade |
|---|---|---|---|
| **UC03** | Diagnóstico integrado (RD · PT · IM · BM · MB) + Grand Rounds | P1 28/08 · P2 02/10 · P3 06/11 · P4 04/12 | `cronogramas/uc03-2026.md` |
| **UC-16 (Ciclo da Vida I)** | Pediatria + Geriatria | prova final única 28-29/09 | `cronogramas/ciclo-da-vida-i-uc16-2026.md` |
| **UC-8 (Digestório · Med5043)** | Anatomia · Histologia (BioTec II) · Fisiologia · Biocel/Embrio | P1 05/10 · P2 30/11 | `cronogramas/digestorio-uc8-med5043-2026.md` |

Do 1º semestre restam **UC01** e **UC02** (ciências básicas, com banco de questões em `banco/`). UC03/UC-16/UC-8 **não têm banco** — resumos usam slide + bibliografia + AnKing.

**No horizonte:** UC04 · UC07 · UC19 · UC21-DIC · UC30 (todas na planilha mestra).

---

## Como quero a estrutura de decks Anki (canônica; espelhada em `flashcards/estrutura-deck-mestre.md` e `FLASHCARDS.md` § Estrutura)

Árvore única, aninhada, um card mora numa aula só:

```
NEBLI                        ← deck-mestre "geralzão" (retenção longa; 15 novos/dia)
└── UC<NN>                   ← ex.: UC03, UC02
    └── P<N>                 ← prova (P1, P2, P3, P4) — PRIMEIRA prova em que a aula cai
        └── <Matéria>        ← componente (Bioquímica, Anatomia, Imunologia, Patologia...)
            └── <Aula>       ← nome curto da aula = mesmo nome usado no Drive e no PDF
```

**Regras operacionais:**

- **Uma aula = um deck-aula** (folha da árvore).
- **A aula fica na PRIMEIRA prova em que aparece.** Quando o tema cai em >1 prova (ex.: "Ferramentas do diagnóstico radiológico" da UC03 marcada como `P1;P2;P3;P4`), o deck-aula mora só em `P1` — as demais provas encontram esse conteúdo estudando o pai `NEBLI::UC03::` (subdeck aninhado inclui tudo abaixo). Sem duplicar card, sem espalhar em múltiplos lugares.
- **Dentro da prova, separação por matéria/componente.** Fica fácil abrir `NEBLI::UC03::P1::Imunologia::` pra cravar só imuno na véspera.
- **Nome canônico da aula = mesmo nome curto e simples do Drive e do PDF** (ex.: `Ferramentas do diagnóstico radiológico`). Bate em três lugares: pasta no Drive, `.apkg` (`<Aula curta>.apkg`), PDF (`<Aula curta> - Etapas 1 a 3 - <sigla prof>.pdf`).
- **AnKing intocado.** Fica 100% suspenso como referência; o card de estudo é sempre uma cópia com tudo (campos, imagem, crédito, tags) para a árvore `NEBLI::`.
- **Ritmo (canon 2026-08-08):** **25 novos/dia no topo `NEBLI`** (era 15; Davi subiu no início do 2º sem porque quer atacar mais volume) + **1 novo/dia no subdeck `NEBLI::Etimologia`** (deck dedicado a raízes/afixos médicos — construção longitudinal separada, ritmo lento e constante). Total efetivo: 26 novos/dia. Cram por prova via filtered deck (`planejar_modo_prova.py`) — devidos/erros da prova rescheduling ligado; novos por urgência preview, rescheduling desligado.
- **Bandeiras (loop estudo → curadoria):** vermelha (Ctrl+1) = suspende + email dessuspende com 2 parágrafos NEBLI; laranja = "esse card pertence?" → julga ancorado/fora; verde = exemplar (vira `flashcards/EXEMPLARES-CARDS.md`).

**Uso resultante:**
- **Dia normal:** abre `NEBLI`, faz 15 novos + revisões devidas na ordem do cronograma. Retenção longa contínua, sem esforço curatorial.
- **Revisar uma matéria antes da prova:** abre `NEBLI::UC03::P1::Imunologia::` — só o que interessa. Todos os cards das aulas de imuno cobradas em P1.
- **Cram total pré-prova:** abre `NEBLI::UC03::P1` — tudo que cai na P1, todas as matérias.

---

## Objetivos de médio prazo (norte editorial e curatorial)

Duas metas que orientam **toda decisão de profundidade, seleção de card e escopo de aprofundamento**:

1. **FMUSP — passar bem em todas as UCs.** Retenção longa do que a faculdade cobra, sem trocar a base do próximo semestre pela nota do atual. Prova de UC vence a decisão de escopo local do resumo.
2. **Step 1 USMLE — construir base longitudinal desde o ciclo básico.** Não estudar do zero na véspera. Cada mecanismo básico da FMUSP é cobrado no Step 1 numa profundidade específica; o deck acumula essa profundidade **quando ela ancora numa aula real** (regra R18 do `FLASHCARDS.md` — camada Step 1 nunca aparece primeiro no deck, entra pela E1 primeiro).
3. **Residência HC (norte de longo prazo).** Ponte clínica pequena e estável — estrutura/alteração → mecanismo → achado discriminante. No ciclo básico entra mecanismo + localização + sinal/lab esperado + morfologia funcional. Ficam de fora conduta, dose, guideline, staging — coisas de Step 2/internato.

**Filtro em conflito:** quando ensinar bem a FMUSP conflita com incluir aprofundamento Step 1, **FMUSP vence a decisão de O QUE entra** (regra-mestra: slide regula escopo, AnKing/bibliografia regula até que profundidade). Step 1 nunca é razão pra abrir um tópico que a aula da FMUSP não abriu.

**Vocabulário Step 1/USMLE fica banido no PDF** (verificado pelo `precompile-check.py`). Aprofundamento entra como mecanismo puro, gancho clínico entra como cenário puro — nunca "isso cai no Step 1" impresso no material.

---

## O que evitar (repete o que o Davi já disse em vários lugares, condensado aqui)

- Robótico, lacônico, catálogo de siglas — sua função é explicar em prosa expositiva fluida, como monitor.
- Presumir que o Davi "já sabe" um pré-requisito. Presumir conhecimento **baixo** e dificuldade real com o assunto.
- Pergunta âncora / retórica / ingênua como recurso de abertura (banido 2026-05-29).
- Cotas rígidas engessando a prosa. Em conflito, **fluidez vence** (F7).
- Card órfão no deck (conceito que a E1 não explica) — gate absoluto.
- Card autoral quando o AnKing/externos cobrem — autoral é último recurso, só pra lacuna tipo-a genuína.

---

## Notas de uso deste arquivo

- Editar aqui quando **um fato sobre o estudo do Davi mudar** (semestre novo, meta nova, mudança de organização de deck, nova UC que entra em curso, mudança de contato). Não usar pra armazenar pendência de projeto (isso vive em `MEMORY.md`).
- Data de última revisão canônica: **2026-08-07**.
