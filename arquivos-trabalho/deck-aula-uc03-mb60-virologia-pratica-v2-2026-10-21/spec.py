# Especificação curada — 64 Virologia prática: métodos de estudo e diagnóstico de vírus (UC03 P3, Microbiologia; 149 lâminas: Ia 1–77, Ib 78–149; sem transcrição, as videoaulas são assíncronas).
# Ciclo básico: princípios dos métodos de estudo e diagnóstico viral (detecção direta e indireta, cultivo, quantificação, sorologia, métodos moleculares, efeito citopático), sem protocolo de bancada.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = "A aula é de métodos (placa de lise, TCID50, hemaglutinação e sua inibição, neutralização, soroconversão e efeito citopático por vírus) que o AnKing não traz; só PCR, blots, ELISA e inclusões estão nas seções; busca nos três caminhos não achou esses cards."
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb60-20261021a"
SHORT = "mb60"
LESSON = "2026-uc03-microbiologia-60-virologia-pratica"
DECK = "NEBLI::UC03::P3::Microbiologia::Virologia prática"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261021-CLAUDE-01 + ANTI-EXEMPLARES §1–16, 21/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (21/10): seções de recurso do AnKing (técnicas de laboratório: PCR, blots e ELISA; busca/secoes); palavra-chave e significado "
         "em AnKing, Referências Externas e NEBLI vivo (busca/semantica.jsonl, uma consulta por conceito). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)



A_, B_, C_, D_, E_, F_ = "A-diagnostico", "B-molecular", "C-cultivo-quantificacao", "D-sorologia", "E-efeito-citopatico", "F-hibridacao"
EXCLUIDOS = []
FORA_DO_RECORTE = [
    "Lâminas 78–89 e 121–149 (versão Ib repete as lâminas 1–77 de cultivo, sorologia e métodos moleculares).",
    "Figuras de livro e de artigos (placas, focos, gel, western blot, imunofluorescência, curvas de PCR em tempo real): ilustram, não ensinam alvo.",
    "Escolha da amostra por tipo de infecção e transporte a 4 °C ou −20 °C (lâminas 6–8): protocolo de bancada, não princípio.",
    "Curva de crescimento em um passo (lâminas 26–28) e kits comerciais (lâminas 75–76): sem texto na lâmina e sem cobrança nas provas.",
    "Southern blot e Northern blot em detalhe, CRISPR, microarray e FISH: são das aulas de biologia molecular; aqui entra só o Western blot e a PCR.",
]

