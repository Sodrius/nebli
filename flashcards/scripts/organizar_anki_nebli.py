#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Organiza a coleção do Davi na árvore NEBLI::UC::Prova::Componente::Aula.
Regra canônica: o AnKing fica INTOCADO como referência (tudo suspenso); os cards de
estudo já são CÓPIAS no NEBLI (com tags). Este script:
  1. cria a árvore NEBLI e MOVE as cópias curadas para o subdeck da aula (por cronograma);
  2. SUSPENDE o AnKing Step Deck inteiro (referência) + árvores duplicadas + restos de teste;
  3. deixa só o NEBLI:: ativo.
Uso: python organizar_anki_nebli.py [--apply]  (default = dry-run).
Reversível: mover de volta + unsuspend. Nunca apaga card.
"""
import json, urllib.request, sys
sys.stdout.reconfigure(encoding="utf-8")
APPLY = "--apply" in sys.argv
def call(a, **p):
    req = urllib.request.Request("http://localhost:8765",
        json.dumps({"action": a, "version": 6, "params": p}).encode(), {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=90))
    if r.get("error"): raise RuntimeError(r["error"])
    return r["result"]
def cards(q): return call("findCards", query=q)

# aula curada (deck atual) -> deck-alvo na árvore NEBLI (prova do cronograma UC02 v1-jul)
MOVES = {
 "UC02::Bioquímica::Metabolismo dos aminoácidos":            "NEBLI::UC02::P4::Bioquímica::Metabolismo dos aminoácidos",
 "UC02::Bioquímica::Metabolismo dos lipídeos":               "NEBLI::UC02::P4::Bioquímica::Metabolismo dos lipídeos",
 "UC02::Biologia Molecular::DNA - mutação, lesão e reparo":  "NEBLI::UC02::P4::Biologia Molecular::DNA - mutação, lesão e reparo",
 "UC02::Embriologia::Embrio I - gametogênese e fertilização":       "NEBLI::UC02::P3::Embriologia::Embrio I - gametogênese e fertilização",
 "UC02::Embriologia::Embrio II-III - gastrulação e neurulação":     "NEBLI::UC02::P3::Embriologia::Embrio II-III - gastrulação e neurulação",
}
# suspender (referência intocada + duplicatas + restos de teste "várzea")
SUSPEND = [
 ('AnKing referência (tudo)',        'deck:"AnKing Step Deck" -is:suspended'),
 ('árvore duplicada Medicina::',     'deck:"Medicina" -is:suspended'),
 ('resto: NEBLI::zerado',            'tag:NEBLI::zerado::2026-07-03 -is:suspended'),
 ('resto: NEBLI::anking-curado (ANATO-06, outra UC)', 'tag:NEBLI::anking-curado -is:suspended'),
 ('resto: glicogênio stray (sem E1)','tag:NEBLI::bioq-glicogenio -is:suspended'),
]

def main():
    print("MODO:", "APPLY" if APPLY else "DRY-RUN", "\n")
    print("== MOVER cópias curadas para a árvore NEBLI ==")
    total_move = 0
    for src, dst in MOVES.items():
        ids = cards('deck:"%s"' % src)
        total_move += len(ids)
        print("  %3d cards | %s  ->  %s" % (len(ids), src, dst))
        if APPLY and ids:
            call("createDeck", deck=dst)
            call("changeDeck", cards=ids, deck=dst)
    print("  total a mover: %d\n" % total_move)
    print("== SUSPENDER (referência + duplicatas + restos) ==")
    total_susp = 0
    for label, q in SUSPEND:
        ids = cards(q)
        total_susp += len(ids)
        print("  %4d cards | %s" % (len(ids), label))
        if APPLY and ids:
            call("suspend", cards=ids)
    print("  total a suspender: %d\n" % total_susp)
    if APPLY:
        # ritmo: 15 novos/dia no topo NEBLI
        try:
            cfg = call("getDeckConfig", deck="NEBLI")
            cfg["new"]["perDay"] = 15
            cfg["rev"]["perDay"] = 9999
            call("saveDeckConfig", config=cfg)
            print("novos/dia=15, revisões/dia=9999 salvos no preset '%s' (usado pelo deck NEBLI)." % cfg.get("name","?"))
        except Exception as e:
            print("!! configurar 15 novos/dia falhou (%s) — setar manual em Opções do deck NEBLI." % e)
        call("sync")
        print("sync disparado.")
    else:
        print("(dry-run — nada mudou. Rode com --apply para executar.)")
        print("Estado esperado após apply: só o NEBLI:: ativo (~%d cards), AnKing e restos suspensos." % total_move)

main()
