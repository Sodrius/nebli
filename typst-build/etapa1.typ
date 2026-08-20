#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  O sistema imune passa o dia inteiro fazendo uma pergunta antes de qualquer outra: este tecido ainda está funcionando dentro da faixa normal? A resposta a essa pergunta é dada por receptores que já nascem prontos, que toda célula do mesmo tipo carrega idênticos, e que não leem moléculas individuais — leem *padrões*. É esse andar do reconhecimento que este resumo destrincha.

  A lógica é sempre a mesma e vale a pena guardá-la antes de começar: alguma coisa denuncia a perda de equilíbrio, um receptor pronto detecta essa denúncia, e a célula que detectou dispara um repertório de reações que tentam devolver o tecido ao normal. Vamos percorrer os três andares desse arco. Na PARTE I, quem detecta e como distingue o tecido em ordem do tecido em apuros. Na PARTE II, o que a célula efetivamente faz depois de detectar — quatro estratégias que se repetem em qualquer infecção, qualquer trauma, qualquer isquemia. Na PARTE III, como o sinal caminha da membrana até o núcleo e por que a mesma via molecular consegue produzir resultados tão diferentes conforme a situação.
]

#parte-title("PARTE I — Quem detecta a perda de homeostasia", primeira: true)

#subtopico("1.1 — Receptor pronto e receptor sorteado")

O sistema imune reconhece moléculas por dois caminhos que funcionam com lógicas opostas, e separar esses dois caminhos é o pré-requisito de tudo o que vem depois. Um deles produz receptores por sorteio; o outro já vem com os receptores escritos no genoma.

O caminho do sorteio é o dos linfócitos. Cada linfócito, enquanto amadurece, recombina aleatoriamente segmentos gênicos e monta *um* receptor, diferente do receptor do linfócito vizinho. Multiplicado por bilhões de células, esse sorteio gera um repertório que os imunologistas chamam de completo: existe, em algum lugar do corpo, um clone capaz de reconhecer praticamente qualquer molécula que se possa imaginar. É esse repertório que carrega o #sigla("TCR", [T cell receptor — receptor de antígeno do linfócito T]) e o #sigla("BCR", [B cell receptor — a imunoglobulina de membrana do linfócito B, que depois vira anticorpo secretado]).

O preço dessa completude é evidente: um repertório capaz de reconhecer qualquer coisa também é capaz de reconhecer o próprio organismo. Por isso a geração aleatória vem obrigatoriamente acompanhada de *seleção*. Nos órgãos linfoides primários — a medula óssea, onde nascem os linfócitos B, e o timo, onde amadurecem os T — os clones recém-montados são confrontados com antígenos do próprio corpo. Quem reage forte demais ao próprio é eliminado ou desativado ali mesmo, antes de ganhar a circulação. *A seleção não acrescenta especificidade nenhuma; ela poda o que sobrou perigoso do sorteio.*

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-03.png",
  largura: 55%,
  legenda: [O repertório clonal nasce completo *porque* nasce aleatório — e é justamente por nascer aleatório que precisa passar por seleção antes de ser liberado.])

O outro caminho é o do reconhecimento inato, e ele não sorteia nada. Os receptores da imunidade inata já vêm codificados na linhagem germinativa: o gene está no genoma desde o zigoto, é o mesmo em você e no seu vizinho, e toda célula que o expressa expressa exatamente a mesma proteína. Esses receptores são os #sigla("PRR", [pattern recognition receptors — receptores para padrões moleculares]), e o nome já entrega a diferença central. Eles não reconhecem *uma* molécula específica; reconhecem uma *classe* de molécula, um padrão estrutural que se repete.

Aqui está o ponto que faz a estratégia funcionar. Um repertório fixo de algumas dezenas de receptores jamais daria conta da variedade do mundo microbiano se cada receptor precisasse de um alvo próprio. O que a evolução fez foi mirar em moléculas que os micro-organismos *não conseguem abandonar sem morrer*: o lipopolissacarídeo da parede externa das bactérias gram-negativas, a flagelina que constrói o flagelo, o RNA de fita dupla que aparece obrigatoriamente quando um vírus de RNA se replica. Um patógeno pode mutar uma proteína de superfície para escapar de um anticorpo; não pode desmontar a própria parede celular para escapar de um PRR. *É essa impossibilidade de fuga que torna um repertório pequeno e fixo suficiente.*

#mini-resumo[Receptor clonal: sorteado, único por célula, precisa de seleção, lê uma molécula. PRR: herdado, idêntico em todas as células, não precisa de seleção, lê um padrão que o micróbio não pode descartar.]

Uma última consequência da diferença, e ela é prática. O repertório clonal precisa de dias para funcionar — o clone certo tem que ser encontrado no meio de bilhões e depois multiplicado. O PRR está pronto no minuto zero, em toda célula que o expressa. Por isso o reconhecimento inato é o que responde primeiro, e por isso ele é quem decide se vale a pena acordar o outro sistema.

#subtopico("1.2 — O que decide entre tolerar e responder")

A distinção entre próprio e não-próprio, sozinha, não explica o comportamento do sistema imune — e é aí que o raciocínio da maioria dos alunos trava. A comida que você almoçou é integralmente não-própria, chega ao intestino em quantidade enorme, é absorvida em fragmentos e mesmo assim não desencadeia resposta alguma. As bactérias que colonizam o intestino são não-próprias e convivem com o organismo a vida inteira. Ao mesmo tempo, na doença autoimune, o alvo atacado é rigorosamente próprio. Se a fronteira próprio/não-próprio fosse o gatilho, os dois fenômenos seriam impossíveis.

O que acontece de verdade é que o reconhecimento específico de um antígeno pode levar a *dois* desfechos opostos. Ou o sistema monta uma reação que tende a eliminar o que foi reconhecido — o que se chama resposta imune —, ou o sistema se adapta e aceita a presença daquele antígeno sem tentar eliminá-lo, o que se chama tolerância imunológica. E aqui vem o detalhe que costuma escapar: *os dois desfechos geram memória*. Tolerar não é esquecer. O sistema aprende a aceitar aquele antígeno com a mesma solidez com que aprenderia a atacá-lo, e vai repetir o comportamento aprendido no próximo encontro.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-05.png",
  largura: 62%,
  legenda: [O mesmo reconhecimento específico se abre em dois desfechos opostos, e os dois deixam memória. A seta dupla no meio marca o que decide para que lado a coisa vai.])

O fator que decide para que lado o encontro vai é o *estado homeostático do tecido de onde aquele antígeno veio* no momento em que foi levado ao sistema imune. #termo-nota[Homeostasia][a faixa estreita de temperatura, pH, composição iônica e distribuição molecular em que as células de um tecido operam bem; sair dessa faixa é o que os PRR detectam] é a condição de tecido em ordem. Antígeno que chega de um tecido em ordem tende à tolerância. Antígeno que chega de um tecido em apuros — com células morrendo mal, com moléculas em lugares onde não deveriam estar — tende à resposta.

