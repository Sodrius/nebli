#import "../typst-template/nebli_v2_apostila.typ": *

#questao-mc("01", badge-consolidacao,
  [Sobre a lógica termodinâmica que justifica a existência da cadeia respiratória, é correto afirmar:],
  (("A", [A oxidação completa da glicose libera energia em quantidade tão pequena que precisa ser amplificada pela cadeia respiratória através de um efeito cascata de reações em série na membrana interna mitocondrial. Esse modelo seria coerente apenas se o ΔG fosse positivo no balanço total da reação, o que contradiz a queda real do potencial entre NADH e O₂.]),
   ("B", [A cadeia respiratória existe para garantir que a oxidação da glicose só aconteça em condições de baixo oxigênio celular, protegendo as estruturas mitocondriais sensíveis à oxidação direta pelo O₂. O argumento ignora que a cadeia opera em condições aeróbicas e que o O₂ não é fonte de dano nas estruturas mitocondriais funcionais quando os complexos estão íntegros.]),
   ("C", [A energia liberada pela oxidação completa da glicose (cerca de 2.870 kJ/mol) é grande demais para ser capturada em uma única reação; a cadeia respiratória fraciona essa liberação em degraus de ~20 kJ/mol, escala que enzimas conseguem aproveitar como bombeamento de prótons.]),
   ("D", [O fracionamento da oxidação serve para gerar ATP em quantidade exatamente proporcional ao número de carbonos da glicose, mantendo razão estequiométrica fixa entre substrato e moeda energética da célula em qualquer condição metabólica. A proporção exata entre carbonos e ATP é variável fisiologicamente (depende da lançadeira e do tecido) — manter razão fixa não corresponde ao comportamento real da via metabólica humana.]),
   ("E", [A cadeia respiratória existe porque a oxidação direta pela O₂ é cineticamente impossível em meio aquoso; a cadeia fornece catalisadores enzimáticos que aceleram a reação por fatores de ordem 10⁶ em condições fisiológicas normais. Apesar de catalisadores serem necessários, a aceleração cinética não explica por que a oxidação é fracionada em quatro complexos em vez de uma única reação enzimática terminal acoplada ao oxigênio molecular.])))

#questao-ce("02", badge-consolidacao,
  [Sobre os componentes anatômicos da cadeia respiratória, julgue os itens a seguir:],
  (("I", [A cadeia respiratória está localizada na membrana interna mitocondrial, que é altamente impermeável a íons e prótons em condições fisiológicas.]),
   ("II", [A membrana externa mitocondrial contém porinas que tornam o espaço intermembrana quimicamente equivalente ao citosol em pequenas moléculas e íons.]),
   ("III", [A matriz mitocondrial contém as enzimas solúveis do ciclo de Krebs, da β-oxidação, além de DNA mitocondrial e ribossomos próprios em razão da origem endossimbiótica do organelo.]),
   ("IV", [Coenzima Q e citocromo c são proteínas integrais grandes equivalentes em estrutura aos 4 complexos da cadeia respiratória.])))

#questao-mc("03", badge-consolidacao,
  [Os elétrons fluem ao longo da cadeia respiratória do par redox com potencial padrão mais negativo para o par com potencial padrão mais positivo. Considerando os pares NAD⁺/NADH (E' = -0,32 V) e O₂/H₂O (E' = +0,82 V), é correto afirmar:],
  (("A", [Os elétrons fluem do par O₂/H₂O para o par NAD⁺/NADH porque o oxigênio é um doador mais forte de elétrons que o NADH em condições padrão bioquímicas. O potencial padrão de oxirredução mede afinidade por elétrons; o par com E' mais positivo é o aceptor mais forte — daí o O₂ ser o aceptor terminal e não doador da cadeia.]),
   ("B", [O ΔE total da cadeia é negativo (cerca de -1,14 V), refletindo o fato de que a transferência ocorre contra o gradiente termodinâmico natural dos pares redox envolvidos. O sinal de ΔE da cadeia respiratória é positivo (+1,14 V) porque os elétrons fluem do par mais negativo para o mais positivo, gerando ΔG negativo e reação termodinamicamente espontânea.]),
   ("C", [O ΔG° é positivo para a transferência completa de NADH a O₂, exigindo input energético externo na forma de hidrólise de ATP em cada etapa da cadeia respiratória mitocondrial. A oxidação biológica do NADH ao O₂ é espontânea e não exige input de ATP em nenhum ponto — esse seria o oposto do que a cadeia respiratória faz fisiologicamente em mitocôndrias funcionais.]),
   ("D", [O ΔG° é cerca de -220 kJ/mol para a transferência de 2 elétrons do NADH ao O₂, calculado por ΔG° = -nFΔE' (n=2; F=96,5 kJ/V·mol; ΔE'=+1,14 V) — energia mais que suficiente para gerar múltiplos ATPs se fracionada.]),
   ("E", [O ΔG° depende apenas do número de prótons bombeados pelos complexos e não da diferença de potencial entre os pares redox dos doadores e aceptores envolvidos. A relação ΔG = -nFΔE é fundamental — o número de prótons bombeados é consequência, não causa primária da variação de energia livre observada nas transferências eletrônicas mitocondriais.])))

#questao-mc("04", badge-consolidacao,
  [Quanto à entrada dos elétrons do NADH e do FADH₂ na cadeia respiratória, é correto afirmar:],
  (("A", [Tanto NADH quanto FADH₂ entram pelo Complexo I, com a diferença sendo apenas o grupo prostético envolvido (FMN para NADH, FAD para FADH₂) na transferência inicial dos elétrons à CoQ.]),
   ("B", [NADH entra pelo Complexo I (via FMN e centros Fe-S) gerando bombeamento de 4 H⁺; FADH₂ entra pelo Complexo II (succinato desidrogenase) sem bombear prótons no Complexo II, gerando rendimento menor de ATP no saldo final.]),
   ("C", [FADH₂ entra pelo Complexo I e NADH entra pelo Complexo II, refletindo a sequência inversa em que aparecem no ciclo de Krebs e na β-oxidação de ácidos graxos durante o metabolismo aeróbico.]),
   ("D", [Ambos NADH e FADH₂ entram diretamente na coenzima Q, sem passagem pelos Complexos I ou II, em uma redução direta da benzoquinona lipossolúvel pelos equivalentes redutores produzidos no metabolismo.]),
   ("E", [NADH e FADH₂ entram pelo Complexo III, que é o ponto comum de convergência dos elétrons antes da passagem pelo citocromo c em direção ao Complexo IV citocromo oxidase mitocondrial.])))

