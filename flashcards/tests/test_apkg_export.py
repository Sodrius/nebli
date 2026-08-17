import subprocess, sys, zipfile
from pathlib import Path
from conftest import lesson
SCRIPTS=Path(__file__).parents[1]/"scripts"; VALID=SCRIPTS/"validar_deck_card_a_card.py"; FINAL=SCRIPTS/"finalizar_entrega_canonica.py"; sys.path.insert(0,str(SCRIPTS))
from apkg_utils import open_collection
from audit_apkg import audit


def test_finalizer_emits_real_audited_apkg(tmp_path):
    deck,data=lesson(tmp_path); report=tmp_path/"validation.json"; out=tmp_path/"out"
    p=subprocess.run([sys.executable,str(VALID),str(deck),"--out",str(report)],capture_output=True,text=True); assert p.returncode==0,p.stdout+p.stderr
    p=subprocess.run([sys.executable,str(FINAL),"--slug","aula","--deck-data",str(deck),"--validation-report",str(report),"--out-dir",str(out)],capture_output=True,text=True); assert p.returncode==0,p.stdout+p.stderr
    apkg=out/"aula.apkg"; assert apkg.is_file() and apkg.stat().st_size>0
    with zipfile.ZipFile(apkg) as package: assert "collection.anki2" in package.namelist() and "media" in package.namelist()
    with open_collection(apkg) as (db,_package,media,_member):
        assert db.execute("SELECT COUNT(*) FROM notes").fetchone()[0]==len(data["cards"]); assert db.execute("SELECT COUNT(*) FROM cards").fetchone()[0]==len(data["cards"]); assert "fluxo.png" in " ".join(media.values())
    result=audit(apkg,"NEBLI::UC99::P1::Fisiologia::Aula sintética"); assert result["passed"],result["errors"]; assert result["notes"]==result["cards"]==len(data["cards"])
