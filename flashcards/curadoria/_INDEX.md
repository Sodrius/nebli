<!-- Razão-mestra da curadoria AnKing v12 por aula.
     Este arquivo é o AVISO VIVO: mostra, a cada momento, quais cards já foram
     dessuspendidos/copiados no deck do Davi, por aula, para ele poder AJUSTAR.
     Atualizado automaticamente por aplicar_curadoria_anking.py.
     Método: flashcards/CURADORIA-ANKING.md -->

# Curadoria AnKing v12 — razão-mestra por aula

Revisão espaçada de longo prazo: cada aula do NEBLI vira um bloco de cards muito bem curados do AnKing v12, marcados com a tag-âncora `NEBLI::<slug>`. Este documento é o painel de controle — mostra o que já está no deck e onde ajustar.

> **RESET 2026-07-11 — começar fresh (2º semestre).** Todos os manifestos, curado.json, checklists, pools, cobertura e mapa-confusoes anteriores foram apagados (recuperáveis via git). A curadoria recomeça do zero pelo método atual. A grande faxina da coleção AnKing (suspender 100% + apagar decks não-AnKing) é feita pelo Davi na volta das férias.

**Fila pendente-gerado:** conceito-chave da E1 sem card real bom no AnKing entra como `PENDENTE-GERADO` no manifesto + `arquivos-trabalho/cobertura-<slug>.json` — enfileirado para card NEBLI cloze gerado numa **sessão futura de calibração** (não gerar antes de destilar/validar o padrão de bom card; ver `calibrar-antes-de-gerar-cards`).

## Como ajustar um bloco no Anki
No **Browse** do Anki, digite a tag-âncora da aula:
- `tag:NEBLI::<slug>` → vê exatamente os cards daquela aula.
- Tirou um card? `Ctrl+J` re-suspende (não apaga). Quer ver os suspensos: `tag:NEBLI::<slug> is:suspended`.

## Estado das aulas

| Aula (slug) | UC/Componente | Status | notes/cards | Aplicado em | Cobertura AnKing | Lacunas → fonte | Tag-âncora |
|---|---|---|---|---|---|---|---|
| biomol-25-mutacao-reparo-recombinacao | UC02/Bio. Molecular | copiado p/ deck-aula | 37/42 | 2026-07-11 | 11/18 COBERTO (1 parc, 6 lac) | 1.5 proofreading · 1.6 5-BrU · 2.1 fotoliase · 2.2 MGMT · 2.6 SOS · 3.5 lambda attB → slide/E1 | `NEBLI::biomol-25-mutacao-reparo-recombinacao` |
| bioq-23-aminoacidos-ureia | UC02/Bioquímica | copiado p/ deck-aula | 74/114 | 2026-07-11 | 13/17 COBERTO (2 parc, 2 lac) | 1.1 turnover · 1.2 balanço N₂ → slide/E1; biciclo Krebs parcial | `NEBLI::bioq-23-aminoacidos-ureia` |
| bioq-21-lipideos-rotas | UC02/Bioquímica | copiado p/ deck-aula | 60/83 | 2026-07-11 | 9/13 COBERTO (1 parc, 1 lac) | 2.1 conta ATP palmitato (peças) · 2.2 gordura vs glicose → slide/E1 | `NEBLI::bioq-21-lipideos-rotas` |

**Total: 3 aulas ativas (deck de teste UC02:: — 171 notes / 239 cards).**

## Notas
- Entradas novas (método card-a-card) trazem `#cards` reais, `%cobertura` e `lacunas→fonte` preenchidos pelo manifesto da aula.
