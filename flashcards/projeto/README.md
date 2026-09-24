# NEBLI Decks — contexto canônico e decisões

> **Decisão de Davi, 23/09/2026 (noite):** **não fazer upload de APKG para o Drive**, nem por aula nem por UC. O APKG pode continuar sendo gerado localmente como backup técnico. E1 e guia continuam publicados na pasta privada da aula. Esta nota prevalece sobre as menções a upload de APKG abaixo e em PUBLICACAO-POR-UC.md.

Versão 4 revisada após o reinício, 23/09/2026. Entrada para Codex e Claude. **Última decisão: um APKG comprimido por UC inteira, sem flags no arquivo; rosa no Anki para candidatos pós-prova, manter como padrão. Não restaurar decks apagados.** **Leia [CALIBRACAO-ESCALA-V4.md](CALIBRACAO-ESCALA-V4.md): contém as 30 respostas recebidas e prevalece sobre regras anteriores.** Critério de entrega: [CONTRATO-DE-QUALIDADE.md](CONTRATO-DE-QUALIDADE.md).

## O que Davi quer

Pedir “gere o deck da aula X” passando o slide/pasta no Drive e receber E1 explicativa, guia com vídeos/bibliografia, seleção ampla de AnKing dentro do assunto, instalação no Anki e APKG no Drive privado. Cobrir a aula, o Step 1 pertinente e a compreensão médica durável. O estudante não deve precisar organizar arquivos, procurar repetidamente cards faltantes ou explicar suas preferências em cada conversa.

O formato AnKing-first foi aprovado. **Vascularização das vísceras é o exemplar aprovado mais forte até agora**; Inflamação aguda consolidou as regras de recalibração e exclusão de excesso. O problema permanente é calibrar cobertura: não deixar faltar conteúdo efetivamente dado, mas não corrigir isso incluindo tudo que poderia explicar o assunto. Melhorar a seleção, não reinventar o formato nem abandonar AnKing.

“Completo” significa completo para o recorte da aula. Um deck-aula não é um curso autossuficiente nem o capítulo inteiro do livro. As aulas se complementam ao longo do currículo.

## Ordem de leitura

Para **gerar um deck de aula**:

1. Este arquivo: preferências e limites atuais.
2. [CALIBRACAO-ESCALA-V4.md](CALIBRACAO-ESCALA-V4.md): decisões atuais das 30 respostas; depois [CONTRATO-DE-QUALIDADE.md](CONTRATO-DE-QUALIDADE.md).
3. [OPERACAO-CODEX-CLAUDE.md](OPERACAO-CODEX-CLAUDE.md): diagnóstico, acervos e publicação; depois [EXECUCAO-DECK-AULA.md](EXECUCAO-DECK-AULA.md), runbook do Drive à entrega.
4. A v3 é histórico de decisões; consultar somente para investigar um piloto, sempre subordinada à v4. Não é necessário relê-la em cada aula.
5. O caso real mais parecido: [APRENDIZADOS-INFLAMACAO-V2.md](APRENDIZADOS-INFLAMACAO-V2.md), [APRENDIZADOS-VASCULARIZACAO-VISCERAS.md](APRENDIZADOS-VASCULARIZACAO-VISCERAS.md) ou [APRENDIZADOS-INTESTINOS.md](APRENDIZADOS-INTESTINOS.md).

Somente para **construir o software/comando genérico**, ler também [ARQUITETURA.md](ARQUITETURA.md) e [IMPLEMENTACAO.md](IMPLEMENTACAO.md). Eles descrevem o alvo futuro e o roadmap; não são necessários para cada curadoria.

Arquivos específicos de Inflamação (`CALIBRACAO-INFLAMACAO.md` e `CONTABILIDADE-INFLAMACAO-V2.md`) são evidência histórica do piloto, não regras gerais.

## Mapa dos arquivos

