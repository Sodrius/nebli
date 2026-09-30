# Imuno P2 UC03 — refazer do zero (pedido de Davi, 30/09) — ESTADO

Pedido: “deletei imuno da p2 e queria que vc gerasse o deck novamente, seguindo o padrão que arrumamos”; “quero decks só, bem completos e cobrindo bem o que há nas provas também (considera as provas da uc03 do drive)”. Prova P2 = 02/10/2026.

Duas aulas: imuno-06 Sistema complemento (08/09) e imuno-07 Inflamação: início e resolução (17/09). Slides relidos no Drive (mod. 07/09, iguais aos anteriores). Provas: 26 (complemento) + 33 (inflamação) questões IM 2015–2025 em `referencias-externas/uc03/provas-questoes.json`; extrato na scratchpad da sessão (refazer com o filtro por chaves se preciso). Buscas AnKing em `busca/`.

## Feito
- `complemento/spec.py` completo (38 AnKing + 12 autorais, cores, excluídos, 2 compartilhados). Falta: build/apply (copiar `deck-aula-uc08-fi05-.../build.py` e `apply.py`, trocar tag de autoral para `NEBLI::author::uc03-imuno31-<key>`, E1 “não aplicável — pedido explícito (só decks)”, somar `extra_tags` às tags).
- Nada instalado no Anki ainda.

## Inflamação — decisões já tomadas (escrever `inflamacao/spec.py`)
Tag da aula: `NEBLI::2026-uc03-imunologia-37-inflamacao-inicio-resolucao`; deck `NEBLI::UC03::P2::Imunologia::Inflamação: início e resolução`.

Verdes (3) / azuis (4), por nid AnKing:
- Sinais: 1487640248028, 1487640253946, 1487640263698, 1487640274492, 1520443529180 {1:4}; 1487640261037 {1,2,3:3}; 1487640269487 {1:3,2:3,3:4}; 1471541327679 {1:4}; 1471541598687 {1:4}; 1487640278577 {1:3,2:3}
- Células/PRR: 1479267358567 {1:3}; 1479267395454 {1:4}; 1487640028986 {1:4,2:3,3:4}; 1487640050564 {1:3}; 1500572039288 {2:4,3:4}; 1520299451730 {1:3}; 1520299562982 {1:4}
- Lipídicos: 1487640059152 {1:3,2:3}; 1487640061733 {1:3}; 1487640068745 {1:3}; 1487640078840 {1:3}; 1487640089158 {1:4,2:4}; 1487640101055 {1:3}; 1487640108934 {1:4}; 1487640120758 {1:4}; 1487640124653 {1:4}; 1488847671701 {1:3,2:3}; 1488847679422 {1:3}; 1488854891621 {1:4}; 1488854922125 {1:4}; 1488854930174 {1:4}; 1488854963588 {1:4}; 1488854967929 {1:4}; 1499356681150 {1:4}; aspirina 1488847688890 {1:3}, 1488847696894 {1:4}, 1473986398130 {1,2,3:4}; corticoide 1463883753623 {1:3}, 1462061188088 {1:4,2:4}; zileuton 1474580819655 {1:4}
- Mastócito: 1487640132837 {1:4}; 1487640136892 {1:4}; 1487207084334 {1:3,2:4}; 1487207091819 {2:4}
- Plasmáticos: 1487640225601 {1:3}; 1487640230861 {1:4,2:3}
- Citocinas/fase aguda: 1489969950421 {1:3}; 1489970022577 {1:4}; 1489970026548 {1:3}; 1489970054827 {1:4}; 1489970091921 {1:4}; 1489970181312 {1:3}; 1489970615786 {1:3}; 1487642795725 {1:3}; 1520444046369 {1:3,2:4}; 1520445108362 {1:3}; 1520445157941 {1:4}; 1520444298927 {1:4}; 1520445172196 {1:4}
- Inflamassoma: 1520715624658 {1:3}; 1520715849479 {1:3}
- Migração: 1487642579270 {1:4,2:4}; 1487642582069 {1:4}; 1487642620769 {1:3,2:3}; 1487642625895 {1:3,2:3}; 1487642632527 {1:4}; 1487642637710 {1:4}
- Fagocitose/burst: 1475890914685 {1:4}; 1487642733736 {1:4,2:4}
- Resolução/desfechos: 1487642784485 {1:3}; 1520715124462 {1:3,2:3}; 1487642801171 {1:4}; 1480563969014 {1:4,2:4}; M1 1520716108281 {1:4,2:4}; M2 1520717070355 {1:4,2:4}

Autorais (inglês) a escrever: TLR por localização (c1 TLR4 azul, c2 TLR5 azul, c3 ácidos nucleicos endossomais verde); NOD-like/RIG-I-like citosólicos (azul; Extra: PRR solúveis/membrana/citosol); Dectin-1–β-glucano (azul; provas fungos 2017/2018); DAMPs → inflamação estéril, ex. infarto (c1 verde, c2 azul; prova P1 2017 2.5); urato → NLRP3 → IL-1β, bloqueio de IL-1 na gota (c1 verde, c2 azul; prova P1 2017 1.6); cinética dos mediadores histamina/bradicinina minutos → PG/LT horas → IL-1/TNF → lipoxinas/resolvinas (verde; prova P2 2025 2.4); lipoxinas/resolvinas pró-resolução (c1 verde, c2 azul); cinética celular 12–48 h, eosinófilos/linfócitos > 72 h (azul); NETs (azul); inflamação neurogênica substância P/CGRP (azul); sequência vascular vasoconstrição transitória → dilatação → permeabilidade venular (c1 azul, c2 verde); eotaxina/PAF × IL-8/LTB4 (azul).

Compartilhados (só tag, sem copiar): as 25 notas que já têm a tag da aula (Inflamação aguda + Patogenicidade) + 1790253141963 (PRR/PAMP), 1790253142871 (marginação), 1790253144373 (NADPH oxidase), 1790253144533 (MPO), 1790253537100 (estase), 1790253537574 (PAF), 1790253537195 (histamina/contração endotelial). Anafilatoxinas e LPS→complemento entram pelo deck de Complemento com `extra_tags`.

Excluídos: mastocitose, Chédiak-Higashi, SIRS, inato × adaptativo (aula P1 imuno-01), IL-2/4/5/12/IFN-γ (P3), ferro/hepcidina/SAA/procalcitonina, LAD tipo 2/herança/dentes/cordão, LTD4/CysLT1/5-HPETE, COX-2 permeabilidade (redundante), lisozima, K+ no burst.

## Depois de instalar
`python3 -m nebli.explicacoes gerar 'deck:"NEBLI::UC03::P2::Imunologia*"'` (explicações do Tab), amostra lida, `python3 arquivos-trabalho/relatorio_decks.py "NEBLI::UC03"` para a tabela final, FEEDBACKS e commit.
