# Revisão profunda Tier 3 — UC02-BMC-01-celulas-do-sangue

**Tema (ancoragem):** Células do Sangue (UC02 · BMC · aula 1 — Histologia)
**Autor:** FS (Fluxo Standard NEBLI — apostila gerada pelo próprio pipeline)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

## Ancoragem prévia

- Tema canônico (literal do slug): "Células do Sangue" — histologia do sangue como tecido conjuntivo + elementos figurados.
- 3 conceitos centrais que eu-aluno gostaria de aprender: (1) por que o sangue é tecido conjuntivo, plasma vs soro e hematócrito; (2) hemácia — anucleada/bicôncava, hemoglobina, ciclo de 120 dias, esferocitose; (3) leucócitos (granulócitos vs agranulócitos com diapedese mecanística) e plaquetas/hemostasia.
- 2 temas vizinhos que NÃO são esse: hemoglobina I/II (BIOQ — curva de saturação, Bohr) e hemostasia/coagulação avançada (vias intrínseca/extrínseca em detalhe).

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| 1.1 Tecido conjuntivo líquido | OK | 3–4 | Abertura por "estranheza" + analogia osso/cartilagem/frouxo prende. Mini-síntese 1.1 segura. |
| 1.2 Plasma/hematócrito | OK | 5 | Números ancorados (39–50% / 35–45%). Justificativa testosterona-eritropoese é bônus. |
| 1.3 Plasma vs soro | OK | 6–7 | "Cenário 1 / Cenário 2" funciona; é o exemplar do que NEBLI deveria copiar. |
| Cascata de coagulação em panorama | [STOP: pág 8] | 8 | Despeja Fator XII, XI, IX, VIII, X, plasmina, varfarina, t-PA, antitrombina III, hemofilia em um único parágrafo sem ancorar nada. O texto avisa "vai ver detalhe em hemostasia" mas mesmo assim joga 8 nomes de fatores sem sequência mecanística — aluno trava. |
| 2.1 Bicôncava | OK | 10–11 | "Disco bicôncavo tem 20–30% mais área" + 3 μm vs 7,5 μm é o melhor parágrafo do documento. |
| 2.2 Hemoglobina + 120 dias | parcial | 11–12 | Sequência "proeritroblasto → eritroblasto basófilo → policromático → ortocromático → reticulócito" aparece in-line sem figura nem footnote. Aluno-alvo vê 5 nomes greco-latinos e fecha. [STOP: pág 12] |
| 2.3 Citoesqueleto eritrocitário | parcial | 14 | "Banda 3, 4.1, 4.2, 4.9, glicoforina C, actina, anquirina, espectrina" em um parágrafo só — sem termo-nota para nenhuma, sem hierarquia (qual é o "cabo" e quais são "âncoras"). [STOP: pág 14] |
| 2.3 ABO/Rh | OK | 15 | Mecanismo de açúcar terminal + lógica anticorpos naturais é exemplar. |
| 3.1 Neutrófilo + 3 grânulos | parcial | 18 | Três tipos de grânulo (específicos/azurófilos/terciários) listados densamente. "Ato 1/Ato 2/Ato 3" salva a diapedese, mas IL-8, TNF, selectinas, integrinas, ICAMs aparecem só na discursiva Q5 com mais clareza do que aqui na E1. |
| 3.1 Eosinófilo/Basófilo | OK | 19–20 | MBP + IgE explicado bem; ligação basófilo↔mastócito é didática. |
| 3.2 Linfócito | [STOP: pág 21] | 21 | Densidade pico: "B (10–15%) — T (70–80%) — T-CD4 (50–60% dos T) — T-CD8 (20–25%) — NK (10%)" + MHC + HIV/AIDS + plasmócito + memória + vacinação em ~400 palavras. Cinco percentuais aninhados em uma página só. |
| 3.3 Plaquetas | OK | 23–24 | Megacariócito 32n/64n é detalhe rico; hemostasia primária/secundária explicada em sequência clara. |

**Diagnóstico do padrão:** o material é forte em aberturas conceituais e em explicações mecanísticas pontuais, mas falha quando precisa apresentar **inventário** (cascata de coagulação, sequência de eritroblastos, proteínas do citoesqueleto, subtipos de linfócito). Toda vez que vira lista densa em prosa corrida sem termo-nota nem figura, o aluno-alvo para.

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria 1 (Explicação mecanística parágrafo-por-parágrafo) — comparação 2 parágrafos:**

