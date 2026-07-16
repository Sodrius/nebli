# CARD-MIRROR — rubrica viva (o que faz um NEBLIcard parecer AnKing-nativo)

> Depósito permanente do aprendizado do loop adversarial. Cada linha nasceu de um **tell** que o discriminador `card-mirror` pegou e o refinador corrigiu. Esta é a spec de geração: NEBLIcard novo deve satisfazer tudo aqui **antes** de entrar e passar por `lint_neblicard.py`.

## Regras aprendidas (por rodada)

### Rodada 0 — baseline (2026-07-12)
- **[IMAGEM] Nunca usar slide de PowerPoint como imagem.** Slide colorido, 4:3, 3000×2250, com título em português = tell gritante. → Reusar a **imagem-mãe de um card AnKing irmão** do mesmo tema (nativa, inglês, ~1080px, leve, já no dispositivo). Fonte na ordem: outro card AnKing > internet limpa > recorte de slide (último recurso, resize p/ ~1080px). *Também conserta o lag: imagem já cacheada não baixa.*
- **[IDIOMA] Corpo do card em inglês.** AnKing é inglês; português no Text/Extra denuncia na hora.
- **[MODELO] Usar o note type AnKingOverhaul.** Herda a ergonomia visual (cor do cloze, reveal do Extra, responsividade) idêntica aos 500M de cards validados. Modelo NEBLI genérico tem CSS/tamanho diferente = tell.
- **[SELO] O selo `❖ NEBLIcard` é a ÚNICA marca permitida.** Discreto, gold mudo, rodapé do verso. Fora dele, zero diferença de manufatura.

### Rodada 1 (2026-07-12) — 5/5 pegos, conf ~85%, veredito distinguível
Tells estruturais fatais corrigidos:
- **[REFERÊNCIA] Nunca citar banca/curso no corpo.** "FMUSP P2/2023", "taught in the course", "classic yields taught" = assinatura autoral imediata. A proveniência de prova vive na tag/curado.json, nunca no card visível.
- **[CRÉDITO] Reusar a imagem de irmão implica herdar o crédito dela.** AnKing carrega "Photo credit: Image licensed by Physeo…". Card com imagem Physeo mas SEM o crédito = híbrido denunciável → adicionei o crédito real (a imagem é Physeo, então blenda e é honesto).
- **[MARCAS] Sem travessão "—", aspas curvas "" nem reticências.** São assinatura de prosa autoral. Usar pontuação reta.

### Rodada 2 (2026-07-12) — 5/5 pegos, conf ~80%, "só a textura do verso denuncia"
- **[VOZ — a regra-mãe] O Extra é ANOTAÇÃO, não EXPLICAÇÃO. Card ≠ E1.** O tell que sobreviveu a tudo foi a voz: prosa de monitor com conectivos causais ("The −2 comes from…", "hence the…", "It only describes…") vs. o fragmento nominal telegráfico do AnKing ("Carnitine acyltransferase-2 (CAT2)", "e.g., ALT or AST"). Reescrever todo Extra como fragmento: nomes, setas →, ponto-e-vírgula, sem oração completa nem conectivo. É o reflexo mais difícil de quebrar porque a voz de monitor é a voz canônica da E1.

