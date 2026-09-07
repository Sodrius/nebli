#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Patologia é o estudo das alterações estruturais, bioquímicas e funcionais que a doença produz no organismo. O diagnóstico patológico é o ato de ler essas alterações num material que veio do paciente — um fragmento, uma peça cirúrgica, um esfregaço de células — e devolver ao clínico uma informação que muda conduta.

A *PARTE I* monta a cadeia que organiza esse raciocínio: causa, mecanismo, marca deixada no tecido e queixa à beira do leito. A *PARTE II* acompanha o material da mesa de macroscopia até a lâmina corada, porque cada etapa desse trajeto preserva uma coisa e destrói outra. A *PARTE III* abre as cinco ferramentas e mostra o que cada uma pergunta ao tecido — e por que são complementares, nunca substitutas.
]

#parte-title("PARTE I — A doença como cadeia: o que o patologista procura", primeira: true)

#subtopico("1.1 — Etiologia e patogênese: a causa e o caminho")

Toda doença pode ser descrita como uma sequência de quatro elos encadeados: a *etiologia*, que é o agente ou condição que a causa; a *patogênese*, que é o conjunto de mecanismos pelos quais esse agente produz o dano; as *alterações morfológicas e funcionais*, que são as marcas resultantes desse dano nas células e nos tecidos; e as *manifestações clínicas*, que são essas alterações se expressando em sintoma, sinal e exame alterado.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-03.png",
  largura: 43%,
  legenda: [A seta é de mão única no tempo, mas o raciocínio diagnóstico percorre a cadeia nos dois sentidos: da clínica de volta à causa.])

A etiologia responde à pergunta *o que* causa a doença, e divide-se em dois grupos. As causas *genéticas* estão no genoma do indivíduo — mutação herdada, alteração cromossômica, variante de suscetibilidade. As causas *adquiridas* vêm de fora ou surgem ao longo da vida: agentes infecciosos, agressões físicas e químicas, hipóxia, desequilíbrio nutricional, resposta imune contra o próprio hospedeiro. A causa pode ser única, como na anemia falciforme, ou múltipla, como na aterosclerose, em que dislipidemia, hipertensão, tabagismo e hiperglicemia somam efeitos sobre o mesmo endotélio.

Reconhecer o agente não basta, porque quase nenhum agente é *suficiente* sozinho. O bacilo da tuberculose é causa *necessária* — sem ele não há tuberculose —, mas apenas uma parcela dos infectados adoece, e quem adoece depende da competência da resposta imune, da carga infectante e do estado nutricional. A distinção entre causa necessária, suficiente e contribuinte é o que permite entender por que duas pessoas expostas ao mesmo agente têm desfechos diferentes.

A patogênese responde à pergunta *como*. É a sequência de eventos genéticos e bioquímicos que vai do estímulo inicial até a expressão da doença — que gene deixou de ser transcrito, que enzima parou, que via de sinalização foi ativada, que célula morreu e por qual mecanismo. A importância médica dessa separação é direta: quando a etiologia não pode ser removida, é sobre a patogênese que o tratamento age. Não se desfaz uma mutação germinativa, mas se bloqueia a via que ela mantém ligada.

A relação entre os elos não é biunívoca em nenhum dos sentidos, e é aqui que a ferramenta entra. Uma mesma etiologia produz patogêneses distintas conforme o hospedeiro, e uma mesma morfologia pode nascer de etiologias diferentes — necrose caseosa em um granuloma sugere tuberculose, mas também aparece em micoses profundas. Por isso o diagnóstico morfológico frequentemente entrega um *padrão*, e fechar a causa exige uma segunda ferramenta dirigida ao agente.

#mini-resumo[Etiologia é o que causa; patogênese é como causa; morfologia é o rastro. O padrão morfológico raramente identifica sozinho a etiologia — e é essa lacuna que as ferramentas da PARTE III preenchem.]

#subtopico("1.2 — A morfologia como registro: presença, grau e tempo da lesão")

A alteração morfológica não é a doença: ela é *secundária* à patogênese, um produto do mecanismo e não a sua causa. Essa é a razão pela qual descrever bem a morfologia permite reconstruir o mecanismo para trás, e é o motivo pelo qual ela costuma ser a primeira forma de detecção da doença.

Essas alterações são avaliadas em três escalas: a *macroscopia* examina a olho nu peso, tamanho, cor, consistência e limites; a *microscopia óptica*, as células e sua organização; a *ultraestrutura*, ao microscópio eletrônico, organelas e estruturas de poucos nanômetros. As três respondem à mesma pergunta em resoluções diferentes, e o achado de uma orienta a busca na seguinte.

