# Ajustes do Anki e do pipeline — proposta para aprovação

08/10/2026. Codex coordena e verifica; Astra participa da análise do plano; Claude executará as mudanças após aprovação. Esta rodada prepara o plano e registra as decisões: nenhuma alteração nos cards, no agendamento ou nos arquivos do Drive foi aplicada.

## 1. Resultado esperado e escopo confirmado

O deck deve reproduzir a aula e seu percurso, cobrir o que precisa ser aprendido e distinguir o que vale reter por anos do que serve principalmente à prova. Cada pergunta e imagem têm um alvo claro. Os autorais devem ter a naturalidade, concisão e apresentação dos bons cards AnKing. O feedback desta rodada deve melhorar tanto a coleção atual quanto as próximas entregas.

Três entregas principais: corrigir os decks médicos atuais, ajustar o pipeline e padronizar os nomes dos slides no Drive. Incluem-se heatmap da meta, Tab longo/curto e ordem no painel. **Suspensão pós-prova será manual, por Davi.** Etimologia e acervos originais ficam fora da correção. Não gerar E1; decks passam a ser a entrega padrão. E1–E3 continuam disponíveis mediante pedido explícito, com acesso e instruções na raiz.

A etapa final **Geração 2026** produzirá progressivamente decks das aulas de UC01, UC02, UC03 inteira, UC19 e UC21 que tenham material no Drive. Só começa depois do pipeline ajustado e validado. UC08 permanece no escopo de correção atual; UC17 fica com bibliografia registrada, fora dessa campanha. A fila antiga não inicia produção paralela. Este documento continua sendo uma proposta para aprovação, não uma execução já iniciada.

## 2. Base examinada

Leitura da memória, feedbacks, roteiro e artefatos de correção; consulta à coleção aberta via AnkiConnect; leitura de todos os 98 comentários, dos quais **88 são médicos**; inspeção de exemplos de mídia e inventário de nomes no Drive pessoal montado. Evidências em `arquivos-trabalho/plano-ajustes-2026-10-08/`.

| Coleção médica viva | Cards físicos | Ação |
|---|---:|---|
| UC08 — nove aulas | 798 | Revisar cobertura, cores, redação, imagens, ordem e Tabs; corrigir famílias de problemas |
| UC03 — GR02, diabetes | 114 | Preservar o deck; corrigir comentários e padrões pertinentes |
| UC03 — Correlação patológica-radiológica 2 | 56 | Preservar: autoria Claude documentada; incluir na revisão |
| UC03 — Morfologia e estrutura das bactérias | 36 | Reconstruir pelo Claude |
| UC03 — Edema e congestão | 67 | Reconstruir pelo Claude |
| UC03 — Patologia ambiental | 41 | Reconstruir pelo Claude |
| UC03 — Biologia geral dos fungos | 66 | Reconstruir pelo Claude |
| **Total atual** | **1.178** | **1.025 notas; contagem não é meta do resultado** |

UC19 não aparece na árvore atual. A Geração 2026 produzirá seus decks a partir do material disponível e do pipeline validado, sem restaurar o pacote antigo por inferência. Os números acima contam localização física; a execução também deve recuperar associações entre aulas por tags.

Há **dez comentários médicos com texto posterior ao último marcador CORRIGIDO**. Revisar também os demais já marcados. Exemplo confirmado: o card sobre reto e vagina apresenta a prancha completa com pelve masculina acima da feminina. Outro exemplo: o card de células serosas usa uma figura com dois painéis e numerosos alvos; recortar apenas título/legenda não resolve a dispersão. Isso exige seleção da imagem pelo objetivo do card, não apenas por procedência ou existência de um arquivo.

Limite desta investigação: fundamenta o plano; não certifica revisão científica de todos os cards, leitura de todos os capítulos ou teste no AnkiDroid. Essas verificações pertencem à execução.

**Contribuição do Astra:** revisão do diagnóstico do pipeline, sem edição nem leitura da versão final deste documento. Confirmou a necessidade de reconciliar geradores antigos, tratar comentários por família e separar evidência de qualidade dos gates declaratórios. Apontou ainda que `nebli/entrega.py` copia slides e que o gate de Drive verifica existência, não atualidade. Portanto, renomeação efetiva e correspondência dos pacotes à coleção corrigida precisam de verificações próprias nesta execução.

