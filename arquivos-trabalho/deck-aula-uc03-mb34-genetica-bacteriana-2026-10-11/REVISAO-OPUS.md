# Genética bacteriana (MB34): revisão pelo Opus, 11/10/2026

Auditoria somente de leitura. Li as 130 notas via AnkiConnect (114 próprias e 16 compartilhadas), as 44 lâminas (folhas 01–08 e slides.txt), a transcrição inteira, Trabulsi cap. 5 (trechos pertinentes), provas, guia de veteranos (cap. genética) e REVISAO-DE-QUALIDADE.md. Há 13 cards suspensos: 5 próprios de estrutura do DNA (nids ...463885, ...464182, ...464309, ...464484, ...464661) e os compartilhados de BM54/morfologia.

## 1. Erros científicos e afirmações imprecisas

| # | nid (chave) | Texto atual | Problema | Correção proposta |
|---|---|---|---|---|
| E1 | 1791730472458 (transposase) | F: "A transposon is a resistance gene flanked by inverted repeats, and the enzyme {{c1::transposase}} moves it to another site" · E: "The repeats act like adhesive tape that finds a matching sequence" | Um transposon não *é* um gene de resistência: é um segmento móvel que codifica a própria transposase, e a resistência é carga. O Extra diz que a inserção procura uma sequência igual, o que contradiz o card 1791730473811 (a transposição não exige homologia). A frase é literal da professora, mas está errada. | F: "Transposons are mobile DNA segments flanked by **inverted repeats** that encode {{c1::transposase}}, the enzyme that inserts them at a new site" · E: "- Antibiotic resistance genes are the most common cargo between the repeats<br>- Transposase recognizes the inverted repeats; the target site needs no homology" |
| E2 | 1791730469435 (planar-etidio) | E: "SDS (sodium dodecyl sulfate) is another chemical mutagen of this kind" | Errado. O SDS é um detergente aniônico, não uma molécula planar intercalante nem um mutagênico clássico (a lâmina 27 erra ao listá-lo). Além disso, o desenho da lâmina (acridina) mostra a consequência principal, a inserção ou deleção (frameshift), e nenhum card cobra isso. | E: "- Intercalation causes **insertions or deletions (frameshift)** when the strand is copied<br>- Acridine dyes act the same way". Remover a linha do SDS (se quiser, registrar o conflito de fonte no REVISAO). |
| E3 | 1791730475358 (lederberg-tatum) | F: "In the U-tube experiment of Lederberg and Tatum, no recombinants appeared when two auxotrophs were separated…" | Atribuição histórica errada: Lederberg e Tatum (1946) misturaram os auxotróficos, e o tubo em U é de Bernard Davis (1950). A transcrição atribui o tubo a L&T. | F: "In the **U-tube** experiment, two auxotrophic E. coli strains separated by a filter that lets DNA pass gave no prototrophs, so conjugation requires {{c1::cell contact}}" · E: "- Lederberg and Tatum (1946) first got prototrophs by mixing the two auxotrophs; the U-tube (Davis, 1950) showed contact was needed<br>- Only young cultures mixed together produced prototrophic colonies" |
| E4 | 1791730471734 (avery) | E: "Only the nucleic acid fraction transformed the rough strain, and RNA is too unstable" | "RNA is too unstable" não foi o argumento de Avery (é fala da professora). A prova foi enzimática: a DNase abolia a transformação, e RNase e proteases não. | E: "- Only the nucleic acid fraction transformed the rough strain<br>- **DNase** abolished transformation, whereas RNase and proteases did not" |
| E5 | 1791730473686 (ilha-patogenicidade) | F: "A cluster of **transposed** virulence genes in the chromosome forms a(n) {{c1::pathogenicity island}}" | Restrito demais. As ilhas vêm de transferência horizontal (fago, plasmídeo ou transposon), como diz o próprio Trabulsi ("adquiridos por transferência horizontal de genes"). | F: "A chromosomal cluster of **virulence genes acquired by horizontal transfer** is a(n) {{c1::pathogenicity island}}" · E: "- Its G+C content differs from the rest of the genome, revealing where it came from<br>- Transposons can carry plasmid virulence genes into the chromosome" |
| E6 | 1791730474735 (fago-engano) | E: "The phage is a vehicle that attaches by electrostatic attraction" | A adsorção do fago depende de **receptores específicos** da superfície; a eletrostática é só o contato inicial e inespecífico (fala da professora). | E: "- The phage adsorbs to **specific receptors** on the bacterial surface" |
| E7 | 1791730469183 (uv-penetracao) | F: "UV light penetrates **only a few millimeters**…" | Superestima a penetração: a UV mal passa da epiderme ou da derme superficial (menos de 1 mm). A professora disse "1, 2 mm". | F: "UV light barely penetrates tissue, so its mutagenic damage and cancer risk are confined to the {{c1::skin}}" · E: "- Ionizing radiation penetrates deeply<br>- For the same reason UV only sterilizes surfaces" |
| E8 | 1791730465661 (genoma-micoplasma) | F: "The **smallest** bacterial genomes, such as that of Mycoplasma genitalium…" | A lâmina 19 mostra *Candidatus* Carsonella ruddii (0,16 Mb), muito menor. O *M. genitalium* é um dos menores e o menor de cultivo axênico. | F: "Mycoplasma genitalium, one of the smallest bacterial genomes (~0.58 Mb), encodes only about {{c1::480}} genes" |
| E9 | 1791730463508 (supertorcido) | F: "…supercoiled, which **favors the action of** enzymes such as gyrase and topoisomerases" · E: "Gyrase and ATP introduce negative supercoils; topoisomerases relax them" | Frase do Trabulsi, mas circular: são as enzimas que geram ou relaxam a supertorção. O Extra opõe a girase às "topoisomerases", só que a girase *é* uma topoisomerase (II). | F: "Bacterial DNA is negatively {{c1::supercoiled}}, which compacts it and eases strand separation" · E: "- DNA gyrase (topoisomerase II) uses ATP to add negative supercoils; topoisomerase I relaxes them" |
| E10 | 1791730469935 (sos) | F: "activated RecA **cleaves** the LexA repressor" | Imprecisão menor: a RecA* (ligada a ssDNA) é coprotease e estimula a **autoclivagem** da LexA. | F: "In the SOS response, RecA activated by single-stranded DNA triggers self-cleavage of the {{c1::LexA}} repressor, derepressing DNA repair genes" |
| E11 | 1791730470106 (fotoliase) | E: "It is the only lesion that visible light can undo" | O sujeito ("It") é a enzima, mas a frase fala da lesão. Ficou ambíguo. | E: "- Pyrimidine dimers are the only DNA lesion that visible light reverses (direct reversal, no nucleotides removed)". Não criar card para a fala da professora de que humanos têm fotoliase (mamíferos placentários não têm). |
| E12 | 1791730468435 (sentido-errado) | E: "Insertions or deletions shift the reading frame" | Só quando não são múltiplos de 3. | E: "- Insertions or deletions not in multiples of three shift the reading frame" |
| E13 | 1791730469059 (uv-bloqueia) | E: "A covalent bond joins the adjacent pyrimidines" | O dímero é um anel ciclobutano com **duas** ligações covalentes; a própria lâmina 26 diz "covalent bonds". | E: "- Covalent bonds join adjacent pyrimidines on the same strand" |
| E14 | 1791730471859 (transf-especies) | F: "…whereas Escherichia coli preferentially takes up plasmids" | A E. coli não tem competência natural: capta plasmídeos na competência artificial. Como está, o card induz a pensar em transformação natural. | Manter a frente (é da aula). E: "- E. coli is transformed in the lab after CaCl₂ treatment<br>- There is a limit to how much DNA a cell can take up" |
| E15 | 1791730474857 (lisogenico, AnKing) | "phage injects **nuclear** material" | Bactéria não tem núcleo. | Trocar por "genetic material" (sem mexer no resto do texto AnKing). |
| E16 | 1791730474985 (lisogenia-toxina, AnKing) | "non-toxic strains of DNA" | Redação errada no original. | "allows non-toxigenic bacterial strains to obtain toxin genes" |

