# Análise de custo-efetividade — comentários e suspensões (31/10/2026)

Pedido: F-20261031-CLAUDE-04. Dados vivos do Anki em 31/10 e `comentarios-cards.jsonl`.

## Números

- 6.899 cartas NEBLI; 2.137 estudadas; 614 suspensas depois de estudar (28,7%), sem contar retiradas pelo pipeline. Tirando os decks suspensos inteiros (UC19, Grand Round 21): 478.
- Das 478: 68% sem nenhum lapso, mediana de 3 revisões, 57% com até 3 revisões. São cartas fáceis cortadas cedo: o motivo é valor baixo, não dificuldade.
- Suspensão por origem: lâmina 43%, Histology 39%, autoral 31%, AnKing 27%, Kenhub 12%.
- Por HY do AnKing: HY1 21%, HY2 26%, HY3 34%, sem HY 32%.
- Por cor: rosa 43%, azul 33%, verde 24%.
- Aulas: BT03 estômago 40%, BT04 intestinos 39%, AN01 esôfago-estômago 37%, IM51 distúrbios 33%, PT47 granuloma 32% (13 autorais), BM52 50%.
- Comentários: 772 falas únicas; 403 em autorais (~0,7 por autoral estudado) contra 157 em AnKing (~0,14 por estudado). Famílias: imagem 276, "não ensina/estranho" 219, verso 167, cloze 142, negrito 75, tamanho 53, organizador 52, repetido 25, fora da aula 23; elogios 123.

## O que está ruim

1. **Volume acima de valor.** "Todo AnKing do conteúdo entra, sem teto", "um pouco mais" e "todo HY 1–2 do Step" premiam presença, não utilidade. Resultado: listas de associação clínica (HLA de cada doença), vários cards do mesmo fato (vilosidade em AnKing, MCAT e autoral), detalhe rosa.
2. **Autoral caro e frágil.** Cada autoral gera quase um comentário; rodadas de revisor aprovam pela rubrica e Davi ainda reprova pela leitura ("linguagem pouco induzível", "cloze num lugar ruim").
3. **Clusters.** Uma aula gera 10–13 cards do mesmo tema com clozes vizinhos (granuloma, histonas); Davi suspende o bloco.
4. **Imagem é a queixa nº 1.** Oclusão de lâmina e páginas inteiras do Histology/BlueLink: frente sem alvo claro, figura grande ou genérica; 66 suspensas eram só imagem.
5. **Falta fio da aula.** Os cards ficam corretos e soltos; Davi pede "pensamento contínuo", organizador e o grande resumo como esqueleto.
6. **Processo pesado demais.** Cerca de 110 checagens por deck, várias de artefato (arquivos, hashes, leituras) e não de aprendizagem; muitas rodadas de agente por detalhe; gates que mudam de outro executor bloqueiam entregas. O custo vai para papelada, não para a escolha do card.

## Como melhorar, de forma realista

1. **Orçamento por aula.** Antes de buscar, fixar um teto (ex.: 1 card por item do mapa, no máximo 2) e escolher o melhor card de cada item; o resto não entra. Trocar "todo AnKing entra" por "o melhor card de cada item; HY1–2 só quando o item é da aula".
2. **Sem rosa por padrão.** Detalhe vai para o verso de um card que já existe; card rosa só sob pedido.
3. **Deduplicação antes de instalar.** Agrupar cards por alvo (semântica) e deixar um por alvo; cluster com 4 ou mais cards vira 1 organizador mais 1–2 de mecanismo.
4. **Autoral só onde falta e só no formato que Davi aprovou.** Copiar um exemplar real; limite baixo por aula (ex.: 5). Primeiro mostrar 3–5 autorais a Davi antes de instalar o resto (piloto rápido) nas UCs novas.
5. **Imagem focada ou nenhuma.** Proibir página inteira e oclusão de lâmina sem recorte; recortar a figura no alvo; render no celular obrigatório.
6. **Esqueleto da aula primeiro.** Ordem e blocos tirados do grande resumo ou do roteiro; cada bloco abre com o organizador e o card de mecanismo, e os detalhes vêm depois e são poucos.
7. **Gates enxutos e medidos pelo resultado.** Manter os gates que correspondem às famílias de queixa (cobertura do roteiro, cloze, negrito, imagem, duplicidade, orçamento) e medir cada deck pela taxa de suspensão e de comentário nas duas primeiras semanas; abaixo de 10% é a meta.