## 3. Critérios que devem governar o resultado

### Aula, fontes e cobertura

- Reconstruir o percurso docente com slides completos, material do professor, exercícios, provas antigas e CAOC. Distinguir o que a fonte demonstra do que a IA infere sobre a explicação oral.
- Usar bibliografia e Step 1 para aprofundar os fundamentos e aplicações pertinentes. Apostilas de veteranos e vídeos calibram detalhes, ênfase e lacunas. Não importar uma aula inteira de clínica a partir de uma doença mencionada como exemplo.
- **A checagem de todas as famílias de fontes indicadas é parte central do planejamento de cada aula.** Conferir slides, demais materiais docentes, exercícios, provas, CAOC, bibliografia pertinente, apostilas de veteranos/pessoais, canais e Step 1; considerar E1 existente como fonte auxiliar. Registrar disponibilidade, leitura do material pertinente e contribuição concreta para cobertura, profundidade, forma de cobrança e cores. Fonte não aplicável ou não localizada recebe justificativa e busca, nunca é omitida silenciosamente. A E1 não substitui a conferência das fontes e não será gerada nesta rodada.
- Criar o inventário da aula **antes** de procurar cards. Cada alvo recebe card, apoio suficiente ou exclusão didática justificada. A conferência final volta às fontes: o inventário não pode apenas repetir os cards escolhidos.
- Não limitar cards por aula nem cores para caber numa quota. Os cerca de 91 cards/aula relatados não são teto ou objetivo. Manter básicos úteis; Davi suspende o que já domina.
- Buscar AnKing e outros acervos antes de autorar. Redundância é a mesma recuperação sem ganho: conservar perguntas complementares que ensinam relação, contraste ou profundidade. Não juntar fatos independentes para aparentar redução de volume.
- Livro já conhecido não exige nova pergunta. Se continuar incerto depois de memória, bibliografia da UC e Drive, perguntar antes de gerar. Fonte essencial inacessível exige resolver a lacuna; registrar busca não equivale a leitura.

Bibliografia confirmada pelo usuário:

| UC | Referências |
|---|---|
| UC01 | Lehninger, Alberts, Guyton |
| UC02 | Lehninger, Alberts, Guyton, Junqueira, Netter |
| UC03 | Abbas, Robbins, Lehninger, Trabulsi, Netter; referências HCFMUSP para clínica pertinente |
| UC08 | Guyton, Margarida/Aires, Junqueira, Alberts, Netter |
| UC17 | Neuroanatomia Funcional, Angelo Machado, 3ª edição, Manole |
| UC19 | Rang & Dale; consultar também a pasta Outros |

Consultar o livro pertinente ao componente/tema, não todos os livros da UC indiscriminadamente. Preservar referências adicionais já confirmadas na memória quando aplicáveis. UC21/DIC: o caso guia a cobertura; perguntas oficiais e HY orientam o núcleo verde; desenvolver a base clínica e fisiopatológica introdutória antes de manejo específico. Amplitude não é sinônimo de especialização precoce.

Canais indicados: Ninja Nerd, Medicosis Perfectionalis, Osler, Osmosis, Professor Mike, AK Lectures, MK Fisiologia, Dirty Medicine e Shomu's Biology, especialmente para microbiologia. Identificar o canal/vídeo correto e usar conteúdo efetivamente consultado; seleção pertinente por tema, sem transformar toda a lista numa obrigação de assistir a todos em cada aula.

### Redação, imagens e cores

