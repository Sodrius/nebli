# ANTI-EXEMPLARES-CARDS.md — o que NÃO fazer

> Catálogo de padrões de card ruins e de **matches falsos** (o card parece cobrir o subtópico, mas não permite reter). Cada item: o padrão, por que é ruim, e o conserto. Sementes da aula embrio-gastrulacao-neurulacao (2026-07-10).

## A1 — Match falso: "conceito similar" contado como cobertura (o que o Davi sentiu)
O subtópico da E1 é **processo**, mas o único card que o toca cobra um **fato de timing/rótulo** adjacente. A rubrica R6 chama isso de nível 1 — não deve contar como "forte".
```
During which week of gestation does the primitive streak appear? {{c1::Week 3}}
```
Por que é ruim como cobertura de "1.2 Linha primitiva, nó e ingressão (EMT)": responde *quando* a linha aparece, não o que ela **faz** (organizador, eixo, simetria, cílios/lateralidade) nem a EMT. O Davi decora a semana e continua sem reter o mecanismo.
**Conserto:** manter o card de timing (é bom no que faz), mas marcar o subtópico como RASO e gerar cards de mecanismo (nó organizador; EMT) — via loop Card→E1 + cards autorais.

## A2 — Card de próxima-aula infiltrado (escopo)
Toca um termo que **é** subtópico da E1 ("tubo neural / neuroectoderma"), mas num nível que a aula não abre — é conteúdo da aula seguinte (organogênese do tubo neural).
```
The embryonic brainstem and spinal cord have a(n) {{c2::dorsally}}-located {{c1::alar}} plate
The alar plate and basal plate are separated by the {{c1::sulcus limitans}}
The neural tube begins as {{c1::three::number}} primary vesicles
```
Por que é ruim: viola R1 (Davi esbarra em "placa alar", "sulco limitante", "vesículas primárias" — nada disso está na E1) e R4 (é próxima-aula, não aprofundamento da atual).
**Conserto:** **drop** (balde FORA). Não é candidato a loop — não force a E1 a abrir a próxima aula.

## A3 — Pegadinha de nível celular fora do escopo do slide
```
What is the embryonic origin of microglia? {{c1::Mesoderm}}   (M icroglia = M esoderm)
What is the embryonic origin of dura mater? {{c1::Meso::Endo/Meso/Ecto}}derm
```
Por que é ruim aqui: oligodendrócito/astrócito/micróglia/dura são embriologia neural fina, clássica de banca Step 1 **mas de outra aula** (histologia/neuro do SNC). A aula é gastrulação→dobramento. Cai em FORA por escopo, mesmo sendo high-yield noutro contexto.
**Conserto:** drop nesta aula; reaproveitar quando a aula do sistema nervoso for curada (mora no deck daquela aula).

## A4 — Card só-Step-2 (fora do alvo do Davi)
Qualquer nota de manejo/tratamento avançado, estadiamento, conduta — tag `#AK_Step2_v12::` ou equivalente.
Por que é ruim: Davi se prepara para o **Step 1** (R7). Step 2 é ruído de pool.
**Conserto:** podar no `prefiltrar_pool.py` **antes** do keep/drop fino.

## A5 — Card não-atômico (dois fatos num cloze só)
```
The foregut runs from the {{c1::lower esophagus}} to the {{c2::proximal duodenum}}, supplied by the {{c3::celiac trunk}}
```
Por que costuma ser ruim: se o Davi sabe uma metade e erra a outra, o card inteiro conta como falha e vira leech. Além disso, limites anatômicos precisos de fore/mid/hindgut podem ser mais fundos que a E1 (que só nomeia as três regiões + irrigação por artéria própria) → checar R6/R1.
**Conserto:** quebrar em cards atômicos **e** confirmar ancoragem na E1; se a E1 não dá o limite anatômico, ou sobe (loop) ou o card sai.

## A6 — Pergunta + resposta solta em vez de cloze AnKing-like
```
Which glial cell is the exception, arising from {{c1::mesoderm}} (monocyte lineage)? {{c2::Microglia}}
```
Por que é ruim: mistura pergunta/resposta com cloze e deixa o card com cara de protótipo. O padrão AnKing-like é uma afirmação curta em que os alvos de recall são os próprios clozes.

Conserto:
```
Microglia are the CNS glial exception: they arise from {{c1::mesoderm}} (monocyte lineage), not neuroectoderm, and function as resident {{c2::macrophages}}.
```

## A7 — Frase que entrega a resposta antes do cloze
```
Anterograde axonal transport (body → terminal) uses {{c1::kinesin}}; retrograde (terminal → body) uses {{c2::dynein}}.
```
Risco: quando a direção, a seta ou a oposição já tornam a resposta óbvia, o card vira reconhecimento passivo. Ajustar para que o cloze cobre o pareamento direção→motor sem pistas redundantes demais.

