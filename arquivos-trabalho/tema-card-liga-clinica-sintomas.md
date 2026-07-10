# Tema Card — Sintomas-chave do raciocínio clínico (Liga de Clínica Médica FMUSP 2026, PDF 1/2)

## Seção A — Identidade

- **Tema:** Sintomas-chave do raciocínio clínico — Dor Torácica (Arthur), Avaliação da Dispneia (Leonardo), Edema (Marcela). Três palestras independentes do curso introdutório da Liga de Clínica Médica da FMUSP, costuradas aqui em um único resumo NEBLI cujo eixo é "o paciente chega com um sintoma — como pensar".
- **Disciplina:** Liga de Clínica Médica — Curso Introdutório 2026.
- **Slug:** `liga-clinica-sintomas`.
- **Profundidade:** **PROFUNDO** (8 Cons · 17 Int · 5 Apl). As 3 palestras juntas cruzam semiologia, fisiopatologia, raciocínio probabilístico, diagnóstico diferencial e clínica integrada — pede E2 mais densa em Integração porque a IC aparece nas 3 PARTES e é o nó natural de cruzamento.
- **Tamanho-alvo:** piso 18, **teto 32 páginas** (excepcionalmente ampliado de 22 — autorizado por Davi 2026-05-29 dado o escopo do PDF integrar 3 palestras independentes com casos clínicos próprios). Distribuição: PARTE I ≈ 8–10 pp · PARTE II ≈ 8–10 pp · PARTE III ≈ 10–12 pp · Intro + Conclusão + Resumindo ≈ 2–3 pp.
- **Onde estudar:** Harrison *Principles of Internal Medicine* (cap. dor torácica, dispneia, edema); Goldman-Cecil *Medicine* (cap. dor torácica, dispneia, edema); UpToDate "Clinical manifestations and evaluation of edema in adults"; Patel H, Skok CJ, DeMarco A. *Peripheral edema: evaluation and management in primary care*. Am Fam Physician. 2022;106(5):557-564; Swap CJ, Nagurney JT. *Value and limitations of chest pain history in the evaluation of patients with suspected acute coronary syndromes*. JAMA. 2005;294(20):2623-2629.
- **Recorte slide × tema:** sem corte significativo nas 3 palestras-fonte. As palestras de Arthur e Leonardo são compactas (51 e 22 slides) com casos clínicos explícitos; Marcela é a mais densa (61 slides) cobrindo Starling + nefro + hepato + cardio + venosa. Cada palestra vira uma PARTE; a Conclusão integradora costura as 3 pelo eixo do raciocínio probabilístico e pela IC como nó convergente.
- **Calibração (substitui banco_slim):** este resumo não filtra `banco_slim.json` porque Liga de Clínica Médica não está mapeada em `banco/aulas_uc*.yml` (banco cobre UC01 e UC02 da Med-FMUSP, não a Liga). A calibração se faz pelos próprios slides e pela bibliografia oficial da liga. Mapa de Confusões alimentado pelos pontos de quebra observados nas perguntas de discussão dos slides + armadilhas clínicas clássicas dos 3 sintomas.
- **Pasta de trabalho:** `typst-build/` raiz. Saída: `resumos-gerados/LIGA-CLINICA-SINTOMAS.pdf`.

## Seção B — Estrutura da E1

### Intro-box (1 página)

Antes de mergulhar nos três sintomas, ancorar o porquê do agrupamento: paciente chega com queixa subjetiva ("dói o peito", "falta o ar", "minha perna inchou"), e o trabalho do clínico é **dar nome a essa queixa em forma de diagnóstico provável**. Os três sintomas escolhidos compartilham estrutura idêntica de raciocínio — abertura por epidemiologia + gravidade, hierarquização de hipóteses por probabilidade pré-teste, exames como ferramenta de ajuste (likelihood ratios), e clínica que **converge na insuficiência cardíaca** como nó comum. A IC aparece nas 3 PARTES como diferencial obrigatório, e essa convergência é o gancho da Conclusão integradora.

### PARTE I — Dor Torácica: pensar antes de pedir exame (4 subtópicos, ~8–10 pp)

**1.1 — Por que começamos pelo raciocínio, não pela tomografia**

- Pergunta de abertura (uma das 3 permitidas no resumo inteiro): "Por que dois pacientes com a mesma queixa — 'dor no peito' — recebem investigações tão diferentes?". Resposta: porque o contexto (idade, sexo, fatores de risco, padrão da dor) muda a **probabilidade pré-teste** das hipóteses, e o exame só faz sentido depois de hierarquizar.
- Modelo hipotético-dedutivo: geração inicial de hipóteses → coleta direcionada de dados → testar hipóteses → revisar e refinar. O ECG é quase sempre o primeiro passo na dor torácica aguda — barato, rápido, descarta a hipótese mais letal (SCA) em 30 segundos.
- O exame complementar não é "pedir tudo para ver o que aparece" — é alimentar o raciocínio. Cada exame **move a probabilidade** para cima ou para baixo de cada hipótese (likelihood ratio na prática).
- Justifica raciocínio das perguntas do palestrante Arthur (slides 14, 18, 23, 49).
- Figuras: `slide-14.png` (modelo hipotético-dedutivo simplificado), `slide-18.png` (modelo completo com revisão).

