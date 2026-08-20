#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Um adulto come cerca de uma tonelada de comida por ano e, ainda assim, costuma terminar o ano com um peso parecido com o do começo. Isso não acontece por acaso nem por disciplina: acontece porque o corpo *mede* o próprio estoque de energia e ajusta, sem que ninguém perceba, o quanto se come e o quanto se gasta. Este resumo persegue como essa medida é feita e por onde ela falha. Primeiro, o alicerce: como se fecha a conta da energia, por que o estoque é feito de gordura e como um hormônio consegue comandar o corpo inteiro a partir de algumas moléculas — a lógica da cascata, da amplificação e da retroalimentação negativa. Depois, o mensageiro principal: a leptina, o hormônio que o próprio tecido adiposo fabrica para dizer ao cérebro o tamanho da reserva, sua irmã de sinal invertido, a adiponectina, e a razão pela qual dar leptina a um obeso não o emagrece. Por fim, o centro de comando: os dois neurônios do hipotálamo que disputam a decisão de comer, os sinais que o tubo digestivo manda a cada refeição, e o que acontece com o metabolismo inteiro quando o tecido adiposo, cheio demais, adoece. A linha que atravessa tudo é uma só: massa corpórea não é resultado de força de vontade contra apetite, é a saída de uma alça de controle biológica — e entender a alça é entender por que ela quebra e como se tenta consertá-la.
]

#parte-title("PARTE I — O balanço energético e a orquestra que o comanda", primeira: true)

#subtopico("1.1 — A conta que o corpo fecha todo dia")

Toda a regulação da massa corpórea repousa sobre uma equação de contabilidade que não tem como ser burlada: a energia que entra pela comida é igual à energia gasta mais a energia armazenada. Se os dois primeiros termos se igualam, o estoque fica parado; se entra mais do que se gasta, a diferença precisa ir para algum lugar, e esse lugar é o tecido adiposo. O ponto que costuma escapar é que *nenhum* dos três termos é fixo. O gasto não é só exercício — a maior fatia dele é o metabolismo basal, a energia que o corpo consome apenas para manter bomba de sódio e potássio funcionando, coração batendo, proteínas sendo renovadas e temperatura estável. Uma parte menor, mas regulada, é o calor produzido de propósito, e é exatamente sobre essa parte que o sistema hormonal consegue mexer.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-11-crop.png",
  largura: 66%,
  legenda: [A alça básica do estoque: o alimento entra e vira gordura por síntese; a gordura sai por oxidação, virando energia e calor. As setas tracejadas voltando de dentro do tecido adiposo são o que interessa — o próprio estoque regula as duas torneiras.])

Por que o estoque é feito de gordura, e não de açúcar, é uma decisão de engenharia que vale entender de saída. O #termo-nota[triacilglicerol][glicerol com três ácidos graxos ligados — a forma química em que a gordura é estocada no adipócito] é praticamente carbono e hidrogênio, com pouquíssimo oxigênio na molécula: por isso rende cerca de 9 kcal por grama quando é oxidado, mais que o dobro das 4 kcal por grama de um carboidrato. E há um segundo ganho, ainda maior. O glicogênio é armazenado hidratado, arrastando duas a três vezes o próprio peso em água; a gota de gordura do adipócito é anidra. Somando os dois efeitos, guardar energia como gordura é cerca de seis vezes mais eficiente por quilo carregado do que guardá-la como glicogênio. *Um adulto magro leva no corpo reserva de gordura para semanas de jejum e reserva de glicogênio para menos de um dia* — e essa assimetria explica por que o glicogênio é o troco do metabolismo, enquanto a gordura é a poupança.

#mini-resumo[Entrada = gasto + estoque. O gasto é dominado pelo metabolismo basal, e só uma fração dele é regulável. O estoque é feito de triacilglicerol porque gordura é anidra e mais reduzida — 9 kcal/g contra 4 kcal/g, e sem carregar água junto.]

#subtopico("1.2 — Teoria lipostática: o estoque é medido, e defendido")

À primeira vista, parece natural pensar no tecido adiposo como um porão: o que sobra desce para lá e fica. Se fosse assim, um excedente calórico constante produziria ganho de peso linear e indefinido, e uma dieta produziria perda proporcional e permanente. Não é o que acontece — e a explicação é a *teoria lipostática*, formulada muito antes de existir qualquer evidência molecular. Ela propõe que existe uma substância circulante cuja concentração é proporcional à quantidade de gordura estocada, e que o cérebro lê essa concentração como se lesse o nível de um tanque. Quando o nível sobe, o cérebro reduz a ingestão e aumenta o gasto; quando o nível desce, faz o contrário.

Repare no que essa proposta exige. Ela exige que o tecido adiposo *fale*, e que o cérebro tenha um receptor sintonizado nessa fala. Enquanto essa substância não foi identificada, a lipostática era só uma hipótese elegante — e a PARTE II deste resumo é, em boa medida, a história de como ela foi encontrada. O que já dá para adiantar é a consequência clínica: se o sistema defende ativamente um valor de massa gorda, então perder peso não é apenas subtrair calorias, é lutar contra uma alça de controle que interpreta a perda como ameaça e responde reduzindo o gasto e aumentando a fome. É por isso que a maior dificuldade do tratamento da obesidade não é emagrecer, e sim não reganhar.

E há um detalhe que muda o problema todo: *o valor defendido pode se deslocar*. A capacidade de estocar com eficiência foi vantagem enquanto comida era escassa e imprevisível, e ser magro protegia de predadores que hoje não existem. Num ambiente com alimento disponível a qualquer hora, com preparo industrial que estimula fortemente as vias de recompensa do cérebro, e com mudanças de composição da microbiota intestinal, a mesma máquina de guardar passa a defender um estoque maior do que o saudável. A obesidade, nessa leitura, não é a falha do sistema — é o sistema funcionando exatamente como foi construído, num ambiente para o qual ele não foi construído.

#subtopico("1.3 — Como um hormônio comanda: cascata, amplificação e retroalimentação")

