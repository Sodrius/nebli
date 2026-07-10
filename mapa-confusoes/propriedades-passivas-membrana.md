# Mapa de Confusões — Propriedades passivas da membrana

Construído pelo ORQUESTRADOR antes de delegar à E2. Cada subtópico tem 4 confusões (36 total). QUESTIONADOR escolhe 3-4 por questão MC e 2 por questão C/E, deixando explícito qual confusão cada distratora encarna.

## 1.1 Da química para a eletricidade (Em, gradientes, condutâncias)

1. **Em = ENa - EK ou média aritmética** — atribui o potencial de membrana à mera diferença entre os potenciais de equilíbrio, ignorando que Em é uma **média ponderada pelas condutâncias** (equação de Goldman). Em pende para o íon mais permeável, não para a média. (origem: armadilha clássica de Nernst × GHK)
2. **Equilíbrio = corrente individual zero** — confunde "equilíbrio elétrico da membrana no repouso" (corrente líquida total = 0) com "cada íon tem fluxo zero". Verdade: K⁺ sai continuamente, Na⁺ entra continuamente; as correntes se cancelam, mas existem. (origem: banco NEBLI)
3. **Potencial de Nernst depende da condutância** — mistura Eion (Nernst, calcula só a partir de concentrações dentro/fora) com Em (que precisa das condutâncias). Eion é um "valor-alvo" químico de cada íon; Em é o valor real que a célula atinge. (origem: livro-texto Boron)
4. **Bomba Na/K cria o Em diretamente** — acha que a Na⁺/K⁺-ATPase é o autor direto do potencial de membrana. Verdade: a bomba **mantém os gradientes** ao longo do tempo (consumindo ATP); o Em em si vem da **difusão passiva** pelos canais de vazamento. Sem bomba, o Em desaba em minutos a horas; sem canal de vazamento, o Em não existe. (origem: armadilha clínica — ouabaína)

## 1.2 A bicamada lipídica é um capacitor

1. **Capacitor = canal aberto** — confunde o papel da bicamada (separar cargas, atuar como dielétrico fino entre dois "reservatórios" de íons) com o do canal (deixar íons atravessarem). Capacitor armazena; canal conduz. (origem: armadilha conceitual recorrente)
2. **C depende do número de canais** — acha que mais canais = mais capacitância. Verdade: C depende da **área da membrana** (mais área = mais C) e da **espessura da bicamada** (mais fina = mais C). Mielina engrossa o "dielétrico efetivo" → reduz C. (origem: livro-texto Kandel)
3. **Corrente capacitiva passa pelos canais** — confunde iC (acumulação de cargas nas duas faces da bicamada, sem atravessar) com iR (cargas que efetivamente atravessam pela proteína-canal). iC "carrega" o capacitor; iR "vaza" pelos canais. (origem: banco NEBLI)
4. **C = V/Q (invertido)** — erro algébrico básico que muda o sentido físico. Verdade: **C = Q/V** — capacitância é a capacidade de armazenar carga por unidade de voltagem. Para a mesma ΔV, C maior = mais carga acumulada = demora mais para mudar V. (origem: armadilha de fórmula)

## 1.3 Os canais iônicos são resistências em paralelo

1. **R = g (não 1/g)** — confunde resistência com condutância. Verdade: **R = 1/g**. Quando muitos canais abrem, g sobe, R cai. (origem: armadilha algébrica básica)
2. **R em paralelo soma direto** — usa a fórmula serial (R_total = R1 + R2 + R3) para resistências em paralelo. Verdade: **1/R_total = 1/R1 + 1/R2 + 1/R3**, ou equivalentemente, **g_total = g_K + g_Na + g_Cl**. (origem: livro-texto Boron)
3. **Rm cai → menos canais abertos** — invertido. **Rm cai = MAIS canais abertos**, porque mais canais = mais condutância = menos resistência. Pensar no canal como "buraco na parede": mais buracos = a parede deixa passar mais corrente = "menos resistente". (origem: banco NEBLI)
4. **Rm de repouso é dominada por canais voltagem-dep** — ignora os canais de vazamento. Verdade: no repouso, a maior parte de Rm vem de **canais de vazamento de K⁺** (sempre abertos); canais voltagem-dep estão majoritariamente fechados. (origem: livro-texto Costanzo)

## 2.1 Despolarização e hiperpolarização

1. **ΔV = Em (não V − Em)** — confunde a variação com o valor absoluto. Verdade: **ΔV = V − Em** — quanto o potencial se afastou do repouso. Se Em = -70 mV e V = -60 mV, ΔV = +10 mV (despol); se V = -80 mV, ΔV = -10 mV (hiperp). (origem: armadilha de fraseado)
2. **Despolarização = potencial mais negativo** — invertido. **Despol = potencial menos negativo** (sobe na escala, aproxima do zero). Hiperp = mais negativo (desce, afasta do zero). (origem: armadilha clássica)
3. **Despolarização sub-limiar sempre dispara PA** — confunde despol passiva (sub-limiar, decai) com supralimiar (atinge gatilho, abre canais Na⁺ voltagem-dep, dispara PA). (origem: livro-texto Boron)
4. **Hiperpolarização = ↑afluxo de Na⁺** — confunde mecanismo. Hiperp acontece por **↑saída de K⁺** (canais K⁺ extras abertos) ou **↑entrada de Cl⁻** (canais Cl⁻ abertos, ex.: GABA-A). Na⁺ entrando = despol. (origem: armadilha clínica — IPSP)

