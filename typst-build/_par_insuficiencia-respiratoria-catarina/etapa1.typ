#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Catarina A.P. tem 46 anos, é varredora de rua em Paulistania (PI), fumou um maço por dia durante dez anos e parou quando o neto nasceu. Diabética. No dia 16 de fevereiro de 2026, procura a #sigla("UPA", [Unidade de Pronto Atendimento]) com tosse há uma semana, febre que ela não mediu e expectoração que começou branca e virou amarela há quatro dias. O médico do plantão a libera com amoxicilina e a frase de que "ela não deveria se preocupar". Quarenta e oito horas depois ela volta cianótica, sentada porque não consegue respirar deitada, com uma gasometria que mostra #sigla("pH", [potencial hidrogeniônico — medida da acidez/alcalinidade de uma solução]) 7,14 e #sigla("pCO\u{2082}", [pressão parcial de gás carbônico no sangue arterial]) 62. Vai para #sigla("UTI", [Unidade de Terapia Intensiva]) com suporte ventilatório e melhora em dez dias.

O que aconteceu nessas 48 horas é o assunto desta apostila. Vamos seguir uma rota fixa: primeiro entender o pulmão saudável (PARTE I), depois as quatro leis físico-químicas que governam a troca gasosa e o equilíbrio ácido-base (PARTE II), e só então entrar na trajetória da Catarina dia a dia, gasometria a gasometria, lendo cada achado pela lente das duas partes anteriores (PARTE III). No fim, você deve conseguir explicar não só *o que* aconteceu, mas *por que* uma paciente com pneumonia "risco 1" pode chegar à beira do óbito em 48h, e o que cada peça do quebra-cabeça contribuiu para isso.

Uma observação editorial: como você está no primeiro ano e provavelmente vai apresentar esse caso em #sigla("GD", [Grupo de Discussão — formato de aula tutorial com casos clínicos]), a apostila é generosa em tamanho porque o material é denso e exige construção de base antes da clínica. Não pule a PARTE II achando que o caso clínico é o que importa — sem ela, a PARTE III vira anedota sem mecanismo.
]

#parte-title("PARTE I — Como o pulmão funciona quando está saudável", primeira: true)

#subtopico("1.1 — Anatomia funcional: cano que vira esponja")

A função do pulmão acontece num único lugar: na parede onde o ar encontra o sangue. Toda a anatomia que vem antes — traqueia, brônquio, bronquíolo — existe para conduzir o ar até esse ponto de encontro. Por isso a melhor forma de entender a árvore respiratória é olhar para ela como um sistema de canos que vão afinando até virar uma esponja aerada na ponta.

O ar entra pela traqueia, um tubo único de cartilagem em forma de anéis abertos posteriormente. A traqueia se bifurca em dois brônquios principais — direito e esquerdo —, que vão se ramificando como uma árvore invertida, perdendo calibre e, mais importante, perdendo cartilagem. Quando você chega no nível do *bronquíolo terminal*, a cartilagem já não existe mais. Sem cartilagem, a parede do tubo depende inteiramente do tecido conjuntivo elástico ao redor para não colapsar — por isso o bronquíolo é tão vulnerável a broncoespasmo (basta o músculo liso da parede contrair, como na asma, para o tubo fechar).

A figura abaixo mostra essa árvore inteira numa única peça anatômica preservada, com as vias aéreas em amarelo e a vasculatura pulmonar em vermelho/azul; repare especialmente no detalhe do pulmão isolado à esquerda, que tem aparência de bucha porque a multiplicação alveolar transforma o que era cano em malha aerada.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-01.png",
  largura: 75%,
  legenda: [Anatomia macro pulmonar do slide da Prof.ª Marisa Doholnikoff. As vias aéreas em amarelo formam a árvore brônquica; em vermelho/azul, a vasculatura arterial/venosa pulmonar. O detalhe do pulmão isolado à esquerda mostra a textura esponjosa que vem da multiplicação alveolar — não é tecido sólido, é uma malha aerada.],
)

Depois do bronquíolo terminal vêm os *bronquíolos respiratórios*, e a partir daí começa a aparecer alvéolo na parede do próprio tubo. O alvéolo é o saco final, o destino do ar, o lugar onde a troca acontece. Não é uma estrutura passiva — é parede metabolicamente ativa, com células que produzem surfactante e macrófagos que ficam patrulhando, como você vai ver na sessão 1.2.

#mini-resumo[Do nariz ao alvéolo: cano duro (traqueia) → cano flexível com cartilagem (brônquio) → cano sem cartilagem (bronquíolo terminal) → cano com alvéolo na parede (bronquíolo respiratório) → saco final (alvéolo). Cada nível tem defesa própria e vulnerabilidade própria.]

Tanta ramificação existe por uma razão geométrica. Um único saco do tamanho de uma laranja teria área de superfície ridiculamente pequena para a quantidade de gás que você precisa trocar por minuto. Quando você fragmenta esse volume em ~300 milhões de alvéolos pequenos, a área total chega a ~70 m² — o tamanho de uma quadra de tênis empacotada dentro do tórax. Essa área é o "A" da Lei de Fick que você vai encontrar na PARTE II; guarde o número, ele vai voltar.

Na imagem a seguir, observe o detalhe inferior: um *cluster* de alvéolos é sempre envolvido por um leito capilar denso, quase não há "espaço morto" entre alvéolo e vaso. Essa proximidade anatômica é a justificativa para a barreira fina que você vai ver na sessão 1.2 — é fina porque pode ser, porque o vaso está logo ali.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-02.png",
  largura: 80%,
  legenda: [Hierarquia traqueia → brônquios → bronquíolos → alvéolos, com detalhe da relação entre o ácino terminal (cluster de alvéolos) e o capilar pulmonar. Note que o alvéolo nunca está sozinho: cada um partilha parede com 5–6 vizinhos, e essa interdependência mecânica é o que mantém o conjunto aberto durante a respiração normal.],
)

#confusao-prevista(
  titulo: "Alvéolo não é saco passivo de ar",
  aluno_acha: [aluno pensa no alvéolo como um balão inerte que enche e esvazia, sem função própria além de "guardar ar"],
  mecanismo: [o alvéolo é parede biologicamente ativa: pneumócito II produz surfactante a cada poucos minutos; macrófago alveolar patrulha continuamente fagocitando partículas e bactérias; o epitélio sinaliza para o sistema imune quando detecta agressão. Virar saco passivo é o que acontece NA pneumonia (quando exsudato substitui a parede ativa) — não no normal.],
)

#subtopico("1.2 — Membrana alvéolo-capilar: a parede mais fina do corpo")

A membrana alvéolo-capilar — a barreira que separa o ar dentro do alvéolo do sangue dentro do capilar — mede cerca de 0,3 µm. Para comparar: o papel comum tem ~100 µm. É mais fina que muitas membranas celulares isoladas, e a razão para tanta finura é direta: a velocidade da troca gasosa é inversamente proporcional à espessura. O O₂ precisa sair do ar alveolar, atravessar a parede, entrar no sangue e ligar-se à hemoglobina em menos de 0,75 segundo — o tempo que a hemácia leva para atravessar o capilar pulmonar em repouso. Se a parede fosse grossa, não daria tempo de equilibrar.

A imagem a seguir é o corte histológico clássico dessa região; aproveite para identificar visualmente as quatro estruturas que estão amontoadas numa fatia tão fininha — espaço alveolar (1), pneumócito II ainda cuboide e granular (2), hemácias dentro do capilar (3) e pneumócito I achatado cobrindo quase toda a superfície (4).

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-05.png",
  largura: 70%,
  legenda: [Membrana alvéolo-capilar vista em histologia. (1) Espaço alveolar — onde fica o ar. (2) Pneumócito II, cuboide, ainda com aspecto granular pelo citoplasma cheio de corpos lamelares com surfactante pronto para liberação. (3) Hemácias dentro do capilar pulmonar — a coluna vermelha fica encostada na parede do alvéolo. (4) Pneumócito I, achatado, é o que cobre 95% da superfície alveolar e forma o "vidro fino" da barreira.],
)

