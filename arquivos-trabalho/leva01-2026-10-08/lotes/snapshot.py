"""Relê UC08+UC03 vivos para notas-atual.json (base de 'comentario_visto' dos lotes). Rodar ao reler comentários."""
import json, urllib.request
from pathlib import Path
W = Path(__file__).resolve().parents[1]
def call(a, **p):
    return json.load(urllib.request.urlopen(urllib.request.Request("http://localhost:8765", json.dumps({"action": a, "version": 6, "params": p}).encode())))["result"]
info = call("notesInfo", notes=call("findNotes", query="deck:NEBLI*UC08* OR deck:NEBLI*UC03*"))
(W / "notas-atual.json").write_text(json.dumps(info, ensure_ascii=False))
print(len(info))