**1.2 — Causas graves primeiro: o que não pode passar**

- Regra de ouro: **sempre começar pensando nas causas graves (ameaçadoras à vida)** — não porque sejam as mais frequentes, mas porque o custo de errar é morte.
- As 5 causas que não podem passar na dor torácica aguda: **SCA** (síndrome coronariana aguda — IAM e angina instável), **dissecção de aorta** (dor súbita, intensa, irradiando para dorso, assimetria de pulso/PA), **TEP** (tromboembolismo pulmonar — dor pleurítica, dispneia, fatores de risco para TVP), **pneumotórax** (dor súbita + dispneia + redução de murmúrio vesicular), **pericardite/tamponamento** (dor pleurítica que melhora ao inclinar-se à frente, atrito pericárdico).
- ECG entra primeiro: se há alteração isquêmica → conduz como SCA imediatamente; se não há, conduz conforme probabilidade das outras hipóteses. ECG **não exclui SCA**, mas elimina a urgência absoluta do supra de ST.
- `#atencao-box` central (cota máxima 1–2 por PARTE; este é o crítico): aluno tende a achar que ECG normal = pode descartar IAM. **Falso.** ECG inicial é normal em ~30–50% dos IAMs sem supra (IAMSSST); a troponina seriada e o quadro clínico decidem.
- Justifica conselho preciosos dos slides 16, 17, 49.
- Figuras: `slide-17.png` (algoritmo dor aguda — instabilidade, ECG, conduta).

**1.3 — Os 5 grandes diferenciais — scripts de doença lado a lado**

- "Scripts de doença" é o nome técnico para representação mental do quadro clássico de cada diagnóstico — inclui epidemiologia, fisiopatologia, apresentação clínica, exame físico, exames complementares e tratamento. O clínico experiente reconhece um script em segundos; o aluno constrói scripts uma por uma.
- Lado a lado, os 5 scripts da dor torácica letal:
  - **SCA típica:** homem >50 anos, fatores de risco (HAS, DM, dislipidemia, tabagismo, obesidade, sedentarismo), dor retroesternal em aperto, irradiação para MSE/mandíbula, associada a diaforese e dispneia, dura mais de 20 min, não melhora com repouso ou nitrato.
  - **Dissecção de aorta:** dor súbita, intensa, "rasgando", irradiação para dorso interescapular, fatores de risco (HAS mal controlada, Marfan, válvula bicúspide, gravidez); ao exame, assimetria de pulso ou de PA entre membros.
  - **TEP:** mulher jovem com fatores de risco (anticoncepcional, gravidez/puerpério, TVP prévia, neoplasia, imobilização recente, trombofilia), dor pleurítica em hemitórax, piora à inspiração, dispneia, taquicardia.
  - **Pericardite:** jovem após infecção viral recente, dor que piora ao deitar e melhora ao inclinar-se à frente, atrito pericárdico, ECG com supra côncavo difuso.
  - **Esofágica/musculoesquelética/ansiedade:** dor que reproduz à palpação ou que melhora com IBP; sem fatores de risco cardiovasculares, ECG normal, troponina normal.
- Pergunta de bolso para cada hipótese: "**o que fala a favor? o que fala contra? o que está faltando se for verdade?**". Eliminar por exclusão é tão importante quanto confirmar por inclusão.
- Justifica scripts dos slides 34–38 + cenários 1–4 (slides 24, 30, 40, 43).
- Figuras: `slide-34.png` (templo dos scripts de doença), `slide-29.png` + `slide-30.png` (cenário 1 SCA × cenário 2 TEP lado a lado).

**1.4 — Raciocínio tipo 1 e tipo 2 + escores probabilísticos**

- **Tipo 1** = rápido, intuitivo, reconhecimento de padrão; baixo gasto cognitivo. É o "olho clínico". Funciona bem para scripts dominados; falha quando o caso é atípico.
- **Tipo 2** = lento, analítico, deliberado; alto gasto cognitivo. É o "raciocínio de cobertura". Necessário quando o tipo 1 não encaixa.
- Bom clínico **alterna**: dispara tipo 1 → se há dúvida ou conflito, ativa tipo 2 → reformula hipóteses → volta para tipo 1 calibrado.
- Escores probabilísticos (HEART, GRACE, TIMI para SCA; Wells/PERC para TEP) são ferramentas de **tipo 2 sistematizado**: convertem variáveis clínicas em probabilidades quantitativas, ajudando a decidir conduta quando o tipo 1 está em dúvida.
- Dados de anamnese, exame físico e exames complementares **aumentam ou diminuem** a probabilidade pré-teste — é a versão clínica do raciocínio bayesiano.
- Justifica slides 27, 41, 20–22, 23, 45–48 do palestrante.
- Figuras: `slide-41.png` (tipo 1 × tipo 2 comparativo).

### PARTE II — Avaliação da Dispneia: aguda × crônica, raciocínio epidemiológico (4 subtópicos, ~8–10 pp)

