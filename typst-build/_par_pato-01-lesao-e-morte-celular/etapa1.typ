#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Uma célula viva não é um objeto parado. Ela é um estado de equilíbrio mantido a custo de energia: bombas que empurram sódio para fora e potássio para dentro, canais que mantêm o cálcio guardado fora do citoplasma, enzimas que trabalham dentro de uma faixa estreita de pH, membranas que precisam ficar íntegras para separar o que está dentro do que está fora. Esse equilíbrio ativo, mantido segundo a segundo, é a *homeostase*. Retirar energia dessa célula, ou atacar diretamente qualquer uma dessas estruturas, é retirar o chão em que ela se sustenta.

  Esta apostila percorre o que acontece quando esse chão é retirado. Na *PARTE I* montamos o mapa geral: a célula agredida tem um número pequeno de saídas — adaptar-se, sofrer uma lesão que ainda pode ser desfeita, ou atravessar um ponto sem retorno e morrer. Veremos também em que ordem o dano aparece, o que o microscópio consegue mostrar em cada fase e quais são os dois critérios que definem a irreversibilidade. Na *PARTE II* descemos ao nível bioquímico: queda de ATP, radicais livres, dano mitocondrial e entrada de cálcio no citoplasma são os quatro mecanismos que, combinados, empurram a célula para além do ponto de retorno. Na *PARTE III* e na *PARTE IV* olhamos os dois desfechos dessa travessia — a *necrose*, que é destruição desordenada com inflamação em volta, e a *apoptose*, que é um programa de autodemolição limpo e silencioso.

  O fio que costura tudo é uma frase só: *lesão celular é, no fundo, um problema de energia e de membranas*. Quando falta energia, as bombas param; quando as bombas param, os gradientes se desfazem; quando os gradientes se desfazem, entram água e cálcio; e o cálcio dentro do citoplasma liga as enzimas que terminam de destruir a própria célula. Entender essa cadeia é entender por que uma dor no peito de vinte minutos pode ser reversível e a de seis horas não é, por que uma enzima cardíaca dosada no sangue significa morte celular, e por que reabrir um vaso entupido precisa ser feito depressa.
]

#parte-title("PARTE I — Da homeostase à morte: o mapa da resposta celular", primeira: true)

#subtopico("1.1 — Homeostase, estresse e as três saídas possíveis")

O ponto de partida é a célula normal, em homeostase, gastando energia para manter suas concentrações internas diferentes das do meio externo. Em algum momento chega um estímulo que a tira desse ponto de equilíbrio. O que acontece depois depende de duas variáveis, e só de duas: a *intensidade* do estímulo e a *duração* dele.

Quando o estímulo é leve e prolongado, a célula tem tempo de fazer alguma coisa a respeito. Ela muda a expressão de proteínas, fabrica mais componentes de que precisa, reorganiza sua estrutura e atinge um novo ponto de equilíbrio, diferente do anterior mas estável. Esse processo se chama *adaptação celular*. O exemplo mais direto vem da hipertensão arterial: quando a resistência dos vasos periféricos aumenta, o coração precisa gerar mais pressão a cada batimento. Para dar conta, os cardiomiócitos aumentam o número de filamentos contráteis dentro de si, ficam maiores, e a parede do miocárdio engrossa — é a *hipertrofia cardíaca*. A adaptação também pode ir na direção contrária, com perda de conteúdo celular: um paciente com lesão medular que fica restrito ao leito perde massa muscular esquelética por *atrofia*; na doença de Alzheimer há perda progressiva de sinapses e de neurônios, com atrofia cortical. Adaptar não significa melhorar, significa alcançar um novo equilíbrio possível dentro das novas condições.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-02-organograma-resposta-celular.png",
  largura: 62%,
  legenda: [Todo o percurso desta apostila em um só desenho. Da célula normal saem dois caminhos: o estresse leve e prolongado leva à adaptação; o estímulo lesivo leva à lesão celular. Quando é brando e transitório, a seta volta para a célula normal — lesão reversível. Quando é grave e progressivo, a seta desce para a lesão irreversível, que desemboca em necrose ou apoptose. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

Quando o estímulo é intenso, ou cresce depressa demais, falta exatamente aquilo de que a adaptação depende: tempo. Modificar a expressão de proteínas leva horas; um vaso que entope leva segundos. Sem tempo para se adaptar, a célula entra em *lesão celular*. Se essa lesão for moderada e transitória, ela ainda é *reversível*: removido o agressor, a célula desfaz as alterações e volta ao estado normal. O exemplo clássico é o de alguém destreinado que faz um esforço intenso, aumenta a demanda do miocárdio além do que o fluxo coronariano consegue suprir e sente dor no peito. Se essa pessoa para, o fluxo se restabelece, a oferta volta a cobrir a demanda e as células cardíacas retomam a função normal. Nada se perdeu.

Se, ao contrário, o estímulo é intenso e progressivo — vai piorando ao longo do tempo em vez de ceder —, a célula atravessa um ponto sem retorno. A partir dali, mesmo devolvendo oxigênio e nutrientes, ela não volta mais. É a *lesão irreversível*, que termina em morte celular por *necrose* ou por *apoptose*. O infarto agudo do miocárdio é a versão irreversível do exemplo anterior. E vale registrar desde já que a irreversibilidade não é privilégio da falta de oxigênio: um vírus que invade um hepatócito, se multiplica dentro dele e o destrói produz lesão irreversível pela via da infecção, como acontece na hepatite aguda.

#confusao-prevista(
  titulo: "Adaptação não é uma etapa antes da lesão",
  aluno_acha: [muitos leem o esquema como uma escada — primeiro a célula se adapta, depois, se o estímulo continuar, ela se lesa.],
  mecanismo: [adaptação e lesão são *caminhos alternativos*, escolhidos pelo perfil do estímulo. Estímulo leve e prolongado dá tempo à adaptação; estímulo intenso ou rápido não dá, e a célula vai direto para a lesão sem passar pela adaptação. A seta pontilhada que liga adaptação a lesão no esquema tem um rótulo específico: incapacidade de adaptar. Ou seja, a célula só cai da adaptação para a lesão quando a adaptação falha, não como passo natural seguinte.],
)

#subtopico("1.2 — As causas que tiram a célula do equilíbrio")

Antes de descer aos mecanismos, vale ter em mente de onde vêm os estímulos agressores. A lista é curta e cada item age por um caminho diferente.

A *privação de oxigênio* é a causa mais prevalente de todas, e por isso é ela que estrutura a explicação mecanística da PARTE II. Ela pode vir de fluxo sanguíneo insuficiente, do aumento da demanda acima da oferta ou de um problema na oxigenação do sangue.

Os *agentes físicos* incluem temperatura, trauma e radiação. Uma exposição solar prolongada ilustra bem os três desfechos possíveis num único tecido: a radiação ultravioleta gera dano às células epiteliais de revestimento, e conforme a dose esse dano produz adaptação, lesão reversível ou destruição direta das células, com inflamação e o quadro clínico da queimadura solar.

Os *agentes químicos e drogas* agem por dano molecular direto. A fumaça do cigarro, por exemplo, pode induzir adaptação com modificação do epitélio respiratório ou levar à lesão irreversível das células de revestimento.

Os *agentes infecciosos* podem destruir a célula diretamente, ao se multiplicarem dentro dela, como na hepatite aguda. As *reações imunológicas* — alergias e doenças autoimunes — causam dano quando a própria resposta imune do organismo agride tecidos. Há ainda uma situação intermediária importante: em infecções intracelulares, como a tuberculose e várias viroses, o microrganismo se esconde dentro da célula, e a única forma de o sistema imune alcançá-lo é destruir a célula infectada. O dano, nesse caso, é feito pela defesa, não pelo agressor.

Fecham a lista os *desarranjos genéticos*, em que translocações e grandes modificações do material genético comprometem a função celular, e o *desbalanço nutricional*, em que faltam à célula os substratos das reações bioquímicas de que ela depende.

