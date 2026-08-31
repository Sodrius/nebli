# Mapa de Confusões — micro-02-fisiologia-crescimento-bacteriano

Erros mecanísticos típicos por subtópico da E1. Origem: acervo interno de subquestões UC03/MB (2015-2025), bibliografia (Trabulsi, Murray, Brock, Tortora) e armadilha clínica. Alimenta as distratoras da E2 — nada daqui vai colado no PDF com rótulo de origem.

## 1.1 Divisão binária e tempo de geração

1. **Divisão binária é "a célula partindo ao meio"** — o aluno imagina só a constrição. Antes de qualquer estrangulamento, a célula precisa duplicar o cromossomo, expandir massa de proteína, lipídeo e parede, e segregar as duas cópias do DNA para os polos opostos. A constrição é o último ato, não o processo.
2. **Tempo de geração é constante para a espécie** — não é. É o tempo de duplicação naquele meio, naquela temperatura e naquele pH; a mesma *E. coli* que dobra em 20 min em meio rico dobra muito mais devagar em meio mínimo, onde precisa sintetizar aminoácido do zero.
3. **Tempo de geração é o tempo de replicar o cromossomo** — são grandezas diferentes. Bactérias de crescimento muito rápido chegam a iniciar uma nova rodada de replicação antes de terminar a anterior, o que desacopla os dois tempos.
4. **As duas células-filhas são "mãe e filha", como no brotamento** — na divisão binária o produto são duas células equivalentes, cada uma com uma cópia do cromossomo e metade do citoplasma; não há célula-mãe que permanece.
5. **A parede se rompe para a célula se dividir** — ao contrário: a maquinaria de síntese de parede é recrutada para o plano de divisão e ergue ali uma parede nova, o septo, que depois é clivado ao meio. Divisão é construção, não ruptura.

## 1.2 A conta que descreve o crescimento

1. **O expoente n é o tempo decorrido** — n é o número de gerações, isto é, o tempo dividido pelo tempo de geração. Trocar minutos por gerações é o erro aritmético mais comum, e ele muda o resultado por ordens de grandeza.
2. **A base 2 poderia ser qualquer número** — a base é 2 porque cada célula gera exatamente duas. É uma consequência do modo de divisão, não uma convenção de cálculo.
3. **O gráfico de crescimento é uma reta porque o crescimento é linear** — o gráfico só vira reta porque o eixo vertical é logarítmico. Em escala aritmética a mesma população desenha uma curva que sobe verticalmente e não cabe no papel.
4. **A inclinação da fase exponencial mede o número de bactérias** — mede a velocidade de duplicação. Duas culturas podem partir do mesmo inóculo e ter inclinações muito diferentes por terem tempos de geração diferentes.
5. **x₀ é sempre 1** — x₀ é o inóculo inicial, que quase nunca é uma célula. Assumir 1 quando o dado é 10⁵ subestima o resultado no mesmo fator.

## 1.3 Por que a exponencial sempre quebra

1. **O resultado do cálculo descreve a cultura real** — a fórmula descreve só a fase exponencial. Aplicada a 24 h, prevê 10¹⁰ células por colônia, mas o teto observado é da ordem de 10⁸; a diferença não é erro de conta, é o fim da fase exponencial.
2. **O crescimento para porque as bactérias envelhecem** — não há senescência programada como causa. O crescimento para porque o nutriente se esgota, o produto do metabolismo se acumula e, na colônia sólida, porque o nutriente não difunde até o centro do monte de células.
3. **Na colônia o limite é espaço físico** — o limite é fluxo de nutriente e saída de produto por difusão. Colônia e cultura líquida travam em ordens de grandeza semelhantes, ainda que em geometrias diferentes.
4. **Sinalização de densidade populacional é um mecanismo de suicídio coletivo** — não é. É leitura de densidade: cada célula secreta um sinal difusível, e quando a concentração passa de um limiar a população troca de programa gênico — biofilme, fatores de virulência, redução da divisão. É coordenação, não morte.
5. **O teto de 10⁸ é uma constante universal** — é uma ordem de grandeza típica, que varia com espécie, meio e geometria. O que é universal é a existência de um teto, não o número.

