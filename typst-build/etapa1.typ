#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Um hospital gasta uma fração enorme do seu esforço diário fazendo uma coisa só: impedir que micro-organismos cheguem onde não devem. Lava-se a mão antes de tocar o paciente, esfrega-se a pele antes de furá-la, mergulha-se o endoscópio numa solução antes de reutilizá-lo, coloca-se a caixa de instrumentais numa autoclave antes da cirurgia. Cada um desses gestos usa um agente diferente, por um tempo diferente, e promete uma coisa diferente — e é exatamente isso que esta aula ensina a distinguir.

A lógica que atravessa tudo é uma só: *nenhum método mata "os micro-organismos" em bloco; cada método derruba uma fração da população por unidade de tempo, e essa fração depende de qual barreira física o alvo carrega*. Daí saem as três PARTES. A PARTE I monta a régua — o que cada palavra promete, o que o sufixo do agente significa, por que a morte microbiana é logarítmica e por que existe uma escada bem definida de resistência, do micoplasma sem parede ao príon sem ácido nucleico. A PARTE II percorre os agentes físicos: calor, radiação, filtração e frio, cada um com um mecanismo próprio e um limite próprio. A PARTE III fecha com os agentes químicos e com a decisão que interessa na clínica — diante deste material, contaminado por este agente, qual processo se aplica.
]

#parte-title("PARTE I — A régua: o que cada palavra promete", primeira: true)

#subtopico("1.1 Limpeza, desinfecção, antissepsia, esterilização: quatro promessas diferentes")

Essas quatro palavras aparecem na mesma frase na rotina hospitalar e são tratadas como sinônimos de "deixar limpo". Não são. Cada uma é uma promessa distinta sobre *o que sobrevive ao procedimento*, e a distância entre elas é o que decide se um instrumento pode entrar numa articulação ou apenas encostar na pele.

A *limpeza* é a base e não mata nada. Detergente e água removem sujidade, resto de tecido, sangue e o filme onde o micro-organismo se aloja; o que ocorre é remoção mecânica e diluição, não morte. A carga microbiana cai porque a maior parte dela vai embora no enxágue. A palavra *descontaminação* nomeia o resultado dessa etapa quando ele já basta: tratar um objeto ou superfície de modo a torná-lo seguro para o uso seguinte — lavar o utensílio de cozinha antes de usá-lo de novo é descontaminação completa e suficiente.

A *desinfecção* é a primeira que age quimicamente. Um agente desinfetante ataca diretamente o micro-organismo sobre uma superfície inanimada, matando-o ou inibindo severamente seu crescimento. A promessa aqui é explícita e limitada: ela *não elimina todos*. A água sanitária — solução de #termo-nota[hipoclorito de sódio][sal do ácido hipocloroso; em água libera ácido hipocloroso, a espécie que efetivamente oxida] — cobre uma faixa ampla de aplicações domésticas e hospitalares justamente porque não precisa ser absoluta para ser útil.

A *antissepsia* é a mesma ideia deslocada para o tecido vivo, e esse deslocamento muda tudo. Sobre pele ou mucosa existe um segundo interessado no resultado — o hospedeiro. O agente precisa matar sem cauterizar, sem irritar, sem ser absorvido em quantidade tóxica. É por isso que o antisséptico costuma ser um produto mais brando que o desinfetante de superfície: *a restrição não é química, é o dano colateral*.

No topo está a *esterilização*: morte ou remoção de todos os micro-organismos, vírus incluídos. Repare no "ou remoção" — filtrar uma solução e reter as bactérias na membrana produz um filtrado estéril sem ter matado ninguém. E repare também na palavra "todos", que é o que separa esterilização de tudo o que vem abaixo: o critério não é o quanto se matou, é se sobrou alguma forma viável, inclusive a mais resistente que existir naquele material.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-21.png",
  largura: 60%,
  legenda: [A sequência que a rotina exige, em corte lateral. Em cima, a limpeza: o detergente descola a sujeira aderida e a rinsagem a leva embora, deixando micro-organismos ainda vivos sobre a superfície agora exposta. Embaixo, a desinfecção: o agente alcança o que restou porque não há mais nada entre ele e o alvo. Trocar a ordem das duas etapas é o erro mais comum da rotina — e o mais silencioso.])

Uma consequência incômoda fecha o subtópico. A esterilidade nem sempre é alcançável, e nem sempre é o objetivo. Não se esteriliza um piso, uma mão, um campo cirúrgico ou o ar de um centro cirúrgico — em todos esses casos, o realista é reduzir a carga a um nível seguro e manter a redução. Em outros casos ela é inegociável: um implante, uma agulha, um instrumento que atravessa a barreira cutânea. O critério que decide entre um caso e outro não é o zelo de quem processa — é o destino do artigo, e ele será formalizado na PARTE III.

#mini-resumo[Em uma frase: limpeza remove, desinfecção mata o que ficou numa superfície, antissepsia faz o mesmo num tecido vivo dentro do limite da toxicidade, e esterilização é a única que promete nenhuma forma viável.]

#subtopico("1.2 Estático e cida: por que o sufixo decide a conduta")

O sufixo do rótulo parece detalhe de nomenclatura e é a informação mais operacional da embalagem. Um agente *bacteriostático* não mata: ele trava a multiplicação. A população fica parada no número em que estava, e quem termina o serviço é o sistema imune do hospedeiro, fagocitando células que já não conseguem repor as perdas. Um agente *bactericida* mata: a curva de sobreviventes desce sozinha, com hospedeiro ou sem ele.

Essa diferença é abstrata até o momento em que o hospedeiro não pode cumprir sua parte. Em alguém com neutropenia profunda, ou num sítio para onde a célula de defesa não chega bem — vegetação de válvula cardíaca, líquor, osso —, deixar a população parada não resolve; ela retoma o crescimento assim que a concentração do agente cai. *O ponto fino é que "estático" descreve uma parceria, e a parceria pode não existir.*

A família se repete para cada grupo de alvo. Do lado estático estão bacteriostático, fungistático e esporostático; do lado cida, bactericida, fungicida, esporocida e virucida. Duas dessas etiquetas merecem atenção. A primeira é *esporocida*, que a bibliografia costuma marcar com um asterisco: matar a forma vegetativa não prediz nada sobre matar o #termo-nota[endósporo][forma de repouso com o núcleo desidratado, córtex espesso e DNA embalado em proteínas protetoras], porque a barreira ali é estrutural e não química. A segunda é "virustática", termo que a própria bibliografia marca com dúvida — o vírus não tem metabolismo próprio fora da célula hospedeira, então não há multiplicação a ser paralisada do lado de fora. Contra partícula viral livre, ou se inativa ou não se faz nada.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-31.png",
  largura: 56%,
  legenda: [Os dois destinos possíveis e as variáveis que decidem entre eles. À esquerda, a família estática, que interrompe a multiplicação; à direita, a família cida, que mata — com o asterisco sobre "esporocida" sinalizando que essa é a fronteira difícil. Embaixo, os quatro parâmetros que transformam qualquer molécula da lista em um resultado concreto.])

