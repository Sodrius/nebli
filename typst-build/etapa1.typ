#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  O sistema imune tem duas maneiras completamente diferentes de olhar para o mundo, e esta aula é sobre a primeira delas. Os linfócitos enxergam com receptores gerados ao acaso, um por clone, capazes de reconhecer praticamente qualquer molécula — mas justamente por serem aleatórios precisam ser selecionados, demoram para expandir e não sabem, sozinhos, se o que encontraram é perigoso. Antes disso, e o tempo todo, existe um segundo olhar: receptores prontos desde o nascimento, iguais em todas as células do mesmo tipo, que não perguntam "quem é você?" e sim "está tudo bem por aqui?". São os receptores para padrões moleculares. Eles não reconhecem indivíduos moleculares; reconhecem assinaturas de classes inteiras de moléculas que só deveriam aparecer quando há micro-organismo ou quando há dano — e, portanto, reconhecem a perda da homeostasia. Este resumo persegue quatro movimentos. Primeiro, por que o reconhecimento imune é hierárquico e o que a resposta inata decide antes de a adquirida existir. Depois, as famílias desses receptores e a lógica geográfica que explica onde cada um mora e por quê. Em seguida, o que acontece dentro da célula quando um deles é acionado — as duas vias dos TLR e a plataforma do inflamassoma. Por fim, as quatro estratégias com que o tecido tenta voltar ao normal e a linguagem química com que as células combinam esse esforço.
]

#parte-title("PARTE I — Duas maneiras de reconhecer e quem pergunta primeiro", primeira: true)

#subtopico("1.1 — O repertório clonal: aleatório, selecionado e ainda assim ambíguo")

Vale recuperar o que já foi construído nas aulas anteriores, porque é contra esse pano de fundo que o reconhecimento inato faz sentido. O repertório dos receptores clonais — #sigla("TCR", [T-cell receptor, receptor de antígeno do linfócito T]) e imunoglobulinas/#sigla("BCR", [B-cell receptor, imunoglobulina de membrana do linfócito B]) — é *completo*: em princípio ele consegue reconhecer qualquer molécula que exista. Essa completude tem um preço, e o preço é o método: o repertório é *gerado aleatoriamente*. Gerar ao acaso um receptor para tudo significa gerar também receptores contra o próprio corpo. A solução do sistema é acoplar geração aleatória a uma etapa de seleção, e essa seleção acontece num lugar específico, os órgãos linfoides primários, onde os antígenos próprios funcionam como filtro. O resultado é um repertório que, de maneira muito geral, distingue o próprio do não-próprio.

Dois fatos impedem que isso baste. O primeiro é que a seleção não é perfeita: quando ela falha, aparece a doença autoimune. O segundo é mais interessante e mais estrutural: se a única régua fosse próprio versus não-próprio, o organismo responderia contra tudo que é externo e inofensivo — a comida, por exemplo. Ou seja, distinguir próprio de não-próprio não é suficiente para decidir o que fazer. Faltava uma segunda pergunta, e é ela que a imunidade inata responde.

#subtopico("1.2 — Resposta ou tolerância: quem decide é o estado do tecido")

O mesmo reconhecimento específico pode terminar em dois desfechos opostos. Ou o sistema tenta *eliminar* o que reconheceu — é o que se chama, em geral, de resposta imune — ou o sistema *aceita* a presença daquele antígeno sem tentar eliminá-lo, e isso é tolerância imunológica. Repare que tolerância não é ausência de reconhecimento: é um desfecho ativo do reconhecimento. Tanto a resposta quanto a tolerância deixam #termo-nota[memória][adaptação duradoura do sistema imune que faz um mesmo estímulo ser tratado da mesma maneira na próxima vez, valendo tanto para resposta quanto para tolerância], isto é, o sistema se adapta para lidar com aquele mesmo estímulo da mesma maneira na próxima vez.

Isso transforma a escolha entre resposta e tolerância na questão essencial da imunologia clínica: no transplante, o desejável seria induzir tolerância ao órgão enxertado; no tumor, o desejável seria responder e eliminá-lo — e o problema é exatamente que o organismo com tumor já aprendeu que aquilo não é problema. O que hoje parece ser o principal fator de diferenciação é o estado homeostático do tecido de onde o antígeno veio quando foi levado ao sistema imune. Não é a identidade química do antígeno que decide; é o contexto em que ele foi coletado. E quem lê esse contexto é a imunidade inata.

#subtopico("1.3 — A hierarquia: primeiro a homeostasia, depois o antígeno")

Daí a formulação central: o reconhecimento no sistema imune é hierárquico. A primeira pergunta não é "que molécula é esta?", e sim "existe homeostasia?". Quem responde a essa primeira pergunta são os #termo-nota[receptores para padrões moleculares][receptores prontos, não clonais, que reconhecem assinaturas moleculares associadas a patógenos ou a dano tecidual e sinalizam perda de homeostasia] (#sigla("PRR", [pattern recognition receptors — receptores para padrões moleculares])). Se a resposta for "não há homeostasia", dispara-se a resposta imune inata.

Ao mesmo tempo — e esta simultaneidade é o ponto fino — a constituição molecular daquele tecido está sendo amostrada e apresentada aos receptores clonais nos órgãos linfoides secundários. As duas leituras correm em paralelo sobre o mesmo material: uma pergunta se está tudo bem, a outra pergunta o que exatamente está ali. Havendo o sinal da imunidade inata, aqueles antígenos desencadeiam uma resposta imune adquirida; não havendo, o mesmo antígeno tende à tolerância. A imunidade inata não é, portanto, um sistema mais primitivo que age enquanto a adquirida não chega: ela é a instância que autoriza e orienta a adquirida.