## 1.4 As quatro fases da curva

1. **Na fase lag a bactéria está inativa** — é o inverso: não há divisão, mas a atividade metabólica é intensa. A célula está fabricando transportadores, enzimas da via que a nova fonte de carbono exige e, sobretudo, ribossomos, para poder crescer depois.
2. **A duração da lag é característica da espécie** — depende sobretudo da diferença entre o meio anterior e o novo. Inóculo transferido de um meio idêntico, em fase exponencial, entra em log quase sem lag.
3. **Na fase estacionária as bactérias pararam de se dividir** — pode ocorrer, mas a situação mais comum é dinâmica: a divisão continua e o número de células novas iguala o número que perde viabilidade. O platô é equilíbrio, não paralisia.
4. **A fase de declínio significa que todas as células morreram** — significa que a taxa de morte excede a de divisão; a queda é progressiva, e subpopulações podem persistir muito tempo em estado de baixa atividade.
5. **A fase log é a mais resistente porque as bactérias estão "fortes"** — é a mais vulnerável. Agente que depende de parede em construção ou de síntese ativa de proteína encontra na multiplicação intensa o alvo que precisa; a célula quiescente da estacionária é justamente a difícil.
6. **Curva de crescimento é a curva de uma bactéria** — é a curva de uma população. Nenhuma célula individual percorre lag, log, estacionária e declínio; as fases descrevem o comportamento do conjunto.

## 1.5 Como se acompanha uma cultura

1. **Turvação conta células viáveis** — turvação mede luz espalhada por partícula em suspensão, viva ou morta. Uma cultura que entrou em declínio pode manter a turvação enquanto a contagem de viáveis despenca.
2. **Contagem em placa conta células** — conta unidade formadora de colônia. Bactéria que cresce em cacho ou em cadeia origina uma única colônia a partir de várias células, e o método a subestima.
3. **Contagem ao microscópio é o método mais confiável** — é o mais direto para número total, mas não distingue viva de morta, exige carga alta e é trabalhoso; por isso a rotina prefere turvação e contagem em placa.
4. **Os métodos se equivalem porque medem a mesma coisa** — medem grandezas diferentes: número total, número de viáveis e massa que espalha luz. Enquanto a cultura só cresce, os três andam juntos; a partir da estacionária eles divergem, e a divergência é a informação.
5. **Medir consumo de oxigênio ou produto do metabolismo é método indireto e impreciso** — é indireto, mas é a base de sistemas automatizados de hemocultura, que detectam crescimento pela produção de CO₂ muito antes de haver turvação visível.

## 2.1 Macronutrientes: a lista de compras da célula

1. **Fonte de energia e fonte de carbono são a mesma coisa** — coincidem no heterotrófico que usa açúcar, mas são eixos independentes: há bactéria que tira energia de composto inorgânico ou de luz e carbono do CO₂, e combinações intermediárias.
2. **Autotrófico é sinônimo de fotossintetizante** — autotrófico é quem fixa carbono inorgânico; a energia para isso pode vir da luz ou da oxidação de composto inorgânico, sem luz nenhuma.
3. **Nitrogênio só entra na célula como amônio** — entra também como nitrito e nitrato, que precisam ser reduzidos antes de serem incorporados, e algumas espécies fixam N₂ atmosférico, processo caro em energia.
4. **Fósforo e enxofre são micronutrientes por serem minoritários** — são macronutrientes: o fósforo compõe o esqueleto de ácido nucleico, o ATP e o fosfolipídeo, e o enxofre entra em dois aminoácidos e em centros de ferro-enxofre de proteínas respiratórias.
5. **Bactéria de interesse clínico é sempre heterotrófica porque não sabe fazer o resto** — é heterotrófica porque vive de matéria orgânica do hospedeiro; isso é adaptação de nicho, não incapacidade genérica.

## 2.2 Micronutrientes e fatores de crescimento