A parede tem quatro camadas em sequência, cada uma com função específica. Primeiro vem a camada de surfactante (filme líquido com fosfolípides, ~0,1 µm) — não é exatamente "parede", mas é o que reveste o ar e impede o colapso (você vai entender o porquê quando chegar em La Place na PARTE II). Depois vem o pneumócito I (epitélio achatado, ~0,1 µm), uma célula gigante e fina que cobre 95% da área alveolar com 5% do total de células — é o "vidro" da barreira. Atrás dele há a membrana basal compartilhada com o capilar. E finalmente o endotélio capilar (também achatado).

E é só isso que separa O₂ do plasma. Quando algo engrossa qualquer uma dessas camadas — edema, fibrose, exsudato inflamatório —, a difusão cai. Você vai ver esse fenômeno em ação na PARTE III, quando os alvéolos da Catarina se encherem de exsudato fibrino-purulento e o caminho do O₂ passar de 0,3 µm para várias dezenas de micrômetros.

#mini-resumo[Membrana alvéolo-capilar = surfactante + pneumócito I + membrana basal + endotélio. Espessura ~0,3 µm. Pneumonia engrossa o caminho do O₂; em Fick, isso é T no denominador, e cresce o T cai V_gás.]

Os pneumócitos II merecem parágrafo próprio. São células cuboides menores, com citoplasma cheio de corpos lamelares (estruturas em camadas que armazenam surfactante pronto para liberação). Representam ~10% das células alveolares mas ocupam só ~5% da superfície — não estão ali para cobrir, estão ali para *produzir*. Além do surfactante, têm função de reserva: quando um pneumócito I morre (por toxicidade do oxigênio, por inflamação, por trauma), um pneumócito II vizinho prolifera, achata-se e vira pneumócito I. É a célula-tronco do epitélio alveolar.

Ao lado do alvéolo passa o capilar pulmonar. Diferente da circulação sistêmica, aqui o vaso recebe sangue *desoxigenado* (vindo do ventrículo direito) e devolve sangue *oxigenado* (para o átrio esquerdo). Toda a hemácia do corpo passa por aqui a cada ~1 minuto. A pressão hidrostática no capilar pulmonar é baixa (~12 mmHg, contra ~25 mmHg nos capilares sistêmicos) — isso é proteção, porque pressão alta espremeria líquido para dentro do alvéolo (edema pulmonar).

#subtopico("1.3 — Clearance mucociliar: a defesa que o cigarro desliga")

Aqui vem a parte que mais conecta a anatomia ao caso Catarina. O pulmão respira ar não-estéril o tempo todo. Cada inspiração traz poeira, bactérias, vírus, fungos, fragmentos celulares — e tudo isso é interceptado antes de chegar ao alvéolo por uma máquina de limpeza contínua chamada *clearance mucociliar*, ou "elevador mucociliar". A máquina tem duas partes: o tapete de muco em cima e os cílios que batem por baixo arrastando o tapete.

A figura abaixo mostra o epitélio onde tudo isso acontece — é um pseudo-estratificado com três tipos celulares interconvertidos. A célula caliciforme (1) tem aspecto "de cálice" porque acumula grânulos de mucina no ápice; é ela quem produz o muco. A célula cilíndrica ciliada (2) bate os cílios na superfície apical, arrastando o muco em direção à faringe. A célula basal (3) é tronco — fica encostada na membrana basal e repõe as duas anteriores. A célula granular ou neuroendócrina (4) é sensor químico do que entra com o ar.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-03.png",
  largura: 65%,
  legenda: [Epitélio respiratório pseudo-estratificado. (1) Célula caliciforme — produz o muco. (2) Célula cilíndrica ciliada — bate os cílios na superfície apical. (3) Célula basal — tronco. (4) Célula granular (neuroendócrina) — sensor químico.],
)

A célula caliciforme libera, junto com glândulas submucosas, uma mistura viscosa de glicoproteínas (mucinas), água, eletrólitos e proteínas antimicrobianas (lisozima, lactoferrina, defensinas). O muco organiza-se em duas camadas: uma camada *gel* viscoelástica por cima (que captura as partículas), e uma camada *sol* aquosa por baixo (onde os cílios batem livremente). Sem a camada sol, os cílios travam — é o que acontece na fibrose cística, onde o defeito no canal CFTR deixa o líquido superficial desidratado e os cílios não conseguem mais empurrar o gel.

Os cílios do epitélio respiratório (cílios "móveis", diferentes dos cílios sensoriais imóveis de outras células) batem com frequência de 12 a 15 Hz, num movimento bidirecional coordenado: golpe efetivo para frente (rápido, empurra o muco em direção à faringe) e golpe de recuperação para trás (lento, dobra o cílio sem arrastar o muco de volta). O resultado é uma esteira rolante contínua que move o muco da periferia do pulmão até a faringe, onde ele é engolido sem percebermos. A figura a seguir esquematiza esse mecanismo em duas vistas: à esquerda, microscopia eletrônica mostrando a estrutura interna do cílio (9 pares de microtúbulos periféricos + 1 par central, com dineína gerando o batimento); à direita, o esquema funcional do elevador com a camada gel capturando partículas e a camada sol dando espaço para o cílio bater.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-04.png",
  largura: 80%,
  legenda: [À esquerda, microscopia eletrônica dos cílios — cada cílio é um cilindro de microtúbulos (9+2) com dineína entre eles para gerar o batimento. À direita, esquema do "elevador": camada gel captura partículas; camada sol acomoda os cílios; batimento coordenado empurra muco para faringe. Cigarro paralisa esse mecanismo em horas.],
)

O cigarro é o vilão clássico desse sistema. Cada tragada deposita milhares de compostos químicos no epitélio respiratório, e os cílios respondem em duas escalas de tempo. Em horas, o batimento ciliar diminui — efeito direto da nicotina e de outros componentes voláteis. Em meses a anos de exposição crônica, o epitélio sofre *metaplasia escamosa*: as células cilíndricas ciliadas são substituídas por células escamosas (planas, sem cílios), que oferecem mais resistência mecânica mas perdem a função de transporte. O muco produzido pelas células caliciformes restantes (que aumentam em número — bronquite crônica) fica estagnado, virando meio de cultura para bactérias.

Catarina fumou um maço por dia durante dez anos e parou há cinco. Recuperação ciliar completa após cessação leva *meses a anos*, e a metaplasia escamosa persistente leva ainda mais tempo — em muitos casos, nunca volta totalmente ao normal. A confusão clássica aqui é achar que "5 anos sem fumar" já trouxe o pulmão de volta ao estado pré-cigarro; não trouxe. O elevador mucociliar dela ainda funciona com fração da eficiência original, e essa é uma das razões pelas quais ela é mais vulnerável à pneumonia do que uma colega não-fumante da mesma idade.

#mini-resumo[Defesa pulmonar do alto até o alvéolo: filtro nasal → reflexo da tosse → muco + cílios (elevador mucociliar) → macrófago alveolar + imunidade celular. Cigarro tira o cílio; diabetes tira a função do macrófago. Catarina perdeu as duas.]

A diabetes é o segundo fator de defesa caída no caso. A hiperglicemia, mesmo "controlada com dieta", produz *produtos finais de glicação avançada* (AGEs) ao longo dos anos — proteínas e lipídios glicados que ficam menos funcionais. Em particular, neutrófilos diabéticos têm fagocitose menos eficiente, e a microangiopatia (alterações nos pequenos vasos) reduz a perfusão local — chega menos célula de defesa onde precisa. Um diabético tem 1,5 a 2 vezes mais pneumonia do que um não-diabético da mesma idade, e quando tem, evolui pior.

#sintese-box("PARTE I",
[O pulmão é um cano hierárquico que vira esponja. A esponja é feita de ~300 milhões de alvéolos com parede fina (0,3 µm) onde O₂ atravessa para o sangue e CO₂ sai. Essa parede contém pneumócitos I (cobertura), pneumócitos II (surfactante e reserva), endotélio capilar e membrana basal. Tudo isso vive em risco constante de invasão microbiana, mas é protegido pelo elevador mucociliar — muco em duas camadas + cílios batendo a 12–15 Hz. Cigarro paralisa os cílios; diabetes derruba os macrófagos. Quando essas defesas falham, a infecção atinge o alvéolo, e aí a física da troca gasosa (PARTE II) começa a desmoronar.],
)

