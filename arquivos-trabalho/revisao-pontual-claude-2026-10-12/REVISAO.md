# Revisão incremental dos decks de Claude

Revisão direta e focal: não foi avaliação cega nem certificação científica integral dos cinco decks. Fontes locais: snapshots anteriores, planos, slides e imagens das respectivas corridas. Critério: recuperar o objetivo da aula, retirar pistas que substituem interpretação, distinguir núcleo de exemplos e limitar Extras ao que ajuda a compreensão.

## Resultado aplicado

60 notas distintas: 31 com alterações de campos e 31 com ajustes de cor (há sobreposição). Nenhum card novo nesta rodada. IDs, histórico, agendamento, comentários e suspensões preservados nas correções, conforme verificacao.json; 18 notas originais de referência conferidas sem alterações. As correções foram incorporadas aos specs, planos e correcoes-vivas, para sobreviver à próxima geração.

| Aula | Notas ajustadas | Foco |
|---|---:|---|
| FA01 Farmacologia | 26 | Oito gráficos exigem leitura; mecanismo no Extra; exemplos periféricos rosa |
| RD02 Diagnóstico radiológico | 6 | Condições de escolha de exame explícitas; remoção de absolutos inadequados |
| PT03 Diagnóstico patológico | 18 | Conceitos organizadores valorizados; corantes específicos periféricos; Extras sem mini-aulas clínicas |
| MB34 Genética bacteriana | 2 | Recuperar intercalação em vez do nome do exemplo; Tn3 rosa |
| MB39 Homem e ambiente | 8 | Precisão sobre microbiota e cores de detalhes periféricos |

## Critérios transferíveis derivados da comparação local

- Gráfico: perguntar sobre a curva identificável, deixando deslocamento, platô e interpretação para a resposta/Extra quando seriam pistas. Não basta incluir uma figura se a frase já resolve a questão.
- Menor unidade útil pode ser uma relação: histoquímica versus imuno-histoquímica organiza os detalhes dos corantes. Cobrar apenas nomes não garante essa compreensão.
- Extra: avaliar texto e cada figura separadamente. Uma micrografia pertinente foi preservada; tabela de glicogenoses e algoritmo clínico de tireoide foram retirados por extrapolar o alvo.
- Cor acompanha a importância do alvo na aula, sem percentual desejado. Exemplos úteis podem ser rosa; o núcleo precisa de recuperação própria.
- Frases naturais e qualificações suficientes evitam ensinar absolutos falsos. Concisão não justifica retirar a condição que torna a afirmação correta.

Esses critérios são inferências pedagógicas a partir dos cards; não foram medidos por um ensaio de retenção com o aluno.

## Verificação e limites

- Gates finais: FA01 54/54, RD02 56/56, PT03 56/56, MB39 54/54. MB34 53/54: 134 Tabs anteriores desatualizados; não declarar o deck inteiro entregue/revalidado.
- Os 33 cards com campos alterados tiveram Tab atualizado no formato Básico / Explicação / Na aula / Não confundir. Revisão humana focal das explicações; não alegar leitura integral de todos os Tabs da coleção.
- Verificação visual com HTML/CSS real do modelo e imagens locais: arquivos em visual/. Inspeção focal de frentes de gráficos/GPCR e versos de agonismo parcial/escolha por custo. Não é certificação visual de todos os cards.
- 29 testes de lint, explicações e gates passaram. Corrigido falso positivo do lint que proibia a expressão científica comum “this is”; teste de regressão incluído.
- Das 230 retiradas registradas nas quatro corridas de escopo, 210 já não existiam; 20 restantes foram apagadas após backup APKG verificado e checagem de associações. Ver exclusao-recibo.json e backup-retiradas-0.apkg.
- Pacotes finais UC03/UC19 copiados e conferidos por hash na montagem local do Drive. Isso não comprova upload remoto. Ver entrega-pacotes.json. Produção concorrente de Claude pode publicar pacote posterior; não substituir esse pacote por snapshot antigo.
- RD04/RD05 foram concluídos por Claude durante esta sessão segundo o estado atualizado do projeto; não foram revisados nesta rodada.

## Fontes externas usadas para precisão científica

A pesquisa apoiou correções pontuais, não substituiu a análise local:

