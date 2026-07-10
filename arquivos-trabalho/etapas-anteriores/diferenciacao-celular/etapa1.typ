#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Você começou como uma única célula — o zigoto, fruto do encontro entre o óvulo da sua mãe e o espermatozoide do seu pai. Nove meses depois, essa célula virou *você*: cerca de trinta trilhões de células, organizadas em fígado, cérebro, sangue, pele, intestino, músculo. Todas elas carregam o *mesmo* #sigla("DNA", [ácido desoxirribonucleico — molécula que guarda a informação genética da célula]), com os mesmos vinte mil genes. E mesmo assim, um neurônio do seu córtex não se parece em nada com uma hemácia do seu sangue ou com uma célula-beta do seu pâncreas.

A pergunta que organiza este resumo inteiro é essa: *como células com instruções idênticas viram coisas tão diferentes — e como cada uma "se lembra" do que é, divisão após divisão, pelos próximos oitenta anos?*

A resposta tem três ângulos, e cada PARTE pega um:

Na PARTE I você vai entender *o que é diferenciação*: o caminho do zigoto até as três camadas de células do embrião (os folhetos), e por que quanto mais a célula se especializa, menos opções de virar outra coisa ela conserva.

Na PARTE II a gente conhece a *célula-tronco* — a peça que mantém flexibilidade no meio de um corpo já especializado. Você vai ver as três classes (totipotente, pluripotente, multipotente), o conceito de nicho e como o sangue novo é fabricado todos os dias na sua medula óssea.

Na PARTE III entra o *mecanismo molecular*: como combinações de poucos reguladores transcricionais geram centenas de destinos diferentes, e como a *memória epigenética* (metilação de #sigla("CpG", [dinucleotídeo citosina-fosfato-guanina — sítio preferencial de metilação no DNA de mamíferos]), histonas, RNAs não codificantes) trava o destino sem precisar mexer no DNA. No fim, a reviravolta: Yamanaka mostrou que esse trava se *desfaz* — quatro fatores reprogramam um fibroblasto adulto numa célula com pluripotência praticamente embrionária. É o nascimento da medicina regenerativa.
]


#parte-title("PARTE I — O que é diferenciação celular", primeira: true)

#subtopico("1.1 — Especialização: a célula que faz uma coisa muito bem")

A pergunta certa aqui não é "o que uma célula faz" — é *por que faz só uma coisa, e por que faz tão bem*. Uma célula muscular lisa consegue contrair com uma eficiência mecânica difícil de imitar; uma hemácia carrega oxigênio com uma capacidade que nenhum outro tipo celular se aproxima; um neurônio do córtex propaga sinal elétrico por mais de um metro de distância. Em cada caso, a célula abandonou a versatilidade em troca de *eficiência em uma única função*.

Esse é o significado operacional de #termo-nota[diferenciação celular][processo pelo qual uma célula adquire fenótipo e função especializada por meio de expressão gênica diferencial; geralmente estável, mas não absolutamente irreversível]: o processo pelo qual a célula vai se comprometendo com um perfil cada vez mais estreito de função, à custa da capacidade de fazer outras coisas. Não é que a célula diferenciada *perca* genes — ela continua com o genoma completo. O que muda é *quais* genes ela liga e quais ela mantém silenciados. Um hepatócito tem o gene da hemoglobina; ele só não transcreve nem traduz esse gene. A hemácia tem o gene da albumina; nunca o expressa.

#figura-nebli("/figuras/diferenciacao-celular/slide-04.png",
  largura: 75%,
  legenda: [Uma amostra do destino possível: oócito, espermatozoide, neurônio do encéfalo, hemácia, célula muscular lisa, célula óssea, célula adiposa, célula do epitélio intestinal. Todas vieram da mesma célula-zigoto, todas carregam o mesmo DNA. A diferença entre elas está em *qual subconjunto de genes está ativo*.])

#mini-resumo[Em uma frase: diferenciação é a célula trocando versatilidade por eficiência funcional — mesmos genes, leituras diferentes.]

#subtopico("1.2 — Do zigoto aos folhetos: o caminho da especialização")

Lembre que tudo começa com a fusão de um espermatozoide e um óvulo, formando o zigoto. Essa célula é, em termos de potencial, a campeã absoluta: ela vai virar o corpo inteiro e ainda os anexos embrionários (placenta, saco amniótico) que sustentam a gestação. Os primeiros dias são de divisão celular pura — sem grande diferenciação. A célula se parte em duas, depois em quatro, oito, dezesseis, formando a *mórula*, uma bolinha compacta.

Por volta do quinto ou sexto dia, a mórula vira *blastocisto*: um aglomerado oco em que aparece a primeira diferenciação reconhecível. As células externas formam o *trofoblasto* (que vai dar origem à placenta) e as internas formam a *massa celular interna* (que vai dar origem ao embrião propriamente). É da massa celular interna que se extraem as células-tronco embrionárias humanas (#sigla("ES", [embryonic stem — célula-tronco extraída da massa celular interna do blastocisto, com pluripotência])) que apareceram em todas as discussões de bioética da década de 90.

#figura-nebli("/figuras/diferenciacao-celular/slide-03.png",
  largura: 80%,
  legenda: [O caminho do zigoto até os tecidos: fertilização → clivagem (divisões celulares) → blastocisto (dia 6) → diferenciação do trofoblasto e da massa celular interna → formação das três camadas germinativas (dia 14). Cada folheto vai gerar conjuntos previsíveis de tecidos.])

