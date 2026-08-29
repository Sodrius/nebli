# TEMA CARD — imuno-06-sistema-complemento

## Seção A — Escopo

- **Tema (título de capa):** Sistema complemento
- **Slug:** `imuno-06-sistema-complemento`
- **Disciplina / componente:** Imunologia (UC03 — Princípios do Desenvolvimento das Doenças)
- **Slide-fonte:** Apresentação em PDF da videoaula "IM — Sistema Complemento", 60 páginas → `figuras/imuno-06-sistema-complemento/` (60 PNGs + MAPA_CONTEUDO.txt)
- **Onde estudar:** Abbas — *Imunologia Celular e Molecular* (10ª ed., cap. 13) · Janeway/Murphy — *Immunobiology* (10ª ed., cap. 2) · Roitt — *Fundamentos de Imunologia* (13ª ed., cap. 4)
- **Alvo de páginas da E1:** piso 2, **teto 22** · alvo prático 17–21
- **`profundidade: fundo`** — Davi pediu explicitamente "um nível um pouco acima do da prova". Dial `fundo` (CLAUDE.md § Profundidade 2026-07-12 item 2): mais injeção mecanística por subtópico, limiar de admissão afrouxado, blocos clínicos maiores.
- **Recorte slide × tema:** coincidem. O slide cobre exatamente o arco reconhecimento → fase enzimática → fase destrutiva, mais funções, receptores, regulação e deficiências. Nada do slide fica de fora; o degrau a mais entra *dentro* desse escopo.

### Calibração UC03 (passo 2b — `consultar.py --slug imuno-06-sistema-complemento`)

25 subquestões do acervo (2015–2025). **Teto histórico desta aula:** interpretar CH50/AH50 e dosagem de C3/C4 para localizar em qual via está o defeito; ligar deficiência de via alternativa a infecção por encapsulados; ligar fator H/I a consumo de C3 e microangiopatia renal; escolher qual via foi ativada pelo tempo de infecção (precoce → alternativa/lectinas; tardia → clássica, dependente de anticorpo); listar funções efetoras perdidas numa deficiência.

**A E1 vai um degrau acima em:** (a) o tioéster intramolecular do C3/C4 — *por que* a opsonina gruda covalentemente e por que o raio de ação é curto; (b) a decisão próprio × estranho por densidade de ácido siálico e recrutamento de fator H, e não por "reconhecimento" ativo; (c) os três níveis de freio (iniciação, convertase, MAC) com o mecanismo de cada regulador; (d) C3b → iC3b como *reetiquetagem* (perde convertase, ganha CR3/CR4); (e) C3d–CR2 como amplificador do limiar do linfócito B; (f) a leitura mecanística de CH50 × AH50 × C3 × C4 como localizador de defeito.

**Contrato:** nada do acervo vai colado no PDF — nem enunciado, nem menção a exame anterior, nem número de bloco. A calibração só diz *até onde* aprofundar.

### Prioridades desta corrida (do § Diário de revisões do MEMORY.md)

1. **`biocel-07` (peso alto, ativa): "sem slide ≠ sem figura"; tema com coreografia espacial exige figura.** Aqui há slide e o tema é todo espacial (montagem de convertase na superfície, poro do MAC, âncora de GPI) — **16 figuras planejadas, ≥3 por PARTE**, com tabela auditável no fechamento.
2. **ERROS #23 (C/E sorteado antes da redação):** a sequência C/E vai ser lida **item a item depois de escritas as assertivas**, e só então a guarda anti-degeneração age reescrevendo assertiva — nunca trocando letra no gabarito.
3. **ERROS #20 (`#termo-nota` com termo repetido):** auto-check antes de fechar a E1.
4. **ERROS #16 / F3 (excesso de caixa vermelha):** cota 1 `atencao-box` + 1 `confusao-prevista` por PARTE; o resto vira prosa dialogada.

---

## Seção B — Esqueleto das 3 PARTES

### PARTE I — Reconhecimento: três portas para a mesma cascata

- **1.1 A lógica da cascata: zimogênio, clivagem e convertase**
  Proteína inativa no plasma → clivagem em fragmento *a* (pequeno, difunde) e *b* (grande, gruda) → o *b* ancorado vira protease que cliva o próximo → amplificação em série. Onde o sistema é produzido (fígado + monócito, endotélio, dendrítica) e por que isso importa na resposta de fase aguda.
  *Figuras:* `slide-06` (58%) — a lógica genérica; `slide-05` (66%) — as três vias convergindo em recrutamento, opsonização e morte.
