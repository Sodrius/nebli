# estrutura-deck-mestre.md — como o deck NEBLI espelha a FMUSP

> Plano de organização do deck Anki para (a) refletir a estrutura FMUSP (UC › componente › aula) que o Davi já usa no Drive com as apostilas, (b) permitir "revisar só a aula X" e (c) manter o fluxo "deck geralzão, 15 novos/dia". Criado 2026-07-10; a decisão A vs B abaixo estava marcada "a pensar" pelo Davi.

## Decisão: deck-AnKing puro vs deck-NEBLI estruturado

**Modelo A — só dessuspender no deck AnKing original.** Cards ficam na árvore `#AK_Step1_v12::...`; dessuspende por tag; estuda o deck AnKing gigante filtrado.
- ✅ zero movimentação de notas; à prova de update de deck compartilhado.
- ❌ não dá "revisar só a aula X" como deck próprio; não espelha a FMUSP; a ordem é a do AnKing, não a do teu cronograma.

**Modelo B — puxar os curados para um deck NEBLI estruturado (recomendado).** `changeDeck` das notas curadas para uma árvore que espelha a FMUSP.
- ✅ espelha o Drive; cada aula vira um subdeck estudável isolado; "deck geralzão" = o topo `NEBLI::` com 15 novos/dia; ordem controlada pelo cronograma.
- ❌ move a nota para fora da árvore AnKing (uma nota mora numa deck só). Mitigação: `card_origem` já é gravado em `<slug>-curado.json` → reversível (dá pra devolver à árvore AnKing). Se o AnKing publicar update, reimporta na árvore original e re-puxa por tag.

**Recomendação:** Modelo B. O ganho de ter o deck na tua estrutura e poder revisar aula-a-aula supera o custo, e a reversibilidade via `card_origem` cobre o risco de update. A tag `NEBLI::<slug>` continua em todas as notas (é ela que o monitor e a cobertura usam) — o deck é a *casa*, a tag é o *rótulo de aula*.

## Árvore de decks proposta

```
NEBLI                                   ← "deck geralzão": 15 novos/dia vêm daqui
└── UC02
    └── 03_Embriologia                  ← componente
        ├── P3-05_gametogenese-fertilizacao
        └── P3-06_gastrulacao-neurulacao ← deck-aula: revisar só isto quando quiser
```

- **Prefixo numérico** (`P3-06_`) força a ordem cronológica (Anki ordena subdecks alfabeticamente). O índice sai do cronograma da UC (`banco/aulas_uc02.yml`) — mesmo princípio da memória [[ordem-cards-cronograma-uc2]], agora aplicado à hierarquia de deck, não só à new-queue.
- **Componente** numerado (`03_Embriologia`) idem, na ordem em que o Davi cursa.
- Estudar o **topo `NEBLI`** = mistura tudo, 15 novos/dia na ordem do cronograma. Estudar um **subdeck** = só aquela aula.

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
- **Dia normal:** abre `NEBLI`, faz 15 novos + revisões, na ordem do cronograma.
- **Revisar uma aula:** abre `NEBLI::UC02::03_Embriologia::P3-06_gastrulacao-neurulacao`, revisa só ela — mesma estrutura do Drive.
