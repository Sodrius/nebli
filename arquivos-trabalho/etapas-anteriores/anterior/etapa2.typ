#import "../typst-template/nebli_v2_apostila.typ": *

// ───────────────────────── CONSOLIDAÇÃO Q01-Q10 ─────────────────────────

#questao-mc("01", badge-consolidacao,
  [Meselson e Stahl marcaram o DNA de _E. coli_ com nitrogênio pesado (¹⁵N) e, após uma geração em meio com ¹⁴N, analisaram a densidade do DNA em gradiente de CsCl. O resultado comprovou qual modelo de replicação?],
  (("A", [Dispersiva — o ¹⁵N foi distribuído aleatoriamente entre todos os fragmentos de ambas as fitas filhas.]),
   ("B", [Semiconservativa — cada dupla-hélice filha possui uma fita parental intacta e uma fita nova recém-sintetizada.]),
   ("C", [Conservativa — uma das hélices filhas reteve ambas as fitas parentais enquanto a outra era inteiramente nova.]),
   ("D", [Híbrida — metade dos fragmentos continha somente ¹⁵N e a outra metade somente ¹⁴N após a primeira divisão.]),
   ("E", [Aleatória — a incorporação de ¹⁵N e ¹⁴N variou conforme a temperatura de incubação no gradiente de CsCl.])))

#questao-mc("02", badge-consolidacao,
  [A replicação do DNA bacteriano começa em uma sequência específica chamada oriC. Por que essa sequência está enriquecida em pares A=T em comparação com outras regiões do cromossomo?],
  (("A", [Pares A=T possuem três pontes de hidrogênio, tornando a separação das fitas mais eficiente quando catalisada pela helicase.]),
   ("B", [Pares A=T são reconhecidos especificamente pelas proteínas DnaA, que só se ligam a adeninas e timinas na dupla-hélice bacteriana.]),
   ("C", [Pares A=T possuem apenas duas pontes de hidrogênio, exigindo menor energia para fundir as fitas e iniciar a abertura da forquilha.]),
   ("D", [Pares A=T aumentam a estabilidade da região de origem, evitando que a girase clive o esqueleto fosfodiéster na região inicial.]),
   ("E", [Pares A=T facilitam o reconhecimento das proteínas SSB, que só se fixam em adeninas livres após a desnaturação parcial local.])))

#questao-mc("03", badge-consolidacao,
  [A helicase bacteriana (DnaB) catalisa a separação das fitas da dupla-hélice durante a replicação. Qual é o mecanismo molecular pelo qual ela realiza esse trabalho?],
  (("A", [Cliva covalentemente o esqueleto fosfodiéster de uma das fitas, permitindo que a outra se desenrole espontaneamente pelo relaxamento da tensão.]),
   ("B", [Liga-se ao sulco menor da dupla-hélice e intercala-se entre as bases, rompendo o empilhamento hidrofóbico que sustenta a estrutura B.]),
   ("C", [Hidrolisa ATP para translocar ao longo de uma das fitas, quebrando ativamente as pontes de hidrogênio entre bases complementares.]),
   ("D", [Catalisa a ligação de moléculas de água às pontes de hidrogênio, convertendo a energia de hidratação em trabalho mecânico de abertura.]),
   ("E", [Remove histonas do DNA compactado para expor a dupla-hélice, facilitando a ação subsequente das topoisomerases de tipo II na região.])))

#questao-mc("04", badge-consolidacao,
  [A DNA-Polimerase I de _E. coli_ possui três sítios ativos funcionalmente distintos. Qual deles é responsável pela correção de erros durante a própria síntese de DNA?],
  (("A", [A atividade exonuclease 3′→5′, que remove o nucleotídeo recém-incorporado caso ele forme um par de bases incorreto com o molde.]),
   ("B", [A atividade exonuclease 5′→3′, que degrada a fita molde à frente da polimerase, expondo novas bases para incorporação imediata.]),
   ("C", [A atividade de polimerização 5′→3′, que verifica o complemento antes de catalisar a ligação fosfodiéster no extremo 3′-OH livre.]),
   ("D", [Um sítio de edição alostérico separado dos outros dois que só atua quando a taxa de erro ultrapassa um limiar interno de fidelidade.]),
   ("E", [A atividade de ligase intrínseca, que refaz as ligações fosfodiéster após detectar um mismatch na fita recém-sintetizada adjacente.])))

