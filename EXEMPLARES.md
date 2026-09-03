# EXEMPLARES — Referência few-shot do padrão NEBLI

**Status:** documento vivo. Atualizado conforme novos exemplares são identificados em resumos gerados.

**Última atualização:** 2026-05-26 — Categorias 8 (`atencao-box`) e 9 (`clinica-box`) preenchidas com exemplares concretos extraídos de Diferenciação Celular (2 + 1). Cota canônica de boxes embutida no rationale. Anteriormente (2026-05-15) — pré-retomada da Geração 20: Categoria 16 adicionada (catálogo de família proteica/molecular = parágrafo + tabela, padrão GLUTs — originalmente Categoria 17, renumerada em 2026-05-26 após remoção da E4). Anteriormente na mesma data: Categoria 15 (figura integrada lateralmente — `#figura-lateral`) criada com exemplar concreto do novo helper introduzido em 2026-05-15. **Categoria removida 2026-05-26: Etapa 4 (cor por formato) — E4 saiu do pipeline em 2026-05-22 (canônico), exemplares de `#prova-mc/#prova-ce/#prova-discursiva` arquivados.** Categoria 14 (Glossário de siglas) reescrita para refletir o novo padrão de footnote no rodapé. Anterior: 2026-05-14 — auditoria pré-Geração 20.

**Propósito:** este arquivo é a referência operacional do que é "bom" no padrão NEBLI. Cada exemplar é um trecho real, escolhido pelo usuário (Davi), de um resumo já gerado, classificado por padrão didático e anotado com o motivo de funcionar. Substitui regras abstratas ("explique o porquê", "use distratores mecanísticos") por demonstrações concretas que o REDATOR-E1 e o QUESTIONADOR podem imitar.

---

## Como usar este arquivo

**REDATOR-E1**, antes de redigir a Etapa 1 de um resumo novo, lê este arquivo e usa os exemplares como referência few-shot. Cada categoria tem ao final um bloco "Quando usar este padrão" — respeitar essas regras (especialmente as restrições: "não usar quando…").

**QUESTIONADOR**, antes de redigir Etapas 2/3, lê especificamente as categorias 10 (Discursivas modelares) e 11 (Distratores mecanísticos), e segue o padrão demonstrado.

**COMPILADOR** não precisa ler este arquivo — sua função é determinística.

Quando um exemplar conflitar com uma instrução abstrata do CLAUDE.md ou do prompt mestre, **o exemplar tem precedência** — ele é a operacionalização concreta da instrução.

**Exceção única (CANON 2026-09-03): o `CLAUDE.md` § Registro científico vence o exemplar.** Os exemplares deste arquivo foram escritos sob o registro anterior e carregam três padrões que hoje estão revogados: (a) **jargão adiado ou parafraseado** — "ligação temporária entre o açúcar e a enzima (chamada thiohemiacetal)"; hoje o termo entra junto da definição, na mesma frase; (b) **pergunta retórica de ponte** — o "Por que isso importa?" do Exemplar 1.2 é anterior ao banimento de 2026-05-29 e não deve ser imitado; (c) **frase de moldura ou de reafirmação** que não afirma fato, não faz ponte causal e não nomeia termo. O que continua valendo integralmente nos exemplares é o **gesto pedagógico** — cada parágrafo com função discreta, cadeia mecanística completa, exemplo canônico em vez de nome citado, ritmo e variação de abertura. Leia-os pelo gesto; a superfície da frase segue o registro novo.

---

## Quando usar cada categoria (índice operacional + lazy-load)

**Canônico 2026-05-26 — economia de contexto:** este arquivo tem 17K tokens; ler tudo a cada resumo gasta ~40% do contexto sem ganho. **A partir de agora você lê APENAS** (a) as 3 categorias universais marcadas com `*` (toda E1 usa); (b) as categorias listadas como "aplicar" no tema do resumo conforme a tabela abaixo. Categorias não-marcadas: pular. Em dúvida, abrir só o "POR QUE É BOM" do exemplar (3-5 linhas) — não o trecho completo.

| # | Categoria | Tags temáticas | Universal? |
|---|---|---|---|
| 1 | Explicação mecanística parágrafo-por-parágrafo | *qualquer mecanismo encadeado* | **\* universal** |
| 2 | Origem evolutiva / pergunta motivadora | #celula #evolucao #metabolismo #neuro | quando "porquê" > "como" |
| 3 | Abertura por desfazer confusão comum | #neuro #genetica #imuno | só se há confusão clássica documentada |
| 4 | Magnitudes ancoradas e comparação externa | #neuro #metabolismo #fisiologia | quando há números importantes |
| 5 | Refinamento histórico de teoria | #celula #genetica #imuno | só se há modelo histórico revisado |
| 6 | Organização terminológica | #sinalizacao #receptores #genetica | família com nomenclatura ramificada |
| 7 | Analogia construtiva | #metabolismo #sinalizacao #membrana | mecanismo abstrato + analogia segura |
| 8 | Boxes `.atencao-box` | *qualquer tema com inversão conceitual* | **\* universal** |
| 9 | Boxes `.clinica-box` | #metabolismo #fisiologia #genetica | clínica com cadeia 4-6 linhas |
| 10 | Discursivas modelares | *QUESTIONADOR sempre* | só se for QUESTIONADOR |
| 11 | Distratores mecanísticos para objetivas | *QUESTIONADOR sempre* | só se for QUESTIONADOR |
| 12 | Cálculo bem explicado | #metabolismo #enzimas #farmaco | só se houver matemática |
| 13 | Texto motivador em questão objetiva | *QUESTIONADOR sempre* | só se for QUESTIONADOR |
| 14 | Glossário de siglas (footnote) | *qualquer tema com 5+ siglas* | **\* universal** |
| 15 | Figura integrada lateralmente | #celula #histologia #anatomia | texto curto + figura média |
| 16 | Catálogo de família proteica/molecular | #metabolismo #sinalizacao #receptores | família 3+ membros |
| 17 | Cadência dialogal — enriquecer a prosa com flexibilidade | *qualquer tema, qualquer PARTE* | **\* universal** (leitura leve, sem cota) |
| 18 | Quando quebrar a prosa — tópico, tabela e cálculo | *tema com catálogo de tipos, premissas, ou matemática* | quando a prosa corrida cansa ou perde alinhamento |

**Procedimento de lazy-load (canônico 2026-05-26):**

