# Revisão de qualidade — X3

**Aula:** UC08 AN 01, esôfago, estômago e intestino delgado. **Run:** 2026-09-24, Codex. **Escopo:** slides de 24 páginas + roteiro prático e 12 questões orientadoras. **Seleção:** `plan.json`, 51 notas novas/60 cards novos; uma nota de X1 associada por tag, logo 61 cards na visão lógica desta aula.

## Seis fontes

| Fonte exigida | Estado e uso |
|---|---|
| Prova | **Não localizada:** `banco/` local e buscas UC08 P1/MED5043/Provas no Drive; pastas Provas encontradas continham UC01–03/UC21, sem UC08. Não usei frequência de prova como evidência. |
| Slide | **Consultado:** slides da professora Patricia Castelucci, páginas 2–24, com objetivos e casos usados apenas para relações anatômicas. |
| E1 anterior | **Consultada:** seções sobre três constrições, regiões do estômago, papila/Treitz e contraste jejuno–íleo. Não foi criado E1/guia. |
| Livro | **Consultado:** Netter, *Atlas of Human Anatomy*, pranchas 237–239 (constrições e junção esofagogástrica), 276–279 (estômago, duodeno, intestino delgado) e 294 (arcadas/vasos retos). Rótulos e legendas textuais do atlas; não alego leitura de capítulo narrativo. |
| YouTube | **Consultados título, descrição e legendas automáticas:** Armando Hasudungan, [Digestive System Anatomy](https://www.youtube.com/watch?v=1-m3z_d531E&t=200s), 03:20–03:50 para corpo, fundo e piloro. A fala simplifica indevidamente a chegada inicial do alimento ao fundo; a ordem anatômica foi conferida pelo slide/Netter. Imagens do vídeo não foram inspecionadas e ele não introduziu perguntas. |
| Step 1 | **Consultado:** AnKing Step vivo, buscas em inglês por esôfago, regiões gástricas, duodeno, Treitz, jejuno/íleo, papila e termos vizinhos; 12 notas/13 clozes aproveitados. Detalhes patológicos laterais recusados. |

Links e localizadores completos em `source-manifest.json`; recorte em `MAPA-ESCOPO.md`.

## Matriz de recuperação

| Alvo | Pergunta ou imagem que o aluno recebe | Situação |
|---|---|---|
| Porções, constrições e músculos do esôfago | AnatoKing cervical/torácico/hiato, autoral abdominal, Dorian adaptado à tríade da aula, AnKing esfíncteres/T10/estriado–liso e Dope muscular | Recuperação textual e visual. A cópia do AnKing foi corrigida para “distal third”; o terço médio misto fica no Extra. |
| Regiões/curvaturas do estômago | 14 imagens AnatoKing e três perguntas AnKing sobre relações ligamentares | Cárdia, fundo, corpo, região pilórica, incisura angular e curvaturas identificáveis. |
| Relações gástricas | Dope de estômago refletido com pâncreas/baço e autoral da parede posterior; AnKing hepatogástrico, gastrocolic e gastrosplenic | Posterior é explícita; anterior aparece na relação com fígado do card hepatogástrico e na prancha Netter 276. |
| Quatro porções do duodeno/papila/Treitz | AnatoKing visual, AnKing colédoco/ducto pancreático/papila/Treitz | Pergunta e imagem presentes; conteúdo de secreção fica fora. |
| Jejuno versus íleo e transição ileocecal | AnatoKing visual, Dope pregas/gordura e prancha de arcadas/vasos retos, nota de X1 associada | Comparação de pregas, arcadas e vasos; a pergunta de vasos retos longos não foi duplicada. |

## Curadoria, repetição e limites

- **Identidade:** 49 notas copiadas de fontes, duas autorais. Antes de criar, consulta por tag de identidade em todo o NEBLI vivo. Uma nota já existente, `1790247520212` (Dope `1461962333435`, jejuno e vasos retos longos), recebeu a tag desta aula; conserva deck X1, histórico, bandeira e agendamento. Não houve outra pergunta física repetida com a mesma identidade.
- **Entre fontes:** AnatoKing testa identificação visual de estruturas cujas relações o AnKing/Dope testam em texto; essas repetições têm recuperação diferente. Ramos arteriais gástricos presentes na X1 ficaram na X1, porque não são foco da AN 01. A formulação Dorian com quatro pontos foi agrupada em três níveis, conforme slide e Netter 237; a origem não foi editada.
- **Autoria:** 2/60 cards (3,3%). Ambos curtos, com contexto e imagem existente pertinente: porção abdominal após T10; pâncreas atrás do estômago por meio da bolsa omental. As imagens foram inspecionadas. Nenhum comentário de curadoria ou vídeo foi posto nos cards.
- **Rosas:** 8 cards novos, ativos. Sinalizam nível T10 isolado, variantes visuais da região pilórica/incisura e dois visuais de pregas. As funções centrais dos esfíncteres foram retiradas de rosa após revisão. São detalhes ensinados de menor valor para manutenção, não matéria externa. Nenhum verde novo: nenhum dos 13 cards AnKing selecionados possuía a tag HY literal exigida.
- **Exclusões:** refluxo/Barrett, câncer esofágico, investigação de disfagia, tratamento de úlcera, motilidade/secreção e histologia específica de X5/X9. Os três casos docentes não viraram decks de doença.
- **Lacunas:** prova antiga específica não localizada; vídeo consultado por legenda automática, sem inspeção das imagens. Isso limita a calibração por prova e a comparação visual com o vídeo, mas os objetivos formais estão cobertos por slides, roteiro, E1, atlas e perguntas verificadas.

## Verificação técnica

`verification.json`: perfil Davi; 51 notas/60 cards; 8 rosas, 0 verdes, 0 suspensos, 0 falhas; 49 notas fonte preservadas. As 31 primeiras imagens visuais escolhidas foram examinadas em `contact-sheet.jpg`; 94 mídias das notas AnatoKing candidatas verificadas como presentes e três pranchas Dope relevantes inspecionadas. `receipt.json` e `journal.jsonl` registram cada identidade. A primeira tentativa parou depois dos 12 AnKing porque o modelo AnatoKing requer Header preenchido; o plano foi corrigido e as 39 restantes foram instaladas sem duplicar os 12. A revisão final corrigiu duas marcações rosa indevidas e sincronizou novamente.

AnkiConnect `sync` concluiu três vezes (`sync-initial.json`, `sync-after-preset.json`, `sync-after-pink-correction.json`); o deck passou para o preset NEBLI, com 35 novos/dia preservados. Isso confirma solicitação de sincronização deste perfil, não inspeção de Mac/Android.

`NEBLI-UC08.publication-ready.json`: pacote local único da UC, 156 cards físicos (96 X1 + 60 X3), 70 mídias, 17.400.626 bytes, ZIP DEFLATE nível 9, IDs/campos/agendamento e mídia conferidos. Zero flags no APKG; 49 flags retiradas só da cópia, coleção viva intacta. Nenhum upload ao Drive, conforme decisão vigente.

**Estado do conteúdo:** revisado para o recorte disponível; parcial quanto à prova específica e à inspeção visual do vídeo. **Estado técnico:** verificado no perfil Windows e no APKG. **Acesso:** Anki local instalado e sincronização solicitada com sucesso; outros dispositivos não inspecionados.
