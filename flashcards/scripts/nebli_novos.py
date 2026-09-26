"""Controle manual de quantos cards novos do NEBLI entram por dia ou por semana.

Todos os decks NEBLI::* usam o mesmo preset de opções ("NEBLI"). Mudar o número
aqui (ou em Anki > Opções do baralho NEBLI > Limites diários > Novos cards/dia)
vale para o NEBLI inteiro, sem tocar em AnKing, Referências ou Etimologia.

Uso (Anki aberto, AnkiConnect ativo):
    python flashcards/scripts/nebli_novos.py --status
    python flashcards/scripts/nebli_novos.py --dia 35
    python flashcards/scripts/nebli_novos.py --semana 245      # vira ceil(245/7) = 35 por dia
    python flashcards/scripts/nebli_novos.py --alinhar         # põe decks NEBLI novos no preset

O Anki não tem limite semanal nativo: --semana só converte para o limite diário.
Para um dia só (cram), use a aba "Somente hoje" nas opções do baralho NEBLI.
"""
import argparse
import json
import math
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

URL = "http://127.0.0.1:8765"
PRESET = "NEBLI"
ROOT = "NEBLI"
BACKUP_DIR = Path(__file__).resolve().parents[2] / "arquivos-trabalho" / "anki-config-backups"


def ac(action, **params):
    req = urllib.request.Request(URL, json.dumps({"action": action, "version": 6, "params": params}).encode())
    res = json.load(urllib.request.urlopen(req, timeout=30))
    if res.get("error"):
        raise SystemExit(f"AnkiConnect {action}: {res['error']}")
    return res["result"]


def canonical(name):
    """Tira o total de cards que o add-on nebli_decks põe no nome ("NEBLI (1525)")."""
    return re.sub(r" \(\d+\)(?=::|$)", "", name)


def nebli_decks():
    return [d for d in ac("deckNames") if canonical(d).split("::")[0] == ROOT]


def root():
    return next(d for d in ac("deckNames") if canonical(d) == ROOT)


def preset():
    cfg = ac("getDeckConfig", deck=root())
    if cfg["id"] == 1:
        raise SystemExit("O deck NEBLI usa o preset Padrão; rode --alinhar para criar o preset próprio.")
    return cfg


def backup(tag):
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    snap = {d: ac("getDeckConfig", deck=d) for d in nebli_decks()}
    path = BACKUP_DIR / f"{datetime.now():%Y%m%d-%H%M%S}-{tag}.json"
    path.write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
    return path


def alinhar():
    root_cfg = ac("getDeckConfig", deck=root())
    if root_cfg["id"] == 1:
        new_id = ac("cloneDeckConfigId", name=PRESET, cloneFrom=1)
        ac("setDeckConfigId", decks=[root()], configId=new_id)
        root_cfg = ac("getDeckConfig", deck=root())
    antigos = {}
    for d in nebli_decks():
        cfg = ac("getDeckConfig", deck=d)
        if cfg["id"] != root_cfg["id"]:
            antigos.setdefault(cfg["id"], (cfg, []))[1].append(d)
    fora = [d for _, decks in antigos.values() for d in decks]
    if fora:
        ac("setDeckConfigId", decks=fora, configId=root_cfg["id"])
    # Preset largado com o mesmo nome é a armadilha do menu de Opções: escolher o
    # "NEBLI" errado tira o deck do preset compartilhado sem aviso.
    for cfg, _ in antigos.values():
        if cfg["id"] != 1 and cfg["name"] == root_cfg["name"]:
            cfg["name"] = f"{PRESET} antigo {cfg['id']} (não usar)"
            ac("saveDeckConfig", config=cfg)
    return root_cfg, fora


def definir(por_dia):
    cfg = preset()
    cfg["new"]["perDay"] = por_dia
    cfg["name"] = PRESET
    ac("saveDeckConfig", config=cfg)


def status():
    cfg = preset()
    decks = nebli_decks()
    fora = [d for d in decks if ac("getDeckConfig", deck=d)["id"] != cfg["id"]]
    novos = len(ac("findCards", query=f'"deck:{root()}" is:new -is:suspended'))
    hoje = len(ac("findCards", query=f'"deck:{root()}" introduced:1'))
    print(f"Preset: {cfg['name']} (id {cfg['id']})")
    print(f"Novos por dia: {cfg['new']['perDay']}  (≈ {cfg['new']['perDay'] * 7} por semana)")
    print(f"Revisões por dia: {cfg['rev']['perDay']}")
    print(f"Novos disponíveis no NEBLI: {novos}; introduzidos hoje: {hoje}")
    if novos and cfg["new"]["perDay"]:
        print(f"No ritmo atual, os novos acabam em ~{math.ceil(novos / cfg['new']['perDay'])} dia(s).")
    print("Decks fora do preset: " + (", ".join(fora) if fora else "nenhum"))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--status", action="store_true")
    g.add_argument("--dia", type=int, metavar="N")
    g.add_argument("--semana", type=int, metavar="N")
    g.add_argument("--alinhar", action="store_true")
    a = p.parse_args()

    if a.status:
        status()
        return
    tag = "alinhar" if a.alinhar else f"dia-{a.dia}" if a.dia is not None else f"semana-{a.semana}"
    print(f"Backup: {backup(tag)}")
    alinhar()
    if a.dia is not None or a.semana is not None:
        n = a.dia if a.dia is not None else math.ceil(a.semana / 7)
        if n < 0:
            sys.exit("Número negativo.")
        definir(n)
    status()


if __name__ == "__main__":
    main()
