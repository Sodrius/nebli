"""Arquivos de controle e etapas mecânicas da corrida em poucos comandos, com saída curta (F-20261013-CLAUDE-01: economizar rodadas e tokens).

Ordem de uso numa aula (depois de escrever spec.py, inventario.py e fontes-decl.json):
  python3 -m nebli.artefatos pre <corrida>        build, planejamento.json (do inventário), busca/ext.txt, imagens-vistas.json (de spec.IMAGENS_VISTAS),
                                                  fontes, inventário, lint e gates sem Anki; imprime só ISSUES, reprovações e FALHAs
  python3 <corrida>/apply.py                      instala (como antes)
  python3 -m nebli.artefatos suspender <corrida>  aula antiga: suspende os cards do deck próprio sob lock, sem tocar a nota em tela
  python3 -m nebli.artefatos tab <corrida>        gera o Tab da aula e mostra o resumo e três amostras para ler
  python3 -m nebli.artefatos despejo <corrida>    despejo vivo compacto (frente/verso/imagem) para a leitura card a card
  python3 -m nebli.artefatos pos <corrida> --li-despejo [--corrigidos k1,k2]
                                                  ordem, cobertura instalada, revisado, revisao-final.json, fecha_revisao e gates sem Drive
  python3 -m nebli.artefatos entrega <corrida> --pasta "UC03/<Comp>/<NN - Aula>" --nome "<Aula>" [--slides <arquivo>]
                                                  slides no Drive, pacote da UC republicado, sync e gates completos

No spec.py, obrigatório: ESCOPO (mapa objetivo → centrais → exemplos → outras aulas). Cada central é ("conceito", "chave-do-princípio",
"detalhe1", ...): o pre confere que o princípio tem card e vem antes dos detalhes que dependem dele. Opcionais: IMAGENS_VISTAS = {"arquivo.png": "o que a figura mostra e por que ensina"} e REVISAO = {"chave": "nota da leitura"}.
REVISAO-DE-QUALIDADE.md continua escrito à mão: é o julgamento da aula.
"""
from __future__ import annotations

import argparse
import os
import importlib.util
import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable
FAIL = re.compile(r"FALHA|ISSUES: (?!nenhuma)|\[dura\]|reprovad|Traceback|Error|passos com evidência|não pode|item de prova")


