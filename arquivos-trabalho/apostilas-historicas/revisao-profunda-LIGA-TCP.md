# Revisão profunda Tier 3 — LIGA-TCP

**Tema (ancoragem):** Transplante Cardíaco Pediátrico — apostila inaugural da Liga de Cardiologia e Transplante Cardíaco Pediátrico (LCTXCP) da FMUSP. Cobre anatomia e fisiologia cardiovascular, IC, cardiomiopatias, cardiopatias congênitas, transplante e emergências cardiológicas pediátricas, em cinco partes.
**Autor:** Davi Sousa (apostila NEBLI própria — flag "não tão bom" no original sugere autocrítica).
**Personagem:** aluno FMUSP 1º ano, dificuldade real (ensino médio + meses de medicina; sem clínica prévia, sem familiaridade com cardiopatia congênita).
**Avaliador:** Opus via thread principal simulando revisor-pdf-profundo (sandbox bash).
**Data:** 2026-05-25

### Ancoragem de tema (passo obrigatório)
- **3 conceitos centrais que VOCÊ-aluno gostaria de aprender:** (1) por que algumas cardiopatias congênitas só descompensam dias depois do nascimento (canal arterial / forame oval); (2) lógica do shunt — quando vira cianose e quando vira IC por hiperfluxo; (3) por que o transplante cardíaco pediátrico é diferente do adulto (logística, ABO flexível, indicação por HLHS).
- **2 temas vizinhos que NÃO são esse:** cardiologia adulta (IAM, fibrilação atrial crônica) e cirurgia cardíaca adulta (revascularização, troca valvar adulta).

---

## 1. Pontos de parada (simulação aluno-em-dificuldade)

| Seção | Status | Pág | Razão |
|---|---|---|---|
| 1.1 Quatro câmaras | OK | 4–6 | Analogia "célula no fundo do oceano" prende o aluno. Diálogo claro. |
| 1.2 Frank-Starling | OK | 7–10 | Equação DC = FC × VS bem ancorada na consequência clínica pediátrica (taquicardia compensatória). |
| 1.3 Circulação fetal | OK | 11–14 | Forame oval × canal arterial bem separados; caixa "FOP ≠ CIA" salva o aluno. |
| 2.1 IC sistólica × diastólica | **[STOP: pág 15]** | 15 | "A fração de ejeção pode estar normal, mas como o volume que entra é pequeno..." — o conceito *fração de ejeção* aparece como termo-nota só nesse parágrafo, mas o aluno acabou de ver IC pela primeira vez; preciso de 1 parágrafo prévio dizendo "o que é uma fração de ejeção, o que é normal, o que é alta/baixa" antes de usar como discriminante entre sistólica/diastólica. |
| 2.2 Ciclo neuro-humoral | OK | 16–17 | Caixa "Por que digoxina caiu" é ouro — explicita a contraintuição. |
| 2.4 Cardiomiopatias | OK | 19–21 | Tabela 3-padrões + analogia "balão que perdeu elasticidade" funciona bem. |
| 3.1 Shunts | **[STOP: pág 22]** | 22 | "Se houver um shunt, o fluxo inicial vai ser da esquerda para a direita." — *inicial*? Por quê *inicial*? O aluno fica esperando a inversão prometida (que só aparece 2 páginas depois, com Eisenmenger). Sinalizar no momento: "vamos voltar a esse *inicial* na pág X". |
| 3.3 Fallot | OK | 28–30 | Manobra joelho-ao-peito + caixa explicativa fecham o mecanismo lindamente. |
| 3.5 HLHS | **[STOP: pág 34]** | 34 | "A fisiologia de Fontan tem uma peculiaridade: o sangue passa pelo pulmão sem ser bombeado por ventrículo. Como isso funciona? Pela pressão venosa elevada (forçando passagem passiva pelo leito pulmonar) e pela pressão pleural negativa da respiração espontânea." — aluno-em-dificuldade lê isso e fecha o PDF. *Como* a respiração espontânea ajuda? *Por quê* a pressão venosa fica elevada? Falta uma frase a mais. |
| 4.3 Captação | OK | 37–38 | Sequência operacional numerada (1–6) é o tipo de organização que o aluno quer ver. |
| 5.1 Choque | OK | 41–42 | Tabela 4-tipos é a referência operacional que o aluno volta a consultar antes da prova. |
| E2 Q01–Q20 | OK | 48–63 | Distratoras com mecanismo plausível, paridade preservada (raro em apostila NEBLI — ver T3.10). |
| Gabarito p.67 | **[STOP: pág 67]** | 67 | Diagramação do gabarito quebrou: ordem das questões aparece embaralhada na grade (Q12, Q13, Q20 caem na coluna de Consolidação visualmente). Aluno ansioso pré-prova vai pensar que o gabarito está errado e travar. **Bug de layout, não de conteúdo.** |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categorias relevantes consultadas:** Abertura por analogia macroscópica (cf. exemplares de glicólise/membrana onde "o todo vem antes da molécula"); Caixas explicativas tipo "Por que X funciona contraintuitivamente" (cf. exemplares de bioquímica clínica).

