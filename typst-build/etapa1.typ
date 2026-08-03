#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Nos primeiros anos de vida, o cérebro de uma criança faz algo que nenhum órgão adulto repete: constrói-se a si mesmo em resposta ao que vive. Não é um adulto pequeno esperando crescer — é um sistema em obra, montando a própria arquitetura a partir da experiência. Este resumo persegue uma única ideia, por três caminhos. Primeiro, o que os estudiosos entenderam por *desenvolvimento* e as lentes que criaram para enxergá-lo. Depois, o motor biológico por baixo de tudo: o cérebro plástico e a janela estreita em que ele mais se deixa moldar. Por fim, o que acontece quando o ambiente ajuda — ou machuca — essa construção, e como o pediatra vigia, mede e protege esse processo. A pergunta de fundo é sempre a mesma: por que os primeiros anos decidem tanto do que vem depois.
]

#parte-title("PARTE I — O que é desenvolvimento e as lentes para enxergá-lo", primeira: true)

#subtopico("1.1 — Do \"adulto em miniatura\" ao desenvolvimento por maturação")

Por muito tempo a infância simplesmente não existia como categoria. Até o século XVII, passada a primeira infância, a criança era tratada como um indivíduo comum em tamanho reduzido — um adulto em miniatura, com as mesmas roupas, os mesmos deveres e nenhuma expectativa de que pensasse ou sentisse de modo próprio. A virada veio com o Iluminismo. Rousseau propôs que a criança nasce com um plano interno que se realiza por etapas até a vida adulta — a ideia, ainda tosca, de que existe um percurso próprio da infância.

Esse germe amadureceu, entre o fim do século XVIII e o início do XX, na chamada *teoria organicista*: a criança se desenvolve à medida que seus órgãos amadurecem, e cada órgão mais maduro permite funções cada vez mais complexas. É daqui que nasce a noção de #termo-nota[marco do desenvolvimento][habilidade esperada para uma idade — sentar, andar, falar — que sinaliza a maturação de um sistema] — sustentar a cabeça, sentar, andar, falar. O ponto que fica desta primeira lente é mecânico e vale para tudo o que vem a seguir: *desenvolver é ganhar função porque uma estrutura amadureceu*. A habilidade nova não aparece por acaso; ela é o sinal externo de que algo, por dentro, ficou pronto.

#subtopico("1.2 — Quatro lentes teóricas complementares")

Se a maturação dos órgãos explica o *quando*, ela não explica sozinha o *como* a criança constrói uma mente. Ao longo do século XX, quatro grandes teóricos ofereceram lentes diferentes — e complementares, não concorrentes — para esse mesmo processo. Vale conhecê-las porque cada uma ilumina um pedaço que as outras deixam na sombra.

Jean Piaget olhou para a #termo-nota[cognição][o conjunto dos processos de conhecer: perceber, raciocinar, lembrar, resolver problemas]. Para ele, a criança não recebe conhecimento passivamente: ela o *constrói ativamente* interagindo com o mundo, e passa por estágios com formas de pensar qualitativamente distintas. No estágio sensório-motor (0–2 anos), o bebê conhece pelo corpo — toca, leva à boca, sacode — e conquista a #termo-nota[permanência do objeto][entender que uma coisa continua existindo mesmo quando sai de vista; firma-se por volta dos 8–9 meses], a descoberta de que o objeto que sumiu de vista continua existindo — conquista que se firma por volta dos 8 a 9 meses e que, não por acaso, coincide com o surgimento da ansiedade diante de estranhos: o bebê agora guarda a imagem do cuidador e percebe quem *não* é ele. No pré-operacional (2–7 anos), surgem símbolos, linguagem e imaginação, mas o pensamento ainda é egocêntrico — a criança custa a sair do próprio ponto de vista. No operatório concreto (7–11 anos), o raciocínio lógico se firma sobre coisas concretas; e só no operatório formal (12 anos em diante) o pensamento abstrato e hipotético se abre por completo.

