#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""GATE do deck-aula: PRÓ-COBERTURA (hard) + ANTI-REDUNDÂNCIA (aviso), num passo.

- Cobertura: todo conceito do spec cobertura-<slug>.yml (subtópico -> conceitos,
  escrito a partir da E1) precisa de >=1 card. LACUNA => exit 1 (gate-hard).
- Redundância: dentro de cada subtópico, flaga cards que testam a MESMA resposta
  clozada ou têm frente quase idêntica (Jaccard) — candidatos a poda. Aviso (não trava).
- Carga: total de cards vs banda peso×rendimento (informativo).

Uso:  python flashcards/scripts/verificar_cobertura_deck.py <slug> [--apkg CAMINHO] [--strict-redundancia]
Exit: 0 ok | 1 LACUNA (ou redundância dura com --strict-redundancia) | 2 erro de setup
"""
import sys, os, re, html, zipfile, sqlite3, tempfile, argparse, itertools
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
try: import yaml
except ImportError: print("pip install pyyaml"); sys.exit(2)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STOP = set("a o e de da do que com para por em no na the of and is are to as an".split())
# palavras de domínio comuns: não distinguem o FATO testado (evita falso-positivo
# ao comparar cards que só compartilham o template "X disease is GSD type Y").
DOMAIN = set(("glycogen glicogênio glicogenio disease doença doenca storage enzyme enzima "
    "type tipo caused deficiency deficiência also known associated characterized presents "
    "blood glucose glicose acid via reaction reação forma form cell célula cellular "
    "increased decreased causes cause is are of the que uma pela pelo com sua seu").split())

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s)
    s = re.sub(r"\{\{c\d+::(.*?)(::.*?)?\}\}", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()

def answers(field0):
    out = []
    for m in re.finditer(r"\{\{c\d+::(.*?)(?:::.*?)?\}\}", field0):
        a = re.sub(r"<[^>]+>", "", m.group(1))
        a = html.unescape(a).strip().lower().strip(" .,:;()[]")
        if a: out.append(a)
    return out

def toks(s):
    return {w for w in re.findall(r"[a-zà-ú0-9]+", s.lower()) if len(w) > 2 and w not in STOP}

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

def load_cards(apkg):
    z = zipfile.ZipFile(apkg)
    cn = [n for n in z.namelist() if n.startswith("collection.anki")][0]
    tmp = tempfile.mkdtemp(); p = os.path.join(tmp, "c.anki2")
    open(p, "wb").write(z.read(cn))
    c = sqlite3.connect(p); out = []
    for (flds,) in c.execute("select flds from notes"):
        parts = flds.split("\x1f")
        f0 = parts[0]
        front = clean(f0)
        extra = clean(parts[1]) if len(parts) > 1 else ""
        ans = answers(f0)
        # assinatura do FATO = tokens distintivos da frente + respostas (sem domínio)
        sig = (toks(front) | {w for a in ans for w in toks(a)}) - DOMAIN
        out.append({"front": front, "extra": extra, "ans": ans,
                    "hay": (front + " " + extra).lower(), "sig": sig})
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug"); ap.add_argument("--apkg", default=None)
    ap.add_argument("--strict-redundancia", action="store_true")
    ap.add_argument("--jaccard", type=float, default=0.70)
    args = ap.parse_args()

    spec_p = os.path.join(RAIZ, "flashcards", "curadoria", f"cobertura-{args.slug}.yml")
    if not os.path.exists(spec_p): print(f"x spec ausente: {spec_p}"); sys.exit(2)
    spec = yaml.safe_load(open(spec_p, encoding="utf-8"))
    apkg = args.apkg
    if not apkg:
        d = os.path.join(RAIZ, "flashcards", "cards-nebli")
        cand = [p for p in os.listdir(d) if p.endswith(".apkg")]
        if len(cand) == 1: apkg = os.path.join(d, cand[0])
        else: print("informe --apkg (há vários .apkg)"); sys.exit(2)
    cards = load_cards(apkg)
    print(f"deck: {os.path.basename(apkg)} | {len(cards)} notas\n")

    # ---- COBERTURA (hard) + atribuição de cada card ao subtópico de melhor match ----
    lacunas = []; cobertos = 0; total = 0
    card_subt = [None] * len(cards)
    subt_score = [{} for _ in cards]
    print("== COBERTURA ==")
    for subt, conceitos in spec.items():
        linhas = []
        for cid, alts in conceitos.items():
            total += 1; hits = 0
            for i, cd in enumerate(cards):
                if any(a.lower() in cd["hay"] for a in alts):
                    hits += 1; subt_score[i][subt] = subt_score[i].get(subt, 0) + 1
            if hits == 0: linhas.append((cid, "LACUNA")); lacunas.append(f"{subt}::{cid}")
            else: linhas.append((cid, f"ok({hits})")); cobertos += 1
        print(f"  {subt}")
        for cid, v in linhas:
            print(f"     {'x' if v=='LACUNA' else 'v'} {cid:30} {v}")
    for i in range(len(cards)):
        if subt_score[i]:
            card_subt[i] = max(subt_score[i], key=subt_score[i].get)

    # ---- REDUNDÂNCIA (aviso) — dentro de cada subtópico ----
    print("\n== REDUNDÂNCIA (candidatos a poda) ==")
    dups = []
    by_subt = {}
    for i, s in enumerate(card_subt):
        by_subt.setdefault(s or "??", []).append(i)
    for s, idxs in by_subt.items():
        # testam o MESMO fato = assinatura distintiva (frente+resposta, sem domínio) quase igual
        for i, j in itertools.combinations(idxs, 2):
            jac = jaccard(cards[i]["sig"], cards[j]["sig"])
            if jac >= args.jaccard:
                dups.append((s, f"mesmo fato (J={jac:.2f})",
                             [cards[i]["front"][:66], cards[j]["front"][:66]]))
    if dups:
        for s, why, fronts in dups:
            print(f"  ! [{s}] {why}")
            for f in fronts: print(f"      - {f}")
    else:
        print("  (nenhum candidato — sem cards testando o mesmo fato)")

    # ---- resumo ----
    print(f"\nconceitos {cobertos}/{total} cobertos | LACUNAS {len(lacunas)} | redundância-candidatos {len(dups)}")
    if lacunas:
        print("GATE FALHOU — LACUNAS:"); [print("   -", l) for l in lacunas]; sys.exit(1)
    if dups and args.strict_redundancia:
        print("GATE FALHOU — redundância (strict)."); sys.exit(1)
    print("GATE OK — E1 coberta." + (f" ({len(dups)} candidatos a poda p/ revisar)" if dups else ""))
    sys.exit(0)

if __name__ == "__main__":
    main()
