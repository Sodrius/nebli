#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Catarina A.P. tem 46 anos, é varredora de rua em Paulistania (PI), fumou um maço por dia durante dez anos e parou quando o neto nasceu. Diabética. No dia 16 de fevereiro de 2026, procura a #sigla("UPA", [Unidade de Pronto Atendimento]) com tosse há uma semana, febre que ela não mediu e expectoração que começou branca e virou amarela há quatro dias. O médico do plantão a libera com amoxicilina e a frase de que "ela não deveria se preocupar". Quarenta e oito horas depois ela volta cianótica, sentada porque não consegue respirar deitada, com uma gasometria que mostra #sigla("pH", [potencial hidrogeniônico — medida da acidez/alcalinidade de uma solução]) 7,14 e #sigla("pCO\u{2082}", [pressão parcial de gás carbônico no sangue arterial]) 62. Vai para #sigla("UTI", [Unidade de Terapia Intensiva]) com suporte ventilatório e melhora em dez dias.

O que aconteceu nessas 48 horas é o assunto desta apostila. Vamos seguir uma rota fixa: primeiro entender o pulmão saudável (PARTE I), depois as quatro leis físico-químicas que governam a troca gasosa e o equilíbrio ácido-base (PARTE II), e só então entrar na trajetória da Catarina dia a dia, gasometria a gasometria, lendo cada achado pela lente das duas partes anteriores (PARTE III). No fim, você deve conseguir explicar não só *o que* aconteceu, mas *por que* uma paciente com pneumonia "risco 1" pode chegar à beira do óbito em 48h, e o que cada peça do quebra-cabeça contribuiu para isso.

Uma observação editorial: como você está no primeiro ano e provavelmente vai apresentar esse caso em #sigla("GD", [Grupo de Discussão — formato de aula tutorial com casos clínicos]), a apostila é generosa em tamanho porque o material é denso e exige construção de base antes da clínica. Não pule a PARTE II achando que o caso clínico é o que importa — sem ela, a PARTE III vira anedota sem mecanismo.
]

#parte-title("PARTE I — Como o pulmão funciona quando está saudável", primeira: true)

#subtopico("1.1 — Anatomia funcional: cano que vira esponja")

A pergunta certa para começar não é "qual a anatomia do pulmão" — é "como o ar chega no lugar onde encontra o sangue". Porque é nesse encontro, e só nele, que a função do pulmão acontece. Todo o resto da arquitetura existe para garantir esse encontro.

O ar entra pela traqueia, um tubo único de cartilagem em forma de anéis abertos posteriormente. A traqueia se bifurca em dois brônquios principais — direito e esquerdo —, que vão se ramificando como uma árvore invertida, perdendo calibre e, mais importante, perdendo cartilagem. Quando você chega no nível do *bronquíolo terminal*, a cartilagem já não existe mais. Sem cartilagem, a parede do tubo depende inteiramente do tecido conjuntivo elástico ao redor para não colapsar. Por isso o bronquíolo é tão vulnerável a broncoespasmo — basta o músculo liso da parede contrair (asma) para o tubo fechar.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-01.png",
  largura: 75%,
  legenda: [Anatomia macro pulmonar do slide da Prof.ª Marisa Doholnikoff. As vias aéreas em amarelo formam a árvore brônquica; em vermelho/azul, a vasculatura arterial/venosa pulmonar. O detalhe do pulmão isolado à esquerda mostra a textura esponjosa que vem da multiplicação alveolar — não é tecido sólido, é uma malha aerada.]
)

Depois do bronquíolo terminal vêm os *bronquíolos respiratórios*, e a partir daí começa a aparecer alvéolo na parede do próprio tubo. O alvéolo é o saco final, o destino do ar, o lugar onde a troca acontece. Não é uma estrutura passiva — é parede metabolicamente ativa, com células que produzem surfactante e macrófagos que ficam patrulhando, como você vai ver na sessão 1.2.

