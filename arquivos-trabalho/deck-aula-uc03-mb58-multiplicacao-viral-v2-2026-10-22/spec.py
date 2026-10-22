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

PIPELINE_VERSAO = 5
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb58-20261022a"
SHORT = "mb58v"
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
 au("au-produtiva", "A viral infection is <b>productive</b> when it releases new infectious virions, and {{c1::abortive}} when it releases none",
    "A-aula", A_, "Infecção produtiva × abortiva", 6, "lâmina 6; apostila guia de Micro e monitoria P3 (produtiva × abortiva)",
    extra="- Abortive infections happen in nonpermissive cells or with defective viruses<br>- Infection itself means bringing the viral genome into the cell"),
 au("au-etapas", ORG("<b>Steps of the viral cycle</b>, in order:<br>- {{c1::adsorption}}<br>- penetration<br>- {{c1::uncoating}}<br>"
                     "- synthesis of proteins and genome<br>- {{c2::assembly}} and maturation<br>- {{c2::release}}"),
    "V-pilar", A_, "As etapas do ciclo viral", 8, "lâminas 7–8 e 96; apostila guia de Micro; prova 2025 P3 2.1 (etapas do ciclo)",
    extra="- Every antiviral targets one of these steps<br>" + IMG("ciclo.jpg")),
 # ---------- Adsorção, penetração, desnudamento (lâminas 9–19) ----------
 au("au-receptor", "<b>Adsorption</b> needs a receptor that only some cells express, so the receptor largely sets the virus {{c1::tropism}}",
    "V-pilar", B_, "Receptor específico define o tropismo", 9, "lâmina 9 (receptores reconhecidos de maneira específica); Jawetz cap. 29 (presença de receptor determina tropismo)",
    extra="- Receptors are host membrane proteins or sugars that the virus exploits<br>- HIV gp120, for instance, binds CD4 and a coreceptor"),
 sh(1792166995490, "azul", B_, "gp120 liga CD4 e correceptores (exemplo de adsorção)", 10, "A-aula: lâminas 10 e 15 (HIV); card da 51"),
 au("au-penetracao", ORG("<b>Viral penetration</b> routes:<br>- receptor-mediated {{c1::endocytosis}}<br>- translocation across the membrane<br>"
                         "- {{c2::fusion}} of the envelope with the plasma membrane"),
    "A-aula", B_, "Três vias de penetração", 11, "lâminas 11–16; apostila guia de Micro",
    extra="- Fusion is only possible for enveloped viruses (herpes, paramyxovirus, HIV)<br>- Endocytosis uses clathrin or caveolin pits"),
 au("au-desnudamento", "<b>Uncoating</b> frees the genome directly in the cytoplasm, after {{c1::endosome acidification}}, or at the nuclear pore",
    "A-aula", B_, "Onde ocorre o desnudamento", 17, "lâminas 17–19; apostila UC3 e monitoria P3",
    extra="- Adenovirus rides microtubules to the nuclear pore and releases its DNA there<br>- At uncoating the virion loses its infectivity: the eclipse phase"),
 # ---------- Síntese (lâmina 20) ----------
 au("au-precoce", "Early viral mRNAs make {{c1::nonstructural}} proteins for replication, and late mRNAs make {{c2::structural}} proteins",
    "A-aula", C_, "Proteínas precoces × tardias", 20, "lâmina 20; monitoria P3 (precoces não estruturais, tardias estruturais)",
    extra="- Copying the genome comes first, so capsid proteins are not made with nothing to package"),
 K(1502152021975, "A-aula", C_, "Vírus de DNA replicam no núcleo", 20, "lâmina 20 (DNA no núcleo); seção FirstAid"),
 K(1516321076508, "A-aula", C_, "Vírus de RNA replicam no citoplasma", 20, "lâmina 20 (RNA no citoplasma); seção Bootcamp"),
 # ---------- Polimerase e estratégia (lâminas 21–33) ----------
 sh(1792677734751, "azul", C_, "Grupos de Baltimore: a estratégia depende do genoma", 22, "A-aula: lâmina 22 (a estratégia depende da natureza do genoma); card da 57"),
 K(1467771853847, "A-aula", C_, "DNA polimerase precisa de iniciador", 23, "lâminas 23–24 (iniciador e molde)"),
 au("au-pequeno-grande", "Small DNA viruses rely on the host's {{c1::replication machinery}}, while large ones encode most of their own",
    "V-pilar", D_, "Vírus de DNA pequeno × grande", 29, "lâminas 28–30 e 197; apostila UC3",
    extra="- Even small ones must make at least one viral protein to start replication<br>- Small: papilloma, polyoma, parvo · Large: herpes, adeno, pox"),
 au("au-mecanismos", "Replication forks use {{c1::RNA}} primers, while strand displacement uses a protein or DNA hairpin instead",
    "A-aula", D_, "Dois mecanismos de síntese de DNA", 32, "lâminas 32 e 195; apostila guia de Micro",
    extra="- Fork: papilloma, polyoma, herpes, retroviral provirus<br>" + IMG("mecanismos.png")),
 au("au-5linha", "Removing the last RNA primer leaves the {{c1::5'}} end of a linear DNA strand uncopied",
    "A-aula", D_, "O problema da extremidade 5'", 33, "lâminas 33 e 196; monitoria P3",
    extra="- Circular genomes, protein or DNA primers and rolling circle all solve it<br>- Human chromosomes solve it with telomerase"),
 # ---------- Exemplos de vírus de DNA (lâminas 34–61) ----------
 au("au-antigeno-t", "Polyomavirus large {{c1::T antigen}} binds the replication origin and unwinds it as a helicase, recruiting the host polymerase",
    "A-aula", D_, "Antígeno T do poliomavírus", 36, "lâminas 36–37; apostila guia de Micro",
    extra="- The genome is circular, so there is no 5' problem<br>- Host topoisomerases relieve the twisting<br>" + IMG("t-antigen.png", 300)),
 au("au-hpv-fase-s", "HPV copies its genome in differentiating keratinocytes, which no longer divide, so its proteins push them back into {{c1::S phase}}",
    "A-aula", D_, "HPV força a síntese de DNA em células diferenciadas", 43, "lâminas 43–44; apostila guia de Micro",
    extra="- E7 unleashes DNA synthesis by acting on Rb, and E6 blocks p53-driven arrest and apoptosis<br>- Cancer is an accidental by-product of this strategy"),
 K(1463105915437, "A-aula", D_, "E7 do HPV inativa Rb", 43, "lâmina 43 (E7 ⊣ pRb)"),
 K(1463105909117, "A-aula", D_, "E6 do HPV degrada p53", 43, "lâmina 43 (E6 ⊣ p53)"),
 au("au-adeno", "Adenovirus DNA is primed by a terminal {{c1::protein}} bound to dCMP and copied by strand displacement, without Okazaki fragments",
    "A-aula", D_, "Adenovírus: iniciador proteico", 47, "lâminas 46–49 e 203–204; apostila guia de Micro",
    extra="- It uses the host RNA polymerase but encodes its own DNA polymerase<br>" + IMG("adeno.jpg")),
 au("au-herpes", "Herpesvirus DNA circularizes in the nucleus and is copied by {{c1::rolling circle}}, making concatemers that are later cleaved",
    "A-aula", D_, "Herpesvírus: círculo rolante", 53, "lâminas 50–53 e 205–207; apostila guia de Micro",
    extra="- It encodes its own DNA polymerase and helicase-primase, which antivirals target<br>" + IMG("rolling.png")),
 K(1502570386887, "V-hy", D_, "Poxvírus: único DNA que replica no citoplasma", 54, "lâmina 54 (vírus de DNA que replicam no citoplasma); seção Physeo"),
 K(1502570452327, "V-hy", D_, "Poxvírus traz a própria RNA polimerase", 55, "lâmina 55 (RNA polimerase dependente de DNA no vírion)"),
 au("au-parvo", "Parvovirus single-stranded DNA folds its ends into hairpins whose 3'-OH serves as the {{c1::DNA}} primer",
    "A-aula", D_, "Parvovírus: iniciador de DNA em grampo", 60, "lâminas 59–61 e 212–214; apostila guia de Micro",
    extra="- It depends on host enzymes in the nucleus, so it needs dividing cells<br>- Group II of Baltimore, the only ssDNA viruses"),
 # ---------- Vírus de RNA (lâminas 62–83) ----------
 au("au-lembrar", "A virus must {{c1::encode}} any enzyme for a step the cell cannot perform, like copying RNA",
    "V-pilar", E_, "O que a célula não faz, o vírus traz", 67, "lâminas 67 e 219 (Lembrar); conexão entre vírus de DNA e de RNA",
    extra="- Whether the virion must carry its polymerase depends on the genome: can it be translated? is it a retrovirus?"),
 K(1506609599866, "A-aula", E_, "RNA positivo vira uma poliproteína clivada", 68, "lâmina 68 (produção direta de uma poliproteína, Picornaviridae)"),
 K(1516320980606, "A-aula", E_, "Ortomixovírus: RNA negativo que replica no núcleo", 70, "lâmina 70 (genoma segmentado replica no núcleo)"),
 K(1502069441823, "V-hy", E_, "Retrovírus: transcriptase reversa e integração", 71, "lâminas 71–75 e 229–231 (transcrição reversa e integração obrigatória)"),
 K(1506551550710, "V-hy", E_, "HBV: DNA de dupla fita parcial", 76, "lâminas 76–77 (hepadnavírus)"),
 K(1506551930834, "A-aula", E_, "HBV usa transcriptase reversa a partir de RNA", 77, "lâmina 77 (DNA com intermediário de RNA)"),
 au("au-rdrp", "Every RNA virus except retroviruses encodes an {{c1::RNA-dependent RNA polymerase}}, which makes both new genomes and mRNAs",
    "V-pilar", E_, "Todo vírus de RNA codifica RdRp", 79, "lâminas 79 e 224; resumo geral (todos usam polimerase viral); prova 2024 P3 1.1 (proteína Q)",
    extra="- The cell has no enzyme that copies RNA from an RNA template<br>- Retroviruses copy RNA into DNA instead"),
 sh(1792677740802, "azul", E_, "RNA negativo traz a própria polimerase no vírion", 80, "A-aula: lâminas 80–81; card da 57"),
 sh(1792677742577, "azul", E_, "Genoma de RNA negativo não é infeccioso", 80, "A-aula: lâmina 80 (genomas não são infecciosos); card da 57"),
 au("au-mutacao", "RNA viruses mutate fast because their RNA polymerase has no {{c1::proofreading}}, and segmented genomes also exchange segments",
    "V-pilar", E_, "Alta taxa de mutação dos vírus de RNA", 83, "lâmina 83; apostila guia de Micro",
    extra="- Influenza shows both: point mutations and segment reassortment"),
 K(1523926575639, "A-aula", E_, "Rearranjo ocorre em vírus segmentados", 83, "lâmina 83 (reordenamento de segmentos)"),
 K(1523806341324, "A-aula", E_, "Rearranjo causa mudança antigênica (shift)", 83, "lâmina 83 (exemplo: influenza)"),
 # ---------- Montagem e liberação (lâminas 84–92) ----------
 au("au-montagem", "Viral assembly happens in the cytosol, ER-Golgi, plasma membrane or nucleus, and {{c1::inclusion bodies}} mark where it occurs",
    "V-prova", F_, "Montagem e corpúsculos de inclusão", 84, "lâminas 84–86; prova 2015 P2 4.8 (corpúsculo de inclusão indica o local de montagem)",
    extra="- Intracytoplasmic: pox, reo, paramyxo, rabies<br>- Intranuclear: herpes, adeno, parvo"),
 au("au-liberacao", ORG("<b>Ways new virions leave the cell</b>:<br>- {{c1::lysis}}<br>- {{c1::budding}}<br>- direct passage to neighbor cells<br>"
                        "- {{c2::syncytium}} formation"),
    "A-aula", F_, "Quatro formas de liberação", 87, "lâminas 87–90 e 237–240; apostila guia de Micro",
    extra="- Naked viruses usually leave by lysis, enveloped ones by budding, which gives them the envelope<br>" + IMG("brotamento.png")),
 K(1502066667272, "V-hy", F_, "gp41 do HIV faz fusão e sincícios", 89, "lâminas 87 e 15 (fusão de membranas, sincícios)"),
 K(1483913062659, "V-hy", F_, "Vírus de RNA no citoplasma, exceto ortomixo e retro", 91, "lâmina 91 (resumão: regra e casos particulares)"),
 # ---------- Antivirais: princípio (lâminas 93–99) ----------
 au("au-poucos", "There are few antivirals because viruses use the host's own machinery, leaving few {{c1::virus-specific}} targets",
    "V-pilar", G_, "Por que há poucos antivirais", 94, "lâmina 94; apostila guia de Micro; Jawetz cap. 30",
    extra="- Each virus also has its own proteins, some stay latent, and many are treatable only early"),
 au("au-antiviral", "An antiviral must block a step of the viral cycle without being too {{c1::toxic}} to the host cell",
    "V-pilar", G_, "Definição de antiviral", 95, "lâminas 95–96; monitoria P3",
    extra="- It may inactivate free virions or block entry, genome replication, viral protein function, assembly or release"),
 # ---------- Entrada e desnudamento (lâminas 100–105) ----------
 K(1506806715774, "A-aula", H_, "Inibidor de fusão: enfuvirtida na gp41", 102, "lâminas 100–102"),
 K(1506806433678, "A-aula", H_, "Maraviroc bloqueia CCR5", 103, "lâmina 103"),
 K(1516324096049, "A-aula", H_, "M2 do influenza acidifica para o desnudamento", 104, "lâminas 104–105"),
 K(1516401763134, "A-aula", H_, "Amantadina inibe o desnudamento", 104, "lâminas 104–105"),
 # ---------- Polimerases (lâminas 106–129) ----------
 au("au-polimerase-propria", "Viral polymerase inhibitors work only against viruses that encode their own {{c1::polymerase}}, as nucleoside analogs or non-analogs",
    "V-pilar", G_, "Inibidores de polimerase: só para quem tem polimerase própria", 107, "lâmina 107; monitoria P3 (não serve para papiloma e poliomavírus)",
    extra="- Papilloma and polyoma use the host polymerase, so these drugs cannot reach them"),
 K(1506784610676, "A-aula", G_, "Análogo sem 3'-OH termina a cadeia", 111, "lâminas 108–112 (análogos de nucleosídeo)"),
 K(1506723704374, "V-pilar", H_, "Aciclovir é ativado pela timidina quinase viral", 115, "lâminas 111 e 115; monitoria P3 (seletividade pela TK viral)"),
 K(1506728737669, "A-aula", H_, "Foscarnet: análogo do pirofosfato, sem ativação", 117, "lâmina 117 (não análogo de nucleosídeo)"),
 K(1506789392960, "A-aula", H_, "NNRTI liga outro sítio da transcriptase reversa", 124, "lâminas 123–124 (não análogos, sítio alostérico)"),
 K(1461797689978, "R-detalhe", H_, "Sofosbuvir inibe a RdRp NS5B do HCV", 126, "lâminas 125–129 (inibidores da replicase)"),
 # ---------- Outras enzimas e protease (lâminas 130–142) ----------
 K(1506807835841, "A-aula", H_, "Inibidor de integrase impede a integração", 131, "lâmina 131"),
 K(1516324960043, "A-aula", H_, "Inibidores de neuraminidase impedem a saída", 134, "lâminas 134–135 (inibidores do brotamento)"),
 K(1506795652147, "A-aula", H_, "Inibidor de protease impede o vírion maduro", 138, "lâminas 137–142 (poliproteínas precisam ser processadas)"),
 # ---------- Histórias de sucesso (lâminas 149–163) ----------
 K(1506783017772, "V-hy", G_, "HAART: três fármacos para evitar resistência", 163, "lâminas 155–163 (terapia combinada)"),
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
 "au-etapas": "uncoating também é resposta do card da amantadina; aqui é a posição da etapa no ciclo",
 "au-penetracao": "fusion também aparece no card da enfuvirtida; aqui é uma das três vias de entrada",
 "au-rdrp": "RdRp também é resposta no card do sofosbuvir; aqui é a regra de que todo vírus de RNA a codifica",
 "au-polimerase-propria": "polymerase aparece em outros cards; aqui o alvo é a condição para o inibidor funcionar",
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
REVISAO = {"despejo": "Despejo lido inteiro em 22/10 (51 notas novas, 69 cards; frentes, clozes, versos, imagens e cores conferidos; as imagens retiradas saíram). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Acompanhar a aula: as etapas comuns do ciclo, a estratégia de replicação que depende do genoma (DNA pequeno × grande, iniciadores, RdRp e "
             "mutação), montagem e saída, e os antivirais como bloqueio de uma etapa com alvo próprio do vírus.",
 "centrais": [
   ("ciclo", "au-produtiva", "au-etapas"),
   ("entrada", "au-receptor", "au-penetracao", "au-desnudamento"),
   ("vírus de DNA", "au-pequeno-grande", "au-mecanismos", "au-5linha"),
   ("vírus de RNA", "au-lembrar", "au-rdrp", "au-mutacao"),
   ("saída", "au-montagem", "au-liberacao"),
   ("antivirais", "au-poucos", "au-antiviral", "au-polimerase-propria", "ak1506723704374", "ak1506783017772"),
 ],
 "exemplos": ["famílias de vírus de DNA e de RNA", "fármacos por nome em cada etapa", "covid-19", "desenvolvimento de fármacos"],
 "outras_aulas": [("efeito citopático", "60 Virologia prática"), ("inclusões por doença", "61 Patologia da infecção viral"),
                  ("oncogênese viral", "78 Carcinógenos biológicos"), ("farmacologia dos antivirais", "UC19"),
                  ("Baltimore, polaridade e estrutura", "57 Princípios gerais dos vírus (sh)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
