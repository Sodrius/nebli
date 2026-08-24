#import "../typst-template/nebli_v2_apostila.typ": *

// ---------------------------------------------------------------
// Helpers locais de esquema (figuras nativas NEBLI).
// A aula chegou como transcrição integral, sem slides em imagem:
// as cadeias multi-passo ganham esquema construído em Typst.
// ---------------------------------------------------------------

#let esq-caixa(titulo, corpo, cor: navy, fundo: white) = box(
  fill: fundo,
  stroke: 0.8pt + cor,
  radius: 4pt,
  inset: (x: 6pt, y: 6pt),
  width: 100%,
  {
    set par(justify: false, leading: 4pt)
    set text(hyphenate: false)
    stack(
      spacing: 3pt,
      align(center, text(size: 8pt, font: titulo-fam, weight: 700, fill: cor, upper(titulo))),
      align(center, text(size: 7.6pt, fill: text-main, corpo)),
    )
  },
)

#let esq-seta = align(center + horizon, text(size: 13pt, fill: text-light, [→]))
#let esq-desce = align(center + horizon, text(size: 13pt, fill: text-light, [↓]))

#let esquema(corpo, legenda: none, largura: 100%) = figure(
  placement: auto,
  caption: none,
  numbering: none,
  supplement: none,
  block(
    breakable: false,
    width: largura,
    stack(
      block(
        width: 100%,
        fill: gray-bg,
        stroke: 0.6pt + gray-border,
        radius: 5pt,
        inset: 9pt,
        corpo,
      ),
      v(6pt),
      align(left, text(size: 9.5pt, style: "italic", fill: text-light, legenda)),
    ),
  ),
)

#let tabela-nebli(cabecalho, linhas, colunas: (1fr, 1fr, 1fr)) = block(
  breakable: false,
  width: 100%,
  table(
    columns: colunas,
    stroke: 0.5pt + gray-border,
    inset: (x: 7pt, y: 6pt),
    fill: (_, y) => if y == 0 { navy } else if calc.odd(y) { white } else { gray-bg },
    ..cabecalho.map(c => text(size: 8.5pt, font: titulo-fam, weight: 700, fill: white, c)),
    ..linhas.flatten().map(c => text(size: 8.6pt, c)),
  ),
)

#intro-box[
  Uma célula viva é um estado improvável mantido a peso de energia. Bombas seguram o sódio do lado de fora, o cálcio dentro de reservatórios fechados, a água em equilíbrio — e nada disso é gratuito: cada gradiente custa #sigla("ATP", [adenosina trifosfato — a moeda energética da célula]) por segundo. É por aí que começa toda a patologia. Quando um estímulo agride a célula, ela responde numa ordem previsível: primeiro tenta se adaptar, encontrando um novo ponto de equilíbrio; se o estímulo for rápido ou intenso demais para isso, sofre uma lesão que ainda pode ser desfeita; se ele persistir, atravessa um ponto sem retorno e morre. Este resumo percorre esse caminho em três movimentos. Primeiro, o mapa: o que separa adaptação de lesão, o que causa lesão, em que ordem os danos aparecem e o que exatamente define a irreversibilidade — inclusive como isso é lido num exame de sangue. Depois, o motor da lesão isquêmica, a mais comum de todas: a queda de ATP e o que ela desencadeia na bomba de sódio, na mitocôndria, no cálcio e na membrana. Por fim, o paradoxo do oxigênio — os radicais livres e a lesão que o próprio tratamento provoca —, as agressões que fogem a essa cascata e o destino final da célula que não voltou.
]

#parte-title("PARTE I — Do equilíbrio à irreversibilidade", primeira: true)

#subtopico("1.1 — Adaptação, lesão e o limiar entre elas")

Uma célula normal vive em #termo-nota[homeostase][estado de equilíbrio dinâmico mantido ativamente, com gasto de energia, apesar das variações do meio externo] — um equilíbrio ativo, mantido dentro de uma faixa estreita de volume, pH e concentração iônica. Um estímulo agressor tira a célula dessa faixa, e o que acontece a seguir depende de duas variáveis, não de uma: a *intensidade* do estímulo e a sua *duração*. Estímulos leves e prolongados dão à célula tempo de reorganizar sua maquinaria e alcançar um novo ponto de equilíbrio — é a adaptação. Estímulos intensos ou rápidos não dão esse tempo, e a célula sofre lesão.

O contraste fica claro na musculação. Quem começa a puxar peso impõe ao músculo um estresse mecânico repetido, moderado e crônico; ao longo de semanas, as fibras respondem sintetizando mais proteína contrátil e o músculo cresce. A mesma carga aplicada de uma vez, em um único movimento mal executado, rompe fibras. Não é a natureza do estímulo que muda — é o tempo que ele dá à célula para responder.

*O ponto fino é entender por que a adaptação precisa de tempo.* Adaptar-se significa mudar quais proteínas a célula fabrica: ativar genes, transcrever, traduzir, montar novas estruturas. Isso leva horas a dias. Uma artéria coronária que oclui em segundos simplesmente não abre essa janela — e é por isso que a mesma sobrecarga que, imposta lentamente, produz hipertrofia, imposta de repente produz morte celular.

Os exemplos clínicos da adaptação vêm dessa lógica. Na hipertensão arterial, a resistência vascular periférica sobe aos poucos, e o ventrículo esquerdo precisa gerar mais pressão a cada batimento; a resposta é acumular filamentos contráteis dentro de cada cardiomiócito, e a parede engrossa — hipertrofia. Aqui vale uma distinção que costuma escapar: o cardiomiócito é uma célula *permanente*, que perdeu a capacidade de se dividir depois do nascimento. O coração hipertrofiado não tem mais células, tem células maiores. Já um epitélio, feito de células lábeis que se dividem a vida toda, responde ao mesmo tipo de demanda somando células — hiperplasia. No sentido oposto está a atrofia: o paciente com lesão medular que fica restrito ao leito perde massa muscular porque a célula, sem estímulo mecânico, aumenta a degradação de suas próprias proteínas pela via da autofagia e do sistema ubiquitina-proteassoma. Ela encolhe, mas continua viva — atrofia não é morte celular. O mesmo raciocínio explica a atrofia cortical da doença de Alzheimer, em que a perda progressiva de sinapses e de neurônios reduz o volume do córtex.

Quando o estímulo ultrapassa a capacidade de adaptação, a célula entra em lesão. Se o agressor é moderado e transitório — a coronária que fica insuficiente durante uma corrida e volta a suprir quando o indivíduo para —, a lesão é *reversível*: retirado o estímulo, a célula recupera a estrutura e a função. Se o agressor é intenso e progressivo, a lesão avança até um ponto a partir do qual nenhuma intervenção devolve a célula ao normal — lesão *irreversível* —, e daí ela segue para um de dois desfechos, necrose ou apoptose. Esse é o organograma que organiza toda esta aula, e vale guardá-lo inteiro antes de descer aos mecanismos.

