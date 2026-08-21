#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Toda doença começa no mesmo lugar: uma célula que deixou de dar conta do que estava sendo exigido dela. Antes de existir sintoma, exame alterado ou lesão visível numa peça, existe uma célula que perdeu a capacidade de manter o próprio meio interno estável. A patologia começa aqui porque este é o degrau mais baixo do qual todo o resto se constrói — o infarto, a hepatite, a pancreatite e a vasculite são, no fundo, a mesma história contada em tecidos diferentes.

  Este resumo percorre essa história em três movimentos. Primeiro, o espectro completo da resposta celular: o que separa a célula que se adapta da que se lesa, e onde exatamente fica a linha depois da qual não há volta. Depois, os mecanismos bioquímicos que produzem a lesão — quatro caminhos que parecem independentes e que na prática se alimentam uns aos outros até convergir. Por fim, os dois desfechos possíveis dessa convergência, necrose e apoptose, com a morfologia que permite reconhecer cada um no microscópio e o significado clínico que cada padrão carrega.

  O fio condutor é sempre o mesmo: *o mecanismo explica a morfologia, e a morfologia explica o quadro clínico*. Quando você entender por que a célula lesada fica rosa ao microscópio, terá entendido o que aconteceu com o retículo endoplasmático dela — e é essa cadeia, e não a lista de nomes, que sustenta o raciocínio na frente de uma lâmina ou de um paciente.
]

#parte-title("PARTE I — Da agressão à linha de não-retorno", primeira: true)

#subtopico("1.1 Homeostase, adaptação e lesão: o espectro completo")

A célula normal não vive em equilíbrio absoluto. Ela vive numa faixa estreita de composição interna — íons, pH, volume, quantidade de organelas — que é mantida ativamente, custando energia o tempo todo. Essa manutenção ativa dentro de uma faixa é o que chamamos de homeostase, e o ponto importante é que ela tem margem: a célula suporta variações razoáveis de demanda funcional e de oferta de nutrientes sem sair do estado normal.

Quando o estímulo aumenta e passa dessa margem, a célula não morre imediatamente. Ela tenta um segundo estado estável, mais alto ou mais baixo, ajustado ao novo nível de exigência. Isso é *adaptação*, e ela é um sucesso, não um começo de doença: o miocárdio submetido a hipertensão arterial crônica responde aumentando o tamanho de cada fibra para gerar mais força contra uma pós-carga maior, e essa hipertrofia mantém o débito cardíaco por anos. O ponto fino é que adaptação tem preço — a fibra hipertrofiada precisa de mais oxigênio, e a rede capilar não cresce na mesma proporção, o que deixa o coração adaptado mais vulnerável à próxima agressão do que o coração normal.

Se o estímulo ultrapassa a capacidade adaptativa, ou se a célula simplesmente não consegue montar a adaptação, o que se instala é *lesão celular*. E aqui a distinção que organiza toda a patologia: a lesão pode ser reversível ou irreversível. Enquanto o insulto for leve e transitório, as alterações que ele produz podem ser desfeitas e a célula retorna à homeostase — é o que acontece num acidente isquêmico transitório, em que o fluxo cerebral cai o suficiente para causar déficit neurológico e volta antes de matar o neurônio. Se o insulto for severo ou persistente, a célula cruza um ponto a partir do qual restaurar o fluxo não adianta mais, e o desfecho é morte celular — necrose ou apoptose.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-02.png",
  largura: 62%,
  legenda: [O mapa completo da resposta celular. Repare que o estresse dentro da capacidade adaptativa leva à adaptação, e que a incapacidade de adaptar desemboca em lesão — não são vias paralelas, uma alimenta a outra. Da lesão, a seta de volta ("leve, transitória") existe; a seta para baixo ("severa, progressiva") é de mão única.])

Vale fixar o mapa antes de descer aos detalhes, porque cada caixa dele vai virar um subtópico. Hipertensão arterial e doença de Alzheimer são exemplos de estados em que a célula opera adaptada por muito tempo. Hipóxia moderada e acidente isquêmico transitório são lesão reversível. Hepatite aguda e infarto agudo do miocárdio são lesão irreversível — a célula do miocárdio que ficou sem fluxo por mais de vinte a trinta minutos não volta, por mais que a artéria seja desobstruída depois.

#mini-resumo[Estresse dentro da margem gera adaptação; acima dela, lesão reversível; se o insulto for severo ou persistente, a lesão vira irreversível e a célula morre.]

#subtopico("1.2 As causas da agressão: por que a privação de oxigênio lidera")

Há uma tentação natural de decorar as causas de lesão celular como uma lista de sete itens. O problema dessa leitura é que ela apaga a hierarquia: as sete categorias não são equivalentes nem em frequência nem em mecanismo, e a primeira delas explica sozinha a maior parte da patologia que você vai encontrar.

A *privação de oxigênio* é a causa mais comum porque atinge o ponto único de que a célula não consegue escapar — a produção de #sigla("ATP", [adenosina trifosfato — a moeda energética da célula, gasta em toda reação que consome energia]) pela fosforilação oxidativa. E aqui entra a distinção que mais confunde quem está começando. #termo-nota[Isquemia][redução ou interrupção do fluxo sanguíneo para um tecido, com perda simultânea de oxigênio, de substratos e da remoção de catabólitos] é redução do fluxo sanguíneo. Hipóxia é déficit de oxigênio por qualquer via. Toda isquemia causa hipóxia, mas nem toda hipóxia é isquemia — e a diferença tem consequência mecanística direta.

#confusao-prevista(
  titulo: "Isquemia lesa mais rápido que hipóxia — e não é por causa do oxigênio",
  aluno_acha: [aluno acha que isquemia e hipóxia são o mesmo problema com nomes diferentes],
  mecanismo: [na hipóxia sem isquemia — anemia grave, intoxicação por #sigla("CO", [monóxido de carbono — gás que ocupa o sítio de ligação do oxigênio na hemoglobina com afinidade muito maior]), grande altitude — o fluxo sanguíneo está preservado. A célula perde a fosforilação oxidativa, mas continua recebendo glicose e continua exportando lactato, então a glicólise anaeróbia sustenta a produção de ATP por um bom tempo. Na isquemia o fluxo caiu: a glicose deixa de chegar, o lactato deixa de ser removido, o pH despenca e a própria glicólise anaeróbia trava. Por isso o tecido isquêmico morre em minutos e o tecido apenas hipóxico resiste muito mais.],
)

As demais causas se organizam melhor pelo alvo que atingem do que pela ordem em que aparecem na lista. Os *agentes físicos* — trauma mecânico, extremos de temperatura, radiação, choque elétrico — lesam por transferência direta de energia, rompendo membranas ou quebrando ligações químicas. Os *agentes químicos e as drogas* atuam num espectro que vai do trivial ao violento: glicose e sal em concentração suficiente lesam por desequilíbrio osmótico, e a lição embutida aí é que não existe substância inerentemente inócua — é a dose que faz o agente.

