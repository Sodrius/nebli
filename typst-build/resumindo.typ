#import "../typst-template/nebli_v2_apostila.typ": *

#resumindo-page((
  ("O problema em uma conta",
   [Um epítopo tem 10 a 12 aminoácidos, e há cerca de 10¹³ superfícies possíveis desse tamanho. O corpo produz mais de 10¹² anticorpos com um genoma de 25 000 genes — logo, a diversidade é fabricada, não armazenada.]),

  ("A molécula e onde ela varia",
   [O anticorpo é um Y de duas pesadas e duas leves idênticas. A região variável, nas pontas, forma o sítio na interface entre os domínios variáveis das duas cadeias; a constante, na haste, define a classe e a função efetora, sem tocar na especificidade.]),

  ("Segmentos no DNA, splicing no RNA",
   [A região variável existe no genoma herdado como coleções de peças — V e J na leve, V, D e J na pesada. A célula B corta o DNA e deleta o que fica entre as peças escolhidas, reescrevendo o cromossomo; o splicing vem depois, no transcrito, e só remove o que sobrou até o C.]),

  ("A conta da combinatória",
   [Leve: 35 × 5 = 175 regiões κ, mais 120 λ, somando 295. Pesada: 40 × 23 × 6 = 5 520. Como qualquer leve emparelha com qualquer pesada, 295 × 5 520 ≈ 1,6 × 10⁶ — ainda um milhão de vezes menos que o repertório real.]),

  ("A regra 12/23 impede a junção errada",
   [Cada segmento é flanqueado por heptâmero, espaçador e nonâmero. Só recombina um espaçador de 12 com um de 23, porque equivalem a uma e a duas voltas da hélice e alinham os blocos conservados na mesma face do DNA.]),

  ("Cortar em grampo, costurar sem molde",
   [RAG1 e RAG2 reúnem os dois sinais num só complexo e cortam uma fita; a hidroxila liberada ataca a fita oposta e fecha a extremidade codificante num grampo. Ku, DNA-PKcs, Artemis e a ligase IV então abrem o grampo e colam as pontas.]),

  ("A imprecisão é a maior fonte de diversidade",
   [Aparo de bases, nucleotídeos P vindos da abertura assimétrica do grampo e nucleotídeos N inseridos sem molde pela TdT tornam cada junção única e criam a CDR3. O preço é que só um terço dos rearranjos mantém a fase de leitura.]),

  ("Duas junções, dois destinos",
   [A junta codificante, imprecisa, fica no cromossomo e vira a região variável daquela célula. A junta-sinal, precisa, sai num círculo de DNA sem origem de replicação e se dilui até desaparecer nas divisões seguintes.]),

  ("Exclusão alélica: o sucesso desliga a máquina",
   [O rearranjo produtivo gera uma cadeia expressa na membrana que sinaliza o desligamento das recombinases, deixando o segundo alelo intacto. A ordem é fixa — pesada primeiro, leve depois — e garante uma única especificidade por célula.]),

  ("AID: mesma enzima, dois destinos opostos",
   [Na região variável, a AID desamina citosina e o reparo converte isso em mutação pontual: é a hipermutação, que muda a afinidade. Nas regiões switch, ela dispara quebras que deletam constantes inteiras: é a mudança de classe, que muda a função e não gera diversidade.]),
))