#esquema(
  grid(
    columns: (1fr, 16pt, 1fr, 16pt, 1fr),
    align: horizon,
    row-gutter: 8pt,
    esq-caixa("Célula normal", [homeostase], cor: teal),
    esq-seta,
    esq-caixa("Estímulo", [intensidade × duração], cor: slate),
    esq-seta,
    esq-caixa("Adaptação", [hipertrofia · hiperplasia · atrofia · metaplasia], cor: teal),
    grid.cell(colspan: 5, align(center, text(size: 8pt, style: "italic", fill: text-light, [estímulo leve e prolongado → acima · estímulo intenso ou rápido → abaixo]))),
    esq-caixa("Lesão reversível", [edema celular · esteatose · #emph[blebs]], cor: gold),
    esq-seta,
    esq-caixa("Lesão irreversível", [membrana rompida · DNA destruído], cor: red-alert),
    esq-seta,
    esq-caixa("Morte celular", [necrose · apoptose], cor: red-alert),
  ),
  legenda: [O organograma da lesão celular. O mesmo agressor pode levar a três destinos diferentes, e quem decide é a combinação entre intensidade e duração. A seta de volta existe só na faixa reversível: removida a causa, a célula retorna à homeostase. Depois do ponto sem retorno, não há caminho de volta.],
)

#mini-resumo[Adaptação e lesão não são graus da mesma coisa: adaptação exige tempo para trocar o repertório de proteínas; lesão é o que sobra quando esse tempo não existe.]

#subtopico("1.2 — As causas: sete portas para a mesma casa")

Uma tarde de sol no fim de semana resume, sozinha, o funcionamento de toda esta seção. A radiação ultravioleta atinge as células epiteliais da pele, forma ligações anômalas entre bases vizinhas do DNA e gera radicais livres. Em dose pequena e repetida, a resposta é adaptativa: mais melanina, epiderme mais espessa. Em dose um pouco maior, há lesão reversível e a pele fica temporariamente alterada. Em dose alta, células morrem em massa, o conteúdo derramado desencadeia inflamação, e o resultado é a queimadura solar — vermelha, dolorosa, descamativa. Um só agressor, três desfechos, separados apenas pela dose.

As causas de lesão celular se agrupam em sete categorias, e conhecê-las importa menos como lista do que como conjunto de mecanismos distintos. A *privação de oxigênio* é a mais prevalente de todas, e aqui há uma distinção que muda o raciocínio clínico inteiro. #termo-nota[Hipóxia][redução da oferta de oxigênio à célula, com fluxo sanguíneo preservado] é a falta de oxigênio com o fluxo sanguíneo mantido — acontece na insuficiência respiratória, na anemia grave, na intoxicação por monóxido de carbono. #termo-nota[Isquemia][redução ou interrupção do fluxo sanguíneo, que retira oxigênio, substratos energéticos e a remoção de metabólitos ao mesmo tempo] é a interrupção do próprio fluxo, e ela retira três coisas de uma vez: o oxigênio, os substratos energéticos que chegariam pelo sangue e a lavagem dos metabólitos ácidos que a célula produz. Por isso a isquemia lesa mais rápido e mais profundamente que a hipóxia pura — a célula isquêmica não só perde a respiração aeróbia, como fica sem combustível para a alternativa anaeróbia e marinando nos próprios resíduos. Um caso à parte é a intoxicação por cianeto: o oxigênio chega normalmente ao tecido, mas a célula não consegue usá-lo, porque a citocromo-oxidase está bloqueada.

Os *agentes físicos* incluem trauma mecânico, temperaturas extremas, choque elétrico, mudanças bruscas de pressão e radiação — a mesma radiação da tarde de sol. Os *agentes químicos e as drogas* atuam de duas formas: alguns lesam diretamente, ligando-se a componentes celulares, e outros só depois de convertidos em metabólitos reativos pelo fígado. A fumaça do cigarro ilustra os dois lados da moeda: cronicamente, força o epitélio respiratório a trocar de fenótipo — metaplasia, uma adaptação que protege contra a agressão química mas custa o transporte mucociliar; agudamente e em alta dose, lesa diretamente as células de revestimento. Os *agentes infecciosos* podem destruir a célula por replicação intracelular, como o vírus que prolifera dentro do hepatócito na hepatite aguda até rompê-lo.

As *reações imunológicas* fecham um circuito que costuma ser lido ao contrário: nem sempre é o agente que destrói a célula. Em alergias e doenças autoimunes, a própria resposta imune agride tecidos do hospedeiro. E em infecções intracelulares — tuberculose, hepatites virais — a estratégia do sistema imune contra o micro-organismo escondido é matar a célula que o abriga; boa parte da destruição tecidual que se vê é resposta do hospedeiro, não do patógeno. Restam os *desarranjos genéticos*, em que mutações e translocações comprometem proteínas essenciais, e o *desequilíbrio nutricional*, que lesa tanto por carência — sem substrato, as reações que sustentam a célula param — quanto por excesso, com sobrecarga lipídica e estresse oxidativo.

#mini-resumo[Sete causas, dois modos de agir: privar a célula do que ela precisa (oxigênio, substrato, nutriente) ou atacar diretamente suas moléculas (radiação, químicos, radicais, resposta imune).]

#subtopico("1.3 — A ordem dos acontecimentos: a morfologia chega atrasada")

Há uma defasagem entre o que já aconteceu na célula e o que se consegue ver, e ignorá-la é a origem de um erro clínico frequente. A lesão começa por alterações *bioquímicas* — queda de ATP, mudança de pH, desequilíbrio iônico — que nenhum microscópio mostra. Em seguida vem a *perda de função*: o miócito isquêmico deixa de contrair em segundos, muito antes de qualquer alteração de forma. Só então aparecem as alterações *ultraestruturais*, visíveis apenas ao microscópio eletrônico. As alterações do *microscópio de luz* vêm depois, e as alterações *macroscópicas* — a área esbranquiçada do infarto sobre a superfície de corte — só se instalam quando a lesão já é irreversível e a célula já morreu há horas.

A consequência prática é direta e vale para a beira do leito: quando a lesão fica visível, a janela de reversibilidade já passou. É exatamente por isso que a medicina investe tanto em ferramentas de diagnóstico precoce — restabelecer o fluxo enquanto a lesão ainda é bioquímica devolve a célula ao normal; fazê-lo depois apenas impede que mais células morram, sem recuperar as que já se perderam.

*A linha que separa reversível de irreversível não fica no mesmo lugar para toda célula.* Ela depende da demanda energética basal, do estoque de glicogênio e da capacidade de sustentar a glicólise anaeróbia. O neurônio, com demanda altíssima e reserva quase nula, atravessa essa linha em três a cinco minutos de isquemia. O cardiomiócito resiste algumas dezenas de minutos. Fibroblastos e células musculares esqueléticas, com metabolismo mais baixo e glicogênio guardado, aguentam horas. É a mesma cascata em todos — só o relógio muda.

Na fase reversível, a microscopia de luz é quase muda: o que se vê é o *edema celular* — a célula inchada, com citoplasma pálido e vacuolizado, achado também chamado de degeneração hidrópica — e, às vezes, a *esteatose*, o acúmulo de vacúolos de gordura no citoplasma, achado inespecífico que aparece em fígado, coração e rim. Ambos regridem se a causa for removida.

O que de fato acontece nessa fase está no microscópio eletrônico, e cada achado tem uma origem mecânica clara. A membrana plasmática perde a ancoragem ao citoesqueleto e forma protrusões arredondadas, os #termo-nota[blebs][bolhas na superfície celular formadas quando a membrana plasmática se desprende do citoesqueleto que a sustentava]. Já as células com borda em escova, como as do túbulo renal proximal e as do epitélio intestinal, perdem suas microvilosidades e a superfície fica irregular. As mitocôndrias incham. O retículo endoplasmático se dilata, e os ribossomos se desprendem da sua face rugosa. No núcleo, a cromatina começa a se condensar. Nada disso é decoração: cada um desses achados é a assinatura visível de um mecanismo bioquímico que a PARTE II vai abrir. Não vale decorar a lista; vale saber de onde cada item dela veio.

#tabela-nebli(
  ("", "Lesão reversível", "Lesão irreversível"),
  (
    ([*Membrana*], [#emph[blebs], perda de microvilosidades — mas bicamada íntegra], [perda de integridade; conteúdo intracelular extravasa]),
    ([*Núcleo*], [cromatina levemente condensada], [picnose → cariorrexe → cariólise; DNA destruído]),
    ([*Mitocôndria*], [edema, densidades pequenas], [edema intenso, densidades amorfas grandes]),
    ([*Microscopia de luz*], [edema celular, às vezes esteatose], [alterações francas, mas só após horas]),
    ([*No sangue*], [sem enzimas intracelulares], [troponina, creatina-quinase MB, lipase — conforme o órgão]),
    ([*Desfecho*], [retorno ao normal se a causa cessa], [necrose ou apoptose]),
  ),
  colunas: (0.9fr, 1.5fr, 1.5fr),
)

#esquema(
  grid(
    columns: (1fr, 12pt, 0.9fr, 12pt, 1.35fr, 12pt, 1.25fr, 12pt, 1fr),
    align: horizon,
    esq-caixa("Bioquímica", [↓ ATP, ↓ pH, íons], cor: teal),
    esq-seta,
    esq-caixa("Função", [a contração para], cor: teal),
    esq-seta,
    esq-caixa("Ultraestrutura", [microscópio eletrônico], cor: gold),
    esq-seta,
    esq-caixa("Microscopia de luz", [horas depois], cor: red-alert),
    esq-seta,
    esq-caixa("Macroscopia", [área de infarto], cor: red-alert),
  ),
  legenda: [A ordem é sempre esta, e a janela de reversibilidade fica nas duas primeiras caixas. Quando a alteração aparece ao microscópio de luz, a célula já morreu — a imagem é o registro tardio de um evento bioquímico antigo. Onde cai a linha da irreversibilidade depende do tipo celular: minutos para o neurônio, dezenas de minutos para o cardiomiócito, horas para o fibroblasto.],
)

#subtopico("1.4 — O ponto sem retorno, lido no exame de sangue")

Dois eventos, e apenas dois, definem a irreversibilidade: a *perda da integridade da membrana plasmática* e a *destruição extensa do DNA e das proteínas*. Enquanto a membrana se mantém funcional e o material genético está preservado, retirar o agressor devolve a célula ao normal, por mais alterada que ela pareça. Quando qualquer um dos dois cede em extensão suficiente, não há intervenção que recupere.

Os dois costumam acontecer juntos, mas a ordem depende do agressor. Na lesão isquêmica, a membrana cede primeiro — é a cascata energética que a PARTE II detalha. Em agressões que atacam o material genético diretamente, como grandes translocações, radiação ionizante ou certos quimioterápicos, a destruição do DNA vem antes, e a célula muitas vezes aciona um programa de autodestruição antes mesmo de perder a membrana.

*E é aqui que o mecanismo vira medicina de plantão.* Um paciente chega ao pronto-socorro com dor torácica em aperto irradiada para a mandíbula e para o membro superior esquerdo. Além do eletrocardiograma, colhe-se sangue seriado — na chegada, uma hora depois, duas horas depois — para dosar marcadores de lesão miocárdica: #sigla("CK-MB", [fração MB da creatina-quinase, isoforma característica do músculo cardíaco]) e troponina cardíaca. Essas duas proteínas vivem *dentro* do cardiomiócito, participando do aparato contrátil. Se elas aparecem no sangue, é porque saíram da célula; e para sair, tiveram que atravessar uma membrana que deveria estar fechada. A elevação dos marcadores, portanto, não mede dor nem tamanho do susto: ela é evidência bioquímica de que a membrana se rompeu, ou seja, de lesão *irreversível* e morte celular.

#atencao-box("Enzima intracelular no sangue significa membrana rompida", [
  A tentação é ler a troponina elevada como marcador de "gravidade da dor" ou de "intensidade da isquemia". Não é isso que ela informa. A troponina é uma proteína do citoesqueleto contrátil do cardiomiócito, e não existe mecanismo que a exporte de uma célula viva. Sua presença na circulação demonstra que a barreira que separava o citoplasma do interstício deixou de existir. Traduzindo o achado em uma frase: *enzima intracelular na circulação sanguínea significa lesão celular irreversível.* O raciocínio inverso vale igualmente: dor torácica isquêmica com troponina normal é lesão reversível — angina —, e a célula ainda pode ser salva.
])