Um hormônio circula em concentração ridiculamente pequena — picomolar a nanomolar, o equivalente a algumas gotas num reservatório — e mesmo assim muda o comportamento metabólico de órgãos inteiros. O truque é que ele não faz o trabalho: ele autoriza. Pense num sistema de alarme em que apertar um botão pequeno aciona uma sirene que mobiliza um prédio inteiro. Em cada degrau, o sinal ganha volume. O hipotálamo libera alguns picomols de um fator liberador direto nos vasos que descem para a hipófise anterior; a hipófise responde liberando nanomols de um hormônio trópico na circulação geral; a glândula-alvo responde produzindo micromols do hormônio final, que alcança todas as células do corpo. Três degraus, e o sinal foi multiplicado milhares de vezes.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-04-crop.png",
  largura: 48%,
  legenda: [O eixo completo, do estímulo à resposta: frio é captado por neurônio sensorial, o hipotálamo secreta o fator liberador, a hipófise anterior secreta o hormônio trópico, a tireoide secreta o hormônio final e o tecido responde. As setas vermelhas de retorno são a retroalimentação negativa — repare que ela alcança os *dois* degraus acima, não só o de cima.])

A segunda peça é o que impede o sistema de disparar sem parar: a #termo-nota[retroalimentação negativa][arranjo em que o produto final de uma via inibe as etapas que o produziram, estabilizando a concentração — mesma lógica de um termostato]. O hormônio final, ao subir, inibe tanto a hipófise quanto o hipotálamo. O efeito é o de um termostato: qualquer desvio para cima aciona o freio, qualquer desvio para baixo o solta, e a concentração oscila estreitamente em torno de um valor. *O detalhe que mais confunde é o alcance do freio* — como ele age nos dois degraus acima, um hormônio administrado de fora suprime o eixo inteiro, e a glândula, sem estímulo trófico, atrofia. É a razão pela qual corticoide em uso prolongado não pode ser suspenso de uma vez.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-07-crop.png",
  largura: 84%,
  legenda: [O mapa inteiro do sistema neuroendócrino. Leia de cima para baixo: o sistema nervoso central recebe o sinal do ambiente, o hipotálamo converte esse sinal em hormônio, a hipófise distribui, e cada eixo termina num tecido diferente. Repare na coluna da direita — o hipotálamo também alcança diretamente a medula adrenal por via nervosa, sem passar pela hipófise.])

Vale nomear o que torna esse arranjo *neuroendócrino*. A célula que inicia a cascata é um neurônio de verdade: recebe sinapses, dispara potencial de ação e, em vez de liberar neurotransmissor numa fenda estreita, libera seu produto na corrente sanguínea. Essa célula neurossecretora é a dobradiça entre dois mundos — o sistema nervoso, que é rápido e endereçado, e o sistema endócrino, que é lento e difuso. Guarde essa dobradiça: na PARTE III, o hipotálamo vai fazer exatamente o mesmo movimento para controlar o apetite.

#subtopico("1.4 — Duas velocidades de resposta: catecolaminas e cortisol")

O eixo que acabamos de montar tem uma característica que a fisiologia do estresse deixa evidente: o corpo usa duas linhas de resposta com tempos completamente diferentes, e as duas terminam na mesma glândula. A resposta rápida não passa pela hipófise. Uma fibra nervosa simpática desce da medula espinhal direto para a medula adrenal e, em segundos, faz liberar #termo-nota[catecolaminas][adrenalina e noradrenalina — hormônios derivados da tirosina, hidrossolúveis, que agem em receptores de superfície]. O efeito é imediato: frequência cardíaca e pressão sobem, brônquios dilatam, o fígado quebra glicogênio e joga glicose no sangue, o fluxo sai da digestão e vai para o músculo, e a taxa metabólica sobe.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-06-crop.png",
  largura: 52%,
  legenda: [As duas linhas do estresse lado a lado. À esquerda, o atalho nervoso: medula espinhal → fibra simpática → medula adrenal → catecolaminas, em segundos. À direita, o caminho longo: hipotálamo → CRH → ACTH → córtex adrenal → glicocorticoides, em minutos a horas. Compare as duas listas de efeitos embaixo — a de curto prazo mobiliza, a de longo prazo reorganiza.])

A resposta lenta percorre o eixo inteiro. O hipotálamo secreta o #sigla("CRH", [hormônio liberador de corticotropina — primeiro degrau do eixo do cortisol]), a hipófise anterior secreta o #sigla("ACTH", [hormônio adrenocorticotrófico — estimula o córtex adrenal a produzir cortisol]) e o córtex adrenal, minutos depois, produz glicocorticoides. O cortisol também mobiliza energia, mas por outro caminho e com outra duração: quebra proteína muscular para fornecer aminoácidos, aciona a gliconeogênese hepática, favorece a lipólise e suprime respostas imunes e reprodutivas. A diferença de tempo tem uma causa química direta: a catecolamina é hidrossolúvel, não atravessa a membrana e age por receptor de superfície, com resposta em segundos; o cortisol é um esteroide lipossolúvel, entra na célula, liga-se a um receptor que vai ao núcleo e muda a *transcrição de genes* — por isso demora e por isso persiste.

#confusao-prevista(
  titulo: "Medula e córtex da adrenal não são a mesma glândula",
  aluno_acha: [aluno acha que a adrenal é um tecido só, que secreta adrenalina e cortisol pelo mesmo comando],
  mecanismo: [são dois órgãos empacotados juntos, com origens embrionárias distintas. A *medula* é tecido nervoso modificado — um gânglio simpático que perdeu os axônios e passou a secretar catecolaminas no sangue, sob comando nervoso direto. O *córtex* é tecido esteroidogênico, sem inervação de comando, que só produz cortisol quando o ACTH chega pelo sangue. Duas origens, dois comandos, dois tempos de resposta.],
)

#subtopico("1.5 — O tecido adiposo entra na orquestra como glândula")