#confusao-prevista(
  titulo: "O gatilho não é ser estranho; é o tecido estar fora de faixa",
  aluno_acha: [o aluno acha que o sistema imune ataca o que é não-próprio e poupa o que é próprio],
  mecanismo: [na prática, o que autoriza a resposta é a *perda de homeostasia* detectada pelos PRR no tecido de origem do antígeno. Proteína própria liberada por uma célula que morreu de forma desorganizada aparece fora do lugar, é lida como sinal de dano e autoriza a resposta; proteína de camarão absorvida por um intestino saudável chega sem nenhum sinal de dano junto e tende a ser tolerada. Próprio e não-próprio informam *o que* será reconhecido; o estado do tecido decide *o que fazer* com esse reconhecimento.],
)

Essa lógica tem duas consequências clínicas que valem a pena guardar porque são espelhadas uma da outra. No transplante, o ideal seria induzir tolerância ao órgão enxertado — mas o órgão chega ao receptor depois de horas de isquemia, com células danificadas derramando conteúdo, ou seja, no pior estado homeostático possível, empurrando o sistema exatamente para o lado da resposta. No tumor, o ideal seria o oposto: você quer que o sistema responda e elimine. Só que o tumor cresceu devagar, dentro do próprio tecido, muitas vezes sem alarme algum de perda de homeostasia — e o sistema já aprendeu, com memória e tudo, que aquilo ali não é problema.

É desse impasse que nasce boa parte da imunologia terapêutica moderna. Como a tolerância ao tumor foi *aprendida* e não é uma ausência de reconhecimento, ela pode em princípio ser desaprendida: existem linfócitos que reconhecem o tumor, só que estão freados. Retirar o freio molecular desses linfócitos — em vez de tentar ensinar um reconhecimento novo — é a estratégia que mudou o tratamento de vários cânceres nas últimas duas décadas. #mini-resumo[Se você só lembrar de uma coisa: tolerância é um aprendizado ativo, não um buraco no repertório. Por isso ela pode ser revertida.]

#subtopico("1.3 — A ponte da apresentação de antígenos")

Os dois sistemas de reconhecimento que acabamos de separar não trabalham em compartimentos isolados, e o mecanismo que os costura é o mesmo fenômeno que vai reaparecer em todos os subtópicos seguintes: a apresentação de antígenos. Vale entender bem esse mecanismo agora, porque é ele que transforma "um PRR detectou dano" em "um linfócito T foi ativado".

A peça central é a #sigla("APC", [antigen presenting cell — célula apresentadora de antígeno, tipicamente a célula dendrítica]). Instalada dentro dos tecidos, ela faz duas coisas ao mesmo tempo, e é a simultaneidade que importa. De um lado, captura indiscriminadamente moléculas do ambiente ao redor — tudo o que estiver por ali, próprio ou não. De outro lado, seus próprios PRR estão o tempo todo medindo o estado homeostático daquele tecido. A APC, portanto, não é um mensageiro que carrega uma amostra; é um mensageiro que carrega uma amostra *e* um laudo sobre o lugar de onde a amostra veio.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-07.png",
  largura: 64%,
  legenda: [A APC captura no tecido (azul), processa, e apresenta no órgão linfoide secundário (verde). O raio no canto inferior esquerdo é o estado homeostático — a informação que viaja junto com o antígeno.])

O que a APC faz com o material capturado se chama processamento: ela desmonta as proteínas em fragmentos peptídicos e encaixa esses fragmentos em moléculas de superfície que funcionam como bandeja de exibição. Processar não é destruir, é picar em pedaços exibíveis. Em seguida a célula migra do tecido para o órgão linfoide secundário mais próximo — o linfonodo que drena aquela região, ou o baço — e é *lá*, e só lá, que ela encontra os linfócitos T e apresenta o que trouxe. Vale fixar a diferença de endereço, porque ela confunde: nos órgãos linfoides primários o linfócito *nasce e é filtrado*; nos secundários ele *encontra o antígeno* trazido de fora.

O detalhe mecanístico que fecha a ponte é como o "laudo" viaja fisicamente. Quando um PRR da APC é ativado no tecido, a célula muda de estado: passa a expressar na superfície moléculas coestimulatórias que antes quase não tinha, e liga o programa de migração para o linfonodo. Uma APC que veio de um tecido em ordem chega ao linfonodo com a bandeja cheia e a coestimulação baixa, e o linfócito T que reconhece aquele peptídeo tende a ser desligado — tolerância. Uma APC que veio de um tecido com perda de homeostasia chega com a mesma bandeja mas com coestimulação alta, e o mesmo reconhecimento vira ativação. *O antígeno determina qual linfócito responde; o sinal inato determina se ele responde.*

Os antígenos podem também chegar ao órgão linfoide por conta própria, carregados pela linfa, e ser capturados diretamente pelos linfócitos B através da imunoglobulina de membrana. O linfócito B, uma vez que captura antígeno por seu próprio receptor, também processa e apresenta — ele funciona como célula apresentadora, e não apenas como fábrica de anticorpo.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-06.png",
  largura: 74%,
  legenda: [O mapa do reconhecimento hierárquico. À esquerda, os PRR lendo padrões moleculares e disparando a imunidade inata; à direita, os receptores clonais lendo antígenos e disparando a adquirida. A seta vermelha grossa é a ponte: sem ela, a coluna da direita não sai do lugar.])

#subtopico("1.4 — DAMP, PAMP e as famílias de PRR")

Pense num prédio com dois tipos de sensor. Os detectores de fumaça leem uma coisa que só existe quando há fogo — fumaça não faz parte do prédio. Já os sensores estruturais leem material *do próprio prédio* aparecendo onde não deveria: uma viga fora do prumo, entulho no corredor. Nenhum dos dois procura por um incêndio específico; ambos procuram por assinaturas genéricas de que algo saiu do lugar. O sistema imune inato usa exatamente essa dupla estratégia, e os dois tipos de assinatura têm nome.

Os #sigla("PAMP", [pathogen associated molecular patterns — padrões moleculares associados a patógenos]) são as moléculas que só existem em micro-organismos: o #sigla("LPS", [lipopolissacarídeo — componente da membrana externa das bactérias gram-negativas, também chamado endotoxina]), a flagelina, o peptidoglicano, o β-glucano da parede dos fungos, o RNA de fita dupla dos vírus. São a fumaça. Os #sigla("DAMP", [damage associated molecular patterns — padrões moleculares associados a dano]) são o outro tipo: moléculas *do próprio hospedeiro* que, em condição normal, ficam trancadas em compartimentos onde nenhum PRR as encontra, e que só aparecem fora do lugar quando uma célula é rompida ou morre de forma desorganizada. São a viga fora do prumo.

