"""Auditoria de cobertura em dois sentidos para corridas de deck-aula v13+.

Usa a compreensão e a revisão final que já pertencem à corrida. Não cria
planilha paralela: cada relação de `aprender` aponta os cards que a fazem
recuperar, e `cards_conferidos` cobre o plano inteiro no sentido inverso.
"""


def problemas(compreensao, plan):
    blocos = [b for b in compreensao.get("blocos", []) if isinstance(b, dict)]
    fidelidade = (compreensao.get("fidelidade") or {}).get("blocos") or []
    chaves = {e["key"] for e in plan.get("entries", [])}
    chaves |= {f"sh-{k}" for k in (plan.get("compartilhados") or {})}
    erros = []
    conferidos = set()
    por_laminas = {}
    for f in fidelidade:
        if not isinstance(f, dict):
            continue
        lam = tuple(f.get("laminas") or [])
        if lam in por_laminas:
            erros.append(f"bloco {lam}: revisão duplicada")
        por_laminas[lam] = f
        cards = f.get("cards_conferidos") or []
        if not isinstance(cards, list) or not all(isinstance(c, str) for c in cards):
            erros.append(f"bloco {lam}: cards_conferidos precisa conter chaves textuais")
            cards = []
        conferidos.update(cards)
        desconhecidos = set(cards) - chaves
        if desconhecidos:
            erros.append(f"bloco {lam}: cards_conferidos fora do plano {sorted(desconhecidos)[:3]}")

    for b in blocos:
        if b.get("papel") not in ("principio", "exemplo"):
            continue
        lam = tuple(b.get("laminas") or [])
        f = por_laminas.get(lam) or {}
        aprender = b.get("aprender") or []
        relacoes = f.get("relacoes") or []
        if not isinstance(aprender, list) or not all(isinstance(x, str) for x in aprender):
            erros.append(f"bloco {lam}: aprender precisa conter frases textuais")
            continue
        if not isinstance(relacoes, list):
            erros.append(f"bloco {lam}: relacoes precisa ser lista")
            continue
        textos = [r.get("aprender") for r in relacoes if isinstance(r, dict)]
        if len(textos) != len(set(textos)):
            erros.append(f"bloco {lam}: relação repetida")
        if set(textos) != set(aprender):
            erros.append(f"bloco {lam}: cada item de aprender precisa de uma relação exata")
        for r in relacoes:
            if not isinstance(r, dict):
                erros.append(f"bloco {lam}: relação sem campos")
                continue
            cards = r.get("cards") or []
            if not isinstance(cards, list) or not all(isinstance(c, str) for c in cards):
                erros.append(f"bloco {lam}: cards da relação precisam ser chaves textuais")
                continue
            if r.get("estado") != "recuperavel" or not cards or not set(cards) <= chaves:
                erros.append(f"bloco {lam}: {str(r.get('aprender', ''))[:45]} não recuperável em cards válidos")
            if not set(cards) <= set(f.get("cards_conferidos") or []):
                erros.append(f"bloco {lam}: relação aponta card não conferido no bloco")

    faltam = chaves - conferidos
    if faltam:
        erros.append(f"cards sem conferência no sentido cards → aula: {sorted(faltam)[:5]}")
    return erros
