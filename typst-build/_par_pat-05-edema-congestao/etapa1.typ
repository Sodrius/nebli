#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Edema e congestão são o mesmo tipo de problema visto de lados opostos da parede do vaso. No *edema*, água sai do capilar e fica onde não deveria — no interstício ou numa cavidade serosa. Na *congestão*, é o sangue que não consegue sair do órgão e se acumula dentro dos vasos. O elo entre os dois é mecânico: o capilar congesto está sob pressão alta, e pressão alta empurra líquido para fora.

A PARTE I monta o balanço que mantém o líquido no lugar — as forças que atravessam a parede do capilar, o dreno linfático e a qualidade do líquido que escapa. A PARTE II mostra as maneiras de romper esse balanço, cada uma com a sua doença-modelo. A PARTE III vai ao fígado e ao pulmão e mostra o que o patologista vê quando o balanço falhou.
]

#parte-title("PARTE I — O balanço que mantém o líquido no lugar", primeira: true)

#subtopico("1.1 — Edema, hiperemia e congestão")

*Edema* é o acúmulo anormal de líquido no interstício — o espaço extracelular fora dos vasos — ou nas cavidades revestidas por serosa. A definição exclui de propósito o inchaço de dentro da célula: a tumefação celular da lesão reversível nasce da falha das bombas iônicas da membrana, não da troca entre sangue e tecido. A água corporal equivale a cerca de 60% do peso; um terço dela é extracelular, e desse terço aproximadamente três quartos estão no interstício e só um quarto circula como plasma. Como o interstício é três vezes maior que o plasma e sua matriz de colágeno e glicosaminoglicanos absorve água antes de inchar à vista, alguns litros podem se acumular antes que o edema apareça no exame. O peso sobe antes do inchaço.

Hiperemia e congestão descrevem outro excesso: sangue demais *dentro* dos vasos de um tecido. A diferença está na direção do defeito. A *hiperemia* é ativa: arteríolas se dilatam — por metabólitos locais no músculo em exercício, por mediadores na inflamação — e mais sangue arterial entra no leito, deixando o tecido vermelho vivo e quente, como a conjuntiva da lâmina de definições. A *congestão* é passiva: a entrada é normal, mas a saída venosa está dificultada, e o sangue se acumula no leito. Como esse sangue estagnado já cedeu oxigênio, a hemoglobina desoxigenada dá ao tecido cor vermelho-escura a azulada, a cianose. A congestão pode ser local, quando uma veia é obstruída, ou sistêmica, quando o coração não dá conta do retorno venoso.

#figura-nebli("/figuras/pat-05-edema-congestao/slide-03.png",
  largura: 70%,
  legenda: [Os três fenômenos da lâmina de definições. À esquerda, glomérulo com capilares distendidos por hemácias — congestão ao microscópio. À direita, conjuntiva vermelho-viva de hiperemia ativa. Abaixo, membro inferior edemaciado, com bolhas na pele distendida.])

Os dois raramente andam sozinhos. Um leito congesto tem pressão venosa e capilar elevadas, e pressão alta dentro do capilar empurra líquido para o interstício: congestão e edema aparecem juntos, o que o slide resume como limitação de fluxo, parcial ou total. *Quando a congestão se prolonga, o custo deixa de ser só volume.* O sangue parado oferece menos oxigênio às células mais distantes da chegada arterial, que degeneram ou morrem; capilares distendidos se rompem em micro-hemorragias; macrófagos fagocitam as hemácias extravasadas e acumulam #termo-nota[hemossiderina][pigmento castanho-dourado, rico em ferro, formado pela degradação da hemoglobina dentro de macrófagos]; e o interstício responde com fibrose. É esse percurso que a PARTE III reencontra no pulmão e no fígado.

#mini-resumo[Em uma frase: hiperemia é entrada ativa de sangue arterial; congestão é saída venosa dificultada; edema é líquido fora do vaso — e o capilar congesto, sob pressão, produz edema.]

#subtopico("1.2 — As forças de Starling e o dreno linfático")