O rótulo, sozinho, não entrega o resultado. Quatro variáveis o completam. O *espectro de ação* diz quais grupos o agente alcança — e é ele que separa um produto tuberculicida de um que não é. A *concentração* decide se a molécula chega ao alvo em número suficiente, e quase sempre existe uma faixa útil com piso e teto: álcool concentrado demais funciona pior, como se verá adiante. O *tempo de contato* é o parâmetro mais desrespeitado da rotina: passar o agente e secar em seguida cancela o efeito de quase todos eles. E a *toxicidade* é o veto — ela não melhora o desempenho, apenas define onde o produto pode ser usado.

Vale separar ainda um terceiro objetivo, que não é desinfetar nem esterilizar: a *preservação*. Conservantes em cosméticos, alimentos e soluções injetáveis são agentes estáticos em concentração baixa, cuja função é impedir que uma contaminação eventual cresça durante a validade do produto. Não se pede a eles que limpem nada; pede-se que segurem a curva no lugar.

#mini-resumo[Se você só lembrar de uma coisa: o sufixo diz se o agente mata ou apenas segura, e espectro, concentração, tempo e toxicidade decidem se essa promessa vai se cumprir naquela situação.]

#subtopico("1.3 A morte microbiana é logarítmica: o valor D e o que \"mata 99,9%\" significa")

Imagine uma liquidação em que a loja anuncia 90% de desconto sobre o preço a cada hora que passa. Na primeira hora, um produto de mil reais cai para cem. Na segunda, de cem para dez. Na terceira, de dez para um. O desconto percentual é sempre o mesmo, mas a quantia abatida despenca — e o preço nunca chega a zero. A morte microbiana funciona exatamente assim, e entender esse formato resolve metade das confusões desta aula.

O agente não mata um número fixo de células por minuto; ele mata uma *fração constante* por unidade de tempo. É o que se chama de cinética de primeira ordem, e a razão é intuitiva: cada célula tem, naquele instante, a mesma probabilidade de sofrer o evento letal, então o número absoluto de mortes é proporcional a quantas células ainda existem. Numa população de 10⁶ por mililitro, o primeiro intervalo mata 900 mil; no intervalo seguinte, com a mesma eficácia, mata 90 mil. A eficácia não caiu — o estoque é que diminuiu.

Isso dá à cinética uma unidade natural. O *valor D*, ou tempo de redução decimal, é o tempo necessário para reduzir a população a um décimo do valor inicial naquelas condições fixas de temperatura e concentração. Um D é uma redução de 1 log₁₀, ou 90%. A leitura em etapas é direta:

#align(center)[
#table(
  columns: 4,
  align: (center, center, center, center),
  inset: 6pt,
  stroke: 0.4pt + gray,
  table.header(
    [*Reduções*], [*log₁₀*], [*% eliminado*], [*De 10⁶/mL, sobram*]
  ),
  [1 D], [1], [90%], [10⁵/mL],
  [2 D], [2], [99%], [10⁴/mL],
  [3 D], [3], [99,9%], [10³/mL],
  [6 D], [6], [99,9999%], [1/mL],
  [12 D], [12], [—], [1 em 10⁶ unidades],
)
]

Agora a frase de rótulo fica legível. "Mata 99,9%" não é "praticamente tudo": é uma redução de 3 log₁₀. Sobre uma carga inicial de um milhão por mililitro, sobram mil por mililitro — e a relevância desse resíduo depende do volume que se vai usar. O exemplo da água de rio é o mais claro: com 10⁴ bactérias por mililitro, uma cloração que remove 90% deixa 10³ por mililitro; se forem necessários 10 mililitros dessa água, o que chega ao copo são 10 mil células viáveis. *O que muda a leitura não é o percentual, é o produto entre a concentração residual e o volume utilizado.*

Daí sai a consequência conceitual mais importante da aula. Se a curva é exponencial, ela se aproxima do zero sem nunca tocá-lo, e "ausência absoluta de vida" deixa de ser uma grandeza mensurável. A esterilidade passa a ser definida em *probabilidade*: convenciona-se um nível de segurança de esterilidade de 10⁻⁶, isto é, no máximo uma chance em um milhão de que um item processado carregue uma forma viável. É por isso que a esterilização por calor úmido é calibrada com folga sobre o tempo teoricamente necessário, e é por isso que a indústria de alimentos enlatados trabalha com o conceito de doze reduções decimais sobre o esporo do agente do botulismo. *Não se esteriliza até não sobrar nada; esteriliza-se até que a chance de sobrar seja aceitavelmente pequena.*

#subtopico("1.4 A escada de resistência: quem morre primeiro e quem resiste a tudo")

O valor D do subtópico anterior tem uma propriedade que muda tudo: ele não é uma característica do processo isolado, e sim do par processo–organismo. O mesmo tempo de exposição ao mesmo desinfetante entrega dez reduções decimais num micoplasma e nenhuma num endósporo. Existe, portanto, uma ordem estável de resistência — e ela não é arbitrária: cada degrau corresponde a uma barreira física que dá para nomear.

No degrau mais sensível está o *micoplasma*, e a razão é a ausência de parede celular. Sem peptideoglicano, a membrana plasmática fica diretamente exposta a qualquer agente tensoativo ou lipofílico, e cede com facilidade. Logo acima vêm, juntas, três coisas que parecem muito diferentes: bactérias Gram-positivas, bactérias Gram-negativas e *vírus envelopados*. A companhia surpreende até se lembrar do que o envelope viral é — uma bicamada lipídica roubada da célula hospedeira. Álcool e detergente dissolvem lipídio; um vírus envelopado, portanto, é dos alvos mais frágeis que existem, apesar de ser um patógeno temível dentro do corpo.

O primeiro degrau realmente difícil aparece com os *vírus não envelopados*. Sem lipídio a dissolver, sobra apenas um capsídeo de proteína compacto e resistente, o que os torna mais duros que boa parte das bactérias vegetativas — e é o que explica um fato clínico que contraria a intuição de todo mundo, o de que álcool em gel não resolve norovírus. Acima deles estão as *micobactérias*, protegidas não por uma parede mais espessa, mas por uma camada cerosa de #termo-nota[ácido micólico][ácido graxo de cadeia muito longa que forma uma capa hidrofóbica sobre a parede da micobactéria], hidrofóbica, que repele solução aquosa e retarda a entrada de qualquer agente que dependa de água como veículo.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-09.png",
  largura: 74%,
  legenda: [A escala completa, do mais sensível ao topo. À esquerda, os grupos em ordem de resistência crescente; ao centro, a faixa de suscetibilidade; à direita, as classes químicas que ainda funcionam em cada altura — repare como a lista encurta conforme se sobe, até restar hipoclorito muito concentrado e álcali forte no degrau dos príons. Embaixo, os dois pares tempo-temperatura que resolvem quase tudo abaixo do topo.])

