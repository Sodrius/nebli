# Curadoria AnKing — biomol-25-mutacao-reparo-recombinacao

**Título:** Mutação, reparo e DNA móvel
**UC/Prova:** UC02/P? · **Gerado em:** 2026-07-05
**Total curado (kept):** 46 · **Alvo:** 30–50 · **Cobertura AnKing:** 5/9 COBERTOS (3 parciais, 1 lacuna)
**Tag-âncora:** `NEBLI::biomol-25-mutacao-reparo-recombinacao`

Perfil **biologia molecular** (mutação/reparo/DNA móvel): o AnKing Step1 cobre com força os tipos de mutação (FA/Bootcamp), o NER/Xeroderma (FA/Pixorize) e toda a genética bacteriana — conjugação, transposição, fago. As lacunas centrais são o reparo direto (fotoliase e MGMT), o SOS (LexA/RecA) e os análogos de base químicos (5-BrU) — conceitos mecanísticos da E1 que o Step1 quase não carda. Esses viram LACUNAS apontando o slide do Prof. PC + Lehninger cap. 25.

## Checklist-alvo (da E1) — fonte-verdade
Fonte: `typst-build/_par_biomol-25-mutacao-reparo-recombinacao/etapa1.typ` (PARTES I–III). Também em `arquivos-trabalho/checklist-biomol-25-mutacao-reparo-recombinacao.tsv`.

| id | Frase-alvo (o que um card teria que testar) | Termos de busca |
|---|---|---|
| 1.1 | Tipos de mutação: substituição (transição/transversão), inserção, deleção, frameshift — efeito de cada um na proteína | point_mutation\|missense\|nonsense\|silent\|frameshift\|transition\|transversion |
| 1.2 | Fidelidade da replicação: proofreading da DNA pol III; tautômeros e deaminação C→U como fontes espontâneas | proofreading\|tautomer\|deamination\|spontaneous_mutation |
| 1.3 | Mutações induzidas: análogos de base (5-BrU, 2-aminopurina) e UV → dímero de pirimidina/timina | base_analog\|5-bromouracil\|UV\|pyrimidine_dimer\|thymine_dimer\|mutagen |
| 2.1 | Reparo direto: fotoliase reverte dímero com luz; MGMT remove metila da O6-metilguanina (enzima suicida) | photolyase\|photoreactivation\|MGMT\|direct_repair\|O6-methylguanine |
| 2.2 | NER/uvrABC: reconhecimento de distorção → excinuclease incisão 8nt/4nt → Pol I preenche → ligase sela | nucleotide_excision_repair\|NER\|uvrABC\|excinuclease |
| 2.3 | Xeroderma pigmentoso: NER defeituoso (AR) → dímeros acumulam → cânceres de pele; SOS: LexA/RecA | xeroderma_pigmentosum\|SOS_response\|LexA\|RecA |
| 3.1 | Plasmídeos como replicons; conjugação F⁺/F⁻ pelo fator F; Hfr; disseminação de resistência | plasmid\|conjugation\|F_factor\|F_plasmid\|Hfr\|antibiotic_resistance |
| 3.2 | Transposons: transposase catalisa salto; IS; transposons compostos (Tn3, Tn5) com resistência | transposon\|transposase\|insertion_sequence\|jumping_genes\|Tn3\|Tn5 |
| 3.3 | Fago lambda: ciclo lítico vs lisogênico; prófago; integração no attB = recombinação sítio-específica | bacteriophage\|phage_lambda\|lysogeny\|prophage\|lytic_cycle\|lysogenic_cycle |

## Camada 1 — tags candidatas (grossa)
Saída de `buscar_tags_lote.py checklist-biomol-25-mutacao-reparo-recombinacao.tsv --md` (999 tags brutas; abaixo só CANDIDATAS on-topic; o resto = RUÍDO — NinjaNerd/OME_banner de cardiologia/renal/farmacologia que casaram por termos amplos como "insertion"/"excision"/"deletion"; alkylating agents de oncofarmaco, cromossomopatias Physeo, vitaminas Sketchy).

