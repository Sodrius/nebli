#!/usr/bin/env python3
"""verificar_imagem_card.py — GATE de imagem×card (feedback 2026-07-16).

Garante que a imagem de um card TREINA o alvo daquele card. Nasceu de um estoque
onde figuras de visão-geral de capítulo, prints de texto e imagens reusadas foram
coladas em cards de conceito específico (o erro nº 1 do Davi).

Três camadas, barato -> forte:
  L0  detector de REUSO (deterministico): mesma imagem em >=2 cards de alvo
      diferente vira suspeita (parte do reuso e' legitima -> a L1 decide).
  L1  JUIZ MULTIMODAL: manda imagem + texto do card (cloze revelado) + Extra pro
      Claude vision. Rubrica -> MATCH / WEAK / MISMATCH + motivo + is_text_shot.
  L2  ACAO/GATE: MISMATCH ou print-de-texto -> remove <img>, marca img::substituir
      + NEBLI::img_gate::fail (card nao sobe assim). WEAK -> NEBLI::img_gate::weak.
      MATCH -> NEBLI::img_gate::ok (re-runs pulam).

Uso:
  python verificar_imagem_card.py --slug histo-11-orgaos-linfaticos        # dry-run (so relatorio)
  python verificar_imagem_card.py --all --apply                            # roda tudo e aplica acoes
  python verificar_imagem_card.py --nid 1783971583409                      # 1 card (hook de novo card)

Requer ANTHROPIC_API_KEY no ambiente (mesmo padrao de monitor_email_anking.py).
Sem a key, roda so L0 (reuso) + heuristica, sem o juiz semantico.
Nunca muta com o Reviewer aberto (checa guiCurrentCard).
"""
from __future__ import annotations
import argparse, base64, collections, datetime as dt, json, os, re, sys, urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ANKI = "http://localhost:8765"
API = "https://api.anthropic.com/v1/messages"
MODEL = "claude-haiku-4-5-20251001"          # vision, barato — 1 call por card
OK, WEAK, FAIL = "NEBLI::img_gate::ok", "NEBLI::img_gate::weak", "NEBLI::img_gate::fail"
OUT = Path("arquivos-trabalho/gate-imagem")


def anki(action, **params):
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        ANKI, data=json.dumps({"action": action, "version": 6, "params": params}).encode(),
        headers={"Content-Type": "application/json"})))
    if r.get("error"):
        raise RuntimeError("%s: %s" % (action, r["error"]))
    return r["result"]


def frontfield(f):
    for n in ("Text", "Front", "Pergunta", "Cloze"):
        if n in f:
            return n
    return list(f.keys())[0]


def plain(h):
    return re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", re.sub(r"\{\{c\d+::|\}\}", " ", h or ""))).strip()


def media_type(fn):
    e = Path(fn).suffix.lower()
    return {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".gif": "image/gif", ".webp": "image/webp"}.get(e, "image/png")


RUBRIC = (
    "You are a flashcard image auditor. A cloze card tests ONE specific fact (the text "
    "between {{c1::...}}). An image is GOOD only if it visually trains THAT specific fact.\n"
    "Bad patterns to catch: (a) a whole-chapter/whole-body OVERVIEW figure on a specific-concept "
    "card; (b) an image that is really a SCREENSHOT OF TEXT (a paragraph), not a diagram; "
    "(c) an image about a neighboring concept that does not depict the card's target.\n"
    "Reply with ONLY a JSON object: "
    '{\"verdict\":\"MATCH|WEAK|MISMATCH\",\"is_text_screenshot\":true|false,'
    '\"image_shows\":\"<=12 words\",\"why\":\"<=20 words\"}'
)


def judge(img_bytes, fn, card_text, extra, key):
    content = [
        {"type": "image", "source": {"type": "base64", "media_type": media_type(fn),
                                     "data": base64.b64encode(img_bytes).decode()}},
        {"type": "text", "text": "CARD (target in brackets): %s\nEXTRA: %s\n\n%s" % (
            card_text, extra[:400], RUBRIC)},
    ]
    body = json.dumps({"model": MODEL, "max_tokens": 200,
                       "messages": [{"role": "user", "content": content}]}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "content-type": "application/json", "x-api-key": key,
        "anthropic-version": "2023-06-01"})
    r = json.load(urllib.request.urlopen(req))
    txt = "".join(b.get("text", "") for b in r.get("content", []))
    m = re.search(r"\{.*\}", txt, re.S)
    return json.loads(m.group(0)) if m else {"verdict": "WEAK", "why": "parse-fail", "image_shows": txt[:40], "is_text_screenshot": False}


def set_tags(nid, add=None, remove=None):
    if remove:
        anki("removeTags", notes=[nid], tags=" ".join(remove))
    if add:
        anki("addTags", notes=[nid], tags=" ".join(add))


