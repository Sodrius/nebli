# Revisão profunda Tier 3 — UC01-BC-20-estrutura-dos-acidos-nucleicos

**Tema (ancoragem):** Estrutura dos ácidos nucleicos (DNA/RNA — peças, polímero, dupla hélice, RNA, cromatina)
**Autor:** declarado "drive do CAOC", mas o PDF é NEBLI nativo (cabeçalho "NEBLI · APOSTILA", contato Davi). Tratado aqui como apostila histórica NEBLI para fins de calibração; conclusões servem igual à Phase F do REDATOR-E1.
**Personagem:** aluno FMUSP 1º ano, ensino médio + meses, **com dificuldade real** em biologia molecular.
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

## Ancoragem prévia (obrigatória)

- **Tema canônico (literal do slug):** Estrutura dos ácidos nucleicos.
- **3 conceitos centrais que eu-aluno quero aprender:**
  1. Por que DNA e RNA são "quase iguais" mas têm destinos tão diferentes.
  2. Como base, açúcar e fosfato se montam num nucleotídeo, e por que isso vira dupla hélice.
  3. Como 1,2 m de DNA cabem em 5 µm de núcleo (cromatina) sem virar nó.
- **2 temas vizinhos que NÃO são esse:** Replicação do DNA; Transcrição/Tradução. A apostila acena pra eles ("vamos retomar em Replicação", "aula 36"), mas o foco é estrutura — confirmação correta de escopo.

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Capa + sumário | OK | 1–2 | Promessa clara, capa sóbria, sumário cabe em 1 pág. Aluno entra calmo. |
| Intro Etapa 1 | OK | 3 | Frase de abertura "um único átomo de oxigênio" é gancho concreto — aluno engata. |
| 1.1 Bases (purina/pirimidina) | OK | 3–4 | Mnemônicos "GA"/"CUT" + box "Tamanho não é só estética" + tabela. Aluno sai com modelo mental. |
| 1.2 Pentoses (2'-OH) | OK | 5–6 | Apresenta o 2'-OH como "personagem que volta" — bom recurso narrativo. |
| 1.3 Nucleosídeo vs nucleotídeo | OK | 6–7 | Box "nucleotídeos têm vida dupla" amarra ATP/AMPc cedo. |
| 2.1 Fosfodiéster + 5'→3' | **[STOP: pág 8]** | 8 | Página 8 do PDF é texto + nota de rodapé sobre figura "Representação de um polinucleotídeo" mas a figura **não aparece**: o txt menciona legenda na linha 257 ("Representação de um polinucleotídeo. Cada açúcar (S)..."), porém a renderização da pág. 8 mostra ~50% de página em branco abaixo de "Sai água, sobra polímero." Aluno fica esperando o desenho que nunca chega. Conceito de "extremidade 5'-fosfato livre" sem suporte visual = bloqueio. |
| 2.2 Dupla hélice / Watson-Crick | OK | 9–10 | Reapresenta tamanho + Hbond — boa redundância intencional. Box doxorrubicina dá ancoragem clínica. |
| 2.3 Tm + hipercromismo + superenovelamento | parcial | 11–12 | "Hipercromismo" introduzido com mecanismo de empilhamento — bom. Mas superenovelamento entra no último parágrafo só pra "fechar"; topoisomerases viram nome solto. |
| 3.1 2'-OH revisitado | OK | 13 | Promessa cumprida — retoma o personagem com mecanismo completo (nucleófilo → fosfato → cliva). Estabilidade espelhada DNA/RNA exposta de forma simétrica. |
| 3.2 Famílias de RNA | OK | 14–15 | tRNA em trevo, ribozima. Box antibióticos ribossomais ancora clinicamente. |
| 3.3 Cromatina (níveis 1–4) | **[STOP: pág 16]** | 16 | "Nível 3 — alças e domínios" é um parágrafo de 4 linhas que diz literalmente "este nível é difícil de visualizar mas é importante". Aluno-em-dificuldade lê isso como "pula" — e pula. O nível 3 fica oco; o salto 30 nm → cromossomo metafásico fica sem ponte mental. |
| Conclusão integradora | OK | 18 | Três fios (economia / mecanismo escondido / geometria) — excelente síntese de alto nível. |
| **Resumindo** | **[STOP: pág 19]** | 19 | Página 19 do PDF (renderização visual): muro de texto em 2 colunas, leading apertado, 12 seções espremidas. Aluno-em-dificuldade vê parede e fecha. Compare com Resumindo bem-respirado: deveria ser 1 pág com 8–10 blocos, ou 2 págs com leading confortável. |
| Q01–Q30 | OK | 20–30 | Enunciados claros. Paridade de distratoras boa (ver §9). |
| Q1–Q5 discursivas | OK | 31–33 | Modelos completos. Q5 (erro conceitual ribossomo vs aaRS) é exemplar — pega o tipo de confusão exata que persiste. |
| Gabarito | OK | 34 (PDF: 37) | Página dedicada, layout limpo. |

**Dois STOPs estruturais:** pág. 8 (figura prometida ausente / página meio-vazia) e pág. 19 (Resumindo como muro). Um STOP didático: pág. 16 (nível 3 da cromatina elidido).

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria invocada:** "Abertura por pergunta ingênua + escala física concreta" (típica EXEMPLARES) e "Personagem que volta" (recurso narrativo).

### Parágrafo NEBLI-histórico — abertura da Etapa 1 (pág. 3)

> "Quase tudo o que importa numa célula passa, em algum momento, por uma fita de DNA ou de RNA. O DNA guarda a receita; o RNA executa. Os dois são polímeros longuíssimos feitos de peças muito parecidas — tão parecidas que a diferença entre elas cabe num único átomo de oxigênio, e essa diferença minúscula é o que decide se a molécula vai durar décadas dentro do núcleo ou ser destruída em minutos no citoplasma."

**Análise:** abre com função ("guarda a receita / executa") + paradoxo concreto ("um átomo de oxigênio"). Não usa jargão técnico antes do gancho. Cria o personagem (2'-OH) que reaparece em 3.1 — antecipação genuína, não enrolação. **Equivalente a exemplar canônico** (compara bem com "abertura por analogia macroscópica" usada em Membrana Plasmática / Citoesqueleto).

### Parágrafo problemático — Resumindo (pág. 19), seção "Estabilidade química espelhada"

> "DNA é atacado por ácido (quebra ligação N-glicosídica purina-açúcar) e resistente a base. RNA é resistente a ácido e hidrolisado por base diluída (graças ao 2'-OH). Propriedades espelhadas que caem em prova nesse formato exato."

**Análise:** aqui o NEBLI-histórico cai no vício de "decoreba travestida de explicação" — o "graças ao 2'-OH" pressupõe o mecanismo da seção 3.1 sem retomá-lo em 1 frase. No Resumindo, que é a ferramenta de fechamento e revisão pré-prova, o aluno tem que voltar 6 páginas pra entender de novo. EXEMPLARES.md de Resumindo bem-feito sempre tem **mecanismo embutido em 1 frase**, não só etiqueta. **Reescrita:** "RNA é hidrolisado por base diluída porque o 2'-OH desprotonado vira nucleófilo e ataca o próprio fosfato vizinho; DNA não tem esse OH, então é imune a base."

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo fraco #1 — Nível 3 da cromatina (pág. 17, txt linhas 528–531)

**(a) Citação literal:**
> "Nível 3 — alças e domínios. A fibra de 30 nm forma alças ancoradas em uma matriz proteica. Cada alça pode ter dezenas de milhares de pares de base. Esse nível é difícil de visualizar mas é importante: ele organiza o DNA em domínios funcionais dentro do núcleo, e diferentes regiões de um cromossomo podem ter destinos diferentes (mais ou menos expressos)."

**(b) Diagnóstico mecanístico:** o autor reconhece a dificuldade ("difícil de visualizar mas é importante") e **resolve abandonando o aluno**. Não há mecanismo, não há analogia macroscópica, não há figura. O nível 3 é literalmente "tem alças, sei lá, são importantes". Para o aluno-em-dificuldade que vinha bem em níveis 1–2, isso quebra a confiança: se o autor não consegue explicar, eu sou burro por não entender. Resultado: STOP da pág. 16.

**(c) Reescrita pronta:**
> "Nível 3 — alças ancoradas. Imagine a fibra de 30 nm como um fio de telefone bem grosso. Ele não fica solto no núcleo: a cada ~50.000 pares de base, esse fio é grampeado numa estrutura proteica chamada matriz nuclear — como um varal que sustenta lençóis longos. Cada 'lençol' é uma alça (loop), e cada alça é tratada pela célula como uma unidade funcional: a célula pode abrir uma alça inteira para transcrição, ou manter outra fechada e silenciosa. É o equivalente cromossômico de organizar livros em estantes — sem as estantes, os livros existiriam, mas você não acharia nenhum."

### Parágrafo fraco #2 — Pág. 8, transição para fosfodiéster + figura ausente

**(a) Citação literal (txt 242–245 + 254–259):**
> "Temos a peça. Agora, como construir o polímero? A célula precisa 'soldar' um nucleotídeo no próximo, e a solda que ela usa se chama ligação fosfodiéster. O nome é descritivo: é um fosfato que faz dupla ligação éster — uma para o C5 de um açúcar e outra para o C3 do açúcar seguinte. Sai água, sobra polímero. [...legenda referenciada...] Representação de um polinucleotídeo. Cada açúcar (S) é conectado ao próximo via um fosfato (P)..."

**(b) Diagnóstico mecanístico:** a pág. 8 do PDF tem ~50% de espaço em branco abaixo do parágrafo "Sai água, sobra polímero." A legenda da figura aparece **na pág. 9**, sem a figura na pág. 8 e sem indicação de overflow. Aluno lê "Sai água, sobra polímero" esperando ver o desenho que justifica o "5'→3'" — a próxima frase é puramente abstrata ("E aqui aparece uma consequência sutil mas central: como o fosfato sempre liga 5' a 3'..."). Sem visual, "5' vs 3'" vira string vazia. Falha **estrutural**, não estética: a página foi paginada errado.

**(c) Reescrita pronta:** mover a figura de polinucleotídeo (com legenda "ponta 5'-fosfato livre / ponta 3'-OH livre" destacada) para ANTES da frase "E aqui aparece uma consequência sutil". Texto novo de transição: "Olhe a figura: repare como o fosfato (P) sempre liga o C5' (acima) de um açúcar ao C3' (abaixo) do próximo. Na ponta de cima, sobra um fosfato sem par — é a extremidade 5'. Na ponta de baixo, sobra um OH sem par — é a extremidade 3'. A fita inteira é, por construção, assimétrica."

### Parágrafo fraco #3 — Superenovelamento (pág. 12, txt linhas 388–394)

**(a) Citação literal:**
> "Uma última observação sobre estabilidade, importante quando o DNA é circular (como em plasmídeos bacterianos ou em DNA mitocondrial): o número de voltas da hélice por unidade de comprimento pode variar. Se a célula introduz voltas a mais ou a menos do que o natural (10 bases/volta), a molécula gera tensão e se torce sobre si mesma — fenômeno chamado superenovelamento. Enzimas chamadas topoisomerases controlam essa tensão e são alvo de antibióticos importantes (quinolonas, como ciprofloxacino, inibem topoisomerases bacterianas)."

**(b) Diagnóstico mecanístico:** o conceito de superenovelamento é parachuted em 5 linhas no fim da seção 2.3. Não há analogia (corda telefônica? mangueira de jardim?), não há figura, não há "por que isso importa pro aluno agora" — o gancho clínico (ciprofloxacino) entra em meia-linha. Aluno lê e fica com a sensação "ok, anotei o nome", sem modelo mental. Para tema de "estrutura dos ácidos nucleicos", superenovelamento merece ou um parágrafo de mecanismo de verdade, ou ser cortado (replicação cobre depois).

**(c) Reescrita pronta:**
> "Última propriedade física: o DNA pode ficar 'enrolado demais' ou 'enrolado de menos'. Pense num cabo de telefone espiralado. Se você dá voltas a mais antes de soltar, ele se torce sobre si mesmo formando alças visíveis — superenovelamento positivo. Se você dá voltas a menos, ele afrouxa e fica mais fácil de separar as duas fitas — superenovelamento negativo. No DNA circular de bactérias e da mitocôndria, esse parâmetro é regulado ativamente por enzimas chamadas topoisomerases, que cortam uma fita, permitem rotação e religam. Por que isso importa? Quinolonas (como ciprofloxacino, antibiótico de uso diário em UTI) inibem a topoisomerase bacteriana — sem topoisomerase, o cromossomo bacteriano não replica e a bactéria morre."

---

## 4. T3.3 — 3 seções mais densas (com mitigação)

| Seção | Densidade observada | Mitigação concreta |
|---|---|---|
| **2.3 Tm + hipercromismo + superenovelamento** (pág. 11–12) | Mistura três conceitos físico-químicos heterogêneos (Tm/curva, hipercromismo, superenovelamento) em ~2 páginas. Aluno engasga em qual é o protagonista. | Quebrar em 2.3a (Tm + curva, com box "Tm cai em prova nesse formato exato") e 2.3b (superenovelamento + topoisomerase, com analogia do cabo telefônico). Mover hipercromismo para dentro de 2.3a como subseção pequena ("efeito ótico da denaturação"). |
| **3.2 Famílias de RNA** (pág. 14–15) | mRNA, tRNA, rRNA + estrutura em trevo + L 3D + ribozima + antibióticos ribossomais em 2 páginas. Boa, mas tRNA fica abstrato sem figura própria das alças. | Garantir que a figura "Estrutura em trevo do tRNA" tenha legenda apontando explicitamente para "alça do anticódon" e "extremidade 3'-CCA com aminoácido". Como está agora (txt 469–471), a legenda é descritiva mas o aluno precisa adivinhar onde é cada parte. |
| **Conclusão integradora** (pág. 18) | 3 fios narrativos abstratos (economia, mecanismo escondido, geometria) sem âncoras concretas. Forma muito boa mas demanda que o aluno já tenha digerido tudo. | Cada fio deveria abrir com 1 exemplo concreto do próprio resumo antes da abstração. Ex.: "Primeiro fio — economia: 4 bases, 1 troca (T↔U), 1 oxigênio (2'-OH presente/ausente) geram dois universos funcionais. [continua]". |

---

## 5. T3.4 — Voz fora do padrão

**Padrão NEBLI canônico:** diálogo, segunda pessoa do singular, mecanismo antes do nome, pergunta ingênua.

**Citações dentro do padrão (positivo):**
- "Aqui está a pergunta que provavelmente já passou pela sua cabeça: por que uma diferença tão pequena gera dois polímeros tão diferentes?" (pág. 5)
- "Pense no problema geométrico que a dupla hélice precisa resolver." (pág. 4)
- "Como é que a célula resolve isso?" (pág. 16)

**Citações fora do padrão (problemáticas):**
- "Anote bem isso" (pág. 4, sobre 2 vs 3 pontes de H) — voz de cursinho, não diálogo NEBLI. NEBLI diria "guarde esse número, ele volta na seção 2.3 transformado em Tm".
- "Vale registrar uma coisa que cai em prova com frequência" (pág. 7) — meta-comentário sobre prova. NEBLI evita isso fora dos boxes "Por que isso importa fora do laboratório".
- "Propriedades espelhadas que caem em prova nesse formato exato" (Resumindo, pág. 19) — meta-prova de novo, no Resumindo, onde já é tarde para esse tipo de aviso.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô identificada:** **2.3 Estabilidade física (Tm + hipercromismo + superenovelamento)**, págs. 11–12. Razão: é o ponto onde o resumo deixa o registro mecanístico-visual (purinas, açúcares, fosfodiéster) e entra no físico-químico (Tm em curva, hipercromismo em espectrofotômetro, topologia em DNA circular). Três modelos mentais novos em ~2 páginas sem ancoragem clínica forte além do ciprofloxacino solto.

**3 mitigações possíveis:**

1. **Cortar superenovelamento** desta aula (mover para Replicação, onde topoisomerase é protagonista). Ganho: 2.3 vira só Tm + hipercromismo, coeso.
2. **Box "Termômetro do DNA"** consolidando: "Tm = ponto de meio-derretimento. GC manda mais que A=T. Hipercromismo é só o jeito de medir (UV 260 nm aumenta 30–40%). Curva de denaturação é o gráfico canônico." Aluno teria 1 caixa pra revisar antes da prova.
3. **Figura do gráfico de Tm com duas curvas sobrepostas** (uma rica em GC, outra rica em AT, eixo x temperatura, eixo y absorbância) — converte o conceito em imagem. Hoje o resumo só descreve a curva (txt 370–372) sem mostrá-la.

**Escolha:** **mitigação 1 + 3** combinadas. Cortar superenovelamento limpa a página; figura de Tm comparativa dá ancoragem visual ao conceito mais provável de cair em prova. Box (mitigação 2) é redundante com a Síntese 6 já existente.

---

## 7. T3.8 — ANÁLISE VISUAL (do PDF)

| Sub-item | Observação |
|---|---|
| **Hierarquia tipográfica** | Bem definida: títulos de PARTE em navy bold grande, seções (1.1, 1.2) em navy bold menor, corpo em Merriweather serifado. Header "NEBLI" cinza claro + breadcrumb à direita ("ETAPA 1 — TEXTO DIDÁTICO"). Aluno se localiza fácil. **Bom.** |
| **Valor pedagógico das figuras** | 10 imagens no resumo (estrutura JSON). Pág. 4 tem caixa lateral azul-clara com mnemônico "1. Bases Nitrogenadas / Pirimidinas (C,U,T) / Purinas (A,G)" — figura **resumitiva e decorativa**, não estrutural (não mostra o anel duplo vs simples que o texto promete!). Falha de oportunidade pedagógica. Pág. 8 menciona figura de polinucleotídeo mas a página está meio vazia (figura possivelmente caiu na 9, quebrando o fluxo). **Mediano com falhas estruturais.** |
| **Densidade visual (respiro)** | Pág. 8 com 50% em branco → falta de figura prometida. Pág. 19 (Resumindo) é o oposto: 2 colunas justificadas com leading apertado, sem respiro entre seções de cores diferentes. **Inconsistente — ou sobra ou falta.** |
| **Uso de cor** | Box vermelho-claro "vida dupla" (pág. 8) e box verde-claro "Resumindo até aqui" (pág. 8) e box azul-claro "Síntese 3" (pág. 8) coexistem na mesma página → 3 cores de boxes diferentes em 1 página confunde a leitura. Aluno não sabe se "vermelho = atenção" ou "vermelho = curiosidade". Resumindo (pág. 19) usa barra navy/dourada no topo — coerente com capa. **Cores intencionais existem mas a semântica não está fixa.** |
| **Cortes/overflow** | Pág. 8 (figura ausente / página meio vazia, possível overflow para pág. 9). Resumindo (pág. 19) — risco de overflow comprimido em 1 página em vez de 2 confortáveis (canônico 2026-05-20 flexibiliza). **Dois pontos de fricção visível.** |

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas — ALIMENTA Phase F)

### Técnica 1 — "Personagem que volta" (callback de mecanismo)
**Citação literal:**
> "Em condições normais isso não acontece, mas se o meio ficar levemente alcalino, ou se a temperatura subir, esse 2'-OH ataca o fosfato e a fita se rompe. O RNA, em outras palavras, carrega dentro de si o mecanismo de sua própria destruição. [...] **Vamos retomar essa lógica com mais cuidado na seção 3.1, agora que a peça está dissecada.**" (pág. 5–6, depois cumprido em pág. 13)

**Nome da técnica:** **callback antecipado de mecanismo** — apresentar uma peça mecânica resumida cedo, prometer retomada profunda depois, e cumprir a promessa.

**Quando NEBLI deveria usar (gancho para REDATOR-E1):** sempre que uma peça molecular tem **dupla aparição** (uma estrutural, uma funcional/clínica). Ex.: lançadeira do malato em gliconeogênese (mencionar em PARTE I no transporte de elétrons, retomar em PARTE III no mecanismo de bypass); biotina em carboxilases (mencionar em PARTE I como cofator, retomar quando ovos crus aparecem clinicamente). Regra: **se você diz "vamos retomar na seção X", seção X TEM que retomar literalmente, com novo nível de detalhe.**

### Técnica 2 — "Conclusão por fios narrativos" (não por bullet list)
**Citação literal:**
> "Olhando para o caminho que percorremos, três fios amarram toda a história. O primeiro é a economia de peças: a célula constrói duas moléculas radicalmente diferentes em função (arquivo permanente versus mensagem descartável) usando essencialmente os mesmos componentes [...] O segundo fio é o do mecanismo escondido em detalhes que parecem cosméticos [...] O terceiro fio é o da geometria como condição de função." (pág. 18)

**Nome da técnica:** **conclusão por fios temáticos** (3 lentes que reorganizam o conteúdo retrospectivamente, sem repetir bullets).

**Quando NEBLI deveria usar:** **substituir a Conclusão integradora padrão** ("vimos que X, Y, Z") por 3 fios temáticos quando o tema tem natureza unificadora forte. Templates de fios úteis: (a) economia / paralelismo / contraste molecular, (b) mecanismo escondido em detalhe estrutural, (c) geometria como restrição e solução, (d) tempo / meia-vida / regulação temporal, (e) hierarquia de escala. Para REDATOR-E1: incluir no Tema Card Seção C uma sugestão de 2–3 fios candidatos, e deixar o REDATOR escolher na hora de escrever a Conclusão.

### Técnica 3 — "Pergunta ingênua antecipada na voz do aluno"
**Citação literal:**
> "Aqui está a pergunta que provavelmente já passou pela sua cabeça: por que uma diferença tão pequena gera dois polímeros tão diferentes?" (pág. 5)

E em:
> "Por que essa divisão importa tanto? Pense no problema geométrico que a dupla hélice precisa resolver." (pág. 4)

**Nome da técnica:** **antecipação de pergunta ingênua na voz do aluno** — não "vamos discutir", mas "a pergunta que você está fazendo é X".

**Quando NEBLI deveria usar:** abrir todo segundo ou terceiro parágrafo de uma seção com uma pergunta nessa forma, sempre que o tópico tenha um "porquê não-óbvio" no centro. Diferença em relação ao NEBLI atual: hoje o REDATOR-E1 já faz perguntas, mas tipicamente abstratas ("Por que isso acontece?"). A técnica do histórico é mais forte porque atribui a pergunta ao aluno ("que você está fazendo", "que já passou pela sua cabeça") — quebra a quarta parede e faz o aluno se sentir antecipado.

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro NEBLI canônico | Status nesta apostila | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação (Q26–Q30) | **AUSENTE** (calibrado bem) | Q26: correta D tem 18 palavras, distratoras 12–15 palavras. Q28: correta E ~30 palavras, distratoras 15–25. Q30: correta A 22 palavras, distratoras 15–18. Razão correta/maior-distratora ≤ 1.5 em todas. **Esta apostila acertou paridade — virou exemplar positivo.** |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PARCIAL** | DNA, RNA, ATP, GTP, AMPc, GMPc, PCR, Tm, mRNA, tRNA, rRNA, UV: todos declarados como footnotes na 1ª aparição (txt confirma). **CCA** (sequência terminal do tRNA, pág. 14) aparece sem expansão — aluno-em-dificuldade vê "sempre a sequência CCA na extremidade 3'" sem saber que é citosina-citosina-adenina. **HDAC** (pág. 17 box clínico) aparece como "HDAC inhibitors" sem footnote. **70S/80S/30S/50S** (pág. 15 box antibióticos) aparecem sem explicar o que significa o "S" (unidade Svedberg de sedimentação). Total: 3 siglas faltando. |
| 3 | Subagentes Opus customizados falhando | **N/A** | Esta é uma apostila histórica, não foi gerada pelo pipeline subagentado atual. Não testa o fix de 2026-05-25. |
| 4 | Heredoc atômico `ENAMETOOLONG` | **N/A** | Erro de produção, não de output. |
| 5 | `questao-ce` exige tupla `("I", [conteúdo])` | **N/A** (compilou) | Estrutura compilou — Q03, Q06, Q12, Q16, Q20, Q24, Q27 são CE e renderizam OK. |
| 6 | Termo-notas abaixo do alvo (alvo 6–8) | **PRESENTE** (limite inferior) | Contando `#termo-nota` no texto: ligação N-glicosídica, ligação fosfodiéster, denaturação, histonas, **4 termos-nota**. Alvo 6–8 → faltam ~2–4. Candidatos óbvios não-marcados: **antiparalelo**, **nucleófilo / ataque nucleofílico**, **superenovelamento**, **ribozima**, **hipercromismo**, **operon**, **aminoacil-tRNA-sintetase**. Erro #6 do checklist NEBLI **confirmado**. |
| 7 | Teto E1 errado (canônico atual 22 págs) | **N/A** (não há Tema Card visível) | Resumo total = 34 págs; E1 = págs 3–18 = **16 págs**. Dentro do teto 22. **OK.** |

**Sumário de calibração:** 2 erros confirmados (siglas faltando + termo-notas abaixo), 1 com calibração positiva (paridade distratoras — copiar para futuros resumos), 4 N/A.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Paginação da pág. 8 quebrada.** A figura "Representação de um polinucleotídeo" precisa estar NA pág. 8, junto da introdução da ligação fosfodiéster, não na pág. 9. O REDATOR-E1 deve forçar `figura-nebli(..., largura: 65%)` imediatamente antes do parágrafo "E aqui aparece uma consequência sutil" para garantir adjacência. **Regra geral acionável:** sempre que uma frase do corpo referenciar "Olhe a figura / veja como / repare que", a figura tem que estar na mesma página renderizada — validação visual obrigatória do compilador.
2. **Resumindo da pág. 19 está comprimido demais em 1 coluna.** 12 seções em 2 colunas com leading apertado vira muro. Canônico 2026-05-20 permite 2 páginas — usar. Para REDATOR-E1: se Resumindo tem >10 seções OU se alguma seção tem >35 palavras, **default = 2 páginas confortáveis**, não 1 página apertada.
3. **Nível 3 da cromatina elidido com "difícil de visualizar".** Sempre que o redator se ouvir escrevendo "isso é difícil de visualizar mas é importante", o gatilho deve ser: parar, voltar, achar analogia macroscópica. Adicionar essa regra ao § "anti-armadilhas" do redator-e1.md.

### MECANÍSTICO (max 3)
1. **Mecanismo do 2'-OH atacando o fosfato (3.1) está nominalmente correto mas não desenhado.** O conceito de "intermediário cíclico 2',3'-fosfato" só aparece no modelo da Q2 discursiva (pág. 32) — deveria estar no corpo da seção 3.1, com seta curva representando o ataque. Aluno-em-dificuldade não monta esse mecanismo só com texto.
2. **Superenovelamento entra como nome solto.** Não explicar mecanismo se não for explicar de verdade — corte ou aprofunde. Recomendação: cortar e mover para Replicação.
3. **"O fosfato faz dupla ligação éster" (pág. 8)** — o aluno não sabe o que é "ligação éster" (química orgânica fora do ensino médio). Adicionar footnote ou reescrita: "ligação éster é uma ligação química entre um ácido e um álcool; aqui o ácido é o fosfato e os álcoois são os OHs do açúcar — uma de cada lado, daí o 'di-éster'."

### DIDÁTICO (max 3)
1. **Aumentar termo-notas de 4 → 7.** Adicionar nominalmente: antiparalelo, nucleófilo, ribozima.
2. **Substituir "anote bem isso" / "vale registrar que cai em prova" por callbacks mecanísticos.** Voz NEBLI canônica não usa imperativos de cursinho.
3. **Reescrita do Resumindo "estabilidade espelhada"** com mecanismo embutido (ver §2 reescrita).

### ESTÉTICO (max 3)
1. **Padronizar semântica de cores dos boxes.** Definir: vermelho = armadilha/atenção; verde = síntese/resumo até aqui; azul = curiosidade clínica; dourado = Resumindo. Documentar no `typst-template/CLAUDE.md`.
2. **Caixa azul "1. Bases Nitrogenadas" da pág. 4 é decorativa redundante** — repete o que o corpo já disse. Substituir por figura estrutural mostrando o anel duplo da purina vs anel simples da pirimidina (a diferença que o texto promete e nunca mostra direito).
3. **Gabarito (pág. 34/37) tem 2 colunas implícitas mas alinhamento dos códigos fica torto** (Q03 CECC alinha com Q08 D mas Q07 B alinha com Q12 CCEE) — usar tabela explícita.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM, com 2 ressalvas.** A apostila acerta narrativa, callbacks, paridade de distratoras, conclusão por fios — use como exemplar canônico para essas técnicas. **Ressalvas:** pág. 8 (figura ausente) e pág. 19 (Resumindo comprimido) NÃO devem ser usadas como modelo.

2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM** — 3 estruturais (paginação pág. 8, Resumindo apertado, nível 3 oco) e 3 mecanísticos (2'-OH sem seta, superenovelamento solto, ligação éster sem prerrequisito).

3. **Seção para refazer?** **Seção 3.3 nível 3 da cromatina** (reescrita acima em §3 #1). Seção 2.3 (superenovelamento) — recomendado **cortar**, não refazer.

4. **Parágrafos para reescrever?** **3:**
   - Pág. 17, "Nível 3 — alças e domínios" (reescrita pronta em §3 #1).
   - Pág. 12, parágrafo do superenovelamento (reescrita pronta em §3 #3 — ou cortar e mover).
   - Pág. 19 Resumindo, seção "Estabilidade química espelhada" (reescrita pronta em §2).

---

[APROVAR COM RESERVAS]
