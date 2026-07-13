# Meta-avaliação — pipeline de cards P3 + IO (2026-07-12)

Baseada no que REALMENTE aconteceu nesta sessão (não em teoria).

## 1. Que modelo faz cada etapa (Opus / Sonnet / Haiku / Fable 5)

Régua: Opus = raciocínio pesado + decisão editorial + orquestração; Sonnet = julgamento por rubrica; Haiku = checagem barata determinística; Fable 5 = velocidade/throughput em tarefa bem-especificada (spec fechada, muitas repetições, latência importa).

| Etapa do pipeline | Fez agora | Deveria ser | Por quê (observado) |
|---|---|---|---|
| Endurecer agente / decidir rubrica | Opus | **Opus** | É design: exige entender os 5 exemplares e antecipar tells. Não delegável. |
| Discriminador card-mirror (rodada) | Sonnet | **Sonnet** (padrão) / **Fable 5** em lote grande | Sonnet deu tells precisos e honestos (rodada 2 confessou indistinguibilidade sem inventar). É julgamento por rubrica — cabe em Sonnet. Quando rodar dezenas de lotes/rodada, **Fable 5**: a rubrica já é a spec, o custo/latência mandam. Rodada de aprofundamento (tell sutil de voz) → Opus. |
| OCR + geometria das caixas (io_from_slide) | Python (sem LLM) | **Python** | Determinístico. Nenhum LLM precisa. O LLM só entra para (a) escolher a imagem e (b) revisar o preview. |
| Escolher/baixar a imagem certa da web | Opus (inline) | **Fable 5** ou **Sonnet** | Tarefa de busca + julgamento "essa imagem é limpa, EN, rotulada?". Spec fechada → Fable 5 dá conta com custo baixo; borderline visual → Sonnet. |
| Revisar preview (caixas justas? cobre rótulo?) | Opus (visão) | **Sonnet** (visão) | Julgamento visual por checklist. Opus é overkill; Haiku erra em imagem. Sonnet é o ponto. |
| Curar pool AnKing keep/drop (Embrio) | — | **Sonnet** | É rubrica de admissão (3 baldes, 0-3). Sonnet é o alvo canônico já usado. Opus só se o tema for ambíguo. |
| Gate B2 (card ∈ E1?) | — | **Haiku** (match) + **Opus** (borderline) | Casar conceito↔E1 é quase determinístico → Haiku/Python. Só o "isso está *implícito* na E1?" sobe pra Opus. |
| Gerar NEBLIcard de texto | — | **Opus** rascunho → **Fable 5** volume | 1º card do tema exige voz (Opus); depois, com a rubrica travada, gerar os N seguintes é transformação com spec → Fable 5. |
| Revisor-completude (E1↔cards) | — | **Sonnet** | Já é agente Sonnet. Confirmado adequado. |
| apkg export + Drive upload | Python/rclone | **Python** | Sem LLM. |
| Redação de E1/E2 (resumo) | Opus | **Opus** | Fora de escopo hoje, mas: voz de monitor + cadeia causal = Opus. |

**Resumo da régua:** o pipeline é mais barato do que parece. As únicas etapas genuinamente-Opus são *design de rubrica*, *rascunho do 1º card de cada tipo/tema* e *borderline de gate*. O grosso do volume (discriminar lotes, revisar previews, curar por rubrica, gerar cards conformes) é **Sonnet/Fable 5**. OCR, apkg e Drive não precisam de LLM.

## 2. O que Fable 5 destrava especificamente

Fable 5 é o motor de **throughput com spec fechada**. Onde ele muda o jogo aqui:
- Gerar 25-35 NEBLIcards/aula depois que a rubrica está travada (histo/anato NEBLIcard-heavy) — hoje isso seria Opus caro; Fable faz em fração do custo.
- Rodar o card-mirror em muitos lotes por rodada (estatística mais forte que "1 card vs 3 AnKing").
- Triagem inicial de imagens web ("limpa/EN/rotulada? sim/não") em lote.
- Não usar Fable em: design de rubrica, voz sutil, decisão de gate ambígua.

## 3. Como melhorar o processo (achados reais desta sessão)