Lá por volta da segunda semana, vem o passo crítico: a *gastrulação*. A massa celular interna se reorganiza em três camadas distintas — os três #termo-nota[folhetos embrionários][as três camadas de células formadas na gastrulação (ectoderma, mesoderma, endoderma); cada folheto origina conjuntos previsíveis de tecidos no organismo adulto]:

O *ectoderma* (camada externa) vira a pele, o cabelo, e — talvez surpreendentemente — todo o sistema nervoso (cérebro, medula, nervos periféricos, retina). O *mesoderma* (camada do meio) vira músculo esquelético, músculo cardíaco, ossos, sangue, vasos, rim. O *endoderma* (camada interna) vira o revestimento do tubo digestivo, fígado, pâncreas, pulmão. Em paralelo, um pequeno grupo de células se separa dos três folhetos no início do desenvolvimento e vira a *linhagem germinativa* — os precursores dos futuros oócitos e espermatozoides.

#atencao-box("Multipotente não é pluripotente", [O leitor costuma derrapar aqui com uma identificação solta entre os termos. Quem origina os *três* folhetos embrionários (ecto, meso, endoderma) são as células *pluripotentes* — massa celular interna do blastocisto, células-ES, células iPS em cultura. Uma célula *multipotente* já está dentro de uma linhagem só: a #sigla("HSC", [hematopoietic stem cell — célula-tronco hematopoiética, multipotente para a linhagem do sangue]) da medula gera todos os tipos de células do sangue, mas não gera neurônio nem hepatócito. A célula-tronco mesenquimal gera osso, cartilagem, adipócito, músculo — toda linhagem mesodermal, mas não atravessa folheto. Memorize essa fronteira: *três folhetos é pluripotente; um folheto/linhagem é multipotente*.])


#subtopico("1.3 — A escala invertida: potencialidade × diferenciação")

Agora vem a relação mais importante do tema, e a que mais escorrega na primeira leitura. Conforme a célula caminha do zigoto até virar uma hemácia madura, *duas grandezas se movem em direções opostas*:

A *potencialidade* — o número de tipos diferentes que aquela célula consegue gerar como descendência — vai *caindo*. O zigoto pode virar qualquer coisa; uma célula da massa celular interna pode virar tudo do embrião (mas não a placenta); uma HSC já só pode virar células do sangue; uma hemácia já não pode virar absolutamente nada.

A *diferenciação* — o grau de especialização funcional — vai *subindo*. O zigoto é uma célula relativamente genérica; a hemácia é tão especializada que perdeu o núcleo para abrir espaço para mais hemoglobina.

#figura-nebli("/figuras/diferenciacao-celular/slide-08.png",
  largura: 85%,
  legenda: [A escala canônica. Da esquerda para a direita: zigoto, blástula, gástrula, células comprometidas com cada folheto, células terminalmente diferenciadas. A barra de baixo mostra os dois eixos inversos: *potencialidade decresce, diferenciação cresce*. Guarde essa imagem — ela vai reaparecer várias vezes.])

#atencao-box("A inversão que parece trivial mas confunde", [A intuição inicial é tratar "potencialidade" e "diferenciação" como se andassem juntas — como se uma célula "mais diferenciada" tivesse "mais capacidade". Esse é o erro central. Pense pelo lado funcional: o hepatócito é altamente diferenciado *porque* dedicou seu maquinário inteiro à função hepática, abrindo mão de qualquer outra. Ele *não* consegue virar um neurônio. A célula-tronco da medula, ao contrário, ainda é relativamente indiferenciada — por isso *consegue* virar várias coisas. Quanto mais especializado o currículo, menos opção de carreira sobra.])

#mini-resumo[Se você só lembrar de uma coisa: *quanto mais diferenciada, MENOS potencial*. Eixos inversos. Sempre.]

#subtopico("1.4 — Sinais que toda célula animal precisa")

Antes de fechar a PARTE I, uma peça que vai voltar várias vezes daqui pra frente. Para *qualquer* célula animal sobreviver e se dividir, ela precisa receber três classes distintas de sinais do ambiente extracelular. Não basta ter nutriente — célula animal não é planta nem bactéria, ela precisa de instrução química explícita para crescer, dividir, ou simplesmente continuar viva.