O degrau seguinte é o *endósporo bacteriano*, e a resistência dele é uma soma de estados: núcleo praticamente desidratado, #termo-nota[dipicolinato de cálcio][complexo que ocupa o núcleo do esporo, imobiliza a água restante e estabiliza o DNA] ocupando o interior, pequenas proteínas ácido-solúveis embalando o DNA e um córtex espesso de peptideoglicano modificado ao redor. Sem água livre, a desnaturação térmica fica lenta demais para acontecer nos 100 °C da fervura — daí a regra que organiza toda a PARTE II. Mais acima ainda estão os *oocistos de protozoário*, cuja parede resiste às concentrações de cloro usadas em água de abastecimento, o que faz de *Cryptosporidium* uma causa clássica de surto veiculado por água tratada; o que o controla é filtração e ultravioleta.

E no topo, sozinho, o *príon* — que não é um organismo, e é justamente por isso que resiste. Sendo apenas uma proteína mal dobrada, agregada em folha β, não há ácido nucleico a quebrar nem membrana a romper. Ele atravessa o ciclo padrão de autoclave e exige ciclo prolongado a temperatura mais alta associado a álcali forte ou hipoclorito muito concentrado. Pior: o formaldeído, que inativa quase tudo, *fixa* o agregado e o estabiliza — um dos raros casos em que um bom desinfetante piora o problema.

#confusao-prevista(
  titulo: "Menor não é mais resistente",
  aluno_acha: [que vírus resiste mais que bactéria porque é menor, e que bactéria resiste mais que fungo pelo mesmo motivo],
  mecanismo: [o que decide a posição na escada é a barreira física, não a dimensão. Vírus envelopado está entre os alvos mais frágeis porque o lipídio se dissolve; vírus não envelopado sobe vários degraus porque só tem capsídeo proteico; e o príon, a menor entidade da lista, é a mais resistente de todas porque não tem estrutura vulnerável a atacar.],
)

Guarde a escada inteira, porque ela é a chave de leitura de tudo o que vem a seguir: todo método será descrito por *até onde ele sobe*.

#parte-title("PARTE II — Agentes físicos: calor, radiação, filtração e frio")

#subtopico("2.1 Por que o calor mata: desnaturação, o leite e o ovo")

Dizer que o calor mata porque "cozinha" o micro-organismo é a explicação que atrasa o entendimento de toda esta PARTE. O calor não rompe ligações covalentes: a cadeia de aminoácidos sai intacta do processo. O que ele desfaz são as interações fracas que sustentam o dobramento — pontes de hidrogênio, interações hidrofóbicas entre os resíduos do miolo da molécula, pares iônicos. A energia térmica agita a cadeia até que essas interações não segurem mais a forma, e a proteína se abre.

A consequência é imediata e específica. Uma enzima é um sítio ativo, e o sítio ativo é uma geometria: um conjunto de resíduos que ficam a distâncias exatas uns dos outros *porque* a cadeia está dobrada daquele jeito. Desfeito o dobramento, os resíduos continuam presentes e o sítio deixa de existir. É por isso que a desnaturação é letal com tão pouca energia comparada à necessária para quebrar a molécula: não é preciso destruir a proteína, basta desarrumá-la.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-06.png",
  largura: 62%,
  legenda: [Os dois destinos de uma proteína aquecida. Em cima, o caminho irreversível: aberta, a cadeia se agrega com as vizinhas e não volta — é a clara do ovo, que nunca destranslucidece. Embaixo, o reversível: retirado o calor a tempo, a cadeia reencontra o próprio dobramento — é o leite morno. A diferença entre as duas linhas não está na molécula, está no tempo e na temperatura a que ela foi submetida.])

Nem toda desnaturação é definitiva, e a diferença entre os dois desfechos é o que transforma temperatura e tempo em parâmetros acoplados. Aqueça leite brandamente e deixe esfriar: boa parte das proteínas reencontra o próprio dobramento, porque a sequência de aminoácidos continua contendo toda a informação necessária para se enovelar. Frite um ovo: as cadeias abertas ficam expostas o suficiente, e por tempo suficiente, para se agarrarem umas às outras formando uma rede insolúvel — e agora não há mais volta, porque cada cadeia está presa às vizinhas. *O que decide entre um caso e outro é quanto tempo a molécula passa aberta.*

Daí a regra que governa todo método térmico: temperatura e tempo se compensam. Elevar a temperatura acelera a abertura e a agregação, e permite encurtar a exposição; baixá-la exige esperar mais. Citar uma sem a outra descreve metade do processo — e é por isso que nenhum método de calor desta aula tem uma temperatura como definição, todos têm um par.

Duas ressalvas fecham o mecanismo. A primeira é que a proteína não é o único alvo: o calor também desorganiza a bicamada lipídica da membrana, que passa a vazar íons e metabólitos, e fragmenta ácido nucleico em temperaturas altas. A desnaturação é o mecanismo dominante, não o exclusivo. A segunda é que a presença de água muda drasticamente a facilidade de desnaturar — e é esse detalhe, aparentemente lateral, que decide a disputa do próximo subtópico.

#subtopico("2.2 Autoclave e forno: por que 121 °C úmidos vencem 180 °C secos")

Aquela última observação sobre a água é a chave de um resultado que parece contradizer a física do dia a dia: o vapor a 121 °C esteriliza em 15 minutos, e o ar seco a 180 °C precisa de uma hora inteira para fazer o mesmo. O número maior perde, e o motivo tem três camadas.

A primeira camada é química. A água participa da desestabilização da proteína: ela compete pelas pontes de hidrogênio internas, solvata os resíduos que estavam escondidos no miolo hidrofóbico e permite a hidrólise de ligações que, em meio seco, permaneceriam intactas. Uma proteína hidratada abre-se a temperatura muito menor que a mesma proteína seca — e é exatamente por isso que o esporo, com o núcleo desidratado, é tão resistente ao calor.

A segunda camada é o transporte de energia. Quando o vapor encontra a superfície fria do material, ele condensa, e a condensação libera de uma vez o *calor latente* que havia sido gasto para evaporar aquela água — uma quantidade de energia muito maior do que o ar quente entregaria por simples contato. O vapor, portanto, não só está quente: ele deposita energia no ponto exato onde toca. É o mesmo princípio pelo qual um vapor de 100 °C queima a pele com muito mais gravidade do que um ar de 100 °C.

A terceira camada é a que explica a pressão, e é onde quase todo mundo erra. *A pressão não mata bactéria.* Água em recipiente aberto ferve a 100 °C e não passa disso, porque toda a energia adicional vai para a mudança de estado. Fechando a câmara e permitindo que a pressão suba cerca de uma atmosfera acima da atmosférica, o ponto de ebulição sobe junto, e o #termo-nota[vapor saturado][vapor em equilíbrio com a água líquida na temperatura e na pressão da câmara — é ele que condensa ao tocar o material e entrega o calor latente] pode existir a 121 °C. A pressão é o meio de obter vapor mais quente; o agente letal continua sendo o calor úmido. É a panela de pressão da cozinha, com um manômetro e um cronômetro.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-10.png",
  largura: 66%,
  legenda: [Os dois equipamentos e os dois pares tempo-temperatura. Em cima, autoclaves de porte hospitalar e o desenho original do aparelho de Chamberland, com o vaso fechado que sustenta a pressão. Embaixo, estufas de calor seco, onde o material precisa ficar de uma a duas horas. Repare que o forno processa vidraria, pó e óleo — justamente o que o vapor não penetra bem.])