Falta uma peça no mapa da coordenação metabólica, e ela é a peça que este resumo persegue. Nos esquemas clássicos, o tecido adiposo aparece na ponta da seta, como destino: o lugar onde a energia excedente é depositada. Essa leitura está incompleta desde os anos 1990. O adipócito secreta na circulação um conjunto de proteínas mensageiras — as #termo-nota[adipocinas][proteínas sinalizadoras secretadas pelo tecido adiposo na circulação, como leptina, adiponectina e resistina] —, e com elas informa o resto do corpo sobre o tamanho da reserva, sobre o estado inflamatório local e sobre a disponibilidade de combustível. O tecido adiposo é, portanto, um órgão endócrino de pleno direito, com a particularidade de estar distribuído pelo corpo inteiro em vez de concentrado numa cápsula.

Duas propriedades tornam esse órgão diferente dos demais. A primeira é que sua massa varia enormemente — pode multiplicar por cinco no mesmo indivíduo, o que nenhuma outra glândula faz —, e como a secreção de várias adipocinas é proporcional à massa, o *sinal* também varia junto. A segunda é que ele não é um tecido único. A gordura branca estoca triacilglicerol numa gota única que empurra o núcleo para a borda, e é ela que secreta leptina; a gordura parda é recheada de mitocôndrias e existe para uma finalidade oposta, gerar calor, o que a torna o efetor da #termo-nota[termogênese][produção deliberada de calor pelo metabolismo, sem trabalho mecânico associado, usada para manter a temperatura e queimar excedente].

*Daqui para frente, cada mecanismo desta apostila é uma frase que o tecido adiposo diz ou deixa de dizer* — e a primeira delas, a mais importante, é o assunto da PARTE II.

#parte-title("PARTE II — As adipocinas: leptina, adiponectina e o freio que falha")

#subtopico("2.1 — Leptina, o produto do gene ob")

A substância que a teoria lipostática exigia recebeu nome em 1994, e o nome veio do grego para "magro": leptina. Ela é uma proteína de 167 aminoácidos secretada pelo adipócito branco, e a propriedade que a torna a candidata perfeita ao papel é a proporcionalidade — *quanto mais massa de gordura, mais leptina no sangue*. A concentração circulante não informa o que se comeu no almoço; informa quanto de reserva existe estocada, uma informação que muda em escala de dias e semanas. Chegando ao hipotálamo, essa concentração é lida, e a leitura tem dois efeitos somados: reduzir a ingestão de alimento e aumentar o gasto energético. Nos termos da PARTE I, é a alça de retroalimentação negativa da lipostática finalmente fechada — mais estoque produz mais sinal, e mais sinal reduz o estoque.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-20-crop.png",
  largura: 40%,
  legenda: [A mesma alça da PARTE I, agora com o mensageiro nomeado. A leptina sai do tecido adiposo em quantidade proporcional ao estoque, fecha a torneira de cima (bloqueia a síntese de gordura, reduzindo a ingestão) e abre a de baixo (estimula a oxidação, aumentando o gasto).])

#figura-lateral("/figuras/regulacao-massa-corporea/slide-22.png",
  lado: "right",
  largura-figura: 42%,
  texto: [O gene que codifica a leptina é chamado _ob_, de _obese_, e recebeu esse nome pelo camundongo da foto. O animal à esquerda é _ob/ob_: tem os dois alelos defeituosos e não fabrica leptina nenhuma. O que se vê nele é a alça de controle rompida na origem — o cérebro nunca recebe a informação de que há estoque e se comporta como se o animal estivesse permanentemente em jejum. O resultado é apetite voraz, obesidade extrema, alterações metabólicas típicas e, o detalhe mais revelador, *sensibilidade ao frio*.],
  legenda: [Camundongo _ob/ob_ e um irmão normal, mesma idade.])

A sensibilidade ao frio merece atenção porque ela desmonta a leitura mais comum sobre a leptina. Se o hormônio apenas reduzisse o apetite, faltar leptina causaria hiperfagia e nada mais. Mas o animal também não consegue gerar calor direito, o que significa que a leptina, além de frear a entrada, *comanda o gasto* — e comanda pela via termogênica. Guarde essa dupla função: ela é o assunto do subtópico 2.3 e o motivo pelo qual o tratamento da obesidade é muito mais difícil do que "comer menos".

#subtopico("2.2 — Parabiose: hormônio faltando de um lado, receptor faltando do outro")

Havia uma segunda linhagem de camundongo obeso, chamada _db_, de _diabetes_, com um problema aparentemente idêntico ao do _ob_: hiperfagia, obesidade e distúrbio metabólico. Para saber se as duas obesidades tinham a mesma causa, Douglas Coleman usou nos anos 1960 uma técnica que hoje parece brutal e continua sendo elegante: a #termo-nota[parabiose][união cirúrgica de dois animais de modo que compartilhem a circulação sanguínea, permitindo testar se um fator do plasma de um afeta o outro]. Costurados lado a lado, os dois animais passam a partilhar tudo o que circula no plasma. Se a doença de um for causada pela falta de um fator circulante, o parceiro que o tem deve corrigi-la.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-24-crop.png",
  largura: 72%,
  legenda: [Os pares de Coleman (1969). Da esquerda para a direita: _db/db_ com normal, _db/db_ com _ob/ob_, _ob/ob_ com normal e o par-controle de dois normais. As barras embaixo, cobertas na animação do slide, marcam a ingestão de cada animal. O padrão a extrair: o _ob/ob_ melhora quando unido a qualquer parceiro; o _db/db_ nunca melhora, e ainda emagrece quem se une a ele.])

O resultado dividiu as duas doenças de uma vez. O camundongo _ob/ob_ unido a um animal normal *emagreceu e comeu menos* — logo, o que lhe faltava era um fator presente no sangue do parceiro. O camundongo _db/db_ unido a um animal normal não mudou nada; pior, o parceiro normal parou de comer e emagreceu até morrer de inanição. A conclusão é bonita e vale reconstruir com calma: o _db/db_ tem o fator circulante em excesso — tanto que envenena de saciedade o parceiro —, mas é incapaz de responder a ele. Ele não é surdo por falta de voz; é surdo por falta de ouvido. Quando os dois mutantes foram unidos entre si, a previsão se confirmou: o _ob/ob_ emagreceu, recebendo o fator do _db/db_, e o _db/db_ permaneceu obeso.