#confusao-prevista(
  titulo: "Inato não quer dizer inespecífico nem inferior",
  aluno_acha: [aluno acha que a imunidade inata é uma barreira grosseira e genérica que segura o inimigo até a resposta “de verdade”, a adquirida, ficar pronta],
  mecanismo: [na verdade o reconhecimento inato é específico — TLR3 reconhece dsRNA e não reconhece LPS —, só que a especificidade é para *classes* de moléculas, não para indivíduos moleculares, e é fixa no genoma em vez de sorteada. Mais do que isso: é a inata que decide se haverá resposta adquirida ou tolerância. Sem o sinal inato, o antígeno apresentado tende à tolerância.],
)

#subtopico("1.4 — A ponte entre as duas imunidades: apresentação de antígenos")

A ligação material entre as duas maneiras de reagir é a apresentação de antígenos. As células apresentadoras de antígenos (#sigla("APC", [antigen presenting cell — célula apresentadora de antígenos])) fazem duas coisas ao mesmo tempo no tecido: capturam moléculas e avaliam o estado homeostático do lugar de onde as capturaram. Depois processam esse material e o apresentam aos linfócitos T nos órgãos linfoides secundários. Os antígenos podem chegar diretamente ou ser capturados por linfócitos B, que também funcionam como células apresentadoras. O que sai dessa apresentação — resposta ou tolerância — carrega junto a informação de contexto que os PRR coletaram lá atrás.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-07.png",
  largura: 62%,
  legenda: [A APC captura moléculas do tecido e, junto com elas, o estado homeostático daquele tecido. O que ela leva ao órgão linfoide secundário não é só o antígeno: é o antígeno mais o contexto em que foi encontrado.])

#subtopico("1.5 — PAMP, DAMP e a ideia de perigo")

Os padrões que os PRR reconhecem vêm de duas origens. Quando a assinatura molecular pertence a um micro-organismo, fala-se em #sigla("PAMP", [pathogen associated molecular pattern — padrão molecular associado a patógeno]); quando ela pertence ao próprio tecido lesado e só aparece fora de lugar por causa do dano, fala-se em #sigla("DAMP", [damage associated molecular pattern — padrão molecular associado a dano]). É por incluir os DAMP que o sistema consegue disparar sem que exista qualquer infecção: uma queimadura, um infarto ou um trauma produzem inflamação legítima porque produzem padrões de dano.

Historicamente, a primeira formulação dessa ideia foi de Polly Matzinger, que falava em *danger* associated molecular pattern — o que dispara a resposta não é o não-próprio, é o perigo. A troca de "danger" por "damage" preservou o conteúdo e ancorou o conceito em algo mensurável: moléculas que só aparecem quando há lesão.

#mini-resumo[O repertório clonal é completo porque é aleatório, e por isso precisa de seleção nos órgãos linfoides primários; mesmo assim, distinguir próprio de não-próprio não decide o desfecho. Quem decide entre resposta e tolerância é o estado homeostático do tecido de onde veio o antígeno, lido pelos PRR. Por isso o reconhecimento é hierárquico: primeiro pergunta-se se existe homeostasia, depois o que é o antígeno. A ponte entre as duas leituras é a apresentação de antígenos. Os padrões lidos são PAMP, de micro-organismos, e DAMP, do tecido lesado.]

#mapa-parte(
  parte: "PARTE I",
  centro: [Primeiro o contexto, depois a identidade],
  nos: ((id: "1.2", titulo: [Contexto decide], texto: [O estado homeostático do tecido decide entre resposta e tolerância]),
        (id: "1.3", titulo: [Hierarquia], texto: [O PRR pergunta se há homeostasia antes de o antígeno ser lido]),
        (id: "1.5", titulo: [PAMP e DAMP], texto: [Assinatura de micróbio ou assinatura de dano do próprio tecido])),
  arestas: (),
  fecha-com: [Se os PRR fazem a primeira pergunta, cabe agora conhecer quem são e onde ficam.],
)

#parte-title("PARTE II — As famílias de PRR e a geografia celular do reconhecimento")

#subtopico("2.1 — Seis famílias e quatro endereços")

Os PRR não são uma molécula, e sim um conjunto de famílias que a pesquisa foi descobrindo uma a uma — encontrava-se um receptor e, em seguida, vários outros parecidos com ele, o que dá nome à família. O que organiza esse zoológico não é a estrutura, é o *endereço*: eles estão distribuídos por toda a célula, na membrana externa, nas membranas internas, soltos no citoplasma e até dentro do núcleo.

Na membrana ficam os C-type lectin receptors (#sigla("CTLR", [C-type lectin receptors — receptores de lectina tipo C, ligam açúcares de forma dependente de cálcio]), com Dectina-1 e DEC-205), os scavenger receptors (CD36, CD68, LOX-1) e os Toll-like receptors (#sigla("TLR", [Toll-like receptors — família de PRR de membrana com domínio TIR citoplasmático])), com TLR-3, TLR-4 e TLR-9 como exemplos. Os NOD-like receptors (#sigla("NLR", [NOD-like receptors — família de PRR com domínio de oligomerização ligante de nucleotídeo]), com NOD1, NOD2 e NLRP3) aparecem em membranas e no citoplasma. Só no citoplasma ficam os RIG-like receptors (#sigla("RLR", [RIG-I-like receptors — sensores citoplasmáticos de RNA viral]), com RIG-I, MDA5 e LGP2). E dentro do núcleo ficam os AIM2-like receptors (#sigla("ALR", [AIM2-like receptors — sensores de DNA de dupla fita, com localização nuclear]), com AIM2 e IFI16).

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-08.png",
  largura: 78%,
  legenda: [As famílias de PRR pela localização. Guardar o endereço vale mais do que guardar a lista de siglas: ele antecipa que tipo de ligante cada família encontra.])

