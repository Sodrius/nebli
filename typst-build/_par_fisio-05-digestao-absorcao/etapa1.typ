#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Comer não é ainda nutrir-se. O amido, as proteínas e as gorduras do prato são moléculas grandes demais para atravessar a parede do intestino, e o trabalho do tubo digestório é duplo: quebrá-las em peças pequenas, a *digestão*, e levar essas peças do lúmen ao sangue ou à linfa, a *absorção*. As duas tarefas acontecem quase no mesmo lugar, a superfície do intestino delgado, e dependem do mesmo motor, o gradiente de sódio mantido pelo enterócito.

A PARTE I apresenta essa superfície e acompanha os carboidratos até a veia porta. A PARTE II faz o mesmo percurso com as proteínas e com os lipídios, que saem por um caminho diferente, a linfa. A PARTE III trata do que vem junto: os nove litros de água que passam pelo tubo todos os dias, os íons, o ferro, o cálcio, as vitaminas e a via que corre entre as células.
]

#parte-title("PARTE I — A superfície que absorve e os carboidratos", primeira: true)

#subtopico("1.1 — O epitélio absortivo e as duas vias de travessia")

A digestão dos macronutrientes começa no estômago, sob a secreção gástrica, e se completa no intestino delgado, onde chegam as secreções do pâncreas e a bile. A absorção, porém, é quase toda intestinal, e a razão é geométrica: a mucosa multiplica sua área em três níveis sucessivos. As *pregas circulares*, dobras permanentes da mucosa e da submucosa mais desenvolvidas no jejuno, aumentam a área cerca de 3 vezes. Sobre elas se erguem as *vilosidades*, projeções em dedo de luva que multiplicam o resultado por 10. E a membrana luminal de cada célula absortiva, o *enterócito*, é pregueada em *microvilosidades*, que acrescentam outro fator de 20 e formam a #termo-nota[borda em escova][face luminal do enterócito, coberta de microvilosidades e de enzimas digestivas ancoradas na membrana]. Somados os três níveis, a superfície disponível é centenas de vezes maior que a do cilindro original.

#figura-nebli("/figuras/fisio-05-digestao-absorcao/slide-02-epitelio.png",
  largura: 62%,
  legenda: [Os três níveis de amplificação da superfície: pregas (3×), vilosidades (10×) e microvilosidades (20×). Abaixo, à direita, as duas rotas de travessia do epitélio: transcelular (T), através da célula, e paracelular (P), entre as células.])

O epitélio que reveste essa superfície é simples, com uma única camada de células, e heterocelular: enterócitos absortivos convivem com células caliciformes, endócrinas e de defesa. Cada enterócito tem dois lados com proteínas diferentes. A *membrana luminal* olha para o conteúdo do intestino; a *membrana basolateral* olha para o interstício, onde estão os capilares que drenam para a veia porta e o vaso linfático central da vilosidade. Essa assimetria é o que dá direção ao transporte: o que entra por um lado sai pelo outro.

Entre o lúmen e o sangue há dois caminhos. Na via *transcelular*, a molécula atravessa as duas membranas, quase sempre com ajuda de transportadores, e por isso pode ser movida contra seu gradiente. Na via *paracelular*, ela passa entre as células, através das #termo-nota[junções de oclusão][cinturão de proteínas que une células epiteliais vizinhas perto da face luminal e regula o que passa entre elas], e só anda a favor de gradientes. *O ponto fino é que a permeabilidade dessas junções muda ao longo do tubo.* No delgado elas são frouxas e deixam passar água e íons com facilidade; no intestino grosso são apertadas. O delgado é, por isso, o segmento que absorve grandes volumes de forma isosmótica, e o grosso é o que consegue sustentar gradientes e secar o conteúdo.

Antes de tocar a membrana, o nutriente ainda precisa cruzar a *camada de água não agitada*, uma película de líquido quase imóvel retida entre as microvilosidades e o muco. Para moléculas solúveis em água ela é apenas uma etapa de difusão; para os produtos da digestão das gorduras ela é uma barreira real, e a PARTE II mostra como as micelas a contornam.

Dentro do delgado, o *jejuno* concentra a maior parte da absorção. É nele que as pregas são mais altas e as vilosidades mais longas, e é o que mostra o experimento trazido na aula: a mesma substância atravessa a parede do jejuno com fluxo maior do que a do duodeno ou do íleo, e muito maior do que a do cólon.

#mini-resumo[Em uma frase: pregas, vilosidades e microvilosidades multiplicam a área por 3, 10 e 20, e o nutriente cruza o epitélio através da célula ou entre as células, por junções que são frouxas no delgado e apertadas no grosso.]

#subtopico("1.2 — Do amido aos monossacarídeos")

Os carboidratos da dieta chegam em três formas principais: o amido, um polímero de glicose, e dois dissacarídeos, a sacarose do açúcar comum e a lactose do leite. O amido tem duas frações. A amilose é uma cadeia linear de glicoses unidas por ligações α-1,4; a amilopectina tem a mesma cadeia e, a intervalos, ramificações presas por ligações α-1,6. Essa diferença de ligação decide quais enzimas conseguem cortar o quê.

