#import "../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Uma proteína bacteriana purificada, mesmo em concentração muito alta, não ativa linfócitos T isolados. Explique mecanicamente por que aumentar a quantidade de antígeno não resolve o problema.],
  [O receptor de célula T não encaixa em proteína nativa. Ele reconhece uma superfície composta: um peptídeo linear curto deitado dentro da fenda de uma molécula de MHC própria, mais os resíduos polimórficos da borda dessa molécula. A proteína em solução nunca adquire essa forma, por mais concentrada que esteja. A falha, portanto, é de formato e não de quantidade. Para haver reconhecimento é preciso que uma célula apresentadora capture a proteína, a corte em peptídeos e exponha um deles na fenda — só então existe o alvo que o receptor foi selecionado para ler.])

#discursiva("Q2",
  [Explique por que a molécula de MHC de classe II deixa o retículo endoplasmático com a fenda ocupada pela cadeia invariante, e o que precisa acontecer para que ela apresente antígeno.],
  [O retículo está cheio de peptídeos bombeados pelo TAP e de proteínas próprias em síntese. Se a fenda da classe II saísse aberta, seria ocupada ali mesmo por peptídeo próprio e chegaria à superfície apresentando material do próprio corpo ao linfócito CD4, a linhagem que comanda a resposta. A cadeia invariante tapa a fenda e ainda endereça a molécula ao compartimento vesicular. Lá, as proteases a digerem e deixam o CLIP; o HLA-DM remove esse resto e favorece a entrada do peptídeo externo de maior afinidade. Só depois dessa troca a molécula segue para a membrana.])

#discursiva("Q3",
  [Explique como a arquitetura da fenda de cada classe de MHC determina qual maquinaria de processamento a abastece.],
  [A fenda da classe I é fechada nas duas extremidades e só acomoda peptídeos que caibam por inteiro, de oito a dez aminoácidos. Fragmentos desse tamanho são exatamente o produto do proteassoma citosólico, e por isso a classe I é abastecida pela via do citosol, com transporte ativo pelo TAP até o retículo. A fenda da classe II é aberta nas pontas e aceita peptídeos de treze a dezoito resíduos, com as extremidades sobrando para fora — o tipo de fragmento gerado por proteases lisossomais dentro de vesículas. Continente e conteúdo são compatíveis por construção.])

#discursiva("Q4",
  [Explique o impasse da resposta antiviral que a apresentação cruzada resolve, e como ela o resolve sem quebrar a regra do compartimento.],
  [Para se tornar citotóxico, o linfócito CD8 precisa de ajuda do CD4, e essa ajuda funciona melhor quando ambos são estimulados pela mesma apresentadora. Só que a célula dendrítica que fagocita uma célula infectada processaria aquele material pela via endocítica e o apresentaria apenas em classe II, ao CD4 — o CD8 ficaria de fora justamente na infecção viral. Algumas dendríticas deixam conteúdo do fagossomo escapar para o citosol; ali as proteínas externas passam pelo proteassoma, pelo TAP e pelo retículo, saindo em classe I. A regra do compartimento permanece: o que mudou foi o compartimento em que a proteína está.])

#discursiva("Q5",
  [Um vírus da família do herpes bloqueia o transportador de peptídeos e permanece anos em latência. Explique por que esse bloqueio funciona como estratégia de evasão e o que ele confirma sobre a montagem da molécula de classe I.],
  [A molécula de classe I é montada no retículo, onde a cadeia α e a β2-microglobulina aguardam o peptídeo trazido do citosol pelo TAP. A regra é rígida: o conjunto só se estabiliza e só é liberado do retículo depois que a fenda é ocupada. Bloquear o transportador interrompe a chegada do peptídeo, a molécula fica retida e a superfície da célula infectada se esvazia de classe I. Sem complexo peptídeo-MHC para ler, o linfócito T CD8 passa pela célula sem encontrar alvo, ainda que ela esteja produzindo proteína viral no citosol. A evasão é elegante porque não enfrenta a resposta já deflagrada: desliga a etapa que a deflagraria. E confirma, pela via negativa, que a apresentação por classe I é indissociável da carga da fenda.])
