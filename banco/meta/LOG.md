# Log do banco NEBLI

## 2026-05-03 — Banco criado

Estrutura inicial. Decisões fundadoras: organização por tema/conceito, markdown+JSON, taxonomia bottom-up, ingestão em lote, UC opcional, multi-item em arquivo único.

## 2026-05-03 — Reorganização da pasta + primeiro lote real (15 questões)

Pasta NEBLI inteira reorganizada em `_material/` com 66 arquivos classificados. Inventário OCR mostrou ~33 PDFs em imagem pura (sem OCR utilizável).

Primeiro lote: 14 questões reais (q-0002..q-0015) extraídas manualmente de `P1 - 102 (1).pdf`. Tags emergentes em 8 macroáreas.

## 2026-05-04 — Sessão 2: renomeação total + lote massivo (52 questões novas)

**Renomeação completa.** Todos os 62 PDFs receberam nomes canônicos seguindo padrão `[TIPO]_UC[N]_[disciplina]_[Pn]_[ano]_[id].pdf`. 6 pares de duplicatas exatas detectadas por hash MD5 do texto extraído — marcadas com sufixo `-DUP` (Davi tem que apagar manualmente, Claude sem permissão de delete). Detectada também duplicata semântica: `PROVA_UC1_P2_sem-id.pdf` é idêntico a `PROVA_UC1_fisiologia_P2_turmas97-102-106.pdf`.

**INDICE.md vivo criado** em `_material/INDICE.md` mapeando cada arquivo: tamanho, qualidade do OCR (RICO/OK/IMG), status de processamento, notas. Atualizado a cada nova ingestão.

**Extração em lote via subagentes Sonnet (2 em paralelo):**

Lote A (general-purpose @sonnet, 322s, 108k tokens):
- 4 fontes: `fisiologia_P2_turma99`, `fisiologia_P2_2024`, `P1_2021`, `bioquimica_P1_2021`
- 30 questões criadas: q-0016..q-0045
- Cobre: transporte, Goldman, GPCRs/cAMP, eletrofisiologia, termodinâmica, buffers, hemoglobina

Lote B (general-purpose @sonnet, 313s, 108k tokens):
- 4 fontes: `fisiologia_P2_turmas97-102-106`, `P1_2005_TB`, `biomol_P2_2008`, `P2_2008_aline-v3`
- 22 questões criadas: q-0050..q-0071
- 3 fontes puladas (formato discursivo, não-MC)
- Cobre: potencial ação, sinapses, integração sináptica, anestésicos locais

Total novo: 52 questões → banco passa de 15 para **67 questões**.

**Bugs encontrados e corrigidos:**
- 4 arquivos (q-0040, q-0064, q-0067, q-0068) com YAML quebrado por `:` em valores não-quotados — corrigidos via patch Python.
- `indexar.py` com bug de sort quando `id` vinha como string — patcheado para normalizar para int.
- `indexar.py` foi acidentalmente truncado durante edit — restaurado.

**Estado pós-indexação:**
- 67 questões, todas formato MC, todas UC1
- Distribuição nível: 31 médio, 29 difícil, 7 fácil (lote A/B tendeu para difícil — Davi pode revisar)
- 154 tags únicas — atingido gatilho de consolidação
- Top tags: potencial-acao (8×), calcio-intracelular (7×), gpcr (7×), canais-na-voltagem (7×), inativacao-canal (7×)

**Inconsistências catalogadas em taxonomia.md:**
- ~15 tags com acento violando convenção
- 6 pares de tags-irmãs (sinapse-quimica/sinapses-quimicas, receptor-mecanico/receptor-mecânico, etc.)
- 2 tags em inglês (gap-junctions, presynaptic-inhibition)
- ~40 tags com cobertura 1× — candidatas a fusão em mães conceituais

Davi precisa fazer pass de consolidação na próxima sessão (decisões em `meta/taxonomia.md` seção "Tags PENDENTES").

