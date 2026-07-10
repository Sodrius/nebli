# Revisão profunda Tier 3 — UC01-FMEMB-02-sistemas-de-transporte-na-membrana

**Tema (ancoragem):** Sistemas de transporte na membrana (Fisiologia, UC1)
**3 conceitos centrais que o aluno-alvo quer aprender:**
1. Por que algumas moléculas atravessam sozinhas e outras precisam de proteína — e que regra física separa as duas.
2. Como uma proteína consegue mover soluto *contra* o gradiente — onde entra ATP, onde entra "carona" do Na+.
3. Por que a Na/K-ATPase é tratada como "motor de tudo" — o que de fato ela sustenta na fisiologia.

**2 temas vizinhos que NÃO são esse:** potencial de ação (mecânica do disparo neuronal); sinalização por proteína G (cascatas intracelulares). Estão tangenciados em boxes (digoxina, AMPA, cólera) mas não são o assunto.

**Autor:** Italiano (NEBLI — apostila histórica antes do pipeline atual)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real com fisiologia de membrana, ensino médio + meses
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25
**PDF:** 38 páginas, 10 535 palavras, 9 imagens, média 277 palavras/página
**Páginas amostradas (estrutura JSON + texto):** 1, 2, 4, 5, 17, 23, 38
**Nota metodológica:** `pdftoppm` instalado mas fora do sandbox seguro do Read tool. Análise visual feita por triangulação entre (a) JSON de estrutura com contagem de imagens por página, (b) marcações textuais de boxes/mapas conceituais/legendas preservadas no .txt, (c) revisão Tier 2 prévia que já reportou densidade e distribuição visual.

---

## 1. Pontos de parada (simulação linha-a-linha do aluno-alvo)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Abertura ("por que precisamos discutir transporte?") | SEGUE | 3 | Pergunta ingênua + resposta ancorada na 2ª lei da termodinâmica em uma frase. Aluno sente que está sendo conduzido. |
| 1.1 Lipossolubilidade ("sanduíche de óleo entre fatias de pão molhado") | SEGUE | 3 | Metáfora instantânea, traz junto o porquê (custo de largar camada de hidratação). |
| 1.2 — fórmula `v = √(3KT/m)` aparece sem dizer o que K significa antes | **[STOP: p.4]** | 4 | Aluno lê "K é a constante de Boltzmann" mas nunca ouviu falar; sem 1 frase explicando "constante que mede agitação térmica em escala microscópica", ele trava. A próxima fórmula (Fick) chega antes de ele se recompor. |
| 1.2 Lei de Fick (J = −D·A·ΔC/Δx) | SEGUE | 5 | Aqui o autor faz bem: aborda cada variável com "gesto físico" depois da fórmula. Recupera o aluno que parou em K. |
| 1.3 O2 e CO2 ("a fisiologia delega o transporte para a física") | SEGUE | 6 | Frase-síntese excelente; aluno entende por que não há "bomba de O2". |
| 2.1 GLUT-1/GLUT-2/Km — "Km baixo = transportador ávido" | SEGUE | 8 | Box "KM como decisão tecidual" responde a pergunta-armadilha antes do aluno fazer. |
| 2.2 Canais — "10² a 10⁴ moléculas/s vs 10⁶ a 10⁸ íons/s" | **[STOP curto: p.9]** | 9 | Os expoentes estão truncados no .txt como "10�10" em vários lugares — no PDF render aparecem correto, mas o aluno, vendo "quatro a seis ordens de magnitude", precisa de uma ancoragem do que isso significa concretamente. Autor não traduz para tempo de disparo (ex: "1 íon a cada 10 ns no canal vs 1 a cada 100 µs no transportador") — perde gesto físico. |
| 2.3 Tabela canal × transportador | SEGUE | 11 | Variação de registro (prosa → tabela) bem-vinda. |
| 3.1 Bomba — ciclo 3 Na+/2 K+/1 ATP | SEGUE | 13 | Coreografia descrita em sequência temporal clara. |
| 3.1 — "três outras bombas importantes" (SERCA, H/K-ATPase, V-ATPase) parágrafo único corrido | **[STOP: p.14]** | 14 | Três bombas distintas, três fisiologias, ATPase tipo P × tipo V — tudo num parágrafo só. Aluno em dificuldade lê SERCA, esquece, lê parietal, esquece, lê lisossomo, fecha. Falta micro-estrutura (mini-tabela ou três frases-síntese isoladas) e ancoragem da diferença P × V. |
| 3.2 Cólera + SRO (box clínico) | SEGUE | 16 | Box é um dos pontos altos da apostila — narrativa clara com final salvador. |
| 3.3 Na/K-ATPase como motor de tudo | SEGUE | 17 | Três efeitos numerados (gradiente Na+, gradiente K+, eletrogênica). Box "Eletrogênico não é o que faz o potencial de repouso" desfaz a confusão recorrente. |
| 3.3 — "potencial de repouso", "-70 mV", "potencial de equilíbrio do K+" | **[STOP: p.17]** | 17 | Aqui é o STOP mais sério. O conceito de potencial de equilíbrio do K+ (-90 mV) é mobilizado como se o aluno já tivesse visto Nernst. Mas em UC1 FMEMB-02 isso ainda não foi dado — vem em FMEMB-08 (eletrofisiologia). O aluno em dificuldade percebe o buraco e fecha o PDF achando que "perdeu" pré-requisito. Falta a frase-paraquedas ("veremos em eletrofisiologia; por ora basta saber que..."). |
| Conclusão integradora | SEGUE | 18 | Integra os três blocos com voz didática. |
| Resumindo (2 colunas, banner gold) | SEGUE | 19 | 8 cápsulas autossuficientes, ordenadas por relevância clínica. |
| Etapa 2 Q01–Q25 | SEGUE | 20–31 | Distratoras mecanísticas de qualidade até Integração. |
| Etapa 2 Q26–Q30 (Aplicação) | **[STOP cognitivo: p.32–34]** | 32–34 | Confirma o "Erro 1 do NEBLI": distratoras de Aplicação encurtam (10–12 palavras) enquanto a correta carrega 25–35 palavras de mecanismo. Aluno responsável acerta por contagem visual, não por raciocínio mecanístico. |

