#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
A patologia do útero junta dois territórios histológicos diferentes — corpo (endométrio glandular e miométrio liso) e colo (epitélio escamoso do ectocérvice encontrando o cilíndrico do endocérvice na #sigla("JEC", [junção escamo-colunar])) — e dois mecanismos oncogênicos que se comportam como linhas paralelas. No corpo, estrogênio sem oposição estimula o endométrio, instala hiperplasia, abre porta para o carcinoma endometrioide (tipo I). No colo, o #sigla("HPV", [papilomavírus humano]) de alto risco integra DNA viral no epitélio metaplásico da zona de transformação, despeja E6 e E7 sobre p53 e Rb, transforma displasia em carcinoma escamoso invasor. O patologista é quem traduz esses processos: recebe peças que vão da biópsia de poucos milímetros à histerectomia radical, descreve macro e micro, e devolve ao clínico o diagnóstico que decide conduta. Este resumo segue exatamente esse fluxo — primeiro como a peça chega e como se descreve, depois o que se vê no corpo, finalmente o que se vê no colo.
]

#parte-title("PARTE I — Como a peça uterina chega ao patologista", primeira: true)

#subtopico("1.1 — Procedimentos cirúrgicos do útero")

O útero é abordado cirurgicamente por três grandes motivos: diagnosticar lesão suspeita, tratar doença benigna e ressecar neoplasia maligna. Cada motivo gera um tipo de peça com características próprias, e o patologista precisa saber qual a indicação para entender o que está recebendo. Procedimentos diagnósticos coletam fragmentos pequenos — uma #termo-nota[biópsia endometrial][fragmento obtido por cureta ou pipelle, alguns milímetros, fixado em formol] mede poucos milímetros e busca confirmar hipóteses de hiperplasia ou carcinoma; a #termo-nota[histeroscopia diagnóstica][visualização direta da cavidade com câmera, permite biópsia dirigida] orienta a biópsia para a área suspeita. Procedimentos de rastreio são feitos no colo: o citopatológico cervical (Papanicolau) raspa células do ectocérvice e do endocérvice, e a colposcopia avalia a superfície com ácido acético e lugol. Não geram peça maciça — geram lâmina ou pequena biópsia.

O grupo terapêutico ressecativo amplia a escala. A #sigla("EZT", [exérese da zona de transformação]) — também chamada de #termo-nota[LEEP][loop electrosurgical excision procedure, alça diatérmica] — retira a faixa epitelial onde JEC e metaplasia coexistem, num cone raso de alguns milímetros de profundidade. A conização propriamente dita aprofunda o cone (até 2 cm) para alcançar lesão endocervical alta. A polipectomia retira lesão pediculada da cavidade. Quando a doença é miometrial, a miomectomia retira o nódulo de leiomioma preservando o útero — opção da paciente que quer manter fertilidade. Quando o útero inteiro precisa sair, entra a família das histerectomias. A histerectomia total retira corpo e colo; a subtotal preserva colo; a vaginal usa via baixa; a laparoscópica é minimamente invasiva. A histerectomia radical, indicação oncológica, amplia a ressecção para paramétrios e terço superior da vagina, frequentemente acompanhada de linfadenectomia pélvica. A traquelectomia, mais rara, retira apenas o colo preservando o corpo para pacientes jovens com tumor inicial que ainda querem engravidar.

#mini-resumo[Procedimento diagnóstico = peça pequena, foco em confirmar hipótese. Procedimento terapêutico = peça intermediária (mioma, pólipo, cone). Procedimento oncológico = peça grande, com margens e linfonodos, foco em estadiar.]

#figura-nebli(
  "/figuras/patologia-utero/img-p004-01.jpeg",
  largura: 60%,
  legenda: [Peça A — útero retirado por histerectomia total. Macroscopia mostra abaulamento miometrial irregular, padrão típico de leiomiomatose. A peça chega ao patologista intacta, com colo preservado para descrição da JEC.]
)

#subtopico("1.2 — Protocolo de envio e fixação")

