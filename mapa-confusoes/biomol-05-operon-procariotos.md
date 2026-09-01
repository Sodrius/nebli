# Mapa de Confusões — biomol-05-operon-procariotos

Erros mecanísticos típicos por subtópico da E1. Alimenta as distratoras da E2 (regra: distratora
tem mecanismo plausível-mas-errado, 25–35 palavras) e os boxes da E1.

## PARTE I — A lógica do operon e a gramática do DNA bacteriano

### 1.1 Por que regular
1. **Regulação = ligar/desligar binário.** Aluno acha que o operon está a 0 ou a 100. Na verdade a repressão derruba ~1000×, e o resíduo basal é funcionalmente necessário. (origem: livro-texto)
2. **Regular para economizar espaço no genoma.** Confunde economia energética com compactação. O que se economiza é aminoácido, ATP e ribossomo ocupado — não DNA. (armadilha conceitual)
3. **A bactéria regula por degradação de proteína.** Transfere o mecanismo eucarioto/proteassoma; em procarioto o gargalo regulado é a iniciação da transcrição. (banco NEBLI #309)
4. **Enzima induzida aparece "na hora".** Ignora que o mRNA bacteriano tem meia-vida de minutos e que a resposta exige transcrição + tradução novas. (armadilha)

### 1.2 Unidade transcricional e mRNA policistrônico
1. **Policistrônico = uma proteína grande que depois é clivada.** Confunde com poliproteína viral. Cada cistron tem seu próprio códon de início e seu próprio sítio de ligação ao ribossomo. (livro-texto)
2. **Um promotor por gene.** Aluno projeta o modelo eucarioto. No operon, um promotor serve a todos os genes estruturais a jusante. (armadilha)
3. **Estequiometria igual para todos os produtos.** Como o mRNA é um só, o aluno espera quantidades iguais; a eficiência de cada RBS e a degradação 3′→5′ fazem β-galactosidase sair em muito maior quantidade que a transacetilase. (aprofundamento)
4. **lacI faz parte do operon.** lacI tem promotor próprio, é transcrito constitutivamente e não está sob controle do operador. (banco NEBLI #305)

### 1.3 Cis × trans
1. **Cis/trans é sobre estar perto ou longe.** Não é distância, é natureza: sequência de DNA não difunde, produto proteico difunde. Um sítio a 60 pb e um sítio no fim do operon são igualmente *cis*. (armadilha central)
2. **Um alelo bom sempre corrige o ruim.** Só se o produto for difusível. Operador mutante não é corrigível por operador bom noutra molécula. (prova histórica)
3. **Gene regulador tem que ficar colado ao operon.** A proximidade do lacI ao lac é acidente genômico; funcionalmente ele poderia estar em qualquer lugar, inclusive num plasmídeo. (armadilha)
4. **Sítio CAP e operador são a mesma classe de coisa que lacI.** Os dois primeiros são sequência (cis); lacI codifica proteína (trans). (armadilha)

### 1.4 Peças do operon lac
1. **lacY é dispensável.** Sem permease a lactose externa quase não entra, e o operon não é induzido de forma eficiente — lacY é parte da alça de retroalimentação positiva. (aprofundamento)
2. **lacZ codifica a permease.** Troca de rótulo clássica: Z = β-galactosidase, Y = permease, A = transacetilase. (livro-texto)
3. **O operador está antes do promotor.** Ele se sobrepõe ao promotor/início da transcrição, logo a jusante do −10 — é essa sobreposição que faz a repressão funcionar. (armadilha mecanística)
4. **Sítio CAP fica dentro do gene lacZ.** Fica a montante do promotor, por volta de −61. (prova histórica)

## PARTE II — Controle negativo

### 2.1 O que o repressor bloqueia
1. **Repressor impede a RNA polimerase de encostar no DNA.** A polimerase ainda liga o promotor; o que fica bloqueado é a abertura da bolha e o escape para o alongamento. (banco NEBLI #305)
2. **Repressor degrada o mRNA já feito.** Confunde controle transcricional com estabilidade de mRNA. (armadilha)
3. **Repressor é um monômero que cobre um sítio.** É um tetrâmero, e é justamente a estrutura de 4 subunidades que permite o alelo dominante-negativo e a alça de DNA entre operadores. (aprofundamento)
4. **Repressão zera a transcrição.** Derruba ~1000×; o basal remanescente é o que permite o arranque. (livro-texto)

### 2.2 O indutor
1. **A lactose é o indutor.** O indutor fisiológico é a alolactose, isômero produzido pela própria β-galactosidase. (livro-texto / prova histórica)
2. **O indutor se liga ao operador.** Liga-se ao repressor, num sítio diferente do sítio de DNA — é alosteria. (armadilha)
3. **O indutor arranca o repressor por competição pelo mesmo sítio.** Não há competição: a mudança de conformação reduz a afinidade do repressor pelo operador. (armadilha)
4. **IPTG é metabolizado como a lactose.** IPTG é gratuito — entra, induz e não é consumido, por isso mantém indução estável. (prova histórica)

### 2.3 X-Gal e IPTG
1. **X-Gal induz o operon.** X-Gal é substrato cromogênico; quem induz é o IPTG. (prova histórica)
2. **Colônia azul = operon reprimido.** Azul é clivagem de X-Gal, logo β-galactosidase presente, logo operon ativo. (inversão comum)
3. **Colônia branca prova que o gene lacZ está deletado.** Branco só diz que não há atividade de β-galactosidase — pode ser lacZ⁻, lacI^s, promotor mutante ou sítio CAP mutante. (prova histórica)
4. **A cor vem do próprio X-Gal.** A cor vem do produto: o indol liberado dimeriza e oxida a um pigmento índigo insolúvel. (aprofundamento)

### 2.4 Mutantes constitutivos
1. **O^c e lacI⁻ são o mesmo defeito.** Mesmo fenótipo em haploide, mecanismos e comportamentos opostos em diploide parcial. (prova histórica)
2. **O^c significa operador ausente.** Significa operador alterado que não é mais reconhecido pelo repressor — a sequência continua lá. (armadilha)
3. **lacI⁻ é dominante.** É recessivo: o repressor bom feito pela outra cópia difunde e reprime os dois operadores. (prova histórica)
4. **Constitutivo quer dizer "expressão máxima".** Quer dizer "sem regulação pelo indutor". Em O^c com glicose alta, a expressão é constitutiva mas baixa, porque o braço positivo continua desligado. (aprofundamento de alto valor)

### 2.5 Diploide parcial
1. **Diploide parcial é uma bactéria diploide.** É haploide com um plasmídeo F′ carregando uma segunda cópia só da região lac. (livro-texto)
2. **A dominância é lida sem olhar em que molécula está a mutação.** Para sítio de DNA, a leitura tem que ser por molécula. (prova histórica)
3. **Z⁻ na mesma molécula do O^c é resgatado pelo Z⁺ do plasmídeo.** É — mas só a enzima; a regulação daquela molécula continua constitutiva. Separar "quem produz" de "quem regula". (aprofundamento)
4. **Todo mutante dominante é ganho de função.** lacI^-d é dominante por envenenamento do tetrâmero, o que é perda de função com efeito dominante. (aprofundamento)

### 2.6 Alelos que fecham a lógica
1. **lacI^s é constitutivo.** É o oposto: não-induzível — o repressor perdeu o sítio do indutor e nunca solta o operador. (aprofundamento)
2. **lacI^s é recessivo como lacI⁻.** É dominante em trans: o super-repressor difunde e trava os dois operadores. (aprofundamento)
3. **Mutação no promotor dá fenótipo constitutivo.** Dá o oposto — não-induzível por falta de transcrição, indistinguível de lacZ⁻ na placa sem outros testes. (prova histórica)
4. **Sítio CAP mutante dá fenótipo idêntico ao promotor mutante.** Parecido, não idêntico: o sítio CAP mutante ainda permite o basal e continua respondendo ao indutor, só nunca chega ao nível ativado. (aprofundamento)

## PARTE III — Controle positivo

### 3.1 O limite do controle negativo
1. **Sem glicose e sem lactose o operon liga.** Falta o indutor: repressor no operador, operon desligado, ainda que o CAP esteja ativo. (livro-texto)
2. **Com lactose o operon sempre liga forte.** Com glicose alta, o operador está livre mas o promotor fraco sozinho dá só nível basal. (prova histórica)
3. **Glicose reprime ligando alguma proteína ao operador.** Glicose age no braço positivo, nunca no operador. (armadilha central)
4. **Repressão por catabólito é feita pela própria glicose ligando ao CAP.** Quem liga ao CAP é o cAMP; a glicose age antes, derrubando o cAMP. (armadilha)

### 3.2 Anatomia do promotor
1. **Quem reconhece o promotor é o core da polimerase.** É a subunidade σ; o core sozinho não distingue promotor de DNA qualquer. (livro-texto)
2. **−10 e −35 são contados a partir do códon de início.** São contados a partir do +1 da transcrição, não da tradução. (armadilha)
3. **Consenso é a sequência que todo promotor tem.** É a base mais frequente em cada posição, num alinhamento — quase nenhum promotor real tem todas. (livro-texto)
4. **O espaçamento entre −35 e −10 é irrelevante.** ~17 pb é parte do elemento: alterar o espaçamento desalinha os dois domínios de σ e enfraquece o promotor mesmo com sequências perfeitas. (aprofundamento)

### 3.3 Promotor fraco
1. **Promotor fraco = promotor mutante/defeituoso.** É sequência selvagem; a fraqueza é a estratégia que permite regulação por ativador. (armadilha central)
2. **Promotor forte é sempre melhor.** Promotor forte não pode ser ativado — já está no teto; a amplitude de regulação exige começar baixo. (aprofundamento)
3. **A fraqueza do lac vem do operador.** Vem do desvio das próprias caixas −35 (TTTACA vs TTGACA) e −10 (TATGTT vs TATAAT). (prova histórica)
4. **Ativador transforma promotor fraco em promotor forte.** Não muda a sequência: compensa energeticamente por contato proteína-proteína. (armadilha)

### 3.4 CAP-cAMP
1. **CAP é ativado pela glicose.** É ativado pelo cAMP, que sobe quando a glicose falta. (inversão clássica)
2. **CAP liga no operador.** Liga a montante do promotor, por volta de −61. (armadilha)
3. **CAP abre a dupla-hélice para a polimerase.** Quem abre é a polimerase; CAP dobra o DNA ~90° e recruta a enzima por contato com o domínio C-terminal da subunidade α. (aprofundamento)
4. **A glicose derruba o cAMP por consumo de ATP.** Derruba por sinalização: o transporte pelo PTS mantém a EIIA desfosforilada, e a EIIA desfosforilada não ativa a adenilato-ciclase. (aprofundamento de alto valor)
5. **Exclusão do indutor e repressão por catabólito são a mesma coisa.** Duas alavancas distintas da mesma glicose: uma fecha a permease (entrada de lactose), outra derruba o cAMP (ativação do promotor). (aprofundamento)

### 3.5 Quatro estados, diauxia e o mapa geral
1. **A curva diáuxica tem platô porque a bactéria "descansa".** O platô é o tempo de induzir o operon: transcrever, traduzir e montar permease e β-galactosidase. (livro-texto)
2. **Operon indutível é sinônimo de operon com controle negativo.** Indutível/reprimível é sobre o sinal; positivo/negativo é sobre o efeito da proteína reguladora. As duas dimensões são independentes. (armadilha central)
3. **Operon trp é regulado só por atenuação.** Tem repressor com co-repressor (triptofano) *e* atenuação; são camadas que se somam. (banco NEBLI #318)
4. **Toda proteína reguladora é ou repressor ou ativador.** AraC do operon da arabinose é os dois, dependendo do ligante. (aprofundamento)
5. **Atenuação depende do splicing.** Não há splicing aqui: depende do acoplamento transcrição-tradução, um ribossomo lendo o peptídeo-líder enquanto a polimerase ainda avança. (armadilha)