**2.1 — É dispneia mesmo? Distinguir de fadiga**

- Dispneia = percepção subjetiva de **incapacidade de respirar confortavelmente**. Inclui sensação de falta de ar, peso no peito, fome de ar, esforço respiratório desproporcional.
- Fadiga = sensação de cansaço generalizado, intolerância ao esforço, sem componente respiratório dominante. Pode ter origem cardíaca, hematológica, metabólica, psiquiátrica.
- A distinção importa porque o caminho de investigação diverge: dispneia puxa cardio/pulmo; fadiga puxa anemia/tireoide/depressão/desnutrição/IC oculta.
- Confusão clássica: paciente com IC inicial frequentemente diz "estou cansado" em vez de "falto ar" — o clínico precisa perguntar dirigido ("subir escada te faz parar para respirar ou só te cansa?") para destravar a queixa real.
- Justifica slide 3 do palestrante Leonardo.

**2.2 — Dispneia aguda (horas a dias): estabilidade primeiro, ECG e RX depois**

- Pergunta operacional: **é grave? precisa tratamento imediato?**
- Sinais vitais primeiro — FR e SpO₂ são os dois números que decidem se o paciente vai para sala vermelha ou consultório. SpO₂ < 90% em ar ambiente é red flag; FR > 24 em adulto é red flag.
- Suporte de oxigênio e ventilatório se necessário — não esperar diagnóstico para suplementar O₂ em paciente hipoxêmico.
- Anamnese e exame clínico direcionados aos sistemas cardiovascular e respiratório. Causas graves de dispneia aguda: edema pulmonar (IC descompensada), TEP, pneumotórax, broncoespasmo grave (asma/DPOC exacerbado), pneumonia extensa, tamponamento cardíaco.
- Justifica slide 5 do palestrante.

**2.3 — Dispneia crônica (>4–8 semanas): raciocínio epidemiológico — as 6 causas comuns**

- Aqui o método muda: em vez de descartar causas raras e letais imediatas, vai-se às 6 causas mais frequentes:
  - **Asma** — pacientes jovens, marcha atópica (rinite, eczema, alergia), flutuação dos sintomas, desencadeantes (frio, exercício, ácaro, alérgeno), tosse crônica especialmente noturna, sintomas induzidos por exercício, espirometria pode ser normal entre crises.
  - **DPOC** — pacientes acima dos 40 anos, tabagistas (geralmente >10 maços-ano), dispneia progressiva aos esforços, tosse com expectoração, sintomas que pioram com infecções respiratórias.
  - **Insuficiência cardíaca** — dispneia aos esforços progressiva, ortopneia (precisa de travesseiros para dormir), DPN (acorda no meio da noite com falta de ar), bendopneia (dispneia ao inclinar-se para frente — amarrar sapato), turgência jugular, refluxo hepatojugular, hepatomegalia, B3 ao exame.
  - **Doenças intersticiais** — dispneia progressiva, tosse seca, estertores em velcro nas bases, possíveis exposições ocupacionais (asbesto, sílica) ou drogas (amiodarona).
  - **Obesidade + descondicionamento** — diagnóstico de exclusão; dispneia proporcional ao esforço e ao peso, melhora com perda ponderal e exercício.
  - **Anemia** — fadiga + dispneia aos esforços, palidez, soproso sistólico funcional; identifica-se com hemograma simples.
- A pergunta para o aluno: **"qual o quadro epidemiológico do paciente?"** orienta qual hipótese sobe primeiro. Mulher jovem com tosse noturna e rinite → asma sobe. Homem 65 anos tabagista → DPOC. Idoso com infartos prévios → IC.
- Justifica slides 4, 6, 7, 8 do palestrante.
- Figuras: `slide-07.png` (asma × DPOC comparativo), `slide-08.png` (sinais de IC).

**2.4 — Exames como ferramenta de ajuste — sensibilidade, especificidade, likelihood ratio**

- Exames iniciais do paciente com dispneia: **SpO₂ no esforço** (caminhada de 6 min ou simulação no consultório), **hemograma** (Hb afasta anemia), **RX de tórax** (cardiomegalia, infiltrado pulmonar, derrame, hipertransparência do DPOC), **ECG** (sinais de IAM antigo, hipertrofia ventricular), **BNP/NTproBNP** (peptídeo natriurético — sobe em IC; >100 pg/mL com NTproBNP >300 sugere etiologia cardíaca da dispneia), **TSH** (hipo/hipertireoidismo pode dar dispneia).
- Próximos exames se primeira leva não fechar: **prova de função pulmonar** (avalia obstrução vs restrição), **TC de tórax** (detalha parênquima e vasos), **ecocardiograma** (avalia função ventricular, valvopatias, derrame pericárdico).
- SpO₂ no esforço — útil para diferenciar etiologias: causa pulmonar dessatura cedo; causa cardíaca pode dessaturar, mas geralmente menos; descondicionamento/ansiedade tem SpO₂ preservada (paciente para por desconforto, não por hipoxemia).
- **Likelihood ratio (LR)** é o nome técnico do "quanto este achado muda a probabilidade do diagnóstico". Regra de bolso prática (sem precisar de nomograma):
  - LR <0,1 → reduz **muito** (quase exclui).
  - LR 0,1–0,2 → reduz bastante.
  - LR 0,2–0,5 → reduz pouco.
  - LR ≈1 → não muda nada.
  - LR 2–5 → aumenta pouco.
  - LR 5–10 → aumenta bastante.
  - LR >10 → aumenta **muito** (quase confirma).
