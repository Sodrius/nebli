#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Uma bactéria no seu intestino carrega mais ou menos quatro mil genes e, a qualquer momento, usa uma fração pequena deles. Fabricar proteína é a coisa mais cara que uma célula faz: cada ligação peptídica custa energia, ocupa um ribossomo e consome aminoácidos que poderiam virar outra coisa. Uma bactéria que produzisse todas as suas enzimas o tempo todo seria varrida por qualquer vizinha que só produzisse o necessário. É por isso que existe regulação — e, em procariotos, ela se concentra quase toda num único ponto: a decisão de iniciar ou não a transcrição de um bloco de genes.

Este resumo constrói esse mecanismo em três movimentos. Na PARTE I montamos a peça de hardware: o que é um operon, como o DNA bacteriano é pontuado e por que uma sequência de DNA e uma proteína reguladora obedecem a regras opostas. Na PARTE II entra o controle negativo — o repressor que segura o operon desligado, a molécula que o solta, e a genética de bancada que provou tudo isso antes de existir sequenciamento. Na PARTE III entra o controle positivo, que é onde o modelo fica realmente interessante: um promotor deliberadamente fraco, um ativador que responde ao nível de açúcar, e uma decisão que só sai ligada quando duas condições independentes são satisfeitas ao mesmo tempo.
]

#parte-title("PARTE I — A lógica do operon e a gramática do DNA bacteriano", primeira: true)

#subtopico("1.1 — Por que uma bactéria regula, e quanto ela regula")

Regular expressão gênica é decidir quanto de cada proteína existe na célula num dado momento. Em bactéria, essa decisão é tomada quase inteiramente na largada: a célula controla se a #sigla("RNAP", [RNA polimerase — enzima que copia uma fita de DNA em RNA]) inicia ou não a transcrição de um trecho do genoma. Não há núcleo separando transcrição de tradução, o mRNA bacteriano dura poucos minutos e o ribossomo começa a traduzir a extremidade 5' enquanto a polimerase ainda copia a 3'. Quem controla a iniciação controla, na prática, tudo o que vem depois.

O ganho é energético e é grande. Uma #emph[Escherichia coli] crescendo em glicose não tem nenhum motivo para fabricar a enzima que quebra lactose: seriam mil e poucos aminoácidos gastos por molécula de enzima, multiplicados por milhares de cópias, para catalisar uma reação cujo substrato não está lá. Quando a lactose aparece e a glicose acaba, a mesma célula precisa dessa enzima em minutos. Regulação é o que permite os dois comportamentos no mesmo genoma.

A amplitude dessa regulação é o número que vale guardar: *a transcrição do bloco da lactose cai cerca de mil vezes quando o açúcar está ausente*. Mil vezes, não infinitas vezes. Essa distinção parece detalhe e não é — o resíduo que sobra no estado desligado tem função, e vamos precisar dele em 2.2 para explicar como o sistema consegue sair do repouso. Guarde por enquanto que "operon desligado" significa transcrição residual, nunca transcrição nula.

#mini-resumo[Proteína é cara → a bactéria só fabrica o que o meio pede → o ponto de controle é a iniciação da transcrição → a amplitude é de ~1000×, não de zero a tudo.]

#subtopico("1.2 — A pontuação do DNA bacteriano e o mRNA policistrônico")

Um texto sem pontuação é ilegível não porque falte conteúdo, mas porque falta a marcação de onde cada unidade começa e termina. O DNA tem o mesmo problema, e o resolve com sinais de sequência que a maquinaria lê como pontuação. O #termo-nota[promotor][trecho de DNA a montante do gene onde a RNA polimerase se posiciona antes de começar a copiar] é o sinal de início: é ali que a polimerase pousa. A primeira base efetivamente copiada recebe o número +1, e tudo que está antes dela ganha coordenada negativa — o que estiver 35 pares de base antes do início é a posição -35. No fim do trecho há um terminador, que sinaliza à polimerase para soltar o molde.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-04.png",
  largura: 52%,
  legenda: [A pontuação mínima de uma unidade transcricional: promotor, o sítio +1 de início e o terminador. Toda coordenada que aparecer daqui pra frente conta a partir do +1.])

O detalhe que separa bactéria de célula humana é o que cabe entre um promotor e um terminador. Em eucariotos, a regra geral é um promotor para um gene. Em bactéria, um único promotor pode servir a vários genes enfileirados, e a transcrição atravessa todos eles de uma vez, produzindo um mRNA único que carrega várias mensagens em sequência — um #termo-nota[mRNA policistrônico][RNA mensageiro que contém as sequências codificantes de mais de uma proteína, transcritas a partir de um só promotor]. É essa arquitetura que permite coordenar genes: se as três enzimas de uma via metabólica estão no mesmo transcrito, ligar uma é necessariamente ligar as três.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-05.png",
  largura: 64%,
  legenda: [Um mRNA, três proteínas. Repare que cada trecho codificante tem seu próprio sítio de ligação ao ribossomo (RBS) e seus próprios códons de início e parada — o mRNA não vira uma proteína gigante que depois é cortada.])

Vale desfazer aqui uma leitura errada que atrapalha adiante. O mRNA policistrônico não é traduzido como uma proteína grande que depois é clivada; cada trecho codificante tem seu próprio #sigla("RBS", [sítio de ligação ao ribossomo — sequência curta antes do códon de início que recruta a subunidade menor do ribossomo]), seu códon de início e seu códon de parada, e o ribossomo entra em cada um deles de forma independente. *A consequência é fina e é útil:* como cada RBS tem eficiência própria, e como o mRNA vai sendo degradado a partir de uma das extremidades, os genes de um mesmo operon não geram quantidades iguais de proteína. No bloco da lactose, a primeira enzima sai em quantidade muito maior que a última, mesmo saindo do mesmo transcrito.

