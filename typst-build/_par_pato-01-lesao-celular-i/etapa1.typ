#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Uma célula saudável não está parada: ela gasta energia o tempo todo para manter tudo dentro dos limites — sódio fora, potássio dentro, cálcio guardado em compartimentos, membranas íntegras, proteínas dobradas do jeito certo. Esse estado de trabalho constante e equilibrado é a homeostase. Quando alguma coisa de fora empurra a célula para longe desse ponto, ela tem duas saídas: mudar o próprio funcionamento até encontrar um novo equilíbrio, o que se chama adaptação, ou não dar conta e entrar em lesão.

  A pergunta que organiza esta apostila inteira é uma só: *até onde a célula lesada ainda consegue voltar, e o que exatamente a impede de voltar*. Existe uma lesão que se desfaz quando o agressor sai de cena, e existe uma lesão que já não se desfaz mais, porque a própria maquinaria de sobrevivência foi destruída. Entre uma e outra passa um ponto sem retorno, e reconhecer de que lado do ponto o paciente está muda a conduta na beira do leito.

  A PARTE I estabelece o mapa: homeostase, adaptação, lesão reversível, lesão irreversível e as causas que disparam tudo isso. A PARTE II mostra o que se vê e em que ordem — por que a bioquímica denuncia a lesão horas antes de o microscópio mostrar qualquer coisa, e quais são os dois eventos que definem a irreversibilidade. A PARTE III abre o motor: queda de ATP, radicais livres, dano mitocondrial e influxo de cálcio, os quatro processos que, somados, empurram a célula para além do ponto de retorno.
]

#parte-title("PARTE I — Do equilíbrio ao ponto sem retorno", primeira: true)

#subtopico("1.1 — A célula normal e as três saídas possíveis")

O ponto de partida é sempre a célula normal, em homeostase. Homeostase, aqui, não significa imobilidade: significa que a célula consegue manter suas concentrações internas, suas membranas e suas proteínas dentro da faixa em que trabalha bem, gastando energia para isso. Um tecido em homeostase é um tecido que está dando conta do serviço que lhe pedem.

Em algum momento, um estímulo tira essa célula do seu ponto de equilíbrio. E aí abrem-se três saídas, que dependem do quanto e do quão rápido o estímulo aperta.

A primeira saída é a *adaptação*. Quando a agressão é de baixa intensidade e se estende no tempo, a célula tem tempo de mudar quais proteínas fabrica e em que quantidade, e com isso encontra um novo ponto de equilíbrio. Isso acontece conosco todos os dias. Quem começa a levantar peso submete a musculatura a um estresse mecânico repetido e moderado; o organismo responde construindo mais massa contrátil e passa a operar num novo patamar. Adaptação, portanto, não é sinônimo de dano — é uma resposta bem-sucedida.

A segunda saída é a *lesão celular*. Quando o dano é rápido demais ou intenso demais, a célula não tem tempo nem substrato para fazer os ajustes bioquímicos e moleculares que a adaptação exige, e passa a funcionar mal. Um indivíduo destreinado que faz um esforço muito intenso aumenta abruptamente a demanda de oxigênio do miocárdio; o suprimento sanguíneo não acompanha, e as células do coração começam a sofrer. A dor no peito é o sinal externo dessa lesão.

A terceira saída aparece quando a lesão não é interrompida: a *morte celular*, que pode ocorrer por necrose ou por apoptose. Estas duas formas de morte já foram vistas em detalhe; aqui elas interessam como desfecho para o qual os mecanismos desta aula convergem.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-03-organograma.png",
  largura: 62%,
  legenda: [O mapa da aula inteira. Da célula normal saem duas setas: estresse leve leva à adaptação, estímulo agressor leva à lesão celular. Repare na seta que sobe pela direita — a lesão reversível devolve a célula ao normal quando o estímulo é leve e transitório. A seta que desce, com estímulo grave e progressivo, chega à lesão irreversível e daí à morte por necrose ou apoptose. Note também a seta pontilhada: a incapacidade de se adaptar é, ela própria, uma porta de entrada para a lesão. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

#subtopico("1.2 — O que decide entre adaptar-se e lesar-se")

Duas variáveis decidem o destino da célula: a intensidade do estímulo e o tempo pelo qual ele age. Elas não agem separadamente — é a combinação das duas que determina a saída.

A adaptação exige tempo. Modificar a expressão de proteínas, montar filamentos novos, remodelar organelas: nada disso acontece em segundos. A hipertrofia cardíaca da hipertensão arterial é o exemplo mais limpo. O aumento da resistência vascular periférica obriga o coração a gerar pressões de contração maiores a cada batimento; para dar conta, o cardiomiócito aumenta o número de filamentos contráteis que possui, e a parede do ventrículo espessa. Essa hipertrofia cardíaca da hipertensão só é possível porque o estímulo é leve e prolongado, o que dá à célula tempo de fabricar novos filamentos contráteis.

A adaptação também pode ir no sentido oposto, reduzindo a célula em vez de aumentá-la. Um paciente com lesão medular que fica restrito ao leito perde estímulo mecânico sobre a musculatura esquelética, que atrofia. Na doença de Alzheimer, a perda progressiva de sinapses e de neurônios se traduz numa atrofia cortical visível. Aumentar ou diminuir, nos dois casos, é a mesma lógica: um ajuste lento a uma demanda que mudou.

Quando o estímulo é intenso, ou quando cresce depressa demais, esse tempo não existe. A célula é apanhada com a maquinaria antiga diante de uma demanda nova, e o resultado é lesão. Vale guardar a inversão que costuma confundir: o que torna um estímulo adaptável não é ele ser fraco, é ele ser *lento*.

#confusao-prevista(
  titulo: "Adaptação não é o mesmo que lesão leve",
  aluno_acha: [aluno lê adaptação como um grau menor de lesão, o primeiro degrau de uma escada que termina na morte celular],
  mecanismo: [adaptação é uma resposta bem-sucedida: a célula chegou a um *novo equilíbrio* e voltou a funcionar bem nele. Lesão é o contrário — a célula não conseguiu chegar a equilíbrio nenhum e está funcionando mal. Por isso o organograma coloca as duas em ramos separados, ligados apenas pela seta pontilhada da incapacidade de se adaptar.],
)

