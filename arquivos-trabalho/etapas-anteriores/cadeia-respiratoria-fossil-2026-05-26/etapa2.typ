#import "../typst-template/nebli_v2_apostila.typ": *

#questao-mc("01", badge-consolidacao,
  [Sobre a lógica termodinâmica que justifica a existência da cadeia respiratória, é correto afirmar:],
  (("A", [A oxidação completa da glicose libera energia pequena demais para ser capturada em um único passo enzimático, e a cadeia respiratória amplifica essa energia por efeito cascata entre complexos.]),
   ("B", [A cadeia respiratória existe para impedir que o oxigênio reaja diretamente com a glicose dentro da célula, evitando dano oxidativo nas membranas mitocondriais durante o metabolismo aeróbico ativo.]),
   ("C", [A oxidação da glicose libera 2.870 kJ/mol — grande demais para captura em uma reação só; a cadeia fraciona em degraus de ~20 kJ/mol, escala que enzimas aproveitam como bombeamento de prótons.]),
   ("D", [O fracionamento da oxidação serve para gerar ATP em quantidade proporcional aos carbonos da glicose, mantendo razão estequiométrica fixa entre substrato e moeda energética nas condições metabólicas usuais.]),
   ("E", [A cadeia respiratória existe porque a oxidação direta pelo O₂ seria cineticamente lenta demais em meio aquoso; a cadeia acelera a reação por catálise enzimática em fatores de ordem 10⁶ habituais.])))

#questao-ce("02", badge-consolidacao,
  [Sobre os componentes anatômicos da mitocôndria e da cadeia respiratória, julgue os itens:],
  (("I", [A cadeia respiratória está cravada na membrana interna mitocondrial, que é altamente impermeável a íons e prótons em condições fisiológicas usuais.]),
   ("II", [A membrana externa contém porinas que tornam o espaço intermembrana quimicamente equivalente ao citosol em pequenas moléculas e íons.]),
   ("III", [A matriz mitocondrial contém as enzimas solúveis do ciclo de Krebs, β-oxidação, DNA mitocondrial e ribossomos próprios em razão da origem endossimbiótica.]),
   ("IV", [Coenzima Q e citocromo c são proteínas integrais grandes equivalentes em estrutura aos 4 complexos fixos da cadeia respiratória mitocondrial.])))

#questao-mc("03", badge-consolidacao,
  [Os elétrons fluem na cadeia respiratória do par redox com potencial mais negativo para o par com potencial mais positivo. Considerando NAD⁺/NADH (E' = -0,32 V) e O₂/H₂O (E' = +0,82 V):],
  (("A", [Os elétrons fluem do par O₂/H₂O para o par NAD⁺/NADH porque o oxigênio funciona como doador mais forte de elétrons em condições padrão bioquímicas mitocondriais.]),
   ("B", [O ΔE total da cadeia é negativo (cerca de -1,14 V), refletindo transferência contra o gradiente termodinâmico natural dos pares redox envolvidos em condições padrão.]),
   ("C", [O ΔG é positivo para transferência de NADH a O₂, exigindo input energético externo via hidrólise de ATP em cada etapa da cadeia respiratória mitocondrial fisiológica.]),
   ("D", [O ΔG é cerca de -220 kJ/mol para transferência de 2 elétrons do NADH ao O₂, calculado por ΔG = -nFΔE' (n=2; F=96,5 kJ/V·mol; ΔE'=+1,14 V) — fartamente suficiente para múltiplos ATPs.]),
   ("E", [O ΔG depende apenas do número de prótons bombeados pelos complexos e não da diferença de potencial redox entre os pares envolvidos nas transferências eletrônicas mitocondriais.])))

#questao-mc("04", badge-consolidacao,
  [Sobre a entrada dos elétrons do NADH e do FADH₂ na cadeia respiratória, é correto afirmar:],
  (("A", [Tanto NADH quanto FADH₂ entram pelo Complexo I, mas com grupos prostéticos diferentes (FMN para NADH, FAD para FADH₂) durante a transferência inicial dos elétrons à CoQ.]),
   ("B", [NADH entra pelo Complexo I via FMN e centros Fe-S (bombeando 4 H⁺); FADH₂ entra pelo Complexo II (succinato desidrogenase) sem bombear prótons, gerando rendimento de ATP menor no saldo final.]),
   ("C", [FADH₂ entra pelo Complexo I e NADH entra pelo Complexo II, refletindo a sequência inversa em que aparecem no Krebs e na β-oxidação dos ácidos graxos durante a oxidação aeróbica.]),
   ("D", [Ambos NADH e FADH₂ entram diretamente na CoQ sem passar pelos Complexos I ou II, em redução direta da benzoquinona lipossolúvel pelos equivalentes redutores celulares.]),
   ("E", [NADH e FADH₂ entram pelo Complexo III, ponto comum de convergência dos elétrons antes da passagem pelo citocromo c em direção ao Complexo IV citocromo oxidase mitocondrial.])))

