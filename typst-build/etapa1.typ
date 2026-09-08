#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Um vírus não tem metabolismo próprio: ele só existe enquanto usa a célula. Toda a patologia da infecção viral nasce dessa dependência — do que a célula sofre para produzir vírus, e do que o organismo destrói ao tentar interromper essa produção.

A *PARTE I* percorre o que o vírus faz com a célula que ocupa, e como cada efeito se torna um achado reconhecível ao microscópio. A *PARTE II* mostra que o padrão da lesão é esculpido pela resposta imune — quem chega primeiro, o que cada efetor faz e por que o dano acompanha a resposta, não a carga viral. A *PARTE III* junta as duas metades num órgão só: a hepatite pelo vírus B, do acúmulo de antígeno no hepatócito até a arquitetura cirrótica.
]

#parte-title("PARTE I — O que o vírus faz com a célula", primeira: true)

#subtopico("1.1 — Sete efeitos, três destinos")

A infecção viral lesa a célula por caminhos que terminam em três desfechos distintos, e essa separação organiza toda a aula: a célula rompe, a célula sobrevive alterada, ou a célula sobrevive e passa a proliferar sem controle.

A *lise celular* é o desfecho da replicação que consome a célula por dentro. À medida que a maquinaria de síntese é desviada para produzir capsídeo e genoma viral, a membrana perde integridade e o conteúdo citoplasmático — enzimas lisossomais, ácido úrico, #sigla("ATP", [adenosina trifosfato — nucleotídeo energético que, fora da célula, funciona como sinal de perigo]) e fragmentos de DNA — é despejado no interstício. Essas moléculas são #sigla("DAMP", [padrão molecular associado a dano — molécula do interior da célula que, no meio extracelular, sinaliza morte violenta e ativa a resposta inata]), e o macrófago residente que as reconhece libera interleucina-1 e fator de necrose tumoral, citocinas que abrem o endotélio e recrutam neutrófilo em horas. É por isso que o slide liga a lise diretamente a inflamação aguda.

A *apoptose* é o desfecho oposto em termos de repercussão tecidual. A célula infectada se retrai, condensa a cromatina e fragmenta-se em corpos apoptóticos envolvidos por membrana íntegra, prontamente fagocitados pelo vizinho. Nada vaza, nenhum sinal de perigo é liberado e não há quimiotaxia: morre-se muita célula sem infiltrado inflamatório proporcional. A apoptose pode ser disparada pelo próprio vírus, que a usa para dispersar partículas dentro de corpos apoptóticos, ou pelo hospedeiro, que a usa como forma de eliminar a fábrica antes que ela produza.

Entre esses dois extremos está o #termo-nota[efeito citopático][conjunto de alterações morfológicas que a célula infectada exibe ao microscópio óptico sem necessariamente morrer — inclusões, sincícios, arredondamento e parada mitótica], que é o que o patologista efetivamente vê. O professor agrupa quatro entradas sob essa chave. O *bloqueio da síntese proteica* vem dos dois lados: o vírus cliva fatores de iniciação da tradução para monopolizar o ribossomo, e o hospedeiro paralisa a mesma tradução como defesa — mecanismo retomado na PARTE II. A *formação de sincícios* funde células vizinhas numa massa multinucleada. A *despolimerização do citoesqueleto* desfaz a rede de filamentos que sustenta a forma e a adesão, e a célula arredonda e se destaca do vizinho. A *interrupção do ciclo mitótico* trava a célula na fase em que nucleotídeos e enzimas de replicação estão mais disponíveis, sequestrando-os para o genoma viral.

O terceiro desfecho inverte a lógica dos dois primeiros. Na *transformação celular*, proteínas virais inativam os freios do ciclo celular e a célula infectada não morre — prolifera. O destino é neoplasia, e o exemplo clássico é o papilomavírus no colo uterino.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-04.png",
  largura: 72%,
  legenda: [A chave do meio agrupa os efeitos que a célula exibe *estando viva*. Repare que lise e transformação ficam de fora dela: uma termina em ruptura e inflamação aguda, a outra em proliferação — e é a única em que a célula infectada tem futuro.])

#mini-resumo[A lise vaza conteúdo → sinal de perigo → neutrófilo. A apoptose empacota o conteúdo → nenhum sinal → nenhum infiltrado. O efeito citopático deixa a célula viva e deformada — e é ele que dá o diagnóstico morfológico.]

#subtopico("1.2 — Inclusões: onde o vírus se acumula é onde ele se monta")