- Exemplo: BNP <100 pg/mL em paciente com dispneia tem LR ≈0,1 → reduz muito a probabilidade de IC. Útil para **descartar** mais que para confirmar.
- Justifica slides 10, 11, 13, 14, 21 do palestrante.

### PARTE III — Edema: Starling + as 4 grandes etiologias sistêmicas (5 subtópicos, ~10–12 pp)

**3.1 — Por que o líquido sai do vaso — as 4 forças de Starling + drenagem linfática**

- Edema = acúmulo anormal de líquido no **espaço intersticial**. Não acontece "porque sim"; é violação de uma equação que funciona normalmente.
- **Forças de Starling** governam a troca de fluido entre capilar e interstício:
  - **Pc** (pressão hidrostática capilar) — empurra água para fora; sobe em IC (congestão venosa), DRC, cirrose, insuficiência venosa.
  - **πp** (pressão oncótica plasmática) — puxa água para dentro; cai em hipoalbuminemia (síndrome nefrótica, cirrose com falência hepática, desnutrição, enteropatia perdedora de proteínas).
  - **Pi** (pressão hidrostática intersticial) — normalmente baixa.
  - **πi** (pressão oncótica intersticial) — normalmente baixa; sobe se proteína vaza do vaso (inflamação, queimadura).
- Equação simplificada: fluxo = K × [(Pc − Pi) − σ(πp − πi)]. Em equilíbrio, pouco líquido sai; o pouco que sai volta pelo **sistema linfático**.
- **5ª via — permeabilidade capilar aumentada** (inflamação, sepse, queimadura, angioedema): proteína vaza junto com água, πp cai localmente, edema acompanha.
- **6ª via — prejuízo na drenagem linfática** (linfedema): mesmo com forças normais, sem retorno linfático o líquido se acumula. Causas: pós-cirúrgico (esvaziamento ganglionar), pós-radioterapia, infecções (filariose), tumores.
- Mapa mental do edema: **identificar qual força está alterada → o mecanismo aponta para a etiologia → a etiologia define a investigação**.
- Justifica slide 2 do palestrante Marcela.
- Figuras: `slide-02.png` (5 mecanismos do edema lado a lado).

**3.2 — Localizado × sistêmico, agudo × crônico — onde olhar primeiro**

- Dois eixos de classificação que orientam o raciocínio diagnóstico:
  - **Localizado/unilateral × sistêmico** — edema de uma perna só puxa para causas locais; edema simétrico nos 4 membros puxa para sistêmico (renal, hepático, cardíaco).
  - **Agudo (horas-dias) × crônico (semanas-meses)** — agudo sugere TVP, celulite, angioedema, trauma; crônico sugere IC, cirrose, síndrome nefrótica, insuficiência venosa.
- Edema localizado/agudo — diagnósticos a descartar: **TVP** (assimetria, dor à palpação da panturrilha, fatores de risco), **celulite/erisipela** (eritema, calor, febre), **artrite/sinovite** (dor articular, sinal flogístico), **angioedema** (face, lábios, língua — pode obstruir via aérea), **trauma**.
- Edema sistêmico/simétrico — investigar as 4 etiologias da PARTE III: **renal** (nefrótica/nefrítica/DRC), **hepática** (cirrose), **cardíaca** (IC), **outras** (venosa crônica bilateral, medicamentoso, tireoide).
- A anamnese é o filtro decisivo: paciente nega dispneia → IC sobe na lista mas precisa exame; paciente refere aumento abdominal + etilismo → cirrose sobe; paciente refere urina espumosa → nefrótica sobe.
- Justifica slides 6, 7, 10, 12, 14 do palestrante.

**3.3 — Edema de origem renal — nefrótica × nefrítica × DRC/IRA**

- **Síndrome nefrótica** = perda maciça de proteína na urina (>3,5 g/24h) por dano à barreira de filtração glomerular. Tríade: **edema + proteinúria pesada + hipoalbuminemia**. Acompanhantes: hipercolesterolemia (fígado compensa perda proteica fabricando lipoproteína), trombose (perda de proteínas anticoagulantes como antitrombina), infecções (perda de imunoglobulinas), disfunção renal eventualmente.
  - **Mecanismo do edema:** πp cai (hipoalbuminemia) → desequilíbrio Starling favorece saída → edema generalizado (anasarca em casos graves), com componente facial (manhã) e periorbital característico.
  - **Causas:** diabetes mellitus, lesões mínimas (criança), GESF (primária ou secundária a obesidade/HAS/HIV), nefropatia membranosa (primária ou secundária a neoplasia, hepatite B, drogas, LES), amiloidose.
