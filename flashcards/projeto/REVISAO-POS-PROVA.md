# Revisão pós-prova — completar com aprovação de Davi

Instituída em 04/11/2026 (F-20261104-CODEX-03). Preferência vigente: MEMORY §12b.

## Como iniciar

“Faz a revisão pós-prova da UC03 P3” basta. Executar a investigação inteira e entregar propostas prontas; parar antes de alterar o Anki. A revisão acontece quando Davi pedir, sem agendamento, prova extra ou mudança no FSRS. O objetivo é aproveitar que ele agora conhece o assunto para decidir o que vale manter para a vida.

Abrir `arquivos-trabalho/pos-prova-<uc>-<prova>-<data>/`, registrar responsável no ESTADO-ATUAL e copiar o [molde de relatório](MOLDE-REVISAO-POS-PROVA.md) para `RELATORIO.md`. Reutilizar fontes e buscas existentes, mas conferir o deck vivo. Não iniciar a fila de novas aulas por causa deste pedido.

## 1. Reunir a base

- Identificar UC, prova, aulas e turma (Davi é Turma B da UC3 em 2026); não presumir o recorte pelo cronograma da Turma A. Perguntar apenas se o recorte não puder ser encontrado.
- Inventariar material local, Drive pessoal e da turma, e-Disciplinas e bibliografia disponível: resumos (inclusive Grande Resumo/monitoria), apostilas, slides, transcrições, roteiros práticos, listas, questões orientadoras, prova realizada, gabarito e provas antigas. Usar ferramentas e regras de acesso de cada fonte.
- Para cada fonte, registrar caminho/link, versão/data, páginas/questões relevantes, leitura realizada e limitações. Material indisponível fica explícito; não alegar ter consultado tudo se houve lacunas de acesso. Não exigir que Davi reenvie o que já estiver acessível.
- Relato de memória da prova é indício identificado como tal; não inventar enunciado ou gabarito. Divergências entre resumo, prova e livro devem ser resolvidas por fonte apropriada ou apresentadas como incerteza.
- Ler comentários, gosteis, suspensões e alterações pessoais. Dificuldades relatadas após a prova orientam a revisão, mas não são pré-requisito para começar. Não inferir erro de conteúdo apenas de lapso/nota baixa.

Salvar `fontes.tsv` (id, localização, versão, trecho, leitura, limitação) e `deck-antes.json` com IDs, campos relevantes, associações, flags e suspensões. Coleta somente de leitura; nenhuma tag ou marca de comentário alterada nesta fase.

## 2. Mapear o que realmente falta

Confrontar as fontes com as frentes dos cards vivos, incluindo cards compartilhados e suspensos. Registrar `cobertura.tsv`: fonte/questão, conceito ou relação, capacidade exigida, IDs que a recuperam, diagnóstico, proposta associada.

Diagnósticos: coberto; ausente; parcial; presente só no Extra/Tab; mal induzido; falta organizador/comparação/conexão; visual insuficiente; existe mas está suspenso; duplicado; fora do recorte. Menção do termo não comprova que o card permite lembrar, explicar, distinguir ou reconhecer o alvo.

Verificar tanto as questões da prova quanto o assunto inteiro: mecanismos, fundamentos, comparações, conjuntos, conexões entre aulas, reconhecimento visual e detalhes básicos/AnKing-Step que agreguem. A prova revela lacunas, mas não limita o conhecimento ao que caiu. Separar lacuna indispensável, complemento útil e aprofundamento opcional. Não impor teto de cards nem completar por volume; justificar o ganho e o custo de revisão de cada proposta.

## 3. Buscar candidatos e escolher a intervenção

Seguir E2–E5 do pipeline vigente para cada lacuna: entender o alvo antes da busca; consultar seções de recursos, palavras-chave/sinônimos e significado, em AnKing, demais acervos e NEBLI vivo. Registrar consultas, candidatos lidos, IDs, origem e motivo de escolha/descarte em `busca/`. Usar os comandos do [pipeline](EXECUCAO-DECK-AULA.md), com seus pré-requisitos; não falsificar registros de etapa para fazer uma busca passar.