#mini-resumo[Do nariz ao alvéolo: cano duro (traqueia) → cano flexível com cartilagem (brônquio) → cano sem cartilagem (bronquíolo terminal) → cano com alvéolo na parede (bronquíolo respiratório) → saco final (alvéolo). Cada nível tem defesa própria e vulnerabilidade própria.]

A pergunta natural aqui é: por que tantas divisões? Resposta em duas palavras: *área de superfície*. Um único saco do tamanho de uma laranja teria área de superfície ridiculamente pequena para a quantidade de gás que você precisa trocar por minuto. Quando você fragmenta esse volume em ~300 milhões de alvéolos pequenos, a área total chega a ~70 m² (uma quadra de tênis). Essa área é o "A" da Lei de Fick que você vai encontrar na PARTE II — guarde o número, ele vai voltar.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-02.png",
  largura: 80%,
  legenda: [Hierarquia traqueia → brônquios → bronquíolos → alvéolos, com detalhe da relação entre o ácino terminal (cluster de alvéolos) e o capilar pulmonar. Note que o alvéolo nunca está sozinho: cada um partilha parede com 5–6 vizinhos, e essa interdependência mecânica é o que mantém o conjunto aberto durante a respiração normal.]
)

Repare ainda na imagem acima na parte inferior, onde aparece um *cluster* de alvéolos envolvidos por capilares. Cada alvéolo está em contato com um leito capilar denso — quase não há "espaço morto" entre alvéolo e vaso. Essa é a justificativa anatômica para a barreira fina que você vai ver na próxima sessão.

#confusao-prevista(
  titulo: "Alvéolo não é saco passivo de ar",
  aluno_acha: [aluno pensa no alvéolo como um balão inerte que enche e esvazia, sem função própria além de "guardar ar"],
  mecanismo: [o alvéolo é parede biologicamente ativa: pneumócito II produz surfactante a cada poucos minutos; macrófago alveolar patrulha continuamente fagocitando partículas e bactérias; o epitélio sinaliza para o sistema imune quando detecta agressão. Virar saco passivo é o que acontece NA pneumonia (quando exsudato substitui a parede ativa) — não no normal.]
)

#subtopico("1.2 — Membrana alvéolo-capilar: a parede mais fina do corpo")

Imagine a folha de papel mais fina que você já viu. O papel comum tem cerca de 100 µm de espessura. A *membrana alvéolo-capilar* — a barreira que separa o ar dentro do alvéolo do sangue dentro do capilar — mede cerca de 0,3 µm. Mais fina que muitas membranas celulares isoladas. Por quê?

Porque a velocidade da troca de gás é inversamente proporcional à espessura. O O₂ tem que sair do ar alveolar, atravessar essa parede, entrar no sangue e se ligar à hemoglobina — tudo em menos de 0,75 segundo (o tempo que a hemácia leva para atravessar o capilar pulmonar em repouso). Se a parede fosse grossa como uma membrana plasmática normal, não daria tempo de equilibrar.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-05.png",
  largura: 70%,
  legenda: [Membrana alvéolo-capilar vista em histologia. (1) Espaço alveolar — onde fica o ar. (2) Pneumócito II, cuboide, ainda com aspecto granular pelo citoplasma cheio de corpos lamelares com surfactante pronto para liberação. (3) Hemácias dentro do capilar pulmonar — a coluna vermelha fica encostada na parede do alvéolo. (4) Pneumócito I, achatado, é o que cobre 95% da superfície alveolar e forma o "vidro fino" da barreira.]
)

A parede tem quatro camadas, cada uma com função específica:

1. Camada de surfactante (filme líquido com fosfolípides, ~0,1 µm) — não é exatamente "parede", mas é o que reveste o ar e impede o colapso (veja La Place na PARTE II).
2. Pneumócito I (epitélio achatado, ~0,1 µm) — célula gigante e fina que cobre 95% da área alveolar com 5% do total de células. É o "vidro" da barreira.
3. Membrana basal compartilhada com o capilar.
4. Endotélio capilar (também achatado).

