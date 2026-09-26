import re, fitz, os
from PIL import Image
os.makedirs('img', exist_ok=True)
doc = fitz.open('slide.pdf')
M = {'particulado': 37, 'primarios': 35, 'londres': 20, 'iceberg': 22, 'oms': 34, 'mecanismos-sistemicos': 45, 'ldl': 44, 'biomassa': 50}
for k, p in M.items():
    fn = f'img/nebli-ambiental-{k}.png'
    doc[p - 1].get_pixmap(dpi=110).save(fn)
    im = Image.open(fn).convert('RGB')
    if im.width > 760:
        im = im.resize((760, int(im.height * 760 / im.width)))
    im.save(fn, optimize=True)

s = open('../deck-aula-grand-round-2-2026-09-24/prepare.py', encoding='utf-8').read()
a = s.index('AUTHORED=['); b = s.index("ROSA_AUTH=")
new = '''AUTHORED=[
 ('amb-particulado','Particulate matter is classed by aerodynamic diameter (PM10, PM2.5, ultrafine); the smaller the particle, the {{c1::deeper}} it reaches in the airways',
  'Partículas grandes param por impactação nas vias altas; as médias sedimentam nos brônquios; as ultrafinas chegam ao alvéolo por difusão (movimento browniano). Composição: nitratos, sulfatos, metais e HPA. Fontes: solo, vulcões e florestas; transporte, indústria e combustão incompleta.','P-particulado','particulado'),
 ('amb-secundario','Ozone is a {{c1::secondary}} pollutant: it forms in the air from NOx and hydrocarbons under sunlight, rather than being emitted directly',
  'Primários (emitidos pela fonte): material particulado, CO, NOx, SO₂, HPA, metais. Secundários (formados na atmosfera): O₃, H₂SO₄ e sulfatos de amônio.','P-poluentes','primarios'),
 ('amb-londres','The London fog of December 1952 killed about 4,000 people in one week, proof that {{c1::air pollution}} can kill acutely',
  'Mais de 8.000 em três semanas. As mortes subiram junto com a concentração de fumaça, dia a dia (Logan, Lancet 1953).','H-historia','londres'),
 ('amb-iceberg','Health effects of pollution form a pyramid: deaths at the top, then admissions and visits, and {{c1::subclinical inflammation}} in most exposed people at the base',
  'Quanto mais grave o desfecho, menos pessoas afetadas. Medir só mortalidade subestima o problema.','H-efeitos','iceberg'),
 ('amb-oms','São Paulo\\u2019s mean PM2.5 (~28 µg/m³) is well above the WHO annual guideline, which was {{c1::10 µg/m³}} (tightened to 5 in 2021)',
  'Na aula: outras metrópoles brasileiras com 16 e 20 µg/m³. Nos EUA, a mortalidade ajustada sobe linearmente com o PM2.5 (Pope, 2000), sem limiar seguro evidente.','H-megacidades','oms'),
 ('amb-sistemico','Inhaled particles cause oxidative stress and lung inflammation that spill into the blood, causing endothelial dysfunction, platelet activation and {{c1::plaque instability}}',
  'Daí o aumento de infarto e AVC nos dias de poluição alta. Partículas ultrafinas também podem atravessar a barreira epitelial e chegar à circulação.','S-sistemico','mecanismos-sistemicos'),
 ('amb-ldl','In animal studies, polluted air increased {{c1::LDL oxidation}} and atherosclerotic plaque thickness without raising the plaque lipid content',
  'Também aumentou autoanticorpos contra LDL oxidada. É o elo entre poluição e doença coronariana.','S-aterosclerose','ldl'),
 ('amb-biomassa','Biomass smoke (e.g., indoor wood stoves) impairs {{c1::mucociliary clearance}} and alveolar macrophage activity, favoring respiratory infections',
  'Também: irritação química (olhos, coriza), menos antioxidantes, reações oxidativas, IL-6 e IL-8 elevadas com recrutamento de granulócitos, inflamação crônica, sibilância e queda da função pulmonar (DPOC). Gases indoor: CO, metano, NO₂.','M-biomassa','biomassa'),
]
'''
s = s[:a] + new + s[b:]
s = s.replace("ROSA_AUTH=set()", "ROSA_AUTH={'amb-londres','amb-oms'}")
s = s.replace("LESSON='2026-uc03-grand-round-21-grand-round-2-diabetes'", "LESSON='2026-uc03-patologia-24-patologia-ambiental'")
s = s.replace("DECK='NEBLI::UC03::P2::Grand Round::Grand Round 2 (diabetes mellitus)'", "DECK='NEBLI::UC03::P2::Patologia::Patologia ambiental'")
s = s.replace("SLIDE='Fonte: slides do Grand Round 2 — Diabetes mellitus (UC03)'", "SLIDE='Fonte: slides da aula de Patologia ambiental (UC03, Prof. Luiz Fernando Ferraz da Silva)'")
s = re.sub(r"IMGS=\[[^\]]*\]", "IMGS=" + repr(list(M)), s)
s = s.replace("nebli-gr2-", "nebli-ambiental-").replace("'lesson_date':'2026-09-29'", "'lesson_date':'2026-09-03'")
assert 'ROSA_AUTH={' in s and "LESSON='2026-uc03-patologia-24" in s
open('prepare.py', 'w', encoding='utf-8').write(s)
ap = open('../deck-aula-grand-round-2-2026-09-24/apply.py', encoding='utf-8').read().replace("'Grand Round 2 (diabetes mellitus).apkg'", "'Patologia ambiental.apkg'")
open('apply.py', 'w', encoding='utf-8').write(ap)
print('ok')