| Arquivo | Papel | Quando o Claude deve ler |
|---|---|---|
| `README.md` | Entrada, contexto e estado real | Sempre em tarefas de deck-aula |
| `CALIBRACAO-ESCALA-V4.md` | Decisões atuais das 30 respostas | Sempre, prevalece sobre v3 |
| `CONTRATO-DE-QUALIDADE.md` | Evidências para declarar uma entrega pronta | Sempre antes de fechar |
| `OPERACAO-CODEX-CLAUDE.md` | Preflight, acervos e acesso ao Drive | Início da execução |
| `ACERVOS-REFERENCIA.md` | Mapa vivo de modelos e rotas, incluindo MCAT | Antes das buscas |
| `PUBLICACAO-POR-UC.md` | Comando de exportação/compressão sem flags e atualização por UC | Antes de publicar |
| `EXECUCAO-DECK-AULA.md` | Como executar uma aula hoje, passo a passo | Sempre que gerar, revisar ou auditar um deck |
| `CALIBRACAO-DECK-AULA-V3.md` | Histórico de calibração, parcialmente superado pela v4 | Investigação dos pilotos, não leitura obrigatória de cada aula |
| `APRENDIZADOS-INFLAMACAO-V2.md` | Caso real mecanístico/patológico | Quando a nova aula for semelhante |
| `APRENDIZADOS-VASCULARIZACAO-VISCERAS.md` | Caso real anatômico e visual | Anatomia, histologia e aulas com atlas/IO |
| `APRENDIZADOS-INTESTINOS.md` | Caso real de histologia com mecanismos e lâminas; ainda aguardando feedback | Histologia/biologia tecidual, sem copiar seus números como meta |
| `ARQUITETURA.md` | Produto final desejado e contratos de dados | Somente para evoluir o sistema |
| `IMPLEMENTACAO.md` | Roadmap e testes do comando genérico | Somente para programar a automação |
| `CALIBRACAO-INFLAMACAO.md` / `CONTABILIDADE-INFLAMACAO-V2.md` | Histórico detalhado do primeiro piloto | Auditoria ou investigação específica |

Os artefatos de cada corrida ficam em uma única pasta de `arquivos-trabalho/`; não são nova fonte de regras. Ao concluir uma aula, somente seus aprendizados generalizáveis sobem para este diretório.

As instruções explícitas mais recentes do usuário prevalecem. Este conjunto substitui a v1 em `arquivos-trabalho/arquitetura-nebli/` para decisões de deck-aula; a v1 permanece como histórico e inventário. Regras de escrita de resumos não devem ser automaticamente aplicadas aos cards. A auditoria anterior diagnosticou lacunas; não é autorização para expandir o recorte de cada aula.

## Preferências confirmadas

