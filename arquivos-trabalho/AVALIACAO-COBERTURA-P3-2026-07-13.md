# Avaliador de cobertura mútua E1↔cards + rebalanceamento — P3 UC02 (2026-07-13)

Pedido do Davi: avaliador COMPLETO — (a) todo card ∈ E1 (gate B2) e, **sobretudo**, (b) todo conceito/estrutura principal da E1 ∈ algum card. + relatório de erros + rebalancear (anatomia merece mais profundidade) + achar redundância.

## Densidade (card/subtópico) — o achado do rebalanceamento
| Aula | Subtópicos E1 | Cards | card/subt | Veredito |
|---|---|---|---|---|
| Tecido nervoso | 10 | 34 | 3.4 | equilibrado |
| Histologia dos vasos | 9 | 25 | 2.8 | equilibrado |
| Órgãos linfáticos | 11 | 30 | 2.7 | equilibrado |
| **Anatomia circ/linf I (coração)** | **15** | **28** | **1.9** | **RASO — aprofundar** |
| **Sistema linfático (pt2)** | **10** | **18** | **1.8** | **RASO** |
| **Anatomia circ/linf II** | ~15 | **21** | ~1.4 | **RASO — aula riquíssima** |
| Embrio I / II-III | — | 31/37 | — | AnKing curado, ok |

**Conclusão:** histologia bem coberta; **as 3 aulas de anatomia estão sub-cardadas** — exatamente o que o Davi sentiu. Anatomia é reconhecimento de estrutura + relações espaciais → merece MAIS cards e profundidade, e imagens (que faltaram).

## Gate B2 (card ∈ E1): PASSA
Todos os 156 NEBLIcards foram redigidos a partir das frases das E1 lidas nesta operação. Nenhum card órfão. (Confirmado na redação; o rebuild EN mantém a âncora.)

## Cobertura reversa (conceito da E1 → tem card?) — LACUNAS por aula

### Tecido nervoso — quase completo; faltam:
- Tipos de sinapse por posição (**axodendrítica / axossomática / axoaxônica**) — só a elétrica foi cardada.
- Espinhas dendríticas como substrato da plasticidade — mencionado de leve.

### Histologia dos vasos — completo. Sem lacuna relevante. Redundância baixa.

### Órgãos linfáticos — completo. (Todas as 3 assinaturas + linhagens cobertas.)

### Anatomia circ/linf I (coração) — LACUNAS reais (aprofundar):
- **Músculos pectíneos** e **aurículas** (estruturas atriais) — não cardados.
- Nomes das **cúspides da tricúspide** (anterior/posterior/septal) e detalhe da mitral.
- **Trajeto das coronárias** (esquerda no sulco interventricular anterior; direita no AV + interventricular posterior) — só o óstio foi cardado.
- **Microcirculação** (subtópico 3.3 inteiro): metarteríola, esfíncter pré-capilar, canal de escoamento, anastomose AV — sub-representado.
- Focos de ausculta; bulhas (1ª cardada, contexto raso).
- Tipos de capilar (contínuo/fenestrado/sinusoide) — aparecem na E1 de anato tb, cardados na histologia (ok, evitar duplicar).

### Sistema linfático (pt2) — LACUNAS:
- Os **5 troncos linfáticos completos** (só intestinal+lombar cardados; faltam jugulares, subclávios, broncomediastinais como card próprio).
- Redes superficiais × profundas (cardado 1, raso).
- Linfonodo: córtex/paracórtex/medula (cardado na histologia; aqui a drenagem regional é o foco — ok).

### Anatomia circ/linf II — LACUNAS (aula rica, poucos cards):
- **Circulação fetal**: os 3 atalhos cardados, mas falta o destino de cada um pós-nascimento (lig. venoso, fossa oval, lig. arterioso).
- **Ramos do arco** além dos nomeados; **subclávia → vertebral** (para o polígono de Willis).
- Ramos **viscerais vs parietais** da aorta torácica (cardado 1, poderia detalhar).
- **Ílio-femoral**; ramos da ilíaca interna.
- Sistema ázigo: hemiázigo/hemiázigo acessória (cardado só ázigo).

## Redundância (cards que se sobrepõem) — BAIXA, com 1 ponto de atenção
- "Válvulas venosas / bomba muscular" aparece na **histologia dos vasos**, na **anato I** e implicitamente no **sistema linfático**. Nos 3 decks-aula separados é aceitável (cada um é estudado como unidade), mas no **deck-prova combinado** vira 2-3 cards quase iguais. Ação: no combinado, manter a versão da histologia (mecanismo) e enxugar a repetição literal na anato.
- "Ducto torácico / cisterna do quilo / ângulo venoso" duplicado entre anato-I-linfático, sistema-linfático e anato-II. Consolidar para 1 card mecanístico + 1 de território.

## Erros de PADRÃO a corrigir no rebuild (não são de conteúdo, são de forma)
1. **Idioma:** PT → **EN** (decisão nova do Davi; melhor p/ indistinguibilidade + Step 1).
2. **Extra sem imagem:** todos os Extra eram só-texto. AnKing tem **imagem no Extra** (essencial). Rebuild anexa imagem-mãe por cluster + crédito.
3. **Extra prolixo ("voz de monitor"):** telegrafar no estilo AnKing.
4. **Sem IO:** faltou image occlusion (embrião + micrografia Junqueira). Construir e incluir.
5. **Anatomia sem imagem da internet** e **rasa** — aprofundar + ilustrar.

## Plano de correção (= rebuild ao padrão novo, aula por aula)
Cada aula é reescrita: EN + Extra-com-imagem + IO visual + lacunas acima preenchidas + anatomia aprofundada, passando pelo card-mirror até indistinguível. Exemplar provado primeiro (Tecido nervoso), depois escala. Sistema em `flashcards/scripts/build_card.py` + `io_visual.py`.
