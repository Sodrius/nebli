# Mapa de Confusões — biomol-05-operon-procariotos

Erros mecanísticos típicos por subtópico da E1. Origem: acervo interno de subquestões UC03 (2019, 2024 e 2025, etiquetas BM e BQ/BM), bibliografia (Lehninger cap. 28, Alberts cap. 7, Watson cap. 18) e armadilha de bancada. Alimenta as distratoras da E2 — nada daqui vai colado no PDF com rótulo de origem.

## 1.1 Onde o controle acontece, e por que na largada da transcrição

1. **Bactéria só regula transcrição** — o aluno lê "a iniciação é o mais importante" como "é a única". A célula regula também estabilidade e tradução do mRNA, atividade enzimática por alosteria e degradação proteica; o controle transcricional é o mais econômico porque impede o gasto antes de ele acontecer, e os outros níveis existem porque são mais rápidos que ele.
2. **Promotor e operador são a mesma coisa** — funde os dois elementos cis. O promotor é onde a RNA-polimerase se liga; o operador é onde a proteína reguladora se liga, e no operon lac ele **sobrepõe** o início da transcrição, logo à jusante do promotor. Sítios distintos, ocupantes distintos, efeitos opostos.
3. **O terminador marca o fim do gene** — troca a unidade. O terminador marca o fim do **transcrito**, e num operon esse transcrito carrega vários genes; a pontuação promotor → +1 → terminador delimita a unidade de transcrição, não a unidade de proteína.
4. **Regular a transcrição é uma decisão binária** — imagina interruptor liga/desliga. O que a célula ajusta é a **frequência de iniciação**: o nível basal existe mesmo reprimido, e repressão e ativação deslocam essa frequência em ordens de grandeza para baixo ou para cima.
5. **O mRNA bacteriano dura tanto quanto o eucariótico** — desfaz o motivo da estratégia. A meia-vida do mRNA bacteriano é de poucos minutos, e a tradução começa no transcrito ainda em síntese; por isso desligar a transcrição já derruba a proteína em minutos, sem precisar de mecanismo de destruição dedicado.

## 1.2 Repressor, ativador, indutor, co-repressor: as quatro combinações

1. **Indutor liga o operon** — a inversão mais cara da aula. Na regulação negativa induzível o indutor não toca no DNA nem na polimerase: ele se liga **ao repressor** e o faz soltar o operador. Quem transcreve é a RNA-polimerase, que estava impedida; o indutor apenas remove o impedimento.
2. **Regulação negativa é sinônimo de gene desligado** — confunde o sinal do mecanismo com o estado do gene. "Negativa" descreve *quem* regula — uma proteína que **inibe** —, não se o gene está ativo agora. Um operon sob regulação negativa fica ligado sempre que o indutor está presente.
3. **Co-repressor e indutor fazem a mesma coisa em proteínas diferentes** — apaga a direção do efeito. O indutor **dissocia** o repressor do DNA (ou dissocia o ativador, na positiva repressível); o co-repressor **associa** o repressor ao DNA. São efeitos alostéricos opostos.
4. **Regulação positiva é a que responde a nutriente, negativa a toxina** — inventa uma regra que não existe. O sinal químico pode ser qualquer metabólito nos dois casos; o que separa positiva de negativa é a proteína reguladora **facilitar** ou **impedir** a transcrição.
5. **Ativador e RNA-polimerase são a mesma proteína** — colapsa duas entidades. O ativador é uma proteína reguladora que se liga a um sítio próprio no DNA e **recruta** a polimerase; sozinho ele não sintetiza RNA nenhum.

## 1.3 Operon, cis e trans: a unidade que a bactéria transcreve de uma vez

1. **Cada gene do operon tem seu promotor** — desfaz a definição. Um operon é justamente o conjunto de genes sob **um único promotor**, transcritos num mRNA policistrônico; é isso que garante que as enzimas de uma mesma via apareçam juntas e na mesma proporção aproximada.
2. **mRNA policistrônico é traduzido numa proteína gigante que depois é clivada** — mistura com poliproteína viral. Cada cístron tem seu próprio sítio de ligação do ribossomo e seus próprios códons de início e parada; saem proteínas separadas do mesmo transcrito.
3. **O gene regulador fica dentro do operon** — assume adjacência obrigatória. O gene do repressor tem promotor próprio e pode estar em qualquer lugar do genoma; no operon lac ele calha de estar ao lado, mas é uma unidade de transcrição independente.
4. **Elemento cis é o que está perto, trans é o que está longe** — troca o critério. Cis e trans não são distância: **cis** é sequência de DNA que só influencia genes na **mesma molécula** de DNA em que está; **trans** é produto difusível — proteína ou RNA — que alcança qualquer cópia, esteja onde estiver.
5. **Operador e promotor são produtos gênicos** — transforma sítio em molécula. Nem operador nem promotor são transcritos como produto funcional: são endereços no DNA. Repressor e ativador, sim, são produtos.

