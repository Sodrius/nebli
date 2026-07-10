#import "../typst-template/nebli_v2_apostila.typ": *

// ─── CONSOLIDAÇÃO (Q01–Q10) ───────────────────────────────

#questao-mc("01", badge-consolidacao,
  [A reação catalisada pelo *complexo da piruvato desidrogenase* (PDH) — "passo 0" do ciclo — produz, a partir de uma molécula de piruvato:],
  (("A", [oxaloacetato + 1 NADH + 1 CO₂, em uma reação anaplerótica que repõe o intermediário de 4 carbonos do passo 8 para a próxima volta do ciclo, sem geração de acetila]),
   ("B", [acetil-CoA + 1 NADH + 1 CO₂, com perda de um carbono como dióxido de carbono e captura de elétrons no NAD⁺ pela ação combinada de E1, E2 e E3]),
   ("C", [acetil-CoA + 1 FADH₂ + 1 CO₂, usando FAD ligado covalentemente como aceptor primário em mecanismo análogo ao do Complexo II da cadeia respiratória mitocondrial interna]),
   ("D", [acetil-CoA + 1 GTP em nível de substrato, sem liberação de CO₂, em paralelo com a quebra da ligação tioéster pelo lipoato com regeneração simultânea da coenzima A livre]),
   ("E", [acetil-CoA + 1 ATP em nível de substrato, sem perda de carbono, com fosforilação direta do ADP pela transferência da ligação fosfato do piruvato em mecanismo de catálise tioéster])))

#questao-mc("02", badge-consolidacao,
  [Qual enzima catalisa o *passo 1* do ciclo de Krebs, condensando acetil-CoA e oxaloacetato em citrato?],
  (("A", [Aconitase, que recebe o citrato formado e o isomeriza em isocitrato, movendo a hidroxila do carbono terciário para o secundário em rearranjo geométrico sem cofator]),
   ("B", [Isocitrato desidrogenase, que cataliza a primeira oxidação do ciclo e libera o primeiro CO₂, sendo o marco-passo regulado por ADP e Ca²⁺ alostericamente]),
   ("C", [Citrato sintase, que aproveita a energia da ligação tioéster da acetil-CoA para forçar a condensação aldólica com OAA em reação fortemente exergônica e irreversível]),
   ("D", [Malato desidrogenase, que fecha o ciclo no passo 8 produzindo o terceiro NADH e regenerando o OAA para receber a próxima acetila vinda da PDH]),
   ("E", [Succinil-CoA sintetase, que catalisa a única fosforilação em nível de substrato do ciclo, produzindo GTP a partir da quebra da ligação tioéster da succinil-CoA])))

#questao-mc("03", badge-consolidacao,
  [Em qual posição do ciclo se encontra o intermediário *isocitrato*?],
  (("A", [entre os passos 1 e 2, sendo o produto direto da condensação acetil-CoA + OAA catalisada pela citrato sintase em sua forma final hidratada]),
   ("B", [entre os passos 2 e 3, formado pela aconitase a partir do citrato e oxidado em seguida pela isocitrato desidrogenase, gerando o primeiro NADH do ciclo]),
   ("C", [entre os passos 3 e 4, sendo o produto da primeira descarboxilação e o substrato direto do complexo α-cetoglutarato desidrogenase na sequência]),
   ("D", [entre os passos 4 e 5, com função de transportar a ligação tioéster até a succinil-CoA sintetase, viabilizando a fosforilação em nível de substrato]),
   ("E", [entre os passos 7 e 8, atuando como precursor imediato do oxaloacetato regenerado pela malato desidrogenase em condições de baixo ATP intracelular])))

#questao-mc("04", badge-consolidacao,
  [A *succinato desidrogenase*, enzima do *passo 6*, possui uma característica única dentre as enzimas do ciclo. Assinale a alternativa correta:],
  (("A", [é o único complexo multienzimático do ciclo, formado por três enzimas distintas e cinco coenzimas, em arranjo análogo ao do PDH no passo 0 da entrada do piruvato]),
   ("B", [usa NADP⁺ em vez de NAD⁺ como aceptor de elétrons, gerando NADPH para vias biossintéticas como a síntese de ácidos graxos no citosol após exportação pelo citrato]),
   ("C", [está embutida na membrana mitocondrial interna e funciona simultaneamente como Complexo II da cadeia respiratória, entregando elétrons à ubiquinona via FAD ligado covalentemente]),
   ("D", [catalisa uma descarboxilação oxidativa, eliminando o segundo CO₂ do ciclo e gerando o terceiro NADH em reação irreversível regulada por ADP e cálcio intracelular]),
   ("E", [é regulada por fosforilação reversível pela ação de uma quinase e fosfatase específicas, em paralelo ao mecanismo regulatório clássico do PDH no passo 0])))

