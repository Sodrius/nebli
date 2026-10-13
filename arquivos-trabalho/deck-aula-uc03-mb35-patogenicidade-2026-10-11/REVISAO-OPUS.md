# Patogenicidade bacteriana: revisão Opus (11/10/2026, só leitura)

Deck `NEBLI::UC03::P2::Microbiologia::Patogenicidade bacteriana`, corrida `uc03-mb35-20261011a`.

**O que foi lido:**
- deck ao vivo pelo AnkiConnect: 140 notas e 155 cards, incluindo os 8 compartilhados; cor tirada das *flags* de `cardsInfo`;
- `nebli.revisar` da corrida;
- `fontes/slides.txt` e as 7 folhas `visual/folha-NN.png` (41 lâminas);
- turma I (pp. 35–85), II e III; transcrições I e II, inteiras;
- monitoria P2: aula 6 (l. 1917–2045) e aula 8 (l. 2199–2330);
- `provas.txt`, `inventario.py` e `REVISAO-DE-QUALIDADE.md`;
- no Trabulsi, só trechos por busca (eEF-2, EAEC).

Nada foi escrito no Anki.

Legenda de cor: V = verde (flag 3), A = azul (4), P = rosa (5); uma letra por card da nota.

## 0. Achado estrutural (antes das tabelas)

**1. Âncoras de lâmina erradas no spec e no inventário.**
- A **lâmina 35 é a figura das etapas do biofilme** (planctônica → adesão → microcolônias → *quorum sensing* → comunidade madura). Não fala de toxinas.
- Mesmo assim, 14 notas de tétano, botulismo, *C. perfringens*, *C. difficile* e difteria estão marcadas como "Slide 35".
- TB, *H. pylori* e proteínas A e M estão marcadas como "Slide 32", que só mostra cápsula.
- Todas vêm do material da turma de 2025 (Patogenicidade I, pp. 35–58 e 67–84; III, pp. 28–30) e devem citar essa fonte.

**2. Ordem no Browser.**
- Pela `ordem` (mb35-108 a 121), os clostrídios e a difteria entram **entre biofilme e *quorum sensing***, o que quebra a história da aula.
- O lugar deles é com os exemplos de exotoxinas (depois da lâmina 25).

**3. Peso dos exemplos de 2025.**
- São 19 notas e cerca de 24 cards (perto de 15% do deck) para conteúdo que **não aparece nas lâminas de 2026**.
- A lâmina 25 só dá a eritrogênica, a colérica e a enterotoxina estafilocócica.
- Detalhe em 2.1.

**4. Mapeamentos frouxos no inventário.** A regra diz que menção no verso não conta. Estes itens apontam para cards que não os perguntam:

| Lâmina | Item | Card apontado | Problema |
|---|---|---|---|
| 4 | funções dos linfócitos | `transferrina` | não tem relação |
| 8 | relação parasito-hospedeiro (anticorpo, Th, CTL) | `nutrientes-patogeno` | não tem relação |
| 10 | hipersensibilidade como lesão | `febre-reumatica` | o card pergunta a proteína M, não o mecanismo |
| 18 | EspA | `t3ss` | EspA não é perguntada |
| 21 | FHA | `adesinas-tipos` | FHA só no Extra |
| 21 | autotransportadoras | — | nenhum card |
| 35 | etapas do biofilme | `biofilme-def` | o card não pergunta etapas |
| — | tropismo (turma) | sideróforo compartilhado | o card não pergunta tropismo |
| — | difteria | `difteria-toxina` | o card pergunta eEF-2, não o fago da turma |

## 1. Lacunas (itens do material sem card que os pergunte)

