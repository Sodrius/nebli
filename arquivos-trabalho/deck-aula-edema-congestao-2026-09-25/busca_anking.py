import json, sys
from anki import *
AK = '"deck:Referências::Anking Step Deck"'
Q = {
 "O1-def": ['edema', 'hyperemia', '"passive congestion"', 'congestion cyanosis', '"active hyperemia"', 'anasarca', 'hydrothorax', 'hydropericardium', '"ascites"'],
 "O3-starling": ['starling', 'oncotic', '"hydrostatic pressure"', '"filtration coefficient"', 'K_f', 'interstitial lymphatics', '"lymphatic drainage"', '"net filtration"'],
 "O4-mech": ['lymphedema', 'filariasis', '"peau d\'orange"', 'kwashiorkor edema', '"pitting edema"', 'nonpitting', 'hypoalbuminemia edema', '"venous obstruction"', '"sodium retention"', '"effective circulating volume"', 'aldosterone edema', 'periorbital edema'],
 "O5-exud": ['transudate', 'exudate', 'transudative', 'exudative'],
 "O6-hf": ['"heart failure cells"', 'hemosiderin-laden', '"right heart failure"', '"left heart failure"', '"heart failure" RAAS', '"heart failure" sodium', 'jugular venous distension', '"heart failure" edema'],
 "O7-pulm": ['"pulmonary edema"', 'frothy', 'cardiogenic', 'noncardiogenic', 'non-cardiogenic'],
 "O8-nephrotic": ['nephrotic edema', 'nephrotic hypoalbuminemia', 'nephrotic albumin', 'nephrotic sodium'],
 "O9-cirr": ['"portal hypertension" ascites', 'splanchnic vasodilation', 'hepatorenal', 'cirrhosis ascites', 'cirrhosis albumin'],
 "O10-nutmeg": ['nutmeg', 'centrilobular congestion', '"congestive hepatopathy"', 'centrilobular necrosis', '"zone III" congestion', '"zone 3" hepatocytes'],
 "O11-ards": ['ARDS', '"acute respiratory distress"', '"hyaline membrane"', '"diffuse alveolar damage"'],
}
res = {}
for obj, qs in Q.items():
    for q in qs:
        try: nids = call("findNotes", query=f"{AK} {q}")
        except Exception as e: print("ERR", q, e); continue
        for n in nids: res.setdefault(n, set()).add(f"{obj}:{q}")
        print(f"{obj:12s} {q:40s} {len(nids)}")
json.dump({str(k): sorted(v) for k,v in res.items()}, open("cand_anking_hits.json","w",encoding="utf-8"), ensure_ascii=False)
print("total notes", len(res))