1. **Sempre leia** categorias 1, 8, 14 (universais) — completas (trecho + "POR QUE É BOM"). **Passe o olho na 17** (cadência dialogal) — não precisa ler completa toda vez; ela é repertório de voz, não receita. Em resumo onde a prosa anterior "soou seca", abrir o trecho-modelo.
2. **Identifique tags do tema** (ex.: tema "Diferenciação Celular" → #celula #genetica).
3. **Leia apenas categorias com tag matching** — completas.
4. **Para QUESTIONADOR:** adicione obrigatoriamente categorias 10, 11, 13 (independente das tags).
5. **Pular** o resto. Se durante a redação você precisar de uma categoria não-prevista, abrir só ela (não o arquivo inteiro).

**Custo médio:** 5–7 categorias por resumo (em vez de 16) → ~7K tokens (em vez de 17K). Economia de ~10K tokens por sessão de redação.

**Heurística do REDATOR:** num resumo típico de PADRÃO/PROFUNDO, espere usar 4–7 categorias. Em SUPERFICIAL, 2–4. Em conflito entre exemplar concreto e regra abstrata, exemplar vence.

---

## Categorias

1. Explicação mecanística parágrafo-por-parágrafo
2. Origem evolutiva / pergunta motivadora
3. Abertura por desfazer confusão comum
4. Magnitudes ancoradas e comparação externa
5. Refinamento histórico de teoria
6. Organização terminológica
7. Analogia construtiva
8. Boxes `.atencao-box` *(2 exemplares — Diferenciação Celular, adicionados 2026-05-26)*
9. Boxes `.clinica-box` *(1 exemplar — Diferenciação Celular DM1+iPS, adicionado 2026-05-26)*
10. Discursivas modelares *(aguardando exemplares)*
11. Distratores mecanísticos para objetivas — notas canônicas 2026-05-14 inseridas *(4 exemplares: Q15 transporte de membrana + Q26/Q27/Q08 de Divisão celular, adicionados 2026-05-26)*
12. Cálculo bem explicado (2 exemplares — Michaelis-Menten + Lineweaver-Burk, a partir de Enzimas I)
13. Texto motivador em questão objetiva — NOVO 2026-05-14 *(1 exemplar)*
14. Glossário de siglas — REESCRITA 2026-05-15 (footnote no rodapé, não mais seção final) *(1 mini-exemplar)*
15. Figura integrada lateralmente — NOVO 2026-05-15 *(1 exemplar: `#figura-lateral`)*
16. Catálogo de família proteica/molecular — parágrafo + tabela — NOVO 2026-05-15 *(1 exemplar: GLUTs)*

---

## CATEGORIA 1 — Explicação mecanística parágrafo-por-parágrafo

### Exemplar 1.1 — Receptores ionotrópicos e PEPS/PIPS

**DE ONDE:** Resumo "Transmissão Sináptica", subtópico 2.3 (Pós-sinapse — PEPS e PIPS).

**TRECHO:**

> O neurotransmissor atravessou a fenda por difusão. Agora ele precisa ser "lido" pela membrana pós-sináptica — e é aqui que a natureza do sinal depende completamente do tipo de receptor encontrado.
>
> Existem duas grandes famílias de receptores. Os **receptores ionotrópicos** são canais iônicos que abrem quando o neurotransmissor se liga — eles *são* o canal. A resposta é rápida (milissegundos) porque não há intermediários. Os **receptores metabotrópicos** são acoplados a proteínas G e ativam cascatas intracelulares que, eventualmente, modulam canais ou enzimas. A resposta é lenta (centenas de milissegundos a segundos), mas permite amplificação. Vamos focar agora nos ionotrópicos, que dominam a comunicação rápida do SNC. Os metabotrópicos voltam no item 3.2.
>
> Um receptor ionotrópico pode produzir dois tipos de resposta pós-sináptica, dependendo de quais íons ele deixa passar. Se abre um canal permeável a Na⁺ (e às vezes K⁺), os íons positivos entram — a célula despolariza — e temos um **potencial excitatório pós-sináptico (PEPS)**. O exemplo canônico é o receptor AMPA do glutamato no SNC: glutamato liga → canal abre → Na⁺ entra e K⁺ sai em menor grau → despolarização de alguns mV. Na junção neuromuscular, o receptor nicotínico de acetilcolina faz o mesmo, mas com uma despolarização tão grande (chega a -70 mV) que sempre ultrapassa o limiar do PA na fibra muscular.
>
> Se, em vez de Na⁺, o canal deixa passar Cl⁻, a resposta é diferente. O Cl⁻ está em concentração maior fora da célula, e o potencial de equilíbrio do Cl⁻ é próximo ou mais negativo que o potencial de repouso. Quando o canal abre, Cl⁻ entra (ou se a célula estava despolarizada, o canal "ancora" o potencial em -70 mV), e o resultado é uma **hiperpolarização** — ou, mais precisamente, uma estabilização em valores mais negativos. Isso é um **potencial inibitório pós-sináptico (PIPS)**. O exemplo clássico é o receptor GABA-A, o principal receptor inibitório do SNC — é um canal iônico, abre com GABA, deixa passar Cl⁻, hiperpolariza.

**POR QUE É BOM:**
- Cada parágrafo tem uma função discreta e encadeada (contexto → famílias → mecanismo do PEPS → mecanismo do PIPS); não há parágrafo "decorativo".
- Define a sigla na primeira aparição entre parênteses: `potencial excitatório pós-sináptico (PEPS)` — operacionaliza a regra do item 4.5 das pendências.
- Apresenta o exemplo canônico em **cadeia mecanística completa** ("glutamato liga → canal abre → Na⁺ entra → despolarização") em vez de só citar o nome do receptor.
---

### Exemplar 1.2 — Sinapse elétrica (estrutura → função)

**DE ONDE:** Resumo "Transmissão Sináptica", subtópico sobre Sinapse Elétrica.

**TRECHO:**

> A sinapse elétrica é a solução mais "direta" possível: ela conecta o citoplasma de dois neurônios através de canais proteicos atravessando as duas membranas lado a lado, sem fenda significativa no meio. Esses canais se chamam **conexons**, formados por seis proteínas conexinas em cada membrana, que se alinham com os seis conexons da célula vizinha e formam um poro contínuo. As membranas ficam a apenas 3,5 nm uma da outra — dez vezes mais perto do que na sinapse química.
>
> Por que isso importa? Porque íons passam diretamente de uma célula para a outra. Se o neurônio pré-sináptico despolariza, as cargas positivas fluem pelo conexon e despolarizam imediatamente o neurônio pós-sináptico. O retardo sináptico é quase zero (cerca de 0,1 ms, praticamente só o tempo de propagação passiva). E como os conexons não têm direção intrínseca, a corrente pode fluir nos dois sentidos — a sinapse elétrica é bidirecional. Esta é a primeira grande diferença para a sinapse química.

**POR QUE É BOM:**
- Movimento clássico **estrutura no primeiro parágrafo, função no segundo** — disciplina pedagógica que evita o erro de despejar tudo junto.
- O segundo parágrafo abre com **pergunta-ponte** ("Por que isso importa?"). Esse movimento força o leitor a fazer ele mesmo a ligação estrutura → função, em vez de receber a conclusão de bandeja.
- Comparação numérica concreta ("dez vezes mais perto do que na sinapse química") ancora o conceito em algo dimensionalmente real — o aluno não decora "3,5 nm", ele entende *o que* 3,5 nm significa relativamente.
---

## CATEGORIA 2 — Origem evolutiva / pergunta motivadora

### Exemplar 2.1 — Por que a evolução fez sinapses químicas (Transmissão Sináptica)

**DE ONDE:** Resumo "Transmissão Sináptica", introdução à PARTE I (Tipos de Sinapse).

**TRECHO:**

> A pergunta fundamental é: por que a evolução não fez simplesmente uma continuidade elétrica direta entre os neurônios, como num fio de cobre? A resposta revela os três grandes serviços que a sinapse presta. Primeiro, **unidirecionalidade**: a informação precisa ter um sentido definido para que circuitos neurais funcionem (o estímulo doloroso precisa ir da pele até o cérebro, não o contrário). Segundo, **amplificação e modulação**: um único neurônio recebe milhares de sinais e precisa integrá-los; se tudo fosse contínuo, não haveria onde essa integração aconteceria. Terceiro, **plasticidade**: a força de uma sinapse pode aumentar ou diminuir ao longo do tempo, e é nisso que se baseia o aprendizado — algo impossível numa conexão elétrica fixa.
>
> Existem duas grandes famílias de sinapse. A sinapse elétrica é rápida, fixa e bidirecional — útil em circunstâncias específicas. A sinapse química é mais lenta (tem um retardo de ~0,5 ms), mas é unidirecional, modulável e plástica — por isso ela domina o sistema nervoso dos mamíferos. Vamos entender cada uma.

**POR QUE É BOM:**
- A pergunta de abertura é **genuína**, não retórica: "por que a evolução não fez X?" — não há resposta óbvia, e a curiosidade do leitor é genuinamente ativada antes de qualquer conteúdo.
- A resposta vem em **três itens numerados, cada um com mecanismo** (não apenas rótulos). "Unidirecionalidade" sozinho seria decoreba; "unidirecionalidade porque circuitos neurais precisam de sentido para funcionar" é mecanismo.
- Cada item termina com uma **consequência hipotética** ("não haveria onde a integração aconteceria"; "impossível numa conexão elétrica fixa") — isso é raciocínio contrafactual, força do pensamento mecanístico.
**Quando usar este padrão:**
- Apenas quando a pergunta "por que isso existe?" tem resposta **didaticamente interessante e mecanística**. Não forçar.
- Funciona em temas com **trade-off evolutivo claro** (sinapse química vs elétrica; mioglobina vs hemoglobina; transporte ativo vs passivo).
- Não usar em temas onde a resposta é "porque sim" ou puramente histórica.

---

## CATEGORIA 3 — Abertura por desfazer confusão comum

### Exemplar 3.1 — "Enzimas não fazem reação acontecer" (Enzimas I)

**DE ONDE:** Apostila "Enzimas I — Marisa Helena", subtópico 1.1 (Por que precisamos de enzimas).

**TRECHO:**

> Antes de qualquer coisa, precisamos desfazer uma confusão comum. Muitas pessoas pensam que «enzima faz reação acontecer». **Isso está errado.** Uma enzima não transforma uma reação impossível em possível — ela só torna uma reação que *já é termodinamicamente favorável* muito mais **rápida**.
>
> Vamos separar duas coisas que frequentemente se misturam na cabeça de quem está começando:
>
> **(1) A espontaneidade** de uma reação é decidida pela variação de energia livre de Gibbs (ΔG). Se ΔG < 0, a reação *pode* ocorrer espontaneamente — ou seja, ela libera energia ao caminhar do reagente para o produto. Se ΔG > 0, ela não ocorre espontaneamente; precisa ser acoplada a outra reação que libere energia. **Enzimas não mudam ΔG.** Uma enzima pega uma reação que já é favorável e acelera, mas não consegue «forçar» uma reação desfavorável.
>
> **(2) A velocidade** de uma reação é controlada por uma barreira energética chamada **energia de ativação** (ΔG‡, lê-se «delta G duplo cruz»). Mesmo uma reação favorável (ΔG < 0) pode ser extremamente lenta se essa barreira for alta.

**POR QUE É BOM:**
- Abre **explicitando o erro mental** antes de construir o certo. Isso é didaticamente superior a "vamos começar definindo X" — engaja a metacognição do leitor ("ah, então eu achava errado").
- O grifo "**Isso está errado.**" não é grosseiro; é honesto. O aluno sabe imediatamente que vai aprender algo contra-intuitivo.
- Constrói a distinção espontaneidade/velocidade **antes de qualquer fórmula**. Quando ΔG e ΔG‡ aparecerem em equações nas próximas seções, o aluno já tem o gesto físico do que cada um significa.
**Quando usar este padrão:**
- Em temas onde há **uma confusão sistemática conhecida** entre alunos iniciantes (enzima como motor mágico; pH como medida apenas de acidez; potencial de membrana como "carga"; etc.).
- Abrir desfazendo a confusão funciona melhor do que "complementar com nota de atenção depois" — pega o aluno antes da concepção errada se cimentar na leitura.

---

## CATEGORIA 4 — Magnitudes ancoradas e comparação externa

### Exemplar 4.1 — Enzimas vs catalisadores industriais (Enzimas I)

**DE ONDE:** Apostila "Enzimas I — Marisa Helena", continuação do subtópico 1.1.

**TRECHO:**

> O truque das enzimas é exatamente esse: elas reduzem a energia de ativação. Não tocam no ΔG total (reagente e produto permanecem nas mesmas alturas no gráfico), mas diminuem a altura do pico intermediário. O resultado é impressionante: **as enzimas aceleram reações em fatores de 10⁶ a 10¹²** em comparação com as reações não catalisadas. A anidrase carbônica, por exemplo, acelera a hidratação do CO₂ por um fator de 10⁷.
>
> Além disso, enzimas têm três características que catalisadores industriais (platina, níquel, ácidos fortes) em geral não têm:
>
> **Condições brandas:** funcionam em temperatura corporal (~37°C), pressão atmosférica e pH próximo ao neutro — o ambiente de uma célula. Um catalisador industrial tipicamente exige centenas de graus e pressões altas.
>
> **Especificidade:** uma enzima reconhece apenas um (ou poucos) substratos, com altíssima precisão — até distingue entre L-aminoácidos e D-aminoácidos (veremos isso em 1.3).
>
> **Capacidade de regulação:** a célula pode ligar e desligar enzimas conforme a necessidade, por mecanismos variados (inibidores, modificação covalente, regulação alostérica).

**POR QUE É BOM:**
- O **range numérico** (10⁶ a 10¹²) vem **antes** do exemplo concreto (anidrase carbônica, 10⁷). O aluno primeiro vê a magnitude do fenômeno, depois ancora num caso real. Essa ordem (magnitude geral → exemplo específico) é mais didática que o inverso.
- O exemplo da anidrase carbônica tem **escolha de propósito**: é uma das enzimas mais rápidas conhecidas e participa de um processo familiar (transporte de CO₂). Não foi escolha aleatória.
- A comparação com **catalisadores industriais** dá ao aluno uma referência externa do mundo dele (química do ensino médio). Sem essa comparação, o leitor não tem como avaliar se 37°C é "muito" ou "pouco" — comparando com "centenas de graus e pressões altas", a baixíssima temperatura biológica vira **insight**.
**Quando usar este padrão:**
- Sempre que um número tem **ordem de magnitude relevante** (10⁶, mM, nM, μs, MPa) que o aluno não tem intuição prévia para avaliar. Ancorar com comparação externa transforma número em sensação.
- Especialmente útil em bioquímica e farmacologia, onde concentrações fisiológicas (mM, μM, nM) variam por ordens de magnitude e mudam significado biológico.

---

## CATEGORIA 5 — Refinamento histórico de teoria

### Exemplar 5.1 — De Fischer (chave-fechadura) a Koshland (encaixe induzido) (Enzimas I)

**DE ONDE:** Apostila "Enzimas I — Marisa Helena", subtópico sobre especificidade enzimática.

**TRECHO:**

> Daniel Koshland refinou a ideia em 1958 com o **modelo do encaixe induzido**: a enzima não é rígida. Quando o substrato se aproxima, ele induz uma pequena mudança conformacional no sítio ativo, que se adapta. **O encaixe perfeito não é com o substrato, e sim com o estado de transição.** Isso é a pedra angular da catálise enzimática: como vimos em 1.1, estabilizar o estado de transição é exatamente o que baixa a energia de ativação.
>
> A especificidade é tão alta que as enzimas distinguem **estereoisômeros**. Como as enzimas são construídas com L-aminoácidos (que são quirais), seus sítios ativos são assimétricos. Por isso, uma enzima que reconhece L-lactato não reconhece D-lactato, mesmo que a única diferença seja a orientação espacial de átomos idênticos. Essa estereoespecificidade é o que permite ao corpo distinguir, por exemplo, glicose de galactose — moléculas com fórmula molecular idêntica (C₆H₁₂O₆) mas configuração espacial diferente.
>
> Apesar disso, nem toda enzima é super seletiva. Algumas são **promíscuas** — aceitam múltiplos substratos parecidos. A quimotripsina é um exemplo: embora sua função principal seja hidrolisar ligações peptídicas em proteínas, ela também hidrolisa ligações éster. Isso tem uma vantagem evolutiva: permite que enzimas sejam «reaproveitadas» para novas reações ao longo da evolução.

**POR QUE É BOM:**
- Apresenta a teoria nova **com a data (1958) e o autor** — ancora o conhecimento como produto humano em evolução, não como verdade caída do céu. Isso constrói atitude científica.
- A **gancho retrospectivo** ("como vimos em 1.1, estabilizar o estado de transição é exatamente o que baixa a energia de ativação") é o que evita que o refinamento histórico vire trivia. O aluno entende **por que esse refinamento importa mecanisticamente**, não só "porque é a teoria atual".
- O exemplo do **L-lactato vs D-lactato** é mecanístico: a estereoespecificidade é justificada pela quiralidade dos aminoácidos da enzima, não declarada como dom. "Sítio ativo assimétrico → não encaixa o enantiômero" é causa-efeito.
**Quando usar este padrão:**
- Em temas onde uma teoria substituiu outra e a substituição **explica algo mecanístico** que a antiga não explicava (Fischer → Koshland; modelo de Bohr → modelo quântico; teoria celular original → endossimbiose mitocondrial).
- Sempre ligando o refinamento a um **insight mecanístico ganho**, nunca só a "agora sabemos mais".

---

## CATEGORIA 6 — Organização terminológica

### Exemplar 6.1 — Cofator / coenzima / grupo prostético / holoenzima / apoenzima (Enzimas I)

**DE ONDE:** Apostila "Enzimas I — Marisa Helena", subtópico 1.4 (Cofatores, coenzimas e grupos prostéticos).

**TRECHO:**

> Muitas enzimas não conseguem trabalhar sozinhas apenas com os 20 aminoácidos padrão — elas precisam de «ajudantes» moleculares. Vamos organizar a terminologia primeiro, porque ela confunde:
>
> **Cofator** é o termo guarda-chuva para qualquer molécula não proteica que a enzima precisa. Divide-se em dois tipos:
>
> **Íons inorgânicos** (metais): Fe²⁺, Mg²⁺, Zn²⁺, Mn²⁺, K⁺, Cu²⁺, Ni²⁺. Exemplos: a anidrase carbônica depende de Zn²⁺, a urease depende de Ni²⁺, as quinases precisam de Mg²⁺ para neutralizar cargas negativas do ATP.
>
> **Coenzimas**: moléculas orgânicas complexas, frequentemente derivadas de vitaminas. Exemplos: NAD⁺/NADH (derivado da vitamina B₃/niacina), FAD/FADH₂ (da B₂/riboflavina), coenzima A (da B₅/ácido pantotênico), piridoxal fosfato (da B₆).
>
> E mais dois termos importantes:
>
> **Grupo prostético** = uma coenzima ou íon metálico que fica **fortemente ligado** (às vezes covalentemente) à proteína, de forma permanente. Exemplo clássico: o grupo heme na hemoglobina e nas citocromos.
>
> **Holoenzima** = a enzima completa, funcional = parte proteica + coenzima/metal. **Apoenzima** = apenas a parte proteica, sem o cofator — geralmente inativa.
>
> Uma propriedade importante das coenzimas é que elas **são quimicamente modificadas durante a reação**. Ao contrário da enzima (que volta ao estado inicial ao final), a coenzima funciona como um co-substrato: ela recebe ou doa átomos/elétrons e precisa ser **regenerada** em outra reação para voltar a ser usada.

**POR QUE É BOM:**
- Abre **avisando que a terminologia confunde** ("organizar a terminologia primeiro, porque ela confunde") — preempta a frustração do aluno antes dela acontecer. Sinaliza honestidade didática.
- Constrói o vocabulário **em hierarquia explícita**: cofator (guarda-chuva) → divide em íons inorgânicos / coenzimas → depois grupo prostético / holoenzima / apoenzima como categorias relacionadas. Sem essa hierarquia, os termos viram lista solta.
- Cada termo vem com **exemplo concreto e mecanístico**, não só definição. "Mg²⁺ para neutralizar cargas negativas do ATP" é causa-efeito; "as quinases precisam de Mg²⁺" sozinho seria decoreba.
**Quando usar este padrão:**
- Quando o tema tem **família de 4+ termos correlatos** que alunos confundem (cofator/coenzima/grupo prostético; ortodromia/antidromia/propagação saltatória; agonista/antagonista/agonista parcial/inverso).
- Construir hierarquia explícita antes de definir os termos individualmente. Definição sem hierarquia vira lista; com hierarquia vira sistema.

---

## CATEGORIA 7 — Analogia construtiva

### Exemplar 7.1 — Lápis dobrado e a ligação ao estado de transição (Enzimas I)

**DE ONDE:** Apostila "Enzimas I — Marisa Helena", subtópico 2.1 (Como as enzimas baixam a energia de ativação).

**TRECHO:**

> Em 1.1, dissemos que enzimas baixam a energia de ativação. Agora vamos entender *como* elas fazem isso, mecanicamente. A pergunta central é: **o sítio ativo é mais complementar ao substrato ou ao estado de transição?**
>
> Imagine que você quer quebrar um lápis ao meio (S → 2 metades P). O lápis intacto é o substrato; o lápis quebrado é o produto; o «lápis dobrado prestes a quebrar» é o estado de transição. Compare duas estratégias hipotéticas para uma enzima-máquina-de-quebrar-lápis:
>
> **Estratégia A (enzima complementar ao substrato):** a máquina tem um encaixe perfeito para o lápis reto. O lápis entra, se acomoda perfeitamente — e nada acontece. Pior: para quebrar, o lápis precisa dobrar; dobrar *tira* o lápis do encaixe perfeito, exigindo energia extra para distorcer a forma. Essa enzima *atrapalharia* a catálise.
>
> **Estratégia B (enzima complementar ao estado de transição):** a máquina tem um encaixe perfeito para o «lápis dobrado». O lápis reto entra meio desconfortavelmente; mas, ao se deformar na direção do estado de transição, encontra cada vez mais interações favoráveis (ligações de hidrogênio, interações eletrostáticas) com a cavidade — o encaixe vai melhorando. Quando chega ao estado de transição, ele está em seu «lar energético». Essa enzima *favorece* a catálise, porque estabiliza — baixa a energia — do estado de transição.
>
> Essa é a ideia central proposta por Linus Pauling em 1946: **as enzimas se ligam com maior afinidade ao estado de transição do que ao substrato**. A energia de ligação «extra» usada para estabilizar o estado de transição é o que, efetivamente, baixa a barreira. Essa é a *ligação preferencial ao estado de transição*.

**POR QUE É BOM:**
- A analogia (lápis) é **autoconsistente**: substrato = lápis reto; estado de transição = lápis dobrado; produto = lápis quebrado. Cada parte da analogia mapeia em uma parte do conceito, e nenhuma parte "sobra" ou "falta". Analogias frouxas confundem; esta é apertada.
- A analogia é usada para **fazer raciocínio contrafactual** ("e se a enzima encaixasse perfeitamente o substrato?") em vez de só ilustrar a conclusão. O aluno **descobre** que a estratégia A não funciona, em vez de receber a estratégia B de bandeja.
- O contraste **estratégia A vs estratégia B** explora a categoria 3 (desfazer confusão) embutida: o aluno provavelmente intuiria "encaixe perfeito do substrato" e descobre que está errado.
**Quando usar este padrão:**
- Quando o tema tem um conceito espacial ou geométrico que precisa de visualização (encaixe, dobra, deformação, fluxo, gradiente).
- A analogia deve **mapear 1-1** em cada elemento conceitual. Se sobrar parte da analogia sem significado biológico (ou vice-versa), ela vai confundir mais do que ajudar.
- Idealmente, a analogia permite raciocínio **contrafactual** ("e se fosse o outro jeito?") — não só ilustração.
- Não usar para conceitos abstratos não espaciais (energia livre, entropia) — para esses, prefira números ou contraste verbal.

---

## CATEGORIA 8 — Boxes `.atencao-box`

**Canônico 2026-05-26:** cota máxima 1–2 `atencao-box` por PARTE (ver redator-e1.md regra 79). Default é prosa explicativa; box é exceção pontual quando a confusão (a) inverte um conceito destruidor de raciocínio ou (b) tem consequência clínica letal. Voz: 2 movimentos no mesmo parágrafo — (1) **a quebra** (onde o aluno derrapa mecanisticamente) seguida de (2) **a correção** (o caminho certo).

### Exemplar 8.1 — Inversão conceitual destruidora (Diferenciação Celular, PARTE I)

**DE ONDE:** Resumo "Diferenciação Celular", subtópico 1.2 (Folhetos embrionários), linha 46.

**TRECHO:**

```typst
#atencao-box("Multipotente não é pluripotente", [O leitor costuma derrapar aqui com uma identificação solta entre os termos. Quem origina os *três* folhetos embrionários (ecto, meso, endoderma) são as células *pluripotentes* — massa celular interna do blastocisto, células-ES, células iPS em cultura. Uma célula *multipotente* já está dentro de uma linhagem só: a #sigla("HSC", [hematopoietic stem cell — célula-tronco hematopoiética, multipotente para a linhagem do sangue]) da medula gera todos os tipos de células do sangue, mas não gera neurônio nem hepatócito. [...] Memorize essa fronteira: *três folhetos é pluripotente; um folheto/linhagem é multipotente*.])
```

**POR QUE É BOM:**
- Movimento canônico de 2 passos: **quebra** ("O leitor costuma derrapar aqui...") + **correção** ("Memorize essa fronteira: três folhetos é pluripotente; um folheto/linhagem é multipotente").
- Quebra a confusão dando o caso concreto (HSC: gera sangue, **não** gera neurônio) antes da regra abstrata — o aluno aprende pelo limite, não pela definição.
- Sigla expandida na 1ª aparição (HSC) com expansão completa — opera a regra 8 do redator-e1.
- Sem vocábulos banidos ("prova", "pegadinha", "cai") — o foco é o mecanismo do erro, não o rótulo de avaliação.

### Exemplar 8.2 — Armadilha técnica com consequência clínica (Diferenciação Celular, PARTE III)

**DE ONDE:** Resumo "Diferenciação Celular", subtópico 3.3 (Epigenética), linha 184.

**TRECHO:**

```typst
#atencao-box("Epigenética NÃO é mudança de DNA", [Esse é provavelmente o ponto mais sensível do tema todo. A palavra "epi" significa "acima" — o que está *acima* do gene, não *dentro* dele. Se uma "herança epigenética" envolvesse mudança de sequência, ela seria, por definição, herança genética. Toda vez que você ler ou ouvir uma descrição que coloca metilação ou marca de histona como "modificação do DNA" no mesmo nível de uma mutação, pare e desmonte: a base nitrogenada continua sendo a mesma; o que mudou foi um grupo químico *adicionado* à base (no caso da metilação de citosina) ou um *grupo adicionado a uma proteína associada* (no caso das modificações de histona). A sequência permanece intacta.])
```

**POR QUE É BOM:**
- Ancora a correção na etimologia ("epi = acima") — dá ao aluno uma ferramenta mnemônica embutida no significado, não decorada.
- Movimento de quebra ("Toda vez que você ler ou ouvir... pare e desmonte") é literalmente uma instrução procedural — o aluno sabe O QUE FAZER quando bate o gatilho do erro.
- Distingue os 2 alvos químicos (base nitrogenada vs proteína associada) sem entrar em jargão excessivo — termo técnico chega DEPOIS do mecanismo.
- Justifica o uso de box (não de prosa): essa confusão é inversão destruidora — se o aluno acha que epigenética muda DNA, todo o capítulo desmorona.

### Quando usar este padrão
- Use quando: (a) a confusão inverte conceito-pilar do subtópico; (b) sem desfazer, o restante do raciocínio fica comprometido; (c) cabe em 1 parágrafo denso.
- Não usar quando: a confusão é "curiosidade" ou tem peso periférico — converta em prosa dialogada com marcador ("a confusão clássica aqui é...").
- Cota: 1–2 boxes por PARTE no máximo. Se a Seção D do Tema Card lista 4+ confusões para uma PARTE, escolha as 2 mais destruidoras e converta as demais em prosa.

---

## CATEGORIA 9 — Boxes `.clinica-box`

**Quando usar:** aplicação clínica direta do mecanismo cuja cadeia causal exige 4–6 linhas para fechar (apresentação → mecanismo → diagnóstico ou conduta). Para clínica colateral à argumentação principal (1–2 frases), preferir **inline entre travessões** (Regra 12 do redator-e1.md). Meta por PARTE: ≥3 clínicas inline + 2–3 box.

### Exemplar 9.1 — Aplicação regenerativa com cadeia mecanística completa (Diferenciação Celular, PARTE III)

**DE ONDE:** Resumo "Diferenciação Celular", subtópico 3.5 (Reprogramação e iPS), linha 246.

**TRECHO:**

```typst
#clinica-box("Tratamento de diabetes tipo 1 com iPS", [O paciente com DM1 perdeu as células-beta produtoras de insulina (destruição autoimune das ilhotas de Langerhans). Estratégia regenerativa: célula somática do paciente → reprogramação por Oct3/4, Sox2, c-Myc, Klf4 → iPS → diferenciação direcionada em endoderma definitivo → progenitor pancreático → célula-beta funcional → transplante. A iPS contorna dois problemas das células-ES: (1) não exige embriões humanos; (2) sendo autóloga, não dispara rejeição. O desafio que sobra: c-Myc é oncogene — protocolos atuais buscam substituir ou eliminar para reduzir risco tumorigênico.])
```

**POR QUE É BOM:**
- Cadeia causal completa em uma única seta encadeada: célula somática → 4 fatores → iPS → endoderma → progenitor → beta → transplante. O aluno reconstrói a estratégia inteira sem esforço.
- A "moral" clínica é dada *contrastando* iPS com ES — duas vantagens numeradas (não-embrionária + autóloga = sem rejeição) que respondem à pergunta "por que esta abordagem e não outra?".
- O desafio remanescente (c-Myc é oncogene) entra no final — calibra a expectativa do aluno: a técnica não é perfeita, ela tem fronteira aberta. Honesta com o estado da ciência.
- Sem floreio: zero adjetivos de venda ("promissora", "revolucionária"), só mecanismo e trade-off.

### Quando usar este padrão
- Use quando a cadeia clínica requer 4+ passos mecanísticos para ser entendida (transplante de iPS, terapia gênica, ressincronização cardíaca, bloqueio enzimático escalonado).
- Não usar quando a aplicação é colateral (1–2 frases): prefira inline entre travessões — ex.: "—a anemia falciforme nasce de uma única troca de glutamato por valina na cadeia β—".
- Cota: 2–3 box por PARTE no máximo. Excesso vira "pular de caixa em caixa" e perde a textura de prosa narrativa.

---

## CATEGORIA 10 — Discursivas modelares

*(Aguardando exemplares concretos — placeholder.)*

---

## CATEGORIA 11 — Distratores mecanísticos para objetivas

**Critério de inclusão:** padrão canônico (2026-05-18) onde a CORRETA é escrita primeiro com tese + mecanismo completo (~25–35 palavras), e cada distratora é construída para caber em 80–120% dela invertendo **um passo mecanístico plausível** — não trocando por "fato curto". Cada distratora deve parecer correta para o aluno que dominou o conceito-pai mas perdeu o conceito-filho específico que ela inverte.

### Padrão consagrado — Q15 transporte de membrana (correta: B)

**Enunciado (motivador + pergunta):** Um paciente com intoxicação grave por monóxido de carbono apresenta hipoxemia sistêmica refratária ao O₂ a 100%. Qual mecanismo molecular explica a hipóxia tecidual neste cenário?

- **(A)** Espessamento da barreira alvéolo-capilar (Δx aumentado) por edema intersticial difuso, reduzindo a difusão de O₂ pela lei de Fick. *[28 palavras]*
- **(B) — CORRETA.** Inibição do transporte sanguíneo de O₂ pela ligação irreversível do CO ao heme da hemoglobina, com prejuízo da entrega tecidual. *[24 palavras]*
- **(C)** Redução da área alveolar funcional pelo colapso de unidades por atelectasia compressiva, com diminuição da troca gasosa total. *[20 palavras]*
- **(D)** Diminuição do gradiente alvéolo-capilar de O₂ pela hipoventilação, com retenção secundária de CO₂ na unidade alveolar. *[19 palavras]*
- **(E)** Bloqueio da cadeia respiratória mitocondrial pela ligação do CO ao citocromo c, impedindo o uso de O₂ pelos tecidos. *[20 palavras]*

**O que cada distratora faz:**
- **A** inverte o local do dano (membrana alvéolo-capilar, não hemoglobina) — testa se o aluno confunde "barreira física" com "transporte sanguíneo".
- **C** inverte o estágio (perda de área alveolar, não captação no eritrócito) — testa se distingue ventilação de transporte.
- **D** inverte o gradiente (hipoventilação clássica) — clássico distrator de fisiologia respiratória; testa se o aluno isola o efeito do CO.
- **E** é o distrator mais sutil: o CO **realmente** se liga ao citocromo c (efeito secundário, dose alta), mas o mecanismo dominante na intoxicação aguda é a carboxiemoglobina. Testa se o aluno reconhece o mecanismo **principal** vs. acessório.

**Por que esse padrão funciona:** todas as distratoras descrevem mecanismos **reais** que causam hipóxia em outros cenários. O aluno que decora "CO é tóxico" marca qualquer uma; o aluno que entende o mecanismo escolhe B. Distratoras "fato curto" como *"Diminuição da área alveolar funcional."* não exercitam discriminação mecanística — quebram a paridade visual e entregam a resposta.

### Contraste rápido — o que NÃO fazer

Mesma questão, distratoras estilo antigo (encurtadas para caber na correta encurtada):
- (A) Edema alveolar. *(4 palavras)*
- (B) CO se liga à hemoglobina. *(6 palavras)*
- (C) Atelectasia. *(1 palavra)*

Aqui a B é visualmente óbvia: única alternativa "completa". Aluno marca por forma, não por conteúdo. Além disso, perde-se a oportunidade didática de cada distratora ensinar **por que aquele outro mecanismo não se aplica aqui**.

### Exemplar 11.2 — Aplicação clínica/oncológica com supressores tumorais intactos (Divisão celular, Q26)

**DE ONDE:** `resumos-gerados/BIOCEL-07-DIVISAO-CELULAR.pdf`, Etapa 2, Q26. Geração 2026-05-26. Calibração de paridade: ratio correta/maior_distratora = **0,96** (alvo ≤ 1,25).

**Enunciado:** Uma paciente de 32 anos é diagnosticada com câncer cervical invasor. A biópsia confirma infecção por HPV-16. Análise molecular mostra p53 e Rb com sequências de DNA *normais* (não-mutados). Como o tumor se desenvolveu com supressores intactos?

- **(A)** Amplificação gênica de Myc e Ras, ativando vias mitogênicas que sobrepujaram a função supressora intacta de p53 e Rb na proliferação descontrolada do epitélio cervical infectado, com via Rb-E2F preservada apenas no DNA mas funcionalmente neutralizada pelo excesso mitogênico crônico exógeno. *[47 palavras]*
- **(B)** A presença de HPV-16 indica que o tumor é benigno por definição — o câncer descrito provavelmente tem outra origem etiológica não relacionada ao vírus, possivelmente alterações estruturais cromossômicas não detectadas na análise convencional, sendo HPV apenas marcador epidemiológico sem papel causal na cervicogênese tumoral observada. *[46 palavras]*
- **(C)** Infecção crônica por HPV gerou inflamação local que ativou diretamente E2F via NFκB independente de Rb, contornando a supressão tumoral preservada — mecanismo predominante em cânceres associados a inflamação persistente, em que citocinas pró-inflamatórias drivam proliferação descontrolada apesar de supressores tumorais intactos no DNA. *[45 palavras]*
- **(D) — CORRETA.** HPV-16 expressa E6 e E7, que se ligam respectivamente a p53 (recrutando E6AP para ubiquitinar) e Rb (induzindo degradação proteassomal), inativando as proteínas funcionalmente. Os genes selvagens são transcritos normalmente, mas as proteínas são degradadas pelo proteassoma — daí supressão funcional sem mutação no DNA. *[45 palavras]*
- **(E)** HPV-16 induziu metilação dos promotores de p53 e Rb, silenciando a transcrição sem alterar a sequência do DNA — a análise por sequenciamento não detecta esse mecanismo epigenético, dando aparência enganosa de gene íntegro apesar de proteína indetectável funcional em ensaios bioquímicos modernos. *[43 palavras]*

**O que cada distratora faz:**
- **A** inverte o nível da lesão (oncogenes ativados em vez de supressores inativados) — testa se o aluno entende que "DNA selvagem" significa que a inativação está no nível proteico, não no genoma.
- **B** é a *armadilha tipográfica*: parece teste de leitura ("HPV está aqui, será que importa?"). Inverte o vetor causal — aluno que não sabe o mecanismo molecular vai duvidar do enunciado.
- **C** é o distrator mais sutil: a inflamação crônica realmente importa em alguns cânceres (Hp+gástrico, hepatite+HCC), mas no HPV o mecanismo dominante é molecular direto. Testa se o aluno sabe *qual* mecanismo é central neste tumor específico.
- **E** é o distrator "epigenética genérica" — silenciamento por metilação é real em vários supressores, mas no HPV não é o mecanismo descrito. Testa se o aluno sabe que E6/E7 fazem degradação proteica, não regulação transcricional.

**Por que esse padrão funciona:** todas as distratoras são mecanismos *reais de carcinogênese* em outros contextos. O aluno que decora "HPV causa câncer cervical" marca qualquer uma; o aluno que entende E6→p53/E6AP e E7→Rb/proteassoma escolhe D. A paridade visual (43–47 palavras) impede que o aluno acerte por exclusão de tamanho.

### Exemplar 11.3 — Aplicação farmacológica com via molecular precisa (Divisão celular, Q27)

**DE ONDE:** Mesmo resumo, Q27. Calibração de paridade: ratio = **0,90** (correta A com 43 palavras; maior distratora B com 48).

**Enunciado:** Paciente de 65 anos com LLC, refratário à fludarabina, com TP53 mutado biálico e BCL-2 superexpressa. O hematologista inicia venetoclax. Racionalidade molecular?

- **(A) — CORRETA.** Venetoclax inibe BCL-2 diretamente, liberando Bax/Bak previamente sequestrados; estes permeabilizam a mitocôndria, liberam citocromo c, que com Apaf-1 ativa caspase 9 → caspase 3 → apoptose. A via mitocondrial é independente de p53, daí a eficácia mesmo em tumores p53-mutados como esta LLC. *[43 palavras]*
- **(B)** Venetoclax restaura a função de p53 mutado por ligação alostérica direta a um sítio críptico da proteína, recuperando o programa apoptótico clássico p53-dependente em células leucêmicas que haviam perdido essa via essencial pela mutação bialélica, mecanismo análogo ao do APR-246 em ensaios. *[42 palavras]*
- **(C)** Venetoclax inibe a topoisomerase II como a fludarabina, gerando quebras de dupla fita que ativam ATM → p53 → apoptose; a maior afinidade pelo alvo justifica a eficácia mesmo em mutantes p53 parciais clínicos por amplificação do sinal genotóxico, contornando o limiar de detecção ATM/ATR em células LLC. *[48 palavras]*
- **(D)** Venetoclax bloqueia BCL-2 por mecanismo competitivo no sítio de ligação ao DNA do BCL-2, impedindo sua função como fator de transcrição nuclear e levando à parada do ciclo em G1 nas células leucêmicas linfoides ativas, por inibição secundária da transcrição de ciclina D e ciclina E. *[46 palavras]*
- **(E)** Venetoclax ativa diretamente caspase 3 por ligação alostérica em sítio críptico da pró-caspase, contornando toda a sinalização montante mitocondrial e p53-dependente em mecanismo único entre drogas oncológicas modernas, sendo eficaz especificamente em leucemias linfoides crônicas com BCL-2 elevado. *[38 palavras]*

**O que cada distratora faz:**
- **B** inverte o alvo molecular (p53 em vez de BCL-2) — mas chega na mesma destino apoptótico. Testa se o aluno conhece o *alvo* específico do venetoclax.
- **C** confunde com a outra droga do caso (fludarabina, análogo de purina, mecanismo genotóxico) — testa se o aluno separou os dois fármacos quando leu o enunciado.
- **D** inverte a *função* do BCL-2 (fator de transcrição em vez de proteína anti-apoptótica) — armadilha do aluno que viu "BCL-2" e supôs ser regulador transcricional.
- **E** pula a montante e ativa caspase 3 diretamente — mecanismo *quase* certo (apoptose final, sim) mas com via errada. Testa se o aluno entende a hierarquia mitocôndria → caspase 9 → caspase 3.

**Por que esse padrão funciona:** o caso traz **duas drogas** (fludarabina e venetoclax) e **duas vias** (genotóxica p53-dependente e mitocondrial p53-independente). Distratoras são cruzamentos plausíveis dessas combinações. Aluno que decorou nome de droga sem mecanismo erra; aluno que entende a *lógica do resgate* (precisa contornar p53) escolhe A.

### Exemplar 11.4 — Consolidação com inversão mecanística sutil (Divisão celular, Q08)

**DE ONDE:** Mesmo resumo, Q08 Consolidação (gatilho da anáfase). Mostra que mesmo em Consolidação dá para usar inversão mecanística quando há ≥2 mecanismos candidatos plausíveis.

**Enunciado:** Sobre a anáfase e os mecanismos que disparam a separação das cromátides-irmãs:

- **(A)** A anáfase é disparada pela aplicação progressiva de mais força mecânica pelos microtúbulos do cinetócoro, que vencem a resistência das coesinas por puro acúmulo de tensão contrátil.
- **(B)** A separação das cromátides depende da síntese de uma nova proteína (separase) durante a metáfase em resposta a sinais do checkpoint do fuso liberado pelo alinhamento metafásico completo.
- **(C)** Coesinas são clivadas espontaneamente quando atingem certa idade na célula, em mecanismo independente de proteases ou ligases regulatórias — apenas degradação por hidrólise lenta natural.
- **(D) — CORRETA.** APC/C ativo ubiquitina securina (inibidora da separase) e ciclina B; com securina destruída, separase fica livre e cliva a coesina, separando cromátides — gatilho químico, não mecânico.
- **(E)** A anáfase só ocorre quando o M-CDK atinge concentração máxima, fosforilando diretamente a coesina e desestabilizando-a por modificação pós-traducional sem necessidade de proteólise.

**O que cada distratora faz:**
- **A** é a inversão central do tema (mecânico vs químico) — testa o nó conceitual do assunto. Aluno que pensa "microtúbulos puxam mais forte" cai aqui; aluno que entende "tensão já estava aplicada, faltava liberar" rejeita.
- **B** inverte o *timing* da separase (síntese nova vs liberação de uma já existente) — testa se aluno sabe que separase já está lá, sequestrada por securina.
- **C** é o distrator nonsense — útil porque elimina o aluno que chuta. Coesinas não se degradam sozinhas.
- **E** é o distrator de "máximo ativador" — aluno acha que tudo na mitose é M-CDK, mas a anáfase é o ponto onde M-CDK *desliga* (ciclina B destruída).

**Por que esse padrão funciona:** mesmo sendo Consolidação, a distratora A é uma **inversão conceitual destruidora** — testa se o aluno aprendeu que a anáfase é química. Sem essa inversão, a questão vira "qual é a definição de anáfase" e perde a oportunidade didática. O padrão "inversão mecanística" cabe em qualquer nível quando há nó conceitual.

**Quando usar este padrão:**
- Sempre que houver ≥2 mecanismos candidatos que o aluno poderia razoavelmente confundir.
- Especialmente em questões de Integração e Aplicação, onde discriminar mecanismo é o ponto.
- Em Consolidação simples (definição direta), o padrão pode pesar — aceitar correta mais curta + distratoras na faixa, sem forçar inversão se a questão não pede.

---

## CATEGORIA 12 — Cálculo bem explicado

**Critério de inclusão:** trechos com cálculo onde cada passo da matemática vem acompanhado de **interpretação física/biológica** do que aquele passo significa, em vez de só "aplicamos a fórmula e obtemos X". A regra inegociável: nunca apresentar desenvolvimento matemático sem explicar o raciocínio por trás de cada passo. Fórmula obrigatoriamente em bloco `.formula-box` com três peças (fórmula isolada, legenda com gesto físico, exemplo numérico contextualizado).

### Exemplar 12.1 — Equação de Michaelis-Menten com derivação narrada e gesto físico de Km

**DE ONDE:** Reescrita didática a partir de Enzimas I — Marisa Helena, p. 15-16, subtópico 3.1 (modelo de Michaelis-Menten). Diagnóstico identificou padrões (a), (b), (c), (d), (e), (f) na versão original.

**TRECHO:**

> Já temos o modelo cinético: `E + S ⇌ ES → E + P`. Agora queremos uma fórmula que diga, dados um substrato em concentração [S] e uma quantidade total de enzima, qual será a velocidade da reação. Michaelis e Menten resolveram isso em 1913 com uma hipótese inteligente: **logo após o início da reação, a concentração do complexo ES estabiliza em um regime estacionário** — ou seja, ES se forma e se desfaz na mesma taxa, e [ES] passa a ser aproximadamente constante.
>
> Por que essa hipótese? Porque, em regime estacionário, podemos escrever uma equação simples:
>
> ```html
> <div class="formula-box">
>   <p class="formula">k<sub>1</sub>[E][S] = (k<sub>−1</sub> + k<sub>2</sub>)[ES]</p>
>   <div class="formula-legenda">
>     <p><strong>lado esquerdo</strong> — taxa com que ES <em>se forma</em> (E e S se encontram e ligam, com constante k<sub>1</sub>).</p>
>     <p><strong>lado direito</strong> — taxa com que ES <em>se desfaz</em>, seja voltando a E + S (k<sub>−1</sub>), seja avançando para E + P (k<sub>2</sub>).</p>
>   </div>
> </div>
> ```
>
> Esta equação é o pivô da derivação. Vamos isolar [ES], porque é ele que controla a velocidade da reação (a reação anda na taxa k₂·[ES] — só quem está no complexo está reagindo). Dividindo ambos os lados por (k<sub>−1</sub> + k<sub>2</sub>) e lembrando que `[E] = [E]total − [ES]` (a enzima ou está livre, ou está em complexo), depois de mais algumas manipulações chega-se a:
>
> ```html
> <div class="formula-box">
>   <p class="formula">v<sub>0</sub> = V<sub>max</sub> · [S] / (K<sub>M</sub> + [S])</p>
>   <div class="formula-legenda">
>     <p><strong>v<sub>0</sub></strong> — velocidade inicial da reação (µM/s). É o que se mede em laboratório, antes que o produto se acumule e atrapalhe.</p>
>     <p><strong>V<sub>max</sub></strong> — velocidade máxima (µM/s). Gesto físico: a velocidade que se observa quando toda enzima está, instante a instante, ocupada com substrato. É um teto, não um valor "comum".</p>
>     <p><strong>[S]</strong> — concentração de substrato (mM). É a variável que o experimentador controla.</p>
>     <p><strong>K<sub>M</sub></strong> — constante de Michaelis (mM). Gesto físico duplo: (1) é a [S] que faz a enzima trabalhar a meia força (v<sub>0</sub> = V<sub>max</sub>/2); (2) algebricamente, K<sub>M</sub> = (k<sub>−1</sub> + k<sub>2</sub>)/k<sub>1</sub> — uma razão entre quem "tira" o substrato do complexo (numerador) e quem o "põe" (denominador). Por isso K<sub>M</sub> baixo significa alta afinidade: o substrato custa pouco para ser retido.</p>
>   </div>
>   <div class="formula-exemplo">
>     <strong>Exemplo:</strong> a hexoquinase do cérebro tem K<sub>M</sub> ≈ 0,05 mM para glicose. A glicemia normal em jejum é ~5 mM, ou seja, [S] é cerca de 100× maior que K<sub>M</sub>. Substituindo: v<sub>0</sub> = V<sub>max</sub> · 5 / (0,05 + 5) ≈ V<sub>max</sub> · 0,99. **O cérebro opera a 99% de V<sub>max</sub> mesmo em jejum prolongado.** Por isso a hexoquinase é a enzima certa para um tecido que não pode parar.
>   </div>
> </div>
> ```
>
> Olhe a equação como uma máquina. Quando [S] é muito menor que K<sub>M</sub>, o denominador é dominado por K<sub>M</sub>, e a fórmula vira `v ≈ (V<sub>max</sub>/K<sub>M</sub>)·[S]` — linear em [S]. Quando [S] é muito maior que K<sub>M</sub>, o denominador é dominado por [S], e a fórmula vira `v ≈ V<sub>max</sub>·[S]/[S] = V<sub>max</sub>` — platô. Os dois regimes da curva (linear em baixas [S], platô em altas [S]) não são fatos observados que precisam decorar; **são consequência inevitável da estrutura algébrica da fórmula**.

**POR QUE É BOM:**
- **Abre com pergunta-ponte explícita** ("queremos uma fórmula que diga…") antes da derivação aparecer — o aluno sabe para onde a matemática está indo antes de embarcar.
- **A hipótese do estado estacionário é justificada mecanisticamente** ("ES se forma e se desfaz na mesma taxa, e [ES] passa a ser aproximadamente constante") em vez de ser apresentada como condição arbitrária.
- **A equação intermediária `k₁[E][S] = (k₋₁+k₂)[ES]` ganha seu próprio `.formula-box`** com legenda que nomeia o que cada lado representa fisicamente ("taxa com que ES se forma" / "taxa com que ES se desfaz"). Não é fórmula muda.
**Quando usar este padrão:**
- Sempre que uma fórmula tem **derivação curta mas conceitualmente importante** (Michaelis-Menten, Henderson-Hasselbalch, equação de Nernst). A derivação deve ser narrada *no resumo*, não terceirizada para slide ou livro-texto.
- Quando a variável da fórmula tem **gesto físico duplo** (definição operacional + interpretação mecanística), a legenda deve trazer os dois explicitamente, ligados por um traço claro: "(1) operacional: …; (2) mecanístico: …".
- A análise dos limites (`[S] << K<sub>M</sub>` vs `[S] >> K<sub>M</sub>`) deve fechar a explicação **sempre que a fórmula tem assíntotas ou regimes** — converte memorização de comportamento em consequência algébrica.
- **Não usar este padrão para fórmulas puramente definicionais** (ex: pH = −log[H⁺]) — para essas, o `.formula-box` simples sem derivação basta.

---

### Exemplar 12.2 — Linearização de Lineweaver-Burk com álgebra falada

**DE ONDE:** Reescrita didática a partir de Enzimas I — Marisa Helena, p. 18, subtópico 3.3 (Lineweaver-Burk). Diagnóstico identificou padrões (a), (b), (f), (h) na versão original — derivação algébrica completamente muda ("tomar o inverso dos dois lados — você obtém"), com 3 passos algébricos pulados.

**TRECHO:**

> Determinar V<sub>max</sub> diretamente do gráfico v<sub>0</sub> × [S] tem um problema prático. V<sub>max</sub> é uma **assíntota** — você só a atinge se conseguir manter a enzima saturada com [S] tendendo ao infinito. Na bancada isso é impossível, e a olho nu não dá para saber se a curva já chegou no platô ou se ainda vai subir um pouquinho. A solução de Lineweaver e Burk (1934) é elegante: **converter a hipérbole em uma reta**. Reta tem só dois parâmetros — inclinação e intercepto — e ambos se leem direto do gráfico.
>
> O truque é inverter os dois lados da equação de Michaelis-Menten. Vamos fazer isso devagar, porque cada passo importa:
>
> ```html
> <div class="formula-box">
>   <p class="formula">1/v<sub>0</sub> = (K<sub>M</sub> + [S]) / (V<sub>max</sub> · [S])</p>
>   <div class="formula-legenda">
>     <p><strong>Passo 1.</strong> Invertendo `v<sub>0</sub> = V<sub>max</sub>·[S]/(K<sub>M</sub>+[S])` lado a lado: o que estava no numerador foi pro denominador e vice-versa. Nada de novo ainda — só é a mesma equação escrita de cabeça pra baixo.</p>
>   </div>
> </div>
> ```
>
> Agora separamos o numerador em dois pedaços, porque uma soma sobre um denominador pode virar duas frações somadas:
>
> ```html
> <div class="formula-box">
>   <p class="formula">1/v<sub>0</sub> = K<sub>M</sub>/(V<sub>max</sub>·[S]) + [S]/(V<sub>max</sub>·[S])</p>
>   <div class="formula-legenda">
>     <p><strong>Passo 2.</strong> Cada termo do numerador (K<sub>M</sub> e [S]) ganhou sua própria fração. No segundo termo, [S] aparece no numerador e no denominador — vai se cancelar no próximo passo.</p>
>   </div>
> </div>
>
> <div class="formula-box">
>   <p class="formula">1/v<sub>0</sub> = (K<sub>M</sub>/V<sub>max</sub>) · (1/[S]) + 1/V<sub>max</sub></p>
>   <div class="formula-legenda">
>     <p><strong>1/v<sub>0</sub></strong> — eixo Y do novo gráfico (s/µM). Gesto físico: tempo médio para a enzima processar uma quantidade fixa de substrato.</p>
>     <p><strong>1/[S]</strong> — eixo X do novo gráfico (1/mM). Gesto físico: quanto maior 1/[S], mais "escasso" está o substrato.</p>
>     <p><strong>K<sub>M</sub>/V<sub>max</sub></strong> — inclinação da reta. Combina os dois parâmetros cinéticos num só número.</p>
>     <p><strong>1/V<sub>max</sub></strong> — intercepto Y. Gesto físico: o valor que a reta toca quando 1/[S] = 0, ou seja, quando [S] → ∞ — substrato hipoteticamente infinito. **Saturar a enzima virou extrapolação geométrica, não experimento impossível.**</p>
>   </div>
>   <div class="formula-exemplo">
>     <strong>Exemplo:</strong> num experimento com a fosfatase alcalina, você mede v<sub>0</sub> em cinco [S] diferentes, calcula 1/v<sub>0</sub> e 1/[S] para cada ponto, e plota. Se a reta passar por 0,02 s/µM no eixo Y (quando 1/[S] = 0), então V<sub>max</sub> = 1/0,02 = 50 µM/s. Se ela cruzar o eixo X em −10 mM⁻¹, então K<sub>M</sub> = −1/(−10) = 0,1 mM. **Você extraiu os dois parâmetros sem nunca ter saturado a enzima.** Esse é o ganho prático da linearização.
>   </div>
> </div>
> ```
>
> Agora a leitura geométrica do gráfico ganha sentido mecanístico. Quando um inibidor competitivo é adicionado, ele **rouba o sítio ativo do substrato**, mas pode ser deslocado por excesso de [S]. Portanto, no limite [S] → ∞ (intercepto Y), o inibidor é vencido, e V<sub>max</sub> não muda — as duas retas (com e sem inibidor) cruzam no eixo Y. Quando o inibidor é não-competitivo, ele liga em outro sítio e **estraga uma fração das enzimas** mesmo em [S] alto; V<sub>max</sub> cai (o intercepto Y sobe, porque 1/V<sub>max</sub> aumenta) — mas as enzimas que sobraram funcionando têm afinidade normal, então K<sub>M</sub> não muda (o intercepto X fica no mesmo lugar). A leitura do gráfico **é** a leitura do mecanismo.

**POR QUE É BOM:**
- **Cada passo algébrico ganha seu próprio `.formula-box` numerado** — a derivação `(K<sub>M</sub>+[S])/(V<sub>max</sub>·[S]) → K<sub>M</sub>/(V<sub>max</sub>·[S]) + [S]/(V<sub>max</sub>·[S]) → (K<sub>M</sub>/V<sub>max</sub>)·(1/[S]) + 1/V<sub>max</sub>` não é pulada; cada manipulação é exibida e nomeada ("agora separamos o numerador em dois pedaços, porque uma soma sobre um denominador pode virar duas frações somadas").
- **A frase "vamos fazer isso devagar, porque cada passo importa"** sinaliza explicitamente que o resumo é o lugar da derivação — diretamente oposto ao "revise nos slides 49-52" da apostila original.
- **O intercepto Y é explicado pelo gesto físico do limite matemático** (`1/[S] = 0 ⇔ [S] → ∞`), e a consequência didática é nomeada: "saturar a enzima virou extrapolação geométrica, não experimento impossível". O aluno entende **por que a linearização vale a pena**, não só *o que* ela faz.
**Quando usar este padrão:**
- Para qualquer **derivação algébrica curta (3-5 passos) com utilidade prática**: Lineweaver-Burk, Henderson-Hasselbalch (ácido-base), equação de Nernst (potencial de equilíbrio), Hill (cooperatividade).
- Quando o gráfico resultante da fórmula **tem leitura mecanística** (interceptos, inclinações com significado físico), tratar a leitura do gráfico como **consequência** do mecanismo, não como conjunto de regras decoradas.
- **Não usar este padrão para derivações longas** (>6 passos) — para essas, ou se reorganiza o conteúdo em partes ou se cita um livro-texto explicitamente como referência complementar. NEBLI não é livro de cálculo; é resumo didático.
- **Não usar para fórmulas onde a álgebra é trivial** (ex.: kcat = Vmax/[E]total — divisão simples não merece três boxes; um único `.formula-box` com legenda + exemplo basta).

---

---

## CATEGORIA 13 — Texto motivador em questão objetiva (NOVO 2026-05-14)

**Propósito:** mostrar que o texto motivador não é exclusivo de questões clínicas — qualquer categoria (Consolidação, Integração, Aplicação) pode ter uma vinheta curta que ancora o mecanismo antes da pergunta. Rejeita o padrão "decoreba descontextualizado".

### Exemplar 13.1 — Integração com motivador experimental (modelo construído)

**DE ONDE:** Exemplo construído para demonstrar o padrão. Tema fictício: glicólise.

**TRECHO (corpo da questão como ficaria no Typst):**

> *Em um experimento clássico, eritrócitos humanos foram incubados em solução com glicose marcada (¹⁴C-glicose). Após 30 minutos, detectou-se acúmulo de ¹⁴C-lactato e queda progressiva do pH intracelular. Nenhuma outra fonte de carbono estava disponível.*
>
> **A queda de pH observada é consequência direta de qual evento metabólico?**
>
> A) Hidrólise de ATP pela hexoquinase, que libera H⁺ ao fosforilar a glicose.
> B) Produção de lactato pela LDH, acompanhada de liberação de H⁺ pela dissociação do ácido lático.
> C) Consumo de NAD⁺ na gliceraldeído-3-fosfato desidrogenase, que acidifica o meio ao oxidar o substrato.
> D) Acúmulo de piruvato, que é ácido fraco e reduz o pH ao se ionizar.
> E) Entrada de glicose pelo GLUT-1, antiporte com H⁺, que aumenta [H⁺] intracelular.

