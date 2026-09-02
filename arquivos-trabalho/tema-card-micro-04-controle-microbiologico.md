# Tema Card — micro-04-controle-microbiologico

## Seção A — Escopo

- **Tema:** Controle do crescimento microbiano — esterilização, desinfecção e antissepsia
- **Slug:** `micro-04-controle-microbiologico` (UC03 · Microbiologia · conteúdo 30)
- **Slide-fonte:** *Controle do Crescimento Microbiano* — Profa. Elisabete Vicente (Bete), Dep. Microbiologia ICB/USP, 2023 (34 páginas)
- **Disciplina (capa):** Microbiologia
- **Onde estudar (capa):** Trabulsi & Alterthum · Murray · Brock · Tortora · Manual de Processamento de Produtos para Saúde (Anvisa)
- **Alvo E1:** piso 2, **teto 22 páginas**. Alvo prático 19–21.
- **`profundidade:` `fundo`** — pedido explícito de Davi ("roda as etapas 1 a 3 acima do nível da prova"). O dial sobe o teto de **conteúdo**, nunca o de **verbosidade** (`ERROS.md` F10): alvo mantido em **450–550 palavras por subtópico**, 15 subtópicos.
- **Recorte slide × tema:** coincidem. O slide cobre exatamente descontaminação/desinfecção/esterilização, agentes físicos e agentes químicos. **Fronteiras declaradas** (ficam de fora, são outras aulas): antibiótico, antibiograma, CIM e mecanismo de resistência (`micro-05`); estrutura fina do esporo e da parede (`micro-01` — entra aqui só como retomada de 1–2 frases, porque é ela que explica a escada de resistência); curva de crescimento e fase estacionária (`micro-02`); técnica de assepsia de bancada (`micro-03`). O último slide anuncia desinfetantes ambientais e antibióticos como aula seguinte — o resumo para onde o slide para.

### Teto histórico desta aula × degrau da E1 (calibração UC03)

**O que o acervo já cobrou** (1 subquestão diretamente etiquetada, 2025 P2 · 3.3 MB):
- Diante de material reutilizável contaminado por *Mycobacterium tuberculosis*, **escolher o método** e **justificar pela característica do agente**: termorresistente → autoclave (121 °C/15–30 min ou 134 °C/3–10 min); termossensível → óxido de etileno ou plasma de peróxido de hidrogênio; superfície → hipoclorito 0,5–1% ou álcool 70% com tempo de contato adequado. O gabarito exige explicitar **por que** micobactéria pede alto nível: parede rica em lipídio.

**Onde a E1 vai um degrau acima** (o que faz o resumo passar do teto histórico):
1. Não parar em "autoclave 121 °C/15 min". Explicar **por que o vapor saturado sob pressão vence o forno**: a pressão eleva o ponto de ebulição; a água é necessária para a hidrólise das ligações que desestabilizam a proteína; e o calor latente de condensação entrega energia na superfície do material. Daí a consequência operacional: **ar retido dentro da câmara derruba a temperatura efetiva** — a falha mais comum do método.
2. Não parar em "mata 99,9%". Descer ao **valor D**, à cinética de primeira ordem e ao motivo de a esterilidade ser definida em **probabilidade** (nível de segurança de esterilidade de 10⁻⁶), não em ausência absoluta. Isso responde ao "Você concorda?" que o próprio slide planta.
3. Não parar na lista de resistência. Explicar a **escada inteira pelo mecanismo**: mycoplasma sem parede → vírus envelopado com lipídio dissolvível → vegetativa → vírus não envelopado só de capsídeo proteico → micobactéria com ácido micólico → esporo desidratado com dipicolinato e SASP → oocisto → príon sem ácido nucleico. Cada degrau é uma barreira física nomeável.
4. Não parar em "álcool 70%". Explicar **por que 70 e não 100** (a água é reagente da desnaturação e retarda a evaporação, garantindo tempo de contato) e por que isso não alcança esporo nem vírus não envelopado — com o gancho clínico do norovírus, que álcool em gel não resolve.
5. Não parar em "fita indicadora mudou de cor". Separar **indicador químico** (prova exposição à temperatura) de **indicador biológico** (*Geobacillus stearothermophilus* para calor úmido, *Bacillus* para calor seco e óxido de etileno) — o único que testa o parâmetro que interessa, a morte de esporo.
6. Não parar em "filtro de 0,22 µm esteriliza". Mostrar que ele **retém bactéria e fungo, mas não vírus nem micoplasma** — e que o HEPA não funciona por peneira, mas por interceptação, impactação inercial e difusão browniana, razão pela qual partícula *menor* que 0,3 µm é retida melhor, não pior.
7. Acrescentar o eixo que o slide só insinua: **critério de Spaulding** (crítico / semicrítico / não crítico) como a regra que transforma toda essa química em conduta — é ele que decide quando esterilizar e quando desinfetar.
8. Fechar com a **pergunta 7 do próprio slide**: todo esporocida é esterilizante? Não — a atividade esporocida depende de concentração e tempo, e esterilização é um processo validado, não uma propriedade da molécula. Glutaraldeído a 2% é alto nível em 20–30 minutos e esterilizante químico só em horas.