#subtopico("1.3 — Lesão reversível e lesão irreversível")

Dentro da lesão celular há dois estados diferentes, e a diferença entre eles é a coisa mais importante desta aula.

Na *lesão reversível*, o estímulo é moderado a alto, mas transitório. A célula perde função e acumula alterações internas, porém a maquinaria que a mantém viva continua de pé. Se o agressor for retirado a tempo, ela reconstrói o que perdeu e volta ao estado normal. É o que acontece com o corredor destreinado que sente dor no peito, para de correr, restabelece o fluxo coronariano e volta ao normal sem sequela.

Na *lesão irreversível*, o estímulo é intenso e progressivo — ele não cessa, ele piora ao longo do tempo. Em algum ponto, a célula cruza uma linha a partir da qual retirar o agressor já não adianta. Ela vai morrer, por necrose ou por apoptose. O infarto agudo do miocárdio é o exemplo canônico: passado o ponto de retorno, aquelas células estão perdidas.

Vale notar que nem toda lesão irreversível vem de isquemia. Um vírus que infecta o hepatócito, se multiplica dentro dele e o destrói produz lesão irreversível por uma via totalmente diferente, como acontece na hepatite aguda. O que define a irreversibilidade não é a causa, é o estado final da célula.

#clinica-box("Angina e infarto: a mesma artéria, dois estados",
  [O paciente que chega ao pronto-socorro com dor em aperto no peito irradiada para o braço e para a mandíbula tem, em ambos os casos, sofrimento isquêmico do miocárdio. A diferença está no lado do ponto de retorno em que ele se encontra. Se as células ainda estão em lesão reversível, restabelecer a oxigenação devolve a função e não há morte celular — este quadro de dor torácica sem morte celular chama-se angina. Se já houve lesão irreversível, houve infarto: as células perdidas não voltam, e o que se salva é o que ainda não morreu. Toda a urgência do atendimento existe porque essa linha está sendo cruzada enquanto o paciente espera.])

#subtopico("1.4 — As causas de lesão celular")

As agressões capazes de tirar a célula da homeostase são de sete grandes tipos, e vale percorrê-los porque cada um deles reaparece adiante como disparador de um mecanismo específico.

A *privação de oxigênio* é a mais prevalente e a mais comum de todas, e é ela que serve de fio condutor para o resto da aula. Ela pode vir de queda da perfusão, de aumento da demanda ou de falta de oxigênio no ar inspirado.

Os *agentes físicos* incluem temperatura e radiação. Uma exposição solar moderada gera dano ultravioleta às células epiteliais de revestimento que ainda cabe numa resposta adaptativa; uma exposição excessiva destrói diretamente essas células, e a destruição desencadeia inflamação — é o quadro clínico da queimadura solar.

Os *agentes químicos e drogas* agem por dano químico direto. A fumaça do cigarro, em exposição prolongada e moderada, provoca adaptação do epitélio respiratório; em intensidade maior, provoca lesão irreversível das células de revestimento.

Os *agentes infecciosos* podem destruir a célula de dentro para fora, como o vírus que prolifera no hepatócito da hepatite aguda.

As *reações imunológicas* colocam o próprio sistema imune como agressor, seja em alergias, seja em doenças autoimunes. Há ainda uma situação particular: quando o microrganismo vive dentro da célula, como na tuberculose e em várias viroses, a resposta imune normalmente elimina o agente destruindo a célula infectada. A célula morre pela defesa, não pelo micróbio.

Os *desarranjos genéticos* — translocações e outras grandes modificações do material genético — levam à perda de função celular. E o *desbalanço nutricional* retira da célula os substratos de que suas reações bioquímicas dependem.

