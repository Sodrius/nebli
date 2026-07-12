"""nebli_flag_suspender — Ctrl+1 = bandeira vermelha (flag:1) + suspender card.

Conserto 2026-07-12: a versão antiga registrava um QShortcut GLOBAL para Ctrl+1,
que conflitava com o Ctrl+1 NATIVO do Anki (já é bandeira vermelha) → Qt tratava o
atalho como ambíguo e não disparava nenhum ("não pegava"). Agora nós SUBSTITUÍMOS o
callback nativo do Ctrl+1 no reviewer (monkeypatch de Reviewer._shortcutKeys), então
não há competição: uma tecla, uma ação = marcar vermelho + suspender + avançar.

Instalar: copiar esta pasta para
  Windows: %APPDATA%\\Anki2\\addons21\\nebli_flag_suspender\\
  Linux/Mac: ~/.local/share/Anki2/addons21/nebli_flag_suspender/
e reiniciar o Anki. (No Anki do Docker, copiar para a pasta addons21 do container.)

Uso: durante a revisão, Ctrl+1 marca o card com bandeira vermelha E o suspende; ele
some da fila até você rodar `monitor_email_anking.py --bandeira`, que explica e devolve.
"""
from aqt import mw
from aqt.reviewer import Reviewer


def _flag_vermelha_e_suspender():
    if mw.state != "review":
        return
    reviewer = getattr(mw, "reviewer", None)
    if not reviewer or not reviewer.card:
        return
    cid = reviewer.card.id
    # bandeira vermelha (flag:1) — API de coleção, Anki 2.1.45+
    try:
        mw.col.set_user_flag_for_cards(1, [cid])
    except AttributeError:
        reviewer.card.set_user_flag(1)
        reviewer.card.flush()
    # suspende (sai da fila até o --bandeira devolver)
    mw.col.sched.suspend_cards([cid])
    # avança sem mostrar a resposta
    reviewer.nextCard()


# Substitui o callback do Ctrl+1 no reviewer (não adiciona um concorrente).
_orig_shortcut_keys = Reviewer._shortcutKeys


def _shortcut_keys(self):
    keys = _orig_shortcut_keys(self)
    out = []
    for entry in keys:
        # entradas são tuplas (tecla, callback); as de flag usam "Ctrl+1".."Ctrl+4"
        if isinstance(entry, tuple) and len(entry) >= 2 and entry[0] == "Ctrl+1":
            out.append(("Ctrl+1", _flag_vermelha_e_suspender))
        else:
            out.append(entry)
    # se por algum motivo o Ctrl+1 nativo não existir nesta versão, adiciona o nosso
    if not any(isinstance(e, tuple) and e and e[0] == "Ctrl+1" for e in out):
        out.append(("Ctrl+1", _flag_vermelha_e_suspender))
    return out


Reviewer._shortcutKeys = _shortcut_keys
