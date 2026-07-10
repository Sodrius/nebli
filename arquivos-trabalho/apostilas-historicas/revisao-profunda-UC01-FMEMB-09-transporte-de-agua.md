# Revisão profunda Tier 3 — UC01-FMEMB-09-transporte-de-agua

**Tema (ancoragem):** Transporte de água pelo epitélio intestinal
**Autor:** Fernando Abdulkader (apostila histórica; voz herdada, dialógica)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real, ensino médio + meses de medicina
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

### Ancoragem prévia (obrigatória)
- **3 conceitos centrais que eu-aluno gostaria de aprender:** (1) por que a água "segue" o soluto — o mecanismo termodinâmico da osmose sem cair em "as moléculas querem"; (2) como o enterócito polarizado consegue mover litros de água sem gastar ATP diretamente nela; (3) por que a SRO funciona na cólera mesmo com diarreia ativa.
- **2 temas vizinhos que NÃO são esse:** (a) néfron e reabsorção tubular renal de água; (b) transporte de glicose no metabolismo intracelular (glicólise/GLUT-4 no músculo).

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão (mecanística, do ponto de vista do aluno) |
|---|---|---|---|
| Intro + 3 peças | OK | 3 | Abertura limpa, anuncia o roteiro. Não paro. |
| 1.1 Osmose | OK | 3–4 | Pergunta ingênua dos dois copos. Reflexo errado nomeado. Bom. |
| 1.2 Aquaporinas / motivo NPA / Grotthuss | **[STOP: pág 5]** | 5 | "Quebra a cadeia de hopping (mecanismo de Grotthuss pelo qual prótons normalmente se propagam pela água)" — Grotthuss aparece sem prep e some. Aluno em dificuldade trava: "preciso saber Grotthuss?" Não há retomada de 1 linha. Footnote ausente. |
| 1.3 Transcelular vs paracelular | OK | 6–7 | Boa metáfora do epitélio como fronteira. |
| Mapa conceitual I | OK | 7 | Reforço útil. |
| 2.1 Na/K-ATPase | OK | 7–8 | Metáfora "bola na rampa" + boxe "bomba mora na basolateral" funciona. |
| 2.2 SGLT-1 | OK | 9 | Diálogo continua. |
| 2.3 Solvent drag + cinética numerada | **[STOP: pág 10]** | 10 | A "sequência típica após refeição" lista tempos (0s, ms, 0,1s, 1s, contínuo) mas o que é a unidade "ms" no item 2 e 3 sem número? "2 ms" parece "2 milissegundos" mas item 3 também tem "ms" — aluno fica em dúvida se é tempo ou marcador. Tipografia da tabela é confusa (ver T3.8). |
| 3.1 Leaky vs tight + tabela segmentar | **[STOP: pág 12–13]** | 12 | **A tabela quebrou.** A coluna "Rota dominante" aparece desencaixada das linhas; "Duodeno / Jejuno / Íleo / Cólon" aparece em coluna isolada com linhas em branco ao lado. Aluno tenta ler "Duodeno — Muito leaky — ??? — ???" e perde 30s reconstituindo a correspondência. Risco real de fechar PDF. |
| 3.2 Distribuição quantitativa | OK | 13–14 | Os números (6 L jejuno, 2 L íleo, 400 mL cólon, 100 mL fezes) ancoram bem. |
| 3.3 Diarreia / cólera / SRO | OK | 14–15 | Excelente. Curva crescente de complexidade: osmótica simples → secretora → SRO como engenharia. |
| Mapa conceitual III + Conclusão integradora | OK | 16 | Fecha em 3 níveis (molecular/celular/órgão). Boa síntese. |
| Resumindo (2 colunas) | OK | 17–18 | Denso mas navegável. |
| Etapa 2 — Q1 a Q30 | Parada parcial | 19–31 | Q22 item III mistura SGLT-1 com toxina coleriana em uma frase só — leitura pesada. Q25 alternativa D tem typo "o açúcar não é seu substrato" (ver T3.2). |
| Gabarito | **[STOP: pág 35]** | 35 | Layout do gabarito está bagunçado: "Q01 B Q02 CEEC Q03 E Q04 C Q05 EECC / Q08 CECE Q09 C Q10 B / Q06 A Q07 D" — a ordem das linhas embaralha Q06–Q07 abaixo de Q08–Q10. Aluno conferindo gabarito tem que caçar a questão. Erro estrutural de bloco. |