Observação de baixa prioridade: no compartilhado 1791668521839 (fluoroquinolonas), o Extra diz "Topoisomerase IV prevents sister chromatid from getting twisted"; para bactérias, o correto seria "separates (decatenates) daughter chromosomes". O card é AnKing e compartilhado; ajustar só se o deck de antibióticos concordar.

## 2. Cards ambíguos ou que entregam a resposta

| nid (chave) | Problema | Correção |
|---|---|---|
| 1791730475859 (hfr-def) | A frente entrega a sigla expandida ("Hfr, for high frequency of recombination"). | F: "A cell with the F plasmid integrated into its chromosome is called a(n) {{c1::Hfr}} cell" · E: "- Hfr = high frequency of recombination…" |
| 1791730465408 (plasmideo-perda) | "can be [lost]… so some daughter cells end up without them" responde a própria lacuna. | F: "{{c1::Low-copy-number}} plasmids can be lost during cell division, so some daughter cells end up without them" |
| 1791730469810 (lesao-destino) | A lacuna "[mutants]" é trivial; o conceito que a professora enfatizou é a **tolerância às lesões**, ou reparo propenso a erro. | F: "When lesions overwhelm repair, the polymerase loses proofreading and inserts any base, a process called {{c1::lesion tolerance}} (error-prone repair) that generates mutants" |
| 1791730470484 (reparo-recombinacional) | A lacuna "[strand]" é trivial. | F: "In the dark, {{c1::recombinational}} repair uses the intact sister copy present after replication to fix a damaged strand" |
| 1791730472285 (transposicao, AnKing) | c1 "Transposition" fica com "transposon" visível, e vice-versa; os dois clozes se entregam. | Fundir em um cloze (c1 = transposon), ou suspender: o 1791730473335 e o transposase já cobrem o item. |
| 1791730475984 (hfr-genoma, AnKing) | c1 "[conjugation]" é óbvio a partir de "high frequency strains". | Recloze em "{{c1::chromosomal}}" (manter c2). |
| 1791730476207 (hfr-mapa, AnKing) | Mesma coisa: "[Conjugation] of high-frequency strains". | Recloze em "{{c1::genetic mapping}}". |
| 1791730473559 (transposon-estabilidade) | A oração causal ("because it is no longer lost with the plasmid") entrega "stable". | Mover a causa para o Extra. |
| 1791730475984 | Extra "Hfr * F- conjugation". | "Hfr × F⁻ conjugation" |
| 1791730470734 (mutantes-aplicacao) | "can be used to **select** mutants": a radiação induz, não seleciona. | "…used to **obtain** mutants with higher production of {{c1::antibiotics}}" |