O *mitógeno* é o sinal que diz "pode dividir". Funciona liberando os freios do ciclo celular (que você já deve ter encontrado em Divisão Celular). Sem mitógeno, a célula entra em quiescência (G0) e fica parada. Exemplos: fatores de crescimento epidermal (#sigla("EGF", [epidermal growth factor — mitógeno clássico para epitélio e fibroblasto])) na pele, fatores plaquetários na cicatrização.

O *fator de crescimento*, num sentido mais estreito, é o sinal que diz "fica maior" — aumenta a síntese de proteína e bloqueia a degradação. A célula ganha massa. Sem ele, dividir-se geraria células cada vez menores até o ridículo.

O *fator de sobrevivência* é o sinal que diz "não morra". Sem ele, a célula entra em #termo-nota[apoptose][morte celular programada, executada por uma cascata de caspases; processo limpo, sem inflamação, que remove células supérfluas ou danificadas]. Esse mecanismo é a base do "uso ou perde" do desenvolvimento: neurônios que não conseguem fazer sinapse com um alvo morrem por falta de fator de sobrevivência. O sistema nervoso central produz quase o dobro de neurônios que vai precisar — metade morre por não receber sinal de sobrevivência do alvo.

Esses três sinais podem ser combinados livremente: a mesma molécula pode ser mitógeno num contexto e fator de sobrevivência em outro. O que importa é que *toda* divisão e *toda* sobrevida celular dependem desse cardápio mínimo de sinais — e na PARTE III a gente vai ver que os sinais que comandam *diferenciação* (os *morfógenos*) são uma quarta categoria, com lógica própria.


#parte-title("PARTE II — Célula-tronco: a peça que mantém flexibilidade", primeira: false)

#subtopico("2.1 — Duas propriedades que definem uma célula-tronco")

Para entender o que a célula-tronco *é*, comece pelo problema que ela resolve. A epiderme da sua pele se renova mais ou menos a cada quatro semanas; o epitélio do seu intestino, a cada cinco dias; suas hemácias, a cada quatro meses. Esse turnover constante exige uma fonte de células novas que (a) consiga produzir células do tipo certo (queratinócito, enterócito, hemácia) e (b) *não se esgote no processo*. Se a fonte fosse uma célula comum que se dividisse e fosse virando as filhas, em duas semanas ela acabaria.

A solução evolutiva é a #termo-nota[célula-tronco][célula com capacidade de auto-renovação (manter o pool após divisão) combinada com potencial de gerar pelo menos um tipo celular diferenciado]: uma célula com duas propriedades inseparáveis. Primeiro, *auto-renovação* — quando ela se divide, pelo menos uma das filhas continua sendo célula-tronco, mantendo o pool. Segundo, *capacidade de gerar células diferenciadas* — a outra filha (ou a própria filha, em outra divisão) pode seguir o caminho da especialização.

#figura-nebli("/figuras/diferenciacao-celular/slide-19.png",
  largura: 55%,
  legenda: [O modelo canônico. A célula-tronco se divide; uma filha mantém o estado de tronco (volta para o pool por *auto-renovação*) e a outra inicia o caminho de *diferenciação* até virar uma célula terminalmente diferenciada. As duas propriedades juntas é o que define o conceito.])

Note que nenhuma das duas propriedades sozinha define célula-tronco. Uma célula em câncer pode se auto-renovar indefinidamente, mas não diferencia — e não é célula-tronco verdadeira. Uma célula progenitora comprometida pode diferenciar em vários tipos, mas não se auto-renova — e não é célula-tronco em sentido estrito.

#subtopico("2.2 — Três classes hierárquicas de potencialidade")

O conceito de potencialidade que apareceu na PARTE I se aplica também ao mundo das células-tronco. As três classes formam uma hierarquia clara, com regras de "o que vira o quê":

A célula *totipotente* é o topo absoluto. Inclui o zigoto e os blastômeros das primeiras divisões (até cerca de oito células). Pode gerar o embrião inteiro *mais* os anexos extraembrionários (placenta, saco vitelínico). É a única classe com essa amplitude — depois que o blastocisto se forma, o trofoblasto e a massa celular interna já estão comprometidos com destinos diferentes, e nenhum dos dois sozinho gera o organismo completo.

#figura-nebli("/figuras/diferenciacao-celular/slide-13.png",
  largura: 70%,
  legenda: [Célula totipotente — zigoto e mórula até oito células. Origem do embrião inteiro mais os anexos (placenta, saco vitelínico). A potencialidade máxima da escala.])

A célula *pluripotente* vem em seguida. É a célula que pode gerar todos os tipos celulares dos *três folhetos* embrionários — ou seja, qualquer tipo de tecido somático. Não gera, em condições normais, anexos placentários. As mais conhecidas são as células-ES (extraídas da massa celular interna do blastocisto) e as células #sigla("iPS", [induced pluripotent stem — célula-tronco pluripotente induzida; obtida por reprogramação de uma célula somática adulta com os quatro fatores de Yamanaka]) — que a gente vai conhecer no fim da PARTE III.

#figura-nebli("/figuras/diferenciacao-celular/slide-14.png",
  largura: 70%,
  legenda: [Célula pluripotente — massa celular interna, ES, iPS. Gera células dos três folhetos embrionários (todos os tipos somáticos), mas não gera anexos.])

A célula *multipotente* é o nível mais restrito do trio. Só gera células de *uma linhagem* — não atravessa folheto. A HSC da medula gera todas as células do sangue (eritrócito, leucócito, plaqueta) mas não vira músculo, neurônio ou hepatócito. A célula-tronco mesenquimal gera tecidos mesodermais (osso, cartilagem, adipócito, músculo) mas não vira epitélio nem neurônio. As multipotentes são as células-tronco *adultas*, *teciduais* — as que ficam no seu corpo a vida inteira mantendo o turnover.

#figura-nebli("/figuras/diferenciacao-celular/slide-15.png",
  largura: 70%,
  legenda: [Célula multipotente — adulta, tecidual. Cada uma serve a uma linhagem só: a hematopoiética repõe o sangue; uma neural repõe neurônios e glia; uma da medula óssea reconstrói tecido conjuntivo. Potencialidade restrita, mas suficiente para manter o tecido onde mora.])

