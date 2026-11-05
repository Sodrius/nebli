# GUIA 1 — Regras: como Davi quer cada card

## Rodada diária de 05/11 — prevenção vigente

- Coração de gostei usa #_flag nativo, mede sua geometria visível e mantém posição segura sem bandeira; testar oito combinações de largura/bandeira/gostei e conferir a janela real. `qualidade_comentarios.badge_layout_ok` reprova ausência, sobreposição e saída da tela.
- Negrito de organizador deve permanecer visível no critério de cada linha, além do título; `qualidade_comentarios.negrito_contexto` bloqueia destaque ausente ou escondido no cloze. O significado discriminante do destaque ainda exige leitura humana.
- Organizador tem eixo comum e alvo essencial em cada linha; reduzir carga retirando qualificadores repetidos, sem esconder detalhe secundário nem expor nome cognato da resposta. Exemplos: HST1793784421465 e GLP-1/PYY1793476864207.
- Não recolocar iniciais retiradas por Davi nem usar inicial de sigla curta como dica; `spec_lib.dicas`, `gates.inducao_clozes` e `verificador_casos.forma_das_lacunas` respeitam a preferência literal local, sem dispensar revisão de indução.
- Novas seleções não incluem fontes marcadas Only_Step_2; a presença de uma tag Step2 junto de Step1 não prova exclusividade. `qualidade_comentarios.step2_only` é gate duro antes da instalação. A retirada de1793803589750 foi expressamente pedida; não chamar uma palavra de conduta de critério automático para qualquer card.
- Imagem precisa mostrar o objeto ou mecanismo cobrado, e seus rótulos precisam continuar legíveis no render real em390px. Nome de arquivo não prova anatomia. Verificar também o CSS do modelo: tabela a6,63px reprova mesmo que o HTML declare16px sem!important.
- Analisar X pela função e pela dimensão aprovada; índice editado pelo usuário e organização que ele escolheu prevalecem sobre uniformização estética. Correção do executor não vira exemplar positivo sem X/elogio novo.
- Estatística por formato é descritiva: comparar UC/assunto, fase, intervalo, idade e exposição, registrar tamanho da amostra e reconhecer que formato atual pode diferir do usado em revisões antigas. Não converter tempo ou retenção bruta em lei causal nem mexer no FSRS.

## Feedback de 04/11 — alvo essencial e figura limpa

- **Gate de organizador:** antes de aprovar cada linha, declarar o eixo comum, a informação a recuperar e por que é a mais importante. Com o cloze tapado, a pista deve conduzir à resposta por efeito ou mecanismo, sem revelar por inicial ou outra linha. Se o agente principal ficar visível e a lacuna esconder detalhe secundário, reprovar. Exemplo 1793784421465: `IV: T cells activating {{c1::macrophages::m…}}` → `IV · direct cytotoxicity or macrophage activation: {{c1::T cells}}`. Em 1793476864207, `{{c1::GLP-1::G…}}` → `L cell · satiety and slower gastric emptying: {{c1::GLP-1}}`. O alvo exige julgamento humano no verificador por casos; `verificador_casos.forma_das_lacunas` bloqueia inicial de sigla curta.
- **Fonte da figura fica no registro da corrida, sem legenda visível abaixo da imagem.** `imagens_cards.fontes_visiveis_sob_imagem` reprova `<img ...><br><small>Aula/slide/Fonte…</small>`. Exemplo 1793199677071: retirar `<small>Aula MB60, slide 22…</small>`.
- **Duplicata coberta por organizador:** manter suspenso o avulso 1792695020938 (HA isolada), pois 1792695019915 já contrasta HA e NA por entrada e saída.
- **Comando de imagem:** conferir se a figura real mostra exatamente o alvo do cloze, ler seus rótulos e medir a resolução antes de remover a marcação; preferir o painel da aula ou uma fonte identificada. Uma foto genérica ou uma lâmina de texto não resolve o pedido. O verso deve manter a imagem legível em largura responsiva.
- **Comando de comentário ou escrita:** reparar a operação de recuperação na frente e explicar no verso o passo causal que faltava, com poucas linhas; não remover a marcação só porque há um texto anterior. Se o card já tinha sido corrigido e o pedido remanescente está atendido, conferir no vivo antes de limpar a tag.
- **Indicador de gostei:** manter o coração fora da área da bandeira em todas as escalas; conferir no Anki depois de reiniciar o add-on e registrar a inspeção visual antes de fechar o comentário.