## A8 — Sequência visual fragmentada em clozes demais
```
The meninges, outside in, are {{c1::dura}}, {{c2::arachnoid}}, and {{c3::pia}}...
```
Por que é ruim: três clozes separados podem virar cartões fáceis e redundantes, cada um entregue pelo restante da sequência. Para sequências curtas, preferir um cloze único da sequência inteira e outro card separado para a relação anatômica/funcional.

Conserto:
```
From superficial to deep, the meninges are {{c1::dura mater → arachnoid mater → pia mater}}; CSF circulates in the {{c2::subarachnoid space}}.
```

## A9 — Redundância entre cards do mesmo slug
Por que é ruim: dois cards quase iguais competem por revisões e não aumentam cobertura. Manter redundância só quando cada card treina uma habilidade diferente: identificação visual, mecanismo, função, origem, clínica ou comparação.

Regra: antes de aplicar lote autoral, rodar uma passada de duplicidade por slug. Se dois cards têm o mesmo alvo e a mesma explicação, fundir, apagar um ou transformar um deles em card visual/IO.

**Duplicata EXATA por re-importação (achado 2026-07-16).** Pior caso de A9: a MESMA nota (texto idêntico sem cloze + mesma imagem, mesmo slug) existe duas vezes porque um re-import/re-add da curadoria recriou o card. No estoque isso apareceu em massa (cards de imagem histológica e de anatomia, cada um em duas cópias). São lixo puro — a cópia não agrega nada. **Conserto:** passada de dedup por assinatura `(slug, texto-sem-cloze normalizado, conjunto de src de imagem)`; manter a nota com histórico de revisão (mais reps), suspender+marcar a cópia (`NEBLI::dup-removido-<data>`, reversível) antes de deletar. **Prevenção:** o apply de curadoria deve casar por texto-bruto do campo 1 e NÃO re-adicionar nota que já existe no slug.

## A10 — A mesma imagem aparece duas vezes na mesma face

Por que é ruim: duplica espaço, distrai e denuncia que o pipeline anexou mídia sem verificar o HTML já existente. A comparação deve ser feita por `src` normalizado e SHA-256 do arquivo; o template renderizado também precisa ser testado para não contar campos ocultos como duplicata visível.

Conserto: manter a primeira ocorrência e remover apenas a segunda ocorrência dentro da mesma nota/face. Reutilizar a imagem em cards diferentes é permitido quando ela agrega a cada recuperação; isso não é o defeito chamado de "imagem duplicada".

## A11 — Manutenção AnkiConnect durante revisão

Por que é ruim: atualizar nota, tag ou fila enquanto o Reviewer está aberto pode recarregar a frente e fazer o card virado "desvirar" antes da nota 1–4.

Conserto: toda rotina mutável consulta `guiCurrentCard` e aborta se houver revisão ativa. Preparar artefatos e decisões fora da coleção; aplicar em lote curto numa janela sem Reviewer e validar depois.

## A12 — Imagem que não bate com o card (o erro nº 1, feedback 2026-07-15)
O defeito mais repetido no lote de feedback do Davi: "imagem não bate com card (padrão para muitos cards)", "imagem incompatível", "imagens estão repetidas", "imagem esquisita". Distinto de A10 (mesma imagem duas vezes na face). Aqui a imagem **existe e é única, mas não treina o alvo daquele card** — foi anexada por ser do tema/aula, não do conceito.
```
Card: Endothelium secretes {{c1::von Willebrand factor}} → platelet adhesion.
Imagem anexada: esquema genérico de camadas do vaso (não mostra vWF/plaqueta).
```
Por que é ruim: a imagem só ajuda a reter se ela **é** o mecanismo que o cloze cobra. Imagem decorativa/de-tema vira ruído, ocupa espaço e mascara a lacuna real. Pior quando a mesma figura de tema é colada em 5 cards diferentes ("repetidas").
**Conserto (regra dura):** só anexar imagem se ela treina o alvo **específico** daquele cloze. Nunca deixar a automação colar imagem de nível-aula sem conferência card-a-card. Na dúvida, `img::substituir` (marca a lacuna) **em vez** de shippar imagem errada — card sem imagem > card com imagem errada. Cards de anatomia/histologia com localização (meninges, córtex/medula do timo) são o caso onde vale caçar/recortar a imagem certa, muitas vezes como **Image Occlusion** (ver A16).