**POR QUE É BOM:**
- A vinheta experimental (eritrócito + glicose marcada) ancora a questão num contexto real sem exigir propedêutica clínica — o aluno de 1º semestre consegue visualizar o experimento.
- O motivador já entrega o dado essencial (queda de pH + acúmulo de lactato) sem revelar o gabarito — reduz o peso cognitivo sem eliminar o raciocínio.
- Os distratores são inversões mecanísticas plausíveis: A troca o mecanismo (hexoquinase libera H⁺?), C confunde a oxidação de NADH com acidificação, D acerta o substrato mas erra o mecanismo de acidificação, E inventa antiporte inexistente.
**Quando usar este padrão:**
- Em qualquer categoria quando a pergunta sem contexto vira "qual substância faz X?" puro. O motivador transforma em "dado este cenário, o que explica Y?".
- Especialmente útil em Integração: duas vias se cruzam, o motivador sinaliza qual ponto de cruzamento explorar.
- Vinheta deve ser curta (2–4 linhas). Se crescer mais, provavelmente está carregando conteúdo que deveria estar no enunciado principal.

---

## CATEGORIA 14 — Glossário de siglas (REESCRITA 2026-05-15)

**Propósito:** mostrar como o helper `#sigla(...)` funciona no texto. Canônico desde 2026-05-15: **glossário não existe mais como seção final do PDF — vive como footnote no rodapé de cada página**, gerada automaticamente na 1ª aparição de cada sigla. O modelo anterior (registry + seção dedicada no fim) foi descontinuado em 05-15 porque obrigava o aluno a folhear N páginas para tirar dúvida sobre uma sigla; footnote na própria página resolve no olho, sem perder o fio do raciocínio.