- **1.2 Via clássica: o anticorpo já ligado é o gatilho**
  C1 = C1q + 2×C1r + 2×C1s, dependente de Ca²⁺. C1q precisa de **dois** Fc vizinhos: dois IgG lado a lado, ou **um** IgM pentamérico que muda de conformação planar para grampo ao ligar antígeno. C1s cliva C4 → C4b (gruda) + C4a; depois C2 → C4b2a, a C3 convertase clássica.
  *Figuras:* `slide-09` (68%) — IgG × IgM; `slide-20` (48%) — a cadeia até a C3 convertase.
- **1.3 Via das lectinas: o açúcar do micróbio no lugar do anticorpo**
  MBL e ficolinas são colectinas com a mesma arquitetura de buquê do C1q; MASP-1/2 fazem o papel de C1r/C1s. Reconhecem manose e N-acetilglicosamina terminais — açúcares que a glicoproteína própria esconde sob ácido siálico e galactose. Mesma C3 convertase, sem anticorpo, sem espera.
  *Figura:* `slide-30` (72%).
- **1.4 Via alternativa: a vigilância que nunca desliga**
  Hidrólise espontânea contínua do tioéster do C3 → C3(H₂O), que se comporta como C3b e liga fator B; fator D cliva B → Ba + Bb; nasce a convertase de fase fluida C3(H₂O)Bb. Properdina estabiliza. É sondagem permanente, não "via de reserva".
  *Figura:* `slide-23` (72%).

### PARTE II — Fase enzimática: C3, amplificação, MAC e os freios

- **2.1 C3 e o tioéster: por que a opsonina gruda de verdade**
  Ligação tioéster interna escondida no C3 nativo; a clivagem expõe o carbono eletrofílico, que reage em microssegundos com hidroxila ou amina da superfície → ligação covalente. Se não achar alvo, hidrólise inativa. Daí o raio de ação curto e a deposição restrita à superfície ativadora.
  *Figura:* `slide-22` (70%).
- **2.2 A alça de amplificação e a decisão próprio × estranho**
  C3b + fator B + fator D → C3bBb, que gera mais C3b, que gera mais convertase. A superfície própria carrega ácido siálico e glicosaminoglicanos que recrutam fator H → dissociação e degradação; a bacteriana não carrega → a convertase sobrevive. A "escolha" é cinética, não cognitiva.
  *Figura:* `slide-26` (56%).
- **2.3 Da C5 convertase ao complexo de ataque à membrana**
  Um C3b extra acoplado à C3 convertase muda a especificidade do sítio → C4b2a3b / C3bBb3b clivam C5. C5b recruta C6, C7 (insere), C8 (fura) e polimeriza 10–18 C9 → poro. Poro sublítico em célula nucleada sinaliza em vez de matar.
  *Figura:* `slide-27` (56%).
- **2.4 Os freios: onde a cascata é desligada em cada nível**
  Iniciação: C1-INH (e sua ação sobre calicreína/FXIIa). Convertase: DAF/CD55 (acelera dissociação), MCP/CD46 e fator H (cofatores do fator I). Fluido: carboxipeptidase N inativa anafilatoxinas. Membrana: CD59 barra a polimerização de C9. Tudo ancorado por GPI nas duas últimas.
  *Figuras:* `slide-49` (72%); `slide-51` (50%); `slide-53` (55%).

### PARTE III — Fase efetora: o que os fragmentos fazem no tecido

- **3.1 Opsonização e os receptores de complemento**
  C3b/C4b → CR1; iC3b → CR3/CR4. Tabela nativa dos quatro receptores + C3aR/C5aR + C1qRp (padrão Exemplar 16). Sinergia com FcγR.
  *Figura:* `slide-36` (76%) + `table()` com header navy.
- **3.2 Anafilatoxinas: C3a, C4a e C5a**
  Desgranulação de mastócito, vasodilatação, permeabilidade, quimiotaxia de neutrófilo, indução de moléculas de adesão, ativação da NADPH oxidase. Potência C5a ≫ C3a ≫ C4a; carboxipeptidase N como freio.
- **3.3 Remoção de imunocomplexos e de células mortas**
  C3b intercala e quebra a rede (solubilização); CR1 da hemácia transporta até fígado e baço, onde o macrófago retira o complexo e devolve a hemácia. C1q, MBL, iC3b e C4b opsonizam corpo apoptótico.
  *Figura:* `slide-38` (62%).
- **3.4 A ponte com o linfócito B: C3d, CR2 e o co-receptor**
  C3d ligado ao antígeno + CR2(CD21) no complexo CD19/CD21/CD81 → baixa o limiar de ativação do linfócito B em 100–1000×; célula folicular dendrítica retém antígeno opsonizado no centro germinativo.
  *Figura:* `slide-43` (62%).
