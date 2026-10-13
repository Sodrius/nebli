# Anki e pipeline NEBLI — plano aprovado

Atualizado em 08/10/2026 após F-20261008-CODEX-03. Codex coordena; Claude executa; Astra contribuiu com o diagnóstico inicial. Estado e próxima ação: [ESTADO-ATUAL.md](ESTADO-ATUAL.md). Preferências canônicas: [MEMORY.md](MEMORY.md).

**Estado:** aprovado integralmente por Davi em 08/10/2026 (F-20261008-CLAUDE-01), com execução contínua: as levas seguem em sequência sem esperar retorno; dúvidas são listadas ao fim de cada deck e o feedback é incorporado quando chega (substitui a espera entre levas da seção 7). Progresso em [ESTADO-ATUAL.md](ESTADO-ATUAL.md). Versão anterior integral preservada em `arquivo/2026-10-08-organizacao/`.

**Davi usa o Anki enquanto o executor trabalha (F-20261008-CLAUDE-02): isso não bloqueia.** Preparar fora do Anki e aplicar em lotes curtos mesmo durante a revisão dele; nunca alterar a nota em exibição (`guiCurrentCard`) nem seus irmãos (adiar só essas); não mexer na tela dele; escrita com `sync=False` enquanto ele revisa e sync quando estiver ocioso ou no fim da sessão; readback após cada lote.

## 1. Resultado esperado

O deck representa o planejamento pedagógico da aula: objetivos, conceitos, mecanismos, exemplos, prática e cobrança da prova. O Browser deve permitir reconstruir a história da aula e entender por que cada card está naquela posição. A IA infere a intenção docente pelas fontes, sem inventar falas não registradas.

Primeiro consolidar o pipeline, demonstrar qualidade e corrigir o acervo atual. Depois produzir a biblioteca de decks-aula de 2026. Trabalho **por levas**, com uso e feedback de Davi entre elas. Não executar toda a campanha de uma vez nem fixar um total arbitrário de cards por leva.

Codex mantém direção, dependências e verificação; Claude implementa, produz e revisa. Gates mecânicos não substituem julgamento de cobertura, redação e imagens. Davi comenta durante o estudo; não precisa auditar cada card ou certificar a cobertura técnica.

Somente decks por padrão, sem gerar E1 nesta campanha. E1 existente é fonte auxiliar; E1–E3 continuam disponíveis sob pedido, com rotas acessíveis pela raiz. Etimologia e acervos originais ficam fora da correção. Suspensão pós-prova é manual. A introdução dos decks antigos na rotina será decidida depois por Davi: **retirada integralmente a proposta de 10 cards/dia e a divisão 10/30**.

## 2. Organizar a raiz e a continuidade das sessões

- `README.md`: mapa de entrada e localização dos materiais.
- `CLAUDE.md` e `AGENTS.md`: instruções curtas apontando para os mesmos documentos atuais.
- `MEMORY.md`: única memória normativa de preferências.
- `PLANO-AJUSTES-ANKI-2026-10-08.md`: escopo, etapas e critérios desta campanha.
- `ESTADO-ATUAL.md`: leva atual, ações concluídas, pendências, feedback aguardado e próximo passo.
- `flashcards/projeto/FEEDBACKS.md`: registro histórico das falas e decisões.
- `arquivo/`: documentos superados e versões anteriores, preservados com origem e hash.
- `bibliografia/`: destino local preparado para os livros que Davi poderá copiar; presença local nunca presumida.

Reunir documentos superados em `arquivo/`, conferir integridade e atualizar referências. Código, fontes, livros, mídia, backups técnicos e trabalhos de outras frentes não são lixo por idade. A organização será incremental e sem perda de conteúdo. Referências antigas que ainda forem usadas recebem apontador para o arquivo preservado e para o fluxo atual.

Ao encerrar cada sessão: registrar o que foi realmente feito, o que falta, o feedback incorporado e onde continuar. Não deixar estado relevante dependente do chat privado. Entradas antigas não podem disparar outra fila de produção.

## 3. Fontes obrigatoriamente consideradas antes da seleção

Para cada aula, explorar slides, material docente, exercícios, roteiros, provas, CAOC, bibliografia, apostilas de veteranos/pessoais, canais e referências Step/HY. E1 existente pode complementar a leitura. **Explorar também Outros, Materiais complementares e pastas equivalentes de cada UC.**