A primeira enzima é a *α-amilase*, secretada pelas glândulas salivares e, mais adiante, pelo pâncreas. Ela é uma endoamilase: rompe ligações α-1,4 no interior da cadeia, não nas pontas, e não toca as ligações α-1,6. O resultado nunca é glicose livre. Sobram *maltose*, com duas glicoses, *maltotriose*, com três, e as *dextrinas α-limite*, fragmentos curtos que guardam um ponto de ramificação que a amilase não conseguiu desfazer.

#figura-nebli("/figuras/fisio-05-digestao-absorcao/slide-04.png",
  largura: 78%,
  legenda: [Digestão e absorção de carboidratos. A amilase corta ligações α-1,4 e produz oligossacarídeos; as oligossacaridases da borda em escova liberam os monossacarídeos, que entram por SGLT1 ou GLUT5 e saem por GLUT2 para o sangue portal.])

Seria natural supor que a amilase salivar trabalha só durante os segundos em que o alimento fica na boca. A distribuição apresentada na aula mostra outra coisa: apenas 3 a 5% do amido é digerido na boca, cerca de 75% no estômago e os 25% restantes no intestino. A enzima salivar é engolida junto com o bolo alimentar e continua ativa no interior dele enquanto o ácido gástrico não penetra a massa. Quando o pH finalmente cai, a amilase é inativada, e o que restou de amido é terminado no duodeno pela amilase pancreática, que já é secretada na forma ativa.

Nenhum desses produtos pode ser absorvido. *O enterócito só transporta monossacarídeos*, e a etapa final cabe às *oligossacaridases*, enzimas ancoradas na própria borda em escova. A *maltase* separa as duas glicoses da maltose. A *α-dextrinase*, também chamada isomaltase, é a que desfaz as ligações α-1,6 das dextrinas. A *sacarase* corta a sacarose em glicose e frutose, e a *lactase* corta a lactose em glicose e galactose. Como essas enzimas ficam presas à membrana, o monossacarídeo é liberado a nanômetros do transportador que vai levá-lo para dentro, sem se perder no lúmen.

A dependência da borda em escova tem uma consequência clínica direta. Quando a lactase falta — por declínio programado depois da infância, o mais comum, ou porque uma doença destruiu as vilosidades — a lactose permanece no lúmen. Ali ela é uma partícula osmoticamente ativa que retém água e produz diarreia; no cólon, as bactérias a fermentam e geram gases e ácidos orgânicos, responsáveis pela distensão e pelas cólicas.

#mini-resumo[Se você só lembrar de uma coisa: a amilase corta α-1,4 e para em oligossacarídeos; quem entrega monossacarídeos é a borda em escova, e sem a enzima certa o açúcar fica no lúmen puxando água.]

#subtopico("1.3 — A travessia dos açúcares pelo enterócito")

Terminada a digestão, restam três monossacarídeos. Nas proporções apresentadas na aula, cerca de 80% é *glicose*, 15% é *frutose* e 5% é *galactose*. Nenhum deles atravessa sozinho a membrana luminal, porque são moléculas polares diante de uma bicamada lipídica, e cada um depende de uma proteína transportadora.

Glicose e galactose entram pelo #sigla("SGLT1", [cotransportador sódio-glicose tipo 1 — proteína da membrana luminal que leva glicose ou galactose para dentro da célula junto com sódio]). O transportador liga dois íons sódio e uma molécula de açúcar do lado do lúmen e os libera no citosol. O sódio desce seu gradiente, porque é escasso dentro da célula, e arrasta o açúcar consigo mesmo quando a glicose já está mais concentrada dentro do que fora. Esse é um *transporte ativo secundário*: o SGLT1 não gasta #sigla("ATP", [adenosina trifosfato — molécula que fornece energia às reações da célula]) diretamente, mas depende do gradiente de sódio. Quem paga a conta é a *bomba de sódio e potássio* da membrana basolateral, que expulsa o sódio para o interstício à custa de ATP e mantém baixa a concentração intracelular.

A frutose segue outra lógica. Ela entra pelo #sigla("GLUT5", [transportador de glicose tipo 5 — proteína da membrana luminal que, apesar do nome, transporta frutose]), um transportador de #termo-nota[difusão facilitada][passagem por uma proteína carreadora a favor do gradiente de concentração, sem gasto de energia], sem sódio e sem capacidade de concentrar. A frutose só entra enquanto houver mais dela no lúmen do que na célula, o que explica por que sua absorção é mais lenta e mais fácil de saturar.

Do outro lado da célula, os três açúcares usam a mesma porta de saída. O #sigla("GLUT2", [transportador de glicose tipo 2 — proteína da membrana basolateral que deixa glicose, galactose e frutose saírem da célula]), também de difusão facilitada, deixa glicose, galactose e frutose passarem para o interstício, de onde entram nos capilares da vilosidade. Esses capilares drenam para a *veia porta*, de modo que tudo o que foi absorvido passa primeiro pelo fígado antes de alcançar a circulação geral.