#atencao-box("DAMP é molécula própria, não molécula de micróbio danificado", [O nome engana, e a troca custa caro porque desmonta metade do capítulo. O "D" de DAMP é de *damage*, o dano ao tecido — não de "bactéria danificada". O #sigla("ATP", [adenosina trifosfato — a moeda energética da célula, normalmente confinada ao meio intracelular]) é o exemplo mais limpo: dentro da célula ele está em concentração altíssima e não significa nada de anormal; derramado no meio extracelular por uma célula que se rompeu, ele vira sinal de dano e é lido como tal. O mesmo vale para o ácido úrico cristalizado e para o #sigla("DNA", [ácido desoxirribonucleico]) mitocondrial — que, por herança evolutiva bacteriana, tem justamente as marcas químicas que os PRR de ácido nucleico procuram. *O que define o DAMP não é a origem da molécula, é o endereço errado dela.* Corolário: dano estéril, sem micróbio nenhum — trauma, infarto, isquemia — ativa a imunidade inata do mesmo jeito.])

Vale um parêntese histórico, porque ele ajuda a entender a lógica. Quem primeiro sustentou que o gatilho da resposta era o *perigo* e não a estranheza foi Polly Matzinger, que propunha chamar essas moléculas de padrões associados ao perigo. A nomenclatura que pegou foi outra, mas o conteúdo do modelo é o que a imunologia usa até hoje: o sistema não pergunta "isto é meu?", pergunta "está tudo bem por aqui?".

Do lado do receptor, os PRR não formam uma família única. São várias famílias, e o eixo que organiza todas elas é a *localização celular* — que, por sua vez, é determinada pelo lugar onde o padrão que cada família procura costuma aparecer. Padrão de superfície bacteriana aparece do lado de fora, então o receptor fica na membrana plasmática. Ácido nucleico viral aparece no citoplasma da célula infectada, então o receptor fica solto no citosol.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-08.png",
  largura: 80%,
  legenda: [As famílias de PRR organizadas pela localização. Repare que a coluna do meio é o eixo real da tabela: onde o receptor mora prediz que tipo de padrão ele consegue encontrar. Ambos os tipos de padrão — DAMP e PAMP — convergem para a mesma resposta.])

A tabela do professor lista seis famílias, e é útil ler cada linha pelo par localização-alvo. Os #sigla("CLR", [C-type lectin receptors — receptores de lectina do tipo C, dependentes de cálcio]), na membrana, leem açúcares de parede de fungo — a dectina-1 e o β-glucano são o par clássico. Os *scavenger receptors*, também de membrana, reconhecem padrões de lipídio modificado e partículas a serem removidas. Os #sigla("TLR", [toll-like receptors — a família de PRR mais estudada, com membros na membrana plasmática e em membranas de vesícula]) ocupam membranas, tanto a externa quanto as internas, e são o assunto de toda a PARTE III. Os #sigla("NLR", [NOD-like receptors — família citoplasmática de PRR, incluindo os NOD e os NLRP]) e os #sigla("RLR", [RIG-I-like receptors — sensores citoplasmáticos de RNA viral]) trabalham no citoplasma, e os AIM2-like chegam a atuar dentro do núcleo. A distribuição não é acidental: cobrir membrana externa, membranas internas, citosol e núcleo é o jeito de não deixar nenhum compartimento sem vigilância, já que um patógeno intracelular passaria despercebido por qualquer sensor que só olhasse para fora.

#sintese-box("1", [Padrão molecular de micróbio (PAMP) ou molécula própria fora do lugar (DAMP) é detectado por um PRR codificado no genoma. Onde o PRR mora determina que padrão ele consegue alcançar — e a cobertura de todos os compartimentos é o que impede o patógeno intracelular de passar em branco. Detectada a perda de homeostasia, começa a resposta que a PARTE II descreve.])

#parte-title("PARTE II — O que a célula faz depois de detectar")

Detectar a perda de homeostasia só tem valor se algo acontecer em seguida. O que acontece em seguida é sempre uma tentativa de restaurar o equilíbrio, e essa tentativa se organiza em quatro estratégias que aparecem, com pesos diferentes, em qualquer situação de dano. A célula tenta salvar as vizinhas ainda sadias; tenta eliminar as que já estão comprometidas; tenta limpar os restos e os invasores; e, atravessando as três anteriores, chama reforço produzindo mediadores que modulam o ambiente inteiro.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-09.png",
  largura: 70%,
  legenda: [As quatro estratégias da resposta inata. As três primeiras são ações locais sobre células; a quarta é comunicação, e é ela que permite às outras três acontecerem de forma coordenada.])

#subtopico("2.1 — Salvar o vizinho: interferons do tipo I")

Retomando o que a PARTE I estabeleceu: os PRR de ácido nucleico moram no citoplasma e em vesículas justamente porque é ali que o material genético de um vírus aparece. Quando esses receptores disparam, a primeira coisa que a célula infectada faz não é tentar se salvar. Ela avisa a vizinhança.

O mecanismo vale a pena ser seguido do começo. O vírus adere à célula-alvo e, em seguida, penetra e libera seu ácido nucleico no citoplasma. Essas duas etapas, aliás, são exatamente os dois pontos onde um anticorpo neutralizante consegue agir: bloqueando a adesão, ou deixando aderir mas impedindo a liberação do material genético. Se o vírus vence essas barreiras e o ácido nucleico chega ao citoplasma, os PRR citoplasmáticos o detectam e a célula liga imediatamente a produção de #sigla("IFN", [interferon — família de citocinas; os do tipo I, alfa e beta, são os antivirais produzidos por qualquer célula infectada]) do tipo I. O interferon é secretado, difunde pelo interstício e alcança as células ao redor, que ainda estão sadias.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-10.png",
  largura: 62%,
  legenda: [A célula infectada (esquerda) libera IFN antes de sucumbir. As vizinhas alcançadas pelo interferon entram em estado antiviral — e por isso as células da direita continuam íntegras mesmo com o vírus circulando.])

O que o interferon faz nessas vizinhas é o núcleo do conceito. Ele não mata vírus; ele induz nelas a expressão de um conjunto de genes que instala um *estado antiviral* — enzimas que degradam RNA viral, proteínas que bloqueiam a tradução, fatores que travam a montagem de novas partículas. Quando o vírus finalmente chega a essas células, encontra um citoplasma que não permite mais a replicação. A célula que produziu o interferon, por sua vez, está perdida: ela será destruída pelo vírus que já a habita. #mini-resumo[O que ficou de pé: o interferon é um gesto de vizinhança, não de autossalvamento. A célula que avisa morre; quem sobrevive são as que ouviram o aviso.]

O aprofundamento que vale acrescentar aqui é a lógica temporal disso. A resposta adquirida contra um vírus novo leva vários dias para ficar pronta — tempo suficiente para uma infecção respiratória se disseminar por todo o epitélio. O interferon age em horas e não depende de reconhecimento prévio nenhum. Sem essa contenção inicial, a resposta adquirida chegaria a um tecido já arrasado. É por isso que uma falha genética na via do interferon do tipo I, mesmo com imunidade adquirida intacta, se manifesta como suscetibilidade grave a infecções virais — o sistema perde não a arma final, mas o tempo de que precisava para prepará-la.