### Exemplar 14.1 — Uso inline do helper e comportamento da footnote

**DE ONDE:** Exemplo construído; helper `#sigla` reescrito em 2026-05-15 (helper antigo `#glossario-siglas-page()` virou no-op silencioso, preservado só para compat de resumos legacy).

**No corpo da Etapa 1 (Typst) — assinatura canônica:**

```typst
A #sigla("ATP", [adenosina trifosfato — moeda energética da célula]) é produzida
na membrana mitocondrial interna por uma máquina molecular chamada ATP sintase.
Mais à frente, quando voltarmos a falar de ATP, o helper não precisa ser
chamado de novo: o state interno do template já sabe que ATP estreou.
```

> **Atenção à assinatura:** a abreviação vai como **string entre aspas** (`"ATP"`), e a expansão vai como **content entre colchetes** (`[adenosina trifosfato — …]`). Forma errada — `#sigla[ATP][adenosina trifosfato]` — compila silenciosamente em alguns contextos mas quebra o registry de "siglas vistas". Use a forma canônica string-content sempre.

**Saída esperada na 1ª aparição:** `"ATP¹"` no texto + footnote `¹ **ATP** — adenosina trifosfato — moeda energética da célula` no rodapé daquela página.

**Saída esperada nas aparições subsequentes:** só `"ATP"` em texto plano, sem decoração nem footnote nova. O state interno (`_siglas-vistas`) garante que cada sigla emite no máximo uma footnote por documento.