#mini-resumo[Sete famílias de causas, um mesmo funil: todas terminam empurrando a célula para adaptação, para lesão reversível ou para lesão irreversível, dependendo de quanto apertam e por quanto tempo.]

#parte-title("PARTE II — O que se enxerga, e quando se enxerga")

#subtopico("2.1 — A ordem em que os achados aparecem")

Há uma defasagem entre o que a célula está sofrendo e o que conseguimos detectar, e essa defasagem tem consequência clínica direta.

A primeira coisa que se altera na lesão celular é o desempenho: a célula deixa de fazer bem aquilo que fazia. Logo em seguida vêm as alterações bioquímicas, dosáveis em exames. Depois delas aparecem as alterações ultraestruturais, que só o microscópio eletrônico revela. Só mais tarde surgem as alterações no microscópio de luz. E por último aparecem as alterações macroscópicas, visíveis a olho nu na peça.

Repare na ordem, porque ela inverte a intuição de quem espera enxergar o dano para acreditar nele. Quando uma isquemia miocárdica é detectada apenas na macroscopia, ela já ultrapassou a fase reversível: a alteração macroscópica de um infarto só se torna visível quando a lesão já é irreversível. Por isso o diagnóstico precoce é decisivo. Reconhecer a isquemia enquanto a lesão ainda é reversível e restabelecer o fluxo devolve o tecido às condições normais; reconhecê-la depois do infarto instalado apenas impede que mais células morram, sem recuperar as que já se perderam.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-11-curva-tempo.png",
  largura: 66%,
  legenda: [O eixo horizontal é a duração da lesão e o vertical, a magnitude de cada efeito. A curva vermelha é a função celular, a primeira a despencar. As demais são detecções, e cada uma entra mais tarde: alterações bioquímicas, ultraestruturais, de microscópio de luz e, por último, macroscópicas. A linha pontilhada vertical marca o ponto de retorno. Note que ela separa a zona rosa da azul: quase tudo o que o olho consegue ver já está do lado irreversível. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

Um detalhe importante: a posição dessa linha pontilhada não é a mesma para todos os tecidos. Células mais resistentes toleram mais tempo e mais alterações antes de cruzá-la, e nelas a linha está deslocada para a direita. Já o tempo de lesão reversível é curtíssimo em células sensíveis como o neurônio, cuja linha está muito próxima da origem do eixo. É por isso que poucos minutos de parada circulatória bastam para lesar irreversivelmente o encéfalo, enquanto outros tecidos suportam intervalos bem maiores.

#subtopico("2.2 — A morfologia da lesão reversível")

Na lesão reversível a discrepância entre o que se vê ao microscópio de luz e o que se vê ao microscópio eletrônico é enorme. Ao microscópio de luz, o achado que caracteriza a lesão celular reversível é o edema celular, e no máximo aparece uma alteração gordurosa — a esteatose —, que é um achado inespecífico e será estudada na aula de acúmulos. É pouco, e é pouco específico.

A riqueza está na ultraestrutura, e ela decorre de um encadeamento simples de entender. Com as funções bioquímicas em queda, a célula perde o controle do pH e do equilíbrio hidroeletrolítico, e a membrana plasmática sofre. A alteração mais característica vem da perda do acoplamento entre a membrana plasmática e o citoesqueleto: sem essa ancoragem, a membrana se solta em bolhas na superfície da célula, e essas bolhas se chamam blebs. Nas células que possuem microvilosidades, como as intestinais e as do túbulo renal, as microvilosidades desaparecem.

As organelas acompanham. As mitocôndrias incham e acumulam corpos amorfos no seu interior. O retículo endoplasmático se dilata, e os ribossomos que estavam aderidos a ele se desprendem. No núcleo, a cromatina condensa e alguns elementos fibrilares e granulares se desagregam.

Nada disso precisa ser decorado no nível do detalhe ultraestrutural isolado. O que importa é enxergar que todas essas alterações são a expressão morfológica de uma mesma falência energética, cujo mecanismo a PARTE III vai abrir.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-13-ultraestrutura.png",
  largura: 40%,
  legenda: [Acima, a célula normal com contorno regular e organelas compactas. Abaixo, a mesma célula em lesão reversível: contorno deformado pelas bolhas de membrana, os blebs, e organelas edemaciadas — retículo endoplasmático e mitocôndrias dilatados. A seta de retorno indica o essencial: até aqui, retirado o agressor, a célula se recompõe. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

#subtopico("2.3 — O túbulo renal como caso de leitura")

O túbulo renal, que reabsorve íons durante a filtração do sangue e a formação da urina, oferece uma comparação didática das três situações lado a lado.

Na coloração de rotina, o túbulo normal mostra células regulares, com borda luminal bem definida e núcleos corados e íntegros. No túbulo em lesão reversível, as células estão edemaciadas, a borda luminal perdeu as microvilosidades e ficou irregular — mas os núcleos continuam todos lá. No túbulo em lesão irreversível, várias células já não têm núcleo: o núcleo foi destruído. Nessas células, restabelecer fluxo sanguíneo e oxigênio não adianta mais, e o epitélio será reposto pela proliferação de células tubulares novas.

Daí sai o critério prático de leitura da lâmina: no túbulo renal, a ausência de núcleo nas células marca a passagem para a lesão irreversível.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-17-histologia.png",
  largura: 92%,
  legenda: [Três túbulos renais na mesma coloração. Em A, o normal: células regulares, borda luminal nítida, núcleos íntegros em todas. Em B, a lesão reversível: células tumefeitas, luz irregular pela perda das microvilosidades, mas os núcleos permanecem presentes e corados. Em C, a lesão irreversível: várias células perderam o núcleo, e é essa ausência que fecha o diagnóstico de morte celular. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

O microscópio eletrônico conta a mesma história com outra resolução. A célula tubular normal exibe a franja densa de microvilosidades voltada para a luz do túbulo e a cromatina distribuída de forma difusa no núcleo. Na lesão reversível, as microvilosidades desapareceram, a membrana ainda está identificável e a cromatina começa a se condensar. Na lesão irreversível, quase não se reconhece mais a estrutura celular: há vesículas citoplasmáticas por toda parte, o núcleo está intensamente condensado e a própria membrana nuclear se desorganiza.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-19-microscopia-eletronica.png",
  largura: 72%,
  legenda: [Ultraestrutura do mesmo epitélio tubular. Em A, o normal, com as microvilosidades identificadas por mv projetando-se para a luz L e cromatina difusa. Em B, a lesão reversível: superfície lisa, microvilosidades perdidas, cromatina começando a condensar. Em C, a lesão irreversível: perda quase completa do desenho celular, vesículas citoplasmáticas e núcleo condensado. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

#subtopico("2.4 — Os dois critérios de irreversibilidade")

A pergunta que fica é o que exatamente define a passagem. A resposta é curta: os dois critérios que tornam a lesão irreversível são a destruição excessiva de DNA e proteínas e a perda de permeabilidade da membrana.

O raciocínio por trás de cada um é o mesmo. A membrana plasmática é o que separa o meio interno do externo; enquanto ela retém o conteúdo celular, retirar o agressor permite que a célula reconstrua o que perdeu. O DNA é o molde a partir do qual toda proteína é refeita; enquanto ele estiver íntegro, existe a possibilidade de refazer a maquinaria danificada. Destruídos um ou outro, a célula perde a barreira ou perde o molde — e não há como reconstruir.

Nos quadros reais os dois eventos costumam se cruzar, mas a ordem em que aparecem depende da causa. Na privação de oxigênio, a perda de permeabilidade da membrana vem primeiro. Nos grandes danos ao material genético, como doenças genéticas e grandes translocações, a destruição do DNA é que acontece antes.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-15-criterios.png",
  largura: 52%,
  legenda: [Os dois critérios como conjuntos que se intersectam. Nenhum deles é obrigatório sozinho, e na maioria das lesões reais os dois terminam presentes; a causa decide qual chega primeiro. Fonte: slide da aula.])

#confusao-prevista(
  titulo: "Perder função não é perder permeabilidade",
  aluno_acha: [aluno trata qualquer alteração de membrana já como irreversibilidade, porque a membrana aparece alterada desde cedo],
  mecanismo: [na lesão reversível a membrana já está alterada — ela faz blebs, perde microvilosidades, incha. O que ainda não aconteceu é a *perda de permeabilidade*, isto é, ela ainda retém o conteúdo da célula. O critério não é a membrana estar deformada, é ela ter deixado de segurar o que está dentro.],
)

#subtopico("2.5 — A enzima intracelular no sangue")

Esse critério de membrana tem uma tradução laboratorial usada todos os dias, e ela é a ponte entre a bioquímica da lesão e a prática clínica.

Diante de um paciente com dor torácica sugestiva de infarto, além de ofertar oxigênio, tratar a dor para reduzir a frequência cardíaca e melhorar a oxigenação do miocárdio, e realizar o eletrocardiograma, colhe-se sangue seriado — na chegada, uma hora depois, duas horas depois — para dosar marcadores. Historicamente usou-se a mioglobina; hoje a dosagem se apoia na creatina quinase fração MB e na troponina, ambas específicas do músculo cardíaco.

O raciocínio é o seguinte. Troponina e creatina quinase MB são proteínas que vivem *dentro* do cardiomiócito, participando do acoplamento entre actina e miosina que produz a contração. Elas não deveriam estar circulando. Se aparecem no sangue, é porque saíram de dentro da célula, e para sair precisaram atravessar uma barreira que deixou de reter: troponina e creatina quinase MB só chegam ao sangue depois que a célula perde a integridade da membrana plasmática. Encontrá-las na circulação é, portanto, uma leitura direta do critério de irreversibilidade.

#confusao-prevista(
  titulo: "Troponina elevada não indica isquemia, indica morte celular",
  aluno_acha: [aluno lê a troponina como um marcador de sofrimento isquêmico em geral, e por isso espera vê-la elevada também na angina],
  mecanismo: [a troponina não vaza porque a célula está com pouco oxigênio; ela vaza porque a membrana *rompeu*. Dor torácica com troponina normal é lesão reversível, ou seja, angina — restabelecida a oxigenação, o miocárdio volta ao normal. Troponina elevada já é do outro lado da linha.],
)

A mesma lógica vale fora do coração. O pâncreas exócrino produz lipase e a lança no ducto pancreático, de onde ela segue para o tubo digestivo; lipase não deveria estar no sangue. Quando uma pancreatite, seja inflamatória, seja isquêmica, leva as células exócrinas à lesão irreversível, elas liberam seu conteúdo, e passa a ser possível dosar amilase e lipase pancreáticas na circulação. O princípio geral é este: enzima intracelular encontrada na circulação sanguínea significa lesão celular irreversível.

#sintese-box(1)[Reversibilidade é uma leitura de barreira e de molde. A membrana que ainda retém o conteúdo e o DNA que ainda serve de matriz mantêm a célula recuperável; a troponina no sangue é a notícia de que a barreira caiu.]

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-21-marcadores.png",
  largura: 62%,
  legenda: [Curvas de elevação dos marcadores no sangue a partir do início dos sintomas, em múltiplos do valor de referência. A mioglobina sobe e cai cedo; a creatina quinase MB tem pico intermediário; a troponina I sobe e permanece elevada por dias. É por isso que a dosagem é seriada — o momento da coleta define o que se enxerga. Fonte: monografias.com, reproduzido no slide da aula.])