#questao-mc("05", badge-consolidacao,
  [Em qual *passo* do ciclo de Krebs ocorre a *fosforilação em nível de substrato*, a única do ciclo?],
  (("A", [Passo 3, na isocitrato desidrogenase, aproveitando a energia da descarboxilação para gerar o primeiro NADH e simultaneamente um GTP que será convertido em ATP]),
   ("B", [Passo 4, na α-cetoglutarato desidrogenase, em mecanismo idêntico ao da PDH mas com produção adicional de GTP pela presença de uma quarta enzima no complexo]),
   ("C", [Passo 5, na succinil-CoA sintetase, que aproveita a energia da ligação tioéster da succinil-CoA — vinda do passo 4 — para fosforilar GDP a GTP independentemente de O₂]),
   ("D", [Passo 6, na succinato desidrogenase, junto com a produção de FADH₂, aproveitando a localização membranar para acoplamento direto com a bomba de prótons do Complexo III]),
   ("E", [Passo 8, na malato desidrogenase, com a fosforilação acoplada à oxidação do malato, gerando NADH e ATP simultaneamente em mecanismo análogo ao da glicólise])))

#questao-mc("06", badge-consolidacao,
  [Qual a sequência *correta* dos quatro últimos intermediários do ciclo, na ordem em que aparecem após o passo 5?],
  (("A", [succinato → fumarato → oxaloacetato → malato, com a fumarase hidratando o fumarato diretamente no OAA e a MDH fechando o ciclo ao isomerizar OAA em malato]),
   ("B", [succinato → malato → fumarato → oxaloacetato, com a fumarase produzindo malato primeiro e a desidratação no passo seguinte gerando fumarato antes da oxidação final]),
   ("C", [succinato → fumarato → malato → oxaloacetato, com SDH gerando fumarato, fumarase hidratando para malato e MDH oxidando malato em OAA com produção do terceiro NADH]),
   ("D", [fumarato → succinato → malato → oxaloacetato, com a SDH atuando no fumarato primeiro e o succinato sendo intermediário posterior na sequência das reações]),
   ("E", [malato → fumarato → succinato → oxaloacetato, numa ordem reversa em que o malato perde água para formar fumarato antes de ser oxidado a succinato e depois OAA])))

#questao-mc("07", badge-consolidacao,
  [O saldo de cofatores reduzidos e composto fosforilado *por volta* do ciclo de Krebs (excluindo o passo 0) é:],
  (("A", [4 NADH + 0 FADH₂ + 1 GTP, com NADH sendo gerado em todos os quatro passos de oxidação inclusive o passo 6 do succinato desidrogenase em arranjo solúvel na matriz]),
   ("B", [3 NADH + 1 FADH₂ + 1 GTP, com NADH nos passos 3, 4 e 8; FADH₂ no passo 6 ligado à membrana; GTP no passo 5 por fosforilação em nível de substrato independente de O₂]),
   ("C", [2 NADH + 2 FADH₂ + 1 GTP, com FADH₂ sendo gerado tanto na succinato desidrogenase quanto na α-cetoglutarato desidrogenase em arranjo multienzimático compartilhado]),
   ("D", [3 NADH + 1 FADH₂ + 2 GTP, com fosforilação em nível de substrato ocorrendo no passo 5 e novamente no passo 8 pela ação da malato desidrogenase nucleotidil-quinase]),
   ("E", [4 NADH + 1 FADH₂ + 0 GTP, com produção exclusiva de cofatores reduzidos que serão depois convertidos em ATP pela cadeia respiratória sem etapa de substrato])))

#questao-mc("08", badge-consolidacao,
  [Qual enzima do ciclo é considerada *marco-passo* (rate-limiting), ativada alostericamente por ADP e Ca²⁺?],
  (("A", [Citrato sintase no passo 1, regulada principalmente por ATP e succinil-CoA, com cálcio atuando como estabilizador alostérico do sítio ativo em condições de demanda]),
   ("B", [Aconitase no passo 2, sensível ao estado redox da célula e ativada por ADP em resposta à queda da carga energética, sendo o ponto onde fluoroacetato bloqueia o ciclo]),
   ("C", [Isocitrato desidrogenase no passo 3, alostericamente ativada por ADP e cálcio em resposta a contração muscular, e inibida por ATP e NADH em condições de carga energética alta]),
   ("D", [Succinil-CoA sintetase no passo 5, regulada por GDP/GTP citosólico e pela razão acetil-CoA/CoA livre, sendo o ponto da única fosforilação em nível de substrato do ciclo]),
   ("E", [Malato desidrogenase no passo 8, ativada por ADP em condições aeróbias e funcionando como sensor primário da carga energética ao fechar o ciclo regenerando OAA])))

#questao-ce("09", badge-consolidacao,
  [Julgue os itens abaixo sobre a localização das reações do ciclo de Krebs:],
  ((("I", [Todas as enzimas do ciclo encontram-se dissolvidas na matriz mitocondrial, formando um conjunto homogêneo de catalisadores solúveis sem ancoragem a estruturas membranares.]),
    ("II", [O *passo 6* (succinato desidrogenase) está embutido na membrana mitocondrial interna e é também o Complexo II da cadeia respiratória.]),
    ("III", [O *passo 0* (complexo PDH) ocorre no citosol antes do transporte do piruvato para a matriz, em paralelo com a fase final da glicólise.]),
    ("IV", [Os 2 CO₂ liberados por volta do ciclo provêm dos *passos 3 e 4*, ambos descarboxilações oxidativas catalisadas por desidrogenases ligadas a NAD⁺.]))))

