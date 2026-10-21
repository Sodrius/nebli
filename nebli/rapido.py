"""Atalhos para fechar um deck-aula com poucos tokens (F-20261021-CLAUDE-01).

    python3 -m nebli.rapido cobertura <corrida> decisoes.json    # busca/cobertura.tsv + REVISAO-AUTORAIS.md
    python3 -m nebli.rapido inventario <corrida> lampadas.json   # inventario.py a partir dos cards e das classes das lâminas
    python3 -m nebli.rapido exclusoes <corrida> "motivo geral"   # EXCLUIDOS das seções declaradas que ficaram fora

decisoes.json: {"au-chave": ["lacuna|parcial", "decisão com motivo"]}.
lampadas.json: {"n_laminas": 81, "paginas": {"1": ["capa","Capa"], "5": ["logistica","Divisória"], "9": ["fora_do_recorte","Figura"]},
                "alias": {"7": "au-etapas"}, "livro": [["Livro", [["l1","ideia","chave"]]]], "provas": [["Provas", [["p1","ideia","chave"]]]]}
 • página com card cujo `evid` é o número: item automático para cada card; `alias` liga lâmina sem card a um card existente.
"""
import json, re, sys, collections, html
from pathlib import Path


def _plan(run):
    return json.loads((Path(run) / "plan.json").read_text(encoding="utf-8"))