#questao-ce("05", badge-consolidacao,
  [Sobre a síntese do primer de RNA durante a replicação bacteriana, avalie cada afirmativa como Correta (C) ou Errada (E):],
  (("I", [A primase é uma RNA-polimerase que sintetiza um segmento curto de RNA (~10 nucleotídeos) complementar ao molde de DNA.]),
   ("II", [A primase pertence à família das DNA-polimerases e usa desoxirribonucleotídeos, mas pode iniciar a síntese sem 3′-OH prévio.]),
   ("III", [A DNA-Polimerase III consegue iniciar a síntese de nova cadeia diretamente no DNA molde sem necessitar de um primer pré-formado.]),
   ("IV", [Após a replicação, a DNA-Polimerase I remove o primer de RNA usando sua atividade exonuclease 5′→3′ e preenche a lacuna com DNA.])))

#questao-mc("06", badge-consolidacao,
  [A DNA-Polimerase III possui alta processividade, sintetizando o cromossomo bacteriano inteiro sem se dissociar do molde. Qual estrutura molecular é a principal responsável por essa característica?],
  (("A", [O núcleo catalítico α-ε-θ forma ligações covalentes temporárias com o DNA molde, impedindo a dissociação até o término da replicação.]),
   ("B", [O fator σ da holoenizema reconhece sequências repetidas ao longo do cromossomo e ancora a polimerase a cada passo de extensão.]),
   ("C", [Uma subunidade hidrofóbica do núcleo catalítico intercala-se entre as bases do DNA molde e funciona como âncora molecular permanente.]),
   ("D", [O grampo deslizante β₂ forma um anel toroidal em torno da dupla-hélice, conectado ao núcleo catalítico pelo complexo γ e mantendo a enzima ancorada.]),
   ("E", [O segmento τ da holoenizema forma uma alça de 20 nt no molde que funciona como âncora estrutural, reduzindo a frequência de dissociação.])))

#questao-mc("07", badge-consolidacao,
  [Os fragmentos de Okazaki surgem porque a síntese de DNA só ocorre no sentido 5′→3′, mas as duas fitas molde são antiparalelas. Qual das opções descreve corretamente a consequência direta dessa restrição?],
  (("A", [A fita líder é sintetizada descontinuamente, com cada fragmento exigindo um novo primer, pois o molde corre no sentido 5′→3′ da forquilha.]),
   ("B", [A fita retardada é sintetizada em fragmentos curtos (Okazaki), cada um com seu próprio primer, porque o molde corre no sentido 5′→3′ da forquilha.]),
   ("C", [Ambas as fitas são sintetizadas continuamente, porém em sentidos opostos, e os fragmentos resultam apenas de pausas da polimerase por falta de dNTPs.]),
   ("D", [A fita retardada é sintetizada apenas uma vez, na direção oposta à abertura da forquilha, usando a exonuclease 5′→3′ como motor direcional.]),
   ("E", [Os fragmentos de Okazaki surgem exclusivamente em eucariotos, pois a cromatina impede a síntese contínua da fita retardada nas bactérias.])))

#questao-ce("08", badge-consolidacao,
  [Sobre a atividade de proofreading (revisão) da DNA-Polimerase I e III de _E. coli_, avalie cada afirmativa:],
  (("I", [A atividade exonuclease 5′→3′ é a principal responsável pelo proofreading, removendo nucleotídeos mal pareados logo após a incorporação.]),
   ("II", [A atividade exonuclease 3′→5′ catalisa a remoção do nucleotídeo recém-inserido se ele estiver mal pareado com a base do molde.]),
   ("III", [O proofreading ocorre sem dissociação da polimerase do molde, pois o sítio exonuclease 3′→5′ fica na mesma molécula que o sítio de polimerização.]),
   ("IV", [Somente a atividade de polimerização 5′→3′ está disponível para corrigir erros; não há sítio exonuclease dedicado ao proofreading.])))