**Total de STOPs:** 4 (1 menor em p.4, 1 curto em p.9, 1 estrutural em p.14, 1 crítico em p.17). O PDF segue até o fim — STOPs são solucionáveis com frases-paraquedas curtas e uma reescrita da seção 3.1 final.

---

## 2. T3.1 — Comparação com EXEMPLARES.md

Categorias relevantes selecionadas: **C1** (mecanismo parágrafo-por-parágrafo), **C2** (pergunta motivadora), **C4** (magnitudes ancoradas), **C7** (analogia construtiva), **C12** (cálculo bem explicado), **C17** (catálogo de família).

### Comparação A — Abertura mecanística (C1 vs Italiano)

**EXEMPLARES C1.1 (Transmissão Sináptica, sinapse química):**
> "O neurotransmissor atravessou a fenda por difusão. Agora ele precisa ser 'lido' pela membrana pós-sináptica — e é aqui que a natureza do sinal depende completamente do tipo de receptor encontrado."

**Italiano (p.3, abertura da E1):**
> "Antes de mergulhar em bombas, canais e curvas de saturação, vale parar e perguntar a coisa óbvia que ninguém costuma perguntar: por que precisamos discutir transporte? A resposta é direta. A membrana plasmática é boa demais no que faz."

**Veredito:** Italiano supera o exemplar nessa abertura específica. O exemplar C1.1 começa numa pergunta intermediária (já dentro do mecanismo); Italiano abre num nível mais ingênuo ("por que precisamos discutir transporte?"). Para o aluno-alvo declarado (dificuldade real, pouco conhecimento), o nível de Italiano é mais acolhedor. **Lição para o REDATOR-E1:** abrir a E1 numa pergunta mais ingênua do que o instinto pede.

### Comparação B — Magnitude ancorada (C4 vs Italiano)

**EXEMPLARES C4.1 (Enzimas I, anidrase carbônica):**
> "as enzimas aceleram reações em fatores de 10⁶ a 10¹² em comparação com as reações não catalisadas. A anidrase carbônica, por exemplo, acelera a hidratação do CO₂ por um fator de 10⁷."

**Italiano (p.9, velocidade de canal vs transportador):**
> "Um transportador típico move 10² a 10⁴ moléculas por segundo. Um canal aberto move 10⁶ a 10⁸ íons por segundo — quatro a seis ordens de magnitude mais rápido."

**Veredito:** Italiano traz o número certo e o range; mas o exemplar C4.1 *ancora* com referência externa ("catalisador industrial — centenas de graus, pressões altas"). Italiano para no número e na palavra "ordens de magnitude". **Lição:** Italiano poderia ter ancorado: "10⁸ íons/s significa um íon a cada 10 nanossegundos — mais rápido que o tempo de um neurônio decidir disparar". O exemplar venceria essa comparação porque o número, sem ancoragem temporal/intuitiva, vira decoreba. **Para o REDATOR-E1:** quando soltar potência de 10, anexar comparação externa em até 1 frase.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação completa)

