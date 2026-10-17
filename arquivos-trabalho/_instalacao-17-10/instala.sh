#!/bin/zsh
# uso: instala.sh <corrida>  — build, cobertura, pre, refação, apply, ordem e despejo (a leitura do despejo é manual)
set -e
cd ~/NEBLI; R=$1
espera() { until [ ! -f arquivos-trabalho/ANKI-ESCRITA.lock ]; do sleep 15; done; for i in $(seq 1 60); do r=$(/usr/bin/python3 -c "
from nebli.decks import Anki;A=Anki()
try: A('findNotes',query='nid:1'); print('ok' if A('guiSelectedNotes')==[] else 'x')
except Exception as e: print('x')" 2>/dev/null); [ "$r" = ok ] && return 0; sleep 15; done; echo ANKI-OCUPADO; exit 3; }
(cd $R && NEBLI_SEM_TAB=1 /usr/bin/python3 build.py 2>&1 | grep ISSUES | cut -c1-200)
[ -f $R/io/au.json ] && /usr/bin/python3 arquivos-trabalho/deck-aula-uc03-rd05-tomografia-v2-2026-10-16/io/cob.py $R $R/io/au.json | tail -1
NEBLI_SEM_TAB=1 /usr/bin/python3 -m nebli.artefatos pre $R 2>&1 | grep "FALHA\|passos" || true
if NEBLI_SEM_TAB=1 /usr/bin/python3 -m nebli.artefatos pre $R 2>&1 | grep -q "FALHA \[duro\]"; then echo "GATE DURO — parar"; exit 2; fi
espera
/usr/bin/python3 -m nebli.refacao $R 2>&1 | tail -1
touch arquivos-trabalho/_instalacao-17-10/aplicando.lock; P=arquivos-trabalho/anki-acao-pedido.json; [ -f $P ] && mv $P arquivos-trabalho/_instalacao-17-10/fila-reposicao/pendente-$(date +%s).json
(cd $R && NEBLI_SEM_TAB=1 /usr/bin/python3 apply.py 2>&1 | tail -1); rm -f arquivos-trabalho/_instalacao-17-10/aplicando.lock
espera
L=$(python3 -c "import json;print(json.load(open('$R/plan.json'))['lesson_id'])")
/usr/bin/python3 -m nebli.ordem verificar NEBLI::$L --plan $R/plan.json 2>&1 | tail -1
/usr/bin/python3 -m nebli.artefatos despejo $R >/dev/null 2>&1; wc -l $R/revisao-despejo.txt
