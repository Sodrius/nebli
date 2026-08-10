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

Leia `CLAUDE.md`, `MEMORY.md`, `ERROS.md`, `docs/canon/PIPELINE-E1-DECK.md` e
todos os demais arquivos de `docs/canon/` listados no `CLAUDE.md`. Leia
`config/pipeline.json` e confirme:

- `pipeline_version=e1-deck-v3`;
- E2, E3 e RemNote desligados;
- 25 novos/dia;
- APKG offline e auditoria obrigatórios.
- teto de cards por contrato, cloze 1/2/3 palavras e IO multi-rótulo em
  `hide_all_guess_all`.

Nunca leia `docs/legacy/` durante uma corrida normal.

## 1. Entrada e checkpoint

Resolva slug, slide, UC, prova, componente e nome curto. Use cronogramas quando
possível; pergunte apenas se a ambiguidade alterar o produto. Crie
`arquivos-trabalho/<slug>/CHECKPOINT.md` com fase, fontes, decisões, pendências e
próximo passo literal. Atualize após cada fase.

## 2. Fontes e contrato inicial

Extraia slides e objetivos. Crie
`arquivos-trabalho/<slug>/contrato-cobertura.json` a partir de
`flashcards/schemas/lesson-contract-v3.example.json`. Registre cada conceito com
nome PT/EN, subtópico, origem, importância e possível necessidade visual.
Classifique o porte, proponha `card_budget.hard_max` e congele esse teto antes da
busca. Slides/objetivos definem o escopo; não acrescente conteúdo adjacente.

## 3. E1 rascunho

Escreva `typst-build/etapa1.typ` e `resumindo.typ` no estilo didático NEBLI.
Mecanismo antes de nomenclatura; aluno com conhecimento inicial baixo; figuras
quando carregam estrutura, mecanismo ou comparação. Não gere `etapa2.typ`,
`etapa3.typ`, gabarito ou RemNote.

## 4. E1 atomizada + busca privada

Converta a E1 em conceitos recuperáveis e acrescente âncoras literais ao
contrato. Traga o índice privado com
`python flashcards/scripts/fetch_private_index.py` e busque nele com
`search_private_index.py`, em consultas independentes PT, EN,
sinônimos, mecanismo/estrutura, tags e cards irmãos. Se o fetch responder
`no_credential`, aponte `docs/SETUP-ANKING-DRIVE.md` no relatório final. Use a união deduplicada;
busca única sem resultado não prova lacuna. Para gaps, consulte decks externos. Se o índice privado
não estiver disponível, **pare o deck**: não compense com autoria em massa.

## 5. Passe Step 1 → E1

Para cada candidato Step 1, aplique `docs/canon/COBERTURA-E-STEP1.md`. Aceite
somente aprofundamento do mesmo mecanismo/estrutura que encaixe naturalmente na
E1. Registre fonte, decisão e motivo. Incorpore e explique o conteúdo aceito na
E1 antes de qualquer card. Revalide todas as âncoras e congele o contrato.

## 6. Curadoria e autoria

Roteie cada conceito na ordem AnKing → externo → autoral. Preencha `cards[]` e
conte `generated_card_count`; nunca exceda `card_budget.hard_max`. Preserve os originais;
cópias recebem GUID novo, `source_guid` e todos os campos/mídia/créditos. Autoral
só para lacuna comprovada, em inglês médico, uma recuperação e uma ocorrência
`c1`. Cloze: 1 palavra por padrão, 2 quando necessário e 3 raramente, com motivo.
Separe `opcional` em subdeck; nunca misture com `nucleo`.

## 7. Plano visual e IO

Preencha uma decisão visual por conceito antes de fechar cards. Priorize imagem
do AnKing, card irmão e deck externo; slide é último caso. Use Image Occlusion ou
prompt visual para reconhecer/localizar; imagem no Extra para mecanismo. Em
diagrama rotulado, a máscara cobre o rótulo-resposta, nunca a estrutura. Mapas
coerentes com várias partes usam `hide_all_guess_all`. Em imagem não rotulada,
adicione seta/contorno + rótulo ou use prompt visual; não apague a pista
morfológica. Gere previews de pergunta e resposta e valide fonte, hash, crédito,
crop, legibilidade, vazamento e todas as máscaras.

## 8. Montagem offline

Monte `<Nome curto>.apkg` sem AnkiConnect, incluindo note types, templates,
cards, tags, mídia e subdeck `Optional`. Deduplicate por hash e trate colisões de
nome. Gere `<Nome curto> - E1.pdf` e a versão leve.

## 9. Revisão independente

Com os artefatos completos, podem rodar `revisor-cobertura`,
`revisor-cards-visual` e `auditor-apkg`. Eles não editam. A sessão principal lê
os relatórios, decide e aplica cada correção, registrando o destino no checkpoint.

## 10. Gates finais

Rode o validador do contrato, o validador visual e `audit_apkg.py`. Abra o APKG
real. Renderize todos os autorais, IO, mídia alterada e uma amostra das cópias.
Bloqueie se houver lacuna nuclear, card órfão, Step 1 fora do tema, autoral sem
rejeição de fonte, card não atômico, cloze longo, teto excedido, IO mascarando a
pista, mídia quebrada, GUID colidindo, visual obrigatório pendente ou APKG não
auditável. O total real do APKG deve ser igual ao previsto no contrato.

## 11. Entrega

Entregue e aponte explicitamente primeiro o PDF E1 e seu fonte
`typst-build/<slug>/etapa1.typ`; depois APKG e `relatorio-final-<slug>.json` com conceitos por
importância/cobertura, cards por fonte, Step 1 aceito/rejeitado, decisões
visuais/IO, auditoria e pendências reais. Configure/instrua 25 novos/dia e 9999
revisões/dia. Inclua buscas prontas para cram. Nunca marque como concluído só
porque comandos foram executados.
