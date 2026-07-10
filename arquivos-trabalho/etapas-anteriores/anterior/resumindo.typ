#import "../typst-template/nebli_v2_apostila.typ": *

#resumindo-page((
  ("Replicação semiconservativa",
   [Cada dupla-hélice-filha herda uma fita parental intacta + uma fita nova complementar. Evidência: experimento de Meselson–Stahl com N¹⁵/N¹⁴ em gradiente de CsCl mostrou uma banda intermediária após a 1ª divisão.]),

  ("oriC e abertura da forquilha",
   [A replicação começa no oriC, sequência rica em A=T (só 2 pontes de hidrogênio por par) que separa mais facilmente. Do oriC partem duas forquilhas em sentidos opostos (replicação bidirecional).]),

  ("A trinca que abre a forquilha",
   [Helicase: quebra pontes de hidrogênio entre as bases. SSB: estabiliza fitas únicas impedindo re-enrolamento. DNA girase: corta e religa o esqueleto à frente da forquilha para aliviar o superenrolamento gerado.]),

  ("Por que o primer é de RNA",
   [DNA-polimerases não iniciam do zero — precisam de 3'-OH livre. A primase (RNA-polimerase) consegue iniciar sem 3'-OH, sintetizando um primer de RNA de ~10 nt. Após a síntese, o primer é removido pela Pol I.]),

  ("DNA-Pol III: a máquina principal",
   [Sintetiza >99% do DNA novo. Velocidade: 1.000 nt/s. Alta processividade pelo grampo β₂ (anel que envolve o duplex e ancora a enzima). Não solta o molde até terminar todo o cromossomo.]),

  ("DNA-Pol I: revisão e reparo",
   [Três sítios ativos: polimerização (5'→3'), exonuclease 3'→5' (proofreading — remove nucleotídeo mal pareado) e exonuclease 5'→3' (remove primer de RNA e dímeros de timina). Baixa processividade; função principal: preencher gaps curtos.]),

  ("Fita líder × fita retardada",
   [Fita líder: sintetizada continuamente no mesmo sentido da forquilha (molde 3'→5'). Fita retardada: sintetizada em fragmentos de Okazaki (molde 5'→3' no sentido da forquilha). Cada fragmento exige um novo primer.]),

  ("Ciclo do fragmento de Okazaki",
   [1) Primase faz primer de RNA. 2) Pol III estende até encontrar o primer anterior. 3) Pol I remove esse primer e preenche com DNA. 4) Ligase sela o nick residual usando NAD⁺ (bactérias) ou ATP (eucariotos).]),

  ("Fidelidade da replicação",
   [Erro final: 1 em 10⁹–10¹⁰ nucleotídeos. Contribuições: seleção do nucleotídeo correto na polimerização (~10⁵×) e proofreading 3'→5' (~10²×). Sistemas de reparo pós-replicativo acrescentam outros 10²–10³× de fidelidade.]),

  ("Eucariotos: múltiplas origens",
   [3 bilhões de pb → centenas de origens ativas simultaneamente (1 por 3–300 kbp). Polimerases: Pol α/primase (inicia), Pol δ e ε (replicação; ancoradas pelo PCNA — equivalente eucarioto do β₂), Pol β (reparo).]),

  ("Telomerase e imortalidade celular",
   [Cromossomos lineares encurtam a cada divisão (limite de Hayflick). Telomerase — transcriptase reversa com RNA-molde interno (hTR) — estende os telômeros. Reativada em 85–90% dos tumores → imortalidade replicativa.]),

  ("Fluoroquinolonas na clínica",
   [Ciprofloxacino, levofloxacino e congêneres inibem a DNA girase bacteriana, aprisionando o complexo enzima–DNA no estado de fita cortada. Acúmulo de quebras de dupla-fita → morte bacteriana. Seletivos para bactérias: girase humana tem estrutura diferente.]),
))
