#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  A imunidade inata trabalha com receptores herdados, fixos, iguais em todo indivíduo da espécie: eles leem assinaturas moleculares comuns a classes inteiras de micróbios e disparam uma resposta imediata, mas sempre a mesma. Este resumo trata do outro sistema — aquele em que o organismo *adquire* resistência a um agente que nunca encontrou antes, e guarda essa resistência por meses ou anos. Duas perguntas organizam tudo o que vem a seguir, e vale deixá-las explícitas desde já. A primeira é onde essa imunidade adquirida mora fisicamente: se ela pode ser retirada de um animal e entregue a outro, então ela é feita de alguma coisa, e essa coisa pode ser isolada, medida e descrita. A segunda é como um sistema com um genoma de tamanho finito consegue produzir um receptor capaz de encaixar em praticamente qualquer molécula do mundo — inclusive moléculas que a evolução nunca viu.

  A trilha da aula responde às duas na ordem em que a imunologia as respondeu historicamente. Primeiro reconstruímos o que a resposta adquirida é e quem participa dela. Depois isolamos o produto da resposta humoral — o anticorpo — e descemos até sua estrutura molecular, porque é a estrutura que explica todas as funções. Por fim, uma anomalia observada nessa estrutura força a conclusão de que o repertório não vem pronto do genoma: ele é montado, célula a célula, por recombinação. A história não é ornamento aqui; ela é o próprio argumento, porque cada descoberta só faz sentido como resposta ao impasse que a anterior criou.
]

#parte-title("PARTE I — A resposta adquirida: o que é, onde mora, quem participa", primeira: true)

#subtopico("1.1 — Um repertório completo gerado ao acaso e podado pelo próprio")

Antes de o linfócito encontrar qualquer micróbio, o receptor dele já existe. Essa é a inversão que sustenta todo o sistema adaptativo e convém fixá-la antes de qualquer outra coisa: o organismo não fabrica um receptor sob encomenda depois de ver o antígeno — ele fabrica, por antecipação e ao acaso, um conjunto de receptores tão vasto que algum deles vai encaixar em qualquer molécula que apareça. Esse conjunto é o que se chama repertório completo, e "completo" aqui significa exatamente isso: cobre o mundo molecular inteiro, não porque foi planejado para cobri-lo, mas porque foi gerado sem plano nenhum.

Gerar ao acaso resolve um problema e cria outro. Se as combinações são sorteadas sem critério, uma fração delas vai encaixar em moléculas do próprio organismo — e um linfócito que reconhece o próprio com força é uma célula programada para atacar o hospedeiro. O sistema precisa, portanto, de uma etapa de poda, e a poda tem um critério só disponível: a interação com o que está presente. Nos #termo-nota[órgãos linfoides primários][medula óssea e timo — onde o linfócito nasce, monta seu receptor e é testado, antes de circular], o repertório recém-sorteado é confrontado com os antígenos próprios que ali circulam. Quem reage forte demais é eliminado ou silenciado; quem passa no teste sai para a periferia. O resultado dessa subtração é o repertório final — o mesmo repertório completo, menos as especificidades que apontavam para dentro.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-03.png",
  largura: 62%,
  legenda: [Repare que a seta de seleção não acrescenta nada — ela subtrai. O repertório entra completo, atravessa o crivo dos antígenos próprios e sai menor. É por isso que o sistema consegue distinguir próprio de não-próprio sem nunca ter visto o não-próprio: ele aprendeu apenas o que *não* deve atacar.])

A consequência lógica dessa arquitetura é elegante e vale enunciar devagar, porque ela reaparece ao longo do resumo inteiro. O sistema imune nunca foi ensinado a reconhecer micróbios. Nos órgãos linfoides primários não há micróbio nenhum para servir de modelo — só há o próprio. Tudo o que o sistema aprende ali é o que evitar. O reconhecimento do não-próprio é, então, um resultado por exclusão: qualquer coisa que ative um receptor sobrevivente é, por definição, algo que não estava presente durante a seleção. Essa é a razão de a imunologia clássica ter sido descrita como a ciência da discriminação entre o próprio e o não-próprio — o nome pega a lógica do sistema com precisão, mesmo em textos anteriores a tudo o que hoje se sabe de mecanismo molecular.

Vale acrescentar uma camada que a poda no timo torna mais nítida. A seleção tímica não tem um único sentido: além de eliminar o que reage forte demais com o próprio, ela descarta também o que não reage *nada* — um linfócito T cujo receptor é incapaz de encostar nas moléculas de apresentação do hospedeiro é inútil, porque nunca conseguirá enxergar antígeno algum. Sobrevive a faixa intermediária, que reconhece o próprio fracamente. Essa dupla exigência é a razão de a maior parte dos timócitos produzidos morrer antes de sair do timo, e volta a aparecer no fim deste resumo, quando o receptor do linfócito T for descrito como restrito.

#mini-resumo[
  O que ficou de pé: o repertório é sorteado antes do encontro com o antígeno e depois filtrado contra o próprio. O sistema não aprende quem é inimigo — ele aprende quem é de casa, e trata todo o resto como estranho.
]

#subtopico("1.2 — O reconhecimento no sistema imune é composto")

Nenhuma célula sozinha executa o reconhecimento adaptativo. Três atores dividem a tarefa, e cada um enxerga uma coisa diferente, o que é justamente o motivo de o arranjo funcionar. O primeiro é a #sigla("APC", [célula apresentadora de antígeno, do inglês _antigen-presenting cell_ — captura moléculas do ambiente, lê o contexto e traduz ambos para o linfócito T]), que amostra o ambiente sem discriminar origem: ela captura moléculas microbianas, moléculas próprias alteradas, moléculas vindas dos alimentos e moléculas próprias comuns, tudo junto. Ao mesmo tempo, e por um canal separado, ela lê o estado homeostático do microambiente em que está — usa para isso os receptores de padrão molecular da imunidade inata, que detectam assinaturas de agressão e sinais de dano tecidual. A célula apresentadora entrega então duas informações ao mesmo tempo: *o que* estava no ambiente e *em que estado* o ambiente estava.

Essa segunda informação é o que impede o sistema de reagir contra tudo o que amostra. Uma proteína alimentar e uma proteína bacteriana chegam à célula apresentadora pelo mesmo caminho; o que as distingue não é a molécula em si, mas o contexto inflamatório que acompanha uma e não a outra.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-04.png",
  largura: 76%,
  legenda: [Duas setas entram na célula apresentadora e carregam informações de natureza distinta: a amarela traz o conteúdo molecular do ambiente, a azul traz o estado homeostático desse ambiente. A seta verde que sai leva as duas informações fundidas ao linfócito T. Note que o linfócito B recebe a linha pontilhada diretamente do mundo molecular — ele não depende de tradução.])

O segundo ator é o linfócito T, e ele é a célula que decide. Todo o restante do sistema adaptativo depende do sinal que o T emite ou deixa de emitir, e o T só emite esse sinal depois de receber a informação processada pela célula apresentadora — nunca antes, e nunca diretamente do antígeno solúvel. O terceiro ator é o linfócito B, que opera sob uma regra diferente: seus receptores clonais interagem *diretamente* com o antígeno íntegro, sem intermediário nenhum. O linfócito B, portanto, reconhece sozinho — mas o que ele faz depois de reconhecer depende, quase sempre, do sinal que recebe do linfócito T.