1. **Micronutriente é opcional** — é necessário em quantidade pequena, não dispensável: sem o metal certo no sítio ativo, a enzima que depende dele não funciona.
2. **Ferro é abundante no corpo humano, então não limita bactéria** — ferro livre é escasso justamente porque o hospedeiro o mantém sequestrado em proteínas; a disputa por ferro é um eixo real da infecção, e bactérias secretam quelantes de alta afinidade para arrancá-lo.
3. **Fator de crescimento é um estimulante do crescimento** — é uma molécula essencial que aquela bactéria não sabe sintetizar e precisa receber pronta: vitamina, aminoácido, base nitrogenada, fator presente no sangue.
4. **Ágar chocolate contém chocolate** — o nome vem da cor. É ágar sangue aquecido, e o aquecimento rompe a hemácia liberando fatores intracelulares que certas espécies exigentes não fabricam; por isso elas crescem no chocolate e não no sangue íntegro.
5. **Bactéria exigente é bactéria fraca** — exigente descreve necessidade nutricional, não virulência. Vários agentes exigentes causam doença grave; a exigência apenas dificulta o cultivo no laboratório.

## 2.3 pH: o interno é que importa

1. **Acidófilo tem citoplasma ácido** — o citoplasma da grande maioria é mantido próximo do neutro; o que muda entre acidófilo, neutrófilo e alcalófilo é o pH externo tolerado e a capacidade de manter o gradiente através da membrana.
2. **Fora do pH ótimo a bactéria morre** — fora da faixa ela deixa de crescer; morrer é outra coisa e depende de intensidade e tempo. Conservação de alimento por acidificação explora exatamente essa diferença.
3. **Todo patógeno humano cresce melhor em pH 7 porque o corpo é neutro** — o corpo tem microambientes muito distintos; há nichos ácidos, e a sobrevivência gástrica de alguns agentes depende de hidrolisar ureia e cercar-se de amônia, tamponando o próprio entorno.
4. **A faixa de pH de crescimento é estreita, de uma unidade** — a faixa típica cobre cerca de três unidades em torno do ótimo, com queda de velocidade nas bordas; é a faixa larga que permite crescer em meios diferentes.
5. **Meio de cultura não precisa de tampão porque o pH é ajustado no preparo** — precisa: o próprio metabolismo bacteriano desloca o pH, acidificando quando fermenta açúcar e alcalinizando quando degrada proteína.

## 2.4 Temperatura: subida química, queda proteica

1. **A curva de temperatura é simétrica em torno do ótimo** — é francamente assimétrica. A subida é aceleração progressiva de reação química; a queda, acima do ótimo, é abrupta porque reflete desnaturação de proteína. O ótimo fica colado no limite superior.
2. **Mesófilo cresce apenas a 37 °C** — 37 °C é o ótimo dos de interesse médico; a faixa mesófila é ampla, aproximadamente de 20 a 45 °C.
3. **Refrigeração esteriliza o alimento** — refrigeração retarda o crescimento, não mata. Algumas espécies crescem lentamente perto de 4 °C, o que é justamente o risco de alimento conservado por muito tempo.
4. **Termófilo é resistente porque tem parede mais espessa** — a resistência está nas macromoléculas: proteínas com estrutura mais estável e membranas com lipídeos que mantêm fluidez adequada em alta temperatura.
5. **Temperatura ótima é a que dá mais células no fim** — é a que dá maior velocidade de crescimento. O rendimento final depende de nutriente disponível, e uma cultura mais lenta pode terminar com a mesma densidade.

## 2.5 Oxigênio: usar sem se envenenar

