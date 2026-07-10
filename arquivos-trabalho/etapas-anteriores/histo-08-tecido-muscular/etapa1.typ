#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  O tecido muscular existe para resolver um problema que nenhum outro tecido do corpo resolve: transformar energia química em *força mecânica* — movimento de verdade, que empurra o sangue, mexe o esqueleto e empurra o alimento pelo intestino. Todos os três tipos de músculo fazem isso com a mesma maquinaria básica (dois filamentos de proteína que deslizam um sobre o outro, gastando #sigla("ATP", [adenosina trifosfato — a moeda de energia da célula]) e disparados por um pulso de cálcio). O que muda de um tipo para o outro é como essa maquinaria é *organizada* e *controlada*.

  Este resumo segue essa lógica em três blocos. Na PARTE I montamos a célula muscular peça por peça, usando o músculo esquelético como modelo. Na PARTE II vemos a maquinaria *funcionar* — como o sinal elétrico vira contração — e por que o cardíaco e o liso são variações do mesmo tema. A PARTE III é prática pura: aprender a *reconhecer* cada um dos três tecidos ao microscópio, na lâmina corada por #sigla("HE", [hematoxilina-eosina — a coloração de rotina; hematoxilina cora núcleos de roxo-azul, eosina cora citoplasma e fibras de rosa]).
]

#parte-title("PARTE I — A célula muscular e sua organização", primeira: true)

#subtopico("1.1 Três tecidos, uma só tarefa: virar química em força")

Os três tecidos musculares nascem todos da mesma origem embrionária — a #termo-nota[mesoderme][a camada embrionária intermediária, de onde também saem osso, cartilagem e sangue]. Apesar de aparências bem diferentes ao microscópio, eles compartilham a função central: encurtar-se de forma controlada para gerar movimento. Em todos, a contração é o resultado de dois conjuntos de filamentos proteicos — um de *actina* (fino) e outro de *miosina* (grosso) — que deslizam um sobre o outro consumindo ATP, num passo disparado pela subida do cálcio dentro da célula. Guarde esse trio: *actina, miosina e cálcio*. Ele vai voltar em cada tipo de músculo, sempre com o mesmo papel de fundo.

A divisão clássica é em três tipos. O *músculo estriado esquelético* é o que move o esqueleto: está sob controle *voluntário* e mostra estrias transversais bem marcadas ao microscópio. O *músculo estriado cardíaco* é o do coração: também estriado, mas *involuntário* e dotado de um automatismo próprio. O *músculo liso* forma a parede dos vasos e das vísceras (intestino, bexiga, útero): é *involuntário* e, ao microscópio, *não* mostra estrias. A palavra "estriado", então, separa o liso dos outros dois logo de cara — e o detalhe que confunde todo mundo é justamente o que *une* esquelético e cardíaco, que parecem irmãos por terem estrias mas funcionam de modos bem diferentes, como veremos.

#figura-nebli("/figuras/histo-08-tecido-muscular/slide-02.png",
  largura: 52%,
  legenda: [Todos os três tipos derivam da mesoderme. O esquelético se forma quando células precursoras (mioblastos) proliferam e se fundem em fibras multinucleadas (miotubos), sob o comando de fatores como MyoD e Myf5; a miostatina atua como freio desse crescimento.])

#mini-resumo[Os três músculos vêm da mesoderme e contraem pelo mesmo motor (actina + miosina + ATP, disparado por cálcio). O que os distingue é a *organização* dos filamentos e o *modo de controle* — não o motor em si.]

#subtopico("1.2 O vocabulário próprio da fibra e as bainhas de conjuntivo")

A célula muscular é tão especializada que ganhou nomes próprios para suas partes — e isso atrapalha quem está chegando, porque parece que tudo é novo quando, na verdade, são estruturas já conhecidas com um apelido. Vale fixar as quatro trocas de nome de uma vez: a membrana plasmática vira *sarcolema*; o citoplasma vira *sarcoplasma*; o retículo endoplasmático liso vira #termo-nota[retículo sarcoplasmático][o retículo endoplasmático liso da fibra muscular, especializado em estocar e liberar cálcio] (#sigla("RS", [retículo sarcoplasmático — estoca o cálcio que dispara a contração])); e a mitocôndria é chamada de *sarcossoma*. O prefixo "sarco-" (de "carne") é a pista: sempre que ele aparece, pense "isto é a versão muscular de uma estrutura comum".

