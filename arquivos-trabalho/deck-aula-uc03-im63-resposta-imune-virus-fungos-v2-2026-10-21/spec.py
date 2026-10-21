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


A_, B_, D_, E_ = "A-principios", "B-defesa-antiviral", "C-evasao-viral", "D-fungos"
EXCLUIDOS = []
FORA_DO_RECORTE = [
    "Repetição das lâminas 42–47 (introdução da parte de fungos é a mesma da parte de vírus), capas e figuras de livro (Figure 11-5, lâminas 36–39).",
    "Vírus e câncer (lâmina 40): é a aula 78 Agentes carcinogênicos biológicos; epidemias de influenza em datas e números (lâmina 29): ilustração.",
    "Paracoccidioidomicose (lâminas 79–81): é o Grand Round 4 (aula 53) e a micologia; aqui fica só o princípio Th1 × Th2.",
    "Imunodeficiências, clínica das micoses e dos vírus, e fármacos: patologia, micologia e farmacologia.",
]

CARDS = [
    au("au-balanca", "The outcome of an <b>infection</b> is the balance between pathogen {{c1::pathogenicity}} and host immune {{c2::response}}",
       "V-pilar", A_, "Infecção: patogenicidade × resposta imune", 2, "lâminas 2 e 42; transcrição (balanço entre o patógeno e a resposta imune)",
       extra="- An exaggerated response can itself damage tissue, as in hepatitis B<br>- Pathogens survive by evading the immune response"),
    K(1487117288751, "A-aula", A_, "Imunidade celular defende contra agentes intracelulares", 6, "lâmina 6 (localização × imunidade); seção Bootcamp de defesa do hospedeiro"),
    K(1461792762468, "A-aula", B_, "Interferons: citocinas liberadas por células infectadas por vírus", 13, "lâmina 13 (inibição da replicação por IFN α/β); seção Bootcamp de defesa"),
    au("au-tlr-virus", "<b>Viral nucleic acids</b> are sensed by {{c1::TLR3}} (dsRNA), {{c2::TLR7 and TLR8}} (ssRNA) and {{c2::TLR9}} (CpG DNA)",
       "V-pilar", B_, "TLRs que reconhecem vírus", 14, "lâmina 14; monitoria P3 de Imuno (TLR3, TLR7/8, TLR9)",
       extra="- Cytosolic RNA sensors, such as RIG-I, and NLRs also detect viruses"),
    K(1497440851060, "A-aula", B_, "Vírus no citosol disparam interferon tipo I por receptores citosólicos", 14, "lâmina 14; seção Bootcamp de defesa"),
    K(1489970693302, "V-pilar", B_, "IFN α/β preparam as células vizinhas", 17, "lâmina 17 (estado antiviral); seção Bootcamp de defesa"),
    K(1520301328706, "A-aula", B_, "IFN tipo I reduz a síntese proteica", 17, "lâmina 17 (ação antiviral do IFN α/β); seção Bootcamp de defesa"),
    K(1461794583601, "R-detalhe", B_, "Interleucinas aumentam a síntese de interferon", 17, "lâmina 17; seção Bootcamp de defesa"),
    K(1497450277629, "R-detalhe", B_, "RNA dupla fita no citosol leva à apoptose via IFN", 17, "lâmina 17; seção Bootcamp de defesa"),
    K(1520301453074, "A-aula", B_, "IFN tipo I aumenta o MHC I da célula", 17, "lâmina 17; seção Bootcamp de defesa"),
    K(1487117304665, "A-aula", B_, "NK: linfócito da imunidade inata", 14, "lâmina 14 (células NK); seção FirstAid de NK"),
    K(1487117308213, "A-aula", B_, "NK induz apoptose por perforina e granzima", 14, "lâmina 14; seção FirstAid de NK"),
    K(1487117314403, "V-pilar", B_, "NK mata células sem MHC I", 14, "lâmina 14 (citotoxicidade para células infectadas); seção FirstAid de NK"),
    K(1487117310594, "A-aula", B_, "IFN α e β ativam as NK", 14, "lâmina 14; seção FirstAid de NK"),
    K(1487117312582, "A-aula", B_, "IL-2 e IL-12 ativam as NK", 19, "lâmina 19 (IL-12); seção FirstAid de NK"),
    K(1487117321802, "R-detalhe", B_, "NK mata por CD16 ligado ao Fc do IgG", 19, "lâmina 19 (ADCC); seção FirstAid de NK"),
    K(1487117328797, "A-aula", B_, "A imunoglobulina da ADCC é IgG", 19, "lâmina 19 (ADCC); seção Bootcamp de defesa"),
    K(1487640158306, "A-aula", B_, "Via alternativa do complemento: ativação espontânea", 15, "lâmina 15 (complemento pela via alternativa)"),
    K(1489970456186, "A-aula", B_, "Quem secreta IFN-γ: NK e Th1", 19, "lâmina 19 (NK produz IFN-γ); seção FirstAid de IFN-γ"),
    K(1489970364081, "A-aula", B_, "IFN-γ ativa macrófagos para matar o que fagocitaram", 19, "lâmina 19; seção FirstAid de IFN-γ"),
    K(1487117293576, "V-pilar", B_, "CD8 T mata células infectadas por apoptose", 21, "lâmina 21 (citotoxicidade por CTL); seção Bootcamp de defesa"),
    K(1487115889320, "A-aula", B_, "MHC I apresenta antígenos endógenos ao CD8", 21, "lâmina 21 (via MHC classe I)"),
    sh(1791629595197, "azul", B_, "Anticorpos neutralizantes bloqueiam a ligação aos receptores", 21, "A-aula: lâmina 21 (neutralização por IgG e IgA); card da aula 22"),
    au("au-evasao-mhc", "<b>Viruses</b> lower MHC I by blocking the {{c1::proteasome}}, {{c2::TAP}} or MHC I export from the {{c2::ER}}",
       "V-pilar", D_, "Escape viral: queda do MHC I", 25, "lâmina 25; monitoria P3 de Imuno (bloqueio do proteassoma e do TAP, retenção no RE)",
       extra="- HSV blocks TAP with ICP47; CMV also lowers MHC I<br>- Low MHC I protects from CD8 cells but exposes the cell to NK cells"),
    K(1503876244084, "A-aula", D_, "CMV inibe a expressão de MHC I", 25, "lâmina 25 (CMV inibe classe I)"),
    K(1503876156644, "A-aula", D_, "CMV bloqueia o MHC I e a morte pelo CD8", 25, "lâmina 25"),
    au("au-evasao-citocinas", "<b>EBV</b> makes a homolog of {{c1::IL-10}}, and some viruses secrete soluble {{c2::decoy}} receptors for cytokines",
       "A-aula", D_, "Escape viral: homólogos de citocinas e receptores", 27, "lâmina 27; monitoria P3 de Imuno (homólogo de IL-10 do EBV)",
       extra="- IL-10 lowers the function of lymphocytes, dendritic cells and macrophages"),
    K(1489970615786, "A-aula", D_, "IL-10 atenua a resposta inflamatória", 27, "lâmina 27 (homólogo de IL-10)"),
    K(1506805786448, "A-aula", D_, "HIV infecta linfócitos T CD4, macrófagos e células dendríticas", 28, "lâmina 28 (imunossupressão por destruição de CD4)"),
    K(1516321589458, "A-aula", D_, "Variação antigênica do influenza: HA e NA", 29, "lâminas 29–34; seção de influenza"),
    K(1516322271299, "A-aula", D_, "Variação antigênica: deriva ou virada", 30, "lâmina 30 (mecanismos de variação)"),
    K(1516322855117, "A-aula", D_, "Deriva: mutações pontuais em HA ou NA", 31, "lâmina 31 (escape por mutações)"),
    K(1516323022237, "A-aula", D_, "Deriva: epidemias", 31, "lâmina 31"),
    K(1516323064948, "A-aula", D_, "Virada: reassortment de HA e NA entre espécies", 29, "lâmina 29 (troca de material genético com vírus de outras espécies)"),
    K(1516323168130, "A-aula", D_, "Virada: pandemias", 29, "lâmina 29"),
    K(1520087988222, "R-detalhe", D_, "Dengue: quatro sorotipos", 31, "lâmina 31 (dengue e sorotipos)"),
    K(1520088551261, "R-detalhe", D_, "Segunda infecção por dengue: quadro mais grave", 31, "lâmina 31 (anticorpos prévios não protegem)"),
    au("au-fungos-tipos", ORG("<b>Fungi</b>:<br>- opportunistic: {{c1::Aspergillus}}, {{c1::Cryptococcus}}, {{c1::Pneumocystis}}<br>- primary: {{c2::Histoplasma}}, {{c2::Blastomyces}}, {{c2::Paracoccidioides}}"),
       "A-aula", E_, "Fungos oportunistas × primários", 55, "lâmina 55; apostila guia de Imuno (oportunistas)",
       extra="- Opportunists cause disease in immunosuppressed people; primary fungi also in people with no apparent immunodeficiency<br>- Coccidioides is also primary"),
    au("au-fungos-pamps", "The <b>fungal wall</b> is rich in sugars, such as {{c1::β-glucan}} and mannans, that act as {{c2::PAMPs}}",
       "V-pilar", E_, "Parede do fungo: açúcares como PAMPs", 58, "lâmina 58 (os fungos são doces); apostila guia de Imuno (lectinas tipo C)",
       extra="- C-type lectin receptors recognize them, with help from TLRs"),
    sh(1791743340332, "azul", E_, "β-glucana do fungo é reconhecida pela Dectin-1", 59, "A-aula: lâmina 59 (reconhecimento de estruturas dos fungos); card de outra aula"),
    sh(1791743344060, "azul", E_, "NETs: redes de cromatina com proteínas antimicrobianas", 62, "A-aula: lâmina 62 (NETs contra fungos); card de outra aula"),
    K(1520715849479, "A-aula", E_, "Inflamassoma aumenta IL-1β e IL-18", 63, "lâmina 63 (fungos ativam o inflamassoma NLRP3)"),
    au("au-fungos-il1", "<b>Fungi</b> activate NLRP3, and IL-1β drives {{c1::Th17}} while IL-18 drives {{c2::Th1}}",
       "A-aula", E_, "Inflamassoma: IL-1β para Th17 e IL-18 para Th1", 63, "lâmina 63; apostila guia de Imuno (inflamassoma estimula Th17 via IL-1β e Th1 via IL-18)",
       extra="- Innate recognition dictates the pattern of adaptive immunity"),
    au("au-fungos-protecao", "<b>Th1</b> and Th17 responses protect against fungi, whereas {{c1::Th2}} and {{c2::Treg}} responses make the disease worse",
       "V-pilar", E_, "Th1 e Th17 protegem; Th2 e Treg pioram", 66, "lâminas 66–67 e 73–74; apostila guia de Imuno",
       extra="- TLR2 signaling favors Treg, which is deleterious in fungal infection<br>- Exception: in Pneumocystis a Th2 response may protect"),
    K(1520300296240, "A-aula", E_, "Th17 recruta neutrófilos", 71, "lâmina 71 (a imunidade Th17 é protetora)"),
    K(1520300013308, "A-aula", E_, "Th17 secreta IL-17, IL-21 e IL-22", 71, "lâmina 71"),
    K(1520716108281, "A-aula", E_, "Th1 ativa macrófagos M1", 69, "lâmina 69 (Th1 e M1 × Th2 e M2)"),
    K(1520717070355, "A-aula", E_, "Th2 ativa macrófagos M2", 69, "lâmina 69"),
    K(1487643792482, "A-aula", E_, "Granuloma: IL-12 dos macrófagos", 70, "lâmina 70 (granulomas de pulmão com fungo)"),
    K(1487643795892, "A-aula", E_, "Granuloma: IFN-γ do Th1 gera histiócitos epitelioides", 70, "lâmina 70"),
    K(1503254160003, "A-aula", E_, "Sem TNF-α não há granuloma e a infecção reativa", 70, "lâmina 70 (importância do Th1 e do TNF-α)"),
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
 "ak1461792762468": "- They signal neighboring cells to resist viral replication",
 "ak1520301328706": "- Less protein synthesis in the cell means less viral protein",
 "ak1461794583601": "- Interleukins such as IL-1 and TNF amplify the interferon response",
 "ak1497450277629": "- Enzymes such as PKR and RNase L stop translation and trigger apoptosis",
 "ak1520300013308": "- IL-17 also keeps the epithelium intact",
 "ak1503876156644": "- Without MHC I on the surface, CD8 cells cannot recognize the infected cell",
 "ak1506805786448": "- Losing CD4 cells removes the help that CD8 cells and B cells need",
 "ak1516323022237": "- Small mutations only partly reduce immunity from earlier infections",
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
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    _c = next((c for c in CARDS if c["key"] == _k), None)
    if _c:
        _c["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
    "objetivo": "Explicar como o sistema imune reconhece e controla vírus e fungos (inata e adaptativa) e como esses patógenos evadem a resposta.",
    "centrais": [("princípio", "au-balanca"), ("defesa antiviral", "au-tlr-virus"), ("evasão", "au-evasao-mhc"), ("fungos", "au-fungos-pamps", "au-fungos-protecao")],
    "exemplos": ["epidemias de influenza em datas", "paracoccidioidomicose", "vírus e câncer"],
    "outras_aulas": [("hipersensibilidade", "64 Reações de hipersensibilidade"), ("vírus e câncer", "78 Agentes carcinogênicos biológicos"),
                     ("paracoccidioidomicose", "53 Grand Round 4"), ("interferon, NK e complemento", "08 e 31 (sh)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
