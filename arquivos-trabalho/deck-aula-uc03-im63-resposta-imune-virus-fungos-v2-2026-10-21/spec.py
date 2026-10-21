# Especificação curada — 63 Organização da resposta imune aos vírus e fungos (UC03 P3, Imunologia; 81 lâminas = vírus 1–40 e fungos 41–81).
# Ciclo básico: princípios da resposta imune a vírus e a fungos (reconhecimento, efetores, evasão), sem clínica. Cópias NEBLI vivas entram por acervo()/sh().
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ("O AnKing cobre interferons, NK, CTL e o CMV, mas não traz o que a aula ensina sobre fungos (parede como PAMP, inflamassoma → Th17/Th1, Th1 e Th17 × Th2 e Treg) nem a organização dos TLRs e do escape viral; busca em seções, palavra-chave e significado não achou esses cards.")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-im63-20261021a"
SHORT = "im63"
LESSON = "2026-uc03-imunologia-63-resposta-imune-virus-fungos"
DECK = "NEBLI::UC03::P3::Imunologia::Resposta imune a vírus e fungos"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261021-CLAUDE-01 + ANTI-EXEMPLARES §1–16, 21/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (21/10): seções de recurso do AnKing (defesa do hospedeiro, NK, IFN-γ; busca/secoes); palavra-chave e significado em AnKing, "
         "Referências Externas e NEBLI vivo (busca/semantica.jsonl, uma consulta por conceito). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


A_, F1_, F2_, F3_, V1_, V2_, V3_ = "A-principios", "B-fungos-reconhecimento", "C-fungos-padrao-th", "D-fungos-efetores", "E-virus-inata", "F-virus-adaptativa", "G-virus-evasao"
EXCLUIDOS = []
FORA_DO_RECORTE = [
    "Repetição das lâminas 3–12 (introdução da parte de vírus repete a de fungos), capas e figuras de livro (Figure 11-5, lâminas 36–39).",
    "Vírus e câncer (lâmina 40): é a aula 78 Agentes carcinogênicos biológicos; epidemias de influenza em datas e números, dengue e sorotipos (lâminas 29–31): ilustração e outra aula.",
    "Paracoccidioidomicose (lâminas 79–81) e lista de fungos oportunistas × primários (lâmina 55): é o Grand Round 4 e a micologia; aqui fica o princípio Th1 × Th2.",
    "Imunodeficiências, clínica das micoses e dos vírus, e fármacos: patologia, micologia e farmacologia.",
]

FAIXAS = [[41, 81], [1, 40]]  # ordem em que as aulas foram dadas: fungos (lâminas 41–81) antes de vírus (1–40), como diz a transcrição

