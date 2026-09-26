import re, fitz, os
from PIL import Image
os.makedirs('img', exist_ok=True)
doc = fitz.open('slide.pdf')
# (página do PDF, metade: 0 = de cima, 1 = de baixo)
M = {'tenias': (16, 0), 'apendice-posicao': (15, 0), 'labios': (11, 0), 'reto-sem-tenias': (21, 0), 'puborretal': (19, 1),
     'pectinada': (23, 1), 'esfincteres': (25, 0), 'seios': (22, 0), 'escavacao': (20, 0), 'mcburney': (14, 1)}
for k, (p, half) in M.items():
    page = doc[p - 1]; r = page.rect
    clip = fitz.Rect(r.x0, r.y0 + half * r.height / 2, r.x1, r.y0 + (half + 1) * r.height / 2)
    fn = f'img/nebli-intgrosso-{k}.png'
    page.get_pixmap(dpi=160, clip=clip).save(fn)
    im = Image.open(fn).convert('RGB')
    if im.width > 760:
        im = im.resize((760, int(im.height * 760 / im.width)))
    im.save(fn, optimize=True)

s = open('../deck-aula-patologia-ambiental-2026-09-24/prepare.py', encoding='utf-8').read()
a = s.index('AUTHORED=['); b = s.index("ROSA_AUTH=")
new = '''AUTHORED=[
 ('intg-tenias','The three taeniae coli, bands of longitudinal muscle, are the mesocolic, omental and {{c1::free}} taenia',
  'Mesocólica: na borda de inserção do mesocolo; omental: onde se prende o omento maior no colo transverso; livre: sem inserção. Vão do ceco até o início do reto; como são mais curtas que a parede, formam os haustros (saculações).','C-caracteristicas','tenias'),
 ('intg-apendice','The vermiform appendix (6–10 cm, rich in lymphoid tissue) most often lies in a {{c1::retrocecal}} position',
  'Na aula: retrocecal ~64%, pélvico ~34%, pré e pós-ileal raros. As três tênias convergem na base do apêndice.','I-apendice','apendice-posicao'),
 ('intg-labios','The ileocecal valve is formed by the ileocecal and {{c1::ileocolic}} lips around the ileal orifice (ileal papilla)',
  'A papila ileal é a projeção do íleo terminal dentro do ceco. Abaixo dela fica o óstio do apêndice.','I-ileocecal','labios'),
 ('intg-reto','Unlike the colon, the rectum has no {{c1::taeniae, haustra or epiploic appendages}}',
  'O reto (~15 cm) vai do colo sigmoide ao canal anal, com flexura sacral, pregas transversas e ampola retal.','R-reto','reto-sem-tenias'),
 ('intg-puborretal','The {{c1::puborectalis}} sling pulls the anorectal junction forward, creating the anorectal flexure that helps keep continence',
  'Na defecação o puborretal relaxa e a junção anorretal se retifica. Faz parte do músculo levantador do ânus.','R-reto','puborretal'),
 ('intg-escavacao','In men the rectum is separated from the bladder by the {{c1::rectovesical}} pouch; in women, from the uterus by the rectouterine pouch',
  'São os pontos mais baixos da cavidade peritoneal em cada sexo, onde líquido e pus se acumulam.','R-reto','escavacao'),
 ('intg-pectinada','The pectinate line separates the endoderm-derived upper anal canal from the {{c1::ectoderm}}-derived lower canal',
  'Acima: inervação visceral, drenagem para linfonodos ilíacos internos, vasos retais superiores. Abaixo: inervação parietal (somática), linfonodos inguinais, vasos retais inferiores.','A-pectinada','pectinada'),
 ('intg-seios','The small mucus-secreting recesses between the anal columns are the anal {{c1::sinuses}}, closed below by the anal valves',
  'As colunas anais contêm ramos dos vasos retais superiores (plexo venoso interno). A linha branca (anocutânea) fica abaixo da pectinada.','A-canal','seios'),
 ('intg-esfincteres','The internal anal sphincter is {{c1::smooth}} muscle (involuntary), while the external anal sphincter is skeletal muscle (voluntary)',
  'O interno é o espessamento da camada circular do reto. O externo trabalha com o puborretal/levantador do ânus. Funções do canal anal: continência, retenção e expulsão do bolo fecal.','A-canal','esfincteres'),
 ('intg-mcburney','McBurney\\u2019s point, the surface projection of the appendix base, lies one-third of the way from the {{c1::anterior superior iliac spine}} to the umbilicus',
  'Na apendicite, a dor periumbilical migra para esse ponto na fossa ilíaca direita.','I-apendice','mcburney'),
]
'''
s = s[:a] + new + s[b:]
s = s.replace("ROSA_AUTH={'amb-londres','amb-oms'}", "ROSA_AUTH=set()")
s = s.replace("LESSON='2026-uc03-patologia-24-patologia-ambiental'", "LESSON='2026-uc08-anatomia-02-intestino-grosso-canal-anal'")
s = s.replace("DECK='NEBLI::UC03::P2::Patologia::Patologia ambiental'", "DECK='NEBLI::UC08::P1::Anatomia::Intestino grosso e canal anal'")
s = s.replace("SLIDE='Fonte: slides da aula de Patologia ambiental (UC03, Prof. Luiz Fernando Ferraz da Silva)'", "SLIDE='Fonte: slides da aula de Intestino grosso e canal anal (UC08, Profa. Patricia Castelucci)'")
s = re.sub(r"IMGS=\[[^\]]*\]", "IMGS=" + repr(list(M)), s)
s = s.replace("nebli-ambiental-", "nebli-intgrosso-").replace("'lesson_date':'2026-09-03'", "'lesson_date':'2026-08-10'")
# AnatoKing: mesma transformação do X3 do Codex (frente = 1ª imagem de cadáver; resto vazio)
old = "        elif e[0]=='set': f[e[1]]=e[2]"
assert old in s
s = s.replace(old, old + """
        elif e[0]=='anato':
            imgs=re.findall(r'<img[^>]+>',f.get('Cadaver','') or f.get('Illustration','') or f.get('Model','') or f.get('Imaging',''))
            if not imgs: raise RuntimeError(f'Sem imagem AnatoKing {n["noteId"]}')
            f={k:('Identify the highlighted structure' if k=='Header' else imgs[0] if k=='Cadaver' else f[k] if k=='Text' else '') for k in f}""", 1)
assert "LESSON='2026-uc08-anatomia-02" in s and 'anato' in s
open('prepare.py', 'w', encoding='utf-8').write(s)
ap = open('../deck-aula-patologia-ambiental-2026-09-24/apply.py', encoding='utf-8').read().replace("'Patologia ambiental.apkg'", "'Intestino grosso e canal anal.apkg'")
ap = ap.replace("'Cloze-Lightyear':'NEBLI AnKing independente - v3'}", "'Cloze-Lightyear':'NEBLI AnKing independente - v3',\n        'AnatoKingOverhaul V2':'NEBLI UC08 AnatoKing V2 v1',\n        'Cloze-b12d6':'NEBLI UC08 Visceral Dorian Cloze v1'}")
assert 'AnatoKingOverhaul V2' in ap
open('apply.py', 'w', encoding='utf-8').write(ap)
print('ok')
