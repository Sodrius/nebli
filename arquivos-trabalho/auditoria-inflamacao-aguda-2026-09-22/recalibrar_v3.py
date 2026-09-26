"""Recalibra o piloto de inflamação após feedback do estudante.

Escopo desta correção: mantém dados e histórico, remove só o rodapé meta
adicionado pela revisão v2 e suspende itens fora da seleção. Bandeira vermelha
é decisão pessoal de revisão, não yield. Não toca no AnKing original.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from inspecionar_v2 import ROOT, call

OUT = ROOT / "revisao-v2"
PLAN = json.loads((OUT / "plan.json").read_text(encoding="utf-8"))
DECK = PLAN["target_deck"]

# O único complemento mantido: lacuna direta do material/prova antiga.
KEEP_LOCAL = {"flegmao"}
EXCLUDE_LOCAL = {
    "finalidade", "edema-funcao", "estase", "contracao-lesao",
    "lesao-leucocitaria", "transcitose", "linfa", "linfonodo",
    "histamina-fontes", "no", "paf", "residentes", "cinética",
    "afinidade", "quimiotaxia-gradiente", "sistemico", "resolucao-lipidica",
    "desfechos", "drenagem", "tabela-local", "fontes-pg-lt",
    "v-ulcera", "v-flegmao", "v-abscesso", "v-marginacao", "v-diapedese",
    "v-fases-pulmao",
}
EXCLUDE_SOURCE_NIDS = {
    # Conteúdo pleural/derrame: não é objetivo desta aula.
    1487981833078, 1487982014218, 1535296447535,
    1474503768203, 1474503771577, 1474503784942,
    # Fármaco de asma: ponte lateral, não conteúdo ensinado aqui.
    1474580780060,
}
META = re.compile(r'<div class="nebli-aula-v2".*?</div>\s*', re.S)
HIGH_YIELD_TAG = "#AK_Step1_v12::#Low/HighYield::1-HighYield"


def key_tag(entry):
    if entry.get("source_nid"):
        return f'NEBLI::source::nid-{entry["source_nid"]}'
    return f'NEBLI::lesson-local::{PLAN["lesson_id"]}::{entry["key"]}'


def selected_entries():
    keep, excluded = [], []
    for entry in PLAN["entries"]:
        is_local = entry["origin"].startswith("NEBLI-")
        excluded_here = (is_local and entry["key"] in EXCLUDE_LOCAL) or (
            entry.get("source_nid") in EXCLUDE_SOURCE_NIDS
        )
        (excluded if excluded_here else keep).append(entry)
    assert {e["key"] for e in keep if e["origin"].startswith("NEBLI-")} == KEEP_LOCAL
    return keep, excluded


def load_current():
    note_ids = call("findNotes", query=f'deck:"{DECK}"')
    notes = call("notesInfo", notes=note_ids)
    cards = call("cardsInfo", cards=[cid for note in notes for cid in note["cards"]])
    return notes, cards


def map_entries(notes):
    by_tag = {}
    for note in notes:
        for tag in note["tags"]:
            by_tag[tag] = note
    absent = [entry["key"] for entry in PLAN["entries"] if key_tag(entry) not in by_tag]
    if absent:
        raise RuntimeError("Notas do plano ausentes: " + ", ".join(absent))
    return by_tag


def snapshot(notes, cards):
    return {
        "at": datetime.now(timezone.utc).isoformat(),
        "deck": DECK,
        "notes": notes,
        "cards": cards,
        "sha256": hashlib.sha256(
            json.dumps({"notes": notes, "cards": cards}, sort_keys=True).encode()
        ).hexdigest(),
    }


def check():
    notes, cards = load_current()
    by_tag = map_entries(notes)
    keep, excluded = selected_entries()
    current = {c["cardId"]: c for c in cards}
    excluded_cards = [cid for entry in excluded for cid in by_tag[key_tag(entry)]["cards"]]
    active_cards = [cid for entry in keep for cid in by_tag[key_tag(entry)]["cards"]]
    hy_cards = [
        cid for entry in keep if HIGH_YIELD_TAG in entry.get("source_tags", [])
        for cid in by_tag[key_tag(entry)]["cards"]
    ]
    meta_notes = [n["noteId"] for n in notes if META.search(n["fields"].get("Extra", {}).get("value", ""))]
    current_flags = {str(i): call("findCards", query=f'deck:"{DECK}" flag:{i}') for i in range(1, 8)}
    return {
        "deck": DECK,
        "notes": len(notes),
        "cards": len(cards),
        "selected_cards": len(active_cards),
        "excluded_cards": len(excluded_cards),
        "selected_keys": [e["key"] for e in keep],
        "excluded_keys": [e["key"] for e in excluded],
        "high_yield_card_ids": hy_cards,
        "meta_notes": meta_notes,
        "current_flags": current_flags,
        "already_suspended": [cid for cid, card in current.items() if card.get("queue") == -1],
    }


def apply():
    before_notes, before_cards = load_current()
    before = snapshot(before_notes, before_cards)
    (OUT / "before-v3.json").write_text(json.dumps(before, ensure_ascii=False, indent=2), encoding="utf-8")
    by_tag = map_entries(before_notes)
    keep, excluded = selected_entries()
    excluded_notes = [by_tag[key_tag(entry)]["noteId"] for entry in excluded]
    excluded_cards = [cid for entry in excluded for cid in by_tag[key_tag(entry)]["cards"]]
    hy_cards = [
        cid for entry in keep if HIGH_YIELD_TAG in entry.get("source_tags", [])
        for cid in by_tag[key_tag(entry)]["cards"]
    ]

    # Remove somente o rodapé criado por nós na v2; explicações originais ficam intactas.
    changed_extras = []
    for note in before_notes:
        extra = note["fields"].get("Extra", {}).get("value", "")
        cleaned = META.sub("", extra).rstrip()
        if cleaned != extra:
            call("updateNoteFields", note={"id": note["noteId"], "fields": {"Extra": cleaned}})
            changed_extras.append(note["noteId"])

    # Reversível: nada é apagado. Tags de prioridade/faculdade adicionadas pela
    # v2 são retiradas para não se passarem por decisão do estudante.
    all_notes = [n["noteId"] for n in before_notes]
    custom_tags = [
        tag for note in before_notes for tag in note["tags"]
        if tag.startswith("NEBLI::IA::")
    ]
    if custom_tags:
        call("removeTags", notes=all_notes, tags=" ".join(sorted(set(custom_tags))))
    if excluded_notes:
        call("addTags", notes=excluded_notes, tags="NEBLI::selection::v3-suspended")
    if excluded_cards:
        call("suspend", cards=excluded_cards)

    # Ajusta o único autoral remanescente para uma pergunta curta, sem comentário meta.
    flegmao = by_tag[key_tag(next(e for e in keep if e["key"] == "flegmao"))]
    call("updateNoteFields", note={"id": flegmao["noteId"], "fields": {
        "Text": "{{c1::Phlegmon}} is diffuse suppurative inflammation spreading through tissue planes; an {{c2::abscess}} is a localized collection of pus.",
        "Extra": "",
    }})

    # Yield é informação de origem: vermelho tem semântica pessoal de
    # revisar/remover/melhorar; esta recalibração não muda bandeiras.
    flags_before = {str(i): call("findCards", query=f'deck:"{DECK}" flag:{i}') for i in range(1, 8)}

    after_notes, after_cards = load_current()
    verified = check()
    suspended_after = {c["cardId"] for c in after_cards if c.get("queue") == -1}
    if verified["meta_notes"]:
        raise RuntimeError("Rodapé meta ainda encontrado")
    if not set(excluded_cards).issubset(suspended_after):
        raise RuntimeError("Nem todos os excluídos foram suspensos")
    if {str(i): call("findCards", query=f'deck:"{DECK}" flag:{i}') for i in range(1, 8)} != flags_before:
        raise RuntimeError("Bandeiras mudaram durante a recalibração")
    if len(after_notes) != len(before_notes) or len(after_cards) != len(before_cards):
        raise RuntimeError("A contagem de notas/cards mudou")
    package = OUT / "Inflamacao aguda.apkg"
    call("exportPackage", deck=DECK, path=str(package.resolve()), includeSched=True)
    receipt = {
        "at": datetime.now(timezone.utc).isoformat(),
        "version": "v3-recalibration",
        "deck": DECK,
        "total_notes": len(after_notes),
        "total_cards": len(after_cards),
        "active_selected_cards": verified["selected_cards"],
        "suspended_out_of_selection_cards": len(excluded_cards),
        "active_imported_cards": verified["selected_cards"] - 2,
        "active_authored_cards": 2,
        "high_yield_source_cards": len(hy_cards),
        "removed_meta_footers": len(changed_extras),
        "removed_system_priority_tags": len(set(custom_tags)),
        "suspended_keys": verified["excluded_keys"],
        "only_authored_active_key": "flegmao",
        "package": str(package.resolve()),
        "package_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
        "original_AnKing_source": "not modified",
    }
    (OUT / "receipt-v3.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("check", "apply"))
    args = parser.parse_args()
    if args.mode == "check":
        print(json.dumps(check(), ensure_ascii=False, indent=2))
    else:
        apply()