CARDS = [
    # Fungos (aula anterior, lâminas 41–81)
    au("au-balanca", "The outcome of an <b>infection</b> is the balance between pathogen {{c1::pathogenicity}} and host immune {{c2::response}}",
       "V-pilar", A_, "Infecção: patogenicidade × resposta imune", 42, "lâminas 2 e 42; transcrição (balanço entre o patógeno e a resposta imune)",
       extra="- An exaggerated response can itself damage tissue, as in hepatitis, where the immune response injures hepatocytes<br>- Pathogens survive by evading the immune response"),
    K(1487640050564, "A-aula", F1_, "TLR ativa NF-κB e a resposta imune", 47, "lâmina 47 (reconhecimento por TLR); seção de imunologia"),
    K(1520715624658, "A-aula", F1_, "Inflamassoma: complexo citoplasmático que reconhece produtos microbianos", 52, "lâmina 52 e transcrição (inflamassoma e NLR)"),
    au("au-inflam-sinais", ORG("<b>Inflammasome</b>:<br>- signal 1: {{c1::NF-κB}} makes pro-IL-1β<br>- signal 2: {{c2::ATP}} or K+ efflux assembles it<br>- {{c3::caspase-1}} makes active IL-1β"),
       "V-pilar", F1_, "Inflamassoma: dois sinais e caspase-1", 52, "lâmina 52; transcrição (primeiro sinal pelo PRR e segundo pelo ATP e fluxo de potássio)",
       extra="- IL-1β is made as an inactive precursor and must be cleaved<br>- The same pathway releases active IL-18"),
    au("au-fungos-pamps", "The <b>fungal wall</b> is rich in sugars, such as {{c1::β-glucan}} and mannans, that act as {{c2::PAMPs}}",
       "V-pilar", F2_, "Parede do fungo: açúcares como PAMPs", 58, "lâmina 58 (os fungos são doces); transcrição e apostila guia de Imuno (lectinas tipo C)",
       extra="- C-type lectin receptors recognize them, with help from TLRs<br>- Several receptors recognize different molecules of the same fungus"),
    sh(1791743340332, "azul", F2_, "β-glucana do fungo é reconhecida pela Dectin-1", 59, "A-aula: lâmina 59 (reconhecimento de estruturas dos fungos); card de outra aula"),
    sh(1791743344060, "azul", F2_, "NETs: redes de cromatina com proteínas antimicrobianas", 62, "A-aula: lâmina 62 (NETs contra fungos); card de outra aula"),
    K(1487116831797, "A-aula", F2_, "MHC II apresenta antígenos exógenos ao CD4", 65, "lâmina 65 e transcrição (a APC fagocita o fungo e apresenta ao CD4)"),
    K(1487116849895, "A-aula", F2_, "Segundo sinal do T: B7 liga CD28", 65, "lâmina 65 e transcrição (coestimulação na ativação do T)"),
    K(1520715849479, "A-aula", F2_, "Inflamassoma aumenta IL-1β e IL-18", 63, "lâmina 63 (fungos ativam o inflamassoma NLRP3)"),
    au("au-fungos-il1", "<b>Fungi</b> activate NLRP3, and IL-1β drives {{c1::Th17}} while IL-18 drives {{c2::Th1}}",
       "A-aula", F2_, "Inflamassoma: IL-1β para Th17 e IL-18 para Th1", 63, "lâmina 63; transcrição e apostila guia de Imuno (inflamassoma estimula Th17 via IL-1β e Th1 via IL-18)",
       extra="- Innate recognition dictates the pattern of adaptive immunity<br>- IL-12 from the antigen-presenting cell also induces Th1"),
    K(1487116888778, "A-aula", F2_, "IFN-γ e IL-12 induzem Th1", 64, "lâmina 64 (o padrão inato determina o Th)"),
    K(1487116975048, "A-aula", F2_, "IL-1, IL-6 e TGF-β induzem Th17", 64, "lâmina 64 (o padrão inato determina o Th)"),
    au("au-fungos-protecao", "<b>Th1</b> and Th17 responses protect against fungi, whereas {{c1::Th2}} and {{c2::Treg}} responses make the disease worse",
       "V-pilar", F2_, "Th1 e Th17 protegem; Th2 e Treg pioram", 66, "lâminas 66–67 e 73–74; transcrição e apostila guia de Imuno",
       extra="- TLR2 signaling favors Treg, which is deleterious in fungal infection<br>- Exception: in Pneumocystis a Th2 response may protect"),
    K(1487116895205, "A-aula", F2_, "IL-4 e IL-10 inibem Th1", 66, "lâmina 66 (Th1 e Th2 são uma balança)"),
    K(1487116928027, "V-pilar", F3_, "Th1 ativa macrófagos e T citotóxicos", 68, "lâmina 68 (a imunoproteção por Th1 e APC)"),
    K(1520716108281, "A-aula", F3_, "Th1 ativa macrófagos M1", 69, "lâmina 69 (Th1 e M1 × Th2 e M2)"),
    K(1520717070355, "A-aula", F3_, "Th2 ativa macrófagos M2", 69, "lâmina 69"),
    K(1487643792482, "A-aula", F3_, "Granuloma: IL-12 dos macrófagos", 70, "lâmina 70 (granulomas de pulmão com fungo)"),
    K(1487643795892, "A-aula", F3_, "Granuloma: IFN-γ do Th1 gera histiócitos epitelioides", 70, "lâmina 70"),
    K(1503254160003, "A-aula", F3_, "Sem TNF-α não há granuloma e a infecção reativa", 70, "lâmina 70 (importância do Th1 e do TNF-α)"),
    K(1520300296240, "A-aula", F3_, "Th17 recruta neutrófilos", 71, "lâmina 71 (a imunidade Th17 é protetora)"),
    K(1520300013308, "A-aula", F3_, "Th17 secreta IL-17, IL-21 e IL-22", 71, "lâmina 71"),
    K(1487117295752, "A-aula", F3_, "CD8 induz apoptose por perforinas e granzimas", 72, "lâmina 72 (CD8 confere imunoproteção contra fungos)"),
    K(1487117300306, "R-detalhe", F3_, "CD8 induz apoptose por Fas ligante e Fas", 72, "lâmina 72"),
    K(1487116971703, "A-aula", F3_, "Treg produz IL-10, IL-35 e TGF-β", 73, "lâmina 73 (Treg deletério ou protetor)"),
    K(1487640169311, "A-aula", F3_, "Via das lectinas: manose na superfície do micróbio", 77, "lâmina 77 (fungos ativam as três vias do complemento)"),
    K(1487640151914, "A-aula", F3_, "Via clássica começa em C1, ativado por IgM ou IgG", 77, "lâmina 77 (anticorpos contra o fungo ativam a via clássica)"),
    # Vírus (lâminas 1–40)
    K(1487117288751, "A-aula", V1_, "Imunidade celular defende contra agentes intracelulares", 6, "lâmina 6 (localização × imunidade); seção Bootcamp de defesa do hospedeiro"),
    K(1461792762468, "A-aula", V1_, "Interferons: citocinas liberadas por células infectadas por vírus", 13, "lâmina 13 (inibição da replicação por IFN α/β); seção Bootcamp de defesa"),
    au("au-tlr-virus", "<b>Viral nucleic acids</b> are sensed by {{c1::TLR3}} (dsRNA), {{c2::TLR7 and TLR8}} (ssRNA) and {{c2::TLR9}} (CpG DNA)",
       "V-pilar", V1_, "TLRs que reconhecem vírus", 14, "lâmina 14; transcrição e monitoria P3 de Imuno (TLR3, TLR7/8, TLR9)",
       extra="- Cytosolic RNA sensors, such as RIG-I, and NLRs also detect viruses"),
    K(1497440851060, "A-aula", V1_, "Vírus no citosol disparam interferon tipo I por receptores citosólicos", 14, "lâmina 14; seção Bootcamp de defesa"),
    K(1489970693302, "V-pilar", V1_, "IFN α/β preparam as células vizinhas", 17, "lâmina 17 (estado antiviral); seção Bootcamp de defesa"),
    K(1520301328706, "A-aula", V1_, "IFN tipo I reduz a síntese proteica", 17, "lâmina 17 (ação antiviral do IFN α/β, via PKR); seção Bootcamp de defesa"),
    K(1497450277629, "R-detalhe", V1_, "RNA dupla fita no citosol leva à apoptose via IFN", 17, "lâmina 17; seção Bootcamp de defesa"),
    K(1520301453074, "A-aula", V1_, "IFN tipo I aumenta o MHC I da célula", 17, "lâmina 17; seção Bootcamp de defesa"),
    K(1487117304665, "A-aula", V1_, "NK: linfócito da imunidade inata", 14, "lâmina 14 (células NK); seção FirstAid de NK"),
    K(1487117310594, "A-aula", V1_, "IFN α e β ativam as NK", 14, "lâmina 14 e 19; seção FirstAid de NK"),
    K(1487117314403, "V-pilar", V1_, "NK mata células sem MHC I", 14, "lâmina 14 (citotoxicidade para células infectadas); seção FirstAid de NK"),
    K(1487117308213, "A-aula", V1_, "NK induz apoptose por perforina e granzima", 14, "lâmina 14; seção FirstAid de NK"),
    K(1487640158306, "A-aula", V1_, "Via alternativa do complemento: ativação espontânea", 15, "lâmina 15 (complemento pela via alternativa, sem anticorpo)"),
    K(1489970456186, "A-aula", V1_, "Quem secreta IFN-γ: NK e Th1", 19, "lâmina 19 (NK produz IFN-γ); seção FirstAid de IFN-γ"),
    K(1489970364081, "A-aula", V1_, "IFN-γ ativa macrófagos para matar o que fagocitaram", 19, "lâmina 19; seção FirstAid de IFN-γ"),
    au("au-ac-fab-fc", "<b>Antibodies</b> protect against viruses by {{c1::neutralization}} (Fab) and, through Fc, by {{c2::ADCC}} and {{c3::complement}}",
       "A-aula", V2_, "Anticorpos: neutralização (Fab) e ADCC e complemento (Fc)", 19, "lâminas 19 e 21; transcrição (neutralização, ADCC, complemento, opsonização)",
       extra="- IgA and IgG neutralize the virus before it enters the cell<br>- Fc also allows opsonization, which matters less for viruses"),
    K(1487117328797, "A-aula", V2_, "A imunoglobulina da ADCC é IgG", 19, "lâmina 19 (ADCC); seção Bootcamp de defesa"),
    K(1487115889320, "A-aula", V2_, "MHC I apresenta antígenos endógenos ao CD8", 21, "lâmina 21 (via MHC classe I)"),
    au("au-ctl-duplo", "A <b>CD8</b> T cell primed by a {{c1::dendritic}} cell must find the peptide on {{c2::MHC I}} of the infected cell",
       "V-pilar", V2_, "CD8: primado pela dendrítica, reconhece o peptídeo na célula infectada", 21, "lâmina 21; transcrição (reconhecimento duplo do CD8)",
       extra="- CD4 help and cross-presentation prime the CD8 cell<br>- Then it releases perforin, granzyme and Fas ligand and survives to kill again"),
    K(1487117293576, "V-pilar", V2_, "CD8 T mata células infectadas por apoptose", 21, "lâmina 21 (citotoxicidade por CTL); seção Bootcamp de defesa"),
    sh(1791629595197, "azul", V2_, "Anticorpos neutralizantes bloqueiam a ligação aos receptores", 21, "A-aula: lâmina 21 (neutralização por IgG e IgA); card da aula 22"),
    K(1487117255825, "A-aula", V2_, "IgA secretora: componente secretor protege no lúmen", 21, "lâmina 21 (IgA de alta afinidade neutraliza); provas de Imuno (IgA em mucosa)"),
    K(1487117156031, "R-detalhe", V2_, "IL-5 e TGF-β promovem a troca para IgA", 21, "lâmina 21 e provas de Imuno (geração de IgA na mucosa)"),
    au("au-evasao-mhc", "<b>Viruses</b> lower MHC I by blocking the {{c1::proteasome}}, {{c2::TAP}} or MHC I export from the {{c2::ER}}",
       "A-aula", V3_, "Escape viral: queda do MHC I", 25, "lâmina 25; transcrição e monitoria P3 de Imuno (bloqueio do proteassoma e do TAP, retenção no RE)",
       extra="- HSV blocks TAP with ICP47; CMV also lowers MHC I<br>- Low MHC I protects from CD8 cells but exposes the cell to NK cells"),
    K(1503876156644, "A-aula", V3_, "CMV bloqueia o MHC I e a morte pelo CD8", 25, "lâmina 25 (CMV inibe classe I)"),
    K(1489970615786, "A-aula", V3_, "IL-10 atenua a resposta inflamatória", 27, "lâmina 27 (homólogo de IL-10 do EBV)"),
    au("au-evasao-ifn", "<b>HCV</b> blocks interferon signaling through {{c1::PKR}}, and SARS-CoV-2 lowers {{c2::IFN α/β}} production",
       "A-aula", V3_, "Escape viral: bloqueio da resposta de interferon", 27, "lâmina 27; transcrição (HCV bloqueia PKR e o coronavírus reduz o IFN α/β)",
       extra="- IFN α/β is the main early antiviral cytokine<br>- Lower IFN α/β has been linked to more severe COVID-19"),
    K(1506805786448, "A-aula", V3_, "HIV infecta linfócitos T CD4, macrófagos e células dendríticas", 28, "lâmina 28 (imunossupressão por destruição de CD4)"),
    K(1516321589458, "A-aula", V3_, "Variação antigênica do influenza: HA e NA", 29, "lâminas 29–34; transcrição e seção de influenza"),
    K(1516323064948, "A-aula", V3_, "Virada: reassortment de HA e NA entre espécies", 29, "lâmina 29 (troca de material genético com vírus de outras espécies)"),
    K(1516322271299, "A-aula", V3_, "Variação antigênica: deriva ou virada", 30, "lâmina 30 (mecanismos de variação)"),
    K(1516322855117, "A-aula", V3_, "Deriva: mutações pontuais em HA ou NA", 31, "lâmina 31 (escape por mutações)"),
]

