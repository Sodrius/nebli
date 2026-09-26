# NEBLI — decisões para a nova arquitetura

Data: 2026-09-22. Estado: decisões levantadas; arquitetura v1 em `arquitetura-nebli/ARQUITETURA.md`.

Este registro documenta a conversa. Não ativa o novo fluxo, não altera a coleção Anki e não substitui ainda os documentos operacionais existentes. O trabalho solicitado é arquitetar e preparar uma implementação posterior com um modelo mais leve.

## Objetivo e fontes

Objetivo declarado: conseguir aprender bem, de forma prática, com direcionamento para a faculdade e o Step 1. O usuário está no segundo semestre do primeiro ano e pensa em fazer o Step 1 ao final do quarto ano. Data da prova ainda aproximada.

Prompt de origem: https://docs.google.com/document/d/1gHGICvzQMe_B5CJFPAKwo6SvtIjcqEwBPCV5v-dBhD0/edit

Drive indicado: https://drive.google.com/drive/folders/18HEmYCd--zhu5KRi9IutMggaoNAtBqcK

Planilha indicada: https://docs.google.com/spreadsheets/d/1T1RZ_vpqtchmdM8U2BXYmlHk7e-Ov-iCGM51PFIEqMU/edit

O usuário pediu muitas perguntas interativas. Decisões que não souber responder devem ser reapresentadas em outra leva, com situações concretas.

## Preferências explicitamente confirmadas

1. Manter a E1. Suspender E2/E3 e substituir o processo atual de flashcards na proposta. A correção mais recente do usuário prevalece sobre sua menção anterior a suspender E1/E2.
2. Os dois problemas principais são seleção ruim de conteúdo e qualidade ruim dos cards. Priorizar esses problemas antes de acelerar a produção.
3. Aprendizado principalmente por videoaulas, bibliografia sugerida e materiais de cursinho. E1 usada ocasionalmente para consultar escopo ou quando não houver boa fonte de estudo.
4. Usar múltiplas fontes: slides, bibliografia, vídeos, provas antigas e outros materiais pertinentes. A E1 participa da definição do conteúdo, mas não é fonte exclusiva.
5. Se uma aula exigir 120 bons cards, entregar os 120 disponíveis, divididos entre núcleo recomendado e reserva. Sem teto rígido por aula.
6. Aceita aumentar temporariamente o tempo diário perto das provas. Isso não significa aceitar carga permanente ilimitada.
7. Sem prioridade universal faculdade versus Step 1. Nos exemplos posteriores, aprovou detalhes de protocolo para a prova com pausa posterior, preservando o princípio; aprovou pequenas pontes clínicas compreensíveis no núcleo durável mesmo sem cobrança local prevista.
8. Frente e resposta em inglês; ajuda e explicação em português quando necessário. Sem duplicar por idioma.
9. O mesmo card deve poder aparecer nas seleções de várias aulas, existindo uma única vez e mantendo um único histórico de revisão.
10. Cópias NEBLI independentes; AnKing original preservado como referência. Não depender de atualizações automáticas do AnKing/AnkiHub nas cópias.
11. Card pertinente com pré-requisito ainda não estudado pode ser incluído: sinalizar e indicar videoaula; decisão de suspender fica com o usuário. Não criar bloqueio automático de pré-requisitos.
12. Liberação pela data do cronograma, com possibilidade de correção manual.
13. Depois da prova, manter automaticamente o núcleo durável e pausar detalhes locais.
14. Preferir poucos vídeos bons; indicar trechos quando verificados e explicar as lacunas separadamente.
15. Incluir pequenas pontes clínicas relacionadas à aula para preparação progressiva ao Step 1.
16. Tutor de cards difíceis fica para depois. Primeira versão centrada em decks confiáveis.
17. Entrada por comando no Codex/Claude, passando nome ou link da aula.
18. Usar somente assinaturas atuais; nenhum gasto adicional com APIs. Quais assinaturas e integrações estão disponíveis ainda precisa ser identificado.
19. Primeira versão para uso pessoal. Compartilhamento com colegas em etapa posterior.
20. Sucesso após o primeiro mês: aprender bem de forma prática, com alinhamento à faculdade e ao Step 1; não medir sucesso apenas por quantidade de cards produzidos.

