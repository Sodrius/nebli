# Meta-avaliação — Deck P3 UC02 completo (2026-07-13)

Pedido do Davi: "vai até o final, quero o deck da p3 completo... avalia de forma real, visando melhorar o processo... o que poderia ter sido feito pelo Sonnet, o que não, o que deveria ser Fable."

## O que foi entregue (verificável no Anki + Drive)
- **8 aulas P3 com deck-aula fechado**, 338 cards de estudo:
  - Tecido nervoso (34 NEBLIcards + 1 IO), Histologia dos vasos (25), Órgãos linfáticos (30),
    Anatomia circ/linf I (28), Sistema linfático pt2 (18), Circ/linf II (21) — **156 notas autorais → 256 cards** (atomização c1/c2/c3).
  - Embrio I (31) + Embrio II-III (37) — AnKing curados de sessão anterior.
- **9 .apkg exportados** (`flashcards/decks-apkg/`) e **subidos ao Drive** nas pastas de aula (por componente) + `P3 - UC02 completo.apkg` na raiz UC02.
- **Sincronizado ao AnkiWeb** (chega no celular).
- **QA pelo card-mirror** (o revisor que o Davi mandou endurecer): cravou 3 AnKings reais por match literal (conf 99), identificou os 6 NEBLIcards, e deu crítica de craft acionável.

## A correção real que o revisor gerou (prova de que ele agrega)
O card-mirror apontou que eu reusava `{{c1::}}` para fatos independentes (ex.: os 3 atalhos fetais). Convenção AnKing = `c1/c2/c3` → **um card atômico por item**. Apliquei em 27 cards; isso sozinho transformou 156 notas em 256 cards de estudo mais atômicos (melhor retenção). Sem o revisor, o deck sairia com cards que escondem 3 coisas de uma vez.
- O revisor também flagou "voz de monitor no Extra" como tell de NEBLI. **Ignorei de propósito**: para os cards do Davi, Extra explicativo é recurso desejado, não defeito. O discriminador julga *manufatura*; a decisão editorial é do operador.

## Quem deveria fazer cada passo (avaliação real desta sessão)

| Passo | Quem fez | Quem DEVERIA fazer | Por quê |
|---|---|---|---|
| Ler E1 + extrair conceitos (gate B2) | Opus (sessão) | **Opus** | Exige julgar o que é testável e ancorar cada card numa frase da E1 — raciocínio, não padrão. |
| Redigir os NEBLIcards PT | Opus (sessão) | **Fable 5** | Depois que o conceito e o craft estão travados, é geração de volume sob spec fechada. Fable é mais barato/rápido e a qualidade de escrita basta. Opus aqui foi overkill. |
| QA / discriminação de craft | card-mirror (Sonnet) | **Sonnet** | Ponto ideal: leu 55 exemplares, deu tells precisos, calibrou confiança. Confirmado 2ª vez. |
| Renumerar cloze, aplicar, exportar, upload, sync | script (sem LLM) | **sem LLM** | Determinístico. Nunca gastar token de modelo nisso. |
| Decidir PT vs EN, incluir/excluir, gate B2 | Opus | **Opus** | Decisão editorial com trade-off (indistinguibilidade vs língua da prova). |

**Conclusão de modelo:** o gargalo de custo desta sessão foi usar Opus para *redigir* 156 cards. O pipeline ótimo é **Opus destila conceitos + trava craft → Fable redige em massa → Sonnet faz QA → script aplica**. Opus só nas pontas (extração e QA-de-decisão), nunca no meio (redação em volume).

## Como melhorar o processo (real)
1. **Fila Fable para redação.** Montar um passo em que, dado o checklist de conceitos da E1 (Opus) + 2-3 exemplares de craft travado, o Fable gera o lote de cards. Corta ~70% do custo de redação.
2. **Instalar poppler.** Segue sendo a maior alavanca: destrava ler P1/P2/P4 (scans) em massa → extrair a lista histórica de estruturas cobradas → checklist de prioridade dos IO. Hoje só li a P3 por visão, imagem a imagem.
3. **Gerador de IO "seta-manual" (sem OCR)** para micrografia. A P3 prática é micrografia H&E + seta → identificar estrutura. Isso NÃO sai de OCR (não há texto sobre a estrutura). Precisa de um modo que posiciona a oclusão sobre a estrutura e põe o nome no Extra. É o item que mais transfere pra prova e o único não construído.
4. **Fonte de imagem limpa para IO.** Os slides do professor são compostos 4-em-1 densos (confirmado no slide-23 de embrio) — a rubrica manda preferir imagem limpa da web/atlas. Para IO de qualidade (embrião + Junqueira), o passo é curar imagens limpas antes, não OCR o slide sujo.
5. **Idempotência do apply + encoding.** Dois bugs pequenos custaram tempo: (a) colisão de dois reapply em background sobre o mesmo AnkiConnect; (b) crash de print em cp1252 no Windows. Ambos corrigidos (guard de duplicata + encode ascii-safe). Rodar apply sempre em foreground, um por vez.

## Honestidade sobre o que NÃO foi feito
- **IO visual (embrião + micrografias Junqueira):** não produzido nesta sessão além do 1 IO de neurônio já existente. Motivo declarado e alinhado ao critério do Davi ("cards de qualidade"): o slide-fonte é composto denso e a fonte limpa + gerador seta-manual são pré-requisitos de um IO bom. Forçar sairia abaixo da barra. É o próximo passo de maior valor.
- **Re-curadoria séria das 2 Embrio** (hoje AnKing-curadas de antes): mantidas como estão; são boas, mas não passaram pelo loop Card→E1 desta rodada.