**Comparação parágrafo a parágrafo:**

**Parágrafo A (LIGA-TCP, pág 4):**
> "Pense numa célula isolada no fundo do oceano. Ela respira, come e excreta direto pela membrana — tudo o que precisa está a poucos micrômetros de distância, e a difusão resolve. Agora pense num organismo do tamanho de um ser humano..."

**Vs. exemplar canônico de abertura por analogia macroscópica:** essa abertura está *no padrão NEBLI*. Macroscopia → problema biológico → solução evolutiva → desenho anatômico. O aluno-em-dificuldade entra. ✅

**Parágrafo B (LIGA-TCP, pág 34):**
> "A fisiologia de Fontan tem uma peculiaridade: o sangue passa pelo pulmão sem ser bombeado por ventrículo. Como isso funciona? Pela pressão venosa elevada (forçando passagem passiva pelo leito pulmonar) e pela pressão pleural negativa da respiração espontânea."

**Vs. exemplar de "Por que X funciona contraintuitivamente":** o exemplar canônico de "betabloqueador em IC" (que aparece na *própria* apostila, pág 17) tem 3 frases de mecanismo + uma reviravolta + a regra prática. O parágrafo de Fontan tem **duas linhas e termina**. Conteúdo idêntico em densidade, mas a explicação ficou pela metade. O aluno fecha o PDF aqui.

**Veredito comparativo:** a apostila *tem* o padrão exemplar quando quer (pág 4, 7, 17, 28). Mas o aplica de forma desigual — alguns mecanismos centrais (Fontan, FE como métrica) recebem 1/4 do espaço que merecem.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Bloco 1 — Fontan sem mecanismo (pág 34)
**Citação literal:** "Como isso funciona? Pela pressão venosa elevada (forçando passagem passiva pelo leito pulmonar) e pela pressão pleural negativa da respiração espontânea. O paciente fica funcional, mas com pressões venosas cronicamente altas..."

**Diagnóstico mecanístico:** Davi cita os dois drivers (gradiente venoso passivo + bomba torácica respiratória) mas não *explica* nenhum dos dois. O aluno-em-dificuldade não sabe que respiração espontânea gera pressão pleural negativa, nem sabe que essa pressão "puxa" sangue venoso. A pergunta retórica "Como isso funciona?" cria expectativa que o parágrafo não cumpre.

