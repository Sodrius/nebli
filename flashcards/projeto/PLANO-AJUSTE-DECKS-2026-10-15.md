# Plano de ajuste dos decks UC03 e UC21 (F-20261015-CLAUDE-05, 15/10/2026 noite)

Pedido de Davi (literal em FEEDBACKS): decks com falta de informação e poucos cards; cards em tópicos e de conexão demais (“deveriam ser poucos e só quando realmente úteis”); não cobrem a aula toda; sobretudo UC03 e UC21; **UC08 está bem melhor, comparar**; gate duro de fontes (slide + bibliografia + apostila de veterano + tudo da pasta e de `Outros`); ajustar **cada deck individualmente**, amplo, sem sair do conteúdo da aula; seguir os comentários.

## 1. Diagnóstico (medido no Anki vivo e nas corridas, 15/10)

**Densidade.** Decks da UC08 têm 105–130 cards por aula de anatomia/histologia e 52–110 nas de fisiologia, quase todos cards de conteúdo e nenhum marcado como organizador. Os decks UC03 feitos em 14–15/10 ficaram com 22–63 cards para 20–99 lâminas:

| Aula | Lâminas | Notas | Cards | Organizadores | Conexão | Cards/lâmina |
|---|---|---|---|---|---|---|
| 07 Organização do sistema imune | 26 | 35 | 55 | **12** | 3 | 2,1 |
| 08 Reconhecimento inato | 23 | 39 | 61 | **8** | 0 | 2,7 |
| 17 Reconhecimento adaptativo | 18 | 31 | 41 | 4 | 0 | 2,3 |
| 20 MHC | 75 | 46 | 63 | 5 | 1 | **0,8** |
| 22 Mecanismos efetores | 64 | 40 | 63 | **8** | 2 | **1,0** |
| 10 Ação hormonal | 56 | 75 | 110 | **14** | **9** | 2,0 |
| 16 Regulação hormonal e massa corpórea | 62 | 30 | 37 | 6 | 1 | **0,6** |
| 15 Grand Round 1 | 57 | 25 | 30 | 4 | 0 | **0,5** |
| 18 Recombinação V(D)J | 25 | 36 | 42 | 1 | 2 | 1,7 |
| 09 Lesão celular | 47 | 53 | 77 | 7 | 0 | 1,6 |
| 11 Acúmulos e adaptação | 60 | 61 | 88 | **11** | 1 | 1,5 |
| 13 Envelhecimento | 22 | 25 | 35 | 5 | 3 | 1,6 |
| 14 Declaração de óbito | 20 | 14 | 22 | 5 | 0 | 1,1 |
| 12 RM | 99 | 37 | 45 | 5 | 0 | 0,5 (radio: aceitável se o núcleo estiver) |
| 40 Prática 3 | 42 | 44 | 73 | 7 | 0 | 1,7 |
| UC21 Caso 5 | 10 (caso) | 59 | 76 | 4 | 0 | 19 notas próprias, 40 compartilhadas |

**Causa 1 — fontes não lidas.** Em 14–15/10, a família “veteranos” e às vezes a “bibliografia” foram preenchidas com a **transcrição** ou com o relatório de um grupo (UC21). As apostilas-guia de Imuno, Pato, Micro e Biomol (`UC03/Outros/Apostilas de veteranos`), as monitorias (`<componente>/Material para Estudos`: p. ex. Imuno “Mapa Imunológico 1–3” e “Resumo da P1”) e o capítulo do livro não foram lidos. O gate antigo aceitava porque só conferia que havia *algum* arquivo na família.

**Causa 2 — lâminas “de revisão” excluídas.** Inventários marcaram blocos inteiros como `EXC: aula 08; Tab` (ex.: 22, lâminas 4–21). Parte é repetição real, mas a aula retoma e aprofunda: o que ela ensina de novo precisa de card.

**Causa 3 — volume trocado por tópicos.** Depois de F-20261015-CLAUDE-03/04, organizadores e conexões passaram a ser “padrão” e ocuparam o lugar de cards de conteúdo (07: 12 de 35 notas; 10: 23 de 75). Davi agora diz que devem ser poucos.

**Causa 4 — tópicos mal escritos.** Organizadores em linha (“acute phase: a, b, c, d – subacute: …”) em vez do modelo que Davi aprovou na UC08 (constrições do esôfago: pergunta + itens numerados, um por linha, cloze só no nome).

**UC21.** O Caso 5 tem 19 notas próprias e 40 compartilhadas de outras UCs: o caso guia e as 12 perguntas foram cobertos quase só por associação, e a “bibliografia” foi o relatório do grupo 11, não Guyton/Robbins/Milech.

## 2. O que muda nas regras (já gravado)

