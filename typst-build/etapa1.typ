#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
O granuloma é a resposta do organismo a um problema específico: um agente que a imunidade inata reconhece mas não consegue eliminar. Quando destruir de imediato não é opção, o tecido monta uma estrutura que isola — e essa estrutura tem forma reconhecível ao microscópio, mediadores nomeáveis e um ponto de falha previsível.

A *PARTE I* percorre o problema: o que define um granuloma, e por que o bacilo da tuberculose, o modelo que a aula usa, sobrevive exatamente dentro da célula encarregada de matá-lo. A *PARTE II* monta a estrutura peça por peça — o eixo de citocinas que transforma o macrófago parasitado em macrófago armado, de onde vêm tantos macrófagos, e como eles se organizam em camadas. A *PARTE III* lê o resultado na lâmina e no paciente: as formas da tuberculose, o granuloma que se calcifica, o que acontece quando o eixo falha, e os granulomas em que não há micro-organismo nenhum.
]

#parte-title("PARTE I — O agente que não se destrói", primeira: true)

#subtopico("1.1 — O granuloma como decisão de arquitetura")

Granuloma é um padrão de inflamação crônica em que macrófagos ativados se agregam num foco compacto, assumem morfologia de #termo-nota[célula epitelioide][macrófago ativado com citoplasma eosinofílico abundante e limites celulares indistintos, cujo arranjo em bloco lembra um epitélio] e ficam circundados por uma coroa de linfócitos T. Não é uma célula nem um mediador: é uma *organização espacial* da resposta celular.

Essa organização aparece em duas situações, e as duas têm o mesmo denominador. A primeira é o agente que a imunidade inata não elimina — o micro-organismo que sobrevive dentro do macrófago não ativado, como a micobactéria, ou fungos como o *Paracoccidioides* e o *Histoplasma*, ou parasitas como a leishmânia. A segunda é o material que não se digere: partículas de sílica de jateamento de areia, fibras de asbesto, restos vegetais aspirados, fio cirúrgico não absorvível. Em ambos os casos a fagocitose acontece e não resolve.

Diante de um agente que não sai, o tecido troca de objetivo. Em vez de destruir imediatamente, ele *isola*: concentra macrófagos num ponto, cerca esse ponto de linfócitos e impede que o agente alcance a corrente sanguínea e se dissemine. É um estado de sítio — se o agente escapa do centro, encontra artilharia montada em volta. Destruir, quando acontece, é consequência da concentração local de macrófagos ativados, não a finalidade primária da estrutura.

Essa lógica separa dois tipos de granuloma que a lâmina permite distinguir. O *granuloma imune* é T-dependente: exige que o antígeno seja processado, apresentado a um linfócito CD4 e devolvido ao foco como sinal de ativação. É o granuloma da tuberculose, das micoses profundas e da sarcoidose. O *granuloma de corpo estranho* dispensa esse circuito: o macrófago tenta englobar uma partícula grande demais, falha, e o agregado se monta por frustração fagocítica pura, com coroa linfocitária escassa e sem necrose central. A sílica ocupa um lugar intermediário — partícula inerte, mas imunogênica o bastante para recrutar resposta T.

Do ponto de vista imunológico, o granuloma imune é a expressão morfológica da *hipersensibilidade tardia*, ou hipersensibilidade do tipo IV — a reação mediada por linfócito T e macrófago, sem participação de anticorpo, que leva dias para se instalar porque depende de células que precisam ser geradas. É por isso que a lista de causas inclui doenças imunomediadas sem agente infeccioso identificado, como a sarcoidose e a granulomatose com poliangiite, o quadro descrito historicamente como granulomatose de Wegener.

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-05.png",
  largura: 44%,
  legenda: [O foco rosado central é material necrótico; o halo mais escuro em volta é a soma de macrófagos ativados e linfócitos. O alvéolo aerado ao redor dá a escala: o granuloma é uma lesão focal dentro de um pulmão que continua funcionando.])

#subtopico("1.2 — Por que o bacilo da tuberculose sobrevive dentro do macrófago")

