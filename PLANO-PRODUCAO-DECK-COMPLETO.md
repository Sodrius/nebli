# NEBLI Etimologia — plano de produção do deck completo (v2)

> Reescrito em 2026-07-16 para corrigir um desvio de rota. A v1 virou, na prática, um **deck de terminologia médica organizado por sistema** (260/540 cards eram "raízes por sistema", com linha `Clinical:` como alvo, módulo de farmacologia, etc.). Isso faz decorar o *significado médico* das palavras — exatamente o que **não** queremos. A v2 recentra tudo no objetivo real do Davi.

---

## 0. MISSÃO (a régua que decide tudo)

**O deck ensina ETIMOLOGIA, não conteúdo médico.** O objetivo é dar ao Davi conhecimento de **latim, grego e formação de palavras** — a competência de *decompor e decodificar* qualquer termo novo — para ele aguentar a enxurrada de palavras diferentes ao longo do curso. O termo médico é **exemplo** da regra etimológica, nunca o alvo de memorização.

**O erro canônico a evitar (Davi, 2026-07-16):** colocar no deck cards para decorar o significado de palavras do léxico da saúde. "O que é hepatomegalia?" é vocabulário médico → **fora**. "O radical `hepat/o` vem do grego ἧπαρ (fígado)" é etimologia → **dentro**.

**Teste de admissão de UMA linha (aplicar a todo card, sem exceção):**
> *Se o Davi já soubesse o significado clínico desta palavra, este card ainda ensinaria algo sobre latim/grego/formação de palavras?*
> **Não → o card é vocabulário médico disfarçado → corta.** Sim → é etimologia legítima.

Corolário: o **alvo do cloze** (`{{c1::...}}`) tem que ser sempre um **morfema, uma origem (étimo grego/latino), ou uma regra de formação** — nunca um fato clínico, nunca "o que a doença é/faz".

Fundamentação (pesquisa 2026-07-16): o ensino por raízes decodifica termos novos "de primeira" e reduz a carga de decorar milhares de palavras uma a uma; aprende-se o morfema como item de vocabulário e a etimologia como âncora de memória; a estratégia de leitura é **direita→esquerda** (sufixo → radical → prefixo). Ver `## Fontes`.

---

## 1. O QUE É UM BOM CARD (contrato detalhado — a parte mais importante)

Todo card pertence a **um** dos seis tipos abaixo. Cada tipo tem um alvo de aprendizagem etimológico explícito. **Deck e explicação: TUDO em português.** (Exceção à regra global "card em inglês" — este é o único deck em PT, por ser sobre a língua.)

### Tipo A — Morfema (o átomo)
Ensina UM morfema: forma, sentido operacional, e **origem (grego ou latim, com o étimo)**.
```
Frente:  O radical {{c1::nefr/o}} designa o rim; vem do grego νεφρός (nephrós).
Extra:   Origem: grego. Étimo: νεφρός. Domina em contexto de doença/patologia
         (nefrite, nefropatia). Dupla latina: ren/o (ver card de contraste).
```
Alvo: recuperar o morfema a partir do sentido+origem. NÃO testa nenhum termo clínico.

### Tipo B — Regra de formação (a gramática)
Ensina uma regra de como as peças se juntam. É o que dá **transferência** de verdade.
```
Frente:  Regra da vogal de ligação: o "o" cai quando o sufixo já começa por vogal —
         gastr/o + -ite = {{c1::gastrite}} (não "gastroite").
Extra:   Vogal de ligação (quase sempre "o") só entra para juntar radical+radical ou
         radical+sufixo que começa por consoante. Antes de vogal, cai.
```
Outros: leitura direita→esquerda; radical vs forma combinante; quando NÃO se decompõe.

### Tipo C — Origem grega/latina (a língua em si)
Ensina o étimo antigo e o que ele espalha por várias palavras. Aqui mora o "aprender latim e grego".
```
Frente:  O grego {{c1::dys-}} (δυσ-) significa "mau/difícil/perturbado" e aparece em
         disfunção, dispneia, distrofia.
Extra:   Antônimo grego: eu- (bem). Não confundir com o latim "dis-" (separação:
         dissecar). Produtividade altíssima — vale por dezenas de palavras.
```

