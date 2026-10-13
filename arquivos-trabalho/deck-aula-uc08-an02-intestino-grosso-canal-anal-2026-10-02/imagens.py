# Figuras para os cards de estrutura (F-20261003-CLAUDE-15: livro/AnKing, slide não). Moore, Anatomia Orientada para a
# Clínica (bibliografia da UC08), figuras extraídas do PDF da turma para arquivos-trabalho/livros/moore-figs e vistas na
# folha de contato (scratchpad/moore.png).
LIVRO = {f"nebli-moore-fig-{n}.png": f"../livros/moore-figs/nebli-moore-fig-{n}.png" for n in ("5-43", "5-52", "5-53", "6-27", "6-31", "6-56", "6-59")}
F543, F552, F553, F627, F631, F656, F659 = (f"nebli-moore-fig-{n}.png" for n in ("5-43", "5-52", "5-53", "6-27", "6-31", "6-56", "6-59"))
IMAGENS = {
 "mobilidade": F543, "fixos": F543, "flexura-baco": F543,          # Fig. 5.43: intestinos in situ, flexuras e mesocolos
 "tres-caracteristicas": F552, "apendices-gordura": F552, "tenias-hx": F552,  # 5.52: tênias, apêndices omentais, saculações
 "sigmoide-ureter": F631,                                           # 6.31: colo sigmoide, reto e ureter
 "apendice-linfoide-hx": F553, "apendice-retrocecal": F553, "retrocecal-dor": F553, "io-papila-ileal-texto": F553,  # 5.53: ceco, papila ileal, posições do apêndice
                                     # AnKing (apendicite): ponto de McBurney
 "douglas": F627, "reto-prostata": F627, "reto-vagina": F627,       # 6.27: cortes medianos masculino e feminino
 "puborretal": F656, "dissinergia": F656, "pregas-tres": F656, "ampola-funcao": F656, "juncao-anorretal": F656,
 "valvulas-anais": F656, "seios-muco": F656, "esfincter-interno-hx": F656, "esfincter-externo-hx": F656,  # 6.56: reto e canal anal
 "fissura-anal": F659,                                              # 6.59: transições na linha pectinada
}
SEM_IMAGEM = {}
