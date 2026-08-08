# Estrutura do deck-mestre NEBLI

## Árvore canônica

`NEBLI::<UC>::<Prova>::<Matéria>::<Aula>`

Exemplo: `NEBLI::UC03::P1::Radiologia::Ferramentas do diagnóstico radiológico`.

Uma aula que cai em várias provas mora apenas na **primeira prova**. A hierarquia serve tanto ao estudo longitudinal quanto ao cram sem duplicar cards.

## Fontes

AnKing e decks externos ficam intocados. Cards aprovados são **copiados** para a folha NEBLI e mantêm tag `NEBLI::<slug>` para rastreabilidade. O manifesto da aula, não a tag isolada, decide o que pode entrar.

## Fila de novos

Dentro da aula, `nuclear` vem antes de `supporting`. Entre aulas, seguir a ordem do cronograma quando possível. Não usar quantidade fixa por subtópico para fabricar uma ordem.

## Dois modos, um histórico

- **Rotina:** estudar `NEBLI`, 25 novos/dia + todas as revisões devidas pelo FSRS.
- **Pré-prova:** estudar `NEBLI::<UC>::<Prova>` e elevar temporariamente o limite daquele subdeck até cobrir o restante da prova. Depois, restaurar o normal.

Não exportar/importar uma segunda cópia para cram: isso fragmenta scheduling e duplica esforço.
