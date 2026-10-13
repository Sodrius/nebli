#!/bin/zsh
cd /Users/davisousa/NEBLI
for d in arquivos-trabalho/deck-aula-uc03-*-2026-10-{09,10}; do
  [ -f $d/receipt.json ] || continue
  echo "## $d"; python3 -m nebli.gates $d 2>&1 | grep -E "FALHA|passos"
done
echo FIM