#questao-mc("10", badge-consolidacao,
  [O acetil-CoA, substrato real do ciclo no passo 1, *não* pode ser gerado a partir de qual via?],
  (("A", [β-oxidação de ácidos graxos, processo que ocorre na matriz mitocondrial gerando acetil-CoA, NADH e FADH₂ em sucessivas voltas até quebrar a cadeia carbônica]),
   ("B", [descarboxilação oxidativa do piruvato pelo complexo PDH no passo 0, com perda de um CO₂ e captura dos elétrons em NAD⁺ formando NADH na matriz]),
   ("C", [degradação de aminoácidos cetogênicos como leucina e lisina, que convergem para acetil-CoA ou acetoacetato sem produzir piruvato como intermediário comum]),
   ("D", [degradação de corpos cetônicos no jejum prolongado em tecidos extra-hepáticos, com regeneração da acetil-CoA pela ação combinada da β-cetoacil-CoA transferase]),
   ("E", [gliconeogênese a partir de glicerol no fígado, que entra na via como diidroxiacetona-fosfato após fosforilação e segue até glicose-6-fosfato sem passar por acetil-CoA]) ))

// ─── INTEGRAÇÃO (Q11–Q25) ─────────────────────────────────

#questao-mc("11", badge-integracao,
  [Os *passos 0* (PDH) e *4* (α-KG-DH) compartilham uma característica arquitetural marcante:],
  (("A", [ambos são enzimas únicas e solúveis na matriz, com um sítio catalítico que combina ligante de TPP, lipoato e CoA em arranjo sequencial dentro da mesma cadeia polipeptídica]),
   ("B", [ambos catalisam reações reversíveis em condições fisiológicas, dependendo do equilíbrio entre piruvato e acetil-CoA no caso do passo 0 e do α-KG e succinil-CoA no caso do passo 4]),
   ("C", [ambos são complexos multienzimáticos com três enzimas (E1, E2, E3) e cinco coenzimas (TPP, lipoato, FAD, NAD⁺, CoA), diferindo apenas no substrato — piruvato vs α-cetoglutarato]),
   ("D", [ambos usam FAD como aceptor primário de elétrons em vez de NAD⁺, gerando FADH₂ que será entregue diretamente à ubiquinona da cadeia respiratória em arranjo membranar]),
   ("E", [ambos produzem GTP por fosforilação em nível de substrato, aproveitando a quebra da ligação tioéster do produto para fosforilar GDP simultaneamente à liberação de CO₂])))

#questao-mc("12", badge-integracao,
  [O *fluoroacetato* (rodenticida) é convertido a fluorocitrato no organismo e bloqueia o ciclo no *passo 2*. A enzima inibida é a aconitase. A consequência metabólica imediata é o acúmulo de:],
  (("A", [α-cetoglutarato e succinil-CoA, com bloqueio nas descarboxilações dos passos 3 e 4 por inibição direta das desidrogenases pela própria molécula de fluoracetato livre]),
   ("B", [citrato (substrato da aconitase, que se acumula porque não é convertido a isocitrato) e oxaloacetato (porque continua sendo gerado no passo 8 mas não consumido no passo 1 sem citrato sintase)]),
   ("C", [fumarato e malato, por inibição cruzada da fumarase no passo 7 secundária à queda do estado redox da matriz pela depleção do NADH e oxidação reversa da malato desidrogenase]),
   ("D", [succinato e FADH₂, com bloqueio do Complexo II da cadeia respiratória por uma ação tóxica direta do fluoroacetato sobre a porção membranar da succinato desidrogenase]),
   ("E", [acetil-CoA e piruvato, porque o bloqueio do passo 2 impede a entrada de acetila no ciclo e força o piruvato a se acumular antes de ser convertido pela PDH no passo 0])))

