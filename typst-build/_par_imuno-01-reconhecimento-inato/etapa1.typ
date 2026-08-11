#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  O sistema imune tem duas maneiras de olhar para um tecido, e elas fazem perguntas diferentes. Os receptores clonais — o #sigla("TCR", [receptor de células T]) e os anticorpos — perguntam _quem é você_: leem antígenos, um por um, com um repertório gerado ao acaso. Os receptores para padrões moleculares perguntam antes disso, e a pergunta é outra: _este tecido ainda está em ordem?_ Eles não identificam o invasor pelo nome; identificam assinaturas moleculares que só aparecem quando há micro-organismo ou quando há dano. Esta aula percorre essa segunda pergunta do começo ao fim. Primeiro, por que ela vem antes e o que exatamente esses receptores leem. Depois, o que acontece dentro da célula quando um deles é acionado — as vias moleculares dos toll-like receptors e a montagem do inflamassoma. Em seguida, as quatro estratégias com que a resposta inata tenta devolver o tecido à homeostasia. E, por fim, a linguagem com que tudo isso é coordenado: as citocinas. A régua que atravessa a aula é uma só — o reconhecimento inato é o sensor da homeostasia, e é ele que autoriza, ou não, a resposta que vem depois.
]

#parte-title("PARTE I — Quem pergunta primeiro: os PRR e a perda da homeostasia", primeira: true)

#subtopico("1.1 — Recapitulando: um repertório aleatório precisa de seleção")

Vale começar de onde a aula anterior parou. O repertório dos receptores clonais é, em princípio, _completo_: existe linfócito capaz de reconhecer praticamente qualquer molécula. Ele consegue isso porque é gerado aleatoriamente, por recombinação, e não a partir de um catálogo pré-definido de alvos. O preço dessa aposta é óbvio: se a geração é ao acaso, nascem também receptores que reconhecem o próprio organismo. A correção vem por #termo-nota[seleção][processo, nos órgãos linfoides primários, em que linfócitos cujos receptores reconhecem antígenos próprios são eliminados ou inativados], e ela acontece num lugar específico — os órgãos linfoides primários, onde o antígeno próprio funciona como filtro. O resultado é um repertório que, de maneira geral, distingue o próprio do não-próprio.

Essa distinção, porém, não é completa nem suficiente. Não é completa porque ela falha, e é dessa falha que nascem as doenças autoimunes. E não é suficiente porque, se a única regra fosse "não-próprio dispara resposta", nós responderíamos contra a comida que ingerimos e contra a microbiota que nos habita — o que evidentemente não acontece. Falta, portanto, uma segunda camada de informação. É ela que esta aula descreve.

#subtopico("1.2 — Tolerância ou resposta: quem decide é o estado do tecido")

O reconhecimento específico de um antígeno não tem sempre o mesmo desfecho. Ele pode levar a uma resposta que tenta eliminar o que foi reconhecido — é isso que se chama, em sentido estrito, de resposta imune — ou pode levar a uma adaptação em que o sistema aceita a presença daquele antígeno e não tenta eliminá-lo, o que se chama tolerância imunológica. Os dois desfechos são ativos e os dois geram memória: o sistema se ajusta para lidar com aquele mesmo estímulo da mesma maneira na próxima vez.

Qual é o fator que decide entre um e outro? O principal fator que decide entre tolerância e resposta é o estado homeostático do tecido de onde aquele antígeno veio quando foi levado ao sistema imune. Não é a origem própria ou estranha da molécula, e sim o contexto em que ela foi capturada. É essa a questão essencial da imunologia clínica que a aula levanta: num transplante, o desejável seria induzir tolerância ao órgão enxertado; num tumor, o desejável seria responder e eliminá-lo. O problema prático é que, no indivíduo que tem o tumor, o sistema já aprendeu que aquele tecido não é problema.

#clinica-box("Por que o tumor escapa", [O tumor cresce dentro de um tecido que o sistema lê como homeostático. Suas moléculas chegam aos órgãos linfoides sem o contexto de perigo, e o desfecho aprendido é tolerância. Boa parte da imuno-oncologia moderna consiste, justamente, em fabricar artificialmente o contexto que faltou — inflamação local, adjuvantes, bloqueio de checkpoints — para reconverter tolerância em resposta.])