#questao-mc("09", badge-consolidacao,
  [À medida que a helicase abre a forquilha, o DNA à frente acumula superenrolamento positivo. Qual enzima alivia essa tensão torsional e como ela age?],
  (("A", [A helicase II (UvrD) desfaz o superenrolamento translocando na direção oposta e absorvendo a torção gerada pela helicase principal.]),
   ("B", [A SSB (proteína de ligação a fita simples) absorve a tensão torsional ao se ligar ao sulco maior do DNA à frente da forquilha aberta.]),
   ("C", [A DNA girase (topoisomerase II bacteriana) cliva transitoriamente a dupla-fita, passa um segmento pelo corte e religa, aliviando o superenrolamento positivo.]),
   ("D", [A DNA ligase usa energia de NAD⁺ para introduzir quebras duplas controladas à frente da forquilha, revertendo o superenrolamento acumulado.]),
   ("E", [A primase alivia a tensão ao sintetizar segmentos de RNA que deslocam fisicamente a torção acumulada para a extremidade do cromossomo.])))

#questao-mc("10", badge-consolidacao,
  [Na replicação bidirecional do DNA bacteriano, duas forquilhas partem do oriC em sentidos opostos. Como essa replicação termina?],
  (("A", [As duas forquilhas param ao atingir sequências terminadoras codificadas em lados opostos do cromossomo, onde helicases especializadas as dissociam.]),
   ("B", [Uma das forquilhas para quando detecta falta de dNTPs, enquanto a outra continua até ligar-se à primeira pela DNA ligase no ponto de encontro.]),
   ("C", [A replicação termina quando a Pol III de cada forquilha encontra a extremidade livre do cromossomo linear bacteriano e cai por falta de molde.]),
   ("D", [As duas forquilhas avançam em sentidos opostos e se encontram do lado oposto ao oriC, onde as ligases selam os nicks residuais restantes.]),
   ("E", [A replicação termina quando as duas forquilhas atingem regiões Ter, que bloqueiam o avanço de uma delas e permitem à outra completar a síntese.])))

// ───────────────────────── INTEGRAÇÃO Q11-Q25 ─────────────────────────

#questao-mc("11", badge-integracao,
  [As proteínas SSB estabilizam as fitas simples geradas pela helicase durante a abertura da forquilha. Qual é o impacto direto das SSBs sobre a eficiência global da helicase?],
  (("A", [As SSBs aumentam a eficiência da helicase ao impedir o re-anelamento das fitas separadas, mantendo o substrato de fita simples disponível para progressão.]),
   ("B", [As SSBs reduzem a eficiência da helicase ao competir pelo mesmo sítio de ligação no sulco menor e bloquear parcialmente a translocação enzimática.]),
   ("C", [As SSBs são redundantes em bactérias, pois a girase já impede o re-anelamento ao manter o DNA em estado superenrolado negativo à frente da forquilha.]),
   ("D", [As SSBs aumentam a especificidade da helicase ao sinalizar quimicamente quais regiões do DNA devem ser abertas com prioridade na forquilha ativa.]),
   ("E", [As SSBs reduzem a necessidade de ATP pela helicase ao realizarem parte do trabalho de separação usando energia de ligação cooperativa às fitas expostas.])))

#questao-mc("12", badge-integracao,
  [O oriC é rico em pares A=T, enquanto a maioria do cromossomo bacteriano é mais rico em G≡C. Qual princípio termodinâmico explica por que essa composição favorece o início da replicação?],
  (("A", [Pares G≡C formam duas pontes de hidrogênio e, por isso, têm menor entalpia de fusão; a célula aproveita essa instabilidade para iniciar a replicação no oriC.]),
   ("B", [Pares A=T interagem por forças de van der Waals mais intensas do que G≡C, mas a célula compensa com hidrólise adicional de ATP pela helicase no oriC.]),
   ("C", [Pares G≡C se acumulam em regiões de alta expressão gênica; o oriC evita esses pares para não atrapalhar a RNA-polimerase durante a transcrição paralela.]),
   ("D", [Pares A=T formam duas pontes de hidrogênio, enquanto G≡C formam três; regiões ricas em A=T têm menor temperatura de fusão e separam mais facilmente as fitas.])))

