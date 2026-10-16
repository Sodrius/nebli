"""NEBLI — explicação do card com Tab (Anki desktop).

No verso do card, Tab mostra num balão flutuante a explicação daquele card; Tab de novo
fecha o balão. X marca/desmarca "gostei" para o card como um todo, com ou sem o balão aberto.
Outra tecla só fecha (a tecla de resposta responde na mesma hora). Uma explicação por
card (irmãos de cloze têm a sua), lida de user_files/explicacoes.sqlite, que é
gerada fora do Anki por `python -m nebli.explicacoes gerar`. Nada vai para a coleção.
Cada abertura e cada "gostei" é anotado em user_files/tab-log.jsonl.

Não mexe em nenhuma outra tecla. Guia: GUIA-EXPLICACOES-TAB.md na raiz do NEBLI.
Instalar/atualizar: python -m nebli.explicacoes instalar (reiniciar o Anki depois).
"""
import hashlib
import html
import json
import sqlite3
import time
import traceback
from pathlib import Path

from aqt import gui_hooks, mw
from aqt.qt import QApplication, QEvent, QObject, Qt, QTimer

USER = Path(__file__).resolve().parent / "user_files"
STORE = USER / "explicacoes.sqlite"
LABELS = ("Básico:", "Explicação:", "Na aula:", "Não confundir:",
          "Base:", "Por quê:", "Mais a fundo:", "Liga com:")
# Balão flutuante na parte de baixo da tela, por cima do card, fonte grande.
POPUP_JS = """(function(body){
  var old = document.getElementById('nebli-tab'); if (old) old.remove();
  var night = document.body.classList.contains('nightMode') || document.documentElement.classList.contains('night-mode');
  var d = document.createElement('div'); d.id = 'nebli-tab'; d.innerHTML = body;
  d.style.cssText = 'position:fixed;left:50%;bottom:22px;transform:translateX(-50%);z-index:99999;'
    + 'width:min(960px,94vw);max-height:66vh;overflow-y:auto;box-sizing:border-box;padding:18px 24px;'
    + 'border-radius:14px;text-align:left;font:21px/1.6 -apple-system,system-ui,sans-serif;'
    + 'box-shadow:0 10px 32px rgba(0,0,0,.3);'
    + (night ? 'background:#26282c;color:#e8e8e8;border:1px solid #3a3d42;'
             : 'background:#fffdf7;color:#1f2328;border:1px solid #e3dccb;');
  d.setAttribute('role', 'note'); d.setAttribute('aria-label', 'Explicação do card');
  document.body.appendChild(d);
})(__BODY__);"""
_popup = {"open": False, "card": None, "nota": None, "deck": None,
          "achou": False, "explicacao": None}


