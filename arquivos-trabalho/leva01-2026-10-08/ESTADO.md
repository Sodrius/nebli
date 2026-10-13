# Leva 1 — comentários médicos + famílias (início 08/10/2026)

Checklist da corrida. Marcar `[x]` ao concluir cada item; a próxima sessão continua do primeiro `[ ]`.

## Infra feita nesta leva
- [x] `comentarios-before.json`: snapshot dos 98 comentários (88 médicos), campos, fila e bandeiras.
- [x] `nebli/zif.py`: recorte de lâmina virtual do Histology Guide por região + busca no índice (`--buscar termo`).
- [x] `nebli/seta.py`: setas amarelas estilo AnKing e rótulos sobre imagem, com recorte.
- [x] Atlas Sorenson cap. 14 (GI) gratuito em `arquivos-trabalho/livros/sorenson/ch14-clean.pdf` (marca d'água removida, micrografias intactas).
- [x] `nebli/reconcilia.py` + `nebli.delta` respeita `correcoes-vivas.json`: 307 campos vivos de 11 corridas (UC08 + GR02/PR02) reconciliados; delta recusa sobrescrever campo vivo não reconciliado.
- [x] `nebli/corrige.py` (aplicação em lote com backup/readback/CORRIGIDO/dessuspensão; pula nota na tela).
- [x] `nebli/css_recorte.py`: recorte por CSS → arquivo recortado (62 notas usam o estilo, 58 na BT03).
- [x] `nebli.decks.escrita`: sync adiado se Davi está revisando (`ANKI-SYNC-PENDENTE`), `em_tela()` para excluir a nota na tela do lote, `sync_se_ocioso()`.
- [ ] Testes: 5 falhas pré-existentes (test_entrega, test_e1_mode, test_handoff texto antigo, test_ordem, test_explicacoes) → resolver na trilha P.

## Famílias (classificação dos 88)
- [ ] `casos.json`: cada nid → família(s), decisão, novo conteúdo, imagem, status.
Famílias: A imagem não direcionada/excesso/errada/ausente; B oclusão sem seta/errada/sobrecarregada/sem dica; C cloze longo/ambíguo/vazado; D escrita estranha, sem negrito/sublinhado; E Extra ("comentário" para Davi) estranho/ausente/com ; e :; F Tab não didático; G fora do recorte; H ordem/adjacência; I positivos (preservar); J tamanho da imagem.

## Execução
- [x] Histologia BT03 (32) + BT04 (9): imagens HG/Sorenson com seta, Extra AnKing, clozes.
  - [x] BT03 salivares (11 notas, lote `bt03-salivares`, aplicado 17:15)
  - [x] BT03 língua/mucosa oral/dentes (22 notas, `bt03-lingua-dentes`, 17:21)
  - [x] BT03 parede do tubo + esôfago (14 notas, `bt03-parede`, 17:28)
  - [x] BT03 estômago (23 notas, `bt03-estomago`, 17:33) + feedback ao vivo (`bt03-feedback1`: bt03-98 reescrito, bt03-64 retirado redundante)
  - [x] BT04 (9 notas, `bt04`, 17:36; 4 dessuspensos; haustros e grânulos de Paneth retirados)
- [x] Anatomia AN01 + AN02 + AN07 (`an-lote1`, 30 notas, 9 dessuspensos, 17:48): setas de foco nas oclusões (`nebli.io_seta`), oclusões refeitas sobre Netter limpo (`nebli.io_novo`, `atlas_pdf --limpo`), dicas no Header, vasos retos curtos logo após os longos (spec AN01 + tags; `nebli.ordem` ok).
- [x] Fisiologia FI05/FI06/FI08/FI09 + GR02 (`fi-lote1`, 15 notas, 17:51): diagramas em caixa de texto retirados (família E, 8 notas), esquema de varicosidade, gráfico de spikes, cor rosa pedida (tight junctions).
- [ ] Generalizar cada família aos cards sem comentário das mesmas aulas (busca por padrão).
- [ ] Tab regenerado para todos os cards alterados; leitura de amostra.
- [ ] 2–4 cards de conexão rosas de exemplo (uma aula).
- [ ] Aplicar em lotes (nota em tela excluída), readback, dessuspender corrigidos, `CORRIGIDO, 08, 10, 26.`
- [ ] `nebli.reconcilia` nas corridas afetadas depois de aplicar.
- [ ] REVISAO.md + receipt/verification; regras novas → MEMORY/lint; perguntas → ESTADO-ATUAL.
