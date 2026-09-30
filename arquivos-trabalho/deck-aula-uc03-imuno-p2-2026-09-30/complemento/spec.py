# Sistema complemento (UC03 P2, Imunologia, conteúdo 31, aula 08/09). Refeito do zero em 30/09 a pedido de Davi
# ("deletei imuno da p2 ... gerasse o deck novamente, seguindo o padrão"). Só cards; inglês; irmãos pertinentes; provas UC03.
# Fontes: slides "Sistema complemento - slides" (Drive 1DOzPt5O51Zf5lpubkKKiQkEQlVWsGxHn, mod. 07/09) + 26 questões IM 2015–2025
# (índice referencias-externas/uc03) + AnKing v12 (FA Imunologia 04_Complement / 05_Complement_disorders, lidos por inteiro).
RUN_ID = "uc03-imuno31-20260930a"
SHORT = "imuno31"
LESSON = "2026-uc03-imunologia-31-sistema-complemento"
DECK = "NEBLI::UC03::P2::Imunologia::Sistema complemento"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20260930-CLAUDE-14) + EXECUCAO-DECK-AULA, 30/09/2026"
AUTHOR = "uc03"
MEDIA = {}
INFL = "NEBLI::2026-uc03-imunologia-37-inflamacao-inicio-resolucao"

def ak(key, src, flags, bloco, alvo, evid, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=evid, uso=kw.pop("uso", "Imunologia; Step 1."), motivo=motivo, **kw)

def au(key, flags, bloco, text, extra, alvo, evid, motivo, busca, **kw):
    return dict(key=key, kind="autoral", flags=flags, bloco=bloco, text=text, extra=extra, alvo=alvo, evid=evid, uso=kw.pop("uso", "Imunologia; provas UC03."), motivo=motivo, busca=busca, **kw)

NOMEN = 'In the lecture this convertase is written C4b2a (older naming); it is the same enzyme.<br><br>'

