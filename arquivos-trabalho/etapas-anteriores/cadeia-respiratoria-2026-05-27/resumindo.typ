#import "../typst-template/nebli_v2_apostila.typ": *

#resumindo-page((
  ("Por que existe uma cadeia",
   [oxidar NADH direto em O₂ libera 220 kJ/mol, energia demais para qualquer enzima capturar de uma vez. A célula fraciona em ~10 degraus de ~20 kJ/mol, e em cada degrau bombeia prótons em vez de gerar calor.]),

  ("Potenciais de redução governam a ordem",
   [elétrons fluem espontaneamente do par com E°' mais negativo (NADH = −0,32 V) para o mais positivo (O₂/H₂O = +0,82 V). A ordem dos complexos na membrana é termodinâmica, não geográfica.]),

  ("Atores e anatomia",
   [4 complexos integrais (I, II, III, IV) + 2 transportadores móveis (CoQ lipossolúvel na bicamada, citocromo c periférico hidrossolúvel na face externa) cravados na membrana mitocondrial INTERNA, impermeável a prótons.]),

  ("Complexo I bombeia, II não",
   [Complexo I (NADH → CoQ via FMN e Fe-S) bombeia 4 H⁺ por par de elétrons. Complexo II (succinato → CoQ via FAD) bombeia ZERO — degrau termodinâmico raso demais. Daí FADH₂ render menos ATP.]),

  ("Ciclo Q no Complexo III",
   [duas CoQH₂ em sítios diferentes (Q#sub[o] e Q#sub[i]) permitem casar a estequiometria 2:1 entre CoQ (2 e⁻) e cit c (1 e⁻). Bombeamento líquido: 4 H⁺ por par — o dobro do que seria sem bifurcação.]),

  ("Complexo IV reduz O₂ a água",
   [4 elétrons + 4 H⁺ + O₂ → 2 H₂O no centro binuclear heme a#sub[3]–CuB. Bombeia 2 H⁺. Cianeto e CO ligam-se ao Fe³⁺ do heme a#sub[3] e param toda a cadeia — hipóxia histotóxica, sangue venoso vermelho-cereja.]),

  ("Quimiosmose e PMF",
   [teoria de Peter Mitchell: cadeia bombeia H⁺ para fora, gerando força próton-motriz (~200 mV em humanos, ~70% elétrica + ~30% química). Essa PMF é o "intermediário energético" — não há intermediário químico fosforilado.]),

  ("ATP sintase F₀F₁ e binding change",
   [F₀ (anel de 8 subunidades c em humanos) gira com fluxo de prótons; F₁ (3 sítios catalíticos β alternando O→L→T→O) sintetiza ATP. 3 ATPs por volta = 8 H⁺. A energia da PMF abre o sítio T, não forma a ligação química.]),

  ("P/O moderno e saldo da glicose",
   [NADH rende 2,5 ATP (não 3), FADH₂ rende 1,5 (não 2). Custo de 3,7 H⁺ por ATP citosólico (rotor + transportes). Glicose completa rende 32 ATP (malato-aspartato) ou 30 ATP (glicerol-3-P), não 38.]),

  ("Lançadeiras transferem NADH citosólico",
   [malato-aspartato (fígado/rim/coração) preserva NADH → 2,5 ATP. Glicerol-3-P (músculo/cérebro) converte para FADH₂, bypassa Complexo I → 1,5 ATP. Tecidos rápidos preferem a glicerol-3-P, tecidos eficientes preferem malato-aspartato.]),

  ("Inibidores vs desacopladores",
   [inibidores (rotenona/I, antimicina/III, cianeto-CO/IV, oligomicina/sintase) param a cadeia — sem O₂ consumido, sem ATP. Desacopladores (DNP tóxico, FCCP pesquisa, UCP1 fisiológica) deixam cadeia rodar mas dissipam gradiente como calor — O₂ consumido sobe, ATP cai, hipertermia.]),

  ("UCP1 e termogênese no neonato",
   [tecido adiposo marrom expressa UCP1 (termogenina), ativada por norepinefrina via β₃-adrenérgico. Cria canal regulado para H⁺ voltarem sem passar pela sintase — gera calor controlado. Vital para neonatos (que não tremem) e redescoberta em adultos como alvo anti-obesidade.]),
))
