# Figuras do Robbins cap. 24 (bibliografia da UC03), extraídas em 03/10 para arquivos-trabalho/livros/robbins-figs,
# recortadas só na figura (sem legenda; F-20261003-CLAUDE-19) e vistas uma a uma (imagens-vistas.json).
NOMES = ("24-30", "24-31", "24-32", "24-33a", "24-33b", "24-34", "24-35", "24-37", "24-39")
LIVRO = {f"nebli-robbins-fig-{n}.png": f"../livros/robbins-figs/nebli-robbins-fig-{n}.png" for n in NOMES}
LIVRO.update({f"nebli-uc03-gr02-p47-{n}.png": f"visual/nebli-uc03-gr02-p47-{n}.png" for n in ("inicio", "fim")})
LIVRO["nebli-uc03-gr02-p57-t2fs.png"] = "visual/nebli-uc03-gr02-p57-t2fs.png"
F = {n: f"nebli-robbins-fig-{n}.png" for n in NOMES}
IMAGENS = {
 "cd8-dm1": F["24-30"],                                   # estágios do DM1: massa de células β cai antes da hiperglicemia
 "perda-peso-mecanismo": F["24-39"], "poliuria": F["24-39"],   # sequência de desarranjos metabólicos
 "insulina-dm2": F["24-31"],                              # compensação → falência das células β
 "insulite": F["24-33a"], "amilina": F["24-33b"],
 "mbg-primeira": F["24-35"],
 "mesangio": F["24-37"], "nodular": F["24-37"], "kimmelstiel": F["24-37"],
 "rim-inicio": "nebli-uc03-gr02-p47-inicio.png", "rim-final": "nebli-uc03-gr02-p47-fim.png",
 "osteo-sinal": "nebli-uc03-gr02-p57-t2fs.png",
 "iam-morte": F["24-32"],
}