#questao-ce("13", badge-integracao,
  [A divisão de trabalho entre a DNA-Polimerase I e a DNA-Polimerase III é essencial para completar a replicação bacteriana. Avalie cada afirmativa:],
  (("I", [A Pol III é a principal polimerase replicativa e depende da Pol I para remover os primers de RNA e preencher os gaps resultantes com DNA.]),
   ("II", [A Pol I pode substituir completamente a Pol III na replicação do cromossomo, pois também possui velocidade de polimerização de 1.000 nt/s.]),
   ("III", [A Pol III pode remover seus próprios primers de RNA usando sua atividade exonuclease 5′→3′ intrínseca, dispensando a Pol I para essa etapa.]),
   ("IV", [Após a Pol I preencher os gaps, a DNA ligase sela o nick residual usando NAD⁺ como fonte de energia nas bactérias, completando o fragmento.])))

#questao-mc("14", badge-integracao,
  [A antiparalelidade da dupla-hélice, combinada com a restrição de síntese no sentido 5′→3′, obriga a célula a usar um mecanismo especial na fita retardada. Qual é a consequência funcional direta dessa combinação?],
  (("A", [A fita retardada precisa de uma helicase dedicada que opere no sentido inverso, pois a helicase principal só abre o molde da fita líder no oriC.]),
   ("B", [A fita retardada exige a inversão temporária do sentido de síntese para 3′→5′, realizada por uma subunidade especial da Pol III denominada ε.]),
   ("C", [A síntese da fita retardada ocorre em direção oposta ao avanço da forquilha, formando fragmentos de Okazaki que serão unidos depois pela DNA ligase.]),
   ("D", [A fita retardada é sintetizada pela RNA-polimerase em comprimento total e depois convertida em DNA por uma transcriptase reversa associada ao replichore.]),
   ("E", [A antiparalelidade obriga a célula a aguardar o término da fita líder para então sintetizar a retardada inteira no sentido correto a partir do oriC.])))

#questao-mc("15", badge-integracao,
  [A telomerase possui uma subunidade de RNA (hTR) que serve de molde para estender os telômeros. Qual é a relação entre essa atividade e a imortalização de células tumorais?],
  (("A", [Tumores reativam a telomerase para encurtar deliberadamente os telômeros, desencadeando apoptose das células vizinhas e permitindo invasão tecidual.]),
   ("B", [Tumores que reativam a telomerase superam o limite de Hayflick ao estender os telômeros a cada divisão, evitando a senescência replicativa e tornando-se imortais.]),
   ("C", [Células somáticas normais expressam telomerase constitutivamente; em tumores, a enzima é inibida, levando ao encurtamento acelerado e instabilidade genômica.]),
   ("D", [A telomerase adiciona sequências codificantes nos telômeros, aumentando o número de genes disponíveis e acelerando a proliferação tumoral independente dos fatores de crescimento.]),
   ("E", [A imortalização tumoral ocorre porque a telomerase fosforila o p53, inativando o principal supressor tumoral e acelerando a progressão do ciclo celular.])))

#questao-ce("16", badge-integracao,
  [A fidelidade global da replicação bacteriana é da ordem de 1 erro em 10⁹–10¹⁰ nucleotídeos incorporados. Avalie quais mecanismos contribuem para essa precisão extraordinária:],
  (("I", [A atividade exonuclease 5′→3′ da Pol III realiza o proofreading cotejando o nucleotídeo recém-inserido com a base do molde à frente da síntese.]),
   ("II", [A atividade exonuclease 3′→5′ da Pol III corrige erros logo após a inserção, removendo o nucleotídeo mal pareado na extremidade 3′ da cadeia nascente.]),
   ("III", [Sistemas de reparo pós-replicativo, como o mismatch repair, detectam e corrigem erros remanescentes após a conclusão da replicação da forquilha.]),
   ("IV", [A seleção do nucleotídeo correto pela geometria do sítio ativo da polimerase é suficiente por si só para atingir 1 erro em 10⁹, sem necessidade de proofreading.])))

