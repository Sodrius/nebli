"""Monta lotes cegos v3 (frente; frente + Extra só texto) e a calibração do juiz. Uso: make_batch.py dev|test <seed>"""
import json, re, subprocess, sys
sys.path.insert(0, "/Users/davisousa/NEBLI")
from nebli import card_mirror
which, seed = sys.argv[1], int(sys.argv[2])
noimg = lambda s: re.sub(r"<img[^>]*>", "", s or "")
authored = json.load(open(f"authors-{which}.json"))
natives = json.load(open(f"private-{which}-natives.json"))
records = [{"id": a["id"], "origin": "Autoral", "family": a["family"], "text": a["text"], "extra": a.get("extra", "")} for a in authored]
# vista só de texto: figuras saem das duas origens (o redator não tinha figura; imagem é avaliada à parte)
records += [{"id": str(n["id"]), "origin": "AnKing", "family": n["family"], "text": noimg(n["text"]), "extra": noimg(n["extra"]),
             "group_id": n.get("group_id")} for n in natives]
json.dump(records, open(f"private-input-{which}.json", "w"), ensure_ascii=False, indent=1)
for mode in ("front", "front_extra"):
    subprocess.run([sys.executable, "-m", "nebli.card_mirror", "build", "--input", f"{sys.path[0]}/arquivos-trabalho/calibracao-card-mirror-2026-10-02/v3/private-input-{which}.json",
                    "--output", f"{sys.path[0]}/arquivos-trabalho/calibracao-card-mirror-2026-10-02/v3/{which}-{mode}", "--seed", str(seed), "--mode", mode], check=True, cwd=sys.path[0])
cal = []
for n in json.load(open(f"private-judge-calibration-{which}.json")):
    cal.append({"family": n["family"], "text": card_mirror.normalize_field(noimg(n["text"]))[0],
                "extra": card_mirror.normalize_field(noimg(n["extra"]))[0]})
json.dump(cal, open(f"judge-calibration-{which}.json", "w"), ensure_ascii=False, indent=1)
print("ok", which, len(records))