## Segunda leva — respostas 21 a 32

21. Os 50 minutos diários incluem novos cards e revisões regulares. Sessões extras de estudo direcionado/cram não entram nesse orçamento; eventuais revisões futuras geradas por essas sessões precisam aparecer na projeção.
22. Tempo extra perto da prova decidido conforme cada prova, sem teto adicional fixo por enquanto.
23. Usa tablet e notebook; celular menos, mas quer ampliar seu uso. Já revisa cards NEBLI e usa AnkiHub. Preservar histórico e separar cópias NEBLI dos originais gerenciados pelo AnkiHub. Sistemas operacionais e perfil principal ainda não identificados.
24. Piloto: Patologia da inflamação. Materiais e identificação exata da aula ainda precisam ser localizados.
25. Gerar E1 SEMPRE junto do deck. A E1 continua sendo consulta opcional para o estudante. E2/E3 ficam fora do fluxo.
26. Detalhes de protocolo laboratorial relevantes para a prova podem ser pausados após a avaliação; manter o princípio do método no núcleo durável.
27. Pequena ponte clínica compreensível e diretamente ligada ao mecanismo pode entrar no núcleo durável mesmo sem cobrança local prevista, com indicação de vídeo.
28. Atualizações de calendário serão processadas ao executar o comando no Codex/Claude. Primeira versão sem serviço em segundo plano.
29. Bibliografia varia por matéria e está em locais diferentes. Perguntar onde o usuário está estudando quando necessário e guardar a referência. Não exigir biblioteca inteira baixada. Distinguir fonte sugerida de fonte efetivamente acessada. Assinaturas específicas não foram respondidas.
30. Aulas atuais primeiro; recuperação de aulas antigas gradual.
31. A planilha é a fonte principal de datas de aulas e provas, prevalecendo sobre cronogramas oficiais. Aba e campos exatos ainda precisam ser identificados.
32. Avaliação inicial pelos cards e pelo desempenho nas provas da faculdade. Não adicionar testes de explicação de mecanismos ou questões extras como requisito do piloto; não reativar E2/E3.

## Consequências propostas pelo arquiteto, ainda sujeitas ao fechamento

### Terceira leva — respostas 33 a 37

33. Tablet e celular Android; notebook principal Mac. A sessão atual está no Windows, que não deve ser presumido como hospedeiro da coleção principal.
34. Materiais do piloto em UC03 → Patologia. A exploração identificou a pasta `38 - Inflamação aguda`, com transcrição e PDF antigo de etapas 1 a 3. Bibliografia particular do piloto ainda não informada.
35. O usuário autorizou explorar a planilha. A aba `Matérias` contém blocos por UC e a aba `Mês` contém o calendário mensal editado pelo usuário.
36. Assinatura atual: Codex. Pode considerar Claude futuramente, mas o desenho não deve depender dessa contratação.
37. Quando houver divergência, `Mês` prevalece nas datas porque é onde o usuário atualiza mudanças. `Matérias` continua útil para identificação, componente, número de conteúdo e vínculos com provas. Exemplo observado: P1 UC03 em 28/08 em `Matérias` e 04/09 em `Mês`.

### Consequências de arquitetura

- Um mapa de objetivos da aula orienta E1, seleção de cards e indicação de recursos. Deve permitir verificar separadamente o que está explicado e o que é efetivamente cobrado pelos cards.
- Nenhum card precisa obrigatoriamente estar explicado na E1 se houver outra fonte de aprendizagem adequada e identificada. Fonte disponível não significa conteúdo já estudado.
- Separar acervo, seleção para a aula, prioridade para a prova e manutenção longitudinal. Um único rótulo high yield não representa essas dimensões.
- Separar nota Anki de card gerado por template/cloze. Contar carga em cards reais e revisões, não apenas em notas.
- Criar uma única cópia NEBLI por identidade da nota de origem; associar seus cards pertinentes a múltiplas aulas. A granularidade por card precisa evitar inclusão involuntária de clozes irmãos fora do escopo.
- Preservar identidades e histórico existentes na migração. Recriar cards já estudados não é estratégia de atualização.
- Na pausa pós-prova, respeitar escolhas manuais e outras aulas/provas que ainda precisem do mesmo card.
- Cronograma indica elegibilidade, não domínio. Cards liberados entram conforme o ritmo diário; liberação não obriga estudar todos no mesmo dia.
- Atualizações por data acontecem na execução do comando. Uma data vencida durante um período sem execução não deve ser reportada como ação já aplicada.
- Medir o piloto pela qualidade e cobertura dos cards, experiência de revisão, correções necessárias, tempo de uso e desempenho nas provas já realizadas pelo usuário. Sem avaliações adicionais obrigatórias. Nota de prova é um resultado acompanhado, não prova isolada de causalidade ou de domínio integral.