Há ainda um efeito que todo mundo já sentiu sem saber a causa. Como qualquer mediador produzido no sítio da reação, o interferon não fica só ali: ele cai na circulação e produz efeitos sistêmicos, entre eles febre e dor no corpo. #clinica-box("Os sintomas da gripe são do interferon, não do vírus", [Costuma-se atribuir o mal-estar da gripe à destruição de células pelo vírus, mas a maior parte dele é consequência dos próprios mediadores da resposta inata, o interferon do tipo I à frente. Ele age no hipotálamo elevando o ponto de ajuste da temperatura, e age no músculo e nas terminações nervosas produzindo a mialgia difusa característica. Isso explica um fenômeno clínico corriqueiro: pacientes tratados com interferon recombinante para hepatite viral crônica desenvolvem, de forma reprodutível, febre, calafrios e dores musculares nas primeiras horas após cada aplicação — a "síndrome gripal" da droga, sem vírus nenhum envolvido. O mesmo raciocínio explica por que a intensidade dos sintomas não mede diretamente a carga viral: ela mede a intensidade da resposta.])

#subtopico("2.2 — Eliminar a célula doente: citotoxicidade")

Quando uma célula já está comprometida — infectada por um vírus que se replica dentro dela, ou transformada — salvar as vizinhas não basta, e o sistema parte para a segunda estratégia. Aqui mora uma imagem errada muito difundida: a de que a célula efetora fura, perfura ou dissolve a célula-alvo, como um tiro dado de fora. Não é o que acontece, e entender o mecanismo real muda a compreensão de todo o resto.

#termo-nota[Citotoxicidade celular][mecanismo pelo qual uma célula efetora induz a célula-alvo a ativar seu próprio programa de morte, em vez de destruí-la de fora] é, literalmente, um convencimento. A célula efetora entrega à célula-alvo um sinal, e é a *célula-alvo* que executa a própria morte, por apoptose. Apoptose é morte programada: a célula desmonta o conteúdo de forma ordenada, empacota tudo em vesículas de membrana intacta e não derrama nada no interstício — o que evita gerar uma nova onda de DAMP no meio de um tecido já inflamado.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-11.png",
  largura: 74%,
  legenda: [Os três tempos da citotoxicidade. Repare no terceiro: a célula efetora sai íntegra do encontro e vai procurar o próximo alvo, enquanto a célula-alvo entra em apoptose.])

O processo tem três tempos. Primeiro, o reconhecimento: as células efetoras identificam a célula-alvo, e podem fazê-lo por dois caminhos distintos — por receptores clonais, quando a efetora é um linfócito T citotóxico da imunidade adquirida, ou por receptores inatos, quando a efetora não precisou de adaptação nenhuma para reconhecer. Esse segundo caminho é o que interessa aqui, e é a razão de a citotoxicidade aparecer nesta aula: há células que matam alvos usando PRR, sem nunca terem passado por seleção clonal.

Segundo, a sinalização. As duas células se encostam e o encontro dispara a morte por um de dois mecanismos, que costumam ser confundidos entre si. Um deles é a interação entre moléculas de membrana que já estavam presentes nas duas superfícies o tempo todo e só precisavam ser aproximadas — o par FasL na efetora e Fas na célula-alvo é o exemplo canônico, e o que o reconhecimento específico faz é justamente promover essa aproximação. O outro é a #termo-nota[desgranulação][liberação, no espaço estreito entre as duas células, de grânulos pré-formados contendo proteínas que penetram na célula-alvo e ativam suas caspases]: a efetora despeja no ponto de contato grânulos cujo conteúdo, agindo sobre a célula-alvo, liga o programa apoptótico por dentro.

Terceiro, o desfecho, que tem uma elegância própria. A célula-alvo sofre apoptose e é removida. A célula citotóxica, que não gastou a própria integridade no processo, permanece viável e parte em busca de outros alvos — uma efetora atende muitos alvos em sequência. #mini-resumo[Em uma frase: quem executa a morte é a célula-alvo; a efetora só entrega a ordem e segue adiante.]

#subtopico("2.3 — Limpar a área: a fagocitose em etapas")

A terceira estratégia é a mais antiga de todas, e essa antiguidade não é detalhe decorativo. Engolir partículas é o que um protozoário faz para se alimentar; o sistema imune não inventou a fagocitose, ele incorporou um processo ancestral de nutrição e o reaproveitou como mecanismo de defesa. Toda a maquinaria já existia — o que a evolução acrescentou foram os receptores que dizem *o que* engolir e as moléculas que ajudam a segurar o alvo.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-12.png",
  largura: 68%,
  legenda: [As etapas da fagocitose. Cada linha é um problema mecânico distinto: achar o alvo, grudar nele, envolvê-lo, e só então digeri-lo.])

O primeiro problema é achar o alvo, e a solução é a #termo-nota[quimiotaxia][migração celular dirigida por um gradiente de concentração de moléculas solúveis, em direção à maior concentração]. O fagócito tem receptores para moléculas quimiotáticas e caminha na direção em que a concentração delas aumenta. Essas moléculas vêm de várias fontes: a própria bactéria libera produtos que funcionam como sinal, as células do tecido lesado liberam mediadores, e existe ainda um sistema inteiro de proteínas plasmáticas dedicado a isso.

Esse sistema merece atenção, porque ele é um PRR que a maioria não reconhece como tal. As proteínas do complemento circulam dissolvidas no plasma e, ao encontrarem superfícies com certos padrões moleculares, ativam-se em cascata. Ou seja, o complemento é um *sistema de reconhecimento de padrão solúvel*: faz o mesmo trabalho de leitura que um PRR de membrana, só que sem estar preso a nenhuma célula. Alguns fragmentos gerados na cascata são potentes agentes quimiotáticos; outros grudam na superfície do alvo, e é para esses que vamos agora.

O segundo problema é a adesão, e ele é menos óbvio do que parece. Encostar não basta: a superfície de uma bactéria pode não interagir bem com a membrana do fagócito, e o encontro se desfaz. A solução tem duas camadas. Os fagócitos carregam PRR de membrana que reconhecem diretamente padrões comuns em alvos fagocitáveis. E o organismo produz, além disso, moléculas que grudam na partícula e para as quais o fagócito tem receptor próprio — o processo se chama #termo-nota[opsonização][revestimento da partícula-alvo por moléculas solúveis, como fragmentos do complemento e anticorpos, que funcionam como alças para os receptores do fagócito]. A direção importa e é a fonte do erro mais comum: *a opsonina reveste o alvo, não o fagócito*.

Resolvida a adesão, vem o englobamento, e o professor usa uma imagem exata para descrevê-lo: um zíper. A membrana do fagócito não engole a partícula de uma vez; ela avança progressivamente, e cada receptor que encontra sua alça na superfície do alvo puxa a membrana um pouco mais adiante, o que aproxima o receptor seguinte, que se liga, e assim por diante até a membrana se fechar do outro lado. Fechada, a partícula fica contida numa vesícula intracelular — o fagossomo.

