# estrutura-deck-mestre.md — como o deck NEBLI espelha a FMUSP

> Plano de organização do deck Anki para (a) refletir a estrutura FMUSP (UC › prova › matéria › aula) que o Davi já usa no Drive com as apostilas, (b) permitir "revisar só a aula X" e (c) manter o fluxo "deck geralzão, 25 novos/dia (+ 1 em NEBLI::Etimologia, canon 2026-08-08)".
>
> **Estado (2026-08-07):** canonizado como **Modelo B** desde 2026-07-12. A regra da **primeira prova** (aula cobrada em >1 prova mora só na primeira) foi explicitada em 2026-08-07 a pedido do Davi. Este documento é o **plano operacional detalhado** que o `FLASHCARDS.md` § Estrutura resume; em conflito de detalhe, este vence.

## Decisão: deck-AnKing puro vs deck-NEBLI estruturado

**Modelo A — só dessuspender no deck AnKing original.** Cards ficam na árvore `#AK_Step1_v12::...`; dessuspende por tag; estuda o deck AnKing gigante filtrado.
- ✅ zero movimentação de notas; à prova de update de deck compartilhado.
- ❌ não dá "revisar só a aula X" como deck próprio; não espelha a FMUSP; a ordem é a do AnKing, não a do teu cronograma.

**Modelo B — puxar os curados para um deck NEBLI estruturado (recomendado).** `changeDeck` das notas curadas para uma árvore que espelha a FMUSP.
- ✅ espelha o Drive; cada aula vira um subdeck estudável isolado; "deck geralzão" = o topo `NEBLI::` com 25 novos/dia (+ 1 em NEBLI::Etimologia, canon 2026-08-08); ordem controlada pelo cronograma.
- ❌ move a nota para fora da árvore AnKing (uma nota mora numa deck só). Mitigação: `card_origem` já é gravado em `<slug>-curado.json` → reversível (dá pra devolver à árvore AnKing). Se o AnKing publicar update, reimporta na árvore original e re-puxa por tag.

**Recomendação:** Modelo B. O ganho de ter o deck na tua estrutura e poder revisar aula-a-aula supera o custo, e a reversibilidade via `card_origem` cobre o risco de update. A tag `NEBLI::<slug>` continua em todas as notas (é ela que o monitor e a cobertura usam) — o deck é a *casa*, a tag é o *rótulo de aula*.

## Árvore de decks canônica (2026-08-07)

```
NEBLI                                          ← "deck geralzão": 25 novos/dia (+ 1 em NEBLI::Etimologia, canon 2026-08-08) vêm daqui
└── UC03                                       ← UC
    └── P1                                     ← PROVA (P1, P2, P3, P4)
        ├── Radiologia                         ← MATÉRIA/componente
        │   └── Ferramentas do diagn. radiológico  ← AULA (deck-aula, folha)
        ├── Imunologia
        │   ├── Organização do sistema imune
        │   └── MHC, processamento e apresentação de antígenos
        └── Patologia
            ├── Necrose e apoptose
            └── Acúmulos e adaptação celular
```

Ordem canônica dos níveis: **UC → Prova → Matéria → Aula.**

**Regra da PRIMEIRA prova (canon 2026-08-07):** quando uma aula cai em mais de uma prova (ex.: "Ferramentas do diagn. radiológico" está marcada `P1;P2;P3;P4` na planilha), o deck-aula vive **APENAS** em `NEBLI::UC03::P1::Radiologia::Ferramentas...`. Estudar `NEBLI::UC03::` (topo da UC) inclui essa aula em qualquer momento do semestre por aninhamento. Sem duplicata, sem espalhamento.

**Naming:**
- **Aula** = nome curto e simples, mesmo que a pasta do Drive e o PDF (`<Aula curta> - Etapas 1 a 3 - <sigla prof>.pdf`) e o `.apkg` (`<Aula curta>.apkg`).
- **Matéria/componente** = nome legível (`Bioquímica`, `Anatomia`, `Imunologia`), sem prefixo numérico. Ordem alfabética dentro da prova é aceitável — dentro de uma prova são poucas matérias e o Davi lê pelo nome.
- **Prova** = `P1`, `P2`, `P3`, `P4` (ordem alfabética coincide com a cronológica).
- **UC** = `UC01`, `UC02`, `UC03`, `UC-16` (usando o rótulo oficial). Zero-padding quando ajudar a ordenação (UC01, não UC1) — mas UCs de 2 dígitos (UC-16) já ordenam sozinhas.

**Uso resultante:**
- **Estudar o topo `NEBLI`** = mistura tudo, 25 novos/dia (+ 1 em NEBLI::Etimologia, canon 2026-08-08) na ordem do cronograma. Retenção longa contínua.
- **Estudar `NEBLI::UC03::P1`** = tudo que cai na P1 da UC03 (todas as matérias). Cram pré-prova.
- **Estudar `NEBLI::UC03::P1::Imunologia`** = só imuno cobrada em P1. Cram matéria-a-matéria.
- **Estudar deck-aula folha** = revisar aquela aula específica.

## Ordem dos cards DENTRO de um deck-aula

Dois níveis de ordenação:
1. **Entre aulas** (qual aula aparece primeiro no deck geral): posição da new-queue segue a data da aula no cronograma — já resolvido pelo `reposicionar` (memória [[reposicionar-cards-curados-frente-fila]] + [[ordem-cards-cronograma-uc2]]).
2. **Dentro da aula** (ordem dos cards de uma mesma aula): seguir a **ordem dos subtópicos da E1** (1.1 → 3.3), para o card reforçar na sequência em que o Davi leu o resumo. Implementar gravando `due` crescente na ordem do `conceito_por_nota` (que já carrega o índice do subtópico, ex.: "1.1/1.3...", "2.4...", "3.3...").

## Implicações para os scripts (quando migrar para Modelo B)
- `aplicar_curadoria_anking.py`: além de marcar tag + dessuspender, fazer `changeDeck` para `NEBLI::UCxx::NN_Componente::PX-NN_slug`. Criar a árvore se não existir (AnkiConnect `createDeck`).
- Derivar o caminho do deck de `banco/aulas_ucNN.yml` (UC, componente, índice cronológico) + slug.
- `reposicionar`: ordenar `due` por (índice-de-aula, índice-de-subtópico).
- Reversão: `card_origem` no curado.json permite `changeDeck` de volta à árvore AnKing.

## Fluxo de estudo resultante (o que o Davi quer)
- **Dia normal:** abre `NEBLI`, faz 25 novos + 1 etimologia + revisões, na ordem do cronograma.
- **Revisar uma aula:** abre `NEBLI::UC02::03_Embriologia::P3-06_gastrulacao-neurulacao`, revisa só ela — mesma estrutura do Drive.
