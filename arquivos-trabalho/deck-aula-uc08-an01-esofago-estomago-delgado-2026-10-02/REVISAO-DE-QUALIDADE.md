# Revisão de qualidade — Esôfago, estômago e intestino delgado (UC08 P1, Anatomia)

> **Versão 2, depois do feedback de Davi (F-20261002-CLAUDE-09), mesma data. Estado vivo: 112 notas / 125 cards — 34 verdes, 81 azuis, 10 rosas. Origem dos cards: slide da aula 43, AnKing 35, BlueLink 18, autoral 17 (14%), Dope 6, Dorian 5, AnatoKing 1.** O texto abaixo descreve a versão 1 (89 cards); o que mudou:
> - **Cobertura item a item** (`cobertura.json`, 92 itens: roteiro prático, 12 questões, atividade prática II e cada slide): todo item de roteiro e exercício tem card; 9 itens de slide excluídos com motivo (faringe, funções, biografia, bibliografia…).
> - **43 oclusões feitas do próprio slide** (`nebli/slide_io.py`): porções do esôfago, três constrições, hiatos, ligamento frenoesofágico, linha Z, cárdia, fundo, corpo, antro, piloro, incisuras, curvaturas, canal pilórico, canal gástrico, pregas, quatro porções do duodeno, flexura duodenojejunal, ligamento de Treitz, colédoco, ducto pancreático, papilas maior e menor, artérias jejunais e ileais, vasos retos longos e curtos, seis regiões abdominais. Rótulos da imagem em português (são os da professora); nome em inglês no verso. Todas as prévias vistas (`visual/io-folha1–5.png`); títulos e legendas que entregavam a resposta foram mascarados.
> - **7 identificações AnatoKing retiradas** (nunca estudadas), substituídas pelas oclusões do slide; ficou só a parte pilórica.
> - **Ordem estrita dos slides**: entradas reordenadas pelo slide, sem recuo; tag `an01-NN` e posição na fila de novos regravadas (`update2.py`). `nebli.ordem verificar` sem problema.
> - **Netter conferido**: pranchas 237, 239, 276–279 vistas (`visual/netter.png`); terminologia bate com os cards. Não fiz oclusão das pranchas do Netter nesta aula; `slide_io` aceita PDF com rótulos em texto, então é viável nas próximas.
> - **Tab** 125/125; o gerador passou a ler o alvo das oclusões (nome em negrito no verso) e das pranchas numeradas.
> - **Gate**: `python3 -m nebli.gates` 18 de 18, incluindo os dois gates novos (ordem estrita, cobertura item a item).
> - Não visto na tela do Anki: a renderização das oclusões novas e a coluna “Ordem da aula”.

**Run:** `uc08-an01-20261002a` (Claude, 02/10/2026), primeira aula da campanha de regeneração (só decks, sem E1). Deck `NEBLI::UC08::P1::Anatomia::Esôfago, estômago e intestino delgado`. Critérios: MEMORY + FEEDBACKS até F-20261002-CLAUDE-08. Sem revisão de outra IA. O deck de 29/09 tinha sido apagado por Davi; nada foi restaurado.

## Fontes
| Família | Estado | O que foi feito |
|---|---|---|
| Slides | consultada | `fontes/slides.pdf` (Drive pessoal, pasta da aula), 24 páginas com 2 lâminas cada; texto extraído e **todas as páginas vistas** (`visual/folha1–6.png`). Cópia idêntica em texto no drive da turma |
| Exercícios | consultada | 12 questões orientadoras e roteiro prático de 7 itens, lidos. O PDF “Prática de Anatomia I” é um e-mail de gabarito sem o conteúdo. A apostila da monitoria só tem histologia e fisiologia |
| Provas antigas UC08 | **não localizada** | Pasta de provas do Drive só tem UC01, UC02, UC03 e UC21; drive da turma sem provas; CAOC inacessível |
| CAOC arquivos | **inacessível** | Conector do Drive ainda como dpbdes@gmail.com (404 na pasta); pasta fora da montagem FMUSP |
| Livro | consultada | **Moore**, cap. 5, pp. 714–742 do PDF (esôfago abdominal, estômago, duodeno, jejuno e íleo), lido inteiro; origem: Bibliografia Básica do drive da turma. É o livro que a professora lista no slide 24. Quadro 5.8 (jejuno × íleo) é imagem e não foi lido. Netter (atlas) não aberto: as pranchas da aula estão nos slides |
| Canais | consultada | Transcrição lida inteira: Dr Matt & Dr Mike (esôfago, estômago, duodeno, jejuno e íleo) e Armando Hasudungan (esôfago). Medicosis (estômago): só o início, não usado. Ninja Nerd não tem aula de anatomia macroscópica destes órgãos; Osmosis sem transcrição disponível |
| Acervos | consultada | AnKing: 46 consultas (`busca/anking.txt`, `busca/complemento.txt`); externos: 27 consultas (`busca/ext.txt`), antes de qualquer autoral |