O que define se o patologista vai conseguir trabalhar é o que acontece nos primeiros minutos depois da peça sair do campo. Tecido vivo sem fixação entra em #termo-nota[autólise][autodigestão por enzimas próprias da célula liberadas no pós-mortem tecidual] em questão de horas — núcleos picnóticos, citoplasma esfumaçado, epitélio descolado da membrana basal. Resultado prático: a lâmina perde a arquitetura que daria o diagnóstico. O fixador-padrão é o formol tamponado a 10%, em volume igual a dez vezes o volume da peça. Volume menor não penetra; tampão errado precipita pigmento de formol.

Antes de mergulhar no formol, peças grandes — útero inteiro, cone profundo — precisam ser abertas. Útero fechado é uma cavidade selada onde o fixador não chega ao endométrio em tempo útil; o patologista corta o útero ao longo do eixo crânio-caudal, separando parede anterior de posterior, e expõe a cavidade ao fixador. Cone cervical exige orientação espacial preservada — pontos cardeais (12h, 3h, 6h, 9h) marcados com fio cirúrgico pelo ginecologista antes do envio. Sem essa marcação, o patologista não consegue dizer onde estava a margem positiva, e o cirurgião não sabe onde reampliar.

O tempo de fixação importa: 24 a 48 horas para histerectomia, 12 horas para biópsia pequena. Fixação curta deixa o centro da peça mole e mal preservado; fixação muito longa endurece demais e prejudica corte em micrótomo, além de mascarar antígenos para imuno-histoquímica. Estudos moleculares (#sigla("IHQ", [imuno-histoquímica]), painel de p53, p16, receptores hormonais) dependem de fixação adequada — se a célula autolisou antes de fixar, nenhum anticorpo recupera o sinal.

#atencao-box("Erro de fixação não tem volta",
  [Peça enviada a seco, ou em formol diluído, ou fechada sem abrir — o tecido autolisa nas primeiras horas e o diagnóstico se torna inviável. Não existe técnica de salvamento. Numa peça oncológica isso significa repetir cirurgia ou aceitar laudo inconclusivo. O patologista deve recusar peça mal fixada e devolver protocolo escrito ao bloco cirúrgico.]
)

#subtopico("1.3 — Descrição macroscópica orientada")

A descrição macroscópica não é livre — segue protocolo. O patologista anota peso, dimensões nos três eixos, abertura da peça, aspecto da serosa, espessura do miométrio, dimensões da cavidade, aspecto do endométrio, dimensões do colo, características da JEC e do orifício externo, presença de lesões e suas relações com as referências anatômicas. Cada item dessa lista vira frase no laudo, e cada frase tem papel na decisão clínica seguinte.

Pesar a peça importa porque o útero hipertrofiado por leiomiomatose pode passar de 500 g (normal 60–90 g) e essa massa contribui para sintomatologia compressiva. Medir nos três eixos (longitudinal, transversal, ântero-posterior) permite comparar com imagem pré-operatória e calcular volume. Avaliar serosa procura aderências, implantes de #termo-nota[endometriose][endométrio funcional fora da cavidade, sangra ciclicamente] e nódulos suspeitos. Abrir o útero pelo plano sagital expõe a cavidade, e aí entra a parte mais informativa: o endométrio normal pós-menopausa é fino (menos de 5 mm), pálido, atrófico; o endométrio hiperplásico é espesso, polipoide, às vezes com pólipos discretos; o endométrio neoplásico é massa irregular, ulcerada, friável, invadindo miométrio.

#clinica-box("Por que abrir o útero antes de fixar muda o laudo",
  [Útero fechado em formol mantém apenas a superfície externa bem fixada — o endométrio fica autolisado. Quando o patologista abre tarde, perde a arquitetura glandular justamente onde o diagnóstico mora. Por isso o protocolo manda abrir na hora do recebimento, mesmo que isso atrase o macro descritivo. Em peça oncológica essa antecipação é a diferença entre laudo "hiperplasia atípica" e laudo "carcinoma endometrioide grau 2 com invasão miometrial menor que 50%".]
)

O colo é descrito separadamente: comprimento, diâmetro do orifício externo, posição da JEC (ectocervical, no orifício, intracervical), presença de lesão vegetante, ulcerada ou infiltrativa, características da mucosa adjacente. Quando há lesão suspeita, fotografar antes de seccionar — fotografia macro vira referência no laudo e na discussão multidisciplinar.

