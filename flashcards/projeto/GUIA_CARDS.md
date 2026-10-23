# GUIA_CARDS — como Davi quer os cards

Gerado por `python3 -m nebli.exemplares` (F-20261023-CLAUDE-02/03). **Ler inteiro antes de escrever qualquer card** (gate `exemplares_lidos`): achar os casos parecidos, moldar o autoral num EXEMPLAR específico e conferir contra o ANTI-EXEMPLAR do mesmo erro. Nada aqui é escrito à mão: exemplares são os cards com X de Davi; anti-exemplares, os cards que ele comentou; as análises vêm de `exemplares_analise.py`.

## Os dois erros principais (Davi, 23/10)

1. **Deck que não entende a aula**: não seguir o passo a passo (compreender o que a aula ensina, bloco a bloco do slide, antes de buscar) e encher de conteúdo lateral. Gate `passo_a_passo`.
2. **Autoral de baixa qualidade**: cloze no lugar errado, sem negrito, sem porquê, frase estranha, fato solto sem processo. Custo-efetividade bom = um card carrega algo importante, de forma compreensível, a longo prazo, entendendo e relembrando bem um processo.

## Análise geral: o que aprender destes casos

Cada anti-exemplar abaixo pertence a uma família de erro; a lista diz o que fazer e quantas vezes Davi apontou o erro. Os exemplares mostram o certo: modelo de função + consequência (azol, HDAC), contraste no mesmo índice com dica (inata/adaptativa, ecto/endotrix), organizador em pé com índices deliberados (tolerância periférica, falhas do sistema imune), verso com o porquê (CTLA-4, GLUT-2) e figura que ensina o que o card cobra.

- **imagem** (86 casos): Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).
- **estranho** (39 casos): Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.
- **negrito** (28 casos): Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).
- **porque** (26 casos): Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.
- **elogio** (22 casos): Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).
- **cloze_local** (19 casos): Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.
- **organizador** (18 casos): Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).
- **cloze_longo** (14 casos): Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.
- **aula** (14 casos): Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.
- **io** (13 casos): Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.
- **tab** (9 casos): Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.
- **dica** (7 casos): Falta dica no cloze quando a pergunta é ambígua (parte do duodeno, fase, ramo de qual artéria). Dica curta no próprio cloze, sem entregar.
- **repetido** (5 casos): Card repetido ou muito parecido com outro: confunde e gasta revisão. Um fato, um card; o outro aspecto vai no verso ou em card com ganho próprio.
- **sigla** (4 casos): Sigla sozinha no card ou no cloze. Escrever o nome por extenso com a sigla junto; card tem de fazer sentido sozinho.
- **cobertura** (3 casos): Deck incompleto ou com repetição no conjunto: faltou cobrir o que a aula/quiz ensina ou sobrou o mesmo fato várias vezes. Planejar a cobertura pelo slide antes de escolher cards (pipeline v7).
- **cor** (2 casos): Cor errada para a importância (HY rosa, detalhe verde). A cor segue a rubrica: HY 1–2 e pilares verdes, detalhe rosa.
- **etimologia** (0 casos): Card de etimologia (prefixo, sufixo, radical): termo vago ou impreciso ('x ou y', definição errada, avançado sem explicação). Lição geral: uma palavra no cloze, definição exata e comparação quando ajuda a reter.
- **outro** (0 casos): Comentário pontual de Davi; ler o literal e aplicar a correção específica.

## Exemplares (X de Davi)

### Exemplar · note 1791557942606 (2026-uc03-microbiologia-43-biologia-fungos; X em 2026-10-17)
- **Card:** Azoles inhibit the conversion of {{c1::lanosterol}} to {{c1::ergosterol}}
- **Verso:** [IMG 1208651b2b9faf1a6523a710eff3180c.jpg] / / - Less ergosterol, leaky membrane, growth stops
- **Análise:** Função + consequência num card só: azol bloqueia lanosterol→ergosterol e o verso diz o efeito (membrana vaza, fungo para). Custo-efetividade alta: um card carrega o mecanismo de uma classe inteira. Usar para todo alvo de fármaco/enzima: passo bloqueado no cloze, efeito no verso.

### Exemplar · note 1792166970014 (2026-uc03-imunologia-51-disturbios-sistema-imune; X em 2026-10-17)
- **Card:** Autoimmune diseases come from {{c1::adaptive::innate/adaptive}} immunity, and autoinflammatory diseases from {{c1::innate::innate/adaptive}} immunity
- **Verso:** - Autoimmunity has a self antigen, autoantibodies and autoreactive T cells / - Autoinflammation has none of them: the inflammasome or cytokine brakes fail
- **Análise:** Contraste complementar no mesmo índice com dica innate/adaptive: um lado não entrega o outro e o par organiza um grupo inteiro de doenças. Verso explica o critério (antígeno próprio × freio da inflamação). Modelo para todo par confundível.

### Exemplar · note 1791625434983 (2026-uc03-imunologia-45-ativacao-linfocitos-t; X em 2026-10-17)
- **Card:** Tregs constitutively express {{c1::CTLA-4}}, which strips B7 from antigen-presenting cells
- **Verso:** - Without B7, APCs cannot activate effector T cells
- **Análise:** Fato decorável (CTLA-4) dentro de um mecanismo (retira B7 da APC) e verso com a consequência (sem B7, não ativa efetora). Curto, uma lacuna, nome específico. Modelo de molécula + o que ela faz + por que importa.

### Exemplar · note 1791023354943 (2026-uc08-biologia-tecidual-03-estrutura-estomago; X em 2026-10-17)
- **Card:** About two-thirds of all saliva comes from the {{c1::submandibular}} glands
- **Verso:** - Mixed gland, mostly serous / / [IMG 392281736e881dcc1c4cfebdbd375f80.jpg]
- **Comentário de Davi (2026-10-13):** “imagem zuada em vários cards, vou pagar de avisar”
- **Análise:** Número que se decora (dois terços da saliva) com contexto mínimo e figura que mostra a glândula; verso acrescenta o tipo de secreção. Modelo de card de 'qual é o principal X' com ganho visual.

### Exemplar · note 1791575024195 (2026-uc08-fisiologia-09-motilidade-ii; X em 2026-10-17)
- **Card:** A slow wave that reaches only the {{c1::contractile}} threshold, with no spike potentials, still causes a weak contraction
- **Verso:** - Contractile threshold: small Ca²⁺ rise, weak contraction / - Electrical threshold: spikes bring more Ca²⁺, strong contraction / / [IMG nebli-uc08-fi09-p03f.png]
- **Análise:** Explica um limiar (contrátil × elétrico) cobrando a palavra que distingue os dois; verso põe os dois lados lado a lado com a figura. Modelo de card de fisiologia que ensina o processo e não só o nome.

### Exemplar · note 1790979869860 (2026-uc03-bioquimica-16-regulacao-hormonal-massa-corporea; X em 2026-10-17)
- **Card:** Ghrelin is secreted by gastric cells and acts to {{c1::increase}} appetite
- **Verso:** - Rises before meals and falls after eating
- **Análise:** Simples e útil: hormônio → efeito (aumenta o apetite) e verso com o quando (sobe antes das refeições). Prova que card básico bem escrito tem lugar.

### Exemplar · note 1791762418274 (2026-uc19-farmacologia-01-introducao-mecanismos; X em 2026-10-17)
- **Card:** Vmax of a drug is indicative of {{c1::efficacy::potency or efficacy}}
- **Verso:** Directly related (efficacious drugs have high Vmax) / [IMG caa30be6e81384f2dbcbfc23e338d1c0.webp] / / [IMG c5f7510919d6ed56a5e37d7e87d1ded9.webp] /
- **Análise:** Pergunta curta com dica 'potency or efficacy' que desfaz a ambiguidade e figura das curvas no verso. Modelo de conceito de gráfico: cobrar a leitura, mostrar o gráfico atrás.

### Exemplar · note 1791630904844 (2026-uc03-microbiologia-50-micoses-sistemicas; X em 2026-10-17)
- **Card:** The yeast wall of Paracoccidioides is rich in {{c1::α-glucan::α-glucan or β-glucan}}, whereas the mold wall has mostly {{c1::β-glucan::α-glucan or β-glucan}}
- **Verso:** - α-glucan is the outer layer that resists phagocyte β-glucanase
- **Análise:** Contraste levedura × bolor no mesmo índice, com dica, e verso com o porquê funcional (α-glucano resiste à glucanase). Modelo de diferença estrutural ligada à virulência.

### Exemplar · note 1791630906493 (2026-uc03-microbiologia-50-micoses-sistemicas; X em 2026-10-17)
- **Card:** Chronic {{c1::Histoplasmosis::fungal infection}} can look similar to {{c2::tuberculosis (TB)}}, with cavitary lesions in the upper lobes of the lungs and {{c2::calcified}} nodules with fibrotic scarring
- **Verso:** - In general, systemic fungi are asymptomatic / / - Severe infections (for instance, those in immunocompromised patients) result in major symptoms / / - Calcifications common in the hilar regions
- **Análise:** AnKing clínico curto que liga a doença a um par confundível (TB) com os achados que se cobram; verso traz o quadro geral. Mostra quando clínica vale: quando ensina a distinguir.

### Exemplar · note 1792166970767 (2026-uc03-imunologia-51-disturbios-sistema-imune; X em 2026-10-17)
- **Card:** Peripheral tolerance of mature T cells: / 1. {{c1::Anergy::A…}} (antigen without costimulation) / 2. Suppression by {{c1::regulatory T::r…}} cells / 3. {{c1::Deletion::D…}} by apoptosis
- **Verso:** - Each mechanism has a single-gene disease when it fails: FOXP3 (IPEX) for Treg, FAS (ALPS) for deletion
- **Análise:** Organizador em pé, três mecanismos com dica da 1ª letra no mesmo índice e verso que liga cada mecanismo à doença monogênica. Modelo de organizador: conjunto + critério + consequência.

### Exemplar · note 1792166971544 (2026-uc03-imunologia-51-disturbios-sistema-imune; X em 2026-10-17)
- **Card:** The PD1 receptor is normally involved in the maintenance of {{c1::peripheral}} immunologic tolerance
- **Verso:** This "checkpoint" system is another line of defense against autoreactive immune cells that have escaped central tolerance / [IMG 836cf8aa3fa2d15146315deb6d782cfe.jpg]
- **Análise:** AnKing: função (tolerância periférica) de uma molécula com o verso situando no sistema (checkpoint além da tolerância central). Modelo de 'para que serve' com contexto.

### Exemplar · note 1792166978741 (2026-uc03-imunologia-51-disturbios-sistema-imune; X em 2026-10-17)
- **Card:** {{c1::B}}-cell deficiencies cause recurrent bacterial infections / {{c1::T}}-cell deficiencies produce fungal and viral infections
- **Verso:** B-cell deficiency = Bacterial
- **Análise:** Dois clozes paralelos (B → bacterianas, T → fungos e vírus) num índice só e mnemônico curto no verso. Alto custo-efetividade: uma regra que resolve muitas questões.