**Total de [STOP]:** 4 paradas reais (Grotthuss, cinética ms, tabela segmentar quebrada, gabarito desordenado).

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria relevante:** "Abertura por pergunta ingênua + reflexo errado nomeado" e "Mecanismo termodinâmico sem antropomorfismo grosseiro".

**Parágrafo da apostila (pág 3, abertura de 1.1):**
> "Imagine dois copos separados por uma membrana que deixa água passar mas barra um soluto qualquer — açúcar, por exemplo. No copo da esquerda, água pura. No copo da direita, água com bastante açúcar dissolvido. O que acontece com o nível dos dois copos depois de algumas horas? A intuição diz 'nada' — afinal, o açúcar está preso de um lado, então a água 'não tem motivo' para se mexer. Errado."

Padrão exemplar: cena concreta → pergunta direta ao aluno → nomeia o reflexo errado → corrige. **Esse parágrafo É exemplar candidato** — entra no banco de aberturas (ver T3.9).

**Parágrafo NEBLI canônico equivalente (gliconeogênese, abertura PARTE I):** abre direto em "depois de 16h de jejum, sua glicemia ainda está em 4,5 mM — por quê?". Mais clínico, menos físico, mas a mesma assinatura: pergunta → reflexo provável → contradição. Há paridade. **Empate técnico.**

**Onde a apostila ganha:** o "errado" lacônico isolado em linha funciona como pausa dramática — o aluno relê. NEBLI tende a explicar antes de deixar o aluno errar internamente.

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação completa)

### Parágrafo fraco 1 — Grotthuss em 1.2 (pág 5)

**Citação literal:**
> "Prótons (H+) também são barrados, apesar de pequenos, porque o motivo NPA orienta as moléculas de água dentro do poro de modo a quebrar a cadeia de hopping (o mecanismo de Grotthuss pelo qual prótons normalmente se propagam pela água)."

**Diagnóstico mecanístico:** Grotthuss é citado como apêndice entre parênteses, sem desenho, sem retomada. Para o aluno que não sabe que prótons "andam de boca em boca" entre moléculas de água, a frase vira ruído denso. Pior: a expressão "cadeia de hopping" + "mecanismo de Grotthuss" empilha dois termos novos em um parêntese. **Quebra a regra do aluno baseline = baixo.**

**Reescrita pronta:**
> "Prótons (H⁺) também são barrados, apesar de minúsculos. O truque é o seguinte: prótons normalmente atravessam a água saltando de uma molécula para a próxima — como se passassem 'de boca em boca' por uma cadeia de H₂O alinhadas. O motivo NPA gira as moléculas de água dentro do poro de jeito que essa cadeia quebra: nenhuma H₂O fica orientada para passar o próton adiante. Resultado: a água atravessa, o próton fica preso. (Esse mecanismo de salto se chama Grotthuss — você verá o nome em fisiologia ácido-base.)"

### Parágrafo fraco 2 — Cinética numerada (pág 10)

**Citação literal:**
> "1 0s   Glicose e Na+ chegam à luz após digestão do amido / 2 ms   SGLT-1 apical captura 2 Na+ e 1 glicose; conformação muda / 3 ms   Soluto liberado no citoplasma; concentração local sobe"

**Diagnóstico mecanístico:** "2 ms" e "3 ms" não comunicam tempo absoluto (são milissegundos depois de quê? do item 1?). A tabela mistura ordem (1, 2, 3, 4, 5, 6) com instante temporal (0s, ms, 0,1s, 1s, contínuo), e o número da linha cola no número do tempo sem espaço claro. Aluno em dificuldade lê "1 0s" como "10s". **Carga cognitiva desnecessária — informação útil arruinada por tipografia.**

