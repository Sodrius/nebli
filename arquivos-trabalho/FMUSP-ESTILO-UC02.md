# O que a FMUSP cobra em UC02 — calibração para os cards (2026-07-13)

Fonte: provas reais em `slides/UC02/P1-P4/` (escaneadas; lidas por extração de imagem + visão).

## Achado decisivo — formato da prova prática P3 (histologia/anatomia)
A prova P3 mostra **micrografia H&E real com seta numerada** apontando uma estrutura; o aluno **identifica a estrutura indicada** (ex.: página da composta turma108, arrow "7" sobre a transição de camadas). Não é múltipla escolha de mecanismo — é **reconhecimento visual de estrutura em corte real**.

### Consequência direta para os cards (muda a fonte de imagem do IO)
- **Histologia → IO sobre MICROGRAFIA H&E** (não esquema vetorial). A fonte ideal é o **Junqueira 12ed** (`slides/Cópia de Junqueira Histologia 12ed.pdf`) — micrografias H&E rotuladas, idênticas em modalidade ao que a prova mostra. Ocluir o **rótulo da estrutura**; a resposta é o nome. Transferência máxima: o aluno treina no mesmo tipo de imagem que vai ver na prova.
- **Anatomia → IO sobre line-art/atlas** (estilo AK-IO-01, ramos arteriais rotulados EN + setas) OU peça, conforme a prova de anatomia. Puxar da internet por ora (decisão Davi 2026-07-13); atlas didático sob demanda.
- **Embriologia → mistura:** cloze de texto (bem coberto pelo AnKing) + IO de corte transversal (tubo neural/somitos) para as fases que a prova cobra em esquema.

## Implicação para o pipeline
O IO de histologia agora tem uma fonte canônica (Junqueira) e um gesto canônico (ocluir rótulo de estrutura em H&E). Isso resolve o gargalo de "onde acho imagem boa" para as 3 aulas de histologia da P3 (vasos, nervoso, linfoide). O OCR do `io_from_slide.py` funciona em micrografia rotulada desde que os rótulos sejam texto (não letras soltas de legenda) — quando forem letras+legenda, gerar as caixas a partir da posição das letras e pôr o nome no Extra/gabarito.

## Pendência
- Ler P1/P2/P4 com render+OCR (poppler ausente nesta sessão) para confirmar o mesmo padrão nas outras provas e extrair a lista de estruturas historicamente cobradas → vira checklist de prioridade dos IO. Provas são scans, exigem visão página a página.