A esse conjunto — promotor, sítios de controle e genes estruturais transcritos juntos — dá-se o nome de *operon*. É a resposta bacteriana ao problema de coordenar genes funcionalmente relacionados, e é simples justamente porque o mecanismo está todo no DNA contíguo.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-06.png",
  largura: 62%,
  legenda: [O operon do triptofano: um promotor, cinco genes estruturais, um mRNA, cinco enzimas de uma mesma via biossintética. Coordenar aqui não exige nada além de estarem juntos.])

#subtopico("1.3 — A regra que resolve o resto: sequência age em cis, proteína age em trans")

Aqui está o conceito que separa quem entende o operon de quem decorou o operon. Dentro de uma unidade regulada convivem duas classes de elementos que se comportam de maneiras opostas, e confundir as duas torna impossível prever o efeito de qualquer mutação.

A primeira classe é de *sequências de DNA*: o promotor, o sítio onde uma proteína reguladora se encaixa, o operador. Elas não são transcritas em nada útil — são endereços. Um endereço não sai do lugar. Se ele estiver estragado, o estrago afeta apenas os genes que estão naquela mesma molécula de DNA, porque não existe forma de um endereço de uma molécula influenciar outra molécula. Diz-se que essas sequências agem em #termo-nota[cis][do latim "do mesmo lado" — um elemento que só influencia os genes fisicamente ligados a ele, na mesma molécula de DNA]: só do próprio lado.

A segunda classe é de *genes reguladores*: trechos que são transcritos e traduzidos, e cujo produto é uma proteína. Proteína é difusível. Uma vez sintetizada, ela solta do ribossomo e circula pelo citoplasma inteiro, encontrando qualquer sítio compatível em qualquer molécula de DNA que esteja na célula. Diz-se então que o produto age em *trans*, "do outro lado" — a distância física é irrelevante.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-42.png",
  largura: 78%,
  legenda: [As duas classes lado a lado. À esquerda, o gene regulador produz ativador ou repressor, que difundem. À direita, sítio do ativador e operador são endereços fixos no DNA, imediatamente antes dos genes estruturais A, B e C. Endereço não difunde; produto difunde.])

*O ponto fino é que cis e trans não têm nada a ver com distância.* Um operador colado ao gene e um sítio de ligação a 200 pares de base dele são igualmente cis. O gene regulador do bloco da lactose fica logo ao lado do próprio operon, mas isso é acidente do arranjo do genoma: funcionalmente ele poderia estar do outro lado do cromossomo, ou até num plasmídeo separado, e continuaria funcionando exatamente igual, porque o que ele exporta é proteína.

#atencao-box("Cis e trans não são posições, são naturezas",
  [A confusão que mais estraga previsão de fenótipo é ler cis/trans como "perto/longe". Não é geografia, é o tipo de coisa que o elemento produz. Sequência de DNA que serve de sítio de ligação age *sempre* em cis, esteja onde estiver, porque um sítio não se desprende do DNA. Gene que codifica proteína reguladora age *sempre* em trans, esteja onde estiver, porque a proteína se desprende do ribossomo. Fixar isso agora resolve sozinho toda a PARTE II: para qualquer mutante novo, a primeira coisa a perguntar não é "onde está a mutação", é "o elemento mutado é endereço ou é produto".])

#subtopico("1.4 — O operon lac, peça por peça")

Com o vocabulário montado, o sistema concreto fica fácil de ler. O bloco da lactose de #emph[E. coli] é o exemplo canônico porque foi nele que o modelo nasceu, e porque ele contém, ao mesmo tempo, um exemplar de cada elemento descrito acima.

