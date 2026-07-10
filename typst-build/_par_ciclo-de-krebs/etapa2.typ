#import "../../typst-template/nebli_v2_apostila.typ": *

#set-etapa("Etapa 2 — questões objetivas")

// ================================
// CONSOLIDAÇÃO (Q01-Q10) — verde
// ================================

#questao-mc("01", badge-consolidacao,
  [Em qual compartimento celular ocorrem todas as 8 reações do ciclo de Krebs?],
  (("A", [Citosol]),
   ("B", [Espaço intermembrana mitocondrial]),
   ("C", [Matriz mitocondrial]),
   ("D", [Retículo endoplasmático]),
   ("E", [Membrana mitocondrial externa])))

#questao-mc("02", badge-consolidacao,
  [Uma volta completa do ciclo de Krebs, a partir de uma molécula de acetil-CoA, produz:],
  (("A", [2 NADH, 2 FADH₂, 1 GTP e 1 CO₂]),
   ("B", [3 NADH, 1 FADH₂, 1 GTP e 2 CO₂]),
   ("C", [1 NADH, 1 FADH₂, 2 GTP e 2 CO₂]),
   ("D", [3 NADH, 2 FADH₂, 1 GTP e 3 CO₂]),
   ("E", [4 NADH, 1 FADH₂, 0 GTP e 2 CO₂])))

#questao-mc("03", badge-consolidacao,
  [O complexo da piruvato desidrogenase catalisa a conversão de:],
  (("A", [Acetil-CoA em citrato]),
   ("B", [Piruvato em lactato]),
   ("C", [Piruvato em acetil-CoA, com liberação de CO₂ e geração de NADH]),
   ("D", [Oxaloacetato em malato]),
   ("E", [Citrato em isocitrato])))

#questao-mc("04", badge-consolidacao,
  [O ciclo de Krebs também é conhecido como ciclo do ácido cítrico porque o citrato é:],
  (("A", [O substrato consumido na última reação]),
   ("B", [O produto formado na primeira reação, a partir da condensação entre acetil-CoA e oxaloacetato]),
   ("C", [O único intermediário com 6 carbonos]),
   ("D", [O composto que liga o ciclo à cadeia respiratória]),
   ("E", [O regulador alostérico negativo principal da piruvato desidrogenase])))

#questao-mc("05", badge-consolidacao,
  [A única reação do ciclo de Krebs que gera diretamente um nucleotídeo trifosfato por fosforilação em nível de substrato é catalisada por:],
  (("A", [Citrato sintase]),
   ("B", [Isocitrato desidrogenase]),
   ("C", [α-cetoglutarato desidrogenase]),
   ("D", [Succinil-CoA sintetase]),
   ("E", [Malato desidrogenase])))

#questao-mc("06", badge-consolidacao,
  [A enzima do ciclo de Krebs que gera FADH₂ em vez de NADH é a:],
  (("A", [Isocitrato desidrogenase]),
   ("B", [Malato desidrogenase]),
   ("C", [α-cetoglutarato desidrogenase]),
   ("D", [Succinato desidrogenase]),
   ("E", [Fumarase])))

#questao-mc("07", badge-consolidacao,
  [Quantas moléculas de CO₂ são liberadas a cada volta completa do ciclo de Krebs?],
  (("A", [1]),
   ("B", [2]),
   ("C", [3]),
   ("D", [4]),
   ("E", [6])))

#questao-mc("08", badge-consolidacao,
  [A coenzima associada à enzima E1 do complexo da piruvato desidrogenase é derivada da vitamina:],
  (("A", [B1 (tiamina)]),
   ("B", [B2 (riboflavina)]),
   ("C", [B3 (niacina)]),
   ("D", [B5 (ácido pantotênico)]),
   ("E", [B12 (cobalamina)])))

#questao-mc("09", badge-consolidacao,
  [A succinato desidrogenase é uma enzima singular no ciclo de Krebs porque:],
  (("A", [Catalisa a única reação reversível do ciclo]),
   ("B", [É a única enzima do ciclo ancorada na membrana mitocondrial interna, sendo também o Complexo II da cadeia respiratória]),
   ("C", [Não requer coenzima alguma para funcionar]),
   ("D", [Produz GTP em vez de FADH₂]),
   ("E", [Atua em conjunto com a piruvato carboxilase])))

