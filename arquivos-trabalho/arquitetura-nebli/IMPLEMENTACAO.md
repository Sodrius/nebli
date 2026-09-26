# Roteiro de implementação e passagem para o executor

> **Roteiro histórico:** seguir o [plano v2](../../flashcards/projeto/IMPLEMENTACAO.md) para a próxima implementação. Preservado para rastreabilidade.

Leia primeiro [ARQUITETURA.md](ARQUITETURA.md). Este roteiro transforma o desenho em entregas verificáveis. Os comandos `nebli` abaixo ainda são interfaces propostas, não ferramentas instaladas.

## 1. Regras de execução do trabalho

- Implementar em fatias; não iniciar pela geração de todos os decks e não reescrever o repositório inteiro.
- Nenhuma chave paga de LLM é requisito. A sessão do Codex faz decisões pedagógicas; os scripts recebem e validam os artefatos que ela produz.
- Preservar mudanças locais anteriores. A inspeção encontrou material ativo de glicogênio e alterações nos documentos canônicos. Fazer patches pontuais após ler os diffs pertinentes.
- Não executar os scripts legados de escrita como se fossem seguros por nome. A inspeção encontrou um modo dry que cria deck e um cliente que repete escritas após timeout.
- Testes de software são necessários para identidade, atualização e estado. Isso não autoriza criar avaliações adicionais para o estudante: E2/E3 continuam suspensas.
- Cada entrega termina com resultado observável e descrição do que ainda não está conectado. Sem alegar instalação se houve apenas exportação.
- Uma regra já escolhida pelo usuário não volta a ser pergunta de preferência. Dúvidas de instalação e conflitos reais são resolvidos quando aparecerem.

## 2. Ordem de construção

### Entrega A — inventário e contexto portável

Entradas: este plano, configurações locais, metadados do Drive/Sheets e exportação/inventário da coleção principal no Mac.

Construir:

1. Configuração com raiz do projeto, máquina de aplicação, identificação do perfil/coleção, planilha, pastas e idioma. Caminhos relativos e configuração fora do código; nenhum `C:\AI use\...` ou usuário macOS fixo.
2. Comando de diagnóstico somente leitura: versão Anki, capacidades do adaptador, perfil ativo, modelos, campos, tags, contagens de notas/cards, disponibilidade da mídia e estado de sincronização conhecido.
3. Exportador de inventário com identidades de origem e cópias. Se GUID não estiver disponível via API, obter por exportação/snapshot consistente suportado; não inventar que `notesInfo` fornece o campo nem escrever no banco vivo para acrescentá-lo.
4. Relatório das cópias NEBLI existentes, histórico e possíveis duplicatas. Não executar limpeza nessa entrega.

Aceite: rodar duas vezes não muda coleção, calendário ou Drive. O inventário distingue notas de cards, documenta perfil/horário e pode ser lido no Windows como snapshot. Se o Mac não estiver disponível, a entrega identifica precisamente a dependência; não usa uma coleção qualquer do Windows.

### Entrega B — registro e calendário

Dependência: A. Construir migrations do SQLite, contratos de identidade e leitor das abas confirmadas.

Normalização:

- Ler cabeçalhos e datas nativas/textuais; não usar posições fixas como identidade.
- Mês vence nas datas; Matérias fornece identificação e associações. Preservar origens.
- Reconhecer eventos de prova, aulas compostas e múltiplas provas; não usar checkbox E como aprendizado.
- Extrair do piloto: conteúdo 38 PT em 11/09, P2 em 02/10, ano letivo 2026; revalidar na execução.
- Marcar vínculo incoerente, data não confirmada e correspondência ambígua como pendências localizadas.

Aceite: testes com P1 divergente, data múltipla, aula sem número, reordenação de linha e evento remarcado. Sem alteração do documento original. O conflito Grand Round 3/P2 deve aparecer como conflito, sem correção inventada.

### Entrega C — fontes e mapa de objetivos do piloto

Dependência: B. Ler os PDFs da pasta localizada; extrair texto e renderizar páginas relevantes quando imagens/diagramas importarem. Distinguir transcrição, material docente e E1 antiga. Identificar o tema real de cada documento.

Construir mapa tipado com objetivo, resposta esperada, origem/localização, papel, decisão de retenção e recurso de aprendizagem. Uma segunda leitura do material-fonte procura omissões do mapa, especialmente imagens e detalhes locais que o resumo anterior possa ter perdido.

Perguntar por livro/cursinho quando a verificação realmente depender dele; não parar toda a preparação porque a biblioteca completa não está disponível. Localizar poucos vídeos e verificar os trechos/cobertura antes de atribuí-los.