Uma fábrica clandestina não é descoberta pela máquina, que é pequena e escondida, mas pelo estoque que ela deixa acumulado num canto. A inclusão viral é esse estoque.

Um vírion mede de 20 a 300 nanômetros e está bem abaixo do limite de resolução da microscopia óptica, em torno de 0,2 micrômetro — nenhuma partícula isolada é visível na lâmina de hematoxilina-eosina. O que se enxerga é a *inclusão*, agregado de nucleocapsídeos e proteínas virais acumulados em quantidade suficiente para formar uma massa com afinidade tintorial própria, em geral eosinofílica e com contorno definido.

O #termo-nota[corpúsculo de Negri][inclusão citoplasmática eosinofílica, arredondada, característica da raiva; encontrada sobretudo em neurônios do corno de Ammon e em células de Purkinje] é o exemplo canônico de inclusão citoplasmática. Ele aparece no neurônio, é único ou escasso por célula, e sua localização no citoplasma corresponde ao compartimento em que o vírus da raiva — um vírus de RNA — transcreve, traduz e monta suas partículas.

Essa correspondência é a regra que dá utilidade ao achado: *a topografia da inclusão indica o compartimento de replicação*. Vírus de DNA replicam no núcleo, porque dependem da maquinaria de transcrição nuclear da célula, e por isso formam inclusões nucleares — herpes-vírus e citomegalovírus são os exemplos diários; a exceção é o poxvírus, que carrega as próprias enzimas e replica no citoplasma. Vírus de RNA replicam no citoplasma, onde estão os ribossomos e onde sua polimerase própria opera, e as exceções são o ortomixovírus e os retrovírus, que precisam do núcleo.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-05.png",
  largura: 46%,
  legenda: [A inclusão está no citoplasma, ao lado do núcleo, e não dentro dele. A barra de 10 µm dá a escala: o corpúsculo tem alguns micrômetros — dezenas de vezes maior que a partícula viral que o compõe.])

O sarampo é a exceção instrutiva. É um vírus de RNA, replica no citoplasma e ali forma inclusões — mas seus nucleocapsídeos também migram para o núcleo e se acumulam como *inclusão nuclear*, o que faz da célula infectada portadora dos dois tipos ao mesmo tempo. A inclusão nuclear eosinofílica cercada por um halo claro, com a cromatina empurrada contra a membrana nuclear, recebe o nome de *corpúsculo de Cowdry tipo A* e não é exclusiva do sarampo: herpes simples e citomegalovírus produzem a mesma imagem. É o contexto — qual tecido, qual quadro clínico, que outras alterações acompanham — que separa os agentes, não a inclusão isolada.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-06.png",
  largura: 48%,
  legenda: [Duas células no centro do campo trazem massa eosinofílica dentro do núcleo, com a cromatina deslocada para a periferia. Compare com os núcleos vizinhos, de cromatina distribuída por igual.])

#confusao-prevista(
  titulo: "Inclusão não é o vírus sendo visto",
  aluno_acha: [o aluno lê "acúmulo de componentes virais" e imagina estar enxergando partículas virais na lâmina],
  mecanismo: [o vírion está uma ordem de grandeza abaixo do que a lente resolve. A inclusão só aparece porque milhares de nucleocapsídeos se agregam num mesmo ponto e formam uma massa micrométrica. Enxergar a partícula exige microscopia eletrônica — e é por isso que a inclusão indica infecção, mas não identifica o agente sozinha.],
)

#subtopico("1.3 — Sincício e coilócito: duas deformações, duas estratégias")

Uma célula com vinte núcleos e uma célula escavada em torno do núcleo parecem acidentes morfológicos sem parentesco. São, na verdade, dois efeitos citopáticos com mecanismo definido, e cada um denuncia a estratégia do vírus que o produziu.

O #termo-nota[sincício][massa citoplasmática única contendo múltiplos núcleos, formada pela fusão de células vizinhas induzida por proteína viral de fusão] se forma quando a célula infectada insere na própria membrana plasmática a glicoproteína de fusão do vírus — a proteína F dos paramixovírus, a gp41 do #sigla("HIV", [vírus da imunodeficiência humana]), a glicoproteína B dos herpes-vírus. Essa proteína é a mesma que funde o envelope viral com a membrana da célula na entrada; exposta na superfície de uma célula já infectada, ela funde essa membrana com a da vizinha. Os citoplasmas se unem, os núcleos se somam, e o resultado é a célula gigante multinucleada da bronquiolite pelo #sigla("VSR", [vírus sincicial respiratório — principal agente de bronquiolite no lactente]), da pneumonia do sarampo e do esfregaço de lesão herpética.