Os genes estruturais são três, transcritos num mRNA único. O #emph[lacZ] codifica a #termo-nota[β-galactosidase][enzima que hidrolisa a ligação entre a galactose e a glicose da lactose, liberando os dois monossacarídeos], a enzima que corta a lactose em galactose e glicose. O #emph[lacY] codifica a lactose-permease, o transportador de membrana que traz lactose de fora para dentro. O #emph[lacA] codifica uma transacetilase, de papel acessório na eliminação de galactosídeos que a célula não consegue metabolizar. Note a lógica: o transportador que traz o substrato e a enzima que o quebra estão sob o mesmo interruptor — não faria sentido ter um sem o outro.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-15.png",
  largura: 80%,
  legenda: [O operon completo, com o tamanho real de cada trecho em pares de base. Repare em duas coisas: o #emph[lacI] tem promotor próprio (o P à esquerda) e não faz parte do transcrito do operon; e o operador ocupa apenas 82 pares de base entre o promotor e o início do #emph[lacZ] — pouca sequência para um efeito de mil vezes.])

À frente deles estão os elementos em cis. O promotor do operon, chamado P#sub[lac], é onde a polimerase pousa. O #termo-nota[operador][sequência curta de DNA, sobreposta ao início da transcrição, onde o repressor se encaixa e bloqueia a saída da polimerase] fica logo depois, sobreposto ao ponto de início da transcrição — essa sobreposição é o que torna a repressão possível, e voltamos a ela em 2.1. E, mais a montante, por volta da posição -61, há um terceiro endereço: o sítio de ligação do ativador, o sítio CAP, que fica guardado para a PARTE III.

Fora do operon, com promotor próprio e transcrição contínua e independente, está o #emph[lacI] — o gene regulador. Ele é transcrito o tempo todo, num nível baixo e constante, e seu produto é o repressor Lac. Como todo produto proteico, ele age em trans. *É a única peça do sistema que não obedece ao interruptor que ela mesma controla.*

#mini-resumo[Três genes estruturais num transcrito (lacZ, lacY, lacA) · três endereços em cis a montante (sítio CAP, promotor, operador) · um gene regulador fora do operon (lacI) cujo produto difunde. Toda a PARTE II é sobre o que o produto do lacI faz com o operador.]

#parte-title("PARTE II — Controle negativo: o repressor como sensor, e a genética que provou")

#subtopico("2.1 — O que exatamente o repressor bloqueia")

O repressor Lac é uma proteína montada a partir de quatro cópias idênticas da cadeia codificada pelo #emph[lacI] — um tetrâmero. Essa estrutura quaternária não é detalhe decorativo: ela tem duas consequências que vão aparecer em 2.5 e 2.6, e que explicam comportamentos genéticos que de outra forma pareceriam arbitrários. Por ora basta a função: cada tetrâmero tem domínios que reconhecem a sequência do operador e se encaixam nela com afinidade altíssima.

Com o operador ocupado, a transcrição do operon despenca. A pergunta que importa é *como* — e é aqui que a intuição da maioria dos alunos erra o alvo.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-09.png",
  largura: 72%,
  legenda: [O repressor Lac produzido pelo #emph[lacI] difunde e se encaixa no operador, imediatamente a jusante do promotor. Os três genes estruturais deixam de ser transcritos ao mesmo tempo — coordenação sem nenhum mecanismo adicional.])

A imagem intuitiva é a de um tampão que impede a polimerase de encostar no DNA. Não é isso. O operador não fica sobre o promotor: fica *depois* dele, sobreposto ao ponto de início da transcrição e ao começo do trecho transcrito. A polimerase continua reconhecendo e ocupando o promotor normalmente. O que ela não consegue fazer é o passo seguinte — abrir a dupla-hélice para formar a bolha de transcrição e escapar do promotor para o alongamento. O repressor age como uma trava física logo à frente da linha de partida, não como um muro em volta dela.

#atencao-box("O repressor não impede o pouso da polimerase",
  [Descrever a repressão como "a polimerase não consegue se ligar" inverte o mecanismo e destrói a previsão de qualquer experimento posterior. A polimerase se liga; ela é que fica presa. Por que isso importa na prática: se o bloqueio fosse a ligação, um promotor mais forte compensaria a repressão, e não compensa. E o modelo errado também não explica o vazamento de ~1/1000 que o sistema tem, que existe justamente porque uma polimerase já posicionada eventualmente escapa quando o repressor se desprende por um instante.])

Esse vazamento merece uma frase a mais, porque é a peça que faz o sistema inteiro funcionar. A ligação do repressor ao operador é reversível: ela tem uma constante de dissociação muito baixa, mas não é zero. O tetrâmero solta e volta a se ligar continuamente, e a cada janela em que ele está solto uma polimerase que já estava posicionada consegue escapar. É por isso que a repressão dá mil vezes e não dez mil vezes, e por isso que sempre há um punhado de moléculas de permease e de β-galactosidase na célula mesmo no estado desligado.

#subtopico("2.2 — O indutor é a alolactose, e é por isso que o sistema consegue arrancar")

Se o repressor fica preso ao operador com afinidade tão alta, alguma coisa precisa tirá-lo de lá quando a lactose aparece. A resposta imediata seria "a lactose tira" — e essa resposta está errada de um jeito que vale a pena entender, porque o erro esconde o mecanismo mais elegante da aula.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-11.png",
  largura: 56%,
  legenda: [Lactose ausente: o tetrâmero ocupa o operador e o operon fica no nível residual.])

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-13.png",
  largura: 56%,
  legenda: [Indutor presente: ele se liga ao repressor num sítio próprio, longe do domínio de DNA. A mudança de forma resultante derruba a afinidade pelo operador, e o tetrâmero se solta — sem nunca competir pelo mesmo sítio.])

Quem se liga ao repressor é a #termo-nota[alolactose][isômero da lactose em que a galactose está unida ao carbono 6 da glicose em vez do carbono 4; é o indutor fisiológico do operon], um isômero da lactose. E a alolactose não vem de fora: ela é produzida dentro da célula pela própria β-galactosidase, que além de cortar a lactose também catalisa, numa fração das vezes, a transferência da galactose para outra posição da glicose. A enzima que o operon codifica é a mesma que fabrica o sinal que liga o operon.

Isso monta um problema circular que vale enunciar em voz alta: para produzir alolactose é preciso ter β-galactosidase; para ter β-galactosidase é preciso que o operon esteja ligado; para ligar o operon é preciso alolactose. Se o estado desligado fosse mesmo zero, o sistema jamais arrancaria. *É exatamente aqui que aquele resíduo de 1/1000 deixa de ser detalhe e vira o mecanismo.* As poucas moléculas de permease que existem no estado reprimido trazem as primeiras lactoses para dentro; as poucas moléculas de β-galactosidase convertem parte delas em alolactose; a alolactose solta alguns repressores; mais transcrição acontece; mais permease e mais enzima aparecem; e a alça se retroalimenta até o operon estar plenamente induzido em poucos minutos.

O modo de ação da alolactose sobre o repressor é alostérico, e a distinção importa. Ela não disputa o operador com o repressor, nem o arranca à força. Ela se encaixa num sítio próprio do tetrâmero, distante do domínio que reconhece o DNA, e a mudança de conformação que essa ligação provoca reposiciona os domínios de DNA de forma que eles deixam de encaixar bem no operador. A afinidade cai algumas ordens de grandeza e o repressor se solta sozinho.

#confusao-prevista(
  titulo: "Lactose não é indutor; alolactose é",
  aluno_acha: [aluno acha que a lactose que entra na célula se liga ao repressor e o retira do operador],
  mecanismo: [a lactose precisa antes ser convertida em alolactose pela própria β-galactosidase. Só a alolactose tem geometria compatível com o sítio alostérico do repressor. A consequência experimental é direta: mutante sem β-galactosidase funcional não induz o operon com lactose, mesmo tendo repressor e operador perfeitos — porque nunca fabrica o indutor.],
)

Há ainda um indutor artificial que aparece em toda bancada e que resolve esse problema por atalho: o #sigla("IPTG", [isopropil-β-D-tiogalactosídeo — análogo sintético da alolactose que induz o operon sem ser metabolizado]). O IPTG tem forma parecida o bastante com a alolactose para ocupar o sítio alostérico do repressor, mas a β-galactosidase não consegue quebrá-lo, porque a ligação glicosídica foi trocada por uma ligação com enxofre. Ele entra, induz e permanece — indução constante, sem consumo, sem depender de ter enzima ativa. Por isso ele é chamado de indutor gratuito.

#mini-resumo[O operon não é induzido pelo substrato bruto, e sim por um isômero que a própria enzima do operon fabrica. Sem expressão basal, o circuito não teria como começar. O IPTG é o atalho de bancada porque induz sem ser metabolizado.]