Antes de entrar na célula, é útil olhar de longe. Um músculo esquelético inteiro é um conjunto de feixes dentro de feixes, e cada nível desses é embrulhado por uma bainha de #sigla("TCD", [tecido conjuntivo denso]). O músculo todo é envolvido pelo *epimísio*; cada feixe de fibras (um *fascículo*) é envolvido pelo *perimísio*; e cada fibra muscular individual é envolvida pelo *endomísio*. Essas três bainhas se continuam umas nas outras e, nas pontas do músculo, convergem para formar o *tendão*, que ancora a força no osso. Não é só embalagem: é por dentro dessas bainhas de conjuntivo que os vasos e nervos viajam para alcançar cada fibra lá no fundo do músculo.

#figura-nebli("/figuras/histo-08-tecido-muscular/slide-07.png",
  largura: 72%,
  legenda: [Do músculo inteiro até a fibra, cada nível tem sua bainha de conjuntivo: *epimísio* (todo o músculo), *perimísio* (cada fascículo) e *endomísio* (cada fibra). À esquerda, o mesmo arranjo visto em corte transversal no HE. As bainhas se continuam no tendão e levam vasos e nervos para dentro.])

Agora a fibra em si. A célula muscular esquelética é um *sincício*: um #termo-nota[sincício][uma única célula com muitos núcleos, formada pela fusão de várias células precursoras] formado pela fusão de muitas células precursoras (os mioblastos) durante o desenvolvimento. Por isso ela é multinucleada — e os núcleos ficam *empurrados para a periferia*, encostados no sarcolema, porque o interior está lotado de filamentos contráteis. É uma célula enorme: 10 a 100 µm de diâmetro e podendo alcançar vários centímetros de comprimento. Logo por fora do sarcolema, sob uma lâmina basal, ficam as *células satélite* — células-tronco adormecidas que serão a chave da regeneração, e a que voltaremos na PARTE II.

#subtopico("1.3 Miofibrila, sarcômero e os filamentos")

Retomando a fibra que acabamos de descrever: cerca de 80% do seu volume é ocupado por *miofibrilas* — longos cilindros que correm de ponta a ponta da célula. Cada miofibrila, por sua vez, é uma fila de unidades repetidas chamadas #termo-nota[sarcômero][a unidade básica de contração do músculo estriado, definida como o segmento entre duas linhas Z consecutivas]. O sarcômero é *a* unidade de contração: tudo o que o músculo faz, ele faz somando o encurtamento de milhões de sarcômeros em série. Repare na escala, porque é um ponto que confunde — a *miofibrila* é o cilindro longo (a fila de sarcômeros); o *miofilamento* é a molécula individual (actina ou miosina) lá dentro. Não são sinônimos.

#figura-nebli("/figuras/histo-08-tecido-muscular/slide-10.png",
  largura: 75%,
  legenda: [A hierarquia completa, do músculo ao filamento: músculo → fascículo → fibra → miofibrila → sarcômero → miofilamentos (actina e miosina). Cada zoom é um nível de organização; o sarcômero (entre duas linhas Z) é a unidade que encurta.])

O sarcômero tem um padrão de listras que vem da forma como os dois filamentos se encaixam. Os *filamentos finos* (actina) estão ancorados na *linha Z*, que marca as duas bordas do sarcômero. Os *filamentos grossos* (miosina) ficam no meio, e ocupam a chamada *banda A*, que tem sempre o comprimento da miosina. Onde só há actina, sem miosina sobreposta, vemos a *banda I* (mais clara). No miolo da miosina, onde ainda não chega a actina, fica a *zona H*; e bem no centro, a *linha M* segura os filamentos grossos no lugar. Essa contabilidade de bandas não é decoreba gratuita: ela é exatamente o que vai mudar — e o que vai *ficar igual* — quando o músculo contrair.

#figura-lateral("/figuras/histo-08-tecido-muscular/slide-15.png",
  lado: "right",
  largura-figura: 42%,
  texto: [Vale abrir o filamento fino, porque é nele que mora o interruptor da contração. O filamento de actina não é só actina: ao longo dele se enrolam duas proteínas reguladoras — a *tropomiosina*, uma fita que cobre os sítios onde a miosina se ligaria, e o complexo *troponina*, encaixado de espaço em espaço. A troponina C liga cálcio; enquanto o cálcio não chega, a tropomiosina mantém a actina "tampada" e o músculo fica relaxado. É esse o interruptor que a PARTE II vai acionar.],
  legenda: [Sem cálcio, a tropomiosina tampa a actina; com cálcio, a troponina C a desloca e a miosina engata, gastando ATP.])