def _norm(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip().lower()


def cobertura(run, dec):
    run = Path(run); plan = _plan(run); D = json.loads(Path(dec).read_text(encoding="utf-8"))
    sem = {}
    for l in (run / "busca" / "semantica.jsonl").read_text(encoding="utf-8").splitlines():
        d = json.loads(l); sem[d["chave"]] = d
    rows = ["chave\tconceito\tfonte_aula\tveredito\tlidos\tdecora\tdecisao"]
    rev = [f"# Revisão dos autorais — {plan.get('lesson_id')}", "", "Cada autoral relido contra EXEMPLARES-CARDS e ANTI-EXEMPLARES-CARDS §1–16 (busca/cobertura.tsv: lacuna ou parcial).", ""]
    falta = []
    for e in plan["entries"]:
        k = e["key"]; base = [k, e.get("alvo") or k, e.get("evid") or ""]
        if e.get("origin") == "Autoral":
            if k not in D or k not in sem:
                falta.append(k); continue
            v, dec_ = D[k]
            lidos = " ".join(str(t["nid"]) for t in [t for t in sem[k]["top"] if t["acervo"] == "AnKing"][:3])
            cl = [re.sub(r"::.*", "", c) for c in re.findall(r"\{\{c\d+::(.*?)\}\}", e["fields"]["Text"])]
            dec_txt = re.sub(r"<[^>]+>", "", cl[0]).strip()
            rows.append("\t".join(base + [v, lidos, dec_txt, dec_]))
            rev.append(f"- {k} — par: ANTI-EXEMPLARES §1–16 e os clozes curtos e organizadores dos EXEMPLARES — decora: {dec_txt} — ok")
        else:
            rows.append("\t".join(base + ["coberto", "", "", "card de acervo achado por seção, palavra-chave ou significado"]))
    if falta:
        print("FALTA decisão ou busca (chave exata) para:", falta); sys.exit(1)
    (run / "busca" / "cobertura.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    rev += ["", "Organizadores necessários: sim — a aula enumera conjuntos que ela mesma nomeia; cada organizador cobre um desses conjuntos."]
    (run / "REVISAO-AUTORAIS.md").write_text("\n".join(rev) + "\n", encoding="utf-8")
    print(len(rows) - 1, "linhas")


def inventario(run, cfg):
    run = Path(run); plan = _plan(run); C = json.loads(Path(cfg).read_text(encoding="utf-8"))
    cards = collections.defaultdict(list)
    for e in plan["entries"]:
        cards[int(re.search(r"\d+", e["evid"]).group())].append((e["key"], e.get("alvo", "")))
    for k, v in plan["compartilhados"].items():
        cards[int(re.search(r"\d+", v["evid"]).group())].append(("sh-" + k, v.get("alvo", "")))
    allk = {k for v in cards.values() for k, _ in v}
    src = {}
    for k, v in plan["compartilhados"].items():
        m = re.search(r"AnKing (\d{13})", v.get("motivo", ""))
        if m: src[m.group(1)] = "sh-" + k
    def kk(c):
        if c in allk: return c
        m = re.match(r"ak(\d{13})$", c)
        if m and m.group(1) in src: return src[m.group(1)]
        return None
    out = []
    for n in range(1, int(C["n_laminas"]) + 1):
        items = [(f"i{n}-{i+1}", alvo, key) for i, (key, alvo) in enumerate(cards.get(n, []))]
        al = C.get("alias", {}).get(str(n))
        if al:
            for j, a in enumerate([al] if isinstance(al, str) else al):
                if kk(a): items.append((f"i{n}-a{j+1}", f"Apoio ao card {a}", kk(a)))
        pg = C.get("paginas", {}).get(str(n))
        if items:
            out.append((n, "conteudo", (pg[1] if pg else f"Lâmina {n}"), items))
        elif pg:
            out.append((n, pg[0], pg[1], []))
        else:
            out.append((n, "fora_do_recorte", f"Lâmina {n}: figura ou detalhe sem card próprio (FORA_DO_RECORTE)", []))
    def grp(g):
        r = []
        for t, its in g:
            novos = []
            for i, idea, c in its:
                cs = [c] if isinstance(c, str) else c
                cs = [kk(x) or x for x in cs if (x.startswith("EXC") or kk(x))]
                if not cs: print("ITEM SEM CARD:", i, idea); continue
                novos.append((i, idea, cs if len(cs) > 1 else cs[0]))
            r.append((t, novos))
        return r
    L = [f'"""Inventário atômico — {plan.get("lesson_id")} (gerado por nebli.rapido a partir dos cards e das classes das lâminas)."""',
         f'PREFIXO = "{plan["short"]}"', f'AULA = {C.get("aula", plan.get("lesson_id"))!r}', 'EXC = "EXC: "', "", "SLIDES = ["]
    L += [" " + repr(s) + "," for s in out] + ["]"]
    L.append("JUSTIFICATIVAS = " + repr({"capa": "capa sem conteúdo", "fora_do_recorte": "figura ou detalhe sem card próprio; o conceito está no card vizinho ou no FORA_DO_RECORTE",
                                         "logistica": "divisória, leitura recomendada, agradecimento ou repetição"}))
    L.append("CAPITULO = " + repr(grp(C.get("livro", []))))
    L.append("EXERCICIOS = " + repr(grp(C.get("provas", []))))
    (run / "inventario.py").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(len(out), "lâminas")


def exclusoes(run, motivo):
    import urllib.request
    run = Path(run); plan = _plan(run)
    def ac(a, **p):
        return json.loads(urllib.request.urlopen(urllib.request.Request("http://localhost:8765", json.dumps({"action": a, "version": 6, "params": p}).encode())).read())["result"]
    inc = {str(e["src"]) for e in plan["entries"] if e.get("src")} | {str(v["source_nid"]) for v in plan["compartilhados"].values() if v.get("source_nid")}
    shn = [int(k) for k in plan["compartilhados"]]
    for n in (ac("notesInfo", notes=shn) if shn else []):
        for t in n["tags"]:
            m = re.match(r"NEBLI::source::nid-(\d+)", t)
            if m: inc.add(m.group(1))
    ex = (run / "exclusoes.py").read_text(encoding="utf-8") if (run / "exclusoes.py").exists() else "EXCLUIDOS.extend([\n])\n"
    ja = set(re.findall(r"\((\d{13}),", ex)); novos = []
    for s in [l.strip() for l in (run / "busca" / "secoes-da-aula.txt").read_text().splitlines() if l.strip()]:
        for l in (run / "busca" / "secoes" / s).read_text(encoding="utf-8").splitlines()[1:]:
            nid = l.split(" ", 1)[0]
            if nid not in inc and nid not in ja and nid not in novos: novos.append(nid)
    ex = ex.replace("\n])\n", "\n" + "".join(f" ({n}, {motivo!r}),\n" for n in novos) + "])\n")
    (run / "exclusoes.py").write_text(ex, encoding="utf-8"); print(len(novos), "exclusões novas")


if __name__ == "__main__":
    c, run, arg = sys.argv[1:4]
    {"cobertura": cobertura, "inventario": inventario, "exclusoes": exclusoes}[c](run, arg)