Aceite: cada objetivo tem fonte, destino e justificativa; todos os materiais usados estão listados; os não acessados não aparecem como consultados. A E1 antiga não é usada para provar a própria completude.

### Entrega D — busca e seleção em nível de card

Dependências: A e C. Construir índice de corpus com texto limpo para busca e campos originais preservados para cópia/renderização. Paginar por objetivo e registrar buscas. Tags por assunto/recurso e busca textual são complementares.

Usar consulta NEBLI existente primeiro, depois AnKing e outros decks. Para IO, usar metadados e inspeção visual. Cada decisão keep/drop/reuse precisa apontar card/template/cloze e objetivo, não apenas nota.

Lacunas passam por segunda busca. Só então produzir autoral apropriado ou declarar o impedimento real. Não aplicar cotas de autorais, quantidade de palavras ou percentual de cards externos.

Aceite: um caso conhecido encontrado fora da tag principal; um objetivo apenas mencionado no Extra corretamente rejeitado como cobertura; um cloze irmão fora do escopo identificado; uma lacuna verdadeira documentada; uma imagem inadequada detectada. Validar em material do piloto e casos de regressão selecionados do acervo.

### Entrega E — E1, guia e auditoria

Dependência: D. Gerar E1 sempre e guia de estudo, com renderização Typst isolada por execução. Adaptar auditoria visual para saída E1-only sem desativar verificações úteis.

Reaproveitar voz/exemplares, fontes e helpers existentes depois de ler suas instruções. Não limpar `typst-build/etapa*.typ` globais. E2/E3 deixam de ser dependência desta rota.

Validar cobertura em duas direções e coerência de grupos durável/prova/reserva. Conferir cada card autoral ou com mudança semântica; conferir toda imagem nova/alterada. Verificar que o guia não promete cobertura de vídeo que não foi examinada.

Aceite: E1 renderizada e inspecionada; mapa, guia e cards concordam no escopo; núcleo/reserva explícitos; quantidade de cards reais calculada pelo modelo; problemas científicos não são disfarçados como reserva.

### Entrega F — aplicação idempotente no Mac

Dependências: B e E. Primeiro implementar em perfil de teste isolado, sem AnkiHub sincronizando a coleção principal.

Construir adaptador com métodos de alto nível: `inventory`, `plan_diff`, `apply_operations`, `readback`, `export_package`. Os métodos reais de AnkiConnect são descobertos/testados; o restante do programa não depende diretamente de detalhes da API.

Aplicação usa identidades recuperáveis, diário por operação, lock de escritor e detecção de Reviewer. Snapshot consistente antes de mudanças. Modelos copiados independentes do AnkiHub; campos e mídia preservados; identidade do clone reutilizada em toda execução.

Aceite: repetição exata cria zero notas/cards adicionais; timeout após criação é reconciliado; interrupção após metade do lote retoma corretamente; mudança manual é preservada; originais e revlogs não mudam por geração de conteúdo.

Só após os testes, adotar cards existentes do piloto na coleção principal e aplicar novos. Se cópias com histórico competirem, resolver localmente sem fundir revlogs. Deleção em massa não faz parte do piloto.

### Entrega G — seleções, calendário e pacotes

Dependência: F. Gerar seleções por aula/prova com granularidade de card, atualizar calendário e implementar overrides persistentes. Validar consultas no desktop e Android.

Criar exportação por aula e por UC com mesmas identidades, mídia e modelos. Verificar nas duas ordens de importação e após uma atualização de conteúdo. Pacotes são de conteúdo; estado pessoal é reconciliado pelo aplicador.

Implementar upload para destino privado identificado, com file_id, hash, versão, recibo e leitura de confirmação. A pasta compartilhada da fonte não é destino automático de saída pessoal.

Aceite: uma pergunta compartilhada por Patologia e Imunologia aparece nas duas seleções e apenas uma vez no inventário/revisão. Final de uma prova não suspende a associação requerida por outra. Falha de upload não refaz importação. PDFs/APKGs têm versões correspondentes no manifesto da entrega.

### Entrega H — uso real e expansão gradual

Dependência: G. Estudar o piloto e recolher feedback de qualidade. Medir tempo real, novos/revisões, atraso e correções; não criar testes novos para o aluno.

Depois de duas a três semanas, revisar tamanho do núcleo e taxa de introdução com dados; resultados de prova entram quando disponíveis. Registrar limitações da amostra e não inferir causalidade de uma nota.