Disso decorre a falha operacional mais importante do método: *ar retido derruba a temperatura efetiva*. Numa mistura de ar e vapor a uma dada pressão, a temperatura é menor do que seria com vapor saturado puro, e bolsões de ar dentro de um pacote mal arrumado ficam abaixo do alvo enquanto o manômetro exibe um valor normal. Daí as regras que parecem burocráticas e não são: purgar o ar no início do ciclo, não superlotar a câmara, embalar em material permeável ao vapor. O forno de calor seco escapa dessa armadilha porque não depende de penetração de vapor — e por isso é a escolha para vidraria, instrumento cortante que a umidade corroeria, pós e substâncias oleosas —, mas paga o preço no mecanismo: sem água, a morte passa a depender de oxidação lenta dos componentes celulares, e daí os 160 °C por duas horas ou 180 °C por uma hora.

Falta comprovar que deu certo, e aqui há duas ferramentas que costumam ser confundidas. A *fita termossensível* colada no pacote muda de cor ao atingir determinada temperatura: ela é um indicador químico e informa apenas que o pacote esteve exposto ao calor. O *indicador biológico* é outra coisa — uma ampola contendo esporos de uma espécie escolhida por ser mais resistente que qualquer contaminante esperado, *Geobacillus stearothermophilus* para calor úmido e um esporo de *Bacillus* para calor seco e óxido de etileno. Depois do ciclo, quebra-se a ampola sobre o meio de cultura e incuba-se: meio límpido significa esporos mortos e processo eficaz; meio turvo significa que sobreviveu esporo, e portanto que o ciclo falhou.

#atencao-box("Fita colorida não comprova esterilidade", [
A fita registra que o pacote alcançou certa temperatura em algum momento — nada mais. Ela não informa por quanto tempo o material permaneceu naquela temperatura, nem se o vapor penetrou até o centro do pacote, que são exatamente os dois parâmetros que decidem a morte do esporo. Um pacote com bolsão de ar sai da autoclave com a fita perfeitamente escurecida e o conteúdo não estéril. Só o indicador biológico testa o parâmetro que interessa, porque nele o que está sendo desafiado é um esporo vivo.
])

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-11.png",
  largura: 68%,
  legenda: [Como se comprova o ciclo. À esquerda, o indicador biológico: a tira de esporos é autoclavada dentro da ampola, o meio é liberado esmagando o vidro interno e o conjunto vai à estufa — límpido significa esporos mortos, turvo significa falha. Ao centro, as duas placas correspondentes. À direita, a fita termossensível, cujas listras escurecem com a temperatura e não dizem nada sobre tempo nem penetração.])

#subtopico("2.3 Chama, fervura e pasteurização: os calores que não miram a esterilidade")

Nem todo uso de calor persegue esterilidade, e reunir os três casos em que ele não persegue deixa a lógica da PARTE inteira mais nítida. Cada um deles troca a promessa por outra coisa: velocidade, simplicidade ou preservação do material.

O caso extremo é a *incineração*, e ela não é um método de esterilização — é de destruição. Resíduo biológico hospitalar é convertido em dióxido de carbono, água e cinza mineral por combustão a temperaturas de centenas de graus, sem que sobre estrutura biológica alguma. Aplica-se justamente ao que não se pretende reutilizar. A *flambagem* é o mesmo princípio em miniatura: a alça de platina passa pela chama até o rubro, e tudo o que estava nela é queimado — é o gesto que garante que cada semeadura na bancada comece de um instrumento sem carga microbiana. Versões modernas fazem isso em cones de aquecimento elétrico, que evitam o aerossol produzido pelo estalo de material orgânico na chama aberta.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-15.png",
  largura: 60%,
  legenda: [Três calores com três promessas distintas. À esquerda, a flambagem da alça e da boca do tubo, esterilização instantânea por combustão direta. À direita, a fervura — 100 °C por cerca de 15 minutos, suficiente para as formas vegetativas e insuficiente para o esporo — e a pasteurização, mais branda ainda, que não pretende esterilizar nada.])

A *fervura* é o método caseiro por excelência e o mais mal interpretado. Cem graus por cerca de quinze minutos matam bactérias vegetativas, fungos e a maioria dos vírus — e não matam endósporo, pelo motivo já montado no subtópico anterior: sem água livre no núcleo, a desnaturação térmica ali é lenta demais para acontecer nessa temperatura. Ferver, portanto, é desinfetar, não esterilizar, e essa distinção é tudo o que separa um utensílio doméstico seguro de um instrumento cirúrgico confiável. Historicamente contornou-se o problema com ciclos repetidos — ferver, deixar em temperatura ambiente para que os esporos germinem, ferver de novo, três vezes —, uma manobra engenhosa que hoje só sobrevive onde não há autoclave.

A *pasteurização* fecha o grupo com a lógica mais interessante. Desenvolvida por Pasteur em 1862 para vinho e cerveja, ela expõe o alimento a uma temperatura abaixo do ponto de ebulição e o resfria bruscamente em seguida. O objetivo declarado é reduzir a concentração de micro-organismos e eliminar os patógenos, preservando sabor, aroma e valor nutricional — e a restrição da temperatura vem dessa segunda exigência, não da primeira. Na versão lenta clássica, o leite fica a 62–65 °C por 30 minutos; na versão rápida, a cerca de 72 °C por 15 segundos, com o resfriamento imediato limitando a exposição térmica das proteínas do próprio alimento.

*O detalhe que se costuma perder é como se escolheu esse par.* Ele foi calibrado sobre o patógeno não esporulado mais resistente ao calor que podia estar no leite — historicamente o agente da tuberculose bovina e, depois, o agente da febre Q. Matar aquele, com margem, mata todos os menos resistentes. O leite de longa duração muda de promessa: 130–150 °C por poucos segundos, o que atinge esterilidade comercial e explica por que ele permanece meses fora da geladeira, enquanto o pasteurizado, que continua tendo micro-organismos vivos, exige refrigeração e vence em dias.

#subtopico("2.4 Radiação: a ionizante quebra o DNA, a ultravioleta o solda")

Duas radiações aparecem no mesmo espectro, ambas microbicidas, e é tentador tratá-las como versões mais forte e mais fraca do mesmo efeito. São mecanismos diferentes — e a diferença aparece exatamente onde importa, na capacidade de penetrar o material.

A *radiação gama* é ionizante: cada fóton carrega energia suficiente para arrancar elétrons dos átomos que atravessa. O dano ao DNA é em boa parte indireto e passa pela água, que é o componente mais abundante da célula: a ionização da água gera radical hidroxila, uma espécie extremamente reativa e de vida curtíssima, que ataca o açúcar e as bases do DNA ali por perto e produz quebras de fita. Acumuladas, essas quebras tornam a replicação impossível. Como o fóton gama atravessa papelão, plástico e o próprio produto, o material pode ser irradiado *já embalado e lacrado* — e como o processo praticamente não eleva a temperatura, ele é chamado de esterilização a frio, o que o torna o método industrial padrão para seringas, luvas, fios de sutura e placas descartáveis.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-13.png",
  largura: 72%,
  legenda: [As três radiações e o que as separa. À esquerda, a instalação de irradiação gama, com a fonte guardada sob água e o produto passando embalado em esteira. À direita, o forno de micro-ondas, que não ioniza nada e mata apenas pelo calor que gera na água. Embaixo, o espectro: a faixa microbicida está entre 200 e 300 nm, no ultravioleta C — repare que ela fica fora do visível, o que significa que a lâmpada acesa não indica que a superfície está sendo alcançada.])