1. **Anaeróbio estrito morre por falta de enzima que usa oxigênio** — morre por não neutralizar os derivados reativos que se formam espontaneamente na presença de O₂. Faltam-lhe superóxido-dismutase e catalase, não uma enzima que consuma O₂.
2. **Aerotolerante é o mesmo que anaeróbio facultativo** — o aerotolerante cresce igual com ou sem O₂ porque não o usa em momento nenhum; o facultativo usa O₂ quando há, e rende muito mais nessa condição.
3. **Microaerófilo é intermediário entre aeróbio e anaeróbio** — é aeróbio que exige tensão de O₂ menor que a atmosférica: precisa de oxigênio, mas é lesado pela concentração do ar.
4. **Catalase e superóxido-dismutase fazem a mesma reação** — a dismutase converte superóxido em peróxido de hidrogênio; a catalase decompõe esse peróxido em água e O₂. São passos sequenciais de uma mesma linha de desintoxicação, e há espécies que têm um e não o outro.
5. **A posição da bactéria no tubo de tioglicolato é decidida pelo peso da célula** — é decidida pela relação da espécie com o oxigênio, que difunde de cima para baixo e forma um gradiente; cada classe cresce na faixa de tensão que tolera e aproveita.
6. **Fermentar é o que o anaeróbio faz por não ter cadeia transportadora** — muitos anaeróbios têm cadeia transportadora e fazem respiração usando outro aceptor final que não o O₂; fermentação e anaerobiose não são sinônimos.

## 3.1 Catabolismo, anabolismo e o cruzamento das vias

1. **Catabolismo e anabolismo acontecem em momentos separados** — ocorrem simultaneamente e acoplados: o catabolismo fornece o ATP, o poder redutor e os esqueletos de carbono que o anabolismo consome no mesmo instante.
2. **Anabolismo só serve para crescer** — serve também para repor: parede, membrana e proteína são renovadas continuamente, mesmo quando a população não aumenta.
3. **A via central existe para gerar ATP** — gera ATP e, ao mesmo tempo, fornece os intermediários de que a célula parte para fabricar aminoácido, base nitrogenada, lipídeo e precursor de parede. Desviar demais para biossíntese reduz o rendimento energético, e é essa dupla função que a torna o eixo do metabolismo.
4. **Reação anabólica libera energia porque constrói ordem** — construir consome energia; a ordem é paga com ATP e com poder redutor obtidos no catabolismo.
5. **Cada bactéria tem um metabolismo único e imprevisível** — a diversidade é grande, mas organizada: o que varia é a fonte de energia, a fonte de carbono, o aceptor final de elétrons e o repertório de enzimas hidrolíticas — e é essa variação que o laboratório usa para identificar espécies.

## 3.2 Fermentação × respiração: o aceptor final decide

1. **Fermentação ocorre porque falta oxigênio, e só** — o gargalo é o transportador de elétrons: a glicólise consome NAD⁺ e o devolve reduzido, e sem reoxidá-lo a via para em segundos. A fermentação despeja esses elétrons num derivado do piruvato para regenerar NAD⁺.
2. **Respiração é sinônimo de uso de oxigênio** — respiração é gerar ATP por cadeia transportadora com um aceptor final externo. Quando esse aceptor é nitrato ou sulfato em vez de O₂, é respiração anaeróbia, com rendimento intermediário.
3. **Fermentação não gera ATP** — gera, por fosforilação no nível do substrato, dentro da própria glicólise. O que ela não tem é a cadeia transportadora, e é daí que vem a diferença de rendimento.
4. **A fermentação queima a glicose até CO₂ e água** — não queima: o produto final é um composto orgânico ainda rico em energia — lactato, etanol, ácidos diversos — que a célula descarta.
5. **O rendimento de ATP da respiração é fixo** — os números clássicos são estimativas; o rendimento real varia com a eficiência do bombeamento de prótons e com o desvio de intermediários para biossíntese.

## 3.3 O produto final é identidade — e muda o meio

1. **Todas as bactérias fermentam a glicose do mesmo jeito** — as etapas até piruvato são as mesmas; a diferença está em como cada gênero reduz o piruvato, e é o conjunto de produtos finais que distingue os grupos no laboratório.
2. **A cor da colônia em meio diferencial é a cor da bactéria** — a cor vem da reação entre um produto do metabolismo e um indicador presente no meio; a bactéria em si é praticamente incolor.
3. **Todo metabolismo bacteriano acidifica o meio** — fermentar açúcar acidifica; degradar proteína e aminoácido libera amônia e alcaliniza. Meio diferencial explora as duas direções.
4. **Se a bactéria não muda a cor do meio, ela não cresceu** — pode ter crescido usando outra fonte de carbono que não a do indicador; ausência de reação é informação sobre a via, não sobre o crescimento.
5. **Produzir gás é sinal de contaminação** — gás é produto legítimo de algumas vias de fermentação, e sua presença ou ausência é um dos critérios de identificação.