Expandir para aulas atuais. A recuperação de UCs antigas entra aos poucos. Acrescentar o mapa Step 1 conforme os objetivos forem mapeados; não bloquear a produção até completar todo o currículo.

## 3. Contratos entre IA e programa

A IA entrega dados estruturados; o programa rejeita campos ausentes e referências inválidas. Um texto dizendo “está completo” não substitui a matriz. Versão de schema acompanha todos os artefatos.

### `objectives.json`

```json
{
  "schema_version": 1,
  "lesson_id": "<id-persistente>",
  "source_snapshot": "<hash-do-inventario>",
  "objectives": [{
    "objective_id": "<id-persistente>",
    "target": "<o que precisa ser recuperado>",
    "expected_answer": "<criterio de resposta>",
    "source_refs": [{"source_id": "<id>", "locator": "<pagina ou trecho>"}],
    "role": "core",
    "retention_group": "durable",
    "card_decision": "required",
    "rationale": "<justificativa concreta>"
  }]
}
```

O exemplo é estrutural; valores entre `<...>` não são dados válidos de execução. Enums documentados: `role = core|local_detail|prerequisite|clinical_bridge|optional`; `retention_group = durable|exam|reserve`; `card_decision = required|resource_only|deferred|excluded`. Adiar/excluir exige motivo, e objetivo central originalmente exigido continua visível como pendência até uma decisão justificada.

### `decisions.jsonl`

Uma decisão por candidato e alvo de card: `objective_id`, `source_key`, `source_card_identity`, `action=keep|drop|reuse|author`, `reason`, `question_target`, `answer`, `coverage=full|partial|mention|none`, `visual_check`, `search_evidence_refs`. Para reutilização, informar `nebli_card_key`. Autorais incluem referência factual acessada e buscas prévias. Evitar duplicar a íntegra do corpus em todo artefato.

### `plan.json`

Inclui `plan_id`, `schema_version`, `collection_identity`, `registry_revision`, `calendar_revision`, hashes das decisões/modelos, operações identificadas, precondições, estados antes/depois e recursos exigidos. Separar alterações de conteúdo das alterações de calendário. Plano para uma coleção não é aplicável a outra sem reconciliação.

### `receipt.json`

Por operação: chave, resultado confirmado, ID real, hash de conteúdo, status e horário. Estados possíveis: `not_started`, `applied`, `verified`, `failed`, `unknown`. `unknown` dispara leitura/reconciliação; nunca repetição cega de criação. Resultado geral distingue aplicado, exportado e publicado.

## 4. Política de ativação — exemplos de aceite

| Situação | Resultado esperado |
| --- | --- |
| Aula passada, núcleo durável aprovado, sem override | Elegível/ativo conforme política; novos respeitam fila |
| Aula futura | Não liberar automaticamente; usuário pode antecipar |
| Detalhe local e prova futura | Ativo na janela, se recomendado |
| Prova passada e nenhuma outra demanda | Suspenso com histórico preservado |
| Prova passada, mas outra aula/prova precisa do card | Manter ativo |
| Card durável de aula antiga também associado a aula futura | Manter ativo |
| Usuário suspendeu no Android e sincronizou | Preservar suspensão; não reativar por calendário |
| Reserva ativada manualmente | Tratar como escolha persistente; calendário não desfaz sem regra explícita |
| Estado mudou, mas motivo da suspensão é desconhecido | Preservar/registrar para esclarecer; não presumir erro do usuário |
| Card temporariamente enterrado pelo Anki | Não criar override permanente |
| Data ambígua ou prova com vínculo incoerente | Adiar apenas a ação afetada e informar |
| Reviewer ativo ou estado inacessível | Preparar/exportar quando possível; aplicação pendente |

## 5. Matriz mínima de testes de software

1. Repetir a mesma aula e depois adicionar outra associação: nenhuma nova cópia da mesma origem.
2. Nota com c1 e c2 para aulas distintas: seleção e ativação apenas dos cards pertinentes.
3. Duas origens com texto igual: não confundir identidade; sinalizar redundância sem fundir automaticamente.
4. Imagens com mesmo nome e bytes diferentes: ambos os cards renderizam sua mídia correta.
5. Fonte AnKing e modelo compartilhado: alterações NEBLI não afetam o original nem entram na gestão AnkiHub.
6. Nota NEBLI antiga com revisões: atualização mantém IDs e histórico.
7. Timeout após criação confirmada no destino: retomada não duplica.
8. Modo dry não chama nenhuma ação mutante, mesmo em erro parcial.
9. Comentário ou edição pessoal após planejamento: merge conserva mudança; conflito é explícito.
10. Exportar/importar aula e UC em ordens diferentes e depois atualizar: identidade estável e progresso existente preservado.
11. Plano feito com snapshot antigo no Windows: Mac reconcilia e recusa precondições inválidas.
12. Calendário reordenado/remarcado e várias provas: regras da tabela anterior preservadas.
13. Palavra só no Extra: não aprovar automaticamente cobertura do objetivo.
14. HTML/cloze/IO renderizados no Mac e Android: pergunta, resposta, máscara e mídia corretas.
15. Falha após aplicar e antes de publicar: retomar só export/publicação.

