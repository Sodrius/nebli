"""Aplica correções de cards vivos (comentários de Davi e famílias) com backup, readback e marcador CORRIGIDO.

    python3 -m nebli.corrige <mudancas.json> [--simular] [--data 08,10,26]

mudancas.json = [{"nid": 123, "comentario_visto": "<texto lido ao decidir>", "fields": {"Text": "...", "Extra": "..."}, "media": ["caminho/arquivo.jpg"],
                  "corrigido": true, "familia": "A", "motivo": "..."}]
  "retirar": "<motivo-curto>" suspende os cards e marca NEBLI::retirado::<motivo> (redundante/sem ganho), sem CORRIGIDO.

Protocolo de 08/10 (F-20261008-CODEX-03, F-20261008-CLAUDE-02):
- backup integral da nota e dos cards antes (`<pasta>/corrige-antes-<ts>.json`); journal por operação;
- nota que Davi tem na tela (`guiCurrentCard`) fica para o próximo lote, sem bloquear o resto;
- só com `corrigido: true` (correção feita e verificada): dessuspende os cards suspensos da nota e anexa na linha de
  baixo do comentário `CORRIGIDO, DD, MM, YY.`, preservando todo o texto anterior;
- comentário vivo diferente de `comentario_visto` → não marca nem dessuspende (crítica nova não tratada);
- readback dos campos; divergência vai para o recibo e o comando sai com erro.
Depois, rodar `python3 -m nebli.reconcilia <corrida>` nas corridas das aulas afetadas.
"""
from __future__ import annotations

import argparse
import base64
import json
import re
from datetime import datetime
from pathlib import Path