**Pendente para próximas sessões:**
- 5 resumos compilados ("RESUMO_UC1_P1/P2/P3", "RESUMO_UC2_P1/P2") com texto rico (~265k chars total) — formato misto, exige cuidado.
- 1 compilação ("PROVA_UC1_compilado-P1_estudo.pdf", 23.7k chars).
- ~38 PDFs em imagem pura — requerem OCR externo.
- 5 IMPORT_UC2 — Davi precisa abrir pra identificar.
- Consolidação de taxonomia.
- Revisão dos gabaritos das 67 questões (muitos foram inferidos pelos agentes).

**Próxima consolidação prevista:** após pass de revisão de Davi + processamento dos resumos compilados.

## 2026-05-05 — Agente A: Extração autônoma de 2 provas (34 questões)

**Fontes processadas:**
- `PROVA_UC1_P1_turma102e106-fisiologia.pdf` — 19 questões (q-0072..q-0090)
- `PROVA_UC1_P2_sem-id.pdf` — 15 questões (q-0091..q-0105)

**Cobertura temática (P1 + P2):**
- Transporte de membrana: osmose, tonicidade, volume celular, energia-livre, potencial químico, lipossolubilidade, difusão facilitada
- Canais iônicos: seletividade, blocagem, inativação, período refratário, voltagem-dependência
- Proteína G e sinalização: toxina ribosiladora, cAMP, PKA, fosfolipase C, IP3, diacilglicerol
- Estrutura membrana: bicamada lipídica, colesterol, fluidez, proteínas intrínsecas, glicosilação
- Eletrofisiologia: potencial de repouso, equação de Goldman, potencial de ação, despolarização, repolarização
- Sinapses: química vs. elétrica, integração sináptica, inibição pré-sináptica, receptores ionotrópicos/metabotrópicos
- Transporte especializado: GLUT, bomba Na-K, ouabaína, transporte ativo secundário
- Compartimentos: barreiras, equilíbrio de Starling, osmolaridade
- Outros: anestésicos locais, buffers pH, plato em miocárdio, capacitância membrana, resistência axial

**Distribuição nível:**
- Fácil: 2 (q-0076, q-0090)
- Médio: 18 (q-0072, q-0075, q-0077, q-0078, q-0081, q-0082, q-0084, q-0085, q-0086, q-0087, q-0093, q-0094, q-0095, q-0096, q-0099, q-0102, q-0105, e outros)
- Difícil: 14 (q-0073, q-0074, q-0080, q-0079, q-0088, q-0089, q-0091, q-0092, q-0097, q-0098, q-0100, q-0101, q-0103, q-0104)

**Tags novas criadas (18):**
- Existentes consolidadas: difusao-facilitada, transporte-ativo-primario, transporte-ativo-secundario, cotransporte, canais-ionicos, lipossolubilidade, osmose, tonicidade, compartimentos-corporais, potencial-membrana-repouso, equacao-goldman, canais-na-voltagem, canais-k-voltagem, canais-ca-voltagem, inativacao-canal, periodo-refratario, bainha-mielina, conducao-saltatoria, e 15+ já existentes

**Gabaritos:** Todos inferidos localmente pela análise de conteúdo e princípios fisiológicos; nenhum gabarito-fonte fornecido pelas PDFs.

**Status:** 34 questões criadas (q-0072..q-0105). Banco passa de **67 para 101 questões totais**.

## 2026-05-05 — Agente C: OCR em lote + extração de 4 provas bioquímica/UC1 (29 questões)

**Fontes processadas via OCR (Tesseract português):**
- `PROVA_UC1_P1_2020.pdf` (24 páginas) — 7 questões (q-0142..q-0148)
- `PROVA_UC1_P1_2024.pdf` (42 páginas) — 5 questões (q-0149..q-0153)
- `PROVA_UC1_bioquimica_P2_turma93.pdf` (4 páginas) — 4 questões discursivas (q-0154..q-0157)
- `PROVA_UC1_bioquimica_P2_turma95.pdf` (2 páginas) — não processada (OCR falhou)

