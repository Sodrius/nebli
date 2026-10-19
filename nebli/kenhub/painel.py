"""Painel da UC07 para começar toda sessão: feedbacks de Davi → gates duros (conferidos) + onde estamos + próximo passo.

    ./kenhub-deck --painel      (gera flashcards/projeto/UC07-PAINEL.md e imprime o resumo)
"""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SAIDA = ROOT / "flashcards" / "projeto" / "UC07-PAINEL.md"
PLANO = "flashcards/projeto/PLANO-UC07-NEUROANATOMIA-COMPLETA-2026-10-17.md"


def ordem_oficial():
    """slug → posição oficial do Kenhub, lida da coluna # do plano mestre."""
    out = {}
    for linha in (ROOT / PLANO).read_text().splitlines():
        cols = [c.strip() for c in linha.split("|")]
        if len(cols) > 7 and cols[1].isdigit() and cols[3].isdigit() and "`" in cols[6]:
            out[cols[6].strip("`")] = int(cols[3])
    return out


def gate_ordem_kenhub(valores):
    """[G29 ordem Kenhub] A sequência de auditoria/produção segue a ordem oficial."""
    return [] if valores and valores == sorted(valores) else ["[G29 ordem Kenhub] unidades fora da ordem oficial do Kenhub ou fila vazia"]


def main():
    reg = json.loads((Path(__file__).parent / "feedbacks.json").read_text())
    teste = subprocess.run([sys.executable, "-W", "ignore", "-m", "nebli.kenhub.teste_gates"], cwd=ROOT, capture_output=True, text=True)
    ok = teste.returncode == 0
    unidades = []
    ordem = ordem_oficial()
    recibos = list((ROOT / "arquivos-trabalho").glob("uc07-kenhub-*/receipt.json"))
    recibos.sort(key=lambda rec: ordem.get(json.loads((rec.parent / "curadoria.json").read_text()).get("unidade_kenhub"), 999))
    for rec in recibos:
        r = json.loads(rec.read_text())
        cor = [n["cor"] for n in r["notas"]]
        rev = rec.parent / "revisao.json"
        revisada = rev.exists() and json.loads(rev.read_text()).get("run") == r["run"]
        estado = "REPROVADA" if (r.get("falhas_pos") or r.get("falhas_render")) else (
            "ENTREGUE (gates ok + revisão card a card e do deck)" if revisada else "AGUARDANDO REVISÃO (revisao.md)")
        unidades.append(f"| {r['deck']} | {len(r['notas'])} | {cor.count('verde')}/{cor.count('azul')}/{cor.count('rosa')} | {estado} | {r['at'][:16]} | `{rec.parent.name}` |")
    linhas = ["# UC07 — painel de sessão (gerado; não editar à mão)", "",
              f"Gerado em {datetime.now():%d/%m/%Y %H:%M} por `./kenhub-deck --painel`. **Ler no início de toda sessão da UC07.**", "",
              "## Onde estamos", "", "| Deck | Notas | Verde/azul/rosa | Estado | Última execução | Corrida |", "|---|---|---|---|---|---|",
              *unidades, "", f"Fila e tabela das 51 unidades: [{Path(PLANO).name}]({Path(PLANO).name}). Próxima: a primeira “a fazer” na ordem sugerida do plano.",
              "", "## Rodar uma unidade", "", "```", "./kenhub-deck <slug-da-unidade> \"<Módulo>\" \"<Submódulo>\"", "```",
              "Para pedindo curadoria (rascunho gerado); depois instala, reconcilia e só termina com TODOS os gates ok. Olhar as folhas de contato.",
              "Antes de instalar: navegador de cards do Anki fechado (o comando avisa). No fim: `pkill -f nebli.kenhub.navegador` (Kenhub = 1 aparelho por vez).",
              "", f"## Feedbacks de Davi → gates duros (teste dos gates: {'OK' if ok else 'REPROVADO'})", "",
              "| Id | Regra | Gates (onde reprova) | Prova |", "|---|---|---|---|"]
    for f in reg["feedbacks"]:
        g = "<br>".join(f"`{x['codigo'].strip()}` ({Path(x['arquivo']).name})" for x in f["gates"])
        linhas.append(f"| {f['id']} | {f['regra']} | {g} | {f['teste']} |")
    linhas += ["", "Feedback novo: literal em FEEDBACKS → regra no MEMORY §15 → entrada em `nebli/kenhub/feedbacks.json` → gate no código "
               "→ caso ruim em `teste_gates.py` → `./kenhub-deck --painel` verde.", ""]
    if not ok:
        linhas += ["## FALHA DO TESTE DOS GATES", "", "```", teste.stdout[-2000:] + teste.stderr[-1000:], "```"]
    SAIDA.write_text("\n".join(linhas) + "\n")
    print(f"painel: {SAIDA.relative_to(ROOT)} | teste dos gates: {'ok' if ok else 'REPROVADO'} | unidades: {len(unidades)}")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