Ler os quatro guias INTEIROS antes de escrever ou revisar qualquer card (gate `exemplares_lidos`, v10 com a leitura obrigatória inteira de `gates.LEITURA_OBRIGATORIA`): este (regras), `GUIA-2-EXEMPLARES.md` (modelos), `GUIA-3-ANTI.md` (erros) e `GUIA-4-AULA.md` (o deck inteiro: entender a aula, exemplo × princípio). Tudo aqui saiu dos comentários literais de Davi (`comentarios-cards.jsonl`; 451 casos analisados no guia vivo em 31/10/2026) e dos cards que ele marcou com X. O histórico completo, nota a nota, fica em `GUIA_CARDS.md` (consulta, não leitura obrigatória).

A pergunta de todo card: **"isso agrega algo no conhecimento ou está só para ficar bonito?"** Um bom card **explica algo e ajuda a decorar** — o processo e o nome, juntos (custo-efetividade).

## 1. Que cards entram

- **Cobrir a aula inteira.** "Sinto que faltou informação no deck como um todo." Todo item do slide, do quiz e das provas tem card ou motivo escrito para ficar fora. Deck raso é o erro mais caro.
- **AnKing e acervos primeiro**, todos os irmãos; autoral só para lacuna provada. O AnKing é o modelo de forma: "os do AnKing são melhores".
- **Cobertura vem antes do teto de autoral.** "Avalia se a aula toda tá coberta, que é mais importante que o teto de 30%." Quando o acervo não cobre: buscar de novo com sinônimos em todos os acervos, juntar em organizador, e só então autoral — mesmo acima de 30%. Nunca cortar item da aula para caber no teto.
- **Aula certa.** "Aula errada para esse card", "isso é mais de anato". O que é de outra aula vai para ela (ou entra associado, sem repetir).
- **Básico antes de clínica.** "Quero aprender a base bem." Clínica é **um card por doença**, com a informação que Davi sempre vai associar a ela ("resistência à insulina na DM, skip lesion em Crohn"), não uma ficha da doença.
- **Sem repetição.** "Dois cards para a mesma coisa, suspender o outro." Dois cards parecidos se confundem: ou se fundem, ou cada um ganha uma resposta diferente (IL-2 × IL-12). O aspecto secundário vai para o verso de outro card — "diminui a quantidade de cards sem diminuir a quantidade de informação".
- **Mais conteúdo por card quando é um conjunto.** "Pode ter mais de um cloze por card, estilo tópico, assim economizamos cards." Conjunto da aula vira organizador (seção 4), não N cards avulsos.
- **Ordem de criação:** a necessidade (lacuna da aula) chama o card; depois se justifica o formato. Nunca criar o card e inventar a justificativa.
- **Autoral inspirado no exemplar do mesmo tipo de informação (F-20261103-CODEX-01):** perguntar o que o card quer ensinar e qual exemplar aprovado pede a mesma operação de memória. Usar a taxonomia e os nids do GUIA-2; copiar a relação, o contexto e o alvo, adaptando o conteúdo da aula. Registrar tipo, exemplar, semelhança e adaptação no `REVISAO-AUTORAIS.md`. Semelhança visual ou mesmo número de lacunas não basta.
- **Aprender com as suspensões:** comparar cards estudados e depois suspensos com os que ficaram ativos na mesma aula. Registrar o trecho da aula, a função do card, duplicatas e o comentário correspondente. Se a suspensão veio de troca de deck, fase da prova ou retirada do pipeline, não tratá-la como juízo de qualidade. Usar apenas padrões sustentados para ajustar a próxima seleção.
- **Evidência das suspensões de 31/10:** o retrato mostra que autorais da UC08 foram suspensos com mais frequência que os AnKing estudados da mesma UC, enquanto a UC19 passou por troca de deck. Esta diferença orienta a auditoria, mas não prova a causa de cada suspensão. O caso pró-B/pré-B/imatura (avulsos suspensos → organizador pedido por Davi) é evidência direta para preferir um card de comparação quando a aula ensina um conjunto.