#questao-ce("10", badge-consolidacao,
  [Julgue os itens sobre a etapa de entrada do ciclo de Krebs:],
  (("I", [O acetil-CoA carrega um grupo acetil ligado à coenzima A por uma ligação tioéster de alta energia.]),
   ("II", [A piruvato desidrogenase pertence ao ciclo de Krebs propriamente dito.]),
   ("III", [A reação catalisada pelo complexo da piruvato desidrogenase é uma descarboxilação oxidativa.]),
   ("IV", [O acetil-CoA pode também ser gerado pela β-oxidação de ácidos graxos na matriz mitocondrial.])))

// ================================
// INTEGRAÇÃO (Q11-Q25) — azul
// ================================

#questao-mc("11", badge-integracao,
  [A deficiência de tiamina afeta simultaneamente o complexo da piruvato desidrogenase e a α-cetoglutarato desidrogenase porque:],
  (("A", [Ambos catalisam reações de hidratação que dependem de B1]),
   ("B", [Ambos são complexos multienzimáticos que utilizam TPP como coenzima essencial para a descarboxilação oxidativa]),
   ("C", [A tiamina é o aceptor final de elétrons em ambas as reações]),
   ("D", [A B1 atua como regulador alostérico de ambos]),
   ("E", [Ambos consomem GTP, e a tiamina é necessária para sua síntese])))

#questao-mc("12", badge-integracao,
  [O FADH₂ produzido no ciclo de Krebs rende menos ATP por molécula do que o NADH porque:],
  (("A", [O FADH₂ tem menor potencial redutor e por isso doa menos elétrons]),
   ("B", [O FADH₂ é oxidado no citosol enquanto o NADH é oxidado na mitocôndria]),
   ("C", [O FADH₂ entra na cadeia respiratória diretamente na ubiquinona, pulando o Complexo I e portanto bombeando menos prótons]),
   ("D", [O FADH₂ é convertido em NAD⁺ antes de chegar à cadeia respiratória]),
   ("E", [O FADH₂ requer transporte ativo pela membrana, gastando ATP no processo])))

#questao-ce("13", badge-integracao,
  [Sobre a regulação do complexo da piruvato desidrogenase, julgue os itens:],
  (("I", [A PDH quinase fosforila e inativa o complexo, sendo estimulada por altos níveis de ATP, NADH e acetil-CoA.]),
   ("II", [A PDH fosfatase é ativada por Ca²⁺, ligando contração muscular à produção de ATP.]),
   ("III", [O acúmulo de piruvato inibe a PDH quinase, mantendo o complexo ativo.]),
   ("IV", [A insulina inibe a PDH fosfatase, reduzindo a entrada de piruvato no ciclo durante o estado alimentado.])))

#questao-mc("14", badge-integracao,
  [O envenenamento por fluoracetato (rodenticida) leva à paralisação do ciclo de Krebs porque:],
  (("A", [Inibe diretamente a citrato sintase, impedindo a entrada do acetil-CoA no ciclo]),
   ("B", [É convertido pela citrato sintase em fluorocitrato, que se liga irreversivelmente à aconitase e bloqueia a isomerização do citrato]),
   ("C", [Sequestra o oxaloacetato disponível, impedindo a primeira reação]),
   ("D", [Liga-se à coenzima A, impedindo a formação de acetil-CoA]),
   ("E", [Despolariza a membrana mitocondrial interna, dissipando o gradiente de prótons])))

#questao-mc("15", badge-integracao,
  [A piruvato carboxilase é considerada a principal reação anaplerótica do ciclo de Krebs porque:],
  (("A", [Acelera a velocidade do ciclo ao consumir piruvato em excesso]),
   ("B", [Repõe o oxaloacetato consumido em vias biossintéticas como gliconeogênese e síntese de aspartato, e é alostericamente ativada pelo acúmulo de acetil-CoA]),
   ("C", [Catalisa a etapa irreversível do ciclo, controlando seu sentido]),
   ("D", [É a única reação do ciclo que ocorre fora da mitocôndria]),
   ("E", [Produz GTP, complementando a fosforilação em nível de substrato])))