Quatro forças decidem o movimento de água através da parede do capilar, e o conjunto leva o nome de *forças de Starling*. A *pressão hidrostática capilar* é a pressão do sangue contra a parede e empurra líquido para fora; é maior na extremidade arteriolar e cai ao longo do trajeto. A *pressão oncótica plasmática*, ou coloidosmótica, é a pressão osmótica gerada pelas proteínas que não atravessam a parede — sobretudo a albumina — e retém água dentro do vaso. Do lado de fora atuam a pressão hidrostática do interstício e a pressão oncótica do interstício, esta dada pela pouca proteína que escapou. O fluxo de líquido através da parede reúne as quatro numa só relação:

$ J_v = K_f dot ((P_c - P_i) - sigma dot (pi_c - pi_i)) $

Lida da esquerda para a direita, a relação diz que o fluxo para fora (J#sub[v]) é a diferença de pressão hidrostática entre capilar e interstício menos a diferença de pressão oncótica, multiplicada pela condutância hidráulica da parede (K#sub[f]). O termo $sigma$, o *coeficiente de reflexão*, mede quanto a parede barra a proteína: vale perto de 1 quando a albumina é quase toda retida e cai quando a parede passa a deixá-la escapar. *O ponto fino está em $sigma$.* A mesma pressão oncótica segura muita água num capilar íntegro e quase nenhuma num capilar inflamado — é daí que parte o edema de permeabilidade da PARTE II.

O esquema clássico, reproduzido no slide, divide o capilar em duas metades: na extremidade arteriolar a pressão hidrostática vence e o líquido é filtrado; na venular, a pressão hidrostática já caiu abaixo da oncótica e o líquido seria reabsorvido, sobrando um pequeno excedente para a linfa. Medidas diretas pediram um ajuste. Na maioria dos tecidos há filtração discreta ao longo de todo o capilar, inclusive nas vênulas, e a reabsorção venular é transitória — aparece, por exemplo, logo após uma hemorragia, quando a pressão capilar despenca.

#figura-nebli("/figuras/pat-05-edema-congestao/slide-04.png",
  largura: 52%,
  legenda: [O esquema clássico: filtração na extremidade arterial, retorno na venosa e excedente recolhido pela rede linfática até o ducto torácico. O texto explica por que a reabsorção venular sustentada é hoje considerada exceção.])

O gradiente oncótico que conta é o que se forma logo abaixo do #termo-nota[glicocálice][camada de glicoproteínas e proteoglicanos que reveste a face luminal do endotélio e funciona como a verdadeira peneira de proteínas da parede], e não o do interstício como um todo; reabsorção sustentada só existe em leitos especializados, como a mucosa intestinal e os capilares peritubulares do rim. Para o raciocínio sobre edema, os dois modelos levam à mesma conclusão: o que é filtrado e não volta pelo capilar precisa deixar o interstício pela linfa.

Os linfáticos começam em fundo cego no tecido, com células endoteliais sobrepostas como abas, que se abrem quando o interstício incha, tracionadas por filamentos de ancoragem presos à matriz. Por essas abas entram água e proteína — e remover a proteína importa tanto quanto remover o volume, porque mantém baixa a pressão oncótica do interstício. A linfa atravessa os linfonodos e chega ao ducto torácico, que desemboca na junção da veia subclávia esquerda com a jugular interna. O dreno tem reserva: quando a filtração aumenta, o fluxo linfático pode subir várias vezes antes que o líquido se acumule, e a própria pressão do interstício, ao subir, freia a saída. Edema aparece quando a filtração supera essa capacidade, ou quando o dreno está bloqueado.

#mini-resumo[Se você só lembrar de uma coisa: edema = filtração maior que a drenagem linfática — seja por excesso de filtração, seja por dreno obstruído.]

#subtopico("1.3 — Transudato, exsudato e o nome das coleções")