A vantagem para o vírus é direta: passando de citoplasma a citoplasma pela fusão, a partícula nunca atravessa o meio extracelular, onde o anticorpo neutralizante a encontraria. É a razão de a resposta humoral, sozinha, não conter uma infecção estabelecida.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-07.png",
  largura: 46%,
  legenda: [Os núcleos aparecem agrupados em ilhas, sem membrana separando-os — cada ilha era um conjunto de células independentes antes da fusão.])

#atencao-box("Sincício viral e célula gigante de granuloma têm origens distintas", [
As duas são células multinucleadas, e o aluno costuma tratá-las como o mesmo achado. O sincício viral resulta da fusão de células *infectadas* com suas vizinhas, comandada por uma glicoproteína viral de fusão exposta na membrana. A célula gigante do granuloma resulta da fusão de *macrófagos* ativados por interferon-gama, sem participação de vírus, e aparece onde o organismo tenta murar um agente que não consegue digerir. Ler um sincício como granuloma inverte o mecanismo, o agente e o significado do achado.
])

A #termo-nota[coilocitose][alteração da célula escamosa infectada pelo papilomavírus, com halo claro amplo em torno do núcleo e núcleo aumentado, hipercromático e de contorno irregular] tem outra origem. O #sigla("HPV", [papilomavírus humano]) expressa a proteína E4, que desmonta a rede de filamentos de queratina disposta em torno do núcleo. Sem esse arcabouço, o citoplasma perinuclear colapsa e deixa a cavidade óptica que dá o nome à célula — um caso particular da despolimerização do citoesqueleto listada como efeito citopático em 1.1. O núcleo, em paralelo, aumenta, escurece e adquire contorno enrugado.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-08.png",
  largura: 52%,
  legenda: [Duas células centrais mostram o halo perinuclear nítido e núcleos escuros de contorno irregular — uma delas binucleada. Ao redor, células escamosas de citoplasma homogêneo servem de comparação.])

O coilócito marca *infecção produtiva*: o vírus está replicando e montando partículas nas camadas superficiais do epitélio escamoso, onde a célula já se diferenciou. Nas lesões de alto grau o quadro se inverte — o genoma viral tende a integrar-se ao da célula hospedeira, a produção de partículas cai e o coilócito rareia, enquanto a atipia nuclear e as mitoses em camadas altas aumentam. Encontrar coilócito é, portanto, evidência de infecção ativa, não medida de gravidade da lesão.

#mini-resumo[Sincício: proteína de fusão viral na membrana → citoplasmas unidos → propagação sem passar pelo meio extracelular. Coilócito: E4 do HPV desmonta a queratina perinuclear → halo → assinatura de infecção produtiva.]

#parte-title("PARTE II — A resposta do hospedeiro esculpe a lesão")

#subtopico("2.1 — A cronologia da resposta e o infiltrado que ela deixa")

Os efeitos da PARTE I explicam o que acontece dentro de uma célula infectada. Não explicam o campo inteiro que o patologista examina — as células mortas onde nenhum vírus foi detectado, e o infiltrado que ocupa o tecido dias depois. Esse segundo andar da lesão é obra da resposta imune, e ela obedece a um cronograma.

Nos primeiros dias a defesa é *inata*: barreiras epiteliais, células #sigla("NK", [natural killer — linfócito da imunidade inata capaz de matar célula alterada sem reconhecimento de antígeno específico]) e macrófagos, e o sistema complemento. O #sigla("IFN", [interferon — citocina que instala nas células vizinhas um programa de resistência à replicação viral]) tipo I aparece já no primeiro dia e atinge o pico por volta do terceiro ou quarto; a atividade das células NK acompanha, entre o terceiro e o sétimo dia. É essa dupla que derruba a curva de carga viral antes que qualquer resposta específica esteja pronta.

A resposta *adaptativa* ocupa o segundo tempo. Os linfócitos T efetores só chegam ao pico em torno do décimo dia — o intervalo é o tempo de apresentação do antígeno no linfonodo, expansão clonal e migração para o tecido. Os anticorpos sobem depois deles e permanecem em platô por semanas a anos. A leitura clínica desse deslocamento é direta: quadros agudos são governados pela resposta inata, quadros sub-agudos e crônicos exibem a assinatura da resposta adaptativa.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-10.png",
  largura: 74%,
  legenda: [A carga viral já está caindo quando os linfócitos T chegam, e despenca antes de o anticorpo subir. Quem contém a fase inicial é o interferon com a célula NK; o anticorpo chega para neutralizar partícula livre e impedir a reinfecção.])