## 2.2 Corrente capacitiva vs resistiva

1. **iC presente sempre** — acha que iC continua durante todo o pulso. Verdade: **iC só existe quando V está mudando** (dV/dt ≠ 0). No plateau, dV/dt = 0 → iC = 0; toda a corrente vai como iR. (origem: armadilha gráfica)
2. **iR predomina no início** — invertido. **No início**, V mal mudou → força motriz pequena → **iR baixa**; toda a corrente externa vai como iC (carregando o capacitor). À medida que V sobe, iR cresce e iC cai. (origem: livro-texto Kandel)
3. **iC atravessa os canais** — confunde caminho físico. **iC = cargas se acumulando** nas faces interna e externa da bicamada — não atravessam. iR = cargas que **efetivamente atravessam** pelos canais. (origem: banco NEBLI)
4. **im = iR (esquece iC)** — confunde corrente total com componente resistivo. Verdade: **im = iC + iR**. Esquecer iC é não entender por que a despol é gradual. (origem: armadilha conceitual)

## 2.3 Constante de tempo τ = RmC

1. **τ = Rm + C (soma)** — errou a operação. Verdade: **τ = Rm × C** (produto). Soma não faz sentido dimensional (Ω + F). (origem: armadilha algébrica)
2. **τ menor = resposta mais lenta** — invertido. **τ menor = resposta MAIS rápida**. τ é o tempo característico: quanto menor, mais rápido o potencial sobe e estabiliza. (origem: armadilha gráfica)
3. **τ só depende da resistência** — esquece o capacitor. Aumentar C (mais membrana, mais área) deixa a resposta mais lenta mesmo com Rm igual. (origem: livro-texto Boron)
4. **τ é a constante espacial (confunde com λ)** — confunde os dois. τ governa **tempo** (em segundos); λ governa **espaço** (em mm). São fenômenos diferentes: τ explica por que a resposta a um pulso demora; λ explica por que o sinal cai com a distância. (origem: armadilha estrutural)

## 3.1 Por que o sinal cai com a distância (fuga + Ri)

1. **Eletrotônica = sem decaimento** — acha que sinal passivo viaja sem perdas, "como num fio". Verdade: **cai exponencialmente** — quanto mais longe, menos sinal. Só o PA viaja sem decaimento (porque é regenerativo). (origem: armadilha conceitual fundamental)
2. **Fuga pela Rm é desejável** — confunde papel mecanístico. Fuga pela Rm = **perda de sinal pra fora**, ruim para alcance. λ é maior quando **Rm é maior** (membrana isolante, pouco vazamento). (origem: livro-texto Costanzo)
3. **Ri alta = sinal viaja longe** — invertido. **Ri alta = corrente trava no citoplasma = sinal não chega longe.** λ é maior quando **Ri é menor** (citoplasma "transparente" à corrente). (origem: banco NEBLI)
4. **Eletrotônica = igual ao PA** — confunde sinal passivo (graduado, decai com distância e amplitude do estímulo) com PA (tudo-ou-nada, regenerativo, amplitude fixa). Sinapses produzem sinal **eletrotônico**; o axônio carrega **PA**. (origem: armadilha estrutural)

## 3.2 Constante de espaço λ = √(Rm/Ri)

1. **λ = Rm × Ri (multiplica)** — errou a operação. Verdade: **λ = √(Rm/Ri)** — razão, depois raiz. λ aumenta com Rm (isolamento) e cai com Ri (resistência interna). (origem: armadilha algébrica)
2. **λ é tempo (confunde com τ)** — confunde dimensão. λ é distância (mm); τ é tempo (ms). (origem: armadilha estrutural)
3. **λ maior = resposta mais rápida no tempo** — confunde domínio. λ governa **alcance espacial** (até onde o sinal chega); a velocidade temporal é governada por τ e pela combinação λ/τ. (origem: armadilha de domínio)
4. **λ = distância em que V = 0** — erro de definição. **λ = distância em que V cai para Vmax/e ≈ 37%** do valor inicial — não zera, decai exponencialmente. Aos 3λ, ainda sobra ~5%. (origem: livro-texto Kandel)

## 3.3 Mielina e diâmetro do axônio

1. **Mielina = mais canais expostos** — confunde efeito. **Mielina isola** — reduz canais expostos a quase zero entre nodos de Ranvier (canais ficam concentrados só nos nodos). (origem: armadilha clínica EM)
2. **Mielina = ↑capacitância** — invertido. **Mielina REDUZ C** — mais camadas de membrana entre o axoplasma e o extracelular = "dielétrico mais espesso" = capacitância menor = capacitor carrega mais rápido = τ menor. (origem: livro-texto Costanzo)
3. **Diâmetro maior → Ri maior** — invertido. **Diâmetro maior → Ri MENOR** — mais área de seção transversal = mais "espaço" para a corrente fluir no citoplasma. Por isso axônios de invertebrados (lula) são gigantescos: aumentar diâmetro foi a solução evolutiva pré-mielina. (origem: livro-texto Kandel)
4. **Desmielinização = velocidade aumentada** — invertido. Desmielinização → ↑C (canais expostos, dielétrico fino) e ↓Rm (correntes vazam) → **τ maior, λ menor** → propagação mais lenta ou bloqueada. Sintomas: visão turva (neurite óptica), fraqueza (Guillain-Barré). (origem: armadilha clínica EM e Guillain-Barré)