#subtopico("1.3 — A ordem em que o dano aparece")

Há um ponto que costuma passar despercebido e que organiza toda a prática diagnóstica: as alterações não aparecem todas ao mesmo tempo. Elas obedecem a uma ordem fixa, e essa ordem é a razão de existirem exames de sangue precoces em cardiologia.

O primeiro efeito da agressão é a *perda de função*. A célula ainda está estruturalmente inteira, mas já não faz direito o que deveria fazer. Logo em seguida aparecem as *alterações bioquímicas*, detectáveis por dosagens. Depois vêm as *alterações ultraestruturais*, aquelas que só o microscópio eletrônico enxerga, porque acontecem em membranas e organelas. Só mais tarde surgem as *alterações no microscópio de luz*, que é o microscópio comum de lâmina corada. E por último aparecem as *alterações macroscópicas*, visíveis a olho nu na peça cirúrgica ou na autópsia.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-06-curva-efeito-duracao.jpg",
  largura: 66%,
  legenda: [O eixo horizontal é a duração da lesão e o vertical, a magnitude do efeito. A curva vermelha, a primeira a se mover, é a queda da função celular. Só depois sobem, em fila, as alterações bioquímicas, as ultraestruturais, as de microscopia de luz e as macroscópicas. A linha tracejada marca a passagem de reversível para irreversível — e repare que ela cai antes de qualquer alteração visível ao microscópio de luz. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

A consequência prática é dura: quando a lesão finalmente se torna visível ao microscópio de luz ou a olho nu, ela já é irreversível há um bom tempo. Uma isquemia miocárdica só aparece macroscopicamente depois que as células morreram. É por isso que a medicina investe tanto em ferramentas de diagnóstico precoce: identificar a isquemia enquanto a lesão ainda é reversível e restabelecer o fluxo de oxigênio devolve a célula ao normal; identificá-la depois do infarto instalado apenas evita que mais células morram, sem recuperar as que já se perderam.

A posição da linha tracejada que separa reversível de irreversível não é fixa para todo tecido. Ela depende da resistência do tipo celular. Células mais resistentes toleram períodos maiores de agressão antes de cruzar o limite, e sua linha fica deslocada para a direita. O neurônio, ao contrário, é extremamente sensível: sua janela de lesão reversível é curtíssima, e a linha fica muito próxima do eixo zero. Esse detalhe explica por que minutos de parada circulatória custam neurônios enquanto o mesmo intervalo poupa fibroblastos.

#mini-resumo[Função cai primeiro, bioquímica em seguida, ultraestrutura depois, microscopia de luz e macroscopia por último. Quem espera a alteração ficar visível está sempre chegando atrasado, e o quanto se pode esperar varia com a resistência do tipo celular.]

#subtopico("1.4 — O que se vê na lesão reversível")

Na fase reversível, o microscópio de luz oferece muito pouco. Fundamentalmente aparecem dois achados, e ambos são inespecíficos: o *edema celular*, ou seja, a célula inchada de água, e a *alteração gordurosa*, também chamada *esteatose*, que é o acúmulo de lipídio no citoplasma.

O que de fato caracteriza essa fase são as alterações ultraestruturais, e todas elas decorrem do mesmo problema de base — a queda da produção de energia, com as consequentes alterações de pH e do equilíbrio hidroeletrolítico. Na membrana plasmática, o citoesqueleto perde a ancoragem que mantinha a membrana esticada e presa; sem essa ancoragem, a membrana se solta em bolhas, chamadas #termo-nota[blebs][bolhas na superfície da célula formadas quando a membrana plasmática perde o acoplamento com o citoesqueleto que a mantinha tensionada]. Células que possuem microvilosidades, como as do epitélio intestinal e as do túbulo renal, perdem essas projeções, e a superfície antes regular fica irregular. Nas mitocôndrias aparecem edema e corpos amorfos. O retículo endoplasmático se dilata e os ribossomos que estavam grudados nele se desligam. No núcleo, a cromatina se condensa e elementos fibrilares e granulares se desagregam.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-09-tubulo-renal-microscopia-luz.jpg",
  largura: 94%,
  legenda: [Três túbulos renais na microscopia de luz. Em *A*, o túbulo normal: borda luminal regular e núcleos bem definidos em todas as células. Em *B*, lesão reversível: as células estão infladas, a superfície voltada para a luz perdeu a regularidade das microvilosidades, mas todos os núcleos continuam presentes e corados. Em *C*, lesão irreversível: várias células já não têm núcleo — a marca de que a célula morreu e não voltará, mesmo que o fluxo seja restabelecido. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

O contraste entre o painel B e o painel C dessa imagem resume a diferença entre as duas fases de um jeito que a prosa sozinha não alcança: na lesão reversível a célula está deformada mas viva, com núcleo; na irreversível o núcleo desapareceu. Quando isso acontece no túbulo renal, o organismo não recupera aquelas células — ele prolifera células tubulares novas para ocupar o espaço que ficou.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-10-tubulo-renal-microscopia-eletronica.jpg",
  largura: 70%,
  legenda: [As mesmas três situações na microscopia eletrônica, onde a fase reversível realmente se revela. Em *A*, a célula normal exibe microvilosidades densas projetadas para a luz do túbulo (_mv_ e _L_). Em *B*, na lesão reversível, as microvilosidades sumiram, a membrana ainda está lá e a cromatina começa a se condensar dentro do núcleo. Em *C*, na lesão irreversível, restam vesículas citoplasmáticas e um núcleo densamente condensado, com a arquitetura celular já desmanchada. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

#subtopico("1.5 — Os dois critérios de irreversibilidade")

Toda a discussão anterior converge para um critério objetivo do que define a passagem pelo ponto de retorno. São dois critérios, e apenas dois.

O primeiro é a *perda de permeabilidade seletiva da membrana*. A membrana plasmática é o que separa o meio interno do externo e permite que a célula mantenha concentrações diferentes dos dois lados. Enquanto ela ainda controla o que entra e o que sai, a retirada do agressor permite que os gradientes sejam refeitos e a célula volte ao normal. Quando ela perde essa seletividade e passa a deixar passar livremente moléculas nos dois sentidos, não há mais como restabelecer nada: o interior da célula e o meio externo se igualam.

O segundo é a *destruição excessiva do DNA e das proteínas*. O DNA é o molde a partir do qual tudo é refeito, e as proteínas são a maquinaria que executa. Enquanto o material genético estiver preservado, a célula ainda pode ressintetizar o que perdeu. Destruído o molde, não há reconstrução possível.

Na maior parte das situações os dois critérios acabam se encontrando, e é essa intersecção que consolida a irreversibilidade. Mas a ordem varia com a causa. Na privação de oxigênio, a perda de permeabilidade de membrana acontece primeiro, porque é a falência energética que derruba as bombas e desestabiliza a bicamada. Já nos grandes danos ao material genético — doenças genéticas com grandes translocações, radiação ionizante intensa —, a destruição do DNA vem antes, e a membrana pode até estar íntegra quando a célula já está condenada.

#atencao-box("A irreversibilidade é definida pela membrana e pelo DNA, não pela morfologia",
  [O aluno tende a decidir se a lesão é irreversível olhando a foto: célula inchada é reversível, célula feia é irreversível. Isso inverte a ordem causal e falha na clínica. A morfologia é *consequência tardia*, e vimos na curva da seção 1.3 que ela chega depois. Os critérios são funcionais e estruturais: perda de permeabilidade seletiva da membrana e destruição excessiva de DNA e proteínas. É por isso que existe um exame de sangue capaz de diagnosticar morte celular horas antes de qualquer alteração aparecer na lâmina — e é exatamente isso que a próxima seção explora.])

#subtopico("1.6 — Enzima intracelular no sangue: a leitura clínica da irreversibilidade")

O critério da membrana tem uma consequência clínica que vale a pena percorrer devagar, porque ela transforma um conceito de patologia num exame que se pede todos os dias no pronto-socorro.

Considere um paciente que chega com dor em aperto no peito e formigamento na mão e na mandíbula. Além das medidas imediatas — oferecer oxigênio, tratar a dor para reduzir o estresse e a frequência cardíaca e, com isso, melhorar a oxigenação do miocárdio —, colhe-se um eletrocardiograma e uma amostra de sangue. Nessa amostra dosam-se marcadores de lesão do músculo cardíaco: a *mioglobina*, hoje menos usada, a #sigla("CK-MB", [creatinaquinase fração MB — isoforma da creatinaquinase concentrada no músculo cardíaco, que participa da transferência de fosfato de alta energia dentro da célula]) e a *troponina* cardíaca. E o exame não é colhido uma vez só: repete-se na chegada, uma hora depois, duas horas depois, para acompanhar a curva.

O raciocínio por trás disso é inteiramente mecanístico. Troponina e CK-MB são moléculas *intracelulares*: elas moram dentro do cardiomiócito e participam do aparelho contrátil, ajudando no acoplamento entre actina e miosina. Elas não têm função nenhuma no plasma, e em condições normais não estão lá. Se essas moléculas passam a ser detectadas no sangue, elas necessariamente atravessaram a membrana plasmática de dentro para fora. Para atravessar, a membrana precisa ter perdido a permeabilidade seletiva. E perda de permeabilidade de membrana é, pela definição da seção anterior, o critério de irreversibilidade. Portanto: *enzima intracelular na circulação significa lesão celular irreversível*, isto é, morte celular.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-11-marcadores-cardiacos.png",
  largura: 64%,
  legenda: [Cinética dos marcadores após o início dos sintomas, em múltiplos do valor de referência. A mioglobina sobe primeiro e cai rápido, o que a torna precoce mas pouco específica. A CK-MB tem um pico intermediário. A troponina I sobe um pouco mais tarde, alcança o pico mais alto e permanece elevada por dias — daí a lógica de colher amostras seriadas em vez de uma só. Fonte: reproduzido nos slides da aula a partir de material de acesso público sobre troponina.])

O contraste entre dois pacientes com a mesma queixa fecha o raciocínio. O paciente com dor no peito e troponina normal tem *angina*: houve isquemia, houve perda de função, houve lesão — mas reversível. Restabelecida a oxigenação, ele recupera a função e nenhuma célula morre. O paciente com dor no peito e troponina e CK-MB elevadas já teve lesão irreversível, ou seja, infarto: parte do músculo morreu.

#clinica-box("O mesmo princípio fora do coração", [A lógica vale para qualquer órgão cuja célula guarde uma enzima característica. O pâncreas exócrino produz lipase e amilase e as despeja no ducto pancreático, de onde seguem para o tubo digestivo — elas não deveriam circular no sangue. Numa pancreatite, seja por inflamação ou por falta de oxigenação, as células acinares sofrem lesão irreversível, rompem-se e liberam essas enzimas em todas as direções. Dosar amilase e lipase pancreáticas elevadas na circulação é, portanto, a mesma leitura feita no coração com a troponina: houve lesão celular irreversível, houve necrose no pâncreas. A base de boa parte dos exames laboratoriais de lesão de órgão é exatamente este raciocínio de patologia celular.])

#sintese-box(1)[A célula agredida tem três destinos, escolhidos pela intensidade e pela duração do estímulo: adaptação, lesão reversível ou lesão irreversível com morte. O dano aparece numa ordem fixa — função, bioquímica, ultraestrutura, microscopia de luz, macroscopia —, de modo que a lâmina sempre chega atrasada. A irreversibilidade é definida por perda de permeabilidade da membrana e destruição de DNA e proteínas, e é a primeira dessas duas que permite dosar no sangue uma enzima que só deveria estar dentro da célula.]

#parte-title("PARTE II — Os mecanismos bioquímicos da lesão")

#subtopico("2.1 — Quatro alvos, um mesmo desfecho")

A PARTE I estabeleceu *quando* a célula morre. Esta parte explica *como*. Por trás de causas muito diferentes há um conjunto pequeno de mecanismos que se repetem, e vale conhecê-los como um mapa antes de percorrer cada um.

O primeiro é o *dano mitocondrial*. A mitocôndria é onde a fosforilação oxidativa transforma oxigênio e substratos em ATP; danificada, ela produz menos energia e, ao mesmo tempo, mais espécies reativas de oxigênio. Da queda de ATP derivam efeitos em cascata por toda a célula; das espécies reativas derivam danos a lipídios, proteínas e DNA.

O segundo é a *entrada de cálcio* no citoplasma. O cálcio funciona como sinalizador, e quando se acumula ativa um conjunto de enzimas que degradam a própria célula, além de piorar a permeabilidade mitocondrial.

O terceiro é o *dano de membrana*, que tem duas faces: na membrana plasmática, a célula perde seus componentes internos para o meio externo; nas membranas dos lisossomos, as enzimas digestivas guardadas dentro deles escapam e digerem a célula por dentro.

O quarto reúne o *dobramento anômalo de proteínas e o dano ao DNA*, que ativam proteínas pró-apoptóticas e levam a célula a se autodestruir de forma programada.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-12-panorama-mecanismos.png",
  largura: 98%,
  legenda: [Os quatro mecanismos lado a lado, cada um com seus efeitos imediatos. Vale voltar a esta figura ao fim da PARTE II: os quatro blocos não são independentes, e o restante desta parte mostra como cada um alimenta os outros. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

#subtopico("2.2 — Queda de ATP: a cascata da isquemia")

Tomemos a isquemia miocárdica como fio condutor, porque nela a cadeia inteira aparece com clareza. Isquemia significa fluxo sanguíneo insuficiente, e a primeira coisa que falta é oxigênio.

Sem oxigênio suficiente, a fosforilação oxidativa na mitocôndria diminui, e com ela cai a produção de #sigla("ATP", [adenosina trifosfato — a molécula que armazena e entrega energia para praticamente todo trabalho celular, inclusive o das bombas de membrana]). A partir daqui a cadeia se abre em três ramos.

O ramo mais importante começa na *bomba de sódio e potássio*, que é uma proteína de membrana que consome ATP para manter sódio fora da célula e potássio dentro. Sem ATP, essa bomba desacelera. O sódio, que era mantido do lado de fora contra o seu gradiente, passa a entrar na célula; o potássio sai, porque as duas correntes são reguladas de forma acoplada; e cálcio também entra. O ponto decisivo é que o sódio traz água consigo, por osmose. O resultado é o *edema*: o retículo endoplasmático incha, a célula inteira incha, a membrana perde estrutura e forma as bolhas descritas na seção 1.4, e as microvilosidades desaparecem. Toda aquela lista de alterações ultraestruturais da lesão reversível se resume, portanto, a uma frase — é a bomba de sódio funcionando mal por falta de ATP.

O segundo ramo é a *glicólise anaeróbica*. Privada da via que depende de oxigênio, a célula tenta compensar produzindo ATP sem ele. Isso consome os estoques de glicogênio e aumenta a produção de ácido lático, que contribui para a queda do pH intracelular — embora, vale a ressalva, o ácido lático seja apenas um dos componentes dessa acidificação, e não o maior deles, já que há também um efeito metabólico sistêmico. O pH mais baixo faz a cromatina se condensar dentro do núcleo, o que é uma reação de proteção do DNA a um ambiente mais ácido.

O terceiro ramo é o *desligamento dos ribossomos* do retículo endoplasmático, com queda da síntese proteica. A lógica é de economia: com pouca energia disponível, a prioridade é manter as funções vitais em vez de fabricar proteínas novas.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-13-cascata-isquemia-atp.png",
  largura: 60%,
  legenda: [A cascata completa a partir da isquemia. Repare que os três ramos que saem da queda de ATP terminam em achados que já conhecemos da PARTE I: edema e blebs à esquerda, condensação da cromatina no centro, queda da síntese proteica à direita. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

#mini-resumo[Menos oxigênio, menos fosforilação oxidativa, menos ATP. Sem ATP a bomba de sódio para, o sódio entra puxando água e a célula incha; a glicólise anaeróbica gasta glicogênio e acidifica o meio, condensando a cromatina; e os ribossomos se soltam, derrubando a síntese proteica.]

#subtopico("2.3 — Radicais livres: produção, defesa e alvos")

A mitocôndria não falha apenas por falta de oxigênio. Ela falha também quando há oxigênio *demais*, e entender esse ponto é o que permite compreender a lesão de reperfusão da próxima seção.

A fosforilação oxidativa acontece nas cristas mitocondriais e depende de uma quantidade adequada de oxigênio para receber os elétrons ao fim da cadeia transportadora. Com oxigênio de menos, faltam receptores para os elétrons e a transferência fica irregular. Com oxigênio em excesso, há moléculas demais concentradas nas cristas e a transferência também perde eficiência. Nos dois extremos o oxigênio acaba sendo reduzido de forma incompleta, e é essa redução incompleta que gera um *radical livre*: uma molécula com um elétron desemparelhado, quimicamente instável, que reage com quase tudo à sua volta para se estabilizar.

O primeiro radical formado é o *superóxido*. A partir dele a célula monta uma linha de conversão: a enzima *superóxido dismutase* transforma o superóxido em peróxido de hidrogênio, a conhecida água oxigenada. O peróxido de hidrogênio ainda é perigoso, porque na presença de ferro ele participa da *reação de Fenton* e origina o *radical hidroxila*, o mais reativo do grupo.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-14-geracao-radicais-livres.jpg",
  largura: 82%,
  legenda: [A linha de produção das espécies reativas de oxigênio dentro da mitocôndria. A redução incompleta do oxigênio gera superóxido; a superóxido dismutase o converte em peróxido de hidrogênio; e a reação de Fenton, na presença de ferro, transforma o peróxido em radical hidroxila. Cada seta é ao mesmo tempo um passo de defesa e um passo de risco, conforme o sistema esteja ou não conseguindo acompanhar. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

Formar radical livre faz parte da respiração celular normal — o processo nunca é perfeito. O que impede que isso seja um problema é a existência de *mecanismos antioxidantes* que removem esses radicais continuamente. A *catalase*, presente nos peroxissomos, decompõe o peróxido de hidrogênio em água e oxigênio, anulando o excesso antes que ele siga adiante. A *glutationa peroxidase* também neutraliza radicais. Junto com a superóxido dismutase, elas formam um sistema de remoção que dá conta da produção basal.

O desequilíbrio aparece quando a produção sobe além da capacidade de remoção. Isso acontece na oxigenação inadequada, na inflamação, na exposição à radiação e na reperfusão. Nessas condições os antioxidantes são consumidos em excesso, tornam-se insuficientes e o radical livre começa a sobrar. E radical livre que sobra reage com três classes de alvo, cada uma com uma consequência própria. Ao reagir com *lipídios*, especialmente os fosfolipídios da membrana, ele desorganiza a bicamada por *peroxidação lipídica* e altera a permeabilidade — que é, lembrando a seção 1.5, um dos dois critérios de irreversibilidade. Ao reagir com *proteínas*, ele as oxida, o que faz perder a conformação alostérica e a atividade enzimática. Ao reagir com o *DNA*, favorece a quebra da molécula e dificulta o reparo, o que acumula mutações.

#subtopico("2.4 — Lesão de reperfusão")

Chegamos ao ponto em que a seção anterior se paga. Imagine um paciente em lesão ainda reversível: entrando sódio, saindo potássio, célula inchada, mitocôndria adaptada a trabalhar com pouco oxigênio. Faz-se um cateterismo e o vaso obstruído é reaberto. De repente, uma grande quantidade de oxigênio chega a mitocôndrias que estavam justamente ajustadas ao contrário.

O resultado é uma explosão de produção de radicais livres, exatamente pelo mecanismo do excesso de oxigênio descrito na seção 2.3, num momento em que as defesas antioxidantes já estavam consumidas. Esse excesso peroxida membranas, oxida proteínas e lesa o DNA, e as células que estavam à beira do limite — ainda vivas, mas cambaleando — atravessam o ponto sem retorno e morrem. Esse dano adicional, causado pela própria restauração do fluxo, chama-se *lesão de reperfusão*.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-15-funcao-apos-reperfusao.png",
  largura: 76%,
  legenda: [Função do órgão em porcentagem do basal, medida antes da isquemia e após a reperfusão. Depois de reperfundido, o órgão não volta a 100 por cento: a função cai e só depois começa a subir de novo. A queda visível no gráfico é a lesão de reperfusão. Fonte: Flynn e Akers, _Pharmacotherapy_ 2003, reproduzido nos slides da aula.])

O transplante renal ilustra o fenômeno com clareza. Retirado do doador, o rim atravessa o transporte e a cirurgia praticamente sem oxigenação, acumulando lesão reversível. No momento em que o vaso é ligado no receptor e a reperfusão acontece, a função do enxerto *cai*, em vez de subir imediatamente, e só depois inicia a recuperação.

Isso não é um argumento contra reperfundir. Ao reabrir o vaso não se está tentando salvar todas as células, e sim o máximo possível delas: algumas morrem por causa do próprio retorno do oxigênio, mas as vizinhas, que estavam em grau menos avançado de lesão, recuperam a função normal — o que jamais aconteceria se o fluxo não fosse restabelecido. O que o fenômeno exige é *velocidade*. Quanto mais tempo o tecido passa isquêmico, maior a proporção de células no limiar e maior o estrago da reperfusão. Por isso transplantes e revascularizações têm janelas curtas, e por isso a reperfusão do miocárdio realizada mais de vinte e quatro horas depois de um infarto agudo traz benefício mínimo no quadro agudo.

#confusao-prevista(
  titulo: "Lesão de reperfusão não significa que reperfundir faz mal",
  aluno_acha: [ao ver a função cair depois da revascularização, o aluno conclui que restabelecer o fluxo piora o paciente.],
  mecanismo: [a queda é *localizada num subgrupo de células* que já estava no limiar da irreversibilidade e foi empurrada além dele pelo surto de radicais livres. O saldo continua amplamente favorável, porque todas as demais células só sobrevivem porque o oxigênio voltou. O que a lesão de reperfusão realmente ensina é sobre *tempo*: quanto mais curta a isquemia, menor a fração de células no limiar e menor o custo da reperfusão.],
)

#subtopico("2.5 — A mitocôndria decide entre necrose e apoptose")

Além de produzir menos ATP e mais radicais livres, a mitocôndria lesada faz duas coisas que determinam, literalmente, qual será o tipo de morte da célula.

A primeira é a abertura da *transição de permeabilidade mitocondrial*. Entre a membrana mitocondrial interna e a externa existe uma diferença de potencial elétrico, construída pelo bombeamento de prótons e absolutamente necessária para que a cadeia de fosforilação oxidativa consiga sintetizar ATP. Quando um poro de alta condutância se abre na membrana interna, os prótons vazam e essa diferença de potencial se dissipa. Sem potencial de membrana não há síntese de ATP, e sem ATP a lesão piora — inclusive porque a cadeia, funcionando mal, transfere elétrons de forma ainda mais irregular e produz mais radicais livres. Instala-se uma alça de retroalimentação positiva, em que a falta de energia gera mais falta de energia. Esse é o caminho da *necrose*.

A segunda é a *liberação do citocromo c*. O citocromo c é uma proteína que normalmente fica confinada no espaço entre as membranas mitocondriais e participa da cadeia transportadora de elétrons. Quando a permeabilidade da membrana mitocondrial se altera, ele escapa para o citoplasma. No citoplasma o citocromo c não transporta elétrons: ele se torna o gatilho de um conjunto de enzimas pró-apoptóticas. Esse é o caminho da *apoptose*, e é exatamente a via intrínseca ou mitocondrial que a PARTE IV vai detalhar.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-16-mitocondria-necrose-apoptose.jpg",
  largura: 47%,
  legenda: [Uma mesma mitocôndria lesada, dois desfechos. À esquerda, a transição de permeabilidade deixa os prótons escaparem, o potencial de membrana se perde, o ATP não é gerado e a célula caminha para a necrose. À direita, o citocromo c e outras proteínas pró-apoptóticas vazam para o citoplasma e disparam a apoptose. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

#subtopico("2.6 — Cálcio citosólico: o amplificador")

O cálcio merece uma seção própria porque é ele que transforma um problema energético num programa de autodestruição.

Em repouso, a concentração de cálcio livre no citoplasma é mantida extraordinariamente baixa. Isso é feito de forma ativa: bombas que consomem ATP empurram o cálcio para fora da célula e para dentro de dois reservatórios internos, o retículo endoplasmático e a própria mitocôndria. Manter o cálcio guardado, portanto, custa energia — e é isso que liga esta seção à anterior. Quando a produção de ATP cai, as bombas não dão mais conta, e o cálcio se acumula no citoplasma, vindo tanto do meio extracelular quanto dos reservatórios internos.

O acúmulo importa porque o cálcio citosólico é um *segundo mensageiro*: uma molécula cuja concentração a célula usa como sinal para disparar respostas. Cálcio alto e sustentado é interpretado como sinal de lesão, e a resposta a esse sinal é a ativação de um conjunto de enzimas.

As *fosfolipases* quebram os fosfolipídios da membrana — a mesma membrana que já está perdendo lipídios pela peroxidação dos radicais livres. As *proteases* clivam proteínas do citoesqueleto e da membrana; com isso a célula perde não só componentes da membrana como também as proteínas que a ancoram no citoesqueleto, o que agrava o dano estrutural. As *endonucleases* quebram DNA e RNA. E as *ATPases* degradam o pouco ATP que ainda restava, fechando o círculo vicioso.

Em paralelo, o cálcio que entra na mitocôndria aumenta a transição de permeabilidade descrita na seção anterior, reduzindo ainda mais a geração de ATP.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-17-calcio-citosolico.jpg",
  largura: 52%,
  legenda: [O cálcio chega ao citoplasma por três frentes — do meio extracelular, da mitocôndria e do retículo endoplasmático liso — e a partir do aumento da concentração citosólica ativa quatro classes de enzima. Siga as setas até a base da figura: elas convergem para dano de membrana, dano nuclear e queda adicional de ATP, que são precisamente os dois critérios de irreversibilidade mais o agravamento energético. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

Note o que aconteceu: as enzimas ativadas pelo cálcio atacam exatamente os dois alvos que definem a irreversibilidade. Fosfolipases e proteases produzem dano de membrana; endonucleases produzem dano ao material genético. O cálcio, portanto, não é mais um mecanismo entre outros — é o grande potencializador que converte lesão em irreversibilidade.

#subtopico("2.7 — Dano de membrana: onde tudo converge")

Vale reunir num só lugar tudo o que ataca a membrana, porque essa convergência é o coração da PARTE II. O dano de membrana nunca vem de uma causa única; ele é a soma de vias independentes que chegam ao mesmo ponto.

A queda de oxigênio leva à *peroxidação lipídica* pelos radicais livres. A queda de ATP reduz a *síntese e a reacilação de fosfolipídios*, ou seja, a célula deixa de repor o que perde. O cálcio citosólico ativa *fosfolipases*, que degradam ativamente os fosfolipídios existentes. Menos reposição somada a mais degradação e a mais oxidação resulta em *perda de fosfolipídios da membrana*. E, em paralelo, o cálcio ativa *proteases* que quebram o citoesqueleto e as proteínas de membrana, retirando o suporte estrutural que a mantinha organizada.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-19-dano-de-membrana.jpg",
  largura: 66%,
  legenda: [Quatro caminhos independentes descendo para o mesmo desfecho. Da esquerda para a direita: radicais livres peroxidando lipídios, falta de ATP travando a reposição de fosfolipídios, fosfolipases do cálcio degradando fosfolipídios e proteases do cálcio destruindo o citoesqueleto. A convergência na base da figura explica por que a membrana é o alvo final de quase toda lesão celular. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

Há ainda uma segunda membrana em jogo, e ela merece destaque porque será central na PARTE III: a membrana dos *lisossomos*. Os lisossomos guardam enzimas digestivas em compartimento fechado justamente para que elas não ataquem a própria célula. Quando essas membranas se rompem, as enzimas escapam para o citoplasma e digerem os componentes celulares por dentro. É essa digestão enzimática que dá à necrose sua aparência característica.

#subtopico("2.8 — Dobramento anômalo de proteínas e dano direto ao DNA")

Falta um último grupo de lesões, que precisa ser tratado à parte porque não passa pela cadeia da isquemia descrita até aqui. São as doenças de dobramento proteico e o dano direto ao material genético — em geral condições inatas, ou adquiridas por infecção ou distúrbio metabólico, cujo mecanismo de morte tem pouca relação com falta de ATP, cálcio e radicais livres.

Uma proteína recém-sintetizada precisa assumir uma forma tridimensional específica para funcionar. Quando ela se dobra errado, existe um sistema de recuperação: um complexo de proteínas chamadas *chaperonas* recebe a proteína malformada e, gastando ATP, promove a redobragem até a conformação nativa correta. Em algumas doenças esse sistema não dá conta. A proteína permanece mal dobrada, não desempenha sua função e recebe uma marcação para ser destruída; o acúmulo dessas proteínas defeituosas gera dano celular importante, e a célula dispara sinalizações intracelulares de morte, fundamentalmente por apoptose. A doença de Creutzfeldt-Jakob é o exemplo citado na aula desse tipo de mecanismo.

O dano direto e extenso ao DNA segue lógica parecida: quando a lesão do material genético ultrapassa a capacidade de reparo, a própria célula reconhece o estrago e ativa o programa de apoptose, em vez de seguir dividindo com o genoma corrompido.

#sintese-box(2)[Quatro mecanismos explicam a lesão bioquímica: queda de ATP, radicais livres, dano mitocondrial e influxo de cálcio. Combinados, eles produzem uma lesão progressiva que termina em irreversibilidade. A mitocôndria funciona como chave de desvio — a transição de permeabilidade leva à necrose, a saída do citocromo c leva à apoptose — e o cálcio funciona como amplificador, ativando as enzimas que produzem os dois critérios de irreversibilidade ao mesmo tempo.]

#parte-title("PARTE III — Necrose: a morte com digestão e inflamação")

#subtopico("3.1 — O que é necrose e como ela difere da apoptose")

Chegado o ponto sem retorno, a célula pode morrer de duas maneiras, e a diferença entre elas está menos no fato de morrer do que na *sequência dos acontecimentos*.

Na *necrose*, o dano vem primeiro e a demolição vem depois. É o processo de desestruturação das proteínas intracelulares e de digestão enzimática de células que *já apresentam dano letal*. Ou seja, a célula é atingida, sofre o dano irreversível, e só então suas próprias enzimas terminam de desmanchá-la. A necrose é sempre um evento patológico.

Na *apoptose*, a ordem se inverte. Uma sinalização ativa um programa enzimático, e é esse programa que produz o dano letal — a célula é levada a se desmontar de dentro para fora, de forma controlada, a partir de uma decisão. Por isso a apoptose é chamada de *morte celular programada*, e por isso ela pode ser fisiológica.

#subtopico("3.2 — A cadeia da necrose e a diferença entre célula e arcabouço")

A necrose começa onde a PARTE II terminou: em alterações irreversíveis de pH e de permeabilidade das membranas. Dali a cadeia segue por dois ramos paralelos que depois se encontram.

Pelo primeiro ramo, o rompimento das membranas dos lisossomos *libera enzimas lisossômicas* no citoplasma. Essas enzimas digerem proteínas, lipídios e ácidos nucleicos da própria célula, produzindo a *digestão e desestruturação celular*.

Pelo segundo ramo, o rompimento da membrana plasmática *libera proteínas e enzimas intracelulares para o meio extracelular*. Além de servirem como marcadores no sangue, como visto na seção 1.6, essas moléculas sinalizam para o organismo que houve dano, e o resultado é o *recrutamento de células inflamatórias* para o local. Os leucócitos recrutados trazem consigo mais enzimas, que se somam à digestão do tecido morto.

É por isso que a necrose vem sempre acompanhada de inflamação adjacente, enquanto a apoptose não. O extravasamento de conteúdo intracelular é, ao mesmo tempo, o que permite o diagnóstico laboratorial e o que convoca a resposta inflamatória.

Há uma segunda ideia nessa cadeia, e ela é a chave para entender os tipos de necrose: a distinção entre a *célula* e o *arcabouço*. Célula é o conteúdo vivo; arcabouço é a malha de tecido conjuntivo e matriz extracelular que sustenta o órgão e dá forma a ele. As duas coisas podem ser destruídas em graus diferentes, e é essa proporção que determina o aspecto final do tecido morto. Quando o arcabouço se mantém depois que as células morreram, o órgão preserva o desenho geral e a lesão fica firme. Quando o arcabouço também é digerido, não sobra estrutura e o tecido vira uma massa líquida.

#subtopico("3.3 — Morfologia da necrose")

Dois grupos de achados identificam uma célula necrótica na lâmina corada pela hematoxilina e eosina.

O primeiro é a *eosinofilia*, isto é, a célula fica mais rosada e intensamente corada pela eosina do que a célula normal. Isso tem duas causas somadas. Primeiro, a célula perde RNA citoplasmático, e como o RNA é basofílico — capta o corante azul —, sua perda deixa o citoplasma relativamente mais rosa. Segundo, as proteínas citoplasmáticas se desnaturam, e proteínas desnaturadas ligam mais eosina. O citoplasma da célula morta, portanto, aparece vermelho-róseo homogêneo.

O segundo grupo são as *alterações nucleares*, que seguem uma sequência. Na *picnose* o núcleo encolhe e fica pequeno, denso e escuro, com a cromatina toda condensada em um bloco. Na *cariorrexe* esse núcleo picnótico se fragmenta em pedaços dispersos pelo citoplasma. E na cariólise o núcleo simplesmente desaparece, dissolvido pela ação das endonucleases — que é o que se vê no painel C da figura do túbulo renal da seção 1.4, com células sem núcleo nenhum.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-27-picnose-cariorrexe.jpg",
  largura: 62%,
  legenda: [Tecido em necrose. O citoplasma das células afetadas está rosa-intenso e homogêneo, sem a granulação normal — é a eosinofilia por perda de RNA e desnaturação proteica. Entre elas veem-se núcleos pequenos, densos e escuros (picnose) e núcleos já quebrados em fragmentos dispersos (cariorrexe). Fonte: reproduzido nos slides da aula.])

#subtopico("3.4 — Os tipos de necrose")

Os tipos de necrose não são doenças diferentes: são aparências diferentes que o tecido morto assume, dependendo do órgão, da causa e — sobretudo — do que aconteceu com o arcabouço.

Na *necrose coagulativa*, a desnaturação das proteínas predomina sobre a digestão enzimática. As enzimas que digeririam o tecido também são desnaturadas e param de funcionar, de modo que o arcabouço se mantém. O resultado é um tecido em que a arquitetura geral continua reconhecível por dias, mas as células perderam os núcleos: são os chamados *fantasmas de células*, contornos celulares preservados e vazios. É o padrão dos órgãos de circulação terminal, como o coração e o baço, e é a necrose do infarto agudo do miocárdio — o mesmo evento que, na seção 1.6, libera troponina e CK-MB para o sangue em uma sequência temporal característica.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-28-necrose-coagulativa.jpg",
  largura: 92%,
  legenda: [Necrose coagulativa. À esquerda, miocárdio infartado: as fibras mantêm o alinhamento e o desenho do tecido, mas estão intensamente eosinofílicas e sem núcleos, e há infiltrado de leucócitos entre elas. À direita, fígado, com a zona necrótica pálida à esquerda contrastando com os hepatócitos preservados e nucleados à direita. Fonte: reproduzido nos slides da aula.])

Na *necrose liquefativa*, a digestão enzimática predomina e o arcabouço não resiste. Isso acontece em duas situações: em tecidos que naturalmente têm pouco arcabouço de sustentação, como o cérebro, e em qualquer tecido no qual o arcabouço tenha sido destruído, como nos abscessos, em que as enzimas dos neutrófilos digerem tudo. As células mortas são digeridas por completo e o que resta é material líquido, dentro de uma cavidade.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-29-necrose-liquefativa.jpg",
  largura: 92%,
  legenda: [Necrose liquefativa. À esquerda, pulmão com múltiplos abscessos, focos amarelados de tecido digerido. No centro, corte de encéfalo em que a área lesada perdeu a substância e deixou uma cavidade, porque o tecido nervoso quase não tem arcabouço de sustentação. À direita, o mesmo processo na microscopia, com a zona central desestruturada e cheia de leucócitos. Fonte: reproduzido nos slides da aula.])

Na *necrose caseosa*, o aspecto macroscópico lembra queijo branco esfarelado, e daí vem o nome. Ela está geralmente associada ao granuloma da tuberculose, e microscopicamente consiste em coleções de células fragmentadas em meio a debris amorfos, cercadas por um halo de células inflamatórias. Aqui não há nem preservação do arcabouço como na coagulativa, nem liquefação completa como na liquefativa: o tecido vira uma massa amorfa delimitada.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-30-necrose-caseosa.jpg",
  largura: 62%,
  legenda: [Necrose caseosa em linfonodos comprometidos por tuberculose. O material esbranquiçado e opaco no interior das lesões é o tecido morto transformado em massa amorfa, com aspecto de queijo — bem diferente da arquitetura preservada da coagulativa e da cavidade líquida da liquefativa. Fonte: reproduzido nos slides da aula.])

Na *necrose gordurosa*, áreas focais de tecido adiposo são destruídas. O exemplo típico é a pancreatite aguda: a lipase pancreática liberada pelas células acinares lesadas cai no tecido adiposo vizinho e quebra os triglicerídeos, e os ácidos graxos liberados se combinam com cálcio formando depósitos esbranquiçados. Repare que essa é a mesma lipase que, caindo na circulação, permite o diagnóstico laboratorial da pancreatite discutido na seção 1.6.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-33-necrose-gordurosa.jpg",
  largura: 62%,
  legenda: [Necrose gordurosa no tecido adiposo peripancreático. Entre os adipócitos preservados, de contorno claro e vazio, veem-se áreas de aspecto granular e basofílico — são os focos de gordura destruída pela lipase, com depósito de cálcio. Fonte: reproduzido nos slides da aula.])

