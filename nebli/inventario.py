"""Inventário atômico de uma aula → inventario-aula.json, alvos do planejamento.json e cobertura.json (F-20261009-CLAUDE-02).

    python3 -m nebli.inventario arquivos-trabalho/<corrida> [--instalado]

Lê `<corrida>/inventario.py`, escrito a partir do material de base ANTES de escolher cards, com:
    PREFIXO = "fi09"; AULA = "Motilidade II (...)"
    SLIDES = [(n, classe, titulo, [(chave, texto, destino), ...]), ...]   # classe: conteudo | capa | revisao | video
    CAPITULO = [(secao, [(chave, texto, destino), ...]), ...]             # livro da UC
    EXERCICIOS = [(fonte, [(chave, texto, destino), ...]), ...]           # provas, monitoria, apostila de veteranos
    JUSTIFICATIVAS = {"capa": "...", ...}                                  # opcional, por classe sem conteúdo
destino: chave de card do spec, lista de chaves, "sh-<nid>" de compartilhado, ou "EXC: motivo" (só lâmina; nunca livro/prova).

Um item é uma ideia que a aula ensina e que deve ser recuperável por pelo menos um card; menção no verso não conta.
`--instalado` marca a cobertura como conferida depois de instalar (só use depois de ver os cards no Anki).
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

EXC = "EXC:"
JUST = {"capa": "capa, abertura ou encerramento, sem conteúdo", "video": "vídeo sem conteúdo próprio na lâmina",
        "revisao": "revisão de outra aula, sem alvo novo"}


def _load(run: Path):
    spec = importlib.util.spec_from_file_location("inventario_aula", run / "inventario.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _cards(dest):
    return list(dest) if isinstance(dest, (list, tuple)) else [dest]


def gerar(run: Path, instalado: bool = False):
    m = _load(run)
    pre, just = m.PREFIXO, {**JUST, **getattr(m, "JUSTIFICATIVAS", {})}
    slides, alvos, cob = [], [], []

    def item(iid, texto, dest, fonte, slide):
        it = {"id": iid, "texto": texto}
        rec = {"id": iid, "fonte": fonte, "item": texto}
        if isinstance(dest, str) and dest.startswith(EXC):
            motivo = dest[len(EXC):].strip()
            it.update(exclusao_permitida=True, exclusao=motivo)
            rec.update(cards=[], excluido=motivo)
            prev = "exclusão"
        else:
            it["card"] = _cards(dest)[0] if len(_cards(dest)) == 1 else _cards(dest)
            rec["cards"] = _cards(dest)
            prev = ", ".join(_cards(dest))
        alvos.append({"id": iid, "slide": slide, "alvo": texto, "fontes": [fonte], "origem_prevista": prev})
        cob.append(rec)
        return it

    for n, classe, titulo, itens in m.SLIDES:
        s = {"numero": n, "classe": "conteudo" if classe == "conteudo" else classe, "titulo": titulo}
        if classe == "conteudo":
            s["itens"] = [item(f"{pre}-s{n:02d}-{k}", t, d, f"slide {n}", str(n)) for k, t, d in itens]
        else:
            s["classe"] = "capa" if classe in ("capa", "video") else classe
            s["justificativa"] = just[classe]
            cob.append({"id": f"{pre}-s{n:02d}", "fonte": f"slide {n}", "item": titulo, "cards": [], "excluido": just[classe]})
        slides.append(s)
    secs = {}
    for nome, attr, prefixo, slide in (("capitulo", "CAPITULO", "cap", "livro"), ("exercicios", "EXERCICIOS", "prova", "prova")):
        out = []
        for fonte, itens in getattr(m, attr, []):
            src = f"livro {fonte}" if prefixo == "cap" else fonte
            for k, t, d in itens:
                # F-20261012-CLAUDE-01: o capítulo do livro vai além da aula; item que pertence a outra aula do cronograma
                # pode ser excluído com motivo. Prova/material da aula continua sem exclusão.
                # F-20261013-CLAUDE-03: só a questão de PROVA obriga card; palavras-cruzadas, apostila, monitoria e bibliografia
                # podem ficar sem card quando o detalhe não é alvo da aula (com motivo escrito).
                prova = prefixo != "cap" and "prova" in fonte.lower()
                if isinstance(d, str) and d.startswith(EXC) and ((prefixo == "cap" and "aula" not in d.lower()) or prova
                                                                 or not d[len(EXC):].strip()):
                    raise SystemExit(f"{k}: item de prova não pode ser excluído (livro só com motivo citando a aula própria); ligue a um card")
            its = [item(f"{pre}-{prefixo}-{k}", t, d, src, slide) for k, t, d in itens]
            if prefixo != "cap" and "prova" not in fonte.lower():
                for it in its:
                    it["apoio"] = True  # material de apoio, não questão de prova
            out.append({("secao" if prefixo == "cap" else "fonte"): fonte, "itens": its})
        secs[nome] = out
    inv = {"aula": m.AULA, "lido_antes_da_selecao": True, "slides": slides, "capitulo": secs["capitulo"], "exercicios": secs["exercicios"]}
    (run / "inventario-aula.json").write_text(json.dumps(inv, ensure_ascii=False, indent=1))

    pp = run / "planejamento.json"
    plan = json.loads(pp.read_text()) if pp.exists() else {"aula": m.AULA, "feito_antes_de_montar": True}
    antigos = [a for a in plan.get("alvos", []) if not a.get("id")]
    if antigos:
        plan["alvos_por_lamina_antigos"] = antigos
    plan["alvos"] = alvos
    pp.write_text(json.dumps(plan, ensure_ascii=False, indent=1))

    cp = run / "cobertura.json"
    old = json.loads(cp.read_text()) if cp.exists() else {}
    cobertura = {"aula": old.get("aula", m.AULA), "conferido_depois_de_instalar": bool(instalado),
                 "como": "inventário atômico (nebli.inventario): cada ideia das lâminas, do livro e das provas/monitoria ligada a um card que a recupera",
                 "itens": cob}
    cp.write_text(json.dumps(cobertura, ensure_ascii=False, indent=1))
    n_exc = sum(1 for c in cob if not c["cards"])
    print(f"{len(slides)} lâminas; {len(cob)} itens; {n_exc} sem card (lâminas sem conteúdo ou exclusões)")


if __name__ == "__main__":
    gerar(Path(sys.argv[1]), "--instalado" in sys.argv)