#confusao-prevista(
  titulo: "O linfócito B não precisa de apresentação para reconhecer",
  aluno_acha: [se o linfócito T só enxerga antígeno apresentado, o linfócito B deveria seguir a mesma regra],
  mecanismo: [o receptor do linfócito B é um anticorpo ancorado na membrana, e anticorpo liga antígeno íntegro em solução — é literalmente o que ele faz. O que o linfócito B precisa do linfócito T não é a apresentação do antígeno, é a *autorização* para responder e a instrução sobre que tipo de anticorpo produzir.],
)

O nome dessa arquitetura de três peças é imunidade adquirida, e a palavra "composto" descreve bem o reconhecimento que ela realiza: nenhum dos participantes tem, sozinho, informação suficiente para decidir. A célula apresentadora sabe o que havia no ambiente mas não tem repertório clonal; o linfócito T tem repertório clonal e recebe o contexto, mas não enxerga antígeno solúvel; o linfócito B enxerga antígeno solúvel mas não lê o contexto. Reunidas, as três geram uma resposta que é ao mesmo tempo específica ao agente e proporcional à ameaça.

#subtopico("1.3 — Especificidade e memória: o que o desafio com bactéria atenuada demonstrou")

Duas propriedades definem a resposta adquirida e ambas foram estabelecidas por um experimento de desenho simples, feito muito antes de qualquer molécula ser conhecida. Injeta-se em um camundongo uma bactéria X virulenta e o animal morre. Repete-se o procedimento em outro animal, mas agora a bactéria X passa antes por um tratamento que reduz sua #termo-nota[virulência][capacidade de causar doença; a bactéria atenuada continua estimulando o sistema imune, apenas deixa de matar] sem eliminá-la. Esse animal sobrevive à injeção, e duas semanas depois recebe a bactéria X virulenta. Ele sobrevive de novo. Alguma coisa mudou nele durante essas duas semanas, e essa mudança é o que se chama imunidade.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-05.png",
  largura: 72%,
  legenda: [As três fileiras são o experimento inteiro. A de cima é o controle: X virulenta mata. A do meio mostra proteção depois de X atenuada. A de baixo é o braço decisivo — Y atenuada não protege contra X, e é isso que separa imunidade de vigor genérico.])

A terceira fileira do experimento é a que carrega o argumento. Se o animal for previamente exposto a uma bactéria Y atenuada e depois desafiado com a bactéria X virulenta, ele morre. A exposição prévia não conferiu resistência geral, não deixou o animal "mais forte", não estimulou uma defesa inespecífica: protegeu contra X e apenas contra X. A resistência adquirida é dirigida a um alvo, e essa é a primeira propriedade — a especificidade. A segunda propriedade está escondida no intervalo de duas semanas e nos meses que se seguem. A proteção não é imediata, o que indica que algo precisa ser construído; e ela persiste muito depois de a bactéria atenuada ter sido eliminada, o que indica que o que foi construído permanece. Essa persistência é a memória.

O intervalo, aliás, não é detalhe de protocolo. Ele é o tempo necessário para que os raríssimos clones cujo receptor encaixa em X sejam encontrados, ativados, expandidos em número e diferenciados em células capazes de produzir grandes quantidades do produto efetor. Desafiar o animal um dia depois da imunização não protege — não porque a especificidade não exista, mas porque a expansão clonal ainda não aconteceu. Especificidade e memória, portanto, não são duas curiosidades independentes: são as duas faces de um sistema que localiza um clone raro, multiplica-o e guarda o resultado.

#clinica-box("Por que a vacina precisa de tempo e de reforço", [
  Todo o princípio da vacinação está nesse experimento. Apresenta-se ao organismo uma versão do agente incapaz de causar doença — atenuada, inativada ou reduzida a um de seus componentes — e deixa-se o sistema montar a resposta em condições seguras. Duas consequências práticas decorrem direto do desenho: a proteção não é imediata, porque a expansão clonal leva dias a semanas, e por isso vacinar durante um surto já instalado protege menos do que vacinar antes; e a proteção é específica, motivo pelo qual imunizar contra um agente não oferece cobertura contra outro, ainda que os dois causem quadros clínicos parecidos. O reforço existe justamente para explorar a memória: o segundo contato encontra um contingente de clones já expandido e produz uma resposta mais rápida, mais intensa e mais duradoura do que o primeiro.
])

#subtopico("1.4 — Humoral ou celular: uma classificação que nasceu do experimento de transferência")

Uma vez estabelecido que o animal imunizado carrega alguma coisa que o protege, a pergunta seguinte é de localização — e o começo do século XX oferecia um instrumento só para respondê-la: retirar frações do animal imune e entregá-las a um animal virgem. Se a fração transferida protege o receptor, então a imunidade estava ali. A lógica é a de um teste de transplante, e o vocabulário que ela gerou continua em uso até hoje.

A primeira fração testada foi o soro, e o resultado tem duas metades igualmente importantes. Em alguns casos, transferir o soro de um animal imune para um animal virgem torna o receptor capaz de sobreviver ao desafio com a bactéria virulenta: a imunidade estava nos humores, e por isso se chamou imunidade humoral. Em outros casos, porém, o soro do animal comprovadamente imune não protege o receptor — e aqui está o ponto que costuma escapar. O fracasso não significa que o doador não estivesse imune; significa apenas que a imunidade dele não morava no soro. Muito depois, quando se tornou tecnicamente possível transferir células do animal imune, viu-se que exatamente esses casos eram transferíveis por via celular. A imunidade que não passa pelo soro mas passa pelas células recebeu o nome de imunidade celular.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-06.png",
  largura: 74%,
  legenda: [O animal imune se bifurca em duas frações. Pelo braço do soro, sobrevivência define imunidade humoral; morte pelo soro seguida de sobrevivência pela transferência celular define imunidade celular. A definição é inteiramente operacional — ela descreve o que se transferiu, não que célula produziu o quê.])

#atencao-box("Humoral não quer dizer linfócito B, e celular não quer dizer linfócito T", [
  A tentação é traduzir a dupla humoral/celular para a dupla B/T, e a tradução é falsa. Os nomes vêm de um experimento de transferência, não de uma atribuição celular: humoral é o que viaja no soro, celular é o que só viaja dentro de células. Ocorre que a resposta humoral depende do linfócito T tanto quanto a celular — é o T que autoriza o B a responder e que instrui qual tipo de anticorpo produzir. O que torna a resposta humoral transferível pelo soro não é a ausência do linfócito T na história; é o fato de o produto final dela ser uma molécula solúvel, que continua funcionando depois de separada da célula que a fabricou. Concluir "depende de linfócito T, logo é celular" inverte a definição e leva o raciocínio para o lugar errado.
])

Com os critérios de hoje, aliás, separar as duas respostas ficou difícil, e vale dizer isso com todas as letras: uma resposta descrita como celular também recruta anticorpo, e uma resposta humoral também exige sensibilização de linfócitos T. A dicotomia sobrevive porque é historicamente fundadora e porque nomeia bem os dois braços efetores, não porque descreva compartimentos estanques. O que ela deixou de herança prática foi a sorologia: procurar no soro os sinais moleculares de uma resposta imune é, ainda hoje, como se documenta contato prévio com um agente e como se avalia proteção — e o exame de rotina que se pede no ambulatório é descendente direto daquele experimento de transferência.

