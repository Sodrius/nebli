#import "../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Descreva o saldo energético por *volta* do ciclo de Krebs, identificando cada passo (1 a 8) gerador de cofator reduzido ou de composto fosforilado de alta energia. Inclua a numeração e o tipo de transformação química em cada caso.],
  [Por volta do ciclo, os geradores são: *passo 3* (isocitrato desidrogenase) → 1º NADH + 1º CO₂; *passo 4* (α-cetoglutarato desidrogenase) → 2º NADH + 2º CO₂; *passo 5* (succinil-CoA sintetase) → 1 GTP por fosforilação em nível de substrato; *passo 6* (succinato desidrogenase, embutida na membrana) → 1 FADH₂; *passo 8* (malato desidrogenase) → 3º NADH. Saldo total: *3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂*. Os passos 1, 2 e 7 não produzem cofator (condensação, isomerização e hidratação, respectivamente).])

#discursiva("Q2",
  [Explique por que o *passo 6* do ciclo (succinato desidrogenase) usa FAD em vez de NAD⁺ como aceptor de elétrons, e qual a importância dessa escolha para a integração com a cadeia respiratória.],
  [A oxidação succinato → fumarato tem ΔE° próximo de zero, incompatível com NAD⁺ (que exige potencial mais negativo). FAD aceita elétrons em potencial menor, viabilizando a reação. Além disso, a SDH é a *única* enzima do ciclo embutida na membrana mitocondrial interna — é, simultaneamente, o Complexo II da cadeia respiratória. O FAD ligado covalentemente entrega os elétrons direto à ubiquinona, sem intermediário solúvel, integrando ciclo e cadeia em um só ponto.])

#discursiva("Q3",
  [Compare os *passos 0* (PDH) e *4* (α-cetoglutarato desidrogenase) do ciclo, indicando substrato, produto, coenzimas envolvidas e por que ambos são paralisados na deficiência de tiamina.],
  [Os dois são *complexos multienzimáticos* arquiteturalmente idênticos: 3 enzimas (E1/E2/E3) e 5 coenzimas (TPP, lipoato, FAD, NAD⁺, CoA). PDH (*passo 0*): piruvato → acetil-CoA + NADH + CO₂. α-KG-DH (*passo 4*): α-cetoglutarato → succinil-CoA + NADH + CO₂. Ambos usam *tiamina pirofosfato (TPP)* — derivada da vitamina B1 — no primeiro passo enzimático (E1). Sem tiamina, os dois param simultaneamente, gerando o quadro de *beriberi* e *encefalopatia de Wernicke*.])

#discursiva("Q4",
  [Defina *anfibolismo* e *anaplerose*, exemplificando com pelo menos três pontos de saída de intermediários do ciclo e a reação anaplerótica principal. Identifique os passos do ciclo relacionados.],
  [*Anfibolismo* = via que serve tanto ao catabolismo (oxidação) quanto ao anabolismo (biossíntese). *Anaplerose* = reações que repõem intermediários removidos. Saídas (cataplerose): citrato (após *passo 1*) → ácidos graxos no citosol; α-cetoglutarato (entre *passos 3 e 4*) → glutamato e aminoácidos; succinil-CoA (após *passo 4*) → heme; OAA (após *passo 8*) → aspartato e gliconeogênese. Reposição: *piruvato carboxilase* converte piruvato + HCO₃⁻ + ATP em OAA — ativada alostericamente pela própria acetil-CoA, fechando o circuito de feed-forward.])

#discursiva("Q5",
  [Em um experimento, mitocôndrias isoladas são tratadas com *oligomicina* (inibidor da ATP-sintase) na presença de glicose, O₂ e ADP. Descreva: (a) o efeito sobre a cadeia respiratória, (b) o efeito sobre o ciclo de Krebs (identificando os passos prejudicados), (c) qual a única fosforilação que sobrevive e por quê, e (d) o saldo final de ATP por glicose nessa condição.],
  [(a) Cadeia respiratória *para* por contra-pressão — sem fluxo pela ATP-sintase, o gradiente de prótons acumula e os Complexos I-IV deixam de bombear. (b) Sem cadeia rodando, NADH/FADH₂ não são re-oxidados; NAD⁺/FAD livres se esgotam e *todas* as desidrogenases param — *passos 3, 4, 6 e 8* travam, e o passo 0 (PDH) também. (c) Sobrevive a *fosforilação em nível de substrato* — o *passo 5* (succinil-CoA sintetase → GTP) e os 2 ATP diretos da glicólise — porque independem do gradiente de prótons. Mas, com Krebs travado, o passo 5 também acaba parando por falta de succinil-CoA. (d) Restam apenas os 2 ATP líquidos da *glicólise anaeróbia*, com piruvato sendo reduzido a lactato pela LDH para regenerar NAD⁺ citosólico — saldo final: *2 ATP por glicose*.])