#questao-ce("05", badge-consolidacao,
  [Sobre o Complexo II e o succinato desidrogenase, julgue:],
  (("I", [O Complexo II é a única enzima do ciclo de Krebs que está cravada na membrana mitocondrial interna; as demais são solúveis na matriz.]),
   ("II", [O Complexo II bombeia 2 prótons por par de elétrons da matriz para o espaço intermembrana, contribuindo para o gradiente eletroquímico que dirige a ATP sintase.]),
   ("III", [Os elétrons do FADH₂ gerado dentro do Complexo II são transferidos diretamente à Coenzima Q sem necessidade de envolver o Complexo I ou outros carregadores intermediários.]),
   ("IV", [O succinato é o substrato do Complexo II e é convertido a fumarato durante a transferência dos elétrons; essa é simultaneamente uma reação do ciclo de Krebs.])))

#questao-mc("06", badge-consolidacao,
  [O ciclo Q do Complexo III resolve uma incompatibilidade estrutural específica da cadeia respiratória. Que incompatibilidade é essa?],
  (("A", [Coenzima Q carrega 2 elétrons (CoQH₂ → CoQ), mas citocromo c carrega apenas 1 elétron por vez (Fe³⁺ ↔ Fe²⁺); o ciclo Q bifurca os 2 elétrons da CoQ entregando 1 ao citocromo c e desviando o outro de volta para outra molécula de CoQ.]),
   ("B", [Citocromo c funciona apenas em meio lipídico, enquanto a CoQ é hidrossolúvel; o ciclo Q transforma a CoQ em forma compatível com a passagem para o citocromo c hidrossolúvel localizado na matriz mitocondrial interna.]),
   ("C", [A diferença de potencial entre CoQ e citocromo c é negativa, impedindo o fluxo espontâneo dos elétrons; o ciclo Q inverte essa polaridade através de bombeamento ativo de elétrons contra o gradiente termodinâmico natural.]),
   ("D", [Os centros Fe-S do Complexo III só aceitam elétrons aos pares, enquanto a CoQ doa elétrons individualmente; o ciclo Q acumula elétrons da CoQ até formar pares antes da transferência aos centros Fe-S do complexo.]),
   ("E", [A Coenzima Q precisa ser regenerada em sua forma oxidada por dois ciclos consecutivos de Krebs, e o Complexo III coordena essa regeneração através do ciclo Q como mecanismo de feedback metabólico em condições de alta demanda energética.])))

#questao-mc("07", badge-consolidacao,
  [A teoria quimiosmótica proposta por Peter Mitchell em 1961 (Nobel de 1978) explica o acoplamento entre transporte de elétrons e síntese de ATP através de:],
  (("A", [Uma molécula intermediária de alta energia (X~P) que carrega a energia liberada pela cadeia respiratória diretamente para o sítio catalítico da ATP sintase, fechando o ciclo da fosforilação oxidativa em uma única etapa enzimática.]),
   ("B", [Uma proteína transportadora específica que liga o ADP gerado pela hidrólise do ATP ao sítio do Complexo IV, sincronizando consumo de oxigênio com regeneração de ATP em todos os tecidos animais funcionalmente acoplados.]),
   ("C", [Um gradiente de carbonato/bicarbonato gerado pela acidificação local do citosol durante o trabalho metabólico, atuando como tampão fisiológico que estabiliza o pH durante a oxidação dos combustíveis na matriz mitocondrial.]),
   ("D", [Uma reação acoplada via enzima específica que catalisa simultaneamente a oxidação do NADH e a fosforilação do ADP usando a mesma energia em uma única etapa catalítica de transferência de fosfato.]),
   ("E", [Um gradiente eletroquímico de prótons (força próton-motriz) através da membrana mitocondrial interna, gerado pelo bombeamento dos complexos respiratórios e consumido pela ATP sintase para gerar ATP em uma turbina molecular rotativa.])))

#questao-ce("08", badge-consolidacao,
  [Sobre a ATP sintase F₀F₁ e o mecanismo de binding change descoberto por Paul Boyer (Nobel de 1997), julgue:],
  (("I", [A subunidade F₀ (lê-se "F-zero", em referência à sensibilidade à oligomicina) é um canal de prótons embebido na membrana mitocondrial interna, em forma de roda rotatória.]),
   ("II", [A subunidade F₁ saliente para a matriz tem 3 sítios catalíticos que passam por 3 conformações sequenciais: Loose (liga ADP+Pi), Tight (forma ATP) e Open (libera ATP).]),
   ("III", [A energia da rotação dos prótons é usada para *formar* a ligação fosfoanidrido do ATP no sítio catalítico, com gasto energético direto na ligação química e não na liberação.]),
   ("IV", [Oligomicina liga-se à subunidade F₀ impedindo a rotação, e em mitocôndrias funcionais a ATP sintase opera no sentido de síntese (não hidrólise) de ATP.])))

#questao-mc("09", badge-consolidacao,
  [A razão P/O (fosforilações por átomo de oxigênio reduzido) atualmente aceita para NADH e FADH₂ na cadeia respiratória humana é:],
  (("A", [NADH: P/O = 3,0 (clássico); FADH₂: P/O = 2,0 (clássico) — valores que rendem o saldo total de 38 ATP por glicose oxidada em condições aeróbicas plenas.]),
   ("B", [NADH: P/O = 2,5; FADH₂: P/O = 1,5 — valores que rendem saldo de 30-32 ATP por glicose, dependendo da lançadeira de NADH citosólico operante no tecido.]),
   ("C", [NADH e FADH₂ têm P/O idênticos (~1,5) porque a cadeia respiratória gera quantidade fixa de ATP por par de elétrons, independente do ponto de entrada na cadeia.]),
   ("D", [NADH tem P/O = 4,0 e FADH₂ tem P/O = 2,5, valores que justificam o saldo elevado da β-oxidação dos ácidos graxos quando comparado à oxidação aeróbica da glicose pelo ciclo de Krebs.]),
   ("E", [P/O depende exclusivamente do tecido analisado e varia de 1 a 5 sem relação direta com o ponto de entrada do equivalente redutor na cadeia respiratória mitocondrial.])))

