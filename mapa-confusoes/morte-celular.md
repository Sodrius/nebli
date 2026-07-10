# Mapa de Confusões — MORTE CELULAR (biocel-08)

Atualizado 2026-05-28 — reescrita do zero. Banco NEBLI sem questões classificadas para esta aula; confusões derivam dos slides + Alberts 3ª ed. cap. 18 + Junqueira & Carneiro 10ª ed. + armadilhas clínicas conhecidas (oncologia e neurodegeneração).

Formato: **nome curto · mecanismo do erro · correção mecanística · origem**.

---

## PARTE I — Por que a célula morre por ordem

### 1.1 Sinais extracelulares que sustentam a vida

1. **"A célula vive sozinha enquanto tiver nutriente."**
   - Erro: aluno trata a célula animal como organismo unicelular autossuficiente — bastaria glicose e oxigênio para sobreviver.
   - Correção: célula animal é viciada em comunicação. Mesmo com nutrientes em abundância, ela entra em apoptose se faltarem *fatores de sobrevivência* (proteínas secretadas por vizinhas, sinalizando "fique viva"). O default é morrer.
   - Origem: Alberts 3ª ed. cap. 18 — princípio fundamental, foco do slide 9.

2. **"Mitógeno = fator de crescimento."**
   - Erro: aluno usa os termos como sinônimo.
   - Correção: mitógeno estimula *divisão* (passa G1→S vencendo freios). Fator de crescimento estimula *aumento de massa* (síntese de proteína, crescimento sem necessariamente dividir). Fator de sobrevivência *impede apoptose*. Algumas moléculas (PDGF) fazem mais de um.
   - Origem: slides 4–9.

3. **"Sem sinal de sobrevivência a célula vira necrótica."**
   - Erro: associa qualquer falta de input externo com colapso bagunçado.
   - Correção: sem sinal de sobrevivência ela vai para *apoptose* — programa silencioso, ordenado, sem inflamação. Necrose é outra coisa: lise descontrolada por trauma, isquemia ou ativação de via necroptótica específica.
   - Origem: Junqueira 10ª ed. cap. 5.

4. **"Fator de sobrevivência atua dentro da célula."**
   - Erro: aluno pensa em algo intracelular tipo "antioxidante endógeno".
   - Correção: é extracelular. Ligante secretado por células vizinhas que se liga a receptor de superfície, dispara via de sinalização (PI3K-Akt, p.ex.), e essa via *suprime* o programa apoptótico que estava engatilhado.
   - Origem: Alberts 3ª ed. cap. 18.

### 1.2 Morte programada vs acidental

5. **"PCD significa só apoptose."**
   - Erro: aluno aprendeu antiga sinonímia PCD ≡ apoptose.
   - Correção: hoje PCD ou RCD são guarda-chuvas. Apoptose é o tipo 1 (clássico, mais estudado), autofagia em contexto de morte é o tipo 2, necrose regulada (necroptose/piroptose/ferroptose) é o tipo 3.
   - Origem: slide 15 explícito sobre a mudança de nomenclatura.

6. **"Morte sem extravasamento = morte sem inflamação."**
   - Erro: o aluno acerta que apoptose tardia eventualmente lisa, então conclui que ela inflama "no fim".
   - Correção: na prática, a apoptótica é *fagocitada* antes de extravasar. A fosfatidilserina exposta convoca o macrófago em segundos. Em laboratório (sem fagócito), a apoptótica vai a apoptose tardia e lisa — *in vivo*, raramente chega a esse ponto.
   - Origem: slide 23 + 27 + 36.

7. **"Necrose sempre é acidental."**
   - Erro: dicotomia rígida apoptose-programada × necrose-acidental.
   - Correção: necroptose é necrose *molecularmente programada* via RIPK1/RIPK3/MLKL. Morfologicamente é necrose (inchaço, lise), mecanisticamente é regulada. Morfologia ≠ mecanismo.
   - Origem: Alberts 5ª ed. cap. 18 + slide 75.

