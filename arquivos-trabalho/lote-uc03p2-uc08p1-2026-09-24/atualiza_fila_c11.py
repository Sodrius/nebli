p = 'flashcards/projeto/FILA-UC03-P2-UC08-P1.md'
s = open(p, encoding='utf-8').read()
old = "| Harper | 3 | em andamento — 24/09/2026 (Claude) |"
assert old in s
s = s.replace(old, "| Harper | 3 | **instalado e sincronizado 24/09** (antes da aula) — 48 notas/53 cards novos: 45 AnKing, 8 autorais; 16 verdes, 6 rosas; + 15 notas da Integração II associadas; aguarda revisão |")
row = ("| 24/09 | Claude | Grand Round 2 (DM) | 48 notas/53 cards novos (45 AnKing, 8 autorais = 15%); 16 verdes, 6 rosas; 15 notas da Integração II associadas | "
       "Aula de caso, deck compacto. Slides (43 lâminas) + caso clínico (DM1 tardio/LADA). Entraram: AGEs/RAGE, nefropatia, retinopatia, catarata, neuropatia, pé diabético, Charcot, osteomielite, escore de cálcio, angioTC × cateterismo, AVC na TC, exames do caso (HbA1c, frutosamina, peptídeo C, anti-GAD), GLP-1, insulinas basal/rápida, glucagon na hipoglicemia grave. "
       "Fora: fármacos por classe, metas e critérios de síndrome metabólica, manejo de cetoacidose, aortopatia. O PDF \"Grand Round 2.pdf\" em outra pasta é o guia de 2025 (mesmo caso); não ampliou o recorte (imunologia do GAD/perforina não está nos slides de 2026) |\n")
anchor = "| 24/09 | Claude | Motilidade I (UC08) |"
s = s.replace(anchor, row + anchor, 1)
open(p, 'w', encoding='utf-8').write(s)
print('ok')