**EXEMPLAR-LIKE (padrão NEBLI canônico) — Plasma vs soro (pág 6–7):**

> "Cenário 1: você adicionou anticoagulante. O anticoagulante — pode ser heparina, citrato de sódio (que quela cálcio) ou EDTA — bloqueia a cascata de coagulação. Sem coagulação, o sangue continua líquido. Quando você centrifuga esse tubo, o que sobe é plasma: a matriz líquida intacta, com fibrinogênio, protrombina e todos os fatores de coagulação ainda dissolvidos."

Funciona pelo molde de "cenário": parêntese técnico ("que quela cálcio") explica em-linha, sem footnote pesado; consequência mecanística vem na frase seguinte; soro entra no Cenário 2 paralelo. É a Categoria 1 do EXEMPLARES executada com sucesso, e por extensão a Categoria 3 (abertura por desfazer confusão clássica).

**CONTRA-EXEMPLO (densidade que quebra o padrão) — Cascata de coagulação em panorama (pág 8):**

> "Fator XII, XI, IX, VIII, X, que convergem em uma via comum — protrombina vira trombina (a serina-protease central), trombina corta fibrinogênio em fibrina, e a fibrina se polimeriza em rede. Cálcio é cofator essencial em vários passos; vitamina K é cofator na síntese hepática de protrombina, daí o uso de varfarina como anticoagulante."

Aqui o texto deixa de seguir Categoria 1 (parágrafo-por-parágrafo com mecanismo encadeado) e vira lista compactada. O comentário "você não precisa decorar todos os fatores" não compensa — o aluno-alvo lê a lista mesmo assim e trava. Reescrita seguindo o exemplar de plasma vs soro: separar em três micro-cenários (vaso íntegro / vaso lesado / cascata terminal) com 1 fator-âncora cada (Fator tecidual → Fator X → trombina), deixando XII/XI/IX/VIII como nomes secundários numa lateral ou no termo-nota.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo 1 — Cascata de coagulação em panorama (pág 8)

**(a) Citação literal:**
> "léso vascular libera fator tecidual e ativa uma sequência de proteases plasmáticas (Fator XII, XI, IX, VIII, X), que convergem em uma via comum — protrombina vira trombina (a serina-protease central), trombina corta fibrinogênio em fibrina, e a fibrina se polimeriza em rede. Cálcio é cofator essencial em vários passos; vitamina K é cofator na síntese hepática de protrombina, daí o uso de varfarina como anticoagulante. Quando o coágulo já cumpriu o papel, o sistema plasmina dissolve a rede."

**(b) Diagnóstico mecanístico:** o parágrafo lista 5 fatores numerados + protrombina + trombina + fibrinogênio + fibrina + Ca²⁺ + vitamina K + varfarina + plasmina em 4 linhas. Para aluno-alvo isso é 11 entidades novas sem ordem visual. O aviso "você não precisa decorar" não funciona porque o aluno ainda não sabe identificar o que é decorável e o que é mecanístico.

**(c) Reescrita pronta:**

> Para entender hoje, basta o esqueleto em três passos. **Passo 1 — gatilho:** a parede vascular lesada expõe fator tecidual, uma proteína de membrana das células endoteliais. Esse fator é o "fósforo" que acende a cascata. **Passo 2 — convergência:** uma série de proteases plasmáticas (Fatores XII, XI, IX, VIII — não decore os números) ativa o Fator X, que é o ponto onde as vias intrínseca e extrínseca se encontram. **Passo 3 — produto final:** Fator X ativo converte protrombina em trombina (a tesoura central da hemostasia); trombina corta fibrinogênio dissolvido em fibrina insolúvel, que se polimeriza em rede. O cálcio entra como cofator em vários passos — é por isso que tubos com citrato (que quela Ca²⁺) bloqueiam a cascata in vitro. A vitamina K participa da síntese hepática de protrombina, e a varfarina bloqueia esse ciclo — daí seu uso como anticoagulante oral. Quando o coágulo cumpre o papel, a plasmina dissolve a rede de fibrina. (Hemofilia clássica = falta do Fator VIII; ver hemostasia.)

### Parágrafo 2 — Eritropoese in-line (pág 12)

**(a) Citação literal:**
> "Ela nasce na medula óssea a partir de uma célula-tronco hematopoiética, passa pela linhagem eritroide (proeritroblasto → eritroblasto basófilo → eritroblasto policromático → eritroblasto ortocromático → reticulócito) e só então expulsa o núcleo e cai na circulação como hemácia madura."