- **Síndrome nefrítica** = inflamação glomerular ativa. Tríade: **edema moderado + hipertensão + hematúria** (cilindros hemáticos no sedimento). Acompanhantes: disfunção renal aguda em graus variados, proteinúria geralmente <3,5 g/24h (sub-nefrótica).
  - **Mecanismo do edema:** retenção primária de Na⁺ e água pelo rim inflamado → Pc sistêmico sobe → edema, geralmente menos volumoso que na nefrótica.
  - **Causas:** **GNPE** (glomerulonefrite pós-estreptocócica em criança), nefropatia por IgA (adulto jovem após infecção de via aérea), nefrite lúpica, vasculites ANCA-associadas, membranoproliferativa (associada a neoplasia, LES, HCV, esquistossomose).
- **DRC e IRA** — perda de função renal por dano estrutural prolongado (DRC) ou queda abrupta (IRA). Edema vem por retenção hidrossalina + hipertensão volume-dependente. DRC acompanha-se de anemia (eritropoetina cai), distúrbios do perfil osteometabólico (cálcio, fósforo, PTH, vitamina D), uremia (sintomas pelo acúmulo de produtos nitrogenados), distúrbios hidroeletrolíticos e ácido-base, hipervolemia. Etiologias clássicas: diabetes, HAS, glomerulopatias crônicas, doença renal policística autossômica dominante. IRA classifica-se em pré-renal (perfusão), renal (parênquima) e pós-renal (obstrução).
- Investigação: **urina 1** (sedimento — hemácias, leucócitos, cilindros), **proteinúria de 24h** ou relação proteína/creatinina em amostra, **albumina sérica**, **creatinina e ureia**, **TFG estimada**, **USG dos rins e vias urinárias**, **biópsia renal** quando indicado para diagnóstico etiológico.
- Justifica slides 15–26 do palestrante.
- Figuras: `slide-16.png` (síndrome nefrótica componentes), `slide-19.png` (síndrome nefrítica componentes), `slide-26.png` (investigação).

**3.4 — Edema de origem hepática — cirrose, hipertensão portal, ascite**

- **Cirrose** = desorganização da arquitetura lobular do fígado, definida histologicamente por **fibrose + formação de nódulos regenerativos**. É via final comum de inúmeras agressões crônicas.
- **Causas:** etilismo, doença hepática esteatótica metabólica (antiga DHGNA, ligada à síndrome metabólica), hepatites virais B e C, doenças autoimunes (HAI — hepatite autoimune, CBP — colangite biliar primária, CEP — colangite esclerosante primária), hemocromatose, doença de Wilson, hepatopatia congestiva (IC direita crônica que congestiona o fígado).
- **Consequências** dividem-se em dois grandes blocos:
  - **Insuficiência hepática:** queda da síntese proteica → albumina cai → πp despenca → edema generalizado. Fatores de coagulação caem → coagulopatia. Bilirrubina não conjugada não vira conjugada → icterícia. Função detoxificadora cai → encefalopatia hepática (acúmulo de amônia atravessa BHE e altera função neuronal).
  - **Hipertensão portal:** fibrose comprime os sinusoides → resistência ao fluxo portal sobe → pressão portal sobe. Consequências: **ascite** (Pc no leito esplâncnico sobe + queda de πp + ativação do SRAA → líquido extravasa para a cavidade peritoneal), **peritonite bacteriana espontânea** (PBE — infecção do líquido ascítico), **hemorragia digestiva alta** (varizes esofágicas e gástricas se rompem), **encefalopatia hepática** (shunts portosistêmicos desviam amônia do fígado), **carcinoma hepatocelular** (CHC — risco anual significativo em cirrótico).
- **Sinais clínicos clássicos** que aparecem ao exame e gritam "cirrose": **unhas de Terry** (leito ungueal esbranquiçado por hipoalbuminemia), **ginecomastia** (fígado não metaboliza estrógenos → acúmulo periférico), **telangectasias** (em geral em face e tórax superior, mecanismo igual), **circulação colateral abdominal** (cabeça de medusa periumbilical — shunt portossistêmico), **rarefação de pelos** (corporais e axilares por desequilíbrio hormonal), **atrofia testicular** (mesmo mecanismo do estrógeno aumentado), **eritema palmar**, **icterícia**, **ascite** (palpação revela macicez deslocável e/ou semicírculo de Skoda), **edema MMII**, **flapping** (asterixis, sinal de encefalopatia).
- Investigação: **bilirrubinas + transaminases + albumina + INR + plaquetas** (avalia função e síntese), **USG abdominal com Doppler** (avalia parênquima, vasos portais, ascite), **endoscopia digestiva alta** (rastreia varizes), **paracentese diagnóstica** se houver ascite (descarta PBE).
- Justifica slides 27–36 do palestrante.
- Figuras: `slide-32.png` (insuficiência hepática × hipertensão portal), `slide-36.png` (sinais clínicos clássicos da cirrose).

**3.5 — Edema de origem cardíaca — IC, ICFER × ICFEP, NYHA + outras causas sistêmicas**

