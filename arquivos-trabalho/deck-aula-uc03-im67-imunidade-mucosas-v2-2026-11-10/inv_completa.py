"""Liga todo card do plano à sua lâmina no inventário (sh e entradas) e registra lâmina visual sem figura."""
import json, re, importlib.util
plan = json.load(open('plan.json'))
sp = importlib.util.spec_from_file_location('inv', 'inventario.py'); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
S = [list(s) for s in m.SLIDES]
have = {it[2] for s in S for it in s[3]}
cards = [(e['key'], int(re.search(r'\d+', e['evid']).group()), e.get('alvo', '')) for e in plan['entries']] + \
        [(f"sh-{k}", int(re.search(r'\d+', v['evid']).group()), v.get('alvo', '')) for k, v in plan['compartilhados'].items()]
validos = {k for k, _, _ in cards}
for s in S:
    s[3] = [it for it in s[3] if it[2] in validos]
have = {it[2] for s in S for it in s[3]}
for k, n, alvo in cards:
    if k not in have:
        S[n - 1][3] = list(S[n - 1][3]) + [(f"x{n}-{len(S[n - 1][3])}", alvo, k)]
txt = open('inventario.py').read()
a = txt.index("SLIDES = ["); b = txt.index("\n]\n", a) + 3
txt = txt[:a] + "SLIDES = [\n" + "".join(f" {tuple(s)!r},\n" for s in S) + "]\n" + txt[b:]
if "FIGURA_SEM_CARD" not in txt:
    txt += "FIGURA_SEM_CARD = {10: 'lâmina só com uma frase curta (CONTUDO... aparecem rapidamente PMNs), sem figura; o conteúdo está em k-infl-fisiologica'}\n"
open('inventario.py', 'w').write(txt)
print("ok", sum(len(s[3]) for s in S))