## 3.4 Meio líquido e meio sólido; mínimo e completo

1. **Meio sólido tem composição diferente do líquido** — tem a mesma composição, acrescida de agente solidificante em torno de 2%. É a mesma nutrição em outra apresentação.
2. **O agente solidificante serve de alimento** — é justamente escolhido por não ser degradado pela imensa maioria das bactérias, o que mantém a placa firme enquanto elas crescem sobre ela.
3. **Meio mínimo é meio pobre, de uso restrito** — é meio de composição definida, com sais e uma única fonte de carbono; sua utilidade é justamente diagnosticar exigência nutricional, porque só cresce quem sabe sintetizar todo o resto.
4. **Meio completo é melhor que meio mínimo** — são ferramentas para perguntas diferentes: o completo faz crescer o maior número de espécies; o mínimo revela o que a bactéria sabe fabricar.
5. **Semeadura por esgotamento serve para contar bactérias** — serve para separar células no espaço até que colônias isoladas se formem, cada uma derivada de uma célula. Contagem exige diluição seriada e volume medido.
6. **Curva de crescimento pode ser levantada em placa** — em meio sólido a colônia trava cedo por difusão; a curva se levanta em meio líquido, onde o nutriente alcança cada célula.

## 3.5 Meios diferenciais, seletivos e os dois juntos

1. **Meio seletivo e meio diferencial são a mesma coisa** — o seletivo contém algo que impede parte das bactérias de crescer; o diferencial deixa todas crescerem e as separa pela cor da colônia. Um reduz o número de espécies presentes, o outro apenas revela diferenças.
2. **Meio seletivo mata a bactéria indesejada** — em geral inibe o crescimento, o que basta para o objetivo: sal biliar e corante desorganizam membrana que a Gram-positiva não tem por fora da parede, e concentração alta de sal impõe estresse osmótico que poucas espécies toleram.
3. **Ágar sangue é meio seletivo** — é meio completo enriquecido e diferencial, porque revela o padrão de hemólise; não inibe grupo nenhum.
4. **Colônia rosa em meio com lactose significa "bactéria rosa"** — significa que aquela colônia fermentou a lactose, acidificou o entorno e virou o indicador de pH; colônia incolor significa que não fermentou.
5. **Um meio não pode ser seletivo e diferencial ao mesmo tempo** — pode, e vários são: contêm inibidor para restringir quem cresce e indicador para separar por cor quem cresceu.
6. **Escolher o meio é detalhe técnico do laboratório** — a escolha depende do sítio de coleta e da hipótese clínica: amostra de local com microbiota abundante exige meio seletivo, sob pena de o agente procurado ser encoberto por acompanhantes.

## 3.6 Quando o meio não resolve

1. **Bactéria que não cresce no meio de rotina é rara e pouco relevante** — as exigentes e as de crescimento muito lento incluem agentes centrais da clínica; o que muda é a estratégia diagnóstica, não a importância.
2. **A demora da cultura de micobactéria é problema do meio** — é consequência do tempo de geração, medido em horas e não em minutos; mesmo em meio ideal a colônia visível leva semanas.
3. **Não crescer em meio artificial significa não ter metabolismo próprio** — significa depender de fatores fornecidos pelo hospedeiro, muitas vezes por perda evolutiva de vias biossintéticas; a célula continua metabolicamente ativa dentro do hospedeiro.
4. **Se não cresce, não há diagnóstico possível** — há: coloração específica direta, detecção de ácido nucleico, resposta imune do hospedeiro e cultivo em modelo animal ou celular.
5. **Cultura negativa exclui infecção** — cultura negativa pode significar agente exigente, agente de crescimento lento, coleta em sítio errado ou uso prévio de antimicrobiano; ausência de crescimento não é ausência de agente.