O *Mycobacterium tuberculosis* não evita ser fagocitado: ele se oferece. A explicação está na parede celular, que difere tanto da gram-positiva quanto da gram-negativa. Sobre o peptidoglicano assenta-se uma camada de arabinogalactano, e sobre ela uma camada espessa de #termo-nota[ácido micólico][ácidos graxos de cadeia muito longa, com 60 a 90 carbonos, que formam uma barreira cerosa quase impermeável em torno da micobactéria], recoberta por lipídeos de superfície entre os quais está o #termo-nota[fator corda][trealose-6,6'-dimicolato, glicolipídeo de superfície cujo nome vem do crescimento do bacilo em cordas serpentiformes na cultura]. Atravessando tudo isso, o #sigla("LAM", [lipoarabinomanano — glicolipídeo que atravessa a parede micobacteriana e expõe açúcares na superfície do bacilo]) expõe um capuz de manose.

São esses açúcares que o bacilo usa para ser reconhecido. O *receptor de manose* do macrófago, um dos #sigla("PRR", [receptores de reconhecimento de padrão — sensores inespecíficos que a imunidade inata usa para identificar estruturas moleculares comuns a classes inteiras de micro-organismos]) da imunidade inata, liga o capuz de manose; o receptor de complemento CR3 e receptores do tipo Toll completam a internalização. O bacilo entra porque o interior do macrófago é o lugar mais seguro do organismo para ele: ali dentro, *nem anticorpo nem sistema complemento o alcançam*, e a opsonização que melhoraria a fagocitose deixa de ter alvo.

O passo seguinte é a *subversão da maturação do fagossomo*. No macrófago normal, o fagossomo amadurece trocando os marcadores da sua membrana e passa a poder fundir-se com o lisossomo, formando o fagolisossomo ácido em que as enzimas digestivas trabalham. O bacilo trava essa maturação em vários pontos ao mesmo tempo: exclui a bomba de prótons que acidificaria o compartimento, libera amônia que eleva o pH do fagossomo, e usa uma proteína-quinase própria, a cinase G, para interferir no tráfego de membrana que levaria ao encontro com o lisossomo. *Sem acidificação não há maturação, e sem maturação não há fusão.*

O que resta de defesa também é neutralizado. A destruição de bactérias no fagossomo depende de espécies reativas de oxigênio; o bacilo produz *catalase*, que degrada peróxido de hidrogênio e reduz o estresse oxidativo local. Parte dos bacilos vai além e *escapa do fagossomo para o citosol*, usando um sistema de secreção que perfura a membrana do compartimento.

O fator corda acrescenta uma camada de sabotagem. Ele inibe a migração de leucócitos para o foco, induz produção de fator de necrose tumoral e é citotóxico para o próprio macrófago — efeito que *depende da carga*: à medida que o bacilo se multiplica no citoplasma, o lipídeo acumulado mata a célula hospedeira e libera a nova geração de bacilos. O LAM, em paralelo, inibe a apresentação de antígeno e bloqueia a ativação do macrófago pelo interferon-gama. O bacilo não apenas se esconde; *ele mantém o macrófago inoperante*.

#mini-resumo[O bacilo é fagocitado de propósito, bloqueia a maturação do fagossomo, neutraliza o estresse oxidativo e desarma o macrófago. Enquanto ele está dentro da célula, a imunidade humoral não tem como agir — a saída tem de ser celular.]

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-11.png",
  largura: 48%,
  legenda: [Comparada às paredes gram-positiva e gram-negativa à esquerda, a parede micobacteriana acrescenta arabinogalactano, ácido micólico e lipídeos de superfície. A mesma camada que dá impermeabilidade dá a álcool-ácido resistência da coloração de Ziehl-Neelsen.])

#subtopico("1.3 — Da inata insuficiente ao linfonodo: montando a resposta que faltava")

O bacilo chega ao alvéolo em partículas de aerossol e encontra ali o *macrófago alveolar*, célula residente carregada de receptores de padrão justamente para fazer vigilância local. Parasitado esse macrófago, o bacilo se multiplica no citoplasma por semanas sem oposição efetiva. Há alguma ativação e alguma produção de citocinas inflamatórias, mas insuficientes, porque nesse momento só existe imunidade inata — e *a inata, contra este agente, é o próprio abrigo dele*.

Essa fase de proliferação livre tem uma consequência que reaparece na PARTE III. Bacilos liberados por exocitose ou pela lise do macrófago caem na circulação e semeiam sítios distantes: ápices pulmonares, rins, ossos, meninges. É uma *bacteremia silenciosa*, sem tradução clínica, e os focos que ela deixa ficam contidos quando a resposta celular finalmente chega — *contidos, não eliminados*.