A próxima PARTE vai mostrar essa física — quatro leis que descrevem como o gás atravessa a parede alveolar, como o alvéolo se mantém aberto, como ventilação e perfusão se acoplam, e como o sangue tampona o ácido produzido pelo metabolismo. Sem essas quatro leis, a leitura da gasometria de Catarina vira decoreba de tabelas; com elas, vira diagnóstico mecanístico.

#parte-title("PARTE II — As físicas da troca gasosa e do equilíbrio ácido-base")

#subtopico("2.1 — Lei de Fick: a equação que governa a troca gasosa")

A primeira lei da troca gasosa é a Lei de Fick, e o professor do caso já entregou ela pronta para vocês na imagem abaixo. Antes de detalhar variável por variável, observe a fórmula: V_gás é o volume de gás trocado por unidade de tempo (o que queremos maximizar); A, ΔP e K estão multiplicando no numerador; T está dividindo. Tudo o que aumenta numerador aumenta a troca; tudo o que aumenta denominador derruba.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/caso-fick.png",
  largura: 85%,
  legenda: [Lei de Fick (difusão simples) e Lei de Graham, conforme apresentadas no PDF do caso clínico. V_gás representa o volume de gás por unidade de tempo que atravessa a barreira; A é a área da superfície de troca; ΔP = P₁ - P₂ é o gradiente de pressão entre os dois lados; T é a espessura da barreira; K é uma constante que depende do gás (η/√PM pela Lei de Graham).],
)

Vou traduzir cada variável em linguagem clínica.

*A — área de superfície disponível para troca.* No pulmão saudável: ~70 m². Cada alvéolo recrutado contribui um pedacinho dessa área. Quando o alvéolo se enche de líquido (edema) ou de exsudato (pneumonia), ele é *retirado* do recrutamento — sai de A. Em pneumonia extensa como a de Catarina no dia 18, A pode cair pela metade.

*ΔP — diferença de pressão parcial do gás entre os dois lados.* Para o O₂: pressão parcial alveolar (#sigla("PAO\u{2082}", [pressão parcial alveolar de oxigênio])) ~100 mmHg no nível do mar; pressão parcial no sangue venoso (#sigla("PvO\u{2082}", [pressão parcial venosa de oxigênio])) ~40 mmHg. Gradiente ~60 mmHg empurra O₂ para dentro do sangue. Para o CO₂: gradiente ~6 mmHg na direção contrária. Quando o alvéolo se enche de líquido com pouco O₂, a PAO₂ local cai e o gradiente cai junto.

*T — espessura da barreira.* No pulmão normal: 0,3 µm. Em pneumonia, com exsudato dentro do alvéolo + edema intersticial, T pode multiplicar por 10 a 30 vezes. T no denominador significa que crescer T diminui V_gás linearmente.

*K — coeficiente de difusão do gás.* Depende da solubilidade na membrana (η) e do peso molecular (PM), pela Lei de Graham (K = η/√PM). Para gases respiratórios, o CO₂ tem K ~20 vezes maior que o O₂ — apesar do PM um pouco maior (44 vs 32), a solubilidade do CO₂ é muito maior. Consequência clínica: em insuficiência respiratória parcial (pulmão funcionando mal), o primeiro gás a ter problema é o O₂; o CO₂ se acumula só quando a coisa fica grave.

#confusao-prevista(
  titulo: "Molécula maior não difunde mais devagar (no pulmão)",
  aluno_acha: [pela intuição "molécula grande = lenta", aluno espera que CO\u{2082} (PM 44) difunda mais devagar que O\u{2082} (PM 32)],
  mecanismo: [pelo PM isolado, sim, mas a solubilidade do CO\u{2082} no plasma é ~24× maior que a do O\u{2082}. Como K é proporcional a η/√PM, o CO\u{2082} ganha de longe — difunde ~20× mais rápido. Por isso, na falência respiratória, hipoxemia aparece antes da hipercapnia.],
)

#mini-resumo[V_gás = (A × ΔP × K) / T. Pneumonia mexe em três das quatro variáveis: A↓ (alvéolo cheio sai), ΔP↓ (PAO₂ local cai), T↑ (parede engrossa). K é a única que não muda. A difusão despenca.]

#subtopico("2.2 — Lei de La Place e o papel do surfactante")

A segunda lei é a Lei de La Place, e ela existe para responder uma pergunta importante: por que o alvéolo, uma esfera líquido-ar muito pequena, não colabou ainda. Para uma superfície esférica com uma única interface líquido-ar (como o alvéolo, diferente da bolha de sabão que tem duas), a Lei de La Place diz:

$ P = 2T / r $

Onde P é a pressão dentro da esfera, T é a tensão superficial do líquido que reveste a parede, e r é o raio. *Quanto menor o raio, maior a pressão para manter a esfera aberta* — porque a tensão superficial puxa para dentro com mais eficácia em superfícies muito curvas.

Aqui vem o problema. O alvéolo é pequeno (~0,1 mm de raio). Se a tensão superficial fosse a da água pura (~70 dynes/cm), a pressão necessária para manter o alvéolo aberto seria enorme — maior do que o tórax consegue gerar na inspiração. Pior: alvéolos vizinhos têm tamanhos ligeiramente diferentes. Pelo La Place, alvéolos pequenos teriam pressão maior do que os grandes — então esvaziariam para dentro dos grandes, e o pulmão viraria poucos balões grandes em vez de uma esponja uniforme de pequenos.

A natureza resolve isso com o #termo-nota[surfactante][mistura de fosfolípides (principalmente DPPC) e proteínas SP-A/B/C/D que reveste a interface ar-líquido alveolar reduzindo a tensão superficial], sintetizado e secretado pelo #termo-nota[pneumócito II][célula cuboide do epitélio alveolar produtora de surfactante e reserva regenerativa do pneumócito I]. O surfactante é uma mistura de fosfolípides — predominantemente dipalmitoilfosfatidilcolina (DPPC) — com algumas proteínas (SP-A, SP-B, SP-C, SP-D). Ele se distribui na interface líquido-ar e *reduz drasticamente* a tensão superficial, de ~70 para algo entre 5 e 25 dynes/cm.

Mais elegante ainda: o surfactante não reduz T uniformemente — ele se concentra mais nos alvéolos pequenos. O motivo é geométrico: alvéolo menor tem menos área de superfície por molécula de surfactante, então as moléculas ficam mais próximas, mais densas, mais eficazes em derrubar T. Resultado: nos alvéolos pequenos, T cai mais → P (= 2T/r) cai mais → o alvéolo pequeno deixa de ter pressão maior que o vizinho grande. Os tamanhos se equilibram. O pulmão respira como uma esponja uniforme, não como um balão único.

Sem surfactante, alvéolos pequenos colabariam — é o que acontece em recém-nascidos prematuros (doença da membrana hialina) e em adultos com #sigla("SDRA", [síndrome do desconforto respiratório agudo — falência respiratória com edema não-cardiogênico e destruição do surfactante]). E é parte do que acontece com Catarina no dia 18: a inflamação intra-alveolar destrói pneumócitos II e degrada o surfactante existente. Sem surfactante, os alvéolos pequenos colabam; e alvéolo colabado (cheio de líquido) recebe sangue mas não recebe ar — vira shunt (próxima sessão).

#mini-resumo[P = 2T/r diz que alvéolo pequeno precisa de pressão alta para abrir. Surfactante derruba T, especialmente nos alvéolos pequenos, e equilibra o sistema. Inflamação destrói surfactante; alvéolos colabam; o que resta vira shunt.]

#subtopico("2.3 — Relação V/Q: shunt e espaço morto")

