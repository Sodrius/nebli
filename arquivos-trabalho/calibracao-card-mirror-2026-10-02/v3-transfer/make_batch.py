"""Transferência: os mesmos 24 alvos do Operon antes (autorais instalados) e depois (reescritos por espelhos), contra os mesmos 24 AnKing."""
import json, re, subprocess, sys
R = "/Users/davisousa/NEBLI"; V = R + "/arquivos-trabalho/calibracao-card-mirror-2026-10-02/v3-transfer/"
sys.path.insert(0, R)
from nebli import card_mirror
noimg = lambda s: re.sub(r"<img[^>]*>", "", s or "")
nat = [dict(n, text=noimg(n["text"]), extra=noimg(n["extra"])) for n in json.load(open(V + "private-natives-A.json"))]
sets = {"before": json.load(open(V + "private-before.json")),
        "after": [{"id": a["id"], "origin": "Autoral", "family": a["family"], "text": a["text"], "extra": a.get("extra", "")}
                  for a in json.load(open(V + "authors-after.json"))]}
for name, authored in sets.items():
    for a in authored:
        a["extra"] = noimg(a["extra"])
    json.dump(authored + nat, open(V + f"private-input-{name}.json", "w"), ensure_ascii=False, indent=1)
    subprocess.run([sys.executable, "-m", "nebli.card_mirror", "build", "--input", V + f"private-input-{name}.json",
                    "--output", V + name, "--seed", str({"before": 811, "after": 812}[name]), "--mode", "front_extra"], check=True, cwd=R)
cal = [{"family": n["family"], "text": card_mirror.normalize_field(noimg(n["text"]))[0],
        "extra": card_mirror.normalize_field(noimg(n["extra"]))[0]} for n in json.load(open(V + "private-natives-calibration.json"))]
json.dump(cal, open(V + "judge-calibration.json", "w"), ensure_ascii=False, indent=1)