Se a imunidade humoral viaja no soro, ela é feita de moléculas — e o passo seguinte é isolar essas moléculas e descobrir o que são. É a PARTE II inteira.

#parte-title("PARTE II — O anticorpo: da mancha no gel à molécula em Y")

#subtopico("2.1 — Anticorpo é gama-globulina: o que a eletroforese mostra e o que ela esconde")

O soro do animal imune contém algo que o protege, e esse algo recebeu o nome de anticorpo muito antes de se saber o que era. Para descobrir a natureza química da coisa, o instrumento disponível era a eletroforese de proteínas: coloca-se o soro num meio que dificulta a migração, aplica-se um campo elétrico e cada proteína caminha a uma velocidade que depende de sua carga e de seu tamanho. O soro humano gera um padrão razoavelmente reprodutível. Uma proteína domina em quantidade e migra depressa por ser pequena e bem carregada — a albumina. Todo o resto forma o grupo das globulinas, que a #termo-nota[densitometria][medida da intensidade de coloração ao longo do gel, que converte as bandas em picos de altura proporcional à quantidade de proteína] separa em picos alfa-1, alfa-2, beta e gama.

Convém corrigir aqui uma leitura equivocada frequente: albumina e globulina não são definidas pela velocidade de migração. O critério original é de solubilidade — as globulinas precipitam bem antes da albumina à medida que a concentração de sais aumenta na solução. A eletroforese apenas as separa; quem as define é o comportamento frente ao sal.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-07.png",
  largura: 76%,
  legenda: [À esquerda, quatro eletroforeses normais empilhadas: repare que elas diferem principalmente na faixa gama. O pico gama não é um pico — é uma montanha larga, e a largura é o retrato direto da heterogeneidade do repertório. À direita, a hiperimunização experimental levanta essa montanha (curva pontilhada), e foi esse deslocamento que permitiu chamar os anticorpos de gama-globulinas.])

O experimento óbvio, uma vez que se sabe que a imunidade viaja no soro, é imunizar um animal e procurar na eletroforese a proteína nova que apareceu. E o resultado é negativo: o perfil eletroforético não muda. A explicação desse achado negativo é mais instrutiva do que qualquer resultado positivo teria sido. O organismo não está parado esperando o experimentador — ele está o tempo todo exposto a estímulos antigênicos do ambiente e produzindo anticorpos contra eles. A montanha gama já existe e já é alta antes da imunização; o contingente novo de moléculas dirigidas ao antígeno injetado se dilui nela e não se destaca. Só quando se estimula o animal repetidas vezes com o mesmo antígeno — a hiperimunização — o acúmulo se torna grande o bastante para levantar visivelmente a faixa gama. Foi esse deslocamento que autorizou a definição histórica dos anticorpos como gama-globulinas.

A definição é uma aproximação, hoje relativizada: com métodos atuais sabe-se que parte dos anticorpos não migra na faixa gama. A aproximação foi útil o suficiente para sustentar décadas de terapêutica — tratavam-se doenças administrando gama-globulina purificada, isto é, a fração do soro que contém os anticorpos. Hoje se purifica o anticorpo específico, e não mais a fração inteira, o que aumenta muito a potência e reduz o volume necessário.

#mini-resumo[
  Em uma frase: o anticorpo se esconde na eletroforese porque nunca esteve ausente — o soro normal já é uma mistura policlonal densa, e um clone novo é uma gota nesse oceano.
]

Duas palavras convivem daqui em diante e não são intercambiáveis por acaso. Toda gama-globulina que exerce função imune é chamada imunoglobulina — #sigla("Ig", [imunoglobulina — gama-globulina que exerce função de anticorpo; o termo nomeia a molécula sem se comprometer com um alvo específico]) nas siglas —, e todo anticorpo é uma imunoglobulina. A recíproca também vale, mas a escolha da palavra carrega ênfase: dizer "anticorpo" pressupõe um alvo em mente — anticorpo *contra alguma coisa* —, enquanto dizer "imunoglobulina" nomeia a classe de molécula sem se comprometer com especificidade nenhuma.

#subtopico("2.2 — O mieloma múltiplo como lupa: pico monoclonal e o paradoxo de Dreyer & Bennett")

Estudar quimicamente as gama-globulinas do soro normal é quase impossível pelo motivo que a eletroforese acabou de mostrar: elas são heterogêneas demais. Sequenciar uma proteína exige tê-la pura e em quantidade, e o soro normal oferece uma mistura de milhões de moléculas diferentes em concentrações minúsculas cada uma. O que destravou o problema foi uma doença.

O mieloma múltiplo é uma neoplasia hematológica de #termo-nota[plasmócitos][linfócito B em estágio terminal de diferenciação, especializado em secretar anticorpo em grande quantidade] — o nome combina "mielo", de medula, com "oma", de tumor, e o adjetivo "múltiplo" registra as várias lesões líticas que a doença produz no osso. A consequência decisiva é o que se vê na eletroforese desse paciente: em vez da montanha larga, aparece um pico reto, alto e de base estreita. Um único clone de plasmócitos, escapado do controle de divisão, se reproduz indefinidamente e secreta uma proteína homogênea em grande quantidade. É o pico monoclonal — e ele é, ao mesmo tempo, um marcador diagnóstico e a fonte de proteína pura que a bioquímica precisava.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-08.png",
  largura: 74%,
  legenda: [Compare os dois traçados. À esquerda o soro normal, com a gama espalhada; à direita o soro do paciente com mieloma, onde o pico monoclonal se ergue reto e estreito sobre a mesma faixa. No centro, as lesões líticas no crânio e no osso longo — o "múltiplo" do nome está literalmente na imagem.])

De posse de proteínas monoclonais vindas de pacientes diferentes, Dreyer e Bennett fizeram em 1965 a comparação que abriu o problema seguinte. Ao sequenciar essas proteínas, encontraram em todas elas um trecho idêntico — a mesma sequência de aminoácidos, em pacientes sem parentesco algum, produzida por clones tumorais independentes. E encontraram, na mesma molécula, um trecho diferente em cada paciente. A proteína tinha, portanto, uma porção constante e uma porção variável.

A leitura imediata desse achado seria supor duas cadeias polipeptídicas — uma constante codificada por um gene, outra variável codificada por outro — unidas depois da tradução por algum mecanismo de montagem. Foi exatamente essa hipótese que os dados derrubaram: a porção constante e a porção variável estão numa *única* cadeia polipeptídica contínua. E uma cadeia polipeptídica contínua, pela regra que a biologia molecular tinha estabelecido, vem de um gene lido de ponta a ponta. Duas informações incompatíveis passam então a coexistir — um trecho compartilhado por indivíduos diferentes e um trecho exclusivo de cada um, dentro da mesma cadeia, logo do mesmo gene. É o paradoxo que dá título ao trabalho deles, e ele fica aberto até a PARTE III.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-09.png",
  largura: 66%,
  legenda: [O diagrama à esquerda é o desenho original da cadeia múltipla da gama-globulina, com a região comum marcada no centro. À direita, o esquema que resume o achado: várias cadeias leves de origens diferentes divergem à esquerda da linha tracejada e convergem para uma sequência idêntica à direita dela.])