Erik Erikson mudou a lente do cognitivo para o afetivo e social. O desenvolvimento, para ele, avança pela resolução de uma sequência de crises psicossociais — cada fase da vida coloca um conflito, e resolvê-lo bem deixa como saldo uma virtude. No primeiro ano e meio, a criança vive *confiança versus desconfiança*: se o cuidado é previsível e responsivo, ela sai com a virtude da esperança. Vêm depois *autonomia versus vergonha* (a virtude da vontade), *iniciativa versus culpa* (o propósito), *indústria versus inferioridade* (a competência) e, na adolescência, *identidade versus confusão de papéis* (a lealdade). A leitura que fica é que o vínculo com o cuidador não é pano de fundo — é o material com que a criança constrói a confiança básica em si e no mundo.

As duas últimas lentes puxam o foco para fora da criança. Urie Bronfenbrenner desenhou um *modelo ecológico*: o desenvolvimento acontece dentro de sistemas encaixados como bonecas russas. O microssistema é o contato direto (família, escola); o mesossistema são as interações entre esses contatos; o exossistema são ambientes que afetam a criança sem que ela participe (o trabalho dos pais, por exemplo); o macrossistema são os valores e políticas da cultura; e o cronossistema é o próprio tempo histórico. Lev Vygotsky, por sua vez, colocou a interação social no centro do desenvolvimento cognitivo. Seu conceito mais útil na clínica é a #termo-nota[zona de desenvolvimento proximal][a distância entre o que a criança faz sozinha e o que consegue com ajuda de alguém mais capaz] (ZDP)#h(0pt) — a distância entre o que a criança já faz sozinha e o que ela consegue fazer com a ajuda de um adulto ou de um colega mais capaz. É nessa faixa, com mediação pela linguagem, que o aprendizado efetivamente ocorre.

#table(
  columns: (10em, 1fr),
  inset: 7pt,
  align: left + horizon,
  stroke: 0.5pt + gray-border,
  fill: (_, row) => if row == 0 { navy } else { white },
  table.header(
    text(fill: white, weight: "bold", font: titulo-fam)[Teoria (autor)],
    text(fill: white, weight: "bold", font: titulo-fam)[O que a lente enxerga],
  ),
  [*Cognitiva* — Piaget], [A criança constrói o conhecimento em estágios; o pensamento muda de forma, não só de tamanho.],
  [*Psicossocial* — Erikson], [Cada fase resolve uma crise; o vínculo com o cuidador gera a confiança básica.],
  [*Ecológica* — Bronfenbrenner], [O desenvolvimento mora em sistemas encaixados: da família à cultura ao tempo histórico.],
  [*Sociocultural* — Vygotsky], [Aprende-se na interação social, dentro da zona de desenvolvimento proximal, mediado pela linguagem.],
)

#figura-nebli("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-03.png",
  largura: 62%,
  legenda: [Piaget descreve *como* a criança pensa em cada idade; Erikson, *qual conflito emocional* ela resolve. As duas lentes correm em paralelo na mesma criança.])

#subtopico("1.3 — O que é desenvolvimento, afinal — e em quantas frentes ele corre")

Reunindo as lentes, chega-se à definição operacional que a #sigla("SBP", [Sociedade Brasileira de Pediatria]) adota e que orienta a prática: desenvolvimento é um processo que começa na concepção e envolve a maturação em várias frentes — neurológica, comportamental, cognitiva, social e afetiva —, tendo como produto tornar a criança *competente* para responder às próprias necessidades e às do meio, considerando o contexto em que vive. Duas coisas nessa frase merecem peso. Começar "na concepção" já avisa que o período intrauterino conta. E terminar em "competência considerando o contexto" avisa que não existe desenvolvimento no vácuo — ele é sempre desenvolvimento *para* um ambiente.