#subtopico("1.3 — O reconhecimento no sistema imune é hierárquico")

Junte as duas peças e aparece a arquitetura da aula. O reconhecimento no sistema imune é hierárquico, e a primeira pergunta não é sobre antígeno, é sobre homeostasia: existe homeostasia neste tecido? Na hierarquia do reconhecimento imune, os receptores que respondem a essa primeira pergunta são os #sigla("PRR", [pattern recognition receptors — receptores para padrões moleculares]), e é a resposta deles que desencadeia a imunidade inata. Ao mesmo tempo, e em paralelo, a constituição molecular daquele tecido está sendo capturada e seus antígenos apresentados aos receptores clonais nos órgãos linfoides secundários.

A ponte entre as duas maneiras de reagir é a apresentação de antígenos. A célula apresentadora de antígenos faz duas coisas simultaneamente: captura moléculas do tecido e avalia o estado homeostático desse tecido. Ela processa e apresenta ao linfócito T carregando, junto com o antígeno, a informação de contexto que os PRR produziram. É por isso que a ordem importa: sem o sinal da imunidade inata, o mesmo antígeno tende à tolerância; com ele, tende à resposta.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-06.png",
  largura: 66%,
  legenda: [As duas camadas de leitura. Em cima, os PRR lendo padrões moleculares e respondendo pela homeostasia — imunidade inata. Embaixo, TCR e imunoglobulinas lendo antígenos — imunidade adquirida. A camada de cima é que informa o contexto para a de baixo.])

#subtopico("1.4 — O que os PRR leem: PAMP e DAMP")

Os PRR não reconhecem moléculas individuais como um anticorpo reconhece um epítopo; reconhecem _padrões_ — arranjos moleculares repetidos, conservados, que sinalizam uma de duas coisas.

Os padrões moleculares associados a patógenos são chamados de #sigla("PAMP", [pathogen-associated molecular patterns]): são assinaturas típicas de micro-organismos, como o lipopolissacarídeo da parede bacteriana, o peptidoglicano ou o RNA de fita dupla viral. Como são estruturas de que o micro-organismo não pode abrir mão, o sistema pôde se dar ao luxo de codificá-las na linha germinativa — o receptor já nasce pronto para elas.

Os padrões moleculares associados a dano tecidual são chamados de #sigla("DAMP", [damage-associated molecular patterns]): são moléculas do próprio hospedeiro que normalmente estão trancadas dentro da célula e que, extravasadas, denunciam morte ou lesão. Eles explicam por que uma inflamação estéril — um infarto, um trauma, um cristal — dispara resposta inata sem nenhum micro-organismo envolvido.

#confusao-prevista(
  titulo: "DAMP não é a versão fraca de PAMP",
  aluno_acha: [aluno acha que DAMP é um estímulo menor, um "PAMP do próprio", que gera uma resposta mais discreta],
  mecanismo: [os dois entram pelos mesmos receptores e desencadeiam as mesmas vias. A diferença é de _origem_ do sinal, não de intensidade: PAMP diz "há micro-organismo", DAMP diz "há dano". Um infarto ou um cristal de urato disparam inflamação inata robusta sem nenhum patógeno presente.],
)

Uma nota histórica ajuda a fixar o conceito. Quem primeiro propôs essa leitura foi Polly Matzinger, com o termo _danger_: o que dispara a resposta não é a estraneidade da molécula, é o perigo para o organismo. A sigla DAMP nasceu dessa proposta e ficou.

#subtopico("1.5 — As famílias de PRR e onde cada uma vigia")

Existem várias famílias de PRR, e a lógica de descoberta foi sempre a mesma: identificou-se um receptor e, em seguida, vários parecidos com ele. O que interessa reter não é a lista de nomes, e sim uma ideia estrutural — os PRR estão distribuídos por toda a célula, porque as ameaças também estão. Há PRR na membrana plasmática, em membranas internas, soltos no citoplasma e até no núcleo, e essa distribuição é funcional: cada compartimento é vigiado por quem consegue encontrar ali o padrão que interessa.

