set -e
cd /Users/davisousa/NEBLI/arquivos-trabalho/deck-aula-uc03-pt75-biologia-crescimento-tumores-v2-2026-11-10
export PYTHONPATH=/Users/davisousa/NEBLI
/usr/bin/python3 planejar.py
/usr/bin/python3 - <<'PY'
import json,re
mot={x['atendida_por'][0]:x['id'] for x in json.load(open('motivacoes.json'))['motivacoes']}
s=open('spec.py').read()
for k,mid in mot.items():
    s=re.sub(r'(au\("%s",.*?motivacao=")m\d+(")'%re.escape(k), r'\g<1>%s\2'%mid, s, count=1, flags=re.S)
open('spec.py','w').write(s); print('m0 restantes', s.count('motivacao="m0"'))
PY
/usr/bin/python3 build.py >/dev/null 2>&1 || true
/usr/bin/python3 escopo_extra.py
/usr/bin/python3 artefatos_e5.py | tail -1
/usr/bin/python3 build.py 2>&1 | grep -E "ISSUES"
/usr/bin/python3 revisao_e6e7.py | tail -1
/usr/bin/python3 inv_completa.py | tail -1
/usr/bin/python3 - <<'PY'
import re,json,importlib.util
t=open('inventario.py').read(); seen={}
def f(m):
    k=m.group(1); seen[k]=seen.get(k,0)+1
    return m.group(0) if seen[k]==1 else f"('{k}b{seen[k]}',"
t=re.sub(r"\('([sx]\d+-\d+)',",f,t)
if 'FIGURA_SEM_CARD' not in t: t+="FIGURA_SEM_CARD = {3: 'lâmina 3 é uma lista de quatro tópicos em texto, sem figura; o conteúdo está no organizador k-criterios'}\n"
open('inventario.py','w').write(t)
sp=importlib.util.spec_from_file_location('i','inventario.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
p=json.load(open('planejamento.json'))
p['alvos']=[{'id':f'pt75-s{n:02d}-{i}','slide':str(n),'alvo':a,'fontes':[f'slide {n}'],'origem_prevista':k} for n,c,tt,its in m.SLIDES for i,a,k in its]
json.dump(p,open('planejamento.json','w'),ensure_ascii=False,indent=1)
g=open('REVISAO-AUTORAIS-gerado.md').read().splitlines()
r=open('REVISAO-AUTORAIS.md').read()
a,_,b=r.partition("## Revisão final no deck vivo")
keys=[l.split(' ')[1] for l in g if l.startswith('- k-')]
a="\n".join(l for l in a.splitlines() if not (l.startswith('- k-') and l.split(' ')[1] in keys))
a=a.rstrip()+"\n"+"\n".join(l for l in g if l.startswith('- k-'))+"\n\n"
open('REVISAO-AUTORAIS.md','w').write(a+("## Revisão final no deck vivo"+b if b else ""))
PY
cd /Users/davisousa/NEBLI
/usr/bin/python3 -m nebli.inventario arquivos-trabalho/deck-aula-uc03-pt75-biologia-crescimento-tumores-v2-2026-11-10 | tail -1