A virada depende de *deslocamento anatômico*. Parte dos macrófagos infectados migra pelo vaso linfático até o *linfonodo de drenagem*, o órgão linfoide secundário onde estão os linfócitos T virgens. Ali, o antígeno micobacteriano processado é apresentado no #sigla("MHC", [complexo principal de histocompatibilidade — conjunto de moléculas de superfície que exibem peptídeos para os linfócitos T; nos humanos, o sistema HLA]) de classe II e reconhecido pelo receptor de célula T de um linfócito #sigla("CD4", [marcador de superfície do linfócito T auxiliar, a célula que coordena a resposta celular e produz o interferon-gama do granuloma]) específico.

O reconhecimento aciona uma sequência que a aula anterior já montou e que aqui só precisa ser retomada. A #sigla("IL-1β", [interleucina-1 beta — citocina inflamatória produzida precocemente pelo macrófago, que participa da ativação do linfócito T CD4]) participa da ativação inicial do CD4; o CD4 ativado passa a produzir #sigla("IL-2", [interleucina-2 — fator de crescimento que o próprio linfócito T ativado secreta e ao qual responde, sustentando a expansão clonal]), que age sobre a própria célula que a produziu num *circuito autócrino* e sustenta a *expansão clonal*. O resultado é um contingente de linfócitos T com receptor específico para aquele antígeno, que cai na circulação e alcança o alvéolo onde o bacilo está.

Duas consequências desse desenho valem ser fixadas. A primeira é *temporal*: como os linfócitos efetores precisam ser gerados, existe uma janela de semanas entre a infecção e a capacidade de responder — é essa janela que explica por que o teste cutâneo de reatividade ao antígeno tuberculínico, que depende de células T de memória, permanece negativo no início. A segunda é *topográfica*: *o linfonodo não é só estação de passagem, é sítio de infecção*. O macrófago que levou o antígeno levou também o bacilo, e por isso a lesão da primo-infecção é um par — foco no pulmão e foco no linfonodo satélite.

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-21.png",
  largura: 50%,
  legenda: [O trajeto completo em uma imagem: o bacilo parasita o macrófago alveolar, o macrófago leva o antígeno ao linfonodo, o CD4 é ativado e prolifera sob estímulo autócrino de IL-2, e os efetores retornam ao alvéolo. O par pulmão-linfonodo é o complexo primário.])

#parte-title("PARTE II — A montagem do granuloma")

#subtopico("2.1 — O eixo IL-12, TH1 e interferon-gama: o macrófago que vira arma")

O linfócito CD4 expandido no linfonodo chega ao alvéolo e reconhece, na superfície do macrófago alveolar, o antígeno micobacteriano apresentado no MHC de classe II. Forma-se a sinapse imunológica, e o macrófago responde produzindo #sigla("IL-12", [interleucina-12 — citocina secretada pelo macrófago que polariza o linfócito T CD4 para o perfil TH1]). É a IL-12 que decide o rumo da resposta: ela liga, dentro do linfócito, o fator de transcrição *T-bet*, proteína que reprograma a célula para transcrever o gene do interferon-gama. O CD4 torna-se um linfócito de perfil TH1.

O #sigla("IFN-γ", [interferon-gama — citocina produzida pelo linfócito TH1; é o principal ativador do macrófago e o mediador central da formação e da manutenção do granuloma]) produzido por essa célula faz duas coisas simultâneas. *Retroalimenta a própria expansão do perfil TH1*, e *ativa o macrófago que apresentou o antígeno*. A direção do circuito precisa ficar clara porque tudo o mais depende dela: quem produz IL-12 é o macrófago, quem produz IFN-γ é o linfócito, e quem é ativado pelo IFN-γ é de volta o macrófago.

#atencao-box("Quem produz o interferon-gama é o linfócito, não o macrófago", [
A inversão mais cara desta aula é atribuir a produção de IFN-γ ao macrófago. O macrófago produz *IL-12*, que polariza o linfócito; o linfócito TH1 produz *IFN-γ*, que ativa o macrófago. A consequência dessa direção é o que explica a doença: sem linfócito CD4 funcionante não há IFN-γ, sem IFN-γ não há macrófago ativado, e sem macrófago ativado não há granuloma. É por isso que o granuloma é uma estrutura que depende do linfócito para existir, embora a célula que executa o trabalho seja o macrófago.
])