#questao-ce("16", badge-integracao,
  [Sobre a função anfibólica do ciclo de Krebs, julgue os itens:],
  (("I", [O α-cetoglutarato pode ser desviado do ciclo para a síntese de glutamato e outros aminoácidos.]),
   ("II", [O succinil-CoA é um precursor da síntese do grupo heme.]),
   ("III", [O citrato sai da mitocôndria para o citosol, onde é utilizado na síntese de ácidos graxos.]),
   ("IV", [Todos os intermediários do ciclo são consumidos exclusivamente em vias catabólicas.])))

#questao-mc("17", badge-integracao,
  [A interrupção do suprimento de oxigênio paralisa o ciclo de Krebs, ainda que nenhuma das 8 reações do ciclo utilize O₂ diretamente, porque:],
  (("A", [A ausência de O₂ inibe alostericamente a citrato sintase]),
   ("B", [Sem O₂, a cadeia respiratória trava, o NADH não é reoxidado a NAD⁺, e a falta de NAD⁺ paralisa as reações 3, 4 e 8 do ciclo]),
   ("C", [O O₂ é necessário para a regeneração do oxaloacetato pela malato desidrogenase]),
   ("D", [A ausência de O₂ ativa a piruvato carboxilase, desviando todo o piruvato]),
   ("E", [O CO₂ acumulado em condições anaeróbias inibe a aconitase])))

#questao-mc("18", badge-integracao,
  [O valor de ~30-32 ATP por molécula de glicose oxidada completamente substituiu o valor histórico de 38 ATP porque:],
  (("A", [O ciclo de Krebs foi reinterpretado como gerando menos NADH do que se pensava]),
   ("B", [Os valores modernos consideram que cada NADH rende ~2,5 ATP e cada FADH₂ ~1,5 ATP, refletindo a estequiometria real da ATP sintase e o custo do transporte do NADH citosólico]),
   ("C", [A descoberta da β-oxidação alterou o balanço]),
   ("D", [A glicólise foi corrigida para gerar apenas 1 ATP líquido]),
   ("E", [A piruvato desidrogenase deixou de ser contabilizada no balanço total])))

#questao-mc("19", badge-integracao,
  [Entre as 8 reações do ciclo de Krebs, qual NÃO produz nem NADH nem FADH₂?],
  (("A", [Isocitrato desidrogenase]),
   ("B", [α-cetoglutarato desidrogenase]),
   ("C", [Succinato desidrogenase]),
   ("D", [Fumarase]),
   ("E", [Malato desidrogenase])))

#questao-mc("20", badge-integracao,
  [O íon Ca²⁺ é um sinal central que liga atividade contrátil à produção de ATP por ativar simultaneamente:],
  (("A", [A piruvato desidrogenase quinase e a citrato sintase]),
   ("B", [A piruvato desidrogenase fosfatase, a isocitrato desidrogenase e a α-cetoglutarato desidrogenase]),
   ("C", [Apenas a piruvato carboxilase]),
   ("D", [A fumarase e a succinato desidrogenase]),
   ("E", [A succinil-CoA sintetase e a malato desidrogenase])))

#questao-mc("21", badge-integracao,
  [Entre as biomoléculas listadas, qual depende do succinil-CoA proveniente do ciclo de Krebs como precursor central de sua biossíntese?],
  (("A", [Glutamato]),
   ("B", [Ácidos graxos]),
   ("C", [Heme]),
   ("D", [Aspartato]),
   ("E", [Glicose])))

#questao-ce("22", badge-integracao,
  [Sobre as oito reações do ciclo de Krebs, julgue os itens:],
  (("I", [A condensação entre acetil-CoA e oxaloacetato é altamente exergônica e, na prática, irreversível, sendo um ponto de regulação do ciclo.]),
   ("II", [A primeira descarboxilação oxidativa do ciclo é catalisada pela isocitrato desidrogenase e gera o primeiro NADH e o primeiro CO₂.]),
   ("III", [A reação catalisada pela fumarase é uma desidrogenação que gera FADH₂.]),
   ("IV", [A regeneração do oxaloacetato pela malato desidrogenase gera o terceiro NADH da volta.])))