**Política de cobertura — quando expandir em-linha + chamar `#sigla(...)`, e quando só chamar `#sigla(...)`:**
- Se entender a sigla é pré-requisito do parágrafo (ex.: o raciocínio depende de o aluno saber o que é ATP nesse exato momento), expandir em-linha *e* ainda chamar `#sigla(...)`. A footnote vira reforço, não única fonte.
- Se a sigla é rótulo conhecido ou auto-explicativo no contexto (ex.: "a NADH desidrogenase recebe elétrons do NADH"), só `#sigla(...)`. A footnote no rodapé cobre, sem interromper o ritmo do diálogo.
- Sem teto: resumo de bioquímica mitocondrial pode ter 25+ siglas; todas viram footnote na 1ª aparição.

**Diferença operacional vs `#termo-nota`:**
- `#sigla(...)` = abreviação/acrônimo (ATP, NADH, JNM, RyR, GLUT-4). Sem teto. Sempre na 1ª aparição.
- `#termo-nota[...][...]` = termo técnico denso (acetilcolina, thiohemiacetal, plasmalema). 5–10 por resumo. Sempre na 1ª aparição.
- Os dois usam o mesmo mecanismo Typst (footnote no rodapé), mas têm helpers separados por clareza editorial.

**Quando usar:**
- Todo resumo a partir de 2026-05-15. Sem exceção.
- Resumo novo **NÃO** deve chamar `#glossario-siglas-page()` — esse helper existe só como no-op silencioso para compat de resumos antigos.