**(b) Diagnóstico mecanístico:** cinco estágios greco-latinos sem ancoragem mecanística — o aluno-alvo não sabe por que cada nome muda. "Basófilo/policromático/ortocromático" remetem a coloração de cromatina/hemoglobina mas isso nunca é dito. Vira pura decoreba.

**(c) Reescrita pronta:**

> A linhagem eritroide é uma sequência de "deixar de ser célula completa para virar saco de hemoglobina". Começa no proeritroblasto, célula grande com núcleo ativo. À medida que produz hemoglobina, o citoplasma vai ficando vermelho — daí os nomes dos estágios refletem o que se vê no microscópio: basófilo (citoplasma azul, ainda fazendo ribossomo), policromático (mistura de azul ribossômico e vermelho da hemoglobina nascente), ortocromático (vermelho dominando, núcleo já pequeno). No estágio reticulócito o núcleo já foi expulso, mas restam mRNAs visíveis com corante supravital. Ao perder esses últimos restos, vira hemácia madura e cai no sangue. Não decore os nomes — saiba que é uma escala de cor refletindo "perdendo organela, ganhando hemoglobina".

### Parágrafo 3 — Citoesqueleto da hemácia (pág 14)

**(a) Citação literal:**
> "A espinha dorsal da malha é a espectrina, um par de cadeias α e β entrelaçadas como um cabo. Vários cabos de espectrina se conectam em nós (junções de actina, banda 4.1 e banda 4.9) formando uma rede hexagonal logo abaixo da membrana. Essa rede é ancorada à membrana por anquirina e banda 3 (canal de troca de ânions); glicoforina C faz outra ancoragem ao lado."

**(b) Diagnóstico mecanístico:** sete proteínas (espectrina α/β, actina, banda 4.1, banda 4.9, anquirina, banda 3, glicoforina C) em duas frases. Falta hierarquia explícita "cabo vs nó vs âncora". Falta também figura referenciada à legenda — a legenda da imagem diz tudo, mas o parágrafo se sobrepõe a ela sem complementar.

**(c) Reescrita pronta:**

> Pense na rede em três camadas funcionais. **Camada cabo (o elástico):** a espectrina é a estrela — duas cadeias (α e β) entrelaçadas como uma corda dupla. Cordas individuais de espectrina não bastam; várias se cruzam em pontos chamados nós. **Camada nó (a junção):** cada nó é uma plataforma de actina mais duas proteínas auxiliares (banda 4.1 e banda 4.9) que prendem os cabos uns nos outros, formando uma rede hexagonal logo abaixo da membrana. **Camada âncora (preso na membrana):** essa rede hexagonal precisa estar grudada na membrana plasmática — duas grudadores cuidam disso: anquirina (que segura via banda 3, o canal que troca Cl⁻ por HCO₃⁻ no transporte de CO₂) e glicoforina C. Quando uma dessas proteínas falha geneticamente — espectrina, anquirina, banda 3 ou banda 4.1 — a malha desorganiza e a hemácia perde a forma bicôncava: vira esfera (esferocitose) ou elipse (eliptocitose).

---

## 4. T3.3 — 3 seções mais densas

| Seção | Densidade | Mitigação concreta |
|---|---|---|
| Cascata de coagulação (pág 8) | 11 entidades novas em 4 linhas | Reescrever em 3 passos numerados como acima; mover XII/XI/IX/VIII para termo-nota ou rodapé. |
| Subtipos de linfócito (pág 21) | 5 percentuais aninhados em 1 parágrafo (B 10–15%, T 70–80%, T-CD4 50–60% dos T, T-CD8 20–25%, NK 10%) | Tabela mínima de 4 linhas (B / T-CD4 / T-CD8 / NK) com colunas "% dos linfócitos" e "função em uma frase". Cabe em ¼ de página e libera prosa para mecanismo HIV → AIDS. |
| Linhagem eritroide (pág 12) | 5 estágios in-line sem ancoragem visual | Mini-figura horizontal "→ basófilo → policromático → ortocromático → reticulócito → hemácia" com 1 linha de legenda por estágio (cor + perda). Ou parágrafo reescrito como acima. |

---

## 5. T3.4 — Voz fora do padrão

A voz é majoritariamente coerente com o padrão NEBLI (diálogo conversacional, sem bullets, com mini-resumos). Dois desvios pontuais:

- **Telegráfico técnico:** "Fator XII, XI, IX, VIII, X, que convergem em uma via comum" (pág 8) — é a única passagem onde a apostila abandona prosa dialógica e vira manual; conflita com a abertura "Vamos por mecanismo" da pág 6 que define o tom da unidade.
- **Auto-referência meta:** "Da PARTE I você sai entendendo…" / "A PARTE II te entrega a hemácia inteira…" — boas como conclusões integradoras, mas o "te entrega" repete fórmula 3× ao longo do documento (pág 9, 16, 26). Variar para evitar tique.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** pág 21 (subtipos de linfócito + HIV/MHC + NK + memória). Concentra 5 percentuais, 3 siglas críticas novas (MHC, NK, HIV), e a explicação fisiopatológica do AIDS, tudo em ~400 palavras.

**3 mitigações possíveis:**
1. Tabela de 4 linhas para os subtipos (separa estrutura de função, libera prosa).
2. Quebrar parágrafo do HIV/CD4 em box `.clinica-box` separado (assim a fisiopatologia da AIDS vira destaque, não nota corrida).
3. Mover a citação de NK para subseção própria ("imunidade inata celular") — hoje aparece encaixada como exceção dos linfócitos T, o que confunde (NK não é T).

**Qual escolher:** combinar 1 + 2. A tabela resolve o pico numérico; o box clínico transforma "o AIDS" de aside em destaque didático calibrado para o aluno-alvo.

---

## 7. T3.8 — Análise visual (do PDF, páginas 1, 2, 4, 5, 16, 21, 46)