A troca gasosa só funciona se *ventilação* (V — ar chegando ao alvéolo) e *perfusão* (Q — sangue passando pelo capilar) estão acopladas. A relação ideal é V/Q ≈ 1: cada litro de ar encontra um litro de sangue. Quando o acoplamento quebra, surgem dois extremos com mecânicas e nomes diferentes — e confundi-los é um dos erros mais clássicos do estudante de fisiologia respiratória.

#termo-nota[Shunt intrapulmonar][sangue que passa pelo capilar pulmonar sem trocar gás, porque o alvéolo correspondente está cheio de líquido ou colabado — V/Q tendendo a zero]: alvéolo perfundido sem ser ventilado. V/Q → 0. O sangue chega no capilar, mas o alvéolo está cheio de líquido (edema), cheio de exsudato (pneumonia) ou colapsado (atelectasia). Resultado: sangue venoso passa pelo capilar e volta para o átrio esquerdo sem ter trocado gás — é como se houvesse uma "curva curta" desviando o sangue do leito de troca.

#termo-nota[Espaço morto alveolar][alvéolo que recebe ar mas não recebe sangue (vaso obstruído ou destruído) — V/Q tendendo ao infinito]: alvéolo ventilado sem ser perfundido. V/Q → ∞. O ar chega no alvéolo, mas o capilar não passa sangue ali — porque o vaso foi obstruído por um trombo (embolia pulmonar) ou destruído (enfisema). Resultado: o ar entra e sai do alvéolo sem encontrar sangue para trocar.

A foto a seguir é um corte macroscópico de broncopneumonia em peça anatômica, e mostra os dois fenômenos coexistindo no mesmo pulmão: à esquerda, uma área enfisematosa marcada como "espaço morto" (ar sem sangue trocando); ao centro, área de consolidação esbranquiçada marcada como "shunt" (sangue passando por alvéolo cheio). É essa heterogeneidade que torna a hipoxemia da pneumonia parcialmente refratária ao oxigênio suplementar.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-08.png",
  largura: 75%,
  legenda: [Corte macroscópico de broncopneumonia com setas indicando regiões de "espaço morto" (área enfisematosa, ar sem sangue trocando) e "shunt" (área de consolidação esbranquiçada, sangue passando por alvéolo cheio). Os dois fenômenos coexistem no mesmo pulmão doente, em locais diferentes.],
)

#atencao-box("Shunt e espaço morto são opostos, não sinônimos",
[O sintoma compartilhado é hipoxemia — em ambos, o sangue arterial fica com pouco O₂. Mas o mecanismo é oposto: shunt é *sangue desperdiçado* (passa por alvéolo que não respira); espaço morto é *ar desperdiçado* (entra em alvéolo que não tem sangue). E mais: shunt verdadeiro é refratário a O₂ suplementar — adianta pouco aumentar a FiO₂ porque o sangue não está chegando no alvéolo onde o O₂ extra estaria. Espaço morto responde, porque o ar realmente chega. Tratamento divergente: shunt → recrutamento alveolar com pressão positiva (CPAP, ventilação mecânica); espaço morto → tratar a obstrução (anticoagulação na embolia).],
)

Pneumonia gera *shunt*. O alvéolo da Catarina no dia 18, cheio de exsudato fibrino-purulento (você vai ver a histologia na PARTE III), está recebendo sangue do capilar pulmonar e devolvendo sem que o O₂ tenha entrado. Por isso, mesmo dando O₂ a 100% pela máscara, a Sat dela só vai melhorar parcialmente até o suporte ventilatório recrutar os alvéolos colapsados.

V/Q também não é uniforme dentro do pulmão saudável. Por causa da gravidade, o ápice (parte alta) é mais ventilado que perfundido (V/Q ~3), e a base (parte baixa) é mais perfundida que ventilada (V/Q ~0,6). A média é ~0,8, não exatamente 1.

#mini-resumo[V/Q normal médio ~0,8. Shunt (V/Q→0) = pneumonia, edema, atelectasia, alvéolo cheio. Espaço morto (V/Q→∞) = embolia, enfisema, vaso obstruído. Ambos causam hipoxemia; só o espaço morto responde bem a O₂ suplementar.]

#subtopico("2.4 — O sistema bicarbonato como tampão aberto")

Aqui o terreno muda de pulmão para sangue, mas a conexão é direta: o pulmão é a metade respiratória do sistema ácido-base mais importante do corpo. Todo metabolismo aeróbico gera CO₂. Esse CO₂ vai do tecido para o sangue (transportado em três formas, mas a principal é em forma de bicarbonato dissolvido), chega ao pulmão e é exalado. A reação química central é:

$ "CO"_2 + "H"_2"O" arrows.lr "H"_2"CO"_3 arrows.lr "HCO"_3^- + "H"^+ $

Essa reação é catalisada pela *anidrase carbônica* dentro das hemácias. O equilíbrio mostra que quando o CO₂ sobe, a reação corre para a direita e gera H⁺ — acidifica o sangue. Quando o CO₂ cai (hiperventilação, por exemplo), a reação corre para a esquerda e consome H⁺ — alcaliniza.

A equação de Henderson-Hasselbalch aplicada a esse sistema diz que o pH do sangue depende da razão entre #sigla("HCO\u{2083}\u{207B}", [bicarbonato — base conjugada do ácido carbônico, principal tampão extracelular]) e CO₂:

$ "pH" = 6,1 + log(["HCO"_3^-] / (0,03 dot "pCO"_2)) $

O fator 6,1 é o pKa do par H₂CO₃/HCO₃⁻. Agora vem o ponto sutil — esse sistema é potente apesar do pKa (6,1) estar longe do pH fisiológico (7,4), e a regra clássica de tampão diz que tampão só funciona bem em ±1 unidade do pKa. Pelo critério clássico, bicarbonato seria um péssimo tampão a pH 7,4. A resposta está na palavra *aberto*. Diferente de um tampão num tubo de ensaio (fechado), o sangue está conectado ao pulmão. Toda vez que H⁺ se acumula e empurra a reação para esquerda gerando mais CO₂, o pulmão *retira* esse CO₂ — sopra para fora. Tira o produto, desloca o equilíbrio. Tira mais ainda. O sistema se comporta como se tivesse capacidade ilimitada, porque um dos produtos sai do sistema continuamente.

#confusao-prevista(
  titulo: "pKa 6,1 não impede bicarbonato de tamponar bem a pH 7,4",
  aluno_acha: [aluno aplica a regra "tampão só funciona em ±1 do pKa" e conclui que bicarbonato seria fraco a pH 7,4 (distância de 1,3 unidades)],
  mecanismo: [a regra vale para sistemas fechados. O bicarbonato é aberto: pulmão sopra CO\u{2082} fora continuamente, eliminando um dos produtos do equilíbrio. Resultado: a capacidade tamponante é praticamente ilimitada enquanto o pulmão funciona. Quando o pulmão falha (caso Catarina), o sistema vira fechado, e aí sim o pKa distante manifesta a fraqueza — acidose explode.],
)

Esse é o motivo pelo qual paciente com pulmão funcionando aguenta bem grandes cargas ácidas (acidose metabólica compensada por hiperventilação). E é o motivo pelo qual paciente com pulmão falhando entra em acidose grave rápido (porque perdeu a "torneira" que abria o sistema).

Os quatro quadros possíveis de distúrbio ácido-base saem da combinação de qual variável muda primeiro e em que direção. Em *acidose respiratória*, o pCO₂ sobe (pulmão não exala bem) e o pH cai — causa típica é insuficiência respiratória. Em *alcalose respiratória*, o pCO₂ cai (hiperventilação) e o pH sobe — causa típica é ansiedade, dor, febre, embolia inicial. Em *acidose metabólica*, o HCO₃⁻ cai (perdido ou consumido por ácido) e o pH cai — causa típica é lactato por hipóxia tecidual, cetose, insuficiência renal. Em *alcalose metabólica*, o HCO₃⁻ sobe e o pH sobe — causa típica é vômitos prolongados (perde H⁺) e uso de diurético.

