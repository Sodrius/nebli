#import "../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Explique, em até 100 palavras, por que a apoptose é considerada uma morte "limpa" do ponto de vista imunológico, articulando integridade de membrana, sinal de fosfatidilserina e resposta do macrófago fagocitário.],
  [Em apoptose, a membrana plasmática permanece íntegra durante todo o processo — não há extravasamento de conteúdo citosólico nem liberação de DAMPs. Paralelamente, caspases ativas inativam a flipase e ativam a scramblase, fazendo fosfatidilserina aparecer na face externa. Macrófagos com receptores específicos (TIM4, BAI1, estabilina) reconhecem essa fosfatidilserina como sinal "coma-me" e fagocitam silenciosamente os corpos apoptóticos. Essa fagocitose dispara produção de IL-10 e TGF-β (anti-inflamatórias) e suprime IL-12 — oposto da resposta a debris necrótico. Sem extravasamento e sem citocinas pró-inflamatórias, não há inflamação local.],
)

#discursiva("Q2",
  [Descreva mecanisticamente como o sinal da via extrínseca pode ser amplificado pela via intrínseca em células do tipo II (até 100 palavras), nomeando as proteínas envolvidas e a direção do cross-talk.],
  [O ligante (FasL/TNF) ativa o receptor de morte, que monta o DISC com FADD e pró-caspase-8. Caspase-8 ativa, em células tipo I (linfócitos), cliva diretamente caspase-3 em quantidade suficiente para apoptose completa. Em células tipo II (hepatócitos, células beta), a quantidade gerada não basta — caspase-8 cliva Bid em tBid (truncated Bid), uma BH3-only ativadora. tBid migra à mitocôndria e ativa BAX/BAK, disparando MOMP. Citocromo c escapa, o apoptossomo se forma com Apaf-1 e ativa caspase-9, que amplifica massivamente a clivagem de caspase-3. Direção é sempre extrínseca → intrínseca.],
)

#discursiva("Q3",
  [Explique por que uma célula em isquemia profunda tende a morrer por necrose e não por apoptose, mesmo recebendo sinais pró-apoptóticos do ambiente lesado (até 100 palavras). Articule o papel do ATP.],
  [A apoptose é um programa ativo que requer ATP: caspases dependem de hidrólise, scramblase precisa de cálcio mobilizado por bombas, _blebbing_ exige ATP citoesquelético, formação do apoptossomo requer dATP. Em isquemia profunda, a célula perde rapidamente ATP — a cadeia respiratória para, a fosforilação oxidativa cessa. Sem combustível, o programa apoptótico não consegue rodar até o fim. A célula então perde controle iônico (bombas Na⁺/K⁺-ATPase falham), incha, a membrana rompe e o conteúdo extravasa — morfologia de necrose. Em isquemia parcial, com ATP residual, ainda pode ocorrer apoptose; sem ATP, só sobra necrose.],
)

#discursiva("Q4",
  [Considerando que muitos vírus expressam inibidores de caspase-8 (como vICA do citomegalovírus), explique por que isso teria sido vantajoso evolutivamente para o vírus e como o sistema imune evoluiu para responder, articulando necroptose e RIPK3/MLKL (até 100 palavras).],
  [O vírus se beneficia mantendo a célula-hospedeira viva: célula apoptótica é fagocitada e silenciada antes de produzir novas partículas virais. Inibindo caspase-8, o vírus bloqueia a via extrínseca e prolonga sua replicação. A célula respondeu evolutivamente com uma rota alternativa: na ausência de caspase-8 ativa, RIPK1 e RIPK3 não são clivadas, associam-se no necrossomo, e RIPK3 fosforila MLKL. MLKL fosforilada oligomeriza, fura a membrana plasmática — necroptose. A célula morre fazendo barulho: libera DAMPs, alerta o sistema imune, recruta resposta inflamatória contra o vírus. O patógeno tranca uma porta, a outra abre.],
)

#discursiva("Q5",
  [O gene TP53 está mutado em cerca de 50% dos cânceres humanos. Explique mecanisticamente por que a perda funcional de p53 favorece progressão tumoral, articulando ponto de verificação G1, parada do ciclo e via apoptótica intrínseca (até 130 palavras).],
  [Em células normais, p53 tem meia-vida curta — é degradada por MDM2 continuamente. Quando há dano de DNA, cinases ATM/ATR fosforilam p53, que escapa da degradação e se acumula. Acumulada, p53 atua como fator de transcrição em duas direções: ativa p21, que inibe Cdks e para o ciclo em G1 (dando tempo para reparo); e ativa Puma/Noxa (BH3-only) e Bax, disparando via intrínseca da apoptose se o dano for grande demais. A decisão "parar e reparar × matar" depende da extensão. Sem p53 funcional, células com DNA quebrado não param em G1 (continuam ciclando com lesões) nem disparam apoptose (não há transcrição de Puma/Noxa). O resultado é acúmulo progressivo de mutações em células que deveriam ter morrido, seleção de clones agressivos e progressão tumoral. É por isso que p53 é chamado "guardião do genoma".],
)
