#!/usr/bin/env bash
# Constrói todos os Image Occlusion da aula a partir dos rótulos reais do PDF de
# slides. Regra aplicada em todos: a máscara cobre o NOME da estrutura; textos
# explicativos entre parênteses ficam visíveis (não vazam a resposta e evitam
# que o IO teste duas vezes o que um cloze já testa).
set -euo pipefail

SLIDES="${1:?uso: build_io.sh <slides.pdf>}"
OUT="$(cd "$(dirname "$0")" && pwd)/io"
TOOL="$(cd "$(dirname "$0")/../../flashcards/scripts" && pwd)/pdf_figura_io.py"
DPI=200

io() { python3 "$TOOL" build "$SLIDES" --dpi "$DPI" "$@"; }

io --page 2 --crop 100,395,470,625 --out-dir "$OUT/io-01-partes" --name io-01-partes \
  --header "<b>Anatomy · Large intestine</b> — name each numbered part and say whether it is fixed or mobile" \
  --label "1. Ceco e 2. Apêndice vermiforme:1" \
  --label "3. Colo ascendente (fixo) e 4. flexura cólica direita:4,6" \
  --label "5. Colo transverso (móvel) e 6. flexura cólica esquerda:8,11" \
  --label "7. Colo descendente (fixo):14" \
  --label "8. Colo sigmóide (móvel):16" \
  --label "9. Reto e 10. Canal anal:18"

io --page 3 --crop 88,60,470,318 --out-dir "$OUT/io-02-superficie" --name io-02-superficie \
  --header "<b>Anatomy · Large intestine</b> — identify the surface features and flexures of the colon" \
  --label "Flexura cólica esquerda:0,2" \
  --label "Flexura cólica direita:1" \
  --label "Haustros ou saculações:3,5" \
  --label "Corpos adiposos ou apêndices epiploicos:4,6,7,8" \
  --label "Tênias:9" \
  --label "Colo sigmóide:10" \
  --label "Apêndice vermiforme:11,13" \
  --label "Reto:12" \
  --pixel-label "Colo transverso:330,40,100,24" \
  --pixel-label "Tênia omental:432,62,50,40" \
  --pixel-label "Pregas semilunares:519,42,82,38"

io --page 15 --crop 95,395,450,640 --out-dir "$OUT/io-03-tenias" --name io-03-tenias \
  --header "<b>Anatomy · Large intestine</b> — identify the three taeniae coli and the structures at the cecum" \
  --label "Tênia livre:0" \
  --label "Apêndice vermiforme:1,2" \
  --label "Tênia mesocólica:3" \
  --label "Tênia omental:4,5" \
  --label "Ceco:6" \
  --label "Íleo:7"

io --page 11 --crop 90,60,475,333 --out-dir "$OUT/io-04-ceco-interno" --name io-04-ceco-interno \
  --header "<b>Anatomy · Cecum</b> — identify the components of the ileocecal region seen from inside the cecum" \
  --label "Papila ileal (projeção do íleo no ceco):1" \
  --label "Válvula íleocecal:3,4" \
  --label "Lábio íleocólico:5" \
  --label "Óstio ileal:6" \
  --label "Lábio íleocecal:7" \
  --label "Óstio do apêndice:8" \
  --label "Apêndice vermiforme:9,10"

io --page 16 --crop 88,365,445,642 --out-dir "$OUT/io-05-peca-ileocecal" --name io-05-peca-ileocecal \
  --header "<b>Anatomy · Cadaveric specimen</b> — identify the ileocecal region on the real specimen" \
  --label "Íleo distal:0" \
  --label "Tênia livre:1" \
  --label "Ceco:2" \
  --label "Apêndice vermiforme:3"

io --page 21 --crop 100,135,450,322 --out-dir "$OUT/io-06-reto" --name io-06-reto \
  --header "<b>Anatomy · Rectum</b> — identify the lateral flexures, the transverse folds and the ampulla" \
  --label "Flexura superior:0" \
  --label "Prega transversa média:1,2,4" \
  --label "Prega transversa superior:3,5,7" \
  --label "Ampola retal:6" \
  --label "Flexura intermediária:8,9" \
  --label "Flexura inferior:10" \
  --label "Prega transversa inferior:11,12"

io --page 21 --crop 88,365,455,642 --out-dir "$OUT/io-07-peca-reto" --name io-07-peca-reto \
  --header "<b>Anatomy · Cadaveric specimen</b> — identify the rectum on the sagittal section of the real specimen" \
  --label "Prega transversa:0" \
  --label "Flexura sacral:1" \
  --label "Ampola retal:2" \
  --label "Flexura anorretal:3"

io --page 20 --crop 90,368,450,642 --out-dir "$OUT/io-08-pelve-fem" --name io-08-pelve-fem \
  --header "<b>Anatomy · Female pelvis</b> — identify the peritoneal pouches and the rectal landmarks" \
  --label "Escavação retouterina:3,4" \
  --label "Prega transversa:5,6" \
  --label "Escavação vesicouterina:7,8" \
  --label "Ampola retal:9" \
  --label "Flexura anorretal:10"

io --page 22 --crop 90,136,455,332 --out-dir "$OUT/io-09-canal-anal" --name io-09-canal-anal \
  --header "<b>Anatomy · Anal canal</b> — identify each landmark of the anal canal" \
  --label "Canal anal cirúrgico:0,1,3,5" \
  --label "Junção anorretal:2,4,6,7" \
  --label "Coluna anal:8,9,11,12" \
  --label "Plexo venoso interno:10" \
  --label "Seio anal:13,15,17,18" \
  --label "Linha branca (anocutânea):14,16" \
  --label "Plexo venoso externo:19" \
  --label "Linha pectinada:20,21,22"

io --page 22 --crop 88,368,470,648 --out-dir "$OUT/io-10-peca-canal" --name io-10-peca-canal \
  --header "<b>Anatomy · Cadaveric specimen</b> — identify the anal canal landmarks on the real specimen" \
  --label "Ampola retal:0,1" \
  --label "Flexura anorretal:2" \
  --label "Seio anal:3" \
  --label "Coluna anal:4"

io --page 25 --crop 95,65,450,330 --out-dir "$OUT/io-11-esfincteres" --name io-11-esfincteres \
  --header "<b>Anatomy · Anal sphincters</b> — name each masked muscle of the anal sphincter complex" \
  --label "Esfíncter anal externo:0" \
  --label "Esfíncter anal interno:1" \
  --label "M. circular:5" \
  --label "M. puborretal / m. levantador do ânus:6,8,9" \
  --label "M. longitudinal:7" \
  --label "Esfíncter externo do ânus:10,11,12" \
  --blank "652,410,340,290"


echo "IO construídos em $OUT"
