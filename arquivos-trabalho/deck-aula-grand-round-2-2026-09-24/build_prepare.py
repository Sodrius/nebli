import re, fitz
from PIL import Image
import os
os.makedirs('img', exist_ok=True)
doc = fitz.open('slide.pdf')
M = {'glicacao': 15, 'rage': 19, 'nefro-us': 33, 'calcio': 35, 'angiotc': 38, 'charcot': 42, 'dm1': 5}
for k, p in M.items():
    fn = f'img/nebli-gr2-{k}.png'
    doc[p - 1].get_pixmap(dpi=110).save(fn)
    im = Image.open(fn).convert('RGB')
    if im.width > 760:
        im = im.resize((760, int(im.height * 760 / im.width)))
    im.save(fn, optimize=True)

s = open('../deck-aula-motilidade-ii-2026-09-24/prepare.py', encoding='utf-8').read()
a = s.index('AUTHORED=['); b = s.index("ROSA_AUTH=")
new = '''AUTHORED=[
 ('gr2-ages','Persistent hyperglycemia glycates proteins without enzymes: reversible Schiff bases become Amadori products and finally irreversible {{c1::advanced glycation end products (AGEs)}}',
  'É a base da maioria das complicações crônicas. AGEs no colágeno dificultam a cicatrização; LDL glicada é captada mais facilmente (aterosclerose); AGEs inativam o óxido nítrico e resistem à degradação proteica.','C-age','glicacao'),
 ('gr2-rage','AGEs binding their receptor {{c1::RAGE}} on monocytes and mesenchymal cells trigger cytokines, vascular leak and a procoagulant state',
  'Na aula: migração de monócitos, secreção de citocinas e fatores de crescimento, aumento da permeabilidade vascular, da atividade pró-coagulante, da proliferação celular e da matriz extracelular.','C-age','rage'),
 ('gr2-frutosamina','{{c1::Fructosamine}} (glycated albumin) reflects mean glucose over the last 2–3 weeks, a shorter window than HbA1c',
  'A HbA1c reflete cerca de 3 meses. A frutosamina serve quando a HbA1c pode estar falseada (hemoglobinopatias, hemólise) e para ver a resposta rápida ao tratamento, como no caso da aula (575 → 289 µmol/L).','L-exames','glicacao'),
 ('gr2-lada','Diabetes starting in an adult, with positive anti-GAD65 and still-detectable C-peptide, is autoimmune {{c1::LADA}} (latent type 1)',
  'Caso da aula: homem de 26 anos, IMC normal, poliúria/polidipsia, anti-GAD65 muito alto e peptídeo C ainda no normal (reserva de célula β). Tratado com insulina basal + bolus por contagem de carboidratos.','L-exames','dm1'),
 ('gr2-nefro-us','On ultrasound, diabetic kidneys are {{c1::enlarged}} early (hyperfiltration) and shrunken with a thin, echogenic cortex at end stage',
  'No estágio final perde-se também a diferenciação córtico-medular. Na histologia: espessamento da membrana basal, expansão mesangial e glomeruloesclerose.','R-nefro','nefro-us'),
 ('gr2-calcio','The coronary calcium score uses non-contrast, ECG-gated CT to quantify {{c1::calcified plaque}} and stratify risk in asymptomatic people',
  'Calcificação = área acima de 130 UH; o método de Agatston é a referência. Detecta aterosclerose subclínica, que tem longa fase assintomática.','R-coronarias','calcio'),
 ('gr2-angiotc','Coronary CT angiography has a negative predictive value near 100%, so it is best used to {{c1::rule out}} CAD in low- or intermediate-probability patients',
  'Usa contraste e radiação e quantifica mal as estenoses; lesão grave vai para o cateterismo. O cateterismo (angiocoronariografia invasiva) é o padrão-ouro e permite tratar.','R-coronarias','angiotc'),
 ('gr2-charcot','Diabetic neuropathy removes pain and proprioception, so repeated unnoticed trauma progressively destroys joints: {{c1::Charcot arthropathy}}',
  'Na radiografia: destruição e erosão articular, reabsorção óssea, osteófitos e esclerose desorganizada, típicas do médio e retropé. Diferencial com osteomielite (infecção da medular óssea), vista melhor na RM.','R-charcot','charcot'),
]
'''
s = s[:a] + new + s[b:]
s = s.replace("LESSON='2026-uc08-fisiologia-09-motilidade-absorcao-intestinal-ii'", "LESSON='2026-uc03-grand-round-21-grand-round-2-diabetes'")
s = s.replace("DECK='NEBLI::UC08::P1::Fisiologia::Motilidade e absorção intestinal II'", "DECK='NEBLI::UC03::P2::Grand Round::Grand Round 2 (diabetes mellitus)'")
s = s.replace("SLIDE='Fonte: slides da aula Motilidade do TGI (UC08, Profa. Fran Goulart da Silva)'", "SLIDE='Fonte: slides do Grand Round 2 — Diabetes mellitus (UC03)'")
s = re.sub(r"IMGS=\[[^\]]*\]", "IMGS=['glicacao','rage','nefro-us','calcio','angiotc','charcot','dm1']", s)
s = s.replace("nebli-motil-", "nebli-gr2-").replace("'lesson_date':'2026-09-28'", "'lesson_date':'2026-09-29'")
open('prepare.py', 'w', encoding='utf-8').write(s)
ap = open('../deck-aula-motilidade-ii-2026-09-24/apply.py', encoding='utf-8').read().replace("'Motilidade e absorção intestinal II.apkg'", "'Grand Round 2 (diabetes mellitus).apkg'")
open('apply.py', 'w', encoding='utf-8').write(ap)
print('ok')