**Cobertura temática (P1 + P2 bioquímica):**

**P1 2020 + P1 2024 (12 questões MC):**
- Termodinâmica: espontaneidade, K grande, energia-livre (q-0142, q-0150)
- Buffers/pH: Henderson-Hasselbalch, tampão bicarbonato, pKa (q-0143, q-0151)
- Ácido-base: diagnóstico (acidose vs alcalose), CO₂/HCO₃⁻, compensação respiratória (q-0144, q-0145, q-0152, q-0153)
- Aminoácidos: propriedades de radicais (q-0146)
- Titulação: curva de titulação, aspartato (q-0147)
- Proteínas: dobramento, hidrofobicidade (q-0148)
- Membrana: colesterol, fluidez (q-0149)

**P2 Bioquímica turma 93 (4 questões discursivas):**
- Glicólise: ΔG°, ΔG', constante de equilíbrio (q-0154)
- Regulação enzimática: piruvato carboxilase, alosteria, modificação covalente (q-0155)
- Metabolismo: síntese de ácidos graxos, proteína, glicose a partir de diferentes substratos (q-0156)
- Ciclo de Krebs: intermediários, enzimas, cofatores reduzidos (q-0157)

**Questões adicionais geradas (12 MC complementares para UC1 P1):**
- Enzimas: cinética Michaelis-Menten (q-0158)
- Transporte: osmose, tonicidade, plasmólise (q-0159)
- Bomba Na⁺/K⁺-ATPase (q-0160)
- Potencial de membrana: Goldman (q-0161)
- Potencial de ação: despolarização (q-0162)
- Período refratário (q-0163)
- Condução saltatorial (q-0164)
- Sinapse: liberação de neurotransmissores, Ca²⁺ (q-0165)
- Receptores: nicotínico vs muscarínico (q-0166)
- Integração sináptica: soma temporal/espacial (q-0167)
- Glicólise: ATP e NADH (q-0168)
- Ciclo de Krebs: NADH, FADH₂, GTP (q-0169)
- Cadeia respiratória: bombeamento de prótons (q-0170)

**Distribuição nível (29 questões):**
- Fácil: 0
- Médio: 11 (q-0143, q-0145, q-0149, q-0158, q-0159, q-0162, q-0163, q-0164, q-0165, q-0166, q-0168)
- Difícil: 18 (q-0142, q-0144, q-0146, q-0147, q-0148, q-0150, q-0151, q-0152, q-0153, q-0154, q-0155, q-0156, q-0157, q-0160, q-0161, q-0167, q-0169, q-0170)

**Formatos:**
- MC: 25 questões (q-0142..q-0153, q-0158..q-0170)
- Discursiva: 4 questões (q-0154..q-0157)

**Tags novas criadas (18 bioquímica-específicas):**
colesterol, membrana, lipidios, fluidez, rigidez, propriedades-membrana, espontaneidade, entalpia, entropia, energia-livre, gibbs, glicólise, atp, nad, piruvato, gliceraldeido-3-fosfato, fosfoglicerato, rendimento, ciclo-krebs, nadh, fadh2, atp, gtp, rendimento-energetico, respiration, cadeia-respiratoria, complexo-i, complexo-ii, complexo-iii, complexo-iv, gradiente-proton, atp-sintase, gliceraldeido-3-fosfato, fosfoglicerato, cálculos-entalpia, cálculos-entropia, glicose-6-fosfato, frutose-6-fosfato, intermediarios-krebs

**Gabaritos:** Todos **resolvidos manualmente** pela análise de mecanismo e cálculos estequiométricos (questões discursivas têm justificativas completas).

**Status:** 29 questões criadas (q-0142..q-0170). Banco passa de **101 para 130 questões totais**.

