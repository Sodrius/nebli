# NEBLI — arquitetura v1 para E1, decks e estudo longitudinal

> **Substituída nos pontos de conflito pela [arquitetura v2](../../flashcards/projeto/ARQUITETURA.md).** A v2 incorpora o formato aprovado do piloto e o recorte por aula, sem inclusão recursiva de pré-requisitos. Este texto permanece como histórico.

22/09/2026. Especificação para implementação posterior; o pipeline atual ainda não foi alterado.

Leitura complementar: [decisões do usuário](../arquitetura-nebli-decisoes-2026-09-22.md), [descobertas verificadas](DESCOBERTAS.md) e [roteiro do executor](IMPLEMENTACAO.md).

## 1. Resultado que o sistema deve entregar

Um comando com nome ou link da aula produz E1, deck completo, núcleo recomendado, reserva e um guia curto de onde estudar. Ao executar, também reconcilia calendário e estado do Anki. Aulas atuais têm prioridade; conteúdo antigo entra progressivamente.

O usuário aprende principalmente com vídeos, livros e materiais de cursinho. A E1 é sempre produzida como explicação e referência de escopo, mas sua leitura não é condição para estudar os cards. E2/E3 e o tutor durante a revisão ficam fora da primeira versão.

A rotina longitudinal dispõe de aproximadamente 50 minutos para novos cards e revisões. Estudo direcionado extra fica fora desse orçamento, mas suas consequências futuras sobre as revisões devem ser consideradas. Não há promessa de que todo o acervo caiba nesse tempo: o sistema deve mostrar a diferença entre material disponível e material efetivamente incorporado à revisão.

Não construir um aplicativo web, um serviço de IA permanente, uma equipe de agentes ou um novo algoritmo de repetição espaçada. Usar uma sessão do Codex, scripts locais, o Anki e os arquivos já existentes. Claude pode ser adaptado no futuro sem ser dependência.

## 2. O modelo central: objetivos, fontes e perguntas

O objeto central é um objetivo recuperável: algo que o estudante deve conseguir lembrar, distinguir, localizar ou explicar. Cada objetivo possui origem verificável, relevância para a aula, valor longitudinal e uma forma apropriada de estudo.

Fluxo: fontes da aula → mapa de objetivos → curadoria e recursos de estudo → E1 + deck → auditoria → aplicação e publicação.

O mapa é um contrato comum, não uma lista gerada exclusivamente da E1. A lista ampla de assuntos do AnKing também não define o escopo da aula. Exemplos de granularidade: “recrutamento celular” é um assunto; discriminar etapas e seus mediadores pode exigir diferentes objetivos. O nível de decomposição depende do que as fontes efetivamente ensinam, sem converter cada frase em card.

Cada objetivo registra:

- Uma formulação clara do que deve ser recuperado e uma resposta/critério esperado.
- Fonte e localização: página, slide, seção ou trecho de vídeo verificado.
- Papel: central da aula, detalhe local relevante, pré-requisito imediato, ponte clínica ou enriquecimento opcional.
- Decisão: testar com card, abordar na E1/recurso sem card, adiar para aula identificada ou excluir com motivo.
- Cards exatos que o testam, distinguindo cobertura completa, parcial e apenas menção.

Há duas verificações independentes: fontes → objetivos (evita omissão no próprio mapa) e objetivos → perguntas reais (evita fingir cobertura porque uma palavra está no Extra). Um objetivo central só fecha se a recuperação exigida estiver coberta. Um conteúdo ilustrativo pode ficar sem card com motivo explícito.

Não há percentual científico de “completude absoluta”. Relatar cobertura do inventário analisado, fontes ausentes e decisões de recorte. O programa verifica integridade das referências; a avaliação semântica exige leitura do card renderizado pela IA e revisão do usuário no piloto.

## 3. Fontes com papéis diferentes

| Fonte | Uso principal | Limite |
| --- | --- | --- |
| Slide, transcrição, roteiro, caso e anotações | Delimitar objetivos da aula | Transcrição pode conter erros; nome de arquivo não basta para confirmar conteúdo |
| Prova antiga e objetivos docentes | Identificar exigência local e pontos de confusão | Ausência em prova antiga não demonstra irrelevância |
| Bibliografia e cursinho | Verificar e explicar os mecanismos | Só citar como consultado o conteúdo acessado; capítulo sugerido é recomendação |
| Vídeos | Dar um caminho prático para aprender | Título/tag não prova cobertura; trechos devem ser verificáveis |
| AnKing e outros decks | Encontrar boas perguntas, contrastes e lacunas do mapa | Quantidade disponível não autoriza ampliar indefinidamente a aula |
| E1 anterior | Aproveitar explicação e organização | Não é validação independente das fontes das quais foi derivada |