### Prioridades desta corrida (Diário de revisões + ajustes finos)

1. **F10 — economia de palavra (peso alto, 2026-08-31).** Alvo 450–550 palavras por subtópico. `fundo` sobe conteúdo, não verbosidade. Caçar os cinco desperdícios antes de fechar: moldura, legenda que repete o corpo, achado recontado, conclusão que reconta, duas frases onde uma cabe.
2. **Figura é canônica (diário 2026-05-29, peso alto).** O slide é rico em esquema (escada de resistência, desnaturação, cascata de filtros, sequência limpeza→desinfecção). Meta ≥3 figuras por PARTE, todas do slide.
3. **ERROS #23 — gabarito C/E conferido item a item** depois de escrito, nunca sorteado antes.
4. **ERROS #20 — `#termo-nota[X][def]` substitui a palavra**, não a antecede.
5. **Vocabulário banido.** Este tema é minado: "à prova de calor" → *resistente ao calor*; "prova biológica" → *indicador biológico* / *teste biológico*; "provas bioquímicas" → *testes bioquímicos*. Nenhuma ocorrência de prova/questão/gabarito no PDF.
6. **`didatica/ajustes-finos-recentes.md` §1 — início monocromático.** Tema de catálogo (métodos, classes químicas): risco alto de 5 parágrafos abrindo com "O/A [método] é…". Trocar 1 em cada 4.
7. **§3 — encenar a confusão na prosa antes da caixa.**
8. **Imagem descartada por juízo editorial:** `slide-07` e a foto central de `slide-20` (pira de corpos humanos, febre amarela em Cuba, séc. XIX). Conteúdo histórico legítimo no slide, mas gratuito no PDF — a incineração é ensinada em prosa com o esquema técnico, sem a fotografia.

---

## Seção B — Esqueleto das PARTES (15 subtópicos · 15 figuras)

### PARTE I — A régua: o que cada palavra promete (4 subtópicos)

| # | Subtópico | Núcleo mecanístico |
|---|---|---|
| 1.1 | Limpeza, desinfecção, antissepsia, esterilização: quatro promessas | Escala crescente de exigência; limpeza remove carga e matéria orgânica por ação mecânica; desinfecção mata/inibe patógeno em superfície inanimada; antissepsia é a mesma ideia sobre tecido vivo (e por isso limitada pela toxicidade); esterilização = eliminação de TODA forma, esporo e vírus inclusive |
| 1.2 | Estático e cida: por que o sufixo decide a conduta | -stático interrompe multiplicação e depende do hospedeiro para terminar o serviço; -cida mata; esporocida é a fronteira; "virustático" é conceitualmente vazio porque o vírus não se multiplica fora da célula. Quatro variáveis: espectro, concentração, tempo, toxicidade |
| 1.3 | A morte microbiana é logarítmica: valor D e o que "mata 99,9%" significa | Cinética de primeira ordem: fração constante morre por unidade de tempo, nunca um número absoluto; D = tempo para 1 log₁₀ = 90%; a curva nunca toca zero → esterilidade é definida em probabilidade (10⁻⁶); o resíduo de 10% importa em função do volume usado |
| 1.4 | A escada de resistência: quem morre primeiro e quem resiste a tudo | Cada degrau é uma barreira física: sem parede (mycoplasma) → envelope lipídico dissolúvel → parede vegetativa → capsídeo proteico nu → ácido micólico → esporo desidratado com Ca-dipicolinato/SASP → parede do oocisto → príon sem ácido nucleico a atacar |

