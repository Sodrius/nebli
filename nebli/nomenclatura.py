"""Nomenclatura oficial em deck de anatomia (F-20261022-CLAUDE-10, gate duro).

Davi (22/10): “gate-hard: deck de anatomia sempre checar se a nomenclatura oficial está batendo com a do deck”.

O nome que o deck mostra para uma estrutura (Nome PT das notas do Kenhub, rótulo de oclusão do slide, termo de card em PT) tem de ser:
  1. o nome que o material da aula usa (lâminas, roteiro, perguntas, transcrição, apostila), ou
  2. o nome de um livro brasileiro da bibliografia (Moore, Gray, Machado; texto em ~/NEBLI-privado/kenhub/glossario/*.txt).
O próprio Kenhub NÃO atesta: a tradução dele às vezes é de Portugal (“bolbo raquidiano”) ou não é a da aula.
E se o nome do deck não está na aula mas um sinônimo dele está (campo Sinonimos ou NOMES_ALTERNATIVOS abaixo), reprova:
o deck tem de mostrar o nome que a professora usa. A correção vai no spec/plano (NOMENCLATURA = {nome do deck: nome da aula}).
"""
from __future__ import annotations

import re
import unicodedata
from functools import lru_cache
from pathlib import Path

GLOSSARIO = Path.home() / "NEBLI-privado" / "kenhub" / "glossario"
ARTIGOS = {"o", "a", "os", "as", "do", "da", "dos", "das", "de", "no", "na"}
# Pares que a mesma estrutura recebe em fontes diferentes (Kenhub PT × uso brasileiro/aula). Cada linha: grafias equivalentes.
NOMES_ALTERNATIVOS = [
    ("bulbo", "bolbo raquidiano", "bulbo raquidiano", "medula oblonga"),
    ("ducto colédoco", "colédoco", "ducto biliar comum"),
    ("papila maior do duodeno", "papila duodenal maior"),
    ("ampola hepatopancreática", "ampola de vater"),
    ("ducto pancreático", "ducto de wirsung", "ducto pancreático principal"),
    ("trígono cisto-hepático", "triângulo de calot", "trígono de calot", "triângulo cisto-hepático"),
    ("porta do fígado", "hilo hepático", "hilo do fígado"),
    ("veia porta", "veia porta do fígado", "veia porta hepática"),
    ("ligamento hepatogástrico", "ligamento hepático gástrico"),
    ("ligamento hepatoduodenal", "ligamento hepático duodenal"),
    ("aqueduto cerebral", "aqueduto mesencefálico", "aqueduto do mesencéfalo"),
    ("filamentos radiculares", "radículas", "radículas de nervo espinal"),
    ("sulco lateral anterior", "sulco anterolateral", "sulco pré-olivar"),
    ("sulco lateral posterior", "sulco posterolateral", "sulco retro-olivar"),
    ("sulco intermédio posterior", "sulco intermédio dorsal"),
    ("oliva", "núcleos olivares", "oliva (núcleos olivares)"),
    ("quarto ventrículo", "4.º ventrículo", "iv ventrículo"),
]


def _singular(w: str) -> str:
    for fim, novo in (("oes", "ao"), ("aes", "ao"), ("ais", "al"), ("eis", "el"), ("res", "r"), ("ns", "m")):
        if len(w) > len(fim) + 2 and w.endswith(fim):
            return w[:-len(fim)] + novo
    return w[:-1] if len(w) > 3 and w.endswith("s") else w


def norm(t: str) -> str:
    t = unicodedata.normalize("NFD", (t or "").lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    pal = [_singular(w) for w in re.findall(r"[a-z0-9]+", t)]
    while pal and pal[0] in ARTIGOS:
        pal = pal[1:]
    return " ".join(pal)


def _corpo(textos) -> str:
    juntado = " ".join(re.sub(r"-\s*\n\s*", "", t) for t in textos)
    return " " + norm(juntado) + " "


@lru_cache(maxsize=1)
def _livros() -> dict:
    return {f.stem: _corpo([f.read_text(errors="ignore")]) for f in sorted(GLOSSARIO.glob("*.txt"))} if GLOSSARIO.exists() else {}


def _variantes(nome: str) -> list[str]:
    n = norm(nome)
    for grupo in NOMES_ALTERNATIVOS:
        if n in {norm(g) for g in grupo}:
            return [g for g in grupo if norm(g) != n]
    return []


def _partes(nome: str) -> list[str]:
    """“Corno lateral da medula espinal” → ["corno lateral", "medula espinal"]; parênteses e posição (rostral/caudal) à parte."""
    base = re.sub(r"\(([^)]*)\)", r" , \1 ,", nome)
    return [x for x in (norm(p) for p in re.split(r",|\s+(?:d[oa]s?|de|e)\s+", base)) if x]


def _oficial(n: str, aula: str, livros: dict) -> bool:
    return f" {n} " in aula or any(f" {n} " in t for t in livros.values())


def conferir(nomes, corpus_aula, livros=None):
    """nomes: [(chave, nome_no_deck, [sinônimos])]. Devolve a lista de reprovações (vazia = ok)."""
    aula = _corpo(corpus_aula)
    livros = _livros() if livros is None else {k: _corpo([v]) for k, v in livros.items()}
    probs = []
    for chave, nome, sinonimos in nomes:
        n = norm(nome)
        if not n:
            continue
        if f" {n} " not in aula:  # a aula usa outra grafia conhecida da mesma estrutura: o deck mostra a da aula
            alt = [v for v in _variantes(nome) if f" {norm(v)} " in aula]
            if alt:
                probs.append(f"[nomenclatura] {chave}: o deck diz {nome!r}, a aula diz {alt[0]!r} — usar o nome da aula")
                continue
        if _oficial(n, aula, livros) or all(_oficial(x, aula, livros) for x in _partes(nome)):
            continue
        alt = [x for x in sinonimos if len(norm(x)) >= 5 and f" {norm(x)} " in aula]
        if alt:
            probs.append(f"[nomenclatura] {chave}: o deck diz {nome!r}, a aula diz {alt[0]!r} — usar o nome da aula")
        else:
            ruins = [x for x in _partes(nome) if not _oficial(x, aula, livros)]
            probs.append(f"[nomenclatura] {chave}: {nome!r} não está na aula nem em livro brasileiro (Moore, Gray, Machado): {ruins}")
    return probs


def nomes_do_plano(entries):
    """Nomes em PT que um plan.json mostra: Nome PT das notas do Kenhub e rótulos das oclusões do slide."""
    out = []
    for e in entries:
        f = e.get("fields", {})
        if f.get("Nome PT"):
            sin = [s.strip() for s in re.split(r"[;,]", re.sub(r"<[^>]+>", "", f.get("Sinonimos", ""))) if s.strip()]
            out.append((e["key"], re.sub(r"<[^>]+>", "", f["Nome PT"]).strip(), sin))
        elif e.get("kind") == "slideio" and e.get("rotulo") and "(rect)" not in e["rotulo"]:
            out.append((e["key"], e["rotulo"], []))
    return out