#questao-ce("05", badge-consolidacao,
  [Sobre o Complexo II e a succinato desidrogenase, julgue:],
  (("I", [O Complexo II é a única enzima do ciclo de Krebs cravada na membrana mitocondrial interna; as demais enzimas do Krebs são solúveis na matriz.]),
   ("II", [O Complexo II bombeia 2 prótons por par de elétrons da matriz para o espaço intermembrana, contribuindo para o gradiente eletroquímico que dirige a ATP sintase.]),
   ("III", [Os elétrons do FADH₂ gerado dentro do Complexo II são transferidos diretamente à Coenzima Q sem envolvimento do Complexo I ou outros carregadores intermediários.]),
   ("IV", [O succinato é o substrato do Complexo II e é convertido a fumarato durante a transferência dos elétrons — essa é simultaneamente uma reação do ciclo de Krebs.])))

#questao-mc("06", badge-consolidacao,
  [O ciclo Q do Complexo III resolve uma incompatibilidade estrutural específica da cadeia respiratória. Qual é essa incompatibilidade?],
  (("A", [CoQ carrega 2 elétrons (CoQH₂ → CoQ) mas cit c carrega só 1 por vez (Fe³⁺ ↔ Fe²⁺); o ciclo Q bifurca os 2 elétrons da CoQ, entregando 1 ao cit c e desviando o outro de volta para outra CoQ.]),
   ("B", [Cit c só opera em meio lipídico enquanto CoQ é hidrossolúvel; o ciclo Q transforma CoQ em forma compatível com a passagem para o cit c hidrossolúvel localizado na matriz mitocondrial interna.]),
   ("C", [A diferença de potencial entre CoQ e cit c é negativa, impedindo o fluxo espontâneo dos elétrons; o ciclo Q inverte essa polaridade via bombeamento ativo de elétrons contra o gradiente termodinâmico natural.]),
   ("D", [Os centros Fe-S do Complexo III só aceitam elétrons aos pares enquanto a CoQ doa individualmente; o ciclo Q acumula elétrons da CoQ até formar pares antes da transferência aos centros Fe-S do complexo.]),
   ("E", [A CoQ precisa ser regenerada por dois ciclos consecutivos de Krebs, e o Complexo III coordena essa regeneração via ciclo Q como mecanismo de feedback metabólico em condições aeróbicas elevadas.])))

#questao-mc("07", badge-consolidacao,
  [A teoria quimiosmótica proposta por Peter Mitchell em 1961 (Nobel de 1978) explica o acoplamento entre transporte de elétrons e síntese de ATP através de:],
  (("A", [Uma molécula intermediária de alta energia (X~P) que carrega a energia da cadeia respiratória diretamente para o sítio catalítico da ATP sintase, fechando o ciclo da fosforilação oxidativa numa única etapa.]),
   ("B", [Uma proteína transportadora que liga o ADP gerado pela hidrólise do ATP ao sítio do Complexo IV, sincronizando consumo de oxigênio com regeneração de ATP em todos os tecidos animais aerobicamente acoplados.]),
   ("C", [Um gradiente de carbonato/bicarbonato gerado pela acidificação local do citosol durante trabalho metabólico, atuando como tampão fisiológico que estabiliza pH durante oxidação na matriz mitocondrial ativa.]),
   ("D", [Uma reação enzimática acoplada que catalisa simultaneamente a oxidação do NADH e a fosforilação do ADP usando a mesma energia em uma única etapa catalítica de transferência de fosfato.]),
   ("E", [Um gradiente eletroquímico de prótons (força próton-motriz) através da membrana mitocondrial interna, gerado pelo bombeamento dos complexos e consumido pela ATP sintase como turbina molecular rotativa.])))

#questao-ce("08", badge-consolidacao,
  [Sobre a ATP sintase F₀F₁ e o mecanismo binding change descoberto por Paul Boyer (Nobel de 1997), julgue:],
  (("I", [A subunidade F₀ (em referência à oligomicina) é um canal de prótons embebido na membrana mitocondrial interna em forma de roda rotatória.]),
   ("II", [A subunidade F₁ saliente para a matriz tem 3 sítios catalíticos que passam por 3 conformações sequenciais: Loose (liga ADP+Pi), Tight (forma ATP) e Open (libera ATP).]),
   ("III", [A energia da rotação dos prótons é usada para *formar* a ligação fosfoanidrido do ATP no sítio catalítico, com gasto energético direto na ligação química, não na liberação do produto.]),
   ("IV", [Oligomicina liga-se à subunidade F₀ impedindo a rotação, e em mitocôndrias funcionais a ATP sintase opera no sentido de síntese (não hidrólise) de ATP.])))

#questao-mc("09", badge-consolidacao,
  [A razão P/O (fosforilações por átomo de oxigênio reduzido) atualmente aceita para NADH e FADH₂ na cadeia respiratória humana é:],
  (("A", [NADH: P/O = 3,0 (clássico); FADH₂: P/O = 2,0 (clássico) — valores que rendem o saldo total de 38 ATP por glicose oxidada em condições aeróbicas plenas mitocondriais usuais.]),
   ("B", [NADH: P/O = 2,5; FADH₂: P/O = 1,5 — valores que rendem saldo de 30-32 ATP por glicose, dependendo da lançadeira de NADH citosólico operante no tecido envolvido.]),
   ("C", [NADH e FADH₂ têm P/O idênticos (cerca de 1,5) porque a cadeia respiratória gera quantidade fixa de ATP por par de elétrons, independente do ponto de entrada na cadeia mitocondrial.]),
   ("D", [NADH tem P/O = 4,0 e FADH₂ tem P/O = 2,5, valores que justificam o saldo elevado da β-oxidação dos ácidos graxos quando comparado à oxidação aeróbica da glicose pelo Krebs.]),
   ("E", [P/O depende exclusivamente do tecido analisado e varia de 1 a 5 sem relação direta com o ponto de entrada do equivalente redutor na cadeia respiratória mitocondrial humana.])))

