#import "../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Explique por que uma inserção de uma única base no meio de um gene costuma ser mais destrutiva do que a substituição de uma base, recorrendo ao conceito de quadro de leitura.],
  [A tradução lê o mRNA em trincas (códons), de três em três, a partir de um ponto fixo. Uma substituição troca uma base e, no máximo, muda um aminoácido naquela posição. Já a inserção de uma base — número não-múltiplo de três — desloca o quadro de leitura: todos os códons seguintes passam a ser lidos fora de fase. A partir do ponto da inserção, cada trinca muda, e a proteína sai inteira trocada a jusante, em geral terminando cedo num códon de parada surgido por acaso. Por isso o frameshift é mais destrutivo.])

#discursiva("Q2",
  [Descreva, em ordem, as quatro etapas do reparo por excisão de nucleotídeo (sistema uvrABC) que corrige um dímero de timina em bactérias.],
  [Primeiro, o complexo uvr reconhece a distorção que o dímero impõe à hélice — repara a deformação geométrica, não a química específica. Segundo, a excinuclease faz duas incisões assimétricas na fita danificada: a 8 nucleotídeos do lado 5′ e a 4 do lado 3′, liberando um oligonucleotídeo de cerca de 12 bases que contém a lesão. Terceiro, a DNA polimerase I preenche a lacuna sintetizando DNA novo sobre a fita-molde intacta. Quarto, a DNA ligase sela a última emenda, restaurando a continuidade da fita. O resultado é a sequência original reconstruída.])

#discursiva("Q3",
  [Um paciente com xeroderma pigmentoso desenvolve câncer de pele ainda na infância. Conecte o defeito molecular ao desfecho clínico.],
  [No xeroderma pigmentoso, as proteínas do reparo por excisão de nucleotídeo (NER) humano são defeituosas — herança autossômica recessiva. Sem NER funcional, os dímeros de pirimidina formados pela luz ultravioleta do sol não são removidos. A cada exposição, eles se acumulam; quando a célula replica o DNA por cima do dímero não-reparado, a lesão se fixa como mutação permanente. Mutações sucessivas em genes que controlam a divisão celular transformam a célula em tumoral. Como o reparo está quebrado, a conta de mutações sobe rápido, e o câncer de pele aparece cedo e em múltiplos pontos.])

#discursiva("Q4",
  [Explique como uma bactéria pode adquirir resistência a um antibiótico sem nunca ter sido exposta a ele, usando os conceitos de plasmídeo e conjugação.],
  [A resistência costuma estar em genes carregados por plasmídeos — moléculas de DNA circular com origem de replicação própria, independentes do cromossomo. Esses genes não precisam surgir de novo em cada célula: eles viajam. Na conjugação, uma bactéria doadora (F⁺) faz contato direto com uma receptora (F⁻) e transfere a ela uma cópia do plasmídeo. A receptora, que era sensível, passa a portar o gene de resistência — e se torna resistente sem nunca ter encontrado o antibiótico. É por isso que a resistência se dissemina tão rápido em hospitais: o gene salta de célula em célula, inclusive entre espécies diferentes.])

#discursiva("Q5",
  [Compare os ciclos lítico e lisogênico do fago lambda e explique por que a integração no sítio attB é um exemplo de recombinação sítio-específica.],
  [No ciclo lítico, o fago sequestra a maquinaria da bactéria, fabrica centenas de cópias de si mesmo, monta novas partículas e rompe (lisa) a célula, liberando a progênie — é rápido e mata o hospedeiro. No ciclo lisogênico, o fago faz o oposto: integra seu DNA ao cromossomo bacteriano e fica latente como prófago, replicado passivamente junto com a célula a cada divisão, até que um estresse (como dano por UV) o induza de volta ao lítico. A integração não é aleatória: ocorre num ponto definido e reconhecível, o sítio attB, próximo ao gene da galactose. Por reconhecer uma sequência-alvo específica — e não depender de longas regiões de identidade, como a recombinação homóloga —, chama-se recombinação sítio-específica.])