Na *necrose fibrinóide*, o material necrótico da parede de um vaso adquire aspecto homogêneo e intensamente eosinofílico, parecido com fibrina. Ela ocorre tipicamente em reações imunes que atingem vasos, ou seja, nas vasculites, e está associada à deposição de complexos antígeno-anticorpo na parede vascular.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-34-necrose-fibrinoide.jpg",
  largura: 58%,
  legenda: [Necrose fibrinóide em uma arteríola. A parede do vaso, em torno da luz que contém hemácias, está substituída por um material rosa-vivo homogêneo, sem a organização normal das camadas — o depósito que dá nome a este padrão. Fonte: reproduzido nos slides da aula.])

Por fim, a *necrose gangrenosa* não é um mecanismo próprio, e sim uma designação clínica para o comprometimento necrótico de múltiplos tecidos ao mesmo tempo, tipicamente em um membro. O quadro combina isquemia extensa e, com frequência, infecção sobreposta.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-35-necrose-gangrenosa.jpg",
  largura: 40%,
  legenda: [Necrose gangrenosa em pé. Os pododáctilos estão escurecidos e mumificados, com limite nítido em relação ao tecido viável — o comprometimento é de todo o segmento, pele, subcutâneo e planos profundos juntos, e não de um tipo celular isolado. Fonte: reproduzido nos slides da aula.])

