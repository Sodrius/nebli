# Lições para o REDATOR-NEBLI — Phase F

**Data:** 2026-05-25
**Insumo:** 66 relatórios (33 T2 Sonnet + 33 T3 Opus) sobre o corpus de 33 apostilas históricas NEBLI em `arquivos-trabalho/apostilas-historicas/`.
**Propósito:** converter a meta-análise (`META-ANALISE-APOSTILAS-HISTORICAS.md`) em **diffs literais** prontos para colar nos system prompts dos agents NEBLI (`redator-e1.md`, `questionador.md`), no `CLAUDE.md`, no `EXEMPLARES.md`, e no `errosComuns_nebli.md`.

A meta-análise descreve **o que está no mundo**. Este arquivo descreve **o que mudar no próximo resumo NEBLI**.

---

## 1. Aprendizados acionáveis para REDATOR-E1

### 1.1 — Rotacionar os 5 registros canônicos entre subtópicos vizinhos [NOVA REGRA]

**Evidência (problema):**
- `UC01-FMEMB-06-transmissao-sinaptica`: "estrutura idêntica nas 9 seções torna leitura previsível a partir da metade"
- `UC01-BC-05-compartimentos-iii`: "não muda de ritmo entre seções bioquímicas e casos clínicos graves"
- `UC01-BIOQ-17-ciclo-de-krebs`: "PARTE II tem registro repetitivo entre as etapas 3–8"

**Diagnóstico:** o REDATOR-E1 internalizou "abertura por pergunta ingênua" como receita única. Em PDFs de 9+ subtópicos, o aluno entra em piloto automático na metade.

**Texto canônico pronto para colar em `redator-e1.md` (nova regra 10 ou anexa à regra de abertura):**

```markdown
### Rotação obrigatória de registro entre subtópicos vizinhos

Subtópicos consecutivos NÃO podem abrir no mesmo registro. Rotacione entre os 5 registros canônicos:

1. **Enquadramento** — abre nomeando o problema concreto que o subtópico resolve ("a célula precisa decidir se entra em mitose ou para")
2. **Integração-anterior** — abre conectando ao subtópico imediatamente anterior ("agora que a coesina está em duplicata, separar as cromátides exige...")
3. **Integração-posterior** — abre antecipando o subtópico seguinte ("o que vamos ver aqui é o gatilho que o próximo subtópico vai amplificar")
4. **Analogia concreta** — abre por imagem cotidiana mapeada ao mecanismo ("imagine um zíper com a chave perdida — é assim que...")
5. **Ponto-de-quebra** — abre por confusão antecipada ("aluno tende a achar que X — é exatamente o oposto")

**Verificação:** em E1 com 9 subtópicos (3 por PARTE), nenhum par vizinho de subtópicos pode abrir no mesmo registro. Se o REDATOR-E1 escrever 3 subtópicos consecutivos em "enquadramento", refazer o do meio em outro registro.
```

### 1.2 — Conclusão integradora obrigatoriamente em 4 camadas [REGRA REVISADA]

**Evidência (problema):**
- `UC01-FMEMB-03-potencial-de-repouso`: "síntese clínica (digoxina, hipercalemia) fica nos boxes da E1 mas não reaparece na Conclusão"
- `UC01-BIOQ-14-glicolise`: "Conclusão sem camada clínica/projeção para Krebs"
- `UC01-BIOQ-04-aminoacidos`: "falta 4ª camada prospectiva ligando ao próximo resumo (proteínas I)"

**Diagnóstico:** o REDATOR-E1 fecha a conclusão em "estrutura → mecanismo → clínica" (3 camadas). A 4ª camada (projeção/continuidade) é canônica no `redator-e1.md` como **opcional** — promover a obrigatória.

**Texto canônico pronto para colar em `redator-e1.md` (substituir a regra atual de conclusão):**

```markdown
### Conclusão integradora — 4 camadas obrigatórias

A `#conclusao-box(...)` ao fim da E1 DEVE costurar 4 camadas explícitas, nesta ordem:

1. **Princípio unificador** — qual ideia central atravessa as 3 PARTES?
2. **Mecanismo nuclear** — em 1-2 frases, o "como" mais importante.
3. **Clínica retomada** — uma das doenças citadas nos boxes da E1 reaparece NA CONCLUSÃO, com 1 frase de mecanismo (não só nome).
4. **Projeção para o próximo resumo** — frase explícita conectando ao tema seguinte. Ex: "o que aprendemos aqui sobre membrana é o palco de tudo que o próximo resumo (transporte) explica como acontece".

A camada 4 é o que diferencia um resumo isolado de uma **apostila** que conta uma história ao longo da UC. Sem ela, o aluno fecha o PDF e não sabe por que aquele tema importa para o próximo.