#clinica-box("Angina e infarto: a mesma isquemia dos dois lados da linha", [
  Angina e infarto agudo do miocárdio nascem do mesmo mecanismo — oferta de oxigênio abaixo da demanda — e se separam exatamente pelo critério de irreversibilidade. Na angina, o desequilíbrio é transitório: o paciente para o esforço, a demanda cai, o fluxo volta a ser suficiente, e o cardiomiócito, que chegou a perder função e a inchar, recupera estrutura e contração. A membrana nunca se rompeu, e por isso a troponina não sobe. No infarto, a obstrução persiste; passado o tempo de tolerância do miocárdio, a membrana cede, a troponina vaza e a área correspondente morre. A conduta segue o mecanismo: ofertar oxigênio, reduzir a demanda com controle da dor e da frequência cardíaca, e restabelecer o fluxo o mais rápido possível — porque cada minuto desloca células da faixa reversível para a irreversível.
])

A cinética dos marcadores refina essa leitura, e vale conhecê-la porque ela nasce do mesmo mecanismo. A mioglobina é a primeira a subir, em duas a quatro horas, porque é uma proteína pequena que escapa por brechas menores — mas está presente também no músculo esquelético, o que a torna sensível e pouco específica. A troponina cardíaca sobe em três a quatro horas e permanece elevada por sete a dez dias, o que permite diagnosticar um infarto ocorrido dias antes. A fração MB da creatina-quinase normaliza em dois a três dias e por isso ganha uma utilidade própria: uma nova elevação depois da queda sugere um segundo evento isquêmico. Vale ainda um cuidado que o raciocínio mecanístico entrega de graça: a troponina marca *necrose de miócito cardíaco*, qualquer que seja a causa — miocardite, sepse e embolia pulmonar também a elevam. Ela responde "morreu músculo cardíaco", não "houve obstrução coronária".

O mesmo princípio se aplica a qualquer órgão, e é isso que o torna poderoso. O pâncreas exócrino produz lipase e amilase e as despeja no ducto pancreático, rumo ao tubo digestivo — não há razão para essas enzimas circularem no sangue. Numa pancreatite, as células acinares sofrem lesão irreversível, rompem-se e liberam seu conteúdo enzimático no interstício e na circulação: dosar lipase e amilase elevadas é ler, indiretamente, que houve destruição de células pancreáticas. No fígado, a mesma lógica sustenta as aminotransferases; nos rins e no músculo, outras proteínas contam a mesma história. *Toda vez que uma proteína que deveria estar dentro da célula é encontrada fora dela, o que se está medindo é a integridade da membrana.*

O que a PARTE I deixou de pé é o quadro: a lesão tem causas variadas, uma cronologia fixa e dois critérios objetivos de irreversibilidade. Falta agora abrir o motor — por que, na lesão isquêmica, a membrana cede. A resposta começa em uma única molécula que deixa de ser produzida.

#parte-title("PARTE II — A cascata da isquemia: ATP, mitocôndria, cálcio e membrana")

#subtopico("2.1 — Queda de ATP: a bomba de sódio para e a célula incha")

A lesão isquêmica começa em um ponto único e desce em cascata a partir dele. Sem oxigênio suficiente chegando à mitocôndria, a fosforilação oxidativa desacelera — falta o aceptor final de elétrons que sustenta o bombeamento de prótons pelas cristas — e a produção de ATP despenca. Tudo o que vem depois é consequência da falta dessa molécula, e vale insistir nisso porque a intuição costuma parar no oxigênio: a célula não morre por falta de oxigênio, morre por falta de ATP.