#parte-title("PARTE III — Os mecanismos que empurram a célula")

#subtopico("3.1 — Os quatro alvos da agressão")

Percorrido o quadro geral, resta abrir o motor. Uma agressão celular ataca quatro alvos, e é a soma dos danos nesses quatro pontos que constrói a irreversibilidade: a mitocôndria, os reservatórios de cálcio, as membranas e as proteínas, incluindo aqui também o material genético.

Vistos pelo lado do processo em vez do lado da estrutura, esses quatro alvos aparecem como quatro processos que se retroalimentam. Na prática, quatro processos combinados empurram a lesão até a irreversibilidade: queda de ATP, produção de radicais livres, influxo de cálcio e dano mitocondrial. Nenhum deles age sozinho, e nenhum deles é suficiente isoladamente — o que torna a lesão irreversível é a combinação.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-23-quatro-mecanismos.png",
  largura: 95%,
  legenda: [Os quatro alvos e o que cada um desencadeia. O dano mitocondrial reduz ATP e aumenta radicais livres; a entrada de cálcio aumenta a permeabilidade mitocondrial e ativa enzimas celulares; o dano de membrana esvazia a célula pela membrana plasmática e libera enzimas pela membrana lisossômica; o dano a proteínas e ao DNA ativa proteínas pró-apoptóticas. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

#subtopico("3.2 — A queda de ATP e a cascata isquêmica")

Tomando o infarto agudo do miocárdio como modelo, o primeiro dominó é a mitocôndria. Sem oxigênio suficiente chegando ao tecido, a cadeia respiratória não tem para quem entregar os elétrons ao final do percurso, e na isquemia a queda de ATP começa pela redução da fosforilação oxidativa mitocondrial. A produção de ATP despenca, e a célula desvia o que consegue para a via anaeróbica.

Dessa queda de ATP saem três ramos, e vale seguir cada um até o fim.

O primeiro ramo é a bomba de sódio e potássio, que consome ATP para manter sódio fora e potássio dentro da célula. Com menos ATP, ela desacelera: o sódio entra, e a água entra atrás dele por osmose; ao mesmo tempo, pela regulação cruzada entre os dois íons, o potássio sai; e o cálcio também começa a entrar. O influxo de sódio e água é o que produz a dilatação do retículo endoplasmático, o edema celular, o descolamento da membrana em blebs e a perda das microvilosidades. Toda a alteração ultraestrutural da lesão reversível decorre, no fundo, da falência da bomba de sódio por queda de ATP.

O segundo ramo é a glicólise anaeróbica, acionada para compensar a produção que faltou. Ela consome os estoques de glicogênio da célula e produz ácido lático, e a acidose que se instala tem também um componente metabólico sistêmico — o lactato é apenas uma parte dela. O efeito nuclear dessa acidose é sobre o núcleo: a acidose intracelular leva o núcleo a condensar a cromatina, uma reação de proteção do DNA num ambiente mais ácido.

O terceiro ramo é a síntese proteica. A escassez de energia sinaliza que a hora não é de produzir proteína, e os ribossomos se desprendem do retículo endoplasmático, reduzindo a síntese proteica. A prioridade passa a ser manter a célula viva.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-25-cascata-isquemia.png",
  largura: 58%,
  legenda: [A cascata inteira a partir da isquemia. Note que os três ramos saem do mesmo nó — a queda de ATP — e que cada um termina num achado morfológico já descrito na PARTE II: o edema e os blebs vêm da bomba de sódio, a condensação da cromatina vem da queda do pH, e a queda da síntese proteica vem do desligamento dos ribossomos. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

#sintese-box(2)[A falência energética não produz um dano; produz um leque de danos que convergem. Reconhecer o nó comum — a queda de ATP — é o que permite reconstruir a morfologia inteira da lesão reversível a partir de um único ponto de partida.]

#subtopico("3.3 — Radicais livres: produção, defesas e alvos")

A mitocôndria não falha apenas por falta de oxigênio. A fosforilação oxidativa depende de uma quantidade adequada de oxigênio nas cristas mitocondriais, e a fosforilação oxidativa produz excesso de radicais livres tanto quando falta oxigênio quanto quando ele está em excesso. Com pouco oxigênio, os elétrons não encontram aceptor no momento certo e escapam; com oxigênio demais, a aglomeração de moléculas também desorganiza a transferência. Nos dois extremos, sobra elétron desemparelhado, e o resultado é a formação de radicais livres.

Formar radical livre, aliás, é parte normal da respiração celular: a redução do oxigênio nunca é perfeita, e uma fração escapa como radical superóxido. O que impede que isso seja um problema é um sistema de defesa antioxidante que trabalha o tempo todo.

O sistema tem três peças principais. A superóxido dismutase converte o radical superóxido em peróxido de hidrogênio. Esse peróxido, se encontrar ferro na forma reduzida, entra numa reação que gera o radical hidroxila — a reação que usa Fe#super[2+] para converter peróxido de hidrogênio no radical hidroxila chama-se reação de Fenton, e o radical hidroxila é o mais agressivo dos três. Para impedir que a reação de Fenton aconteça, o peróxido precisa ser removido antes: a enzima que transforma o peróxido de hidrogênio em água e oxigênio é a catalase, e a glutationa peroxidase atua no mesmo sentido, degradando peróxido e radical hidroxila.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-27-radicais-livres.png",
  largura: 88%,
  legenda: [A cadeia de geração dentro da mitocôndria. O oxigênio sofre redução incompleta e vira superóxido; a superóxido dismutase o converte em peróxido de hidrogênio; a reação de Fenton, na presença de ferro, produz o radical hidroxila. À esquerda estão os disparadores externos que aumentam a produção: inflamação, radiação, agentes químicos e lesão de reperfusão. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

O sistema antioxidante é finito. Quando a produção de radicais dispara — por hipóxia, por inflamação, por radiação —, o consumo dessas enzimas e dos demais quelantes ultrapassa a capacidade de reposição, elas se tornam insuficientes e o radical livre começa a sobrar. É esse excedente que causa dano.

O dano acontece em três frentes, porque o radical livre reage com quase tudo. Sobre os lipídios, o radical livre ataca os fosfolipídios da membrana por peroxidação lipídica, desorganizando-a e alterando sua permeabilidade. Sobre as proteínas, provoca oxidação com perda da conformação alostérica e da atividade enzimática. Sobre o DNA, a oxidação favorece a quebra da molécula e dificulta o reparo, o que se acumula em mutações.

#subtopico("3.4 — A lesão de reperfusão")

Há um momento em que a própria terapêutica agrava a lesão, e entendê-lo depende de tudo o que foi dito sobre radicais livres.

Imagine uma célula ainda em lesão reversível: entrando sódio, saindo potássio, mitocôndria adaptada a trabalhar com pouco oxigênio, glicólise anaeróbica em curso, defesas antioxidantes já consumidas pelo período isquêmico. Nesse cenário, um cateterismo desobstrui o vaso e o oxigênio volta de uma vez. A mitocôndria que estava operando num regime de escassez recebe uma carga que não consegue processar ordenadamente, e a produção de radicais livres explode sobre um sistema antioxidante já esgotado. O resultado é um dano adicional, provocado pela reperfusão — e por isso chamado de lesão de reperfusão.

O experimento com rim transplantado torna isso visível. O órgão passa o transporte e a cirurgia praticamente sem oxigenação, e entra em lesão reversível. No momento em que o vaso é ligado e a reperfusão acontece, a função renal, em vez de subir, cai — de cem por cento para algo em torno de setenta por cento. Depois de reperfundir o rim transplantado, a função cai antes de voltar a subir porque o excesso de oxigênio gerou radicais livres, e esses radicais peroxidaram membranas, DNA e proteínas de células que estavam à beira do ponto de retorno sem tê-lo cruzado. Elas cruzam agora, e morrem.

Isso não é argumento contra reperfundir. A queda é transitória e a função volta a subir logo depois, porque reabrir o vaso é o único jeito de salvar as células que ainda estavam recuperáveis. O objetivo da reperfusão nunca é salvar todas as células, é salvar o máximo possível delas. Mas explica por que o tempo é decisivo em transplante e em revascularização: quanto mais longa a isquemia, maior a proporção de células no limiar e maior o custo do reencontro com o oxigênio. Reperfundir o miocárdio mais de 24 horas depois do infarto agudo traz benefício mínimo no quadro agudo, porque a essa altura o que havia para ser salvo já se perdeu.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-33-reperfusao.png",
  largura: 66%,
  legenda: [Função renal em porcentagem do basal ao longo do procedimento. Do basal à pré-isquemia a queda é pequena; a partir da reperfusão, aos 15 minutos, todas as curvas despencam, e aos 30 minutos já estão subindo de novo. A queda no momento exato em que o oxigênio retorna é a assinatura da lesão de reperfusão. Fonte: Flynn e Akers, Pharmacotherapy 2003;23(11), reproduzido no slide da aula.])

#subtopico("3.5 — Dano mitocondrial: duas saídas para duas mortes")

A mitocôndria não é apenas vítima da queda de ATP: uma vez lesada, ela decide qual será a forma de morte da célula. E ela faz isso por duas rotas distintas, que partem do mesmo evento inicial — o aumento da permeabilidade da membrana mitocondrial provocado por cálcio citosólico elevado, radicais livres e peroxidação lipídica.

A primeira rota é a permeabilidade de transição. A cadeia de fosforilação oxidativa depende de uma diferença de potencial mantida entre as membranas mitocondriais interna e externa. Quando essa diferença de potencial se perde, forma-se uma alça de retroalimentação: sem potencial, não há como formar ATP; sem ATP, a célula perde ainda mais controle; e o pouco oxigênio que chega, sem uma crista funcionante para transferir elétrons, gera mais radical livre ainda. A abertura da permeabilidade de transição mitocondrial dissipa o potencial de membrana, impede gerar ATP e leva a célula à necrose.

A segunda rota passa pelo conteúdo das cristas. Entre as proteínas alojadas nas cristas mitocondriais está o citocromo c, peça da cadeia respiratória. A mesma alteração de permeabilidade que dissipa o potencial libera das cristas o citocromo c, que ativa enzimas pró-apoptóticas no citoplasma — é a via intrínseca, ou mitocondrial, da apoptose.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-35-mitocondria.png",
  largura: 50%,
  legenda: [Um único evento inicial, duas saídas. À esquerda, a permeabilidade de transição dissipa o potencial de membrana, impede a geração de ATP e leva à necrose. À direita, a saída do citocromo c e de outras proteínas pró-apoptóticas leva à apoptose. Repare que o que separa os dois desfechos não é a intensidade da agressão, e sim qual consequência da permeabilidade predomina. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

#subtopico("3.6 — O cálcio como amplificador da lesão")

O cálcio é o elo que transforma uma falha energética em autodestruição organizada, e entender por que ele sobe é entender por que a lesão se acelera.

Em condições normais, o cálcio citoplasmático é mantido baixíssimo: ele fica estocado no retículo endoplasmático e na mitocôndria ou é bombeado para fora da célula, sempre por transporte ativo. Na célula lesada, o cálcio se acumula no citoplasma porque as bombas que o mantêm nos reservatórios dependem de ATP. Falta ATP, as bombas param, e o cálcio vaza dos estoques internos e entra do meio extracelular.

O problema é que o cálcio não é um íon qualquer: é um segundo mensageiro, um sinalizador que a célula usa para deflagrar respostas. Cálcio citoplasmático persistentemente alto é lido pela célula como sinal de lesão, e a resposta a esse sinal é ativar um conjunto de enzimas que desmontam a própria célula.

São quatro famílias, e cada uma faz um estrago específico. As fosfolipases quebram os fosfolipídios e danificam a membrana — a mesma membrana que já vinha sendo atacada pela peroxidação dos radicais livres. As proteases fazem o segundo estrago: o cálcio citosólico ativa proteases que rompem o citoesqueleto e desancoram a membrana plasmática, de modo que se perdem tanto proteínas da membrana quanto as proteínas que a prendiam ao esqueleto interno. As endonucleases quebram DNA e RNA. E as ATPases degradam o pouco ATP que ainda estava sendo produzido, fechando mais um círculo vicioso. Além disso, o cálcio que entra na mitocôndria aumenta a permeabilidade de transição, ligando este mecanismo diretamente ao anterior.

O resultado combinado é exatamente o par que define a irreversibilidade: dano de membrana e dano ao material genético. É por isso que o influxo de cálcio funciona como grande potencializador da lesão celular irreversível.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-37-calcio.png",
  largura: 50%,
  legenda: [O cálcio chega ao citoplasma por duas origens — do meio extracelular e dos reservatórios internos, mitocôndria e retículo endoplasmático liso. Uma vez elevado, ativa quatro famílias de enzimas cujos produtos finais estão nas caixas de baixo: dano de membrana, dano nuclear e queda adicional de ATP. À direita, o ramo que aumenta a permeabilidade de transição mitocondrial. Fonte: Robbins, Pathologic basis of disease, 9ª edição.])

#subtopico("3.7 — O dano de membrana como ponto de convergência")

Vale reunir num só lugar tudo o que chega à membrana, porque o dano de membrana não tem causa única: ele é a soma de quatro linhas que já foram percorridas separadamente.

A primeira é a peroxidação lipídica pelos radicais livres, que desorganiza os fosfolipídios da bicamada. A segunda é a queda da síntese de fosfolipídios, consequência direta da falta de ATP: a membrana é uma estrutura em renovação constante, e sem energia a reposição para. A terceira é a ativação das fosfolipases pelo cálcio citosólico, que degrada ativamente os fosfolipídios existentes. Somadas, as três produzem perda de fosfolipídio de membrana. A quarta linha é a ativação das proteases, também pelo cálcio, que destrói proteínas de membrana e o citoesqueleto que a sustenta.

É a convergência dessas quatro linhas que finalmente rompe a barreira e faz a célula perder a permeabilidade — o primeiro dos dois critérios de irreversibilidade. Do lado de fora, isso aparece como a troponina no sangue do paciente.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-39-venn-mecanismos.png",
  largura: 52%,
  legenda: [A síntese da PARTE III. Queda de ATP, radicais livres, dano mitocondrial e influxo de cálcio não são quatro histórias paralelas: eles se sobrepõem, cada um alimentando os outros três. É na interseção dos quatro que a lesão atravessa o ponto de retorno. Fonte: slide da aula.])

#subtopico("3.8 — Uma rota à parte: proteínas mal dobradas e dano direto ao DNA")

Falta um último grupo de lesões, e ele merece destaque justamente por não seguir o roteiro anterior. São as doenças de dobramento proteico e o dano direto ao material genético, que podem ser inatas ou adquiridas por infecção ou por distúrbio metabólico, e que não guardam relação mecanística com a cascata de ATP, radicais livres e cálcio.

O funcionamento normal é o seguinte. Uma proteína recém-sintetizada que assume uma conformação errada é encaminhada ao complexo das chaperonas, que a redobra na forma correta. Proteína mal dobrada é normalmente resgatada pelo complexo das chaperonas, e quando esse resgate falha a célula dispara sinalizações intracelulares de morte, fundamentalmente por apoptose. A proteína malformada é marcada para destruição, e o acúmulo desse material defeituoso gera dano celular relevante.

A doença de Creutzfeldt-Jakob, correlato humano da encefalopatia espongiforme bovina, é o exemplo clássico desse mecanismo: o processo de dobramento falha, a proteína anômala se acumula e a célula morre por essa via, sem que a isquemia ou o cálcio tenham qualquer papel.

#figura-nebli("/figuras/pato-01-lesao-celular-i/slide-43-chaperona.png",
  largura: 60%,
  legenda: [O ciclo normal da chaperona: a proteína em novelo desordenado entra no complexo, o gasto de ATP promove a redobragem e a proteína sai na conformação nativa. É a falha desse ciclo que caracteriza as doenças de dobramento proteico. Fonte: Robbins, Pathologic basis of disease, 9ª edição, e biorom.uma.es, reproduzidos no slide da aula.])

