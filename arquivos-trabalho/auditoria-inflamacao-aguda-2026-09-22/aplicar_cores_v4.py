"""Aplica a semântica de cores definida por Davi para o piloto.

Vermelho (1): card a melhorar/remover/rever.
Verde (3): High Yield explícito na origem AnKing.
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from inspecionar_v2 import call
from recalibrar_v3 import DECK, PLAN, HIGH_YIELD_TAG, key_tag, load_current, map_entries, selected_entries

RED_TO_REVIEW = {
    1790095122911, 1790099855279, 1790099859373, 1790099860750,
    1790099861466, 1790099863854, 1790099865259, 1790099865260,
    1790100260031, 1790100260032, 1790080243792,
}

notes, cards = load_current()
by_tag = map_entries(notes)
keep, _ = selected_entries()
green = {
    card_id
    for entry in keep if HIGH_YIELD_TAG in entry.get("source_tags", [])
    for card_id in by_tag[key_tag(entry)]["cards"]
}
if RED_TO_REVIEW & green:
    raise RuntimeError("Um card não pode ser simultaneamente vermelho e verde")

# Antes de mudar: não tomar outra bandeira do usuário como propriedade do sistema.
for color in (2, 3, 4, 5, 6, 7):
    unexpected = set(call("findCards", query=f'deck:"{DECK}" flag:{color}')) - green
    if unexpected:
        raise RuntimeError(f"Bandeira {color} pessoal/conflitante: {sorted(unexpected)}")
current_red = set(call("findCards", query=f'deck:"{DECK}" flag:1'))
if current_red != RED_TO_REVIEW:
    raise RuntimeError("A lista vermelha mudou; não aplicar automaticamente")

for card_id in green:
    call("setSpecificValueOfCard", card=card_id, keys=["flags"], newValues=[3])

actual_red = set(call("findCards", query=f'deck:"{DECK}" flag:1'))
actual_green = set(call("findCards", query=f'deck:"{DECK}" flag:3'))
if actual_red != RED_TO_REVIEW or actual_green != green:
    raise RuntimeError("Cores não conferem após escrita")

out = Path(__file__).resolve().parent / "revisao-v2"
package = out / "Inflamacao aguda.apkg"
call("exportPackage", deck=DECK, path=str(package.resolve()), includeSched=True)
record = {
    "at": datetime.now(timezone.utc).isoformat(),
    "deck": DECK,
    "red": {"meaning": "melhorar/remover/rever", "cards": sorted(actual_red)},
    "green": {"meaning": "High Yield explícito do AnKing", "cards": sorted(actual_green)},
    "package_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
}
(out / "colors-v4.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(record, ensure_ascii=False, indent=2))
