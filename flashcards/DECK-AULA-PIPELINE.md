# Pipeline canônico de deck-aula

Este é o caminho operacional. A política editorial está em `FLASHCARDS.md`.

## 1. E1 primeiro

Redigir a E1-base a partir do material da aula. O deck nunca ensina conteúdo pela primeira vez.

## 2. Inventário e decisão de card

Rodar `gerar_checklist.py <slug>` **antes da E2**. O script semeia candidatos a conceito, mas não decide o que merece card.

Revisar cada linha e trocar `review` por:

- `nuclear`: precisa ser lembrado ativamente; card obrigatório;
- `supporting`: card apenas se houver retrieval target distinto e útil;
- `no_card`: fica na E1, sem custo de Anki.

Fundir linhas redundantes. Negrito, `#termo-nota`, sigla e tamanho do subtópico são pistas de extração, não prova de card-worthiness.

## 3. Curar pela ordem de fontes

Para cada `nuclear` e `supporting` selecionado:

1. buscar AnKing;
2. ler os candidatos e aprovar só os semanticamente exatos;
3. se faltar, buscar os decks externos adequados;
4. só então criar NEBLIcard autoral para a lacuna restante.

`curar_anking_v2.py` gera **candidatos**, não uma seleção final automática. O curador registra keep/drop e o conceito exato. Um score de forma nunca substitui esse julgamento.

Se um bom card revelar um aprofundamento pequeno e imediatamente adjacente, incorporar e explicar esse conteúdo na E1 antes de aprovar o card. Se exigir outra aula/pré-requisitos laterais, drop/defer. A corrida normal não materializa parking off-aula; `--emit-parking` existe só para investigação deliberada.

## 4. Fechar a matriz

O manifesto `matriz-deck-aula-<slug>.json` é a lista de admissão:

- `e1_inventory`: todos os conceitos inventariados, com `card_decision`;
- `facts`: somente conceitos que realmente receberão card;
- cada rota: `anking | other_deck | own`, `card_refs`, `retrieval_target`, qualidade e justificativa;
- autoral: `prior_search.anking=insufficient` e `prior_search.other_decks=insufficient` + rejeição dos candidatos;
- `load_profile`: porte da aula e estimativa real de cards;
- visual obrigatório: plano/ativo aprovado.

`validate_lesson_coverage.py` exige cobertura de todos os `nuclear`, mas permite que `supporting` seja dispensado e que `no_card` permaneça apenas na E1.

## 5. Montar somente o que foi aprovado

Rodar:

`python flashcards/scripts/montar_deck_aula.py --slug <slug> --deck "NEBLI::<UC>::<Prova>::<Matéria>::<Aula>" --manifest arquivos-trabalho/matriz-deck-aula-<slug>.json`

O script copia das fontes apenas cards cujas referências constam do manifesto. A presença de uma tag antiga `NEBLI::<slug>` não basta.

**Sem AnkiConnect:** materializar o mesmo conjunto aprovado em `flashcards/cards-nebli/<slug>.json` (preservando `source`/tags de proveniência), rodar `empacotar_apkg.py <slug>` e usar o `.apkg` como artefato final. Não rebaixar a curadoria só porque a montagem é offline.

## 6. Hard gate

Antes de E2/PDF/.apkg final:

Com AnkiConnect: `python flashcards/scripts/gate_deck_aula_completo.py ... --verify-anki`.

Offline: `python flashcards/scripts/gate_deck_aula_completo.py ... --verify-apkg "resumos-gerados/<Aula>.apkg"`.

Bloqueia quando:

- algum `nuclear` está sem card;
- um `no_card` aparece roteado;
- existe card sem âncora E1;
- autoral pulou AnKing/outros decks;
- retrieval target está duplicado;
- visual `required` não está aprovado;
- volume >60 não passou revisão explícita de redundância;
- o deck real não contém os `card_refs` aprovados ou o `.apkg` traz note que não consta do manifesto.

Faixas ~15–25 / ~25–40 / ~35–55 para pequena/média/grande são **guardrails**, não quotas. Ultrapassar a faixa gera revisão, não criação de cards para “preencher” uma meta.

## 7. Uso

Normal: topo `NEBLI`, 25 novos/dia + FSRS. Cram: abrir o subdeck da prova e acelerar temporariamente o restante daquela prova; depois voltar ao preset normal. O agendamento e o histórico são os mesmos.