#figura-lateral("/figuras/histo-08-tecido-muscular/slide-18.png",
  lado: "left",
  largura-figura: 46%,
  texto: [Antes de passar para a contração, vale ver como tudo isso se empacota dentro da fibra. As miofibrilas não ficam soltas: o sarcolema manda para dentro prolongamentos — os *túbulos T* — que correm junto às cisternas do retículo sarcoplasmático. É esse encontro entre o túbulo e o retículo, na próxima PARTE, que leva o sinal elétrico da superfície até cada sarcômero no fundo da célula.],
  legenda: [Corte 3D da fibra: as bandas (I, A, H, linha M, disco Z) e, à esquerda, o *túbulo T* entre duas cisternas do retículo — a *tríade*.])

#parte-title("PARTE II — Como o músculo contrai e por que os três tipos diferem")

#subtopico("2.1 Deslizamento dos filamentos e o acoplamento excitação-contração")

Há um paradoxo aparente na contração muscular: o sarcômero encurta, mas nem a actina nem a miosina mudam de comprimento. A explicação é a *teoria dos filamentos deslizantes* — os dois filamentos deslizam um sobre o outro, como dois pentes que se interpenetram, e o que diminui é a *distância entre as linhas Z*, não o tamanho das peças. Pense numa luneta telescópica que encurta quando os tubos se sobrepõem mais, sem que nenhum tubo fique menor. Em termos das bandas: a *banda I* e a *zona H* encolhem (porque a actina avança sobre a miosina), enquanto a *banda A* permanece exatamente igual — afinal, ela é o comprimento da miosina, que não muda. Esse é um ponto que inverte fácil: na contração, não é a banda A que some.

#figura-nebli("/figuras/histo-08-tecido-muscular/slide-16.png",
  largura: 66%,
  legenda: [Relaxamento (acima) e contração (abaixo). Os filamentos mantêm o comprimento; a actina desliza sobre a miosina e aproxima as linhas Z. O sarcômero encurta — a banda I e a zona H diminuem, a banda A não.])

Falta a pergunta prática: como um sinal que chega na *superfície* da fibra consegue disparar, ao mesmo tempo, milhões de sarcômeros lá no *fundo* dela? Uma fibra de 100 µm de espessura é grossa demais para o cálcio simplesmente se difundir de fora para dentro a tempo. A solução é uma cadeia de eventos chamada *acoplamento excitação-contração*, e ela merece ser seguida passo a passo.

Primeiro, o nervo motor chega na fibra numa região especializada, a *placa motora*, e libera o neurotransmissor #termo-nota[acetilcolina][o neurotransmissor liberado na placa motora; abre canais que despolarizam o sarcolema] (#sigla("ACh", [acetilcolina — neurotransmissor da junção neuromuscular])). A ACh abre canais no sarcolema e gera um *potencial de ação* — uma onda de despolarização que corre pela membrana. Segundo, para levar essa onda elétrica até o interior, o sarcolema mergulha para dentro da fibra em invaginações profundas, os *túbulos T* (transversais); o potencial de ação desce por eles e alcança o centro da célula. Terceiro, no fundo, cada túbulo T encosta em duas cisternas do retículo sarcoplasmático, formando uma estrutura de três peças chamada #termo-nota[tríade][no músculo esquelético, o conjunto de 1 túbulo T entre 2 cisternas do retículo sarcoplasmático, na junção das bandas A e I]: a chegada do potencial de ação faz o RS *despejar cálcio* no sarcoplasma. Quarto, esse cálcio liga-se à troponina C, a tropomiosina sai da frente, a miosina engata na actina e puxa — gastando ATP a cada ciclo. Multiplicado por todos os sarcômeros, isso é a contração.

#figura-nebli("/figuras/histo-08-tecido-muscular/slide-26.png",
  largura: 70%,
  legenda: [O acoplamento excitação-contração no esquelético, em quatro passos: (1) a ACh na placa motora despolariza o sarcolema; (2) o potencial de ação desce pelos *túbulos T*; (3) na *tríade*, o retículo sarcoplasmático libera Ca²⁺; (4) o Ca²⁺ liga a troponina C e libera a interação actina-miosina — a contração.])

