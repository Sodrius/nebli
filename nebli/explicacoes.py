"""Explicações do Tab: uma por card, fora da coleção, geradas pelo Claude da assinatura.

Uso (Anki aberto com AnkiConnect):
    python -m nebli.explicacoes gerar '"tag:NEBLI::2026-uc08-fisiologia-08-motilidade-i"'   # aula inteira
    python -m nebli.explicacoes gerar 'deck:*Microbiologia* rated:1:1' --limite 20
    python -m nebli.explicacoes gerar '<busca>' --refazer      # refaz mesmo as que já existem
    python -m nebli.explicacoes gerar '<busca>' --simular      # mostra o que seria enviado, sem gerar
    python -m nebli.explicacoes mostrar <card_id> [<card_id> ...]
    python -m nebli.explicacoes resumo                        # totais da base
    python -m nebli.explicacoes resumo '"tag:NEBLI::<aula>"'  # cobertura exata; sai 1 se faltar

Não usar deck:"NEBLI::UCxx::..." exato: o add-on nebli_decks põe o total no nome dos decks,
e a busca volta vazia. Use a tag da aula (inclui os compartilhados) ou deck:*trecho*.
    python -m nebli.explicacoes instalar                       # só o add-on do Tab

Guia completo: GUIA-EXPLICACOES-TAB.md na raiz do repositório.

Cada card (não a nota) tem a sua: irmãos de cloze recebem explicações diferentes.
A base fica em addons21/nebli_explicacoes/user_files/explicacoes.sqlite, onde o
add-on nebli_explicacoes a lê quando se aperta Tab no verso. Nada é escrito na coleção.

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


ADDON = "nebli_explicacoes"
OLD_STORE = ("nebli_atalhos", "user_files", "explicacoes.sqlite")  # antes de 30/09, 11h


def store_path():
    return anki_base() / "addons21" / ADDON / "user_files" / "explicacoes.sqlite"


def install():
    """Copia só o add-on do Tab (não mexe em outras teclas) e leva a base antiga, se houver."""
    target = anki_base() / "addons21" / ADDON
    (target / "user_files").mkdir(parents=True, exist_ok=True)
    source = ROOT / "anki-addon" / ADDON
    shutil.copy2(source / "__init__.py", target / "__init__.py")
    if not (target / "meta.json").exists():
        shutil.copy2(source / "meta.json", target / "meta.json")
    old = anki_base() / "addons21" / Path(*OLD_STORE)
    if old.exists() and not store_path().exists():
        for suffix in ("", "-wal", "-shm"):
            if Path(f"{old}{suffix}").exists():
                shutil.move(f"{old}{suffix}", f"{store_path()}{suffix}")
        print(f"Explicações já geradas movidas para {store_path()}.")
    print(f"Add-on do Tab em {target}. Reiniciar o Anki para carregar.")


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
    ids = call("findCards", query=f'prop:reps>0 "{term[:60]}" -nid:{card["note"]}')[:limit]
    return [card_text(c)[1][:220] for c in call("cardsInfo", cards=ids)] if ids else []


def collect(call, query, limit=None):
    cards = []
    ids = call("findCards", query=query)
    if not ids:
        # Armadilha real (30/09): o add-on nebli_decks põe o total no nome ("UC03 (992)"), então
        # deck:"NEBLI::UC03::P2::..." não acha nada. Buscar pela tag da aula ou por deck:*trecho*.
        raise SystemExit(f"Nenhum card para a busca {query!r}. Use a tag da aula "
                         "('\"tag:NEBLI::<aula>\"') ou deck:*trecho*; nomes de deck vivos levam o total.")
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
    if os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("ANTHROPIC_API_KEY está definida: geração interrompida para não usar API paga.")
    exe = shutil.which("claude") or str(Path.home() / ".local/bin/claude")
    cmd = [exe, "-p", "Cards:\n" + json.dumps(payload, ensure_ascii=False, indent=1),
           "--system-prompt", system, "--tools", "", "--strict-mcp-config", "--setting-sources", "",
           "--no-session-persistence", "--output-format", "json", "--model", MODEL]
    done = subprocess.run(cmd, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=300)
    if not done.stdout.strip():
        raise RuntimeError(f"Claude não devolveu JSON (exit {done.returncode}): {done.stderr[:300]}")
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
    have = {cid: (h, style, status) for cid, h, style, status in
            db.execute("select card_id, hash, estilo, status from explicacoes")}
    todo = []
    cards = collect(call, query, limit)
    print(f"Conferindo {len(cards)} cards e explicações já salvas…", flush=True)
    for index, card in enumerate(cards, 1):
        ordered = [f["value"] for f in sorted(card["fields"].values(), key=lambda f: f["order"])]
        saved = have.get(card["cardId"])
        if not redo and saved and saved[:2] == (card_hash(ordered, card["ord"]), version):
            continue
        todo.append(item(call, card))
        if len(todo) % 50 == 0:
            print(f"  contexto preparado: {index}/{len(cards)}", flush=True)
    print(f"{len(todo)} cards a explicar (estilo {version}).", flush=True)
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
        print(f"  {min(start + BATCH, len(todo))}/{len(todo)}", flush=True)
    print(f"Pronto. Cota equivalente (não cobrada na assinatura): US$ {cost:.3f}.", flush=True)


def show(ids, db=None):
    db = db or open_store()
    for cid in ids:
        row = db.execute("select status, texto, motivo, estilo from explicacoes where card_id=?",
                         (int(cid),)).fetchone()
        print(f"--- {cid}: " + ("sem explicação" if not row else f"{row[0]} (estilo {row[3]})"))
        if row:
            print(row[1] or row[2])


def summary(db=None, call=None, query=None):
    """Sem busca: totais da base. Com busca: cobertura exata daqueles cards (sai 1 se faltar algo)."""
    db = db or open_store()
    version = style_version(STYLE.read_text(encoding="utf-8"))
    total = db.execute("select count(*) from explicacoes").fetchone()[0]
    by = dict(db.execute("select status, count(*) from explicacoes group by status").fetchall())
    old = db.execute("select count(*) from explicacoes where estilo != ?", (version,)).fetchone()[0]
    print(f"{total} explicações ({by}); {old} em estilo antigo; base {store_path()}")
    if not query:
        return 0
    saved = {cid: (h, style, status) for cid, h, style, status in
             db.execute("select card_id, hash, estilo, status from explicacoes")}
    count = {"atual": 0, "revisar": 0, "desatualizada": 0, "faltando": 0}
    for card in collect(call, query):
        ordered = [f["value"] for f in sorted(card["fields"].values(), key=lambda f: f["order"])]
        row = saved.get(card["cardId"])
        if not row:
            count["faltando"] += 1
        elif row[:2] != (card_hash(ordered, card["ord"]), version):
            count["desatualizada"] += 1
        else:
            count["revisar" if row[2] != "ok" else "atual"] += 1
    print(f"Cobertura de {query}: {count}")
    return 1 if count["faltando"] or count["desatualizada"] else 0


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
    rs = sub.add_parser("resumo", help="totais da base; com busca, cobertura exata daqueles cards")
    rs.add_argument("busca", nargs="?")
    sub.add_parser("instalar", help="copia só o add-on do Tab para o Anki deste computador")
    args = parser.parse_args()
    if args.cmd == "instalar":
        install()
    elif args.cmd == "gerar":
        generate(Anki(), args.busca, args.limite, args.refazer, args.simular)
    elif args.cmd == "mostrar":
        show(args.ids)
    else:
        sys.exit(summary(call=Anki() if args.busca else None, query=args.busca))


if __name__ == "__main__":
    main()