A amostragem (retirada de fragmentos para microscopia) segue regra simples: amostrar onde mais provavelmente está a doença e onde a doença muda o estadiamento. Em útero com lesão endometrial focal, amostrar a lesão inteira mais a transição lesão-normal e a parede oposta. Em cone cervical, amostrar todo o cone em fatias seriadas perpendiculares ao eixo longitudinal — só assim se verifica se a margem profunda está livre. Em histerectomia radical por câncer de colo, amostrar paramétrios em sua totalidade e linfonodos um a um.

#figura-nebli(
  "/figuras/patologia-utero/img-p025-01.jpeg",
  largura: 70%,
  legenda: [Peça G — esquema de amostragem do útero. Numerais indicam fragmentos retirados em locais estratégicos: lesão endometrial, transição lesão-normal, parede oposta, miométrio profundo, colo. Cada fragmento vira bloco em parafina e lâmina em HE.]
)

#parte-title("PARTE II — Patologia do corpo uterino")

#subtopico("2.1 — Leiomioma e adenomiose")

O #termo-nota[leiomioma][tumor benigno de músculo liso, monoclonal, hormônio-sensível] é o tumor uterino mais frequente — está em algum grau em 70% das mulheres acima de 50 anos. Cresce a partir de uma única célula muscular lisa do miométrio que perde controle de proliferação por mutação somática (frequentemente em MED12, mediador de transcrição). Hormônio-dependente, expande na menacme, estabiliza ou regride na pós-menopausa. Macroscopicamente o leiomioma é nódulo bem delimitado, branco-acinzentado, de aspecto rodopiado quando seccionado, firme à palpação, sem cápsula verdadeira (a pseudocápsula é tecido miometrial comprimido). Tamanho de poucos milímetros a tumores que distorcem todo o útero.

A localização classifica o leiomioma e prediz sintoma. Leiomioma subseroso projeta-se para a serosa, costuma ser assintomático mas pode pediculizar e torcer. Leiomioma intramural fica dentro do miométrio, é o mais comum, e quando volumoso aumenta o útero, comprime estruturas vizinhas e gera dismenorreia. Leiomioma submucoso projeta-se para a cavidade endometrial, distorce o endométrio, é o que mais sangra — sangramento uterino anormal é a clínica que leva ao diagnóstico. Microscopicamente, fibras musculares lisas alongadas, fusiformes, com núcleos cigarroides, agrupadas em fascículos entrelaçados, sem atipia, mitoses raras (menos de 5 por 10 campos de grande aumento). Vasos de paredes espessas. Áreas de degeneração hialina, mixoide ou hemorrágica são comuns em tumores grandes — não significam malignidade.

#confusao-prevista(
  titulo: "Leiomioma vs. leiomiossarcoma",
  aluno_acha: [Que qualquer tumor de músculo liso no útero pode ser benigno ou maligno, e que a diferença está no tamanho.],
  mecanismo: [Tamanho isolado não distingue. O critério histológico vence: leiomiossarcoma tem atipia citológica significativa + necrose tumoral coagulativa (não hemorrágica) + mais de 10 mitoses por 10 campos de grande aumento. Os três critérios juntos. Leiomioma pode ser enorme e degenerar sem nunca virar sarcoma. Sarcoma é raro (menos de 1% dos tumores miometriais) e surge de novo, não da transformação de leiomioma.]
)

A #termo-nota[adenomiose][presença de endométrio ectópico dentro do miométrio, com hipertrofia muscular ao redor] compartilha localização com leiomioma mas tem mecanismo diferente. Glândulas endometriais e estroma se aprofundam no miométrio (mais de 2,5 mm abaixo da junção endomio-miometrial), e o miométrio reage com hipertrofia muscular ao redor desses focos. Resultado macroscópico: útero globoso, aumentado, parede miometrial espessada de modo difuso (raramente nodular), com pequenos focos hemorrágicos puntiformes ao corte — sangue antigo dentro dos focos ectópicos. Microscopicamente, glândulas endometriais com estroma envolvente em meio a feixes musculares lisos hipertrofiados, longe da cavidade. Clinicamente: dismenorreia progressiva, menorragia, dor pélvica crônica.

