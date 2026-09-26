"""CLI deliberadamente offline: prepara contratos para o Android e o Drive."""
from __future__ import annotations
import argparse, hashlib, json, sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from nebli.registry import connect

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "nebli.example.yaml"

def load_config(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))
def db_for(config: dict[str, Any]) -> sqlite3.Connection: return connect(ROOT / config["state_path"])
def now() -> str: return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""): digest.update(chunk)
    return digest.hexdigest()

def seed_pilot(db: sqlite3.Connection, config: dict[str, Any]) -> dict[str, Any]:
    lesson = {"lesson_id":"2026-uc03-patologia-38-inflamacao-aguda","year":2026,"uc":"UC03","component":"Patologia","content_number":38,"title":"Inflamação aguda","source_folder_id":"1apmeYFBAs8fHkc1wMw7AIsGdHUOtIxT3","output_folder_id":config["drive"]["pilot_output_folder_id"]}
    db.execute("""INSERT INTO lesson(lesson_id,year,uc,component,content_number,title,source_folder_id,output_folder_id) VALUES(:lesson_id,:year,:uc,:component,:content_number,:title,:source_folder_id,:output_folder_id) ON CONFLICT(lesson_id) DO UPDATE SET source_folder_id=excluded.source_folder_id,output_folder_id=excluded.output_folder_id""", lesson)
    sources = [
      {"source_id":"src-uc03-pato-38-transcricao","drive_file_id":"1O5qLt4JANr93Hv7tEXeZ8TddmsiHKAjw","title":"Inflamação aguda - transcrição.pdf","mime_type":"application/pdf","drive_url":"https://drive.google.com/file/d/1O5qLt4JANr93Hv7tEXeZ8TddmsiHKAjw/view","modified_time":"2026-09-07T10:53:15.429Z","byte_size":2762877,"role":"lecture_transcript"},
      {"source_id":"src-uc03-pato-38-e1-legacy","drive_file_id":"1uvoBwMJA4HPSb-pTQmtLx9wXzkSylTR4","title":"Inflamação aguda - etapas 1 a 3.pdf","mime_type":"application/pdf","drive_url":"https://drive.google.com/file/d/1uvoBwMJA4HPSb-pTQmtLx9wXzkSylTR4/view","modified_time":"2026-09-07T10:53:12.625Z","byte_size":2698130,"role":"legacy_e1"}]
    for source in sources:
        db.execute("""INSERT INTO source(source_id,lesson_id,drive_file_id,title,mime_type,drive_url,modified_time,byte_size,role,downloaded_at,access_status) VALUES(:source_id,:lesson_id,:drive_file_id,:title,:mime_type,:drive_url,:modified_time,:byte_size,:role,:downloaded_at,:access_status) ON CONFLICT(drive_file_id) DO UPDATE SET title=excluded.title,modified_time=excluded.modified_time,byte_size=excluded.byte_size,role=excluded.role""", {**source,"lesson_id":lesson["lesson_id"],"downloaded_at":now(),"access_status":"connector_downloaded"})
    db.execute("INSERT OR IGNORE INTO run(run_id,lesson_id,target,status,note) VALUES(?,?,?,?,?)", ("bootstrap-uc03-pato-38",lesson["lesson_id"],config["device_target"],"sources_resolved","Android: pacote será importado manualmente; não há ADB/AnkiConnect nesta máquina."))
    db.commit(); return lesson

def write_source_manifest(db: sqlite3.Connection, lesson_id: str) -> Path:
    lesson = dict(db.execute("SELECT * FROM lesson WHERE lesson_id=?", (lesson_id,)).fetchone())
    sources = [dict(row) for row in db.execute("SELECT * FROM source WHERE lesson_id=? ORDER BY source_id", (lesson_id,))]
    document = {"schema_version":1,"generated_at":now(),"lesson":lesson,"sources":sources,"target":"android_import","state":"sources_resolved","note":"Arquivos foram obtidos pelo conector Drive. O pacote APKG ainda não foi produzido nem instalado."}
    path = ROOT / "artifacts" / lesson_id / "bootstrap" / "sources.json"; path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); return path

def stage_publication(db: sqlite3.Connection, lesson_id: str, path: Path) -> dict[str, Any]:
    if not path.is_file(): raise SystemExit(f"arquivo não existe: {path}")
    folder=db.execute("SELECT output_folder_id FROM lesson WHERE lesson_id=?",(lesson_id,)).fetchone()
    if not folder: raise SystemExit(f"aula desconhecida: {lesson_id}")
    key=f"{lesson_id}:{path.name}"; digest=sha256(path)
    db.execute("""INSERT INTO publication(artifact_key,lesson_id,local_path,sha256,drive_folder_id,status) VALUES(?,?,?,?,?,?) ON CONFLICT(artifact_key) DO UPDATE SET local_path=excluded.local_path,sha256=excluded.sha256,status='staged'""",(key,lesson_id,str(path.resolve()),digest,folder["output_folder_id"],"staged")); db.commit()
    return {"artifact_key":key,"file":str(path.resolve()),"sha256":digest,"parent_folder_id":folder["output_folder_id"],"status":"staged"}

def record_publication(db: sqlite3.Connection, lesson_id: str, filename: str, drive_file_id: str) -> None:
    key=f"{lesson_id}:{filename}"
    result=db.execute("UPDATE publication SET drive_file_id=?, status='published', published_at=? WHERE artifact_key=? AND status='staged'",(drive_file_id,now(),key))
    if result.rowcount != 1: raise SystemExit(f"publicação não encontrada ou já confirmada: {key}")
    db.commit()

def status(db: sqlite3.Connection) -> None:
    report={"lessons":[dict(row) for row in db.execute("SELECT lesson_id,title,output_folder_id FROM lesson")],"sources":[dict(row) for row in db.execute("SELECT source_id,title,role,access_status FROM source")],"publications":[dict(row) for row in db.execute("SELECT artifact_key,status,drive_file_id FROM publication")]}; print(json.dumps(report,ensure_ascii=False,indent=2))

def main() -> None:
    p=argparse.ArgumentParser(prog="nebli"); p.add_argument("--config",type=Path,default=DEFAULT_CONFIG); sub=p.add_subparsers(dest="command",required=True)
    sub.add_parser("bootstrap-pilot"); m=sub.add_parser("source-manifest"); m.add_argument("lesson_id"); s=sub.add_parser("stage-publication"); s.add_argument("lesson_id"); s.add_argument("file",type=Path); r=sub.add_parser("record-publication"); r.add_argument("lesson_id"); r.add_argument("filename"); r.add_argument("drive_file_id"); sub.add_parser("status")
    args=p.parse_args(); config=load_config(args.config); db=db_for(config)
    if args.command=="bootstrap-pilot":
        lesson=seed_pilot(db,config); print(write_source_manifest(db,lesson["lesson_id"]))
    elif args.command=="source-manifest": print(write_source_manifest(db,args.lesson_id))
    elif args.command=="stage-publication": print(json.dumps(stage_publication(db,args.lesson_id,args.file),ensure_ascii=False))
    elif args.command=="record-publication": record_publication(db,args.lesson_id,args.filename,args.drive_file_id)
    else: status(db)
if __name__ == "__main__": main()