A morfologia informa mais do que a presença da doença: informa o *grau*. Dizer que existe fibrose no fígado é um dado; dizer que ela forma septos circundando nódulos de hepatócitos em todo o parênquima é outro, e apenas o segundo caracteriza cirrose e prevê insuficiência hepática. Extensão da necrose, profundidade da invasão tumoral e proporção de glomérulos esclerosados são medidas morfológicas com consequência prognóstica direta.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-09.png",
  largura: 55%,
  legenda: [Três infartos de idades diferentes no mesmo coração, com a microscopia correspondente ao lado. A morfologia não diz apenas que houve lesão: diz há quanto tempo.])

O tempo é a informação que mais escapa a quem começa. Cada lesão tem uma cronologia previsível de achados, e ler essa cronologia data o evento. No infarto do miocárdio, o miócito privado de oxigênio perde a contração em menos de um minuto, mas a necrose só se torna reconhecível ao microscópio depois de algumas horas — o citoplasma fica intensamente rosado e o núcleo desaparece por #termo-nota[cariólise][dissolução da cromatina pela ação de nucleases, a etapa final da morte do núcleo, precedida por picnose e cariorrexe]. Nas primeiras 24 horas chegam neutrófilos; entre o terceiro e o sétimo dia predominam macrófagos removendo os restos; na segunda semana instala-se #termo-nota[tecido de granulação][tecido de reparo formado por capilares neoformados, fibroblastos e matriz frouxa, que substitui a área necrótica antes da cicatriz]; ao fim de semanas resta cicatriz colágena pálida.

O corolário é incômodo: nas primeiras horas a morfologia é normal apesar de a doença já estar instalada e já ser letal. A alteração funcional pode preceder em muito a estrutural, e tecido morfologicamente preservado não garante tecido saudável.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-10.png",
  largura: 49%,
  legenda: [A falha de enchimento no ramo arterial pulmonar da tomografia e o trombo cavalgando a bifurcação na peça são o mesmo achado, lidos por dois métodos com escalas de resolução separadas por três ordens de grandeza.])

A morfologia macroscópica corresponde quase termo a termo à imagem radiológica, porque ambas leem densidade, contorno e limite — a diferença está na resolução, próxima de um milímetro na tomografia e de dois décimos de micrômetro na microscopia, e no fato de a imagem ser feita no paciente vivo.

#subtopico("1.3 — As cinco frentes da patologia e o raciocínio da causa da morte")

O último elo da cadeia montada em 1.1 é a manifestação clínica, definida com precisão: é como a patogênese e as alterações morfológicas se expressam à beira do leito. O ícterico tem bilirrubina impregnando mucosa e pele porque a excreção hepática falhou; a dispneia da insuficiência cardíaca é congestão pulmonar em forma de sintoma. Nenhum sinal existe sem uma alteração estrutural ou funcional por baixo dele.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-14.png",
  largura: 49%,
  legenda: [Cinco frentes, um mesmo objeto. A interface com as demais especialidades não é acessória: o material só é bem interpretado com a história clínica junto.])

A especialidade se organiza em cinco frentes. A *patologia cirúrgica* examina biópsias e peças de ressecção, e é a que mais decide conduta oncológica; a *citopatologia*, células isoladas obtidas por raspado, punção ou líquido corporal; a *patologia clínica* corresponde ao laboratório de análises; a *patologia forense* investiga mortes violentas ou suspeitas; e a *autópsia* investiga a doença que levou à morte natural.

A autópsia mantém uma função que nenhum exame de imagem substituiu: comparar o que se pensou em vida com o que se encontra depois. Séries hospitalares modernas ainda mostram discrepâncias maiores — achados que, se conhecidos antes, teriam mudado a conduta — em cerca de uma em cada dez autópsias.

Desse raciocínio nasce um documento que todo médico assina e quase ninguém aprende a preencher. A parte I da declaração de óbito é uma *cadeia causal escrita ao contrário*: a primeira linha traz a causa imediata, aquela que encerrou a vida, e cada linha abaixo traz a condição que originou a de cima, até a última linha preenchida, que é a *causa básica* — a doença que iniciou a sequência. A parte II reúne as condições que contribuíram para a morte sem pertencer a essa cadeia.

