# NEXT-SESSION.md — rode o pipeline sem reconstruir contexto

Este é o ponto de entrada operacional para uma nova sessão.

## Situação já resolvida

A infraestrutura do Deck-Aula está pronta no `main`:

- pipeline `e1-deck-v10`;
- Companion AnkiDroid final instalado no tablet;
- conexão real com AnkiDroid testada;
- cópia segura real testada;
- busca local real testada;
- AnKing, deck externo, autoral, mídia nova e IO suportados no fluxo direto;
- hard gates de qualidade e regressão de 40 cards no CI.

**Não reabra a arquitetura, não volte para Drive/Colab/APKG e não peça ao usuário para escolher cards manualmente.** Se uma aula real revelar um bug, corrija o bug dentro do pipeline canônico.

## Pedido que deve bastar na nova sessão

O usuário pode simplesmente anexar os PDFs e dizer:

> Rode o pipeline Nebli completo desta aula até o fim. Use o canônico atual do repo, teste e corrija tudo sozinho e me devolva somente o E1/PDF e o manifesto final para abrir no Companion. Pergunte só se houver um bloqueio impossível de resolver pelos arquivos/contexto.

Isso deve ser suficiente.

## Ao iniciar

1. Leia `CLAUDE.md`, este arquivo, `MEMORY.md`, `ERROS.md` e `config/pipeline.json`.
2. Leia `docs/canon/E1.md`, `docs/canon/CARD-QUALITY.md`,
   `docs/canon/ANKIDROID-COMPANION.md`,
   `docs/canon/LOCAL-DECKS-AND-MEDIA.md`,
   `docs/canon/PIPELINE-E1-DECK.md` e `.claude/commands/resumo.md`.
3. Confirme mecanicamente `pipeline_version=e1-deck-v10`, release gate
   `nebli-e1-deck-release-v1` e schema `nebli-ankidroid-deck-v3`.
4. Consulte a planilha mestra registrada em `MEMORY.md`, aba `Matérias`, para
   resolver UC, prova, componente, número e título da aula.
5. Trate os PDFs/objetivos/perguntas orientadoras fornecidos como fontes da aula.
6. Execute `/resumo` integralmente. Não pare entre etapas para pedir autorização.

## Definição do Deck-Aula

Nome final:

`NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`

Se houver cards `optional`, usar subdeck:

`<Deck-Aula>::Optional`

A sessão deve inferir UC/prova/componente/nome curto pelos arquivos e contexto quando isso for seguro. Perguntar somente se duas interpretações plausíveis produzirem decks materialmente diferentes.

## Qualidade de card — não negociar

Antes de criar ou aceitar qualquer card, aplicar `docs/canon/CARD-QUALITY.md`.

Resumo dos hard gates:

- um card = uma recuperação independente;
- card precisa ser relevante para a aula e ter âncora literal na E1;
- não criar cards para cumprir cota;
- classificar conceitos como `must_recall`, `derivable`, `e1_only` ou `optional`;
- fixar slots antes da busca e exigir resposta estimada em até 10 segundos;
- remover todo card que não cause perda relevante no teste de ablação;
- congelar e respeitar `card_budget.hard_max`;
- ordem de fonte: AnKing adequado → deck externo adequado → autoral;
- AnKing/deck externo deve testar exatamente a recuperação desejada, não um tema vizinho;
- nota AnKing é buscada pelo contexto e sibling é escolhido pela resposta esperada;
- autoral direto exige busca AnKing completa e motivo concreto de rejeição;
- cópia de fonte real é literal e a fonte é somente leitura;
- autoral: inglês médico natural, Extra curto em português, exatamente um `c1`;
- cloze: 1 palavra por padrão, 2 quando necessário, 3 excepcionalmente com justificativa, 4+ proibido;
- evitar enumerações, mini-resumos, múltiplas respostas e redundância funcional;
- visual só quando agrega uma tarefa cognitiva;
- IO: `hide_two_guess_two`, preferencialmente duas respostas coerentes e no máximo duas;
- máscara cobre o rótulo-resposta, nunca a pista morfológica/estrutura a reconhecer;
- card autoral procura primeiro imagem AnKing local; imagem nova exige rejeição visual AnKing documentada, fonte real, valor didático, crédito, legibilidade, preview pergunta/resposta e ausência de vazamento;
- anatomia/histologia com objetivo de reconhecimento não pode fechar só com cards verbais.

## Resolução local do Anki

Para uma recuperação planejada como AnKing/deck externo:

1. gerar `search_queries`, `expected_answers` e restrições contextuais;
2. buscar localmente no AnkiDroid;
3. ranquear a nota pelo contexto;
4. selecionar automaticamente apenas com confiança suficiente;
5. inferir o sibling pela resposta esperada;
6. copiar literal e suspender siblings não escolhidos;
7. reler a fonte e provar que não mudou;
8. se ausente/ambíguo, usar o fallback validado; se `anking_required=true`,
   bloquear em vez de cair silenciosamente no autoral.

## Autorais e IO

Toda lacuna/fallback já deve chegar ao manifesto validada.

Autorais e IO são instalados diretamente pelo Companion. Mídia nova é self-contained no manifesto com SHA-256 e crédito; não carregar mídia privada do AnKing para GitHub.

## Validação final obrigatória

Não amostrar. Validar cada card real.

Obrigatório:

- `expected_card_count == validated_card_count`;
- `passed_card_count == expected_card_count`;
- `failed_card_count == 0`;
- total ≤ `card_budget.hard_max`;
- nenhuma `card_key` duplicada;
- toda âncora E1 presente;
- todo fallback aplicável validado;
- todo visual aplicável validado.

Depois gerar o manifesto único `nebli-ankidroid-deck-v3`.

O Companion deve:

- criar/reusar o deck correto;
- criar `::Optional` se necessário;
- instalar o lote inteiro;
- fazer rollback das notas novas se qualquer card falhar;
- terminar somente com `installed_card_count == expected_card_count`;
- selecionar e abrir o deck raiz no AnkiDroid.

## O que entregar ao usuário

Não despejar arquivos intermediários se não forem pedidos. Entregar:

1. E1/PDF final;
2. manifesto final `<slug>.ankidroid.json`;
3. uma frase curta dizendo que o gate passou e quantos cards foram validados;
4. instrução única: **abrir o `.ankidroid.json` no Nebli Companion**.

O usuário não deve precisar montar JSON, procurar cards, importar APKG, usar Colab, usar Drive, configurar desktop ou revisar card por card.

## Quando interromper o usuário

Somente se houver um bloqueio real que não possa ser resolvido por:

- arquivos da aula;
- canônico do repo;
- busca local do AnkiDroid;
- fallback validado;
- inferência segura de metadados.

Nunca interromper apenas para confirmar decisões já definidas no canônico.