#questao-mc("13", badge-integracao,
  [No *passo 8*, a malato desidrogenase converte malato em oxaloacetato com ΔG' padrão *positivo*. Por que essa reação ocorre no sentido direto nas células?],
  (("A", [porque o OAA é consumido em tempo real pela citrato sintase do passo 1, mantendo sua concentração intracelular muito baixa e deslocando o equilíbrio para frente pelo princípio de Le Chatelier]),
   ("B", [porque a célula gasta uma molécula de ATP para forçar a reação adiante, em mecanismo análogo ao da hexoquinase na glicólise que captura a glicose por fosforilação inicial]),
   ("C", [porque a enzima é alostericamente ativada pelo próprio malato em altas concentrações, com cooperatividade positiva análoga à hemoglobina e mudança conformacional dos sítios catalíticos]),
   ("D", [porque, em condições celulares, o pH baixa o suficiente para mudar o ΔG' efetivo da reação, em mecanismo análogo ao do ciclo de Bohr na captura/liberação de oxigênio pela hemoglobina]),
   ("E", [porque o NADH produzido é imediatamente exportado para o citosol via lançadeira do malato-aspartato, deslocando o equilíbrio ao remover um dos produtos da reação enzimática]) ))

#questao-mc("14", badge-integracao,
  [A *piruvato carboxilase* é a principal reação anaplerótica do ciclo. Ela é virtualmente inativa na ausência de qual efetor?],
  (("A", [biotina como coenzima covalente, sem a qual a transferência do grupo carboxila do bicarbonato para o piruvato é impedida — o que ocorre em deficiência alimentar prolongada de ovo cru]),
   ("B", [ATP como substrato energético, sem o qual a carboxilação do piruvato em OAA não pode prosseguir pela falta da energia necessária para a formação da ligação carbono-carbono]),
   ("C", [acetil-CoA como efetor alostérico positivo, sinal de que está chegando muito combustível e que o ciclo precisa de mais OAA para receber a próxima acetila no passo 1]),
   ("D", [HCO₃⁻ como doador do grupo carboxila incorporado ao piruvato, sem o qual a enzima fica catalíticamente competente mas sem substrato para a transferência da carboxila ativa]),
   ("E", [Mg²⁺ como cofator metálico, sem o qual o ATP não pode se posicionar adequadamente no sítio ativo para doar o fosfato gama necessário à fosforilação do intermediário carboxibiotina])))

#questao-ce("15", badge-integracao,
  [Em paciente com etilismo crônico e desnutrição grave, espera-se *deficiência de tiamina (B1)*. Julgue:],
  ((("I", [O *passo 0* (complexo PDH) sofre redução de atividade, com acúmulo de piruvato e lactato no plasma por carência de TPP na enzima E1.]),
    ("II", [O *passo 4* (complexo α-KG-DH) também é prejudicado, pois compartilha a mesma exigência de TPP no primeiro passo enzimático.]),
    ("III", [O *passo 6* (succinato desidrogenase) é diretamente inibido pela deficiência de B1 e contribui para a queda do FADH₂ no quadro clínico.]),
    ("IV", [Quadro clínico compatível inclui encefalopatia de Wernicke e beriberi, com manifestações neurológicas e cardiovasculares por insuficiência energética cerebral.]))))

#questao-mc("16", badge-integracao,
  [Numa célula muscular em contração intensa, o cálcio liberado pelo retículo sarcoplasmático *acelera* o ciclo de Krebs porque:],
  (("A", [ativa alostericamente a IDH no passo 3 e a α-KG-DH no passo 4, além de estimular a desfosforilação e ativação da PDH no passo 0 via piruvato desidrogenase fosfatase]),
   ("B", [inibe a succinato desidrogenase no passo 6, redirecionando o fluxo de elétrons do FAD para o NAD⁺ via uma ponte molecular alternativa que se forma em alta carga de cálcio]),
   ("C", [fosforila e ativa a citrato sintase no passo 1, em mecanismo análogo ao da glicogênio fosforilase no músculo, com cascata de quinases dependentes de cálcio-calmodulina ativando o ciclo]),
   ("D", [ativa diretamente a ATP-sintase da membrana mitocondrial interna, "puxando" o ciclo por aumento de demanda de NADH e FADH₂ na cadeia respiratória subsequente sem efeito local nas enzimas]),
   ("E", [bloqueia as reações anapleróticas e cataplerose do ciclo, concentrando os intermediários dentro da matriz e forçando o fluxo a se manter dentro do circuito sem perdas para biossíntese])))

#questao-mc("17", badge-integracao,
  [No jejum prolongado, qual intermediário do ciclo é *predominantemente* desviado para a gliconeogênese hepática?],
  (("A", [citrato (saída após o passo 1), exportado ao citosol e clivado em acetil-CoA e OAA pela citrato liase ATP-dependente para alimentar simultaneamente cetogênese e síntese de glicose]),
   ("B", [α-cetoglutarato (entre os passos 3 e 4), transaminado no citosol em glutamato e posteriormente convertido em piruvato pela cadeia de transaminação tecidual no rim e no fígado]),
   ("C", [succinil-CoA (após o passo 4), convertido a propionil-CoA e depois a propionato, principal substrato para a síntese de glicose em mamíferos no jejum por excesso de aminoácidos]),
   ("D", [oxaloacetato (após o passo 8), convertido em fosfoenolpiruvato pela PEPCK e iniciando a sequência inversa da glicólise hepática para manter a glicemia durante o jejum prolongado]),
   ("E", [fumarato (após o passo 6), entrando diretamente na via gliconeogênica pela ação reversa da fumarase e da SDH em sequência inversa para regenerar precursores carbônicos de glicose])))

