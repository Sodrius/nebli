# Especificação curada — 02 Farmacocinética I: bôlus endovenoso, clearance I e clearance II/metabolismo (UC19 P1, Farmacologia; Gilberto De Nucci; 186 lâminas em pptx convertidas em texto: bôlus 1–76, clearance I 77–140, clearance II 141–186; sem transcrição).
# Ciclo básico: princípios da farmacocinética quantitativa (cinética de primeira ordem, volume de distribuição, clearance, metabolismo e variabilidade), sem fármaco por indicação.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = "A aula é de farmacocinética quantitativa (equação exponencial, semilog, t½, fração de extração, clearance do órgão, R0 = Cl·Css, doses repetidas) que o AnKing não traz; só aparecem fórmulas isoladas; busca nos três caminhos não achou esses cards."
PIPELINE = "anking-primeiro"
RUN_ID = "uc19-fc02-20261021a"
SHORT = "fc02"
LESSON = "2026-uc19-farmacologia-02-farmacocinetica-i"
DECK = "NEBLI::UC19::P1::Farmacologia::Farmacocinética I"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261021-CLAUDE-01 + ANTI-EXEMPLARES §1–16, 21/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (21/10): seções de recurso do AnKing (farmacocinética: Bootcamp, FirstAid e Physeo; busca/secoes); palavra-chave e significado "
         "em AnKing, Referências Externas e NEBLI vivo (busca/semantica.jsonl, uma consulta por conceito). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)



A_, B_, C_, D_, E_, F_, G_ = "A-bolus-cinetica", "B-distribuicao-vd", "C-dose-acumulo", "D-clearance", "E-rim", "F-metabolismo", "G-variabilidade"
EXCLUIDOS = []
FORA_DO_RECORTE = [
    "Capas, dúvidas e figuras de livro (Rowland e Tozer, Principles of Pharmacology, Vander): ilustram, não ensinam alvo; as curvas de estudos clínicos (varfarina, nortriptilina, metanfetamina, fenobarbital) ficam como exemplo.",
    "Insulinas humana e análogas, NPH e nomes comerciais (lâminas 25–31): exemplo de formulação, sem cobrança; só entram a PEGuilação e a insulina de ação prolongada como mudança de meia-vida.",
    "Cinética de ordem zero, Michaelis-Menten e Lineweaver-Burk: não são da aula; ficam para a P2 de enzimas.",
    "Lista de inibidores e indutores do CYP450 por isoforma (lâmina 160) e os estudos de coorte de clopidogrel e omeprazol (lâminas 21–25 do clearance II): detalhe de fármaco específico.",
    "Doses e esquemas de fármacos por indicação (aminofilina, teofilina, isoniazida, morfina) além do cálculo: farmacologia clínica de outras UCs.",
]