#clinica-box("O que o pico monoclonal significa na prática", [
  A eletroforese de proteínas séricas segue sendo o primeiro exame diante da suspeita de mieloma, e a lógica de leitura é exatamente a da figura: procura-se uma banda estreita e alta destacando-se da faixa gama, porque banda estreita significa produto de um clone só. O quadro clínico decorre das duas metades da doença. A proliferação plasmocitária na medula ativa reabsorção óssea e produz as lesões líticas, a dor óssea e a hipercalcemia; e a proteína monoclonal, produzida em excesso, sobrecarrega o rim. Ao mesmo tempo o paciente é imunodeprimido, e por um motivo que a lógica do repertório explica bem: um único clone ocupa a medula e domina a produção, de modo que a gama-globulina policlonal normal — a que cobria o mundo molecular inteiro — despenca. O paciente tem muita imunoglobulina e pouquíssima variedade, e é a variedade que protege.
])

Vale registrar desde já que o mesmo padrão constante-variável reaparece fora do tumor, na resposta imune normal, e essa coincidência é a peça que fecha o argumento lá na frente. No primeiro contato com um antígeno, produz-se um tipo de imunoglobulina; algum tempo depois, produz-se outro tipo, com estrutura bem diferente, contra o mesmo antígeno e com a mesma capacidade de ligá-lo. Isolando um plasmócito que fabrica o primeiro tipo e dando-lhe os estímulos adequados, ele passa a fabricar o segundo — a mesma célula troca a classe de imunoglobulina que produz, sem mudar o alvo. O fenômeno se chama troca de classes, e ele mostra que a associação flexível entre uma porção constante e uma porção variável não é uma esquisitice do tumor: é como o sistema opera normalmente.

#subtopico("2.3 — A estrutura em Y: Fab, Fc e por que a papaína só corta na dobradiça")

Sabendo que a molécula tem partes com propriedades diferentes, o caminho experimental para descrevê-la foi cortá-la e ver o que cada pedaço faz. A ferramenta é a digestão enzimática controlada: usa-se uma protease em condições diluídas e por tempo limitado, de modo que ela quebre poucas ligações peptídicas em vez de degradar tudo. E há uma informação embutida na escolha da ferramenta que costuma passar despercebida — protease quebra ligação peptídica, e apenas ligação peptídica. Se um tratamento com protease separa dois pedaços, eles estavam unidos por ligação peptídica; se dois pedaços continuam juntos depois da digestão completa, eles estão unidos por outra coisa.

A papaína, protease do mamão, gera dois tipos de fragmento. Um deles conserva a capacidade de ligar antígeno e por isso se chama Fab — fragmento de ligação ao antígeno, do inglês _antigen binding_. O outro não liga antígeno, mas é homogêneo o bastante entre anticorpos de especificidades diferentes para formar cristais, e daí o nome Fc, fragmento cristalizável. A pepsina, usada no lugar da papaína, produz um resultado diferente e informativo: um único fragmento capaz de ligar *dois* antígenos ao mesmo tempo. A pepsina ataca a molécula a partir da extremidade C-terminal e a degrada até logo antes de uma região central flexível — a #termo-nota[dobradiça][segmento flexível e exposto que une os dois braços do Y ao tronco; por não estar protegido pelo enovelamento, é o ponto onde as proteases encontram acesso] —, preservando os dois braços ainda ligados um ao outro.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-11.png",
  largura: 70%,
  legenda: [A molécula é um tetrâmero em Y: duas cadeias pesadas longas ao centro e duas cadeias leves nos braços, todas unidas por pontes dissulfeto. As alças laranja marcam as porções variáveis, no alto de cada braço; as azuis, as constantes. À direita da dobradiça o tronco é o Fc; acima dela, cada braço é um Fab.])

A estrutura que emerge desses cortes é um tetrâmero — quatro cadeias polipeptídicas. Duas são longas e se chamam cadeias pesadas; duas são curtas e se chamam cadeias leves. Elas não se mantêm unidas por ligações peptídicas, e sim por pontes dissulfeto, o que é exatamente coerente com a resistência da estrutura à protease e com o fato de um tratamento redutor, e não uma enzima, ser o que separa cadeia pesada de cadeia leve. O arranjo final é o Y: cada braço reúne uma cadeia leve inteira com a metade N-terminal de uma pesada, e o tronco reúne as metades C-terminais das duas pesadas. Tanto nas leves quanto nas pesadas há porção variável, na ponta, e porção constante, no resto.

Falta explicar por que a papaína corta exatamente na dobradiça e não em qualquer outro lugar, já que ligações peptídicas existem ao longo de toda a cadeia. A resposta está no domínio de imunoglobulina — a unidade estrutural de cerca de 110 aminoácidos em que a cadeia polipeptídica se enovela formando um novelo compacto e muito estável. Enovelada assim, a cadeia expõe pouquíssimos trechos ao solvente, e o que uma protease não alcança ela não corta. A dobradiça é justamente a região que fica *fora* dos domínios, flexível e exposta — e é por isso que ela é o ponto de clivagem. A pepsina consegue avançar um pouco mais porque ataca pela extremidade e progride devagar, mas mesmo ela é barrada pelos domínios enovelados. Esse arranjo se mostrou tão eficiente que reaparece em dezenas de outras proteínas de reconhecimento celular, e o conjunto delas é o que se chama superfamília das imunoglobulinas.

O último elemento estrutural define a nomenclatura inteira do próximo subtópico. As cadeias leves vêm em dois tipos, kappa e lambda. As cadeias pesadas vêm em muito mais: duas alfa, uma delta, uma épsilon, quatro gama e uma mu. É a cadeia pesada que dá nome à molécula — cadeia alfa faz #sigla("IgA", [imunoglobulina A — classe definida pela cadeia pesada alfa; principal imunoglobulina de secreções e mucosas]), delta faz #sigla("IgD", [imunoglobulina D — classe definida pela cadeia pesada delta; atua como receptor de membrana no linfócito B e praticamente não é secretada]), épsilon faz #sigla("IgE", [imunoglobulina E — classe definida pela cadeia pesada épsilon; fica ligada a células de mucosa e tecido conjuntivo, não circulando livre]), gama faz #sigla("IgG", [imunoglobulina G — classe definida pela cadeia pesada gama; a mais abundante no soro e a que sustenta a memória humoral]) e mu faz #sigla("IgM", [imunoglobulina M — classe definida pela cadeia pesada mu; primeira produzida na resposta e organizada em pentâmero]). Qualquer uma dessas pesadas pode se combinar com kappa ou com lambda, o que significa que o tipo de cadeia leve não define classe nenhuma.

#subtopico("2.4 — Isotipos, alotipos e idiotipos: três eixos de variação")

As imunoglobulinas variam em três eixos independentes, e confundi-los é a origem de boa parte da dificuldade com esse vocabulário. O que separa os três é sempre a mesma coisa — em relação a quem a variação está sendo medida.

O primeiro eixo é a variação que existe em todos os indivíduos da espécie, igual em todos. São os isotipos, e "iso" registra exatamente essa igualdade. Historicamente eles foram chamados de classes, quando os métodos disponíveis eram grosseiros — carga, migração, resistência —, e depois se refinaram em subclasses, quando ficou claro que moléculas com o mesmo comportamento geral de IgG ainda podiam ser separadas entre si. Hoje se sabe que cada classe e cada subclasse é codificada por um gene de cadeia pesada distinto, o que dá base molecular ao que começou como distinção físico-química. Vale notar que a composição de isotipos é característica da espécie: outras espécies têm conjuntos diferentes dos nossos.