O macrófago ativado é uma célula funcionalmente diferente, e *cada ganho dele desfaz um dos mecanismos de escape* descritos em 1.2. A maturação do fagossomo é restaurada e o fagolisossomo se forma; a acidificação volta, e a amônia e a exclusão da bomba de prótons deixam de ser suficientes para impedi-la. A produção de espécies reativas de oxigênio aumenta a ponto de ultrapassar a capacidade da catalase micobacteriana. A sintase induzível de óxido nítrico passa a gerar óxido nítrico e derivados reativos de nitrogênio, tóxicos para o bacilo. A expressão de MHC de classe II sobe, e com ela a capacidade de apresentar antígeno; a produção de IL-12 aumenta, realimentando o eixo. *O macrófago que era abrigo passa a ser executor.*

O macrófago ativado produz também #sigla("TNF", [fator de necrose tumoral — citocina que recruta monócitos para o foco e mantém a coesão arquitetural do granuloma]) e IL-1 em quantidade, e essas citocinas *recrutam novos monócitos* para o alvéolo, onde os linfócitos TH1 presentes os ativam por sua vez. A partir daí o processo se multiplica: muitos macrófagos ativados sob muitos linfócitos TH1, com intensa atividade lítica e destruição do tecido vizinho às células infectadas. O centro dessa área acumula restos celulares, células mortas e fragmentos de bactéria.

Duas funções distintas convém não fundir. O IFN-γ *ativa*; o TNF *mantém a estrutura coesa*. E a estrutura inteira é um circuito de retroalimentação dependente de estímulo: enquanto houver antígeno sendo apresentado, há IFN-γ e há macrófago ativado. Eliminado o agente, a estimulação cessa e a lesão caminha para fibrose e calcificação.

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-25.png",
  largura: 50%,
  legenda: [O CD4 entrega IFN-γ ao macrófago e o converte em macrófago ativado; IFN-γ e TNF-α puxam monócitos do sangue, que se diferenciam em macrófagos no tecido. O granuloma cresce por conversão e por afluxo ao mesmo tempo.])

#clinica-box("Quando o eixo falha: HIV e bloqueio do TNF", [
A infecção pelo #sigla("HIV", [vírus da imunodeficiência humana — infecta e destrói progressivamente os linfócitos T CD4]) destrói progressivamente os linfócitos T CD4. Com poucos CD4, não há contingente suficiente chegando ao alvéolo para reconhecer o antígeno e entregar IFN-γ, o macrófago não é adequadamente ativado, e o granuloma se forma mal — coroa linfocitária rala, contenção insuficiente, tendência à disseminação. O organismo compensa com resposta de padrão neutrofílico, que é ineficaz contra o bacilo intracelular e produz muito dano tecidual. É esse mecanismo que explica o aumento de casos de tuberculose observado a partir dos anos 1980, inclusive em regiões de baixa incidência prévia.

*O mesmo fenótipo aparece por outras portas.* Defeitos genéticos do receptor de IFN-γ ou do receptor de IL-12 produzem suscetibilidade a micobactérias com granulomas mal formados, mesmo sem qualquer imunossupressão adquirida. E o bloqueio farmacológico do TNF, usado em doenças inflamatórias crônicas, desorganiza granulomas já constituídos e reativa focos latentes — porque retira exatamente a citocina que mantinha a estrutura coesa.
])

#subtopico("2.2 — De dois macrófagos alveolares a uma paliçada")

Um alvéolo normal tem poucos macrófagos residentes; *um granuloma é forrado deles*. Explicar essa diferença numérica exige olhar de onde vem a linhagem e por quais três mecanismos ela se acumula.

O macrófago origina-se de um precursor da medula óssea, o *monoblasto*, que dá o *monócito* circulante; recrutado para o tecido, o monócito se diferencia em macrófago. Muitos permanecem como residentes especializados e recebem nomes próprios conforme o órgão — célula de Kupffer no fígado, micróglia no sistema nervoso central, macrófago alveolar no pulmão, osteoclasto no osso. São todos da mesma *linhagem mononuclear fagocitária*, com funções locais distintas: o osteoclasto reabsorve osso, o macrófago alveolar faz vigilância com um repertório amplo de receptores de padrão. Parte importante dessas populações residentes tem origem embrionária e se automantém no tecido, mas na inflamação estabelecida o reforço vem do sangue.