Os #sigla("TLR", [toll-like receptors]) são proteínas de membrana. Todo TLR é um receptor de membrana, seja da membrana plasmática, seja da membrana do lisossomo — nenhum deles fica solto no citosol. Os que reconhecem componentes de superfície do micro-organismo ficam voltados para fora; os que reconhecem ácidos nucleicos ficam nas membranas internas, onde só encontram material genético depois que a partícula foi internalizada e degradada. Os #sigla("NLR", [NOD-like receptors]) aparecem em membranas e no citoplasma. Os #sigla("RLR", [RIG-like receptors]) são citoplasmáticos: RIG-I e MDA5 detectam RNA viral livre no citoplasma, que é exatamente onde um vírus replicando deixa esse rastro. Os #sigla("ALR", [AIM2-like receptors]), como AIM2 e IFI16, vigiam o núcleo. Somam-se ainda os receptores de lectina tipo C, como a dectina-1, e os _scavenger receptors_, como CD36 e CD68, ambos de membrana.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-08.png",
  largura: 78%,
  legenda: [As famílias de PRR pela localização. Repare que a tabela não é uma lista de nomes: é um mapa de compartimentos. Membrana para o que vem de fora, citoplasma para o que replica dentro, núcleo para o DNA que não deveria estar ali. Ao pé, as duas classes de padrão — DAMP e PAMP — convergindo para a mesma resposta.])

Há ainda uma família que não aparece na tabela porque não é celular. Existem proteínas solúveis do plasma capazes de reconhecer padrões moleculares na superfície do alvo e marcá-lo; o sistema de proteínas plasmáticas que funciona como um sistema solúvel de reconhecimento de padrões é o complemento. Ele será estudado à parte, mas convém já registrar que reconhecimento de padrão não é privilégio de receptor de membrana.

#mini-resumo[O repertório clonal é aleatório e depende de seleção nos órgãos linfoides primários, mas próprio versus não-próprio não basta para decidir o desfecho. O que decide entre tolerância e resposta é o estado homeostático do tecido de origem do antígeno. Por isso o reconhecimento é hierárquico: os PRR perguntam primeiro se há homeostasia, lendo PAMP (assinatura de micro-organismo) e DAMP (assinatura de dano). Eles estão distribuídos por compartimento — TLR em membranas, NLR em membranas e citoplasma, RLR no citoplasma, ALR no núcleo — e o complemento é a versão solúvel do mesmo princípio.]

#parte-title("PARTE II — Da ativação do receptor à decisão da célula")

#subtopico("2.1 — Como um TLR percebe que o ligante chegou")

Um receptor precisa converter um evento de ligação em um sinal intracelular, e o TLR faz isso mudando de forma. Quando um ligante se liga a dois TLR que estavam isolados na membrana, a sinalização começa porque os receptores sofrem dimerização — as porções intracelulares se aproximam e passam a servir de plataforma de encaixe para os adaptadores. Há também uma segunda possibilidade: o dímero já existe pré-formado, e o ligante, ao se encaixar nele, muda a sua conformação. O efeito é o mesmo — o domínio intracelular assume o arranjo capaz de recrutar adaptador —, mas sem que dois receptores precisem se encontrar.

Vale um parêntese sobre o nome, porque ele ajuda a lembrar de onde a família veio. _Toll_ é uma palavra alemã que significa algo como "bacana", e foi dado à molécula descoberta na drosófila, onde seu papel inicial é a embriogênese. Os receptores humanos foram batizados de _toll-like_ por semelhança estrutural com ela — e só depois se descobriu que essa arquitetura servia ao reconhecimento de padrões moleculares.

O exemplo canônico de par receptor–ligante desta família é o TLR4: o ligante típico do TLR4 é o lipopolissacarídeo bacteriano, a endotoxina de bactérias gram-negativas. Vale a advertência que o professor faz sobre essas listas: o ligante listado é o _típico_, não o exclusivo. Não seria plausível que existissem apenas onze padrões moleculares no mundo; o mesmo TLR4 reconhece outras estruturas, inclusive próprias, e é isso que torna a fronteira entre reconhecimento de patógeno e reconhecimento de dano menos nítida do que a tabela sugere.

#subtopico("2.2 — Dois adaptadores, dois programas: MyD88 e TRIF")