- **Insuficiência cardíaca** = conjunto de sinais e sintomas decorrentes de **falha do coração em ofertar fluxo sanguíneo adequado aos tecidos**, ou em fazê-lo às custas de pressões de enchimento elevadas. Não é doença única, é síndrome de via final comum.
- **ICFER × ICFEP** — divisão funcional por fração de ejeção:
  - **ICFER** (IC com fração de ejeção reduzida, FE ≤40%): coração não consegue ejetar; câmara dilata-se, parede afina, contratilidade cai. Causas comuns: isquêmica (pós-IAM), dilatada idiopática, chagásica, alcoólica.
  - **ICFEP** (IC com fração de ejeção preservada, FE ≥50%): coração ejeta bem mas não enche; parede hipertrofiada e rígida, complacência cai. Causas comuns: hipertensiva, infiltrativa (amiloidose), constrição pericárdica, obesidade/síndrome metabólica.
- **Manifestações clínicas comuns às duas formas:** dispneia aos esforços, ortopneia, dispneia paroxística noturna, tosse seca, edema. Achados de exame físico — **B3** (galope ventricular, mais comum na ICFER), **refluxo hepatojugular**, **estase jugular**, estertores crepitantes, hepatomegalia.
- **Mecanismo do edema:** débito cai → SRAA ativa → retém Na⁺ e água + vasoconstrição → pré-carga sobe → coração já no platô da curva Frank-Starling não converte volume em débito → pressões venosas sobem → **Pc capilar sistêmico sobe** → edema MMII, ascite, anasarca em casos avançados.
- **Classificação NYHA** (classe funcional pelo grau de dispneia/limitação):
  - **NYHA I** — sem limitação às atividades habituais.
  - **NYHA II** — dispneia aos esforços habituais (subir 1 lance de escada com pausa).
  - **NYHA III** — dispneia aos pequenos esforços (atividades menores que habituais).
  - **NYHA IV** — dispneia em repouso ou ao mínimo esforço.
- **Causas etiológicas da IC:** **hipertensiva** (HAS crônica → HVE → ICFEP/ICFER), **isquêmica** (DAC → IAM → perda de miocárdio → ICFER), **valvopatias** (sobrecarga crônica de pressão ou volume), **infecciosas** (Chagas é importante na América Latina), **tóxicas** (alcoólica, quimioterápicos cardiotóxicos), **outras** (amiloidose, hemocromatose, sarcoidose).
- **Investigação:** **BNP/NTproBNP**, **RX tórax + ECG**, **ecocardiograma** (define FE, valvopatias, derrame pericárdico), **pesquisa etiológica** orientada pelo quadro (cinecoronariografia, ressonância, biópsia).
- **Outras causas sistêmicas de edema** (não compõem PARTE separada por economia — entram aqui na cauda da PARTE III):
  - **Insuficiência venosa crônica** — incompetência valvar venosa nos MMII → Pc local sobe → edema vespertino, melhora à elevação dos membros, varizes visíveis, eczema venoso, úlceras de estase em casos avançados.
  - **Linfedema** — pode ser pós-cirúrgico (esvaziamento axilar pós-câncer de mama), pós-radioterapia, parasitário (filariose); edema "fibrosado", sinal de Stemmer (não consegue pinçar a pele do segundo pododáctilo).
  - **Medicamentoso** — bloqueadores de canal de cálcio (especialmente anlodipino, retém líquido por vasodilatação arteriolar), AINE (retêm sódio renal), corticoide (efeito mineralocorticoide), tiazolidinedionas, estrógenos.
  - **Endócrino** — hipotireoidismo (mixedema — mucopolissacarídeos no interstício, sem cacifo característico), hipertireoidismo (mecanismo de IC de alto débito).
  - **Gestação** — fisiológico no 3º trimestre por compressão da veia cava inferior pelo útero gravídico.
- Justifica slides 42–57 do palestrante.
- Figuras: `slide-44.png` (sinais de IC ao exame), `slide-48.png` (ICFER × ICFEP comparativo), `slide-52.png` (classificação NYHA), `slide-57.png` (lista completa de causas de edema).

### Conclusão integradora (4 camadas, slide-livre)

1. **Princípio unificador:** os três sintomas — dor torácica, dispneia e edema — são portas de entrada do paciente no consultório, e o trabalho do clínico em todos eles é o mesmo: **hierarquizar hipóteses por probabilidade pré-teste, eliminar causas graves primeiro, e usar exames como ajuste, não como pesca**. A semiologia bem feita não substitui exames complementares, mas decide quais pedir.
2. **Mecanismo nuclear:** as **forças de Starling** explicam metade da história — o edema, mas também o estertor pulmonar da IC esquerda (Pc capilar pulmonar sobe) e a ascite da cirrose (Pc esplâncnica sobe). A outra metade é **raciocínio probabilístico**: cada achado clínico move a probabilidade pós-teste do diagnóstico, e o clínico que conhece o LR de cada achado decide melhor.
3. **Clínica retomada — a IC como nó convergente:** a insuficiência cardíaca aparece nas três PARTES — como diferencial obrigatório na dor torácica (isquêmica), como causa comum de dispneia crônica e aguda (descompensada), e como etiologia central do edema sistêmico (Pc venosa elevada). Reconhecer IC com fluência é destravar 1/3 dos casos clínicos do plantão de clínica médica.
4. **Projeção:** o PDF 2 ("Fundamentos do bom clínico" — Osler, uso racional do laboratório, MCP/bioética) trata do **como pensar/decidir/conduzir** — a moldura ética e cognitiva que envolve o raciocínio diagnóstico aqui apresentado. Os dois PDFs juntos cobrem o curso introdutório da Liga.