O acúmulo no foco depende de três alavancas, e nenhuma delas isolada dá conta. A primeira é *recrutamento*: as frações C3a e C5a do complemento, a quimiocina MCP-1, o TNF e a IL-1 produzidos no foco atraem monócitos circulantes. A segunda é *proliferação local* — o macrófago maduro em geral não se divide, mas sob estímulo de citocinas do próprio foco, o IFN-γ entre elas, ele volta a proliferar; é comportamento excepcional, e é justamente por isso que chama atenção. A terceira é *retenção*, mediada pelo #sigla("MIF", [fator inibidor da migração de macrófagos — citocina que impede a saída do macrófago do foco inflamatório, retendo-o no tecido]): o padrão normal do macrófago é levar o antígeno ao linfonodo, e o MIF cancela essa saída, mantendo no alvéolo a população que acabou de ser recrutada e ativada.

A ativação também *muda a célula por dentro*, e a mudança é visível. O volume citoplasmático aumenta, o número de lisossomos, de ribossomos e de vacúolos aumenta, o metabolismo sobe, a capacidade fagocítica sobe. O núcleo, ao contrário do que a intuição sugere, *tende a diminuir e a cromatina fica frouxa* — retrato de célula transcrevendo intensamente. E o macrófago ativado secreta um arsenal: elastases e colagenases que remodelam a matriz, fatores que ativam complemento e coagulação, espécies reativas de oxigênio, citocinas, quimiocinas e fatores de crescimento.

#mini-resumo[Recrutar, proliferar e reter. É a soma das três, e não o afluxo sozinho, que transforma dois ou três macrófagos alveolares na paliçada compacta que define o granuloma.]

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-29.png",
  largura: 52%,
  legenda: [Da medula ao tecido: monoblasto, monócito circulante e macrófago residente, com os nomes que a linhagem recebe em cada órgão. À direita, a mesma célula ativada — citoplasma repleto de organelas e cromatina frouxa.])

#subtopico("2.3 — A arquitetura pronta: epitelioide, célula gigante, coroa e centro")

O granuloma maduro lê-se de dentro para fora, em *três camadas*. No centro fica a área de exsudação: restos celulares, células mortas e fragmentos de bactéria acumulados pela destruição tecidual intensa. Em torno dele dispõem-se os macrófagos ativados transformados em células epitelioides, arranjados de forma compacta e por vezes descritos como paliçada. E fechando o conjunto vem a coroa periférica de linfócitos, com predomínio de CD4 sobre #sigla("CD8", [marcador de superfície do linfócito T citotóxico, capaz de destruir células que exibem antígeno em MHC de classe I]).

A célula epitelioide é um macrófago que trocou de ofício. O citoplasma cresce e fica eosinofílico, os limites entre células ficam indistintos, e o conjunto adquire semelhança com epitélio — daí o nome, que descreve aparência e não origem. A troca funcional é o ponto: a célula epitelioide *perde parte da capacidade de englobar e ganha capacidade de secretar*. Ela é mais fábrica de mediadores do que fagócito.

Algumas dessas células se fundem, ou dividem o núcleo sem completar a divisão do citoplasma, e formam a *célula gigante multinucleada de Langhans*, com os núcleos dispostos em ferradura na periferia do citoplasma. A fusão tem finalidade mecânica: um único macrófago não dá conta de um agente muito maior que ele, como uma fibra de asbesto, e o sincício aumenta a superfície disponível para envolvê-lo. Em granulomas de corpo estranho a mesma fusão ocorre, mas os núcleos ficam desordenados no centro da célula, e essa diferença de arranjo é reconhecível na lâmina.

#confusao-prevista(
  titulo: "Célula de Langhans não é célula de Langerhans",
  aluno_acha: [os nomes soam iguais e o aluno os usa como sinônimos],
  mecanismo: [a célula gigante de *Langhans* é multinucleada, deriva da fusão de células epitelioides e vive no granuloma; a célula de *Langerhans* é uma célula dendrítica apresentadora de antígeno da epiderme, mononucleada, que pertence a outro capítulo inteiro. Homofonia, origens opostas.],
)

*O linfócito da coroa não é decorativo.* É ele que produz o IFN-γ que mantém os macrófagos ativados, e sem esse suprimento contínuo a estrutura se desfaz. O CD8 acrescenta um segundo mecanismo efetor: reconhece antígeno micobacteriano apresentado em MHC de classe I pelo macrófago ainda parasitado e não plenamente ativado, e o destrói por citotoxicidade — solução para a célula que não conseguiu resolver o problema por dentro.

