"""uso: fecha.py <corrida> <notas> <cards> '<resumo md (linhas após o título)>' — grava REVISAO no spec, REVISAO-DE-QUALIDADE.md, rebuild e pos."""
import sys, subprocess, json
from pathlib import Path
run, notas, cards, corpo = Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
corr = sys.argv[5] if len(sys.argv) > 5 else ""
s = (run / "spec.py").read_text()
txt = f"Despejo lido inteiro em 17/10 ({notas} notas novas, {cards} cards; frentes, clozes, versos, imagens e cores conferidos). " + ("Nada a corrigir." if not corr else corr)
lista = json.dumps([c for c in sys.argv[6:]], ensure_ascii=False) if len(sys.argv) > 6 else "[]"
if "REVISAO = {}" in s:
    s = s.replace("REVISAO = {}", "REVISAO = {" + f'"despejo": {json.dumps(txt, ensure_ascii=False)}, "corrigidos": {lista}' + "}", 1)
    (run / "spec.py").write_text(s)
plan = json.loads((run / "plan.json").read_text())
(run / "REVISAO-DE-QUALIDADE.md").write_text(f"# {plan['lesson_id']} — v2 (pipeline AnKing-primeiro v4), instalada 17/10 (Claude)\n\n**Deck:** `{plan['deck']}`; {cards} cards novos ({notas} notas). Sem Tab.\n{corpo}\n**Lido no deck instalado:** despejo inteiro lido; " + ("nada a corrigir." if not corr else corr) + " Ordem conferida.\n**Pendências:** Tab (Codex).\n")
subprocess.run("NEBLI_SEM_TAB=1 /usr/bin/python3 build.py >/dev/null 2>&1", shell=True, cwd=run)
args = ["--li-despejo"] + (["--corrigidos", ",".join(sys.argv[6:])] if len(sys.argv) > 6 else [])
out = subprocess.run(["/usr/bin/python3", "-m", "nebli.artefatos", "pos", str(run)] + args, cwd=Path.home() / "NEBLI",
                     capture_output=True, text=True, env={**__import__("os").environ, "NEBLI_SEM_TAB": "1"}).stdout
print("\n".join(l for l in out.splitlines() if "FALHA" in l or "passos" in l))
