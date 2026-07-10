"""
Gerador de q-NNNN.md para os primeiros 80 itens do EXCEL_UNICOS.json.
IDs de saida: q-0280 a q-0359.
"""
import json, os, re, textwrap

BASE = r"C:\AI use\Cowork playground\NEBLI - criador de resumos"
JSON_FILE = os.path.join(BASE, "banco", "meta", "EXCEL_UNICOS.json")
OUT_DIR   = os.path.join(BASE, "banco", "questoes")
START_ID  = 280

NIVEL = {"Dificil": "dificil", "Intermediario": "medio", "Facil": "facil"}

# Metadados por id_excel: tags, conceito_central, armadilha
META = {
  1: {"tags":["gliconeogenese","metabolismo-etanol","regulacao-alosterica","acidose-metabolica","krebs","buffers"],
      "conceito":"consequencias metabolicas da intoxicacao alcoolica: inibicao indireta da gliconeogenese por falta de substrato (NADH alto desvia piruvato→lactato e OAA→malato) e cetoacidose",
      "armadilha":"confundir inibicao direta das enzimas gliconeogenicas com inibicao indireta por falta de substrato — o etanol nao inibe PEPCK/FBPase, mas consome NAD+ desviando seus substratos"},
  2: {"tags":["cetogenese","krebs","fosforilacao-oxidativa","beta-oxidacao","energia-livre"],
      "conceito":"calculo do saldo de ATP na oxidacao do beta-hidroxibutirato em condicoes aerobia, anaerobia e com desacoplador (DNP)",
      "armadilha":"corpos cetonicos NAO sao oxidaveis sem O2 (Krebs para por acumulo de NADH); DNP elimina apenas o ATP oxidativo, nao o substrato-nivel"},
  3: {"tags":["cadeia-respiratoria","fosforilacao-oxidativa","glicolise","regulacao-metabolica","efeito-pasteur"],
      "conceito":"efeito da oligomicina sobre leveduras (Crabtree-positivas) em glicose vs glicerol: glicolise compensa parcialmente, mas glicerol exige cadeia respiratoria funcional",
      "armadilha":"S. cerevisiae e Crabtree-positiva: pode crescer em glicose sem mitocondria, mas NAO em glicerol (entra pela cadeia via FADH2)"},
  4: {"tags":["glicolise","regulacao-alosterica","enzimologia","regulacao-metabolica","f26bp"],
      "conceito":"caracteristicas bioquimicas, termodinamicas e cineticas da PFK-1 e seu controle alosterico por ATP (inibicao) e F2,6BP (ativacao) incluindo efeito do pH",
      "armadilha":"curva V×[ATP] tem forma de sino (ATP e substrato E inibidor alosterico em alta concentracao); F2,6BP ATENUA a inibicao por ATP, nao simplesmente aumenta Vmax"},
  5: {"tags":["cadeia-respiratoria","fosforilacao-oxidativa","inibidores-enzimaticos","metabolismo-integrado"],
      "conceito":"experimento para distinguir antimicina (bloqueia Complexo III) de oligomicina (bloqueia ATP-sintase) usando oximetria + DNP como revelador",
      "armadilha":"oligomicina e revertida por DNP (gradiente preso se dissocia), antimicina NAO (problema e upstream na transferencia de eletrons)"},
  6: {"tags":["glicolise","eritrocito","transporte-ativo-primario","bomba-na-k","doencas-metabolicas"],
      "conceito":"seletividade eritrociaria de droga que degrada PEP: eritrocito depende 100% da glicolise (sem mitocondria), perda da piruvato-quinase = colapso energetico → hemolise",
      "armadilha":"outros tecidos tem fosforilacao oxidativa e substrato alternativo — a seletividade e pela ausencia de mitocondria no eritrocito maduro"},
  8: {"tags":["gliconeogenese","regulacao-alosterica","modificacao-covalente","krebs","enzimologia"],
      "conceito":"piruvato carboxilase ativada por acetil-CoA como sinal de excesso de combustivel; modificacao covalente (fosforilacao) como segundo mecanismo regulatorio",
      "armadilha":"acetil-CoA ativa piruvato carboxilase porque sinaliza excesso de acetil sem OAA suficiente — nao por falta de energia"},
  9: {"tags":["metabolismo-integrado","gliconeogenese","lipogenese","beta-oxidacao","energia-livre"],
      "conceito":"regras de interconversao de macronutrientes: glicose→AG (sim); AG→glicose (nao em mamiferos, regra fundamental); proteina→glicose (sim, AA glicogenicos)",
      "armadilha":"acidos graxos de cadeia par NAO geram glicose em mamiferos (falta ciclo do glioxilato); so o glicerol e AG impares (propionil-CoA→succinil-CoA) contribuem minimamente"},
  10: {"tags":["krebs","fosforilacao-oxidativa","enzimologia","cofatores-enzimaticos","energia-livre"],
       "conceito":"identificacao dos intermediarios alfa-KG→OAA, classes de enzimas, reagentes/produtos e saldo de ATP por volta de Krebs com e sem DNP",
       "armadilha":"alfa-KG-DH e complexo multienzimatico (como PDH), nao enzima unica; GTP do Krebs e substrato-nivel, NAO afetado pelo DNP"},
  11: {"tags":["cadeia-respiratoria","fosforilacao-oxidativa","inibidores-enzimaticos","glicolise","energia-livre"],
       "conceito":"amital bloqueia Complexo I → NADH nao oxidado; FADH2 (entra em Q diretamente via Complexo II) continua; saldo de ATP despenca; DNP nao reverte",
       "armadilha":"FADH2 nao e afetado pelo amital (entra em Q pelo Complexo II, downstream do bloqueio) — DNP funciona para oligomicina, NAO para inibidores da cadeia"},
  12: {"tags":["metabolismo-glicogenio","regulacao-alosterica","modificacao-covalente","regulacao-metabolica","glicolise"],
       "conceito":"estrutura do glicogenio (alfa1→4 e alfa1→6) e vantagens; condicoes fisiologicas de mobilizacao hepatica vs muscular; por que musculo nao exporta glicose (sem G6Pase)",
       "armadilha":"musculo nao exporta glicose porque nao tem glicose-6-fosfatase — G6P fica aprisionada; glucagon age so no figado (receptor ausente no musculo)"},
  13: {"tags":["via-pentoses","glicolise","nadph","energia-livre","regulacao-metabolica"],
       "conceito":"quando a celula precisa so de ribose-5-P, usa ramo NAO-oxidativo (F6P+G3P → 3 ribose-5-P), sem consumo ou sintese de ATP e sem gerar NADPH desnecessario",
       "armadilha":"o ramo oxidativo gera NADPH (desperdicado se nao necessario); a via nao-oxidativa e reversivel e nao produz NADPH; custo e apenas 1 ATP da hexoquinase"},
  14: {"tags":["glicolise","fosforilacao-oxidativa","efeito-pasteur","regulacao-metabolica","eritrocito"],
       "conceito":"efeito Pasteur no musculo cardiaco: em anaerobiose consumo de glicose dispara (glicolise compensa); em aerobiose, 30 ATP/glicose reduz 15x o consumo",
       "armadilha":"LDH cardiaca normalmente converte LACTATO→piruvato em aerobiose, NAO produz lactato — so em anaerobiose o sentido se inverte para reoxidar NADH citosólico"},
  15: {"tags":["cromatina","eucromatina-heterocromatina","nucleossomo","transcricao","ciclo-celular"],
       "conceito":"identificacao de heterocromatina (periferica densa), nucleolo (fabrica de rRNA) e eucromatina (descondensada, ativa) em micrografia eletronica",
       "armadilha":"nucleolo esta DENTRO do nucleo e sintetiza rRNA (nao processa mRNA) — confundir com eucromatina ou com o envelope nuclear"},
  16: {"tags":["ciclo-celular","mitose","cromatina"],
       "conceito":"numero de cromatides em G1 (46 cromossomos × 1 = 46) vs metafase (46 cromossomos × 2 = 92 cromatides) antes da disjuncao",
       "armadilha":"confundir numero de cromossomos com numero de cromatides — em metafase os 46 cromossomos ja se duplicaram mas ainda nao se separaram → 92 cromatides"},
  17: {"tags":["ciclo-celular","citometria-fluxo","marcadores-proliferacao"],
       "conceito":"interpretacao de histograma de citometria de fluxo com iodeto de propidio: pico G1 (2N), vale S (conteudo intermediario), pico G2/M (4N)",
       "armadilha":"o pico da direita e G2/M (nao so M) — ambas as fases tem conteudo 4N de DNA e nao sao separaveis por este metodo sem outro marcador especifico de mitose"},
  18: {"tags":["apoptose","ciclo-celular","quimioterapia","citometria-fluxo","p53"],
       "conceito":"doxorrubicina intercala DNA + inibe topoisomerase II → quebras de dupla fita → apoptose via p53 → pico sub-G1 em citometria por fragmentacao internucleossomal",
       "armadilha":"pico sub-G1 representa celulas APOPTOTICAS (DNA fragmentado), nao G0 — esta a ESQUERDA do pico G1 com conteudo de DNA menor que 2N"},
  19: {"tags":["ciclo-celular","ciclinas-cdk","oncoproteinas","regulacao-genica"],
       "conceito":"mapa dos complexos ciclina-CDK por fase: CDK4/6+ciclinaD em G1, CDK2+ciclinaE em G1/S, CDK2+ciclinaA em S, CDK1+ciclinaB em M — todas afirmativas corretas",
       "armadilha":"CDK1 = Cdc2 = MPF (denominacoes antigas e modernas coexistem); nao confundir CDK2-ciclinaA (fase S) com CDK2-ciclinaE (transicao G1/S)"},
  20: {"tags":["ciclo-celular","marcadores-proliferacao","quimioterapia","oncoproteinas"],
       "conceito":"Ki67 marca celulas em qualquer fase ativa do ciclo (G1,S,G2,M), ausente em G0 — aumento APOS tratamento indica falha terapeutica, nao resposta",
       "armadilha":"aumento de Ki67 APOS tratamento indica RESISTENCIA — erro clinico e interpretar Ki67 alto como 'tumor respondendo e morrendo'"},
  21: {"tags":["ciclo-celular","oncoproteinas","p53","quimioterapia","ciclinas-cdk"],
       "conceito":"com p53 wild-type, resistencia ao tratamento pode ocorrer por: perda de p14ARF (libera MDM2 para degradar p53) OU amplificacao de MDM2 (degrada p53 diretamente)",
       "armadilha":"p53 wild-type NAO garante funcao de p53 — MDM2 amplificado degrada p53 mesmo sem mutacao; perda de p14ARF tem o mesmo efeito (libera MDM2)"},
  22: {"tags":["apoptose","oncoproteinas","quimioterapia","p53"],
       "conceito":"venetoclax (inibidor de BCL-2) ativa via intrinseca de apoptose independente de p53 — util em leucemias com delecao 17p/mutacao TP53, resistentes a quimioterapia convencional",
       "armadilha":"via BCL-2/BAX e UPSTREAM de p53 — contorna a resistencia classica de tumores p53-mutados; BCL-2 sequestra BAX/BAK impedindo MOMP"},
  23: {"tags":["ciclo-celular","oncoproteinas","p53","ciclinas-cdk","cromatina"],
       "conceito":"HPV16/18: E7 degrada pRb (cai), libera E2F (sobe), causa superexpressao de p16 por perda do feedback repressivo (sobe — paradoxo); E6 degrada p53 (p21 cai)",
       "armadilha":"p16 SOBE nos tumores HPV+ (paradoxo) porque pRb degradado nao reprime mais a transcricao de p16 — p16 alto e biomarcador de tumor HPV-relacionado"},
  24: {"tags":["nucleossomo","cromatina","histonas","estrutura-proteina"],
       "conceito":"nucleossomo: octamero de histonas (H2A, H2B, H3, H4 × 2) com ~147 pb de DNA em 1,65 voltas; histonas tem carga POSITIVA (Lys/Arg) que neutraliza fosfatos do DNA",
       "armadilha":"histonas tem carga POSITIVA (nao negativa); o octamero tem 8 subunidades (nao 7); H1 se liga ao DNA linker (nao ao octamero central)"},
  25: {"tags":["p53","oncoproteinas","ciclo-celular","quimioterapia","regulacao-genica"],
       "conceito":"com p53 wild-type, resistencia ao tratamento pode ocorrer por perda de p14ARF (II) e amplificacao de MDM2 (III) — ambos neutralizam p53 funcionalmente sem mutacao",
       "armadilha":"perda de p14ARF e amplificacao de MDM2 tem o mesmo efeito final (menos p53 funcional) por mecanismos opostos — nao confundir perda com amplificacao"},
  26: {"tags":["transcricao","rna-polimerase","regulacao-genica","processamento-mrna","fatores-transcricao"],
       "conceito":"RNA pol NAO precisa de primer (inicia de novo) e tem menor fidelidade que DNA pol; fator sigma reconhece promotores bacterianos; ativacao pos-traducional de TFs por fosforilacao/ligante/relocalizacao",
       "armadilha":"RNA pol NAO tem proofreading 3'→5' (mRNA e transiente, erros toleraveis); acoplamento quimiosmótico de Mitchell e fator sigma e especifico de procariontes"},
  27: {"tags":["regulacao-genica","operon-lac","transcricao","metabolismo-integrado"],
       "conceito":"regulacao dupla do operon lac: repressao negativa por LacI (removida pela alolactose) E ativacao positiva por CAP-cAMP (presente so sem glicose) — explica o crescimento diauxico",
       "armadilha":"com GLICOSE+LACTOSE: LacI e removido (OK), mas cAMP esta BAIXO → CAP nao recruta RNA-pol → transcricao e basal; bacteria consome glicose primeiro"},
  28: {"tags":["processamento-mrna","splicing","cap5","poliadenilacao","transcricao","regulacao-genica"],
       "conceito":"diferencas gene→pre-mRNA→mRNA maduro: cap 5', remocao de introns por spliceossomo, poliadenilacao 3'; contraste com procariontes (sem splicing, sem cap, sem compartimento)",
       "armadilha":"splicing alternativo gera multiplas isoformas do mesmo gene — relacao gene:proteina nao e 1:1 em eucariotos; spliceossomo e snRNP+proteinas, nao ribossomo"},
  29: {"tags":["traducao","aminoacil-trna","ribossomo","enzimologia","regulacao-genica"],
       "conceito":"fidelidade da traducao depende exclusivamente da aminoacil-tRNA sintetase (nao do ribossomo) — ribossomo verifica so pareamento codon-anticodon, nao o aminoacido ligado",
       "armadilha":"ribossomo NAO 'le' qual aminoacido esta no tRNA — toda a fidelidade reside na aaRS e seu sitio de proofreading que hidrolisa aminoacidos incorretos"},
  30: {"tags":["dna-recombinante","splicing","transcricao","traducao","metabolismo-integrado"],
       "conceito":"producao de hGH em E. coli requer cDNA (sem introns); IPTG como indutor do promotor lac; HBsAg NAO pode ser feito em bacteria (glicoproteina, requer levedura)",
       "armadilha":"HBsAg NAO pode ser feito em E. coli porque precisa de glicosilacao no Golgi/RE e montagem em particulas subvirais; hGH SIM pode (nao e glicosilada)"},
  31: {"tags":["regulacao-genica","transcricao","cromatina","epigenetica","splicing","traducao"],
       "conceito":"eucariotos regulam expressao em multiplos niveis (cromatina, transcricao, processamento, exportacao, estabilidade mRNA, traducao, pos-traducao); procariontes concentram na transcricao (operons, sigma, riboswitches)",
       "armadilha":"procariontes tambem tem regulacao pos-transcricional (riboswitches, atenuacao), mas a PRINCIPAL diferenca e que eucariotos tem multiplas camadas adicionais"},
  32: {"tags":["gliconeogenese","enzimologia","regulacao-metabolica","regulacao-alosterica","energia-livre"],
       "conceito":"sequencia completa da gliconeogenese (piruvato→glicose): 4 etapas de bypass (piruvato carboxilase, PEPCK, FBPase-1, G6Pase) e 6 etapas reversiveis da glicolise — custo de 6 ATP + 2 NADH",
       "armadilha":"F2,6BP e o regulador mais potente do switch: alto em estado pos-prandial (ativa PFK-1, inibe FBPase-1), baixo em jejum (via glucagon→AMPc→PKA→PFK-2 inativa)"},
  33: {"tags":["fosforilacao-oxidativa","desacoplador","glicolise","energia-livre","krebs"],
       "conceito":"DNP elimina todo ATP oxidativo — saldo com DNP = so ATP de substrato-nivel (2 ATP da glicolise + 2 GTP do Krebs = 4 ATP por glicose)",
       "armadilha":"com DNP o Krebs CONTINUA girando (NAD+ e regenerado pela cadeia), mas ATP nao e formado — saldo real e 4, nao 0 nem 38"},
  34: {"tags":["cadeia-respiratoria","fosforilacao-oxidativa","krebs","acetil-coa","regulacao-metabolica"],
       "conceito":"analise V/F: desacoplador AUMENTA consumo de O2 mas DIMINUI ATP; acetil-CoA nao atravessa membrana interna; acoplamento e quimiosmotico (protons, nao eletrons para ATP-sintase)",
       "armadilha":"desacoplador AUMENTA consumo de O2 (cadeia roda mais) mas DIMINUI producao de ATP — alunos confundem 'acoplamento' com transferencia direta de eletrons"},
  35: {"tags":["gliconeogenese","energia-livre","metabolismo-integrado"],
       "conceito":"gliconeogenese a partir de glicerol: 1 ATP por glicerol (glicerol-quinase); 2 glicerois = 1 glicose → custo de 2 ATP por glicose (muito menor que a partir de piruvato: 6 ATP)",
       "armadilha":"interpretar '4 glicerois → quantos ATP?' como custo total (4 ATP) vs por glicose (2 ATP) — a questao pergunta ATPs por glicose"},
  36: {"tags":["gliconeogenese","metabolismo-integrado","beta-oxidacao","energia-livre"],
       "conceito":"substratos gliconeogenicos validos: oxaloacetato, piruvato, glicerol SIM; acetil-CoA e acidos graxos de cadeia par NAO (regra fundamental em mamiferos)",
       "armadilha":"acetato → acetil-CoA → Krebs gera CO2 (2 carbonos sao perdidos nas etapas ICDH e alfa-KG-DH) — nenhum carbono do acetil-CoA chega ao OAA em saldo liquido"},
  37: {"tags":["cadeia-respiratoria","fosforilacao-oxidativa","inibidores-enzimaticos","desacoplador"],
       "conceito":"inibidor que para consumo de O2 e e revertido por DNP = oligomicina (inibe ATP-sintase): gradiente fica preso, cadeia para, DNP cria via alternativa de dissipacao",
       "armadilha":"rotenona/malonato (bloqueiam upstream) NAO sao revertidos por DNP — DNP so reverte quando o problema e acumulo de gradiente (oligomicina), nao bloqueio da cadeia"},
  38: {"tags":["gliconeogenese","energia-livre","ciclo-cori","cofatores-enzimaticos"],
       "conceito":"na gliconeogenese a partir de lactato, o NADH gerado pela LDH (lactato→piruvato) compensa exatamente o NADH consumido pela GAPDH reversa — saldo de NADH = 0",
       "armadilha":"o ciclo de Cori e 'neutro' em NADH — o proprio lactato 'traz' o NADH necessario; figado nao precisa de NADH adicional, ao contrario da gliconeogenese a partir de aminoacidos"},
  39: {"tags":["processamento-mrna","splicing","cap5","poliadenilacao","rna-polimerase"],
       "conceito":"etapas de processamento do pre-mRNA eucariotico: capeamento 5' (co-transcricional), splicing (spliceossomo U1-U6), poliadenilacao 3' (CPSF+CstF+PAP), exportacao via NPC",
       "armadilha":"capeamento e CO-TRANSCRICIONAL (ocorre nos primeiros ~30 nt); poliadenilacao envolve CLIVAGEM antes da adicao de poli-A; splicing pode ser co- ou pos-transcricional"},
  40: {"tags":["regulacao-genica","operon-lac","operon-trp","transcricao","metabolismo-integrado"],
       "conceito":"lac e catabolico-induzivel (substrato desativa repressor LacI + ativacao positiva por CAP-cAMP); trp e anabolico-repressivel (produto ativa repressor TrpR como corepressor + atenuacao)",
       "armadilha":"logica oposta: no lac o substrato DESATIVA o repressor; no trp o produto ATIVA o repressor como corepressor; o trp tem segundo nivel (atenuacao por ribossomo) que o lac nao tem"},
  41: {"tags":["gliconeogenese","energia-livre","enzimologia"],
       "conceito":"custo de 6 ATP equivalentes para sintetizar 1 glicose a partir de 2 piruvatos: 2 ATP (piruvato carboxilase) + 2 GTP (PEPCK) + 2 ATP (fosfoglicerato quinase reversa)",
       "armadilha":"confundir saldo com custo — a gliconeogenese 'gasta' 6 ATP; os 2 NADH consumidos pela GAPDH reversa nao sao contados como ATP mas sao um custo adicional"},
  42: {"tags":["krebs","cofatores-enzimaticos","enzimologia","metabolismo-integrado"],
       "conceito":"no Krebs, os carbonos do acetil-CoA sao OXIDADOS → NAD+/FAD sao REDUZIDOS — 4 reacoes de oxidorredução por volta gerando 3 NADH + 1 FADH2",
       "armadilha":"o Krebs e via OXIDATIVA — acetil-CoA perde eletrons (oxidado), NAD+/FAD ganham eletrons (reduzidos); confundir quem oxida e quem reduz e erro classico"},
  43: {"tags":["glicolise","fosforilacao-oxidativa","eritrocito","energia-livre","metabolismo-integrado"],
       "conceito":"hemacia gera 2 ATP/glicose; hepatocito com lancadeira malato-aspartato gera 38 ATP/glicose → razao 19:1 → hemacia precisa metabolizar 19 moles de glicose para cada mol no hepatocito",
       "armadilha":"lancadeira de glicerol-fosfato renderia 36 ATP (nao 38); a questao especifica malato-aspartato (38 ATP) — nao confundir as duas lancadeiras"},
  44: {"tags":["glicolise","gliconeogenese","regulacao-alosterica","f26bp","regulacao-metabolica"],
       "conceito":"F2,6BP regula reciprocamente PFK-1 (ativa) e FBPase-1 (inibe) — produzido pela enzima bifuncional PFK-2/FBPase-2, controlada por glucagon (PKA→inativa PFK-2) e insulina",
       "armadilha":"a enzima bifuncional PFK-2/FBPase-2 NAO e PFK-1 ou FBPase-1 — e um regulador que sintetiza/degrada F2,6BP; PKA INATIVA o dominio PFK-2 (reduz F2,6BP)"},
  45: {"tags":["cadeia-respiratoria","fosforilacao-oxidativa","inibidores-enzimaticos","desacoplador","metabolismo-integrado"],
       "conceito":"identificacao de rotenona vs DNP por oximetria: rotenona bloqueia Complexo I (revertida por succinato); DNP dissipa gradiente (potencial cai a zero, cadeia continua, O2 cai ate zero)",
       "armadilha":"succinato REVERTE o bloqueio por rotenona (Complexo II contorna Complexo I) mas NAO reverte DNP; criterio de reversao por succinato distingue inibicao de Complexo I de desacoplamento"},
  46: {"tags":["gliconeogenese","metabolismo-glicogenio","doencas-metabolicas","enzimologia"],
       "conceito":"G6Pase existe SÓ em figado e rim cortex → sua ausencia afeta APENAS essas celulas (doenca de Von Gierke); musculo e cerebro nao a expressam e nao 'perdem' nada diretamente",
       "armadilha":"deficiencia de G6Pase afeta o figado (problema primario); cerebro sofre INDIRETAMENTE pela hipoglicemia resultante — o defeito bioquimico primario e hepatico"},
  47: {"tags":["fosforilacao-oxidativa","inibidores-enzimaticos","glicolise","energia-livre","cadeia-respiratoria"],
       "conceito":"oligomicina inibe ATP-sintase → gradiente acumula → cadeia para por contra-pressao → Krebs/PDH param → so glicolise anaeróbia funciona → 2 ATP por glicose",
       "armadilha":"com oligomicina a cadeia respiratoria TAMBEM para (gradiente acumula) — Krebs e PDH param junto; saldo final e 2 ATP da glicolise, nao 6 ou mais"},
  62: {"tags":["conducao-eletrotonica","constante-espaco","capacitancia-membrana","resistencia-membrana","axonio"],
       "conceito":"propagacao eletrotonica: constante de espaco lambda = sqrt(rm/ri); MAIOR rm e MENOR ri = maior alcance; capacitancia ALTA atenua e atrasa o sinal",
       "armadilha":"relacao e inversa para ri: MENOR ri = melhor conducao; MAIOR rm = melhor conducao; capacitancia ATENUA (nao amplifica)"},
  64: {"tags":["calcio-intracelular","receptores-ionotropicos","neurotransmissor","sinapse-quimica","canais-ca-voltagem"],
       "conceito":"excitotoxicidade por glutamato = ativacao excessiva de receptores NMDA (alta permeabilidade a Ca2+) → influxo massivo de Ca2+ → calpaina, NOS, PLA2 → morte celular",
       "armadilha":"receptores AMPA/KA despolarizam mas tem baixa permeabilidade a Ca2+; a toxicidade e mediada pelo NMDA-R cujo bloqueio por Mg2+ e removido pela despolarizacao previa"},
  70: {"tags":["modulador-alosterico","enzimologia","estrutura-proteina"],
       "conceito":"alosteria (heterotropica): ligacao em sitio DIFERENTE do sitio funcional afeta propriedades de outro local na proteina — diferente de cooperatividade homotropica (mesmo sitio)",
       "armadilha":"alternativa A descreve cooperatividade homotropica (efeito no mesmo sitio) — alosteria generica envolve sitios DIFERENTES"},
  71: {"tags":["hemoglobina","afinidade-oxigenio","estrutura-proteina","metaloproteina"],
       "conceito":"Fe2+ do heme tem 6 coordenacoes: 4 pelos nitrogenios da porfirina, 1 pela histidina proximal (F8) e 1 por O2; histidina distal (E7) estabiliza O2 por ponte H mas nao se liga ao ferro",
       "armadilha":"histidina distal (E7) estabiliza O2 por ponte de hidrogenio mas NAO se liga ao ferro; confundir proximal (F8, liga Fe) com distal (E7, estabiliza O2) e erro classico"},
  72: {"tags":["regulacao-genica","fosfolipidios","estrutura-membrana","fatores-crescimento"],
       "conceito":"betametasona/dexametasona em gestantes < 34 semanas ativa transcricao de genes de surfactante (DPPC + SP-A/B/C/D) nos pneumocitos tipo II, reduzindo sindrome do desconforto respiratorio neonatal",
       "armadilha":"corticosteroides sao administrados a GESTANTE, atravessam a placenta e agem nos pneumocitos fetais; efeito e na PRODUCAO de surfactante, nao no surfactante ja formado"},
  73: {"tags":["estrutura-membrana","lipossolubilidade","fosfolipidios"],
       "conceito":"acidos graxos insaturados cis REDUZEM o ponto de fusao e AUMENTAM a fluidez da membrana (dobras cis impedem empacotamento compacto) — o enunciado afirma o contrario (e falso)",
       "armadilha":"dobra cis IMPEDE empacotamento → MENOR ponto de fusao, MAIOR fluidez — isomeros TRANS nao tem esse efeito (cadeia mais reta, similar aos saturados)"},
  74: {"tags":["citoesqueleto","dineina-axonemal","microtubulos","proteinas-membrana"],
       "conceito":"cilios/flagelos tem axonema (9+2 microtubulos) com dineinas axonemais que convertem deslizamento em flexao; diferente de microvilos (actina) que aumentam superficie absortiva",
       "armadilha":"confundir motor do flagelo (dineina axonemal, microtubulos) com motor de actina (miosina) — miosina e do anel contractil e da musculatura; dineina e de cilios/flagelos"},
  75: {"tags":["mitose","citoesqueleto","actino-miosina"],
       "conceito":"anel contractil da citocinese e de ACTINA + MIOSINA II (nao dineina) — posicao e determinada pelo fuso de microtubulos, mas a contracao em si e actomiosina",
       "armadilha":"dineina e motor de microtubulos (fuso mitotico), miosina II e motor de actina (anel contractil) — posicao sinalizada por microtubulos, mecanismo de contracao e actina+miosina"},
  77: {"tags":["canais-ionicos","potencial-eletroquimico","permeabilidade-ionica","gradientes-ionicos","potencial-equilibrio"],
       "conceito":"valinomicina aumenta permeabilidade ao K+ → K+ sai (Vm = -70 mV e menos negativo que E_K+ = -88 mV) → equilibrio quando Vm = E_K+; concentracoes NAO se igualam",
       "armadilha":"K+ sai porque Vm (-70 mV) e MENOS negativo que E_K+ (-88 mV) — forca eletrica nao compensa o gradiente quimico; concentracoes NAO se igualam (equilibrio eletroquimico ocorre antes)"},
  78: {"tags":["bomba-na-k","transporte-ativo-primario","calcio-intracelular","transporte-ativo-secundario","energia-livre"],
       "conceito":"queda de ATP afeta: Na/K-ATPase para → gradiente de Na+ dissipa → NCX reverte (Ca2+ entra) → SERCA para → [Ca2+]i dispara → proteases → edema celular → necrose",
       "armadilha":"difusao passiva (GLUTs, canais ionicos) NAO e afetada pela queda de ATP — apenas transportes ATIVOS param; edema ocorre porque Na+ entra osmoticamente arrastando agua"},
  79: {"tags":["canais-ionicos","seletividade-ionica","canais-k-voltagem","canais-na-voltagem","estrutura-proteina"],
       "conceito":"seletividade ionica e determinada pelo filtro de seletividade (P-loop, sequencia TVGYG em canais K+) — para mudar K+→Na+ seria necessario alterar geometria e quimica do filtro",
       "armadilha":"seletividade e geometrica e eletronica: K+ se encaixa perfeitamente nas carbonilas do filtro TVGYG; Na+ e menor e nao faz o mesmo contato — mudar o filtro ou a geometria muda a seletividade"},
  80: {"tags":["gpcr","mensageiro-celular","camp","receptores-ionotropicos","sinalizacao-celular","hormonio-peptidico"],
       "conceito":"analise V/F sobre sinalizacao celular: hormonios peptidicos nao se ligam SÓ a GPCRs (tambem RTKs, JAK-STAT); cAMP nao e o unico 2o mensageiro de GPCRs (Gq→IP3+DAG+Ca2+)",
       "armadilha":"hormonios peptidicos NAO sao exclusivos de GPCRs — insulina liga RTK, GH liga JAK-STAT, ANP liga guanilato-ciclase; e IP3, DAG e Ca2+ tambem sao 2os mensageiros de GPCRs (via Gq)"},
  81: {"tags":["enzimologia","energia-livre","termodinamica","regulacao-metabolica"],
       "conceito":"enzima diminui energia de ativacao (estabiliza estado de transicao) e aumenta a constante de velocidade — NAO altera DeltaG, posicao de equilibrio, reversibilidade, nem energia do substrato ou produto",
       "armadilha":"enzima NAO altera o equilibrio termodinamico (Keq e DeltaG) — altera apenas a CINETICA (velocidade com que o equilibrio e atingido); reversibilidade e propriedade termodinamica"},
  82: {"tags":["reticulo-endoplasmatico","traducao","proteinas-membrana","exocitose","endocitose"],
       "conceito":"proteina de membrana segue via secretoria: nucleo → processamento → SRP reconhece peptideo sinal → RER → RE → Golgi → membrana plasmatica; traducao ocorre no RER (nao em ribossomos livres)",
       "armadilha":"traducao de proteinas de membrana ocorre no RER (nao ribossomos livres, nao no nucleo); confundir RER (traducao) com Golgi (processamento de glicosilacao)"},
  83: {"tags":["estrutura-proteina","aminoacidos-propriedades","ph","buffers","enzimologia"],
       "conceito":"glutationa tem ligacao gama-glutamil (nao alfa-peptidica) entre Glu-Cys → resistente a aminopeptidases; pI = (pK alfa-COOH 2,35 + pK Asp-COOH 3,9)/2 = 3,1; carga em pH 5 = -1",
       "armadilha":"tioes das Cys BLOQUEADOS pela ponte S-S (nao ionizaveis no calculo do pI); o pI nao usa o carboxil gama (esta na ligacao peptidica) nem os tiois se em S-S"},
  84: {"tags":["estrutura-membrana","lipossolubilidade","fosfolipidios","aminoacidos-propriedades"],
       "conceito":"linoleico (18:2, cis-Delta9,12, omega-6) tem duplas dobras → maior fluidez vs palmitico (saturado, linear); dominios transmembranares usam AA apolares (Val/Ile/Leu/Phe/Ala)",
       "armadilha":"linoleico e omega-6 (NAO omega-9 = oleico); sistema omega conta a partir do CH3 terminal; Trp e Tyr ficam na INTERFACE membrana-agua, nao no centro hidrofobico"},
  85: {"tags":["estrutura-membrana","lipossomos","endocitose","reticulo-endoplasmatico"],
       "conceito":"DSPC (2 cadeias, formato cilindrico) forma lipossomos (nao micelas); lipidio cationico ionizavel ALC-0315 condensa mRNA em pH acido e permite escape endossomal por protonacao em pH ~ 5",
       "armadilha":"DSPC forma LIPOSSOMOS (bicamada, formato cilindrico) — nao micelas (formato conico); segredo do lipidio ionizavel: neutro em pH 7,4 (circulacao), cationico em pH 5 (endossomo)"},
  86: {"tags":["hemoglobina","afinidade-oxigenio","modulador-alosterico","efeito-bohr","estrutura-proteina"],
       "conceito":"HbF tem maior afinidade por O2 que HbA porque cadeia gama tem Ser143 (vs His143 beta) — His contribui ao bolso de BPG; sem BPG efetivo, HbF permanece no estado R (alta afinidade)",
       "armadilha":"BPG liga-se ao bolso entre as cadeias BETA — HbF (alfa2-gama2) tem Ser143 nas cadeias gama, nao His → bolso nao funcional → BPG nao estabiliza estado T → HbF sempre mais afim pelo O2"},
  87: {"tags":["estrutura-proteina","aminoacidos-propriedades","enzimologia","ph"],
       "conceito":"cromatografia de exclusao: sai primeiro quem e MAIOR (300 kDa); troca ionica com resina negativa em pH 6: sai primeiro quem e NEGATIVO nesse pH (pI < pH → nao retido pela resina negativa)",
       "armadilha":"em troca ionica com resina NEGATIVA, proteina com carga NEGATIVA (pI < pH tampao) NAO liga e sai primeiro; proteina positiva (pI > pH) retida; alunos frequentemente invertem a logica"},
  88: {"tags":["estrutura-proteina","aminoacidos-propriedades","ph","buffers"],
       "conceito":"heptapeptideo com ponte S-S: tiois das Cys bloqueados (nao ionizaveis); pI = (2,35 + 3,9)/2 = 3,1; carga em pH 5 = -1 (alfa-NH3+ = +1; alfa-COO- = -1; Asp-COO- = -1)",
       "armadilha":"ponte S-S bloqueia os tiois das Cys (nao ionizaveis no calculo do pI); incluir o pK do tiol mesmo com S-S formada e erro frequente"},
  89: {"tags":["buffers","ph","equacao-henderson-hasselbalch","enzimologia"],
       "conceito":"para pH 5-6, tampao adequado e acetato (pKa 4,5, zona efetiva 3,5-5,5); para pH 6-7 e fosfato (pKa2 7,21); eficiencia depende de pKa proximo ao pH desejado e concentracao total alta",
       "armadilha":"acetato e eficaz SÓ ate ~pH 5,5; usar acetato para pH 6-7 seria inadequado (>95% como Ac-, sem capacidade tamponante) — deve-se trocar para fosfato"},
  90: {"tags":["hemoglobina","afinidade-oxigenio","modulador-alosterico","estrutura-proteina","metaloproteina"],
       "conceito":"Hb (tetramero, curva sigmoide, libera O2 nos tecidos) vs Mb (monomero, curva hiperbolica, armazena O2 no musculo) — cooperatividade e alosteria exigem multiplas subunidades",
       "armadilha":"se a Hb fosse o armazenador muscular, nao soltaria O2 nos tecidos (alta afinidade demais); se a Mb fosse o transportador, nao responderia a BPG/H+ (sem cooperatividade)"},
  91: {"tags":["estrutura-membrana","lipossolubilidade","fosfolipidios","regulacao-metabolica"],
       "conceito":"homeoviscose bacteriana: em frio sintetiza mais AG insaturados cis (dobras cis impedem empacotamento → fluidez mantida); em calor mais saturados; demonstra que fluidez e o parametro regulado",
       "armadilha":"isomeros TRANS nao tem o efeito de reduzir ponto de fusao como os CIS — cadeia trans e mais reta, similar aos saturados; C18:1 oleico: pf 13 graus C vs C18:0 estearico: pf 70 graus C"},
  92: {"tags":["estrutura-proteina","aminoacidos-propriedades","hormonio-peptidico","gpcr"],
       "conceito":"atividade biologica de oxitocina/vasopressina depende da conformacao imposta pela ponte S-S (anel de 6 AA) e da identidade do residuo 8 (Leu vs Arg) que determina seletividade pelo receptor",
       "armadilha":"DTT quebra a ponte S-S → peptideo perde conformacao → perde atividade; residuo 8 e o discriminador receptor-especifico; estrutura (nao so sequencia) e essencial para funcao"},
  93: {"tags":["estrutura-proteina","enzimologia","proteinas-membrana"],
       "conceito":"SDS-PAGE sem DTT mantem pontes S-S (banda de 180 = 2×90 unidas); com DTT quebra S-S → viram banda de 90; 160 e 60 sao subunidades individuais sem S-S; total = 160+90+90+60 = 400 kDa",
       "armadilha":"SDS sem DTT mantem S-S → cadeias S-S aparecem como banda maior; com DTT tudo se separa; banda de 90 aparece DUPLICADA mas se sobrepoe como pico unico em gel"},
  94: {"tags":["diferenciacao-celular","celulas-tronco","epigenetica","ciclo-celular","cromatina"],
       "conceito":"V/F: multipotentes nao originam 3 folhetos (so pluripotentes); diferenciacao continua na vida adulta; maior diferenciacao = menor potencialidade; heranca epigenetica e SEM mudanca de sequencia",
       "armadilha":"heranca epigenetica e justamente a transmissao de padroes de expressao SEM mudanca no DNA (metilacao de CpG mantida por DNMT1) — o item (d) inverte isso"},
  95: {"tags":["hematopoiese","granulocitos","fatores-crescimento","regulacao-metabolica"],
       "conceito":"excesso de G-CSF ou infeccao bacteriana (via TNF-alfa/IL-1/IL-6→G-CSF) acelera producao granulocitica → libera neutrofilos imaturos (desvio a esquerda); mecanismo e o mesmo",
       "armadilha":"desvio a esquerda (bastonetes, metamielocitos no sangue) e normal em infeccoes — nao confundir com leucemia; sinal de alarme sao blastos (>20% = leucemia aguda)"},
  96: {"tags":["hematopoiese","leucocitos","eritrocito","metabolismo-integrado"],
       "conceito":"V/F sobre celulas do sangue: monocitos sao maiores leucocitos circulantes (nao macrofagos); reticulocitose indica medula ativa (nao sempre problema); neutrofilos circulantes sao MADUROS (nao imaturos)",
       "armadilha":"reticulocitose ALTA pode indicar medula saudavel respondendo (hemolise, hemorragia) OU demanda extrema; contexto clinico determina a interpretacao"},
  97: {"tags":["dna-recombinante","splicing","transcricao","traducao","enzimologia"],
       "conceito":"producao de insulina recombinante em E. coli: cDNA (sem introns), promotor lac + IPTG, selecao por ampicilina; insulina NAO e glicosilada → pode ser produzida em bacteria",
       "armadilha":"insulina recombinante precisa de refolding (pontes S-S entre cadeias A e B formadas in vitro); cDNA e essencial porque E. coli nao tem spliceossomo"},
  98: {"tags":["reparo-dna","mutacao","transcricao","dna-recombinante","regulacao-genica"],
       "conceito":"UvrABC (NER bacteriano): UvrA reconhece distorcao, UvrBC faz incisoes assimetricas (4-5 nt do 3' e 8 nt do 5'), UvrD remove o oligonucleotideo, Pol I preenche, ligase sela",
       "armadilha":"fotoliase (fotorreativacao) reverte dimeros de timina DIRETAMENTE usando luz azul — nao envolve incisao; e reparo, nao bypass; ausente em mamiferos placentarios"},
  99: {"tags":["anatomia-coracao","valvas-cardiacas"],
       "conceito":"faces e margens do coracao: pulmonar direita = atrio direito (margem direita); esternocostal = ventriculo direito (margem ANTERIOR); diafragmatica = ambos ventriculos (margem inferior); pulmonar esquerda = ventriculo esquerdo (margem ESQUERDA)",
       "armadilha":"face pulmonar esquerda corresponde a margem ESQUERDA (obtusa), nao inferior; face esternocostal corresponde a margem ANTERIOR (nao superior) — a base dos atrios ocupa a porcao superior"},
  100: {"tags":["anatomia-coracao","valvas-cardiacas","grandes-vasos"],
        "conceito":"na sistole ventricular abrem-se as valvas SEMILUNARES (pulmonar e aortica) para ejetar sangue no tronco pulmonar e aorta — as valvas AV fecham nessa fase",
        "armadilha":"na sistole ventricular, as valvas AV (mitral/tricuspide) estao FECHADAS (pressao intraventricular > atrial); as que se ABREM sao as semilunares — alunos frequentemente invertem"},
  101: {"tags":["anatomia-coracao","grandes-vasos","sistema-linfatico"],
        "conceito":"tronco braquiocefalico (so lado direito) origina carotida comum DIREITA e subclavia DIREITA (nao esquerdas); seio coronario drena no atrio direito; braquiocefalicas D+E formam VCS",
        "armadilha":"tronco braquiocefalico existe SÓ no lado direito e origina carotida e subclavia DIREITAS — no lado esquerdo essas arterias saem DIRETAMENTE do arco aortico"},
  102: {"tags":["sistema-linfatico","anatomia-coracao","grandes-vasos"],
        "conceito":"ducto linfotico direito drena quadrante superior direito; ducto toracico (da cisterna do quilo) drena tudo o mais; ambos drenam no angulo venoso subclavia-jugular do respectivo lado",
        "armadilha":"ducto toracico drena ~75% da linfa corporal (incluindo membros inferiores e orgaos abdominais); cisterna do quilo recebe tambem troncos lombares, nao so o intestinal"},
  103: {"tags":["neuroanatomia-divisoes","substancia-cinzenta-branca","regulacao-genica"],
        "conceito":"V/F divisoes do SN: SNA (simpatico+parassimpatico) e subdivisao FUNCIONAL do SNA (I-V); divisao SNC/SNP e ANATOMICA, nao funcional (II-F); SNS vs SNA e divisao FUNCIONAL (III-V); SNP nao inclui encefalo (IV-F)",
        "armadilha":"divisao SNC/SNP e ANATOMICA (onde estao os neuronios), nao funcional; a divisao FUNCIONAL e SNS (voluntario) vs SNA (involuntario)"},
  104: {"tags":["neuroanatomia-divisoes","substancia-cinzenta-branca","citoesqueleto"],
        "conceito":"substancia cinzenta contem corpos celulares (pericarions) + dendritos + terminacoes sinapticas + celulas gliais; ausencia de mielina da a coloracao acinzentada; substancia branca = axonios mielinizados",
        "armadilha":"substancia CINZENTA = corpos celulares + glia (sem mielina = cinza); substancia BRANCA = axonios mielinizados (mielina = branca); confundir as duas e erro classico"},
  105: {"tags":["anatomia-coracao","neuroanatomia-divisoes","substancia-cinzenta-branca"],
        "conceito":"V/F sobre subdivisoes da anatomia: (I-V) clinica = aplicacao pratica; (II-F) sistematica organiza por sistemas (nao regioes); (III-F) superficie estuda projecoes na pele (nao sistemas); (IV-V) seccional = cortes TC/RM",
        "armadilha":"anatomia SISTEMATICA organiza por sistemas funcionalmente relacionados (nao por regioes); anatomia REGIONAL/TOPOGRAFICA organiza por regioes; anatomia de SUPERFICIE estuda projecoes na pele"},
  106: {"tags":["anatomia-coracao","neuroanatomia-divisoes","substancia-cinzenta-branca"],
        "conceito":"V/F: (I-V) radiografica usa topografica+seccional; (II-F) clinica usa TODOS os tipos (nao so superficie); (III-V) sistematica organiza por sistemas; (IV-F) patologica diagnostica por macro/microscopia (nao superficie)",
        "armadilha":"anatomia clinica usa TODOS os subtipos (superficie, topografica, seccional, sistematica) — restringi-la a superficie e absurdo; anatomia patologica analisa tecidos, nao superficie"},
  107: {"tags":["planos-anatomicos","neuroanatomia-divisoes"],
        "conceito":"planos: (1) sagital mediano D/E; (2) eixo longitudinal cranio-caudal; (3) transverso superior/inferior; (4) coronal/frontal anterior/posterior; (5) eixo sagital AP; (6) eixo transversal laterolateral",
        "armadilha":"plano sagital MEDIANO divide D/E em metades iguais; plano CORONAL (frontal) divide anterior/posterior — os termos coronal e frontal sao sinonimos; eixo transversal corre de lado a lado"},
  109: {"tags":["planos-anatomicos","anatomia-coracao","neuroanatomia-divisoes"],
        "conceito":"cavidade abdominal e delimitada por musculatura em TODOS os lados (diafragma superior, musculos anterolaterais, quadrado lombar/psoas posterior) — nao apenas anteriormente",
        "armadilha":"a afirmacao 'delimitada por musculatura apenas anteriormente' e INCORRETA — o diafragma (superior), a parede posterolateral (quadrado lombar, psoas) e os musculos anterolaterais formam as paredes"},
  110: {"tags":["planos-anatomicos","anatomia-coracao","neuroanatomia-divisoes"],
        "conceito":"em corte axial do abdome superior: estruturas 3 (estomago, esquerda) e 4 (figado, direita) sao BILATERAIS (um de cada lado da linha mediana); 1 e 2 (rins) sao ipsilaterais entre si (ambos sao 'rins')",
        "armadilha":"'bilaterais' significa que as estruturas estao em LADOS OPOSTOS da linha mediana (um a direita, um a esquerda) — estomago e figado sao bilaterais; 'ipsilaterais' significa no MESMO lado"},
}