#questao-mc("17", badge-integracao,
  [O grampo deslizante β₂ da DNA-Polimerase III envolve topologicamente a dupla-hélice em forma de anel. De que maneira essa arquitetura garante a alta processividade da enzima?],
  (("A", [O anel β₂ forma ligações covalentes com o sulco maior da hélice, sendo liberado apenas por proteases específicas ativadas ao final da replicação cromossômica.]),
   ("B", [O anel β₂ bloqueia fisicamente a saída do molde do canal catalítico, forçando a polimerase a manter contato com o DNA enquanto desliza ao longo da fita.]),
   ("C", [O anel β₂ hidrolisa ATP de forma contínua para empurrar ativamente a polimerase ao longo do molde, impedindo a retrodifusão da enzima para o ponto de origem.]),
   ("D", [O anel β₂ recruta fatores de processividade auxiliares que formam uma gaiola proteica ao redor do complexo polimerase–DNA durante toda a síntese.]),
   ("E", [O anel β₂ encircla topologicamente a dupla-hélice sem ligação covalente, sendo incapaz de se dissociar lateralmente e mantendo a polimerase ancorada ao molde.])))

#questao-mc("18", badge-integracao,
  [A DNA ligase sela o nick residual após a Pol I preencher os gaps dos fragmentos de Okazaki. Qual diferença no cofator energético distingue a ligase bacteriana da eucariota e o que ela revela sobre a origem evolutiva dessas enzimas?],
  (("A", [A ligase bacteriana usa NAD⁺ como doador de adenilato, enquanto a ligase eucariota usa ATP; essa diferença sugere que as duas enzimas evoluíram independentemente ou divergiram cedo de um ancestral comum.]),
   ("B", [A ligase bacteriana usa ATP como doador de adenilato, enquanto a eucariota usa NAD⁺; a inversão de cofatores resultou da pressão seletiva imposta pela resposta ao dano de DNA nos eucariontes.]),
   ("C", [Tanto bactérias quanto eucariotos usam ATP, mas a bactéria também pode usar NAD⁺ como alternativa quando os níveis de ATP caem abaixo do limiar de saturação enzimática.]),
   ("D", [A ligase bacteriana usa GTP como cofator derivado do ciclo de Krebs; a eucariota usa ATP; a diferença reflete a compartimentalização mitocondrial da síntese de GTP nos eucariontes.])))

#questao-ce("19", badge-integracao,
  [Os eucariotos apresentam características distintas de replicação em comparação com as bactérias. Avalie cada afirmativa:],
  (("I", [O genoma eucarioto possui centenas de origens de replicação ativas simultaneamente, reduzindo o tempo necessário para duplicar os ~3 bilhões de pb.]),
   ("II", [Eucariotos possuem uma única origem de replicação por cromossomo, análoga ao oriC bacteriano, e a replicação procede bidirecionalmente a partir dela.]),
   ("III", [O PCNA é uma proteína do nucléolo que organiza o rRNA ribossômico; não tem relação com a replicação do DNA cromossômico em eucariotos.]),
   ("IV", [A Pol δ e a Pol ε replicam o DNA nos dois lados da forquilha eucariota, ancoradas ao molde pelo PCNA, equivalente funcional do grampo β₂ bacteriano.])))

#questao-mc("20", badge-integracao,
  [A DNA-Polimerase I remove os primers de RNA dos fragmentos de Okazaki usando sua atividade exonuclease 5′→3′ e simultaneamente preenche a lacuna. Como se chama esse processo e por que ele exige atividade exonuclease 5′→3′ e não 3′→5′?],
  (("A", [Chama-se nick rotation; a direção 5′→3′ é necessária porque os primers de RNA ficam na extremidade 3′ de cada fragmento, e só a exo 3′→5′ poderia removê-los.]),
   ("B", [Chama-se nick sealing; a direção 3′→5′ permite que a polimerase remova o primer enquanto avança na direção contrária ao crescimento da nova cadeia.]),
   ("C", [Chama-se nick translation; a direção 5′→3′ permite que a exonuclease degrada o RNA à frente enquanto a polimerase sintetiza DNA por trás, deslocando o nick.]),
   ("D", [Chama-se gap repair; a exo 5′→3′ atua exclusivamente no reparo por excisão de nucleotídeos e não é usada para remover primers durante a replicação normal.]),
   ("E", [Chama-se strand displacement; a polimerase empurra o primer intacto à frente sem degradá-lo e uma endonuclease separada cliva o RNA deslocado posteriormente.])))

