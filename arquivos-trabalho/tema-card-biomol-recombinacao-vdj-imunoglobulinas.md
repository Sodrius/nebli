# TEMA CARD — Recombinação V(D)J e geração de diversidade de anticorpos

## Seção A — Escopo

- **Tema (capa):** Geração de diversidade de anticorpos
- **Subtítulo (capa):** Biologia Molecular
- **Slug:** `biomol-recombinacao-vdj-imunoglobulinas`
- **Aula curta (Drive/deck):** Recombinação e diversidade de anticorpos
- **Docente:** Alexandre Bruni-Cardoso (sigla ABC) — Depto. de Bioquímica, IQ-USP
- **Onde estudar:** Alberts, *Molecular Biology of the Cell* 6ª ed., cap. 24 · Watson, *Molecular Biology of the Gene* 7ª ed., cap. 12 · Krebs, *Lewin's Genes XI*, cap. 18
- **Alvo de páginas E1:** piso 2, **teto 22**; alvo 18–21
- **profundidade:** `padrao` (default já elevado — CANON 2026-07-12)
- **Recorte slide × tema:** o slide cobre o arco completo (antígeno/epítopo → estrutura da Ig → loci em segmentos → regra 12/23 → RAG → JNHE → diversidade juncional → exclusão alélica → hipermutação somática → mudança de classe → consequências indesejadas). O tema pedido = o slide inteiro. Sem estreitamento nem alargamento — **não há recorte a validar**.
- **Sem calibração de banco:** não existe `aula:` correspondente em `banco/aulas_uc01.yml` / `uc02.yml` (a aula é de um bloco de Biologia Molecular novo, fora das UCs com banco). Calibração vem do slide + bibliografia citada pelo professor. Declarado aqui para o relatório de fechamento.
- **Sem deck-aula nesta corrida:** o pedido foi explicitamente "etapas 1 a 3". Além disso, esta sessão roda em container remoto — AnkiConnect (localhost) é inalcançável, então o passo 11 do `/resumo` fica pendente por impossibilidade técnica, não por escolha.

### Prioridades desta corrida (do § Diário de revisões do MEMORY.md)

1. **Peso alto — `biocel-07-divisao-celular` (2026-05-29): figura é canônica, "sem slide" ≠ "sem figura".** Aqui há slide farto, mas o risco irmão é usar o slide *inteiro* como figura, com legenda em inglês e três painéis competindo. Mitigação adotada: **19 recortes** de painel único a partir do PDF do professor, cada um carregando **um** mecanismo. Cadeia ≥4 setas (nick → hairpin → abertura → junção) recebe figura adjacente obrigatória.
2. **ERROS #12 — cadeia ≥4 setas sem figura adjacente.** O tema é quase todo cadeia multi-passo. Toda cadeia longa da E1 tem `#figura-nebli` colada.
3. **ERROS #16 / F3 — excesso de caixa vermelha.** Cota 1–2 boxes pesados por PARTE; as demais confusões viram prosa dialogada (o tema tem muitas confusões nomeáveis, e a tentação de encaixotar todas é real).
4. **ERROS #20 — `#termo-nota` com termo repetido na prosa.** Auto-check antes de fechar a E1.
5. **Regra editorial 3 — prosa fluida, nunca empilhamento de siglas.** Tema com RAG1, RAG2, RSS, TdT, JNHE, AID, Ku, DNA-PKcs, XRCC4, UNG. Risco máximo de A4 (`ANTI-EXEMPLARES.md`). Cada sigla entra dentro de frase com sujeito + verbo + complemento.

---

## Seção B — Esqueleto das 3 PARTES

### PARTE I — O desafio: um repertório maior que o genoma (4 subtópicos)