### 1.3 Os três tipos canônicos

8. **"Autofagia é um tipo de morte celular."**
   - Erro: já que entra na lista dos tipos, deve ser mecanismo de morte.
   - Correção: autofagia é primariamente *sobrevivência* (reciclagem em jejum, controle de qualidade). Vira morte só em contexto restrito — *autosis* — quando exacerbada. A maioria das células com vacúolos autofágicos visíveis está se mantendo viva, não morrendo.
   - Origem: slide 66, 70.

---

## PARTE II — Apoptose: o suicídio silencioso

### 2.1 Morfologia e sinal eat-me

9. **"Fosfatidilserina sempre está exposta na superfície externa."**
   - Erro: aluno trata PS como qualquer fosfolipídio simétrico.
   - Correção: em célula viva, PS fica restrita à monocamada *citosólica* por flipase ATP-dependente. Externalização exige *dois* eventos coordenados: inativação da flipase + ativação da scramblase (que mistura as monocamadas). Sem ATP, a flipase para — necrose tardia também expõe PS, mas por outro caminho.
   - Origem: slide 34, 35.

10. **"Anexina V positivo = célula morta."**
    - Erro: confunde apoptose precoce com morte completa.
    - Correção: Anexina V+ / PI− = apoptose inicial (PS exposta, membrana ainda íntegra). Anexina V+ / PI+ = apoptose tardia ou necrose (membrana já permeável). A diferença é se o PI consegue entrar e marcar o DNA.
    - Origem: slide 37.

### 2.2 Cascata de caspases

11. **"Toda caspase ativa = célula morta."**
    - Erro: simplifica caspase a "tesoura da apoptose".
    - Correção: hierarquia clara. Iniciadoras (8, 9, 10) ativadas por agregação em plataformas (DISC ou apoptossomo) clivam pró-executoras. Executoras (3, 6, 7) cortam centenas de substratos celulares — *aí* a célula morre. Caspases inflamatórias (1, 4, 5, 11) fazem piroptose, não apoptose.
    - Origem: slides 39–43.

12. **"Pro-caspase é caspase inativa por causa de fosforilação."**
    - Erro: assume regulação por fosforilação como nas quinases.
    - Correção: pro-caspase tem prodomínio bloqueando o sítio. Ativação se dá por *clivagem proteolítica* (remoção do prodomínio + corte entre subunidades grande e pequena), não por fosforilação. O mecanismo de cascata existe porque uma caspase ativa cliva a próxima pro-caspase.
    - Origem: slide 41 + Alberts 5ª ed.

### 2.3 Via extrínseca

13. **"FasL e Fas estão na mesma célula."**
    - Erro: confunde a estrutura cis com a interação trans.
    - Correção: FasL fica na membrana de uma célula efetora (linfócito T citotóxico, NK), Fas fica na membrana da célula-alvo. A morte por via extrínseca é *intercelular* — uma célula manda a outra morrer.
    - Origem: slide 44.

14. **"Receptor armadilha aumenta a sinalização."**
    - Erro: assume que mais receptor = mais sinal.
    - Correção: receptor armadilha (decoy) tem o domínio externo que liga o ligante mas falta o domínio de morte intracelular. Funciona como *esponja*: sequestra ligante sem disparar via. Mecanismo de modulação fisiológica e de escape tumoral.
    - Origem: slide 45.

### 2.4 Via intrínseca

15. **"Bcl-2 é pró-apoptótico."** ← inversão canônica.
    - Erro: aluno deduz "Bcl-2 — apoptose — provoca apoptose".
    - Correção: Bcl-2 é *anti-apoptótico*. Sequestra BH3-only e impede Bax/Bak de oligomerizar na membrana mitocondrial externa. Foi descoberto como oncogene super-expresso no linfoma folicular B (translocação t(14;18) joga o gene sob promotor de IgH). Família Bcl-2 tem membros pró e anti — a proteína Bcl-2 nominal é anti.
    - Origem: slides 48–50 + clínica oncológica clássica. → **`#confusao-prevista` recomendada**.