#questao-mc("18", badge-integracao,
  [A succinil-CoA sintetase, no passo 5, gera GTP — único composto fosforilado de alta energia produzido *diretamente* dentro do ciclo. Numa célula tratada com *oligomicina* (inibidor da ATP-sintase), este GTP:],
  (("A", [deixa de ser produzido porque depende do gradiente de prótons da membrana mitocondrial interna, que colapsa quando a ATP-sintase é bloqueada e a passagem de H⁺ é impedida]),
   ("B", [continua sendo produzido normalmente porque a fosforilação em nível de substrato aproveita a energia da ligação tioéster da succinil-CoA — independente do gradiente de prótons e da ATP-sintase]),
   ("C", [é redirecionado para a síntese de creatina-fosfato muscular pela ação de uma transferase mitocondrial específica, mantendo a reserva de fosfato de alta energia para a contração]),
   ("D", [acumula na matriz mitocondrial sem ser convertido em ATP, porque a nucleosídeo difosfato quinase depende do gradiente de prótons para operar em sentido GTP → ATP eficiente]),
   ("E", [é hidrolisado de volta a GDP pela própria succinil-CoA sintetase em mecanismo de feedback negativo quando a ATP-sintase está bloqueada e o produto final ATP não pode ser formado])))

#questao-mc("19", badge-integracao,
  [Numa célula tratada com *2,4-dinitrofenol* (desacoplador), o consumo de O₂ aumenta dramaticamente enquanto a produção de ATP cai. Sobre as fontes preservadas de ATP:],
  (("A", [a fosforilação em nível de substrato é preservada — incluindo os 2 ATP líquidos da glicólise e o GTP do passo 5 do ciclo, todos independentes do gradiente de prótons mitocondrial]),
   ("B", [toda produção de ATP da célula é abolida, pois a fosforilação em nível de substrato também depende indiretamente do gradiente de prótons mantido pela cadeia respiratória ativa]),
   ("C", [apenas o FADH₂ do passo 6 continua sendo produtivo, pois ele tem uma rota alternativa direta para a ATP-sintase que não passa pelo gradiente de prótons da membrana]),
   ("D", [a produção de ATP aumenta proporcionalmente ao consumo de O₂, pois o desacoplador acelera a cadeia respiratória e a ATP-sintase em sintonia mantendo a estequiometria preservada]),
   ("E", [a célula passa a usar exclusivamente corpos cetônicos como combustível, ignorando a glicose e o ciclo de Krebs, em adaptação metabólica idêntica à do jejum prolongado clínico]) ))

#questao-mc("20", badge-integracao,
  [Sobre o caráter *anfibólico* do ciclo, qual afirmação é a mais completa?],
  (("A", [só α-cetoglutarato sai do ciclo para biossíntese, sendo convertido em glutamato pela glutamato desidrogenase em reação reversível dependente de NADPH como cofator redutor, sem participação anabólica dos demais intermediários do ciclo do ácido cítrico]),
   ("B", [só succinil-CoA tem função anabólica, servindo de precursor exclusivo para a síntese de heme em medula óssea e hepatócitos por incorporação na via da δ-aminolevulinato sintase, sem participação dos outros intermediários do ciclo]),
   ("C", [só o citrato é exportado para o citosol, alimentando exclusivamente a síntese de ácidos graxos em condições de carga energética alta via citrato liase ATP-dependente, sem outras saídas anabólicas possíveis do ciclo metabólico]),
   ("D", [só oxaloacetato pode ser desviado para a gliconeogênese hepática, sendo o único ponto de saída anabólico do ciclo em mamíferos no estado de jejum prolongado e na gliconeogênese a partir de aminoácidos glicogênicos sem outras opções]),
   ("E", [todos esses são pontos de saída anabólica do ciclo: α-cetoglutarato (entre passos 3 e 4) → aminoácidos; succinil-CoA (após passo 4) → heme; citrato (após passo 1) → ácidos graxos; OAA (após passo 8) → gliconeogênese])))

#questao-mc("21", badge-integracao,
  [O *passo 6* (succinato desidrogenase) é o único do ciclo que usa FAD em vez de NAD⁺. A razão termodinâmica principal é:],
  (("A", [FAD tem maior afinidade pelo substrato succinato do que NAD⁺ devido à geometria do sítio ativo da enzima, em diferença evolutiva selecionada por pressão metabólica em condições aeróbias]),
   ("B", [o ΔE° da reação succinato/fumarato é incompatível com NAD⁺ (que exige potencial mais negativo) e adequado para FAD, que aceita elétrons em potencial menor — viabilizando energeticamente a reação]),
   ("C", [o NAD⁺ não consegue atravessar a membrana mitocondrial interna onde a SDH se encontra, sendo substituído pelo FAD por uma questão de acessibilidade espacial mais do que energética]),
   ("D", [o FAD é a única coenzima disponível na membrana porque a célula concentra todo o NAD⁺ na matriz solúvel e reserva o FAD para enzimas integradas a complexos transmembranares]),
   ("E", [a SDH é uma enzima evolutivamente ancestral que precede o aparecimento do NAD⁺ no metabolismo primitivo, mantida no ciclo como reminiscência de uma via anaeróbia mais antiga]) ))