**Figuras I:** `slide-21` (sequência limpeza → rinsagem → desinfecção → rinsagem, com legenda de símbolos, 60%) · `slide-31` (estática × cida + as quatro variáveis, 56%) · `slide-09` (escada de resistência com os desinfetantes eficazes em cada faixa, 74%). Tabela nativa do valor D em 1.3.

### PARTE II — Agentes físicos: calor, radiação, filtração e frio (6 subtópicos)

| # | Subtópico | Núcleo mecanístico |
|---|---|---|
| 2.1 | Por que o calor mata: desnaturação, o leite e o ovo | Calor rompe ligações fracas que sustentam a estrutura terciária; enzima desdobrada perde sítio ativo; desnaturação reversível (leite morno) × irreversível (ovo frito) explica por que temperatura e tempo são parâmetros acoplados |
| 2.2 | Autoclave e forno: por que 121 °C úmidos vencem 180 °C secos | Pressão eleva o ponto de ebulição da água → vapor saturado a 121 °C; água hidrolisa e desestabiliza a proteína; condensação entrega calor latente na superfície; ar retido derruba a temperatura efetiva. Calor seco mata por oxidação → exige 160 °C/2 h ou 180 °C/1 h. Indicador químico (fita) × indicador biológico (esporo) |
| 2.3 | Chama, fervura e pasteurização: os calores que não miram a esterilidade | Incineração converte o resíduo a CO₂ + H₂O; flambagem esteriliza a alça por combustão; fervura a 100 °C mata vegetativa e poupa esporo; pasteurização reduz carga preservando o alimento — alvo histórico é o patógeno não esporulado mais resistente ao calor |
| 2.4 | Radiação: a ionizante quebra o DNA, a ultravioleta o solda | Gama ioniza a água → radical hidroxila → quebra de fita: penetrante, "esterilização a frio" de descartáveis. UV-C 254 nm é absorvida pelas bases → dímero de timina → replicação travada, mas sem penetração e com reparo por fotoliase. Micro-onda só aquece dipolo de água → morte térmica desigual |
| 2.5 | Filtração: separar em vez de matar | Membrana de 0,22 µm retém bactéria e fungo, não vírus nem micoplasma; pré-filtros em cascata evitam colmatação; HEPA retém 0,3 µm por interceptação, impactação e difusão — por isso partícula menor é retida melhor; fluxo laminar protege o produto, não o operador |
| 2.6 | Frio, dessecação e liofilização: preservar não é matar | Frio é bacteriostático: metabolismo cai, população não morre; cristal de gelo mata parte, crioprotetor evita; liofilização sublima a água do estado congelado e preserva por décadas; dessecação para o metabolismo mas deixa sobreviventes |

**Figuras II:** `slide-06` (desnaturação reversível × irreversível, 62%) · `slide-10` (autoclave e forno, 66%) · `slide-11` (ampola com tira de esporos + fita termossensível, 70%) · `slide-15` (flambagem, fervura, pasteurização, 60%) · `slide-13` (gama, micro-ondas, UV e espectro com a faixa microbicida, 72%) · `slide-14` (filtração por membrana e cabine com HEPA, 70%) · `slide-18` (cascata 5 → 1,2 → 0,22 µm, 44%) · `slide-17` (dessecação, liofilização e a escala de temperaturas, 66%).

### PARTE III — Agentes químicos e a decisão clínica (5 subtópicos)