| Leaf-tag | #cards | Conceitos | Classe | Decisão |
|---|---|---|---|---|
| FirstAid::01_Biochem::01_Molecular::08_Mutations_in_DNA (subárvore) | 12 | 1.1, 1.2 | CANDIDATA | Camada 2 — tipos de mutação |
| FirstAid::01_Biochem::01_Molecular::07_DNA_repair (subárvore) | 36 | 2.2, 2.3 | CANDIDATA | Camada 2 — NER, Xeroderma, NHEJ, HR, BER |
| Pixorize::01_Biochemistry::10_DNA_Repair (subárvore) | 29 | 2.3 | CANDIDATA | Camada 2 — Xeroderma, Lynch, Ataxia-telangiectasia, Bloom |
| Bootcamp::Microbiology::02_Bacterial_Genetics (subárvore) | 30 | 3.1, 3.2, 3.3 | CANDIDATA | Camada 2 — conjugação, transposição, transdução |
| SketchyPharm::08_Antineoplastics::02_DNA_&_Cellular_Division::01_Alkylating_Agents | 59 | (2.1 parcial) | CANDIDATA | Camada 2 — agentes alquilantes; busca por MGMT |
| Physeo::05_Biochem::04_Genetics::24_Microdeletion_Syndromes e variantes | 41 | — | RUÍDO | rejeita (deleções cromossômicas; E1 ensina deleção de base, não síndrome) |
| NinjaNerd::01_Biochemistry (glicogênio, glicólise, etc.) | 200+ | — | RUÍDO | rejeita (vias metabólicas, fora do escopo) |
| SketchyBiochem::04_Vitamins, SketchyBiochem::05_Clinical_Genetics | vários | — | RUÍDO | rejeita (vitaminas, imprinting; fora do escopo) |

Pool unificado (dedup por note): **156 notes únicos** em `arquivos-trabalho/anking-pool-biomol-25-mutacao-reparo-recombinacao.json`.

> **Sem classe PURA** (canônico 2026-07-04): toda CANDIDATA passa pela Camada 2.

## Camada 2 — curadoria card-a-card (156 lidos → 46 kept)

**KEPT por cluster (46):**

- **Tipos de mutação — hierarquia e efeito (1.1, 9 cards):** eC6.axc5D% (silent=mínimo dano), pXB9u{]WQp (frameshift=máximo dano), h@*st8m~,p (transição=purina→purina), PE:l}h-apM (transversão=purina→pirimidina), ic5$^ZX*`8 (point mutation = 1 nt), r]JU>+9q^n (silent = mesmo aminoácido), I>8b76*:kp (missense = aminoácido diferente; ex: anemia falciforme), mr<L}a>Lp9 (nonsense = stop codon), lEse#5m=+g (frameshift = inserção/deleção não-múltipla de 3).

- **Espontâneas: deaminação e slippage (1.2, 3 cards):** Bi84|O=k+u (deaminação C→U = mutação espontânea ou por calor/HNO₂), kjkdApy8u% (slippage no molde → deleção), sDyd6qUVj) (slippage na fita replicada → inserção).

- **Induzidas: UV/dímero → NER (1.3+2.2, 1 card):** r&`FW|Y2Y# (radiação não-ionizante → dímeros de pirimidina → NER remove; sem NER → xeroderma).

