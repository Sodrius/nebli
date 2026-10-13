# Figuras do Trabulsi-Alterthum 6ª ed., cap. 64.1 (bibliografia da Micro na UC03), recortadas só na figura (sem legenda;
# F-20261003-CLAUDE-19) a partir do exemplar de Davi e vistas uma a uma (imagens-vistas.json).
NOMES = ("64-1-3", "64-1-4", "64-1-5", "64-1-8", "64-1-12")
LIVRO = {f"nebli-trabulsi-fig-{n}.png": f"../livros/trabulsi-figs/nebli-trabulsi-fig-{n}.png" for n in NOMES}
F = {n: f"nebli-trabulsi-fig-{n}.png" for n in NOMES}
IMAGENS = {
 "dimorfismo": F["64-1-3"],     # colônia de bolor × colônia de levedura
 "brotamento": F["64-1-4"],     # blastoconídio, pseudo-hifa, fissão
 "mucor-hifa": F["64-1-5"],     # hifa não septada × septada
 "esporangio": F["64-1-8"],     # esporângio, esporangióforo, esporangiósporos
 "asco": F["64-1-12"],          # ascos e ascocarpos
}