#clinica-box("A cadeia escrita de trás para frente", [
Paciente diabética sofre trauma no hálux, evolui com infecção cutânea, depois pneumonia hospitalar, e morre em insuficiência respiratória. A parte I fica, de cima para baixo: insuficiência respiratória, pneumonia hospitalar, infecção cutânea, contusão do hálux; a parte II traz o diabetes.

O diabetes não ocupa a parte I porque não iniciou *esta* sequência — ele a permitiu, ao produzir a neuropatia que apagou a dor do trauma e a vasculopatia que impediu a cicatrização. Trocar a ordem, ou promovê-lo a causa básica, altera a estatística de mortalidade, montada a partir da causa básica de cada declaração.
])

#parte-title("PARTE II — Do corpo à lâmina: o que acontece com o material")

#subtopico("2.1 — Macroscopia e amostragem: a decisão que precede o microscópio")

Uma peça de colectomia tem 30 cm de comprimento; o fragmento que vira lâmina tem 2 cm de lado e 4 micrômetros de espessura. O que o microscópio examina é uma fração minúscula do que foi retirado, e quem escolhe essa fração é o patologista na mesa de macroscopia. Essa escolha é irreversível e limita tudo o que virá depois — nenhuma coloração recupera o que não foi amostrado.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-17.png",
  largura: 51%,
  legenda: [Da peça medida com régua ao fragmento no cassete: cada etapa da macroscopia gera um dado que não existe mais depois que o material é cortado.])

O exame macroscópico começa antes do formol: o material *a fresco* permite o que a fixação impede — congelar um fragmento para análise imediata, semear cultura, separar tecido para citometria de fluxo ou banco de tumor. Decidir isso depois que a peça mergulhou no fixador é tarde.

A descrição segue ordem fixa: pesos e medidas — peso do baço, espessura da parede ventricular, maior diâmetro do tumor —, cortes seriados, caracterização das lesões quanto a cor, consistência, limites e distância às margens, fotografia do que não sobreviverá ao corte, e a *representação histológica*, que é a amostragem propriamente dita.

Um detalhe operacional carrega peso oncológico. Antes de cortar, a superfície de ressecção é pintada com tinta nanquim, que resiste ao processamento e reaparece preta no microscópio; assim o patologista sabe exatamente onde estava o limite do que o cirurgião retirou. Tumor tocando a tinta significa margem comprometida, e margem comprometida costuma significar reoperação ou radioterapia — um dado gerado por um pincel, não por um reagente caro.

A amostragem também define o que vale um resultado negativo. Protocolos fixam quantos fragmentos representam cada tipo de peça porque o erro de amostragem é a principal causa de falso-negativo em patologia. Quando a lesão é focal e pequena, a agulha precisa ser levada até ela por um método de imagem — a ponte para o item 2.3. Em material exíguo, a ausência de achado significa que aquela amostra não continha a lesão, não que o órgão esteja livre dela.

#mini-resumo[A macroscopia decide o que será visto: material a fresco abre opções que o formol fecha, a tinta na margem transforma um dado espacial em dado microscópico, e a representatividade da amostra é o que dá — ou tira — valor a um resultado negativo.]

#subtopico("2.2 — Fixação e processamento: por que o formol, e o que ele custa")

O tecido removido do corpo começa a se digerir sozinho em minutos: as enzimas dos lisossomos vazam de células que morrem sem irrigação e destroem a arquitetura, um processo chamado #termo-nota[autólise][autodigestão do tecido pelas próprias enzimas lisossômicas após a morte celular, responsável pela perda de detalhe morfológico em material mal fixado]. Fixar é interromper essa destruição no instante mais próximo possível do estado vivo.

O fixador de rotina é o formol tamponado a 10%, com cerca de 4% de formaldeído. Ele reage com grupos amino livres de proteínas, sobretudo o grupo ε-amino da lisina, e forma *pontes de metileno* que ligam cadeias vizinhas entre si. Essa reticulação enrijece o tecido, imobiliza as proteínas onde estavam e inativa as enzimas da autólise. O fixador penetra a cerca de 1 mm por hora, o que explica duas regras de bancada: fatiar a peça em lâminas de poucos milímetros e usar volume de fixador dez vezes maior que o dela. Peça grossa mergulhada inteira fixa a superfície e autolisa o centro.