#mini-resumo[O sinal elétrico entra na profundidade da fibra pelos túbulos T; na tríade, ele faz o retículo sarcoplasmático soltar cálcio; o cálcio destrava a actina e a miosina puxa. *Quem dá a ordem é a subida do cálcio* — a interação actina-miosina é a consequência, não o gatilho.]

#subtopico("2.2 Cardíaco e liso pelo contraste com o esquelético")

Com o músculo esquelético montado, fica fácil entender os outros dois como *variações* do mesmo plano — basta perguntar, em cada um, o que mudou na organização e de onde vem o cálcio. Comecemos pelo cardíaco. A célula é o *cardiócito*: um cilindro mais curto, muitas vezes *ramificado*, com apenas *um ou dois núcleos centrais* (não periféricos, como no esquelético). Os cardiócitos não são uma massa fundida; são células separadas, unidas ponta a ponta por uma estrutura exclusiva, o #termo-nota[disco intercalar][a junção entre dois cardiócitos; combina junções aderentes/desmossomos (adesão mecânica) e junções comunicantes (acoplamento elétrico)].

O disco intercalar faz duas coisas ao mesmo tempo. As junções aderentes e os desmossomos *ancoram* mecanicamente uma célula na outra, para que a força da batida não rasgue o tecido. As junções comunicantes (gap), por sua vez, *acoplam eletricamente* as células, deixando o impulso passar direto de uma para a outra. O resultado é que o coração se comporta como um *sincício funcional* — contrai como se fosse uma célula só, embora seja feito de muitas.

#figura-nebli("/figuras/histo-08-tecido-muscular/slide-44.png",
  largura: 70%,
  legenda: [À esquerda, o cardiócito no HE: *núcleo central* e os *discos intercalares* cruzando as fibras. À direita, a ultraestrutura do disco — a *junção comunicante* (acoplamento elétrico), os *desmossomos* e a *faixa de adesão* (ancoragem mecânica), ao lado de miofibrilas e mitocôndrias.])

Por dentro, o cardiócito também tem sarcômeros e túbulos T, mas com diferenças finas: o túbulo T encosta em *uma* só cisterna do RS (formando uma *díade*, não uma tríade), e o RS é menos extenso. Por isso o cardíaco depende de um truque a mais para a contração — e aqui está a confusão mais importante de todo este tema.

#atencao-box("De onde vem o cálcio muda conforme o músculo", [No *esquelético*, todo o cálcio da contração sai do retículo sarcoplasmático, liberado pela tríade — a célula praticamente não depende do cálcio de fora. No *cardíaco* é diferente: um pouco de cálcio *extracelular* entra pelo canal #sigla("DHPR", [receptor de di-hidropiridina — canal de cálcio do túbulo T]) durante o potencial de ação, e é *essa entrada* que dispara o retículo sarcoplasmático a liberar o resto, num mecanismo chamado #sigla("CICR", [liberação de cálcio induzida por cálcio]) (liberação de cálcio induzida por cálcio), pelos canais de #sigla("RyR", [receptor de rianodina — canal que libera cálcio do retículo sarcoplasmático]). Generalizar "o cálcio sempre vem do RS" para os três tipos é o erro mais punido neste assunto. É também por isso que o coração é tão sensível a bloqueadores de canal de cálcio.])

Os cardiócitos ainda têm mitocôndrias abundantes e cheias de cristas (o coração nunca descansa e vive de fosforilação oxidativa) e secretam o *hormônio natriurético* quando a parede atrial é muito esticada — um detalhe que liga histologia a fisiologia da pressão arterial.

O músculo liso é a variação mais radical. A célula é *fusiforme* (formato de charuto, afilada nas pontas), com *um único núcleo central*, e — o ponto que reorganiza tudo — *não tem sarcômeros nem estriação*. A actina e a miosina existem, mas não estão alinhadas em bandas; ficam em redes oblíquas ancoradas em #termo-nota[corpos densos][placas ricas em α-actinina espalhadas pela célula lisa, equivalentes funcionais da linha Z, onde a actina se ancora] espalhados pelo citoplasma e pela membrana, ligados ainda por filamentos intermediários (desmina e vimentina). Quando a actina puxa contra esses pontos de ancoragem, a célula inteira se enruga e encurta. No lugar dos túbulos T, o liso usa pequenas invaginações chamadas *cavéolas*, e as células se acoplam por junções comunicantes.

