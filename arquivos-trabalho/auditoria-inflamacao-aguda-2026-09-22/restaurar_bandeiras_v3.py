"""Restaura a semântica pessoal de vermelho: cartão a revisar/remover/melhorar.

Os IDs são a leitura de flag:1 imediatamente anterior à recalibração v3.
Não representam yield do AnKing.
"""
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

from inspecionar_v2 import call
from recalibrar_v3 import DECK

RED_TO_REVIEW = [
    1790095122911, 1790099855279, 1790099859373, 1790099860750,
    1790099861466, 1790099863854, 1790099865259, 1790099865260,
    1790100260031, 1790100260032, 1790080243792,
]

current = call("findCards", query=f'deck:"{DECK}" flag:1')
for card_id in current:
    call("setSpecificValueOfCard", card=card_id, keys=["flags"], newValues=[0])
for card_id in RED_TO_REVIEW:
    call("setSpecificValueOfCard", card=card_id, keys=["flags"], newValues=[1])
after = call("findCards", query=f'deck:"{DECK}" flag:1')
if set(after) != set(RED_TO_REVIEW):
    raise RuntimeError("Bandeiras não foram restauradas exatamente")
record = {
    "at": datetime.now(timezone.utc).isoformat(),
    "deck": DECK,
    "meaning": "revisar, remover ou melhorar (inclusive imagem); não yield",
    "cards": after,
}
path = Path(__file__).resolve().parent / "revisao-v2" / "flags-v3.json"
package = path.parent / "Inflamacao aguda.apkg"
call("exportPackage", deck=DECK, path=str(package.resolve()), includeSched=True)
record["package_sha256"] = hashlib.sha256(package.read_bytes()).hexdigest()
path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(record, ensure_ascii=False, indent=2))