Os *agentes infecciosos* lesam por vias que variam com o patógeno: vírus que se replicam dentro da célula e a consomem, bactérias que liberam toxinas, parasitas que ocupam espaço. Os *mecanismos imunológicos* têm uma particularidade que vale marcar — quem lesa é a própria resposta do hospedeiro, e não um invasor. Na autoimunidade não há patógeno nenhum; o efetor é o anticorpo, o complemento ou o linfócito T citotóxico do próprio paciente. Os *desarranjos genéticos* produzem proteínas defeituosas ou ausentes, e a lesão vem da função que faltou. Os *desbalanços nutricionais* fecham o grupo pelos dois extremos: a deficiência proteico-calórica que impede a manutenção celular e o excesso calórico que sobrecarrega o metabolismo lipídico.

#mini-resumo[Sete causas, uma hierarquia: privação de oxigênio lidera porque ataca a produção de ATP, e isquemia é pior que hipóxia porque tira substrato junto.]

#subtopico("1.3 Lesão reversível: a célula incha e a gordura se acumula")

Pense na célula lesada de forma reversível como uma casa em que a bomba d'água parou de funcionar mas as paredes continuam de pé. Nada se rompeu ainda; o que aconteceu é que um serviço que dependia de energia contínua foi interrompido, e as consequências desse serviço parado começam a se acumular. Duas dessas consequências são visíveis ao microscópio óptico, e as duas dão nome às alterações clássicas da lesão reversível: o edema celular e a alteração gordurosa.

O *edema celular* — também chamado de tumefação ou degeneração hidrópica — nasce diretamente da falência da bomba de sódio. A membrana plasmática mantém a célula osmoticamente enxuta gastando ATP para jogar sódio para fora e trazer potássio para dentro. Quando o ATP cai, a bomba desacelera, o sódio se acumula no citosol arrastando água por osmose, e a célula incha. É a primeira alteração morfológica de praticamente qualquer lesão, e é reversível: restabelecido o ATP, a bomba volta a trabalhar e o volume normaliza.

A *alteração gordurosa*, ou #termo-nota[esteatose][acúmulo de triglicerídeo em vacúolos dentro do citoplasma, típico de hepatócito e de miocárdio sob lesão], é o segundo achado e obedece a outra lógica. Ela aparece em células que lidam com muito lipídio, sobretudo o hepatócito, e resulta de um desbalanço: o ácido graxo continua chegando e sendo esterificado em triglicerídeo, mas a exportação como lipoproteína depende de síntese proteica — que caiu, porque os ribossomos se desligaram do retículo. O lipídio fica retido em vacúolos que empurram o núcleo para a periferia.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-09.png",
  largura: 52%,
  legenda: [Túbulo renal em três estados, no mesmo aumento. Em A, epitélio normal, com luz ampla e limites nítidos. Em B, o citoplasma já está mais volumoso e a luz tubular se estreitou — edema celular. Em C, as células estão francamente tumefeitas, com vacuolização e perda da borda apical. Repare que o núcleo continua presente e bem corado nos três: enquanto o núcleo estiver íntegro, a lesão ainda é reversível.])

A ultraestrutura mostra o mesmo processo com mais resolução, e cada achado ao microscópio eletrônico corresponde a um serviço celular que parou. Na membrana plasmática aparecem #termo-nota[blebs][bolhas de membrana que se projetam da superfície celular quando o citoesqueleto de actina deixa de ancorá-la] e ocorre perda das microvilosidades — as duas coisas por falha do citoesqueleto de actina, que precisa de ATP para manter as projeções montadas. As mitocôndrias incham e desenvolvem densidades amorfas na matriz. O retículo endoplasmático se dilata por entrada de água e, o mais revelador, os polissomos se desprendem dele: a síntese proteica cai. No núcleo, os elementos fibrilares e granulares do nucléolo se desagregam.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-10.png",
  largura: 42%,
  legenda: [Ultraestrutura da mesma sequência. Em A, célula normal com microvilosidades densas e regulares. Em B e C, as microvilosidades desapareceram, o citoplasma está claro e vacuolizado e as mitocôndrias estão dilatadas — todos achados de lesão ainda reversível.])

#mini-resumo[Bomba de sódio parada deixa o sódio entrar, a água vem atrás e a célula incha — edema celular. Síntese proteica parada impede a exportação de lipoproteína e o triglicerídeo se acumula — esteatose.]

#subtopico("1.4 A linha de irreversibilidade e o atraso da morfologia")

Tudo o que a PARTE I descreveu até aqui pode ser desfeito. O que precisa ficar claro agora é o que *não* pode — e a resposta do slide é enxuta e mecanisticamente exata: dois critérios definem a irreversibilidade, e eles se somam.

O primeiro é a *perda da permeabilidade seletiva da membrana*. Enquanto a membrana plasmática separa o interior do exterior, existe gradiente, existe potencial e existe a possibilidade de recuperar o controle iônico. Quando ela deixa de ser barreira, o conteúdo celular se derrama para fora e o meio externo entra — e não há bomba que compense um vazamento livre. O segundo é a *destruição extensa de DNA e de proteínas*. Uma célula pode repor proteína e reparar DNA dentro de certos limites; ultrapassados esses limites, o programa de manutenção não tem mais molde para trabalhar.

Estabelecido o ponto sem volta, aparece a consequência que mais atrapalha a leitura de uma lâmina: *a morte celular acontece muito antes de ficar visível*. Existe um intervalo, medido em horas, entre o momento em que a célula está bioquimicamente morta e o momento em que o corte corado revela isso. As alterações bioquímicas vêm primeiro; as alterações ultraestruturais, detectáveis só ao microscópio eletrônico, vêm depois; as alterações de microscopia óptica vêm em seguida; e a alteração macroscópica, visível a olho nu na peça, é a última de todas.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-06.png",
  largura: 52%,
  legenda: [O eixo horizontal é duração da agressão. A função celular (curva vermelha) despenca primeiro, ainda na faixa reversível. Depois da linha tracejada, as alterações bioquímicas letais aparecem, seguidas pelas ultraestruturais, pelas de microscopia óptica e, por último, pelas macroscópicas. O intervalo entre a linha tracejada e a curva roxa é o tempo em que a célula está morta e a lâmina ainda parece normal.])

Isso tem consequência prática direta. Num paciente que morre nas primeiras horas de um infarto, o miocárdio pode não mostrar necrose ao microscópio óptico, ainda que a área já esteja irremediavelmente morta. O patologista precisa saber disso para não concluir, de uma lâmina de aparência preservada, que não houve infarto.

Como a morfologia atrasa, a clínica precisou de outro sinal — e ele vem exatamente do primeiro critério de irreversibilidade. Se a membrana rompeu, o conteúdo intracelular está no sangue. Dosar esse conteúdo é ler indiretamente a integridade da membrana.