Bibliografia é perguntada por matéria/aula quando necessária e lembrada para as próximas. Não exigir download de todos os livros. Registrar `consultada`, `sugerida` ou `indisponível`, sem inventar página ou edição.

Além de slides, a entrada pode ser caso clínico/PBL, roteiro prático, anotação, print de livro, vídeo ou erro em questão. Todos passam pelo mesmo mapa de objetivos. Dados ausentes não são preenchidos com uma aula parecida.

## 4. Três grupos visíveis e duas prioridades separadas

| Grupo | Antes/na aula | Depois da prova | Motivo típico |
| --- | --- | --- | --- |
| Núcleo durável | Elegível a partir da aula | Continua ativo | Fundamento, mecanismo, fato relevante ou pequena ponte clínica compreensível |
| Complemento de prova | Elegível durante a janela da disciplina | Pausado quando nenhuma avaliação pertinente ainda o exigir | Detalhe local necessário, como um protocolo específico |
| Reserva | Disponível, inicialmente suspensa | Continua disponível | Complemento pertinente de menor prioridade |

“Núcleo recomendado agora” = núcleo durável + complemento de prova pertinente. Não confundir esse conjunto com o que deve permanecer por anos. Um objetivo pode ter importância local e longitudinal simultaneamente; nenhuma dessas classificações é sinônimo de etiqueta high yield de um deck externo.

Se a aula exigir 120 cards de qualidade, entregar os 120 e mostrar os três grupos. A escolha do núcleo precisa cobrir seus objetivos declarados; não chamar uma seleção incompleta de cobertura total. Sem cotas de 30–50, sem proporção mínima de AnKing e sem gerar cards artificiais para atingir quantidade.

Preferências por anatomia e bioquímica aumentam a prioridade durável, sem ativar automaticamente toda informação dessas disciplinas. Conteúdo de clínica entra por conexão direta: pequena ponte mecanismo–condição–achado, sem expandir uma aula básica para uma coleção de condutas.

Pré-requisito não estudado gera aviso e recurso de estudo, não bloqueio automático. O usuário decide suspender. Rótulo Step 1 não pode justificar conteúdo incorreto, fora de escopo ou incompreensível.

## 5. Curadoria com busca ampla e decisão precisa

Ordem: reutilizar card NEBLI existente → encontrar original AnKing → procurar outros decks adequados → criar autoral para lacuna demonstrada. Reutilização é sempre verificada contra o objetivo, inclusive quando já existe na coleção.

Busca inicial combina nomes PT/EN, sinônimos, termos distintivos, conteúdo dos campos, tags por sistema/tema e referências a vídeos. Tags ajudam a localizar candidatos; não autorizam importação em lote sem leitura. Buscar também fora da tag esperada para reduzir lacunas falsas.

Para cada objetivo sem boa cobertura, fazer uma segunda busca independente: expandir termos e verificar outros caminhos de tags. Uma busca sem resultados não prova inexistência no corpus. Diferenciar `não encontrado após busca documentada`, `corpus indisponível` e `candidatos inadequados`. Não produzir autoria como se uma falha de acesso fosse ausência científica.

Usar índice local do corpus e busca textual antes de cogitar embeddings. A IA recebe lotes por objetivo com candidatos suficientes e pode expandir a busca. Paginar sem truncar silenciosamente os resultados. Não impor a leitura de 500 cards por aula nem um número universal de candidatos.

Cards visuais exigem rota própria: texto vazio em IO não significa ausência do assunto. Usar tags, imagens, rótulos e inspeção visual. Para anatomia/histologia, escolher o material pelo reconhecimento que será cobrado; esquema e peça real podem treinar habilidades diferentes e não são duplicatas automaticamente.

Todo candidato aprovado registra o objetivo e o alvo de recuperação de cada card gerado, não apenas a nota que o contém. Um cloze irmão fora do escopo fica não selecionado; copiar a nota não autoriza ativar todos os seus cards.

## 6. Qualidade de card

Frente e resposta em inglês; ajuda em português no verso quando útil. Preservar o inglês e conteúdo original de bons cards. Evitar mudanças cosméticas no texto sem necessidade.

Cada card deve ter um alvo avaliável e contexto suficiente. Cloze não é obrigatório para todo tipo de informação: fatos e discriminações podem usar cloze; relações causais podem usar pergunta curta ou cloze causal; reconhecimento visual pode usar IO. Mecanismo não exige sempre fluxograma, e uma imagem de via inteira não precisa virar uma única pergunta enorme.