#subtopico("2.3 — Como se enxerga o operon funcionando: X-Gal, IPTG e a placa azul e branca")

Nada do que foi dito acima seria demonstrável se não houvesse um jeito de olhar para uma colônia de bactérias e saber, a olho nu, se a β-galactosidase está sendo produzida ali. O truque é dar à enzima um substrato falso que, ao ser cortado, libera um pigmento.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-19.png",
  largura: 68%,
  legenda: [O X-Gal é um galactosídeo com um indol preso no lugar da glicose. A β-galactosidase corta a ligação, o indol liberado dimeriza espontaneamente e oxida, e o produto é um pigmento índigo insolúvel que fica retido na colônia. Colônia azul significa enzima presente; colônia branca significa enzima ausente ou inativa.])

O X-Gal é *substrato*, não indutor — ele revela a enzima que já existe, e não faz nada para que ela passe a existir. Quem induz é o IPTG, que é adicionado junto. Os dois cumprem funções diferentes e complementares no mesmo meio de cultura: o IPTG força o operon a ligar, o X-Gal denuncia se ele ligou. É por isso que um meio de triagem carrega os dois.

A leitura da placa exige um cuidado. Colônia azul é conclusiva num sentido só: há β-galactosidase ativa, logo o operon está sendo expresso. Colônia branca é ambígua por natureza — ela apenas informa que não há atividade enzimática, e isso pode ter várias causas mecanísticas distintas: o gene #emph[lacZ] pode estar mutado, o promotor pode estar destruído, o repressor pode ter perdido a capacidade de responder ao indutor, o sítio do ativador pode estar inutilizado. *A placa é um filtro, não um diagnóstico.* Foi combinando esse filtro simples com variação sistemática das condições de cultura — com e sem glicose, com e sem indutor — que Jacob e Monod, no Instituto Pasteur, extraíram o modelo inteiro no começo dos anos 1960, muito antes de existir qualquer método de leitura direta de sequência.

#clinica-box("O mesmo pigmento, meio século depois, no laboratório de rotina",
  [A triagem azul-e-branca não ficou na história da genética: ela é a base de boa parte da clonagem molecular usada até hoje para produzir proteínas recombinantes de uso clínico, como insulina humana e fatores de coagulação. O plasmídeo receptor carrega o começo do #emph[lacZ]; quando um fragmento estranho de DNA é inserido exatamente ali, o gene é interrompido e a bactéria perde a β-galactosidase funcional. Na placa com X-Gal e IPTG, as colônias que receberam o inserto ficam brancas e as que apenas recircularizaram o plasmídeo vazio ficam azuis. O pesquisador escolhe as brancas a olho nu. O mecanismo que se está usando é exatamente o desta aula — expressão do operon revelada por substrato cromogênico —, aplicado como ferramenta de seleção.])

#subtopico("2.4 — Dois caminhos para o mesmo fenótipo constitutivo")

Jacob e Monod isolaram mutantes que perderam a regulação: bactérias que produziam β-galactosidase o tempo todo, com ou sem lactose no meio. Esse comportamento recebeu o nome de expressão *constitutiva* — sem controle pelo sinal. O achado decisivo foi que existiam dois tipos de mutante constitutivo, indistinguíveis na placa e completamente diferentes por dentro.

O primeiro tipo tem mutação no operador. A sequência continua no lugar, mas foi alterada o bastante para que o repressor não a reconheça mais. Chama-se O#super[c], de operador constitutivo. O repressor produzido é perfeitamente funcional — ele simplesmente não tem mais onde se encaixar naquele trecho de DNA.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-20.png",
  largura: 58%,
  legenda: [Operador mutante: repressor normal, produzido normalmente, mas sem sítio de encaixe. O operon é transcrito e traduzido continuamente.])

O segundo tipo tem mutação no #emph[lacI]. O operador está intacto, mas a proteína produzida é um repressor defeituoso, incapaz de se ligar ao DNA. Chama-se lacI#super[-]. O resultado observável é o mesmo — expressão contínua — mas a causa é o produto, não o endereço.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-21.png",
  largura: 58%,
  legenda: [Gene regulador mutante: o operador está perfeito, mas o repressor sintetizado não reconhece DNA. Mesmo fenótipo, mecanismo oposto.])

Vale registrar uma precisão que muita gente perde: constitutivo não quer dizer "no máximo". Quer dizer "sem resposta ao indutor". Um mutante O#super[c] crescendo em meio rico em glicose expressa o operon de forma constitutiva e, ainda assim, em nível baixo — porque o outro braço de controle, que veremos na PARTE III, continua desligado. *Constitutivo é sobre perda de regulação por um sinal específico, não sobre intensidade.*

#mini-resumo[Dois mutantes constitutivos, um fenótipo só na placa: O#super[c] é endereço estragado (age em cis), lacI#super[-] é produto estragado (age em trans). Para separá-los é preciso um experimento que coloque duas cópias na mesma célula.]

#subtopico("2.5 — Diploide parcial: o experimento que separa cis de trans")

Se dois mutantes dão o mesmo resultado numa célula com uma cópia só do operon, a saída é dar à célula duas cópias — uma mutante, outra normal — e ver o que acontece. É isso que faz o #termo-nota[diploide parcial][bactéria haploide que recebeu um plasmídeo F′ carregando uma segunda cópia apenas da região do operon lac, ficando com duas cópias dessa região e uma só de todo o resto]: o cromossomo carrega uma versão, o plasmídeo carrega outra, e as duas convivem no mesmo citoplasma.