O granuloma é, afinal, *inflamação crônica organizada*. A inflamação crônica define-se pela tríade *destruição tecidual, infiltrado de células mononucleares e fibrose*; o granuloma tem as três, dispostas em camadas. A fibrose entra pela mesma via de qualquer processo crônico: macrófagos em perfil reparador, sob estímulo de IL-4, secretam #sigla("TGF-β", [fator de transformação do crescimento beta — citocina que estimula proliferação de fibroblastos e síntese de colágeno]), que faz o fibroblasto proliferar e produzir colágeno. Ela costuma aparecer na periferia do granuloma e pode ocupar o centro quando o agente já foi eliminado e resta cicatrizar.

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-27.png",
  largura: 62%,
  legenda: [As camadas nomeadas: centro de exsudação ou caseificação, células epitelioides em paliçada, célula gigante de Langhans, rima periférica de linfócitos com predomínio de CD4, e fibroblastos depositando colágeno nas fases avançadas. À direita, o mesmo arranjo na coloração de rotina.])

#parte-title("PARTE III — O granuloma na lâmina e no paciente")

#subtopico("3.1 — Ler o granuloma: caseoso, duro, antigo")

Nem todo granuloma tem centro necrótico, e confundir as duas coisas custa caro. O granuloma com #termo-nota[necrose caseosa][necrose de coagulação com liquefação incompleta, de aspecto branco-amarelado e consistência friável semelhante à de queijo, característica da tuberculose] central é o padrão da tuberculose e de algumas micoses profundas. Sarcoidose, silicose e reação a corpo estranho produzem granulomas *não caseosos*, chamados granulomas duros, formados essencialmente por células epitelioides e coroa linfocitária.

A explicação para a diferença está *no que sobra da destruição*. Onde a resposta macrofágica é intensa e o agente é rico em lipídeo, os restos celulares se acumulam com o material da própria parede micobacteriana, e o produto não é nem líquido nem sólido: é friável, macio, de aspecto de queijo — daí caseosa. Onde o agente é uma partícula inerte que não se destrói e não desencadeia lise maciça, não há material necrótico suficiente para formar centro, e o granuloma fica compacto.

O tempo também *deixa marcas legíveis*. Um granuloma antigo mostra fibrose espessa na periferia, todo colágeno, e frequentemente #termo-nota[calcificação distrófica][deposição de sais de cálcio em tecido previamente lesado, com concentração sérica de cálcio normal — distinta da calcificação metastática, que depende de hipercalcemia] no centro necrótico. Costuma mostrar também antracose: o macrófago do foco fagocita tudo o que chega, e as partículas de carbono inaladas se acumulam nele ao longo do tempo. Antracose abundante não indica poeira de carvão como causa do granuloma — *indica que aquele granuloma é velho*.

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-43.png",
  largura: 50%,
  legenda: [Granuloma antigo: anel externo de fibrose densa, centro de necrose caseosa com restos celulares e calcificação, coroa fina de linfócitos e pigmento antracótico acumulado. Cada achado data a lesão.])

Para identificar o agente, a lâmina de rotina não basta. A coloração de Ziehl-Neelsen busca o *bacilo álcool-ácido resistente*, e a propriedade que dá esse nome vem do ácido micólico da parede: ele retém a fucsina mesmo depois da lavagem com álcool-ácido, e o bacilo aparece em vermelho contra o fundo azulado. Para granulomas de causa fúngica, colorações específicas para parede de fungo cumprem papel equivalente.

#figura-lateral("/figuras/pat-08-inflamacao-granulomatosa/slide-45.png",
  lado: "right",
  largura-figura: 36%,
  texto: [Encontrar o bacilo confirma a etiologia e localiza o agente na cena. Na imagem ao lado, bastonetes vermelhos aparecem tanto no citoplasma de macrófagos quanto livres entre as células, retrato exato da alternância entre parasitismo intracelular e liberação após lise que a PARTE I descreveu. A escassez de bacilos numa lesão bem controlada é esperada: onde a ativação macrofágica funcionou, sobram poucos.],
  legenda: [Ziehl-Neelsen.])

#subtopico("3.2 — Tuberculose: primária, secundária e miliar")

Na primo-infecção, o indivíduo sem contato prévio inala o bacilo, desenvolve a resposta celular descrita na PARTE II e forma granulomas em dois lugares: no parênquima pulmonar e no linfonodo hilar satélite, para onde o macrófago levou o antígeno. Esse par é o *complexo primário tuberculoso*, ou complexo de Ghon. Com resposta T competente, o processo é contido; a necrose central calcifica por calcificação distrófica, e o resultado aparece anos depois em uma radiografia de rotina como duas opacidades — um nódulo calcificado na periferia do pulmão e um linfonodo hilar calcificado. A leitura correta desse achado é lesão antiga e resolvida, não doença em atividade. A infecção latente é frequente na população, o que torna esse achado incidental comum.

