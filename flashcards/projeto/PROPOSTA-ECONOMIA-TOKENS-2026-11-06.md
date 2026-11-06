# Proposta: gastar menos tokens e condensar os arquivos (06/11/2026, Claude)

Pedido de Davi (06/11): "me dá uma forma de gastarmos menos tokens e condensarmos os arquivos, porque gerar qualquer coisa aqui tem sido extremamente pesado e bate o limite de memória do sonnet mt rápido".

## Diagnóstico medido

| O que pesa | Tamanho | Por quê |
|---|---|---|
| Leitura obrigatória por corrida (GUIA-1 a 4, MEMORY, pipeline, revisor, calibração) | 228 KB ≈ 60 mil tokens | o gate `exemplares_lidos` exige reler tudo inteiro a cada corrida |
| FEEDBACKS.md | 340 KB | só se lê o novo, mas a busca do F-id e as citações forçam abrir trechos grandes |
| ESTADO-ATUAL.md | 106 KB | “Retomar aqui” acumula dezenas de entradas antigas; a sessão lê o arquivo inteiro |
| GUIA_CARDS.md | 880 KB | histórico, não é leitura obrigatória, mas os gates leem nids dele |
| Gates por corrida | ~125 checagens, várias com saída longa | cada rodada de correção relê centenas de linhas de falha |
| Revisores independentes | 3 agentes × até 3 rodadas | cada rodada relê o pacote inteiro (~100 mil tokens por agente) |
| `arquivos-trabalho/` | 626 corridas, 28 GB | cópias de fontes e planos antigos que ninguém mais lê |

Nesta sessão, a 69 sozinha gastou mais tokens em leitura obrigatória, gates e revisores do que em escrever cards.

## Proposta (do maior ganho ao menor)

1. **Leitura obrigatória por resumo, não inteira.** Gerar `LEITURA-ESSENCIAL.md` (≤ 15 KB): as regras vigentes em uma linha cada, com o ID do feedback e um exemplar/anti por regra, construído a partir dos quatro guias e do MEMORY. O gate passa a exigir o hash desse resumo, não dos oito arquivos. Os arquivos completos ficam para consulta quando o resumo apontar. Economia estimada: ~50 mil tokens por corrida.
2. **MEMORY enxuto.** As seções de UC07/Kenhub, Tab, add-on e deck-prova (≈ 60% do arquivo) vão para arquivos próprios, lidos só na rota correspondente. MEMORY fica com o deck-aula (≈ 30 KB).
3. **ESTADO-ATUAL só com o vivo.** “Retomar aqui” com no máximo 5 entradas; o resto vai para `arquivo/estado-<mês>.md` com hash. Hoje são 106 KB, ficariam ~8 KB.
4. **FEEDBACKS por mês.** `FEEDBACKS.md` guarda só o mês corrente; meses fechados vão para `arquivo/feedbacks-2026-10.md`. O `ultimo_feedback()` lê só o mês corrente.
5. **Gates com saída curta.** `nebli.gates --resumo` imprime só as falhas, uma linha cada, e um código por falha; o detalhe sai só com `--detalhe <gate>`.
6. **Um revisor por rodada, não três.** Revisor de autorais e verificador por casos viram um só agente com a mesma rubrica; formatação final só no vivo e só nos autorais alterados (a revisão por delta, hash a hash, já existe).
7. **Molde de corrida mais completo.** Muitos tokens desta sessão foram para encaixar artefatos de formato (cobertura.tsv, tipos.tsv, inventário, fidelidade, escopo). Um script `nebli.corrida artefatos <corrida>` que gera todos a partir do spec e do mapa (como o `art69.py` feito aqui) evita refazê-los à mão em cada aula.
8. **Limpeza de `arquivos-trabalho/`.** Compactar corridas entregues há mais de 15 dias (fontes, livros, visual) num `.tar.zst` em `~/NEBLI-privado/arquivo/`, mantendo só spec, plan, receipt e recibos no repositório.

## O que não muda

Os gates de qualidade (cobertura por lâmina, AnKing primeiro, revisão dos autorais, figuras) continuam; muda só a quantidade de texto relido para chegar neles.

## Decisão pedida

Davi escolhe quais itens aplicar. Sugestão de ordem: 1, 3, 4, 7, 5 (ganho grande, risco baixo); 2, 6, 8 depois.