**Verificação:** o REDATOR-E1 declara explicitamente as 4 camadas no comentário acima da `#conclusao-box`. Falta de qualquer camada bloqueia o resumo.
```

### 1.3 — Box anti-confusão com título-negação como helper canônico [NOVA REGRA + NOVO HELPER]

**Evidência (acerto que está vazando como técnica não-formalizada):**
- `UC01-FMEMB-04-passivas`: "Despolarização não é inversão" — formato exemplar
- `UC01-BC-02-citoesqueleto`: "Cinesina-Cresce/Dineína-Direto" — mnemônica anti-armadilha
- `UC01-BIOQ-02-ph-e-tampoes`: "Ka/pKa inversos" sugerido virar helper canônico
- `UC01-BC-07-divisao-celular`: "Box de inversão de polaridade" — aluno acha X, é o oposto

**Diagnóstico:** o REDATOR-E1 já escreve esses boxes ad-hoc, mas como `#atencao-box` genérico. Falta um sub-padrão canônico que force a estrutura "aluno acha X → na verdade Y → razão mecanística".

**Proposta de helper novo (a implementar no `typst-template/nebli_v2_apostila.typ`):**

```typst
#confusao-prevista(
  titulo: [Despolarização não é inversão],
  aluno_acha: [aluno acha que despolarizar significa o interior virar positivo, espelhando a polaridade externa],
  mecanismo: [na verdade, "despolarizar" significa SAIR DO REPOUSO — pode ser ficar menos negativo (de -70 para -50) ou, em casos extremos, virar positivo (overshoot). Inversão de polaridade é uma sub-categoria rara de despolarização.],
)
```

**Texto canônico para `redator-e1.md` (nova seção):**

```markdown
### Helper `#confusao-prevista()` — quando usar

Use `#confusao-prevista()` em vez de `#atencao-box` quando o aviso é especificamente sobre uma confusão antecipável do aluno (não sobre uma armadilha de prova nem sobre uma exceção mecanística).

Diferença canônica:
- `#atencao-box` → exceção mecanística OU contraste útil
- `#confusao-prevista` → aluno tende a entender ERRADO de uma forma específica
- `#sentinela-box` → distinguir o subtópico de algo vizinho (não-confundir)

Cota: 1-2 `#confusao-prevista` por PARTE. Mais que isso vira ruído.

Título da confusão DEVE ser uma negação curta ("X não é Y") ou uma equação errada nomeada ("Ka × pKa = constante? Não."). Título descritivo sem negação ("Sobre a despolarização") quebra o propósito.
```

### 1.4 — Clínica inline entre travessões [NOVA REGRA]

**Evidência (acerto não-formalizado):**
- `UC01-BIOQ-04-aminoacidos`: "Fármaco-âncora inline (warfarina, loratadina em 8-12 palavras entre travessões) — NEBLI tende a guardar para Etapa 2/clinica-box"
- `UC01-BIOQ-18-cadeia-respiratoria`: "Clínica injetada em 1 frase — apoptose por cit c, hipóxia histotóxica por CN⁻, sem virar box"

**Diagnóstico:** o REDATOR-E1 hoje empacota TODA clínica em `#clinica-box`. Mas o autor que faz isso bem (de novo: o próprio Davi em alguns resumos) intercala 1-2 fármacos/casos inline em 8-12 palavras, sem caixa. Isso dá densidade clínica sem quebrar o fluxo da prosa.

**Texto canônico para `redator-e1.md`:**

```markdown
### Clínica inline (entre travessões)

Nem toda clínica precisa virar `#clinica-box`. Use **inline entre travessões** quando:

- O fármaco/caso é colateral à argumentação principal (ex: enquanto se explica o mecanismo da hemoglobina, citar "—a anemia falciforme nasce de uma única troca de glutamato por valina na cadeia β—" entre travessões).
- A integração não exige mecanismo expandido (1-2 frases bastam).
- Quebrar o fluxo para uma caixa interromperia a cadeia causal central.

Use `#clinica-box` quando:

- A clínica EXIGE 4-6 linhas de mecanismo (cadeia causal completa).
- A clínica é o ponto-pivô do subtópico (não colateral).
- O caso é uma cápsula auto-suficiente que merece destaque visual.

**Meta:** ≥3 clínicas inline + 2-3 `#clinica-box` por PARTE. Hoje a maioria dos resumos NEBLI tem 0 clínicas inline e 4-5 caixas — o equilíbrio está errado.
```

### 1.5 — Mini-resumo encadeado com setas ao fim de cada subseção [REGRA REVISADA]

**Evidência (acerto):**
- `UC01-FMEMB-04-passivas`: "Mini-resumo encadeado com setas — 2-4 linhas em cadeia causal ao fim de cada subseção; hoje NEBLI só faz Resumindo no fim"
- `UC01-BIOQ-14-glicolise`: "Resumindo aritmético com a conta visível (4-2=+2 ATP)"
- `UC01-BIOQ-11-enzimas-ii`: "Resumindo até aqui terminando com 3-4 pares droga-alvo nominais"

**Diagnóstico:** a regra atual T2.8 pede `#mini-resumo` em parágrafos >5 linhas, mas com fórmula variável. O padrão "X → Y → Z" + 3-4 pares concretos NÃO está nos exemplos canônicos. Promover.