O líquido que escapa carrega a assinatura do mecanismo que o fez escapar. Quando a parede do capilar está íntegra e o desequilíbrio é só de forças — pressão hidrostática alta ou oncótica baixa —, o que atravessa é um #termo-nota[ultrafiltrado][líquido que passou por uma barreira seletiva, levando água e pequenos solutos e retendo proteínas e células] do plasma: água e eletrólitos, pouca proteína, quase nenhuma célula. É o *transudato*, claro e de densidade baixa, abaixo de cerca de 1,012. Quando a própria parede fica permeável, passam proteínas grandes, fibrinogênio e leucócitos, e o líquido é um *exsudato*: turvo, denso — acima de cerca de 1,020 —, rico em proteína e células. Na clínica, a comparação é feita com o sangue do próprio paciente: razão alta entre a proteína do líquido e a do soro, ou #sigla("DHL", [desidrogenase láctica — enzima intracelular que se eleva no líquido quando há inflamação e lesão celular]) desproporcional no líquido, apontam exsudato.

À primeira vista, parece natural supor que muito líquido seja exsudato e pouco seja transudato — só que pressão, por maior que seja, não fabrica exsudato.

#confusao-prevista(
  titulo: "Transudato e exsudato não medem quantidade",
  aluno_acha: [aluno acha que transudato é edema leve e exsudato é edema intenso],
  mecanismo: [os dois nomes descrevem a composição do líquido, e a composição denuncia o mecanismo. Uma insuficiência cardíaca grave enche a pleura com litros de transudato porque a barreira continua retendo a albumina; uma pleurite inicial produz pouco volume, mas exsudato desde o início, porque a parede já está permeável. Composição revela o porquê; volume mede a intensidade.],
)

Quando o líquido se acumula numa cavidade serosa, recebe o nome da cavidade: *hidrotórax* na pleura, *hidropericárdio* no saco pericárdico e *hidroperitônio*, quase sempre chamado de *ascite*, no peritônio. Edema subcutâneo grave e generalizado, que infiltra o corpo inteiro, é *anasarca*. Os nomes dizem onde o líquido está, não por que chegou lá: um hidrotórax pode ser transudato de insuficiência cardíaca ou exsudato de pneumonia.

#figura-nebli("/figuras/pat-05-edema-congestao/slide-06.png",
  largura: 68%,
  legenda: [Coleções à autópsia. À esquerda, líquido citrino na cavidade pleural sobre o pulmão (hidrotórax). À direita, saco pericárdico distendido por líquido (hidropericárdio).])

No subcutâneo, o edema pobre em proteína se desloca sob pressão: o dedo comprimido contra o osso deixa uma depressão que demora a desaparecer, o #termo-nota[sinal do cacifo][depressão persistente após compressão digital do tecido edemaciado, também chamado sinal de Godet]. A distribuição também informa. O edema de causa hidrostática sistêmica obedece à gravidade — tornozelos em quem está de pé, região sacral em quem está acamado — e por isso é chamado *dependente*. Nos estados de albumina baixa e nas doenças renais, o edema aparece cedo nas pálpebras, onde o tecido conjuntivo é frouxo e oferece pouca resistência. Quando a causa é uma veia ou um linfático obstruído, o edema é localizado e assimétrico, restrito ao território drenado.

#parte-title("PARTE II — As maneiras de romper o balanço")

#subtopico("2.1 — Pressão hidrostática: do obstáculo venoso à insuficiência cardíaca")

A pressão hidrostática capilar sobe quase sempre por dificuldade de escoamento venoso, que se transmite de trás para a frente até o capilar. O alcance do edema depende de onde está o obstáculo. Uma #sigla("TVP", [trombose venosa profunda — trombo numa veia profunda, em geral da perna]) eleva a pressão só a montante dela: aquele membro incha, o outro não. Compressão de uma veia por tumor e a estase de quem passa horas de pé sem contrair a panturrilha seguem a mesma lógica, sempre local.

Quando o obstáculo é o próprio coração, o edema é generalizado, e a insuficiência cardíaca soma dois braços. O primeiro é mecânico: o ventrículo que falha ejeta menos, o sangue não ejetado aumenta a pressão de enchimento, e essa pressão se transmite para as veias e os capilares a montante. O segundo é renal. Com menos débito, a perfusão do rim cai, e o aparelho justaglomerular libera renina, que inicia a cascata do #sigla("SRAA", [sistema renina-angiotensina-aldosterona — eixo hormonal que contrai arteríolas e retém sódio e água quando o rim percebe perfusão baixa]): a angiotensina II contrai arteríolas e estimula a aldosterona, que faz o túbulo reabsorver sódio, e a água acompanha. O rim, que está sadio, responde corretamente ao que percebe — um volume arterial efetivo baixo.