| Tema | Decisão vigente |
|---|---|
| Objetivo | Aprender e lembrar o conteúdo da faculdade, construindo progressivamente base para Step 1 e depois Step 2. Não prometer domínio ou aprovação só com cards. |
| Horizonte | Primeiro ano, segundo semestre; pensa no Step 1 ao final do quarto ano. Não presumir data de prova marcada. |
| Fontes | Material docente, comentários/transcrição, anotações, roteiros práticos, PBL/casos, vídeos indicados, provas antigas pertinentes e bibliografia. Slide tradicional não é a única entrada. |
| Escopo | Assunto da aula, aprofundado por bibliografia/vídeos/E1/provas e AnKing pertinente; não limitado à literalidade do slide nem expandido para outras aulas. |
| AnKing | Prioridade de curadoria. Buscar bem por texto, sinônimos, sistemas e múltiplas tags de recursos. Preferência não equivale a copiar tudo da tag. |
| Outros decks | Complementam lacunas reais, principalmente anatomia, cadáver e histologia/IO; só contar corpus realmente acessível. |
| Autoral | Última alternativa para lacuna relevante comprovada após buscas distintas. Não meta de produção. |
| Acervo já revisado | Preservar identidade, histórico e edições. Não recriar uma cópia existente só porque apareceu numa nova aula. |
| Idioma | Frente/resposta em inglês; ajuda/explicação em português quando útil. As antigas ideias de tradução integral não são a escolha atual. |
| Clozes | Não impor um único cloze; não juntar automaticamente todos os irmãos. Julgar pergunta, redundância e carga por card real. |
| Quantidade | Sem teto obrigatório ou cota de origem. O deck deve cobrir a aula, não conter cada detalhe ou exemplo do professor. Não criar frente se o verso já ensina suficientemente. |
| Seleção e manutenção | Antes da prova: todos os AnKing adequados ao assunto, admitindo alguma repetição. Depois: proposta confirmável de suspensão de bons cards menos úteis à manutenção. Perguntas inversas precisam de ganho específico (Q8). Sem corte silencioso para caber numa cota. |
| Bandeira | Vermelho = melhorar; laranja = pedido pendente; verde = HY literal; rosa = bom card candidato à suspensão pós-prova, sinalizado desde a criação. Manter ativo é o padrão. Colisões seguem v4. APKG publicado sem bandeiras, coleção preservada. |
| Integração clínica | Pouca clínica, diretamente ligada ao conceito da aula, Step pertinente ou compreensão; evidência e justificativa obrigatórias. Não importar diagnóstico/tratamento de outro assunto por vir no AnKing. |
| Clínica em frente e verso | Não importar clínica desconexa por vir no AnKing, em atlas, Extra ou campo `Clinical`. Mesmo quando uma doença é mencionada, não criar card clínico se ela não esclarecer o mecanismo central ensinado. No verso, manter apenas a frase necessária para essa relação; limpar campos herdados laterais nas cópias NEBLI, preservando as origens. |
| Aprendizagem | Principalmente videoaula + bibliografia/cursinho; E1 como consulta. Preferir poucos vídeos bons e trechos, indicando lacunas. |
| Vídeos no chat, não nos cards (23/09/2026, substitui a regra da manhã) | Vídeos dos canais preferidos vão **na resposta do chat** ao entregar o deck (e podem constar no E1/guia), por objetivo e com timestamp quando houver capítulos. **Nunca** colocar link de vídeo em `Additional Resources` nem em outro campo de card. Conferir canal/título (oEmbed); nunca canal fora da lista; declarar lacuna. |
| Proporção e tamanho dos autorais (23/09/2026) | Autorais **menos**, AnKing/outros decks **mais**, proporcionalmente. Antes de autorar, refazer a busca AnKing por sinônimos/bioquímica/fisiologia correlata e recuperar recusados "por redundância com o verso" (V4: seleção ampla até a prova). Autoral **pequeno**: frente de ~8–15 palavras (máx. ~18), um único alvo, sem exemplo+contraste+parêntese na mesma frente; Extra de 1–2 frases curtas. Se o alvo pede frase longa, dividir em cards menores ou deixar o detalhe no verso. Relatar a proporção autoral e justificar se passar de ~15%. |
| Imagem em autorais (23/09/2026) | Autoral sem imagem é erro comum. Todo autoral recebe imagem quando ela ensina ou ancora o alvo: preferir imagem de outro card AnKing; depois figura do slide; depois internet com licença livre e crédito. Inspecionar visualmente. |
| E1/E2/E3 | E1 explicativa do recorte + guia curto sempre; reutilizar boa E1 existente. Guia sozinho não substitui E1. E2/E3 suspensas; sem explicar todo Extra lateral. |
| Anki | Uma cópia NEBLI independente por origem; AnKing/AnkiHub originais preservados. Mesma pergunta pode ter associações a duas aulas sem dois históricos. |
| Rotina | Deseja cerca de 50 minutos/dia e 35 novos/dia. Estimar se cabem juntos com revisões e carga por prova; não garantir sustentabilidade nem alterar agendador sem pedido. Cram extra separado. |
| Calendário | Planilha, aba Mês, prevalece nas datas. Matérias ajuda a identificar aulas. Reconciliar quando executar comando; sem serviço em segundo plano no MVP. |
| Liberação | Data da aula, com correção manual. Elegibilidade não prova estudo nem domínio. |
| Pós-prova | Padrão é manter. Bons candidatos à suspensão já vêm rosas; Davi decide a cada prova se suspende ou não. Sem suspensão automática por calendário, cor ou ausência de HY. |
| Suspensão vs. exclusão | Suspender somente card bom, mas não prioritário agora. Card ruim, excessivo, duplicado ou fora do recorte deve ser excluído do deck-aula, com backup e originais preservados. |
| Avaliação | Qualidade dos cards e desempenho nas provas reais. Não impor quizzes novos nem reativar E2/E3 para validar o sistema. |
| Dispositivos | Mac principal declarado; Android tablet/celular; Windows atual com Anki acessível. Sincronização e perfil de escrita precisam ser confirmados, nunca presumidos. |
| Custo | Usar assinaturas de Codex/Claude, sem exigir API adicional paga. Davi pretende usar mais o Claude neste fluxo. |
| Ordem de expansão | Aulas atuais primeiro; recuperar antigas gradualmente. Tutor interativo e compartilhamento ficam para depois. |
| Saída | E1/guia por aula; **um APKG da UC inteira**, comprimido internamente e sem flags, atualizado pelo mesmo file_id a cada aula. Não publicar pacote por aula por padrão. Pasta pessoal privada, metadados conferidos. |
| Executor preferido | Davi usará mais o Claude para estas operações. Especificações e manifests devem ser portáveis, sem depender de memória ou automação exclusiva do Codex. |