| # | Item | Fonte | Cobertura atual | Proposta (seção 6) |
|---|---|---|---|---|
| L1 | Etapas do biofilme: adesão → microcolônias → *quorum sensing* → maduro (sequência) | lâm. 35 (figura) | nenhuma | N1, N2 |
| L2 | Hipersensibilidade como 3º mecanismo de lesão (ao lado de lesão direta e toxinas) | lâm. 10 | nenhuma | N3 |
| L3 | Resposta a extracelular (anticorpo, complemento) × intracelular (Th1/IFN-γ, CTL); TB exige imunidade celular | lâm. 8; transcr. II p.48 | nenhuma | N4 |
| L4 | A seringa do T3SS é de EspA | lâm. 18 | só no Extra de `t3ss` | N5 |
| L5 | Pili tipo IV (BFP da EPEC) e parentesco com o T2SS | lâm. 16, 18, 22 | nenhuma | N6 |
| L6 | *Shigella*: depois de matar o macrófago, invade o enterócito pela face **basolateral**; IcsA polimeriza actina | lâm. 20 | só a actina (`shigella-actina`) | N7, N8 |
| L7 | FHA da *B. pertussis*; autotransportadoras (domínio próprio de poro, lâm. 23) | lâm. 21, 23 | FHA só no Extra | N9, N10 |
| L8 | LPS causa ativação policlonal de linfócitos B | lâm. 29 (figura) | nenhuma | N11 |
| L9 | Receptores de membrana externa para sideróforo, transferrina/lactoferrina e heme | lâm. 33 (figura) | só o Extra do compartilhado | N12 |
| L10 | Mecanismos de QS: LuxI/LuxR (AHL); sistema de dois componentes (peptídeos); QseC/LEE (AI-3) | lâm. 36–38 | só os nomes dos sistemas | N13–N15 |
| L11 | Difteria: toxina **codificada por fago** (conversão lisogênica); sem fago, não há doença | turma I p.58; transcr. II p.28 | nenhuma (o card cobra eEF-2, que só está no Trabulsi) | N16 |
| L12 | Tríade capsulada da meningite: *N. meningitidis*, *S. pneumoniae*, *H. influenzae* | turma I p.70; transcr. I p.56 | nenhuma | N17 |
| L13 | Sorotipagem O/H/K da *E. coli* (K = cápsula; K1 na meningite neonatal) | prova 2017 P2 1.2; turma III p.29; transcr. II p.38 | nenhuma | N18 |
| L14 | Ilha de patogenicidade reconhecida por conteúdo GC diferente; vem de fagos e plasmídeos | transcr. II p.44 | `salmonella-spi1` não pergunta o conceito | N19 |
| L15 | Bacteremia transitória (eliminada) × septicemia (multiplicação no sangue) | transcr. II p.8; turma I p.61 | só no Extra de `etapas-infeccao` | N20 |
| L16 | Proteases de IgG (*S. aureus*, *S. pyogenes*) | turma I p.72; transcr. I p.60 | nenhuma | N21 |
| L17 | *N. meningitidis* liga o fator H e inibe o complemento | prova 2018 P2 2.2 | nenhuma | N22 |
| L18 | Exotoxinas pirogênicas estreptocócicas (SpeA/SpeC) como superantígenos | prova 2025 P2 2.3 | `superantigeno` é genérico | N23 |
| L19 | Toxina alfa do *S. aureus*: forma poros | prova 2024 P2 1.11 | nenhuma | N24 |
| L20 | Tropismo por enzimas (*C. acnes*: lipases; *Proteus*: ambiente com amônia) | turma III p.4; transcr. II p.6 | nenhuma (mapeado ao sideróforo) | N25 |
| L21 | TB latente: infectado, assintomático, não transmite | turma I p.82 | nenhuma (há Pott, mais lateral) | N26 |
| L22 | Tétano instalado: trata-se com antitoxina, porque a vacina não dá tempo | transcr. II p.22 | nenhuma | N27 |
| L23 | Disenteria pede antibiótico; diarreia por toxina, reidratação | transcr. II p.38 | nenhuma | N28 |
| L24 | Monitoria aula 6: defesas do TGI (pH, bile) e resistência ácida bacteriana; tipos de motilidade (flagelo, endoflagelo, deslizamento); mutualismo/comensalismo/parasitismo | monitoria l.1952–1990 | nenhuma | rosa opcional (N29) ou EXC |
| L25 | Tabela de defesas (PMN, MBL, complemento, IgG/IgM) e funções dos linfócitos | lâm. 3–4 | mapeada a `transferrina` | **EXC** justificado: é do deck de Imunologia. Corrigir o inventário, sem card. |
| L26 | Proteína A liga o Fab do BCR e mata linfócitos B | turma I p.71 | nenhuma | rosa opcional |
| L27 | β-lactamase como enzima de virulência | turma I p.62 | nenhuma | EXC: aula de resistência |

## 2. Fugas e peso desproporcional

### 2.1 Exemplos da turma de 2025

Todos têm item no material de base, então não são fuga estrita. O excesso está no **peso**:
- só o tétano tem 5 notas e 6 cards, contra **zero lâminas de 2026**;
- vários cards são AnKing com profundidade que nem a turma deu (SNARE, células de Renshaw, despolimerização de actina pela toxina B, eEF-2).

