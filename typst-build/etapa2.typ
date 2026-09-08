#import "../typst-template/nebli_v2_apostila.typ": *

#questao-mc("01", badge-consolidacao,
  [Qual gene do operon lac codifica a enzima que hidrolisa a lactose em glicose e galactose?],
  (("A", [lacA — codifica a transacetilase, que acetila galactosídeos não metabolizáveis para excreção]),
   ("B", [lacY — codifica a permease, que transporta a lactose através da membrana plasmática]),
   ("C", [crp — codifica a proteína CAP, ativador transcricional que se liga ao sítio CAP]),
   ("D", [lacZ — codifica a β-galactosidase, que hidrolisa a lactose em glicose e galactose]),
   ("E", [lacI — codifica o repressor tetramérico, que se liga ao operador do operon lac])))

#questao-mc("02", badge-consolidacao,
  [O indutor fisiológico do operon lac, isto é, a molécula que efetivamente se liga ao repressor, é:],
  (("A", [a alolactose, isômero da lactose gerado pela própria β-galactosidase em reação lateral]),
   ("B", [a lactose intacta, transportada para o citoplasma pela permease codificada por lacY]),
   ("C", [a galactose livre, liberada pela hidrólise da ligação β-1,4 da lactose]),
   ("D", [o cAMP, nucleotídeo cíclico sintetizado pela adenilato-ciclase na ausência de glicose]),
   ("E", [a glicose-6-fosfato, primeiro intermediário fosforilado do catabolismo da glicose])))

#questao-ce("03", badge-consolidacao,
  [Julgue os itens sobre a localização e a natureza dos elementos do operon lac.],
  (("I",   [O operador é uma sequência de DNA que sobrepõe o sítio de início da transcrição.]),
   ("II",  [O gene lacI tem promotor próprio, independente do promotor dos genes estruturais.]),
   ("III", [O sítio CAP localiza-se à jusante do operador, dentro do gene lacZ.]),
   ("IV",  [Os genes lacZ, lacY e lacA são transcritos em três moléculas de mRNA distintas.])))

#questao-mc("04", badge-consolidacao,
  [As sequências consenso das regiões −35 e −10 do promotor bacteriano são, respectivamente:],
  (("A", [TATGTT e TTTACA, as sequências efetivamente encontradas no promotor lac]),
   ("B", [TTTACA e TATGTT, as sequências reconhecidas pela proteína CAP no sítio CAP]),
   ("C", [TATAAT e TTGACA, na ordem em que aparecem a partir do sítio de início]),
   ("D", [TTGACA e TATAAT, as bases mais frequentes em cada posição dos promotores]),
   ("E", [GGGCGG e CCAAT, elementos de ligação de fatores gerais de transcrição])))

#questao-mc("05", badge-consolidacao,
  [Sobre as proteínas que regulam o operon lac, assinale a alternativa *incorreta*:],
  (("A", [O repressor LacI é um tetrâmero formado pela associação de dois dímeros idênticos]),
   ("B", [A CAP só assume conformação capaz de ligar o DNA quando complexada ao cAMP]),
   ("C", [O sítio de ligação do indutor em LacI fica no domínio hélice-volta-hélice N-terminal]),
   ("D", [A subunidade σ da RNA-polimerase é quem reconhece as regiões −35 e −10]),
   ("E", [A permease codificada por lacY transporta lactose em simporte com um próton])))

#questao-mc("06", badge-consolidacao,
  [No cultivo de bactérias em placa, a função do X-Gal é:],
  (("A", [servir de substrato cromogênico que, clivado pela β-galactosidase, libera pigmento azul]),
   ("B", [induzir o operon lac sem ser hidrolisado, mantendo a indução constante ao longo do cultivo]),
   ("C", [inibir a permease LacY e impedir a entrada de lactose na célula bacteriana]),
   ("D", [funcionar como co-repressor do operon, ativando o repressor LacI sobre o operador]),
   ("E", [elevar o cAMP intracelular e permitir a ligação da CAP ao seu sítio de ativação])))