### Parágrafo 1 — As três outras bombas (p.14)

**(a) Citação literal:**
> "Vale citar três outras bombas importantes porque cada uma sustenta uma fisiologia específica. A Ca²-ATPase do retículo sarcoplasmático (SERCA) bombeia cálcio do citoplasma de volta para o retículo, e é o que termina a contração muscular — sem SERCA ativa, o músculo não relaxa. A H+/K+-ATPase das células parietais gástricas bombeia H+ para a luz do estômago contra um gradiente de quase 10⁶ (pH 1 versus pH 7 no citoplasma); é nessa bomba que os inibidores de bomba de prótons (omeprazol e similares) atuam. A V-ATPase, espalhada em vesículas, mantém o pH ácido do lisossomo (pH 4,5), o que ativa enzimas hidrolíticas e mantém o resto da célula seguro de uma acidificação acidental."

**(b) Diagnóstico mecanístico:** três bombas distintas em três fisiologias distintas (muscular, gástrica, lisossomal), com duas famílias estruturais diferentes (P × V) tudo num parágrafo de 5 frases. Para o aluno-alvo, isso é overload — ele lê linear, esquece SERCA quando chega em V-ATPase. A diferença mecanística entre tipo P (autofosforila) e tipo V (não autofosforila) é citada na legenda da figura anterior mas nunca enfatizada como organizadora. Falta também a ponte para Q23 (V-ATPase do lisossomo) e Q18 (omeprazol) da Etapa 2 — o aluno não vai conectar.

**(c) Reescrita pronta:**
> "Vale citar três outras bombas — cada uma com um trabalho fisiológico próprio.
>
> **SERCA** (Ca²-ATPase do retículo sarcoplasmático). Família P, mesma do Na/K. Bombeia Ca² do citoplasma de volta para o retículo, e é o que termina a contração muscular: sem SERCA ativa, o músculo não relaxa porque o cálcio que disparou a contração não tem caminho de volta.
>
> **H+/K+-ATPase** das células parietais gástricas. Também família P. Bombeia H+ contra um gradiente brutal — pH 1 na luz do estômago contra pH 7 no citoplasma, fator 10⁶. É essa bomba que o omeprazol bloqueia (voltamos a isso na Etapa 2, Q18).
>
> **V-ATPase** (vacuolar). Família estrutural diferente — não autofosforila, gira como um rotor. Espalhada nas membranas de lisossomos e endossomos, mantém o pH interno em 4,5, condição que ativa as hidrolases lisossomais e mantém o resto da célula segura.
>
> O fio comum: as três pagam ATP direto e cada uma sustenta uma fisiologia que para sem elas (relaxar, digerir, degradar)."

Diferença: 3 sub-blocos visualmente distintos, família estrutural explícita, ponte para Q18, frase-síntese fechando.

### Parágrafo 2 — Movimento browniano e fórmula v = √(3KT/m) (p.4)

**(a) Citação literal:**
> "A velocidade média de uma molécula nesse 'andar bêbado' é dada por uma fórmula da teoria cinética dos gases adaptada para líquidos: v = √(3KT/m) onde K é a constante de Boltzmann, T a temperatura em Kelvin e m a massa da molécula. O gesto físico aqui é o seguinte: aumentar a temperatura aumenta a agitação (velocidade sobe com √T); aumentar a massa diminui a agitação (velocidade cai com 1/√m)."

**(b) Diagnóstico:** o autor introduz uma fórmula com 3 variáveis e nomeia K como "constante de Boltzmann" sem explicar 1 frase do que ela é. Aluno-alvo de UC1 não viu Boltzmann no ensino médio — vai parar. Pior: a fórmula não é usada depois (Fick não a usa). Ela serve só para motivar "por que perfume difunde mais rápido que açúcar dissolvido", o que poderia ser feito em prosa pura.

**(c) Reescrita pronta:**
> "A velocidade média desse caminhar aleatório depende de duas coisas que a intuição já dá: quanto mais quente o meio, mais agitação (a velocidade sobe com a raiz da temperatura); quanto mais pesada a molécula, menos agitação (velocidade cai com a raiz da massa). É por isso que perfume difunde mais rápido que açúcar dissolvido: não porque seja 'volátil' no sentido mágico, mas porque suas moléculas são leves. Quem quiser o número exato encontra a fórmula `v = √(3kT/m)` na teoria cinética — para o que vamos fazer com a Lei de Fick adiante, a intuição basta."

