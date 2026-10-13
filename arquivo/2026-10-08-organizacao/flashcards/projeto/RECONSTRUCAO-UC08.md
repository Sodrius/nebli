# UC08 — fila e fontes da reconstrução

> **02/10/2026:** Davi apagou todos os decks médicos NEBLI para refazer do zero. Os estados “instalado” abaixo são históricos. Fila ativa: **UC08 P1 → UC03 P2, somente decks, sem E1, entregues aula por aula** (F-20261002-CODEX-09/10). UC03 P3, UC19 P1 e UC08 P2 são backlog, fora deste ciclo. Método: CLAUDE.md + `python3 -m nebli.gates`.

Atualizado em 29/09/2026 após respostas e esclarecimentos. Documento de **estado**, sem política paralela. Preferências no [MEMORY](../../MEMORY.md), procedimento em [EXECUCAO-DECK-AULA](EXECUCAO-DECK-AULA.md), retorno de ambos os executores em [FEEDBACKS](FEEDBACKS.md).

## Próxima sessão Claude

**Planejamento de 02/10:** regeneração após reset aguarda sessão própria de execução; arquitetura no roteiro §9, pesquisa/heatmap no ANALISTA-RETENCAO e evolução do Tab no guia existente. Os parágrafos e inventários de 29/09 abaixo são históricos quando conflitarem com o reset e o pedido atual. Não repetir exclusão.

Pedido vigente: **Claude entrega primeiro UC08 P1, depois UC03 P2; só decks, sem E1 neste ciclo**. Entregar cada aula completa após revisão, sem aguardar toda a campanha. Seguir bibliografia e recorte conforme MEMORY; roteiro operacional em EXECUCAO-DECK-AULA, seção 9. Não reabrir briefing geral.

UC08 P1 inclui AN01, AN02, BT03, BT04, AN07, FI08 e FI09, a reconciliar com as fontes atuais. Motilidade é P1; secreções FI05/FI06 são P2 e não entram neste pedido. UC03 continua referência de qualidade. Davi já apagou os decks médicos: não repetir reset nem restaurar pacotes/scripts antigos. Reconciliar o perfil vivo antes de instalar novas seleções e preservar qualquer estudo iniciado desde o reset.

**Andamento da campanha (Claude, 02/10):**

