# uso: qq.sh < consultas ; acrescenta em busca/anking.txt e imprime só nids novos, curtos
K='"deck:Referências::Anking Step Deck*"'
while IFS= read -r q; do python3 q.py "$K $q" ${N:-30}; done | tee -a busca/anking.txt > /tmp/gr02_last.txt
python3 - <<'P'
seen=set()
import re
for l in open('busca/anking.txt').read().splitlines()[:-len(open('/tmp/gr02_last.txt').read().splitlines())]:
    if l[:1].isdigit(): seen.add(l.split('|')[0].strip())
for l in open('/tmp/gr02_last.txt'):
    if l.startswith('#'): print(l.strip()); continue
    n=l.split('|')[0].strip()
    if not n.isdigit() or n in seen: continue
    seen.add(n); p=l.split('|'); print(n, p[3].strip()[:200].replace('\n',' '))
P