def strip_first_img(nid, note, fn):
    """Remove a 1a ocorrencia da imagem fn de todos os campos da nota."""
    fields = {}
    for name, v in note["fields"].items():
        val = v["value"]
        new = re.sub(r'<img[^>]*src="%s"[^>]*>' % re.escape(fn), "", val, count=1)
        if new != val:
            fields[name] = new
    if fields:
        anki("updateNoteFields", note={"id": nid, "fields": fields})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug"); ap.add_argument("--nid", type=int)
    ap.add_argument("--all", action="store_true"); ap.add_argument("--apply", action="store_true")
    ap.add_argument("--recheck", action="store_true", help="reavalia mesmo cards ja ok")
    a = ap.parse_args()

    if a.apply:
        try:
            if anki("guiCurrentCard"):
                sys.exit("ABORTA: Reviewer ativo — feche o estudo p/ aplicar.")
        except RuntimeError as e:
            if "not currently active" not in str(e) and "not available" not in str(e).lower():
                raise

    if a.nid:
        query = "nid:%d" % a.nid
    elif a.slug:
        query = 'tag:"NEBLI::%s"' % a.slug
    elif a.all:
        query = "tag:NEBLI::*"
    else:
        sys.exit("informe --nid, --slug ou --all")
    if not a.recheck:
        query += ' -tag:"%s"' % OK

    notes = anki("notesInfo", notes=anki("findNotes", query=query))
    # L0 — reuso: mapa imagem -> alvos distintos (informa o relatorio)
    img2t = collections.defaultdict(set)
    for n in notes:
        f = n["fields"]; tgt = (re.findall(r"\{\{c\d+::([^:}]+)", f[frontfield(f)]["value"]) or ["?"])[0].strip()
        for s in set(re.findall(r'src="([^"]+)"', " ".join(v["value"] for v in f.values()))):
            img2t[s].add(tgt)

    key = os.environ.get("ANTHROPIC_API_KEY")
    OUT.mkdir(parents=True, exist_ok=True)
    rows, acted = [], 0
    for n in notes:
        f = n["fields"]; nid = n["noteId"]
        srcs = re.findall(r'src="([^"]+)"', " ".join(v["value"] for v in f.values()))
        if not srcs:
            continue
        fn = srcs[0]
        card_text = plain(f[frontfield(f)]["value"])
        extra = plain(f.get("Extra", {}).get("value", ""))
        reused = len(img2t[fn]) > 1
        if not key:
            rows.append((nid, fn, "NO_KEY", reused, "", card_text[:60])); continue
        try:
            img = base64.b64decode(anki("retrieveMediaFile", filename=fn))
            v = judge(img, fn, card_text, extra, key)
        except Exception as e:
            rows.append((nid, fn, "ERR", reused, str(e)[:50], card_text[:60])); continue
        verdict = v.get("verdict", "WEAK")
        if v.get("is_text_screenshot"):
            verdict = "MISMATCH"
        rows.append((nid, fn, verdict, reused, "%s | %s" % (v.get("image_shows", ""), v.get("why", "")), card_text[:60]))
        if a.apply:
            if verdict == "MISMATCH":
                strip_first_img(nid, n, fn)
                set_tags(nid, add=["img::substituir", FAIL], remove=[WEAK, OK]); acted += 1
            elif verdict == "WEAK":
                set_tags(nid, add=[WEAK], remove=[OK]); acted += 1
            else:
                set_tags(nid, add=["%s::%s" % (OK, dt.date.today())], remove=[WEAK, FAIL]); acted += 1

    ts = dt.datetime.now().strftime("%Y%m%d-%H%M")
    rep = OUT / ("relatorio-%s.md" % ts)
    counts = collections.Counter(r[2] for r in rows)
    with rep.open("w", encoding="utf-8") as fh:
        fh.write("# Gate imagem×card — %s\n\n%s\n\n" % (ts, dict(counts)))
        fh.write("| nota | veredito | reuso | imagem mostra / porquê | card |\n|---|---|---|---|---|\n")
        for nid, fn, verd, reused, why, txt in sorted(rows, key=lambda x: x[2]):
            fh.write("| %d | **%s** | %s | %s | %s |\n" % (nid, verd, "⚠" if reused else "", why, txt))
    print("Cards com imagem avaliados:", len(rows))
    print("Veredito:", dict(counts))
    print("Ações aplicadas:", acted if a.apply else "(dry-run — nada mutado)")
    print("Relatório:", rep)
    if a.apply:
        anki("sync"); print("Sync OK")
    if not key:
        print("\n[sem ANTHROPIC_API_KEY: rodou só L0/reuso. Defina a key p/ o juiz semântico.]")


if __name__ == "__main__":
    main()