Proposta: um card por ideia que a turma ensinou e cor rosa, exceto o contraste espástica × flácida, que a monitoria repete.

| nid | chave | cor | Veredito | Ação |
|---|---|---|---|---|
| 1791746132701 | tetano-toxina | V | Só recupera o nome "tetanospasmin"; a turma não dá o nome | suspender |
| 1791746132826 | tetano-espastica | V | Contraste espástico × flácido (turma, monitoria) | manter, **V→A** |
| 1791746133349 | tetano-snare | AA | Mecanismo; a turma diz "bloqueia neurotransmissores inibitórios" | manter um card só: cloze em GABA/glicina, SNARE no Extra; **P** |
| 1791746134262 | tetano-glicina | A | Duplica `tetano-snare` | suspender |
| 1791746134964 | tetano-formas | P | Clínica (neonatal, localizado, generalizado) | suspender ou manter P; trocar por N27 (antitoxina), que é mais útil |
| 1791746135561 | botulinica | V | Ideia central do par | **V→A** |
| 1791746136268 | botox | P | Turma I p.49; detalhe lateral | manter P ou suspender (decisão de Davi) |
| 1791746136808 | difteria-toxina | A | eEF-2 só no Trabulsi; a turma ensina fago e pseudomembrana | **A→P**, mais N16 (fago, A) |
| 1791746137382 | perfringens-alfa | **VVV** | Três cards verdes para um detalhe só da turma; duplica `perfringens-lecitinase` | suspender (ou, no máximo, 1 card P) |
| 1791746138075 | perfringens-lecitinase | AA | Liga com "lecitinase" da lâm. 30 | manter 1 card, **P** |
| 1791746138675 | gangrena-gasosa | P | Tratamento (câmara hiperbárica) | suspender |
| 1791746139201 | cdiff-toxinas | V | Toxinas A/B não aparecem na turma (só "citotoxina") | **V→P** |
| 1791746139742 | cdiff-toxinab | A | Despolimerização de actina: fora do material | suspender ou **P** |
| 1791746140352 | cdiff-colite | A | Antibiótico seleciona *C. difficile*: liga com microbiota e infecção endógena | manter A |
| 1791746131503 | tb-fagossomo | V | Bom exemplo de evasão intracelular (turma, monitoria) | **V→A** |
| 1791746131627 | tb-manlam | P | Turma I p.77 | manter P |
| 1791746131779 | tb-tratamento | P | Farmacologia (RIPE); fora do eixo patogenicidade | **suspender** |
| 1791746131901 | tb-formas | P | Mal de Pott não contagioso: lateral | suspender; trocar por N26 (TB latente, que se liga ao iceberg) |
| 1791746132075 | hpylori-vaca | A | Só na turma | **A→P** |

Resultado: 6 suspensões firmes (mais 3 opcionais: tetano-formas, cdiff-toxinab e botox), 8 recolorações e 4 cards novos que trocam detalhe por ideia (N16, N26, N27, N4).

### 2.2 Outros pontos de peso

| nid | chave | cor | Problema | Ação |
|---|---|---|---|---|
| 1791746126851 | ehec-vero | A | AnKing profundo (60S, esquistócitos) além da turma; é a 3ª nota de EHEC | **A→P** |
| 1791746131326 | gnpe-proteina-m | PP | SpeB além do material (a transcrição atribui a GNPE a anticorpos anti-M); 2 cards | manter só o c1 (proteína M) em P, ou suspender o c2 |
| 1791746129003 | coagulase | AA | O c1 ("único estafilococo coagulase-positivo") é identificação da aula de estafilococos | suspender o c1 e manter o c2 |
| 1791746118751 | eaec-daec | P | Só no resumo da turma I | manter P |
| 1791746126478 | etec-viajante | A | "Montezuma's revenge" no Extra é trivia | cortar o bullet |

## 3. Cores

Recolorações dos exemplos de 2025: ver 2.1.