16. **"Citocromo c sempre induz apoptose."**
    - Erro: aluno conhece cyt c só como sinal de apoptose.
    - Correção: cyt c *dentro* da mitocôndria carrega elétrons na cadeia respiratória (Complexo III → IV) — função vital. Só vira sinal de morte quando escapa para o citosol via MOMP e se liga a Apaf-1. Mesma molécula, dois compartimentos, dois destinos.
    - Origem: conexão com aula de cadeia respiratória.

17. **"MOMP é abertura do mPTP."**
    - Erro: confunde permeabilização da membrana externa com poro de transição mitocondrial.
    - Correção: MOMP é a formação de poro feito por Bax/Bak oligomerizados na *membrana externa* — libera cyt c e Smac. O mPTP (poro de transição) é outra estrutura, na membrana interna, ligado a necrose por sobrecarga de Ca²⁺. São fenômenos distintos.
    - Origem: Alberts 5ª ed.

### 2.5 Regulação fina e cross-talk

18. **"Anti-IAP libera tudo de uma vez."**
    - Erro: imagina que Smac/Diablo sai e a célula morre instantaneamente.
    - Correção: Smac/Diablo sai junto com cyt c via MOMP, inibe XIAP/IAPs e libera caspases 3/7/9. Mas a célula tem *redundância* anti-apoptótica em múltiplas camadas (Bcl-2, IAPs, c-FLIP). A decisão é por *razão* entre todas, não gatilho único.
    - Origem: slides 57, 58.

19. **"Vias extrínseca e intrínseca são independentes."**
    - Erro: trata como dois pipelines paralelos sem comunicação.
    - Correção: amplificação cruzada via tBid. Caspase 8 (extrínseca) cliva Bid → tBid migra para a mitocôndria → ativa Bax/Bak → MOMP. Em células tipo II (hepatócitos), a via extrínseca *depende* dessa amplificação para gerar caspase 3 suficiente. Em tipo I (linfócitos), caspase 8 direta basta.
    - Origem: slides 52, 53.

---

## PARTE III — Autofagia e necrose regulada

### 3.1 Autofagia

20. **"Autofagossomo é vesícula de membrana simples."**
    - Erro: aluno assume estrutura típica de vesícula de transporte.
    - Correção: autofagossomo é vesícula de membrana *dupla* (nasce do fagóforo que enrola sobre si mesmo). A dupla membrana é o que permite identificá-lo na microscopia eletrônica e diferenciá-lo de endossoma ou lisossoma.
    - Origem: slides 65, 67.

21. **"LC3 = atividade autofágica."**
    - Erro: ver LC3 marcada = autofagia rodando.
    - Correção: LC3 ancorada na membrana do autofagossomo é marcador *estrutural*. Para saber se a autofagia está rodando bem, mede-se *fluxo* (turnover do LC3-II com inibidor de lisossomo). Estoque alto de LC3-II pode ser autofagia ativa ou autofagia bloqueada na etapa de degradação.
    - Origem: slide 67 (monitoramento).

### 3.2 Necroptose

22. **"Necroptose é necrose comum."**
    - Erro: pelo nome e pela morfologia, parece sinônimo de necrose acidental.
    - Correção: necroptose é necrose *programada* — depende de RIPK1 + RIPK3 (necrossomo) → fosforilação de MLKL → MLKL forma poros na membrana → lise. Ocorre quando caspase 8 está inibida (vírus que bloqueia caspase para evitar apoptose, p.ex.) — *necessita* que a apoptose esteja bloqueada para acontecer.
    - Origem: slides 75–77.

23. **"Necroptose acontece em paralelo com apoptose."**
    - Erro: dois caminhos simultâneos para o mesmo estímulo.
    - Correção: caspase 8 ativa cliva RIPK1/RIPK3 e bloqueia necroptose. Logo, em célula competente para apoptose, necroptose não roda. Necroptose só aparece quando a apoptose foi sabotada — é via de backup contra patógenos que aprenderam a desligar apoptose.
    - Origem: slide 77.