## 2.1 Os cinco elementos do operon lac e o açúcar que eles processam

1. **lacI é gene estrutural do operon** — coloca o repressor dentro do que ele reprime. lacI é o **gene regulador**, com promotor próprio e expressão constitutiva baixa; os genes estruturais são lacZ, lacY e lacA.
2. **A lactose entra na célula por difusão** — dispensa o transportador e quebra a lógica da expressão basal. A entrada é feita pela **permease** codificada por lacY, um simporte que traz lactose junto com H⁺ usando a força próton-motriz; sem permease basal, não há lactose dentro para virar indutor.
3. **A lactose é o indutor** — atalho quase certo, e errado. O indutor fisiológico é a **alolactose**, isômero produzido por uma reação lateral da própria β-galactosidase sobre a lactose. Sem alguma β-galactosidase basal, não há alolactose.
4. **β-galactosidase só quebra lactose** — reduz a enzima a uma reação. Ela hidrolisa a ligação β-1,4 em galactose e glicose *e* transgalactosila parte do substrato em alolactose; é a mesma enzima gerando o produto e o sinal.
5. **lacA é dispensável e não faz nada** — descarta o terceiro gene. A transacetilase transfere acetil da acetil-CoA para galactosídeos não metabolizáveis, marcando-os para excreção; é destoxificação, não catabolismo.

## 2.2 LacI: um sensor alostérico que solta o DNA quando encontra o indutor

1. **O repressor tapa o promotor** — troca o sítio. LacI ocupa o **operador**, que sobrepõe o sítio de início da transcrição; a RNA-polimerase ainda consegue se ligar ao promotor, mas não consegue escapar para a fase de alongamento.
2. **O indutor compete com o DNA pelo mesmo sítio do repressor** — imagina competição direta. O sítio do indutor fica no **core** da proteína, longe do domínio de ligação ao DNA; a ligação muda a conformação e desalinha as hélices-volta-hélice. É alosteria, não competição.
3. **LacI é monomérico** — perde a simetria que explica tudo. É um **tetrâmero**, dois dímeros unidos pelo domínio de tetramerização; cada dímero lê um sítio operador, e o operador é palindrômico exatamente porque quem o lê é um dímero simétrico.
4. **Repressão é bloqueio absoluto** — apaga a expressão basal. A repressão derruba a transcrição em cerca de mil vezes, não a zero; a fração que escapa produz as poucas moléculas de permease e β-galactosidase que tornam o sistema indutível.
5. **Só existe um operador no operon lac** — simplifica demais e perde o looping. Além do operador principal, há dois sítios auxiliares; o tetrâmero pode ocupar dois deles ao mesmo tempo e dobrar o DNA numa alça, o que aumenta a repressão muito além do que um sítio isolado daria.

## 2.3 Jacob e Monod: mutantes, o diploide parcial e a prova de que o repressor difunde

1. **Mutante constitutivo é o que não responde ao indutor** — troca os dois fenótipos. **Constitutivo** expressa sempre, com ou sem lactose; **não indutível** não expressa nunca, nem com lactose. São extremos opostos da mesma curva.
2. **I⁻ e O^c dão o mesmo resultado no diploide parcial** — o ponto exato do experimento. I⁻ é **recessivo** e age em **trans**: o repressor selvagem da segunda cópia difunde e reprime as duas moléculas de DNA. O^c é **dominante** e age em **cis**: o operador defeituoso só desregula o operon da própria molécula, que fica constitutivo mesmo com repressor bom disponível.
3. **LacI^S é só um I⁻ mais forte** — inverte o defeito. Em I⁻ o repressor não se liga ao DNA; em **LacI^S** ele se liga bem ao DNA mas perdeu afinidade pelo **indutor**, então não solta nunca — fenótipo não indutível, e dominante, porque as subunidades mutantes se misturam com as selvagens no tetrâmero.
4. **IPTG e X-Gal são a mesma coisa** — funde reagente indutor com reagente revelador. **IPTG** é análogo da alolactose que induz e não é metabolizado, mantendo indução constante; **X-Gal** é substrato cromogênico que a β-galactosidase cliva liberando pigmento azul. Um liga o sistema, o outro mostra que ele foi ligado.
5. **Colônia azul significa que o operon está mutado** — inverte a leitura. Azul indica β-galactosidase **ativa**; branco indica ausência de atividade, seja por lacZ defeituoso, seja por ausência de indução.
6. **O merozigoto é uma bactéria diploide** — generaliza. É **diploide parcial**: só a região trazida pelo epissomo está em duas cópias; o resto do genoma continua único.