#clinica-box("Marcadores de necrose miocárdica: a membrana rompida no exame de sangue", [O paciente com dor torácica chega ao pronto-socorro e o eletrocardiograma nem sempre fecha o diagnóstico. A conduta se apoia então em moléculas que só estão no sangue porque a membrana do cardiomiócito deixou de ser barreira. A *mioglobina* é pequena e citoplasmática: sobe em uma a duas horas, atinge o pico cedo e cai rápido — sensível, porém inespecífica, porque qualquer músculo esquelético lesado a libera. A *creatinoquinase fração MB* sobe em quatro a seis horas e normaliza em dois a três dias, o que a torna útil para detectar reinfarto precoce. A *troponina I* é a proteína do aparelho contrátil cardíaco: sobe em três a quatro horas, atinge pico em torno de vinte e quatro horas e permanece elevada por até dez dias — é a que combina especificidade cardíaca com janela longa, e por isso governa a decisão. Repare que a lógica das três curvas é a mesma: tamanho da molécula e localização dentro da célula determinam quando ela aparece; a via de depuração determina quanto tempo ela fica.])

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-11.png",
  largura: 46%,
  legenda: [Cinética dos três marcadores a partir do início dos sintomas. A mioglobina (círculo cheio) sobe e cai primeiro; a fração MB da creatinoquinase (círculo vazio) ocupa a faixa intermediária; a troponina I (triângulo) tem a janela mais longa. Nenhuma delas é elevada porque lesa — todas são elevadas porque a membrana deixou passar.])

O que fecha a PARTE I é a percepção de que os dois critérios de irreversibilidade não são pontos de chegada arbitrários: eles são o resultado final de processos bioquímicos que começaram muito antes, no instante em que o ATP começou a cair. Entender *como* a membrana perde a permeabilidade e *por que* o DNA é destruído exige descer um nível — e é isso que a PARTE II faz.

#parte-title("PARTE II — Os mecanismos bioquímicos que convergem")

#subtopico("2.1 Depleção de ATP: a falência em cadeia das bombas")

A PARTE I fechou dizendo que a membrana perde permeabilidade e que o DNA é destruído. Nenhuma das duas coisas acontece por acidente: as duas são o ponto de chegada de quatro processos bioquímicos que começam separados e terminam alimentando uns aos outros. Antes de abrir cada um, vale ver os quatro juntos, porque a arquitetura deles importa tanto quanto o conteúdo.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-12.png",
  largura: 64%,
  legenda: [Os quatro mecanismos, com o alvo final de cada um. Dano mitocondrial rebate em dois lados — queda de ATP e produção de radicais. Entrada de cálcio ativa enzimas e agrava a permeabilidade mitocondrial. Dano de membrana se divide em plasmática (perda de conteúdo) e lisossômica (digestão enzimática). Proteína mal dobrada e DNA lesado convergem para a ativação de proteínas pró-apoptóticas.])

O primeiro mecanismo é a *depleção de ATP*, e ele é o mais didático porque tudo nele decorre de uma única falta. A isquemia reduz a oferta de oxigênio; sem oxigênio no fim da cadeia respiratória, a fosforilação oxidativa para; sem fosforilação oxidativa, o ATP despenca em minutos. A partir daí, cada consequência é o desligamento de um serviço que dependia daquele ATP, e cada desligamento tem uma morfologia correspondente que você já conhece da PARTE I.

A bomba de sódio e potássio é a primeira a sentir, porque é a maior consumidora de energia da célula. Com ela lenta, o sódio se acumula dentro, o potássio sai, a água entra por osmose e aparecem o edema celular, a dilatação do retículo endoplasmático, a perda de microvilosidades e as bolhas de membrana. O cálcio, que também depende de bomba para ser mantido baixo no citosol, começa a entrar — e essa entrada vai virar o segundo mecanismo.

Em paralelo, a célula tenta compensar ligando a *glicólise anaeróbia*. Ela funciona, mas o rendimento cai de dezenas de ATP por glicose para dois, e o preço aparece rápido: o glicogênio se esgota, o lactato se acumula e o pH intracelular despenca. A acidose não é subproduto inofensivo — ela condensa a cromatina nuclear, desnatura proteínas estruturais e inativa enzimas, participando ativamente do dano.

A terceira consequência é o *desprendimento dos ribossomos* do retículo endoplasmático rugoso. A síntese proteica cai, e é essa queda que explica a deposição lipídica descrita em 1.3: sem apoproteína recém-sintetizada, o triglicerídeo não sai do hepatócito.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-13.png",
  largura: 58%,
  legenda: [A cascata inteira a partir da isquemia. Três braços saem da queda de ATP: falência da bomba de sódio (à esquerda, com o edema no fim), glicólise anaeróbia (ao centro, com a acidose e a condensação da cromatina) e desprendimento dos ribossomos (à direita, com a queda de síntese proteica). Repare que o edema celular, a perda de microvilosidades e as bolhas — os achados morfológicos da PARTE I — aparecem aqui como produtos finais de um braço específico.])

Guarde uma consequência dessa dependência energética, porque ela volta em 2.2 e depois em toda a PARTE III: *sem ATP a célula não consegue morrer de forma organizada*. A apoptose, que parece a morte "econômica", precisa de energia para montar seus complexos enzimáticos. Célula sem ATP não apopta — ela necrosa.

#subtopico("2.2 Dano mitocondrial: a mesma organela decide os dois desfechos")

Existe um ponto em que a intuição costuma escorregar. Como o citocromo c da mitocôndria dispara apoptose, é natural concluir que mitocôndria lesada leva a apoptose. Não é isso que acontece — a mesma lesão mitocondrial tem duas saídas, e qual delas ocorre depende de *quanto* a mitocôndria foi comprometida.

A mitocôndria é alvo convergente de tudo o que a PARTE II descreve: cálcio citosólico elevado, espécies reativas de oxigênio e peroxidação lipídica agridem suas membranas. A partir daí, dois caminhos.

O primeiro é a abertura de um canal de alta condutância na membrana interna, a *transição de permeabilidade mitocondrial*. Quando esse poro se abre de forma ampla e sustentada, os prótons atravessam livremente, o gradiente que a cadeia respiratória construiu se dissipa e o potencial de membrana mitocondrial se perde. Sem gradiente de prótons não há síntese de ATP — e a célula, agora sem energia, cai em necrose. O detalhe que fecha o raciocínio é que esse poro não é um rasgo mecânico: é um canal, e sua abertura é um evento regulado.

O segundo caminho é o *vazamento seletivo de citocromo c* e de outras proteínas pró-apoptóticas pela membrana externa, com a mitocôndria ainda parcialmente funcional. O citocromo c, que no espaço intermembrana é apenas um transportador de elétrons da cadeia respiratória, ganha uma segunda função assim que chega ao citosol: ele se liga à proteína Apaf-1 e nucleia a montagem do complexo que ativa a via apoptótica. Como a célula ainda tem ATP, ela consegue executar o programa.

#atencao-box("Sem ATP não existe apoptose", [O aluno tende a tratar apoptose e necrose como dois destinos que a célula escolhe livremente, e a escolher a apoptose como o desfecho "menos grave". Mecanisticamente, não há escolha livre: a apoptose é um programa que consome energia — montar o complexo ativador de caspases, clivar zimogênios, reorganizar o citoesqueleto e empacotar o conteúdo em corpos delimitados por membrana são passos que exigem ATP. Quando a lesão mitocondrial é ampla o bastante para zerar a produção energética, o programa apoptótico não pode ser executado, e a célula segue para necrose por falência osmótica. Daí a regra que organiza toda a PARTE III: *lesão mitocondrial parcial com ATP preservado tende à apoptose; lesão mitocondrial ampla com ATP zerado leva à necrose*. É por isso, também, que o mesmo insulto pode produzir apoptose no centro de uma área lesada e necrose na periferia, ou o contrário, conforme a energia disponível em cada ponto.])

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-16.png",
  largura: 48%,
  legenda: [A bifurcação dentro da mesma organela. À esquerda, a transição de permeabilidade dissipa o potencial de membrana e impede a geração de ATP — necrose. À direita, o citocromo c e outras proteínas pró-apoptóticas escapam para o citosol — apoptose. O gatilho de cima é o mesmo para os dois: cálcio citosólico elevado, espécies reativas e peroxidação lipídica.])