#figura-nebli(
  "/figuras/patologia-utero/img-p011-01.jpeg",
  largura: 75%,
  legenda: [Peça B — micro do endométrio normal proliferativo. Glândulas tubulares retas, estroma celular denso, sem atipia. Padrão de referência para comparar com hiperplasia e carcinoma nas próximas peças.]
)

#subtopico("2.2 — Pólipos e hiperplasia endometrial")

O pólipo endometrial é uma projeção localizada da mucosa endometrial para dentro da cavidade, com pedículo vascular próprio. Origem: provável resposta focal e desregulada do endométrio ao estímulo estrogênico, com proliferação glandular sobre um eixo de estroma fibroso e vasos de parede espessa. Macroscopicamente: massa pediculada ou séssil, de poucos milímetros a vários centímetros, superfície lisa ou irregular, base estreita. Frequente em mulheres na perimenopausa e pós-menopausa. Histologicamente: glândulas endometriais de tamanhos e formas variados, frequentemente dilatadas, em estroma fibroso denso, com vasos centrais de parede espessada. Pode haver focos de metaplasia escamosa, ciliada ou tubária.

Pólipo geralmente é assintomático ou cursa com sangramento intermenstrual. Diagnóstico por histeroscopia + polipectomia. A questão clínica que importa: pólipo abriga hiperplasia ou carcinoma. A literatura mostra que em torno de 9% dos pólipos endometriais escondem alguma lesão proliferativa de risco — hiperplasia sem atipia, hiperplasia atípica ou carcinoma. Por isso polipectomia não é só alívio sintomático: é amostra obrigatória para histopatológico.

A #termo-nota[hiperplasia endometrial][proliferação anormal das glândulas endometriais por estímulo estrogênico sem oposição] resulta de exposição prolongada do endométrio a estrogênio sem progesterona contrabalançando. Causas: anovulação crônica (síndrome dos ovários policísticos), obesidade (tecido adiposo converte androgênio em estrogênio via aromatase), tumores ovarianos secretores, terapia de reposição com estrogênio isolado, tamoxifeno. O endométrio responde ao estímulo proliferando — glândulas mais numerosas, mais ramificadas, com epitélio pseudoestratificado.

A classificação atual da OMS separa em apenas duas categorias com base em atipia citológica: hiperplasia sem atipia (anteriormente "simples" ou "complexa sem atipia") e hiperplasia atípica, sinônimo de #sigla("NIE", [neoplasia intraepitelial endometrial]). O risco de progressão para carcinoma muda dramaticamente entre elas. Hiperplasia sem atipia regride em 80% dos casos com progesterona; risco de progressão para carcinoma é de 1 a 3%. Hiperplasia atípica ou NIE tem risco de carcinoma concomitante de até 40% na peça de histerectomia, e progressão sem tratamento próxima de 30%. Microscopicamente, a hiperplasia atípica mostra aglomerados glandulares com perda de polaridade, núcleos arredondados (perderam a forma tubular), nucléolos visíveis, cromatina aberta, citoplasma eosinofílico ou claro.

#atencao-box("Hiperplasia atípica é tratada como pré-câncer",
  [Diagnóstico de hiperplasia atípica em biópsia endometrial deve ser conduzido com histerectomia total com ou sem salpingo-oforectomia bilateral, preferencialmente laparoscópica. O motivo: até 40% das pacientes já têm carcinoma endometrioide oculto na peça definitiva. Tratamento conservador com progestágenos só em pacientes jovens, com desejo de fertilidade, com seguimento histológico rigoroso.]
)

#figura-nebli(
  "/figuras/patologia-utero/img-p013-01.jpeg",
  largura: 70%,
  legenda: [Micro de pólipo endometrial — glândulas variadas em tamanho e forma, estroma fibroso central, vasos de parede espessa. A literatura mostra que cerca de 9,5% dos pólipos abrigam hiperplasia ou carcinoma; daí a indicação obrigatória de exame histopatológico em toda polipectomia.]
)

#subtopico("2.3 — Carcinoma endometrial — tipos I e II")