Preferir AnKing adequado e reaproveitamento de notas existentes; autoral só para lacuna demonstrada, com exemplar aprovado da mesma função. Ler o candidato completo: sem adicionar ficha de doença só porque o nome apareceu. Um organizador precisa recuperar o conjunto ou contraste que falta; conferir avulsos já cobertos e propor separadamente qualquer suspensão/substituição. Pequeno detalhe pode justificar card, ajuste no Extra ou Tab, conforme a necessidade de recuperação. Tabs só são gerados quando incluídos na aprovação.

Para cada proposta, preparar conteúdo final e destino, incluindo mídia quando necessária. Se editar, mostrar antes/depois; se incluir, mostrar frente, resposta/clozes e Extra. Se reaproveitar, mostrar o ID vivo e qualquer efeito em outros decks. Não instalar candidatos para que Davi consiga vê-los: apresentar prévias locais ou no relatório.

## 4. Entregar para decisão

Usar IDs estáveis P01, P02 etc. Cada item deve trazer:

- O que falta e por que agrega, com fonte e página/questão.
- Cobertura atual e por que ela não basta (IDs ou busca negativa documentada).
- Ação exata: incluir AnKing, associar existente, criar organizador/autoral, editar, melhorar imagem/Extra/Tab ou sugerir suspensão.
- Texto completo ou antes/depois; origem/ID AnKing; deck e posição propostos.
- Prioridade, número de notas e cards novos (contar clozes), cards alterados, dependências e impacto em suspensões/histórico.
- Decisão inicialmente **pendente**. Davi pode aprovar, rejeitar, pedir ajuste ou adiar.

Apresentar primeiro uma tabela curta por tema/prioridade, seguida das propostas completas. Não esconder propostas opcionais; separar para facilitar a escolha. Mostrar também os temas já cobertos e as limitações da auditoria. “Muito completo” significa cobertura demonstrada no recorte e nas fontes consultadas, sem promessa de exaustividade universal.

**Ponto de parada obrigatório por pedido de Davi:** aguardar aprovação das propostas concretas. “Aprovo P01 e P03; P02 não” autoriza apenas esses itens. Silêncio, pedido de análise ou autorização antiga de fazer decks não autorizam esta escrita. Ajuste de conteúdo após aprovação volta para avaliação; não aproveitar a janela para corrigir outros cards. Itens dependentes precisam de aprovação conjunta ou alternativa que preserve cobertura.

## 5. Aplicar apenas o aprovado

Registrar a fala de aprovação, data, IDs e versão exata dos textos em `decisoes.json`. Antes da escrita, reler os cards afetados: se Davi ou outro executor os modificou, reconciliar e reapresentar diferenças materiais. Preparar alteração incremental nas corridas de origem; usar E6–E8 e os gates/revisores aplicáveis do pipeline vigente. Esta rota não substitui os controles de qualidade.

Backup antes da escrita; usar `nebli.decks.escrita()`, preservar originais AnKing, IDs/histórico, comentários, flags e suspensões pessoais. Não mover, dessuspender, retirar, fundir ou apagar sem que essa ação conste da proposta aprovada. Não tocar nota em tela/irmãos; sincronizar quando ocioso. Verificar os campos e cards resultantes contra a proposta aprovada, atualizar cobertura e pacote aplicável, registrar recibo e atualizar ESTADO-ATUAL.

Encerrar com aprovados aplicados, falhas/adiamentos, rejeitados e o que ainda ficou sem cobertura. Rejeição é decisão de Davi, não lacuna a preencher automaticamente na próxima rodada; só reapresentar com nova evidência ou pedido dele. Registrar preferências aprendidas no fluxo FEEDBACKS → MEMORY, sem generalizar rejeição pontual para todos os assuntos.

## Limite desta estrutura

Este documento e o molde organizam o trabalho e a aprovação; não são uma automação de escrita nem um novo gate de software. Nenhum comando de instalação deve ser executado durante a proposta. A implementação de cada lote aprovado deve preservar a lista exata de ações autorizadas e os controles existentes.
