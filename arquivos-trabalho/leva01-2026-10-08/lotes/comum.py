"""Helpers dos lotes da leva 1: imagem no padrão (cabe na tela sem rolar) e montagem do JSON de mudanças."""
import json
from pathlib import Path

W = Path(__file__).resolve().parents[1]
IMG_DIR = W / "img"


def img(nome):
    # max-height: cabe na tela do celular/desktop sem rolar (comentário de Davi, nid 1790972067861)
    return f'<img src="{nome}" style="max-width:100%;max-height:52vh">'


_SNAP = None


def _visto(nid):
    """Comentário que embasou a decisão: snapshot da leva (atualizar o snapshot ao reler comentários novos)."""
    global _SNAP
    if _SNAP is None:
        _SNAP = {n["noteId"]: n["fields"].get("NEBLI_Comentario", {}).get("value", "")
                 for n in json.loads((W / "notas-atual.json").read_text())}
    return _SNAP.get(nid)


def mud(nid, text=None, extra=None, media=(), corrigido=False, familia="", motivo="", outros=None, retirar=None, ordem=None, cor=None):
    f = {}
    if text is not None: f["Text"] = text
    if extra is not None: f["Extra"] = extra
    if outros: f.update(outros)
    return {"nid": nid, "comentario_visto": _visto(nid), "fields": f, "media": [str(IMG_DIR / m) for m in media], "corrigido": corrigido,
            "familia": familia, "motivo": motivo, **({"retirar": retirar} if retirar else {}), **({"ordem": ordem} if ordem else {}), **({"cor": cor} if cor else {})}


def salvar(nome, lista):
    p = W / "lotes" / f"{nome}.json"
    p.write_text(json.dumps(lista, ensure_ascii=False, indent=1))
    print(p, len(lista))