#mini-resumo[O que separa os tipos de necrose é a sorte do arcabouço. Preservado, dá a coagulativa, com fantasmas de células e arquitetura reconhecível. Digerido, dá a liquefativa, com cavidade e material líquido. Transformado em massa amorfa delimitada, dá a caseosa da tuberculose. A gordurosa e a fibrinóide são definidas pelo substrato atacado — gordura pela lipase e parede vascular por imunocomplexos —, e a gangrenosa é a designação clínica para um segmento inteiro necrosado.]

#parte-title("PARTE IV — Apoptose, comparação e necroptose")

#subtopico("4.1 — Por que existe uma morte celular programada")

A apoptose surpreende à primeira vista porque a intuição associa morte celular a doença. Mas o organismo depende de eliminar células de forma controlada, e faz isso o tempo todo em situações completamente normais.

Entre as *situações fisiológicas*, a embriogênese é a mais evidente: a formação dos dedos, por exemplo, depende da eliminação programada das células que ocupam o espaço entre eles. Há a involução dependente de hormônio, em que tecidos regridem quando o estímulo hormonal cessa. Há a tolerância imunológica, em que linfócitos que reconheceriam o próprio organismo são eliminados antes de causar autoimunidade. E há a morte das células inflamatórias residentes ao fim de uma resposta imune, que encerra o processo em vez de deixá-lo indefinidamente ativo.