## 2. A frente

- **Frase AnKing:** curta (8–19 palavras), afirma um fato concreto, faz sentido sozinha ("um card tem que fazer sentido sozinho"). Situar o assunto quando não é óbvio: "faltou falar que era sobre embrio", "tem que deixar claro que é o cérebro".
- **Cloze no que se decora**, não no que se entende: nome específico, molécula, estrutura, número que a aula dá. Nunca verbo, adjetivo ou palavra genérica que o resto da frase completa ("cloze em algo que não é para ser decorado, mas entendido").
- **Uma resposta só.** "Há outra resposta possível: B7 e CD28 — tem que ser uma única resposta." Se cabe sinônimo ou outro item, reescrever ou pôr dica de categoria.
- **A frase não entrega a resposta**: nem por oposição ("há a resposta por oposição aqui"), nem por irmão visível, nem por termo já escrito antes do cloze ("card tem a resposta nele mesmo"). Teste: tapar o cloze e ver se dá para acertar **sem saber**. Acertar por contexto é indução ruim.
- **Contexto na frente, não só no deck:** dizer “granuloma” antes de falar do anel de linfócitos T, “entrada viral” antes de “uncoating”, “glândula gástrica” antes de diferenciar suas células e o vírus específico antes de citar neuraminidase. O gate `check_v10_feedback` confere os dois primeiros padrões e clozes mal fechados; os demais dependem de leitura humana.
- **Cloze curto:** até 3 palavras ("se há mais de 4 palavras no cloze tem que mostrar uma ou o tanto que for para o cloze ser de no máximo 3"); de preferência no fim da frase.
- **Sem "x ou y" no cloze nem na frase.** "Duas palavras não aumentam o valor pedagógico, só atrapalham." Quando a pergunta é ambígua, **dica curta de categoria** dentro do cloze, mostrada antes de tentar: `{{c1::ileocolic::SMA branch}}`, `::part of duodenum`, `::phase`. Exceção: alternativa visível só se Davi a deixou de propósito.
- **Sigla nunca sozinha**: nome por extenso junto ("de novo, sigla só o card"); a expansão vai no verso quando a sigla é o alvo (NLS).
- **Linguagem de livro, simples e rigorosa:** "simplicidade e rigor valem mais"; nada de "subset", palavras abstratas ou expressão forte e ambígua ("quem não tem intrinsic activity? receptor ou antagonista?").
- **Sem ";" nem rótulo com ":" no meio da frase** ("tipo de card ruim, com ponto e vírgula"); 3+ itens numa frase viram organizador.
- **Sem absolutos falsos** (never, all, every, any): a frente pode esconder generalização; a ressalva vai no verso.

## 3. Negrito

- **Gate duro em todo autoral**, conferido card a card: "negrito tem que ser gate hard, checado card a card".
- Padrão AnKing: 1–2 termos que **situam** o card (o universo, a condição), **fora do cloze**, distribuídos pela frase — "faltou distribuir negrito e não deixar só no título". Itálico/sublinhado como no AnKing quando ajudam.
- Quando Davi edita o negrito ("coloquei um negrito, aprende isso"), aquele é o modelo: localiza o universo e deixa visíveis os atributos que induzem a resposta.
- **Revisão de negrito e sublinhado (1792788316281):** o revisor aponta o trecho exato e sua função: negrito situa o contexto ou a ação que continua visível; sublinhado destaca um contraste ou detalhe que ajuda a distinguir a resposta; a lacuna não recebe negrito manual. Reprovar destaque só no título, destaque ornamental e destaque que entrega a resposta. Exemplo: `<b>gastric</b>` dentro de `{{c1::...}}` → `<b>stomach distension and nutrients</b>` fora de `{{c1::gastric}}`; em `1792788316281`, sublinhar `cover its activation domain` explicita o mecanismo que induz `coactivators`.