- [IUPHAR: farmacodinâmica](https://pharmacologyeducation.org/pharmacodynamics/): eficácia, potência e antagonismo.
- [ACR/RSNA: dor no quadrante superior direito](https://www.radiologyinfo.org/en/info/acs-right-upper-quadrant-pain): contexto da escolha por ultrassom.
- [ACR/RSNA: TC na gravidez](https://www.radiologyinfo.org/en/info/safety-ct-pregnancy): evitar proibição absoluta de exame necessário.
- [NCI: testes de biomarcadores](https://www.cancer.gov/about-cancer/treatment/types/biomarker-testing-cancer-treatment): alvo molecular não se reduz a superexpressão de receptor.
- [Estudo primário da conjuntiva](https://pmc.ncbi.nlm.nih.gov/articles/PMC5054734/), [esôfago](https://pmc.ncbi.nlm.nih.gov/articles/PMC384727/) e [pulmão](https://pmc.ncbi.nlm.nih.gov/articles/PMC4590020/): correções dos absolutos sobre esterilidade/ausência de microbiota. Para conjuntiva e esôfago, foram consultados trechos indexados; não alegar leitura integral. Divergência com slides registrada nas justificativas.

## Registro verificável: antes → depois

Textos abaixo são HTML dos campos, permitindo verificar cloze e destaques. No Anki, buscar `nid:ID`.

### fa01 / g-potencia — nid:1791826286643

Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no Extra. Mesmos IDs/clozes.

**Text — antes:**
```html
<img src="fa01-g-potencia.png"><br>On these <b>dose–response curves</b>, drug {{c1::A}} is the most potent, reaching 50% of its effect at the lowest concentration
```

**Depois:**
```html
<img src="fa01-g-potencia.png"><br>Which drug is <b>most potent</b>? {{c1::A}}
```

**Extra — antes:**
```html
- Potency is read on the x-axis (EC<sub>50</sub>)
```

**Depois:**
```html
- A has the lowest EC<sub>50</sub>, read at half of its own maximal response.<br>- A and B reach the same plateau despite different potencies.
```

### fa01 / g-eficacia — nid:1791826286795

Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no Extra. Mesmos IDs/clozes.

**Text — antes:**
```html
<img src="fa01-g-potencia.png"><br><b>Drugs A and B</b> reach the same plateau, so they share the same {{c1::efficacy}} despite different potencies
```

**Depois:**
```html
<img src="fa01-g-potencia.png"><br>Which drugs have the <b>same maximal efficacy</b>? {{c1::A and B}}
```

**Extra — antes:**
```html
- Efficacy is read on the y-axis (E<sub>max</sub>)<br>- Drug C has lower potency and lower efficacy
```

**Depois:**
```html
- A and B reach the same plateau. C reaches a lower maximum.<br>- Compare plateau height for efficacy and EC<sub>50</sub> for potency.
```

### fa01 / g-inverso — nid:1791826287669

Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no Extra. Mesmos IDs/clozes.

**Text — antes:**
```html
<img src="fa01-g-agonismo.png"><br>The curves that fall <b>below the baseline</b> response belong to {{c1::inverse}} agonists
```

**Depois:**
```html
<img src="fa01-g-agonismo.png"><br>The <b>red diamonds and purple triangles</b> represent {{c1::inverse agonists}}
```

**Extra — antes:**
```html
- They need a receptor with constitutive activity
```

**Depois:**
```html
- Both curves fall below the basal response, indicating suppression of constitutive activity.<br>- The flat blue curve represents a neutral antagonist.
```

### fa01 / g-neutro — nid:1791826287819

Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no Extra. Mesmos IDs/clozes.

**Text — antes:**
```html
<img src="fa01-g-agonismo.png"><br>The <b>flat curve</b> at zero response belongs to a {{c1::neutral antagonist}}
```

**Depois:**
```html
<img src="fa01-g-agonismo.png"><br>The <b>blue triangles</b> represent a {{c1::neutral antagonist}}
```

**Extra — antes:**
```html
- It binds without changing basal activity
```

**Depois:**
```html
- Basal activity remains unchanged as concentration increases.<br>- An inverse agonist would lower activity below baseline.
```

### fa01 / g-parcial — nid:1791826287969

Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no Extra. Mesmos IDs/clozes.

**Text — antes:**
```html
<img src="fa01-g-agonismo.png"><br>The curve that rises but levels off near <b>50%</b> belongs to a {{c1::partial}} agonist
```

**Depois:**
```html
<img src="fa01-g-agonismo.png"><br>The <b>green squares</b> represent a {{c1::partial agonist}}
```

**Extra — antes:**
```html
- Full agonists reach 100%
```

**Depois:**
```html
- The plateau is lower than that of the full agonist shown in black.<br>- The value near 50% belongs to this example; partial agonists do not all have a 50% maximum.
```

### fa01 / g-competitivo — nid:1791826292069

Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no Extra. Mesmos IDs/clozes.

**Text — antes:**
```html
<img src="fa01-g-antagonismo.png"><br>In the <b>upper graph</b>, the antagonist shifts the agonist curve to the right but the maximum is still reached, typical of {{c1::competitive}} antagonism
```

**Depois:**
```html
<img src="fa01-g-antagonismo.png"><br>Which type of <b>antagonism</b> is shown in the upper graph? {{c1::Competitive}}
```

**Extra — antes:**
```html
- More agonist overcomes the block
```

**Depois:**
```html
- The agonist curve shifts right, but its maximum is preserved.<br>- A higher agonist concentration overcomes the blockade.
```

### fa01 / g-naocompetitivo — nid:1791826292220

Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no Extra. Mesmos IDs/clozes.

**Text — antes:**
```html
<img src="fa01-g-antagonismo.png"><br>In the <b>lower graph</b>, the antagonist lowers the maximal response, typical of {{c1::noncompetitive}} antagonism
```

**Depois:**
```html
<img src="fa01-g-antagonismo.png"><br>Which type of <b>antagonism</b> is shown in the lower graph? {{c1::Noncompetitive}}
```

**Extra — antes:**
```html
- Adding agonist cannot restore the maximum
```

**Depois:**
```html
- The maximum falls despite increasing the agonist concentration.<br>- The upper graph instead shows a surmountable, competitive blockade.
```

### fa01 / g-quantal — nid:1791826294319

Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no Extra. Mesmos IDs/clozes.

**Text — antes:**
```html
<img src="fa01-g-quantal.png"><br>The farther apart the <b>ED<sub>50</sub></b> and <b>TD<sub>50</sub></b> curves, the {{c1::wider}} the margin of safety
```

**Depois:**
```html
<img src="fa01-g-quantal.png"><br>Which curves determine the <b>therapeutic index</b>? {{c1::Therapeutic and toxic}}
```

**Extra — antes:**
```html
- TI = TD<sub>50</sub>/ED<sub>50</sub>
```

**Depois:**
```html
- Read ED<sub>50</sub> and TD<sub>50</sub> at 50% of individuals, then calculate TD<sub>50</sub>/ED<sub>50</sub>.<br>- This is a population response, not half of the maximal effect in one person.
```

### fa01 / alvo-sem-endereco — nid:1791762409923

Troca a lacuna genérica choose por relação farmacológica recuperável; lâminas 24/35.

**Text — antes:**
```html
A drug acts wherever its <b>target</b> is expressed, so it cannot {{c1::choose}} the painful site
```

**Depois:**
```html
A drug can cause <b>adverse effects</b> by acting on its target in {{c1::other tissues}}
```

**Extra — antes:**
```html
- The same target in other tissues explains adverse effects
```

**Depois:**
```html
- Target distribution helps explain why the desired effect may be accompanied by effects elsewhere.
```

### fa01 / gpcr — nid:1791762410348

Corrige generalização bind glycoproteins na cópia NEBLI e retira patologias laterais do Extra; IUPHAR Receptors. Original preservado.

**Text — antes:**
```html
{{c1::<b>G protein-coupled</b>}} <b>receptors</b> bind glycoproteins and contain three domains; an <u>extracellular domain</u> for {{c2::ligand}} binding, a <u>transmembrane domain</u>, and an <u>intracellular domain</u> coupled with heterotrimeric G proteins
```

**Depois:**
```html
{{c1::<b>G protein–coupled</b>}} receptors transmit extracellular {{c2::ligand}} binding to heterotrimeric G proteins inside the cell
```

**Extra — antes:**
```html
The <b>G-alpha subunits</b> of these G proteins are associated with unique pathologies:<br>- <b>G<u>s</u>-alpha</b>: McCune Albright / Albrights Hereditary Osteodystrophy<br>- <b>G<u>q</u>-alpha</b>: Sturge-Weber
```

**Depois:**
```html
- Receptor activation couples an extracellular signal to intracellular enzymes or ion channels.
```

### fa01 / rtk — nid:1791762411098

Retira generalização de dimerização que não descreve corretamente todos os receptores do exemplo; mantém princípio da lâmina 25.

**Extra — antes:**
```html
- Ligand binding → dimerization and autophosphorylation (e.g., insulin receptor)
```

**Depois:**
```html
- Ligand binding activates receptor kinase signaling and phosphorylation of intracellular proteins.
```

### fa01 / gc — nid:1791762412899

Extra passa a explicar a cadeia da aula, sem farmacoterapia de hipertensão pulmonar.

**Extra — antes:**
```html
- cGMP then acts to relax smooth muscle; same mechanism as ANP but with a <b>soluble guanylyl cyclase</b> receptor<br><br>- Agents that mimic nitric oxide (e.g., riociguat) are useful in treating pulmonary arterial hypertension
```

**Depois:**
```html
- NO activates soluble guanylyl cyclase → increased cGMP → smooth-muscle relaxation.
```

### fa01 / bupre — nid:1791762420425

Retira conduta de início de tratamento; conserva conexão com agonismo parcial.; Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

**Extra — antes:**
```html
- Buprenorphine-naloxone (Suboxone)<br><br>- Patient <u>must</u> have symptoms of <u>opioid withdrawal</u> <b>prior</b> to administration to avoid <b>causing</b> withdrawal symptoms
```

**Depois:**
```html
- A partial agonist produces a lower maximal receptor response than a full agonist.<br>- Buprenorphine illustrates this property at μ-opioid receptors.
```

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / atropina — nid:1791762422275

Mantém exemplo cobrado em prova e mecanismo; retira sequência terapêutica lateral.

**Extra — antes:**
```html
Treat with <u>atropine</u> <b>first</b> because <u>pralidoxime</u> can cause transient inhibition of AChE
```

**Depois:**
```html
- Atropine illustrates competitive antagonism at muscarinic receptors.<br>- The receptor subtype matters: nicotinic effects are not blocked by atropine.
```

### fa01 / nitro-prodroga — nid:1791762412151

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / nitrato-tolerancia — nid:1791762412275

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / pde5 — nid:1791762413301

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / manitol — nid:1791762415273

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / h1-inverso — nid:1791762419700

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / bupre-abstinencia — nid:1791762420550

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / varfarina-fenobarbital — nid:1791762424899

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / it-baixo — nid:1791762425700

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / anestesico-na — nid:1791762428200

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / gq — nid:1791762410526

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / gs — nid:1791762410700

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### fa01 / gi — nid:1791762410873

Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.

Cor aplicada: {"aula": "2026-uc19-farmacologia-01-introducao-mecanismos", "cor": "rosa"}

### rd02 / mais-barato — nid:1791810568420

Conserva princípio econômico da aula, condicionado à adequação clínica; elimina cheapest como critério absoluto.

**Text — antes:**
```html
The best <b>imaging exam</b> is the {{c1::cheapest}} one that answers the clinical question
```

**Depois:**
```html
Among <b>clinically appropriate imaging tests</b> that answer the same question, prefer the {{c1::less costly}} option
```

**Extra — antes:**
```html
- Ultrasound for gallstones avoids ordering CT or MRI
```

**Depois:**
```html
- Diagnostic adequacy and patient safety come before cost.<br>- A more expensive or technologically complex test is not automatically better.
```

### rd02 / ruq-us — nid:1791810565995

Restringe cópia NEBLI ao caso da aula; retira regra falsa other quadrants use CT. ACR Right Upper Quadrant Pain.

**Text — antes:**
```html
Generally, pathology of the RUQ is confirmed via {{c1::ultrasound::imaging modality}}
```

**Depois:**
```html
For suspected <b>biliary disease</b> causing right upper quadrant pain, the usual first imaging test is {{c1::ultrasound::modality}}
```

**Extra — antes:**
```html
<div>- e.g., for cholecystitis</div><br><div>- Other quadrants use <b>CT </b>scan</div><div></div>
```

**Depois:**
```html
- The initial choice follows the diagnostic hypothesis.<br>- Further imaging depends on the ultrasound findings and the clinical scenario.
```

### rd02 / radiacao-gravidez — nid:1791810574372

Evita ensinar gestação como contraindicação absoluta a RX/TC; ACR/RSNA CT safety during pregnancy.

**Text — antes:**
```html
<b>Ionizing radiation</b> is teratogenic, so radiography and CT are avoided in {{c1::pregnancy}}
```

**Depois:**
```html
During <b>pregnancy</b>, ultrasound or MRI is preferred when it can answer the clinical question without {{c1::ionizing radiation}}
```

**Extra — antes:**
```html
- The risk to the developing embryo is highest early in pregnancy
```

**Depois:**
```html
- A necessary radiograph or CT may still be appropriate when its diagnostic benefit outweighs the risk.<br>- Risk depends on the examination, fetal dose and stage of pregnancy.
```

### rd02 / rx-contraste-baixo — nid:1791810584372

Retira comparação absoluta incorreta entre resolução espacial de RX e TC; explica limitação por contraste/sobreposição.

**Extra — antes:**
```html
- Its spatial resolution is also lower than that of CT
```

**Depois:**
```html
- Soft tissues may have similar X-ray attenuation and overlap in a projection image.<br>- CT separates structures into cross-sectional images.
```

### rd02 / angio-radiacao-iodo — nid:1791810587172

Corrige intravenous como rota universal da angiografia por cateter; coerência com card angio-def da própria aula.

**Text — antes:**
```html
<b>Digital angiography</b> uses ionizing radiation and intravenous {{c1::iodinated}} contrast
```

**Depois:**
```html
Catheter <b>angiography</b> uses X-rays and {{c1::iodinated}} contrast injected into the vessel being examined
```

**Extra — antes:**
```html
- It images the vessels with X-rays while contrast is injected
```

**Depois:**
```html
- Contrast outlines the vessel lumen.<br>- The injection route depends on the vessel and procedure.
```

### rd02 / rx-primeira-linha — nid:1791810584997

Elimina generalização first exam in most situations; preserva vantagem logística ensinada.

**Text — antes:**
```html
<b>Plain films</b> are usually the first-line imaging because of low dose and easy {{c1::availability}}
```

**Depois:**
```html
Low cost and wide {{c1::availability}} make <b>plain radiography</b> useful as an initial test for suitable clinical questions
```

**Extra — antes:**
```html
- It is usually the first exam in most situations
```

**Depois:**
```html
- The initial test depends on the suspected condition; radiography is not first-line for every region or complaint.
```

### pt03 / etiologia-multipla — nid:1791810350574

Evita misturar mecanismos de formas diferentes de diabetes no mesmo exemplo.

**Extra — antes:**
```html
- Diabetes combines HLA-related genes with diet and obesity<br>- Atherosclerosis and cancer are multifactorial
```

**Depois:**
```html
- Genetic susceptibility and environmental exposures can contribute together to a disease.
```

### pt03 / fna-tireoide — nid:1791810359272

Recupera a ferramenta/citologia, não um algoritmo clínico de todo nódulo; retira must do because highly vascularized.

**Text — antes:**
```html
<div>How is a <b>biopsy</b> performed for a <b>thyroid nodule</b>? </div><br><div>{{c1::Fine needle aspiration (FNA)}}</div>
```

**Depois:**
```html
Which sampling method obtains <b>isolated cells</b> from a thyroid nodule? {{c1::Fine-needle aspiration (FNA)}}
```

**Extra — antes:**
```html
Must do FNA because the thyroid is highly vascularized<br><br><img src="b63923145e281b74c5583108a4094479.webp" width="850px">
```

**Depois:**
```html
- The aspirate supports cytological evaluation.<br>- A tissue biopsy also preserves architecture, which isolated cells cannot fully show.
```

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "azul"}

### pt03 / he-primeiro — nid:1791810361547

Remove always e torna explícita a função organizadora do H&E; lâminas 15/23.; Focaliza a relação morfologia → testes complementares, sem expressão longa na cloze.

**Text — antes:**
```html
<b>H&amp;E</b> is always performed first, because tissue morphology must be known before {{c1::special}} tests
```

**Depois:**
```html
Routine <b>H&E</b> provides the morphological context for choosing {{c1::ancillary tests}}
```

**Extra — antes:**
```html
- Special stains are chosen after seeing the H&amp;E pattern
```

**Depois:**
```html
- H&E shows the overall tissue pattern.<br>- Additional methods answer a more specific diagnostic question.
```

### pt03 / terapia-alvo — nid:1791810368374

Corrige only overexpresses para o princípio geral de seleção por alvo; NCI Biomarker Testing.

**Text — antes:**
```html
<b>Targeted therapy</b> is worthwhile only when the tumor {{c1::overexpresses}} the target receptor
```

**Depois:**
```html
Selection of a <b>targeted cancer therapy</b> depends on identifying a suitable {{c1::molecular target}} in the tumor
```

**Extra — antes:**
```html
- Molecular characterization shows whether the receptor drives the tumor
```

**Depois:**
```html
- A relevant biomarker may involve protein expression or a genetic alteration.<br>- Receptor overexpression is one example, not a universal requirement.
```

### pt03 / oil-red — nid:1791810363770

Retira comparação McArdle/MCAD alheia ao objetivo introdutório.; Conserva a micrografia de lipídios relevante; exclui a tabela de doenças metabólicas e a comparação clínica.

**Extra — antes:**
```html
<div>Helps <u>distinguish</u> <b>McArdle's disease</b> (PAS) from <b>MCAD deficiency</b> (oil red O)<br></div><br><img src="4b39a42452786b009cb3c3ea4cc5bdde.jpg" height="200"><img src="143ca9b446258c89d24154845b37ea0f.jpg" height="200">
```

**Depois:**
```html
- Lipid stains answer a specific compositional question that routine morphology may not resolve.<br><img src="143ca9b446258c89d24154845b37ea0f.jpg" height="250">
```

### pt03 / pas-glicogenio — nid:1791810364025

Retira comparação de doenças metabólicas usada como expansão lateral.

**Extra — antes:**
```html
Helps <u>distinguish</u> <b>McArdle's disease</b> (PAS), from <b>MCAD deficiency</b> (oil red O)<br><br><img src="4b39a42452786b009cb3c3ea4cc5bdde.jpg" alt="Vacuolar myopathy mcArdle type V glcogenosis.jpg" height="250" style="width: 432px;"><img src="143ca9b446258c89d24154845b37ea0f.jpg" height="250" style="width: 432px;"><img src="8412e62f35b76d85fa69d4b05169138d.webp" width="800">
```

**Depois:**
```html
- PAS highlights carbohydrate-rich structures; interpret the staining pattern in its tissue context.
```

### pt03 / pneumonia-patogenese — nid:1791810349772

Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. Harmoniza com a revisão de escopo.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "rosa"}

### pt03 / picrosirius — nid:1791810362699

Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. Harmoniza com a revisão de escopo.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "rosa"}

### pt03 / elastica — nid:1791810362822

Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. Harmoniza com a revisão de escopo.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "rosa"}

### pt03 / bh — nid:1791810363072

Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. Harmoniza com a revisão de escopo.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "rosa"}