#questao-mc("10", badge-consolidacao,
  [Sobre a distinção fundamental entre inibidores e desacopladores da fosforilação oxidativa, é correto afirmar:],
  (("A", [Inibidores aceleram o consumo de O₂ porque liberam o gradiente acumulado, enquanto desacopladores travam o consumo de O₂ por feedback negativo do gradiente sobre os complexos respiratórios mitocondriais.]),
   ("B", [Inibidores e desacopladores produzem efeitos clínicos idênticos porque ambos bloqueiam a síntese de ATP independentemente do mecanismo molecular subjacente envolvido em cada caso.]),
   ("C", [Inibidores agem apenas na ATP sintase (F₀ ou F₁), enquanto desacopladores agem exclusivamente nos complexos respiratórios I a IV bloqueando o transporte de elétrons em pontos específicos.]),
   ("D", [Inibidores travam o transporte de elétrons (O₂ consumo cai a zero), enquanto desacopladores deixam a cadeia rodar mas furam a membrana para H⁺ — O₂ consumo aumenta, gradiente vaza, toda energia vira calor sem ATP.]),
   ("E", [Inibidores são sempre tóxicos letais enquanto desacopladores são sempre fisiológicos e mantidos sob controle pela própria célula através de mecanismos de feedback negativo robustos.])))

#questao-mc("11", badge-integracao,
  [Em um experimento de oximetria com mitocôndrias isoladas em meio com succinato como substrato, é adicionado rotenona em quantidade suficiente para bloquear completamente o Complexo I. Sobre o consumo de O₂ resultante, espera-se:],
  (("A", [Queda imediata e completa do consumo de O₂ a zero, pois a rotenona bloqueia o ponto de entrada exclusivo de todos os elétrons na cadeia respiratória mitocondrial em todas as condições experimentais.]),
   ("B", [Aumento explosivo do consumo de O₂ devido ao desvio dos elétrons do Complexo I para o Complexo II, gerando uma rota compensatória de oxidação acelerada do succinato em meio acidificado.]),
   ("C", [Consumo de O₂ preservado em ritmo praticamente normal porque os elétrons do succinato entram pelo Complexo II (que não depende do Complexo I) e seguem normalmente CoQ → III → cit c → IV → O₂.]),
   ("D", [Consumo de O₂ reduzido em proporção exata ao número de moléculas de rotenona ligadas, sem dependência da disponibilidade de outros substratos doadores de elétrons no meio experimental.]),
   ("E", [Inversão da direção do fluxo de elétrons na cadeia, com geração de espécies reativas de oxigênio em quantidade tão elevada que provoca lise imediata das mitocôndrias do preparado experimental.])))

#questao-ce("12", badge-integracao,
  [Em uma mitocôndria isolada, são feitas três adições sequenciais: (1) ADP em excesso, (2) oligomicina, (3) DNP (2,4-dinitrofenol). Sobre o consumo de O₂ em cada momento, julgue:],
  (("I", [Após adição de ADP em excesso, o consumo de O₂ aumenta — o ADP é o sinal que faz a ATP sintase girar, dissipando o gradiente e liberando os complexos para bombear novamente em estado 3 da respiração mitocondrial.]),
   ("II", [Após adição de oligomicina (que segue o ADP), o consumo de O₂ aumenta ainda mais porque a oligomicina libera os complexos respiratórios do controle por gradiente, permitindo bombeamento máximo de prótons em todos os 4 complexos.]),
   ("III", [Após adição de DNP (que segue a oligomicina), o consumo de O₂ aumenta porque o DNP perfura a membrana para H⁺ e dissipa o gradiente, removendo a retroinibição imposta pela oligomicina e deixando a cadeia respiratória acelerar ao máximo.]),
   ("IV", [Em qualquer dessas três condições, há síntese normal de ATP, garantida pela presença de fosfato inorgânico e ADP no meio experimental, independente do estado do gradiente eletroquímico mitocondrial.])))

#questao-mc("13", badge-integracao,
  [Um paciente intoxicado com cianeto chega à emergência com sangue venoso vermelho-cereja, taquicardia, taquipneia e rebaixamento de consciência. O mecanismo bioquímico que explica essa apresentação é:],
  (("A", [Cianeto bloqueia o Complexo IV (citocromo oxidase), impedindo a redução final do O₂ a H₂O; o oxigênio fica disponível no sangue (não é consumido) mas a célula não pode usá-lo — quadro de hipóxia histotóxica; a falência ATP-dependente é o que mata.]),
   ("B", [Cianeto se liga à hemoglobina com afinidade maior que o O₂, formando cianometemoglobina que não transporta oxigênio aos tecidos periféricos, gerando hipóxia hipoxêmica de tipo similar à intoxicação por monóxido de carbono em pacientes não tratados.]),
   ("C", [Cianeto inibe o Complexo I por mecanismo similar à rotenona, parando a cadeia no ponto inicial e levando ao acúmulo de NADH não-oxidado que deprime o ciclo de Krebs e o metabolismo aeróbico de forma cascata gradual e progressiva.]),
   ("D", [Cianeto é um desacoplador que funciona como o DNP, dissipando o gradiente e produzindo hipertermia letal por dissipação de energia em calor sem geração de ATP nos tecidos periféricos do organismo intoxicado.]),
   ("E", [Cianeto causa hemólise maciça por oxidação direta da hemoglobina a metemoglobina em todas as hemácias circulantes, gerando anemia hemolítica aguda como mecanismo principal da letalidade observada em intoxicações agudas humanas.])))

