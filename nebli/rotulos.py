"""Total de cards no nome dos decks NEBLI: "Antibióticos e resistência (112)".

O número é decoração; a identidade do deck é o nome canônico, sem ele. Quem lê
compara pelo canônico; quem escreve no Anki usa nebli.decks.escrita(), dentro da
qual o add-on nebli_decks deixa a árvore sem números. Sem Anki nem rede aqui.
"""
from __future__ import annotations

import re

ROOT = "NEBLI"
_LABEL = re.compile(r" \(\d+\)$")


def canonical(name):
    return "::".join(_LABEL.sub("", part) for part in name.split("::"))


def in_tree(name):
    """Árvore NEBLI e os filtrados de liberação no nível de cima ("NEBLI · Microbiologia: ...")."""
    top = canonical(name).split("::")[0]
    return top == ROOT or top.startswith(ROOT + " · ")


def labeled(name):
    return canonical(name) != name


def live_names(names, canonical_name):
    """Nomes vivos cujo canônico é exatamente o pedido (mais de um é conflito)."""
    return [n for n in names if canonical(n) == canonical_name]


def plan(decks, home_counts, filtered_counts=None, strip=False):
    """Passos [(did, último segmento desejado)] do mais raso ao mais fundo.

    decks: {did: nome vivo}; home_counts: {did: cards cujo deck de origem é did};
    filtered_counts: {did: cards hoje dentro de um deck filtrado}, que rotula só
    ele, porque esses cards já contam no deck de origem. Renomear um deck muda o
    caminho dos filhos, então cada passo troca apenas o último segmento. Dois
    decks com o mesmo canônico ficam de fora com o ramo inteiro e são relatados.
    """
    filtered_counts = filtered_counts or {}
    canon = {did: canonical(name) for did, name in decks.items() if in_tree(name)}
    seen, conflicts = {}, set()
    for did, path in canon.items():
        if path in seen:
            conflicts.add(path)
        seen[path] = did
    totals = {}
    for did, path in canon.items():
        parts = path.split("::")
        for i in range(1, len(parts) + 1):
            prefix = "::".join(parts[:i])
            totals[prefix] = totals.get(prefix, 0) + home_counts.get(did, 0)
    steps = []
    for did, path in sorted(canon.items(), key=lambda item: (item[1].count("::"), item[1])):
        if any(path == c or path.startswith(c + "::") for c in conflicts):
            continue
        leaf = path.rsplit("::", 1)[-1]
        total = filtered_counts.get(did, totals[path])
        steps.append((did, leaf if strip else f"{leaf} ({total})"))
    return steps, sorted(conflicts)