#questao-ce("07", badge-consolidacao,
  [Julgue os itens sobre os reagentes e as construções usados no estudo do operon lac.],
  (("I",   [O IPTG induz o operon lac e não é hidrolisado pela β-galactosidase.]),
   ("II",  [O X-Gal, ao ser clivado pela β-galactosidase, libera um pigmento azul insolúvel.]),
   ("III", [O diploide parcial contém duas cópias de todo o genoma bacteriano.]),
   ("IV",  [A alolactose é produzida pela permease LacY durante o transporte da lactose.])))

#questao-mc("08", badge-consolidacao,
  [Em _Escherichia coli_, a relação entre a disponibilidade de glicose e o nível de cAMP é:],
  (("A", [glicose alta eleva o cAMP, que se liga à CAP e ativa fortemente o promotor lac]),
   ("B", [o cAMP independe da glicose e varia apenas com a concentração de lactose no meio]),
   ("C", [glicose baixa reduz o cAMP, o que impede a CAP de reconhecer o sítio CAP]),
   ("D", [glicose alta reduz o cAMP; glicose baixa eleva o cAMP e habilita a CAP]),
   ("E", [glicose e cAMP variam juntos, ambos sob controle direto do repressor LacI])))

#questao-mc("09", badge-consolidacao,
  [O transcrito primário gerado a partir dos genes estruturais do operon lac é classificado como:],
  (("A", [monocistrônico, com um sítio de ligação do ribossomo e um único códon de início]),
   ("B", [antissenso, complementar ao mRNA funcional e responsável por bloquear a tradução]),
   ("C", [poliproteico, traduzido em uma cadeia única depois clivada por proteases específicas]),
   ("D", [processado por splicing, com remoção dos íntrons antes da saída para o citoplasma]),
   ("E", [policistrônico, com um sítio de ligação do ribossomo próprio para cada cístron])))

#questao-ce("10", badge-consolidacao,
  [Julgue os itens sobre a pontuação da transcrição e os níveis de controle da expressão.],
  (("I",   [O sítio +1 corresponde ao primeiro nucleotídeo efetivamente transcrito.]),
   ("II",  [A numeração das posições do promotor inclui uma posição zero entre −1 e +1.]),
   ("III", [O terminador delimita o fim do transcrito, e não o fim de um gene isolado.]),
   ("IV",  [O controle pós-traducional atua sobre a proteína já sintetizada.])))

#questao-mc("11", badge-integracao,
  [Uma cepa de _E. coli_ teve o promotor lac substituído por uma versão idêntica à sequência consenso em −35 e −10, permanecendo intactos o operador, o gene lacI e o sítio CAP. Essa cepa é cultivada em meio com lactose e glicose, ambas abundantes. O resultado esperado para a transcrição de lacZ é:],
  (("A", [transcrição elevada, porque a alolactose retirou o repressor do operador e a afinidade da holoenzima pelo promotor consenso dispensa o reforço que a CAP daria com cAMP alto]),
   ("B", [transcrição nula, porque o promotor consenso deixa de ser reconhecido pela subunidade σ e a holoenzima não consegue mais se posicionar sobre a região reguladora do operon]),
   ("C", [transcrição basal, porque a glicose alta mantém o cAMP baixo e, sem CAP ligada ao seu sítio, nenhum promotor consegue iniciar acima do nível residual característico da repressão]),
   ("D", [transcrição nula, porque a glicose alta mantém o repressor LacI firmemente ligado ao operador e nenhuma modificação da sequência do promotor é capaz de deslocá-lo dali]),
   ("E", [transcrição elevada, porque a substituição do promotor abole a necessidade de indutor e o operon passa a ser constitutivo mesmo em meio sem qualquer fonte de lactose])))

#questao-mc("12", badge-integracao,
  [Considere uma cepa mutante cujo operador sofreu alteração que aumenta em muitas ordens de grandeza a afinidade pelo repressor, tornando a repressão praticamente absoluta. Essa cepa é transferida para meio sem glicose e com lactose como única fonte de carbono. O comportamento esperado é:],
  (("A", [indução normal, porque a lactose atravessa a membrana por difusão simples e se liga diretamente ao repressor, dispensando qualquer produto do próprio operon para iniciar o processo]),
   ("B", [indução mais lenta, porém completa, porque a CAP ativada pelo cAMP alto compensa integralmente o excesso de afinidade do repressor pelo operador e restaura a transcrição máxima]),
   ("C", [ausência de indução, porque sem transcrição basal não há permease nem β-galactosidase residuais, e sem elas a lactose não entra nem é convertida na alolactose que dissociaria o repressor]),
   ("D", [indução constitutiva, porque um operador com afinidade aumentada perde a capacidade de responder ao indutor e o operon passa a transcrever continuamente os três genes estruturais]),
   ("E", [ausência de indução, porque a repressão absoluta impede a transcrição do gene lacI e, sem repressor sintetizado, a maquinaria reguladora do operon deixa de existir por completo])))