**Reescrita pronta:**
> "Cinética típica após refeição rica em carboidratos (sequência de eventos no jejuno):
> - **t = 0:** glicose e Na⁺ chegam à luz, recém-liberados pela digestão do amido.
> - **t ≈ 2 ms:** SGLT-1 apical liga Na⁺ + glicose e muda de conformação.
> - **t ≈ 3 ms:** soluto liberado no citoplasma; concentração local sobe.
> - **t ≈ 0,1 s:** gradiente osmótico forma-se; aquaporinas trazem água.
> - **t ≈ 1 s:** GLUT-2 solta glicose pela basolateral; Na/K-ATPase expulsa Na⁺.
> - **regime contínuo:** capilar absorve glicose + Na⁺ + água; volume plasmático se mantém."

### Parágrafo fraco 3 — Q22 item III + Q25 alternativa D (pág 27 e 29)

**Citação literal Q22 III:**
> "a toxina coleriana inativa o SGLT-1 apical, eliminando a base do tratamento com SRO."

**Citação literal Q25 D:**
> "na cólera, o SGLT-1 segue intacto e absorve glicose+Na+ em má-absorção, o açúcar não é seu substrato."

**Diagnóstico mecanístico:** Q25 alternativa D é ininteligível — frase truncada, sem operador lógico claro entre as duas orações. Parece que faltou "porque" ou "enquanto que". Como distratora de Aplicação, isso é falha de paridade (canon NEBLI erro #1): a correta C é cristalina ("o SGLT-1 cotransporta Na+ e arrasta água por solvent drag, mesmo com CFTR ativado") enquanto D é gramaticalmente quebrada. Aluno exclui D por estranhamento, não por mecanismo. **Falha pedagógica.**

**Reescrita pronta da D (Q25):**
> "D) na má-absorção de carboidratos, o açúcar ofensor (ex: lactose) não é substrato do SGLT-1 e não pode ser cotransportado com Na⁺ — a SRO oferece glicose, mas o problema é o açúcar dietético retido na luz, não a falta de Na⁺ para reabsorver."

(Distratora agora rica em mecanismo plausível-mas-errado, paridade com a correta.)

---

## 4. T3.3 — 3 seções mais densas + mitigação concreta

| Seção | Densidade | Mitigação |
|---|---|---|
| 1.2 Aquaporinas (tetrâmero + NPA + Grotthuss) — pág 5 | NPA + Grotthuss + estrutura tetramérica + 12 isoformas, tudo em ~600 palavras. | Quebrar: estrutura tetramérica em 1 parágrafo + figura, seletividade (íons + prótons) em 2º parágrafo com reescrita Grotthuss acima, isoformas em 3º parágrafo com tabela enxuta de AQP1/2/3/4 (não enumerar 1–12). |
| 3.1 Tabela segmentar — pág 12 | Tabela quebrada (ver T3.8), 4 segmentos × 3 colunas + função, mas linhas misturadas. | Reconstruir tabela com 4 colunas claras: **Segmento \| Junção \| Rota dominante \| Função principal**. Hoje a coluna "Função" está colada na coluna "Rota" e o aluno não acha o limite. |
| 3.3 Cólera (toxina → Gs → adenilato → AMPc → CFTR → Cl⁻ → Na⁺ paracelular → água) — pág 14–15 | Cadeia de 7 passos em 2 parágrafos densos. | Adicionar mini-diagrama vertical (causa → mecanismo → consequência) com setas. Ou box numerado de 4 etapas. Está bem escrito, só faltou ancoragem visual. |

---

## 5. T3.4 — Voz fora do padrão (citações)

A voz é **muito consistente** — Abdulkader mantém o tom dialógico do começo ao fim. Pouquíssimos desvios.

**Desvio 1 (pág 16, Conclusão integradora):** "A natureza inventou o transporte epitelial uma vez, e replicou a ideia em toda fronteira do corpo onde precisava mover fluido."
- Tom literário/contemplativo bate com o didático sem destoar — é fechamento, posição justifica. **Não é desvio nocivo.**

**Desvio 2 (pág 10, sobre SRO):** "A SRO salva milhões de vidas por ano com um mecanismo que cabe em duas linhas de bioquímica. Não é por acaso que o The Lancet a chamou de 'a maior descoberta médica do século XX'."
- Quase publicitário. Mas o aluno gosta — funciona como dopamina narrativa para fixar o conceito. **Aceitável.**

**Sem desvios graves.** Voz coesa.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** 1.2 Aquaporinas (pág 5). Concentra: estrutura tetramérica + poro em ampulheta + motivo NPA + seletividade por desidratação iônica + bloqueio de prótons via Grotthuss + 12 isoformas + distribuição por tecido. ~600 palavras em uma página.

**3 mitigações possíveis:**
1. Cortar Grotthuss para footnote curta ("salto entre moléculas, ver fisiologia ácido-base"). Foco em "o gargalo é estreito demais para íons hidratados".
2. Separar estrutura (1 parágrafo) de seletividade (1 parágrafo) de isoformas (1 parágrafo curto com tabela AQP1/2/3/4 só).
3. Adicionar figura de aquaporina em corte com o NPA marcado — substitui 3 parágrafos por 1 imagem + legenda.

**Qual escolher:** **#3 + #2 combinados.** A figura resolve o impasse estrutural; a separação por subtemas reduz carga cognitiva. Grotthuss permanece, mas como nota — o aluno em dificuldade pula sem perder o fio.

---

## 7. T3.8 — ANÁLISE VISUAL (do PDF)

Baseado em metadata JSON (sem renderização PIL disponível neste ambiente — pdftoppm ausente). Inferência por contagem de palavras/imagens por página + texto extraído.

| Sub-item | Avaliação | Evidência |
|---|---|---|
| **Hierarquia tipográfica** | OK | Headers PARTE I/II/III distintos; sub-headers numerados 1.1/1.2/1.3; "Resumindo até aqui" como marcador de fechamento. |
| **Valor pedagógico das figuras** | Misto | 7 imagens consistentes por página (logos, banners, ornamentos = decorativas). Figuras de slide referenciadas no texto ("repare como o slide ilustra...") mas o aluno não vê o slide embutido — apenas referência textual. **Figuras pedagógicas integradas estão ausentes ou são poucas.** O texto pede figura ("o slide é o desenho-chave do tema") mas o aluno fica com a referência sem o desenho. |
| **Densidade visual (respiro)** | Variável | Pág 10 (508 palavras), pág 17 (516), pág 14 (448) — picos de densidade. Resumindo (pág 17) carrega 516 palavras em 2 colunas — é o limite do tolerável. Pág 18 cai para 112 palavras (boa pausa). |
| **Uso de cor** | Inferido coerente | Banner gold no Resumindo (canônico NEBLI); categorias de questão (Consolidação/Integração/Aplicação) provavelmente com cores distintas. **Não verificável sem render visual.** |
| **Cortes/overflow** | **Tabela 3.1 (pág 12) tem layout quebrado** | Texto extraído mostra colunas desencaixadas: "Duodeno Muito leaky / Jejuno Leaky / Íleo Intermediário / Cólon Tight" em coluna isolada com linhas em branco. Gabarito (pág 35) com ordem das questões bagunçada (Q06–Q07 fora de sequência). **Bug estrutural confirmado.** |

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas — ALIMENTA Phase F)