Fixado o tecido, a água é retirada em álcoois de concentração crescente, porque a parafina não se mistura com água. O álcool é então substituído pelo xilol na etapa de #termo-nota[diafanização][banho em solvente miscível tanto com álcool quanto com parafina, que torna o tecido translúcido e permite a impregnação pela parafina]. O tecido é impregnado por parafina líquida a cerca de 58 °C e incluído em bloco. O micrótomo corta fitas de 3 a 5 micrômetros — espessura de uma a duas células —, que são estendidas em banho-maria morno e pescadas com a lâmina. Antes de corar, desfaz-se o caminho: a parafina sai no xilol e o tecido é reidratado, porque a hematoxilina é uma solução aquosa.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-19.png",
  largura: 49%,
  legenda: [Processador, micrótomo, banho de flotação e os dois corantes. O fragmento mal orientado no molde gera corte oblíquo e epitélio ilegível — o trajeto inteiro existe para permitir um corte de poucos micrômetros que ainda se pareça com tecido vivo.])

O formol cobra três preços, e os três reaparecem na PARTE III. As pontes de metileno alteram a conformação das proteínas e escondem os sítios que os anticorpos reconhecem — daí a etapa de #termo-nota[recuperação antigênica][aquecimento do corte em tampão de citrato ou de EDTA, que desfaz parte das ligações cruzadas do formol e reexpõe os epítopos para o anticorpo] na imunohistoquímica. O formaldeído também fragmenta o DNA e o liga a proteínas, o que restringe os testes moleculares a segmentos curtos, tipicamente abaixo de 300 pares de base. E álcool e xilol dissolvem os lipídeos: gordura não é vista na lâmina de rotina, e o vacúolo vazio do hepatócito esteatótico é o buraco que ela deixou.

#atencao-box("Congelação responde rápido; não responde tudo", [
No exame de congelação o fragmento é resfriado a cerca de −25 °C, e a água transformada em gelo dá a dureza que a parafina daria. O corte sai no criostato e a coloração fica pronta em 10 a 15 minutos, com o cirurgião ainda operando: diz se a margem está livre, se o material é representativo e qual a natureza geral da lesão.

O preço é morfológico: os cristais de gelo rasgam o citoplasma, distorcem o núcleo e o detalhe fino se perde. O diagnóstico definitivo é sempre o da parafina.
])

#subtopico("2.3 — Citopatologia e punção guiada: células sem arquitetura")

A citopatologia abre mão da arquitetura do tecido para ganhar acesso. Em vez de retirar um fragmento, colhem-se células soltas — por raspado do colo uterino, por escova brônquica, do sedimento de um derrame pleural ou da urina, ou por *punção aspirativa por agulha fina*, técnica em que uma agulha de calibre fino, semelhante à de injeção, aspira células de um nódulo sem retirar um cilindro de tecido. O material é espalhado na lâmina, fixado em álcool e corado.

#figura-lateral("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-21.png",
  lado: "right",
  largura-figura: 36%,
  texto: [O esfregaço tem uma técnica própria: a segunda lâmina espalha a gota em camada única, porque células empilhadas não permitem avaliar núcleo. Material espesso, coagulado ou seco ao ar antes da fixação gera artefato que imita atipia — parte dos resultados inconclusivos nasce aqui, e não na lesão.],
  legenda: [Do aspirado ao esfregaço em monocamada.])

O que se lê numa célula isolada é o critério de atipia: aumento da #termo-nota[relação núcleo-citoplasma][proporção entre a área do núcleo e a do citoplasma, em torno de 1:4 a 1:6 em epitélio maduro; sua elevação é um dos primeiros sinais de transformação], hipercromasia, cromatina grosseira, nucléolo proeminente e contorno nuclear irregular — suspeita de malignidade levantada com rapidez, custo baixo e agressão mínima.

O que a citologia *não* decide é a invasão. Invasão é uma relação espacial — células neoplásicas atravessando a membrana basal e ocupando o estroma subjacente — e uma relação espacial só existe onde a arquitetura foi preservada. Por isso a distinção entre lesão *in situ*, que não rompeu a membrana basal, e neoplasia invasora exige um fragmento de tecido, não um esfregaço. A citologia levanta a suspeita e seleciona quem precisa de biópsia; a histologia estadia.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-20.png",
  largura: 49%,
  legenda: [A ultrassonografia leva a agulha ao nódulo em tempo real e confirma que a ponta está dentro da lesão. Sem esse guia, a punção de um nódulo pequeno amostra o parênquima ao redor.])