*Latente não significa estéril.* Bacilos viáveis podem permanecer contidos dentro da lesão fibrocalcificada, em equilíbrio com uma resposta imune organizada que os impede de sair. Esse equilíbrio se rompe de duas maneiras: nova exposição com carga bacilar muito acima da capacidade de contenção, ou queda da imunidade celular — a mesma falha do eixo CD4–IFN-γ discutida em 2.1.

Rompido o equilíbrio, instala-se a *tuberculose secundária*, ou pós-primária. Sem ativação macrofágica adequada, o bacilo prolifera, a lesão cresce e a necrose caseosa central liquefaz e drena por um brônquio, deixando no lugar uma cavidade de paredes revestidas por reação granulomatosa. A localização preferencial é apical, onde a tensão de oxigênio é mais alta e a drenagem linfática menos eficiente — condições que favorecem um bacilo aeróbio estrito. A cavidade tem consequência epidemiológica direta: comunicada com a via aérea, ela despeja bacilos no escarro, e é o paciente cavitário que transmite.

#clinica-box("Por que a caverna é o problema de saúde pública", [
A cavitação reúne três coisas ao mesmo tempo. Primeiro, é a maior carga bacilar da doença: o interior da caverna é bem oxigenado e o bacilo se multiplica ali em quantidade que nenhuma outra forma alcança. Segundo, ela comunica-se com um brônquio, de modo que cada acesso de tosse aerossoliza material infectante. Terceiro, ela representa destruição irreversível de parênquima — mesmo curada a infecção, resta uma cavidade fibrosada e perda funcional definitiva.

O paradoxo vale ser notado: *boa parte da destruição não é obra do bacilo, e sim da própria resposta*. Onde a resposta é exagerada com carga bacilar alta, ou onde a imunidade celular falhou e sobrou resposta neutrofílica, o dano tecidual é maior. O granuloma bem formado, com poucos bacilos e contenção eficaz, é a apresentação que menos destrói.
])

Quando a contenção falha e o bacilo alcança a corrente sanguínea, surge a *tuberculose miliar*. A disseminação hematogênica leva o agente a outras áreas do pulmão, ao fígado, ao baço e potencialmente a qualquer órgão — sempre há macrófago residente disponível como célula de infecção. Em cada sítio forma-se um granuloma pequeno, e o resultado macroscópico são incontáveis nódulos de 1 a 2 mm distribuídos difusamente. O nome vem do *milium*, o grão de painço, pela semelhança de tamanho e distribuição. Microscopicamente, cada um daqueles pontos é uma tentativa individual de contenção.

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-53.png",
  largura: 36%,
  legenda: [Tuberculose secundária: o corte do pulmão mostra cavidades múltiplas escavadas no parênquima, delimitadas por parede espessa de reação granulomatosa.])

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-55.png",
  largura: 50%,
  legenda: [Tuberculose miliar. Da esquerda para a direita: o padrão micronodular difuso na radiografia, a peça pulmonar semeada de nódulos e a espiga de painço que deu nome ao padrão.])

#subtopico("3.3 — Granuloma sem bacilo: corpo estranho e sarcoidose")

A sílica mostra que *o mecanismo do granuloma não depende de micro-organismo*. O trabalhador exposto ao jateamento de areia inala partículas microscópicas que o macrófago fagocita e não consegue digerir; a partícula rompe a membrana do lisossomo, o macrófago responde com produção sustentada de citocinas inflamatórias, e o resultado é ativação de resposta T e formação de granuloma por caminho praticamente igual ao da micobactéria. A diferença está no desfecho: como a sílica é *inerte*, *nem o macrófago ativado a destrói*. Sem destruição maciça não há necrose central, e o granuloma silicótico é duro — células epitelioides e rima de linfócitos, com fibrose progressiva porque o estímulo nunca cessa. A sericita, usada em indústria, comporta-se do mesmo modo, e sua partícula é birrefringente à microscopia de luz polarizada.

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-57.png",
  largura: 46%,
  legenda: [Silicose: a exposição ocupacional à esquerda e o granuloma duro que ela produz, compacto e sem necrose central, evoluindo para nódulo fibroso.])

