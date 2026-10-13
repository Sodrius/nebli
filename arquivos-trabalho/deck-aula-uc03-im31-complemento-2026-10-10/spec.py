# Especificação curada — Sistema complemento (UC03 P2, Imunologia, aula 31; 60 lâminas). Gerada a partir de inventario.py (escrito antes).
# Fontes: lâminas, transcrição da turma (Aula 06), bibliografia da aula, provas (imuno-06: 2025 P2 1.7, 6.1–6.2; 2024 P3 3.1; 2019…), monitoria P2 aula 7.
# Vídeos dispensados (F-20261010-CLAUDE-06). Nomenclatura da aula: C4b2a (AnKing usa C4b2b; mantida a da aula, nota no verso).
# Notas da Ativação de células B (im49) que tratam de complemento ficam lá e são associadas aqui (F-04).
RUN_ID = "uc03-im31-20261010a"
SHORT = "im31"
LESSON = "2026-uc03-imunologia-31-sistema-complemento"
DECK = "NEBLI::UC03::P2::Imunologia::Sistema complemento"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-06) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por seções FirstAid/Bootcamp/B&B de complemento (busca/tags-secao.txt, 62 notas) e texto livre em AnKing e Referências "
         "Externas (busca/anking.txt), 10/10: ")
EXCLUIDOS = [
 (1487640184312, "C3 convertase 'C4b2b': nomenclatura diferente da aula (C4b2a); coberto pelo autoral convertase-classica"),
 (1487640197206, "C5 convertase 'C4b2b3b': idem; coberto por c5-convertase-classica"),
 (1487640175721, "lectina começa com 'C1-like complex': redundante com mbl-masp"),
 (1487640207727, "MAC = C5b-C9: repete o card do MAC (1487640204292)"),
 (1478994993913, "ausência de GPI e lise: repete o card de GPI/DAF/CD59"),
 (1478995078338, "eculizumabe na HPN: farmacologia, fora da aula"),
 (1474686417807, "IECA contraindicado no angioedema hereditário: farmacologia, fora da aula"),
 (1475376514149, "complemento baixo na GNPE: aula de patologia renal"),
 (1517365303958, "morte por edema de via aérea no AEH: clínica lateral"),
]
FORA_DO_RECORTE = ["COVID-19 e rejeição de transplante (lâminas 2/32): só citados", "PNH além do mecanismo (sacarose, citometria, trombose)",
                   "Degeneração macular: citada na lâmina 55", "Sinalização intracelular do co-receptor de B (Vav, PI3K…), lâmina 43"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


COMP = [1487640180743, 1487640144801]
FUN = [1487640219508, 1487640139590]
DEF = [1487727820979, 1501968263352]
A_, B_, C_, D_, E_, F_, G_, H_ = ("A-visao-geral", "B-via-classica", "C-via-alternativa", "D-via-lectinas", "E-mac", "F-funcoes", "G-regulacao", "H-deficiencias")
CARDS = [
 # ---------- A. Visão geral (lâminas 2–7) ----------
 ak("inata", 1520299391760, {1: V}, A_, "Complemento é imunidade inata", 2, "Verde: HY 1."),
 ak("figado", 1487640142103, {1: Z}, A_, "Síntese hepática", 3, "Azul: lâmina 3."),
 au("cascata", "Complement proteins circulate as inactive {{c1::zymogens}}, switched on in a cascade where each enzyme cleaves the next", {1: V}, A_,
    "Cascata proteolítica", "3, 6; transcrição; monitoria", "central", "sem card do princípio de cascata.", COMP, "Verde: lógica da aula.",
    extra="- It amplifies the signal, so it must be tightly regulated"),
 au("frag-a-b", "Cleaving a complement protein yields a small {{c1::'a'}} fragment that diffuses away and a large {{c2::'b'}} fragment that binds surfaces", {1: V, 2: V}, A_,
    "Fragmentos a e b", "6; transcrição", "central", "sem card da regra a/b.", COMP, "Verde: chave para ler toda a cascata.",
    extra="- 'b' fragments opsonize and build convertases; 'a' fragments drive inflammation<br>- C2 is the exception here: the bound piece is called C2a"),
 au("tres-fases", "Complement activation runs through recognition, an enzymatic phase that builds convertases, and a {{c1::destructive}} phase", {1: R}, A_,
    "Três fases", "4", "lateral", "sem card.", COMP, "Rosa: esquema da lâmina 4."),
 # ---------- B. Via clássica (lâminas 8–20) ----------
 ak("classica", 1487640144801, {1: V, 2: V}, B_, "Via clássica: IgG e IgM", 9, "Verdes: HY 2."),
 sh(1791629595872, "verde", B_, "Uma IgM basta; IgG precisa de duas", 11, "Nota viva da Ativação de células B; lâminas 9–11."),
 sh(1791629595622, "azul", B_, "IgM ligada expõe o sítio de C1q", 9, "Nota viva da Ativação de células B."),
 sh(1791629595747, "azul", B_, "IgM e IgG fixam complemento", 9, "Nota viva da Ativação de células B."),
 ak("comeca-c1", 1487640151914, {1: Z}, B_, "Via clássica começa em C1", 10, "Azul: lâmina 10."),
 au("c1qrs", "After C1q binds antibody, its partners C1r and {{c1::C1s}} become proteases that cleave C4 and C2", {1: Z}, B_,
    "Complexo C1qr2s2", "11; transcrição", "central", "sem card.", COMP, "Azul: lâmina 11."),
 au("c4-primeiro", "Activated C1 cleaves {{c1::C4}} first and C2 second", {1: Z}, B_,
    "Ordem C4 antes de C2", "12–20; transcrição", "central", "sem card.", COMP, "Azul: ordem da cascata.", extra="- C4b binds the surface and captures C2"),
 au("convertase-classica", "The C3 convertase of the classical and lectin pathways is {{c1::C4b2a}}", {1: V}, B_,
    "C3 convertase clássica", "20; transcrição; monitoria", "central", "AnKing usa C4b2b.", COMP, "Verde: lâmina-resumo 20.",
    extra="- Newer texts call it C4b2b, naming the larger C2 fragment 'b'"),
 au("c5-convertase-classica", "Adding C3b to C4b2a forms {{c1::C4b2a3b}}, the classical C5 convertase", {1: Z}, B_,
    "C5 convertase clássica", "20; transcrição; monitoria", "central", "AnKing usa C4b2b3b.", COMP, "Azul: passo seguinte."),
 # ---------- C. Via alternativa (lâminas 21–23) ----------
 ak("alternativa", 1487640158306, {1: V}, C_, "Via alternativa espontânea", 21, "Verde: lâmina 21."),
 ak("comeca-c3", 1487640163185, {1: Z}, C_, "Via alternativa começa em C3", 22, "Azul."),
 au("ativadores-alt", "Besides LPS and teichoic acid, snake and bee {{c1::venoms}} can trigger the alternative pathway", {1: R}, C_,
    "Ativadores da via alternativa", "21", "lateral", "sem card.", COMP, "Rosa: lista da lâmina 21."),
 au("tioester", "C3 is constantly hydrolyzed at its internal {{c1::thioester}} bond, keeping the alternative pathway ticking over", {1: Z}, C_,
    "Hidrólise espontânea de C3", "22, 60; transcrição", "central", "sem card.", COMP, "Azul: lâmina 22.",
    extra="- Without a nearby surface, the hydrolyzed C3 is quickly inactivated"),
 au("fator-d", "In the alternative pathway, factor {{c1::D}} cleaves factor B bound to C3, leaving Bb in the convertase", {1: V}, C_,
    "Fatores B e D", "22; transcrição; monitoria", "central", "sem card.", COMP, "Verde: lâmina 22.", extra="- Ba diffuses away"),
 ak("c3bbb", 1487640188409, {1: V}, C_, "C3 convertase alternativa C3bBb", 22, "Verde: convertase central da via."),
 au("properdina", "{{c1::Properdin}} stabilizes the alternative C3 convertase on microbial surfaces", {1: V}, C_,
    "Properdina", "23; transcrição; prova 2025", "prova", "sem card.", COMP, "Verde: prova 2025 (AH50).",
    extra="- The only complement protein that boosts the cascade"),
 au("alca-positiva", "Each alternative C3 convertase makes C3b that builds more convertase, an amplification {{c1::loop}}", {1: V}, C_,
    "Alça de amplificação", "23; transcrição", "central", "sem card.", COMP, "Verde: explica consumo de C3 sem regulação.",
    extra="- Unchecked, it exhausts plasma C3"),
 ak("c3bbb3b", 1487640200798, {1: Z}, C_, "C5 convertase alternativa", 23, "Azul."),
 # ---------- E. MAC (lâminas 24–27) ----------
 ak("todas-c3", 1487640180743, {1: V}, E_, "Todas as vias geram C3 convertase", 24, "Verde: ponto de convergência."),
 au("c3-central", "{{c1::C3}} is the central, most abundant complement protein, where all three pathways converge", {1: V}, E_,
    "C3 central", "24, 60; transcrição; monitoria", "central", "AnKing diz só que a via alternativa começa em C3.", COMP, "Verde: monitoria ('C3 seria a pior deficiência').",
    duplicacao_ok="ganho: C3 como ponto de convergência e abundância; comeca-c3 é o início da via alternativa"),
 ak("todas-c5", 1487640191924, {1: V}, E_, "Todas as vias geram C5 convertase", 24, "Verde."),
 ak("mac", 1487640204292, {1: V}, E_, "MAC = C5b + C6–C9", 24, "Verde: HY 2."),
 au("mac-lise", "The membrane attack complex kills by forming a pore that causes {{c1::osmotic}} lysis", {1: V}, E_,
    "Como o MAC mata", "25–27, 34; transcrição", "central", "AnKing nomeia o MAC sem o mecanismo.", COMP, "Verde: lâmina 34.",
    extra="- Many C9 molecules polymerize into the pore"),
 # ---------- D. Via das lectinas (lâminas 28–30) ----------
 ak("lectinas", 1487640169311, {1: V, 2: V}, D_, "Via das lectinas: manose", 28, "Verdes: terceira via."),
 au("mbl-masp", "MBL bound to microbial mannose activates {{c1::MASP}}-1 and MASP-2, which cleave C4 and C2", {1: Z}, D_,
    "MBL e MASPs", "28–30; transcrição", "central", "sem card das MASPs.", COMP, "Azul: lâminas 28–29.",
    extra="- MBL resembles C1q; from C4b2a on the pathway equals the classical one"),
 # ---------- F. Funções (lâminas 31–46) ----------
 ak("opsoninas", 1487640219508, {1: V, 2: V}, F_, "C3b e IgG opsoninas", 33, "Verde: função principal."),
 au("opsoninas-outras", "Besides C3b, complement opsonins include iC3b, C4b, C1q and {{c1::MBL}}", {1: Z}, F_,
    "Outras opsoninas", "33; transcrição", "central", "sem card.", FUN, "Azul: tabela da lâmina 33.",
    duplicacao_ok="ganho: MBL como opsonina; lectinas cobra a manose"),
 ak("anafilatoxinas", 1487640139590, {1: V}, F_, "C3a, C4a, C5a anafilatoxinas", 40, "Verde: lâminas 40–42."),
 au("anafilatoxina-acoes", "Anaphylatoxins cause mast cell {{c1::degranulation}}, vasodilation and increased vascular permeability", {1: V}, F_,
    "O que as anafilatoxinas fazem", "40–42, 45; transcrição", "central", "AnKing nomeia, sem os efeitos.", FUN, "Verde: lâminas 40–42."),
 au("c5a", "C5a is a more potent anaphylatoxin and {{c1::chemotactic}} factor than C3a", {1: Z}, F_,
    "C5a × C3a", "40, 44; monitoria", "central", "sem card.", FUN, "Azul: monitoria.", extra="- C5a binds C5aR on neutrophils and mast cells"),
 ak("lps", 1500572318680, {1: Z, 2: Z}, F_, "LPS ativa complemento", 21, "Azul: via alternativa por produtos microbianos."),
 ak("imunocomplexos", 1487640222923, {1: V}, F_, "C3b remove imunocomplexos", 38, "Verde: lâmina 38."),
 au("cr1-hemacia", "Erythrocyte {{c1::CR1}} carries C3b-coated immune complexes to the liver and spleen for removal", {1: V}, F_,
    "CR1 nas hemácias", "38, 44; transcrição; monitoria", "central", "sem card.", FUN, "Verde: lâmina 38.",
    extra="- Small complexes are cleared; large ones deposit in kidney, lung and joints"),
 au("apoptoticos", "{{c1::C1q}}, iC3b and C4b tag apoptotic bodies for removal by macrophages", {1: V}, F_,
    "Remoção de corpos apoptóticos", "37; transcrição", "central", "sem card.", FUN, "Verde: lâmina 37 e base do lúpus.",
    extra="- Failure to clear them exposes self antigens (lupus)", duplicacao_ok="ganho: C1q na remoção de corpos apoptóticos; a nota da im49 trata de C1q na IgM"),
 au("ic3b-cr3", "{{c1::iC3b}} is recognized by CR3 and CR4 on phagocytes", {1: Z}, F_,
    "iC3b e CR3/CR4", "36, 44; transcrição", "central", "sem card.", FUN, "Azul: tabela da lâmina 44."),
 sh(1791629591396, "azul", F_, "CR2 (CD21) recebe C3d", 43, "Nota viva da Ativação de células B."),
 sh(1791629594223, "azul", F_, "FDC retém antígeno", 43, "Nota viva da Ativação de células B."),
 au("coestimulo-b", "C3d on an antigen binding CR2 gives B cells a {{c1::co-stimulatory}} signal that lowers their activation threshold", {1: Z}, F_,
    "Complemento como co-estímulo de B", "43; transcrição; monitoria", "central", "AnKing não liga C3d ao limiar.", FUN, "Azul: lâmina 43.",
    extra="- CR2 pairs with CD19 and CD81 in the B-cell co-receptor"),
 # ---------- G. Regulação (lâminas 47–53) ----------
 au("c1-inibidor", "{{c1::C1 inhibitor}} shuts down the classical pathway at its start by inactivating C1r and C1s", {1: V}, G_,
    "Inibidor de C1", "48; transcrição; monitoria", "central", "AnKing trata C1-INH só no angioedema.", DEF, "Verde: lâmina 48.",
    extra="- It also inhibits kallikrein, which makes bradykinin"),
 au("carboxipeptidase", "Plasma carboxypeptidase {{c1::N}} inactivates the anaphylatoxins C3a and C4a", {1: R}, G_,
    "Carboxipeptidase N", "49", "lateral", "sem card.", FUN, "Rosa: figura da lâmina 49."),
 ak("daf", 1478986720423, {1: V, 2: V}, G_, "DAF inibe C3 convertase", 49, "Verde: regulador de membrana."),
 au("fator-h", "Factor {{c1::H}} binds C3b, blocks factor B and lets factor I cleave C3b", {1: V}, G_,
    "Fator H", "51; transcrição; prova 2025", "prova", "sem card.", DEF, "Verde: prova 2025 (SHU atípica)."),
 au("fator-i", "Factor {{c1::I}} cleaves C3b into iC3b and then C3c and C3dg", {1: Z}, G_,
    "Fator I", "52; transcrição", "central", "sem card.", DEF, "Azul: lâmina 52.", extra="- It also cleaves C4b into C4c and C4d"),
 au("cd59", "{{c1::CD59}} on host cells blocks assembly of the membrane attack complex", {1: V}, G_,
    "CD59", "53; transcrição", "central", "AnKing só cita CD59 na HPN.", DEF, "Verde: lâmina 53."),
 ak("gpi", 1478994988572, {1: V}, G_, "DAF e CD59 presos por GPI", 53, "Verde: HY 2; mecanismo da HPN."),
 # ---------- H. Deficiências (lâminas 54–59; provas) ----------
 ak("precoces-les", 1487727820979, {1: V}, H_, "Deficiências precoces → LES", 56, "Verde: lâmina 56; prova 2024 P3."),
 ak("terminal-neisseria", 1501968263352, {1: V}, H_, "Deficiência terminal → Neisseria", 59, "Verde: HY 1."),
 au("c3-def", "C3 deficiency causes recurrent {{c1::pyogenic}} infections with encapsulated bacteria", {1: V}, H_,
    "Deficiência de C3", "54–55; transcrição", "central", "sem card.", DEF, "Verde: lâmina 54.", extra="- Opsonization fails in every pathway"),
 au("alternativa-def", "Factor D or properdin deficiency predisposes to infections by {{c1::encapsulated}} bacteria such as Neisseria", {1: Z}, H_,
    "Deficiências da via alternativa", "55; prova 2025 P2 6.2", "prova", "sem card.", DEF, "Azul: prova 2025.",
    extra="- Too little early C3b deposition on the bacteria"),
 au("fator-h-shu", "Factor H or I deficiency lets the alternative pathway run unchecked, causing atypical {{c1::hemolytic uremic syndrome}}", {1: V}, H_,
    "Fator H/I e SHU atípica", "55; prova 2025 P2 6.1", "prova", "zero resultado para SHU atípica.", DEF, "Verde: prova 2025.",
    extra="- Low C3 with normal C4 signals alternative-pathway consumption"),
 au("ch50-ah50", "A normal CH50 with undetectable AH50 points to a defect in the {{c1::alternative}} pathway", {1: V}, H_,
    "Ler CH50 e AH50", "55; prova 2025 P2 1.7", "prova", "AnKing só tem CH50 baixo no LES.", DEF, "Verde: prova 2025.",
    extra="- CH50 tests the classical pathway; AH50 the alternative", duplicacao_ok="ganho: leitura dos exames da prova; alternativa é a definição da via"),
 ak("ch50-les", 1487815366607, {1: Z}, H_, "CH50 baixo no LES", 56, "Azul."),
 ak("aeh", 1487727789545, {1: V, 2: V}, H_, "Deficiência de C1-INH → angioedema hereditário", 57, "Verde: lâmina 57; fotos clínicas retiradas (F-03).",
    extra="<div>- C1 inhibitor (AKA C1-esterase inhibitor) normally <u>inhibits kallikrein</u>, which is responsible for conversion of HMWK to bradykinin</div><br><div>- <b>Deficiency</b> leads to <u>high levels</u> of <b>serum bradykinin</b> → episodes of <b>swelling</b> and <b>edema</b></div>"),
 ak("aeh-bradicinina", 1517068230955, {1: Z}, H_, "Bradicinina no AEH", 57, "Azul: mecanismo do edema."),
 ak("aeh-c4", 1487727803414, {1: Z}, H_, "C4 baixo no AEH", 57, "Azul."),
 au("mbl-def", "MBL deficiency resembles classical-pathway deficiency, with infections and {{c1::lupus}}-like disease", {1: R}, H_,
    "Deficiência de MBL", "58", "lateral", "sem card.", DEF, "Rosa: lâmina 58."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
 'todas-c3': '- Classical/lectin: C4b2a; alternative: C3bBb',
 'c1qrs': '- C1 = C1q + 2 C1r + 2 C1s',
 'c5-convertase-classica': '- It cleaves C5 into C5a and C5b',
 'c3-central': '- Its loss would cripple every pathway',
 'opsoninas-outras': '- C3b and iC3b are read by CR1 and CR3/CR4; C1q and MBL by their own receptors',
 'anafilatoxina-acoes': '- They also recruit neutrophils',
 'inata': '- Complement also links to adaptive immunity through B cells and dendritic cells',
 'figado': '- Monocytes, endothelium and dendritic cells also make some components',
 'comeca-c1': '- C1 = C1q + 2 C1r + 2 C1s',
 'alternativa': '- No antibody is needed',
 'c3bbb': '- Stabilized by properdin',
 'c3bbb3b': '- Cleaves C5 into C5a and C5b',
 'todas-c5': '- C5b starts the membrane attack complex',
 'mac': '- C9 polymerizes into the pore',
 'lectinas': '- MBL binds mannose and N-acetylglucosamine',
 'anafilatoxinas': '- Named for their role in anaphylactic shock',
 'imunocomplexos': '- C3b-coated complexes bind CR1',
 'gpi': '- Their absence causes paroxysmal nocturnal hemoglobinuria',
 'precoces-les': '- Immune complexes and apoptotic bodies are not cleared',
 'terminal-neisseria': '- Neisseria\'s thin wall is vulnerable to the MAC',
 'ch50-les': '- Complement is consumed by immune complexes',
 'aeh': '- Swelling of lips, eyes and gut without urticaria',
 'aeh-c4': '- Uncontrolled C1 keeps cleaving C4',
 'aeh-bradicinina': '- C1-INH normally blocks kallikrein',
 'tres-fases': '- Recognition differs between pathways; the MAC at the end is shared',
 'mbl-def': '- MBL behaves like C1q',
 'ativadores-alt': '- Kallikrein and clotting enzymes can too',
 'fator-h': '- It also protects host cells from the alternative pathway',
 'cd59': '- It explains why host cells escape lysis',
 'ic3b-cr3': '- CR3 = CD11b/CD18; CR4 = CD11c/CD18',
 'c4-primeiro': '',
 'carboxipeptidase': '- It removes their C-terminal arginine',
}
VERSO = {k: v for k, v in VERSO.items() if v}
DUPLICACAO = {}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