#figura-lateral("/figuras/histo-08-tecido-muscular/slide-53.png",
  lado: "right",
  largura-figura: 40%,
  texto: [A regulação do liso também é diferente, e é o segundo ponto que inverte fácil. Aqui o cálcio — que vem em boa parte do *meio extracelular* — não tem troponina para se ligar. Em vez disso, ele se liga à #termo-nota[calmodulina][proteína citosólica que liga cálcio; o complexo cálcio-calmodulina ativa a MLCK no músculo liso], e o complexo cálcio-calmodulina ativa uma enzima, a #sigla("MLCK", [quinase de cadeia leve da miosina — fosforila a miosina e habilita a contração no músculo liso]), que *fosforila a miosina*. Ou seja: no liso, a contração é regulada na *miosina*; no esquelético, era regulada na *actina* (pela troponina). Esse músculo é lento, sustentado e responde a hormônios e estiramento — perfeito para manter o tônus de um vaso por horas.],
  legenda: [Liso: actina e miosina ancoradas em *corpos densos*; a célula encurta como um todo.])

#subtopico("2.3 Os três tipos lado a lado, regeneração e hipertrofia")

Tudo o que vimos na função se condensa numa comparação direta — e este é um caso em que a tabela rende mais que a prosa, porque são seis dimensões que se cruzam e o aluno precisa enxergar as três colunas de uma vez:

#figure(
  table(
    columns: (1.3fr, 1fr, 1fr, 1fr),
    inset: 7pt,
    align: (left, left, left, left),
    stroke: 0.5pt + gray-border,
    table.header(
      [*Característica*], [*Esquelético*], [*Cardíaco*], [*Liso*],
    ),
    [Núcleos], [Vários, periféricos], [1–2, centrais], [1, central],
    [Estriação], [Sim, evidente], [Sim, mais sutil], [Ausente],
    [Controle], [Voluntário], [Involuntário (automatismo)], [Involuntário],
    [Junção entre células], [Nenhuma (fibras independentes)], [Discos intercalares], [Junções comunicantes],
    [Fonte do Ca²⁺], [RS (tríade)], [Extracelular dispara o RS (CICR, díade)], [Sobretudo extracelular],
    [Regulação na…], [Actina (troponina)], [Actina (troponina)], [Miosina (calmodulina/MLCK)],
    [Regeneração], [Parcial (células satélite)], [Praticamente nula], [Boa (mantém mitose)],
  ),
  caption: [Os três tipos de músculo nas dimensões que mais importam. Repare na linha do cálcio e na da regulação — são elas que mais confundem.],
)

A última linha da tabela merece um parágrafo próprio, porque a capacidade de regeneração é bem desigual. O *músculo liso* é o que melhor se repara: suas células conservam a capacidade de entrar em mitose. O *cardíaco*, no extremo oposto, praticamente *não regenera* — depois de um infarto, a área morta é substituída por cicatriz fibrosa, não por músculo novo, e isso explica por que a lesão cardíaca é tão definitiva. O *esquelético* fica no meio: a fibra madura em si *não* entra em mitose, mas o tecido tem uma carta na manga — as células satélite.

E aqui mora outra inversão comum. Quando alguém treina e o músculo cresce, a fibra não se *multiplica*; ela *engorda*. O aumento de massa é *hipertrofia*: a fibra existente sintetiza mais miofilamentos e fica mais grossa. Fibras novas (ou o reparo de fibras lesadas) vêm da diferenciação das #termo-nota[células satélite][células-tronco musculares sob a lâmina basal; ao se diferenciar, reparam fibras lesadas e fornecem novos núcleos] em mioblastos, que se fundem à fibra. Esse programa de diferenciação é controlado por fatores como o MyoD, e *freado* por uma proteína chamada miostatina — animais sem miostatina desenvolvem musculatura exageradamente volumosa, o que mostra, ao contrário, o quanto ela contém o crescimento no dia a dia.

Montada a célula e entendida a função, falta a habilidade prática que fecha o tema: pegar uma lâmina e dizer, olhando, qual dos três músculos está ali. É o que faremos na PARTE III.

