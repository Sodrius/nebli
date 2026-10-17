# Especificação curada — 56 Contrastes radiológicos (UC03 P3, Radiologia; Dr. André Bordini e preceptoria; 85 lâminas = Contraste I
# (1–42, aula com transcrição) + Contraste II (43–85, versão 2023 da mesma aula, com casos)). Gerada a partir de inventario.py.
# Ordem = lâminas. AnKing → cópias NEBLI vivas da 02 e da UC08 → vagas para os cards da 05 (fases) e da 12 (gadolínio, fibrose
# nefrogênica), que ainda não estão instaladas → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = ["_Bootcamp_Nephrology_10_Nephrolithiasis_01_Nephrolithiasis_Overview.txt"]  # caso da cólica renal (lâmina 81); o AnKing não tem seção de meios de contraste
AUTORAL_EXCECAO = ("Aula de técnica radiológica: regras do bário, duplo contraste, água como contraste neutro, colangio-RM e angio-RM "
                   "sem contraste, microbolhas, faixas de clearance e gravidade das reações não têm card em AnKing, MCAT, Ankisthesia ou "
                   "NEBLI vivo (busca/anking.txt: 0 notas para double contrast, microbubble, angioedema+contrast, gadolinium; "
                   "busca/semantica.jsonl); o que existe (achados de bário, nefropatia, Jod-Basedow, cistografia, HSG) entra como AnKing")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-rd56-20261017a"
SHORT = "rd56n"
LESSON = "2026-uc03-radiologia-56-contrastes"
DECK = "NEBLI::UC03::P3::Radiologia::Contrastes radiológicos"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"rd56-{n}.jpg": f"img/rd56-{n}.jpg" for n in ("enema", "microbolhas", "reacoes", "angiorm")}
IMG = lambda n, w=460: f'<img src="rd56-{n}.jpg" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (não há seção de meios de contraste; busca/secoes vazio de propósito); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt: barium, water-soluble, double contrast, microbubble, "
         "cystogram, HSG, MRCP, urography, contrast-induced, angioedema, MR angiography, anaphylactoid, gadolinium); significado em "
         "todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
# Vagas: cópias NEBLI das aulas 05 (TC) e 12 (RM), prontas mas não instaladas; preencher com o nid da cópia depois do apply delas.
RD05 = {"FASES": 1792239680174}   # au-fases da 05
RD12 = {"GADO": 1792240900691, "FNS": 1792240901193}   # au-gadolinio e au-fns da 12
EXCLUIDOS = [
 (1578963423619, "conduta antes do contraste no renal (hidratar, suspender metformina): farmacologia clínica, fora das lâminas"),
 (1550709687046, "cintilografia V/Q no TEP com TFG < 30: escolha de exame de outra aula"),
 (1535889785581, "repete ak-cistografia (cistografia retrógrada no trauma pélvico)"),
 (1557097138665, "pielografia IV no trauma renal instável: conduta de trauma, fora das lâminas"),
 (1511123850582, "contraste hidrossolúvel na obstrução de delgado: conduta, fora das lâminas"),
 (1532189052771, "angio-TC na dissecção de aorta: indicação clínica de outra aula"),
 (1475453132862, "definição do cálculo: nefrologia, fora das lâminas"),
 (1475453135801, "fatores de risco do cálculo: nefrologia, fora das lâminas"),
 (1475453150219, "tratamento/prevenção do cálculo: nefrologia"),
 (1587951758262, "dieta no cálculo renal: nefrologia"),
 (1475713336232, "hematúria sem cilindros: nefrologia, fora das lâminas"),
 (1520726640112, "colangiografia com falhas de enchimento: a aula mostra a colangiografia só como lista de exames"),
]
FORA_DO_RECORTE = [
 "Videodeglutografia, videodefecografia, trânsito intestinal, dacriocistografia, sialografia e cistotomografia: nomes de exames sem cobrança.",
 "Protocolos de tempo das fases (segundos), equações de clearance e diretrizes de nefropatia: Tab (§4) e aula 05.",
 "Tratamento detalhado das reações (protocolos de cada serviço): farmacologia/emergência.",
]
A_, B_, C_, D_, E_ = "A-por-que-e-quais", "B-intracavitario", "C-intravascular", "D-reacoes-contraindicacoes", "E-casos"

