# Revisão do deck vivo em 05/10/2026

O despejo integral de `python3 -m nebli.revisar` mostrou 50 notas e 60 cards
instalados. A revisão ainda não autoriza `revisao-inventario.json` com todos os
itens aprovados nem a entrega.

## Lacunas reais a corrigir

- **Slide 10, retenção renal de sódio:** `retencao-renal-primaria` oculta
  `hypo` e `expansion` numa frase sobre expansão hipo-osmótica de volume.
  Sua frente não pergunta pelo mecanismo de retenção renal primária de sódio.
  O Extra menciona o mecanismo, mas isso não cumpre o alvo
  `s10-retencao-sodio-edema`, que pede distinguir retenção primária e
  secundária. Buscar card externo que teste essa diferença ou replanejar
  explicitamente a cobertura.
- **Slide 12, neutrófilos e barreira alvéolo-capilar:**
  `lesao-alveolocapilar` testa aumento de permeabilidade por dano da
  interface; `contracao-endotelial` testa histamina. Nenhuma frente instalada
  testa a participação dos neutrófilos no dano descrito em
  `s12-lesao-alveolocapilar`. Conferir a imagem e buscar card específico.
- **Slide 14, extravasamento de hemácias:** `morfologia-pulmonar-s14`
  testa capilares septais congestos; `celulas-insuficiencia-cardiaca` testa
  macrófagos com hemossiderina. O elo hemorrágico é explicado no Extra,
  mas não é perguntado diretamente. Verificar se a lâmina exige reconhecer
  hemácias fora dos vasos e selecionar card visual para esse alvo.

## Tabs

`nebli.explicacoes gerar` parou antes de produzir qualquer Tab pelo limite
semanal da assinatura Claude, que reinicia em 08/10 às 12h (São Paulo).
Não há `ollama`, `llama-cli`, `lmstudio`, `mlx_lm` nem modelos locais detectados
na máquina. O CLI `codex` existe, mas não foi usado como substituto automático:
não há configuração verificada que garanta uso sem API paga. Explicações
autoradas manualmente continuam possíveis, mas precisam ser individuais,
revisadas e ter 150–220 palavras por card antes da gravação na base do Tab.

## Estado de entrega

Gate com `--sem-drive`: 33/40 passos, sete falhas. Nenhum novo `.apkg`, cópia
no Drive ou sync final desta refação foi declarado concluído.
