# NEBLI Decks — plano de implementação v2

> Atualização 23/09/2026: [CALIBRACAO-ESCALA-V4.md](CALIBRACAO-ESCALA-V4.md) prevalece sobre este plano histórico. Seleção ampla pré-prova e manutenção menor pós-prova são fases distintas; suspensão só após proposta confirmada. E1 explicativa + guia + Anki + APKG privado são a entrega atual. Operação assistida em [OPERACAO-CODEX-CLAUDE.md](OPERACAO-CODEX-CLAUDE.md); não confundir roadmap com funcionalidades testadas.

Este arquivo é o roadmap de software do comando genérico, não o procedimento de curadoria de cada aula. Para gerar um deck hoje, use [EXECUCAO-DECK-AULA.md](EXECUCAO-DECK-AULA.md). Ao programar a automação, leia [README.md](README.md) e [ARQUITETURA.md](ARQUITETURA.md). O formato dos pilotos está aprovado; melhorar integração sem refazer a experiência.

## Estado inicial e limites

Há `nebli/cli.py`, `registry.py`, `anki_apply.py`, seleção/objetivos dos pilotos, recibos e decks instalados. São componentes iniciais, não o comando completo. Os fluxos de Inflamação e Vascularização foram executados por scripts específicos dentro de `arquivos-trabalho/`; servem como evidência, não como API genérica. Reaproveitar utilitários legados depois de inspecioná-los, nunca executar um script de escrita só porque tem “dry” no nome.

Problemas já observados: aplicação por nota em vez de card; tipo de nota compartilhado com AnKing; tag da aula fixa no código; reutilização move os cards; cobertura sem verificação semântica; recibo de dry-run no caminho da aplicação; registro insuficiente para associações e calendário. Fonte/download/publicação devem ser estados comprovados, não preenchidos por seed estático.

O worktree contém alterações de outras tarefas, inclusive exclusão de `FLASHCARDS.md` observada durante a preparação. Não restaurar esse arquivo, descartar diffs, rodar reset ou presumir que a exclusão é erro. Adicionar roteamento para esta especificação sem reescrever regras alheias.

Não escrever no Anki/Drive para validar arquitetura. Implementação de mutações começa com mocks e perfil isolado; adoção no perfil principal somente no escopo solicitado e com salvaguardas.

## Fatias de entrega

### P0 — diagnóstico, identidades e contratos

Objetivo: reconhecer o ambiente real e tornar a seleção auditável antes de sofisticar o gerador.

- Configurar coleção/host/perfil, fontes e destinos sem caminho fixo Windows/Mac.
- Diagnóstico somente leitura: versão/capacidades, modelos, mídia, deck/card/note IDs, flags e suspensões observadas; indicar o que não é possível inferir sobre sync.
- Schemas versionados de fonte, escopo, seleção por card, prioridade, recibo e operação; validação explícita.
- Expandir migrations para notas/cards/associações, prioridades, buscas e operações. Migração separada de status.
- Snapshot consistente; mapear cópias do piloto e originais. Colisão/duplicata vira relatório, não deleção.

Aceite: duas leituras não mudam Anki/Drive; schema inválido falha com mensagem; 31 notas versus 45 cards corretamente separados; nenhum passo promete GUID via API sem verificar suporte.

### P1 — extração e delimitação da aula

Objetivo: definir exatamente o que os cards devem cobrir.

- Resolver título/link/material para `lesson_id`, disciplina, componente, fontes e relações curriculares.
- Extrair texto visível, comentários/transcrição e figuras; preservar página/localizador e status de acesso.
- Modelo lê materiais e produz `scope.json` usando taught/recap/prerequisite/bridge/illustration/future/out_of_scope.
- Cruza provas pertinentes e consulta bibliografia disponível para precisão, sem transformar o capítulo em escopo.
- Auditar exclusões: conteúdo realmente dado não pode desaparecer do mapa por dificuldade de busca.