Justamente por correr em várias frentes ao mesmo tempo, a #sigla("OMS", [Organização Mundial da Saúde]) organiza o desenvolvimento em domínios, e conhecê-los é o que permite ao pediatra não olhar só para "a criança anda?". São eles o motor (grosso, dos grandes músculos, e fino, da pinça e do traço), a linguagem (compreender e se expressar), a cognição (adquirir conhecimento, memória, resolver problemas), as funções executivas (memória de trabalho, foco, autorregulação, flexibilidade mental), o temperamento (como a criança sente e expressa emoções), o socioemocional (regular as respostas emocionais na interação) e as habilidades adaptativas (dar conta das tarefas do dia a dia). O aluno leva daqui uma disposição de olhar: uma criança pode ir bem no motor e mal na linguagem — e é o mapa dos domínios que impede que um atraso passe despercebido só porque outra frente vai bem.

#figura-nebli("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-06.png",
  largura: 66%,
  legenda: [Os domínios do desenvolvimento (OMS). Avaliar "o desenvolvimento" é avaliar todas essas frentes — não apenas a motora, que é a mais visível.])

#mini-resumo[Desenvolver é ganhar função porque uma estrutura amadureceu. Quatro lentes complementares (Piaget/cognição, Erikson/vínculo, Bronfenbrenner/contexto, Vygotsky/interação) descrevem esse ganho, que a OMS organiza em domínios — motor, linguagem, cognição, funções executivas, temperamento, socioemocional e adaptativo.]

#parte-title("PARTE II — O motor biológico: cérebro plástico e a janela dos primeiros anos")

#subtopico("2.1 — Habilidades se constroem em camadas")

O Center on the Developing Child, de Harvard, resumiu numa imagem o que há de mais importante nesta parte: a criança adquire habilidades como se constrói uma casa. As habilidades iniciais são as fundações; sobre elas se assentam habilidades mais complexas, andar por andar, em ordem crescente de sofisticação. A consequência é direta e severa: fundações sólidas permitem o desenvolvimento pleno, enquanto fundações frágeis limitam tudo o que se tentar construir por cima. Um atraso de linguagem aos dois anos não fica confinado à linguagem — ele empobrece o tijolo sobre o qual viriam a leitura, o raciocínio verbal e a vida escolar. É por isso que os primeiros anos pesam tanto: não porque o que se aprende neles seja "mais importante" em si, mas porque é *base* de todo o resto.

#figura-nebli("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-07.png",
  largura: 56%,
  legenda: [A habilidade nova se apoia nas anteriores. Fundação frágil não derruba só um andar — encolhe todos os que viriam acima.])

#subtopico("2.2 — Plasticidade: como o cérebro se esculpe pela experiência")

Sob a metáfora da casa há biologia concreta, e ela é o coração deste resumo. O #termo-nota[neurônio][a célula do sistema nervoso que conduz e transmite sinais] passa sinais a outros neurônios pelas #termo-nota[sinapses][pontos de contato onde um neurônio transmite sinal a outro], os pontos de contato entre células. Nos primeiros anos, o cérebro faz essas conexões numa velocidade que nunca mais repetirá: o número de sinapses aumenta de forma explosiva logo após o nascimento — é a #termo-nota[sinaptogênese][formação de novas sinapses, intensíssima nos primeiros anos de vida]. O bebê produz sinapses em enorme excesso, muito além do que usará. Aos dois anos, o cérebro já desenvolveu cerca de 80% da capacidade que terá.

O detalhe decisivo é o que acontece com esse excesso. As conexões que são usadas — porque a experiência as ativa repetidamente — se fortalecem e permanecem; as que ficam ociosas são eliminadas, num processo de #termo-nota[poda sináptica][eliminação das sinapses pouco usadas, refinando os circuitos conforme a experiência]. É a experiência, portanto, que decide quais circuitos ficam de pé. Em paralelo, os axônios vão sendo revestidos de #termo-nota[mielina][bainha lipídica que envolve o axônio e acelera muito a condução do sinal], a bainha que acelera a transmissão — a #termo-nota[mielinização][revestimento progressivo dos axônios por mielina, que continua por anos e amadurece por último no córtex pré-frontal] avança por regiões, terminando por último no córtex pré-frontal, sede do planejamento e do autocontrole. O resultado dessa tríade — produzir em excesso, podar pelo uso, mielinizar — é um cérebro que se especializa no ambiente concreto em que vive.