Conferência posterior: a atividade prática com gabarito da turma (“Prática de Anatomia II”, lida depois da instalação) cobra desta aula as três constrições do esôfago, a papila maior do duodeno, a cárdia, o canal gástrico e o vaso reto longo do jejuno; os cinco alvos têm card (`constricoes`, `papila-maior-bl`, `cardia-ak`, `canal-gastrico`, `vasos-retos-jejuno`/`arcadas-dope`).

Q020: a falta de prova antiga e do CAOC não foi tratada como bloqueio porque slides, exercícios da professora e livro do curso foram lidos; fica como pendência declarada.

## Percurso da aula e cobertura (ordem dos slides; “Slide N” = página do PDF)
| Slide | Conteúdo | Cobertura |
|---|---|---|
| 1–2 | Título, objetivos, definição do sistema digestório | sem card (objetivos guiaram a seleção) |
| 3–4 | Esôfago: tubo de 23–25 cm; músculo estriado/liso; cricofaríngeo = esfíncter superior; faringe | comprimento (rosa), terços, cricofaríngeo na prancha, função do esfíncter superior, Zenker. Faringe e véu palatino fora |
| 5 | Porções e três estreitamentos | 3 porções (identificação), relação com a traqueia, constrições |
| 6–8 | Porção abdominal, hiatos do diafragma, ligamento frenoesofágico, linha Z, Chagas, figura de Mittal | T8/T10/T12, pilar direito, esfíncter inferior, ligamento, linha Z, megaesôfago chagásico e mecanismo |
| 9 | Caso do tumor de esôfago | perfuração instrumental e constrições |
| 9–12 | Estômago: forma, partes, incisuras, curvaturas, interior, músculos, funções | cárdia, fundo, corpo, parte pilórica, antro, canal, piloro e esfíncter, incisuras cárdica e angular, curvaturas, pregas, canal gástrico, camada oblíqua. Funções (quimo, reservatório) fora |
| 13 | Caso da úlcera perfurada; exercício 9 | úlcera na curvatura menor, relações anterior e posterior |
| 14–17 | Regiões abdominais; duodeno: 4 porções com níveis, forma de C, Treitz, papilas, ampola | 4 porções, níveis L1/L3, cabeça do pâncreas, AMS × aorta, papila maior e menor, ductos, Oddi, Treitz (estrutura e importância). Nove regiões e biografia de Treitz fora |
| 17–21 | Jejuno e íleo: 2/5 e 3/5, mesentério, início e fim, quadrantes, vasos, tabela | fração, mesentério, identificação, junção ileocecal, quadrantes, vasos retos e arcadas, gordura, parede e calibre, pregas |
| 22 | Divertículos do íleo (Meckel) | 4 notas |
| 23 | Caso de isquemia mesentérica | cobrado pelos cards de vasos retos |

Excluídos com motivo (40 notas lidas e recusadas) e fora do recorte: `plan.json`.

## Seleção e bandeiras (Anki vivo, 02/10)
**76 notas / 89 cards: 34 verdes, 48 azuis, 7 rosas.** Origem dos cards: AnKing 35, BlueLink 18, AnatoKing 8, Dope 6, Dorian 5, **autoral 17 (19%)**. Nenhum compartilhado: é a primeira aula instalada depois do reset.

