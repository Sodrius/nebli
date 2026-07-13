# PIPELINE-CANDIDATOS.md — o que aprendemos montando o deck-prova P3 que deve entrar no pipeline canônico

> Notas vivas (aberto 2026-07-13). Objetivo declarado do Davi: **deck-prova nível AnKing, montável com facilidade nas próximas vezes.** Cada item aqui é um candidato a virar regra canônica (CLAUDE.md / FLASHCARDS.md / ROLES.md) ou script. Quando um item amadurece, promover e marcar ✅.

## Contexto do achado
O deck-prova P3 (1º sério) saiu 6/10. Auditoria do card-mirror (Opus) + pesquisa de decks + os 5 decks de referência importados revelaram **por que** e **como** consertar. As lições abaixo são o destilado.

---

## A. CRAFT — o que faz um bom card (a lição-mãe: RECALL, não reconhecimento)

**Candidato 1 — Gate de indução no fechamento de card (virar `lint_neblicard.py` + item de ROLES § Flashcards).**
O erro dominante (≈45% dos cards P3) é **testar reconhecimento, não recall**: o cloze é adivinhável só lendo a frase. Pergunta de ouro por card: *"dá pra acertar o branco sem saber a matéria?"*. Se sim, reprovar. 4 padrões a caçar (detalhe em `CARD-MIRROR-RUBRICA.md` § Rodada P3):
1. **NAME-in-stem leak** — nome da estrutura no stem + descrição apagada. Inverter: stem = descrição, cloze = o nome.
2. **Parêntese que entrega** — exemplos/sinônimo/número que dá o branco. Mover pra cloze irmão.
3. **Cloze-dump** — branco de 4+ palavras. Atomizar em c1/c2/c3 de 1-3 palavras.
4. **Extra em prosa de monitor** — frase causal = voz E1. Extra = fragmento telegráfico ou vazio.
→ **Promessa de virar linter automático** antes do card-mirror (barato, pega 3 dos 4 padrões por regex/heurística: negrito-no-stem + cloze>3 palavras + "porque/because" no Extra).

**Candidato 2 — card-mirror como GATE de fechamento, não QA de amostra.** Roda em TODO card autoral do deck até indistinguível (já é regra em `regras-neblicard-anking-nivel`; reforçar que só se aplica ao *resíduo autoral*, não aos reais curados).

---

## B. CURADORIA — curar real antes de autorar, mas TIERAR as fontes

**Candidato 3 — Ordem canônica: curar real > autorar (só o resíduo).** Com os 5 decks de referência, a maioria dos cards de anato/histo deve ser **card real curado** (já nativo, não precisa da batalha de indistinguibilidade). Autorar só a lacuna. Corta ~70% da autoria. → Entra no `CURADORIA-ANKING.md` como passo 0.

**Candidato 4 — TIER das fontes (imported ≠ AnKing-grade). LIÇÃO IMPORTANTE.**
Nem todo deck importado é craft AnKing. Descoberto ao inspecionar via AnkiConnect:
| Deck | Tier | Uso |
|---|---|---|
| **LLU Histology** (149) | ★ ouro visual | micrografia real + `{{c1::nome}}` — formato EXATO da prova prática. Cloze apaga o nome = indução perfeita. Preferir. |
| **BlueLink** (2992) | ★ ouro espacial | IO de cadáver real. **Só por tag** `BlueLink::<Região>` (texto vazio, keyword=0). |
| **Dope Anatomy** (3186) | bom | IO Netter idealizado; aprender o esquema limpo. |
| **`Histology (ploirodon)`** (6023) | reservatório de TEXTO/imagem | verboso, baixa indução (h3, bullets, c1 repetido na lista). **Colher a imagem do Extra**; card só entra se passar o filtro de craft (A). Nunca dump. |
| **100 Concepts (Dorian)** (303) | gancho clínico | correlato p/ `#clinica-box`. |
→ Regra: **card real ainda passa pelo gate de indução + gate B2 (∈ E1) + linha de crédito.** Curar não é copiar cegamente.

**Candidato 5 — Preferência de fonte por tipo de card (já em `CARD-MIRROR-RUBRICA` § fonte de imagem; consolidar):** histologia→LLU/micrografia; anatomia macro→BlueLink(real)+Dope(esquema); clínica→Dorian.

---

## C. IMAGEM / IO — o buraco maior do P3

**Candidato 6 — IO de anatomia AnKing-grade a partir de OpenStax/AnatomyTOOL (CC BY 4.0).** Fontes limpas EN mapeadas (pesquisa 2026-07-13): coração Fig 19.9/19.20; linfático Fig 21.4 (ducto torácico + cisterna do quilo numa imagem); great vessels OpenStax. → tabela completa em `CARD-MIRROR-RUBRICA` a consolidar; virar input do gerador de IO.

**Candidato 7 — Gerador de IO "seta-na-estrutura" para micrografia H&E (NÃO-OCR).** A prova prática = micrografia + seta → identificar. Não sai de OCR. Modo a construir: posiciona oclusão sobre a estrutura, nome no gabarito. Item de maior transferência pra prova e o único não-construído. (LLU já entrega parte disso pronto — priorizar LLU antes de construir.)

**Candidato 8 — Embriologia é a fronteira de autoria real.** Nenhum dos 5 decks cobre embrio. IO próprio a partir de OpenStax Fig 28.9 (gastrulação) e Fig 5.5 (neurulação) + AnKing embryology cloze. Gênero genuinamente aditivo (não existe embryo-IO comunitário).

---

## D. PROCESSO / MODELO (do meta-avaliação P3)

**Candidato 9 — Fila Fable para redigir o resíduo autoral.** Opus destila conceito + trava craft → Fable redige volume → card-mirror QA → script aplica. Opus só nas pontas.
**Candidato 10 — poppler** (ler P1/P2/P4 scans → checklist histórico de estruturas cobradas).
**Candidato 11 — apply sempre em foreground, 1 por vez** (colisão de reapply + crash cp1252 já corrigidos).

---

## Estado / próximos
- [x] Drive limpo dos .apkg P3 (melhorar antes de voltar).
- [x] Lição de indução gravada em `regras-neblicard-anking-nivel` + `CARD-MIRROR-RUBRICA` § Rodada P3.
- [x] 5 decks de referência confirmados vivos via AnkiConnect + tierados.
- [~] Curar **Histologia dos vasos** (piloto do fluxo curar-real):
  - [x] **6 cards LLU (ouro)** tagueados `NEBLI::histo-09-vasos` + `NEBLI::from-LLU`: elastic artery (gross+mag), muscular artery (gross+mag), vein (gross+mag) — micrografia real, cloze apaga o nome. Backbone visual da aula.
  - [ ] **Resíduo a preencher** (conceitos da E1 que LLU não cobre): túnicas íntima/média/adventícia (camadas + lâmina elástica interna/externa), tipos de capilar (contínuo/fenestrado/sinusoide), vasa vasorum, efeito Windkessel, válvulas venosas/bomba muscular, pericito. Fonte: ploirodon filtrado pelo gate de indução OU autoral corrigido (apagar o nome, atomizar).
  - Nota: cards LLU extras vistos e roteados pra outras aulas — umbilical cord → circ fetal (anato-II); AV-valve vs semilunar → coração (anato-I).
- [ ] Escalar às outras 7 aulas.
- [ ] IO anatomia (OpenStax) + embrio IO.