**Reescrita pronta:**
> "Como isso funciona — circulação que atravessa o pulmão sem ventrículo bombeando? Por duas forças, ambas pequenas mas suficientes. A primeira é o gradiente de pressão: a pressão venosa sistêmica do paciente de Fontan é cronicamente alta (12–15 mmHg, três vezes a normal), e a pressão dentro do átrio pulmonar é baixa (2–4 mmHg). Esses 10 mmHg de diferença empurram sangue passivamente para o pulmão — não com a força de um ventrículo, mas o suficiente se a resistência pulmonar estiver baixa. A segunda é a bomba torácica respiratória: cada inspiração espontânea cria pressão pleural negativa (cerca de −5 mmHg), e essa pressão negativa puxa sangue venoso para dentro do tórax. Por isso paciente de Fontan piora com ventilação mecânica de pressão positiva — ela inverte a bomba torácica, e o retorno venoso despenca. Pressão venosa cronicamente alta tem preço: enteropatia perdedora de proteínas, fibrose hepática, arritmias atriais — as três grandes complicações tardias de Fontan."

### Bloco 2 — Eisenmenger anunciado sem cumprir (pág 22)
**Citação literal:** "Logo, se houver um shunt, o fluxo inicial vai ser da esquerda para a direita."

**Diagnóstico mecanístico:** A palavra *inicial* é uma promessa narrativa não cumprida no momento. O aluno-em-dificuldade não tem âncora para o que vem depois e fica em suspenso. Promessa narrativa só funciona se houver retorno explícito ("vamos voltar a esse *inicial* daqui a 2 páginas").

**Reescrita pronta:**
> "Logo, se houver um shunt, o fluxo inicial vai ser da esquerda para a direita. (Marque mentalmente esse *inicial* — daqui a duas páginas voltamos a ele, quando o pulmão se defender contra anos de hiperfluxo e o gradiente se inverter. É a síndrome de Eisenmenger.)"

### Bloco 3 — Fração de ejeção introduzida tarde (pág 15)
**Citação literal:** "Na IC diastólica, o ventrículo bombeia bem mas não consegue encher direito — a câmara está rígida, fibrótica ou hipertrofiada. A fração de ejeção pode estar normal, mas como o volume que entra é pequeno, o volume que sai também é pequeno..."

**Diagnóstico mecanístico:** o termo-nota de "fração de ejeção" aparece como footnote *neste* parágrafo, mas a métrica é usada como discriminante entre IC sistólica e diastólica já na frase anterior. O aluno-em-dificuldade lê "FE pode estar normal" sem ter assimilado o que é uma FE normal. A ordem ideal é: definição → escala normal → uso clínico — não os três simultâneos.

**Reescrita pronta:**
> "Antes de avançar, um conceito que vai voltar o tempo todo: **fração de ejeção** (FE). É a porcentagem do volume que estava no ventrículo no final da diástole e que foi de fato ejetado na sístole. Coração normal ejeta cerca de 55–65% — sobra um terço do volume dentro do ventrículo a cada batida. FE abaixo de 40% sinaliza IC sistólica (o ventrículo enche mas não ejeta direito); FE acima de 50% com sintomas de IC sinaliza IC diastólica (o ventrículo ejeta bem o pouco que conseguiu encher). Voltemos. Na IC sistólica, a FE despenca — é o critério ecocardiográfico que define a doença. Na IC diastólica, a FE pode estar normal, mas o volume absoluto que entra é pequeno; logo o volume absoluto que sai também é pequeno, e o débito cai mesmo com FE preservada."

---

## 4. T3.3 — 3 seções mais densas (com mitigação)

**S1 — Pág 31–33 (TGA + cirurgia de Jatene + Senning/Mustard).** Três cirurgias diferentes em duas páginas, com switch arterial × correção atrial misturados, e "janela de 15 dias" surge sem ancoragem prévia ao por quê. Mitigação: dividir em "TGA — anatomia" (1 página) → "TGA — manejo neonatal: PGE1 e atrioseptostomia de Rashkind" (1 página) → "TGA — correção definitiva: switch arterial e por que cedo" (1 página, com caixa "Por que a janela fecha"). Isso é o que a apostila *já tenta fazer* na pág 34 com a caixa "Por que o switch precisa ser feito cedo" — só precisa antecipar.