#subtopico("2.3 Influxo de cálcio: o mensageiro que vira faca")

Compare o cálcio a uma ferramenta guardada num armário trancado. Enquanto está trancada, ela serve para tarefas precisas, retirada e devolvida sob controle. O que a lesão faz é arrombar o armário — e a mesma ferramenta que servia para trabalhos finos passa a estar solta, em toda parte, o tempo todo.

A célula mantém o cálcio citosólico livre em torno de dez mil vezes menor que o extracelular, e essa diferença brutal é exatamente o que permite usá-lo como sinal: uma pequena entrada muda a concentração em ordens de grandeza e é lida como mensagem. Manter esse gradiente custa ATP, e há dois compartimentos de estoque interno — a mitocôndria e o retículo endoplasmático liso.

A agressão eleva o cálcio citosólico por duas frentes simultâneas. A membrana plasmática lesada deixa entrar cálcio extracelular, e os estoques internos, também sob lesão, liberam o que guardavam. O ponto que precisa ficar claro é *por que* isso lesa: não é excesso de carga positiva. O cálcio lesa porque é um ativador enzimático, e cada enzima que ele ativa destrói um alvo diferente.

A *fosfolipase* degrada os fosfolipídios da membrana, atacando justamente a estrutura cuja integridade define a reversibilidade. As *proteases* clivam proteínas de membrana e do citoesqueleto, desmontando a arquitetura que sustenta a forma celular. As *endonucleases* fragmentam o DNA — o segundo critério de irreversibilidade. E as *ATPases* consomem ATP, o que soa quase irônico: numa célula que já está em déficit energético, o cálcio elevado acelera o gasto. Além disso, o cálcio aumenta diretamente a permeabilidade mitocondrial, fechando o circuito com o mecanismo de 2.2.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-17.png",
  largura: 52%,
  legenda: [O cálcio chega de fora e dos dois estoques internos. Do aumento citosólico saem quatro braços enzimáticos, e cada um termina numa lesão nomeada: dano de membrana, dano nuclear e queda de ATP. A seta que vai para a permeabilidade mitocondrial é a que conecta este mecanismo ao anterior.])

#mini-resumo[O cálcio não lesa por carga: lesa porque ativa fosfolipase, protease, endonuclease e ATPase — e cada uma destrói um alvo distinto.]

#subtopico("2.4 Radicais livres: uma redução incompleta com consequências grandes")

O oxigênio é indispensável e perigoso pelo mesmo motivo: ele aceita elétrons com facilidade. Na cadeia respiratória, a redução completa do oxigênio a água exige quatro elétrons de uma vez, e a enzima terminal é feita para isso. Só que uma fração pequena das moléculas escapa reduzida pela metade — e é dessa redução incompleta que nascem as espécies reativas.

A sequência tem três degraus e vale seguir cada um. A adição de um elétron ao oxigênio gera o *ânion superóxido*. A enzima superóxido-dismutase converte o superóxido em *peróxido de hidrogênio* — que, atenção, não é um radical livre, porque não tem elétron desemparelhado, mas continua sendo uma espécie reativa. O terceiro degrau é o que faz a diferença: na presença de ferro na forma reduzida, o peróxido de hidrogênio origina o *radical hidroxila* pela #termo-nota[reação de Fenton][conversão do peróxido de hidrogênio em radical hidroxila catalisada por ferro reduzido; é o passo que gera a espécie mais destrutiva da série], e o radical hidroxila é a espécie mais agressiva da série.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-14.png",
  largura: 52%,
  legenda: [A geração das espécies reativas na mitocôndria e os dois destinos possíveis. À esquerda, os efeitos patológicos: peroxidação de ácidos graxos com ruptura de membranas, oxidação de proteínas com perda de atividade enzimática, oxidação de DNA com mutações e quebras. À direita, o sistema de remoção — superóxido-dismutase, glutationa-peroxidase e catalase.])

Os alvos são três e cobrem o essencial da célula. Nos *lipídios*, a peroxidação das duplas ligações dos ácidos graxos insaturados quebra a estrutura da bicamada e propaga em cadeia, porque cada lipídio oxidado gera um novo radical. Nas *proteínas*, a oxidação de resíduos altera o dobramento e destrói a atividade enzimática. No *DNA*, a oxidação de bases produz quebras e mutações.

Contra isso a célula mantém um sistema de defesa em série, e é útil ver que ele é uma linha de montagem, não três enzimas redundantes. A *superóxido-dismutase*, principalmente mitocondrial, converte o superóxido em peróxido de hidrogênio — ela não encerra o problema, apenas o transforma. A *glutationa-peroxidase* e a *catalase*, esta última peroxissomal, terminam o serviço convertendo o peróxido de hidrogênio em água. Antioxidantes não enzimáticos, como as vitaminas E e C, e proteínas que sequestram ferro e cobre livres completam a proteção — e o papel dessas proteínas de transporte fica claro justamente pela reação de Fenton: metal livre é o que permite o pior degrau da série.

#clinica-box("Lesão de reperfusão: por que restaurar o fluxo pode piorar antes de melhorar", [Reabrir uma artéria coronária ocluída é a conduta correta e salva miocárdio. Mesmo assim, uma parte das células que estavam vivas no momento da reperfusão morre depois dela, e o mecanismo é o desta seção. Durante a isquemia, as mitocôndrias ficaram danificadas e o ferro intracelular foi liberado de suas proteínas de ligação; o cálcio citosólico subiu e o sistema antioxidante foi consumido. Quando o oxigênio volta de uma vez, essas mitocôndrias comprometidas geram um pico de espécies reativas muito maior que o normal, o ferro livre alimenta a reação de Fenton, e a peroxidação lipídica atinge células que ainda estavam recuperáveis. Soma-se a isso o influxo de leucócitos trazidos pelo próprio fluxo restaurado, que liberam mais radicais e enzimas. A conclusão prática não é deixar de reperfundir — é entender que a área final de infarto tem dois componentes, o isquêmico e o de reperfusão, e que parte da pesquisa em cardiologia mira exatamente o segundo.])

#subtopico("2.5 Dano de membrana, proteínas mal dobradas e DNA: onde tudo se encontra")

Os três mecanismos anteriores parecem independentes até chegarmos à membrana. É nela que eles se encontram, e é por isso que a perda de permeabilidade é o critério mais confiável de irreversibilidade: chegar lá exige que várias frentes tenham falhado ao mesmo tempo.

