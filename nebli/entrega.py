"""Entrega da aula no Drive do Davi (pasta montada), com os nomes padrão.

    python3 -m nebli.entrega "<UCxx>/<Componente>/<NN - Aula>" --nome "<Nome da aula>" \\
        [--e1 <pdf>] [--deck <apkg>] [--slides <arquivo já na pasta>] [--uc-apkg <apkg>]

Grava `<Nome> - E1.pdf` e `<Nome>.apkg` na pasta da aula, renomeia o slide para `<Nome> - slides.<ext>`
(sem sobrescrever outro arquivo) e, com --uc-apkg, atualiza `NEBLI - <UCxx>.apkg` na pasta da UC.
Nunca mexe em compartilhamento. A pasta é a do Google Drive para desktop; o conector não envia binário grande.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path.home() / "Library/CloudStorage/GoogleDrive-dpbdes@gmail.com/Mon Drive/MEGA DRIVE/Medicina/Material de estudo/A - Primeiro ano (2026)"


def names(nome, slides=None):
    return {"e1": f"{nome} - E1.pdf", "deck": f"{nome}.apkg",
            "slides": f"{nome} - slides{Path(slides).suffix if slides else '.pdf'}"}


def deliver(folder, nome, e1=None, deck=None, slides=None, uc_apkg=None, root=ROOT):
    folder = Path(root) / folder
    if not folder.is_dir():
        raise SystemExit(f"pasta da aula não encontrada no Drive montado: {folder}")
    target = names(nome, slides)
    done = []
    for kind, source in (("e1", e1), ("deck", deck)):
        if source:
            shutil.copy2(source, folder / target[kind]); done.append(target[kind])
    if slides:
        source = Path(slides)
        old = source if source.is_file() else folder / slides
        new = folder / target["slides"]
        if not old.is_file():
            raise SystemExit(f"slide não encontrado: {old}")
        if old != new:
            if new.exists():
                raise SystemExit(f"já existe {new.name}; não sobrescrevo o slide")
            shutil.copy2(old, new); done.append(f"{old.name} → {new.name} (cópia; original preservado)")
    if uc_apkg:
        uc = Path(folder).relative_to(root).parts[0]
        shutil.copy2(uc_apkg, Path(root) / uc / f"NEBLI - {uc}.apkg"); done.append(f"{uc}/NEBLI - {uc}.apkg")
    return done


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("pasta"); parser.add_argument("--nome", required=True)
    parser.add_argument("--e1"); parser.add_argument("--deck"); parser.add_argument("--slides"); parser.add_argument("--uc-apkg")
    args = parser.parse_args(argv)
    for item in deliver(args.pasta, args.nome, args.e1, args.deck, args.slides, args.uc_apkg):
        print("ok:", item)
    for path in sorted((ROOT / args.pasta).iterdir()):
        print("  ", path.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