A ordem das chegadas determina a composição do infiltrado, e é aqui que a cronologia vira morfologia. O neutrófilo é recrutado por interleucina-8, liberada por macrófago que reconheceu sinal de perigo — o cenário da lise maciça de 1.1 e da infecção bacteriana extracelular. Já o interferon tipo I induz outro conjunto de quimiocinas, a família CXCL9 a CXCL11, cujos receptores são expressos por linfócito T e célula NK. O tecido infectado por vírus, portanto, chama preferencialmente linfócito e macrófago, e o infiltrado *linfomononuclear* é a assinatura esperada da lesão viral estabelecida.

O complemento participa em duas janelas distintas. As vias alternativa e das lectinas operam desde as primeiras horas, opsonizando partículas virais e lisando vírus envelopados; a via clássica só entra depois, porque depende de anticorpo já formado. Depositar C3b sobre a partícula aumenta a fagocitose, mas não alcança o vírus que já está dentro da célula — limitação que devolve o problema às células citotóxicas.

#mini-resumo[Interferon e NK contêm a fase inicial e derrubam a carga viral; o linfócito T chega no décimo dia; o anticorpo, depois. Como o interferon recruta linfócito e não neutrófilo, o infiltrado da lesão viral é linfomononuclear.]

#subtopico("2.2 — Interferon tipo I: um estado celular, não uma citocina lítica")

O interferon tipo I reúne o *interferon-alfa* e o *interferon-beta*, citocinas que qualquer célula nucleada produz ao detectar replicação viral no próprio citoplasma. O gatilho é o RNA de fita dupla, intermediário obrigatório da replicação de muitos vírus e molécula ausente da célula sadia: receptores citosólicos da família RIG-I e o receptor TLR3, no endossomo, o reconhecem e ativam fatores de transcrição que ligam o gene do interferon.

A citocina liberada age sobre a própria célula e sobre as vizinhas, ligando-se ao receptor IFNAR e acionando a via JAK-STAT, que transcreve centenas de genes estimulados por interferon. Dois deles carregam o efeito antiviral central. A #sigla("PKR", [proteína-quinase R — enzima ativada por RNA de fita dupla que fosforila o fator de iniciação eIF2α e paralisa a tradução]) fosforila o fator de iniciação da tradução e a síntese proteica da célula para — a do vírus junto, porque ele depende do ribossomo do hospedeiro. A 2'-5'-oligoadenilato sintetase produz um segundo mensageiro que ativa a RNase L, endonuclease que degrada RNA mensageiro no citoplasma, viral e celular indistintamente.

O resultado é o que o esquema chama de *estado de resistência antiviral*: a célula vizinha, ainda não infectada, deixa de ser fábrica utilizável antes que o vírus chegue nela. Aqui se fecha o item "bloqueio de síntese proteica" da lista de 1.1 — parte dele é sabotagem viral, e parte é o hospedeiro desligando a própria linha de produção.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-11.png",
  largura: 66%,
  legenda: [A célula infectada, à esquerda, não se salva: ela sinaliza. O interferon que ela libera atinge a vizinha sadia, que passa a sintetizar proteína antiviral antes de qualquer contato com o vírus.])

O segundo braço do interferon é imunológico e tem custo. Ele aumenta a expressão do #sigla("MHC", [complexo principal de histocompatibilidade — conjunto de moléculas que exibem peptídeos na superfície celular para inspeção pelo linfócito T]) de classe I, o que amplia a exibição de peptídeos virais na superfície e torna a célula infectada *mais* visível ao linfócito T citotóxico. E ativa NK, linfócito T citotóxico e macrófago. Aumentar a apresentação não protege a célula — condena-a com mais eficiência, em benefício do tecido.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-12.png",
  largura: 62%,
  legenda: [A célula do centro, infectada, exporta interferon nas duas direções. As laterais entram em estado de resistência e sobem MHC de classe I; abaixo, o mesmo sinal ativa NK, linfócito T citotóxico e macrófago.])