A perda de fosfolipídio acontece por três caminhos que operam juntos. As espécies reativas peroxidam os ácidos graxos insaturados da bicamada, quebrando-a por dentro. A queda de ATP reduz a ressíntese de fosfolipídio, de modo que o que é perdido não é reposto. E o cálcio ativa a fosfolipase, que degrada ativamente o que restou. A esses três soma-se o dano ao citoesqueleto pelas proteases ativadas por cálcio: a membrana perde a ancoragem interna e passa a se destacar em bolhas — as mesmas bolhas que a PARTE I registrou como achado ultraestrutural.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-19.png",
  largura: 48%,
  legenda: [As frentes que convergem para o dano de membrana. À esquerda, a via das espécies reativas e da queda de ressíntese; ao centro e à direita, as vias dependentes de cálcio — degradação de fosfolipídio e dano ao citoesqueleto. Repare que perda de fosfolipídio, produtos de degradação lipídica e dano citoesquelético desembocam todos no mesmo retângulo.])

Duas membranas importam, e por razões diferentes. A ruptura da *membrana plasmática* deixa o conteúdo celular escapar e o meio externo entrar — é o critério de irreversibilidade e, como visto em 1.4, é o que coloca troponina no sangue. A ruptura da *membrana lisossômica* é mais insidiosa: o lisossomo guarda hidrolases ácidas em um compartimento fechado justamente para que elas digiram apenas o que for entregue a elas. Quando essa membrana se rompe, as hidrolases caem no citosol e digerem a célula de dentro para fora. Guarde esse passo — ele é o motor da necrose, e a PARTE III vai retomá-lo literalmente.

O último braço do mapa é o do *dano a proteínas e ao DNA*. Proteínas mal dobradas surgem por mutação, por radicais livres ou por sobrecarga de síntese. A célula responde com chaperonas, que gastam ATP tentando redobrar a proteína, e com o proteassoma, que degrada o que não tem conserto. Note a divisão de trabalho: quem tenta recuperar é a chaperona, quem destrói é o proteassoma. Quando o acúmulo excede a capacidade das duas — o chamado estresse do retículo endoplasmático — a resposta reduz a transcrição e ativa proteínas pró-apoptóticas.

O dano ao DNA segue lógica parecida. Dentro dos limites do reparo, a célula conserta e segue. Ultrapassados esses limites, a proteína p53 interrompe o ciclo celular e, se o dano persistir, ativa o programa de morte — a célula prefere morrer a se dividir com genoma corrompido.

#mini-resumo[Membrana perde fosfolipídio por três frentes simultâneas — peroxidação, queda de ressíntese e fosfolipase. Lisossomo rompido solta hidrolases e digere a célula por dentro.]

Fecha assim a PARTE II: quatro mecanismos que começam separados e terminam no mesmo lugar. A queda de ATP abre a porta para o cálcio; o cálcio agrava a permeabilidade mitocondrial; a mitocôndria comprometida gera mais espécies reativas e menos ATP; as espécies reativas destroem a membrana que continha o cálcio. Onde essa convergência termina — em necrose ou em apoptose — depende de quanta energia sobrou e de qual via de sinalização foi acionada. É essa bifurcação que a PARTE III abre.

#parte-title("PARTE III — Necrose e apoptose: os dois desfechos")

#subtopico("3.1 Duas mortes, dois mecanismos")

Há uma leitura sedutora e errada de que apoptose seria uma "necrose organizada" — a mesma coisa, feita com mais cuidado. Elas não são versões uma da outra: a ordem dos eventos é invertida, e é essa inversão que produz todas as diferenças morfológicas e clínicas.

Na *necrose*, o dano letal vem primeiro e a atividade enzimática vem depois. A célula é agredida até um ponto em que já está irremediavelmente lesada, e só então as enzimas — vindas dos próprios lisossomos e, mais tarde, dos leucócitos — desestruturam as proteínas e digerem o que sobrou. A digestão é consequência da morte.

Na *apoptose*, a ordem se inverte. Uma cascata enzimática é deliberadamente ativada, e é essa ativação que *produz* o dano letal. Nenhuma agressão externa precisou romper nada: a célula executa um programa que a desmonta por dentro, de forma ordenada, mantendo a membrana íntegra até o fim.

Dessa inversão decorre tudo o mais, e vale ver as consequências lado a lado antes de detalhar cada uma.

#table(
  columns: (auto, 1fr, 1fr),
  stroke: 0.5pt + gray-border,
  inset: 7pt,
  table.header([*Característica*], [*Necrose*], [*Apoptose*]),
  [Tamanho da célula], [aumentado — a célula incha por entrada de água], [reduzido — a célula se contrai],
  [Núcleo], [picnótico, depois fragmentado, depois ausente], [fragmentado em pedaços do tamanho de nucleossomos],
  [Membrana plasmática], [rompida], [íntegra, com estrutura de superfície alterada],
  [Conteúdo celular], [digerido enzimaticamente e extravasado], [intacto, empacotado em corpos apoptóticos],
  [Inflamação adjacente], [presente e obrigatória], [ausente],
  [Papel no organismo], [sempre patológico], [fisiológico ou patológico],
)

#atencao-box("O divisor real é a membrana, não o tamanho", [O aluno tende a guardar a diferença pelo par "incha versus encolhe", e esse par funciona para reconhecer, mas não explica nada. O divisor mecanístico é a *integridade da membrana plasmática*, e dele decorrem os outros itens da tabela. Como a membrana da célula necrótica se rompe, o conteúdo citoplasmático — enzimas lisossômicas, proteínas desnaturadas, moléculas que normalmente nunca circulam — se derrama no interstício, é reconhecido pelo sistema imune como sinal de dano e recruta leucócitos: por isso a inflamação é obrigatória na necrose. Como a membrana da célula apoptótica permanece íntegra e o conteúdo é empacotado em corpos delimitados por membrana antes de qualquer vazamento, nada é liberado no interstício e o fagócito remove os pacotes silenciosamente: por isso não há inflamação. É a mesma razão pela qual a necrose coloca troponina no sangue e a apoptose não coloca nada.])

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-26.png",
  largura: 62%,
  legenda: [Os dois caminhos a partir da mesma célula normal. À esquerda, a lesão reversível (bolhas, retículo e mitocôndrias dilatados) com a seta de recuperação ainda disponível, e depois a necrose, com ruptura de membrana, extravasamento e leucócitos chegando. À direita, a apoptose: contração, condensação da cromatina, fragmentação em corpos apoptóticos e fagocitose — sem nenhuma célula inflamatória na cena.])

#subtopico("3.2 Necrose: digestão por dentro, inflamação por fora")

Imagine um prédio cujas tubulações de produto químico corrosivo estivessem todas dentro de compartimentos lacrados. Enquanto os lacres resistem, o prédio funciona. Quando o incêndio compromete os lacres, o corrosivo se espalha — e o prédio passa a ser destruído por aquilo que ele mesmo guardava. A necrose funciona assim, e o incêndio é a combinação de acidose com perda de permeabilidade que a PARTE II construiu.

A cascata tem quatro passos e o slide os coloca em ordem. As alterações irreversíveis de pH e permeabilidade rompem a membrana lisossômica, e as enzimas lisossômicas são *liberadas no citosol* — a digestão começa de dentro. Ao mesmo tempo, a membrana plasmática rompida deixa *proteínas e enzimas escaparem para o meio extracelular*. A digestão intracelular desestrutura a célula; o extravasamento sinaliza dano ao tecido e *recruta células inflamatórias*, que chegam trazendo mais enzimas e mais espécies reativas e aceleram a digestão do que restou.