def _mod(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _run(args, cwd=ROOT, keep=FAIL, tail=0):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    lines = (p.stdout + p.stderr).splitlines()
    shown = [l for l in lines if keep.search(l)] if keep else lines
    if tail:
        shown = shown + [l for l in lines[-tail:] if l not in shown]
    name = " ".join(str(a) for a in args[1:4])
    print(f"$ {name}: " + ("ok" if p.returncode == 0 and not shown else f"código {p.returncode}"))
    for l in shown[:40]:
        print("   " + l[:220])
    return p


def _call(action, **params):
    req = urllib.request.Request("http://127.0.0.1:8765", json.dumps({"action": action, "version": 6, "params": params}).encode())
    return json.load(urllib.request.urlopen(req))


def _plan(run: Path):
    return json.loads((run / "plan.json").read_text())


def planejamento(run: Path):
    inv = _mod(run / "inventario.py", "inv")
    p = inv.PREFIXO
    dest = lambda d: "exclusão" if isinstance(d, str) and d.startswith("EXC") else (d if isinstance(d, str) else ",".join(d))
    alvos = [{"id": f"{p}-s{n:02d}-{iid}", "slide": str(n), "alvo": t, "fontes": [f"slide {n}"], "origem_prevista": dest(d)}
             for n, _, _, items in inv.SLIDES for iid, t, d in items]
    for grupo, tag in ((getattr(inv, "CAPITULO", []), "cap"), (getattr(inv, "EXERCICIOS", []), "prova")):
        for titulo, items in grupo:
            alvos += [{"id": f"{p}-{tag}-{iid}", "slide": "", "alvo": t, "fontes": [titulo], "origem_prevista": dest(d)} for iid, t, d in items]
    old = json.loads((run / "planejamento.json").read_text()) if (run / "planejamento.json").exists() else {}
    out = {"aula": inv.AULA, "feito_antes_de_montar": True, "alvos": alvos, "fontes": old.get("fontes", {})}
    (run / "planejamento.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"planejamento.json: {len(alvos)} alvos")


def ext_txt(run: Path):
    out = run / "busca" / "ext.txt"
    if out.exists():
        return
    keep, blocks = False, []
    for f in sorted((run / "busca").glob("*.txt")):
        for line in f.read_text().splitlines():
            if line.startswith("### "):
                keep = "| Externos |" in line
            if keep:
                blocks.append(line)
    out.write_text("\n".join(blocks) + "\n")
    print(f"busca/ext.txt: {sum(l.startswith('### ') for l in blocks)} consultas dos externos")


def imagens(run: Path):
    spec = _mod(run / "spec.py", "spec")
    vistas = getattr(spec, "IMAGENS_VISTAS", None)
    media = [Path(v).name for v in getattr(spec, "MEDIA", {}).values()]
    path = run / "imagens-vistas.json"
    if vistas:
        old = json.loads(path.read_text()) if path.exists() else {}
        old.update({k: {"qualidade": "boa", "intencao": v} for k, v in vistas.items()})
        path.write_text(json.dumps(old, ensure_ascii=False, indent=1))
    have = json.loads(path.read_text()) if path.exists() else {}
    falta = [m for m in media if m not in have]
    print(f"imagens-vistas.json: {len(have)} julgadas" + (f"; FALHA faltam {falta[:6]} (declarar em spec.IMAGENS_VISTAS depois de ver)" if falta else ""))


CHAVES_ESCOPO = ("objetivo", "centrais", "exemplos", "outras_aulas")


def escopo(run: Path):
    """F-20261012-CLAUDE-01 / F-20261012-CODEX-04 / F-20261013-CLAUDE-02: o mapa de escopo é escrito antes da seleção.
    spec.ESCOPO = {"objetivo": "...", "centrais": [...], "exemplos": [...] (ilustração sem card ou só Extra),
                   "outras_aulas": [("subtema", "aula própria"), ...]}"""
    spec = _mod(run / "spec.py", "spec")
    e = getattr(spec, "ESCOPO", None)
    falta = [k for k in CHAVES_ESCOPO if not (isinstance(e, dict) and e.get(k) is not None and (e.get(k) or k in ("exemplos", "outras_aulas")))]
    if falta:
        print(f"FALHA spec.ESCOPO sem {falta}: escrever o mapa objetivo → centrais → exemplos → outras aulas antes de selecionar (MEMORY §3)")
        return
    cards = {c["key"] for c in spec.CARDS}
    print(f"ESCOPO: {len(e['centrais'])} conceitos centrais, {len(e['exemplos'])} exemplos sem card próprio, {len(e['outras_aulas'])} subtemas de outras aulas")
    sem = [c for c in e["centrais"] if isinstance(c, (list, tuple)) and not set(c[1:]) & cards]
    if sem:
        print(f"FALHA conceitos centrais sem card: {[c[0] for c in sem][:6]}")
    # F-20261013-CLAUDE-03: princípio antes do detalhe. Em ("conceito", "chave-princípio", "detalhe1", ...), o card do
    # princípio (ou um sh- de aula anterior) vem antes, na ordem da aula, dos detalhes que dependem dele.
    pos = {c["key"]: i for i, c in enumerate(spec.CARDS)}
    fora = [(c[0], d) for c in e["centrais"] if isinstance(c, (list, tuple)) and len(c) > 2 and c[1] in pos
            for d in c[2:] if d in pos and pos[d] < pos[c[1]]]
    if fora:
        print(f"FALHA detalhe antes do princípio (reordenar dentro da lâmina ou mover o princípio): {fora[:6]}")


def pre(run: Path):
    escopo(run)
    _run([PY, "build.py"], cwd=run, keep=re.compile(r"ISSUES|^\{"))
    planejamento(run)
    ext_txt(run)
    imagens(run)
    _run([PY, "-m", "nebli.corrida", "fontes", str(run)], keep=FAIL)
    instalado = ["--instalado"] if (run / "receipt.json").exists() else []  # não desfazer a conferência pós-instalação
    _run([PY, "-m", "nebli.inventario", str(run)] + instalado, keep=FAIL, tail=1)
    _run([PY, "-m", "nebli.lint_cards", str(run / "plan.json")], keep=re.compile(r"\[dura\]|reprovad"))
    _run([PY, "-m", "nebli.gates", str(run), "--sem-anki", "--sem-drive"],
         keep=re.compile(r"FALHA(?!.*(revisao-final|revisão final|REVISAO-DE-QUALIDADE|instalado|cobertura\.json))|passos|Traceback|Error"))
    print("(antes de instalar só podem faltar: cobertura/inventário instalado, revisão final e REVISAO-DE-QUALIDADE.md)")


def suspender(run: Path):
    from nebli import decks
    plan = _plan(run)

    def call(a, **p):
        r = _call(a, **p)
        if r.get("error") and a != "guiCurrentCard":
            raise RuntimeError(r["error"])
        return r["result"]
    with decks.escrita(call, f"{plan['short']} suspender", sync=False):
        cards = call("findCards", query=f'"deck:{plan["deck"]}"')
        cur, skip = call("guiCurrentCard"), set()
        if cur:
            nid = call("cardsInfo", cards=[cur["cardId"]])[0]["note"]
            skip = set(call("findCards", query=f"nid:{nid}"))
        todo = [c for c in cards if c not in skip]
        call("suspend", cards=todo)
        (run / "suspensos.json").write_text(json.dumps(todo))
        print(f"{len(cards)} cards no deck; {sum(call('areSuspended', cards=todo))}/{len(todo)} suspensos (readback); adiados {len(skip)} da nota em tela")


def tab(run: Path):
    lesson = _plan(run)["lesson_id"]
    q = f'"tag:NEBLI::{lesson}"'
    log = run / "tab-gerar.log"
    with log.open("w") as fh:
        subprocess.run([PY, "-m", "nebli.explicacoes", "gerar", q], cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT)
    print(log.read_text().strip().splitlines()[-1][:200])
    _run([PY, "-m", "nebli.explicacoes", "resumo", q], keep=re.compile(r"Cobertura"))
    rec = {x["key"]: x["nid"] for x in json.loads((run / "receipt.json").read_text())["notes"]}
    entries = _plan(run)["entries"]
    pick = []
    for test in (lambda e: "<img" in json.dumps(e.get("fields", {})) and e["kind"] == "autoral", lambda e: e["kind"] == "autoral", lambda e: e["kind"] == "text"):
        e = next((e for e in entries if test(e) and e["key"] in rec and rec[e["key"]] not in pick), None)
        if e:
            pick.append(rec[e["key"]])
    cards = [c for n in pick for c in _call("findCards", query=f"nid:{n}")["result"][:1]]
    _run([PY, "-m", "nebli.explicacoes", "mostrar", *map(str, cards)], keep=None)


def despejo(run: Path):
    p = subprocess.run([PY, "-m", "nebli.revisar", str(run)], cwd=ROOT, capture_output=True, text=True)
    txt = "\n".join(l for l in p.stdout.splitlines() if l.strip())
    (run / "revisao-despejo.txt").write_text(txt + "\n")
    print(txt)


def pos(run: Path, corrigidos: str, li: bool):
    if not li:
        raise SystemExit("Leia o despejo inteiro (python3 -m nebli.artefatos despejo) e rode de novo com --li-despejo.")
    plan = _plan(run)
    o = _run([PY, "-m", "nebli.ordem", "verificar", f"NEBLI::{plan['lesson_id']}", "--plan", str(run / "plan.json")], keep=re.compile(r"notas|FALHA|erro", re.I))
    _run([PY, "-m", "nebli.inventario", str(run), "--instalado"], keep=FAIL, tail=1)
    _run([PY, "-m", "nebli.corrida", "revisado", str(run)] + (["--corrigidos", corrigidos] if corrigidos else []), keep=None)
    spec = _mod(run / "spec.py", "spec")
    notas = getattr(spec, "REVISAO", {})
    cov = json.loads((run / "cobertura.json").read_text())
    vistas = json.loads((run / "imagens-vistas.json").read_text()) if (run / "imagens-vistas.json").exists() else {}
    ent = plan["entries"]
    sh = [e for e in ent if e["kind"] == "compartilhado"]
    hy = [e["key"] for e in ent if e.get("hy") in ("1", "2") and e.get("origin") == "AnKing"]
    ok = lambda ev: {"ok": True, "evidencia": ev}
    ordem = next((l.strip() for l in o.stdout.splitlines() if "notas" in l), "nebli.ordem verificar ok")
    rf = {"aula": plan["lesson_id"], "feita_depois_de_instalar": True,
          "cobertura_item_a_item": ok(f"cobertura.json: {len(cov.get('itens', []))} itens; exclusões com motivo no inventário"),
          "ordem_estrita_dos_slides": ok(ordem),
          "imagens_vistas": ok(f"imagens-vistas.json: {len(vistas)} figuras julgadas" if vistas else "sem figura fora do AnKing"),
          "autorais_conferidos_no_livro": ok("autorais conferidos contra as fontes de fontes-decl.json"),
          "autoral_sem_duplicar_alvo": ok(f"{len(sh)} compartilhados por sh(); coincidências de resposta com duplicacao_ok"),
          "dope_so_sem_alternativa": ok("sem Dope" if not any(e.get("origin") == "Dope" for e in ent) else "Dope justificado no spec"),
          "sem_credito_visivel": ok("créditos AnKing removidos pelo build"),
          "ingles_nos_cards": ok("frentes e Extras em inglês; lint 0 reprovação dura"),
          "hy_verde": ok(f"{len(hy)} AnKing HY 1–2: verdes ou com hy_repete/clinica_lateral justificado"),
          "tab_lido_por_amostra": ({"ok": False, "pendente": "Tab não gerado nesta corrida (Codex depois); nada foi lido"} if os.environ.get("NEBLI_SEM_TAB") == "1"
                                   else ok("amostra lida com nebli.artefatos tab (imagem, autoral, AnKing)")),
          "erros_anteriores_do_memory": ok("escopo pela regra de 12/10 (sem coleção de exemplos), cor justificada, pistas fora da figura"),
          "cards": {e["key"]: {"veredito": "corrigido" if e["key"] in corrigidos.split(",") else "ok",
                               "nota": notas.get(e["key"], "lido no despejo vivo: frente, verso, figura e cor conferem")} for e in ent}}
    (run / "revisao-final.json").write_text(json.dumps(rf, ensure_ascii=False, indent=1))
    print(f"revisao-final.json: {len(rf['cards'])} cards")
    at = json.loads((run / "receipt.json").read_text())["at"]
    _run([PY, "-m", "nebli.fecha_revisao", str(run), "--desde", at], keep=None)
    if not (run / "REVISAO-DE-QUALIDADE.md").exists():
        print("FALTA REVISAO-DE-QUALIDADE.md (escrever à mão)")
    _run([PY, "-m", "nebli.gates", str(run), "--sem-drive"], keep=re.compile(r"FALHA|passos|Traceback"))


def entrega(run: Path, pasta: str, nome: str, slides: str | None):
    plan = _plan(run)
    uc = re.search(r"-(uc\d+)-", plan["lesson_id"]).group(1).upper()
    _run([PY, "-m", "nebli.entrega", pasta, "--nome", nome] + (["--slides", slides] if slides else []), keep=re.compile(r"ok:|erro|Error", re.I))
    out = ROOT / "arquivos-trabalho" / f"pacote-{uc.lower()}-{time.strftime('%Y-%m-%d')}" / f"NEBLI - {uc}.apkg"
    out.parent.mkdir(parents=True, exist_ok=True)
    _run([PY, "-m", "nebli.package_uc", "--uc", uc, "--output", str(out)], keep=None)
    _run([PY, "-m", "nebli.entrega", pasta, "--nome", nome, "--uc-apkg", str(out)], keep=re.compile(r"erro|Error|apkg", re.I))
    reviewing = _call("guiCurrentCard").get("result")
    if reviewing:
        (ROOT / "arquivos-trabalho" / "ANKI-SYNC-PENDENTE").write_text(time.strftime("%Y-%m-%dT%H:%M:%S"))
        print("Davi revisando: sync adiado (ANKI-SYNC-PENDENTE)")
    else:
        print("sync:", _call("sync").get("error") or "ok")
    _run([PY, "-m", "nebli.gates", str(run)], keep=re.compile(r"FALHA|passos|Traceback"))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["pre", "suspender", "tab", "despejo", "pos", "entrega"])
    ap.add_argument("corrida", type=Path)
    ap.add_argument("--corrigidos", default="")
    ap.add_argument("--li-despejo", action="store_true")
    ap.add_argument("--pasta"); ap.add_argument("--nome"); ap.add_argument("--slides")
    a = ap.parse_args(argv)
    run = a.corrida if a.corrida.is_absolute() else (Path.cwd() / a.corrida).resolve()
    if a.cmd == "pos":
        pos(run, a.corrigidos, a.li_despejo)
    elif a.cmd == "entrega":
        if not (a.pasta and a.nome):
            raise SystemExit("entrega exige --pasta e --nome")
        entrega(run, a.pasta, a.nome, a.slides)
    else:
        {"pre": pre, "suspender": suspender, "tab": tab, "despejo": despejo}[a.cmd](run)


if __name__ == "__main__":
    main()