#confusao-prevista(
  titulo: "SGLT1 e GLUT2 não fazem o mesmo trabalho",
  aluno_acha: [aluno acha que os dois são transportadores de glicose equivalentes, um em cada membrana],
  mecanismo: [o SGLT1 é acoplado ao sódio e consegue concentrar glicose dentro da célula, contra o gradiente; o GLUT2 apenas deixa o açúcar acumulado sair a favor do gradiente. É a combinação de uma entrada ativa com uma saída passiva que garante que o açúcar ande num só sentido, do lúmen para o sangue.],
)

O acoplamento entre sódio e glicose tem uma aplicação que salva vidas. Nas diarreias secretoras, como a da cólera, o intestino perde litros de água e de sal, mas o SGLT1 continua intacto. Oferecer pela boca uma solução com glicose e sódio faz o transportador puxar os dois para dentro da célula, e a água os acompanha por osmose. É o princípio da terapia de reidratação oral, e o detalhe que importa aqui é que ela só funciona com os dois solutos juntos.

#mini-resumo[O que ficou de pé: glicose e galactose entram com sódio pelo SGLT1, a frutose entra sozinha pelo GLUT5, os três saem pelo GLUT2 para o sangue portal, e a bomba de sódio e potássio sustenta todo o processo.]

#parte-title("PARTE II — Proteínas e lipídios")

#subtopico("2.1 — Proteínas: da pepsina à cascata da tripsina")

A digestão das proteínas começa no estômago. As células principais das glândulas gástricas secretam *pepsinogênio*, um precursor inativo que o ácido clorídrico converte em *pepsina*. A pepsina rompe ligações peptídicas no interior das cadeias e funciona apenas em pH muito ácido. Sua contribuição é pequena: responde por 10 a 15% da digestão proteica, e uma pessoa sem estômago continua digerindo proteínas. O papel mais importante da etapa gástrica é outro. Os peptídeos e aminoácidos que ela libera chegam ao duodeno e estimulam as células I da mucosa a secretar #sigla("CCK", [colecistocinina — hormônio do duodeno e do jejuno que estimula a secreção de enzimas pelo pâncreas e a contração da vesícula biliar]), que manda o pâncreas liberar seu suco enzimático; ainda no estômago, esses mesmos peptídeos estimulam a gastrina. Ao mesmo tempo, o ácido que chega com o quimo faz as células S do duodeno liberarem *secretina*, e a secretina manda os ductos do pâncreas secretarem bicarbonato. Os dois hormônios se completam: as enzimas que a CCK libera só trabalham perto da neutralidade, e é o bicarbonato da secretina que cria esse meio.

O pâncreas secreta as proteases como #termo-nota[zimogênios][precursores enzimáticos inativos, que só passam a funcionar depois de terem um trecho da cadeia removido]: *tripsinogênio*, *quimiotripsinogênio*, *pró-elastase* e *pró-carboxipeptidase*. Guardá-las e transportá-las inativas é o que impede o pâncreas de digerir a si mesmo. A ativação acontece só no lúmen do intestino e tem um único ponto de partida. A *enteropeptidase*, enzima da borda em escova do duodeno e do jejuno, converte tripsinogênio em *tripsina*. A tripsina, uma vez formada, ativa os outros três zimogênios e também mais tripsinogênio, numa retroalimentação positiva que o slide marca com o sinal de mais ao lado de cada precursor.