#conclusao-box[
  A aula inteira cabe numa única linha do tempo. A célula normal em homeostase recebe uma agressão; se ela for leve e prolongada, a célula se adapta; se for intensa ou rápida, a célula se lesa. A lesão começa reversível — perda de função, alterações bioquímicas, edema, blebs, perda de microvilosidades, mitocôndrias e retículo dilatados — e permanece reversível enquanto a membrana ainda retém o conteúdo celular e o DNA ainda serve de molde. Retirado o agressor nessa fase, a célula volta.

  O que rompe essa possibilidade são quatro processos que se alimentam mutuamente. A queda de ATP desliga a bomba de sódio, aciona a glicólise anaeróbica e desprende os ribossomos, gerando toda a morfologia da lesão reversível. Os radicais livres, produzidos em excesso tanto na falta quanto no excesso de oxigênio, esgotam as defesas antioxidantes e peroxidam lipídios, proteínas e DNA. O dano mitocondrial abre a permeabilidade de transição, que dissipa o potencial de membrana e conduz à necrose, e libera o citocromo c, que conduz à apoptose. E o influxo de cálcio, permitido pela própria falta de ATP, ativa fosfolipases, proteases, endonucleases e ATPases que desmontam membrana, citoesqueleto e material genético.

  Quando esses quatro processos somados produzem perda de permeabilidade da membrana e destruição excessiva de DNA e proteínas, a lesão é irreversível — e a partir daí a célula morre por necrose ou por apoptose. É essa mesma cadeia que sustenta a clínica: a troponina no sangue do paciente com dor torácica é a leitura direta de uma membrana que se rompeu, e a janela estreita para reperfundir existe porque cada minuto de isquemia empurra mais células para o outro lado da linha. Entender lesão celular é, no fundo, aprender a reconhecer de que lado dessa linha o tecido está — e quanto tempo ainda resta.
]