Aqui a regra de 1.3 faz todo o trabalho. Se o elemento defeituoso for um *produto difusível*, a cópia boa fabrica proteína boa, essa proteína circula e corrige as duas moléculas de DNA. Se o elemento defeituoso for um *endereço*, nada corrige: cada molécula carrega o próprio destino.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-23.png",
  largura: 62%,
  legenda: [Repressor em trans. Uma das moléculas tem lacI mutado, mas a outra produz repressor funcional. Como o repressor difunde, ele ocupa os dois operadores e as duas cópias ficam reguladas. O alelo lacI#super[-] é, portanto, recessivo.])

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-22.png",
  largura: 62%,
  legenda: [Operador em cis. O repressor funcional é produzido em abundância e ocupa o operador normal, silenciando aquela molécula. Mas o operador mutante da outra molécula não o reconhece, e os genes ligados a ele continuam sendo transcritos. O alelo O#super[c] é dominante — e a dominância vale apenas para os genes da própria molécula.])

Reunindo os dois resultados numa leitura só: o alelo lacI#super[-] é *recessivo*, porque basta uma cópia boa do gene regulador em qualquer lugar da célula para restaurar o controle; e o alelo O#super[c] é *dominante em cis*, porque ele impõe expressão constitutiva aos genes que estão fisicamente ligados a ele, e apenas a esses. É esse par de resultados que estabelece, sem nenhuma ferramenta molecular, que o operador é um sítio de DNA e que o produto do #emph[lacI] é uma molécula que se desloca.

Um genótipo concreto ajuda a fixar. Considere uma bactéria com o cromossomo I#super[+] P#super[+] O#super[c] Z#super[+] e um plasmídeo I#super[-] P#super[+] O#super[+] Z#super[+]. Sem indutor, o repressor produzido pelo I#super[+] do cromossomo circula e silencia o operador normal do plasmídeo, mas não consegue silenciar o O#super[c] do cromossomo: há produção de β-galactosidase, vinda apenas da cópia cromossômica. Com indutor, o repressor solta também do plasmídeo, e as duas cópias produzem — a quantidade sobe. O fenótipo global, portanto, é constitutivo e dominante, com atuação em cis, e a explicação inteira sai de dois passos: *identificar quem produz repressor difusível* e, em seguida, *verificar qual operador reconhece esse repressor*.

#subtopico("2.6 — Os dois alelos que fecham a lógica, e um método para prever qualquer genótipo")

O modelo fica completo com dois alelos do #emph[lacI] que não são simples perdas de função e que, por isso mesmo, testam se o raciocínio foi realmente entendido.

O primeiro é o lacI#super[s], chamado super-repressor. A mutação não atinge o domínio que reconhece o DNA — atinge o sítio alostérico onde a alolactose se encaixa. O resultado é um repressor que liga o operador normalmente e nunca solta, porque não enxerga mais o indutor. O fenótipo é o oposto do constitutivo: *não-induzível*. E, como se trata de um produto difusível, esse repressor cego circula pela célula e trava também o operador da outra cópia — de modo que lacI#super[s] é dominante em trans. Um diploide parcial com lacI#super[s] em qualquer uma das duas moléculas fica branco na placa mesmo com IPTG.

O segundo é o lacI#super[-d], dominante-negativo. Aqui volta a estrutura quaternária mencionada em 2.1. Como o repressor funcional é um tetrâmero montado a partir de quatro cadeias, uma célula que produz cadeias normais e cadeias defeituosas ao mesmo tempo monta tetrâmeros mistos. Basta uma subunidade ruim para desestabilizar a geometria de encaixe do complexo inteiro, e a maioria dos tetrâmeros formados fica inútil. É perda de função com efeito dominante — o alelo ruim envenena o produto do alelo bom.

#confusao-prevista(
  titulo: "Nem todo alelo dominante é ganho de função",
  aluno_acha: [aluno associa dominante a "faz mais" e recessivo a "faz menos"],
  mecanismo: [o lacI#super[-d] não faz nada a mais: ele produz uma subunidade quebrada. Torna-se dominante porque o produto é multimérico e uma peça ruim inutiliza o conjunto montado. Dominância descreve o comportamento do alelo quando há outro presente, não a direção do efeito bioquímico.],
)

Com isso é possível abandonar as tabelas e usar um procedimento. Diante de qualquer genótipo novo, três passos resolvem, nesta ordem. *Primeiro passo:* separar os elementos mutados em sequência (P, O, sítio CAP) e gene que produz proteína (I) — isso decide de saída o que é cis e o que é trans. *Segundo passo:* somar todos os produtos difusíveis presentes na célula e decidir se existe repressor capaz de ligar DNA e se ele ainda responde ao indutor — isso define o estado do braço negativo. *Terceiro passo:* percorrer molécula por molécula perguntando se aquele operador reconhece o repressor disponível e se aquele gene estrutural é funcional — isso define quanto de enzima sai de cada cópia. Somar as contribuições das duas moléculas dá o fenótipo final, com e sem indutor.

#mini-resumo[lacI#super[-] recessivo e constitutivo · lacI#super[s] dominante e não-induzível · lacI#super[-d] dominante-negativo por tetramerização · O#super[c] dominante só em cis. Um método de três perguntas substitui a memorização: separar endereço de produto, somar os produtos da célula inteira, depois ler molécula por molécula.]

A PARTE II fecha com o operon inteiramente explicado por controle negativo — e com um resultado experimental que esse modelo não consegue explicar. Se a lactose está presente e o repressor está solto, a transcrição deveria ir ao máximo. Quando a bactéria cresce em lactose *e* glicose ao mesmo tempo, ela não vai. É desse buraco que nasce a PARTE III.

#parte-title("PARTE III — Controle positivo: promotor fraco, CAP-cAMP e a decisão combinatória")

#subtopico("3.1 — O buraco que o controle negativo deixa")

Feche os olhos e rode o modelo da PARTE II para uma bactéria em meio com lactose e glicose. Há lactose, logo há alolactose, logo o repressor está solto, logo o operador está livre. O modelo negativo prevê transcrição plena. O experimento mostra pouquíssimo mRNA — a célula consome a glicose primeiro e praticamente ignora a lactose enquanto houver glicose disponível.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-26.png",
  largura: 60%,
  legenda: [Com indutor presente, o operador está livre e a polimerase encontra o promotor desobstruído — e mesmo assim sai pouco mRNA. O gargalo não está mais no operador.])

Duas conclusões saem daí. A primeira é que remover o repressor é condição necessária, não suficiente: liberar o operador apenas devolve o promotor ao seu comportamento natural. A segunda, mais incômoda, é que o comportamento natural desse promotor é ruim. Se com operador livre a transcrição continua baixa, então *o promotor lac, sozinho, é fraco* — e entender por que ele é fraco, e por que isso é uma escolha e não um defeito, é o assunto dos próximos dois subtópicos.

#subtopico("3.2 — Anatomia de um promotor bacteriano e a ideia de consenso")

A RNA polimerase bacteriana é uma enzima só, e o núcleo dessa enzima não sabe distinguir um promotor de qualquer outro trecho de DNA. Quem sabe é uma subunidade destacável que se acopla ao núcleo e forma a holoenzima: a #termo-nota[subunidade sigma][subunidade da RNA polimerase bacteriana responsável por reconhecer o promotor; a versão principal em crescimento normal é a σ70]. É ela que lê o DNA e escolhe onde a transcrição vai começar.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-29.png",
  largura: 72%,
  legenda: [Os dois elementos que a subunidade σ lê ficam a montante do +1: a caixa em torno de -35 e a caixa em torno de -10, separadas por cerca de 17 pares de base. A separação faz parte do sinal — dois domínios da mesma proteína precisam alcançar as duas caixas ao mesmo tempo.])