A consulta deve definir o que entra, como é perguntado, quanto aprofundar e qual prioridade atribuir. Registrar disponibilidade, material efetivamente lido e contribuição concreta para os alvos do deck. Título de vídeo, busca ou referência bibliográfica não equivale a consulta. Ausência/inaplicabilidade exige justificativa; fonte essencial ausente deixa a aula pendente enquanto avançam tarefas independentes.

**Para matérias anteriores, material extra de veteranos e professores é essencial.** Não tratá-lo como leitura opcional apenas porque os slides já permitem montar cards. Se realmente não houver material pertinente, registrar a busca e resolver a necessidade de cobertura antes de declarar a aula pronta.

A bibliografia está no Drive segundo Davi. Ele poderá copiá-la para a raiz do NEBLI; consultar a pasta local quando estiver preenchida e usar o Drive enquanto isso. Não pedir de novo livro já conhecido. Perguntar apenas quando o livro pertinente continuar indefinido após memória, bibliografia e busca.

| UC | Referências conhecidas |
|---|---|
| UC01 | Lehninger, Alberts, Guyton |
| UC02 | Lehninger, Alberts, Guyton, Junqueira, Netter |
| UC03 | Abbas, Robbins, Lehninger, Trabulsi, Netter; HCFMUSP para clínica pertinente |
| UC08 | Guyton, Margarida/Aires, Junqueira, Alberts, Netter |
| UC17 | Neuroanatomia Funcional, Angelo Machado, 3ª edição, Manole |
| UC19 | Rang & Dale; explorar também Outros |

Consultar o livro pertinente ao componente/tema. Canais indicados: Ninja Nerd, Medicosis Perfectionalis, Osler, Osmosis, Professor Mike, AK Lectures, MK Fisiologia, Dirty Medicine e Shomu’s Biology, especialmente em microbiologia. Selecionar conteúdo pertinente e identificar a contribuição de cada consulta.

## 4. Cobertura, ordem, deduplicação e cards de conexão

Inventariar os alvos da aula antes de selecionar cards. Cada conceito, relação e habilidade prática precisa de destino: recuperação ativa, apoio suficiente ou exclusão didática justificada. Conferência final volta às fontes; não aceitar inventário que apenas repete a seleção feita. Menção no verso não substitui pergunta quando a prova cobra recuperação ou identificação.

Quantidade acompanha o conteúdo. **Não repetir conceitos sem ganho real ou nova perspectiva.** Comparar alvo, resposta e habilidade dentro da aula e entre aulas; reaproveitar identidades compartilhadas quando adequado. Não juntar recuperações independentes para reduzir a contagem. Básicos úteis permanecem disponíveis; Davi suspende os que já domina.

Browser e painel seguem o percurso da aula, do fundamento às relações e consequências, para conectar o estudo dos cards ao que foi visto em sala. Preservar progressão dos novos e associações por aula sem alterar o histórico ou forçar revisões vencidas à ordem dos slides.

**Cards de conexão:** poucos, rosas, em pontos de transição úteis, para recuperar uma ligação causal ou conceitual entre blocos da aula. Devem acrescentar uma relação que ainda não esteja testada; aproveitar um card existente se já fizer esse papel. Padrão AnKing integral: frente natural e curta, um alvo claro, cloze focal, Extra conciso, ênfase econômica e imagem apenas quando ajuda. Não virar resumo da aula, lista de vários mecanismos ou card que explica por que o deck foi organizado assim. Não reduzir a rosa um card HY/central já existente para torná-lo “conexão”; o novo conjunto rosa é apoio integrador complementar. Validar poucos exemplos com Davi na primeira leva antes de ampliar.

## 5. Escrita, imagens, cores e Tab

Buscar AnKing e outros acervos antes de autorar. Cards médicos em inglês, com formulação focal, contexto suficiente e cloze curto/inequívoco; sem resposta vazada. Termos indivisíveis não são mutilados por limite de palavras. Extra específico e curto; explicação aprofundada no Tab. Não inserir bastidores de curadoria.