- Frente focal, cloze curto e inequívoco, sem resposta vazada nem adivinhação por oposição. Inglês nos cards médicos, conforme preferência já estabelecida. Termo técnico indivisível não deve ser mutilado por limite de palavras.
- Extra curto e específico, com explicação útil e ênfase econômica no estilo AnKing. Não inserir bastidores, localizadores de slides ou parágrafos genéricos. Comentário do usuário permanece separado e íntegro.
- A imagem deve sustentar diretamente o alvo. Escolher painel/estrutura/processo, verificar seta, máscara, rótulos, legibilidade e tamanho; trocar a fonte quando recorte não resolver. Não obrigar imagem decorativa em toda pergunta nem removê-la quando é necessária para compreender.
- Histologia: lâmina ou esquema adequado à característica cobrada; pouco ruído e orientação visual suficiente. Anatomia: valorizar o estilo AnKing de cloze visual, Netter e BlueLink/cadáver quando pertinentes. Preservar exemplos elogiados.
- **UC02: identificação de lâminas é essencial**, conforme ensino, materiais práticos e formato das provas. Planejar recuperação visual real de tecido/estrutura e características discriminantes, usando imagens adequadas, incluindo as apostilas de lâminas que Davi acrescentará. Não aplicar o teto histórico de 25% de identificação como regra universal à UC02; teoria e prática devem acompanhar o planejamento pedagógico da matéria.
- Retirar créditos visíveis em campos/rodapés do card; manter procedência técnica. Não apagar legendas científicas úteis nem marcas incorporadas aos pixels por automatismo.
- **Verde:** conhecimento duradouro, central e conectado; priorizar fisiologia, anatomia e relações clínicas compreensíveis. Todo HY pertinente deve receber recomendação verde. **Azul:** importante para a prova, com menor prioridade longitudinal. **Rosa:** útil para a prova, dispensável na manutenção futura. Incerteza real fica explícita, sem atribuição automática de cor.
- Cor acompanha o alvo, não a disciplina ou a simples presença de uma doença. Reconciliar marcas pessoais; preservar vermelho/comentários pendentes e guardar recomendação separada em caso de conflito. Não declarar HY resolvido enquanto houver conflito sem tratamento.

## 4. Sequência de execução do Claude

### A. Consolidar regras e preparar mudanças

1. Reler a coleção e os comentários na hora de executar. Criar backup restaurável, inventário de IDs, campos, mídia, estudo, flags, suspensões, associações e Tabs. Preservar o trabalho concorrente.
2. Reconciliar `MEMORY.md`, `AGENTS.md`, `CLAUDE.md`, índice, roteiro, instruções dos agentes e fila. Eliminar divergências sobre E1 padrão, tamanho fixo de Tab, suspensão automática pós-prova, revisão por amostra versus completa e políticas antigas de cores.
3. Ajustar o código correspondente e seus testes necessários. Regras mecânicas podem bloquear automaticamente; pertinência de imagem, fidelidade e cor exigem julgamento fundamentado. Não converter declarações como “imagem boa” em prova automática de qualidade.
4. Claude fará pesquisa delimitada sobre AnKing, autoria, oclusões e estatísticas de estudo com documentação oficial e exemplos reais. Aproveitar a pesquisa já existente em `ANALISTA-RETENCAO.md`. Produzir decisões aplicáveis ao projeto; não iniciar outro projeto de monitoramento ou alterar parâmetros de estudo sem justificativa e escopo.

### B. Calibrar com exemplos reais

5. Usar exemplos comentados de histologia, anatomia e fisiologia, incluindo aprovados e reprovados. Demonstrar frente, verso, imagem, Tab e cor antes/depois, com o motivo da mudança. Validar o padrão em outros cards da mesma família, sem exigir que Davi revise todos.
6. Codex confronta a proposta com o pedido e verifica a evidência; Claude corrige os problemas encontrados. Não repetir rodadas cegas sem um defeito concreto a resolver. A aprovação do plano autoriza seguir por aulas; não criar nova aprovação obrigatória para cada lote.

### C. Corrigir a coleção e reconstruir UC03