#questao-mc("14", badge-integracao,
  [Considere um paciente musculista que adquiriu DNP no mercado ilegal para "secar" rapidamente para uma competição. Após overdose, chega à emergência com hipertermia (41,8°C), taquicardia, sudorese profusa e óbito em 6 horas apesar de medidas suportivas agressivas. O mecanismo da letalidade do DNP é:],
  (("A", [DNP bloqueia o Complexo IV impedindo o consumo de O₂; a hipertermia decorre da elevação compensatória do metabolismo basal por estímulo simpático intenso secundário à hipóxia tissular instalada em todos os órgãos.]),
   ("B", [DNP inibe a glicose-6-fosfatase hepática, gerando hipoglicemia profunda e elevação de cetonas circulantes; a hipertermia é consequência do estado de cetose com produção exagerada de calor pelo tecido adiposo marrom em hibernadores adultos humanos.]),
   ("C", [DNP é um inibidor da ATP sintase semelhante à oligomicina, levando à parada da cadeia respiratória e à hipertermia paradoxal por elevação do gasto basal compensatório do tecido muscular esquelético em condições anaeróbicas.]),
   ("D", [DNP é desacoplador lipossolúvel que perfura a membrana mitocondrial interna para H⁺, dissipando o gradiente sem passar pela ATP sintase; cadeia respiratória acelera tentando recompor, O₂ é consumido em volume máximo, mas toda a energia da oxidação vira calor, levando à hipertermia letal.]),
   ("E", [DNP é precursor de óxido nítrico endógeno em altas concentrações; a hipertermia decorre da vasodilatação maciça com choque distributivo descompensado e óbito por colapso circulatório periférico em poucas horas após ingesta.])))

#questao-ce("15", badge-integracao,
  [Sobre as lançadeiras mitocondriais do NADH citosólico e o saldo final de ATP por glicose, julgue:],
  (("I", [A membrana mitocondrial interna é impermeável ao NADH citosólico — as lançadeiras transferem os equivalentes redutores via intermediários que atravessam a membrana, não o NADH em si.]),
   ("II", [A lançadeira malato-aspartato (predominante no fígado, rim e coração) entrega os elétrons como FADH₂ matricial, rendendo 1,5 ATP por NADH citosólico ao final da oxidação.]),
   ("III", [A lançadeira glicerol-3-fosfato (predominante no músculo esquelético e cérebro) entrega os elétrons como FADH₂ via Complexo II, rendendo 1,5 ATP por NADH citosólico (perda de 1 ATP por molécula).]),
   ("IV", [O saldo de ATP por glicose oxidada varia de 30 a 32 dependendo da lançadeira operante no tecido — malato-aspartato resulta em saldo maior (~32) e glicerol-3-fosfato em saldo menor (~30).])))

#questao-mc("16", badge-integracao,
  [Em um experimento, mitocôndrias isoladas são incubadas com substrato (succinato), ADP, fosfato e oxigênio. Observa-se consumo de O₂ acelerado e síntese de ATP em ritmo correspondente. Em seguida, é adicionado um antibiótico que se liga ao F₀ da ATP sintase. O efeito esperado sobre consumo de O₂ é:],
  (("A", [Aumento do consumo de O₂, porque a ligação ao F₀ libera os prótons para vazarem livremente pela membrana, dissipando o gradiente e permitindo aceleração contínua da cadeia em busca de recomposição energética. A ligação de oligomicina ao F₀ NÃO permite passagem livre de prótons — pelo contrário, ela bloqueia o canal e impede o vazamento, gerando retroinibição sobre todos os complexos da cadeia mitocondrial.]),
   ("B", [Queda do consumo de O₂ — o antibiótico (oligomicina) bloqueia a passagem de prótons pela ATP sintase; o gradiente cresce e retroinibe os complexos da cadeia respiratória; sem dissipação, a cadeia para. Consumo de O₂ cai a níveis basais ou abaixo, com cessação da síntese de ATP.]),
   ("C", [Inversão da direção do fluxo da ATP sintase, com hidrólise de ATP residual sendo usada para bombear prótons de volta para o espaço intermembrana até esgotamento das reservas energéticas mitocondriais existentes no preparado. A ATP sintase em mitocôndrias funcionais opera apenas no sentido de síntese sob gradiente positivo; reverter para hidrólise só ocorre em condições não fisiológicas com gradiente colapsado e ATP elevado no meio experimental.]),
   ("D", [Manutenção do consumo de O₂ em ritmo normal porque a inibição da ATP sintase não interfere com o transporte de elétrons na cadeia respiratória, que opera independentemente da síntese de ATP em qualquer condição. A retroinibição do gradiente sobre os complexos é fenômeno conhecido (controle respiratório) — bloquear a ATP sintase necessariamente afeta o transporte de elétrons em mitocôndrias acopladas.]),
   ("E", [Liberação súbita de íons cálcio do retículo sarcoplasmático mitocondrial, com contração espasmódica dos sarcômeros adjacentes e consumo descontrolado de oxigênio celular em todos os tecidos preparados em ambiente experimental. A liberação de Ca²⁺ não está mecanisticamente conectada à inibição da ATP sintase por oligomicina — o evento não ocorre por esse motivo em preparados de mitocôndrias isoladas usados em ensaios clássicos.])))

#questao-ce("17", badge-integracao,
  [Sobre a relação entre a cadeia respiratória e o ciclo de Krebs, julgue:],
  (("I", [O Complexo II (succinato desidrogenase) é a única enzima do ciclo de Krebs que está fixada na membrana mitocondrial interna; as demais enzimas do ciclo são solúveis na matriz.]),
   ("II", [Os equivalentes redutores gerados no ciclo de Krebs (NADH e FADH₂) são utilizados imediatamente pela cadeia respiratória — o ciclo de Krebs depende da cadeia para regenerar NAD⁺ e FAD oxidados, mantendo o fluxo metabólico aeróbico contínuo.]),
   ("III", [Em condições de bloqueio total da cadeia respiratória (ex.: cianeto), o ciclo de Krebs também para porque NADH e FADH₂ acumulam-se sem serem oxidados; a produção de ATP de qualquer fonte aeróbica é interrompida nessa situação.]),
   ("IV", [O GTP gerado no ciclo de Krebs (passo da succinil-CoA → succinato) depende diretamente da cadeia respiratória para sua síntese e não é produzido em condições de bloqueio dos complexos respiratórios I a IV.])))

