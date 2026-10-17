"""Apaga (com backup) as notas criadas por um apply interrompido desta corrida: só notas sem comentário, com a tag da aula, criadas depois do último
'parcial-apagada' do journal. uso: limpa_parcial.py <corrida>"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / "NEBLI"))
from nebli.decks import Anki, escrita
run = Path(sys.argv[1]); plan = json.loads((run / "plan.json").read_text()); tag = f"NEBLI::{plan['lesson_id']}"
ev = [json.loads(l) for l in open(run / "journal.jsonl")]
corte = max([i for i, d in enumerate(ev) if d.get("op") == "parcial-apagada"] or [-1])
nids = [d["nid"] for d in ev[corte + 1:] if d.get("op") == "addNote"]
A = Anki(); info = [i for i in A("notesInfo", notes=nids) if i]
keep = {int(k) for k in plan["compartilhados"]}
info = [i for i in info if i["noteId"] not in keep and tag in i["tags"] and not i["fields"].get("NEBLI_Comentario", {}).get("value")]
bk = run / f"parcial-apagada-backup-{len(list(run.glob('parcial-apagada-backup*.json')))}.json"
bk.write_text(json.dumps(info, ensure_ascii=False, indent=1))
with escrita(A, f"{plan['short']} limpeza parcial"):
    if info: A("deleteNotes", notes=[i["noteId"] for i in info])
with open(run / "journal.jsonl", "a") as f: f.write(json.dumps({"op": "parcial-apagada", "nids": [i["noteId"] for i in info]}) + "\n")
print(len(info), "apagadas; backup", bk.name)