7. Prioridade de correção: histologia UC08 → anatomia UC08 → fisiologia UC08 → GR02 e PR02. Ler cada card médico e conferir seu alvo, frente/verso, cor, imagem quando houver, Tab e posição. Estender cada comentário à família: imagem compartilhada, irmãos, construção semelhante ou mesmo problema em outra aula, inclusive cópias AnKing.
8. Para cada comentário, registrar padrão, cards atingidos, correção e verificação. Preservar todo o texto; acrescentar `CORRIGIDO, DD/MM/AAAA.` apenas depois de conferir o resultado. Elogios também entram na calibração. O marcador anterior nunca dispensa a releitura.
9. Reconstruir as quatro aulas UC03 pelo Claude, com novo planejamento a partir das fontes. Fazer a substituição aula a aula, com backup e mapa antigo→novo. Remover a versão rejeitada ao instalar sua substituta, evitando duplicação e perda desnecessária de acesso durante a preparação. Preservar identidades/histórico quando o alvo continua o mesmo; novos alvos não herdam artificialmente revisão de outro conteúdo. Comentários e suspensões pessoais são reconciliados; cards compartilhados preservados em outras aulas não podem ser apagados em cascata.
10. Reconciliar specs/plans com o Anki corrigido. Os próximos builds não podem restaurar texto ou imagens rejeitados. Revisar deduplicação entre aulas sem perder ordem, cobertura e acesso ao card compartilhado.

### D. Entregar os ajustes de uso

11. **Tab:** longa narrativa (~20 linhas), situando a visão macro e a cadeia causal; curta (~5 linhas), fiel ao mesmo mecanismo. Exibir lado a lado quando houver espaço, com adaptação legível à tela pequena. Tamanhos são referências de leitura, não mínimos de palavras para preencher. Preservar a interação aprovada; versionar as duas variantes por card e invalidar as explicações quando o conteúdo mudar. Exigir cobertura atual em 100% dos cards do escopo.
12. **Heatmap:** implementar o verde por cumprimento da meta de novos, usando os **40 novos únicos/dia** já confirmados na memória, até eventual mudança explícita. Repetições/reaprendizagens do mesmo card não contam como novos. Usar a virada do dia do Anki, respeitar desfazer e conferir um dia abaixo, no limiar e acima da meta. Verde da meta não afirma que todas as revisões foram feitas. A distribuição proposta para incluir a retomada de conteúdos antigos está na Geração 2026; não elevar silenciosamente a meta total.
13. **Ordem:** conferir coluna e ordenação no Browser, acesso pelo painel e progressão dos novos por aula, inclusive compartilhados e pares comparativos próximos quando compatíveis com o percurso docente. A ordenação das revisões vencidas continua com o agendador; não mudar histórico para simular sequência de slides.
14. **Pós-prova:** nenhuma rotina automática de suspensão. Cores e organização ajudam Davi a fazer sua seleção manual; preservar suas suspensões. Não dessuspender em massa por regra antiga de proteção dos verdes.
15. Verificar renderização no desktop e em largura móvel; testar integração com AnkiDroid quando o aparelho estiver acessível. HTML responsivo sozinho não comprova funcionamento no aplicativo. Não declarar Tab sincronizado no tablet enquanto depender apenas de SQLite local; reutilizar o caminho de mídia documentado se sua implantação for necessária ao suporte escolhido, explicitando a validação disponível.

### E. Renomear slides e fechar a entrega

16. Inventariar os slides de aulas nas pastas médicas do Drive pessoal, incluindo UCs sem deck atual. Produzir mapa de nome atual→nome proposto no padrão existente `<Aula> - slides.<extensão>`. Preservar distinção necessária de parte, professor ou versão quando houver arquivos diferentes. Não converter formato apenas para trocar extensão.
17. Conferir conteúdo e cronograma quando pasta e arquivo discordam. Exemplos observados: FI05/FI06 têm títulos de pasta diferentes dos PDFs; Expressão gênica em procariotos e em eucariotos I ainda têm nomes técnicos/ilegíveis. Não resolver esses casos renomeando às cegas pelo nome da pasta.
18. Renomear sem substituir conteúdos, apagar variantes ou alterar organização/compartilhamento. Atualizar referências locais dependentes do caminho; conferir o nome no Drive depois. Exercícios e roteiros não viram “slides”.
19. Oferecer na raiz uma entrada clara para deck padrão e E1–E3 opcionais, reaproveitando os materiais existentes e sem gerar esses documentos nesta rodada. Publicar pacotes corrigidos conforme a política de entrega vigente, com idioma e conteúdo derivados explicitamente identificados; nunca chamar pacote inglês de tradução pronta. Verificar arquivos entregues e sincronização efetivamente realizada. Conferir versão/hash do artefato entregue e conteúdo/mídia do pacote contra a exportação da coleção corrigida: arquivo existente não comprova entrega atual. Não usar a cópia de slides feita por `entrega.py` como prova de que os originais foram renomeados.

