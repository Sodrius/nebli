#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consultar.py — régua de calibração das provas antigas da UC03, por AULA.

Espelha o papel do banco_slim.json e do blueprint-step1.md: é consultado durante a redação
para saber ATÉ ONDE a FMUSP costuma cobrar cada aula da UC03 — e NUNCA é colado no PDF.

O filtro é deliberadamente estreito: uma subquestão só é devolvida para uma aula se
(a) a área etiquetada na prova bate com a componente da aula E
(b) alguma `chave` da aula aparece no enunciado ou no gabarito.
É esse "E" que impede misturar conteúdo de aulas diferentes: questão de complemento não
aparece na aula de inflamação, questão de operon não aparece na aula de genética bacteriana.

Uso:
  python referencias-externas/uc03/consultar.py --slug micro-05-antibioticos-resistencia
  python referencias-externas/uc03/consultar.py --slug pat-07-inflamacao-aguda --desde 2023
  python referencias-externas/uc03/consultar.py --listar [--prova P2]
  python referencias-externas/uc03/consultar.py --termo "operon" --completo
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
AULAS = RAIZ / "banco" / "aulas_uc03.yml"
BASE = Path(__file__).resolve().parent / "provas-questoes.json"


def normalizar(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def carregar_aulas():
    try:
        import yaml
    except ImportError:
        sys.exit("pip install pyyaml")
    return yaml.safe_load(AULAS.read_text(encoding="utf-8"))["aulas"]


def codigos(aula):
    """Códigos de área da prova que podem pertencer a esta aula."""
    bruto = (aula.get("codigo_prova") or "").upper()
    cods = set(re.split(r"[/\-+ ]+", bruto)) - {""}
    if "BQ" in cods or "BM" in cods:
        cods |= {"BM"}          # a base normaliza BQ e BQ/BM em BM
    return cods


def contem(chave, texto):
    """Sigla ou palavra curta casa por limite de palavra; frase casa por substring
    (permite raiz truncada como 'hipoecog', 'radiotranspar')."""
    ch = normalizar(chave)
    if " " not in ch and len(ch) <= 5:
        return re.search(rf"(?<![a-z0-9]){re.escape(ch)}(?![a-z0-9])", texto) is not None
    return ch in texto


def casa(aula, q):
    """Devolve (chaves_no_enunciado, chaves_so_no_gabarito) ou None."""
    if not (codigos(aula) & set(q["componentes"])):
        return None
    enun = normalizar(q["enunciado"])
    gab = normalizar(q["gabarito"])
    no_enun = [c for c in aula.get("chaves", []) if contem(c, enun)]
    no_gab = [c for c in aula.get("chaves", []) if contem(c, gab) and c not in no_enun]
    if not (no_enun or no_gab):
        return None
    return no_enun, no_gab


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    ap.add_argument("--termo", help="busca livre no acervo, sem filtro de aula")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--prova", help="filtra por P1..P4")
    ap.add_argument("--desde", type=int, default=0, help="ano mínimo (ex.: 2023)")
    ap.add_argument("--completo", action="store_true", help="imprime gabarito inteiro")
    a = ap.parse_args()

    aulas = carregar_aulas()
    base = json.loads(BASE.read_text(encoding="utf-8"))

    if a.listar:
        for x in aulas:
            if a.prova and a.prova.upper() not in str(x["prova"]).upper():
                continue
            flag = " (provisório)" if x.get("provisorio") else ""
            print(f"{x['prova']:<11} {x['codigo_prova']:<6} {x['slug']:<48} {x['titulo']}{flag}")
        return

    if a.termo:
        alvo = normalizar(a.termo)
        hits = [q for q in base if alvo in normalizar(q["enunciado"] + " " + q["gabarito"])]
    elif a.slug:
        aula = next((x for x in aulas
                     if x["slug"] == a.slug or a.slug in (x.get("apelidos") or [])), None)
        if not aula:
            alvo = normalizar(a.slug)
            pistas = [x["slug"] for x in aulas
                      if any(t in normalizar(x["slug"]) for t in alvo.split("-") if len(t) > 3)]
            dica = ("\n  talvez: " + "\n  talvez: ".join(pistas[:5])) if pistas else ""
            sys.exit(f"slug desconhecido: {a.slug} (use --listar){dica}")
        print(f"# {aula['slug']} — {aula['titulo']}")
        print(f"# componente: {aula['componente']} ({aula['codigo_prova']}) · prova: {aula['prova']}"
              + (" · CRONOGRAMA PROVISÓRIO" if aula.get("provisorio") else ""))
        print("# Régua de calibração — nada daqui vai colado no PDF. O slide manda no ESCOPO;")
        print("# estas questões dizem o TETO histórico, e a E1 fica um degrau acima dele.\n")
        hits = []
        for q in base:
            r = casa(aula, q)
            if r:
                no_enun, no_gab = r
                hits.append(dict(q, _chaves=no_enun or no_gab, _forte=bool(no_enun)))
    else:
        sys.exit("use --slug, --termo ou --listar")

    hits = [q for q in hits if q["ano"] >= a.desde]
    if a.prova:
        hits = [q for q in hits if q["prova"].upper().startswith(a.prova.upper())]
    if not hits:
        print("(nenhuma subquestão no acervo 2015-2025 — aula sem evidência direta; "
              "calibrar pelo teto da componente em CALIBRACAO.md)")
        return

    for q in hits:
        ch = (" | chaves: " + ", ".join(q["_chaves"])) if q.get("_chaves") else ""
        marca = "" if q.get("_forte", True) else "  [eco — a chave só aparece no gabarito; confira se a subquestão é mesmo desta aula]"
        print(f"── [{q['ano']} {q['prova']}] {q['q']} ({q['tag']}){ch}{marca}")
        print(f"   P: {q['enunciado']}")
        gab = q["gabarito"] if a.completo else q["gabarito"][:400]
        if gab:
            print(f"   G: {gab}")
        print()
    anos = sorted({q["ano"] for q in hits}, reverse=True)
    print(f"# {len(hits)} subquestões · anos: {', '.join(map(str, anos))}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