#figura-nebli("/figuras/pat-05-edema-congestao/slide-08.png",
  largura: 60%,
  legenda: [O círculo da insuficiência cardíaca: a queda do volume ejetado ativa o SRAA, sódio e água são retidos, e o volume circulante maior sobrecarrega o miocárdio já disfuncional — remodelamento, mais consumo de oxigênio, mais rigidez.])

O que fecha o círculo é que o volume retido não conserta o coração doente. Num coração sadio, mais retorno venoso aumentaria o débito; no coração que falha, aumenta a pressão de enchimento e a congestão sem corrigir a ejeção. A sobrecarga ainda estimula remodelamento ventricular, maior consumo de oxigênio e rigidez da parede, que agravam a disfunção. *A resposta renal, adequada em si, alimenta a congestão que a disparou.* Parte dessa resposta é contrabalançada pelos peptídeos natriuréticos liberados pelas câmaras distendidas, que promovem excreção de sódio, mas na falência avançada esse freio não vence a ativação do SRAA.

#mini-resumo[O que ficou de pé: na insuficiência cardíaca, o edema nasce da pressão venosa transmitida e cresce com a retenção renal de sódio, que responde a um volume arterial efetivo baixo.]

Qual metade do coração falha decide onde o líquido aparece. Na falência esquerda, o sangue represa nas veias pulmonares, e o resultado é congestão e edema do pulmão — é assim que um infarto extenso do ventrículo esquerdo produz edema pulmonar de causa hidrostática, com transudato no alvéolo. Na falência direita, o represamento acontece nas veias sistêmicas: jugulares ingurgitadas, fígado congesto, edema dependente dos membros e, com o tempo, derrames e ascite. Como a causa mais comum de falência direita é a própria falência esquerda prolongada, o quadro avançado costuma combinar os dois territórios.

#subtopico("2.2 — Pressão oncótica baixa e retenção de sódio")

A albumina é produzida pelo fígado e responde pela maior parte da pressão oncótica do plasma, por ser a proteína plasmática mais abundante em número de moléculas. Sua concentração cai por perda ou por produção insuficiente. A perda mais expressiva é renal: na *síndrome nefrótica*, a barreira de filtração do glomérulo — endotélio fenestrado, membrana basal e podócitos — é lesada e deixa passar proteína em grande quantidade, mais de 3,5 g por dia no adulto. A produção cai na doença hepática difusa e na desnutrição proteica grave. Com menos albumina, a força que segura água no vaso diminui em todos os leitos capilares ao mesmo tempo, e o edema é generalizado.

A explicação clássica do edema nefrótico parte daí: líquido sai do vaso, o volume plasmático cai, o rim ativa o SRAA e retém sódio — retenção *secundária*, na mesma lógica da insuficiência cardíaca. O esquema da aula mostra que essa não é a história toda. Muitos pacientes nefróticos têm volume plasmático normal ou aumentado e renina baixa, sinal de que o rim retém sódio por conta própria: é a retenção *primária*. Duas vias levam a ela no esquema. No túbulo, o infiltrado inflamatório do interstício — linfócitos T e macrófagos — aumenta a angiotensina II local e reduz o óxido nítrico, e a reabsorção de sódio sobe. No glomérulo, a lesão reduz a área de filtração, e o sódio filtrado cai. Trabalhos mais recentes somam uma terceira peça: proteases filtradas com a proteinúria ativam o canal epitelial de sódio do ducto coletor.

#figura-nebli("/figuras/pat-05-edema-congestao/slide-10.png",
  largura: 66%,
  legenda: [Edema nefrótico por dois ramos. À direita, a hipoalbuminemia reduz a pressão oncótica. À esquerda, a lesão tubulointersticial e glomerular produz retenção primária de sódio, que expande o volume e eleva a pressão capilar. Os dois ramos convergem para superar os mecanismos de remoção.])

