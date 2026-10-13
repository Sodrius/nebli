# Figuras para os cards de estrutura (F-20261003-CLAUDE-15: livro/AnKing, slide não). Moore (bibliografia da UC08),
# extraídas para arquivos-trabalho/livros/moore-figs e vistas na folha scratchpad/moore-an01.png.
NOMES = ("5-33", "5-37", "5-38", "5-39", "5-45", "5-47", "5-48")
LIVRO = {f"nebli-moore-fig-{n}.png": f"../livros/moore-figs/nebli-moore-fig-{n}.png" for n in NOMES}
F533, F537, F538, F539, F545, F547, F548 = (f"nebli-moore-fig-{n}.png" for n in NOMES)
IMAGENS = {
 "esofago-comprimento": F533, "terco-superior-estriado": F533, "ees-ar": F533, "eei-refluxo": F533, "chagas-neuronios": F533,
 "lig-frenoesofagico": F533, "pilar-direito": F533, "barrett-linha-z": F533, "perfuracao-endoscopia": F533,   # 5.33: esôfago, constrições, ligamento frenoesofágico, linha Z
 "incisura-cardica": F537, "incisura-angular": F537, "estomago-anterior": F537,                              # 5.37: partes e relações do estômago
 "canal-gastrico": F538,                                                                                      # 5.38: face interna, canal gástrico
 "camada-obliqua": "1702221209267#0",                                                                         # Junqueira 15-14: camadas musculares do estômago
 "estomago-posterior": F539, "ulcera-posterior-esplenica": F539,                                             # 5.39: bolsa omental e leito do estômago (a. esplênica)
 "duodeno-niveis": F545, "segunda-porcao-ampola": F545, "esfincter-oddi": F545, "calculo-ampola": F545,
 "pancreas-2a-porcao": F545, "ducto-principal-papila-maior": F545, "ducto-acessorio-papila-menor": F545,      # 5.45: partes do duodeno, papilas
 "jejuno-fracao": F547, "quadrantes": F547,                                                                   # 5.47: jejuno no QSE, íleo no QID
 "mesenterio": F548, "vasos-retos-jejuno": F548, "gordura-ileo": F548, "jejuno-parede": F548, "plicas-jejuno": F548,  # 5.48: jejuno × íleo
}
SEM_IMAGEM = {}
