#!/bin/zsh
cd /Users/davisousa/NEBLI
python3 - <<'PY' | while read q; do python3 -m nebli.explicacoes gerar "$q" --refazer; done
import json
ids=json.load(open("arquivos-trabalho/correcao-comentarios-2026-10-11/tab-refazer-ids.json"))
for i in range(0,len(ids),40):
    print('cid:'+",".join(map(str,ids[i:i+40])))
PY
echo FIM