#clinica-box("Nódulo de tireoide: a punção decide quem opera", [
Nódulos tireoidianos são frequentes na ultrassonografia e a maioria é benigna. A punção guiada por imagem separa quem precisa de cirurgia de quem precisa apenas de seguimento, e decide por critérios nucleares — o carcinoma papilífero tem núcleo claro, com fenda longitudinal e pseudoinclusão, reconhecível célula a célula.

A exceção confirma a regra do parágrafo anterior: diante de lesão folicular a punção não decide, porque adenoma e carcinoma folicular têm células idênticas e o que os separa é a invasão de cápsula ou de vasos. O diagnóstico só sai na peça, com a cápsula inteira examinada — a diferença não está na célula, está na relação dela com o que existe ao redor.
])

#parte-title("PARTE III — As cinco ferramentas: o que cada uma pergunta ao tecido")

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-15.png",
  largura: 55%,
  legenda: [O mapa da PARTE III. A palavra em vermelho é o ponto: as ferramentas são complementares — cada uma responde a uma pergunta que as outras não respondem, e a ordem de uso é dirigida pela hipótese.])

#subtopico("3.1 — Hematoxilina e eosina: a química das duas cores")

Toda coloração é uma reação química com endereço: o corante se liga a um tipo de sítio molecular e não a outro, e a imagem colorida é o mapa desses sítios. A coloração de rotina, a #sigla("HE", [hematoxilina-eosina — a coloração de rotina da anatomia patológica, base de praticamente todo diagnóstico morfológico]), tem dois corantes com endereços opostos.

A hematoxilina, extraída de uma árvore e oxidada a hemateína, não cora sozinha: precisa de um mordente de alumínio, com o qual forma um complexo de carga positiva. Esse complexo se liga aos grupos fosfato de carga negativa do #sigla("DNA", [ácido desoxirribonucleico]) e do #sigla("RNA", [ácido ribonucleico]), e é por isso que ele cora de azul-arroxeado tudo o que é rico em ácido nucleico — o núcleo, em primeiro lugar, mas também o retículo endoplasmático rugoso coberto de ribossomos. Essa afinidade por corante básico é a #termo-nota[basofilia][propriedade de estruturas aniônicas, ricas em fosfato de ácidos nucleicos, de fixar corantes básicos como a hematoxilina].

A eosina faz o contrário: corante ácido, em solução vira ânion e se liga a grupos de carga positiva — as cadeias laterais protonadas de lisina e arginina. Cora o citoplasma rico em proteína, o colágeno da matriz e, com intensidade máxima, a hemácia repleta de hemoglobina. Essa afinidade é a acidofilia, ou eosinofilia.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-23.png",
  largura: 55%,
  legenda: [O mundo em roxo e rosa. À esquerda, um nódulo dérmico reconhecível pelo padrão de arranjo; à direita, miocárdio com infiltrado inflamatório — núcleos azuis entre fibras rosadas.])

A regra de carga explica leituras que parecem decorebas isoladas. O plasmócito tem citoplasma intensamente basófilo porque é uma fábrica de anticorpo, e fábrica de proteína secretada significa retículo rugoso abundante. A célula em necrose fica hipereosinofílica por dois motivos somados: perde o RNA citoplasmático, que puxava hematoxilina, e tem suas proteínas desnaturadas, o que expõe mais sítios para a eosina — enquanto o núcleo escurece e encolhe, fragmenta-se e desaparece. E a distinção nítida entre núcleo e citoplasma, que o slide destaca como virtude do método, é justamente o que torna possível avaliar a relação núcleo-citoplasma discutida em 2.3.

A HE é rápida, barata e universal: fica pronta em poucas horas, permite avaliar padrões de arranjo tecidual e gera a hipótese. O que ela não faz é identificar moléculas — duas neoplasias de células pequenas e azuis podem ser indistinguíveis nela, e é dessa limitação que nascem as quatro ferramentas seguintes.

#subtopico("3.2 — Histoquímica: reagentes dirigidos a classes de moléculas")

A HE separa estruturas por carga elétrica, o que é uma regra grosseira. A histoquímica troca essa regra por uma reação química dirigida a uma classe de moléculas — carboidrato, lipídeo, ferro, colágeno, componente de parede de microrganismo —, e por isso responde perguntas que a rotina deixa em aberto.