O que ela lê são duas caixas curtas, uma centrada por volta de -35 e outra por volta de -10, separadas por aproximadamente 17 pares de base. A separação não é enchimento: a subunidade σ tem dois domínios de reconhecimento a uma distância fixa entre si, e só consegue tocar as duas caixas simultaneamente se elas estiverem espaçadas dentro de uma faixa estreita. Um promotor com sequências perfeitas mas espaçamento de 12 ou de 22 pares de base é um promotor ruim, porque a proteína não alcança as duas âncoras de uma vez.

O segundo conceito é o de #termo-nota[sequência consenso][a base mais frequente em cada posição, obtida alinhando muitos promotores reais; nenhum promotor individual precisa ser idêntico a ela]. Alinhando dezenas de promotores de *E. coli* e anotando qual base aparece com mais frequência em cada posição, obtém-se TTGACA para a caixa -35 e TATAAT para a caixa -10. Isso não é a sequência que todo promotor tem — é uma média estatística, e quase nenhum promotor real bate com ela em todas as posições.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-31.png",
  largura: 66%,
  legenda: [Promotores reais de #emph[E. coli] alinhados. Cada linha é um gene; as colunas destacadas são as caixas -35 e -10. Os números embaixo do consenso indicam em quantos por cento dos promotores aquela base aparece — nenhuma coluna chega a 100%.])

E é dessa imperfeição que nasce toda a regulação por força de promotor. *Quanto mais próxima do consenso, mais forte é o promotor* — a subunidade σ se encaixa melhor, a holoenzima permanece mais tempo no sítio, a probabilidade de abrir a bolha e iniciar a transcrição sobe. Quanto mais distante do consenso, mais fraco. A célula bacteriana usa esse gradiente como forma nativa de calibrar a expressão de cada gene, sem precisar de nenhum regulador: um gene ribossômico, necessário em quantidade enorme e o tempo todo, tem promotor quase consenso; um gene de uso ocasional tem promotor divergente.

#subtopico("3.3 — O promotor lac é fraco de propósito")

Chega a hora de olhar as letras. O promotor do operon lac diverge do consenso nas duas caixas, e diverge exatamente onde dói.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-33.png",
  largura: 62%,
  legenda: [Duas trocas, dois efeitos. Na caixa -35, o G do consenso virou T; na caixa -10, as duas últimas posições saíram do padrão. Cada divergência tira um contato entre a subunidade σ e o DNA.])

Na caixa -35, o consenso é TTGACA e o promotor lac traz TTTACA — uma troca de G por T. Na caixa -10, o consenso é TATAAT e o lac traz TATGTT. Cada divergência dessas custa um contato entre a subunidade σ e a dupla-hélice; somadas, elas explicam por que a holoenzima ocupa esse promotor de forma instável e raramente progride para o alongamento.

*O ponto que muda a leitura inteira da aula é este:* isso não é um promotor defeituoso. É a sequência selvagem, conservada, e a fraqueza é uma escolha de projeto. Um promotor forte já opera perto do teto e não tem para onde subir — não sobra amplitude para regular. Um promotor fraco, ao contrário, é uma base baixa sobre a qual um ativador pode construir uma diferença de dezenas de vezes. *A fraqueza não é o problema que o ativador resolve; a fraqueza é a condição que torna o ativador útil.*

#atencao-box("Promotor fraco não é promotor mutante",
  [Tratar a fraqueza do promotor lac como defeito leva a duas previsões erradas em cadeia. A primeira é achar que existe alguma condição em que o operon dispensa o ativador — não existe, porque a sequência não muda. A segunda é achar que ativador e repressor são forças simétricas atuando sobre a mesma coisa. Não são: o repressor decide se a polimerase pode sair da linha de partida, e o ativador decide com que frequência ela chega lá. São dois gargalos em série, e por isso o operon exige que os dois estejam liberados ao mesmo tempo.])

#subtopico("3.4 — CAP-cAMP: o interruptor que conta glicose")

O ativador do operon lac é uma proteína chamada #sigla("CAP", [proteína ativadora dependente de cAMP — também chamada CRP; liga-se ao DNA a montante do promotor e recruta a RNA polimerase]), e ela só funciona acompanhada. Sozinha, a CAP não reconhece DNA. Ela precisa antes ligar duas moléculas de #sigla("cAMP", [AMP cíclico — nucleotídeo mensageiro produzido a partir do ATP pela enzima adenilato-ciclase]), e é essa ligação que muda sua conformação e cria a superfície capaz de reconhecer o sítio CAP no DNA.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-34.png",
  largura: 74%,
  legenda: [O sítio CAP fica a montante do promotor, por volta da posição -61 — bem antes do trecho coberto pela RNA polimerase e muito antes do trecho coberto pelo repressor. Ativador e repressor não disputam espaço: cada um tem seu endereço.])

