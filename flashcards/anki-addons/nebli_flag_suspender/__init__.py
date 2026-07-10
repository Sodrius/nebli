"""nebli_flag_suspender — Ctrl+1 = bandeira vermelha (flag:1) + suspender card.

Instalar: copiar esta pasta para ~/.local/share/Anki2/addons21/ (Linux/Mac)
          ou %APPDATA%\Anki2\addons21\ (Windows) e reiniciar o Anki.

Uso durante o estudo:
  Ctrl+1  →  marca o card atual com bandeira vermelha (flag:1) E o suspende.
             O card some da fila de revisão até você rodar --bandeira.
             Depois de ler a explicação no email, o card volta automaticamente.
"""
from aqt import mw, gui_hooks
from aqt.qt import QKeySequence, QShortcut


def _flag_e_suspender():
    if mw.state != "review":
        return
    reviewer = getattr(mw, "reviewer", None)
    if not reviewer or not reviewer.card:
        return
    card = reviewer.card
    cid = card.id
    # Seta bandeira vermelha (flag:1) — API compatível com Anki 2.1.50+
    try:
        mw.col.set_user_flag_for_cards(1, [cid])
    except AttributeError:
        # Anki < 2.1.50: API legada (card-level)
        card.set_user_flag(1)
        card.flush()
    # Suspende o card da fila (sai até email --bandeira o devolver)
    mw.col.sched.suspend_cards([cid])
    # Avança para o próximo card sem mostrar a resposta
    reviewer.nextCard()


def _ativar():
    atalho = QShortcut(QKeySequence("Ctrl+1"), mw)
    atalho.activated.connect(_flag_e_suspender)


gui_hooks.main_window_did_init.append(_ativar)