**Texto canônico para `redator-e1.md` (revisão da T2.8 existente):**

```markdown
### Mini-resumo encadeado — fórmula preferencial

`#mini-resumo` ao fim de cada subseção (não só dos parágrafos >5 linhas) DEVE preferir a fórmula **cadeia causal com setas**:

```
Em resumo: ATP — ADP+Pi → energia disponível → contração muscular → calor residual.
```

Ou variantes equivalentes:
- "Em uma frase: ..."
- "Se você só lembrar: X → Y → Z"
- "O que ficou de pé: 4 pares droga-alvo (AAS-COX, penicilina-transpeptidase, AZT-transcriptase, DFP-AChE)"
- "Resumindo aritmético: 4 ATP − 2 ATP = +2 ATP líquido por glicose"

Evite o formato "Em resumo, vimos que..." seguido de parágrafo longo recapitulando — vira repetição.

**Verificação:** se 3 mini-resumos consecutivos usam a MESMA fórmula, rotacionar. Variação rítmica > monotonia.
```

### 1.6 — Pré-requisito retomado em 1 frase pronta no Tema Card [REGRA REVISADA + MUDANÇA NO ORQUESTRADOR]

**Evidência (problema):**
- `UC01-BIOQ-03-lipideos`: "Box SDR usa Lei de Laplace sem retocar tensão superficial"
- `UC01-FMEMB-05-conducao-impulso`: "screening eletrostático em §3.3 p.30"
- `UC01-FMEMB-03-potencial-de-repouso`: "derivação de Nernst introduz potencial químico/ln/zF sem justificar"

**Diagnóstico:** o REDATOR-E1 com baseline "aluno sabe pouco" ainda usa Lei de Laplace, Nernst, ΔG como se conhecidos. O Tema Card Seção C deveria listar pré-requisitos NOMINAIS com 1 frase de retomada pronta para o REDATOR-E1 colar.

**Texto canônico para `orquestrador.md` (adição ao Tema Card Seção C):**

```markdown
### Seção C — Pré-requisitos cruzados com frase-âncora pronta

Para cada pré-requisito que aparece NESTA aula e não foi detalhado no resumo NEBLI imediatamente anterior, listar:

| Pré-requisito | Frase-âncora pronta para colar (≤25 palavras) |
|---|---|
| Lei de Laplace | "Lei de Laplace: para uma esfera, a tensão na parede é proporcional ao raio e à pressão interna; quanto menor a esfera, maior a tendência ao colapso." |
| Nernst | "Equação de Nernst: o potencial de equilíbrio de um íon depende da razão entre concentrações externa e interna; quanto maior a razão, mais o potencial empurra o íon para dentro ou para fora." |
| ΔG | "ΔG mede se uma reação ocorre espontaneamente; ΔG negativo libera energia, ΔG positivo precisa de input para acontecer." |

Mínimo 3 pré-requisitos com frase-âncora por Tema Card. O REDATOR-E1 cola essa frase na 1ª aparição do conceito.
```

### 1.7 — Cadeia ≥5 atores SEM figura = bloqueio [REGRA REVISADA + CHECK AUTOMATIZADO]

**Evidência (problema):**
- `UC01-BIOQ-11-enzimas-ii`: "cascata AMPc-PKA SEM figura (viola canônico)"
- `UC01-FMEMB-08-sinalizacao-celular`: "pág 18 sem figura (535 palavras, mais densa do PDF)"
- `UC01-BC-06-nucleo`: "figura de fluxo Ran-GTP/GDP ausente"

**Diagnóstico:** a regra "cadeia multi-passo enzimática (≥5 reações) = figura obrigatória" do `redator-e1.md` está sendo violada em pontos críticos. Faltam: (a) figura disponível no MAPA; (b) o REDATOR esqueceu de chamar.

**Texto canônico para `redator-e1.md` (revisão da regra existente):**

```markdown
### Cadeia ≥5 atores = figura obrigatória — verificação automatizada

Em todo parágrafo da E1 que contém ≥4 setas (`→`, `->`, `=>`) ou ≥5 atores nominais conectados causalmente:

1. ANTES de redigir, consultar `figuras/[tema]/MAPA_CONTEUDO.txt` por uma figura de cascata correspondente.
2. Se não houver, sinalizar ao ORQUESTRADOR e parar; o ORQUESTRADOR deve extrair slide adicional OU criar SVG esquemático em `figuras/[tema]/SVG/cascata-X.svg`.
3. O parágrafo DEVE conter `#figura-nebli(...)` referenciada explicitamente ("veja o esquema abaixo", "compare com o diagrama") imediatamente antes ou depois.