def _tab_event(event, **details):
    USER.mkdir(exist_ok=True)
    record = {"em": time.strftime("%Y-%m-%d %H:%M:%S"), "evento": event, **details}
    with (USER / "tab-log.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def _log(message):
    USER.mkdir(exist_ok=True)
    with (USER / "log.txt").open("a", encoding="utf-8") as handle:
        handle.write(time.strftime("%Y-%m-%d %H:%M:%S ") + message + "\n")


def _reviewer():
    reviewer = getattr(mw, "reviewer", None)
    return reviewer if mw.state == "review" and reviewer and reviewer.card else None


def _card_hash(card):
    return hashlib.sha1(("\x1f".join(card.note().fields) + f"\x1e{card.ord}").encode("utf-8")).hexdigest()


def _lookup(card):
    if not STORE.exists():
        return None
    db = sqlite3.connect(f"file:{STORE}?mode=ro", uri=True)
    try:
        return db.execute("select status, texto, motivo, hash from explicacoes where card_id=?",
                          (card.id,)).fetchone()
    finally:
        db.close()


def _render(row, card):
    if not row:
        return "<i>Ainda sem explicação para este card.</i>", False
    status, text, reason, digest = row
    if status != "ok":
        return f"<i>Card marcado para revisão:</i> {html.escape(reason or '')}", True
    lines = []
    for line in html.escape(text or "", quote=False).splitlines():
        for label in LABELS:
            if line.startswith(label):
                line = f"<b>{label}</b>{line[len(label):]}"
        lines.append(line)
    body = "<br>".join(lines)
    if digest != _card_hash(card):
        body += "<div style='margin-top:6px;font-size:12px;opacity:.6'>O card mudou depois desta explicação.</div>"
    return body, True


def _close_popup(*_args):
    """Remove sempre (barato), mesmo se o card já mudou antes do fechamento agendado."""
    _popup["open"] = False
    _popup["card"] = None
    _popup["nota"] = None
    _popup["deck"] = None
    _popup["explicacao"] = None
    reviewer = getattr(mw, "reviewer", None)
    if reviewer and reviewer.web:
        reviewer.web.eval("var n=document.getElementById('nebli-tab'); if(n) n.remove();")


def _is_liked(cid):
    path = USER / "tab-log.jsonl"
    marked = False
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("card") == cid and event.get("evento") in ("card_gostei", "card_gostei_desfeito"):
                marked = event["evento"] == "card_gostei"
    return marked


def _show_like_state():
    reviewer = _reviewer()
    if reviewer:
        label = "Gostei deste card · X desfaz" if _popup.get("gostei") else "X marca gostei neste card"
        reviewer.web.eval("(function(){var n=document.getElementById('nebli-tab');if(!n)return;"
                          "var s=document.getElementById('nebli-tab-status');"
                          "if(!s){s=document.createElement('div');s.id='nebli-tab-status';"
                          "s.style.cssText='font-size:13px;margin-top:10px';n.appendChild(s);}"
                          "s.textContent=" + json.dumps(label) + ";})();")


def _toggle_like():
    reviewer = _reviewer()
    if reviewer and reviewer.card:
        card = reviewer.card
        liked = not _is_liked(card.id)
        _tab_event("card_gostei" if liked else "card_gostei_desfeito",
                   card=card.id, nota=card.nid, deck=card.did,
                   card_hash=_card_hash(card))
        from aqt.utils import tooltip
        if _popup["open"] and _popup["card"] == card.id:
            _popup["gostei"] = liked
            _show_like_state()
        tooltip("Gostei registrado para este card." if liked else "Gostei removido deste card.")


def _toggle():
    try:
        reviewer = _reviewer()
        if not reviewer or reviewer.state != "answer":
            return
        if _popup["open"]:
            _close_popup()
            return
        card = reviewer.card
        row = _lookup(card)
        body, found = _render(row, card)
        reviewer.web.eval(POPUP_JS.replace("__BODY__", json.dumps(body)))
        _popup["open"] = True
        _popup["card"] = card.id
        _popup["nota"] = card.nid
        _popup["deck"] = card.did
        _popup["achou"] = found
        _popup["explicacao"] = hashlib.sha256((row[1] or "").encode("utf-8")).hexdigest()[:16] if row else None
        _popup["gostei"] = _is_liked(card.id)
        _show_like_state()
        _tab_event("abriu", card=card.id, nota=card.nid, deck=card.did,
                   achou=found, explicacao=_popup["explicacao"])
    except Exception:
        _log(traceback.format_exc())


class _TabKey(QObject):
    def eventFilter(self, obj, event):
        if event.type() != QEvent.Type.KeyPress or event.isAutoRepeat():
            return False
        active = QApplication.activeWindow() is mw and _reviewer()
        if active and event.key() == Qt.Key.Key_X and not event.modifiers():
            _toggle_like()
            return True
        if event.key() == Qt.Key.Key_Tab and not event.modifiers() and active:
            QTimer.singleShot(0, _toggle)
            return True  # Tab não passa adiante (no Anki ele só mudaria o foco)
        if _popup["open"]:
            QTimer.singleShot(0, _close_popup)  # qualquer tecla fecha; a tecla segue valendo
        return False


_tab = _TabKey()
QApplication.instance().installEventFilter(_tab)
gui_hooks.reviewer_did_show_question.append(_close_popup)
gui_hooks.reviewer_did_show_answer.append(_close_popup)
_log("carregado")