Entre as *situações patológicas*, a apoptose é acionada quando o dano ao DNA excede a capacidade de reparo, quando há acúmulo de proteínas deformadas — o mecanismo da seção 2.8 —, em infecções, especialmente por organismos intracelulares, e na atrofia patológica de órgãos.

#subtopico("4.2 — As quatro etapas do programa")

Antes de olhar as vias específicas, vale fixar a estrutura geral, que é a mesma independentemente do estímulo inicial.

Primeiro vem a *sinalização*: algo indica à célula que ela deve morrer, seja a falta de um sinal de sobrevivência, seja a presença de um sinal de morte. Depois vem o *controle e a integração*, etapa em que a célula pondera sinais pró e antiapoptóticos e decide — é aqui que a apoptose pode ser interrompida. Em seguida vem a *execução*, em que enzimas específicas desmontam a célula por dentro. E, por último, a *remoção dos fragmentos*, em que as sobras são fagocitadas.

As enzimas executoras são as *caspases*, proteases que existem na célula em forma inativa e que, uma vez ativadas, clivam alvos definidos. Elas se organizam em cascata: caspases iniciadoras ativam caspases executoras, que fazem o trabalho de demolição propriamente dito, quebrando o citoesqueleto e ativando endonucleases que fragmentam o DNA.