#questao-mc("10", badge-consolidacao,
  [Sobre a distinção fundamental entre inibidores e desacopladores da fosforilação oxidativa, é correto afirmar:],
  (("A", [Inibidores aceleram o consumo de O₂ porque liberam o gradiente acumulado, enquanto desacopladores travam o O₂ por feedback negativo do gradiente sobre os complexos respiratórios mitocondriais ativos.]),
   ("B", [Inibidores e desacopladores produzem efeitos clínicos idênticos porque ambos bloqueiam a síntese de ATP independentemente do mecanismo molecular subjacente envolvido em cada caso clínico.]),
   ("C", [Inibidores agem só na ATP sintase (F₀ ou F₁), enquanto desacopladores agem exclusivamente nos complexos respiratórios I a IV bloqueando o transporte de elétrons em pontos específicos.]),
   ("D", [Inibidores travam o transporte de elétrons (consumo de O₂ cai a zero); desacopladores deixam a cadeia rodar mas furam a membrana para H⁺ — consumo de O₂ aumenta ao máximo, mas toda energia vira calor.]),
   ("E", [Inibidores são sempre tóxicos letais enquanto desacopladores são sempre fisiológicos mantidos sob controle pela célula via mecanismos de feedback negativo regulado por morfógenos celulares.])))

#questao-mc("11", badge-integracao,
  [Em oximetria com mitocôndrias isoladas em meio com succinato, é adicionado rotenona em quantidade suficiente para bloquear inteiramente o Complexo I. Sobre o consumo de O₂ resultante, espera-se:],
  (("A", [Queda imediata e completa do consumo de O₂ a zero, pois rotenona bloqueia o ponto de entrada exclusivo de todos os elétrons na cadeia respiratória mitocondrial em qualquer condição experimental.]),
   ("B", [Aumento explosivo do consumo de O₂ por desvio dos elétrons do Complexo I para o II, gerando rota compensatória de oxidação acelerada do succinato em meio acidificado experimental.]),
   ("C", [Consumo de O₂ preservado próximo ao normal — elétrons do succinato entram pelo Complexo II (independente do Complexo I) e seguem normalmente CoQ → III → cit c → IV → O₂.]),
   ("D", [Consumo de O₂ reduzido em proporção exata ao número de moléculas de rotenona ligadas, sem dependência da disponibilidade de outros substratos doadores de elétrons no meio experimental utilizado.]),
   ("E", [Inversão da direção do fluxo de elétrons na cadeia, com geração de espécies reativas de oxigênio em quantidade tão elevada que provoca lise imediata das mitocôndrias do preparado utilizado.])))

#questao-ce("12", badge-integracao,
  [Em mitocôndria isolada são feitas adições sequenciais: (1) ADP em excesso, (2) oligomicina, (3) DNP. Sobre consumo de O₂ em cada momento:],
  (("I", [Após ADP em excesso, consumo de O₂ aumenta — ADP é o sinal que faz a ATP sintase girar, dissipando o gradiente e liberando os complexos para bombear novamente (estado 3).]),
   ("II", [Após oligomicina (que segue o ADP), consumo de O₂ aumenta ainda mais porque ela libera os complexos respiratórios do controle por gradiente, permitindo bombeamento máximo em todos os complexos.]),
   ("III", [Após DNP (que segue oligomicina), consumo de O₂ aumenta porque DNP perfura a membrana para H⁺, dissipa o gradiente e remove a retroinibição imposta pela oligomicina, deixando a cadeia acelerar.]),
   ("IV", [Em qualquer dessas três condições há síntese normal de ATP, garantida pela presença de fosfato inorgânico e ADP no meio, independente do estado do gradiente eletroquímico mitocondrial atual.])))

#questao-mc("13", badge-integracao,
  [Paciente intoxicado com cianeto chega à emergência com sangue venoso vermelho-cereja, taquicardia, taquipneia, rebaixamento de consciência. O mecanismo bioquímico que explica essa apresentação é:],
  (("A", [Cianeto bloqueia o Complexo IV (cit oxidase), impedindo a redução do O₂ a H₂O; O₂ fica disponível no sangue (não consumido) mas a célula não pode usá-lo — hipóxia histotóxica letal pela falência ATP-dependente sistêmica.]),
   ("B", [Cianeto liga-se à hemoglobina com afinidade maior que O₂, formando cianometemoglobina que não transporta oxigênio aos tecidos periféricos, gerando hipóxia hipoxêmica similar à intoxicação por monóxido de carbono não tratada.]),
   ("C", [Cianeto inibe o Complexo I por mecanismo similar à rotenona, parando a cadeia no ponto inicial e levando ao acúmulo de NADH não oxidado que deprime o Krebs e o metabolismo aeróbico progressivamente.]),
   ("D", [Cianeto é desacoplador que funciona como o DNP, dissipando o gradiente e produzindo hipertermia letal por dissipação de energia em calor sem geração de ATP nos tecidos periféricos do intoxicado.]),
   ("E", [Cianeto causa hemólise maciça por oxidação direta da hemoglobina a metemoglobina em todas as hemácias circulantes, gerando anemia hemolítica aguda como mecanismo principal da letalidade observada em intoxicações.])))

