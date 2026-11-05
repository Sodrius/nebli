# Retomada UC07 — 04/11/2026

Git atualizado por `git pull --ff-only`: `main` já estava em `a6eb814`. Alterações locais anteriores foram preservadas.

## Aulas e transcrições locais

Pasta real: `Aulas UC07/` dentro do repositório; a pasta de mesmo nome em Downloads contém apenas `.DS_Store`. Os vídeos já estavam baixados. Não houve novo download.

Whisper executado nas cinco aulas pendentes com `mlx-community/whisper-large-v3-turbo`, português, modelo em cache e execução offline. O acesso à GPU Metal exigiu execução fora do sandbox. As quatro transcrições anteriores foram preservadas. Resultado: nove vídeos com TXT, SRT, VTT, TSV e JSON; cinco novas transcrições, correspondentes a 206,2 minutos de gravação.

| Vídeo | Aula do cronograma | Duração | Situação |
|---|---|---:|---|
| MSP2061 - 01 - Topografia do Tronco Cerebral (1) | 03 | 26.9 min | transcrição anterior preservada |
| MSP2061 - 02 - Topografia do Nervos Cranianos (1) | 04 | 20.8 min | transcrição anterior preservada |
| MSP2061 - 03 - Topografia do Cerebelo (1) | 05 | 12.5 min | transcrição anterior preservada |
| MSP2061 - 04 - Topografia da Medula Espinhal (2) | 02 | 104.2 min | transcrição anterior preservada |
| MSP2061 - 05 - Topografia do Diencéfalo | 06 | 70.6 min | nova transcrição |
| MSP2061 - 06 - Topografia do Telencéfalo | 07 | 57.5 min | nova transcrição |
| MSP2061 - 13 - Meninges, ventrículos e líquor | 10 | 31.2 min | nova transcrição |
| UC7 - 03 - Irrigação do Encéfalo | 08 | 19.2 min | nova transcrição |
| UC7 - 04 - Demonstração Prática Neuroanatomia (1) | prática transversal; conferir alvos por aula | 27.8 min | nova transcrição |

O manifesto registra SHA-256, duração, modelo, idioma, destinos e estado por arquivo. Os cinco resultados novos têm texto/segmentos não vazios; os últimos timestamps ficam a menos de um segundo do fim dos vídeos. Foram lidos trechos de início/fim, sem revisão integral do áudio ou do conteúdo. Isso verifica a execução, não a fidelidade de cada termo. Exemplos que exigem revisão: “dia encéfalo” no fim do diencéfalo e “pacmeninge” na abertura de meninges. Não corrigir o bruto silenciosamente: derivar texto revisado com apoio nos slides/livro e manter a versão Whisper.

Para retomar o lote: `python3 arquivos-trabalho/uc07-retomada-2026-11-04/transcrever.py --transcrever`. Sem a opção, apenas atualiza o inventário. Saídas completas são reaproveitadas. Vídeos e transcrições integrais continuam locais/ignorados pelo Git.

## Ponto de partida do Anki

Consulta somente leitura pelos IDs dos decks, pois os nomes vivos incluem contagens. Encontrados 604 cards em 13 decks; 31 suspensos. Nenhuma nota, bandeira, suspensão, tag, agendamento ou tela foi alterada. Os números não demonstram cobertura de conteúdo.

| Aula existente | Cards | Suspensos |
|---|---:|---:|
| 01 Construção morfofuncional do sistema nervoso | 28 | 8 |
| 02 Medula espinal, plexos e nervos | 120 | 6 |
| 03 Tronco encefálico | 104 | 8 |
| 04 Nervos cranianos | 103 | 0 |
| 05 Cerebelo | 55 | 9 |
| 06 Diencéfalo | 21 | 0 |
| 07 Núcleos da base e telencéfalo | 89 | 0 |
| 08 Irrigação do SNC | 24 | 0 |
| 09 Sistemas neurovegetativos | 20 | 0 |
| 10 Meninges e líquor | 15 | 0 |
| 11 Cortes seriados do SNC | 8 | 0 |
| 12 Sistema límbico | 4 | 0 |
| 13 Organização do córtex cerebral | 13 | 0 |

## Cronograma conferido e lacunas do inventário

Fonte: `/Users/davisousa/Downloads/Programa final MSP2061 TB.pdf`, uma página, texto integral lido nesta sessão. Prova em **02/12/2026**. O cronograma pede conceitos morfofuncionais e nomenclatura anatômica vigente. Os 13 decks existentes preservam seus nomes e IDs enquanto planejamos; não renumerar nem reorganizar agora.