## 4. Organizador

- **Quando a aula compara ou enumera** — "card organizador serve precisamente para isso: comparar coisas diferentes e organizar na minha cabeça as ideias". Todo deck termina respondendo: **há organizador onde deve haver?**
- **Em pé**, título que diz o que organiza, uma linha curta por item (≤ 26 palavras), sem numeração deitada: "tópicos mal escritos, tem que ficar em pé, tipo os cards de constrição esofágica".
- **O cloze é o que deve ser lembrado** em cada linha; o critério de cada item fica visível e induz.
- **Índices:** o mesmo c1 para um conjunto que se recupera junto; grupos reais em c1/c2 ("agrupa 2 clozes por card"). 3+ itens no mesmo índice recebem dicas apenas quando não revelam o alvo. Siglas curtas nunca recebem inicial. Respeitar retirada de iniciais pedida por Davi, registrando a fala em `dicas_preferencia_davi` (≥30 caracteres); gerador e gates preservam essa exceção local.
- **Classificação com fonte**, nunca inventada: "esses cards organizadores não podem ter classificação inventada por você, tem que ter uma fonte". Não misturar critérios para fabricar um conjunto.
- Ao criar o organizador, **aposentar os avulsos** que ele cobre (suspender, sem apagar).

## 5. O verso (comentário)

- **Profundo, mas pequeno:** "eles têm que ser profundos, mas pequenos, porque se não nem leio". 1 a 3 linhas curtas; em tópicos quando é lista ("comentário tem que estar em tópicos aqui").
- **Diz o porquê ou a consequência** que a frente não diz: "o bom card tem o porquê no comentário"; "comentário só repete o card — poderia ser tanta coisa: por que ele é assim, o que causa, alguma relação dele com qualquer coisa útil".
- **Explica o termo que pode estar obscuro** (o que é somestésica, B-1, invariant chain, nanquim = India ink, right crus) e **a diferença para o vizinho que confunde** (CD40 × B7, DNMT1 × reader–writer, folículo × centro germinativo).
- **Agrega algo real do assunto**: "comentário poderia falar do morcego, não essa baboseira"; "comentário pode agregar algo sobre a doença realmente".
- **Ordem ou sequência pedida vai no verso**, em linhas (contínuo → fenestrado → sinusoide).
- **Forma:** sem travessão, sem excesso de ";" e ":", sem cara de IA; nunca embaixo da imagem; dois enters de espaço depois da última coisa escrita.

## 6. Imagem

- **Real** (livro, slide, AnKing, Kenhub), nunca esquema inventado, e **direcionada**: "uma boa imagem tem pouca informação, mas direcionada em específico para o card".
- Mostra **exatamente o que o card cobra** ("imagem não me ajuda a entender o que é o canaliculus" = trocar). Só o gráfico cobrado: "quebra ao meio a imagem, assim fica mais atômico".
- **Tamanho legível no celular**, com espaço entre comentário e imagem; sem rolar demais. Renderizar o card depois de fazê-lo.
- Card de conceito visual (curva, anatomia, histologia, embriologia) **sai com figura**; card que não precisa não leva ("não precisa de imagem aqui, ficou excessivo").
- **Indicação de figura pelos comentários (1791630174044, 1793199677071):** quando a resposta depende de localização, direção, forma, sequência espacial, curva ou reconhecimento de célula/tecido, procurar primeiro figura real da aula ou fonte identificável. Na revisão, comparar a pergunta com o alvo da figura; recortar o painel relevante, deixar uma linha de espaço e usar largura responsiva (`width:100%;max-width:850px;height:auto`) quando a fonte permitir. Medir a largura real do arquivo e conferir no render do celular: ampliar CSS não recupera detalhe de imagem pequena. Exemplo: ribossomo ocultado pelo riboswitch em `1791630174044` recebeu o painel de tradução do slide 11; foco viral em `1793199677071` trocou a figura de 380 px pelo recorte legível do slide 22.
- **Gate de imagem:** `nebli.imagens_cards.imagens_batem` decide pertinência; `nebli.imagens_cards.imagens_legiveis` aponta figura com largura fixa pequena ou arquivo de origem insuficiente. O parecer visual só aprova depois de conferir foco e leitura no render do celular.
- Tabela comparativa é ótima para conjuntos (papilas, glândulas salivares).