CARDS = [
    # Diagnóstico e métodos (lâminas 3–9)
    au("au-metodos", ORG("<b>Viral diagnosis</b>:<br>- direct: finds the {{c1::virus}}, its antigen or nucleic acid<br>- indirect: finds {{c2::antibodies}}"),
       "V-pilar", A_, "Métodos diretos × indiretos", 3, "lâmina 3 e 79 (estudo de vírus: diretos e indiretos); provas de Micro",
       extra="- Direct: electron microscopy, culture, antigen and nucleic acid tests<br>- Indirect: serology, which shows exposure and immune status"),
    # Cultivo (lâminas 14–38)
    au("au-placa", "In a <b>plaque assay</b> each lysis plaque comes from {{c1::one}} infectious particle and is counted as {{c2::PFU}}",
       "V-pilar", C_, "Ensaio de placas de lise", 21, "lâminas 17–21; transcrição ausente, texto das lâminas (1 partícula gera uma placa)",
       extra="- It needs cells that grow in a monolayer and are lysed by the virus<br>- A semisolid medium keeps the virus from spreading beyond neighboring cells"),
    au("au-tcid50", "<b>TCID50</b> is the dilution that causes {{c1::cytopathic effect}} in half of the cell cultures",
       "A-aula", C_, "Endpoint: TCID50", 37, "lâminas 29–37 (endpoint para vírus que não formam placas); texto das lâminas",
       extra="- LD50 is the dilution at which half of the animals die<br>- It is used for viruses that do not form plaques or foci"),
    # Sorologia (lâminas 39–54)
    au("au-ha", "<b>Hemagglutination</b> titrates the virus, and its {{c1::inhibition}} by antibody identifies the virus {{c2::type}}",
       "A-aula", D_, "Hemaglutinação e inibição da hemaglutinação", 42, "lâminas 41–47; texto das lâminas (ensaio rápido e barato; o título e o tipo de vírus)",
       extra="- The virus agglutinates red blood cells<br>- It is a quick and cheap assay"),
    au("au-soroconversao", "<b>Seroconversion</b> is a rising antibody {{c1::titer}} between the {{c2::acute}} and convalescent sera",
       "V-pilar", D_, "Soroconversão: soro agudo × convalescente", 40, "lâminas 7, 15 e 39–40 (colheita na fase aguda e na convalescença; sorologia a ser confirmada por soroconversão); provas de Micro",
       extra="- A fourfold rise in titer is the usual criterion<br>- Hemagglutination inhibition can be used to compare the two sera"),
    au("au-igm", "<b>IgM</b> against the virus indicates {{c1::recent}} infection, while IgG indicates past exposure or {{c2::memory}}",
       "A-aula", D_, "IgM × IgG na sorologia viral", 40, "lâminas 39–40 (métodos baseados em sorologia); provas de Micro (2024 P3 1.6)",
       extra="- ELISA detects and quantifies specific IgM and IgG in the serum"),
    au("au-neut", "A <b>neutralization</b> test detects antibodies that block the {{c1::infectivity}} of the virus in cell culture",
       "A-aula", D_, "Neutralização de vírus", 48, "lâminas 48–49; texto das lâminas (baseado em anticorpos neutralizantes)",
       extra="- The antibody binds the virus and prevents it from infecting the cells<br>- It indicates protective antibodies"),
    # Efeito citopático (lâminas 90–120)
    au("au-cpe-def", "The <b>cytopathic effect</b> gives only a {{c1::preliminary}} grouping of viruses, not their identification",
       "V-pilar", E_, "Efeito citopático: agrupamento preliminar", 91, "lâminas 31–32 e 91–92; texto das lâminas",
       extra="- It is a change visible under the microscope in cultured cells<br>- It results from changes in the host cell caused by the virus"),
    au("au-cpe-tipos", ORG("<b>Cytopathic effect</b>:<br>- poliovirus: cell {{c1::rounding}} and rapid lysis<br>- adenovirus: {{c2::grape-like}} clusters<br>- measles: {{c3::giant}} syncytia"),
       "A-aula", E_, "Efeito citopático por vírus", 96, "lâminas 96–107 e 120; texto das lâminas e apostila UC3",
       extra="- HSV makes star-shaped syncytia with a nuclear inclusion and clear halo<br>- Vaccinia makes small round syncytia with cytoplasmic inclusions"),
    K(1506298786823, "A-aula", E_, "Paramixovírus: proteína F funde células", 103, "lâmina 103 e 107 (sincícios do sarampo)"),
    K(1506299172244, "A-aula", E_, "Sarampo: células gigantes de Warthin-Finkeldey", 107, "lâmina 107 (sincícios gigantes)"),
    K(1503861947945, "A-aula", E_, "CMV: inclusão nuclear em olho de coruja", 102, "lâmina 102 (corpos de inclusão em glândula salivar com CMV)"),
    K(1516475827100, "A-aula", E_, "Herpesvírus: inclusões nucleares eosinofílicas (Cowdry)", 106, "lâmina 106 (núcleo com corpúsculo de inclusão e halo claro)"),
    K(1506290563519, "A-aula", E_, "Esfregaço de Tzanck: células gigantes de VZV, HSV e CMV", 106, "lâmina 106 (sincícios do herpesvírus)"),
    K(1516475620459, "A-aula", E_, "Raiva: corpos de Negri no citoplasma", 111, "lâmina 111 (corpos de Negri em neurônios)"),
    K(1385335604751, "A-aula", E_, "Coilócitos: halo perinuclear do HPV", 118, "lâmina 118 (epitélio da cérvice infectado por HPV)"),
    # Moleculares (lâminas 55–76)
    K(1468549285757, "A-aula", B_, "Western blot analisa proteína", 67, "lâminas 67–69 (detecção de proteínas virais)"),
    K(1468549288868, "A-aula", B_, "Western blot: sonda é anticorpo marcado", 68, "lâmina 68 (soro do paciente contra proteínas virais)"),
    K(1468549222931, "A-aula", B_, "Eletroforese separa fragmentos pelo tamanho", 67, "lâmina 67 (gel de proteínas virais)"),
    K(1468549213267, "A-aula", B_, "DNA precisa de fragmentação; RNA e proteína não", 67, "lâmina 67 e seção de blots"),
    K(1468549231401, "A-aula", B_, "Nos blots a sonda define o que é detectado", 67, "lâminas 57–58 e 67–68 (sondas)"),
    K(1468549239653, "A-aula", F_, "Southern blot analisa DNA", 57, "lâmina 57–58 (hibridação de ácidos nucleicos)"),
    K(1468549248441, "A-aula", F_, "Northern blot analisa RNA", 57, "lâmina 57–58 (hibridação de ácidos nucleicos)"),
    K(1468549297186, "A-aula", F_, "Southern e Northern: sonda de oligonucleotídeo marcado", 58, "lâmina 58 (hibridação com sonda)"),
    K(1506535107169, "A-aula", D_, "HIV: teste confirmatório por imunoensaio de diferenciação", 69, "lâmina 69 (soroconversão em indivíduo com HIV)"),
    K(1468605422972, "V-pilar", B_, "PCR amplifica um fragmento de DNA", 62, "lâminas 61–62 (reação em cadeia da polimerase)"),
    K(1468605428299, "A-aula", B_, "PCR, 1º passo: calor desnatura as fitas", 61, "lâmina 61 (separação das fitas)"),
    K(1468605437554, "A-aula", B_, "PCR, 2º passo: primers se ligam às fitas", 61, "lâmina 61 (síntese do primer)"),
    K(1468605447110, "A-aula", B_, "PCR, passo final: Taq alonga após cada primer", 61, "lâmina 61 (extensão)"),
    K(1468605460088, "A-aula", B_, "PCR usa dois primers", 61, "lâmina 61 (um primer para cada fita)"),
    K(1468605476084, "A-aula", B_, "O primer da PCR é de DNA", 61, "lâmina 61"),
    K(1468605486456, "A-aula", B_, "O primer da PCR liga ao extremo 3'", 61, "lâmina 61 (5' e 3')"),
    K(1468605494779, "A-aula", B_, "A PCR usa os quatro dNTPs", 61, "lâmina 61 (extensão)"),
    K(1506535130975, "V-pilar", B_, "Carga viral: quantifica o RNA viral no plasma", 66, "lâmina 66 (PCR em tempo real quantifica a carga viral)"),
    K(1468605640090, "V-pilar", D_, "ELISA detecta antígeno ou anticorpo específico", 53, "lâminas 50–54 (ensaios baseados em anticorpos)"),
    K(1468605649044, "A-aula", D_, "ELISA: detecção por anticorpo ligado a enzima", 53, "lâminas 53–54 (reação que gera cor)"),
    K(1520277897542, "A-aula", D_, "ELISA direto detecta antígeno; indireto, anticorpo", 54, "lâmina 54 (detecção de antígenos virais e de anticorpos)"),
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
 "ak1506298786823": "- F protein fuses the membranes, so the virus passes from cell to cell",
 "ak1506299172244": "- Giant cells with 30 to 100 nuclei and cytoplasmic inclusions",
 "ak1503861947945": "- Inclusion body in infected salivary gland cells",
 "ak1516475827100": "- The nucleus shows an eosinophilic inclusion with a clear halo",
 "ak1506290563519": "- Syncytia with star-shaped cytoplasmic bridges",
 "ak1516475620459": "- Rabies: Negri bodies in infected neurons",
 "ak1385335604751": "- The infected cervical epithelium shows koilocytes",
 "ak1468549285757": "- The patient serum detects antibodies against viral proteins separated in the gel (seroconversion in HIV)",
 "ak1468549288868": "- A labeled antibody binds the protein after it is transferred to the membrane",
 "ak1468549222931": "- Proteins and nucleic acids are separated by size before transfer to the membrane",
 "ak1468549213267": "- DNA is cut into fragments first, while RNA and proteins go directly",
 "ak1468549231401": "- Southern uses a DNA probe, Northern an RNA or DNA probe and Western an antibody",
 "ak1468549239653": "- Hybridization detects viral genomes in cells, such as HPV16 in SiHa cells",
 "ak1468549248441": "- Northern blot also studies gene expression",
 "ak1468549297186": "- The probe is complementary to the viral sequence it must find",
 "ak1506535107169": "- Western blot also confirms HIV antibodies, showing the seroconversion",
 "ak1468605422972": "- For RNA viruses, RT-PCR first makes cDNA with reverse transcriptase",
 "ak1468605428299": "- Heat at about 95 °C separates the strands",
 "ak1468605437554": "- Each primer anneals to one strand, flanking the viral sequence",
 "ak1468605447110": "- Taq polymerase is heat stable, so it survives each cycle",
 "ak1468605460088": "- One primer for each strand, at the 3' end of the target",
 "ak1468605476084": "- The primer is a short DNA oligonucleotide complementary to the target",
 "ak1468605486456": "- DNA polymerase adds nucleotides to the 3' end of the primer",
 "ak1468605494779": "- dATP, dCTP, dGTP and dTTP are the building blocks of the new strands",
 "ak1506535130975": "- In real-time PCR, the lower the Ct (cycle threshold), the higher the amount of viral genome in the sample",
 "ak1468605640090": "- A color reaction shows the antigen-antibody complex (influenza rapid tests give the result in about 15 minutes)",
 "ak1468605649044": "- The enzyme converts a substrate into a colored product",
 "ak1520277897542": "- Direct: finds viral antigen in secretions; indirect: finds antibodies in the serum",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
exec((HERE / "exclusoes.py").read_text(encoding="utf-8")) if (HERE / "exclusoes.py").exists() else None

SEM_IMAGEM = "fato ou conjunto sem estrutura a reconhecer; as figuras da aula são fotografias de cultura, géis e esquemas de livro"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
DUPLICACAO = {"au-cpe-tipos": "os cards de sarampo, herpes e CMV dão a inclusão; este compara a morfologia do efeito citopático entre vírus"}
for _k, _v in DUPLICACAO.items():
    _c = next((c for c in CARDS if c["key"] == _k), None)
    if _c:
        _c["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
    "objetivo": "Reconhecer os métodos de estudo e diagnóstico de vírus: o que cada um detecta, para que serve e que limite tem.",
    "centrais": [("métodos", "au-metodos"), ("cultivo", "au-placa"), ("efeito citopático", "au-cpe-def"), ("sorologia", "au-soroconversao"), ("molecular", "ak1468605422972", "ak1506535130975")],
    "exemplos": ["kits comerciais", "curva de crescimento", "escolha da amostra"],
    "outras_aulas": [("PCR e blots em detalhe", "aulas de Biologia Molecular"), ("multiplicação viral", "58 Multiplicação viral e antivirais"), ("patogênese", "59 Patogênese da infecção viral")],
}
_slide = lambda c: int(_re.search(r"\d+", c["evid"]).group())
FAIXAS = [[1, 38], [90, 120], [39, 77]]  # o efeito citopático (lâminas 90–120, da versão Ib) vem logo depois do cultivo e do endpoint
CARDS.sort(key=lambda c: next((i for i, f in enumerate(FAIXAS) if f[0] <= _slide(c) <= f[1]), len(FAIXAS)) * 1000 + _slide(c))
