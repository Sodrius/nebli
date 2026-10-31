"""Correções do revisor (rodada 1, lote 3) nos autorais antigos de cinética reaproveitados: tirar negrito de dentro do cloze e pôr as
fórmulas no verso do organizador de dose. Backup em backup-autorais-antigos-lote3.json. Só escreve sem card na tela de Davi.
    /usr/bin/python3 corrige_antigos.py
"""
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita, em_tela  # noqa: E402

NIDS = [1792657545614, 1792624457204, 1792624458275, 1792624463275, 1792657541196, 1792657537231, 1792657544384, 1792624466325, 1792657541958]
EXTRA = {1792657541958: "- Loading dose = Cp·Vd/F: reaches the target level at once<br>- Maintenance dose = Cp·Cl·τ/F: replaces what clearance removes each interval"}
sem_b = lambda t: re.sub(r"\{\{c(\d+)::(.*?)\}\}", lambda m: "{{c%s::%s}}" % (m.group(1), re.sub(r"</?b>", "", m.group(2))), t)

A = Anki()
for _ in range(30):
    if not em_tela(A):
        break
    time.sleep(10)
else:
    raise SystemExit("Davi estudando; tentar depois")
notes = A("notesInfo", notes=NIDS)
(HERE / "backup-autorais-antigos-lote3.json").write_text(json.dumps(notes, ensure_ascii=False, indent=1), encoding="utf-8")
with escrita(A, "deck-prova dp3: autorais antigos sem negrito no cloze (revisor)", sync=False):
    for n in notes:
        f = {"Text": sem_b(n["fields"]["Text"]["value"])}
        if n["noteId"] in EXTRA:
            f["Extra"] = EXTRA[n["noteId"]]
        A("updateNoteFields", note={"id": n["noteId"], "fields": f})
for n in A("notesInfo", notes=NIDS):
    print(n["noteId"], n["fields"]["Text"]["value"][:110])