- **1.1 — O que o anticorpo precisa reconhecer** (antígeno, epítopo de 10–12 aminoácidos, a aritmética 20¹⁰)
- **1.2 — A imunoglobulina por dentro: onde mora a variabilidade** (2 pesadas + 2 leves, região variável × constante, sítio de ligação na interface V_L/V_H, CDRs)
- **1.3 — A região constante decide a classe, e a classe decide a função** (μ δ γ α ε; κ ou λ; IgM/IgD/IgG/IgA/IgE)
- **1.4 — O paradoxo aritmético e a hipótese que o resolveu** (>10¹² Ig com ~25 000 genes; Dreyer–Bennett; Tonegawa; seleção clonal — o repertório é prévio ao antígeno)

Figuras planejadas: `fig-selecao-clonal` (slide-07), `fig-ig-esquema` + `fig-ig-3d` (slide-08), `fig-cadeias-vc` (slide-10), `fig-classes-ig` (slide-10), `fig-linfopoiese` (slide-06), `fig-expansao-clonal` (slide-07). → 6–7 na PARTE I.

### PARTE II — A máquina: recombinação V(D)J (5 subtópicos)

- **2.1 — O locus em segmentos: da linhagem germinativa ao DNA da célula B** (V/J na leve, V/D/J na pesada; corte no DNA, splicing no RNA — dois cortes diferentes)
- **2.2 — Diversidade combinatória: a primeira conta** (35×5, 40×23×6, λ, 295×5520 ≈ 1,6×10⁶) — cálculo em etapas rotuladas
- **2.3 — RSS e a regra 12/23: a gramática que impede a junção errada** (7-mer, espaçador 12 ou 23 pb, 9-mer; uma ou duas voltas da hélice)
- **2.4 — Primeiro passo: RAG1/RAG2 corta** (sinapse, nick, transesterificação, hairpin covalente)
- **2.5 — Segundo passo: a JNHE costura** (recombinação homóloga × JNHE; Ku, DNA-PKcs, Artemis, XRCC4–ligase IV; junta codificante × junta-sinal descartada)

Figuras: `fig-vj-fluxo` (slide-11), `fig-locus-pesada` (slide-11), `fig-rss` + `fig-rss-arranjo` (slide-13), `fig-rag-nick-hairpin` (slide-15), `fig-rag-sinapse` (slide-16), `slide-19` inteiro (RH × JNHE, texto já em português), `fig-jnhe-ku` (slide-20), `fig-junta-codificante` (slide-21). → 8–9 na PARTE II. Cadeia ≥5 passos em 2.4 e 2.5 = figura obrigatória, cumprida.

### PARTE III — Ampliar a diversidade, e pagar por ela (5 subtópicos)

- **3.1 — Diversidade juncional: a imprecisão que multiplica** (aparo, nucleotídeos P, TdT e os N; CDR3; o preço do desalinhamento de fase)
- **3.2 — Exclusão alélica: uma célula B, um anticorpo** (pré-BCR desliga RAG; ordem pesada→leve; por que a seleção clonal exige isso)
- **3.3 — Hipermutação somática: AID e a maturação de afinidade** (desaminação C→U; U:G; UNG e sítio abásico; polimerases translesão)
- **3.4 — Mudança de classe: função nova, especificidade intacta** (regiões switch, deleção em círculo, AID de novo — e por que isso *não* gera diversidade)
- **3.5 — O preço do sistema: células inúteis, células autorreativas e quebras no lugar errado** (deleção clonal, edição de receptor, anergia; translocações)

Figuras: `fig-diversidade-juncional` (slide-17), `fig-exclusao-alelica` (slide-14), `fig-aid-cascata` (slide-22), `fig-switch-classe` (slide-23). → 4 na PARTE III (piso 3 cumprido).

**Total planejado: ~19 figuras.**

---

