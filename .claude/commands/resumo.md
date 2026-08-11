---
description: Gera a E1 e o deck-aula Anki completo, visual e auditado
argument-hint: <slug> <slide.pdf> [UC] [Prova] [Componente] [Nome curto]
---

# /resumo — pipeline E1 + deck-aula

Argumentos: $ARGUMENTS

A **sessão principal executa todo o trabalho**. Não delegue redação, curadoria,
aprofundamento, visual, autoria ou montagem. Agentes só podem ser chamados após
existirem artefatos completos, em modo revisor e somente leitura.

## 0. Carregar o canônico

Leia `CLAUDE.md`, `MEMORY.md`, `ERROS.md`, `docs/canon/PIPELINE-E1-DECK.md`,
`docs/canon/ANKIDROID-COMPANION.md` e os demais arquivos canônicos. Leia
`config/pipeline.json` e confirme:

- `pipeline_version=e1-deck-v5`;
- backend preferido `ankidroid`;
- manifest `nebli-ankidroid-lesson-v2`;
- E2, E3 e RemNote desligados;
- 25 novos/dia;
- teto de cards, cloze 1/2/3 palavras e IO multi-rótulo `hide_all_guess_all`.

Nunca leia `docs/legacy/` durante corrida normal.

## 1. Entrada e checkpoint

Resolva slug, slide, UC, prova, componente e nome curto. Use cronogramas quando
possível; pergunte apenas se a ambiguidade alterar o produto. Crie
`arquivos-trabalho/<slug>/CHECKPOINT.md` com fase, fontes, decisões, pendências e
próximo passo literal. Atualize após cada fase.

## 2. Fontes e contrato inicial

Extraia slides e objetivos. Crie
`arquivos-trabalho/<slug>/contrato-cobertura.json` a partir do schema canônico.
Registre cada conceito com nome PT/EN, subtópico, origem, importância, aliases e
necessidade visual. Classifique o porte, proponha `card_budget.hard_max` e congele
o teto antes da seleção. Slides/objetivos definem o escopo.

## 3. E1 rascunho

Escreva `typst-build/etapa1.typ` e `resumindo.typ` no estilo didático NEBLI.
Mecanismo antes de nomenclatura; aluno com conhecimento inicial baixo; figuras
quando carregam estrutura, mecanismo ou comparação. Não gere E2/E3/RemNote.

## 4. Atomização para busca local

Converta a E1 em conceitos recuperáveis e atômicos. Cada conceito deve ter:

- `id` estável;
- `query` preferencialmente em inglês médico;
- `aliases` quando houver sinônimos úteis;
- `required=true` para núcleo da aula;
- âncora literal na E1.

Grave `arquivos-trabalho/<slug>/conceitos-anking.json`. Não selecione cards por
memória, não dependa de Drive/Colab e não exija IDs do Anki nesta etapa.

## 5. Passe Step 1 → E1

Para cada conceito que aprofunda o mesmo mecanismo/estrutura da aula, aplique
`docs/canon/COBERTURA-E-STEP1.md`. Conteúdo aceito entra na E1 antes do card.
Conteúdo de próxima aula/Step 2 fica fora. Revalide as âncoras e congele o
contrato.

## 6. Gerar manifesto AnkiDroid v2

Execute:

```bash
python flashcards/scripts/gerar_manifesto_ankidroid.py \
  --slug <slug> \
  --deck "NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>" \
  --conceitos arquivos-trabalho/<slug>/conceitos-anking.json
```

O manifesto não contém os 6 GB do AnKing. Ele leva conceitos/aliases ao Companion,
que pesquisa diretamente a coleção local do tablet.

## 7. Resolução local no Companion

O Companion deve, por conceito:

1. buscar na coleção do AnkiDroid;
2. remover cópias NEBLI do pool;
3. preferir marcadores AnKing quando existirem;
4. ranquear candidatos;
5. exigir score e margem mínimos;
6. inferir o sibling cloze correto quando houver vários;
7. copiar literalmente `mid + flds + tags` para `NEBLI::*`;
8. suspender siblings não selecionados;
9. reler a fonte e comprovar que permaneceu intacta;
10. deixar resultado ambíguo como `unresolved`, nunca escolher à força.

## 8. Lacunas reais, autoria e visual

O recibo do Companion separa `resolved[]` e `unresolved[]`. Só `unresolved`
comprovado pode virar autoral/IO. Para cada lacuna:

- refaça buscas com aliases antes de autorar;
- use externo real quando superior;
- autoral em inglês médico, atômico, uma recuperação;
- cloze 1 palavra por padrão, 2 quando necessário, 3 raramente;
- IO apenas quando a tarefa espacial agrega valor;
- IO multi-rótulo coerente usa `hide_all_guess_all`;
- imagem deve ter função cognitiva e passar QA visual.

Até o Companion suportar note types autorais/IO nativamente, esses itens usam o
backend desktop/APKG como fallback **somente para as lacunas**, sem recolocar o
AnKing inteiro no fluxo antigo.

## 9. Revisão independente

Com E1, manifesto, recibo e eventuais autorais/IO completos, podem rodar
`revisor-cobertura`, `revisor-cards-visual` e os auditores aplicáveis. Eles não
editam. A sessão principal lê os relatórios e aplica correções.

## 10. Gates finais

Bloqueie se houver:

- conceito nuclear sem card real ou lacuna explicitamente tratada;
- seleção AnKing de baixa confiança;
- fonte modificada;
- card não atômico;
- cloze longo;
- teto excedido;
- IO com máscara/pista errada;
- mídia quebrada;
- card órfão da E1;
- `unresolved` ignorado.

O número final de cards não pode exceder o contrato.

## 11. Entrega

Entregue primeiro E1/PDF, depois o manifesto AnkiDroid v2 e o relatório final com
conceitos resolvidos/pendentes, cards por fonte, decisões visuais, autorais/IO e
auditoria. O fluxo preferido no tablet é abrir o manifesto no Nebli Companion e
deixar a resolução/cópia AnKing ocorrer localmente. Configure 25 novos/dia e
9999 revisões/dia. Nunca marque concluído só porque comandos foram executados.