## 3. Lacunas (itens das lâminas ou da transcrição sem card)

1. **Fita atrasada e fragmentos de Okazaki** (lâmina 22): nenhum card cobra a síntese contínua da líder e descontínua da atrasada; o ligase só pressupõe isso. Card: "The {{c1::lagging}} strand is synthesized discontinuously as {{c2::Okazaki fragments}}" (azul; procurar um AnKing equivalente primeiro).
2. **Intercalantes causam frameshift** (desenho da acridina, lâmina 27): resolver junto com E2, pela frente ou por um card próprio.
3. **Comparação dos três mecanismos de transferência** (lâmina 28: fago, plasmídeo por contato, DNA livre): falta o card da diferença decisiva. Sugestão: "Transfer of naked DNA that is blocked by DNase = {{c1::transformation}}; phage-mediated = {{c2::transduction}}; requires cell contact = {{c3::conjugation}}" (verde).
4. **Destino do receptor**: F⁺ × F⁻ converte o receptor em F⁺; no cruzamento Hfr × F⁻ o receptor **permanece F⁻**, porque o F vai por último (lâmina 34 e Trabulsi). Card azul.
5. **Epissomo** (transcrição: "epissomal quer dizer que ele se insere no genoma"), e plasmídeos conjugativos serem grandes e de baixo número de cópias: o termo não tem card.
6. **Óperon lac** (lâmina 41): os compartilhados cobrem lacZ/lacY/lacI/operador; faltam o **indutor alolactose** (IPTG) e o **controle glicose → cAMP–CAP**. Compartilhar os cards do BM29, se existirem, em vez de criar novos.
7. **Defesas antifago** (lâmina 43: bloqueio de adsorção/injeção/replicação, **restrição-modificação**, suicídio celular, CRISPR): nada sobre RM, que é a função natural das enzimas de restrição da lâmina 38. Card: "Bacteria use restriction–modification systems to cut unmethylated {{c1::phage}} DNA while methylating their own".
8. Lâmina 24: **fenótipos de mutantes** (resistência a drogas, sensibilidade à temperatura, morfológicos). Baixa prioridade, rosa.
9. Transcrição: a transposição costuma ser **replicativa** ("manda uma cópia… duplica os determinantes"). Baixa prioridade.
10. Itens só mencionados no Extra, o que não conta como cobertura: sítios Ter (lâmina 20), limite de captação na transformação, genoma de E. coli de 4,6 Mb. Os três são de baixo rendimento; decidir se viram rosa.