#questao-mc("21", badge-integracao,
  [A primase é classificada como RNA-polimerase, e não como DNA-polimerase. Qual propriedade bioquímica fundamental da primase explica por que DNA-polimerases não podem iniciar a síntese sem ela?],
  (("A", [A primase usa ribonucleotídeos e consegue iniciar a síntese de uma nova cadeia sem precisar de extremidade 3′-OH livre, suprindo o sítio de início para a DNA-polimerase.]),
   ("B", [A primase possui atividade exonuclease 3′→5′ muito mais potente que a DNA-polimerase, permitindo-lhe corrigir o início da cadeia antes de passá-la à Pol III.]),
   ("C", [A primase reconhece o oriC com muito maior afinidade que a Pol III, por isso só ela consegue se ligar ao molde na região de abertura inicial da forquilha bacteriana.]),
   ("D", [A primase usa desoxirribonucleotídeos como a Pol III, mas possui domínio helicase próprio que lhe permite abrir uma bolha local sem necessitar de DnaB.]),
   ("E", [A primase é recrutada pelo grampo β₂ diretamente, pois possui domínio de interação específico com o anel toroidal ausente em todas as DNA-polimerases bacterianas.])))

#questao-ce("22", badge-integracao,
  [A síntese das fitas líder e retardada ocorre simultaneamente na forquilha, mas com dinâmicas diferentes. Avalie cada afirmativa sobre fidelidade e mecanismo:],
  (("I", [A fita retardada é sintetizada continuamente como a líder, porém no sentido contrário ao avanço da forquilha, sem necessidade de primers adicionais.]),
   ("II", [A fita líder exige um único primer inicial no oriC, enquanto a fita retardada exige um novo primer para cada fragmento de Okazaki ao longo de todo o cromossomo.]),
   ("III", [A Pol III holoenzima atua como dímero assimétrico, sintetizando simultaneamente as duas fitas e aplicando proofreading 3′→5′ em ambas durante a extensão.]),
   ("IV", [A fita retardada acumula mais erros de replicação do que a líder porque não possui atividade de proofreading associada à síntese dos fragmentos de Okazaki.])))

#questao-mc("23", badge-integracao,
  [A Pol I sintetiza DNA a ~100 nt/s e tem baixa processividade, enquanto a Pol III opera a ~1.000 nt/s com altíssima processividade. O que essa diferença quantitativa revela sobre a divisão de trabalho entre elas?],
  (("A", [A Pol I é mais rápida e precisa, por isso é responsável por replicar a maior parte do cromossomo; a Pol III atua apenas no reparo e na remoção de primers.]),
   ("B", [As duas polimerases têm velocidades equivalentes na prática, pois a diferença de 10× é compensada pelo maior número de moléculas de Pol I disponíveis por célula.]),
   ("C", [A Pol III replica o cromossomo inteiro com velocidade e processividade altas; a Pol I cobre apenas gaps curtos após a remoção do primer, onde sua baixa velocidade e processividade são suficientes.]),
   ("D", [A Pol I realiza a replicação da fita líder de forma rápida; a Pol III cobre a fita retardada de forma fragmentada, compensando sua menor velocidade com o grampo β₂.]),
   ("E", [A diferença de velocidade permite que a Pol I termine o proofreading antes que a Pol III chegue ao mesmo segmento, evitando competição entre as duas enzimas pelo molde.])))