## Evidências da inspeção do projeto

Inspeção de código e documentos, sem executar mutações no Anki. Estados históricos nos documentos não foram tratados como estado atual da coleção.

- `FLASHCARDS.md`, `CLAUDE.md` e `flashcards/DECK-AULA-PIPELINE.md` contêm regras que vinculam cards à E1 e exigem enriquecimento da E1/E2. Será necessária migração explícita dessas regras para evitar conflito com o novo desenho.
- `flashcards/scripts/copiar_curadoria_para_deck.py` verifica duplicação no deck de destino por primeiro campo, pode acrescentar prefixo ao texto e remove tags com prefixo `#AK`. Não implementa a identidade global e preservação de tags desejadas.
- `flashcards/scripts/montar_deck_aula.py` verifica duplicação por primeiro campo dentro do destino; chama `createDeck` antes de verificar `--dry`. Esse modo não deve ser considerado estritamente não mutante.
- `flashcards/scripts/verificar_cobertura_deck.py` procura palavras na frente e no Extra. Isso verifica presença textual, não se a pergunta testa o objetivo. Também lê notas para contagem; não representa necessariamente o número de cards estudáveis.
- `flashcards/scripts/validate_lesson_coverage.py` oferece inventário e justificativas estruturadas úteis, mas exige E1 e usa trechos textuais como referências. Reaproveitar conceitos após revisar o contrato.
- `flashcards/scripts/anki.py` repete chamadas após timeout. Para escrita, resultado desconhecido exige reconciliação antes de repetir, evitando duplicações.
- `flashcards/scripts/subir_drive.py` contém mapeamento fixo para poucas aulas. Nova arquitetura deve resolver aula e destino por identificadores persistentes.
- Existem scripts, testes, exemplos de cards, rubricas visuais e materiais de decks externos reaproveitáveis; sua presença não prova integração nem funcionamento atual.
- O registro `flashcards/deck-cards/registro-deck.md` é um snapshot de julho. O perfil e o estado vivo do Anki ainda não foram verificados nesta arquitetura.
- Há alterações locais preexistentes em regras e materiais de glicogênio. Preservá-las; não restaurar nem sobrescrever em massa.

## Perguntas ainda necessárias

- Confirmar na implementação o perfil principal e as versões/integrações instaladas no Mac. Não bloqueia a especificação da arquitetura.
- Perguntar a bibliografia usada no piloto quando necessário; fontes já localizadas permitem iniciar a preparação.
- Resolver ambiguidades específicas do calendário na execução, sem voltar a perguntar a hierarquia já decidida.
- Escolher destino privado para novos artefatos: a pasta existente da aula é compartilhada, mas a primeira versão foi definida como pessoal. Não publicar novos pacotes nela por mera inferência.

## Referências técnicas consultadas

- Opções e simulação de carga do Anki: https://docs.ankiweb.net/deck-options.html
- Seleções por estudo filtrado: https://docs.ankiweb.net/filtered-decks.html
- Importação e atualização de pacotes: https://docs.ankiweb.net/importing/packaged-decks.html
- Notas e edição: https://docs.ankiweb.net/editing.html
- Matriz oficial do Step 1: https://www.usmle.org/exam-resources/step-1-materials/step-1-content-outline-and-specifications

Essas referências informam o desenho. Compatibilidade com a instalação do usuário, importação cruzada de pacotes por aula/UC e preservação de histórico precisam ser verificadas na implementação, em perfil de teste antes de mudanças na coleção principal.