O eixo *célula contra arcabouço* que fecha a figura é a chave da próxima seção, e vale entendê-lo agora. Todo tecido tem duas coisas: as células e a trama de matriz extracelular e vasos que as sustenta. A necrose sempre mata as células; o que varia entre um tecido e outro é se a trama resiste ou é destruída junto. Quando o arcabouço permanece, o contorno do tecido é preservado por dias e reconhecemos a arquitetura mesmo sem células vivas. Quando o arcabouço é destruído, o tecido colapsa e vira uma massa liquefeita.

Ao microscópio, três achados definem a célula necrótica, e cada um tem explicação mecanística direta. O primeiro é a *eosinofilia* — a célula fica mais rosa que a vizinha normal. Isso acontece por dois motivos somados: ela perde RNA ribossômico, que era basófilo e puxava a coloração para o azul, e suas proteínas citoplasmáticas se desnaturam, expondo mais sítios que ligam eosina.

Os outros dois achados são nucleares, e é importante ver que não são categorias paralelas, e sim etapas de uma mesma sequência. Primeiro vem a #termo-nota[picnose][retração do núcleo com condensação da cromatina numa massa basófila densa e homogênea], em que o núcleo encolhe e a cromatina se condensa numa massa escura. Depois vem a #termo-nota[cariorrexe][fragmentação do núcleo picnótico em pedaços de cromatina dispersos pelo citoplasma], com o núcleo picnótico se quebrando em fragmentos. Por fim, a #termo-nota[cariólise][dissolução da basofilia nuclear pela ação das endonucleases, até o núcleo desaparecer da lâmina], em que as endonucleases digerem o DNA e a basofilia desaparece — o núcleo simplesmente some, e o que sobra é o contorno citoplasmático anucleado que chamamos de célula-fantasma.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-27.png",
  largura: 48%,
  legenda: [Em cima, neurônios eosinofílicos ("neurônios vermelhos") destacando-se do parênquima cerebral por perda de RNA e desnaturação proteica. Embaixo, hepatócitos necróticos com núcleos picnóticos e em cariorrexe ao lado de hepatócitos ainda preservados — o contraste dentro do mesmo campo é o que treina o olho.])

#mini-resumo[Lisossomo rompido digere por dentro; membrana rompida extravasa por fora e chama inflamação. Eosinofilia é perda de RNA mais desnaturação; picnose, cariorrexe e cariólise são três tempos do mesmo núcleo.]

#subtopico("3.3 Os padrões de necrose: o que o arcabouço decide")

Os padrões morfológicos de necrose costumam ser apresentados como uma lista de nomes a decorar, e é por isso que eles escorregam da memória. Organizados pelo eixo da seção anterior — o que aconteceu com o arcabouço e qual enzima predominou —, eles param de ser lista e viram consequência.

#table(
  columns: (auto, 1fr, auto),
  stroke: 0.5pt + gray-border,
  inset: 7pt,
  table.header([*Padrão*], [*Mecanismo que o define*], [*Onde ocorre*]),
  [Coagulativa],
  [a acidez desnatura as proteínas estruturais *e* as enzimas lisossômicas; sem enzima ativa, a digestão fica bloqueada e o arcabouço permanece],
  [órgãos sólidos de circulação terminal — coração, baço, rim],
  [Liquefativa],
  [as hidrolases predominam e digerem tudo, inclusive o arcabouço; o tecido vira massa viscosa],
  [encéfalo e focos de infecção bacteriana (abscessos)],
  [Caseosa],
  [necrose no centro de um granuloma; células fragmentadas em meio a debris amorfos, com halo de células inflamatórias],
  [tuberculose e outras infecções granulomatosas],
  [Gordurosa],
  [lipase pancreática extravasada hidrolisa o triglicerídeo; o ácido graxo liberado precipita com cálcio],
  [pancreatite aguda e gordura peripancreática],
  [Fibrinoide],
  [imunocomplexos depositados na parede do vaso, somados a fibrina extravasada, formam material rosa-brilhante],
  [vasculites por complexo antígeno-anticorpo],
  [Gangrenosa],
  [termo clínico para necrose de um segmento, em geral coagulativa; se houver infecção bacteriana superposta, torna-se liquefativa],
  [membros, especialmente inferiores],
)

A *necrose coagulativa* é o padrão mais comum e o mais contraintuitivo pelo nome. Ela nada tem a ver com coagulação do sangue: o que coagula são as proteínas da própria célula. A acidose intensa da isquemia desnatura tudo — inclusive as enzimas lisossômicas que fariam a digestão. Com as enzimas desativadas, a digestão é bloqueada e o arcabouço permanece de pé por dias. É por isso que o miocárdio infartado, olhado ao microscópio nas primeiras horas, mostra fibras com contorno preservado, eosinofílicas e sem núcleo — as células-fantasma. A digestão só ocorre depois, quando os leucócitos chegam trazendo enzimas de fora.

#confusao-prevista(
  titulo: "Necrose coagulativa não tem relação com coágulo sanguíneo",
  aluno_acha: [aluno associa "coagulativa" à formação de trombo ou à coagulação do sangue no vaso],
  mecanismo: [o nome descreve o aspecto das *proteínas intracelulares*, que se desnaturam e se agregam como clara de ovo cozida. A consequência funcional é o bloqueio da digestão enzimática pela própria acidez — as hidrolases lisossômicas são proteínas e se desnaturam junto. O tecido preserva a arquitetura porque ninguém a digeriu, não porque algo coagulou no vaso. A oclusão vascular é a *causa* da isquemia; a coagulação proteica é o *efeito* dentro da célula.],
)

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-28.png",
  largura: 46%,
  legenda: [Necrose coagulativa. À esquerda, miocárdio infartado: as fibras mantêm o contorno e a estriação, mas perderam o núcleo e ficaram intensamente eosinofílicas — fantasmas de células —, com neutrófilos infiltrando entre elas. À direita, o mesmo padrão em rim: arquitetura tubular reconhecível, células anucleadas.])

A *necrose liquefativa* é o oposto exato: as hidrolases dominam e digerem tudo, inclusive a trama de sustentação. Dois contextos a produzem. O primeiro é a infecção bacteriana, em que os neutrófilos recrutados despejam grande quantidade de enzimas — o resultado é o pus, e a cavidade que sobra é o abscesso. O segundo é a isquemia do sistema nervoso central, e este é o achado que costuma surpreender: o encéfalo liquefaz mesmo em isquemia estéril, sem bactéria nenhuma, porque tem pouca matriz extracelular de sustentação e alto conteúdo lipídico e enzimático. O infarto cerebral evolui para uma cavidade cística, não para uma cicatriz firme como a do coração.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-29.png",
  largura: 46%,
  legenda: [Necrose liquefativa. À esquerda, pulmão com cavidades de abscesso. Ao centro, encéfalo com área amolecida e escavada após infarto — sem bactéria envolvida. À direita, o correspondente microscópico: parênquima desestruturado, sem arquitetura reconhecível.])

A *necrose caseosa* aparece no centro do #termo-nota[granuloma][coleção organizada de macrófagos ativados, muitas vezes circundada por linfócitos, formada quando o agente agressor resiste à eliminação] e recebe o nome do aspecto macroscópico branco-amarelado e friável, semelhante a queijo. Microscopicamente, é uma área amorfa e granular, com restos de células fragmentadas, cercada por um halo inflamatório — o próprio granuloma. É característica da tuberculose, mas não é exclusiva dela: o padrão sugere infecção granulomatosa e orienta a investigação, sem fechar o diagnóstico sozinho.