A queda de ATP se ramifica em três direções ao mesmo tempo. A primeira e mais visível atinge a bomba de sódio e potássio, uma #sigla("ATPase", [enzima que hidrolisa ATP para realizar trabalho — no caso das bombas, transporte de íons contra o gradiente]) de membrana que consome, em repouso, uma parcela enorme do orçamento energético da célula — em muitos tecidos, algo próximo de um terço de todo o ATP produzido. Sem combustível, ela desacelera. O sódio, que era continuamente expulso, passa a se acumular no citosol; o potássio, que era trazido para dentro, escapa para o interstício. E onde o sódio se acumula, a água vai atrás por osmose.

Aqui a PARTE I se fecha por dentro. O influxo de sódio e água é exatamente o que produz o edema celular visto ao microscópio de luz, a dilatação do retículo endoplasmático vista ao microscópio eletrônico, e — junto com a perda de âncoras que virá adiante — os #emph[blebs] e o apagamento das microvilosidades. Cada achado morfológico daquela lista tem, aqui, seu mecanismo. *Do lado de fora da célula, o potássio que saiu tem consequência própria:* no miocárdio isquêmico, o potássio extracelular elevado desestabiliza o potencial de membrana das fibras vizinhas e é uma das razões pelas quais a isquemia gera arritmias antes mesmo de matar músculo.

A segunda ramificação é metabólica. Sem fosforilação oxidativa, a célula recorre à glicólise anaeróbia, que ainda extrai ATP da glicose no citosol — mas a um rendimento muitas vezes menor. O preço é duplo: os estoques de glicogênio se esgotam rapidamente, e o piruvato, sem para onde ir, acumula-se como lactato. O pH intracelular cai. *E vale um cuidado aqui, porque a leitura simplificada atribui toda a acidose ao lactato:* contribuem também a hidrólise maciça de ATP, que libera fosfato inorgânico e prótons, e o componente metabólico sistêmico do quadro. A acidez, por sua vez, tem um efeito visível — a cromatina se condensa, resposta protetora do núcleo a um ambiente ácido — e um efeito perverso: enzimas glicolíticas são inibidas em pH baixo, de modo que a via de socorro sabota a si mesma conforme trabalha. Isso explica por que a glicólise anaeróbia adia a morte celular sem jamais evitá-la, e por que células com bom estoque de glicogênio, como o hepatócito e o músculo esquelético, aguentam bem mais tempo de isquemia que o neurônio.

A terceira ramificação é de economia. Com pouco ATP, a célula desliga o que pode ser desligado, e a síntese proteica é a primeira a cair: os ribossomos se destacam da face rugosa do #sigla("RE", [retículo endoplasmático]) e a tradução diminui. É uma escolha coerente — manter as bombas ligadas importa mais, no curto prazo, do que fabricar proteínas novas. O detalhe estrutural que se vê ao microscópio eletrônico, o retículo "liso" onde antes havia ribossomos aderidos, é o registro dessa decisão energética.

#esquema(
  grid(
    columns: (0.85fr, 14pt, 1fr, 14pt, 1.5fr),
    align: horizon,
    row-gutter: 7pt,
    grid.cell(rowspan: 3, align(horizon, esq-caixa("Isquemia", [↓ oxigênio, ↓ substrato], cor: slate))),
    grid.cell(rowspan: 3, esq-seta),
    grid.cell(rowspan: 3, align(horizon, esq-caixa("↓ ATP", [fosforilação oxidativa freia], cor: red-alert))),
    esq-seta,
    esq-caixa("Bomba de Na⁺/K⁺ falha", [Na⁺ e água entram, K⁺ sai → edema celular, dilatação do RE, #emph[blebs]], cor: teal),
    esq-seta,
    esq-caixa("Glicólise anaeróbia", [glicogênio se esgota, lactato sobe, pH cai → cromatina condensa], cor: gold),
    esq-seta,
    esq-caixa("Ribossomos se soltam", [síntese proteica cai — economia de energia], cor: navy),
  ),
  legenda: [As três ramificações da queda de ATP. Repare que cada achado morfológico da lesão reversível descrito na PARTE I aparece aqui como consequência direta de um dos três ramos — a morfologia é o retrato da bioquímica. Enquanto o ATP puder ser restabelecido, os três ramos são reversíveis.],
)

#mini-resumo[A célula não morre por falta de oxigênio, morre por falta de ATP: a bomba de sódio para e ela incha, a glicólise anaeróbia a acidifica, e a síntese proteica é desligada para poupar energia.]

#subtopico("2.2 — A mitocôndria no centro: duas portas, dois destinos")

A mitocôndria ocupa uma posição incômoda nessa história: é a primeira vítima da isquemia e, ao mesmo tempo, quem decide como a célula vai morrer. E ela decide abrindo uma de duas portas, na mesma membrana interna.

A primeira porta é o #termo-nota[poro de transição de permeabilidade mitocondrial][canal de alta condutância que se abre na membrana interna da mitocôndria e dissipa o gradiente de prótons, desligando a síntese de ATP]. Para entender por que ele é catastrófico, é preciso lembrar o que a membrana interna faz: ela separa cargas, mantendo uma diferença de potencial entre a matriz e o espaço intermembranas, e é *essa* diferença que a ATP-sintase usa como força motriz. Um canal de alta condutância aberto nessa membrana equivale a um curto-circuito — os prótons voltam sem passar pela turbina, o potencial se dissipa e a síntese de ATP cessa, mesmo que ainda chegue algum oxigênio. Pior: sem gradiente adequado, a transferência de elétrons na cadeia fica desorganizada e escapam mais elétrons pelo caminho, formando mais radicais livres, que por sua vez favorecem a abertura de mais poros. É uma alça de retroalimentação que se fecha sobre si mesma, e o desfecho dela é a necrose.

A segunda porta é mais discreta. Entre as cristas mitocondriais fica o citocromo c, componente normal da cadeia respiratória. Quando a permeabilidade da membrana se altera, ele escapa para o citosol — e fora da mitocôndria ele deixa de ser transportador de elétrons e passa a ser sinal. No citosol, o citocromo c se associa a proteínas adaptadoras e monta uma plataforma que ativa a primeira caspase da cadeia; a partir daí, a cascata de caspases executoras desmonta a célula de dentro para fora, de maneira ordenada. É a via intrínseca da apoptose.

*O que decide qual das duas portas prevalece não é o tamanho do dano, e sim quanto ATP sobrou.* A apoptose é um programa: exige energia para montar a plataforma de ativação, para clivar substratos, para empacotar o conteúdo celular em fragmentos com membrana íntegra. Quando a isquemia é profunda e o ATP desapareceu, a célula não tem como executar esse programa e o desfecho é a necrose. Quando a agressão é mais branda ou mais lenta, e resta ATP, o mesmo estímulo termina em apoptose. Duas mortes, uma organela, e um único parâmetro decisivo.

#confusao-prevista(
  titulo: "Citocromo c no citosol leva à apoptose, não à necrose",
  aluno_acha: [aluno acha que, como o citocromo c faz parte da cadeia respiratória, perdê-lo derruba o ATP e mata a célula por necrose],
  mecanismo: [a saída do citocromo c é um #emph[sinal], não uma falência energética. No citosol ele monta o apoptossomo e liga a cascata de caspases — morte programada, com membrana preservada e sem inflamação. Quem produz necrose é a abertura do poro de transição, que dissipa o potencial de membrana e desliga a produção de ATP. As duas coisas acontecem na mesma organela e podem coexistir; o que separa os desfechos é o ATP disponível para executar o programa apoptótico.],
)

#esquema(
  grid(
    columns: (1fr, 14pt, 1.15fr, 14pt, 1fr),
    align: horizon,
    row-gutter: 7pt,
    grid.cell(rowspan: 3, align(horizon, esq-caixa("Dano mitocondrial", [isquemia · cálcio na matriz · radicais livres], cor: slate))),
    grid.cell(rowspan: 3, esq-seta),
    esq-caixa("Poro de transição abre", [potencial de membrana se dissipa], cor: red-alert),
    esq-seta,
    esq-caixa("Necrose", [sem ATP para executar programa], cor: red-alert),
    grid.cell(colspan: 3, align(center, text(size: 7.5pt, style: "italic", fill: text-light, [as duas portas se abrem na mesma organela — o ATP restante decide qual prevalece]))),
    esq-caixa("Citocromo c escapa", [vira sinal no citosol], cor: violet),
    esq-seta,
    esq-caixa("Apoptose", [caspases desmontam a célula], cor: violet),
  ),
  legenda: [As duas portas da mitocôndria. O poro de transição desliga a produção de ATP e empurra para a necrose; o citocromo c no citosol liga a cascata de caspases e leva à apoptose. Note a alça de retroalimentação implícita: menos potencial de membrana significa mais radicais livres, que abrem mais poros.],
)