## Seção B.bis — Registro de abertura por subtópico (rotação, sem par vizinho igual)

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | analogia concreta (a peça e o encaixe) |
| 1.3 | integração-posterior (a haste que ainda não usamos) |
| 1.4 | ponto-de-quebra (a conta não fecha) |
| 2.1 | integração-anterior (retoma o paradoxo de 1.4) |
| 2.2 | enquadramento (a conta que a segmentação permite) |
| 2.3 | ponto-de-quebra (o que impede V+V?) |
| 2.4 | analogia concreta (a tesoura que amarra a ponta que corta) |
| 2.5 | integração-posterior (a quebra ainda está aberta) |
| 3.1 | ponto-de-quebra (a máquina erra — e o erro é o produto) |
| 3.2 | integração-anterior (retoma seleção clonal de 1.4) |
| 3.3 | enquadramento |
| 3.4 | analogia concreta (trocar o cabo, manter a ponta) |
| 3.5 | ponto-de-quebra (o que sobra de errado) |

---

## Seção B.ter — Pré-requisitos cruzados com frase-âncora pronta

| Pré-requisito | Frase pronta (≤25 palavras) |
|---|---|
| Íntron/éxon e splicing | "Splicing é a edição do RNA: o transcrito sai com trechos que não codificam nada e a célula os remove antes de traduzir." |
| Quebra de dupla fita e reparo | "Quebra de dupla fita é o dano mais perigoso do DNA — as duas fitas se rompem no mesmo ponto e nenhuma serve de molde para a outra." |
| Recombinação homóloga | "Na recombinação homóloga a célula copia a informação perdida da cromátide-irmã, que é idêntica — reparo fiel, mas só disponível depois da replicação." |
| Transcrição → tradução | "A sequência de DNA vira RNA mensageiro e o mensageiro vira cadeia de aminoácidos: mexer no DNA muda a proteína no fim da linha." |
| Fase de leitura (códons) | "O ribossomo lê o mensageiro de três em três; inserir ou tirar um número de bases que não seja múltiplo de três desloca todos os códons seguintes." |
| Desaminação de citosina | "Tirar o grupo amina de uma citosina a transforma em uracila — uma base que o DNA não deveria conter, e que pareia como se fosse timina." |

---

## Seção C — Distribuição da E2

Profundidade **PADRÃO** (o slide é denso, mecanístico, com cadeia longa, mas é a primeira aula do bloco): **10 Consolidação · 15 Integração · 5 Aplicação**.

Formatos: 20 múltipla escolha · **10 Certo/Errado** (Q03, Q06, Q10, Q12, Q15, Q18, Q21, Q24, Q27, Q30 — sempre 4 itens I–IV) · **3 "assinale a incorreta"** (Q05, Q17, Q23).

Gabarito sorteado (bloco `gabarito:` no YAML). Distribuição das 20 MC: A=4 · B=4 · C=5 · D=4 · E=3 (máx 25%, nenhuma corrida ≥4). C/E: 20 C e 20 E nos 40 itens, sem bloco longo, sem CECE mecânico.

---

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** o aluno trata a recombinação V(D)J como splicing.
  **Correção:** a recombinação corta e religa o **DNA** da célula B, e o que fica de fora é fisicamente deletado do genoma daquela célula; o splicing acontece depois, no **RNA**, para tirar o íntron entre J e C. São duas edições, em moléculas diferentes, em momentos diferentes.

- **Quebra:** o aluno acha que o antígeno instrui o anticorpo a tomar a forma certa.
  **Correção:** o repertório é construído **antes** de qualquer encontro, por recombinação aleatória na medula óssea; o antígeno apenas **seleciona** e expande o clone cujo receptor já encaixava. Diversidade primeiro, seleção depois.

- **Quebra:** o aluno conclui que a maior fonte de diversidade é a combinatória de segmentos.
  **Correção:** a combinatória entrega ~1,6×10⁶ combinações; é a **diversidade juncional** — aparo variável, nucleotídeos P e nucleotídeos N da TdT — que multiplica esse número por várias ordens de grandeza. O erro na junção é a fonte dominante.