#questao-mc("23", badge-integracao,
  [Experimentos com isótopos radioativos mostraram que, em uma primeira volta do ciclo, os dois carbonos liberados como CO₂:],
  (("A", [Correspondem exatamente aos dois carbonos do acetil-CoA que acabou de entrar]),
   ("B", [Vêm originalmente do oxaloacetato, enquanto os carbonos do acetil permanecem no ciclo e só são oxidados em voltas posteriores]),
   ("C", [Vêm da hidrólise da coenzima A]),
   ("D", [São formados pela descarboxilação do citrato em uma reação anterior à isocitrato desidrogenase]),
   ("E", [Vêm metade do acetil e metade do oxaloacetato])))

#questao-mc("24", badge-integracao,
  [Entre as enzimas regulatórias do ciclo de Krebs, qual é ativada alostericamente por ADP e Ca²⁺ e inibida por ATP e NADH?],
  (("A", [Citrato sintase]),
   ("B", [Aconitase]),
   ("C", [Isocitrato desidrogenase]),
   ("D", [Succinato desidrogenase]),
   ("E", [Malato desidrogenase])))

#questao-ce("25", badge-integracao,
  [Sobre a regulação integrada do metabolismo aeróbio, julgue os itens:],
  (("I", [Altos níveis de ATP e NADH inibem a citrato sintase, a isocitrato desidrogenase e a α-cetoglutarato desidrogenase.]),
   ("II", [O acetil-CoA, ao se acumular, ativa alostericamente a piruvato carboxilase, sinalizando a necessidade de reposição de oxaloacetato.]),
   ("III", [A ativação da PDH fosfatase pelo Ca²⁺ desliga a piruvato desidrogenase durante o exercício.]),
   ("IV", [A insulina favorece o estado oxidativo ativando indiretamente a piruvato desidrogenase no fígado e no tecido adiposo.])))

// ================================
// APLICAÇÃO (Q26-Q30) — violeta
// PARIDADE RIGOROSA: ratio palavras(correta)/palavras(maior distratora) ≤ 1.25
// ================================

#questao-mc("26", badge-aplicacao,
  [Um homem de 52 anos, alcoolista crônico, chega ao pronto-socorro confuso, com ataxia de marcha e nistagmo. A primeira conduta nutricional do plantonista deve ser:],
  (("A", [Administrar solução glicosada hipertônica em bolus imediatamente para reverter possível hipoglicemia profunda e prevenir lesão neurológica progressiva por privação energética cerebral no quadro descrito.]),
   ("B", [Repor tiamina por via intravenosa antes de qualquer aporte de glicose, porque a glicose dispara consumo do estoque residual de B1 e pode precipitar encefalopatia de Wernicke aguda.]),
   ("C", [Suspender qualquer aporte calórico por 24 horas para permitir estabilização do equilíbrio ácido-base intracelular e evitar piora progressiva da síndrome de Korsakoff já presumivelmente instalada no caso.]),
   ("D", [Iniciar dieta hiperproteica enteral imediata para fornecer aminoácidos cetogênicos que sustentem o metabolismo neuronal até a recuperação espontânea da via oxidativa cerebral comprometida pelo álcool.]),
   ("E", [Administrar bicarbonato de sódio endovenoso para corrigir a acidose láctica grave esperada pelo bloqueio funcional do complexo da piruvato desidrogenase no quadro de privação descrito.])))

#questao-mc("27", badge-aplicacao,
  [Em jejum prolongado, o fígado produz grandes quantidades de corpos cetônicos a partir do acetil-CoA derivado da β-oxidação de ácidos graxos. O mecanismo bioquímico fundamental que explica essa cetogênese é:],
  (("A", [A inibição direta do ciclo de Krebs pelos próprios corpos cetônicos circulantes, que retroalimentam negativamente a via para evitar saturação metabólica do fígado.]),
   ("B", [O oxaloacetato hepático é desviado em massa para a gliconeogênese, faltando OAA para condensar com o acetil-CoA acumulado, que então é desviado para a síntese de corpos cetônicos.]),
   ("C", [A piruvato carboxilase é inibida pela queda da glicemia, impedindo qualquer reposição anaplerótica de intermediários do ciclo durante o estado de privação prolongada de carboidratos.]),
   ("D", [A deficiência de oxigênio tecidual durante o jejum paralisa a cadeia respiratória, impedindo a oxidação do acetil-CoA no ciclo de Krebs hepático e desviando-o para cetogênese.]),
   ("E", [A insulina basal do jejum estimula diretamente as enzimas cetogênicas hepáticas, num mecanismo paradoxal de adaptação metabólica ainda incompletamente compreendido.])))

