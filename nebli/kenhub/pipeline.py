"""Uma unidade do Kenhub → deck final no Anki, com todos os gates duros (F-20261017-CLAUDE-01/02/03).

    ./kenhub-deck <slug-da-unidade> "<Módulo>" "<Submódulo>"
    ./kenhub-deck <slug> "<Módulo>" "<Submódulo>" --dry-run   (coleta, curadoria e gates PRÉ sem escrever no Anki)
    ./kenhub-deck --painel        (feedbacks → gates conferidos + onde estamos; ler no início de toda sessão)
    ./kenhub-deck --resumo <corrida>   (rascunho da curadoria em forma compacta, com os candidatos já pré-checados nos gates)

Etapas (tudo invisível, nada abre janela; Davi está sempre no Anki):
  1. navegador do Kenhub (sessão de Davi) — sobe se não estiver de pé;
  2. coleta (estruturas, nomes PT/EN/latim, uma figura por estrutura), só o que falta;
  3. busca nos acervos e rascunho da curadoria (cores, acervo, AnKing candidatos) — PARA se `curadoria.json` ainda não existe;
  4. deck: gates pré → instalação (dessuspenso, bandeiras) → gates pós (lê o Anki) → renderização do deck inteiro (PC e celular).
Sai com erro se qualquer gate reprovar. Depois: olhar as folhas de contato em <corrida>/render/grandes antes de entregar.
"""
import hashlib
import json
import re
import subprocess
import sys
import time
import unicodedata
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

from nebli.kenhub import caminhos, navegador

ROOT = Path(__file__).resolve().parents[2]
SISTEMA = "/usr/bin/python3"   # tem fastembed (busca semântica); o venv do Kenhub tem o Playwright


def slug(texto: str) -> str:
    s = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def navegador_de_pe() -> bool:
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{navegador.PORTA}/json/version", timeout=3)
        return True
    except Exception:
        return False


def subir_navegador():
    if navegador_de_pe():
        return
    log = Path("/tmp/kenhub-navegador.log")
    subprocess.Popen([sys.executable, "-m", "nebli.kenhub.navegador"], cwd=ROOT, stdout=log.open("w"), stderr=subprocess.STDOUT,
                     start_new_session=True)
    for _ in range(40):
        time.sleep(1)
        if navegador_de_pe():
            return
    raise SystemExit(f"navegador do Kenhub não subiu; ver {log}")


def _pre_checar(A, cand, media):
    """Para cada candidato do acervo, calcula o que os gates do deck vão exigir (evita tentativa e erro na curadoria)."""
    import os
    import re
    import urllib.parse
    from nebli.kenhub import deck
    n = A("notesInfo", notes=[cand["nid"]])[0]
    campos = deck._local({k: v["value"] for k, v in n["fields"].items()}, media)
    if cand["acervo"] == "AnatoKing":
        modelos = deck._imgs(campos.get("Model", ""))
        todas = " ".join(modelos + deck._imgs(campos.get("Cadaver", "")) + deck._imgs(campos.get("Imaging", "")) + deck._imgs(campos.get("Illustration", "")))
        falta = deck._midia_faltando(todas, media)
        if not modelos:
            cand["gate"] = "sem figura de modelo"
            return cand
        nome = urllib.parse.unquote(re.search(r'src="([^"]+)"', modelos[0]).group(1))
        arq = os.path.join(media, nome)
        verm = deck._fracao_vermelha(arq) if os.path.exists(arq) else 0.0
        usos = len(A("findNotes", query=f'"deck:Referências::Referências Externas::AnatoKing" "Model:*{nome}*"'))
        motivos = []
        if falta:
            motivos.append(f"{len(falta)} imagem(ns) ausente(s)")
        if usos > 1:
            motivos.append(f"modelo genérico ({usos} cards)")
        if not 0.0001 <= verm <= 0.045:
            motivos.append(f"sem seta vermelha ({verm:.3%})")
        cand["gate"] = "OK" if not motivos else "; ".join(motivos)
        cand["en"] = deck._limpo(re.sub(r"\{\{c\d::(.*?)(?:::[^}]*)?\}\}", r"\1", campos["Text"]))[:70]
    else:
        cand["gate"] = "falta mídia" if deck._midia_faltando(" ".join(campos.values()), media) else "OK"
        cand["en"] = deck._limpo(re.sub(r"\{\{c\d::(.*?)(?:::[^}]*)?\}\}", r"[\1]", campos["Text"]))[:130]
        cand["hy"] = next((t.split("::")[-1][:1] for t in n["tags"] if "Yield" in t), "")
    return cand


