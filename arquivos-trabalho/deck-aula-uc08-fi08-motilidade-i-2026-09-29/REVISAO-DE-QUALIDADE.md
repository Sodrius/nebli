# Revisão de qualidade — FI08 Motilidade I (UC08 P1)

**Aula / run_id / versão:** FI08 · `uc08-fi08-20260929a` · seleção v2, `selection_hash 35af34ac5699f23f` (v1 `38078f4d85ee462e` instalada primeiro; v2 alterou só as notas `varicosidades` e `no-relaxa`). Critérios: README/CONTRATO/BANDEIRAS/ESTILO-ANKING/TRADUCAO de 29/09 e RECONSTRUCAO-UC08 v1. E1: não aplicável (pedido de 29/09).

**Fontes consultadas:** slide `Aula-1_MED_2026.pdf`, 6 lâminas, com texto lido e todas as lâminas vistas; FI09 lida só para delimitar a fronteira; OpenStax A&P 2e 10.8 e 23.1; figuras Berne & Levy (lâmina 4) e Cole & Welsh 2011 (lâmina 6); da Silveira 2007 (resumo); AnKing Step (Costanzo GI 01–03, busca por alvo); lista de nids de Davi "cards UC08" usada como pista. Detalhes em `fontes.json`.
**Fontes ausentes e impacto:** prova UC08 **não localizada** (buscas no `fontes.json`), então não há calibração por prova. Margarida **inacessível** nesta sessão (conector vazio, download acima de 10 MB recusado, extensão Chrome não conectada); substitutos abertos cobriram os mecanismos. NCBI/StatPearls bloqueado por reCAPTCHA.

## Alvos → cards
Matriz completa em `matriz-objetivos.tsv`, na ordem das lâminas 2 → 6. Cada alvo ensinado tem recuperação ativa ou verso. A lista "outros neuromediadores" é ilustrativa: só o NO virou card. "Absorção" do título não existe no PDF, portanto não gerou cards.

- **Recorte:** a aula é motilidade/inervação/músculo liso. Chagas entra só com o mecanismo do slide, sem diagnóstico nem tratamento. O plexo submucoso aparece só como função, e o bloco secretório fica na P2. Piloro (regulação antral/duodenal), relaxamento receptivo, deglutição e ondas lentas ficam para a FI09 (exclusões nomeadas em `plan.json › excluidos`).
- **Step do mesmo assunto:** 16 AnKing (Costanzo GI/FA). Excluídos: vias anatômicas da inervação (AN14, P2), farmacologia (atropina, M3–Gq), clínica lateral (acalasia primária, Lightyear dor→íleo).
- **Mecanismos/contrastes:** mioentérico×submucoso, curto×longo, ACh×VIP/NO, fásica×tônica, MLCK×MLCP, calmodulina (músculo liso) × troponina (verso com a figura AnKing).
- **Excessos e redundância:** 20 candidatos excluídos com motivo. Pares mantidos com respostas diferentes: plexos, reflexos, VIP/NO (transmissores distintos) e fásica/tônica. Irmãos triviais foram desfeitos: calmodulina c2/c4, MLCK c2, MLCP c2 e varicosidades c2–c4.

## Autoria (5 de 22 notas)
| Autoral | Lacuna e buscas | Recusados |
|---|---|---|
| sna-divisoes | AnKing: sympathetic/parasympathetic + GI/motility/peristalsis; decrease/inhibit motility. Externos MCAT/Histology/Lightyear | Vias anatômicas, atropina, listas MCAT, dor→íleo |
| reflexo-curto | "short reflex", "local reflex", intramural, "peristaltic reflex" (AnKing + externos): 0 pertinentes | — |
| ach-excitatorio | acetylcholine/cholinergic + motility/peristalsis/GI smooth muscle | Atropina e tratamento de íleo (laterais) |
| chagas-plexo | Chagas/cruzi + plexus/ganglion/neurons: 0 no AnKing | 1403046909909 e 1509815200893 não cobram o plexo |
| rho-cinase | Rho/RhoA/ROCK/CPI-17/Gq + smooth muscle (AnKing, MCAT, Histology) | Gq genérico de farmacologia |

