#import "../typst-template/nebli_v2_apostila.typ": *

#questao-mc("01", badge-consolidacao,
  [O que torna possível a uma bactéria coordenar a expressão de três enzimas de uma mesma via metabólica sem precisar de nenhum mecanismo regulatório adicional além do próprio arranjo do DNA:],
  (("A", [os três genes ficam sob um único promotor e são copiados num mRNA policistrônico único, de modo que qualquer decisão tomada na iniciação da transcrição atinge necessariamente os três ao mesmo tempo]),
   ("B", [cada gene tem promotor próprio, mas os três promotores compartilham a mesma sequência consenso, o que faz a subunidade sigma reconhecê-los simultaneamente e iniciar as três transcrições em paralelo]),
   ("C", [os três genes são transcritos separadamente e os mRNAs resultantes são unidos no citoplasma por uma ligase de RNA, formando um transcrito composto que o ribossomo traduz de uma só vez]),
   ("D", [a coordenação ocorre na tradução: um único sítio de ligação ao ribossomo serve aos três genes, e a estequiometria idêntica dos produtos garante que as três enzimas apareçam juntas]),
   ("E", [os três genes compartilham o mesmo terminador de transcrição, e é o terminador comum que sincroniza o término das três cópias e, por consequência, o aparecimento das três enzimas])))

#questao-mc("02", badge-consolidacao,
  [Uma cultura de #emph[E. coli] cresce em meio sem lactose. Descreva corretamente o que a ligação do repressor Lac ao operador impede que aconteça:],
  (("A", [a RNA polimerase ainda ocupa o promotor, mas fica impedida de abrir a dupla-hélice e escapar para o alongamento, porque o operador está sobreposto ao ponto de início da transcrição]),
   ("B", [a RNA polimerase é impedida de reconhecer e ocupar o promotor, porque o repressor recobre fisicamente as caixas -35 e -10 e as torna inacessíveis à subunidade sigma da holoenzima]),
   ("C", [o mRNA do operon continua sendo produzido normalmente, mas é degradado logo após a síntese por ribonucleases recrutadas pelo próprio repressor ligado à região do operador]),
   ("D", [os ribossomos ficam impedidos de encontrar o sítio de ligação de cada cistron, de modo que o transcrito é produzido em quantidade normal mas nunca chega a ser traduzido em proteína]),
   ("E", [a subunidade sigma é sequestrada pelo repressor e não consegue se acoplar ao núcleo da enzima, o que impede a formação da holoenzima capaz de reconhecer qualquer promotor da célula])))

