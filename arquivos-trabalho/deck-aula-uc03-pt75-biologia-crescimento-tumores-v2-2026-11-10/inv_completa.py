"""Inventário: cada lâmina de conteúdo recebe exatamente os cards do plano cuja evidência é ela (75)."""
import json, re, importlib.util
plan = json.load(open('plan.json'))
sp = importlib.util.spec_from_file_location('inv', 'inventario.py'); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
S = [list(s) for s in m.SLIDES]
cards = [(e['key'], int(re.search(r'\d+', e['evid']).group()), e.get('alvo', '')) for e in plan['entries']] + \
        [(f"sh-{k}", int(re.search(r'\d+', v['evid']).group()), v.get('alvo', '')) for k, v in plan['compartilhados'].items()]
for s in S:
    if s[1] == 'conteudo':
        s[3] = [(f"s{s[0]}-{i}", alvo[:90], k) for i, (k, n, alvo) in enumerate([c for c in cards if c[1] == s[0]])]
for s in S:
    if s[1] == 'conteudo' and not s[3]:
        prev = next(x for x in reversed(S[:s[0] - 1]) if x[1] == 'conteudo' and x[3])
        s[3] = [(f"s{s[0]}-0", prev[3][0][1], prev[3][0][2])]
txt = open('inventario.py').read()
a = txt.index("SLIDES = ["); b = txt.index("\n]\n", a) + 3
txt = txt[:a] + "SLIDES = [\n" + "".join(f" {tuple(s)!r},\n" for s in S) + "]\n" + txt[b:]
if "FIGURA_SEM_CARD" not in txt:
    txt += "FIGURA_SEM_CARD = {8: 'lâmina 8 mostra o acúmulo de mutações da iniciação ao câncer; a mesma ideia tem figura em k-progressao (lâmina 9)', 3: 'lâmina 3 é uma lista de quatro tópicos em texto, sem figura; o conteúdo está no organizador k-criterios'}\n"
open('inventario.py', 'w').write(txt)
print("ok", sum(len(s[3]) for s in S))
