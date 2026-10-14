"""Explicações do Tab: uma por card, fora da coleção, geradas pelo Claude da assinatura.

Uso (Anki aberto com AnkiConnect):
    python -m nebli.explicacoes gerar '"tag:NEBLI::2026-uc08-fisiologia-08-motilidade-i"'   # aula inteira
    python -m nebli.explicacoes gerar 'deck:*Microbiologia* rated:1:1' --limite 20
    python -m nebli.explicacoes gerar '<busca>' --refazer      # refaz mesmo as que já existem
    python -m nebli.explicacoes gerar '<busca>' --backend codex  # alternativa pela assinatura quando Claude atinge o limite
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

O estilo e as regras ficam em config/explicacao-tab.md. Mudar esse arquivo muda a
versão do estilo; `resumo` mostra quantas explicações estão em estilo antigo. Elas
continuam visíveis no Tab e são atualizadas aula a aula quando `gerar` recebe a
tag da aula. Não iniciar uma regeneração geral só pela mudança de estilo.

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
import tempfile
import time
from pathlib import Path

from nebli.decks import Anki
from nebli.rotulos import canonical

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
    if not target and "Answer Mask" in fields:
        # Oclusão de imagem: o rótulo só existe nos pixels. As cópias NEBLI trazem o nome em negrito no início de Remarks.
        named = re.match(r"\s*<b>(.*?)</b>", fields.get("Remarks", {}).get("value", ""), flags=re.S)
        target = plain(named.group(1)) if named else None
    if not target and f"{card['ord'] + 1}a" in fields:
        # Prancha numerada (modelo Anatomy): o card N cobra o rótulo do campo "Na".
        target = plain(fields[f"{card['ord'] + 1}a"]["value"]) or None
    front, back = card_text(card)
    if target and "Answer Mask" in fields:
        front, back = ("Image occlusion on a figure from the lecture (cadaver photo, histology slide or atlas plate): identify the marked "
                       "structure. The figure is never available as text and that is expected: do NOT mark this card 'revisar' for lack "
                       "of the image. Explain the hidden target itself: what it is, where it lies, how to recognize it and what it does."), target
    if target and front.strip() in ("[...]", ""):
        front = "Identify the structure shown on the anatomy figure (the image is not available as text; explain the hidden target itself)."
    extra = next((plain(fields[k]["value"]) for k in ("Extra", "Remarks", "Extra 1") if k in fields), "")
    return {
        "id": str(card["cardId"]),
        "aula": canonical(card["deckName"]).split("::")[-1],
        "parte_da_aula": next((t.split("::")[-1] for t in ((call("notesInfo", notes=[card["note"]]) or [{}])[0].get("tags", []) if call else []) if t.startswith("NEBLI::objetivo::")), ""),
        "frente": front[:1200],
        "verso": back[:1500],
        "alvo_oculto": target,
        "extra": extra[:800],
        "ja_estudados": studied_related(call, card, target) if call else [],
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


def codex_cli(system, payload):
    """Alternativa pela assinatura do Codex quando a assinatura do Claude está indisponível."""
    if os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY está definida: geração interrompida para não usar API paga.")
    exe = shutil.which("codex")
    if not exe:
        raise RuntimeError("Codex CLI não encontrado.")
    with tempfile.TemporaryDirectory(prefix="nebli-tab-") as tmp:
        output = Path(tmp) / "resposta.json"
        prompt = system + "\n\nCards:\n" + json.dumps(payload, ensure_ascii=False, indent=1)
        cmd = [exe, "exec", "--ephemeral", "--sandbox", "read-only",
               "--skip-git-repo-check", "--output-last-message", str(output), "-"]
        done = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                              cwd=tmp, timeout=300)
        if done.returncode or not output.is_file():
            raise RuntimeError(f"Codex CLI não devolveu JSON (exit {done.returncode}): {done.stderr[-500:]}")
        answer = output.read_text(encoding="utf-8").strip()
        answer = re.sub(r"^```(?:json)?\s*|\s*```$", "", answer)
        return json.loads(answer), 0


EMPTY_LINK = re.compile(r"(?im)^\s*Liga com:\s*(nada|nenhum|nenhuma|sem|n[ãa]o h[áa])\b[^\n]*\n?")
TAB_LABELS = ("Básico", "Explicação", "Na aula", "Não confundir")
TAB_LABEL_RE = re.compile(r"(?m)^(Básico|Explicação|Na aula|Não confundir):[ \t]*")
ANY_LABEL_RE = re.compile(r"(?m)^([^:\n]{2,35}):[ \t]*")


NUMERADA = re.compile(r"(?m)(?:(?:^|[\s:])[1-9]\)\s|(?:^\s*|:\s*)[1-9]\.\s)")
META = re.compile(r"(?i)\b(este card|neste card|o card (quer|pede|cobra)|a pergunta quer|o extra)\b")


OLD_LABEL_RE = re.compile(r"(?m)^\s*(Básico|Explicação|Na aula|Não confundir|Base|Por quê|Mais a fundo|Liga com):")


def problema_estilo(text):
    """F-20261013-CLAUDE-03: texto corrido, do princípio geral ao card, em 2–4 parágrafos, sem rótulos, listas ou passos."""
    if not text or not text.strip():
        return "texto vazio"
    if OLD_LABEL_RE.search(text):
        return "rótulos de bloco (estilo antigo); escrever texto corrido"
    paras = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    if len(paras) < 2:
        return "um parágrafo só; descer do princípio ao card em 2–4 parágrafos"
    if len(paras) > 5:
        return "parágrafos demais"
    if len(NUMERADA.findall(text)) >= 2 or re.search(r"(?m)^\s*[-•*]\s", text):
        return "lista ou passos numerados"
    if META.search(text):
        return "metacomentário sobre o card"
    return None


def drop_empty_link(text):
    """O estilo manda omitir "Liga com" quando nada estudado serve; o modelo às vezes escreve "Liga com: nada da lista" (03/10)."""
    return EMPTY_LINK.sub("", text).strip() if text else text


def generate(call, query, limit=None, redo=False, simulate=False, db=None, backend="auto"):
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
        if not redo and saved and saved[:2] == (card_hash(ordered, card["ord"]), version) and not str(saved[2]).startswith("revisar"):
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
    used = set()
    for start in range(0, len(todo), BATCH):
        chunk = todo[start:start + BATCH]
        if backend == "auto":
            try:
                result, spent = claude(system, [payload for payload, _, _ in chunk])
                producer = "claude"
                used.add("claude")
            except RuntimeError as error:
                print(f"  Claude indisponível ({error}); tentando Codex CLI.", flush=True)
                result, spent = codex_cli(system, [payload for payload, _, _ in chunk])
                producer = "codex"
                used.add("codex")
        else:
            result, spent = (codex_cli if backend == "codex" else claude)(system, [payload for payload, _, _ in chunk])
            producer = backend
            used.add(backend)
        cost += spent or 0
        for payload, digest, note_id in chunk:
            answer = result.get(payload["id"]) or {"status": "revisar", "motivo": "sem resposta do modelo"}
            answer["texto"] = drop_empty_link(answer.get("texto"))
            falha = problema_estilo(answer["texto"]) if answer.get("status", "ok") == "ok" else None
            if falha:  # não grava texto fora do estilo como atual; fica pendente para nova geração
                print(f"  estilo recusado ({falha}) no card {payload['id']}: {answer['texto'][:300]!r}", flush=True)
                answer = {"status": "revisar", "motivo": f"estilo: {falha}", "texto": None}
            db.execute("insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)",
                       (int(payload["id"]), note_id, digest, answer.get("status", "ok"),
                        answer.get("texto"), answer.get("motivo"), version,
                        "codex-cli" if producer == "codex" else MODEL, stamp))
        db.commit()
        print(f"  {min(start + BATCH, len(todo))}/{len(todo)}", flush=True)
    if used == {"claude"}:
        print(f"Pronto. Cota equivalente (não cobrada na assinatura): US$ {cost:.3f}.", flush=True)
    elif used:
        print("Pronto. Gerado pela assinatura do Codex CLI.", flush=True)


def show(ids, db=None):
    db = db or open_store()
    for cid in ids:
        row = db.execute("select status, texto, motivo, estilo from explicacoes where card_id=?",
                         (int(cid),)).fetchone()
        print(f"--- {cid}: " + ("sem explicação" if not row else f"{row[0]} (estilo {row[3]})"))
        if row:
            print(row[1] or row[2])


def cobertura(query, call=None, db=None):
    """Cobertura e estrutura do formato atual; não certifica a qualidade didática."""
    if db is None:
        path = store_path()
        if not Path(path).is_file():
            cards = collect(call or Anki(), query)
            return {"atual": 0, "revisar": 0, "desatualizada": 0, "faltando": len(cards),
                    "formato_incompleto": 0}
        with sqlite3.connect(Path(path).resolve().as_uri() + "?mode=ro", uri=True) as connection:
            return cobertura(query, call=call, db=connection)
    version = style_version(STYLE.read_text(encoding="utf-8"))
    saved = {cid: (h, style, status, text) for cid, h, style, status, text in
             db.execute("select card_id, hash, estilo, status, texto from explicacoes")}
    count = {"atual": 0, "revisar": 0, "desatualizada": 0, "faltando": 0,
             "formato_incompleto": 0}
    words = []
    for card in collect(call or Anki(), query):
        ordered = [f["value"] for f in sorted(card["fields"].values(), key=lambda f: f["order"])]
        row = saved.get(card["cardId"])
        if not row:
            count["faltando"] += 1
        elif row[:2] != (card_hash(ordered, card["ord"]), version):
            count["desatualizada"] += 1
        elif row[2] != "ok":
            count["revisar"] += 1
        elif not (row[3] or "").strip():
            count["faltando"] += 1
        elif problema_estilo(row[3]):
            count["formato_incompleto"] += 1
        else:
            count["atual"] += 1
            words.append(len(row[3].split()))
    # Mediana descritiva, sem limite editorial de palavras.
    count["palavras_mediana"] = sorted(words)[len(words) // 2] if words else 0
    return count


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
    count = cobertura(query, call=call, db=db)
    print(f"Cobertura de {query}: {count}")
    return 1 if not count["atual"] or any(count[key] for key in
            ("faltando", "desatualizada", "revisar", "formato_incompleto")) else 0


def bad_tabs(log_path=None, db=None):
    """Lista reprovações explícitas ainda ligadas à versão atual da explicação."""
    path = Path(log_path or store_path().parent / "tab-log.jsonl")
    if not path.is_file():
        print("Nenhum Tab marcado como ruim.")
        return []
    marked = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("evento") == "tab_ruim" and event.get("card") is not None:
            marked[int(event["card"])] = event
        elif event.get("evento") == "tab_ruim_desfeito" and event.get("card") is not None:
            cid = int(event["card"])
            if marked.get(cid, {}).get("explicacao") == event.get("explicacao"):
                marked.pop(cid, None)
    if not marked:
        print("Nenhum Tab marcado como ruim.")
        return []
    db = db or open_store()
    pending = []
    for cid, event in marked.items():
        row = db.execute("select texto from explicacoes where card_id=?", (cid,)).fetchone()
        current = hashlib.sha256(((row or [""])[0] or "").encode("utf-8")).hexdigest()[:16]
        if current == event.get("explicacao") or not row:
            pending.append(event)
    for event in sorted(pending, key=lambda x: x.get("em", ""), reverse=True):
        print(f"{event.get('em', '?')} card {event['card']} nota {event.get('nota', '?')} — Tab ruim pendente")
    print(f"{len(pending)} Tab(s) ruim(ns) pendente(s).")
    return pending


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    gen = sub.add_parser("gerar")
    gen.add_argument("busca")
    gen.add_argument("--limite", type=int)
    gen.add_argument("--refazer", action="store_true")
    gen.add_argument("--simular", action="store_true")
    gen.add_argument("--backend", choices=("auto", "claude", "codex"), default="auto")
    sh = sub.add_parser("mostrar")
    sh.add_argument("ids", nargs="+")
    rs = sub.add_parser("resumo", help="totais da base; com busca, cobertura exata daqueles cards")
    rs.add_argument("busca", nargs="?")
    sub.add_parser("ruins", help="lista Tabs marcados como ruins ainda não reescritos")
    sub.add_parser("instalar", help="copia só o add-on do Tab para o Anki deste computador")
    args = parser.parse_args()
    if args.cmd == "instalar":
        install()
    elif args.cmd == "gerar":
        generate(Anki(), args.busca, args.limite, args.refazer, args.simular, backend=args.backend)
    elif args.cmd == "mostrar":
        show(args.ids)
    elif args.cmd == "ruins":
        bad_tabs()
    else:
        sys.exit(summary(call=Anki() if args.busca else None, query=args.busca))


if __name__ == "__main__":
    main()
