# Curadoria AnKing — embrio-gastrulacao-neurulacao

**Aula:** Gastrulação e Neurulação (Embriologia, UC02, Prova 3 · 16/jul)
**Gerado:** 2026-07-10
**Status:** ✅ KEEP/DROP FINO FEITO + DECK DE REVISÃO CRIADO (2026-07-10). AnkiConnect subiu vivo (container `anki-nebli` com o AnKing Step Deck, ~25,7k cards). Pool bruto das tags-âncora = **275 notas** (muito Step 2 fora de escopo). Keep fino manual (Opus lê o slim) = **50 notas / 60 cards**, movidas para o deck real `NEBLI::embrio-gastrulacao-neurulacao` (todas SUSPENSAS — deck só-pra-ver, não inunda revisão), marcadas `NEBLI::embrio-gastrulacao-neurulacao`, `sync` disparado (aparece no celular). Seleção + origem por card em `embrio-gastrulacao-neurulacao-curado.json` (`card_origem` = "AnKing Step Deck" para todas → reversível). Para ativar de verdade no estudo: dessuspender + reposicionar due (ver [[reposicionar-cards-curados-frente-fila]]).

**Tag-âncora:** `NEBLI::embrio-gastrulacao-neurulacao`
**Deck separado:** via filtered deck sobre `tag:NEBLI::embrio-gastrulacao-neurulacao` (a convenção NEBLI não move o card do deck AnKing; agrupa por tag e dessuspende). Se Davi quiser um deck REAL separado (changeDeck), sinalizar — exige passo extra.

## Método usado (offline)

`buscar_tags_lote` retornou 0 (bug conhecido: termos EN multi-palavra subestimam recall — memória 2026-07-07). A cobertura real veio de mapear as **subárvores-âncora de embriologia** no export `anking-v12-export.txt` (28k cards Step 1) contra a checklist da E1. Critério rígido de inclusão (2026-07-04): entra só o card cujo conceito está na Seção B do Tema Card; vizinhança (arcos faríngeos em detalhe, embriologia genital, teratógenos, malformações de fossa posterior) fica de fora.

## Matriz conceito × tag (checklist da E1 → AnKing)

| # | Conceito da E1 | Tag-âncora AnKing candidata | #cards | Status | Fonte se lacuna |
|---|---|---|---|---|---|
| 1.1 | Três folhetos vêm do epiblasto | `#B&B::22_Repro::01_Embryology::03_Germ_Layers` (18) + `#FirstAid::15_Repro::01_Embryology::02_Embryologic_derivatives` (30) | ~15 on-scope | COBERTO | — |
| 1.2 | Disco bilaminar (epiblasto/hipoblasto) | `#FirstAid::15_Repro::01_Embryology::01_Early_embryonic_development` (17) | ~4 | PARCIAL | slide 6-9 / Moore cap. 3 |
| 1.3 | Linha primitiva e nó primitivo | `#B&B::22_Repro::01_Embryology::02_Embryogenesis` (5) + Early_embryonic_development | ~3 | PARCIAL | slide 7 / Moore |
| 1.4 | EMT (ingressão) | — | 0 | LACUNA | slide / Moore (Step 1 não drilla EMT no contexto embrio) |
| 1.5 | Notocorda: eixo, indutor, núcleo pulposo | `#B&B::22_Repro::01_Embryology::02_Embryogenesis` + `01_Embryonic_Genes` (SHH) (11) | ~4 | PARCIAL | slide 12-13 / Moore |
| 2.1 | Indução neural e placa neural | `#B&B::16_Neuro::05...::06_Neuroembryology` (48) + `#Physeo::01_Embryology::07_Neuro::01_...` (49) | ~10 on-scope | COBERTO | — |
| 2.2 | Fechamento do tubo neural e neuroporos | `#FirstAid::15_Repro::01_Embryology::02_Embryologic_derivatives::01_Ectoderm::*Neural_Tube` (7) + Neuroembryology | ~8 | COBERTO | — |
| 2.3 | DTN e ácido fólico | `#SketchyPath::13_Neuro::04_Congenital_&_Neurocutaneous::01_Neural_Tube_Defects...` (53) + `#Bootcamp::Neurology::01_Embryology::04_Embryologic_Cranial_Defects_and_Spinal_Defects` (32) | ~15 on-scope | COBERTO (rico) | — |
| 2.4 | Crista neural e derivados | `#FirstAid::15_Repro::01_Embryology::02_Embryologic_derivatives::01_Ectoderm::*Neural_Crest` (12) + Neuroembryology | ~10 | COBERTO | — |
| 3.1 | Derivados do mesoderma; somitos | `#FirstAid::15_Repro::01_Embryology::02_Embryologic_derivatives::02_Mesoderm` (10) | ~8 | COBERTO | — |
| 3.2 | Dobramento do corpo (céfalo-caudal/lateral) | — | 0 | LACUNA | slide 25-30 / Moore (Step 1 quase não cobre body folding explícito) |
| 3.3 | Tubo digestório; membranas bucofaríngea/cloacal | `#B&B::10_GI::01_Anatomy::01_Gastrointestinal_Embryology` (76) | ~6 on-scope | PARCIAL | slide 31-33 / Moore (foregut/hindgut sim; membranas parcial) |

## Cobertura

**COBERTOS:** 6/12 (1.1, 2.1, 2.2, 2.3, 2.4, 3.1)
**PARCIAIS:** 4/12 (1.2, 1.3, 1.5, 3.3) — âncora existe, complementar com slide/Moore
**LACUNAS:** 2/12 (1.4 EMT, 3.2 dobramento) — não cobertos pelo AnKing Step 1; cobrir por slide do professor + Moore cap. 4-5

Alvo estimado após keep/drop fino: **~35-45 cards on-scope** (dentro da faixa 30-50). A contagem por tag acima é bruta (subárvore inteira); o keep fino remove pathologia pura de Step 1 (holoprosencefalia, Chiari, teratógenos, malformações de fossa posterior, arcos faríngeos detalhados) que caem fora da Seção B.

## Próximo passo (quando o Anki estiver vivo)

```bash
# 1. subir o container (INFRA-REMOTO.md) com o perfil do Davi + login AnkiWeb
# 2. extrair texto real dos cards das tags-âncora acima:
python flashcards/scripts/extrair_cards_anking.py "<tags acima>" --slug embrio-gastrulacao-neurulacao
python flashcards/scripts/prefiltrar_pool.py embrio-gastrulacao-neurulacao
# 3. keep/drop fino (Opus lê o slim), gravar guids_kept em embrio-gastrulacao-neurulacao-curado.json
# 4. aplicar (marca NEBLI:: + dessuspende) + sync:
python flashcards/scripts/aplicar_curadoria_anking.py embrio-gastrulacao-neurulacao
python flashcards/scripts/verificar_cobertura_anking.py embrio-gastrulacao-neurulacao
# 5. filtered deck sobre tag:NEBLI::embrio-gastrulacao-neurulacao = o "deck separado"
```