#questao-mc("22", badge-integracao,
  [Num experimento com *antimicina A* (inibidor do Complexo III da cadeia respiratória), o que acontece com o ciclo de Krebs?],
  (("A", [Krebs continua rodando normalmente porque é independente da cadeia respiratória — gera seus próprios cofatores reduzidos em circuito fechado e não depende do consumo subsequente de O₂]),
   ("B", [Krebs lentifica drasticamente porque NADH e FADH₂ não são re-oxidados na cadeia bloqueada — sem NAD⁺ e FAD livres, as desidrogenases dos passos 3, 4, 6 e 8 ficam sem aceptor de elétrons]),
   ("C", [apenas o passo 6 do ciclo é afetado porque é o único membranar e está adjacente ao Complexo II, ficando isolado dos outros passos solúveis que continuam rodando normalmente]),
   ("D", [apenas os passos 3 e 4 (descarboxilações) são afetados porque produzem CO₂ e a antimicina inibe a difusão de CO₂ através da membrana mitocondrial interna em sentido bidirecional]),
   ("E", [Krebs acelera para compensar a queda da produção de ATP, em mecanismo de feedback positivo mediado por queda de carga energética e ativação alostérica das três desidrogenases reguladas]) ))

#questao-ce("23", badge-integracao,
  [Sobre os 2 CO₂ liberados por volta do ciclo:],
  ((("I", [Um CO₂ sai no *passo 3* (isocitrato desidrogenase) e outro no *passo 4* (α-KG-DH), ambos em descarboxilações oxidativas com produção simultânea de NADH.]),
    ("II", [Esses 2 CO₂ liberados provêm dos carbonos do oxaloacetato (os 4 originais), não dos 2 carbonos da acetila que acabou de entrar no passo 1.]),
    ("III", [Sem essas descarboxilações o ciclo não se "fecharia" — acumularia massa a cada volta sem retornar a um intermediário de 4 carbonos como OAA.]),
    ("IV", [O CO₂ formado pelo *passo 0* (PDH) é contado separadamente, ocorrendo antes da entrada da acetila no ciclo propriamente dito.]))))

#questao-mc("24", badge-integracao,
  [Análise química do substrato da malato desidrogenase no *passo 8*: 4 carbonos com hidroxila no C-2. Produto: 4 carbonos com carbonila no lugar da hidroxila. Esta transformação é:],
  (("A", [uma desidratação com perda de água, em mecanismo análogo ao da fumarase do passo 7 que precedeu a malato desidrogenase no ciclo, sem participação de cofator]),
   ("B", [uma descarboxilação com perda de CO₂, em mecanismo análogo aos passos 3 e 4 do ciclo, com a hidroxila do C-2 sendo perdida juntamente com um carbono carboxílico adjacente]),
   ("C", [uma oxidação com transferência de 2 elétrons e 1 H⁺ do C-2 ao NAD⁺, formando NADH e convertendo o álcool secundário em cetona — terceiro NADH do ciclo gerado no passo 8]),
   ("D", [uma fosforilação com gasto de ATP, em mecanismo análogo ao da hexoquinase glicolítica, com a hidroxila do C-2 sendo o ponto de ataque do fosfato gama do ATP doador]),
   ("E", [uma isomerização sem balanço de elétrons, em mecanismo análogo ao da aconitase do passo 2, com a hidroxila migrando de uma posição a outra no mesmo esqueleto carbônico] )) )

#questao-mc("25", badge-integracao,
  [Numa célula com acetil-CoA alta e OAA baixo, qual o mecanismo de resposta via piruvato carboxilase?],
  (("A", [inibição da piruvato carboxilase pela acetil-CoA, permitindo acúmulo de piruvato no citosol e desvio para a fermentação lática sem reposição de OAA na matriz mitocondrial]),
   ("B", [conversão direta da acetil-CoA em OAA por uma enzima dedicada na matriz mitocondrial em condições de carga energética alta — caminho biossintético oposto ao do ciclo]),
   ("C", [ativação alostérica da piruvato carboxilase pela acetil-CoA, repondo OAA via reação anaplerótica (piruvato + HCO₃⁻ + ATP → OAA) para que o ciclo possa receber a acetila no passo 1]),
   ("D", [paralisação completa do passo 1 (citrato sintase) até que a concentração de acetil-CoA caia o suficiente para desinibir o ciclo e permitir a regeneração natural do OAA pelo passo 8]),
   ("E", [conversão da acetil-CoA em corpos cetônicos no fígado independentemente do estado do OAA, com bypass total do ciclo enquanto o jejum prolongado mantém o estado metabólico ativo]) ))

// ─── APLICAÇÃO (Q26–Q30) ──────────────────────────────────