#questao-mc("18", badge-integracao,
  [A teoria quimiosmótica de Mitchell foi inicialmente recebida com ceticismo pela comunidade científica porque contrariava o modelo dominante de intermediário químico de alta energia. Sobre as evidências experimentais que sustentaram a teoria, é correto afirmar:],
  (("A", [Mitchell isolou e caracterizou quimicamente uma molécula intermediária (X~P) que ligava a cadeia respiratória à ATP sintase via ligação fosfoanidrido de alta energia armazenada em grupo lateral fosfatado de proteína matricial.]),
   ("B", [A teoria foi validada quando ficou demonstrado que mitocôndrias inteiras eram desnecessárias — mitocondriossomos solúveis em meio aquoso geravam ATP a partir de NADH sem necessidade de qualquer membrana lipídica intacta na preparação.]),
   ("C", [Mitchell mostrou que mitocôndrias com membrana íntegra geravam gradiente de prótons mensurável durante a respiração, e que esse gradiente era requisito para a síntese de ATP — quando a membrana era danificada (perda de gradiente), a síntese cessava mesmo com cadeia respiratória funcional.]),
   ("D", [A teoria foi corroborada pelo isolamento de bactérias mutantes incapazes de gerar gradiente eletroquímico e que, no entanto, sintetizavam ATP em ritmo elevado mesmo em condições anaeróbicas com substratos puramente glicolíticos disponíveis.]),
   ("E", [A descoberta da fosforilação a nível de substrato no ciclo de Krebs e na glicólise tornou a teoria quimiosmótica desnecessária, demonstrando que toda síntese aeróbica de ATP poderia ser explicada por reações solúveis sem participação de gradientes através de membranas.])))

#questao-mc("19", badge-integracao,
  [Considere um paciente com mutação em um gene mitocondrial codificador de uma subunidade do Complexo I (deficiência parcial — atividade residual de ~30% do normal). A apresentação clínica esperada e o mecanismo bioquímico subjacente são:],
  (("A", [Paciente é saudável e assintomático porque o ciclo de Krebs gera FADH₂ via succinato desidrogenase do Complexo II como rota compensatória completa, mantendo o fluxo metabólico aeróbico inalterado em todos os tecidos.]),
   ("B", [Paciente apresenta hemólise crônica leve com anemia compensada por aumento de produção medular; o quadro decorre da fragilidade aumentada das hemácias por sobrecarga oxidativa secundária à deficiência do Complexo I em todos os tecidos analisados.]),
   ("C", [Paciente apresenta sintomas em tecidos com alta demanda energética (sistema nervoso central, músculo esquelético, retina) — encefalomiopatia, ataxia, miopatia. A passagem dos elétrons do NADH é prejudicada, NADH acumula, geração de ATP cai abaixo do necessário em tecidos oxidativos.]),
   ("D", [Paciente apresenta intolerância à glicose com hiperglicemia pós-prandial, porque a deficiência do Complexo I impede o consumo aeróbico da glicose em todos os tecidos, levando ao acúmulo intracelular e alterações do metabolismo dos carboidratos.]),
   ("E", [Paciente apresenta nefropatia isolada, porque o Complexo I é mais abundantemente expresso nos túbulos renais e a deficiência leva à perda de função tubular específica sem manifestação em outros órgãos do organismo afetado.])))

#questao-mc("20", badge-integracao,
  [Sobre a citocromo c oxidase (Complexo IV) e sua função clínica e bioquímica, é correto afirmar:],
  (("A", [O Complexo IV recebe 4 elétrons (um de cada vez, do citocromo c), consome 4 H⁺ da matriz e 1 molécula de O₂ por ciclo, produzindo 2 H₂O e bombeando 2 H⁺ adicionais por par de elétrons. Cianeto e CO bloqueiam essa enzima ligando-se ao Fe do citocromo a3 com afinidade superior ao próprio O₂.]),
   ("B", [O Complexo IV reduz O₂ a H₂O₂ (peróxido de hidrogênio) como produto principal, e a catalase secundária converte H₂O₂ em H₂O para evitar dano oxidativo às estruturas celulares em ambiente aeróbico ativo dependendo de cofator metálico. O produto final do Complexo IV é H₂O, não H₂O₂ — o peróxido de hidrogênio é um subproduto raro gerado em condições de bloqueio parcial da cadeia (rotenona, isquemia-reperfusão) e não é o resultado normal da redução completa do oxigênio.]),
   ("C", [O Complexo IV pode operar reversivelmente como produtor de O₂ a partir de H₂O em condições de baixa demanda mitocondrial, mantendo equilíbrio dinâmico entre síntese e consumo do oxigênio nos tecidos altamente vascularizados em condições aeróbicas. A reação não é reversível em condições fisiológicas — o ΔG da redução do O₂ a H₂O é muito negativo e a barreira termodinâmica para a reversão impede qualquer produção significativa de O₂ a partir de H₂O em mitocôndrias funcionais.]),
   ("D", [O Complexo IV é independente do citocromo c — recebe elétrons diretamente da CoQ no espaço intermembrana, bypass do Complexo III completo quando este está parcialmente saturado em condições de elevada demanda metabólica. O citocromo c é o transportador obrigatório entre o Complexo III e o IV — não há rota direta de CoQ ao Complexo IV em condições normais nem patológicas comprovadas em estudos experimentais com mitocôndrias isoladas.]),
   ("E", [O Complexo IV é o único complexo da cadeia respiratória que não bombeia prótons, funcionando apenas como aceptor final dos elétrons sem contribuir para a formação do gradiente eletroquímico utilizado pela ATP sintase mitocondrial. O Complexo IV bombeia 2 H⁺ adicionais por par de elétrons, contribuindo significativamente para o gradiente eletroquímico que dirige a ATP sintase em condições aeróbicas fisiológicas normais com substratos disponíveis.])))

