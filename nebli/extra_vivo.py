"""Acrescenta imagem ao Extra de notas NEBLI mantidas numa refação (pedidos de Davi nos comentários: "imagem"), com backup do campo antes.

    python3 -m nebli.extra_vivo <corrida> [--simular]

Lê spec.EXTRA_VIVO = {nid: "<nome>"} e envia img/<SHORT>-<nome>.png; anexa <img> ao fim do Extra se ainda não estiver lá.
Backup em <corrida>/extra-vivo-backup.json. Não toca no campo NEBLI_Comentario nem em outra nota.
"""
import base64
import importlib.util
import json
import sys
from pathlib import Path

from nebli.decks import Anki, escrita


def main(argv):
    run = Path(argv[0]).resolve(); simular = "--simular" in argv
    sys.path.insert(0, str(run.parents[1]))
    spec_mod = importlib.util.spec_from_file_location("spec", run / "spec.py"); spec = importlib.util.module_from_spec(spec_mod); spec_mod.loader.exec_module(spec)
    pedidos = getattr(spec, "EXTRA_VIVO", {})
    A = Anki(); backup = {}; feitos = []
    with escrita(A, f"extra vivo {spec.SHORT}", sync=False):
        for nid, nome in pedidos.items():
            arq = f"{spec.SHORT}-{nome}.png"
            n = A("notesInfo", notes=[nid])[0]
            extra = n["fields"]["Extra"]["value"]
            if arq in extra:
                continue
            backup[str(nid)] = extra
            if simular:
                feitos.append(nid); continue
            if not A("retrieveMediaFile", filename=arq):
                A("storeMediaFile", filename=arq, data=base64.b64encode((run / "img" / arq).read_bytes()).decode())
            novo = (extra + "<br>" if extra.strip() else "") + f'<img src="{arq}" width="360">'
            A("updateNoteFields", note={"id": nid, "fields": {"Extra": novo}})
            if arq not in A("notesInfo", notes=[nid])[0]["fields"]["Extra"]["value"]:
                raise SystemExit(f"readback falhou em {nid}")
            feitos.append(nid)
    if not simular and backup:
        p = run / "extra-vivo-backup.json"
        old = json.loads(p.read_text()) if p.exists() else {}
        old.update({k: v for k, v in backup.items() if k not in old})
        p.write_text(json.dumps(old, ensure_ascii=False, indent=1))
    print(f"{len(feitos)} notas com imagem nova no Extra" + (" (simulação)" if simular else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