| Aula | Estado |
|---|---|
| AN01 Esôfago, estômago e delgado | **Instalada e entregue em 02/10**, run `uc08-an01-20261002a`: v3 após F-20261002-CLAUDE-09/10: 112 notas / 123 cards (oclusões do próprio slide 45, AnKing 35, BlueLink 18, autoral 17, Dorian 5, Dope 2 de texto, AnatoKing 1; 34 verdes, 78 azuis, 11 rosas), ordem estrita, `cobertura.json` com 92 itens, Netter conferido, gate 22/22, ordem `an01-NN`, pasta `arquivos-trabalho/deck-aula-uc08-an01-esofago-estomago-delgado-2026-10-02/`. Livro lido: Moore cap. 5 (drive da turma). Provas antigas e CAOC não consultados |
| AN02 Intestino grosso e canal anal | **Instalada e entregue em 02/10**, run `uc08-an02-20261002a`: v2 após F-20261002-CLAUDE-11: 96 notas / 105 cards (oclusões do slide e Netter 39, AnKing 32, autoral 21, BlueLink 9, Dorian 4; 37 verdes, 53 azuis, 15 rosas) + 2 notas da AN01 associadas; planejamento, cobertura (80 itens) e revisão final gravados; gate 22/22; pasta `arquivos-trabalho/deck-aula-uc08-an02-intestino-grosso-canal-anal-2026-10-02/` |
| BT03 Estrutura do estômago | **Instalada e entregue em 02/10**, run `uc08-bt03-20261002a`: 78 notas / 90 cards (AnKing 37, oclusão do slide 26, Histology reescrito 12, autoral 10, MCAT 3, LLU 2; 29 verdes, 46 azuis, 15 rosas) + 1 nota da AN01; Junqueira cap. 15 e apostila da monitoria lidos; gate 24/24; pasta `arquivos-trabalho/deck-aula-uc08-bt03-estrutura-estomago-2026-10-02/` |
| BT04 Intestinos | **Instalada e entregue em 02/10**, run `uc08-bt04-20261002a`: 52 notas / 55 cards (AnKing 20, autoral 12, oclusão do slide 10, Histology reescrito 6, LLU 5, MCAT 2; 20 verdes, 28 azuis, 7 rosas) + 2 notas associadas; gate 24/24; pasta `arquivos-trabalho/deck-aula-uc08-bt04-intestinos-2026-10-02/` |
| AN07 Vascularização das vísceras | **Instalada e entregue em 02/10**, run `uc08-an07-20261002a`: 109 notas / 122 cards (oclusão do slide 61, AnKing 46, autoral 13, Dorian 2; 45 verdes, 64 azuis, 13 rosas) + 8 notas associadas; gate 24/24 |
| Correções de 03/10 (F-20261003-CLAUDE-13) | AN01, AN02 e AN07: oclusões refeitas por rótulo inteiro nas notas vivas, busca registrada, seções do Moore na cobertura. BT03 v2 (115 cards) e BT04 v2 (79 cards): teoria do Junqueira pelo deck Histology, menos oclusões e autorais. Estado em PLANO-GERACAO-ANO |
| FI08 Motilidade I | **Instalada e entregue em 03/10**, run `uc08-fi08-20261003a`: 34 notas / 40 cards (AnKing 29, Histology 4, autoral 7; 24 verdes, 13 azuis, 3 rosas) + 11 notas associadas de BT03, AN01 e AN02; Aires cap. 59–60; gate 26/26 |
| FI09 Motilidade II | **Instalada e entregue em 03/10**, run `uc08-fi09-20261003a`: 49 notas / 59 cards (AnKing 45, autoral 14; 24 verdes, 31 azuis, 4 rosas) + 7 notas associadas; Aires cap. 60 |
| P2 | FI05 refeita (102 cards) e FI06 Secreção gástrica (57 cards) entregues em 03/10; AN11, AN13, AN14, BC10 e FI12 sem material no Drive |

Fontes novas para as próximas aulas: drive da turma na conta FMUSP (slides, exercícios, práticas e Bibliografia Básica), ver ACERVOS-REFERENCIA. As pastas de Fisiologia desse drive estavam vazias em 02/10; os slides de FI08/FI09 estão no Drive pessoal. Preset NEBLI em 40 novos/dia desde 02/10. Tipos de nota `… independente - v2` (Anatomy, Image Occlusion Enhanced+, AnatoKing) criados com `NEBLI_Comentario`; usar estes, não os v1.

Marcar aula/run_id/pasta ao começar trabalho autorizado e atualizar resultado/pendências ao terminar. Esta preparação de memória não inicia a próxima aula e não opera o Anki.

## Inventário conferido em 29/09