A partir do receptor ativado, o sinal segue por um caminho longo, mas com dois grandes portões de entrada. O principal adaptador proximal que transduz o sinal da maioria dos TLR é o #sigla("MyD88", [myeloid differentiation primary response protein 88]). A via que parte dele passa por várias quinases intermediárias — a família IRAK, entre outras — e termina ativando fatores de transcrição. A sinalização por MyD88 converge sobre o fator de transcrição #sigla("NF-κB", [nuclear factor kappa B]), que no núcleo liga os genes das citocinas inflamatórias; junto com ele atua a AP-1. O produto final desse ramo são citocinas e quimiocinas inflamatórias — ou seja, inflamação, chegada de fagócitos e tentativa de restaurar a homeostasia.

O segundo portão é o #sigla("TRIF", [TIR domain-containing adaptor protein inducing interferon beta]), e o ramo que parte dele ativa outra classe de fatores de transcrição, os #sigla("IRF", [interferon regulatory factors]). Por ativar esses fatores, o ramo do TRIF leva à produção de interferons do tipo I. E os interferons do tipo I, como veremos adiante, têm atividade antiviral e participam da ativação de linfócitos T.

O ponto conceitualmente mais importante desta parte não é a lista dos nomes, e sim o que acontece entre as duas vias. Alguns TLR sinalizam por MyD88, outros por TRIF, alguns pelos dois — e as duas vias se cruzam. Não é o MyD88 que ativa diretamente o NF-κB: há uma cadeia de moléculas no caminho, e nessa cadeia existem ramificações. Por isso um ligante que aciona um TLR tipicamente "de MyD88", que deveria produzir citocinas inflamatórias, pode acabar produzindo interferon. A via molecular desenhada no esquema é uma simplificação útil, não um trilho fechado.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-18.png",
  largura: 82%,
  legenda: [O leque de consequências da ativação de um TLR. À esquerda, DAMP e PAMP chegando ao receptor, que dimeriza ou muda de conformação. No centro, os dois adaptadores — MyD88 e TRIF — cruzando-se. À direita, os cinco desfechos: citocinas inflamatórias por NF-κB e AP-1, sobrevivência por AKT, ativação do inflamassoma, apoptose por caspase 8 e interferons do tipo I pelos IRF.])

#atencao-box("Todos os caminhos levam às mesmas moléculas — e isso não é um erro do esquema", [Se cada TLR reconhece um ligante diferente e produz um efeito diferente, mas todos convergem para os mesmos adaptadores e fatores de transcrição, como a especificidade sobrevive? A resposta está na anatomia interna da célula. Não adianta ativar o MyD88 se ele não estiver perto do IRAK 4 e do IRAK 1 que ele precisa ativar. Essas moléculas não flutuam soltas num saco homogêneo: são ativamente levadas para determinados sítios, e a pré-ativação da célula muda essa distribuição. O que decide o desfecho, portanto, é a composição do complexo que se monta naquele lugar e naquele momento — e é por isso que a mesma via pode dar respostas diferentes.])

#subtopico("2.3 — As outras consequências: sobrevivência, apoptose e inflamassoma")

Citocinas e interferons são os desfechos mais lembrados, mas o esquema mostra outros três, e vale nomeá-los porque cada um é um programa celular distinto.

Além da inflamação, a sinalização por TLR pode promover sobrevivência celular por meio da AKT — a mesma quinase que, em outros contextos, sustenta células que deveriam morrer. Em direção oposta, a sinalização por TLR também pode levar à apoptose, ativando a caspase-8. E há uma terceira consequência que abre a próxima seção: além de citocinas e interferons, a sinalização por TLR pode acionar outra plataforma molecular, o inflamassoma, por meio do TRIF.

Que a mesma ativação possa produzir sobrevivência ou morte parece contraditório, mas não é: elas não acontecem todas ao mesmo tempo nem na mesma proporção. O que pende a balança é a disposição e a quantidade de TLR naquela célula e, sobretudo, quais outros sinais ela está recebendo simultaneamente.

#subtopico("2.4 — O inflamassoma: montar a plataforma para maturar a citocina")

Inflamassomas são plataformas moleculares — aglomerados em que uma molécula se junta a outra, e a outra, até formar um complexo funcional — que se montam a partir da ativação de determinados PRR. A função desse complexo é muito específica: a maturação de citocinas pró-inflamatórias.

Vale desmontar a palavra "maturação", porque é nela que está o mecanismo. O gene ativado por um fator de transcrição gera uma proteína que ainda não é funcional: uma pró-citocina. O inflamassoma não transcreve essa citocina; ele age sobre o precursor já pronto, clivando-o e liberando a forma ativa. São dois eventos distintos, com controles distintos.