O que a CAP faz depois de ligada é mecanicamente concreto e vale a pena visualizar. Ela se encaixa no sítio a -61 e *dobra o DNA em cerca de 90 graus*. Essa dobra aproxima a própria CAP da região onde a polimerase pousa, e o contato que se estabelece ali é entre a superfície da CAP e o domínio carboxi-terminal da subunidade α da polimerase. Esse contato proteína-proteína é energia livre a favor: ele segura a holoenzima no promotor por tempo suficiente para que ela abra a bolha e escape, compensando exatamente o que as duas caixas divergentes tiraram.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-38.png",
  largura: 54%,
  legenda: [O dímero de CAP (em azul) encaixado no DNA. Repare na curvatura acentuada que a dupla-hélice sofre ao redor da proteína — é essa deformação que reposiciona o promotor em relação ao ativador.])

Falta a parte que faz da CAP um sensor. Ela responde ao cAMP, e o nível de cAMP na célula responde à glicose — de forma inversa e por um caminho que vale seguir passo a passo, porque é aqui que quase todo mundo pula direto para a conclusão.

A glicose entra na bactéria por um transportador que a fosforila durante a própria passagem, e a fonte do fosfato é uma cadeia de proteínas transportadoras que termina numa peça chamada #sigla("EIIA", [enzima IIA específica para glicose — componente do sistema de transporte da glicose que funciona também como sensor e distribuidor de sinal]). Quando há glicose entrando, a EIIA está constantemente entregando seu fosfato ao açúcar que passa, e portanto permanece na forma desfosforilada. Quando não há glicose entrando, o fosfato não tem para onde ir e a EIIA se acumula fosforilada. *A EIIA é, portanto, um medidor direto de fluxo de glicose* — e ela distribui essa informação por duas saídas independentes.

A primeira saída é a adenilato-ciclase, a enzima que fabrica cAMP a partir do ATP. Ela só é ativada pela EIIA fosforilada. Logo: glicose alta → EIIA desfosforilada → ciclase parada → cAMP baixo → CAP sem ligante → CAP não liga o sítio → nenhuma dobra, nenhum recrutamento → promotor fraco operando sozinho → pouco mRNA. E o inverso: glicose baixa → EIIA fosforilada → ciclase ativa → cAMP alto → CAP ativada → dobra e recrutamento → transcrição forte.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-39.png",
  largura: 56%,
  legenda: [O sentido da seta é o que mais confunde: a glicose derruba o cAMP, e é o cAMP que ativa a CAP. Glicose alta significa CAP inativa e operon lac no chão, mesmo com lactose sobrando.])

A segunda saída é mais direta ainda: a EIIA desfosforilada se liga à lactose-permease e a inibe. Isso se chama *exclusão do indutor*, e é um mecanismo distinto da repressão por catabólito, ainda que provocado pela mesma glicose. Um fecha a porta de entrada da lactose; o outro derruba o ativador do promotor. A célula usa duas alavancas independentes para garantir a mesma prioridade metabólica.

#confusao-prevista(
  titulo: "A glicose não age no operador",
  aluno_acha: [aluno resume "com glicose o operon fica reprimido" e associa isso ao repressor Lac],
  mecanismo: [o repressor Lac responde apenas à alolactose e ignora completamente a glicose. A glicose atua no braço positivo, e por sinalização, não por consumo: mantém a EIIA desfosforilada, a adenilato-ciclase parada e o cAMP baixo, deixando a CAP sem ligante. O termo #termo-nota[repressão por catabólito][queda da expressão de operons de açúcares alternativos quando há glicose, mediada pela redução de cAMP e consequente inativação da CAP] é historicamente infeliz: não há repressor envolvido, e sim ausência de ativação.],
)

#subtopico("3.5 — Quatro estados, a curva diáuxica e o mapa geral da regulação")

Com os dois braços montados, o comportamento do operon vira uma tabela pequena de duas entradas. E, mais importante do que a tabela, vira uma lógica: o operon só liga forte quando *falta glicose* e *sobra lactose*. As duas condições precisam ser satisfeitas ao mesmo tempo, porque cada uma libera um gargalo diferente.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-40.png",
  largura: 78%,
  legenda: [Os estados que importam. Em (a), sem lactose, o repressor ocupa o operador e nada acontece — a situação da CAP é irrelevante. Em (b), com lactose e com glicose, o operador está livre mas a CAP está inativa: só o nível basal do promotor fraco. Em (c), com lactose e sem glicose, o operador está livre e a CAP dobra o DNA: transcrição alta.])

#table(
  columns: (auto, auto, auto, auto, auto),
  stroke: 0.5pt + rgb("#c8ccd4"),
  table.header(
    [*Glicose*], [*Lactose*], [*Repressor no operador*], [*CAP ativa*], [*Transcrição*]
  ),
  [alta], [ausente], [sim], [não], [nula],
  [alta], [presente], [não], [não], [basal, muito baixa],
  [baixa], [ausente], [sim], [sim], [nula],
  [baixa], [presente], [não], [sim], [alta],
)

A leitura da última coluna mostra que a saída só é alta numa das quatro combinações. E há uma assimetria que a tabela revela e que vale nomear: quando não há lactose, o estado da CAP não muda absolutamente nada, porque o repressor no operador é um bloqueio a jusante — ele trava a polimerase depois de ela já ter sido recrutada. *Recrutar melhor uma polimerase que vai ficar presa não adianta.* Por isso o braço negativo tem precedência lógica sobre o positivo.

Essa lógica tem uma manifestação visível no crescimento da bactéria. Cultivada num meio com glicose e lactose juntas, *E. coli* cresce em duas fases separadas por um platô — o fenômeno chamado crescimento diáuxico. Na primeira fase ela consome glicose e ignora a lactose. Quando a glicose acaba, o crescimento para por um intervalo, e depois recomeça mais lentamente com a lactose. *O platô não é descanso:* é o tempo material de subir o cAMP, ativar a CAP, transcrever o operon, traduzir o mRNA e acumular permease e β-galactosidase suficientes. O gráfico de crescimento é, na prática, uma leitura direta do tempo de indução de um operon.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-41.png",
  largura: 66%,
  legenda: [Os três regimes, no mesmo promotor. Sem regulador, o promotor entrega seu nível basal. Com repressor no operador, cai abaixo dele. Com ativador no sítio a montante, sobe acima dele. Regulação negativa e positiva não são opostos — são duas direções a partir de uma mesma linha de base.])