## A13 — Card sem Extra (comentário breve do porquê)
Davi: "faltou aqui um comentário explicando o que é isso, para caso eu tivesse esquecido… veja para todos os cards quais têm isso"; "todo card tem que ter imagem + breve comentário, ou pelo menos a grande maioria". Implementa R9 como item auditável, não só como diretriz.
Por que é ruim sem Extra: quando o Davi esquece o conceito, o card testa mas não **reensina** — ele fica travado sem a 1 frase que reancora ("o que é TCR?"). O Extra é a rede de segurança que separa reter de decorar cego.
**Conserto:** todo card leva Extra de 1–2 frases, voz NEBLI, dando o *porquê*/o-que-é (não repetir a frase da frente). Passada de auditoria antes de aplicar: listar cards do lote com Extra vazio → preencher.

## A14 — Cloze sem dica de tipo quando o tipo não é inferível
Davi: "dentro do cloze poderia estar escrito (processo) para eu saber que o cloze de dilatação era um processo, algo que não dava para saber sozinho".
```
Ruim:  …relaxes medial smooth muscle → {{c2::vasodilation}}.
Bom:   …relaxes medial smooth muscle → {{c2::vasodilation::process}}.
```
Por que importa: sem a dica, o Davi não sabe se o alvo é uma estrutura, um processo, uma célula ou um número — e erra por ambiguidade, não por não saber. A dica (`::process`, `::cell`, `::number`, `::enzyme`…) delimita o espaço da resposta como os cards AnKing fazem.
**Conserto:** usar `{{c1::resposta::dica}}` sempre que o *tipo* do alvo não estiver óbvio pela frase. Não usar dica quando ela entregaria a resposta.

## A15 — Excesso de tags
Davi: "você também adicionou tags demais pros cards, o que pode ser um problema".
Por que é ruim: tag-bloat suja o Browse, infla o dessuspender por tag e cria ruído de manutenção. O card precisa da tag-âncora da aula (`NEBLI::<slug>`) + as poucas tags funcionais do pipeline (image_status, visual_need, source) — não de uma nuvem de tags temáticas redundantes.
**Conserto:** manter o conjunto mínimo. Ver `normalize_tags` no fechamento de feedback (`fechar_feedback_*.py`) como referência do enxoval canônico; podar o resto.

## A16 — Card de localização anatômica/histológica sem Image Occlusion
Davi, sobre o card córtex/medula do timo: "típico card onde IO ficaria ótimo, uma oclusão apontando pra uma palavra que está apontada pro córtex e outra pra medula numa foto do timo". E, sobre meninges: "é o tipo de card que precisa muito de imagem".
Por que texto puro falha aqui: "outer/dark" vs "inner/pale" é relação **espacial** — decorar em texto não transfere pra prova/lâmina. IO treina o reconhecimento visual real.
**Conserto:** quando o alvo é *onde* uma estrutura fica numa imagem, preferir Image Occlusion (modelo IO do deck) a cloze de texto. Recortar a figura do deck de histologia/anatomia importado.

## A17 — Card em português (ou PT+EN misturado)
Feedback 2026-07-16, o mais repetido do lote: "card em português + inglês, deveria ser só inglês"; "todos os erros aqui devem ser checados em todos os cards". Reforçado: **todos os cards sempre em inglês, ÚNICA exceção = cards de etimologia** (origem de termo, que naturalmente discute a palavra em PT). Contradiz [[regras-neblicard-anking-nivel]] (card é EN). Frente e cloze em inglês; Extra pode ter explicação PT-BR curta, mas o *card testável* é inglês, como AnKing. **Conserto:** traduzir frente/cloze pro inglês; auditoria em TODO o deck caçando `[ãõçáâàéêíóôú]` na frente (exclui os de etimologia). Card elogiado só por estar em PT ("gostei, só faltou inglês") = traduzir e manter.

## A18 — Enumeração fatiada em cards redundantes (refina A8)
Feedback 2026-07-16: túnicas do vaso, camadas das meninges, B vs T, capilar fenestrado/sinusoide, astrócito proto/fibroso — "pode ser 1 card só", "diminuir redundância". Um conjunto paralelo (3 camadas, 2 tipos irmãos) vira **um card que cobra o conjunto**, não N cards quase iguais competindo por revisão. Duas mecânicas válidas: mesmo número em cada item (`{{c1::dura}} {{c1::arachnoid}} {{c1::pia}}` → 1 card, lembra os três juntos) OU `c1/c2/c3` quando faz sentido testar cada slot — mas **nunca** um card separado por membro do conjunto. O inimigo é a redundância, não o nº de clozes. Par contrastante (B matura na medula / T no timo) = 1 card com 2 clozes, não 2 cards.