Diferença: remove o STOP em "K constante de Boltzmann" sem perder o gesto físico; sinaliza que a fórmula existe para quem quer fundo.

### Parágrafo 3 — Potencial de repouso e Nernst implícito (p.17)

**(a) Citação literal:**
> "Segundo, ela mantém o gradiente de K+ alto dentro. Esse gradiente é a base do potencial de repouso da membrana — o K+ tende a sair (porque está mais concentrado dentro), e o vazamento permanente de K+ por canais de 'vazamento' mantém a célula com interior negativo."

E mais à frente, no modelo da Q3 da Etapa 3:
> "Essa saída deixa o interior negativo até atingir o potencial de equilíbrio do K+ (~-90 mV)."

**(b) Diagnóstico:** o conceito de "potencial de equilíbrio de um íon" é da equação de Nernst — não foi apresentado em FMEMB-02. O aluno-alvo vai ler "-90 mV" e perguntar "por que esse número? de onde veio?". A apostila não responde nem sinaliza onde vai responder. É o STOP mais sério porque mina a confiança do aluno ("eu não sabia disso, devo ter perdido alguma aula").

**(c) Reescrita pronta (parágrafo do texto E1 + acréscimo à Q3):**
> "Segundo, ela mantém o gradiente de K+ alto dentro. Esse gradiente é a base do potencial de repouso: o K+, mais concentrado dentro, tende a sair por canais 'de vazamento' sempre abertos. Cada K+ que sai leva uma carga positiva embora — e o interior fica progressivamente mais negativo até a atração elétrica (negativo puxando o positivo de volta) equilibrar o gradiente químico (mais K+ dentro empurrando para fora). Esse ponto de equilíbrio é por volta de -90 mV para o K+; o cálculo formal sai da equação de Nernst, que vocês veem em eletrofisiologia. Por ora basta: a bomba criou o gradiente, o vazamento de K+ lê esse gradiente como voltagem."

Diferença: explica o mecanismo do equilíbrio (química × elétrica) em uma frase, ancora Nernst sem exigir que o aluno saiba, sinaliza onde vai aprofundar.

---

## 4. T3.3 — 3 seções mais densas (densidade × páginas e mitigação)

| Seção | Pág | Palavras | Densidade observada | Mitigação concreta |
|---|---|---|---|---|
| 3 outras bombas (SERCA, H/K, V) | 14 | ~150 em 1 parágrafo único | 3 fisiologias + 2 famílias estruturais sem sub-quebra | Reescrita acima (3 sub-blocos com negrito da bomba). |
| 1.2 Fick + gesto físico de cada variável | 5 | ~340 | Fórmula + 4 variáveis explicadas em sequência + EAP em box + Fick para CO2 — tudo na mesma página | Quebrar em 2 páginas: variáveis em p.5, EAP+Fick para gases em p.6. Reduz para 200 pp/pág. |
| Conclusão integradora + Resumindo | 18–19 | 442 + 200 | Densidade aceitável, mas Resumindo carrega 8 cápsulas em 2 colunas — corre risco de "muro" | Considerar 7 cápsulas em vez de 8, com mais respiro entre elas. Cápsula "Tudo é combinação dos três" pode virar fecho visual destacado. |

Observação: as seções 1.1 (lipossolubilidade), 2.1 (GLUT-Km), 2.2 (canais com comporta) e 3.1 (Na/K-ATPase) NÃO são densas — o autor consegue manter ~250 pp/pág com diálogo. O problema concentra-se em 1.2 e 3.1-final, exatamente onde aparece matemática ou catálogo.

---

## 5. T3.4 — Voz fora do padrão (citações)

Apostila é fortemente consistente em voz dialogal de monitor. Saliências:

- **Voz didática exemplar (p.13, box digoxina):** *"E daí o que acontece é interessante — o miocárdio tem um trocador Na/Ca... Com mais Na+ intracelular, o gradiente de Na+ cai, o trocador trabalha menos, e o Ca² intracelular sobe. Mais cálcio nos cardiomiócitos = contração mais forte. É assim que um inibidor de bomba se torna um inotrópico positivo."* — esse é o nível-padrão de NEBLI quando funciona.
- **Voz quase-formal (p.4):** *"A velocidade média de uma molécula nesse 'andar bêbado' é dada por uma fórmula da teoria cinética dos gases adaptada para líquidos"* — momentaneamente vira manual antes de retomar o gesto físico. Aceitável mas não exemplar.
- **Voz sentenciosa eficaz (p.17):** *"a Na/K-ATPase é mais que uma bomba — é a infraestrutura"* — frase-síntese curta, alta densidade conceitual, sem perder dialogismo.

