<!-- Razão-mestra da curadoria AnKing v12 por aula.
     Este arquivo é o AVISO VIVO: mostra, a cada momento, quais cards já foram
     dessuspendidos/copiados no deck do Davi, por aula, para ele poder AJUSTAR.
     Atualizado automaticamente por aplicar_curadoria_anking.py.
     Método: flashcards/CURADORIA-ANKING.md -->

# Curadoria AnKing v12 — razão-mestra por aula

Revisão espaçada de longo prazo: cada aula do NEBLI vira um bloco de cards muito bem curados do AnKing v12, marcados com a tag-âncora `NEBLI::<slug>`. Este documento é o painel de controle — mostra o que já está no deck e onde ajustar.

> As linhas abaixo registram decks já aplicados e podem refletir regras históricas. Para aula nova, a política canônica é `FLASHCARDS.md`: classificar `nuclear | supporting | no_card`, buscar AnKing → outros decks → autoral e fechar na mesma corrida. `PENDENTE-GERADO` antigo não é estado de entrega.

## Como ajustar um bloco no Anki
No **Browse** do Anki, digite a tag-âncora da aula:
- `tag:NEBLI::<slug>` → vê exatamente os cards daquela aula.
- Tirou um card? `Ctrl+J` re-suspende (não apaga). Quer ver os suspensos: `tag:NEBLI::<slug> is:suspended`.

## Estado das aulas

| Aula (slug) | UC/Componente | Status | notes/cards | Aplicado em | Cobertura AnKing | Lacunas → fonte | Tag-âncora |
|---|---|---|---|---|---|---|---|
| biomol-25-mutacao-reparo-recombinacao | UC02/Bio. Molecular | copiado p/ deck-aula | 37/42 | 2026-07-11 | 11/18 COBERTO (1 parc, 6 lac) | 1.5 proofreading · 1.6 5-BrU · 2.1 fotoliase · 2.2 MGMT · 2.6 SOS · 3.5 lambda attB → slide/E1 | `NEBLI::biomol-25-mutacao-reparo-recombinacao` |
| bioq-23-aminoacidos-ureia | UC02/Bioquímica | RE-CURADO 2026-07-12 | 48 AnKing + 2 NEBLIgerado = 50 | 2026-07-12 | 15/15 subtópicos E1 cobertos; 2 gerados (bal. N₂, desaminação) | PENDENTE: 1.1 turnover · 3.3 biciclo ATP (conceitual, sem card) | `NEBLI::bioq-23-aminoacidos-ureia` |
| bioq-21-lipideos-rotas | UC02/Bioquímica | RE-CURADO 2026-07-12 | 48 AnKing + 3 NEBLIgerado = 51 | 2026-07-12 | 12/12 subtópicos E1 cobertos; 3 gerados (FAS/ATP/ativação) | PENDENTE: 1.1 densidade energética · 2.2 gordura>glicose (conceitual) | `NEBLI::bioq-21-lipideos-rotas` |
| embrio-01-gametogenese-fertilizacao | UC02/Embriologia | export-add p/ deck-aula (PDF pronto) | 14 AnKing + 17 NEBLIgerado = 31 notes/40 cards | 2026-07-11 | 8/19 por AnKing; toda a PARTE III (fertilização) é NEBLIcard | AFP/rastreio · não-disjunção clínica (fora do escopo da E1) | `NEBLI::embrio-01-gametogenese-fertilizacao` |
| embrio-02-03-gastrulacao-neurulacao | UC02/Embriologia | export-add p/ deck-aula (PDF pronto) | 22 AnKing + 15 NEBLIgerado = 37 notes/41 cards | 2026-07-11 | derivados via AnKing; processo (EMT, neuroporo, somito, dobramentos) é NEBLIcard | AFP em DTN aberto → falta na E1 | `NEBLI::embrio-02-03-gastrulacao-neurulacao` |

**Total: 5 aulas ativas (deck de teste UC02::). Re-curadas 2026-07-12: aminoácidos 74→50 e lipídeos 60→51 (enxugadas + NEBLIcards de gap de prova). 38 cards cortados foram movidos para `UC02::Bioquímica::_cortados-recuradoria-20260712` + suspensos (reversível, tag `NEBLI::recuradoria-cortado-20260712`).**

> **Nota técnica (2026-07-11):** os 2 decks de embrio foram feitos a partir de **PDF pronto** (sem etapa de E1 sendo redigida) → gate B2 estrito: só entrou conceito já na E1; nada de aprofundamento novo. O `copiar_curadoria_para_deck.py` (match ao vivo) casou só 5/22 no deck 2 porque o **export ⊋ coleção viva** do Davi (cards atualizados/ausentes); usei `aplicar_deck_export.py` (novo) que adiciona os notes a partir do conteúdo do export — determinístico, independe do subset vivo. AnKing embrio cobre **derivados** (high-yield Step 1), quase não cobre a **coreografia** (fertilização, EMT, neuroporos, somito, dobramentos) → daí o volume de NEBLIcards.

## Notas
- Entradas novas (método card-a-card) trazem `#cards` reais, `%cobertura` e `lacunas→fonte` preenchidos pelo manifesto da aula.