### Tipo D — Contraste / dupla grego–latim (o sistema)
Ensina pares que designam a mesma coisa por línguas diferentes, e a divisão de trabalho entre eles.
```
Frente:  Mesmo órgão, duas línguas: grego {{c1::nefr/o}} e latim {{c2::ren/o}} = rim.
Extra:   Regra prática: o grego costuma reger a patologia (nefrite), o latim a anatomia
         (artéria renal). Outros pares: derm/o–cut/o, flebo–ven/o, oftalmo–oculo.
```

### Tipo E — Armadilha / falso amigo / etimologia popular (a segurança)
Ensina onde a decomposição ingênua falha. Evita o erro plausível e confiante.
```
Frente:  Falso amigo: {{c1::angina}} NÃO vem de "raiva"; vem do latim angere (apertar) —
         a ideia é constrição/aperto.
Extra:   Literal ≠ clínico. "Angina" descreve a sensação de aperto, não uma emoção.
         Regra geral: a glosa literal é pista, não definição.
```

### Tipo F — Decodificação guiada (o exercício da habilidade)
O Davi decompõe um termo **usando morfemas já vistos**. O alvo é o processo, não o termo.
```
Frente:  Leia direita→esquerda: hepat/o + -megalia. O sufixo {{c1::-megalia}} significa
         "aumento", então o termo descreve aumento do fígado.
Extra:   Passo 1: sufixo (-megalia = aumento). Passo 2: radical (hepat/o = fígado).
         Passo 3: prefixo (nenhum). Este card treina o MÉTODO, não a palavra.
```
Regra dura do tipo F: **nenhum termo de decodificação pode testar um morfema ainda não ensinado**; e o alvo do cloze é sempre o *morfema/regra*, nunca "a doença".

### Anti-exemplos (o que NUNCA entra)
```
RUIM: "Hepatomegalia é o aumento do {{c1::fígado}}."      → testa fato médico, não etimologia
RUIM: "A hepatite é uma inflamação causada por {{c1::vírus}}." → conteúdo clínico puro
RUIM: "O tratamento da {{c1::pancreatite}} inclui jejum."   → medicina, zero etimologia
RUIM: card de farmacologia/indicação/conduta                → fora de escopo por definição
```
Todo card reprovado no **teste de admissão de uma linha** vira anti-exemplo em `flashcards/ANTI-EXEMPLARES-CARDS.md` com o porquê.

### Regras transversais de forma (todos os tipos)
- **Cloze**: exatamente um `c1` (raros `c1+c2` em contraste tipo D); alvo de 1–3 palavras; resposta inequívoca; sem vazamento (a frente não entrega a resposta).
- **Extra**: PT-BR, 30–70 palavras, teto 90; usa só as linhas necessárias do contrato `Origem / Étimo / Regra / Contraste / Limite / Exemplos`. **`Limit` (literal ≠ clínico) é obrigatório em todo card de tipo E e sempre que houver risco de inferência insegura.**
- **Sem imagem por padrão** (`visual_need=none`). Imagem só resolve tarefa explícita (mapa de família de morfemas, assimilação sonora, uma relação espacial). Proibida imagem decorativa — herda o gate `verificar_imagem_card.py`.
- **Atomicidade**: um morfema/regra por card. Enumeração paralela (um par de dupla) pode ser 1 card com 2 clozes; nunca N cards-irmãos redundantes (ver A18).
- **Áudio**: opcional e seletivo (30–50 étimos gregos/latinos de alto atrito), só no verso. Ensina pronúncia médica contemporânea, não reconstrução do grego antigo.

---

## 2. ESCOPO E MATRIZ (540 cards, reorganizados por ETIMOLOGIA)

A v1 organizava 260 cards "por sistema do corpo" — o vetor do desvio. A v2 organiza pelo **eixo etimológico**: o que se aprende é a língua e a formação, e os sistemas do corpo só fornecem os *exemplos* dos morfemas.