### Técnica 1 — **Pergunta ingênua + reflexo errado nomeado + correção em frase curta**

**Citação literal (pág 3, 1.1):**
> "O que acontece com o nível dos dois copos depois de algumas horas? A intuição diz 'nada' — afinal, o açúcar está preso de um lado, então a água 'não tem motivo' para se mexer. Errado. O nível do copo da direita sobe; o da esquerda baixa."

**Nome da técnica:** **"Pergunta-reflexo-errado-correção em três frases."**

**Quando NEBLI deveria usar:** abertura de QUALQUER sub-tópico onde haja intuição-armadilha conhecida (já catalogada no mapa-confusoes/<slug>.md). Hoje o REDATOR-E1 tende a explicar o mecanismo correto antes do aluno errar — perde o momento de "errar e corrigir" que fixa mais. Gancho: integrar ao § "Diálogo precede tudo" do redator-e1.md com regra explícita: "se mapa-confusoes lista uma intuição errada, abrir o sub-tópico com pergunta que provoque essa intuição, ANTES de dar a resposta".

### Técnica 2 — **Boxe destacado para confusão clássica espacial/anatômica**

**Citação literal (pág 8):**
> "A bomba mora na basolateral, não na apical / Confusão clássica: aluno desenha a Na/K-ATPase no topo do enterócito, virada para a luz. Não. Ela está na membrana voltada para o sangue. Faz sentido se você pensar no destino do Na+ absorvido..."