#subtopico("4.3 — A via intrínseca, ou mitocondrial")

A via intrínseca é acionada por sinais que vêm de dentro da própria célula: falta de fatores de crescimento, dano ao DNA, estresse do retículo endoplasmático por proteínas mal dobradas. Ela é a via que a seção 2.5 já antecipou.

O controle está numa família de proteínas, a *família Bcl-2*, dividida em dois campos que se opõem. Do lado antiapoptótico estão Bcl-2, Bcl-x e Mcl-1: em uma célula saudável, que recebe sinais de sobrevivência, essas proteínas ficam ancoradas na membrana mitocondrial e a mantêm fechada, impedindo o vazamento do citocromo c. Do lado pró-apoptótico estão *Bax* e *Bak*, efetoras que, quando ativadas, se agregam na membrana mitocondrial e formam um canal por onde o conteúdo do espaço intermembranas escapa. Um terceiro grupo, os sensores, detecta o estresse celular e antagoniza as proteínas antiapoptóticas, liberando Bax e Bak para agir.

Uma vez formado o canal, o *citocromo c* vaza para o citoplasma. Lá ele se associa à proteína adaptadora *APAF-1*, e esse complexo ativa as caspases iniciadoras, que por sua vez ativam as executoras. A partir daí a demolição é irreversível.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-38-vias-intrinseca-extrinseca.jpg",
  largura: 98%,
  legenda: [À esquerda, a via intrínseca em dois estados. Em *A*, a célula viável recebe sinal de sobrevivência, produz proteínas antiapoptóticas do tipo Bcl-2 e não há vazamento de citocromo c. Em *B*, a falta de sinal ou o dano ao DNA ativa sensores que antagonizam a Bcl-2, liberando o canal Bax/Bak; o citocromo c escapa e as caspases são ativadas. À direita, a via extrínseca: o ligante FasL une três moléculas do receptor Fas, os domínios de morte recrutam a proteína adaptadora FADD, a procaspase-8 é aproximada e se autoativa, e a caspase-8 ativa as caspases executoras. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

#subtopico("4.4 — A via extrínseca, ou dos receptores de morte")

A via extrínseca começa fora da célula. Existem receptores de membrana cuja função é receber uma ordem de morte vinda de outra célula — os principais são o *Fas* e o receptor de #sigla("TNF", [fator de necrose tumoral — citocina que, entre outras funções, pode acionar receptores de morte na superfície da célula-alvo]).

Quando o ligante correspondente, por exemplo o *FasL* presente na superfície de um linfócito T citotóxico, se liga ao receptor Fas da célula-alvo, várias moléculas do receptor se agrupam. As porções intracelulares desses receptores, chamadas *domínios de morte*, ficam então próximas umas das outras e recrutam uma proteína adaptadora, a *FADD*. A FADD, por sua vez, aproxima várias moléculas de procaspase-8. É a simples proximidade que permite que elas se clivem mutuamente e se ativem: essa autoativação gera a caspase-8, que ativa as caspases executoras e converge para o mesmo desfecho da via intrínseca.

O sistema tem freios próprios. A proteína *FLIP* se liga à caspase-8 sem cliva-la, ocupando o lugar e bloqueando a ativação. E existem inibidores fisiológicos da apoptose que atuam sobre as caspases já formadas. O TNF, em particular, tem papel duplo: por um lado aciona a via extrínseca e elimina linfócitos autorreativos, por outro pode aumentar a produção das proteínas antiapoptóticas Bcl-2 e Bcl-x.

#subtopico("4.5 — A morfologia da apoptose")

O programa apoptótico produz um conjunto de achados morfológicos completamente diferente do da necrose, e cada um deles decorre diretamente do mecanismo.

Há *contração celular*: a célula encolhe em vez de inchar, porque a membrana continua íntegra e as bombas ainda funcionam, de modo que não há entrada osmótica de água. Há *condensação da cromatina*, que se agrega em massas densas junto à membrana nuclear, resultado da ação das endonucleases ativadas pelas caspases. Há *formação de bolhas e de corpúsculos apoptóticos*: a célula se fragmenta em pedaços envoltos por membrana, cada um contendo organelas intactas. E há *fagocitose por macrófagos*, porque esses corpúsculos expõem em sua superfície sinais que os marcam para remoção.

Esse último ponto explica a característica mais importante da apoptose do ponto de vista tecidual: como o conteúdo celular nunca é derramado no meio extracelular — permanece sempre embalado por membrana até ser engolido —, *não há inflamação em volta*. A célula desaparece silenciosamente.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-26-necrose-versus-apoptose.jpg",
  largura: 96%,
  legenda: [Os dois destinos desenhados lado a lado a partir da mesma célula normal. À esquerda, a via da necrose: a lesão reversível produz edema do retículo e das mitocôndrias e bolhas de membrana, e pode ainda regredir (seta _Recovery_); se a agressão progride, a membrana plasmática se rompe, o conteúdo vaza e células inflamatórias acorrem. À direita, a apoptose: a cromatina se condensa, a célula se contrai e se fragmenta em corpúsculos envoltos por membrana, que um fagócito remove sem que nada extravase. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-41-corpos-apoptoticos.jpg",
  largura: 90%,
  legenda: [Apoptose na lâmina e na microscopia eletrônica. Em *A*, epiderme: uma única célula arredondada, encolhida e intensamente eosinofílica, isolada no meio de vizinhas absolutamente normais e sem qualquer infiltrado inflamatório em volta — o retrato da morte individual e silenciosa. Em *B*, microscopia eletrônica com a cromatina condensada em massas densas junto à membrana nuclear. Abaixo, imagens de fragmentação nuclear. Fonte: Robbins, _Pathologic basis of disease_, 8ª edição, reproduzido nos slides da aula.])

#subtopico("4.6 — Necrose e apoptose lado a lado")

Reunidos os dois processos, o quadro comparativo deixa de ser uma lista para decorar e passa a ser a consequência previsível de dois mecanismos diferentes.

#align(center, block(width: 96%, breakable: false, stroke: 0.5pt + gray-border, inset: 10pt, radius: 4pt, fill: gray-bg,
  table(
    columns: (1.05fr, 1fr, 1fr),
    stroke: (x, y) => if y == 1 { (top: 0.5pt + gray-border) } else { none },
    inset: 6pt,
    align: left,
    text(size: 9pt, weight: "bold", fill: navy)[Característica],
    text(size: 9pt, weight: "bold", fill: navy)[Necrose típica],
    text(size: 9pt, weight: "bold", fill: navy)[Apoptose],
    text(size: 9pt)[Tamanho da célula], text(size: 9pt)[Aumentado, por edema], text(size: 9pt)[Reduzido, por contração],
    text(size: 9pt)[Núcleo], text(size: 9pt)[Picnótico até ausente], text(size: 9pt)[Fragmentado em pedaços],
    text(size: 9pt)[Membrana plasmática], text(size: 9pt)[Rompida], text(size: 9pt)[Íntegra],
    text(size: 9pt)[Conteúdos celulares], text(size: 9pt)[Sofrem digestão enzimática], text(size: 9pt)[Permanecem intactos],
    text(size: 9pt)[Inflamação adjacente], text(size: 9pt)[Presente], text(size: 9pt)[Ausente],
    text(size: 9pt)[Papel no organismo], text(size: 9pt)[Sempre patológico], text(size: 9pt)[Fisiológico ou patológico],
  )
))