#mini-resumo[O que ficou de pé: *toti* gera embrião + anexos; *pluri* gera os 3 folhetos; *multi* gera só uma linhagem. Lugar de cada uma no corpo: toti = zigoto e mórula muito precoce; pluri = blastocisto e iPS em cultura; multi = medula, intestino, pele, músculo no adulto.]


#subtopico("2.3 — Divisão assimétrica: como uma só vira duas com destinos diferentes")

A célula-tronco precisa, divisão após divisão, gerar uma filha que seja *cópia dela mesma* e outra filha que *siga adiante na diferenciação*. Como uma única mitose produz duas filhas com destinos tão diferentes? A natureza tem duas soluções, e as duas operam no seu corpo agora mesmo.

A primeira é a *assimetria divisional* (intrínseca). Aqui, a própria célula-mãe distribui *o seu conteúdo citoplasmático de forma desigual* entre as duas filhas. Determinantes celulares — proteínas reguladoras como Numb, mRNAs localizados em uma extremidade da célula, organelas com distribuição polarizada — vão preferencialmente para uma das filhas. Quando a divisão acontece, aquela filha que herdou mais Numb (ou mais do mRNA decisivo) vai por um destino; a outra, com menos, vai por outro. A informação que decide o destino *está dentro da célula-mãe antes da divisão*, ela só é repartida desigualmente.

A segunda é a *assimetria ambiental* (extrínseca). Aqui, a divisão começa simétrica: as duas filhas saem idênticas. Mas o *espaço físico* em que elas pousam é diferente. Uma fica em contato com o #termo-nota[nicho][microambiente especializado que mantém a célula-tronco indiferenciada por sinais de contato direto e fatores secretados; saída do nicho dispara diferenciação]; a outra é empurrada para fora. A filha que ficou no nicho recebe os sinais de manutenção (Wnt, contato com osteoblasto, contato com matriz específica) e continua tronco. A filha que saiu perde esses sinais e começa a diferenciar.

#figura-nebli("/figuras/diferenciacao-celular/slide-38.png",
  largura: 90%,
  legenda: [Três cenários de divisão da célula-tronco. À esquerda, o modelo de auto-renovação simples (estêncil). No centro, *assimetria ambiental*: as duas filhas são idênticas mas só uma fica no nicho (laranja); a outra vai para fora (verde) e diferencia. À direita, *assimetria divisional*: a marca vermelha (determinantes citoplasmáticos) é herdada por uma só filha, definindo destino antes mesmo da separação física.])

#atencao-box("Assimetria não é só o nicho", [Uma leitura apressada da literatura conclui que toda divisão assimétrica acontece por causa do ambiente — afinal, o conceito de nicho é elegante e fácil de visualizar. Mas a *assimetria divisional* (intrínseca) é tão importante quanto. Em alguns sistemas (neuroblastos de Drosophila, divisão da célula-mãe de hemácia em alguns modelos) é o mecanismo principal. Os dois coexistem; em muitos tecidos, operam em paralelo. O ponto editorial: divisão assimétrica é um *fenômeno*, não uma única implementação molecular.])

#subtopico("2.4 — Renovação tecidual no adulto: tronco → progenitor → célula madura")

Você não tem só células-tronco e células diferenciadas no seu corpo adulto. Existe uma classe intermediária crítica para entender o turnover real dos tecidos: as células #termo-nota[transit-amplifying][célula progenitora comprometida que se divide rapidamente várias vezes para amplificar o número de células antes da diferenciação terminal; multipotência restrita, sem auto-renovação indefinida].

A célula-tronco verdadeira é *rara* (1 em 10.000 a 1 em 100.000 numa medula óssea), se divide *raramente* (entrando em ciclo só esporadicamente) e tem potencialidade alta. Quando ela se divide, uma das filhas vai para o pool das células transit-amplifying — que se dividem *rápido*, várias vezes seguidas, expandindo numericamente. Cada divisão dessas filhas já gera células um pouco mais comprometidas. Depois de algumas rodadas, as descendentes saem do ciclo celular e fazem a diferenciação terminal — viram a célula funcional que o tecido precisa.

#figura-nebli("/figuras/diferenciacao-celular/slide-45.png",
  largura: 85%,
  legenda: [A cadeia da renovação tecidual: *célula-tronco* (rara, autorrenova, raramente se divide) → *progenitores transit-amplifying* (multipotentes restritas, dividem-se rápido) → *células especializadas* (trabalham na função, não dividem mais). Em qualquer tecido com turnover (sangue, intestino, pele) você encontra essa arquitetura.])

#figura-nebli("/figuras/diferenciacao-celular/slide-46.png",
  largura: 70%,
  legenda: [Exemplo clássico: a epiderme. A camada basal contém células-tronco (raras) e progenitores transit-amplifying (mais numerosos). À medida que sobem, as células param de se dividir, queratinizam, e descamam na superfície. O ciclo completo leva cerca de quatro semanas.])

E o sangue? A medula óssea tem uma HSC (rara, quiescente) que gera dois progenitores comuns — *linfoide* e *mieloide*. O progenitor linfoide gera células T, células B, células NK; o mieloide gera neutrófilo, eosinófilo, basófilo, monócito (macrófago/osteoclasto/célula dendrítica), megacariócito (plaqueta) e eritrócito (hemácia). Esse esquema vai aparecer em Hematopoese com muito mais detalhe — guarde só a arquitetura geral.