**Check automatizado (a implementar em `precompile-check.py`):** contar setas e atores nominais por parágrafo. Se ≥4 setas sem `#figura-nebli` adjacente, bloquear pipeline.
```

---

## 2. Aprendizados acionáveis para QUESTIONADOR

### 2.1 — Paridade Q26–Q30: redigir as 5 distratoras ANTES da correta [GATE HARD]

**Evidência (problema):**
- `UC01-BIOQ-16-gliconeogenese`: "correta 70 palavras vs distratoras 25-30, ratio ≈ 2.8"
- `UC01-FMEMB-01-compartimentos-e-homeostase`: "ratios 2.4-5.2"
- `UC01-BC-07-divisao-celular`: "Q28 com ratio 1.73 e Q30 com ratio 1.49"

**Diagnóstico:** **erro #1 do `errosComuns_nebli.md`**, confirmado em ~17/33 PDFs. A regra é canônica mas não está sendo enforçada. Promover de "regra" para "gate hard" no QUESTIONADOR.

**Texto canônico para `questionador.md` (substituir a regra atual de paridade):**

```markdown
### Paridade de distratoras em E2 Aplicação — gate hard

Para Q26–Q30 (Aplicação), redigir nesta ordem **obrigatória**:

1. **Primeiro, escrever as 5 distratoras com 25-35 palavras CADA**, contendo mecanismo plausível-mas-errado. Cada distratora deve nascer de uma confusão antecipável (do Mapa de Confusões).
2. **Só DEPOIS escrever a alternativa correta**, com tamanho ≤ 1.25× a maior distratora.
3. Calcular o ratio antes de fechar: `len(correta_palavras) / max(len(distratora_i_palavras) for i in [1..4])` ≤ 1.25.

**Check automatizado (a implementar em `precompile-check.py`):** para Q26-Q30, contar palavras de cada alternativa e calcular ratio. Se ratio > 1.25, exit 1.

**Razão da inversão de ordem:** quando o QUESTIONADOR escreve a correta primeiro, ela inflada de mecanismo (porque ele sabe a resposta certa e quer ser completo); as distratoras nascem encolhidas porque ele já gastou o mecanismo na correta. Invertendo a ordem, o QUESTIONADOR é forçado a investir mecanismo em CADA distratora.
```

### 2.2 — Distratoras nascem do Mapa de Confusões, não de simulação [REGRA REFORÇADA]

**Evidência (acerto que precisa virar regra):**
- `UC01-FMEMB-06-transmissao-sinaptica`: "Box-armadilha 'X mas não Y' com prova experimental embutida"
- `UC01-BIOQ-08-hemoglobina-i-e-ii`: "Box farmacológico de inversão (sildenafil/PDE5)"

**Diagnóstico:** distratoras genéricas ("a glicose é convertida em proteína") são pedagogicamente nulas. Distratoras boas nascem de confusões REAIS do aluno-alvo, documentadas no `mapa-confusoes/<slug>.md`.

**Texto canônico para `questionador.md`:**

```markdown
### Distratoras com origem rastreável no Mapa de Confusões

Cada distratora de Q26-Q30 DEVE poder ser mapeada a uma entrada do `mapa-confusoes/<slug>.md`. Formato no comentário acima da questão:

```
// Q27 - distratoras:
// A) confusão #3 do mapa (aluno acha que glicogenólise libera glicose direto no sangue)
// B) confusão #7 do mapa (G6P sai como glicose-1-fosfato — erro de etapa)
// C) confusão #11 (acha que glucagon ativa a glicogênio sintase)
// D) confusão #15 (confunde fígado com músculo na via)
// E) CORRETA
```

