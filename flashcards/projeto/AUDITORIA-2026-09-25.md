# Auditoria do lote e repasse — 25/09/2026

## Conclusão

O formato está próximo do desejado: AnKing predominante, acervos externos realmente usados, mistura de relações e reconhecimento visual, sem exigir autoria generalizada. **Não está validado como coleção completa, núcleo sustentável ou processo sem supervisão.** Os maiores problemas são calibração do núcleo, regressão de feedback, falsos negativos de busca e revisão desigual dos autorais. Não se resolve apagando tudo, incluindo mais conteúdo indiscriminadamente ou trocando apenas o modelo executor.

O pedido inicial era avaliação; durante a análise Davi autorizou "já ajeita o que der". Foram aplicadas correções limitadas, com backup, lock, diário e verificação. O Docs foi relido na versão modificada em 25/09 às 09:29 UTC. Novas decisões: [CALIBRACAO-2026-09-25.md](CALIBRACAO-2026-09-25.md).

## Evidência e limites

- Perfil vivo: Davi. Snapshot inicial com IDs estáveis na coleta: **1.453 cards, 1.115 notas, 23 decks médicos**; UC03 P2 1.088 e UC08 P1 365.
- Campos/HTML e metadados coletados integralmente; análise textual dirigida a autorais, amostras de fontes, duplicações, cores e casos de risco. **Não foi revisão científica individual de todos os 1.453 cards.**
- Inventário integral de origem por `source_nid`, confrontado com os decks-fonte vivos. Leitura de relatórios/planos do lote e fonte docente de Edema diretamente no Drive; não reconferidos todos os materiais docentes, vídeos e capítulos de todas as aulas.
- Quatro imagens abertas nesta rodada (histologia gástrica, cadáver/ceco, placa X-gal, nicho intestinal); HTML da frente conferido em exemplos. Não é inspeção visual integral nem teste no Android/Mac.
- Todos os 1.453 cards iniciais tinham `reps=0`, sem suspensos nem comentários. Isso só descreve este perfil; não demonstra retenção, compreensão, desempenho real ou ausência de estudo em outro contexto.
- Entraram **71 cards de Correlação patológica-radiológica 2 durante outra execução**. A verificação detectou o conjunto diferente, reconciliou os IDs e preservou esse trabalho. Esses novos cards não fazem parte da auditoria semântica inicial.

## Contabilidade inicial corrigida por fonte

| Origem real | Cards |
|---|---:|
| AnKing Step | 1.060 |
| Outros decks | 176 |
| Autorais | 217, de 191 notas |
| Total | 1.453 |

Outros: Dope 59, AnatoKing 53, MCAT 36, Histology 16, LLU 7, Dorian 5. Assim, aproximadamente **85% aproveitados e 15% autorais**. A proporção geral esconde problemas localizados; não é meta de produção.

38 cards externos estavam rotulados como AnKing (33 notas, sobretudo Intestino grosso e Intestinos). O erro vinha da classificação do grupo de seleção, não de ausência dos acervos. As tags foram corrigidas sem modificar fontes. O AnatoKing já está instalado e foi usado: adquirir outro deck não é a prioridade antes de buscar melhor nos existentes. Ankisthesia também está vivo (4.338 cards); isso não torna conteúdo anestésico pertinente a aulas básicas.

O diagnóstico de acervos tinha comparação sensível a maiúsculas: não reconhecia `Referências::Anking Step Deck`. Corrigido para comparação case-insensitive, com teste de regressão. Não prova que todas as buscas antigas falharam; várias selecionaram AnKing diretamente.

## Onde houve avanço

- Vascularização: 96 cards, apenas 1 autoral; fontes externas realmente complementam reconhecimento visual. A dimensão visual explica parte do volume, não autoriza chamar os 96 de núcleo.
- Esôfago/estômago/delgado: 60 cards, 2 autorais; 31 AnatoKing, 12 Dope e 2 Dorian, além de 13 AnKing. Bom exemplo de aproveitar o acervo anatômico.
- Estômago histológico: 35 cards, 2 autorais; roteiro prático e Junqueira documentados como consultados. Reconhecimento e teoria presentes; prova antiga específica ausente e interpretação visual ainda requer avaliação por alvo.
- Operon: MCAT acrescentou 25 cards, demonstrando que external-first está sendo usado. Isso não certifica os 19 autorais restantes.
- Não houve colisão nas identidades `NEBLI::source::nid-*` registradas entre notas do snapshot. `ankihub_id` vazio nas cópias que têm o campo. Essas verificações são boas salvaguardas, não prova de não redundância semântica ou preservação histórica em todas as corridas anteriores.