O método mais usado é o #sigla("PAS", [ácido periódico-reativo de Schiff — coloração que revela carboidratos, da membrana basal ao glicogênio e à parede de fungos]). O ácido periódico oxida carbonos adjacentes que carregam hidroxilas, abundantes em açúcares, gerando aldeídos; o reativo de Schiff liga-se a eles e assume cor magenta, corando glicogênio, muco neutro, membrana basal e parede de fungo. Tratando o corte com diastase antes, o glicogênio é digerido e some — o que persiste é muco ou membrana basal, e o método traz o próprio controle.

#align(center)[
#text(size: 8.6pt)[
#table(
  columns: (auto, 1fr, 1fr),
  inset: 5.5pt,
  align: left + top,
  stroke: 0.4pt + gray-border,
  table.header([*Método*], [*Alvo químico*], [*Onde decide*]),
  [PAS · Alcian blue], [carboidratos; muco neutro e ácido], [membrana basal, glicogênio, fungo, muco],
  [Ziehl-Neelsen], [ácidos micólicos da parede], [micobactéria (bacilo álcool-ácido resistente)],
  [Grocott (prata)], [polissacarídeos da parede fúngica], [fungo em tecido, contorno negro],
  [Brown-Hopps], [parede bacteriana (Gram tecidual)], [bactéria em abscesso e vegetação],
  [Perls], [ferro férrico da hemossiderina], [hemorragia antiga, sobrecarga de ferro],
  [Fontana-Masson], [melanina], [pigmento castanho de origem melanocítica],
  [Masson · Picro-Sirius], [colágeno], [fibrose e cirrose, quantificação],
  [Verhoeff · resorcina-fucsina], [fibra elástica], [parede arterial, elastose],
  [Oil Red O], [lipídeo neutro], [esteatose e embolia gordurosa, só em congelação],
)]]

Duas linhas da tabela carregam mais mecanismo do que parece. O #termo-nota[bacilo álcool-ácido resistente][micobactéria, cuja parede rica em ácidos micólicos retém a carbol-fucsina mesmo sob descoloração por álcool e ácido — daí o nome do achado] retém o corante porque a parede cerosa é impermeável ao descorante, não por afinidade especial: o método explora uma propriedade física da parede. E o Oil Red O só funciona em congelação porque o álcool e o xilol da rotina já dissolveram a gordura, como ficou estabelecido em 2.2.

Há um limite embutido no nome: a identificação histoquímica é *grosseira* no sentido técnico — reconhece a classe química, não a molécula. PAS positivo indica material rico em carboidrato, que pode ser glicogênio, muco ou fungo, e o contexto morfológico decide. Do mesmo modo, um pigmento castanho na rotina tem candidatos que só as reações separam: hemossiderina azula no Perls, melanina escurece no Fontana-Masson, lipofuscina não reage a nenhum dos dois, e antracose é preta e não cora — é carvão inerte.

#clinica-box("Quando o achado morfológico não fecha o agente", [
Um granuloma com necrose caseosa no pulmão levanta tuberculose, mas o mesmo padrão aparece em micoses profundas e em micobactérias não tuberculosas: o Ziehl-Neelsen procura o bacilo no corte, o Grocott procura fungo no mesmo material.

O ponto de atenção está no negativo. A carga bacilar em lesão bem organizada pela imunidade é baixa, e um Ziehl negativo não exclui tuberculose — segue-se para cultura, que leva semanas, ou para amplificação de ácido nucleico, que responde em horas. A ferramenta seguinte é acionada pela limitação da anterior, não por preferência.
])

#subtopico("3.3 — Imunohistoquímica e imunofluorescência: o anticorpo como reagente")

A #sigla("IHQ", [imunohistoquímica — identificação de proteínas no corte histológico por meio de anticorpos específicos, com revelação por reação enzimática]) usa como reagente a molécula mais específica que a biologia produz. Um anticorpo dirigido contra um epítopo da proteína procurada é aplicado sobre o corte; onde a proteína estiver, ele fica.

Cada passo da sequência técnica tem uma razão. O corte passa antes pela recuperação antigênica, que desfaz parte das pontes de metileno do formol e reexpõe o epítopo. Bloqueia-se a peroxidase endógena do tecido, que produziria cor falsa. Aplica-se o anticorpo primário e, depois, um anticorpo secundário biotinilado, que reconhece o primeiro; sobre ele monta-se o complexo avidina-biotina carregado de peroxidase. A enzima oxida a diaminobenzidina, que precipita como pigmento castanho insolúvel *no local exato da reação* — e é essa insolubilidade que permite ver a proteína sobre a arquitetura preservada, com hematoxilina contracorando os núcleos. Cada etapa custa incubação e lavagem: por isso o método acrescenta ao menos 24 horas ao tempo do laudo.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-29.png",
  largura: 53%,
  legenda: [À esquerda, marcação nuclear; à direita, marcação de membrana desenhando o contorno de cada célula. O castanho está nos dois, mas o resultado é diferente — a localização faz parte da resposta.])