*Duas décadas antes de qualquer clonagem, a cirurgia já havia previsto duas moléculas distintas.* O gene _ob_ foi identificado em 1994 e codifica a leptina; o gene _db_ foi identificado logo depois e codifica o receptor da leptina. A lógica que a parabiose estabeleceu é a mesma que se aplica a qualquer via de sinalização: quando um sistema hormonal falha, o defeito está no ligante ou no receptor, e o comportamento do hormônio circulante — baixo no primeiro caso, alto no segundo — é o que separa os dois.

#subtopico("2.3 — O braço periférico da leptina: do simpático ao calor")

A leptina reduz o apetite no hipotálamo, e essa metade da história é a mais conhecida. A outra metade é o gasto, e ela funciona por uma via que sai do cérebro e volta para o tecido adiposo. Os neurônios hipotalâmicos que leram a leptina aumentam o tônus do sistema nervoso simpático; as fibras simpáticas que inervam o tecido adiposo liberam noradrenalina; e a noradrenalina encontra no adipócito um receptor específico, o receptor β#sub[3]-adrenérgico. Repare no desenho: *a leptina não age no adipócito*, ela age no cérebro, e o cérebro responde por nervo. O adipócito recebe uma ordem nervosa, não hormonal.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-26-crop.png",
  largura: 88%,
  legenda: [À esquerda, a alça completa: a leptina sobe pelo sangue até o hipotálamo — arqueado, ventromedial e paraventricular — e a resposta desce por neurônio simpático até o tecido adiposo. À direita, o que acontece dentro do adipócito quando a noradrenalina chega: β#sub[3] → proteína G → adenilato-ciclase → AMPc → PKA, e daí para os dois destinos — fosforilar perilipina e lipase para liberar ácido graxo, e induzir a expressão da UCP1 no núcleo.])

A partir do receptor, a cadeia é a via clássica de proteína G. O β#sub[3] ativa a #termo-nota[adenilato-ciclase][enzima de membrana que converte ATP em AMPc, o segundo mensageiro da via adrenérgica], que converte #sigla("ATP", [adenosina trifosfato — a moeda energética da célula]) em #sigla("AMPc", [AMP cíclico — segundo mensageiro que ativa a proteína-quinase A]); o AMPc solta as subunidades catalíticas da #sigla("PKA", [proteína-quinase A — enzima que fosforila alvos em resposta ao AMPc]); e a PKA fosforila dois alvos que trabalham juntos. O primeiro é a #termo-nota[perilipina][proteína que reveste a gota de gordura e a protege; fosforilada, muda de forma e libera acesso das lipases ao triacilglicerol], que reveste a gota lipídica como uma casca protetora — fosforilada, ela se reorganiza e abre passagem. O segundo é a lipase hormônio-sensível, que só então alcança o triacilglicerol e o quebra. O produto dessa #termo-nota[lipólise][quebra do triacilglicerol estocado em ácidos graxos livres e glicerol, liberados para uso da própria célula ou de outros tecidos] são ácidos graxos livres, que entram na mitocôndria e alimentam a β-oxidação.

A PKA faz ainda uma terceira coisa, e é ela que fecha o mecanismo do calor: aumenta a expressão do gene da #sigla("UCP1", [proteína desacopladora 1 — canal de próton da membrana mitocondrial interna, característico da gordura parda]). Para entender o que essa proteína faz, é preciso lembrar como a mitocôndria fabrica ATP: a cadeia respiratória bombeia prótons para fora, criando um gradiente, e esses prótons só deveriam voltar passando pela ATP-sintase, que aproveita a passagem para fabricar ATP. A UCP1 é um caminho alternativo — um poro que deixa o próton voltar *sem* passar pela turbina. A energia do gradiente, que viraria ATP, sai como calor. É por isso que a queima aumenta sem que a célula produza mais ATP, e é por isso que o camundongo sem leptina sente frio.

#mini-resumo[Leptina → hipotálamo → simpático → noradrenalina → β#sub[3] → AMPc → PKA. A PKA fosforila perilipina e lipase (libera ácido graxo) e induz a UCP1 (dissipa o gradiente como calor). Um sinal, dois destinos: mobilizar e queimar.]

#subtopico("2.4 — Resistência à leptina: por que repor não funciona")

Com o mecanismo montado, a expectativa terapêutica dos anos 1990 era óbvia: se falta o freio, basta repô-lo. A leptina recombinante foi produzida e testada, e o resultado foi decepcionante. A explicação estava no primeiro exame de sangue: *a maioria absoluta dos obesos tem leptina alta*, não baixa — proporcional à massa gorda, como a fisiologia previa. Não falta hormônio. O que falha é a leitura.

#atencao-box("Resistência não é deficiência — e a diferença decide a conduta", [O aluno costuma derrapar aqui tratando o obeso comum como um _ob/ob_ humano, e concluindo que dar leptina resolve. A dosagem desfaz o engano: no _ob/ob_ a leptina é indetectável e a reposição corrige tudo; no obeso comum a leptina está muito alta e a reposição não muda o peso. O quadro humano típico corresponde ao lado _db_ do experimento de Coleman — sinal presente, resposta ausente. O bloqueio é *central* e tem três andares possíveis: transporte reduzido da leptina através da barreira hematoencefálica, receptor de leptina menos responsivo no hipotálamo, e sinalização travada a jusante do receptor, com inibidores intracelulares induzidos pela própria estimulação crônica e pela inflamação. Repor hormônio num sistema cujo receptor não responde é subir o volume de um rádio desligado.])

A exceção confirma a lógica e é clinicamente preciosa.

#clinica-box("Deficiência congênita de leptina", [Uma criança com mutação bialélica no gene da leptina apresenta hiperfagia extrema desde os primeiros meses, obesidade grave e precoce, atraso puberal por falta do sinal permissivo da leptina sobre o eixo reprodutivo, e maior suscetibilidade a infecções. A dosagem sérica de leptina vem indetectável apesar da enorme massa gorda — a dissociação que fecha o diagnóstico. O tratamento com leptina recombinante normaliza o apetite em dias e reduz drasticamente a massa corpórea, com recuperação do eixo puberal. É o único cenário em que repor leptina funciona, exatamente porque é o único em que ela de fato falta.])

Vale extrair a regra geral, que serve para toda a endocrinologia: diante de uma síndrome de "falta de efeito hormonal", medir o hormônio separa dois mundos. Hormônio baixo aponta para defeito de produção, e a reposição corrige; hormônio alto aponta para defeito de receptor ou de transdução, e a reposição não corrige nada. Esse é o mesmo raciocínio que vamos aplicar à insulina na PARTE III — e é a razão pela qual o desenho de fármacos contra a obesidade abandonou a leptina e migrou para outras alças da mesma rede.

#subtopico("2.5 — Adiponectina e a AMPK: a adipocina que sobe quando a gordura desce")

Se todas as adipocinas subissem com a massa gorda, o tecido adiposo teria uma só voz. A adiponectina inverte essa expectativa: ela é *mais* abundante em indivíduos magros e cai à medida que a obesidade se instala, em boa parte porque o fator de necrose tumoral produzido no tecido adiposo inflamado inibe sua expressão. Ter pouca adiponectina, portanto, é marca de tecido adiposo doente — e as consequências dessa queda são metabólicas e vasculares, o que faz dela uma das pontes mais diretas entre obesidade e doença cardiovascular.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-27-crop.png",
  largura: 76%,
  legenda: [À esquerda, os efeitos da adiponectina sobre a parede do vaso: sustenta a célula endotelial, freia a transformação do macrófago em célula espumosa e empurra a polarização para o perfil anti-inflamatório, contendo doença vascular. À direita, o eixo metabólico: AMPK ativada fosforila a acetil-CoA carboxilase, inativando-a — sem malonil-CoA, a carnitina-aciltransferase I é liberada e o ácido graxo entra na mitocôndria para ser oxidado.])