Esses períodos de altíssima #termo-nota[plasticidade][a capacidade do cérebro de mudar sua estrutura e função em resposta à experiência] são as chamadas *janelas de oportunidade*, ou #termo-nota[período crítico][fase em que um circuito precisa de um certo estímulo para se formar bem; fora dela, o ganho fica muito mais difícil]. Em certas funções, se o estímulo esperado não chega dentro da janela, o circuito se forma mal e recuperar depois é muito mais custoso — o exemplo clássico é o da visão: um olho privado de imagem nítida nos primeiros anos perde permanentemente parte da acuidade, ainda que o olho em si seja perfeito, porque o córtex visual não recebeu o estímulo na hora de se organizar. Em outras funções, a janela é mais frouxa (um *período sensível*), em que o aprendizado é mais fácil dentro dela mas ainda possível depois. Fica a distinção que sustenta metade da clínica do desenvolvimento: *a janela não fecha a porta para sempre, mas o preço de entrar atrasado sobe rápido*.

#figura-nebli("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-10.png",
  largura: 72%,
  legenda: [A densidade de conexões dispara do recém-nascido aos 2 anos e depois é refinada pela poda. Não é o número de neurônios que a experiência mais muda — é a floresta de sinapses entre eles.])

#confusao-prevista(
  titulo: "A experiência não faz mais neurônios — faz (e desfaz) conexões",
  aluno_acha: [o aluno tende a achar que estimular a criança "cria mais neurônios", como se o ganho fosse de células],
  mecanismo: [o que a experiência mais esculpe são as *sinapses*: fortalece as usadas e poda as ociosas. O número de neurônios muda pouco; o que floresce ou murcha é a rede de conexões entre eles. Por isso privação e estímulo se inscrevem tão fundo — eles editam o cabeamento, não a contagem de peças.],
)

#subtopico("2.3 — O espectro da normalidade: mesma ordem, ritmos diferentes")

Reunindo a maturação da PARTE I com a plasticidade que acabamos de ver, chega-se a um fato que confunde muita gente na prática: a *sequência* de aquisição das habilidades é notavelmente ordenada e parecida entre as crianças — em regra, senta antes de andar, balbucia antes de falar, rabisca antes de escrever —, mas a *velocidade* com que cada uma percorre essa sequência varia muito, e varia dentro da normalidade. Duas crianças saudáveis podem andar com meses de diferença. O que explica essa variação é a interação entre gene e ambiente: o mesmo programa de fundo, rodando em contextos diferentes, produz ritmos diferentes. Separar essas duas dimensões — a ordem, que é conservada, e o ritmo, que é elástico — é o que impede o pediatra de confundir uma variação normal de ritmo com um atraso verdadeiro, e vice-versa.

#figura-nebli("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-13.png",
  largura: 60%,
  legenda: [A trajetória se lê em janelas (nascimento, 6, 12, 36, 72 meses). A sequência das aquisições é a mesma; onde cada criança está dentro da janela é que varia.])

Vale tornar essa sequência concreta, porque é dela que sai a régua prática do pediatra. Os marcos abaixo são os pontos de referência mais usados — não para decorar idade exata, mas para reconhecer a *ordem* e perceber quando uma criança se distancia demais da janela esperada. Repare como cada linha reúne as quatro frentes (motor grosso, motor fino, linguagem e social) amadurecendo em paralelo.