- **NER / uvrABC (2.2, 5 cards):** D+aa%tW(nr (NER repara mutações de UV), lW[I?/0%c~(excinuclease = enzima que excisa dímero), Q.s;;D]DTJ (Pol I + ligase selam após NER), IC[-?&IFM7 (NER ocorre em G₁), c@k7sMQ=X4 (xeroderma = NER defeituoso, herança).

- **Xeroderma pigmentoso (2.3, 4 cards):** #jjn?4~/K (AR, autossômico recessivo), L:P;6~uq#. (pele seca/freckled, fotossensibilidade extrema, cicatriz corneal), Jb9Gw7bgyo (risco para todos os tipos de câncer de pele), qB$u`?AY5k (não consegue reparar dímeros de pirimidina do UVB).

- **Plasmídeos e conjugação / fator F / Hfr (3.1, 5 cards):** e.EMV?Q=L= (plasmídeos = DNA pequeno que se replica independentemente; pode carregar resistência), k`c7C8XTK) (conjugação = pilus sexual, troca de DNA entre bactérias), zz:SZGvcAK (Hfr = plasmídeo integrado ao cromossomo, alta frequência de recombinação), d>157HCw+z (conjugação Hfr transfere DNA cromossômico + plasmídeo), LY!}:t.}<^ (conjugação normal NÃO transfere DNA cromossômico).

- **Transposons e transposição (3.2, 5 cards):** E-pqB(_lO? (VanA = gene transferido via transposição), k@rSelUHzZ (transposon "salta" de um ponto a outro; confer resistência), 7kfGkn!LF (transposon pode pular para um plasmídeo, viajando entre bactérias), qy-^#X]Gk4 (transposição = transferência de resistência entre linhagens), vHd]4o<t0# (vancomicina-resistente se espalha via transposição).

- **Fago lambda: lítico vs lisogênico, transdução (3.3, 14 cards):** O,cjH!MqgS (bacteriófago = vírus de bactéria), KsEZ(/%&6C (transdução = transferência de DNA via bacteriófago), hu+Z.L7gM1 (dois tipos: generalizada e especializada), xOTGW!/!Vb (transdução generalizada: fago lítico), bl@4$z8hs_ (transdução especializada: fago lisogênico), M6bO9o}ogN (generalizada: DNA cromossômico aleatório empacotado no virion), Dyn=#zdaj, (especializada: DNA viral + DNA bacteriano específico adjacente), L<t.E_=<%7 (ciclo lítico: replica, lisa a bactéria), fkEX<Ki}J, (ciclo lisogênico: integra DNA, fica latente, UV aciona ciclo lítico), sJjey-*@a. (fago virulento = só ciclo lítico), r<Z6gLLWl? (fago temperado = ambos os ciclos), i*o2F3tm?- (lisogenia: bactérias não-tóxicas adquirem toxinas), hgn9CST,,1 (transdução generalizada = DNA aleatório), w:{^BM&@rf (transdução especializada = DNA específico).

**DROP (categorias, 110 cards):**
- Mismatch repair (MMR) e Lynch syndrome (Pixorize 35–41, FA cards 18–23): conceito fora do escopo da E1 (E1 menciona MMR apenas de passagem no clinica-box como gancho, sem ensinar o mecanismo).
- NHEJ, HR, ataxia-telangiectasia, Bloom syndrome, Fanconi anemia (FA 31–32, 45–50, 133–141, 145–150): reparo de quebra de fita dupla — não está na E1.
- BER enzimas (glicosylase, AP-endonuclease, lyase: FA 26–30): BER não nomeado na E1; deaminação ensinada em 1.2 mas o sistema de reparo BER não está no escopo.
- SketchyPharm Alkylating agents inteiros (SIADH, ciclofos, busulfan, nitrosoureas, carboplatin, MESNA, etc. — cards 1–2, 33–34, 53–65, 91–128, 142–144, 155–156): farmacologia de antineoplásicos além da linha da E1 (E1 ensina MGMT como desfazedor de lesão alquilante, não os fármacos que a causam).
- Transformation (Bootcamp cards 67–68, 70, 73–74): transformação não ensinada na E1 como mecanismo nomeado.
- Depurinação (FA card 154): não citada na E1.
- Splice site mutation (FA card 12): não ensinada como tipo na E1.
- Ataxia-telangiectasia clinical cards (Pixorize 45–50, 151): não na E1.
- UV → basal cell / SCC clinical oncology (Pixorize 51–52): oncologia clínica além da linha da E1.

## Cobertura por PARTE da E1 (gap-analysis)

### PARTE I — Mutação: o que muda e por que aparece
| id | Cobertura | #cards | Fonte da lacuna (se PARCIAL/LACUNA) |
|---|---|---|---|
| 1.1 Tipos de mutação (substituição transição/transversão, frameshift, missense, nonsense, silent) | COBERTO | 9 | — |
| 1.2 Espontâneas: proofreading da pol III; tautômeros; deaminação C→U | PARCIAL | 3 | slide-Prof.PC + Lehninger cap.25: deaminação e slippage cardados; **tautômeros e proofreading = 0 cards no AnKing** |
| 1.3 Induzidas: análogos de base (5-BrU, 2-aminopurina) + UV → dímero de pirimidina | PARCIAL | 1 | slide-Prof.PC: UV→dímero→NER coberto (r&`FW|Y2Y#); **5-BrU / análogos de base = 0 cards** |

### PARTE II — Reparo: desfazer o erro antes que fixe
| id | Cobertura | #cards | Fonte da lacuna (se PARCIAL/LACUNA) |
|---|---|---|---|
| 2.1 Reparo direto: fotoliase (fotorreativação, dímero pirimidina) + MGMT (O6-metilguanina, suicida) | LACUNA | 0 | slide-Prof.PC + Lehninger cap.25 — **AnKing Step1 não carda fotoliase nem MGMT como mecanismo de reparo**; MGMT aparece somente em contexto de farmaco (resistência a temozolomida) — não usável |
| 2.2 NER/uvrABC: distorção → excinuclease (8nt/4nt) → Pol I → ligase | COBERTO | 5 | — |
| 2.3 Xeroderma pigmentoso (NER defeituoso, AR, cânceres de pele); resposta SOS (LexA/RecA) | PARCIAL | 5 | Xeroderma coberto com força (4 cards + 1 card NER-xero); **SOS response / LexA / RecA = 0 cards** — slide-Prof.PC + Lehninger |

### PARTE III — DNA móvel e recombinação
| id | Cobertura | #cards | Fonte da lacuna (se PARCIAL/LACUNA) |
|---|---|---|---|
| 3.1 Plasmídeos (replicons); conjugação F⁺/F⁻; fator F; Hfr; resistência via conjugação | COBERTO | 5 | — |
| 3.2 Transposons: transposase; IS; Tn compostos (Tn3, Tn5); resistência; transposon→plasmídeo→bactéria | COBERTO | 5 | — |
| 3.3 Fago lambda: ciclo lítico vs lisogênico; prófago; attB; recombinação sítio-específica; transdução | COBERTO | 14 | — |

## Resumo de lacunas → onde completar (proativo)
- **Fotoliase e MGMT (2.1 — LACUNA total):** AnKing Step1 não carda esses mecanismos de reparo direto. Estudar pelo **slide do Prof. PC + Lehninger cap. 25** e pela própria E1, que os ensina em prosa. Fotoliase é específica de bactérias/plantas — sem card dedicado no Step1 porque humanos não a possuem. MGMT aparece no Step1 apenas em contexto de farmacologia de temozolomida (não extraído).
- **Análogos de base como mutagênicos (1.3 — parcial):** 5-BrU, 2-aminopurina, hipoxantina — zero cards no AnKing. Estudar pelo **slide-12 + E1 (mecanismo do 5-BrU)**.
- **Tautômeros e proofreading (1.2 — parcial):** tautomeria como fonte de erros espontâneos de replicação + atividade exonuclease da Pol III — zero cards. Estudar pelo **slide do Prof. PC + E1 (subtópico 1.2)**.
- **SOS response / LexA / RecA (2.3 — parcial):** regulação do reparo de emergência em bactérias — zero cards dedicados. Estudar pelo **slide do Prof. PC + Lehninger cap. 28** (SOS) e E1 (subtópico 2.3).

46 cards do AnKing cobrem bem os tipos de mutação, o NER/Xeroderma e toda a genética bacteriana (conjugação, transposição, fago); as quatro lacunas mecanísticas (fotoliase, MGMT, análogos de base, SOS/LexA/RecA) ficam com o slide + Lehninger, como marcado.