#questao-ce("03", badge-consolidacao,
  [Julgue os itens sobre elementos que agem em cis e em trans no operon lac:],
  (("I",   [O operador é um elemento que age em cis: uma alteração nele afeta apenas os genes estruturais localizados na mesma molécula de DNA.]),
   ("II",  [O gene #emph[lacI] age em cis, porque está fisicamente próximo do operon que ele controla no cromossomo de #emph[E. coli].]),
   ("III", [O sítio de ligação da CAP, por estar a cerca de 60 pares de base do início da transcrição, age em trans sobre os dois operadores presentes num diploide parcial.]),
   ("IV",  [Um elemento age em trans quando seu produto é uma molécula difusível capaz de alcançar qualquer cópia de DNA presente na célula.])))

#questao-mc("04", badge-consolidacao,
  [Uma linhagem tem operador, promotor e gene #emph[lacI] perfeitamente selvagens, mas carrega uma deleção que inativa a β-galactosidase. Explique por que essa linhagem não induz o operon quando cresce em meio com lactose:],
  (("A", [o indutor fisiológico é a alolactose, isômero produzido pela própria β-galactosidase a partir da lactose; sem a enzima ativa, o sinal que retira o repressor do operador nunca chega a ser fabricado]),
   ("B", [a lactose intacta é o indutor, mas ela precisa antes ser fosforilada pela β-galactosidase para adquirir carga negativa e conseguir atravessar o sítio alostérico do repressor tetramérico]),
   ("C", [sem β-galactosidase a lactose se acumula no citoplasma e compete com a alolactose pelo mesmo sítio do repressor, deslocando o indutor verdadeiro e mantendo o operador continuamente ocupado]),
   ("D", [a β-galactosidase é necessária para degradar o repressor Lac já sintetizado; sem essa proteólise o tetrâmero permanece íntegro sobre o operador mesmo na presença de concentrações altas de indutor]),
   ("E", [a ausência de β-galactosidase impede a produção de galactose livre, que é o verdadeiro ligante alostérico do repressor e o único açúcar capaz de reduzir sua afinidade pela sequência do operador])))

#questao-mc("05", badge-consolidacao,
  [Explique o que significa dizer que a sequência consenso de um promotor bacteriano é TTGACA na região -35 e TATAAT na região -10:],
  (("A", [significa que todo promotor funcional de #emph[E. coli] contém exatamente essas duas sequências; promotores que divergem delas em qualquer posição não são reconhecidos pela subunidade sigma e não iniciam transcrição]),
   ("B", [significa que essas são as sequências do promotor mais forte já descrito na bactéria, e que os demais promotores foram derivados dele por acúmulo de mutações ao longo da história evolutiva da espécie]),
   ("C", [significa que, alinhando muitos promotores reais, essas são as bases mais frequentes em cada posição; nenhum promotor individual precisa ser idêntico a elas, e o grau de aproximação determina a força]),
   ("D", [significa que essas sequências são reconhecidas pelo núcleo da RNA polimerase, enquanto a subunidade sigma reconhece separadamente o espaçador de 17 pares de base que fica entre as duas caixas]),
   ("E", [significa que a transcrição começa dentro dessas duas caixas, uma delas fornecendo a base +1 e a outra fornecendo o molde inicial que a polimerase copia antes de escapar do promotor])))

#questao-ce("06", badge-consolidacao,
  [Uma placa de cultura contém meio sólido com X-Gal e IPTG. Julgue os itens:],
  (("I",   [O X-Gal atua como indutor do operon: ao entrar na célula, liga-se ao repressor Lac e reduz sua afinidade pelo operador.]),
   ("II",  [O IPTG induz o operon e não é metabolizado pela β-galactosidase, o que mantém a indução estável ao longo do crescimento da colônia.]),
   ("III", [Uma colônia azul indica que há β-galactosidase ativa clivando o X-Gal e liberando um produto que dimeriza e oxida a um pigmento índigo.]),
   ("IV",  [Uma colônia branca demonstra necessariamente que o gene #emph[lacZ] daquela linhagem foi deletado.])))

#questao-mc("07", badge-consolidacao,
  [Descreva corretamente a relação entre a concentração de glicose no meio e a atividade da proteína CAP:],
  (("A", [a glicose liga-se diretamente à CAP num sítio alostérico e a converte na forma capaz de reconhecer o sítio a montante do promotor, o que explica por que a ativação exige glicose disponível no meio]),
   ("B", [a glicose reduz a concentração intracelular de cAMP; sem cAMP ligado, a CAP não adota a conformação que reconhece o DNA e o promotor lac fica operando apenas com sua força intrínseca baixa]),
   ("C", [a glicose aumenta a concentração intracelular de cAMP, que se liga à CAP e a mantém presa ao sítio de ligação, o que garante recrutamento eficiente da polimerase enquanto houver glicose no meio]),
   ("D", [a glicose é convertida em cAMP pela adenilato-ciclase, de modo que a concentração do mensageiro acompanha a do açúcar e a CAP funciona como um medidor direto da oferta energética da célula]),
   ("E", [a glicose desloca o cAMP já ligado à CAP por competição pelo mesmo sítio, liberando a proteína do DNA e permitindo que o repressor Lac ocupe o operador imediatamente a jusante do promotor])))

#questao-mc("08", badge-consolidacao,
  [Sobre os elementos que compõem a região do operon lac, assinale a alternativa *incorreta*:],
  (("A", [o gene #emph[lacI] possui promotor próprio e é transcrito de forma contínua e independente, não fazendo parte do mRNA policistrônico que carrega as mensagens dos genes estruturais do operon]),
   ("B", [o gene #emph[lacY] codifica a lactose-permease, transportador de membrana sem o qual a entrada de lactose fica muito reduzida e a indução eficiente do operon deixa de acontecer]),
   ("C", [o operador está situado a montante do promotor, de modo que o repressor ligado a ele recobre as caixas -35 e -10 e impede o reconhecimento do promotor pela subunidade sigma da holoenzima]),
   ("D", [o sítio de ligação da CAP fica a montante do promotor, por volta da posição -61, em região distinta daquela ocupada pela RNA polimerase e daquela ocupada pelo repressor Lac]),
   ("E", [o gene #emph[lacZ] codifica a β-galactosidase, enzima que hidrolisa a lactose em glicose e galactose e que também produz, como reação secundária, o isômero que funciona como indutor])))

#questao-mc("09", badge-integracao,
  [Um mutante do #emph[lacI] produz cadeias polipeptídicas que se montam normalmente com cadeias selvagens, mas cujo domínio de ligação ao DNA está deformado. Em um diploide parcial que carrega esse alelo e um alelo selvagem, o resultado esperado e sua explicação são:],
  (("A", [expressão normalmente regulada, porque metade dos tetrâmeros formados contém apenas cadeias selvagens e essa fração é suficiente para ocupar os dois operadores e manter a repressão íntegra]),
   ("B", [expressão não-induzível, porque os tetrâmeros mistos perdem o sítio de ligação ao indutor e permanecem ancorados aos dois operadores mesmo quando a alolactose se acumula no citoplasma]),
   ("C", [expressão constitutiva, porque a maioria dos tetrâmeros montados incorpora ao menos uma cadeia deformada, o que inutiliza o complexo inteiro e caracteriza uma perda de função com efeito dominante]),
   ("D", [expressão constitutiva apenas na molécula que carrega o alelo mutante, porque o defeito de montagem só se manifesta nos tetrâmeros sintetizados nas proximidades do gene alterado]),
   ("E", [expressão normalmente regulada, porque a célula compensa o alelo defeituoso aumentando a transcrição do alelo selvagem até restaurar a concentração fisiológica de repressor funcional])))

#questao-mc("10", badge-integracao,
  [Uma linhagem hipotética tem repressão absoluta: o repressor Lac ligado ao operador reduz a transcrição a zero, sem qualquer vazamento. Prevê-se que essa linhagem, colocada em meio contendo apenas lactose como fonte de carbono, apresente:],
  (("A", [indução mais rápida que a linhagem selvagem, porque a ausência de transcrição residual concentra toda a maquinaria de transcrição disponível no operon assim que o primeiro indutor aparece]),
   ("B", [indução normal, porque a lactose atravessa a membrana por difusão simples em quantidade suficiente e se liga diretamente ao repressor sem depender de nenhuma enzima previamente existente]),
   ("C", [indução normal, porque o cAMP acumulado na ausência de glicose ativa a CAP e o recrutamento da polimerase pelo ativador dispensa a retirada prévia do repressor do operador]),
   ("D", [indução mais lenta, porém completa, porque a permease necessária para importar lactose é fornecida por outros transportadores de açúcar da membrana até que o operon alcance seu nível pleno]),
   ("E", [ausência de indução, porque sem permease e sem β-galactosidase residuais a lactose não entra em quantidade útil nem é convertida em alolactose, e o sinal que retiraria o repressor nunca se forma])))

#questao-mc("11", badge-integracao,
  [Considere o diploide parcial de genótipo I#super[+] P#super[+] O#super[c] Z#super[+] no cromossomo e I#super[-] P#super[+] O#super[+] Z#super[+] no plasmídeo. O comportamento esperado da produção de β-galactosidase, na ausência e na presença de IPTG, é:],
  (("A", [ausência de produção sem IPTG e produção pelas duas cópias com IPTG, porque o repressor produzido pelo alelo I#super[+] cromossômico difunde e silencia os dois operadores enquanto não houver indutor]),
   ("B", [produção pela cópia cromossômica sem IPTG e produção pelas duas cópias com IPTG, porque o operador mutante não reconhece o repressor difusível e o operador selvagem do plasmídeo reconhece]),
   ("C", [produção pelas duas cópias em ambas as condições, porque o alelo I#super[-] do plasmídeo impede a formação de qualquer repressor funcional na célula, tornando o sistema inteiramente constitutivo]),
   ("D", [produção apenas pela cópia plasmidial em ambas as condições, porque o operador mutante bloqueia a transcrição dos genes ligados a ele e transfere toda a expressão para a outra molécula]),
   ("E", [ausência de produção em ambas as condições, porque o alelo O#super[c] impede a ligação do ativador CAP e o promotor sozinho não sustenta transcrição detectável de β-galactosidase])))

#questao-ce("12", badge-integracao,
  [Quatro linhagens crescem em meio com X-Gal e IPTG, sem glicose, e todas produzem colônias brancas. Julgue as explicações propostas para cada caso:],
  (("I",   [Uma deleção no gene #emph[lacZ] produz colônia branca, porque não há enzima capaz de clivar o X-Gal, ainda que o operon esteja sendo transcrito normalmente.]),
   ("II",  [Uma mutação que destrói as caixas -35 e -10 do promotor produz colônia branca, porque a holoenzima não reconhece mais o sítio e a transcrição do operon deixa de ocorrer.]),
   ("III", [Um alelo lacI#super[s], cujo repressor perdeu o sítio de ligação ao indutor, produz colônia azul nessas condições, porque o IPTG do meio garante a indução do operon.]),
   ("IV",  [Uma mutação que inutiliza o sítio de ligação da CAP produz colônia branca absoluta, porque sem o ativador a transcrição do operon é reduzida a zero.])))

#questao-mc("13", badge-integracao,
  [Um pesquisador substitui as caixas -35 e -10 do promotor lac pelas sequências consenso, mantendo intactos o operador, o gene #emph[lacI] e o sítio da CAP. Prevê-se que, em meio com lactose e com glicose abundante, essa construção apresente:],
  (("A", [transcrição nula, porque o promotor consenso é reconhecido por uma subunidade sigma alternativa que não está disponível durante o crescimento em meio rico em glicose]),
   ("B", [transcrição idêntica à da construção selvagem, porque na presença de glicose o fator limitante é a ocupação do operador pelo repressor, e o operador não foi alterado pela substituição]),
   ("C", [transcrição nula, porque a ausência de dobra do DNA pela CAP impede a formação do complexo aberto independentemente da qualidade das sequências reconhecidas pela subunidade sigma]),
   ("D", [transcrição reduzida em relação à selvagem, porque promotores consenso ligam a holoenzima com afinidade tão alta que ela deixa de escapar para o alongamento e permanece retida no sítio]),
   ("E", [transcrição elevada, porque o operador está livre pela ação do indutor e o promotor agora recruta a polimerase por conta própria, deixando de depender da ativação por CAP-cAMP])))

#questao-mc("14", badge-integracao,
  [Uma linhagem tem o sistema de transporte de glicose alterado de tal modo que a proteína EIIA permanece constitutivamente fosforilada, mesmo com glicose abundante no meio. Prevê-se que, nessa linhagem crescendo em glicose e lactose:],
  (("A", [o operon lac seja transcrito em nível alto, porque a EIIA fosforilada mantém a adenilato-ciclase ativa, o cAMP elevado e a CAP capaz de dobrar o DNA e recrutar a polimerase]),
   ("B", [o operon lac permaneça no nível basal, porque a fosforilação da EIIA é irrelevante para a adenilato-ciclase e o que determina o cAMP é a concentração citoplasmática de glicose-6-fosfato]),
   ("C", [o operon lac seja completamente silenciado, porque a EIIA fosforilada liga-se ao operador e reforça a ação do repressor Lac, somando dois bloqueios sobre a mesma região do DNA]),
   ("D", [o operon lac seja transcrito em nível alto apenas se a lactose for retirada do meio, porque a EIIA fosforilada substitui a alolactose como ligante alostérico do repressor tetramérico]),
   ("E", [o operon lac permaneça silenciado, porque a EIIA fosforilada inibe a lactose-permease com mais intensidade que a forma desfosforilada, impedindo a entrada do açúcar indutor na célula])))

#questao-ce("15", badge-integracao,
  [Julgue os itens sobre o mRNA policistrônico do operon lac e seus produtos:],
  (("I",   [O transcrito é traduzido como uma poliproteína única, que em seguida é clivada por proteases específicas em três polipeptídeos separados.]),
   ("II",  [Um único mRNA carrega as sequências codificantes de #emph[lacZ], #emph[lacY] e #emph[lacA], e cada uma delas possui seu próprio sítio de ligação ao ribossomo.]),
   ("III", [A eficiência distinta de cada sítio de ligação ao ribossomo, somada à degradação progressiva do transcrito, faz com que a β-galactosidase seja produzida em quantidade maior que a transacetilase.]),
   ("IV",  [A tradução do transcrito só pode começar depois que a RNA polimerase o libera por inteiro, o que separa no tempo a transcrição e a tradução em bactérias.])))

#questao-mc("16", badge-integracao,
  [O operon lac contém uma alça de retroalimentação positiva. Identifique o par de elementos que a constitui e explique como ela opera:],
  (("A", [o repressor e o operador: quanto mais repressor a célula produz, mais operadores ficam ocupados, e a queda de transcrição resultante reduz a síntese do próprio repressor num circuito autolimitado]),
   ("B", [a CAP e o cAMP: quanto mais CAP ativa se liga ao sítio a montante, maior a produção de adenilato-ciclase codificada pelo operon, o que eleva ainda mais o cAMP disponível na célula]),
   ("C", [a transacetilase e a permease: a transacetilase modifica galactosídeos tóxicos e assim protege a permease da inativação, permitindo entrada progressivamente maior de lactose na célula]),
   ("D", [o promotor e a subunidade sigma: a transcrição do operon libera moléculas de sigma que reingressam no ciclo e aumentam a frequência de reconhecimento do próprio promotor lac]),
   ("E", [a permease e a β-galactosidase: mais permease traz mais lactose, mais β-galactosidase converte parte dela em alolactose, mais repressores se soltam e mais dos dois produtos são sintetizados])))

#questao-mc("17", badge-integracao,
  [Sobre a posição do operador e a etapa da transcrição que ele bloqueia, assinale a alternativa *incorreta*:],
  (("A", [o operador está sobreposto ao ponto de início da transcrição, e é essa sobreposição que permite ao repressor interferir num evento posterior ao reconhecimento do promotor pela holoenzima]),
   ("B", [o bloqueio imposto pelo repressor pode ser superado pela substituição do promotor lac por um promotor mais forte, porque a etapa limitante nesse estado é a afinidade da holoenzima pelo sítio]),
   ("C", [a repressão reduz a transcrição em cerca de mil vezes, e o resíduo que persiste decorre da natureza reversível da ligação entre o tetrâmero repressor e a sequência do operador]),
   ("D", [a RNA polimerase consegue ocupar o promotor mesmo com o repressor ligado, de modo que descrever a repressão como impedimento ao pouso da enzima descreve mal o mecanismo real]),
   ("E", [o resíduo de transcrição que escapa da repressão tem papel funcional, por manter na célula as poucas moléculas de permease e de β-galactosidase necessárias para a indução começar])))

#questao-ce("18", badge-integracao,
  [Julgue os itens sobre as duas alavancas pelas quais a glicose reduz a expressão do operon lac:],
  (("I",   [A repressão por catabólito atua sobre o braço positivo: com glicose entrando, o cAMP cai e a CAP deixa de ser capaz de reconhecer seu sítio no DNA.]),
   ("II",  [A exclusão do indutor consiste na inibição da lactose-permease pela EIIA desfosforilada, o que reduz a entrada do açúcar que originaria o indutor.]),
   ("III", [A repressão por catabólito recebe esse nome porque a glicose ativa um repressor que se liga ao operador em conjunto com o repressor Lac.]),
   ("IV",  [As duas alavancas são disparadas pelo mesmo evento, o transporte de glicose pelo sistema de fosfotransferase, mas atuam sobre alvos moleculares diferentes.])))

#questao-mc("19", badge-integracao,
  [Duas linhagens crescem em meio com IPTG, X-Gal e sem glicose. A linhagem 1 forma colônias brancas e a linhagem 2 forma colônias azuis intensas mesmo quando o IPTG é retirado. Os genótipos mais compatíveis com esses resultados são, respectivamente:],
  (("A", [linhagem 1 com operador mutante e linhagem 2 com repressor incapaz de responder ao indutor, porque o operador alterado silencia os genes ligados a ele e o repressor cego libera a transcrição]),
   ("B", [linhagem 1 com sítio da CAP inutilizado e linhagem 2 com promotor substituído pelo consenso, porque nenhuma das duas alterações mantém qualquer resposta ao indutor adicionado ao meio]),
   ("C", [linhagem 1 com deleção da permease e linhagem 2 com deleção da transacetilase, porque ambas as enzimas participam diretamente da conversão do X-Gal no pigmento azul insolúvel]),
   ("D", [linhagem 1 com repressor que perdeu o sítio do indutor e linhagem 2 com operador que o repressor não reconhece, porque a primeira é não-induzível e a segunda é constitutiva]),
   ("E", [linhagem 1 com adenilato-ciclase inativa e linhagem 2 com excesso de cAMP, porque a primeira não ativa a CAP e a segunda mantém o ativador permanentemente ligado ao seu sítio])))

#questao-mc("20", badge-integracao,
  [Num diploide parcial com genótipo I#super[+] P#super[+] O#super[c] Z#super[-] no cromossomo e I#super[+] P#super[+] O#super[+] Z#super[+] no plasmídeo, a produção de β-galactosidase na ausência de indutor será:],
  (("A", [alta, porque o operador mutante do cromossomo mantém aquela molécula em transcrição contínua e o gene estrutural do plasmídeo fornece a enzima funcional que falta na cópia cromossômica]),
   ("B", [alta, porque o repressor produzido pelas duas cópias do gene regulador é titulado pelos dois operadores presentes e sobra pouca proteína livre para manter qualquer um deles ocupado]),
   ("C", [intermediária, porque metade dos transcritos produzidos na célula vem da molécula constitutiva e essa metade é suficiente para gerar enzima funcional a partir do gene selvagem]),
   ("D", [nula ou residual, porque a molécula que transcreve de forma constitutiva carrega um gene estrutural inativo e a molécula que carrega o gene funcional está com o operador reprimido]),
   ("E", [nula ou residual, porque o alelo O#super[c] é dominante e impõe silenciamento constitutivo às duas moléculas presentes na célula, independentemente do estado dos genes estruturais])))

#questao-ce("21", badge-integracao,
  [Julgue os itens sobre a combinação dos dois braços de regulação do operon lac:],
  (("I",   [Na ausência de lactose, o estado de ativação da CAP é irrelevante para a transcrição do operon, porque o repressor bloqueia uma etapa posterior ao recrutamento da polimerase.]),
   ("II",  [Com lactose presente e glicose abundante, o operador está livre e a transcrição atinge seu nível máximo.]),
   ("III", [A transcrição alta exige simultaneamente operador desocupado e CAP ativa, o que faz do operon uma conjunção de duas condições independentes.]),
   ("IV",  [Com glicose baixa e lactose ausente, o cAMP elevado mantém a CAP ligada ao seu sítio, mas a transcrição permanece no nível reprimido.])))

#questao-mc("22", badge-integracao,
  [Um promotor sintético é construído com as caixas -35 e -10 exatamente iguais ao consenso, porém separadas por 24 pares de base em vez dos 17 habituais. Prevê-se que esse promotor seja:],
  (("A", [mais forte que o consenso canônico, porque o espaçamento maior facilita a abertura da dupla-hélice entre as duas caixas e reduz a energia necessária para formar a bolha de transcrição]),
   ("B", [equivalente ao consenso canônico, porque a força de um promotor depende exclusivamente da identidade das bases nas duas caixas, e ambas foram mantidas idênticas ao padrão de referência]),
   ("C", [reconhecido apenas pelo núcleo da RNA polimerase sem a subunidade sigma, o que resulta em iniciação aleatória ao longo de todo o trecho de DNA situado entre as duas caixas conservadas]),
   ("D", [mais forte apenas na presença da CAP, porque a dobra imposta pelo ativador ao DNA reduz a distância efetiva entre as caixas e restaura o alinhamento perdido pelo espaçamento excessivo]),
   ("E", [mais fraco que o consenso canônico, porque os dois domínios de reconhecimento da subunidade sigma ficam a uma distância fixa entre si e não alcançam as duas caixas ao mesmo tempo])))

#questao-ce("23", badge-integracao,
  [Julgue os itens que comparam o operon lac e o operon trp:],
  (("I",   [O operon lac controla uma via catabólica e é indutível: o metabólito relacionado ao substrato retira o repressor do operador.]),
   ("II",  [O operon trp controla uma via anabólica e é reprimível: o triptofano funciona como co-repressor, tornando o TrpR capaz de ligar o operador.]),
   ("III", [O operon trp possui, além da repressão pelo TrpR, um mecanismo de atenuação que decide se a transcrição prossegue além da região líder.]),
   ("IV",  [Tanto no lac quanto no trp o pequeno metabólito atua reduzindo a afinidade da proteína reguladora pela sequência do operador.])))

#questao-mc("24", badge-integracao,
  [Sobre o mecanismo pelo qual a CAP ativa a transcrição do operon lac, assinale a alternativa *incorreta*:],
  (("A", [a CAP ligada ao seu sítio dobra a dupla-hélice de forma acentuada, e essa deformação reposiciona o ativador em relação à região onde a RNA polimerase se acomoda no promotor]),
   ("B", [o contato entre a superfície da CAP e o domínio carboxi-terminal da subunidade alfa da polimerase fornece energia livre favorável e estabiliza a holoenzima sobre um promotor divergente]),
   ("C", [a CAP altera as sequências das caixas -35 e -10 do promotor lac, convertendo-as no padrão consenso e tornando desnecessária a manutenção do ativador ligado durante a transcrição]),
   ("D", [a CAP só reconhece o DNA depois de ligar cAMP, de modo que sua atividade reflete indiretamente o fluxo de glicose através do sistema de transporte por fosfotransferase]),
   ("E", [o efeito da CAP compensa a perda de contatos causada pela divergência do promotor lac em relação ao consenso, sem alterar a sequência de nenhum dos elementos envolvidos])))

#questao-ce("25", badge-integracao,
  [Julgue os itens sobre a atenuação no operon trp e sua dependência da organização celular procariótica:],
  (("I",   [A atenuação poderia operar em uma célula eucariótica de maneira idêntica, uma vez que depende apenas da estrutura secundária do RNA transcrito.]),
   ("II",  [Com triptofano escasso, o ribossomo avança rapidamente pela região líder e favorece a formação do grampo terminador, abortando a transcrição.]),
   ("III", [A atenuação depende de um ribossomo traduzir um peptídeo-líder no mRNA que ainda está sendo sintetizado pela RNA polimerase.]),
   ("IV",  [O acoplamento entre transcrição e tradução que a atenuação exige é possível porque, em procariotos, não há envoltório nuclear separando os dois processos.])))

#questao-mc("26", badge-aplicacao,
  [Uma indústria farmacêutica produz insulina humana recombinante em #emph[E. coli]. O gene da insulina foi colocado sob controle de um operador lac, e o fermentador só recebe o indutor quando a cultura atinge densidade elevada. Explique a razão dessa estratégia:],
  (("A", [o indutor é necessário para que a bactéria metabolize a lactose do meio de cultura, e adicioná-lo cedo demais esgotaria a fonte de carbono antes que a cultura atingisse a densidade desejada]),
   ("B", [a adição tardia do indutor permite que o repressor seja degradado gradualmente ao longo do crescimento, o que sincroniza a produção de insulina entre todas as células da população]),
   ("C", [o indutor precisa ser adicionado quando o cAMP já caiu, porque só nessas condições a CAP se desliga do sítio e libera o promotor para a transcrição eficiente do gene heterólogo]),
   ("D", [a expressão precoce do gene aumentaria a concentração de alolactose no meio, e o excesso de indutor natural saturaria o repressor antes que a cultura alcançasse a densidade necessária]),
   ("E", [manter o operador reprimido durante o crescimento evita o custo metabólico e a toxicidade de produzir uma proteína estranha; a indução na hora certa concentra esse custo na fase de produção])))

#questao-ce("27", badge-aplicacao,
  [Um laboratório clona um fragmento de DNA humano dentro do início do gene #emph[lacZ] de um plasmídeo e semeia as bactérias transformadas em meio com X-Gal e IPTG. Julgue os itens:],
  (("I",   [As colônias que receberam o fragmento inserido aparecem brancas, porque a interrupção do #emph[lacZ] impede a produção de β-galactosidase funcional.]),
   ("II",  [As colônias azuis correspondem a plasmídeos que se recircularizaram sem inserto, mantendo o #emph[lacZ] íntegro.]),
   ("III", [A presença de IPTG no meio é dispensável, porque o X-Gal já induz por si só a transcrição do operon no plasmídeo.]),
   ("IV",  [Uma colônia branca garante que o fragmento inserido está na orientação correta para expressar a proteína humana.])))

#questao-mc("28", badge-aplicacao,
  [Um estudante cultiva #emph[E. coli] em meio contendo glicose e lactose e registra a curva de crescimento. Observa duas fases exponenciais separadas por um platô de aproximadamente vinte minutos. A explicação mecanística correta para o platô é:],
  (("A", [durante o platô a bactéria consome o oxigênio residual do meio e passa ao metabolismo fermentativo, o que reduz o rendimento energético e interrompe temporariamente a divisão celular]),
   ("B", [o platô corresponde ao tempo necessário para que a lactose acumulada seja transportada para fora da célula, evitando a toxicidade osmótica antes que o metabolismo do segundo açúcar comece]),
   ("C", [o platô reflete a degradação do repressor Lac acumulado durante a primeira fase, processo que depende de proteases e só se completa após o esgotamento total da glicose do meio]),
   ("D", [ao esgotar a glicose, o cAMP sobe e a CAP é ativada, mas o operon ainda precisa ser transcrito e traduzido até que haja permease e β-galactosidase suficientes para sustentar o crescimento]),
   ("E", [o platô resulta da queda de pH provocada pelos ácidos orgânicos liberados na primeira fase, e o crescimento só recomeça depois que o tampão do meio restabelece as condições fisiológicas])))

#questao-ce("29", badge-aplicacao,
  [Uma cepa de #emph[E. coli] isolada de urina é analisada em laboratório. Ela cresce normalmente em glicose, mas não consegue usar lactose como única fonte de carbono. O sequenciamento mostra o gene #emph[lacZ] íntegro e o gene #emph[lacI] íntegro. Julgue os itens:],
  (("I",   [Uma mutação que inutilize as caixas -35 e -10 do promotor lac explicaria o fenótipo, porque sem transcrição do operon não há permease nem β-galactosidase.]),
   ("II",  [Um alelo lacI#super[s] explicaria o fenótipo mesmo com o gene íntegro, porque o super-repressor resulta de uma modificação pós-traducional do repressor selvagem.]),
   ("III", [Uma deleção do sítio de ligação da CAP explicaria o fenótipo de forma completa, porque sem o ativador a transcrição do operon é reduzida a zero.]),
   ("IV",  [Uma mutação que inative o gene #emph[lacY] explicaria o fenótipo, porque sem a permease a lactose praticamente não entra na célula.])))

#questao-mc("30", badge-aplicacao,
  [Um grupo de pesquisa constrói um circuito genético sintético em que um gene repórter é colocado sob controle simultâneo de um operador lac e de um sítio de ligação para um ativador. O objetivo declarado é obter alta amplitude de resposta entre o estado desligado e o estado ligado. A escolha de promotor mais coerente com esse objetivo é:],
  (("A", [um promotor com as caixas consenso e espaçamento canônico, porque a amplitude de resposta depende sobretudo do nível máximo alcançável e esse é o promotor com maior taxa de iniciação]),
   ("B", [um promotor sem caixa -35 reconhecível, porque a dependência total do ativador elimina qualquer expressão residual e garante que o estado desligado tenha transcrição rigorosamente nula]),
   ("C", [um promotor consenso combinado com a remoção do operador, porque manter apenas o controle positivo simplifica o circuito e evita interferência entre o repressor e o ativador ligados ao DNA]),
   ("D", [um promotor reconhecido por uma subunidade sigma alternativa, porque a competição entre fatores sigma amplia a diferença entre os dois estados sem depender da qualidade das caixas conservadas]),
   ("E", [um promotor divergente do consenso, porque um nível basal baixo deixa espaço para o ativador construir uma diferença grande, enquanto um promotor forte já opera perto do teto e não sobe])))