O carcinoma de endométrio se divide classicamente em dois tipos com mecanismos, perfis moleculares e prognósticos distintos. O carcinoma tipo I — endometrioide — corresponde a 80 a 85% dos casos e nasce do eixo estrogênico que já discutimos: obesidade, anovulação, diabetes, hipertensão (a tríade da síndrome metabólica está presente em 80% das pacientes), terapia estrogênica isolada, menarca precoce e menopausa tardia. O fenótipo clínico clássico: mulher pós-menopausa, obesa, diabética, com sangramento vaginal anormal. Progride pelo continuum endométrio normal, hiperplasia sem atipia, hiperplasia atípica ou NIE, e finalmente carcinoma endometrioide bem diferenciado. Microscopicamente: glândulas semelhantes ao endométrio proliferativo, fundidas, com perda de estroma entre elas, atipia variável. Grau histológico de 1 a 3 baseado em arquitetura sólida e atipia nuclear.

Marcadores moleculares do tipo I: receptores de estrogênio e progesterona positivos (a doença é hormonalmente dirigida), mutações em PTEN, KRAS, beta-catenina, instabilidade de microssatélites. p53 selvagem (não mutado). Prognóstico globalmente bom: estádio I tem sobrevida em 5 anos próxima de 90%. Tratamento: histerectomia total com salpingo-oforectomia bilateral, mais linfadenectomia em casos selecionados; radioterapia adjuvante quando há invasão miometrial profunda ou invasão linfo-vascular.

O carcinoma tipo II — seroso, de células claras e indiferenciado — corresponde a 10 a 15% dos casos e tem mecanismo completamente diferente. Não nasce de hiperplasia, não é estrogênio-dependente, surge em endométrio atrófico de mulher mais idosa, magra, sem síndrome metabólica. Carcinoma seroso é o paradigma: mutação precoce em #termo-nota[TP53][gene supressor tumoral que codifica p53, guardião do genoma] gera lesão precursora chamada carcinoma intraepitelial seroso, e dali sai o carcinoma invasor com padrão papilar complexo, atipia nuclear marcada, mitoses abundantes, propensão precoce a disseminação peritoneal mesmo com invasão miometrial mínima. Marcadores: p53 com padrão aberrante (forte e difuso ou completamente nulo) na IHQ, p16 difusamente positivo, receptores hormonais geralmente negativos, frequentemente HER2 superexpresso.

#figura-nebli(
  "/figuras/patologia-utero/img-p029-01.jpeg",
  largura: 55%,
  legenda: [Hiperplasia endometrial — glândulas adensadas, irregulares, com diminuição do estroma. A tríade clínica das pacientes com hiperplasia ou carcinoma tipo I — obesidade, diabetes, hipertensão — está presente em cerca de 80% dos casos, somada a sangramento pós-menopausa.]
)

Prognóstico do tipo II é nitidamente pior: estádio I do carcinoma seroso tem sobrevida em 5 anos de 60 a 70%, e a doença frequentemente já se disseminou pela cavidade peritoneal ao diagnóstico, mesmo quando a invasão miometrial parece superficial. O tratamento adiciona quimioterapia sistêmica baseada em platina e taxano à cirurgia, e cada vez mais se investiga uso de anti-HER2 em casos selecionados.

#clinica-box("Por que importa distinguir os tipos no laudo",
  [O patologista que escreve "carcinoma endometrial G1" sem subtipar perde informação que muda conduta. Carcinoma endometrioide G1 estádio IA pede histerectomia mais observação. Carcinoma seroso aparentemente estádio IA pede histerectomia mais estadiamento peritoneal completo mais quimioterapia adjuvante. Por isso painel de IHQ (p53, p16, RE, RP, MMR) entrou na rotina do laudo, especialmente quando há atipia desproporcional ao grau arquitetural.]
)

#figura-nebli(
  "/figuras/patologia-utero/img-p031-01.jpeg",
  largura: 70%,
  legenda: [Histerectomia total — peça definitiva no manejo da hiperplasia atípica/NIE e do carcinoma endometrial. Macroscopia mostra cavidade aberta com lesão endometrial polipoide. Amostragem deve incluir a lesão, transição, miométrio profundo (para medir invasão), colo e anexos.]
)

#parte-title("PARTE III — Patologia do colo uterino")

#subtopico("3.1 — HPV, displasia e carcinoma in situ")