def rascunho(corrida: Path, base: Path, unidade: str, modulo: str, sub: str):
    """Candidatos por estrutura nos acervos, já pré-checados contra os gates (AnatoKing: modelo com seta, único, mídia presente)."""
    from nebli.kenhub import deck
    A = deck.AnkiPaciente()
    media = A("getMediaDirPath")
    itens = json.loads((base / "itens.json").read_text())["itens"]
    consultas = [f"{i['slug']}={i['nome_en']} neuroanatomy" for i in itens]
    for t in json.loads((base / "itens.json").read_text()).get("texto", []):   # AnKing também para os fatos do texto (F-20261018-CLAUDE-01)
        for k, frase in enumerate([x.strip() for x in re.split(r"(?<=[.;])\s+|\n", t["en"]) if len(x.strip()) >= 30], 1):
            consultas.append(f"texto:{t['chave']}#{k}={frase[:240]}")
    subprocess.run([SISTEMA, "-m", "nebli.semantica", "buscar", str(corrida), *consultas, "--k", "8"], cwd=ROOT, check=True,
                   stdout=subprocess.DEVNULL)
    linhas = [json.loads(x) for x in (corrida / "busca" / "semantica.jsonl").read_text().splitlines()]
    cand, vistos = {}, {}
    for r in linhas:
        lista = []
        for t in r["top"]:
            if t["acervo"] in ("AnatoKing", "AnKing") and t["sim"] >= 0.8:
                if t["nid"] not in vistos:
                    vistos[t["nid"]] = _pre_checar(A, {"acervo": t["acervo"], "nid": t["nid"], "sim": t["sim"], "frente": t["frente"][:90]}, media)
                lista.append(dict(vistos[t["nid"]], sim=t["sim"]))
        cand[r["chave"]] = lista[:6]
    cand_texto = {k: v for k, v in cand.items() if k.startswith("texto:")}
    cand = {k: v for k, v in cand.items() if not k.startswith("texto:")}
    sem_figura = [i["slug"] for i in itens if i.get("sem_figura")]
    (corrida / "curadoria.rascunho.json").write_text(json.dumps(
        {"modulo": slug(modulo), "unidade": slug(sub), "unidade_kenhub": unidade,
         "deck": f"NEBLI::UC07::{modulo}::{sub}", "short": "u7" + hashlib.md5(f"{modulo}/{sub}".encode()).hexdigest()[:4],
         "lesson_id": f"2026-uc07-{slug(modulo)}-{slug(sub)}", "kenhub_excluir": {}, "nome_pt": {}, "nome_igual_ok": [],
         "acervo": [], "anking": [], "cores": {i["slug"]: "azul" for i in itens}, "texto": [], "sem_figura_no_kenhub": sem_figura, "candidatos": cand, "candidatos_texto": cand_texto},
        ensure_ascii=False, indent=1))
    return sem_figura


def resumo(corrida: Path):
    """Imprime o rascunho de forma compacta para curar rápido: estruturas, e candidatos que PASSAM nos gates marcados com ✔."""
    base_itens = None
    r = json.loads((corrida / "curadoria.rascunho.json").read_text())
    itens = json.loads((caminhos.RAIZ / r["modulo"] / r["unidade"] / "itens.json").read_text())["itens"]
    for i in itens:
        print(f"{i['slug']} | {i.get('nome_pt', '—')} | {i['nome_en']}" + (" | SEM FIGURA NO KENHUB" if i.get("sem_figura") else ""))
        for c in r["candidatos"].get(i["slug"], []):
            marca = "✔" if c.get("gate") == "OK" else "✘ " + str(c.get("gate"))
            print(f"     {c['acervo'][:4]} {c['nid']} {c['sim']:.2f} {marca} | {c.get('hy', '')} {c.get('en', c['frente'])}")
    _resumo_texto(r, caminhos.RAIZ / r["modulo"] / r["unidade"])


