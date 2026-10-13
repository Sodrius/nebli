# Análise de NEBLI::UC03::P1 — 13/10/2026

Sinais mecânicos para orientar a leitura; o julgamento (cobertura, ordem lógica, princípios antes dos detalhes, complementaridade, peso de ciclo básico, Tabs) é feito lendo `frentes.txt` e registrado abaixo.

| Aula | Notas | verde | azul | rosa | CLIN | NUM | sem Tab | Tab antigo | ESCOPO |
|---|---|---|---|---|---|---|---|---|---|
| 02 02-diagnostico-radiologico | 75 | 25 | 43 | 7 | 6 | 2 | 0 | 75 | não |
| 03 03-diagnostico-patologico | 79 | 15 | 51 | 13 | 3 | 0 | 0 | 79 | não |
| 04 04-radiografia-ultrassom | 81 | 27 | 49 | 5 | 7 | 1 | 0 | 81 | não |
| 05 05-tomografia | 65 | 25 | 37 | 3 | 4 | 6 | 0 | 65 | não |
| 06 radiologia-06-correlacao-1 | 43 | 21 | 15 | 7 | 2 | 1 | 0 | 43 | sim |

## Possíveis repetições (8 pares; similaridade de palavras e resposta em comum)

- 0.71 · 1791844733654 (05-tomografia): [img] This abdominal CT was acquired in the portal phase
  ↔ 1791844733903 (05-tomografia): [img] This abdominal CT was acquired in the late phase
- 0.71 · 1791844733254 (05-tomografia): [img] This abdominal CT was acquired in the arterial phase
  ↔ 1791844733903 (05-tomografia): [img] This abdominal CT was acquired in the late phase
- 0.71 · 1791844733254 (05-tomografia): [img] This abdominal CT was acquired in the arterial phase
  ↔ 1791844733654 (05-tomografia): [img] This abdominal CT was acquired in the portal phase
- 0.67 · 1791844730979 (05-tomografia): [img] This chest CT is displayed in a lung window
  ↔ 1791844731104 (05-tomografia): [img] This chest CT is displayed in a bone window
- 0.67 · 1791810582199 (02-diagnostico-radiologic): On T2 -weighted MRI, fluid appears bright
  ↔ 1791810582322 (02-diagnostico-radiologic): On T1 -weighted MRI, fluid appears dark
- 0.6 · 1791844723178 (05-tomografia): [img] This CT reconstruction is in the sagittal plane
  ↔ 1791844723573 (05-tomografia): [img] This CT reconstruction is in the coronal plane
- 0.57 · 1791810569898 (02-diagnostico-radiologic, 04-radiografia-ultrassom): Ultrasound is fast, dynamic and can be performed at the bedside
  ↔ 1791810584247 (02-diagnostico-radiologic, 04-radiografia-ultrassom): Radiography is fast and can be performed at the bedside
- 0.45 · 1791810351323 (03-diagnostico-patologico): The mechanism by which an etiologic agent causes disease is called pathogenesis
  ↔ 1791810351795 (03-diagnostico-patologico): Many drugs act on the mechanism of disease, that is, on its pathogenesis, rather than on the etiologic agent

## Julgamento (13/10, leitura integral das 403 frentes antes e das 296 depois)

- **Cobertura:** cada aula cobre seu núcleo. 02: o que cada método usa, como forma a imagem, termos de cada método, vantagens/limites, contrastes, planos, fases e janelas em conceito, T1/T2. 03: etiologia → patogênese → morfologia → clínica, áreas da patologia, biópsia/citologia/autópsia, H&E e colorações especiais, IHQ, métodos moleculares. 04: produção do RX, atenuação e densidades, radiação e efeitos, projeção/incidências, magnificação, silhueta, princípios do US (piezoelétrico, eco, impedância, frequência × resolução), termos, sombra e reforço, Doppler. 05: aquisição, voxel, Hounsfield, janelas, fases, artefatos, vantagens. 06: correlação dos dois casos. Nenhum princípio central faltando.
- **Ordem lógica:** 02 (panorama dos métodos) → 03 (panorama da patologia) → 04 (RX e US) → 05 (TC) → 06 (correlação) é progressiva; a 06 usa termos que 02/04 definem (compartilhados). Não foi preciso card-ponte.
- **Peso acima do ciclo básico (o problema relatado por Davi):** 02/04/05 tinham engenharia do equipamento (óleo, chumbo, tungstênio, frenagem, gerações da TC, slip rings, matriz 512, retroprojeção, MIP/MinIP), números (tempos de cada fase, UH de músculo/hemorragia/contraste, 20 tons de cinza, 20.000 Hz), clínica (FAST, estenose ao Doppler, marca-passo, sedação, insuficiência renal) e exemplos (hemangioma, esteatose, osteomielite, colangio-RM, fontanelas, mamografia). 03 tinha estatística de artigo (16%, 50% → 10%, SVOC), técnica de bancada (cassete, pesagem, monobloco) e clínica (core biopsy, ER/PR além da prova).
- **Repetição entre aulas:** lateralidade (04 e 05), “mais atenuação = mais branco” (02 e 05), “TC sem sobreposição” (três vezes na 05), PA “feixe de trás para frente” (02 e 04), ZN em dois cards na 03 (um compartilhado da Micro), FNA de tireoide (autoral e AnKing), resolução de contraste da TC (duas vezes).
- **Detalhes que se complementam:** depois do corte, cada detalhe restante pendura num princípio que vem antes na aula (densidades → radiopaco/radiolucente; eco → hiper/hipoecoico → sombra/reforço; HU → janelas → fases).
- **Tabs:** todos em estilo antigo; regenerados no formato novo (texto corrido do princípio ao card). Amostra lida depois da geração.
- **Correções aplicadas (`nebli.enxuga`):** 02: 12 retiradas + 3 exemplos desassociados (90 → 75); 03: 23 retiradas, 2 devolvidas por serem questão de prova (Papanicolaou 2016 P3; ER/PR 2015 P3) (100 → 79); 04: 30 retiradas, 3 devolvidas (ecocardiograma, item de prova; PA e perfil, texto do bloco de incidências) e 1 repetição desassociada (109 → 81 notas); 05: 44 retiradas + 1 desassociada (110 → 65). Total P1: 403 → 296 notas. Notas retiradas ficam suspensas com `NEBLI::retirado::<motivo>` (comentários preservados).
