# Execução canônica do pipeline

## Entrada e saída

A entrada é o conjunto de materiais da aula mais a identificação curricular na planilha mestra. A saída visível é o PDF da E1 e o `.apkg` auditado.

## Ordem obrigatória

### Fase 1 — inventário e calibração da E1

1. Inventariar objetivos, slides, blocos relevantes de transcrição/roteiro, perguntas orientadoras, notas e toda informação visual com valor didático.
2. Ler `docs/canon/E1.md` integralmente.
3. Antes de escrever, calibrar a E1 conforme esse contrato: `EXEMPLARES.md`, `ANTI-EXEMPLARES.md`, documentos didáticos aplicáveis e pelo menos dois exemplares UC02 adequados.
4. Registrar no `e1_review` quais referências de calibração foram efetivamente usadas e por quê.

### Fase 2 — matriz fonte → E1

5. Criar `source_to_e1_matrix` antes da redação, com uma linha por unidade relevante da fonte: `origin`, `decision`, `anchor` quando ensinada/integrada/visual e justificativa quando excluída ou indisponível.
6. A matriz deve cobrir objetivos, mecanismos, relações, informação visual e detalhes necessários para compreensão inicial zero. O fato de algo não merecer card nunca é razão para excluí-lo da E1.

### Fase 3 — redação e revisão da E1

7. Produzir `main.typ`, `etapa1.typ` e `resumindo.typ` com `nebli_v2_apostila.typ`, seguindo `docs/canon/E1.md`.
8. A prosa deve ensinar do zero em encadeamento: ponto de partida → fenômeno concreto → mecanismo em etapas → nome técnico → consequência → integração → nuance.
9. Compilar e executar quatro passadas, nesta ordem:
   - completude fonte → E1;
   - aluno iniciante zero;
   - didática/voz, comparando com os exemplares calibradores;
   - inspeção visual de todas as páginas renderizadas.
10. Preencher o ledger de figuras com origem, tarefa cognitiva, corte, resolução, legenda/correspondência, página renderizada e aprovação. Se não houver figura, justificar pedagogicamente.
11. Só congelar a E1 quando não houver omissões nucleares, ambiguidades, lacunas de iniciante ou defeitos visuais pendentes.

### Fase 4 — ganho da aula e cards

12. Somente depois da E1 congelada, ler `FLASHCARDS.md` e `EXEMPLARES-CARDS.md`.
13. Construir `curriculum_context` com a planilha mestra e classificar os claims como `foco_novo`, `relacao_nova`, `aprofundamento_novo`, `pre_requisito`, `revisao`, `contexto`, `exemplo` ou `mencao`.
14. Rodar `validar_ganho_aula.py`. Conteúdo de suporte pode permanecer explicado na E1, mas não recebe card.
15. Congelar o núcleo de retenção antes da autoria. Aplicar compressão e ablação; não preencher cotas.
16. Criar apenas cards `source=authored` e `source=io`, em português, dentro do ganho real da aula.
17. Rodar `validar_deck_card_a_card.py` e a revisão independente ligada ao hash final do conjunto.

### Fase 5 — pacote final

18. Rodar `finalizar_entrega_canonica.py`.
19. O finalizador deve rejeitar qualquer mudança posterior de card, ordem, conjunto, E1 ou mídia e gerar o `.apkg` apenas a partir do lote aprovado.
20. Reabrir o pacote, validar a estrutura interna e a compatibilidade do metadata schema legado exigido pelo importador atual do Anki/AnkiDroid.
21. Entregar somente quando E1 e `.apkg` estiverem aprovados.

## Definição de pronto

A corrida só fecha com:

- inventário e matriz fonte → E1 completos;
- calibração documentada antes da redação;
- E1 completa, didática, autocontida e visualmente aprovada;
- quatro passadas de revisão concluídas;
- ganho da aula classificado antes da autoria dos cards;
- todos os cards aprovados, ancorados e hash-idênticos ao lote revisado;
- APKG estruturalmente íntegro e compatível com importação;
- nenhuma regressão bloqueadora pendente.

`CLAUDE.md` contém os comandos; este documento preserva a ordem pedagógica que nenhum executor pode abreviar.