**Nome da técnica:** **"Boxe-anti-erro-anatômico" (formato: título-imperativo + 'aluno faz X. Não.' + justificativa pelo destino fisiológico).**

**Quando NEBLI deveria usar:** sempre que houver assimetria espacial (apical vs basolateral, intra vs extracelular, núcleo vs citosol, mitocôndria interna vs externa). Aluno em dificuldade erra essa orientação espacial constantemente. Hoje NEBLI tem `#nota-mnemonica` mas não um padrão dedicado a corrigir erro anatômico. Sugestão: helper `#boxe-anti-erro-anatomico[título imperativo][conteúdo]` no template visual.

### Técnica 3 — **Princípio integrador unificador no fecho ("uma fronteira, o mesmo design")**

**Citação literal (pág 16, Conclusão integradora):**
> "A natureza inventou o transporte epitelial uma vez, e replicou a ideia em toda fronteira do corpo onde precisava mover fluido."

E no Resumindo (pág 18, "Princípio integrador"):
> "Molécula (aquaporina) → célula (gradiente de Na+) → órgão (epitélio leaky vs tight). Em todos os três níveis, o tema é o mesmo: a água é arrastada por gradientes que o epitélio gera manipulando soluto. Replica-se em néfron, vesícula, plexo coroide — uma fronteira, o mesmo design."

**Nome da técnica:** **"Hat-trick integrador: molécula → célula → órgão + ponte para temas vizinhos."**

**Quando NEBLI deveria usar:** SEMPRE na Conclusão integradora. Hoje o REDATOR-E1 fecha com "vimos X, Y, Z" sem o gesto de generalização ("isso reaparece em..."). O hat-trick faz três coisas em um parágrafo: (a) reagrupa os três níveis de escala, (b) explicita o princípio único, (c) lista 2-3 temas futuros onde o mesmo padrão aparece — funciona como gancho de currículo. **Gancho concreto:** adicionar à seção "Conclusão integradora" do redator-e1.md a regra: "fecho deve nomear 2-3 temas vizinhos do currículo onde o mesmo princípio reaparece".

---

## 9. T3.10 — 7 erros NEBLI (tabela de calibração)

| # | Erro NEBLI | Status no PDF | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **PRESENTE (parcial)** | Q25 alternativa D truncada/ininteligível vs correta C rica. Q26 alternativa D ("a glicose alimenta as bactérias coleranas, distraindo-as") é bem-humorada mas curta vs C rica. Paridade não foi rigorosamente respeitada. |
| 2 | Siglas sem `#sigla()` 1ª aparição | **PRESENTE (parcial)** | ENaC (pág 13) e DP (pág 12, "diferença de potencial") aparecem sem definição explícita na 1ª ocorrência. Gs (pág 14, "proteína G") tem definição parcial mas faltou expansão formal. AQP3, AQP10 (pág 5) aparecem sem definição própria — apenas AQP1/2/4 ganham footnote. |
| 3 | Subagentes Opus falhando | N/A | Apostila histórica, não foi gerada pelo pipeline NEBLI atual. |
| 4 | Heredoc `ENAMETOOLONG` | N/A | Não aplicável a apostila histórica. |
| 5 | `questao-ce` exige tupla | N/A | Não verificável fora do .typ. Questões CE renderizadas corretamente no PDF. |
| 6 | Termo-notas abaixo do alvo | **AUSENTE** | Termo-notas estão **acima** do alvo — aquaporina, AQP1, AQP2, AQP4, Na/K-ATPase, ATP, SGLT-1, GLUT-2, deficiência de lactase, CFTR (10+ definições explícitas). Apostila modela o que NEBLI deveria fazer. |
| 7 | Tema-card teto E1 errado | N/A (PDF tem 18 pp E1) | Dentro do teto canônico de 22. **OK.** |