#questao-mc("26", badge-aplicacao,
  [Lactente de 4 meses, sexo masculino, com acidose láctica grave, atraso neuropsicomotor e hipotonia. Exames: piruvato e lactato elevados, bicarbonato baixo. Investigação metabólica: ausência de atividade do complexo PDH (passo 0). Qual a explicação mais completa para a acidose láctica?],
  (("A", [a deficiência de PDH gera carência direta de ATP cerebral pela falta de acetil-CoA na matriz mitocondrial, e a acidose láctica decorre do consumo desregulado de bicarbonato pela hiperventilação compensatória secundária à hipóxia tecidual periférica e à demanda neuronal aumentada]),
   ("B", [o ciclo de Krebs roda ao contrário na ausência da PDH, gerando piruvato em vez de consumi-lo, e a acidose láctica vem da quebra reversa do passo 8 com produção excessiva de prótons na matriz e oxidação reversa dos cofatores reduzidos que se acumulam por feedback negativo]),
   ("C", [o bloqueio do passo 0 impede a conversão de piruvato em acetil-CoA; o piruvato acumulado é reduzido a lactato pela LDH para regenerar NAD⁺ na glicólise, gerando acidose. O acetil-CoA escasso também limita a anaplerose, secundariamente comprometendo o ciclo de Krebs.]),
   ("D", [a succinato desidrogenase do passo 6 é hiperativada na deficiência de PDH como mecanismo compensatório, gerando excesso de FADH₂ não acoplado à cadeia respiratória e levando à acidose por produção mitocondrial elevada de radicais livres e queda do pH celular]),
   ("E", [o bicarbonato plasmático é consumido pela aconitase no passo 2 em mecanismo de reação alternativa ativada na deficiência da PDH, com geração de CO₂ excessivo, queda do pH plasmático e formação de lactato em circuito metabólico de compensação adaptativo]) ))

#questao-mc("27", badge-aplicacao,
  [Etilista crônico desnutrido, confuso, com ataxia e oftalmoplegia. Diagnóstico: encefalopatia de Wernicke. Qual a explicação bioquímica integrada, identificando os passos do ciclo afetados?],
  (("A", [o álcool inibe diretamente a malato desidrogenase do passo 8 via geração de acetaldeído tóxico no fígado, com queda da produção do terceiro NADH do ciclo e prejuízo da regeneração do oxaloacetato para a próxima volta no passo 1 da citrato sintase em arranjo coordenado da via]),
   ("B", [deficiência de *tiamina (B1)* — coenzima TPP — paralisa simultaneamente o *passo 0* (complexo PDH) e o *passo 4* (complexo α-KG-DH), reduzindo a oxidação de piruvato e a continuidade do ciclo; o cérebro, altamente dependente de glicose oxidada via Krebs, sofre dano metabólico agudo.]),
   ("C", [deficiência de vitamina B12 (cobalamina) paralisa o passo 6 do ciclo (succinato desidrogenase) por interferência com a síntese do grupo heme do Complexo II da cadeia respiratória, levando à queda da produção de FADH₂ mitocondrial e dano cerebral progressivo no etilista crônico desnutrido]),
   ("D", [o acetaldeído gerado pelo metabolismo do etanol no fígado acumula-se no passo 1 do ciclo (citrato sintase) e bloqueia diretamente a condensação acetil-CoA mais oxaloacetato em citrato, paralisando o ciclo no ponto de entrada da acetila com dano neurológico secundário]),
   ("E", [a piruvato carboxilase é hiperestimulada pelo etanol em mecanismo alostérico e desvia todo o piruvato disponível para oxaloacetato no fígado, esgotando o acetil-CoA disponível e impedindo a continuidade do ciclo no passo 1 da próxima volta da engrenagem metabólica]) ))

#questao-mc("28", badge-aplicacao,
  [Paciente em jejum de 72h com hálito cetônico, cetonúria intensa, bicarbonato baixo. Qual a explicação metabólica integrada (Krebs + gliconeogênese)?],
  (("A", [no jejum, o fígado desvia *oxaloacetato* (saída após o passo 8) para a gliconeogênese a fim de manter a glicemia; o pool de OAA cai e a acetil-CoA da β-oxidação, sem OAA suficiente para entrar no passo 1, é desviada para corpos cetônicos. A acidose vem do β-hidroxibutirato e acetoacetato.]),
   ("B", [o jejum prolongado bloqueia diretamente a aconitase do *passo 2* do ciclo por carência intracelular de citrato citosólico e mitocondrial, paralisando o ciclo no segundo passo e forçando o acúmulo de acetil-CoA derivada da β-oxidação que é então convertida em corpos cetônicos hepáticos liberados na circulação portal]),
   ("C", [os corpos cetônicos circulantes são produzidos pela fumarase do *passo 7* do ciclo em uma reação alternativa ativada no estado de jejum prolongado, com clivagem direta do fumarato citosólico em duas moléculas de β-hidroxibutirato e acetoacetato em mecanismo metabólico hepático compensatório]),
   ("D", [a deficiência de tiamina (vitamina B1) secundária ao jejum prolongado é a única explicação plausível para a cetose, com paralisia simultânea da PDH no passo 0 e da α-KG-DH no passo 4, levando ao desvio do piruvato acumulado para corpos cetônicos no fígado e tecidos extra-hepáticos]),
   ("E", [o glicogênio hepático esgotado no jejum bloqueia a succinato desidrogenase do *passo 6* do ciclo por carência secundária de FAD, redirecionando todo o fluxo metabólico do ciclo para a produção compensatória de corpos cetônicos por uma via alternativa ativada no hepatócito em hipoglicemia]) ))