### Exemplar · note 1792166976595 (2026-uc03-imunologia-51-disturbios-sistema-imune; X em 2026-10-18)
- **Card:** {{c2::Myasthenia gravis}} is caused by autoantibodies to {{c1::post}}synaptic {{c1::ACh receptors}} at the NMJ
- **Verso:** - Importantly, these antibodies (IgM and/or IgG) block activation resulting in a reduced number of functional acetylcholine receptors at the neuromuscular junction / / - This results in a decreased end plate potential (not allowing muscle cells to depolarize) since there are fewer postsynaptic cation channels that can now open in response to acetylcholine / / [IMG 102dfc79376f17f2912bfab257713d25.
- **Análise:** Doença + alvo do anticorpo com o mecanismo inteiro no verso (bloqueio do receptor → menor potencial de placa). Mostra que o verso pode aprofundar o processo sem pesar a frente.

### Exemplar · note 1791575690369 (2026-uc03-microbiologia-43-biologia-fungos; X em 2026-10-18)
- **Card:** Yeasts reproduce asexually mainly by {{c1::budding}}, which gives unequal cells, whereas {{c1::binary fission}} gives two equal cells
- **Verso:** - The bud is a blastoconidium / / [IMG nebli-trabulsi-fig-64-1-4.png]
- **Análise:** Contraste brotamento × fissão binária cobrando os nomes e verso com o termo técnico (blastoconídio) e figura. Modelo de comparação morfológica com imagem que ensina.

### Exemplar · note 1790981523773 (2026-uc08-anatomia-07-vascularizacao-visceras; X em 2026-10-18)
- **Card:** 
- **Análise:** Oclusão de imagem bem feita (estrutura destacada, nome escondido). Modelo para anatomia: a figura é o card, o nome é a resposta.

### Exemplar · note 1790999270833 (2026-uc08-fisiologia-08-motilidade-i; X em 2026-10-18)
- **Card:** {{c1::Phasic}} contractions of GI smooth muscle are periodic contractions followed by relaxation
- **Verso:** Occur in the esophagus, gastric antrum, small intestine
- **Análise:** Definição curta com o termo no cloze e verso que diz onde ocorre. Modelo de definição útil (não abstrata).

### Exemplar · note 1792261811401 (2026-uc07-telencefalo-e-cortex-cerebral-homunculo-motor-e-sensitivo; X em 2026-10-18)
- **Card:** O giro {{c1::pós}}-central é a área {{c2::somestésica}} primária (lobo parietal)
- **Verso:** - Área somestésica: relativa à sensibilidade somática (tato, dor, temperatura e propriocepção); corresponde ao córtex somatossensitivo primário (áreas 3, 1 e 2 de Brodmann). / / [IMG e471a62e6fae4d390299a1d3bc903a36.png]
- **Comentário de Davi (2026-10-22):** “num card assim, pode ter no comentário alguma informação dessa área, tipo o que é somestésica”
- **Análise:** Duas lacunas complementares (giro e área) num card de localização; comentário de Davi pede que o verso explique o termo (somestésica). Usar: em card de área/estrutura, verso diz o que o nome significa.

### Exemplar · note 1790981516405 (2026-uc08-anatomia-07-vascularizacao-visceras; X em 2026-10-18)
- **Card:** The {{c1::gastroduodenal}} artery gives rise to the anterior superior and posterior superior pancreaticoduodenal arteries
- **Verso:** [IMG deea37ee076e159f96e016d0c783feec.png][IMG 043269e64d3dbcc7dea3b1d2af443703.jpg] / / Superior pancreaticoduodenals (celiac) meet the inferior ones (SMA) around the pancreatic head
- **Análise:** Ramo arterial com o que ele origina e verso que fecha a anastomose (superior × inferior). Modelo de anatomia relacional: um vaso, seus ramos, e a ligação com o próximo.

### Exemplar · note 1792328931894 (?; X em 2026-10-18)
- **Card:** A {{c1::fissura mediana anterior}} é um sulco profundo que divide incompletamente a medula em metades simétricas
- **Verso:** [IMG kh-anterior-median-fissure-of-medulla.jpg]
- **Análise:** Estrutura do Kenhub com nome em português e figura destacada; frase curta com a função anatômica (divide a medula). Modelo de card de estrutura que ensina o que ela é.

### Exemplar · note 1791629593673 (2026-uc03-imunologia-49-ativacao-celulas-b; X em 2026-10-18)
- **Card:** {{c2::Hyper-IgM}} syndrome is most commonly due to mutated {{c1::CD40L}} on Th cells
- **Verso:** Class-switching defect / / [IMG 8246e29ed402d1087af107a0c864d6c1.webp]
- **Análise:** Doença + defeito molecular (CD40L) e verso com a consequência (falha da troca de classe). Duas lacunas que se apoiam. Modelo de defeito → mecanismo → nome.

### Exemplar · note 1792330247661 (?; X em 2026-10-18)
- **Card:** O cerebelo fica abaixo do cérebro, inferior ao lobo {{c1::occipital}}
- **Verso:** [IMG kh-cerebellum.jpg]
- **Análise:** Localização com uma referência fácil (abaixo do cérebro, inferior ao occipital) e figura. Card simples de orientação espacial.

### Exemplar · note 1791625424957 (2026-uc03-imunologia-20-mhc-apresentacao; X em 2026-10-19)
- **Card:** What protein is associated with MHC I? / {{c1::β2-microglobulin}}
- **Verso:** Whereas MHC II is associated with invariant chain / / [IMG 6e345c353d9e220d52029fd44fc589eb.png]
- **Análise:** Pergunta direta (que proteína se associa ao MHC I) e verso com o contraste (MHC II → cadeia invariante). Modelo: uma pergunta + o par no verso.

### Exemplar · note 1791716422184 (2026-uc03-grand-round-03-espondilodiscite-tuberculosa; X em 2026-10-19)
- **Card:** Which cytokine is responsible for maintaining granulomas in TB infection? / / {{c1::TNF-α (from macrophages)}}
- **Verso:** While IFN-y stimulates macrophages to kill phagocytosed pathogens / / [IMG 1eb2af7eda99066b2127c844e70c54f0.webp]
- **Análise:** Citocina responsável pela manutenção do granuloma com o contraste no verso (IFN-γ ativa, TNF mantém). Modelo de 'quem faz o quê' com o par confundível explicado.

### Exemplar · note 1791625430208 (2026-uc03-imunologia-22-mecanismos-efetores; X em 2026-10-19)
- **Card:** Which cytokine is primarily responsible for stimulating monocytes / macrophages to kill the microbes they ingest (macrophage-lymphocyte interaction)? / / {{c1::IFN-γ}}
- **Verso:** IFN-γ also inhibits differentiation into Th2 cells / [IMG 60704af48c483fd79792cca0f3460146.jpg][IMG paste-cb59b7ccab181ae788f4de3f994ee4bff549d7d1.jpg] /
- **Análise:** Pergunta funcional com a resposta específica (IFN-γ) e verso com o efeito adicional (inibe Th2). Bom custo-efetividade: um card, dois fatos ligados.

### Exemplar · note 1791983679330 (2026-uc03-patologia-62-inflamacao-cronica; X em 2026-10-20)
- **Card:** The characteristic triad of chronic inflammation is: / 1. {{c2::scarring}} / 2. {{c1::mononuclear infiltrate}} / 3. {{c2::tissue destruction}}
- **Comentário de Davi (2026-10-22):** “gostei desse, mas poderia estar em inglês”
- **Análise:** Tríade em tópicos com índices escolhidos (o núcleo c1, os outros c2). Modelo de organizador de tríade: em pé, nomes curtos.

### Exemplar · note 1791631345241 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii; X em 2026-10-20)
- **Card:** At the yeast HO gene, Swi5 first opens chromatin, allowing the second activator {{c1::SBF}} to bind
- **Verso:** This is sequential recruitment: Swi5 recruits a remodeler and a HAT; only after chromatin opens can SBF recruit the transcription machinery.
- **Comentário de Davi (2026-10-22):** “imagem aqui, decoro o nome de algo, mas o card falta storytelling”
- **Análise:** Recrutamento sequencial (Swi5 abre, SBF entra) cobrando o segundo ativador; verso explica a ordem e por quê. Davi pediu imagem e storytelling: usar com figura e ligado ao princípio que ilustra.

### Exemplar · note 1791762416971 (2026-uc19-farmacologia-01-introducao-mecanismos; X em 2026-10-20)
- **Card:** Benzodiazepines exert their effects via binding to an allosteric site on the {{c1::GABAA}} receptor /
- **Verso:** [IMG 911639beb5d525b2c181e5a04444613d.webp] / / - BZDs need GABA present; they do not open the channel alone
- **Análise:** Fármaco → sítio de ligação, com o porquê no verso (BZD precisa de GABA). Modelo de farmacologia por mecanismo, não por lista.

### Exemplar · note 1791631347092 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii; X em 2026-10-20)
- **Card:** After replication, a {{c1::maintenance DNA methyltransferase}} copies methylation onto the new strand
- **Verso:** - It recognizes hemimethylated CpG
- **Comentário de Davi (2026-10-22):** “comentário zuado veja como melhorei o cloze, entenda o padrçao e coloca nos exemplares”
- **Análise:** Enzima com nome completo no cloze, verso com o que ela reconhece (CpG hemimetilado). Davi reescreveu o cloze: o nome específico é o que se decora.

### Exemplar · note 1792350094380 (?; X em 2026-10-20)
- **Card:** [estrutura com seta] Artéria basilar
- **Verso:** [IMG kh-arteria-basilaris.jpg]
- **Análise:** Estrutura do Kenhub (artéria) com seta e nome; modelo para neuroanatomia vascular.

### Exemplar · note 1792166969765 (2026-uc03-imunologia-51-disturbios-sistema-imune; X em 2026-10-20)
- **Card:** How the immune system fails: / 1. Too weak a response: {{c1::immunodeficiency::i…}} / 2. Adaptive response against self: {{c1::autoimmunity::a…}} / 3. Innate inflammation with no trigger: {{c1::autoinflammatory::a…}} disease
- **Verso:** - Each group is a different failure: defense, self-tolerance, or the brake on inflammation / - An exaggerated response to a harmless foreign antigen is hypersensitivity (lesson 64)
- **Análise:** Organizador das falhas do sistema imune com dica da 1ª letra e verso que distingue cada falha e aponta a aula vizinha. Modelo de mapa da aula em 3 linhas.

### Exemplar · note 1792328879263 (?; X em 2026-10-20)
- **Card:** [estrutura com seta] Espaço epidural
- **Verso:** [IMG kh-epidural-space.jpg]
- **Análise:** Estrutura do Kenhub em português com figura e seta. Modelo de card de estrutura.

### Exemplar · note 1791762418025 (2026-uc19-farmacologia-01-introducao-mecanismos; X em 2026-10-20)
- **Card:** Affinity is the ability to bind the target, whereas {{c1::intrinsic activity}} is the ability to activate it once bound
- **Verso:** - Antagonists have affinity but zero intrinsic activity
- **Análise:** Contraste afinidade × atividade intrínseca com o termo no cloze e verso que aplica (antagonista: afinidade sem atividade). Alto custo-efetividade: define dois conceitos e uma classe de fármacos.

### Exemplar · note 1790974689880 (2026-uc08-anatomia-02-intestino-grosso-canal-anal; X em 2026-10-22)
- **Card:** Three external features distinguish the large intestine from the small intestine / / - {{c1::haustra (sacculations)}}- {{c2::omental (epiploic) appendices}}- {{c3::taeniae coli}}
- **Verso:** - The rectum has none of them / / [IMG nebli-moore-fig-5-52.png]
- **Análise:** Organizador com três características que distinguem o intestino grosso, cada uma num índice, e verso com a exceção (reto) e figura do livro. Modelo de 'como reconhecer X'.

### Exemplar · note 1791629593848 (2026-uc03-imunologia-07-organizacao-sistema-imune; X em 2026-10-22)
- **Card:** Which region of the lymph node enlarges and multiplies during humoral immune response (e.g., bacterial infection)? / / {{c1::Germinal centers}}
- **Verso:** Increased number of germinal centers → lymphadenopathy / / [IMG a05cb5f548622083368e4ff1c9597f04.webp]
- **Comentário de Davi (2026-10-22):** “não tem um card igual a esse?”
- **Análise:** Pergunta funcional (o que aumenta na resposta humoral) e verso com a consequência clínica mínima (linfadenomegalia) e figura. Modelo de histologia funcional.

### Exemplar · note 1790981523225 (2026-uc08-anatomia-07-vascularizacao-visceras; X em 2026-10-22)
- **Card:** {{c2::Acute}} mesenteric ischemia may occur due to a thrombotic or embolic occlusion of the {{c1::superior mesenteric}} artery
- **Verso:** [IMG ae426f51d894c4f87ff49e803f10956c.jpg] / / Classic picture: pain out of proportion to the exam
- **Análise:** Doença com o vaso causal e o quadro clássico no verso; clínica mínima e ligada à anatomia da aula.

### Exemplar · note 1792175047836 (2026-uc03-microbiologia-44-micoses-cutaneas; X em 2026-10-22)
- **Card:** Dermatophyte spores coating the outside of the hair shaft form an {{c1::ectothrix::ectothrix/endothrix}} infection, and spores inside it an {{c1::endothrix::ectothrix/endothrix}} infection
- **Verso:** - Microsporum canis is typically ectothrix; Trichophyton tonsurans is endothrix, giving the black-dot tinea capitis
- **Análise:** Contraste ecto × endotrix no mesmo índice com dica e verso com exemplos de agentes. Modelo de par complementar.

### Exemplar · note 1791000313954 (2026-uc08-fisiologia-05-digestao-absorcao-nutrientes; X em 2026-10-22)
- **Card:** Vitamin K deficiency may occur in {{c1::newborns}} due to lack of {{c1::colonic bacteria}} that normally synthesize vitamin K
- **Verso:** Vitamin K injection is given prophylactically to all newborns at birth to prevent hemorrhagic disease of the newborn
- **Comentário de Davi (2026-10-13):** “isso é um bom card clínico + agrega conteúdo”
- **Análise:** Deficiência + causa (falta de bactérias) com a conduta no verso. Card clínico que ensina fisiologia (quem produz vitamina K).

### Exemplar · note 1792588686964 (2026-uc07; X em 2026-10-22)
- **Card:** Cada nervo espinal forma-se pela união de: / 1. Raiz {{c2::anterior}}— axônios {{c1::eferentes}} / 2. Raiz {{c2::posterior}} — axônios {{c1::aferentes}}
- **Verso:** O mesmo índice oculta os dois lados do contraste, evitando que um entregue a resposta do outro. / / [IMG kh-anterior-root-of-spinal-nerve.jpg]
- **Comentário de Davi (2026-10-22):** “card entrega a resposta em si mesmo completando a ideia ESSE comentário é mt ruim”
- **Análise:** Organizador das raízes do nervo espinal com o mesmo índice nos dois lados (anterior/eferente) depois da edição de Davi. Modelo: o par que se completa fica no mesmo índice.

### Exemplar · note 1792572870692 (2026-uc07-cerebelo-cortex-cerebelar; X em 2026-10-23)
- **Card:** [estrutura com seta] Tenda do cerebelo
- **Verso:** [IMG kh-tentorium-cerebelli.jpg]
- **Análise:** Estrutura do Kenhub em português (cerebelo) com seta e figura destacada. Modelo de estrutura.

### Exemplar · note 1791000306802 (2026-uc08-fisiologia-05-digestao-absorcao-nutrientes; X em 2026-10-23)
- **Card:** Which monosaccharide(s) are extruded from the intestinal cell into the blood by GLUT-2? / {{c1::Glucose, galactose, and fructose}}
- **Verso:** [IMG 28f38c4892f40525fdb651ffa8badb2d.png] / / All three monosaccharides leave through the same basolateral carrier
- **Análise:** Pergunta curta com a resposta conjunta (três monossacarídeos) e verso com a regra (mesmo transportador basolateral) e figura. Custo-efetividade: um card resolve a saída de todos.

### Exemplar · note 1791631347467 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii; X em 2026-10-23)
- **Card:** HDAC inhibitors prevent histones from being {{c1::deacetylated}} resulting in genes such as tumor suppressors being {{c2::transcribed}}
- **Verso:** [IMG a4794dc612338ff62357e1a81d0dea71.jpg] / / - Approved for some lymphomas and multiple myeloma
- **Comentário de Davi (2026-10-23):** “isso é um bom exemplo de card que poderia ser simples, mas ensina e ajuda a decorar com extrema eficácia: poderia ser só um card perguntando o que faz HDAC, mas já há informação sobre inibidores dessa enzima e o resultado do que acontece ao inibi-lo + um comentário que aprofunda ainda mais ótimo card”
- **Análise:** Modelo de custo-efetividade citado por Davi: em vez de só 'o que faz HDAC', cobra o efeito de inibi-la e a consequência (supressores voltam a ser transcritos), com verso que aprofunda (uso em linfoma/mieloma). Usar: função + o que acontece se bloqueada + consequência, num card só.

### Exemplar · note 1792588686980 (2026-uc07; X em 2026-10-23)
- **Card:** A cavidade do tubo neural origina, no tronco e na medula: / - mesencéfalo: {{c1::aqueduto cerebral::a…}} / - ponte e bulbo: {{c1::quarto ventrículo::q…}} / - medula espinal: {{c1::canal central::c…}}
- **Verso:** - No prosencéfalo a mesma cavidade forma os ventrículos laterais e o terceiro ventrículo / [IMG kh-cap-3490.jpg]
- **Comentário de Davi (2026-10-23):** “poderia ser com 3 clozes, um só card e tópicos”
- **Análise:** Organizador refeito pelo comentário de Davi: três destinos da cavidade do tubo neural, um por linha, no mesmo índice com dica da 1ª letra, e o verso completa o quadro (prosencéfalo). Modelo de como um pedido de 'um só card em tópicos' vira um organizador que se lembra inteiro.

## Anti-exemplares (comentários de Davi, com o processo de ajuste)

### Anti-exemplar · note 1784300091178 (?)
- **Card antes:** A forma combinatória diverticul/o refere-se a uma {{c1::evaginação sacular}} .
- **Davi, rodada 1 (2026-10-03):** “não sei o que é evaginação sacular”
- **Card depois (vivo):** Diverticul/o indica uma pequena {{c1::bolsa}} que se projeta para fora da parede de um órgão.
  - **Verso depois:** Evaginação sacular significa uma projeção para fora em forma de saco. Um divertículo intestinal comunica-se com o interior do intestino; diverticulite é sua inflamação.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1784308057250 (?)
- **Card antes:** Em disjunção , dis- indica {{c1::separação}} .
- **Davi, rodada 1 (2026-10-03):** “nesse tipo de card, é horrível que haja x ou y, o certo é que haja uma palavra só. duas palavras não aumentam o valor pedagógico, só atrapalham, porque dificultam a reter”
- **Card depois (vivo):** Em disjunção, dis- indica {{c1::separação}}.
  - **Verso depois:** Aplicação: disjunção é a separação de estruturas antes unidas, como cromossomos durante a divisão celular.
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1784308057313 (?)
- **Card antes:** Em exocitose , exo- indica movimento para {{c1::fora}} da célula.
- **Davi, rodada 1 (2026-10-03):** “aqui valeria comparar ecto e exo, pra saber a diferença (esse tipo de coisa ajuda a reter). quando for ver os comentários, não apaga eles, vai mantendo, mesmo que estejam corrigidos, porque daí uma hora reúnos e vemos seus erros mais frequentes”
- **Card depois (vivo):** Em exocitose, exo- indica movimento para {{c1::fora}} da célula.
  - **Verso depois:** Contraste: exo- indica movimento ou relação para fora; ecto- indica posição/camada externa, como em ectoderma.
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1784308057390 (?)
- **Card antes:** Em paratireoide , para- indica {{c1::adjacência}} à tireoide.
- **Davi, rodada 1 (2026-10-03):** “lado ou anormal? não sei e o card não explica, só confude. reveja todos os erros que aponto para todos os cards, não pode ter nenhum erro já cometido mantido quando for corrigir, porque se eu já te corrigi você tem que entender o padrão”
- **Card depois (vivo):** Em paratireoide, para- indica {{c1::adjacência}} à tireoide.
  - **Verso depois:** Aplicação: Neste termo, para- significa “junto a”. Em outros termos, pode ter outro sentido; o contexto deve selecionar apenas um.
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1784308059839 (?)
- **Card antes:** Em odinofagia , o elemento odino- indica {{c1::dor}} .
- **Davi, rodada 1 (2026-10-03):** “caard incoerente e incorret”
- **Card depois (vivo):** Em odinofagia, o elemento odino- indica {{c1::dor}}.
  - **Verso depois:** Aplicação: Odinofagia é dor ao engolir.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1784308059853 (?)
- **Card antes:** Em atresia esofágica , atresia indica {{c1::ausência congênita de luz}} .
- **Davi, rodada 1 (2026-10-03):** “muito avançado com comentário fraco. poderia decompôr a e tresia, para ficar mais didático (não sei se esse card existe no deck, mas o card que estamos conversando em cima apareceu logo no primeiro dia de estudo, então não consegui respondê-lo o cloze também tem muitas respostas”
- **Card depois (vivo):** Em atresia, a- indica {{c1::ausência}} de uma abertura normal.
  - **Verso depois:** a- = ausência; trēsis = abertura/perfuração. A luz é o espaço interno de um órgão tubular. Na atresia esofágica, a passagem pelo esôfago não é contínua; estenose significa estreitamento.
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1784308059925 (?)
- **Card antes:** Em eosinófilo , -filo indica {{c1::afinidade pela eosina}} ; eosinofilia indica {{c1::aumento de eosinófilos}} .
- **Davi, rodada 1 (2026-10-03):** “clozes com muitas palavras. conteúdo é importante, mas o card é ruim, vale reescrevê-lo”
- **Card depois (vivo):** Em eosinófilo, -filo indica {{c1::afinidade}} pela eosina.
  - **Verso depois:** Eosina é um corante. Os grânulos do eosinófilo têm afinidade por ele. Eosinofilia é aumento de eosinófilos; esse é o significado do termo clínico completo.
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1784308059948 (?)
- **Card antes:** Em litíase , lit/o = {{c1::cálculo}} ; -íase = {{c1::condição}} .
- **Davi, rodada 1 (2026-10-03):** “não compreendi esse”
- **Card depois (vivo):** Em litíase, lit/o significa {{c1::cálculo}}.
  - **Verso depois:** lit/o = pedra/cálculo; -íase = condição patológica. Litíase é a condição caracterizada por cálculos.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1784308062198 (?)
- **Card antes:** Em hipertrofia , -trofia indica {{c1::crescimento}} .
- **Davi, rodada 1 (2026-10-03):** “trofia é desenvolvimento, não crescimento, porque atrofia não é crescimento”
- **Card depois (vivo):** O elemento -trofia refere-se à {{c1::nutrição}} dos tecidos.
  - **Verso depois:** Do grego trophḗ, nutrição. O termo completo descreve a condição do tecido: hipertrofia = aumento do tamanho celular; atrofia = redução. A raiz não significa que todo termo com -trofia indique crescimento.
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1790974691830 (2026-uc08-anatomia-02-intestino-grosso-canal-anal)
- **Card antes:** The left colic flexure lies higher than the right one and is related to the {{c1:: spleen }}
- **Davi, rodada 1 (2026-10-03):** “imagem”
- **Card depois (vivo):** The left colic flexure lies higher than the right one and is related to the {{c1::spleen}}
  - **Verso depois:** - The right colic flexure lies under the liver / / [IMG nebli-moore-fig-5-43.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790974692329 (?)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-03):** “cloze zuado”
- **Card depois (vivo):** 
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1790978724448 (2026-uc08-anatomia-02-intestino-grosso-canal-anal)
- **Card antes:** In the female, the rectum is related anteriorly to the {{c1:: vagina }}, with the rectouterine pouch above it
- **Davi, rodada 1 (2026-10-03):** “poderia ter imagem”
- **Davi, rodada 2 (2026-10-13):** “card sobre mulher e imagem de homem preciso esperar o claude para voltar aos bons cards SETAS ZUADAS”
- **Card depois (vivo):** In the female, the rectum is related anteriorly to the {{c1::vagina}}, with the rectouterine pouch above it
  - **Verso depois:** - Rectovaginal septum between them / - Rectouterine pouch (of Douglas) above / / [IMG a4081b1bdab85a9b3e8a9380b1ea128d.png]
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1790980910230 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** {{c1::Villi}} are small finger-like projections of tissue which {{c2:: increase the surface area of the intestine ::function as what?}}.
- **Davi, rodada 1 (2026-10-03):** “cloze mt grande: poderia ser só inscrease intestinal surface”
- **Card depois (vivo):** {{c1::Villi}} are small finger-like projections that increase the intestinal {{c2::surface area}}
  - **Verso depois:** - Capillaries absorb water-soluble nutrients / - Lacteal absorbs fat into lymph / / [IMG 50c5a616a8bf0f52dfaeb2f05ef163b9-8f58ff0f5178bf77595cd5b5ed9fa05af3afa26d.png]
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1790981527126 (2026-uc03-patologia-radiologia-19-correlacao-2)
- **Card antes:** {{c2:: Anorectal varices }} result from portosystemic shunting between the {{c1:: superior rectal }} (portal) and {{c1:: middle/inferior rectal }} (systemic) veins
- **Davi, rodada 1 (2026-10-03):** “poderia ter imagem”
- **Davi, rodada 2 (2026-10-05):** “depois que eu fizer um comentário e vc corrigir, é bom colocar o comentário como corrigido, só colocar assim, na linha de baixo após o comentário: CORRIGIDO, data. assim vou saber quais cards o chat já corrigiu”
- **Card depois (vivo):** {{c2::Anorectal varices}} result from portosystemic shunting between the {{c1::superior rectal}} (portal) and {{c1::middle/inferior rectal}} (systemic) veins
  - **Verso depois:** Superior rectal (portal) meets middle and inferior rectal veins (systemic) / / [IMG nebli-moore-fig-5-75.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023294146 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** Permanent circular folds of mucosa and submucosa in the small intestine are the {{c1::plicae circulares}}
- **Davi, rodada 1 (2026-10-03):** “poderia ter imagem”
- **Card depois (vivo):** Permanent circular folds of mucosa and submucosa in the small intestine are the {{c1::plicae circulares}}
  - **Verso depois:** Plicae include submucosa; villi are mucosa only / / [IMG 61c046678c4269035ed102ab7c9bca75-fig.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023351944 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The most numerous lingual papillae, conical and heavily keratinized, are the {{c1::filiform}} papillae
- **Davi, rodada 1 (2026-10-03):** “[nota original papilas-tipos, 03/10] card gigantesco, não dá poderia ter imagem”
- **Card depois (vivo):** The most numerous lingual papillae, conical and keratinized, are the {{c1::filiform}} papillae
  - **Verso depois:** - No taste buds, only friction / / [IMG tg-filiform.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023352068 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Mushroom-shaped, lightly keratinized papillae scattered among the filiform ones are the {{c1::fungiform}} papillae
- **Davi, rodada 1 (2026-10-03):** “poderia ter imagem faltou coisa no comentário: algo curto, como vários cards tem”
- **Davi, rodada 2 (2026-10-05):** “imagem ficou zuada, não deu pra aprender bem com ela comentário também ficou ruim nesse tipo, cabe bem uma tabela com os tipos de papillae”
- **Card depois (vivo):** Mushroom-shaped papillae scattered among the filiform ones are the {{c1::fungiform}} papillae
  - **Verso depois:** PapillaShape / locationTaste budsFiliformPointed; most of the anterior dorsumNone — frictionFungiformMushroom; scattered, especially tip and sidesOn the upper surfaceFoliateParallel folds on the posterolateral edgesIn the fold wallsVallateLarge, in a V just anterior to terminal sulcusIn the trench w
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1791023352198 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The largest lingual papillae, lined up just in front of the sulcus terminalis, are the {{c1::vallate}} papillae
- **Davi, rodada 1 (2026-10-03):** “poderia ter imagem”
- **Davi, rodada 2 (2026-10-05):** “imagem zuada poderia ter uma tabela + algo pra ser visual na língua de forma fácil”
- **Card depois (vivo):** The largest lingual papillae, in a V row just in front of the sulcus terminalis, are the {{c1::vallate}} papillae
  - **Verso depois:** - Each sits in a moat lined with taste buds / / [IMG tg-sulcus.jpg]
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1791023355318 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The sublingual gland is made mostly of {{c1::mucous}} tubules
- **Davi, rodada 1 (2026-10-03):** “falta comentário com explicação”
- **Davi, rodada 2 (2026-10-05):** “imagem ruim”
- **Card na rodada 3:** The sublingual gland is made mostly of {{c1:: mucous }} tubules
- **Davi, rodada 3 (2026-10-22):** “AQUI tem que ter aquela tabela do outro card”
- **Card depois (vivo):** The sublingual gland is made mostly of {{c1::mucous}} tubules
  - **Verso depois:** - Pale, foamy tubules → mucus that lubricates food / / [IMG sal-sublingual.jpg] / ParotidSubmandibularSublingualAciniexclusively serousmixed, mostly serousmixed, mostly mucousShare of saliva~25%~70%~5%
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1791023363069 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Progenitor cells that migrate down into the gland become {{c1::secretory}} cells, renewed more slowly than surface cells
- **Davi, rodada 1 (2026-10-03):** “tá faltanod comentário de novo”
- **Card depois (vivo):** Progenitor cells that migrate down into the gland become {{c1::secretory}} cells, renewed more slowly than surface cells
  - **Verso depois:** - They replace parietal, chief and enteroendocrine cells
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791034105561 (2026-uc08-anatomia-02-intestino-grosso-canal-anal)
- **Card antes:** The projection of the terminal ileum into the cecum, closing the ileal orifice with two lips, is the {{c1::ileal papilla}}
- **Davi, rodada 1 (2026-10-03):** “[oclusão substituída io-papila-ileal, 03/10] cloze zuado”
- **Card depois (vivo):** The projection of the terminal ileum into the cecum, closing the ileal orifice with two lips, is the {{c1::ileal papilla}}
  - **Verso depois:** Also called the ileocecal valve; its upper (ileocolic) and lower (ileocecal) lips meet at the ileal orifice / / [IMG nebli-moore-fig-5-53.png]
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1790980911405 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** Cells born in the crypt differentiate as they migrate {{c1:: up the villus }}, except Paneth cells, which stay at the crypt base
- **Davi, rodada 1 (2026-10-03):** “gostei muito dessa imagem!!!! porém, cloze pode ser mais curto, ficou ruim de lembrar cloze também fica melhor, quando dá, no fim da frase”
- **Card na rodada 2:** Most intestinal epithelial cells are born in the crypt and differentiate as they migrate toward the villus {{c1:: tip }}
- **Davi, rodada 2 (2026-10-05):** “card está bom, mas acho que o cloze poderia obrigar a relembrar uma parte mais central do processo”
- **Card depois (vivo):** Most intestinal epithelial cells arise in the {{c1::crypts}} and differentiate while migrating toward the villus tip.
  - **Verso depois:** Paneth cells move down to the crypt base instead of up / / [IMG bba4d2f83e511fcdce6fa8edc50d1f21.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023296668 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** The apical {{c1::striated (brush) border}} of enterocytes is a dense layer of microvilli
- **Davi, rodada 1 (2026-10-03):** “cloze mt grande, ruim de lembrar”
- **Card depois (vivo):** Dense microvilli on the apical surface of enterocytes form the {{c1::brush border}}
  - **Verso depois:** Under light microscopy the microvilli look like stripes, hence 'striated' / / / / [IMG bt04-enterocyte-tem.png]
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1791023302118 (?)
- **Card antes:** The colon wall is puckered into sacs called {{c1::haustra}}
- **Davi, rodada 1 (2026-10-03):** “isso é mais de anato, não desse deck”
- **Card depois (vivo):** (nota apagada)
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1790980916154 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** Compare the mucosae: the left image with villi is {{c1::small intestine}}, while the right image with straight crypts is {{c1::colon}}
- **Davi, rodada 1 (2026-10-04):** “cloze de imagem tá vindo zuado no ankidroid do cell”
- **Davi, rodada 2 (2026-10-05):** “mt info no mesmo card tb imagens são ruins e nao aparecem no ankidroid”
- **Card depois (vivo):** This H&E mucosa belongs to the {{c1::small intestine}} / [IMG bt4-jejunum.jpg]
  - **Verso depois:** - Tall villi above the crypts (colon: crypts only, no villi) / - Plica = fold of mucosa + submucosa; villus = mucosa only
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1784308054026 (?)
- **Card antes:** -tripsia indica {{c1::fragmentação}} ; -clasia, {{c1::fratura}} .
- **Davi, rodada 1 (2026-10-05):** “cada um desses deveria ser um card só, fica confundido as duas infos”
- **Card depois (vivo):** Em litotripsia, -tripsia indica {{c1::fragmentação}}.
  - **Verso depois:** Litotripsia fragmenta um cálculo em pedaços menores. O termo -clasia é estudado separadamente em osteoclasia.
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1790972069711 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** The duodenojejunal flexure is supported by the {{c1:: suspensory muscle }} of the duodenum (ligament of Treitz)
- **Davi, rodada 1 (2026-10-05):** “imagem aqui ficou ruim pra explicar o card”
- **Card depois (vivo):** The duodenojejunal flexure is supported by the {{c1::suspensory muscle}} of the duodenum (ligament of Treitz)
  - **Verso depois:** - Skeletal muscle from the right crus plus smooth muscle from the duodenum / / [IMG an-treitz.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790973222133 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-05):** “cards de estruturas muito similares em anatomia poderiam vir juntos, não sei como seria ao certo para isso ocrrer mas aqui, por exemplo, seria bom se logo em seguida eu fizesse o card de vasos curtos do íleo”
- **Card depois (vivo):** 
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1790979864034 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The {{c1:: submucosal (Meissner's) }} plexus of the gut wall primarily controls secretion and blood flow
- **Davi, rodada 1 (2026-10-05):** “imagem zuada, mas esse mnemônico é ótimo esses comentários, é bom que tenha aquele "CORRIGIDO, data.", porque daí daqui um tempo teremos uma base de dados boa para calibração fina de criação de cards com IA”
- **Card depois (vivo):** The {{c1::submucosal (Meissner's)}} plexus of the gut wall primarily controls secretion and blood flow
  - **Verso depois:** - Submucosal: Secretion / - Myenteric: Motility / / [IMG wl-meissner.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790979866060 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** This is a magnified image of {{c1::antral/pyloric stomach}}
- **Davi, rodada 1 (2026-10-05):** “cloze com mt info, tem que ser específico pra decorar melhor”
- **Card depois (vivo):** This is a magnified image of {{c1::pylorus}} / / [IMG paste-3c60c7c15a904453246835ff33ccaf3d3c6a6c83.png][IMG paste-d7c5ef5cd521a3cf957a7db2d65f6b58bfaa2489.png]
  - **Verso depois:** - Pyloric (antral) mucosa has deep gastric pits and coiled, predominantly mucous glands.
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1790980909978 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-05):** “esse cloze poderia ser substituído por um feito de forma manual, só com "duodeno", para ficar mais atômico anotar feedback que isso é possível e arrumar aqui”
- **Card depois (vivo):** 
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1790980912277 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-05):** “imagens ruins para identificação. teria sido melhor puxar de algum livro ou do histology guide imagens melhores”
- **Card na rodada 2:** Identify the cells with red apical granules at the crypt base.
- **Davi, rodada 2 (2026-10-13):** “card mt estranho”
- **Card depois (vivo):** 
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790980916280 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** In the colon, which lacks Paneth cells, the stem cell niche is supported by {{c1:: deep crypt secretory }} cells
- **Davi, rodada 1 (2026-10-05):** “ficou estranho esse cloze, não compreendi bem o que o card quer lembrar”
- **Card depois (vivo):** The colon has no Paneth cells, so its crypt-base stem cells are supported by {{c1::deep crypt secretory}} cells
  - **Verso depois:** - Same niche role as Paneth cells in the small intestine
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791000309552 (2026-uc08-fisiologia-05-digestao-absorcao-nutrientes)
- **Card antes:** {{c1:: Colipase }} anchors pancreatic lipase to the bile salt-coated fat droplet
- **Davi, rodada 1 (2026-10-05):** “explicação do tab não didática (não sei bem o porquê) imagem zuada também”
- **Card depois (vivo):** (nota apagada)
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791014716874 (2026-uc08-fisiologia-06-secrecao-gastrica)
- **Card antes:** Pepsinogen is secreted in response to {{c1:: vagal stimulation }} and {{c2:: local H + }}
- **Davi, rodada 1 (2026-10-05):** “esse comentário do tab com 1, 2 3 e 4 não gostei dá para achar formas melhores de explicar com storytelling”
- **Card depois (vivo):** Pepsinogen is secreted in response to {{c1::vagal stimulation}} and {{c2::local H+}}
  - **Verso depois:** - Vagal acetylcholine stimulates chief cells to release pepsinogen. / - Luminal acid also stimulates secretion through local reflexes and converts pepsinogen into pepsin.
- **Análise:** [tab] Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.

### Anti-exemplar · note 1791023352819 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The only lingual papillae without taste buds are the keratinized {{c1::filiform}} papillae
- **Davi, rodada 1 (2026-10-05):** “imagem zuada”
- **Card na rodada 2:** The only lingual papillae without taste buds are the {{c1:: filiform }} papillae
- **Davi, rodada 2 (2026-10-15):** “faltou comentário do porquê”
- **Card depois (vivo):** The only lingual papillae without taste buds are the {{c1::filiform}} papillae
  - **Verso depois:** [IMG tg-filiform.jpg] / - They are keratinized and roughen the tongue to grip and move food; their role is mechanical, so they need no taste buds
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023353318 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The cheeks, soft palate and floor of the mouth have {{c1::lining}} mucosa, with nonkeratinized epithelium
- **Davi, rodada 1 (2026-10-05):** “IMAGEM RUIM”
- **Card depois (vivo):** The cheeks, soft palate and floor of the mouth have {{c1::lining}} mucosa
  - **Verso depois:** - Nonkeratinized and flexible
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023366868 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** In the fundus, enteroendocrine cells mainly secrete {{c1::serotonin}}
- **Davi, rodada 1 (2026-10-05):** “imagem ruim, esse tipo”
- **Card depois (vivo):** Gastrointestinal enterochromaffin (EC) cells release {{c1::serotonin}}.
  - **Verso depois:** CellMediatorRoleECSerotonin (5-HT)Coordinates intestinal secretion and motilityECL, gastric body/fundusHistamineStimulates acid secretion by parietal cells
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791054012018 (2026-uc03-grand-round-21-diabetes)
- **Card antes:** Diabetic ketoacidosis (DKA) is associated with {{c1:: Kussmaul }} breathing, which is rapid/deep breathing to compensate for metabolic {{c2:: acidosis }}
- **Davi, rodada 1 (2026-10-05):** “card tem a resposta nele mesmo está bom, só há esse pequeníssimo problema, porque não tenho que lembrar tanto gostei do conteúdo, formatação”
- **Card depois (vivo):** In uncontrolled diabetes mellitus, {{c1::Kussmaul}} breathing compensates for the metabolic {{c2::acidosis}} caused by ketone accumulation.
  - **Verso depois:** - Deep breathing lowers CO₂ and partially compensates for the pH fall. / - Ketone accumulation produces the metabolic disorder; ventilation does not remove its cause.
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1791054015697 (2026-uc03-grand-round-21-diabetes)
- **Card antes:** What is the first change that occurs in the kidney in a diabetes mellitus patient? {{c1::Non-enzymatic glycation of the GBM}}
- **Davi, rodada 1 (2026-10-05):** “cloze com muitas palavras (8), difícil de lembrar”
- **Card depois (vivo):** Hyperglycemia damages the glomerular basement membrane through nonenzymatic {{c1::glycation}}.
  - **Verso depois:** [IMG bd8b2d59515a17a289866930cc2b2722.webp] / / The GBM thickens but becomes more permeable to albumin / / [IMG nebli-robbins-fig-24-35.png]
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1790973210184 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-05):** “faltou o cloze ter uma seta apontando para onde era pra ver nos irmãos tb”
- **Card depois (vivo):** 
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1790979868887 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** When a parietal cell is stimulated, its {{c1:: tubulovesicles }} fuse with the canaliculus, expanding the membrane that carries the proton pumps
- **Davi, rodada 1 (2026-10-05):** “imagem poderia cobrar o processo melhor”
- **Card depois (vivo):** During parietal cell stimulation, proton pump-containing tubulovesicles fuse with the {{c1::canalicular membrane}}
  - **Verso depois:** - Resting: pumps stored in tubulovesicles (TV) / - Stimulated: microvilli (MV) expand, adding pumps / / [IMG par-tv.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023270317 (2026-uc08-fisiologia-08-motilidade-i)
- **Card antes:** Varicosities release {{c1::acetylcholine}} or norepinephrine, which diffuse to many smooth muscle cells
- **Davi, rodada 1 (2026-10-05):** “imagem”
- **Card na rodada 2:** Varicosities release {{c1:: acetylcholine }} or norepinephrine, which diffuse to many smooth muscle cells
- **Davi, rodada 2 (2026-10-13):** “imagem ruim”
- **Card depois (vivo):** Varicosities release {{c1::acetylcholine}} or norepinephrine, which diffuse to many smooth muscle cells
  - **Verso depois:** [IMG nebli-guyton-fig-8-4.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023270891 (2026-uc08-fisiologia-08-motilidade-i)
- **Card antes:** Smooth muscle actin filaments lack {{c1::troponin}}; contraction starts through calmodulin and MLCK
- **Davi, rodada 1 (2026-10-05):** “tipo de card ruim, com ponto e vírgula”
- **Card depois (vivo):** Unlike skeletal muscle, smooth muscle lacks {{c1::troponin}}.
  - **Verso depois:** MuscleCa²⁺ sensorHow contraction is enabledSkeletalTroponin CMoves tropomyosin off actin sitesSmoothCalmodulinActivates MLCK, which phosphorylates myosin
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791023353568 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The ventral surface of the tongue is smooth and covered by {{c1::lining}} mucosa
- **Davi, rodada 1 (2026-10-05):** “imagem”
- **Card na rodada 2:** The ventral surface of the tongue is smooth and covered by {{c1:: lining }} mucosa
- **Davi, rodada 2 (2026-10-13):** “imagem zuada ainda”
- **Card depois (vivo):** The ventral surface of the tongue is smooth and covered by {{c1::lining}} mucosa
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023355818 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Mucous cells stain poorly in H&E because their granules hold hydrophilic {{c1::mucins}}
- **Davi, rodada 1 (2026-10-05):** “imagem desse estilo é zuada tem várias, anota pra não ter mais imagem tem que ser mais direcionada pro card”
- **Card na rodada 2:** Mucous cells stain pale on H&E because their granules hold hydrophilic {{c1:: mucins }}
- **Davi, rodada 2 (2026-10-13):** “imagem ruim, também faltou explicar a diferença entre mucous cells e goblet cells”
- **Card depois (vivo):** Mucous cells stain pale on H&E because their granules hold hydrophilic {{c1::mucins}}
  - **Verso depois:** - Intestinal goblet cells look the same, but each one is a single mucous cell scattered in an epithelium
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023357918 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Near the stomach, esophageal {{c1::cardiac}} glands in the lamina propria add mucus
- **Davi, rodada 1 (2026-10-05):** “imagem”
- **Card depois (vivo):** Near the stomach, esophageal {{c1::cardiac}} glands in the lamina propria add mucus
  - **Verso depois:** - Same mucous type as the gastric cardiac glands
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023364492 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The apical membrane of the parietal cell folds inward to form an intracellular {{c1::canaliculus}} lined with microvilli
- **Davi, rodada 1 (2026-10-05):** “aqui, a imagem não me ajuda a entender o que é o canaliculus”
- **Card na rodada 2:** The deep, microvilli-lined channel that runs inside the parietal cell and receives its H⁺ is the {{c1:: intracellular canaliculus }}
- **Davi, rodada 2 (2026-10-13):** “imagem + card estranho + card não claro + card não prende a atenção card não induz a resposta, nem explica bem”
- **Card depois (vivo):** The deep, microvilli-lined channel that runs inside the parietal cell and receives its H⁺ is the {{c1::intracellular canaliculus}}
  - **Verso depois:** - Inward fold of the apical membrane, open to the gland lumen / - Its microvilli carry the H⁺/K⁺ ATPase / / [IMG par-canal.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790979869685 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Pepsinogen (inactive) is converted into {{c1:: pepsin }} (active) in the presence of {{c2:: H + }}
- **Davi, rodada 1 (2026-10-05):** “imagem inadequada”
- **Davi, rodada 2 (2026-10-13):** “comentário estranho”
- **Card depois (vivo):** Pepsinogen (inactive) is converted into {{c1::pepsin}} (active) in the presence of {{c2::H+}}
  - **Verso depois:** - Pepsin then activates more pepsinogen (autocatalysis)
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790999832528 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** Slow waves originate in the {{c1:: interstitial cells of Cajal }}, which serve as the pacemaker for GI smooth muscle
- **Davi, rodada 1 (2026-10-05):** “imagem poderia ter aqui”
- **Card depois (vivo):** Slow waves originate in the {{c1::interstitial cells of Cajal}}, which serve as the pacemaker for GI smooth muscle
  - **Verso depois:** Interstitial cells of Cajal set the slow-wave rhythm; gap junctions spread it to the muscle / [IMG 8c95b6838315e860024bc9caae2bcae1.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790999833204 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** A slow wave crossing the contractile threshold causes contraction, but spike potentials appear only above the {{c1::electrical}} threshold
- **Davi, rodada 1 (2026-10-05):** “IMAGEM RUIM card zuado cloze não num local bom de lembrar”
- **Card depois (vivo):** At the crest of a GI slow wave, crossing the electrical threshold triggers {{c1::spike potentials}}
  - **Verso depois:** - Spikes let more Ca²⁺ in, so the contraction gets stronger / / [IMG fi-spikes.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790999835379 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** In antral systole , the antrum contracts against a closed pylorus, causing {{c1::retropulsion}} of chyme into the body
- **Davi, rodada 1 (2026-10-05):** “IMAGEM ZUADA”
- **Card depois (vivo):** In antral systole, the antrum contracts against a closed pylorus, causing {{c1::retropulsion}} of chyme into the body
  - **Verso depois:** - Grinds and mixes chyme into smaller particles
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790999838053 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** {{c1::Mass movements}}, a few times a day, push feces from the colon into the rectum
- **Davi, rodada 1 (2026-10-05):** “cloze aqui poderia ter várias respostas não ficou um bom cloze, único”
- **Card na rodada 2:** Strong colonic contractions that push contents toward the rectum only a few times a day are {{c1:: mass movements }}
- **Davi, rodada 2 (2026-10-13):** “ficou estranho o comentário aqui”
- **Card depois (vivo):** Strong colonic contractions that push contents toward the rectum only a few times a day are {{c1::mass movements}}
  - **Verso depois:** - Often after meals (gastrocolic reflex)
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1791023270196 (2026-uc08-fisiologia-08-motilidade-i)
- **Card antes:** Autonomic axons in smooth muscle release transmitter from periodic swellings called {{c1::varicosities}}
- **Davi, rodada 1 (2026-10-05):** “imagem zuada alguns cards autorais faltam negrito e sublinhado como no anking tme”
- **Card na rodada 2:** Autonomic axons in smooth muscle release transmitter from periodic swellings called {{c1:: varicosities }}
- **Davi, rodada 2 (2026-10-13):** “poderia ter imagem card escrito de forma não clara faltou negrito”
- **Card depois (vivo):** Autonomic axons in smooth muscle release transmitter from periodic swellings called {{c1::varicosities}}
  - **Verso depois:** [IMG nebli-guyton-fig-8-4.png]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791023355444 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Pyramidal protein-secreting salivary cells with round nuclei and apical granules are {{c1::serous}} cells
- **Davi, rodada 1 (2026-10-05):** “card mt denso imagem zuada não ficou bom pensa o porquê depois”
- **Card na rodada 2:** Salivary cells with round nuclei and dark apical granules are {{c1:: serous }} cells
- **Davi, rodada 2 (2026-10-13):** “IMAGEM ZUADA”
- **Davi, rodada 3 (2026-10-22):** “coloquei um negrito, aprende isso para entender o que fiz e porquê melhora tanto o card toda mudança que eu fizer manualmente nos cards vc tem que perceber quando eu pedir para ver os comentários, porque assim você pode aprender a fazer cards melhores, já colocando os que mexi como bons exemplares”
- **Card depois (vivo):** Salivary cells with round nuclei and dark apical granules are {{c1::serous}} cells
  - **Verso depois:** - Granules = zymogen (proteins such as amylase) / / [IMG sal-serous-cell.jpg]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791023357394 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The serosa is covered by a simple squamous epithelium called {{c1::mesothelium}}
- **Davi, rodada 1 (2026-10-05):** “imagem”
- **Card na rodada 2:** The serosa is covered by a simple squamous epithelium called {{c1:: mesothelium }}
- **Davi, rodada 2 (2026-10-13):** “poderia ter imagem, nem que fosse gerada pelo chat”
- **Davi, rodada 3 (2026-10-22):** “IMAGEM RUIM”
- **Card depois (vivo):** The serosa is covered by a simple squamous epithelium called {{c1::mesothelium}}
  - **Verso depois:** The mesothelium is the thin outer epithelial sheet facing the peritoneal cavity; it secretes lubricating fluid. / / [IMG 7622bdccaa72d53bb3fae2ccf397d414.webp]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023362817 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Gastric stem cells sit in the {{c1::isthmus}}, between the pit and the gland
- **Davi, rodada 1 (2026-10-05):** “imagem inadequada, todas as desse livro”
- **Card depois (vivo):** Gastric stem cells sit in the {{c1::isthmus}}, between the pit and the gland
  - **Verso depois:** - Daughter cells move up to the surface or down into the gland / / [IMG st-isthmus.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023364242 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Parietal cells lie among {{c1::mucous neck}} cells and in the deeper part of the gland
- **Davi, rodada 1 (2026-10-05):** “imagem”
- **Card depois (vivo):** Parietal cells lie among {{c1::mucous neck}} cells and in the deeper part of the gland
  - **Verso depois:** - Arrow: large, pale parietal cell with a central nucleus / / [IMG st-parietal-neck.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023819869 (2026-uc08-fisiologia-08-motilidade-i)
- **Card antes:** During peristalsis, the circular muscle on the oral side of the bolus {{c1::contracts}} while the segment just aboral to it relaxes
- **Davi, rodada 1 (2026-10-05):** “há a resposta por oposição aqui”
- **Card depois (vivo):** During peristalsis, circular muscle immediately behind the bolus {{c1::contracts}}.
  - **Verso depois:** Behind the bolus, excitatory motor neurons release acetylcholine and substance P. Ahead of it, inhibitory neurons release VIP and NO.
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1791054012719 (2026-uc03-grand-round-21-diabetes)
- **Card antes:** Chronic hyperinsulinemia can {{c1:: downregulate }} insulin receptors.
- **Davi, rodada 1 (2026-10-06):** “muitas palavras no cloze”
- **Card depois (vivo):** Chronic hyperinsulinemia can {{c1::downregulate}} insulin receptors.
  - **Verso depois:** - Obesity alters insulin signaling at receptor and post-receptor steps. / - Lipid excess and inflammatory signals interfere with insulin action in muscle, liver and adipose tissue. / - Receptor downregulation alone does not explain the full defect.
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1790972065436 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** The esophageal hiatus is formed by the {{c1:: right crus }} of the diaphragm, which acts as an external lower esophageal sphincter
- **Davi, rodada 1 (2026-10-13):** “faltou uma explicação do que é esse right crus”
- **Card depois (vivo):** The esophageal hiatus is formed by the {{c1::right crus}} of the diaphragm, which acts as an external lower esophageal sphincter
  - **Verso depois:** - The crura are tendinous bands that anchor the diaphragm to the upper lumbar vertebrae; the right crus (L1–L3) is longer and stronger than the left (L1–L2) / - Its fibers split to loop around the esophageal hiatus (T10) like a sling, so it pinches the esophagus on inspiration / / [IMG nebli-moore-f
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1790972067760 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** What is the most common location for a gastric ulcer ? {{c1:: Lesser curvature }}
- **Davi, rodada 1 (2026-10-13):** “tab tem que explicar o h pylori”
- **Card depois (vivo):** What is the most common location for a gastric ulcer? / {{c1::Lesser curvature}}
  - **Verso depois:** - Usually at the transition zone between the gastric body and the antrum / / - Glands in body produce HCl, glands in antrum produce gastrin / - Transitional zone provides optimal microenvironment for H. pylori proliferation / [IMG 4513cb2d9ae02edfe3503b8f011d67ab.png] / / - Lesser curvature of stoma
- **Análise:** [tab] Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.

### Anti-exemplar · note 1790972067861 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** The anterior surface of the stomach is related to the diaphragm, the anterior abdominal wall and the {{c1:: left lobe }} of the liver
- **Davi, rodada 1 (2026-10-13):** “tamanho da imagem poderia ser reduzido, para caber sem eu ter que descer quando abrir o card”
- **Card depois (vivo):** The anterior surface of the stomach is related to the diaphragm, the anterior abdominal wall and the {{c1::left lobe}} of the liver
  - **Verso depois:** - Also the diaphragm and anterior abdominal wall / / [IMG an-stomach-ant.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790972067961 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** The posterior surface of the stomach forms most of the anterior wall of the {{c1:: omental bursa }}
- **Davi, rodada 1 (2026-10-13):** “imagem estranha não entendi bem o que porquê do card também”
- **Card depois (vivo):** The posterior surface of the stomach forms most of the anterior wall of the {{c1::omental bursa}}
  - **Verso depois:** - Also called the lesser sac, a space behind the stomach / / [IMG an-bursa.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790972068062 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** A posterior gastric ulcer may erode into the lesser sac , damaging the {{c1:: splenic }} artery
- **Davi, rodada 1 (2026-10-13):** “imagem não explica”
- **Card depois (vivo):** A posterior gastric ulcer may erode into the lesser sac, damaging the {{c1::splenic}} artery
  - **Verso depois:** - Runs along the upper border of the pancreas, in the stomach bed / / [IMG an-splenic.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790972068360 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** Part of duodenum
- **Davi, rodada 1 (2026-10-13):** “poderia ter dica aqui: parte do duodeno part of the duodenum”
- **Card depois (vivo):** 
- **Análise:** [dica] Falta dica no cloze quando a pergunta é ambígua (parte do duodeno, fase, ramo de qual artéria). Dica curta no próprio cloze, sem entregar.

### Anti-exemplar · note 1790972069412 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** Gallstones that reach the confluence of the common bile and pancreatic ducts at the {{c1:: hepatopancreatic ampulla }} can block both ducts (double-duct sign) causing cholangitis and pancreatitis
- **Davi, rodada 1 (2026-10-13):** “de novo, a imagem contém tudo que deveria ter aqui, mas está genérica o comentário também ficou abaixo da imagem, o que é ruim”
- **Card depois (vivo):** Gallstones that reach the confluence of the common bile and pancreatic ducts at the {{c1::hepatopancreatic ampulla}} can block both ducts (double-duct sign) causing cholangitis and pancreatitis
  - **Verso depois:** - Jaundice plus gallstone pancreatitis / / [IMG an-ampulla.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790972069911 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** The jejunum makes up the proximal {{c1:: two-fifths }} of the small intestine beyond the duodenum
- **Davi, rodada 1 (2026-10-13):** “bom exemplo de card que conjuga duas informações: não precisa de um card pro ileum ser distal three-fifths, porque se sei o card do jejunum já sei o outro”
- **Card depois (vivo):** The jejunum makes up the proximal {{c1::two-fifths}} of the small intestine beyond the duodenum
  - **Verso depois:** - The ileum makes up the distal three-fifths / / [IMG nebli-moore-fig-5-47.png]
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1790972070612 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** The {{c1:: jejunum }} has few, large arterial arcades and long vasa recta
- **Davi, rodada 1 (2026-10-13):** “resposta tava no card, então mudei poderia ter imagem aqui”
- **Davi, rodada 2 (2026-10-22):** “imagem ruim”
- **Card depois (vivo):** The {{c1::jejunum}} has few, large arterial arcades and long vasa recta
  - **Verso depois:** - Ileum: many short arcades, short vasa recta / / [IMG nebli-moore-fig-5-48-bc.png]
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1790972070958 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** Compared with the ileum , the jejunum has a {{c1:: thicker ::thicker / thinner}} wall and a larger caliber
- **Davi, rodada 1 (2026-10-13):** “imagem ruim mt info uma boa imagem tem pouco informação, mas direcionada em específico para o card que contribui excesso de ; e : no comentário”
- **Card depois (vivo):** Compared with the ileum, the jejunum has a {{c1::thicker::thicker / thinner}} wall and a larger caliber
  - **Verso depois:** - Also taller plicae and redder color / - Ileum: thinner, paler, more mesenteric fat
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790972071259 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** Meckel diverticulum arises due to persistence of the {{c1::vitelline duct}}
- **Davi, rodada 1 (2026-10-13):** “os cards de clínica desse deck de anato do esôfago, estômago e intestino delgado ficaram excedentes: é bom que seja um só card de clínica, com a principal informação do assunto. uma informação que vou me lembrar e associar sempre àquela doença. ex: resistência à insulina na DM, autoimunidade no lúpus, skip lesion em chrons... aqui, os cards eram coisas que seria bom ter estudado para realmente trazer. foram cards de clínica, não cards que me dão um conhecimento de uma patologia realmente associada ao conteúdo da aula só com o que poderia saber da aula o foco não é conhecer tudo de uma doença r”
- **Card depois (vivo):** Meckel diverticulum arises due to persistence of the {{c1::vitelline duct}}
  - **Verso depois:** AKA omphalomesenteric duct / / [IMG 05a9661ac68136e7292511f9a6980940.webp] / / [IMG 4d312dd26072007eca47af22e43d3a3a.webp] / / - Rule of 2s: ~2% of people, ~2 feet (60 cm) proximal to the ileocecal valve, ~2 inches long; the most common congenital anomaly of the GI tract
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1790973210308 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-13):** “seta para o local errado”
- **Card depois (vivo):** 
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1790973218382 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** Part of duodenum + vertebral level
- **Davi, rodada 1 (2026-10-13):** “nesse tipo de cloze é bom que tenha dica no card virado antes em específico, algo direto no cloze, tipo: [part of duodenum and height related to the spine), mas mais curto duas ou três palavras para direcionar, porque se não fica mt genérico”
- **Card depois (vivo):** 
- **Análise:** [dica] Falta dica no cloze quando a pergunta é ambígua (parte do duodeno, fase, ramo de qual artéria). Dica curta no próprio cloze, sem entregar.

### Anti-exemplar · note 1790974689756 (2026-uc08-anatomia-02-intestino-grosso-canal-anal)
- **Card antes:** The ascending and descending colon are secondarily {{c1:: retroperitoneal ::peritoneal relation}}
- **Davi, rodada 1 (2026-10-13):** “acho que não era a aula para isso isso não veio da aula portanto, não sei o cronograma também consta uma aula disso por isso vou suspender e talvez possa voltar depois”
- **Card depois (vivo):** The ascending and descending colon are secondarily {{c1::retroperitoneal::peritoneal relation}}
  - **Verso depois:** - Fixed to the posterior abdominal wall / - The cecum, transverse and sigmoid colon are intraperitoneal / / [IMG nebli-moore-fig-5-43.png]
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1790974691958 (2026-uc08-anatomia-02-intestino-grosso-canal-anal)
- **Card antes:** Behind the apex of the sigmoid mesocolon , on the left common iliac vessels, lies the {{c1:: left ureter }}
- **Davi, rodada 1 (2026-10-13):** “imagem poderia ser um pouco menor card escrito de forma estranha um pouco”
- **Card depois (vivo):** Behind the apex of the sigmoid mesocolon, on the left common iliac vessels, lies the {{c1::left ureter}}
  - **Verso depois:** - Surgical landmark when mobilizing the sigmoid colon / / [IMG nebli-moore-fig-6-31.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790974697004 (2026-uc08-anatomia-02-intestino-grosso-canal-anal)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-13):** “excesso de informações aqui, fica difícil identificar o que o card fala sobre anal valve seria bom achar outra imagem para cobrar isso card ficou estranho a IO”
- **Card depois (vivo):** 
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1790974697406 (2026-uc08-anatomia-02-intestino-grosso-canal-anal)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-13):** “esse card possui um excesso de informações, não fica claro o que tenho que saber ou não a imagem fica muito pequena e os detalhes se perdem”
- **Card depois (vivo):** 
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790978739486 (2026-uc08-anatomia-02-intestino-grosso-canal-anal)
- **Card antes:** The upper ends of the anal columns mark the {{c1:: anorectal }} junction, where the rectum becomes the anal canal
- **Davi, rodada 1 (2026-10-13):** “imagem com mt info”
- **Card depois (vivo):** The upper ends of the anal columns mark the {{c1::anorectal}} junction, where the rectum becomes the anal canal
  - **Verso depois:** - Puborectalis sling makes the anorectal angle here / / [IMG an-anorectal.jpg]
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1790979869136 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Mucous neck cells secrete a mucin different from that of the surface cells, with {{c1:: antibiotic }} properties
- **Davi, rodada 1 (2026-10-13):** “imagem”
- **Card depois (vivo):** Mucous neck cells secrete a mucin different from that of the surface cells, with {{c1::antibiotic}} properties
  - **Verso depois:** - Surface mucin protects against acid / / [IMG st-mucneck.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790979869985 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The gastric hormone that increases appetite is {{c1:: ghrelin }}
- **Davi, rodada 1 (2026-10-13):** “card estranho + comentário estranho esses estranhos não sei bem o que são, mas quero manter o conteúdo e trocar o card”
- **Card depois (vivo):** The gastric hormone that increases appetite is {{c1::ghrelin}}
  - **Verso depois:** - Made by enteroendocrine cells of the gastric fundus/body / - Also stimulates GH release
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1790980015534 (2026-uc03-microbiologia-35-patogenicidade-bacteriana)
- **Card antes:** H. pylori produces {{c1::urease::enzyme}}, which alkalinizes the local environment, enabling bacterial survival
- **Davi, rodada 1 (2026-10-13):** “tab ficou ruim explicaçao zuada”
- **Card depois (vivo):** H. pylori produces {{c1::urease::enzyme}}, which alkalinizes the local environment, enabling bacterial survival
  - **Verso depois:** Urea → NH3 and CO2 → NH3 combines with H+→ increases the pH → stimulates gastrin release → excess acid production and ulcer formation / [IMG 2958275289630e8ea4e8dfa84fcc196c.webp] / / [IMG 58ac69594902a9a78c19af98fe8eb023.webp] / / [IMG b9a7f0771521c69a6ee7f4985578118e.webp]
- **Análise:** [tab] Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.

### Anti-exemplar · note 1790980913981 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** Mucus is secreted into the GI tract via {{c1:: Brunner }} glands in the duodenum
- **Davi, rodada 1 (2026-10-13):** “card dá a impressão de que é só assim o que é errado há outras formas de secretar muco”
- **Card depois (vivo):** In the duodenum, submucosal {{c1::Brunner}} glands secrete alkaline mucus that neutralizes gastric acid
  - **Verso depois:** [IMG e4793eaf6f95edad5055c9014b757e35.png] / / Only the duodenum has glands in the submucosa (besides the esophagus) / - Mucus is also made by goblet cells along the intestine and by surface mucous cells in the stomach
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1790980914355 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** The villi and plicae in this H&E section identify the {{c1:: small intestine }}
- **Davi, rodada 1 (2026-10-13):** “aqui não deveria ter descrição: acerto sem ver a imagem dá para ser um IO melhor sem texto”
- **Card depois (vivo):** What part of the GI tract is shown in the image below? / [IMG paste-3d75c628a54f5825cea895dd00967de1fd6489e7.png] / {{c1::Small intestine}}
  - **Verso depois:** - Plica = fold of mucosa + submucosa / - Villi = mucosa only
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1790981514202 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-13):** “card não indica nada o cloze não tem seta apontando”
- **Card depois (vivo):** 
- **Análise:** [dica] Falta dica no cloze quando a pergunta é ambígua (parte do duodeno, fase, ramo de qual artéria). Dica curta no próprio cloze, sem entregar.

### Anti-exemplar · note 1790981514326 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-13):** “MESMA coisa já comentada em outros cards desse slide”
- **Card depois (vivo):** 
- **Análise:** [repetido] Card repetido ou muito parecido com outro: confunde e gasta revisão. Um fato, um card; o outro aspecto vai no verso ou em card com ganho próprio.

### Anti-exemplar · note 1790981515925 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-13):** “NÃO HÁ INDICAÇÃO DA ESTRUTURA NO CARD”
- **Card depois (vivo):** 
- **Análise:** [dica] Falta dica no cloze quando a pergunta é ambígua (parte do duodeno, fase, ramo de qual artéria). Dica curta no próprio cloze, sem entregar.

### Anti-exemplar · note 1790981519924 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** From the lymph , chylomicrons reach the blood through the {{c1:: thoracic duct }}
- **Davi, rodada 1 (2026-10-13):** “card com cloze num lugar mt fácil o cloze cairia melhor em [thoracic duct]”
- **Card depois (vivo):** From the lymph, chylomicrons reach the blood through the {{c1::thoracic duct}}
  - **Verso depois:** - Drains at the junction of the left subclavian and internal jugular veins
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1790981522079 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** The {{c1:: ileocolic ::SMA branch}} artery supplies the terminal ileum, the cecum and, through its appendicular branch, the appendix
- **Davi, rodada 1 (2026-10-13):** “aqui poderia ter dica também tipo branch of the SMA”
- **Card depois (vivo):** The {{c1::ileocolic::SMA branch}} artery supplies the terminal ileum, the cecum and, through its appendicular branch, the appendix
  - **Verso depois:** Ileocolic is the last branch of the SMA / / [IMG nebli-moore-fig-5-54.png]
- **Análise:** [dica] Falta dica no cloze quando a pergunta é ambígua (parte do duodeno, fase, ramo de qual artéria). Dica curta no próprio cloze, sem entregar.

### Anti-exemplar · note 1790981522327 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** The middle colic artery, a branch of the superior mesenteric artery, supplies the {{c1:: transverse }} colon
- **Davi, rodada 1 (2026-10-13):** “faltou negrito em superior mesenteric artery”
- **Card depois (vivo):** The middle colic artery, a branch of the superior mesenteric artery, supplies the {{c1::transverse}} colon
  - **Verso depois:** Middle colic runs in the transverse mesocolon / / [IMG nebli-moore-fig-5-54.png]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1790981524526 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** Vessel · colonic arcade
- **Davi, rodada 1 (2026-10-13):** “aqui poderia ter uma dica, tipo: vaso”
- **Card depois (vivo):** 
- **Análise:** [dica] Falta dica no cloze quando a pergunta é ambígua (parte do duodeno, fase, ramo de qual artéria). Dica curta no próprio cloze, sem entregar.

### Anti-exemplar · note 1790981524777 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-13):** “ficou ruim de ver tentar achar outro em deck extero, netter ou imagem da internet para cobrir essa informação melhor seta não aponta certo”
- **Card depois (vivo):** 
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1790981524902 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** The {{c1:: marginal artery }} (of Drummond) runs along the mesenteric border of the colon and joins the SMA and IMA territories
- **Davi, rodada 1 (2026-10-13):** “linguagme estranha, que não induz”
- **Card depois (vivo):** The {{c1::marginal artery}} (of Drummond) runs along the mesenteric border of the colon and joins the SMA and IMA territories
  - **Verso depois:** - Fed by the colic arteries; if one territory fails, the other can supply the colon / / [IMG nebli-moore-fig-5-54.png]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1790981526502 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** The middle rectal artery is a branch of the {{c1:: internal iliac }} artery
- **Davi, rodada 1 (2026-10-13):** “imagem com mt info comentário com IA ; : ,”
- **Card depois (vivo):** The middle rectal artery is a branch of the {{c1::internal iliac}} artery
  - **Verso depois:** - Superior rectal: IMA / - Middle rectal: internal iliac / - Inferior rectal: internal pudendal / / [IMG an-midrectal.jpg]
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1790981526625 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** The inferior rectal artery is a branch of the {{c1::internal pudendal}} artery
- **Davi, rodada 1 (2026-10-13):** “imagem nada a ver aqui”
- **Card depois (vivo):** The inferior rectal artery is a branch of the {{c1::internal pudendal}} artery
  - **Verso depois:** - Supplies the anal canal below the pectinate line / / [IMG an-infrectal.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790999837929 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** {{c1:: Haustrations }} are slow segmental contractions of the proximal colon that mix contents and expose them to the mucosa for water absorption
- **Davi, rodada 1 (2026-10-13):** “outro exemplo de falta de negrito + falta de escrita que capta a atenção”
- **Card depois (vivo):** {{c1::Haustrations}} are slow segmental contractions of the proximal colon that mix contents and expose them to the mucosa for water absorption
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1790999838304 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** Rectal distension triggers a sacral reflex through the {{c1:: pelvic }} nerves that contracts the rectum and relaxes the internal anal sphincter
- **Davi, rodada 1 (2026-10-13):** “imagem poderia ser memlhor e mais direcionada especificamente ao conteúdo do card”
- **Card depois (vivo):** Rectal distension triggers a sacral reflex through the {{c1::pelvic}} nerves that contracts the rectum and relaxes the internal anal sphincter
  - **Verso depois:** - External anal sphincter (pudendal, voluntary) decides when
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791000311952 (2026-uc08-fisiologia-05-digestao-absorcao-nutrientes)
- **Card antes:** Enterocytes absorb dietary {{c1:: heme }} intact, with its iron still inside the {{c2:: porphyrin }} ring
- **Davi, rodada 1 (2026-10-13):** “card estranho”
- **Card depois (vivo):** Enterocytes absorb dietary {{c1::heme}} intact, with its iron still inside the {{c2::porphyrin}} ring
  - **Verso depois:** - Absorbed better than non-heme iron / / [IMG 3a35111470df6ac145ebfb635e652424.png]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791000315902 (2026-uc03-microbiologia-39-homem-ambiente-microrganismo)
- **Card antes:** What proteins are tight junctions composed of? {{c1::Claudins and occludins::2}}
- **Davi, rodada 1 (2026-10-13):** “esse tipo de card é para ser rosa”
- **Card depois (vivo):** What proteins are tight junctions composed of? / {{c1::Claudins and occludins::2}}
  - **Verso depois:** Claudins set charge and size selectivity of the paracellular pathway. After a meal, SGLT1 activity opens tight junctions via MLCK
- **Análise:** [cor] Cor errada para a importância (HY rosa, detalhe verde). A cor segue a rubrica: HY 1–2 e pilares verdes, detalhe rosa.

### Anti-exemplar · note 1791014713674 (2026-uc08-fisiologia-06-secrecao-gastrica)
- **Card antes:** Acute gastritis may arise with {{c1:: NSAID }} use due to decreased {{c2:: PGE 2 }}
- **Davi, rodada 1 (2026-10-13):** “tab ruim”
- **Card depois (vivo):** Acute gastritis may arise with {{c1::NSAID}} use due to decreased {{c2::PGE2}}
  - **Verso depois:** Prostaglandins decrease acid production, stimulate mucus/HCO3- production, and increase blood flow / / [IMG 6c4b329864adb2b4c6aca3e931fde848.webp] / / [IMG b9a7f0771521c69a6ee7f4985578118e.webp]
- **Análise:** [tab] Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.

### Anti-exemplar · note 1791014714650 (2026-uc08-fisiologia-06-secrecao-gastrica)
- **Card antes:** Of the three phases of gastric secretion, the {{c1::intestinal::phase}} phase accounts for only ~10% of gastric acid secretion and mostly brakes it
- **Davi, rodada 1 (2026-10-13):** “faltou uma dica no cloze tipo: fase intestinal reescreve o card e vê como poderia ser”
- **Card depois (vivo):** Of the three phases of gastric secretion, the {{c1::intestinal::phase}} phase accounts for only ~10% of gastric acid secretion and mostly brakes it
  - **Verso depois:** Cephalic ~30%, gastric ~60%, intestinal ~10%; the intestinal phase mostly brakes acid secretion / / [IMG nebli-uc08-fi06-p03f.png]
- **Análise:** [dica] Falta dica no cloze quando a pergunta é ambígua (parte do duodeno, fase, ramo de qual artéria). Dica curta no próprio cloze, sem entregar.

### Anti-exemplar · note 1791014717050 (2026-uc08-fisiologia-06-secrecao-gastrica)
- **Card antes:** In the duodenum, acid releases {{c1:: secretin }}, which also stimulates pepsinogen secretion by chief cells
- **Davi, rodada 1 (2026-10-13):** “comentário não anking card com escrita estranha: acid releases secretin”
- **Card depois (vivo):** In the duodenum, acid releases {{c1::secretin}}, which also stimulates pepsinogen secretion by chief cells
  - **Verso depois:** - Minor route; secretin mainly inhibits acid secretion
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791023299366 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** Paneth cells have large apical {{c1:: eosinophilic }} secretory granules
- **Davi, rodada 1 (2026-10-13):** “card com informação não storytelling: não aprendo nada, só decoro algo meio inutil”
- **Card depois (vivo):** Paneth cells at the crypt base store {{c1::lysozyme}} and defensins in large eosinophilic granules, protecting the stem cells
  - **Verso depois:** Granules hold lysozyme, phospholipase A2 and defensins / / / / [IMG bt04-paneth.png]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791023303193 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** Goblet cells of the large intestine become more numerous toward the {{c1:: rectum }}
- **Davi, rodada 1 (2026-10-13):** “faltando negrito e itálico em card autoral”
- **Davi, rodada 2 (2026-10-22):** “NEGRITO E ITÁLICO”
- **Card depois (vivo):** Goblet cells of the large intestine become more numerous toward the {{c1::rectum}}
  - **Verso depois:** More mucus where feces are most solid / / / / [IMG bt04-colon-mucosa.png]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791023353192 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The gingiva and hard palate have {{c1:: masticatory }} mucosa, with keratinized epithelium
- **Davi, rodada 1 (2026-10-13):** “IMAGEM”
- **Card depois (vivo):** The gingiva and hard palate have {{c1::masticatory}} mucosa, with keratinized epithelium
  - **Verso depois:** - Bound to bone, resists abrasion
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023354693 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The parotid gland has exclusively {{c1:: serous }} acini
- **Davi, rodada 1 (2026-10-13):** “não precisa de imagem aqui, ficou excessivo poderia ter uma tabela comparando as glândulas aqui”
- **Davi, rodada 2 (2026-10-22):** “poderia ter uma tabela comparando as glândulas aqui bom exemplo de tabela seria bom uma imagem com localização das glândulas imagem clara e bom”
- **Card depois (vivo):** The parotid gland has exclusively {{c1::serous}} acini
  - **Verso depois:** - Watery, amylase-rich saliva / / ParotidSubmandibularSublingualAciniexclusively serousmixed, mostly serousmixed, mostly mucousShare of saliva~25%~70%~5% / / [IMG 392281736e881dcc1c4cfebdbd375f80.jpg]
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791023354943 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** About two-thirds of all saliva comes from the {{c1:: submandibular }} glands
- **Davi, rodada 1 (2026-10-13):** “imagem zuada em vários cards, vou pagar de avisar”
- **Card depois (vivo):** About two-thirds of all saliva comes from the {{c1::submandibular}} glands
  - **Verso depois:** - Mixed gland, mostly serous / / [IMG 392281736e881dcc1c4cfebdbd375f80.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023355569 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Serous cells are grouped into round secretory units called {{c1:: acini }}
- **Davi, rodada 1 (2026-10-13):** “imagem zuada card com escrita estranha”
- **Card depois (vivo):** Serous cells are grouped into round secretory units called {{c1::acini}}
  - **Verso depois:** - Mucous cells usually form tubules / / [IMG sal-serous-acinus.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023355691 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Salivary cells with pale, foamy cytoplasm and flattened basal nuclei are {{c1:: mucous }} cells
- **Davi, rodada 1 (2026-10-13):** “card estranho ajustar esses cards estranhos para serem anking like melhor e realmente me ensinarem algo”
- **Card depois (vivo):** Salivary cells with pale, foamy cytoplasm and flattened basal nuclei are {{c1::mucous}} cells
  - **Verso depois:** - Stored mucinogen pushes the nucleus against the base / / [IMG sal-mucous-cell.jpg]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791023355944 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Contractile cells wrapped around acini, inside the basal lamina, are {{c1:: myoepithelial }} cells
- **Davi, rodada 1 (2026-10-13):** “cards autorais poderiam ter negrito + sublinhado no padrão anking”
- **Card depois (vivo):** Contractile cells wrapped around acini, inside the basal lamina, are {{c1::myoepithelial}} cells
  - **Verso depois:** - Squeeze secretion into the ducts
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791023356892 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The lamina propria is {{c1:: loose }} connective tissue rich in vessels, lymphatics and lymphocytes
- **Davi, rodada 1 (2026-10-13):** “imagem ruim”
- **Card depois (vivo):** The lamina propria is {{c1::loose}} connective tissue rich in vessels, lymphatics and lymphocytes
  - **Verso depois:** - Sits right under the epithelium / / [IMG wl-lp.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023357519 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** Lymphoid nodules and free immune cells in the gut mucosa and submucosa form the {{c1:: MALT }}
- **Davi, rodada 1 (2026-10-13):** “imagem ruim + card com escrita estranha”
- **Card depois (vivo):** Lymphoid nodules and free immune cells in the gut mucosa and submucosa form the {{c1::MALT}}
  - **Verso depois:** - Example: Peyer patches in the ileum / / [IMG wl-malt.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023357791 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The esophageal glands , which secrete lubricating mucus, lie in the {{c1:: submucosa }}
- **Davi, rodada 1 (2026-10-13):** “comentário zuado nesse estilo”
- **Card depois (vivo):** The esophageal glands, which secrete lubricating mucus, lie in the {{c1::submucosa}}
  - **Verso depois:** [IMG wl-esoph-gland.jpg]
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791023359842 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The pyloric sphincter is a thickening of the {{c1:: middle circular }} layer of the gastric muscularis
- **Davi, rodada 1 (2026-10-13):** “imagem”
- **Card depois (vivo):** The pyloric sphincter is a thickening of the {{c1::middle circular}} layer of the gastric muscularis
  - **Verso depois:** - The circular layer also forms the other GI sphincters / / [IMG st-pylorus.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791023360217 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** The gastric surface epithelium dips into the lamina propria to form the {{c1:: gastric pits }}
- **Davi, rodada 1 (2026-10-13):** “card estranho não ensina algo”
- **Card depois (vivo):** Gastric glands open into funnel-shaped invaginations of the surface epithelium called {{c1::gastric pits}} (foveolae)
  - **Verso depois:** - Surface mucous cells line the pits; parietal and chief cells lie deeper in the glands / [IMG st-pits.jpg]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791023365216 (2026-uc08-biologia-tecidual-03-estrutura-estomago)
- **Card antes:** In the neck of gastric glands, scattered among parietal cells, {{c1:: mucous neck }} cells secrete a less alkaline mucus
- **Davi, rodada 1 (2026-10-13):** “imagem zuada escrita estranha sem storytelling”
- **Card depois (vivo):** In the neck of gastric glands, scattered among parietal cells, {{c1::mucous neck}} cells secrete a less alkaline mucus
  - **Verso depois:** [IMG st-mucneck.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791052257826 (2026-uc08-fisiologia-08-motilidade-i)
- **Card antes:** After contraction, {{c1:: SERCA }} pumps Ca²⁺ back into the sarcoplasmic reticulum
- **Davi, rodada 1 (2026-10-13):** “card sem negrito”
- **Card depois (vivo):** After contraction, {{c1::SERCA}} pumps Ca²⁺ back into the sarcoplasmic reticulum
  - **Verso depois:** - Smooth muscle also pumps Ca²⁺ out of the cell / - Relaxation needs myosin light-chain phosphatase
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791054016595 (2026-uc03-grand-round-21-diabetes)
- **Card antes:** Histology of type 1 diabetes mellitus demonstrates islets with {{c1:: leukocytic infiltrate }}
- **Davi, rodada 1 (2026-10-13):** “nesse caso, o (inflammation) pode vir no comentário a explicação no card não fica tão legal sei que é anking, mas é um padrão que gostaria de anotar pros autorais saberem”
- **Card depois (vivo):** Histology of type 1 diabetes mellitus demonstrates islets with {{c1::leukocytic infiltrate}}
  - **Verso depois:** [IMG ba7dd1c2a1a69819d61732128b2ccec5.jpg][IMG 22993d36835f411dc6956c53337acb76.webp] / / T cells and macrophages invade the islets in type 1 / / [IMG nebli-robbins-fig-24-33a.png]
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791557940633 (2026-uc03-microbiologia-43-biologia-fungos)
- **Card antes:** {{c1:: Yeasts::Yeasts/Molds }} form creamy, pasty colonies, whereas {{c1:: molds::ye asts/molds }} form cottony, velvety or powdery ones
- **Davi, rodada 1 (2026-10-13):** “card pode ter um só cloze e dica tipo yeast/mold no cloze antes de eu tentar acertar a dica guia assim o próprio card nn entrega a resposta tipo como deixei”
- **Card depois (vivo):** {{c1::Yeasts::Yeasts/Molds}} form creamy, pasty colonies, whereas {{c1::molds::yeasts/molds}} form cottony, velvety or powdery ones
  - **Verso depois:** - Telling them apart is the first step in culture identification / / [IMG nebli-trabulsi-fig-64-1-3.png]
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1791557945582 (2026-uc03-microbiologia-44-micoses-cutaneas)
- **Card antes:** {{c2::Dermatophytes::Which cutaneous fungi}} contain {{c1:: keratinase ::enzyme}}, allowing them to subsist off keratin , a protein resistant to most organisms
- **Davi, rodada 1 (2026-10-13):** “card no deck errado era para estar no deck de dermatoses cutâneas”
- **Card depois (vivo):** {{c2::Dermatophytes::Which cutaneous fungi}} contain {{c1::keratinase::enzyme}}, allowing them to subsist off keratin, a protein resistant to most organisms
  - **Verso depois:** This is why dermatophytes are commonly found in the skin (tinea - "ringworm") and nails (onychomycosis)
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1791575024496 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** {{c1::Acetylcholine}} and stretch of the gut wall raise slow-wave amplitude , so more spike potentials ride on each wave
- **Davi, rodada 1 (2026-10-13):** “FALTAM NEGRITOS voltar colocando negritos em todos os autorais que faltam, seguindo o padrão do anking em detalhes”
- **Card depois (vivo):** {{c1::Acetylcholine}} and stretch of the gut wall raise slow-wave amplitude, so more spike potentials ride on each wave
  - **Verso depois:** Norepinephrine lowers slow-wave amplitude and spike frequency
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791575029793 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** Acid and digested nutrients in the duodenum release hormones that slow gastric emptying by relaxing the {{c1::stomach}} and contracting the {{c2::pylorus}}
- **Davi, rodada 1 (2026-10-13):** “negrito”
- **Card depois (vivo):** Acid and digested nutrients in the duodenum release hormones that slow gastric emptying by relaxing the {{c1::stomach}} and contracting the {{c2::pylorus}}
  - **Verso depois:** - Acid releases secretin; nutrients release CCK, GIP, GLP-1 and PYY / - Emptying matches what the duodenum can process / / [IMG nebli-uc08-fi09-p10f.png]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791575032019 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** Conditions that cause {{c1::vomiting}} include infection, medication, vestibular dysfunction, and chemoradiation
- **Davi, rodada 1 (2026-10-13):** “NEGRITO”
- **Card depois (vivo):** Conditions that cause {{c1::vomiting}} include infection, medication, vestibular dysfunction, and chemoradiation
  - **Verso depois:** Drugs and chemoradiation act on the area postrema; motion sickness comes through the vestibular system; stomach distension through vagal afferents
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791575683767 (2026-uc03-microbiologia-43-biologia-fungos)
- **Card antes:** In {{c1:: sick building }} syndrome, indoor fungi cause fatigue, headache and airway irritation in more than 20% of occupants
- **Davi, rodada 1 (2026-10-13):** “card mal feito probabilidade zuada em quê agrega na minha formação?”
- **Card depois (vivo):** (nota apagada)
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791575686544 (2026-uc03-microbiologia-43-biologia-fungos)
- **Card antes:** Fungal mitochondria have {{c1:: flattened }} (plate-like) cristae
- **Davi, rodada 1 (2026-10-13):** “poderai ter imagem aqui”
- **Card depois (vivo):** (nota apagada)
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791575690219 (2026-uc03-microbiologia-43-biologia-fungos)
- **Card antes:** Mucor , Rhizopus and Lichtheimia now belong to the phylum {{c1:: Mucoromycota }}
- **Davi, rodada 1 (2026-10-13):** “esse tipo de card é melhor com visualidade: mostrar a árvore genealógica”
- **Card depois (vivo):** (nota apagada)
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791625436408 (2026-uc03-imunologia-64-hipersensibilidade)
- **Card antes:** Type {{c2:: IV }} HSRs may occur via delayed-type hypersensitivity , which involves CD4 + T-cells
- **Davi, rodada 1 (2026-10-13):** “card do conteúdo errado”
- **Card depois (vivo):** Type {{c2::IV}} HSRs may occur via delayed-type hypersensitivity, which involves CD4+ T-cells
  - **Verso depois:** Sensitized helper T cells encounter antigen and release cytokines / [IMG a80f3b267d2602619a54f6b55ec55750.webp] / / [IMG 075aa85beb288f3ca73ad0a7a5517a33.png]
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1791625436533 (2026-uc03-grand-round-03-espondilodiscite-tuberculosa)
- **Card antes:** What type of hypersensitivity reaction is a tuberculin skin test (PPD)? {{c1::Type IV HSR (Th 1 mediated)}}
- **Davi, rodada 1 (2026-10-13):** “card era para ser de outro deck”
- **Card depois (vivo):** What type of hypersensitivity reaction is a tuberculin skin test (PPD)? / {{c1::Type IV HSR (Th1 mediated)}}
  - **Verso depois:** This is to determine tuberculosis infection status / [IMG b7ac85be73980eae7e5b834b46b4cdd6.webp][IMG a80f3b267d2602619a54f6b55ec55750.webp] /
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1791626776803 (2026-uc03-microbiologia-44-micoses-cutaneas)
- **Card antes:** Dermatophytes rarely invade below the {{c1::stratum corneum}}
- **Davi, rodada 1 (2026-10-13):** “imagem”
- **Davi, rodada 2 (2026-10-22):** “bela imagem”
- **Card depois (vivo):** Dermatophytes rarely invade below the {{c1::stratum corneum}}
  - **Verso depois:** - Itching and scaling are a host reaction to fungal products, not deep invasion / [IMG 2b5e7156d2ac6df8a3aaf0a737822a1c.webp]
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791626778904 (2026-uc03-microbiologia-44-micoses-cutaneas)
- **Card antes:** Dermatophyte onychomycosis usually starts at the {{c1::distal}} nail edge, whereas Candida starts at the proximal nail fold
- **Davi, rodada 1 (2026-10-13):** “já pontuei 300 cards nesse estilo, que são ruins”
- **Card na rodada 2:** Dermatophyte onychomycosis usually starts at the {{c1::distal}} nail edge, whereas Candida starts at the {{c1::proximal}} nail fold
- **Davi, rodada 2 (2026-10-15):** “ajustei”
- **Card depois (vivo):** Dermatophyte onychomycosis usually starts at the {{c1::distal}} nail edge, whereas Candida starts at the {{c1::proximal}} nail fold
  - **Verso depois:** - Candida nail infection often comes with paronychia
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791627550702 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** Phosphorylation can switch a transcription factor off by blocking its {{c1::DNA binding}} or by keeping it out of the {{c2::nucleus}}
- **Davi, rodada 1 (2026-10-13):** “card repetido, não?”
- **Card na rodada 2:** Phosphorylation keeps FOXO1 out of the {{c1:: nucleus }}, turning this transcription factor off
- **Davi, rodada 2 (2026-10-22):** “card mal escrito não aparece nada”
- **Davi, rodada 3 (2026-10-23):** “exemplo de card que poderia ter uma consequência, já em sequência, sobre o que acontece quando ele não é transcrito, ajudando a decorar mais algo sem custo precisamos usar mais o conceito de custo-efetividade”
- **Card depois (vivo):** Insulin, via AKT, phosphorylates FOXO1 and keeps it out of the {{c1::nucleus}}, so {{c2::gluconeogenic}} genes stay off
  - **Verso depois:** - Moving a transcription factor out of the nucleus switches genes off fast, without degrading it / - In fasting, low insulin lets FOXO1 return to the nucleus and turn gluconeogenesis on
- **Análise:** [repetido] Card repetido ou muito parecido com outro: confunde e gasta revisão. Um fato, um card; o outro aspecto vai no verso ou em card com ganho próprio. Aqui: Fato isolado (FOXO1 fora do núcleo); Davi pediu a consequência em sequência: custo-efetividade é carregar o efeito (genes gliconeogênicos desligados) no mesmo card.

### Anti-exemplar · note 1791628672372 (2026-uc03-microbiologia-48-micoses-subcutaneas)
- **Card antes:** Subcutaneous mycoses begin when saprobic fungi from soil or plants are {{c1::implanted}} through a skin wound
- **Davi, rodada 1 (2026-10-13):** “card com escrita estranha”
- **Card na rodada 2:** Soil or plant fungi implanted into the dermis and subcutis by a penetrating injury cause {{c1:: subcutaneous }} mycoses
- **Davi, rodada 2 (2026-10-22):** “de novo, o card aqui ficou com cloze em algo que não é para ser decorado, mas entendido NEGRITO isso é algo específico tb de subcutânea? cutânea não tem tb?”
- **Card depois (vivo):** Soil or plant fungi implanted into the dermis and subcutis by a penetrating injury cause {{c1::subcutaneous}} mycoses
  - **Verso depois:** - Dermatophytes also enter through small skin breaks, but they stay in the keratin layer; subcutaneous agents are pushed deep by a thorn or splinter / - The fungus then grows in the dermis and subcutis near the wound; some spread along lymphatics
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791628674449 (2026-uc03-microbiologia-48-micoses-subcutaneas)
- **Card antes:** At 25ºC , Sporothrix conidia cluster at the tip of the conidiophore in a {{c1::daisy}}-like pattern
- **Davi, rodada 1 (2026-10-13):** “imagem”
- **Card depois (vivo):** (nota apagada)
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791648193118 (2026-uc03-microbiologia-28-pratica-1)
- **Card antes:** Cocci that stay together in cubic packets after dividing are called {{c1::sarcinae}}
- **Davi, rodada 1 (2026-10-13):** “poderia ter imagem boa disso”
- **Card depois (vivo):** Cocci that stay together in cubic packets after dividing are called {{c1::sarcinae}}
  - **Verso depois:** - The arrangement reflects the planes in which the cells divide / / [IMG nebli-sarcina-pacote-cubico.svg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791664582151 (2026-uc03-biologia-molecular-29-operon-procariotos)
- **Card antes:** Bound Lac repressor lowers lac operon transcription about {{c1::1000}}-fold
- **Davi, rodada 1 (2026-10-13):** “escrita estranha + sem negrito + faltou ensinar e colocar cloze que pede para lembrar algo”
- **Card depois (vivo):** Binding of the Lac repressor to the operator reduces transcription of the {{c1::lac operon}} by about 1000-fold
  - **Verso depois:** The operator-bound repressor blocks productive RNA polymerase passage; rare basal transcription still makes a few β-galactosidase molecules.
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791716411684 (2026-uc03-patologia-47-inflamacao-granulomatosa)
- **Card antes:** Granulomas expand partly through continued {{c1::monocyte recruitment}}
- **Davi, rodada 1 (2026-10-13):** “tab esquisito”
- **Card depois (vivo):** Granulomas expand partly through continued {{c1::monocyte recruitment}}
  - **Verso depois:** - Recruited monocytes differentiate into tissue macrophages.
- **Análise:** [tab] Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.

### Anti-exemplar · note 1791730463385 (2026-uc03-microbiologia-34-genetica-bacteriana)
- **Card antes:** The bacterial chromosome is packed into a compact {{c1::nucleoid}}, which has no membrane around it
- **Davi, rodada 1 (2026-10-13):** “detalhe deixou card mt grande sem necessidade "through DNA interaction with the proteins HU and H-NS" isso aqui é meio away”
- **Card depois (vivo):** The bacterial chromosome is packed into a compact {{c1::nucleoid}}, which has no membrane around it
  - **Verso depois:** - Proteins such as HU and H-NS help compact it
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1791762418521 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** A drug whose curve is shifted right and has a lower plateau has lower potency and lower {{c1::efficacy}}
- **Davi, rodada 1 (2026-10-13):** “card mal feito cobra mal relembrar conceito é quase um card perdido: só gasta meu tempo um bom card cobraria diferença de potência e eficácia, relação de mover para direita ou para esquerda ou pra cima e pra baixo, tentando deixar intuitivo essa pegada de car”
- **Card depois (vivo):** On a dose-response curve, a shift to the right means lower {{c1::potency::potency/efficacy}}, whereas a lower plateau means lower {{c1::efficacy::potency/efficacy}}
  - **Verso depois:** - Potency = dose needed for a given effect (EC50); efficacy = maximal effect (Emax) / [IMG nebli-fa01-antagonista-competitivo.png]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares. Aqui: Cobra 'eficácia' numa curva sem ensinar a diferença potência × eficácia; o card bom pediria a relação (direita = menos potente, platô baixo = menos eficaz).

### Anti-exemplar · note 1791762422573 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** What effect does a competitive antagonist have on efficacy ? {{c1::No change}}
- **Davi, rodada 1 (2026-10-13):** “IMAGEM”
- **Card depois (vivo):** What effect does a competitive antagonist have on efficacy? / {{c1::No change}}
  - **Verso depois:** - Emax is reached with enough agonist / - Curve shifts right in parallel; same maximum / / [IMG nebli-rang-fig-2-5a.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791762424650 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** In pharmacokinetic antagonism , one drug lowers the {{c1::concentration}} of another at its site of action
- **Davi, rodada 1 (2026-10-13):** “card escrito de forma estranha”
- **Card depois (vivo):** In pharmacokinetic antagonism, one drug weakens another by lowering its {{c1::concentration}} at the target, e.g. by inducing its metabolism
  - **Verso depois:** - It can act through absorption, metabolism or excretion
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791625431633 (2026-uc03-imunologia-45-ativacao-linfocitos-t)
- **Card antes:** A committed Th1 cell keeps the IL-4 gene silent by packing it into closed {{c1::chromatin}}
- **Davi, rodada 1 (2026-10-15):** “card estranho de linguagem linguagem autoral ainda não está 100% anking like tipo "subset????"”
- **Card depois (vivo):** A committed Th1 cell keeps the IL-4 gene silent by packing it into closed {{c1::chromatin}}
  - **Verso depois:** - This epigenetic lock stabilizes the lineage, so the cell does not drift into a Th2 program
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791625433083 (2026-uc03-imunologia-45-ativacao-linfocitos-t)
- **Card antes:** Induced Tregs develop from naive CD4+ T cells exposed to TGF-β plus {{c1::retinoic acid}}
- **Davi, rodada 1 (2026-10-15):** “um bom comentário explicaria o porquê ao invés de só falar que deriva”
- **Card depois (vivo):** Induced Tregs develop from naive CD4+ T cells exposed to TGF-β plus {{c1::retinoic acid}}
  - **Verso depois:** - Retinoic acid derives from vitamin A / - Gut dendritic cells make retinoic acid, so induced Tregs arise mainly in the intestine and keep tolerance to food and commensal bacteria
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791626776253 (2026-uc03-microbiologia-44-micoses-cutaneas)
- **Card antes:** Sites infected by each dermatophyte genus: Skin Hair Nails Trichophyton ✓ ✓ ✓ Microsporum ✓ {{c1::✓}} {{c1::✗}} Epidermophyton ✓ {{c2::✗}} {{c2::✓}}
- **Davi, rodada 1 (2026-10-15):** “card deveria ser a tabela em IO assim fica ruim”
- **Card na rodada 2:** Sites infected by each dermatophyte genus: Skin Hair Nails Trichophyton {{c2::Yes}} {{c2::Yes}} {{c2::Yes}} Microsporum {{c3::Yes}} {{c3::Yes}} {{c3::Rarely}} Epidermophyton {{c1::Yes}} {{c1::No}} {{c
- **Davi, rodada 2 (2026-10-22):** “ajustei o card para ficar bom”
- **Card depois (vivo):** Sites infected by each dermatophyte genus: / Skin Hair Nails Trichophyton{{c2::Yes}}{{c2::Yes}}{{c2::Yes}}Microsporum{{c3::Yes}}{{c3::Yes}}{{c3::Rarely}}Epidermophyton{{c1::Yes}}{{c1::No}}{{c1::Yes}}
  - **Verso depois:** Dermatophytes are cutaneous mycosis /
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791627549152 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** A eukaryotic activator binds DNA through one domain and recruits the transcription machinery through a separate {{c1::activation domain}}
- **Davi, rodada 1 (2026-10-15):** “o que isso sequer quer dizer? card bom explica algo e ajuda a decorar esse cria conceitos específicos e me joga como se decorar qualquer coisa servisse”
- **Card na rodada 2:** An activator has a DNA-binding domain and an {{c1:: activation domain }} that recruits Mediator and RNA polymerase II
- **Davi, rodada 2 (2026-10-22):** “card mal escrito e sem negrito”
- **Card depois (vivo):** An activator has a DNA-binding domain and an {{c1::activation domain}} that recruits Mediator and RNA polymerase II
  - **Verso depois:** - The activation domain contacts Mediator and coactivators, which bring RNA polymerase II to the promoter
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7). Aqui: Frase genérica sobre domínios do ativador, sem o experimento e sem por que importa: decorar 'activation domain' não ensina nada.

### Anti-exemplar · note 1791628675323 (2026-uc03-microbiologia-48-micoses-subcutaneas)
- **Card antes:** Because the fungus is implanted by minor trauma from soil and plants, chromoblastomycosis mostly affects the {{c1::lower limbs}}
- **Davi, rodada 1 (2026-10-15):** “card ruim não ensina nada, só decora para ser bom, seria a explicação do porquê é lower limbs que são afetados + clozem em algo de decorar”
- **Card depois (vivo):** Because the fungus is implanted by minor trauma from soil and plants, chromoblastomycosis mostly affects the {{c1::lower limbs}}
  - **Verso depois:** - Typical patients are rural workers who walk barefoot or handle wood and thorny plants / [IMG mb48-cromomicose-membro.png]
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas. Aqui: Cloze no local (membros inferiores) sem o porquê (trauma com solo e plantas); o card bom explica a causa e cobra o que se decora.

### Anti-exemplar · note 1791716407251 (2026-uc03-patologia-47-inflamacao-granulomatosa)
- **Card antes:** {{c1::Foreign-body}} granulomas surround material that macrophages cannot readily degrade
- **Davi, rodada 1 (2026-10-15):** “fiz um ajuste no card aprende o que foi entende o que é assim fica melhor: cloze no que realmente é para decorar”
- **Card depois (vivo):** {{c1::Foreign-body}} granulomas surround material that macrophages cannot readily degrade
  - **Verso depois:** - Large or indigestible material persists despite attempts at phagocytosis. / - A retained suture illustrates this mechanism.
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791716425502 (2026-uc03-patologia-47-inflamacao-granulomatosa)
- **Card antes:** Foreign-body giant cells tend to have {{c1::irregularly scattered}} nuclei
- **Davi, rodada 1 (2026-10-15):** “palavras mt abstratas dif´ceis de lembrar para lembrar, simplicidade e rigor valem mais”
- **Card depois (vivo):** In foreign-body giant cells, the nuclei are {{c1::scattered}} throughout the cytoplasm rather than at the periphery
  - **Verso depois:** - Nuclear position alone does not establish the cause of a granuloma.
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1791716425974 (2026-uc03-patologia-47-inflamacao-granulomatosa)
- **Card antes:** Neither {{c1::caseous necrosis}} nor {{c2::giant cells}} are required to diagnose a granuloma
- **Davi, rodada 1 (2026-10-15):** “ajeitei para ficar melhor o card aprende”
- **Card depois (vivo):** Neither {{c1::caseous necrosis}} nor {{c2::giant cells}} are required to diagnose a granuloma
  - **Verso depois:** - The defining feature is an organized aggregate of activated macrophages.
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791716432060 (2026-uc03-patologia-47-inflamacao-granulomatosa)
- **Card antes:** Granulomas heal by {{c1::fibrosis}}, which replaces functional parenchyma and can impair the organ
- **Davi, rodada 1 (2026-10-15):** “de novo: o que isso sequer quer dizer? card ruim conserta e grava como exemplo ruim para não ter mais às vezes vc fica só seguindo regra ao invés de fazer as coisas bem feitas aprende a fazer bons card, anking like em tamanho, linguagem, forma de apresentar e clareza”
- **Card depois (vivo):** Granulomas heal by {{c1::fibrosis}}, which replaces functional parenchyma and can impair the organ
  - **Verso depois:** - In the lung, scarred granulomas reduce the surface available for gas exchange
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares. Aqui: Afirmação vaga ('cicatriza por fibrose') sem processo nem consequência concreta; Davi: 'o que isso sequer quer dizer?'.

### Anti-exemplar · note 1791716444100 (2026-uc03-patologia-47-inflamacao-granulomatosa)
- **Card antes:** Unlike immune granulomas, foreign-body granulomas (e.g., around sutures or talc) form without {{c1::T-cell}} activation
- **Davi, rodada 1 (2026-10-15):** “card ruim mts autorais desse não tem explicado bem não fica claro a explicação nem o que querem lembrar”
- **Card depois (vivo):** Unlike immune granulomas, foreign-body granulomas (e.g., around sutures or talc) form without {{c1::T-cell}} activation
  - **Verso depois:** - The material is too large or inert to be phagocytosed, so macrophages simply surround it
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791744435681 (2026-uc03-microbiologia-43-biologia-fungos)
- **Card antes:** Asexual spores formed freely on hyphae are {{c1::conidia}}, whereas spores formed inside a sac (sporangium) are sporangiospores
- **Davi, rodada 1 (2026-10-15):** “o card realmente não explica bem algo digo, não fica claro o conceito que ele tenta lembrar”
- **Card depois (vivo):** (nota apagada)
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791744812583 (2026-uc03-grand-round-04-paracoccidioidomicose)
- **Card antes:** In paracoccidioidomycosis , conidia from the environmental {{c1::mold::mold/yeast}} form are inhaled, and in tissue the fungus becomes a {{c1::yeast::mold/yeast}}
- **Davi, rodada 1 (2026-10-15):** “não seria mold phase?”
- **Davi, rodada 2 (2026-10-22):** “ficou top esse card”
- **Card depois (vivo):** In paracoccidioidomycosis, conidia from the environmental {{c1::mold::mold/yeast}} form are inhaled, and in tissue the fungus becomes a {{c1::yeast::mold/yeast}}
  - **Verso depois:** - The switch happens at body temperature (37 °C)
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791762422450 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** What effect does a competitive antagonist have on potency ? {{c1::Decrease (curve shifts right)}}
- **Davi, rodada 1 (2026-10-15):** “poderia ter uma imagem aqui”
- **Card depois (vivo):** What effect does a competitive antagonist have on potency? / {{c1::Decrease (curve shifts right)}}
  - **Verso depois:** - Higher agonist concentrations overcome the block / - A: agonist alone; B: agonist plus a competitive antagonist (same maximum, shifted right) / [IMG nebli-fa01-antagonista-competitivo.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791983678232 (2026-uc03-patologia-62-inflamacao-cronica)
- **Card antes:** Chronic inflammation is inflammation that lasts {{c1::weeks to months}}
- **Davi, rodada 1 (2026-10-15):** “quando falei de card organizador, era para o cloze ser aquilo que deve ser lembrado também é essencial que fosse em tópicos C I D”
- **Card depois (vivo):** Chronic inflammation is inflammation that lasts {{c1::weeks to months}}
  - **Verso depois:** - There is no exact cutoff: the coexistence of inflammation, injury and repair (C/I/D) defines chronicity
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1790972065310 (2026-uc08-anatomia-01-esofago-estomago-delgado)
- **Card antes:** The {{c2:: aorta }}, thoracic duct , and azygos vein perforate the diaphragm at the level of {{c1:: T12 }}
- **Davi, rodada 1 (2026-10-22):** “falta um card organizador de atravessar o diafragma card novo em tabela com clozes”
- **Card depois (vivo):** The {{c2::aorta}}, thoracic duct, and azygos vein perforate the diaphragm at the level of {{c1::T12}}
  - **Verso depois:** - At T-1-2, its the red (aorta), white (thoracic duct), and blue (azygos vein) / - "I (IVC) ate (8) ten (10) eggs (esophagus) at (aorta) twelve (12)" / [IMG 45d522d8275fc877ec0cf6d51ef36d5d.jpg] / [IMG ded1ba10a42684612fa97fc7ca1eccf0.jpg]
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1790974695882 (2026-uc08-anatomia-02-intestino-grosso-canal-anal)
- **Card antes:** In the male, the rectum is related anteriorly to the bladder, the seminal glands and the {{c1:: prostate }}
- **Davi, rodada 1 (2026-10-22):** “IMAGEM ruim”
- **Card depois (vivo):** In the male, the rectum is related anteriorly to the bladder, the seminal glands and the {{c1::prostate}}
  - **Verso depois:** No homem, o reto relaciona-se anteriormente com a bexiga, as glândulas seminais e a próstata.
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790981518578 (2026-uc03-patologia-radiologia-19-correlacao-2)
- **Card antes:** At the lower esophagus , the portal system meets the systemic system through the {{c1:: left gastric }} vein and the esophageal branches of the {{c1:: azygos }} vein
- **Davi, rodada 1 (2026-10-22):** “tem um card mt parecido com esse, daí fico confundido escreve diferente esse um pouco poderia ter uma foto melhor”
- **Card depois (vivo):** At the lower esophagus, the portal system meets the systemic system through the {{c1::left gastric}} vein and the esophageal branches of the {{c1::azygos}} vein
  - **Verso depois:** - Esophageal branch of azygos → azygos → IVC / SVC / - Left gastric → portal vein / - If ruptured, manifests as painless bleeding, can cause massive hematemesis / [IMG paste-35381940584451.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1790981525201 (2026-uc08-anatomia-07-vascularizacao-visceras)
- **Card antes:** The {{c2::rectosigmoid junction (Sudeck point)}} is a watershed region supplied by the last sigmoid arterial branch from the {{c1:: inferior mesenteric artery }} and the {{c1:: superior rectal artery
- **Davi, rodada 1 (2026-10-22):** “melhorei o card”
- **Card depois (vivo):** The {{c2::rectosigmoid junction (Sudeck point)}} is a watershed region supplied by the last sigmoid arterial branch from the {{c1::inferior mesenteric artery}} and the {{c1::superior rectal artery}}
  - **Verso depois:** - Remember, superior rectal artery is a branch of the IMA (so an anastomosis within the IMA) / / - Thus susceptible to ischemic colitis (AKA colonic ischemia) / [IMG 7c2309ebccf6aab648b9fcce20c297e6.webp] / / - inferior mesenteric artery (IMA).
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1790999272782 (2026-uc08-fisiologia-08-motilidade-i)
- **Card antes:** RhoA activates {{c1::Rho kinase}}, which inhibits myosin light chain phosphatase and raises the Ca 2+ sensitivity of smooth muscle
- **Davi, rodada 1 (2026-10-22):** “card estranho, poderia ensinar melhor”
- **Card depois (vivo):** In smooth muscle, {{c1::Rho kinase}} inhibits myosin light-chain phosphatase, so the same Ca2+ produces more force
  - **Verso depois:** - This is Ca2+ sensitization: myosin stays phosphorylated longer and keeps tone without more Ca2+ / - PKC does the same by phosphorylating CPI-17, an inhibitor of the phosphatase / [IMG nebli-uc08-fi08-p06f.png]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1790999833029 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** Slow waves of the GI tract are produced via cyclic opening of {{c1:: Ca 2+ }} channels (depolarization), followed by opening of {{c1:: K + }} channels (repolarization)
- **Davi, rodada 1 (2026-10-22):** “AJUSTEI o card para melhorá-lo anota no exemplares card sumiu, não compreendo”
- **Card depois (vivo):** Slow waves of the GI tract are produced via cyclic opening of {{c1::Ca2+}} channels (depolarization), followed by opening of {{c1::K+}} channels (repolarization)
  - **Verso depois:** Slow waves set the rhythm; past the contractile threshold they already give a weak contraction, and spikes add force
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791000310976 (2026-uc08-fisiologia-05-digestao-absorcao-nutrientes)
- **Card antes:** The basolateral {{c1:: Na⁺/K⁺-ATPase }} maintains the Na⁺ gradient that drives nutrient cotransport in enterocytes
- **Davi, rodada 1 (2026-10-22):** “negrito”
- **Card depois (vivo):** The basolateral {{c1::Na⁺/K⁺-ATPase}} maintains the Na⁺ gradient that drives nutrient cotransport in enterocytes
  - **Verso depois:** Low intracellular Na⁺ powers SGLT1 and the Na⁺ amino acid carriers.
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791000316027 (?)
- **Card antes:** Glucose uptake by SGLT1 activates myosin light chain kinase , which opens the {{c1:: paracellular }} pathway so water and nutrients follow
- **Davi, rodada 1 (2026-10-22):** “CARD com boa ideia, mas mal aplicada”
- **Card depois (vivo):** Glucose uptake by SGLT1 activates myosin light chain kinase, which opens the {{c1::paracellular}} pathway so water and nutrients follow
  - **Verso depois:** Glucose absorption opens the paracellular route, adding solvent drag / / [IMG nebli-uc08-fi05-s12.png] / - MLCK = myosin light chain kinase, which regulates the perijunctional actomyosin ring.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791023298343 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** Enterocytes keep {{c1:: disaccharidases }} and {{c1:: peptidases }} in the glycocalyx, finishing digestion at the brush border
- **Davi, rodada 1 (2026-10-22):** “melhorei o card, aprende”
- **Card depois (vivo):** Enterocytes keep {{c1::disaccharidases}} and {{c1::peptidases}} in the glycocalyx, finishing digestion at the brush border
  - **Verso depois:** Final digestion happens on the brush border, right where absorption occurs
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791023298718 (2026-uc08-biologia-tecidual-04-intestinos)
- **Card antes:** Enterocytes export triglycerides as {{c1:: chylomicrons }}, which enter the lacteal
- **Davi, rodada 1 (2026-10-22):** “imagem ruim”
- **Card depois (vivo):** Enterocytes export triglycerides as {{c1::chylomicrons}}, which enter the lacteal
  - **Verso depois:** Chylomicrons are too large for blood capillaries, so they enter the lymph. / / [IMG ec2b39a8ba0085d3780674c447fb7979.webp]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791557941879 (2026-uc03-microbiologia-43-biologia-fungos)
- **Card antes:** In dimorphic fungi, the yeast phase at 37 °C has more {{c1:: α-glucan }} in its wall than the mold phase
- **Davi, rodada 1 (2026-10-22):** “seria bom explicar no comentário que esse é o fator de virulência”
- **Card depois (vivo):** In dimorphic fungi, the yeast phase at 37 °C has more {{c1::α-glucan}} in its wall than the mold phase
  - **Verso depois:** - Mold phase (25 °C): more β-glucan / - Virulence factor: the outer α-glucan layer hides β-glucan from the macrophage receptor dectin-1, so the yeast is recognized less
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791575026219 (2026-uc08-fisiologia-09-motilidade-ii)
- **Card antes:** In the pharyngeal phase , a peristaltic wave of the {{c1:: pharyngeal constrictors }} pushes the bolus toward the esophagus
- **Davi, rodada 1 (2026-10-22):** “faltou imagem do que é essa estrutura”
- **Davi, rodada 2 (2026-10-23):** “imagem zuada”
- **Card depois (vivo):** In the pharyngeal phase, a peristaltic wave of the {{c1::pharyngeal constrictors}} pushes the bolus toward the esophagus
  - **Verso depois:** - The wave runs from the superior to the middle and inferior constrictors, which overlap like stacked cups / - The cricopharyngeal part then relaxes and lets the bolus into the esophagus / [IMG MSA-Muscles_of_Pharynx_342.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791575691218 (2026-uc03-microbiologia-43-biologia-fungos)
- **Card antes:** Hyphae grow by elongating at their {{c1:: tips }}, and a hyphal fragment can start a new colony
- **Davi, rodada 1 (2026-10-22):** “isso é um bom exemplo de card de mecanismo, me ajuda a compreender coisas básicas de vários tipos de fungos assim, para aula de aspectos gerais dos fungos, é isso que espero coisas que me ajudam a compreender o fenômeno como um todo, para depois aprofundar em detalhes e minúcias da exceções”
- **Card depois (vivo):** Hyphae grow by elongating at their {{c1::tips}}, and a hyphal fragment can start a new colony
  - **Verso depois:** - Fragmentation is a simple form of asexual reproduction
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791625425207 (2026-uc03-imunologia-07-organizacao-sistema-imune)
- **Card antes:** Naive T cells recirculate through lymph nodes, whereas activated effector T cells home to the {{c1:: infected tissue }}
- **Davi, rodada 1 (2026-10-22):** “negrito”
- **Card depois (vivo):** Naive T cells recirculate through lymph nodes, whereas activated effector T cells home to the {{c1::infected tissue}}
  - **Verso depois:** - Activation downregulates the lymph node homing receptors (CCR7, L-selectin)
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791625425333 (2026-uc03-imunologia-20-mhc-apresentacao)
- **Card antes:** As dendritic cells migrate to the lymph node they mature and raise MHC and the costimulatory molecule {{c1:: B7 }}
- **Davi, rodada 1 (2026-10-22):** “NEGRITO e sublinhado”
- **Card depois (vivo):** As dendritic cells migrate to the lymph node they mature and raise {{c1::MHC}} and the costimulatory molecule {{c1::B7}}
  - **Verso depois:** - They become less phagocytic and better at presenting
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791625426282 (2026-uc03-imunologia-20-mhc-apresentacao)
- **Card antes:** Antigens that lack a(n) {{c1:: peptide }} component are not recognizable by T cells and thus stimulate B cells directly
- **Davi, rodada 1 (2026-10-22):** “tab bom comentário ruim”
- **Card depois (vivo):** Antigens that lack a(n) {{c1::peptide}} component are not recognizable by T cells and thus stimulate B cells directly
  - **Verso depois:** - These are thymus-independent antigens (polysaccharides, lipids) / - T cells recognize only peptides on MHC, so B cells answer alone: mostly IgM, little memory
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791625427358 (2026-uc03-imunologia-20-mhc-apresentacao)
- **Card antes:** Antigen loading onto MHC II occurs following release of the {{c2:: invariant chain }} in a(n) {{c1:: acidified endosome }}
- **Davi, rodada 1 (2026-10-22):** “tab não fala o que é invariant chain corrigir isso”
- **Card depois (vivo):** Antigen loading onto MHC II occurs following release of the {{c2::invariant chain}} in a(n) {{c1::acidified endosome}}
  - **Verso depois:** [IMG 9c1606051a9932a7bca3218fbee13935.webp] / / - The invariant chain blocks the MHC II groove until then / - The invariant chain is made with MHC II in the ER, blocks its groove and guides it to the endosome, where it is cut
- **Análise:** [tab] Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.

### Anti-exemplar · note 1791625427531 (2026-uc03-imunologia-07-organizacao-sistema-imune)
- **Card antes:** In {{c1:: cross-presentation }}, dendritic cells load peptides from ingested antigens onto MHC I and activate CD8+ T cells
- **Davi, rodada 1 (2026-10-22):** “negrito”
- **Card depois (vivo):** In {{c1::cross-presentation}}, dendritic cells load peptides from ingested antigens onto MHC I and activate CD8+ T cells
  - **Verso depois:** - Lets CD8+ T cells respond to viruses that do not infect dendritic cells
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791625428782 (2026-uc03-imunologia-45-ativacao-linfocitos-t)
- **Card antes:** {{c1:: CTLA-4 }} is an inhibitory receptor , induced on activated T cells, that binds B7
- **Davi, rodada 1 (2026-10-22):** “negrito”
- **Card depois (vivo):** {{c1::CTLA-4}} is an inhibitory receptor, induced on activated T cells, that binds B7
  - **Verso depois:** - CD28 is constitutive and activating / - CTLA-4 helps end the response
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791625434208 (2026-uc03-imunologia-45-ativacao-linfocitos-t)
- **Card antes:** IFN-γ from Th1 cells promotes B-cell class switching to {{c1:: IgG }}
- **Davi, rodada 1 (2026-10-22):** “negrito”
- **Card depois (vivo):** IFN-γ from Th1 cells promotes B-cell class switching to {{c1::IgG}}
  - **Verso depois:** - These IgG subclasses opsonize and fix complement
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791625434632 (2026-uc03-imunologia-45-ativacao-linfocitos-t)
- **Card antes:** {{c1:: Natural Tregs }} arise in the thymus, whereas induced Tregs develop from naive CD4+ T cells in the periphery
- **Davi, rodada 1 (2026-10-22):** “negrito”
- **Card depois (vivo):** {{c1::Natural Tregs}} arise in the thymus, whereas induced Tregs develop from naive CD4+ T cells in the periphery
  - **Verso depois:** Both populations express FOXP3; induced Tregs arise after peripheral antigen exposure in a tolerogenic cytokine environment.
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791627546300 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** Besides saving energy, regulating gene expression drives cell {{c1:: differentiation }} during development
- **Davi, rodada 1 (2026-10-22):** “NEGRITO”
- **Card depois (vivo):** Besides saving energy, regulating gene expression drives cell {{c1::differentiation}} during development
  - **Verso depois:** - Responses can depend on location and timing
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791627546552 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** Regulated genes, such as alcohol dehydrogenase in the liver, are expressed only in certain {{c1:: cell types }} or times
- **Davi, rodada 1 (2026-10-22):** “falando desse deck como um todo: excesso de cards autorais de baixa qualidade, com cloze em palavras que não são as mais específicas a serem decoradas sinto que faltou informação no deck como um todo, para cobrir a aula é necessário se perguntar, para um card autoral: isso aqui agrega algo no conhecimento ou está só para ficar bonito? existem formas boas e ruins de criar cards autorais os do anking são melhores”
- **Card depois (vivo):** Regulated genes, such as alcohol dehydrogenase in the liver, are expressed only in certain {{c1::cell types}} or times
  - **Verso depois:** - They act as markers of differentiation
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791627548276 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** The TATA-binding protein , which recognizes the TATA box, is a subunit of the general factor {{c1:: TFIID }}
- **Davi, rodada 1 (2026-10-22):** “de novo, sigla só o card”
- **Card depois (vivo):** The TATA-binding protein, which recognizes the TATA box, is a subunit of the general factor {{c1::TFIID}}
  - **Verso depois:** - TFIID is the first general factor to bind the promoter; the others assemble on it
- **Análise:** [sigla] Sigla sozinha no card ou no cloze. Escrever o nome por extenso com a sigla junto; card tem de fazer sentido sozinho.

### Anti-exemplar · note 1791627548403 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** In an RNA polymerase II promoter , the BRE beside the TATA box is recognized by {{c1:: TFIIB }}
- **Davi, rodada 1 (2026-10-22):** “COMENTÁRIO RUIM”
- **Card depois (vivo):** In an RNA polymerase II promoter, the BRE beside the TATA box is recognized by {{c1::TFIIB}}
  - **Verso depois:** TFIIB binds the BRE and helps position RNA polymerase II at the transcription start site; INR and DPE are recognized by TFIID.
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791627548775 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** Several activators on one enhancer give more than the sum of their separate effects, which is called {{c1:: synergy }}
- **Davi, rodada 1 (2026-10-22):** “boa ideia de card bom comentário porém, o card em si está escrito de forma estranha”
- **Card depois (vivo):** Several activators on one enhancer give more than the sum of their separate effects, which is called {{c1::synergy}}
  - **Verso depois:** - Two activators together give far more than the sum of each alone
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791627548902 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** The yeast activator {{c1:: Gal4 }} turns on the genes that metabolize galactose
- **Davi, rodada 1 (2026-10-22):** “negrito negrito e sublinhado tem que ser gate-hard dos autorais”
- **Card depois (vivo):** The yeast activator {{c1::Gal4}} turns on the genes that metabolize galactose
  - **Verso depois:** - Like the lac operon in function, but each GAL gene has its own promoter
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1791627549027 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** The Gal4 DNA-binding domain recognizes one to four copies of the {{c1:: upstream activating sequence (UAS) }}
- **Davi, rodada 1 (2026-10-22):** “card ruim: cloze é só a sigla e tá dada a resposta”
- **Card depois (vivo):** The Gal4 DNA-binding domain recognizes one to four copies of the {{c1::upstream activating sequence (UAS)}}
  - **Verso depois:** The UAS is a yeast regulatory DNA sequence that functions like an enhancer.
- **Análise:** [sigla] Sigla sozinha no card ou no cloze. Escrever o nome por extenso com a sigla junto; card tem de fazer sentido sozinho.

### Anti-exemplar · note 1791627549276 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** The Gal4 activation domain recruits TFIID, Mediator and {{c1:: chromatin-modifying proteins }}
- **Davi, rodada 1 (2026-10-22):** “falta um organizador dessa aula falta gate hard em negrito nos cards autorais”
- **Card depois (vivo):** The Gal4 activation domain recruits TFIID, Mediator and {{c1::chromatin-modifying proteins}}
  - **Verso depois:** Gal4 activates transcription by recruiting the machinery; it does not contact RNA polymerase II directly.
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1791627549902 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** Ways to switch on a eukaryotic transcription factor: 1. {{c1:: Ligand ::L…}} binding 2. {{c1:: Phosphorylation ::P…}} 3. Unmasking 4. {{c1:: Nuclear entry ::N…}}
- **Davi, rodada 1 (2026-10-22):** “poderia ser tópicos aqui, não sequencial só faltou negrito”
- **Card depois (vivo):** Ways to switch on a eukaryotic transcription factor: / 1. {{c1::Ligand::L…}} binding / 2. {{c1::Phosphorylation::P…}} / 3. Unmasking / 4. {{c1::Nuclear entry::N…}}
  - **Verso depois:** - Also protein synthesis, adding a subunit or release from a membrane
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1791627550027 (2026-uc03-biologia-molecular-46-expressao-eucariotos-i)
- **Card antes:** Steroid and thyroid hormones cross the membrane and bind {{c1:: nuclear }} receptors, which then act as transcription factors
- **Davi, rodada 1 (2026-10-22):** “CARD RUIM”
- **Card depois (vivo):** Steroid and thyroid hormones cross the membrane and bind {{c1::nuclear}} receptors, which then act as transcription factors
  - **Verso depois:** - Steroids, thyroid hormone, vitamin D and retinoic acid use them
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791628672497 (2026-uc03-microbiologia-48-micoses-subcutaneas)
- **Card antes:** {{c1:: Madurella grisea }}, an agent of eumycetoma in Brazil, forms black grains
- **Davi, rodada 1 (2026-10-22):** “imagem no back”
- **Card depois (vivo):** {{c1::Madurella grisea}}, an agent of eumycetoma in Brazil, forms black grains
  - **Verso depois:** The color of grains recovered from drainage or biopsy helps narrow the causative fungus. / / [IMG mb48-micetoma-graos.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791628674574 (2026-uc03-microbiologia-48-micoses-subcutaneas)
- **Card antes:** Sporothrix is a a cigar-shaped budding {{c1::yeast::yeast/mold}} in tissue and a {{c1::mold::yeast/mold}} on plants and soil
- **Davi, rodada 1 (2026-10-22):** “melhorei o card falta só a imagem agora aprendi do que fiz”
- **Card depois (vivo):** Sporothrix is a a cigar-shaped budding {{c1::yeast::yeast/mold}} in tissue and a {{c1::mold::yeast/mold}} on plants and soil
  - **Verso depois:** - In Brazil the main species is S. brasiliensis / [IMG mb48-sporothrix-levedura.png]
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791628675824 (2026-uc03-microbiologia-48-micoses-subcutaneas)
- **Card antes:** A mycetoma is defined by: 1. Tumor-like {{c1:: swelling }} 2. Draining {{c2:: sinuses }} 3. {{c1:: Grains }}
- **Davi, rodada 1 (2026-10-22):** “tríade assim tem que vir em tópicos com c1 c2 c1”
- **Card depois (vivo):** A mycetoma is defined by: / 1. Tumor-like {{c1::swelling}} / 2. Draining {{c2::sinuses}} / 3. {{c1::Grains}}
  - **Verso depois:** Grains are compact colonies of the causative organism and can be examined directly or in biopsy. / [IMG mb48-micetoma-graos.png]
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1791628676074 (2026-uc03-microbiologia-48-micoses-subcutaneas)
- **Card antes:** {{c2:: Actinomyces }} is a(n) {{c1:: obligate anaerobe ::obligate aerobe or anaerobe}} that is typically found in the gums and causes dental abscesses
- **Davi, rodada 1 (2026-10-22):** “card hy rosa, tem q ser verde comentário só repete o card poderia ser tanta coisa: pq ele é assim, o que causa, alguma relação dele com qualquer coisa útil”
- **Card depois (vivo):** {{c2::Actinomyces}} is a(n) {{c1::obligate anaerobe::obligate aerobe or anaerobe}} that is typically found in the gums and causes dental abscesses
  - **Verso depois:** Actinomyces grows in low-oxygen gingival crevices; disruption of the mucosa lets it invade contiguous tissue and form dental or cervicofacial abscesses. Unlike Nocardia, it is anaerobic.
- **Análise:** [cor] Cor errada para a importância (HY rosa, detalhe verde). A cor segue a rubrica: HY 1–2 e pilares verdes, detalhe rosa.

### Anti-exemplar · note 1791628676621 (2026-uc03-microbiologia-48-micoses-subcutaneas)
- **Card antes:** Jorge Lobo disease produces {{c1:: keloid }}-like skin nodules
- **Davi, rodada 1 (2026-10-22):** “imagem”
- **Card depois (vivo):** Jorge Lobo disease produces {{c1::keloid}}-like skin nodules
  - **Verso depois:** - Often on the ear / [IMG mb48-lobomicose-queloide.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791629587272 (2026-uc03-imunologia-49-ativacao-celulas-b)
- **Card antes:** The {{c1:: immature }} B cell is characterized by surface IgM , but no surface IgD
- **Davi, rodada 1 (2026-10-22):** “tem que ter um card que organiza isso progenitor immature naive ... mt nome sem agrupar eles”
- **Card depois (vivo):** The {{c1::immature}} B cell is characterized by surface IgM, but no surface IgD
  - **Verso depois:** [IMG 2ed48de586dceb80416a8eeb128fc496.webp] / / - IgD appears only when the cell finishes maturing in a secondary lymphoid organ
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1791629590097 (2026-uc03-imunologia-49-ativacao-celulas-b)
- **Card antes:** B-1 cells are marked by surface {{c1::CD5}}
- **Davi, rodada 1 (2026-10-22):** “faltou explicar o que é B1”
- **Card depois (vivo):** B-1 cells are marked by surface {{c1::CD5}}
  - **Verso depois:** - B-1 cells are innate-like B cells of the peritoneal and pleural cavities that make natural IgM against polysaccharides without T-cell help / - Conventional B-2 cells are CD5 negative and form germinal centers with T-cell help
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791629592622 (2026-uc03-imunologia-49-ativacao-celulas-b)
- **Card antes:** Do thymus-independent antigens result in immunologic memory ? {{c1::No}}
- **Davi, rodada 1 (2026-10-22):** “tab bom”
- **Card depois (vivo):** Do thymus-independent antigens result in immunologic memory? / {{c1::No}}
  - **Verso depois:** - Weakly immunogenic / - Vaccines often require boosters and adjuvants (e.g., pneumococcal polysaccharide vaccine)
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791629592997 (2026-uc03-imunologia-49-ativacao-celulas-b)
- **Card antes:** B-cell activation begins with presentation of foreign antigen on {{c1:: MHC II }}, which is recognized by a T-cell receptor
- **Davi, rodada 1 (2026-10-22):** “- CD28: receptor coestimulador dos linfócitos T. - CD40: receptor presente nos linfócitos B e em outras células apresentadoras de antígeno (APCs). - CD80/CD86 (B7): ligantes de CD28, expressos pelas APCs. - CD40L (CD154): ligante de CD40, expresso principalmente por linfócitos T CD4+ ativados”
- **Card depois (vivo):** B-cell activation begins with presentation of foreign antigen on {{c1::MHC II}}, which is recognized by a T-cell receptor
  - **Verso depois:** - Signal 1 is TCR–MHC II; signal 2 is costimulation / - CD28: costimulatory receptor of T cells / - CD80/CD86 (B7): ligands of CD28, expressed by APCs / - CD40: receptor on B cells and other APCs / - CD40L (CD154): ligand of CD40, mainly on activated CD4+ T cells
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1791629593422 (2026-uc03-imunologia-49-ativacao-celulas-b)
- **Card antes:** Pneumococcal conjugate vaccine for children produces an Ig{{c1::G}} response
- **Davi, rodada 1 (2026-10-22):** “tab ruim”
- **Card depois (vivo):** Pneumococcal conjugate vaccine for children produces an Ig{{c1::G}} response
  - **Verso depois:** - As it is conjugated to a protein / - Conjugate vaccine for Children
- **Análise:** [tab] Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.

### Anti-exemplar · note 1791629593848 (2026-uc03-imunologia-07-organizacao-sistema-imune)
- **Card antes:** Which region of the lymph node enlarges and multiplies during humoral immune response (e.g., bacterial infection)? {{c1::Germinal centers}}
- **Davi, rodada 1 (2026-10-22):** “não tem um card igual a esse?”
- **Card depois (vivo):** Which region of the lymph node enlarges and multiplies during humoral immune response (e.g., bacterial infection)? / / {{c1::Germinal centers}}
  - **Verso depois:** Increased number of germinal centers → lymphadenopathy / / [IMG a05cb5f548622083368e4ff1c9597f04.webp]
- **Análise:** [repetido] Card repetido ou muito parecido com outro: confunde e gasta revisão. Um fato, um card; o outro aspecto vai no verso ou em card com ganho próprio.

### Anti-exemplar · note 1791629593971 (2026-uc03-imunologia-07-organizacao-sistema-imune)
- **Card antes:** Activated helper T cells and antigen-bearing B cells meet at the edge of the {{c1::follicle}}
- **Davi, rodada 1 (2026-10-22):** “FOTO”
- **Card depois (vivo):** Activated helper T cells and antigen-bearing B cells meet at the edge of the {{c1::follicle}}
  - **Verso depois:** - Chemokine receptors guide both cells to the same region: the T cell toward the follicle, the B cell toward the T-cell zone / [IMG a10fc17517aad74736e4bb8bd3204683.webp]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791629594347 (2026-uc03-imunologia-49-ativacao-celulas-b)
- **Card antes:** After B-cell activation, alternative RNA processing converts membrane immunoglobulin into {{c1:: secreted antibody }}
- **Davi, rodada 1 (2026-10-22):** “cloze num lugar ruim”
- **Card depois (vivo):** After B-cell activation, alternative RNA processing converts membrane immunoglobulin into {{c1::secreted antibody}}
  - **Verso depois:** The antigen-binding variable region is unchanged; only the C-terminal form switches from a membrane anchor to a secreted tail.
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1791629595872 (2026-uc03-imunologia-31-sistema-complemento)
- **Card antes:** A single antigen-bound {{c1:: IgM pentamer }} can recruit two C1q heads and activate the classical complement pathway
- **Davi, rodada 1 (2026-10-22):** “estranho TAB RUIM card não ficou claro”
- **Card depois (vivo):** A single antigen-bound {{c1::IgM pentamer}} can recruit two C1q heads and activate the classical complement pathway
  - **Verso depois:** C1q must bind at least two Fc regions. One pentameric IgM supplies them after binding antigen, whereas IgG requires two adjacent molecules; IgG4 does not activate complement.
- **Análise:** [tab] Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.

### Anti-exemplar · note 1791630905768 (2026-uc03-microbiologia-50-micoses-sistemicas)
- **Card antes:** {{c2:: Histoplasma capsulatum ::Which fungus}} characteristically presents on histology as {{c1:: macrophages }} containing {{c1:: oval }} bodies
- **Davi, rodada 1 (2026-10-22):** “cadê a foto card pouco específico também tem um card anking disso de demlhor qualidade se inspira e coloca nos anti exemplares”
- **Card depois (vivo):** {{c2::Histoplasma capsulatum::Which fungus}} characteristically presents on histology as {{c1::macrophages}} containing {{c1::oval}} bodies
  - **Verso depois:** - Small yeasts (2–4 µm) packed inside macrophages, smaller than a red blood cell / - Seen with Giemsa or Gomori-Grocott silver stain / [IMG 7b3d0402fd492edfab022f362531dc53.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791630906668 (2026-uc03-microbiologia-50-micoses-sistemicas)
- **Card antes:** Because Histoplasma is hard to see on direct exam , diagnosis relies on fungal {{c1::culture}}
- **Davi, rodada 1 (2026-10-22):** “imagem”
- **Card depois (vivo):** Because Histoplasma is hard to see on direct exam, diagnosis relies on fungal {{c1::culture}}
  - **Verso depois:** - Yeasts are small and hidden inside macrophages / [IMG mb50-histoplasma-intracelular.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791630908168 (2026-uc03-microbiologia-50-micoses-sistemicas)
- **Card antes:** After a lung infection , Cryptococcus shows marked tropism for the {{c1::meninges}}
- **Davi, rodada 1 (2026-10-22):** “o comentário deveria dar uma ideia dar uma ideia do porquê todos os comentários que deixo aqui tem que ir para os exemplares e antiexemplares dos cards”
- **Card depois (vivo):** After a lung infection, Cryptococcus shows marked tropism for the {{c1::meninges}}
  - **Verso depois:** - Why the CNS: the capsule lets the yeast survive in the blood, it crosses the blood–brain barrier (directly or inside macrophages), and the CSF has little complement and few phagocytes / - Brain catecholamines also feed its melanin, which protects it from oxidative killing / - It causes meningitis 
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791630910669 (2026-uc03-microbiologia-50-micoses-sistemicas)
- **Card antes:** {{c1:: India ink }} stain outlines the heavy capsule that surrounds {{c2:: Cryptococci }} fungi, giving it a unique "{{c1:: halo }}" appearance
- **Davi, rodada 1 (2026-10-22):** “tem que ter no comentário a tradução disso, que é outro nome (nanquim)”
- **Card depois (vivo):** {{c1::India ink}} stain outlines the heavy capsule that surrounds {{c2::Cryptococci}} fungi, giving it a unique "{{c1::halo}}" appearance
  - **Verso depois:** [IMG 6844923e23e97a5afd182b9ea0b457d2.jpg][IMG 9d1788feb193de739c5a0e9be49e95f3.jpg][IMG f91dd421a8fdf654c5e3cfba6363525d.webp] / / - Used on CSF / - India ink is the same stain called nanquim (tinta da China) in Portuguese
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791630910843 (2026-uc03-microbiologia-50-micoses-sistemicas)
- **Card antes:** Which fungus is urease -positive? {{c1:: Cryptococcus neoformans }}
- **Davi, rodada 1 (2026-10-22):** “tab não explicou o porque ele tem urease, o que é um problema, porque não me ajuda a saber”
- **Card depois (vivo):** Which fungus is urease-positive? / / {{c1::Cryptococcus neoformans}}
  - **Verso depois:** Separates crypto from other fungi / / - Urease turns urea into ammonia; in Cryptococcus it helps the yeast cross the blood–brain barrier / - In the lab, urease separates Cryptococcus (positive) from Candida (negative)
- **Análise:** [tab] Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.

### Anti-exemplar · note 1791631342791 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** The basal state of eukaryotic transcription is {{c1:: restrictive }} because nucleosomes limit access to DNA
- **Davi, rodada 1 (2026-10-22):** “uso dsa palavras corretas aqui? essa é a melhor forma de fazer um card com essa info? autorais desse deck ficaram estranho”
- **Card depois (vivo):** Because nucleosomes cover promoters, a eukaryotic gene is {{c1::off}} until activators open its chromatin
  - **Verso depois:** - In bacteria the default is the opposite: RNA polymerase reaches naked DNA and repressors must stop it
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791631343592 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** Interactions between histone {{c1:: N-terminal tails }} help compact nucleosomes into higher-order chromatin
- **Davi, rodada 1 (2026-10-22):** “cloze num local terrível”
- **Card depois (vivo):** Histone N-terminal tails stick out of the nucleosome, so enzymes can {{c1::acetylate}} them and loosen the chromatin
  - **Verso depois:** - Acetylation neutralizes the lysine positive charge, so the tail grips the DNA less / - Tail-to-tail contacts are what compact nucleosomes into fibers
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1791631343842 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** ATP-dependent nucleosome-remodeling complexes slide, eject or restructure nucleosomes using energy from {{c1:: ATP }}
- **Davi, rodada 1 (2026-10-22):** “falta um card organizador desse tipo de processo card organizador serve precisamente para isso: comparar coisas diferentes e organizar na minha cabeça as ideias adiciona nesse deck, coloca nos exemplares e coloca uma pergunta (há card organizadores onde deve-se no deck?) como gate-hard no fim da geração de todo deck”
- **Card depois (vivo):** ATP-dependent nucleosome-remodeling complexes slide, eject or restructure nucleosomes using energy from {{c1::ATP}}
  - **Verso depois:** They change nucleosome position or composition without covalently modifying histones, unlike HATs, HDACs and histone methyltransferases.
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova). Aqui: Cloze em 'ATP' (genérico) e faltou o organizador que compara os mecanismos de remodelação.

### Anti-exemplar · note 1791631344117 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** {{c1:: Histone acetyltransferases (HATs) }} transfer acetyl groups to lysines in histone tails
- **Davi, rodada 1 (2026-10-22):** “quando for assim não dá para deixar sigla fora do card”
- **Card depois (vivo):** {{c1::Histone acetyltransferases (HATs)}} transfer acetyl groups to lysines in histone tails
  - **Verso depois:** Acetylation neutralizes lysine's positive charge, weakens histone–DNA interactions and usually marks accessible chromatin.
- **Análise:** [sigla] Sigla sozinha no card ou no cloze. Escrever o nome por extenso com a sigla junto; card tem de fazer sentido sozinho.

### Anti-exemplar · note 1791631344241 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** {{c1:: Histone deacetylases (HDACs) }} remove acetyl groups from lysines in histone tails
- **Davi, rodada 1 (2026-10-22):** “mesma coisa: sigla de fora nã odá comentário tá no padrão IA não didático tb”
- **Card depois (vivo):** {{c1::Histone deacetylases (HDACs)}} remove acetyl groups from lysines in histone tails
  - **Verso depois:** Removing acetyl groups restores positive charge, favors tighter DNA binding and usually promotes condensed, inactive chromatin.
- **Análise:** [sigla] Sigla sozinha no card ou no cloze. Escrever o nome por extenso com a sigla junto; card tem de fazer sentido sozinho.

### Anti-exemplar · note 1791631344666 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** Histone tails can be acetylated, methylated, ubiquitinated or {{c1:: phosphorylated }}
- **Davi, rodada 1 (2026-10-22):** “senti falta nesse deck de um pensamento contínuo para realmente passar por tudo ocm coerência e profundidade”
- **Card depois (vivo):** Histone tail marks and their effect: / - acetylation: {{c1::opens}} chromatin, gene active / - methylation: active or silent, depending on the {{c2::lysine}} marked / - the marks are read by proteins that recruit the next enzymes
  - **Verso depois:** - So the same histone can carry an on or off message, which reader proteins translate
- **Análise:** [cobertura] Deck incompleto ou com repetição no conjunto: faltou cobrir o que a aula/quiz ensina ou sobrou o mesmo fato várias vezes. Planejar a cobertura pelo slide antes de escolher cards (pipeline v7). Aqui: Lista de modificações de histona sem pensamento contínuo: nomes soltos, sem dizer o que cada marca faz.

### Anti-exemplar · note 1791631345241 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** At the yeast HO gene , Swi5 first opens chromatin, allowing the second activator {{c1:: SBF }} to bind
- **Davi, rodada 1 (2026-10-22):** “imagem aqui, decoro o nome de algo, mas o card falta storytelling”
- **Card depois (vivo):** At the yeast HO gene, Swi5 first opens chromatin, allowing the second activator {{c1::SBF}} to bind
  - **Verso depois:** This is sequential recruitment: Swi5 recruits a remodeler and a HAT; only after chromatin opens can SBF recruit the transcription machinery.
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791631346241 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** {{c1:: DNA methyltransferases }} use SAM to methylate cytosine at CpG sites, helping establish or maintain transcriptional silencing
- **Davi, rodada 1 (2026-10-22):** “card falta realmente ajudar num processo, onde isso se encaixa”
- **Card depois (vivo):** {{c1::DNA methyltransferases}} use SAM to methylate cytosine at CpG sites, helping establish or maintain transcriptional silencing
  - **Verso depois:** Methylated CpGs recruit proteins that cooperate with HDACs and histone methyltransferases, linking the DNA mark to compact chromatin.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791631346842 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** Methylated cytosines silence genes by recruiting histone deacetylases and nucleosome {{c1:: remodelers }}
- **Davi, rodada 1 (2026-10-22):** “card passa a informação que quer da melhor forma”
- **Card na rodada 2:** Methylated cytosines silence genes by recruiting {{c1::histone deacetylases}} and nucleosome {{c1:: remodelers }}
- **Davi, rodada 2 (2026-10-23):** “comentário poderia explicar o que é cada um dos clozes”
- **Card depois (vivo):** Methylated cytosines silence genes by recruiting {{c1::histone deacetylases}} and nucleosome {{c1::remodelers}}
  - **Verso depois:** - Histone deacetylases remove acetyl groups, so histones grip the DNA tightly / - Nucleosome remodelers slide nucleosomes over the promoter and hide it / - Methylated CpG islands also attract histone methyltransferases
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791631346967 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** Heritable gene-expression states that do not alter the DNA sequence are called {{c1:: epigenetic }} states
- **Davi, rodada 1 (2026-10-22):** “cloze num local ruim arrumar”
- **Card depois (vivo):** Epigenetic states are gene-expression patterns that persist through {{c1::cell division}} without changing the DNA sequence
  - **Verso depois:** - They are copied by maintenance DNA methylation and by histone marks restored after replication / - This is how a liver cell keeps making liver cells
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1791631347092 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** After replication , a {{c1:: maintenance DNA methyltransferase }} copies methylation onto the new strand
- **Davi, rodada 1 (2026-10-22):** “comentário zuado veja como melhorei o cloze, entenda o padrçao e coloca nos exemplares”
- **Card depois (vivo):** After replication, a {{c1::maintenance DNA methyltransferase}} copies methylation onto the new strand
  - **Verso depois:** - It recognizes hemimethylated CpG
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791716408660 (2026-uc03-patologia-47-inflamacao-granulomatosa)
- **Card antes:** T-cell–mediated immune granulomas involve {{c1::type IV}} hypersensitivity
- **Davi, rodada 1 (2026-10-22):** “aula errada para esse card”
- **Card depois (vivo):** T-cell–mediated immune granulomas involve {{c1::type IV}} hypersensitivity
  - **Verso depois:** - Foreign-body reactions can form without antigen-specific T-cell activation.
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1791762415623 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Antacids act without a drug target, by {{c1:: neutralizing }} gastric acid in the lumen
- **Davi, rodada 1 (2026-10-22):** “melhorei o card para ficar mais atômico”
- **Card depois (vivo):** Antacids act without a drug target, by {{c1::neutralizing}} gastric acid in the lumen
  - **Verso depois:** - A proton-pump inhibitor instead blocks new acid secretion
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791762418150 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Because of signal amplification and {{c1:: spare receptors }}, EC 50 need not equal the dissociation constant K d
- **Davi, rodada 1 (2026-10-22):** “esse deck ficou com excesso de cards que cobram a mesma coisa”
- **Card depois (vivo):** Because of signal amplification and {{c1::spare receptors}}, EC50 need not equal the dissociation constant Kd
  - **Verso depois:** - With spare receptors, a maximal response needs only part of the receptors occupied
- **Análise:** [repetido] Card repetido ou muito parecido com outro: confunde e gasta revisão. Um fato, um card; o outro aspecto vai no verso ou em card com ganho próprio.

### Anti-exemplar · note 1791762418773 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** An antagonist occupies the receptor but has zero {{c1:: efficacy }}, so it blocks the agonist without a response
- **Davi, rodada 1 (2026-10-22):** “card de novo com padrão de usar uma expressão forte que fica estranha e ambígua quem não tem intrisic activity? receptor or antagonis”
- **Card depois (vivo):** An antagonist occupies the receptor but has zero {{c1::efficacy}}, so it blocks the agonist without a response
  - **Verso depois:** - It blocks the agonist by occupying the receptor
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares. Aqui: Expressão forte e ambígua ('zero efficacy'): quem não tem atividade? Escrever o sujeito e o conceito com precisão.

### Anti-exemplar · note 1791762419322 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Pharmacological agonism includes full, partial, {{c1:: inverse }} and biased agonists
- **Davi, rodada 1 (2026-10-22):** “bom exemplo de card organizador de ideias”
- **Card depois (vivo):** Pharmacological agonism includes full, partial, {{c1::inverse}} and biased agonists
  - **Verso depois:** - They differ in the maximal response and in the pathway they favor
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791762419700 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Many H1 antihistamines such as loratadine act as inverse agonists because the H1 receptor has {{c1:: constitutive }} activity
- **Davi, rodada 1 (2026-10-22):** “card escrito de forma estranha”
- **Card depois (vivo):** Loratadine acts as an {{c1::inverse agonist}} at H1 receptors, which signal even without histamine
  - **Verso depois:** - An inverse agonist lowers the constitutive (ligand-free) activity of the receptor below baseline / - A neutral antagonist only blocks the agonist and leaves the baseline unchanged
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791762419949 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** A {{c1:: full agonist }} has enough efficacy to produce the maximal response of its receptor system
- **Davi, rodada 1 (2026-10-22):** “card ruim”
- **Card depois (vivo):** A {{c1::full agonist}} has enough efficacy to produce the maximal response of its receptor system
  - **Verso depois:** It mimics an endogenous signaling molecule, but 'full' describes maximal efficacy in that system—not necessarily stronger binding affinity.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791762421022 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** A {{c1::biased agonist}} preferentially activates one signaling pathway, such as G protein over β-arrestin, through the same receptor
- **Davi, rodada 1 (2026-10-22):** “cloze estava num local ruim”
- **Card depois (vivo):** Through the same receptor, a {{c1::biased}} agonist activates G-protein signaling more than β-arrestin signaling
  - **Verso depois:** - A receptor can signal through more than one pathway; a biased agonist selects one, which may separate the wanted effect from side effects / - β-arrestin also drives receptor desensitization and internalization
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1791762422823 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Antagonism on the dose–response curve : 1. Competitive antagonist — {{c1:: increases EC50 }} without changing Emax 2. Noncompetitive antagonist — {{c2:: reduces Emax }}
- **Davi, rodada 1 (2026-10-22):** “card estranho não compreendi”
- **Card depois (vivo):** Antagonism on the dose–response curve: / 1. Competitive antagonist — {{c1::increases EC50}} without changing Emax / 2. Noncompetitive antagonist — {{c2::reduces Emax}}
  - **Verso depois:** A surmountable competitive antagonist shifts the curve right (lower apparent potency). Noncompetitive or irreversible blockade removes functional receptors and lowers maximal efficacy.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791762425325 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Safer drugs generally have a {{c1:: higher therapeutic index }}
- **Davi, rodada 1 (2026-10-22):** “comentário ruim sem imagem”
- **Card depois (vivo):** Safer drugs generally have a {{c1::higher therapeutic index}}
  - **Verso depois:** TI = TD₅₀/ED₅₀: a larger separation between toxic and effective doses gives a wider safety margin. / / [IMG Screen Shot 2022-06-26 at 12.49.57 PM.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791762425949 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Quantal dose–response curves plot the percentage of individuals showing the therapeutic, toxic and {{c1:: lethal }} effect at each dose
- **Davi, rodada 1 (2026-10-22):** “faltou imagem”
- **Card depois (vivo):** Quantal dose–response curves plot the percentage of individuals showing the therapeutic, toxic and {{c1::lethal}} effect at each dose
  - **Verso depois:** - They describe a population, not the intensity in one person / / [IMG nebli-goodman-fig-4-2.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791826292220 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Which type of antagonism is shown in the lower graph? {{c1:: Noncompetitive }}
- **Davi, rodada 1 (2026-10-22):** “quando for assim, coloca só o gráfico que quiser cobrar, quebra ao meio a imagem assim fica mais atômico”
- **Card depois (vivo):** [IMG fa01-g-antagonismo-nao-competitivo.png] / Which type of antagonism lowers the maximal response even at high agonist doses? {{c1::Noncompetitive}}
  - **Verso depois:** - The antagonist removes functional receptors, so adding agonist cannot restore the maximum (Emax falls) / - A competitive antagonist instead shifts the curve to the right and the maximum is reached again
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1791826294319 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Which curves determine the therapeutic index ? {{c1:: Therapeutic and toxic }}
- **Davi, rodada 1 (2026-10-22):** “CARD mal feito, mal epensando”
- **Card depois (vivo):** [IMG fa01-g-quantal.png] / On population dose curves, the therapeutic index is {{c1::TD50}} / {{c2::ED50}}
  - **Verso depois:** - ED50: dose that gives the therapeutic effect in half of the individuals; TD50: dose that is toxic in half / - The farther apart the curves, the larger the index and the safer the drug
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791983684707 (2026-uc03-patologia-62-inflamacao-cronica)
- **Card antes:** In chronic inflammation , activated macrophages secrete {{c1:: IL-12 }}, which drives T cells toward Th1
- **Davi, rodada 1 (2026-10-22):** “mt info num card só”
- **Card depois (vivo):** In chronic inflammation, activated macrophages secrete {{c1::IL-12}}, which drives T cells toward Th1
  - **Verso depois:** - Each cell keeps the other active, so immune-driven inflammation tends to be persistent and severe / [IMG pt62-macrofago-linfocito.png]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1791984889849 (2026-uc03-patologia-61-patologia-infeccao-viral)
- **Card antes:** Which defenses act in each phase of a viral infection ? 1) acute phase: {{c1:: NK cells }}, {{c1:: macrophages }}, complement and barriers 2) subacute and chronic phases: {{c2:: T cells }}, {{c2:: B c
- **Davi, rodada 1 (2026-10-22):** “tópicos mal escritos, tem que ficar em pé, tipo os cards de constrição esofágica do deck de anato da p1 da uc08”
- **Card depois (vivo):** (nota apagada)
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova). Aqui: Organizador deitado (1) ... 2) ... em linha): tem de ficar em pé, um item por linha.

### Anti-exemplar · note 1792064698883 (2026-uc03-microbiologia-44-micoses-cutaneas)
- **Card antes:** Superficial × cutaneous mycoses : 1. Superficial — limited to the {{c1:: stratum corneum }} or hair surface, with little inflammation 2. Cutaneous — fungi digest {{c1:: keratin }} in skin, hair or nai
- **Davi, rodada 1 (2026-10-22):** “BOA IDEIa, mas mal aplicada”
- **Card depois (vivo):** Superficial × cutaneous mycoses: / 1. Superficial — limited to the {{c1::stratum corneum}} or hair surface, with little inflammation / 2. Cutaneous — fungi digest {{c1::keratin}} in skin, hair or nails and provoke inflammation
  - **Verso depois:** Subcutaneous mycoses are implanted beneath the skin; systemic mycoses are usually acquired by inhalation.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792065183130 (2026-uc03-microbiologia-50-micoses-sistemicas)
- **Card antes:** Agents of endemic systemic mycoses share three features: 1. Defined {{c1:: geographic distribution }} 2. Environmental reservoir in {{c2:: soil }} 3. Entry through the {{c3:: airways }}
- **Davi, rodada 1 (2026-10-22):** “card ruim”
- **Card depois (vivo):** Agents of endemic systemic mycoses share three features: / 1. Defined {{c1::geographic distribution}} / 2. Environmental reservoir in {{c2::soil}} / 3. Entry through the {{c3::airways}}
  - **Verso depois:** Their inhaled environmental propagules convert to a tissue form at body temperature; geography reflects the ecological niche of each fungus.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792082171335 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** Because chromatin already limits access to DNA, purely negative regulation is {{c1:: less common }} in eukaryotic transcription
- **Davi, rodada 1 (2026-10-22):** “NEGRITO passar card a card vendo negrito tem que ser gate-hard”
- **Card depois (vivo):** Because chromatin already limits access to DNA, purely negative regulation is {{c1::less common}} in eukaryotic transcription
  - **Verso depois:** Most eukaryotic genes require positive steps: activators expose regulatory DNA and recruit the transcription machinery.
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1792082183634 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** After replication, {{c1:: reader–writer complexes }} restore histone marks on new nucleosomes
- **Davi, rodada 1 (2026-10-22):** “FALTA UM CARD ORGANIZADOR DESSA AULA negrito estou marcando os cards que gosto com x, isso tem que virar exemplar, sempre lido antes de crira um deck fortalecer que autoral é só 30%”
- **Card depois (vivo):** After replication, histone marks are restored because a {{c1::reader}} domain binds the old mark and a writer copies it to new nucleosomes
  - **Verso depois:** - Old histones are split between the two daughter strands, so each daughter keeps a template of the marks
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1792083296387 (2026-uc03-grand-round-04-paracoccidioidomicose)
- **Card antes:** In paracoccidioidomycosis , protection depends on {{c1::cell-mediated}} immunity, while circulating antibodies are not protective
- **Davi, rodada 1 (2026-10-22):** “terceira parte do card entrega o cloze não há explicação do porquê também: o bom card tem o porquê no comentário”
- **Card depois (vivo):** In paracoccidioidomycosis, protection depends on {{c1::cell-mediated}} immunity
  - **Verso depois:** - Th1 IFN-γ activates macrophages that form granulomas and kill the yeast; antibodies do not reach the fungus inside cells / - A weak Th1 response allows the severe juvenile form
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso. Aqui: A última parte da frase entrega o cloze; e o verso não explica por que a imunidade celular protege.

### Anti-exemplar · note 1792166974340 (2026-uc03-imunologia-51-disturbios-sistema-imune)
- **Card antes:** {{c1:: Autoimmune }} disorders are associated with polymorphisms in the PTPN22 gene
- **Davi, rodada 1 (2026-10-22):** “comentário poderia mencionar o porquê, de forma sucinta, sem ser como foi”
- **Card depois (vivo):** {{c1::Autoimmune}} disorders are associated with polymorphisms in the PTPN22 gene
  - **Verso depois:** A gain-of-function PTPN22 variant dampens antigen-receptor signaling. Autoreactive lymphocytes may then receive too little signal for deletion or other tolerance checkpoints, increasing autoimmune risk.
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1792166988890 (2026-uc03-imunologia-51-disturbios-sistema-imune)
- **Card antes:** What is the most common primary immunodeficiency ? {{c1::Selective IgA deficiency}}
- **Davi, rodada 1 (2026-10-22):** “excesso de card de clínica: isso aqui tudo é legal, mas eu vou aprender mais para frente no momento quero aprender a base bem”
- **Card depois (vivo):** What is the most common primary immunodeficiency? / / {{c1::Selective IgA deficiency}}
  - **Verso depois:** Associated with celiac disease / / [IMG 8246e29ed402d1087af107a0c864d6c1.webp]
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1792175890985 (2026-uc03-microbiologia-48-micoses-subcutaneas)
- **Card antes:** A biopsy of a patient with {{c1::sporotrichosis ( Sporothrix schenckii )::what fungal infection}} will reveal {{c2:: granulomas }} consisting of histiocytes , multinucleated giant cells , and cigar-sh
- **Davi, rodada 1 (2026-10-22):** “foto”
- **Card depois (vivo):** A biopsy of a patient with {{c1::sporotrichosis (Sporothrix schenckii)::what fungal infection}} will reveal {{c2::granulomas}} consisting of histiocytes, multinucleated giant cells, and cigar-shaped budding yeast
  - **Verso depois:** - Few yeasts are seen; silver (Grocott) stain shows them best / [IMG b42863726b6f038acfb7d737d5313991.webp]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792176896207 (2026-uc03-microbiologia-50-micoses-sistemicas)
- **Card antes:** {{c2:: Coccidioides immitis ::Which fungus}} has a characteristic {{c3:: mold }} form containing {{c1:: barrel }} -shaped arthroconidia
- **Davi, rodada 1 (2026-10-22):** “FOTO”
- **Card depois (vivo):** {{c2::Coccidioides immitis::Which fungus}} has a characteristic {{c3::mold}} form containing {{c1::barrel}}-shaped arthroconidia
  - **Verso depois:** - Inhaled arthroconidia become spherules full of endospores in the lung / [IMG e026c380fb9c3cc6a2c51fdeb7b23d4d.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792240186582 (2026-uc03-imunologia-08-reconhecimento-inato)
- **Card antes:** LPS, bacterial flagellin, and viral nucleic acids are detected by the innate immune system via {{c1:: pattern-recognition }} receptors
- **Davi, rodada 1 (2026-10-22):** “esse deck de rec. imune inato ficou incompleto, faltou coisa para ele ficar completo de forma satisfatória (vê se outros da p1 tem o mesmo problema e complementa eles com os detalhes da aula que faltaram)”
- **Card depois (vivo):** LPS, bacterial flagellin, and viral nucleic acids are detected by the innate immune system via {{c1::pattern-recognition}} receptors
  - **Verso depois:** Examples of PRRs include toll-like receptors (TLRs) or NOD-like receptors / / - These shared microbial patterns (PAMPs) are absent from host cells
- **Análise:** [cobertura] Deck incompleto ou com repetição no conjunto: faltou cobrir o que a aula/quiz ensina ou sobrou o mesmo fato várias vezes. Planejar a cobertura pelo slide antes de escolher cards (pipeline v7).

### Anti-exemplar · note 1792241811997 (2026-uc03-imunologia-17-reconhecimento-adaptativo)
- **Card antes:** IgE cross-links when exposed to allergen , mediating type {{c1:: I }} hypersensitivity reactions
- **Davi, rodada 1 (2026-10-22):** “aula errada”
- **Card depois (vivo):** IgE cross-links when exposed to allergen, mediating type {{c1::I}} hypersensitivity reactions
  - **Verso depois:** - When multiple bound IgE on mast cells / basophils cross links a multivalent antigen, this pulls the FcεRI (high affinity IgE receptor) together / - Clumping of many FcεRI induces signaling that leads to degranulation / [IMG a80f3b267d2602619a54f6b55ec55750.webp] / / / - Discovered through allergy
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1792244803917 (?)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “de novo, mesma coisa, quero que já puxa a imagem com o cloze no local que está verde também quero que tenha só o nome em português”
- **Card depois (vivo):** [estrutura com seta] Nervo vestibulococlear
  - **Verso depois:** [IMG kh-nervus-vestibulocochlearis.jpg]
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1792244819469 (?)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “cloze me atrapalha de novo, não sei qual a estrutura que se trata”
- **Card depois (vivo):** [estrutura com seta] Parte superior do bulbo
  - **Verso depois:** [IMG kh-superior-part-of-medulla-oblongata.jpg]
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1792244839896 (?)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “exemplo claro: o cloze obstrui minha visualização da estrutura. o próprio kenhub deixa-a destacada de verde, basta colocar a seta e o cloze próximos”
- **Card depois (vivo):** [estrutura com seta] Glândula pineal
  - **Verso depois:** [IMG kh-glandula-pinealis.jpg]
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1792244857819 (2026-uc07-telencefalo-e-cortex-cerebral-vista-inferior-do-encefalo)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “quero que o IO fique já onde está ID, para eu não ter que olhar para outro lugar”
- **Card depois (vivo):** [estrutura com seta] Pedúnculo cerebral
  - **Verso depois:** [IMG b2c9eed7ce361447b478cfdfce185797.jpg]
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1792261732797 (2026-uc07-introducao-ao-sistema-nervoso-sistema-nervoso-central-introducao-ao-encefalo)
- **Card antes:** {{c1:: Mesencéfalo }}
- **Davi, rodada 1 (2026-10-22):** “card ficou zuado”
- **Card depois (vivo):** [IMG kh-mesencephalon-2.jpg] / {{c1::Mesencéfalo}}
  - **Verso depois:** Parte superior do tronco encefálico, situada entre a ponte e o diencéfalo.
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792261811401 (2026-uc07-telencefalo-e-cortex-cerebral-homunculo-motor-e-sensitivo)
- **Card antes:** O giro {{c1::pós}}-central é a área {{c2::somestésica}} primária (lobo parietal)
- **Davi, rodada 1 (2026-10-22):** “num card assim, pode ter no comentário alguma informação dessa área, tipo o que é somestésica”
- **Card depois (vivo):** O giro {{c1::pós}}-central é a área {{c2::somestésica}} primária (lobo parietal)
  - **Verso depois:** - Área somestésica: relativa à sensibilidade somática (tato, dor, temperatura e propriocepção); corresponde ao córtex somatossensitivo primário (áreas 3, 1 e 2 de Brodmann). / / [IMG e471a62e6fae4d390299a1d3bc903a36.png]
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1792264998268 (2026-uc07-introducao-ao-sistema-nervoso-sistema-nervoso-periferico-nervos-ganglios-e-plexos)
- **Card antes:** Qual estrutura a seta indica? {{c1::Raiz posterior}}
- **Davi, rodada 1 (2026-10-22):** “faltou tirar uma image”
- **Card depois (vivo):** Qual estrutura a seta indica? {{c1::Raiz posterior}} / / [IMG paste-f5d861916e170604b0e43a5e14f7464a7b5b6266.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792264999465 (?)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “não precisa ter cloze escondendo a estrutura da imagem, basta que haja uma seta e um cloze no nome dela”
- **Card depois (vivo):** [estrutura com seta] Gânglio espinal
  - **Verso depois:** [IMG kh-ganglion-spinale.jpg]
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1792265022241 (2026-uc07-introducao-ao-sistema-nervoso-sistema-nervoso-periferico-nervos-ganglios-e-plexos)
- **Card antes:** Os ramos anteriores dos nervos espinais C5 a T1 formam o plexo {{c1::braquial}}
- **Davi, rodada 1 (2026-10-22):** “esse deck aqui não cobriu tudo do quiz, todos tem que cobrir o quiz todo da unidade”
- **Card depois (vivo):** Os ramos anteriores dos nervos espinais C5 a T1 formam o plexo {{c1::braquial}}
  - **Verso depois:** [IMG 7ff06247b94afad1c090448a244a5d84.webp]
- **Análise:** [cobertura] Deck incompleto ou com repetição no conjunto: faltou cobrir o que a aula/quiz ensina ou sobrou o mesmo fato várias vezes. Planejar a cobertura pelo slide antes de escolher cards (pipeline v7).

### Anti-exemplar · note 1792328824811 (?)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “mts palavras num só cloze”
- **Card depois (vivo):** [estrutura com seta] Sulco mediano posterior da medula espinal
  - **Verso depois:** [IMG kh-posterior-median-sulcus-of-spinal-cord.jpg]
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1792328838620 (?)
- **Card antes:** Qual estrutura a seta indica? {{c1::Artérias vertebrais}}
- **Davi, rodada 1 (2026-10-22):** “seta ruim”
- **Card depois (vivo):** Qual estrutura a seta indica? {{c1::Artérias vertebrais}}
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1792328894044 (?)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “nova regra se há mais de 4 palavras no cloze tem que mostrar uma ou o tanto que for para o cloze ser de no máximo 3”
- **Card depois (vivo):** [estrutura com seta] Ramo posterior do nervo espinal
  - **Verso depois:** [IMG kh-posterior-ramus-of-spinal-nerve.jpg]
- **Análise:** [cloze_longo] Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.

### Anti-exemplar · note 1792328896320 (2026-uc07-medula-espinal-nervos-espinais)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “ficou mt zuado”
- **Card depois (vivo):** [estrutura com seta] Ramo lateral do ramo posterior
  - **Verso depois:** [IMG u7-netter-lateral-muscular-ramus.jpg]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792329457242 (?)
- **Card antes:** O espaço {{c1::subaracnóideo}} contém líquido cerebrospinal e separa a aracnoide da pia-máter
- **Davi, rodada 1 (2026-10-22):** “card fora da formatação anking clássico”
- **Card depois (vivo):** O espaço {{c1::subaracnóideo}} contém líquido cerebrospinal e separa a aracnoide da pia-máter
  - **Verso depois:** [IMG kh-arachnoidea-mater-spinalis.jpg]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792329943440 (2026-uc07-medula-espinal-nervos-espinais)
- **Card antes:** A síndrome da {{c1::cauda equina}} é uma lesão por compressão das raízes espinais de {{c2::L2}} para baixo
- **Davi, rodada 1 (2026-10-22):** “imagem boa para isso, mas ficou zuada”
- **Card depois (vivo):** A síndrome da {{c1::cauda equina}} é uma lesão por compressão das raízes espinais de {{c2::L2}} para baixo
  - **Verso depois:** Geralmente causada por hérnia de disco intervertebral ou tumores. / - Cauda equina: feixe das raízes lombares, sacrais e coccígeas, com aspecto de “cauda de cavalo”. / / [IMG d93b24c80a6780f87cb8e741efe6a5f6.webp]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792329948440 (?)
- **Card antes:** O ramo {{c1::anterior}} do nervo espinal fornece inervação motora (somática ou visceral) ao resto do corpo do nível segmentar, incluindo os membros
- **Davi, rodada 1 (2026-10-22):** “cloze no local ruim”
- **Card depois (vivo):** O ramo {{c1::anterior}} do nervo espinal fornece inervação motora (somática ou visceral) ao resto do corpo do nível segmentar, incluindo os membros
  - **Verso depois:** [IMG kh-anterior-ramus-of-spinal-nerve.jpg]
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1792329951089 (?)
- **Card antes:** Os nervos espinais C1–C7 saem do canal vertebral {{c1::acima}} das vértebras correspondentes
- **Davi, rodada 1 (2026-10-22):** “IMAGEM NO CLOZE”
- **Card depois (vivo):** Os nervos espinais C1–C7 saem do canal vertebral {{c1::acima}} das vértebras correspondentes
  - **Verso depois:** [IMG kh-cap-1099.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792330092316 (?)
- **Card antes:** Cada nervo espinal forma-se pela união de: 1. Raiz {{c1:: anterior }} — axônios {{c1:: eferentes }} 2. Raiz {{c1:: posterior }} — axônios {{c1:: aferentes }}
- **Davi, rodada 1 (2026-10-22):** “card entrega a resposta em si mesmo completando a ideia”
- **Card depois (vivo):** Cada nervo espinal forma-se pela união de: / 1. Raiz {{c1::anterior}} — axônios {{c1::eferentes}} / 2. Raiz {{c1::posterior}} — axônios {{c1::aferentes}}
  - **Verso depois:** O mesmo índice oculta os dois lados do contraste, evitando que um entregue a resposta do outro. / / [IMG kh-anterior-root-of-spinal-nerve.jpg]
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1792330093160 (?)
- **Card antes:** Os axônios aferentes entram na medula espinal pela raiz {{c1:: posterior }} do nervo espinal
- **Davi, rodada 1 (2026-10-22):** “ao invés de sensitivo é bom usar aferente”
- **Card depois (vivo):** Os axônios aferentes entram na medula espinal pela raiz {{c1::posterior}} do nervo espinal
  - **Verso depois:** Aferente descreve a direção em relação ao SNC; essas fibras conduzem informação somática ou visceral da periferia ao sistema nervoso central. / / [IMG kh-nervus-spinalis.jpg]
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1792330094311 (?)
- **Card antes:** Os corpos dos neurônios motores somáticos ficam no corno anterior da {{c1:: substância cinzenta }} da medula espinal
- **Davi, rodada 1 (2026-10-22):** “imagem fora de contexto”
- **Card depois (vivo):** Os corpos dos neurônios motores somáticos ficam no corno anterior da {{c1::substância cinzenta}} da medula espinal
  - **Verso depois:** [IMG kh-anterior-horn-of-spinal-cord.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792330246172 (?)
- **Card antes:** As três partes principais do encéfalo são: 1. {{c1:: Cérebro }} 2. {{c2:: Cerebelo }} 3. {{c3:: Tronco encefálico }}
- **Davi, rodada 1 (2026-10-22):** “mesma coisa: pode ter mais coisa por card”
- **Card depois (vivo):** As três partes principais do encéfalo são: / 1. {{c1::Cérebro}} / 2. {{c2::Cerebelo}} / 3. {{c3::Tronco encefálico}}
  - **Verso depois:** [IMG kh-brainstem.jpg]
- **Análise:** [repetido] Card repetido ou muito parecido com outro: confunde e gasta revisão. Um fato, um card; o outro aspecto vai no verso ou em card com ganho próprio.

### Anti-exemplar · note 1792330249686 (?)
- **Card antes:** O tronco encefálico é formado por: 1. {{c1:: Mesencéfalo }} 2. {{c2:: Ponte }} 3. {{c3:: Bulbo }}
- **Davi, rodada 1 (2026-10-22):** “pode ter mais de um cloze por card estilo tópico assim economizamos cards”
- **Card depois (vivo):** O tronco encefálico é formado por: / 1. {{c1::Mesencéfalo}} / 2. {{c2::Ponte}} / 3. {{c3::Bulbo}}
  - **Verso depois:** [IMG kh-brainstem.jpg]
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1792338715108 (?)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “seta errada”
- **Card depois (vivo):** [estrutura com seta] Núcleo espinal do nervo trigêmeo
  - **Verso depois:** [IMG kh-nucleus-spinalis-nervi-trigemini.jpg]
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1792339386764 (2026-uc07-nervos-cranianos-nervo-olfatorio-i)
- **Card antes:** Qual é a função do nervo craniano I (olfatório)? {{c1::Olfato}}
- **Davi, rodada 1 (2026-10-22):** “card mt bobo”
- **Card na rodada 2:** O nervo olfatório (I) chega ao bulbo olfatório atravessando a {{c1::lâmina crivosa}} do etmoide
- **Davi, rodada 2 (2026-10-23):** “(Claude): card reescrito: em vez de perguntar a função (bobo), pergunta por onde o I sai e por que o trauma tira o olfato”
- **Card depois (vivo):** O nervo olfatório (I) chega ao bulbo olfatório atravessando a {{c1::lâmina crivosa}} do etmoide
  - **Verso depois:** - Por isso a fratura da lâmina crivosa no trauma de crânio rompe os filamentos e causa anosmia / / [IMG kh-nervus-olfactorius.jpg]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792344677325 (2026-uc07-cerebelo-cortex-cerebelar)
- **Card antes:** A camada molecular do córtex cerebelar contém células {{c1:: em cesto }} e {{c2:: estreladas }}
- **Davi, rodada 1 (2026-10-22):** “faltou card organizador, com mais infos”
- **Card na rodada 2:** A camada molecular do córtex cerebelar contém células {{c1:: em cesto }} e {{c1:: estreladas }}
- **Davi, rodada 2 (2026-10-23):** “(Claude): organizador criado (ce-camadas: as três camadas e as células de cada uma)”
- **Card depois (vivo):** A camada molecular do córtex cerebelar contém células {{c1::em cesto}} e {{c1::estreladas}}
  - **Verso depois:** [IMG fdf0f05d2e06612ca1710806b8e40415.jpg]
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1792572870665 (2026-uc07-introducao-ao-sistema-nervoso-sistema-nervoso-periferico-nervos-ganglios-e-plexos)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-22):** “não precisa ter cloze escondendo a estrutura da imagem, basta que haja uma seta e um cloze no nome dela”
- **Card depois (vivo):** [estrutura com seta] Gânglio espinal
  - **Verso depois:** [IMG kh-ganglion-spinale.jpg]
- **Análise:** [io] Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.

### Anti-exemplar · note 1792588686964 (2026-uc07)
- **Card antes:** Cada nervo espinal forma-se pela união de: 1. Raiz {{c1:: anterior }} — axônios {{c1:: eferentes }} 2. Raiz {{c1:: posterior }} — axônios {{c1:: aferentes }}
- **Davi, rodada 1 (2026-10-22):** “card entrega a resposta em si mesmo completando a ideia ESSE comentário é mt ruim”
- **Card depois (vivo):** Cada nervo espinal forma-se pela união de: / 1. Raiz {{c2::anterior}}— axônios {{c1::eferentes}} / 2. Raiz {{c2::posterior}} — axônios {{c1::aferentes}}
  - **Verso depois:** O mesmo índice oculta os dois lados do contraste, evitando que um entregue a resposta do outro. / / [IMG kh-anterior-root-of-spinal-nerve.jpg]
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1792588686965 (2026-uc07)
- **Card antes:** Os axônios aferentes entram na medula espinal pela raiz {{c1:: posterior }} do nervo espinal
- **Davi, rodada 1 (2026-10-22):** “ao invés de sensitivo é bom usar aferente”
- **Card depois (vivo):** Os axônios aferentes entram na medula espinal pela raiz {{c1::posterior}} do nervo espinal
  - **Verso depois:** Aferente descreve a direção em relação ao SNC; essas fibras conduzem informação somática ou visceral da periferia ao sistema nervoso central. / / [IMG kh-nervus-spinalis.jpg]
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.

### Anti-exemplar · note 1792588686966 (2026-uc07)
- **Card antes:** Os corpos dos neurônios motores somáticos ficam no corno anterior da {{c1:: substância cinzenta }} da medula espinal
- **Davi, rodada 1 (2026-10-22):** “imagem fora de contexto”
- **Card depois (vivo):** Os corpos dos neurônios motores somáticos ficam no corno anterior da {{c1::substância cinzenta}} da medula espinal
  - **Verso depois:** [IMG kh-anterior-horn-of-spinal-cord.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792588686968 (2026-uc07)
- **Card antes:** As três partes principais do encéfalo são: 1. {{c1:: Cérebro }} 2. Cerebelo 3. {{c1:: Tronco encefálico }}
- **Davi, rodada 1 (2026-10-22):** “mesma coisa: pode ter mais coisa por card MELHOREI”
- **Card depois (vivo):** As três partes principais do encéfalo são: / 1. {{c1::Cérebro}} / 2. Cerebelo / 3. {{c1::Tronco encefálico}}
  - **Verso depois:** [IMG kh-brainstem.jpg]
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1792588686971 (2026-uc07)
- **Card antes:** O tronco encefálico é formado por: 1. {{c1:: Mesencéfalo }} 2. {{c1:: Ponte }} 3. {{c1:: Bulbo }}
- **Davi, rodada 1 (2026-10-22):** “pode ter mais de um cloze por card estilo tópico assim economizamos cards melhorei o card, mas agora tem que sempre excluir quando fica assim faltando um dos clozes porque apaguei na edição”
- **Card depois (vivo):** O tronco encefálico é formado por: / 1. {{c1::Mesencéfalo}} / 2. {{c1::Ponte}} / 3. {{c1::Bulbo}}
  - **Verso depois:** [IMG kh-brainstem.jpg]
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1792588686986 (2026-uc07)
- **Card antes:** A dorsiflexão do tornozelo depende de L4 e {{c1::L5}}; a flexão plantar, de S1 e {{c2::S2}}
- **Davi, rodada 1 (2026-10-22):** “imagem errada”
- **Card depois (vivo):** A dorsiflexão do tornozelo depende de L4 e {{c1::L5}}; a flexão plantar, de S1 e {{c2::S2}}
  - **Verso depois:** [IMG kh-myotomes-l4-and-l5.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792588687006 (2026-uc07)
- **Card antes:** O gânglio vestibular tem uma parte superior e uma parte {{c1::inferior}}
- **Davi, rodada 1 (2026-10-22):** “DÁ PARA MELHORAR, FICOU MT RUIM”
- **Card depois (vivo):** O gânglio vestibular tem uma parte superior e uma parte {{c1::inferior}}
  - **Verso depois:** [IMG kh-pars-superior-ganglii-vestibularis.jpg]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792588687018 (2026-uc07)
- **Card antes:** O cerebelo fica posterior à ponte e ao bulbo, na fossa {{c1::posterior}} do crânio
- **Davi, rodada 1 (2026-10-22):** “imagem ruim”
- **Davi, rodada 2 (2026-10-23):** “(Claude): figura trocada por uma vista do encéfalo em que se vê o cerebelo atrás do tronco, na fossa posterior”
- **Card depois (vivo):** O cerebelo fica posterior à ponte e ao bulbo, na fossa {{c1::posterior}} do crânio
  - **Verso depois:** [IMG kh-cerebellum.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792588687019 (2026-uc07)
- **Card antes:** O córtex cerebelar tem três camadas: {{c1::molecular}} (externa), de {{c2::Purkinje}} (média) e {{c1::granulosa}} (interna)
- **Davi, rodada 1 (2026-10-22):** “imagem ruim”
- **Davi, rodada 2 (2026-10-23):** “(Claude): figura trocada pela das camadas do córtex cerebelar (AnKing)”
- **Card depois (vivo):** O córtex cerebelar tem três camadas: {{c1::molecular}} (externa), de {{c2::Purkinje}} (média) e {{c1::granulosa}} (interna)
  - **Verso depois:** [IMG 9aced0d1052fdbc0be7c61c29481b699.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792588687021 (2026-uc07)
- **Card antes:** As estruturas de substância cinzenta do cerebelo são o córtex cerebelar e os núcleos {{c1::cerebelares}}
- **Davi, rodada 1 (2026-10-22):** “imagem”
- **Davi, rodada 2 (2026-10-23):** “(Claude): figura trocada pela do córtex cerebelar com camadas e núcleos profundos”
- **Card depois (vivo):** As estruturas de substância cinzenta do cerebelo são o córtex cerebelar e os núcleos {{c1::cerebelares}}
  - **Verso depois:** [IMG 9aced0d1052fdbc0be7c61c29481b699.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792588687023 (2026-uc07)
- **Card antes:** Do medial para o lateral, os núcleos do cerebelo são o {{c2::fastigial}}, o {{c1::globoso}}, o {{c2::emboliforme}} e o {{c1::denteado}}
- **Davi, rodada 1 (2026-10-22):** “melhorei o card imagem zuada”
- **Davi, rodada 2 (2026-10-23):** “(Claude): figura trocada pela dos quatro núcleos profundos lado a lado (AnKing)”
- **Card depois (vivo):** Do medial para o lateral, os núcleos do cerebelo são o {{c2::fastigial}}, o {{c1::globoso}}, o {{c2::emboliforme}} e o {{c1::denteado}}
  - **Verso depois:** [IMG 140faecd24bf8653274f35a5a8097516.jpg]
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791625435907 (2026-uc03-imunologia-45-ativacao-linfocitos-t)
- **Card antes:** Tregs survive on {{c1:: IL-2 }} made by activated conventional T cells
- **Davi, rodada 1 (2026-10-23):** “poderia ser um card que explica mais”
- **Card depois (vivo):** Tregs cannot make their own {{c1::IL-2}} and survive on the IL-2 secreted by activated conventional T cells
  - **Verso depois:** - FOXP3 represses the IL-2 gene, yet Tregs carry high CD25, the IL-2 receptor α chain / - By consuming IL-2 they also starve nearby effector T cells, one of their ways to suppress
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1791631347467 (2026-uc03-biologia-molecular-52-expressao-eucariotos-ii)
- **Card antes:** HDAC inhibitors prevent histones from being {{c1:: deacetylated }} resulting in genes such as tumor suppressors being {{c2:: transcribed }}
- **Davi, rodada 1 (2026-10-23):** “isso é um bom exemplo de card que poderia ser simples, mas ensina e ajuda a decorar com extrema eficácia: poderia ser só um card perguntando o que faz HDAC, mas já há informação sobre inibidores dessa enzima e o resultado do que acontece ao inibi-lo + um comentário que aprofunda ainda mais ótimo card”
- **Card depois (vivo):** HDAC inhibitors prevent histones from being {{c1::deacetylated}} resulting in genes such as tumor suppressors being {{c2::transcribed}}
  - **Verso depois:** [IMG a4794dc612338ff62357e1a81d0dea71.jpg] / / - Approved for some lymphomas and multiple myeloma
- **Análise:** [elogio] Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).

### Anti-exemplar · note 1791762424899 (2026-uc19-farmacologia-01-introducao-mecanismos)
- **Card antes:** Phenobarbital induces CYP enzymes and so {{c1:: reduces }} the anticoagulant effect of warfarin
- **Davi, rodada 1 (2026-10-23):** “fazer uma lista dos inibidores e potenciadores da PCYP450, daí vira card conexão”
- **Card depois (vivo):** Phenobarbital induces CYP enzymes and so {{c1::reduces}} the anticoagulant effect of warfarin
  - **Verso depois:** - Phenytoin and carbamazepine are also potent inducers
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1792065187180 (2026-uc03-grand-round-04-paracoccidioidomicose)
- **Card antes:** Clinical forms of paracoccidioidomycosis : - {{c1:: chronic adult }} form: about 90%, mostly men, lungs and mucosa - {{c2:: acute juvenile }} form: 3–5%, most severe, lymph nodes, liver and spleenc
- **Davi, rodada 1 (2026-10-23):** “pode melhorar ser mais profundo, ter um cloze num local melhor”
- **Card depois (vivo):** Clinical forms of paracoccidioidomycosis: / - chronic (adult): a latent focus in the {{c1::lungs}} reactivates and reaches the mucosa / - acute (juvenile): spreads to the {{c2::reticuloendothelial}} system, nodes, liver and spleen
  - **Verso depois:** - The adult form is about 90% of cases, mostly in men: estrogen blocks the mold-to-yeast switch / - The juvenile form (3–5%) follows a weak Th1 response and is the most severe
- **Análise:** [cloze_local] Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.

### Anti-exemplar · note 1792328913378 (2026-uc07-medula-espinal-topografia-e-morfologia-da-medula-espinal)
- **Card antes:** Se há corno lateral , a medula espinal está entre {{c2::T1}} e {{c2::L2}}
- **Davi, rodada 1 (2026-10-23):** “imagem zuada (Claude): figura trocada pelos cortes da medula por nível (a do Kenhub não mostrava o corno lateral no corte)”
- **Card depois (vivo):** Se há corno lateral, a medula espinal está entre {{c2::T1}} e {{c2::L2}}
  - **Verso depois:** - Os neurônios pré-ganglionares simpáticos ficam no corno lateral, e só esses segmentos os têm / / [IMG 393da414ecb28c7a423c83bfa7a1ccea.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792328914296 (2026-uc07-medula-espinal-topografia-e-morfologia-da-medula-espinal)
- **Card antes:** Se não há corno lateral, a medula espinal está entre {{c1::C1}} e {{c1::C8}} ou {{c1::L3}} e {{c1::S5}}
- **Davi, rodada 1 (2026-10-23):** “imagem ruim, poderia ser outra (Claude): figura trocada pelos cortes da medula por nível, em que se vê onde há e onde não há corno lateral”
- **Card depois (vivo):** Se não há corno lateral, a medula espinal está entre {{c1::C1}} e {{c1::C8}} ou {{c1::L3}} e {{c1::S5}}
  - **Verso depois:** - Sem corno lateral: fora do trecho simpático T1–L2 / / [IMG 393da414ecb28c7a423c83bfa7a1ccea.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792328916159 (2026-uc07-medula-espinal-topografia-e-morfologia-da-medula-espinal)
- **Card antes:** Se o corno anterior é grande, o nível da medula espinal está entre {{c1::C5}} e {{c1::T1}} ou {{c1::L2}} e {{c1::S2}}
- **Davi, rodada 1 (2026-10-23):** “imagem (Claude): figura trocada pelos cortes da medula por nível (corno anterior grande nas intumescências)”
- **Card depois (vivo):** Se o corno anterior é grande, o nível da medula espinal está entre {{c1::C5}} e {{c1::T1}} ou {{c1::L2}} e {{c1::S2}}
  - **Verso depois:** - C5–T1 e L2–S2 são as intumescências: neurônios motores dos membros / / [IMG 393da414ecb28c7a423c83bfa7a1ccea.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792572870673 (2026-uc07-medula-espinal-nervos-espinais)
- **Card antes:** (sem texto: estrutura/imagem)
- **Davi, rodada 1 (2026-10-23):** “poderia colocar a altura aqui no cloze entre parênteses”
- **Card depois (vivo):** [estrutura com seta] Intumescência cervical (C4–T1)
  - **Verso depois:** [IMG kh-cervical-enlargement.jpg]
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).

### Anti-exemplar · note 1792588686967 (2026-uc07)
- **Card antes:** A sinapse entre os neurônios pré e pós-ganglionares ocorre no gânglio {{c1::autônomo}}, onde ficam os corpos dos neurônios pós-ganglionares
- **Davi, rodada 1 (2026-10-23):** “PODE MELHORAR ESSE CARD”
- **Card depois (vivo):** Via eferente visceral (autônoma): / - neurônio pré-ganglionar: corpo no {{c1::SNC}} / - sinapse no {{c2::gânglio autônomo}} / - neurônio pós-ganglionar: do gânglio ao {{c3::órgão efetor}}
  - **Verso depois:** - Na via somática basta um neurônio do SNC ao músculo; na visceral são dois, com sinapse no gânglio / [IMG kh-autonomic-ganglion.jpg]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792588686980 (2026-uc07)
- **Card antes:** A cavidade do tubo neural origina o {{c1::aqueduto cerebral}}, o {{c2::quarto ventrículo}} e o {{c3::canal central}} da medula espinal
- **Davi, rodada 1 (2026-10-23):** “poderia ser com 3 clozes, um só card e tópicos”
- **Card depois (vivo):** A cavidade do tubo neural origina, no tronco e na medula: / - mesencéfalo: {{c1::aqueduto cerebral::a…}} / - ponte e bulbo: {{c1::quarto ventrículo::q…}} / - medula espinal: {{c1::canal central::c…}}
  - **Verso depois:** - No prosencéfalo a mesma cavidade forma os ventrículos laterais e o terceiro ventrículo / [IMG kh-cap-3490.jpg]
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova). Aqui: Três itens em frase com três índices: virou organizador em pé com um índice e dica da 1ª letra.

### Anti-exemplar · note 1792624465974 (2026-uc19-farmacologia-02-farmacocinetica-i)
- **Card antes:** The hepatic clearance of a drug with: - high E (lidocaine) depends on {{c1:: blood flow }} - low E (warfarin) depends on {{c2:: enzyme activity }}
- **Davi, rodada 1 (2026-10-23):** “um card tem que fazer sentido sozinho isso do E não faz sentido sozinho”
- **Card depois (vivo):** Hepatic clearance depends on the extraction ratio (fraction removed in one pass): / - high-extraction drugs (lidocaine): {{c1::blood flow}} / - low-extraction drugs (warfarin): {{c2::enzyme activity}}
  - **Verso depois:** - A high-extraction liver clears almost all that arrives, so only more flow clears more / - A low-extraction liver is limited by its enzymes and by the free fraction
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares. Aqui: Símbolo 'E' sem definição: card não faz sentido sozinho (gate v7: símbolo de uma letra).

### Anti-exemplar · note 1792657543181 (2026-uc19-farmacologia-02-farmacocinetica-i)
- **Card antes:** An organ cannot clear more than the blood that reaches it, so its clearance is capped by its {{c1:: blood flow }}
- **Davi, rodada 1 (2026-10-23):** “card estranho”
- **Card depois (vivo):** Organ clearance is blood flow times extraction ratio, so it can never exceed the organ's {{c1::blood flow}}
  - **Verso depois:** - Extraction ratio: fraction of drug removed in one pass, from 0 to 1 / - When it is 1, everything that arrives is cleared and clearance equals blood flow
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792659585105 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** Cephalocaudal and lateral folding pull the endoderm inside the embryo and close it into the {{c1:: primitive gut }} tube
- **Davi, rodada 1 (2026-10-23):** “negrito tem que ser gate hard, checado card a card”
- **Card depois (vivo):** Cephalocaudal and lateral folding of the embryo pull the endoderm inside and close it into the {{c1::primitive gut}} tube
  - **Verso depois:** - The yolk sac stays outside, connected by the vitelline duct / - The tube ends blind at both ends, in the foregut and hindgut / [IMG langman-15-1.png]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1792659586974 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** Layers of the gut wall : - epithelium and gland cells: {{c1:: endoderm }} - muscle, connective tissue, serosa: {{c1:: splanchnic mesoderm }}
- **Davi, rodada 1 (2026-10-23):** “faltou falar que era sobre embrio”
- **Card depois (vivo):** Embryonic origin of the gut wall layers: / - epithelium and glands: {{c1::endoderm}} / - muscle, connective tissue, serosa: {{c1::splanchnic mesoderm}}
  - **Verso depois:** - Splanchnic mesoderm lines the gut, while somatic mesoderm lines the body wall / [IMG langman-15-3.png]
- **Análise:** [aula] Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina. Aqui: Organizador de embriologia sem dizer que é embriologia na frente (gate v7: contexto embriológico).

### Anti-exemplar · note 1792659587475 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** The septum transversum is splanchnic mesoderm that forms the central tendon of the {{c1:: diaphragm }} and receives the {{c1:: liver }}
- **Davi, rodada 1 (2026-10-23):** “NEGRITO pode aprofundar e melhorar escrita gate-hard: cada autoral tem que ser inspirado num exemplar específico, para tentar sair como modelo, mas mudando o conteúdo gate-hard: cada autoral deve ser revisto no fim para boa escrita, cloze no local adequado, aprofundamento grande e negrito”
- **Card depois (vivo):** In the embryo, the septum transversum receives the growing {{c1::liver}} and later forms the central tendon of the {{c2::diaphragm}}
  - **Verso depois:** - It is mesoderm between the heart and the yolk-sac stalk / - Around the liver it gives the capsule, the lesser omentum and the falciform ligament / [IMG langman-15-15.png]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1792659588552 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** The rotation of the stomach pulls the dorsal mesogastrium to the left and opens the {{c1:: omental bursa }} behind it
- **Davi, rodada 1 (2026-10-23):** “IMAGEM”
- **Card depois (vivo):** Rotation of the stomach in the embryo pulls the dorsal mesogastrium left, opening the {{c1::omental bursa}} behind it
  - **Verso depois:** - The bursa opens to the rest of the peritoneal cavity through the epiploic foramen / [IMG langman-15-9.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792659592051 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** After the return, the ascending and descending colon fuse to the posterior wall and become {{c1:: secondarily retroperitoneal }}
- **Davi, rodada 1 (2026-10-23):** “imagem”
- **Card depois (vivo):** After the embryonic gut returns, the ascending and descending colon fuse posteriorly and become {{c1::secondarily retroperitoneal}}
  - **Verso depois:** - Their mesocolon fuses with the posterior parietal peritoneum / - The mesentery proper of the small intestine stays free / [IMG langman-15-30.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792659596102 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** The endoderm that was folded into the gut tube now buds out the {{c1:: liver }} and the {{c1:: pancreas }}
- **Davi, rodada 1 (2026-10-23):** “IMAGEM”
- **Card depois (vivo):** In the embryo, the foregut endoderm buds out the {{c1::liver}} and the {{c1::pancreas}}
  - **Verso depois:** - Both buds grow from the duodenal region into the surrounding mesoderm, which gives their connective tissue / [IMG langman-15-19.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792659596600 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** The liver starts as the {{c1:: hepatic bud }}, an outgrowth of the caudal foregut endoderm that invades the septum transversum
- **Davi, rodada 1 (2026-10-23):** “NEGRITO IMAGEM”
- **Card depois (vivo):** The embryonic liver starts in week 3 as the {{c1::hepatic bud}}, an outgrowth of foregut endoderm into the septum transversum
  - **Verso depois:** - Its connection with the gut narrows into the bile duct / [IMG langman-15-14.png]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1792659597350 (2026-uc08-anatomia-11-figado-pancreas-vias-biliares)
- **Card antes:** Which GI ligament connects the liver to the anterior abdominal wall ? {{c1::Falciform ligament}}
- **Davi, rodada 1 (2026-10-23):** “IMAGEM”
- **Card depois (vivo):** Which GI ligament connects the liver to the anterior abdominal wall? / {{c1::Falciform ligament}}
  - **Verso depois:** - It comes from the ventral mesentery that the liver grew into / [IMG langman-15-16.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792659597673 (2026-uc08-anatomia-11-figado-pancreas-vias-biliares)
- **Card antes:** The remnant of the umbilical vein is the {{c1:: ligamentum teres hepatis }}, which is contained in the {{c2:: falciform ligament }}
- **Davi, rodada 1 (2026-10-23):** “IMAGEM”
- **Card depois (vivo):** The remnant of the umbilical vein is the {{c1::ligamentum teres hepatis}}, which is contained in the {{c2::falciform ligament}}
  - **Verso depois:** - The umbilical vein closes after birth and leaves this ligament / [IMG langman-15-10.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792659598025 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** The hepatic cords mix with the vitelline and umbilical veins, and these vessels become the {{c1:: sinusoids }}
- **Davi, rodada 1 (2026-10-23):** “IMAGEM + negrito pôr gate-hard nesses dois imagens tem que ter, baseando-se nos que já tem tem que ser feita fazer esse julgamento card poderia aprofundar mais”
- **Card depois (vivo):** In the embryonic liver, hepatic cords grow around the vitelline and umbilical veins, whose branches become the {{c1::sinusoids}}
  - **Verso depois:** - So gut blood (vitelline, later the portal vein) and placental blood (umbilical) pass between hepatocytes / - The vitelline veins later form the portal vein / [IMG langman-13-47.png]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7). Aqui: Embriologia sem figura e sem aprofundamento; refeito com a figura do Langman (veias vitelinas → sinusoides).

### Anti-exemplar · note 1792659598275 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** The rotation of the stomach and duodenum places the liver on the {{c1:: right }} and the spleen on the {{c1:: left }}
- **Davi, rodada 1 (2026-10-23):** “esse deck tem coisa de embrio do foregut e hindgut tb? se não tiver, colocar alguns autorais com qualidade resolver negritos tb de todos os cards”
- **Card depois (vivo):** Rotation of the stomach in the embryo moves the liver to the {{c1::right}} and the spleen to the {{c1::left}}
  - **Verso depois:** - The liver was at first on the midline / - The spleen develops in the dorsal mesogastrium, which swings left with the stomach / [IMG langman-15-10.png]
- **Análise:** [negrito] Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).

### Anti-exemplar · note 1792659598525 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** The pancreas forms from a {{c1:: dorsal }} and a {{c1::ventral}} bud of the duodenal endoderm
- **Davi, rodada 1 (2026-10-23):** “IMAGEM esse card poderia aprofundar um pouco mais na explicação cobrando o mesmo conceito”
- **Card depois (vivo):** The embryonic pancreas forms from a {{c1::dorsal}} and a {{c1::ventral}} bud of duodenal endoderm
  - **Verso depois:** - Dorsal bud: most of the gland, body and tail / - Ventral bud: uncinate process and lower head, next to the bile duct / [IMG langman-15-19.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792659598777 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** The duodenum swings right and carries the {{c1:: ventral }} pancreatic bud behind it to meet the dorsal bud
- **Davi, rodada 1 (2026-10-23):** “card ficou zuado, mas a ideia foi boa”
- **Card depois (vivo):** As the embryonic duodenum rotates, the {{c1::ventral}} pancreatic bud swings behind it and fuses with the {{c1::dorsal}} bud
  - **Verso depois:** - The main pancreatic duct joins the ventral duct with the distal dorsal duct / - If the ducts fail to fuse, the result is pancreas divisum / [IMG langman-15-20.png]
- **Análise:** [estranho] Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.

### Anti-exemplar · note 1792659599275 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** Which embryological pancreatic bud(s) contribute to the uncinate process ? {{c1::Ventral pancreatic buds}}
- **Davi, rodada 1 (2026-10-23):** “imagem”
- **Card depois (vivo):** Which embryological pancreatic bud(s) contribute to the uncinate process? / {{c1::Ventral pancreatic buds}}
  - **Verso depois:** EmbryologyStructures FormedVentral Pancreatic BudsUncinate processDorsal Pancreatic BudsAccessory pancreatic duct, body, tail, isthmus of the pancreasVentral & Dorsal Pancreatic BudsMain pancreatic duct, head of the pancreas / [IMG langman-15-20.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792659600102 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** Which embryological pancreatic bud(s) contribute to the accessory pancreatic duct ? {{c1::Dorsal pancreatic buds}}
- **Davi, rodada 1 (2026-10-23):** “imagem”
- **Card depois (vivo):** Which embryological pancreatic bud(s) contribute to the accessory pancreatic duct? / {{c1::Dorsal pancreatic buds}}
  - **Verso depois:** EmbryologyStructures FormedVentral Pancreatic BudsUncinate processDorsal Pancreatic BudsAccessory pancreatic duct, body, tail, isthmus of the pancreasVentral & Dorsal Pancreatic BudsMain pancreatic duct, head of the pancreas / [IMG langman-15-20.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792659601153 (2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas)
- **Card antes:** The pancreas ends up {{c1:: retroperitoneal }} because the duodenum and its mesentery fuse with the posterior abdominal wall
- **Davi, rodada 1 (2026-10-23):** “imagem”
- **Card depois (vivo):** The embryonic pancreas becomes {{c1::retroperitoneal}} when the duodenum and its mesentery fuse with the posterior wall
  - **Verso depois:** - The dorsal mesoduodenum disappears, so the gland lies against the posterior wall / [IMG langman-15-17.png]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792695019665 (2026-uc03-microbiologia-58-multiplicacao-viral-antivirais)
- **Card antes:** After HIV gp120 binds CD4 and the coreceptor, it changes shape and exposes {{c1:: gp41 }}, which inserts into the membrane
- **Davi, rodada 1 (2026-10-23):** “explicação ruim do mecanismo tem que cobrar decoreba num ou dois bons clozes E explicar um processo bem”
- **Card depois (vivo):** HIV {{c2::gp120}} binds CD4 and a coreceptor, which exposes {{c1::gp41}} to fuse the envelope with the cell membrane
  - **Verso depois:** - gp120 binds CD4 → changes shape → binds CCR5 or CXCR4 / - gp41 harpoons into the cell membrane and folds back like a zipper, pulling the two membranes together / - Enfuvirtide binds gp41 and blocks this fold
- **Análise:** [porque] Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.

### Anti-exemplar · note 1792696993158 (2026-uc07)
- **Card antes:** O tronco encefálico vai do plano do {{c1::forame magno}} até os {{c2::pedúnculos cerebrais}}
- **Davi, rodada 1 (2026-10-23):** “imagem ruim”
- **Card depois (vivo):** O tronco encefálico vai do plano do {{c1::forame magno}} até os {{c2::pedúnculos cerebrais}}
  - **Verso depois:** - Fica entre a medula e o diencéfalo e à frente do cerebelo, que cobre sua face posterior / [IMG kh-brainstem.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792697127074 (2026-uc07)
- **Card antes:** O canal vertebral começa na articulação {{c1::atlantoccipital}}, entre o osso occipital e o {{c2::atlas}} (C1)
- **Davi, rodada 1 (2026-10-23):** “IMAGEM”
- **Card depois (vivo):** O canal vertebral começa na articulação {{c1::atlantoccipital}}, entre o osso occipital e o {{c2::atlas}} (C1)
  - **Verso depois:** - É ali, no forame magno, que o bulbo continua como medula espinal / [IMG khref-abfdce9d7a55f0e8fa23-back.jpg]
- **Análise:** [imagem] Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).

### Anti-exemplar · note 1792697128629 (2026-uc07)
- **Card antes:** Plexos por região da medula: 1. cervical: plexo {{c1::cervical}} (pescoço) e plexo {{c2::braquial}} (membro superior) 2. lombossacral: plexo {{c3::lombossacral}} (membro inferior) 3. torácica: {{c4::n
- **Davi, rodada 1 (2026-10-23):** “escrita estranha AJUSTA PARA SER EM TÓPICOS”
- **Card depois (vivo):** Plexos por região da medula: / - cervical: plexos {{c1::cervical}} (pescoço) e {{c2::braquial}} (membro superior) / - lombossacral: plexo {{c3::lombossacral}} (membro inferior) / - torácica: {{c4::nenhum}}
  - **Verso depois:** - Os plexos se formam onde muitas raízes vão ao mesmo território; no tórax cada nervo intercostal segue sozinho / [IMG kh-brachial-plexus.jpg]
- **Análise:** [organizador] Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova). Aqui: Enumeração numerada em linha: devia ser organizador em pé (gate v7).

## Suspensos por Davi (cards que ele estudou e tirou)

- **Análise:** Davi suspende o card que não o ajuda a gravar um mecanismo da aula a longo prazo. Os padrões: (1) moldura genérica sem mecanismo ('fígado e neurônio têm o mesmo genoma', 'a expressão é controlada em vários níveis', 'a maior parte da regulação é na iniciação', 'um gene tem dezenas de fatores'); (2) nome solto de uma cadeia picada em vários cards (TFIID, TFIIB, BRE, cauda da RNA pol II, cada um num card), em vez de um card que conta o processo; (3) detalhe de experimento ou de organismo-modelo sem o princípio que ele prova (Gal4/UAS, híbrido LexA, Pho4, geleia real, gêmeos, iPS); (4) número ou definição isolada (80% dos CpG, 'HATs transferem acetil', constitutiva × facultativa, HP1, bromodomínio); (5) repetidos e AnKing fora do recorte (RNA pol I/II/III duplicados, 30 nm, lisina/arginina). O que ele mantém carrega função + consequência e se encaixa na história da aula: acetilação abre a cromatina, inibidor de HDAC volta a transcrever supressores, metiltransferase de manutenção copia a marca, repressor recruta HDAC, domínio de ligação × de ativação, FOXO1 fora do núcleo desliga a gliconeogênese. Regra: o autoral só nasce de um conceito que precisa durar (motivação) e carrega o processo, não o nome.

### 2026-uc03-biologia-molecular-18-recombinacao — 1 suspensos
- (acervo) note 1791629589372: The enzymes responsible for gene recombination in heavy and light chains are encoded by the genes {{c1::RAG1}} and {{c1::RAG2}}

### 2026-uc03-biologia-molecular-29-operon-procariotos — 5 suspensos
- (autoral) note 1791664577750: Some bacteria switch fimbriae on and off by {{c1::inverting}} their promoter through recombination
- (autoral) note 1791664578043: Regulation by a repressor is called {{c1::negative}} control, whereas regulation by an activator is called {{c1::positive}} control
- (autoral) note 1791664583970: X-gal does not bind the Lac repressor, so it reports β-galactosidase activity without {{c1::inducing}} the operon
- (autoral) note 1791664584596: In a partial diploid, is an Oc mutation dominant or recessive? / / {{c1::Dominant}}
- (autoral) note 1791664584721: An Oc mutation affects only the genes on its own DNA molecule, so it acts in {{c1::cis}}

### 2026-uc03-biologia-molecular-46-expressao-eucariotos-i — 18 suspensos
- (autoral) note 1791627546174: Most gene regulation happens at the {{c1::initiation}} of transcription
- (autoral) note 1791627546802: Unlike bacterial regulators, eukaryotic activators and repressors mostly act on RNA polymerase II {{c1::indirectly}}
- (acervo) note 1791627547776: Are enhancers/silencers close or far from the gene it regulates? / {{c1::May be close to, far from, or within the gene (in an intron)}}
- (autoral) note 1791627548276: The TATA-binding protein, which recognizes the TATA box, is a subunit of the general factor {{c1::TFIID}}
- (autoral) note 1791627548403: In an RNA polymerase II promoter, the BRE beside the TATA box is recognized by {{c1::TFIIB}}
- (autoral) note 1791627548902: The yeast activator {{c1::Gal4}} turns on the genes that metabolize galactose
- (autoral) note 1791627549276: The Gal4 activation domain recruits TFIID, Mediator and {{c1::chromatin-modifying proteins}}
- (autoral) note 1791627549526: Expressing Gal4 under a tissue-specific enhancer turns on a UAS-linked {{c1::transgene}} only in that tissue
- (autoral) note 1791627549777: In bacteria, the signal usually binds the transcription factor {{c1::directly}}, whereas eukaryotic signals often act through signaling pathways
- (autoral) note 1791627549902: Ways to switch on a eukaryotic transcription factor: / 1. {{c1::Ligand::L…}} binding / 2. {{c1::Phosphorylation::P…}} / 3. Unmasking / 4. {{c1::Nuclear entry::N…}}
- (autoral) note 1791627550027: Steroid and thyroid hormones cross the membrane and bind {{c1::nuclear}} receptors, which then act as transcription factors
- (autoral) note 1791627550877: Cytokine-activated JAK kinases phosphorylate {{c1::STAT}} transcription factors
- (autoral) note 1791627551003: High phosphate inactivates the yeast activator Pho4 by {{c1::phosphorylation}}
- (acervo) note 1792082056485: RNA polymerase {{c1::II}} makes {{c2::m}}RNA
- (acervo) note 1792082056911: RNA polymerase {{c1::I}} makes {{c2::r}}RNA
- (acervo) note 1792082057314: RNA polymerase {{c1::III}} makes {{c2::t}}RNA and 5S rRNA
- (autoral) note 1792082060658: The first general transcription factor to bind a TATA promoter is {{c1::TFIID}}, through its TBP subunit
- (autoral) note 1792082060961: After the preinitiation complex forms, phosphorylation of the RNA polymerase II {{c1::tail}} releases it to elongate

### 2026-uc03-biologia-molecular-52-expressao-eucariotos-ii — 18 suspensos
- (acervo) note 1791631343090: With H1, the nucleosome exists as {{c1::30}} nm chromatin
- (acervo) note 1791631343217: What classes of histones are found as a pair in the nucleosome? / {{c1::H2A, H2B, H3, and H4::4}}
- (acervo) note 1791631343467: Histones are rich in the amino acids {{c1::lysine}} and {{c1::arginine}}
- (autoral) note 1791631343592: Histone N-terminal tails stick out of the nucleosome, so enzymes can {{c1::acetylate}} them and loosen the chromatin
- (autoral) note 1791631343715: Some activators bind closed chromatin and then recruit {{c1::remodeling}} complexes that expose nearby sites
- (autoral) note 1791631344117: {{c1::Histone acetyltransferases (HATs)}} transfer acetyl groups to lysines in histone tails
- (autoral) note 1791631344241: {{c1::Histone deacetylases (HDACs)}} remove acetyl groups from lysines in histone tails
- (autoral) note 1791631344366: Acetylation neutralizes the positive charge of lysine, lowering histone affinity for {{c1::DNA}}
- (autoral) note 1791631344792: Histone marks recruit {{c1::reader}} proteins that recognize specific modifications
- (acervo) note 1791631345492: What form of chromatin is highly condensed? / {{c1::Heterochromatin}}
- (autoral) note 1791631345616: {{c1::Constitutive}} heterochromatin stays condensed in every cell, as at centromeres and repeats
- (autoral) note 1791631345741: Facultative heterochromatin depends on cell type or cycle phase, as in the inactive {{c1::X}} chromosome
- (autoral) note 1791631346116: Methylated histone H3 recruits {{c1::HP1}}, which self-associates and packs chromatin into heterochromatin
- (autoral) note 1791631346967: Epigenetic states are gene-expression patterns that persist through {{c1::cell division}} without changing the DNA sequence
- (acervo) note 1791631347641: Panobinostat and vorinostat are antineoplastics that are nonselective {{c1::histone deacetylase (HDAC)}} inhibitors
- (autoral) note 1791631347892: Therapeutic use of iPS cells is limited because two of the factors, c-Myc and Klf4, are {{c1::oncogenes}}
- (autoral) note 1792082171335: Because chromatin already limits access to DNA, purely negative regulation is {{c1::less common}} in eukaryotic transcription
- (autoral) note 1792082177137: Proteins with a {{c1::bromodomain}} read acetylated histone lysines and help open chromatin

### 2026-uc03-bioquimica-10-acao-hormonal — 9 suspensos
- (acervo) note 1791054008921: What peptide is packaged with insulin and may be used to monitor β cell function in patients receiving exogenous insulin? / {{c1::C-peptide (connecting peptide)}}
- (acervo) note 1791054010097: In a nonmedical setting, severe hypoglycemia is ideally treated with intramuscular {{c1::glucagon}}
- (acervo) note 1791054011246: Glucagon increases blood glucose concentration by increasing {{c1::glycogenolysis}} and gluconeogenesis, while simultaneously inhibiting {{c1::glycogen}} formation from glucose
- (acervo) note 1791054011372: Insulin increases glucose transport to {{c1::muscle}} and {{c1::adipose}} tissue by directing the insertion of the {{c2::GLUT-4}} transporter into the cell membranes
- (acervo) note 1791054013222: Glucagon, cortisol, and epinephrine induce {{c1::insulin resistance}} due to phosphorylation of {{c2::serine}} / {{c2::threonine}} residues of the insulin receptor and IRS-1
- (acervo) note 1791054014146: {{c1::Sulfonylureas}} and {{c1::meglitinides}} bind the ATP-dependent {{c2::K+}} channels on pancreatic β cells, causing release of endogenous insulin
- (acervo) note 1791054014447: GLP-1 stimulates {{c1::insulin}} secretion and inhibits {{c1::glucagon}} secretion.
- (acervo) note 1791647354044: The major factor that stimulates glucagon secretion is {{c1::hypoglycemia}}
- (acervo) note 1791762411098: {{c1::Receptor tyrosine kinases}} have intrinsic tyrosine kinase activity within the receptor molecule

### 2026-uc03-bioquimica-16-regulacao-hormonal-massa-corporea — 6 suspensos
- (acervo) note 1791054012719: Chronic hyperinsulinemia can {{c1::downregulate}} insulin receptors.
- (acervo) note 1791054012972: Insulin resistance is particularly associated with excess {{c1::visceral}} adipose tissue.
- (acervo) note 1791054013396: Adipocytes, β cells, and FFAs cause release of {{c1::adipokines}}, which contribute to insulin resistance in obesity
- (acervo) note 1791054014570: GLP-1 analogs cause increased {{c1::insulin}} release and satiety /
- (acervo) note 1791647352594: {{c1::Thermogenin (UCP-1)}} in brown fat may act as a(n) {{c2::uncoupling}} agent of oxidative phosphorylation
- (acervo) note 1792241687923: GLP-1 analogs cause decreased {{c1::glucagon}} release and gastric emptying /

### 2026-uc03-bioquimica-25-integracao-metabolica-i — 5 suspensos
- (acervo) note 1791647346246: Which insulin-independent transporter is found in the brain, placenta, cornea, and RBCs? / / {{c1::GLUT-1}}
- (acervo) note 1791647348120: Fructose-1,6-bisphosphatase is regulated via negative feedback by {{c1::fructose-2,6-bisphosphate}} and {{c1::AMP}}
- (acervo) note 1791647348245: Muscle cannot release glucose into the blood because it lacks {{c1::glucose-6-phosphatase}}
- (acervo) note 1791647351570: Pyruvate is converted to {{c2::lactate}} via the enzyme {{c1::lactate dehydrogenase (LDH)}} (Cori cycle)
- (acervo) note 1791647352896: After three days of starvation, the main source of energy for the brain becomes {{c1::ketone bodies}} from {{c2::adipose}} stores

### 2026-uc03-bioquimica-33-integracao-metabolica-ii — 8 suspensos
- (autoral) note 1791054010222: Diabetes mellitus is chronic hyperglycemia caused by defective insulin secretion, defective insulin {{c1::action}}, or both
- (acervo) note 1791054010873: One of the most feared complications of type 2 diabetes is {{c1::hyperosmolar hyperglycemic state}}
- (acervo) note 1791054010997: Type 1 DM is caused by autoimmune destruction of β cells by {{c1::CD8+ T}} cells
- (acervo) note 1791054011671: In T1DM, increased {{c2::lipolysis}} leads to an increase in free fatty acids, which the liver consumes to secrete {{c1::ketone bodies}}
- (acervo) note 1791054012847: A major pathogenic factor underlying metabolic syndrome is {{c1::insulin}} resistance
- (acervo) note 1791054013770: {{c1::Metformin}}, a biguanide, is the first-line oral agent for the management of type 2 diabetes
- (acervo) note 1791054013895: Metformin modulates enzyme function to decrease hepatic {{c1::gluconeogenesis}} /
- (acervo) note 1791054014020: Thiazolidinediones (glitazones) cause increased insulin {{c1::sensitivity}}, therefore enhancing glucose uptake in peripheral tissues

### 2026-uc03-grand-round-03-espondilodiscite-tuberculosa — 4 suspensos
- (acervo) note 1791054020796: What mode of imaging is the best for detecting acute osteomyelitis? / {{c1::MRI}}
- (autoral) note 1791054020921: In osteomyelitis, the infected marrow is {{c1::hyperintense}} on fat-suppressed T2 MRI
- (autoral) note 1791716431615: The absence of caseous necrosis on one biopsy does {{c1::not}} exclude tuberculosis
- (autoral) note 1791716448950: A granuloma is a {{c1::dynamic}} cell network, not an impermeable wall

### 2026-uc03-grand-round-04-paracoccidioidomicose — 4 suspensos
- (acervo) note 1791557942007: {{c1::Echinocandins}} are a class of antifungals that inhibit the enzyme {{c2::1,3-β-glucan synthase}}
- (acervo) note 1791557942183: {{c1::Polyenes (e.g. nystatin, amphotericin B)}} are a class of antifungals that bind {{c2::ergosterol}}, creating {{c2::pores}} in the fungal cell membranes
- (acervo) note 1791557944405: Paracoccidioides brasiliensis is a {{c1::thermally dimorphic}} fungus that grows as a mold at 25 °C and as a yeast at 37 °C
- (acervo) note 1792170505829: Which antifungal inhibits fungal DNA and RNA / protein synthesis? / / {{c1::Flucytosine}}

### 2026-uc03-grand-round-21-diabetes — 65 suspensos
- (acervo) note 1791054007644: Polyuria, polydipsia and unexplained weight loss suggest {{c1::DM1}}.
- (acervo) note 1791054007769: With classic hyperglycemic symptoms, random plasma glucose ≥ {{c1::200}} mg/dL establishes diabetes.
- (acervo) note 1791054007900: What is the typical serum potassium level in a patient with T1DM in diabetic ketoacidosis? / / {{c1::Increased::Increased or Decreased}}
- (acervo) note 1791054008019: What is the intracellular potassium level in a patient with T1DM in diabetic ketoacidosis? / {{c1::Decreased::Increased or Decreased}}
- (acervo) note 1791054008148: How does insulin cause K+ to shift into cells? / {{c1::Increased Na+-K+ ATPase}}
- (acervo) note 1791054008544: What is the diagnostic cutoff for the 2-hour oral glucose tolerance test (OGTT) for a diagnosis of diabetes mellitus? / {{c1::≥ 200 mg/dL}}
- (acervo) note 1791054008670: What is the diagnostic cutoff for HbA1c for a diagnosis of diabetes mellitus? / {{c1::≥ 6.5%}}
- (autoral) note 1791054008796: Fructosamine measures glycated serum {{c1::albumin}} and reflects glucose control over the last 2–3 weeks
- (acervo) note 1791054009046: An autoimmune marker of type 1 diabetes is the presence of {{c3::anti-GAD}} antibodies.
- (autoral) note 1791054009345: Continuous glucose monitors measure glucose in {{c1::interstitial}} fluid rather than in blood
- (acervo) note 1791054009472: Insulin detemir, degludec, and glargine are characterized by {{c1::long::rapid/short/intermediate/long}} action and duration
- (acervo) note 1791054009721: The diagnosis for diabetes mellitus may be made using {{c1::HbA1c}} which reflects average blood glucose over 3 prior months
- (autoral) note 1791054009969: The {{c1::honeymoon}} period of type 1 diabetes needs little insulin because some β cells still survive
- (acervo) note 1791054010347: Compared with type 2 diabetes, type 1 diabetes has a {{c1::weaker}} genetic predisposition.
- (acervo) note 1791054010623: What HLA subtypes are associated with type I diabetes mellitus? / {{c1::DR3}} and {{c1::DR4}}
- (acervo) note 1791054011848: Diabetic ketoacidosis is associated with a(n) {{c1::fruity}} breath odor due to exhaled {{c2::acetone}}
- (acervo) note 1791054012018: In uncontrolled diabetes mellitus, {{c1::Kussmaul}} breathing compensates for the metabolic {{c2::acidosis}} caused by ketone accumulation.
- (acervo) note 1791054012198: Diabetic ketoacidosis causes metabolic acidosis with an {{c1::increased}} anion gap.
- (acervo) note 1791054012447: In hyperosmolar hyperglycemic state, residual {{c1::insulin}} usually suppresses substantial ketone production.
- (acervo) note 1791054013097: Excess glucose and free fatty acids (FFAs) may contribute to {{c1::β}} cell dysfunction
- (acervo) note 1791054013522: The incretin {{c1::GLP}} may inadequately stimulate β cells and contribute to β cell dysfunction in type 2 diabetes mellitus
- (acervo) note 1791054013647: {{c2::Exercise}} may increase the expression of the GLUT-4 receptor in muscle tissue only
- (acervo) note 1791054014697: Do GLP-1 agonists and/or DPP-4 inhibitors cause hypoglycemia as a possible side effect? / / {{c1::No}}
- (autoral) note 1791054014822: Nonenzymatic binding of glucose to protein amino groups first forms a reversible {{c1::Schiff base}}
- (autoral) note 1791054014945: HbA1c is a stable {{c1::Amadori}} product formed when the Schiff base of glucose and hemoglobin rearranges
- (autoral) note 1791054015070: Over months, Amadori products {{c1::cross-link}} proteins into irreversible advanced glycation end products
- (acervo) note 1791054015322: One chronic complication of diabetes mellitus is {{c1::non-enzymatic glycation}} of vascular basement membranes
- (acervo) note 1791054015447: Non-enzymatic glycation of medium and large-sized vessels leads to {{c1::atherosclerosis}} in patients with diabetes
- (acervo) note 1791054015573: Diabetes is a risk factor for {{c1::atherosclerosis}} due to chronic inflammation, lipid oxidation, and advanced glycation end products
- (acervo) note 1791054015697: Hyperglycemia damages the glomerular basement membrane through nonenzymatic {{c1::glycation}}.
- (autoral) note 1791054015822: AGEs activate monocytes and endothelium through the receptor {{c1::RAGE}}
- (acervo) note 1791054015947: Which renal arteriole is initially affected by non-enzymatic glycation? / {{c1::Efferent arteriole}}
- (acervo) note 1791054016196: In diabetes, {{c1::osmotic}} damage may occur when glucose in tissue is converted to {{c2::sorbitol}} by the enzyme {{c3::aldose reductase}}
- (acervo) note 1791054016421: In diabetes, osmotic damage to {{c2::Schwann}} cells causes {{c1::peripheral}} neuropathy and {{c1::autonomic}} neuropathy
- (acervo) note 1791054016595: Histology of type 1 diabetes mellitus demonstrates islets with {{c1::leukocytic infiltrate}}
- (acervo) note 1791054016721: Type 2 diabetes mellitus is associated with deposition of {{c1::amylin}} in the islets of the pancreas
- (acervo) note 1791054016847: In patients with diabetes, blindness occurs as a result of osmotic damage to {{c1::pericytes::cell type}} of retinal blood vessels, weakening the vessel wall and causing aneurysm formation
- (acervo) note 1791054016970: What is the likely diagnosis in a patient with diabetes that presents with decreased vision in both eyes? Ophthalmoscopy reveals microaneurysms, dot and blot hemorrhages, hard exudates, and macular edema / / {{c1::Nonpro
- (acervo) note 1791054017097: {{c1::Proliferative}} diabetic retinopathy results in new blood vessel formation with resultant traction on the retina
- (acervo) note 1791054017222: Proliferative diabetic retinopathy is prone to {{c1::hemorrhage}} due to disorganized neovascularization
- (acervo) note 1791054017347: In diabetes, {{c1::cataracts}} occur as a result of osmotic damage to the lens
- (acervo) note 1791054017471: Secondary closed-angle glaucoma is caused by {{c1::hypoxia}} from retinal disease, which induces vasoproliferation in the iris that contracts the angle (e.g., diabetes mellitus, vein occlusion)
- (acervo) note 1791054017598: Microaneurysms are a sign of early {{c1::nonproliferative diabetic}} retinopathy
- (acervo) note 1791054017721: Initially, non-enzymatic glycation of the glomerular basement membrane (diabetes mellitus) causes hyperfiltration injury which leads to the development of {{c1::microalbumin}}uria by promoting production of heparanase
- (acervo) note 1791054017844: Diabetic glomerulonephropathy is associated with {{c1::mesangial}} expansion on light microscopy
- (acervo) note 1791054017972: Non-enzymatic glycation of small vessels may cause nodular {{c1::glomerulosclerosis}} with Kimmelstiel-Wilson nodules; may cause chronic kidney disease
- (acervo) note 1791054018093: The hyperfiltration in diabetic glomerulonephropathy can lead to eosinophilic nodular glomerulosclerosis, known as {{c1::Kimmelstiel-Wilson}} nodules
- (acervo) note 1791054018222: Non-enzymatic glycation of small vessels can cause hyaline {{c1::arteriolosclerosis}} of the kidney, which may lead to chronic kidney disease
- (acervo) note 1791054018344: What endocrine pathology is associated with UTI? / {{c1::Diabetes mellitus}}
- (acervo) note 1791054018470: Non-enzymatic glycation of medium and large-sized vessels may cause {{c1::peripheral vascular disease}}, which is the leading cause of nontraumatic amputation in patients with diabetes
- (acervo) note 1791054018596: What is the most important contributing factor for diabetic foot ulcers? / / {{c1::Diabetic neuropathy}}
- (acervo) note 1791054018721: Patients with diabetic neuropathy present with a slowly progressive decrease in vibratory sensation, {{c1::proprioception}}, and {{c2::temperature}} sensation
- (acervo) note 1791054018897: Chronic diabetes predisposes patients to recurrent {{c1::infection}} due to poor wound healing, urinary retention, neutrophil dysfunction, and hyperglycemia
- (acervo) note 1791054019022: Secondary infection of diabetic foot ulcers may lead to gangrene requiring {{c1::amputation::treatment}}
- (acervo) note 1791054019147: What is the leading cause of death in patients with diabetes mellitus? / {{c1::Heart attack (MI)}}
- (acervo) note 1791054019271: Tight blood glucose control in patients with diabetes is most likely to decrease risk of {{c1::micro}}vascular complications
- (autoral) note 1791054019396: Early diabetic nephropathy shows {{c1::enlarged}} kidneys on ultrasound
- (autoral) note 1791054019520: End-stage diabetic nephropathy shows small kidneys with a thin {{c1::hyperechoic}} cortex on ultrasound
- (acervo) note 1791054019772: Myocardial infarction is often due to rupture of an atherosclerotic plaque with thrombosis and {{c2::complete}} occlusion of a coronary artery
- (autoral) note 1791054019897: The coronary calcium score on non-contrast CT is calculated by the {{c1::Agatston}} method
- (acervo) note 1791054020395: Unperceived joint damage due to diabetic neuropathy may lead to formation of {{c1::charcot joint (neurogenic arthropathy)}}, which is managed with casting and orthotic footwear
- (acervo) note 1791054020545: What is the likely diagnosis in a patient with diabetes who has a severely deformed foot? X-ray shows bony destruction, decreased bone mass, osteophytes, and loss of joint spaces / / {{c1::Charcot joint}}
- (acervo) note 1791054020671: Osteomyelitis in patients with diabetes is typically preceded by a long-standing foot ulcer that spreads {{c1::contiguously}} to bone, causing a(n) {{c1::poly}}microbial infection
- (acervo) note 1791054021044: Osteomyelitis may be seen on X-ray as a(n) {{c1::lytic}} focus (sequestrum) surrounded by sclerosis (involucrum)
- (autoral) note 1791482469941: HbA1c reflects about 3 months of glycemia because glycated hemoglobin lasts as long as the {{c1::red blood cell}} that carries it

### 2026-uc03-imunologia-07-organizacao-sistema-imune — 3 suspensos
- (acervo) note 1791023357519: Lymphoid nodules and free immune cells in the gut mucosa and submucosa form the {{c1::MALT}}
- (autoral) note 1791629597796: Compared with the primary response, the secondary antibody response has a shorter lag and a {{c1::higher}} peak
- (autoral) note 1792166970267: Self-tolerance induced in the thymus or bone marrow is {{c1::central::central/peripheral}}, and in tissues is {{c1::peripheral::central/peripheral}}

### 2026-uc03-imunologia-17-reconhecimento-adaptativo — 2 suspensos
- (autoral) note 1791629588997: Unlike antibodies, the T-cell receptor is never {{c1::secreted}}
- (acervo) note 1792241813320: Does IgA cross the placenta? / {{c1::No}}

### 2026-uc03-imunologia-20-mhc-apresentacao — 1 suspensos
- (acervo) note 1792241984143: Which MHC class is formed by 1 long chain and 1 short chain? / {{c1::MHC I}}

### 2026-uc03-imunologia-22-mecanismos-efetores — 2 suspensos
- (acervo) note 1791625430456: {{c1::Nitric oxide synthase}} cleaves the amino acid {{c2::arginine}} into citrulline and nitric oxide
- (autoral) note 1791629596121: In ADCC, NK cells bind antibody-coated cells through the low-affinity receptor {{c1::FcγRIII}} (CD16)

### 2026-uc03-imunologia-31-sistema-complemento — 2 suspensos
- (autoral) note 1791629595622: Bound, but not free, IgM exposes its binding sites for {{c1::C1q}}
- (autoral) note 1791667100388: MBL deficiency resembles classical-pathway deficiency, with infections and {{c1::lupus}}-like disease

### 2026-uc03-imunologia-45-ativacao-linfocitos-t — 8 suspensos
- (autoral) note 1791625423557: Double-positive thymocytes whose TCR cannot bind self-MHC die by {{c1::neglect}}
- (acervo) note 1791625424057: Deficiency of {{c2::autoimmune regulator (AIRE)}} protein causes {{c1::autoimmune polyendocrine syndrome (APS) type 1}}
- (autoral) note 1791625424356: Unlike single-chain CD4, the CD8 coreceptor is a {{c1::dimer}} of α and β chains
- (autoral) note 1791625428283: In the immunological synapse, TCR–MHC contacts gather at the center, ringed by adhesion between {{c1::LFA-1}} and ICAM-1
- (autoral) note 1791625429158: IL-2 acts mainly on the same T cell that secretes it, an {{c1::autocrine}} action
- (autoral) note 1791625431633: A committed Th1 cell keeps the IL-4 gene silent by packing it into closed {{c1::chromatin}}
- (autoral) note 1791625433083: Induced Tregs develop from naive CD4+ T cells exposed to TGF-β plus {{c1::retinoic acid}}
- (autoral) note 1791625435406: Treg-derived {{c1::IL-10}} inhibits antigen-presenting cells and macrophages

### 2026-uc03-imunologia-49-ativacao-celulas-b — 5 suspensos
- (autoral) note 1791629590097: B-1 cells are marked by surface {{c1::CD5}}
- (autoral) note 1791629590347: Conventional B-2 cells are continuously replenished from the {{c1::bone marrow}}
- (acervo) note 1791629590597: What cellular organelle is abundant in mucus-secreting goblet cells (small intestine) and antibody-secreting plasma cells? / {{c1::Rough endoplasmic reticulum}}
- (autoral) note 1791629591272: {{c1::CD19}} is the signaling chain of the B-cell coreceptor, together with CD21 and CD81
- (autoral) note 1791629591522: {{c1::CD22}} is an inhibitory B-cell coreceptor that recruits the phosphatase SHP-1

### 2026-uc03-imunologia-51-disturbios-sistema-imune — 17 suspensos
- (acervo) note 1792166972544: What HLA subtype is associated with seronegative spondyloarthritis? / {{c1::HLA-B27}}
- (acervo) note 1792166972789: What HLA subtypes are associated with Addison disease? / {{c1::DR3}} and {{c1::DR4}}
- (acervo) note 1792166973044: What HLA subtypes are associated with celiac disease? / {{c1::DQ2}} and {{c1::DQ8}}
- (acervo) note 1792166973339: What HLA subtypes are associated with SLE? / {{c1::DR2}} and {{c1::DR3}}
- (acervo) note 1792166973591: What HLA subtype is associated with Goodpasture syndrome? / {{c1::HLA-DR2}}
- (acervo) note 1792166973842: What HLA subtype is associated with pernicious anemia? / {{c1::DR5}}
- (acervo) note 1792166974094: Myasthenia gravis is associated with HLA-{{c1::B8}}
- (autoral) note 1792166976092: Autoimmune diseases are {{c1::organ-specific::organ-specific/systemic}} when one organ is attacked (Graves, type 1 diabetes) and {{c1::systemic::organ-specific/systemic}} when many are (SLE)
- (acervo) note 1792166976344: TSH receptors on thyroid gland follicular cells may be activated by {{c1::TSH receptor antibodies (TRAbs)}} in Graves disease
- (acervo) note 1792166977241: Which antibodies are specific, but not sensitive for SLE? / {{c1::anti-dsDNA and anti-Smith antibodies::2}}
- (autoral) note 1792166977992: Immunodeficiencies are {{c1::primary::primary/secondary}} when inherited and {{c1::secondary::primary/secondary}} when acquired, as in HIV, malnutrition or chemotherapy
- (acervo) note 1792166982191: {{c1::Adenosine deaminase}} deficiency results in buildup of dATP, which is toxic to lymphocytes; causes SCID
- (acervo) note 1792166985287: {{c2::X-linked (Bruton) agammaglobulinemia}} is caused by a defect in the {{c1::Bruton tyrosine kinase (BTK)}} gene
- (acervo) note 1792166986642: Which immunodeficiencies are characterized by absent / scanty lymph nodes and tonsils? / / {{c1::X-linked (Bruton) agammaglobulinemia}} and {{c1::severe combined immunodeficiency (SCID)}}
- (acervo) note 1792166994690: Patients with Chédiak-Higashi syndrome have increased risk for {{c1::pyogenic}} infections (e.g., Staphylococci and Streptococci)
- (acervo) note 1792166997066: Serum amyloid A (SAA) is an acute phase reactant that is increased in chronic inflammatory states, malignancy, and {{c1::familial Mediterranean fever (FMF)::inherited condition}}
- (acervo) note 1792166997364: Familial Mediterranean fever is characterized by {{c1::AA amyloid (secondary)}} deposits in tissues during attacks

### 2026-uc03-microbiologia-26-morfologia-estrutura-bacteriana — 23 suspensos
- (autoral) note 1791163022242: Woese defined the three domains of life (Bacteria, Archaea, Eukarya) by comparing {{c1::ribosomal RNA}} sequences
- (acervo) note 1791163027172: Peptidoglycan cell walls have repeating {{c1::D-alanyl-D-alanine}} oligopeptides
- (acervo) note 1791163028321: What molecule present on the surface of gram positive bacteria drives immune response to the organism? / / {{c1::Lipoteichoic acid}}
- (acervo) note 1791163030347: {{c1::Lipopolysaccharide}} is contained on the {{c2::outer membrane}} of gram {{c3::negative}} bacteria
- (acervo) note 1791163033119: Which part of lipopolysaccharide is a target for antibodies? / / {{c1::O antigen}}
- (acervo) note 1791163035024: Small DNA within the cells of bacteria that replicate independently are known as {{c1::plasmids}}
- (acervo) note 1791163036170: Which structural component of bacterial flagella is responsible for generating torque and molecular motion? / / {{c1::The basal body}}
- (acervo) note 1791163040622: A bacterial capsule increases virulence by inhibiting {{c1::phagocytosis}}
- (autoral) note 1791576665465: Most bacteria that live with us are {{c1::commensal}} or mutualistic, and only a small minority cause disease
- (autoral) note 1791576665990: {{c1::Differential}} solid media show colonies of different colors (e.g., lactose fermenters) or hemolysis patterns
- (acervo) note 1791576666993: Bunches/clusters of cocci bacteria is characteristic of {{c1::Staphylococci}}
- (autoral) note 1791576667142: Bacilli that stay in chains after division are called {{c1::streptobacilli}}
- (acervo) note 1791576667293: Vibrio cholerae is a bacterium that has a(n) {{c1::comma}} shape
- (acervo) note 1791576670517: Does inhibition of transpeptidases directly kill bacteria? / / {{c1::No}}
- (autoral) note 1791576671341: Teichoic acids regulate {{c1::autolysins}}, letting the wall be remodeled during division without lysis
- (acervo) note 1791576673767: Most rods (and coccobacillus) are gram {{c1::negative}}
- (acervo) note 1791576675192: {{c1::Mycoplasma::Which bacteria}} does not {{c3::Gram}} stain because it lacks a cell wall; its cell membrane instead has {{c2::sterols}} for stability
- (acervo) note 1791576675592: Prokaryotic cells have {{c1::circular}} DNA while eukaryotic cells have {{c2::linear}} DNA
- (acervo) note 1791576676015: The two ribosomal subunits in bacteria/prokaryotes are {{c1::50}}S and {{c1::30}}S making {{c1::70}}S
- (acervo) note 1791576678691: {{c1::Peptidoglycans}} make up the middle layer, or {{c2::cortex}}, of a bacterial spore
- (acervo) note 1791576680065: Does E. coli have a capsule? / / {{c1::Yes}}
- (acervo) note 1791576680215: Staphylococcus epidermidis forms a protective {{c1::biofilm}} that allows it to colonize prosthetic devices
- (autoral) note 1791576680665: Bacteria inside a {{c1::biofilm}} resist biocides and antibiotics much better than free cells

### 2026-uc03-microbiologia-27-fisiologia-bacteriana — 6 suspensos
- (autoral) note 1791647812370: Bacteria multiply by {{c1::binary fission}}, so growth means an increase in cell number
- (acervo) note 1791647812993: {{c2::Superoxide dismutase}} and {{c2::catalase}} are two enzymes contained in all {{c1::obligate aerobic}} organisms
- (acervo) note 1791647813545: {{c2::Clostridioides}} difficile; botulinum; perfringens; tetani are all {{c1::obligate anaerobes::obligate aerobes or anaerobes}}
- (acervo) note 1791647814920: {{c1::Obligate anaerobes::Obligate aerobes or Anaerobes}} use fermentation to generate ATP
- (autoral) note 1791647815469: Bacterial growth in broth can be followed by the rise in {{c1::turbidity}} measured in a spectrophotometer
- (acervo) note 1791647815720: The 3 phases of the bacterial growth curve are: / / {{c1::Lag}} phase / {{c1::Growth/log}} phase / {{c1::Stationary}} phase

### 2026-uc03-microbiologia-28-pratica-1 — 2 suspensos
- (autoral) note 1791648193118: Cocci that stay together in cubic packets after dividing are called {{c1::sarcinae}}
- (autoral) note 1791648193993: A {{c1::minimal}} medium contains only mineral salts and a carbon source such as glucose

### 2026-uc03-microbiologia-30-controle-microbiologico — 2 suspensos
- (autoral) note 1791666340440: The microbial forms most resistant to disinfection and sterilization are bacterial {{c1::spores}}
- (acervo) note 1791666343290: Autoclaves work to sterilize equipment by using {{c1::pressurized steam}}

### 2026-uc03-microbiologia-32-antibioticos-resistencia — 1 suspensos
- (acervo) note 1791668525764: {{c1::Vancomycin}} resistance occurs in Enterococcus spp. ({{c1::VRE}}) via amino acid modification of D-Ala-D-Ala to D-Ala-D-Lac

### 2026-uc03-microbiologia-39-homem-ambiente-microrganismo — 1 suspensos
- (autoral) note 1791014718900: Bacterial fermentation of fiber yields {{c1::butyrate}}, the short-chain fatty acid that nourishes colonocytes

### 2026-uc03-microbiologia-43-biologia-fungos — 5 suspensos
- (acervo) note 1791557940256: Patients get exposed to aflatoxins produced by Aspergillus by way of eating improperly stored {{c1::grains}} and {{c1::nuts}}
- (acervo) note 1791557941081: {{c1::Eukaryotes::Prokaryotes or Eukaryotes}} include protozoa and fungi
- (acervo) note 1791557941506: The two ribosomal subunits in eukaryotes are {{c1::60}}S and {{c1::40}}S making {{c1::80}}S
- (autoral) note 1791557941879: In dimorphic fungi, the yeast phase at 37 °C has more {{c1::α-glucan}} in its wall than the mold phase
- (acervo) note 1792170507325: Candida albicans is {{c1::dimorphic*}}, meaning it assumes different forms depending on the temperature of its environment

### 2026-uc03-microbiologia-44-micoses-cutaneas — 7 suspensos
- (autoral) note 1791626776427: Besides keratinases, dermatophytes secrete {{c1::elastases}}, collagenase and DNase
- (acervo) note 1791626776929: What demographic of adults are at risk for tinea (ringworm) infections? / / {{c1::Athletes}}
- (autoral) note 1791626778303: Trichophyton indotineae, an emerging dermatophyte, resists terbinafine through mutations in {{c1::squalene epoxidase}}
- (autoral) note 1791626778603: A sterile eruption on the hands caused by an immune reaction to a distant dermatophyte focus is a {{c1::dermatophytid}}
- (acervo) note 1791626781776: {{c2::Hyphae}} of tinea lesions due to {{c3::dermatophytes}} are seen with {{c1::KOH}} prep of {{c1::skin}} scrapings
- (acervo) note 1792175046437: What microorganism is most commonly involved in the pathogenesis of tinea capitis? / / {{c1::Trichophyton tonsurans}}
- (acervo) note 1792175046687: What is the likely diagnosis in an African American child that presents with pruritic, erythematous plaque on the scalp that resulted in patchy hair loss with residual "black dots"? Lymphadenopathy is present / / {{c1::T

### 2026-uc03-microbiologia-48-micoses-subcutaneas — 5 suspensos
- (acervo) note 1791628674273: The yeast of {{c1::Sporothrix schenckii::which fungus}} takes on a(n) {{c2::cigar}} shape under microscope
- (acervo) note 1791628674948: What is the drug of choice for treatment of sporotrichosis / Sporothrix schenckii infection? / / {{c1::Itraconazole}}
- (autoral) note 1791628675824: A mycetoma is defined by: / 1. Tumor-like {{c1::swelling}} / 2. Draining {{c2::sinuses}} / 3. {{c1::Grains}}
- (acervo) note 1791628676247: What is the oxygen dependency of Nocardia spp.? / / {{c1::Obligate aerobe}}
- (autoral) note 1791628676373: Jorge Lobo disease (lobomycosis) is caused by the fungus {{c1::Lacazia loboi}}

### 2026-uc03-microbiologia-50-micoses-sistemicas — 5 suspensos
- (autoral) note 1791630903393: The {{c1::armadillo}} is a suspected natural reservoir of Paracoccidioides
- (autoral) note 1791630904844: The yeast wall of Paracoccidioides is rich in {{c1::α-glucan::α-glucan or β-glucan}}, whereas the mold wall has mostly {{c1::β-glucan::α-glucan or β-glucan}}
- (autoral) note 1791630907794: An {{c1::auxanogram}} identifies yeasts by the carbon and nitrogen sources they assimilate
- (autoral) note 1791630908043: Cryptococcus gattii (serotypes B and C) is linked to {{c1::eucalyptus}} trees
- (autoral) note 1791744812082: The mold phase of Paracoccidioides is rich in immunogenic {{c1::galactomannan}}, which the yeast phase largely lacks

### 2026-uc03-microbiologia-58-multiplicacao-viral-antivirais — 1 suspensos
- (autoral) note 1792695030288: Adenovirus DNA synthesis starts at both ends from a terminal protein primer linked to {{c1::dCMP}}, by {{c2::strand displacement}}

### 2026-uc03-microbiologia-59-patogenese-viral — 7 suspensos
- (autoral) note 1792753605841: Enteric viruses: / - localized, causing diarrhea: {{c1::rotavirus}}, norovirus / - systemic, reaching far organs: {{c2::poliovirus}} (CNS), hepatitis A (liver)
- (autoral) note 1792753609593: Herpes reactivations reach lower viral loads than the primary infection because {{c1::immune memory}} already exists
- (autoral) note 1792753609843: Herpesviruses replicate lytically in one cell type and stay latent in a long-lived one, like {{c1::memory B cells}} for EBV
- (autoral) note 1792753615465: To establish a chronic infection, a virus needs mechanisms of immune {{c1::evasion}}
- (autoral) note 1792753617191: Viral infections cause about {{c1::15–20}}% of human cancers
- (autoral) note 1792753617695: A red blood cell may bind a virus but is not {{c1::permissive}}, lacking machinery to copy a genome
- (acervo) note 1792753636542: What is the mechanism for antigenic variation of envelope proteins in hepatitis C virus? / / {{c1::Lack of 3'-5' exonuclease}} → {{c1::lack of proofreading}} → antigenic variation

### 2026-uc03-patologia-11-acumulos-adaptacao — 2 suspensos
- (acervo) note 1791022171771: Which form of alcoholic liver disease may be reversible with abstinence? / {{c1::Hepatic steatosis}}
- (acervo) note 1792240576568: Kwashiorkor may present as liver malfunction with fatty change due to decreased {{c1::apolipoprotein}} synthesis

### 2026-uc03-patologia-13-envelhecimento — 1 suspensos
- (acervo) note 1792240993866: Cancers may increase expression of {{c1::telomerase}} to prevent chromosome shortening and cell death

### 2026-uc03-patologia-14-declaracao-obito — 1 suspensos
- (acervo) note 1791022175426: Esophageal {{c2::varices}} are a common cause of death in patients with {{c1::cirrhosis}}

### 2026-uc03-patologia-23-edema-congestao — 8 suspensos
- (autoral) note 1791141188737: Edema is an abnormal accumulation of fluid in the {{c1::interstitial}} space
- (acervo) note 1791141192064: When net fluid movement is out of the capillary into the interstitial fluid, it is called {{c1::filtration}}
- (acervo) note 1791141198656: Edema may be caused by {{c1::sodium}} and {{c1::water}} retention
- (acervo) note 1791169084658: Edema may be caused by {{c1::lymphatic}} disruption/obstruction
- (acervo) note 1791169088281: Right heart failure is associated with a characteristic "{{c1::nutmeg}}" appearance of the liver
- (acervo) note 1791169088580: Cirrhosis may lead to activation of {{c1::RAAS}} due to decreased intravascular volume which is complicated by impaired metabolism of aldosterone
- (acervo) note 1791169089207: Damage to the alveolar-capillary interface leads to {{c1::increased}} alveolar-capillary permeability
- (autoral) note 1791592962843: Edema worse in the {{c1::morning}}, around the eyes, suggests low oncotic pressure, while evening edema of the legs suggests a gravitational cause

### 2026-uc03-patologia-24-patologia-ambiental — 2 suspensos
- (autoral) note 1791592723419: Inhaled fine particles raise systemic {{c1::IL-6}} and TNF-α, promoting atherosclerosis and plaque rupture
- (autoral) note 1791592724893: Chronic exposure to biomass smoke causes chronic airway inflammation that lowers lung function and leads to {{c1::COPD}}

### 2026-uc03-patologia-47-inflamacao-granulomatosa — 9 suspensos
- (autoral) note 1791716405167: When macrophages cannot eliminate a persistent stimulus, they may organize into a {{c1::granuloma}}
- (autoral) note 1791716411025: Activated macrophages increase in {{c1::size}} and gain more {{c2::lysosomal enzymes}}
- (autoral) note 1791716432060: Granulomas heal by {{c1::fibrosis}}, which replaces functional parenchyma and can impair the organ
- (autoral) note 1791716447474: Material too large to engulf can cause {{c1::frustrated phagocytosis}}
- (autoral) note 1791910083901: Granulomatous inflammation is an organized pattern of {{c1::chronic inflammation}}
- (autoral) note 1791910084370: By concentrating macrophages around a persistent stimulus, granulomas help limit its {{c1::spread}}
- (autoral) note 1791910084649: In immune granulomas, persistent antigen sustains macrophage activation through antigen-specific {{c1::T cells}}
- (autoral) note 1791910085849: IFN-γ enhances macrophage {{c1::microbicidal activity}} against persistent intracellular pathogens
- (autoral) note 1792081482263: Granulomas in the same lung may differ in their degree of necrosis and {{c1::fibrosis}}

### 2026-uc03-patologia-62-inflamacao-cronica — 3 suspensos
- (autoral) note 1791983680855: Blood monocytes live about {{c1::1 day}}, whereas tissue macrophages survive for {{c1::months}}
- (autoral) note 1791983682157: M1 macrophages kill ingested microbes using reactive oxygen species and {{c1::nitric oxide}}
- (autoral) note 1791983685881: Unlike tertiary follicles induced by inflammation, {{c1::MALT}} is constitutive lymphoid tissue beneath mucosal surfaces

### 2026-uc03-patologia-radiologia-19-correlacao-2 — 9 suspensos
- (acervo) note 1791022169576: Hepatic hemangiomas, hepatic adenomas, and focal nodular hyperplasias are most common in {{c1::reproductive-age women}}
- (autoral) note 1791022169697: An incidental, well-defined hyperechoic liver nodule in a young asymptomatic woman is most likely a {{c1::hemangioma}}
- (acervo) note 1791022170427: {{c1::Blood::Blood or Bile}} flows from the portal triad towards the central vein
- (acervo) note 1791022172150: Alcoholic {{c2::hepatitis}} is characterized by {{c1::swelling}} of hepatocytes with necrosis and neutrophilic infiltration
- (acervo) note 1791022173097: Within the space of Disse are {{c2::stellate (Ito)}} cells, which produce {{c1::extracellular matrix}} when activated
- (acervo) note 1791022173674: All patients with cirrhosis should have a screening ultrasound every {{c1::6 months::duration}} ± alpha-fetoprotein
- (acervo) note 1791022174254: Cirrhosis is often complicated by {{c1::portal}} hypertension
- (autoral) note 1791022174376: On CT, portal hypertension shows a nodular liver, ascites, collateral veins and an enlarged {{c1::spleen}}
- (acervo) note 1791022174502: Portal hypertension can lead to {{c1::ascites}}, which is fluid in the peritoneal cavity

### 2026-uc03-radiologia-04-radiografia-ultrassom — 1 suspensos
- (acervo) note 1792238912652: What is the appearance of calcium kidney stones on X-ray and CT? / {{c1::Radiopaque}}

### 2026-uc07 — 4 suspensos
- (acervo) note 1792588686975: O sulco {{c1::basilar}} da ponte aloja a artéria basilar
- (acervo) note 1792588687021: As estruturas de substância cinzenta do cerebelo são o córtex cerebelar e os núcleos {{c1::cerebelares}}
- (acervo) note 1792588687023: Do medial para o lateral, os núcleos do cerebelo são o {{c2::fastigial}}, o {{c1::globoso}}, o {{c2::emboliforme}} e o {{c1::denteado}}
- (autoral) note 1792697127074: O canal vertebral começa na articulação {{c1::atlantoccipital}}, entre o osso occipital e o {{c2::atlas}} (C1)

### 2026-uc07-cerebelo-cortex-cerebelar — 2 suspensos
- (acervo) note 1792344675723: A camada média do córtex cerebelar é a camada {{c1::de Purkinje}}
- (acervo) note 1792344676226: A camada externa do córtex cerebelar é a camada {{c1::molecular}}

### 2026-uc08-anatomia-01-esofago-estomago-delgado — 33 suspensos
- (autoral) note 1790972063767: The esophagus is a muscular tube about {{c1::25}} cm long that runs from the pharynx to the stomach
- (acervo) note 1790972064487: On a CT of the thorax, the {{c1::trachea}} is a good landmark to localize the esophagus (located posteriorly) and the great vessels (located anteriorly)
- (acervo) note 1790972064584: 
- (autoral) note 1790972066262: What is the name of the notch between the left border of the esophagus and the fundus of the stomach? / / {{c1::Cardiac notch}}
- (acervo) note 1790972066759: Identify the highlighted gastric region. / {{c1::Pylorus}}
- (acervo) note 1790972067059: 
- (acervo) note 1790972067359: 
- (acervo) note 1790972068261: 
- (acervo) note 1790972068360: 
- (acervo) note 1790972068706: On an abdominal CT scan, the pancreas can be identified by: / / - Its head in close association with the {{c1::2nd}} part of the duodenum- Its body overlying the {{c1::abdominal aorta::vasculature}}
- (acervo) note 1790972069210: The main pancreatic duct drains into the {{c1::major}} duodenal papilla
- (autoral) note 1790972070012: The {{c1::mesentery}} is the fold of peritoneum that attaches the jejunum and ileum to the posterior abdominal wall
- (acervo) note 1790972070110: 
- (acervo) note 1790972070210: 
- (acervo) note 1790972070410: 
- (acervo) note 1790973209810: 
- (acervo) note 1790973209933: 
- (acervo) note 1790973210057: 
- (acervo) note 1790973210184: 
- (acervo) note 1790973210308: 
- (acervo) note 1790973211156: 
- (acervo) note 1790973211408: 
- (acervo) note 1790973212607: 
- (acervo) note 1790973213781: 
- (acervo) note 1790973215632: 
- (acervo) note 1790973215757: 
- (acervo) note 1790973218132: 
- (acervo) note 1790973218257: 
- (acervo) note 1790973218382: 
- (acervo) note 1790973218507: 
- (acervo) note 1790973218633: 
- (acervo) note 1790973220082: 
- (acervo) note 1790973408235: 

### 2026-uc08-anatomia-02-intestino-grosso-canal-anal — 19 suspensos
- (acervo) note 1790974688878: 
- (acervo) note 1790974689130: 
- (acervo) note 1790974689253: 
- (acervo) note 1790974689380: 
- (acervo) note 1790974689504: 
- (acervo) note 1790974690604: 
- (acervo) note 1790974691531: Colonic diverticula containing mucosa and submucosa but not the full muscular wall are {{c1::false}} diverticula.
- (autoral) note 1790974691958: Behind the apex of the sigmoid mesocolon, on the left common iliac vessels, lies the {{c1::left ureter}}
- (acervo) note 1790974694628: 
- (acervo) note 1790974695630: 
- (acervo) note 1790974696004: 
- (acervo) note 1790974696629: 
- (acervo) note 1790974697004: 
- (acervo) note 1790974698404: Which lymph nodes drain the rectum below the pectinate line? / {{c1::Superficial inguinal nodes}}
- (acervo) note 1790974698531: {{c1::External}} hemorrhoids receive somatic innervation from the {{c2::pudendal}} nerve
- (autoral) note 1790978722492: The rectum has {{c1::three}} transverse folds (superior, middle and inferior) that help support the fecal mass
- (autoral) note 1790978739486: The upper ends of the anal columns mark the {{c1::anorectal}} junction, where the rectum becomes the anal canal
- (autoral) note 1790978740593: The lower ends of the anal columns are joined by the anal {{c1::valves}}, whose free edges form the pectinate line
- (autoral) note 1790980442408: The omental (epiploic) appendices of the colon are small pouches of peritoneum filled with {{c1::fat}}

### 2026-uc08-anatomia-07-vascularizacao-visceras — 11 suspensos
- (acervo) note 1790981514202: 
- (acervo) note 1790981514577: 
- (acervo) note 1790981515925: 
- (acervo) note 1790981518203: 
- (acervo) note 1790981519551: 
- (acervo) note 1790981520301: 
- (acervo) note 1790981521053: 
- (autoral) note 1790981522826: The pre-aortic lymph nodes lie in three groups around the celiac, superior mesenteric and {{c1::inferior mesenteric}} arteries
- (acervo) note 1790981522953: Which lymph node cluster drains the jejunum and ileum? / {{c1::Superior mesenteric}}
- (autoral) note 1790981526502: The middle rectal artery is a branch of the {{c1::internal iliac}} artery
- (autoral) note 1790981527427: Lymph from the upper rectum follows the superior rectal vessels to the {{c1::inferior mesenteric}} lymph nodes

### 2026-uc08-anatomia-11-figado-pancreas-vias-biliares — 1 suspensos
- (autoral) note 1792713397381: The lesser omentum runs from the lesser curvature of the stomach and the proximal {{c1::duodenum}} to the liver

### 2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas — 8 suspensos
- (autoral) note 1792659587805: The 90° turn of the stomach brings the left vagus to its {{c1::anterior}} wall and the right to the {{c1::posterior}}
- (autoral) note 1792659591802: Primary loop of the midgut: / - cephalic limb forms {{c2::jejunum}} and {{c2::ileum}} / - caudal limb forms {{c1::cecum}} and {{c2::ascending colon}}
- (autoral) note 1792659596102: In the embryo, the foregut endoderm buds out the {{c1::liver}} and the {{c1::pancreas}}
- (autoral) note 1792659596852: The liver grew inside the ventral mesentery, so the lesser omentum and the falciform ligament are the {{c1::remnants}} around it
- (autoral) note 1792659601722: Pancreatic acinar cells store enzymes in apical {{c1::zymogen}} granules
- (autoral) note 1792659603225: The liver gets nutrient-rich blood from the {{c1::portal vein}} and oxygen-rich blood from the {{c1::hepatic artery}}
- (autoral) note 1792659603475: In pig liver the lobules are clearly separated by connective tissue, whereas the human liver shows {{c1::no visible lobulation}}
- (autoral) note 1792659606725: Bile canaliculi are grooves between neighboring {{c1::hepatocytes}} and get their own wall only in the portal space

### 2026-uc08-biologia-tecidual-03-estrutura-estomago — 35 suspensos
- (acervo) note 1790979862409: The mucosa of the gut wall consists of three layers: a(n) {{c1::epithelium}}, {{c2::lamina propria}}, and {{c3::muscularis mucosa}}
- (acervo) note 1790979862760: External to the submucosal layer of the gut wall is the {{c1::muscularis externa}}
- (acervo) note 1790979863534: 
- (acervo) note 1790979864659: Which gut wall layer contains Auerbach's plexus? / {{c1::Muscularis externa}}
- (acervo) note 1790979865684: This is a magnified image of {{c1::oxyntic/fundic stomach}} / / [IMG paste-285af7c65716abbec41ced6e635e74ff448f45f5.png] / [IMG paste-438815d1674aec9e56d5491223223627e1a70d65.png] / [IMG paste-5fd70752adbdef98c597af64c2c
- (acervo) note 1790979866060: This is a magnified image of {{c1::pylorus}} / / [IMG paste-3c60c7c15a904453246835ff33ccaf3d3c6a6c83.png][IMG paste-d7c5ef5cd521a3cf957a7db2d65f6b58bfaa2489.png]
- (acervo) note 1790979866434: 
- (acervo) note 1790979867059: The gastric {{c1::glands}} of the stomach body contain the mucous cells, chief cells, and parietal cells
- (acervo) note 1790979867308: 
- (acervo) note 1790979867432: 
- (autoral) note 1790980013307: In rodents, the gastric glands grow and the mucosa completes its maturation around {{c1::weaning}}, in the third postnatal week
- (acervo) note 1791023352328: Parallel ridges on the lateral tongue, rudimentary in adults, are the {{c1::foliate}} papillae
- (acervo) note 1791023352694: Taste buds lie within the epithelium of the lingual {{c1::papillae}}
- (acervo) note 1791023353068: The oral cavity is lined by {{c1::stratified squamous}} epithelium, keratinized or not depending on the site
- (acervo) note 1791023353443: The tongue is a mass of {{c1::striated muscle}} covered by mucosa
- (acervo) note 1791023353568: The ventral surface of the tongue is smooth and covered by {{c1::lining}} mucosa
- (acervo) note 1791023354443: The enamel matrix is secreted by {{c1::ameloblasts}} of the enamel organ
- (acervo) note 1791023354569: The periodontal ligament anchors the {{c1::cementum}} to the alveolar bone
- (acervo) note 1791023355569: Serous cells are grouped into round secretory units called {{c1::acini}}
- (acervo) note 1791023355818: Mucous cells stain pale on H&E because their granules hold hydrophilic {{c1::mucins}}
- (acervo) note 1791023357017: The thin smooth muscle layer that separates the mucosa from the submucosa is the {{c1::muscularis mucosae}}
- (acervo) note 1791023357143: The submucosa is {{c1::denser}} connective tissue that carries the larger blood and lymph vessels
- (acervo) note 1791023359842: The pyloric sphincter is a thickening of the {{c1::middle circular}} layer of the gastric muscularis
- (acervo) note 1791023360742: Compared with fundic glands, typical mucous pyloric glands contain fewer {{c1::parietal}} and {{c2::chief}} cells
- (acervo) note 1791023361941: The gastric lumen and pits are lined by surface {{c1::mucous}} cells
- (acervo) note 1791023362067: Surface mucous cells coat the gastric mucosa with a thick, bicarbonate-rich {{c1::mucus layer}}
- (acervo) note 1791023362817: Gastric stem cells sit in the {{c1::isthmus}}, between the pit and the gland
- (acervo) note 1791023362943: Progenitor cells that move upward replace the surface mucous cells every {{c1::4–7}} days
- (acervo) note 1791023364242: Parietal cells lie among {{c1::mucous neck}} cells and in the deeper part of the gland
- (acervo) note 1791023364492: The deep, microvilli-lined channel that runs inside the parietal cell and receives its H⁺ is the {{c1::intracellular canaliculus}}
- (acervo) note 1791023365216: In the neck of gastric glands, scattered among parietal cells, {{c1::mucous neck}} cells secrete a less alkaline mucus
- (acervo) note 1791023365342: Unlike surface mucous cells, mucous neck cells have {{c1::round}} nuclei
- (acervo) note 1791023366191: Chief cells secrete protein, so their basal cytoplasm is packed with {{c1::rough ER}}
- (acervo) note 1791023366616: Scattered gastric cells with endocrine or paracrine function are the {{c1::enteroendocrine}} cells
- (acervo) note 1791023366868: Gastrointestinal enterochromaffin (EC) cells release {{c1::serotonin}}.

### 2026-uc08-biologia-tecidual-04-intestinos — 26 suspensos
- (acervo) note 1790980909855: 
- (acervo) note 1790980909978: 
- (acervo) note 1790980910107: All three parts of the small intestine contain {{c1::villi}} and {{c1::microvilli}}, which increase absorptive surface area
- (acervo) note 1790980910230: {{c1::Villi}} are small finger-like projections that increase the intestinal {{c2::surface area}}
- (autoral) note 1790980911279: Epithelial cells die by apoptosis and are shed at the villus {{c1::tip}}, as shown by TUNEL staining
- (autoral) note 1790980911405: Most intestinal epithelial cells arise in the {{c1::crypts}} and differentiate while migrating toward the villus tip.
- (autoral) note 1790980911781: Active intestinal stem cells at the crypt base are identified by the marker {{c1::Lgr5}}
- (acervo) note 1790980911905: 
- (acervo) note 1790980912028: 
- (acervo) note 1790980912155: 
- (acervo) note 1790980912277: 
- (autoral) note 1790980912831: The actin core of each microvillus is bundled by the structural protein {{c1::villin}}
- (autoral) note 1790980913855: Villi are leaf-shaped in the {{c1::duodenum}} and become finger-shaped toward the ileum
- (acervo) note 1790980914603: 
- (acervo) note 1790980916154: This H&E mucosa belongs to the {{c1::small intestine}} / [IMG bt4-jejunum.jpg]
- (autoral) note 1790980916280: The colon has no Paneth cells, so its crypt-base stem cells are supported by {{c1::deep crypt secretory}} cells
- (acervo) note 1791023295067: Short tubular glands that open between the villi are the {{c1::crypts of Lieberkühn}}
- (acervo) note 1791023296668: Dense microvilli on the apical surface of enterocytes form the {{c1::brush border}}
- (acervo) note 1791023296918: Microvilli enlarge the intestinal surface about {{c1::20}}-fold, villi 10-fold and plicae 3-fold
- (acervo) note 1791023297666: Goblet cells secrete glycoprotein {{c1::mucins}}, which hydrate into protective mucus
- (acervo) note 1791023298092: Open-type enteroendocrine cells reach the lumen and carry {{c1::chemoreceptors}} that sense nutrients
- (acervo) note 1791023298593: Inside the enterocyte, absorbed lipids are rebuilt into triglycerides in the {{c1::smooth ER}}
- (acervo) note 1791023298992: Smooth muscle fibers in the villus core come from the {{c1::muscularis mucosae}}
- (acervo) note 1791023299245: Paneth cells sit at the {{c1::base}} of the intestinal crypts
- (acervo) note 1791023302244: The large intestine absorbs water and electrolytes and turns {{c1::indigestible}} material into feces
- (acervo) note 1791023303318: Colonocytes have short irregular {{c1::microvilli}}, reflecting fluid absorption

### 2026-uc08-fisiologia-05-digestao-absorcao-nutrientes — 11 suspensos
- (acervo) note 1791000306302: Glucose and galactose are transported from the intestinal lumen into the cells by {{c1::Na+-dependent cotransport (SGLT1)}}
- (acervo) note 1791000307927: {{c1::Chymotrypsinogen}} (inactive) is activated to chymotrypsin (active) via trypsin
- (acervo) note 1791000308176: {{c1::Procarboxypeptidase}} (inactive) is activated to carboxypeptidase (active) via trypsin
- (acervo) note 1791000308425: Dipeptides and tripeptides are transported from the intestinal lumen into the cells by {{c1::H+}}-mediated cotransport
- (autoral) note 1791000309802: Pancreatic phospholipase A2 hydrolyzes phospholipids into a fatty acid and a {{c1::lysophospholipid}}
- (autoral) note 1791000311226: {{c1::ENaC}} channels mediate Na+ absorption in the distal colon
- (acervo) note 1791000313279: 1,25-dihydroxycholecalciferol increases {{c1::intestinal}} absorption of Ca2+ through synthesis of calbindin D-28K
- (acervo) note 1791000313527: Absorption of fat-soluble vitamins is dependent on the intact {{c2::ileum}}, {{c2::pancreatic}} secretions, and {{c2::bile}} emulsification
- (acervo) note 1791000313954: Vitamin K deficiency may occur in {{c1::newborns}} due to lack of {{c1::colonic bacteria}} that normally synthesize vitamin K
- (acervo) note 1791000314976: In the duodenum, vitamin B12 is cleaved by {{c1::pancreatic proteases}} from R-binder and attaches to {{c1::intrinsic factor}}
- (autoral) note 1791051794902: Maltose is split into two glucose molecules by the brush border enzyme {{c1::maltase}}

### 2026-uc08-fisiologia-06-secrecao-gastrica — 4 suspensos
- (acervo) note 1791014715994: Histamine, from ECL cells, activates {{c1::H2}} receptors (coupled to {{c1::Gs}}) on the basolateral membrane of parietal cells
- (acervo) note 1791014716874: Pepsinogen is secreted in response to {{c1::vagal stimulation}} and {{c2::local H+}}
- (autoral) note 1791014717050: In the duodenum, acid releases {{c1::secretin}}, which also stimulates pepsinogen secretion by chief cells
- (autoral) note 1791014718401: Most gut bacteria belong to two phyla, Firmicutes and {{c1::Bacteroidetes}}

### 2026-uc08-fisiologia-08-motilidade-i — 2 suspensos
- (autoral) note 1790974699480: What type of muscle forms the external anal sphincter? / / {{c1::Skeletal muscle (voluntary)}}
- (acervo) note 1791023270196: Autonomic axons in smooth muscle release transmitter from periodic swellings called {{c1::varicosities}}

### 2026-uc08-fisiologia-09-motilidade-ii — 4 suspensos
- (acervo) note 1790999833579: Which cranial nerve provides motor innervation to the muscles of mastication? / / {{c1::V3}}
- (acervo) note 1790999833829: The {{c1::masseter}}, {{c2::temporalis}}, and {{c3::medial pterygoid}} muscles are responsible for {{c4::closing}} the jaw (muscles of mastication)
- (autoral) note 1790999838304: Rectal distension triggers a sacral reflex through the {{c1::pelvic}} nerves that contracts the rectum and relaxes the internal anal sphincter
- (autoral) note 1791575030295: Transit time is about {{c1::2–4 h}} in the small intestine and up to {{c2::48 h}} in the colon

### 2026-uc19-farmacologia-01-introducao-mecanismos — 13 suspensos
- (autoral) note 1791762409172: Medical pharmacology studies drugs used for the diagnosis, {{c1::prevention}} and treatment of disease
- (autoral) note 1791762409550: Pharmacokinetics follows the drug through absorption, distribution, {{c1::metabolism}} and excretion
- (autoral) note 1791762409674: Pharmacodynamics covers drug–target interactions, {{c1::dose–response}} phenomena and mechanisms of therapeutic and toxic action
- (autoral) note 1791762409923: A drug can cause adverse effects by acting on its target in {{c1::other tissues}}
- (acervo) note 1791762412401: {{c1::Tolerance}} is when the body becomes used to a drug so it needs more of it to achieve the same effect.
- (autoral) note 1791762417222: An allosteric modulator that weakens the response to the endogenous agonist is a {{c1::negative}} allosteric modulator
- (autoral) note 1791762418150: Because of signal amplification and {{c1::spare receptors}}, EC50 need not equal the dissociation constant Kd
- (autoral) note 1791762418650: An agonist binds a receptor and {{c1::activates}} it, triggering a cellular response
- (autoral) note 1791762418773: An antagonist occupies the receptor but has zero {{c1::efficacy}}, so it blocks the agonist without a response
- (autoral) note 1791762421773: Antagonist drugs block or reduce the action of an {{c1::agonist}}
- (autoral) note 1791762422823: Antagonism on the dose–response curve: / 1. Competitive antagonist — {{c1::increases EC50}} without changing Emax / 2. Noncompetitive antagonist — {{c2::reduces Emax}}
- (autoral) note 1791762427174: Drugs act on ion channels either as blockers of permeation or as {{c1::modulators}} of opening probability
- (autoral) note 1791826292220: [IMG fa01-g-antagonismo-nao-competitivo.png] / Which type of antagonism lowers the maximal response even at high agonist doses? {{c1::Noncompetitive}}

### ? — 5 suspensos
- (acervo) note 1784308059664: Em pluripotente, pluri- indica {{c1::vários}}.
- (acervo) note 1784308059731: Em heterozigoto, hetero- indica {{c1::diferente}}.
- (acervo) note 1790974692329: 
- (autoral) note 1790999838179: Food entering the stomach triggers the {{c1::gastrocolic}} reflex, which increases colonic mass movements
- (autoral) note 1791000308801: Absorbed monosaccharides and amino acids enter the {{c1::portal}} circulation and travel to the liver

