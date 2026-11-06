# 65 Reparo tecidual v4 — revisão de qualidade (06/11/2026, Claude)

## Por que houve v4
Davi (05/11 e 06/11): "ficou raso", "faltou card de fases da cicatrização", "não abordou tudo (ex: o gráfico com fases da inflamação)". Diagnóstico verificado: o inventário da v3 marcava 13 de 43 lâminas de conteúdo como `fora_do_recorte` (5, 9, 16, 17, 18, 20, 24, 25, 30, 32, 34, 35, 37), entre elas os três gráficos da aula. A v3 tinha encolhido de 54 para 29 notas ao longo de 11+ rodadas de revisor (F-20261105-CLAUDE-01).

## Lacunas fechadas (aula → cards)
- Lâmina 5 (potência das células-tronco): três AnKing (totipotente, pluripotente, multipotente).
- Lâmina 8 (tabela de fatores): EGF, TGF-α, VEGF e FGF-2 do AnKing (VEGF, FGF-2 e EGF estavam em EXCLUIDOS como "repete"; voltaram porque a aula ensina a tabela) + organizador KGF/HGF.
- Lâmina 9 (importância prática): TGF-β inibe proliferação (card do Treg, Imuno, associado) além do TGF-β fibrose/angiogênese.
- Lâminas 13 e 17: cobertas pelo organizador das fases (mesma ordem temporal).
- Lâmina 16 (gráfico das fases): card próprio com a figura; remodelação de 21 dias a 2 anos.
- Lâmina 18: vasoconstrição como primeiro passo da hemostasia (AnKing HY 1).
- Lâmina 20: serotonina e histamina da plaqueta (card da aula 38 suspenso por Davi, puxado para reavaliar).
- Lâmina 24 (gráfico de células e oxigênio): pico do neutrófilo; hipóxia relativa pelo consumo da proliferação.
- Lâmina 25 (dia 3): TNF/IL-1 na fase inflamatória × TGF-β na proliferativa, com a figura.
- Lâmina 30 (gráfico da matriz): colágeno I predomina em cerca de 3 semanas; fibronectina e força no verso.
- Lâminas 32–34: desbridar até o leito vermelho do tecido de granulação.
- Lâmina 35: cicatriz mais clara porque o melanócito repõe menos que a célula basal.
- Lâmina 37: redução do edema, força tênsil e contração já tinham card (maturação, 70–80% da força, miofibroblasto).

## Correções nos cards antigos
- Organizadores da v3 (destinos, nichos, fases, M1 × M2, mediadores do macrófago) ganharam negrito no critério de cada linha (gate de 05/11).

## Excessos e limites
- Total: 47 notas / 53 cards próprios (antes 29) + compartilhados. Nenhum card de doença novo; o único caso clínico novo (desbridamento) é a fala do professor sobre o leito de granulação.
- Os dois autorais compartilhados de outras aulas (Treg e plaqueta) têm negrito dentro do cloze, anti-padrão do GUIA-3; corrigidos na escrita.
- `c-org-fases` e `c-grafico-fases` usam a mesma figura com alvos diferentes (nome das fases × duração da remodelação).

## Cards → aula
Todo card do plano está num bloco da compreensão (`fidelidade.blocos[].cards_conferidos`) e num item do mapa; tipos e princípio em `tipos.tsv`.