#questao-mc("14", badge-integracao,
  [Musculista compra DNP no mercado ilegal para "secar" antes de competição. Após overdose, chega à emergência com hipertermia (41,8°C), taquicardia, sudorese profusa, óbito em 6h apesar de medidas suportivas. O mecanismo da letalidade do DNP é:],
  (("A", [DNP bloqueia o Complexo IV impedindo consumo de O₂; a hipertermia decorre de elevação compensatória do metabolismo basal por estímulo simpático intenso secundário à hipóxia tissular instalada em todos os órgãos.]),
   ("B", [DNP inibe a glicose-6-fosfatase hepática gerando hipoglicemia profunda e elevação de cetonas; a hipertermia é consequência de cetose com produção exagerada de calor pelo tecido adiposo marrom em hibernadores adultos humanos.]),
   ("C", [DNP é inibidor da ATP sintase semelhante à oligomicina, parando a cadeia respiratória e gerando hipertermia paradoxal por elevação do gasto basal compensatório do tecido muscular esquelético em condições anaeróbicas extremas.]),
   ("D", [DNP é desacoplador lipossolúvel que perfura a membrana mitocondrial interna para H⁺, dissipando o gradiente; cadeia acelera tentando recompor, O₂ consumo máximo, mas toda energia vira calor → hipertermia letal.]),
   ("E", [DNP é precursor de óxido nítrico endógeno em altas concentrações; a hipertermia decorre de vasodilatação maciça com choque distributivo descompensado e óbito por colapso circulatório periférico em horas após ingesta.])))

#questao-ce("15", badge-integracao,
  [Sobre as lançadeiras mitocondriais do NADH citosólico e o saldo final de ATP por glicose, julgue:],
  (("I", [A membrana mitocondrial interna é impermeável ao NADH citosólico — as lançadeiras transferem os equivalentes redutores via intermediários que atravessam a membrana, não o NADH em si.]),
   ("II", [A lançadeira malato-aspartato (predominante no fígado, rim, coração) entrega os elétrons como FADH₂ matricial, rendendo 1,5 ATP por NADH citosólico ao final da oxidação completa.]),
   ("III", [A lançadeira glicerol-3-fosfato (predominante no músculo esquelético e cérebro) entrega os elétrons como FADH₂ via Complexo II, rendendo 1,5 ATP por NADH citosólico (perda de 1 ATP por molécula).]),
   ("IV", [O saldo de ATP por glicose varia de 30 a 32 dependendo da lançadeira operante no tecido — malato-aspartato resulta em saldo maior (~32) e glicerol-3-fosfato em saldo menor (~30).])))

#questao-mc("16", badge-integracao,
  [Em experimento, mitocôndrias com succinato + ADP + Pi + O₂ apresentam consumo de O₂ acelerado e síntese de ATP. Em seguida adiciona-se antibiótico que se liga ao F₀ da ATP sintase. O efeito esperado sobre consumo de O₂ é:],
  (("A", [Aumento do consumo, porque a ligação ao F₀ libera os prótons para vazarem livremente pela membrana, dissipando o gradiente e permitindo aceleração contínua da cadeia em busca de recomposição energética.]),
   ("B", [Queda do consumo — oligomicina bloqueia a passagem de prótons pela ATP sintase; o gradiente cresce e retroinibe os complexos; sem dissipação, a cadeia para. Consumo de O₂ cai a níveis basais ou abaixo.]),
   ("C", [Inversão da direção do fluxo da ATP sintase, com hidrólise de ATP residual sendo usada para bombear prótons de volta para o espaço intermembrana até esgotamento das reservas mitocondriais existentes.]),
   ("D", [Manutenção do consumo em ritmo normal porque a inibição da ATP sintase não interfere com o transporte de elétrons na cadeia respiratória, que opera independentemente da síntese de ATP em qualquer condição.]),
   ("E", [Liberação súbita de íons cálcio do retículo sarcoplasmático mitocondrial com contração espasmódica dos sarcômeros adjacentes e consumo descontrolado de O₂ celular em todos os tecidos preparados em ambiente experimental.])))