#questao-ce("13", badge-integracao,
  [Julgue os itens sobre o comportamento genético dos elementos do operon em diploides parciais.],
  (("I",   [A mutação lacI⁻ é dominante no diploide parcial, porque o repressor defeituoso ocupa o operador da cópia selvagem.]),
   ("II",  [O operador O#super[c] mantém constitutiva a expressão da própria molécula mesmo com repressor selvagem disponível.]),
   ("III", [O alelo lacI#super[S] produz repressor incapaz de reconhecer o indutor, com fenótipo não induzível.]),
   ("IV",  [Elementos que atuam em cis são produtos gênicos difusíveis que alcançam qualquer cópia do sítio-alvo.])))

#questao-mc("14", badge-integracao,
  [Um repressor mutante liga-se ao operador com afinidade normal, mas o sítio localizado no core da proteína perdeu a capacidade de acomodar o indutor. Em meio com lactose abundante e sem glicose, o fenótipo dessa cepa e a razão mecanística são:],
  (("A", [constitutiva, porque a perda do sítio do indutor desestabiliza o tetrâmero, os dímeros se separam e os domínios hélice-volta-hélice deixam de encaixar simultaneamente no operador]),
   ("B", [constitutiva, porque a alolactose passa a competir diretamente com o DNA pelo domínio de ligação e ocupa o sítio do operador antes que o repressor consiga alcançá-lo]),
   ("C", [induzível normal, porque o excesso de alolactose no meio compensa a queda de afinidade e desloca o equilíbrio para a conformação incapaz de reconhecer a sequência do operador]),
   ("D", [não induzível, porque a alolactose formada não encontra sítio de ligação, o repressor mantém os dois domínios alinhados no sulco maior e a polimerase não escapa do promotor]),
   ("E", [não induzível, porque a mutação no core impede a transcrição do próprio gene lacI e a célula deixa de produzir qualquer proteína reguladora funcional para o operon])))

#questao-mc("15", badge-integracao,
  [Sobre o transcrito do operon lac e as proteínas dele derivadas, assinale a alternativa *incorreta*:],
  (("A", [um único evento de iniciação no promotor lac gera um mRNA que contém as sequências codificantes de lacZ, lacY e lacA em série]),
   ("B", [cada cístron do transcrito tem sítio de ligação do ribossomo próprio, de modo que as três proteínas são sintetizadas como cadeias independentes]),
   ("C", [a eficiência distinta desses sítios permite que as três proteínas apareçam em quantidades diferentes, ainda que venham do mesmo transcrito]),
   ("D", [a β-galactosidase atua tanto na hidrólise da lactose quanto na produção do isômero que funciona como indutor do próprio operon]),
   ("E", [o transcrito é traduzido em uma poliproteína única, posteriormente clivada por proteases que liberam a β-galactosidase, a permease e a transacetilase])))

#questao-ce("16", badge-integracao,
  [Julgue os itens sobre os efeitos da glicose sobre o operon lac.],
  (("I",   [A glicose reprime o operon ao se ligar diretamente ao repressor LacI e aumentar sua afinidade pelo operador.]),
   ("II",  [A entrada de glicose pelo sistema fosfotransferase mantém a EIIA#super[Glc] desfosforilada e reduz a estimulação da adenilato-ciclase.]),
   ("III", [A EIIA#super[Glc] desfosforilada inibe a permease LacY, reduzindo a entrada de lactose — a exclusão do indutor.]),
   ("IV",  [A repressão por catabólito age reduzindo a transcrição do gene lacI e a quantidade de repressor disponível.])))

#questao-mc("17", badge-integracao,
  [A justificativa mecanística para que a iniciação da transcrição seja o principal ponto de controle da expressão gênica em bactérias apoia-se em:],
  (("A", [na longa meia-vida do mRNA bacteriano, que torna qualquer intervenção posterior ineficaz e concentra toda a regulação possível na etapa de iniciação da síntese]),
   ("B", [na existência de envoltório nuclear, que separa transcrição e tradução e permite regular o transporte do transcrito antes que o ribossomo tenha acesso a ele]),
   ("C", [na meia-vida curta do mRNA somada à tradução acoplada à transcrição, de modo que interromper a iniciação derruba a concentração da proteína em poucos minutos]),
   ("D", [na ausência de mecanismos pós-traducionais em procariotos, o que deixa a iniciação da transcrição como a única etapa passível de regulação na célula bacteriana]),
   ("E", [no fato de a inibição alostérica de enzimas prontas ser mais lenta que a repressão transcricional, tornando o controle da largada também o mais rápido dos quatro])))

#questao-mc("18", badge-integracao,
  [No operon do triptofano, o acúmulo do aminoácido leva ao desligamento da via que o sintetiza. A classificação desse arranjo e o papel do triptofano são:],
  (("A", [regulação negativa repressível, com o triptofano atuando como co-repressor que ativa o repressor e o torna capaz de ocupar o operador]),
   ("B", [regulação negativa induzível, com o triptofano atuando como indutor que dissocia o repressor do operador e libera a transcrição dos genes]),
   ("C", [regulação positiva repressível, com o triptofano atuando como indutor que habilita o ativador a recrutar a RNA-polimerase para o promotor]),
   ("D", [regulação positiva induzível, com o triptofano atuando como co-repressor que remove o ativador do sítio e reduz a frequência de iniciação]),
   ("E", [regulação negativa repressível, com o triptofano atuando como indutor que se liga ao operador e impede fisicamente o acesso da polimerase])))

#questao-ce("19", badge-integracao,
  [Uma cepa selvagem é semeada em quatro meios contendo X-Gal, variando a presença de glicose e de IPTG. Julgue os itens sobre as colônias esperadas.],
  (("I",   [Em meio sem glicose e com IPTG, as colônias crescem azuis.]),
   ("II",  [Em meio com glicose e com IPTG, as colônias crescem intensamente azuis.]),
   ("III", [Em meio com glicose e sem IPTG, as colônias crescem azuis.]),
   ("IV",  [Em meio sem glicose e sem IPTG, as colônias crescem brancas.])))

#questao-mc("20", badge-integracao,
  [A sequência do operador lac é palindrômica. A explicação estrutural para essa propriedade está em que:],
  (("A", [a palindromia permite que a fita simples do operador se dobre sobre si mesma numa alça em grampo, que é a estrutura efetivamente reconhecida pelo repressor]),
   ("B", [a palindromia garante que a mesma sequência seja lida pela subunidade σ da polimerase e pelo repressor, o que faz os dois competirem pelo mesmo sítio de ligação]),
   ("C", [quem reconhece o operador é um dímero simétrico, com dois motivos hélice-volta-hélice que entram em voltas sucessivas do sulco maior e leem metades simétricas]),
   ("D", [a palindromia é exigência da replicação, porque só sequências simétricas conseguem ser duplicadas sem erro pela DNA-polimerase na região reguladora do operon]),
   ("E", [a simetria da sequência permite que o operador atue em trans, alcançando também a segunda molécula de DNA presente num diploide parcial de mesma origem])))