O padrão de marcação é parte do resultado. Receptor de estrogênio e o marcador de proliferação Ki-67 marcam *núcleo*, porque são proteínas nucleares; o #sigla("HER2", [receptor 2 do fator de crescimento epidérmico humano — proteína de membrana cuja superexpressão indica terapia dirigida]) e a caderina-E marcam *membrana*, porque são proteínas de superfície; citoqueratina e actina marcam *citoplasma*. Marcação num compartimento incompatível com a biologia da proteína é artefato, e é por isso que toda bateria roda com controle positivo e controle negativo.

#atencao-box("Marcação no lugar errado é resultado errado", [
Uma reação para HER2 que aparece difusa no citoplasma, sem desenhar a membrana, não é HER2 positivo — é reação inespecífica. Ler apenas a presença do castanho, sem a localização, inverte condutas: um resultado falso-positivo indica um tratamento caro e cardiotóxico a quem não vai se beneficiar dele, e um falso-negativo nega o tratamento a quem responderia.
])

A imunohistoquímica presta dois serviços. O primeiro é dizer *o que* é a lesão e de onde ela veio: citoqueratina indica carcinoma, o antígeno leucocitário comum indica linfoma, S-100 e Melan-A indicam melanoma; numa metástase de sítio primário desconhecido, marcadores como TTF-1, CDX2 e GATA3 apontam pulmão e tireoide, trato digestório e mama. O segundo é *predizer resposta a tratamento*: receptor de estrogênio positivo indica hormonioterapia, superexpressão de HER2 indica anticorpo dirigido contra ele — e aqui a coloração deixa de ser diagnóstica e passa a ser preditiva.

#figura-lateral("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-30.png",
  lado: "left",
  largura-figura: 40%,
  texto: [A #sigla("IF", [imunofluorescência — variante da imunohistoquímica em que o anticorpo carrega um fluoróforo, lida em microscópio de fluorescência]) troca a enzima por um fluoróforo. Ela é a técnica de escolha na biópsia renal e nas doenças bolhosas da pele, e exige tecido *congelado*, porque a fixação e a inclusão destroem a antigenicidade dos imunocomplexos depositados. A topografia da fluorescência entrega o mecanismo: depósito *linear* ao longo da membrana basal glomerular indica anticorpo dirigido contra a própria membrana; depósito *granular* indica imunocomplexos circulantes que se depositaram ali. Mesmo corante, mesmo órgão, doenças diferentes.],
  legenda: [Glomérulo em IF e o esquema da amplificação por avidina-biotina.])

#subtopico("3.4 — Microscopia eletrônica e patologia molecular: resolução e genótipo")

Existe um limite físico onde o microscópio óptico para, e ampliar não o resolve. A resolução — menor distância entre dois pontos que ainda aparecem separados — é imposta pelo comprimento de onda da luz visível, entre 400 e 700 nanômetros, e fica em torno de 0,2 micrômetro; além disso, só se amplia o borrão. A microscopia eletrônica usa elétrons acelerados, de comprimento de onda associado da ordem de 0,004 nanômetro, e alcança na prática poucos nanômetros: ganho de cerca de mil vezes.

Esse ganho tem custo proporcional. O tecido é fixado em glutaraldeído, pós-fixado em tetróxido de ósmio, incluído em resina epóxi, cortado em fatias ultrafinas de 60 a 90 nanômetros — cinquenta vezes mais finas que o corte de parafina — e contrastado com sais de metais pesados. Poucos centros mantêm a estrutura, o que obriga a seleção prévia rigorosa: manda-se o caso cuja pergunta só ela responde.

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-24.png",
  largura: 49%,
  legenda: [Corte transversal de cílios. À esquerda, o padrão normal de nove pares periféricos e um par central; à direita, as setas apontam onde deveriam estar os braços de dineína — a ausência mede cerca de 25 nanômetros e é invisível na microscopia óptica.])