| nid | chave | atual | proposta | Motivo |
|---|---|---|---|---|
| 1791746114724 | infeccao-def | A | **V** | Definição-eixo da lâm. 2 |
| 1791746116828 | portas-entrada | A | **V** | Lâm. 9 e 10; central e durável |
| 1791746116327 | fases-infeccao | A | **V** | Lâm. 7 inteira |
| 1791746116953 | etapas-infeccao | A | **V** | Esqueleto da aula (adesão → colonização → disseminação) |
| 1791746127752 | peptidoglicano-endotoxina | P | **A** | Repetido nas lâm. 26 e 29; não é detalhe |
| 1791746130249 | camuflagem | P | **A** | Item próprio da lâm. 31 |
| 1791746129176 | leucocidina | P | **A** | Cobrado (prova 2024 P2 1.11: PVL lisa PMN) |
| 1791746123621 | opa | A | **P** | A professora diz na transcrição I (p.40): "precisa lembrar o nome? Não" |
| 1791746119824 | salmonella-spi1 | A | **P** | SPI-1 vem só do livro |
| 1791746130953 | proteina-a-mecanismo | V | **A** | Cobrado (prova 2024); evasão específica do *S. aureus* |

## 4. Erros científicos (correção em inglês)

| # | nid | chave | Onde | Erro | Correção |
|---|---|---|---|---|---|
| E1 | 1791746115653 | oportunista | Extra | "Primary pathogens such as *Mycobacterium tuberculosis* cause disease whenever they are found" contradiz o card `iceberg`, que traz a TB como exemplo de infecção subclínica, e a TB latente da turma | `- Primary pathogens such as Mycobacterium tuberculosis can cause disease in healthy hosts` |
| E2 | 1791746130953 | proteina-a-mecanismo | Extra | "Virulence factor (exotoxin) of Staph aureus": a proteína A é proteína de superfície ancorada na parede, não exotoxina | `- Protein A is a cell wall–anchored surface protein of Staphylococcus aureus` |
| E3 | 1791746129176 | leucocidina | Frente | PVL "a cytotoxic **protease**": a PVL é citotoxina bicomponente formadora de poro | `...express {{c1::Panton-Valentine leukocidin (PVL)}}, a pore-forming cytotoxin that kills leukocytes and causes tissue necrosis` |
| E4 | 1791746127876 | lps-estrutura | Frente | "a(n) Lipid A **core**": lipídeo A e cerne (*core*) são partes distintas, como o próprio Extra diz | `Lipopolysaccharide {{c1::endotoxins}} have a {{c2::lipid A}} anchor responsible for their toxicity, a conserved core polysaccharide and a(n) {{c2::O antigen}} that varies among strains` |
| E5 | 1791746129976 | salmonella-fase | Frente | "through a transposable insertion sequence": a variação de fase H1/H2 é **inversão sítio-específica** de um segmento com promotor (recombinase Hin), não transposição | `...switching between flagellin {{c1::H1 and H2}} by inverting a promoter-containing DNA segment` |
| E6 | 1791746125051 | endotoxina-membrana | Frente | "cell membranes": o LPS fica na membrana **externa** | `...a component of the gram {{c2::negative}} outer membrane` |
| E7 | 1791746132075 | hpylori-vaca | Frente | "one way the bacterium evades host defenses" é enquadramento frouxo (a turma diz "gerando danos no epitélio gástrico") | `...induces {{c1::vacuoles}} in gastric epithelial cells, damaging the gastric epithelium` |