Aceite no piloto: p. 13 e pp. 33–35 recuperadas apesar de conteúdo em figuras/comentários; distinção flegmão/abscesso preservada; doenças inteiras relacionadas à fagocitose não viram obrigação; Robbins informado mas edição/capítulo não acessados ficam explícitos. Caso sem slides também produz escopo a partir do material fornecido.

### P2 — busca ampliada e curadoria por card

Objetivo: encontrar o que já existe antes de criar.

- Índice FTS local incremental, campos originais preservados, normalização e tags por recurso/tema.
- Plano de busca por objetivo; camada de identidade NEBLI; AnKing primeiro para novas perguntas; depois corpus externo adequado.
- Consultas textuais e taxonômicas independentes; segunda busca obrigatória para pendências relevantes, sem teto arbitrário de cards retornados.
- Paginação para o modelo, triagem e seleção pelo que o cloze realmente exige; registro de rejeições e fora de escopo.
- Deduplicação de origem e análise de redundância semântica sem apagar histórico. Reaproveitar cópia já revisada quando apropriado.

Aceite: recuperar candidatos de [CALIBRACAO-INFLAMACAO.md](CALIBRACAO-INFLAMACAO.md); rejeitar Crohn como cobertura de morfologia; rejeitar IgA como cobertura de transcitose vascular; distinguir verso explicativo de simples palavra no Extra; não selecionar todos os irmãos por herança da nota. Não chamar corpus inacessível de “sem cards”.

### P3 — auditoria, prioridades e prévia do piloto

Objetivo: calibrar conteúdo e sinalização antes da escrita.

- Modelo executa auditorias fontes→mapa, mapa→cards e cards→escopo.
- Cobertura separa obrigatório, apoio, ponte, pré-requisito e exclusão. Não usar porcentagem de conceitos encontrados por substring como selo de completude.
- Normalizar yield das tags mantendo rótulos brutos; admitir desconhecido/conflitante; não inferir prioridade para a faculdade ou grupo de retenção.
- Gerar relatório de cobertura e das flags já existentes; não aplicar cores automaticamente.
- Finalizar autoria mínima somente para lacunas ainda reais. Verso explicativo pode fechar aprendizagem; criar pergunta própria apenas quando o recall ativo trouxer ganho claro.

Aceite: HY fora da aula excluído; LY obrigatório local mantido; ausência de tag não vira LY; flag pessoal intocada; nenhum objetivo obrigatório parcial recebe “pronto”. Autorais sempre trazem evidência de busca e fonte. Não impor novo teste de aprendizagem ao usuário.

**Marco útil:** ao concluir P3, já existe uma seleção melhor e auditável para Inflamação aguda. Não esperar construir um mapa de todo o Step 1 para corrigir o piloto.

### P4 — aplicação segura e compartilhamento entre aulas

Objetivo: instalar essa seleção preservando tudo que importa.

- Implementar adaptador com interface de alto nível: inventariar, planejar diff, aplicar, conferir, exportar. Descobrir/testar métodos reais disponíveis.
- Separar tipo de nota NEBLI de AnKing sem mudar originais. Preservar aparência aprovada, campos úteis, mídia, atribuição e identidade.
- Metadados por card/cloze no manifesto; não renderizar rótulos de prioridade no verso.
- Home deck estável, relações N:N e visualizações por aula; corrigir deslocamento automático no ramo de reutilização.
- Journal, locks, dry-run genuíno, precondições, atualização com preservação de edições e reconciliação de resultados desconhecidos.

Aceite isolado: mesma execução duas vezes cria zero novas cópias na segunda; adicionar aula de Imunologia não desloca/perde o card de Patologia; usuário suspende/edita/flagga e reexecução preserva; timeout após add é reconciliado; tipo de nota original não muda; reexecução não substitui recibo verdadeiro por planejamento. Contagens e mídia conferidas por readback.