| Sub-item | Estado | Detalhe |
|---|---|---|
| Hierarquia tipográfica | OK forte | Capa (pág 1): faixa navy + título serifado grande + subtítulo cinza + bloco meta canônico (Disciplina/Nota/Onde). Cabeçalho de runner ("ETAPA 1 — TEXTO DIDÁTICO") em caps cinza-claro funciona. Títulos de PARTE em teal, 1.x em peso médio — clara escada visual. |
| Valor pedagógico das figuras | misto | Pág 4 (categorias de tecido conjuntivo + sangue): figura **integrada** com legenda em itálico que reformula o conceito principal — exemplar. Pág 5 (tubo centrifugado + gráfico de proteínas plasmáticas em pizza): duas figuras pequenas lateralizadas; legenda do tubo é literal e útil, gráfico de proteínas é decorativo (só repete o que o texto já disse). |
| Densidade visual | aceitável a problemática | Pág 16 fica QUASE VAZIA: só uma `.atencao-box` de Conclusão integradora ocupa ~25% da página, restante é branco. Sinal de que a quebra de página antes da PARTE III foi forçada. Pág 21 é o oposto: muro de texto + figura pequena de linfócito em repouso espremida na lateral. |
| Uso de cor | coerente | Navy (#1F3A5F-ish) para faixas/capa, teal para títulos de PARTE/seção, gold só na faixa "Resumindo" (pág 27 — ver txt). Boxes em borda azul (`.atencao-box`) — coerentes. Sem cor decorativa supérflua. |
| Cortes/overflow | nenhum cortado, mas hiphenização inconsistente | Pág 5: "globu-/linas" quebrando entre linhas com hífen. Pág 4: "soluç-/ão" não detectada nesta amostra mas é padrão Merriweather. Sem figura cortada nas amostras. Pág 16 é overflow para baixo (branco de mais). |

**Achado visual crítico:** pág 46 (gabarito) mostra header "ETAPA 4 — FUNDAMENTOS" em runner — porém Etapa 4 foi removida do PDF canônico em 2026-05-22. Esse é metadata de header desatualizado (cosmético, mas confunde aluno).

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### Técnica 1 — "Função antes da forma" como fio narrativo declarado

**Citação literal (pág 1, Nota de uso):**
> "O fio mecanístico é função → forma: cada elemento figurado existe porque uma demanda fisiológica precisava ser resolvida de um jeito que nenhuma outra célula resolveria. Não decore 'neutrófilo tem núcleo lobulado' antes de entender por que essa forma serve à diapedese."

**Nome da técnica:** declaração explícita do fio narrativo na capa, com promessa de método (função → forma) que se repete como refrão nas conclusões integradoras.

**Quando o REDATOR-E1 NEBLI deveria usar:** sempre que o tema for histológico ou taxonômico (Compartimentos I/II/III, Citoesqueleto, Células do sangue, futuros temas de Imuno). Promove a "Nota de uso" de boilerplate para promessa pedagógica — Davi já valida na capa o que o leitor vai receber. **Gancho concreto:** adicionar à `redator-e1.md` regra "se o tema tem inventário de entidades (≥4 tipos celulares/organelas comparáveis), a Nota de uso declara o fio narrativo unificador que será refrão nas conclusões integradoras."

### Técnica 2 — "Cenário 1 / Cenário 2" para desfazer confusão clássica

**Citação literal (pág 6):**
> "Imagine que você tirou sangue de uma veia e colocou no tubo. Duas coisas podem acontecer dali em diante, dependendo do que você fez com o tubo. Cenário 1: você adicionou anticoagulante… Cenário 2: você não adicionou nada."

**Nome da técnica:** "bifurcação em dois cenários paralelos" — confusão clássica desfeita por colocar os dois caminhos lado-a-lado, em frases simétricas.

**Quando o REDATOR-E1 NEBLI deveria usar:** confusões binárias específicas (plasma vs soro, intrínseca vs extrínseca, T-CD4 vs T-CD8, oxi-Hb vs desoxi-Hb, ABO vs Rh — qualquer "A vs B com mecanismo separável"). É instância concreta da Categoria 3 do EXEMPLARES.md, mas mais ritualizada. **Gancho concreto:** adicionar como sub-padrão dentro da Categoria 3 ("variante: bifurcação simétrica com frases-eco — 'Cenário 1: X. Cenário 2: Y'").

### Técnica 3 — "Por quê" macroscópico antes da descrição estrutural

**Citação literal (pág 10):**
> "Por que tanta especialização? Porque a função da hemácia é uma só: transportar oxigênio dos pulmões para os tecidos, e gás carbônico no caminho inverso. Toda estrutura dela se subordina a essa função. Sem núcleo, ela não sintetiza proteínas novas — mas também não gasta espaço com cromatina… Sem mitocôndrias, ela não consome o oxigênio que carrega — uma hemácia que respirasse aerobicamente seria o pior tipo de carregador, porque consumiria parte da carga no caminho."

**Nome da técnica:** "interrogação retórica seguida de cadeia de consequências mecanísticas" — pergunta motivadora abre, e cada perda de organela é justificada como otimização funcional.

**Quando o REDATOR-E1 NEBLI deveria usar:** toda vez que descrever uma célula altamente especializada (hemácia, neutrófilo, plaqueta, plasmócito, hepatócito, neurônio). Em vez de "a hemácia não tem núcleo", a fórmula é "por que ela não tem núcleo? — porque X, porque Y, porque Z". **Gancho concreto:** sub-padrão dentro da Categoria 2 (Origem evolutiva/pergunta motivadora): "variante 'interrogação retórica + cadeia de consequências': pergunta de uma frase + 3+ consequências encadeadas com 'sem X, então Y'."

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro | Status | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **PRESENTE leve** | Q26 correta (B) tem 28 palavras com mecanismo; distratoras A/C/D/E variam 19–24 palavras — ratio ≤1.25 OK. Q27 (C) tem 47 palavras; outras 31–46 — OK. Q28 (E): correta 35 palavras, distratora A 38, B 36, C 33, D 34 — paridade exemplar. Q29 (A) 30 palavras; outras 23–30 — OK. Q30 (D) 38 palavras; outras 33–43 — OK. **Aplicação está dentro da regra**, mas Q26 tem distratora E (24 palavras) ligeiramente curta — atenção, não falha. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PRESENTE** | "HbA1c" usado em pág 12 sem footnote `#sigla` próprio (só aparece em contexto). "MBP" definida apenas no parágrafo (pág 19) sem footnote separado. "ICAM" mencionado apenas em Q5 da discursiva, não na E1. "PDGF" pág 23 — apenas glosa em parênteses, sem `#sigla`. "PTI", "CIVD" no box de trombocitopenia (pág 24) sem footnote. **Vários candidatos a footnote faltando.** |
| 3 | Subagentes Opus customizados falhando | N/A | Erro de pipeline, não de conteúdo do PDF. |
| 4 | Heredoc atômico ENAMETOOLONG | N/A | Erro técnico, não detectável no PDF. |
| 5 | `questao-ce` exige tupla | N/A | Não detectável; Q05/Q14/Q19/Q23 são CE e compilaram OK. |
| 6 | Termo-notas abaixo do alvo (alvo 6–8) | **PRESENTE** | Contagem de `#termo-nota` no .txt é difícil aferir (vira footnote no rodapé), mas pela frequência de footnotes numerados (1–28 ao longo do documento), o material está bem servido em **siglas** (≥20 footnotes) mas com **termos-nota densos faltando** para: diapedese, eritropoese, hemostasia, anafilaxia, glicação, opsonização. Contagem aparente: 3–4 termos-nota verdadeiros (rolling, varfarina, etc) — abaixo de 6–8. |
| 7 | Teto E1 errado (canônico 22 páginas) | **AUSENTE** | Etapa 1 ocupa páginas 3–26 = ~24 páginas, **acima do teto de 22**. Sem ter o tema-card à mão, mas o resumo extrapolou 22. Pendência a olhar — Davi pode achar que está bom (tema denso justifica), mas é desvio do canônico. |

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)