## Problemas concretos

### 1. Feedback explícito voltou a ser desrespeitado

Intestinos continha a nota `1790271593612`, cobrando Lgr5 e repetindo Ascl2/Olfm4/Bmi1/Hopx/Tert. É o caso rejeitado na Q2. **Excluída nesta rodada**, pois ruim para o recorte aprovado, não candidata a suspensão. Backup APKG anterior preservado. Ainda revisar villin, Ki67/TUNEL e outros detalhes caso a caso: não apagar só por serem moléculas.

### 2. Há autoria evitável e perguntas semanticamente sobrepostas

Em Edema, 15/36 cards eram autorais. Busca viva achou AnKing sobre macrófagos com hemossiderina (`1471914979068`) e fígado em noz-moscada por falência direita (`1471915035278`). Não são necessariamente perguntas com direção idêntica; contudo impedem alegar lacuna de conteúdo sem comparação e possível adaptação.

Em Inflamação início/resolução, o autoral PRR→PAMP (`1790272038297`) sobrepõe o AnKing já em Inflamação aguda (`1790253141963`). O detalhe germline-encoded está na frente, não é o alvo escondido: não basta para justificar automaticamente mais uma recuperação de PAMP. Prioridade: associar a identidade apropriada e verificar irmãos, sem apagar histórico.

### 3. Autorais precisam de revisão de pergunta, não só tamanho

- X-gal (`1790263385937`) dizia "blue product" antes de esconder "blue". Frente corrigida para não entregar a resposta.
- 30 notas autorais do snapshot não tinham imagem nos campos; 15 delas eram todos os autorais de Edema. Nem toda pergunta exige figura, mas morfologia pulmonar/hepática e arranjos flagelares são prioridades visuais claras. Imagens ainda não acrescentadas nesta rodada.
- Autorais de Edema estão em português, divergindo do padrão inglês. Correção de idioma e curadoria desse conjunto permanecem pendentes; não considerar aprovados por serem curtos.
- Estômago tem micrografia pertinente, mas a formulação "large pink cells" permite usar uma pista verbal. Para certificar identificação, conferir se o alvo é visual de fato e se precisa de seta/oclusão. Não fabricar versões redundantes.
- Há comentários meta em versos de Inflamação ("the lecture lists..."). Foi ajustado o Extra da tabela exsudato, retirando a instrução de curadoria; o restante exige limpeza dirigida, distinguindo crédito de imagem de comentário meta.

### 4. Precisão científica não pode ser terceirizada ao slide

A nota de Microbiota (`1790265248472`) afirmava esterilidade das vias aéreas inferiores. Corrigida para comunidades microbianas de baixa biomassa, com apoio sucinto e referência. [Estudo primário de Dickson et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28196961/) demonstra comunidades no trato respiratório inferior saudável, com controles para contaminação.

O Extra da nota TLR (`1790272038619`) dizia "São 11 em humanos". Removida a contagem acessória sem alterar os três alvos. A distinção entre genes/receptores funcionais não cabe numa afirmação solta: trabalhos de modelagem humana excluem TLR11 por interrupções no quadro de leitura ([PLOS ONE, 2012](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0049978)). Não foi feita auditoria científica completa dos demais enunciados.

### 5. As cores não entregam ainda o núcleo que Davi quer

Antes: 365 verdes, 161 rosas e 927 sem bandeira. Os 365 verdes tinham a tag literal HY exigida. Portanto, **a execução da regra antiga de verde estava coerente**, mas essa regra não responde "qual o melhor conjunto de longo prazo para Davi?".

Mesmo suspendendo todos os 161 candidatos, restariam **1.292 cards**: média física de 56 por deck, não até 35. Patogenicidade tinha 107 verdes em 188 cards; conservar todo HY automaticamente já excede muito 35. É um conflito real entre unidade de aula ampla, tag de fonte e orçamento de manutenção — não licença para cortar às cegas.

Prioridade deve avaliar: relação central, reutilização futura, habilidade distinta, cobertura já garantida por outro card, custo de revisão e profundidade adequada ao ciclo básico. HY é evidência, não substitui esse julgamento. Ausência em prova antiga não prova desimportância; sem verde não é low yield. Os **161 rosas foram migrados para azul**, sem fazer nova classificação semântica.

## Carga e o que ainda não se sabe