#questao-ce("17", badge-integracao,
  [Sobre a relação entre cadeia respiratória e ciclo de Krebs, julgue:],
  (("I", [O Complexo II (succinato desidrogenase) é a única enzima do Krebs cravada na membrana mitocondrial interna; as demais enzimas do Krebs são solúveis na matriz mitocondrial.]),
   ("II", [Os equivalentes redutores do Krebs (NADH e FADH₂) são usados pela cadeia respiratória — o Krebs depende da cadeia para regenerar NAD⁺ e FAD oxidados, mantendo o fluxo metabólico aeróbico contínuo.]),
   ("III", [Em bloqueio total da cadeia (ex.: cianeto), o Krebs também para porque NADH e FADH₂ acumulam-se sem oxidação; a produção de ATP de fonte aeróbica é interrompida nessa situação metabólica.]),
   ("IV", [O GTP gerado no Krebs (passo succinil-CoA → succinato) depende diretamente da cadeia respiratória para sua síntese e não é produzido em bloqueio dos complexos respiratórios I a IV usuais.])))

#questao-mc("18", badge-integracao,
  [A teoria quimiosmótica de Mitchell foi inicialmente recebida com ceticismo porque contrariava o modelo dominante de intermediário químico de alta energia. Sobre as evidências experimentais que sustentaram a teoria:],
  (("A", [Mitchell isolou e caracterizou quimicamente uma molécula intermediária (X~P) ligando a cadeia respiratória à ATP sintase via ligação fosfoanidrido de alta energia armazenada em grupo lateral de proteína matricial.]),
   ("B", [A teoria foi validada quando mitocôndrias inteiras se mostraram desnecessárias — mitocondriossomos solúveis em meio aquoso geravam ATP a partir de NADH sem qualquer membrana lipídica intacta na preparação.]),
   ("C", [Bactérias mutantes incapazes de gerar gradiente eletroquímico mostraram-se ainda capazes de sintetizar ATP em ritmo elevado em condições anaeróbicas com substratos puramente glicolíticos disponíveis no meio.]),
   ("D", [A descoberta da fosforilação a nível de substrato no Krebs e na glicólise tornou a teoria quimiosmótica desnecessária, demonstrando que toda síntese aeróbica de ATP poderia ser explicada por reações solúveis.]),
   ("E", [Mitchell mostrou que mitocôndrias com membrana íntegra geravam gradiente de prótons mensurável durante respiração, e esse gradiente era requisito para síntese de ATP — quando a membrana era danificada, a síntese cessava.])))

#questao-mc("19", badge-integracao,
  [Considere paciente com mutação em gene mitocondrial codificador de subunidade do Complexo I (deficiência parcial — atividade residual de ~30%). A apresentação clínica esperada e o mecanismo bioquímico são:],
  (("A", [Paciente é assintomático porque o Krebs gera FADH₂ via succinato desidrogenase do Complexo II como rota compensatória completa, mantendo o fluxo metabólico aeróbico inalterado em todos os tecidos humanos.]),
   ("B", [Paciente apresenta hemólise crônica leve com anemia compensada por aumento de produção medular; quadro decorre de fragilidade aumentada das hemácias por sobrecarga oxidativa secundária à deficiência do Complexo I.]),
   ("C", [Paciente apresenta sintomas em tecidos de alta demanda energética (SNC, músculo esquelético, retina) — encefalomiopatia, ataxia, miopatia. NADH acumula, geração de ATP cai abaixo do necessário em tecidos oxidativos.]),
   ("D", [Paciente apresenta intolerância à glicose com hiperglicemia pós-prandial, porque a deficiência do Complexo I impede o consumo aeróbico da glicose em todos os tecidos, levando ao acúmulo intracelular e alterações dos carboidratos.]),
   ("E", [Paciente apresenta nefropatia isolada, porque o Complexo I é mais abundantemente expresso nos túbulos renais e a deficiência leva à perda de função tubular específica sem manifestação em outros órgãos do organismo afetado.])))

#questao-mc("20", badge-integracao,
  [Sobre a citocromo c oxidase (Complexo IV) e sua função, é correto afirmar:],
  (("A", [O Complexo IV recebe 4 elétrons (um de cada vez do cit c), consome 4 H⁺ da matriz e 1 O₂ por ciclo, produzindo 2 H₂O e bombeando 2 H⁺ adicionais por par de elétrons; cianeto e CO bloqueiam essa enzima ligando-se ao Fe do cit a3.]),
   ("B", [O Complexo IV reduz O₂ a H₂O₂ (peróxido) como produto principal, e a catalase secundária converte H₂O₂ em H₂O para evitar dano oxidativo nas estruturas celulares em ambiente aeróbico ativo mitocondrial usual.]),
   ("C", [O Complexo IV pode operar reversivelmente como produtor de O₂ a partir de H₂O em condições de baixa demanda mitocondrial, mantendo equilíbrio dinâmico entre síntese e consumo de O₂ em tecidos altamente vascularizados.]),
   ("D", [O Complexo IV é independente do citocromo c — recebe elétrons diretamente da CoQ no espaço intermembrana, bypass do Complexo III completo quando este está parcialmente saturado em condições de elevada demanda metabólica.]),
   ("E", [O Complexo IV é o único complexo da cadeia que não bombeia prótons, funcionando apenas como aceptor final dos elétrons sem contribuir para a formação do gradiente eletroquímico utilizado pela ATP sintase mitocondrial.])))