#questao-mc("21", badge-integracao,
  [O operon lac possui, além do operador principal, dois sítios operadores auxiliares. A consequência funcional dessa arquitetura é:],
  (("A", [os sítios auxiliares recrutam moléculas adicionais de RNA-polimerase e aumentam a taxa de iniciação quando o indutor está presente no meio de cultivo]),
   ("B", [a ocupação simultânea dos três sítios impede a ligação da CAP e explica por que o operon lac não responde à variação de cAMP quando o meio contém glicose]),
   ("C", [cada sítio auxiliar responde a um indutor diferente, o que permite ao operon distinguir a lactose da alolactose e de análogos como o IPTG usado em laboratório]),
   ("D", [os sítios auxiliares suprimem por completo a transcrição basal, o que torna a repressão absoluta e impede qualquer vazamento de β-galactosidase na ausência de lactose]),
   ("E", [um tetrâmero ocupa dois sítios ao mesmo tempo e dobra o DNA intermediário em alça, elevando a concentração local de repressor e aprofundando muito a repressão])))

#questao-ce("22", badge-integracao,
  [Julgue os itens sobre o reconhecimento do promotor pela RNA-polimerase bacteriana.],
  (("I",   [A subunidade σ reconhece as regiões −35 e −10 e converte o core em holoenzima seletiva.]),
   ("II",  [O core da enzima, sem fator σ associado, já distingue promotor de sequência de DNA qualquer.]),
   ("III", [Fatores σ alternativos redirecionam a mesma polimerase para conjuntos distintos de promotores.]),
   ("IV",  [O espaçamento de cerca de 17 pb entre −35 e −10 mantém os dois blocos na mesma face da hélice.])))