A compensação obedece a uma regra simples: distúrbio respiratório é compensado pelo rim (lento, dias), e distúrbio metabólico é compensado pelo pulmão (rápido, minutos a horas, mudando a FR). Por isso, paciente com acidose metabólica aguda mostra hiperventilação imediata; paciente com acidose respiratória aguda ainda tem HCO₃⁻ normal nas primeiras horas.

#mini-resumo[Quatro quadros: respiratória/metabólica × acidose/alcalose. Pulmão regula CO₂ rápido (minutos); rim regula HCO₃⁻ lento (dias). Bicarbonato é tampão potente apesar do pKa distante porque é sistema aberto. Quando o pulmão falha, o sistema vira fechado e a acidose dispara.]

#subtopico("2.5 — Tampões intra, extra e intravasculares")

O bicarbonato é o principal tampão *extracelular*, mas não é o único. O corpo distribui a carga ácida em vários compartimentos com vários tampões diferentes, e entender essa distribuição ajuda a prever o que vai acontecer em uma acidose aguda como a do dia 18 da Catarina.

*Intravasculares* (dentro do vaso): bicarbonato é o dominante (~95% da capacidade). A hemoglobina contribui significativamente — cada hemoglobina tem 38 histidinas com nitrogênio imidazólico que tampona H⁺, e o pKa muda com o estado de oxigenação (efeito Haldane: deoxiHb tem pKa maior, é tampão mais eficiente — explica por que o sangue venoso aceita CO₂ tão bem).

*Extracelulares fora do vaso* (interstício): bicarbonato continua sendo o principal, junto com pequena contribuição do fosfato.

*Intracelulares*: proteínas (citoplasmáticas) e fosfato orgânico (com pKa ~6,8 — perfeito para o pH intracelular que é ~7,2). O tampão intracelular recebe ~50% de uma carga ácida aguda. O mecanismo é importante: o H⁺ entra na célula via antiporters Na⁺/H⁺ em troca de K⁺ — por isso acidose grave causa hipercalemia, com risco cardíaco de arritmia. A membrana celular não é barreira impermeável a H⁺; é compartimento comunicante. Quando o extracelular acidifica, H⁺ entra; quando alcaliniza, sai. O equilíbrio é dinâmico.

Em Catarina no dia 18, todos os três compartimentos estão sobrecarregados: o intravascular consumindo bicarbonato (HCO₃⁻ caiu de 21 para 15), o intracelular recebendo H⁺ em troca de K⁺ (risco de hipercalemia), e o pulmão — a "torneira" do sistema bicarbonato aberto — falhando em soprar CO₂ para fora.

#sintese-box("PARTE II",
[Quatro leis governam o que vai acontecer na PARTE III. Fick (V_gás = A·ΔP·K/T) diz que pneumonia despenca a difusão. La Place (P = 2T/r) diz que sem surfactante alvéolos pequenos colabam. V/Q distingue shunt (pneumonia) de espaço morto (embolia) e prevê o que vai responder a O₂. Henderson-Hasselbalch + Bicarbonato como tampão aberto diz que o pH depende da razão HCO₃⁻/CO₂, mantida pelo pulmão (rápido) e pelo rim (lento). Quando uma dessas leis quebra, o sistema fica fragilizado; quando duas quebram juntas, há falência.

Você agora tem as ferramentas para entender por que a gasometria 1 de Catarina é alcalose respiratória, por que a gasometria 2 engana o médico de plantão, e por que a gasometria 3 é acidose mista grave. Vamos para a PARTE III lê-las uma a uma.],
)

#parte-title("PARTE III — A trajetória da Catarina")

#subtopico("3.1 — Dia 16-02: a UPA, a gasometria 1, a alcalose que ninguém leu")

Catarina chega à UPA de Paulistania no dia 16-02 com sintomas de uma semana — mal-estar, febre que ela não chegou a medir, tosse com expectoração que começou branca e há quatro dias está amarela. A tosse piora à noite. Ela está tomando dipirona, mas o efeito dura ~6 horas e os sintomas voltam.

No exame físico, o que importa é o aparelho respiratório. O médico encontra #sigla("FR", [frequência respiratória — número de inspirações por minuto]) de 22 ipm (normal 12–18), #sigla("FC", [frequência cardíaca — batimentos por minuto]) de 90 bpm, #sigla("PA", [pressão arterial]) 120×80, T 37,9°C. Aspecto geral bom, sem cianose. À ausculta pulmonar: #sigla("MV", [murmúrio vesicular — som respiratório normal auscultado no pulmão]) presente bilateralmente, mas no ápice do pulmão direito há macicez à percussão, MV diminuído, estertores crepitantes, broncofonia aumentada e #termo-nota[pectorilóquia][transmissão exagerada da voz pelo tórax consolidado; o examinador ouve as sílabas nítidas quando o paciente fala — sinal de consolidação alveolar]. Alguns roncos e sibilos no #sigla("HTD", [hemitórax direito]).

Esse conjunto semiológico — macicez + MV reduzido + crepitantes + broncofonia + pectorilóquia em um único quadrante pulmonar — é a *síndrome de consolidação*. Significa que aquele pedaço do pulmão tem alvéolos cheios de líquido em vez de ar. O som da percussão fica abafado porque líquido conduz percussão diferente de ar; o MV some porque o ar não consegue mais vibrar contra a parede; os crepitantes aparecem porque alvéolos colapsados pelo líquido se abrem ruidosamente na inspiração; e a voz transmite mais alto porque líquido é melhor condutor de som que ar.

O médico pede exames de sangue e #sigla("RX", [radiografia]) de tórax. Após 5 horas, libera Catarina com amoxicilina via oral 8/8h e orientação de retorno em 1 semana na #sigla("UBS", [Unidade Básica de Saúde]). Catarina questiona o médico sobre seu estado, dizendo que não está se sentindo bem para ir para casa; o médico responde que ela "não deveria se preocupar". A filha pede atestado e ouve que "apenas o médico do trabalho está autorizado".

Antes de avaliar essa conduta, vamos ler a gasometria 1 com cuidado. Os números: pH 7,50, pCO₂ 26, HCO₃⁻ 21, #sigla("pO\u{2082}", [pressão parcial de oxigênio no sangue arterial]) 93, Sat O₂ 95%.

Primeiro reflexo: pH 7,50 é alcalose (normal 7,35–7,45). Segundo reflexo: pCO₂ 26 está baixo (normal 35–45), então o componente respiratório está alcalinizando o sangue. Terceiro reflexo: HCO₃⁻ 21 está no limite inferior do normal (21–24), praticamente normal — não há ainda compensação metabólica significativa. Conclusão: *alcalose respiratória aguda*.

#mini-resumo[Gasometria 1: pH↑, pCO₂↓, HCO₃⁻ normal = alcalose respiratória aguda. Causa: hiperventilação por dor pleurítica, febre e ativação de receptores J pulmonares (irritação alveolar). O quadro respiratório já está alterado mesmo com Sat preservada.]

Catarina hiperventilou porque a consolidação no LSD ativa *receptores J pulmonares* (receptores justa-capilares no interstício alveolar, sensíveis a edema e inflamação), que disparam estímulo ao centro respiratório pelo nervo vago. Soma-se a isso a febre (cada grau acima de 37 acelera o metabolismo basal em ~10%, gerando mais CO₂ que precisa ser eliminado) e a dor pleurítica leve (talvez ainda não percebida pela paciente, mas presente como estímulo nociceptivo). O centro respiratório responde aumentando FR, e a hiperventilação derruba pCO₂.

Mas há uma armadilha: Sat O₂ 95% e pO₂ 93 *parecem* tranquilizadores. Estão preservados porque ela está usando o pulmão saudável restante (a maior parte ainda funciona) e a hiperventilação compensatória ajuda a aumentar a PAO₂ alveolar nas regiões sãs. É como pilotar um carro só com 3 rodas no asfalto: ainda anda, ainda parece normal nos primeiros minutos, mas o sistema está sob estresse máximo e qualquer agravamento derruba.