O sódio retido expande o volume e eleva a pressão hidrostática capilar, enquanto a hipoalbuminemia reduz a oncótica: *os dois lados da equação de Starling empurram no mesmo sentido.* Dito de outro modo, o edema nefrótico não é só falta de albumina — o rim doente continua retendo sódio, e é por isso que o edema resiste a tentativas de corrigir apenas um dos termos.

A retenção primária de sódio também explica o edema da insuficiência renal, aguda ou crônica. O rim que filtra pouco excreta pouco sódio, a água acompanha o sódio retido e o volume extracelular se expande, elevando a pressão hidrostática capilar e diluindo as proteínas do plasma ao mesmo tempo. A diferença para a insuficiência cardíaca está em quem começa: lá o rim sadio responde a um sinal de volume baixo; aqui o rim doente é a causa.

#subtopico("2.3 — Linfa obstruída e parede permeável")

Na obstrução linfática, nenhuma força de Starling mudou: a filtração continua a de um tecido normal, mas o excedente diário não tem por onde sair. Como o linfático também removia a proteína escapada, o líquido acumulado é rico em proteína, que atrai mais água e estimula fibroblastos. O resultado é o *linfedema* — instalação lenta, restrito ao território drenado, mole no início e, com os meses, firme, com pele espessada e sem cacifo, porque o interstício fibrosou. As causas vêm de outros capítulos da patologia: tumor que invade ou comprime linfáticos, retirada cirúrgica e irradiação de linfonodos — o linfedema do braço após esvaziamento axilar — e infecções como a filariose, em que o verme adulto nos linfáticos provoca inflamação e fibrose até o extremo da elefantíase. Quando um carcinoma de mama ocupa os linfáticos da derme, a pele edemaciada fica presa nos pontos em que ligamentos a ancoram à fáscia, e surge o aspecto em casca de laranja.

#figura-nebli("/figuras/pat-05-edema-congestao/slide-07.png",
  largura: 84%,
  legenda: [Obstrução linfática: linfedema unilateral do membro inferior e mama volumosa, avermelhada, com edema da pele. À direita, coleção turva em cavidade serosa à autópsia — a turbidez indica líquido com proteína, lipídio ou células em abundância, diferente do transudato límpido da lâmina anterior.])

O último mecanismo rompe a premissa dos anteriores: a parede deixa de ser peneira. Na inflamação aguda, histamina, bradicinina e leucotrienos contraem as células endoteliais das vênulas pós-capilares e abrem fendas entre elas em minutos — resposta rápida e passageira. Citocinas como a #sigla("IL-1", [interleucina 1 — citocina pró-inflamatória produzida sobretudo por macrófagos]) e o #sigla("TNF", [fator de necrose tumoral — citocina pró-inflamatória que ativa o endotélio]) reorganizam o citoesqueleto endotelial ao longo de horas e sustentam o vazamento. Lesão direta do endotélio por queimadura, toxina ou infecção grave, e lesão causada por neutrófilos aderidos à parede, produzem vazamento mais prolongado. Na equação de Starling, é o coeficiente de reflexão que cai: a albumina escapa, a pressão oncótica deixa de reter água, e sai um líquido rico em proteína, fibrina e leucócitos — o exsudato.

Quando esse vazamento é difuso num órgão inteiro, deixa de ser um edema entre outros e vira síndrome. No pulmão, é o dano alveolar difuso da PARTE III. Numa infecção sistêmica grave, o vazamento em muitos leitos ao mesmo tempo explica por que o pulmão de um paciente séptico se enche de líquido sem que o coração tenha falhado: a pressão de enchimento está normal ou baixa, e o edema é de permeabilidade.

#mini-resumo[Em resumo: pressão hidrostática alta, oncótica baixa e retenção de sódio produzem transudato com parede íntegra; a obstrução linfática acumula líquido rico em proteína por falta de remoção; só a permeabilidade aumentada produz exsudato inflamatório.]

#parte-title("PARTE III — O que o patologista vê")

#subtopico("3.1 — A morfologia do edema e da congestão")