#parte-title("PARTE III — Reconhecer o tecido muscular ao microscópio (prática)")

#subtopico("3.1 As três perguntas do microscópio e o estriado esquelético no HE")

Agora reencontramos os três tipos de músculo, mas pela lente do microscópio óptico, na lâmina de rotina corada por HE. Antes de tentar nomear o tecido, vale ter na cabeça três perguntas — elas resolvem quase todos os casos sem decoreba. *Primeira: há estriação transversal?* Se sim, é esquelético ou cardíaco; se não, é liso. *Segunda: onde estão os núcleos e quantos são?* Periféricos e vários → esquelético; central e um ou dois → cardíaco ou liso. *Terceira: qual a forma e o arranjo das células?* Fibras longas e paralelas, ramificadas, ou fusiformes. Com essas três respostas, o tecido se denuncia.

Começando pelo *músculo estriado esquelético*, os critérios de reconhecimento no HE são:

- *Tecido bastante acidófilo* — cora-se em rosa intenso pela eosina (muita proteína contrátil no citoplasma).
- *Fibras de grande diâmetro e comprimento* — em corte longitudinal aparecem como faixas longas e paralelas; em corte transversal, como polígonos grandes e justapostos.
- *Vários núcleos, periféricos* — alinhados na borda da fibra, logo sob o sarcolema.
- *Estriação citoplasmática transversal* — as listras claras e escuras do alinhamento dos sarcômeros, visíveis sobretudo no corte longitudinal.

#figura-nebli("/figuras/histo-08-tecido-muscular-pratica/slide-03.png",
  largura: 76%,
  legenda: [Músculo estriado esquelético no HE. À esquerda, *corte longitudinal*: fibras longas, paralelas, com estriação transversal e núcleos na periferia. À direita, *corte transversal*: polígonos grandes, com os núcleos empurrados para a borda de cada fibra.])

O corte transversal é também o melhor lugar para reencontrar as bainhas de conjuntivo da PARTE I — e aqui é fácil inverter os nomes, então vale o cuidado. A bainha fina que cerca *cada fibra* é o endomísio; a que envolve *um fascículo* inteiro é o perimísio (mais espessa, fácil de ver separando os feixes); e a que reveste *todo o músculo* por fora é o epimísio. Um truque seguro: do menor para o maior, *endo → peri → epi*, acompanhando fibra → fascículo → músculo.

#figura-nebli("/figuras/histo-08-tecido-muscular-pratica/slide-07.png",
  largura: 66%,
  legenda: [O mesmo músculo esquelético em corte transversal, com as bainhas identificadas: (1) *perimísio* envolve o fascículo, (2) *endomísio* envolve cada fibra, (3) *epimísio* envolve o músculo. Os pontos roxos na borda de cada polígono são os núcleos periféricos.])

Dentro de alguns fascículos pode aparecer uma estrutura encapsulada com fibras finas no interior: é o #termo-nota[fuso neuromuscular][receptor sensitivo do músculo, com fibras musculares modificadas (intrafusais) dentro de uma cápsula; informa o comprimento do músculo], um receptor que informa ao sistema nervoso o quanto o músculo está estirado. Não confundir com vaso ou nervo cortado: a cápsula com fibras musculares finas (intrafusais) lá dentro é a assinatura do fuso.

#subtopico("3.2 Cardíaco no HE: o disco intercalar como marcador")

O ponto que separa o cardíaco do esquelético ao microscópio não é a estriação — os dois a têm — e sim *três achados combinados*, sendo um deles exclusivo. Os critérios de reconhecimento são:

- *Estriação presente, porém mais sutil* que a do esquelético.
- *Núcleo central, único ou em par (1–2)*, muitas vezes com um halo claro ao redor.
- *Fibras ramificadas e de contorno mais irregular*, diferentes das faixas retas e paralelas do esquelético.
- *Discos intercalares* — linhas transversais escuras cruzando as fibras no corte longitudinal. Este é o *marcador exclusivo* do cardíaco: nenhum outro músculo os tem.

#figura-nebli("/figuras/histo-08-tecido-muscular-pratica/slide-13.png",
  largura: 70%,
  legenda: [Músculo cardíaco em corte longitudinal (HE). As *setas* apontam os discos intercalares — as linhas transversais escuras que unem cardiócitos vizinhos. Note os núcleos centrais e o arranjo ramificado, menos regular que o do esquelético.])