O mecanismo metabólico passa por um sensor que vale conhecer bem, porque ele reaparece em farmacologia e em exercício: a #sigla("AMPK", [proteína-quinase ativada por AMP — sensor de baixa energia celular]). Pense nela como o alarme de caixa baixo da célula. Quando o ATP é consumido, sobra #sigla("AMP", [adenosina monofosfato — acumula quando o ATP é gasto e sinaliza baixa energia]); a AMPK detecta essa subida de AMP e liga as vias que *produzem* energia, desligando as que a *gastam*. A adiponectina ativa a AMPK no músculo e no fígado, e a partir daí a cadeia é curta e decisiva: a AMPK fosforila a #termo-nota[acetil-CoA carboxilase][enzima que converte acetil-CoA em malonil-CoA, primeiro passo comprometido da síntese de ácidos graxos] e a *inativa*.

Repare no encadeamento, porque ele é um dos mais elegantes do metabolismo. A acetil-CoA carboxilase produz malonil-CoA. O malonil-CoA tem duas funções: é o tijolo da síntese de ácidos graxos e, ao mesmo tempo, é o inibidor natural da carnitina-aciltransferase I, a enzima que carrega o ácido graxo para dentro da mitocôndria. Uma única fosforilação, portanto, faz duas coisas opostas ao mesmo tempo: interrompe a fabricação de gordura e, ao derrubar o malonil-CoA, *libera a porta de entrada* para a queima. Ou seja: onde há adiponectina, a célula para de guardar e começa a gastar. Na obesidade, com adiponectina baixa, essa dupla ordem se enfraquece justamente quando seria mais necessária — e o excesso de ácido graxo que sobra é o que vai adoecer o metabolismo inteiro na PARTE III.

#parte-title("PARTE III — O comando hipotalâmico e a doença que nasce quando ele é vencido")

#subtopico("3.1 — O núcleo arqueado: dois neurônios disputando a decisão")

Toda a PARTE II terminou com hormônios chegando ao hipotálamo, sem dizer o que acontece lá dentro. O lugar exato onde a leptina é lida chama-se núcleo arqueado, e sua posição não é acidental: ele fica encostado na eminência mediana, uma das poucas regiões do encéfalo em que a barreira hematoencefálica é frouxa. *É por essa janela que hormônios do sangue alcançam neurônios* — sem ela, leptina, insulina e grelina simplesmente não chegariam ao cérebro.

Dentro do arqueado moram duas populações de neurônios de primeira ordem que se opõem ponto a ponto. A primeira produz o #sigla("NPY", [neuropeptídeo Y — neuropeptídeo orexígeno do núcleo arqueado]) e a #sigla("AgRP", [proteína relacionada ao agouti — antagonista do receptor MC4R, orexígena]), e é #termo-nota[orexígena][que estimula a ingestão de alimento; o oposto de anorexígeno] — quando ela dispara, o animal come. A segunda produz a #sigla("POMC", [pró-opiomelanocortina — proteína precursora que, clivada, gera o α-MSH]) e o #sigla("CART", [transcrito regulado por cocaína e anfetamina — neuropeptídeo anorexígeno]), e é #termo-nota[anorexígena][que reduz a ingestão de alimento e aumenta o gasto energético] — quando ela dispara, o animal para de comer e gasta mais.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-32-crop.png",
  largura: 46%,
  legenda: [O circuito do arqueado. Embaixo, os três sinais periféricos e seus destinos: grelina do estômago *ativa* o neurônio NPY/AgRP (+); insulina e leptina *inibem* esse mesmo neurônio (−) e *ativam* o POMC (+). Acima, os neurônios de segunda ordem: o NPY/AgRP estimula o MCH da área lateral e, ao mesmo tempo, inibe a saciedade.])