## 4. Cards sem item no material de base, ou fora da aula

- **1791730473932 (integron)**: integrons não aparecem nas lâminas, na transcrição nem no Trabulsi cap. 5; a única fonte é a apostila NEBLI (derivada, não é material de base). Pela regra F-20261009-CLAUDE-02, sai ou vai para o Extra do 1791730473335.
- **1791730470611 (xeroderma, AnKing)**: a aula não fala de XP. Já está no Extra do 1791730468934; rebaixar para rosa ou suspender.
- **Pendências de Davi** (comentários "fugiu do conteúdo da aula / isso é aula de biomol / várias assim"): 5 notas já estão suspensas. Seguem ativas no mesmo bloco de estrutura do DNA: **1791730464008 (antiparalelo)**, **1791730464785 (G-C/Tm, AnKing; Tm não está na aula)**, **1791730464910 (desnaturação)** e **1791730465036 (renaturação, Extra sobre PCR)**. Pelo "várias assim", suspender também. O comentário do 1791730464182 está no campo `NEBLI_Resposta`, não em `NEBLI_Comentario`; conferir o campo.
- **1791730463385 (nucleoide)**: comentário pendente de Davi. Tirar "through DNA interaction with the proteins HU and H-NS" da frente. Nova frente: "The bacterial chromosome is packed into a compact {{c1::nucleoid}}, which has no membrane around it"; HU/H-NS, se ficar, vai para o Extra.
- 1791730468686 e 1791730468809 (transição/transversão): a professora deu os termos, mas disse "na prática não acho importantes". Podem ficar; considerar rosa.

## 5. Duplicatas internas

- **1791730474735 (fago-engano) × 1791730474486 (generalized, AnKing)**: os dois cobram o empacotamento por engano de DNA bacteriano na transdução generalizada. Manter o AnKing e incorporar o "lytic phage, by mistake" no Extra dele, ou reclozar o autoral em "{{c1::lytic}} phage".
- **1791730474985 (lysogeny → toxins) × 1791730475110 (lysogenic conversion)**: mesmo fato. Ficar com o 1791730475110 e suspender o 1791730474985, ou reclozar este último para cobrar a doença ou o exemplo.
- **1791730468934 (UV → pyrimidine dimers, AnKing) × compartilhado 1791666344741 (UV → thymine dimers, MB30)**: mesma resposta. Como o MB30 já cobre o fato, aqui só se justifica um dos dois.
- O Extra do 1791730478484 (Cas1–Cas2) repete o compartilhado de espaçadores 1791630174296 (repeats/spacers). É aceitável, mas o compartilhado está suspenso.

## Resumo

- **Erros científicos ou imprecisões de conteúdo: 16** (E1–E16). Os graves são E1–E6; E7–E14 são moderados ou menores; E15–E16 são redação errada no texto AnKing.
- **Ajustes de redação ou cloze: 10** (seção 2).
- **Lacunas: 7 relevantes** (itens 1–7 da seção 3) e 3 menores.
- **Fora do material ou pendência de Davi: 8 notas** (integron, XP, 4 de estrutura do DNA, nucleoide, e transição/transversão como opcional).
- **Duplicatas: 3 pares** e 1 sobreposição de Extra.

### Correções a aplicar, por prioridade

1. E1, transposon/transposase (definição errada e Extra que contradiz o card do recA).
2. E2, Extra do SDS e intercalante → frameshift (fecha também a lacuna 2).
3. E3, atribuição do tubo em U (Davis).
4. E4, evidência de Avery (DNase).
5. Pendências de Davi: frente do nucleoide; suspender antiparalelo, G-C/Tm, desnaturação e renaturação.
6. E5, ilha = transferência horizontal; E6, receptores do fago.
7. Integron para o Extra (sem item de base); XP para rosa ou suspenso.
8. Lacunas 1, 3 e 4: Okazaki/fita atrasada, comparação dos três mecanismos, destino do receptor F⁺/Hfr.
9. Duplicatas: fago-engano, lysogeny/conversão, UV dimers.
10. Clozes que entregam a resposta: hfr-def, plasmideo-perda, lesao-destino, reparo-recombinacional, hfr-genoma, hfr-mapa, transposicao.
11. E7–E14 (UV penetração, Mycoplasma, supertorção, SOS, fotoliase, missense, ligações do dímero, E. coli/CaCl₂).
12. Lacunas 5–7 (epissomo, alolactose/CAP compartilhados, restrição-modificação) e E15–E16.