Não há saída-de-personagem clínica (tipo "vai cair na prova"). Voz limpa de manual.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** página 17 (3.3 — Na/K-ATPase como motor de tudo + box "Eletrogênico não é o que faz o potencial de repouso").

A página acumula em ~520 palavras: (i) integração retrospectiva dos três efeitos da bomba, (ii) introdução implícita de potencial de repouso, (iii) introdução implícita de potencial de equilíbrio de K+, (iv) eletrogênese e contribuição direta de 5–10 mV, (v) clínica de isquemia + edema celular agudo, (vi) box desfazendo confusão sobre eletrogênese vs Nernst. **6 ideias-densas em uma página.** Para o aluno-alvo é o pico.

**3 mitigações possíveis:**

1. **Quebrar em duas páginas.** Página A: gradiente Na+ + gradiente K+ + eletrogênese (3 efeitos). Página B: aplicação clínica (isquemia) + box "eletrogênico ≠ Nernst". Reduz para 3 ideias-densas por página.

2. **Adicionar frase-paraquedas de pré-requisito.** Antes de "potencial de equilíbrio do K+ (-90 mV)", inserir 1 frase explicando o gesto físico do equilíbrio químico/elétrico (vide reescrita do parágrafo 3 acima). Custa 2 linhas; salva o STOP crítico.

3. **Figura adicional.** A revisão Tier 2 já apontou que p.17–p.38 não têm imagem. Uma figura esquemática do ciclo Na/K + cabo elétrico de canais de K+ "vazando" + sentido do potencial gerado resolveria simultaneamente o problema visual e o cognitivo.

**Escolha:** opção 2 (frase-paraquedas) tem custo mínimo e ganho máximo — é o que mais devolve confiança ao aluno-alvo. Opção 3 é o "ideal" mas demanda asset novo. Opção 1 (quebrar página) é melhor combinada com 2, não isolada.

---

## 7. T3.8 — ANÁLISE VISUAL (do PDF, triangulada)

Análise feita por triangulação: estrutura JSON (contagem de imagens por página) + marcadores textuais no .txt + revisão Tier 2 prévia (que mapeou boxes, mapas conceituais e cores).

**Hierarquia tipográfica:** o .txt preserva: faixa "N E B L I · A P O S T I L A" como header de toda página, títulos "ETAPA 1 — TEXTO DIDÁTICO" como subheader, "PARTE I/II/III" como nível 2, "1.1 / 1.2 / ..." como nível 3, "Síntese N —" como blocos numerados. Hierarquia presente em 4 níveis — adequada. Os "MAPAS CONCEITUAIS" no fim de cada PARTE aparecem com diagramação ASCII no .txt, sugerindo que no PDF rodam como bloco visual destacado (provavelmente caixa com fundo claro + 3 colunas). Boxes clínicos ("Edema pulmonar e a lei de Fick", "Digoxina e a Na/K-ATPase", "Cólera e a SRO", "Eletrogênico não é o que faz o potencial de repouso") aparecem sempre com título isolado no .txt, sugerindo banner colorido no PDF.

**Valor pedagógico das figuras:** 9 imagens distribuídas em p.5, 6, 8, 9, 11, 13, 14, 15, 16 — todas na primeira metade. Cada uma tem legenda própria embutida no fluxo de texto (extraídas do .txt):
- p.5: "Repare como a gota de tinta começa concentrada num ponto e se espalha sozinha..." — figura de difusão livre, legenda forte (mecanismo explícito na legenda).
- p.6: "Sangue arterial (pO2 alta) banha tecidos com pO2 baixa. O O2 sai por difusão pura." — figura da troca tecidual, legenda concisa.
- p.8: figura da curva Jmax/Km com legenda "Repare como a curva sobe quase linear em baixas concentrações e depois encurva..."
- p.9: figura do canal com legenda sobre subunidades em coroa.
- p.11: figura dos 4 gradientes iônicos com legenda forte ("Cada gradiente é uma 'bateria' pronta para gerar trabalho...").
- p.13: figura do ciclo da bomba (3 Na+/2 K+/1 ATP).
- p.14: figura comparativa de famílias de ATPase (P, V).
- p.15: figura do SGLT-1 no enterócito (Trojan).
- p.16: figura do NHE3 no túbulo proximal.

**Veredito de figuras:** todas integradas, todas com legenda mecanística (não decorativa). **Padrão exemplar — para NEBLI absorver.** Porém: distribuição desequilibrada (zero figura entre p.17 e p.38, 55% do documento sem imagem). A seção 3.3 (motor de tudo), a conclusão integradora e o Resumindo poderiam ganhar 2 figuras.

