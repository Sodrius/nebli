# Lote cego IO — rodada 2

Regras para o discriminador:
- Julgue **manufatura de image occlusion**, não conteúdo. O domínio do assunto (histologia vs clínica) NÃO é tell.
- Abra com Read as imagens raster (PNG/JPG) — caminhos relativos à raiz `C:\AI use\nebli\`. Imagens SVG não são visualizáveis; julgue pelos metadados + campos de texto. Viewability não é tell.
- Saída no formato exato do seu prompt.

---

## Card #1
- **Image:** SVG (não visualizável). Metadados: SVG de algoritmo clínico, EN, fundo branco.
- **Header:** `<u>Management</u> of <b>subclinical hypothyroidism</b>`
- **I0:** `[#!occlusions [[rect0::341,73,107,27]]<br>[[rect0::147,213,157,27]]<br>[[rect0::167,433,117,27]]<br>[[rect0::502,213,147,27]] #]<br>active`
- **Extra:** `<img src="7722e513746b980b2f07324063581ede.svg"><br><span style="font-size: 8pt;">Last updated: April 28, 2024</span>`

## Card #2
- **Image:** raster viewable → `arquivos-trabalho/io/anking/paste-08ef3b8f8bb35d3a477b9fc742d2db2dda6a77a1.jpg`
- **Header:** `How to Create This Note: visit the AnKing shared Github page`
- **I0:** `[#!occlusions [[rect0::223,448,60,32]]<br>[[rect0::354,321,53,24]]<br>[[rect0::200,424,54,23]]<br>[[rect0::133,414,57,28]]<br>[[rect0::417,288,40,24]]<br>[[rect0::439,187,42,29]]<br>[[rect0::208,223,49,31]]<br>[[rect0::380,111,49,20]] #]`
- **Extra:** (vazio)

## Card #3
- **Image:** raster viewable → `arquivos-trabalho/io/1fe1d39f6b540339dec1042af9348c8b.png`
- **Header:** `<b>Multipolar</b> neuron structure`
- **I0:** `[#!occlusions [[rect0::177,49,127,29]]<br>[[rect0::540,84,68,34]]<br>[[rect0::801,83,157,30]]<br>[[rect0::27,249,108,23]]<br>[[rect0::431,360,163,23]]<br>[[rect0::915,354,249,33]]<br>[[rect0::424,505,214,29]]<br>[[rect0::44,542,173,57]]<br>[[rect0::72,653,189,31]]<br>[[rect0::422,655,113,23]]<br>[[rect0::417,748,253,23]] #]<br>active`
- **Extra:** (vazio)

## Card #4
- **Image:** SVG (não visualizável). Metadados: SVG de algoritmo clínico, EN, fundo branco.
- **Header:** `<b>Blunt</b> abdominal <b>trauma</b> management algorithm`
- **I0:** `[#!occlusions [[rect0::364,73,77,27]]<br>[[rect0::92,463,147,27]]<br>[[rect0::559,193,157,27]]<br>[[rect0::579,463,77,27]]<br>[[rect0::294,313,147,27]] #]<br>active`
- **Extra:** `<img src="b9d02a5f99921bed397c0cda7b73a1ca.svg"><br><br><div><b>- CT scan:</b> detects abdominal fluid, solid organ injury</div><br><div><b>- FAST:</b> detects hemoperitoneum</div>`
