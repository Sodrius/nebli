# Execução de um deck-aula — runbook canônico

Revisado após as 30 respostas, 23/09/2026. Ler primeiro CALIBRACAO-ESCALA-V4.md, CONTRATO-DE-QUALIDADE.md e OPERACAO-CODEX-CLAUDE.md; prevalecem sobre a v3 e pilotos. Este é o procedimento operacional para Codex ou Claude executar o pedido “gere/rode o deck da aula X”. Preferências e limites vivem em [README.md](README.md); critérios vigentes vivem na v4. Publicação em [PUBLICACAO-POR-UC.md](PUBLICACAO-POR-UC.md); acervos em [ACERVOS-REFERENCIA.md](ACERVOS-REFERENCIA.md).

## Estado real do pipeline

O fluxo já foi executado com sucesso em dois pilotos, mas ainda não existe um comando genérico totalmente implementado. Os scripts dentro de `arquivos-trabalho/` são evidências e ferramentas específicas de cada aula, não uma CLI universal.

Hoje, “rodar o deck” significa o modelo executar este runbook de ponta a ponta, usando scripts locais auditáveis para inventário, planejamento, aplicação e verificação. Não afirmar que `nebli aula ...` funciona até essa interface existir e passar nos testes de `IMPLEMENTACAO.md`.

## Autoridade do pedido

- “Gere”, “rode”, “faça o deck” ou “vai até o fim” autoriza criar a cópia NEBLI, instalar no perfil Anki configurado, exportar o APKG e publicar na pasta privada correspondente, desde que as precondições abaixo passem.
- “Avalie”, “audite”, “o que falta?” ou “planeje” é somente leitura. Não escrever no Anki ou Drive.
- Nunca editar notas/modelos originais AnKing, AnkiHub ou de outros decks.
- Nunca presumir que a escrita no Windows já sincronizou o Mac/Android.

## Entrada mínima

Aceitar nome, link, pasta ou material de aula. Resolver, sem perguntar quando for seguro:

- UC, componente e título curto;
- pasta/material docente no Drive;
- perfil Anki acessível;
- destino privado de entrega, espelhando a organização já existente.

Perguntar somente quando a ambiguidade mudar materialmente o recorte ou o destino. Falta de prova antiga, livro integral ou vídeo não bloqueia o trabalho independente; registrar a limitação.

## Fluxo obrigatório

### 1. Abrir contexto e criar a corrida

1. Ler `flashcards/projeto/README.md`.
2. Ler `CALIBRACAO-ESCALA-V4.md`, `CONTRATO-DE-QUALIDADE.md`, `OPERACAO-CODEX-CLAUDE.md` e este arquivo inteiro.
3. Ler ACERVOS-REFERENCIA.md e PUBLICACAO-POR-UC.md. V3 é histórico opcional. Executar preflight vivo; não restaurar decks/cards apagados por Davi a partir de recibos antigos.
4. Ler o caso real mais parecido:
   - mecanismo/patologia: `APRENDIZADOS-INFLAMACAO-V2.md`;
   - anatomia/atlas: `APRENDIZADOS-VASCULARIZACAO-VISCERAS.md`.
5. Criar uma pasta única: `arquivos-trabalho/deck-aula-<slug>-<AAAA-MM-DD>/`.

6. Rodar diagnóstico somente leitura; verificar acesso ao Drive e publicação. Revisar pendências anteriores, vermelhos, laranjas e comentários; resolver conservadoramente o que estiver sustentado, registrar bloqueios e relatar brevemente. Se a nota foi apagada intencionalmente, encerrar a pendência como removida pelo usuário, não como corrigida nem recriar a nota. Não limpar sinalizações por mera leitura.

Não aplicar ao deck independente os gates antigos do pipeline completo de resumo (`FLASHCARDS.md`, loop obrigatório Card→E1, E2/E3, cota de 30–50 ou 25 novos/dia). E1 explicativa + guia curto acompanham sempre; E2/E3 estão suspensas. Rotina desejada: 35 novos/dia e cerca de 50 minutos incluindo revisões; estimar viabilidade, sem alterar configurações automaticamente.

### 2. Descobrir e registrar as fontes

Inventariar tudo que define a aula:

- slides e material obrigatório;
- roteiro prático e questões orientadoras;
- comentários/transcrição/anotações, se existirem;
- provas antigas realmente pertinentes;
- bibliografia e vídeo efetivamente disponíveis;
- E1 existente, quando houver.