O detalhe que faz o sistema funcionar como um interruptor limpo é que *o mesmo hormônio empurra os dois neurônios em direções opostas*. A leptina inibe o NPY/AgRP e ativa o POMC; a soma dos dois efeitos aponta para o mesmo lado — comer menos. A grelina faz o oposto no primeiro neurônio. Um circuito com duas populações antagônicas e um sinal que age nas duas com sinais invertidos amplifica a decisão em vez de deixá-la ambígua, e é esse desenho que converte uma variação suave de concentração hormonal numa mudança nítida de comportamento.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-33-crop.png",
  largura: 78%,
  legenda: [As duas direções da mesma alça, para ler passo a passo. À direita (A), queda de massa gorda: menos leptina → menos ação hipotalâmica → NPY/AgRP ativado e POMC inibido → mais ingestão. À esquerda (B), aumento de massa gorda: mais leptina → NPY/AgRP inibido e POMC ativado → mais α-MSH → menos ingestão. Repare que cada braço tem duas colunas: a alça não depende de um único neurônio.])

#subtopico("3.2 — Segunda ordem: α-MSH, MC4R e onde a decisão vira comportamento")

Os neurônios do arqueado não comandam o comportamento diretamente; eles conversam com neurônios de segunda ordem em outros núcleos, e é nessa sinapse que o mecanismo fica interessante. O neurônio POMC não libera POMC — libera um fragmento clivado dessa proteína precursora, o #sigla("α-MSH", [hormônio estimulador de melanócitos alfa — fragmento da POMC que ativa o MC4R e produz saciedade]), o mesmo peptídeo que estimula melanócitos na pele. No núcleo paraventricular, o α-MSH encontra seu receptor, o #sigla("MC4R", [receptor de melanocortina tipo 4 — receptor hipotalâmico do α-MSH, ponto de convergência do sinal de saciedade]), e ativá-lo significa saciedade e aumento do gasto.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-34-crop.png",
  largura: 72%,
  legenda: [O detalhe da sinapse de segunda ordem. O neurônio verde (POMC/CART) libera α-MSH, que ativa o MC4R do neurônio vermelho; o neurônio amarelo (NPY/AgRP/GABA) libera AgRP no *mesmo* receptor, sem ativá-lo, e ainda inibe o neurônio POMC por GABA. Os pontos vermelhos marcam onde mutações humanas já foram descritas causando obesidade.])

Aqui está a peça que costuma ser lida ao contrário. O AgRP, produzido pelo neurônio da fome, também se liga ao MC4R — mas *não o ativa*. Ele é antagonista: ocupa o sítio e impede o α-MSH de agir. Isso significa que a fome comandada pelo AgRP não vem de acionar um "botão de comer", e sim de *bloquear o botão de parar*. O neurônio orexígeno faz ainda um segundo movimento no mesmo sentido, liberando #sigla("GABA", [ácido gama-aminobutírico — principal neurotransmissor inibitório do sistema nervoso central]) sobre o neurônio POMC vizinho e calando-o. E há um terceiro braço, na direção oposta do hipotálamo: o mesmo neurônio da fome estimula, na área hipotalâmica lateral, as células que produzem o #sigla("MCH", [hormônio concentrador de melanina — neuropeptídeo orexígeno da área hipotalâmica lateral]), que empurram ativamente para comer. Duas frentes, o mesmo resultado: com o MC4R silenciado, o comportamento default do organismo é comer.

#confusao-prevista(
  titulo: "AgRP não estimula o MC4R — ele o bloqueia",
  aluno_acha: [aluno acha que, se o AgRP dá fome e liga no MC4R, então ele ativa esse receptor],
  mecanismo: [AgRP é *antagonista* do MC4R. Ele ocupa o mesmo sítio do α-MSH e impede a ativação, sem produzir sinal próprio. O efeito orexígeno, portanto, é uma *desinibição*: sem MC4R ativo, a saciedade não se instala. A consequência prática confirma o mecanismo — perder o MC4R por mutação produz o mesmo fenótipo de excesso de AgRP, porque nos dois casos o receptor deixa de sinalizar.],
)

#clinica-box("Obesidade monogênica por mutação do MC4R", [Mutações com perda de função no MC4R são a causa monogênica mais comum de obesidade humana, respondendo por algo em torno de 2% a 5% dos casos de obesidade grave de início precoce. O quadro se instala nos primeiros anos, com hiperfagia intensa, crescimento linear acelerado e aumento de massa magra, e é herdado de modo geralmente codominante — quem tem um alelo alterado apresenta forma mais leve que quem tem dois. A leitura mecanística é direta: a leptina está alta, o arqueado a lê corretamente, o POMC dispara e o α-MSH é liberado — mas o receptor que deveria recebê-lo não funciona. Todo o sinal de saciedade construído nos subtópicos anteriores chega ao gargalo e para ali. Não adianta somar mais sinal a montante; por isso essas famílias não respondem a dieta convencional, e por isso o desenvolvimento de agonistas de melanocortina foi buscado justamente para esse grupo.])

#subtopico("3.3 — Sinais de curto prazo: o que o tubo digestivo informa a cada refeição")

A leptina responde a semanas de estoque, e sozinha ela não explicaria por que se para de comer no meio de um almoço. Esse controle de curto prazo vem do próprio tubo digestivo, que libera peptídeos conforme o alimento avança e informa o cérebro em tempo real sobre volume, composição e chegada de nutriente ao intestino. São dois relógios sobrepostos: um mede a reserva, o outro mede a refeição — e o hipotálamo integra os dois no mesmo circuito do arqueado.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-29-crop.png",
  largura: 88%,
  legenda: [À esquerda, a rota do sinal intestinal: nutriente no intestino → CCK e GLP-1 → cérebro (mais saciedade, menos ingestão) e pâncreas (mais secreção e mais síntese de insulina). À direita, a lista dos peptídeos que suprimem o apetite — e, isolada no fim, a única linha do outro lado: a grelina.])

