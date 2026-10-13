"""Total|dessuspensos|novos disponíveis no nome: "Antibióticos e resistência (112|80|25)".

O número é decoração; a identidade do deck é o nome canônico, sem ele. Quem lê
compara pelo canônico; quem escreve no Anki usa nebli.decks.escrita(), dentro da
qual o add-on nebli_decks deixa a árvore sem números. Sem Anki nem rede aqui.
"""
from __future__ import annotations

import re

ROOT = "NEBLI"
_LABEL = re.compile(r" \(\d+(?:\|\d+\|\d+)?\)$")


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


def plan(decks, home_counts, filtered_counts=None, strip=False, home_stats=None, filtered_stats=None):
    """Passos [(did, último segmento desejado)] do mais raso ao mais fundo.

    decks: {did: nome vivo}; home_counts: {did: cards cujo deck de origem é did};
    home_stats: {did: (dessuspensos, novos disponíveis)}; sem ele, mantém formato antigo.
    filtered_counts: {did: cards hoje dentro de um deck filtrado}, que rotula só
    ele, porque esses cards já contam no deck de origem. Renomear um deck muda o
    caminho dos filhos, então cada passo troca apenas o último segmento. Dois
    decks com o mesmo canônico ficam de fora com o ramo inteiro e são relatados.
    """
    filtered_counts = filtered_counts or {}
    filtered_stats = filtered_stats or {}
    canon = {did: canonical(name) for did, name in decks.items() if in_tree(name)}
    seen, conflicts = {}, set()
    for did, path in canon.items():
        if path in seen:
            conflicts.add(path)
        seen[path] = did
    totals = {}
    stats = {}
    for did, path in canon.items():
        parts = path.split("::")
        for i in range(1, len(parts) + 1):
            prefix = "::".join(parts[:i])
            totals[prefix] = totals.get(prefix, 0) + home_counts.get(did, 0)
            if home_stats is not None:
                available, new = home_stats.get(did, (0, 0))
                prev_available, prev_new = stats.get(prefix, (0, 0))
                stats[prefix] = (prev_available + available, prev_new + new)
    steps = []
    for did, path in sorted(canon.items(), key=lambda item: (item[1].count("::"), item[1])):
        if any(path == c or path.startswith(c + "::") for c in conflicts):
            continue
        leaf = path.rsplit("::", 1)[-1]
        total = filtered_counts.get(did, totals[path])
        if strip:
            label = leaf
        elif home_stats is not None:
            available, new = filtered_stats.get(did, stats.get(path, (0, 0)))
            label = f"{leaf} ({total}|{available}|{new})"
        else:
            label = f"{leaf} ({total})"
        steps.append((did, label))
    return steps, sorted(conflicts)