Drive docente: [UC08](https://drive.google.com/drive/folders/1iZf8WWtcjNqJtcQLkZcOFQ5qmdrxaWMR). Foram listadas as quatro pastas de componentes e as 14 pastas de aula. “Slide localizado” abaixo significa metadados/listagem, não leitura integral ou conferência visual. O texto de FI08 foi lido pelo conector como teste de acesso; renderização e leitura científica ainda pertencem à execução.

Calendário: [planilha 2026](https://docs.google.com/spreadsheets/d/1T1RZ_vpqtchmdM8U2BXYmlHk7e-Ov-iCGM51PFIEqMU/edit), aba **Mês**, faixas A1:S65 e A66:G78, consultadas em 29/09: P1 em **05/10**, P2 em **30/11**, Turma B. Datas não definem orçamento de cards.

**Conflito identificado:** `Matérias!AB1:AI22` ainda marca FI05/FI06 como P1 e FI08/FI09 como P2. A instrução explícita de Davi, de 24/09 e reafirmada em 29/09, prevalece: **motilidade P1; secreções P2**. Não alteramos a planilha. Não inferir prova apenas da data anterior a 05/10 nem do número no nome do PDF.

### P1 — sete aulas com slides localizados

| ID | Aula / data B | Pasta Drive | Material observado | Estado da reconstrução |
|---|---|---|---|---|
| AN01 | Esôfago, estômago e delgado · 03/08 | [01](https://drive.google.com/drive/folders/1sg4WMtpGzA3LhdZg9M8sXXM0MJkP0llG) | Slides + roteiro + 12 questões; E1 histórica | **Instalado 29/09 pelo Claude; sem revisão Codex** — run `uc08-an01-20260929a`, **59 notas/70 cards (AnKing 26, BlueLink 18, AnatoKing 8, Dope 8, Dorian 5 cards; 5 autorais; 27 verdes/43 azuis) + 7 notas FI08/BT03 associadas por tag**, inglês; pasta `arquivos-trabalho/deck-aula-uc08-an01-esofago-estomago-delgado-2026-09-29/` (REVISAO-DE-QUALIDADE.md). Prova não localizada; Netter do Drive inacessível (pranchas via slides + substitutos abertos) |
| AN02 | Intestino grosso e canal anal · 10/08 | [02](https://drive.google.com/drive/folders/1GATNLKY4BG7oR-iCUBtWpuKXjkRA03Pi) | Slides + roteiro 7–10 + perguntas 1–3 | **Instalado 29/09 pelo Claude; sem revisão Codex** — run `uc08-an02-20260929a`, **59 notas/76 cards (AnKing 31, BlueLink 24, Dorian 1, autorais 20 cards/9 notas; 36 verdes/40 azuis) + Chagas FI08 associado**, inglês; pasta `arquivos-trabalho/deck-aula-uc08-an02-intestino-grosso-canal-anal-2026-09-29/` |
| BT03 | Estrutura do estômago · 17/08 | [03](https://drive.google.com/drive/folders/1ujdOnueUeBz9uVGzmBRFwCLSX08a_rCG) | Slides; extra na pasta-pai BT; E1 histórica | **Instalado 29/09 segundo Claude; sem revisão integral Codex** — run `uc08-bt03-20260929a`, **v3 após F-C44: 37 notas/49 cards (19 AnKing, 13 Histology, 2 LLU, 3 autorais; 19 verdes/30 azuis)**; pasta `arquivos-trabalho/deck-aula-uc08-bt03-estrutura-estomago-2026-09-29/`. Registro histórico do primeiro par |
| BT04 | Intestinos · 24/08 | [04](https://drive.google.com/drive/folders/1GSN_lBnaYQh4d1zdMUjQfYnWeXVFs5vd) | Slides (36 lâminas) + roteiro BT | **Instalado 29/09 pelo Claude; sem revisão Codex** — run `uc08-bt04-20260929a`, **29 notas/37 cards (AnKing 14, Histology 12, LLU 5, autorais 6 cards/3 notas; 13 verdes/24 azuis) + 11 notas associadas (BT03 8, UC03 2, AN01 1)**, inglês; F-C02 aplicado; pasta `arquivos-trabalho/deck-aula-uc08-bt04-intestinos-2026-09-29/` |
| AN07 | Vascularização das vísceras · 11/09 | [07](https://drive.google.com/drive/folders/1anr09zp44SG100cQsQ-4jMVk6b0rcM2W) | Slides + roteiro 11–14 + questões 1–12 | **Instalado 29/09 pelo Claude; sem revisão Codex** — run `uc08-an07-20260929a`, **48 notas/76 cards (AnKing 49, Dope 17, autorais 10 cards/5 notas; 36 verdes/40 azuis) + 11 associadas (AN01 4, AN02 6, UC03 1)**, inglês; pasta `arquivos-trabalho/deck-aula-uc08-an07-vascularizacao-visceras-2026-09-29/` |
| FI08 | Motilidade e absorção intestinal I · 14/09 | [08](https://drive.google.com/drive/folders/1sDVPs-kjaAw7VFzYHZkiLfU3Ozm_rXxb) | `Aula-1_MED_2026.pdf`; texto acessado | **Instalado 29/09 segundo Claude; sem revisão integral Codex** — run `uc08-fi08-20260929a`, **v3 após F-C44: 37 notas/47 cards (29 AnKing, 1 Histology, 7 autorais; 22 verdes/25 azuis)**, PT-BR; pasta `arquivos-trabalho/deck-aula-uc08-fi08-motilidade-i-2026-09-29/` (REVISAO-DE-QUALIDADE.md). Margarida inacessível na sessão; prova não localizada |
| FI09 | Motilidade e absorção intestinal II · 28/09 | [09](https://drive.google.com/drive/folders/1fdb4ci7o_gRURac8DVZFEfc_9FeSKiFk) | `Aula-2_MED_2026.pdf` (15 lâminas) | **Instalado 29/09 pelo Claude; sem revisão Codex** — run `uc08-fi09-20260929a`, **33 notas/47 cards (AnKing 33, autorais 14 cards/7 notas; 19 verdes/28 azuis) + 11 associadas (FI08 7, BT03 1, AN02 3)**, inglês; sem conteúdo de absorção no slide; pasta `arquivos-trabalho/deck-aula-uc08-fi09-motilidade-ii-2026-09-29/` |

### P2 — sete aulas, sem misturar com a P1

| ID | Aula / data B na planilha | Pasta Drive | Material observado | Estado da reconstrução |
|---|---|---|---|---|
| FI05 | Esôfago e estômago: secreções e digestão · 24/08 | [05](https://drive.google.com/drive/folders/1dLEyYNKkmu8TMsdKcYrlEboKAOu3yIxp) | `Aula-3_MED_2026.pdf` = “Digestão e absorção dos nutrientes” (12 lâminas) | **Refeito do zero em 02/10 pelo Claude (piloto E1 + deck); o deck de 29/09 foi apagado por Davi** — run `uc08-fi05-20261002a`, **94 notas/108 cards (AnKing 76, autoral 32; 38 verdes/57 azuis/13 rosas) + 9 associadas**, inglês, ordem `fi05-NN`, E1 em PDF local; pasta `arquivos-trabalho/deck-aula-uc08-fi05-digestao-absorcao-2026-10-02/` (REVISAO-DE-QUALIDADE.md). Aires não consultado; prova não localizada. **Aula de secreções continua sem material** |
| FI06 | Intestino: secreções e digestão · 31/08 | [06](https://drive.google.com/drive/folders/1qgRJjxVc1bWaCqw4AnsdWK83Wji-sVN_) | Pasta vazia nesta consulta | Aguardar material; procurar também em FI05 |
| BC10 | Fígado e pâncreas — embrio · 19/10 | [10](https://drive.google.com/drive/folders/1TJmcKg6jftonBaEJY7cggHnlQKCYFNG-) | Pasta vazia nesta consulta | Aguardar material |
| AN11 | Fígado, pâncreas e vias biliares · 26/10 | [11](https://drive.google.com/drive/folders/1g2MAvaZlq8SuvTr1DPSDYtxlM5BVz2bp) | Pasta vazia nesta consulta | Aguardar material |
| FI12 | Função hepatobiliar e metabolismo · 09/11 | [12](https://drive.google.com/drive/folders/1WAJMD5RO1AbxclEVOvEGHOAArZd9PkGb) | Pasta vazia nesta consulta | Aguardar material |
| AN13 | Cavidade abdominal e peritônio · 16/11 | [13](https://drive.google.com/drive/folders/1OWV6s-dry8hV4a_HoRYNyKWA0Y9eYh84) | Pasta vazia nesta consulta | Aguardar material |
| AN14 | Inervação do digestório · 23/11 | [14](https://drive.google.com/drive/folders/1YLZmqgZVGJmXNNe58tSt2oLSK0VJhH72) | Pasta vazia nesta consulta | Aguardar material |

Introdução e estudo livre não viram decks artificiais. Títulos amplos não provam conteúdo: “absorção” no nome de FI08/FI09 só recebe cards se o material efetivo sustentar. A classificação P2 de secreções não retira automaticamente de BT03 uma relação célula–função ensinada em histologia, nem de FI09 um efeito motor de hormônio: classificar **alvos**, evitando importar o bloco secretório.

Provas UC08: não localizadas nas buscas desta sessão. Foram listadas as pastas [Provas pessoal](https://drive.google.com/drive/folders/1ZgyavSCg72ZBFpg7dmGr8K-WBYVHPd_C), [Provas compartilhada](https://drive.google.com/drive/folders/1_lkx8ryVqnub5Fs65zeC4Ij3ly21Xo4F) e [provas antigas](https://drive.google.com/drive/folders/1eReSnbZUkmIGxTOuITIvAHctxRapU992), sem ramo UC08; busca por nomes de prova com UC08/UC 8/Digest também vazia. Isso não prova inexistência em todo o Drive. Na execução, ampliar por UC8/Med5043/nomes dos temas e registrar a busca; não pedir download manual. Avaliar o impacto conforme Q020 no MEMORY: falta de fonte importante impede instalar; não presumir que toda ausência de prova seja indispensável ou irrelevante. Preparação independente pode continuar.

## Histórico da fila anterior ao reset

Ordem inicialmente proposta: FI08 e BT03 (já executadas), depois AN01 → AN02 → BT04 → AN07 → FI09 — **P1 concluída em 29/09**; FI05 (digestão/absorção) instalada na P2. P2: FI05 → FI06 → BC10 → AN11 → FI12 → AN13 → AN14 conforme fontes disponíveis. O pedido atual de Davi define o trabalho; esta lista não é agendamento automático nem novo tamanho de lote. A sequência de estudo pretendida segue o professor, com o agendador atual preservado.

Reconsultar Drive ao retomar: pasta vazia em 29/09 não prova que continua vazia. Um PDF que cubra duas aulas precisa de páginas/alvos segmentados; não duplicar o conjunto. Biblioteca e modelos em [ACERVOS-REFERENCIA](ACERVOS-REFERENCIA.md). A fila antiga UC03 P2/UC08 P1 foi arquivada integralmente no [histórico](HISTORICO.md); a divisão antiga por matéria não rege este ciclo.

## Evidência conhecida e limites

FI08: `arquivos-trabalho/deck-aula-uc08-fi08-motilidade-i-2026-09-29/`; BT03: `arquivos-trabalho/deck-aula-uc08-bt03-estrutura-estomago-2026-09-29/`. Corridas receberam v3/v3c segundo Claude após F-C44; 47/49 cards também foram observados numa consulta pontual anterior aos nomes dos decks. Essas evidências **não são auditoria integral de conteúdo, imagens ou tradução**. Reabrir recibos/versão viva quando houver execução; não interpretar aprovação parcial de autoria como certificação do conjunto.

F-C44 e F-20260929-CLAUDE-01 registram a insuficiência de cobertura/cortes de irmãos e o pedido de calibrar pela aula, sem devolver a decisão de quantidade/verdes ao estudante. Incorporar às próximas entregas junto das 99 respostas consolidadas; correção de FI08/BT03, se solicitada, é incremental nas mesmas identidades. Fonte indispensável ausente continua sendo pendência do deck existente, sem disparar modificação retroativa durante organização da memória.

Referência do primeiro briefing FI08: [Aula-1_MED_2026.pdf](https://drive.google.com/file/d/1kUUqmssC4UrxI1EzmbjeqNu7wyyMkR9R/view). Texto consultado indicava inervação/plexos, reflexos, contração/relaxamento, esfíncteres e Chagas como exemplo do mecanismo. Não autoriza importar diagnóstico/tratamento nem absorção ausente do PDF. Capítulo de Margarida precisa de consulta efetiva, não só presença no Drive.

A preparação inicial Codex teve preflight bloqueado pelo sandbox; registro em `arquivos-trabalho/reconstrucao-uc08-2026-09-29/preflight-planejamento.json`. Isso antecede as instalações relatadas pelo Claude e não descreve o Anki atual. Nesta consolidação documental não se repetiu leitura viva nem escrita Anki/Drive. Não presumir sync entre aparelhos ou instalação de automação a partir destes documentos.