### pt03 / melanina — nid:1791810364272

Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. Harmoniza com a revisão de escopo.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "rosa"}

### pt03 / ihq-24h — nid:1791810364399

Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. Harmoniza com a revisão de escopo.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "rosa"}

### pt03 / hormonioterapia — nid:1791810368797

Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. Harmoniza com a revisão de escopo.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "rosa"}

### pt03 / biopsia-def — nid:1791810359400

Conceito organizador duradouro das ferramentas diagnósticas explicitamente ensinado, antes das listas de corantes.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "verde"}

### pt03 / histoquimica-def — nid:1791810359920

Conceito organizador duradouro das ferramentas diagnósticas explicitamente ensinado, antes das listas de corantes.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "verde"}

### pt03 / ihq-vs-histo — nid:1791810360046

Conceito organizador duradouro das ferramentas diagnósticas explicitamente ensinado, antes das listas de corantes.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "verde"}

### pt03 / he-principal — nid:1791810361836

Conceito organizador duradouro das ferramentas diagnósticas explicitamente ensinado, antes das listas de corantes.

Cor aplicada: {"aula": "2026-uc03-patologia-03-diagnostico-patologico", "cor": "verde"}

### mb34 / tn3 — nid:1791730472958

Associação nominal Tn3–ampicilina é detalhe, como Tn5/Tn9/Tn10; mecanismo geral permanece.

