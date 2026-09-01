#import "../typst-template/nebli_v2_apostila.typ": *

#let secoes-resumindo = (
  ("O que é um operon",
   [Um promotor, sítios de controle em cis e vários genes estruturais transcritos num mRNA policistrônico único. Como o transcrito é um só, ligar um gene é ligar todos — é assim que a bactéria coordena uma via metabólica inteira sem precisar de nenhum mecanismo adicional.]),

  ("Cis e trans decidem tudo",
   [Sequência de DNA — promotor, operador, sítio CAP — age em cis: só afeta os genes da própria molécula, porque endereço não difunde. Gene regulador produz proteína, que age em trans e alcança qualquer cópia da célula. Não é distância, é natureza do elemento.]),

  ("O repressor Lac e o que ele trava",
   [O tetrâmero codificado pelo lacI ocupa o operador, sobreposto ao início da transcrição. A polimerase ainda pousa no promotor; o que ela não consegue é abrir a bolha e escapar para o alongamento. A queda é de cerca de mil vezes, nunca até zero.]),

  ("Alolactose é o indutor, não a lactose",
   [A β-galactosidase converte parte da lactose em alolactose, que se liga a um sítio alostérico do repressor e derruba sua afinidade pelo operador. O resíduo basal de permease e enzima é o que permite ao circuito arrancar; o IPTG induz sem ser consumido.]),

  ("Constitutivo por dois caminhos",
   [O#super[c] é operador que o repressor não reconhece mais: dominante, mas só sobre os genes da própria molécula. lacI#super[-] é repressor incapaz de ligar DNA: recessivo, porque uma cópia boa difunde e corrige as duas. Mesmo fenótipo na placa, mecanismos opostos.]),

  ("Diploide parcial e os alelos que fecham a lógica",
   [Duas cópias da região lac na mesma célula separam endereço de produto. lacI#super[s] perdeu o sítio do indutor e prende o operador para sempre — não-induzível e dominante em trans. lacI#super[-d] produz subunidade que envenena o tetrâmero misto: perda de função com efeito dominante.]),

  ("Promotor fraco é projeto, não defeito",
   [As caixas -35 e -10 do promotor lac divergem do consenso TTGACA e TATAAT, e cada divergência custa um contato com a subunidade σ. Promotor forte já opera no teto e não deixa amplitude para regular; a base baixa é justamente o que torna o ativador útil.]),

  ("CAP-cAMP como sensor de glicose",
   [Glicose entrando mantém a EIIA desfosforilada, a adenilato-ciclase parada e o cAMP baixo, deixando a CAP sem ligante. Sem glicose o cAMP sobe, a CAP dobra o DNA e recruta a polimerase pelo contato com a subunidade α. A mesma EIIA ainda inibe a permease — exclusão do indutor.]),

  ("Quatro estados e uma porta lógica",
   [O operon só transcreve alto com lactose presente e glicose ausente, porque cada sinal libera um gargalo diferente. Sem lactose o estado da CAP é irrelevante: recrutar melhor uma polimerase que vai ficar travada no operador não adianta. O platô da curva diáuxica é o tempo dessa indução.]),

  ("O mapa geral: trp e ara",
   [Efeito da proteína (negativo reduz, positivo aumenta) e sentido do sinal (indutível liga, reprimível desliga) são dimensões independentes. No trp, o triptofano é co-repressor e ainda há atenuação pelo peptídeo-líder; no operon da arabinose, a AraC reprime sem o açúcar e ativa com ele.]),
)

#resumindo-page(secoes-resumindo)