A *ultravioleta* está do lado não ionizante do espectro e mata por um caminho completamente distinto. O comprimento de onda em torno de 254 nm é justamente o que as bases nitrogenadas do #sigla("DNA", [ácido desoxirribonucleico — a molécula que guarda a informação genética]) absorvem melhor. A energia absorvida faz duas timinas adjacentes na mesma fita se ligarem covalentemente, formando um *dímero de timina* — uma dobra na fita que a DNA-polimerase não consegue atravessar. Não há quebra: há uma solda no lugar errado, que trava replicação e transcrição.

Duas limitações decorrem direto desse mecanismo e são o que se cobra na rotina. A primeira é a *ausência de penetração*: a ultravioleta é absorvida por vidro comum, plástico, poeira e pela primeira camada de qualquer material — ela age na superfície exposta e no ar que passa diante da lâmpada, e qualquer face voltada para baixo ou sombreada permanece intocada. A segunda é o *reparo*: bactérias possuem enzimas de fotorreativação que desfazem dímeros de timina na presença de luz visível, de modo que uma dose subletal pode ser revertida em horas. Ultravioleta é excelente para manter a carga baixa num ambiente controlado, e é pouco confiável como método isolado de esterilização.

Sobra a pergunta que o slide deixa em aberto sobre o *micro-ondas*. Micro-ondas não ionizam e não formam dímeros: elas fazem os dipolos das moléculas de água girarem rapidamente, e o atrito desse movimento gera calor. A morte, portanto, é térmica e herda todos os problemas do aquecimento em campo desigual — pontos frios, regiões secas que quase não aquecem e distribuição dependente da geometria da carga. Existem sistemas industriais de tratamento de resíduo por micro-ondas, com trituração prévia para uniformizar a carga; para instrumental clínico, o método não é confiável.

#subtopico("2.5 Filtração: separar em vez de matar")

Todos os métodos anteriores compartilham um pressuposto que parece inevitável: para controlar o micro-organismo, é preciso destruí-lo. A filtração quebra esse pressuposto, e é justamente por isso que ela existe — soro fisiológico com proteína, meio de cultura com vitamina termolábil, solução de antimicrobiano e produto biológico não sobrevivem a nenhum dos calores da PARTE. Para eles, a saída é *tirar o micro-organismo de dentro do líquido* e deixá-lo vivo do outro lado da membrana.

O padrão é a membrana de 0,22 µm. O poro é menor que o menor diâmetro de qualquer bactéria de interesse, incluindo as mais finas, e por isso ela retém bactérias e fungos com confiabilidade suficiente para o filtrado ser tratado como estéril. A expressão correta, porém, é *filtro esterilizante por convenção*, e a ressalva não é acadêmica: vírus, com dezenas de nanômetros, e micoplasmas, deformáveis e sem parede, atravessam. Uma solução filtrada em 0,22 µm é confiavelmente livre de bactéria e não é, por si, livre de vírus.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-14.png",
  largura: 70%,
  legenda: [Filtração em dois contextos. À esquerda e embaixo, o sistema para líquidos: a amostra atravessa a membrana puxada por vácuo, e o filtrado cai estéril no frasco; a micrografia mostra bactérias retidas sobre a superfície da membrana, ainda íntegras — a filtração separa, não mata. À direita, a cabine com filtros de alta eficiência na entrada e na saída, aplicando o mesmo princípio ao ar.])

Dois detalhes de engenharia explicam o resto do método. O primeiro é a *cascata de pré-filtros*. Se a suspensão passasse direto pela membrana de 0,22 µm, as partículas grandes obstruiriam os poros em segundos e o fluxo cessaria antes de processar qualquer volume — é a #termo-nota[colmatação][entupimento progressivo dos poros de uma membrana pelo material retido, que faz o fluxo cair até parar]. Por isso se empilham estágios: um pré-filtro de fibra de vidro segura o material grosseiro, uma membrana de 5 µm segura o que passou, uma de 1,2 µm afina mais, e só então a de 0,22 µm recebe um líquido já quase limpo e sobrevive ao volume inteiro.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-18.png",
  largura: 44%,
  legenda: [A cascata em vista explodida. A cada estágio a população de partículas que segue adiante é menor e mais fina — o desenho mostra literalmente isso na densidade dos pontos dentro da seta. A última membrana é a que define a retenção; as anteriores existem para que ela chegue viva ao fim do volume.])

O segundo é o filtro #sigla("HEPA", [high efficiency particulate air — filtro de altíssima eficiência para retenção de partículas suspensas no ar]), que trata o ar de cabines de segurança, salas limpas e centros cirúrgicos, e cuja especificação — reter 99,97% das partículas de 0,3 µm — costuma ser lida errado. Ele não funciona como peneira. Partículas maiores são interceptadas ao esbarrar nas fibras e sofrem impactação inercial, porque são pesadas demais para acompanhar a curva que o ar faz ao contornar a fibra. Partículas muito pequenas, por outro lado, são retidas por *difusão*: leves o bastante para serem empurradas ao acaso pelas moléculas de ar, elas zigue-zagueiam e acabam colidindo com uma fibra. O resultado é contraintuitivo e vale guardar: *0,3 µm é o tamanho mais difícil de reter, e partícula menor que isso é capturada com eficiência maior, não menor* — por isso a especificação é escrita justamente nesse ponto, o pior caso.

Uma advertência prática fecha o subtópico, porque troca de mão com frequência: cabine de fluxo laminar horizontal protege o produto e empurra o ar da bancada na direção do rosto de quem trabalha. Quando o material é infeccioso, o equipamento correto é a cabine de segurança biológica, que aspira o ar da bancada e o devolve filtrado ao ambiente.

#subtopico("2.6 Frio, dessecação e liofilização: preservar não é matar")

Vale terminar esta PARTE pelo avesso dela. Os métodos anteriores existem para eliminar; os três deste subtópico existem para *conservar* — e entender por que eles conservam é o que impede o erro clínico mais frequente sobre temperatura.

O frio não mata: ele desacelera. A velocidade de toda reação enzimática cai com a temperatura, e abaixo de certo ponto o metabolismo praticamente cessa; a célula fica parada, viável, esperando. O frio é, portanto, bacteriostático — e é por isso que a geladeira preserva uma cepa no laboratório com a mesma eficiência com que preserva o micro-organismo indesejado no alimento. A escala usada na rotina de bancada faz sentido nessa lógica: 4 °C guarda material por dias, −20 °C por meses, −80 °C por anos, e o nitrogênio líquido a −196 °C mantém coleções de cepas por décadas.