**Densidade visual:** 277 palavras/página em média, ideal NEBLI ~200–240 — está 15–25% acima. Picos de densidade: p.3 (490 pp/pág, intro corrida), p.17 (520 pp/pág, motor de tudo), p.19 (442 pp/pág, conclusão integradora). Vales: p.34 (130 pp/pág, final E2), p.38 (82 pp/pág, gabarito). Distribuição irregular sugere que o autor priorizou conteúdo sobre respiro.

**Uso de cor:** Tier 2 indica banner gold no Resumindo, e as questões E2 têm cores por categoria (Consolidação/Integração/Aplicação) seguindo padrão NEBLI. Boxes clínicos provavelmente em cor distinta dos boxes de "atenção" (a apostila distingue boxes de confusão — "Difusão simples não satura" — de boxes clínicos — "Cólera e SRO" —, e na NEBLI essa distinção tem cor própria). Coerente com padrão.

**Cortes/overflow:** o .txt mostra quebras tipo "f�gado" e "in�meras invagina��es" — são artefatos da extração (encoding), não overflow real do PDF. JSON não indica páginas com 0 palavras nem imagens cortadas. Sem evidência de overflow. Tier 2 deu score 3 em densidade — coerente: legibilidade aceitável, não exemplar.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

Essa é a parte de maior valor para o NEBLI. Italiano (autor histórico) executa 3 movimentos que o REDATOR-E1 atual subutiliza.

### Técnica 1 — Pergunta ingênua "anti-óbvia" antes do conteúdo

**Citação:**
> "Antes de mergulhar em bombas, canais e curvas de saturação, vale parar e perguntar a coisa óbvia que ninguém costuma perguntar: por que precisamos discutir transporte?" (p.3)

E na seção 3.1:
> "Atravessar a favor do gradiente é grátis — termodinamicamente, o sistema está caminhando para o equilíbrio, e a célula só precisa 'abrir a porta'. Mas e quando a célula precisa que o gradiente exista? Quem cria o gradiente em primeiro lugar?" (p.12)

**Nome da técnica:** "pergunta ingênua anti-óbvia" — pergunta que o aluno *não pensou em fazer* porque parecia óbvia demais, e que ao ser feita reorganiza todo o assunto.

**Quando REDATOR-E1 deveria usar:** em toda abertura de PARTE da E1, sempre que houver um pressuposto que o aluno aceita sem questionar. Não confundir com C2 (pergunta motivadora evolutiva) — é mais ingênua e mais próxima do "ué, e por quê?". O exemplar C2.1 ("por que a evolução não fez sinapse elétrica?") é uma versão sofisticada. Italiano traz a versão crua e ela funciona melhor para baseline baixo. **Sugestão:** criar Categoria 2-B em EXEMPLARES.md ("pergunta anti-óbvia / desnaturalização do pressuposto") com este trecho como exemplar.

### Técnica 2 — Frase-síntese sentenciosa fechando o subtópico ("Síntese N —")

**Citação:**
> "Síntese 5 — Bomba é a fonte do gradiente. Quem cobra ATP é a bomba; depois disso, qualquer canal ou transportador a favor do gradiente está, em última análise, vivendo do trabalho que a bomba fez antes. O gradiente de Na+ vai virar a 'moeda corrente' da próxima seção." (p.14)

E:
> "Síntese 7 — A Na/K-ATPase é o paradigma da economia celular: ATP entra, gradientes saem, e os gradientes alimentam tudo o mais. Quando você ouvir 'esse transporte é ativo secundário' em qualquer contexto — intestino, rim, coração, neurônio — pode quase sempre assumir que o ATP que paga essa conta foi gasto na Na/K-ATPase em algum momento anterior." (p.17)

**Nome da técnica:** "síntese sentenciosa numerada + ponte para o próximo subtópico". Combina três funções em uma: (i) consolida o subtópico recém-fechado em 1 frase memorizável, (ii) destaca a consequência mais ampla, (iii) anuncia o próximo subtópico como continuação natural.

**Quando REDATOR-E1 deveria usar:** ao final de cada subseção 1.1, 1.2, etc. da E1. O NEBLI atual usa "Resumindo até aqui:" — mais funcional, menos memorável. A "Síntese N —" do Italiano é mais autoral e mais ancoradora. **Sugestão:** introduzir helper Typst `#sintese(numero, [texto])` no template e atualizar regra do REDATOR para 1 síntese por subseção (≥ 6 por E1). Combinar com "Resumindo até aqui:" não — substituir.

