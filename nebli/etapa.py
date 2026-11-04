"""Diário das etapas do pipeline de deck (F-20261023-CLAUDE-02: “coloca gate para seguir o passo a passo e fazer o planejamento e revisão
de verdade, sem só fazer um deck com base no que vc acha que é a aula”).

    python3 -m nebli.etapa <corrida> E2 "o que fiz nesta etapa"     # registra a etapa ao concluí-la (E0…E8)
    python3 -m nebli.etapa <corrida> --ver

Cada linha de <corrida>/etapas.jsonl guarda a etapa, a hora e o hash dos artefatos dela. Registrar uma etapa exige o artefato da etapa
e a etapa anterior já registrada; a busca (E4) e o build recusam rodar sem a compreensão (E2) e o mapa (E3) prontos (`exigir_planejamento`).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ORDEM = ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"]
ARTEFATOS = {"E0": ["exemplares-lidos.json"], "E1": ["fontes-decl.json"], "E2": ["compreensao-aula.json"],
             "E3": ["mapa-de-profundidade.json", "escopo.json", "inventario.py"], "E4": ["busca/semantica.jsonl"],
             "E5": ["spec.py", "plan.json", "busca/cobertura.tsv"], "E6": ["receipt.json", "revisao-despejo.txt"],
             "E7": ["compreensao-aula.json"], "E8": []}


def _sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16] if p.is_file() else None


def registros(run: Path):
    arq = Path(run) / "etapas.jsonl"
    return [json.loads(l) for l in arq.read_text(encoding="utf-8").splitlines() if l.strip()] if arq.exists() else []


def problemas_compreensao(run: Path):
    """O que falta para a compreensão (E2) valer: o que a aula ensina, e em cada bloco de conteúdo o processo e o que se aprende."""
    try:
        d = json.loads((Path(run) / "compreensao-aula.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ["compreensao-aula.json ausente"]
    probs = []
    if "<" in str(d.get("o_que_a_aula_ensina", "")) or len(str(d.get("o_que_a_aula_ensina", ""))) < 150:
        probs.append("o_que_a_aula_ensina não escrito")
    for b in d.get("blocos", []):
        if b.get("papel") in ("principio", "exemplo"):
            apr = [x for x in b.get("aprender", []) if len(str(x).strip()) >= 15]
            if not apr:
                probs.append(f"bloco {b.get('laminas')} sem 'aprender' (o que o professor quer que se aprenda ali, conferido no slide)")
            if b.get("papel") == "exemplo" and not b.get("ilustra"):
                probs.append(f"bloco de exemplo {b.get('laminas')} sem 'ilustra' (a lâmina inicial do bloco de princípio que ele ilustra)")
    if versao(run) >= 10:
        probs += problemas_exemplo_da_aula(run)
    return probs


ROTULO_EXEMPLO = re.compile(r"\bexemplo|\bexemplifica|\bilustra|caso cl[ií]nico|combina[çc][ãa]o de tudo", re.I)


def _paginas_slides(run: Path):
    try:
        txt = (Path(run) / "fontes" / "slides.txt").read_text(encoding="utf-8")
    except OSError:
        return None
    pags = {}
    for m in re.finditer(r"=+\s*p[áa]gina\s+(\d+)\s*=+\n(.*?)(?=\n=+\s*p[áa]gina|\Z)", txt, re.S | re.I):
        pags[int(m.group(1))] = "\n".join(l for l in m.group(2).splitlines() if "@" not in l)
    return pags


def problemas_exemplo_da_aula(run: Path):
    """F-20261029-CLAUDE-03 (61 virou deck de hepatite): “VIROU UM DECK DE HEPATITE, MAS ISSO ERA SÓ PARA ILUSTRAR / O COMEÇO DA AULA
    É MAIS IMPORTANTE”. Lâmina que o próprio professor chama de exemplo (“o exemplo da hepatite”, “caso clínico”, “combinação de
    tudo”) é bloco de papel 'exemplo', nunca 'principio'. Só sai disso com `rotulo_exemplo_e_conteudo` (≥ 80 caracteres) MAIS
    `trecho_transcricao` literal da transcrição mostrando que o professor trata os casos como o conteúdo (58: cada família resolve um
    problema). Todo bloco de exemplo declara `principios_ilustrados`: o princípio geral (≥ 40 caracteres) que cada card carrega."""
    run = Path(run)
    try:
        d = json.loads((run / "compreensao-aula.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ["compreensao-aula.json ausente"]
    pags = _paginas_slides(run)
    if not pags:
        return ["fontes/slides.txt ausente ou sem '===== página N =====': o rótulo de exemplo do professor não pôde ser conferido"]
    if re.search(r"(?m)^MODO\s*=\s*['\"]prova['\"]", (run / "spec.py").read_text(encoding="utf-8") if (run / "spec.py").exists() else ""):
        # F-20261029-CLAUDE-04: na base da prova o rótulo é o título da página ('# bloco — fonte'); “por exemplo” no texto não conta
        pags = {k: next((l for l in v.splitlines() if l.startswith("# ")), "") for k, v in pags.items()}
    try:
        transc = re.sub(r"\s+", " ", (run / "fontes" / "transcricao.txt").read_text(encoding="utf-8")).lower()
    except OSError:
        transc = ""
    probs = []
    for b in d.get("blocos", []):
        a, z = (list(b.get("laminas") or [0, 0]) + [0, 0])[:2]
        rot = sorted({ROTULO_EXEMPLO.search(pags.get(p, "")).group(0) for p in range(int(a), int(z) + 1)
                      if ROTULO_EXEMPLO.search(pags.get(p, ""))})
        if rot and b.get("papel") not in ("exemplo", "motivacao", "resumo", "repeticao"):
            trecho = re.sub(r"\s+", " ", str(b.get("trecho_transcricao", ""))).strip().lower()
            if not (len(str(b.get("rotulo_exemplo_e_conteudo", "")).strip()) >= 80 and len(trecho) >= 40 and trecho in transc):
                probs.append(f"lâminas {a}-{z}: o slide diz '{rot[0]}', mas o bloco está como '{b.get('papel')}' (exemplo do professor "
                             "é papel 'exemplo'; F-20261029-CLAUDE-03)")
        if b.get("papel") == "exemplo":
            pis = [p for p in b.get("principios_ilustrados", []) if isinstance(p, dict)]
            if not pis or any(len(str(p.get("principio", "")).strip()) < 40 for p in pis):
                probs.append(f"bloco de exemplo {a}-{z} sem 'principios_ilustrados' (o princípio geral, ≥ 40 caracteres, que cada card carrega)")
    return probs


def problemas_motivacoes(run: Path):
    """F-20261023-CLAUDE-04: “a necessidade de manter um conceito a longo prazo gera o autoral, o autoral não é justificado depois de
    feito”. Cada motivação diz qual item do mapa ela serve, o que Davi tem de conseguir reconstruir e por que precisa durar."""
    try:
        d = json.loads((Path(run) / "motivacoes.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ["motivacoes.json ausente"]
    try:
        m = json.loads((Path(run) / "mapa-de-profundidade.json").read_text(encoding="utf-8"))
        itens = {i.get("id") for p in m.get("passos", []) for i in p.get("itens", [])}
    except (OSError, ValueError):
        itens = set()
    mot = d.get("motivacoes", [])
    probs = [] if mot else ["nenhuma motivação"]
    ids = [x.get("id") for x in mot]
    if len(set(ids)) != len(ids):
        probs.append("ids de motivação repetidos")
    for x in mot:
        if x.get("item_mapa") not in itens:
            probs.append(f"{x.get('id')}: item_mapa fora do mapa")
        if len(str(x.get("reconstruir", "")).strip()) < 40 or len(str(x.get("por_que_dura", "")).strip()) < 40:
            probs.append(f"{x.get('id')}: falta o que reconstruir ou por que precisa durar (≥ 40 caracteres cada)")
    return probs


def versao(run: Path) -> int:
    m = re.search(r"^PIPELINE_VERSAO\s*=\s*(\d+)", (Path(run) / "spec.py").read_text(encoding="utf-8"), re.M) if (Path(run) / "spec.py").exists() else None
    return int(m.group(1)) if m else 0


def exigir_planejamento(run: Path, etapa: str = "a busca"):
    """Chamada pelas ferramentas de busca: sem compreensão e mapa prontos (E2 e E3 registradas), não roda (corridas v7)."""
    run = Path(run)
    if versao(run) < 7:
        return
    feitas = {r["etapa"] for r in registros(run)}
    falta = [e for e in ("E0", "E1", "E2", "E3") if e not in feitas]
    probs = problemas_compreensao(run)
    if falta or probs:
        raise SystemExit(f"{etapa} só roda depois de compreender e planejar a aula (pipeline v7): "
                         + (f"etapas não registradas {falta}; " if falta else "") + "; ".join(probs[:4]))


def registrar(run: Path, etapa: str, nota: str):
    run = Path(run)
    if etapa not in ORDEM:
        raise SystemExit(f"etapa desconhecida: {etapa}")
    feitas = [r["etapa"] for r in registros(run)]
    anterior = ORDEM[ORDEM.index(etapa) - 1] if etapa != "E0" else None
    if anterior and anterior not in feitas:
        raise SystemExit(f"{etapa} antes de {anterior}: siga o passo a passo")
    precisa = ARTEFATOS[etapa] + (["motivacoes.json"] if etapa == "E3" and versao(run) >= 8 else [])
    if etapa == "E6" and versao(run) >= 14:  # F-20261104-CLAUDE-02: E6 revisa o plano, antes de instalar
        precisa = ["plan.json", "REVISAO-DE-QUALIDADE.md", "mapa-de-profundidade.json"]
    arts = {a: _sha(run / a) for a in precisa}
    if any(v is None for v in arts.values()):
        raise SystemExit(f"{etapa} sem artefato: {[a for a, v in arts.items() if v is None]}")
    if etapa == "E0" and versao(run) >= 10:  # F-20261029-CLAUDE-03: sem a leitura obrigatória inteira, a corrida não abre
        from nebli import gates
        ruins = [k for k, ok in gates.exemplares_lidos(run) if not ok]
        if ruins:
            raise SystemExit("leitura obrigatória incompleta: " + "; ".join(ruins[:3]))
    if etapa == "E2":
        probs = problemas_compreensao(run)
        if probs:
            raise SystemExit("compreensão incompleta: " + "; ".join(probs[:5]))
    if etapa == "E3" and versao(run) >= 8:  # F-20261023-CLAUDE-04: a necessidade gera o autoral; congelar antes de buscar e escrever
        probs = problemas_motivacoes(run)
        if probs:
            raise SystemExit("motivações incompletas: " + "; ".join(probs[:5]))
        (run / "etapas").mkdir(exist_ok=True)
        (run / "etapas" / "E3-motivacoes.json").write_bytes((run / "motivacoes.json").read_bytes())
    if len(nota.strip()) < 40:
        raise SystemExit("nota da etapa curta demais: diga o que foi feito e decidido (≥ 40 caracteres)")
    linha = {"etapa": etapa, "em": datetime.now(timezone.utc).isoformat(timespec="seconds"), "nota": nota.strip(), "artefatos": arts}
    with (run / "etapas.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(linha, ensure_ascii=False) + "\n")
    print(f"{etapa} registrada")


def ordem_ok(run: Path, ate: str):
    """Para o gate: etapas E0..ate registradas, cada uma uma vez antes da seguinte."""
    regs = registros(run)
    primeiro = {}
    for i, r in enumerate(regs):
        primeiro.setdefault(r["etapa"], i)
    precisa = ORDEM[: ORDEM.index(ate) + 1]
    falta = [e for e in precisa if e not in primeiro]
    fora = [e for a, e in zip(precisa, precisa[1:]) if a in primeiro and e in primeiro and primeiro[e] < primeiro[a]]
    return falta, fora


def main(argv):
    run = Path(argv[0])
    if "--ver" in argv:
        for r in registros(run):
            print(r["em"], r["etapa"], r["nota"][:100])
        return
    registrar(run, argv[1], " ".join(argv[2:]))


if __name__ == "__main__":
    main(sys.argv[1:])
