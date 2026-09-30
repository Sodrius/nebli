"""Explicações do Tab: uma por card, fora da coleção, geradas pelo Claude da assinatura.

Uso (Anki aberto com AnkiConnect):
    python -m nebli.explicacoes gerar 'deck:"NEBLI::UC08::P1::Fisiologia::Motilidade e absorção intestinal I"'
    python -m nebli.explicacoes gerar 'deck:*Microbiologia* rated:1:1' --limite 20
    python -m nebli.explicacoes gerar '<busca>' --refazer      # refaz mesmo as que já existem
    python -m nebli.explicacoes gerar '<busca>' --simular      # mostra o que seria enviado, sem gerar
    python -m nebli.explicacoes mostrar <card_id> [<card_id> ...]
    python -m nebli.explicacoes resumo

Cada card (não a nota) tem a sua: irmãos de cloze recebem explicações diferentes.
A base fica em addons21/nebli_atalhos/user_files/explicacoes.sqlite, onde o add-on
nebli_atalhos a lê quando Davi aperta Tab no verso. Nada é escrito na coleção.

O estilo e as regras ficam em config/explicacao-tab.md (inclusive os exemplos
aprovados). Mudar esse arquivo muda a versão do estilo; `resumo` mostra quantas
explicações estão em estilo antigo, e `gerar --refazer` as atualiza.

`hash` identifica o conteúdo do card (campos da nota + ordem do card). Se o card
for editado depois, o add-on mostra a explicação com aviso de que o card mudou.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

from nebli.decks import Anki

ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / "config" / "explicacao-tab.md"
BATCH = 10
MODEL = "sonnet"
NOISE = ("Reveal Next", "Toggle All")


def anki_base():
    if sys.platform == "win32":
        return Path(os.environ.get("APPDATA", "")) / "Anki2"
    return Path.home() / ("Library/Application Support/Anki2" if sys.platform == "darwin"
                          else ".local/share/Anki2")


def store_path():
    return anki_base() / "addons21" / "nebli_atalhos" / "user_files" / "explicacoes.sqlite"


def open_store(path=None):
    path = Path(path or store_path())
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.execute("pragma journal_mode=wal")
    db.execute("""create table if not exists explicacoes (
        card_id integer primary key, note_id integer, hash text, status text,
        texto text, motivo text, estilo text, modelo text, gerado_em text)""")
    return db


def card_hash(field_values, ord_):
    return hashlib.sha1(("\x1f".join(field_values) + f"\x1e{ord_}").encode("utf-8")).hexdigest()


def style_version(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def plain(value):
    value = re.sub(r"<(style|script)\b.*?</\1>", "", value, flags=re.S | re.I)
    value = re.sub(r"<br\s*/?>|</div>|</p>|</li>", "\n", value, flags=re.I)
    value = html.unescape(re.sub(r"<[^>]+>", "", value))
    for noise in NOISE:
        value = value.replace(noise, "")
    return re.sub(r"\n\s*\n+", "\n", value).strip()


CLOZE = r"\{\{c(\d+)::(.*?)(?:::(.*?))?\}\}"


def hidden_target(fields, ord_):
    """Texto que ESTE card esconde, quando é cloze (c<ord+1>)."""
    text = " ".join(f["value"] for f in fields.values())
    found = [m.group(2) for m in re.finditer(CLOZE, text, flags=re.S) if int(m.group(1)) == ord_ + 1]
    return "; ".join(plain(f) for f in found) or None


def card_text(card):
    """Frente e verso deste card a partir dos campos, sem tags, botões nem pseudo-campos do AnKing."""
    fields = card["fields"]
    if "Text" in fields:
        raw = fields["Text"]["value"]
        mine = lambda m: int(m.group(1)) == card["ord"] + 1
        front = re.sub(CLOZE, lambda m: "[...]" if mine(m) else m.group(2), raw, flags=re.S)
        back = re.sub(CLOZE, lambda m: m.group(2), raw, flags=re.S)
        return plain(front), plain(back)
    def clean(value):
        lines, seen = [], set()
        for line in plain(value).splitlines():
            line = line.strip()
            if (not line or line.startswith("#") or "PSEUDO-FIELD" in line or line.isdigit()
                    or line in seen or line in ("×", "↪")):
                continue
            seen.add(line)
            lines.append(line)
        return "\n".join(lines)
    return clean(card["question"]), clean(card["answer"])


def studied_related(call, card, target, limit=4):
    """Cards que Davi já estudou (não novos) com o termo escondido, de outras notas."""
    if not target:
        return []
    term = re.sub(r'["*_:\\()]', " ", target.split(";")[0]).strip()
    if len(term) < 4:
        return []
    ids = call("findCards", query=f'deck:NEBLI* -is:new "{term[:60]}" -nid:{card["note"]}')[:limit]
    return [card_text(c)[1][:220] for c in call("cardsInfo", cards=ids)] if ids else []


def collect(call, query, limit=None):
    cards = []
    ids = call("findCards", query=query)
    for start in range(0, len(ids), 200):
        cards.extend(call("cardsInfo", cards=ids[start:start + 200]))
    return cards[:limit] if limit else cards


def item(call, card):
    fields = card["fields"]
    ordered = [f["value"] for f in sorted(fields.values(), key=lambda f: f["order"])]
    target = hidden_target(fields, card["ord"])
    front, back = card_text(card)
    extra = next((plain(fields[k]["value"]) for k in ("Extra", "Remarks", "Extra 1") if k in fields), "")
    return {
        "id": str(card["cardId"]),
        "aula": re.sub(r" \(\d+\)", "", card["deckName"]).split("::")[-1],
        "frente": front[:1200],
        "verso": back[:1500],
        "alvo_oculto": target,
        "extra": extra[:800],
        "ja_estudados": studied_related(call, card, target),
    }, card_hash(ordered, card["ord"]), card["note"]


def claude(system, payload):
    exe = shutil.which("claude") or str(Path.home() / ".local/bin/claude")
    cmd = [exe, "-p", "Cards:\n" + json.dumps(payload, ensure_ascii=False, indent=1),
           "--system-prompt", system, "--tools", "", "--strict-mcp-config", "--setting-sources", "",
           "--no-session-persistence", "--output-format", "json", "--model", MODEL]
    done = subprocess.run(cmd, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=300)
    envelope = json.loads(done.stdout)
    if envelope.get("is_error"):
        raise RuntimeError(envelope.get("result") or done.stderr[:300])
    text = envelope["result"].strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text)
    return json.loads(text), envelope.get("total_cost_usd")


def generate(call, query, limit=None, redo=False, simulate=False, db=None):
    db = db or open_store()
    system = STYLE.read_text(encoding="utf-8")
    version = style_version(system)
    have = {cid: h for cid, h in db.execute("select card_id, hash from explicacoes")}
    todo = []
    for card in collect(call, query, limit):
        if not redo and card["cardId"] in have:
            continue
        todo.append(item(call, card))
    print(f"{len(todo)} cards a explicar (estilo {version}).")
    if simulate:
        for payload, _, _ in todo[:3]:
            print(json.dumps(payload, ensure_ascii=False, indent=1))
        return
    cost, stamp = 0.0, time.strftime("%Y-%m-%d %H:%M:%S")
    for start in range(0, len(todo), BATCH):
        chunk = todo[start:start + BATCH]
        result, spent = claude(system, [payload for payload, _, _ in chunk])
        cost += spent or 0
        for payload, digest, note_id in chunk:
            answer = result.get(payload["id"]) or {"status": "revisar", "motivo": "sem resposta do modelo"}
            db.execute("insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)",
                       (int(payload["id"]), note_id, digest, answer.get("status", "ok"),
                        answer.get("texto"), answer.get("motivo"), version, MODEL, stamp))
        db.commit()
        print(f"  {min(start + BATCH, len(todo))}/{len(todo)}")
    print(f"Pronto. Cota equivalente (não cobrada na assinatura): US$ {cost:.3f}.")


def show(ids, db=None):
    db = db or open_store()
    for cid in ids:
        row = db.execute("select status, texto, motivo, estilo from explicacoes where card_id=?",
                         (int(cid),)).fetchone()
        print(f"--- {cid}: " + ("sem explicação" if not row else f"{row[0]} (estilo {row[3]})"))
        if row:
            print(row[1] or row[2])


def summary(db=None):
    db = db or open_store()
    version = style_version(STYLE.read_text(encoding="utf-8"))
    total = db.execute("select count(*) from explicacoes").fetchone()[0]
    by = dict(db.execute("select status, count(*) from explicacoes group by status").fetchall())
    old = db.execute("select count(*) from explicacoes where estilo != ?", (version,)).fetchone()[0]
    print(f"{total} explicações ({by}); {old} em estilo antigo; base {store_path()}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    gen = sub.add_parser("gerar")
    gen.add_argument("busca")
    gen.add_argument("--limite", type=int)
    gen.add_argument("--refazer", action="store_true")
    gen.add_argument("--simular", action="store_true")
    sh = sub.add_parser("mostrar")
    sh.add_argument("ids", nargs="+")
    sub.add_parser("resumo")
    args = parser.parse_args()
    if args.cmd == "gerar":
        generate(Anki(), args.busca, args.limite, args.refazer, args.simular)
    elif args.cmd == "mostrar":
        show(args.ids)
    else:
        summary()


if __name__ == "__main__":
    main()