Permitir múltiplos clozes quando gerarem perguntas úteis e autônomas. Não juntar `c1/c2` mecanicamente para diminuir contagem: uma nota com menos cards pode produzir uma pergunta pior. Não tratar afirmações opostas como redundantes sem verificar o que cada pergunta exige.

Comparar autorais com bons exemplos AnKing em clareza, dificuldade, pistas e concisão. Distribuição de palavras é diagnóstico auxiliar; não é meta para média, mediana ou desvio-padrão. Não impor imagem a um fato verbal. Inspecionar visualmente todas as imagens/oclusões novas ou alteradas e amostras dos modelos já validados.

Critérios de rejeição: erro factual, pergunta ambígua, resposta entregue na frente, cloze sem valor, imagem incompatível, alvo já testado sem ganho, ou conteúdo fora do recorte. Autorais e modificações de significado recebem uma segunda leitura orientada a encontrar erro antes da aplicação.

Card com problema científico não vai para reserva: reserva contém material aprovado, apenas de menor prioridade.

## 7. E1 e guia de estudo

Sempre gerar uma E1 atual da aula, aproveitando o padrão editorial/Typst existente. Fontes → mapa → seleção preliminar → E1 final + deck. Esse compartilhamento de mapa reduz divergências sem impor ciclos de reescrita a cada card encontrado.

A E1 explica o núcleo e organiza o tema. Cada card precisa apontar uma fonte de aprendizagem, que pode ser E1, vídeo ou bibliografia acessada. Não exigir que toda resposta esteja transcrita na E1. Se a auditoria revelar ausência essencial no mapa/E1, reparar pontualmente; complementos pertinentes podem ter fonte própria.

O guia, curto e separado da E1, informa objetivos, poucos recursos principais, ordem sugerida, duração dos trechos verificados, lacunas e links aos decks. Prioridade editorial dos canais: Ninja Nerd, Medicosis Perfectionalis e Patologia Fácil; depois os demais canais indicados pelo usuário, considerando adequação e duração. Preferência de canal não vence cobertura ou precisão.

Não afirmar que um conjunto de vídeos cobre tudo quando só foram lidos títulos. Sem transcrição/acesso suficiente, marcar cobertura estimada e indicar a lacuna. O caminho de estudo pode combinar vídeo e leitura curta. Não criar um resumo adicional obrigatório de duas páginas para cada ponte clínica.

Produzir PDF da E1 e guia leve em Markdown/HTML; E2/E3 não entram no template de saída. Compilar em diretório exclusivo da execução, sem limpar arquivos comuns de outras aulas.

## 8. Identidade única e seleções por aula

Decisão: uma cópia NEBLI independente por nota de origem, com vários cards quando o modelo exigir, e associações de cada card a quantas aulas forem pertinentes. Originais e histórico existente são preservados.

Identidades:

- `source_key`: namespace do corpus + GUID da nota original, obtido de exportação/inventário confiável; quando indisponível, usar identidade provisória marcada e impedir clonagem ambígua até reconciliar.
- `nebli_note_key`: identidade permanente da cópia, independente de texto, idioma, aula ou nome do deck. Notas autorais recebem identidade própria.
- `nebli_card_key`: nota NEBLI + identidade do template/cloze/oclusão, mapeada ao card real. Reordenação de templates ou renumeração de clozes é migração explícita, nunca atualização cosmética.
- `lesson_id`: UUID persistente, com UC, ano, número de conteúdo quando disponível e aliases de título. Número da linha da planilha não é identidade.

NIDs/CIDs do Anki são vínculos operacionais dentro da coleção observada; conservar também as identidades acima e uma identificação da coleção. Não usar apenas o texto da frente como chave. Texto parecido gera candidato a revisão de redundância, não fusão automática.

A cópia recebe metadados NEBLI e preserva campos pedagógicos, tags de origem, mídia e créditos. Metadados operacionais que vinculam a nota ao AnkiHub não devem vincular a cópia independente: guardar proveniência no registro e usar modelos NEBLI não gerenciados pelo AnkiHub. Clonar/versionar o modelo uma vez e conservar sua identidade; não recriá-lo a cada execução. Validar a independência em perfil de teste antes da migração.

Não editar modelos compartilhados com originais. Não suspender todos os originais só por terem tags AnKing. Detectar originais já estudados e cópias antigas: adoção/migração precisa preservar o histórico escolhido, sem transferir revlogs arbitrariamente nem criar duplicação ativa.

Organização física sugerida para novos cards: `NEBLI::2026::UC03::P2::Patologia::38 - Inflamação aguda`. Essa é a casa de origem, não a lista completa de pertencimentos. Cards existentes mantêm sua casa até uma migração justificada. Uma segunda aula associa o card; não o move nem duplica.