1.453/35 = aproximadamente **42 dias só para introduzir** o snapshot pelo limite diário, sem novas aulas. UC03 tinha 1.088 cards; UC08, 365. Não eram 2 mil por prova nesse instante; associações por aula podem aumentar somas aparentes sem aumentar o conjunto único.

Não dá para garantir 50 minutos/dia com 35 novos sem dados de uso. Tempo por resposta, erros, reaprendizagem e revisões acumuladas ainda não foram medidos. Se fossem sete aulas por semana com 35 novos únicos de núcleo em cada uma, já seriam 245 por semana: todo o orçamento de introdução de 35/dia, antes de extras. Compartilhamento e aulas menores podem reduzir isso; não prometer que ocorrerá.

Não existe neste relatório contagem certificada de núcleo por aula nem porcentagem de cobertura. Próxima etapa recomendada: proposta de núcleo em 2–3 aulas de tipos distintos, com matriz de cobertura refeita para o núcleo, depois observação de uso. Não impor novos quizzes.

## Botão de estudar a aula

É uma prioridade de usabilidade, não detalhe cosmético: a seleção lógica deve reunir cards pertinentes compartilhados sem exigir que Davi administre suspensões. [Decks filtrados do Anki](https://docs.ankiweb.net/filtered-decks.html) ajudam no treino sem reagendar, mas não puxam cards suspensos/enterrados ou já em outro filtrado. Logo, "todos independentemente do estado" exige solução adicional e teste de restauração/identidade. Não está implementado nem aprovado por esta auditoria.

## Correções realizadas e estado final observado

- Quatro notas com campos corrigidos (X-gal, microbiota respiratória, Extra TLR e Extra da tabela exsudato).
- 33 notas / 38 cards com tag de corpus corrigida; fontes intactas por não serem alvo de escrita.
- 161 flags rosas → azuis; nenhuma suspensão, limitação diária ou classificação global de núcleo alterada.
- 1 nota / 1 card autoral rejeitado excluído, recuperável pelo backup de Intestinos.
- Sincronização AnkiConnect retornou sem erro; chegada aos outros dispositivos não verificada.
- 71 cards de outra execução foram detectados e não modificados.
- Fechamento às 11:10 UTC: **1.523 cards**, sendo 1.452 do conjunto auditado após exclusão + 71 novos não auditados. **392 verdes, 161 azuis, 7 rosas novos, 963 sem bandeira**, zero vermelho/laranja. As sete rosas são do trabalho concorrente, não marcas antigas esquecidas pela migração. Reconciliar com o responsável; não sobrescrever uma sessão em andamento.

Evidências privadas: `arquivos-trabalho/auditoria-lote-2026-09-25/{snapshot.json,metrics.json,verified-origins.json,targeted-source-search.json,before-fixes.json,fix-journal.jsonl,fix-receipt.json}`; backup `backup-intestinos-before-exclusion.apkg`. Não fazer push dos snapshots/conteúdo de decks. Nenhum upload ao Drive, nenhum push ou alteração de configurações/modelo de IA nesta rodada. Pacotes UC antigos são anteriores às correções; não reimportá-los para "atualizar" a coleção.

## Repasse operacional ao Claude

Verificação do código/contexto: 14 testes unitários passaram em `python -m unittest discover -s nebli/tests -v`, incluindo descoberta do AnKing com grafia variável, semântica azul, proibição de mutações no preflight e roteamento dos pontos de entrada à calibração atual. Testes não certificam curadoria. Backup APKG da exclusão teve integridade ZIP conferida.

Ler README → calibração 25/09 → este relatório → v4/contrato/runbook/fila. A próxima sessão não precisa desta conversa, mas precisa desses arquivos e acesso real às fontes/Anki.

Ordem de trabalho: (1) confirmar estado concorrente e pendências, (2) revisar autoria e busca em Edema/Inflamação/Intestinos/Operon, (3) propor núcleo por objetivo, (4) melhorar seleção compartilhada/cram, (5) medir rotina real antes de ampliar confiança. Não apresentar mais documentação como se fosse validação pedagógica. Não há evidência comparativa controlada para declarar Claude ou GPT superior; aprovação do usuário é válida como preferência, não teste de retenção entre modelos.

Perguntas realmente necessárias, com recomendação, para a próxima calibração: verde deve continuar como HY de origem ou passar a núcleo personalizado? E, em aulas muito amplas como Patogenicidade, quais blocos/organismos o material e as provas sustentam como centrais? Não repetir as 30 perguntas já respondidas.
