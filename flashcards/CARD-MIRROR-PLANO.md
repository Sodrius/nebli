# CARD-MIRROR — loop adversarial para NEBLIcards indistinguíveis do AnKing

> **Origem:** pedido do Davi (2026-07-12): "cria um agente que compara os seus cards com os do AnKing várias vezes e faz ajustes nos seus até não dar para reconhecer padrões mais — isso é um plano pra você aprender a fazer cards melhores." Este documento é o plano; o agente vive em `.claude/agents/card-mirror.md`; o que se aprende decanta em `flashcards/CARD-MIRROR-RUBRICA.md`.

## A ideia central (um GAN em texto)

Dois papéis em oposição, rodando em rodadas:

- **Discriminador (D)** — agente `card-mirror`. Recebe um lote **cego** (cards NEBLI + AnKing embaralhados, sem tag/selo). Para cada card, decide "AnKing-nativo" ou "autoral/NEBLI" **e nomeia o tell** (a característica que o entregou). Métrica: acurácia acima de 50% (chance). Enquanto D acerta, há padrão a corrigir.
- **Refinador (R)** — a sessão principal (Opus). Lê os tells de D e reescreve os NEBLIcards para apagá-los (frente, cloze, Extra, imagem, HTML). Reaplica via AnkiConnect.
- **Árbitro/loop** — a sessão principal embaralha, cega (remove selo `❖`, tag, e qualquer marca intencional), roda D, alimenta R, repete.

**Convergência:** para quando D cai a ~chance **e** os tells que ele cita são não-substantivos ("chutei", "50/50"). Com poucos NEBLIcards a estatística é fraca — então o **tell qualitativo** manda mais que o número. Um card só "passa" quando D, vendo-o cego, não sabe justificar por que seria autoral.

**O que D deve ignorar (marcas intencionais, não são tells):** o selo `❖ NEBLIcard` e a tag `NEBLI::gerado` são identificadores propositais — D julga **só a manufatura** (frase, cloze, imagem, Extra, HTML), não esses carimbos. Indistinguibilidade é da *craft*, não da etiqueta.

## Eixos de tell que D investiga (checklist de features)

1. **Imagem** — dimensão (~1080px de largura no AnKing), formato (jpg/webp leve vs PNG pesado), **fonte** (recorte limpo/textbook vs slide de PowerPoint colorido em português), idioma dos rótulos, se é **imagem-mãe reusada** de cards irmãos (o mais nativo). *Preferência de fonte declarada por Davi: outros cards AnKing > internet > slide.*
2. **Cloze** — nº de clozes (AnKing: 86% single), comprimento do branco (mediana ~1–3 palavras), o que é apagado (token de alto valor vs oração inteira), sintaxe de hint `::`, densidade de `<b>/<i>/<u>` no branco.
3. **Frente** — comprimento (mediana AnKing ~17 palavras), forma pergunta ("What/Which…?") vs afirmação com cloze, wrapper `<div>`, negrito nos termos-chave, travessão "—" (raro no AnKing — **tell NEBLI clássico**).
4. **Extra** — presença (~83% AnKing), comprimento (mediana ~20 palavras), voz (AnKing: telegráfico, bullet/mecanismo; NEBLI: prosa de monitor — **tell**), presença de mnemônico.
5. **HTML/formatação** — AnKing embrulha em `<div>`, usa `<b>` p/ termo, `<sub>/<sup>` p/ química; travessões, aspas curvas "" e reticências … são pistas de prosa autoral.
6. **Idioma** — AnKing é inglês; qualquer português no corpo = tell imediato (por isso NEBLIcard passou a ser EN).

## Extensões (o "planeje mais coisa em cima")

1. **Rubrica viva → gerar nativo desde o nascimento.** Cada tell corrigido vira linha em `CARD-MIRROR-RUBRICA.md`. Com o tempo a rubrica é a *spec de geração*: NEBLIcards já nascem conformes e o loop precisa de menos rodadas. É o depósito do aprendizado (o objetivo do Davi).
2. **Linter pré-inserção (`lint_neblicard.py`).** Converte os tells estáveis em checagem determinística e barata que roda **antes** de um card entrar: comprimento da frente, travessão, tamanho do branco, dimensão/peso da imagem, presença de Extra, português residual. Barra o card que reintroduz um tell já aprendido (guarda anti-regressão).
3. **Pipeline de imagem (`preparar_imagem_neblicard.py` + sourcing).** Ordem canônica: (a) **reusar imagem-mãe de card AnKing irmão** (nativa, leve, já no dispositivo → sem lag — *default*); (b) imagem limpa da internet (fundo branco, inglês); (c) recorte do slide + resize p/ ~1080px como último recurso. Nunca slide inteiro colorido.
4. **Davi como discriminador humano (juiz final).** Periodicamente, um lote cego vai pro Davi (canal do monitor/email): ele tenta adivinhar quais são autorais. O que ele erra = indistinguível; o que ele acerta e por quê = novo tell pra rubrica. Fecha o loop com o julgamento que mais importa.
5. **Generalização pro pipeline canônico.** Rubrica + linter viram parte da regra R9 (NEBLIcard) do `FLASHCARDS.md`: todo card autoral futuro passa pelo mesmo crivo. O aprendizado destas 2 aulas beneficia todas as próximas.
6. **Métrica versionada.** Guardar por rodada a acurácia de D e os tells restantes (`arquivos-trabalho/card-mirror-<data>.md`), pra ver a curva de convergência e provar que os cards melhoraram (não é vibe).

## Fluxo operacional de uma rodada

```
1. dump cego: Text + Extra (sem selo/tag) + [imagem: arquivo] dos NEBLIcards + amostra AnKing, embaralhado, numerado; chave salva à parte.
2. spawn card-mirror com o lote cego → verdict por card + tell + confiança.
3. medir acurácia vs chave; coletar tells dos NEBLIcards pegos.
4. R (sessão principal) corrige cada tell; reaplica via AnkiConnect; registra o tell na rubrica.
5. repetir até D ≈ chance e tells não-substantivos.
```

## Estado
- Rodada 0 (baseline, 2026-07-12): tell dominante = **imagem** (slide roxo PT 3000×2250 vs textbook EN 1080). Corrigido antes da rodada 1 (reuso da imagem-mãe). Ver rubrica.
- Próximas rodadas: registradas em `CARD-MIRROR-RUBRICA.md` + `arquivos-trabalho/card-mirror-*.md`.