#figura-nebli("/figuras/diferenciacao-celular/slide-49.png",
  largura: 80%,
  legenda: [Hematopoese — a HSC multipotente gera dois progenitores comprometidos (linfoide e mieloide), cada um com seu próprio leque de descendentes. Toda a hierarquia da renovação do sangue cabe nessa árvore.])

#atencao-box("Nicho vascular não é nicho endosteal", [Dentro da medula óssea, existe um detalhe que confunde quem está vendo o assunto pela primeira vez: há *dois* nichos com funções distintas. O *nicho endosteal* (em contato com o osso, via osteoblastos) mantém a HSC quiescente, indiferenciada. É onde ela "vive" no estado de tronco. O *nicho vascular* (em contato com os sinusoides) é onde acontece a *liberação* das células sanguíneas maduras para a circulação. Em outras palavras: o endosteal *guarda*, o vascular *libera*. Tratar os dois como sinônimos joga fora uma distinção que vai ser cobrada em hematologia.])


#parte-title("PARTE III — Como o destino é controlado", primeira: false)

#subtopico("3.1 — Mesmos genes, leituras diferentes")

A pergunta que abriu o resumo — *como células com instruções idênticas viram coisas tão diferentes?* — é exatamente a pergunta desta PARTE. A premissa que precisa estar fixa: o DNA é o mesmo. Não há perda de gene durante a diferenciação somática (com exceções específicas como o rearranjo dos genes de imunoglobulina nos linfócitos B/T, que é caso à parte). Um neurônio tem o gene da insulina; ele só não o expressa. Uma célula-beta do pâncreas tem o gene da actina cardíaca; nunca o transcreve.

A diferença, então, está no padrão de *expressão gênica*. Cada tipo celular tem um subconjunto característico de genes ativos, e a *estabilidade desse padrão* — ele continua o mesmo divisão após divisão, ano após ano — é o que precisa ser explicado. A explicação tem duas camadas. A primeira é *quem decide* qual gene liga em cada tipo: as combinações de reguladores transcricionais. A segunda é *como a decisão se mantém*: a memória epigenética. Os dois operam juntos.

#subtopico("3.2 — Controle combinatorial: poucos reguladores, muitos destinos")

Comece pelo problema combinatório. O corpo humano tem em torno de duzentos tipos celulares histologicamente reconhecíveis. Se cada tipo precisasse de uma proteína mestre exclusiva para defini-lo, o genoma teria que dedicar duzentos genes só para essa função — e a evolução teria gerado um sistema rígido, difícil de modificar.

A solução real é *combinatória*. Combinações de poucos reguladores transcricionais geram um número grande de destinos. Com três reguladores binários (presente/ausente), você tem oito combinações possíveis; com cinco, trinta e duas; com dez, mais de mil. O número de tipos celulares cabe com folga nesse esquema.

#figura-nebli("/figuras/diferenciacao-celular/slide-42.png",
  largura: 85%,
  legenda: [Combinatorial control. A célula precursora se divide e, dependendo de qual proteína regulatória apareceu em cada filha (1, 2, 3 ou alguma combinação delas), ela termina como Célula A, B, C... até H. Apenas três proteínas regulatórias geram oito identidades distintas. É essa lógica que permite ao genoma humano construir centenas de tipos celulares sem precisar de uma proteína mestre por tipo.])

A consequência prática é grande: para *reprogramar* uma célula, você não precisa mexer em mil genes. Basta acertar nos poucos reguladores combinatórios certos — e foi exatamente o que Yamanaka fez em 2006, como você vai ver no fim da PARTE.

#subtopico("3.3 — Herança epigenética: a célula-filha lembra o que a célula-mãe era")

Agora o passo seguinte. Suponha que durante o desenvolvimento, um conjunto de reguladores transcricionais foi ativado num precursor de hepatócito, e o gene da albumina ficou ligado. Essa célula se divide. As filhas também são hepatócitos, e também expressam albumina. *Sem* que ninguém precise ativar os reguladores transcricionais de novo. Como isso é possível?

A resposta é a #termo-nota[herança epigenética][transmissão fiel do padrão de expressão gênica às células-filhas sem alterar a sequência de DNA; opera por modificação da cromatina e por alças autossustentáveis]: a habilidade de uma célula-filha de manter uma memória do padrão de expressão da célula-mãe, *sem que a sequência de DNA mude*. Releia essa frase. A definição da herança epigenética é exatamente o *oposto* da herança genética. Genética = sequência muda → padrão herdado. Epigenética = sequência *NÃO* muda → padrão herdado por outro mecanismo.

#figura-nebli("/figuras/diferenciacao-celular/slide-22.png",
  largura: 85%,
  legenda: [Contraste limpo entre os dois modos. À esquerda (herança genética): o gene X é desligado por *mudança na sequência* do DNA (uma mutação); as filhas herdam essa sequência alterada e o gene continua off. À direita (herança epigenética): o gene Y é desligado por *mudança na cromatina* (sem alterar a sequência); as filhas herdam essa cromatina e o gene continua off. Resultado funcional parecido, mecanismos completamente diferentes.])