Quem executa o corte é uma enzima. A enzima que o inflamassoma montado ativa é a caspase-1, uma protease que cliva a pró-IL-1-beta e a pró-IL-18. As duas citocinas resultantes são centrais na reação inflamatória: a interleucina-1-beta, uma das primeiras citocinas descritas, e a interleucina-18.

Daí decorre a exigência mais elegante do sistema, o chamado #termo-nota[priming][primeiro sinal, geralmente via TLR, TNF ou IL-1beta, que induz a transcrição do precursor pró-IL-1-beta e sem o qual o inflamassoma não tem substrato para clivar]: um inflamassoma montado não consegue liberar IL-1-beta se um sinal pró-inflamatório anterior não tiver induzido a pró-IL-1-beta. Uma célula que recebe apenas o sinal de montagem provavelmente não vai adiante — falta-lhe substrato. São necessários dois sinais, um para fabricar o precursor e outro para cortá-lo, e essa arquitetura de dupla checagem é o que impede que uma citocina tão potente seja liberada por acidente.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-21.png",
  largura: 84%,
  legenda: [À esquerda, a montagem do inflamassoma NLRP3: os sinais de perigo convergem, NLRP3 se oligomeriza através dos domínios NACHT, recruta o ASC pelos domínios PYD e este recruta a pró-caspase-1 pelos CARD. À direita, a mesma história em cinco passos. Repare no rodapé da figura: o _priming_ por TLR, TNF ou IL-1β é o que produz a pró-IL-1β que a caspase-1 vai clivar.])

Falta responder quais PRR montam inflamassoma. A família de receptores cujos membros montam inflamassomas é a dos NOD-like receptors, e dentro dela é preciso separar duas turmas. NLRP1, NLRP3 e o IPAF montam de fato o complexo; junta-se a eles o AIM2, da família ALR. Já os NOD propriamente ditos, embora pertençam à mesma família, fazem outra coisa: os NOD ficam soltos no citoplasma, reconhecem produtos bacterianos e ativam o NF-κB em vez de montar inflamassoma. É um bom exemplo de que pertencer à mesma família estrutural não implica ter a mesma função efetora.

#clinica-box("Inflamassoma e doença", [Alterações em moléculas do inflamassoma estão fortemente associadas a doenças inflamatórias hereditárias — as síndromes autoinflamatórias, raras, em que o complexo se ativa sem estímulo — e também a doenças inflamatórias adquiridas comuns, como a gota, em que o cristal de urato é o sinal de perigo. Bloquear a IL-1 é, hoje, tratamento real em várias dessas condições.])

#mini-resumo[O TLR converte ligação em sinal por dimerização ou por mudança conformacional de um dímero pré-formado, e seu ligante típico mais citado é o LPS pelo TLR4. Do receptor saem dois adaptadores: MyD88, que converge sobre NF-κB e AP-1 e produz citocinas e quimiocinas inflamatórias, e TRIF, que ativa os IRF e produz interferons do tipo I — com cruzamento entre as vias. Há ainda sobrevivência por AKT, apoptose por caspase-8 e ativação do inflamassoma. O inflamassoma é uma plataforma montada por NLR que ativa a caspase-1, a qual cliva pró-IL-1-beta e pró-IL-18 — mas só funciona se um sinal anterior de priming tiver produzido o precursor.]

#parte-title("PARTE III — As quatro estratégias de restaurar a homeostasia")

Desencadeada a resposta inata, o que ela efetivamente faz? A aula organiza as consequências em quatro estratégias, e a lógica delas é a de uma equipe de emergência: salvar quem ainda dá para salvar, eliminar quem já não dá, limpar a área e chamar reforço.

#subtopico("3.1 — Salvar as vizinhas: os interferons do tipo I")

A primeira estratégia é impedir que o problema se espalhe, e o exemplo perfeito é a resposta antiviral. Quando um vírus adere a uma célula e injeta seu ácido nucleico, a célula infectada responde imediatamente produzindo interferon. Esse interferon é liberado e alcança as células vizinhas. Os vírus produzidos ali também vão alcançar essas vizinhas — mas, se elas estiverem sob ação do interferon, o interferon bloqueia a replicação viral dentro delas.

