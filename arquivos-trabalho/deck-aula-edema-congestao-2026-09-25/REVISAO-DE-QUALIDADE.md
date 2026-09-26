# REVISAO-DE-QUALIDADE — piloto E1 + cards, Edema e congestão

```text
Aula / run_id / versão: UC03 Patologia 23 · Edema e congestão (27/08/2026) · deck-aula-edema-congestao-2026-09-25 (Claude, 25/09)
  · plan.json sha256 b4732213cee531264db3c8df4d60def1c0fe5b24a567f7d30318ce369664678e · substitui o deck X4 do Codex (24/09)
```

## Fontes consultadas
| Família | Estado | Localizador |
|---|---|---|
| Slide | consultado | Drive `1akEbdwSRKaGC3-6rj2e7XZEsyYHK2yss`, 4.936.174 B, sha256 `ba25e7f2…`; lâminas 1–16 vistas uma a uma (17+ = Patologia ambiental, fora) |
| Provas | consultado | índice UC03 `pat-05-edema-congestao`: 32 subquestões (várias ecos). Pertinentes: 2024 P2 1.2 (edema pulmonar hidrostático pós-IAM → transudato), 2024 P4 2.6 (choque séptico → permeabilidade, não congestão), 2018 P1 1.3/1.6 (derrame hidrostático+oncótico × ascite com PMN), 2019 P1 1.4, 2017 P1 1.7, 2023 P1 1.10, 2025 P2 1.2/1.6 (exsudato, mecanismos de permeabilidade), 2016 P1 2.6 (densidade 1,000 não é exsudato) |
| E1 existente | consultado | Drive `1VKwKWVk11boLAp5lfQcWApHIHYYme7Nl`, etapa 1 lida inteira (14 subtópicos, ~7 mil palavras): usada como fonte, não reaproveitada |
| Livro | **não localizado** | Robbins cap. 4 fora do Drive; substituído por revisões primárias (GUIA.md), só resumos lidos |
| Vídeos | indicados | 4 vídeos, título/canal por oEmbed; Osmosis com legendas lidas em 24/09; nenhum assistido integralmente |
| Step 1 | consultado | AnKing Step: 67 buscas em 11 objetivos → 651 notas, 565 com tag Step 1, 344 lidas após filtro lateral; externos: 22 buscas (MCAT, Histology, LLU, Dope, BlueLink, Dorian, AnatoKing, Ankisthesia) |

**Fontes ausentes e impacto:** sem transcrição (recorte pelo slide + E1 antiga + provas); Robbins não lido — profundidade conferida por revisões primárias. Recorte provavelmente completo; profundidade bibliográfica parcial.

## Matriz alvo → evidência → E1 → recuperação
| Alvo | Evidência | E1 | Card/verso |
|---|---|---|---|
| A1 edema (interstício/serosas; ≠ tumefação celular) | slide 2–3 | 1.1 | verso anasarca; mec-* |
| A2 hiperemia ativa × congestão passiva | slide 2–3 | 1.1 | **hiperemia-congestao** (autoral) |
| A3 hidrotórax, hidropericárdio, ascite, anasarca | slide 2, 6 | 1.3 | **anasarca** (autoral; demais no verso) |
| B forças de Starling; linfa e limiar | slide 4 | 1.2 | linfa-retorna; limiar-edema |
| C1 ↑ hidrostática (TVP local, IC) | slide 5, 8 | 2.1 | mec-hidrostatica |
| C2 ↓ oncótica (perda, ↓síntese) | slide 5, 10 | 2.2 | mec-oncotica |
| C3 retenção de Na primária × secundária | slide 8, 10, 11 | 2.1–2.2, 3.2 | mec-sodio; nefrotica-sodio; ic-sraa |
| C4 obstrução linfática → linfedema | slide 7 | 2.3 | mec-linfatico |
| C5 ↑ permeabilidade → exsudato | slide 5; provas | 2.3 | mec-permeabilidade |
| D transudato × exsudato | provas (várias) | 1.3 | nota compartilhada 1790253536913 (2 cards) |
| E1 IC: círculo do SRAA; esquerda × direita | slide 8 | 2.1 | ic-sraa; ic-esquerda; ic-direita |
| E2 edema pulmonar hemodinâmico | slide 9, 14; prova 2024 | 3.3 | pulm-cardio-vs-nao; **pulm-histologia** (autoral, imagem) |
| E3 nefrótica | slide 10 | 2.2 | nefrotica-sodio; mec-oncotica |
| E4 cirrose: ascite e síndrome hepatorrenal | slide 11–12 | 3.2 | cirrose-ascite |
| E5 SDRA/dano alveolar difuso | slide 13–15; prova 2024 P4 | 3.3 | sdra-interface; sdra-hialina (imagem na frente); sdra-neutrofilos; sdra-fibrose |
| F morfologia: edema, congestão aguda/crônica, células da IC, noz-moscada | slide 3, 9, 12 | 3.1–3.2 | ic-cacifo; ic-celulas; nozmoscada (macro + centrolobular) |