A imagem sustenta diretamente o alvo, com pouco ruído. Conferir estrutura/processo, painel, seta, máscara, rótulos, tamanho, legibilidade e vazamento. Recortar quando resolver; substituir quando a imagem continuar inadequada. Revisar o card renderizado, não só o arquivo. Preservar exemplos elogiados. Anatomia: estilo visual AnKing, Netter, BlueLink e cadáver pertinentes. Histologia: lâmina/esquema adequado ao reconhecimento ou mecanismo exigido. Remover créditos visíveis dos campos/rodapés, mantendo procedência técnica e legendas científicas úteis.

| Cor | Critério |
|---|---|
| Verde | Conhecimento central e duradouro; fisiologia, anatomia e relações clínicas pertinentes. Todo HY pertinente verde. |
| Azul | Importante para a prova, com menor prioridade longitudinal. |
| Rosa | Útil para a prova e dispensável no futuro; inclui os poucos cards complementares de conexão. |

Sem quota de verdes. Julgar o alvo e o ganho incremental; preservar marcas pessoais e tratar conflitos explicitamente. Não remover conteúdo necessário para caber na rotina.

**Tab único, mantendo o funcionamento atual.** Cancelada a proposta de versão curta/longa ou duas colunas. Garantir uma explicação correta e didática, do fundamento ao mecanismo e à resposta, com contexto da aula, termos difíceis definidos e prosa encadeada. Sem preenchimento genérico ou numeração mecânica. Conferir qualidade substantiva e atualização em 100% dos cards do escopo; teste quantitativo sozinho não certifica explicação boa. Mudança no card exige revisar a explicação correspondente. Não alterar silenciosamente cache/prompt em uma sessão de planejamento.

## 6. Corrigir a coleção atual e reconstruir UC03

Inventário lido em 08/10: 1.178 cards médicos, 1.025 notas e 88 comentários médicos. Dez comentários têm novas críticas após o último CORRIGIDO. **Davi esclareceu que muitos marcadores vêm de correções ruins: todos precisam ser revalidados**, mesmo sem texto posterior ao marcador.

| Conjunto | Ação |
|---|---|
| UC08 — nove aulas, 798 cards | Corrigir cobertura, redundância, escrita, imagens, cores, ordem e Tab |
| UC03 — GR02, 114 cards | Preservar e corrigir problemas pertinentes |
| UC03 — Correlação patológica-radiológica 2, 56 cards | Preservar; autoria Claude confirmada; revisar |
| UC03 — Morfologia bacteriana, 36 cards | Apagar/substituir versão Codex e reconstruir pelo Claude |
| UC03 — Edema e congestão, 67 cards | Apagar/substituir versão Codex e reconstruir pelo Claude |
| UC03 — Patologia ambiental, 41 cards | Apagar/substituir versão Codex e reconstruir pelo Claude |
| UC03 — Biologia geral dos fungos, 66 cards | Apagar/substituir versão Codex e reconstruir pelo Claude |

Executar com backup, inventário atualizado e mapa antigo→novo. Preservar comentários, histórico de alvos equivalentes e compartilhados de outras aulas. Novos alvos não herdam artificialmente revisão de conteúdo diferente. UC19 ausente na leitura inicial será produzida na Geração 2026 com o material disponível, sem restaurar pacote rejeitado por inferência.

Para cada comentário: ler card e feedback completo → identificar padrão → localizar semelhantes → corrigir → verificar → **dessuspender o card corrigido se estiver suspenso** → acrescentar no comentário `CORRIGIDO, DD, MM, YY.` com a data real (ex.: `CORRIGIDO, 08, 10, 26.`). Preservar todo o texto e marcadores anteriores. Releitura sem mudança não autoriza marcar nem dessuspender; a regra vale para correção efetivamente realizada e validada, não para liberar decks inteiros. Se a correção afeta vários cards, conferir os irmãos e os IDs dessuspensos. Suspensão pós-prova continua manual.

Aplicar o aprendizado a todos os cards médicos da família, inclusive sem comentário e cópias AnKing. Positivos também calibram. Incorporar resultado aos specs/plans para evitar regressão no próximo build.

## 7. Levas de execução e feedback

Após aprovação, a primeira leva proposta combina consolidação do pipeline com correções representativas de histologia UC08, anatomia, mecanismo fisiológico, Tab e poucos cards de conexão. Usar exemplos comentados bons/ruins e outros semelhantes para verificar generalização. O tamanho acompanha a capacidade de revisar bem, sem quota artificial.