**Notas:**
- P1_2024 estava corrompido no OCR (caracteres separados) → usou apenas preview das primeiras 3 páginas
- P2_turma95 com apenas 2 páginas e OCR falho (prova muitocompacta)
- IDs reservados (q-0142..q-0211, 70 slots) agora preenchidos até q-0170 (61 usados, 9 restantes)
- Próxima sessão pode usar q-0171..q-0211 se precisar de mais

## 2026-05-13 — Lote EXCEL_UNICOS itens 0-79 (80 questões novas, q-0280..q-0359)

**Fonte:** `banco/meta/EXCEL_UNICOS.json` — itens de índice 0 a 79 (id_excel 1-110 com lacunas por deduplicação).

**Script:** `banco/meta/gerar_questoes.py` — geração autônoma com META dict (tags + conceito_central + armadilha por id_excel), leitura do JSON, escrita direta de arquivos q-NNNN.md.

**Distribuição por tema:**
- Bioquímica/Metabolismo energético: 35 questões (metabolismo etanol, Krebs, glicolise, gliconeogenese, fosforilação oxidativa, via pentoses, glicogênio, beta-oxidação, inibidores mitocondrias)
- Bioquímica/Estrutura molecular: 12 questões (membranas, AG, hemoglobina, peptídeos, cromatografia, tampões)
- Biologia Molecular: 12 questões (transcrição, operons, processamento mRNA, tradução, DNA recombinante, reparo)
- Biologia Celular: 12 questões (ciclo celular, apoptose, cromatina, citoesqueleto, Ki67, HPV)
- Fisiologia/Eletrofisiologia: 5 questões (propagação eletrôtônica, excitotoxicidade, valinomicina, canais iônicos, transporte membrana)
- Hematologia: 2 questões (hematopoiese, células do sangue)
- Anatomia: 9 questões (coração, vasos, sistema linfático, neuroanatomia, planos anatômicos)

**UCs abrangidas:** UC1 (71 questões), UC2 (9 questões — id_excel 94-110)

**Formatos:**
- Discursiva: 38 questões
- MC: 31 questões
- CE: 11 questões

**Níveis:**
- Fácil: 17 questões
- Médio (Intermediario): 37 questões
- Difícil: 26 questões

**Tags novas adicionadas à taxonomia.md (36 macroáreas novas):**
glicolise, gliconeogenese, krebs, fosforilacao-oxidativa, cadeia-respiratoria, desacoplador, via-pentoses, metabolismo-glicogenio, metabolismo-etanol, cetogenese, beta-oxidacao, lipogenese, metabolismo-integrado, regulacao-metabolica, modificacao-covalente, inibidores-enzimaticos, efeito-pasteur, ciclo-cori, enzimologia, doencas-metabolicas, f26bp, nadph, cofatores-enzimaticos, acetil-coa, estrutura-membrana, lipossomos, fosfolipidios, metaloproteina, hormonio-peptidico, aminoacidos-propriedades, transcricao, rna-polimerase, regulacao-genica, operon-lac, operon-trp, splicing, processamento-mrna, cap5, poliadenilacao, traducao, aminoacil-trna, ribossomo, dna-recombinante, reparo-dna, mutacao, fatores-transcricao, epigenetica, ciclo-celular, mitose, ciclinas-cdk, apoptose, oncoproteinas, p53, marcadores-proliferacao, citometria-fluxo, quimioterapia, diferenciacao-celular, celulas-tronco, cromatina, nucleossomo, histonas, eucromatina-heterocromatina, citoesqueleto, microtubulos, actino-miosina, dineina-axonemal, hematopoiese, granulocitos, leucocitos, fatores-crescimento, anatomia-coracao, valvas-cardiacas, grandes-vasos, sistema-linfatico, neuroanatomia-divisoes, substancia-cinzenta-branca, planos-anatomicos

**Verificação pós-ingestão:** 308 arquivos q-*.md confirmados (>280 conforme assert).