- **Quebra:** o aluno junta hipermutação somática e mudança de classe como se fossem o mesmo processo por serem ambos dependentes de AID.
  **Correção:** a hipermutação muda a **região variável** (a especificidade e a afinidade mudam); a mudança de classe troca a **região constante** (a função efetora muda, a especificidade não). Mesma enzima, alvos e consequências opostos.

- **Quebra:** o aluno espera que a regra 12/23 sirva para "escolher" o melhor segmento.
  **Correção:** a regra não escolhe nada — ela é uma restrição **geométrica** que só permite sinapse entre um sinal de espaçador 12 e um de espaçador 23. Qual V e qual J entram continua sendo sorteio.

- **Quebra:** o aluno lê "junta-sinal" e "junta codificante" como dois nomes da mesma coisa.
  **Correção:** o corte gera duas junções: a **codificante**, imprecisa, que fica no cromossomo e vira a região que reconhece antígeno; e a **junta-sinal**, precisa, que sai num círculo de DNA sem origem de replicação e se perde nas divisões seguintes.

- **Quebra:** o aluno supõe que toda recombinação produz um anticorpo funcional.
  **Correção:** como o aparo e a inserção são aleatórios, apenas cerca de um terço das junções mantém a fase de leitura. As demais produzem cadeia truncada, e a célula tenta o segundo alelo ou morre.

- **Quebra:** o aluno vê a JNHE como reparo "ruim" que a célula B usaria por falta de opção.
  **Correção:** a JNHE é o reparo escolhido **de propósito** aqui. A célula B em desenvolvimento está fora da fase S — não há cromátide-irmã para copiar — e, mais importante, a imprecisão da JNHE é o próprio produto desejado.

---

## Seção E — Exemplares-âncora (de `EXEMPLARES.md`)

- **Categoria 1 (mecanística parágrafo-a-parágrafo)** — acerta em dar a **cadeia completa** ("liga → abre → entra → despolariza") em vez de citar nomes. Vou usar em 2.4 e 2.5, onde a tentação é enfileirar RAG1, RAG2, Ku, Artemis, XRCC4 sem dizer o que cada um faz na sequência.
- **Categoria 3 (abrir desfazendo confusão)** — acerta em explicitar o erro mental antes de construir o certo. Vou usar em 2.1 (recombinação ≠ splicing) e em 3.4 (mudança de classe não gera diversidade).
- **Categoria 5 (refinamento histórico com insight mecanístico)** — acerta em ancorar autor + data **e** amarrar ao ganho mecanístico. Vou usar em 1.4: Dreyer–Bennett (1965) propõem dois genes para um polipeptídeo, Tonegawa (1976) mostra que o DNA da célula B é fisicamente diferente do DNA embrionário. O refinamento importa porque destrói o dogma "um gene, um polipeptídeo" para esse locus.
- **Categoria 6 (organização terminológica em hierarquia)** — acerta em avisar que os termos confundem e construir hierarquia antes das definições. Vou usar em 1.2/1.3 (cadeia pesada/leve, região variável/constante, κ/λ, classes) e em 3.1 (P × N, aparo × inserção).
- **Categoria 8 (`atencao-box` em 2 movimentos)** — quebra + correção no mesmo parágrafo. Uma por PARTE, no máximo duas: PARTE II sobre recombinação × splicing; PARTE III sobre hipermutação × mudança de classe.
- **Categoria 12/18 (cálculo em etapas rotuladas, modelo Mankiw)** — acerta em montar em prosa, rotular cada etapa e reler o número em palavras. Vou usar em 1.1 (20¹⁰) e em 2.2 (a conta da combinatória). Nada de parede de símbolos (`ANTI-EXEMPLARES` A1).
- **Categoria 14 (siglas por footnote)** — universal; o tema tem 10+ siglas e é onde A4 mais ameaça.
- **Categoria 17 (cadência dialogal)** — repertório de voz: variar abertura, pingar avaliação narrativa, encenar a confusão antes da caixa, plantar marcador de progressão. Distribuir, não encaixotar.