Cor aplicada: {"aula": "2026-uc03-microbiologia-34-genetica-bacteriana", "cor": "rosa"}

### mb34 / planar-etidio — nid:1791730469435

Troca nome específico do exemplo por mecanismo ensinável; exemplo passa ao Extra.

**Text — antes:**
```html
<b>Planar molecules</b> such as {{c1::ethidium bromide}} intercalate between <b>DNA bases</b> and interrupt polymerase synthesis
```

**Depois:**
```html
Planar <b>DNA mutagens</b> can {{c1::intercalate}} between adjacent base pairs
```

**Extra — antes:**
```html
- Intercalation causes insertions or deletions (frameshift) when the strand is copied<br>- Acridine dyes act the same way
```

**Depois:**
```html
- Ethidium bromide is an example.<br>- Insertion between base pairs distorts the DNA structure and can disrupt accurate replication.
```

### mb39 / conjuntiva-esteril — nid:1791780583732

Corrige contradição esterilidade/microbiota no slide 8; estudo primário PMC5054734. Divergência com fonte docente registrada.

**Text — antes:**
```html
The <b>conjunctiva</b> is normally {{c1::sterile}}
```

**Depois:**
```html
The healthy <b>conjunctiva</b> has a {{c1::low}} bacterial biomass, limited by tears and local defenses
```

