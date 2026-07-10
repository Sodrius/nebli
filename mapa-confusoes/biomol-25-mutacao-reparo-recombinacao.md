# Mapa de Confusões — biomol-25-mutacao-reparo-recombinacao

**Slug:** `biomol-25-mutacao-reparo-recombinacao` · **Aula UC02:** mutação, reparo e DNA móvel · **Versão:** 2026-06-24

Catálogo dos erros mecanísticos típicos do tema. Distratoras da E2 puxam DESTE arquivo.

## 1.1 O que é mutação e os três tipos

1. **Substituição causa frameshift** — falso. Trocar uma base mantém o número total de letras; só inserção/deleção não-múltipla de 3 desloca o quadro de leitura. *Origem: banco-confusão clássica.*
2. **Toda deleção causa frameshift** — falso. Deletar múltiplo de 3 remove aminoácidos inteiros sem deslocar as trincas seguintes. *Origem: livro.*
3. **Transição é troca entre purina e pirimidina** — invertido. Transição é entre bases do MESMO tipo químico (A↔G, C↔T); a troca entre tipos é transversão. *Origem: livro.*
4. **Lesão já é mutação** — falso. Lesão (dímero, base alterada) só vira mutação se a célula replicar por cima sem reparar; há uma janela de reparo. *Origem: lógica de reparo.*

## 1.2 Mutações espontâneas e a fidelidade da replicação

1. **Fidelidade vem só da seletividade da polimerase** — incompleto. A revisão (proofreading) que remove a base errada incorporada é a segunda linha que derruba a taxa para ~1 em 1 bilhão. *Origem: livro.*
2. **O tautômero é estável e some sozinho** — falso. É uma forma rara e fugaz; o erro nasce justo se a replicação flagra a base nesse instante e encaixa o parceiro errado. *Origem: livro.*
3. **Deaminação da citosina gera adenina** — falso. Gera uracila, que pareia como timina e semeia transição C→T. *Origem: livro.*
4. **Mutação espontânea precisa de agente externo** — falso. Tautomerismo e deaminação ocorrem sem mutagênico; o "espontâneo" é justamente a origem interna. *Origem: slide-06/07.*

## 1.3 Mutações induzidas: química e radiação UV

1. **5-BrU pareia sempre com guanina** — falso. Entra como timina (pareia A) e só na forma alterada reconhece G; a troca leva rodadas de replicação. *Origem: slide-12.*
2. **UVA é o principal causador do dímero de timina** — falso. O UVB é absorvido diretamente pelas bases e gera o dímero; UVA age mais por radicais livres. *Origem: slide-13/16.*
3. **O dímero de timina une bases de fitas opostas** — falso. Une duas pirimidinas vizinhas na MESMA fita, deformando a hélice. *Origem: slide-17.*
4. **Análogo de base corta o DNA** — falso. Ele não cliva nada; apenas imita uma base e engana o pareamento. *Origem: slide-11.*

## 2.1 Reparo direto: fotoliase e MGMT

1. **Humano repara dímeros por fotoliase** — falso. Fotoliase é bem caracterizada em bactérias; humanos dependem do NER para dímeros. *Origem: slide-28.*
2. **MGMT é catalítica e se regenera** — falso. Transfere a metila para uma cisteína própria e se inativa de vez: uma proteína gasta por lesão (uso único). *Origem: slide-30/31.*
3. **Reparo direto corta e ressintetiza a fita** — falso. Reparo direto desfaz a lesão no lugar, sem incisão nem remoção de trecho. *Origem: lógica de reparo.*
4. **Fotoliase usa UV para reparar** — impreciso. Usa luz visível captada por cofator derivado do folato; o UV é o que CAUSA o dímero. *Origem: slide-28/29.*

## 2.2 Reparo por excisão de nucleotídeo

1. **As incisões do NER são simétricas** — falso. São assimétricas: 8 nt do lado 5′ e 4 nt do 3′, removendo ~12 nt. *Origem: slide-18/20.*
2. **A Pol III preenche a lacuna do NER** — falso. No NER bacteriano é a DNA polimerase I que preenche, e a ligase sela. *Origem: slide-19.*
3. **O NER reconhece a química específica da lesão** — falso. Reconhece a distorção geométrica da hélice; por isso repara lesões diversas. *Origem: slide-20.*
4. **NER dispensa a fita-molde** — falso. Reconstrói o trecho recortado usando a fita complementar intacta como guia. *Origem: livro.*

## 2.3 Quando o reparo falha: xeroderma e SOS

1. **Xeroderma é dominante** — falso. É autossômico recessivo: precisa das duas cópias do gene de reparo defeituosas. *Origem: slide-24/25.*
2. **Xeroderma é falta de pigmento** — falso. O nome engana; o defeito é no NER, e o câncer vem do acúmulo de dímeros não-reparados. *Origem: slide-24.*
3. **A resposta SOS é ligada por LexA ativo** — invertido. LexA é o repressor; a SOS liga quando RecA estimula a AUTOCLIVAGEM de LexA. *Origem: slide-26.*
4. **SOS é disparada por falta de nutrientes** — falso. O gatilho é dano extenso ao DNA (ex.: UV), que expõe fita simples e ativa RecA. *Origem: slide-26.*

## 3.1 Plasmídeos, fator F e conjugação

1. **Plasmídeo depende do cromossomo para replicar** — falso. É replicon: tem origem de replicação própria e copia com autonomia. *Origem: slide-35/36.*
2. **Conjugação é fusão das duas bactérias** — falso. Há contato e transferência de uma CÓPIA do plasmídeo; as células seguem separadas, a F⁻ vira F⁺. *Origem: slide-37/38.*
3. **Adquirir resistência exige contato com o antibiótico** — falso. Por conjugação, a receptora ganha o gene sem nunca ter encontrado o antibiótico. *Origem: slide-36.*
4. **Plasmídeo é sempre linear** — falso. É uma molécula de DNA circular. *Origem: slide-33/35.*

## 3.2 Transposons: genes que saltam

1. **Transposon = plasmídeo** — falso. Plasmídeo viaja ENTRE células (conjugação); transposon salta DENTRO do genoma (transposase). *Origem: slide-33/39.*
2. **O salto não precisa de enzima** — falso. É catalisado pela transposase, em geral codificada pelo próprio transposon. *Origem: slide-40.*
3. **Sequência de inserção (IS) e Tn são a mesma coisa** — impreciso. IS é a forma simples (só a transposase); Tn carrega genes extras, em geral resistência. *Origem: slide-40/41.*
4. **Transposons são uma fração mínima do genoma humano** — falso. Compõem fração enorme, bem maior que a que codifica proteína. *Origem: slide-40.*

## 3.3 Vírus, fago lambda e recombinação sítio-específica

1. **Lítico e lisogênico são fagos diferentes** — falso. O mesmo fago lambda escolhe entre os dois; o prófago pode ser induzido ao lítico. *Origem: slide-45/49.*
2. **O prófago fabrica vírus o tempo todo** — falso. Está latente, replicado passivamente com o cromossomo, até ser induzido. *Origem: slide-45.*
3. **A integração do lambda é aleatória** — falso. Ocorre no sítio attB específico (recombinação sítio-específica), perto do gene da galactose. *Origem: slide-46/48.*
4. **Vírus se reproduz sozinho** — falso. Depende inteiramente da maquinaria da célula hospedeira para replicar seu material genético. *Origem: slide-44.*