#table(
  columns: (5em, 1fr, 1fr, 1fr),
  inset: 6pt,
  align: left + horizon,
  stroke: 0.5pt + gray-border,
  fill: (_, row) => if row == 0 { navy } else { white },
  table.header(
    text(fill: white, weight: "bold", font: titulo-fam)[Idade],
    text(fill: white, weight: "bold", font: titulo-fam)[Motor],
    text(fill: white, weight: "bold", font: titulo-fam)[Linguagem],
    text(fill: white, weight: "bold", font: titulo-fam)[Social / cognitivo],
  ),
  [*2 meses*], [Sustenta a cabeça em prono], [Emite sons (arrulha)], [Sorriso social],
  [*6 meses*], [Senta com apoio; transfere objeto de mão em mão], [Balbucia], [Leva objetos à boca; explora],
  [*9 meses*], [Senta sem apoio; preensão em pinça grosseira], [Duplica sílabas ("dadada")], [Permanência do objeto; estranha desconhecidos],
  [*12 meses*], [Primeiros passos; pinça fina], ["mamã/papá" com sentido], [Aponta; brinca junto do adulto],
  [*18 meses*], [Anda com firmeza; rabisca], [~10 palavras; aponta partes do corpo], [Come sozinho com os dedos],
  [*2 anos*], [Corre; sobe escada; torre de 6 cubos], [Frases de 2 palavras], [Brincar paralelo (ao lado, não com)],
  [*3 anos*], [Triciclo; copia um círculo], [Frases de 3 palavras; ~75% inteligível], [Usa garfo; brincadeira de faz de conta],
)

Duas leituras clínicas saltam da tabela. A permanência do objeto, aos 9 meses, é o marco de Piaget virando comportamento observável — e vem junto do estranhamento, porque guardar a imagem do cuidador implica reconhecer quem não é ele. E o *brincar paralelo* dos 2 anos (brincar ao lado de outra criança, não ainda com ela) é o lembrete de que o social também tem sequência: a cooperação genuína vem só depois. Um sinal de alerta não é "chegar atrasado a um marco", e sim *estagnar* ou *regredir* — perder uma habilidade já conquistada é o que mais preocupa.

#subtopico("2.4 — A tríade gene × ambiente × experiência")

O ponto de quebra desta parte é entender que "genético" e "ambiental" não são times rivais disputando a criança — são camadas que operam juntas, cada uma no seu papel. Harvard organiza essa cooperação em três termos. A *genética* fornece o *plano* da arquitetura cerebral: a planta baixa, as regras gerais de como o cérebro se monta. O *ambiente* — a nutrição, os estímulos, o afeto, mas também as toxinas e as privações — *modula o quanto e como* esse plano genético consegue se expressar, e tem influência profunda sobre a arquitetura inicial. E as *experiências* concretas, repetidas, *moldam os circuitos* de modo a adaptar a criança ao ambiente específico em que ela vive.

A ponte molecular entre o ambiente e o gene tem nome: #termo-nota[epigenética][marcas químicas que ligam e desligam genes sem alterar a sequência do DNA; é por elas que o ambiente regula o genoma]. São marcas químicas depositadas sobre o DNA — sem trocar uma única letra da sequência — que ligam e desligam genes, ajustando o quanto cada um é lido. É por esse mecanismo que uma experiência precoce, boa ou má, consegue deixar uma marca duradoura na forma como o genoma funciona: o ambiente não reescreve o DNA, mas regula que partes dele serão usadas. A marca química mais estudada é a #termo-nota[metilação do DNA][adição de grupos metil ao DNA que, em geral, silencia o gene marcado — uma das principais assinaturas epigenéticas]: grupos metil depositados sobre um gene tendem a silenciá-lo. Em modelos animais, o próprio cuidado materno regula, por metilação, o gene do receptor que desliga a resposta ao estresse — filhotes bem cuidados ficam com esse "freio" mais ativo e reagem melhor à adversidade a vida toda. Cuidado responsivo e adversidade crônica, ambos, deixam assinaturas epigenéticas — e é aí que a biografia começa a virar biologia.

#figura-nebli("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-12.png",
  largura: 62%,
  legenda: [Três camadas cooperando: o gene dá o plano, o ambiente modula a expressão, a experiência esculpe o circuito. A epigenética é o mecanismo que costura o ambiente ao genoma.])