Falta generalizar, porque o operon lac é um caso e não a regra inteira. Duas dimensões independentes classificam qualquer operon. A primeira é o *efeito da proteína reguladora*: negativa quando a proteína ligada ao DNA reduz a transcrição, positiva quando a aumenta. A segunda é o *sentido do sinal*: um operon é indutível quando um pequeno metabólito liga a via, e reprimível quando um pequeno metabólito a desliga. Como as duas dimensões são independentes, existem operons negativos indutíveis, negativos reprimíveis, positivos indutíveis e positivos reprimíveis. O lac ocupa duas casas ao mesmo tempo: é negativo indutível pelo lado do repressor e positivo indutível pelo lado da CAP.

A regra de fundo por trás dessa classificação é metabólica, e é o que responde ao problema de quando cada tipo de controle é necessário. *Via catabólica — que consome um nutriente — costuma ser indutível, porque faz sentido ligar a máquina quando o substrato aparece.* *Via anabólica — que fabrica um produto — costuma ser reprimível, porque faz sentido desligar a fábrica quando o produto já está sobrando.* O operon do triptofano ilustra o segundo caso de forma exata: seu repressor, o TrpR, nasce incapaz de ligar DNA e só ganha essa capacidade quando o próprio triptofano se acopla a ele. O triptofano funciona ali como #termo-nota[co-repressor][pequeno metabólito que ativa um repressor, permitindo que ele ligue o operador — o inverso funcional de um indutor], e o comportamento é o espelho perfeito da alolactose: uma molécula que solta o repressor, outra que o prende.

E o triptofano ainda acrescenta uma camada que só é possível porque em bactéria transcrição e tradução acontecem juntas. Além da repressão pelo TrpR, o operon trp tem #termo-nota[atenuação][mecanismo em que a estrutura secundária do RNA nascente decide se a transcrição continua ou é abortada, controlada pela velocidade do ribossomo que traduz um peptídeo-líder], em que um ribossomo traduzindo um pequeno peptídeo no começo do próprio mRNA nascente determina, pela sua velocidade, qual grampo o RNA vai formar — e um dos grampos possíveis é um terminador que aborta a transcrição antes dos genes estruturais. Com triptofano abundante o ribossomo corre, forma-se o terminador e a transcrição para; com triptofano escasso ele emperra, o terminador não se forma e a transcrição segue. É controle fino sobreposto ao controle grosso.

Por fim, um caso mostra que nem a dicotomia positivo/negativo é rígida: no operon da arabinose, a proteína AraC atua como repressor quando não há arabinose e como ativador quando há, mudando de papel conforme o ligante. A mesma proteína, os mesmos genes, dois sinais opostos.

#mini-resumo[O operon lac é uma porta lógica: liga só com lactose presente E glicose ausente. O braço negativo tem precedência porque trava a polimerase depois do recrutamento. Indutível ou reprimível é sobre o sinal; positivo ou negativo é sobre o efeito da proteína — e as duas dimensões se combinam livremente.]

#conclusao-box[
*O princípio que unifica a aula* é que regular expressão em bactéria é, quase sempre, modular a probabilidade de a RNA polimerase iniciar a transcrição num promotor — e que essa modulação é feita por proteínas difusíveis que leem o meio e se encaixam em endereços fixos no DNA. Todo o resto são variações sobre esse tema: se a proteína reduz ou aumenta a probabilidade, se o metabólito prende ou solta a proteína, se o endereço fica antes ou depois do ponto de início.

*O mecanismo nuclear a levar embora* é a arquitetura de dois gargalos em série do operon lac. O operador, imediatamente a jusante do promotor, decide se a polimerase que já pousou consegue abrir a bolha e escapar; o sítio CAP, bem a montante, decide com que frequência ela é recrutada para lá. O repressor responde à alolactose e ignora a glicose; a CAP responde ao cAMP, que é o relatório que a célula escreve sobre o fluxo de glicose pelo transportador. Como os dois gargalos são independentes e ambos precisam estar abertos, a saída obedece a uma lógica de conjunção — e é essa conjunção, não a repressão isolada, que dá ao sistema a capacidade de escolher entre dois açúcares.

*A clínica que isso sustenta* já está no laboratório em que a medicina se apoia. A triagem de colônias azuis e brancas, que usa um substrato cromogênico para revelar a atividade de β-galactosidase, é a etapa de seleção de boa parte da clonagem molecular que produz insulina humana, hormônio de crescimento e fatores de coagulação recombinantes: o inserto interrompe o #emph[lacZ], a colônia perde a cor e é escolhida a olho nu. E o próprio operon é usado como interruptor de expressão sob demanda — construções controladas por operador lac permanecem silenciosas até que se acrescente IPTG ao fermentador, exatamente porque o indutor gratuito não é consumido e mantém a produção estável. Entender por que uma colônia fica branca é entender por que aquele frasco de insulina existe.

*O que vem a seguir* é a mesma pergunta feita a uma célula com núcleo. O eucarioto perde as duas conveniências que tornam o operon simples: seus genes não estão agrupados por via metabólica, e transcrição e tradução acontecem em compartimentos separados, o que inviabiliza mecanismos como a atenuação. Em troca, ele ganha camadas que a bactéria não tem — o DNA enrolado em nucleossomos, que precisa ser aberto antes de qualquer coisa; sítios reguladores a milhares de pares de base do promotor; e controle sobre processamento, exportação, estabilidade e tradução do mRNA. Ao ler aquele material, o mapa desta aula continua servindo: continue perguntando quem é endereço e quem é produto difusível, e o que o produto difusível está medindo no meio.
]