A *necrose gordurosa* é a que melhor mostra que a enzima define o padrão. Na pancreatite aguda, as enzimas do pâncreas são ativadas dentro do próprio órgão em vez de no duodeno, e a lipase extravasada hidrolisa os triglicerídeos da gordura peripancreática. Os ácidos graxos liberados se combinam com cálcio e precipitam — a saponificação —, produzindo focos brancos, opacos e de aspecto giz.

#clinica-box("Pancreatite aguda: por que o cálcio sérico cai", [Na pancreatite aguda grave, o paciente pode apresentar hipocalcemia, e a explicação está inteiramente no mecanismo desta seção. A lipase pancreática extravasada hidrolisa os triglicerídeos do tecido adiposo peripancreático e mesentérico, liberando grande quantidade de ácidos graxos livres. Esses ácidos graxos se ligam ao cálcio e precipitam como sabões de cálcio nas áreas de necrose gordurosa — o cálcio sai do plasma e fica sequestrado no tecido. A queda do cálcio sérico é, portanto, marcador indireto da extensão da necrose gordurosa e um dos elementos que compõem os escores de gravidade da doença. É um bom exemplo de como um achado laboratorial aparentemente distante do órgão doente se explica pela enzima que vazou.])

A *necrose fibrinoide* é um padrão exclusivamente microscópico, encontrado em paredes de vasos. Complexos antígeno-anticorpo se depositam ali e, somados à fibrina que extravasa do plasma, produzem um material amorfo, intensamente rosa e brilhante ao H&E. É o achado que caracteriza as vasculites de mecanismo imune.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-34.png",
  largura: 42%,
  legenda: [Necrose fibrinoide. A parede arterial está substituída por material amorfo e intensamente eosinofílico, e a luz do vaso está reduzida — as hemácias em vermelho vivo marcam o lúmen estreitado. Não há arquitetura muscular reconhecível na parede.])

A *necrose gangrenosa*, por fim, não é um mecanismo novo: é um termo clínico para necrose que compromete um segmento inteiro do corpo, tipicamente um membro, e envolve múltiplos tecidos ao mesmo tempo. Na forma seca, o padrão histológico é coagulativo. Quando uma infecção bacteriana se superpõe e traz digestão enzimática, o quadro passa a ter componente liquefativo e chamamos de gangrena úmida.

#subtopico("3.4 Apoptose: quando desmontar é a decisão certa")

A necrose é sempre patológica — nenhum organismo depende dela para funcionar. A apoptose é o contrário: boa parte dela é fisiológica e indispensável, e entender isso muda a forma de encarar a morte celular.

Entre as *situações fisiológicas*, a mais visível é a embriogênese: a separação dos dedos, o fechamento do tubo neural e a remodelação de estruturas transitórias dependem de eliminar células em locais precisos. A involução hormônio-dependente é o segundo caso — o endométrio no fim do ciclo menstrual e a mama após a lactação reduzem o *número* de células por apoptose, o que é diferente da atrofia por desuso, que reduz principalmente o *tamanho*. A tolerância imunológica é o terceiro: linfócitos que reconhecem antígenos do próprio corpo são eliminados por apoptose durante a maturação, e é isso que impede a autoimunidade. O quarto é a morte de células inflamatórias residentes depois que a resposta cumpriu sua função — sem essa retirada programada, a inflamação não termina.

Entre as *situações patológicas*, quatro se destacam e todas já apareceram na PARTE II. Dano ao DNA acima da capacidade de reparo aciona a via do p53. Acúmulo de proteínas mal dobradas, quando chaperonas e proteassoma não dão conta, produz o estresse do retículo endoplasmático. Infecções, especialmente por organismos intracelulares, disparam apoptose por duas frentes — o próprio patógeno e o linfócito T citotóxico que reconhece a célula infectada. E a atrofia patológica de órgãos parenquimatosos após obstrução de ducto, como no pâncreas e no rim, elimina células que perderam a razão funcional de existir.

A morfologia acompanha o programa passo a passo. A célula *se contrai* — o citoplasma fica denso e as organelas se compactam. A *cromatina se condensa* em massas nítidas junto ao envoltório nuclear, e essa é a alteração mais característica ao microscópio. A membrana forma *bolhas* que se destacam levando pedaços de citoplasma e de núcleo, e cada bolha destacada vira um *corpo apoptótico* — um pacote delimitado por membrana íntegra, com organelas preservadas dentro. Por fim, os corpos apoptóticos são *fagocitados por macrófagos* antes que qualquer coisa vaze.

Uma consequência prática vale registrar: como cada célula apoptótica é removida individualmente e sem inflamação, a apoptose é *difícil de ver* numa lâmina. Ao contrário da necrose, que produz áreas confluentes com infiltrado, a apoptose aparece como células isoladas, retraídas e intensamente eosinofílicas, com cromatina condensada — passa despercebida se o olho não estiver procurando.

#subtopico("3.5 As duas vias e a família Bcl-2")

O programa apoptótico se organiza em quatro fases, e vale nomeá-las antes de entrar nos detalhes moleculares, porque elas dão o esqueleto: *sinalização* (o que dispara), *controle e integração* (o que decide se o disparo vira execução), *execução* (a demolição propriamente dita) e *remoção* dos fragmentos. As duas vias clássicas se diferenciam apenas na primeira fase — a partir da execução, elas são idênticas.

A *via intrínseca*, ou mitocondrial, responde a sinais de dentro da célula: perda de fatores de crescimento e de sinais de sobrevivência, dano ao DNA, proteína mal dobrada. Em condições normais, proteínas anti-apoptóticas da família Bcl-2 — a própria Bcl-2, a Bcl-xL e a Mcl-1 — mantêm a membrana mitocondrial externa fechada. Quando o sinal de sobrevivência falta, proteínas sensoras da mesma família são ativadas e antagonizam as anti-apoptóticas. Livres desse freio, os efetores *Bax* e *Bak* se agregam na membrana mitocondrial externa e formam canais. Por esses canais escapa o citocromo c, que no citosol se liga à *Apaf-1* e monta o complexo que ativa a *caspase-9*.

A *via extrínseca*, ou dos receptores de morte, responde a sinais de fora. Receptores da superfamília do #sigla("TNF", [fator de necrose tumoral — citocina que sinaliza através de receptores com domínio de morte]) — o Fas e o receptor de TNF — carregam no lado citoplasmático um segmento chamado domínio de morte. Quando o ligante correspondente se acopla, três receptores se agrupam, os domínios de morte se aproximam e recrutam a proteína adaptadora #sigla("FADD", [proteína adaptadora que conecta o domínio de morte do receptor à pró-caspase-8]). Note a divisão de papéis: o receptor recebe o sinal, o FADD faz a ponte, e quem é ativado é a *pró-caspase-8*, que se ativa por autocatálise ao ser concentrada nesse complexo.

