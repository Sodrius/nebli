"""Remove somente as cópias novas e nunca revisadas do lote interrompido."""
import json
from datetime import datetime, timezone

from inventory_vascularizacao import call
from prepare_vascularizacao import LESSON, ROOT


TAG = f"NEBLI::{LESSON}"
ALLOWED_MODELS = {
    "NEBLI AnKing independente - v3",
    "NEBLI Anatomy independente - v1",
    "NEBLI Dope Cloze independente - v1",
    "NEBLI Dorian Cloze independente - v1",
}


def main():
    note_ids = call("findNotes", query=f'tag:"{TAG}"')
    notes = call("notesInfo", notes=note_ids)
    cards = call("cardsInfo", cards=[card for note in notes for card in note["cards"]])
    if len(notes) != 40 or len(cards) != 53:
        raise RuntimeError(f"Lote parcial mudou: {len(notes)} notas, {len(cards)} cards")
    if any(note["modelName"] not in ALLOWED_MODELS for note in notes):
        raise RuntimeError("O lote parcial contém modelo não autorizado.")
    if any(f"NEBLI::source::nid-" not in " ".join(note["tags"]) for note in notes):
        raise RuntimeError("Uma nota não tem identidade de fonte.")
    if any(card["reps"] != 0 for card in cards):
        raise RuntimeError("Há card revisado; exclusão cancelada.")
    snapshot = {
        "at": datetime.now(timezone.utc).isoformat(),
        "reason": "lote interrompido antes da validação por defeito do template Anatomy",
        "notes": notes,
        "cards": cards,
    }
    (ROOT / "failed-batch-before-delete.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    call("deleteNotes", notes=note_ids)
    remaining = call("findNotes", query=f'tag:"{TAG}"')
    if remaining:
        raise RuntimeError(f"Cópias parciais restantes: {remaining}")
    print(json.dumps({"deleted_notes": len(notes), "deleted_cards": len(cards)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
