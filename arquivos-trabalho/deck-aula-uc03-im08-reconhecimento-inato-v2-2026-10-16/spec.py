# Especificação curada — Reconhecimento inato no sistema imune (UC03 P1, Imunologia; Barbuto; 23 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing → cópias NEBLI vivas (37/38, 61, 45, 31, 51) por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
# Nunca associar 1791667093238 (nota aberta no navegador de Davi em 16/10) nem 1791743339611 (cópia antiga em português).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06 (só notas do baralho AnKing; cópias NEBLI por sh)
    "_FirstAid_04_Pathology_Acute_inflammation_Toll_Like_Receptors.txt",
    "_FirstAid_04_Pathology_Acute_inflammation_Inflammasome.txt",
    "_FirstAid_02_Immunology_Innate_vs_adaptive_Innate.txt",
]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"  # F-20261015-CLAUDE-06: liga os gates duros (cobertura_anking, cores_rubrica, inducao_clozes); não remover
RUN_ID = "uc03-im08-20261016a"
SHORT = "im08n"
LESSON = "2026-uc03-imunologia-08-reconhecimento-inato"
DECK = "NEBLI::UC03::P1::Imunologia::Reconhecimento imune inato"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 16/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (16/10): seções de recurso do AnKing (FirstAid TLR, inflamassoma, inata × adaptativa, interferons; busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt: PRR, TLR, NOD/inflamassoma, MyD88/NF-κB, IFN tipo I, citotoxicidade, "
         "fagocitose, citocinas, febre, CSF, lipídicos, autoinflamatórias); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
EXCLUIDOS = [
 (1487639996379, "seção TLR: PRR × PAMP — entra a cópia NEBLI da aula 38 (sh-1791780342851)"),
 (1487640028986, "seção TLR: CD14 + TLR4 + LPS — entra a cópia NEBLI (sh-1791743339358)"),
 (1520715624658, "seção inflamassoma: definição — entra a cópia NEBLI (sh-1791743339740)"),
 (1520715849479, "seção inflamassoma: IL-1β e IL-18 — entra a cópia NEBLI (sh-1791743339860)"),
 (1486867513384, "seção inata: inespecífica — card da aula 07 (ak-inata-inespecifica)"),
 (1486867518070, "seção inata: sem memória — card da aula 07 (ak-inata-memoria)"),
 (1486867532110, "seção inata: minutos a horas — card da aula 07 (ak-inata-rapida)"),
 (1486867606359, "seção inata: diversidade limitada — card da aula 07 (ak-inata-diversidade)"),
 (1486867633025, "seção inata: barreiras físicas — card da aula 07 (ak-inata-barreiras)"),
 (1520299391760, "seção inata: PCR e complemento — a cópia NEBLI da aula 31 (1791667093238) está aberta no navegador de Davi; não tocar"),
 (1520301328706, "IFN tipo I reduz síntese proteica — repete sh-1791984890700 (estado antiviral)"),
 (1489970693302, "IFN α/β agem nas células vizinhas — entra a cópia NEBLI da 61 (sh-1791984890453)"),
 (1487117308213, "NK com perforina — entra a cópia NEBLI da 61 (sh-1791984891827)"),
 (1487117295752, "CTL com perforina — entra a cópia NEBLI (sh-1791593462592)"),
 (1487117300306, "CTL com FasL — entra a cópia NEBLI da 45 (sh-1791625430882)"),
 (1487640219508, "opsoninas C3b e IgG — entra a cópia NEBLI da 31 (sh-1791667096988)"),
 (1487640050564, "seção TLR: TLR ativa NF-κB — a cópia NEBLI existente (1791743339611) está em português; o conteúdo entra em au-myd88-trif e ak-ikb"),
 (1487117310594, "IFN α/β ativam NK — entra a cópia NEBLI da 61 (sh-1791984891204)"),
 (1471541613557, "prostaglandinas F vasoconstritoras: farmacologia dos eicosanoides, fora"),
 (1497310326771, "PRR detectam cristais na gota — repete sh-1791743340632 (urato ativa NLRP3)"),
 (1497215299862, "canakinumabe bloqueia IL-1β — repete sh-1792166997617"),
]
FORA_DO_RECORTE = [
 "Recapitulação da aula 07 (lâminas 3–5, 7): seleção, tolerância e apresentação ficam lá.",
 "Lista completa de ligantes de cada TLR e a figura de vias (lâminas 16, 19): só os exemplos clássicos (TLR4/LPS, TLR endossomais, TLR7).",
 "Uso clínico dos interferons (hepatites, Kaposi, esclerose múltipla): farmacologia.",
 "Exossomos e citação de Ehrlich (lâminas 13 e 15): sem fato cobrável.",
 "Imunidade treinada (prova 2025 P2 7.1): não dada nesta aula.",
]
A_, B_, C_, D_, E_, F_ = ("A-prr-celulas", "B-efetores", "C-mediadores", "D-tlr-ligantes", "E-vias", "F-inflamassoma-febre")

CARDS = [
 # ---------- A. PRR e células inatas (lâminas 6–9) ----------
 sh(1791780342851, "verde", A_, "PRR reconhecem PAMPs", 6, "lâminas 6 e 8; provas 2017 P1 1.8 e 3.4, 2015 P1 1.2; card da 38"),
 ak("ak-prr-ligantes", 1520299451730, "V-prova", A_, "LPS, flagelina e ácidos nucleicos virais → PRR", 6, "lâmina 6; prova 2017 P1 3.4 (sensores ativados)"),
 ak("ak-inata-macrofagos", 1486867495023, "A-step", A_, "Macrófagos e monócitos: inata", 6, "seção FirstAid inata; prova 2024 P2 2.1 (elementos da primeira linha)"),
 ak("ak-inata-neutrofilos", 1486867499358, "A-step", A_, "Neutrófilos e DC: inata", 6, "seção FirstAid inata"),
 ak("ak-inata-nk", 1486867503989, "A-step", A_, "NK: inata", 6, "seção FirstAid inata; monitoria (NK reconhece a falta de HLA)"),
 au("au-prr-locais", "<b>Pattern recognition receptors</b> cover every compartment, with TLRs on membranes, NLRs and RLRs in the {{c1::cytoplasm}}, AIM2 in the nucleus",
    "V-pilar", A_, "PRR em todos os compartimentos", 8, "lâmina 8 (tabela de famílias e localização); objetivo 2; transcrição (membrana externa, internas, citoplasma, núcleo)",
    extra="- TLRs sit on the plasma membrane or on endosomes; C-type lectin and scavenger receptors on the surface<br>"
          "- So a microbe is sensed wherever it is: outside, in a vesicle or in the cytosol"),
 sh(1791743340457, "verde", A_, "Tecido necrótico libera DAMPs", 8, "lâmina 8 (DAMP × PAMP); prova 2017 P1 2.5 (infarto e inflamação); card da 37"),
 sh(1791743340159, "azul", A_, "NOD1/2 e RIG-I no citoplasma", 8, "lâminas 8 e 17; card da 37"),
 sh(1791743340332, "rosa", A_, "Dectina-1 reconhece β-glucana", 8, "lâminas 8 e 17 (CLR, fungos); card da 37"),
 ak("ak-tlr-ambas", 1487640013531, "R-detalhe", A_, "TLR em células inatas e adaptativas", 8, "seção FirstAid TLR"),
 au("au-febre-defesa", "Infected lizards kept from warming in the sun die more often, showing that <b>fever</b> is a {{c1::defense}} mechanism",
    "A-aula", A_, "Febre é mecanismo de defesa", 9, "lâmina 9 (febre → imunidade social); transcrição (experimento do lagarto)",
    extra="- Cytokines of the innate response (IL-1, IL-6, TNF, IFN) cause fever, malaise and body aches<br>- Antipyretics treat the symptom, not the cause"),
 ak("ak-barreira-quimica", 1486867649389, "A-step", A_, "Barreiras químicas: lisozima e defensinas", 9, "seção FirstAid inata; monitoria (defensinas das mucosas); prova 2024 P2 2.1"),
 ak("ak-barreira-fisiologica", 1486867644687, "R-detalhe", A_, "Barreiras fisiológicas: temperatura e pH", 9, "seção FirstAid inata"),
 ak("ak-inata-geracoes", 1520299291738, "R-detalhe", A_, "Resistência inata passa entre gerações", 9, "seção FirstAid inata (receptores germinativos)"),
 # ---------- B. Efetores: IFN, citotoxicidade, fagocitose (lâminas 10–12) ----------
 sh(1791984890453, "verde", B_, "IFN α/β agem nas células vizinhas", 10, "lâmina 10 (ação solidária); provas 2025 P3 2.5, 2019 P1 3.2, 2015 P2sub 2.1; card da 61"),
 sh(1791984890700, "azul", B_, "IFN tipo I: estado antiviral", 10, "lâmina 10 e transcrição (bloqueia a replicação nas vizinhas); card da 61"),
 ak("ak-virus-ifn", 1497440851060, "A-step", B_, "Vírus disparam IFN tipo I por sensores citosólicos", 10, "lâmina 10 e transcrição (ácido nucleico liberado → IFN)"),
 sh(1791984890952, "rosa", B_, "IFN tipo I aumenta MHC I", 10, "card da 61"),
 sh(1791984891204, "azul", B_, "IFN α/β ativam NK", 10, "lâminas 10–11; prova 2016 P2 1.1 (resposta inata aos vírus); card da 61"),
 sh(1791984891827, "verde", B_, "NK: perforina e granzima", 11, "lâmina 11 (grânulos citotóxicos); card da 61"),
 sh(1791593462592, "azul", B_, "CTL: perforina e granzima", 11, "lâmina 11; card da 22/45"),
 sh(1791625430882, "azul", B_, "CTL: FasL–Fas", 11, "lâmina 11 (sinalização de membrana FasL-Fas); card da 45"),
 sh(1791780361006, "verde", B_, "Etapas da fagocitose", 12, "lâmina 12; prova 2015 P1sub 1.4; card da 38"),
 sh(1791667096988, "azul", B_, "Opsoninas: C3b e IgG", 12, "lâmina 12 (adesão por opsonização); card da 31"),
 ak("ak-explosao", 1487642714884, "A-aula", B_, "Explosão respiratória destrói o fagocitado", 12, "lâmina 12 (radicais livres de oxigênio); transcrição (consome muito mais O2)"),
 sh(1791743343758, "rosa", B_, "HMP fornece NADPH à NADPH oxidase", 12, "card da 37"),
 # ---------- C. Mediadores (lâminas 13–14) ----------
 au("au-pleiotropia", "<b>Cytokines</b> are called {{c1::pleiotropic}} because each one has many different actions, depending on the target cell's receptors",
    "A-aula", C_, "Citocinas são pleiotrópicas", 13, "lâmina 13 (citocinas: produtos proteicos pleiotrópicos); transcrição",
    extra="- Interleukins (IL-1, IL-2…) signal between leukocytes; CSFs came from hematopoiesis; interferons; chemokines<br>- The name rarely tells the whole function"),
 sh(1791743344682, "azul", C_, "COX converte ácido araquidônico em prostaglandinas", 13, "lâmina 13 (metabólitos do AA); card da 37"),
 sh(1791743345233, "azul", C_, "5-LOX converte ácido araquidônico em leucotrienos", 13, "lâmina 13; card da 37"),
 sh(1791743347558, "rosa", C_, "IL-6 induz proteínas de fase aguda", 14, "lâmina 14 (IL-6); card da 37"),
 ak("ak-tocilizumabe", 1497205557686, "R-detalhe", C_, "Tocilizumabe bloqueia o receptor da IL-6", 14, "transcrição (anti-IL-6 nas formas graves da COVID)"),
 ak("ak-filgrastim", 1489967982654, "R-detalhe", C_, "Filgrastim = G-CSF recombinante", 14, "lâmina 14 e transcrição (G-CSF e GM-CSF são remédios)"),
 ak("ak-gcsf-neutropenia", 1480563913058, "R-detalhe", C_, "G-CSF/GM-CSF na neutropenia", 14, "transcrição (fatores de crescimento usados em transplantes)"),
 # ---------- D. Ligantes dos PRR (lâminas 16–17) ----------
 sh(1791743339358, "verde", D_, "TLR4 + CD14 reconhecem LPS", 16, "lâmina 16 (TLR4: LPS) e transcrição; card da 37"),
 sh(1791743339982, "azul", D_, "TLR de ácidos nucleicos ficam nos endossomos", 16, "lâmina 16 (TLR3/7/8/9 no endolisossomo); card da 37"),
 ak("ak-imiquimode", 1591140454546, "R-detalhe", D_, "Imiquimode ativa TLR7", 16, "lâmina 16 (TLR7: ssRNA); exemplo de remédio com alvo molecular (lâmina 15)"),
 ak("ak-nod2-crohn", 1521771712578, "R-detalhe", D_, "NOD2 e doença de Crohn", 17, "lâmina 17 (NOD2 reconhece MDP bacteriano)"),
 # ---------- E. Vias dos TLR (lâminas 18–19) ----------
 au("au-myd88-trif", "<b>TLR</b> signals through {{c1::MyD88}} lead to NF-κB and inflammatory cytokines, while signals through {{c2::TRIF}} lead to type I interferon",
    "A-aula", E_, "MyD88 × TRIF", 18, "lâminas 18–19; objetivo 3; transcrição (alguns TLR por MyD88, outros por TRIF, e as vias se cruzam)",
    extra="- TRIF acts through IRFs (interferon regulatory factors); MyD88 through NF-κB and AP-1<br>- TLR signals can also drive survival (AKT), apoptosis (caspase-8) and the inflammasome"),
 ak("ak-ikb", 1520299562982, "R-detalhe", E_, "PRR → IκB quinase → NF-κB", 18, "seção FirstAid inata (via do NF-κB)"),
 # ---------- F. Inflamassoma e febre (lâminas 20–22) ----------
 sh(1791743339740, "azul", F_, "Inflamassoma: complexo citoplasmático", 20, "lâmina 20; card da 37"),
 sh(1791743339860, "verde", F_, "Inflamassoma → IL-1β e IL-18", 20, "lâmina 20 (clivagem de IL-1β e IL-18); card da 37"),
 sh(1791780343453, "azul", F_, "NLRP3 + ASC + pró-caspase-1", 20, "lâminas 20–21; card da 38"),
 sh(1791780343873, "rosa", F_, "Caspase-1 e piroptose", 20, "card da 38"),
 sh(1792166997617, "rosa", F_, "Síndromes de febre periódica: canakinumabe", 20, "lâmina 20 (doenças inflamatórias hereditárias); palavras-cruzadas (autoinflamatórias); card da 51"),
 au("au-inflamassoma-sinais", "Releasing <b>IL-1β</b> takes two signals, one inducing pro-IL-1β through NF-κB and one assembling the {{c1::inflammasome}}",
    "A-aula", F_, "Dois sinais para a IL-1β", 21, "lâmina 21 (montagem da plataforma; outros sinais); transcrição (sem o sinal da pró-IL-1β não vai para frente)",
    extra="- The inflammasome activates caspase-1, which cleaves pro-IL-1β and pro-IL-18 into active cytokines"),
 sh(1791743340632, "azul", F_, "Cristais de urato ativam NLRP3", 21, "lâmina 21 (sinais de perigo); card da 37"),
 sh(1791743347261, "verde", F_, "Febre: IL-1, IL-6 e TNF dos macrófagos", 22, "lâmina 9 e 22 (produtos da ativação dos PRR); card da 37"),
 sh(1791743347433, "azul", F_, "IL-1: febre e inflamação aguda", 22, "card da 37"),
 ak("ak-pirogenos", 1471541811425, "A-step", F_, "Pirógenos → IL-1 → hipotálamo → PGE2", 22, "lâmina 9 (febre)"),
 sh(1791743344934, "rosa", F_, "PGE2 medeia dor e febre", 22, "card da 37"),
]

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "receptores, vias e mediadores sem estrutura a reconhecer em imagem; os esquemas das lâminas são desenhos ou tabelas"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM

VERSO = {  # chave: "- linha curta" para nota de acervo sem Extra útil
 "ak-prr-ligantes": "- These shared microbial patterns (PAMPs) are absent from host cells",
 "ak-inata-macrofagos": "- Macrophages are tissue sentinels that phagocytose and release cytokines",
 "ak-inata-neutrofilos": "- Neutrophils are the first cells recruited; dendritic cells link innate to adaptive immunity",
 "ak-inata-nk": "- NK cells kill cells that lose MHC I (missing self), with no prior sensitization",
 "ak-tlr-ambas": "- Mostly on macrophages and dendritic cells, but B cells also express TLRs",
 "ak-barreira-quimica": "- Defensins are antimicrobial peptides made by epithelia and neutrophils",
 "ak-barreira-fisiologica": "- Fever and acidic pH (stomach, skin) hinder microbial growth",
 "ak-inata-geracoes": "- Innate receptors are germline-encoded, so they are inherited, not built in each life",
 "ak-virus-ifn": "- Viral nucleic acids in the cytosol are sensed by RIG-I-like receptors",
 "ak-ifn-nk": "- NK cells then kill virus-infected cells early, before T cells arrive",
 "ak-explosao": "- NADPH oxidase makes superoxide; myeloperoxidase turns H2O2 into bleach (HOCl)",
 "ak-tocilizumabe": "- IL-6 drives fever and acute-phase proteins, so blocking it calms cytokine storms",
 "ak-filgrastim": "- G-CSF stimulates neutrophil production in the marrow",
 "ak-gcsf-neutropenia": "- They shorten neutropenia after chemotherapy or transplant",
 "ak-imiquimod": "",
 "ak-imiquimode": "- TLR7 senses single-stranded RNA in endosomes",
 "ak-nod2-crohn": "- NOD2 senses bacterial muramyl dipeptide in the cytoplasm",
 "ak-ikb": "- IκB kinase degrades IκB, freeing NF-κB to enter the nucleus",
 "ak-pirogenos": "- PGE2 raises the hypothalamic set point; COX inhibitors lower fever",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
IMAGENS_VISTAS = {}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (22 notas novas, 28 cards). Nada a corrigir nos campos NEBLI; observação: o Extra original do AnKing em ak-nod2-crohn diz que NOD2 reconhece LPS (é muramil-dipeptídeo) — original preservado, a apontar no Tab.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Identificar os PRR como sensores da perda de homeostasia (PAMP e DAMP), suas famílias e localizações, as vias dos TLR "
             "(MyD88 → NF-κB; TRIF → IFN tipo I), o inflamassoma (caspase-1, IL-1β), as estratégias efetoras inatas (IFN, citotoxicidade, "
             "fagocitose) e os mediadores (citocinas pleiotrópicas, lipídicos), com a febre como defesa.",
 "centrais": [
   ("PRR", "sh-1791780342851", "ak-prr-ligantes", "au-prr-locais", "sh-1791743340457"),
   ("vias", "au-myd88-trif", "sh-1791743339860", "au-inflamassoma-sinais"),
   ("efetores", "sh-1791984890453", "sh-1791984891827", "sh-1791780361006"),
   ("mediadores", "au-pleiotropia", "sh-1791743347261"),
 ],
 "exemplos": ["LPS e TLR4", "vírus e IFN", "gota e NLRP3", "Crohn e NOD2", "imiquimode", "COVID e anti-IL-6"],
 "outras_aulas": [("inata × adaptativa", "07"), ("inflamação aguda e mediadores", "37/38 (sh)"), ("complemento", "31 (sh)"),
                  ("citotoxicidade CD8", "22/45 (sh)"), ("IFN na infecção viral", "61 (sh)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