#questao-ce("21", badge-integracao,
  [Sobre a Coenzima Q (CoQ10) e suas implicações fisiológicas e farmacológicas, julgue:],
  (("I", [CoQ é benzoquinona lipossolúvel que se movimenta livremente dentro da bicamada da membrana mitocondrial interna, transportando elétrons entre complexos fixos.]),
   ("II", [CoQ recebe elétrons de pelo menos quatro fontes: Complexo I (NADH), Complexo II (succinato), acil-CoA desidrogenase (β-oxidação) e glicerol-3-fosfato desidrogenase mitocondrial (lançadeira citosólica do NADH).]),
   ("III", [Deficiências severas de CoQ10 (genéticas ou adquiridas) causam quadros heterogêneos com encefalomiopatia, ataxia cerebelar e miopatia mitocondrial; suplementação oral tem suporte clínico em casos genuínos diagnosticados.]),
   ("IV", [CoQ é proteína periférica hidrossolúvel localizada no espaço intermembrana e conecta o Complexo III ao Complexo IV em ponte mecânica direta sem intermediários moleculares na bicamada.])))

#questao-mc("22", badge-integracao,
  [Em experimento com glicose + ADP + Pi + O₂ em duas condições: (A) malato como substrato com lançadeira malato-aspartato funcional; (B) glicerol-3-fosfato como substrato com lançadeira glicerol-3-fosfato funcional. Compare o saldo de ATP esperado:],
  (("A", [Preparado A gera ~30 ATP/glicose e preparado B gera ~32 ATP/glicose — a lançadeira glicerol-3-fosfato é mais eficiente que a malato-aspartato por usar o Complexo II em vez do I para entrada dos elétrons na cadeia.]),
   ("B", [Os dois preparados geram saldo idêntico (~30 ATP/glicose) porque a lançadeira não influencia o ponto de entrada dos elétrons na cadeia respiratória nem o número total de prótons bombeados durante a oxidação completa.]),
   ("C", [Preparado A gera ~38 ATP/glicose e preparado B gera ~36 ATP/glicose — valores clássicos calculados com P/O = 3 para NADH e 2 para FADH₂ sem ajuste pelo custo de transporte de ADP/ATP/Pi mitocondrial.]),
   ("D", [Preparado A gera ~32 ATP/glicose (lançadeira MA preserva elétrons como NADH matricial — P/O = 2,5 mantido); Preparado B gera ~30 ATP/glicose (lançadeira G3P entrega como FADH₂ — perde 1 ATP por NADH citosólico).]),
   ("E", [Os dois preparados não geram ATP porque a glicose precisa primeiro ser convertida a piruvato e depois acetil-CoA antes de entrar nas vias mitocondriais — sem glicólise prévia, não há oxidação completa em isoladas.])))

#questao-ce("23", badge-integracao,
  [Sobre a UCP1 (proteína desacopladora 1) e o tecido adiposo marrom, julgue:],
  (("I", [UCP1 é desacoplador fisiológico da fosforilação oxidativa que dissipa o gradiente de prótons gerando calor — função importante na termorregulação de neonatos humanos e em mamíferos hibernadores adultos.]),
   ("II", [UCP1 está expressa no tecido adiposo branco em adultos saudáveis e é responsável por aproximadamente 80% do gasto basal de calor em condições de neutralidade térmica em humanos jovens saudáveis.]),
   ("III", [O tecido adiposo marrom é abundante em neonatos para termogênese sem tremores; em adultos foi redescoberto em 2009 por PET-CT em pequena quantidade (principalmente cervical e supraclavicular).]),
   ("IV", [A ativação da UCP1 por noradrenalina (via β3-adrenérgico) leva à dissipação do gradiente mitocondrial sem síntese de ATP — toda energia da oxidação dos ácidos graxos vira calor, gerando termogênese controlada fisiológica.])))

#questao-mc("24", badge-integracao,
  [Compare experimentalmente antimicina A (bloqueia Complexo III) e oligomicina (bloqueia ATP sintase) quanto ao efeito sobre consumo de O₂ em mitocôndrias isoladas:],
  (("A", [Ambos os inibidores aumentam o consumo de O₂ porque liberam os complexos respiratórios do feedback negativo do gradiente eletroquímico, permitindo bombeamento máximo de prótons em todos os complexos disponíveis.]),
   ("B", [Ambos reduzem consumo de O₂ — antimicina A trava o fluxo no Complexo III (elétrons não chegam ao O₂); oligomicina trava a ATP sintase (gradiente cresce, retroinibe os complexos, fluxo cessa). Sem dissipação, a cadeia para.]),
   ("C", [Antimicina A aumenta consumo de O₂ enquanto oligomicina diminui — a antimicina libera elétrons do Complexo III para a CoQ em condições compensatórias, enquanto oligomicina trava completamente a respiração em condições padrão.]),
   ("D", [Os dois inibidores são quimicamente idênticos e geram resposta indistinguível na oximetria de mitocôndrias isoladas — diferenciá-los exige outros métodos espectroscópicos não baseados em consumo de oxigênio observado em ensaios.]),
   ("E", [Antimicina A bloqueia o Complexo IV e oligomicina bloqueia o Complexo I — a oximetria diferencia os dois pela reversibilidade após adição de succinato como substrato compensatório do bloqueio induzido pela antimicina experimental.])))