Cada linha decorre da anterior. A membrana rompida na necrose explica a entrada de água e o aumento de tamanho, a digestão do conteúdo e a inflamação; a membrana íntegra na apoptose explica a contração, a preservação do conteúdo e a ausência de inflamação. Se houver uma única linha para reter, que seja a da membrana, porque dela se deduzem todas as outras.

#subtopico("4.7 — Quando a apoptose falta e quando sobra")

Alguns quadros clínicos se explicam por desvios na regulação da apoptose, e eles se organizam em dois grupos simétricos.

Quando o dano ao DNA é detectado, o *p53* é a proteína que interrompe o ciclo celular para permitir o reparo e, se o reparo não for possível, induz a apoptose através de Bax e Bak. Uma célula com dano genético que perdeu esse controle continua se dividindo com o genoma corrompido.

Quando a apoptose é *inibida* de forma inapropriada, células que deveriam morrer sobrevivem. Se forem linfócitos autorreativos que escaparam da tolerância, o resultado tende a ser doença autoimune; se forem células com dano genético acumulado, o resultado tende a ser neoplasia. Quando a apoptose é *excessiva*, morrem células que deveriam permanecer, e esse é o padrão das doenças neurodegenerativas.

#subtopico("4.8 — Necroptose, a fronteira entre os dois mundos")