Recuperar a intenção do Docs: progressão entre aulas e busca por recursos. Se pertinente, usar tags da videoaula Ninja Nerd e outros recursos como porta de busca, junto a texto/sistemas; tag não autoriza tudo que contém. Registrar o que foi coberto antes e o que pertence a aula futura, sem transformar cada aula num curso autossuficiente.

Guardar nome, link/caminho, tipo, tamanho/hash quando possível e papel da fonte. Não declarar que consultou livro, capítulo ou prova que não estava acessível.

Saída: `source-manifest.json` e, quando útil, material extraído/renderizado para inspeção visual.

### 3. Construir o mapa de escopo antes de buscar cards

Extrair primeiro os objetivos formais e depois classificar o restante como:

- `taught`: ensinado/exigido nesta aula;
- `assessed_recap`: retomado e cobrado de verdade;
- `bridge`: ponte curta ligada diretamente ao conceito da aula, sustentada por fonte consultada e útil à compreensão/Step pertinente, sem importar outro assunto;
- `illustration`: exemplo do professor;
- `prerequisite`: apenas pressuposto;
- `future`: pertence a aula posterior;
- `out_of_scope`: coincidência lateral.

Separar explicitamente conteúdo da aula de exemplo didático. Caso clínico não abre automaticamente um bloco de doença. Bibliografia não amplia automaticamente o capítulo da aula.

Para propor complemento, documentar alvo da aula, fonte, ganho de compreensão/recuperação e por que pertence a este recorte. Menção literal no slide não é condição universal; “cai no Step” não autoriza clínica lateral. Prova antiga sozinha não amplia o recorte sem confirmação no material atual ou por Davi. Auditar teoria e identificação prática separadamente.

Decompor objetivos só até o nível necessário para auditar cobertura. Não transformar cada legenda ou frase em obrigação de card.

Saída: `MAPA-ESCOPO.md` ou `scope.json`, contendo também exclusões deliberadas.

### 4. Verificar identidade antes da busca

Para cada alvo, procurar primeiro se já existe uma cópia NEBLI da mesma origem/pergunta:

- usar identidade de origem quando disponível (`corpus + source_nid/GUID`);
- preservar a nota já revisada e seu histórico;
- se o mesmo card pertence a duas aulas, associar a mesma identidade às duas — não criar uma segunda revisão;
- texto parecido não basta para fundir perguntas com direções diferentes.

Colisão ou múltiplas cópias são conflito a investigar, não licença para duplicar ou apagar.

### 5. Curar candidatos na ordem correta

Para cada objetivo do recorte, mesmo quando outro card já o cobre:

1. buscar AnKing por inglês/português, sinônimos, estrutura, mecanismo, contraste e tags de recursos/sistema;
2. ler frente, verso/Extra, imagens e cada cloze realmente gerado;
   inspecionar também campos `Clinical`/comentários herdados e o verso renderizado, pois clínica lateral pode aparecer em todo card visual de uma prancha;
3. explorar a vizinhança semântica dos bons resultados;
4. fazer uma segunda busca reformulada para lacunas;
5. buscar os acervos adequados descobertos no catálogo vivo: MCAT para lacunas básicas dentro do assunto; Dope/Dorian/BlueLink para anatomia; Histology/LLU para histologia. Não usar caminhos antigos fixos nem excluir modelos visuais da busca. Usar a rota do ACERVOS-REFERENCIA.md e registrar tentativas antes da autoria;
6. autorar somente para lacuna diretamente ensinada, relevante e ainda descoberta. **Antes, segunda busca AnKing obrigatória:** buscar cada substantivo do slide (molécula, enzima, meio, classe), também fora das tags da disciplina (ex.: lactoferrina/hepcidina em imuno/hemato, SOD/catalase em bioquímica), e recuperar cards recusados só por redundância com o verso. Autorais devem ser proporcionalmente poucos; relatar a % e justificar acima de ~15% (Davi, 23/09/2026: "autorais menos, normais mais").

Antes da prova, disponibilizar todos os AnKing adequados encontrados no assunto; registrar buscas amplas, sem importar tags inteiras. Admitir alguma repetição; inversos só com habilidade distinta. O verso evita autoria desnecessária, mas não elimina automaticamente outro bom AnKing pertinente. AnKing-first é ordem de busca, não cota percentual. Em anatomia visual, o atlas pode fornecer muitos cards. O verso conta como cobertura para aprender; isso não obriga criar outra frente.