#questao-ce("21", badge-integracao,
  [Sobre a Coenzima Q (CoQ10) e suas implicações fisiológicas e farmacológicas, julgue:],
  (("I", [CoQ é uma benzoquinona lipossolúvel que se movimenta livremente dentro da bicamada lipídica da membrana mitocondrial interna, transportando elétrons entre complexos fixos.]),
   ("II", [A CoQ recebe elétrons de pelo menos quatro fontes distintas: Complexo I (NADH), Complexo II (succinato), acil-CoA desidrogenase (β-oxidação) e glicerol-3-fosfato desidrogenase mitocondrial (lançadeira citosólica).]),
   ("III", [Deficiências severas de CoQ10 (genéticas ou adquiridas) causam quadros clínicos heterogêneos com encefalomiopatia, ataxia cerebelar e miopatia mitocondrial; suplementação oral tem suporte clínico em casos genuínos diagnosticados.]),
   ("IV", [CoQ é uma proteína periférica hidrossolúvel localizada no espaço intermembrana, e sua função é conectar o Complexo III ao Complexo IV em uma ponte mecânica direta sem intermediários moleculares na bicamada.])))

#questao-mc("22", badge-integracao,
  [Em um experimento, mitocôndrias isoladas são incubadas com glicose + ADP + Pi + O₂. Em duas condições paralelas, são adicionados: (A) malato como substrato adicional (preparado com lançadeira malato-aspartato funcional), (B) glicerol-3-fosfato como substrato adicional (preparado com lançadeira glicerol-3-fosfato funcional). Compare o saldo de ATP esperado por glicose oxidada nos dois preparados:],
  (("A", [Preparado A gera ~30 ATP/glicose e preparado B gera ~32 ATP/glicose — a lançadeira glicerol-3-fosfato é mais eficiente que a malato-aspartato em razão de utilizar Complexo II em vez de Complexo I para entrada dos elétrons na cadeia.]),
   ("B", [Os dois preparados geram saldo idêntico (~30 ATP/glicose) porque a lançadeira utilizada não influencia o ponto de entrada dos elétrons na cadeia respiratória mitocondrial nem o número total de prótons bombeados durante a oxidação completa.]),
   ("C", [Preparado A gera ~38 ATP/glicose e preparado B gera ~36 ATP/glicose — valores clássicos calculados com P/O = 3 para NADH e 2 para FADH₂ sem ajuste pelo custo de transporte de ADP/ATP/Pi pela membrana mitocondrial.]),
   ("D", [Preparado A gera ~32 ATP/glicose (lançadeira malato-aspartato preserva os elétrons como NADH matricial — P/O = 2,5 mantido); Preparado B gera ~30 ATP/glicose (lançadeira glicerol-3-fosfato entrega como FADH₂ — perde 1 ATP por NADH citosólico).]),
   ("E", [Os dois preparados não geram ATP porque a glicose precisa primeiro ser convertida a piruvato e depois acetil-CoA antes de entrar nas vias mitocondriais — sem glicólise prévia, não há oxidação completa em mitocôndrias isoladas.])))

#questao-ce("23", badge-integracao,
  [Sobre a UCP1 (proteína desacopladora 1) e o tecido adiposo marrom, julgue:],
  (("I", [UCP1 é um desacoplador fisiológico da fosforilação oxidativa que dissipa o gradiente de prótons gerando calor — função importante na termorregulação de neonatos humanos e em mamíferos hibernadores.]),
   ("II", [UCP1 está expressa no tecido adiposo branco em adultos saudáveis, sendo responsável por aproximadamente 80% do gasto basal de calor em condições de neutralidade térmica em humanos jovens.]),
   ("III", [O tecido adiposo marrom é abundante em neonatos para termogênese sem tremores; em adultos humanos, foi redescoberto em 2009 por PET-CT em pequena quantidade (principalmente na região cervical e supraclavicular).]),
   ("IV", [A ativação da UCP1 por noradrenalina (via β3-adrenérgico) leva à dissipação do gradiente mitocondrial sem síntese de ATP — toda a energia da oxidação dos ácidos graxos vira calor, gerando termogênese controlada e fisiológica.])))

#questao-mc("24", badge-integracao,
  [A análise comparativa dos inibidores antimicina A (bloqueia Complexo III) e oligomicina (bloqueia ATP sintase) sobre o consumo de O₂ em mitocôndrias isoladas demonstra que:],
  (("A", [Ambos inibidores aumentam o consumo de O₂ porque liberam os complexos respiratórios do controle por feedback negativo do gradiente eletroquímico, permitindo bombeamento máximo de prótons em todos os complexos disponíveis na membrana interna. A retroinibição do gradiente sobre os complexos é um fenômeno de controle respiratório bem documentado — qualquer bloqueio downstream (ATP sintase ou complexo IV) gera acúmulo de gradiente que retroinibe os complexos a montante.]),
   ("B", [Ambos inibidores reduzem o consumo de O₂ — antimicina A trava o fluxo no Complexo III (elétrons não chegam ao O₂); oligomicina trava a ATP sintase (gradiente cresce, retroinibe os complexos, fluxo de elétrons cessa). Em ambos os casos, sem dissipação do gradiente, a cadeia para.]),
   ("C", [Antimicina A aumenta o consumo de O₂ enquanto oligomicina diminui — a antimicina libera os elétrons do Complexo III para a CoQ em condições compensatórias, enquanto a oligomicina trava completamente a respiração em condições experimentais controladas. A antimicina A não tem rota compensatória — bloqueia o Complexo III completamente; os elétrons do Complexo II ficam presos na CoQ reduzida sem conseguir progredir para o citocromo c em direção ao oxigênio terminal.]),
   ("D", [Os dois inibidores são quimicamente idênticos e geram resposta indistinguível na oximetria de mitocôndrias isoladas — diferenciá-los exige outros métodos espectroscópicos não baseados em consumo de oxigênio observado em ensaios padrão. Os dois compostos diferem quimicamente e em alvo molecular específico — antibiótico antimicina A bloqueia o sítio Qi do Complexo III; oligomicina é macrolídeo que se liga ao F₀ da ATP sintase em sítio distinto bem caracterizado.]),
   ("E", [Antimicina A bloqueia o Complexo IV e oligomicina bloqueia o Complexo I — a oximetria diferencia os dois pela reversibilidade após adição de succinato como substrato compensatório do bloqueio induzido pela antimicina experimental. A antimicina bloqueia o Complexo III (não o IV) e oligomicina bloqueia a ATP sintase (não o Complexo I); a confusão de alvos compromete completamente a interpretação experimental dos ensaios de oximetria padrão em mitocôndrias.])))

