"""F-20261110-CLAUDE-02/03: nomenclatura da UC08 AN11 no deck vivo (nome da aula/Terminologia Anatômica, nome mínimo inequívoco).
Kenhub: regera a figura com o rótulo novo (nebli.kenhub.renomear). AnKing: troca 'triângulo cisto-hepático' pelo 'trígono' da aula.
IO: Remarks em PT. Backup dos campos antes; nota em tela pulada."""
import json, sys, re
from pathlib import Path
from nebli.decks import Anki, escrita, em_tela
from nebli.kenhub.renomear import renomear
HERE = Path(__file__).resolve().parent
KH = {1792713392530: "Porta do fígado", 1792713389103: "Lobo direito", 1792713389356: "Lobo esquerdo",
      1792713391025: "Lobo caudado", 1792713391279: "Lobo quadrado", 1792713389602: "Ligamento falciforme",
      1792713392031: "Ligamento venoso", 1792713396053: "Lâmina posterior do ligamento coronário",
      1792713396550: "Ligamento triangular direito", 1792713396866: "Ligamento triangular esquerdo",
      1792713395453: "Área nua"}
TXT = {1792713407379: [("triângulo cisto-hepático", "trígono cisto-hepático")],
       1792713407879: [("triângulo cisto-hepático", "trígono cisto-hepático")]}
ROM = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
A = Anki(); seco = "--seco" in sys.argv
io = {n["noteId"]: n for n in A("notesInfo", notes=A("findNotes", query='"ID (hidden):nebli-uc08-an11-io-seg-*"'))}
plano = []
for nid, nome in KH.items():
    n = A("notesInfo", notes=[nid])[0]; base = {k: v["value"] for k, v in n["fields"].items()}
    novos, midia = renomear(base, nome, HERE / "img", Path(A("getMediaDirPath")))
    plano.append((nid, base, {k: v for k, v in novos.items() if k in base}, midia))
for nid, troca in TXT.items():
    n = A("notesInfo", notes=[nid])[0]; base = {k: v["value"] for k, v in n["fields"].items()}
    t = base["Text"]
    for a, b in troca:
        assert a in t, (nid, a); t = t.replace(a, b)
    plano.append((nid, base, {"Text": t}, {}))
for nid, n in io.items():
    base = {k: v["value"] for k, v in n["fields"].items()}
    r = re.sub(r"Segment (\w+)", r"Segmento \1", base["Remarks"]).replace("(caudate lobe)", "(lobo caudado)")
    if r != base["Remarks"]: plano.append((nid, base, {"Remarks": r}, {}))
for nid, b, novo, m in plano:
    print(nid, {k: (re.sub("<[^>]+>", "", b[k])[:50], re.sub("<[^>]+>", "", v)[:50]) for k, v in novo.items() if k in ("Nome PT", "Text", "Remarks")}, list(m))
if seco: sys.exit()
json.dump({str(nid): b for nid, b, _, _ in plano}, open(HERE / "backup" / "an11-campos-antes.json", "w"), ensure_ascii=False, indent=1)
with escrita(A, "correcao-uc08-an11-nomenclatura", sync=False):
    tela = em_tela(A); log = []
    for nid, b, novo, midia in plano:
        if nid in tela: print("em tela, pulada:", nid); continue
        for nomearq, cam in midia.items():
            A("storeMediaFile", filename=nomearq, path=str(Path(cam).resolve()))
        A("updateNoteFields", note={"id": nid, "fields": novo}); log.append(nid)
    json.dump(log, open(HERE / "an11-aplicado.json", "w"))
print("ok", len(plano))