CARDS = [
 # ---------- VISÃO GERAL ----------
 ak("figado", 1487640142103, {1: 4}, "A-geral", "Complemento é sintetizado no fígado", "Slide 3 (produção: fígado e outras células)", "Azul."),
 ak("inato-crp-complemento", 1520299391760, {1: 4}, "A-geral", "Complemento e PCR são imunidade inata", "Slides 1–2 (reconhecimento inato)", "Azul."),
 au("fragmentos-a-b", {1: 4, 2: 3}, "A-geral",
    'When a complement protein is cleaved, the smaller {{c1::"a"}} fragment diffuses away as a mediator, while the larger {{c2::"b"}} fragment binds covalently to the activating surface',
    'This is the logic of the whole cascade: "b" fragments stay on the microbe and build the next enzyme (convertases) or tag it for phagocytosis (C3b); "a" fragments (C3a, C4a, C5a) leave and cause inflammation. C2 is the historical exception, where C2a is the larger piece.',
    "Fragmento a solúvel × b que gruda", "Slides 6, 13–15 ('solúvel' × 'Gruda!')", "c2 verde; c1 azul.",
    "AnKing só tem convertases por nome; princípio a/b ausente; lacuna."),
 # ---------- VIAS ----------
 ak("classica-igg-igm", 1487640144801, {1: 3, 2: 3}, "B-vias", "Via clássica: IgG e IgM", "Slides 7–10", "Verde."),
 ak("classica-c1", 1487640151914, {1: 3}, "B-vias", "Via clássica começa em C1", "Slides 9–12", "Verde."),
 au("c1q-igm-igg", {1: 4, 2: 3}, "B-vias",
    'C1q must bind at least {{c1::two}} IgG Fc regions close together, but a single antigen-bound {{c2::IgM pentamer}} is enough, so IgM is the most efficient activator of the classical pathway',
    'C1q binds the CH2 domain of IgG and the CH3 domain of IgM. Once C1q is anchored, C1r activates C1s, which cleaves C4 and C2.',
    "C1q exige 2 IgG ou 1 IgM", "Slides 8–10 (IgG CH2 × IgM CH3; '2 anticorpos IgG')", "c2 verde; c1 azul.",
    "AnKing: via clássica por IgG/IgM sem a diferença quantitativa; lacuna."),
 au("c1r-c1s", {1: 4, 2: 4}, "B-vias",
    'After C1q binds antibody, {{c1::C1r}} activates {{c2::C1s}}, which cleaves C4 and C2 to assemble the classical C3 convertase',
    'C1 = C1q + 2 C1r + 2 C1s. C1-inhibitor (C1-INH) shuts this step off by binding C1r and C1s.',
    "C1r ativa C1s", "Slides 10–13", "Azul.", "AnKing só 'começa em C1'; lacuna."),
 ak("alternativa-espontanea", 1487640158306, {1: 3}, "B-vias", "Via alternativa: espontânea ou produtos microbianos", "Slides 21–22", "Verde."),
 ak("alternativa-c3", 1487640163185, {1: 4}, "B-vias", "Via alternativa começa em C3", "Slide 22", "Azul."),
 au("tickover-b-d-properdina", {1: 3, 2: 4, 3: 4}, "B-vias",
    'In the alternative pathway, C3 undergoes spontaneous {{c1::hydrolysis}} ("tickover") and binds factor B; {{c2::factor D}} cleaves factor B, forming the C3 convertase C3bBb, which {{c3::properdin}} stabilizes',
    'This low-level activity runs all the time; host cells shut it down with regulators, while microbial surfaces let it amplify. That is why the alternative pathway works from the first minutes of an infection, without antibodies.',
    "Hidrólise do C3, fator B, fator D, properdina", "Slides 22–23 (C3(H2O), fator B, fator D, properdina)", "c1 verde; c2–c3 azul.",
    "AnKing: só 'espontânea' e 'começa em C3'; fatores B/D/properdina ausentes (busca 'factor B/D', 'properdin' vazia); lacuna."),
 ak("lectinas-manose", 1487640169311, {1: 3, 2: 4}, "B-vias", "Via das lectinas: manose", "Slides 28–30", "c1 verde; c2 azul."),
 ak("lectinas-c1-like", 1487640175721, {1: 4}, "B-vias", "Via das lectinas começa em complexo tipo C1", "Slides 28–30", "Azul."),
 au("mbl-masp", {1: 4, 2: 4}, "B-vias",
    'In the lectin pathway, mannose-binding lectin plays the role of {{c1::C1q}} and its MASPs play the role of C1r/C1s, cleaving {{c2::C4 and C2}} to build the same C3 convertase as the classical pathway',
    'Only the trigger differs: MBL recognizes mannose and N-acetylglucosamine on microbial surfaces instead of antibody.',
    "MBL/MASP análogos de C1q/C1r/C1s", "Slides 28–30 ('MBP ~ C1q', MASP-1/2)", "Azul.",
    "AnKing só manose e 'C1-like complex'; MASP ausente (busca vazia); lacuna."),
 au("vias-inicio-infeccao", {1: 3, 2: 4}, "B-vias",
    'Early in a first infection, before specific antibodies exist, complement is activated mainly by the {{c1::alternative and lectin}} pathways; the classical pathway becomes important once {{c2::IgM and IgG}} are produced',
    'Exception: natural IgM and C-reactive protein can trigger the classical pathway early. UC03 exams repeatedly ask which pathway works in the first days of an infection (P2 2017 1.11; P2 2018 3.6).',
    "Qual via atua no início da infecção", "Slides 5, 7, 60; provas P2 2017 1.11 e P2 2018 3.6", "c1 verde; c2 azul.",
    "Raciocínio cobrado em prova sem card AnKing; lacuna."),
 ak("lps-complemento", 1500572318680, {1: 3, 2: 3}, "B-vias", "LPS ativa complemento → C3a e C5a", "Slide 21 (LPS, ácido teicoico ativam via alternativa)", "Verde.",
    extra_tags=[INFL, "NEBLI::compartilhado::imuno31"]),
 # ---------- CONVERTASES E MAC ----------
 ak("c3-convertase", 1487640180743, {1: 3}, "C-convertases", "Todas as vias geram C3 convertase", "Slides 14–20", "Verde."),
 ak("c3conv-classica", 1487640184312, {1: 4}, "C-convertases", "C3 convertase clássica/lectinas = C4b2b", "Slides 19–20", "Azul.", extra_prefix=NOMEN),
 ak("c3conv-alternativa", 1487640188409, {1: 3}, "C-convertases", "C3 convertase alternativa = C3bBb", "Slide 23", "Verde."),
 ak("c5-convertase", 1487640191924, {1: 3}, "C-convertases", "Todas as vias geram C5 convertase", "Slides 24–25", "Verde."),
 ak("c5conv-classica", 1487640197206, {1: 4}, "C-convertases", "C5 convertase clássica = C4b2b3b", "Slide 24", "Azul.", extra_prefix=NOMEN.replace("C4b2a", "C4b2a3b")),
 ak("c5conv-alternativa", 1487640200798, {1: 4}, "C-convertases", "C5 convertase alternativa = C3bBb3b", "Slide 24", "Azul."),
 ak("mac", 1487640204292, {1: 3}, "D-mac", "C5b + C6–C9 = MAC", "Slides 24–27", "Verde."),
 ak("mac-proteinas", 1487640207727, {1: 4}, "D-mac", "MAC = C5b–C9", "Slides 25–27", "Azul (recuperação inversa)."),
 # ---------- FUNÇÕES E RECEPTORES ----------
 ak("imunocomplexos-c3b", 1487640222923, {1: 3}, "E-funcoes", "C3b remove imunocomplexos", "Slides 33, 45 (remoção via CR1)", "Verde."),
 ak("anafilatoxinas", 1487640139590, {1: 3}, "E-funcoes", "C3a, C4a, C5a ativam mastócitos", "Slides 38–42", "Verde.",
    extra_tags=[INFL, "NEBLI::compartilhado::imuno31"]),
 au("receptores-cr1-cr3", {1: 4, 2: 4}, "E-funcoes",
    '{{c1::CR1 (CD35)}} on phagocytes and red cells binds C3b/C4b to clear immune complexes, while {{c2::CR3 (CD11b/CD18)}} binds iC3b and mediates phagocytosis',
    'CR1 is also a cofactor for factor I. CR2 (CD21) binds C3d on B cells, and C5aR binds C5a (chemotaxis, histamine release).',
    "CR1 × CR3", "Slides 36, 44 (tabela de receptores)", "Azul.",
    "AnKing só CD21–C3d; CR1/CR3 ausentes (busca 'CR1', 'CD35' sem card de complemento); lacuna."),
 ak("cr2-c3d", 1503855271322, {1: 4}, "E-funcoes", "CD21 (CR2) é receptor de C3d", "Slide 43 (correceptor do linfócito B)", "Azul.",
    extra_prefix='On B cells, CR2 forms a co-receptor with CD19/CD81: an antigen coated with C3d engages BCR and CR2 together, lowering the activation threshold (complement as "co-stimulus" of B cells).<br><br>'),
 # ---------- REGULAÇÃO ----------
 au("fator-i-h", {1: 3, 2: 4}, "F-regulacao",
    '{{c1::Factor I}} cleaves C3b (and C4b) into inactive fragments such as iC3b and C3dg, using cofactors like {{c2::factor H}} and CR1',
    'Factor H also displaces Bb from C3bBb. Together they stop the alternative pathway from amplifying on host surfaces.',
    "Fator I cliva C3b com cofator H", "Slides 50–52 (fatores I e H)", "c1 verde; c2 azul.",
    "AnKing: busca 'factor H' só traz proteína M; fator I ausente; lacuna."),
 au("acido-sialico", {1: 4}, "F-regulacao",
    'Host cells avoid alternative-pathway attack because membrane regulators (DAF, CD59, MCP) and surface {{c1::sialic acid}}, which recruits factor H, inactivate any C3b deposited on them',
    'Microbes lacking these signals let C3bBb amplify. Some pathogens copy the trick: streptococcal M protein and sialic-acid capsules recruit factor H to escape complement.',
    "Proteção das células do hospedeiro", "Slides 47–53; prova P2 2018 3.6 (ácido siálico/fator H)", "Azul.",
    "Sem card AnKing (busca 'sialic acid' só vírus/gangliosídeos); lacuna."),
 ak("proteina-m-fator-h", 1500570825309, {1: 4, 2: 4}, "F-regulacao", "Proteína M sequestra fator H", "Prova P2 2018 3.6 (evasão por fator H)", "Azul: ponte com Patogenicidade."),
 ak("daf", 1478986720423, {1: 3, 2: 4}, "F-regulacao", "DAF/CD55 inibe C3 convertase", "Slides 47–49", "c1 verde; c2 azul."),
 ak("gpi-ancora", 1478994988572, {1: 4}, "F-regulacao", "DAF e CD59 ancorados por GPI", "Slides 49, 53", "Azul."),
 ak("gpi-ausente", 1478994993913, {1: 3}, "F-regulacao", "Sem GPI → lise por complemento", "Slides 53, 55 (CD59 → HPN)", "Verde."),
 ak("hpn-defeito", 1478995000657, {1: 4, 2: 3, 3: 4}, "F-regulacao", "HPN: defeito adquirido de GPI", "Slide 55 (CD59 → hemoglobinúria paroxística noturna)", "c2 verde; c1, c3 azul.", uso="Clínica direta (Q044)."),
 ak("hpn-intravascular", 1478995010616, {1: 4}, "F-regulacao", "HPN: hemólise intravascular", "Slide 55", "Azul: consequência direta do MAC.", uso="Clínica direta (Q044)."),
 ak("c1inh-angioedema", 1487727789545, {1: 3, 2: 3}, "F-regulacao", "Deficiência de C1-INH → angioedema hereditário", "Slides 47, 55, 57", "Verde."),
 ak("c1inh-c4", 1487727803414, {1: 3}, "F-regulacao", "C4 baixo na deficiência de C1-INH", "Slide 57; provas (interpretação de C3/C4)", "Verde."),
 ak("c1inh-bradicinina", 1517068230955, {1: 3}, "F-regulacao", "C1-INH deficiente → ↑ bradicinina", "Slide 47 (C1-INH regula calicreína); ponte com Inflamação", "Verde."),
 ak("c1inh-anafilatoxinas", 1578248007976, {1: 4}, "F-regulacao", "↑ C3a/C4a/C5a na deficiência de C1-INH", "Slide 57", "Azul."),
 ak("aeh-ieca", 1474686417807, {1: 4, 2: 4, 3: 3}, "F-regulacao", "IECA contraindicado no angioedema hereditário", "Slide 57 (AEH)", "c3 verde (HY: IECA eleva bradicinina); c1–c2 azul.", uso="Clínica direta (Q044)."),
 ak("aeh-diagnostico", 1563496864933, {1: 4, 2: 4}, "F-regulacao", "AEH: C4 baixo, C1-INH deficiente", "Slide 57", "Azul."),
 ak("aeh-sem-urticaria", 1517365171251, {1: 4}, "F-regulacao", "AEH sem urticária (bradicinina, não histamina)", "Slide 57", "Azul: contraste com histamina."),
 # ---------- DEFICIÊNCIAS E LABORATÓRIO ----------
 ak("terminal-neisseria", 1501968263352, {1: 3}, "G-deficiencias", "C5–C9 sem MAC → Neisseria", "Slides 55, 59", "Verde (1-HighYield)."),
 ak("terminal-quais", 1487727812574, {1: 4}, "G-deficiencias", "Quais deficiências → Neisseria", "Slide 59", "Azul (recuperação inversa)."),
 ak("precoces-sinopulmonares", 1487727814679, {1: 3}, "G-deficiencias", "C1–C4: infecções piogênicas sinopulmonares", "Slides 55–56", "Verde."),
 ak("precoces-les", 1487727820979, {1: 3}, "G-deficiencias", "C1–C4 → LES/glomerulonefrite", "Slides 55–56; prova P3 2024 3.1", "Verde.",
    extra_prefix='Why: C1q, C4 and C2 help clear immune complexes and apoptotic debris; when they are missing, nuclear antigens persist and drive autoimmunity (lupus).<br><br>'),
 au("deficiencia-c3", {1: 3}, "G-deficiencias",
    'Because all three pathways converge on C3, C3 deficiency causes the most severe recurrent {{c1::pyogenic (encapsulated) bacterial}} infections',
    'Without C3 there is no C3b opsonization, no C5 convertase (so no C5a chemotaxis and no MAC), and poor immune-complex clearance.',
    "Deficiência de C3", "Slides 55–56; provas P1 2015 2.2–2.3, P2 2025 6.2", "Verde.",
    "AnKing só 'C1–C4 precoces'; C3 isolado ausente; lacuna."),
 au("fator-h-deficiencia", {1: 3, 2: 3}, "G-deficiencias",
    'In factor H (or factor I) deficiency the alternative pathway runs unchecked and consumes C3, so serum C3 is {{c1::low}} while C4 is {{c2::normal}}',
    'Patients get recurrent pyogenic infections (low C3 → poor opsonization) and may develop atypical hemolytic uremic syndrome from complement damage to glomerular endothelium. The liver makes C3 normally; the low level is consumption.',
    "Fator H/I: C3 baixo com C4 normal", "Slide 55 (fH, fI, SHU); provas P2 2025 6.1, P1 2015 2.4", "Verde.",
    "Sem card AnKing de fator H/I; lacuna."),
 au("padrao-c3-c4", {1: 3, 2: 3}, "G-deficiencias",
    'Low C3 with low C4 points to activation of the {{c1::classical}} pathway (e.g., immune complexes in SLE); low C3 with normal C4 points to consumption through the {{c2::alternative}} pathway',
    'C4 is used only by the classical and lectin pathways, so it separates the two patterns.',
    "Interpretar C3 e C4", "Provas P2 2025 6.1–6.2", "Verde.", "Interpretação cobrada em prova, sem card AnKing; lacuna."),
 au("ch50-ah50", {1: 3, 2: 3, 3: 4}, "G-deficiencias",
    '{{c1::CH50}} tests the classical pathway (C1–C9) and {{c2::AH50}} tests the alternative pathway; a normal CH50 with absent AH50 points to a deficiency of {{c3::factor B, factor D or properdin}}',
    'Both tests measure lysis of red cells, so any missing terminal component (C5–C9) makes both zero.',
    "CH50 × AH50", "Prova P2 2025 1.7", "c1–c2 verde; c3 azul.", "AnKing só 'LES com CH50 baixo'; lacuna."),
 ak("les-ch50", 1487815366607, {1: 4}, "G-deficiencias", "LES: CH50 diminuído (consumo)", "Slides 55–56; prova P2 2025 1.7 (CH50)", "Azul."),
]