- 13/10: construção morfofuncional; **comunicação celular e arco reflexo** (conteúdo próprio no cronograma, sem deck dedicado na árvore UC07 consultada). Há texto de slides de comunicação celular no inventário local de 22/10; cobertura real ainda precisa ser confrontada.
- 14/10: medula/plexos/nervos, tronco, nervos cranianos e cerebelo: quatro vídeos já transcritos; decks refeitos no histórico de 22/10, sujeitos à reconciliação com as demais fontes.
- 21/10 e 11/11: práticas; a demonstração prática recém-transcrita é transversal e deve ser ligada aos alvos de cada aula, sem duplicar identificação.
- 27/10: diencéfalo, núcleos da base/telencéfalo e irrigação: três transcrições novas, respectivamente para os decks 06, 07 e 08.
- 03/11: sistemas neurovegetativos; não foi localizado vídeo correspondente entre os nove arquivos locais.
- 04/11: meninges/líquor (nova transcrição para 10) e cortes seriados (sem vídeo local identificado).
- 18/11: sistema límbico e organização do córtex; sem vídeos próprios identificados neste lote. Não presumir que telencéfalo substitui integralmente essas aulas.
- 25/11: **neuroimagem** e **neuroimagem integrada à neuroanatomia/neurofisiologia**; sem decks dedicados na árvore consultada. Há textos locais intitulados “Aula 1 Gerson” e “Aula 2 Gerson / Neuroimagem integrada”; cabe conferir o conteúdo e a data antes de decidir destino.

## Planejamento a fechar com Davi, antes da geração pelo Claude

1. Reconciliar as fontes por aula: apostila guia e veteranos, questões de provas/gabaritos, bibliografia e transcrição. Não confundir “arquivo localizado” com material lido. Questões de prova ainda não foram inventariadas nesta retomada.
2. Produzir o mapa recuperável de cada aula com fonte/página/timestamp, alvo, operação (identificar, situar, organizar, explicar função, associar lesão), prioridade, card vivo/candidato e lacuna. Dar prioridade operacional às aulas 06, 07, 08 e 10, que ganharam transcrições; a organização final continua na ordem do cronograma.
3. Manter as três bandeiras de prioridade e acrescentar, como proposta, uma classificação por evidência em etiquetas: pilar, cobrança em prova, conteúdo dos materiais e aprofundamento selecionado. Essas classes podem coexistir; frequência em prova só será atribuída após ler e contar questões independentes. Não usar vermelho/laranja pessoais nem ciano da referência externa.
4. Cada bloco deve combinar identificação Kenhub quando visual, AnKing para relações/função/clínica e organizador quando houver conjunto, trajeto ou contraste a recuperar. Fisiopatologia da UC07 continua por acervo. Não criar quota de organizadores nem ficha clínica por estrutura.
5. Apresentar a composição e o custo por aula com exemplos reais e poucos extras justificados antes de o Claude gerar. Nenhum novo card foi escrito nesta retomada.

## Ajustes da sessão anterior

- Skill `pos-prova` e procedimento já constam no projeto; revisão de prova específica não iniciada. Propostas nessa rota continuam exigindo aprovação antes da escrita no Anki.
- Estudo temporário de suspensos: executados novamente os **dois testes** de `test_study_suspensions.py`, ambos passam (retorno/reinício e proteção durante revisão). Validação na interface, após apagar um filtrado e recalcular FSRS, continua pendente. Nenhum filtrado pessoal foi manipulado para testar.
- Farmacologia/UC19 segue reivindicada pelo Claude; esta sessão não alterou lotes, fontes ou cards. O plano de 04/11 continua pedindo confrontar materiais novos com os três lotes existentes.
- `./kenhub-deck --painel` executado: teste dos gates ok, 51 unidades registradas. Isso não substitui auditoria das aulas.

## Continuação em 05/11

Proposta concreta em `flashcards/projeto/PROPOSTA-UC07-COBERTURA-2026-11-05.md`; matriz de40 relações em `matriz-cobertura.tsv`, 14 candidatos destacados em `candidatos-propostos.tsv` e limitações em `fontes-e-limites.md`. Davi confirmou que ainda não tem provas antigas. O inventário vivo usa nomes canônicos sem contagens. Nenhuma escrita no Anki.