#subtopico("2.2 — Por que o endereço prediz o ligante")

Há uma lógica por trás dessa distribuição, e ela é o conteúdo realmente aproveitável da tabela. Um sensor colocado na membrana plasmática está voltado para o meio extracelular e encontra o que existe *na superfície* de um micro-organismo íntegro: lipoproteínas, lipopolissacarídeo, flagelina, β-glucano de parede fúngica. Um sensor colocado na membrana do endossomo/lisossomo só encontra o que já foi internalizado e desmontado — e é exatamente ali que ácidos nucleicos ficam expostos. Um sensor solto no citosol encontra o que conseguiu atravessar a membrana ou o que se replica dentro da célula: RNA viral em replicação, fragmentos de parede bacteriana de bactérias intracelulares.

Isso resolve, de saída, duas perguntas que parecem decoreba. Por que os TLR que leem ácido nucleico são endossomais e não de superfície? Porque DNA e RNA próprios circulam o tempo todo no meio extracelular, vindos de células que morreram; colocar o sensor dentro de um compartimento ácido, ao qual só se chega por endocitose, é um mecanismo de segurança contra autorreatividade. E por que sensores de RNA viral são citoplasmáticos? Porque é no citoplasma que o vírus replica.

#atencao-box("Quando a segregação falha",
  [A separação entre ácido nucleico próprio (extracelular, ignorado) e não-próprio (endossomal ou citosólico, sinalizado) é topológica, não química. Quando esse arranjo se quebra — excesso de material apoptótico não removido, complexos de DNA com autoanticorpos que entram por receptor Fc e entregam DNA próprio dentro do endossomo — o TLR9 passa a ver DNA próprio como se fosse microbiano. É esse o eixo mecanístico que liga sensores inatos a doenças autoimunes com assinatura de interferon, como o lúpus.])

#subtopico("2.3 — Os TLR, um a um: ligante e compartimento")

Os TLR conhecidos vão de 1 a 11, com uma peculiaridade de espécie: o TLR7 é o do camundongo e o TLR8 é o equivalente humano; o humano não tem 7 funcional e o camundongo não tem 8. São proteínas de membrana, e essa membrana pode ser a plasmática ou a do endossomo/lisossomo.

Na membrana plasmática: TLR1 reconhece lipoproteína triacilada de bactérias; TLR2 reconhece lipoproteína, com origem notavelmente ampla — bactérias, vírus, parasitas e o próprio organismo; TLR4 reconhece #sigla("LPS", [lipopolissacarídeo, a endotoxina da parede de bactérias Gram-negativas]), a endotoxina bacteriana, e também tem origens múltiplas incluindo vírus e próprio; TLR5 reconhece flagelina bacteriana; TLR6 reconhece lipoproteína diacilada de bactérias e vírus; TLR11 reconhece uma molécula semelhante à profilina, de protozoários.

No endossomo/lisossomo: TLR3 reconhece #sigla("dsRNA", [double-stranded RNA — RNA de dupla fita, intermediário de replicação de muitos vírus]) viral; TLR7 (TLR8 no humano) reconhece #sigla("ssRNA", [single-stranded RNA — RNA de fita simples]), com origem viral, bacteriana e própria; TLR9 reconhece DNA com motivos CpG não metilados, de vírus, bactérias, protozoários e próprio; TLR10 permanece com ligante desconhecido.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-16.png",
  largura: 92%,
  legenda: [Os TLR com localização, ligante típico e origem do ligante. Leia a coluna do meio junto com a da esquerda: todo sensor de ácido nucleico está no endolisossomo, todo sensor de lipídio ou proteína de superfície está na membrana plasmática.])

#confusao-prevista(
  titulo: "A lista de ligantes não é um catálogo fechado",
  aluno_acha: [aluno decora “TLR4 = LPS” como se cada TLR tivesse exatamente um ligante e o conjunto cobrisse todos os padrões existentes],
  mecanismo: [o que a tabela traz é o ligante *tipicamente* reconhecido. Se onze receptores reconhecessem apenas onze moléculas, o sistema seria pobre demais para funcionar. O TLR4 reconhece LPS e também padrões de origem viral e própria — a coluna “origem do ligante” já mostra isso. Há padrões moleculares que ainda não conseguimos discernir com precisão.],
)

#subtopico("2.4 — Além dos TLR: RLR, NLR e CLR")

As outras famílias completam a cobertura, e de novo o endereço explica o ligante. Entre os RLR, todos citoplasmáticos: RIG-I reconhece dsRNA curto e dsRNA com trifosfato na extremidade 5′ — uma marca química que o RNA próprio maduro não tem —, de vírus de RNA e também de vírus de DNA; MDA5 reconhece dsRNA longo, tipicamente de picornavírus; LGP2 tem ligante desconhecido e função reguladora. Entre os NLR, também citoplasmáticos: NOD1 reconhece iE-DAP e NOD2 reconhece #sigla("MDP", [muramil dipeptídeo, fragmento do peptidoglicano da parede bacteriana]), ambos fragmentos de peptidoglicano bacteriano. Entre os CLR, de membrana plasmática: Dectina-1 e Dectina-2 reconhecem β-glucano de fungos e MINCLE reconhece SAP130, de origem própria e fúngica.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-17.png",
  largura: 92%,
  legenda: [RLR, NLR e CLR. Sensores citoplasmáticos leem RNA viral em replicação e fragmentos de parede de bactéria intracelular; sensores de membrana leem parede fúngica.])