#subtopico("2.3 — Cálcio citosólico: o mensageiro que vira demolidor")

O cálcio é mantido no citosol em concentração cerca de dez mil vezes menor que no meio extracelular, e essa diferença brutal não é acidental — é ela que torna o cálcio um sinal utilizável. Manter o gradiente custa ATP: bombas do retículo endoplasmático recolhem o cálcio para dentro do reservatório, bombas da membrana plasmática o expulsam para fora, e a mitocôndria armazena o excedente. Quando a célula quer disparar uma resposta rápida — contrair, secretar, ativar uma enzima —, basta abrir um canal, e a avalanche de cálcio a favor do gradiente faz o resto.

*Na isquemia, essa arquitetura elegante se volta contra a célula.* Sem ATP, as bombas param, e o cálcio vaza dos reservatórios internos e entra do meio extracelular. A concentração citosólica sobe e permanece alta — e, do ponto de vista da maquinaria celular, cálcio alto e sustentado é um comando. As enzimas que respondem a ele não perguntam se o sinal veio de uma via fisiológica ou de uma falência energética; elas simplesmente executam.

São quatro famílias de enzimas, e o efeito conjunto é uma demolição coordenada. As *fosfolipases* quebram os fosfolipídeos da membrana, atacando exatamente a bicamada que a célula precisa manter íntegra. As *proteases* — as calpaínas — clivam proteínas do citoesqueleto e as âncoras que prendem a membrana plasmática a ele; é essa desancoragem que explica os #emph[blebs] descritos lá atrás. As *endonucleases* fragmentam DNA e RNA, empurrando a célula na direção do segundo critério de irreversibilidade. E as *ATPases* hidrolisam ATP, acelerando a queda da molécula que já estava em falta. O cálcio, além disso, entra na mitocôndria, e a sobrecarga de cálcio na matriz é um dos gatilhos mais potentes do poro de transição — de modo que o desequilíbrio iônico volta para alimentar a falência energética que o gerou.

#esquema(
  grid(
    columns: (1fr, 14pt, 1fr, 14pt, 1.35fr),
    align: horizon,
    row-gutter: 7pt,
    grid.cell(rowspan: 4, align(horizon, esq-caixa("↓ ATP", [bombas de cálcio param], cor: slate))),
    grid.cell(rowspan: 4, esq-seta),
    grid.cell(rowspan: 4, align(horizon, esq-caixa("Ca²⁺ no citosol", [do retículo, da mitocôndria e do meio externo], cor: red-alert))),
    esq-seta,
    esq-caixa("Fosfolipases", [quebram fosfolipídeos → dano de membrana], cor: teal),
    esq-seta,
    esq-caixa("Proteases", [rompem citoesqueleto e âncoras → #emph[blebs]], cor: teal),
    esq-seta,
    esq-caixa("Endonucleases", [fragmentam DNA e RNA], cor: gold),
    esq-seta,
    esq-caixa("ATPases", [consomem o ATP restante], cor: gold),
  ),
  legenda: [O cálcio como catalisador da lesão irreversível. As quatro famílias de enzimas atingem, juntas, os dois critérios de irreversibilidade: dano de membrana e destruição do material genético. E o cálcio captado pela mitocôndria realimenta o poro de transição, fechando o ciclo com a queda de ATP que abriu tudo.],
)

#clinica-box("Rabdomiólise: o mecanismo inteiro em um só quadro", [
  Numa lesão muscular extensa — esmagamento, isquemia prolongada de membro, esforço extremo, certas intoxicações —, a fibra muscular esquelética perde o controle do cálcio citosólico exatamente pelo caminho descrito acima. As calpaínas ativadas destroem o citoesqueleto, as fosfolipases desmontam o sarcolema, e o conteúdo da fibra vaza para a circulação. O laboratório mostra creatina-quinase em valores altíssimos e mioglobina no plasma e na urina — a mesma lógica da troponina no infarto: proteína intracelular fora da célula significa membrana rompida. A mioglobina filtrada, porém, é tóxica para o túbulo renal e precipita nele, e a lesão renal aguda que se segue é a complicação temida do quadro. A conduta — hidratação vigorosa e precoce — nasce do mecanismo: diluir e arrastar a mioglobina antes que ela obstrua e lese o túbulo.
])

#subtopico("2.4 — Dano de membrana: onde os caminhos se encontram")

Tudo o que foi descrito até aqui converge para o mesmo lugar. Dano de membrana não tem causa única, e essa é justamente a razão de ele ser tão difícil de reverter: quatro forças independentes atacam a bicamada ao mesmo tempo, e neutralizar uma delas não impede as outras.

A primeira força é a peroxidação dos lipídeos pelos radicais livres, tema da PARTE III. A segunda é a queda da síntese de fosfolipídeos, consequência direta da falta de ATP — a membrana é uma estrutura em renovação constante, e parar de repô-la já a degrada. A terceira são as fosfolipases ativadas pelo cálcio, que quebram ativamente o que resta. A quarta são as proteases, que destroem tanto proteínas de membrana quanto as âncoras que a fixam ao citoesqueleto. *E há um agravante que costuma passar despercebido:* os produtos dessa quebra — lisofosfolipídeos e ácidos graxos livres — comportam-se como detergentes dentro da própria membrana, dissolvendo o que ainda estava organizado. A degradação, uma vez iniciada, se acelera sozinha.

O ponto que fecha a PARTE II é que não existe uma membrana só. A membrana *plasmática*, ao ceder, deixa escapar o conteúdo citoplasmático — e é isso que se lê no sangue como troponina, creatina-quinase ou lipase. A membrana *mitocondrial* interna, ao ceder, abre o poro de transição e apaga a produção de ATP. E as membranas *lisossomais*, ao cederem, derramam no citosol as hidrolases ácidas que os lisossomos guardavam, e essas enzimas digerem a célula por dentro — a #termo-nota[autólise][digestão da própria célula pelas hidrolases ácidas liberadas dos lisossomos rompidos] que dá à célula necrótica seu aspecto desestruturado ao microscópio.

Quando as três cedem, os dois critérios de irreversibilidade estão preenchidos ao mesmo tempo: a membrana não separa mais nada, e as endonucleases já fragmentaram o material genético. A célula atravessou o ponto sem retorno. Falta entender por que, às vezes, é a chegada do oxigênio — e não a falta dele — que empurra a célula por cima dessa linha.