Ciclo de cada leva:

1. Definir alcance concreto e consultar as fontes necessárias.
2. Claude prepara, aplica e revisa; Codex verifica o resultado e as evidências.
3. Entregar o que mudou e o que falta, com exemplos úteis.
4. Davi usa e dá feedback.
5. Registrar e incorporar o feedback, corrigindo regressões antes de expandir o padrão.
6. Atualizar ESTADO-ATUAL e seguir à próxima leva depois do retorno de Davi.

Não interpretar silêncio como aprovação da leva seguinte. Esperar feedback não transfere a revisão técnica para Davi; tarefas independentes de levantamento e preparação podem continuar. Não exigir confirmação por card.

Depois do piloto, ampliar por famílias/aulas: histologia UC08 → anatomia UC08 → fisiologia UC08 → GR02/PR02 → reconstruções UC03, ajustando a ordem ao feedback. Ajustes técnicos e renomeações podem avançar em levas próprias. A etapa final de geração também seguirá esse ciclo.

## 8. Ajustes de uso, Drive e entrega

- **Heatmap:** verde quando cumprir a meta de novos únicos vigente. Repetições/reaprendizagem não contam novamente; respeitar dia do Anki e desfazer. Conferir configuração real sem impor nova distribuição diária. Meta cumprida não significa revisões zeradas.
- **Ordem:** verificar Browser, painel e sequência dos novos, inclusive compartilhados. O deck deve reconstruir a lógica da aula.
- **Tab:** uma explicação atual por card, interação preservada e qualidade verificada.
- **Pós-prova:** nenhuma suspensão automática; dessuspensão restrita aos cards efetivamente corrigidos conforme a regra anterior.
- **Dispositivos:** conferir desktop e renderização móvel; não confundir prévia responsiva com teste real no AnkiDroid nem afirmar sincronização do Tab enquanto depender de SQLite local.
- **Slides:** mapa de renomeação para `<Aula> - slides.<extensão>`, preservando partes/versões e conferindo cronograma quando pasta e arquivo discordam. Exercícios e roteiros mantêm sua identificação. Não apagar variantes, alterar conteúdo ou converter formato só pela extensão.
- **Entrega:** atualizar referências locais, conferir nomes no Drive e publicar pacotes corrigidos segundo a política vigente. Verificar versão/hash e conteúdo/mídia contra a coleção atual; existência de arquivo não comprova atualização. Registrar sincronização realizada e limites reais.

A revisão de Astra já apontou que a entrega atual copia slides e verifica existência de arquivo: isso não comprova renomeação dos originais nem atualidade do pacote. Corrigir essas verificações na execução.

## 9. Condição para ampliar a produção

Pipeline e levas iniciais precisam demonstrar: fontes usadas de verdade, cobertura fiel, deduplicação com ganho preservado, escrita AnKing, imagens direcionadas, cores justificadas, Tab bom, ordem pedagógica, comentários revalidados e entrega atual. Claude realiza a revisão técnica; Codex verifica; o feedback de uso de Davi calibra o padrão antes da expansão.

Os decks atuais devem estar tratados no alcance previsto, as quatro versões Codex UC03 substituídas e os artefatos de geração reconciliados. Testes cobrem regressões concretas de mídia, identidade/compartilhados, Tab, cores, ordem, dessuspensão pós-correção e heatmap. Não declarar tudo revisado com base apenas numa amostra ou aprovação automática.

## 10. Etapa final — Geração 2026

**Ordem escolhida por Davi: UC03 → UC19 → UC21 → UC02 → UC01.**

Produzir decks-aula de todas as aulas de 2026 dessas UCs com material no Drive. UC03 inteira inclui todas as aulas disponíveis; aproveitar os decks já adequados e as reconstruções anteriores, sem duplicá-los. UC08 permanece no escopo de correção; UC17 tem bibliografia registrada, fora da campanha.

Campanha gradual, em várias sessões e **por levas com feedback**. Primeiro qualidade demonstrada; depois ampliação. Não há prazo artificial de um dia nem plano de distribuição diária: Davi decidirá depois como introduzir os decks no estudo.

### Inventário vivo

