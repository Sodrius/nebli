"""Análise do deck-prova / deck-UC inteiro, não só de cada aula (F-20261013-CLAUDE-03).

    python3 -m nebli.analise_prova "NEBLI::UC03::P1"        # uma prova
    python3 -m nebli.analise_prova "NEBLI::UC03"            # a UC inteira

Somente leitura no Anki. Escreve em arquivos-trabalho/analise-<ramo>-<data>/:
  RELATORIO.md  números por aula e sinais mecânicos (repetição, peso clínico, detalhe numérico, Tab, escopo declarado)
  frentes.txt   todas as frentes na ordem das aulas e da aula, com cor, origem e marcas, para a leitura de julgamento
A leitura humana/IA julga, sobre o deck-prova inteiro: cobertura, ordem lógica e progressão entre aulas, princípios
importantes com card antes dos detalhes, detalhes que se complementam sem repetir, peso de ciclo básico e qualidade dos Tabs.
As correções voltam para os specs das aulas (retirar, rebaixar, acrescentar card-ponte de princípio) — ver EXECUCAO-DECK-AULA §7.
"""
from __future__ import annotations

import collections
import html
import importlib.util
import json
import re
import sqlite3
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSON = re.compile(r"^NEBLI::(20\d\d-uc\d+-[a-z0-9-]+)$")
COR = {1: "verm", 2: "lar", 3: "verde", 4: "azul", 5: "rosa"}
CLOZE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", re.S)
STOP = set("the a an of in to and or is are by with for on as at that which its it be from into this their than".split())
# Sinais de conteúdo clínico/semiológico além do ciclo básico (para leitura, não para corte automático).
CLIN = re.compile(r"(?i)\b(treat(ment|ed)?|management|next step|first[- ]line|drug of choice|dose|presents? with|patient|prognosis|"
                  r"diagnos(is|ed|e)|symptom|physical exam|auscultation|murmur|percussion|therapy|surgery|indicated|contraindicat|"
                  r"most likely|workup|screening)\b")
NUM = re.compile(r"\d")


def call(action, **params):
    req = urllib.request.Request("http://127.0.0.1:8765", json.dumps({"action": action, "version": 6, "params": params}).encode())
    r = json.load(urllib.request.urlopen(req))
    if r.get("error"):
        raise RuntimeError(r["error"])
    return r["result"]


def clean(s):
    s = re.sub(r"<img[^>]*>", " [img] ", s or "")
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def front(fields):
    for k in ("Text", "Front", "Header", "Title"):
        if k in fields and fields[k]["value"].strip():
            return fields[k]["value"]
    return next(iter(fields.values()))["value"] if fields else ""


def full_sentence(text):
    return clean(CLOZE.sub(lambda m: m.group(1), text))


def words(text):
    return {w for w in re.findall(r"[a-zα-ω0-9]+", full_sentence(text).lower()) if w not in STOP and len(w) > 2}


def answers(text):
    return tuple(sorted({clean(a).lower() for a in CLOZE.findall(text or "")}))


def lesson_number(lid):
    m = re.search(r"-(\d{2})-", lid)
    return int(m.group(1)) if m else 99


def corrida(lid):
    best = None
    for p in (ROOT / "arquivos-trabalho").glob("deck-aula-*/plan.json"):
        try:
            if json.loads(p.read_text()).get("lesson_id") == lid and (best is None or p.stat().st_mtime > best.stat().st_mtime):
                best = p
        except Exception:
            continue
    return best.parent if best else None