#figura-nebli("/figuras/fisio-05-digestao-absorcao/slide-05.png",
  largura: 78%,
  legenda: [Digestão e absorção de proteínas. Os produtos da pepsina estimulam a CCK, que libera o suco pancreático; a enteropeptidase gera tripsina, e a tripsina ativa os demais zimogênios. No enterócito, peptídeos entram com H#super[+] pelo PEPT1 e aminoácidos por transportadores próprios.])

*Vale fixar essa hierarquia*, porque ela explica um quadro clínico. Na deficiência congênita de enteropeptidase, nenhuma protease pancreática é ativada, embora o pâncreas esteja normal. A criança tem diarreia, não ganha peso e desenvolve edema, porque a proteína da dieta não é absorvida e a albumina do plasma cai.

As proteases pancreáticas deixam no lúmen uma mistura de aminoácidos livres e de pequenos peptídeos. As peptidases da borda em escova encurtam os peptídeos maiores, e o que chega à membrana tem até três aminoácidos. Aqui a absorção de proteínas difere da dos carboidratos: o enterócito aceita o produto ainda não totalmente digerido. Dipeptídeos e tripeptídeos entram pelo #sigla("PEPT1", [transportador de peptídeos tipo 1 — leva dipeptídeos e tripeptídeos para dentro da célula junto com H#super[+]]), um cotransportador que usa o gradiente de H#super[+] em vez do gradiente de sódio. Os aminoácidos livres entram por várias famílias de transportadores, a maioria acoplada ao sódio, separadas conforme a carga e o tamanho da cadeia lateral.

Dentro da célula, *peptidases citosólicas* terminam o serviço e convertem dipeptídeos e tripeptídeos em aminoácidos. São aminoácidos livres, portanto, que deixam a célula pela membrana basolateral e seguem pelo sangue portal até o fígado.

#mini-resumo[Em uma frase: a pepsina digere pouco e dispara a CCK; a enteropeptidase gera a tripsina, que ativa todas as outras proteases; peptídeos entram com H#super[+], aminoácidos com Na#super[+], e do enterócito saem só aminoácidos, pela veia porta.]

#subtopico("2.2 — Lipídios: emulsificar para digerir")

A gordura da dieta é composta sobretudo de triglicerídeos, acompanhados de fosfolipídios e de ésteres de colesterol. O problema que ela impõe ao tubo digestório é físico antes de ser químico: lipídios não se dissolvem em água, e as enzimas que os digerem são proteínas solúveis. Gordura e enzima só se encontram na superfície da gota, e toda a estratégia consiste em aumentar essa superfície.

A digestão começa com duas enzimas de pequeno alcance. A *lipase lingual*, secretada por glândulas da língua, e a *lipase gástrica*, das células principais do estômago, atuam em meio ácido e hidrolisam uma fração pequena dos triglicerídeos. O que elas liberam, porém, tem função de sinal. Ácidos graxos que chegam ao duodeno estimulam a secreção de CCK, e a CCK faz duas coisas ao mesmo tempo: contrai a vesícula biliar, relaxando o esfíncter que fecha a via biliar, e estimula o pâncreas a secretar suas enzimas. Bile e suco pancreático chegam juntos ao lugar onde a gordura está. Os mesmos produtos da lipólise liberam o #sigla("GIP", [peptídio inibidor gástrico — hormônio do duodeno e do jejuno que retarda o esvaziamento do estômago e estimula a secreção de insulina]), que, somado à CCK e à secretina, retarda o esvaziamento gástrico e dá ao delgado tempo para processar a gordura.

A bile traz os *sais biliares*, moléculas #termo-nota[anfipáticas][que têm uma face que se mistura com água e outra que se mistura com gordura], e com eles vem a *emulsificação*. Os sais biliares e os fosfolipídios da bile recobrem as gotas grandes de gordura, e os movimentos de mistura do intestino as fragmentam em gotículas muito menores, que não voltam a se fundir porque estão revestidas. Nenhuma ligação química foi rompida ainda. O que mudou foi a área exposta à água, agora milhares de vezes maior.

#figura-nebli("/figuras/fisio-05-digestao-absorcao/slide-06.png",
  largura: 78%,
  legenda: [Digestão e absorção de lipídios. A lipase gástrica gera os ácidos graxos que estimulam a CCK; bile e suco pancreático emulsificam e hidrolisam a gordura; os produtos chegam ao enterócito em micelas, são reesterificados e saem em quilomícrons para a linfa.])

Sobre essa superfície atuam três enzimas pancreáticas. A *lipase pancreática* retira os ácidos graxos das posições 1 e 3 do triglicerídeo e deixa dois ácidos graxos livres e um 2-monoglicerídeo. A *colesterol-éster-hidrolase* separa o colesterol do ácido graxo ao qual estava ligado. A *fosfolipase A2* remove um ácido graxo do fosfolipídio e deixa um lisofosfolipídio.

A sutileza que se costuma perder é que os próprios sais biliares atrapalham a lipase. Ao recobrir a gotícula, eles deslocam a enzima da superfície. O pâncreas resolve isso secretando a *colipase* — lançada como pró-colipase e ativada pela tripsina, assim como a fosfolipase A2 —, uma pequena proteína que se fixa à interface coberta de sais biliares e serve de âncora para a lipase. Sem colipase, a lipase não alcança o substrato na presença de bile. Um segundo ponto frágil é o pH: a lipase pancreática é inativada em meio ácido, e depende do bicarbonato do suco pancreático para neutralizar o que vem do estômago — é por isso que doenças com excesso de ácido no duodeno cursam com gordura nas fezes.

#mini-resumo[Se você só lembrar de uma coisa: emulsificar é aumentar a superfície, não digerir; quem digere são a lipase, ancorada pela colipase, a colesterol-éster-hidrolase e a fosfolipase A2, todas chamadas pela CCK.]

#subtopico("2.3 — Lipídios: da micela ao quilomícron")

Os produtos da digestão das gorduras — ácidos graxos, monoglicerídeos, colesterol e lisofosfolipídios — continuam insolúveis em água, e entre eles e o enterócito está a camada de água não agitada. A solução é a *micela*. Os sais biliares, acima de certa concentração, agregam-se em partículas minúsculas com as faces hidrofóbicas voltadas para dentro e as hidrofílicas para fora, e os produtos lipídicos se acomodam no interior. A micela é pequena o bastante para difundir pela camada de água e levar sua carga até a borda em escova.

A micela não entra na célula. Junto à membrana, onde o meio é levemente ácido, os ácidos graxos são protonados, perdem a carga e se desprendem. Os produtos lipídicos atravessam então a membrana luminal, parte por difusão simples através da bicamada, parte com auxílio de transportadores, as duas rotas que o slide marca com D e T. Os sais biliares ficam no lúmen, voltam a formar micelas com mais produtos e só são reabsorvidos adiante, no íleo terminal, em cotransporte com sódio. De lá retornam ao fígado pelo sangue portal e são secretados de novo na bile, várias vezes durante a mesma refeição: é a circulação êntero-hepática.