### 3.3 Piroptose

24. **"Piroptose e necroptose são a mesma coisa porque ambas fazem poro."**
    - Erro: junta pelas semelhanças morfológicas (lise + inflamação).
    - Correção: mecanismos distintos. Necroptose usa MLKL fosforilado por RIPK3 (poro inespecífico, lise osmótica). Piroptose usa gasdermina-D clivada por caspase 1 (poro específico que libera IL-1β e IL-18 maduras *antes* da lise — o ponto pedagógico é que a célula chama o sistema imune antes de morrer).
    - Origem: slides 85 + Alberts 5ª ed.

25. **"Caspase 1 faz apoptose."**
    - Erro: caspase com número pequeno = caspase iniciadora apoptótica.
    - Correção: caspase 1 é *inflamatória* — clivada por inflamassomas (NLRP3, AIM2 etc.) faz piroptose. Junto com caspases 4, 5 e 11 forma o subgrupo inflamatório. Caspases iniciadoras *de apoptose* são 8, 9, 10.
    - Origem: slide 43 (distinção visível na figura) + slide 85.

### 3.4 Necrose acidental e ferroptose

26. **"Toda necrose libera DAMPs e inflama igual."**
    - Erro: trata necrose como bloco único.
    - Correção: necrose acidental por isquemia libera HMGB1, ATP, ácido úrico, DNA mitocondrial — inflamação intensa. Apoptose silencia *via* PS exposta + inibição de citocinas no macrófago. Necroptose e piroptose ficam no meio — liberam conteúdo, mas a piroptose o faz com IL-1β/IL-18 *deliberadamente* madura para alertar.
    - Origem: slide 78 + Alberts 5ª ed.

27. **"Ferroptose é deficiência de ferro."**
    - Erro: lê pelo nome ao contrário.
    - Correção: ferroptose é morte *dependente* de ferro — ferro livre catalisa peroxidação lipídica via reação de Fenton. GPX4 normalmente neutraliza os peróxidos lipídicos; quando GPX4 falha (ou cisteína falta), peroxidação dispara e a membrana desfaz. Relevante em isquemia, neurodegeneração e câncer resistente a quimioterapia.
    - Origem: slide 85.

28. **"Necrose sempre é patológica."**
    - Erro: dicotomia patologia × fisiologia, com necrose só no patológico.
    - Correção: alguns processos fisiológicos *dependem* de necrose programada — renovação de células do epitélio intestinal, maturação folicular durante organogênese, contração da memória de linfócitos T pós-infecção. A regulação fisiológica vs patológica é por contexto e magnitude, não por presença/ausência de necrose.
    - Origem: slide 81.

---

**Conexões transversais (sementes de Integração para a E2)**

- **Apoptose × cadeia respiratória:** cyt c carregando elétrons vs cyt c sinalizando morte. Mesma proteína, dois compartimentos.
- **Apoptose × ciclo celular:** p53 mutado → falha em ativar BH3-only (Puma, Noxa) → célula com DNA danificado não morre → câncer.
- **Bcl-2 × oncogênese:** linfoma folicular B com t(14;18) e BH3-miméticos (venetoclax) como terapia.
- **Necroptose × imunologia viral:** vírus que bloqueia caspase 8 (CMV vICA) provoca necroptose como backup antiviral.
- **Piroptose × imunidade inata:** inflamassoma NLRP3 sensora de PAMPs/DAMPs → caspase 1 → IL-1β; *Salmonella*, *Listeria* como gatilhos clássicos.
- **Autofagia × jejum e mTOR:** mTOR inibido em jejum → autofagia liberada → célula recicla para sobreviver.
- **Fosfatidilserina × biofísica de membrana:** assimetria mantida por ATP; perda de ATP (isquemia) também expõe PS — sinal pode ser ambíguo.