O fagossomo recém-formado, porém, ainda não digere nada. O que o torna digestivo é a fusão com lisossomos, que despejam ali dentro um arsenal de enzimas hidrolíticas. Em paralelo, montado na própria membrana do fagossomo, um complexo enzimático começa a produzir radicais livres de oxigênio. É esse complexo que consome oxigênio em quantidade desproporcional e dá nome ao fenômeno: a #termo-nota[explosão respiratória][aumento abrupto do consumo de oxigênio pelo fagócito ativado, usado para gerar espécies reativas microbicidas — e não para produzir energia]. O nome engana quem pensa em respiração celular. Nada disso serve para fabricar energia; todo o oxigênio consumido vira espécie reativa destinada a destruir o conteúdo do fagossomo. Enzimas de um lado, radicais livres do outro, e a partícula é desmontada.

#clinica-box("Doença granulomatosa crônica: quando a explosão respiratória falha", [O complexo que gera os radicais na membrana do fagossomo é a NADPH-oxidase. Quando uma mutação inativa uma de suas subunidades, o fagócito continua migrando normalmente, continua aderindo, continua englobando e continua formando o fagossomo — tudo funciona, menos a produção de #sigla("ROS", [reactive oxygen species — espécies reativas de oxigênio, os radicais gerados na explosão respiratória]). O resultado é um paciente que fagocita bactérias e fungos mas não consegue matá-los dentro do próprio fagossomo. As bactérias sobrevivem no interior do fagócito, que não consegue nem digerir nem liberar; o tecido responde cercando esses fagócitos com mais fagócitos, e forma-se o granuloma que dá nome à doença. É a demonstração clínica de que cada etapa da fagocitose é um mecanismo independente: perder só a última compromete todo o resultado.])

#subtopico("2.4 — Chamar socorro: citocinas e febre")

A quarta estratégia atravessa as três anteriores em vez de sucedê-las. Nenhuma das ações descritas acima acontece de forma coordenada sem informação circulando entre as células, e o organismo mantém para isso uma coleção grande de mediadores de comunicação intercelular.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-13.png",
  largura: 58%,
  legenda: [As três grandes classes de mediador. As citocinas dominam o quadro, mas os mediadores lipídicos e os exossomos carregam informação por mecanismos completamente distintos.])

Os mais versáteis são as citocinas. São proteínas — em geral glicoproteínas — produzidas por células para modificar o comportamento de outras células. A propriedade que as define é serem #termo-nota[pleiotrópicas][capazes de produzir efeitos diferentes, às vezes opostos, conforme o tipo celular alvo e o contexto em que agem]. A mesma citocina pode induzir proliferação num tipo celular, migração noutro e morte num terceiro. O professor faz uma brincadeira que vale como advertência metodológica: se você quiser demonstrar que uma citocina qualquer faz uma ação qualquer, basta montar o experimento do jeito certo.

Essa versatilidade só é administrável por causa de um segundo componente: *ter a citocina não adianta nada sem o receptor para ela*. Quem decide se uma célula vai responder é a própria célula, expressando ou não o receptor correspondente. É aí que mora a seletividade de um sistema que, à primeira vista, parece caótico — a mensagem é lançada no meio, mas só quem tem a antena escuta.

A nomenclatura, por sua vez, é genuinamente confusa, e organizar a hierarquia antes de decorar rótulos poupa muito esforço. *Citocina* é o termo guarda-chuva: qualquer produto proteico de comunicação intercelular. Debaixo dele vivem quatro rótulos históricos, cada um herdado do contexto em que aquelas moléculas foram descobertas. As *interleucinas*, abreviadas #sigla("IL", [interleucina — o rótulo, seguido de um número de ordem, marca as citocinas descritas como mensageiras entre leucócitos]) seguido de um número, ganharam esse nome por servirem à comunicação entre leucócitos; já passam de trinta descritas. Os *fatores de crescimento* trazem GF no fim do nome, ou #sigla("CSF", [colony stimulating factor — fator estimulador de colônia, nome herdado dos estudos de hematopoiese]) quando foram descobertos no estudo da hematopoiese, com uma letra à frente indicando o tipo de colônia formada. Os *interferons* já apareceram em 2.1. E as *quimiocinas* são as citocinas especializadas em gerar gradientes de migração — são elas que fazem a quimiotaxia de 2.3 funcionar.

O alerta importante é que esses rótulos são históricos, não funcionais. O GM-CSF foi batizado por formar colônias de granulócitos e macrófagos, mas suas ações vão muito além disso; e há moléculas de comunicação que induzem crescimento sem carregar "fator de crescimento" no nome. #mini-resumo[Se você só lembrar de uma coisa: o nome de uma citocina conta onde ela foi descoberta, não o que ela faz.]

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-14.png",
  largura: 55%,
  legenda: [Alguns exemplos de cada categoria. Não é lista para decorar — é para reconhecer o padrão de nomenclatura e saber de que família vem cada sigla ao encontrá-la.])

Nem toda comunicação, porém, é proteica. Quando uma célula é ativada, uma das respostas é atacar os próprios lipídios de membrana: o ácido araquidônico, que fica esterificado nos fosfolipídios, é liberado e metabolizado, gerando prostaglandinas, leucotrienos e o fator ativador de plaquetas. São mediadores lipídicos, produzidos em segundos porque o substrato já estava na membrana — não dependem de transcrição nenhuma. E há ainda os exossomos: nanovesículas com membrana e conteúdo próprios, liberadas pelas células e encontradas circulando no sangue. Foram tratados durante muito tempo como detritos, e hoje se sabe que uma célula é capaz de alterar profundamente a função de outra pelo que envia dentro deles.

Vale um comentário terapêutico, porque ele mostra por que essa lista importa. Como cada citocina age por um receptor definido, bloquear o par citocina-receptor virou estratégia de tratamento: anticorpos que neutralizam a interleucina-6 foram estudados em formas graves de COVID-19 justamente por conta do papel dela na inflamação sistêmica; os fatores estimuladores de colônia são usados para recuperar contagens de células do sangue; e os interferons alfa e beta têm uso clínico consolidado, enquanto o interferon gama, apesar de promissor no papel, nunca se firmou.

Falta a manifestação sistêmica mais visível de tudo isso. Os produtos da resposta inata alcançam a circulação e alteram o organismo inteiro — e a febre é a alteração mais óbvia. Trata-se de resposta efetora, não de efeito colateral: os mediadores inflamatórios elevam o ponto de ajuste térmico do hipotálamo, e o corpo passa a trabalhar para manter uma temperatura mais alta. A evidência experimental mais elegante vem de um animal que não regula a própria temperatura. O lagarto controla a temperatura corporal expondo-se mais ou menos ao sol; se você o infecta e o impede de buscar calor — isto é, impede que ele desenvolva febre — ele morre muito mais facilmente. *A febre faz parte da defesa, e não do dano.*