Cruzar cronogramas, aulas/casos, provas e todas as fontes, incluindo Outros e Materiais complementares. Estado por aula: já adequada; precisa reconstrução; pronta para produzir; aguardando fonte essencial; em produção; em revisão; entregue. Reler o Drive a cada retomada e antes de cada aula. Aula sem material não será inventada. Fonte essencial ausente deixa a aula pendente sem paralisar as independentes.

A bibliografia está no Drive segundo Davi; verificar cópia local quando houver. **A apostila de lâminas já está no Drive segundo Davi**: localizar e ler na produção da UC02, em vez de mantê-la como material futuro. Se não for encontrada, registrar dificuldade de localização. Materiais novos alteram o planejamento e podem exigir atualizar um deck já entregue.

### Método por aula

Consultar fontes → reconstruir percurso e objetivos → inventariar alvos → buscar acervos → selecionar/redigir sem redundância → cores → imagens/oclusões → poucos cards de conexão quando agregarem → Tab único → instalar em ordem → revisar contra fontes e coleção → entregar a leva → incorporar feedback.

Conteúdo recuperável dos slides, habilidades práticas e demandas da prova precisam de cobertura efetiva. Material de veteranos/professores é essencial nas matérias anteriores. E1 existente é auxiliar; não gerar nova E1. Reaproveitar compartilhados com acesso e posição por aula. Registrar continuidade sem depender de chats privados.

### UC21 / DIC

Caso guia cobertura; perguntas oficiais e HY guiam verde. Integrar básico e clínico com amplitude e nível introdutório. Construir fundamentos e fisiopatologia antes de manejo específico: por exemplo, manejo de ICC de VD não substitui compreensão da fisiopatologia do caso. Bibliografia, apostilas e materiais do caso determinam o aprofundamento adequado.

### UC02 / biologia tecidual

Identificação histológica foi grande parte da UC e é essencial na prova. Usar apostila de lâminas já disponibilizada, material docente, provas, bibliografia e Histology Guide conforme o alvo. Perguntas devem cobrar reconhecimento real e características discriminantes, com imagens/oclusões claras; teoria textual não substitui prática. Não impor teto histórico de 25% de identificação à UC02.

### Conclusão

A Geração 2026 estará concluída para o inventário vigente quando todas as aulas elegíveis tiverem deck entregue e verificado. Aulas aguardando fonte essencial permanecem explicitamente pendentes; não declarar conclusão integral enquanto existirem. Novos materiais entram na fila de atualização.

Resultado: biblioteca de decks-aula fiel ao ano, com qualidade comprovada, sem redundância conceitual inútil e com sequência que ajuda a reconstruir a aula. Davi define posteriormente como estudar esse acervo no dia a dia.


## 11. Encerramento — add-on NEBLI compartilhável (pedido de 08/10)

Após a campanha de ajustes/decks, reunir os três add-ons próprios e suas funções em um único **add-on NEBLI**. Terceiros, incluindo Review Heatmap, permanecem separados. Escopo, alterações do Browse (J, Suspenso e ordem só numérica), migração de configurações/Tabs e critérios de pacote instalável em [ADD-ON-NEBLI.md](ADD-ON-NEBLI.md). Documentação criada; pacote único ainda pendente.


## Ajuste de 10/10/2026 — ritmo pelas provas e custo menor (F-20261010-CLAUDE-01)

- **Prioridade = prova mais próxima.** UC03 P3 (prova TA em 06/11/2026): decks na ordem das aulas, cada um pronto poucos dias depois da aula, para o estudo seguir a matéria sem acúmulo. UC08 P2: intercalar pela data da prova assim que o cronograma for conferido. Regerar UC03 P2 (prova já feita em 02/10, decks suspensos) fica para depois da P3, salvo pedido.
- **Uma passada por aula** pelo Roteiro enxuto (EXECUCAO-DECK-AULA): molde `nebli/molde`, `nebli.corrida molde|fontes|cego|revisado`. Gates continuam duros; o que sai é retrabalho (releituras, despejos completos, renders sem necessidade, rodadas cegas repetidas).
- **Canais do YouTube:** com bloqueio de transcrição, a aula sai com o material de base completo e a leitura dos vídeos vira pendência listada (não bloqueia a entrega).
- **Perguntas a Davi** só ao fim de cada deck, objetivas, sem parar a fila.