A conduta do médico falhou em três pontos. Primeiro, *não usou score validado* (CURB-65, PSI) — apenas classificou como "pneumonia risco 1" no julgamento. Segundo, *não respeitou o que a paciente disse*: ela falou que não estava bem para ir embora; isso é dado clínico, não opinião. Terceiro, *não orientou sinais de alarme* nem agendou revisão em 24h. Cada uma dessas falhas é tratada na PARTE de ética (subseção 3.5), mas é importante notar agora que a falha não foi a droga (amoxicilina é primeira escolha para pneumococo sensível) — foi a *subestimação da gravidade*.

#subtopico("3.2 — Por que o quadro piorou em 48 horas: defesa derrubada e germe identificado")

A pergunta do GD vai cair: como uma pneumonia "risco 1" evolui para falência respiratória em 48h? A resposta tem três camadas: a defesa pulmonar de Catarina já estava comprometida; o germe é virulento; a antibioticoterapia ambulatorial pode não ter atingido concentração tecidual suficiente nas primeiras 24h.

*Camada 1 — defesa comprometida.* Como você viu na PARTE I, o pulmão depende de clearance mucociliar + macrófago alveolar + imunidade adaptativa. Catarina tem dois golpes nessas defesas. O tabagismo de 10 anos-maço, mesmo cessado há 5 anos, deixa metaplasia escamosa e clearance ciliar permanentemente reduzido — o muco que captura bactérias inaladas não é mais empurrado para fora com a mesma eficiência. A diabetes (mesmo "controlada com dieta") gera AGEs que comprometem a fagocitose dos neutrófilos e a microangiopatia reduz a chegada de células imunes ao parênquima. Resultado: bactéria que num pulmão saudável seria contida na via aérea superior chega ao alvéolo e se replica sem oposição inicial.

*Camada 2 — germe identificado.* Na UTI, o lavado broncoalveolar (BAL) — endoscopia das vias aéreas inferiores com coleta de líquido — mostra a etiologia. Observe na imagem abaixo: a lâmina corada pelo Gram revela cocos gram-positivos em cadeia (estruturas roxas alongadas — letra A) e polimorfonucleares (núcleos lobulados — letra B). Cocos gram-positivos em cadeia são *Streptococcus pneumoniae* (pneumococo) — o germe mais comum de pneumonia adquirida na comunidade, responsável por 30–50% dos casos com etiologia confirmada.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/caso-lavado.png",
  largura: 75%,
  legenda: [Lavado broncoalveolar corado pelo Gram. A (cocos gram-positivos em cadeia — *Streptococcus pneumoniae*); B (polimorfonucleares — neutrófilos chegando ao alvéolo em resposta à infecção). A presença de PMN abundantes confirma resposta inflamatória vigorosa; a cadeia de cocos gram+ identifica o pneumococo.],
)

O pneumococo tem fatores de virulência específicos: cápsula polissacarídica anti-fagocítica (o organismo precisa fazer anticorpo opsonizante antes de eliminá-lo eficientemente), pneumolisina (toxina que perfura membrana alveolar) e autolisinas (libertam mais pneumolisina ao morrer). Em paciente com defesa derrubada, esses fatores se desdobram em invasão rápida do parênquima.

*Camada 3 — antibioticoterapia subdimensionada.* O médico do dia 16 prescreveu amoxicilina via oral. A dose habitual para pneumonia comunitária ambulatorial seria 875 mg–1 g de 8/8h. No caso, o registro indica apenas "1 dia" de uso antes do retorno — provavelmente ela tomou apenas 1–2 doses, insuficientes para atingir concentração tecidual bactericida estável em pulmão consolidado. A antibioticoterapia certa, na dose certa, pode ter sido tardia.

O RX comparativo a seguir mostra a progressão. À esquerda, um pulmão normal para referência. No meio, RX de Catarina no dia 16, com infiltrado focal no LSD (a pequena setinha vermelha) — coerente com a macicez ouvida ao exame. À direita, RX do dia 18, com consolidação extensa bilateral, padrão de broncopneumonia disseminada que acompanha a árvore brônquica e ocupa múltiplos lobos.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/caso-rx.png",
  largura: 85%,
  legenda: [Comparação radiológica. Esquerda: padrão normal para referência (silhuetas cardíaca e diafragmática nítidas, parênquima escuro=aerado). Centro (16-02): infiltrado focal em LSD da Catarina (seta vermelha), consistente com consolidação localizada. Direita (18-02): consolidação extensa bilateral em 48h — o exsudato preencheu múltiplos lobos. Note como o ar (preto) foi substituído por densidade aumentada (branco).],
)

A histologia do parênquima acometido (figura a seguir) mostra o que esse "branco" do RX significa em nível microscópico. Os espaços alveolares, que no pulmão saudável estariam vazios de líquido e cheios de ar, estão completamente preenchidos por exsudato inflamatório — leucócitos polimorfonucleares (núcleos roxos), fibrina (filamentos rosa) e edema. O alvéolo deixou de ser câmara de troca e virou saco fechado de pus. É exatamente esse achado morfológico que justifica todas as quebras de Fick, La Place e V/Q que você vai ler nas gasometrias seguintes.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/caso-histologia.png",
  largura: 75%,
  legenda: [Histologia do pulmão da Catarina (figura 3B do caso). #termo-nota[Exsudato fibrino-purulento][líquido rico em fibrina, neutrófilos e bactérias que preenche o alvéolo na pneumonia bacteriana, substituindo o ar normal] preenche os espaços alveolares — leucócitos polimorfonucleares (núcleos basofílicos, roxos) misturados com fibrina (eosinofílica, rosa) e edema. Compare com um pulmão saudável: ali os septos alveolares seriam finos linhas rosas separando espaços vazios escuros (ar).],
)

#subtopico("3.3 — Dia 18-02 UPA: a gasometria 2 que enganou o plantonista")

Catarina retorna à UPA no dia 18-02 trazida pela filha. Agora tem dispneia a médios esforços (andar alguns quarteirões no plano), mantém tosse e expectoração, surge dor torácica ao tossir, não dorme há 2 dias. *Ortopneia* (recusa-se a deitar para ser examinada — não consegue respirar deitada).

Exame físico: FR 28 ipm, T 39,5°C, FC 110 bpm, PA 100×70. Roncos audíveis durante a respiração. Paciente confusa, sonolenta, cianótica. Batimento de asa de nariz (uso de musculatura acessória). Tiragem intercostal e supraescapular (retração da pele entre as costelas e acima da escápula na inspiração — sinal de esforço respiratório intenso). MV diminuído bilateralmente. Macicez em todo o HTD e na metade inferior do #sigla("HTE", [hemitórax esquerdo]) — a consolidação dobrou de tamanho em 48h.

Gasometria 2 (UPA, 18-02): pH 7,35, pCO₂ 40, HCO₃⁻ 20, pO₂ 85, Sat 88%.

#atencao-box("FR caindo em paciente exausta não é melhora — é fadiga muscular",
[Esta é a confusão clínica mais letal do caso. Mais adiante, na gasometria 3 (UTI), a FR de Catarina cai de 28 para 17 ipm. O plantonista desavisado pode interpretar como melhora ("respiração mais calma"). É exatamente o contrário: em paciente com pCO₂ 62 e cianose, a respiração *deveria* estar a 35–40 ipm. FR caindo significa que a musculatura respiratória está esgotada — o diafragma e os intercostais estão deixando de responder ao estímulo do centro respiratório porque não conseguem mais. O próximo passo é apneia → parada respiratória → óbito. Em paciente grave, FR caindo é indicação de intubação imediata, não de alta hospitalar.],
)

Aqui a leitura precisa ser fina. A 1ª passada superficial diz "pH 7,35 está no limite inferior do normal, paciente estável". O 2º olhar é o que diferencia o estudante do médico: comparar gasometria 2 com a gasometria 1.