#questao-mc("25", badge-integracao,
  [Sobre as espécies reativas de oxigênio (ROS) geradas pela cadeia respiratória em condições fisiológicas e patológicas, é correto afirmar:],
  (("A", [ROS são geradas exclusivamente em condições patológicas (isquemia-reperfusão, hipóxia) e nunca em condições fisiológicas normais — a cadeia respiratória saudável reduz completamente o O₂ a H₂O sem nenhum subproduto reativo intermediário.]),
   ("B", [ROS são geradas apenas pelo Complexo IV durante a redução final do O₂, em quantidades elevadas que justificam a presença obrigatória de catalase mitocondrial para neutralização imediata dos peróxidos formados em toda condição metabólica.]),
   ("C", [ROS são geradas continuamente em pequena quantidade nos Complexos I e III por vazamento de elétrons que reduzem O₂ a superóxido (O₂⁻); em condições normais, são neutralizadas pelas defesas antioxidantes celulares (SOD, catalase, glutationa peroxidase); em condições de bloqueio parcial (rotenona, isquemia-reperfusão), a produção aumenta drasticamente, justificando dano oxidativo.]),
   ("D", [ROS são geradas apenas no citosol pela NADPH-oxidase em fagócitos e nunca pela cadeia respiratória mitocondrial em qualquer condição experimental ou clínica relevante para a patologia humana atual e suas manifestações.]),
   ("E", [ROS são produtos finais normais da fosforilação oxidativa e são incorporadas à ATP sintase como cofatores estruturais permanentes; sua remoção destrói a função da enzima e leva à parada completa do metabolismo aeróbico mitocondrial em poucas horas.])))

#questao-mc("26", badge-aplicacao,
  [Um homem de 45 anos é trazido à emergência após inalar fumaça de incêndio em um edifício comercial. Apresenta cefaleia, taquicardia, dispneia, rebaixamento de consciência. Saturação de O₂ em oximetria de pulso = 98%. Coloração da pele sem cianose. O exame de gasometria arterial mostra pH 7,15, lactato 14 mmol/L (normal: 0,5-2,2). Sobre o mecanismo bioquímico mais provável, é correto afirmar:],
  (("A", [Trata-se de hipoxemia clássica por pneumonite química — o paciente não está oxigenando bem o sangue, e a oximetria está falsamente normal por interferência da fuligem inalada no sensor. Tratamento: suplementação de O₂ a 100% por máscara facial em alto fluxo.]),
   ("B", [Trata-se de acidose metabólica por shock hipovolêmico decorrente das queimaduras — o lactato elevado reflete hipoperfusão periférica, e o tratamento principal é volume reposição com cristaloides em alta velocidade até estabilização hemodinâmica completa do paciente politraumatizado.]),
   ("C", [Trata-se de intoxicação por cianeto (produzido na queima de plásticos e tecidos sintéticos do edifício); cianeto bloqueia o Complexo IV mitocondrial, impedindo a célula de usar o O₂ que está disponível no sangue (sat 98%); fermentação anaeróbica acumula lactato; tratamento inclui hidroxicobalamina ou nitrito de sódio + tiossulfato para sequestrar o cianeto circulante.]),
   ("D", [Trata-se de intoxicação aguda por monóxido de carbono que reverteu a curva de dissociação da hemoglobina, gerando hipóxia tecidual com saturação de O₂ aparente preservada na oximetria; tratamento: oxigênio hiperbárico em câmara para acelerar deslocamento do CO da hemoglobina circulante restante no paciente.]),
   ("E", [Trata-se de embolia gasosa por traumatismo de via aérea durante o incêndio com lesão de mucosa; o oxigênio entra no sistema venoso e causa colapso circulatório com acidose secundária à hipoperfusão sistêmica em todos os territórios vasculares afetados pelos êmbolos formados.])))

#questao-mc("27", badge-aplicacao,
  [Uma criança de 4 anos com encefalomiopatia mitocondrial é avaliada por suspeita de deficiência genética em um componente da cadeia respiratória. A biópsia muscular mostra fibras vermelhas rasgadas. Os exames bioquímicos mostram: atividade do Complexo I reduzida em 70%, atividades dos Complexos II, III, IV preservadas. Acúmulo intramuscular de lactato e piruvato em proporção aumentada. Sobre o mecanismo dessa criança e a expectativa terapêutica, é correto afirmar:],
  (("A", [A deficiência do Complexo I é compensada inteiramente pelo Complexo II que toma o lugar da entrada de elétrons do NADH na cadeia, e o paciente não apresenta sintomas clínicos relevantes nos tecidos altamente oxidativos como cérebro e músculo esquelético.]),
   ("B", [O acúmulo de lactato decorre de defeito primário da lactato desidrogenase muscular não relacionado à mitocôndria; a deficiência do Complexo I é incidental e não contribui significativamente para o quadro clínico observado nessa apresentação pediátrica complexa.]),
   ("C", [A criança tem hiperglicemia secundária à falência do consumo aeróbico de glicose, e o tratamento principal envolve restrição rigorosa de carboidratos com substituição por dieta hiperlipídica padrão tipo cetogênica em todos os pacientes pediátricos com defeitos respiratórios genéticos confirmados.]),
   ("D", [A deficiência parcial do Complexo I (70% redução) impede a oxidação eficiente do NADH; piruvato não pode ser oxidado pela via aeróbica em ritmo normal, é desviado para lactato (mantendo regeneração de NAD⁺); tecidos oxidativos com alta demanda energética sofrem (encefalomiopatia). Suplementação de CoQ10, riboflavina, tiamina pode ajudar marginalmente, mas terapia curativa não está disponível atualmente.]),
   ("E", [A criança apresenta resposta paradoxal à oxigenação suplementar, com piora dos sintomas ao aumentar a fração inspirada de O₂; a recomendação clínica é manter saturação de O₂ entre 85-90% em todos os pacientes com defeitos genéticos da cadeia respiratória mitocondrial confirmados em biópsia tecidual.])))