### Resumindo (1–2 páginas)

10–12 seções ordenadas por relevância clínica para prova: Modelo hipotético-dedutivo + tipo 1/2 · 5 grandes diferenciais de dor torácica letal · ECG na dor torácica aguda · Dispneia aguda × crônica + 6 causas comuns · Likelihood ratio na prática · BNP/NTproBNP · 4 forças de Starling + 5ª (permeabilidade) + 6ª (linfática) · Síndrome nefrótica × nefrítica · Cirrose: IH + HP + sinais clássicos · ICFER × ICFEP + NYHA · Sinais físicos de congestão (B3, refluxo hepatojugular, estase) · Outras causas sistêmicas de edema.

## Seção C — Termos-nota obrigatórios (alvo 8)

1. **probabilidade pré-teste** — probabilidade estimada de uma hipótese diagnóstica antes da realização de um exame complementar; depende de epidemiologia, anamnese e exame físico.
2. **likelihood ratio (LR)** — razão entre a probabilidade de um achado em pacientes com a doença e em pacientes sem a doença; converte probabilidade pré-teste em pós-teste.
3. **dispneia** — percepção subjetiva de incapacidade de respirar confortavelmente; sintoma, não sinal.
4. **ortopneia** — dispneia que aparece ao deitar e melhora ao sentar; típica de IC esquerda por redistribuição de volume.
5. **dispneia paroxística noturna (DPN)** — episódio de dispneia que acorda o paciente no meio do sono, melhora ao sentar à beira do leito; típica de IC.
6. **ascite** — acúmulo de líquido na cavidade peritoneal; em adulto, hipertensão portal é a causa mais frequente.
7. **fração de ejeção (FE)** — fração do volume diastólico final que o ventrículo ejeta na sístole; normal 55–70%, ICFEP ≥50%, ICFER ≤40%.
8. **refluxo hepatojugular** — elevação sustentada da veia jugular durante compressão hepática por 10–30s; sinal de congestão venosa sistêmica, sugere IC direita.

## Seção D — Pontos de quebra do raciocínio (insumo para boxes)

**PARTE I:**
- D1.1 — Aluno tende a achar que ECG normal exclui IAM. **Falso** — IAM sem supra (IAMSSST) pode ter ECG inicial normal em 30–50% dos casos; troponina seriada decide. **→ `#atencao-box` central da PARTE I (em 1.2).**
- D1.2 — Aluno acha que "pedir todos os exames" é raciocinar. Exame só agrega se move a probabilidade; pedir tudo dilui o raciocínio e aumenta achados incidentais. → prosa inline em 1.1.
- D1.3 — Aluno acha que reconhecimento de padrão (tipo 1) é "intuição mágica". Na verdade, é script de doença bem treinado. Tipo 1 funciona quando o caso bate no script; falha em apresentações atípicas. → prosa inline em 1.4.
- D1.4 — Aluno confunde escore (HEART, Wells) com diagnóstico. Escore só calibra probabilidade; quem decide conduta é o clínico integrando o escore com contexto. → prosa inline em 1.4.

**PARTE II:**
- D2.1 — Aluno confunde dispneia com fadiga. Paciente diz "estou cansado" e o clínico precisa perguntar dirigido para diferenciar — caminho de investigação muda. → prosa inline em 2.1.
- D2.2 — Aluno acha que SpO₂ normal exclui doença pulmonar. SpO₂ no esforço pode dessaturar mesmo com SpO₂ basal normal — daí o teste da caminhada de 6 min. → prosa inline em 2.4.
- D2.3 — Aluno acha que BNP normal exclui IC. **Quase** — BNP <100 tem LR ≈0,1, reduz muito a probabilidade mas não zera; ICFEP precoce pode ter BNP normal. → prosa inline em 2.4.
- D2.4 — Aluno confunde ortopneia com DPN. Ortopneia = dispneia ao deitar; DPN = acorda no meio do sono. Mecanismos parcialmente sobrepostos mas distintos. → prosa inline em 2.3.

**PARTE III:**
- D3.1 — Aluno acha que síndrome nefrótica e síndrome nefrítica são "a mesma coisa, só diferença de intensidade". **Falso** — mecanismos distintos: nefrótica é dano à barreira de filtração (perde proteína sem inflamação significativa); nefrítica é inflamação glomerular ativa (perde sangue e função renal aguda). → `#confusao-prevista` em 3.3.
- D3.2 — Aluno acha que toda ascite é cirrose. Ascite tem 4 grandes causas: cirrose (maioria), IC direita (transudato), carcinomatose peritoneal (exsudato), TB peritoneal. Paracentese com gradiente albumina sero-ascítica decide. → prosa inline em 3.4.
- D3.3 — Aluno acha que B3 sempre é patológica. Em jovens com parede elástica pode ser fisiológica; em adulto com IC é alarme. → prosa inline em 3.5.
- D3.4 — Aluno acha que edema bilateral é sempre sistêmico (renal/hepático/cardíaco). Insuficiência venosa crônica bilateral também dá edema bilateral, e linfedema bilateral existe. → prosa inline em 3.5.
- D3.5 — Aluno acha que bloqueador de canal de cálcio "causa IC" porque o paciente desenvolveu edema. Anlodipino causa edema **periférico por vasodilatação arteriolar**, não por congestão venosa — mecanismo distinto, conduta diferente. → `#atencao-box` central da PARTE III (em 3.5).