| Módulo | Alvo | O que ensina (alvo de aprendizagem) |
|---|---:|---|
| 01_Fundamentos_de_formação | 40 | prefixo/radical/sufixo/forma combinante; vogal de ligação; leitura direita→esquerda; quando NÃO se decompõe; literal ≠ clínico |
| 02_Grego_vs_Latim | 50 | as duas línguas-fonte; étimos-chave; por que a medicina mistura as duas; registros (patologia grega / anatomia latina) |
| 03_Prefixos | 70 | posição, direção, quantidade, tempo, negação, intensidade — **como unidades de sentido produtivas**, com o étimo |
| 04_Sufixos | 80 | condição, processo, inflamação/tumor, exame, cirurgia — o sufixo como "o que a palavra faz", com o étimo |
| 05_Radicais_de_alto_rendimento | 150 | os radicais que **explicam mais palavras** (não "por sistema": por produtividade), sempre com origem grega/latina |
| 06_Duplas_e_contrastes | 60 | pares grego–latim; alomorfes; variantes EN/PT/latim anatômico; formas confundíveis |
| 07_Armadilhas_e_falsos_amigos | 50 | falsa segmentação, polissemia, etimologia popular, epônimos/acrônimos, híbridos |
| 08_Decodificação_guiada | 40 | o exercício do método em termos compostos, cumulativo, só com morfemas já vistos |
| **Total** | **540** | |

Reserva 0–30 só de erros reais; teto operacional 570; 600 absoluto. `09_Avaliações` (segregado) e `10_Resgate` (vazio) não contam.

**Sequência dentro de cada módulo:** morfema (tipo A) → origem (tipo C) → regra que o rege (tipo B) → contraste/dupla (tipo D) → armadilha (tipo E) → decodificação que o usa (tipo F). Nenhum termo de decodificação testa morfema não ensinado; antes de decodificação, cada morfema apareceu em ≥2 contextos.

**Corpus de exemplos:** os radicais de alto rendimento saem do vocabulário que o Davi encontra no 1º ano (embriologia, histologia, anatomia, fisiologia — as aulas que o NEBLI já cobre), mas o **card testa o morfema/regra**, não o conteúdo daquela aula.

---

## 2.1 INVENTÁRIO-SEMENTE — os morfemas de maior frequência no curso (pesquisa 2026-07-16)

Lista priorizada dos morfemas que **mais aparecem e mais decodificam** ao longo do 1º ano e além. É a fonte de onde cada módulo puxa seus cards-âncora (tipo A) + origem (tipo C). Origem marcada: **(G)** grego · **(L)** latim · **(H)** híbrido/uso misto. Cada item vira ≥1 card; os de altíssima produtividade (⭐) entram primeiro. **O card testa o morfema/origem — nunca o termo-exemplo.**

### Prefixos de alta frequência (~35)
- **Posição/direção:** endo-(G)⭐ / intra-(L) · ecto-(G) / exo-(G) · epi-(G)⭐ · peri-(G)⭐ / circum-(L) · inter-(L) · sub-(L) / infra-(L) · supra-(L) / super-(L) · trans-(L) / dia-(G) · retro-(L) · para-(G)⭐ · ante-(L) / pre-(L) / post-(L)⭐ · meso-(G) · meta-(G) · ab-(L) / ad-(L)
- **Quantidade/tamanho:** mono-(G) / uni-(L) · bi-(L) / di-(G) · tri- · hemi-(G) / semi-(L) · oligo-(G) / poly-(G)⭐ · micro-(G) / macro-(G) · mega-(G) / megalo-(G) · pan-(G)
- **Tempo/velocidade:** brady-(G) / tachy-(G)⭐ · neo-(G)⭐
- **Negação/normalidade:** a-/an-(G)⭐ · in-/im-/il-/ir-(L) · dys-(G)⭐ / eu-(G) · mal-(L)
- **Intensidade/relação/semelhança:** hyper-(G)⭐ / hypo-(G)⭐ · auto-(G) / allo-(G) · homo-/homeo-(G) · hetero-(G) · iso-(G) · syn-/sym-(G)⭐ · pseudo-(G) · anti-(G)⭐ / contra-(L)