## A19 — Tag usada como TODO ("resolver depois")
Feedback 2026-07-16: "esse monte de tag é ruim, tem que focar em resolver o problema, não ficar colocando tag pra resolver depois". Refina A15: tag não é lembrete de defeito pendente. Se o card tem problema, conserta agora; não empurra com `NEBLI::visual_need::` etc. como marcador. Enxoval mínimo de tag = só âncora da aula + o que o pipeline realmente usa.

## A20 — Formatação padrão-NEBLI em vez de AnKing-like
Feedback 2026-07-16: "formatação ainda está no padrão NEBLI, todos têm que ficar tipo AnKing". O card não é prosa NEBLI reduzida — é afirmação curta e seca no estilo do deck AnKing (frente enxuta, cloze no alvo, Extra com o porquê). Ver EXEMPLARES-CARDS.md.

## A21 — Erro factual ou card que não renderiza
Feedback 2026-07-16: "esse card faz sentido? não seria mitose?" (conteúdo incorreto) e "esse card deu problema e não apareceu" (cloze quebrado). **Conserto:** todo card passa por checagem de veracidade (bate com a E1/bibliografia?) e de render (o cloze fecha, aparece no estudo). Card factualmente duvidoso volta pra prancheta antes de dessuspender.

## Gate-hard de imagem×card — CONSTRUÍDO 2026-07-16 (`flashcards/scripts/verificar_imagem_card.py`)
Davi pediu "um gate-hard que só passa se a imagem fizer sentido com o card". A ideia inicial de "1 subtópico por imagem" **não basta**: os cards ruins já estão no subtópico certo e a imagem continua errada — o defeito é semântico. O gate tem 3 camadas: **L0** reuso determinístico (mesma imagem em alvos diferentes = suspeita; achou 43 no estoque); **L1** juiz multimodal Claude vision (MATCH/WEAK/MISMATCH + detecta print-de-texto); **L2** ação (MISMATCH → tira `<img>` + `img::substituir`; MATCH → `NEBLI::img_gate::ok`). **Sempre que um card novo com imagem for criado, rodar `verificar_imagem_card.py --nid <id>` antes de dessuspender** (hook do apply/pré-ship). Três assinaturas de falha catalogadas: figura de visão-geral de capítulo em card específico; print de texto virando imagem; mesma imagem reusada em cards não relacionados. **Autonomia (Davi 2026-07-16):** ele para de comentar card-a-card; eu identifico e conserto defeitos proativamente, inclusive sem comentário.

## Checklist pré-ship — rodar em TODO card antes de aplicar / dessuspender
Este é o gate operacional. Nenhum card autoral entra no deck (nem card AnKing é dessuspendido) sem passar por aqui. Cada "não" para o card.

**Escopo e conteúdo**
- [ ] A resposta está numa frase da E1 desta aula? (R1) — senão: loop ou drop
- [ ] É desta aula, não da próxima? (R4/A2)
- [ ] Não é só-Step-2? (R7/A4)
- [ ] Cobra mecanismo, não só rótulo/timing? (R6 — sobe o nível)

**Forma do card**
- [ ] Frente e cloze em **inglês**? Sem PT ou PT+EN misturado (A17)
- [ ] Estilo AnKing (afirmação seca), não prosa NEBLI (A20)
- [ ] Um fato atômico? Se são 2 fatos independentes, viram 2 cards (A5) — "informação desnecessária de vir juntos"
- [ ] Conjunto/enumeração = 1 card que cobra o conjunto, sem cards-irmãos redundantes (A18)
- [ ] Conteúdo factualmente correto e o cloze renderiza no estudo? (A21)
- [ ] É afirmação com cloze, não pergunta+resposta+cloze? (A6)
- [ ] A frase **não** entrega a resposta fora do cloze (leitura passiva)? (A7); enumeração curta = cloze único, não 3 clozes redundantes (A8)
- [ ] Cloze tem `::dica de tipo` quando o tipo não é óbvio? (A14)
- [ ] Tem Extra de 1–2 frases com o porquê/o-que-é? (A13/R9)
- [ ] Tags no mínimo canônico, sem nuvem temática? (A15)

**Imagem**
- [ ] Se tem imagem: ela treina o alvo **específico** deste card? (A12) — imagem de tema/aula não conta; na dúvida `img::substituir`, não shippar errada
- [ ] A mesma imagem não aparece duas vezes na face (A10) nem repetida à toa entre cards do slug
- [ ] Card de localização anatômica/histológica: considerou Image Occlusion? (A16)

**Redundância**
- [ ] Não repete outro card quase igual do mesmo slug — redundância só fica se cada card treina habilidade diferente (A9)
