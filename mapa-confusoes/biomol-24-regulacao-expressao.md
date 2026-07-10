# Mapa de Confusões — biomol-24-regulacao-expressao

## PARTE 1 — Por que regular e em que níveis

1. **Regulação ≠ ligar/desligar gene.** Mecanismo do erro: aluno pensa em interruptor binário; na verdade a célula modula um *equilíbrio* de concentração (síntese × degradação), e o gene pode ficar em qualquer ponto entre 0 e máximo. Origem: q-0305.
2. **Controle temporal vs. espacial são eixos independentes.** Erro: tratar "expressa só no embrião" como sinônimo de "expressa só no fígado". Tempo (quando) e tecido (onde) usam mecanismos parcialmente distintos — um TF pode ser ligado pela fase do ciclo, outro pela identidade da célula.
3. **Procarionte concentra na transcrição; eucarionte distribui.** Erro: assumir que ambos regulam pelos mesmos pontos. Procarionte usa mais operon/sigma/riboswitch porque transcrição e tradução são acopladas no citoplasma; eucarionte separa compartimentos e abre janelas em cromatina, splicing, mRNA, tradução e pós-tradução. Origem: q-0309.
4. **Custo metabólico justifica a regulação.** Erro: ver regulação como elegância, não como economia. Cada proteína desnecessária queima ATP; pressão seletiva favorece quem fabrica só o que precisa, quando precisa.

## PARTE 2 — Operon lac e operon trp

1. **Operon ≠ gene.** Erro: tratar lacZ como o "gene da lactase". O operon lac é um *cluster* (lacZ + lacY + lacA) co-transcrito num único mRNA policistrônico a partir de **um promotor**.
2. **LacI sempre é repressor — não muda função.** Erro: dizer "LacI vira ativador quando lactose chega". LacI continua sendo repressor; o que muda é a **afinidade** pelo operador, perdida quando alolactose o liga.
3. **Indutor não ativa — ele desreprime.** Erro: ver alolactose como sinal positivo direto. Alolactose só *remove* o LacI do operador; a transcrição em si depende de quão bem CAP-cAMP recruta a RNA Pol.
4. **CAP-cAMP responde à glicose, não à lactose.** Erro: imaginar que CAP é o sensor de lactose. CAP-cAMP só se forma com **glicose baixa** (porque adenilato ciclase é inibida por glicose). É o sensor de "fome de glicose".
5. **Crescimento diáuxico revela hierarquia.** Erro: pensar que lactose é consumida em paralelo com glicose. Bactéria come glicose primeiro (cAMP baixo → CAP off → operon lac off mesmo sem repressor); só depois liga o operon lac. A curva de crescimento tem dois platôs separados por uma fase lag — sinal de troca de combustível. Origem: q-0305, q-0318.
6. **Operon trp é o espelho do lac.** Erro: aplicar mecanismo lac ao trp. Trp é **anabólico-repressível**: o produto final (triptofano) age como **corepressor**, ativando o TrpR (que sozinho não se liga ao DNA). Lac é catabólico-induzível; trp é anabólico-repressível.
7. **Atenuação é um segundo nível no trp.** Erro: ignorar que existe controle além do TrpR. A região líder do mRNA do trp tem códons de Trp; se Trp-tRNA está abundante, o ribossomo avança rápido e força um stem-loop que termina a transcrição antes dos genes estruturais. Termo-nota *atenuação*.
8. **Riboswitch ≠ atenuação.** Erro: misturar os dois. Riboswitch é o próprio mRNA mudando de conformação ao ligar um metabólito; atenuação depende de ribossomo traduzindo a região líder.

## PARTE 3 — Regulação eucariótica em camadas

1. **Cromatina não silencia em absoluto — modula acesso.** Erro: ver heterocromatina como "DNA bloqueado para sempre". Mesmo regiões compactas têm dinâmica; mudanças de marcas abrem janelas conforme sinal.
2. **Acetilação relaxa; metilação depende do resíduo.** Erro: dizer "metilação reprime". Metilação de H3K9 e H3K27 reprime; metilação de H3K4 ativa. Acetilação de histonas neutraliza carga positiva e afrouxa contato com DNA. Termo-nota *HAT/HDAC*.
3. **Fator de transcrição não é a polimerase.** Erro: confundir TF com RNA Pol II. TFs recrutam a maquinaria; quem polimeriza é a Pol II. Sem TFs específicos, o promotor basal sustenta transcrição mínima.
4. **Enhancer atua a distância — DNA dobra.** Erro: imaginar enhancer colado ao promotor. Enhancers podem estar a kilobases (até mesmo dentro de íntrons) e contatam o promotor por loop de DNA, mediado por proteínas mediadoras.
5. **Splicing alternativo expande proteoma.** Erro: contar 1 gene = 1 proteína. ~20.000 genes humanos geram mais de 100.000 proteínas porque éxons são combinados de formas diferentes em tipos celulares distintos. Termo-nota *splicing alternativo*.
6. **miRNA não toca DNA — silencia mRNA.** Erro: classificar miRNA como regulador transcricional. miRNA, carregado pelo complexo RISC, pareia com mRNA citoplasmático e bloqueia tradução ou marca para degradação.
7. **Pós-tradução modula sem mexer no mRNA.** Erro: assumir que toda mudança de função passa por novo mRNA. Fosforilação por quinase, ubiquitinação, clivagem proteolítica podem ligar/desligar uma proteína em segundos, sem novo transcrito.
8. **Estabilidade do mRNA é alvo regulado.** Erro: pensar que mRNA dura o que tem de durar. Cauda poli-A encurta com o tempo (deadenilação); mRNAs com elementos AU-ricos na UTR 3' têm meia-vida curta — essa janela define quanto a proteína é traduzida.