# Formato e conversao
def fmt_tipo(t):
    if t == "Discursiva": return "discursiva"
    if t == "CE": return "CE"
    return "MC"

def parse_ce_gabarito(s):
    """'I-V; II-F; III-V; IV-F' → [C, E, C, E]"""
    parts = [p.strip() for p in s.split(";")]
    result = []
    for p in parts:
        m = re.search(r"-([VF])$", p)
        if m:
            result.append("C" if m.group(1) == "V" else "E")
    return result

def yaml_tags(tags):
    return "[" + ", ".join(tags) + "]"

def render_alternativas(alts, tipo):
    if tipo == "discursiva":
        return ""
    lines = []
    for letra in ["A","B","C","D","E"]:
        val = alts.get(letra, "").strip()
        if val:
            lines.append(f"{letra}) {val}")
    return "\n".join(lines) if lines else ""

def render_gabarito_frontmatter(item, tipo):
    g = item.get("gabarito_claude", "").strip()
    if tipo == "discursiva":
        return "ver Explicacao"
    if tipo == "CE":
        parsed = parse_ce_gabarito(g)
        if parsed:
            return "[" + ", ".join(parsed) + "]"
        # fallback: just return raw
        return f'"{g}"'
    # MC: first char if it's a letter A-E
    if g and g[0] in "ABCDE":
        return g[0]
    return f'"{g[:50]}"'