#clinica-box("NOD2 e doença de Crohn",
  [O NOD2 lê MDP, um fragmento de peptidoglicano, dentro do citoplasma de células epiteliais e de Paneth do intestino. Variantes de perda de função no NOD2 estão entre os fatores de risco genético mais bem estabelecidos para doença de Crohn: sensor defeituoso significa resposta antimicrobiana epitelial insuficiente e inflamação crônica compensatória. É um exemplo concreto de que um único PRR mal calibrado produz doença inflamatória.])

#subtopico("2.5 — De onde vem o nome Toll")

A origem do nome ajuda a fixar o que a molécula é. *Toll* é uma palavra alemã coloquial que quer dizer bacana, ótimo, divertido — o nome foi dado a uma molécula descoberta na drosófila, onde o papel inicial do Toll é de embriogênese, não de defesa. As moléculas dos vertebrados foram chamadas de Toll-*like* porque são estruturalmente parecidas com aquele Toll, e nelas essa estrutura tem função de reconhecimento de padrões moleculares na imunidade inata. Isto é: a família não foi batizada pela função imune, foi batizada pela semelhança estrutural com uma proteína de desenvolvimento de mosca.

#mini-resumo[As famílias de PRR se organizam por endereço, e o endereço prediz o ligante: membrana plasmática lê superfície microbiana, endolisossomo lê ácido nucleico internalizado, citoplasma lê replicação viral e parede de bactéria intracelular, núcleo lê DNA. Nos TLR, todo sensor de ácido nucleico é endolisossomal — TLR3 para dsRNA, TLR7/8 para ssRNA, TLR9 para CpG-DNA — e os de superfície leem lipoproteínas, LPS, flagelina e profilina. RIG-I e MDA5 leem dsRNA no citosol, NOD1 e NOD2 leem peptidoglicano, as dectinas leem β-glucano fúngico. O nome Toll vem de uma proteína de embriogênese da drosófila.]

#mapa-parte(
  parte: "PARTE II",
  centro: [O endereço do sensor prediz o ligante],
  nos: ((id: "2.2", titulo: [Topologia], texto: [Ácido nucleico só é lido dentro de compartimento — trava contra o próprio]),
        (id: "2.3", titulo: [TLR], texto: [Superfície lê lipídio e proteína; endolisossomo lê dsRNA, ssRNA e CpG]),
        (id: "2.4", titulo: [Outras famílias], texto: [RLR e NLR leem o citosol; CLR leem parede de fungo])),
  arestas: (),
  fecha-com: [Reconhecido o padrão, falta ver o que acontece dentro da célula.],
)

#parte-title("PARTE III — Da sinalização à plataforma: o que acontece dentro da célula")

#subtopico("3.1 — Como um TLR liga: dimerização e mudança conformacional")

O primeiro evento é mecânico, não químico. Há duas possibilidades. Numa, o TLR estava isolado na membrana e o ligante força a *dimerização* — dois receptores se aproximam e só então a porção citoplasmática consegue dar sinal. Na outra, o dímero já estava pré-formado e o ligante, ao se encaixar, produz uma *mudança conformacional* nesse dímero. Em ambos os casos o que muda é a geometria das caudas citoplasmáticas: elas passam a formar uma superfície capaz de recrutar proteínas adaptadoras. Nada de novo é sintetizado nesse instante; o receptor apenas muda de forma.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-18.png",
  largura: 88%,
  legenda: [DAMPs e PAMPs ativam o TLR por dimerização ou mudança conformacional. Daí saem duas rotas adaptadoras, MyD88 e TRIF, que se cruzam, e cinco consequências distintas.])

#subtopico("3.2 — MyD88 e TRIF: dois adaptadores, dois destinos")

A cauda citoplasmática remodelada recruta um de dois adaptadores principais. O primeiro e mais usado é o #termo-nota[MyD88][myeloid differentiation primary response protein 88; adaptador que acopla a maioria dos TLR à via NF-κB/AP-1 e à produção de citocinas inflamatórias], que inicia um caminho longo terminando em dois fatores de transcrição: o #sigla("NF-κB", [nuclear factor-κB — fator de transcrição central no controle de genes inflamatórios]) e o #sigla("AP-1", [activator protein 1 — fator de transcrição da resposta inflamatória e de estresse]). No núcleo, esses fatores ligam os genes das citocinas inflamatórias e das quimiocinas — e é esse produto que se manifesta como inflamação, chamada de fagócitos e tentativa de restaurar a homeostasia.

O segundo adaptador é o #termo-nota[TRIF][TIR domain-containing adaptor protein inducing IFN-β; adaptador que acopla TLR à ativação dos IRF e à produção de interferons do tipo I], que leva à formação dos #sigla("IRF", [IFN-regulatory factors — fatores reguladores de interferon]) e, portanto, à produção de interferons do tipo I. Os interferons têm atividade antiviral e também participam da ativação de linfócitos T. Traduzindo o desenho: a rota MyD88 é a rota da inflamação e a rota TRIF é a rota antiviral.

