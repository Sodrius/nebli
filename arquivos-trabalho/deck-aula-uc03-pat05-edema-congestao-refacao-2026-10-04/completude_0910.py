"""F-20261009-CLAUDE-02 ("aula de pato também acho que algumas coisas fugiram"): revisão do Edema contra a base (16 lâminas vistas,
apostila de veteranos aula 6 pp. 31–32, monitoria P1 aula 6, Robbins cap. 4 pp. 111–114, provas). Roda sobre spec-antes-completude.py.

- Sai o que veio do material NEBLI de Davi (fontes/exercicios-etapas-1-3 é a apostila NEBLI, não exercício da aula): GNPE e a vinheta
  de nefrite aguda; sai a estenose mitral (exemplo fora da aula). Leucotrienos C4–E4 descem a rosa (a lâmina 13 só cita "leucotrienos").
- Numeração corrigida pelas lâminas vistas: 12 = ascite e noz-moscada; 13 = diagrama do dano alveolar; 14 = edema hidrostático
  (transudato pálido, capilares congestos); 15 = edema por permeabilidade (exsudato, membranas hialinas). O card "s13" usava o diagrama.
- Extra do AnKing volta a valer (a versão Codex o substituía por "On slide N..."); a nota da aula entra como acréscimo, sem citar lâmina.
- Entram: derrame, empiema, edema generalizado × localizado, linfedema por filariose e pós-mastectomia, ducto torácico, PBE e síndrome
  hepatorrenal (apostila, monitoria e lâminas 4, 7, 11).
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
s = (HERE / "spec-antes-completude.py").read_text()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep('    "starling"\n}]', '    "starling", "psgn-edema", "nefrite-aguda-anasarca", "hipertensao-venosa-pulmonar"\n}]')
rep('ak("leucotrienos-permeabilidade",1487640108934,{1:Z}', 'ak("leucotrienos-permeabilidade",1487640108934,{1:R}')
rep('"Azul: mediador indicado no esquema da lâmina e na prova antiga."', '"Rosa: a lâmina 13 só cita leucotrienos entre os produtos dos neutrófilos; o tipo (C4–E4) é detalhe."')
# lâmina 15: edema por permeabilidade (exsudato com membranas hialinas); o card s13 passa a usar a imagem certa
rep("""au("morfologia-pulmonar-s13", '<img src="nebli-pat05-refacao-s13.png"><br>The pink fluid occupying alveolar spaces represents {{c1::pulmonary edema}}', {1:Z}, D,
   "Reconhecer edema alveolar no corte histológico do slide 13",13,""",
    """au("morfologia-pulmonar-s13", '<img src="nebli-pat05-refacao-s15.png"><br>Protein-rich alveolar exudate with {{c1::hyaline membranes}} marks edema from increased permeability', {1:V}, D,
   "Reconhecer edema por permeabilidade (exsudato, membranas hialinas) no corte da lâmina 15",15,""")
rep('"Azul: reconhecimento microscópico ensinado diretamente na lâmina.",\n   extra="Alveolar air spaces become filled by eosinophilic edema fluid, reducing the space available for gas exchange."),',
    '"Verde: contraste da monitoria (hidrostático = transudato pálido; permeabilidade = exsudato e membranas hialinas).",\n   extra="Many cells and hyaline membranes at the alveolar walls, unlike the pale, cell-poor fluid of hydrostatic edema"),')
rep("""au("morfologia-pulmonar-s14", '<img src="nebli-pat05-refacao-s14.png"><br>Engorged septal capillaries indicate {{c1::pulmonary congestion}}', {1:Z}, D,
   "Reconhecer congestão capilar pulmonar no corte do slide 14",14,""",
    """au("morfologia-pulmonar-s14", '<img src="nebli-pat05-refacao-s14.png"><br>Pale, cell-poor fluid filling alveoli around engorged septal capillaries is {{c1::hydrostatic}} pulmonary edema', {1:V}, D,
   "Reconhecer edema hidrostático (transudato) com congestão no corte da lâmina 14",14,""")
rep('"Azul: separa sangue retido no vaso de líquido no alvéolo.",\n   extra="Congestion expands septal capillaries with erythrocytes; associated alveolar fluid may coexist."),',
    '"Verde: imagem da monitoria (líquido pobre e claro, capilares dilatados).",\n   extra="Congested capillaries hold the blood; the alveoli hold the transudate"),')

NOVOS = '''
ak("empiema",1474503790995,{1:Z,2:R},A,"Empiema (piema): pus na pleura",3,"Azul: termo da monitoria para exsudato purulento na cavidade pleural."),
au("derrame", "Edema fluid that collects in a body cavity rather than the interstitium is called an {{c1::effusion}}", {1:Z}, A, "Derrame em cavidade", "6; apostila veteranos aula 6; monitoria P1", [1474503771577,1474503781327],
   "Azul: apostila e monitoria (derrame pleural, pericárdico, peritoneal).", extra="- Blood in a cavity: hemothorax, hemopericardium, hemoperitoneum"),
au("edema-generalizado", "Edema from low plasma oncotic pressure is {{c1::generalized}}, whereas edema from venous obstruction is localized", {1:V}, C, "Oncótico generalizado × hidrostático localizado", "5; monitoria P1; apostila veteranos aula 6", [1475363769043,1471915101703],
   "Verde: contraste explícito da monitoria e da apostila.", extra="- Generalized edema settles in the legs over the day because of gravity"),
au("ducto-toracico", "Lymph returns to the blood through the {{c1::thoracic duct}}, which drains into the left subclavian vein", {1:R}, B, "Ducto torácico", 4, [1471466870844,1474503795880],
   "Rosa: rótulo do esquema da lâmina 4.", extra="- Lymph from most of the body ends there"),
ak("filariose",1509920166742,{1:Z,2:R},C,"Elefantíase por linfedema crônico (filariose)",7,"Azul: linfedema crônico (apostila); rosa: o parasita."),
au("linfedema-mastectomia", "Removal of axillary lymph nodes during breast cancer surgery can cause {{c1::lymphedema}} of the arm", {1:Z}, C, "Linfedema iatrogênico", 7, [1521170206006,1509920166742],
   "Azul: exemplo iatrogênico da apostila (mastectomia).", extra="- Iatrogenic: a complication of treatment, not necessarily an error"),

ak("hepatorrenal",1486522693430,{1:Z},C,"Síndrome hepatorrenal",11,"Azul: último quadro da cascata da lâmina 11."),
ak("pbe",1486591357720,{1:R},C,"Peritonite bacteriana espontânea na ascite",11,"Rosa: monitoria (translocação bacteriana no hepatopata soma permeabilidade)."),
ak("mixedema",1462223793144,{1:Z,2:V,3:Z},C,"Mixedema (hipotireoidismo)",7,"Verde c2 (HY 1): mixedema na Edema II (lâmina 19); azuis: GAG e hipotireoidismo."),
au("edema-mole-duro", "Transudate gives a soft, {{c1::pitting}} edema that shifts with gravity, whereas inflammatory exudate gives a firmer edema", {1:Z}, C, "Edema mole (cacifo) × duro", "7; Edema II 18", [1471915101703,1474512820505],
   "Azul: quadro transudato × exsudato da Edema II.", extra="- Exudate is richer in protein and cells, so the tissue is more viscous"),
ak("light",1495890671464,{1:Z},B,"Critério de Light: proteína pleural/sérica > 0,5",6,"Azul: análise do derrame pleural (Edema II, lâmina 22)."),
au("gsaa", "A serum-ascites albumin gradient of 1.1 g/dL or more points to {{c1::portal hypertension}}", {1:R}, C, "Gradiente soro-ascite de albumina", "12; Edema II 27", [1486522681611,1486591357720],
   "Rosa: avaliação laboratorial da ascite (Edema II).", extra="- The fluid is also checked for color, cell count, protein, LDH, glucose, amylase and AFB"),
au("underfill-overflow", "Cirrhotic ascites is explained by the {{c1::underfill}} theory (low effective volume) and the overflow theory (primary sodium retention), neither of which fits alone", {1:R}, C, "Teorias da ascite na cirrose", "12; Edema II 24–25", [1581191946613,1581193044398],
   "Rosa: discussão da Edema II.", extra="- RAAS and vasopressin rise, which overflow alone would not predict"),
au("edema-horario", "Edema worse in the {{c1::morning}}, around the eyes, suggests low oncotic pressure, while evening edema of the legs suggests a gravitational cause", {1:V}, D, "Anamnese: horário e localização", "16; Edema II 30", [1471915101703,1475363769043],
   "Verde: anamnese da Edema II (matutino = oncótico; vespertino = gravitacional).", extra="- The face swells first because its subcutaneous tissue is loose<br>- Fast onset suggests trauma; heart failure worsens over time"),
au("estase-jugular", "On examination, jugular venous {{c1::distension}} points to systemic venous congestion", {1:R}, D, "Exame físico: estase jugular", "16; Edema II 37", [1471914999950,1471447248110],
   "Rosa: último item do exame físico da Edema II.", extra="- Also check pitting, inflammatory signs, cavity effusions and heart and lung sounds"),
'''
rep('ak("cardiogenico-versus-permeabilidade",', NOVOS.strip("\n") + '\nak("cardiogenico-versus-permeabilidade",')

# numeração pelas lâminas vistas
s = s.replace('SLIDES = {\n', 'SLIDES = {\n    "congestao-hepatica": 12, "nutmeg-direita": 12, "lesao-alveolocapilar": 13, "membrana-hialina": 13,\n'
              '    "neutrofilos-lesao-alveolar": 13, "permeabilidade-capilar-edema": 13, "permeabilidade-exsudato": 13, "edema-proteico-ards": 13,\n'
              '    "cardiogenico-versus-permeabilidade": 13, "histamina-permeabilidade": 13, "bradicinina-permeabilidade": 13,\n'
              '    "leucotrienos-permeabilidade": 13, "contracao-endotelial": 13,\n', 1)
s = s.replace('"exsudato-proteina": 12,', '"exsudato-proteina": 13,').replace('    "congestao-hepatica": 11, "congestao-centrolobular": 11,\n', '')
s = s.replace('"congestao-hepatica": 11,\n    "congestao-centrolobular": 11, "figado-noz-moscada": 11,', '"congestao-hepatica": 12,\n    "congestao-centrolobular": 12, "figado-noz-moscada": 12, "nutmeg-direita": 12,')
s = s.replace('"lesao-alveolocapilar": 12, "membrana-hialina": 12, "neutrofilos-lesao-alveolar": 12,', '"lesao-alveolocapilar": 13, "membrana-hialina": 15, "neutrofilos-lesao-alveolar": 13,')
s = s.replace('"permeabilidade-capilar-edema": 12, "permeabilidade-exsudato": 12,', '"permeabilidade-capilar-edema": 13, "permeabilidade-exsudato": 13,')
s = s.replace('"cardiogenico-versus-permeabilidade": 12,', '"cardiogenico-versus-permeabilidade": 15,')
s = s.replace('"celulas-insuficiencia-cardiaca": 14,', '"celulas-insuficiencia-cardiaca": 14, "derrame": 6, "filariose": 7, "linfedema-mastectomia": 7,')

# Extras sem "slide N": nota curta da aula
NOTAS = {
 "edema": "Edema occupies the interstitium; in a body cavity it is called an effusion",
 "hidrotorax": "Often follows heart failure",
 "hidropericardio": "Often follows pericarditis",
 "ascite": "Often follows cirrhosis (portal hypertension plus low albumin)",
 "anasarca": "Seen in heart failure, nephrotic syndrome, cirrhosis and renal failure",
 "hiperemia-ativa": "Active and red (oxygenated blood), unlike passive congestion",
 "congestao": "Passive: venous blood backs up, as in heart failure or venous obstruction",
 "oncotica": "Albumin provides most of it; losing albumin lets water leave the vessels",
 "filtracao": "Hydrostatic pressure pushes fluid out at the arterial end",
 "reabsorcao": "Oncotic pressure pulls fluid back at the venous end",
 "linfa-retorno": "Whatever the veins do not reabsorb, the lymphatics take back",
 "gradiente-hidrostatico-capilar": "Filtration falls along the capillary as hydrostatic pressure drops",
 "transudato-proteina": "Intact endothelium: clear, cell-poor and protein-poor",
 "exsudato-proteina": "Damaged endothelium lets proteins and cells through",
 "hidrostatica": "Venous outflow obstruction raises upstream capillary pressure",
 "insuficiencia-esquerda": "Fluid backs up into the lungs: alveolar edema and hydrothorax",
 "insuficiencia-esquerda-congestao": "The lung lies upstream of the left ventricle",
 "insuficiencia-direita": "Liver and legs lie upstream of the right ventricle",
 "disfuncao-bomba": "Low forward output and venous backup happen together",
 "sodio-agua": "Retained sodium and water expand volume and feed the edema",
 "raas-insuficiencia-cardiaca": "The macula densa and carotid baroreceptors sense low flow as hypovolemia",
 "raas-agrava-edema": "A vicious circle: more volume, more congestion",
 "edema-pulmonar-venoso": "Pulmonary venous hypertension pushes a transudate into the alveoli",
 "sindrome-nefrotica": "Protein loss lowers oncotic pressure; renal sodium retention adds to it",
 "cirrose-edema": "Hepatic disease is mixed: portal hypertension plus low albumin",
 "hipertensao-portal-cirrose": "Portal hypertension raises hydrostatic pressure in the splanchnic bed",
 "ascite-portal": "Low albumin and sodium retention add to the portal pressure",
 "linfedema-obstrucao": "Fluid and protein stay in the interstitium despite an intact capillary",
 "permeabilidade-exsudato": "Inflammatory mediators loosen endothelial junctions",
 "edema-proteico-ards": "Diffuse alveolar damage: protein-rich edema with hyaline membranes",
 "permeabilidade-capilar-edema": "The injured alveolar-capillary barrier also thickens",
 "lesao-alveolocapilar": "Endothelium and pneumocytes are both injured",
 "membrana-hialina": "Protein-rich fluid and cell debris line the damaged alveoli",
 "congestao-hepatica": "Centrilobular blood backs up behind a failing right heart",
 "nutmeg-direita": "Dark congested centers alternate with paler liver tissue",
 "celulas-insuficiencia-cardiaca": "Chronic congestion leaks red cells; macrophages store their iron",
 "edema-pulmonar-rx": "Cephalization and Kerley B lines reflect interstitial edema",
 "transudato-hidrostatica": "The endothelium is intact, so the fluid stays protein-poor",
 "histamina-permeabilidade": "With bradykinin, the first mediator of inflammatory edema (minutes)",
 "bradicinina-permeabilidade": "Acts within minutes, with histamine",
 "leucotrienos-permeabilidade": "Released by neutrophils in diffuse alveolar damage",
 "retencao-renal-primaria": "Primary sodium retention expands plasma volume before any protein loss",
 "nefrite-retencao-sal": "Less sodium filtered, more volume, more capillary pressure",
 "nefrite-versus-nefrotica": "Nephrotic edema begins with protein loss instead",
 "vasodilatacao-esplancnica": "Effective arterial volume falls despite total body fluid excess",
 "raas-cirrose": "Perceived underfilling makes the kidney retain sodium and water",
 "cardiogenico-versus-permeabilidade": "Cardiogenic: pale transudate; non-cardiogenic: exudate with hyaline membranes",
 "filariose": "The worms block lymphatics; the limb becomes huge, firm and fibrotic",
 "contracao-endotelial": "Histamine and bradykinin act within minutes; wider endothelial gaps let proteins out as an exudate",
 "neutrofilos-lesao-alveolar": "Macrophages call in neutrophils (TNF, IL-8); their proteases and radicals break the barrier",
 "mixedema": "Not true edema: glycosaminoglycans hold water in the tissue (hypothyroidism)",
 "light": "Any of the three criteria (protein or LDH ratios) makes it an exudate",
 "derrame": "Pleural, pericardial or peritoneal; with blood it is hemothorax, hemopericardium, hemoperitoneum",
 "hepatorrenal": "Renal vasoconstriction from the same underfilling that drives ascites",
}
s = re.sub(r'\nEXTRAS = \{.*?\n\}\n', '\nEXTRAS = ' + repr(NOTAS).replace(", '", ",\n '") + '\n', s, flags=re.S)
rep('''    if key in EXTRAS:
        image_slide = VISUAL_IMAGES.get(key)
        card["extra"] = EXTRAS[key] + (f'<br><img src="nebli-pat05-refacao-s{image_slide:02d}.png">' if image_slide else "")''',
    '''    image_slide = VISUAL_IMAGES.get(key)
    image = f'<br><img src="nebli-pat05-refacao-s{image_slide:02d}.png">' if image_slide else ""
    if card["kind"] == "text":  # AnKing: mantém o Extra original; a nota da aula vem depois
        card.pop("extra", None)
        if key in EXTRAS or image:
            card["extra_add"] = (f"- {EXTRAS[key]}" if key in EXTRAS else "") + image
    elif key in EXTRAS and not key.startswith("morfologia-pulmonar-s"):
        card["extra"] = f"- {EXTRAS[key]}" + image''')
rep('''    if key == "morfologia-pulmonar-s14":
        card["extra_add"] = 'Slide 15 repeats the pulmonary pattern in paired histologic fields.<br><img src="nebli-pat05-refacao-s15.png">'
''', "")

# Extra original do AnKing do linfedema traz "Wikimedia Commons" no alt da imagem: cópia sem o alt
LINF = ('- Impaired removal of excess interstitial fluid leads to swelling &amp; pain<br>- Starts as pitting edema → progresses to nonpitting edema + firm, thickened skin<br>'
        '- Etiologies include <u>malignancy</u>, <u>iatrogenic</u> causes (lymph node dissection &amp; radiation), chronic <u>inflammation</u> (recurrent cellulitis), and severe <u>venous insufficiency</u>; obesity is also contributing factor<br>'
        '- Classic (but less common) cause is filariasis<br><img src="9756547cec1b9cf4476f5d2d6ef05076.png" width="541">')
s = s.replace('EXCLUIDOS=[]', 'for card in CARDS:\n    if card["key"] == "linfedema-obstrucao":\n        card["extra"] = ' + repr(LINF) + '\nEXCLUIDOS=[]', 1)
s = s.replace('EXCLUIDOS=[]', 'for card in CARDS:\n    if card["key"] == "linfedema-mastectomia":\n        card["duplicacao_ok"] = "ganho: a causa iatrogênica da apostila; o AnKing cobra a obstrução linfática em geral"\n    if card["key"] == "gsaa":\n        card["duplicacao_ok"] = "ganho: o exame do líquido que aponta a causa; o AnKing cobra a relação portal–ascite"\nEXCLUIDOS=[]', 1)
(HERE / "spec.py").write_text(s)
print("ok")
