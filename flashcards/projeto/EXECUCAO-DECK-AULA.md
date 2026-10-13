# Como fazer um deck-aula (roteiro vigente, 13/10/2026)

As preferências estão no [MEMORY](../../MEMORY.md); este arquivo diz **como** executá-las, na ordem. Um pedido curto de Davi (“faz a aula X”, “continua”) roda tudo isto até a entrega, sem agente e sem parar para aprovação. Versão anterior: `arquivo/2026-10-13-reorganizacao/flashcards/projeto/EXECUCAO-DECK-AULA.md`.

Molde técnico de referência (correlação de imagens, feita direto, 56/56): `arquivos-trabalho/deck-aula-uc03-pr01-correlacao-pat-rad-1-2026-10-11/` (spec.py, inventario.py, fontes-decl.json, REVISAO-DE-QUALIDADE.md). Para aula de texto: `deck-aula-uc03-rd05-tomografia-2026-10-11/`. São moldes de formato, não de seleção.

## 0. Antes de começar (2 minutos)

1. ESTADO-ATUAL › “Retomar aqui”: qual é a próxima aula e quem está com ela. Se outro executor reivindicou, pegar a seguinte. **Registrar a reivindicação** (“Com Claude: <aula>”) antes de criar a corrida.
2. Releitura só do que mudou: entradas novas de FEEDBACKS desde a última sessão. O MEMORY já é a regra consolidada.
3. Corrida: `python3 -m nebli.corrida abrir arquivos-trabalho/deck-aula-<uc>-<curto>-<slug>-<data> --slides <pdf> [--transcricao <pdf>]` e `python3 -m nebli.corrida molde <corrida>`. Conferir que o prefixo `<curto>` está livre (`"tag:NEBLI::ordem::<curto>-*"` vazio).

## 1. Ler as fontes (MEMORY §4)

- Lâminas como imagem: folhas de contato 3×3 (PyMuPDF) em `visual/`; texto extraído para `fontes/`. Ver todas antes de numerar.
- Pasta inteira da aula no drive da turma → `fontes/turma/` (cada arquivo lido ou descartado com motivo); transcrição inteira; monitoria e apostila de veteranos só na seção da aula (`grep`); provas pelo índice; capítulo do livro da UC → `livros/<nome>.txt` (só as páginas da aula).
- Vídeos: não. `fontes-decl.json` sem `canais` registra a dispensa sozinho.

## 2. Escopo e inventário (MEMORY §3) — o passo que mais define a qualidade

1. Cronograma e aulas vizinhas → no `spec.py`, o **mapa obrigatório** `ESCOPO = {"objetivo": ..., "centrais": [("conceito", "chave-do-princípio", "detalhe1", ...)], "exemplos": [...], "outras_aulas": [("subtema", "aula")]}`. O `pre` reprova sem ele, aponta conceito central sem card e detalhe que vem antes do seu princípio (modelo na corrida da 06). Princípio dado em aula anterior entra como `sh-<nid>`. Conferir decks vizinhos vivos (o que já existe entra por `sh()`).
2. `inventario.py`: cada lâmina com conteúdo → itens atômicos, cada um apontando para a chave do card, `sh-<nid>` ou `EXC: motivo` (capa, ilustração, repetição, outra aula citada pelo nome). `CAPITULO` (livro) e `EXERCICIOS` (provas, monitoria, apostila, palavras-cruzadas) também: item de prova/material da aula sempre aponta para card.
3. Antes de buscar, responder por escrito no mapa: quais princípios esta aula precisa que Davi recupere antes dos detalhes (o que é, para que serve, como funciona em geral)? Cada um terá card próprio, antes dos detalhes. Exemplo que é só ilustração vai em `exemplos` (sem card ou só uma linha no Extra). Detalhe só entra se a aula o ensina como alvo ou a prova cobra; profundidade de ciclo básico (sem semiologia, conduta ou fisiopatologia elevada).

## 3. Buscar e selecionar (MEMORY §5)

- `python3 -m nebli.busca_acervos <corrida>/busca/anking.txt "rótulo=frase" ...` (frases, não siglas). Para cada candidato, conferir cópia NEBLI viva (`"tag:NEBLI::source::nid-<nid>"`) e usar `sh(nid_vivo, cor, ...)`.
- AnKing → externos → autoral. Registrar recusas pertinentes em `EXCLUIDOS` e temas fora em `FORA_DO_RECORTE`.

## 4. Escrever o `spec.py` (MEMORY §6–8)

- `ak()` para AnKing (flags por cloze; HY 1–2 verde ou `hy_repete`/`clinica_lateral`), `au()` para autoral (2–3 `espelhos`, `autoria`, motivo da cor), `sh()` para compartilhado. Ordem = lâminas.
- Imagens: recortar da fonte certa para `img/`, ver o recorte (montagem em `visual/`) e declarar `IMAGENS_VISTAS = {"arquivo.png": "o que mostra e por que ensina"}`. Cortar títulos que entreguem a resposta.
- `VERSO` para dar linha curta a card sem texto no verso; `DUPLICACAO` para resposta coincidente com ganho próprio; `slide_sem_alternativa` quando a imagem do caso da aula é o objetivo.
- **Revisão do núcleo antes de rodar:** ler a lista de alvos contra o mapa do passo 2. Faltou conceito organizador? Algum exemplo virou card sem motivo? Cor por ganho, sem quota?

## 5. Comandos (saída só com falhas)