def sanitize_yaml(s):
    """Escapa aspas duplas e remove quebras de linha para uso em YAML inline."""
    return s.replace('"', "'").replace("\n", " ").strip()

def make_file(idx, item):
    qid = START_ID + idx
    excel_id = item["id_excel"]
    m = META.get(excel_id, {})

    tags = m.get("tags", ["metabolismo-integrado"])
    conceito = sanitize_yaml(m.get("conceito", item.get("tema", "")))
    armadilha = sanitize_yaml(m.get("armadilha", ""))

    nivel_raw = item.get("dificuldade", "Intermediario")
    nivel = NIVEL.get(nivel_raw, "medio")

    tipo = item.get("tipo", "MC")
    formato = fmt_tipo(tipo)

    uc_origem = item.get("uc", "UC1")
    enunciado = item.get("enunciado", "").strip()
    alts = item.get("alternativas", {})
    gabarito_claude = item.get("gabarito_claude", "").strip()
    justificativa = item.get("justificativa", "").strip()
    explicacao = justificativa if justificativa else gabarito_claude

    gab_front = render_gabarito_frontmatter(item, formato)
    alts_block = render_alternativas(alts, formato)

    # Build file content
    lines = []
    lines.append("---")
    lines.append(f"id: {qid}")
    lines.append(f"tags: {yaml_tags(tags)}")
    lines.append(f"nivel: {nivel}")
    lines.append(f"formato: {formato}")
    lines.append(f'conceito_central: "{conceito}"')
    lines.append(f"gabarito: {gab_front}")
    if armadilha:
        lines.append(f'armadilha: "{armadilha}"')
    lines.append(f"uc_origem: {uc_origem}")
    lines.append("---")
    lines.append("")
    lines.append("## Enunciado")
    lines.append("")
    lines.append(enunciado)
    lines.append("")

    if alts_block and formato != "discursiva":
        lines.append("## Alternativas")
        lines.append("")
        lines.append(alts_block)
        lines.append("")

    lines.append("## Gabarito")
    lines.append("")
    if formato == "discursiva":
        lines.append("Ver Explicacao abaixo.")
    elif formato == "CE":
        parsed = parse_ce_gabarito(gabarito_claude)
        if parsed:
            itens = ["I","II","III","IV","V","VI"]
            for k, v in enumerate(parsed):
                if k < len(itens):
                    lines.append(f"{itens[k]}: {'Correto' if v == 'C' else 'Errado'}")
        else:
            lines.append(gabarito_claude[:100])
    else:
        g = gabarito_claude
        if g and g[0] in "ABCDE":
            lines.append(f"Alternativa {g[0]}")
        else:
            lines.append(g[:100])
    lines.append("")
    lines.append("## Explicacao")
    lines.append("")
    lines.append(explicacao)
    lines.append("")

    return "\n".join(lines)


with open(JSON_FILE, encoding="utf-8") as f:
    items = json.load(f)

items80 = items[:80]

created = 0
for idx, item in enumerate(items80):
    content = make_file(idx, item)
    fname = f"q-{START_ID + idx:04d}.md"
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    created += 1

print(f"Criados {created} arquivos (q-{START_ID:04d} a q-{START_ID + created - 1:04d}).")