1. **Reescrever a "Cascata de coagulação em panorama" (pág 8)** em três passos numerados (gatilho/convergência/produto final) — é o único ponto onde a apostila quebra o próprio padrão e vira manual. Bloqueador para aluno-alvo. (Triangulação fornecida em §3.)
2. **Reduzir E1 de 24 para ≤22 páginas** comprimindo: (i) a cascata acima; (ii) o muro de subtipos de linfócito virando tabela; (iii) o vazio da pág 16 (Conclusão integradora da PARTE II) absorvido na própria PARTE III. Canônico atual é teto 22.
3. **Tabela de subtipos de linfócito** (B / T-CD4 / T-CD8 / NK × % + função-em-uma-frase) para descomprimir pág 21, que é o pico de carga cognitiva.

### MECANÍSTICO (max 3)

1. **Linhagem eritroide com ancoragem cromática** (basófilo = azul ribossomo, policromático = mistura, ortocromático = vermelho, reticulócito = restos de mRNA) — hoje os nomes são decoreba. (§3, parágrafo 2.)
2. **Citoesqueleto da hemácia em três camadas explícitas** (cabo/nó/âncora) — destrava esferocitose como consequência mecanística, não correlação. (§3, parágrafo 3.)
3. **Box clínico do HIV/AIDS** separado do parágrafo de subtipos de linfócito — hoje a fisiopatologia da AIDS aparece em-linha e perde valor; box destaca.

### DIDÁTICO (max 3)

1. **Termo-notas faltantes:** diapedese, eritropoese, hemostasia (primária × secundária), anafilaxia, glicação, opsonização — adicionar `#termo-nota` na 1ª aparição. Atinge o alvo 6–8.
2. **`#sigla()` faltantes:** HbA1c, MBP, PDGF, ICAM, PTI, CIVD — auditar e adicionar.
3. **Header desatualizado em pág 46**: "ETAPA 4 — FUNDAMENTOS" no runner do gabarito; Etapa 4 foi removida em 2026-05-22. Trocar para "GABARITO" ou "ETAPA 2 — OBJETIVAS".

### ESTÉTICO (max 3)

1. **Pág 16 vazia:** mover a conclusão integradora da PARTE II para o final da pág 15 (espaço sobra) ou absorver no abertura da PARTE III. Página em branco contamina percepção de qualidade.
2. **Variar o tique "te entrega/sai entendendo"** nas 3 conclusões integradoras — repete fórmula 3×.
3. **Gráfico de pizza de proteínas plasmáticas (pág 5)** é decorativo; substituir por tabela 4×2 (classe / função-síntese) ou remover — hoje só repete o que o texto já disse.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** SIM (com 3 técnicas extraídas em T3.9 que alimentam Phase F).
2. **≥1 recomendação ESTRUTURAL/MECANÍSTICO?** SIM (3 estruturais + 3 mecanísticas).
3. **Seção para refazer inteira?** Nenhuma. Apenas o parágrafo "Cascata de coagulação em panorama" (pág 8) precisa de reescrita pontual.
4. **Parágrafos para reescrever?** 3 — listados em §3 com triangulação completa: (i) cascata pág 8; (ii) linhagem eritroide pág 12; (iii) citoesqueleto pág 14.

---

[APROVAR COM RESERVAS]

— Reservas: encolher para ≤22 págs; reescrever 3 parágrafos identificados; auditar termos-nota e siglas faltantes; corrigir header pág 46.

<!-- FIM-REVISAO-PROFUNDA -->