O segundo eixo é a variação entre indivíduos da mesma espécie. Um indivíduo carrega um alelo e outro carrega outro, de modo que os dois fabricam uma IgG que difere levemente em sequência — em geral na cadeia pesada, às vezes na leve. Essa variação alélica é o #termo-nota[alotipo][variante alélica da imunoglobulina; presente em alguns indivíduos da espécie e ausente em outros, ao contrário do isotipo]. O terceiro eixo é a variação dentro de um mesmo indivíduo: o anticorpo que gruda na bactéria X é diferente do anticorpo que gruda na bactéria Y, e essa diferença mora na porção variável. São os idiotipos.

#table(
  columns: (auto, 1fr, 1fr),
  inset: 8pt,
  align: left,
  stroke: 0.5pt + gray-border,
  table.header(
    [*Eixo*], [*Varia em relação a quem*], [*Onde mora a diferença*],
  ),
  [Isotipo], [Igual em todos os indivíduos da espécie — IgM, IgD, IgG (1 a 4), IgA (1 e 2), IgE], [Gene de cadeia pesada distinto para cada classe e subclasse],
  [Alotipo], [Difere entre indivíduos da espécie: um tem um alelo, outro tem outro], [Variação alélica, em geral na porção constante da cadeia pesada],
  [Idiotipo], [Difere entre os anticorpos de um mesmo indivíduo], [Porção variável — é o próprio sítio de ligação que define a diferença],
)

Cada isotipo tem propriedades próprias, e a lista delas antecipa a PARTE III: peso molecular diferente, momento de produção diferente ao longo da resposta, concentração sérica e meia-vida diferentes na circulação, e capacidade diferente de interagir com os demais componentes do organismo. Essa última é o que mais importa funcionalmente — mudar a molécula muda com quem ela consegue conversar, e portanto muda o que ela consegue fazer.

#clinica-box("Meia-vida, alotipo e decisões de beira de leito", [
  As diferenças entre isotipos deixam de ser taxonomia no momento em que se precisa repor anticorpo. Um paciente com imunodeficiência de produção recebe imunoglobulina exógena, e escolher *qual* e *de quanto em quanto tempo* administrar depende diretamente da meia-vida de cada classe na circulação — não é decisão arbitrária de protocolo, é aritmética de reposição. Os alotipos, por sua vez, importam em quem recebe transfusões repetidas: o receptor pode ser sensibilizado contra variantes alélicas de imunoglobulina presentes no doador e ausentes nele, passando a produzir anticorpos contra elas. É por isso que o hemoterapeuta acompanha esse eixo em politransfundidos, e é um bom exemplo de como uma variação que parece invisível no soro normal se torna clinicamente relevante quando o sistema é repetidamente exposto ao alelo do outro.
])

Os idiotipos, por fim, geraram uma linha teórica notável na imunologia. Se cada anticorpo tem uma porção variável única, então essa porção variável é ela própria uma estrutura nova para o organismo — e pode, em princípio, ser reconhecida por outros receptores clonais. A partir dessa observação foi proposto que o sistema imune funcionaria como uma rede de receptores que se reconhecem mutuamente, e dessa rede emergiria a regulação da resposta. A proposta da rede idiotípica perdeu força como mecanismo geral de controle, mas o conhecimento dos idiotipos continua sendo usado, inclusive terapeuticamente. Com a molécula descrita e os eixos de variação separados, resta a pergunta que a estrutura existe para responder: o que, afinal, o anticorpo faz.

#parte-title("PARTE III — O que o anticorpo faz e de onde vem a diversidade")

#subtopico("3.1 — O sítio de ligação, o CDR e as duas funções que nascem só do Fab")

A propriedade central do anticorpo é uma só, e todas as outras derivam dela ou a acompanham: ligar-se com alta afinidade a uma determinada molécula de antígeno. Essa capacidade mora no fragmento Fab, e mais precisamente nas porções variáveis — tanto da cadeia pesada quanto da leve, agindo juntas. Dentro dessas porções variáveis, o contato real com o antígeno se dá em alças curtíssimas da cadeia, que se aproximam no espaço e formam uma bolsa complementar à superfície do antígeno. Essas alças são as regiões determinantes de complementaridade, ou #sigla("CDR", [regiões determinantes de complementaridade, do inglês _complementarity determining regions_ — as alças curtas da porção variável que fazem o contato direto com o antígeno]).

A desproporção aqui é instrutiva. A molécula inteira é grande, e o que efetivamente toca o antígeno é um punhado de aminoácidos distribuídos em algumas alças. A consequência dessa arquitetura é que trocar a especificidade de um anticorpo exige mudar pouquíssima coisa — basta alterar aminoácidos do CDR e a bolsa passa a encaixar em outra molécula. O resto, porém, não pode ser mexido: o arcabouço que sustenta as alças na posição correta é o que mantém a estrutura, e perdida a estrutura, perde-se a função inteira. É essa combinação de um núcleo rígido com pontas altamente variáveis que permite ao sistema gerar diversidade astronômica sem sacrificar estabilidade.

Duas funções nascem diretamente dessa ligação, sem necessidade de mais nada. A primeira é a neutralização. Ao se ligar a um vírus, o anticorpo o impede de infectar; ao se ligar a uma toxina — a tetânica, por exemplo — impede que ela exerça o efeito tóxico. Nos dois casos a atividade do alvo é abolida pela simples ocupação, e por isso o termo se aplica. A segunda é o bloqueio de aderência, e a diferença entre as duas merece atenção porque o vocabulário costuma escorregar.

#confusao-prevista(
  titulo: "Anticorpo não neutraliza bactéria",
  aluno_acha: [se o anticorpo neutraliza vírus e toxina, deveria neutralizar bactéria também],
  mecanismo: [neutralizar significa levar a atividade do alvo a zero, e isso funciona para vírus e toxina porque a função deles depende de uma superfície de contato que o anticorpo ocupa. A bactéria ligada por anticorpo continua metabolizando, continua produzindo toxina e continua se dividindo — ela não foi a zero. O que o anticorpo faz nela é impedir que se fixe ao tecido-alvo, e como a aderência é a primeira etapa de praticamente toda infecção, isso já é proteção considerável. Chame de bloqueio de aderência, não de neutralização.],
)

O bloqueio de aderência é, aliás, mais poderoso do que a descrição sugere. Se o anticorpo se liga a uma molécula de superfície de que o micro-organismo depende para se associar ao tecido, a infecção é interrompida no primeiro passo, antes de qualquer dano. Mas o bloqueio nem sempre basta — a bactéria pode seguir produzindo toxina e se dividindo em suspensão —, e é aí que entram as funções que não dependem do braço que liga, e sim do tronco da molécula.

#subtopico("3.2 — As funções que dependem do Fc: transporte, opsonização, complemento e ativação celular")