Entre 16 e 18, a pCO₂ subiu de 26 para 40 (+14). O HCO₃⁻ caiu de 21 para 20 (–1). O pO₂ caiu de 93 para 85 (–8). A Sat caiu de 95% para 88% (–7 pp). Esses números pintam um quadro diferente do "estável": Catarina *perdeu sua compensação respiratória*. A hiperventilação da gasometria 1, que mantinha a pCO₂ baixa, não está mais funcionando — o pulmão consolidado não está mais conseguindo eliminar CO₂ como antes. E o HCO₃⁻ começou a cair (sinal de que carga ácida metabólica — provavelmente lactato emergente por hipóxia tecidual em outros leitos — já está consumindo tampão).

Esse é o *pseudo-equilíbrio*: pH no limite inferior do normal porque o sistema está titulando a última reserva. Não há mais hiperventilação para "comprar" pH; o pulmão já está no esforço máximo (FR 28 + tiragem + batimento de asa de nariz é trabalho respiratório de exaustão). E o HCO₃⁻ já está caindo. Sem nenhuma reserva adicional, qualquer agravamento desloca o sistema para acidose franca.

Outro número importante: a queda de Sat de 95% para 88% *parece* leve (7 pontos percentuais), mas pela curva de dissociação da hemoglobina, isso corresponde a uma queda de pO₂ de ~95 para ~55 mmHg — uma queda de 40 mmHg em zona íngreme da curva. Para cada queda subsequente de Sat, o pO₂ cai cada vez mais. Catarina está perigosamente próxima do ponto onde Sat despenca.

#mini-resumo[Gasometria 2 não é estável: é pseudo-equilíbrio. pCO₂ subiu de 26 para 40 (perdeu compensação respiratória), HCO₃⁻ caiu de 21 para 20 (já consumindo tampão), pO₂ 85 corresponde a Sat 88% — em zona íngreme da curva da Hb. Sem reserva, qualquer piora despenca o sistema.]

A ortopneia, a confusão mental, a cianose, o batimento de asa de nariz e a tiragem confirmam clinicamente o que a gasometria sugere: insuficiência respiratória iminente. O plantonista da UPA, então, decide remover Catarina para um hospital com UTI. Decisão correta — porque a 1ª UPA não tinha capacidade de oferecer suporte ventilatório.

#subtopico("3.4 — Dia 18-02 UTI: a gasometria 3 e a leitura do colapso")

Já no hospital com UTI, nova gasometria. Os números: pH 7,14, pCO₂ 62, HCO₃⁻ 15, pO₂ 55, Sat 82%, FR 17 ipm.

Cada número diz uma coisa, e juntos contam a história do colapso.

O *pH 7,14* é acidose grave (pH normal 7,35–7,45; pH \< 7,20 já compromete função enzimática, sensibilidade dos receptores de catecolamina e mobiliza K⁺ para fora da célula gerando hipercalemia). É emergência metabólica.

A *pCO₂ 62* (normal 35–45) confirma componente respiratório da acidose — o pulmão não consegue eliminar CO₂. Comparando com gasometria 2 (pCO₂ 40), a retenção saltou +22 em poucas horas. Mecanismo: shunt intrapulmonar pelos alvéolos cheios de exsudato (V/Q→0 nas áreas consolidadas — Fick com A↓, T↑, ΔP↓) + fadiga muscular reduzindo o volume minuto (a FR caindo confirma isso).

O *HCO₃⁻ 15* (normal 21–24) confirma componente metabólico da acidose — não é só CO₂ retido; o tampão também está sendo consumido. Mecanismo: hipóxia tecidual generalizada (Sat 82% chega menos O₂ aos tecidos) → glicólise anaeróbica → produção de lactato → consome HCO₃⁻ para tamponar o ácido lático.

Portanto, *acidose mista* (respiratória + metabólica), grave. Cada componente exige tratamento diferente: o respiratório precisa de suporte ventilatório (recrutamento alveolar com pressão positiva); o metabólico precisa de restauração da perfusão e oxigenação tecidual (que vem indiretamente do suporte ventilatório bem feito).

A *pO₂ 55* (normal 80–100) confirma hipoxemia grave. Em ar ambiente — porque ainda não havia O₂ suplementar nessa coleta da UTI inicial.

A *Sat 82%*: cianose franca (que aparece quando a Hb desoxigenada chega a ~5 g/dL — geralmente Sat \< 80% em quem tem Hb normal). Catarina chegou cianótica.

A *FR 17* — esse é o número mais perigoso. Em paciente com pCO₂ 62 e cianose, a resposta esperada do centro respiratório seria taquipneia (FR 30–40). FR 17 significa que a musculatura respiratória *não está mais conseguindo* atender ao estímulo. Fadiga muscular precedendo apneia. Indicação de intubação orotraqueal e suporte ventilatório mecânico imediatos — que foi exatamente o que a UTI fez.

#mini-resumo[Gasometria 3: acidose mista grave. Respiratória (pCO₂ 62 por shunt + fadiga) + metabólica (HCO₃⁻ 15 por lactato da hipóxia tecidual). Hipoxemia grave (pO₂ 55, Sat 82%). FR 17 em paciente com pCO₂ alto = fadiga muscular = apneia iminente.]

Vou amarrar essa gasometria às leis físicas da PARTE II ponto a ponto, porque é exatamente isso que o GD vai cobrar.

*Fick.* O exsudato fibrino-purulento que você viu na histologia mexe nas variáveis de Fick em três frentes simultâneas. (A) Reduz a área de troca: alvéolos cheios saem do recrutamento — talvez 30–50% da área de troca foi perdida. (B) Aumenta a espessura T: o O₂ agora precisa atravessar não só a parede de 0,3 µm mas também a camada de líquido proteináceo dentro do alvéolo (várias dezenas de micrômetros). (C) Reduz o gradiente ΔP: a PAO₂ dentro do alvéolo cheio é baixa porque não chega ar fresco. As três variáveis no numerador caem, T no denominador sobe — V_gás para O₂ despenca.

*La Place.* A inflamação destrói pneumócitos II (que produzem surfactante) e degrada o surfactante existente. Sem surfactante adequado, alvéolos pequenos no tecido adjacente colabariam (P = 2T/r dispara quando T sobe e r é pequeno). Alvéolo colabado vira shunt — entra na conta da hipoxemia refratária.

*V/Q.* Áreas consolidadas têm V/Q→0 (shunt). Áreas adjacentes podem ter V/Q→∞ (espaço morto) se vasos foram comprimidos ou trombosados localmente. O resultado é hipoxemia heterogênea: parte do sangue passa por alvéolos saudáveis e oxigena normalmente, parte passa por alvéolos cheios e volta sem trocar. A mistura final é o sangue arterial subóxico.

*Henderson-Hasselbalch.* Com pCO₂ 62 e HCO₃⁻ 15, o cálculo dá pH 7,14 (próximo dos dados). O sistema bicarbonato, antes "aberto" (com pulmão funcionando), agora está praticamente fechado — o pulmão não consegue mais soprar CO₂ para deslocar o equilíbrio. A capacidade tamponante caiu drasticamente.

#mini-resumo[Quatro leis em ação simultânea: Fick despencando, La Place colabando alvéolos, V/Q heterogênea com shunt dominante, Henderson-Hasselbalch num sistema bicarbonato semi-fechado. Cada lei contribui para o desfecho. Tratar uma só não basta — suporte ventilatório precisa abrir alvéolo (recruta área para Fick), restaurar surfactante (estabiliza La Place), oxigenar tecido (reverter lactato) e melhorar eliminação de CO₂ (devolve o sistema aberto).]

Há ainda o cálculo de [H⁺] a partir do pH, que aparece como pergunta 3 do caso. Por definição, pH = –log[H⁺]. No dia 16 com pH 7,50, [H⁺] = 10⁻⁷·⁵⁰ ≈ 31,6 nmol/L. No dia 18 UTI com pH 7,14, [H⁺] = 10⁻⁷·¹⁴ ≈ 72,4 nmol/L. Variação: ~131% de aumento na concentração de H⁺ em 48h. A escala logarítmica do pH disfarça mudanças grandes na concentração real de íon hidrogênio. Uma queda de pH de 0,36 unidades (7,50 → 7,14) corresponde a *mais que dobrar* a [H⁺]. Isso explica por que pH \< 7,20 é considerado emergência: cada décimo de pH a menos significa proporcionalmente muito mais ácido livre na solução.