E é só isso que separa O₂ do plasma. Quando algo engrossa qualquer uma dessas camadas — edema, fibrose, exsudato inflamatório —, a difusão cai. Você vai ver esse fenômeno em ação na PARTE III, quando os alvéolos da Catarina se encherem de exsudato fibrino-purulento e o caminho do O₂ passar de 0,3 µm para várias dezenas de micrômetros.

#mini-resumo[Membrana alvéolo-capilar = surfactante + pneumócito I + membrana basal + endotélio. Espessura ~0,3 µm. Pneumonia engrossa o caminho do O₂; em Fick, isso é T no denominador, e cresce o T cai V_gás.]

Os pneumócitos II merecem parágrafo próprio. São células cuboides menores, com citoplasma cheio de corpos lamelares (estruturas em camadas que armazenam surfactante pronto para liberação). Representam ~10% das células alveolares mas ocupam só ~5% da superfície — não estão ali para cobrir, estão ali para *produzir*. Além do surfactante, têm função de reserva: quando um pneumócito I morre (por toxicidade do oxigênio, por inflamação, por trauma), um pneumócito II vizinho prolifera, achata-se e vira pneumócito I. É a célula-tronco do epitélio alveolar.

Ao lado do alvéolo passa o capilar pulmonar. Diferente da circulação sistêmica, aqui o vaso recebe sangue *desoxigenado* (vindo do ventrículo direito) e devolve sangue *oxigenado* (para o átrio esquerdo). Toda a hemácia do corpo passa por aqui a cada ~1 minuto. A pressão hidrostática no capilar pulmonar é baixa (~12 mmHg, contra ~25 mmHg nos capilares sistêmicos) — isso é proteção, porque pressão alta espremeria líquido para dentro do alvéolo (edema pulmonar).

#subtopico("1.3 — Clearance mucociliar: a defesa que o cigarro desliga")

Aqui vem a parte que mais conecta a anatomia ao caso Catarina. O pulmão respira ar não-estéril o tempo todo. Cada inspiração traz poeira, bactérias, vírus, fungos, fragmentos celulares. Por que isso não vira pneumonia toda hora? Porque existe uma máquina de limpeza constante chamada *clearance mucociliar*, ou "elevador mucociliar", que arrasta tudo para fora antes de chegar ao alvéolo.

A máquina tem duas partes: o tapete de muco em cima, e os cílios que batem por baixo arrastando o tapete.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-03.png",
  largura: 65%,
  legenda: [Epitélio respiratório pseudo-estratificado. (1) Célula caliciforme — produz o muco; tem aspecto "de cálice" pelo acúmulo apical de grânulos. (2) Célula cilíndrica ciliada — bate os cílios na superfície apical, arrastando o muco. (3) Célula basal — tronco que repõe as anteriores. (4) Célula granular (neuroendócrina) — sensor químico do ambiente luminal.]
)

A célula caliciforme (do trato superior) produz o muco; junto com glândulas submucosas, ela libera uma mistura viscosa de glicoproteínas (mucinas), água, eletrólitos e proteínas antimicrobianas (lisozima, lactoferrina, defensinas). O muco organiza-se em duas camadas: uma camada *gel* viscoelástica por cima (que captura as partículas), e uma camada *sol* aquosa por baixo (onde os cílios batem livremente). Sem a camada sol, os cílios travam — é o que acontece na fibrose cística, onde o defeito no canal CFTR deixa o líquido superficial desidratado.

Os cílios do epitélio respiratório (são cílios "móveis" — diferentes dos cílios sensoriais imóveis de muitas outras células) batem com frequência de 12 a 15 Hz, num movimento bidirecional coordenado: golpe efetivo para frente (rápido, empurra o muco em direção à faringe) e golpe de recuperação para trás (lento, dobra o cílio sem arrastar o muco de volta). O resultado é uma esteira rolante contínua que move o muco da periferia do pulmão até a faringe, onde ele é engolido sem percebermos.