- **3.5 O mapa das deficiências: onde a falha aparece**
  Início da via clássica (C1q, C4, C2) → lúpus e depósito de imunocomplexo; C3 → piogênicas + imunocomplexo; C5–C9, properdina, fator D → *Neisseria*; C1-INH → angioedema hereditário; fator H/I → consumo de C3 e microangiopatia renal; CD55+CD59 (âncora de GPI) → hemoglobinúria paroxística noturna. Leitura de CH50 × AH50 × C3 × C4.
  *Figura:* `slide-54` (68%).

**Cadeia multi-passo ≥5 reações → figura obrigatória:** via clássica (`slide-20`), via alternativa (`slide-23`), MAC (`slide-27`), degradação do C3b (`slide-51`). Todas cobertas.

---

## Seção B.bis — Registro de abertura por subtópico

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | ponto-de-quebra |
| 1.3 | integração-anterior |
| 1.4 | analogia concreta |
| 2.1 | ponto-de-quebra |
| 2.2 | integração-anterior |
| 2.3 | enquadramento |
| 2.4 | analogia concreta |
| 3.1 | integração-anterior |
| 3.2 | enquadramento |
| 3.3 | ponto-de-quebra |
| 3.4 | integração-posterior |
| 3.5 | analogia concreta |

Nenhum par vizinho compartilha registro. **Pergunta âncora / retórica banida** — abertura é afirmação direta + mecanismo.

---

## Seção B.ter — Pré-requisitos cruzados (frase-âncora pronta)

| Pré-requisito | Frase pronta (≤25 palavras), colada na 1ª aparição |
|---|---|
| Estrutura do anticorpo | "O anticorpo tem dois braços que agarram o antígeno e uma haste, o Fc, que é a parte lida por outras moléculas do sistema imune." |
| IgM pentamérica | "A IgM circula como cinco unidades presas em roda, o que lhe dá dez sítios de ligação e um único bloco de hastes no centro." |
| Fagocitose | "Fagocitar é envolver a partícula com a membrana até fechá-la numa vesícula interna, onde enzimas e radicais a destroem." |
| Pressão osmótica e lise | "Se a membrana ganha um furo permeável a íons, a água entra atrás do soluto e a célula incha até romper." |
| PAMP e receptor de padrão | "O sistema inato reconhece assinaturas químicas que micróbios têm e nós não — açúcares e lipídios em arranjos que a célula própria não expõe." |
| Hemácia sem núcleo | "A hemácia madura não tem núcleo nem ribossomo: o que ela perde de proteína de superfície não é reposto." |

---

## Seção C — Distribuição da E2 e cotas técnicas

- **Profundidade:** PROFUNDO (`profundidade: fundo`) → **8 Consolidação (Q01–Q08) · 17 Integração (Q09–Q25) · 5 Aplicação (Q26–Q30)**.
- **Formatos:** 10 itens Certo/Errado (sempre 4 assertivas I–IV) distribuídos nas três categorias — Q03, Q06, Q08 (Cons); Q11, Q14, Q16, Q18, Q21, Q24 (Int); Q28 (Apl). "Assinale a **incorreta**" em Q05, Q19 e Q26 (sinalizado no stem).
- **Paridade:** banda dupla 0.80 ≤ ratio ≤ 1.25 em Q01–Q30 (MC). Distratoras redigidas ANTES da correta, 25–35 palavras, mecanismo plausível-errado vindo do Mapa de Confusões.
- **Termo-notas obrigatórios (10):** zimogênio · convertase · tioéster · opsonina · anafilatoxina · properdina · ficolina · imunocomplexo · quimiotaxia · âncora de GPI.
- **Siglas com `#sigla` na 1ª aparição:** MAC · MBL · MASP · CR1 · CR3 · CR4 · C3aR · C5aR · DAF · MCP · GPI · IgG · IgM · C1-INH · CH50 · AH50 · SHU · HPN · LES · PAMP · NADPH.
- **Boxes (cota):** por PARTE, 1 `atencao-box` + 1 `confusao-prevista`; `clinica-box` 2 por PARTE.
- **Fronteira da aula (anti-mistura UC03):** hipersensibilidade tipo II/III, estrutura fina da imunoglobulina, sepse e resposta de fase aguda entram só como **retomada de 1–2 frases** ou como cenário motivador da E2/E3 — nunca como subtópico com figura própria. A integração multiárea vive no texto motivador, não na E1.

---

## Seção D — Pontos de quebra do raciocínio (voz de mecanismo)

- **Quebra:** o aluno lê "via alternativa" como via de reserva, que só liga quando as outras falham.
  **Correção:** a hidrólise do tioéster do C3 é contínua e independente de estímulo; a via alternativa está sempre ligada em baixo nível e o que muda é se a superfície permite ou não que a convertase sobreviva.