Os principais peptídeos se distinguem por um traço definidor cada, o que os torna mais fáceis de fixar lado a lado do que em prosa corrida:

#table(
  columns: (auto, 1fr, 1fr),
  inset: 7pt,
  align: left,
  table.header([*Peptídeo*], [*Origem e gatilho*], [*Efeito característico*]),
  [Grelina], [Estômago vazio, antes da refeição], [Único orexígeno da lista: ativa o NPY/AgRP e dispara a fome],
  [#sigla("CCK", [colecistocinina — peptídeo duodenal de saciedade que também contrai a vesícula biliar])], [Duodeno, diante de gordura e proteína], [Saciedade na mesma refeição; contrai a vesícula e libera enzima pancreática],
  [#sigla("GLP-1", [peptídeo semelhante ao glucagon tipo 1 — incretina intestinal com ação pancreática, gástrica e central])], [Íleo e cólon, com chegada de nutriente], [Incretina: insulina dependente de glicose, menos glucagon, esvaziamento gástrico mais lento],
  [#sigla("PYY", [peptídeo YY — peptídeo intestinal que inibe o neurônio orexígeno e sustenta a saciedade])], [Íleo e cólon, após a refeição], [Inibe o NPY/AgRP e sustenta a saciedade por horas],
)

Dos quatro, o GLP-1 é o que mais rende, porque age em três lugares ao mesmo tempo. Ele é uma #termo-nota[incretina][hormônio intestinal que amplifica a secreção de insulina quando o nutriente chega pelo trato digestivo, e não pela veia], e o fenômeno que dá nome à classe é simples de reconhecer: uma carga de glicose tomada pela boca libera bem mais insulina do que a mesma carga infundida na veia. A diferença é o intestino avisando o pâncreas de que comida está a caminho, antes que a glicemia suba. Some a isso o retardo do esvaziamento gástrico, que prolonga a sensação de estômago cheio, e a ação direta no hipotálamo reduzindo a ingestão, e fica claro por que essa molécula virou alvo farmacológico — assunto do subtópico 3.5.

#subtopico("3.4 — Quando o estoque adoece: inflamação, lipotoxicidade e resistência à insulina")

Até aqui o tecido adiposo apareceu como um informante confiável. Quando o excedente calórico é crônico, ele deixa de ser. O adipócito responde ao excesso primeiro crescendo — hipertrofia —, e uma célula que cresce muito acaba se afastando do capilar que a nutre. O interior fica hipóxico, algumas células necrosam, e o tecido recruta macrófagos para limpar os restos. Instala-se então uma inflamação crônica de baixo grau: os macrófagos infiltrados assumem perfil pró-inflamatório e secretam #sigla("TNF-α", [fator de necrose tumoral alfa — citocina pró-inflamatória abundante no tecido adiposo obeso]) e #sigla("IL-6", [interleucina 6 — citocina pró-inflamatória liberada pelo tecido adiposo inflamado]), enquanto a produção de adiponectina despenca. *O tecido que deveria informar passa a agredir.*

#figura-nebli("/figuras/regulacao-massa-corporea/slide-17-crop.png",
  largura: 74%,
  legenda: [A cadeia que transforma excesso em doença: excesso de macronutriente → obesidade → hipertrofia, hipóxia, necrose e infiltração de macrófagos → estado pró-inflamatório com mais TNF-α e IL-6 e menos adiponectina → disfunção endotelial com menos óxido nítrico e mais espécies reativas. A coluna da esquerda lista o desfecho somado, que é a síndrome metabólica.])

O segundo braço do dano não passa pela inflamação, e sim pelo próprio combustível. Com o tecido adiposo saturado, o ácido graxo sobra e é entregue a tecidos que não foram feitos para estocá-lo — músculo e fígado. Dentro dessas células, o excesso de acil-CoA é desviado para diacilglicerol e ceramida, e essas duas moléculas ativam serina-quinases de estresse. Aqui está o nó do mecanismo: essas quinases fosforilam o substrato do receptor de insulina em resíduos de *serina*, e não nas tirosinas que a via correta usa. A fosforilação errada inativa a proteína. A insulina continua ligando no receptor, o receptor continua se autofosforilando, mas o sinal morre no primeiro passo intracelular — e o transportador #sigla("GLUT4", [transportador de glicose sensível à insulina, presente em músculo e tecido adiposo]) não é levado à membrana.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-18-crop.png",
  largura: 62%,
  legenda: [A lipotoxicidade em detalhe. Excesso de ácido graxo → acil-CoA → diacilglicerol e ceramida → serina-quinases de estresse, que bloqueiam o receptor de insulina e a translocação do GLUT4. Dentro da mitocôndria, o mesmo excesso força β-oxidação e ciclo de Krebs além da capacidade, gerando sobrecarga, espécies reativas e queda de CoA livre.])

#atencao-box("Resistência à insulina não é falta de insulina", [Trocar as duas coisas inverte o raciocínio inteiro e, na clínica, inverte a conduta. Na resistência associada à obesidade, *a insulina está alta*: a célula beta compensa o sinal ineficaz secretando mais, e a hiperinsulinemia é o achado precoce, muito antes de qualquer alteração de glicemia. O que falhou foi a transdução dentro da célula-alvo — GLUT4 não chega à membrana, o músculo não capta glicose, e o fígado, que deveria parar de produzir glicose, continua produzindo. A glicemia só sobe quando a célula beta se esgota depois de anos de sobrecarga; aí sim há falta relativa de insulina, e o quadro se instala. Guardar a ordem dos eventos — resistência primeiro, hiperinsulinemia compensatória depois, falência da célula beta por último — é o que permite entender por que o mesmo paciente passa de glicemia normal a diabetes sem que nada de novo tenha começado.])

O mesmo excesso de ácido graxo que trava a sinalização no músculo é reesterificado no fígado e produz #termo-nota[esteatose hepática][acúmulo de triacilglicerol dentro do hepatócito, sem relação obrigatória com álcool], e as três alterações que sobram — glicemia elevada, dislipidemia e hipertensão — compõem, com a obesidade central, o conjunto que se chama síndrome metabólica. Nada disso é uma lista de doenças independentes que acompanham a obesidade: é a mesma cadeia mecanística vista em órgãos diferentes.

