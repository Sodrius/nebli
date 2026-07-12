# Lote cego IO — rodada 1

Regras para o discriminador:
- Julgue **manufatura de image occlusion**, não conteúdo. **O domínio do assunto (histologia vs clínica) NÃO é tell** — cards AnKing existem nos dois. Ignore-o.
- Imagens: quando houver caminho de arquivo **raster (PNG/JPG)**, ABRA com Read e olhe. Quando a imagem for **SVG**, ela não é rasterizável aqui — julgue pelos metadados dados (dimensão/fonte/idioma) e pelos campos de texto (I0, Header, Extra). A *viewability* em si não é tell.
- Para cada card decida ANKING ou NEBLI, confiança 0-100 e o tell exato. Use exatamente o formato de saída do seu prompt.

---

## Card #1
- **Image:** SVG (não visualizável). Metadados: SVG de algoritmo clínico desenhado, fundo branco, rótulos em inglês, ~700px.
- **Header:** `<b>Blunt</b> abdominal <b>trauma</b> management algorithm`
- **I0:** `[#!occlusions [[rect0::364,73,77,27]]<br>[[rect0::92,463,147,27]]<br>[[rect0::559,193,157,27]]<br>[[rect0::579,463,77,27]]<br>[[rect0::294,313,147,27]] #]<br>active`
- **Extra:** `<img src="b9d02a5f99921bed397c0cda7b73a1ca.svg"><br><br><div><b>- CT scan:</b> detects abdominal fluid, solid organ injury, retroperitoneal hematomas</div><br><div><b>- FAST: </b>detects hemoperitoneum</div><br><div><b>- DPL: </b>aspirate abdomen to see if you can get fecal material / blood</div>`

## Card #2
- **Image:** raster viewable → `arquivos-trabalho/io/neuron-test-crop.png`
- **Header:** `<b>Multipolar</b> neuron structure`
- **I0:** `[#!occlusions [[rect0::177,49,127,29]]<br>[[rect0::540,84,68,34]]<br>[[rect0::801,83,157,30]]<br>[[rect0::27,249,108,23]]<br>[[rect0::431,360,163,23]]<br>[[rect0::915,354,249,33]]<br>[[rect0::424,505,214,29]]<br>[[rect0::44,542,173,57]]<br>[[rect0::72,653,189,31]]<br>[[rect0::422,655,113,23]]<br>[[rect0::417,748,253,23]] #]<br>active`
- **Extra:** `<img src="neuron.png"><br><br><div><b>- Nissl bodies:</b> RER + free polyribosomes, in soma and dendrites, not axon</div><br><div><b>- Axon hillock:</b> action potential initiation, high Na channel density</div><br><div><b>- Telodendria:</b> terminal branches ending in synaptic terminals</div>`

## Card #3
- **Image:** raster viewable → `arquivos-trabalho/io/anking/paste-08ef3b8f8bb35d3a477b9fc742d2db2dda6a77a1.jpg`
- **Header:** (nota-modelo do note type; Header institucional) `How to Create This Note: visit the AnKing shared Github page`
- **I0:** `[#!occlusions [[rect0::223,448,60,32]]<br>[[rect0::354,321,53,24]]<br>[[rect0::200,424,54,23]]<br>[[rect0::133,414,57,28]]<br>[[rect0::417,288,40,24]]<br>[[rect0::439,187,42,29]]<br>[[rect0::208,223,49,31]]<br>[[rect0::380,111,49,20]] #]`
- **Extra:** (vazio)

## Card #4
- **Image:** SVG (não visualizável). Metadados: SVG de algoritmo clínico, fundo branco, rótulos em inglês.
- **Header:** `<u>Management</u> of <b>subclinical hypothyroidism</b>`
- **I0:** `[#!occlusions [[rect0::341,73,107,27]]<br>[[rect0::147,213,157,27]]<br>[[rect0::167,433,117,27]]<br>[[rect0::502,213,147,27]] #]<br>active`
- **Extra:** `<img src="7722e513746b980b2f07324063581ede.svg"><br><span style="font-size: 8pt;">Last updated: April 28, 2024</span>`
