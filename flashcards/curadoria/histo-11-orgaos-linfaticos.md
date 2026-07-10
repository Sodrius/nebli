# Curadoria AnKing — histo-11-orgaos-linfaticos

**Status: AVALIAÇÃO DE BUSCA/COBERTURA — NÃO APLICADO AO DECK** (pedido de Davi 2026-07-07: "roda o pipeline até achar os cards certos, só pra ter uma noção de como está, mas não coloca no deck ainda, pra aprimorar a busca/completude"). Nenhum card foi dessuspendido nem marcado `NEBLI::`.

## Fonte da busca

- Checklist-alvo: `arquivos-trabalho/checklist-histo-11-orgaos-linfaticos.tsv` (24 conceitos da E1).
- Pool extraído (read-only via AnkiConnect Docker): `anking-pool-histo-11-orgaos-linfaticos.json` — **102 cards** das tags `01_Lymphoid_Structures` (FirstAid, 104) + `05_Lymph_Nodes_and_Spleen` (B&B, 45), + ganchos clínicos `Encapsulated_bacteria` (10) e `Hereditary_Spherocytosis` (58).
- Slim: `anking-pool-...-slim.md` (88 prováveis-bons, 14 ruído).

## ⚠ Achado de método (o mais importante desta corrida)

**`buscar_tags_lote.py` subestimou grosseiramente a cobertura.** Com termos EN multi-palavra, o tokenizador casou ruído (`ankle`, `Frank-Starling`, `X-linked` por "cell/natural/killer") e declarou **20 de 24 conceitos como LACUNA**. Ao ler o **texto real** dos cards (camada 2), a cobertura verdadeira é **15 COBERTO + 6 PARCIAL + 3 LACUNA**. O recall ruim estava na ferramenta de busca por tag, não no deck.

**Recomendações para aprimorar a busca:**
1. Para termos EN multi-palavra, o `buscar_tags_lote` deveria exigir match de **frase** (ou ≥2 tokens contíguos), não token isolado — hoje um token comum polui o ranking.
2. A verdade vem da **camada 2 (texto do card)**, não da camada 1 (nome da tag). Para aulas de histologia, cujas tags Step1 são funcionais/imunológicas (não histológicas), pular direto para `extrair_cards` de uma subárvore âncora (`Lymphoid_Structures`) rende mais que buscar tag por conceito.
3. Semear a checklist com **1 termo EN curto e canônico** por conceito (ex.: "Hassall", "paracortex", "HEV") em vez de frase — casa melhor.

## Matriz conceito × card (24 conceitos)

### COBERTO (15) — há card real testando o conceito
| Conceito | Card-âncora (resumido) |
|---|---|
| 1.1 primário vs secundário; B→plasmócito | "secondary lymphoid organs allow immune cells to react with antigen"; bone marrow = produção |
| 1.2 subtipos de linfócito T | subsets T citotóxico/helper/reg (basic immuno) |
| 1.3 NK — imunidade inata | NK cells (Physeo/Pixorize) |
| 1.4 macrófago / APC | antigen-presenting cell (basic immuno) |
| 1.7 nódulo / centro germinativo (B) | "outer cortex contains follicles"; "mantle zone adjacent to germinal center"; follicular hyperplasia = B |
| 2.1 timo córtex/medula | "medulla of thymus pale, mature T cells"; cortex = immature |
| 2.5 corpúsculo de Hassall | "Hassall's corpuscles are eosinophilic areas composed of epithelial reticular cells" |
| 2.7 medula óssea — maturação B | "site of B-cell maturation? Bone marrow" |
| 3.1 linfonodo córtex/medula/drenagem | "outer cortex follicles"; medullary sinuses; drainage clusters |
| 3.3 paracórtex (T, timo-dependente) | "paracortex between follicles and medulla"; paracortical hyperplasia = T viral |
| 3.4 vênula de endotélio alto (HEV) | "lymph node paracortex contains high endothelial venules (HEV)" |
| 3.5 cordões/seios medulares (reticular) | "medullary sinuses contain reticular cells and macrophages" |
| 3.6 baço polpa branca/vermelha | "T-cells in PALS (white pulp)"; "B-cells in follicles + marginal zone"; RBC removal by macrophages |
| 3.7 PALS / artéria central | "central arterioles surrounded by periarteriolar lymphatic sheath" |
| 3.9 esplenectomia / encapsulados / esferocitose | encapsulated bacteria post-splenectomy; hereditary spherocytosis (58 cards) |

### PARCIAL (6) — tocado, mas sem o detalhe histológico da lâmina
| Conceito | Situação |
|---|---|
| 1.5 célula reticular / fibra reticular | "reticular cells" citadas nos seios; colágeno III não é testado (detalhe de histologia) |
| 1.6 histiócito (macrófago fixo) | só "sinus histiocytes" em contexto clínico de metástase |
| 1.8 MALT / arranjos frouxo-denso-nodular | MALT/Peyer em imuno de mucosa; os 3 arranjos histológicos não |
| 2.2 célula reticular epitelial | aparece dentro do card de Hassall; não como conceito próprio |
| 2.3 timócito | "immature T cells in cortex" cobre a ideia; o termo/morfologia não |
| 3.8 cordões de Billroth / sinusóide | função (macrófago remove hemácia) coberta; a estrutura nomeada não |

### LACUNA (3) — 0 card; cobrir por fonte externa
| Conceito | Fonte para cobrir |
|---|---|
| 2.4 barreira hematotímica | slide da Profa. Marilene + Junqueira (histologia; não é conceito Step 1) |
| 2.6 involução do timo com a idade | Junqueira + B&B Immunology (envelhecimento imune) — 0 no pool atual |
| 3.2 seio subcapsular (assinatura do linfonodo) | slide + Junqueira (detalhe de diagnóstico diferencial em lâmina) |

## Cobertura

**X/Y = 15/24 COBERTO (62%); +6 PARCIAL = 21/24 (87%) ao menos parcial; 3 LACUNA.**

Se aplicada (numa corrida futura, com sua autorização), a curadoria manteria ~30–40 cards das tags `Lymphoid_Structures` + `Lymph_Nodes_and_Spleen`, dropando os de drenagem linfática puramente anatômica (clusters inguinofemoral etc.), que são ruído para esta aula de histologia. As 3 LACUNAS + parte das PARCIAIS histológicas (barreira hematotímica, seio subcapsular, arranjos, Billroth nomeado) são candidatas naturais a **card NEBLI gerado da E1** numa sessão de calibração — o AnKing Step 1 não testa leitura de lâmina.

## Não aplicado

Deck intacto. Para aplicar numa próxima: `python flashcards/scripts/aplicar_curadoria_anking.py histo-11-orgaos-linfaticos` (depois de gerar o `-curado.json`). Nada foi tocado nesta corrida.