#atencao-box("Epigenética NÃO é mudança de DNA", [Esse é provavelmente o ponto mais sensível do tema todo. A palavra "epi" significa "acima" — o que está *acima* do gene, não *dentro* dele. Se uma "herança epigenética" envolvesse mudança de sequência, ela seria, por definição, herança genética. Toda vez que você ler ou ouvir uma descrição que coloca metilação ou marca de histona como "modificação do DNA" no mesmo nível de uma mutação, pare e desmonte: a base nitrogenada continua sendo a mesma; o que mudou foi um grupo químico *adicionado* à base (no caso da metilação de citosina) ou um *grupo adicionado a uma proteína associada* (no caso das modificações de histona). A sequência permanece intacta.])


#subtopico("3.4 — Os quatro mecanismos de herança epigenética")

A natureza tem (pelo menos) quatro mecanismos distintos para manter um padrão de expressão estável ao longo das divisões. Eles aparecem nas mesmas figuras dos slides da Profa. Ortis e cada um vale uma olhada cuidadosa.

#figura-nebli("/figuras/diferenciacao-celular/slide-24.png",
  largura: 90%,
  legenda: [Os quatro mecanismos canônicos: (A) circuito de retroalimentação positiva — a proteína A é necessária para sua própria transcrição; (B) modificação de histonas — marcas nas caudas histônicas mudam a estrutura da cromatina; (C) metilação de DNA — citosinas em CpG metiladas silenciam transcrição; (D) estado de agregação proteica — versão "exótica" (príons), menos relevante para nós.])

O *primeiro* mecanismo é a alça de retroalimentação positiva. Imagine um gene que codifica a proteína A, e suponha que A se ligue ao próprio promotor de A e ative sua transcrição. Em estado de repouso, A não existe, A não é produzida, e o gene fica silenciado. Mas se *um sinal externo qualquer* (um morfógeno passageiro, um pulso de hormônio) ativar o gene de A por um instante — A começa a ser produzida, A se liga ao próprio promotor, A se mantém produzida sozinha. O sinal externo passou; A se sustenta. As células-filhas, ao herdar pelo menos uma molécula de A no citoplasma, recriam o estado autossustentado. *Memória sem mexer no DNA.*

#figura-nebli("/figuras/diferenciacao-celular/slide-25.png",
  largura: 85%,
  legenda: [Como a retroalimentação positiva gera memória. Estado inicial: gene A silenciado, A ausente. Um sinal externo transitório ativa a transcrição de A. Daí em diante, A se liga ao próprio promotor e mantém sua produção. As filhas herdam algumas moléculas de A no citoplasma e recriam o estado. O sinal pode ter desaparecido há gerações — a memória sobrevive.])

O *segundo* mecanismo é a modificação de histonas. As histonas são as proteínas em torno das quais o DNA se enrola para formar a cromatina. Modificações químicas nas caudas dessas histonas (acetilação, metilação, fosforilação) alteram a maneira como o DNA fica embalado. Cromatina relaxada e aberta é *eucromatina* — transcricionalmente ativa, acessível à RNA polimerase. Cromatina condensada e densa é #termo-nota[heterocromatina][cromatina altamente condensada, transcricionalmente silenciada; aparece nas regiões pericentroméricas e teloméricas constitutivamente e em regiões reguladas durante a diferenciação] — silenciada, escondida da maquinaria de transcrição.

#figura-nebli("/figuras/diferenciacao-celular/slide-27.png",
  largura: 85%,
  legenda: [Cromatina em duas configurações. Em cima: alternância de eucromatina (aberta, ativa) e heterocromatina (condensada, silenciada) ao longo do mesmo cromossomo. Embaixo: como a herança funciona — após a replicação, os complexos de manutenção da heterocromatina se ligam aos nucleossomos parentais e recrutam a maquinaria que repropaga as marcas para os nucleossomos novos.])

Um exemplo dramático desse mecanismo é a *inativação do cromossomo X* nas células de mulheres. Para igualar a dose gênica com homens (que têm um X só), uma das duas cópias do X é silenciada irreversivelmente em cada célula somática feminina — escolha aleatória feita no embrião precoce. Um RNA não codificante longo chamado #sigla("XIST", [X-inactive specific transcript — RNA não codificante longo que recobre o cromossomo X que será inativado e recruta complexos de silenciamento]) recobre o cromossomo a ser inativado e recruta complexos repressivos. O X inativo se condensa em heterocromatina e fica visível em microscópio como o *corpúsculo de Barr*.

#figura-nebli("/figuras/diferenciacao-celular/slide-28.png",
  largura: 90%,
  legenda: [Inativação do X. Um dos dois cromossomos X (escolhido aleatoriamente no embrião precoce) é coberto por XIST, recruta complexos de modificação de histona, condensa-se em heterocromatina e vira o corpúsculo de Barr — visível no neutrófilo feminino. *Não há perda de DNA*; o cromossomo continua presente, só silenciado.])

A consequência fenotípica é um *mosaico*: metade das células de uma mulher tem o X paterno ativo, metade tem o X materno ativo. Em mulheres heterozigotas para uma mutação ligada ao X, isso explica o quadro intermediário (pela mistura de células com X normal e X mutante). É também por isso que gatas calicó têm pelagem em mosaico tricolor.

#figura-nebli("/figuras/diferenciacao-celular/slide-29.png",
  largura: 60%,
  legenda: [O resultado: mosaico de células. No embrião precoce a escolha é aleatória célula a célula; uma vez decidida, é herdada por todas as descendentes da mesma célula. Por isso o tecido adulto da mulher é uma colcha de retalhos epigenéticos.])

