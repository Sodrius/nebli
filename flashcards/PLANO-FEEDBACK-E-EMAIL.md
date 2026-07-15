# Plano operacional — comentários, bandeiras e email NEBLI

> Estado auditado em 2026-07-14. Nenhum email foi enviado e nenhuma bandeira/card foi alterado nesta rodada.

## O que existe hoje

- **26 vermelhas** no conjunto `NEBLI::*`.
- **0 laranjas**.
- **2 verdes**.
- **0 comentários pendentes** em `NEBLI_comentario::pendente`.
- Relatório card a card: `arquivos-trabalho/AUDITORIA-FEEDBACK-ANKI-2026-07-14.md`.

O monitor antigo cortava silenciosamente a bandeira em 14 cards. O teto foi elevado para 50, e o novo modo seguro confirmou que os 26 aparecem:

```powershell
python flashcards/scripts/monitor_email_anking.py --bandeira --read-only
```

## O que as bandeiras estão dizendo

As vermelhas não são lapses (`errou 0x`): são feedback de qualidade/entendimento. Elas se agrupam em:

1. **Gametogênese e cronologia meiótica** — cinco cards AnKing; dois são siblings da mesma nota e mostram que o processo/produto ainda não está firme.
2. **Fertilização e embriologia inicial** — cinco cards autorais; há respostas longas e formulações pouco naturais (`sem crescer`, `represados... por décadas`).
3. **Neurulação e destinos mesodérmicos** — três cards; o conteúdo pertence, mas dois clozes escondem frases grandes.
4. **Reconhecimento visual de neurônio** — um IO; precisa checar se a imagem/oclusão realmente permite localizar o alvo.
5. **Vasos/linfáticos, tecido nervoso e órgãos linfoides** — doze cards EN autorais; vários misturam pergunta, resposta já visível e mais de uma operação de recall.

Os dois verdes são relações estruturais compactas: túnicas do vaso e composição mínima do capilar. O sinal positivo é importante: o usuário aceita múltiplos elementos quando formam **uma única relação coerente**, não quando o card empilha fatos independentes.

## Decisão de curadoria proposta

- Não apagar nem reescrever os 26 automaticamente.
- Na próxima passada, comparar cada vermelho à E1 e classificar: `explicação faltante`, `cloze ruim`, `redundante`, `imagem inadequada`, `idioma/termo`, `fora de escopo`.
- Prioridade de reparo: cards 15–26 (padrão autoral EN recente) → cards 6–13 (clozes longos) → IO → siblings AnKing.
- Os dois verdes viram exemplares somente após confirmar que foram marcados intencionalmente como “bom card”.

## Por que o email ainda não está 100% operacional

1. O cérebro padrão `claude -p` atingiu o limite semanal e volta em 16/07 às 12h; a variável de API alternativa não está configurada.
2. O script antigo enviava fallback manual quando o JSON estruturado falhava.
3. Se o SMTP falhasse, ele ainda removia a bandeira e dessuspendia cards.
4. Cards já suspensos antes do fluxo poderiam ser dessuspensos por engano.
5. O add-on de comentários e o de auto-suspensão usam hooks privados e já foram relatados como quebrados.
6. O modo “semanal” usa lapses históricos/leeches, não uma janela semanal real.

## Correções pequenas já aplicadas

- Preview passou a ser o padrão; envio exige `--send`.
- `--read-only` força zero sync, zero LLM, zero SMTP e zero mutação.
- `--suspender-vermelhos` exige `--apply`.
- Sync só ocorre com `--sync` explícito.
- Falha de LLM cancela o envio, preservando bandeiras.
- Falha de SMTP não remove bandeiras; só a suspensão criada pela própria execução pode ser revertida.
- O monitor agora inclui até 50 bandeiras.
- `auditar_feedback_anki.py` lê as três cores e comentários em um relatório único.

## Email planejado

Assunto: `NEBLI · revisão das 26 bandeiras — padrões e próximos reparos`

Estrutura:

1. **Resumo de padrões frágeis** — cronologia meiótica; fertilização; movimentos/destinos embrionários; discriminação histológica e neuro-histologia.
2. **Explicação por cluster**, não 26 miniapostilas desconectadas.
3. **Tabela card → por que foi marcado → reparo proposto**.
4. **Dois exemplares positivos** para mostrar o padrão desejado.
5. **Ação**: o email não limpa flags até entrega confirmada; reparos no deck ocorrem em corrida separada e auditável.

## Para chegar a 100% operacional

1. Adicionar entrada `--input-json` para o agente atual entregar explicações validadas sem depender da quota do Claude CLI.
2. Validar exatamente N explicações para N cards; falhar fechado.
3. Testar SMTP com fake: falha deve preservar flag/estado; sucesso faz commit uma vez.
4. Testar email real para destinatário explícito, primeiro com um card de perfil descartável.
5. Trocar monkeypatches dos add-ons por hooks públicos/QAction; fazer smoke test no perfil Anki real.
6. Implementar janela semanal de revlog ou renomear o modo para `recorrentes`.
7. Só então habilitar `--send --sync` como fluxo de produção.

Até esses testes, o canal está **seguro para auditoria e preview**, mas não deve limpar automaticamente o feedback do usuário.