COMPARTILHADOS = {
    1790253143896: "Inflamação aguda · quimiotáticos de neutrófilo, incluindo C5a — slides 38–42",
    1790253143998: "Inflamação aguda · C3b e IgG são as opsoninas — slides 33–36",
}

EXCLUIDOS = [
 (1487815316366, "Deficiência precoce e LES — equivalente ao 1487727820979, sem ganho (Q025)"),
 (1478995034893, "HPN: citometria CD55/CD59 — diagnóstico clínico lateral"),
 (1478995016809, "HPN: acidose do sono — fisiopatologia clínica além do slide"),
 (1478995007169, "HPN: anemia normocítica — clínica lateral"),
 (1478995013918, "HPN: episódios noturnos — clínica lateral"),
 (1478995020091, "HPN: teste da sacarose — diagnóstico lateral"),
 (1478995028457, "HPN: NO scavenger — clínica lateral"),
 (1478995038587, "HPN: mnemônico clínico — fora do recorte"),
 (1478995038588, "HPN: mnemônico — idem"),
 (1478995055944, "HPN: trombose venosa — clínica lateral"),
 (1478995063743, "HPN: anemia ferropriva — clínica lateral"),
 (1478995072125, "HPN: LMA — fora do recorte"),
 (1478995078338, "Eculizumabe — terapêutica fora do recorte"),
 (1497203766572, "Eculizumabe — idem"),
 (1497203670771, "Eculizumabe anti-C5 — idem"),
 (1578248124988, "AEH: sintomas GI — clínica lateral"),
 (1517365303958, "AEH: morte por edema de via aérea — clínica lateral"),
 (1578248499297, "AEH: herança AD — fora do recorte"),
 (1503855029259, "EBV–CD21 — Microbiologia/virologia, outra aula"),
 (1478916025067, "Asplenia e encapsulados — outra aula"),
]
FORA_DO_RECORTE = [
 "Clínica e tratamento de HPN (trombose, LMA, sacarose, eculizumabe) e do angioedema hereditário além do elo C1-INH/bradicinina/C4",
 "Glomerulonefrites (GNPE, MPGN/fator nefrítico C3), hipersensibilidade II/III: aulas futuras",
 "Sinalização intracelular do correceptor B (Btk, Vav, PI3K) e estrutura atômica do CD59: ilustração",
 "Venenos e polímeros como ativadores da via alternativa, COVID-19, degeneração macular: exemplos do slide",
]