As duas vias convergem nas *caspases executoras* — as caspases 3, 6 e 7. Aqui é útil fixar a hierarquia, porque ela é fonte constante de troca: caspase-8 e caspase-9 são *iniciadoras*, cada uma no topo de uma via; caspases 3, 6 e 7 são *executoras*, e são elas que fazem a demolição. Toda #termo-nota[caspase][protease que corta proteínas após resíduos de aspartato e é sintetizada como zimogênio inativo, ativada por clivagem] é sintetizada como zimogênio inativo justamente porque uma protease dessas solta no citosol seria letal por acidente.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-38.png",
  largura: 62%,
  legenda: [À esquerda, a via intrínseca: a célula viável (A) mantém Bcl-2 segurando o citocromo c dentro da mitocôndria; na apoptose (B), a falta de sinal de sobrevivência ou o dano ao DNA ativa sensores que antagonizam Bcl-2, abrindo o canal de Bax/Bak. À direita, a via extrínseca: FasL agrupa três Fas, os domínios de morte recrutam FADD, a pró-caspase-8 se ativa por autocatálise e aciona as caspases executoras.])

O que as executoras fazem é a demolição ordenada. Elas clivam proteínas do citoesqueleto e da lâmina nuclear, o que explica a contração celular e a fragmentação do núcleo. Elas ativam uma endonuclease que corta o DNA entre os nucleossomos, produzindo fragmentos de tamanho regular — diferente da digestão difusa e aleatória da necrose. E promovem alterações na superfície da membrana que sinalizam ao macrófago que aquele pacote deve ser ingerido, o que garante a remoção silenciosa.

O balanço entre proteínas pró e anti-apoptóticas é o que decide o desfecho, e o slide o organiza em dois lados. Do lado *pró-apoptótico*: a liberação do citocromo c, os efetores Bax e Bak, a Apaf-1 e o par Fas/FasL com o receptor de TNF. Do lado *anti-apoptótico*: Bcl-2, Bcl-xL e Mcl-1 segurando a mitocôndria, as proteínas inibidoras da apoptose atuando sobre as caspases já ativadas, e a #sigla("FLIP", [proteína que se liga ao complexo do receptor de morte sem clivar a pró-caspase-8, bloqueando a via extrínseca]), que ocupa o lugar da pró-caspase-8 no complexo do receptor sem se deixar clivar. A célula não decide morrer por um sinal isolado — ela integra a razão entre os dois lados.

#subtopico("3.6 Necroptose e o significado clínico do desequilíbrio")

Existe um ponto em que a dicotomia necrose-apoptose deixa de dar conta, e nomeá-lo é honesto com o estado atual do assunto. A *necroptose*, ou necrose programada, tem a sinalização regulada de uma apoptose e o desfecho morfológico de uma necrose — e a condição que a produz é justamente a falha da apoptose.

O gatilho parte do mesmo receptor da via extrínseca. O TNF se liga ao seu receptor e recruta a proteína RIP1. Se a caspase-8 for ativada normalmente, o complexo segue para apoptose. Se a caspase-8 *não* for ativada — situação que alguns vírus produzem deliberadamente, ao codificar inibidores de caspase para impedir o suicídio da célula que estão infectando —, o RIP1 se associa ao RIP3 formando o necrossomo. Esse complexo desencadeia alterações metabólicas que derrubam o ATP, elevam as espécies reativas, peroxidam lipídios e permeabilizam a membrana lisossômica. O resultado é perda de integridade celular com extravasamento e inflamação: morfologia de necrose, sinalização de programa. Do ponto de vista do organismo, é uma saída de emergência — se o vírus bloqueou a apoptose, a célula infectada morre de outro jeito.

#figura-nebli("/figuras/patologia-01-lesao-morte-celular/slide-45.png",
  largura: 58%,
  legenda: [A bifurcação a partir do receptor de TNF. À direita, a ativação da caspase-8 leva à morte por apoptose. À esquerda, a falha em ativar a caspase-8 permite a formação do necrossomo RIP1-RIP3, com queda de ATP, aumento de espécies reativas, peroxidação lipídica e permeabilização lisossômica — morte por necroptose.])

Fechando a PARTE III, vale ver o que acontece quando o balanço apoptótico se desloca para um dos lados, porque é aí que a fisiologia vira doença. *Apoptose insuficiente* deixa sobreviver células que deveriam ter sido eliminadas, e o resultado tem duas faces: linfócitos autorreativos que escapam da tolerância alimentam doenças autoimunes, e células com dano genômico que deveriam ter sido removidas pela via do p53 acumulam mutações e alimentam neoplasias. *Apoptose excessiva* elimina células que fazem falta, e o exemplo clássico é o das doenças neurodegenerativas, em que a perda progressiva de neurônios que não se repõem produz déficit permanente.

Vale ainda registrar o papel duplo do TNF, que sintetiza bem o princípio de balanço desta PARTE: a mesma citocina que ativa a via dos receptores de morte também induz a produção de proteínas anti-apoptóticas como Bcl-2 e Bcl-xL. O que a célula faz diante do TNF não está escrito no sinal — está no estado interno dela no momento em que o sinal chega.

#conclusao-box[
  *O princípio que une as três PARTES* é que a lesão celular é um problema de energia e de barreira. A célula normal gasta ATP continuamente para manter gradientes iônicos e para manter compartimentos fechados; toda agressão relevante age reduzindo a energia disponível, rompendo os compartimentos, ou as duas coisas. Adaptação é conseguir manter os dois; lesão reversível é perdê-los temporariamente; lesão irreversível é perdê-los de forma que não pode ser reconstruída.

  *O mecanismo nuclear* é a convergência dos quatro caminhos da PARTE II num único ponto. A queda de ATP abre a porta para o cálcio; o cálcio ativa fosfolipases e proteases e agrava a permeabilidade mitocondrial; a mitocôndria comprometida produz menos ATP e mais espécies reativas; as espécies reativas destroem a membrana que continha o cálcio. Nenhum dos quatro age sozinho, e é essa realimentação que transforma uma lesão inicialmente reversível em morte celular. A energia que sobra no momento da convergência decide o desfecho: com ATP, apoptose ordenada e silenciosa; sem ATP, necrose com extravasamento e inflamação.

  *A clínica retomada pelo mecanismo:* a troponina no sangue do paciente infartado só existe porque a membrana do cardiomiócito deixou de ser barreira — o exame é uma leitura direta do primeiro critério de irreversibilidade. A hipocalcemia da pancreatite grave é a lipase extravasada precipitando cálcio no tecido adiposo. A cavidade cística que sobra de um infarto cerebral, contra a cicatriz firme que sobra de um infarto do miocárdio, é a diferença entre um arcabouço destruído e um arcabouço preservado. Em todos os casos o achado clínico é a consequência visível de um passo bioquímico que você agora consegue nomear.

  *Para onde isso avança:* a célula necrótica não fica onde está. O conteúdo extravasado recruta leucócitos, e esse recrutamento é o começo da inflamação aguda — o tema que naturalmente se segue a este. Depois da inflamação vem o reparo, e é ali que o eixo célula contra arcabouço reaparece com força: tecido com arcabouço preservado e células capazes de se dividir regenera; tecido sem arcabouço ou com células que não se repõem cicatriza com fibrose. A morte celular é o primeiro capítulo dessa sequência, não um assunto fechado em si mesmo.
]