## 5. Critérios de aceite e acompanhamento

Claude executa e mantém registro de progresso por aula/etapa; Codex coordena dependências, verifica o resultado e aponta o que falta. O registro desta rodada não substitui a memória única: as preferências ficam no MEMORY; falas no FEEDBACKS; evidências na corrida.

- Todos os 88 comentários médicos iniciais têm encaminhamento e verificação; incluir novos comentários surgidos durante a execução. Problemas de padrão têm alcance demonstrado além da nota comentada.
- As nove aulas UC08, GR02 e PR02 foram revisadas; as quatro aulas UC03 foram reconstruídas. Contagens finais saem da coleção, sem quotas artificiais.
- Cobertura confrontada com fontes completas, sem lacunas centrais encobertas por contagem de cards ou relatório autodeclarado.
- Imagens e oclusões pertinentes, legíveis e sem vazamento; exemplos aprovados preservados. A revisão visual considera o card como aparece, não apenas o arquivo-fonte.
- Cores justificadas, HY pertinente tratado como verde, recomendações e marcas pessoais reconciliadas; sem suspensão automática pós-prova.
- Tabs longo/curto completos e atuais; heatmap medindo novos únicos; ordem verificada no Browser/painel e nos novos.
- Pipeline e artefatos locais reproduzem o padrão corrigido; testes cobrem as regressões concretas de mídia, compartilhados, explicações, cores, ordem e contagem de novos.
- Renomeações conferidas, histórico/comentários preservados e nenhuma exclusão fora das quatro reconstruções autorizadas.
- Relatório curto por aula: notas/cards, origens, cores, estudados/novos/suspensos, compartilhados e pendências reais. Teste aprovado ou sync sem erro não será apresentado como validação de algo que não foi observado.

## 6. Etapa final — Geração 2026

### Objetivo e condição de início

Formar uma biblioteca de decks-aula de **UC01, UC02, UC03 inteira, UC19 e UC21**, cobrindo as aulas de 2026 disponíveis no Drive, para Davi revisar qualquer uma delas. Produção gradual ao longo de várias sessões, sem prazo artificial de um dia e sem sacrificar qualidade para completar a fila. Primeiro ajustar o pipeline e demonstrar o padrão em aulas reais; depois ampliar a produção. O volume de produção e a quantidade estudada por dia são decisões separadas.

A campanha começa quando as etapas anteriores estiverem verificadas, com fidelidade à aula/prova, fontes realmente usadas, imagens direcionadas, cores, Tabs e ordem funcionando. Uma lista de checks aprovada sozinha não prova essa qualidade. Claude executa as aulas; Codex acompanha a fila, verifica amostras e os riscos encontrados, e impede que defeitos recorrentes se propaguem.

### Inventário vivo e fila por aula

1. Cruzar cronogramas, organização das disciplinas e materiais do Drive para identificar cada aula/caso, ordem, prova e fontes disponíveis. UC03 inteira significa todas as suas aulas disponíveis, não só a P2/P3.
2. Classificar cada aula como: deck atual revisado; precisa reconstrução; pronta para produzir; aguardando material essencial; em produção; revisada/entregue. Reaproveitar GR02, PR02 e as quatro reconstruções quando já cumprirem o padrão, sem gerar cópias.
3. Ordem inicial de produção: UC01 → UC02 → restantes da UC03 → UC19 com o que houver → UC21, respeitando a sequência pedagógica interna. Prioridades de estudo e chegada de fontes podem antecipar uma aula pronta. A falta de material de uma aula não paralisa as independentes.
4. Não inventar aulas ausentes nem chamar a UC inteira de concluída quando faltam aulas/material. Conferir o Drive antes de iniciar cada aula e a cada retomada da campanha. Novo material vira revisão de impacto no planejamento e, se necessário, atualização do deck já entregue.
5. Para UC02, registrar as apostilas de lâminas anunciadas como material aguardado. Se forem essenciais à parte prática, preparar o restante e concluir essa parte quando estiverem disponíveis; não declarar cobertura prática completa sem elas ou outra fonte realmente equivalente.

