# Figuras para os cards de estrutura (F-20261003-CLAUDE-15: livro/AnKing, slide não). Moore (bibliografia da UC08),
# extraídas para arquivos-trabalho/livros/moore-figs e vistas em scratchpad/moore-an07.png.
NOMES = ("5-41", "5-54", "5-56", "5-75", "5-101", "6-32")
LIVRO = {f"nebli-moore-fig-{n}.png": f"../livros/moore-figs/nebli-moore-fig-{n}.png" for n in NOMES}
F541, F554, F556, F575, F5101, F632 = (f"nebli-moore-fig-{n}.png" for n in NOMES)
IMAGENS = {
 "porta-formacao": F541, "vmi-esplenica": F541,                     # 5.41: veias esplênica e mesentéricas formam a porta
 "porta-territorio": F575, "varizes-anorretais": F575,              # 5.75: tributárias da porta e anastomoses portossistêmicas
 "cisterna-troncos": F5101, "ln-pre-aorticos": F5101,               # 5.101: linfonodos pré-aórticos, troncos, cisterna do quilo
 "pd-inferior-ams": F554, "ileocolica-territorio": F554, "colica-direita-territorio": F554, "colica-media-territorio": F554,
 "ami-ramos": F554, "colica-esquerda-territorio": F554, "marginal": F554,   # 5.54: ramos da AMS e AMI, artéria marginal
 "retal-media": F632,                                               # 6.32: artérias e veias do reto
 "reto-linfa": F556,                                                # 5.56: linfonodos do intestino grosso
}
SEM_IMAGEM = {}