À primeira vista, bastaria agora repetir o que foi feito com açúcares e aminoácidos e lançar os produtos no sangue. O enterócito faz o oposto e reconstrói o que acabou de ser desmontado. No retículo endoplasmático liso, os ácidos graxos são religados aos monoglicerídeos para refazer triglicerídeos, o colesterol é novamente esterificado e os lisofosfolipídios voltam a ser fosfolipídios. Essa *reesterificação* mantém baixa a concentração de produtos livres no citosol, o que preserva o gradiente de entrada, e prepara a etapa seguinte.

Os lipídios refeitos são empacotados com proteínas próprias, as apolipoproteínas, em partículas chamadas *quilomícrons*: um núcleo de triglicerídeos e ésteres de colesterol envolto por uma camada de fosfolipídios e proteína. O quilomícron é exocitado pela membrana basolateral, e aqui está a diferença que organiza toda a absorção. Ele é grande demais para atravessar a parede dos capilares sanguíneos da vilosidade e entra no *vaso linfático central*, cujas células endoteliais deixam fendas largas. Da linfa intestinal, os quilomícrons sobem pelo ducto torácico e caem no sangue venoso perto do coração, sem passar antes pelo fígado. A exceção são os ácidos graxos de cadeia curta e média: solúveis em água, dispensam micela e quilomícron e passam direto ao sangue portal, razão pela qual são usados na dieta de quem absorve mal a gordura.

#confusao-prevista(
  titulo: "Nem tudo o que é absorvido passa primeiro pelo fígado",
  aluno_acha: [aluno acha que todos os nutrientes absorvidos seguem pela veia porta],
  mecanismo: [monossacarídeos e aminoácidos são pequenos e solúveis e entram nos capilares que drenam para a veia porta; os lipídios saem em quilomícrons, que só cabem no vaso linfático. As vitaminas lipossolúveis viajam dentro dos quilomícrons e seguem o mesmo caminho.],
)

A cadeia tem vários elos, e a falha de qualquer um deles produz o mesmo sinal, gordura nas fezes. Falta de bile impede a formação de micelas; falta de enzimas pancreáticas impede a hidrólise; doença da mucosa impede a entrada; e a incapacidade de montar a apolipoproteína do quilomícron deixa o enterócito repleto de gordura que não consegue sair.

#mini-resumo[O que ficou de pé: a micela leva os produtos até a membrana, o enterócito os reesterifica e empacota em quilomícrons, e os quilomícrons saem pela linfa — o único macronutriente que não vai direto ao fígado.]

#parte-title("PARTE III — Água, íons, minerais e vitaminas")

#subtopico("3.1 — Água e sódio: nove litros por dia")

O volume de líquido que o intestino maneja é muito maior do que o que se bebe. A ingestão diária gira em torno de 2 litros, e a ela se somam as secreções do próprio tubo: 1,5 litro de saliva, 2 litros de suco gástrico, 1,5 litro de suco pancreático, 0,5 litro de bile e 1,5 litro secretado pelo delgado. São cerca de 9 litros por dia. O intestino delgado absorve aproximadamente 7,5 litros, o intestino grosso mais 1,4 litro, e apenas uma fração mínima sai nas fezes. A consequência é que uma falha modesta de absorção, em qualquer dos dois segmentos, já aparece como diarreia.

A água não tem transportador ativo. *Ela é sempre absorvida de forma passiva, por osmose, atrás dos solutos.* O enterócito transporta soluto para o interstício, o líquido entre as células fica ligeiramente mais concentrado, e a água o acompanha, pela via transcelular e sobretudo pela paracelular. Ao passar entre as células, o fluxo de água carrega consigo os íons dissolvidos — sódio, potássio, cálcio, cloreto, fosfato —, fenômeno chamado *arraste pelo solvente*. O potássio, em particular, é absorvido no delgado predominantemente por essa via, a favor de seu gradiente químico, que aumenta à medida que a água é retirada do lúmen.