def escopo(run):
    if not run or not (run / "spec.py").exists():
        return None
    try:
        spec = importlib.util.spec_from_file_location("spec_an", run / "spec.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        return getattr(m, "ESCOPO", None)
    except Exception:
        return None


def tabs(card_ids):
    from nebli import explicacoes
    db = sqlite3.connect(explicacoes.store_path())
    version = explicacoes.style_version(explicacoes.STYLE.read_text(encoding="utf-8"))
    out = {}
    for cid in card_ids:
        row = db.execute("select status, texto, estilo from explicacoes where card_id=?", (cid,)).fetchone()
        out[cid] = row and {"status": row[0], "palavras": len((row[1] or "").split()), "atual": row[2] == version}
    return out


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        raise SystemExit(__doc__)
    ramo = argv[0].rstrip(":")
    from nebli.rotulos import canonical
    dids = [str(i) for name, i in call("deckNamesAndIds").items() if canonical(name) == ramo or canonical(name).startswith(ramo + "::")]
    if not dids:
        raise SystemExit(f"nenhum deck em {ramo}")
    nids = call("findNotes", query="(" + " OR ".join(f"did:{d}" for d in dids) + ') -"tag:NEBLI::retirado*"')
    lessons = sorted({m.group(1) for n in call("notesInfo", notes=nids) for t in n["tags"] for m in [LESSON.match(t)] if m},
                     key=lambda l: (lesson_number(l), l))
    out_dir = ROOT / "arquivos-trabalho" / f"analise-{re.sub(r'[^a-z0-9]+', '-', ramo.lower()).strip('-')}-{time.strftime('%Y-%m-%d')}"
    out_dir.mkdir(parents=True, exist_ok=True)
    allnotes, per = {}, collections.OrderedDict()
    for lid in lessons:
        ns = call("notesInfo", notes=call("findNotes", query=f'"tag:NEBLI::{lid}" -"tag:NEBLI::retirado*"'))
        short = collections.Counter(re.match(r"NEBLI::ordem::(.+)-\d+$", t).group(1) for n in ns for t in n["tags"]
                                    if re.match(r"NEBLI::ordem::(.+)-\d+$", t))
        main_short = max(short, key=short.get) if short else None

        def pos(n):
            for t in n["tags"]:
                m = re.match(rf"NEBLI::ordem::{re.escape(main_short or '~')}-(\d+)$", t)
                if m:
                    return int(m.group(1))
            return 9999
        ns.sort(key=pos)
        per[lid] = ns
        for n in ns:
            allnotes[n["noteId"]] = n
    cards = call("cardsInfo", cards=[c for n in allnotes.values() for c in n["cards"]])
    cinfo = {c["cardId"]: c for c in cards}
    tab = tabs(list(cinfo))
    # repetição: mesma resposta com frases parecidas, ou frases quase iguais, entre quaisquer notas do ramo
    io = re.compile(r"^nebli-[\w-]+-io-|^\s*$")  # oclusão de imagem: a frente é um id, não texto comparável
    items = [(nid, words(front(n["fields"])), answers(front(n["fields"]))) for nid, n in allnotes.items()
             if not io.match(clean(front(n["fields"])))]
    rep = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i], items[j]
            if not a[1] or not b[1]:
                continue
            jac = len(a[1] & b[1]) / len(a[1] | b[1])
            same_ans = bool(set(a[2]) & set(b[2]))
            if jac >= 0.6 or (same_ans and jac >= 0.35):
                rep.append((round(jac, 2), a[0], b[0]))
    rep.sort(reverse=True)
    lesson_of = {}
    for lid, ns in per.items():
        for n in ns:
            lesson_of.setdefault(n["noteId"], []).append(lid)
    marks = collections.defaultdict(set)
    for _, x, y in rep:
        marks[x].add("REP"); marks[y].add("REP")
    lines, rows = [], []
    for lid, ns in per.items():
        run = corrida(lid)
        esc = escopo(run)
        cols = collections.Counter()
        clin = num = sem_tab = velho = 0
        lines.append(f"\n######## {lesson_number(lid):02d} {lid}  (corrida: {run.name if run else '?'})")
        if esc:
            lines.append(f"ESCOPO objetivo: {esc.get('objetivo')}")
            lines.append("ESCOPO centrais: " + "; ".join(c[0] if isinstance(c, (list, tuple)) else str(c) for c in esc.get("centrais", [])))
        else:
            lines.append("ESCOPO: não declarado (aula feita antes de 13/10)")
        for k, n in enumerate(ns, 1):
            cs = [cinfo[c] for c in n["cards"] if c in cinfo]
            flag = max((c.get("flags", 0) for c in cs), default=0)
            own_col = next((t.rsplit("::", 1)[1] for t in n["tags"] if t.startswith(f"NEBLI::cor::{lid}::")), COR.get(flag, "-"))
            cols[own_col] += 1
            f = front(n["fields"])
            m = set(marks.get(n["noteId"], set()))
            if CLIN.search(full_sentence(f)):
                m.add("CLIN"); clin += 1
            if NUM.search(" ".join(answers(f))):
                m.add("NUM"); num += 1
            ts = [tab.get(c["cardId"]) for c in cs]
            if any(t is None or t["status"] != "ok" for t in ts):
                m.add("SEM-TAB"); sem_tab += 1
            elif any(not t["atual"] for t in ts):
                m.add("TAB-VELHO"); velho += 1
            origem = next((t.split("::")[-1] for t in n["tags"] if t.startswith("NEBLI::origem::")), "?")
            outras = [l for l in lesson_of[n["noteId"]] if l != lid]
            susp = all(c.get("queue") == -1 for c in cs)
            lines.append(f"{k:03d} [{own_col[:5]:5}] {origem[:7]:7} {'S' if susp else ' '} {n['noteId']} {full_sentence(f)[:170]}"
                         + (f"  <{','.join(sorted(m))}>" if m else "") + (f"  (também: {', '.join(o.split('-', 2)[2][:30] for o in outras)})" if outras else ""))
        rows.append((lid, len(ns), cols, clin, num, sem_tab, velho, bool(esc)))
    (out_dir / "frentes.txt").write_text("\n".join(lines) + "\n")
    rel = [f"# Análise de {ramo} — {time.strftime('%d/%m/%Y')}", "",
           "Sinais mecânicos para orientar a leitura; o julgamento (cobertura, ordem lógica, princípios antes dos detalhes, "
           "complementaridade, peso de ciclo básico, Tabs) é feito lendo `frentes.txt` e registrado abaixo.", "",
           "| Aula | Notas | verde | azul | rosa | CLIN | NUM | sem Tab | Tab antigo | ESCOPO |", "|---|---|---|---|---|---|---|---|---|---|"]
    for lid, n, cols, clin, num, st, ve, esc in rows:
        rel.append(f"| {lesson_number(lid):02d} {lid.split('-', 3)[3]} | {n} | {cols['verde']} | {cols['azul']} | {cols['rosa']} | {clin} | {num} | {st} | {ve} | {'sim' if esc else 'não'} |")
    rel += ["", f"## Possíveis repetições ({len(rep)} pares; similaridade de palavras e resposta em comum)", ""]
    for jac, x, y in rep[:150]:
        rel.append(f"- {jac} · {x} ({', '.join(l.split('-', 3)[3][:25] for l in lesson_of[x])}): {full_sentence(front(allnotes[x]['fields']))[:110]}"
                   f"\n  ↔ {y} ({', '.join(l.split('-', 3)[3][:25] for l in lesson_of[y])}): {full_sentence(front(allnotes[y]['fields']))[:110]}")
    rel += ["", "## Julgamento (preencher após ler frentes.txt)", "",
            "- Cobertura de cada aula e do conjunto:", "- Ordem lógica e progressão entre aulas (cards-ponte a acrescentar):",
            "- Princípios importantes sem card / detalhe antes do princípio:", "- Detalhes que não se complementam ou repetem:",
            "- Peso clínico/semiológico acima do ciclo básico:", "- Tabs (amostra lida):", "- Correções aplicadas:"]
    (out_dir / "RELATORIO.md").write_text("\n".join(rel) + "\n")
    print(f"{len(per)} aulas, {len(allnotes)} notas; {len(rep)} pares de possível repetição; relatório em {out_dir.relative_to(ROOT)}")
    for lid, n, cols, clin, num, st, ve, esc in rows:
        print(f"  {lesson_number(lid):02d} {lid.split('-', 3)[3][:40]:40} {n:4} notas  v{cols['verde']} a{cols['azul']} r{cols['rosa']}  CLIN {clin}  NUM {num}  semTab {st}  TabAntigo {ve}  ESCOPO {'sim' if esc else 'não'}")


if __name__ == "__main__":
    main()
