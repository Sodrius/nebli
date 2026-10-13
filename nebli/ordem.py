"""Ordem da aula no Browser do Anki: cada nota leva NEBLI::ordem::<curto>-<NN> na sequência docente.

A coluna "Ordem da aula" do add-on nebli_decks mostra e ordena por essa tag (cards compartilhados
entram pela tag da aula em que estão sendo vistos). Antes de entregar um deck:

    python3 -m nebli.ordem verificar NEBLI::<lesson_id> [--plan <corrida>/plan.json]

Sai com código 1 se alguma nota da aula ficou sem posição, se o prefixo curto é usado por outra
aula ou se a ordem viva diverge do plano. No Browser: buscar "tag:NEBLI::<lesson_id>" e clicar no
cabeçalho "Ordem da aula" (adicionar a coluna uma vez, pelo botão direito no cabeçalho).
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

KEY = "nebliOrdem"
LABEL = "Ordem da aula"
ORDER = re.compile(r"^NEBLI::ordem::(.+)-(\d+)$", re.I)
BLOCK = re.compile(r"^NEBLI::objetivo::(.+)$", re.I)
LAST = (1, "", 0)


def tag(short, number):
    return f"NEBLI::ordem::{short}-{number:02d}"


def positions(tags):
    """[(prefixo, número)] de uma nota; compartilhada entre aulas tem uma posição por aula."""
    found = [ORDER.match(t) for t in tags]
    return sorted((m.group(1), int(m.group(2))) for m in found if m)


def dominant(tag_lists):
    """Prefixo mais comum no conjunto: a aula que está sendo vista."""
    count = collections.Counter(prefix for tags in tag_lists for prefix, _ in positions(tags))
    return max(sorted(count), key=count.get) if count else None


def sort_key(tags, main=None):
    """Nota sem posição vai para o fim; a aula dominante vem primeiro."""
    found = positions(tags)
    if not found:
        return LAST
    prefix, number = next((p for p in found if p[0] == main), found[0])
    return (0, "" if prefix == main else prefix, number)


def label(tags, main=None):
    found = positions(tags)
    if not found:
        return ""
    contextual = [number for prefix, number in found if prefix == main]
    numbers = contextual or sorted({number for _, number in found})
    return " | ".join(f"{number:02d}" for number in numbers)


def slide(evidence):
    """Primeiro slide citado na evidência do plano; exercício/prova sem slide devolve None."""
    found = re.search(r"slides?\s*(\d+)", evidence or "", re.I)
    return int(found.group(1)) if found else None


def check(lesson_tag, notes, others, plan=None):
    """notes: {nid: tags} da aula; others: {nid: tags} das demais notas NEBLI com tag de ordem."""
    problems, warnings = [], []
    main = dominant(notes.values())
    if main is None:
        return [f"nenhuma nota de {lesson_tag} tem NEBLI::ordem::*"], warnings, None
    missing = [nid for nid, tags in notes.items() if main not in dict(positions(tags))]
    if missing:
        problems.append(f"{len(missing)} nota(s) da aula sem posição '{main}-NN' (compartilhadas também "
                        f"precisam): {missing[:8]}")
    foreign = [nid for nid, tags in others.items() if main in dict(positions(tags))]
    if foreign:
        problems.append(f"prefixo '{main}' também usado fora da aula ({len(foreign)} nota(s)): escolher prefixo único")
    by_number = collections.defaultdict(list)
    for nid, tags in notes.items():
        for prefix, number in positions(tags):
            if prefix == main:
                by_number[number].append(nid)
    repeated = {n: ids for n, ids in by_number.items() if len(ids) > 1}
    if repeated:
        problems.append(f"posições repetidas: {dict(list(repeated.items())[:5])}")
    if plan:
        entries = sorted(plan["entries"], key=lambda e: e["order"])
        first = [(e["order"], slide(e.get("evid"))) for e in entries]
        seen = [s for _, s in first if s]
        if len(seen) < len(first):
            warnings.append(f"{len(first) - len(seen)} entrada(s) do plano sem slide em 'evid'")
        back = [(o, s) for (o, s), (_, prev) in zip(first[1:], first) if s and prev and s < prev]
        if back:
            # Gate duro (F-20261002-CLAUDE-09): o Browser tem de seguir os slides do primeiro ao último, sem voltar.
            problems.append(f"{len(back)} recuo(s) de slide na sequência (ordenar as entradas pelo slide; card que ilustra "
                            f"um slide anterior cita esse slide em 'evid'): {back[:6]}")
        expected = {tag(main, e["order"]) for e in entries}
        # compartilhados também precisam estar na aula com a posição desta aula (11/10: a delta só punha a posição)
        expected |= {s["ordem_tag"] for s in plan.get("compartilhados", {}).values() if s.get("ordem_tag")}
        live = {tag(main, n) for n in by_number}
        if expected - live:
            problems.append(f"posições do plano ausentes no Anki: {sorted(expected - live)[:6]}")
    return problems, warnings, main


def _live(lesson_tag):
    from nebli.decks import Anki
    call = Anki()
    def tags(query):
        ids = call("findNotes", query=query)
        return {n["noteId"]: n["tags"] for n in call("notesInfo", notes=ids)} if ids else {}
    notes = tags(f'"tag:{lesson_tag}"')
    others = {nid: t for nid, t in tags('"tag:NEBLI::ordem::*"').items() if nid not in notes}
    return notes, others


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    verify = sub.add_parser("verificar")
    verify.add_argument("lesson_tag", help="NEBLI::<lesson_id>")
    verify.add_argument("--plan")
    args = parser.parse_args(argv)
    notes, others = _live(args.lesson_tag)
    plan = json.loads(Path(args.plan).read_text(encoding="utf-8")) if args.plan else None
    problems, warnings, main_prefix = check(args.lesson_tag, notes, others, plan)
    print(f"{args.lesson_tag}: {len(notes)} notas, prefixo '{main_prefix}'")
    for text in warnings:
        print("aviso:", text)
    for text in problems:
        print("FALHA:", text)
    if not problems:
        print(f'ok. Browser: buscar "tag:{args.lesson_tag}" e ordenar pela coluna "{LABEL}".')
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