#questao-mc("28", badge-aplicacao,
  [Um neonato prematuro de 32 semanas em UTI neonatal mantém temperatura corporal de 36,2°C apesar de exposto a ambiente termicamente neutro. Apresenta dificuldade em manter a temperatura sem fonte externa de calor. Bioquimicamente, sobre o mecanismo termogênico fisiológico mais importante para neonatos e a explicação para a dificuldade desse paciente, é correto afirmar:],
  (("A", [Neonatos prematuros não dependem do tecido adiposo marrom porque esse tecido só se desenvolve após os 6 meses de vida pós-natal; a regulação térmica em prematuros depende exclusivamente do tremor muscular, que está ainda imaturo nessa idade gestacional.]),
   ("B", [Neonatos têm grande quantidade de tecido adiposo marrom (rico em UCP1 mitocondrial) que dissipa o gradiente de prótons sem síntese de ATP — toda a energia da oxidação dos ácidos graxos vira calor (termogênese sem tremor). Prematuros têm reserva reduzida desse tecido e por isso mais dificuldade em manter temperatura.]),
   ("C", [O mecanismo termogênico principal de neonatos é o tremor muscular, que está totalmente desenvolvido ao nascer mesmo em prematuros, mas requer reserva de glicogênio muscular elevada que prematuros ainda não acumularam durante a vida intrauterina.]),
   ("D", [A regulação térmica em neonatos depende da hibernação metabólica regulada pelo hipotálamo posterior; em prematuros essa função ainda é imatura e por isso a temperatura corporal flutua mais até a maturação completa do sistema nervoso central nas primeiras semanas pós-nascimento.]),
   ("E", [Neonatos regulam a temperatura por vasoconstrição cutânea reflexa de extrema potência (mantendo o calor central), e prematuros têm essa capacidade ainda inadequada por imaturidade da inervação simpática vascular periférica e suas conexões com o sistema nervoso autônomo central.])))

#questao-mc("29", badge-aplicacao,
  [Um pesquisador deseja distinguir experimentalmente um inibidor da ATP sintase (oligomicina) de um desacoplador (DNP) em mitocôndrias isoladas de fígado de rato. Apenas com base no consumo de O₂ medido por oximetria, sem outros marcadores, qual sequência de observações permite distinguir os dois compostos?],
  (("A", [Ambos os compostos aumentam o consumo de O₂ ao máximo, em ritmo similar e indistinguível na oximetria; a distinção requer dosagem direta de ATP gerado, não acessível em oximetria simples sem ensaios adicionais.]),
   ("B", [Ambos os compostos reduzem o consumo de O₂ a níveis basais idênticos; a distinção entre eles requer análise da temperatura do meio de incubação (DNP gera calor, oligomicina não), feita com termopar microeletrônico padrão de laboratório.]),
   ("C", [Após oligomicina, consumo de O₂ cai (cadeia trava por retroinibição do gradiente sobre os complexos); após DNP, consumo de O₂ aumenta (cadeia acelera tentando recompor gradiente que vaza). Se oligomicina for adicionada primeiro e depois DNP, o consumo de O₂ se recupera ao máximo — confirma DNP como desacoplador.]),
   ("D", [Oligomicina aumenta o consumo de O₂ porque libera os complexos respiratórios da retroinibição do gradiente, enquanto DNP reduz o consumo porque dissipa o gradiente que dirige os complexos a operarem em ritmo máximo na cadeia respiratória ativada.]),
   ("E", [Apenas a adição prévia de cianeto seguida de oligomicina permite distinguir os dois compostos, porque cianeto bloqueia o Complexo IV e remove a variável O₂ da equação experimental; mensurar apenas síntese de ATP em pH fixo é insuficiente para diferenciá-los corretamente.])))

#questao-mc("30", badge-aplicacao,
  [Um atleta de endurance ingere CoQ10 oral diariamente como suplemento esportivo após ler artigo afirmando que melhora o desempenho aeróbico em maratonas. Sobre as bases bioquímicas e a evidência clínica do uso de CoQ10 oral como ergogênico, é correto afirmar:],
  (("A", [CoQ10 oral é hub central da cadeia respiratória (recebe elétrons de I, II, β-oxidação, glicerol-3-fosfato desidrogenase). Em pessoas saudáveis, a CoQ endógena é regulada e suficiente — suplementação não tem benefício comprovado no desempenho. A indicação clínica genuína é em deficiências severas (genéticas ou induzidas por estatinas em casos selecionados), onde o défice é mensurável.]),
   ("B", [CoQ10 oral é absorvida em quantidades não significativas no intestino delgado em pessoas saudáveis, mas em atletas de endurance a permeabilidade intestinal aumenta dramaticamente durante o esforço, permitindo absorção elevada e benefício comprovado em maratonas em meta-análises recentes da literatura.]),
   ("C", [CoQ10 funciona como um desacoplador parcial da cadeia respiratória em altas doses, aumentando o gasto basal e o consumo de O₂ por unidade de massa muscular, justificando o uso por atletas que buscam emagrecimento associado ao desempenho aeróbico durante a temporada de treinos pré-competição esportiva.]),
   ("D", [CoQ10 substitui a coenzima Q endógena de forma competitiva, deslocando as moléculas antigas e renovando o pool da cadeia respiratória — esse turnover acelerado é o mecanismo principal da melhora de desempenho descrita em atletas e justifica o uso preventivo a partir dos 25 anos de idade na prática.]),
   ("E", [CoQ10 estimula a síntese de novas mitocôndrias via PGC-1α em condições de treino aeróbico, e essa biogênese mitocondrial é o mecanismo principal do ganho de desempenho — daí a recomendação atual de uso por todos os atletas profissionais de modalidades de resistência.])))