O edema se vê melhor a olho nu do que ao microscópio. No subcutâneo, a pele fica lisa e tensa, com as pregas apagadas; na superfície de corte, o tecido é pálido e úmido e goteja líquido claro. Ao microscópio, o achado é discreto: fibras de colágeno e células ficam afastadas por espaços claros ou por um material levemente róseo e granular — o líquido com a pouca proteína que a fixação precipitou. Não há infiltrado nem necrose, só distância aumentada entre estruturas que deveriam estar próximas. No pulmão, o mesmo material aparece preenchendo os alvéolos.

A congestão, ao contrário, salta aos olhos no microscópio: capilares e vênulas distendidos, abarrotados de hemácias, como os glomérulos da lâmina de definições. O órgão congesto está aumentado, pesado e vermelho-escuro, e sangue escorre da superfície de corte. Na congestão aguda o quadro é reversível; na crônica, hipóxia, micro-hemorragias e fibrose deixam marcas permanentes, e dois órgãos as mostram com clareza — o pulmão atrás do ventrículo esquerdo e o fígado atrás do direito.

No pulmão, a congestão crônica da falência esquerda deixa uma sequência característica. Os capilares alveolares ingurgitados se rompem em pequenas hemorragias dentro dos alvéolos; os macrófagos alveolares fagocitam as hemácias, degradam a hemoglobina e acumulam hemossiderina, e passam a ser chamados de *células da insuficiência cardíaca*. O nome engana: não é uma linhagem própria, e sim o macrófago alveolar comum carregado de pigmento castanho, que a reação de Perls cora de azul. Os septos alveolares espessam e fibrosam, e o pulmão fica firme e acastanhado — a *induração parda*. O septo espessado aumenta a distância que o oxigênio precisa atravessar, o que agrava a falta de ar desses pacientes.

#subtopico("3.2 — O fígado: noz-moscada e a ascite da cirrose")

O fígado mostra a congestão passiva crônica com nitidez, e a nitidez vem da arquitetura do lóbulo. O sangue entra pela periferia, pelos ramos da veia porta e da artéria hepática, percorre os sinusoides e sai pela veia centrolobular; o hepatócito vizinho à veia central, na #termo-nota[zona 3][região centrolobular do ácino hepático, a última a receber sangue oxigenado e por isso a mais sensível à hipóxia], é o último a receber oxigênio. Na falência direita, a pressão das veias hepáticas sobe até as centrolobulares, os sinusoides dessa região se distendem de sangue, e os hepatócitos centrolobulares sofrem atrofia e, se a hipóxia é intensa, necrose; os periportais, mais bem oxigenados, sobrevivem, às vezes com esteatose. No corte, áreas centrais vermelho-escuras e deprimidas alternam com parênquima periportal pálido — o desenho da noz-moscada cortada, que dá nome ao *fígado em noz-moscada*. Anos de congestão depositam colágeno em torno das veias centrais, uma fibrose de origem hemodinâmica.

#figura-nebli("/figuras/pat-05-edema-congestao/slide-12.png",
  largura: 72%,
  legenda: [À esquerda, abdome distendido por ascite volumosa. À direita, de cima para baixo: superfície nodular do fígado cirrótico; superfície de corte mosqueada do fígado em noz-moscada, ao lado da própria noz-moscada; e, ao microscópio, sinusoides distendidos por hemácias em torno da veia central, com a periferia do lóbulo preservada.])

A ascite do fígado cirrótico da mesma lâmina segue outro caminho, que soma quase todos os mecanismos da PARTE II. A fibrose e os nódulos de regeneração distorcem os sinusoides e aumentam a resistência ao fluxo portal: é a *hipertensão portal*. A pressão sinusoidal alta aumenta a formação de linfa hepática além do que o ducto torácico consegue drenar, e o excesso passa para o peritônio; a síntese reduzida de albumina diminui a pressão oncótica.

