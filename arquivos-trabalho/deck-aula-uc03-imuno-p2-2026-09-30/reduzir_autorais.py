"""Reduz os autorais da Imuno P2 (pedido de Davi, 30/09: "sinto que ficou muitos cards de imuno autorais,
ajeita isso"). Só remove autorais NÃO estudados cujo alvo é detalhe ou já está coberto por AnKing/associado;
troca o autoral MBL/MASP pelo AnKing 1487640175721. Snapshot antes, lock nebli.decks.escrita, readback.
Uso: python3 reduzir_autorais.py [--aplicar]   (sem --aplicar só mostra o plano)
"""
import json, re, sys
from datetime import datetime
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita

COMP = "NEBLI::2026-uc03-imunologia-31-sistema-complemento"
DECK = "NEBLI::UC03::P2::Imunologia::Sistema complemento"
BAD_IMG = "8f4ce0ed345e5153fbff4de0c723fa52.webp"  # esquema de complemento com erro (media-corrections)
RESOURCE = {"Sketchy", "Sketchy 2", "Sketchy Extra", "Bootcamp", "Pixorize", "Physeo", "OME", "Picmonic",
            "Additional Resources", "Boards and Beyond", "Pathoma", "First Aid", "ankihub_id", "One by one"}

# nid -> (alvo, onde o alvo continua coberto)
REMOVER = {
    1790781880318: ("C3a/C3b da clivagem de C3", "AnKing: C3 convertase converte C3 em C3a e C3b; anafilatoxinas; opsoninas (associado)"),
    1790781880793: ("C1r ativa C1s", "detalhe; AnKing: via clássica começa em C1"),
    1790781881393: ("MBL ~ C1q, MASPs", "trocado pelo AnKing 1487640175721 (via das lectinas começa em complexo tipo C1)"),
    1790781883117: ("ácido siálico e fator H", "detalhe; AnKing: proteína M sequestra fator H; autoral fator I/H"),
    1790781885393: ("CD59 impede polimerização de C9", "AnKing: DAF e MIRL/CD59 por GPI; ausência → lise"),
    1790781885493: ("C3d + CR2 no linfócito B", "AnKing: CD21 é receptor de C3d (Extra explica correceptor)"),
    1790781885593: ("deficiência de MBL", "detalhe; AnKing: via das lectinas por manose"),
    1790806713995: ("hidrólise espontânea de C3", "AnKing: via alternativa espontânea, começa em C3"),
    1790806714143: ("fator D cliva fator B", "detalhe; fator D aparece no autoral de interpretação do AH50"),
    1790806714292: ("properdina estabiliza C3bBb", "detalhe; properdina aparece no autoral de interpretação do AH50"),
    1790806714567: ("CR1 eritrocitário transporta imunocomplexos", "AnKing: C3b remove imunocomplexos"),
    1790806714718: ("CR3 liga iC3b", "detalhe; AnKing: C3b e IgG são opsoninas (associado)"),
    1790781920089: ("bloquear IL-1 na gota", "autoral urato→NLRP3→IL-1β + AnKing inflamassoma→IL-1β"),
    1790781920189: ("sequência vascular inicial", "AnKing associados: vênulas pós-capilares, edema por contração endotelial"),
    1790781920314: ("monócitos após neutrófilos", "AnKing associado: macrófagos predominam após neutrófilos"),
    1790781920414: ("eotaxina recruta eosinófilos", "detalhe; AnKing associado: quimiotáticos de neutrófilo"),
    1790781920756: ("histamina pré-formada × PG/LT sintetizados", "AnKing: resposta imediata = histamina pré-formada; tardia = mediadores novos"),
    1790781920992: ("eferocitose", "AnKing: neutrófilos diminuem por apoptose; explicação do Tab cobre eferocitose"),
}
ADICIONAR_SRC = 1487640175721


def main(apply):
    A = Anki()
    notes = A("notesInfo", notes=list(REMOVER))
    problems = []
    for n in notes:
        if not n:
            problems.append("nota ausente"); continue
        if "NEBLI::origem::Autoral" not in n["tags"]:
            problems.append(f"{n['noteId']} não é autoral")
        cards = A("cardsInfo", cards=n["cards"])
        if any(c.get("reps", 0) for c in cards):
            problems.append(f"{n['noteId']} já foi estudado")
        if any(c["flags"] not in (3, 4) for c in cards):
            problems.append(f"{n['noteId']} tem marca pessoal")
    src = A("notesInfo", notes=[ADICIONAR_SRC])[0]
    if A("findNotes", query=f'"tag:NEBLI::source::nid-{ADICIONAR_SRC}"'):
        problems.append("cópia do AnKing já existe")
    n_cards = sum(len(n["cards"]) for n in notes if n)
    print(f"Remover {len(notes)} notas autorais / {n_cards} cards; adicionar 1 AnKing ({ADICIONAR_SRC}).")
    print("Problemas:", problems or "nenhum")
    if problems or not apply:
        return
    fields = {k: ("" if k in RESOURCE else v["value"]) for k, v in src["fields"].items()}
    fields["Extra"] = re.sub(rf'<img[^>]*{re.escape(BAD_IMG)}[^>]*>', "", fields.get("Extra", ""))
    target_fields = A("modelFieldNames", modelName="NEBLI AnKing independente - v3")
    fields = {k: fields.get(k, "") for k in target_fields}
    tags = sorted(set(src["tags"]) | {COMP, "NEBLI::escopo::aula", "NEBLI::objetivo::B-vias", "NEBLI::origem::AnKing",
                                      f"NEBLI::source::nid-{ADICIONAR_SRC}", "NEBLI::run::uc03-imuno-reducao-20260930"})
    snap = HERE / f"reducao-autorais-before-{datetime.now():%H%M%S}.json"
    snap.write_text(json.dumps({"remover": {str(k): v for k, v in REMOVER.items()}, "notas": notes,
                                "cards": [A("cardsInfo", cards=n["cards"]) for n in notes]}, ensure_ascii=False, indent=1))
    with escrita(A, "Imuno P2: redução de autorais"):
        nid = A("addNote", note={"deckName": DECK, "modelName": "NEBLI AnKing independente - v3", "fields": fields,
                                 "tags": tags, "options": {"allowDuplicate": True}})
        new_cards = A("findCards", query=f"nid:{nid}")
        for cid in new_cards:
            A("setSpecificValueOfCard", card=cid, keys=["flags"], newValues=[4], warning_check=True)
        A("deleteNotes", notes=list(REMOVER))
    left = A("notesInfo", notes=list(REMOVER))
    readback = {"adicionada": nid, "cards_novos": new_cards,
                "flags_novos": [c["flags"] for c in A("cardsInfo", cards=new_cards)],
                "removidas_ainda_vivas": [n["noteId"] for n in left if n]}
    (HERE / "reducao-autorais-receipt.json").write_text(json.dumps(readback, ensure_ascii=False, indent=1))
    print(readback)


if __name__ == "__main__":
    main("--aplicar" in sys.argv)