#questao-mc("24", badge-integracao,
  [O oriC é uma sequência específica de ~245 pb em _E. coli_. Qual categoria de proteínas reconhece essa sequência e deflagra o início da replicação?],
  (("A", [Proteínas iniciadoras, como a DnaA, ligam-se especificamente às caixas DnaA dentro do oriC e recrutam a helicase DnaB para fundir as fitas na região AT-rich.]),
   ("B", [As SSBs reconhecem o oriC por terem afinidade preferencial por regiões ricas em AT; sua ligação causa a fusão das fitas e recruta a helicase para a forquilha inicial.]),
   ("C", [A DNA-Pol III reconhece o oriC diretamente por seu domínio τ, que tem alta afinidade pelas caixas repetidas da sequência iniciadora bacteriana.]),
   ("D", [A primase reconhece o oriC pela sequência de consenso 5′-TTATCCACA-3′ e inicia a síntese de RNA antes mesmo da abertura completa da dupla-hélice local.])))

#questao-mc("25", badge-integracao,
  [No experimento de Meselson e Stahl, após a primeira geração em meio com ¹⁴N, todo o DNA formou uma única banda de densidade intermediária no gradiente de CsCl. Por que esse resultado elimina o modelo conservativo de replicação?],
  (("A", [O modelo conservativo previa duas bandas — uma pesada (parental intacta) e uma leve (totalmente nova) — após a primeira geração; a banda única intermediária observada é incompatível com essa previsão.]),
   ("B", [O modelo conservativo previa que todo o DNA seria pesado na primeira geração; a banda intermediária mostra que os nucleotídeos foram misturados aleatoriamente entre as fitas.]),
   ("C", [O modelo conservativo previa uma única banda pesada na primeira geração; a banda intermediária observada prova que cada fita nova incorpora exatamente metade de ¹⁵N e metade de ¹⁴N.]),
   ("D", [O modelo conservativo era compatível com a banda única intermediária; o experimento eliminou o modelo dispersivo, que previa bandas espalhadas ao longo de toda a densidade do gradiente.]),
   ("E", [O resultado só elimina o modelo dispersivo, pois a banda intermediária é perfeitamente compatível com o modelo conservativo quando a temperatura de centrifugação é corrigida.])))

// ───────────────────────── APLICAÇÃO Q26-Q30 ─────────────────────────

#questao-mc("26", badge-aplicacao,
  [A citarabina (AraC) é um análogo de nucleosídeo usado em quimioterapia. Ela inibe a DNA-polimerase ao ser incorporada à cadeia nascente, mas bloqueia seletivamente as células cancerosas. Qual característica diferencial das células tumorais explica essa seletividade clínica?],
  (("A", [Células tumorais expressam isoformas mutantes de DNA-polimerase com menor capacidade de proofreading, tornando-as mais suscetíveis à incorporação de análogos.]),
   ("B", [Células tumorais acumulam AraC em maior concentração intracelular por superexpressarem transportadores de nucleosídeos que normalmente estão ausentes nas células normais.]),
   ("C", [Células tumorais se dividem mais ativamente do que as células normais vizinhas, replicando DNA com maior frequência e incorporando o análogo em proporção muito maior.]),
   ("D", [Células tumorais expressam uma DNA ligase mutante que não consegue discriminar AraC do desoxicitidina, incorporando-o nas junções dos fragmentos de Okazaki.]),
   ("E", [Células tumorais possuem maior concentração de SSBs, que estabilizam preferencialmente a cadeia com AraC e impedem a atividade de proofreading da polimerase.])))

#questao-ce("27", badge-aplicacao,
  [As fluoroquinolonas (ciprofloxacino, levofloxacino) são antibióticos amplamente usados na clínica. Avalie cada afirmativa sobre seu mecanismo de ação:],
  (("I", [As fluoroquinolonas inibem a DNA girase bacteriana aprisionando o complexo enzima–DNA no estado de fita cortada, acumulando quebras de dupla-fita letais.]),
   ("II", [A seletividade das fluoroquinolonas para bactérias em relação às células humanas se deve exclusivamente à maior concentração intracelular do fármaco nas bactérias.]),
   ("III", [As fluoroquinolonas inibem as SSBs bacterianas, impedindo a estabilização da fita simples e levando ao colapso da forquilha de replicação em divisão ativa.]),
   ("IV", [A girase bacteriana e a topoisomerase II humana têm estruturas diferentes; por isso as fluoroquinolonas inibem seletivamente a enzima bacteriana com baixa toxicidade às células do hospedeiro.])))