### Técnica 3 — Box clínico narrativo encadeando mecanismo até cadeia farmacológica

**Citação (box "Digoxina e a Na/K-ATPase", p.13):**
> "A digoxina é um inibidor reversível da Na/K-ATPase. Ela se liga ao sítio extracelular da bomba e a bloqueia parcialmente. O resultado: o Na+ intracelular sobe um pouco. E daí o que acontece é interessante — o miocárdio tem um trocador Na/Ca (antiporte secundário, que veremos em 3.2) que normalmente joga Ca² para fora usando a entrada de Na+. Com mais Na+ intracelular, o gradiente de Na+ cai, o trocador trabalha menos, e o Ca² intracelular sobe. Mais cálcio nos cardiomiócitos = contração mais forte. É assim que um inibidor de bomba se torna um inotrópico positivo — clássica conexão entre transporte ativo primário e secundário."

E (box "Cólera e SRO", p.16):
> "A toxina da cólera trava aberta uma proteína G que estimula adenilato ciclase... O AMPc abre o canal CFTR... diarreia litros por dia, morte por desidratação em horas. O remédio é uma solução de reidratação oral: glicose 2% + NaCl 0,3%. Por que glicose junto? Porque o SGLT-1 ainda funciona — ele puxa glicose e Na+ juntos para dentro da célula, e a água segue por osmose."

**Nome da técnica:** "box clínico em cadeia mecanística completa, com forward-reference". Cada box clínico não é um aviso lateral — é um mini-resumo de cadeia "fármaco/doença → alvo molecular → 3–5 passos mecanísticos → desfecho clínico", com referência futura a outro subtópico ("que veremos em 3.2").

**Quando REDATOR-E1 deveria usar:** os boxes `.clinica-box` no NEBLI atual estão na Categoria 9 do EXEMPLARES como "aguardando exemplares". Estes dois boxes do Italiano são candidatos imediatos. A regra que sai: box clínico ≥ 6 frases, com mecanismo encadeado em setas explícitas (texto, não diagrama), e referência futura sempre que possível. Boxes mais curtos viram "atenção"; boxes longos com cadeia são "clínica". **Sugestão:** preencher EXEMPLARES C9 com esses dois boxes como exemplares 9.1 e 9.2, e atualizar a regra para 1 box clínico por PARTE da E1 quando houver doença/fármaco canônico.

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro NEBLI | Status no PDF | Evidência |
|---|---|---|---|
| 1 | Paridade de distratoras em E2 Aplicação (Q26–Q30) | **PRESENTE (leve a moderado)** | Q26: correta A ~35 palavras, distratoras B–E entre 15–22 palavras (ratio ~1.6–2.3). Q28: correta D 20 palavras vs A/B/C/E entre 10–14 (ratio ~1.5–2). Q29: razoável (ratio ~1.2). Q30: ok (~1.0). Q27 é CE, paridade não se aplica do mesmo jeito. Padrão: distratoras truncadas em torno de uma palavra-troca, sem mecanismo plausível-mas-errado. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **N/A (formato)** | Apostila usa nota de rodapé numerada (¹GLUT, ²EAP, ³CFTR) — equivalente funcional. Total de 3 notas para 9+ siglas no texto (GLUT, SGLT, NHE3, NCX, SERCA, CFTR, EAP, SRO, AMPA). Abaixo do alvo NEBLI (5–10). |
| 3 | Subagentes Opus customizados falhando | N/A | Apostila histórica, não passa por pipeline atual. |
| 4 | Heredoc atômico ENAMETOOLONG no Windows | N/A | Erro de pipeline. |
| 5 | `questao-ce` tupla `("I", [conteúdo])` | N/A | Erro de template Typst. |
| 6 | Termo-notas abaixo do alvo (6–8) | **AUSENTE no formato exato, mas baixo no equivalente** | Notas de rodapé seriam o equivalente; só 3. Termos que mereceriam termo-nota (movimento browniano, autofosforilação, antiporte, simporte, eletrogênico, potencial de equilíbrio) não foram destacados como tal. |
| 7 | Tema-card com teto E1 errado | N/A | Não há Tema Card. A E1 tem ~18 páginas (p.3–p.18), dentro do teto canônico atual de 22. |