O *terceiro* mecanismo é a metilação direta do DNA. Uma enzima adiciona um grupo metil ao carbono 5 de citosinas que estejam em sequência CpG (citosina seguida de guanina). Onde há muitos CpGs metilados perto de um promotor, o gene tipicamente fica silenciado — proteínas reguladoras deixam de conseguir se ligar, e complexos repressivos são recrutados ao DNA metilado.

A peça brilhante é a manutenção: durante a replicação, a fita-molde mantém suas metilações e a fita recém-sintetizada começa sem nenhuma. Aí entra a #sigla("DNMT1", [DNA-metiltransferase 1 — enzima de manutenção; reconhece a fita hemimetilada após replicação e copia o padrão para a fita nova]), uma enzima que reconhece especificamente o estado *hemimetilado* (CpG metilado de um lado, não metilado do outro) e completa a metilação na fita nova. Em uma rodada de replicação, o padrão antigo é fielmente copiado.

#figura-nebli("/figuras/diferenciacao-celular/slide-31.png",
  largura: 85%,
  legenda: [Manutenção da metilação por DNMT1. Antes da replicação: ambas as fitas metiladas nos mesmos CpGs. Depois da replicação: uma fita mantém a metilação herdada, a outra ainda não. DNMT1 reconhece especificamente esse estado hemimetilado e adiciona metil na fita nova, restaurando a simetria. Sem DNMT1, o padrão se diluiria a cada geração.])

O *quarto* mecanismo, mais recente, é a ação de RNAs não codificantes, especialmente #sigla("miRNA", [microRNA — pequeno RNA não codificante que se liga a mRNAs específicos e bloqueia sua tradução ou induz sua degradação]) (microRNAs) e ncRNAs longos. Os miRNAs são pequenos RNAs (~22 nucleotídeos) que se ligam a mRNAs alvo por complementaridade parcial e bloqueiam sua tradução ou induzem sua degradação. Diferentes tipos celulares têm portfólios diferentes de miRNAs, e essas redes pós-transcricionais também são herdadas pelas filhas — outra camada de memória.

#mini-resumo[Os quatro: *alça positiva* (a proteína sustenta sua própria expressão), *histonas* (cromatina aberta vs fechada), *metilação de DNA* (DNMT1 copia o padrão), *ncRNAs* (miRNAs ajustam pós-transcrição). Todos preservam o padrão sem mexer na sequência.]


#subtopico("3.5 — Diferenciação reversível? iPS e medicina regenerativa")

Por décadas, a hipótese padrão foi que a diferenciação seria *irreversível* — uma vez hepatócito, sempre hepatócito; o destino estaria escrito em pedra. A primeira rachadura nessa pedra veio em 1962, quando John Gurdon transplantou o núcleo de uma célula intestinal de girino adulto para um oócito enucleado e produziu um sapo inteiro — provando que o DNA da célula somática adulta ainda continha *todas* as instruções para construir um organismo. O núcleo só estava com a leitura travada num padrão; o citoplasma do oócito reformatou a leitura.

A reviravolta seguinte veio em 2006: Shinya Yamanaka mostrou que *não precisa de oócito*. Pegando uma célula somática adulta — um fibroblasto de pele, por exemplo — e introduzindo apenas *quatro* fatores de transcrição (Oct3/4, Sox2, c-Myc, Klf4), o fibroblasto é reprogramado a um estado equivalente ao das células-ES embrionárias. Pluripotência induzida. As células-iPS resultantes podem ser diferenciadas em laboratório para gerar neurônios, células-beta pancreáticas, cardiomiócitos, hepatócitos.

#figura-nebli("/figuras/diferenciacao-celular/slide-56.png",
  largura: 90%,
  legenda: [O experimento de Yamanaka. À esquerda: célula somática adulta. Em cima: os quatro fatores reprogramadores (Oct3/4, Sox2, c-Myc, Klf4) são introduzidos no núcleo. Resultado: a célula adquire morfologia e comportamento de célula-tronco embrionária — a iPS. Em cultura, a iPS pode ser direcionada para diferenciação em qualquer tipo celular dos três folhetos. *A célula somática "esqueceu" seu destino anterior.*])

A vantagem clínica é enorme: a iPS não exige embrião humano (driblando o problema ético das células-ES) e pode ser autóloga (vinda do próprio paciente, sem risco de rejeição imunológica). É a base mecanística da promessa da *medicina regenerativa*.

Tome o exemplo da diabetes tipo 1, doença em que o paciente perde as células-beta do pâncreas por destruição autoimune. A lógica do tratamento por iPS é: tirar um fibroblasto do próprio paciente; reprogramar em iPS com os quatro fatores; direcionar diferenciação em cultura para virar célula-beta (usando combinações de Pdx-1, Ngn3, MafA — outros fatores transcricionais mestres); transplantar de volta no paciente para repor a função perdida. A clínica ainda não chegou nesse cenário em escala, mas o mecanismo é compreendido e protocolos pré-clínicos estão maduros.

#clinica-box("Tratamento de diabetes tipo 1 com iPS", [O paciente com DM1 perdeu as células-beta produtoras de insulina (destruição autoimune das ilhotas de Langerhans). Estratégia regenerativa: célula somática do paciente → reprogramação por Oct3/4, Sox2, c-Myc, Klf4 → iPS → diferenciação direcionada em endoderma definitivo → progenitor pancreático → célula-beta funcional → transplante. A iPS contorna dois problemas das células-ES: (1) não exige embriões humanos; (2) sendo autóloga, não dispara rejeição. O desafio que sobra: c-Myc é oncogene — protocolos atuais buscam substituir ou eliminar para reduzir risco tumorigênico.])