Autoral deve parecer AnKing: uma recuperação por card, **pequeno** (frente de ~8–15 palavras, máx. ~18; Extra de 1–2 frases curtas; sem exemplo + contraste + parêntese na mesma frente), inglês na frente/resposta, mesmo modelo/CSS, sem dissertação, sem rodapé meta. **Autoral leva imagem por padrão** (pedido de Davi, 23/09/2026): primeiro procurar a imagem em outro card AnKing que ilustre o alvo; depois a figura do slide (recortada, legível); por último internet com licença livre e crédito. Só dispensar quando nenhuma imagem ensina algo. Conferir visualmente cada imagem no verso.

Registrar candidatos avaliados, decisão e motivo em `candidate-decisions.jsonl` ou no `plan.json`.

### 6. Auditar cobertura antes de contar cards

Montar uma matriz objetivo → cards/versos/imagens. Para cada objetivo formal, responder:

- há recuperação ativa suficiente?
- o verso cobre informação acessória sem exigir uma nova frente?
- há identificação visual quando a aula exige reconhecer estruturas?
- algum exemplo foi confundido com conteúdo?
- existe redundância sem ganho de direção, contraste ou imagem?
- a redundância é consolidação pré-prova ou erro/expansão lateral? Bons repetitivos são candidatos à manutenção menor depois, não exclusão automática agora;
- alguma clínica, exame, doença ou tratamento desconexo aparece na frente ou no verso renderizado, mesmo se veio de um campo de origem?

Fazer uma passada final pelos materiais, procurando lacunas reais. Quantidade de cards não é métrica de cobertura. Encerrar quando cada alvo está coberto de forma suficiente, precisa e proporcional.

### 7. Preparar plano imutável e dry-run

O `plan.json` deve registrar pelo menos:

- `lesson_id` estável e deck-alvo;
- fontes e hashes/readback;
- origem de cada nota/card;
- objetivo associado;
- campos que serão copiados;
- clozes/templates selecionados e contagem esperada real;
- campos/rótulos visuais desativados;
- autoria e justificativa;
- HY literal de origem;
- total esperado por origem.

Antes de escrever:

- confirmar perfil e pasta de mídia;
- confirmar que as fontes não mudaram;
- testar templates condicionais com os campos selecionados;
- detectar cópias anteriores;
- registrar estado anterior e criar backup quando houver deck/cópias a substituir.

O dry-run não escreve no Anki nem no Drive.

### 8. Aplicar com cópias independentes

- Criar/reutilizar modelos NEBLI independentes equivalentes à origem.
- Copiar campos e mídia necessários; remover vínculo ativo do clone com AnkiHub (`ankihub_id` vazio).
- Não inserir comentários “Faculdade”, “núcleo”, “prova”, “reserva”, “HY/LY” ou justificativas no verso.
- Preservar notas, modelos, flags, suspensões e agendamento dos originais.
- Em modelo visual, esvaziar campos fora do recorte e conferir quantos cards o template realmente criou.
- Em cada cópia NEBLI, limpar ou encurtar `Extra`, `Clinical` e comentários herdados que distraiam do alvo desta aula; nunca fazer essa limpeza no modelo ou nota de origem.
- Verde (`flag 3`) somente para card cuja origem AnKing possua literalmente `#AK_Step1_v12::#Low/HighYield::1-HighYield`.
- Vermelho (`flag 1`) é feedback de Davi; não aplicar preventivamente.
- Laranja (`2`) é comentário pendente: resolver/conferir antes de limpar. Rosa (`5`) é bom card candidato a suspensão pós-prova, já sinalizado na criação e mantido ativo. Na cópia nova, candidatura fundamentada recebe rosa mesmo se houver tag HY (tag permanece); preservar marcas pessoais existentes e não encobrir vermelho/laranja. Colisões seguem v4.
- Não suspender por padrão. Card ruim, cópia acidental ou lateral é corrigido/excluído após backup. Bom AnKing repetitivo pertinente fica disponível; manter é padrão e Davi decide pessoalmente quais rosas suspender após cada prova.

Toda escrita deve ter lock, journal, identidade idempotente e readback. Depois de timeout, procurar a identidade antes de repetir.

### 9. Verificar o deck vivo e o pacote

Bloquear a entrega se falhar qualquer item:

- contagem de notas/cards igual ao plano;
- cards novos no destino previsto; compartilhados conservam identidade/histórico e associação por card, sem movimentação silenciosa para simular duas aulas;
- nenhuma suspensão ou bandeira vermelha inesperada; outras bandeiras pessoais, se existentes, permanecem intocadas e são apenas contabilizadas;
- verdes conforme HY literal planejado, descontando conflitos com marcas pessoais documentados;
- clozes renderizados e respostas não vazias;
- nenhum rodapé meta visível;
- imagens pertinentes, legíveis e presentes no perfil;
- fontes e modelos originais inalterados;
- APKG abre como ZIP/coleção e contém as mesmas notas/cards e mídias exigidas;
- backup e recibo existem.

Inspecionar visualmente as pranchas principais. Regex e contagem não substituem ver a imagem.

Saídas: `before.json`, `journal.jsonl`, `receipt.json`, `verification.json`. APKG por aula pode ser backup local; a entrega publicada é somente o pacote da UC inteira, conforme passo 10.

### 10. Entregar E1/guia e publicar

Gerar `E1-GUIA.md` com:

- sequência curta para aprender a aula;
- materiais realmente disponíveis;
- vídeos dos canais preferidos (README), com canal/título conferidos e trecho/timestamp quando houver capítulos. **Os vídeos são entregues na resposta do chat (e podem constar no guia); nunca no `Additional Resources` nem em qualquer campo de card** (Davi, 23/09/2026);
- bibliografia somente quando verificada;
- pré-requisitos e lacunas honestos;
- casos usados apenas como aplicação, quando pertinente.

Além do guia, gerar E1 explicativa do recorte ou reutilizar E1 boa efetivamente conferida. Guia curto não a substitui. Não explicar cada Extra lateral. E2/E3 não são geradas.

Publicar E1 e guia na pasta privada da aula. Reexportar **a UC inteira viva**, gerar `NEBLI-UCxx.apkg` comprimido e sem flags no arquivo com `python -m nebli.package_uc`; seguir PUBLICACAO-POR-UC.md. Nunca limpar flags na coleção. Conferir cards compartilhados/associações; não declarar conjunto físico completo se faltarem compartilhados de outra UC. Atualizar o mesmo file_id do APKG na pasta privada da UC, registrado em `config/publicacoes-uc.json`. Não publicar pacotes por aula por padrão nem repor removidos de arquivos antigos. Readback de nome, bytes, destino/link/permissões e recibo. Salvar revisão de qualidade antes de declarar pronto.

### 11. Registrar aprendizado e responder

Criar ou atualizar `flashcards/projeto/APRENDIZADOS-<AULA>.md` com:

- resultado e contabilidade;
- fontes acessadas e ausentes;
- recorte e exclusões;
- autoria e motivo;
- falhas/reprises técnicas;
- regras que devem se repetir, sem transformar peculiaridade de uma aula em lei global;
- links e limitações.

Resposta final traz a **lista de vídeos por objetivo (com timestamps)** no próprio chat e deve distinguir: instalado no Anki, exportado, publicado e sincronizado. Informar bibliografia usada/ausente, pendências resolvidas/restantes, notas/cards únicos por origem, compartilhados, autorais, verdes, vermelhos, laranjas, rosas e suspensos. Timestamps só quando verificados. Informar total da aula e total único da UC, candidatos rosas na coleção e zero flags no arquivo. Não confundir sugestão rosa com suspensão aplicada.

## Regra de parada

Não fechar porque “já há muitos cards”. Fechar quando os objetivos formais e o conteúdo realmente ensinado estiverem cobertos com perguntas suficientes, sem expansão lateral. Também não perseguir 100% de cada legenda quando o verso, o guia ou uma relação já cobre o aprendizado de forma adequada.

## Evidências aprovadas

- Patologia/mecanismo: [APRENDIZADOS-INFLAMACAO-V2.md](APRENDIZADOS-INFLAMACAO-V2.md).
- Anatomia/atlas: [APRENDIZADOS-VASCULARIZACAO-VISCERAS.md](APRENDIZADOS-VASCULARIZACAO-VISCERAS.md).
- Histologia/biologia tecidual, ainda aguardando feedback: [APRENDIZADOS-INTESTINOS.md](APRENDIZADOS-INTESTINOS.md).

Esses casos ensinam decisões e salvaguardas; seus números não são cotas para a próxima aula.