**Extra — antes:**
```html
- Tears wash and lyse bacteria that try to settle
```

**Depois:**
```html
- Low bacterial abundance does not mean absolute sterility.<br>- Tears and lysozyme help limit colonization.
```

### mb39 / vias-inferiores — nid:1791780583277

Corrige esterilidade absoluta do slide 8; estudo primário Dickson et al. 2015, PMC4590020.

**Text — antes:**
```html
The <b>bronchioles</b> and alveoli are normally {{c1::sterile}}
```

**Depois:**
```html
Microbes in healthy <b>lower airways</b> reflect a balance between immigration and {{c1::elimination}}
```

**Extra — antes:**
```html
- Mucociliary clearance keeps the lower airways sterile
```

**Depois:**
```html
- Healthy lungs can contain low-biomass microbial communities.<br>- Detection of microbes alone does not establish infection.
```

### mb39 / esofago — nid:1791780595183

Remove ausência absoluta de microbiota; estudo primário PNAS 2004, PMC384727.

**Text — antes:**
```html
The <b>esophagus</b> has no resident microbiota, and its organisms come from {{c1::saliva}} and food
```

**Depois:**
```html
The <b>esophageal microbiota</b> is closely linked to microorganisms from the {{c1::oral cavity}}
```

**Extra — antes:**
```html
- It is a transit organ with no stable colonization
```

