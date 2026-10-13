# Revisão de qualidade — BT03 Estrutura do estômago (UC08 P1)

**Aula / run / versão:** BT03 · `uc08-bt03-20260929a` · `selection_hash b2f15afe20e608c8`. E1 não se aplica.
**Fontes:** texto do slide (o PDF de 15 MB baixa só como texto, então as figuras do slide não foram vistas); roteiro prático completo (5 páginas); Junqueira cap. 15 pelas figuras 15-14 a 15-21 com legendas (PDF do livro não aberto); AnKing, Histology e LLU. Prova: não localizada. Detalhes em `fontes.json`.

## Alvos e recorte
Matriz em `matriz-objetivos.tsv`. O deck cobre parede → esôfago/junção → regiões → fosseta/istmo → tipos celulares (parietal, colo, principal, enteroendócrina/grelina), na ordem do slide.
- **Fora, com motivo:** boca/língua/dente/salivares (slides iniciais, sem objetivo no roteiro: **pergunta a Davi**), desenvolvimento em rato, bariátrica, organoides/Troy+ e a lista de produtos das mucosas do colo.
- **Fronteira P2:** o card de fator intrínseco, as células G/gastrina e a barreira muco-bicarbonato ficam para FI05. O c2 do AnKing de parietais pode ser reativado na mesma nota.
- **Pendente:** transição estômago–duodeno (roteiro, estudo complementar) sem candidato adequado; o duodeno é da BT04.

## Seleção e redundância
11 AnKing, 6 Histology e 2 LLU; nenhum autoral. Os cards do Histology vêm como listas longas com 4–9 clozes e glossários laterais. Nas cópias, cada um foi reduzido ao tópico do alvo, com um cloze selecionado; títulos errados foram corrigidos e a figura Junqueira pertinente ficou no verso (tudo registrado em `curadoria`). Pares inversos e imagens de menor aumento foram excluídos (lista em `plan.json`).

## Precisão
- **Correção científica:** o verso do AnKing 1486608745216 atribuía a eosinofilia da parietal ao fator intrínseco. Foi corrigido para mitocôndrias e membranas (Junqueira 15-17).
- LLU "células-tronco na região mucosa do colo" foi ajustado para istmo–colo, conforme o roteiro.
- O card das mucosas do colo omite a forma do núcleo, porque o Histology diz "redondo" e o roteiro diz "triangular".

## Retenção
6 verdes e 15 azuis. Núcleo: muscular da mucosa, epitélio do esôfago, junção esofagogástrica, parietal → HCl, parietal eosinófila, principal → pepsinogênio. A principal basófila ficou azul por ser dedutível do contraste com a parietal (Q4B). Identificação de regiões em HE, ultraestrutura e grelina também ficaram azuis.

## Tradução e visual
PT-BR aplicado; inglês arquivado em `translation-plan.json`. Mnemônicos em inglês preservados com glosa (Parietal = Pink; CHIEFs … BASe). Dois nomes válidos registrados (fosseta/fovéola, principal/zimogênica, parietal/oxíntica). Renderização WebKit de frente e verso das 21 sem vazamento e com imagens legíveis. Rótulos embutidos continuam em inglês.

## Instalação
Deck `NEBLI::UC08::P1::Biologia Tecidual::Estrutura geral do estômago`, preset da raiz. 19 notas novas / 21 cards; readback sem problemas (`receipt.json`), sync pelo `escrita()`. Nenhum compartilhado com a FI08: os cards de plexo e camada da FI08 cobram outros alvos.

**Estado do conteúdo:** revisado pelo executor; aguarda revisão Codex. Parcial por não ter visto as figuras do slide nem o PDF do Junqueira.
**Estado técnico:** verificado.
**Acesso:** Mac User 1; tablet não verificado.
**Contabilidade:** 19 notas, 21 cards novos (AnKing 12 cards, Histology 7, LLU 2), 0 autorais, 6 verdes, 15 azuis, 0 incertos, 0 suspensos.


---

## v3 — correção após F-C44 (29/09, mesma corrida)

BT03 antiga tinha 35 cards e a v2 tinha 21. **v3: 37 notas / 49 cards (19 AnKing, 13 Histology, 2 LLU, 3 autorais), 19 verdes e 30 azuis.** As notas de cárdia/piloro, istmo e canalículo foram recriadas (sem revisões) para eliminar cards órfãos de clozes antigos.

| Critério de Davi | Decisão concreta nesta aula |
|---|---|
| Todos os AnKing do assunto; irmãos preservados | Parietal c1–c4, principal c1–c3, eosinófila/basófila nas duas direções, as três subcamadas da mucosa. Voltaram submucosa e muscular externa (ordem), serosa e adventícia, Meissner/Auerbach por camada, glândulas do corpo, muco/HCO₃⁻, pepsinogênio→pepsina. |
| Histology sem lista com título (F-C44) | 13 notas do Histology reescritas em **uma frase** com a figura do Junqueira no verso: junção, rugas, fundo = corpo, cárdia/piloro, mucosas superficiais, istmo, canalículo, mucosas do colo, dente, parótida, sublingual, submandibular, língua ventral. |
| Calibrar com vídeos (Q5/Q6) | Osmosis, Stomach: Histology: regiões (fundo = corpo; piloro com fossetas em metade da mucosa), camada oblíqua, rugas, istmo (parietais), colo (mucosas do colo e células-tronco), base (principais e enteroendócrinas). Ninja Nerd SNE: quatro camadas e subcamadas. Todos esses pontos têm card. |
| Identificação visual (Q3/Q12) | Novo card com imagem na frente (célula parietal apontada, imagem de card AnKing) e dois LLU de região em HE. |
| Boca/dente (Davi 29/09: "incluir poucos, azuis") | Cinco azuis: tecidos do dente (3 clozes), parótida serosa, sublingual mucosa, submandibular mista, face ventral da língua. |
| Autoral mínimo | Três autorais: camada oblíqua, fossetas profundas no piloro, identificação da parietal. Cada um tem lacuna registrada. |
| Verde por motivo | 19 verdes: plano da parede e ordem das camadas, epitélio do esôfago e junção, fossetas, cárdia/piloro mucosas, parietal (local, HCl, FI, eosinófila, imagem), principal (pepsinogênio, basófila). |
| Bibliografia | Junqueira cap. 15 pelas figuras 15-14 a 15-21 com legendas (o PDF do Drive não abre pelo conector). Limite declarado. |


**Tradução — revisão independente (agente revisor, 29/09):** 74 cards EN × PT comparados; fluidez 8/10, fidelidade 9/10. Aplicados na v3c: pistas removidas da frente (mucosas superficiais/do colo, fossetas pilóricas, dente, língua); decalques corrigidos ("infecção protozoária" → protozoose, "estômago oxíntico" → região oxíntica, "sulcos" → depressões, "pontes em trava" → mecanismo de trava); absolutos atenuados (cárdia/piloro "poucas ou nenhuma" parietal; reflexos longos "p. ex." vagovagais); REG no lugar de RER; mnemônico cinase/fosfatase adaptado ao PT (C→Contrai, F→Flácido) em vez de glosa; "parede do tubo digestório" padronizado. Sync e readback limpos após as correções; render conferido.