#mini-resumo[O cérebro produz sinapses em excesso, poda pelo uso e mieliniza — por isso a experiência, não a contagem de neurônios, esculpe a arquitetura, dentro de janelas de plasticidade. A sequência das aquisições é universal; o ritmo é elástico. Gene (plano), ambiente (modulação) e experiência (esculpe) cooperam, com a epigenética ligando ambiente a genoma.]

#parte-title("PARTE III — Quando o ambiente esculpe: risco, estresse tóxico e o papel do pediatra")

#subtopico("3.1 — Fatores de risco: quando o ambiente empobrece a construção")

Se a arquitetura cerebral se ergue sobre a experiência, então adversidades no ambiente são, literalmente, adversidades na construção. Chamam-se *fatores de risco* as situações que podem comprometer o desenvolvimento saudável e empurrar a criança para uma situação de vulnerabilidade futura. Na primeira infância, os principais são a má nutrição, as doenças infecciosas de repetição, o abuso físico e verbal, a violência na comunidade, a negligência, a falta de estimulação, a #termo-nota[depressão materna][quadro que reduz a disponibilidade emocional da mãe, tornando as interações com o bebê menos sensíveis e mais negativas] e a pobreza. A depressão materna merece destaque mecânico: uma mãe deprimida tende a ser menos sensível e menos envolvida, com interações mais negativas — e como veremos, é justamente a interação responsiva que protege o cérebro do estresse. O risco, aqui, não é um azar abstrato: ele age subtraindo os estímulos e o afeto de que a construção cerebral depende.

O caso do vocabulário torna isso concreto. Um estudo clássico mostrou que diferenças no vocabulário das crianças já aparecem por volta dos 18 meses; aos 3 anos, filhos de pais com maior escolaridade apresentavam um vocabulário duas a três vezes mais variado do que os de menor escolaridade — e chegavam à escola com atraso de linguagem se não fossem inseridos num ambiente rico em estímulo verbal. A mensagem não é sobre "genética da inteligência": é sobre quantas palavras, quantas trocas, quantas interações banharam aquele cérebro na janela em que ele mais precisava delas.

#figura-lateral("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-17.png",
  lado: "right",
  largura-figura: 40%,
  texto: [O ambiente linguístico pobre não "espera" para cobrar: a diferença de vocabulário já é medível aos 18 meses e se amplia até a escola. É a plasticidade funcionando contra a criança — o circuito da linguagem se especializa no pouco que recebeu.],
  legenda: [Vocabulário aos 3 anos por escolaridade dos pais (Hart & Risley).])

#subtopico("3.2 — A taxonomia do estresse e o eixo hormonal por trás dela")

Nem todo estresse faz mal — e entender por quê é o mecanismo mais importante desta parte. Diante de uma ameaça, o cérebro dispara uma cascata hormonal: o hipotálamo aciona a hipófise, que aciona a suprarrenal, que libera #termo-nota[cortisol][o principal hormônio do estresse, liberado pela suprarrenal; útil em picos breves, danoso quando cronicamente elevado] — o eixo #sigla("HPA", [hipotálamo-hipófise-adrenal — a cascata hormonal que termina na liberação de cortisol pela suprarrenal]). O cortisol mobiliza o corpo para reagir. Em picos breves, isso é saudável e até necessário. O que decide se a resposta constrói ou destrói é a *duração* da ativação e, sobretudo, a presença de um adulto que a amorteça. O Child Development National Scientific Council descreveu três tipos de resposta ao estresse exatamente nesse eixo.

O *estresse positivo* é uma resposta breve e de intensidade leve a moderada — a ansiedade de tomar uma vacina, de se integrar na escola, de se recuperar de um susto. Com um adulto atencioso por perto, o eixo HPA sobe e volta rápido ao normal, e a criança pratica respostas saudáveis à adversidade: é elemento *promotor* do desenvolvimento. O *estresse tolerável* vem de eventos mais pesados — a morte de um familiar, um acidente grave, uma crise séria. A magnitude é maior, mas, de novo, a proteção de adultos responsivos impede que a ativação se torne excessiva e produza dano; o componente essencial continua sendo o relacionamento protetor que facilita o enfrentamento e traz o sistema de volta ao estado inicial.