A discinesia ciliar primária é o exemplo canônico. O #termo-nota[axonema][esqueleto interno do cílio, com nove pares de microtúbulos periféricos ao redor de um par central e braços de dineína que promovem o deslizamento entre os pares] só é resolvido no microscópio eletrônico, e o defeito diagnóstico é a ausência dos braços de dineína, de algumas dezenas de nanômetros. Sem eles o cílio não bate: falha o transporte mucociliar, com sinusite e otite de repetição e bronquiectasias; o flagelo do espermatozoide, que tem o mesmo axonema, não se move, e há infertilidade. No embrião, os cílios do nó que estabelecem a assimetria direita-esquerda também param, e cerca de metade dos pacientes tem situs inversus — a síndrome de Kartagener. A mesma técnica é rotina na biópsia renal, onde mede a membrana basal glomerular e localiza depósitos elétron-densos que a luz não mostra.

A patologia molecular faz a pergunta seguinte: qual mutação, qual sequência, qual gene amplificado. A #sigla("PCR", [reação em cadeia da polimerase — amplificação exponencial de um segmento definido de DNA, que multiplica por milhões uma sequência inicialmente indetectável]) dobra o número de cópias do alvo a cada ciclo, e detecta o que está abaixo do limiar morfológico: micobactéria escassa demais para o Ziehl, genoma viral, rearranjo clonal de linfócitos. A hibridização *in situ* faz o oposto — a sonda marcada é aplicada sobre o próprio corte e a leitura preserva a topografia; na #sigla("FISH", [hibridização in situ por fluorescência — sondas aplicadas ao corte, que permitem contar cópias de um gene dentro de cada núcleo]) contam-se os sinais núcleo a núcleo, e a amplificação de HER2 é definida por razão igual ou maior que 2,0 entre cópias do gene e do centrômero do cromossomo 17.

#confusao-prevista(
  titulo: "Mais aumento não é mais resolução",
  aluno_acha: [aluno acha que basta uma objetiva mais forte para enxergar organela na lâmina de rotina],
  mecanismo: [resolução é fixada pelo comprimento de onda da radiação; ampliação apenas escala a imagem. Ver um braço de dineína de 25 nanômetros exige trocar a luz pelo elétron, não trocar a lente.],
)

#figura-nebli("/figuras/pat-01-ferramentas-diagnostico-patologico/slide-31.png",
  largura: 51%,
  legenda: [À esquerda, a morfologia na rotina; à direita, o mesmo material em hibridização in situ, com os sinais fluorescentes contados núcleo a núcleo. O teste molecular é acoplado à morfologia, não a substitui.])

O limite do método vem de 2.2: o DNA fragmentado pelo formol restringe a amplificação a segmentos curtos, e material muito antigo ou mal fixado pode não amplificar. O produto final não é apenas um nome — a mutação identificada define o fármaco dirigido a ela, como os inibidores de tirosina-quinase nos tumores com mutação do #sigla("EGFR", [receptor do fator de crescimento epidérmico — a mutação ativadora dele define sensibilidade ao inibidor]).

#conclusao-box[
O princípio que atravessa o resumo cabe numa frase: *cada ferramenta da patologia responde a uma pergunta diferente, e a pergunta é definida pela cadeia etiologia–patogênese–morfologia–clínica*. Não há hierarquia entre elas, há complementaridade — a palavra que o professor destaca em vermelho no mapa das ferramentas.

O mecanismo nuclear é a troca permanente entre o que se preserva e o que se perde. O formol preserva a forma criando pontes de metileno, e ao fazê-lo mascara epítopo, fragmenta DNA e abre caminho para o xilol dissolver o lipídeo; a congelação preserva antigenicidade e gordura, e destrói o detalhe com cristal de gelo; a citologia alcança qualquer nódulo com uma agulha fina, e perde a arquitetura que decide invasão. Escolher a ferramenta é escolher qual perda é aceitável diante da pergunta feita.

Na clínica isso aparece como sequência ordenada, não como cardápio: a hematoxilina-eosina gera a hipótese em horas; a histoquímica entra quando a hipótese envolve uma classe química; a imunohistoquímica entra para nomear a proteína, e nela o padrão de marcação faz parte do resultado; a microscopia eletrônica e os testes moleculares entram quando a resposta está abaixo do limite óptico ou dentro do genoma — e é aí que o laudo passa a escolher o tratamento.

O que vem a seguir usa isso como alfabeto: alterações celulares reversíveis e irreversíveis, inflamação e reparo, distúrbios circulatórios e neoplasias serão descritos nos termos aqui montados — o que se vê a olho nu, o que se vê na lâmina, o que a reação revela e o que só o anticorpo, o elétron ou a sonda alcançam.
]