## 7. Estrutura (Kenhub / oclusão)

- Seta na estrutura destacada (verde) e o **nome no cloze ao lado**; o cloze nunca cobre a estrutura ("o cloze obstrui minha visualização da estrutura").
- O rótulo fica onde está a estrutura, para não olhar para outro lugar; só o nome em português; seta conferida.

## 8. Idioma, cor e Tab

- **Idioma:** inglês, como o AnKing. Anatomia (UC07, UC08 anatomia): **frente em português, Extra em inglês**.
- **Cor:** HY 1–2 do AnKing e pilares da aula verdes; detalhe rosa ("esse tipo de card é para ser rosa", "card HY rosa, tem que ser verde").
- **Tab:** texto corrido com storytelling, do básico ao aprofundamento, explicando o porquê (nunca lista 1, 2, 3, 4).

## 9. Como trabalhar com o que Davi faz no Anki

- **Rodada de comentários em sete passos** (gate `nebli.rodada_comentarios verificar`): ver os novos → reavaliar similares → por que teve o problema → prevenção definitiva (gate + indicação precisa + exemplo) → anotar em exemplares, anti-exemplares e guia → corrigir todos (comentário e comando) → aplicar de volta e sincronizar.
- Comentário corrigido recebe `CORRIGIDO, data.` embaixo; o comentário nunca é apagado.
- **Toda edição manual de Davi é lição**: ver o que mudou, por que melhora, e virar exemplar ("melhorei o card, aprende").
- **Todo comentário entra no guia:** preservar a fala literal e registrar o estado anterior, a alteração verificada ou a pendência, e o critério aprendido. Comentário de interface não certifica o conteúdo do card; elogio de uma dimensão não aprova as demais.
- Corrigir um card = corrigir **todos os similares** com o mesmo defeito; um erro já apontado não pode voltar.
- Bandeira vermelha = trocar algo no card e devolver a bandeira anterior. q/w/e/r = comandos (imagem, comentário, escrita, vários) a cumprir na revisão; X = gostei.
- Formatação final conferida por agente ao fim de todo deck, e o deck é renderizado (PC e celular).

### Indicações verificáveis desta rodada (03/11)

- **Organizar estímulos e comparações antes de multiplicar avulsos.** Procurar todos os cards do mesmo conjunto, expor um critério visível por linha e recuperar nomes curtos juntos; exemplo: estímulo gástrico/duodenal → gastrina/secretina/CCK em 1790999836655.
- **Reescrever a lacuna no alvo específico e preservar a indução.** Contexto e mecanismo ficam visíveis; termos genéricos, negativos acumulados e frases longas pedem reescrita; exemplo: syncytium versus granuloma em 1793301692166.
- **Conferir figuras reais contra o alvo e a escala exibida.** O pedido de imagem exige figura focal, legenda de origem, largura responsiva e inspeção da resolução original; exemplo: 1793199677071 saiu de 380 px fixos para o painel do slide 22.
- **Conferir a seta no próprio tecido e nos vizinhos anatômicos.** Cor de destaque não prova o nome; identificar vasos e ductos pela posição/continuidade antes de responder; exemplo: 1792713393203 foi suspenso porque a seta aponta o ducto.
- **Elogio e pergunta sobre seleção exigem inspeção do conjunto.** Registrar o atributo elogiado ou o inventário de cards, distinguir duplicata de aprofundamento e responder no card; exemplo: 1792695019915 validou o organizador HA × NA.
- **Pedido de interface exige instalação e teste na revisão.** Código copiado não demonstra posicionamento nem funcionamento no Anki aberto; exemplo: o indicador de gostei de 1792787231967 depende de recarregar o complemento e conferir sua posição junto à bandeira.