Três precisões impedem que isso vire um esquema ingênuo. Primeira: alguns TLR usam MyD88, outros usam TRIF, e alguns usam as duas. Segunda: as duas vias se cruzam — entre o adaptador e o fator de transcrição há muitas moléculas intermediárias, com ramificações, de modo que um ligante que aciona um TLR essencialmente MyD88 pode acabar produzindo interferon. Terceira: essas não são as únicas consequências. A ativação de TLR também sinaliza sobrevivência celular pela via da AKT, morte por ativação da caspase-8, e ativação do inflamassoma por via do TRIF.

Todas ao mesmo tempo? Não. Sai mais de uma consequência e menos de outra, e o que decide é a disposição dos TLR na célula, quantos TLR aquela célula tem e que outros sinais ela está recebendo naquele momento.

#confusao-prevista(
  titulo: "Especificidade do ligante não garante especificidade do efeito",
  aluno_acha: [aluno espera que cada TLR, por reconhecer um ligante próprio, produza um efeito próprio e distinto dos demais],
  mecanismo: [se olharmos o desenho, todos os TLR convergem para os mesmos dois adaptadores e para os mesmos fatores de transcrição. A especificidade do efeito não vem do receptor sozinho: vem de qual TLR, em que célula, com que outros sinais simultâneos e com que arranjo espacial das moléculas de sinalização. É e não é o mesmo caminho.],
)

#subtopico("3.3 — A anatomia do citoplasma")

Vale reter um conceito que a aula deixa explícito e que costuma passar batido: o citoplasma não é um saco onde tudo está misturado. Assim como a anatomia macroscópica importa para a função de um órgão — o músculo precisa estar inserido no lugar certo para dobrar a articulação —, existe uma anatomia dentro da célula. Não adianta ativar a molécula MyD88 se ela não estiver perto das quinases IRAK4 e IRAK1 para poder ativá-las. Essas moléculas não flutuam ao acaso: são ativamente levadas para um lugar ou para outro. Por consequência, a pré-ativação da célula, ao mudar onde as moléculas estão, muda o resultado do mesmo estímulo. É difícil de estudar porque é dinâmico e espacial, e é justamente aí que se concentram as chances de intervenção farmacológica precisa.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-19.png",
  largura: 70%,
  legenda: [O detalhe real da via não é para memorizar: é para perceber a quantidade de intermediários e o cruzamento entre rotas. Fonte: Gay NJ, Symmons MF, Gangloff M, Bryant CE, Oncogene 2014;14(8):546–58.])

#subtopico("3.4 — O inflamassoma: uma plataforma que corta")

Existe uma segunda rota na imunidade inata que não termina em transcrição, e sim em *processamento de proteína*. Inflamassomas são plataformas moleculares: aglomerados em que uma molécula se junta à outra, que se junta à outra, montados a partir da ativação de determinados PRR. A função dessa plataforma é muito específica — promover a maturação de citocinas pró-inflamatórias.

Maturação aqui tem sentido literal. O gene ativado pelo fator de transcrição produz uma proteína que ainda não é funcional, uma pró-citocina. O inflamassoma corta essa pró-citocina e gera a citocina ativa. As duas principais são a #sigla("IL-1β", [interleucina-1 beta, citocina pró-inflamatória central, produzida como pró-forma inativa]) e a IL-18. Quem executa o corte é a #termo-nota[caspase-1][protease ativada dentro do inflamassoma que cliva pró-IL-1β e pró-IL-18 em suas formas maduras], uma protease ativada dentro da própria plataforma.

Dentro da família dos NLR há uma divisão que a aula faz questão de marcar. Os NOD, apesar de pertencerem à família NOD-like, *não* montam inflamassoma: eles ficam soltos no citoplasma, reconhecem produtos bacterianos e ativam a via do NF-κB, levando à produção de citocinas inflamatórias. Quem monta inflamassoma são os NLRP, o IPAF e, de outra família, o AIM2. Ou seja, dentro do mesmo grupo de sensores citoplasmáticos há dois destinos distintos: transcrição, pelos NOD, e clivagem, pelos NLRP/IPAF/AIM2.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-20.png",
  largura: 70%,
  legenda: [Dois destinos dentro da família NLR: os NOD ativam NF-κB e produzem citocinas; NLRP, IPAF e AIM2 formam inflamassomas, ativam caspase-1 e clivam pró-IL-1β e pró-IL-18.])

#clinica-box("Doenças por inflamassoma",
  [Alterações na função de moléculas do inflamassoma estão fortemente associadas a doenças inflamatórias hereditárias — as síndromes periódicas associadas à criopirina, por ganho de função do NLRP3, com febre recorrente e inflamação estéril — e também a doenças inflamatórias adquiridas, como a gota, em que cristais de urato ativam o NLRP3. É por isso que o bloqueio farmacológico da IL-1 funciona nessas condições: interrompe-se o produto final da plataforma.])

#subtopico("3.5 — NLRP3: por que são precisos dois sinais")

O inflamassoma NLRP3 mostra o modelo completo, e o detalhe decisivo é que uma célula com um só sinal provavelmente não vai adiante. São necessários dois eventos independentes.

