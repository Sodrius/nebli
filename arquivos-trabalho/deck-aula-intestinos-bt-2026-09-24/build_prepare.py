import re, fitz, os
from PIL import Image
os.makedirs('img', exist_ok=True)
doc = fitz.open('slide.pdf')
M = {'plica-vilo': 9, 'nicho': 15, 'linhagens': 14, 'wnt-bmp': 10, 'ki67-tunel': 13, 'celulas': 17, 'lacteo': 20, 'dcs': 32}
for k, p in M.items():
    fn = f'img/nebli-intestinos-{k}.png'
    doc[p - 1].get_pixmap(dpi=110).save(fn)
    im = Image.open(fn).convert('RGB')
    if im.width > 760:
        im = im.resize((760, int(im.height * 760 / im.width)))
    im.save(fn, optimize=True)

s = open('../deck-aula-complemento-2026-09-24/prepare.py', encoding='utf-8').read()
a = s.index('AUTHORED=['); b = s.index("ROSA_AUTH=")
new = '''AUTHORED=[
 ('bt4-plica','Plicae circulares are folds of mucosa plus {{c1::submucosa}}, whereas villi are projections of the mucosa only',
  'Três níveis de aumento de superfície: plica (mucosa + submucosa) > vilo (mucosa) > microvilo (membrana do enterócito). As criptas de Lieberkühn abrem-se entre os vilos.','E-superficie','plica-vilo'),
 ('bt4-lgr5','Actively cycling crypt base columnar stem cells are marked by {{c1::Lgr5}} (with Ascl2 and Olfm4)',
  'Na posição +4 ficam células-tronco de reserva, mais quiescentes (Bmi1, Hopx, Tert), que repõem as Lgr5+ após lesão.','N-nicho','nicho'),
 ('bt4-ta','Stem cell daughters first divide in the crypt as {{c1::transit-amplifying}} progenitors, then differentiate as they migrate up the villus',
  'Duas linhagens: absortiva (enterócitos) e secretora (caliciformes, enteroendócrinas, Paneth). As Paneth são a exceção: descem para a base da cripta.','N-nicho','linhagens'),
 ('bt4-wnt','High {{c1::Wnt}} signaling at the crypt base keeps stem cells proliferating, while BMP toward the villus drives differentiation',
  'O gradiente vem do mesênquima em volta da cripta (telócitos, fibroblastos). É o eixo cripta–vilo da aula.','N-nicho','wnt-bmp'),
 ('bt4-ki67','In the small intestine, Ki67 marks proliferating cells in the {{c1::crypts}}, while TUNEL marks apoptotic cells at the villus tip',
  'O epitélio se renova em poucos dias: nasce na cripta, sobe pelo vilo e é eliminado no ápice.','N-nicho','ki67-tunel'),
 ('bt4-paneth','Besides secreting lysozyme and antimicrobial peptides, Paneth cells form the {{c1::niche}} that supports Lgr5+ stem cells',
  'Ficam intercaladas com as células-tronco na base da cripta, com grânulos eosinofílicos apicais.','C-celulas','celulas'),
 ('bt4-vilina','The enterocyte brush border carries lactase and sucrase and is built on actin bundled by {{c1::villin}}',
  'Caliciforme: mucina 2 (MUC2). Enteroendócrina: hormônios que regulam digestão, metabolismo e apetite. Paneth: lisozima e peptídeos antimicrobianos.','C-celulas','celulas'),
 ('bt4-lacteo','The core of each villus holds a blind lymphatic capillary, the {{c1::central lacteal}}, which takes up chylomicrons',
  'Ao lado: capilares sanguíneos fenestrados (monossacarídeos e aminoácidos vão à veia porta), músculo liso e células imunes da lâmina própria.','E-superficie','lacteo'),
 ('bt4-dcs','In colonic crypts, deep crypt secretory cells play the role that {{c1::Paneth cells}} play in the small intestine, supporting stem cells',
  'O nicho colônico também recebe sinais da imunidade tecidual (IL-13 de ILC2).','G-grosso','dcs'),
]
'''
s = s[:a] + new + s[b:]
s = s.replace("ROSA_AUTH=set()", "ROSA_AUTH={'bt4-dcs'}")
s = s.replace("LESSON='2026-uc03-imunologia-31-sistema-complemento'", "LESSON='2026-uc08-biologia-tecidual-04-intestinos'")
s = s.replace("DECK='NEBLI::UC03::P2::Imunologia::Sistema complemento'", "DECK='NEBLI::UC08::P1::Biologia Tecidual::Intestinos'")
s = s.replace("SLIDE='Fonte: slides da aula de Sistema complemento (UC03)'", "SLIDE='Fonte: slides da aula de Intestinos (UC08, Profa. Patrícia Gama)'")
s = re.sub(r"IMGS=\[[^\]]*\]", "IMGS=" + repr(list(M)), s)
s = s.replace("nebli-complemento-", "nebli-intestinos-").replace("'lesson_date':'2026-09-08'", "'lesson_date':'2026-08-24'")
assert "LESSON='2026-uc08-biologia-tecidual-04" in s and "ROSA_AUTH={'bt4-dcs'}" in s
open('prepare.py', 'w', encoding='utf-8').write(s)
ap = open('../deck-aula-complemento-2026-09-24/apply.py', encoding='utf-8').read().replace("'Sistema complemento.apkg'", "'Intestinos.apkg'")
ap = ap.replace("'Cloze-Lightyear':'NEBLI AnKing independente - v3'}", "'Cloze-Lightyear':'NEBLI AnKing independente - v3',\n        'AnKingOverhaul (LLU Histology / SLin_LLUSOM)':'NEBLI UC08 Stomach LLU v1',\n        'Cloze-AnKingMaster-v3 (Histology / ploirodon)':'NEBLI UC08 Stomach Histology v1'}")
assert 'LLU Histology' in ap
open('apply.py', 'w', encoding='utf-8').write(ap)
print('ok')
