import re, os
from PIL import Image
os.makedirs('img', exist_ok=True)
M = {'prr': 'p07-0', 'tlr': 'p08-0', 'acido-urico': 'p10-0', 'microcirculacao': 'p12-0', 'fagocitose': 'p17-0', 'neurogenica': 'p20-0', 'resumo': 'p28-0', 'quimiocinas': 'p15-1'}
for k, f in M.items():
    im = Image.open(f'e1img/{f}.png').convert('RGB')
    if im.width > 760:
        im = im.resize((760, int(im.height * 760 / im.width)))
    im.save(f'img/nebli-inflam-{k}.png', optimize=True)

s = open('../deck-aula-complemento-2026-09-24/prepare.py', encoding='utf-8').read()
a = s.index('AUTHORED=['); b = s.index("ROSA_AUTH=")
new = '''AUTHORED=[
 ('inflam-pamp','Innate pattern recognition receptors are germline-encoded and recognize conserved microbial motifs called {{c1::PAMPs}}',
  'Especificidade limitada. Podem ser solúveis (PCR, MBL, complemento, IgM natural), de membrana (TLR, lectinas tipo C, scavengers) ou citoplasmáticos (NOD, RIG-I).','P-prr','prr'),
 ('inflam-tlr','Toll-like receptors: TLR4 senses {{c1::LPS}}, TLR5 senses {{c2::flagellin}}, and TLR3 senses viral {{c3::double-stranded RNA}}',
  'TLR2 (com TLR1/6): Gram-positivos e fungos. TLR7/8: RNA viral de fita simples. TLR9: DNA bacteriano (CpG). São 11 em humanos.','P-tlr','tlr'),
 ('inflam-endossomo','The nucleic-acid-sensing TLRs (TLR3, 7, 8 and 9) sit in {{c1::endosomes}}, not on the plasma membrane',
  'Assim encontram o material genético de micróbios fagocitados. Os que reconhecem componentes de parede (TLR1/2/4/5/6) ficam na membrana plasmática.','P-tlr','tlr'),
 ('inflam-citosol','In the cytosol, NOD-like receptors detect bacterial products, while {{c1::RIG-I}} detects viral RNA',
  'NOD, NALP e NAIP reconhecem produtos de bactérias Gram-positivas e negativas. A via TLR/MyD88 converge em NF-κB, que liga genes de citocinas, quimiocinas e moléculas de adesão.','P-prr','prr'),
 ('inflam-damp','Sterile injury triggers inflammation through {{c1::DAMPs}}, such as uric acid crystals or heat-shock proteins released by damaged cells',
  'Na aula: o cristal de ácido úrico ativa o inflamassoma (NLRP3), que libera IL-1β. Dano, isquemia e necrose também ativam TLR4.','P-inflamassoma','acido-urico'),
 ('inflam-vascular','In acute inflammation, a brief arteriolar {{c1::vasoconstriction}} is followed by arteriolar vasodilation and increased venular permeability',
  'Depois: saída de líquido (exsudato), hemoconcentração e estase, que favorecem a marginação e a adesão dos leucócitos.','A-vascular','microcirculacao'),
 ('inflam-net','Activated neutrophils can extrude DNA decorated with granule proteins as {{c1::NETs}}, which trap and kill microbes',
  'Ativação completa do neutrófilo: fagocitose, explosão oxidativa (espécies reativas de O₂), degranulação e NETs.','L-fagocitose','fagocitose'),
 ('inflam-neurogenica','Sensory nerve endings release neuropeptides that activate mast cells and dilate vessels: {{c1::neurogenic}} inflammation',
  'Estimulação antidrômica de fibras sensitivas: vasodilatação, aumento da permeabilidade e edema, sem agente infeccioso.','M-neurogenica','neurogenica'),
 ('inflam-mastocito','Mast cells release preformed {{c1::histamine and serotonin}} from granules, then newly synthesized lipid mediators and cytokines',
  'A histamina age em receptores H1 a H4. Os mediadores lipídicos (prostaglandinas, leucotrienos, PAF) e as citocinas são sintetizados após a ativação.','C-mastocito','resumo'),
 ('inflam-eotaxina','Eosinophils are recruited mainly by {{c1::eotaxin}} (with PAF and LTB4), while neutrophils follow IL-8 and LTB4',
  'Na cinética da aula: neutrófilos primeiro, macrófagos em 12–48 h, eosinófilos (inflamação alérgica) e linfócitos após ~72 h.','L-migracao','quimiocinas'),
]
'''
s = s[:a] + new + s[b:]
s = s.replace("ROSA_AUTH=set()", "ROSA_AUTH={'inflam-endossomo'}")
s = s.replace("LESSON='2026-uc03-imunologia-31-sistema-complemento'", "LESSON='2026-uc03-imunologia-37-inflamacao-inicio-resolucao'")
s = s.replace("DECK='NEBLI::UC03::P2::Imunologia::Sistema complemento'", "DECK='NEBLI::UC03::P2::Imunologia::Inflamação: início e resolução'")
s = s.replace("SLIDE='Fonte: slides da aula de Sistema complemento (UC03)'", "SLIDE='Fonte: slides da aula de Inflamação: início e resolução (UC03)'")
s = re.sub(r"IMGS=\[[^\]]*\]", "IMGS=" + repr(list(M)), s)
s = s.replace("nebli-complemento-", "nebli-inflam-").replace("'lesson_date':'2026-09-08'", "'lesson_date':'2026-09-17'")
assert "LESSON='2026-uc03-imunologia-37" in s
open('prepare.py', 'w', encoding='utf-8').write(s)
ap = open('../deck-aula-complemento-2026-09-24/apply.py', encoding='utf-8').read().replace("'Sistema complemento.apkg'", "'Inflamação início e resolução.apkg'")
open('apply.py', 'w', encoding='utf-8').write(ap)
print('ok')