O primeiro é o *priming*: um estímulo pró-inflamatório — TLR, TNF, a própria IL-1β — ativa NF-κB e faz a célula transcrever e sintetizar a pró-IL-1β, que fica estocada no citosol na forma inativa. Sem essa etapa não existe substrato para cortar. O segundo é o sinal de montagem: sinais de perigo que incluem ATP extracelular agindo no receptor P2X7 com efluxo de potássio pela panexina-1, ligantes cristalinos ou particulados que são fagocitados e rompem o lisossomo, e as espécies reativas de oxigênio geradas nessas duas situações. Esses sinais convergem para a montagem da plataforma: o NLRP3 oligomeriza pelos seus domínios NACHT, recruta o adaptador ASC pelo domínio PYD, e o ASC recruta a pró-caspase-1 pelo domínio CARD.

Montada a plataforma, a caspase-1 se ativa por proximidade, cliva a pró-IL-1β estocada e a IL-1β madura é liberada. A exigência de dois sinais é uma trava de segurança: a citocina mais inflamatória do repertório inato só é liberada quando a célula recebeu, separadamente, a informação de que há contexto inflamatório e a informação de que há dano em curso.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-21.png",
  largura: 82%,
  legenda: [O NLRP3 exige priming, que fabrica a pró-IL-1β, e um segundo sinal — ATP/P2X7 com efluxo de K⁺, ruptura lisossômica por cristais, espécies reativas de oxigênio — que monta NLRP3 + ASC + caspase-1. Fonte: Schroder K, Tschopp J, Cell 2010;140(6):821–32.])

#mini-resumo[O TLR liga por dimerização ou por mudança conformacional de um dímero pré-formado e recruta MyD88, que leva a NF-κB e AP-1 e às citocinas inflamatórias, ou TRIF, que leva aos IRF e aos interferons do tipo I; há também sobrevivência via AKT, apoptose via caspase-8 e ativação do inflamassoma via TRIF, com cruzamento entre as rotas. O resultado depende do arranjo espacial das moléculas dentro da célula. O inflamassoma é uma plataforma que ativa caspase-1 e cliva pró-IL-1β e pró-IL-18; os NOD não o montam, ativam NF-κB. O NLRP3 exige priming, que sintetiza a pró-IL-1β, mais um segundo sinal de dano que monta a plataforma.]

#mapa-parte(
  parte: "PARTE III",
  centro: [Duas rotas de sinal e uma plataforma que corta],
  nos: ((id: "3.1", titulo: [Ligar], texto: [Dimerização ou mudança conformacional de dímero pré-formado]),
        (id: "3.2", titulo: [Bifurcar], texto: [MyD88 leva à inflamação; TRIF leva ao interferon do tipo I]),
        (id: "3.5", titulo: [Cortar], texto: [NLRP3 exige priming e segundo sinal para ativar caspase-1])),
  arestas: (),
  fecha-com: [Sinalizada a perda de homeostasia, resta ver o que o tecido efetivamente faz.],
)

#parte-title("PARTE IV — As quatro estratégias e a linguagem das citocinas")

#subtopico("4.1 — O que a resposta inata está tentando fazer")

A resposta desencadeada pelos PRR é, do começo ao fim, uma tentativa de restauração da homeostasia. As estratégias são quatro e vale enunciá-las pelo verbo, porque o verbo já contém o mecanismo: salvar as células vizinhas, com os interferons do tipo I; eliminar as células doentes, pela citotoxicidade celular; limpar a área, pela fagocitose; e chamar socorro, produzindo fatores de crescimento, citocinas, quimiocinas e outros mediadores. A quarta não é bem uma quarta estratégia isolada — ela está embutida em todas as outras, porque é o que muda a chegada de células ao local e modula a função das que já estão ali.

#subtopico("4.2 — Interferons do tipo I: uma ação solidária")

O interferon é a estratégia de salvar o vizinho, e o desenho é quase altruísta. O vírus adere à célula e libera seu ácido nucleico no interior — e neutralizar um vírus, aliás, significa bloquear ou a adesão ou a penetração, que são etapas distintas: dá para deixar aderir e ainda assim impedir a liberação do ácido nucleico. Uma vez dentro, o ácido nucleico viral é reconhecido, e a resposta imediata da célula infectada é produzir interferon.

Esse interferon é liberado e atinge as células ao redor. Os vírus produzidos também vão atingir as células ao redor — mas, se elas já estiverem sob ação do interferon, a replicação viral dentro delas está bloqueada. O desfecho é preciso: a célula infectada será destruída pelo vírus, não há mais o que fazer por ela, mas ela protege as células do lado. O que o interferon faz não é curar a célula que o produziu; é induzir um estado antiviral nas vizinhas ainda sadias.

Como todo mediador produzido no sítio da reação, o interferon tem também efeitos sistêmicos — inclusive febre e dor no corpo. Os sintomas da gripe são, muitas vezes, causados mais pelo interferon do que pelo vírus em si.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-10.png",
  largura: 62%,
  legenda: [A célula infectada produz interferon e o libera antes de morrer. As vizinhas expostas ao interferon bloqueiam a replicação viral e sobrevivem; a produtora, não. Daí a expressão “ação solidária”.])

#subtopico("4.3 — Citotoxicidade celular: convencer a célula-alvo a morrer")

Aqui também o mecanismo desfaz uma imagem intuitiva. A citotoxicidade celular não é uma destruição de fora para dentro, não é dar um tiro na célula: é um convencimento da célula-alvo a morrer, um suicídio induzido. A célula efetora identifica a célula-alvo — e pode fazê-lo por receptores clonais, da imunidade adquirida, ou por receptores inatos, isto é, por PRR, sem precisar de nenhuma adaptação prévia.