#atencao-box("O interferon não ataca o vírus", [
A palavra "antiviral" leva o aluno a imaginar uma molécula que destrói partículas, como um antibiótico destrói bactéria. O interferon nunca toca no vírus. Ele altera a *célula*: paralisa a tradução pela proteína-quinase R, degrada RNA mensageiro pela RNase L e eleva o MHC de classe I. A consequência prática dessa distinção aparece na clínica — o mal-estar, a febre e a mialgia da fase aguda de uma virose são efeitos do interferon sobre o organismo, não do vírus sobre os músculos.
])

#subtopico("2.3 — NK e linfócito T CD8: matar a célula infectada é a lesão")

A necrose que o patologista descreve na biópsia de uma hepatite não foi produzida pelo vírus. Foi produzida pelo linfócito que reconheceu o hepatócito infectado e o executou — e admitir isso reorganiza a leitura de toda lesão viral.

A célula NK decide sem conhecer o antígeno. Ela não possui receptor antígeno-específico; integra dois sinais opostos. O receptor ativador, NKG2D, lê ligantes de estresse, como as moléculas MICA e MICB, que a célula infectada ou transformada passa a expor. O receptor inibitório, da família #sigla("KIR", [receptor semelhante a imunoglobulina da célula killer — família de receptores inibitórios que leem MHC de classe I na célula-alvo]), lê MHC de classe I: encontrando-o em quantidade normal, cancela a ordem de matar. A morte ocorre quando o sinal ativador está presente e o inibitório ausente — princípio conhecido como #termo-nota[missing self][reconhecimento da ausência: a célula NK executa a célula que deixou de exibir MHC de classe I em quantidade normal, sem precisar identificar o que a alterou].

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-13.png",
  largura: 64%,
  legenda: [À esquerda, os dois receptores encontram seus ligantes e o sinal inibitório vence: a célula normal é poupada. À direita, falta o MHC de classe I, o freio some e sobra apenas o sinal ativador.])

Essa arquitetura fecha uma armadilha sobre o vírus. Reduzir o MHC de classe I é a estratégia clássica de escape do linfócito T citotóxico — sem peptídeo exibido, não há reconhecimento. Mas a mesma redução remove o freio da NK, que passa a matar a célula justamente por ela ter ficado silenciosa. O vírus escolhe entre ser visto pelo linfócito ou ser denunciado pela ausência.

O linfócito T #sigla("CD8", [marcador de superfície do linfócito T citotóxico, que se liga ao MHC de classe I e restringe o reconhecimento a peptídeos apresentados nessa molécula]) resolve o mesmo problema pelo caminho oposto, com especificidade. Seu receptor reconhece um peptídeo viral específico apresentado em MHC de classe I, e o reconhecimento exige que a célula já tenha sido ativada no linfonodo — o que explica o atraso de dias documentado em 2.1.

A maquinaria letal, no entanto, é a mesma nos dois. A *perforina* polimeriza na membrana da célula-alvo e abre a via de entrada; a *granzima*, protease que penetra por ela, cliva e ativa caspases no citoplasma do alvo. Em paralelo, o ligante de Fas na superfície do linfócito engata o receptor Fas do alvo e dispara a mesma cascata. O desfecho é apoptose, não lise: a célula morre empacotada, sem liberar vírions viáveis nem sinal de perigo — o organismo escolhe o modo de morte que menos dissemina.

#mini-resumo[NK mata por ausência de MHC-I; CD8 mata por presença de peptídeo em MHC-I. A maquinaria é a mesma — perforina abre, granzima ativa caspases — e o desfecho é apoptose, porque lisar espalharia vírus viável.]

Daqui decorre o princípio que governa a PARTE III: em vírus pouco citopático, *a extensão da lesão tecidual mede a intensidade da resposta, não a carga viral*. Uma resposta vigorosa elimina o vírus e destrói muito parênquima no processo; uma resposta fraca preserva o tecido e deixa a infecção persistir.

#parte-title("PARTE III — Hepatite viral: a combinação de tudo num órgão")

#subtopico("3.1 — O vírus B dentro do hepatócito")

O princípio que fecha a PARTE II tem no #sigla("HBV", [vírus da hepatite B]) seu exemplo mais limpo, porque este vírus praticamente não mata a célula que ocupa. A partícula carrega um DNA circular parcialmente dupla-fita e replica por transcrição reversa de um RNA intermediário — combinação incomum que a classificação de Baltimore reserva ao grupo VII.