- **Verde (exemplos):** terços do esôfago, esfíncter inferior, constrições (arco aórtico, hiato), T8/T10/T12, linha Z, acalasia por Chagas, cárdia/fundo/corpo/antro, curvaturas, piloro, incisura angular, camada oblíqua, úlcera na curvatura menor, 1ª e 2ª porções do duodeno, cabeça do pâncreas, ampola e papila maior, Treitz como marco, vasos retos do jejuno, Meckel. Critério: estrutura ou relação que volta em cirurgia, endoscopia, imagem e patologia.
- **Azul (exemplos):** identificações do roteiro prático, ligamento frenoesofágico, pilar direito, incisura cárdica, canal gástrico, relações do estômago (exercício 9), nível L1, estrutura do Treitz, 2/5, quadrantes, parede do jejuno.
- **Rosa:** comprimento do esôfago, L3, úlcera posterior e a. esplênica, síndrome da AMS, cálculo na ampola, ducto acessório, pregas circulares na peça.
- **HY × verde:** as 14 notas AnKing com tag HY 1 ou 2 têm pelo menos um card verde (checagem no `build.py`).
- **Casos limítrofes:** Zenker (HY 1) entrou como a clínica do cricofaríngeo, também tratada no vídeo do Armando; estenose do piloro, hérnia de hiato, DRGE e H. pylori ficaram fora (doenças que a aula não ensina); ligamentos peritoneais e SAID PUCKER ficam para AN13; irrigação para AN07.
- **Carga:** 34 verdes únicos; a 40 novos por dia a aula entra em pouco mais de dois dias.

## Ordem
`nebli.ordem verificar`: ok, 76 notas com `NEBLI::ordem::an01-NN`. Cinco recuos de um slide, mantidos de propósito: o caso do slide 9 fica junto das constrições do slide 5; pilar direito (figura do slide 8) antes do esfíncter e do ligamento do slide 7; curvaturas (slide 10) depois do piloro; ductos do slide 16 depois da peça do slide 17; Treitz (slides 15–16) fechando o duodeno.

## Autorais: método e teste cego
16 notas, cada uma com 2 espelhos AnKing e a lacuna registrada em `busca`. Lint: 0 reprovações duras. Conferidos contra Moore (pp. 714–737) e slides.

- **Rodada 1** (`card-mirror/`, 16 autorais + 16 AnKing da aula, juiz cego): 13/16 autorais identificados, 0 AnKing confundido (acurácia 0,91). Pistas sustentadas: frentes sem nenhum negrito, `jejuno-fracao` entregava a resposta pelo complemento, `chagas-neuronios` com alvo genérico, `jejuno-parede` binário sem dica.
- **Correções:** negrito nos termos-chave como nos espelhos; `jejuno-fracao` sem a metade do íleo (foi para o Extra); Chagas passou a ocultar o plexo mioentérico; dica `thicker / thinner`.
- **Rodada 2** (`card-mirror-v2/`, juiz novo, 16 AnKing diferentes): 10/16 no limiar 0,5, todos entre 0,50 e 0,70 (acurácia 0,81); o juiz declarou sinal fraco e confusão entre tema (anatomia descritiva) e estilo. Não é indistinguível: frases de definição com Extra vazio ainda se agrupam. A aprovação que vale é a de Davi estudando.
- O juiz apontou um crédito de imagem restante (`coledoco-pancreatico`); retirado antes de instalar.

## Imagens
Todas as figuras dos 89 cards foram renderizadas e vistas (`visual/midia01–10.png`, `visual/webp-folha1–3.png`), BlueLink com a máscara de resposta. Sem imagem errada. Limites: as fotos de cadáver do AnatoKing têm números pequenos (o modelo com marcação vermelha é a figura legível); a figura do card das constrições tem rabiscos azuis do autor original. Não vi os cards na tela do Anki, só as mídias. Créditos visíveis retirados em 32 notas; origem preservada no plano.

## Instalação
Lock `escrita`, snapshot `before.json`, diário `journal.jsonl`, `receipt.json` com 89/89 cards, bandeiras e tags conferidas, `problems: []`. Três tipos de nota novos (`… independente - v2`), clones dos v1 com `NEBLI_Comentario`, porque os v1 não tinham o campo. Preset NEBLI: 200 → **40 novos por dia**. Pacote `NEBLI-UC08.apkg` (sem bandeiras, em inglês; tradução para português não feita).

## Não feito
Provas antigas e CAOC não consultados; Tab duplo (curto + longo), heatmap da meta e pesquisa do analista de retenção não implementados (só o Tab no formato atual); cards não conferidos na tela nem no tablet; sync entre aparelhos não verificado.


## Correção F-20261003-CLAUDE-18 (03/10)

estomago-posterior: F-18: cloze encurtado para 'omental bursa' (gate de 3 palavras); 'lesser sac' foi para o verso para não dar a resposta por sinônimo.