Todos seguem o mesmo formato: frente focal, verso de 1–2 frases causais, sem mnemônico inventado. Chagas reutiliza a ilustração AnKing de acalasia (ensina a perda de neurônios inibitórios), e a radiografia em "bico de pássaro" foi recusada por ser clínica lateral.

## Retenção
13 verdes, 10 azuis, 0 brancos (motivo por card em `plan.json`). Núcleo: esôfago estriado/liso, autonomia do SNE, função dos plexos, direção do SNA, reflexo curto × longo, ACh × VIP, Chagas → plexo mioentérico, contração tônica dos esfíncteres, MLCK e MLCP. Azuis: localização do plexo, sinapse extrínseca, NO, fásica, funções do EES/EEI (dedutíveis), varicosidades, calmodulina/tipo L (calmodulina já visível na frente do MLCK) e Rho-cinase.
Conferência de lacunas: nenhum alvo ensinado sem card/verso. Conferência de excesso: MLCK e MLCP são enzimas opostas e ficam verdes; calmodulina foi rebaixada por estar coberta pela frente do MLCK.

## Tradução, versos, imagens
PT-BR aplicado na criação das cópias. O inglês original fica arquivado em `translation-plan.json` (`en_base`). Foram preservados HTML, negrito, sublinhado, itálico, `sup/sub`, números de cloze (c3 do card de calmodulina continua c3), dicas `fosforila/desfosforila` e o mnemônico em inglês Kinase/PHosphatase (com glosa em PT). Os campos Sketchy/Bootcamp foram esvaziados na cópia (F-C07). Alterações didáticas estão registradas por card: `didatico`/`curadoria`.
As imagens foram inspecionadas: esôfago estriado/liso, diagrama SNE/SNA, camadas da parede, estriado × liso (AnKing), acalasia (AnkiHub) e figura da junção neuroefetora do slide (267×335, legível, exibida a 400 px). A figura Junqueira 10-20 do card Histology foi trocada porque não mostrava varicosidades.
A renderização (WebKit/qlmanage, 820 px e amostra de 390 px) cobriu frente e verso das 23. Achados corrigidos na v2: tags sobrepostas no template Histology nunca usado (nota passou ao modelo NEBLI AnKing v3, mesmo card ID), dica "pl." e sigla EEI sem expansão no card do NO. O renderizador Swift de 28/09 não compila mais (toolchain × SDK do macOS 27).

## Seleção, identidade, instalação
Deck `NEBLI::UC08::P1::Fisiologia::Motilidade e absorção intestinal I`, no preset da raiz NEBLI. 22 notas novas / 23 cards, sem nenhum compartilhado vivo (o ramo UC08 foi apagado por Davi: preflight com 1.173 cards médicos, todos UC03). Originais AnKing/Histology intocados; `ankihub_id` vazio nas cópias. Tags: aula, origem, objetivo, `NEBLI::ordem::fi08-NN` (sequência docente) e `source::nid`/`author`. O readback (campos, tags, ordinais, flags, deck, suspensão) está em `receipt.json` com `problems: []`. O primeiro `apply.py` parou no readback porque o AnkiConnect não suporta `getSpecificValueOfCard`; as escritas já tinham sido feitas corretamente, e o readback foi refeito por `cardsInfo.flags`. O script foi corrigido.

**Estado do conteúdo:** revisado pelo executor; **aguarda revisão Codex**. Parcial quanto ao livro do curso (não lido).
**Estado técnico:** verificado (readback por ID).
**Estado de acesso:** Anki local Mac User 1. Sync pedido pelo `escrita()` ao fim da v2, aceito sem erro; chegada ao tablet não verificada. APKG não gerado (a UC ainda está em reconstrução).
**Pendências que afetam o estudo:** nenhuma de precisão conhecida. Falta a leitura do capítulo do Margarida para confirmar a profundidade.
**Contabilidade:** 22 notas, 23 cards únicos novos, 0 reutilizados/compartilhados. Origens: 16 AnKing (17 cards), 1 Histology, 5 autorais. 13 verdes, 10 azuis, 0 incertos, 0 marcas pessoais, 0 suspensos.


---

## v3 — correção após F-C44 (29/09, mesma corrida; `selection_hash` em plan.json)