**S2 — Pág 33–35 (HLHS + Norwood + Glenn + Fontan).** Três estágios cirúrgicos com nomes próprios, com idades diferentes, e a fisiologia de Fontan no final como bonus track sem mecanismo (ver T3.2 Bloco 1). Mitigação: figura-resumo dos 3 estágios em uma página + 1 parágrafo dedicado para *cada* estágio explicando o que vira o quê. A apostila tem a legenda de figura ("As três etapas da paliação do HLHS") mas a figura em si não aparece com peso suficiente para carregar a explicação.

**S3 — Pág 41–43 (Choque + ABCDE + 4 tipos + ducto-dependente).** Quatro tipos de choque + sequência ABCDE + dois subgrupos de ducto-dependente + teste de hiperóxia, tudo em duas páginas. Mitigação: a tabela de 4 tipos (pág 42) está ótima — manter. O bloco ducto-dependente merece página dedicada com fluxograma "RN cianótico chega → teste de hiperóxia → não corrige → PGE1 + ecocardiograma" como organizador visual.

---

## 5. T3.4 — Voz fora do padrão (citações)

- Pág 17: "...e aqui vem o que parece contraintuitivo: dar betabloqueador num cora­ção já fraco. Por que isso ajuda?" — **voz exemplar NEBLI**, perfeita. Mantém.
- Pág 22: "Comecemos pela palavra shunt." — bom uso do imperativo pedagógico.
- Pág 30: "Cuidado oposto: vasodilatadores perif­éricos pioram o Tet spell." — frase curta e operacional, ótima.
- Pág 38: "(6) No centro transplantador. Receptor já está sob anestesia." — voz de checklist operacional, contrasta bem com voz narrativa do restante.
- **Desvios negativos:** pág 34 (Fontan, ver T3.2). Pág 26 ("Forte associação com síndrome de Down — até metade das crianças com trissomia 21 tem alguma forma de defeito cardíaco, e o DSAV é o mais característico.") — fato isolado sem mecanismo embriológico explicativo (por *que* trissomia 21 → coxim endocárdico defeituoso?). Aluno-em-dificuldade memoriza a correlação sem entender e esquece na semana seguinte.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** Pág 31–35 (TGA → Senning/Mustard → HLHS → Norwood → Glenn → Fontan). Em 5 páginas o aluno encontra: 2 cardiopatias estruturais distintas, 5 nomes próprios de cirurgia (Jatene, Senning, Mustard, Norwood, Glenn, Fontan), e a fisiologia em paralelo × em série + Fontan-como-univentrículo. O cérebro do aluno-em-dificuldade satura.

**3 mitigações:**
1. **Inserir página de "mapa de cirurgias congênitas" antes da pág 31** — uma tabela com 6 linhas (nome, indicação, idade típica, o que faz mecanicamente, complicação tardia). Aluno volta a essa página o tempo todo enquanto lê.
2. **Quebrar HLHS em duas seções** — uma para "anatomia e por que mata sem cirurgia", outra para "as três cirurgias da paliação + transplante neonatal".
3. **Mover "fisiologia de Fontan" para caixa explicativa dedicada** com diagrama de pressões (PVS alta, PAP baixa, gradiente passivo, bomba torácica) — não enterrar dentro do parágrafo de Norwood-Glenn-Fontan.

**Qual escolher:** a **#1** dá maior alívio cognitivo com menor reescrita. É a intervenção dominante.

---

## 7. T3.8 — Análise visual (do PDF renderizado: páginas 1, 4, 15, 25)