Além de agarrar o antígeno, o anticorpo funciona como uma ponte física entre esse antígeno e as células do organismo. A ponte tem duas extremidades com papéis distintos: o Fab segura o alvo, e o Fc engata em receptores presentes na superfície das células do hospedeiro. Todas as funções descritas neste subtópico dependem das porções constantes das cadeias pesadas, reunidas no Fc — o que explica por que trocar a classe de um anticorpo muda tanto o que ele consegue fazer, sem mudar em nada aquilo que ele reconhece.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-13.png",
  largura: 78%,
  legenda: [A seta que sai da propriedade central leva a neutralização e bloqueio de aderência — as duas funções que nascem só do Fab. Todo o leque de baixo parte da ligação a receptores específicos no organismo e depende do Fc. Note que complemento e ativação celular convergem para a mesma consequência: inflamação.])

O transporte através de epitélios é a primeira dessas funções e a mais fácil de subestimar. Certas células epiteliais expressam receptores que reconhecem o Fc, capturam o anticorpo de um lado e o depositam do outro — e o processo independe de o sítio de ligação estar ocupado. Assim, a imunoglobulina produzida pela mãe atravessa a placenta e passa a proteger o feto, e a imunoglobulina captada pela glândula mamária é lançada no leite, protegendo o recém-nascido. A observação que decorre disso é maior que a imunologia: a resposta imune materna protege a prole, o que significa que o sistema imune não protege apenas o indivíduo que o abriga.

A opsonização é a segunda, e é a que mais depende da ponte. A imunidade inata faz os tecidos serem infiltrados por células fagocitárias, mas fagocitar exige que a célula consiga primeiro agarrar firmemente a partícula — e o fagócito nem sempre tem, na superfície, um receptor capaz de segurar aquele alvo específico. O anticorpo resolve o problema porque tem as duas pontas: liga o antígeno pelo Fab e é agarrado pelo fagócito através de receptores para o Fc. #termo-nota[Opsonizar][revestir uma partícula de moléculas que os fagócitos reconhecem, tornando-a agarrável; a fagocitose é o passo seguinte, executado pela célula] é exatamente isso — revestir o alvo para torná-lo pegável. Vale a distinção: opsonização não é fagocitose, é a condição que a viabiliza.

A terceira função é ativar o sistema complemento, um conjunto de proteínas plasmáticas cujo nome vem justamente da observação de que ele complementa a ação dos anticorpos. É útil notar que o complemento é, na origem, um sistema de reconhecimento de padrões moleculares — ele funciona por conta própria, e a interação com o anticorpo é um dos caminhos de ativação, não o único. A quarta função é ativar diretamente uma célula: o engate do Fc em receptores de superfície pode disparar programas funcionais na célula que o recebeu. Complemento e ativação celular convergem para a mesma consequência — inflamação —, e a inflamação potencializa toda a resposta imune, recrutando mais células e mais moléculas para o local.

#clinica-box("Quando ativar a célula é o problema: a doença de Graves", [
  A capacidade de ativar células diretamente mostra seu lado destrutivo quando o alvo do anticorpo é um receptor hormonal. Na doença de Graves, o organismo produz anticorpos contra o receptor de tireotrofina da célula tireoidiana — e esses anticorpos não bloqueiam o receptor, eles o *acionam*, imitando o hormônio hipofisário. O resultado é uma tireoide que produz hormônio continuamente, fora da alça de retroalimentação que normalmente a regula: como o estímulo não vem da hipófise, a queda da tireotrofina não desliga nada, e a glândula segue funcionando a todo vapor. O paciente desenvolve hipertireoidismo com tireotrofina suprimida e hormônio tireoidiano alto — combinação que, à primeira vista, parece contradizer o controle endócrino, e que só faz sentido quando se percebe que quem está estimulando a glândula é o anticorpo.
])

#subtopico("3.3 — A divisão do trabalho entre as classes: IgM abre, IgG amadurece, IgE e IgA para situações especiais")

Uma resposta imune enfrenta problemas diferentes em momentos diferentes, e a existência de várias classes de anticorpo é a solução do organismo para isso. Cada classe é a mesma capacidade de reconhecimento acoplada a um conjunto distinto de propriedades efetoras, e a lógica de quando cada uma aparece é surpreendentemente prática.

No começo da resposta o problema é de sensibilidade: os clones ainda não foram selecionados, e os receptores disponíveis encaixam mal no antígeno. A IgM resolve isso pela geometria. Ela é um #termo-nota[pentâmero][arranjo de cinco unidades tetraméricas ligadas entre si; multiplica por cinco o número de sítios de ligação da molécula] — cinco tetrâmeros reunidos numa única estrutura. Como cada tetrâmero tem dois sítios de ligação, a IgM apresenta dez sítios ao antígeno, e a imagem que descreve isso é literal: não é uma mão segurando, são dez. Ainda que cada mão segure fraco, o conjunto segura firme. Essa força somada é a avidez, e ela é exatamente o que se precisa quando a qualidade individual do encaixe ainda é baixa.

A segunda propriedade da IgM combina com a mesma fase. Ela ativa o complemento com grande eficiência, e ativar complemento gera inflamação. No início de uma infecção, inflamar é desejável: é assim que se recrutam células e moléculas para o local. A IgM, portanto, é o anticorpo que agarra mesmo com encaixe ruim e faz barulho — e as duas coisas servem ao mesmo objetivo.

Depois, o problema muda. Com o processo já instalado, o objetivo deixa de ser gerar alarme e passa a ser limpar a área sem destruir o tecido. É o momento da IgG, e as vantagens dela se encaixam uma a uma nesse novo objetivo. Ela é excelente opsonina e leva à fagocitose sem depender do complemento, isto é, remove o alvo sem acrescentar inflamação. Ela é monomérica e portanto muito menor que a IgM pentamérica, o que lhe permite penetrar nos tecidos livremente — enquanto a IgM, grande, só alcança um tecido cuja permeabilidade vascular já tenha aumentado. E ela persiste no soro com meia-vida longa, o que faz da IgG o suporte material da memória humoral: em um segundo contato produz-se de novo IgM e IgG, mas a IgG sobe muito mais e é ela que domina a resposta.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-10.png",
  largura: 72%,
  legenda: [À esquerda, a cinética das duas classes: na resposta primária a IgM sobe primeiro e a IgG vem atrás e modesta; na secundária a IgG dispara e domina. À direita, o mesmo fenômeno no nível celular — o plasmócito que fabricava IgM passa a fabricar IgG, com a mesma especificidade e a mesma afinidade.])

Duas situações escapam desse par e exigem classes próprias. A primeira é a emergência que pede reação violenta: expulsar um verme do intestino exige movimento intestinal intenso, e expelir um agente das vias aéreas exige tosse e espirro. A classe encarregada disso é a IgE, e ela foi difícil de encontrar precisamente porque quase não circula — fica ancorada, pelo Fc, em células que carregam os mediadores capazes de provocar essas reações musculares e vasculares abruptas. A IgE foi descrita a partir da doença, não da fisiologia: quando o organismo produz IgE contra substâncias inofensivas do ambiente, a mesma maquinaria de expulsão dispara sem alvo legítimo, e isso é a reação de hipersensibilidade que se chama alergia. Contra um helminto, a mesma reação é imunidade.