O desfecho é característico e vale ser dito sem eufemismo: a célula que produziu o interferon não se salva. Ela será destruída pelo vírus de qualquer maneira. O que ela faz é proteger as células ao lado — por isso o professor chama o interferon de uma ação solidária da célula infectada. É um mecanismo essencial de proteção antiviral, e é fácil esquecê-lo quando se pensa apenas na resposta adaptativa.

#figura-lateral("/figuras/imuno-01-reconhecimento-inato/slide-10.png",
  lado: "right",
  largura-figura: 46%,
  texto: [O interferon também tem efeitos sistêmicos, e eles são mais familiares do que parece. Boa parte dos sintomas da gripe — febre, dor no corpo, prostração — é produzida pelo interferon, e não pelo vírus em si. Isso reposiciona o sintoma: o mal-estar não é o dano causado pelo agente, é o custo da defesa montada contra ele.],
  legenda: [A célula infectada libera interferon; as vizinhas ficam protegidas. Ao lado, os efeitos sistêmicos.])

#subtopico("3.2 — Eliminar a célula doente: a citotoxicidade celular")

A segunda estratégia é remover a célula que já está comprometida. O nome "citotoxicidade" sugere destruição de fora para dentro, e é exatamente essa a imagem que precisa ser corrigida. A citotoxicidade celular não destrói a célula-alvo de fora: ela induz a célula-alvo a morrer por apoptose. É uma morte ativa, executada pelo programa da própria célula — um suicídio induzido, não um tiro.

O processo tem etapas. A célula efetora identifica o alvo, por receptores clonais quando vem da imunidade adquirida ou por receptores inatos quando não precisa de nenhuma adaptação prévia. Feito o reconhecimento, as duas células se encontram e há sinalização. Essa sinalização pode ocorrer por desgranulação — a célula citotóxica possui grânulos com substâncias capazes de induzir a morte do alvo — ou por moléculas de membrana. Além da liberação de grânulos citotóxicos, a célula efetora pode disparar a apoptose do alvo por sinalização de membrana através do FasL, que engata o Fas na célula-alvo. Essas moléculas já estavam lá o tempo todo; o que o reconhecimento específico faz é aproximá-las. Ao final, o alvo entra em apoptose e a célula citotóxica fica livre para procurar outros alvos.

#subtopico("3.3 — Limpar a área: a fagocitose")

A terceira estratégia é a mais antiga de todas — a fagocitose funciona desde os protozoários e foi incorporada à nossa fisiologia como processo ancestral. Ela também se desenvolve em etapas, e cada etapa tem um nome que vale reter.

A primeira etapa da fagocitose é a migração celular dirigida em direção ao alvo, isto é, a quimiotaxia. O fagócito precisa primeiro chegar perto, e ele é chamado por moléculas quimiotáticas geradas de várias formas: pelo próprio micro-organismo, que libera produtos reconhecíveis, e pelo complemento, aquele sistema solúvel de reconhecimento de padrões.

A segunda etapa é a adesão. Não basta encostar: a partícula pode não interagir adequadamente com a membrana do fagócito. Os fagócitos têm receptores de padrões moleculares que identificam padrões comuns em alvos fagocitáveis, mas o sistema também fabrica moléculas que grudam na partícula e para as quais existem receptores na célula fagocítica. A adesão da partícula ao fagócito é facilitada por moléculas que recobrem o alvo, num processo chamado opsonização.

Aderida a partícula, começa o englobamento. A membrana do fagócito se fecha em torno da partícula por interações sucessivas entre receptores e ligantes, um processo descrito como o fechamento de um zíper — cada novo receptor que engata puxa mais um pedaço de membrana para cima do alvo. O resultado é o fagossoma, uma vesícula fechada com a partícula dentro.

Falta destruir o conteúdo, e são dois mecanismos somados. A fusão do fagossoma com os lisossomas forma o fagolisossomo, que traz as enzimas hidrolíticas para dentro. Em paralelo, na membrana do fagossoma monta-se um sistema gerador de radicais livres de oxigênio, e o aumento abrupto do consumo de oxigênio que acompanha esse processo é a explosão respiratória. Uma célula fagocitando consome muito mais oxigênio do que uma célula em repouso — não para produzir ATP, mas para produzir radicais destrutivos. Enzimas e radicais livres, juntos, degradam a partícula fagocitada.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-12.png",
  largura: 74%,
  legenda: [As etapas da fagocitose em sequência. Repare que as três primeiras — localização, adesão e fechamento do zíper — são moduláveis, isto é, o sistema pode acelerá-las ou travá-las. É aí que atuam a quimiotaxia e a opsonização.])