from nebli.decks import Anki, em_tela, escrita, now


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("mudancas"); ap.add_argument("--simular", action="store_true")
    ap.add_argument("--data", default=datetime.now().strftime("%d, %m, %y"))
    a = ap.parse_args(argv)
    path = Path(a.mudancas)
    pasta = path.parent
    muds = json.loads(path.read_text())
    A = Anki()
    from nebli.delta import same
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    nids = [m["nid"] for m in muds]
    antes = A("notesInfo", notes=nids)
    faltam = [n for n, i in zip(nids, antes) if not i]
    if faltam:
        raise SystemExit(f"notas inexistentes: {faltam}")
    cards = {i["noteId"]: A("cardsInfo", cards=i["cards"]) for i in antes}
    (pasta / f"corrige-antes-{ts}.json").write_text(json.dumps({"notas": antes, "cards": cards}, ensure_ascii=False))
    tela = em_tela(A)
    adiadas = [m["nid"] for m in muds if m["nid"] in tela]
    lote = [m for m in muds if m["nid"] not in tela]
    print(f"{len(lote)} notas no lote; adiadas por estarem na tela: {adiadas}")
    if a.simular:
        for m in lote:
            info = next(i for i in antes if i["noteId"] == m["nid"])
            muda = [f for f, v in m.get("fields", {}).items() if not same(info["fields"][f]["value"], v)]
            print(m["nid"], "campos:", muda, "| corrigido" if m.get("corrigido") else "")
        return
    journal = (pasta / "journal.jsonl").open("a")
    log = lambda **k: (journal.write(json.dumps({"at": now(), **k}, ensure_ascii=False) + "\n"), journal.flush())
    marcador = f"CORRIGIDO, {a.data}."
    feitos, dessusp, novos = [], [], []
    with escrita(A, f"corrige {path.name}"):
        for m in lote:
            for mp in m.get("media", []):
                p = Path(mp)
                A("storeMediaFile", filename=p.name, data=base64.b64encode(p.read_bytes()).decode())
            info = A("notesInfo", notes=[m["nid"]])[0]
            fields = {f: v for f, v in m.get("fields", {}).items() if not same(info["fields"][f]["value"], v)}
            c = info["fields"].get("NEBLI_Comentario", {}).get("value", "")
            visto = m.get("comentario_visto")
            if m.get("corrigido") and visto is not None and re.sub(r"(<br>|\s)+$", "", c) != re.sub(r"(<br>|\s)+$", "", visto):
                # F-20261008-CLAUDE-03: Davi comentou de novo depois da leitura; a correção não tratou o texto novo
                novos.append(m["nid"]); m = dict(m, corrigido=False)
            if m.get("corrigido") and c and not re.sub(r"(<br>|\s)+$", "", c).endswith(marcador):  # crítica nova depois do marcador pede outro
                fields["NEBLI_Comentario"] = c + "<br>" + marcador
            if fields:
                A("updateNoteFields", note={"id": m["nid"], "fields": fields})
            if m.get("ordem"):  # "an01-104": troca a tag de posição da aula (Browser), sem mexer em histórico
                pref = "NEBLI::ordem::" + m["ordem"].rsplit("-", 1)[0] + "-"
                velhas = [t for t in info["tags"] if t.startswith(pref)]
                if velhas: A("removeTags", notes=[m["nid"]], tags=" ".join(velhas))
                A("addTags", notes=[m["nid"]], tags="NEBLI::ordem::" + m["ordem"])
            if m.get("cor"):  # {"aula": lesson_id, "cor": "verde|azul|rosa"}: tag da aula + bandeira = maior cor entre aulas
                aula, cor = m["cor"]["aula"], m["cor"]["cor"]
                velhas = [t for t in info["tags"] if t.startswith(f"NEBLI::cor::{aula}::")]
                if velhas: A("removeTags", notes=[m["nid"]], tags=" ".join(velhas))
                A("addTags", notes=[m["nid"]], tags=f"NEBLI::cor::{aula}::{cor}")
                tags = [t for t in info["tags"] if t not in velhas] + [f"NEBLI::cor::{aula}::{cor}"]
                rank = {"verde": 3, "azul": 2, "rosa": 1}; flag_de = {"verde": 3, "azul": 4, "rosa": 5}
                maior = max((t.rsplit("::", 1)[1] for t in tags if t.startswith("NEBLI::cor::")), key=lambda c: rank.get(c, 0))
                for x in A("cardsInfo", cards=info["cards"]):
                    if x["flags"] in (0, 3, 4, 5):  # marca pessoal (1, 2, 6, 7) fica
                        A("setSpecificValueOfCard", card=x["cardId"], keys=["flags"], newValues=[flag_de[maior]], warning_check=True)
                log(op="cor", nid=m["nid"], aula=aula, cor=cor, bandeira=flag_de[maior])
            if m.get("retirar"):  # redundante/sem ganho: sai da revisão sem apagar estudo nem comentário
                A("suspend", cards=info["cards"]); A("addTags", notes=[m["nid"]], tags=f"NEBLI::retirado::{m['retirar']}")
                log(op="retirado", nid=m["nid"], motivo=m.get("motivo")); feitos.append(m["nid"]); continue
            susp = [x["cardId"] for x in A("cardsInfo", cards=info["cards"]) if x["queue"] == -1] if m.get("corrigido") else []
            if susp:
                A("unsuspend", cards=susp); dessusp += susp
            log(op="corrige", nid=m["nid"], campos=sorted(fields), dessuspensos=susp, familia=m.get("familia"), motivo=m.get("motivo"))
            feitos.append(m["nid"])
    depois = {i["noteId"]: i for i in A("notesInfo", notes=feitos)}
    div = [(m["nid"], f) for m in lote for f, v in m.get("fields", {}).items() if not same(depois[m["nid"]]["fields"][f]["value"], v)]
    ainda_susp = [c for c in dessusp if A("areSuspended", cards=[c])[0]]
    rec = {"em": now(), "mudancas": path.name, "feitos": feitos, "adiadas": adiadas, "dessuspensos": dessusp,
           "divergentes": div, "comentario_novo_sem_marcador": novos, "ainda_suspensos": ainda_susp, "marcador": marcador}
    (pasta / f"corrige-recibo-{ts}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in rec.items()}, ensure_ascii=False))
    if div or ainda_susp:
        raise SystemExit(f"readback divergente: {div} {ainda_susp}")


if __name__ == "__main__":
    main()