Se uma distratora não tem origem no mapa, REDIGIR uma nova entrada do mapa AGORA com nome + descrição mecanística do erro + origem (banco NEBLI #ID | livro-texto | armadilha clínica).

**Verificação:** ≥80% das distratoras Q26-Q30 devem ter referência rastreável.
```

### 2.3 — Box farmacológico com cadeia mecanística como sub-padrão [NOVO SUB-PADRÃO]

**Evidência (acerto):**
- `UC01-BIOQ-08-hemoglobina-i-e-ii`: "Box de aterramento clínico (armadilha diagnóstica + conduta + diagnóstico definitivo em 4-6 linhas)"
- `UC01-FMEMB-08-sinalizacao-celular`: "Box farmacológico de inversão para inibidores (sildenafil/PDE5 + milrinona + teofilina)"

**Texto canônico para `questionador.md` (E3 — discursivas):**

```markdown
### Q4-Q5 da E3 — preferir cenário farmacológico com cadeia mecanística

Quando o tema permite, Q4 ou Q5 da E3 deve apresentar um cenário farmacológico onde a resposta-modelo encadeia:

1. **Apresentação clínica** (1-2 frases): paciente, sintoma, contexto.
2. **Mecanismo bioquímico/molecular subjacente** (3-4 frases): por que essa droga age.
3. **Inversão/contraste** (1 frase): "se fosse outro fármaco, a cadeia seria...".
4. **Conduta** (1 frase): qual decisão clínica decorre.

Total ≤130 palavras. O aluno aprende a costurar mecanismo molecular com decisão clínica em 5 minutos de leitura.

Exemplos no corpus histórico: sildenafil/milrinona/teofilina (PDE5/3/4), digoxina/cólera (bomba Na/K e SRO), warfarina/Vit K (γ-carboxilação).
```

---

## 3. Novos exemplares positivos para `EXEMPLARES.md`

### Exemplar A — "Pergunta bactéria↔eucarionte" (Categoria 2 — Abertura)

**Origem:** `UC01-BC-06-nucleo`, parágrafo de abertura do subtópico 1.1.

**Citação completa** (a recuperar do PDF na compilação):

> "Por que toda célula eucariótica gasta energia para manter o material genético separado do citoplasma, enquanto bactérias funcionam bem sem essa separação? A resposta começa com uma incompatibilidade temporal: nas eucarióticas, a transcrição produz um RNA imaturo que precisa ser editado antes de virar mRNA funcional — e essa edição não pode acontecer no meio da tradução, ou ribossomos começariam a ler RNA errado. O envelope nuclear é a solução: separa o lugar onde se escreve do lugar onde se lê."

**Quando usar:** qualquer tema que introduz uma estrutura/processo eucariótico que tem equivalente procarionte simples. Mecanismo: o contraste cria tensão didática antes de resolver.

**Onde inserir no `EXEMPLARES.md`:** Categoria 2 (Aberturas), entre os exemplares de "pergunta ingênua" e "promessa de Pareto 70%".

### Exemplar B — "Mantra de 3 perguntas portáteis na conclusão" (Categoria 12 — Conclusão)

**Origem:** `UC01-BIOQ-15-introducao-ao-metabolismo`, conclusão integradora.

**Citação completa** (a recuperar):

> "Resumindo a essência: a partir de agora, sempre que você ver uma reação metabólica, faça três perguntas. Onde está o ATP? Onde estão os elétrons (NADH, FADH₂)? Por que essa reação é espontânea? Essas três perguntas portáteis vão te acompanhar pela Glicólise, Krebs, β-oxidação e toda a fosforilação oxidativa. Não tente decorar as vias; tente ouvi-las respondendo essas perguntas."

**Quando usar:** em resumos fundacionais (introdução a metabolismo, introdução a sinalização, introdução a transporte). Mecanismo: dá ao aluno uma régua para auto-avaliar o resto do conteúdo da UC.

**Onde inserir no `EXEMPLARES.md`:** Categoria 12, como exemplar do tipo "régua portátil".

### Exemplar C — "Patologia em parágrafo único com cadeia causal completa" (Categoria 9 — Integração clínica)

**Origem:** `UC01-BIOQ-05-proteinas-i`, p.18, anemia falciforme.

**Citação completa** (a recuperar):

> "A anemia falciforme ilustra todo o argumento. Uma única troca na cadeia β da hemoglobina — ácido glutâmico (carregado, hidrofílico) por valina (neutra, hidrofóbica) na posição 6 — cria uma alça hidrofóbica fora-do-lugar. Em condições desoxigenadas, essa alça encaixa em um sulco da molécula vizinha, e moléculas começam a se polimerizar em fibras longas. As fibras deformam o eritrócito em foice, que fica rígido e fica preso em capilares. Resultado: dor isquêmica aguda e hemólise crônica. Tudo isso por uma única troca de aminoácido."

**Quando usar:** quando há uma patologia que ilustra ESTRUTURA → FUNÇÃO → CONSEQUÊNCIA do tema. Mecanismo: substitui o `#clinica-box` decorado por um parágrafo de fluxo causal contínuo.

**Onde inserir no `EXEMPLARES.md`:** Categoria 9, como exemplar do tipo "cadeia causal patológica".

### Exemplar D — "Resumindo aritmético" (Categoria 8 — Mini-resumos)

**Origem:** `UC01-BIOQ-14-glicolise`, fim de cada subseção.

**Citação completa** (típica):

> "Resumindo aritmético: investimos 2 ATP na fase preparatória, ganhamos 4 ATP na fase de payoff, líquido = 4 − 2 = +2 ATP por glicose. Mais 2 NADH na GAPDH que ainda vão para a cadeia respiratória."

**Quando usar:** ao fim de subseções de metabolismo onde há balanço energético. Mecanismo: a conta visível ancora o número que o aluno vai precisar lembrar na P2.

**Onde inserir no `EXEMPLARES.md`:** Categoria 8, como variante específica do `#mini-resumo` aritmético.

---

## 4. Novas entradas para `errosComuns_nebli.md`

Promover de descobertas pontuais a checklist canônico:

### Erro #8 — Header "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" fantasma no gabarito

**Descrição:** após remoção canônica da Etapa 4 em 2026-05-22, o helper de gabarito continuou imprimindo o header "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" em todos os PDFs gerados depois. Páginas afetadas: gabarito da E2 (última seção do PDF). Confirmado em 13/33 PDFs do corpus histórico.

**Como evitar:** corrigir o helper `gabarito-page` em `typst-template/nebli_v2_apostila.typ` removendo a referência hardcoded a "ETAPA 4". Auditor `auditar_pdf.py` deve falhar se `grep "ETAPA 4" output.txt` retornar match no PDF final.

### Erro #9 — Gabarito da E2 em layout de colunas embaralhadas

**Descrição:** helper `gabarito-page` falha em chunking quando contagens de categoria não são múltiplas de 5. Resultado: Q06 depois de Q08, classificações fora-de-grade. Em casos extremos (`UC01-BC-07-divisao-celular`), o gabarito impresso marca letra DIFERENTE da alternativa correta do enunciado — 13/30 questões erradas, **risco pedagógico bloqueador**.

**Como evitar:** refatorar `gabarito-page` para 1 coluna vertical com agrupador de categoria, OU forçar largura fixa por coluna. Verificação automatizada já existe (`verificar_gabarito_ordem.py`) mas não está integrada ao pipeline de resumos (só ao de cadernos).

### Erro #10 — Cadeia ≥5 atores SEM figura

**Descrição:** parágrafos da E1 com 4+ setas causais (`→`/`->`/`=>`) sem `#figura-nebli` adjacente. Caso clássico: cascata AMPc-PKA, RTK-Ras-MAPK-ERK, Ran-GTP-GDP. Confirmado em 11/33 PDFs.

**Como evitar:** check no `precompile-check.py` contando setas por parágrafo da E1; ≥4 setas sem `#figura-nebli` adjacente → bloquear.

### Erro #11 — Vocabulário de prova nos boxes ("cai em prova", "pegadinha")

**Descrição:** boxes com voz prescritiva-de-prova em vez de mecanística. Termos vazando: "cai em prova", "pegadinha clássica", "memorize", "regra de ouro para a P2", "dica clínica". Existe regra T2.6 mas vaza em ~10/33 PDFs.

**Como evitar:** `grep -i 'prova\|pegadinha\|examinador\|cai em\|memorize' etapa1.typ` deve retornar 0. Adicionar ao `precompile-check.py`.

### Erro #12 — Conclusão integradora travada na camada 3

**Descrição:** `#conclusao-box` costura "estrutura → mecanismo → clínica" mas falta a 4ª camada (projeção/continuidade para o próximo resumo). Confirmado em 13/33 PDFs.

**Como evitar:** REDATOR-E1 declara em comentário acima da `#conclusao-box`: "Camadas: (1) ..., (2) ..., (3) ..., (4) ...". Se faltar a 4, refazer. Ver §1.2 deste documento.

### Erro #13 — Variação de registro homogênea entre subtópicos vizinhos

**Descrição:** subtópicos consecutivos abrem no mesmo registro canônico. Texto fica previsível. Confirmado em 22/66 menções.

**Como evitar:** declarar registros no Tema Card Seção B (subtópicos) e ROTACIONAR. Ver §1.1.

### Erro #14 — Numeração de página inflada (helper conta Etapa 4 fantasma)

**Descrição:** rodapé do PDF mostra "44" em PDF de 41 páginas reais — helper conta páginas-fantasma da Etapa 4 removida. Confirmado em 4+ PDFs.

**Como evitar:** `counter(page).update(<atual>)` no fim da E3 (último elemento real do PDF) para resetar a contagem antes do gabarito.

### Erro #15 — Capa exibindo "Bloco: P2" violando regra canônica

**Descrição:** o helper de capa renderiza campo de bloco/prova ("Bloco: P2 — Função 1") mesmo após o `CLAUDE.md` proibir explicitamente. Confirmado em `BIOQ-13-carboidratos`.

**Como evitar:** 1 if no helper de capa removendo qualquer referência a bloco/prova/turma. Reforçar com `grep -E 'Bloco:|P[123]\s|Turma' arquivos-trabalho/capa-render.txt == 0`.

---

## 5. Auto-crítica calibrada — onde NEBLI está bom, onde ainda está pior

### NEBLI atual está **bom** (replicar e não mexer):

- **Abertura por pergunta ingênua** em ~28/33 PDFs (T2.1 score ≥4 em 85%).
- **Mecanismo antes do nome técnico** em ~30/33 (T2.2 score ≥4 em 90%).
- **Voz dialógica consistente** em ~32/33 (T2.5 score ≥4 em 97%) — esse é o maior diferencial competitivo do NEBLI.
- **Mini-resumos sistemáticos** em ~28/33 (T2.8 score ≥4 em 85%).
- **`#sigla()` na 1ª aparição** está sendo executada bem em ~16/33 PDFs (~50%) — viés é cobertura excessiva (>10 footnotes), não falta.
- **Boxes mecanísticos** sem decorrência de prova em ~25/33 (T2.6 score ≥4 em 75%).

### NEBLI atual ainda **pior** que algum histórico (priorizar conserto):

- **Paridade de distratoras Q26-Q30:** ~17/33 PDFs violam. **Prioridade #1.**
- **Cadeia ≥5 atores SEM figura:** ~11/33 PDFs. **Prioridade #2 (especialmente em sinalização e metabolismo).**
- **4ª camada da conclusão (projeção):** ~13/33 não têm. **Prioridade #3.**
- **Rotação de 5 registros:** ~22/33 menções de homogeneidade. **Prioridade #4.**
- **Bugs de template (ETAPA 4, capa, numeração):** afeta TODO PDF gerado pós-2026-05-22. **Prioridade ZERO (correção mecânica, custo nulo).**

---

## 6. Diff de prompt sugerido — patches literais

### Patch 1: `redator-e1.md` — adicionar 4 regras

**Lugar:** ao fim da seção "Regras inegociáveis" (atualmente 9 regras).

```diff
+ ### Regra 10 — Rotação de 5 registros entre subtópicos vizinhos
+
+ Subtópicos consecutivos NÃO podem abrir no mesmo registro. Rotacione entre: (1) enquadramento, (2) integração-anterior, (3) integração-posterior, (4) analogia concreta, (5) ponto-de-quebra. Em E1 com 9 subtópicos, nenhum par vizinho compartilha registro. (Ver `LICOES-PARA-REDATOR-NEBLI.md` §1.1 para detalhes.)
+
+ ### Regra 11 — Conclusão integradora em 4 camadas obrigatórias
+
+ `#conclusao-box` DEVE costurar: (1) princípio unificador, (2) mecanismo nuclear, (3) clínica retomada (com mecanismo, não só nome), (4) **projeção para o próximo resumo** (frase explícita). A camada 4 era opcional; é obrigatória a partir de 2026-05-25.
+
+ ### Regra 12 — Box anti-confusão usa `#confusao-prevista()` com título-negação
+
+ Quando o aviso é especificamente sobre confusão antecipável (não exceção mecanística), use o helper `#confusao-prevista(titulo, aluno_acha, mecanismo)`. Título DEVE ser negação curta ("X não é Y") ou equação errada nomeada. Cota: 1-2 por PARTE.
+
+ ### Regra 13 — Clínica inline entre travessões + `#clinica-box` se denso
+
+ Nem toda clínica vira `#clinica-box`. Use inline entre travessões quando a clínica é colateral à argumentação (1-2 frases bastam). Use box quando a cadeia causal exige 4-6 linhas. Meta: ≥3 inline + 2-3 box por PARTE.
```

### Patch 2: `questionador.md` — substituir regra de paridade

**Lugar:** seção "Paridade intra-questão ±25%".

```diff
- ### Paridade intra-questão ±25%
-
- As 5 alternativas de cada Q26-Q30 devem ter tamanho equivalente, com tolerância de ±25%.

+ ### Paridade Q26-Q30 — gate hard
+
+ Para Q26-Q30 (Aplicação), redigir nesta ordem obrigatória:
+ 1. Escrever as 5 DISTRATORAS PRIMEIRO, cada uma com 25-35 palavras + mecanismo plausível-mas-errado rastreável ao Mapa de Confusões.
+ 2. Só DEPOIS escrever a CORRETA, com tamanho ≤ 1.25× a maior distratora.
+ 3. Calcular ratio = len(correta) / max(len(distratoras)). Se ratio > 1.25, refazer.
+ Verificação automatizada: `precompile-check.py` falha se ratio > 1.25 em qualquer Q26-Q30.
```

### Patch 3: `CLAUDE.md` — adicionar nova entrada em "Erros comuns conhecidos"

```diff
+ ## Erros comuns conhecidos (canônico 2026-05-25, ampliado de 7 para 15)
+
+ Ver `memory/errosComuns_nebli.md` para a lista completa. Os 8 erros novos (erros #8-#15) descobertos via meta-análise dos 33 PDFs históricos cobrem:
+ - Bugs determinísticos de template (header ETAPA 4 fantasma, gabarito embaralhado, numeração inflada, capa com bloco/prova).
+ - Regras canônicas vazando (cadeia ≥5 sem figura, vocabulário de prova, conclusão em só 3 camadas, registro homogêneo).
+ Detalhes em `arquivos-trabalho/LICOES-PARA-REDATOR-NEBLI.md` §4.
```

### Patch 4: `precompile-check.py` — adicionar 4 checks novos

```diff
+ # T1.9 — ETAPA 4 fantasma no gabarito (canônico 2026-05-25)
+ if "ETAPA 4" in extract_pdf_text("output.pdf"):
+     errors.append("ETAPA 4 fantasma no PDF; corrigir helper gabarito-page")
+
+ # T1.10 — Vocabulário de prova nos boxes
+ banned = re.findall(r'\b(prova|pegadinha|examinador|cai em|memorize)\b', etapa1_txt, re.I)
+ if banned:
+     errors.append(f"Vocabulário de prova em etapa1.typ: {banned[:3]}")
+
+ # T1.11 — Paridade Q26-Q30
+ for q in re.findall(r'#questao\(.*?\)', etapa2_txt, re.DOTALL)[25:30]:
+     alts = parse_alternatives(q)
+     ratio = len(alts['correta'].split()) / max(len(a.split()) for a in alts['distratoras'])
+     if ratio > 1.25:
+         errors.append(f"Q{idx}: paridade ratio {ratio:.2f} > 1.25")
+
+ # T1.12 — Cadeia ≥4 setas sem figura
+ for para in etapa1_txt.split("\n\n"):
+     arrows = para.count("→") + para.count("->") + para.count("=>")
+     if arrows >= 4 and "#figura-nebli" not in surrounding_context(para):
+         errors.append(f"Cadeia com {arrows} setas sem figura: {para[:80]}...")
```

---

## 7. Aprendizado meta para Claude (sobre como conduzir tarefas semelhantes)

Notas para sessões futuras de auto-calibração ou análise em massa de artefatos NEBLI:

1. **PDFs ditos "externos" no NEBLI são, na maioria, output do próprio pipeline.** Sempre conferir cabeçalho/rodapé antes de presumir autoria externa. Isso muda o framing da análise de "auditoria de competidores" para "auto-calibração".

2. **`pdftoppm` em sandbox restrito limita análise visual.** Em sessões futuras, ou (a) usar PyMuPDF para renderizar PNGs em pasta gravável e Read os PNGs, ou (b) confiar em metadata estrutural JSON + texto extraído como proxy. Davi já tem `pdftoppm` mas o sandbox bloqueou em ~40/66 chamadas.

3. **Spawn de subagents customizados não funciona em runtime.** Agentes definidos em `.claude/agents/` durante uma sessão NÃO são carregados; só os do session-start. Workaround: `general-purpose` com `model` override e prompt inline lendo um `_prompt-canonico.md` do disco.

4. **Quotas Opus saturam em ~10-15 chamadas paralelas pesadas.** Estratégia: alternar batches Sonnet/Opus, fazer T2 Sonnet primeiro em todos os slugs, depois T3 Opus. Resgatar quota Opus se possível antes de partir para meta-análise.

5. **Batches de 6 paralelos podem causar socket errors.** Sweet spot foi 4 paralelos. Em sessões futuras, default para 4, escalar para 6 só se as 2 primeiras rodadas passaram limpas.

6. **Checkpoint a cada 30min é vital.** Salvou o estado quando Opus saturou às 16h e voltou às 19h — sem checkpoint eu teria perdido a noção do que já estava feito.

7. **A meta-análise vale mais que os 66 relatórios individuais.** ROI da Phase E + F é 10× maior do que o ROI das análises por slug. Em sessões futuras, alocar 30-40% do orçamento total para Phase E + F, não 10%.

---

## 8. Próximos passos sugeridos (não-executados)

1. Aplicar Patch 1 em `.claude/agents/redator-e1.md` (4 regras novas).
2. Aplicar Patch 2 em `.claude/agents/questionador.md` (gate hard de paridade).
3. Aplicar Patch 3 em `CLAUDE.md` (referência aos 8 erros novos).
4. Aplicar Patch 4 em `typst-build/precompile-check.py` (4 checks novos).
5. Corrigir `typst-template/nebli_v2_apostila.typ`: remover header "ETAPA 4" do helper de gabarito; refatorar `gabarito-page` para 1 coluna vertical; corrigir `counter(page).update()` ao fim da E3; suprimir bloco/prova/turma na capa.
6. Implementar helper `#confusao-prevista()` em `nebli_v2_apostila.typ`.
7. Atualizar `memory/errosComuns_nebli.md` ampliando de 7 para 15 erros.
8. Adicionar 4 exemplares novos em `EXEMPLARES.md` (§3 deste documento).
9. Regerar 1-2 PDFs do corpus (ex: `BIOQ-16-gliconeogenese` que foi o 2º pior) com os patches aplicados e comparar.

Davi decide a ordem; nenhum dos passos foi executado nesta sessão — todos os artefatos são propostas com texto canônico pronto para colar.