### Sufixos de alta frequência (~55) — o eixo de maior rendimento
- **Condição/processo:** -ia · -iasis(G) · -ism · -osis(G)⭐ · -y
- **Doença/inflamação/tumor:** -itis(G)⭐ · -oma(G)⭐ · -pathy(G)⭐ · -malacia(G) · -sclerosis(G) · -stenosis(G) · -necrosis(G) · -ptosis(G) · -cele(G) · -megaly(G)⭐ · -plasia(G) · -trophy(G) · -genesis(G)⭐ · -lysis(G)⭐ · -poiesis(G)
- **Sinais/sintomas:** -algia/-dynia(G)⭐ · -emia(G)⭐ · -uria(G) · -penia(G) · -cytosis(G) · -rrhea(G) · -rrhage/-rrhagia(G) · -spasm(G) · -pnea(G) · -phagia(G) · -phasia(G) · -plegia(G) · -paresis(G) · -phobia(G) · -philia(G)
- **Exames/medidas/registros:** -gram/-graph/-graphy(G)⭐ · -meter/-metry(G) · -scope/-scopy(G)⭐ · -opsy(G) · -logy(G)⭐ / -logist(G)
- **Cirurgia:** -ectomy(G)⭐ · -otomy(G) · -ostomy(G) · -plasty(G) · -pexy(G) · -desis(G) · -rrhaphy(G) · -centesis(G) · -tripsy(G)
- **Agente/especialidade/adjetivos:** -ist / -iatry(G) / -iatrics(G) · -oid(G, "semelhante a")⭐ · -ic/-ac/-al/-ar/-ous (adjetivais)

### Radicais de altíssimo rendimento (~90) — priorizados por quantas palavras explicam
- **Célula/geral:** cyt/o(G)⭐ · hist/o(G) · kary/o(G) · nucle/o(L) · somat/o(G) · morph/o(G) · blast/o(G) · gen-(G, produzir/origem)⭐ · phag-(G, comer) · troph-(G, nutrir) · plas-(G, formar) · stas-(G, parar) · lys-(G, quebrar) · scler-(G, endurecer) · malac-(G, amolecer)
- **Sangue/vasos:** cardi/o(G)⭐ · angi/o(G) / vas/o(L) · arteri/o(G) · phleb/o(G) / ven/o(L) · hem/o-hemat/o(G)⭐ · erythr/o(G) · leuk/o(G) · thromb/o(G) · lymph/o(L) · splen/o(G)
- **Respiratório:** pneum/o-pneumon/o(G) / pulmon/o(L) · bronch/o(G) · trache/o(G) · laryng/o(G) · pharyng/o(G) · pleur/o(G) · thorac/o(G) · spir-(L, respirar)
- **Digestório:** stomat/o(G) · gloss/o(G) / lingu/o(L) · odont/o(G) / dent/o(L) · gastr/o(G)⭐ · enter/o(G)⭐ · hepat/o(G)⭐ · col/o(G) · chol/e(G, bile) · pancreat/o(G)
- **Renal:** nephr/o(G)⭐ / ren/o(L) · cyst/o(G) · ur/o(G) · lith/o(G, pedra)
- **Nervoso/sentidos:** neur/o(G)⭐ · encephal/o(G) · cerebr/o(L) · mening/o(G) · myel/o(G, medula) · psych/o(G) · esthesi/o(G, sensação) · ophthalm/o(G) / ocul/o(L) · ot/o(G) / aur/o(L) · rhin/o(G) · opt/o(G)
- **Musculoesquelético:** oste/o(G)⭐ · arthr/o(G)⭐ · chondr/o(G) · my/o(G)⭐ · ten/o(G) / tendin/o(L) · crani/o(G) · spondyl/o(G) / vertebr/o(L)
- **Endócrino/metabólico:** aden/o(G) · glyc/o-gluc/o(G)⭐ · lip/o(G) / adip/o(L) · thyr/o(G) · adren/o(L)
- **Tegumentar:** derm/o-dermat/o(G)⭐ / cut/o(L) · kerat/o(G) · melan/o(G) · trich/o(G) / pil/o(L)
- **Cores (transversais, muito produtivas):** erythr/o(G, vermelho) · leuk/o(G, branco) · melan/o(G, preto) · cyan/o(G, azul) · xanth/o(G, amarelo) · chlor/o(G, verde) · poli/o(G, cinza)