## 10. Rodada de comentários de 01/11: o que virou regra (F-20261101-CLAUDE-04)

- Rodapé do card não mostra nada; bandeira e comando ficam só na bandeira e nas tags (Davi 01/11). Exemplo: antes: 'verde: levar para a vida · comando: escrita ruim' no rodapé → depois: rodapé vazio.
- Elogio de Davi (melhorei, boa imagem, top, aprende) vira caso do banco de casos que deram certo e recebe VISTO. Exemplo: 'melhorei' em 1792713394868 → caso do banco CASOS-QUE-DERAM-CERTO, comentário com VISTO, 01, 11, 26..
- Lacuna curta e decorável: no máximo 3 palavras, de preferência 1 ou 2, num nome; nunca verbo ou expressão abstrata (gate forma_das_lacunas). Exemplo: {{c1::nonhomologous end joining (NHEJ) enzymes}} → error-prone {{c1::nonhomologous end joining}}; {{c1::few selective targets}} → few virus-specific {{c1::targets}}.
- A resposta não pode estar visível nem sair do nome ou da sigla na frente; o gate confere o literal, o verificador confere tradução e oposição. Exemplo: 'Mushroom-shaped papillae… {{c1::fungiform}}' → 'papillae… with taste buds on their upper surface… {{c1::fungiform}}'.
- Verso sem rótulo 'Aplicação:'; sigla com o nome por extenso; negrito fora da lacuna; organizador com uma linha por item iniciada por hífen. Exemplo: '<b>Aplicação:</b> espirometria mede…' → 'A espirometria mede…'; 'use SAM' → 'use S-adenosylmethionine (SAM)'.
- Correção já pedida por Davi não volta: o termo que ele corrigiu muda na frente e no verso (-trofia = desenvolvimento). Exemplo: '-trofia refere-se à {{c1::nutrição}}' → 'Em atrofia e hipertrofia, -trofia indica {{c1::desenvolvimento}} do tecido'.
- Figura real recortada no alvo: esquema desenhado (.svg) reprova; recorte sem texto cortado nem título de outro slide; card visual sem figura reprova. Exemplo: influenza-ha-na-20261031.png (desenho) → mb58-na-slide134-20261101.png (painel 'Neuraminidase activity' do slide 134).
- Card que não ensina, repete outro ou traz pista que só vale fora do Brasil sai do deck (retirado, sem apagar) quando outro card já carrega o conteúdo. Exemplo: 'Mississippi and Ohio river valley… {{c1::Histoplasma}}' → retirado; o nicho (fezes de morcego e ave) já está em 1791630905344.

### Rodada de 01/11 (b)

- Organizador como os de Davi: lacuna primeiro, critério de 3 a 8 palavras com o verbo em negrito; conjunto pequeno num índice só, nunca um cartão por item. Exemplo: '- {{c1::polyprotein}} / - {{c2::protease}} frees RdRp / - {{c3::(-)}} strand' → '- one {{c1::polyprotein::p…}} / - viral {{c1::protease::p…}} frees the RNA-dependent RNA polymerase / - a {{c1::negative::n…}} strand'.
- Card de processo diz o que a estrutura é e de onde vem, numa frase só; o verso dá a exceção (herpes: membrana nuclear). Exemplo: 'Before budding, viral envelope {{c1::glycoproteins}} are inserted…' → 'The envelope of a budding virus is a patch of host {{c1::membrane}} carrying viral glycoproteins'.
- A figura mostra exatamente o que a lacuna cobra: título = maior diluição que ainda aglutina, lido na tabela de diluições, não numa foto da placa. Exemplo: mb60-ha.png (placa) → mb60-titulo-ha-slide44-20261101.png (diluições 1/2 a 1/1024 e título por paciente).
- Card de achado diagnóstico como o de Davi: contexto 'diagnostic finding of <doença>' visível, lacuna no nome do achado, sinônimos no verso com a figura. Exemplo: 1791628675571: 'The diagnostic finding of chromoblastomycosis is brown, thick-walled {{c1::sclerotic bodies}}' + 'muriform cells or copper pennies'.