- **Quebra:** o anticorpo livre no plasma ativaria a via clássica.
  **Correção:** C1q precisa de duas hastes Fc próximas no espaço; isso só acontece quando os anticorpos estão ancorados lado a lado num antígeno, ou quando a IgM muda de conformação ao ligar. Anticorpo solúvel mantém o Fc inacessível.
- **Quebra:** tratar o MAC como o mecanismo principal do sistema.
  **Correção:** a maioria das bactérias tem parede espessa demais para o poro alcançar a membrana; quem elimina o micróbio é a opsonização seguida de fagocitose. O MAC importa de fato contra *Neisseria*, que expõe membrana externa fina.
- **Quebra:** achar que a superfície própria é "reconhecida" ativamente e por isso poupada.
  **Correção:** não há reconhecimento do próprio. O C3b deposita em qualquer superfície; a diferença é que a membrana própria carrega ácido siálico e proteínas reguladoras que recrutam fator H e desmontam a convertase em segundos.
- **Quebra:** ler C3 e C4 baixos como sinônimo de deficiência genética.
  **Correção:** consumo por ativação contínua derruba os mesmos valores; a distinção vem do padrão — deficiência isolada mantém os demais componentes normais, consumo derruba vários ao mesmo tempo e acompanha atividade da doença.
- **Quebra:** supor que iC3b é "C3b inativado" e portanto inerte.
  **Correção:** o fator I retira do C3b a capacidade de formar convertase, mas o produto iC3b continua na superfície e é o melhor ligante de CR3/CR4. A clivagem desarma a amplificação e reetiqueta o alvo para fagocitose.
- **Quebra:** atribuir o angioedema hereditário à histamina.
  **Correção:** o C1-INH também freia calicreína e fator XIIa; sem ele, sobra bradicinina, que abre o endotélio. Por isso o inchaço não coça, não dá urticária e não responde a anti-histamínico nem a adrenalina.
- **Quebra:** achar que deficiência de complemento sempre dá infecção.
  **Correção:** falta de C1q, C4 ou C2 dá principalmente autoimunidade, porque a via clássica é quem solubiliza imunocomplexo e limpa corpo apoptótico; sem ela, restos nucleares se acumulam e viram antígeno.

*(Vocabulário de prova banido em toda a Seção D e no PDF.)*

---

## Seção E — Exemplares-âncora (`EXEMPLARES.md`)

- **Cat. 1 — Explicação mecanística parágrafo-a-parágrafo (universal).** Acerta em encadear causa → mecanismo → consequência sem cortar para lista. Vou usar em 2.1 e 2.2, onde a tentação de virar cadeia de siglas é máxima: cada fragmento entra numa frase com sujeito, verbo e complemento.
- **Cat. 8 — `atencao-box` (universal).** Acerta em reservar o vermelho para inversão com consequência real. Vou usar 3 no resumo inteiro (1.2 anticorpo livre; 2.3 MAC não é o principal; 3.5 consumo × deficiência), cada uma em dois movimentos: quebra + correção.
- **Cat. 14 — Siglas em footnote (universal).** Acerta em declarar a sigla dentro de uma frase que diz o que ela faz. Tema com 20+ siglas — é aqui que o resumo pode desandar em rajada; cada `#sigla` entra ancorada num verbo.
- **Cat. 3 — Abertura por desfazer confusão comum.** Acerta em usar a expectativa errada do aluno como degrau. Vou usar nas aberturas de 1.2, 2.1 e 3.3 (registro ponto-de-quebra), sempre como afirmação, nunca como pergunta.
- **Cat. 6 — Organização terminológica.** Acerta em domar nomenclatura ramificada antes de usá-la. Vou usar em 1.1 para fixar a convenção *a* = pequeno difusível / *b* = grande que gruda, com a exceção nomeada do C2 — e isso paga dividendo em todo o resto do resumo.
- **Cat. 16 — Catálogo de família + tabela.** Acerta em dar o eixo organizador antes dos dados. Vou usar em 3.1 para CR1–CR4 + C3aR/C5aR: o eixo é *qual fragmento cada receptor lê*, e a tabela evita quatro parágrafos gêmeos.
- **Cat. 9 — `clinica-box`.** Acerta em explicar a doença pela cadeia mecanística, não pelo nome. Seis boxes (ABO, properdina/meningococo, SHU atípica, angioedema, lúpus, HPN), cada um explicitando o gancho doença ↔ mecanismo (CLAUDE.md § Profundidade item 3).
- **Cat. 17 — Cadência dialogal.** Passada leve: 1–2 manobras por subtópico (avaliação narrativa, marcador de progressão), sem virar checklist.
- **Cats. 11 e 13 (Questionador).** Distratora com peça roubada da correta e texto motivador que não entrega a resposta.