Fontes do inventário: [Wikipedia — List of medical roots and affixes](https://en.wikipedia.org/wiki/List_of_medical_roots_and_affixes), [OpenMD word parts](https://openmd.com/dictionary/medical-word-parts), [SDR Foundation](https://sdrfoundation.org/medical-terminology-suffix-prefix-combining-forms). Cada morfema aqui recebe, no dossiê, seu **étimo grego/latino real** validado em LSJ / Lewis & Short antes de virar card.

---

## 3. PONTUAÇÃO E PODA (recalibrada para etimologia)

Gate de admissão — o item precisa: (a) ser um morfema/regra/étimo **produtivo** (explica várias palavras) OU uma armadilha de risco real; (b) ter segmentação/origem defensável por fonte linguística; (c) passar no **teste de admissão de uma linha** (§0); (d) acrescentar habilidade não coberta; (e) ser formulável como alvo inequívoco.

| Critério | Pontos |
|---|---:|
| Produtividade (quantas palavras o morfema/regra decodifica) | 0–4 |
| Valor de transferência (ajuda a ler termo novo) | 0–3 |
| Aparece em mais de um sistema/domínio | 0–2 |
| Reduz confusão frequente (contraste/armadilha) | 0–2 |
| Ensina a língua (étimo grego/latino explícito) | 0–2 |
| **É conteúdo médico disfarçado (falha o teste de uma linha)** | **−5 (corte automático)** |
| Interesse só histórico/curiosidade | −2 |
| Favorece inferência insegura sem marcar o limite | −3 |

Limiares: morfema/regra ≥7; contraste ≥6; armadilha ≥5 com risco plausível. Abaixo, vira exemplo no Extra ou corta.

---

## 4. O MEGA-DEBATE MULTI-AGENTE (como gerar os 540 com máxima eficácia)

O norte de eficácia: **cada agente com uma lente única e afiada; críticos baratos em paralelo; síntese cara só no fim; a sessão principal orquestra e é a única que escreve.** Isso contorna o bug F9 (subagente que simula tool call / não dispara Read): **nenhum subagente edita nada — todos só devolvem JULGAMENTO em texto**, no mesmo molde do `card-mirror` que já funciona.

### Unidade de trabalho: o dossiê de família
Antes de qualquer card, a sessão principal monta um **dossiê** de uma família de morfemas (ex.: a família `nefr/o–ren/o` "rim"): formas e alomorfes, sentidos por `sense_id`, **origem grega/latina com étimo**, produtividade, 3–8 termos-exemplo (só como ilustração), contraste, armadilha, e o objetivo de aprendizagem. Um dossiê gera tipicamente 1 morfema + 1 origem + 1 regra aplicável + 1 contraste + (se preciso) 1 armadilha.

### As rodadas do debate (por lote de dossiês)
1. **Proponente** (sessão principal, Opus): rascunha os cards candidatos do dossiê, cada um já marcado com seu **tipo A–F** e alvo de aprendizagem.
2. **Painel adversarial** (subagentes em PARALELO, uma mensagem, modelos baratos, cada um com veto na sua lente):
   - **Etimólogo** (Sonnet): a segmentação e a origem estão corretas? grego vs latim certo? não é etimologia popular?
   - **Guardião anti-vocabulário-médico** (Sonnet) — *o crítico-chave*: este card testa ETIMOLOGIA ou contrabandeia um fato clínico? Aplica o teste de uma linha (§0). **Veto duro.**
   - **Crítico de decodificação** (Sonnet): o card constrói habilidade transferível de decompor, ou é só um par para decorar?
   - **Card-mirror / retenção** (agente `card-mirror` existente): atomicidade, cloze, vazamento, PT natural, indistinguível de bom card real.
   - **Crítico bilíngue/PT** (Haiku): PT-BR natural, nomenclatura oficial, sem tradução artificial.
3. **Síntese/juiz** (sessão principal, Opus): lê os vereditos, **resolve os conflitos** (é aqui que o "debate" acontece — divergências entre etimólogo e guardião viram decisão), reescreve ou mata o card, e aplica a rubrica. Card com qualquer veto aberto não passa.
4. **Registro**: aprovado → lote JSON; reprovado por vocabulário-médico → anti-exemplo com o porquê (alimenta a calibração dos próximos lotes).

### Por que é eficaz (as alavancas)
- **Paralelismo**: os 5 críticos rodam numa tacada só; latência ≈ 1 crítico.
- **Modelos por papel**: críticos em Sonnet/Haiku (baratos, muitos cards), só a síntese em Opus.
- **Lente única por crítico**: julgamento afiado, sem diluição.
- **Veto do guardião**: o erro que queremos extinguir (vocabulário médico) tem um agente dedicado com poder de corte.
- **Reuso**: `card-mirror` e o gate `verificar_imagem_card.py` já existem e entram como estações do painel.
- **Lote por família**: contexto compartilhado, custo amortizado; pesquisa do lote N+1 em paralelo à autoria de N.

Tamanho de lote: 40–60 cards por rodada de debate. Holdout de avaliação separado desde o início.

---

## 5. PIPELINE POR LOTE (gates herdados, com o foco novo)

- **G0 blueprint**: objetivos, morfemas, dependências, holdout congelados.
- **G1 dossiês + fontes**: cada claim mapeado a uma fonte **linguística** e (quando houver termo-exemplo) uma médica.
- **G2 draft**: cards escritos do dossiê (nunca de uma lista/site direto), marcados por tipo A–F.
- **G3 lint/schema**: `validate_etymology.py` — exatamente um `c1`, cloze não vazado, limites de tamanho, **checagem do teste de uma linha por heurística** (flag de termos que parecem alvo clínico), dedup por morfema/família.
- **G4 mega-debate**: painel adversarial + síntese (§4); rubrica aprovada; zero veto aberto.
- **G5 staging + mirror**: render desktop/AnkiDroid, `card-mirror`, dedup, cobertura, zero leakage.
- **G6 auditoria sênior**: amostra cega + 100% dos high-risk (armadilhas, híbridos, disputas de origem).
- **G7 piloto**: liberação gradual + telemetria + teste inédito de decodificação.
- **G8 promoção**: `release_etymology.py` idempotente, suspenso→ativo, rollback testado; nunca toca card alheio.
- **G9 pós-uso**: flags/comentários/leeches viram tickets; erro de origem revalida a família inteira.

Hard gates de lote: 100% fontes, 100% painel, rubrica média ≥19/21, 0 veto de vocabulário-médico, 0 leakage, 0 duplicata injustificada, 100% mirror.

---

## 6. RUBRICA POR CARD — 0 a 3 (recentrada)
- correção **linguística** (segmentação/origem) — obrigatório 3;
- **foco etimológico** (passa o teste de uma linha; não é vocabulário médico) — obrigatório 3;
- valor de transferência/decodificação;
- recuperação/atomicidade/cloze;
- naturalidade PT-BR;
- Extra e limite (literal ≠ clínico onde há risco);
- fontes/direitos.

Gate: ≥18/21, nenhum zero; linguística e foco-etimológico obrigatoriamente 3. **`Blocker`**: fato médico como alvo, falsa etimologia, ambiguidade, licença desconhecida, vazamento de avaliação. **`Major`**: resposta induzida, tradução artificial, redundância, par decorado sem valor de transferência.

---

## 7. PERFIL DO CARD E SCHEMA
- note type `AnKingOverhaul`; perfil `etymology_pt`.
- **Text: PT-BR** (10–24 palavras), um `c1` (1–3 palavras).
- **Extra: PT-BR** estruturado (`Origem / Étimo / Regra / Contraste / Limite / Exemplos`), 30–70 palavras.
- Campo estruturado por card: `tipo` (A–F), `morfema_id` + `sense_id`, `origem` (grego/latim/híbrido), `étimo`, `produtividade`, `inference_class`, `pré-requisitos`, `learning_objective`.
- Produção reversa <10% do deck.
- Fontes como objeto por claim (tipo, obra, URL, verbete, licença, hash). Uma linguística sempre; duas para híbridos/disputas.

---

## 8. FONTES E DIREITOS
Camadas preferenciais, **priorizando as linguísticas** (mudança da v1, que priorizava as médicas):
- **Estrutura de formação**: OER de *Medical Terminology* (OpenRN / Nicolet) como andaime pedagógico.
- **Grego/latim (étimos)**: LSJ (Liddell–Scott–Jones) e Lewis & Short; Wiktionary como ponte com verbete rastreável; duas fontes em casos difíceis.
- **Nomenclatura**: FIPAT / Terminologia Anatomica para as formas oficiais.
- **PT-BR**: DeCS/BVS e nomenclatura oficial para validar a forma usada no Brasil.
- **Termos-exemplo (só ilustração)**: OpenStax/NCBI Bookshelf.
Texto pedagógico é autoral. Decks e livros comerciais são benchmark, não corpus. Toda mídia com fonte, licença, atribuição e hash.

Fundamentação pedagógica e boas práticas pesquisadas em 2026-07-16:
- decodificação por raízes > memorização; aprender o morfema como vocabulário com a etimologia de âncora ([RSIS/IJRISS](https://rsisinternational.org/journals/ijriss/articles/addressing-students-lack-of-latin-knowledge-in-medical-terminology/), [TalentMed](https://talentmed.edu.au/medical-terminology/greek-and-latin-roots-in-medical-terminology/));
- leitura direita→esquerda (sufixo→radical→prefixo) e vogal de ligação ([SDR Foundation](https://sdrfoundation.org/medical-terminology-suffix-prefix-combining-forms), [Sciencefix](https://sciencefix.blog/combining-vowels-secret-medical-terminology-fast));
- duplas grego–latim, híbridos e falsos amigos ([Transcend](https://www.transcendwithwords.com/post/medical-terminology-greek-and-latin-origins-and-word-formation-guidelines), [Wikipedia — medical roots/affixes](https://en.wikipedia.org/wiki/List_of_medical_roots,_suffixes_and_prefixes)).

---

## 9. QA AUTOMÁTICO — `validate_etymology.py`
UID/status únicos; exatamente um `c1`; cloze não vazado por tradução/variante/campo visível; frente e Extra nos limites; **heurística anti-vocabulário-médico** (marca cards cujo alvo é um substantivo clínico sem morfema no cloze); léxico canônico consistente por `morfema_id+sense_id`; reconstrução da forma superficial (regra da vogal de ligação declarada); fonte por claim; high-risk exige armadilha+limite; dedup por morfema/família/similaridade; ausência de termos do holdout em qualquer campo. Cada regra com fixtures ±; todo bug vira teste de regressão.

---

## 10. AVALIAÇÃO, RITMO E ENCERRAMENTO
- **Avaliação segregada** mede **decodificação**, não vocabulário: dado um termo inédito decomponível, o Davi segmenta, dá a glosa literal, aponta origem e marca o limite. "Não sei / não é seguro inferir" é resposta legítima.
- **Ritmo**: 7–10 novos/dia, 6 dias/semana; estudar pelo deck-pai; pausa automática de novos se houver vencidos, retenção <80% ou carga >25 min/dia por 3 dias.
- **Gates de eficácia** (o lote-zero só expande se): ≥85% nos treinados; ≥75% em **termos inéditos decomponíveis** (a métrica que importa — transferência); ≤10% de erro confiante em armadilhas; mediana ≤10 s.
- **Pronto** quando 540 (ou menos) cobrem a matriz etimológica sem enchimento, 100% passam schema/lint + revisão linguística, 0 blocker/major/vazamento, staging idempotente e provas de decodificação prontas.

---

**DECK E EXPLICAÇÃO: TUDO EM PORTUGUÊS.**
**REGRA-MÃE, acima de qualquer outra: se o card não ensina latim/grego/formação de palavras, ele não entra — por mais "médico" e útil que pareça.**
