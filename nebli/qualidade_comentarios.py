"""Regressões da rodada diária: forma mecânica, não julgamento didático."""
import re


def sigla_curta(resposta):
    return bool(re.fullmatch(r'(?:[A-Z][A-Z0-9/-]{1,6}|Ig[AGEMD](?:/Ig[AGEMD])?)', resposta.strip()))


def preferencia_sem_iniciais(e):
    """Exceção local precisa citar a escolha literal; não basta um booleano."""
    return len(str(e.get('dicas_preferencia_davi', '')).strip()) >= 30


def negrito_contexto(texto):
    """Organizador: cada linha com alvo precisa ter destaque visível fora dele."""
    if 'data-nebli-organizacao' not in texto or '<table' in texto:
        return []
    ruins = []
    for i, linha in enumerate(re.split(r'<br\s*/?>|</li>', texto, flags=re.I), 1):
        if not re.search(r'\{\{c\d+::', linha):
            continue
        visivel = re.sub(r'\{\{c\d+::.*?\}\}', '', linha, flags=re.S)
        if not re.search(r'<(?:b|strong)\b[^>]*>\s*[^<\s]', visivel, re.I):
            ruins.append(i)
    return ruins


def step2_only(notas):
    """Only_Step_2 é classificação explícita; uma tag Step2 compartilhada não basta."""
    return [n['noteId'] for n in notas
            if '#AK_Other::Only_Step_2' in n.get('tags', [])]


def badge_layout_ok(metrics):
    """Não aprova no vazio nem aceita coração fora da tela ou sobre a bandeira."""
    if not metrics or not metrics.get('encontrado') or not metrics.get('coracao_visivel'):
        return False
    if metrics.get('bandeira_visivel'):
        gap = metrics.get('gap')
        return isinstance(gap, (int, float)) and gap >= 11.5
    return True