Bibliografia varia por matéria e deve ser localizada/perguntada em cada aula; não presumir Robbins globalmente. Para Inflamação aguda foi informado **Robbins & Cotran**. Edição e capítulo fornecido ainda pendentes. Figuras do livro nos slides não equivalem a capítulo integral consultado.

Canais preferidos declarados: Ninja Nerd; Medicosis Perfectionalis e Patologia Fácil; Dirty Medicine; Armando Hasudungan, Osmosis e Professor Dave; Shomu's Biology. Preferir um recurso pertinente e acessível, sem depender de uma única tag/canal nem alegar cobertura sem verificar.

## Refinamentos que governam esta versão

- AnKing primeiro para NOVAS perguntas; primeiro verificar identidade para não duplicar o que já existe. Essa verificação não é preferência automática por um card autoral antigo pior.
- Pergunta antiga revisada não é substituída silenciosamente por AnKing equivalente. Equivalência, qualidade e custo de trocar histórico devem ser considerados separadamente.
- Conteúdo já coberto em outra aula e apenas pressuposto fica em “revisar antes”, fora da seleção principal. Se for efetivamente ensinado/cobrado nas duas aulas, associar o mesmo card às duas.
- A prova antiga calibra profundidade e prioridade dentro do tema pertinente; não importa a prova inteira para uma aula.
- Ausência em provas antigas não prova baixa importância. Ausência de tag HY não significa LY.
- Livro/vídeo podem esclarecer e localizar candidatos; não acrescentam obrigações novas por conterem mais medicina.
- Cobertura deve ser medida sobre o que foi decidido como escopo, e esse escopo também precisa ser auditado. Nem toda frase vira card; toda exclusão relevante precisa ser justificável.
- Conteúdo correto, pertinente e realmente explicativo no verso conta como cobertura **para aprender**. Recuperação ativa é uma decisão separada: só criar/manter uma frente própria quando o ganho de lembrar ativamente justificar a carga.
- Conhecimento mecanístico pode ser perguntado de forma curta; não obrigar fluxogramas, dissertações ou prosa NEBLI em todo card.
- Antes da curadoria, separar **conteúdo ensinado** de **exemplo didático**. Exemplo não vira card só por ter aparecido; entra apenas se foi cobrado ou se é indispensável para o alvo ensinado.
- Autoria só é aceita depois de AnKing e outros decks acessíveis terem sido pesquisados; deve reproduzir o padrão AnKing, sem rodapé meta, pergunta abrangente ou excesso de explicação.
- A checagem de escopo vale para a pergunta **e para tudo que aparece no verso**. Um card de identificação anatômica não deve exibir um parágrafo clínico herdado sem função para a aula; uma doença citada em exemplo não gera automaticamente perguntas de diagnóstico, exame ou tratamento.
- Cobertura não se mede por número de cards. Auditar também o excesso: duas frentes que testam a mesma relação, clozes irmãos triviais e exemplos transformados em fatos isolados precisam de justificativa específica para coexistir.

## Bandeiras e decisões de estudo

Vermelho significa “revisar/remover/melhorar”, inclusive acrescentar imagem quando ela é necessária. Verde significa somente `1-HighYield` explícito do AnKing; HY relativo, temporário ou inferido não recebe cor. **A v4 acrescentou laranja e rosa.** Laranja acompanha comentário pendente e é removido após resolução conferida; rosa indica qualquer bom candidato a suspensão pós-prova, inclusive variante visual. Sinalizar já na criação e manter ativo por padrão. Outras marcas pessoais são preservadas. Não imprimir rótulos de curadoria no card. Davi decide a cada prova se mantém ou suspende; a marca rosa é sugestão, nunca agendamento automático. Uma bandeira pessoal nunca é sobrescrita silenciosamente.

## Decisões fechadas — não perguntar novamente

Estas são defaults permanentes para uma conversa nova. Só perguntar se faltar um dado específico da aula ou se Davi mudar expressamente uma decisão:

- O comando recebe nome, link ou pasta da aula e, quando o pedido for “gere/rode/vai até o fim”, deve prosseguir até Anki, APKG, E1, verificação e Drive privado (E1, guia e APKG; upload reativado).
- Material da aula define **o que** entra; provas antigas pertinentes calibram profundidade/cobrança; bibliografia e vídeos esclarecem o mesmo recorte. Não transformar livro, vídeo, caso clínico ou exemplo do professor em currículo adicional.
- Deck-aula cobre a aula, não precisa explicar todo o assunto nem repetir pré-requisitos que pertencem a outras aulas. Aula futura fica para a aula futura.
- Conteúdo correto no verso conta como cobertura de aprendizagem. Criar outra frente apenas quando recuperar aquilo ativamente justificar a carga.
- Buscar novas perguntas na ordem: AnKing → outros decks acessíveis e adequados (anatomia, histologia, IO etc.) → autoral como último caso após lacuna comprovada.
- Card autoral deve parecer AnKing: curto, focal, em inglês, mesmo modelo/CSS, sem pergunta ampla, prosa excessiva ou comentário meta. Imagem é o padrão no autoral (AnKing > slide > internet livre), salvo quando não ensina nada.
- Não há teto fixo: se 120 cards bons forem realmente necessários ao recorte, podem ficar disponíveis. Isso não autoriza volume lateral nem cria automaticamente núcleo/prova/reserva.
- Verde é somente HY literal do AnKing; vermelho é feedback para melhorar. Ausência de verde não significa low yield nem pouca importância para a faculdade.
- Card ruim, duplicado ou fora do escopo é corrigido ou excluído da cópia NEBLI após backup; não vira “reserva” suspensa. Suspender apenas card bom que Davi decide não estudar agora.
- E1 explicativa sempre acompanha o deck, além do guia curto. E2/E3 permanecem suspensas. Aprendizagem principal: videoaula + bibliografia/material de cursinho, com E1 quando útil; preferir poucos vídeos bons/trechos e declarar lacunas.
- Uma ponte curta entra quando explica diretamente um conceito do assunto da aula com evidência; a v4 permite usar bibliografia/vídeos/AnKing além do slide literal. Menção isolada da doença ou tag Step não bastam; diagnóstico, exames, tratamento e blocos futuros não entram por arrasto. Um card importante do recorte pode ficar disponível mesmo se exigir pré-requisito ainda não estudado, indicando onde aprender e deixando a decisão com Davi.
- Uma pergunta usada em várias aulas conserva uma única identidade e um único histórico, com múltiplas associações. As cópias NEBLI são independentes; originais AnKing/AnkiHub ficam preservados como referência.
- Referência de rotina: cerca de 50 minutos por dia para novos + revisões e desejo de 35 novos/dia, cuja viabilidade precisa ser estimada; cram temático fica fora dessa conta. Aumento perto da prova é decidido caso a caso, não pelo pipeline.
- A aba **Mês** da planilha prevalece para datas. O comando reconcilia pendências de calendário, mas não presume que uma data prova estudo/domínio nem toma sozinho decisões pós-prova.
- Avaliar pelo padrão dos cards e pelo desempenho nas provas reais; não impor quiz extra. Uso é pessoal/privado por enquanto; compartilhamento fica para etapa posterior.
- Dispositivos: Mac principal e Android (tablet/celular), com Windows também usado. Nunca afirmar sincronização entre eles sem teste/readback.
- Objetivo longitudinal: aprender bem a faculdade e construir progressivamente base para Step 1, pensado para o fim do quarto ano, sem deixar Step expandir o recorte de cada aula.

## Estado após a limpeza intencional — prevalece sobre o histórico abaixo

Leitura viva em 23/09: **89 cards médicos / 74 notas**, somente Genética bacteriana (44) e Fisiologia bacteriana (45), 15 verdes, zero demais cores/suspensos. Perfil Davi. AnKing Step 35.067; seis acervos externos somam 18.959, incluindo MCAT 6.320. A raiz externa agora é `Referências::Referências Externas`; descoberta dinâmica em `nebli.preflight`.

Não restaurar Inflamação, Vascularização, Intestinos ou Complemento nem comentários de cards apagados usando backups. Seus exemplos documentais continuam úteis, mas recibos antigos não provam existência atual. Os 89 remanescentes não foram apagados, reclassificados nem aprovados nesta vistoria.