CARDS = [
 # ---------- A. Por que usar e quais contrastes (lâminas 2–7, 44–45) ----------
 sh(1792141768903, "azul", A_, "Contraste intrínseco × exógeno", 2, "A-aula: lâminas 2, 44–45 (contraste aumenta a resolução de contraste); card da 02"),
 au("au-bario", "<b>Barium</b> goes only inside the GI tract on X-ray, never IV, and never when {{c1::perforation}} is suspected",
    "V-pilar", A_, "Bário: só no tubo digestivo, nunca EV", 7, "lâminas 6–8, 11; transcrição (“falou em bário, pensar em raio-x e nunca endovenoso”)",
    extra="- With suspected perforation or fistula, use water-soluble iodinated contrast<br>- Iodine works orally, rectally and IV, on X-ray or CT"),
 ak("ak-hidrossoluvel", 1511206455074, "A-step", A_, "Perfuração: contraste hidrossolúvel", 7, "lâminas 7 e 11 (iodo na suspeita de fístula/perfuração)"),
 # ---------- B. Intracavitário (lâminas 8–18, 46–56, 68–73) ----------
 au("au-duplo", "In the double-contrast <b>barium enema</b>, barium coats the colon wall and {{c1::air}} distends the lumen",
    "V-prova", B_, "Enema opaco com duplo contraste", 10, "lâminas 8, 10 e 51; transcrição; prova 2018 P3 2.1 (enema opaco: megacólon)",
    extra="- Also used in the upper GI series (EED)<br>- Shows diverticula, strictures, masses and dilation (megacolon)<br>" + IMG("enema")),
 au("au-agua", "On CT, oral <b>water</b> is a neutral contrast that distends bowel loops so their {{c1::wall}} can be seen",
    "A-aula", B_, "Água: contraste neutro na TC", 12, "lâminas 11–12; transcrição",
    extra="- Positive oral contrast (diluted iodine) is almost as bright as bone; water stays near fluid density"),
 au("au-colangio", "<b>MR cholangiography</b> needs no IV contrast, because heavily T2-weighted images make the bile ducts' {{c1::fluid}} bright",
    "A-aula", B_, "Colangio-RM sem contraste EV", 13, "lâminas 13 e 72; transcrição; apostila guia de Radiologia",
    extra="- Shows the common bile duct, hepatic ducts and main pancreatic duct<br>- Entero-MRI distends loops with oral fluid such as polyethylene glycol"),
 ak("ak-mrcp", 1536666750645, "A-step", B_, "Colangio-RM nas estenoses biliares", 13, "lâminas 13 e 72 (colangioRM)"),
 ak("ak-uro-tc", 1532614691597, "A-aula", B_, "Urotomografia avalia todo o trato urinário", 15, "lâminas 14–15 e 53 (urografia excretora substituída pela TC excretora)"),
 ak("ak-vcug", 1539251487780, "A-step", B_, "Uretrocistografia miccional no refluxo", 16, "lâminas 16 e 52 (urografia miccional)"),
 ak("ak-uretrografia", 1495069723619, "A-step", B_, "Uretrografia retrógrada na lesão de uretra", 16, "lâminas 16 e 52 (urografia retrógrada)"),
 ak("ak-hsg", 1525534447417, "V-hy", B_, "Histerossalpingografia: perviedade tubária", 17, "lâminas 17 e 54; transcrição (infertilidade)"),
 ak("ak-bico", 1482203812587, "V-hy", B_, "Acalásia: bico de pássaro no bário", 49, "lâmina 49 (EED com bário: megaesôfago chagásico)"),
 sh(1790972066061, "azul", B_, "Acalásia idiopática ou por Chagas", 49, "A-aula: lâmina 49 (megaesôfago chagásico); card da UC08"),
 ak("ak-maca", 1482959782912, "A-aula", B_, "Câncer colorretal: lesão em maçã mordida", 51, "lâmina 51 (enema opaco com a maçã mordida)"),
 # ---------- C. Intravascular (lâminas 20–31, 57–73) ----------
 sh(1792141769157, "verde", C_, "Contraste EV de cada método", 21, "V-prova: lâminas 21–22, 41, 59; provas 2025 P4 1.2, 2024 P4 2.1, 2023 P1 1.4, 2015 P3sub 1.1 (contraste iodado EV na TC); organizador da 02"),
 sh(1792141766909, "azul", C_, "Arteriografia digital e intervenção", 23, "A-aula: lâminas 22–23; transcrição (embolização, cateterismo); card da 02"),
 au("au-microbolhas", "<b>Ultrasound contrast</b> uses IV microbubbles smaller than {{c1::red blood cells}}, which stay inside the vessels",
    "A-aula", C_, "Microbolhas no ultrassom", 25, "lâminas 25–27; transcrição (1–3 µm, hemácia 6 µm)",
    extra="- They reach the capillary bed and show lesion vascularity in real time<br>" + IMG("microbolhas")),
 au("au-tof", "<b>MR angiography</b> can show vessels without IV contrast, using the {{c1::flow}} of blood",
    "A-aula", C_, "Angio-RM sem contraste (fluxo)", 31, "lâminas 31 e 73; transcrição; apostila guia de Radiologia",
    extra="- Time-of-flight (TOF) or phase contrast; gadolinium adds sequences when needed<br>"
          "- Post-gadolinium MRI is usually T1-weighted with fat saturation<br>" + IMG("angiorm")),
 # ---------- D. Reações adversas e contraindicações (lâminas 33–40, 74–80) ----------
 au("au-reacoes", "Among <b>IV contrast reactions</b>, facial angioedema is feared because it can close the {{c1::glottis}}",
    "V-prova", D_, "Gravidade das reações ao contraste", 33, "lâminas 33–37, 75, 77; transcrição; provas 2019 P3 2.2, 2015 P3sub 1.2 (cuidados com o contraste)",
    extra="- Scale: urticaria → angioedema → bronchospasm, glottic edema, anaphylactic shock → cardiorespiratory arrest<br>"
          "- Rare (severe < 1%), more with iodine than gadolinium; acute within 1 h, late (9 h–1 week) usually cutaneous<br>" + IMG("reacoes")),
 ak("ak-adrenalina", 1477011883318, "V-hy", D_, "Adrenalina no choque anafilático", 37, "lâmina 37; transcrição (angioedema facial: adrenalina)"),
 au("au-clearance", "IV contrast is contraindicated when <b>creatinine clearance</b> is below {{c1::30}} mL/min, unless dialysis follows",
    "V-prova", D_, "Clearance < 30: contraindicação", 38, "lâminas 38, 74 e 76; transcrição; provas 2016 P3 2.6 e 2.7 (iodo e gadolínio no dialítico), 2017 P3 2.2",
    extra="- 30–45 mL/min: weigh the indication; > 45: usually safe, unless acute kidney injury<br>"
          "- A prior severe reaction also contraindicates the same agent: switch method (e.g., MRI instead of CT)"),
 ak("ak-cin", 1532616196814, "V-prova", D_, "Nefropatia induzida por contraste", 39, "lâminas 39 e 75; transcrição (piora transitória da função renal só com iodo); provas 2017 P3 2.2, 2017 P2 2.2"),
 ak("ak-cin-risco", 1536438712655, "A-step", D_, "Risco: lesão renal prévia", 39, "lâminas 38–39 e 74"),
 ak("ak-cin-hidratacao", 1532616085999, "A-step", D_, "Hidratação previne a nefropatia", 39, "lâmina 75 (injúria renal pós-contraste)"),
 ak("ak-jod-basedow", 1519711198292, "R-detalhe", D_, "Contraste iodado e tireotoxicose", 75, "lâmina 75 (muito tardias: tireotoxicose no Graves não controlado)"),
 # ---------- E. Casos (lâminas 81–83) ----------
 ak("ak-colica", 1475453139770, "V-hy", E_, "Cólica renal irradiada para a virilha", 81, "lâmina 81 (dor súbita na FIE, Giordano +); seção Bootcamp"),
 ak("ak-colica-obstrucao", 1475453142267, "A-step", E_, "Cálculo obstrutivo: dor lombar unilateral", 81, "lâmina 81; seção Bootcamp"),
 ak("ak-litiase", 1535195599425, "A-step", E_, "Litíase: TC sem contraste", 81, "lâmina 81 (cólica renal: TC com grande acurácia para litíase)"),
 ak("ak-litiase-us", 1555536756446, "A-step", E_, "Litíase: TC no adulto, US na criança e na gestante", 81, "lâmina 81 (US com sensibilidade moderada para cálculo)"),
 ak("ak-litiase-complica", 1475453353414, "A-step", E_, "Cálculo complica com hidronefrose e pielonefrite", 82, "lâmina 82 (pielonefrite nas fases pré, venosa e excretora); seção Bootcamp"),
 ak("ak-cistografia", 1532602900315, "A-step", E_, "Trauma pélvico com hematúria: cistografia retrógrada", 83, "lâmina 83 (politrauma com hematúria: cistotomografia)"),
]
_SH05 = [("FASES", "azul", C_, "Fases do contraste na TC", 24, "A-aula: lâminas 24, 57–66 (sem contraste, arterial, venosa, equilíbrio, excretora); autoral da 05")]
_SH12 = [("GADO", "azul", C_, "Gadolínio e realce em T1", 28, "A-aula: lâminas 28–30, 71 (gadolínio: sinal alto em T1); autoral da 12"),
         ("FNS", "verde", D_, "Fibrose nefrogênica sistêmica", 39, "V-prova: lâminas 39–40, 76–80; prova 2016 P3 2.7 (gadolínio no dialítico); autoral da 12")]
