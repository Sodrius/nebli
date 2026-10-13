# Recortes das notas do Histology da FI08 (F-20261003-CLAUDE-14, 03/10/2026): uma frase, um fato, cloze de palavra inteira.
V, Z, R = 3, 4, 5
CORTES = {
 "varicosidades": [
  ("dilatacoes", "Autonomic axons in smooth muscle release transmitter from periodic swellings called {{c1::varicosities}}", {1: Z}, "Varicosidades"),
  ("transmissores", "Varicosities release {{c1::acetylcholine}} or norepinephrine, which diffuse to many smooth muscle cells", {1: Z}, "ACh ou noradrenalina"),
 ],
 "juncoes-comunicantes": [
  ("sincronia", "Excitation spreads between smooth muscle cells through {{c1::gap junctions}}, so they contract together", {1: V}, "Junções comunicantes"),
 ],
 "sem-troponina": [
  ("troponina", "Smooth muscle actin filaments lack {{c1::troponin}}; contraction starts through calmodulin and MLCK", {1: Z}, "Músculo liso sem troponina"),
 ],
}