Exportação/compressão sem flags por UC testada localmente; não publicada nesta rodada. Detalhes em PUBLICACAO-POR-UC.md. Próxima aula será indicada por Davi ao Claude; não escolher automaticamente.

## Histórico de entregas e plano — não representa a coleção atual

O piloto inicial tinha 31 notas/45 cards. A expansão intermediária autorizada em 22/09/2026 chegou a 80 notas/116 cards; a recalibração posterior excluiu o excesso e fechou Inflamação aguda em 46 notas/68 cards ativos. Estado e evidências estão em `APRENDIZADOS-INFLAMACAO-V2.md` e nos recibos de `arquivos-trabalho/auditoria-inflamacao-aguda-2026-09-22/`. Parte do acervo antigo citado na primeira auditoria já não estava na coleção e não foi restaurada. Ainda não há pipeline genérico completo, calendário integrado ou validação Mac/Android.

Regra vigente: [CALIBRACAO-ESCALA-V4.md](CALIBRACAO-ESCALA-V4.md), que atualiza a v3. A contabilidade antiga de “80 núcleo” está superada; Inflamação tem 68 ativos, sem suspensos. As 48 cópias fora do recorte foram excluídas após backup.

A arquitetura e o plano continuam especificações; as revisões pontuais implementadas não tornam os comandos propostos funcionalidades prontas nem significam que calendário/sincronização já estejam automatizados.

O slash command `/deck-aula` é um orquestrador documental: obriga o Claude a seguir o runbook atual, mas não substitui o julgamento nem constitui a futura CLI `nebli aula`. O alias `/flashcards` aponta para a mesma rota e não gera mais RemNote.

Em 22/09/2026 foi concluído o segundo deck-aula de calibração: **UC08 — Anatomia — Vascularização das vísceras**, aprovado explicitamente por Davi em 23/09/2026 (“gostei muito de como ficou”). Estado: 47 notas/88 cards ativos; 43 AnKing, 42 Dope Anatomy, 2 Dorian e 1 autoral; 37 verdes por HY explícito do AnKing; zero vermelhos e zero suspensos. O único autoral é curto e cobre a origem da artéria retal média, alvo explícito do slide não encontrado após buscas nos decks acessíveis. O deck foi instalado no Anki deste Windows e exportado para pasta privada no Drive. Materiais, recorte, correção do template anatômico e limitações estão em [APRENDIZADOS-VASCULARIZACAO-VISCERAS.md](APRENDIZADOS-VASCULARIZACAO-VISCERAS.md).