A história do câncer de colo é a história da infecção persistente por HPV de alto risco oncogênico. O HPV é um vírus DNA dupla-fita que infecta queratinócitos da camada basal do epitélio escamoso. A entrada no epitélio acontece através de microtraumas; o sítio mais vulnerável é a #termo-nota[zona de transformação][faixa de epitélio metaplásico onde o epitélio cilíndrico endocervical se transforma em escamoso após exposição ao pH ácido vaginal] do colo, exatamente onde a JEC fica. Metaplasia ativa significa células indiferenciadas em divisão, alvo perfeito para a integração viral.

Existem mais de 200 tipos de HPV; os de alto risco oncogênico — 16, 18, 31, 33, 35, 39, 45, 51, 52, 56, 58 e 59 — concentram 99% dos cânceres de colo. HPV 16 e 18 sozinhos respondem por aproximadamente 70%. Os de baixo risco (6, 11) causam condilomas, sem progressão para câncer. A diferença está nas oncoproteínas: E6 e E7 dos tipos de alto risco têm afinidade alta por p53 e Rb, respectivamente. E6 liga p53 e marca para degradação proteassomal — perda da apoptose por dano de DNA. E7 liga Rb hipofosforilado e libera E2F — passagem desregulada para fase S do ciclo. Resultado celular: proliferação aumentada, instabilidade genômica, acúmulo de mutações.

A infecção pode evoluir de três modos. Em 80 a 90% dos casos o sistema imune elimina o vírus em 1 a 2 anos sem lesão histológica relevante. Em uma fração menor a infecção persiste e gera lesão intraepitelial — primeiro de baixo grau, depois de alto grau. Em fração ainda menor (anos a décadas), a integração do DNA viral no genoma da célula hospedeira instala displasia progressiva até carcinoma in situ e invasor. Tempo médio do infectado ao invasor: 10 a 20 anos. Janela longa que justifica o rastreamento.

A microscopia da #termo-nota[neoplasia intraepitelial cervical][displasia escamosa do colo, gradada por extensão da imaturidade no epitélio] (#sigla("NIC", [neoplasia intraepitelial cervical])) tem nomenclatura dupla na prática brasileira: histológica em três graus (NIC I, II, III) e citológica em dois graus (#sigla("LSIL", [low-grade squamous intraepithelial lesion]) para NIC I e #sigla("HSIL", [high-grade squamous intraepithelial lesion]) para NIC II/III). O critério é a fração do epitélio ocupada por células imaturas (basaloides, com alta relação núcleo-citoplasma): NIC I até o terço inferior, NIC II até os dois terços, NIC III ocupa toda a espessura sem romper a membrana basal — sinônimo histológico de carcinoma in situ. NIC I, por ter maior probabilidade de regressão ou persistência do que de progressão, não é considerada lesão precursora; HSIL (NIC II/III) é o alvo do tratamento.

#figura-nebli(
  "/figuras/patologia-utero-caso/img-p097-04.jpeg",
  largura: 80%,
  legenda: [Microscopia da neoplasia intraepitelial cervical em três graus. LIEBG (NIC I) — proliferação de células imaturas restrita ao terço inferior mais coilocitose. LIEAG (NIC II/III) — proliferação que ocupa dois terços ou toda a espessura, perda da maturação, atipia nuclear.]
)

A #termo-nota[coilocitose][célula escamosa madura com halo perinuclear claro mais núcleo aumentado e hipercromático, marca citopática da infecção por HPV] é o achado citológico característico do efeito viral. Aparece em LSIL e em alguns HSIL. Marcador imuno-histoquímico complementar: p16 fortemente positivo em padrão difuso e em bloco indica displasia de alto grau (E7 do HPV inativa Rb, com acúmulo compensatório de p16). p16 focal ou ausente é mais a favor de processo reativo.

#confusao-prevista(
  titulo: "Coilocitose vs. atipia reativa",
  aluno_acha: [Que toda célula com halo perinuclear é coilocitose por HPV.],
  mecanismo: [Coilocitose verdadeira pede halo perinuclear bem definido mais núcleo aumentado, hipercromático, irregular, frequentemente binucleado. Inflamação simples (vaginite, cervicite) também produz halo perinuclear discreto, mas o núcleo permanece pequeno e regular. Quando há dúvida, IHQ para p16 desempata: positiva difusa indica displasia de alto grau; focal ou negativa indica reação inflamatória.]
)