## 3.1 A anatomia do promotor bacteriano e a força que ele carrega

1. **A RNA-polimerase reconhece o promotor sozinha** — omite o fator que faz a leitura. Quem reconhece −35 e −10 é a subunidade **σ**; o core da polimerase (α₂ββ′) sintetiza RNA mas não distingue promotor de DNA qualquer.
2. **−10 e −35 são posições do primeiro nucleotídeo transcrito** — perde o referencial. A numeração é relativa ao **+1**, o primeiro nucleotídeo do transcrito; os números negativos contam bases à montante, e não existe posição zero.
3. **Sequência consenso é a sequência real de todo promotor** — confunde estatística com sequência. O consenso é a base mais frequente em cada posição no conjunto dos promotores; promotores reais divergem dele, e é justamente essa divergência que gradua a força.
4. **Promotor fraco é promotor defeituoso** — perde o desenho do sistema. A baixa conformidade ao consenso é o que deixa espaço para um ativador dar o ganho que falta; um promotor lac idêntico ao consenso seria forte demais e não obedeceria à CAP.
5. **O espaçamento entre −35 e −10 não importa** — ignora a geometria. A distância de cerca de 17 pares de base posiciona os dois elementos na mesma face da dupla-hélice; alterá-la reduz a iniciação mesmo com as duas sequências perfeitas.

## 3.2 CAP-cAMP: o ativador que compensa um promotor fraco de propósito

1. **CAP responde à lactose** — troca o sinal de entrada. CAP responde à **falta de glicose**, traduzida em cAMP alto. Lactose é lida pelo repressor; glicose, pelo ativador. São dois sensores independentes.
2. **cAMP alto significa muita energia disponível** — inverte o significado. Em *E. coli*, cAMP sobe quando a glicose acaba; é sinal de **escassez** do açúcar preferido, e serve de licença para transcrever operons de fontes alternativas.
3. **CAP se liga ao DNA sempre que existe** — dispensa o ligante. CAP só adquire conformação capaz de ligar o sítio CAP quando está **complexada a cAMP**; sem cAMP ela circula inerte.
4. **O sítio CAP fica dentro do operador** — troca de endereço. O sítio CAP fica **à montante** do promotor; o operador fica à jusante, sobre o início da transcrição. Um recruta, o outro bloqueia, em lados opostos do promotor.
5. **CAP funciona empurrando a polimerase** — metáfora sem mecanismo. CAP faz contato direto com o domínio C-terminal da subunidade α da polimerase; a energia livre favorável dessa interação proteína–proteína compensa a ligação fraca ao promotor imperfeito.
6. **Glicose reprime o operon lac ligando-se ao repressor** — inventa um sítio. A glicose age por dois caminhos indiretos: derruba o cAMP através do sistema fosfotransferase e, pela mesma via, inibe a permease e reduz a entrada de lactose.

## 3.3 Glicose × lactose: quatro ambientes, uma porta lógica

1. **Sem glicose, o operon lac está ligado** — esquece metade da lógica. Sem glicose e **sem** lactose, o repressor continua no operador: cAMP alto com repressor ligado dá transcrição desprezível. É preciso lactose presente **e** glicose ausente.
2. **Glicose e lactose juntas dão expressão máxima** — soma sinais que não se somam. Com as duas, o repressor sai do operador, mas o cAMP está baixo e a CAP não ativa: a transcrição fica em nível basal, muito abaixo do máximo.
3. **Repressão por catabólito é a glicose reprimindo o gene lacI** — desloca o alvo. A repressão por catabólito atua sobre a **ativação**: menos cAMP, menos CAP ligada, menos recrutamento da polimerase. lacI segue transcrito do mesmo jeito.
4. **A diauxia mostra que a bactéria não consegue usar lactose** — lê a curva ao contrário. A curva bifásica mostra que ela usa **primeiro a glicose** e só depois reprograma para lactose; a fase de platô entre os dois crescimentos é o tempo de sintetizar as enzimas do operon.
5. **A porta lógica do operon lac é OU** — troca o operador lógico. A saída alta exige as duas condições ao mesmo tempo: lactose presente **E** glicose ausente. É uma porta AND com uma entrada invertida.