#sintese-box("2", [Quatro estratégias, uma finalidade: devolver o tecido à faixa normal. Interferon protege o vizinho ainda sadio; a citotoxicidade convence a célula comprometida a morrer de forma limpa; a fagocitose remove o que sobrou; e as citocinas costuram as três, mudando quem chega ao local e o que essas células fazem quando chegam — com a febre como a assinatura sistêmica do conjunto.])

#parte-title("PARTE III — Como o sinal entra na célula")

#subtopico("3.1 — Os toll-like receptors e onde eles moram")

A PARTE I deixou os PRR organizados por família e localização; agora vamos abrir uma dessas famílias e ver como o reconhecimento vira sinal. A escolhida é a dos toll-like receptors, e ela é a escolha natural por ser a mais estudada e a que melhor demonstra o princípio geral.

O nome vem de um lugar inesperado. *Toll* é palavra alemã coloquial para "bacana", "genial", e batizou um gene descoberto na mosca *Drosophila* cuja função original nada tem a ver com defesa: a molécula Toll participa da embriogênese, orientando a formação do eixo dorsoventral. Quando se descobriu, nos mamíferos, uma família de proteínas estruturalmente parecidas com aquela, o nome pegou como "semelhantes a Toll" — e só depois se percebeu que a própria Toll da mosca também cumpre papel de reconhecimento de padrões na imunidade dos insetos. A história explica por que a nomenclatura da imunologia parece arbitrária: os nomes vêm do contexto da descoberta, não da função.

Os TLR são proteínas de membrana, e a membrana em que cada um se instala é o dado mais informativo sobre ele. Alguns ficam na membrana plasmática, voltados para o meio extracelular. Outros ficam na membrana de vesículas internas — endossomos e lisossomos —, voltados para o lúmen dessas vesículas. Essa divisão não é aleatória, e a lógica por trás dela é o que vale a pena entender.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-16.png",
  largura: 80%,
  legenda: [Os ligantes típicos dos TLR conhecidos. Leia pela segunda coluna: todos os receptores de ácido nucleico (TLR3, 7, 9) estão no endolisossomo; todos os de superfície microbiana estão na membrana plasmática.])

Repare no padrão. TLR1, TLR2, TLR4, TLR5, TLR6 e TLR11 ficam na membrana plasmática, e todos leem componentes de *superfície* de micro-organismos: lipoproteínas triacil e diacil, LPS, flagelina, molécula semelhante à profilina de protozoário. TLR3, TLR7, TLR8 e TLR9 ficam no endolisossomo, e todos leem *ácidos nucleicos*: RNA de fita dupla, RNA de fita simples, DNA rico em dinucleotídeos CpG não metilados. A razão dessa segregação é elegante e vale guardar: ácido nucleico do próprio hospedeiro circula abundantemente no meio extracelular sempre que alguma célula morre. Se houvesse um sensor de DNA na membrana plasmática, ele dispararia o tempo todo. Colocando esses sensores dentro de vesículas — onde só chega o que a célula engoliu e digeriu parcialmente —, o sistema garante que o ácido nucleico detectado veio de um micro-organismo internalizado, e não do vizinho que morreu. *A localização é o mecanismo de discriminação.*

A tabela pede também uma leitura cautelosa, e o professor insiste nisso. Cada linha traz o ligante *típico* daquele receptor, não a lista fechada do que ele consegue reconhecer. Seria absurdo supor que existem apenas onze padrões moleculares no mundo. O TLR4 é o exemplo que o professor usa: é o receptor canônico do LPS, mas reconhece também proteínas virais e ligantes próprios — e aí fica claro que há padrões moleculares que ainda não conseguimos discernir com precisão, já que a mesma proteína lê coisas tão diferentes. Note ainda, na última coluna da figura, quantas linhas trazem *self* como origem do ligante: os TLR não são sensores exclusivos de micróbio.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-17.png",
  largura: 76%,
  legenda: [As outras famílias seguem a mesma lógica. RLR e NLR no citoplasma, lendo o que já entrou; CLR na membrana plasmática, lendo parede de fungo do lado de fora.])

E os TLR não estão sozinhos. Os RLR, no citoplasma, reconhecem RNA viral com assinaturas químicas que o RNA celular não tem — RIG-I lê fita dupla curta com trifosfato na ponta 5′, MDA5 lê fita dupla longa. Os NLR, também citoplasmáticos, reconhecem fragmentos de peptidoglicano bacteriano que só aparecem no citosol se houve bactéria intracelular. Os CLR, na membrana, leem açúcares de parede fúngica. Somadas, as famílias cobrem os quatro compartimentos e as principais classes químicas — açúcar, lipídio, proteína e ácido nucleico.

#subtopico("3.2 — Do ligante ao núcleo: MyD88 e TRIF")

Reconhecer não é sinalizar, e é aqui que o raciocínio precisa de mais um degrau. Um receptor ocupado por seu ligante ainda não fez nada; ele precisa transformar essa ocupação numa mudança física capaz de ser lida do lado de dentro da membrana. Os TLR resolvem isso de duas maneiras alternativas.

Na primeira, o receptor estava isolado na membrana e o ligante força a *dimerização*: duas moléculas de TLR são aproximadas pelo mesmo ligante, e as duas caudas intracelulares, agora vizinhas, formam uma plataforma que consegue recrutar proteínas. Na segunda, o dímero já estava formado antes do ligante chegar, e o que o ligante faz é mudar a conformação desse dímero — reposicionando as caudas de um jeito que só então permite o recrutamento. Em ambos os casos, o que muda do lado de dentro é a geometria; e é a geometria que cria o sítio de acoplamento.

Recrutada a primeira proteína adaptadora, o sinal segue por uma cadeia comprida até o núcleo. O principal transdutor dessa cadeia é o MyD88 — sigla de *myeloid differentiation primary response protein 88*, um nome que ninguém guarda inteiro e nem precisa. O que precisa ser guardado é a rota que ele abre. O MyD88 não toca em fator de transcrição nenhum diretamente: ele recruta as quinases IRAK, que ativam o TRAF6, que dispara uma cascata de fosforilações até liberar dois fatores de transcrição — o #sigla("NF-κB", [nuclear factor kappa B — fator de transcrição central no controle de genes inflamatórios]) e a proteína ativadora 1, ou #sigla("AP-1", [activator protein 1 — fator de transcrição que atua junto ao NF-κB nos promotores de genes inflamatórios]). Esses dois entram no núcleo, sentam nos promotores dos genes de citocinas e quimiocinas inflamatórias e autorizam a transcrição. O produto final é inflamação: chamada de fagócitos para o local e as demais tentativas de restaurar a homeostasia descritas na PARTE II.