1. **Infra frágil é o maior imposto.** No meio da sessão caíram JUNTOS o AnkiConnect e o daemon do Docker; e não existia container `anki-nebli` (o que respondia era o Anki desktop). A memória diz "AnkiConnect = Docker", mas a realidade era desktop. → **Corrigir a memória** e ter um **`anki_up.py` idempotente** (checa 8765; se cair, sobe o desktop OU o container, o que existir) rodado no início de toda sessão de cards. Perdi ~15% da sessão em infra.
2. **OCR não estava no ambiente.** Tesseract+por foram instalados agora (por.traineddata em `~/tessdata`, apontado por `TESSDATA_PREFIX`). → registrar como dependência do pipeline de IO em `FLASHCARDS.md`.
3. **Os slides são handout 4-em-1 (2480×3508), não figuras IO-ready.** OCR neles rende pouco (rótulos ~14px). A liberação do Davi para **usar imagem limpa da web** resolve isto e melhora indistinguibilidade — deve virar o **default** do IO, com o slide do professor só quando a figura específica for cobrada. → escrever no plano.
4. **"Uma aula por sessão fresca" vs "roda tudo agora" é uma tensão real de contexto.** Curar 8 aulas numa thread relê regras e estoura contexto. Com a máquina de IO pronta, o caminho barato é: **sessão-mãe curta chama 1 subagente-executor por aula** (cada um lê só o plano + rubrica + a E1 da aula), devolve o apkg. Isso respeita o "tudo numa conversa" do Davi SEM o context-bleed — a conversa-mãe fica leve. (Cuidado com o bug F9: usar subagente só para tarefa fechada, como o card-mirror, que funcionou.)
5. **Limitação do card-mirror para IO:** a coleção só tem 5 notas IO, todas clínicas Step-2 — não há IO AnKing de histologia para comparar no mesmo domínio. A convergência foi contra manufatura (geometria/asset/Extra), que é o que importa, mas para robustez vale **importar um deck IO de anatomia/histologia externo** (o Davi já autorizou "colher decks externos") e usá-lo como pool de comparação real.
6. **Custo do loop:** cada rodada de card-mirror = 1 spawn Sonnet ~27k tokens. Convergiu em 2. Barato. Escalar para lotes maiores em Fable baratearia mais.

## 4. Próximo passo recomendado (8 aulas)
Ordem do plano: Embrio I → Embrio II-III (curadoria AnKing, firmam template) → histo (nervoso/vasos/linfoide, IO+NEBLIcard) → anato (I-p1/I-p2/II). Com a máquina pronta, cada aula = recon (feito) → curar/gerar → gate B2 → revisor-completude → apply → apkg → Drive. Melhor rodar **1 aula por subagente-executor** para não estourar contexto.

---
# Sessão 2026-07-13 — discriminador competente + calibração pela prova

## O que foi entregue de real
1. **Discriminador de fato competente** (o pedido central do Davi: "o revisor deve estar fraco"). Antes cravava AnKing por *ausência de defeito*; agora, munido de 50 exemplares reais estratificados (`ANKING-DOSSIE-TEXTO.md`) + 5 IO com imagem (`ANKING-DOSSIE-IO.md`), crava por **impressão digital positiva** e calibra confiança. Validado em lote cego held-out: 5/5 de texto, pegou o autoral craft (conf 94), passou o IO indistinguível (conf 90).
2. **Correção de rubrica que só apareceu com dados reais:** "Wikimedia/Blausen = autoral" estava errado; o tell é a **linha de crédito**, não a fonte. Teria feito o discriminador errar cards AnKing legítimos.
3. **Calibração pela prova:** P3 = micrografia H&E + seta numerada → fonte do IO de histologia é **micrografia (Junqueira)**, não esquema. Muda a estratégia de imagem.
4. **Sync AnkiWeb** feito (82 cards P3 no celular).

## Avaliação REAL de modelo por etapa (revisada com o que aconteceu)
| Etapa | Modelo certo | Evidência desta sessão |
|---|---|---|
| Endurecer rubrica + PASSO 0 + achar a correção da regra de proveniência | **Opus** | Exigiu ver que "ausência de defeito ≠ AnKing" e inferir a regra da linha-de-crédito a partir de exemplares — raciocínio, não checklist. |
| Discriminar lote cego (card-mirror) | **Sonnet** | O subagente Sonnet leu 50+5 exemplares, deu tells precisos, calibrou confiança e rankeou o mais suspeito. Perfeito para julgamento por exemplar. |
| Extrair dossiê / OCR / extrair figura de PDF / sync | **sem LLM** | Scripts determinísticos (`extrair_dossie_anking.py`, pypdf, AnkiConnect). |
| Gerar 25-35 NEBLIcards/aula depois da rubrica travada | **Fable 5** | Spec fechada + volume + repetição — o caso de uso do Fable. NÃO usar Fable no julgamento sutil nem no gate B2. |
| Ler prova escaneada (visão) | **Sonnet/Opus com visão** | Uma imagem bastou para recalibrar a fonte de imagem inteira. Alto valor por token. |

## Como melhorar o processo (achados reais)
1. **O dossiê de 50 é reutilizável e barato** — deveria ser pré-requisito PERMANENTE do card-mirror (já está no PASSO 0). Regenerar quando o AnKing v12 atualizar.
2. **Provas são scans → precisam de poppler/OCR** para leitura em massa. Instalar poppler destrava estudar P1/P2/P4 e extrair a lista histórica de estruturas cobradas (vira o checklist de prioridade dos IO).
3. **Micrografia-com-seta é um modo de gerador novo** (sem OCR): posiciona oclusão sobre a estrutura + nome no Extra. É o formato que mais transfere para a prova FMUSP. Construir antes de curar as 3 aulas de histologia.
4. **Divisão de trabalho honesta:** subagente cura AnKing (keep/drop) bem; **NEBLIcard/IO exige o loop card-mirror da sessão principal** (subagente não spawna subagente). Logo histo/anato (AnKing-pobres, NEBLIcard-heavy) são trabalho da sessão principal, uma aula por vez; só Embrio é delegável.
5. **Escopo honesto:** "curar 8 aulas + IO + apkg + Drive + provas + avaliação" é multi-sessão. Melhor entregar 1 aula completa + infra sólida do que 8 pela metade.