#questao-mc("23", badge-integracao,
  [Sobre a geometria dos sítios reguladores do operon lac e seus efeitos, assinale a alternativa *incorreta*:],
  (("A", [o sítio CAP situa-se à montante das regiões −35 e −10, em posição que permite o contato com o domínio C-terminal da subunidade α]),
   ("B", [o operador situa-se à jusante do promotor, sobrepondo o sítio de início da transcrição, de modo que o repressor bloqueia o escape da polimerase]),
   ("C", [a repressão é estérica: com o repressor ligado, a polimerase ainda ocupa o promotor, mas não consegue avançar para a fase de alongamento]),
   ("D", [a ativação pela CAP é estérica: a proteína ligada empurra fisicamente o repressor para fora do operador e assim libera a região de início]),
   ("E", [o ganho de transcrição promovido pela CAP vem da energia livre favorável de uma interação proteína–proteína, que compensa a fraqueza do promotor lac])))

#questao-mc("24", badge-integracao,
  [Cultivada em meio contendo glicose e lactose, uma população de _E. coli_ exibe curva de crescimento com duas fases separadas por um platô. A interpretação correta desse platô é:],
  (("A", [a lactose exerce efeito tóxico transitório sobre a população, e o platô corresponde ao tempo necessário para que as células neutralizem o dissacarídeo acumulado]),
   ("B", [o platô demonstra que a bactéria é incapaz de utilizar a lactose como fonte de carbono e só retoma o crescimento quando surge glicose residual no meio]),
   ("C", [o platô corresponde ao intervalo em que a glicose se esgota, o cAMP sobe, a CAP se liga ao seu sítio e as enzimas do operon lac são sintetizadas do zero]),
   ("D", [o platô resulta da queda de pH provocada pela fermentação da glicose, e o crescimento retoma quando os sistemas de tamponamento restauram o meio]),
   ("E", [as duas fases correspondem ao consumo simultâneo dos dois açúcares, e o platô marca o momento em que o operon lac é definitivamente reprimido pela CAP])))

