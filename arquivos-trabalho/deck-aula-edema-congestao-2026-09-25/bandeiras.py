"""Ajuste pequeno 1 (25/09, aprovado por Davi): cor nos 20 cards sem bandeira do deck de Edema.

Só flags; nenhum campo, card ou agendamento muda. Uso: python bandeiras.py check|apply
"""
import json, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from anki import call

ROOT = Path(__file__).resolve().parent
LOCK = ROOT.parent / "ANKI-ESCRITA.lock"
DECK = '"deck:NEBLI::UC03::P2::Patologia::Edema e congestão"'
sys.stdout.reconfigure(encoding="utf-8")

# card_id: (flag, motivo)  — verde 3 = manter a longo prazo; azul 4 = aprender agora, esquecer custa pouco
PLAN = {
    1790264438478: (3, "Único card do mecanismo de obstrução linfática (slide 7)."),
    1790264438575: (3, "Distinção central no pulmão: pressão hidrostática × permeabilidade; cobrada em prova."),
    1790347331933: (3, "Relação desequilíbrio de forças → transudato; basta um card para ela."),
    1790347332125: (3, "Definição de edema (interstício/serosa, não intracelular): base do capítulo."),
    1790347332176: (3, "Hiperemia ativa: metade da distinção central hiperemia × congestão."),
    1790347332210: (3, "Congestão passiva: outra metade da distinção central."),
    1790347332282: (3, "Forças de Starling: pressão hidrostática → filtração; base de todos os mecanismos."),
    1790347332366: (3, "IC → SRAA → retenção de sódio e água (slide 8); lógica que reaparece em nefrótica e cirrose."),
    1790347332525: (3, "Sinal do cacifo: correspondente físico do edema, de uso permanente."),
    1790347332590: (3, "Hemossiderina nos macrófagos: marca morfológica da congestão pulmonar crônica."),
    1790347332620: (3, "Fígado em noz-moscada: marca morfológica da congestão hepática crônica (slide 12)."),
    1790264438391: (4, "Mesma informação do verde 1790347332064 (IR → retenção de Na/H₂O); par a decidir."),
    1790347331932: (4, "Repete o verde 'venous outflow → ↑ hidrostática' no contexto de derrame."),
    1790347331971: (4, "Repete o verde 'perda de albumina → ↓ oncótica' no contexto de derrame."),
    1790347331970: (4, "Mesma resposta (transudato) do verde 1790347331933; par a decidir."),
    1790347332095: (4, "Congestão hepática = IC direita já coberta por noz-moscada e IC direita."),
    1790347332338: (4, "Repete o verde 'venous outflow → ↑ hidrostática'; acrescenta só o edema local."),
    1790347332462: (4, "Nome da coleção (como hidrotórax/hidropericárdio/anasarca, já azuis)."),
    1790347332554: (4, "Detalhe morfológico da congestão aguda, reconstruível pela definição de congestão."),
    1790347332661: (4, "Mesma informação do verde 1790347331873 (IC esquerda → pulmão); par a decidir."),
}

def now(): return datetime.now(timezone.utc).isoformat()

def check():
    issues = []
    if LOCK.exists(): issues.append(f"lock existente: {LOCK.read_text(encoding='utf-8')}")
    cards = {c["cardId"]: c for c in call("cardsInfo", cards=call("findCards", query=DECK))}
    if len(cards) != 36: issues.append(f"deck tem {len(cards)} cards")
    for cid in PLAN:
        if cid not in cards: issues.append(f"card ausente {cid}")
        elif cards[cid]["flags"] != 0: issues.append(f"card {cid} já tem bandeira {cards[cid]['flags']} (não sobrescrever)")
    return issues, cards

def apply():
    issues, cards = check()
    if issues: sys.exit("\n".join(issues))
    LOCK.open("x", encoding="utf-8").write(json.dumps({"executor": "Claude", "aula": "edema-bandeiras", "at": now()}))
    try:
        before = {cid: c["flags"] for cid, c in cards.items()}
        (ROOT / "bandeiras-before.json").write_text(json.dumps(before), encoding="utf-8")
        for cid, (flag, motivo) in PLAN.items():
            call("setSpecificValueOfCard", card=cid, keys=["flags"], newValues=[flag], warning_check=True)
            with (ROOT / "bandeiras-journal.jsonl").open("a", encoding="utf-8") as f:
                f.write(json.dumps({"at": now(), "card": cid, "flag": flag, "motivo": motivo}, ensure_ascii=False) + "\n")
        after = {c["cardId"]: c for c in call("cardsInfo", cards=call("findCards", query=DECK))}
        wrong = [cid for cid, (flag, _) in PLAN.items() if after[cid]["flags"] != flag]
        others = [cid for cid in before if cid not in PLAN and after[cid]["flags"] != before[cid]]
        fields_same = all(after[cid]["fields"] == cards[cid]["fields"] and after[cid]["due"] == cards[cid]["due"] for cid in before)
        receipt = {"at": now(), "flags": dict(Counter(c["flags"] for c in after.values())), "wrong": wrong,
                   "others_changed": others, "fields_and_due_unchanged": fields_same}
        (ROOT / "bandeiras-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=1), encoding="utf-8")
        if wrong or others or not fields_same: raise RuntimeError(receipt)
        call("sync")
        print(json.dumps(receipt, ensure_ascii=False))
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    if (sys.argv[1:] or ["check"])[0] == "apply": apply()
    else:
        i, _ = check(); print("\n".join(i) if i else f"check OK — {sum(1 for f,_ in PLAN.values() if f==3)} verdes, {sum(1 for f,_ in PLAN.values() if f==4)} azuis")