Feito o reconhecimento, as duas células se encontram e a sinalização de morte acontece por dois mecanismos. Um é a interação de moléculas de membrana que já estavam presentes o tempo todo e só precisavam ser aproximadas — o par FasL–Fas é o exemplo — e quem faz essa aproximação é o próprio reconhecimento específico. O outro é a desgranulação: a célula citotóxica possui grânulos com substâncias que, agindo sobre a célula-alvo, induzem morte ativa. Nos dois casos a célula-alvo entra em apoptose. E há uma economia elegante no processo: destruída a célula-alvo, a célula citotóxica permanece intacta e parte à procura de outros alvos.

#subtopico("4.4 — Fagocitose: limpar a área, em etapas")

A fagocitose é um processo ancestral — funciona desde os protozoários — incorporado à nossa fisiologia, e se desenvolve em etapas encadeadas.

Primeiro a localização do alvo, por migração celular dirigida, a quimiotaxia. As moléculas quimiotáticas vêm de várias fontes: da própria bactéria, que gera moléculas atrativas, e de um sistema solúvel de reconhecimento de padrões — proteínas do plasma que funcionam como um sistema de PRR solúvel, e cujo nome é complemento.

Depois a adesão. Encostar não basta: a partícula pode não interagir direito com a membrana do fagócito. Os fagócitos têm PRR que identificam padrões comuns em alvos fagocitáveis, mas o sistema também produz moléculas que grudam na partícula e para as quais existem receptores no fagócito — é a #termo-nota[opsonização][revestimento de uma partícula por moléculas do hospedeiro, como anticorpos e complemento, para as quais o fagócito tem receptores, aumentando muito a eficiência da adesão]. A exceção é a chamada fagocitose de superfície, em que a partícula é comprimida contra uma superfície e englobada sem opsonina.

Em seguida, a motilidade da membrana engloba a partícula por interações sucessivas, como o fechamento de um zíper: os receptores da superfície do fagócito vão grudando na partícula, ponto a ponto, e a membrana vai se fechando em volta. Forma-se o fagossoma, que se funde com lisossomas carregados de enzimas. E na própria membrana do fagossoma existe um sistema gerador de radicais livres de oxigênio, o que provoca a explosão respiratória — a célula fagocítica consome muito mais oxigênio do que uma célula que não está fagocitando. A destruição do conteúdo resulta da soma de enzimas lisossômicas com radicais livres.

Duas dessas etapas são explicitamente moduláveis — a motilidade da membrana e o fechamento em zíper —, e é por isso que a fagocitose pode ser potencializada pelo ambiente de citocinas: não se trata de um reflexo tudo-ou-nada.

#figura-nebli("/figuras/imuno-01-reconhecimento-inato/slide-12.png",
  largura: 74%,
  legenda: [As etapas da fagocitose. Quimiotaxia, adesão com opsonização, zíper, fagossoma, fusão lisossômica e destruição por enzimas e radicais livres.])

#subtopico("4.5 — Citocinas: a linguagem que combina o esforço")

Nada disso funciona sem informação circulando, e os mediadores da comunicação intercelular são o que permite que células distantes se coordenem. As citocinas são proteínas ou glicoproteínas produzidas pelas células com múltiplas ações — são #termo-nota[pleiotrópicas][que produzem múltiplos efeitos diferentes, dependendo da célula-alvo, do contexto e dos outros sinais presentes], e é essa pleiotropia que dá plasticidade à resposta. Vale um cuidado experimental que a aula faz questão de registrar: como as citocinas são muito pleiotrópicas, mostrar que uma citocina faz uma determinada ação é fácil, basta montar o experimento do jeito certo.

Um ponto mecanístico importa mais do que a lista de nomes: não adianta ter a citocina se a célula-alvo não tiver o receptor para ela. É a expressão do receptor que define quem escuta a mensagem, e é isso que torna a resposta adaptável — a mesma citocina, no mesmo tecido, produz efeitos diferentes conforme quem está equipado para responder.

Os nomes são categorias históricas, não classes funcionais. Interleucinas (IL mais um número, já mais de trinta descritas) são citocinas de comunicação entre leucócitos; fatores de crescimento terminam em GF ou, quando descobertos no estudo da hematopoiese, em #sigla("CSF", [colony stimulating factor — fator estimulador de colônias, com uma letra na frente indicando o tipo de colônia formada]), com uma letra na frente indicando o tipo de colônia formada; interferons e quimiocinas completam o quadro. A advertência é explícita: uma molécula chamada de fator de crescimento é pleiotrópica e faz muito além de induzir crescimento, e uma molécula que induz crescimento pode nunca ter recebido esse nome. A nomenclatura reflete quem descobriu e como, não o que a molécula faz.

Além das citocinas proteicas existem os mediadores lipídicos: quando a célula é ativada, uma das respostas é retirar lipídios da membrana e metabolizá-los. O ácido araquidônico, pendurado no fosfolipídio de membrana, é fragmentado e gera prostaglandinas e leucotrienos, além do #sigla("PAF", [platelet activating factor — fator ativador de plaquetas, mediador lipídico pró-inflamatório]). E há uma família mais recente e mais complexa: os exossomos, nanovesículas com membrana e conteúdo que a célula libera e que circulam no sangue. Não são restos celulares — são sinalizadores capazes de mudar completamente a função de outra célula, e hoje são estudados inclusive como instrumento terapêutico.

#subtopico("4.6 — Quimiocinas e alguns nomes que voltam")