O nucleocapsídeo levado ao núcleo entrega ali seu genoma, que é reparado e fechado no #termo-nota[cccDNA][DNA circular covalentemente fechado — forma epissomal e estável do genoma do vírus B, que funciona como minicromossomo no núcleo do hepatócito], molde de todas as transcrições subsequentes. Ele não se integra ao genoma da célula e não é alcançado pelos antivirais que inibem a polimerase viral, e é essa dupla propriedade que explica a persistência da infecção e a reativação sob imunossupressão.

A partir do cccDNA a célula transcreve um RNA pré-genômico, que é empacotado num capsídeo novo junto com a polimerase viral. Dentro desse capsídeo ocorre a transcrição reversa, e o genoma de DNA recém-formado segue um de dois caminhos: retorna ao núcleo, ampliando o reservatório de cccDNA, ou brota pelo retículo endoplasmático, onde adquire o envelope.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-15.png",
  largura: 60%,
  legenda: [A seta tracejada de reciclagem é a que sustenta a cronicidade: parte dos capsídeos novos volta ao núcleo em vez de sair da célula, e reabastece o molde que nenhum antiviral remove.])

O envelope é feito do #sigla("HBsAg", [antígeno de superfície do vírus B — proteína do envelope, produzida em enorme excesso e detectável no soro]), e o hepatócito o produz em quantidade muitas vezes superior à necessária para montar partículas completas. O excedente sai na circulação como partículas subvirais vazias e, dentro da célula, acumula-se nas cisternas do retículo endoplasmático liso. O citoplasma assume então aspecto homogêneo, finamente granular e eosinofílico, com um halo claro separando essa massa da membrana: é o #termo-nota[hepatócito em vidro fosco][hepatócito de citoplasma homogêneo e opaco, repleto de antígeno de superfície acumulado no retículo endoplasmático liso, característico do portador crônico do vírus B]. Trata-se do item "acúmulo de componentes virais" da lista de 1.1, materializado num órgão.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-16.png",
  largura: 46%,
  legenda: [A seta aponta um hepatócito de citoplasma opaco e uniforme, sem a granulação grosseira dos vizinhos. O halo claro periférico é o artefato de retração que separa a massa acumulada da membrana.])

#figura-lateral("/figuras/pat-09-patologia-infeccao-viral/slide-17.png",
  lado: "right",
  largura-figura: 36%,
  texto: [A #sigla("IHQ", [imuno-histoquímica — técnica que localiza um antígeno no tecido usando anticorpo marcado, revelado como precipitado castanho]) mostra em que compartimento cada antígeno viral está, e o compartimento informa a fase da infecção. O antígeno de superfície aparece marcado no *citoplasma e na membrana* do hepatócito, coerente com sua rota pelo retículo endoplasmático. Já o #sigla("HBcAg", [antígeno do core do vírus B — proteína do capsídeo, marcador de replicação ativa quando detectada no núcleo do hepatócito]) marca o *núcleo*, onde o capsídeo se monta sobre o RNA pré-genômico — e núcleo positivo significa replicação em curso.],
  legenda: [Antígeno de superfície: marcação citoplasmática.])

#confusao-prevista(
  titulo: "Vidro fosco não é sinal de replicação intensa",
  aluno_acha: [muito antígeno acumulado deveria significar muito vírus sendo produzido],
  mecanismo: [o vidro fosco é acúmulo de *envelope*, e o envelope é fabricado em excesso independentemente de quantas partículas completas se montam. Ele caracteriza o portador crônico, em que a produção de antígeno de superfície segue alta e a replicação pode estar baixa. Replicação ativa se marca de outro jeito: antígeno do core positivo dentro do núcleo do hepatócito.],
)

#subtopico("3.2 — Ler a lesão hepatocitária: necrose e apoptose")

Reconhecer lesão exige a referência do normal. No fígado sadio, o espaço porta reúne ramo da veia porta, ramo da artéria hepática e ducto biliar, e é delimitado pela *placa limitante*, a fileira de hepatócitos que faz a fronteira com o parênquima. Dali os cordões de hepatócitos se irradiam até a veia centrolobular, separados por sinusoides. O oxigênio cai ao longo desse trajeto, e por isso a zona 1, periportal, é a mais bem oxigenada, e a zona 3, centrolobular, a mais vulnerável à hipóxia.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-20.png",
  largura: 52%,
  legenda: [Os números marcam as três zonas, do espaço porta à veia centrolobular. Na hepatite viral crônica o epicentro da agressão é o extremo 1 desse eixo, junto à placa limitante — o oposto do que ocorre na lesão isquêmica ou tóxica.])

