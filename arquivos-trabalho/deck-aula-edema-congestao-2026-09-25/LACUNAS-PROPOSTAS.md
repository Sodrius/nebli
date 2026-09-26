# Edema e congestão — lacunas propostas (aguardando decisão de Davi, 25/09)

Contexto: piloto E1 + cards reprovado ("excessivamente clínico", F-C20) e desfeito; deck restaurado (36 cards, 24 verdes/12 azuis após o ajuste de cores). Davi acha que **ainda falta conteúdo** e pediu para olhar provas, Robbins e aulas da net. Regra: bom deck da aula, sem adiantar clínica; ajustes pequenos sobre o deck existente, um de cada vez.

## Fontes consultadas nesta rodada
- **Provas UC03** (`referencias-externas/uc03/consultar.py --slug pat-05-edema-congestao`, mais 39 subquestões de PT com edema/congestão/exsudato/ascite): mecanismos de permeabilidade (histamina, bradicinina, leucotrienos, IL-1/TNF, lesão direta e por leucócitos) já estão em Inflamação aguda e Inflamação início/resolução — **não repetir aqui**.
- **Robbins**: no Drive (`Robbins Bases Patológicas das Doenças (2).pdf`, id `1u6R2qzAKb7zEDeBzkD6_NSvDh7sjdvn6`, 501 MB, pasta Livros) mas **não aberto**: conector devolve texto vazio, link direto pede login, Chrome desconectado. Itens marcados "Robbins" abaixo vêm de conhecimento do cap. 4, não de leitura desta rodada. Para ler: baixar pelo Chrome (autorizado) para `arquivos-trabalho/livros/` e extrair só o cap. de distúrbios hemodinâmicos (edema/congestão) com pymupdf.
- **Aulas da net** (legendas PT baixadas com yt-dlp para `fontes/aulas-net/`, ignoradas pelo git): Patologia Fácil (`mtshZfw61mM` edema; `YCmRBXkpJ6o` hiperemia/congestão) e Canal Resumed (`BVGapNg-vYw`).
- Quizlet do cap. 4 do Robbins: 403.

## Lacunas (o que a aula ensina e o deck não cobre)
1. Linfa devolve o excedente filtrado ao sangue (ducto torácico) — lâmina 4; AnKing `1471466870844`.
2. Exsudato pelas características: turvo, rico em proteína e leucócitos, densidade > 1,020 — provas 2016/2019/2025; o card transudato×exsudato mora em Inflamação aguda (nota `1790253536913`).
3. Linfedema crônico endurece e perde o cacifo (fibrose por proteína retida) — lâmina 7.
4. Ascite na cirrose: queda do volume circulante efetivo → rim retém Na⁺ — lâmina 11 (sem síndrome hepatorrenal).
5. Edema pulmonar ao microscópio, com a lâmina 9 na frente; macro (pulmão pesado, líquido espumoso) no verso.
6. Membrana hialina como marca do edema por permeabilidade no pulmão, com lâminas 13–15 na frente.
7. Distribuição do edema: dependente na IC (tornozelo/sacro) × periorbital na doença renal.
8. Hiperemia pode ser fisiológica (exercício, rubor) ou inflamatória; congestão (= hiperemia passiva) é sempre patológica. (azul)
9. Casca de laranja na mama = edema por linfáticos da derme obstruídos (foto da lâmina 7). (azul)
10. Opcional: congestão hepática prolongada → fibrose centrolobular. (azul)

Fora de propósito: edema cerebral/herniação, hemorragia (petéquia/equimose), tumefação celular, SDRA com neutrófilos, síndrome hepatorrenal, retenção primária de sódio na nefrótica.

## Decisões pendentes
- Adicionar 1–9 (e 10?) — sim/não por item.
- Idioma dos novos: inglês (regra) ou português (como os autorais antigos do deck).

## Como aplicar (quando decidido)
Escrita no Anki só com `from nebli.decks import Anki, escrita; with escrita(Anki(), "edema"): ...` (os decks têm o total no nome, add-on `nebli_decks`; sem o helper cria árvore NEBLI paralela). Cor e motivo por card; conferir por ID; não tocar nos existentes. Scripts modelo na pasta: `apply.py`, `bandeiras.py` (usar `escrita`, não o lock manual).

## Estado dos arquivos da corrida
`E1` do piloto em `e1/` (PDF completo e leve; fonte Typst em `typst-build/_par_pat-05-edema-congestao/`) — **não publicada**, provavelmente com o mesmo excesso clínico; reescrever ao nível da aula antes de publicar. Regra nova: E1 + guia sobem sempre para a pasta da aula no Drive depois de revisados.