---

## CATEGORIA 15 — Figura integrada lateralmente

**Propósito:** mostrar como usar o helper `#figura-lateral` introduzido em 2026-05-15 para resolver o sintoma clássico de "figura grande + parágrafo curto + 40% da página em branco". O helper coloca figura à direita (ou esquerda) com o texto fluindo ao lado num grid de 2 colunas — reduz drasticamente o espaço vazio quando o parágrafo que fala da figura é curto-médio.

### Exemplar 15.1 — Figura lateral à direita com texto fluindo ao lado

**DE ONDE:** Exemplo construído com tema fictício (estrutura do ATP). Será substituído pelo primeiro caso real da Geração 20 onde uma figura curta couber bem como lateral.

**Sintaxe Typst canônica:**

```typst
#figura-lateral(
  "figuras/atp/estrutura-base.png",
  legenda: [Repare como os três fosfatos terminais concentram carga
    negativa na região γ — é justamente nessa ligação que a hidrólise
    libera ~7,3 kcal/mol em condições padrão.],
  texto: [A molécula de ATP é composta por três partes encadeadas: a base
    nitrogenada (adenina), o açúcar de cinco carbonos (ribose) e a cauda
    de três fosfatos (α, β, γ). O que dá ao ATP sua função de "moeda
    energética" não é o número absoluto de fosfatos, mas a *geometria de
    cargas* na cauda fosfatada. Os três grupos fosfato carregam cargas
    negativas que se repelem mutuamente — uma molécula de ATP em solução
    está, em certo sentido, sob tensão eletrostática constante. Hidrolisar
    a ligação γ alivia parcialmente essa tensão, e essa diferença de
    estabilidade é o que aparece como energia liberada.],
  lado: "right",
  largura-figura: 38%,
)
```

**POR QUE É BOM:**
- O parágrafo de ~95 palavras "casa" com a altura da figura em ~38% da largura útil — o grid termina com texto e figura aproximadamente alinhados na base, sem desperdício visual.
- A legenda direciona o olhar ("repare como os três fosfatos terminais concentram carga negativa"), não descreve a figura passivamente — coerente com a regra de legenda do REDATOR-E1.
- O `lado: "right"` joga a figura à direita, que é a posição de leitura natural em scripts da esquerda-pra-direita (olho lê texto, encontra a figura como "evidência" do que acabou de ler).
**Quando usar este padrão:**
- Quando o parágrafo que fala da figura é **curto-médio** (60–110 palavras) e a figura é **pequena-média** (não é uma micrografia complexa, não é uma estrutura anatômica detalhada). Para figuras grandes e complexas, manter `#figura-nebli` com `largura: 85%` centralizada.
- Quando o texto da explicação **referencia a figura no meio do raciocínio**, não só ao final ("ver figura X"). Esse padrão de leitura entrelaçada é o que justifica o grid lateral.
- O texto passado precisa "casar" com a altura da figura. Se texto < figura, sobra branco abaixo do texto; se texto > figura, o restante continua abaixo do grid (não é erro — só lembrar que o grid não estica o texto).
- Alternar lados (`"right"` e `"left"`) entre figuras consecutivas dá ritmo visual à página — não usar sempre o mesmo lado em sequência.

**Quando NÃO usar:**
- Parágrafo muito curto (<50 palavras) que vai sobrar branco mesmo com `largura-figura: 30%` — prefira `#figura-nebli` pequena centralizada.
- Parágrafo muito longo (>140 palavras) que vai vazar abaixo do grid e gerar "ilha" visual estranha — deixe a figura centralizada e siga com o parágrafo embaixo.
- Figura que precisa ser examinada em detalhe (micrografia, estrutura anatômica complexa, traço eletrofisiológico com vários eventos) — em coluna estreita o aluno não consegue ler os detalhes. Centralize com `largura: 85%`.
- Quando há **2+ figuras consecutivas** que precisam ser comparadas — montar `grid(columns: 2, ...)` direto, sem texto no meio.

---

## CATEGORIA 16 — Catálogo de família proteica/molecular

**Propósito:** mostrar o padrão canônico para apresentar uma família com 3+ membros paralelos (GLUT-1/2/3/4, SGLT-1/2, isoformas da hexoquinase, subtipos de receptor adrenérgico, classes de canal iônico). O REDATOR-E1 vinha defaultando para prosa enumerativa item-por-item — 5 parágrafos quase idênticos que o aluno não consegue comparar visualmente. A regra canônica L3 (CLAUDE.md §Bullets e tabelas, sub-caso da letra a) promove **parágrafo curto + tabela enxuta + parágrafo de fechamento** a default operacional para esses casos.

### Exemplar 16.1 — A família GLUT (transportadores facilitadores de glicose)

**DE ONDE:** Exemplo construído (caso modelo), a ser substituído quando o primeiro resumo da Geração 20 com tema "Transporte de glicose" for gerado e validar o padrão na prática.

**Trecho modelo:**

> O transporte de glicose através da membrana plasmática não é um processo único, mas uma família de pelo menos 14 proteínas relacionadas — os GLUTs. Todas compartilham a mesma arquitetura básica (12 hélices transmembrana com um sítio de ligação alternante para a glicose) e o mesmo mecanismo (difusão facilitada a favor do gradiente, sem gasto de ATP). O que muda entre os membros da família é a **constante de Michaelis (K_M) para a glicose** — e essa diferença não é detalhe biofísico: é o que decide *em qual concentração de glicose* cada GLUT trabalha de forma eficiente. Glicemia normal gira em torno de 5 mM; é em torno desse valor que a tabela abaixo organiza o sistema.
>
> ```
> #table(
>   columns: (auto, auto, 1fr, 1fr),
>   inset: 7pt,
>   align: (left, center, left, left),
>   stroke: 0.5pt + gray-border,
>   table.header(
>     [*Transportador*], [*K_M (mM)*], [*Onde está*], [*Papel fisiológico*]
>   ),
>   [GLUT-1], [~1],   [hemácia, BHE, fetal],       [captação basal contínua — funciona saturado em qualquer glicemia],
>   [GLUT-2], [~17],  [hepatócito, célula β, rim], ["sensor de glicemia" — só capta avidamente quando a glicose sobe],
>   [GLUT-3], [~1],   [neurônio],                  [garante captação mesmo em hipoglicemia leve],
>   [GLUT-4], [~5],   [músculo, adipócito],        [insulina-dependente — translocação para a membrana só com sinal hormonal],
> )
> ```
>
> Repare que GLUT-1 e GLUT-3 têm K_M baixo justamente nos tecidos que não toleram interrupção do suprimento (hemácia, cérebro) — eles operam saturados praticamente sempre. GLUT-2, com K_M alto, é o oposto: só "acorda" quando a glicemia sobe muito, o que é exatamente o que o hepatócito e a célula β do pâncreas precisam para detectar excesso de glicose após uma refeição. GLUT-4 é o caso especial regulado por insulina — voltamos a ele em 1.4 quando discutirmos a sinalização.

**POR QUE É BOM:**
- O **parágrafo de abertura** dá o *princípio organizador* (variação de K_M) antes de jogar os dados — o aluno entende o eixo antes de ver os números, e a tabela vira leitura "ah, faz sentido" em vez de "decoreba".
- A **tabela** tem 4 colunas que realmente se cruzam (transportador / K_M / localização / papel). Em prosa, comparar GLUT-1 e GLUT-2 exigiria voltar dois parágrafos atrás; em tabela, é uma linha de distância vertical.
- A coluna K_M aparece **com unidade explícita (mM)** e valores aproximados (`~1`, `~17`) — sinaliza que números exatos não são o ponto; o que importa é a ordem de grandeza relativa à glicemia normal (5 mM, ancorada no parágrafo de abertura).
**Quando usar este padrão:**
- Família proteica/molecular com **3+ membros paralelos** onde cada membro tem (a) a mesma arquitetura/mecanismo base e (b) parâmetros quantitativos ou contextuais que diferenciam o uso. Exemplos canônicos: GLUTs, SGLTs, isoformas de hexoquinase, subtipos α/β-adrenérgicos, classes de canais de Ca²⁺ (L/T/N/P/Q/R), isoformas de PKC.
- Sempre que o REDATOR-E1 perceber que está prestes a escrever **3 parágrafos quase idênticos com substituição de rótulos** ("O GLUT-1 está em X e tem K_M baixo. O GLUT-2 está em Y e tem K_M alto. O GLUT-3 está em Z e tem K_M baixo…"). Esse é o sinal de que a tabela vai render mais que a prosa.
- Quando o eixo organizador é **um parâmetro quantitativo único** (K_M, afinidade, valência, velocidade de condução) que ordena os membros — a coluna desse parâmetro vira o "espinha" da tabela e o aluno enxerga o sistema.

**Quando NÃO usar este padrão:**
- Quando o subtópico precisa **explicar o mecanismo** de um único membro da família em profundidade (ex.: "como funciona o GLUT-4 quando insulina chega"). Aí é prosa mecanística — o catálogo já existe em outro subtópico, ou nem precisa existir.
- Quando há só **2 membros** para comparar — prosa em parágrafos contrastados resolve melhor ("enquanto X faz A, Y faz B"). Tabela com 2 linhas vira gordura visual.
- Quando os membros **não compartilham arquitetura/mecanismo** (ex.: "transportadores de aminoácidos" — categoria heterogênea demais). Aí não é catálogo de família, é lista de coisas diferentes; vai gerar tabela com colunas que se aplicam mal a alguns membros.
- Quando a diferença entre os membros **não é quantitativa nem contextual paralela**, mas histórica/anedótica ("o GLUT-1 foi descoberto em 1985, o GLUT-2 em 1988…"). Esse tipo de informação não vai na tabela — vira nota de rodapé ou some.

---

## Categoria 17 — Cadência dialogal: enriquecer a prosa com flexibilidade

> **Espírito da categoria (ler antes do trecho).** Esta não é uma categoria de regras — é de **repertório**. O que ela demonstra é a sensação de prosa que *acompanha o leitor*, em vez de despejar parágrafos de estrutura idêntica. A âncora mental útil é a de uma explicação tipo Gemini num assunto que ele explica bem: o texto enriquece, hesita um instante, retoma, marca o que importa, troca de registro quando o conceito pede — sem deixar de ser tecnicamente preciso. Não há cota. **Não é para aplicar todas as manobras em todo parágrafo.** Distribuir 1 ou 2 por subtópico, conforme o tema convidar, já move o ponteiro inteiro. Em PARTE em que a prosa já está fluindo, deixar quieto vale mais que "encaixar" uma manobra. Em conflito entre o exemplar abaixo e regra abstrata, exemplar vence — mas em conflito entre o exemplar e prosa autoral que já está boa, **a prosa boa vence**. A categoria existe para socorrer o REDATOR quando o subtópico saiu plano, não para padronizar o que já tem voz.

### As 8 manobras de enriquecimento (índice rápido)

Cada manobra é um *gesto* que dá vida à prosa sem mudar o conteúdo técnico. O REDATOR escolhe — não cumpre uma checklist.