## Revisões
- **Recorte (F-C15):** toda frente aponta para lâmina ou prova. Fora: critérios de Light numéricos, Berlin, SPPARTAS, tratamento, SAAG, encefalopatia, Budd-Chiari, PBE, herniação, angioedema hereditário, glomerulonefrite pós-estreptocócica, carcinoma inflamatório de mama e filariose como cards próprios (exemplos ficam só na E1).
- **Step do mesmo assunto:** entrou só o que aprofunda alvo da aula (células da IC, zona 3, Starling revisado no verso). Excluídos por imprecisão: `1576690099969` (derrames atribuídos à IC direita); por duplicação: `1473707300427`, `1486522767302`, `1576685673761`, `1586119101293`, `1471915047213`, `1474503768203`, `1474503771577`, `1475453437333`, `1577916403894`.
- **Pares mantidos (F-C05):** linfa-retorna × limiar-edema (papel da linfa × limiar; c2 retirado); mec-hidrostatica × ic-cacifo (mecanismo × sinal/distribuição); nozmoscada c1 × c2 (macro × micro, objetivo 4); pulm-cardio × sdra-interface × sdra-hialina (mecanismo × alvo × morfologia). **Limítrofe:** mec-sodio × nefrotica-sodio (mesma resposta, contextos distintos) — reavaliar com uso. Nota compartilhada exsudato/transudato tem 2 clozes espelhados (da Inflamação aguda; não reestruturada agora).
- **Precisão (F-C11):** imagem do card AnKing de noz-moscada era de hepatotoxicidade por paracetamol (arquivo Wikimedia "Fetge. Acetaminofè") → substituída por macro/micro do slide na cópia; Extra de `1532735591750` sem tabela de tratamento e com membrana hialina restrita à SDRA; DIC retirado de `1473707401320`; Extra de `1581191946613` reescrito pela cascata do slide; kwashiorkor não atribuído só à albumina. Na E1, reabsorção venular clássica apresentada como simplificação (Levick & Michel 2010).
- **Autoria (3/24 = 12,5%):** hiperemia-congestao — AnKing só tem hiperemia fisiológica (`1471468263016`, `1471468271265`); externos: 2 hits Lightyear (Doppler transcraniano), 6 de anatomia/anestesia. anasarca — AnKing 2 hits (extra de hidropisia; diagnóstico nefrítico), hydrothorax 3 (hidrotórax hepático, lateral), hydropericardium 0; externos 0. pulm-histologia — 78 hits AnKing "pulmonary edema", nenhum com imagem histológica testada; externos 16 (Lightyear), Histology/LLU 0. Todos em inglês, frente ≤ 20 palavras, imagem do slide com crédito.
- **Retenção:** 23 verdes (21 próprios + 2 compartilhados), 3 azuis (sdra-neutrofilos, sdra-fibrose, anasarca), 0 incertos. Motivo por card em plan.json. Média do lote: não aplicável (piloto de 1 aula).
- **Versos, imagens e nomenclatura:** 24 frentes renderizadas lidas (nenhuma entrega a resposta); 18 imagens de verso presentes na mídia; imagens do slide inspecionadas visualmente antes do uso; apoio PT curto onde o termo muda.

## E1
9 subtópicos, 4.749 palavras de miolo, E1 em 13 páginas (PDF 18), 11 figuras do slide, 10 siglas, 7 termo-notas, 1 confusão prevista, 1 clínica-box, conclusão em 4 camadas, Antes da aula com 972 palavras e 29 termos, Resumindo com 9 seções. `precompile-check --somente-e1` OK (2 avisos de balanço entre subtópicos); `auditar_pdf` OK; σ/π em modo matemático (sem fonte substituta). Revisão visual de todas as páginas: corrigidos um vazio de ~30% (p. 6) e composições com restos de título. Restam: ~60% em branco no fim da PARTE II (quebra de PARTE do template) e cabeçalho "Sumário" na primeira página da E1 (main somente-E1). Revisão didática feita pelo próprio executor, sem revisor independente.

```text
Estado do conteúdo: revisado (executor; Robbins não lido)
Estado técnico: verificado — readback de campos/cards/cores/seleção por tag, fontes AnKing intactas, mídia presente, APKG UC03 verificado
Estado de acesso: Anki local; sync aceito pela API; Mac/Android não conferidos
Pendências que afetam o estudo: nenhuma bloqueante. E1 não publicada no Drive (aguarda autorização); tamanho da E1 segue a trava atual (calibração em outra conversa)
Contabilidade: deck 23 notas / 24 cards (AnKing 20 notas/21 cards; autorais 3) + 1 nota/2 cards compartilhados = 26 acessíveis pela tag.
  Ações: 7 cópias atualizadas, 3 recriadas (contagem de clozes mudou; reps=0), 13 novas; 23 notas / 29 cards antigos removidos (backup: backup-edema-antes-do-piloto.apkg + before-apply.json).
  Verdes 23, azuis 3, incertos 0, vermelho/laranja 0, suspensos 0. APKG local NEBLI-UC03.apkg: 1.161 cards, 0 bandeiras no arquivo, sem upload.
```