Essa não é, porém, a única rota. Os TLR podem sinalizar também pelo #sigla("TRIF", [TIR domain-containing adaptor protein inducing interferon beta — o adaptador alternativo ao MyD88, que conduz à produção de interferon]) —, e o desfecho dessa segunda rota é outro. O TRIF conduz à ativação dos #sigla("IRF", [interferon regulatory factors — fatores de transcrição que ligam os genes dos interferons do tipo I]), e daí à produção de interferon do tipo I. Fecha-se um circuito com a PARTE II: o interferon que protege as células vizinhas de um vírus e participa da ativação de linfócitos T é produzido por esta via.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-18.png",
  largura: 78%,
  legenda: [O esquema limpo da via. Repare no cruzamento das setas logo depois do TLR: MyD88 e TRIF não são trilhos paralelos, e é dessa mistura que vem a variedade de desfechos à direita.])

#confusao-prevista(
  titulo: "MyD88 e TRIF não levam ao mesmo lugar",
  aluno_acha: [o aluno decora "TLR ativa MyD88 e TRIF" como se fossem dois nomes para a mesma coisa],
  mecanismo: [são dois adaptadores com dois destinos distintos. *MyD88 → NF-κB e AP-1 → citocinas inflamatórias → inflamação.* *TRIF → IRF → interferon do tipo I → estado antiviral e ativação de linfócito T.* Alguns TLR usam só um dos dois; outros usam os dois. A troca dos destinos é o erro mais fácil de cometer e o mais custoso, porque inverte a leitura de qualquer experimento em que um dos adaptadores é eliminado.],
)

O NF-κB merece um parágrafo próprio, porque ele vai reaparecer em imunologia, microbiologia e farmacologia o curso inteiro. Ele é o principal controlador transcricional da atividade das células do sistema imune, e a melhor medida de sua importância vem de quem tenta subvertê-lo: o vírus da imunodeficiência humana se liga e modifica a função do NF-κB. Um patógeno que evoluiu mirando exatamente esse fator está dizendo, de forma indireta, o quanto ele é central. É também por isso que o MyD88 e as moléculas dessa via viraram alvo de manipulação experimental — camundongos com MyD88 nocauteado são modelo padrão para perguntar o que acontece com a resposta quando essa sinalização some.

#subtopico("3.3 — Por que a mesma via dá saídas diferentes")

A ativação de um TLR não produz um resultado, produz um leque deles. Além das citocinas inflamatórias e do interferon já descritos, a mesma ativação envia à célula sinal de *sobrevivência*, pela via da #sigla("AKT", [proteína-quinase B — nó de sinalização que, quando ativado, bloqueia programas de morte e favorece a sobrevivência celular]), e sinal de *morte*, pela ativação da caspase-8. E pode ainda, pelo TRIF, montar o complexo molecular do próximo subtópico, o inflamassoma. Uma célula com TLR ativado tem, portanto, à sua disposição: produzir inflamação, produzir interferon, sobreviver melhor, morrer por apoptose ou montar plataforma de maturação de citocina.

Não acontecem todos ao mesmo tempo. A cada situação, algumas saídas pesam mais e outras quase não aparecem — e o que determina isso são três coisas: quais TLR aquela célula expressa, em que quantidade, e que outros sinais ela está recebendo em paralelo. É esse jogo que dá à resposta inata uma plasticidade que a fama de "resposta monótona" esconde completamente.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-19.png",
  largura: 58%,
  legenda: [Não é figura para ler molécula por molécula. O que ela demonstra é o cruzamento: entrando por qualquer TLR da borda, as setas convergem e se misturam no meio antes de alcançar o núcleo.])

O quadro completo da via, retirado da literatura, mostra por que a previsão é difícil. Há dezenas de moléculas envolvidas e, mais importante, há cruzamento entre os ramos. A via que "deveria" produzir citocina por MyD88 tem ramificações que podem levar à produção de interferon; a que deveria produzir interferon toca em componentes da outra. Olhando o esquema de longe, todos os TLR parecem terminar no mesmo lugar — e a pergunta que se impõe é como receptores tão diferentes, lendo ligantes tão diferentes, produzem efeitos específicos se o caminho é comum.

A resposta é um conceito que costuma passar despercebido, e vale a pena guardá-lo porque ele vale muito além desta aula. Estamos habituados a imaginar o citoplasma como um saco onde tudo está misturado e as moléculas se encontram por difusão livre. Não é assim. Da mesma forma que a anatomia macroscópica importa para a função dos órgãos — um músculo precisa estar inserido no lugar certo para dobrar aquela articulação —, existe uma anatomia dentro da célula. Não adianta ativar o MyD88 se ele não estiver *fisicamente próximo* das quinases IRAK que ele precisa ativar. Essas moléculas não flutuam ao acaso: são ativamente levadas para regiões específicas, e a composição de cada região depende do estado de ativação prévio da célula.

#mini-resumo[Dito de outro modo: a especificidade não está só em qual via foi ligada, está em onde as peças daquela via estavam no momento em que foram ligadas. Duas células com o mesmo TLR e o mesmo ligante podem responder diferente porque organizaram o citoplasma de forma diferente.]

Isso explica também um fato experimental que confunde: dois ligantes da mesma classe química, atuando sobre o mesmo receptor, podem induzir respostas distintas. Duas lipoproteínas diacil diferentes ativam ambas o TLR6, mas a mudança conformacional que cada uma provoca não é idêntica, e o conjunto de proteínas recrutado varia um pouco. Nada disso é previsível a partir do esquema; tem que ser testado caso a caso. É por essa complexidade que a resposta inata, longe de ser um repertório fixo e monótono, é altamente plástica — e é dessa plasticidade que vêm as oportunidades de intervenção farmacológica cada vez mais precisas.

#subtopico("3.4 — O inflamassoma e a maturação da IL-1β")

Faltou fechar uma das saídas listadas no subtópico anterior, e ela merece tratamento próprio porque introduz um mecanismo de controle que a via clássica não tem. #termo-nota[Inflamassoma][plataforma molecular que se monta no citoplasma a partir da ativação de certos PRR e cuja única função é ativar a caspase-1, que corta pró-citocinas inflamatórias em suas formas ativas] é o nome dessa saída.

A palavra "plataforma" é literal. Trata-se de um aglomerado que se forma por adesão sucessiva: uma molécula recruta outra, que recruta outra, até se constituir um complexo grande e funcional no citosol. Quem inicia a montagem são PRR específicos, e a função da plataforma pronta é uma só — a *maturação* de citocinas pró-inflamatórias.

Vale destrinchar o que significa maturação aqui, porque é o ponto que mais gera erro. Quando um fator de transcrição como o NF-κB liga o gene da interleucina-1 beta, o produto traduzido *não é funcional*: é uma pró-citocina, uma cadeia mais longa que precisa ser cortada num ponto específico para virar a molécula ativa. O inflamassoma não liga gene nenhum. Ele ativa uma protease — a caspase-1 — e é a caspase-1 que corta a pró-interleucina-1 beta e a pró-interleucina-18 já sintetizadas, liberando as formas maduras.

