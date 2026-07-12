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
