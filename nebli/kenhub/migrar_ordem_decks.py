"""Planeja (padrão) ou aplica em um lote a ordem visível dos decks da UC07.

Uso seguro:
    python -m nebli.kenhub.migrar_ordem_decks
    python -m nebli.kenhub.migrar_ordem_decks --aplicar

Sem ``--aplicar`` só lê o Anki e grava o relatório local. A aplicação usa o
add-on para renomear os IDs existentes; não move cards e não sincroniza.
"""
from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone

from nebli.decks import Anki, ROOT, escrita
from nebli.rotulos import canonical
from nebli.kenhub.ordem_decks import plano_renomeacao


SAIDA = ROOT / "arquivos-trabalho" / "uc07-ordem-kenhub-migracao.json"
PEDIDO = ROOT / "arquivos-trabalho" / "anki-acao-pedido.json"
RESPOSTA = ROOT / "arquivos-trabalho" / "anki-acao-resposta.json"


def inventario(A: Anki):
    vivos = {canonical(n): did for n, did in A("deckNamesAndIds").items()}
    esperado = plano_renomeacao()
    pares = [{"de": de, "para": para, "id": vivos[de]} for de, para in esperado.items() if de in vivos]
    ja = [{"nome": para, "id": vivos[para]} for para in esperado.values() if para in vivos]
    conflitos = [p for p in pares if p["para"] in vivos and vivos[p["para"]] != p["id"]]
    return vivos, pares, ja, conflitos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aplicar", action="store_true", help="renomeia em um lote, sem sync")
    args = ap.parse_args()
    A = Anki()
    vivos, pares, ja, conflitos = inventario(A)
    rel = {"em": datetime.now(timezone.utc).isoformat(), "modo": "aplicar" if args.aplicar else "simular",
           "renomear": pares, "ja_ordenados": ja, "conflitos": conflitos,
           "garantias": ["IDs dos decks preservados", "cards/notas/histórico/agendamento inalterados", "sem sincronização"]}
    SAIDA.write_text(json.dumps(rel, ensure_ascii=False, indent=2), encoding="utf-8")
    if conflitos:
        raise SystemExit(f"conflitos: {len(conflitos)}; ver {SAIDA}")
    if not args.aplicar:
        print(f"SIMULAÇÃO: {len(pares)} decks a renomear; {len(ja)} já ordenados; relatório {SAIDA}")
        return
    if not pares:
        print("Nada a renomear.")
        return
    with escrita(A, "UC07 ordem Kenhub", sync=False):
        if PEDIDO.exists():
            raise SystemExit(f"há outro pedido pendente: {PEDIDO}")
        RESPOSTA.unlink(missing_ok=True)
        PEDIDO.write_text(json.dumps({"acao": "renomear_decks", "mapeamentos": [{"de": p["de"], "para": p["para"]} for p in pares]},
                                     ensure_ascii=False), encoding="utf-8")
        limite = time.monotonic() + 30
        while not RESPOSTA.exists() and time.monotonic() < limite:
            time.sleep(.25)
        if not RESPOSTA.exists():
            raise SystemExit("o add-on não respondeu em 30 s; nenhuma confirmação de migração")
        resposta = json.loads(RESPOSTA.read_text(encoding="utf-8"))
        if len(resposta.get("renomeados", [])) != len(pares):
            raise SystemExit(f"migração incompleta: {resposta}")
        _, restantes, _, conflitos_pos = inventario(A)
        if restantes or conflitos_pos:
            raise SystemExit(f"readback reprovou: restantes={len(restantes)}, conflitos={len(conflitos_pos)}")
    print(f"OK: {len(pares)} decks renomeados, IDs preservados, sem sync")


if __name__ == "__main__":
    main()