Davi: "ficaram mts poucos cards, não cobriu a aula toda. alguns cards gigantes autorais e fora do padrão… gostava mais dos decks de antes". Comparação com o snapshot de 28/09: FI08 antiga tinha 33 cards e a v2 tinha 23. **v3: 37 notas / 47 cards (29 AnKing, 1 Histology, 7 autorais), 22 verdes e 25 azuis.** As mesmas identidades foram atualizadas; nenhum card tinha revisões.

**Como cada decisão segue o padrão de Davi**

| Critério de Davi | Decisão concreta nesta aula |
|---|---|
| Todos os AnKing do assunto (Q1, 23/09); não desfazer irmãos em massa (F-C44) | Clozes reativados: calmodulina c2/c4, MLCK c2, MLCP c2. Voltaram 2/3 lisos, localização do Meissner, VIP parassimpático, vago/pélvicos, 5-HT/IPANs, GMPc, M3–Gq, α1 contrai esfíncteres, cards de Chagas (c1/c3) e acalasia (EEI e NO/VIP) e esvaziamento por gordura/H⁺. Irmão excluído: Chagas c2 (cardiomiopatia, outra aula). |
| Cobrir a aula inteira (lâminas 2–6) | Acrescentados o piloro (lâmina 4: regulação duodenal retrógrada e antral anterógrada), "distensão relaxa o esfíncter" (título da lâmina 4), exceção simpática nos esfíncteres e a via Gq (lâmina 6). |
| Calibrar com vídeos dos canais (Q5/Q6) | Legendas lidas: Ninja Nerd, Enteric Nervous System (36 min), cobrindo plexos, reflexo peristáltico ascendente/descendente (ACh/SP × VIP/NO), simpático inibe e contrai esfíncteres, parassimpático pelo núcleo motor dorsal do vago, reflexos curto × longo × enterogástrico. Ninja Nerd, Smooth Muscle, e Medicosis, MLCK/fosfatase, cobrindo calmodulina, MLCK, MLCP/GMPc, varicosidades e corpos densos. O recorte do deck coincide com o do vídeo nos temas do slide. |
| Outros acervos antes de autoria (Q10) | Histology (varicosidades) e buscas em MCAT/Histology/Lightyear registradas por lacuna em `plan.json` (`lacuna`). |
| Autoral AnKing-like, curto, com imagem AnKing (F-C04/F-C22/F-C36) | Teste cego com `card-mirror`: os 7 autorais foram detectados. Motivos: frente com mecanismo, verso em prosa e metáfora. Reescritos em frase factual de 10–17 palavras com cloze no termo-chave; verso em fragmentos com a imagem AnKing (diagrama SNE/SNA, acalasia, estriado × liso, regiões do estômago). O verso de dois AnKing (tônica, vagovagal) também foi encurtado. |
| Verde = manter a longo prazo, com motivo por card | 22 verdes nos fundamentos: plexos (posição/função), SNE, direção do SNA, exceção dos esfíncteres, reflexo curto/longo, ACh/VIP/NO, distensão→esfíncter, Chagas/acalasia pelo mecanismo, fásica/tônica, EEI, calmodulina/MLCK/MLCP. Detalhes acessórios em azul. |
| Bibliografia em toda aula | Margarida inacessível: o conector devolve vazio e o arquivo passa do limite de download. Substitutos: OpenStax 10.8/23.1 e figuras do Berne & Levy e do Cole & Welsh no slide. Limite declarado. |

**Pendências:** revisão independente da tradução (agente revisor) em andamento/aplicada abaixo; revisão Codex.


**Tradução — revisão independente (agente revisor, 29/09):** 74 cards EN × PT comparados; fluidez 8/10, fidelidade 9/10. Aplicados na v3c: pistas removidas da frente (mucosas superficiais/do colo, fossetas pilóricas, dente, língua); decalques corrigidos ("infecção protozoária" → protozoose, "estômago oxíntico" → região oxíntica, "sulcos" → depressões, "pontes em trava" → mecanismo de trava); absolutos atenuados (cárdia/piloro "poucas ou nenhuma" parietal; reflexos longos "p. ex." vagovagais); REG no lugar de RER; mnemônico cinase/fosfatase adaptado ao PT (C→Contrai, F→Flácido) em vez de glosa; "parede do tubo digestório" padronizado. Sync e readback limpos após as correções; render conferido.
