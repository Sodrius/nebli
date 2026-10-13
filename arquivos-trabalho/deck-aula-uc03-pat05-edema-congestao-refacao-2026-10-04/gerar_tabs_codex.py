"""Gera Tabs pelo Codex autenticado em ChatGPT, sem chave de API.

Uso: python3 gerar_tabs_codex.py --inicio 0 --limite 5
Cada execução valida texto, palavras e ids antes de gravar na base do add-on.
"""
import argparse
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki
from nebli.explicacoes import STYLE, card_hash, collect, item, open_store, style_version

QUERY = '"tag:NEBLI::2026-uc03-patologia-23-edema-congestao"'
HERE = Path(__file__).parent

INSTRUCTION = """Escreva Tabs de Anki para um estudante de medicina do primeiro ano. Retorne SOMENTE um objeto JSON: cada chave é o id do card e cada valor é {“status”:“ok”,“texto”:“...”}. Para cada card, produza entre 165 e 205 palavras em português, contadas por palavras separadas por espaço; confira esse total antes de responder. Não encerre nenhum texto abaixo de 165 palavras. Use apenas fatos seguros a partir dos dados fornecidos. A explicação deve permitir reconstruir precisamente a resposta escondida: comece do zero, desenvolva o mecanismo causal, e conecte-o ao trecho da aula. Cada parágrafo deve começar, nesta ordem conforme aplicável, com um destes rótulos: Base:, Por quê:, Mais a fundo:, Na aula:, Liga com:, Não confundir:. Base, Por quê e Na aula são obrigatórios. Não repita a pergunta, não use introdução nem listas. O campo alvo_oculto é o que este card esconde. Use apenas o card e o Extra recebidos.

Cards:\n"""


def words(text):
    return len(text.replace("\n", " ").split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inicio", type=int, required=True)
    ap.add_argument("--limite", type=int, default=5)
    args = ap.parse_args()
    call = Anki()
    cards = collect(call, QUERY)
    selected = cards[args.inicio:args.inicio + args.limite]
    if not selected:
        raise SystemExit("lote vazio")
    prepared = []
    for card in selected:
        payload, digest, note_id = item(call, card)
        payload.pop("ja_estudados", None)
        prepared.append((payload, digest, note_id))
    prompt = INSTRUCTION + json.dumps([p for p, _, _ in prepared], ensure_ascii=False)
    with tempfile.NamedTemporaryFile(prefix="nebli-tabs-", suffix=".json", delete=False) as f:
        out = Path(f.name)
    try:
        subprocess.run(["codex", "exec", "--ephemeral", "--skip-git-repo-check", "-c", 'model_reasoning_effort="low"', "-s", "read-only", "-C", "/tmp", "--output-last-message", str(out), "-"],
                       input=prompt, text=True, check=True, timeout=300)
        raw = out.read_text(encoding="utf-8").strip()
        raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        answer = json.loads(raw)
    finally:
        out.unlink(missing_ok=True)
    expected = {p["id"] for p, _, _ in prepared}
    if set(answer) != expected:
        raise RuntimeError(f"ids divergentes: {set(answer) ^ expected}")
    bad = []
    for p, _, _ in prepared:
        a = answer[p["id"]]
        text = a.get("texto", "")
        n = words(text)
        if a.get("status") != "ok" or not all(label in text for label in ("Base:", "Por quê:", "Na aula:")) or not 150 <= n <= 220:
            bad.append((p["id"], a.get("status"), n))
    if bad:
        (HERE / f"tabs-codex-falha-{args.inicio}.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2))
        raise RuntimeError(f"texto fora do padrão: {bad}")
    db = open_store()
    style = style_version(STYLE.read_text(encoding="utf-8"))
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    for p, digest, note_id in prepared:
        a = answer[p["id"]]
        db.execute("insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)",
                   (int(p["id"]), note_id, digest, "ok", a["texto"], None, style,
                    "codex-chatgpt-subscription", stamp))
    db.commit()
    print(json.dumps({"inicio": args.inicio, "cards": len(prepared),
                      "palavras": {p["id"]: words(answer[p["id"]]["texto"]) for p, _, _ in prepared}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