#questao-mc("25", badge-integracao,
  [Sobre as espécies reativas de oxigênio (ROS) geradas pela cadeia respiratória em condições fisiológicas e patológicas, é correto afirmar:],
  (("A", [ROS são geradas exclusivamente em condições patológicas (isquemia-reperfusão, hipóxia) e nunca em condições fisiológicas normais — a cadeia respiratória saudável reduz completamente o O₂ a H₂O sem qualquer subproduto reativo.]),
   ("B", [ROS são geradas apenas pelo Complexo IV durante a redução final do O₂, em quantidades elevadas que justificam a presença obrigatória de catalase mitocondrial para neutralização imediata dos peróxidos formados em toda condição.]),
   ("C", [ROS são geradas apenas no citosol pela NADPH-oxidase em fagócitos e nunca pela cadeia respiratória mitocondrial em qualquer condição experimental ou clínica relevante para a patologia humana atual e suas manifestações.]),
   ("D", [ROS são produtos finais normais da fosforilação oxidativa incorporadas à ATP sintase como cofatores estruturais permanentes; sua remoção destrói a função da enzima e leva à parada do metabolismo aeróbico mitocondrial em horas.]),
   ("E", [ROS são geradas continuamente em pequena quantidade nos Complexos I e III por vazamento de elétrons reduzindo O₂ a superóxido; em condições normais, são neutralizadas pelas defesas antioxidantes (SOD, catalase, glutationa peroxidase).])))

#questao-mc("26", badge-aplicacao,
  [Homem de 45 anos é trazido após inalar fumaça de incêndio em edifício comercial. Apresenta cefaleia, taquicardia, dispneia, rebaixamento de consciência. Saturação de O₂ por oximetria = 98%, sem cianose. Gasometria: pH 7,15, lactato 14 mmol/L. Sobre o mecanismo bioquímico mais provável:],
  (("A", [Hipoxemia clássica por pneumonite química — paciente não está oxigenando bem o sangue, e a oximetria está falsamente normal por interferência da fuligem inalada no sensor. Tratamento: suplementação de O₂ a 100% por máscara facial em alto fluxo.]),
   ("B", [Acidose metabólica por choque hipovolêmico decorrente das queimaduras — o lactato elevado reflete hipoperfusão periférica, e o tratamento principal é volume reposição com cristaloides até estabilização hemodinâmica completa do paciente politraumatizado.]),
   ("C", [Intoxicação por cianeto (produzido na queima de plásticos do edifício); cianeto bloqueia o Complexo IV, impedindo a célula de usar o O₂ disponível no sangue (sat 98%); fermentação anaeróbica acumula lactato; tratamento: hidroxicobalamina ou nitrito + tiossulfato.]),
   ("D", [Intoxicação por monóxido de carbono que reverteu a curva de dissociação da hemoglobina, gerando hipóxia tecidual com saturação de O₂ aparente preservada na oximetria; tratamento: oxigênio hiperbárico em câmara para acelerar deslocamento do CO da hemoglobina circulante.]),
   ("E", [Embolia gasosa por traumatismo de via aérea durante o incêndio com lesão de mucosa; o oxigênio entra no sistema venoso e causa colapso circulatório com acidose secundária à hipoperfusão sistêmica em todos os territórios vasculares afetados pelos êmbolos.])))

#questao-mc("27", badge-aplicacao,
  [Criança de 4 anos com encefalomiopatia mitocondrial. Biópsia muscular: fibras vermelhas rasgadas. Bioquímica: atividade Complexo I reduzida 70%, II/III/IV preservados; lactato e piruvato musculares acumulados. Sobre o mecanismo e expectativa terapêutica:],
  (("A", [A deficiência do Complexo I é compensada inteiramente pelo Complexo II que toma o lugar da entrada de elétrons do NADH na cadeia, e a criança não apresenta sintomas clínicos relevantes nos tecidos altamente oxidativos como cérebro e músculo esquelético.]),
   ("B", [O acúmulo de lactato decorre de defeito primário da lactato desidrogenase muscular não relacionado à mitocôndria; a deficiência do Complexo I é incidental e não contribui significativamente para o quadro clínico observado nessa apresentação pediátrica complexa.]),
   ("C", [A criança tem hiperglicemia secundária à falência do consumo aeróbico de glicose, e o tratamento principal envolve restrição rigorosa de carboidratos com substituição por dieta hiperlipídica padrão tipo cetogênica em todos os pacientes pediátricos com defeitos respiratórios genéticos confirmados.]),
   ("D", [Deficiência parcial do Complexo I impede oxidação eficiente do NADH; piruvato é desviado para lactato (regenera NAD⁺) — daí o acúmulo. Tecidos oxidativos sofrem (encefalomiopatia). CoQ10/riboflavina/tiamina podem ajudar marginalmente; cura não existe.]),
   ("E", [A criança apresenta resposta paradoxal à oxigenação suplementar, com piora dos sintomas ao aumentar a fração inspirada de O₂; a recomendação clínica é manter saturação de O₂ entre 85-90% em todos os pacientes com defeitos genéticos da cadeia respiratória mitocondrial confirmados.])))