#subtopico("3.4 — Chamar reforço: mediadores e febre")

A quarta estratégia, na prática, está embutida em todas as outras: produzir fatores de crescimento, citocinas, quimiocinas e demais mediadores que modulam o ambiente. Eles mudam quem chega ao tecido — chamando um tipo celular e não outro — e mudam a função das células que já estão ali.

Esses produtos não ficam confinados ao sítio da reação. Eles provocam alterações sistêmicas, e a mais visível delas é a febre. Convém tratá-la com cuidado, porque a intuição clínica cotidiana é de que febre é sintoma a ser suprimido. Os dados dizem outra coisa. O lagarto não controla a própria temperatura por metabolismo: ele a regula expondo-se mais ou menos ao sol. Se um lagarto infectado é impedido de se aquecer, ou seja, impedido de desenvolver febre, sua mortalidade aumenta muito. Isso mostra que a febre é um mecanismo de defesa, e não um efeito colateral inútil da inflamação.

#mini-resumo[As quatro estratégias da resposta inata: salvar as vizinhas com interferon do tipo I, que não salva a célula infectada mas bloqueia a replicação viral ao lado e responde por boa parte dos sintomas da gripe; eliminar a célula doente por citotoxicidade, que induz apoptose por grânulos ou por FasL-Fas em vez de destruir de fora; limpar a área por fagocitose — quimiotaxia, opsonização, zíper, fagolisossomo e explosão respiratória; e chamar reforço com mediadores, cujos efeitos sistêmicos incluem a febre, que o experimento do lagarto mostra ser defesa.]

#parte-title("PARTE IV — A linguagem da resposta: citocinas e outros mediadores")

#subtopico("4.1 — O que é uma citocina")

Nada do que foi descrito funciona sem informação circulando entre as células. Citocina é o nome genérico de um produto proteico — em geral glicoproteína — que a célula produz para se comunicar com outras células. Duas propriedades definem o comportamento dessa classe.

A primeira é que uma citocina age sobre muitos alvos diferentes e produz muitos efeitos diferentes, isto é, ela é pleiotrópica. O professor faz a brincadeira que resume o problema experimental: se você quiser demonstrar que uma determinada citocina faz uma determinada ação, basta montar o experimento do jeito certo. Essa promiscuidade funcional é uma característica da molécula, não um defeito do método.

A segunda é que a citocina, sozinha, não faz nada. Uma citocina só muda o comportamento de uma célula se essa célula expressar o receptor correspondente. É essa exigência que devolve especificidade ao sistema: como a expressão de receptores varia com o tipo celular e com o estado de ativação, a mesma citocina no mesmo tecido produz efeitos diferentes conforme quem está ouvindo.

#subtopico("4.2 — Os apelidos: interleucinas, fatores de crescimento e interferons")

Sobre o nome genérico "citocina" foram-se acumulando apelidos históricos, e é útil saber de onde vieram — sabendo, desde o início, que o nome não prevê a função.

Uma citocina batizada por servir à comunicação entre leucócitos chama-se interleucina, abreviada IL seguida de um número; já há mais de trinta descritas. Outras foram descobertas no estudo da hematopoiese e receberam o nome da colônia que induzem — são os fatores estimuladores de colônia, os #sigla("CSF", [colony-stimulating factors]), com uma letra na frente indicando o tipo de colônia, como G-CSF e GM-CSF; outras trazem GF no fim, de _growth factor_. Há ainda os fatores citotóxicos, como o TNF-alfa e o TNF-beta, e os interferons.

Os interferons merecem uma distinção que cai em prova: IFN-alfa e IFN-beta são interferons do tipo I, enquanto o único interferon do tipo II é o IFN-gama. Os do tipo I são os da resposta antiviral descrita na parte anterior. E as quimiocinas, estudadas na aula anterior, são as citocinas especializadas em direcionar migração, organizadas em quatro famílias — CXC, CC, CX3C e XC — conforme o arranjo das primeiras cisteínas.