O *estresse tóxico* é o que ocorre quando a ativação é forte, frequente ou prolongada *e falta o adulto que a amorteça*. Sem esse tampão, o cortisol permanece cronicamente elevado — e níveis persistentemente altos do hormônio do estresse interferem na própria construção da arquitetura cerebral. Além de efeitos de curto prazo, o estresse tóxico precoce pode produzir mudanças mais permanentes na estrutura e na função do cérebro, precursoras de deficiências posteriores de aprendizagem e de comportamento. As regiões mais atingidas são justamente as que o cortisol crônico desgasta: o hipocampo (memória) e o córtex pré-frontal (planejamento e autocontrole) tendem a encolher, enquanto a amígdala, centro do medo, fica hiperativa — o cérebro se recalibra para viver em ameaça constante. Repare no elo causal completo: adversidade sem amortecimento → HPA cronicamente ativado → cortisol alto sustentado → remodelamento do hipocampo, do pré-frontal e da amígdala → déficit de aprendizagem e de autorregulação que se arrasta pela vida.

#atencao-box("O que define o estresse tóxico é a AUSÊNCIA de amortecimento", [
  O erro é classificar o estresse pela gravidade do evento. Não é isso. A morte de um familiar pode ser estresse *tolerável* se houver um adulto responsivo amortecendo; e uma adversidade menor pode virar *tóxica* se a criança a enfrenta sozinha, sem esse tampão. O divisor não é o tamanho do baque — é a presença ou ausência de um relacionamento protetor que devolva o eixo HPA ao repouso. É por isso que o vínculo, e não a eliminação de todo estresse, é o alvo da proteção.
])

#figura-nebli("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-18.png",
  largura: 54%,
  legenda: [Três respostas ao estresse ao longo do mesmo eixo HPA. O que muda entre elas é a duração da ativação e a presença do adulto que amortece — não apenas a gravidade do evento.])

#subtopico("3.3 — A trajetória é mudável — a plasticidade também salva")

O ponto de quebra otimista vem justamente da biologia que assustou no subtópico anterior. A mesma plasticidade que torna o cérebro vulnerável à adversidade é a que permite recuperá-lo: o cérebro tem a capacidade de crescer e mudar, e a primeira infância é o período de maior transformação — logo, a maior oportunidade de intervir. Duas evidências sustentam a esperança. Primeiro, o cérebro é plástico. Segundo, programas e estratégias — programas de parentalidade, ambientes acolhedores alternativos como creche e escola de qualidade — podem alterar a trajetória do desenvolvimento e ajudar a criança a construir e fortalecer habilidades, minimizando o impacto das adversidades externas. A negligência extrema mostra o outro lado desse mesmo espelho: privado do estímulo e do afeto na janela crítica, o cérebro se desenvolve menos — a arquitetura que dependia da experiência simplesmente não foi construída.

#clinica-box("O cérebro da negligência extrema", [
  Imagens de crianças submetidas a negligência extrema nos primeiros anos revelam cérebros menores, com menos substância e ventrículos alargados, comparados aos de crianças criadas em ambientes responsivos. Não é um dano genético: é a plasticidade operando na direção contrária. Sem os estímulos que a experiência deveria fornecer, a sinaptogênese e a poda não tiveram a matéria-prima da vivência para esculpir circuitos ricos, e a arquitetura ficou empobrecida. É a demonstração mais crua de que a experiência precoce não *influencia* o cérebro de fora — ela o *constrói* por dentro. E é também por isso que intervir cedo, ainda dentro da janela, muda o desfecho.
])

#figura-nebli("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-15.png",
  largura: 56%,
  legenda: [Cérebro de criança em desenvolvimento típico (esquerda) e sob negligência extrema (direita). A diferença de tamanho e de substância é a plasticidade privada de experiência — a construção que não aconteceu.])

#subtopico("3.4 — Medir para intervir: vigilância e triagem")