- **Hierarquia tipográfica:** capa canônica NEBLI v2 (Merriweather body + sans para "NEBLI · APOSTILA" eyebrow), faixa navy do título funciona. Headers de PARTE em sans bold navy, headers 1.1/1.2 em sans menor — hierarquia legível. ✅ No corpo, "Resumindo até aqui" + "Síntese 1.1" se diferenciam com fundo bege/caixa — bom recurso.
- **Valor pedagógico das figuras:** páginas 15 e 25 mostram **slides do professor recortados como imagem** (pág 15: card "Insuficiência cardíaca · Definição"; pág 25: cards "CIV" e "CIA" com coração + texto). Legendas abaixo são autorais e relacionam a figura ao parágrafo seguinte. Valor pedagógico real — não decorativo. ✅. **Problema:** as figuras-slide ocupam cerca de 50% da página e o texto que sobra fica comprimido na parte inferior — pág 25 tem 2 imagens + tabela + 1 parágrafo, sensação de fartura visual mas pouco respiro.
- **Densidade visual:** Parte I (págs 4–14) tem boa proporção figura/texto (figura a cada 1–2 páginas). Partes IV e V (pág 36 em diante) viram **muro de texto** — 5 páginas sem figura (47–52 estão todas zero imagens segundo JSON; mesmo padrão 48–67 nas etapas 2 e 3, o que é esperado). Mas na Parte IV (36–40), a densidade caiu de 31 imagens totais para 1 por página, com pág 36 sendo 469 palavras × 0 imagens — claustrofobia visual.
- **Uso de cor:** navy + bege + branco = paleta canônica NEBLI. Caixa "Por que digoxina caiu" usa fundo bege claro — destaca bem sem brigar. As três categorias prometidas no sumário (verde Consolidação, azul Integração, violeta Aplicação) precisam ser checadas visualmente na E2 — o render não pegou essas páginas, mas pela estrutura textual sugiro suspeita de que **não foram aplicadas badges coloridas** (questões listadas como "Questão 01 Consolidação" sem cor visível no header). **Auditar.**
- **Cortes/overflow:** sem mojibake visível; sem hifenização agressiva no que vi; pág 67 (gabarito) tem **bug grave de layout** — questões aparecem fora de ordem numa grade que não respeita o agrupamento por categoria que o cabeçalho promete. Render explícito: Q12, Q13, Q20 caem na coluna errada visualmente, e Q11, Q16 aparecem em outra coluna. **Single point of failure pré-prova.**

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (alimenta Phase F)

### Técnica 1 — "Caixa contraintuitiva com mecanismo"
**Citação:** Pág 17, caixa "Por que digoxina caiu de uso e betabloqueador subiu":
> "Por décadas, o tratamento da IC era melhorar a contratilidade — empurrar o coração a bombear mais (digoxina, dobutamina). Hoje sabemos que isso melhora os sintomas mas piora a sobrevida. Coração que ejeta mais hoje custa mais miocárdio amanhã. O paradigma virou ao contrário: desligar o que está pressionando o miocárdio (SRAA, SNS) e deixar ele 'respirar'. É contraintuitivo mas robusto: menos estímulo → mais sobrevida."

**Nome da técnica:** *Caixa-paradoxo* — abertura com o consenso intuitivo errado, virada pela evidência, mecanismo fisiopatológico fechando a virada, regra prática como cabide.

**Quando NEBLI deveria usar:** sempre que uma terapia ou conduta clínica corrente *parece contrariar* o mecanismo básico que o aluno acabou de aprender. Casos imediatos: betabloqueador em IC (já feito aqui), insulina em DKA hipocalêmica, líquidos cautelosos em cardiogênico, manobra de Valsalva em TSV. **Gancho para REDATOR-E1:** adicionar à régua editorial uma regra "se a parte clínica contradiz o mecanismo, abra caixa-paradoxo de 4 frases".

### Técnica 2 — "Equivalente pediátrico de sintoma adulto"
**Citação:** Pág 18, legenda de figura:
> "Sudorese ao mamar = dispneia aos esforços; baixo ganho ponderal = caquexia cardíaca; mamadas interrompidas = intolerância ao exercício."

**Nome da técnica:** *Mapa de tradução cross-faixa-etária* — listar pareamentos diretos "manifestação A em adulto = manifestação B em criança" como ponte mnemônica.