### Produção e revisão de cada deck-aula

Cada aula repete integralmente o método validado: consultar fontes → reconstruir objetivos e percurso → inventariar alvos → buscar acervos → selecionar/redigir → classificar cores → revisar imagens/oclusões → gerar Tabs → instalar com ordem → conferir contra fontes e coleção → entregar. E1 existente é fonte auxiliar; nenhuma nova E1 será produzida.

O deck deve refletir o planejamento pedagógico: conceitos, pré-requisitos, relações, exemplos e prática na ordem em que se constroem. No Browser, Davi deve reconhecer a aula, como se o professor tivesse organizado as perguntas. A IA reconstrói a intenção apoiada no material disponível, sem inventar falas não registradas. Conteúdo recuperável dos slides precisa de cobertura efetiva; menção no verso não substitui uma pergunta quando a prova exige identificar ou recuperar esse conhecimento.

**UC02:** lâminas e reconhecimento visual são parte central da aprendizagem e da prova. As apostilas e provas orientam quais tecidos/estruturas distinguir e o nível de identificação. Revisar imagens e máscaras em todos os irmãos; não resolver a disciplina só com definições textuais.

**UC21/DIC:** caso guia cobertura; perguntas oficiais e HY guiam o verde. O deck pode ser amplo, respeitando o caráter integrador entre básico e clínico. Ensinar fundamentos, mecanismos e fisiopatologia introdutória antes de manejo especializado; o exemplo de manejo específico de ICC de VD não deve ocupar o lugar da base que permite compreender o caso. Bibliografia e apostilas aprofundam no nível apropriado, sem tornar a menção de uma doença licença para importar todo seu tratamento.

Entregar uma aula assim que estiver pronta e verificada. Registrar fontes, cobertura, cores, imagens, ordem, compartilhados e pendências. Retomadas consultam esse estado e a coleção viva para não duplicar trabalho nem desfazer intervenções pessoais. Feedback de uso ajusta os próximos decks e os anteriores atingidos pelo mesmo problema, dentro da campanha aprovada.

### Retomada do conteúdo antigo em paralelo ao atual

Davi propôs **10 cards/dia de UC01, UC02 e começo da UC03**. Para o plano, interpretar como **10 novos no total desse conjunto**, priorizando o núcleo verde e HY, enquanto continua avançando nas aulas atuais. Proposta inicial: reservar esses 10 dentro dos 40 novos globais já registrados, deixando aproximadamente 30 para o avanço; esta distribuição é proposta, não uma preferência já confirmada nem configuração aplicada. Se a intenção for 10 adicionais, o total e a meta do heatmap devem ser ajustados explicitamente.

Delimitar o começo da UC03 pelo cronograma e pelas aulas já cursadas; registrar os IDs da seleção, sem incluir a UC03 inteira por conveniência. A fila de retomada segue pré-requisitos e ordem das aulas; compartilhados contam uma vez. Revisões já agendadas seguem normalmente. Não resetar histórico para colocar um card antigo na quota de novos, nem dessuspender seleções pessoais em massa. A revisão de conteúdos antigos não obriga estudar todos os azuis/rosas produzidos.

### Conclusão da Geração 2026

A campanha estará concluída para a versão inventariada do Drive quando todas as aulas elegíveis tiverem deck-aula entregue e verificado. Enquanto houver aula aguardando fonte essencial, informar cobertura parcial e a pendência, sem afirmar conclusão integral; a produção das aulas independentes continua. Cada deck precisa cobrir fielmente o que a aula ensina e a prova pede, preservar atomicidade, profundidade apropriada, fontes verificadas, imagens adequadas, cores, Tabs e ordem. Materiais acrescentados depois entram na fila de atualização.

**Estado geral: proposta atualizada aguardando aprovação de Davi.** Inclui a campanha Geração 2026 como etapa final de longo prazo. Nenhuma geração, exclusão ou mudança de configuração foi iniciada nesta preparação.