Depois do aceite, adoção controlada dos cards já existentes do piloto, sem resetar revisões nem fusão de históricos. Se a migração de modelo não preservar identidade no ambiente real, interromper essa migração específica e resolver antes de escrever.

### P5 — E1/guia, calendário e carga no comando único

Objetivo: reduzir trabalho manual sem inflar o deck.

- E1-only com build isolado por execução, mantendo boas regras editoriais sem ativar E2/E3.
- Guia de recursos, pré-requisitos externos e pontes; validar links/trechos e distinguir indicação de consulta efetiva.
- Ler aba Mês e reconciliar datas/vínculos; manter manual overrides e múltiplas associações.
- Política de liberação e reconciliação das pendências de calendário em execução, sem daemon. Não usar checkbox de tarefa como evidência de conhecimento.
- Relatório de ritmo com dados reais e incerteza, sem classificar automaticamente núcleo/prova/reserva. Preservar agendador e parâmetros atuais inicialmente.

Aceite: reagendar prova atualiza pendências, não reescreve cards/E1 nem causa suspensão inferida; futuro não suspende revisão ativa; múltiplas associações aparecem antes de qualquer decisão; flag HY não impede suspensão manual; ausência de data não aciona pausa; E1 não aumenta só porque um card tem muito Extra. Cinquenta minutos não viram uma quota fixa de 400 cards.

### P6 — APKG, Drive e integração completa

Objetivo: entregar e atualizar arquivos sem retrabalho do usuário.

- Exportar aula e união da UC com identidade canônica, proveniência e mídia; prototipar o comportamento de irmãos cloze compartilhados.
- Ensaiar importações limpa/existente, aula→UC→aula e UC→aula; comparar conteúdo, GUID/card IDs quando aplicável, histórico, flags e suspensões.
- Se pacote autossuficiente não preservar seleção exata, não mascarar a limitação. Implementar reconciliador documentado ou resolver o exportador antes de declarar o formato pronto.
- Configurar pasta pessoal e permissões; publicar por file_id estável; ler estado após upload; atualizar links autorizados da planilha.
- Um orquestrador retoma da última fase válida. Erro de upload não dispara nova aplicação de cards.

Aceite: arquivos abrem no destino, mídia funciona em Mac/Android testados, importações repetidas não duplicam nem sobrescrevem versões novas com antigas, artefatos pertencem à mesma versão do mapa. Falha simulada de Drive deixa estado parcial correto e retoma sem mexer no Anki.

**Marco de produto:** “gere o deck da aula X” está pronto somente quando P0–P6 passam numa aula real, numa interseção de aulas e numa reexecução. Antes disso, chamar o resultado de piloto/fluxo parcial.

### P7 — escala gradual e acompanhamento longitudinal

- Validar três perfis de aula: factual/mecanística; anatomia/histologia com IO; caso/PBL integrador.
- Manter conjunto de exemplos de inclusão/exclusão aprovado e feedback de decisões específicas. Não transformar uma preferência de uma aula numa regra global sem evidência.
- Fechar UC/sistema com visão de cobertura curricular Step; alocar pendências a futuras aulas ou recuperação avulsa.
- Comando de complementar por erro, questão ou print usa a MESMA identidade, curadoria e prioridades, não um segundo gerador.
- Tutor, compartilhamento e grandes recuperações entram depois, não como bloqueadores do comando inicial.

## Organização de código proposta

Manter o pacote `nebli/`; extrair responsabilidades conforme a fatia, não criar todos os arquivos vazios antecipadamente:

| Módulo proposto | Responsabilidade |
|---|---|
| registry / schemas | Estado operacional, migrations, validação dos contratos |
| sources / scope | Fontes e mapa decidido pelo modelo |
| corpus / search | Índice e buscas reproduzíveis |
| curation / coverage | Decisões e verificações estruturais; sem fingir julgamento semântico por regex |
| priorities / calendar | Prioridades, grupos, elegibilidade e overrides |
| anki_adapter / operations | Preflight, diff, journal, apply e readback |
| artifacts / publication | E1/guia, pacotes e publicação por identidade |
| pipeline / cli | Um fluxo retomável, status e relatório final |