O asbesto muda a *escala* do problema. A fibra é longa demais para um macrófago só, e a resposta mobiliza células gigantes que tentam envolvê-la; a fibra recoberta por proteína e ferro forma o #termo-nota[corpúsculo ferruginoso][fibra de asbesto revestida por material proteináceo e ferro, com aspecto de haltere acastanhado, identificável na lâmina como marcador de exposição]. Além do granuloma, a exposição ao asbesto associa-se ao mesotelioma pleural, o que motivou sua proibição.

O mesmo princípio explica granulomas *sem qualquer relação com poeira*. Material vegetal broncoaspirado permanece no pulmão porque não existe enzima humana capaz de digerir celulose de modo eficiente, e o tecido responde isolando-o com células gigantes. Fio cirúrgico não absorvível deixado na pele produz reação idêntica — e é essa a razão de se retirarem os pontos após sete a dez dias, prazo em que a aproximação da ferida já cumpriu seu papel. Nesses casos há hiperativação imune local sem necrose central, e as células gigantes exibem núcleos desordenados, não em ferradura.

#figura-lateral("/figuras/pat-08-inflamacao-granulomatosa/slide-69.png",
  lado: "left",
  largura-figura: 34%,
  texto: [Os filamentos claros seccionados no centro da imagem são um fio de sutura multifilamentado, composto por microfilamentos trançados, retido na derme. Em volta deles organizou-se um granuloma de corpo estranho: células epitelioides e gigantes tentando englobar um material que não é degradável, com linfócitos escassos na periferia. É a mesma arquitetura da tuberculose montada por um caminho independente de linfócito T.],
  legenda: [Granuloma a fio cirúrgico.])

A sarcoidose fecha o espectro *pelo outro extremo*. Nela há ativação de resposta imune celular com formação de granulomas não caseosos *sem que se identifique antígeno ou agente* — a hipótese em disputa é uma reação contra antígenos próprios que, em vez de gerar anticorpos, produz resposta celular com polarização TH1. O granuloma é tipicamente duro, com lesão central pequena ou ausente em relação à espessura do halo epitelioide. Algumas células gigantes contêm o #termo-nota[corpo asteroide][inclusão proteica estrelada no citoplasma de células gigantes multinucleadas, de origem incerta, bastante específica da sarcoidose e de baixa sensibilidade], achado bastante específico e de sensibilidade baixa: quando aparece, contribui muito para o diagnóstico; quando não aparece, não afasta nada.

#figura-nebli("/figuras/pat-08-inflamacao-granulomatosa/slide-63.png",
  largura: 40%,
  legenda: [Granuloma sarcoídico não caseoso. No centro da célula gigante, a inclusão estrelada é o corpo asteroide.])

#conclusao-box[
Um princípio organiza a aula inteira: quando o organismo não consegue destruir, ele isola — e isolar tem forma. O granuloma é essa forma, e cada elemento dela é consequência mecânica do problema que resolve.

O mecanismo nuclear é um *circuito de três passos que se realimenta*. O macrófago apresenta o antígeno e produz IL-12; a IL-12 polariza o linfócito CD4 para TH1 e ele produz IFN-γ; o IFN-γ ativa o macrófago, que restaura a acidificação do fagolisossomo, gera óxido nítrico e espécies reativas de oxigênio, apresenta mais antígeno e secreta TNF — que recruta monócitos e mantém a estrutura coesa. Desse circuito nascem a célula epitelioide, a célula gigante de Langhans, a coroa linfocitária e, quando a destruição é intensa, o centro caseoso.

A clínica é a leitura desse circuito *nas duas direções*. Quando ele funciona, o resultado é o complexo primário contido, que fibrosa e calcifica e reaparece anos depois como nódulo radiopaco. Quando o eixo CD4–IFN-γ falha — pelo HIV, por defeito genético do receptor de IFN-γ ou de IL-12, ou pelo bloqueio do TNF —, o granuloma se forma mal, a contenção cede e surgem a cavitação e a disseminação miliar. E quando não há micro-organismo algum, como na sílica, no asbesto, no fio de sutura e na sarcoidose, a mesma arquitetura se monta em torno do que não se digere.

Nas aulas seguintes, este circuito reaparece com outros agentes: as micoses sistêmicas mostram fungos que disparam o mesmo padrão, e o estudo formal das hipersensibilidades devolve o granuloma ao seu lugar na classificação, como expressão morfológica da reação do tipo IV.
]