Em 23/09/2026, por pedido explícito de Davi, foi executada **UC08 — Biologia Tecidual II — Intestinos**. O deck no perfil Windows contém 37 notas/41 cards ativos: 20 AnKing, 4 LLU Histology visuais e 17 autorais curtos para alvos explícitos sem pergunta adequada nos acervos buscados; 6 verdes por HY explícito, nenhum vermelho ou suspenso. APKG, E1, guia, escopo e recibo estão em `arquivos-trabalho/intestinos-2026-09-23/` e na [pasta privada da aula](https://drive.google.com/drive/folders/1Zhfy9tcwzrqCMGcRaHSXFH8gDGGR9FS5). O APKG e sua mídia passaram em verificação local. **Este deck ainda aguarda feedback de Davi e não é exemplar aprovado.** A sincronização no Mac/Android e o pacote agregado da UC não foram validados; o comando único continua não implementado.

Em 23/09/2026 foi executada **UC03 — Imunologia — Sistema complemento**: 43 notas/56 cards (35 AnKing, 21 autorais), 4 verdes, nenhum vermelho ou suspenso, além de 2 cópias da Inflamação aguda associadas por tag. E1/guia e mapa estão na pasta privada. **APKG publicado após a calibração**, com readback em `publication.json` da execução; o canal atual aceitou os 26 MB. Aguarda revisão de conteúdo v4/feedback. Detalhes em [APRENDIZADOS-SISTEMA-COMPLEMENTO.md](APRENDIZADOS-SISTEMA-COMPLEMENTO.md).

**Feedback transversal de 23/09/2026:** Davi percebe excesso de clínica desconexa e possível carga maior que o ganho de aprendizagem em **todos** os decks médicos, incluindo UC03 e UC08. A [auditoria transversal](../../arquivos-trabalho/auditoria-global-cards-2026-09-23/RELATORIO.md) inventariou os 253 cards vivos dos quatro decks e identificou exemplos concretos, inclusive `Clinical` herdado no verso de 37 cards visuais de Vascularização. A aprovação anterior do formato de Vascularização permanece histórica, mas não dispensa essa nova revisão de carga e clínica. Os decks publicados não foram alterados por essa auditoria.

Em 23/09/2026 foi executada **UC03 — Microbiologia — Genética bacteriana**, com foco pedido em qualidade: 36 notas/44 cards (34 AnKing, 10 autorais), 7 verdes, nenhum vermelho ou suspenso, versos limpos de clínica/recurso lateral e duas imagens erradas corrigidas após inspeção visual. Autorais com imagem e vídeos dos canais preferidos em cada card (vídeos nos cards revogados na mesma data: vão no chat); E1/guia e mapa na pasta privada; **APKG publicado após o questionário**, com recibo/readback em `publication.json` da execução. Aguarda revisão v4/feedback. Detalhes em [APRENDIZADOS-GENETICA-BACTERIANA.md](APRENDIZADOS-GENETICA-BACTERIANA.md).

Em 23/09/2026 foi executada, por escolha do Claude, **UC03 — Microbiologia — Fisiologia bacteriana**: após o feedback de Davi na mesma data, 38 notas/45 cards (35 AnKing, 10 autorais pequenos com imagem), 8 verdes, sem vídeos nos cards, um erro de verso do AnKing corrigido na cópia. Guia e mapa na pasta privada; APKG local. Detalhes em [APRENDIZADOS-FISIOLOGIA-BACTERIANA.md](APRENDIZADOS-FISIOLOGIA-BACTERIANA.md).

Em 23/09/2026 o Claude executou ponta a ponta **UC21 — Insuficiência metabólica (Caso 5, DM)**: 575 cards instalados em dois subdecks (roteiro × além do roteiro), E1 e guia publicados como Google Docs. Davi achou grande demais e pediu versão reduzida (núcleo calculado: 224 cards). As notas foram apagadas da coleção logo depois e aguardam decisão, sem restauração automática. Detalhes em [APRENDIZADOS-INSUFICIENCIA-METABOLICA.md](APRENDIZADOS-INSUFICIENCIA-METABOLICA.md).

## Como retomar em outra conversa

Para a próxima sessão com **Opus 5.5 / esforço alto**, ler [HANDOFF-CLAUDE.md](HANDOFF-CLAUDE.md). O modelo é escolha do usuário; o contrato de qualidade e as verificações são os mesmos. GitHub publica código/contexto; coleção, fontes privadas e inventários detalhados permanecem locais/Drive.

No Claude Code, prefira:

```text
/deck-aula <nome ou link da aula>
```

Inicie o Claude Code na raiz deste repositório e abra uma sessão nova depois de alterações em `.claude/commands/`, para que o slash command seja recarregado. Se o nome/link não identificar univocamente o material, acrescente a UC ou a pasta do Drive; não é necessário repetir as preferências acima.

Sem o comando, use:

> Execute o deck da aula [link] seguindo `flashcards/projeto/README.md` e sua ordem de leitura v4, incluindo ACERVOS-REFERENCIA e PUBLICACAO-POR-UC. Resolva pendências anteriores sustentadas; entregue E1 explicativa, guia com vídeos/bibliografia, seleção ampla de AnKing do assunto, Anki verificado e APKG comprimido da UC inteira, sem flags, atualizado na pasta privada da UC. Preserve originais/histórico; outros acervos locais antes de autoria excepcional. Relatório curto com links e contabilidade. Não trate a CLI futura como implementada.

O contexto só será conhecido quando esses arquivos forem lidos; não depende de memória implícita entre chats.

## Fontes de decisões

- [Mega prompt original, relido em 22/09/2026](https://docs.google.com/document/d/1gHGICvzQMe_B5CJFPAKwo6SvtIjcqEwBPCV5v-dBhD0/edit).
- Respostas 1–37 em `arquivos-trabalho/arquitetura-nebli-decisoes-2026-09-22.md`.
- Respostas mais recentes: [CALIBRACAO-ESCALA-V4.md](CALIBRACAO-ESCALA-V4.md) e registro literal ligado nele. Q18/Q22 ainda exigem explicação da interface; Q26, carga real. Q25 foi simplificada: manter como padrão, candidatos rosas e decisão pessoal a cada prova.
- Não migrar regras especiais do projeto de etimologia para os decks médicos.
