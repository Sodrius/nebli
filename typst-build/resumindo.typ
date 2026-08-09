#import "../typst-template/nebli_v2_apostila.typ": *

#let secoes-resumindo = (
  ("A solubilidade decide o mecanismo",
   [Peptídeos e catecolaminas são hidrossolúveis: viajam livres no plasma, param na membrana e precisam de receptor de superfície. Esteroides e tireoidianos são lipossolúveis: precisam de carreador no sangue, mas atravessam a membrana e encontram o receptor dentro da célula.]),

  ("Membrana muda atividade; núcleo muda quantidade",
   [O hormônio de membrana altera a atividade de proteínas que já existem, por fosforilação — responde em segundos e termina em segundos. O hormônio nuclear altera quantas proteínas serão fabricadas, por transcrição — responde em horas e dura dias.]),

  ("Amplificação em cascata",
   [Uma molécula ocupa um receptor, que ativa dezenas de proteínas G, cada uma ativando uma ciclase que produz milhares de AMPc. Uma única molécula de hormônio se traduz em cerca de um milhão de moléculas de produto — por isso concentração nanomolar basta.]),

  ("A célula beta mede glicemia pela própria glicólise",
   [GLUT2 e glicoquinase deixam a entrada e a fosforilação de glicose proporcionais à glicemia. Mais glicose gera mais ATP, o ATP fecha o canal de potássio, a membrana despolariza, o cálcio entra e a vesícula de insulina é liberada.]),

  ("Insulina desfosforila; glucagon e adrenalina fosforilam",
   [A insulina age por tirosina-cinase e termina ativando a fosfatase PP1, que desfosforila as enzimas do combustível. Glucagon e adrenalina agem por AMPc e PKA, que fosforilam as mesmas enzimas — mesmo alvo, sinal invertido.]),

  ("Controle recíproco do glicogênio",
   [A glicogênio-sintase é ativa desfosforilada e a fosforilase é ativa fosforilada. Uma cinase só desliga a síntese e liga a quebra ao mesmo tempo; uma fosfatase só faz o inverso. Nunca as duas vias abertas juntas.]),

  ("Peptídeo C, sulfonilureia e diazóxido",
   [O peptídeo C sai um a um com a insulina e por isso distingue insulina própria de insulina injetada. A sulfonilureia fecha o canal de potássio e força secreção; o diazóxido o mantém aberto e freia a hipersecreção do insulinoma.]),

  ("T4 é reserva; T3 é o ativo",
   [A tireoide secreta muito mais T4 do que T3, mas o T4 tem baixa afinidade pelo receptor. As desiodases dos tecidos periféricos decidem, localmente, se retiram o iodo do anel externo, gerando T3 ativo, ou do interno, gerando T3 reverso inativo.]),

  ("Cortisol converte tecido em glicose",
   [O cortisol aumenta gliconeogênese no fígado, degrada proteína no músculo, mobiliza gordura no adiposo e freia a insulina no pâncreas. Tudo aponta para manter a glicemia num estresse prolongado, às custas de músculo e gordura.]),

  ("Retroalimentação negativa e seus extremos",
   [O cortisol inibe hipotálamo e hipófise, estabilizando a própria concentração. Em Addison falta cortisol, o freio some e o ACTH alto escurece a pele; em Cushing o cortisol sobra, com hiperglicemia, perda muscular e gordura redistribuída para tronco e face.]),
)

#resumindo-page(secoes-resumindo)