| # | Subtópico | Núcleo mecanístico |
|---|---|---|
| 3.1 | Limpar antes: a matéria orgânica é o inimigo do desinfetante | Sangue, pus e resto de tecido consomem o agente por reação química e blindam fisicamente o micro-organismo; biofilme multiplica o problema; por isso a sequência é detergente → enxágue → desinfetante → enxágue, e não desinfetante direto |
| 3.2 | Níveis de desinfecção e o critério que escolhe o agente | Alto nível mata tudo menos grande carga de esporo; intermediário inclui micobactéria; baixo não alcança micobactéria nem vírus não envelopado. Critério de Spaulding cruza isso com o destino do artigo: crítico → esterilizar; semicrítico → alto nível; não crítico → baixo/intermediário |
| 3.3 | Como cada classe química mata | Álcool 70% desnatura e dissolve lipídio (a água é reagente); cloro libera ácido hipocloroso que oxida tiol; iodo halogena tirosina; aldeído alquila e reticula proteína e ácido nucleico (único esporocida líquido comum); fenólico rompe membrana e precipita proteína, com atividade residual; quaternário de amônio é tensoativo catiônico de baixo nível; oxidante gera radical livre |
| 3.4 | Antisséptico: o mesmo princípio com um hospedeiro vivo por perto | A restrição é a toxicidade tecidual, não a potência; Semmelweis e a cal clorada; Lister e o ácido carbólico; clorexidina liga-se ao estrato córneo e por isso tem ação residual — o que muda a escolha na antissepsia cirúrgica e na punção de acesso central |
| 3.5 | Esterilizar o que não aguenta calor — e a pergunta que fecha a aula | Óxido de etileno alquila DNA e proteína, penetra a embalagem, roda a 55–60 °C e exige aeração porque o resíduo é tóxico; plasma de H₂O₂ a 35–45 °C gera radicais e UV, deixa água e oxigênio, mas é barrado por celulose e lúmen longo. Esporocida ≠ esterilizante: a diferença é concentração, tempo e validação |

**Figuras III:** `slide-27` (quadro de produtos de limpeza e desinfecção de superfícies em serviços de saúde, 70%) · `slide-26` (classes, concentração de uso e nível de atividade, 66%) · `slide-22` (Semmelweis e a queda da mortalidade puerperal, 60%) · `slide-12` (esterilizador por plasma de peróxido de hidrogênio, 64%).

---

## Seção B.bis — Registro de abertura por subtópico

| # | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | ponto-de-quebra |
| 1.3 | analogia concreta |
| 1.4 | integração-anterior |
| 2.1 | ponto-de-quebra |
| 2.2 | integração-anterior |
| 2.3 | enquadramento |
| 2.4 | analogia concreta |
| 2.5 | ponto-de-quebra |
| 2.6 | integração-posterior |
| 3.1 | integração-anterior |
| 3.2 | enquadramento |
| 3.3 | analogia concreta |
| 3.4 | integração-posterior |
| 3.5 | ponto-de-quebra |

Nenhum par vizinho compartilha registro.

---

## Seção B.ter — Pré-requisitos cruzados (frase-âncora pronta)

| Pré-requisito | Frase pronta (≤25 palavras) |
|---|---|
| Parede bacteriana Gram± | "A parede é a malha de peptideoglicano que segura a pressão interna; na Gram-negativa ela é fina e coberta por uma membrana externa lipídica." |
| Endósporo | "O endósporo é uma forma de repouso com o núcleo desidratado, um córtex espesso e o DNA embalado em proteínas protetoras — feito para atravessar o que mata a célula ativa." |
| Envelope viral | "Vírus envelopado carrega uma bicamada lipídica roubada da célula hospedeira; vírus não envelopado tem só o capsídeo de proteína." |
| Ácido micólico | "A micobactéria cobre a parede com uma camada cerosa de ácido micólico, hidrofóbica, que repele solução aquosa." |
| Desnaturação proteica | "Desnaturar é desfazer o dobramento que dá forma à proteína; sem forma, o sítio ativo da enzima deixa de existir." |
| Príon | "Príon é proteína mal dobrada que induz cópias da forma normal a se dobrarem errado — não tem ácido nucleico para ser quebrado." |

---

## Seção C — Distribuição da E2

`profundidade: fundo` → taxonomia **PROFUNDO**: **8 Consolidação · 17 Integração · 5 Aplicação**.