#subtopico("3.2 — Carcinoma invasor e estadiamento TNM")

Quando a displasia rompe a membrana basal e células neoplásicas invadem o estroma cervical, instala-se o carcinoma invasor. O tipo histológico mais comum é o #termo-nota[carcinoma escamoso][neoplasia maligna do epitélio estratificado escamoso, com diferenciação escamosa por queratinização e pontes intercelulares] (75 a 80% dos cânceres de colo), originado da metaplasia escamosa da zona de transformação. O adenocarcinoma cervical (15 a 20%) origina-se do epitélio glandular endocervical e ganha relevância porque escapa mais frequentemente ao rastreio citológico (lesão alta, fora do alcance da espátula).

Clinicamente, a invasão se anuncia por sangramento. Os sintomas iniciais — sangramento vaginal pós-coito, sangramento intermenstrual, corrimento fétido, aumento do fluxo — refletem lesão exofítica, ulcerada, friável, que sangra ao toque. A doença avançada acrescenta dor pélvica persistente, lombalgia (invasão de paramétrios e plexos nervosos), perda de peso, fadiga. Sintomas por invasão local trazem hematúria quando o tumor invade bexiga, tenesmo e hematoquezia quando invade reto, fístulas vesicovaginais ou retovaginais em fase terminal.

O exame físico complementa. Toque vaginal e bimanual avaliam colo (endurecido, irregular, friável, com massa tumoral), mobilidade uterina e comprometimento de paramétrios (toque retal palpa o paramétrio através da parede retal e identifica fixação lateral). Exame especular visualiza lesão vegetante, ulcerada ou infiltrativa, e o sangramento ao toque já caracteriza friabilidade tumoral. Citologia é rastreio inicial; a confirmação diagnóstica vem da biópsia direcionada pela colposcopia, ou da conização quando a lesão é endocervical alta. Estadiamento por imagem: ressonância magnética para extensão local, tomografia para órgãos vizinhos e linfonodos, PET-CT para linfonodos a distância e metástases, cistoscopia e retossigmoidoscopia para investigar invasão de bexiga e reto (estádio IVA).

O estadiamento #sigla("TNM", [tumor, nódulos linfáticos, metástases]) do carcinoma de colo, em sua versão recente alinhada à FIGO, segue parâmetros anatômicos definidos. T1 é tumor confinado ao colo: T1a invasão microscópica, T1b lesão clinicamente visível, sempre confinada. T2 ultrapassa o colo: T2a invade vagina sem paramétrio, T2b invade paramétrio. T3 alcança parede pélvica ou terço inferior da vagina, podendo causar hidronefrose. T4 invade bexiga, reto ou ultrapassa a pelve. Linfonodos pélvicos comprometidos indicam N1; metástases a distância (linfonodos paraórticos, pulmão, osso) indicam M1.

#figura-nebli(
  "/figuras/patologia-utero/img-p036-01.jpeg",
  largura: 50%,
  legenda: [Peça I — estadiamento T do TNM cervical. T1 confinado ao colo; T2 invasão de paramétrio (T2b) ou vagina superior (T2a); T3 estende-se à parede pélvica ou ao terço inferior da vagina; T4 invasão de bexiga, reto ou disseminação para fora da pelve.]
)

A profundidade e a extensão lateral da invasão definem se o tumor é "microinvasivo" — invasão estromal menor que 3 mm de profundidade e menor que 7 mm de extensão lateral (T1a1) — ou francamente invasivo. Microinvasivo permite tratamento conservador (conização ampla com margens livres) em paciente que deseja fertilidade. Tumor maior ou com invasão linfo-vascular pede histerectomia radical com linfadenectomia ou quimiorradioterapia definitiva. A invasão linfo-vascular no laudo histológico é determinante: presença de células tumorais dentro de espaços linfáticos ou vasculares próximos ao tumor antecipa disseminação linfonodal e indica adjuvância.

#subtopico("3.3 — Resposta à radioterapia")