**Quando NEBLI deveria usar:** sempre que um tema da matéria adulta (já aprendido) tem manifestação clínica deslocada na criança (semestre 1 = pouca clínica, aluno tem o adulto como referência implícita). Casos imediatos: jugular ingurgitada → hepatomegalia (já feito); dor torácica → choro paroxístico não-explicado; dispneia → recusa alimentar. **Gancho para REDATOR-E1:** quando o resumo for pediátrico, abrir parágrafo com "no adulto X = na criança Y" antes de descrever o quadro.

### Técnica 3 — "Sequência operacional numerada para protocolos"
**Citação:** Pág 37–38, "(1) Identificação e abertura de protocolo de morte encefálica... (2) Aprovação familiar... (3) Avaliação clínica do doador... (4) Decisão sobre transporte... (5) Captação... (6) No centro transplantador."

**Nome da técnica:** *Checklist narrativo* — quando o tema é um *processo* (não um conceito), numerar etapas em prosa curta, cada etapa com 2–4 frases, sem virar bullet point seco.

**Quando NEBLI deveria usar:** processos clínicos com sequência fixa que o aluno precisa internalizar como rotina. Casos imediatos: rastreio neonatal (Apgar → reanimação → teste do pezinho → coraçãozinho), abordagem ao politrauma (ABCDE expandido), purificação de proteína por etapas (já é canônico no NEBLI). **Gancho para REDATOR-E1:** distinguir explicitamente *conceito* (prosa) de *processo* (checklist narrativo numerado).

---

## 9. T3.10 — 7 erros NEBLI no PDF (calibração)

| # | Erro NEBLI | Status | Evidência |
|---|---|---|---|
| 1 | Paridade de distratoras em Aplicação | **AUSENTE** ✅ | Q17–Q20 (págs 60–63): distratoras de 50–80 palavras com mecanismo plausível-mas-errado completo. Correta de Q20 (D, Rashkind + Jatene): ~52 palavras; maior distratora (B, Senning/Mustard): ~45 palavras. Ratio ~1.15. **Calibração superior à média NEBLI.** |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PRESENTE (leve)** ⚠️ | "FiO2" aparece na pág 43 caixa "Teste de hiperóxia" sem sigla declarada. "B2 desdobrada" (pág 25) sem nota técnica para o aluno-em-dificuldade que não tem ausculta. "B3 de galope" (pág 41 tabela) idem. **3 lapsos.** |
| 3 | Subagentes Opus customizados falhando | **N/A** | Apostila não passou por subagentes do pipeline G20 — escrita diretamente como apostila inaugural da liga. |
| 4 | Heredoc ENAMETOOLONG | **N/A** | Não compete análise de produto final. |
| 5 | `questao-ce` exige tupla | **N/A** | Não há questões CE nessa apostila. |
| 6 | Termo-notas abaixo do alvo (alvo 6–8) | **AUSENTE** ✅ | Contei pelo menos 10 termos-nota declarados (válvula, volume sistólico, fração de ejeção, congênita, paliação, anastomose, crise hipoxêmica, correção atrial, Norwood, morte encefálica). **Acima do alvo.** |
| 7 | Tema-card com teto E1 errado | **PRESENTE (variante)** ⚠️ | E1 ocupa páginas 4–46 = **43 páginas de E1**, muito além do teto canônico de 22. Justificável porque é apostila inaugural de liga (não um resumo de aula UC1/UC2), mas o teto canônico não foi sinalizado como flexibilizado em decisão editorial registrada. Se a liga vira fluxo recorrente, **canonizar teto separado para apostilas de liga** (sugestão: 50 páginas E1, 30 questões E2 + 5 E3 mantidos). |

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Bug do gabarito (pág 67):** layout em grade quebra o agrupamento por categoria visualmente. Refazer com 3 colunas explícitas (uma por categoria, cabeçalho colorido) e ordem sequencial dentro de cada coluna. *Single fix de maior impacto pré-prova.*
2. **E2 com 20 questões em vez de 30 canônicas:** ou (a) expandir para 30 (12 Consolidação + 12 Integração + 6 Aplicação), ou (b) canonizar formato "apostila de liga = 20 + 5" como variante registrada. Não deixar implícito.
3. **Inserir mapa-de-cirurgias antes da pág 31:** tabela síntese de Jatene/Senning/Mustard/Norwood/Glenn/Fontan/Blalock-Taussig, uma página dedicada. Vira página de consulta repetida pelo aluno.