Se a intervenção precoce muda o desfecho, então detectar cedo é parte do tratamento — e a pediatria separa esse cuidado em duas ações que costumam ser confundidas. A *vigilância* (ou monitoramento) é um processo de avaliação *contínuo e permanente*, feito em toda consulta, cuja função é eleger quais crianças merecem um olhar mais fino. A *triagem* (ou screening) é pontual: usa um instrumento padronizado, em consultas específicas, para identificar as crianças em risco de atraso — e essas, sim, devem ser encaminhadas para diagnóstico. A ordem é uma engrenagem: vigia-se sempre, tria-se quando algo chama atenção, encaminha-se para diagnóstico quem a triagem sinaliza. Avaliar durante esse período crítico não é burocracia — é o que permite propor intervenção enquanto a janela de plasticidade ainda está aberta, quando o ganho por unidade de esforço é máximo.

#figura-nebli("/figuras/pediatria-01-desenvolvimento-primeira-infancia/slide-25.png",
  largura: 64%,
  legenda: [Vigilância é contínua (toda consulta); triagem é pontual, com instrumento. Uma alimenta a outra, e a triagem positiva leva ao diagnóstico.])

#subtopico("3.5 — A nova abordagem: ecobiodesenvolvimento e o papel do pediatra")

Juntando as três partes, chega-se ao modelo que reorganiza a pediatria do desenvolvimento — a matriz do #termo-nota[ecobiodesenvolvimento][abordagem que integra ecologia, biologia e desenvolvimento: o ambiente precoce se inscreve na biologia e repercute na saúde adulta]. Ela parte de três teses. As experiências adversas precoces são críticas, porque podem afetar o desenvolvimento saudável; as raízes de muitos problemas de saúde e de desenvolvimento estão na primeira infância; e prevenir as consequências de longo prazo da adversidade é possível, com medidas protetoras nesse período. Aqui o "crescimento" do título reencontra o "desenvolvimento": restrições intrauterinas comprometem o crescimento e o desenvolvimento e produzem consequências tardias na saúde do adulto — por isso a atenção especial ao prematuro e ao pequeno para a idade gestacional, cujas janelas começaram em desvantagem.

Desse modelo decorre um novo papel para o profissional de saúde, formalizado pela #sigla("AAP", [American Academy of Pediatrics — Academia Americana de Pediatria]): entender a origem precoce das doenças e o impacto do estresse tóxico; saber identificar as crianças em maior risco e oferecer suporte; diagnosticar problemas de desenvolvimento com um arsenal de instrumentos; e colaborar na busca de intervenções eficazes que minimizem os efeitos da adversidade precoce. A otimização dos ganhos acontece sobretudo nos dois primeiros anos, e programas de estimulação precoce — como visitas domiciliares — são efetivos, principalmente antes da entrada na creche. O pediatra deixa de ser apenas quem mede peso e altura: passa a ser o vigia de uma janela biológica que não volta a se abrir da mesma forma.

#conclusao-box[
  Um único princípio costura este resumo: *na primeira infância, a experiência não influencia o cérebro de fora — ela o constrói por dentro, dentro de uma janela de plasticidade que não se repete*. O mecanismo nuclear é a tríade sinaptogênese → poda experiência-dependente → mielinização: o cérebro produz conexões em excesso e deixa a vivência decidir quais permanecem, esculpindo a arquitetura no ambiente concreto em que vive. É a mesma plasticidade que, sem o amortecimento de um adulto responsivo, deixa o cortisol do eixo HPA remodelar em prejuízo as regiões que aprendem e se autorregulam — o estresse tóxico — e que, com estímulo e afeto, permite recuperar a trajetória. Na clínica, isso reaparece no cérebro empobrecido da negligência, no prematuro que começou a janela em desvantagem, e na engrenagem vigilância → triagem → diagnóstico que existe para intervir enquanto a janela ainda está aberta. A próxima aula parte exatamente daqui: destrinchar os *determinantes* biológicos, psicológicos e socioculturais que decidem, criança a criança, se essa janela será uma oportunidade ou um risco.
]