#esquema(
  grid(
    columns: (1fr, 1fr, 1fr, 1fr),
    column-gutter: 6pt,
    row-gutter: 7pt,
    esq-caixa("Peroxidação lipídica", [radicais livres oxidam ácidos graxos], cor: gold),
    esq-caixa("↓ Síntese de fosfolipídeo", [sem ATP, a membrana não se repõe], cor: slate),
    esq-caixa("Fosfolipases", [cálcio ativa a quebra], cor: teal),
    esq-caixa("Proteases", [citoesqueleto e âncoras], cor: teal),
    grid.cell(colspan: 4, esq-desce),
    grid.cell(colspan: 4, esq-caixa("Dano de membrana", [plasmática: extravasa enzimas · mitocondrial: apaga o ATP · lisossomal: autólise], cor: red-alert)),
  ),
  legenda: [A via final comum. Quatro forças independentes atacam a mesma estrutura, e os produtos da quebra — lisofosfolipídeos e ácidos graxos livres — agem como detergentes, acelerando a degradação. Cada tipo de membrana que cede produz uma consequência distinta, e as três juntas fecham o quadro da irreversibilidade.],
)

#parte-title("PARTE III — O paradoxo do oxigênio, os danos que fogem à regra e os dois destinos")

#subtopico("3.1 — Radicais livres: o custo de respirar e as defesas que o pagam")

Reduzir uma molécula de oxigênio a duas de água exige quatro elétrons entregues em sequência, e a cadeia respiratória faz isso muito bem — mas não perfeitamente. Uma pequena fração dos elétrons escapa antes da hora e reduz o oxigênio pela metade, gerando o ânion superóxido. Formar radical livre, portanto, não é acidente nem doença: é o custo contínuo de respirar. O que separa o normal do patológico é o equilíbrio entre o quanto se forma e o quanto se neutraliza.

Um #termo-nota[radical livre][átomo ou molécula com elétron desemparelhado na camada externa, o que o torna extremamente reativo e capaz de propagar a reação para moléculas vizinhas] é reativo justamente porque tem um elétron desemparelhado: ele arranca elétrons de qualquer molécula ao alcance para se estabilizar — e a molécula atacada vira, ela própria, um radical. A reação se propaga.

As defesas trabalham em sequência, e é importante ver que nenhuma delas resolve sozinha. A superóxido-dismutase converte o superóxido em peróxido de hidrogênio, a água oxigenada — que já é menos reativo, mas *ainda não é inofensivo*. Quem termina o serviço são a catalase, que decompõe o peróxido em água e oxigênio, e a glutationa-peroxidase, que o reduz a água. Se o peróxido não for removido a tempo e encontrar ferro livre, acontece a reação de Fenton, uma reação química direta, sem enzima nenhuma, que produz o radical hidroxila — o mais destrutivo dos três, e contra o qual não há enzima específica. Somam-se a esse sistema os antioxidantes não-enzimáticos: a glutationa reduzida, a vitamina E dentro das membranas e a vitamina C no meio aquoso.

#esquema(
  grid(
    columns: (0.95fr, 12pt, 1fr, 12pt, 1fr, 12pt, 0.95fr),
    align: horizon,
    row-gutter: 6pt,
    esq-caixa("O₂", [redução incompleta na cadeia respiratória], cor: slate),
    esq-seta,
    esq-caixa("Superóxido", [O₂ com um elétron a mais], cor: gold),
    esq-seta,
    esq-caixa("Peróxido de hidrogênio", [ainda reativo], cor: gold),
    esq-seta,
    esq-caixa("Água", [neutralizado], cor: teal),
    grid.cell(colspan: 7, align(center, text(size: 7.5pt, style: "italic", fill: text-light, [superóxido-dismutase no primeiro passo · catalase e glutationa-peroxidase no segundo · com ferro livre, o peróxido desvia para a reação de Fenton]))),
    grid.cell(colspan: 3, align(center, text(size: 7.5pt, fill: text-light, [ferro livre + peróxido]))),
    esq-desce,
    grid.cell(colspan: 3, esq-caixa("Radical hidroxila", [o mais destrutivo — sem enzima que o remova], cor: red-alert)),
  ),
  legenda: [A cadeia de espécies reativas e as duas etapas da defesa. A dismutase não elimina o problema, apenas o transforma: se catalase e glutationa-peroxidase não fecharem a conta, o peróxido encontra ferro livre e vira radical hidroxila. É por isso que sobrecarga de ferro e hemorragia em tecido agravam a lesão oxidativa.],
)

A produção sobe muito acima do basal em várias situações, e conhecê-las explica metade das lesões teciduais que a clínica encontra. A inflamação é a mais importante: neutrófilos e macrófagos produzem superóxido deliberadamente, como arma contra micro-organismos, e o excesso atinge o tecido em volta. Radiação ionizante quebra moléculas de água e gera radicais diretamente. O metabolismo hepático de certas drogas e toxinas produz metabólitos reativos. E há o próprio funcionamento anormal da mitocôndria: quando chega *pouco* oxigênio, os transportadores da cadeia ficam carregados de elétrons que não têm para onde ir e a fuga aumenta; quando chega oxigênio *demais*, há mais moléculas disponíveis para capturar esses elétrons perdidos. Os dois extremos afastam a mitocôndria do seu ponto ótimo, e ambos aumentam a formação de radicais.

O dano se distribui por três alvos, e cada um deles tem uma assinatura própria. Nos *lipídeos*, o radical arranca um hidrogênio de um ácido graxo insaturado da membrana e desencadeia a peroxidação lipídica — uma reação em cadeia autocatalítica, em que cada lipídeo oxidado gera o radical que ataca o próximo. A bicamada perde organização, e a permeabilidade se altera. Nas *proteínas*, a oxidação de resíduos de aminoácidos deforma a estrutura tridimensional, e com ela se perdem a atividade enzimática e a regulação alostérica; proteínas oxidadas são marcadas para degradação, o que consome ainda mais energia. No *DNA*, a oxidação de bases e a quebra de fitas geram mutações que se acumulam quando o reparo não dá conta — o elo entre estresse oxidativo, envelhecimento e carcinogênese.

#mini-resumo[Radical livre é subproduto normal da respiração. A doença aparece quando a produção supera as defesas — e o alvo é sempre o mesmo trio: lipídeo de membrana, proteína e DNA.]

#subtopico("3.2 — Lesão de isquemia-reperfusão: quando salvar machuca")

Restabelecer o fluxo é o único tratamento eficaz da isquemia — e é também uma agressão adicional. Essa aparente contradição não é um detalhe curioso: ela organiza a urgência de toda a cardiologia e de toda a medicina de transplantes.

O mecanismo decorre diretamente da seção anterior. Durante a isquemia, a mitocôndria se acomodou a um regime de pouco oxigênio, os transportadores da cadeia ficaram carregados de elétrons e as defesas antioxidantes foram sendo consumidas sem reposição. Quando o vaso é reaberto — no cateterismo, ao ligar o enxerto ao receptor —, uma onda de oxigênio encontra exatamente esse cenário: muitos elétrons acumulados, poucas enzimas antioxidantes restantes. O resultado é um pico de radicais livres, muito acima do que aquele tecido produziria em condições normais, e o pico peroxida membranas, oxida proteínas e danifica DNA de uma vez só.