O passo decisivo é o menos intuitivo. A hipertensão portal induz a liberação de vasodilatadores — sobretudo #sigla("NO", [óxido nítrico — gás vasodilatador produzido pelo endotélio]) — no território esplâncnico. As arteríolas intestinais se dilatam, e o leito arterial fica grande demais para o sangue disponível: o #termo-nota[volume arterial efetivo][parte do volume sanguíneo que efetivamente enche o leito arterial e é percebida pelos barorreceptores; pode estar baixa mesmo com volume total alto] cai, embora o volume total não tenha caído. Barorreceptores e rim leem subenchimento e ativam o SRAA, o simpático e o #sigla("ADH", [hormônio antidiurético, ou vasopressina — retém água no ducto coletor]). O sódio e a água retidos não ficam no vaso, porque escapam para o peritônio pelas forças já descritas, e a ascite cresce. Na mesma cascata, a vasoconstrição renal intensa reduz a filtração glomerular até a *síndrome hepatorrenal* — uma insuficiência renal funcional, de rins histologicamente normais.

#figura-lateral("/figuras/pat-05-edema-congestao/slide-11.png",
  lado: "right",
  largura-figura: 46%,
  texto: [O esquema da aula condensa a cascata: hipertensão portal, vasodilatação esplâncnica, queda do volume circulante efetivo, ativação do SRAA. Dali saem dois desfechos que parecem opostos e têm a mesma origem. De um lado, a avidez renal por sódio alimenta a ascite; de outro, a vasoconstrição renal leva à síndrome hepatorrenal. *Ou seja, o rim da cirrose retém sódio e perde filtração pelo mesmo motivo:* ele está respondendo a um subenchimento arterial que ele mesmo não consegue corrigir.],
  legenda: [Da hipertensão portal à ascite e à síndrome hepatorrenal.])

#mini-resumo[Em uma frase: a ascite da cirrose soma pressão sinusoidal alta, linfa hepática em excesso, albumina baixa e retenção renal de sódio disparada pela vasodilatação esplâncnica.]

#subtopico("3.3 — O pulmão: edema hemodinâmico e dano alveolar difuso")

O pulmão reúne lado a lado os dois grandes tipos de edema, e a morfologia os separa. No *edema hemodinâmico*, a falência do ventrículo esquerdo eleva a pressão nos capilares alveolares; o líquido filtrado primeiro alarga os septos e depois transborda para os alvéolos. Os pulmões ficam pesados e úmidos, e a compressão da superfície de corte faz sair líquido espumoso, às vezes rosado — transudato batido com o ar. À radiografia, opacidades bilaterais e derrame que vela os seios costofrênicos; ao microscópio, capilares septais ingurgitados e alvéolos cheios de material róseo e homogêneo, com poucas células. Como a gravidade distribui o líquido, as bases são as mais comprometidas.

#figura-nebli("/figuras/pat-05-edema-congestao/slide-09.png",
  largura: 94%,
  legenda: [Edema pulmonar hemodinâmico em três registros, da esquerda para a direita: líquido espumoso na superfície de corte; radiografia com opacidades bilaterais e seios costofrênicos velados (setas vermelhas); e alvéolos preenchidos por material róseo homogêneo, com capilares septais ingurgitados.])

No *dano alveolar difuso*, a pressão capilar é normal, e o problema é a barreira alvéolo-capilar, formada pelo pneumócito tipo I e pelo endotélio. Um agente lesivo — infecção pulmonar, sepse, aspiração, trauma grave — ativa macrófagos alveolares, que liberam TNF, #sigla("IL-8", [interleucina 8 — quimiocina que recruta neutrófilos]) e IL-1. Os neutrófilos recrutados e ativados liberam #sigla("PAF", [fator ativador de plaquetas — mediador lipídico da inflamação]), leucotrienos, proteases e espécies reativas de oxigênio, que lesam o endotélio e os pneumócitos. Com a barreira destruída, plasma e sangue inundam o alvéolo; o fibrinogênio polimeriza em fibrina, e fibrina, proteína e restos de pneumócitos necróticos se depositam revestindo as paredes alveolares — as #termo-nota[membranas hialinas][faixas eosinofílicas densas de fibrina e restos celulares que revestem ductos e sacos alveolares no dano alveolar difuso]. A tradução clínica é a #sigla("SDRA", [síndrome do desconforto respiratório agudo — insuficiência respiratória aguda por dano alveolar difuso]), um edema não cardiogênico.