- Formatos: **20 múltipla escolha** + **10 Certo/Errado** (4 itens I–IV cada, gate hard) + **3 "assinale a incorreta"** dentro das MC.
- C/E distribuídas pelas três categorias, não só em Consolidação.
- Sequência C/E **decidida item a item na redação** e só depois auditada pela guarda anti-degeneração (`ERROS.md` #23).
- **Fronteira da aula:** não entra antibiótico, CIM, antibiograma nem mecanismo de resistência — é `micro-05`. Cruzamento com `micro-01` (parede, esporo, envelope) é legítimo porque é ele que sustenta a escada de resistência.

**Termos-nota obrigatórios (6–10):** vapor saturado · calor latente · dipicolinato de cálcio · ácido micólico · dímero de timina · colmatação · atividade residual · alquilação · oocisto · esporocida.

---

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** tratar desinfecção e esterilização como graus da mesma coisa.
  Correção: são promessas distintas — desinfecção reduz a carga de patógenos a um nível seguro para o uso pretendido; esterilização elimina toda forma viável, esporo e vírus inclusive. O que separa as duas é justamente a forma mais resistente.

- **Quebra:** achar que temperatura mais alta sempre vence.
  Correção: 121 °C de vapor saturado esterilizam em 15 minutos e 180 °C de ar seco precisam de uma hora. A água é reagente da desnaturação e o vapor entrega calor latente na condensação; ar seco só oxida, e devagar.

- **Quebra:** ler a fita indicadora escurecida como comprovação de esterilidade.
  Correção: o indicador químico registra que o pacote foi exposto à temperatura, não que a exposição durou o tempo necessário. Só o indicador biológico, com esporo vivo, testa o parâmetro que interessa.

- **Quebra:** supor que álcool 100% é mais forte que álcool 70%.
  Correção: sem água, o álcool coagula a superfície da proteína e para de penetrar, e evapora antes de completar o tempo de contato. A diluição é o que faz o produto funcionar.

- **Quebra:** confiar em álcool em gel contra qualquer agente de diarreia.
  Correção: álcool age dissolvendo lipídio e desnaturando proteína; vírus não envelopado, como o norovírus, não tem lipídio a dissolver. A conduta é água e sabão pela remoção mecânica, e hipoclorito na superfície.

- **Quebra:** tratar filtro de 0,22 µm como sinônimo de estéril.
  Correção: ele retém bactéria e fungo, mas vírus e micoplasma passam. É esterilizante por convenção para soluções em que o alvo é bactéria — não para conteúdo viral.

- **Quebra:** achar que o frio mata.
  Correção: o frio é bacteriostático. Ele desacelera o metabolismo e conserva o micro-organismo — é por isso que a geladeira preserva a cepa no laboratório e não torna o alimento seguro por tempo indefinido.

- **Quebra:** aplicar desinfetante sobre superfície ainda suja.
  Correção: matéria orgânica consome o agente por reação química e blinda fisicamente o micro-organismo. Sem limpeza prévia, a concentração que chega ao alvo é uma fração da concentração rotulada.

- **Quebra:** concluir que todo esporocida é esterilizante.
  Correção: a atividade esporocida depende de concentração e tempo de contato. Glutaraldeído a 2% é desinfetante de alto nível em vinte a trinta minutos e só esteriliza em horas — a molécula é a mesma, o processo é que muda.

---

## Seção E — Exemplares-âncora

- **Categoria 1 (universal) — explicação mecanística parágrafo a parágrafo.** Vou usar em 2.2 (autoclave) e 1.3 (valor D): cada parágrafo entrega um elo e o seguinte parte dele. É o gesto que sustenta o resumo inteiro.
- **Categoria 8 (universal) — `atencao-box`.** Reservar o vermelho para as duas inversões com consequência real: fita indicadora lida como comprovação de esterilidade (PARTE II) e álcool em gel contra vírus não envelopado (PARTE III). O resto vira `confusao-prevista` gold ou prosa.
- **Categoria 14 (universal) — siglas em footnote.** Tema com UV, HEPA, DNA, RNA, EPI, EtO — declarar na 1ª aparição, sem empilhar.
- **Categoria 4 — magnitudes ancoradas.** 121 °C/15 min, 180 °C/1 h, 0,22 µm, 254 nm, 25 kGy, 10⁻⁶: o resumo vive de números. Cada um entra ancorado no que ele significa, nunca solto.
- **Categoria 7 — analogia construtiva.** Usar duas, no máximo: a panela de pressão para o vapor saturado (analogia segura, o mecanismo é literalmente o mesmo) e o "desconto de 90% sobre o que sobrou" para a cinética logarítmica.
- **Categoria 12 — cálculo bem explicado.** O valor D é a única matemática da aula; entra em etapas rotuladas, montada em prosa antes de virar tabela, e relida em palavras no fim.
- **Categoria 16 — catálogo de família.** As classes químicas de 3.3 são exatamente o caso: parágrafo de mecanismo comum + tabela do slide para o cruzamento classe × concentração × nível.
- **Categoria 18 — quando quebrar a prosa.** A tabela do valor D (1.3) é cruzamento de 3 dimensões numéricas; a de classes químicas (3.3) já vem pronta no slide. Nenhuma outra quebra.