#esquema(
  block(width: 100%, {
    box(width: 100%, height: 3.5cm, {
      place(top + left, dx: 30pt, dy: 2pt, line(start: (0pt, 0pt), end: (0pt, 2.9cm), stroke: 0.7pt + gray-border))
      place(top + left, dx: 30pt, dy: 2.9cm + 2pt, line(start: (0pt, 0pt), end: (100% - 60pt, 0pt), stroke: 0.7pt + gray-border))
      place(top + left, dx: 30pt, dy: 2pt, curve(
        stroke: 1.5pt + navy,
        curve.move((0pt, 10pt)),
        curve.line((70pt, 10pt)),
        curve.line((115pt, 62pt)),
        curve.line((175pt, 44pt)),
        curve.line((380pt, 22pt)),
      ))
      place(top + left, dx: 30pt + 115pt, dy: 2pt, line(start: (0pt, 0pt), end: (0pt, 2.9cm), stroke: (paint: red-alert, thickness: 0.6pt, dash: "dashed")))
      place(top + left, dx: 0pt, dy: 6pt, text(size: 7pt, fill: text-light, [100%]))
      place(top + left, dx: 0pt, dy: 2.55cm, text(size: 7pt, fill: text-light, [0%]))
      place(top + left, dx: 36pt, dy: 2.95cm + 4pt, text(size: 7.5pt, fill: text-light, [isquemia]))
      place(top + left, dx: 118pt, dy: 2.95cm + 4pt, text(size: 7.5pt, fill: red-alert, [reperfusão]))
      place(top + left, dx: 245pt, dy: 2.95cm + 4pt, text(size: 7.5pt, fill: text-light, [recuperação progressiva]))
      place(top + left, dx: 152pt, dy: 14pt, text(size: 7.5pt, fill: red-alert, [pico de radicais livres]))
    })
  }),
  legenda: [O curso da função de um órgão reperfundido — o enxerto renal é o exemplo mais didático. A função cai logo após o restabelecimento do fluxo, e não por falha técnica: é a onda oxidativa matando as células que estavam na faixa limítrofe. Depois ela sobe de novo, porque a maioria das células vizinhas foi resgatada. Quanto mais longa a isquemia, mais profunda a queda e menor a recuperação — daí a janela estreita.],
)

A esse mecanismo somam-se outros três, e vale conhecê-los porque explicam por que a lesão de reperfusão não é evitável apenas com antioxidante. A reentrada de sangue traz uma nova sobrecarga de cálcio para células cujas bombas ainda estão fracas. O plasma que retorna carrega proteínas do sistema complemento, que se depositam no tecido alterado e amplificam a agressão. E os neutrófilos, que só conseguem chegar quando há fluxo, invadem a área e produzem seus próprios radicais. A inflamação, que só é possível depois da reperfusão, participa do dano.

*O ponto que muda o raciocínio é quem morre nesse pico.* Não são as células já mortas — essas não pioram. São as células limítrofes, aquelas que ainda estavam em lesão reversível quando o fluxo voltou e que a onda oxidativa empurra por cima da linha. E ainda assim reperfundir vale a pena, porque o mesmo gesto salva toda a população que estava um degrau atrás. O objetivo nunca foi salvar todas as células; foi salvar o máximo possível delas.

#atencao-box("Reperfundir tarde não é o mesmo que reperfundir cedo", [
  A leitura ingênua conclui que, se reperfundir salva células, reperfundir sempre compensa — a qualquer momento. O mecanismo diz outra coisa. O benefício da reperfusão vem do resgate das células que ainda estão na faixa reversível, e essa população encolhe minuto a minuto. O custo — o pico oxidativo, a sobrecarga de cálcio, a inflamação que chega com o fluxo — permanece. Passado o tempo em que a maior parte do tecido já morreu, o ganho se aproxima de zero enquanto o custo continua de pé; estudos de reperfusão miocárdica muito tardia, além de vinte e quatro horas do evento agudo, mostram benefício mínimo. Não é retórica dizer que tempo é músculo: é a descrição literal da curva.
])

#clinica-box("Transplante renal: isquemia fria e função retardada do enxerto", [
  Entre a retirada do rim do doador e a sua reperfusão no receptor há um intervalo em que o órgão fica praticamente sem oxigênio — refrigerado justamente para reduzir a demanda metabólica e retardar a queda de ATP. Ainda assim, células tubulares vão acumulando lesão reversível durante esse tempo. Quando o cirurgião libera o clampe e o sangue volta, o pico de radicais livres e a sobrecarga de cálcio empurram parte dessas células para a morte, e o enxerto costuma funcionar abaixo do esperado nos primeiros dias — a chamada função retardada do enxerto. A recuperação vem em seguida, à medida que o epitélio tubular sobrevivente prolifera e repõe as células perdidas. Toda a logística do transplante — pressa, refrigeração, soluções de preservação — existe para encurtar esse intervalo e diminuir a profundidade dessa queda.
])

#subtopico("3.3 — Proteínas mal dobradas e dano direto ao DNA: a rota que ignora a cascata")

Nem toda lesão passa pela queda de ATP. Há duas rotas que agridem a célula por caminhos próprios, e reconhecê-las evita aplicar o raciocínio da isquemia onde ele não cabe.

A primeira é a das proteínas mal dobradas. Uma proteína recém-sintetizada só funciona se assumir a conformação tridimensional correta, e o retículo endoplasmático mantém um controle de qualidade para garantir isso: as #termo-nota[chaperonas][proteínas que auxiliam o dobramento correto de outras proteínas e tentam redobrar as que assumiram conformação errada] reconhecem cadeias mal dobradas e tentam redobrá-las. Quando a redobragem falha repetidamente, a proteína recebe uma marcação química e é encaminhada para degradação pelo sistema do proteassoma. É importante separar os dois papéis, que costumam ser confundidos: a chaperona *tenta consertar*; quem *destrói* é o proteassoma.

Se as proteínas anômalas se acumulam mais rápido do que esse sistema consegue processar, a célula dispara a resposta ao acúmulo de proteínas não-dobradas: freia a tradução para não piorar o congestionamento, aumenta a produção de chaperonas e acelera a degradação. É uma resposta adaptativa — a mesma lógica do começo da PARTE I, aplicada a um estresse molecular. E, como toda adaptação, tem limite: se o acúmulo persiste, a própria via desvia para a ativação de morte celular, tipicamente por apoptose.

A doença de Creutzfeldt-Jakob mostra o mecanismo em sua forma mais crua. A proteína priônica normal existe no neurônio; na doença, uma cópia em conformação anômala funciona como molde e impõe a própria dobra às cópias normais que encontra, num processo autocatalítico. A forma anômala resiste à degradação, acumula-se, e o neurônio dispara sinalização de morte. Não há material genético do agente envolvido — o "infeccioso" aqui é uma conformação. O mesmo princípio geral, em versões menos dramáticas, aparece em doenças em que uma mutação faz a proteína dobrar errado e ser destruída antes de chegar ao seu destino.

A segunda rota é o dano direto ao material genético — radiação ionizante, agentes quimioterápicos, produtos químicos que se ligam ao DNA, além dos radicais livres já discutidos. Quando o dano é pequeno, os sistemas de reparo o corrigem. Quando é extenso demais, a célula ativa vias que interrompem o ciclo celular e, se o reparo não for possível, aciona a apoptose. *Esse desfecho é protetor:* uma célula com genoma gravemente comprometido que continuasse a se dividir seria um risco maior para o organismo do que a sua perda.

