#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Corrige os únicos excessos de Extra e uma generalização histórica legada."""
from __future__ import annotations

from nebli_anki import call

FIXES = {
    1784227543173: {
        "Text": "<b>Etimologia.</b> Endo- + thele originou 'endotelio', hoje definido como o revestimento interno de vasos e do {{c1::coracao}}.",
        "Extra": "Endotélio é epitélio simples pavimentoso que reveste vasos e câmaras cardíacas. A origem não basta para localizar a estrutura.",
    },
    1784288528859: {
        "Text": "<b>Etimologia.</b> A utilidade de reconhecer nefr/o e ren/o é ligar termos de uma mesma {{c1::família semântica}}.",
        "Extra": "Nefrite, nefropatia e renal remetem ao rim. Grego e latim ajudam a reconhecer equivalência, mas não predizem sozinhos a área clínica.",
    },
    1784288560133: {
        "Text": "<b>Etimologia.</b> O termo néfron é cunhagem moderna: junta nefr- à desinência grega neutra {{c1::-on}}.",
        "Extra": "Em néfron, -on é desinência grega neutra; não significa “unidade”. O card testa forma histórica, não fisiologia renal.",
    },
}


def main() -> int:
    before = call("notesInfo", notes=list(FIXES))
    absent = set(FIXES) - {n["noteId"] for n in before}
    if absent:
        raise RuntimeError(f"notas legadas ausentes: {sorted(absent)}")
    actions = [{"action": "updateNoteFields", "params": {"note": {
        "id": note_id, "fields": fields}}} for note_id, fields in FIXES.items()]
    result = call("multi", actions=actions)
    failures = [item for item in result if isinstance(item, dict) and item.get("error")]
    if failures:
        raise RuntimeError(f"falha ao refinar notas legadas: {failures[:3]}")
    after = {n["noteId"]: n for n in call("notesInfo", notes=list(FIXES))}
    for note_id, fields in FIXES.items():
        for field, value in fields.items():
            if after[note_id]["fields"][field]["value"] != value:
                raise RuntimeError(f"campo não confirmado: {note_id}/{field}")
    print(f"OK: {len(FIXES)} notas legadas refinadas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