**Síntese:** dos 7 erros, apenas 1 (paridade de distratoras E2 Aplicação) é claramente reproduzido. 1 (termo-notas/footnotes) é uma versão atenuada. Os outros 5 são N/A ao formato. **Para a base de calibração:** mesmo apostilas históricas de qualidade caem no Erro 1 — confirma que essa armadilha não é exclusiva de subagente, é cognitiva do autor humano também. Reforça que a regra "5 distratoras antes da correta" deve ser disciplina rígida.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Reescrever parágrafo "três outras bombas" (p.14)** em 3 sub-blocos visualmente distintos com nome da bomba em negrito, família estrutural (P × V) explícita, e ponte para Q18 e Q23 da E2. Sem isso, 1 STOP é praticamente garantido.
2. **Adicionar frase-paraquedas para Nernst (p.17)** antes de mencionar "-90 mV / potencial de equilíbrio do K+". Texto pronto na § 3 deste relatório.
3. **Redistribuir figuras para a 2ª metade do PDF.** Hoje 9 imagens em p.5–16; zero em p.17–p.38. Adicionar ao menos 1 figura na seção 3.3 (Na/K como motor — esquema integrador) e 1 no Resumindo (mapa visual dos 3 transportes).

### MECANÍSTICO (max 3)
1. **Engordar distratoras de Q26–Q28 Aplicação** com 25–35 palavras de mecanismo plausível-mas-errado (regra canônica NEBLI). Hoje várias têm 10–14. Distratoras truncadas permitem acerto por contagem visual em vez de raciocínio.
2. **Suprimir ou simplificar `v = √(3KT/m)` na p.4.** A fórmula não é usada depois; cobra Boltzmann sem retornar. Versão "raiz de T sobe, raiz de m desce" em prosa basta (reescrita na § 3 acima).
3. **Explicitar a diferença mecanística entre ATPase tipo P (autofosforila) e tipo V (rotor)** em 1 frase quando V-ATPase aparecer (p.14). Hoje a distinção está implícita na legenda de uma figura — para o aluno-alvo, precisa ser explícita no corpo.

### DIDÁTICO (max 3)
1. **Adicionar pergunta ingênua em 2.2 e 2.3** (canais e canal × transportador). Hoje só 2.1, 3.1 e 3.2 abrem com pergunta. Padronizar todas as subseções com a Técnica 1 do T3.9.
2. **Aumentar termos-nota / footnotes** de 3 para 6–8. Candidatos: movimento browniano, autofosforilação, eletrogênico, potencial de equilíbrio, antiporte, simporte. Cada um vale 1 frase no rodapé.
3. **Inserir 1 frase de ponte forward-reference** em todas as Sínteses ("...veremos isso em 3.2"). Hoje só Síntese 5 e 7 têm. Padronizar (Técnica 2 do T3.9).

### ESTÉTICO (max 3)
1. **Reduzir densidade de p.3 (490 pp/pág) e p.17 (520 pp/pág)** quebrando em 2 páginas cada. Ideal NEBLI é 200–240 pp/pág.
2. **Resumindo com 7 cápsulas em vez de 8.** A cápsula "Tudo é combinação dos três" pode virar fecho visual destacado em vez de cápsula 8.
3. **Banner navy / cor de família** para Sínteses numeradas (consistência com Resumindo gold + boxes clínicos coloridos). Hoje sínteses parecem texto comum com numeração.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM.** Esta apostila é fonte primária de 3 técnicas para Phase F (pergunta anti-óbvia, síntese sentenciosa numerada, box clínico em cadeia mecanística). É o melhor exemplar disponível para `clinica-box` no EXEMPLARES.md. Deve entrar como referência viva.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM** — 3 ESTRUTURAIS e 3 MECANÍSTICAS recomendadas acima. Não bloqueiam aprovação como referência, mas se este resumo fosse refeito hoje pelo pipeline NEBLI, deveriam ser endereçadas.
3. **Seção para refazer?** **3.1 final (parágrafo "três outras bombas" em p.14)** — reescrita pronta no § 3.
4. **Parágrafos para reescrever?** **3 parágrafos:** (i) "três outras bombas" (p.14), (ii) fórmula `v = √(3KT/m)` em 1.2 (p.4), (iii) introdução implícita de potencial de equilíbrio em 3.3 (p.17). Reescritas prontas no § 3.

**Para Phase F (alimenta REDATOR-E1):**
- Técnica 1 → criar categoria 2-B em EXEMPLARES.md.
- Técnica 2 → introduzir helper `#sintese(N, [texto])` no template e regra "1 síntese sentenciosa por subseção".
- Técnica 3 → preencher C9 (`.clinica-box`) de EXEMPLARES.md com box-digoxina e box-cólera como exemplares 9.1 e 9.2.

---

[APROVAR COM RESERVAS]

---

FIM-DA-REVISAO-PROFUNDA