#questao-mc("28", badge-aplicacao,
  [Neonato prematuro de 32 semanas em UTI neonatal mantém T = 36,2°C em ambiente termicamente neutro. Apresenta dificuldade em manter temperatura sem fonte externa de calor. Sobre o mecanismo termogênico fisiológico e a dificuldade do paciente:],
  (("A", [Neonatos prematuros não dependem do tecido adiposo marrom porque esse tecido só se desenvolve após os 6 meses de vida pós-natal; a regulação térmica em prematuros depende exclusivamente do tremor muscular, ainda imaturo nessa idade gestacional do desenvolvimento.]),
   ("B", [Neonatos têm grande quantidade de tecido adiposo marrom (rico em UCP1) que dissipa o gradiente sem síntese de ATP — toda energia da oxidação dos ácidos graxos vira calor (termogênese sem tremor). Prematuros têm reserva reduzida — mais dificuldade térmica.]),
   ("C", [O mecanismo termogênico principal de neonatos é o tremor muscular, totalmente desenvolvido ao nascer mesmo em prematuros, mas requer reserva de glicogênio muscular elevada que prematuros ainda não acumularam durante a vida intrauterina inicial.]),
   ("D", [A regulação térmica em neonatos depende da hibernação metabólica regulada pelo hipotálamo posterior; em prematuros essa função ainda é imatura e por isso a temperatura corporal flutua mais até a maturação completa do sistema nervoso central pediátrico.]),
   ("E", [Neonatos regulam temperatura por vasoconstrição cutânea reflexa de extrema potência (mantendo o calor central); prematuros têm essa capacidade ainda inadequada por imaturidade da inervação simpática vascular periférica e suas conexões com o sistema nervoso autônomo central.])))

#questao-mc("29", badge-aplicacao,
  [Pesquisador quer distinguir experimentalmente um inibidor da ATP sintase (oligomicina) de um desacoplador (DNP) em mitocôndrias isoladas de fígado de rato. Apenas com base em consumo de O₂ por oximetria, qual sequência permite distinguir os dois compostos?],
  (("A", [Ambos os compostos aumentam o consumo de O₂ ao máximo, em ritmo similar e indistinguível na oximetria; a distinção requer dosagem direta de ATP gerado, não acessível em oximetria simples sem ensaios adicionais espectrofotométricos.]),
   ("B", [Ambos os compostos reduzem o consumo de O₂ a níveis basais idênticos; a distinção entre eles requer análise da temperatura do meio de incubação (DNP gera calor, oligomicina não), feita com termopar microeletrônico padrão laboratorial.]),
   ("C", [Oligomicina aumenta o consumo de O₂ porque libera os complexos respiratórios da retroinibição do gradiente, enquanto DNP reduz o consumo porque dissipa o gradiente que dirige os complexos a operarem em ritmo máximo na cadeia respiratória ativada.]),
   ("D", [Apenas a adição prévia de cianeto seguida de oligomicina permite distinguir os dois compostos, porque cianeto bloqueia o Complexo IV e remove a variável O₂ da equação experimental; mensurar apenas ATP em pH fixo é insuficiente para diferenciá-los.]),
   ("E", [Após oligomicina, consumo de O₂ cai (cadeia trava por retroinibição); após DNP, consumo aumenta (cadeia acelera tentando recompor gradiente que vaza). Se oligomicina vier primeiro e depois DNP, o consumo se recupera ao máximo — confirma DNP como desacoplador.])))

#questao-mc("30", badge-aplicacao,
  [Atleta de endurance ingere CoQ10 oral diariamente como suplemento esportivo após ler artigo afirmando melhora do desempenho aeróbico em maratonas. Sobre as bases bioquímicas e a evidência clínica do CoQ10 oral como ergogênico:],
  (("A", [CoQ10 é hub central da cadeia respiratória (recebe elétrons de I, II, β-oxidação, G3P-DH). Em pessoas saudáveis, a CoQ endógena é suficiente — suplementação não tem benefício comprovado no desempenho. Indicação genuína: deficiências severas (genéticas ou induzidas por estatinas em casos selecionados).]),
   ("B", [CoQ10 oral é absorvida em quantidades não significativas no intestino delgado em pessoas saudáveis, mas em atletas de endurance a permeabilidade intestinal aumenta dramaticamente durante o esforço, permitindo absorção elevada e benefício comprovado em maratonas em meta-análises.]),
   ("C", [CoQ10 funciona como desacoplador parcial da cadeia respiratória em altas doses, aumentando o gasto basal e o consumo de O₂ por unidade de massa muscular, justificando o uso por atletas que buscam emagrecimento associado ao desempenho aeróbico durante a temporada de treinos pré-competição.]),
   ("D", [CoQ10 substitui a coenzima Q endógena de forma competitiva, deslocando as moléculas antigas e renovando o pool da cadeia respiratória — esse turnover acelerado é o mecanismo principal da melhora de desempenho descrita em atletas e justifica o uso preventivo a partir dos 25 anos.]),
   ("E", [CoQ10 estimula a síntese de novas mitocôndrias via PGC-1α em condições de treino aeróbico, e essa biogênese mitocondrial é o mecanismo principal do ganho de desempenho — daí a recomendação atual de uso por todos os atletas profissionais de modalidades de resistência.])))
