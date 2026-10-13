# Revisão de qualidade — Intestino grosso e canal anal (UC08 P1, Anatomia)

> **Versão 2, depois do feedback de Davi (F-20261002-CLAUDE-11). Estado vivo: 95 notas / 104 cards + 2 notas da AN01 associadas — 37 verdes, 52 azuis, 15 rosas; autoral 20 cards (19%).** Saíram as 6 oclusões da legenda numerada do slide 2. Entraram 8 cards de texto de reto e canal anal (comprimento do reto, três pregas, função da ampola, relação com a vagina, junção anorretal, válvulas anais, seios e muco, vasos das colunas) e a fissura anal do AnKing. Os 8 autorais novos não passaram por teste cego. Tab regenerado com a regra de definir a condição clínica com nome em português. O texto abaixo descreve a versão 1.

**Run:** `uc08-an02-20261002a` (Claude, 02/10/2026). Deck `NEBLI::UC08::P1::Anatomia::Intestino grosso e canal anal`. Critérios: MEMORY + FEEDBACKS até F-20261002-CLAUDE-10. Ciclo: planejar (`planejamento.json`, escrito antes do spec) → fazer → revisar (`cobertura.json`, `revisao-final.json`) → relatório. Sem revisão de outra IA.

## Fontes
| Família | Estado | O que foi feito |
|---|---|---|
| Slides | consultada | 27 páginas (2 lâminas cada), todas vistas (`visual/folha1–7.png`) |
| Exercícios | consultada | 3 casos com perguntas orientadoras, roteiro prático (itens 7–10) e atividade prática II com gabarito |
| Livro | consultada | Moore cap. 5 (pp. 742–753) inteiro; cap. 6, trechos de reto e canal anal. Netter pranchas 281–283, 373, 375, 376 vistas |
| Canais | consultada | Dr Matt & Dr Mike (integral); Medicosis e Armando ×2 (trechos de anatomia) |
| Material de veterano | não localizada | busca no Drive pessoal sem resultado para esta aula |
| Provas antigas | não localizada | sem pasta da UC08 |
| CAOC | inacessível | conector ainda responde como dpbdes@gmail.com (404); montagem usp.br vazia |
| Acervos | consultada | AnKing 18 consultas, externos 13 (`busca/`) antes de autorar |

## Deck (Anki vivo)
**92 notas novas / 100 cards + 2 notas da AN01 associadas (3 cards): 36 verdes, 51 azuis, 13 rosas nos novos.** Origem dos cards: slide da aula 41, Netter 4, AnKing 30, autoral 12 (12%), BlueLink 9, Dorian 4. Sem Dope, sem AnatoKing.

- **Verde:** partes do colo na peça, mobilidade, três características, apêndice, tênias = músculo longitudinal e convergência no apêndice, McBurney, divertículos, Crohn × colite, ampola retal, puborretal, linha pectinada e todo o bloco acima/abaixo (artéria, veia, linfa, inervação, hemorroidas), tipo muscular dos dois esfíncteres.
- **Azul:** identificações do roteiro (legenda numerada, flexuras, haustros, tênias pelo nome, papila e lábios, flexuras do reto, escavações, colunas, seios, plexos), relações (baço, próstata), McBurney e espinha ilíaca, posição retrocecal.
- **Rosa:** ureter atrás do mesocolo sigmoide, óstio do apêndice, íleo distal, linha branca, escavação vesicouterina, segundas identificações em peça.
- **Bloco da linha pectinada:** 13 verdes porque são todos HY 1–2 no AnKing e o slide 23 escreve as quatro diferenças; é o núcleo duradouro da aula.
- **Fora:** irrigação (AN07), peritônio e omento (AN13), defecação (FI09), patologia de Crohn/colite/fístula, regiões abdominais (já na AN01), atlas com rótulos dentro da figura.

## Autorais e teste cego
12 autorais com 2 espelhos e lacuna registrada; lint sem reprovação dura. Rodada 1: 11/12 identificados (acurácia 0,96), nenhum erro científico; pistas: justificativas embutidas (“because…”, “so it is…”), pares gêmeos, Extra vazio, puborretal com três fatos. Correções: frases sem justificativa embutida, pergunta direta no esfíncter externo, dica de cloze, puborretal com um fato e o resto no Extra, figura do slide no Extra de 5 cards. Rodada 2 (juiz novo, 12 AnKing diferentes): 10/12 no limiar 0,5, com probabilidades entre 0,55 e 0,75 (acurácia 0,92). **Continuam distinguíveis**; o juiz atribui a diferença sobretudo a frases de anatomia descritiva, tema raro no AnKing.

## Revisão final
`revisao-final.json` (11 checagens com evidência) e `cobertura.json` (80 itens). Ordem: `nebli.ordem verificar` ok. Tab: 103/103. Instalação: `receipt.json` 100/100, `problems: []`; delta dos autorais em `journal.jsonl`.

## Não feito
Provas antigas, CAOC e material de veterano não consultados (não localizados ou sem acesso). Cards e coluna de ordem não vistos na tela do Anki. As três oclusões corrigidas depois das prévias não foram reabertas. Tab duplo, heatmap e analista continuam pendentes. Pacote em inglês.


## Correção F-20261003-CLAUDE-17/18 (03/10, outra sessão)

Teto de autorais 15% e nova busca no AnKing e nos externos por autoral (consultas no FEEDBACKS F-18). Substituídos por recortes do Histology/Junqueira, com as figuras do Moore já escolhidas: apendice-linfoide, tenias-longitudinal, esfincter-interno, esfincter-externo (estudado: antigo suspenso com NEBLI::substituido::delta). Passaram ao verso de vizinhos, por serem detalhe sem card nos acervos: ponto de McBurney (→ apendicite-mcburney, AnKing HY), comprimento do reto (→ pregas-tres), vasos das colunas anais (→ arteria-acima). Ficou o ureter atrás do mesocolo sigmoide (único card de texto do slide 10). Cloze da escavação de Douglas encurtado para “rectouterine pouch” (gate de 3 palavras). Resultado: 102 cards, autoral 15 (14,7%).