**Resumo da calibração:** apostila histórica é mais limpa que o NEBLI médio em termos-nota (#6) e voz, mas tropeça em paridade de distratoras (#1) e siglas (#2) — mesmos erros do NEBLI. Bug estrutural ADICIONAL: tabela quebrada (pág 12) e gabarito desordenado (pág 35) — não estão no checklist, ENTRAM como erro #8 candidato.

---

## 10. Recomendações por hierarquia de impacto

### ESTRUTURAL (max 3)
1. **Corrigir layout da tabela segmentar 3.1 (pág 12).** A coluna "Função principal" aparece descolada das linhas. Reconstruir com `table()` Typst 4 colunas iguais. **Bloqueia leitura.**
2. **Corrigir ordem do gabarito (pág 35).** Linhas Q06–Q07 aparecem abaixo de Q08–Q10. Reordenar sequencialmente Q01→Q30. **Bloqueia uso prático.**
3. **Adicionar figura de aquaporina (corte mostrando NPA) na pág 5.** Substitui 2-3 parágrafos densos por imagem + legenda curta. Resolve pico de carga cognitiva (T3.7).

### MECANÍSTICO (max 3)
1. **Reescrever bloco Grotthuss (pág 5)** com a versão proposta em T3.2 §1 (salto "de boca em boca" + figura).
2. **Reescrever Q25 alternativa D** com a versão proposta em T3.2 §3 (paridade restaurada).
3. **Reformatar cinética da pág 10** com formato t = 0 / t ≈ 2 ms / t ≈ 0,1 s (T3.2 §2).

### DIDÁTICO (max 3)
1. **Adicionar `#sigla()` em ENaC, DP transepitelial, Gs, AQP3, AQP10** — siglas que apareceram no corpo sem footnote.
2. **Aplicar Técnica 1 (T3.9) — pergunta-reflexo-errado** em mais sub-tópicos do PDF: hoje só 1.1 e o boxe 2.1 usam. 2.2 (SGLT-1) e 3.3 (cólera) poderiam abrir do mesmo jeito.
3. **Reforçar "iso-osmolaridade do fluido absorvido" (pág 10)** como caixa destacada — é o ponto que conecta tudo e está em prosa contínua.

### ESTÉTICO (max 3)
1. **Pág 17 (Resumindo)** com 516 palavras em 2 colunas — perto do limite. Considerar expandir para 18+19 (duas páginas leves) ou cortar a seção "Polaridade do enterócito" (já está em Q21).
2. **Mapas conceituais I/II/III** (pág 7, 11, 16) têm caracteres ASCII de seta (`→`?) mal renderizados no .txt — verificar se PDF os mostra como setas reais ou quadrados/glyph errados.
3. **Footnotes do final da pág 5 (AQP1/2/4)** estão coladas no corpo sem separação clara — adicionar régua horizontal.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva? SIM** — voz dialógica, 3 técnicas exemplares (pergunta-reflexo-errado, boxe-anti-erro-anatômico, hat-trick integrador) entram no banco NEBLI Phase F. Termos-nota modelares (#6 invertido).
2. **≥1 ESTRUTURAL/MECANÍSTICO? SIM** — 3 estruturais + 3 mecanísticos elencados.
3. **Seção para refazer? UMA: 1.2 Aquaporinas (pág 5)** — reescrever Grotthuss + adicionar figura + separar estrutura/seletividade/isoformas.
4. **Parágrafos para reescrever? 3 + 2 estruturais + 1 alternativa de questão:**
   - Bloco Grotthuss (pág 5) — T3.2 §1.
   - Cinética numerada (pág 10) — T3.2 §2.
   - Q25 alternativa D (pág 29) — T3.2 §3.
   - Tabela 3.1 (pág 12) — reconstrução estrutural.
   - Gabarito (pág 35) — reordenação estrutural.

---

[APROVAR COM RESERVAS]

Reservas: corrigir bugs estruturais de layout (tabela 3.1 + gabarito) antes de promover como modelo. Conteúdo didático é exemplar — as 3 técnicas de T3.9 são contribuição direta para o REDATOR-E1 NEBLI.

<!-- FIM-REVISAO-PROFUNDA -->