Testes semânticos usam exemplos de referência julgados, não strings que apenas repetem o algoritmo implementado. Testes de fluxo usam perfil descartável identificado e nunca a coleção pessoal como fixture.

## 6. Alterações planejadas nos documentos existentes

| Local | Alteração após a nova rota estar pronta |
| --- | --- |
| `CLAUDE.md` e futuro ponto de entrada Codex | Referenciar uma especificação operacional única; não duplicar todas as regras |
| `.claude/commands/resumo.md` | Nova rota E1+deck, sem caminhos absolutos nem limpeza compartilhada; preservar mudanças atuais |
| `FLASHCARDS.md` | Consolidar seleção por objetivos, identidade global, grupos e idioma |
| `flashcards/DECK-AULA-PIPELINE.md` | Substituir loop obrigatório E1/E2 pelos contratos novos |
| `flashcards/estrutura-deck-mestre.md` | Corrigir alternativas antigas e documentar casa física versus associações |
| `flashcards/GUIA-RITMO-E-MODOS.md` | Orçamento de 50 min, novos+revisões, extra dirigido separado, calibração real |
| Scripts legados de cópia/validação/upload | Transformar os úteis em adaptadores ou retirar da rota ativa, sem apagar histórico do trabalho |

Não “resolver” a migração anexando novas regras contraditórias ao fim dos arquivos antigos. Revisar os trechos conflitantes, apontar para uma autoridade clara e manter um registro curto da substituição.

## 7. Texto de partida para o modelo executor

```text
Implemente a arquitetura NEBLI descrita em:
- arquivos-trabalho/arquitetura-nebli/ARQUITETURA.md
- arquivos-trabalho/arquitetura-nebli/IMPLEMENTACAO.md
- arquivos-trabalho/arquitetura-nebli/DESCOBERTAS.md
As preferências e correções estão em:
- arquivos-trabalho/arquitetura-nebli-decisoes-2026-09-22.md

Comece pela Entrega A e avance pelas dependências. Leia o estado atual do
repositório antes de editar: há mudanças do usuário que devem ser preservadas.
O alvo de operação é a coleção principal no Mac; a sessão Windows pode preparar
artefatos, mas não deve presumir que seu localhost seja o Anki principal.

O piloto é UC03, Patologia, conteúdo 38 — Inflamação aguda. Gere E1 sempre;
E2/E3 ficam fora. Use objetivos e fontes para curar AnKing, outros decks e
autorais apenas para lacunas reais. Uma cópia NEBLI por origem, associações
por card a várias aulas, histórico preservado, originais independentes.

Não use API paga de LLM. A sessão faz os julgamentos; scripts fazem operações
determinísticas. Não execute mutações legadas nem migração em massa. Construa
os testes de identidade, calendário, importação e recuperação em perfil de
teste antes de aplicar na coleção pessoal. Não invente acesso ao Mac, dados
do Anki, fontes consultadas ou recibos de publicação.

Ao terminar cada entrega, registre arquivos alterados, verificações realizadas
e dependências restantes, e continue para a próxima entrega quando possível.
Não reabra preferências já decididas. Pergunte somente por ambiguidade real
que não consiga resolver nas fontes e que afete a etapa em andamento.
```

## 8. Definição de primeira versão pronta

O usuário pede a aula no Codex; recebe E1, guia e deck completo com prioridades claras; aplica na coleção principal sem duplicar nem perder revisões; estuda no Android; uma segunda aula reutiliza os cards pertinentes; calendário é reconciliado nas próximas execuções; pacotes por aula/UC e recibos correspondem ao estado real. O piloto revela conteúdo ausente ou cards ruins de forma rastreável, permitindo corrigir o processo antes de expandir.

Se algo existir apenas como arquivo preparado, a entrega deve dizê-lo. A arquitetura está completa como especificação; a funcionalidade só está pronta depois desses resultados verificáveis.