### MECANÍSTICO (max 3)
1. **Reescrever parágrafo de Fontan (pág 34)** com mecanismo do gradiente passivo + bomba torácica respiratória (ver T3.2 Bloco 1 reescrita pronta).
2. **Introduzir fração de ejeção como conceito de 4 frases ANTES da distinção sistólica/diastólica** (pág 15) — ver T3.2 Bloco 3 reescrita pronta.
3. **Adicionar 2 frases sobre por que trissomia 21 → DSAV** (pág 26): "Síndrome de Down envolve sinalização de coxim endocárdico — as estruturas embrionárias que dividem o coração entre lados superior e inferior. DSAV é a falha mais clássica dessa via, presente em ~25% das crianças com T21."

### DIDÁTICO (max 3)
1. **Sinalizar promessas narrativas:** quando aparecer um "inicialmente", "por enquanto", "vamos voltar", inserir ponteiro explícito ("voltamos a isso na pág X") — ver T3.2 Bloco 2.
2. **Caixa-paradoxo (Técnica 1 de T3.9):** sistematizar como recurso editorial em REDATOR-E1.
3. **Mapa de tradução cross-faixa-etária (Técnica 2 de T3.9):** abrir parágrafos pediátricos com "no adulto X = na criança Y" explícito.

### ESTÉTICO (max 3)
1. **Auditar badges coloridos da E2:** confirmar visualmente se Consolidação/Integração/Aplicação aparecem com cor (verde/azul/violeta) no header das questões. Se não, aplicar via template.
2. **Respiro na Parte IV:** páginas 36–40 têm densidade textual alta (~400 palavras/pág) sem figura. Adicionar diagrama de fluxograma de captação + foto/esquema de Berlin Heart.
3. **Pág 25 está com 50% figura-slide:** reduzir as 2 imagens para 35% cada e deixar tabela respirar na parte inferior.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM** — é a melhor execução de E2 em termos de paridade de distratoras que já vi em material NEBLI; abertura macroscópica e caixas-paradoxo são padrão exemplar; uso de slide-do-professor como figura central com legenda autoral é o padrão que o REDATOR-E1 deveria seguir mais.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM** — três estruturais (bug do gabarito, formato 20×30, mapa-de-cirurgias) + três mecanísticos (Fontan, FE, T21→DSAV).
3. **Seção para refazer?** **Pág 31–35 (TGA + HLHS + Fontan)** — carga cognitiva pico, três mecanismos centrais subdesenvolvidos, e a página-mapa de cirurgias resolve dois deles de uma vez.
4. **Parágrafos para reescrever?** **3** — (a) Fontan pág 34, (b) Eisenmenger-inicial pág 22, (c) FE introduzida tarde pág 15. Reescritas já prontas em T3.2.

---

[APROVAR COM RESERVAS]

Reservas: (1) bug visual do gabarito pág 67; (2) E2 com 20 ≠ canônico 30 — decidir se canoniza variante "apostila de liga"; (3) páginas 31–35 (TGA/HLHS/Fontan) merecem refatoração com mapa-de-cirurgias e mecanismo de Fontan expandido. As três técnicas extraídas em T3.9 (caixa-paradoxo, mapa cross-faixa-etária, checklist narrativo) devem ser canonizadas no REDATOR-E1 — é o item de maior valor desta revisão para o pipeline NEBLI.