#questao-ce("25", badge-integracao,
  [Julgue os itens sobre o alelo lacI#super[S] e a estrutura quaternária do repressor.],
  (("I",   [O alelo lacI#super[S] é recessivo, já que a cópia selvagem produz repressor funcional suficiente.]),
   ("II",  [O repressor lacI#super[S] perdeu a capacidade de se ligar ao operador, e por isso o fenótipo é constitutivo.]),
   ("III", [As subunidades mutantes se misturam às selvagens ao formar tetrâmeros, o que explica o efeito dominante-negativo.]),
   ("IV",  [O repressor selvagem é um tetrâmero organizado como dois dímeros unidos por um domínio de tetramerização.])))

#questao-mc("26", badge-aplicacao,
  [Um laboratório produz insulina humana recombinante em _E. coli_, com o gene da insulina sob controle do promotor lac. A cultura cresce até alta densidade e só então recebe o indutor. A razão para se usar IPTG, e não lactose, nessa etapa é:],
  (("A", [a lactose é tóxica para _E. coli_ em alta densidade celular e provocaria lise da cultura antes que a proteína recombinante fosse acumulada em quantidade útil]),
   ("B", [o IPTG não é hidrolisado pela β-galactosidase, e sua concentração se mantém estável ao longo do cultivo, sustentando indução constante até o fim da produção]),
   ("C", [o IPTG eleva diretamente o cAMP intracelular e ativa a CAP, o que dispensa a retirada da glicose do meio de cultivo durante a fase de produção da proteína]),
   ("D", [a lactose se liga ao operador e não ao repressor, de modo que a indução por lactose exigiria concentrações inviáveis em escala industrial de fermentação]),
   ("E", [o IPTG inativa de forma irreversível o repressor LacI, o que torna a linhagem constitutiva e dispensa novas adições de indutor em lotes subsequentes])))

#questao-mc("27", badge-aplicacao,
  [Numa clonagem, o fragmento de DNA de interesse é inserido dentro do gene lacZ de um plasmídeo, e as bactérias transformadas crescem em meio com X-Gal e IPTG. A leitura correta das colônias é:],
  (("A", [colônias brancas carregam o inserto, porque a interrupção de lacZ abole a β-galactosidase e o X-Gal deixa de ser clivado em pigmento azul]),
   ("B", [colônias azuis carregam o inserto, porque a interrupção de lacZ desvia a via metabólica para a produção do pigmento a partir do substrato cromogênico]),
   ("C", [colônias brancas não receberam plasmídeo algum, e as azuis correspondem indistintamente a plasmídeos com e sem o fragmento de interesse inserido]),
   ("D", [a cor não distingue os clones, porque o IPTG induz a expressão de lacZ mesmo quando o gene teve sua sequência codificante interrompida pelo inserto]),
   ("E", [colônias azuis não receberam plasmídeo, uma vez que apenas o cromossomo bacteriano contém uma cópia funcional do gene da β-galactosidase])))

#questao-ce("28", badge-aplicacao,
  [Um isolado de enterobactéria é reportado como sensível a uma cefalosporina no antibiograma inicial. Após quatro dias de tratamento, o paciente piora e nova cultura mostra o mesmo isolado agora resistente. A cepa carrega um gene de β-lactamase sob controle de um operon reprimido. Julgue os itens.],
  (("I",   [Fragmentos de parede celular gerados pela ação do β-lactâmico podem funcionar como indutores desse operon.]),
   ("II",  [A resistência observada exige necessariamente o surgimento de uma mutação nova durante o tratamento.]),
   ("III", [O fenômeno exige a aquisição de um gene novo de resistência por transferência horizontal durante o tratamento.]),
   ("IV",  [Trata-se de arranjo análogo ao do operon lac, com sítio operador em cis e repressor difusível em trans.])))

#questao-mc("29", badge-aplicacao,
  [Uma _E. coli_ uropatogênica alcança a urina de um paciente diabético descompensado, meio rico em glicose e pobre em lactose. Considerando apenas a regulação do operon lac, o estado transcricional esperado desse operon e sua justificativa são:],
  (("A", [transcrição máxima, porque a alta oferta de glicose eleva o cAMP e a CAP ligada ao seu sítio recruta a polimerase para o promotor lac com eficiência]),
   ("B", [transcrição basal, porque o repressor permanece no operador na ausência de alolactose e, além disso, a glicose alta mantém o cAMP baixo e a CAP inativa]),
   ("C", [transcrição basal, porque a glicose atua como co-repressor do operon lac e ativa diretamente o repressor LacI, que passa a ocupar o operador com afinidade máxima]),
   ("D", [transcrição máxima, porque o ambiente urinário desreprime constitutivamente operons catabólicos e dispensa a presença do indutor específico de cada via]),
   ("E", [transcrição intermediária, porque a ausência de lactose libera o operador e a presença de glicose mantém a CAP ligada, resultando em ativação parcial do promotor])))

#questao-ce("30", badge-aplicacao,
  [Num experimento de bancada, uma cepa com genótipo lacI⁺ P⁺ O#super[c] Z⁺ recebe por conjugação um plasmídeo lacI⁻ P⁺ O⁺ Z⁺. A cultura é dividida em dois frascos, um com IPTG e outro sem. Julgue os itens sobre a produção de β-galactosidase.],
  (("I",   [No frasco sem IPTG haverá produção de β-galactosidase, proveniente da cópia cromossômica com O#super[c].]),
   ("II",  [No frasco com IPTG a produção aumenta, porque a cópia plasmidial também passa a ser transcrita.]),
   ("III", [A cópia plasmidial, por ser lacI⁻, é constitutiva mesmo sem IPTG, já que não há repressor na célula.]),
   ("IV",  [O genótipo O#super[c] confere efeito dominante e de atuação restrita à própria molécula de DNA.])))