#figura-nebli("/figuras/pat-05-edema-congestao/slide-13.png",
  largura: 78%,
  legenda: [A cadeia do dano alveolar difuso: macrófagos ativados recrutam e ativam neutrófilos, cujos mediadores lesam endotélio e pneumócito até destruir a barreira alvéolo-capilar. À direita, o alvéolo normal ao lado do lesado, com neutrófilos, plasma extravasado e membrana hialina. O ramo dos fibroblastos antecipa a fibrose do reparo.])

Se o paciente sobrevive, pneumócitos tipo II proliferam para recobrir o epitélio perdido, e fibroblastos ativados depositam colágeno — o ramo do esquema que termina em pró-colágeno. Agressões extensas deixam fibrose intersticial residual.

#figura-lateral("/figuras/pat-05-edema-congestao/slide-15.png",
  lado: "left",
  largura-figura: 46%,
  texto: [Ao microscópio, o que separa os dois edemas é a membrana hialina. No hemodinâmico, o alvéolo está cheio de material róseo, mas sua parede é fina e não há revestimento. No dano alveolar difuso, faixas eosinofílicas densas acompanham o contorno das paredes alveolares, os septos estão alargados e celularizados, e há hemácias e células inflamatórias no espaço aéreo. *A membrana hialina é a assinatura morfológica do edema de permeabilidade.*],
  legenda: [Dano alveolar difuso: septos alargados e membranas hialinas revestindo os espaços aéreos (detalhe).])

#clinica-box("Dois pacientes, dois líquidos", [
Uma mulher de 70 anos com infarto extenso da parede anterior chega com falta de ar e opacidades pulmonares difusas. O ventrículo esquerdo não esvazia, a pressão nos capilares pulmonares sobe, e o alvéolo recebe transudato; é a queda dessa pressão que desfaz o edema. Um homem em choque séptico tem opacidades semelhantes, mas a pressão de enchimento do coração está normal ou baixa: citocinas circulantes e neutrófilos lesaram a barreira alvéolo-capilar, o líquido é exsudato e as membranas hialinas começam a se formar. A imagem se parece; mecanismo, composição do líquido e morfologia são opostos.
])

#conclusao-box[
O princípio que unifica o capítulo é que o líquido do corpo fica no lugar por um balanço de três termos: a pressão hidrostática que empurra água para fora do capilar, a pressão oncótica da albumina que a retém — com a parede do vaso barrando a proteína — e o dreno linfático que devolve o excedente. Edema é qualquer situação em que a filtração passa a exceder a drenagem; congestão é o mesmo problema visto de dentro do vaso, sangue que não sai e, sob pressão, empurra líquido para fora.

O mecanismo nuclear é identificar qual termo saiu da faixa. Pressão hidrostática alta, pressão oncótica baixa e retenção de sódio desequilibram forças com a parede íntegra e produzem transudato; a obstrução linfática deixa proteína no interstício e evolui para fibrose; o aumento de permeabilidade derruba a barreira e produz exsudato. A composição do líquido é a pista que entrega o mecanismo.

Na clínica, cada doença-modelo é uma dessas alavancas. Na insuficiência cardíaca, a pressão venosa transmitida se soma ao SRAA ativado por um volume arterial efetivo baixo, e a morfologia registra o tempo: células da insuficiência cardíaca e induração parda no pulmão, fígado em noz-moscada. Na síndrome nefrótica, a albumina perdida e a retenção primária de sódio produzem edema generalizado. Na cirrose, hipertensão portal, linfa hepática, albumina baixa e vasodilatação esplâncnica fazem a ascite, e a mesma vasoconstrição renal explica a síndrome hepatorrenal de rins normais. No pulmão, opacidades iguais podem ser transudato de falência esquerda ou exsudato com membranas hialinas.

Adiante, o mesmo balanço reaparece sempre que o fluxo desacelera ou o endotélio se altera. Sangue estagnado num leito congesto é sangue de fluxo lento, uma das condições que favorecem a formação de trombos — o membro edemaciado por uma trombose venosa junta os dois assuntos. E o rim que aqui retém sódio em resposta a sinais de volume é o regulador que volta em todo distúrbio de volume do organismo.
]
