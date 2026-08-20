#import "../typst-template/nebli_v2_apostila.typ": *

#resumindo-page((
  ("O linfócito T não enxerga o antígeno",
   [O TCR não reconhece proteína nativa nem micro-organismo: só encaixa num peptídeo curto deitado dentro da fenda de uma molécula de MHC na superfície de outra célula. Toda a aula é a consequência dessa cegueira estrutural.]),
  ("Classe I mostra o que a célula produz",
   [A molécula de classe I existe em toda célula nucleada e carrega peptídeos gerados no citosol. É assim que uma célula infectada por vírus ou transformada denuncia o que fabrica por dentro, e por isso ela conversa com o linfócito CD8, que mata.]),
  ("Classe II mostra o que veio de fora",
   [A molécula de classe II é privilégio da célula dendrítica, do macrófago e do linfócito B, e carrega peptídeos digeridos dentro de vesículas. Ela conversa com o linfócito CD4, que coordena a resposta em vez de matar.]),
  ("O correceptor emparelha classe e linhagem",
   [CD8 liga o domínio α3 da classe I e CD4 liga o domínio β2 da classe II — regiões que não variam entre pessoas e ficam longe da fenda. O correceptor não escolhe peptídeo: ele garante que o linfócito certo leia a classe certa.]),
  ("A arquitetura da fenda impõe a via",
   [A fenda da classe I é fechada nas pontas e aceita 8 a 10 aminoácidos; a da classe II é aberta e aceita 13 a 18. Tamanhos diferentes exigem cortes diferentes — é a razão de existirem duas maquinarias de processamento.]),
  ("Via citosólica: etiqueta, proteassoma, TAP",
   [A proteína do citosol é marcada por ubiquitina, cortada pelo proteassoma em fragmentos curtos e bombeada pelo TAP, com gasto de ATP, para dentro do retículo. Lá a classe I é carregada — e só sai para a superfície se a fenda estiver ocupada.]),
  ("Via endocítica: cadeia invariante, CLIP e DM",
   [A classe II sai do retículo com a fenda tampada pela cadeia invariante, para que peptídeo próprio não a ocupe antes da hora. Na vesícula, a digestão deixa o CLIP, que o HLA-DM remove, permitindo entrar o peptídeo externo de maior afinidade.]),
  ("Apresentação cruzada resolve o impasse do CD8",
   [Algumas células dendríticas deixam material do fagossomo escapar para o citosol. Aquele antígeno externo entra na via do proteassoma e sai em classe I — assim a mesma célula ativa CD4 e CD8 juntos, e o CD4 licencia o CD8 a se tornar citotóxico.]),
  ("Restrição ao MHC e polimorfismo",
   [No timo sobrevive o linfócito que reconhece peptídeo estranho dentro de molécula própria: trocar qualquer metade do par anula o reconhecimento. Cada pessoa herda dois haplótipos codominantes, e a variação entre alelos concentra-se justamente na fenda.]),
  ("Apresentar não é ativar",
   [O encaixe TCR-peptídeo-MHC é só o primeiro sinal. Sem coestimulação por B7-CD28, o linfócito entra em anergia. Como o coestímulo só aparece na apresentadora que reconheceu um padrão de patógeno, é o inato que autoriza o adquirido a responder.]),
))