def _resumo_texto(r, itens_dir):
    d = json.loads((itens_dir / "itens.json").read_text())
    print("\n=== TEXTO DA UNIDADE (cada trecho precisa de card: `texto` ou `anking` com `cobre_texto`) ===")
    for t in d.get("texto", []):
        print(f"{t['chave']} | {t['en'][:200].replace(chr(10), ' / ')}")
        vistos = set()
        for k, lista in r.get("candidatos_texto", {}).items():
            if k.startswith(f"texto:{t['chave']}#"):
                for c in lista:
                    if c["nid"] not in vistos and c.get("gate") == "OK" and c["acervo"] == "AnKing":
                        vistos.add(c["nid"])
                        print(f"     AnKi {c['nid']} {c['sim']:.2f} | {c.get('hy', '')} {c.get('en', c['frente'])}")


def revisado(corrida: Path, observacao: str):
    """Atesta que a revisão card a card + deck inteiro (revisao.md) foi feita DEPOIS de olhar as folhas. Libera “ENTREGUE” no painel."""
    rec = json.loads((corrida / "receipt.json").read_text())
    if rec.get("falhas_pos") or rec.get("falhas_render"):
        raise SystemExit("receipt com falhas: corrija antes de revisar")
    folhas = [f for f in rec["folhas"] if (corrida / "render" / "grandes" / Path(f).name).exists() or Path(f).exists()]
    if not folhas or len(folhas) != len(rec["folhas"]):
        raise SystemExit("folhas de contato ausentes: rode o render e olhe as folhas antes de revisar")
    if len(observacao.split()) < 12:
        raise SystemExit("descreva a revisão (o que viu, o que ajustou, o que o deck cobre): pelo menos 12 palavras")
    (corrida / "revisao.json").write_text(json.dumps({"notas": len(rec["notas"]), "folhas": len(folhas), "observacao": observacao,
                                                      "run": rec["run"], "em": datetime.now(timezone.utc).isoformat()}, ensure_ascii=False, indent=1))
    print(f"revisão registrada: {len(rec['notas'])} cards, {len(folhas)} folhas")


def main():
    if sys.argv[1:2] == ["--revisado"]:
        revisado(Path(sys.argv[2]), " ".join(sys.argv[3:]))
        return
    if sys.argv[1:2] == ["--resumo"]:
        resumo(Path(sys.argv[2]))
        raise SystemExit(0)
    if sys.argv[1:2] == ["--painel"]:
        from nebli.kenhub import painel
        painel.main()
    dry = "--dry-run" in sys.argv
    extra = [a for a in sys.argv[1:] if a == "--forcar"]
    args = [a for a in sys.argv[1:] if a not in ("--dry-run", "--forcar")]
    if len(args) != 3:
        raise SystemExit(__doc__)
    unidade, modulo, sub = args
    mslug, sslug = slug(modulo), slug(sub)
    base = caminhos.RAIZ / mslug / sslug
    subir_navegador()
    if not (base / "itens.json").exists():
        from nebli.kenhub import coleta
        coleta.main(unidade, mslug, sslug)
    corrida = next(iter(sorted((ROOT / "arquivos-trabalho").glob(f"uc07-kenhub-{mslug}-{sslug}-*"))), None) \
        or ROOT / "arquivos-trabalho" / f"uc07-kenhub-{mslug}-{sslug}-{date.today().isoformat()}"
    corrida.mkdir(parents=True, exist_ok=True)
    if not (corrida / "curadoria.json").exists():
        sem = rascunho(corrida, base, unidade, modulo, sub)
        raise SystemExit(f"curadoria pendente: revisar {corrida / 'curadoria.rascunho.json'} (estruturas sem figura no Kenhub: "
                         f"{len(sem)}), gravar {corrida / 'curadoria.json'} e rodar de novo")
    r = subprocess.run([sys.executable, "-m", "nebli.kenhub.deck", str(corrida)] + (["--dry-run"] if dry else []) + extra, cwd=ROOT)
    raise SystemExit(r.returncode)


if __name__ == "__main__":
    main()