Um último processo mostra que a divisão entre necrose e apoptose não é tão limpa quanto o quadro comparativo sugere. A *necroptose*, ou necrose programada, tem o gatilho e a regulação de uma via programada, mas a aparência final de uma necrose.

Ela é disparada pelo TNF ligando-se ao seu receptor, o que monta um complexo em torno da proteína RIP1. Se a caspase-8 for ativada nesse complexo, a célula segue para a apoptose habitual. Se a caspase-8 *não* for ativada, forma-se o complexo RIP1–RIP3, chamado *necrossomo*, e o caminho muda: seguem-se alterações metabólicas com queda de ATP e aumento de radicais livres, peroxidação lipídica, aumento da permeabilidade das membranas lisossômicas e degradação de macromoléculas, terminando na perda de integridade da célula e das organelas. Ou seja, o desfecho tem todos os elementos da necrose — rompimento de membrana e derrame de conteúdo —, mas foi acionado por uma via de sinalização regulada.

#figura-nebli("/figuras/pato-01-lesao-e-morte-celular/slide-45-necroptose.png",
  largura: 42%,
  legenda: [A bifurcação da necroptose. Do complexo montado sob o receptor de TNF saem dois caminhos: com ativação da caspase-8, a célula morre por apoptose, à direita; sem ela, forma-se o necrossomo RIP1–RIP3 e a célula percorre queda de ATP, radicais livres e ruptura de membranas até a morte por necroptose, à esquerda. Fonte: Robbins, _Pathologic basis of disease_, 9ª edição, reproduzido nos slides da aula.])

#conclusao-box[
  A aula inteira cabe numa única cadeia causal, e vale reconstruí-la de ponta a ponta. Uma célula em homeostase gasta ATP para manter gradientes iônicos e membranas íntegras. Um estímulo agressor leve e prolongado permite adaptação; um estímulo intenso ou rápido não dá tempo para isso e produz lesão, que é reversível enquanto for moderada e transitória e irreversível quando for grave e progressiva. A irreversibilidade tem dois critérios objetivos: perda de permeabilidade seletiva da membrana e destruição excessiva de DNA e proteínas — e é o primeiro deles que faz uma enzima intracelular como a troponina aparecer no sangue, transformando um conceito de patologia no exame que diferencia angina de infarto.

  Os mecanismos que levam até lá são quatro, e se alimentam mutuamente. A falta de oxigênio derruba a fosforilação oxidativa e o ATP; sem ATP a bomba de sódio para, entra sódio com água e a célula incha, a glicólise anaeróbica acidifica o meio e os ribossomos se soltam. A mitocôndria disfuncional produz radicais livres que peroxidam lipídios, oxidam proteínas e lesam o DNA — o mesmo mecanismo que explica a lesão de reperfusão e a urgência de reabrir vasos depressa. Sem ATP, as bombas de cálcio também param, o cálcio se acumula no citoplasma e ativa fosfolipases, proteases, endonucleases e ATPases, que atacam exatamente os dois critérios de irreversibilidade ao mesmo tempo. E é a mitocôndria que funciona como chave de desvio: a transição de permeabilidade leva à necrose, a saída do citocromo c leva à apoptose.

  Os dois desfechos se distinguem por um único fato estrutural, do qual todo o resto decorre. Na necrose a membrana se rompe: a célula incha, o conteúdo extravasa, enzimas lisossômicas digerem o que restou e a inflamação é recrutada — e o destino do arcabouço define se o resultado será coagulativo, liquefativo, caseoso, gorduroso, fibrinóide ou gangrenoso. Na apoptose a membrana permanece íntegra: a célula se contrai, fragmenta-se em corpúsculos embalados e é fagocitada sem inflamação, por um programa de caspases acionado pela via intrínseca da mitocôndria ou pela via extrínseca dos receptores de morte. A necroptose mostra que os dois mundos se tocam, com gatilho programado e desfecho necrótico.

  Esta é a base sobre a qual se apoiam as aulas seguintes do bloco. A adaptação celular, apenas esboçada aqui, tem mecanismos próprios; o infarto do miocárdio será revisitado como modelo de necrose coagulativa; os acúmulos intracelulares retomarão a esteatose mencionada na fase reversível; e a inflamação, que aqui apareceu apenas como consequência do extravasamento de conteúdo, se tornará objeto por direito próprio.
]