#esquema(
  grid(
    columns: (1fr, 12pt, 1fr, 12pt, 1fr),
    align: horizon,
    row-gutter: 7pt,
    esq-caixa("Proteína mal dobrada", [erro de dobramento, mutação ou estresse], cor: slate),
    esq-seta,
    esq-caixa("Chaperonas", [tentam redobrar], cor: teal),
    esq-seta,
    esq-caixa("Proteassoma", [degrada o que não se recupera], cor: teal),
    grid.cell(colspan: 5, align(center, text(size: 7.5pt, style: "italic", fill: text-light, [se o acúmulo supera a capacidade do sistema ↓]))),
    grid.cell(colspan: 2, esq-caixa("Resposta ao acúmulo", [freia tradução, aumenta chaperonas], cor: gold)),
    esq-seta,
    grid.cell(colspan: 2, esq-caixa("Apoptose", [quando a adaptação não resolve], cor: violet)),
  ),
  legenda: [O controle de qualidade das proteínas e o ponto em que ele se rende. Repare que a sequência repete o esquema geral da PARTE I — estímulo, tentativa de adaptação, e morte celular quando a adaptação não dá conta —, só que em escala molecular e sem passar pela queda de ATP.],
)

#subtopico("3.4 — Os dois destinos: necrose e apoptose")

A célula que atravessou o ponto sem retorno segue por um de dois caminhos, e a diferença entre eles não é de grau, é de natureza.

A *necrose* é sempre patológica e é o desfecho da falência energética. A célula, já inchada pelo influxo de sódio e água, tem a membrana rompida e derrama o conteúdo no interstício. As hidrolases lisossomais liberadas digerem a célula por dentro, e enzimas de células vizinhas e de leucócitos completam o serviço — o resultado é um contorno celular borrado, citoplasma intensamente corado e restos celulares. O núcleo percorre uma sequência característica: primeiro se retrai e escurece — picnose —, depois se fragmenta — cariorrexe — e por fim se dissolve, restando um espaço vazio onde ele estava — cariólise. Como o conteúdo derramado inclui moléculas que o sistema imune reconhece como sinal de dano, a necrose é sempre acompanhada de inflamação. E, como a PARTE I já antecipou, essas alterações levam horas para se tornarem visíveis ao microscópio de luz, mesmo que a célula esteja morta desde o começo.

A necrose ainda assume padrões diferentes conforme o tecido e a causa, e o padrão informa a etiologia. A necrose *coagulativa*, em que a arquitetura do tecido permanece reconhecível por algum tempo, é a da isquemia na maioria dos órgãos. A *liquefativa*, em que o tecido se dissolve em massa amolecida, é a do sistema nervoso central e a das infecções por bactérias piogênicas. A *caseosa*, com aspecto de queijo esfarelado, é característica da tuberculose. A *gordurosa* aparece quando lipases liberadas destroem tecido adiposo — exatamente o que ocorre na pancreatite, fechando o círculo com a lipase elevada no sangue. E a *fibrinoide* aparece na parede de vasos lesados por deposição de complexos imunes.

A *apoptose* é o oposto em quase todos os aspectos. É um programa ativo, dependente de energia, que pode ser fisiológico — na modelagem de estruturas durante o desenvolvimento, na renovação de epitélios, na eliminação de linfócitos autorreativos — ou patológico, quando o dano ao DNA ou o acúmulo de proteínas anômalas o aciona. A célula *encolhe* em vez de inchar, a cromatina se condensa em massas densas junto à membrana nuclear, e o conteúdo é empacotado em fragmentos envoltos por membrana íntegra, os corpos apoptóticos. Nada vaza. A célula em apoptose expõe na face externa da membrana um fosfolipídeo que normalmente fica voltado para dentro — a fosfatidilserina —, e essa exposição funciona como sinal de reconhecimento para que macrófagos e células vizinhas a fagocitem antes que ela se rompa. Por isso não há inflamação: o conteúdo nunca chega ao interstício.

#tabela-nebli(
  ("", "Necrose", "Apoptose"),
  (
    ([*Natureza*], [sempre patológica; falência energética], [programa ativo; fisiológica ou patológica]),
    ([*Energia*], [ocorre justamente por falta de ATP], [depende de ATP para ser executada]),
    ([*Volume celular*], [aumenta — a célula incha], [diminui — a célula encolhe]),
    ([*Membrana*], [rompe; conteúdo extravasa], [permanece íntegra; corpos apoptóticos]),
    ([*Núcleo*], [picnose → cariorrexe → cariólise], [cromatina condensada em massas densas]),
    ([*Inflamação*], [sempre presente], [ausente — fagocitose silenciosa]),
    ([*Extensão*], [grupos de células contíguas], [célula isolada em meio a células sadias]),
  ),
  colunas: (0.85fr, 1.5fr, 1.5fr),
)

#confusao-prevista(
  titulo: "Não é a intensidade do dano que escolhe entre necrose e apoptose",
  aluno_acha: [aluno acha que dano leve leva à apoptose e dano grave leva à necrose, como se fossem dois graus da mesma escala],
  mecanismo: [o mesmo estímulo pode produzir os dois desfechos, e o parâmetro decisivo é o *ATP disponível*. A apoptose é um programa que consome energia: clivar substratos, condensar cromatina, empacotar o conteúdo em corpos com membrana íntegra. Numa isquemia profunda não há ATP para executar nada disso, e a célula desmonta passivamente — necrose. Numa agressão mais lenta, com energia preservada, a mesma célula executa o programa e morre em silêncio. A intensidade influencia porque influencia o ATP, não porque exista uma escala de gravidade.],
)

#conclusao-box[
  *O princípio que amarra tudo.* Uma célula viva é um conjunto de gradientes mantidos contra a tendência natural ao equilíbrio, e manter gradiente custa energia. Toda a patologia da lesão celular é a história do que acontece quando esse pagamento é interrompido: o sódio entra, a água segue, o cálcio escapa dos reservatórios, a membrana se desorganiza. Adaptação, lesão reversível, lesão irreversível e morte não são quatro doenças — são quatro posições numa mesma linha, e o que define a posição é a relação entre a intensidade da agressão, a sua duração e a capacidade daquela célula de sustentar a manutenção.

  *O mecanismo nuclear.* Na isquemia, a queda de ATP para as bombas e desencadeia edema, acidose e desligamento da síntese proteica; a mitocôndria abre o poro de transição, apaga o que restava de produção energética e, pela outra porta, libera citocromo c; o cálcio citosólico ativa fosfolipases, proteases, endonucleases e ATPases; e os radicais livres peroxidam o que a membrana ainda tinha de organizado. Os quatro processos se realimentam e convergem sobre a mesma estrutura. Quando a membrana perde a integridade e o DNA é destruído em extensão suficiente, a linha foi cruzada — e o quanto de ATP sobrou decide se a célula morre desmontando-se passivamente, em necrose, ou executando um programa ordenado, em apoptose.

  *A clínica que sai daí.* Enzima intracelular na circulação significa membrana rompida: troponina e creatina-quinase MB no infarto, lipase e amilase na pancreatite, mioglobina e creatina-quinase na rabdomiólise. Dor torácica isquêmica com troponina normal é lesão reversível — e célula que ainda pode ser salva. Reabrir o vaso é o tratamento, apesar de o próprio ato de reperfundir gerar um pico oxidativo que mata parte das células limítrofes, porque o resgate das demais compensa; e como a população resgatável encolhe minuto a minuto, o benefício depende inteiramente do tempo. Todos os protocolos de urgência da isquemia — coronária, cerebral, de membro, de enxerto — são a tradução prática dessa curva.

  *O passo seguinte.* Com os mecanismos de lesão de pé, o estudo da patologia geral avança em duas direções que já apareceram aqui de relance. Para trás, o detalhamento das adaptações — hipertrofia, hiperplasia, atrofia e metaplasia — como respostas organizadas ao estresse crônico, e os acúmulos intracelulares que sinalizam desequilíbrio metabólico. Para a frente, a resposta do tecido àquilo que a célula morta derrama: a inflamação, e depois o reparo, a cicatrização e a fibrose. A lesão celular é o vocabulário; o que vem depois é a gramática com que o organismo responde a ela.
]