## Cobertura E2 (planejamento de 30 questões)

- **Consolidação (Q01–Q10) — 10:** sarcômero conceitual da dor torácica isquêmica (1Q), causas graves de dor torácica letal (1Q), modelo hipotético-dedutivo (1Q), tipos de raciocínio (1Q), dispneia × fadiga (1Q), 6 causas comuns de dispneia crônica (1Q), forças de Starling (1Q), nefrótica × nefrítica (1Q), sinais clássicos da cirrose (1Q), ICFER × ICFEP (1Q). Todas com formato "Por que / Como / O que explica" sempre que possível (canônico 2026-05-28 — consolidação ativa).
- **Integração (Q11–Q25) — 15:** todas com `Qxx conecta [A]+[B]` em `arquivos-trabalho/integracao-mapa-liga-clinica-sintomas.md`. Cruzamentos planejados:
  - Q11 = SCA + ECG (anatomia coronariana × derivações).
  - Q12 = TEP + Wells (clínica × escore probabilístico).
  - Q13 = Dissecção × dor irradiando + assimetria de pulsos (clínica × exame físico).
  - Q14 = Pericardite + ECG (mecanismo do supra côncavo difuso × pleurítica).
  - Q15 = Dispneia + LR do BNP (probabilidade × biomarcador).
  - Q16 = IC + dispneia × ortopneia × DPN (mecanismo × redistribuição de volume).
  - Q17 = Asma × DPOC + idade/tabagismo (epidemiologia × clínica).
  - Q18 = SpO₂ esforço + diferenciação pulmonar × cardíaca (fisiologia × clínica).
  - Q19 = Forças de Starling + edema de IC × edema da nefrótica (mecanismo × etiologia).
  - Q20 = Nefrótica + complicações (mecanismo × clínica — trombose, infecção, hipercolesterolemia).
  - Q21 = Cirrose + sinais clássicos (mecanismo hormonal × ginecomastia/aranhas vasculares).
  - Q22 = Hipertensão portal + ascite (Starling × SRAA).
  - Q23 = IC + B3 (sarcômero × complacência).
  - Q24 = ICFER × ICFEP + NYHA (mecanismo × classificação funcional).
  - Q25 = Edema por anlodipino × edema por IC (mecanismo de vasodilatação × mecanismo de congestão venosa).
- **Aplicação (Q26–Q30) — 5:** vinhetas clínicas estilo USMLE com paridade ratio ≤ 1.25 em **todas as 30** (canônico 2026-05-29). Ordem invertida obrigatória: distratoras primeiro (25–35 palavras cada com mecanismo plausível-mas-errado), depois a correta calibrada.
  - Q26 — paciente com dor torácica aguda + fator de risco vs paciente jovem com dor pleurítica → escolher hipótese e exame inicial.
  - Q27 — idoso com dispneia progressiva, ortopneia, edema MMII → diagnóstico mais provável e próximo exame.
  - Q28 — paciente com edema sistêmico, urina espumosa, hipoalbuminemia → diagnóstico sindromático e principais complicações esperadas.
  - Q29 — paciente etilista crônico com aumento abdominal e edema MMII → diagnóstico, mecanismo do edema, complicação a rastrear.
  - Q30 — paciente em uso de anlodipino para HAS desenvolve edema bilateral, sem dispneia ou alterações cardíacas/renais → mecanismo do edema e conduta.

## Cobertura E3 (5 discursivas)

- **D1 (≤100 pal):** "Explique por que ECG normal não exclui IAM e qual o próximo passo prático no paciente com alta suspeita clínica e ECG sem alterações." Cobre o ponto de quebra D1.1.
- **D2 (≤100):** "Compare ortopneia e DPN em mecanismo e tempo, e justifique por que ambas são típicas de IC esquerda." Cobre D2.4.
- **D3 (≤100):** "Explique pelas forças de Starling por que a síndrome nefrótica gera edema mais volumoso e generalizado do que a síndrome nefrítica." Cobre D3.1 e 3.3.
- **D4 (≤100):** "Explique o mecanismo da ascite no cirrótico, integrando hipertensão portal, hipoalbuminemia e ativação do SRAA." Cobre 3.4.
- **D5 (≤130):** "Um paciente em uso de anlodipino apresenta edema bilateral de MMII, sem dispneia ou alterações de exame cardíaco/renal. Discuta o mecanismo do edema, a diferença em relação ao edema da IC, e a conduta racional." Cobre D3.5 + 3.5.