#questao-mc("28", badge-aplicacao,
  [Inibidores de telomerase estão em investigação como estratégia antineoplásica. Por que células tumorais são mais vulneráveis a esses inibidores do que a maioria das células somáticas normais?],
  (("A", [Células somáticas normais dependem da telomerase para manter a integridade dos centrômeros; bloqueá-la causaria perda cromossômica igualmente grave em todas as células.]),
   ("B", [Células tumorais reativam a telomerase para superar o limite de Hayflick; sem a enzima, os telômeros encurtam a cada divisão até atingir comprimento crítico, desencadeando senescência ou apoptose.]),
   ("C", [Células tumorais possuem telômeros muito mais longos que as células normais; a inibição da telomerase encurta rapidamente esses telômeros extras sem afetar as células com telômeros normais.]),
   ("D", [Células somáticas normais expressam uma isoforma diferente de telomerase resistente aos inibidores; somente a isoforma tumoral, codificada pelo oncogene hTERT mutado, é sensível ao bloqueio.]),
   ("E", [Células tumorais dependem da telomerase para reparar danos oxidativos no DNA telomérico; sem a enzima, o acúmulo de oxidação paralisa a replicação antes mesmo do encurtamento crítico.])))

#questao-mc("29", badge-aplicacao,
  [O PCNA é detectado imunoistoquimicamente em biópsias tumorais como marcador de proliferação celular. Qual propriedade molecular do PCNA justifica seu uso como indicador de atividade replicativa?],
  (("A", [O PCNA é uma histona variante expressa exclusivamente durante a fase G2/M do ciclo celular, e sua detecção indica que a célula já completou a replicação do DNA.]),
   ("B", [O PCNA é um componente estrutural do nucléolo presente em todas as células; seu aumento em tumores indica apenas aumento do volume nuclear, não da atividade replicativa.]),
   ("C", [O PCNA é um inibidor de CDK que se acumula na fase S para frear o ciclo celular enquanto a replicação transcorre; sua detecção indica estresse replicativo, não proliferação.]),
   ("D", [O PCNA é o grampo deslizante eucarioto que ancora a Pol δ/ε durante a replicação; sua síntese aumenta na fase S e o detectar em tecido indica células com DNA em replicação ativa.]),
   ("E", [O PCNA é exclusivo de células-tronco e sua presença em tumores indica desdiferenciação completa; é usado como marcador de estadiamento e não de velocidade de divisão celular.])))

#questao-mc("30", badge-aplicacao,
  [O xeroderma pigmentosum (XP) resulta de defeitos em enzimas de reparo por excisão de nucleotídeos. Pacientes com XP acumulam dímeros de timina após exposição a UV e desenvolvem cânceres de pele precoces. Qual atividade enzimática deficiente explica a incapacidade de remover essas lesões?],
  (("A", [A atividade exonuclease 3′→5′ das DNA-polimerases de reparo, que normalmente reconhece e remove os dímeros de timina logo após sua formação por radiação ultravioleta.]),
   ("B", [A atividade de ligase NAD⁺-dependente, que sela o nick após a excisão do dímero; sem essa ligação, o fragmento excisado permanece e bloqueia a progressão da forquilha.]),
   ("C", [A atividade exonuclease 5′→3′ das polimerases de reparo, responsável por excisão dos dímeros de timina da fita danificada para permitir nova síntese na região reparada.]),
   ("D", [A atividade de telomerase mutante que, no XP, também atua no reparo telomérico; sem ela, os dímeros acumulam preferencialmente nas sequências TTAGGG dos telômeros.]),
   ("E", [A atividade de primase que, no reparo por excisão, sintetiza um primer de RNA imediatamente após a remoção do dímero; sem ela, a lacuna não é preenchida corretamente.])))