#subtopico("3.5 — Do circuito ao remédio: optogenética e os agonistas de GLP-1")

Uma objeção legítima acompanha todo o circuito montado até aqui: como se demonstra que um neurônio *causa* fome, e não apenas que ele está ativo quando o animal tem fome. Correlação de atividade não fecha o argumento. A ferramenta que fechou chama-se #termo-nota[optogenética][técnica em que um canal iônico sensível à luz é expresso em um tipo neuronal específico, permitindo ligá-lo ou desligá-lo com um pulso de luz]: pega-se o gene de uma proteína de alga que funciona como canal iônico ativado por luz, coloca-se esse gene sob controle de um promotor que só funciona no neurônio de interesse, e implanta-se uma fibra óptica. A partir daí, um pulso de luz azul liga aquele grupo de neurônios — e apenas ele — em milissegundos.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-35-crop.png",
  largura: 54%,
  legenda: [O princípio da optogenética: o gene do canal sensível à luz vem de uma alga, é inserido apenas nos neurônios escolhidos, e a partir daí um flash de luz azul dispara aquele grupo específico. É intervenção, não observação — e é isso que permite afirmar causalidade.])

Aplicada ao circuito do apetite, a técnica produziu demonstrações que nenhuma correlação daria. Estimular os terminais que descem de um núcleo hipotalâmico dorsomedial sobre os neurônios AgRP *silencia* esses neurônios, e um animal faminto interrompe a alimentação em segundos; retirada a luz, ele volta a comer imediatamente. O experimento estabelece as duas metades do argumento causal: ligar o circuito produz o comportamento, desligá-lo o remove.

Do lado terapêutico, o alvo que se mostrou mais produtivo não foi a leptina nem o MC4R, mas o GLP-1 do subtópico 3.3. O peptídeo natural é degradado em poucos minutos por uma peptidase plasmática; os fármacos da classe são análogos modificados que resistem a essa degradação e permanecem ativos por horas ou dias.

#figura-nebli("/figuras/regulacao-massa-corporea/slide-38-crop.png",
  largura: 58%,
  legenda: [As frentes de ação dos análogos de GLP-1: no cérebro, menos apetite e mais saciedade; no estômago, esvaziamento mais lento; no pâncreas, mais insulina e menos glucagon; no músculo e no fígado, melhor sensibilidade à insulina e menos produção hepática de glicose.])

#clinica-box("Por que um análogo de GLP-1 reduz peso e glicemia ao mesmo tempo", [O fármaco reproduz, de forma sustentada, o sinal que o intestino manda por minutos. No pâncreas, amplifica a secreção de insulina *dependente de glicose* — só age quando há glicose alta, o que explica o baixo risco de hipoglicemia — e reduz o glucagon, cortando a produção hepática de glicose. No estômago, retarda o esvaziamento, e o alimento permanece distendendo a parede por mais tempo. No hipotálamo, reduz a ingestão pela mesma via de segunda ordem já descrita. Os três efeitos convergem: menos comida entrando, menos glicose sendo produzida e mais glicose sendo captada. O ponto que fecha o raciocínio da apostila inteira é o que acontece na suspensão — como o valor de massa gorda defendido pelo eixo leptina-melanocortina não foi reprogramado, o peso tende a voltar, e é por isso que o tratamento é pensado como contínuo, e não como um curso com data para terminar.])

#conclusao-box[
  Um único princípio atravessa as três PARTES: *massa corpórea é uma variável controlada por retroalimentação negativa*, não o saldo passivo de uma conta. A PARTE I montou a lógica do controle — uma cascata hormonal que amplifica sinais minúsculos e um freio que volta e desliga os degraus acima —, e mostrou que o gasto energético é tão regulável quanto a ingestão. A PARTE II identificou o sensor: o tecido adiposo secreta leptina em proporção ao próprio tamanho, e a parabiose de Coleman separou, duas décadas antes da genética molecular, o defeito de ligante do defeito de receptor. A PARTE III mostrou onde o sinal é lido e como vira comportamento — leptina inibindo o NPY/AgRP e ativando o POMC, α-MSH ativando o MC4R, AgRP bloqueando o mesmo receptor — e como os peptídeos do tubo digestivo encaixam o controle de cada refeição dentro do controle de longo prazo.

  O mecanismo nuclear, se for para guardar um só, é a dupla saída da leitura hipotalâmica: *o mesmo sinal reduz a entrada e aumenta a saída*. Reduz a entrada pelo eixo arqueado → paraventricular; aumenta a saída pelo simpático → β#sub[3] → AMPc → PKA → lipólise e UCP1. Perder qualquer um dos dois braços produz obesidade, e por isso o camundongo sem leptina não apenas come demais: ele também sente frio.

  Na clínica, esse arranjo explica três fatos que pareceriam desconexos. Repor leptina não emagrece a maioria dos obesos porque neles a leptina já está alta e o que falhou foi a leitura — hormônio alto com efeito ausente aponta receptor, nunca produção. Mutação de MC4R causa obesidade grave porque interrompe o gargalo por onde todo o sinal de saciedade passa. E a síndrome metabólica não é um agregado de doenças: é a mesma cadeia de excesso de ácido graxo ativando serina-quinases, travando o substrato do receptor de insulina e impedindo o GLUT4 de chegar à membrana, vista sucessivamente no músculo, no fígado e na parede do vaso.

  O caminho adiante segue por essa mesma alça. Quando entrarmos na fisiologia da digestão e da absorção, os peptídeos que aqui apareceram como sinais de saciedade — CCK, GLP-1, grelina — reaparecerão comandando secreção enzimática, motilidade e esvaziamento gástrico; e o fígado, que aqui recebeu o excesso de ácido graxo e virou esteatótico, será o órgão central da integração metabólica. O que muda é o ponto de vista, não o mecanismo.
]