Erros do **material** que o deck não reproduziu (bom; avisar Davi para a prova discursiva):
- turma I p.42–46, transcrição II p.20 e monitoria l.2289 dizem que a toxina tetânica causa "excesso/liberação excessiva de acetilcolina". O certo é o bloqueio da liberação de glicina/GABA dos interneurônios inibitórios, como o deck faz.
- transcrição I p.44: *S. mutans* "não causa cárie" e *A. actinomycetemcomitans* seria o cariogênico. Está invertido: o *A. a.* é periodontal. O card `mutans-placa` está certo.
- monitoria l.2309 e transcrição II p.48: *M. leprae*/*M. tuberculosis* "se multiplicam em PMN". O nicho é o macrófago.
- gabarito da prova 2018: "fator H que cliva proteínas do complemento". O fator H é do hospedeiro; a *N. meningitidis* o **recruta** (N22).

## 5. Redundâncias

| # | Cards (nid · chave) | Sobreposição | Ação |
|---|---|---|---|
| R1 | 1791746119584 t3ss-salmonella (A) · 1791746119702 t3ss-shigella (V) · 1791746119824 salmonella-spi1 | Mesmo cloze "type III" duas vezes | suspender `t3ss-salmonella` |
| R2 | 1791746130779 proteina-a (AA) · 1791746130953 proteina-a-mecanismo (V) | Três cards para "proteína A do *S. aureus*" | suspender `proteina-a` (os dois) e manter o mecanismo corrigido (E2) |
| R3 | 1791746125228 endotoxina-morte (A) · 1791746125051 endotoxina-membrana (VV) | "Liberada na lise" já é o Extra da outra | suspender `endotoxina-morte` |
| R4 | 1791746125377 endotoxina-lps (A) · 1791746127876 lps-estrutura c1 · lipídeo A compartilhado 1791163032499 | "Endotoxin = LPS" perguntado 2 vezes | suspender o c1 de `lps-estrutura` |
| R5 | Grupo do tétano (4 notas) | ver 2.1 | ver 2.1 |
| R6 | 1791746137382 perfringens-alfa · 1791746138075 perfringens-lecitinase | Mesma toxina/enzima | ver 2.1 |
| R7 | 1791746142672 celulas-m · 1791746121022 shigella-celulaM | Ambos respondem "M cells" | reescrever `shigella-celulaM` para perguntar o passo seguinte (N7) ou suspender `celulas-m` |
| R8 | 1791746126300 etec-lt c2 · 1791746126602 etec-toxinas · Extra de etec-viajante | LT/ST perguntados 2 vezes | aceitável; opcional suspender o c2 de `etec-lt` |
| R9 | 1791746114975 transferrina · imunidade nutricional compartilhada 1791647814120 | Mesma ideia (ferro sequestrado) | aceitável (ângulos diferentes) |

## 6. Cards novos propostos (inglês AnKing)

| # | Lâmina/fonte | Cor | Text | Extra |
|---|---|---|---|---|
| N1 | lâm. 35 | V | In <b>biofilm</b> development, planktonic bacteria attach to a surface and divide into {{c1::microcolonies}} | - The surface can be biotic or abiotic |
| N2 | lâm. 35 | A | {{c1::Quorum sensing}} drives the transition from microcolonies to a mature <b>biofilm</b> community | - Mature biofilms form mushroom-shaped towers with water channels |
| N3 | lâm. 10 | A | Bacteria injure host cells directly, through toxins or through {{c1::hypersensitivity}} reactions | - Rheumatic fever after Streptococcus pyogenes is an immune-mediated example |
| N4 | lâm. 8; transcr. II | A | Because <b>Mycobacterium tuberculosis</b> lives inside macrophages, its control depends on {{c1::cell-mediated}} immunity rather than antibodies | - IFN-γ from CD4+ T cells activates macrophages; CD8+ T cells kill infected cells |
| N5 | lâm. 18 | P | In the <b>EPEC</b> type III secretion system, the syringe filament is made of the protein {{c1::EspA}} | - EspA is secreted by the system itself |
| N6 | lâm. 16, 22 | P | The <b>bundle-forming pilus</b> (BFP) of EPEC is a type {{c1::IV}} pilus | - Type IV pili are assembled by machinery related to the type II secretion system |
| N7 | lâm. 20 | A | After escaping the macrophage, <b>Shigella</b> invades enterocytes from their {{c1::basolateral}} side | - It reaches the submucosa through M cells |
| N8 | lâm. 20 | P | The <b>Shigella</b> surface protein {{c1::IcsA}} polymerizes host actin for intracellular motility | - Actin tails push the bacterium into the neighboring cell |
| N9 | lâm. 21 | A | <b>Filamentous hemagglutinin</b> (FHA) is a non-fimbrial adhesin of {{c1::Bordetella pertussis}} | - Other non-fimbrial adhesins include outer membrane proteins and LPS |
| N10 | lâm. 21, 23 | P | <b>Autotransporter</b> proteins cross the outer membrane through a {{c1::pore domain}} of their own | - They are the simplest secretion system |
| N11 | lâm. 29 | P | Besides cytokine release, <b>LPS</b> causes {{c1::polyclonal}} B-cell activation | - LPS also activates complement and coagulation |
| N12 | lâm. 33 | P | <b>Gram-negative</b> bacteria take up iron from siderophores, transferrin and heme through specific {{c1::outer membrane}} receptors | - Uptake into the cytoplasm uses ATP |
| N13 | lâm. 36 | P | In <b>Gram-negative quorum sensing</b>, AHL made by a LuxI-type synthase binds a {{c1::LuxR}}-type receptor that activates target genes | - AHL diffuses freely across membranes |
| N14 | lâm. 37 | P | In <b>Gram-positive quorum sensing</b>, the secreted peptide is detected by a {{c1::two-component}} system | - A sensor kinase phosphorylates a response regulator |
| N15 | lâm. 38 | P | In <b>EHEC</b>, AI-3 and host epinephrine are sensed by {{c1::QseC}}, which activates the LEE genes of attaching and effacing lesions | - This is bacteria–host communication |
| N16 | turma I p.58; transcr. II | A | <b>Corynebacterium diphtheriae</b> makes diphtheria toxin only when lysogenized by a {{c1::bacteriophage}} carrying the toxin gene | - This is lysogenic conversion |
| N17 | turma I p.70; transcr. I | A | The encapsulated bacteria that most often cause <b>meningitis</b> are Neisseria meningitidis, Streptococcus pneumoniae and {{c1::Haemophilus influenzae}} | - The capsule lets them evade phagocytosis |
| N18 | prova 2017; turma III p.29 | A | In <b>E. coli</b> serotyping, O is the LPS antigen, H the flagellar antigen and K the {{c1::capsular}} antigen | - K1 strains cause neonatal meningitis |
| N19 | transcr. II p.44 | P | <b>Pathogenicity islands</b> are recognized by a {{c1::GC content}} different from the rest of the genome | - They were acquired from phages or plasmids |
| N20 | transcr. II p.8; turma I p.61 | A | Transient <b>bacteremia</b> is cleared by phagocytes, whereas in {{c1::septicemia}} bacteria multiply in the blood | - Tooth brushing causes a transient bacteremia |
| N21 | turma I p.72 | P | <b>Staphylococcus aureus</b> and Streptococcus pyogenes evade opsonization with {{c1::IgG}} proteases | - Neisseria, H. influenzae and S. pneumoniae make IgA proteases |
| N22 | prova 2018 | A | <b>Neisseria meningitidis</b> recruits the host complement regulator factor {{c1::H}} to its surface, blocking complement attack | - Its capsule and LPS are the other major virulence factors |
| N23 | prova 2025 | A | <b>Streptococcal pyrogenic exotoxins</b> such as SpeA and SpeC act as {{c1::superantigens}}, causing streptococcal toxic shock | - Streptolysins and hyaluronidase add tissue destruction |
| N24 | prova 2024 | A | <b>Staphylococcus aureus</b> alpha-toxin is a {{c1::pore-forming}} toxin that lyses alveolar epithelial cells and leukocytes | - PVL also kills neutrophils in necrotizing pneumonia |
| N25 | turma III p.4; transcr. II | P | <b>Cutibacterium acnes</b> has tropism for sebaceous skin because it is rich in {{c1::lipases}} | - Tropism reflects the enzymes a bacterium carries |
| N26 | turma I p.82 | P | In <b>latent tuberculosis</b> infection, the host has no symptoms and does {{c1::not}} transmit the bacillus | - Immunosuppression can reactivate it as active disease |
| N27 | transcr. II p.22 | P | Established <b>tetanus</b> is treated with {{c1::antitoxin}}, because vaccination acts too slowly | - Vaccination is the prevention |
| N28 | transcr. II p.38 | P | Invasive bacillary <b>dysentery</b> requires antibiotics, whereas toxin-mediated watery diarrhea is treated mainly with {{c1::rehydration}} | - Dysentery has blood, mucus and tissue destruction |
| N29 (opcional) | monitoria l.1983 | P | Enteric bacteria survive <b>gastric acid</b> by maintaining their intracellular {{c1::pH}} with proton pumps and amino acid decarboxylase systems | - Gram-negative bacteria are also more resistant to bile |

Lâminas 2 (inflamação) e 39 (figura de revisão): manter EXC. Lâminas 3–4: transformar em EXC justificado (L25).

## Contagens

| Seção | Total |
|---|---|
| Lacunas | 27 (L1–L27): 23 com card proposto, 3 EXC, 1 opcional |
| Fugas/peso | 19 notas de exemplos de 2025 avaliadas: 6 suspensões firmes e 3 opcionais, 8 recolorações; mais 5 pontos de peso fora desse grupo |
| Cores | 10 recolorações fora dos exemplos de 2025 (mais 8 dentro de 2.1) |
| Erros científicos | 7 no deck, mais 4 erros do material que o deck evitou |
| Redundâncias | 9 grupos (5 com suspensão proposta) |
| Cards novos | 29 (28 mais 1 opcional): 1 V, 12 A, 16 P |