Vale também mencionar a *transdiferenciação* — quando uma célula já diferenciada de um tipo é convertida diretamente em outro tipo, sem voltar para um estado intermediário pluripotente. Em peixes, células α-pancreáticas (produtoras de glucagon) podem se converter em β-pancreáticas (produtoras de insulina) após ablação massiva das β. Em mamíferos esse fenômeno é mais raro e mais difícil de induzir, mas o princípio é o mesmo: o destino não está em pedra.

#figura-nebli("/figuras/diferenciacao-celular/slide-51.png",
  largura: 70%,
  legenda: [Regeneração de membro em salamandra (axolote). Após amputação, células maduras na ferida desdiferenciam para um estado progenitor (blastema) e *re-diferenciam* na ordem certa, reconstruindo osso, músculo, nervo, pele. Em mamíferos esse grau de regeneração não acontece, mas o princípio molecular é o mesmo. Estudar esses sistemas iluminou o que falta para a medicina regenerativa humana.])

#mini-resumo[Diferenciação não é irreversível — só muito difícil de reverter. *Quatro fatores* (Oct3/4, Sox2, c-Myc, Klf4) bastam para reprogramar fibroblasto adulto em iPS. Aplicação clínica em curso: DM1, Parkinson, cardiomiócitos pós-IAM. O preço: c-Myc é oncogene, protocolos refinam.]

#conclusao-box[
A diferenciação celular é o mecanismo pelo qual uma única célula (o zigoto) se transforma em todos os tecidos do corpo *sem* nunca abrir mão da informação genética completa. Cada célula diferenciada carrega o genoma inteiro, mas lê só o subconjunto que define sua função.

A escala vai do *totipotente* (zigoto, embrião + anexos) ao *pluripotente* (massa celular interna, três folhetos) ao *multipotente* (HSC e outras teciduais, uma linhagem só) ao *terminalmente diferenciado* (hemácia, neurônio, hepatócito — sem retorno fácil). Potencialidade e diferenciação caminham em direções inversas — quanto mais especializada, menos versátil.

O destino é decidido por *combinações de fatores transcricionais* (poucos reguladores → muitos destinos) e mantido por *memória epigenética* (alças positivas, marcas de histona, metilação de DNA, ncRNAs) — tudo sem alterar a sequência. Esses mecanismos vão reaparecer em Núcleo Interfásico (organização da cromatina) e Regulação da Expressão Gênica (transcrição diferencial), e o conteúdo desta aula vira pré-requisito direto de Hematopoese.

No adulto, o turnover dos tecidos depende de *células-tronco residentes* que vivem em *nichos* específicos (endosteal da medula, base das criptas intestinais, camada basal da epiderme), dividem-se assimetricamente (intrínseca ou ambientalmente) e geram cascatas de progenitores transit-amplifying antes da diferenciação terminal.

E a peça final: a diferenciação *não é irreversível*. Yamanaka mostrou em 2006 que quatro fatores reprogramam um fibroblasto adulto em iPS pluripotente. Essa demonstração abriu a porta da medicina regenerativa — repor células-beta no DM1, neurônios dopaminérgicos no Parkinson, cardiomiócitos após infarto. O processo é difícil, lento, ainda não escalado clinicamente, mas conceitualmente o muro caiu: o destino celular é estável, *não é eterno*.
]

#mindmap-fechamento(
  tema: "DIFERENCIAÇÃO CELULAR",
  mensagem: "mesmo DNA em toda célula — o que muda é o padrão de leitura, mantido pela memória epigenética divisão após divisão",
  com-setas: true,
  estacoes: (
    (rotulo: "Potencial · zigoto → folhetos → tecidos", titulo: "Toti, pluri, multipotente",
     fala: [a célula vai abrindo mão de versatilidade conforme se especializa — três folhetos, três linhagens, função única no fim], cor: "a"),
    (rotulo: "Decisão · combinatorial control", titulo: "Poucos reguladores, muitos destinos",
     fala: [combinações de fatores de transcrição (3 reguladores = 8 destinos) escolhem o caminho — e a célula trava a escolha em alças autossustentáveis], cor: "neutra", destaque: true),
    (rotulo: "Memória · epigenética em 4 mecanismos", titulo: "Histona, metilação, ncRNA, alça positiva",
     fala: [o padrão é fielmente copiado nas filhas sem mexer no DNA — DNMT1 mantém metilação, complexos repropagam histonas modificadas], cor: "b"),
  ),
  rodape-titulo: "Onde vive · como mantém · como reverter",
  cartoes: (
    (titulo: "Onde a tronco mora", frase: [endosteal da medula segura a HSC quiescente; vascular libera as células maduras na circulação — não confundir os dois]),
    (titulo: "Por que se especializou tanto", frase: [eficiência funcional — hemácia sem núcleo carrega mais hemoglobina; neurônio dedica tudo à sinapse]),
    (titulo: "Reverter dá — é só difícil", frase: [Yamanaka: Oct3/4 + Sox2 + c-Myc + Klf4 reprogramam fibroblasto adulto em iPS pluripotente; base da medicina regenerativa]),
  ),
)
