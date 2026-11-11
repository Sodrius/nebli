"""Monta revisor-autorais-contexto.json: para cada autoral do plano, motivação, fonte literal com localizador
(unidade do percurso + trecho da transcrição/monitoria/Machado) e a busca real da E4 (semântica + cobertura.tsv).
Nada é inventado: trechos são recortes literais dos arquivos da corrida; candidatos vêm de busca/semantica.jsonl."""
from pathlib import Path
import json, re, unicodedata, csv, sys

R = Path(__file__).parent
sys.path.insert(0, str(R))
import curadoria, plano, textos

P = json.loads((R / "plan.json").read_text())
MOT = json.loads((R / "motivacoes.json").read_text())["motivacoes"]
SEM = {}
for l in (R / "busca/semantica.jsonl").read_text().splitlines():
    if l.strip():
        d = json.loads(l); SEM[d["chave"]] = d
COB = {r["chave"]: r for r in csv.DictReader(open(R / "busca/cobertura.tsv"), delimiter="\t")}
UNI = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"===== página (\d+) =====\n(.*?)(?=\n===== página |\Z)", (R / "fontes/slides.txt").read_text(), re.S)}
TRANS = {"t1": "fontes/t1-diencefalo.min.txt", "t2": "fontes/t2-telencefalo.min.txt", "t3": "fontes/t3-irrigacao.min.txt", "t4": "fontes/t4-pratica.min.txt", "ap": "fontes/apostila-guia.txt"}
LIVRO = ["livros/machado-cap6-diencefalo.txt", "livros/machado-cap7-telencefalo.txt", "livros/machado-cap9-vascularizacao.txt"]
MON = ["fontes/gaka-paginas.txt"]

norm = lambda s: unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def trans_de(u):
    return "t1" if u <= 21 else "t2" if u <= 42 else "ap" if u <= 46 else "t3" if u <= 59 else "t4"


def termos(text, item_termos):
    ts = [strip(x) for x in re.findall(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", text)]
    ts = [t for t in ts if len(t) >= 3 and not re.fullmatch(r"[\d+ ]+", t)]
    return [t for t in ts] + list(item_termos)


def trecho(arquivo, ts, minutos=None):
    linhas = (R / arquivo).read_text().splitlines()
    cand = list(enumerate(linhas))
    if minutos:
        a, b = minutos
        dentro = [(i, l) for i, l in cand if (m := re.match(r"\[(\d+)\]", l)) and a - 1 <= int(m.group(1)) <= b + 1]
        cand = dentro + cand
    for t in ts:
        nt = norm(t)
        for i, l in cand:
            if nt and nt in norm(l):
                txt = l.strip()
                if not txt.startswith("["):  # livro/monitoria quebrados em linhas curtas: parágrafo em volta
                    txt = " ".join(x.strip() for x in linhas[max(0, i - 3): i + 7])
                if len(txt) > 900:
                    k = norm(txt).find(nt); txt = txt[max(0, k - 400): k + 450]
                return txt, i + 1
    return None, None


TERMOS_EXTRA = {}
ROW = {}
for row in curadoria.R:
    u, ck, tipo, nid = row[0], row[1], row[2], row[3]
    ROW[f"sh-{nid}" if tipo in ("res", "an01") else ck] = (u, ck)
ITEM_DE = {k: it for it in plano.ITENS for k in it[6]}
ITEM_U = {}
for it in plano.ITENS:
    ITEM_U.setdefault(it[0], it)

cards = {}
todas = [(e["key"], e) for e in P["entries"]] + [(f"sh-{k}", v) for k, v in P["compartilhados"].items()]
for key, e in todas:
    if str(e.get("origin", "")).casefold() != "autoral":
        continue
    u, ck = ROW[key]
    it = ITEM_DE.get(ck) or ITEM_U.get(u)
    text = (e.get("fields") or {}).get("Text", "")
    ts = TERMOS_EXTRA.get(key, []) + termos(text, it[5] if it else [])
    fonte_loc = it[4] if it else ""
    mins = None
    if m := re.search(r"min (\d+)\s*[-–]\s*(\d+)", fonte_loc):
        mins = (int(m.group(1)), int(m.group(2)))
    elif m := re.search(r"min (\d+)", fonte_loc):
        mins = (int(m.group(1)), int(m.group(1)))
    fontes = [{"arquivo": "fontes/slides.txt", "trecho": UNI[u],
               "localizador": f"Percurso da fala do professor (aula sem lâminas), unidade {u}; {fonte_loc}"}]
    arq = TRANS[trans_de(u)]
    t, ln = trecho(arq, ts, mins)
    if t:
        fontes.append({"arquivo": arq, "trecho": t, "localizador": f"Transcrição {trans_de(u).upper()}, linha {ln} ([minuto] no início do trecho)"})
    for arq2 in (MON if 43 <= u <= 46 else []) + LIVRO:
        t2, ln2 = trecho(arq2, ts)
        if t2:
            fontes.append({"arquivo": arq2, "trecho": t2, "localizador": f"{arq2}, linha {ln2}"})
            break
    s = SEM.get(ck) or next((SEM[k] for k in (it[6] if it else []) if k in SEM), None)
    cob = COB.get(ck) or next((COB[k] for k in (it[6] if it else []) if k in COB), None)
    busca = {"descricao": (f"Busca semântica E4 '{s['consulta']}' em {len(s['acervos'])} acervos ({', '.join(s['acervos'])}); seções AnKing da aula lidas inteiras (busca/secoes)." if s else "Seções AnKing da aula lidas inteiras (busca/secoes) e palavra-chave em busca/anking-autorais.txt."),
             "candidatos": [{"acervo": c["acervo"], "nid": c["nid"], "hy": c.get("hy", ""), "frente": c["frente"]} for c in (s["top"][:6] if s else [])],
             "decisao": (cob["decisao"] if cob else "") or next((textos.AU_FONTE.get(key) for _ in [0] if key in textos.AU_FONTE), "") or
                        "Nenhum candidato lido cobra esta relação da aula na forma do professor; a nota da reserva UC07 (feita da transcrição em 22/10) é reaproveitada com ID e histórico."}
    mot = next((m["id"] for m in MOT if key in (m.get("atendida_por") or [])), None)
    c = {"origin": "Autoral", "fontes": fontes, "busca": busca,
         "contexto": {"aula": P.get("lesson_id"), "unidade": u, "item_do_mapa": (it[3] if it else ""), "bloco": e.get("bloco", "")}}
    if mot:
        c["motivacao"] = mot
    elif it:
        c["motivacao"] = {"necessidade": it[3], "reconstruir": it[3]}
    cards[key] = c

(R / "revisor-autorais-contexto.json").write_text(json.dumps({"cards": cards}, ensure_ascii=False, indent=1))
sem_trans = [k for k, c in cards.items() if len(c["fontes"]) < 2]
print(len(cards), "autorais; só com o percurso (sem trecho literal da transcrição/livro):", sem_trans)