A segunda situação é o oposto exato. Há territórios em que inflamar é catastrófico: inflamar o pulmão compromete a troca gasosa, e inflamar a mucosa intestinal compromete a absorção e leva à desnutrição. Ainda assim esses territórios precisam de proteção, e a solução é a IgA. Ela existe para ser secretada: as células das mucosas capturam a IgA produzida na submucosa ou circulante, transportam-na através do epitélio e a lançam na luz. O único sítio de secreção que não é mucosa é a glândula mamária — e mesmo ali o destino final é a mucosa do lactente. Na luz, a IgA associa-se a uma cadeia polipeptídica adicional que estabiliza o complexo e o protege da digestão, e frequentemente aparece como dímero em vez de monômero, montagem que ocorre depois da produção.

O mecanismo de proteção da IgA é o que faz dela uma imunoglobulina anti-inflamatória por desenho: ela neutraliza vírus e toxinas e bloqueia a aderência de bactérias *na luz*, antes que qualquer coisa atravesse o epitélio. Ela impede a confusão de começar, em vez de ter de administrá-la depois. E há um dado quantitativo que ilustra a prioridade do organismo: a IgA é a imunoglobulina mais produzida no corpo — sintetizada e descartada continuamente nas secreções —, ainda que a IgG seja a mais concentrada no soro. O sistema imune gasta a maior parte de sua energia produzindo um anticorpo preventivo, cuja função é evitar a briga.

#table(
  columns: (auto, auto, 1fr, 1fr),
  inset: 8pt,
  align: left,
  stroke: 0.5pt + gray-border,
  table.header(
    [*Classe*], [*Forma*], [*Momento e lugar*], [*O que a torna adequada ali*],
  ),
  [IgM], [Pentâmero], [Início da resposta, no plasma], [Dez sítios somam avidez alta mesmo com afinidade baixa; ativa complemento com eficiência e gera o alarme inflamatório],
  [IgG], [Monômero], [Resposta madura e memória; soro e tecidos], [Opsoniza sem depender do complemento, atravessa para os tecidos e a placenta, meia-vida longa],
  [IgE], [Monômero], [Ancorada em células de mucosa e conjuntivo], [Dispara reação de expulsão rápida — útil contra helminto, patológica contra alérgeno],
  [IgA], [Monômero ou dímero], [Secreções: luz intestinal, vias aéreas, leite], [Neutraliza e bloqueia aderência sem inflamar; cadeia adicional a protege da digestão],
  [IgD], [Monômero], [Membrana do linfócito B, ao lado da IgM], [Funciona como receptor; praticamente não é secretada e não tem função efetora conhecida],
)

A IgD fecha a lista pelo que não faz. Ela não é secretada em quantidade significativa — o pouco que se encontra no sangue parece vazamento — e opera essencialmente como receptor de membrana, ao lado da IgM, no linfócito B maduro. O linfócito B produz primeiro IgM; ao amadurecer, passa a exibir IgM e IgD simultaneamente na membrana. Na hora de secretar, ele ou vira um plasmócito de IgM, ou realiza a troca de classes — depois de conversar com o linfócito T — e passa a produzir IgG, IgE ou IgA. Trocar de classe *para* IgD não faz parte do repertório normal, e concentração alta de IgD no soro é achado de doença, não de fisiologia.

#clinica-box("Anticorpo materno: a janela de proteção do recém-nascido", [
  As propriedades de transporte da IgG e da IgA se somam em uma consequência que se observa direto no berçário. Durante a gestação, a IgG materna atravessa a placenta e o recém-nascido chega ao mundo com um repertório emprestado, que reflete o que a mãe já encontrou na vida. Esse empréstimo decai ao longo dos primeiros meses, à medida que as moléculas maternas são catabolizadas e antes que a produção própria do lactente esteja madura — e é nessa depressão que a suscetibilidade a infecções aumenta. O colostro e o leite acrescentam a outra camada, agora de IgA, que não é absorvida para a circulação: ela permanece na luz intestinal e protege a superfície mucosa exatamente onde o lactente é mais exposto. Uma classe cobre o compartimento interno, a outra cobre a interface com o mundo — e as duas juntas sustentam a criança até que ela produza as suas.
])

#subtopico("3.4 — Avidez não é afinidade, e nenhuma das duas é especificidade")

Esta é a inversão que mais vale guardar de todo o resumo, e ela existe porque três palavras que soam parecidas medem coisas diferentes. A especificidade responde *contra qual* molécula o anticorpo se dirige. A afinidade responde *com que força* um único sítio de ligação segura aquela molécula. A avidez responde *com que força a molécula inteira* segura o alvo, somando todos os sítios que ela consegue engajar ao mesmo tempo.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-15.png",
  largura: 54%,
  legenda: [O aviso riscado sobre a lista de isotipos é literal: nada do que está listado ali — classe, subclasse, alotipo, idiotipo público — altera contra o que o anticorpo se dirige.])

A partir dessas definições, a conclusão é imediata: o tipo de imunoglobulina não afeta a especificidade nem a afinidade. Ambas são propriedades do sítio de ligação, que é construído pelas porções variáveis; a troca de classes mexe na porção constante da cadeia pesada e deixa a variável intacta. O que o isotipo afeta é a avidez, e afeta por geometria pura: a IgM tem dez sítios, a IgG tem dois, logo a IgM segura com força global maior mesmo que cada sítio individual seja igual ou pior.

#atencao-box("A IgG não tem mais afinidade que a IgM", [
  A leitura tentadora, e errada, é a seguinte: como a resposta começa com IgM e amadurece para IgG, e como a resposta melhora com o tempo, a IgG deve ter maior afinidade pelo antígeno. A conclusão não decorre das premissas. Duas coisas distintas acontecem em paralelo ao longo de uma resposta humoral, e confundi-las produz exatamente esse erro. Uma é a troca de classes, que substitui a porção constante e altera função efetora — ela não toca no sítio de ligação e portanto não muda afinidade. A outra é a maturação de afinidade, que atua sobre a porção *variável* e de fato aumenta a força do sítio, mas é um processo independente do isotipo: uma IgM pode ter alta afinidade e uma IgG pode ter baixa. Ler a maturação de afinidade como consequência da troca de classe é atribuir a uma mudança no tronco da molécula um efeito que só acontece na ponta.
])

#mini-resumo[
  Se você só lembrar de uma coisa: especificidade e afinidade moram no sítio, que a porção variável constrói; avidez mora na molécula inteira, e é a única das três que o isotipo consegue mudar.
]

#subtopico("3.5 — De onde vem a diversidade: recombinação somática e o receptor restrito do linfócito T")

O paradoxo aberto na PARTE II volta agora com todos os elementos para ser resolvido. A pergunta é como se gera um repertório completo — um receptor para cada molécula que possa eventualmente aparecer — e a primeira hipótese disponível era a mais direta: o genoma carregaria um gene pronto para cada especificidade possível. A objeção decisiva não é de espaço, é de manutenção. Um gene que nunca é usado não sofre pressão seletiva; ao longo de milhares de anos ele acumula mutações e deixa de codificar uma proteína funcional. Quando finalmente aparecesse o antígeno para o qual aquele gene existia, ele já não serviria. Guardar tudo pronto no genoma é uma estratégia que se degrada exatamente naquilo que deveria preservar.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-16.png",
  largura: 78%,
  legenda: [Os quatro quadrantes reconstroem o argumento na ordem em que ele foi montado: o problema de guardar o repertório no genoma, a pista deixada por Dreyer e Bennett, a hipótese somática de Jerne e a demonstração experimental de Tonegawa. Os dois Nobel embaixo marcam o desfecho.])