A radioterapia é pilar do tratamento do câncer de colo a partir do estádio IB2-IVA, geralmente em combinação com quimioterapia baseada em cisplatina (radiossensibilizador). Modalidade: teleterapia externa para a pelve (45 a 50 Gy) seguida de braquiterapia intracavitária (boost de 30 a 40 Gy no colo e paramétrios). A combinação se justifica porque o tumor é radio-responsivo, e a braquiterapia entrega dose alta na lesão preservando órgãos vizinhos.

A resposta histológica à radioterapia tem padrão característico que o patologista precisa reconhecer. Resposta completa: ausência de células tumorais viáveis na peça pós-tratamento; estroma fibrohialinizado, frequentemente com infiltrado linfocitário e células gigantes multinucleadas; cicatriz substituindo o tumor. Resposta parcial: ilhotas residuais de células tumorais, frequentemente com citoplasma volumoso e eosinofílico (efeito radio-induzido), núcleos bizarros — diferenciação aparente sem capacidade proliferativa. A graduação da resposta (sistema de Mandard ou variantes) influencia decisão sobre tratamento adicional.

#figura-nebli(
  "/figuras/patologia-utero/img-p040-01.jpeg",
  largura: 50%,
  legenda: [Peça J — colo pós-radioterapia. Macroscopia mostra retração e fibrose substituindo a lesão tumoral original. Microscopicamente, ausência de tumor viável com estroma hialinizado e atipia citopática rádio-induzida em células residuais sugere resposta completa ou quase completa.]
)

As complicações da radiopelviterapia desenham um espectro temporal. Agudas (durante e até 3 meses): cistite e proctite actínicas, com disúria, urgência, hematúria, tenesmo, diarreia mucossanguinolenta — resposta inflamatória aguda do epitélio vesical e retal à radiação. Subagudas (3 a 6 meses): epitelite vaginal, dispareunia, ressecamento. Tardias (anos): fibrose vaginal com estenose, fístulas vesico-vaginais e retovaginais (quadros graves, exigem reconstrução cirúrgica), estenose ureteral com hidronefrose, atrofia óssea pélvica com risco de fratura, segundo tumor radioinduzido. O patologista, recebendo peça pós-irradiação, descreve não só o tumor residual mas o grau de lesão actínica no tecido adjacente.

#mini-resumo[Carcinoma de colo é doença prevenível: HPV, displasia, in situ e invasor leva décadas. Rastreio (citologia ou DNA-HPV) intercepta a sequência. Diagnosticado em estádio inicial, conização cura. Diagnosticado tardio, exige radioquimioterapia com sequelas pélvicas frequentes.]

#clinica-box("Por que o eixo HPV-displasia importa no consultório",
  [A linha do tempo HPV, NIC III, invasor é o que justifica vacinação na infância (HPV 16/18 antes do início sexual), rastreio organizado (citologia trienal entre 25 e 64 anos pelas diretrizes de 2016; teste de DNA-HPV pelas novas diretrizes), tratamento de HSIL por EZT ou conização. Cada elo dessa cadeia foi planejado para quebrar a história natural antes do invasor.]
)

#conclusao-box[
Os dois eixos oncogênicos do útero correm em paralelo e não se cruzam. No corpo, estrogênio sem oposição empurra o endométrio por hiperplasia simples, hiperplasia atípica ou NIE, e finalmente carcinoma endometrioide tipo I — fenótipo de mulher pós-menopausa, obesa, diabética, hipertensa, com sangramento. Em uma minoria, mutação direta em TP53 instala carcinoma tipo II, agressivo, em endométrio atrófico. No colo, HPV de alto risco persistente integra DNA viral na zona de transformação, E6 e E7 destroem p53 e Rb, displasia progride por NIC I, NIC II/III, carcinoma in situ e invasor escamoso ao longo de 10 a 20 anos. A intervenção clínica espelha esse contraste: no corpo, suspeita-se na mulher com sangramento pós-menopausa e investiga-se com biópsia endometrial; no colo, rastreia-se sistematicamente toda mulher sexualmente ativa porque a janela longa permite interceptar a doença antes do invasor. O patologista, recebendo a peça, é quem confirma em qual ponto desses dois eixos a paciente está — e do laudo dele depende a conduta seguinte.
]