#questao-mc("29", badge-aplicacao,
  [Célula tumoral cultivada com *oligomicina* (inibe ATP-sintase): O₂ cai, Krebs para por acúmulo de NADH/FADH₂, célula depende da glicólise anaeróbia. Quantos ATP por glicose?],
  (("A", [a célula continua produzindo 30-32 ATP por glicose mesmo com a ATP-sintase bloqueada pela oligomicina, pois o ciclo de Krebs compensa via fosforilação em nível de substrato no passo 5 em mecanismo redundante ativado pela queda do gradiente de prótons da membrana interna em condições de inibição prolongada]),
   ("B", [nenhum ATP é produzido na célula tratada com oligomicina, pois todas as vias glicolíticas citosólicas e do ciclo mitocondrial dependem indiretamente da ATP-sintase ativa para manter o gradiente de prótons que sustenta o transporte mitocondrial de substratos e cofatores entre os compartimentos celulares]),
   ("C", [o ciclo de Krebs gera os 10 ATP por volta normalmente mesmo com oligomicina, pois é totalmente independente da membrana interna e da ATP-sintase em sua maquinaria enzimática, com a fosforilação em nível de substrato do passo 5 sendo suficiente para o saldo energético total observado da via]),
   ("D", [saldo de 2 ATP da glicólise anaeróbia mais o GTP do passo 5 do ciclo (que é fosforilação em nível de substrato), totalizando ~4 ATP — mas como Krebs também para por acúmulo de cofatores, sobram só os 2 ATP da glicólise, com piruvato sendo reduzido a lactato pela LDH para regenerar NAD⁺ citosólico.]),
   ("E", [a célula passa a usar exclusivamente o FADH₂ do passo 6 do ciclo para gerar ATP no citosol via lançadeira reversa do glicerol-3-fosfato em mecanismo alternativo, com bypass total da ATP-sintase bloqueada e produção mantida em níveis basais por circuito compensatório celular adaptativo]) ))

#questao-mc("30", badge-aplicacao,
  [Mitocôndria isolada com succinato (substrato do passo 6), ADP, Pi, O₂ e *malonato* (inibidor competitivo da SDH). Consumo de O₂ é abolido. Qual a interpretação mecanística?],
  (("A", [malonato compete com succinato no sítio ativo da SDH (passo 6), bloqueando a formação de FADH₂ e a entrada de elétrons no Complexo II; sem alimentar a cadeia, o O₂ não é consumido. O ciclo também para porque succinato não vira fumarato no passo 6.]),
   ("B", [o malonato inibe a ATP-sintase diretamente em mecanismo análogo ao da oligomicina, com colapso da fosforilação oxidativa e do consumo de O₂ pelo retorno do gradiente de prótons da membrana interna sem aproveitamento útil em síntese de ATP mitocondrial nas mitocôndrias isoladas testadas]),
   ("C", [o malonato é convertido a malato no passo 8 do ciclo pela ação da malato desidrogenase reversa, drenando o ciclo pelo lado oposto da engrenagem e gerando o terceiro NADH em excesso que bloqueia as desidrogenases por feedback negativo intracelular nas mitocôndrias isoladas em ensaio]),
   ("D", [o malonato bloqueia a citrato sintase do passo 1 em vez da SDH do passo 6 em mecanismo de inibição alostérica direta, paralisando o ciclo no ponto de entrada da acetila e impedindo a regeneração subsequente dos cofatores reduzidos necessários à cadeia respiratória em consumo de O₂]),
   ("E", [o succinato adicionado ao meio extramitocondrial não consegue entrar na mitocôndria isolada por ausência do transportador de dicarboxilato funcional, e o malonato apenas se acumula no meio externo sem efeito sobre a succinato desidrogenase em si nem sobre a cadeia respiratória ativa]) ))

#pagebreak()

#gabarito-page((
  ("Consolidação (Q01–Q10)",
    (("01", "B"), ("02", "C"), ("03", "B"), ("04", "C"), ("05", "C"),
     ("06", "C"), ("07", "B"), ("08", "C"), ("09", "ECEC"), ("10", "E"))),
  ("Integração (Q11–Q25)",
    (("11", "C"), ("12", "B"), ("13", "A"), ("14", "C"), ("15", "CCEC"),
     ("16", "A"), ("17", "D"), ("18", "B"), ("19", "A"), ("20", "E"),
     ("21", "B"), ("22", "B"), ("23", "CECC"), ("24", "C"), ("25", "C"))),
  ("Aplicação (Q26–Q30)",
    (("26", "C"), ("27", "B"), ("28", "A"), ("29", "D"), ("30", "A"))),
))
