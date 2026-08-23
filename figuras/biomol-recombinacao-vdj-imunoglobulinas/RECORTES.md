# RECORTES — biomol-recombinacao-vdj-imunoglobulinas

Os PNGs desta pasta não são versionados (`.gitignore`: `figuras/**/*.png`). Além dos `slide-XX.png`
gerados por `extrair_slides.py`, este resumo usa **19 recortes de painel único** feitos do PDF do
professor. O motivo é didático: quase todo slide desta aula empilha dois ou três painéis lado a lado
com legenda longa em inglês; recortado, cada figura carrega **um** mecanismo e pode ir grande na
página.

Para regenerar (a partir de `slides/aula1-recombinacao-somatica-imunoglobulinas.pdf`, 960 × 540 pt,
300 dpi), rodar:

```python
import pymupdf
d = pymupdf.open("slides/aula1-recombinacao-somatica-imunoglobulinas.pdf")
out = "figuras/biomol-recombinacao-vdj-imunoglobulinas"
W, H, mat = 960.0, 540.0, pymupdf.Matrix(300/72, 300/72)

# (pagina, nome, x0, y0, x1, y1)  -- coordenadas em fracao da pagina
crops = [
 (6,  "fig-linfopoiese",           0.050, 0.150, 0.628, 0.815),
 (7,  "fig-selecao-clonal",        0.055, 0.030, 0.505, 0.930),
 (7,  "fig-expansao-clonal",       0.540, 0.045, 0.985, 0.855),
 (8,  "fig-ig-esquema",            0.060, 0.200, 0.420, 0.740),
 (8,  "fig-ig-3d",                 0.415, 0.240, 0.790, 0.800),
 (10, "fig-cadeias-vc",            0.220, 0.140, 0.750, 0.400),
 (10, "fig-classes-ig",            0.222, 0.540, 0.735, 0.935),
 (11, "fig-vj-fluxo",              0.020, 0.180, 0.445, 0.925),
 (11, "fig-locus-pesada",          0.660, 0.150, 0.980, 0.250),
 (13, "fig-rss",                   0.155, 0.240, 0.552, 0.630),
 (13, "fig-rss-arranjo",           0.555, 0.255, 0.890, 0.480),
 (14, "fig-exclusao-alelica",      0.430, 0.020, 0.975, 0.880),
 (15, "fig-rag-nick-hairpin",      0.240, 0.220, 0.655, 0.820),
 (16, "fig-rag-sinapse",           0.160, 0.170, 0.845, 0.870),
 (17, "fig-diversidade-juncional", 0.020, 0.175, 0.625, 0.935),
 (20, "fig-jnhe-ku",               0.235, 0.110, 0.770, 0.710),
 (21, "fig-junta-codificante",     0.250, 0.120, 0.710, 0.915),
 (22, "fig-aid-cascata",           0.015, 0.400, 0.985, 0.995),
 (23, "fig-switch-classe",         0.035, 0.150, 0.675, 0.930),
]
for pg, nome, x0, y0, x1, y1 in crops:
    clip = pymupdf.Rect(x0*W, y0*H, x1*W, y1*H)
    d[pg-1].get_pixmap(matrix=mat, clip=clip).save(f"{out}/{nome}.png")
```

A vigésima figura da E1 é o `slide-19.png` inteiro (recombinação homóloga × junção não homóloga) —
esse slide já vem em português e com um painel só, então não precisou de recorte.