#questao-mc("28", badge-aplicacao,
  [Um homem de 30 anos é admitido com náusea intensa, vômito, dor abdominal e fibrilação ventricular cerca de 40 minutos após ingerir acidentalmente um pó destinado a controle de roedores. O mecanismo bioquímico mais provável para o quadro é:],
  (("A", [Bloqueio direto da cadeia respiratória na altura do Complexo IV por monóxido de carbono ou cianeto, impedindo a transferência final de elétrons ao oxigênio molecular nos tecidos.]),
   ("B", [Conversão do fluoracetato em fluorocitrato dentro das células, com bloqueio irreversível da aconitase, paralisação do ciclo de Krebs e colapso da produção mitocondrial de NADH e FADH₂.]),
   ("C", [Inibição alostérica da piruvato desidrogenase por análogo estrutural da tiamina, levando ao acúmulo de piruvato no citosol e desvio massivo para a fermentação láctica com acidose grave.]),
   ("D", [Despolarização generalizada da membrana mitocondrial interna por um ionóforo de prótons, dissipando o gradiente eletroquímico e desacoplando a fosforilação oxidativa da respiração celular.]),
   ("E", [Inibição competitiva da succinato desidrogenase por malonato, interrompendo a regeneração do oxaloacetato e cessando a produção de FADH₂ na membrana mitocondrial interna afetada.])))

#questao-mc("29", badge-aplicacao,
  [Em um paciente com infarto agudo do miocárdio por oclusão coronária total, a necrose dos cardiomiócitos começa em minutos. O mecanismo metabólico que explica essa rapidez é:],
  (("A", [A queda do aporte de O₂ paralisa a cadeia respiratória, o NADH gerado pelo ciclo e pela PDH não consegue ser reoxidado, o NAD⁺ se esgota e o ciclo congela em minutos por falta de cofator.]),
   ("B", [A oclusão coronária bloqueia diretamente o transporte de glicose para os cardiomiócitos, paralisando a glicólise no citosol e impedindo qualquer geração de piruvato ou NADH naquele tecido isquêmico.]),
   ("C", [A isquemia ativa a fosfolipase A₂ mitocondrial, que degrada a cardiolipina da membrana interna e dissocia a ATP sintase do complexo respiratório em segundos após a interrupção do fluxo coronário.]),
   ("D", [O acúmulo de lactato no tecido isquêmico inibe a piruvato desidrogenase, e a via glicolítica anaeróbia compensatória se torna insuficiente para manter a integridade das bombas iônicas cardíacas.]),
   ("E", [A queda do pH intracelular ativa proteases dependentes de cálcio, que clivam diretamente as enzimas do ciclo de Krebs antes mesmo que a depleção energética se instale completamente nas células afetadas.])))

#questao-ce("30", badge-aplicacao,
  [Sobre a fisiopatologia metabólica da deficiência grave de tiamina em alcoolismo crônico, julgue os itens:],
  (("I", [O bloqueio simultâneo da piruvato desidrogenase e da α-cetoglutarato desidrogenase leva ao acúmulo de piruvato no citosol e à paralisação parcial do ciclo de Krebs nos tecidos afetados.]),
   ("II", [A reposição de glicose antes da reposição de tiamina pode precipitar encefalopatia de Wernicke aguda, porque o aporte de substrato eleva a demanda por TPP funcional e esgota o estoque residual disponível.]),
   ("III", [A síndrome de Korsakoff representa a evolução crônica e irreversível do quadro, caracterizada por amnésia anterógrada e confabulação compensatória diante de lacunas mnêmicas.]),
   ("IV", [A deficiência de tiamina aumenta a atividade da piruvato carboxilase, compensando a paralisação da PDH pela geração direta de oxaloacetato a partir do piruvato acumulado nos hepatócitos.])))