A saída veio da pista deixada por Dreyer e Bennett. Se proteínas de mielomas diferentes compartilham um trecho idêntico e diferem em outro, e se o mesmo padrão reaparece na resposta imune normal sob a forma da troca de classes — uma IgM contra o antígeno X que vira uma IgG contra o mesmo antígeno X —, então a associação entre porção constante e porção variável é flexível de um modo que a leitura contínua de um gene não explica. Niels Jerne propôs, em 1971, a solução que essa flexibilidade exigia: o reconhecimento imune teria geração *somática*. Isto é, as células germinativas carregariam um número pequeno de segmentos variáveis, e a diversidade seria produzida nas células somáticas por algum mecanismo que ninguém ainda conhecia. A ideia era tão contrária ao consenso que ele precisou fundar uma revista para publicá-la.

Cinco anos depois, Susumu Tonegawa demonstrou o mecanismo. Ele comparou a posição dos segmentos gênicos em células comuns e em linfócitos, e encontrou a diferença: o segmento que codifica a porção variável fica *longe* da porção constante em todas as outras células do organismo, mas nos linfócitos os dois estão próximos. O genoma do linfócito foi rearranjado. O que na célula germinativa está separado, no linfócito se aproximou — e essa aproximação é um evento somático, que acontece durante a diferenciação da célula e não é herdado. Detalhando um pouco mais o que se estabeleceu depois: a porção variável não é um bloco único que se desloca, e sim o produto da união de vários segmentos gênicos distintos, sorteados e recombinados. É dessa combinatória que sai a diversidade, e a mecânica fina dela — quais segmentos, quais regras, que enzimas — é assunto de uma aula própria. Os dois receberam o Nobel: Jerne pela ideia, Tonegawa pela demonstração.

O receptor do linfócito T levantou o mesmo problema com uma dificuldade adicional, e o adjetivo que a literatura lhe deu registra bem essa dificuldade: elusivo, isto é, esquivo. O motivo é mecanístico. O anticorpo, quando secretado, vai até o antígeno e se liga a ele — logo, basta procurar o que gruda no antígeno. O #sigla("TCR", [receptor de antígeno do linfócito T, do inglês _T cell receptor_ — só reconhece fragmento peptídico apresentado por molécula do complexo principal de histocompatibilidade]) não faz isso. Ele só reconhece o antígeno quando um fragmento dele está apresentado por uma molécula codificada pelo complexo principal de histocompatibilidade, o #sigla("HLA", [antígenos leucocitários humanos, do inglês _human leukocyte antigen_ — o nome do complexo principal de histocompatibilidade na espécie humana]) na espécie humana. Essa exigência é o que se chama restrição, e ela foi imposta no timo durante a seleção: sobreviveram apenas os linfócitos T capazes de reagir com as moléculas de apresentação do próprio hospedeiro. Um receptor que só funciona acoplado a outra molécula não pode ser encontrado por um ensaio de ligação simples.

#figura-nebli("/figuras/imuno-17-reconhecimento-adaptativa/slide-17.png",
  largura: 62%,
  legenda: [Os dois trabalhos que resolveram o problema por caminhos diferentes: à esquerda, o anticorpo monoclonal de Allison contra um antígeno tumor-específico do linfoma T; à direita, o isolamento dos clones de cDNA específicos do linfócito T pelo grupo de Davis.])

Duas estratégias resolveram o impasse, e ambas exploram a mesma propriedade — clonalidade. James Allison partiu de um linfoma T, isto é, de um clone único expandido, e produziu anticorpos contra ele. A maior parte dos anticorpos gerados assim reage com moléculas comuns a todos os linfócitos e não serve para nada; o que ele conseguiu foi um anticorpo que reconhecia *apenas aquele* linfoma, e não outro linfoma T qualquer. Reconhecer só um clone é, por definição, reconhecer o receptor clonal — o alvo tinha sido encontrado. A confirmação definitiva veio dois anos depois, com o grupo de Mark Davis, por um raciocínio de subtração: partindo do pressuposto de que linfócitos B e T compartilham a maior parte de sua expressão gênica, eles retiraram do material do linfócito T tudo o que também existia no linfócito B. O resto — uma fração pequena de #sigla("RNA", [ácido ribonucleico — aqui, o conjunto de transcritos que a célula está expressando naquele momento]) — continha o que é exclusivo do linfócito T, e ali estava o gene do receptor.

O fecho do argumento é a convergência dos dois sistemas. O receptor do linfócito B e o receptor do linfócito T são gerados pelo mesmo mecanismo de recombinação somática de segmentos gênicos; o que os separa é o critério de seleção aplicado depois. Para o linfócito B, o critério é essencialmente um: reagir ou não reagir com o próprio, presente durante a geração do repertório. Para o linfócito T existe um critério anterior e adicional — ele precisa ser capaz de enxergar no contexto das moléculas de apresentação do hospedeiro. Mesma máquina de diversidade, filtros diferentes na saída.

#conclusao-box[
  Um único princípio organiza esta aula inteira, e ele é contraintuitivo: o sistema imune adaptativo não é projetado para reconhecer inimigos, e sim para gerar variedade sem plano e depois subtrair dela o que aponta para dentro. Repertório completo sorteado ao acaso, poda contra o próprio nos órgãos linfoides primários, distribuição clonal — tudo o mais decorre dessa arquitetura de excesso seguido de filtragem.

  O mecanismo nuclear que a torna possível é a separação entre uma porção variável e uma porção constante dentro da mesma cadeia polipeptídica. Foi essa separação que Dreyer e Bennett encontraram nas proteínas de mieloma, é ela que a troca de classes explora na resposta normal, e é ela que a recombinação somática de segmentos gênicos produz no precursor do linfócito. A consequência funcional atravessa todo o resumo: a porção variável constrói o sítio de ligação e define especificidade e afinidade; a porção constante define transporte, opsonização, ativação de complemento e ativação celular. Quando o organismo troca IgM por IgG, ou por IgE, ou por IgA, ele não muda o alvo — muda o que fará ao encontrá-lo, e é por isso que uma mesma resposta pode inflamar no começo, limpar no meio e proteger a mucosa sem inflamar.

  A clínica que apareceu ao longo do caminho é a mesma lógica vista de outro ângulo. O mieloma múltiplo produz muita imunoglobulina e pouquíssima variedade, e é a variedade que protege — daí a imunodeficiência de um paciente com gama alta. A doença de Graves mostra o que acontece quando a porção variável encontra um receptor hormonal e a porção constante ativa a célula: hormônio produzido fora da alça de retroalimentação. E o recém-nascido vive alguns meses com um repertório emprestado, IgG pela placenta e IgA pelo leite, porque o transporte epitelial depende do Fc e independe de o antígeno estar ligado.

  Fica um fio explicitamente pendente, e ele é o próximo passo natural. Sabemos agora *que* os segmentos gênicos da porção variável são separados no genoma germinativo e aproximados no linfócito; não vimos ainda *como* — quais segmentos participam, que regras governam a combinação, que maquinaria enzimática corta e junta, e como o acaso da junção acrescenta ainda mais diversidade. É esse detalhamento que transforma "houve um rearranjo" em um mecanismo, e ele explica de quebra por que a maturação de afinidade e a troca de classes são fenômenos distintos, com enzimas distintas, atuando em pontos distintos do mesmo lócus.
]