Seleções por aula/prova/disciplina são geradas a partir do registro. Tags são auxiliares, pois pertencem a notas, enquanto clozes diferentes podem ter associações diferentes. A consulta precisa usar CIDs verificados ou combinação validada de tag de associação e ordinal do card. Uma tag ampla de aula sozinha não é suficiente para selecionar clozes específicos.

Decks filtrados são sessões temporárias sobre as mesmas identidades. Um card não pode ocupar duas sessões filtradas simultaneamente; reconstruir uma sessão por vez e devolver cards à casa anterior ao terminar. No Android, testar a consulta e o fluxo nativo de estudo personalizado, sem depender de add-on desktop na revisão. [Manual do Anki: decks filtrados](https://docs.ankiweb.net/filtered-decks.html).

## 9. Estado e políticas de calendário

Usar `Mês` para datas efetivas e `Matérias` para catálogo/associações. Se Mês não trouxer a aula, Matérias pode fornecer data de fallback com origem explícita. Contradição sem correspondência segura fica pendente. Calendário sem data confirmável não libera/suspende automaticamente aquele conjunto, mas não bloqueia a preparação do material.

Manter relações muitos-para-muitos aula–avaliação. A célula `P1; P2; P3; P4` não vira uma prova única. Mudanças na planilha alteram o calendário normalizado; não reidentificam a aula. Registrar remarcações e processar pendências somente ao executar o comando.

Regra de ativação, avaliada por card:

1. Falha de qualidade ou conflito de identidade bloqueia aplicação do card.
2. Escolha manual explícita de suspender/manter prevalece sobre automação de calendário.
3. Se houver associação durável já liberada, manter ativo.
4. Senão, se houver complemento de prova liberado e ainda requerido por avaliação válida, manter ativo.
5. Senão, reserva/futuro/pós-prova fica suspenso, preservando histórico.

Quando uma prova termina, pausar apenas o complemento que nenhuma outra associação ainda exige. Uma aula futura não suspende um card durável já estudado em outra. Prova remarcada pode reabrir a janela automaticamente, respeitando overrides. Examinar inconsistências como avaliação anterior à aula antes de agir.

Aplicar pausa pós-prova no primeiro comando executado após o fim do dia da avaliação, no fuso da planilha, como default ajustável. Se faltar data ou o vínculo for incerto, não inventar vencimento. Liberação inicial ocorre pela data da aula, com antecipação/adiamento manual disponível.

O registro separa `policy_target` de `observed_anki_state` e `last_applied_state`. Uma mudança externa em suspensão é preservada como intervenção do usuário ou estado a esclarecer. Não reativar automaticamente leeches ou suspensões cuja causa não se conhece. Enterramento temporário do Anki não é suspensão manual.

## 10. Ritmo: 50 minutos, sem promessa de 35 novos/dia

400 respostas em 50 minutos exigem média de 7,5 segundos por resposta; 500 exigem 6 segundos. Essa conta aritmética não demonstra que novos cards, IO e falhas caibam no tempo. Uma resposta/repetição também não equivale necessariamente a um card distinto.

Medir minutos de revisão, novos introduzidos, reaprendizado, atrasos e tempo das sessões extras. O contador do Anki pode não capturar pausas, leitura e raciocínio fora da tela; aceitar correção do usuário. Observar inicialmente duas a três semanas e projetar cenários, sem usar uma razão fixa revisões/novos como garantia.

Preservar configuração FSRS existente no início. Usar os dados e o simulador disponível no Anki para orientar a carga; não escrever parâmetros de memória à mão. Com atraso crescente ou tempo excedido, recomendar reduzir entrada de novos antes de ocultar revisões devidas. Não alterar retenção desejada nem reagendar a coleção em massa para maquiar a fila. [Manual: opções e simulador](https://docs.ankiweb.net/deck-options.html).

Se ainda não houver histórico suficiente, manter o limite atual como ponto de partida e declarar a estimativa incerta. O relatório semanal mostra se o núcleo recebido cabe no ritmo ou se está formando fila. A decisão pode ser aumentar tempo, alongar a introdução ou reavaliar prioridades; não ocultar o conflito apagando objetivos.

Estudo dirigido: distinguir revisão com agendamento e preview sem reagendamento. Reserva suspensa não entra automaticamente em deck filtrado; o modo preview deve resolver isso explicitamente e restaurar o estado anterior ao terminar, inclusive após interrupção. A implementação só oferece esse atalho depois de testá-lo. Enquanto isso, o navegador permite consultar reserva e o usuário pode ativá-la deliberadamente.

Não suspender automaticamente um card apenas porque parece fácil: facilidade e intervalos longos não significam ausência de valor longitudinal. A escolha de suspender continua disponível ao usuário.

## 11. Mapa longitudinal do Step 1

Começar com uma taxonomia pequena por sistema e objetivo, baseada na matriz oficial, versionada e consultada novamente quando a prova se aproximar. Não construir antecipadamente um mapa gigantesco de cada card existente.

Para cada objetivo: ainda não abordado, material disponível, cards selecionados, estudo iniciado, revisão ativa ou avaliação insuficiente. Separar cobertura curricular de evidência de domínio; não transformar uma tag em porcentagem de prontidão para a prova.

Aulas acrescentam associações a esse mapa. Lacunas importantes recebem uma aula futura provável ou tarefa de recuperação. O mapa orienta a progressão; não obriga ativar fisiopatologia inteira durante anatomia. Pequenas pontes diretas aprovadas pelo usuário entram normalmente.

Tags high yield do corpus são um sinal editorial, não frequência oficial comprovada de uma questão. Usar matriz oficial, relevância causal, exigência local e erro recorrente como justificativas distintas. A matriz do USMLE descreve áreas e competências, não uma lista pública exaustiva de tudo que já caiu. [Conteúdo oficial do Step 1](https://www.usmle.org/exam-resources/step-1-materials/step-1-content-outline-and-specifications).

Mostrar HY como rótulo derivado e explicado; não prefixar todas as aulas nem atribuir HY só porque contêm um card relevante. Bandeira roxa pode ser uma preferência visual configurável em cards sem bandeira pessoal; prioridade real fica no registro, pois bandeiras já servem ao feedback do usuário.

## 12. Mac, Android e sessão atual no Windows

Recomendação de operação: executar o comando final no Mac que hospeda a coleção principal. Scripts usam caminhos relativos e configuração por máquina. A IA faz análise e redação na sessão do Codex; scripts determinísticos fazem inventário, validação, cálculo e aplicação. Nenhum script pressupõe chave de API de LLM ou transforma assinatura de chat em API.

No Mac, um adaptador AnkiConnect local deve ser testado contra a instalação real. Se precisar de funcionalidades não disponíveis, decidir uma extensão mínima depois de demonstrar a lacuna; não criar um servidor remoto por padrão.

O Windows pode preparar materiais e planos com um inventário exportado do Mac. Porém `localhost` do Windows não é o Anki do Mac. Sem executar o aplicador no Mac, a saída fica `pronta para aplicar`, nunca `instalada`. Na v1 não configurar acesso remoto ao Mac nem criar outra coleção principal no Windows por inferência.

AnkiWeb é a via normal para sincronizar coleção e mídia entre os dispositivos. Pacotes no Drive são artefatos, não substituto desse fluxo. O estado observado no Mac só inclui alterações do Android que já chegaram pela sincronização. Marcar horário de observação e solicitar sincronização quando necessário; não prometer leitura instantânea do tablet. [Manual: sincronização](https://docs.ankiweb.net/syncing.html).

Os cards devem funcionar no AnkiDroid, com layout responsivo, mídias locais e IO verificada. Não depender de botões/atalhos exclusivos de um add-on desktop para mostrar pergunta ou resposta. Essa compatibilidade precisa ser testada nas versões reais; não é presumida a partir do CSS.

## 13. Componentes e armazenamento

Implementar um aplicativo local modular em Python, com SQLite para estado e JSON/YAML para contratos e material revisável. São módulos de um mesmo programa, não microsserviços. O modelo de IA é o da sessão; prompts não ficam embutidos num cliente de API pago.

| Componente | Responsabilidade | O que não decide |
| --- | --- | --- |
| Entrada e orquestração | Resolver aula, abrir execução, pedir apenas dados ausentes, retomar fases | Não inventa fonte nem muda perfil Anki |
| Fontes | Ler Drive/arquivos, extrair texto e imagens, localizar trechos e registrar versões | Não define sozinho o currículo |
| Calendário | Normalizar Mês/Matérias, associar avaliações, calcular ações pendentes | Não escreve diretamente no Anki |
| Catálogo de cards | Inventariar corpus, mídia, modelos, identidades e estado observado | Não escolhe por contagem de palavras |
| Curadoria | Produzir decisões semânticas, cobertura e autoria de lacunas | Não aplica mutações |
| Editorial | Gerar E1 e guia a partir do mapa comum | Não gera E2/E3 |
| Validação | Conferir contratos, referências, artefatos e consistência | Não transforma coincidência textual em domínio |
| Aplicador | Reconciliar estado, executar plano idempotente e emitir recibos | Não altera conteúdo pedagógico por conta própria |
| Distribuição | Exportar aula/UC e publicar artefatos em destino identificado | Não confunde upload com instalação |
| Acompanhamento | Relatar carga, cobertura, feedback e pendências | Não substitui FSRS nem promete aprovação |

Estrutura sugerida, criada na implementação:

```text
nebli/
  cli.py
  domain/                  # identidades, regras e contratos
  adapters/                # Anki, calendário, arquivos e pacotes
  services/                # catálogo, política, publicação, acompanhamento
  schemas/                 # contratos versionados
  prompts/                 # tarefas pequenas para a sessão de IA
  tests/                   # invariantes e casos reais de regressão
config/
  nebli.example.yaml       # caminhos/IDs sem segredos
curriculum/
  lessons/                 # mapas revisáveis por aula
  step1.yaml               # taxonomia incremental
state/                     # ignorado pelo Git; escritor único no Mac
  nebli.sqlite
  snapshots/
artifacts/<lesson_id>/<run_id>/
  sources.json
  objectives.json
  candidates.jsonl
  decisions.jsonl
  coverage.json
  plan.json
  e1.pdf
  onde-estudar.md
  aula.apkg
  receipt.json
```

O diretório `state` não deve ser uma base SQLite viva sincronizada pelo Drive. Um único escritor controla o registro no Mac. O Windows usa snapshot versionado para preparar trabalho e entrega plano com revisão esperada; o Mac valida/reconcilia antes de aplicar. Um snapshot não se transforma silenciosamente em outra autoridade.

Fonte de verdade por dimensão: calendário nas abas definidas; decisões pedagógicas nos mapas versionados; identidade e aplicação no registro; agendamento/histórico no Anki. `README` e relatórios Markdown são visualizações desses dados, não cadastros manuais paralelos.

## 14. Modelo de dados mínimo

As tabelas abaixo são contratos lógicos. Tipos exatos, índices e migrations ficam para a implementação, preservando as cardinalidades.

| Entidade | Campos essenciais e relações |
| --- | --- |
| `source` | ID persistente, tipo, URL/file_id, versão/hash, acesso, papel, localização extraída |
| `lesson` | UUID, ano, UC, componente, número de conteúdo opcional, título, aliases, pasta-fonte, revisão |
| `lesson_source` | Aula, fonte, papel; vários materiais por aula e uma fonte compartilhável |
| `calendar_event` | ID, tipo aula/prova, data/hora normalizada, valor bruto, célula, confiança, revisão, cancelamento/remarcação |
| `lesson_exam` | Aula, prova, origem do vínculo, status de conflito; relação N:N |
| `objective` | ID, afirmação/alvo, resposta esperada, tipo cognitivo, referências, parent opcional |
| `lesson_objective` | Aula, objetivo, papel local, prioridade, decisão card/sem-card, justificativa |
| `source_note` | Dataset estável, GUID, versão do conteúdo, campos, tags, modelo, mídia; UNIQUE(dataset, GUID) |
| `nebli_note` | Chave permanente, origem opcional, GUID da cópia, NID observado, modelo, revisão; unicidade de origem para cópia canônica |
| `nebli_card` | Chave permanente, nota, identidade do template/cloze/IO, CID observado; não colapsar irmãos |
| `lesson_card` | Aula, card, grupo, motivo, data de liberação/override; UNIQUE(aula, card) |
| `objective_card` | Objetivo, card, recuperação cobrada, cobertura, justificativa, revisão auditada |
| `resource_coverage` | Objetivo, fonte/recurso, localização e evidência de cobertura; recomendação separada de consulta |
| `manual_override` | Card/evento, decisão do usuário, origem, data, vigência e eventual revogação |
| `card_state` | Coleção, card, estado observado, alvo da política, último estado aplicado, horário e sync conhecido |
| `step1_mapping` | Objetivo, nó da taxonomia, justificativa, fonte e versão da matriz |
| `run` / `operation` | Execução, hashes dos inputs, fase, revisão esperada, operação idempotente, estado, antes/depois/erro |
| `artifact` / `publication` | Artefato, hash, versão, aulas/UCs afetadas, destino file_id, estado e recibo |
| `feedback` | Card/objetivo/aula, problema, comentário, situação e resolução; sem apagar feedback ao regenerar |

Referências de cobertura apontam para `nebli_card_key`, nunca um trecho da frente. Fonte e conteúdo têm identidades distintas; atualizar um PDF ou texto não cria automaticamente uma aula/nota nova. `source_note` mantém snapshot de origem; mudanças do AnKing podem ser comparadas futuramente, mas não sobrescrevem as cópias.

Invariantes do banco: relações válidas, unicidade de cópia canônica, associações sem repetição, revisão monotônica, operações identificáveis após interrupção. Similaridade semântica não vira restrição UNIQUE: dois cards podem parecer próximos e testar habilidades diferentes.

## 15. Execução, retomada e aplicação segura

Estados de uma execução: `resolved → mapped → curated → rendered → validated → applied → exported → published`. `blocked`, `partial` e `failed` registram a fase e a causa. `published` exige recibo; não é consequência automática de existir um arquivo local.

Internamente há fases para retomar falhas, mas o usuário continua pedindo uma única tarefa. Cada fase consome artefatos tipados e grava sua saída. Mudou o slide/mapa? Invalidar decisões e E1 dependentes. Mudou apenas a data? Recalcular calendário sem reescrever o conteúdo. Mudou um card compartilhado? Invalidar os pacotes afetados, inclusive de outras UCs.

Passos do aplicador:

1. Confirmar coleção/perfil, ler revisão do registro e snapshot atual. Se o plano veio do Windows, reconciliar diferenças e revalidar apenas operações afetadas.
2. Verificar que o Reviewer está inativo e que o estado da coleção está acessível. Erro de conexão não significa janela segura.
3. Adquirir lock local de escritor, salvar backup consistente e gravar plano de operações. Usar APIs suportadas do Anki; não alterar SQLite da coleção viva.
4. Aplicar mídia, modelos necessários, notas e associações em lotes pequenos. Verificar janela segura entre lotes; usuário voltou a revisar → adiar o restante.
5. Ler de volta os objetos e conferir IDs, campos, contagem de cards, mídia e estado. Aplicar política de suspensão apenas ao conjunto explicitamente gerenciado.
6. Gravar recibo por operação e liberar lock. Gerar/exportar os artefatos a partir do estado confirmado.

Não há transação única abrangendo SQLite local, Anki, exportação e Drive. Usar diário de operações e retomada por etapa. Se `addNote` expirar, a escrita pode ter ocorrido: procurar pela identidade NEBLI gravada na operação antes de repetir. Cada criação deve carregar chave recuperável, não apenas texto.

Atualizar campos por comparação de três versões: base usada para planejar, estado atual e alteração proposta. Preservar comentários e edições pessoais. Conflito de conteúdo relevante fica localizado para decisão, sem interromper partes independentes.

Rollback compensa apenas o que a execução alterou. Se um card novo já ganhou revisão ou edição do usuário, não deletá-lo automaticamente. Não restaurar uma coleção antiga por cima de revisões novas para desfazer uma alteração pequena. Modelos existentes têm migração versionada, não reescrita global.

`dry-run` permite leitura e artefatos locais de planejamento; proíbe toda escrita no Anki, Drive e planilha, inclusive criar deck vazio. Plano e modo aplicar são mecanismos técnicos de controle, não exigência de confirmação repetida para cada operação já autorizada.

## 16. Pacotes, mídia e Drive

Gerar `.apkg` por aula e cumulativo por UC a partir do mesmo conjunto de identidades canônicas. O pacote da UC é uma união deduplicada, não concatenação de pacotes. A casa física de um card deve ser consistente entre todos os pacotes; pertencimentos adicionais ficam nas associações.

Uma nota pode gerar irmãos além dos cards selecionados para a aula. O exportador deve registrar essa expansão e manter irmãos não selecionados fora da ativação automática. Não remover/renumerar clozes só para reduzir o pacote. Importar aula → UC → aula e UC → aula em perfis de teste é requisito para validar que identidades, modelos e histórico não se multiplicam.

Os pacotes devem usar identidades e versões estáveis, incluir mídia e evitar transportar histórico pessoal de revisão. Suspensão, associação seletiva de irmãos e overrides não devem depender somente da semântica de importação do APKG: o aplicador reconcilia o estado após importação. Importação manual fora do comando não equivale a execução completa da política. [Manual: pacotes e atualizações](https://docs.ankiweb.net/importing/packaged-decks.html).

Mídia recebe inventário de origem, crédito e hash; nomes conflitantes com bytes diferentes são resolvidos sem sobrescrever imagens antigas. Dependências em CSS/HTML/áudio/IO também são incluídas. Apenas imagens efetivamente pertinentes entram; preservar crédito não substitui conferir o conteúdo visual.

Na primeira versão, sugerir raiz privada `NEBLI pessoal` com saídas por ano/UC/componente/aula e pacote cumulativo na UC. Reutilizar destino privado identificado ou criar o destino como parte da implementação autorizada; não publicar por engano na pasta-fonte compartilhada. Não alterar permissões de pastas existentes.

Para atualização, usar `file_id` registrado. Publicar somente após validação, guardar hash e versão e ler metadados de volta. Uma falha de upload deixa `applied/exported`, não dispara nova importação no Anki. Publicações da E1, deck-aula e pacote-UC têm recibos separados e um manifesto indica qual conjunto de versões está completo.

Planilha continua sendo entrada de calendário. Não reformatar a rotina do usuário. Uma aba de saídas NEBLI com links pode ser proposta na implementação, mas não é dependência do piloto; o guia e o relatório já dão acesso aos materiais. A coluna `E` não será sobrescrita nem reinterpretada como estado técnico.

## 17. Comandos e experiência

Nomes propostos, ainda não implementados:

```text
nebli aula "UC03 Patologia inflamação aguda"
nebli atualizar
nebli estudar "UC03 P2" --modo revisao
nebli estudar "inflamação aguda" --modo preview
nebli manter <card>
nebli pausar <card>
nebli complementar <fonte-ou-erro>
nebli status
```

A entrada natural no Codex chama a mesma lógica. `aula` reconcilia calendário, resolve fontes, prepara o mapa, cura, produz E1/guia/deck, valida e aplica conforme as condições do host. `complementar` usa a mesma deduplicação e proveniência; não cria um segundo gerador desgovernado.

Relatório ao usuário: o que foi produzido/aplicado; total de cards e quantos são realmente novos; grupos durável/prova/reserva; objetivos cobertos e pendências; fontes principais de estudo; ações de calendário; carga estimada; links. Detalhes de IDs, logs e schemas ficam nos artefatos técnicos.

Pedir ajuda apenas para dado que muda a decisão e não foi encontrado: aula homônima, material ilegível, bibliografia necessária, vínculo de prova incoerente, conflito com edição pessoal. Não perguntar novamente preferência já registrada.

## 18. Migração e avaliação

Começar por inventário e adoção de identidades. Preservar cards NEBLI já revisados e seus agendamentos. Se houver várias cópias antigas, apresentar grupos de possível redundância e escolher sobrevivente com critério explícito; não fundir históricos nem deletar em massa. A migração do acervo inteiro é gradual, separada do primeiro piloto.

Substituir regras contraditórias somente nos pontos necessários: vínculo exclusivo com E1, reescrita obrigatória induzida por qualquer card, E2/E3 obrigatórias, cotas fixas, autoria permitida apenas por um probe textual igual a zero, dedup por deck e quotas de imagem/palavras. Preservar identidade editorial e bons exemplos existentes.

Piloto: UC03, conteúdo 38, Inflamação aguda. Depois testar uma pequena interseção com conteúdo 37 de Imunologia. Não produzir automaticamente toda Imunologia ou toda UC03. A E1 antiga e transcrição são pontos de partida; verificar o material antes de declarar cobertura ou escolher bibliografia.

Avaliação inicial respeita a preferência do usuário: qualidade dos cards, experiência de revisão e desempenho nas provas da faculdade. Sem provas extras de aprendizagem nem retorno de E2/E3. Registrar correções, objetivos ausentes, cards fora de escopo, redundâncias e tempo; não atribuir causalidade à nota de uma única prova.

Aceite técnico: repetir o comando não cria notas extras; mesma pergunta compartilhada mantém um histórico; originais não mudam; suspensão manual sobrevive; prova de uma aula não pausa card exigido por outra; pacote incremental não reinicia aprendizado; renderização no Android está legível; falhas retomam sem duplicação.

## 19. O que fica para depois

Tutor dentro do Anki, serviços em segundo plano, compartilhamento público, tradução integral, expansão retrospectiva de todas as UCs e recuperação automática de todos os leeches. O mapa longitudinal cresce com as aulas; sua completude total não bloqueia a primeira entrega.

Não contratar uma plataforma de anatomia ou novo banco de questões para viabilizar esta arquitetura. Avaliar uma compra somente se o piloto demonstrar uma lacuna concreta nas fontes já disponíveis. A escolha de Claude/GPT não é uma dependência estrutural: contratos, exemplos e testes permitem trocar o executor, mas desempenho pedagógico precisa ser medido nos próprios materiais.

Esta arquitetura fecha o desenho do sistema. O perfil no Mac, versões dos aplicativos, compatibilidade de modelos/IO, corpus disponível e bibliografia específica são verificações de implantação ainda pendentes, identificadas no roteiro. Nenhuma delas foi simulada como já concluída.