**Depois:**
```html
- Swallowed saliva contributes organisms, and bacteria can also associate with the esophageal mucosa.<br>- It is not accurate to describe the healthy esophagus as lacking a microbiota.
```

### mb39 / pele-oito-horas — nid:1791780580926

Número específico ou exemplo histórico/anatômico lateral; preservar conceitos de recolonização, maturação, imunidade e portador.

Cor aplicada: {"aula": "2026-uc03-microbiologia-39-homem-ambiente-microrganismo", "cor": "rosa"}

### mb39 / estabilidade-2anos — nid:1791780598230

Número específico ou exemplo histórico/anatômico lateral; preservar conceitos de recolonização, maturação, imunidade e portador.

Cor aplicada: {"aula": "2026-uc03-microbiologia-39-homem-ambiente-microrganismo", "cor": "rosa"}

### mb39 / intestino-orgao-imune — nid:1791780602393

Número específico ou exemplo histórico/anatômico lateral; preservar conceitos de recolonização, maturação, imunidade e portador.

Cor aplicada: {"aula": "2026-uc03-microbiologia-39-homem-ambiente-microrganismo", "cor": "rosa"}

### mb39 / typhoid-mary — nid:1791780621403

Número específico ou exemplo histórico/anatômico lateral; preservar conceitos de recolonização, maturação, imunidade e portador.

Cor aplicada: {"aula": "2026-uc03-microbiologia-39-homem-ambiente-microrganismo", "cor": "rosa"}

### mb39 / typhi-vesicula — nid:1791780621528

Número específico ou exemplo histórico/anatômico lateral; preservar conceitos de recolonização, maturação, imunidade e portador.

Cor aplicada: {"aula": "2026-uc03-microbiologia-39-homem-ambiente-microrganismo", "cor": "rosa"}

### pt03 / puncao-guiada — nid:1791810361048

Recupera a função do guia de imagem; o card FNA recupera o método de amostragem, evitando duas perguntas pela mesma resposta.

**Text — antes:**
```html
<b>Ultrasound</b> guides the needle during {{c1::fine-needle aspiration}} of a thyroid nodule, an interface of pathology and radiology
```

**Depois:**
```html
During <b>fine-needle aspiration</b>, {{c1::ultrasound}} helps guide the needle into the lesion
```
