# Mapa de Confusões — Metabolismo de Lipídeos (`bioq-21-lipideos-rotas`)

Artefato interno do QUESTIONADOR. Cada confusão = nome curto + descrição mecanística do erro + origem. Alimenta distratoras da E2 e boxes da E1. (Esqueleto auto-gerado curado por mão humana 2026-06-25.)

## Subtópico 1 — Mobilização e entrada na mitocôndria

- **Lipase trocada** — achar que a lipoproteína-lipase (capilar, hidrolisa TAG de quilomícrons/VLDL) é a mesma da lipólise intracelular (HSL/ATGL). A lipólise do estoque é hormônio-sensível (glucagon/adrenalina → AMPc → PKA). (origem: livro-texto)
- **Glicerol = combustível direto** — achar que o glicerol liberado vira ATP no adipócito. O adipócito quase não tem glicerol-quinase; o glicerol vai pelo sangue ao fígado, onde entra na gliconeogênese/glicólise como gliceraldeído-3-P. (origem: slide 7-8)
- **AG atravessa sozinho** — achar que o acil-CoA entra na matriz por difusão. A membrana interna é impermeável ao acil-CoA; só o grupo acil entra, carregado pela carnitina (CPT-1 fora, CPT-2 dentro). (origem: slide 13)
- **Carnitina opcional** — achar que AG de cadeia longa oxidam sem carnitina. Sem a lançadeira, o acil-CoA longo não chega à matriz; só AG de cadeia curta/média dispensam. (origem: slide 70, discursiva 3)

## Subtópico 2 — β-oxidação e contabilidade

- **Custo da ativação subestimado** — contar a ativação como 1 ATP. ATP→AMP+PPi e o PPi é hidrolisado a 2 Pi: gasto equivalente a 2 ligações de alta energia. 131 bruto − 2 = 129. (origem: slide 22)
- **Número de voltas = número de acetil-CoA** — achar que 16C dá 8 voltas. São n/2 − 1 = 7 voltas (a última parte de um butiril-CoA de 4C e gera 2 acetil-CoA de uma vez), produzindo 8 acetil-CoA, 7 NADH, 7 FADH₂. (origem: slide 18)
- **β-oxidação é anaeróbia** — achar que roda sem O₂ "porque não usa O₂". FADH₂ e NADH precisam ser reoxidados na cadeia respiratória; sem aceptor final, FAD/NAD⁺ não se regeneram e o ciclo para. (origem: slide 72, discursiva 4)
- **FADH₂ rende igual a NADH** — esquecer que entram na cadeia em pontos diferentes (FADH₂ no complexo II, NADH no I); no padrão do professor, NADH=3 ATP e FADH₂=2 ATP. (origem: slide 20)

## Subtópico 3 — Corpos cetônicos

- **Cetose = só dieta sem carboidrato** — ignorar que a causa imediata é o excesso de acetil-CoA da β-oxidação somado à falta de oxaloacetato (desviado para a gliconeogênese no jejum/diabetes). (origem: q-0264, slide 31)
- **Corpo cetônico é "lixo"** — achar que não serve de combustível. Acetoacetato e β-hidroxibutirato são combustível de exportação do fígado para cérebro, coração e músculo no jejum. (origem: slide 33-34)
- **Cetoacidose = cetose** — confundir o acúmulo fisiológico (cetose de jejum) com a cetoacidose descompensada do diabetes tipo 1, em que a queda do pH é o evento perigoso. (origem: slide 36)
- **Fígado consome o próprio corpo cetônico** — o fígado fabrica mas não usa (falta a tioforase/SCOT); só os tecidos periféricos reativam acetoacetato a acetil-CoA. (origem: livro-texto)

## Subtópico 4 — Síntese e regulação recíproca

- **Síntese é a β-oxidação ao contrário** — achar que são idênticas no sentido inverso. São espelhadas na lógica, mas: síntese no citosol, usa NADPH, carreador ACP, doador malonil-CoA; β-ox na matriz, usa FAD/NAD⁺, carreador CoA. (origem: q-0265, slide 58)
- **Acetil-CoA sai da mitocôndria sozinho** — a membrana é impermeável ao acetil-CoA; ele sai como citrato (lançadeira do citrato) e é reclivado no citosol pela citrato-liase. (origem: slide 43-44)
- **Malonil-CoA só serve de tijolo** — esquecer seu papel regulatório: malonil-CoA inibe a CPT-1, travando a β-oxidação enquanto a síntese está ligada (evita ciclo fútil). (origem: slide 13, 47)
- **AG par vira glicose** — achar que o acetil-CoA da β-ox alimenta a gliconeogênese. Em mamíferos não há síntese líquida de glicose a partir de acetil-CoA (PDH irreversível, sem glioxilato). Só glicerol e propionil-CoA (ímpar) contribuem. (origem: q-0156, banco bioq-16)
- **Enzima málica = só descarboxilação** — esquecer que enzima málica e glicose-6-P-desidrogenase compartilham o papel de gerar NADPH para a síntese. (origem: slide 64, discursiva 10)