#atencao-box("O inflamassoma corta; quem transcreve é o NF-κB", [Aqui está a inversão que desmonta o subtópico inteiro se ficar errada. A montagem do inflamassoma *não* produz interleucina-1 beta — ela processa a pró-forma que já estava lá. Isso significa que são necessários *dois* sinais independentes para que a citocina madura apareça. O primeiro é o sinal de transcrição, tipicamente por TLR e NF-κB, que enche a célula de pró-interleucina-1 beta; sem ele, montar a plataforma corta o quê? O segundo é o sinal que dispara a montagem propriamente dita — ATP extracelular, cristais, ruptura de lisossomo, espécies reativas. Uma célula que recebeu só o segundo sinal, como o professor observa, provavelmente não vai adiante. *Transcrição e clivagem são etapas separadas, com gatilhos separados.* Essa exigência dupla é a trava de segurança de uma citocina poderosa demais para ser liberada por engano.])

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-20.png",
  largura: 74%,
  legenda: [Dentro da família NLR, dois destinos distintos: os NOD ativam NF-κB e produzem citocina; NLRP, IPAF e AIM2 montam plataforma e ativam caspase-1. Confundir os dois ramos é confundir transcrever com clivar.])

Os PRR que ativam o inflamassoma vêm essencialmente da família dos NLR, e a família se reparte em dois comportamentos que é preciso separar. Os NOD — NOD1 e NOD2 — estão soltos no citoplasma, reconhecem fragmentos de produtos bacterianos que chegaram ao citosol e ativam a via do NF-κB, produzindo citocinas inflamatórias pela rota transcricional comum. Já os NLRP, o #sigla("IPAF", [ICE-protease activating factor — sensor citoplasmático de flagelina que monta inflamassoma]) e o #sigla("AIM2", [absent in melanoma 2 — sensor citoplasmático de DNA de fita dupla que monta inflamassoma]) são os que, quando ativados, montam o complexo. São eles os inflamassomas propriamente ditos.

#figura-nebli("/figuras/imuno-02-reconhecimento-inato/slide-21.png",
  largura: 70%,
  legenda: [O inflamassoma NLRP3 em detalhe. À esquerda, a estrutura do complexo montado; à direita, a sequência lida de cima para baixo — sinal de perigo, montagem, ativação da caspase, clivagem, liberação.])

A estrutura do complexo é razoavelmente bem conhecida hoje: sabe-se quais domínios proteicos precisam estar presentes para que a montagem aconteça, e como o complexo formado recruta e ativa a caspase-1. Vale seguir a sequência inteira uma vez, do estímulo ao produto: um sinal de perigo — ATP extracelular, cristais de ácido úrico, ruptura lisossomal, espécies reativas — é detectado pelo NLRP3; o NLRP3 recruta a proteína adaptadora #sigla("ASC", [apoptosis-associated speck-like protein containing a CARD — o adaptador que costura o sensor NLRP3 à pró-caspase-1]); a ASC recruta a pró-caspase-1, que ao se aglomerar se auto-ativa; a caspase-1 ativa cliva a pró-interleucina-1 beta acumulada; e a interleucina-1 beta madura é liberada da célula. Cada seta é uma etapa fisicamente distinta, e a figura ao lado mostra exatamente essa cadeia.

#clinica-box("Quando o inflamassoma dispara sozinho", [O reconhecimento do inflamassoma abriu um capítulo inteiro da medicina. Existem doenças inflamatórias hereditárias raras em que uma mutação de ganho de função no NLRP3 faz a plataforma se montar sem estímulo adequado: o paciente tem episódios recorrentes de febre alta, erupção cutânea e inflamação articular *sem infecção nenhuma* — inflamação estéril, movida por interleucina-1 beta liberada indevidamente. A confirmação do mecanismo veio da terapêutica: bloquear a ação da interleucina-1 beta controla esses pacientes de forma quase imediata, o que só faz sentido se a citocina for mesmo o motor da doença. O mesmo eixo aparece em condições muito mais comuns — na gota, os cristais de urato depositados na articulação são justamente um dos ativadores clássicos do NLRP3, e a inflamação aguda da crise é interleucina-1 beta em ação. É por isso que alterações em moléculas do inflamassoma se associam tanto a doenças inflamatórias hereditárias quanto adquiridas.])

Um último recado, e ele resume o que a aula toda quis mostrar. A ativação dos PRR pode levar uma célula a liberar quatro tipos de produto, com temporalidades diferentes: produtos que já estavam prontos e guardados em grânulos, liberados na hora; produtos que existiam em forma inativa e são modificados após a ativação, como a pró-interleucina-1 beta; produtos que não existiam e só passam a ser fabricados depois do estímulo, dependendo de transcrição; e produtos de degradação da própria célula, liberados quando ela morre. Quatro cronogramas distintos partindo do mesmo gatilho — e é dessa combinação que nasce a plasticidade enorme de um sistema que costuma ser descrito, injustamente, como monótono.

#conclusao-box[
  O princípio que unifica esta aula inteira cabe numa frase: o sistema imune não pergunta se algo é estranho, pergunta se o tecido ainda está em ordem. Toda a arquitetura descrita aqui é a implementação dessa pergunta. Os PRR existem porque alguém tem que fazer a leitura; eles são herdados e fixos porque miram padrões que o micróbio não pode abandonar; distribuem-se por membrana, citosol e núcleo porque cada compartimento pode esconder um tipo de ameaça; e leem tanto PAMP quanto DAMP porque a perda de homeostasia pode vir de fora ou de dentro.

  O mecanismo nuclear é a conversão dessa leitura em transcrição. Um ligante muda a geometria do receptor, a geometria cria o sítio de acoplamento, o adaptador recrutado define o destino — MyD88 puxando NF-κB e AP-1 para os genes inflamatórios, TRIF puxando IRF para os genes de interferon — e o produto transcrito é o que executa as quatro estratégias da PARTE II. Onde o controle transcricional sozinho seria perigoso demais, o sistema acrescenta uma segunda trava: o inflamassoma exige um segundo sinal, independente, para converter a pró-interleucina-1 beta acumulada em citocina ativa.

  A clínica aparece exatamente nos pontos em que esse arranjo falha ou é forçado. Sem a explosão respiratória, o fagócito engole e não mata, e o organismo cerca o problema com granulomas. Sem controle sobre a montagem do NLRP3, o paciente inflama sem infecção e responde ao bloqueio da interleucina-1 beta. Sem interferon do tipo I, a contenção inicial da infecção viral não acontece e a resposta adquirida chega tarde demais. Em cada caso, uma peça do arco causa-mecanismo-consequência é retirada e o desfecho clínico revela para que ela servia.

  O que fica em aberto é o outro lado da ponte. Tudo o que foi descrito aqui autoriza, calibra e antecede a resposta adquirida — mas quem executa essa resposta são os linfócitos, com seus receptores sorteados, sua expansão clonal e sua memória de longa duração. O próximo passo é seguir a APC que sai do tecido carregando antígeno e laudo, chegar ao linfonodo e ver o que acontece quando o linfócito T finalmente encontra o peptídeo que seu receptor reconhece.
]