_CZ = _re.compile(r"\{\{c(\d+)::((?:(?!\}\}).)*?)(::(?:(?!\}\}).)*?)?\}\}", _re.S)
def _bold_cloze(t):
    def sub(m):
        corpo = m.group(2)
        if "<b>" not in corpo and "<strong>" not in corpo:
            corpo = f"<b>{corpo}</b>"
        return "{{c%s::%s%s}}" % (m.group(1), corpo, m.group(3) or "")
    return _CZ.sub(sub, t)
for _c in CARDS:
    if _c["kind"] == "autoral":
        _c["text"] = _bold_cloze(_c["text"])

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1461792762468": "- Interferons signal neighboring cells to resist viral replication",
 "ak1487640050564": "- TLR signaling is the first signal that makes the cell produce pro-IL-1β and other cytokines",
 "ak1520715624658": "- It senses microbial products, dead-cell products and crystals",
 "ak1487116831797": "- The antigen-presenting cell phagocytoses the fungus, processes it in the endosome and loads MHC II",
 "ak1487116849895": "- Without B7-CD28 the T cell is not fully activated",
 "ak1520301328706": "- Less protein synthesis in the cell means less viral protein",
 "ak1497450277629": "- Enzymes such as PKR and RNase L stop translation and trigger apoptosis",
 "ak1487117310594": "- IFN α/β also raises the cytotoxic capacity of NK cells",
 "ak1487117308213": "- Perforin opens pores in the membrane and granzymes enter and cause apoptosis",
 "ak1487640158306": "- C3b formed by spontaneous C3 hydrolysis binds the virus if regulatory proteins do not stop it",
 "ak1489970456186": "- NK cells make IFN-γ after IFN α/β, which activates CD8 cells and macrophages",
 "ak1487117328797": "- NK cells recognize the Fc of IgG bound to the infected cell through CD16",
 "ak1487117293576": "- In hepatitis the injury of hepatocytes is caused by this immune response, not only by the virus",
 "ak1487117255825": "- IgA neutralizes enteric and respiratory viruses on the mucosa",
 "ak1503876156644": "- Without MHC I on the surface, CD8 cells cannot recognize the infected cell",
 "ak1489970615786": "- EBV makes an IL-10 homolog that lowers lymphocytes, dendritic cells and macrophages",
 "ak1506805786448": "- Losing CD4 cells removes the help that CD8 cells and B cells need",
 "ak1516322855117": "- Small mutations only partly reduce immunity from earlier infections, which is why the vaccine changes every year",
 "ak1516323064948": "- New antigens make people, even vaccinated, susceptible to the new strain",
 "ak1487116888778": "- IL-12 comes from the antigen-presenting cell after innate recognition",
 "ak1487116975048": "- IL-17 then activates neutrophils against the fungus",
 "ak1520300013308": "- IL-17 also keeps the epithelium intact and IL-22 induces antimicrobial peptides",
 "ak1487116971703": "- Treg can inhibit Th1 and Th17 and favor fungal spread",
 "ak1487640169311": "- Fungi activate all three complement pathways: lectin, alternative and classical",
 "ak1487640151914": "- The classical pathway needs antibodies against the fungus",
 "ak1487117300306": "- Fas ligand binds Fas and causes apoptosis, as perforin and granzyme do",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
