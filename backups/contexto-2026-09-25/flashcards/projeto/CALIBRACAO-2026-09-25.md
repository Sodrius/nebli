# Calibração de 25/09 — acervo amplo, manutenção pequena

Vigente para Claude e Codex. Davi pediu reler o Docs atualizado e, depois da auditoria, "já ajeita o que der, deixa pronto pro claude e pra outras sessões saberem". Este complemento prevalece sobre v4/pilotos nos pontos abaixo. Não reativa E2/E3, E1/guia ou upload de APKG pausados no lote atual.

## Intenção atual

- O produto é permitir estudar sem ter de fabricar, procurar ou auditar cards. Feedback pessoal serve à calibração, não substitui nossa revisão.
- Acervo da aula pode ser amplo, com preferência por sobra **pertinente**, não clínica lateral. Davi está no ciclo básico: entender qual aula é esta vem antes de expandir tags Step.
- A manutenção é outra seleção. Nova referência declarada: **35 cards por aula ou menos a longo prazo**. Não é teto de produção nem autorização para destruir cards bons. Contar cards únicos/compartilhados e cobertura do núcleo, não selecionar os primeiros 35. Se relações essenciais não couberem, explicar o conflito em vez de omitir silenciosamente.
- 35 cards/aula não é 35 novos/dia. A referência diária continua 35 novos e aproximadamente 50 minutos incluindo revisões, ainda sem validação de sustentabilidade.

## Cores

- **Azul (`flag:4`) substitui rosa (`flag:5`)** para bom candidato à suspensão pós-prova. Ativo é o padrão; Davi decide suspender. Não usar azul para guardar card ruim ou fora de escopo.
- Vermelho = melhorar; laranja = pedido pendente. Preservar marcas pessoais.
- Verde ainda tem implementação verificável de **HY literal AnKing**. O Docs manifesta vontade de que verde represente também "não suspender"; não tratar essa intenção como classificador de núcleo validado. HY da fonte e utilidade marginal para este aluno são dimensões diferentes. Sem bandeira NÃO significa núcleo aprovado, nem low yield.
- Não migrar toda `flag:5` globalmente. Somente marcas de curadoria NEBLI identificadas e conferidas; não tocar referências/etimologia. Na auditoria de 25/09 a migração prevista limita-se aos IDs do snapshot, após conferir estado atual.

## O que a auditoria ensinou — controles obrigatórios

1. **Feedback negativo vira caso de regressão.** Em Intestinos, Lgr5/Ascl2/Olfm4/Bmi1/Hopx/Tert foram rejeitados como cobrança ilustrativa na Q2. Não reintroduzir essas perguntas por aparecerem no slide. O objetivo é renovação, organização e reconhecimento, salvo nova instrução explícita de Davi.
2. **Identidade não é equivalência semântica.** Não encontrar duas `source::nid` iguais não prova ausência de repetição. Comparar alvo e direção entre autorais e fontes/cópias existentes. Ex.: PRR→PAMP já existe em Inflamação aguda; associar antes de autorar de novo.
3. **A busca ainda pode dar falso negativo.** Em 25/09 havia no AnKing notas de macrófagos com hemossiderina (`1471914979068`) e fígado em noz-moscada por falência direita (`1471915035278`), apesar de autoria nesses alvos. Ler clozes/Extras e justificar ganho antes de manter autoria; não aceitar "não tem no AnKing" sem novas buscas.
4. **A resposta não pode estar dada na frente.** X-gal dizia "blue product" antes de perguntar `blue`. Conferir frente renderizada, não apenas presença de cloze.
5. **Imagem existente não prova recuperação visual.** Conferir alvo/seta/oclusão e legibilidade; texto que entrega "grandes células róseas" pode permitir responder sem olhar a lâmina. Imagem de apoio é útil, mas não equivale a prova prática.
6. **Precisão é independente da fidelidade ao slide.** "Vias aéreas inferiores são estéreis" não deve ser memorizado como verdade atual. Divergências com ensino antigo precisam de nota sucinta, não reprodução automática. AnKing também exige checagem.
7. **Origem deve vir da fonte real.** 38 cards externos estavam rotulados AnKing; o inventário rastreou `source_nid` à coleção de origem. Não usar nome do modelo ou grupo de seleção como corpus.
8. **Autoral focal, natural, em inglês**, apoio PT quando útil. Sem rodapé de curadoria; crédito de figura é diferente de comentário meta. Não perseguir média de palavras igual ao AnKing às custas de sentido. Imagem quando ensina, sem figura decorativa obrigatória.
9. **Cobertura em duas passadas:** material→alvos importantes→cards/versos/visuais; depois cards→alvos para encontrar excesso. O núcleo reduzido precisa passar novamente pela primeira passada. Verso conta para aprender, não garante recuperação ativa.

## Próximo trabalho, por prioridade

1. Ler o relatório e o recibo local da auditoria (`arquivos-trabalho/auditoria-lote-2026-09-25/`). Conferir estado vivo antes de qualquer mudança. Não executar scripts de criação antigos para atualizar um deck: eles contêm cores/escopo/seleções superados.
2. Reavaliar autoria e duplicações em Edema, Inflamação início/resolução, Intestinos e Operon; depois demais aulas. A proporção não é cota nem prova de erro.
3. Fazer **proposta de núcleo por aula**, preservando cobertura conceitual/visual e compartilhados. Azul com motivo no manifesto, jamais justificativa meta no card. Patogenicidade exige separar conceitos gerais, organismos centrais e detalhes de exemplos; provas ajudam, não provam sozinhas a intenção docente.
4. Implementar acesso fácil à seleção lógica da aula, por card/cloze, incluindo compartilhados. O botão de cram precisa separar treino de agendamento. Deck filtrado comum não inclui suspensos: não prometer independência do estado sem implementação/teste. Não dessuspender permanentemente nem duplicar histórico como atalho.
5. Validar uso real e dispositivos. Em 25/09, 1.453/1.453 cards do perfil consultado tinham `reps=0`: não estimar retenção, velocidade pessoal ou superioridade de um modelo a partir disso.

## O que continua incerto — não fingir decisão fechada

- A interpretação exata de verde como núcleo personalizado, mantendo ou não a semântica HY literal.
- O núcleo de cada aula: não foi classificado nesta auditoria; 35 é orçamento desejado, não resultado garantido.
- Se Patogenicidade cobra cada organismo/detalhe ou usa parte como ilustração. Solicitar direcionamento somente nos casos que mudam a seleção, com exemplos concretos.
- Cobertura total de todas as aulas: não foram reconferidos integralmente todos os slides, provas, capítulos e imagens. Ausência de lacuna detectada não prova completude.
- Cram com suspensos, acesso por aula sem irmãos indevidos e experiência Mac/Android: precisam de implementação/verificação.
- O "agente calibrador/Jarvis" é ideia para evoluir com feedback. Hoje há critérios e auditoria assistida, não agente autônomo validado nem promessa de garantia absoluta.

Fonte de intenção: [Docs relido, modificado em 25/09/2026](https://docs.google.com/document/d/1gHGICvzQMe_B5CJFPAKwo6SvtIjcqEwBPCV5v-dBhD0/edit). As notas antigas desse documento são brainstorming, não ordem para reativar cores, tradução integral, união automática de clozes ou publicação que decisões posteriores revogaram.