#confusao-prevista(
  titulo: "O nome da citocina não prevê a função",
  aluno_acha: [aluno acha que "fator de crescimento" induz crescimento, "interleucina" fala entre leucócitos e cada nome delimita a ação],
  mecanismo: [os nomes foram dados na ordem histórica da descoberta, muitas vezes pelo primeiro efeito observado. O GM-CSF forma colônias, mas suas ações são pleiotrópicas e vão muito além disso; há moléculas de comunicação que induzem crescimento e nunca receberam o nome de fator de crescimento. Aprender a origem do nome ajuda; deduzir a função a partir dele engana.],
)

#clinica-box("Citocina como alvo terapêutico", [Vários desses nomes já são fármacos ou alvos. A interleucina-6 tornou-se alvo de anticorpos neutralizantes em formas graves de COVID-19. G-CSF e GM-CSF são usados para recuperar linhagens hematopoéticas, inclusive em transplante. Interferons alfa e beta têm uso clínico frequente; o interferon gama, apesar de teoricamente atraente, nunca se firmou na clínica.])

#subtopico("4.3 — Além das proteínas: mediadores lipídicos e exossomos")

Nem toda comunicação intercelular é proteica. Quando a célula é ativada, uma das respostas é retirar lipídios da própria membrana e metabolizá-los em mediadores. O ácido araquidônico, esterificado no fosfolipídio de membrana, é liberado e metabolizado em duas famílias de mediadores: as prostaglandinas e os leucotrienos, aos quais se soma o #sigla("PAF", [platelet-activating factor — fator ativador de plaquetas]). São mediadores de vida curta e ação local, e é sobre essa via que atuam os anti-inflamatórios não esteroidais.

Uma família estudada mais recentemente são os exossomos. As nanovesículas envoltas por membrana que as células liberam e que circulam no sangue carregando sinais são os exossomos. À primeira vista pareciam resto celular, mas não são: têm membrana, têm conteúdo, circulam e sinalizam de fato — em algumas situações uma célula muda completamente a função de outra através dos seus exossomos. Hoje são estudados inclusive como instrumento terapêutico.

#subtopico("4.4 — Fechando: a plasticidade da resposta inata")

A aula termina com uma síntese que corrige um preconceito comum. Costuma-se dizer que a resposta adquirida, capaz de reconhecer qualquer coisa, é diversa, enquanto a inata seria monótona. Basta olhar o que a ativação dos PRR produz para ver que não é.

Ao ser ativada por PRR, uma célula pode liberar quatro classes de produto: produtos que já estavam prontos e armazenados; produtos que são modificados após a ativação, como a pró-IL-1-beta que é clivada e sai como IL-1-beta; produtos que só passam a ser produzidos depois da ativação, porque a célula não tinha nada estocado, apenas a capacidade de fabricar; e produtos de degradação celular, liberados quando a célula morre. Some-se a isso que o mesmo receptor, diante de variantes do mesmo ligante, transmite sinais um pouco diferentes — dois diacil-lipoproteínas distintos ativando o mesmo TLR6 não produzem exatamente a mesma resposta.

O resultado é uma plasticidade enorme, que torna o organismo capaz de se adaptar a inúmeras situações — e que torna o estudo do sistema um desafio, porque quase nada pode ser previsto sem ser testado.

#conclusao-box[
  A ideia que sustenta a aula inteira cabe numa frase: antes de perguntar _quem é você_, o sistema imune pergunta _está tudo bem aqui_. Quem faz essa primeira pergunta são os PRR, distribuídos por membrana, citoplasma e núcleo, lendo PAMP e DAMP. A resposta deles não é um interruptor único: pelo MyD88 sai inflamação, pelo TRIF saem interferons, e pelas ramificações saem sobrevivência, apoptose e inflamassoma — cuja caspase-1 só corta a IL-1-beta se um sinal anterior tiver fabricado o precursor. O que se segue são as quatro estratégias de reparo — proteger as vizinhas, eliminar a doente, limpar a área, chamar reforço — coordenadas por citocinas pleiotrópicas que só agem onde há receptor. E o desfecho final daquele antígeno, lá na frente, dependerá do estado homeostático que os PRR reportaram. Reconhecimento inato não é a versão simples da imunologia: é a camada que decide o sentido de tudo o que vem depois.
]
