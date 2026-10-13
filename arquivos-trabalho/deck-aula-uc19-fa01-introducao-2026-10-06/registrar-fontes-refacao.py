"""Registra as fontes efetivamente confrontadas com a seleção revisada."""
from pathlib import Path
import hashlib
import json

here = Path(__file__).resolve().parent
inventory = json.loads((here / "inventario-aula.json").read_text())
items = [i for s in inventory["slides"] for i in s["itens"]] + inventory["exercicios"]
ids = [i["id"] for i in items]
plan = {
    "fontes": {k: {"estado": "consultada", "contribuicao": v} for k, v in {
        "slides": "sequência de 69 lâminas, inventário atômico e exemplos",
        "bibliografia": "Rang & Dale capítulo 2: alvos, agonismo, curvas, antagonismo e adaptação",
        "youtube": "Ninja Nerd calibrado contra Rang; Dirty e Professor Dave para ponte PK/PD",
        "veteranos": "DeNucci, introdução à relação concentração–efeito e formulação",
        "provas": "antagonismo fisiológico e indução enzimática como transferência",
        "exercicios": "objetivos e perguntas de farmacodinâmica da UC19",
    }.items()} | {"caoc": {"estado": "inacessível", "contribuicao": "pasta CAOC retorna 404; não usada como fonte"}},
    "alvos": [{"id": i["id"], "slide": (i["fonte"] if i["id"].startswith(("obj", "ex")) else f"Slide {int(i['id'][1:3])}"),
               "alvo": i["alvo"], "fontes": i.get("fontes", [i.get("fonte", "Slides")]),
               "origem_prevista": "AnKing primeiro; autoral apenas lacuna conceitual"} for i in items],
}
(here / "planejamento.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2))

def evidence(family, path, loc, contribution, targets, **extra):
    data = (here / path).read_bytes()
    return {"estado": "consultada", "arquivo": path, "sha256": hashlib.sha256(data).hexdigest(),
            "leitura": "integral", "localizador": loc, "contribuicao": contribution,
            "lida_antes_da_selecao": True, "alvos": targets, **extra}

youtube = [
    ("Ninja Nerd", "https://www.youtube.com/watch?v=JDpg2tdHdq0", "fontes/ninja-pharmacodynamics.txt", "Agonismo, antagonismo, curvas e índice terapêutico; corrigidas simplificações pelo Rang", ["s39-03", "s54-03", "s60-01"]),
    ("Dirty Medicine", "https://www.youtube.com/watch?v=GvZq67dcHXs", "fontes/dirty-pharmaco.txt", "Ponte entre farmacocinética e farmacodinâmica; cálculos de cinética fora do escopo", ["s21-01", "s22-01"]),
    ("Professor Dave", "https://www.youtube.com/watch?v=PGzT3cTPah8", "fontes/dave-pharmacodynamics.txt", "Alvo e curvas; equivalência incorreta entre afinidade e potência rejeitada", ["s39-01", "s39-03"]),
]
channels = [{"canal": c, "url": u, "transcricao": p, "lido": "integral", "calibracao": co} for c,u,p,co,_ in youtube]
ev = {
    "slides": [evidence("slides", "fontes/slides.pdf", "PDF 1–69; folhas visuais 1–69 e inventário s01–s69", "Define ordem, objetivos e exemplos; história reduzida por pedido expresso", ["s25-01", "s39-01", "s54-03", "s67-01"])],
    "bibliografia": [evidence("bibliografia", "fontes/rang-cap2.txt", "Rang & Dale 7ª ed., cap. 2, PDF 34–45", "Corrige afinidade/potência, agonismo parcial/inverso, antagonismos, reserva e tolerância", ["s39-01", "s42-02", "s54-05", "s51-03"])],
    "youtube": [evidence("youtube", p, "transcrição integral do vídeo", co, t, canal=c, url=u) for c,u,p,co,t in youtube],
    "veteranos": [evidence("veteranos", "fontes/denucci-introducao.txt", "DeNucci, PDF 3–5, seção Introdução", "Delimita PK, PD, medicamento e relação concentração–efeito; cinética quantitativa excluída", ["s18-01", "s21-01", "s22-01"])],
    "provas": [evidence("provas", "fontes/prova-farmacodinamica.txt", "Todas as questões, PDF 25–26 e 84–85", "Insulina/glucagon e indução de CYP como antagonismos distintos", ["ex-06", "ex-07"])],
    "exercicios": [evidence("exercicios", "fontes/Objetivos cognitivos e exemplos de questoes avaliacao UC19 - FMUSP exclusivo.txt", "Objetivos PDF 1–2; questões PDF 7; texto integral 9 páginas", "Confirma definições, alvos, agonistas, antagonistas, curvas e dessensibilização", ["obj-01", "obj-02", "ex-01", "ex-03"])],
    "caoc": [{"estado": "inacessível", "essencial": False, "busca": "Pasta CAOC 10URthATN63lr0GSxN9ekgQrGJ1abzxNn retornou 404; fontes da UC19 no Drive pessoal disponíveis", "impacto": "Sem contribuição CAOC; slides, Rang, questões e objetivos docentes disponíveis"}],
}
sources = {
    "nome": "Introdução à Farmacologia e mecanismos de ação dos fármacos",
    "escopo": "cards", "drive_pasta": "UC19/Farmacologia/P1 - Introdução à Farmacologia e mecanismos de ação dos fármacos",
    "slides": {"arquivo": "fontes/slides.pdf", "todas_vistas": True},
    "livros": [{"livro": "Rang & Dale, Farmacologia, 7ª ed., capítulo 2", "texto": "fontes/rang-cap2.txt", "lido": True}],
    "canais": channels,
    "provas": {"estado": "consultada", "contribuicao": "Questões PDF 25–26 e 84–85"},
    "exercicios": {"estado": "consultada", "contribuicao": "Objetivos cognitivos e exercícios PDF 1–9"},
    "veteranos": {"estado": "consultada", "contribuicao": "DeNucci PDF 3–5; ponte PK/PD"},
    "caoc": {"estado": "inacessível", "busca": "CAOC 10URthATN63lr0GSxN9ekgQrGJ1abzxNn retornou 404", "contribuicao": "Nenhuma"},
    "evidencias": ev,
}
(here / "fontes.json").write_text(json.dumps(sources, ensure_ascii=False, indent=2))
print(len(ids), "alvos;", sum(len(x) for x in ev.values()), "registros de evidência")