for _d, _l in ((RD05, _SH05), (RD12, _SH12)):
    for _k, _c, _b, _a, _s, _m in _l:
        if _d[_k]:
            CARDS.append(sh(_d[_k], _c, _b, _a, _s, _m))

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak-hidrossoluvel": "- Barium leaking into the mediastinum or peritoneum is harmful; iodine is absorbed",
 "ak-mrcp": "- The bile itself is the contrast on heavily T2-weighted images",
 "ak-uro-tc": "- It replaced excretory urography (IV iodine + abdominal X-ray), now in disuse",
 "ak-vcug": "- Iodinated contrast through the urethra, filmed while the patient voids",
 "ak-uretrografia": "- Iodinated contrast injected through the urethral meatus",
 "ak-hsg": "- Iodinated contrast injected through the cervix fills the uterus and the tubes",
 "ak-bico": "- Seen on the barium upper GI series (EED); in Brazil, Chagas megaesophagus",
 "ak-maca": "- On the double-contrast barium enema",
 "ak-adrenalina": "- Facial angioedema can progress to glottic edema in minutes",
 "ak-cin": "- Described for iodine, not gadolinium; both are excreted by the kidneys",
 "ak-cin-risco": "- That is why creatinine clearance is checked before IV contrast",
 "ak-cin-hidratacao": "- Recent guidelines are more permissive about post-contrast kidney injury",
 "ak-jod-basedow": "- Very late reaction (weeks), in uncontrolled Graves disease or toxic nodules",
 "ak-litiase": "- Contrast would hide stones in the collecting system",
 "ak-colica": "- First imaging test: non-contrast CT",
 "ak-colica-obstrucao": "- The case: 28-year-old with sudden left flank pain and positive Giordano sign",
 "ak-litiase-complica": "- Pyelonephritis on CT: kidney areas that fail to enhance in the venous and excretory phases",
 "ak-litiase-us": "- US is good for collecting-system dilation, moderate for the stone itself",
 "ak-cistografia": "- CT cystography: iodinated contrast filling the bladder through the catheter",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "regra ou fato sem estrutura a reconhecer; as figuras que ensinam (enema com duplo contraste, microbolhas, angio-RM, escala de reações) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria aula, sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "rd56-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "rd56-enema.jpg": "Lâmina 10: enema opaco com duplo contraste (cólon inteiro, detalhe do sigmoide com divertículos) e esquema da sonda retal; verso de au-duplo.",
 "rd56-microbolhas.jpg": "Lâmina 26: esquema de microbolhas entre hemácias no capilar (1–3 µm × hemácia 6 µm); verso de au-microbolhas.",
 "rd56-angiorm.jpg": "Lâmina 31: angio-RM arterial intracraniana sem contraste, arterial extracraniana e venosa com contraste; verso de au-tof.",
 "rd56-reacoes.jpg": "Lâmina 33: escala de gravidade das reações (urticária, angioedema, broncoespasmo, edema de glote, choque, PCR); verso de au-reacoes.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Saber para que servem os meios de contraste, qual contraste intracavitário e intravascular cada método usa (bário só no "
             "tubo digestivo, iodo, água, gadolínio, microbolhas), os exames contrastados principais e a segurança: gravidade das "
             "reações, clearance < 30, nefropatia pelo iodo e fibrose nefrogênica pelo gadolínio.",
 "centrais": [
   ("intracavitário", "au-bario", "au-duplo"),
   ("intravascular", "sh-1792141769157", "au-microbolhas"),
   ("segurança", "au-reacoes", "au-clearance", "ak-cin"),
 ],
 "exemplos": ["casos de cólica renal, pielonefrite e politrauma", "imagens normais de EED, enema e urografia", "Lancet 2000 (fibrose nefrogênica)"],
 "outras_aulas": [("contraste de cada método e angiografia", "02 Diagnóstico radiológico (sh)"), ("fases do contraste na TC", "05 TC (vaga RD05)"),
                  ("gadolínio e fibrose nefrogênica", "12 RM (vagas RD12)"), ("megaesôfago chagásico", "UC08 (sh)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