O modelo produz julgamentos estruturados, citando fontes e candidatos. O software confere integridade, permissões, invariantes e estado. Um script não precisa chamar API de IA para o fluxo funcionar na sessão.

## Interfaces propostas — ainda não instaladas

```text
nebli doctor
nebli inventory
nebli plan <aula-ou-link>
nebli audit <run-id>
nebli apply <run-id>
nebli resume <run-id>
nebli status <aula-ou-run-id>
nebli aula <aula-ou-link>
nebli complementar <aula> <material-ou-erro>
```

O usuário não precisa aprender a sequência: `aula` é a entrada única após implementação. `plan/apply` existem para diagnóstico, ensaio e controle interno. Pedidos “avalie”, “planeje” ou “o que falta?” nunca são interpretados como autorização para aplicar.

## Regressões mínimas

| Caso | Resultado obrigatório |
|---|---|
| Biblioteca cita o assunto, mas a aula não o dá | Não ampliar escopo automaticamente |
| Pré-requisito já estudado | Referenciar, não duplicar/reinserir no principal |
| Mesmo alvo realmente cobrado em duas aulas | Uma revisão, duas associações |
| LY AnKing e alta cobrança local | Incluir com rótulos distintos |
| Sem tag de yield | Desconhecido, não LY |
| Objetivo explicado adequadamente no verso | Contar como cobertura para aprender; decidir separadamente se merece recall ativo |
| Nota com irmãos fora do escopo | Não ativar/exportar cegamente todos |
| Busca de nome sem resultado, tag alternativa com candidato | Recuperar antes de autoria |
| Timeout depois de criar nota | Reconciliar antes de repetir |
| Mudança manual entre plan e apply | Detectar e preservar/solicitar decisão localizada |
| Prova remarcada ou segunda prova vigente | Recalcular sem perda de conteúdo/histórico |
| APKG de aula e UC sobrepostos | Não duplicar; não sobrescrever versão mais nova sem detecção |
| Falta bibliografia/Drive indisponível | Pendência honesta, trabalho independente preservado |

## Entrega esperada ao usuário

Exibir total de cards reais, quantos já existiam/novos/compartilhados; origem da seleção; lacunas e exclusões importantes; verdes por HY literal, vermelhos, suspensos e não classificados; fontes e onde aprender; pendências de calendário; links e estado de instalação/exportação/publicação. Não produzir “núcleo/prova/reserva”, prioridade de faculdade ou MY/LY por inferência. Métricas de origem são diagnóstico, nunca metas de percentual.

## Passagem para o modelo executor

> Implemente NEBLI Decks seguindo `flashcards/projeto/README.md`, `ARQUITETURA.md` e este roteiro. Comece por P0, confirme o estado atual e preserve o worktree. O piloto AnKing-first foi aprovado; não redesenhe o produto. Construa uma fatia por vez com testes, registre o que realmente passou e avance enquanto houver próximo passo seguro no escopo. Não escreva no Anki principal/Drive durante ensaios nem trate preferências pendentes como resolvidas. O objetivo final é um comando por aula, completo dentro do recorte, com prioridade visível, sem duplicar histórico e com autoria apenas para lacunas reais. Não contrate API, não reative E2/E3 e não imponha testes adicionais ao aluno. Se pedir só planejamento ou auditoria, mantenha leitura externa.

## Pendências específicas, não perguntas repetidas

1. Edição/capítulo do Robbins & Cotran quando a revisão bibliográfica depender disso.
2. Perfil/máquina de aplicação e destino privado para publicação, antes das respectivas mutações.
3. Compatibilidade de modelos, IO, exportações sobrepostas e mídia nos dispositivos reais.

Escopo por aula, inglês com apoio PT, prioridade AnKing, ausência de teto rígido, E1 junto e E2/E3 suspensas NÃO são pendências.