Existe morte no congelamento, mas ela é um efeito colateral mecânico. Ao congelar, a água intracelular forma cristais de gelo que rompem membranas, e uma fração da população se perde — sobretudo em congelamento lento, que dá tempo para os cristais crescerem. É exatamente contra isso que se usa crioprotetor: glicerol e dimetilsulfóxido penetram na célula e reduzem a formação de cristais, aumentando a sobrevivência. *Repare no que isso implica: no congelamento, o objetivo é reduzir a morte, não aumentá-la.*

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-17.png",
  largura: 66%,
  legenda: [Os métodos que preservam. Em cima, dessecação ao sol e dois liofilizadores — no da direita, os frascos com o produto já seco em bloco poroso, pronto para reidratar. Embaixo, a escala térmica da rotina, de 4 °C ao nitrogênio líquido. Nenhuma dessas condições é microbicida: todas mantêm o micro-organismo viável e apenas o impedem de se multiplicar.])

A *dessecação* age pela via oposta, retirando a água em vez de imobilizá-la. Sem água livre, não há solvente para as reações e o metabolismo para. É o princípio da conservação de alimentos por secagem, milenar e eficaz. Mas a promessa continua sendo de inibição, não de morte, e a bibliografia registra sobrevivências longas em material seco: o agente da tuberculose permanece viável em escarro ressecado por semanas, e estafilococos sobrevivem em poeira de ambiente hospitalar.

A *liofilização* combina as duas ideias e produz o melhor método de conservação de longo prazo que existe. Congela-se o material e, mantendo-o congelado, aplica-se vácuo: a água passa direto do gelo ao vapor por *sublimação*, sem nunca voltar ao estado líquido. Como não há água líquida se movendo pelo interior da célula, não há a tensão de superfície nem a concentração de solutos que danificariam as estruturas numa secagem comum — e o material resultante, um bloco poroso e seco, reidrata quase intacto anos depois. É como se conservam coleções de cepas, hemoderivados e boa parte das vacinas que chegam ao posto em frasco de pó com diluente à parte.

#clinica-box("Refrigerar não é o mesmo que tornar seguro", [
A leitura de que "estava na geladeira, então estava seguro" ignora que o frio é estático. Duas consequências aparecem na prática. A primeira: espécies psicrotróficas continuam se multiplicando a 4 °C — *Listeria monocytogenes* é o exemplo clássico, e cresce em queijo, embutido e leite não pasteurizado guardados corretamente na geladeira, o que explica sua importância como causa de doença transmitida por alimento em gestantes e imunossuprimidos. A segunda: a toxina pré-formada por espécies que cresceram antes do resfriamento não desaparece com o frio nem, em vários casos, com o calor do reaquecimento. O frio compra tempo; ele não desfaz o que já aconteceu.
])

#parte-title("PARTE III — Agentes químicos e a decisão clínica")

#subtopico("3.1 Limpar antes: a matéria orgânica é o inimigo do desinfetante")

A PARTE I abriu com a sequência limpeza → desinfecção e pediu que ela fosse guardada. Chegou o momento de dizer por que a ordem é obrigatória, porque essa é a causa mais comum de falha na desinfecção hospitalar — e ela não tem nada a ver com escolher o produto errado.

Sangue, pus, secreção e resto de tecido interferem por dois caminhos independentes. O primeiro é *químico*: boa parte dos desinfetantes age oxidando ou alquilando grupos reativos, e proteínas e lipídios da matéria orgânica oferecem exatamente esses grupos em abundância. O agente reage com a sujeira, é consumido, e a concentração que sobra para atacar o micro-organismo é uma fração da concentração rotulada. O hipoclorito é o caso extremo — ele é tão ávido por matéria orgânica que a inativação é quase imediata, e é por isso que a recomendação para superfície com sangue usa concentrações muito mais altas do que a de rotina, para compensar a perda.

O segundo caminho é *físico* e não se resolve aumentando a dose. O filme residual funciona como uma cobertura sobre o micro-organismo: o agente precisa difundir através dele antes de encostar no alvo, e enquanto difunde está sendo consumido. Quando existe biofilme, o problema muda de escala: a comunidade produz uma matriz de polissacarídeo que retarda a penetração, e as células no interior, em metabolismo reduzido, são intrinsecamente menos sensíveis. Biofilme se remove por ação mecânica; produto sozinho não resolve.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-27.png",
  largura: 68%,
  legenda: [O protocolo de superfície em serviços de saúde, lido como sequência. As três primeiras linhas são limpeza — água, detergente com fricção, enxágue e secagem — e só depois entram os desinfetantes propriamente ditos. Repare que quase toda linha da metade inferior repete "após a limpeza": a etapa anterior não é recomendação, é condição de funcionamento.])

Daí a sequência canônica em quatro tempos: detergente com fricção, enxágue, desinfetante pelo tempo de contato indicado, enxágue e secagem. O enxágue intermediário parece dispensável e não é — resíduo de detergente aniônico neutraliza quimicamente o quaternário de amônio, que é catiônico, de modo que a etapa seguinte seria feita com um produto já inativado. E a fricção não é um detalhe de zelo: é ela que descola o material aderido e desestrutura o biofilme, sem o que nenhum dos dois problemas acima é resolvido.

#mini-resumo[O que ficou de pé: sem limpeza prévia, o desinfetante é consumido pela matéria orgânica antes de chegar ao micro-organismo e bloqueado pelo filme que resta sobre ele — o produto certo aplicado na ordem errada rende quase nada.]

#subtopico("3.2 Níveis de desinfecção e o critério que escolhe o agente")

Com a escada de resistência da PARTE I na mão, os níveis de desinfecção deixam de ser rótulos comerciais e viram cortes num eixo já conhecido. *Baixo nível* elimina bactérias vegetativas, fungos e vírus envelopados — para em micobactéria e em vírus não envelopado. *Nível intermediário* inclui esses dois grupos, e o divisor concreto é a micobactéria: agente de nível intermediário é tuberculicida. *Alto nível* elimina tudo, inclusive esporo em pequena quantidade, e só não é esterilização porque tolera carga elevada de esporo.

Saber a potência, porém, não diz o que usar. A regra que fecha essa lacuna cruza o nível com o *destino do artigo*, e é uma das ideias mais úteis que esta aula entrega. Artigo *crítico* é o que penetra tecido estéril, o sistema vascular ou uma cavidade normalmente estéril — bisturi, agulha, implante, instrumental cirúrgico. Ali qualquer sobrevivente é inoculado diretamente onde não há barreira, e a exigência é *esterilização*, sem alternativa. Artigo *semicrítico* toca mucosa íntegra ou pele não íntegra — endoscópio flexível, lâmina de laringoscópio, circuito de ventilação. A mucosa tem defesa própria contra carga baixa, mas não contra micobactéria nem vírus, e a exigência é *desinfecção de alto nível*. Artigo *não crítico* toca apenas pele íntegra — estetoscópio, manguito de pressão, comadre, superfície de mobiliário —, e nível baixo ou intermediário resolve.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-26.png",
  largura: 64%,
  legenda: [As classes químicas ordenadas pelo nível de atividade. Repare no topo: óxido de etileno, glutaraldeído e formaldeído com álcool são os de alto nível, e não por acaso são os que alquilam. No fundo, quaternário de amônio e compostos mercuriais, de baixo nível. E note a coluna do meio — cada linha tem uma faixa de concentração própria, porque fora dela a atividade declarada não se realiza.])