exec((HERE / "exclusoes.py").read_text(encoding="utf-8")) if (HERE / "exclusoes.py").exists() else None

SEM_IMAGEM = "fato ou conjunto sem estrutura a reconhecer; as figuras da aula são esquemas de livro sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
DUPLICACAO = {"au-fungos-il1": "au-inflam-sinais explica como o inflamassoma gera IL-1β; este liga IL-1β e IL-18 ao padrão Th17 e Th1 que o AnKing traz separado", "au-ctl-duplo": "os cards de CD8 e MHC I dão cada peça; este junta o reconhecimento duplo (primado pela dendrítica e reconhecimento na célula infectada)", "au-evasao-mhc": "os cards de CMV e NK citam o resultado; este nomeia as três etapas bloqueadas (proteassoma, TAP, retenção no RE)"}
for _k, _v in DUPLICACAO.items():
    _c = next((c for c in CARDS if c["key"] == _k), None)
    if _c:
        _c["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
    "objetivo": "Explicar como o sistema imune reconhece e controla fungos e vírus (inata e adaptativa) e como esses patógenos evadem a resposta.",
    "centrais": [("princípio", "au-balanca"), ("reconhecimento", "au-inflam-sinais"), ("fungos", "au-fungos-pamps", "au-fungos-protecao"), ("defesa antiviral", "au-tlr-virus", "au-ctl-duplo")],
    "exemplos": ["epidemias de influenza em datas", "paracoccidioidomicose", "vírus e câncer", "dengue"],
    "outras_aulas": [("hipersensibilidade", "64 Reações de hipersensibilidade"), ("vírus e câncer", "78 Agentes carcinogênicos biológicos"),
                     ("paracoccidioidomicose", "53 Grand Round 4"), ("interferon, NK e complemento", "08 e 31 (sh)")],
}

_slide = lambda c: int(_re.search(r"\d+", c["evid"]).group())
CARDS.sort(key=lambda c: next((i for i, f in enumerate(FAIXAS) if f[0] <= _slide(c) <= f[1]), len(FAIXAS)) * 1000 + _slide(c))
