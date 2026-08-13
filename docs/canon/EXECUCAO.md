# Execução canônica do pipeline

## Entrada e saída

A entrada é o conjunto de materiais da aula. A saída visível é o PDF da E1 e um manifesto `*.ankidroid.json`. O usuário instala o Companion uma única vez; nas aulas seguintes, apenas abre o manifesto.

## Ordem obrigatória

1. Inventariar objetivos, slides, blocos relevantes da transcrição, perguntas orientadoras, notas e informação visual.
2. Criar `source_to_e1_matrix`, com uma linha por unidade de fonte, `origin`, `decision`, `anchor` e justificativa quando excluída/indisponível.
3. Produzir `main.typ`, `etapa1.typ` e `resumindo.typ` com o template `nebli_v2_apostila.typ`, seguindo `E1.md`.
4. Compilar, renderizar e revisar todas as páginas; preencher o ledger de figuras ou justificar a ausência delas.
5. Congelar o núcleo de retenção antes da autoria. Aplicar compressão e ablação; não preencher cotas.
6. Criar somente cards `source=authored` e `source=io`, integralmente em português. Não executar busca AnKing/deck externo.
7. Rodar `validar_release_e1_deck.py` e `validar_deck_card_a_card.py --out validation-report.json`.
8. Rodar `finalizar_entrega_canonica.py`. Ele rejeita mudança posterior de card, ordem, conjunto, E1 ou mídia.
9. Abrir o manifesto no Companion 0.8.0+ e conferir o recibo: contagens iguais, deck selecionado, mídia funcional, idempotência e rollback.

## Artefatos calculáveis

O agente informa somente identidade, conteúdo, âncora, recuperação-alvo, revisão semântica compacta e dados visuais. Scripts calculam número/índice/tamanho de clozes, caracteres, idioma provável, resposta visível, contagens e hashes. O `content_sha256` cobre o conteúdo que afeta aprendizagem/renderização; o relatório e o manifesto carregam também o hash do conjunto ordenado e hashes de mídia.

## Definição de pronto

A corrida fecha apenas com E1 completa e visualmente aprovada, matriz completa, nenhuma lacuna ou pergunta retórica, todos os cards aprovados e hash-idênticos, manifesto v3 compatível, instalação integral no deck canônico, recibo exato e nenhuma duplicação na reexecução.