#figura-nebli(
  "/figuras/insuficiencia-respiratoria-catarina/slide-04.png",
  largura: 80%,
  legenda: [À esquerda, microscopia eletrônica dos cílios — cada cílio é um cilindro de microtúbulos (9+2) com dineína entre eles para gerar o batimento. À direita, esquema do "elevador": camada gel captura partículas; camada sol acomoda os cílios; batimento coordenado empurra muco para faringe. Cigarro paralisa esse mecanismo em horas.]
)

O cigarro é o vilão clássico desse sistema. Cada tragada deposita milhares de compostos químicos no epitélio respiratório, e os cílios respondem em duas escalas de tempo. Em horas, o batimento ciliar diminui — efeito direto da nicotina e de outros componentes voláteis. Em meses a anos de exposição crônica, o epitélio sofre *metaplasia escamosa*: as células cilíndricas ciliadas são substituídas por células escamosas (planas, sem cílios), que oferecem mais resistência mecânica mas perdem a função de transporte. O muco produzido pelas células caliciformes restantes (que aumentam em número — bronquite crônica) fica estagnado, virando meio de cultura para bactérias.

Catarina fumou um maço por dia durante dez anos e parou há cinco. Recuperação ciliar completa após cessação leva *meses a anos*, e a metaplasia escamosa persistente leva ainda mais tempo — em muitos casos, nunca volta totalmente ao normal. A confusão clássica aqui é achar que "5 anos sem fumar" já trouxe o pulmão de volta ao estado pré-cigarro. Não trouxe. O elevador mucociliar dela ainda funciona com fração da eficiência original, e essa é uma das razões pelas quais ela é mais vulnerável à pneumonia do que uma colega não-fumante da mesma idade.

#mini-resumo[Defesa pulmonar do alto até o alvéolo: filtro nasal → reflexo da tosse → muco + cílios (elevador mucociliar) → macrófago alveolar + imunidade celular. Cigarro tira o cílio; diabetes tira a função do macrófago. Catarina perdeu as duas.]

A diabetes é o segundo fator de defesa caída no caso. A hiperglicemia, mesmo "controlada com dieta", produz *produtos finais de glicação avançada* (AGEs) ao longo dos anos — proteínas e lipídios glicados que ficam menos funcionais. Em particular, neutrófilos diabéticos têm fagocitose menos eficiente, e a microangiopatia (alterações nos pequenos vasos) reduz a perfusão local — chega menos célula de defesa onde precisa. Um diabético tem 1,5 a 2 vezes mais pneumonia do que um não-diabético da mesma idade, e quando tem, evolui pior.

#sintese-box("PARTE I",
[O pulmão é um cano hierárquico que vira esponja. A esponja é feita de \~300 milhões de alvéolos com parede fina (0,3 µm) onde O₂ atravessa para o sangue e CO₂ sai. Essa parede contém pneumócitos I (cobertura), pneumócitos II (surfactante e reserva), endotélio capilar e membrana basal. Tudo isso vive em risco constante de invasão microbiana, mas é protegido pelo elevador mucociliar — muco em duas camadas + cílios batendo a 12–15 Hz. Cigarro paralisa os cílios; diabetes derruba os macrófagos. Quando essas defesas falham, a infecção atinge o alvéolo, e aí a física da troca gasosa (PARTE II) começa a desmoronar.]
)

A próxima PARTE vai mostrar essa física — quatro leis que descrevem como o gás atravessa a parede alveolar, como o alvéolo se mantém aberto, como ventilação e perfusão se acoplam, e como o sangue tampona o ácido produzido pelo metabolismo. Sem essas quatro leis, a leitura da gasometria de Catarina vira decoreba de tabelas. Com elas, vira diagnóstico mecanístico.