#figura-nebli("/figuras/fisio-05-digestao-absorcao/slide-07.png",
  largura: 80%,
  legenda: [Absorção de íons e água. No intestino proximal (P), o sódio entra acoplado a solutos orgânicos, ao cloreto, a ânions e em troca por H#super[+]; no distal (D), pelo trocador Na#super[+]/H#super[+] e pelo canal ENaC. A bomba Na#super[+]/K#super[+] basolateral mantém o gradiente, e a água segue os solutos.])

O soluto que comanda a absorção de água é o sódio, e o enterócito tem várias portas para ele na membrana luminal. No intestino proximal, o sódio entra acoplado aos solutos orgânicos, como glicose, galactose e aminoácidos; entra junto com cloreto; entra acompanhado de ânions como o fosfato e o iodeto; e entra em troca por H#super[+], pelo *trocador Na#super[+]/H#super[+]*, cuja forma mais importante é a #sigla("NHE3", [trocador sódio-hidrogênio tipo 3 — proteína da membrana luminal que troca um Na#super[+] que entra por um H#super[+] que sai]). No intestino distal, a oferta de nutrientes já acabou, e restam o trocador e o #sigla("ENaC", [canal epitelial de sódio — canal da membrana luminal que deixa o Na#super[+] entrar a favor de seu gradiente eletroquímico]), um canal que permite retirar sódio mesmo de um conteúdo já pobre nele. É no cólon que entra o controle hormonal: a *aldosterona* aumenta o número de canais ENaC e de bombas de sódio e potássio, eleva a absorção de sódio e de água e, em troca, a secreção de potássio. O cólon ainda secreta bicarbonato, e por isso a diarreia intensa leva embora potássio e base.

Todas essas portas dependem da mesma saída. Na membrana basolateral, a bomba de sódio e potássio expulsa o sódio para o interstício e mantém a concentração intracelular baixa, de modo que o íon continue querendo entrar pelo lado luminal. Sem a bomba, nenhum dos cotransportes da aula funcionaria.

O trocador Na#super[+]/H#super[+] merece o destaque que o slide lhe dá. Ele responde pela maior parte da absorção de sódio entre as refeições, quando não há nutrientes para acoplar, e sua ausência congênita causa diarreia com perda de sódio desde o nascimento. O raciocínio é o mesmo da intolerância à lactose, com outro soluto: o que deixa de ser absorvido fica no lúmen e retém água.

#mini-resumo[Em uma frase: dos 9 litros diários, o delgado absorve 7,5 e o grosso 1,4; a água segue o sódio, o sódio entra por cotransportes, pelo NHE3 e pelo ENaC, e a bomba basolateral sustenta tudo.]

#subtopico("3.2 — Bicarbonato, ferro e cálcio")

O bicarbonato do suco pancreático, depois de neutralizar o ácido, é recuperado no jejuno por um mecanismo indireto. O trocador Na#super[+]/H#super[+] lança H#super[+] no lúmen; o H#super[+] combina-se com o bicarbonato e forma ácido carbônico, que a #termo-nota[anidrase carbônica][enzima que acelera a conversão entre ácido carbônico e gás carbônico mais água, nos dois sentidos] converte em gás carbônico e água. O gás carbônico atravessa a membrana livremente, e dentro da célula a mesma enzima refaz bicarbonato e H#super[+]. O H#super[+] volta ao trocador, e o bicarbonato sai pela membrana basolateral com o sódio. O íon nunca atravessa a membrana luminal como tal.

O *ferro* é o exemplo mais claro de um nutriente cuja absorção é regulada, porque o organismo não tem via para excretá-lo. A absorção ocorre no duodeno e no início do jejuno e tem duas entradas. O ferro das carnes vem dentro do grupo heme; proteases o liberam das hemoproteínas, o heme entra por um transportador próprio, o #sigla("HCP-1", [proteína carreadora de heme tipo 1]), e dentro da célula a heme oxigenase solta o ferro. O ferro dos vegetais está livre, na forma férrica, Fe#super[3+], e essa forma não é transportada. Uma redutase da borda em escova, o #sigla("Dcytb", [citocromo b duodenal — enzima que reduz Fe#super[3+] a Fe#super[2+] na superfície do enterócito]), converte-o em ferro ferroso, Fe#super[2+], que entra pelo #sigla("DMT-1", [transportador de metais divalentes tipo 1 — leva Fe#super[2+] para dentro da célula junto com H#super[+]]) em cotransporte com H#super[+].

#figura-nebli("/figuras/fisio-05-digestao-absorcao/slide-09.png",
  largura: 80%,
  legenda: [Absorção de bicarbonato, ferro e cálcio. O ferro heme entra pelo HCP-1 e o não heme, reduzido pelo Dcytb, pelo DMT-1; no citosol é guardado na ferritina ou exportado pela ferroportina, que a hepcidina bloqueia. O cálcio entra por canais TRPV, liga-se à calbindina e sai pela Ca#super[2+]-ATPase.])

A necessidade de reduzir o ferro explica quem ajuda e quem atrapalha. A vitamina C e os peptídeos da digestão mantêm o ferro reduzido e solúvel e aumentam a absorção. Antiácidos e inibidores da secreção gástrica a diminuem, porque o meio ácido favorece a forma ferrosa; cálcio, zinco, cobre e manganês competem pelo mesmo transportador; e a cafeína também reduz a captação.

Dentro do enterócito, o ferro tem dois destinos. Pode ficar guardado na *ferritina*, e nesse caso é perdido quando a célula descama, alguns dias depois. Ou pode sair pela *ferroportina*, o único exportador de ferro da membrana basolateral; uma ferroxidase o reconverte em Fe#super[3+], e é nessa forma que ele se liga à transferrina do plasma. *O ponto de controle é a ferroportina.* O fígado, quando os estoques estão cheios, secreta *hepcidina*, um hormônio que se liga à ferroportina e provoca sua degradação. O ferro fica preso na célula e é eliminado com ela. Com estoques baixos, a hepcidina cai, a ferroportina permanece na membrana, e o próprio enterócito aumenta a expressão de DMT-1 e HCP-1.

O *cálcio* usa as duas vias. Quando a oferta na dieta é alta, boa parte passa entre as células, a favor do gradiente. Quando é baixa, predomina a via transcelular do duodeno: o cálcio entra por canais da família #sigla("TRPV", [canais de potencial receptor transitório vaniloide — canais de cálcio da membrana luminal do enterócito]), liga-se no citosol à *calbindina*, que o transporta sem deixar subir o cálcio livre, e sai pela membrana basolateral, cerca de 80% por uma bomba de cálcio que gasta ATP e 20% por um trocador sódio-cálcio. A forma ativa da vitamina D aumenta a síntese dessas proteínas, e é assim que ela eleva a absorção de cálcio.

#mini-resumo[Se você só lembrar de uma coisa: o ferro entra como heme ou como Fe#super[2+] pelo DMT-1 e só chega ao sangue se a ferroportina estiver na membrana, o que a hepcidina decide; o cálcio transcelular depende da calbindina, e a calbindina depende da vitamina D.]

#subtopico("3.3 — Vitaminas e o caminho da vitamina B12")

As vitaminas se dividem pela solubilidade, e essa propriedade determina o caminho de cada grupo. As *hidrossolúveis* — a vitamina C e as vitaminas do complexo B — comportam-se como os outros solutos polares: entram por transportadores específicos da membrana luminal, saem pela basolateral e seguem pelo sangue portal. Parte do complexo B vem da dieta e parte é produzida pela microbiota intestinal.

As *lipossolúveis* — A, D, E e K — seguem o caminho das gorduras em todas as etapas. Dissolvem-se nas micelas, entram no enterócito com os produtos da digestão lipídica, são incorporadas aos quilomícrons e saem pela linfa. A consequência prática é que tudo o que prejudica a absorção de gordura — falta de bile, insuficiência pancreática, doença do íleo — produz também deficiência dessas quatro vitaminas.

#figura-nebli("/figuras/fisio-05-digestao-absorcao/slide-10.png",
  largura: 80%,
  legenda: [Absorção de vitaminas. As hidrossolúveis (C e complexo B) saem para o sangue portal; as lipossolúveis (A, D, E, K) são incorporadas aos quilomícrons e saem pela linfa. À direita, as etapas da vitamina B12 até o íleo e as três situações que as interrompem.])

A *vitamina K* tem duas origens. A K1 vem dos vegetais; a K2 é sintetizada pelas bactérias do intestino. O recém-nascido reúne os dois fatores de risco: a passagem pela placenta é limitada e o intestino ainda não foi colonizado. Como a vitamina K é necessária para a síntese hepática de fatores da coagulação, a deficiência se manifesta como hemorragia, e essa é a razão da dose aplicada ao nascimento. A varfarina age nesse mesmo ponto, impedindo a reciclagem da vitamina K no fígado, e por isso é um anticoagulante. A *vitamina D* é um caso à parte, porque a dieta não é sua única fonte. Na pele, a radiação ultravioleta converte um derivado do colesterol em pré-vitamina D3, que o calor transforma em vitamina D3. O fígado faz a primeira hidroxilação e o rim a segunda, gerando a forma ativa, a 1,25-di-hidroxivitamina D.

A *vitamina B12* é hidrossolúvel, mas tem um percurso próprio, com quatro etapas em quatro lugares. No estômago, o ácido e a pepsina a soltam das proteínas do alimento, e ela se liga à #termo-nota[haptocorrina][proteína secretada na saliva que se liga à vitamina B12 e a protege do ácido gástrico; também chamada proteína R], que a protege do ácido. No duodeno, as proteases pancreáticas degradam a haptocorrina, e a vitamina livre é capturada pelo *fator intrínseco*, uma glicoproteína secretada pelas células parietais do estômago. O complexo resiste à digestão e percorre todo o delgado. Só no *íleo* terminal existem receptores que o reconhecem e o internalizam.

Cada etapa é um ponto em que a absorção pode falhar, e o slide lista as três situações. Na gastrectomia falta o fator intrínseco, que é a única secreção gástrica indispensável à vida. Na pancreatite crônica faltam as proteases, a haptocorrina não é degradada e a vitamina não chega ao fator intrínseco. Na ressecção do íleo faltam os receptores. *O resultado é o mesmo nos três casos*, uma deficiência que demora anos para aparecer, porque o fígado guarda um grande estoque.

#mini-resumo[O que ficou de pé: hidrossolúveis vão pelo sangue portal e lipossolúveis pela linfa, dentro dos quilomícrons; a vitamina B12 troca a haptocorrina pelo fator intrínseco no duodeno e só é absorvida no íleo.]

#subtopico("3.4 — A via paracelular regulada")

A via paracelular foi tratada até aqui como uma fresta passiva. Os dois últimos slides da aula mostram que ela tem seletividade própria e que sua abertura é controlada pela célula. A barreira entre dois enterócitos vizinhos é a junção de oclusão, formada por proteínas que atravessam a membrana — *claudinas*, *ocludina* e as #sigla("JAMs", [moléculas de adesão juncional — proteínas de membrana que participam da junção de oclusão]) — e por proteínas de sustentação do lado citosólico, as #sigla("ZOs", [proteínas da zônula de oclusão — ligam as proteínas da junção ao citoesqueleto de actina]), que as prendem a um anel de filamentos de actina e miosina logo abaixo da membrana.

As claudinas definem o que passa. Algumas selam o espaço; outras formam poros com preferência por certos íons. No intestino delgado, as claudinas 2 e 15 formam poros para cátions e deixam o sódio atravessar a junção. O sentido desse fluxo é o que surpreende: o sódio passa do interstício de volta para o lúmen.

#figura-nebli("/figuras/fisio-05-digestao-absorcao/slide-11.png",
  largura: 72%,
  legenda: [Claudinas 2 e 15 deixam o Na#super[+] voltar do interstício ao lúmen, onde é reutilizado pelos cotransportadores de solutos orgânicos e inorgânicos. Sem elas, o sódio luminal se esgota e a absorção de nutrientes para.])

O motivo é contábil. Glicose, galactose, aminoácidos, fosfato e outros solutos entram na célula junto com sódio, e a dieta não traz sódio suficiente para acompanhar todos eles. A bomba basolateral lança no interstício o sódio que entrou, e as claudinas 2 e 15 o devolvem ao lúmen, onde ele é usado de novo. A demonstração de que esse retorno é indispensável vem de camundongos sem as duas claudinas: eles morrem logo após o nascimento, por má absorção de nutrientes, com todos os transportadores presentes.

A abertura da junção também muda com a refeição. No período pós-absortivo, o anel de actina e miosina está relaxado e a junção, mais fechada. No período pós-prandial, a entrada de sódio e glicose pelo SGLT1 ativa a #sigla("MLCK", [quinase da cadeia leve da miosina — enzima que fosforila a miosina e desencadeia a contração do anel de actina e miosina]). O anel se contrai, traciona as proteínas da junção e aumenta a permeabilidade paracelular. Com a junção mais aberta, a água puxada pelos solutos absorvidos passa em maior volume e leva consigo, por arraste, mais nutrientes e íons.

#figura-nebli("/figuras/fisio-05-digestao-absorcao/slide-12.png",
  largura: 72%,
  legenda: [A junção de oclusão no jejum (acima) e depois da refeição (abaixo): a captação de Na#super[+] e glicose pelo SGLT1 ativa a MLCK, o anel de actina e miosina se contrai e a via paracelular se abre.])

As duas vias, portanto, não competem. O transporte transcelular cria o gradiente osmótico e, ao mesmo tempo, o sinal que abre a rota paracelular; a rota paracelular devolve o sódio que mantém o transporte transcelular em funcionamento.

#mini-resumo[Em uma frase: as claudinas 2 e 15 devolvem sódio ao lúmen para alimentar os cotransportes, e a própria absorção de glicose, via MLCK, abre a junção e amplia a passagem entre as células.]

#conclusao-box[
O princípio que unifica a aula é que o intestino absorve criando gradientes. Nenhum nutriente polar atravessa a membrana por conta própria; cada um pega carona num íon que quer entrar, e esse desejo é fabricado pela bomba de sódio e potássio da membrana basolateral. A digestão existe para reduzir cada macronutriente à peça que seu transportador reconhece: monossacarídeo, dipeptídeo ou aminoácido, ácido graxo e monoglicerídeo.

O mecanismo nuclear tem três tempos. Enzimas luminais, do estômago e do pâncreas, fazem o corte grosso; enzimas da borda em escova fazem o corte fino junto ao transportador; e a célula, polarizada, recebe por uma membrana e entrega pela outra. A saída separa os nutrientes em dois destinos: o que é pequeno e solúvel vai pela veia porta ao fígado, e o que é lipídico é remontado, empacotado em quilomícrons e segue pela linfa, levando as vitaminas lipossolúveis. A água não tem mecanismo próprio e acompanha os solutos, por dentro e por entre as células.

Na clínica, cada elo perdido produz a mesma lógica com um nome diferente. Sem lactase, a lactose fica no lúmen e retém água; sem o trocador de sódio e hidrogênio, é o sódio que fica; sem enteropeptidase, nenhuma protease pancreática é ativada; sem bile, sem lipase ou sem quilomícron, a gordura sai nas fezes e leva consigo as vitaminas A, D, E e K. A vitamina B12 depende do estômago, do pâncreas e do íleo, e falha quando qualquer um deles falta. E a reidratação oral funciona porque explora o acoplamento entre sódio e glicose, que a diarreia secretora não destrói.

Adiante, esses mesmos transportadores reaparecem em outros epitélios. O túbulo proximal do rim reabsorve glicose, aminoácidos e bicarbonato com as mesmas proteínas e a mesma bomba, e o controle do ferro pela hepcidina volta sempre que se discutir por que uma inflamação prolongada produz anemia. Quem entende o enterócito como uma célula que organiza gradientes já tem a chave desses outros.
]