1. **Variar a abertura do parágrafo.** Se 4 parágrafos seguidos abrem com "A/O [substantivo]", trocar um por circunstancial ("Em cartilagem…"), retomada tema-rema ("Já a fração orgânica…"), inversão sintática ("Duas camadas formam o periósteo") ou marcador de progressão ("Antes de seguir…").
2. **Pingar 1 avaliação narrativa por subtópico.** *o ponto fino é*, *o preço dessa escolha é*, *o que muda tudo é*, *o detalhe que confunde todo mundo é*. Marca onde o leitor deve olhar.
3. **Antecipar a confusão na prosa, antes da caixa.** Plantar 1 frase tipo *"À primeira vista, parece natural pensar que… — só que…"* imediatamente antes de cada `#confusao-prevista`. A caixa formaliza; a prosa encena.
4. **Desinflar catálogo parentético.** Listas curtas dentro de parênteses quebram cadência. Embutir o exemplo principal na frase ou virar prosa funcional ("aparecem em quantidades menores, como íons coadjuvantes" em vez de "(magnésio, sódio, citrato)").
5. **Plantar marcador de progressão entre subtópicos da mesma PARTE.** *Daqui pra frente…*, *guarde isso, vai voltar…*, *antes de seguir, vale fixar…*. Sinaliza o arco sem listar.
6. **Reformulação como respiro.** Logo depois do mecanismo denso: *Ou seja…*, *Dito de outro modo…*, *Na prática…*. Usar 2 ou 3 vezes no resumo inteiro, no conceito que mais carrega o subtópico. Mais que isso vira tique.
7. **Aposto avaliativo em vez de descritivo.** Em vez de *"fibras de Sharpey, feixes de colágeno I que atravessam do periósteo para dentro da matriz cortical e ficam parcialmente mineralizados"*, escrever *"…costuram a bainha à matriz como pontos permanentes"*. Aposto que diz *função*, não só estrutura.
8. **Negrito funcional dentro da prosa.** Marcar 2 ou 3 frases-âncora por subtópico em negrito, dentro do fluxo contínuo (sem virar bullet). Cria mapa de leitura discreto.

### Trecho-modelo — PARTE I de Histologia do Tecido Ósseo (versão com cadência)

```typst
#parte-title("PARTE I — Identidade e composição do tecido ósseo", primeira: true)

#subtopico("1.1 De onde vem e por que importa")

No resumo anterior fechamos a cartilagem como conjuntivo especializado de matriz hidratada, avascular, que sustenta tensões mas colapsa sob compressão prolongada. O osso resolve exatamente esse limite — e resolve por um caminho oposto ao da cartilagem, o que vai organizar o resto desta PARTE. Como ela, é um conjuntivo especializado derivado do mesênquima; diferente dela, tem matriz extracelular #emph[mineralizada], endurecida pela deposição de cristais de hidroxiapatita sobre as fibras de colágeno. Essa mineralização muda quatro coisas de uma vez: a matriz passa a ser rígida em compressão, deixa de permitir difusão de moléculas pelo seu interior, vira reservatório de íons cálcio e fosfato, e exige células especializadas para ser construída, mantida e desmontada. *Guarde as quatro — vão voltar como organizadoras de toda a fisiologia óssea.*

A partir dessa propriedade central, todas as funções do osso seguem por consequência direta. *Sustentação mecânica* vem da rigidez à compressão. A *proteção* de cérebro, medula espinhal, coração e pulmões depende dessa mesma rigidez aplicada como caixa — o crânio e a caixa torácica são apenas geometria a serviço da mesma propriedade. A *reserva metabólica* de cálcio e fosfato, fundamental para regular calcemia, contração muscular, coagulação e excitabilidade neuronal, depende de a matriz ter cristais que podem ser dissolvidos sob demanda. E o papel hematopoético dos ossos longos do adulto, embora não seja função do tecido ósseo propriamente dito, depende da arquitetura esponjosa que ele forma para abrigar a medula. *No fundo, tudo volta para mineralização da matriz* — e é por isso que vale começar por ela antes de qualquer célula.

#subtopico("1.2 A marca: matriz mineralizada como solução mecânica")

Em cartilagem, a matriz aguenta compressão por estar hidratada — proteoglicanos atraem água por osmose, o gel inchado funciona como esponja que comprime e descomprime. Esse mecanismo tem teto: água é incompressível, mas o gel pode ser espremido até um limite, e a difusão de nutrientes pelo seu interior limita a espessura útil. *O osso resolve o mesmo problema pelo caminho oposto.* Em vez de prender água, deposita um cristal duro. Cristais de hidroxiapatita preenchem o espaço entre fibras de colágeno e formam uma fase sólida que não se deforma sob carga. A consequência é dupla: o tecido aguenta peso sem espremer — vantagem mecânica — mas perde permeabilidade interna a moléculas, desvantagem nutricional que vai exigir solução vascular adiante.

*À primeira vista, parece natural pensar que mineralizar uma cartilagem é o suficiente para "virar osso".* É uma confusão clássica, e vale desarmar antes de seguir.

#confusao-prevista(
  titulo: "Matriz óssea calcificada não é cartilagem calcificada",
  aluno_acha: [aluno acha que mineralizar cartilagem é "virar osso"],
  mecanismo: [matriz óssea tem colágeno #emph[tipo I] em feixes orientados, com hidroxiapatita depositada sobre o colágeno desde o início. Cartilagem calcificada é matriz cartilaginosa (colágeno II + proteoglicanos) que recebeu mineral em cima, sem reorganizar. São duas matrizes quimicamente distintas — a calcificação da cartilagem é etapa preparatória para que o osso a substitua, não conversão de uma na outra.],
)

A solução mecânica do osso traz junto uma consequência que muda a fisiologia toda. *Ou seja:* como a matriz mineralizada é impermeável a difusão de O₂ e glicose, a célula que ficar enterrada nela morre — a menos que tenha um sistema interno de canais para se comunicar com vasos. Por isso o osso é altamente vascularizado por dentro, com canais de Havers correndo ao longo do osso e canais de Volkmann atravessando-os, e por isso suas células maduras ficam conectadas por prolongamentos finos dentro de canalículos. *A arquitetura microscópica que vamos abrir na PARTE III é, no fundo, resposta direta à escolha de mineralizar a matriz.*

#subtopico("1.3 Matriz inorgânica e orgânica: concreto armado biológico")

Duas frações compõem a matriz óssea, e elas se complementam como mãos opostas de uma mesma solução de engenharia. *A inorgânica responde por 50–60% do peso seco e é a fase que dá dureza* — resistência à compressão. *A orgânica responde por 40–50% e dá flexibilidade* — resistência à tração. Quando atuam juntas, o tecido aguenta compressão sem esmagar e aguenta tração sem rachar — exatamente o comportamento mecânico do concreto armado, em que o concreto (fase mineral) resiste à compressão e a armadura de aço (fase orgânica de fibras) resiste à tração. *O ponto fino é que nenhuma das duas, sozinha, serve.* Sem mineral, o osso fica mole como tendão; sem colágeno, fica quebradiço como giz.

Dominando a fração inorgânica está a hidroxiapatita — cristais com fórmula Ca₁₀(PO₄)₆(OH)₂, depositados em forma de placas ou agulhas finas sobre as fibras de colágeno. Magnésio, sódio e citrato aparecem em quantidades menores, como íons coadjuvantes. Cada cristal carrega ao redor uma *capa de hidratação* — uma camada fina de água que permite troca iônica com o líquido intersticial, *e é essa capa, modesta mas decisiva,* que torna o reservatório ósseo de cálcio metabolicamente útil. Íons entram e saem do cristal por difusão na água da capa, e quando o sangue precisa de cálcio, a remoção pode ser feita sem desmontar a matriz inteira.

Já a fração orgânica é dominada por *colágeno do tipo I* — 90% dela, com pequena quantidade de tipo V no apoio. *A diferença em relação ao tipo II da cartilagem é mais funcional do que química:* o tipo I forma feixes grossos, orientados, paralelos no osso lamelar, e é essa orientação que dá direção mecânica preferencial à matriz. Os outros 10% da fração orgânica vêm das proteínas não-colagenosas — osteocalcina, osteopontina, sialoproteína óssea e fosfatase alcalina entre as principais —, e funcionam como sinalizadores moleculares: dizem ao osteoblasto *onde*, *quando* e *quanto* mineral depositar.

#subtopico("1.4 Periósteo e endósteo: fontes de osteoblasto novo")

Toda cartilagem tem pericôndrio cobrindo a superfície externa. *No osso, o esquema dobra:* há periósteo cobrindo a face externa e endósteo cobrindo cada face interna — canal medular, paredes dos canais de Havers e Volkmann, trabéculas do esponjoso. Os dois cumprem função análoga ao pericôndrio: bainha de conjuntivo com células progenitoras que repõem osteoblasto durante crescimento e reparo. *Daqui pra frente, sempre que aparecer "osteoblasto novo", é desses dois lugares que ele veio.*

Duas camadas formam o periósteo. A externa, fibrosa, é rica em colágeno tipo I e fibroblastos, e por ela passam os vasos e nervos que vão alimentar e inervar o osso. A interna, osteogênica, contém as células osteoprogenitoras — descendentes diretas do mesênquima, que mantêm capacidade de virar osteoblasto sob demanda. *A ancoragem do periósteo ao osso não é por encaixe, é por sutura biológica:* feita por fibras de Sharpey, feixes de colágeno I que atravessam do periósteo para dentro da matriz cortical e ficam parcialmente mineralizados — *costuram a bainha à matriz como pontos permanentes.* Tendões e ligamentos que se inserem no osso usam o mesmo mecanismo: suas fibras de colágeno se tornam fibras de Sharpey ao entrar na cortical.

Mais simples é o endósteo: uma camada única de células osteogênicas achatadas. Mas o papel é o mesmo, e tão fundamental quanto — é a fonte interna de osteoblasto novo. Durante o crescimento em espessura, periósteo e endósteo trabalham em espelho: o periósteo deposita matriz nova na superfície externa enquanto o endósteo, do lado de dentro, reabsorve cortical antiga, e o canal medular se mantém proporcional ao diâmetro externo do osso. No reparo de fratura, é dos dois lados que vem a maior parte dos osteoblastos do calo ósseo. *Sem essas duas camadas, simplesmente não há cicatrização* — e essa é uma das razões pelas quais fratura em idoso, com periósteo afinado, demora tanto mais para consolidar.

*Vale notar antes de fechar:* essas duas bainhas costumam ser tratadas pelo aluno como mero revestimento decorativo. Não são.

#confusao-prevista(
  titulo: "Periósteo e endósteo não são só revestimento",
  aluno_acha: [aluno acha que são bainhas passivas, sem papel funcional],
  mecanismo: [as duas camadas têm #emph[células osteoprogenitoras] ativas — fonte permanente de osteoblasto novo durante toda a vida. Periósteo nutre e protege a superfície externa; endósteo controla a remodelação interna. Sem eles, o osso não cresce em espessura e não cicatriza fratura.],
)
```

**DE ONDE.** Reescrita do `_par_histo-07-osseo/etapa1.typ`, PARTE I, gerada em 2026-06-18. Estudo completo + diagnóstico em `didatica/estudo-didatica-tom-dialogal.md` e `didatica/ajustes-finos-recentes.md`. Antes-depois lado-a-lado em `didatica/exemplo-parte1-osso-ajustada.md`.

**POR QUE É BOM.**

- Em 1.1, a abertura *"O osso resolve exatamente esse limite — e resolve por um caminho oposto ao da cartilagem"* anuncia o eixo da PARTE inteira em meia frase, sem listar tópicos. *"Guarde as quatro — vão voltar como organizadoras"* é marcador de progressão que dá ao leitor mapa do que vem sem virar bullet.
- Em 1.2, a frase *"À primeira vista, parece natural pensar que mineralizar uma cartilagem é o suficiente"* planta a confusão na prosa **antes** da `#confusao-prevista`. O leitor encontra a tentação errada como hipótese, descobre na caixa por que ela quebra, e segue. É o substituto canônico da pergunta retórica banida em 2026-05-29.
- Em 1.2, o *"Ou seja:"* que abre o parágrafo pós-caixa não repete o conteúdo da caixa — ele *traduz* o mecanismo de impermeabilidade num registro mais acessível. Usado uma vez por PARTE, é respiro; usado três vezes por subtópico, vira tique.
- Em 1.3, *"O ponto fino é que nenhuma das duas, sozinha, serve"* é avaliação narrativa em duas funções: marca o que importa e prepara a comparação "sem mineral / sem colágeno" que vem em seguida. A frase poderia ter sido suprimida sem perda técnica — mas a leitura ficaria mais plana.
- Em 1.3, o catálogo *"(magnésio, sódio, citrato)"* virou *"Magnésio, sódio e citrato aparecem em quantidades menores, como íons coadjuvantes"*. A informação é a mesma; a desinflação dá ritmo. O parêntese seria neutro; a frase é avaliativa.
- Em 1.4, *"No osso, o esquema dobra:"* substitui *"O osso tem periósteo cobrindo a superfície externa e endósteo cobrindo a superfície interna"* por uma avaliação compactada que diz **o que** o leitor está vendo de novo (a duplicação) antes de nomear as peças. É o gesto inverso do livro-texto, que nomeia primeiro.
- Em 1.4, *"feita por fibras de Sharpey, feixes de colágeno I que atravessam do periósteo para dentro da matriz cortical e ficam parcialmente mineralizados — costuram a bainha à matriz como pontos permanentes"* é aposto duplo: descrição química (*"feixes de colágeno I que…"*) seguida de aposto avaliativo (*"costuram… como pontos permanentes"*). A descrição química sobrevive porque a parte clínica seguinte precisa dela; o aposto avaliativo é o que fixa.
- A distribuição é desigual de propósito. 1.1 carrega mais marcadores de progressão (abertura de PARTE pede mapa). 1.2 carrega a antecipação de confusão e a reformulação densa (subtópico de mecanismo central). 1.3 carrega avaliação e aposto funcional (subtópico de catálogo mineral, que sem voz vira tabela). 1.4 carrega variação de abertura (subtópico de duas estruturas paralelas, fácil de cair em paralelismo monótono). *Cada subtópico chamou as manobras que precisava* — não recebeu todas.

**Quando usar este padrão.**