O caso do endoscópio digestivo é o exemplo que amarra tudo e costuma ser respondido errado. Ele não é esterilizado: é artigo semicrítico, não tolera calor, tem lúmens longos e é reprocessado por desinfecção de alto nível — glutaraldeído a 2% ou ácido peracético em máquina automatizada —, sempre depois de limpeza com escovação dos canais. O raciocínio completo tem três perguntas encadeadas: onde este artigo vai encostar, qual o nível que esse destino exige, e qual agente entrega esse nível sem destruir o material.

#confusao-prevista(
  titulo: "Alto nível não é esterilização",
  aluno_acha: [que desinfecção de alto nível e esterilização são o mesmo processo com nomes diferentes, já que "alto nível mata tudo"],
  mecanismo: [alto nível elimina todas as formas vegetativas, micobactérias, fungos e vírus, e alcança esporo em número pequeno — mas não garante a eliminação de carga elevada de esporo, e não é conduzido com a validação nem a embalagem que permitem manter a condição depois do processo. É a fronteira imediatamente abaixo da esterilização, e a distância entre as duas é exatamente o esporo.],
)

#subtopico("3.3 Como cada classe química mata")

Uma farmácia hospitalar guarda meia dúzia de frascos que parecem intercambiáveis e não são: cada classe química ataca um alvo diferente da célula, e é o alvo que determina até onde ela sobe na escada da PARTE I. Percorrer as classes por mecanismo — e não por nome — deixa o quadro do slide anterior legível de uma vez.

O *álcool* desnatura proteínas e dissolve lipídio de membrana, o que o torna rápido e potente contra bactérias vegetativas, fungos e vírus envelopados, e inútil contra esporo. A faixa de uso é 70–95%, e a razão de não se usar álcool absoluto é elegante: *a água é reagente*. Sem ela a desnaturação é ineficiente, o álcool coagula apenas a camada superficial da proteína e para de penetrar, e ainda evapora rápido demais para completar o tempo de contato. Diluir aumenta a potência — resultado que contraria toda a intuição de dosagem.

Os *halogênios* oxidam. Compostos clorados liberam ácido hipocloroso, que oxida os grupos tiol das enzimas e danifica ácido nucleico; a atividade cresce em pH ácido, porque é a forma não dissociada que penetra a célula, e desaba na presença de matéria orgânica. O iodo age por caminho parecido, halogenando resíduos de tirosina e oxidando grupos tiol; o iodóforo, em que o iodo está complexado a um carreador, libera iodo livre lentamente, o que reduz irritação e mancha — e exige respeitar o tempo de secagem, porque aplicar e limpar em seguida cancela o efeito.

Os *aldeídos* alquilam: eles transferem grupos alquila para as aminas e os tióis das proteínas e para as bases dos ácidos nucleicos, formando ligações cruzadas que travam a molécula. Como o mecanismo não depende de estrutura frágil nenhuma, é o único que alcança esporo entre os desinfetantes líquidos comuns — o que faz do glutaraldeído a 2% o padrão de alto nível para artigo semicrítico termossensível. O formaldeído compartilha o mecanismo e tem uso restrito por toxicidade; e diante de suspeita de príon ele é francamente contraindicado, porque fixa o agregado proteico em vez de destruí-lo.

Três classes fecham o repertório. Os *compostos fenólicos*, herdeiros diretos do ácido carbólico de Lister, rompem a membrana e precipitam proteínas; têm atividade residual sobre a superfície, o que é vantagem ambiental, mas são irritantes, absorvidos pela pele e tóxicos para sistema nervoso, fígado e rim — motivo pelo qual seu uso é restrito e contraindicado em berçário. Os *quaternários de amônio* são tensoativos catiônicos: a cabeça carregada positivamente encontra a superfície aniônica da membrana e a cadeia hidrofóbica se insere na bicamada, que passa a vazar. São de baixo nível, não alcançam micobactéria, esporo nem vírus não envelopado, são inativados por sabão aniônico e água dura — e soluções mal conservadas chegam a ser colonizadas por bacilos Gram-negativos. Os *oxidantes*, peróxido de hidrogênio e ácido peracético, geram radicais livres que atacam lipídio, proteína e ácido nucleico simultaneamente; são esporocidas em concentração adequada, decompõem-se em água, oxigênio e ácido acético, e por isso são a escolha crescente onde o resíduo importa.

#subtopico("3.4 Antisséptico: o mesmo princípio com um hospedeiro vivo por perto")

O repertório do subtópico anterior encolhe drasticamente quando o alvo está sobre tecido vivo, e é útil ver que o corte não é de potência: glutaraldeído mataria muito bem a microbiota da mão, e destruiria a mão junto. *A restrição da antissepsia é o dano colateral*, e é ela que explica por que o arsenal de pele é pequeno e por que cada item dele tem um perfil próprio.

A demonstração histórica dessa ideia veio antes da microbiologia existir. Em 1846, Ignaz Semmelweis notou que a mortalidade por febre puerperal na enfermaria atendida por médicos — que faziam partos, autópsias e cirurgias no mesmo turno — chegava ao triplo da enfermaria atendida por parteiras. Ele não sabia qual era o agente; deduziu que algo era carregado nas mãos e determinou lavagem com solução de cal clorada antes de qualquer exame. A mortalidade caiu de 12,24% para 3,04% no primeiro ano e para 1,27% no segundo. Duas décadas depois, já sob influência de Pasteur, Joseph Lister levou o mesmo raciocínio ao centro cirúrgico com ácido carbólico sobre instrumentos e sobre o campo operatório, e as infecções pós-operatórias despencaram.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-22.png",
  largura: 58%,
  legenda: [O experimento natural que fundou a antissepsia. Duas enfermarias no mesmo hospital, com a única diferença relevante sendo quem atendia — e, portanto, o que essas mãos haviam tocado antes. A queda de 12,24% para 1,27% em dois anos foi obtida com uma intervenção única, décadas antes de existir uma explicação para ela.])

No arsenal atual, o álcool a 70% é o agente de ação mais rápida e potente sobre a pele, e não tem persistência nenhuma: assim que evapora, a atividade acaba. A *clorexidina* funciona por outro caminho — ela rompe a membrana e, sobretudo, liga-se ao estrato córneo e às proteínas da pele, permanecendo ativa por horas depois da aplicação. Essa #termo-nota[atividade residual][permanência do agente ligado ao tecido, mantendo efeito antimicrobiano por horas após a aplicação] é o que decide as escolhas de maior impacto: preparo de pele para cirurgia e para inserção de cateter venoso central usam clorexidina alcoólica justamente porque somam o efeito imediato do álcool à persistência da clorexidina durante todo o procedimento. O iodopovidona ocupa espaço parecido, com persistência menor e a exigência do tempo de secagem.

