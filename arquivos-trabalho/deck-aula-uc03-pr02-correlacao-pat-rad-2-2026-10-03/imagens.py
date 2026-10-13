# Figuras para os cards de estrutura (F-20261003-CLAUDE-15): Robbins (bibliografia da UC03), extraídas para
# arquivos-trabalho/livros/robbins-figs e vistas em scratchpad/robbins.png e robbins2.png.
NOMES = ("18-1", "18-3", "18-24", "18-44")
LIVRO = {f"nebli-robbins-fig-{n}.png": f"../livros/robbins-figs/nebli-robbins-fig-{n}.png" for n in NOMES}
R181, R183, R1824, R1844 = (f"nebli-robbins-fig-{n}.png" for n in NOMES)
IMAGENS = {
 "hemangioma-mulheres": R1844,                        # 18-44: hemangioma
 "micro-macronodular": R1824,                         # 18-24: cirrose alcoólica, nódulos e septos (substitui o slide)
 "hp-esplenomegalia": R183, "hp-plaquetas": R183, "varizes-terco-inferior": R183,   # 18-3: consequências da hipertensão portal
}
SEM_IMAGEM = {}
# A aula é de correlação radiopatológica: estes cards ensinam a ler a imagem da própria aula (US, TC, peça, coloração);
# o Robbins e o AnKing não têm a imagem equivalente (busca de 03/10), então a do slide fica, com o motivo.
SLIDE_OK = {k: "imagem radiológica/da peça da própria aula de correlação; Robbins e AnKing sem equivalente (busca 03/10)"
            for k in ("hemangioma-us", "hemangioma-tc", "hemangioma-macro", "esteatose-us", "esteatose-tc", "reticulina", "hp-tc", "baco-congesto", "macronodular", "cirrose-verde", "us-cirrose", "enfisema-tc")}