```text
python3 -m nebli.artefatos pre <corrida>          # build, planejamento, ext.txt, imagens vistas, fontes, inventário, lint, pré-gate
python3 <corrida>/apply.py                         # instala sob o lock (só notas novas; sync adiado se Davi estiver revisando)
python3 -m nebli.artefatos suspender <corrida>    # só aula antiga (MEMORY §10)
python3 -m nebli.artefatos tab <corrida>          # em segundo plano; depois ler as 3 amostras que ele mostra
python3 -m nebli.artefatos despejo <corrida>      # ler o deck vivo inteiro, card a card
python3 -m nebli.artefatos pos <corrida> --li-despejo [--corrigidos k1,k2]
python3 -m nebli.artefatos entrega <corrida> --pasta "UC03/<Comp>/<NN - Aula>" --nome "<Aula>" --slides <arquivo na pasta pessoal>
```

- `pre` só pode falhar nos passos de pós-instalação. Lint com reprovação dura, ISSUES no build ou item de prova sem card: corrigir o spec e rodar de novo.
- **Leitura do despejo** (o julgamento final): frente natural, cloze certo, resposta vazada, imagem certa e legível, cor coerente com o motivo, Extra útil, erro do AnKing herdado. Corrigir no spec → `python3 build.py --delta` → `python3 -m nebli.delta <corrida>` → Tab de novo para os alterados. Notas da leitura em `REVISAO = {"chave": "o que foi conferido"}` no spec.
- `REVISAO-DE-QUALIDADE.md` à mão, curto: deck, contagens, objetivo e mapa de escopo, fontes, decisões de escopo/cor, imagens, Tab, perguntas a Davi.
- `entrega` republica `NEBLI - UCxx.apkg`, sincroniza (ou adia se Davi estiver revisando) e roda os gates completos: 100% para entregar.

## 7. Análise do deck-prova / deck-UC (quando a prova fecha ou a pedido)

1. `python3 -m nebli.analise_prova "NEBLI::UCxx::Pn"` (ou `"NEBLI::UCxx"`): sinais por aula (cores, CLIN, NUM, Tab antigo, ESCOPO) e pares de possível repetição em `RELATORIO.md`; todas as frentes na ordem em `frentes.txt`.
2. Ler `frentes.txt` inteiro e julgar o conjunto (MEMORY §12b): cobertura, ordem lógica/progressão, princípios antes dos detalhes, detalhes que se complementam, repetição, peso de ciclo básico, amostra de Tabs. Escrever o julgamento no `RELATORIO.md`.
3. Corrigir pelos specs das aulas: `nebli.retira` para repetido/detalhe/clínica acima do ciclo básico (com motivo), `recolor` para cor, card-ponte de princípio no deck onde ele deve aparecer, `ESCOPO` acrescentado às aulas antigas; `build.py --delta` + `nebli.delta`; Tab dos afetados (`artefatos tab`); gates de cada aula; pacote da UC.
4. Relatar a Davi o antes/depois por aula e o que mudou no conjunto.

## 6. Fechar

1. ESTADO-ATUAL: aula entregue (corrida, contagens, gates, sha do pacote), perguntas a Davi com a suposição, próxima aula. Atualizar ao fim de **cada** deck.
2. Relato no chat no formato do MEMORY §11.
3. Feedback recebido na sessão: FEEDBACKS (literal) → MEMORY (regra reescrita no lugar) → lint/gate quando mecanizável.

## Referência técnica (quando precisar)

- **Delta em aula instalada:** `build.py --delta` + `nebli.delta`; nunca rodar apply/delta com ISSUES no build. A delta não apaga nota retirada, estudada, comentada ou com bandeira; correção viva no Anki entra em `correcoes-vivas.json`.
- **Retirar card:** `python3 -m nebli.retira <corrida> --recibo receipt-antes.json chave:motivo ...` (suspende, tag `NEBLI::retirado::<motivo>`, guarda o antes em `retirados.json`). Apagar só com autorização de Davi e backup.
- **Recolorir conforme plano:** `python3 -m nebli.recolor <corrida> [--aplicar]` (inclui compartilhados; nunca baixa bandeira maior de outra aula).
- **Ordem:** `python3 -m nebli.ordem verificar NEBLI::<lesson_id> --plan <corrida>/plan.json`; compartilhados: `nebli.ordem_compartilhados`.
- **Oclusão do próprio slide** (anatomia/histologia, quando reconhecer é objetivo): `nebli.slide_io` (máscara do rótulo inteiro, `aponta="estrutura"`, `busca` registrada).
- **Figura de livro:** `nebli.img_figura` (recorte sem título/legenda); `nebli.ilustrar` busca figura AnKing.
- **Pacote da UC sem a entrega completa:** `python3 -m nebli.package_uc --uc UC03 --output <pasta>/NEBLI - UC03.apkg` (resumo na tela, relatório em `<apkg>.relatorio.json`) + `python3 -m nebli.entrega <pasta da aula> --nome <aula> --uc-apkg <apkg>`.
- **Manutenção de decks sob pedido:** `python3 -m nebli.decks status|suspender|dessuspender|desfazer|liberar|instalar-addon` (registros em `arquivos-trabalho/deck-ops/`).
- **Tab:** `python3 -m nebli.explicacoes gerar|resumo|mostrar|ruins`; estilo em `config/explicacao-tab.md`. Se a geração cair, rodar de novo (pula o que está atual).
- **Escrita no Anki fora dos scripts:** sempre `with nebli.decks.escrita(call, "<rótulo>", sync=False):`; checar `guiCurrentCard` (erro “Gui review is not currently active” = Davi não está revisando).
- **Comentários:** `flashcards/scripts/ler_comentarios.py`; protocolo no MEMORY §10.
- Acervos, canais e localizadores de fontes: [ACERVOS-REFERENCIA](ACERVOS-REFERENCIA.md).