Os discos intercalares ficam ainda mais evidentes em colorações especiais como o #sigla("PTAH", [hematoxilina fosfotúngstica ácida — coloração que realça estriações e discos intercalares do músculo cardíaco]), usada justamente para realçar estriações e discos. Em cortes do coração também podem aparecer, logo abaixo do endocárdio, as *fibras de Purkinje*: cardiomiócitos modificados, especializados em conduzir o impulso, que se reconhecem por serem *maiores e mais pálidos* (cheios de glicogênio, com poucas miofibrilas). O nome engana — são músculo condutor, não tecido nervoso.

#subtopico("3.3 Liso no HE e o exercício integrador do intestino")

Fechando o trio, o *músculo liso* é o mais discreto na lâmina justamente por não ter estriação — e reconhecê-lo é mais um exercício de eliminar os outros dois e confirmar a forma da célula. Os critérios são:

- *Ausência de estriação* — citoplasma acidófilo homogêneo, sem listras.
- *Células fusiformes* (charuto), com *um único núcleo central* e alongado.
- Em *corte longitudinal*, as células aparecem como fusos paralelos; o núcleo de uma fibra contraída assume um aspecto *em saca-rolhas* (espiralado) — achado característico, não defeito de corte.
- Em *corte transversal*, vê-se um mosaico de perfis poligonais pequenos, e *só alguns mostram o núcleo* (apenas onde o corte passou pelo meio da célula).

#figura-nebli("/figuras/histo-08-tecido-muscular-pratica/slide-17.png",
  largura: 70%,
  legenda: [Músculo liso no HE. À direita, *corte transversal*: perfis pequenos e poligonais, com núcleo central só em algumas células. À esquerda e abaixo, *corte longitudinal*: células fusiformes paralelas; quando contraídas, o núcleo aparece espiralado ("saca-rolhas").])

O melhor teste do que aprendemos é um corte de órgão real, onde vários tecidos convivem. Num corte transversal de intestino, o músculo liso aparece em *duas orientações ao mesmo tempo* (a parede tem uma camada circular e outra longitudinal), ao lado de epitélio e tecido conjuntivo. Saber separar tudo isso é exatamente o que o reconhecimento treina: aplicar as três perguntas a cada região e ir nomeando.

#figura-nebli("/figuras/histo-08-tecido-muscular-pratica/slide-19.png",
  largura: 66%,
  legenda: [Corte de intestino (HE) como exercício integrador: (1) epitélio glandular; (2 e 5) músculo liso em corte longitudinal; (3) músculo liso em corte transversal; (4) tecido conjuntivo denso não modelado. O mesmo músculo liso aparece em orientações diferentes conforme o plano de corte.])

No fim, reconhecer o tecido ao microscópio é a mesma história das PARTES I e II vista de outro ângulo. Os núcleos periféricos e a estriação forte do esquelético vêm de ele ser um sincício multinucleado lotado de sarcômeros alinhados; os discos intercalares do cardíaco são a marca de células independentes que precisam se acoplar para bater juntas; a ausência de estrias no liso reflete a actina e a miosina ancoradas em corpos densos, sem o alinhamento em bandas. A imagem na lâmina é a estrutura, e a estrutura é a função — o microscópio só torna isso visível.

#conclusao-box[
  Um único princípio costura todo o tema: *a estrutura de cada músculo é a sua função tornada visível*. O motor é sempre o mesmo — actina e miosina deslizando sob o comando do cálcio, gastando ATP — e cada tipo apenas organiza e controla esse motor de um jeito diferente. O esquelético é um sincício multinucleado de sarcômeros alinhados, controlado voluntariamente e abastecido de cálcio pelo seu próprio retículo na tríade; o cardíaco é feito de células independentes que se acoplam por discos intercalares e usam o cálcio que entra de fora para disparar o retículo (CICR), o que o torna sensível a bloqueadores de canal de cálcio; o liso abre mão do sarcômero e regula a contração na miosina, pela via calmodulina-MLCK, sustentando o tônus das vísceras por horas. No microscópio, esses três projetos se denunciam por três marcas — núcleos periféricos, disco intercalar e célula fusiforme sem estrias —, e é por elas que o reconhecimento começa. Daqui o tema se conecta direto com a histologia do sistema circulatório, em que a parede dos vasos será lida exatamente com este olhar para o músculo liso.
]