CARDS = [
    # Bôlus endovenoso (lâminas 1–76)
    au("au-exp", "After an IV bolus the plasma concentration falls as C = {{c1::C0 · e^(−kt)}}",
       "V-pilar", A_, "Queda exponencial após o bôlus", 8, "lâminas 2–9 (concentração × tempo após 200 mg e dedução de C = C0 e^−kt)",
       extra="- C0 is the virtual concentration at time zero, before any elimination<br>- The fall is exponential because a constant fraction is eliminated per unit time"),
    K(1490066232397, "V-pilar", A_, "Primeira ordem: fração constante por unidade de tempo", 8, "lâminas 3–8 (queda exponencial); seção FirstAid de eliminação"),
    K(1490066239613, "A-aula", A_, "Eliminação de primeira ordem: curva exponencial", 8, "lâminas 3–8; seção FirstAid de eliminação"),
    K(1472426521266, "A-aula", A_, "Primeira ordem: a taxa é proporcional à concentração", 8, "lâminas 3–8; seção Bootcamp de cinética de eliminação"),
    au("au-semilog", "On a semilog plot the decline is a straight line, with slope {{c1::−k}} and intercept {{c2::C0}}",
       "V-pilar", A_, "Gráfico semilogarítmico: reta de inclinação −k", 12, "lâminas 10–12 (logaritmo da concentração × tempo, inclinação −k e C0)",
       extra="- ln C = ln C0 − kt is the linear form of the exponential equation<br>- The slope gives the elimination constant k"),
    au("au-t12", "<b>Half-life</b> t½ = {{c1::0.693}} / {{c2::k}}",
       "V-pilar", A_, "Meia-vida e constante de eliminação", 17, "lâminas 13–17 (dedução de t½ = 0,693/k)",
       extra="- 0.693 is ln 2<br>- If k is larger, the drug is eliminated faster and t½ is shorter"),
    K(1490066195477, "A-aula", A_, "t½ = 0,693 · Vd / CL", 17, "lâmina 17 e apostila (a meia-vida depende do volume e do clearance); seção FirstAid de meia-vida"),
    au("au-fracao", "After n half-lives the fraction left is {{c1::(1/2)^n}}, so after five half-lives almost all is gone",
       "A-aula", C_, "Fração restante após n meias-vidas", 61, "lâminas 55–61 (fração da dose no organismo em relação à meia-vida)",
       extra="- One half-life leaves 50%, two leave 25%, three leave 12.5%<br>- Clinically, five half-lives mean practical elimination"),
    # Distribuição e volume (lâminas 18–52)
    au("au-distrib-ordem", ORG("<b>After an IV bolus</b>, tissues fill by perfusion:<br>- first {{c1::vessel-rich}} organs<br>- then {{c2::muscle}}<br>- last {{c3::fat}}"),
       "V-pilar", B_, "Distribuição: órgãos bem perfundidos, músculo e gordura", 19, "lâminas 18–19 (fase de distribuição, fase de eliminação e modelo de quatro compartimentos)",
       extra="- The early steep fall in plasma is the distribution phase<br>- The later straight part is the elimination phase"),
    K(1523479052793, "A-aula", B_, "Propofol: acumula em tecidos bem perfundidos e redistribui", 19, "lâmina 19 (compartimentos e redistribuição); seção de anestésicos"),
    K(1484778178394, "A-aula", B_, "Tiopental: cai por redistribuição para músculo e gordura", 19, "lâmina 19 (redistribuição); seção de barbitúricos"),
    K(1490061652098, "V-pilar", B_, "Volume de distribuição: volume teórico do fármaco no corpo", 38, "lâminas 38–47 (volume aparente de distribuição); seção FirstAid"),
    K(1490066159100, "V-pilar", B_, "Vd = dose / C0", 46, "lâmina 46 (cálculo do Vd com a dose e C0); seção FirstAid"),
    K(1490066162567, "A-aula", B_, "Molécula grande ou carregada: Vd baixo", 43, "lâminas 39–45 (distribuição conforme tamanho e carga); seção FirstAid"),
    K(1490066166158, "A-aula", B_, "Ligada a proteína plasmática: Vd baixo", 43, "lâmina 43 (ligação a proteínas retém o fármaco no plasma)"),
    K(1490066171169, "A-aula", B_, "Pequena e hidrofílica: Vd médio", 43, "lâminas 40–42 (água extracelular)"),
    K(1490066174929, "A-aula", B_, "Pequena e lipofílica: Vd alto", 44, "lâminas 43–45 (coeficiente de partição óleo-água)"),
    K(1490066178586, "A-aula", B_, "Vd baixo: o fármaco fica no compartimento intravascular", 47, "lâmina 47 (volume e compartimentos)"),
    K(1490066181877, "A-aula", B_, "Vd médio: o fármaco fica no líquido extracelular", 47, "lâmina 47"),
    K(1490066185604, "A-aula", B_, "Vd alto: o fármaco fica em todos os tecidos, inclusive gordura", 47, "lâmina 47"),
    # Dose e acúmulo (lâminas 53–76)
    K(1490066204599, "A-aula", C_, "Dose de ataque = Cp · Vd / F", 54, "lâminas 53–54 (dose de aminofilina para atingir 15 mg/L); seção FirstAid de doses"),
    au("au-acumulo", ORG("<b>Repeated doses</b> of the drug every τ:<br>- fraction of the dose kept: r = {{c1::e^(−kτ)}}<br>- steady state: Qmin = Qmax − {{c1::one dose}}"),
       "A-aula", C_, "Doses repetidas: fração mantida e estado de equilíbrio", 73, "lâminas 62–76 (quantidade máxima e mínima após N doses)",
       extra="- The maximum after N doses is dose × (1 − r^N) / (1 − r)<br>- The amount builds up until what is lost between doses equals one dose"),
    K(1490066198198, "A-aula", C_, "Infusão constante em primeira ordem: 4–5 meias-vidas até o equilíbrio", 76, "lâmina 76 (estado de equilíbrio) e apostila (Css)"),
    K(1490066207488, "A-aula", C_, "Dose de manutenção = Cp · CL · τ / F", 76, "lâmina 76 e apostila (a dose de manutenção depende do clearance)"),
    K(1490066212502, "A-aula", C_, "Doença renal ou hepática: reduz a dose de manutenção", 76, "lâmina 76 (clearance menor, menos dose)"),
    K(1462849196492, "R-detalhe", C_, "Insulinas glargina, detemir e degludec: ação prolongada", 31, "lâminas 25–31 (formulação que muda o perfil de absorção)"),
    K(1497439509366, "A-aula", C_, "PEGuilação do interferon prolonga a meia-vida", 31, "lâmina 31 e questões orientadoras (a formulação muda a meia-vida)"),
    # Clearance I (lâminas 77–140)
    K(1490066192922, "V-pilar", D_, "Clearance = taxa de eliminação / concentração = Vd · Ke", 87, "lâminas 78–87 (o parâmetro mais importante); seção FirstAid de clearance"),
    au("au-extracao", "The <b>extraction fraction</b> of an organ is E = ({{c1::Ca}} − {{c2::Cv}}) / Ca",
       "V-pilar", D_, "Fração de extração", 81, "lâminas 80–82 (balanço de massas entre artéria e veia)",
       extra="- Ca is the arterial concentration entering the organ and Cv the venous concentration leaving it<br>- E varies from 0 to 1"),
    au("au-extracao-lim", ORG("<b>Limits of extraction</b>:<br>- Cv = {{c1::0}}: E is 1, all removed<br>- Cv = Ca: E is {{c2::0}}"),
       "A-aula", D_, "Extração máxima e nula", 83, "lâminas 83–84 (Cv = 0 e Cv = Ca)",
       extra="- High E means a high capacity of the organ to extract the drug<br>- E = 0 means no extraction"),
    au("au-cl-organ", "The <b>clearance of an organ</b> is its blood {{c1::flow}} times its extraction fraction {{c2::E}}",
       "V-pilar", D_, "Clearance do órgão = fluxo × extração", 87, "lâminas 85–87 (balanço de massas e Cl = Fx · E); questões orientadoras",
       extra="- It links the extraction to the dose: clearance is what the organ removes per unit time"),
    au("au-hepatico", ORG("<b>The hepatic clearance</b> of a drug with:<br>- high E (lidocaine) depends on {{c1::blood flow}}<br>- low E (warfarin) depends on {{c2::enzyme activity}}"),
       "V-pilar", D_, "Clearance hepático: fluxo × atividade enzimática", 91, "lâminas 90–93 (alta extração depende do fluxo; baixa extração é independente); questões orientadoras",
       extra="- Beta-blockers lower hepatic blood flow and reduce lidocaine clearance<br>- High E is above 0.7 and low E is below 0.3"),
    au("au-R0", "At steady state the infusion rate is R0 = {{c1::Cl}} × {{c2::Css}}",
       "V-pilar", D_, "Taxa de infusão no equilíbrio", 97, "lâminas 95–97 (aminofilina: 48 mL/min × 15 mg/L, cerca de 43 mg/h); questões orientadoras",
       extra="- Clearance 48 mL/min × 15 mg/L = 0.72 mg/min, about 43 mg/h<br>- It uses the clearance, not the half-life, to set the dose"),
    au("au-cl-soma", "<b>Systemic clearance</b> is the {{c1::sum}} of the hepatic, renal and other clearances",
       "A-aula", D_, "Clearance sistêmico = soma dos parciais", 104, "lâminas 102–106 (taxa de eliminação sistêmica = renal + hepática + outras)",
       extra="- Elimination rate = clearance × concentration (mg/min = mL/min × mg/mL)"),
    # Rim (lâminas 108–140)
    K(1474763194481, "A-aula", E_, "Clearance renal: volume de plasma depurado por unidade de tempo", 108, "lâminas 108–112 (clearance renal); seção de fisiologia renal"),
    K(1474763204239, "A-aula", E_, "Cl renal = (U · V) / P", 110, "lâminas 110–112 (concentração e volume urinários); questões orientadoras"),
    K(1474763614010, "A-aula", E_, "Inulina: livremente filtrada, sem reabsorção nem secreção", 114, "lâmina 114 (manuseio renal da inulina)"),
    K(1474763658246, "A-aula", E_, "Clearance de creatinina também estima a filtração glomerular", 116, "lâminas 116–118 (clearance da creatinina)"),
    K(1474763662554, "R-detalhe", E_, "A creatinina é um pouco secretada e superestima a filtração", 118, "lâmina 118 (clearance da creatinina)"),
    au("au-crcl", "The <b>creatinine clearance</b> is about {{c1::120}} mL/min, the urinary creatinine in 24 h divided by the plasma level",
       "A-aula", E_, "Clearance de creatinina: cerca de 120 mL/min", 118, "lâminas 116–118 (1,73 g em 24 h e 1 mg%); questões orientadoras",
       extra="- 1.73 g in 1440 min with plasma 1 mg/100 mL gives 120 mL/min"),
    K(1474922567572, "A-aula", E_, "Urina ácida: ácido fraco fica HA e é menos excretado", 133, "lâminas 133–136 (pH urinário e clearance renal); seção Bootcamp de pH urinário"),
    K(1474922575831, "A-aula", E_, "Urina alcalina: ácido fraco fica A− e é mais excretado", 134, "lâminas 133–136 (ácido salicílico e fenobarbital)"),
    K(1474922592292, "A-aula", E_, "Urina ácida: base fraca fica BH+ e é mais excretada", 135, "lâminas 133–136 (metanfetamina)"),
    K(1474922584626, "A-aula", E_, "Urina alcalina: base fraca fica B e é menos excretada", 135, "lâmina 133 (metanfetamina na diurese ácida e alcalina)"),
    K(1490066246680, "A-aula", E_, "A forma ionizada fica presa na urina e sai mais rápido", 136, "lâminas 133–136 (captura iônica); seção FirstAid de pH urinário"),
    K(1490066253471, "A-aula", E_, "Ácido fraco em excesso: alcalinizar a urina com bicarbonato", 136, "lâmina 136 (fenobarbital na diurese alcalina)"),
    K(1504365355577, "A-aula", E_, "Probenecida aumenta o nível sérico de penicilina", 137, "lâmina 137 (efeito da probenecida na amoxicilina)"),
    K(1504377142463, "R-detalhe", E_, "Probenecida inibe os transportadores de ânions orgânicos do túbulo proximal", 137, "lâmina 137 (secreção tubular ativa)"),
    K(1474580915632, "R-detalhe", E_, "Teofilina tem índice terapêutico estreito", 139, "lâminas 139–140 (clearance de teofilina em várias condições)"),
    # Metabolismo (lâminas 141–186)
    K(1490066261471, "V-pilar", F_, "Fase I: redução, oxidação e hidrólise", 155, "lâminas 141–155 (metabolismo e CYP450); seção FirstAid de metabolismo"),
    K(1490066263554, "A-aula", F_, "Fase I: metabólito pouco polar, em geral ainda ativo", 155, "lâmina 155"),
    K(1490066265387, "V-pilar", F_, "Fase II: metilação, glicuronidação, acetilação e sulfatação", 155, "lâmina 155 (conjugação)"),
    K(1490066268966, "A-aula", F_, "Fase II: metabólito muito polar, em geral inativo", 155, "lâmina 155"),
    au("au-cyp3a4", "The isoform <b>{{c1::CYP3A4/5}}</b> metabolizes the largest share of clinically used drugs, about 36%",
       "A-aula", F_, "CYP3A4/5: isoforma que metaboliza mais fármacos", 155, "lâmina 155 (percentual de fármacos metabolizados por cada isoforma do CYP450); questões orientadoras",
       extra="- CYP450 is the main superfamily of phase I oxidation in hepatocytes<br>- It is also abundant in the intestine, which lowers oral bioavailability"),
    K(1505265548040, "R-detalhe", F_, "Imipenem é degradado pela dipeptidase renal I", 154, "lâmina 154 (cilastatina e imipenem)"),
    K(1505265624884, "R-detalhe", F_, "Cilastatina inibe a dipeptidase renal I", 154, "lâmina 154; questões orientadoras"),
    K(1503259126424, "A-aula", F_, "Rifampicina induz o citocromo P450", 148, "lâmina 148 (efeito da rifampicina na varfarina); seção Bootcamp de CYP450"),
    au("au-rif-warf", "<b>Rifampin</b> {{c1::induces}} CYP2C9 and shortens the effect of warfarin",
       "A-aula", F_, "Rifampicina induz o CYP e reduz o efeito da varfarina", 148, "lâminas 145–148 (rifampicina e varfarina); questões orientadoras",
       extra="- More enzyme means faster clearance, a lower plasma level and a lower prothrombin time"),
    K(1488765303577, "A-aula", G_, "Varfarina é metabolizada pelo CYP450", 145, "lâminas 145–147 (variabilidade da dose de varfarina)"),
    K(1488765308661, "R-detalhe", G_, "Varfarina: polimorfismos de CYP2C9 e VKORC1", 147, "lâmina 147 (a genética define a dose)"),
    K(1485127406267, "A-aula", F_, "Fenitoína induz o citocromo P450", 151, "lâminas 151–152 (indução por pentobarbital e fenobarbital)"),
    K(1484778245242, "A-aula", F_, "Barbitúricos induzem o citocromo P450", 152, "lâmina 152 (fenobarbital e dicumarol)"),
    K(1490137911734, "R-detalhe", F_, "Álcool crônico induz o CYP450", 152, "lâminas 150–152 (indução e inibição)"),
    K(1490137917396, "R-detalhe", F_, "Álcool agudo inibe o CYP450", 150, "lâmina 150 (inibição do metabolismo)"),
    au("au-prodrug", "<b>Clopidogrel</b> is a prodrug activated by {{c1::CYP2C19}}, a step that omeprazole {{c2::inhibits}}",
       "V-pilar", F_, "Clopidogrel: pró-fármaco ativado pelo CYP2C19", 159, "lâminas 156–164 (ativação do clopidogrel e interação com inibidores de bomba); questões orientadoras",
       extra="- Less active thiol metabolite means less platelet inhibition<br>- Carriers of the CYP2C19*2 allele respond less to clopidogrel"),
    K(1525889378661, "R-detalhe", F_, "Codeína em si não é bioativa", 159, "lâminas 156–159 (pró-fármaco)"),
    au("au-keto", "<b>Ketoconazole</b> inhibits {{c1::CYP3A4}}, so terfenadine accumulates and prolongs the {{c2::QT}} interval",
       "A-aula", G_, "Cetoconazol, CYP3A4 e terfenadina", 167, "lâmina 167 (torsades de pointes por associação); questões orientadoras",
       extra="- Reduced metabolic clearance of terfenadine leads to cardiotoxic accumulation<br>- Clarithromycin irreversibly inactivates CYP3A and raises midazolam levels"),
    K(1505674844706, "A-aula", G_, "Claritromicina e eritromicina inibem o CYP450", 173, "lâmina 173 (claritromicina e midazolam)"),
    K(1472668562134, "R-detalhe", G_, "Estatinas, exceto pravastatina, são metabolizadas pelo CYP450", 175, "lâmina 175 (rifampicina e atorvastatina)"),
    K(1503257887579, "A-aula", G_, "Isoniazida é metabolizada pela NAT2", 177, "lâminas 177–178 (polimorfismo de acetilação); seção de antibióticos"),
    K(1490066271518, "A-aula", G_, "Acetiladores lentos têm mais efeitos adversos", 177, "lâmina 177 (distribuição bimodal da isoniazida); seção FirstAid de metabolismo"),
    K(1503257926878, "A-aula", G_, "Acetilador lento: risco maior com isoniazida", 178, "lâmina 178 (hepatotoxicidade por isoniazida no grupo não genotipado)"),
    K(1520710751756, "R-detalhe", G_, "Biodisponibilidade F pela razão das áreas sob a curva", 179, "lâmina 179 (morfina oral × endovenosa)"),
    K(1490066273472, "A-aula", G_, "A fase I se perde primeiro no idoso", 182, "lâminas 181–183 (idade e metabolismo)"),
    K(1520906706487, "A-aula", G_, "A função renal diminui com a idade", 182, "lâminas 181–183 (idade)"),
    au("au-tabaco", "<b>Smoking</b> induces {{c1::CYP1A2}}, so stopping it raises {{c2::theophylline}} levels",
       "A-aula", G_, "Tabaco induz o CYP1A2 e reduz a teofilina", 139, "lâminas 63 e 139 (clearance de teofilina em fumantes); questões orientadoras",
       extra="- Smokers have a higher theophylline clearance and need a higher dose<br>- After stopping, clearance falls and levels may become toxic"),
    K(1474580933087, "A-aula", G_, "Teofilina é metabolizada pelo citocromo P450", 139, "lâminas 139–140 (clearance de teofilina)"),
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
 "ak1490066239613": "- A constant fraction eliminated per time makes the plasma curve exponential and a straight line on a semilog plot",
 "ak1490066195477": "- Larger volume or lower clearance lengthens the half-life",
 "ak1523479052793": "- The brain gets the drug first, then it is redistributed to muscle and fat, which ends the effect",
 "ak1490061652098": "- It is an apparent volume: dose divided by the initial concentration, not a real anatomical space",
 "ak1474763194481": "- It is the plasma volume cleared per unit time, so its unit is mL/min",
 "ak1484778245242": "- More enzyme means faster clearance and lower levels of other drugs metabolized by the same isoforms",
 "ak1505265624884": "- It is given with imipenem so the antibiotic is not destroyed in the kidney",
 "ak1490066263554": "- Oxidation by CYP450 is the main phase I reaction; the product can still be active",
 "ak1490066268966": "- Conjugation adds glucuronide, acetyl or sulfate, so the metabolite is excreted in urine or bile",
 "ak1490066273472": "- Oxidative phase I metabolism declines with age, so the half-life of drugs like diazepam is longer",
}