A morte por necrose deixa um vazio. O hepatócito lisado desaparece e no seu lugar fica um agregado de macrófagos e linfócitos, de modo que a lesão é lida pela *ausência* de célula, não pela presença de célula morta — padrão descrito como necrose lítica focal quando ocorre em pontos dispersos pelo lóbulo. Focos maiores podem confluir e ligar espaços porta entre si ou a veias centrolobulares, e essa confluência recebe o nome de necrose em ponte, marcador de agressão grave.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-22.png",
  largura: 43%,
  legenda: [No centro, um agrupamento denso de células inflamatórias ocupa o espaço onde havia hepatócitos. O que identifica a necrose é a interrupção do cordão, não uma célula morta reconhecível.])

A morte por apoptose deixa o oposto: uma célula isolada, retraída, de citoplasma intensamente eosinofílico e núcleo picnótico ou já ausente, sem infiltrado ao seu redor. É o #termo-nota[corpúsculo acidófilo][hepatócito apoptótico isolado, arredondado, de citoplasma fortemente eosinofílico e núcleo picnótico ou ausente; também chamado corpúsculo de Councilman], e ele é a tradução morfológica da execução por linfócito T CD8 descrita em 2.3 — perforina, granzima, caspases, membrana preservada. A ausência de inflamação ao redor não é detalhe estético: é a consequência de a célula ter morrido sem vazar conteúdo, exatamente como previsto em 1.1.

#figura-lateral("/figuras/pat-09-patologia-infeccao-viral/slide-24.png",
  lado: "left",
  largura-figura: 36%,
  texto: [Distinguir os dois padrões muda a interpretação do caso. Necrose lítica extensa aponta agressão intensa e aguda, com risco de insuficiência hepática. Corpúsculos acidófilos dispersos apontam citotoxicidade linfocitária dirigida, célula a célula — o padrão da hepatite crônica em atividade. Uma terceira alteração completa o repertório: a *degeneração hidrópica*, ou balonização, em que o hepatócito incha por influxo de água após falha das bombas de membrana. Ela é reversível e, sendo aumento de volume, é o oposto morfológico da retração apoptótica.],
  legenda: [Corpúsculo acidófilo: uma célula, sem infiltrado.])

#clinica-box("Hepatite fulminante: quando a resposta é rápida demais", [
A insuficiência hepática aguda por hepatite viral acomete justamente pacientes com resposta imune vigorosa, e não os mais imunodeprimidos. Uma população grande de linfócitos T CD8 específicos alcança o fígado num intervalo curto e executa hepatócitos em massa; a necrose confluente destrói a maior parte do parênquima antes que a regeneração compense, e instalam-se icterícia intensa, coagulopatia por queda dos fatores de coagulação e encefalopatia por amônia não depurada.

O corolário incomoda e é verdadeiro: reduzir a carga viral não seria, nesse cenário, a intervenção que salva o fígado. O paciente sob imunossupressão profunda tende ao extremo oposto — replica muito vírus, exibe pouca inflamação na biópsia e mantém transaminases próximas do normal, porque falta o efetor que produziria a lesão.
])

#subtopico("3.3 — Do infiltrado à cirrose: quando a resposta vira arquitetura")

A cronicidade transforma o problema: a lesão deixa de ser contada em células e passa a ser contada em arquitetura. O infiltrado que se instala não se distribui ao acaso, e sua topografia reproduz a divisão de trabalho da PARTE II.

O linfócito B se concentra no espaço porta, formando agregados densos que podem organizar-se em folículo linfoide com centro germinativo — estrutura de tecido linfoide construída dentro do órgão agredido, onde não existia. O linfócito T CD8, ao contrário, dispersa-se pelo lóbulo, entre os cordões, porque é lá que estão os hepatócitos que exibem peptídeo viral em MHC de classe I. A posição segue a função: o linfócito B precisa de estrutura organizada para expandir e produzir anticorpo; o CD8 precisa de contato célula a célula com o alvo.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-27.png",
  largura: 54%,
  legenda: [A marcação para CD8 sai do espaço porta e invade o parênquima. Cada célula marcada ao lado de um cordão de hepatócitos é um efetor em posição de execução.])