### Rodada 3 (2026-07-12) — ≈ indistinguível: 2 falsos-positivos, conf ~65%, "chute informado"
- O discriminador passou a **errar cards AnKing reais** (chamou 2 de vazio-Extra de "NEBLI minimalista") e declarou chute nos meus de lipídeo. Convergência atingida para os eixos manejáveis.
- **Resíduo aceito (inerente ao conteúdo):** o verso de contagem de ATP (#10) lista números que o AnKing não carda — não há como escondê-lo sem perder o fato FMUSP. Fica.
- **Resíduo menor não perseguido:** o par de aminoácidos divide a mesma imagem Sketchy (o discriminador leu como "par autoral"), mas cards AnKing também compartilham imagem — over-fitting ao discriminador não valeria a pena.

### Treino de GERAÇÃO — glicogênio, 50 cards (2026-07-12) — convergiu em 3 rodadas
Prova de que dá pra *gerar* do zero, não só consertar. Curva: 15/9 distinguível → confuso (3 falsos-positivos, pegou 1/12) → **0/12 pegos, 46% de acurácia (abaixo do acaso), discriminador confessou indistinguibilidade.**
- **[CRÉDITO — a string EXATA] Reusar imagem AnKing = herdar o crédito literal e completo dela.** Não basta "Photo credit: Physeo"; a assinatura nativa é `Image licensed by Physeo and used with permission. Purchase full access here.` — inclusive o CTA comercial. Meia-string foi o tell que sobreviveu à rodada 2. (Em produção, ver ressalva ética abaixo.)
- **[IMAGEM POR SUBTÓPICO] Uma imagem-mãe por SUBTÓPICO, não por tema.** Glicogênio tem 2 pools nativos: doenças de depósito → `8412e62f…`, fisiologia → `efa5f694…`. Usar a errada denuncia.
- **[VOCABULÁRIO NATIVO] Adotar o "menu" de formatos do AnKing, não inventar.** Card de doença: `"X disease is also known as glycogen storage disease type {{c1::…}}"`; pergunta embutida: `"Which…? {{c1::…}}"`; mnemônico com capitalização interna (`PomPe/PumP`, `One Gierke`, `ABCD`); hint de cloze `{{c1::x::opção1 ou opção2}}`. Usar esse vocabulário faz o card sumir na multidão.
- **[VERSO] Confirmado que a glosa telegráfica de 1-4 palavras + crédito é 100% nativa** ("Reversible.", "Uses Pi, not water.", "Signals low energy.", "By phosphoglucomutase.").

## IMAGE OCCLUSION (note type `IO-one by one`) — rubrica (2026-07-12)

Loop adversarial estendido para IO. Pipeline de geração: `flashcards/scripts/io_from_slide.py` (imagem limpa rotulada → OCR tesseract por+eng, upscale 2-3× → clustering por proximidade "um rótulo = uma caixa" → campo I0 com caixas justas → preview PNG p/ validação visual). Fonte de imagem liberada por Davi (2026-07-12): **pegar boa imagem rotulada da internet** (atlas/Blausen/OpenStax/Wikimedia, EN, alta-res) — melhor que o slide 4-em-1 do professor tanto em qualidade quanto em indistinguibilidade. Slide do professor só quando a figura específica dele for cobrada.

### Rodada 1 IO (2026-07-12) — 4 cards (1 NEBLI neurônio + 3 AnKing), discriminador acertou 4/4, meu NEBLI pego conf 82
Tells de manufatura corrigidos → viram spec de geração:
- **[ASSET — o tell nº1] Nome de arquivo = hash de conteúdo, idêntico em Image e Extra.** AnKing usa `<md5/sha>.png/.svg` (`b9d02a5f…`, `paste-08ef…`). Nome descritivo (`neuron-test-crop.png`) ou divergência entre o `src` do campo Image e o do Extra = tell imediato de card em construção. → `io_from_slide.py` agora salva a imagem como `<md5>.png` e emite `image_field` com esse mesmo nome; o Extra, se referenciar a imagem, usa o mesmo hash.
- **[EXTRA] IO tem Extra vazio OU fragmento telegráfico seco — nunca bullet explicativo.** AnKing IO ou não tem Extra, ou traz `<div><b>- termo:</b> fragmento</div>` sem conectivo, ou o SVG-gabarito + `<span style="font-size:8pt;">Last updated: <Mês DD, AAAA></span>`. Extra com mecanismo embutido ("high Na channel density", "action potential initiation") lê como E1 = tell. → Para card de identificação de estrutura, **preferir Extra vazio** (é o mais nativo) ou glosa de 1-3 palavras por estrutura.
- **[HEADER] EN nominal curto com `<b>/<u>` no termo-chave.** Nunca PT, nunca pergunta, nunca prosa.
- **[GEOMETRIA] Caixas justas de altura uniforme (~27px numa figura ~700-1000px; escala com a DPI).** O pipeline reproduz isso sozinho via OCR + clustering. Validar sempre no preview antes de aplicar.
- **[RESÍDUO ACEITO] Volume de caixas.** 11 oclusões numa figura rica (neurônio completo) ficou acima da mediana AnKing IO (~4-6), e o discriminador citou como tell fraco. É inerente ao conteúdo (a figura TEM 11 rótulos) — não perseguir. Se incomodar, dividir a figura em 2 notas temáticas (soma vs projeções), como o AnKing faz "uma imagem-mãe por subtópico".

### Rodada 2 IO (2026-07-12) — CONVERGIU: 0/1 pego, meu card lido como AnKing conf 91
Card de neurônio regenerado com os 3 fixes (nome hasheado idêntico Image/Extra, Extra vazio, imagem atlas EN via OCR+clustering). Discriminador **fresco** marcou os 4 como ANKING; o meu (#3) passou como nativo conf 91, com "tells" que são elogios ("imagem-mãe de neurônio reutilizável", "padrão AnKing clássico apaga-o-label-não-o-mecanismo", "11 oclusões sobre labels EN de 1-3 palavras"). Ele chegou a dizer ao refinador que um NEBLI-IO *teria* PT/prosa/slide — viés do carimbo, estado-alvo do GAN. **IO indistinguível alcançado em 2 rodadas.**

| Rodada | NEBLI pego | Conf | Falso-positivo | Veredito |
|---|---|---|---|---|
| 1 | 1/1 | 82 | 0 | distinguível (filename + Extra didático) |
| 2 | 0/1 | 91 (lido como AnKing) | meu card | ≈ indistinguível |

### Discriminador endurecido (2026-07-12) + tell de PROVENIÊNCIA
Davi apontou que o discriminador estava fraco (rodada 2 colapsou para "tudo AnKing" cometendo a falácia "sem tell autoral → logo AnKing"). Endurecido no `.claude/agents/card-mirror.md` § Rigor: veredito ANKING exige **impressão digital positiva** (não ausência de defeito), **proveniência de imagem é evidência de 1ª classe**, **ranking relativo obrigatório**, confiança calibrada. Re-teste: o juiz endurecido **pegou** o card de neurônio (conf 68) pelo tell de proveniência.
- **[PROVENIÊNCIA — novo tell forte de IO] A imagem tem que sair de uma biblioteca que o AnKing usa** (Sketchy, Pixorize, Physeo, OpenStax, atlas clássico Netter/Sobotta/Grey's, UWorld, SVG desenhado). Render 3D avulso / Blausen / Wikimedia genérica / figura de blog = suspeito, mesmo limpo e EN. Para histologia isso é fácil: micrografia H&E de OpenStax (que o AnKing usa de fato). Escolher a fonte pensando "de qual biblioteca AnKing isso sairia?".

### Checklist de conformidade IO (antes de aplicar)
- [ ] Imagem = atlas/textbook limpo EN, alta-res, fundo neutro (não slide PT 4:3). Nome = hash de conteúdo.
- [ ] `Image` e o `src` do Extra apontam o MESMO arquivo hasheado.
- [ ] Header EN nominal com `<b>/<u>`; sem PT, sem pergunta.
- [ ] Extra vazio OU fragmento telegráfico (opcional: `Last updated:` span). Nunca mecanismo explicativo.
- [ ] I0: uma caixa por rótulo, justa, altura uniforme — conferido no preview PNG.
- [ ] Note type = `IO-one by one (AnKing Step Deck / AnKingMed)`.
- [ ] Crédito da imagem honesto (Wikimedia/OpenStax/Blausen → a string real da fonte), na página de créditos ou no Extra conforme a fonte.

## Meta — a hierarquia de tells (o "como fazer", aprendido no loop)
Os tells vazam em 3 camadas, da mais barulhenta à mais sutil. Conserta-se de cima pra baixo:
1. **Estrutural/mecânico** (imagem: fonte + tamanho + **string de crédito exata**; note type AnKingOverhaul; idioma inglês). É o que o discriminador pega primeiro e com mais confiança. Resolvido → a acurácia dele despenca.
2. **Vocabulário de formato** (comprimento do cloze, sintaxe de hint `::`, formato de mnemônico, pergunta-vs-afirmação, imagem por subtópico). Não inventar: copiar o menu nativo.
3. **Voz** (Extra = anotação telegráfica, NUNCA prosa de monitor; sem travessão/aspas curvas/referência a banca). É a camada mais sutil e a que os meus reflexos de E1 mais vazam — **card ≠ E1**.
O movimento vencedor de imagem: **reusar a imagem exata do card irmão + a string de crédito exata dele.** O movimento vencedor de voz: **fragmento, não frase.** Quando as 3 camadas batem, o discriminador não só erra — ele fica *confiante* de que o card é AnKing (viés do carimbo), e passa a marcar AnKing real como suspeito. Esse é o estado-alvo.

> **Ressalva ética (produção):** copiar o CTA comercial "Purchase full access here." faz sentido no TREINO (medir indistinguibilidade) e quando o card reusa a imagem Physeo real. Em cards de produção, manter o crédito honesto da imagem que de fato foi usada; não inventar atribuição para imagem que não é daquela fonte.

## Checklist de conformidade (estado atual)
Um NEBLIcard passa se:
- [ ] Imagem = card AnKing irmão (ou limpa EN ~1080px); nunca slide PT; peso leve.
- [ ] Text e Extra em inglês.
- [ ] Note type = AnKingOverhaul.
- [ ] Cloze single, branco de ~1–3 palavras no token de maior valor (não oração inteira).
- [ ] Frente ~10–20 palavras; a frase dá a pista de recuperação sem entregar o branco.
- [ ] Extra = **fragmento telegráfico** (nomes, →, ponto-e-vírgula), NÃO prosa de monitor com conectivos. Card ≠ E1.
- [ ] Sem travessão "—", aspas curvas "" ou reticências … (assinatura de prosa autoral).
- [ ] Sem referência a banca/curso no corpo ("FMUSP", "taught in the course"); proveniência só na tag/curado.json.
- [ ] Se reusa imagem de card irmão, herda a **string de crédito EXATA da FONTE daquela imagem** — Physeo → "Image licensed by Physeo and used with permission. Purchase full access here."; OpenStax → "Photo credit: OpenStax, CC BY 4.0"; foto/Wikimedia/Flickr → "Photo credit: <autor>, <licença>, via <site>". Crédito trocado entre fontes = tell.
- [ ] (Robustez extra, opcional) variar o formato de alguns cloze: multi-cloze c1/c2/c3, hint `::`, mnemônico-acrônimo, pergunta "What/Which?". Cards autorais 100% single-cloze simples podem, num lote muito rico, destoar por *excesso de simplicidade* (tell fraco, ainda não pegou).
- [ ] Só o selo `❖ NEBLIcard` distingue; tag `NEBLI::gerado` para auditoria.

## Métrica de convergência (loop 2026-07-12, aminoácidos+lipídeos)
| Rodada | NEBLI pegos | Conf. média | Falsos-positivos | Veredito |
|---|---|---|---|---|
| 1 | 5/5 | ~85% | 0 | distinguível (tells estruturais) |
| 2 | 5/5 | ~80% | 0 | distinguível (só o verso) |
| 3 | 5/5 (chute) | ~65% | 2 | ≈ indistinguível (resíduo inerente ao conteúdo) |

## Set de calibração de 50 AnKings + validação de competência (2026-07-13)
Davi pediu: "dá uns 50 ankings variados pro discriminador estudar, senão ele não sabe o que é AnKing". Feito:
- **`flashcards/ANKING-DOSSIE-TEXTO.md`** — 50 cards AnKing reais, estratificados por 17 buckets (FirstAid, UWorld, B&B, Physeo, Pixorize, AMBOSS, Sketchy, OME, Bootcamp, Step1+Step2). Gerado por `flashcards/scripts/extrair_dossie_anking.py` (seed 42).
- **`flashcards/ANKING-DOSSIE-IO.md`** — 5 IO reais + imagens exportadas em `arquivos-trabalho/io/anking/`. AK-IO-01 é anatômico (ramos da a. maxilar, line-art EN) — prova que IO de anatomia AnKing é vetorial, não foto.
- card-mirror § PASSO 0 agora **obriga ler os dois dossiês antes de julgar** (julgar de memória = inválido).

**Correção de rubrica forçada pelos exemplares:** a regra "Wikimedia/Blausen = suspeito de autoral" estava ERRADA. O AnKing USA Wikimedia/OpenStax/Blausen — o tell é a **linha de crédito formatada** (`Photo credit: <autor>, CC BY-…, via Wikimedia Commons`), não a fonte. Card com imagem de banco público SEM linha de crédito = autoral. (Confirmado por HELDOUT-1 e HELDOUT-3, ambos AnKing com Blausen/Wikimedia + crédito.)

**Validação de competência (lote cego held-out, seed 99):** 6 cards (4 AnKing reais + 1 texto autoral craft meu + 1 IO meu). Resultado: **5/5 de texto certos** — pegou meu texto autoral (#2) conf 94 pelo Extra em prosa causal ("because… without it…"), e cravou os 4 reais como ANKING **com impressão digital positiva** (fórmula de mnemônico, separador ·, crédito Blausen, fonte OpenStax). Meu IO (#5) passou como ANKING conf 90 (indistinguível — alvo). Confiança calibrada (68 no card básico sem fonte forte). **O revisor deixou de cravar por "ausência de defeito" e passou a cravar por "impressão digital positiva" — que era o pedido do Davi.**

### Rodada P3 (2026-07-13) — deck de histo/anato PT rated 6/10: indução fraca + voz E1

Auditoria fix-oriented do card-mirror (Opus) sobre os 159 cards P3. Diagnóstico-mãe: **a maioria testa RECONHECIMENTO, não recall** — o nome da estrutura está no stem (em negrito) e o cloze apaga a *descrição*; ler o nome entrega o branco. É a inversão exata do craft AnKing (apaga o NOME, a descrição é a pista). Regras que o rebuild deve satisfazer:

INDUÇÃO (a regra-mãe do recall):
- **[NAME-NÃO-NO-STEM]** Se o card testa uma ESTRUTURA/TERMO, o nome é o cloze — nunca aparece (menos ainda em negrito) no stem enquanto a descrição é apagada. Padrão AnKing: stem = descrição/propriedade; cloze = o nome de maior valor.
  - ERRADO: `O neurônio **multipolar** tem {{c1::vários dendritos e um único axônio}}`
  - CERTO: `Which neuron has one axon + multiple dendrites? {{c1::Multipolar}}`
- **[SEM-PARÊNTESE-QUE-ENTREGA]** Proibida a lista de exemplos ou o sinônimo entre parênteses no stem quando ela dá o branco de graça. Número que revela o nome (três cúspides → tricúspide) = mover o número ou o nome para cloze irmão.
- **[CLOZE-ATÔMICO ≤3 palavras]** Branco = 1-3 palavras de maior valor. Span de 4+ palavras-conteúdo é dump: dividir em c1/c2/c3 (um fato por branco) ou encurtar ao token que carrega a informação. Lista de N itens → N clozes, não um só.
- **[UM-FATO-POR-CARD]** Fatos independentes (funções de 3 células T; 5 sítios sem linfático) viram cards separados OU multi-cloze atômico — nunca um branco só.
- **[PERGUNTA-QUANDO-IDENTIFICA]** Para "qual estrutura faz X", usar o formato AnKing "Which/What…? {{c1::Nome}}" (AK-05, AK-24, AK-29) em vez de afirmação-com-nome.

VOZ (Extra = anotação, card ≠ E1) — reforço específico deste deck:
- **[SEM-FRASE-COMPLETA no Extra]** Zero orações narrativas, zero aforismo de monitor ("Quem vem de onde prevê o que a célula faz", "O engano mais comum da aula"). Extra = fragmento nominal, →, ;, = (AK-14 "UV-B for sunburn"; AK-47 "instability = overactivity = random spasms"). Ou vazio. Ou imagem + `Last updated:`.
- **[SEM-REFERÊNCIA-À-AULA]** "erro clássico da aula", "erro comum de identificação" = voz autoral; cortar.

IDIOMA:
- **[EN nativo, não tradução literal]** Traduzir para o registro AnKing, não palavra a palavra. Eponímia PT-específica sem uso EN (ângulo de Pirogoff) → usar o termo que o AnKing/Step1 usa (Nissl bodies OK).

IMAGEM (histo) + IO (anato — o buraco maior):
- **[EXTRA COM IMAGEM]** Card de histologia carrega micrografia H&E no Extra (fato no Text, imagem no Extra) — hoje 0 cards têm imagem.
- **[ANATOMIA SUBCARDADA E SEM IO]** Toda estrutura anatômica identificável (câmaras, valvas, ramos da aorta, troncos linfáticos, círculo de Willis) deve ter IO. IO anatômico AnKing-grade: line-art/atlas EN (estilo AK-IO-01), uma caixa por rótulo (~27px), Header EN nominal, asset hasheado, Extra vazio/seco.

QC de conteúdo achado na auditoria (corrigir ANTES de cardar):
- **3 listas conflitantes** de "sítios sem linfáticos" entre os arquivos (vessels#24: SNC/medula/cartilagem/osso/placenta · anato-I#26: cartilagem/epiderme/córnea/polpa · anato-sistema#5: cartilagem/epiderme/córnea/SNC). Reconciliar 1 lista canônica.
- **~6 duplicatas de anatomia** a dedupar no deck combinado (ducto torácico, ângulo venoso, ramos do arco, sistema porta).

### Rodada cega P3-rebuild EN (2026-07-13) — 13/16; meus 8/8 pegos, 3 AnKing reais errados
Lote cego: 8 cards EN meus (rebuild P3) + 8 AnKing reais. Discriminador (exemplar, sem rulebook) pegou **todos os 8 meus** (conf 55-85) e **errou 3 AnKing reais** (chamou de NEBLI). Aprendizado que fica:

- **TELL REAL nº1 (consertar sempre): mecanismo dentro do STEM da frente.** "sealing passively by their nest shape", "since lymph flows with no heart to push it" DENTRO da pergunta. Nenhum dos 50 exemplares faz isso — front AnKing pede o fato, o mecanismo vai pro Extra ou some. É o separador mais confiável. Consertado nos 4 cards pegos.
- **TELL REAL nº2: cloze de frase-mecanismo (5+ palavras)** ("electrically insulates atria from ventricles") em vez de token. Reestruturar pra apagar 1 token.
- **TELL REAL nº3: cloze que se autoentrega** (apagar sigla com a expansão visível na mesma frase: "Mucosa-associated lymphoid tissue is {{c1::MALT}}").
- **TELLS-RUÍDO (NÃO são discriminadores — AnKing real também faz):** Extra abrindo com "Thus", crédito com citação/DOI longa, Extra que reafirma a frente. O juiz errou 3 AnKing reais (#4/#13/#15) justamente por superpesar esses. Não perseguir.
- **FEATURE DELIBERADA (não é defeito): Extra explicativo.** Davi já decidiu (meta-aval P3): Extra que explica o porquê é **recurso desejado** nos cards dele. Ser "pego" por isso é OK — não achatar todo Extra pra fragmento. Consertar só os 3 tells reais acima; manter a voz explicativa quando ela ensina.

Estado-alvo honesto: meus cards são bons mas ainda distinguíveis pelo tell nº1. Uma passada removendo mecanismo do stem fecha a maior parte do gap sem sacrificar a didática do Extra.

## Fonte de imagem por tipo de card (após ver a prova P3, 2026-07-13)
A prova prática P3 = **micrografia H&E real com seta numerada** → identificar estrutura (`arquivos-trabalho/FMUSP-ESTILO-UC02.md`). Consequência:
- **Histologia:** IO sobre **micrografia H&E** (Junqueira 12ed), gênero NEBLI legítimo (PT, micrografia) que o AnKing não tem — a indistinguibilidade vale para a *manufatura* (caixas, asset, Extra), não para forçar EN/esquema. Micrografia-com-seta **não sai de OCR** (sem texto sobre a estrutura) → precisa de modo de gerador que posiciona oclusão sobre a estrutura + nome no Extra/gabarito (a construir).
- **Anatomia:** line-art/atlas EN (estilo AK-IO-01) — OCR funciona.
- **Embriologia:** cloze de texto (AnKing cobre) + IO de corte transversal para fases esquemáticas.