O *déficit de ATP* (pergunta 8) é a consequência intracelular da hipóxia. Sem O₂ suficiente, a cadeia respiratória mitocondrial não produz ATP — a célula vira para a glicólise anaeróbica, que rende só 2 ATP por glicose (contra 32–36 da via aeróbica). Resultado: déficit energético maciço, especialmente nos órgãos de alto consumo (cérebro, coração, rim). A bomba Na⁺/K⁺-ATPase, que mantém o gradiente iônico da célula, falha por falta de ATP — o Na⁺ entra na célula, a água entra atrás (osmose), a célula incha (edema citotóxico). No cérebro isso vira a confusão mental e sonolência que a UTI documentou; em escala maior, vira encefalopatia hipóxica, e se prolongada, morte neuronal.

Quando o pH cai abaixo de 7,2, o efeito tampão das próprias proteínas começa a falhar — porque os resíduos com pKa próximo de 7 (histidinas, principalmente) ficam saturados. As proteínas mudam de conformação levemente, alterando função enzimática e de receptores. A sensibilidade dos receptores β-adrenérgicos cai (paciente fica refratário à noradrenalina endógena — choque refratário). É o motivo pelo qual a correção da acidose, junto com a oxigenação, é prioridade absoluta na UTI.

A conduta na UTI foi: suporte ventilatório (intubação + ventilação mecânica com PEEP para recrutar alvéolo colapsado) e manutenção do antibiótico (amoxicilina IV agora, em dose plena). A paciente apresentou melhora em 10 dias, recebendo alta. A filha posteriormente registrou queixa na ouvidoria sobre o atendimento do dia 16.

#subtopico("3.5 — Estratificação de risco e a dimensão MCP/ética")

Pelos critérios de estratificação de complexidade assistencial à saúde no SUS brasileiro — atenção 1ária (UBS), 2ária (UPA/hospital secundário), 3ária (hospital terciário com UTI), 4ária (alta complexidade) —, Catarina no dia 16 *já estava em quadro 2ário*. A presença de sinais semiológicos de consolidação (macicez + crepitantes + broncofonia), febre, tosse produtiva amarela e tabagismo prévio configura pneumonia comunitária com necessidade de avaliação hospitalar próxima e antibioticoterapia direcionada — não atenção 1ária com revisão em 1 semana. No dia 18, com falência respiratória franca, evoluiu para necessidade 3ária (UTI).

A #sigla("MCP", [Medicina Centrada no Paciente — abordagem clínica que integra perspectiva biomédica e perspectiva do paciente em decisões compartilhadas]) é o referencial ético-clínico aplicado aqui. Tem quatro eixos: explorar saúde, doença e experiência da doença (perspectiva do paciente); entender o paciente inteiro (não só o órgão); encontrar terreno comum nas decisões (compartilhar); incorporar prevenção e promoção. A conduta do médico no dia 16 violou os quatro: não explorou a queixa subjetiva de "não estou bem para ir para casa", não considerou o contexto social (varredora de rua, baixa renda, distância da UPA), não compartilhou a decisão de alta (apenas "ela não deveria se preocupar"), não orientou sinais de alarme.

A questão do atestado: legalmente, *qualquer médico pode atestar incapacidade temporária para o trabalho*. O médico do trabalho tem competência adicional para avaliar retorno e nexo causal ocupacional, mas não tem monopólio do atestado de afastamento. A recusa do plantonista é tecnicamente incorreta.

A ida da filha à ouvidoria é mecanismo legítimo do Sistema Único de Saúde (Lei nº 8.142/1990 e portarias subsequentes) para garantia de direito do usuário. Conduta médica que fere autonomia ou comunicação centrada no paciente pode ser objeto de registro formal e investigação ética (Código de Ética Médica, capítulo V — relação com pacientes e familiares).

#atencao-box("MCP não é cortesia — é semiologia",
[Quando Catarina disse "não estou bem para ir para casa", isso era *dado clínico*, não opinião emocional. A percepção do paciente sobre o próprio estado é instrumento diagnóstico validado (especialmente em quadros que evoluem rapidamente como pneumonia). Descartar a fala da paciente como "preocupação infundada" foi falha clínica antes de ser falha ética. O fato de o desfecho ter exigido UTI 48h depois confirma retroativamente que a paciente sabia que algo estava muito errado — e o médico não escutou.],
)

#conclusao-box[
*Princípio unificador.* Quando a defesa pulmonar cai, a invasão muda a geometria do alvéolo; quando a geometria muda, a física da troca quebra; quando a física quebra, o pH desmorona; quando o pH desmorona, a célula para. O caso de Catarina é o desfile, em ordem cronológica, de tudo que você viu nas PARTES I e II.

*Mecanismo nuclear.* O exsudato fibrino-purulento que preenche o alvéolo é o ponto de virada. Ele simultaneamente: reduz A (área de troca) em Fick, aumenta T (espessura) em Fick, reduz ΔP local em Fick, destrói surfactante e quebra La Place, gera shunt (V/Q→0) e fecha o sistema bicarbonato (porque o pulmão não consegue mais soprar CO₂). Quatro leis físicas falhando simultaneamente — falência respiratória aguda hipoxêmica + hipercápnica.

*Clínica retomada.* A queda de FR de 28 para 17 ipm entre o dia 18 UPA e o dia 18 UTI não foi melhora; foi fadiga muscular precedendo apneia. Em paciente com pCO₂ 62 e cianose, a respiração deveria estar a 35–40 ipm. FR caindo em quem está esgotado é sinal de intubação imediata.

*Projeção.* O módulo seguinte de MSP4211 vai abordar sistema cardiovascular, e ali você vai ler hipoxemia pelo lado da *entrega tecidual* de O₂ — débito cardíaco, hemoglobina, microcirculação. Aqui ficou a metade da captação alveolar; lá vem a metade do transporte e da entrega. As duas metades juntas dão o quadro completo do fornecimento de O₂ que sustenta toda a função celular.
]

#mindmap-fechamento(
  tema: "INSUFICIÊNCIA RESPIRATÓRIA",
  mensagem: "o alvéolo deixa de ser câmara de troca e vira saco fechado de pus — Fick, La Place, V/Q e bicarbonato falham ao mesmo tempo, e a célula para",
  com-setas: true,
  estacoes: (
    (rotulo: "Dia 16-02 · UPA", titulo: "Alcalose respiratória",
     fala: [dor pleurítica e febre aceleram FR para 22; pH 7,50 com pCO\u{2082} 26 — sinal de que algo já invadiu o LSD], cor: "a"),
    (rotulo: "Dia 18-02 · UPA", titulo: "Pseudo-equilíbrio enganoso",
     fala: [pH 7,35 parece normal mas é reserva esgotada; pCO\u{2082} subiu para 40, HCO\u{2083}\u{207B} caiu, Sat 88% em zona íngreme da Hb], cor: "neutra", destaque: true),
    (rotulo: "Dia 18-02 · UTI", titulo: "Acidose mista grave",
     fala: [pH 7,14, pCO\u{2082} 62, HCO\u{2083}\u{207B} 15; shunt intrapulmonar + lactato + FR caindo por fadiga muscular], cor: "b"),
  ),
  rodape-titulo: "Quem é o vilão · Sinal de alarme · O que MCP nos ensina",
  cartoes: (
    (titulo: "O germe", frase: [*Streptococcus pneumoniae* (cocos gram+ em cadeia) — etiologia mais comum em pneumonia comunitária; amoxicilina em dose plena é primeira escolha]),
    (titulo: "FR caindo = piora", frase: [em paciente exausta com pCO\u{2082} alto, FR caindo é fadiga muscular precedendo apneia — não melhora; é indicação de intubação imediata]),
    (titulo: "Escutar é semiologia", frase: [quando Catarina disse "não estou bem para ir para casa" no dia 16, era dado clínico; ignorar a percepção do paciente foi falha antes de ser ética]),
  ),
)