- MEMORY §4: **gate duro de fontes**; MEMORY §5/§6: tópicos e conexão **poucos**, só para os grupos que a aula ensina; volume vem dos cards de conteúdo; UC08 é referência de densidade.
- `nebli/gates.py › uc_materials` (novo, reprova): (a) bibliografia é livro, não transcrição/slides/relatório; (b) cada apostila de veteranos da UC lida com seção ou descartada com motivo, ao menos uma lida; (c) cada arquivo da pasta pessoal da aula e do `Material para Estudos` do componente lido ou descartado; (d) `pastas_extra` para casos como UC21 (`Não compartilhar/Menores/UC21`). Declaração em `fontes-decl.json › materiais_uc`.
- Hoje **todas** as corridas UC03/UC21 reprovam esse gate: cada deck passa por ele no seu ajuste.

## 3. Procedimento por deck (aplicado a cada um, individualmente)

1. **Fontes (gate duro):** extrair e ler a seção da aula em cada apostila-guia do componente, cada monitoria, o capítulo do livro da UC, a pasta pessoal e a da turma; registrar em `materiais_uc`. `python3 -m nebli.gates <corrida> --sem-anki` sem FALHA nas fontes antes de selecionar.
2. **Inventário por informação** (lâminas + transcrição + apostila + monitoria + livro + provas), na ordem das lâminas. Bloco “de revisão” só sai se a informação já tem card vivo no deck anterior (sh() quando o uso é aqui) — o que a aula acrescenta vira card.
3. **Diferença com o deck vivo:** cada informação sem card → card de conteúdo (AnKing → acervos → autoral pelos ANTI-EXEMPLARES). Organizadores: manter só os que montam um grupo real da aula, reescritos no modelo UC08 (pergunta + itens numerados em linhas, cloze no nome); os demais e as conexões sem ganho próprio saem por `nebli.retira` (suspensos com motivo, nada apagado sem autorização).
4. **Comentários** da aula seguidos pelo protocolo do MEMORY §10 (nada é apagado do campo; anexa `CORRIGIDO, DD, MM, YY.`); os comentários entram como pares em ANTI-EXEMPLARES (pedido de Davi no card de *Cryptococcus*).
5. **Calibração UC08:** comparar o deck lado a lado com um da UC08 de densidade parecida; ler a ordem viva inteira perguntando se um aluno aprenderia a aula só com ele.
6. `build --delta` + `nebli.delta`, ordem, recolor, gates completos (Tab dos cards novos/alterados: Codex ou eu, conforme a fila de Tabs).

## 4. Ordem de execução

1. **P3 em estudo agora (prova 06/11), dessuspensos:** 62 Inflamação crônica, Granulomatosa, 61 Infecção viral, 46 Eucariotos I, 52 Eucariotos II, 54 RNAs não codificadores, 45 Linfócitos T, 49 Células B, 12 Fungos, 44 Superficiais e cutâneas, 48 Subcutâneas, 50 Sistêmicas, GR3.
2. **P1 de 14–15/10 (as mais rasas):** 22, 20, 16, 15, 07, 08, 17, 18, 10, 09, 11, 13, 14, 12, 40.
3. **UC21 Caso 5** (refazer com o caso + perguntas + Guyton/Robbins/Milech de verdade; menos dependência de compartilhados).
4. **P2 e P1 antigas** (02–06, 27–39): só o gate de fontes e as lacunas que ele revelar (esses decks são mais densos).

Cada deck fechado: relato curto no chat (contagens antes/depois, o que entrou, o que saiu, comentários atendidos) e ESTADO-ATUAL atualizado.

## 5. Comentários pendentes (20 UC03, 11 UC08, 5 UC19 — lidos em 15/10)

- **UC03 P3:** LT com 2 cards de hipersensibilidade tipo IV (“conteúdo errado”, “era para ser de outro deck”) → retirar da 45 (aula 64 Hipersensibilidade ainda não dada); Eucariotos I “card repetido?”; fungos: α-glucano (Extra: fator de virulência), mitocôndria (imagem); subcutâneas: cloze no que se entende, *Sporothrix* e lobomicose (imagem); cutâneas: estrato córneo (imagem), tabela e onicomicose ajustadas por Davi (manter); sistêmicas: *Cryptococcus* meninges (Extra: porquê), urease (Tab sem porquê), três elogios (calibram); granulomatosa: Tab esquisito (recrutamento de monócitos), núcleos “irregularly scattered” (palavras abstratas); infecção viral: tópicos mal escritos → modelo das constrições do esôfago (UC08).
- **UC03 P2:** operon, repressor “1000-fold” (escrita estranha, sem negrito, sem ensinar).
- **UC08:** varizes esofágicas × anorretais parecidas demais (diferenciar a escrita); imagem ruim do jejuno e das varicosidades; glândula sublingual precisa da tabela das salivares; Paneth “não storytelling”; elogios (bluelink, jejuno 2/5, ramos da AMI, AMS, vitamina K) calibram.
- **UC19:** antagonista “intrinsic activity” ambíguo; antagonismo farmacocinético escrito de forma estranha; antagonista competitivo pede imagem; dois elogios.