#atencao-box("Fricção alcoólica não cobre todos os cenários", [
A preparação alcoólica para as mãos é obrigatória nos serviços de saúde brasileiros e é preferida na rotina por rapidez e adesão. Mas o álcool depende de lipídio a dissolver e de proteína a desnaturar, e há duas situações em que ele falha: diante de vírus não envelopado, como o norovírus, e diante de esporo, como o de *Clostridioides difficile*. Nesses casos a conduta é água e sabão, cuja eficácia vem da remoção mecânica, e hipoclorito na superfície. A mesma limitação vale para mão com sujidade visível, em que a matéria orgânica bloqueia o contato — o mecanismo do subtópico 3.1 reaparece aqui, agora sobre a pele.
])

Uma última precisão evita uma expectativa errada: a antissepsia da pele reduz drasticamente a microbiota *transitória*, adquirida por contato, e apenas parte da microbiota *residente*, que habita folículos e glândulas e é continuamente reposta. O campo cirúrgico nunca é estéril — é um campo de carga muito baixa, mantido baixo por barreira física e pela persistência do agente.

#subtopico("3.5 Esterilizar o que não aguenta calor — e a pergunta que fecha a aula")

Sobrou o problema mais difícil da aula, o mesmo que se apresenta diante de um instrumental usado em procedimento com suspeita de tuberculose: o material precisa ser estéril, e não tolera 121 °C. Duas tecnologias resolvem esse caso, e as duas usam química no lugar do calor.

O *óxido de etileno* é um gás alquilante. Ele transfere grupos alquila para bases do DNA e para grupos funcionais de proteínas, com o mesmo mecanismo dos aldeídos — e por ser gás, atravessa embalagens permeáveis e alcança lúmens estreitos, o que nenhum líquido faz bem. O ciclo roda a 55–60 °C, em concentração de centenas de miligramas por litro, e é justamente essa combinação de eficácia e penetração que o mantém em uso para material termossensível complexo. O preço é sério: o resíduo é tóxico, mutagênico e carcinogênico, o gás é inflamável, e o material exige *aeração* prolongada antes de ser liberado. O ciclo completo se conta em horas, não em minutos.

#figura-nebli("/figuras/micro-04-controle-microbiologico/slide-12.png",
  largura: 62%,
  legenda: [Esterilização por plasma de peróxido de hidrogênio. Na câmara sob vácuo, o campo elétrico de alta frequência ioniza o peróxido vaporizado e o converte no quarto estado da matéria — a luz violeta da foto inferior é o plasma em atividade. O que mata são os radicais livres e a radiação ultravioleta gerados ali; ao fim do ciclo, o que resta é água e oxigênio.])

O *plasma de peróxido de hidrogênio* resolve boa parte desses inconvenientes. Peróxido vaporizado é injetado numa câmara sob vácuo e submetido a um campo elétrico de alta frequência, que o converte em plasma — o quarto estado da matéria, em que íons e elétrons livres colidem com átomos e moléculas. Desse estado excitado saem radicais livres altamente reativos e radiação ultravioleta, e é essa combinação que oxida lipídio, proteína e ácido nucleico do micro-organismo. A temperatura fica entre 35 °C e 45 °C, o material vai embalado em polipropileno permeável ao gás, e a fase esterilizante dura de 5 a 20 minutos. Melhor ainda, os produtos finais são água e oxigênio — não há aeração a esperar. Os limites são conhecidos e específicos: celulose absorve o peróxido e aborta o ciclo, o que exclui papel e tecido de algodão, e lúmens muito longos e estreitos podem não receber concentração suficiente.

Fica a pergunta com que a aula se encerra, e ela é melhor do que parece: todo agente esporocida é também esterilizante. A resposta é não, e o motivo reorganiza tudo o que veio antes. Atividade esporocida é uma propriedade condicional — depende de concentração e de tempo de contato —, enquanto esterilização é um *processo validado*, com parâmetros definidos, monitoramento por indicador biológico e uma probabilidade de falha aceita de antemão. O glutaraldeído a 2% é o exemplo canônico: em vinte a trinta minutos de imersão ele entrega desinfecção de alto nível; para eliminar carga elevada de esporo, precisa de horas. A molécula é a mesma nos dois casos; o que muda é o processo. E há ainda uma limitação prática que sela a diferença: um artigo esterilizado por imersão em líquido não pode ser embalado durante o processo, de modo que a esterilidade se perde no enxágue e no manuseio — razão pela qual, sempre que o material tolera, o calor úmido continua sendo a escolha.

#conclusao-box[
Uma única ideia sustenta esta aula inteira: *o controle microbiano não é a eliminação de "germes" em bloco, e sim a remoção de uma fração da população por unidade de tempo, contra um alvo que carrega barreiras físicas identificáveis*. Tudo o mais é consequência dessa frase.

Ela explica a matemática. Se a morte é uma fração constante por unidade de tempo, a curva é exponencial, nunca toca o zero, e "mata 99,9%" significa três reduções decimais e um resíduo que importa conforme o volume — daí a esterilidade ser definida como probabilidade de 10⁻⁶, e não como ausência comprovada. Ela explica a escada de resistência, porque cada degrau é uma barreira nomeável: membrana exposta no micoplasma, envelope lipídico dissolúvel, parede vegetativa, capsídeo proteico nu, capa de ácido micólico, núcleo desidratado com dipicolinato no esporo, parede do oocisto e, no topo, a ausência de qualquer estrutura vulnerável no príon. E ela explica por que todo método é descrito por um par de parâmetros e por um teto: 121 °C por 15 minutos de vapor saturado, porque a água é reagente da desnaturação e a condensação entrega calor latente; 180 °C por uma hora de ar seco, porque sem água só resta oxidação lenta; 0,22 µm que retém bactéria e deixa passar vírus; 254 nm que solda timinas sem penetrar um milímetro de sombra; álcool a 70% que dissolve lipídio e não toca esporo.

Na clínica isso vira uma sequência de três perguntas encadeadas. Onde este artigo vai encostar — tecido estéril, mucosa íntegra ou pele íntegra. Qual nível esse destino exige — esterilização, alto nível ou nível baixo a intermediário. E qual agente entrega esse nível sem destruir o material — vapor se ele tolera calor e umidade, óxido de etileno ou plasma de peróxido se não tolera, alto nível por imersão se o artigo for semicrítico. É esse encadeamento que responde ao caso do instrumental contaminado por micobactéria, ao do endoscópio digestivo e ao da superfície com sangue, sem precisar decorar nenhuma lista.

O próximo passo natural muda o cenário do objeto para o organismo. Todos os agentes desta aula são indiscriminados: matam a bactéria e machucariam a célula humana com a mesma facilidade, e é justamente por isso que ficam do lado de fora do corpo. Combater uma infecção já instalada exige moléculas que atinjam alvos existentes na bactéria e ausentes em nós — a parede, o ribossomo de tipo bacteriano, a enzima que desenrola o cromossomo circular. Essa exigência de seletividade, e o que a bactéria faz para escapar dela, é o assunto que vem a seguir.
]