Onde o linfócito T CD8 atravessa a placa limitante e mata hepatócitos na borda do espaço porta, instala-se a #termo-nota[necrose de interface][destruição de hepatócitos na fronteira entre o espaço porta e o parênquima, com rompimento da placa limitante pelo infiltrado inflamatório; marcador morfológico de atividade na hepatite crônica]. Ela é o motor da progressão, porque agride repetidamente a mesma região e mantém ali um estímulo permanente de reparo.

Esse estímulo é recolhido pela #termo-nota[célula estrelada][célula perissinusoidal que armazena vitamina A no fígado normal e, quando ativada, transdiferencia-se em miofibroblasto produtor de colágeno], residente do espaço de Disse. Ativada por fator de crescimento transformador beta liberado por macrófagos e por produtos de hepatócitos lesados, ela perde os depósitos lipídicos, converte-se em miofibroblasto e passa a depositar colágeno tipo I no espaço perissinusoidal. O sinusoide, que era um capilar fenestrado permitindo troca direta com o hepatócito, ganha membrana basal e perde as fenestras — processo de capilarização que compromete a troca antes de qualquer nódulo existir.

O colágeno depositado a partir dos espaços porta forma septos que ligam espaço porta a espaço porta e espaço porta a veia centrolobular. Entre os septos, os hepatócitos remanescentes proliferam e formam *nódulos de regeneração*. A combinação de septos fibrosos difusos e nódulos regenerativos por todo o órgão define a *cirrose*; a impregnação por prata revela a trama de reticulina distorcida e o tricrômio cora em azul o colágeno dos septos.

#figura-nebli("/figuras/pat-09-patologia-infeccao-viral/slide-29.png",
  largura: 54%,
  legenda: [Os septos corados em azul isolam nódulos de hepatócitos. Repare que os nódulos não têm veia centrolobular no centro nem espaço porta na periferia — a relação entre célula, sinusoide e canalículo biliar foi perdida, e é essa perda que a massa regenerada não recupera.])

#clinica-box("Do vírus B ao carcinoma hepatocelular", [
A hepatite crônica pelo vírus B eleva o risco de carcinoma hepatocelular por três mecanismos somados. O ciclo de necrose e regeneração mantém hepatócitos em divisão por décadas, e cada divisão é oportunidade de mutação não reparada. A inflamação crônica fornece espécies reativas de oxigênio e nitrogênio, que lesam o DNA diretamente. E fragmentos do genoma viral se integram ao DNA do hepatócito, desregulando genes vizinhos e mantendo a expressão da proteína viral X, que interfere no controle do ciclo celular.

Daí a distinção prática: no vírus C e no álcool o carcinoma surge quase sempre sobre fígado já cirrótico, enquanto no vírus B pode aparecer *antes* da cirrose, porque a integração atua por via independente da fibrose — e por isso o portador crônico do vírus B é rastreado mesmo sem cirrose estabelecida.
])

#conclusao-box[
Um princípio único organiza a aula inteira: *o que se vê no tecido é a soma do que o vírus faz com a célula e do que o organismo faz com a célula infectada*. Nenhuma das duas metades explica sozinha uma lâmina de infecção viral.

O mecanismo nuclear que sustenta esse princípio é a economia de sinais. A lise vaza conteúdo e chama neutrófilo; a apoptose empacota e não chama ninguém; o interferon não toca no vírus, mas paralisa a tradução da célula vizinha e eleva o MHC de classe I, expondo o alvo; a célula NK lê a ausência desse MHC e o linfócito T CD8 lê a presença do peptídeo — e ambos matam por perforina e granzima, produzindo apoptose. Cada achado morfológico da aula é o registro visível de um desses passos: a inclusão marca o compartimento de montagem, o sincício marca a proteína de fusão, o coilócito marca a queratina desmontada, o vidro fosco marca o antígeno acumulado, o corpúsculo acidófilo marca a execução linfocitária.

A hepatite pelo vírus B mostra o preço dessa aritmética. Quem mata o hepatócito é o linfócito, e a intensidade da lesão acompanha o vigor da resposta: resposta explosiva dá necrose confluente e insuficiência aguda; resposta insuficiente dá replicação persistente com biópsia quase limpa; resposta intermediária e prolongada dá o pior desfecho estrutural, porque sustenta a necrose de interface que ativa a célula estrelada.

O raciocínio se estende adiante: a inflamação que não resolve e o reparo que a acompanha são o tema seguinte, e nele a cirrose deixa de ser desfecho de uma infecção específica para virar o exemplo geral do tecido obrigado a reparar-se sob agressão que não cessa.
]