As quimiocinas são as citocinas cuja função é dirigir migração, e sua nomenclatura, ao contrário das demais, é estrutural: as quatro famílias — CXC, CC, CX3C e XC — são definidas pelo arranjo dos primeiros resíduos de cisteína da molécula. Exemplos que reaparecem: CXCL8, também chamada IL-8; CCL2, também chamada MCP-1; CX3CL1, a fractalquina; e XCL1, a linfotactina. A dupla nomenclatura de CXCL8/IL-8 é a melhor ilustração do problema dos nomes: a mesma molécula foi batizada duas vezes, uma pela função de comunicação entre leucócitos e outra pela estrutura.

Entre as citocinas que vale reconhecer pelo uso clínico: a IL-6 tornou-se alvo terapêutico com anticorpos que bloqueiam sua ação em formas graves de COVID-19; G-CSF e GM-CSF são usados como medicamentos, por exemplo em transplantes; os interferons alfa e beta são usados com frequência na clínica, enquanto o interferon gama, apesar de promissor no papel, nunca funcionou bem na prática clínica.

#clinica-box("Por que a febre é defesa e não apenas sintoma",
  [Os produtos da resposta inata provocam alterações sistêmicas, e a febre é a mais óbvia delas — uma adaptação do organismo para lidar com a perda de homeostasia. O experimento clássico é feito em lagarto, que não regula a própria temperatura e a controla se expondo mais ou menos ao sol: infectando o animal e impedindo que ele se aqueça, ou seja, impedindo que desenvolva febre, ele morre com muito mais facilidade. Daí a cautela com o antitérmico automático: ele trata o desconforto suprimindo um mecanismo de defesa.])

#subtopico("4.7 — Plasticidade: quatro tipos de produto, uma resposta variável")

Fechando o raciocínio da aula: a ativação dos PRR leva uma célula a liberar quatro tipos distintos de produto. Produtos previamente produzidos e armazenados, prontos para sair; produtos modificados após a ativação — e a pró-IL-1β clivada em IL-1β é exatamente esse caso; produtos produzidos somente após a ativação, quando a célula não tinha nada estocado e apenas a capacidade de sintetizar; e produtos de degradação celular, liberados porque a célula morre. Cada categoria tem cinética própria, o que faz a mesma ativação render respostas diferentes ao longo do tempo.

É isso que desmente a ideia de que a resposta inata seria monótona por não ter receptores diversos. A diversidade não está no repertório de reconhecimento e sim na combinação: qual receptor, em qual célula, com quais outros sinais, gerando qual mistura de produtos. Duas moléculas de lipoproteína diacilada ligeiramente diferentes, ativando o mesmo TLR6, podem induzir mudanças diferentes na célula. Essa plasticidade torna o organismo capaz de se adaptar a inúmeras situações, torna o estudo difícil e, ao mesmo tempo, abre as oportunidades de intervenção específica.

#mini-resumo[As quatro estratégias da resposta inata são salvar o vizinho (interferon do tipo I, que induz estado antiviral nas células ao redor enquanto a produtora morre), eliminar a célula doente (citotoxicidade, que induz apoptose por FasL–Fas ou por desgranulação e preserva a efetora), limpar a área (fagocitose, com quimiotaxia, opsonização, zíper, fagossoma, fusão lisossômica, enzimas e explosão respiratória) e chamar socorro (citocinas e quimiocinas). Citocinas são pleiotrópicas e dependem do receptor na célula-alvo; a nomenclatura é histórica, exceto nas quimiocinas, que são classificadas pela estrutura em CXC, CC, CX3C e XC. A febre é mecanismo de defesa. A ativação dos PRR libera produtos estocados, modificados, recém-sintetizados e de degradação — daí a plasticidade.]

#mapa-parte(
  parte: "PARTE IV",
  centro: [Restaurar a homeostasia por quatro caminhos],
  nos: ((id: "4.2", titulo: [Salvar], texto: [O interferon do tipo I induz estado antiviral nas células vizinhas]),
        (id: "4.3", titulo: [Eliminar], texto: [A citotoxicidade induz apoptose na célula-alvo e preserva a efetora]),
        (id: "4.4", titulo: [Limpar e chamar], texto: [Fagocitose destrói o alvo; citocinas e quimiocinas recrutam ajuda])),
  arestas: (),
  fecha-com: [As quatro convergem numa só finalidade: devolver o tecido ao estado homeostático.],
)

#conclusao-box[
  A aula inteira cabe numa reordenação de prioridades. O sistema imune não começa perguntando quem é o invasor; começa perguntando se o tecido está bem. Quem faz essa pergunta são os PRR, receptores prontos, distribuídos por membrana, endossomo, citosol e núcleo, cujo endereço já antecipa que padrão eles encontram — e que leem tanto assinaturas de micro-organismo, os PAMP, quanto assinaturas de dano do próprio tecido, os DAMP. A resposta a essa pergunta é o que autoriza a imunidade adquirida: com sinal inato, o antígeno apresentado gera resposta; sem ele, tende à tolerância. Dentro da célula, o sinal se bifurca em duas rotas que se cruzam — MyD88 para inflamação e TRIF para interferon — e pode montar uma plataforma, o inflamassoma, cuja função não é transcrever e sim cortar pró-citocinas em IL-1β e IL-18 madura, com a trava de segurança dos dois sinais no NLRP3. Fora da célula, o esforço se distribui em quatro estratégias que convergem para o mesmo objetivo de restaurar a homeostasia, coordenadas por uma linguagem química pleiotrópica cujo efeito depende de quem tem o receptor para escutá-la. Guardar essa arquitetura vale mais do que guardar as listas: com ela, cada nome novo encontra um lugar.
]
