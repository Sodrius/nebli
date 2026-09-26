import re, fitz, os
from PIL import Image
os.makedirs('img', exist_ok=True)
doc = fitz.open('slide.pdf')
M = {'c1q': 11, 'alternativa': 22, 'properdina': 23, 'lectinas': 28, 'receptores': 36, 'fatores-ih': 51, 'cd59': 53, 'deficiencias': 54}
for k, p in M.items():
    fn = f'img/nebli-complemento-{k}.png'
    doc[p - 1].get_pixmap(dpi=110).save(fn)
    im = Image.open(fn).convert('RGB')
    if im.width > 760:
        im = im.resize((760, int(im.height * 760 / im.width)))
    im.save(fn, optimize=True)

s = open('../deck-aula-patologia-ambiental-2026-09-24/prepare.py', encoding='utf-8').read()
a = s.index('AUTHORED=['); b = s.index("ROSA_AUTH=")
new = '''AUTHORED=[
 ('comp-c1q','To start the classical pathway, C1q must bind at least {{c1::two}} antigen-bound IgG molecules (or a single pentameric IgM)',
  'C1q ativa C1r, que ativa C1s; C1s cliva C4 e C2 e forma a C3 convertase clássica (C4b2a na aula). Ig: IgG pela região CH2, IgM pela CH3.','V-classica','c1q'),
 ('comp-tickover','The alternative pathway starts with slow spontaneous hydrolysis of C3 into {{c1::C3(H2O)}}, which binds factor B for factor D to cleave',
  'Forma-se C3(H2O)Bb, uma convertase em fase fluida que gera os primeiros C3b. O C3b que cai numa superfície de micróbio (sem reguladores) amplifica a via: C3bBb.','V-alternativa','alternativa'),
 ('comp-properdina','{{c1::Properdin}} stabilizes the alternative-pathway C3 convertase (C3bBb) on microbial surfaces',
  'É o único regulador positivo do complemento. Deficiência de properdina, como de C3, fator D, H e I, aparece na aula entre as deficiências da via alternativa (infecções por Neisseria, pneumococo e Haemophilus).','V-alternativa','properdina'),
 ('comp-masp','In the lectin pathway, mannose-binding lectin bound to microbial sugars activates {{c1::MASP-1/MASP-2}}, which cleave C4 and C2 as C1s does',
  'A MBL é estruturalmente parecida com C1q. Reconhece manose e N-acetilglicosamina na superfície dos patógenos, sem anticorpo.','V-lectinas','lectinas'),
 ('comp-fatores-ih','Factor {{c1::I}} inactivates C3b (to iC3b, then C3dg), using factor H as its cofactor',
  'O mesmo sistema degrada C4b (C4c + C4d). Deficiência de fator H ou I deixa a via alternativa sem freio: consumo de C3, infecções piogênicas e doenças por imunocomplexos (glomerulonefrite, SHU atípica).','R-regulacao','fatores-ih'),
 ('comp-cd59','CD59 protects host cells by preventing {{c1::C9 polymerization}}, so the membrane attack complex cannot form',
  'Ancorado por GPI, como o DAF (CD55). Sem os dois, as hemácias sofrem lise pelo complemento: hemoglobinúria paroxística noturna.','R-regulacao','cd59'),
 ('comp-cr3','iC3b-coated microbes are phagocytosed through {{c1::CR3 (CD11b/CD18)}} and CR4 on phagocytes',
  'CR1 (CD35) liga C3b/C4b: fagocitose, transporte de imunocomplexos pelas hemácias até fígado e baço e cofator do fator I. CR2 (CD21) liga C3d e é correceptor do linfócito B.','F-opsonizacao','receptores'),
 ('comp-c3','C3 deficiency, which affects both classical and alternative pathways, causes severe recurrent {{c1::pyogenic}} infections and immune-complex disease',
  'Sem C3 não há opsonização por C3b, nem convertase C5, nem MAC. Nas questões da UC: criança com infecções bacterianas de repetição e C3 baixo; C3 baixo com síntese normal sugere consumo (falta de fator H ou I).','D-deficiencias','deficiencias'),
]
'''
s = s[:a] + new + s[b:]
s = s.replace("ROSA_AUTH={'amb-londres','amb-oms'}", "ROSA_AUTH=set()")
s = s.replace("LESSON='2026-uc03-patologia-24-patologia-ambiental'", "LESSON='2026-uc03-imunologia-31-sistema-complemento'")
s = s.replace("DECK='NEBLI::UC03::P2::Patologia::Patologia ambiental'", "DECK='NEBLI::UC03::P2::Imunologia::Sistema complemento'")
s = s.replace("SLIDE='Fonte: slides da aula de Patologia ambiental (UC03, Prof. Luiz Fernando Ferraz da Silva)'", "SLIDE='Fonte: slides da aula de Sistema complemento (UC03)'")
s = re.sub(r"IMGS=\[[^\]]*\]", "IMGS=" + repr(list(M)), s)
s = s.replace("nebli-ambiental-", "nebli-complemento-").replace("'lesson_date':'2026-09-03'", "'lesson_date':'2026-09-08'")
assert "LESSON='2026-uc03-imunologia-31" in s
open('prepare.py', 'w', encoding='utf-8').write(s)
ap = open('../deck-aula-patologia-ambiental-2026-09-24/apply.py', encoding='utf-8').read().replace("'Patologia ambiental.apkg'", "'Sistema complemento.apkg'")
open('apply.py', 'w', encoding='utf-8').write(ap)
print('ok')
