"""Lista os cards de estrutura sem imagem (ou só com imagem do slide) de uma corrida. python3 -m nebli.sem_imagem <corrida>"""
import json
import re
import sys
from pathlib import Path

from nebli.gates import has_img, only_slide_img, visible

run = Path(sys.argv[1]); p = json.loads((run / "plan.json").read_text())
for e in p["entries"]:
    if e.get("kind") in ("text", "autoral") and (not has_img(e) or only_slide_img(e)) and not e.get("sem_imagem") and not e.get("slide_sem_alternativa"):
        print(f"{e['key']:34} {e['origin'][:8]:8} {e.get('evid','')[:9]:9} {'SLIDE' if has_img(e) else '-----'} {visible(e)[:150]}")