- Quando o REDATOR sentir que um subtópico "saiu correto, mas saiu plano". Em particular, quando a sequência de aberturas tem 4+ parágrafos começando com "A/O [substantivo]" ou quando há `#confusao-prevista` sem encenação anterior na prosa.
- Quando o tema tem muito catálogo (família proteica, classificação histológica, painel IHQ) e o risco real é virar enumeração mesmo com Categoria 16 aplicada — a 17 enriquece a prosa que costura o catálogo.
- Em fechamento de E1, como passada de calibração: olhar os 4 caracteres iniciais de cada parágrafo da PARTE, contar avaliações narrativas no subtópico mais denso, ver se há marcador na transição entre subtópicos. Ver `didatica/ajustes-finos-recentes.md` § 8 para a checklist de 45 segundos por PARTE.

**Quando NÃO usar este padrão.**

- Quando a prosa autoral já está com voz boa. Não plantar manobras "porque a categoria existe". *Em conflito entre a manobra prescrita aqui e prosa autoral que flui, a prosa autoral vence.* Esta categoria é socorro, não padrão exigido.
- Em `mini-resumo` e em legendas de figura. Esses gêneros pedem prosa plana, telegráfica, sem manobra. Tentar enriquecê-los quebra a função informativa.
- Em `clinica-box` que já tem voz boa (tipicamente a clínica-box carrega narrativa naturalmente). Aplicar manobras adicionais ali tende a redundância.
- Como cota numérica obrigatória ("1 avaliação por subtópico"). Tratar como cota engessa — o que esta categoria mais combate. O canônico anti-engessamento (CLAUDE.md § Diretrizes vs. exemplares; `feedback_evitar_engessar_anti_engessamento`) tem precedência sobre qualquer leitura literal das 8 manobras.
- Como excuse para aumentar extensão. A versão reescrita acima cresceu ~6% sobre a original — sem isso, é sinal de que as manobras viraram floreio, não enriquecimento. Se a versão com manobras ficou 20% maior, está aplicando demais.

**Nota de espírito (canônico 2026-06-18).** Esta categoria nasce da observação de que prosa expositiva tipo Gemini (no estilo dele explicando bem) tem uma flexibilidade de tom — varia abertura, pinga avaliação, antecipa objeção, troca de registro — que o NEBLI já fazia em flashes (ver as melhores frases dos resumos: *"concreto armado biológico"*, *"a peça é a assinatura física de uma decisão clínica anterior"*, *"o tecido nunca esquece como nasceu"*). A categoria não introduz manobra nova; **nomeia gestos que já apareciam, para que possam ser repetidos com consistência sem virar cobrança.** O alvo é menos "checklist cumprido" e mais "leitor sente que está sendo acompanhado".

### Gate complementar — Auditor de densidade pós-resumo (Haiku, canônico 2026-06-18)

A cadência dialogal só rende se a prosa **respira**. Parágrafo que tenta empacotar tudo (4 mecanismos, 8 siglas, 3 ramos de via metabólica em sete linhas) anula as 8 manobras: o leitor não sente acompanhamento, sente avalanche. Por isso esta categoria vem acompanhada de um **gate operacional automático** rodado depois que o COMPILADOR fecha o PDF e antes de mover pra `resumos-gerados/`.

**Agente:** REVISOR-DENSIDADE. Modelo: Claude Haiku 4.5 — escolhido porque (a) a tarefa é diagnóstico por rubrica simples, sem julgamento editorial profundo; (b) custo baixo permite rodar em **todo** resumo sem pesar; (c) latência baixa não atrasa o pipeline. Stub em `.claude/agents/revisor-densidade.md`.

**O que ele audita** (rubrica de 4 sinais, lê `typst-build/.../etapa1.typ` direto):

1. **Carga de siglas por parágrafo.** Conta siglas únicas e ocorrências. Sinaliza parágrafo com **≥ 4 siglas únicas** ou **≥ 6 ocorrências totais** — tipicamente significa empilhamento sem prosa de mecanismo entre elas (Regra Editorial 3 do CLAUDE.md). Não conta `#sigla(...)` na primeira aparição (essa é exigência), conta apenas as menções subsequentes.
2. **Densidade conceitual por parágrafo.** Conta substantivos técnicos distintos (proteínas, enzimas, vias, estruturas histológicas, marcadores) num parágrafo. Sinaliza **≥ 7 entidades técnicas distintas em ≤ 8 linhas** — sintoma de "quis dizer tudo, não disse nada".
3. **Profundidade real do mecanismo.** Heurística simples: o parágrafo tem pelo menos uma cadeia causal explícita (verbos do tipo *ativa, fosforila, recruta, bloqueia, libera, transcita, dissolve, digere, sinaliza*) ligando duas entidades? Parágrafo só com verbos de estado (*é, tem, contém, apresenta, consiste em*) numa região de mecanismo central é flag — informação enumerada sem causalidade.
4. **Foco vs. lateralidade.** O subtópico tem **1 mensagem central identificável**? O auditor faz a pergunta interna *"se eu pudesse só guardar uma coisa deste parágrafo, qual seria?"*. Se a resposta é difusa ("vários detalhes sobre X"), flag.

**Saída.** Arquivo `arquivos-trabalho/auditoria-densidade-<slug>.md` no formato:

```markdown
# Auditoria de densidade — <slug>

## Resumo
- Parágrafos analisados: N
- Flags totais: M
- Severidade global: VERDE / AMARELO / VERMELHO

## Flags por parágrafo
### PARTE I, subtópico 1.2, parágrafo 3
- Sigla overload: 5 únicas em 4 linhas (ATP, GTP, NADH, FADH₂, CoA)
- Sugestão: refundir em prosa de mecanismo. Cada sigla precisa de verbo de ação ao lado.

### PARTE II, subtópico 2.3, parágrafo 2
- Densidade conceitual: 9 entidades técnicas em 7 linhas
- Mensagem central difusa: parece misturar "regulação do osteoblasto" com "diferenciação do osteoclasto"
- Sugestão: separar em dois parágrafos OU recortar o que não é central.
```

**Severidade.**
- **VERDE:** 0–2 flags no resumo inteiro. Liberado.
- **AMARELO:** 3–6 flags. Sessão principal revisa, decide se corrige ou aceita.
- **VERMELHO:** ≥ 7 flags. Bloqueia movimentação do PDF. Sessão principal precisa endereçar antes de mover pra `resumos-gerados/`.

**Onde encaixa no pipeline.** Logo após `auditar_pdf.py` e antes do `mv` final do PDF — paralelo aos revisores Tier 2/3 didáticos que já rodam nesse ponto.

```
COMPILADOR → precompile-check → typst compile → auditar_pdf → REVISOR-DENSIDADE (Haiku) → mover PDF
                                                              ↑ novo gate
```

**Por que isso não engessa.** O REVISOR-DENSIDADE não opina sobre voz ("este parágrafo está chato") — só sobre carga ("este parágrafo tem peso demais"). É métrica simples, auditável, com thresholds explícitos. Se o REDATOR discorda do flag específico (às vezes a densidade é necessária — Krebs tem oito enzimas que **precisam** aparecer), basta aceitar a flag e mover. O gate hard é só o VERMELHO (≥ 7 flags), que indica padrão sistêmico, não caso pontual. Mantém o espírito anti-engessamento: convite forte no AMARELO, parede só no VERMELHO.

**Conexão direta com a categoria.** O REVISOR-DENSIDADE é o **complemento operacional** das 8 manobras. As manobras enriquecem a prosa quando ela está plana; o auditor flagga quando a prosa está sobrecarregada. As duas coisas atacam o mesmo defeito por lados opostos: prosa plana é falta de voz; prosa sobrecarregada é excesso de matéria. Boa cadência exige equilíbrio entre as duas — e é por isso que as duas vivem na mesma categoria.

---

## 18. Quando quebrar a prosa — tópico, tabela e cálculo *(NOVO 2026-06-24)*

**Origem:** pesquisa focada em Mankiw (didática em prosa) + apostila Poliedro (diálogo + redução pontual), em `arquivos-trabalho/pesquisa-didatica/ACHADOS-topico-tabela.md`. Itens 21/33/34/36/40/42/43 das Sugestões (3). Esta categoria é o **complemento** do default "prosa contínua": ela diz os poucos momentos em que quebrar a prosa ENSINA MAIS do que mantê-la.

**Premissa que não muda:** prosa expositiva é o motor. Os dois materiais confirmam isso — abrem por cenário concreto (Mankiw: "Imagine um dia comum…"; Poliedro: "Uma mosca pousa no alimento…"), nunca por pergunta-âncora. Tópico/tabela são exceções deliberadas, não alívio preguiçoso de texto.

### Gatilho 1 — Catálogo de tipos discretos (cada um com 1 traço definidor)

Quando o conteúdo é "N coisas paralelas, cada uma definida pelo traço que a separa das outras", o bullet acelera o contraste que a prosa diluiria.

> **POLIEDRO (classificação de cromossomos):**
> • **Metacêntrico:** centrômero em posição mediana; braços de mesmo comprimento.
> • **Submetacêntrico:** centrômero pouco deslocado do centro; um braço ligeiramente mais longo.
> • **Acrocêntrico:** centrômero próximo a uma extremidade; um braço longo e outro curto.
> • **Telocêntrico:** centrômero na extremidade; não ocorre em humanos.

**POR QUE É BOM:**
- Cada bullet começa pelo **nome em negrito + o traço definidor numa frase** — não fragmento solto.
- O paralelismo (todos descrevem posição do centrômero) torna o contraste imediato; em prosa, o leitor teria que reconstruir a comparação.
- É o caso (a) do CLAUDE.md § Bullets. **Não usar** quando os itens não são paralelos ou quando há cadeia causal entre eles — aí é prosa.

### Gatilho 2 — Cadeia de premissas de um argumento ("estilo cursinho", item 33)

Quando se lista os **passos discretos de uma dedução**, cada passo uma proposição independente que se soma à próxima, o bullet torna a lógica auditável.

> **POLIEDRO (raciocínio de Darwin a partir de Malthus):**
> • os seres de uma espécie diferem entre si;
> • a espécie tem potencial de crescimento exponencial;
> • os recursos são limitados, então nem todos sobrevivem;
> • há luta pela sobrevivência e muitos são eliminados;
> • sobrevivem os mais adaptados — o ambiente faz a seleção.

**POR QUE É BOM:**
- Cada linha é uma proposição fechada; juntas formam uma dedução que o aluno acompanha passo a passo.
- É o "estilo cursinho" que o Davi pediu (item 33) — sucinto, de qualidade, fluido.
- **Cautela:** só quando os passos são genuinamente discretos. Se há causa→mecanismo encadeado (A muda a forma de B que então faz C), fica prosa — bullet quebraria a cadeia.

### Gatilho 3 — Tabela de cruzamento (2+ dimensões que se referenciam)

> **POLIEDRO (ciclo do nitrogênio):** tabela com colunas *Material nitrogenado | Bactéria que o utiliza | Resíduo gerado | Bactéria que usa o resíduo*. Cada linha cruza entrada↔processo↔saída↔próximo processo.

**POR QUE É BOM:**
- A tabela existe porque cada linha **cruza** quatro dimensões que se referenciam; prosa perderia o alinhamento coluna-a-coluna.
- Mesmo princípio do catálogo de família proteica (GLUTs — categoria 16). Caso (a) do CLAUDE.md.

### Gatilho 4 — Resumindo em frase completa (item 36)

> **MANKIW (RESUMO de fim de capítulo):** cada item é frase inteira — "A curva de demanda mostra como a quantidade demandada de um bem depende do preço; conforme o preço cai, a quantidade aumenta."
> **POLIEDRO ("Resumindo"):** tópicos numerados, título curto em negrito + 2-4 linhas de mini-prosa — "**1. Organização do núcleo.** O núcleo é dotado de carioteca, cariolinfa, nucléolo e cromatina."

**POR QUE É BOM:**
- Menos ideias, mais palavras por ideia, frase encadeada — nunca fragmento ou aglomerado de sigla.
- É o modelo direto da diretriz 5 revista (Resumindo NEBLI: 6-10 seções, ~30-45 palavras cada).

### Cálculo bem explicado — etapas rotuladas (itens 1, 18)

> **MANKIW (incidência tributária):** a análise é feita em **Primeira Etapa / Segunda Etapa / Terceira Etapa**, cada uma um parágrafo curto que diz o que se faz E por quê, ancorada numa figura cuja legenda narra o mecanismo inteiro ("a quantidade de equilíbrio cai de 100 para 90 sorvetes…").

**POR QUE É BOM:**
- Matemática nunca é parede de símbolos: monta em prosa → passos rotulados com a razão de cada um → relê o número em palavras → figura que narra.
- Par negativo em `ANTI-EXEMPLARES.md` (A1). Vale para a E1 e para o modelo de resposta da E3; na E2 o gabarito continua só a letra.

**Quando usar esta categoria:** temas com catálogo de tipos (tecidos, organelas, isoformas), argumentos dedutivos, tabelas de cruzamento, ou matemática. **Quando NÃO usar:** mecanismo causal encadeado — esse é sempre prosa. Em conflito entre este exemplar e a regra abstrata, o exemplar vence.

---

## Como adicionar novos exemplares

Quando Davi identificar um trecho exemplar em um resumo:

1. **Trecho** copiado fielmente do PDF/HTML do resumo, com formatação preservada (negritos, itálicos, símbolos químicos).
2. **DE ONDE:** nome do resumo + subtópico de origem.
3. **POR QUE É BOM:** 4 a 6 bullets operacionais (não vagos). Cada bullet identifica um **movimento didático específico** que o exemplar demonstra. "Está bem escrito" não conta; "abre com pergunta-ponte que força o leitor a fazer a ligação estrutura → função" conta.
4. **Quando usar este padrão** (opcional, mas valioso para categorias novas): regras de quando o padrão se aplica e — mais importante — quando **não** usar.

Se o exemplar não couber em nenhuma categoria existente, criar nova categoria com nome descritivo (substantivo + qualificador). Categorias novas precisam de pelo menos um exemplar e um critério de inclusão antes de serem consideradas estáveis.