for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
exec((HERE / "exclusoes.py").read_text(encoding="utf-8")) if (HERE / "exclusoes.py").exists() else None

SEM_IMAGEM = "fato ou conjunto sem estrutura a reconhecer; as figuras da aula são gráficos de estudos clínicos e esquemas de livro"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
DUPLICACAO = {"au-rif-warf": "o card de rifampicina diz só que ela induz o CYP450; este liga a indução do CYP2C9 à queda do efeito da varfarina, exemplo da aula"}
for _k, _v in DUPLICACAO.items():
    _c = next((c for c in CARDS if c["key"] == _k), None)
    if _c:
        _c["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
    "objetivo": "Calcular e interpretar a farmacocinética de um fármaco após bôlus endovenoso: cinética de primeira ordem, volume de distribuição, clearance e metabolismo.",
    "centrais": [("cinética", "au-exp", "ak1490066232397", "au-semilog", "au-t12"), ("distribuição", "au-distrib-ordem", "ak1490061652098"), ("clearance", "au-extracao", "au-cl-organ", "au-hepatico", "au-R0"), ("metabolismo", "au-prodrug")],
    "exemplos": ["aminofilina", "varfarina", "isoniazida", "insulinas", "estudos de coorte"],
    "outras_aulas": [("absorção e vias de administração", "Farmacocinética II"), ("farmacodinâmica", "01 e 04 de UC19"), ("clearance renal em detalhe", "Farmacocinética III e IV")],
}
_slide = lambda c: int(_re.search(r"\d+", c["evid"]).group())
CARDS.sort(key=_slide)
