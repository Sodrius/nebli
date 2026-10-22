# Especificação curada — 58 Multiplicação viral e antivirais (UC03 P3, Microbiologia; Prof. Enrique Boccardo; 242 lâminas = Multiplicação
# viral Ia (1–92) + Antivirais (93–178) + Replicação viral II (179–242, repetição condensada da parte I)). Pipeline v5 (22/10): o deck nasce de
# compreensao-aula.json; princípio antes do exemplo; famílias e fármacos só como exemplo de cada princípio; farmacologia (efeitos adversos,
# esquemas, covid) é da UC19 e ficou fora (F-20261021-CLAUDE-01).
# História: o vírus entra (receptor, penetração, desnudamento) → a célula faz proteínas precoces e tardias → a estratégia de copiar o genoma
# depende dele (DNA pequeno usa a célula, grande traz a sua; iniciador de RNA, proteína ou DNA; RNA precisa de RdRp própria e erra) →
# montagem e saída → antiviral é bloquear uma dessas etapas onde o vírus usa enzima própria.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 6
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb58-20261022b"
SHORT = "mb58w"
LESSON = "2026-uc03-microbiologia-58-multiplicacao-viral-antivirais"
DECK = "NEBLI::UC03::P3::Microbiologia::Multiplicação viral e antivirais"
CRITERIOS = "MEMORY.md + pipeline v5 (EXECUCAO-DECK-AULA) + FEEDBACKS até F-20261022-CLAUDE-07 + EXEMPLARES/ANTI-EXEMPLARES de 22/10"
MEDIA = {f"mb58-{n}": f"img/mb58-{n}" for n in ("ciclo.jpg", "mecanismos.png", "rolling.png", "adeno.jpg", "brotamento.png", "t-antigen.png")}
IMG = lambda n, w=460: f'<img src="mb58-{n}" width="{w}">'
BUSCA = ("Três caminhos (22/10): seções de recurso do AnKing (genomas e replicação viral, mecanismos de infectividade; busca/secoes); palavra-chave em "
         "AnKing e Referências Externas (busca/anking.txt); significado em AnKing, nos 9 acervos externos e no NEBLI vivo, uma consulta por conceito "
         "da compreensão da aula (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


_FAM = "detalhe de família ou de genética viral sem objetivo na aula"
EXCLUIDOS = [
 (1502064476771, "orientação 5'→3' do RNA: detalhe de biologia molecular que a aula não dá"),
 (1502064737111, "orientação 3'→5' do RNA: detalhe de biologia molecular que a aula não dá"),
 (1502064208990, "repete o RNA positivo como mRNA, já com card na 57"),
 (1502570163043, _FAM), (1502570324908, _FAM), (1502570911606, _FAM), (1502570964320, _FAM),
 (1502571002064, "varíola: doença, fora do recorte"), (1502571454317, "molusco contagioso: doença, aula 61"),
 (1502570605009, "corpúsculos de Guarnieri: inclusão por doença, aula 61"), (1502571972870, "corpúsculos do molusco: aula 61"),
 (1516475620459, "Negri: inclusão por doença, aula 61; aqui o organizador das inclusões"),
 (1516475827100, "Cowdry: inclusão por doença, aula 61; aqui o organizador das inclusões"),
 *[(n, "genoma e estrutura: card na 57 Princípios gerais dos vírus, que esta aula não repete") for n in
   (1502065388242, 1502063700798, 1502064066857, 1502064281478, 1502064367585, 1502064775742, 1502572273268)],
 (1502065688092, "vacinas recombinantes: imunologia"), (1502066053913, "vacina da hepatite B: imunologia"),
]
FORA_DO_RECORTE = [
 "Farmacologia dos antivirais (nomes por classe, efeitos adversos, contraindicações, esquemas de HAART, DAAs por geração): UC19; aqui só o mecanismo de cada classe ligado à etapa do ciclo.",
 "Fármacos de covid-19 e antivirais de amplo espectro (lâminas 145–148, 170–175): exemplos sem cobrança, retirados por Davi em 21/10.",
 "Desenvolvimento de fármacos (lâminas 164–169): contexto; o princípio (alvo seletivo e potente) está nos cards das lâminas 94–95.",
 "Efeito citopático (estudo dirigido nas pp. 94–124 da transcrição Ib): aula 60 Virologia prática.",
 "Oncogênese por E6/E7 em detalhe: aula 78 Carcinógenos biológicos; aqui E6/E7 entram como o modo de o HPV forçar a síntese de DNA.",
 "Ciclo dos fagos e genética viral (mistura fenotípica, complementação, recombinação): aula 34 e fora das lâminas; só o rearranjo entra (lâmina 83).",
 "Parte III (lâminas 179–242) repete a parte I; os cards apontam para a parte I.",
]
A_, B_, C_, D_, E_, F_, G_, H_ = ("A-ciclo", "B-entrada", "C-sintese", "D-virus-dna", "E-virus-rna", "F-montagem-liberacao", "G-antivirais", "H-alvos")

CARDS = [
 # ---------- Infecção e etapas (lâminas 5–8) ----------
 au("au-produtiva", "A viral infection that yields new infectious virions is {{c1::productive}}, and one that yields none is {{c1::abortive}}",
    "A-aula", A_, "Infecção produtiva × abortiva", 6, "lâmina 6; apostila guia de Micro e monitoria P3",
    extra="- Abortive: nonpermissive cell or defective virus<br>- Latent: genome persists without progeny"),
 au("au-condicoes", ORG("<b>Productive infection requires</b>:<br>- {{c1::susceptibility}}: a receptor<br>- {{c2::permissiveness}}: factors to finish the cycle<br>- access to the cell<br>- immune permissiveness"),
    "A-aula", A_, "Suscetibilidade, permissividade, acesso, imunidade", 6, "apostila guia de Micro e monitoria P3 (condições da infecção produtiva)",
    extra="- A susceptible cell can still be nonpermissive, giving an abortive infection"),
 au("au-etapas", ORG("<b>Steps of the viral cycle</b>, in order:<br>- {{c1::adsorption}}<br>- {{c1::penetration}}<br>- {{c2::uncoating}}<br>"
                     "- synthesis of proteins and genome<br>- {{c3::assembly}} and maturation<br>- {{c3::release}}"),
    "V-pilar", A_, "As etapas do ciclo viral", 8, "lâminas 7–8 e 96; prova 2025 P3 2.1",
    extra="- Every antiviral targets one of these steps<br>" + IMG("ciclo.jpg")),
 au("au-eclipse", "After uncoating, no infectious virus can be recovered from the cell until progeny appear, the {{c1::eclipse}} period",
    "R-detalhe", A_, "Período de eclipse", 8, "Jawetz cap. 29 (o vírion perde a infecciosidade no desnudamento); lâmina 17",
    extra="- It is the busiest phase: the cell is redirected to make viral parts<br>- Viruses are the only agents that must fall apart to replicate"),
 # ---------- Adsorção (lâminas 9–10) ----------
 au("au-receptor", "<b>Adsorption</b> binds a receptor that only some cells express, so the receptor largely determines viral {{c1::tropism}}",
    "V-pilar", B_, "Receptor específico define o tropismo", 9, "lâmina 9; Jawetz cap. 29 (receptor determina tropismo)",
    extra="- Receptors are ordinary host molecules (CD4, ICAM-1, CD21, sialic acid)<br>- No receptor, no infection, even if the cell is permissive"),
 sh(1792166995490, "azul", B_, "gp120 liga CD4 e correceptores", 10, "A-aula: lâmina 10; card da 51"),
 au("au-gp41", "After HIV <b>gp120</b> binds CD4 and the coreceptor, it changes shape and exposes {{c1::gp41}}, which inserts into the membrane",
    "A-aula", B_, "gp120 muda de forma e expõe a gp41", 10, "lâminas 10 e 15; apostila guia de Micro e apostila UC3 (domínio hidrofóbico da gp41)",
    extra="- gp41 folds back and pulls the two membranes together, causing fusion<br>- Enfuvirtide blocks exactly this step"),
 K(1516323222471, "V-hy", B_, "Hemaglutinina liga ácido siálico", 10, "lâminas 7, 14 e 98 (influenza, vírus-modelo da aula)"),
 # ---------- Penetração (lâminas 11–16) ----------
 au("au-penetracao", ORG("<b>Viral penetration</b> routes:<br>- receptor-mediated {{c1::endocytosis}}<br>- {{c1::translocation}} across the membrane<br>"
                         "- {{c2::fusion}} of the envelope with the plasma membrane"),
    "A-aula", B_, "Três vias de penetração", 11, "lâminas 11–16; apostila guia de Micro",
    extra="- Only enveloped viruses can fuse (herpes, paramyxovirus, HIV)<br>- Endocytosis uses clathrin- or caveolin-coated pits"),
 au("au-endossomo-ph", "In endocytic entry, the endosome's low {{c1::pH}} changes the shape of viral proteins, triggering fusion or capsid release",
    "A-aula", B_, "O pH ácido do endossomo dispara a entrada", 13, "lâminas 13–14; apostila UC3 (mudança de pH altera as proteínas do envelope)",
    extra="- Influenza HA fuses only after acidification<br>- Escaping before the endosome fuses with the lysosome is essential"),
 K(1516323635408, "A-aula", B_, "HA faz o influenza entrar por endocitose", 14, "lâmina 14 (influenza A por endocitose)"),
 # ---------- Desnudamento (lâminas 17–19) ----------
 au("au-desnudamento", "<b>Uncoating</b> releases the genome directly in the cytoplasm, after {{c1::endosome acidification}}, or at the {{c2::nuclear pore}}",
    "V-pilar", B_, "Três locais de desnudamento", 17, "lâminas 17–19; apostila UC3 e monitoria P3",
    extra="- Which site depends on where the genome must work: DNA viruses need the nucleus"),
 au("au-adeno-poro", "Adenovirus binds <b>CAR</b> and integrins, escapes the endosome and rides {{c1::microtubules}} to the nuclear pore to deliver its DNA",
    "A-aula", B_, "Adenovírus é levado ao poro nuclear", 18, "lâmina 18; apostila guia de Micro (CAR, integrinas, dineína, NLS)",
    extra="- Dynein carries it; a nuclear localization signal (NLS) imports the DNA<br>- Free DNA in the cytoplasm would alert innate sensors"),
 K(1516324096049, "A-aula", B_, "M2 acidifica o vírion para o desnudamento", 19, "lâminas 7 e 104 (influenza, canal M2)"),
 # ---------- Síntese (lâmina 20) ----------
 au("au-precoce", "Early viral mRNAs make {{c1::nonstructural}} proteins that replicate the genome, and late mRNAs make {{c2::structural}} proteins",
    "V-pilar", C_, "Proteínas precoces × tardias", 20, "lâmina 20; monitoria P3",
    extra="- Genome copying comes first, so capsids are not made with nothing to package<br>- Many RNA viruses express all genes at once"),
 au("au-re", "Viral envelope <b>glycoproteins</b> are made on the {{c1::rough ER}} and processed in the Golgi, unlike proteins on free ribosomes",
    "A-aula", C_, "Glicoproteínas do envelope no RE rugoso", 20, "lâmina 20 (ribossomos ou retículo endoplasmático); Jawetz cap. 29",
    extra="- Their sugars come from the host Golgi, so they reflect the host cell"),
 K(1506806776715, "A-aula", C_, "gp160 do HIV é processada no RE", 20, "lâmina 20 (síntese no retículo endoplasmático)"),
 K(1502152021975, "A-aula", C_, "Vírus de DNA replicam no núcleo", 20, "lâmina 20; seção FirstAid"),
 au("au-por-que-nucleo", "Most DNA viruses replicate in the nucleus because the host {{c1::RNA polymerase}} and DNA replication machinery are there",
    "V-pilar", C_, "Por que o DNA viral vai ao núcleo", 20, "lâmina 55 (a RNA polimerase do hospedeiro está no núcleo); apostila UC3",
    extra="- A DNA virus that stays in the cytoplasm must bring its own RNA polymerase (poxvirus)"),
 K(1516321076508, "A-aula", C_, "Vírus de RNA replicam no citoplasma", 20, "lâmina 20; seção Bootcamp"),
 # ---------- Estratégia (lâminas 21–25) ----------
 sh(1792677734751, "azul", C_, "Grupos de Baltimore: a estratégia depende do genoma", 22, "A-aula: lâmina 22; card da 57"),
 K(1467771853847, "A-aula", C_, "Polimerase precisa de iniciador e molde", 23, "lâminas 23–24"),
 # ---------- Vírus de DNA: princípios (lâminas 26–33) ----------
 au("au-proteina-viral", "Even the simplest DNA virus must make at least one viral protein, typically one that recognizes the replication {{c1::origin}}",
    "A-aula", D_, "Toda replicação de DNA viral exige proteína viral", 28, "lâminas 28 e 180; apostila UC3",
    extra="- Without it the cell would never start copying the viral genome"),
 au("au-pequeno-grande", ORG("<b>Who copies viral DNA</b>:<br>- small (papilloma, polyoma, parvo): the {{c1::host DNA polymerase}}<br>"
                             "- large (herpes, adeno, pox): a {{c2::virus-encoded}} DNA polymerase"),
    "V-pilar", D_, "Vírus de DNA pequeno × grande", 29, "lâminas 28–29 e 197; apostila UC3",
    extra="- Small ones encode proteins that manipulate the host cell instead<br>- Large ones are less dependent on the cell, so they offer more drug targets"),
 au("au-enzimas-nucleotideo", "Large DNA viruses also encode nucleotide-metabolism enzymes such as <b>thymidine kinase</b> and {{c1::ribonucleotide reductase}}",
    "A-aula", D_, "Enzimas virais do metabolismo de nucleotídeos", 30, "lâminas 30 e 198 (timidina quinase, ribonucleotídeo redutase, dUTPase)",
    extra="- They raise the nucleotide supply in nondividing cells<br>- Viral thymidine kinase is what activates acyclovir"),
 au("au-mecanismos", "Viral DNA copied by a {{c1::replication fork}} needs RNA primers, while {{c2::strand displacement}} uses a protein or <b>DNA hairpin</b>",
    "V-pilar", D_, "Forquilha × deslocamento de fita", 32, "lâminas 32 e 195",
    extra="- Fork: papilloma, polyoma, herpes, retroviral provirus<br>- Strand displacement: adeno (protein), parvo and pox (hairpin)<br>" + IMG("mecanismos.png")),
 au("au-5linha", "On a linear DNA, removing the last RNA primer leaves a gap that would {{c1::shorten}} the genome at each round",
    "V-pilar", D_, "O problema da extremidade 5'", 33, "lâminas 33 e 196; monitoria P3",
    extra="- The gap is at the 5' end of each new strand<br>- Human chromosomes solve it with telomerase; viruses cannot afford the loss"),
 au("au-solucoes-5", ORG("<b>Avoiding loss of the 5' end</b>:<br>- circular genome: {{c1::polyoma}}, papilloma<br>"
                         "- protein primer: {{c2::adenovirus}}<br>- rolling circle: {{c3::herpesvirus}}<br>- DNA hairpins: parvo, pox"),
    "V-pilar", D_, "As soluções para o problema 5'", 33, "lâminas 36–61 e 202–214 (sem problema 5' em cada família); resumo geral",
    extra="- Each family's replication strategy is, at heart, an answer to this problem"),
 # ---------- Poliomavírus e papilomavírus (lâminas 34–45) ----------
 au("au-polioma-genes", "Polyomavirus <b>early</b> genes encode the {{c1::T antigens}}, while late genes encode the capsid proteins VP1–VP3",
    "A-aula", D_, "Genes precoces e tardios do poliomavírus", 35, "lâminas 35 e 200",
    extra="- Early proteins prepare replication, late ones build the virion"),
 au("au-antigeno-t", "SV40 large T antigen binds the replication origin, unwinds it as a {{c1::helicase}} and recruits the host DNA polymerase",
    "A-aula", D_, "Antígeno T: helicase na origem", 36, "lâminas 36–39 e 201; apostila guia de Micro",
    extra="- The genome is circular, so there is no 5' problem<br>" + IMG("t-antigen.png", 300)),
 au("au-topoisomerase", "As T antigen keeps unwinding the circular genome, host {{c1::topoisomerases}} cut strands to relieve the supercoiling",
    "R-detalhe", D_, "Topoisomerases celulares no poliomavírus", 40, "lâminas 40 e 202; apostila guia de Micro",
    extra="- Topoisomerase II also separates the two interlinked daughter circles"),
 K(1502718274711, "A-aula", D_, "HPV infecta a camada basal", 43, "lâmina 43; apostila guia de Micro (chega por microlesões)"),
 au("au-hpv-e1e2", "In HPV, {{c1::E2}} binds sites flanking the origin and loads {{c2::E1}}, the helicase that recruits host DNA polymerase",
    "A-aula", D_, "E1 e E2 do HPV na origem", 42, "lâmina 42; monitoria P3",
    extra="- Viral and cellular proteins act together, as in polyomavirus"),
 au("au-hpv-fase-s", "HPV amplifies its genome in <b>differentiated</b> keratinocytes, which no longer divide, so it must force them back into {{c1::S phase}}",
    "V-pilar", D_, "HPV força a fase S em células diferenciadas", 43, "lâminas 43–44; apostila guia de Micro",
    extra="- E7 releases E2F by inactivating pRb, and E6 removes p53 so the cell does not arrest or die"),
 K(1463105915437, "V-hy", D_, "E7 do HPV inativa Rb", 43, "lâmina 43 (E7 ⊣ pRb)"),
 K(1463105909117, "V-hy", D_, "E6 do HPV degrada p53", 43, "lâmina 43 (E6 ⊣ p53)"),
 au("au-cancer-acidental", "Cancer caused by viruses is an {{c1::accidental}} by-product of their replication strategy, not a step of the viral cycle",
    "V-prova", D_, "Câncer viral é efeito acidental", 44, "lâminas 43–44; prova 2024 P4 2.13",
    extra="- E6 and E7 exist to replicate HPV; transformation does not make more virions"),
 au("au-polioma-papiloma", "Polyoma and papillomaviruses borrow host transcription, DNA synthesis and even the {{c1::histones}} that package their DNA",
    "R-detalhe", D_, "O que a célula fornece ao polioma e papiloma", 45, "lâminas 45 e 197",
    extra="- They contribute only multifunctional proteins (T antigen, E6, E7)"),
 # ---------- Adenovírus (lâminas 46–49) ----------
 au("au-adeno-pol", "Adenovirus uses the host RNA polymerase to make its mRNAs but encodes its own {{c1::DNA polymerase}} as an early protein",
    "A-aula", D_, "Adenovírus: polimerase própria", 46, "lâmina 46; apostila guia de Micro",
    extra="- A large DNA virus, partly independent of the cell"),
 au("au-adeno", "Adenovirus DNA synthesis starts at both ends from a <b>terminal protein</b> primer linked to {{c1::dCMP}}, by {{c2::strand displacement}}",
    "A-aula", D_, "Adenovírus: iniciador proteico e deslocamento de fita", 47, "lâminas 47–49 e 203–204; apostila guia de Micro",
    extra="- Both strands are made continuously, with no Okazaki fragments<br>- The protein primer leaves no 5' gap<br>" + IMG("adeno.jpg")),
 # ---------- Herpesvírus (lâminas 50–53) ----------
 au("au-herpes", "Herpesvirus linear DNA {{c1::circularizes}} in the nucleus and is copied by {{c2::rolling circle}}, making concatemers later cut into genomes",
    "A-aula", D_, "Herpesvírus: círculo rolante", 53, "lâminas 50–53 e 205–207; apostila guia de Micro",
    extra="- Host ligase closes the circle; one oriL and two oriS<br>" + IMG("rolling.png")),
 au("au-herpes-enzimas", "Herpesvirus encodes its own DNA polymerase and {{c1::helicase-primase}}, which makes its replication a target for antivirals",
    "A-aula", D_, "Herpesvírus: polimerase e helicase-primase próprias", 51, "lâminas 51 e 205 (UL5/8/52 primase, UL30 polimerase); lâmina 132",
    extra="- Viral enzymes differ from the host's, so drugs can tell them apart"),
 K(1502152053718, "A-aula", D_, "HSV replica no núcleo", 51, "lâminas 50–51"),
 # ---------- Poxvírus (lâminas 54–58) ----------
 K(1502570386887, "V-hy", D_, "Poxvírus: único DNA que replica no citoplasma", 54, "lâmina 54"),
 K(1502570452327, "V-hy", D_, "Poxvírus traz a própria RNA polimerase", 55, "lâmina 55"),
 au("au-pox-dna", "Purified vaccinia DNA is not {{c1::infectious}}, because the first mRNAs need the RNA polymerase packed in the virion",
    "A-aula", D_, "DNA do poxvírus sozinho não é infeccioso", 55, "lâmina 55 e 209",
    extra="- Right after losing the envelope, the core makes the early mRNAs<br>- Same logic as (−) RNA viruses"),
 # ---------- Parvovírus (lâminas 59–61) ----------
 au("au-parvo", "Parvovirus single-stranded DNA ends fold into {{c1::hairpins}}, whose 3'-OH primes copying by the host DNA polymerase",
    "A-aula", D_, "Parvovírus: grampo como iniciador", 60, "lâminas 60–61 e 213–214; apostila guia de Micro",
    extra="- Group II: ssDNA must become dsDNA before mRNA"),
 au("au-parvo-fase-s", "Parvoviruses replicate only in {{c1::dividing}} cells, because they rely entirely on host enzymes active in S phase",
    "A-aula", D_, "Parvovírus precisa de células em divisão", 59, "lâmina 59 (dependentes de enzimas celulares); Jawetz cap. 29",
    extra="- Contrast: HPV forces differentiated cells into S phase, parvovirus waits for dividing ones"),
 # ---------- Vírus de RNA: do genoma à proteína (lâminas 62–67) ----------
 au("au-lembrar", "Host cells cannot copy RNA from an RNA template, so every RNA virus must supply an {{c1::RNA-dependent RNA polymerase}}",
    "V-pilar", E_, "A célula não copia RNA de RNA", 67, "lâminas 67 e 79; prova 2024 P3 1.1",
    extra="- Whether the virion must carry it depends on the genome: can it be translated? is it a retrovirus?<br>- Retroviruses bring reverse transcriptase instead"),
 K(1516321085226, "V-hy", E_, "Reovírus: RNA de dupla fita", 64, "lâminas 63–64"),
 au("au-reo", "Inside the reovirus core, the virion polymerase transcribes each dsRNA segment into one {{c1::monocistronic}} mRNA",
    "A-aula", E_, "Reovírus: um mRNA por segmento", 64, "lâminas 64 e 220",
    extra="- The cell cannot transcribe dsRNA, so the polymerase must come in the virion"),
 # ---------- Grupo IV (lâminas 68–69) ----------
 au("au-ciclo-mais", ORG("<b>(+) RNA virus cycle</b>:<br>- translated into a {{c1::polyprotein}}<br>- {{c2::protease}} frees RdRp<br>- RdRp makes a {{c3::(-)}} strand<br>- which templates new genomes"),
    "V-pilar", E_, "Ciclo do vírus de RNA +", 68, "lâminas 68–69; provas 2025 P3 2.1 e 2018 P3 1.3",
    extra="- All in the cytoplasm<br>- The same (+) RNA serves as mRNA and as genome, so the purified genome is infectious"),
 K(1506609599866, "A-aula", E_, "Picornavírus: poliproteína clivada", 68, "lâmina 68"),
 K(1506627151740, "A-aula", E_, "Protease viral cliva a poliproteína", 68, "lâmina 68 (picornavírus)"),
 K(1608909035503, "A-aula", E_, "RNA + é copiado em fita − pelo complexo de replicação", 69, "lâminas 68–69 (fita − intermediária)"),
 K(1608909367152, "A-aula", E_, "Fita − é o molde dos novos genomas +", 69, "lâminas 68–69; prova 2018 P3 1.3"),
 # ---------- Grupo V (lâmina 70) ----------
 au("au-ciclo-menos", ORG("<b>(-) ssRNA virus cycle</b>:<br>- virion {{c1::RdRp}} transcribes mRNAs<br>"
                          "- new RdRp makes a full-length {{c2::(+)}} copy<br>- that copy templates new (-) genomes"),
    "V-pilar", E_, "Ciclo do vírus de RNA −", 70, "lâminas 70 e 222; prova 2015 P2 2.3",
    extra="- Non-segmented: cytoplasm · segmented (influenza): nucleus"),
 au("au-nucleoproteina", "The RdRp of (-) RNA viruses copies only genome coated by {{c1::nucleoprotein}}, so virions carry whole nucleocapsids",
    "A-aula", E_, "RdRp do RNA − só copia RNA com nucleoproteína", 81, "lâminas 81 e 226",
    extra="- That is why transcription can start right after entry"),
 K(1516320980606, "V-hy", E_, "Ortomixovírus replica no núcleo", 70, "lâmina 70"),
 au("au-cap-snatching", "Influenza replicates in the nucleus partly to steal 5' {{c1::caps}} from host pre-mRNAs with its endonuclease",
    "R-detalhe", E_, "Roubo do cap no influenza", 70, "lâminas 7 e 136 (endonuclease do influenza, cap snatching)",
    extra="- Without a cap, viral mRNA would not be read by host ribosomes<br>- Baloxavir blocks this endonuclease"),
 # ---------- Grupos VI e VII (lâminas 71–78) ----------
 au("au-retro", ORG("<b>Retroviral cycle</b>:<br>- (+) RNA not used as {{c1::mRNA}}<br>- {{c2::tRNA}}-primed reverse transcription<br>- {{c3::integrase}} inserts provirus<br>- host RNA pol II transcribes"),
    "V-pilar", E_, "Ciclo do retrovírus", 71, "lâminas 71–75 e 229–231",
    extra="- Integration is obligatory, which is why HIV cannot be cured"),
 K(1502069441823, "V-hy", E_, "HIV: transcriptase reversa e integrase", 72, "lâminas 71–75"),
 K(1506551550710, "V-hy", E_, "HBV: DNA de dupla fita parcial", 76, "lâminas 76–77"),
 K(1506551774430, "A-aula", E_, "HBV completa o DNA no núcleo", 77, "lâmina 77"),
 K(1523915541724, "A-aula", E_, "HBV: intermediário de RNA +", 77, "lâmina 77 (RNA pré-genômico)"),
 K(1506551930834, "A-aula", E_, "HBV usa transcriptase reversa", 77, "lâmina 77"),
 # ---------- RdRp e consequências (lâminas 79–83) ----------
 au("au-rdrp", "The RdRp of RNA viruses catalyzes both new {{c1::genomes}} and {{c1::mRNAs}}, so the virus must decide which to make",
    "V-pilar", E_, "RdRp faz genomas e mRNAs", 79, "lâminas 79 e 82; prova 2024 P3 1.1",
    extra="- Segmentation, polyproteins and internal signals help decide<br>- Viral RNA must also be told apart from host RNA"),
 sh(1792677740802, "azul", E_, "RNA negativo traz a polimerase no vírion", 80, "A-aula: lâminas 80–81; card da 57"),
 sh(1792677742577, "azul", E_, "Genoma de RNA negativo não é infeccioso", 80, "A-aula: lâmina 80; card da 57"),
 au("au-mutacao", "RNA viruses mutate fast because their RdRp lacks 3'→5' exonuclease {{c1::proofreading}}",
    "V-pilar", E_, "RdRp sem revisão: alta mutação", 83, "lâmina 83; Osmosis",
    extra="- Segmented genomes add reassortment (influenza)<br>- Fast change helps escape antibodies and drugs"),
 K(1523926575639, "A-aula", E_, "Rearranjo ocorre em vírus segmentados", 83, "lâmina 83"),
 K(1523806341324, "V-hy", E_, "Rearranjo causa shift antigênico", 83, "lâmina 83 (influenza)"),
 # ---------- Montagem (lâminas 84–86) ----------
 au("au-inclusao-local", "Inclusion bodies are viral components piled up at the {{c1::assembly}} site, so intranuclear ones mean assembly in the nucleus",
    "V-prova", F_, "Inclusão mostra o local de montagem", 85, "lâminas 84–86; prova 2015 P2 4.8",
    extra="- Assembly sites: cytosol, ER-Golgi, plasma membrane or nucleus"),
 au("au-inclusoes", ORG("<b>Viral inclusion bodies</b> by location:<br>- intranuclear: {{c1::herpes}}, adeno, parvo<br>- intracytoplasmic: {{c2::pox}}, reo, paramyxo, rabies"),
    "A-aula", F_, "Inclusões intranucleares × citoplasmáticas", 85, "lâminas 85 e 235",
    extra="- DNA viruses assembled in the nucleus vs. RNA viruses and pox in the cytoplasm"),
 au("au-maturacao", "Many viruses need a viral {{c1::protease}} to cut structural polyproteins during maturation, or the particles stay noninfectious",
    "A-aula", F_, "Maturação depende da protease viral", 84, "lâminas 84 e 138–139 (montagem e maturação do HIV)",
    extra="- In HIV, Gag and Gag-Pol are cut after budding<br>- This is the target of protease inhibitors"),
 # ---------- Liberação (lâminas 87–91) ----------
 au("au-liberacao", ORG("<b>Ways new virions leave the cell</b>:<br>- {{c1::lysis}}<br>- {{c1::budding}}<br>- direct passage to neighbor cells<br>- {{c2::syncytium}} formation"),
    "V-pilar", F_, "Quatro formas de liberação", 87, "lâminas 87–90 e 237–240",
    extra="- Naked viruses pile up and leave by lysis<br>" + IMG("brotamento.png")),
 au("au-brotamento", "Before budding, viral envelope {{c1::glycoproteins}} are inserted into the host membrane, and the nucleocapsid exits through that patch",
    "A-aula", F_, "Como o vírus brota", 88, "lâminas 88–89; Jawetz cap. 29 (fig. 29.3)",
    extra="- Enveloped viruses are not infectious until they bud, so they do not accumulate inside the cell"),
 K(1516401726231, "V-hy", F_, "Neuraminidase libera o vírion", 89, "lâminas 98 e 134 (influenza)"),
 au("au-sinapse", "HTLV-1 passes directly from infected to uninfected T cells through a {{c1::virological synapse}}",
    "R-detalhe", F_, "Passagem célula a célula do HTLV-1", 90, "lâminas 90 e 240",
    extra="- The virus avoids the extracellular space and antibodies"),
 K(1502066667272, "V-hy", F_, "gp41 do HIV forma sincícios", 87, "lâmina 87 (sincícios)"),
 K(1483913062659, "V-hy", F_, "RNA no citoplasma, exceto ortomixo e retro", 91, "lâmina 91 (resumão)"),
 # ---------- Antivirais: princípios (lâminas 93–99) ----------
 au("au-poucos", ORG("<b>Why antivirals are few</b>:<br>- few obvious targets<br>- each virus has its own proteins<br>- {{c1::latency}} escapes treatment<br>- works only {{c2::early}}"),
    "V-pilar", G_, "Por que há poucos antivirais", 94, "lâmina 94; apostila guia de Micro; Jawetz cap. 30",
    extra="- Similar symptoms from different viruses also delay diagnosis"),
 au("au-antiviral", ORG("<b>An antiviral may block</b>:<br>- free {{c1::virions}}<br>- binding or {{c1::entry}}<br>- genome {{c2::replication}}<br>- viral protein function<br>- {{c3::assembly}} or release"),
    "V-pilar", G_, "Mecanismos possíveis de um antiviral", 95, "lâminas 95–96 e 143; monitoria P3",
    extra="- The more a step depends on a virus-only protein, the more selective the drug"),
 # ---------- Entrada e desnudamento (lâminas 100–105) ----------
 K(1506806715774, "A-aula", H_, "Enfuvirtida bloqueia a fusão pela gp41", 102, "lâminas 100–102"),
 K(1506806433678, "A-aula", H_, "Maraviroc bloqueia o CCR5", 103, "lâmina 103"),
 K(1516401763134, "A-aula", H_, "Amantadina inibe o desnudamento", 104, "lâminas 104–105"),
 # ---------- Polimerases (lâminas 106–129) ----------
 au("au-polimerase-propria", "Polymerase inhibitors cannot treat {{c1::papillomavirus}} or polyomavirus, which copy their DNA with the <b>host polymerase</b>",
    "A-aula", G_, "Inibidor de polimerase só para polimerase própria", 107, "lâmina 107; monitoria P3",
    extra="- They work on viruses that encode their own polymerase or reverse transcriptase"),
 K(1506723958257, "A-aula", G_, "Análogo precisa ser fosforilado três vezes", 111, "lâminas 108–112"),
 K(1506784610676, "A-aula", G_, "Análogo sem 3'-OH termina a cadeia", 111, "lâmina 111"),
 K(1506723704374, "V-pilar", H_, "Aciclovir é ativado pela TK viral", 115, "lâminas 111 e 115; monitoria P3 (seletividade)"),
 K(1403635898739, "A-aula", H_, "Resistência ao aciclovir: TK mutada ou ausente", 115, "lâmina 115"),
 K(1506728737669, "A-aula", H_, "Foscarnet: análogo do pirofosfato", 117, "lâmina 117"),
 K(1506789392960, "A-aula", H_, "NNRTI liga outro sítio da TR", 124, "lâminas 123–124"),
 K(1506789263570, "V-hy", H_, "NNRTI não precisa de fosforilação", 124, "lâmina 124"),
 K(1461797689978, "R-detalhe", H_, "Sofosbuvir inibe a RdRp NS5B", 126, "lâminas 125–129"),
 # ---------- Outras enzimas e protease (lâminas 130–142) ----------
 K(1506807835841, "A-aula", H_, "Inibidor de integrase impede o provírus", 131, "lâmina 131"),
 K(1516324960043, "A-aula", H_, "Inibidores de neuraminidase impedem a saída", 134, "lâminas 134–135"),
 K(1506795652147, "A-aula", H_, "Inibidor de protease impede o vírion maduro", 138, "lâminas 137–142"),
 # ---------- Amplo espectro (lâminas 143–148) ----------
 au("au-amplo-espectro", "A broad-spectrum antiviral against RNA viruses can target the {{c1::RdRp}}, an enzyme they all need and host cells lack",
    "A-aula", G_, "Amplo espectro: atacar a RdRp", 145, "lâmina 145 (favipiravir, análogo de nucleosídeo)",
    extra="- Another option is the lipid envelope (LJ001), which spares naked viruses"),
 # ---------- Histórias de sucesso (lâminas 149–163) ----------
 au("au-hcv-hiv", "Antivirals can cure HCV infection, but not HIV, because HIV persists as an integrated {{c1::provirus}}",
    "V-pilar", G_, "HCV curável × HIV não", 153, "lâminas 150–163; apostila guia de Micro (não há cura para AIDS porque o vírus integra)",
    extra="- HCV cure = sustained virologic response, from combining drugs against protease, NS5A and polymerase"),
 K(1506783017772, "V-hy", G_, "HAART: três fármacos para evitar resistência", 163, "lâminas 161–163"),
]
for c in CARDS:  # a resposta do cloze autoral vai em negrito, como no AnKing
    if c["kind"] == "autoral":
        c["text"] = _re.sub(r"\{\{(c\d+)::(.*?)\}\}", lambda m: m.group(0) if "<b>" in m.group(2) else "{{%s::<b>%s</b>}}" % m.groups(), c["text"])
finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1502152021975": "- Exception: poxvirus, which replicates in the cytoplasm with its own enzymes",
 "ak1516321076508": "- Exceptions: influenza (orthomyxovirus) and retroviruses use the nucleus",
 "ak1467771853847": "- Every polymerase needs a template and a primer with a free 3'-OH",
 "ak1463105915437": "- Freed E2F starts S phase, so the differentiated cell copies DNA again",
 "ak1463105909117": "- Without p53 the cell neither arrests nor dies when DNA is copied out of program",
 "ak1502570386887": "- The host RNA polymerase is in the nucleus, out of its reach",
 "ak1502570452327": "- That is why vaccinia DNA stripped of proteins is not infectious",
 "ak1506609599866": "- The (+) genome is translated at once and viral proteases cut the chain",
 "ak1516320980606": "- Segmented (−) genomes replicate in the nucleus, non-segmented ones in the cytoplasm",
 "ak1502069441823": "- Integration into the host genome is obligatory: the provirus",
 "ak1506551550710": "- Host repair completes the gap before transcription",
 "ak1506551930834": "- A pregenomic RNA is reverse transcribed inside the core particle",
 "ak1523926575639": "- Influenza has 8 segments, so coinfection mixes them",
 "ak1523806341324": "- Shift is abrupt, drift comes from point mutations",
 "ak1502066667272": "- Fused infected cells form a syncytium, passing virus without leaving the cell",
 "ak1483913062659": "- Influenza and retroviruses use the nucleus",
 "ak1506806715774": "- Blocking entry stops the cycle before the genome gets in",
 "ak1506806433678": "- Only works if the virus uses CCR5",
 "ak1516324096049": "- Protons entering the virion trigger uncoating",
 "ak1516401763134": "- Without acidification the genome stays trapped until the lysosome degrades it",
 "ak1506784610676": "- The next nucleotide has nowhere to attach, so the chain stops",
 "ak1506723704374": "- Only infected cells activate the drug, which is why it is selective",
 "ak1506627151740": "- The protease is itself part of the polyprotein and cuts it in cis and in trans",
 "ak1403635898739": "- Without viral TK the drug is never activated: the price of selectivity",
 "ak1506806776715": "- Envelope glycoproteins follow the secretory pathway to the plasma membrane",
 "ak1608909035503": "- This (−) strand never serves as mRNA, only as a template",
 "ak1608909367152": "- Each (−) template yields many (+) genomes, amplifying the infection",
 "ak1506728737669": "- It needs no activation, so it works on thymidine-kinase-deficient virus",
 "ak1506789392960": "- They bind an allosteric pocket and do not need phosphorylation",
 "ak1461797689978": "- HCV RdRp has no cellular counterpart, a clean target",
 "ak1506807835841": "- Without integration there is no provirus to transcribe",
 "ak1516324960043": "- New virions stay stuck to sialic acid on the cell surface",
 "ak1506795652147": "- Uncleaved Gag-Pol polyproteins give noninfectious particles",
 "ak1506783017772": "- One drug selects resistant mutants quickly; three targets at once rarely fail together",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (ciclo, mecanismos, círculo rolante, iniciador proteico, antígeno T, brotamento) estão nos cards do conceito"
SLIDE_SEM_ALT = "esquema da própria aula, sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "mb58-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {
 "au-etapas": "uncoating e penetration também aparecem em cards de fármacos; aqui é a ordem do ciclo",
 "au-penetracao": "fusion também é resposta da enfuvirtida; aqui é uma das três vias de entrada",
 "au-lembrar": "RdRp também é resposta do sofosbuvir e da amplo espectro; aqui é por que todo vírus de RNA precisa dela",
 "au-amplo-espectro": "RdRp aparece em outros cards; aqui é o alvo comum a todos os vírus de RNA",
 "au-ciclo-menos": "RdRp do vírion também está no card associado da 57; aqui é a sequência do ciclo",
 "au-maturacao": "protease também é resposta do card de poliproteína; aqui é sua função na maturação",
 "au-gp41": "gp41 também é resposta da enfuvirtida e dos sincícios; aqui é o mecanismo da entrada",
 "au-por-que-nucleo": "RNA polymerase também é resposta do poxvírus; aqui é por que o DNA vai ao núcleo",
 "au-ciclo-mais": "protease e poliproteína têm cards do AnKing; aqui é a sequência inteira do ciclo pedida nas provas",
 "au-retro": "integrase também é resposta do card do HIV; aqui é a sequência do ciclo com o tRNA iniciador",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
STRIP_IMG = {  # F-20261022-CLAUDE-01: quadros que não batem com o cloze (célula vazia da animação, tabela de efeitos adversos)
 "ak1502066667272": ["aacb7afba5b4ddacc0439349e0bb7f71.webp"], "ak1506806715774": ["aacb7afba5b4ddacc0439349e0bb7f71.webp"],
 "ak1506806433678": ["aacb7afba5b4ddacc0439349e0bb7f71.webp"], "ak1502069441823": ["2d7ec7fa20c74336b35e28f972bfb3d7.webp"],
 "ak1506784610676": ["2d7ec7fa20c74336b35e28f972bfb3d7.webp"], "ak1461797689978": ["436bed9d794a18f2bf0f7257c4e123a6.webp"],
 "ak1506795652147": ["fb1617ebcc759d875ae3dd9119e84256.webp"],
}
IMAGENS_VISTAS = {
 "mb58-ciclo.jpg": "Lâmina 7: ciclo do influenza dividido em entrada (1), síntese (2) e saída (3); verso do organizador das etapas.",
 "mb58-mecanismos.png": "Lâmina 32: forquilha com iniciadores de RNA × deslocamento de fita com iniciador; verso de au-mecanismos.",
 "mb58-rolling.png": "Lâmina 53: círculo rolante com síntese contínua e concatâmero; verso de au-herpes.",
 "mb58-adeno.jpg": "Lâmina 48: proteína terminal ligada a dCMP como iniciador e deslocamento de fita; verso de au-adeno.",
 "mb58-brotamento.png": "Lâmina 88: capsídeo brotando pela membrana com proteínas do envelope; verso de au-liberacao.",
 "mb58-t-antigen.png": "Lâmina 36: antígeno T se liga à origem do SV40, muda de conformação e abre a dupla fita com ATP; verso de au-antigeno-t.",
}
REVISAO = {"despejo": "Despejo lido inteiro em 22/10 (97 notas novas, 137 cards; frentes, clozes, versos, imagens e cores conferidos; as imagens retiradas saíram). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Acompanhar a aula pelo processo: entrada, síntese, a estratégia de copiar o genoma por tipo de vírus (quem fornece a polimerase e o "
             "iniciador, o problema 5', a RdRp), montagem e saída, e cada antiviral como bloqueio de uma etapa com alvo próprio do vírus.",
 "centrais": [
   ("ciclo", "au-produtiva", "au-etapas"),
   ("entrada", "au-receptor", "au-penetracao", "au-desnudamento"),
   ("síntese", "au-precoce", "au-por-que-nucleo"),
   ("vírus de DNA", "au-pequeno-grande", "au-mecanismos", "au-5linha", "au-solucoes-5", "au-hpv-fase-s", "au-cancer-acidental"),
   ("vírus de RNA", "au-lembrar", "au-ciclo-mais", "au-ciclo-menos", "au-retro", "au-rdrp", "au-mutacao"),
   ("saída", "au-inclusao-local", "au-liberacao"),
   ("antivirais", "au-poucos", "au-antiviral", "ak1506723704374", "au-hcv-hiv"),
 ],
 "exemplos": ["fármacos por nome em cada etapa", "covid-19", "desenvolvimento de fármacos", "estruturas químicas"],
 "outras_aulas": [("efeito citopático", "60 Virologia prática"), ("inclusões por doença", "61 Patologia da infecção viral"),
                  ("oncogênese viral", "78 Carcinógenos biológicos"), ("farmacologia dos antivirais", "UC19"),
                  ("Baltimore, polaridade e estrutura", "57 Princípios gerais dos vírus (sh)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
