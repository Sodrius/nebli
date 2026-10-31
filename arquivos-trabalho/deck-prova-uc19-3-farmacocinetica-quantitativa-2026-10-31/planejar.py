"""Planejamento do lote 3 do deck-prova UC19 (Farmacocinética quantitativa), fonte única da E3 em diante (F-20261029-CLAUDE-04).

    /usr/bin/python3 planejar.py      # grava mapa-de-profundidade.json, motivacoes.json, matriz-prova.json, inventario.py, escopo.json

ITENS é o que a prova cobra, tirado das fontes base (objetivos FC item f, apostila aulas 2–3 e exercícios, De Nucci cap. 1, orientadoras FC 1, 8, 31–34, questões do Prof. Gilberto, banco) e
conferido no Rang cap. 10. CARDS (item → chaves do spec) é preenchido depois da busca (E4/E5); a matriz e o mapa saem daqui.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.base_prova import texto_paginas  # noqa: E402

# id: (página da base, tipo, o que Davi tem de saber, fonte, termos que o card precisa conter)
ITENS = {
 "k1": (1, "explicar", "Na primeira ordem o organismo elimina uma fração constante do fármaco por tempo; metabolismo e excreção renal são de primeira ordem longe da saturação.", "objetivos f.i(1a); De Nucci p.4", ["first-order"]),
 "k2": (3, "decorar", "Depois do bolus IV, C = C0·e^(−ke·t); C0 é a concentração extrapolada ao tempo zero, virtual.", "apostila p.16; De Nucci p.3; questão orientadora 32", ["C0"]),
 "k3": (3, "explicar", "No gráfico semilogarítmico a eliminação de primeira ordem é uma reta, de inclinação −ke.", "apostila p.16; De Nucci p.4; questão orientadora 33", ["slope"]),
 "k4": (4, "distinguir", "Depois do bolus, a queda inicial rápida é a fase de distribuição; a reta seguinte é a fase de eliminação.", "objetivos f.i(1a); questão orientadora 31", ["distribution"]),
 "k5": (1, "distinguir", "Curva exponencial (fração constante) é primeira ordem; curva linear (quantidade constante) é ordem zero.", "objetivos f.i(1a) e f.ii(1)", ["exponential"]),
 "h1": (6, "decorar", "t½ = 0,693/ke, e também t½ = 0,693·Vd/Cl.", "De Nucci p.4–5; questão orientadora 34; objetivos f.i(1b)", ["half-life"]),
 "h2": (5, "explicar", "Cada meia-vida elimina metade do que resta: 50, 25, 12,5%; após 5 meias-vidas o fármaco está praticamente eliminado.", "apostila p.16; De Nucci p.4", ["half-lives"]),
 "h3": (6, "e-se", "Com doses repetidas ou infusão, o estado de equilíbrio chega em 4–5 meias-vidas, qualquer que seja a dose.", "apostila p.16; De Nucci p.4; objetivos f.i(3b)", ["steady state"]),
 "h4": (6, "decorar", "Tempo médio de residência (MRT) = AUMC/AUC = 1/ke.", "apostila p.16; De Nucci p.5", ["residence"]),
 "h5": (7, "e-se", "Vd maior ou clearance menor aumentam a meia-vida.", "apostila p.15; banco p.8", ["half-life"]),
 "c1": (7, "decorar", "Vd = quantidade no corpo / C0 (dose IV / concentração inicial).", "apostila p.15; questão orientadora 8", ["volume of distribution"]),
 "c2": (7, "decorar", "Clearance = taxa de eliminação / concentração = ke·Vd.", "apostila p.15; objetivos f.i(1b)", ["clearance"]),
 "c3": (8, "explicar", "Na infusão contínua a concentração sobe até a entrada igualar a saída: R0 = Cl·Css.", "De Nucci p.10; questão orientadora 1; objetivos f.i(3a)", ["infusion"]),
 "c4": (8, "decorar", "Dose de ataque = Cp·Vd/F; enche o volume de distribuição e encurta o tempo até o nível-alvo.", "objetivos f.i(3c)", ["loading dose"]),
 "c5": (8, "decorar", "Dose de manutenção = Cp·Cl·τ/F; repõe o que o clearance remove a cada intervalo.", "objetivos f.i(4a)", ["maintenance dose"]),
 "c6": (8, "e-se", "Na insuficiência renal ou hepática, a dose de ataque não muda e a de manutenção diminui.", "banco p.18 e p.55", ["renal"]),
 "o1": (11, "explicar", "Na curva oral a concentração sobe enquanto a absorção vence a eliminação; no pico (Cmáx) as duas se igualam.", "objetivos f.i(2a); apostila p.16 (ka)", ["absorption"]),
 "o2": (11, "decorar", "Biodisponibilidade oral = ASC oral / ASC IV.", "objetivos f.i(2b)", ["AUC"]),
 "r1": (11, "explicar", "Doses repetidas acumulam até o platô; o intervalo define a oscilação entre pico e vale.", "objetivos f.i(4); De Nucci p.4", ["steady state"]),
 "z1": (11, "distinguir", "Ordem zero: quantidade constante eliminada por tempo, curva linear e meia-vida que varia com a dose.", "objetivos f.ii(1)", ["zero-order"]),
 "z2": (11, "decorar", "Fenitoína, etanol e aspirina em dose alta seguem ordem zero.", "objetivos f.ii(1); banco p.65", ["phenytoin"]),
 "z3": (11, "explicar", "Michaelis-Menten: Km é a concentração em que a velocidade é metade da Vmax; acima de Km a enzima satura.", "objetivos f.ii(1)", ["Michaelis"]),
 "z4": (11, "e-se", "Na saturação, um pequeno aumento da dose eleva muito a concentração (fenitoína).", "objetivos f.ii(1); banco p.65", ["phenytoin"]),
 "z5": (11, "e-se", "Quando a ligação às proteínas satura (salicilato em superdose), a fração livre sobe de forma desproporcional à dose.", "objetivos f.ii(2)", ["salicylate"]),
 "z6": (11, "e-se", "Absorção que depende de transportador intestinal satura: a biodisponibilidade muda com a dose.", "objetivos f.ii(3)", ["absorbed"]),
 "x1": (12, "e-se", "Vd calculado pela dose IV dividida pela concentração inicial.", "apostila ex.2; questão orientadora 8", ["volume of distribution"]),
 "x2": (12, "explicar", "ke pela meia-vida (0,693/t½) e a fração eliminada por hora.", "objetivos (Prof. Gilberto 5); apostila ex.10", ["half"]),
 "x3": (12, "e-se", "Taxa de infusão para um Css: R0 = Cl·Css.", "apostila ex.1; questão orientadora 1", ["Css"]),
}

PASSOS = [("Bolus IV e constante de eliminação", ["k1", "k5", "k2", "k3", "k4"]), ("Meia-vida, estado de equilíbrio e MRT", ["h1", "h2", "h3", "h4"]),
          ("Volume de distribuição, clearance e infusão", ["c1", "c2", "h5", "c3", "c4", "c5", "c6"]),
          ("Via oral, doses repetidas e cinética não linear", ["o1", "o2", "r1", "z1", "z2", "z3", "z4", "z5", "z6"]), ("Aplicação (cálculos)", ["x1", "x2", "x3"])]

def _tabela():
    """item → nids/chaves, lido de tabela.tsv (a mesma tabela monta o spec); EXTRA liga o card a um segundo item que ele também atende."""
    out = {}
    for l in (HERE / "tabela.tsv").read_text(encoding="utf-8").splitlines():
        if l.startswith("#") or not l.strip():
            continue
        x, item = l.split("\t")[:2]
        out.setdefault(item, []).append(int(x) if x.isdigit() else x)
    for item, xs in EXTRA.items():
        out[item] = out.get(item, []) + xs
    return out


EXTRA = {"x1": [1490066159100], "x2": [1490066195477, "sh-1792624463275"], "x3": ["sh-1792624466325"], "c2": ["sh-1792657544384"]}
CARDS_SRC = _tabela()
TERMOS = {}
def _resolver():
    try:
        plan = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
    except OSError:
        return {}
    chaves = {e["key"] for e in plan["entries"]} | {f"sh-{k}" for k in plan.get("compartilhados", {})}
    por_fonte = {str(v.get("source_nid")): f"sh-{k}" for k, v in plan.get("compartilhados", {}).items() if v.get("source_nid")}
    out = {}
    for item, xs in CARDS_SRC.items():
        ks = []
        for x in xs:
            k = x if isinstance(x, str) else (f"ak{x}" if f"ak{x}" in chaves else por_fonte.get(str(x)))
            if k not in chaves:
                raise SystemExit(f"{item}: {x} não está no plano")
            ks.append(k)
        out[item] = ks
    return out


CARDS = _resolver() if __name__ != "spec" else {}  # o spec só lê ITENS

# Matriz: (id, fonte, tipo, âncora do trecho literal, itens) — questões numeradas pelo próprio enunciado
F = {"O": ("fontes/objetivos.pdf", 6, 9), "A": ("fontes/apostila.pdf", 18, 20), "Q": ("fontes/orientadoras-fc.pdf", 1, 10),
     "T": ("fontes/todas-questoes.pdf", 1, 91)}
L2 = lambda o: ("fora", "fora-do-escopo", f"Conceito qualitativo coberto no deck-prova 2 (Farmacocinética): {o}.")
QUESTOES = {1: ["c3", "x3"], 8: ["c1", "x1"], 31: ["k4"], 32: ["k2"], 33: ["k3"], 34: ["h1"]}
OUTRAS = [  # (id, chave de F, tipo, âncora, itens ou ("fora", motivo, porquê))
 ("obj-f1a", "O", "item", "(a) Definição do processo de primeira ordem", ["k1", "k3", "k4"]),
 ("obj-f1b", "O", "item", "(b) Parâmetros farmacocinéticos que determinam o gráfico", ["h1", "c1", "c2", "o2"]),
 ("obj-f2", "O", "item", "(2) Dose única oral", ["o1", "o2"]),
 ("obj-f3", "O", "item", "(3) infusão constante i.v.", ["c3", "h3", "c4"]),
 ("obj-f4", "O", "item", "(4) dosagem repetida em um compartimento", ["r1", "c5"]),
 ("obj-fii1", "O", "item", "(1) Eliminação com cinética de ordem zero", ["z1", "z2", "z3", "z4"]),
 ("obj-fii2", "O", "item", "(2) Saturação da ligação às proteínas plasmáticas", ["z5"]),
 ("obj-fii3", "O", "item", "(3) Absorção dependente da dose", ["z6"]),
 ("gil1", "O", "questao", "1. “Foi dado a um paciente nefropata", ["c6", "c3"]), ("gil3", "O", "questao", "3. Do gráfico ao lado, podemos identificar", ["h2", "k3"]),
 ("gil4", "O", "questao", "4. Um indivíduo sadio, de 70 kg", ["h1"]), ("gil5", "O", "questao", "5. Sabendo que o cálculo da constante de eliminação", ["x2"]),
 ("gil6", "O", "questao", "6. Levando em consideração que o volume de distribuição", ["c1"]),
 ("ap1", "A", "questao", "1. A substância B possui", ["c3", "x3"]), ("ap2", "A", "questao", "2. Um paciente de 35 anos e 70kg", ["c1", "x1"]),
 ("ap5", "A", "questao", "5. Um fármaco com meia-vida de 10 horas", ["h3"]), ("ap10", "A", "questao", "10. Foi injetado, por via endovenosa, 200mg", ["h1", "x2"]),
]
BANCO = [  # questões de cálculo do banco dos grupos (fontes/todas-questoes.pdf), lidas inteiras em 30/10 no lote 2
 ("t-g1a2", "2. Do gráfico ao lado, podemos identificar o tempo de meia-vida", ["h2", "k3"]), ("t-g1a3", "3. Um indivíduo sadio, de 70 kg, dá entrada", ["h1"]),
 ("t-g1a4", "4. Sabendo que o cálculo da constante de eliminação", ["x2"]), ("t-g1a5", "5. Levando em consideração que o volume de distribuição do dipirona", ["c1"]),
 ("t-g2a4", "4) Uma criança com clearance normal recebeu uma dose de 200mg", ["h2"]), ("t-g2b2", "2) Um jovem de 50 kg foi medicado com 700mg", ["c1", "h1"]),
 ("t-g2b3", "3) Um homem de 70kg recebeu 500mg de um fármaco", ["c1"]), ("t-g2b5", "5) A concentração de um fármaco A no sangue decai seguindo", ["k1", "h2"]),
 ("t-g3a2", "2) Paciente de sexo masculino, 20 anos, 80 kg", ["c4"]), ("t-g3a5", "5) Um paciente de 70 kg, após realização de cirurgia de correção de hérnia", ["c1"]),
 ("t-g3b1", "1- Um determinado fármaco chega a um determinado local de ação", L2("fração de extração (Ca − Cv)/Ca")),
 ("t-g3b2", "2- Foi injetado, por via endovenosa, 200mg de um fármaco com volume de distribuição de 40L", ["h1", "x2"]),
 ("t-g3b4", "4- Um médico injetou num paciente, por via endovenosa, um fármaco cuja constante", ["h1", "h2"]),
 ("t-g4a1", "1) Um Bôlus de 354ml de um fármaco", ["h2"]), ("t-g4a4", "4) Foi administrado em um paciente 500mg de uma droga intravenosa", ["c2"]),
 ("t-g4b2", "2) Uma dose de 660 mg gramas", ["c1", "h1"]), ("t-g4b3", "3) Sobre tempo de meia-via e estado de equilíbrio", ["h3"]),
 ("t-g4b5", "5) Adaílton adoeceu", ["c5"]), ("t-g5-5", "5) Um fármaco, como visto no gráfico abaixo, apresenta três formas", ["o1"]),
 ("t-g6-1", "1) Qual o volume de distribuição em litros do antibiótico Z", ["c1"]), ("t-g6-4", "4) Deseja-se administrar um determinado fármaco em bolus", ["r1"]),
 ("t-g6b2", "Questão 2) Um interno calculou uma dose de vancomicina", ["c4"]), ("t-g6b4", "Questão 4) Um fármaco com um índice terapêutico de 1,2", ["c4", "c5"]),
 ("t-g7a1", "1. Um certa droga foi administrada na concentração de 12 mg/L", ["x2"]), ("t-g7a6", "6. Tabela: Concentrações Plasmáticas", ["x2"]),
 ("t-g8-4", "4- Segue, na tabela abaixo, valores da concentração plasmática de 200 mg", ["c1"]),
 ("t-107-3", "Durante a administração crônica do fármaco", ["h3", "h5"]), ("t-diaz", "apresentou convulsões e foi levada ao pronto socorro", ["c4"]),
 ("t-feni", "O fármaco fenitoína apresenta cinética de saturação", ["z4"]), ("t-elix", "Se um elixir de 10 mL", ["o2"]),
 ("t-fx", "Um fármaco X de faixa terapêutica de 7-9mg/L", ["c4"]), ("t-mrt", "tempo médio de residência desse fármaco", ["h4"]),
 ("t-770", "Uma dose de 770 mg gramas", ["c1", "h1"]), ("t-faixa", "Sabendo-se que a faixa terapêutica de certo", ["c4"]),
 ("t-infus", "é iniciada às 8 horas da manhã", ["c3"]), ("t-repet", "Suponha que se deva administrar a um paciente, inicialmente sem tratamento", ["r1", "h3"]),
 ("t-mv1", "A respeito da meia vida de um fármaco em um modelo de compartimento único", ["h3", "k1"]),
 ("t-mv2", "Com relação ao tempo de meia-vida de um fármaco, é correto", ["h2"]), ("t-rimfig", "Se a eliminação de um fármaco ocorre, essencialmente, pelo rim e fígado", ["c2"]),
]

def _txt(chave):
    f, a, z = F[chave]
    return texto_paginas(HERE / f, a, z)


def _linha(id_, k, tipo, txt, ancora, alvo):
    i = txt.find(ancora)
    if i < 0:
        raise SystemExit(f"âncora da matriz não achada: {id_} {ancora!r}")
    linha = {"id": id_, "fonte": F[k][0], "tipo": tipo, "trecho": txt[i:i + max(len(ancora), 40)]}
    if isinstance(alvo, tuple):
        linha.update({"fora": alvo[1], "porque": alvo[2]})
    else:
        linha["itens"] = alvo
    return linha


def matriz():
    txts = {k: _txt(k) for k in F}
    linhas = []
    for n, alvo in QUESTOES.items():
        m = re.search(rf"Questão {n} (.{{20,70}}?\S)(?=\s)", txts["Q"])
        linhas.append(_linha(f"q{n}", "Q", "questao", txts["Q"], m.group(0), alvo))
    for id_, k, tipo, ancora, alvo in OUTRAS:
        linhas.append(_linha(id_, k, tipo, txts[k], ancora, alvo))
    for id_, ancora, alvo in BANCO:
        linhas.append(_linha(id_, "T", "questao", txts["T"], ancora, alvo))
    for x in linhas:
        if "itens" in x:
            x["cards"] = sorted({c for it in x["itens"] for c in CARDS.get(it, [])})
    q = {}
    for x in linhas:
        if x["tipo"] == "questao":
            q[x["fonte"]] = q.get(x["fonte"], 0) + 1
    return {"_como": "uma linha por item das fontes base e por questão; cards = união dos cards dos itens (planejar.py)",
            "questoes_por_fonte": q, "linhas": linhas}


def mapa():
    return {"objetivos_da_aula": "Objetivos cognitivos de farmacocinética quantitativa (item f: primeira ordem, bolus, oral, infusão, doses repetidas, desvios), "
                                 "as questões orientadoras FC de cálculo, os exercícios da apostila, as questões do Prof. Gilberto e as de cálculo do banco",
            "cronograma": {"aulas_vizinhas": ["Deck-prova 2 Farmacocinética", "UC19 Farmacocinética aula 3 (Prof. Gilberto)", "Rodada final do deck-prova UC19"],
                           "conferido": "Cronograma 2026 da UC19 lido: farmacocinética nas aulas do Prof. Gilberto; o lote 3 cobre o item f do roteiro (cinética quantitativa) e os cálculos da prova; os itens a–e ficaram no lote 2."},
            "passos": [{"passo": nome, "laminas": ITENS[ids[0]][0], "itens": [
                {"id": i, "tipo": ITENS[i][1], "o_que": ITENS[i][2], "fonte": ITENS[i][3], "termos": TERMOS.get(i, ITENS[i][4]), "cards": CARDS.get(i, [])}
                for i in ids]} for nome, ids in PASSOS],
            "fora": [{"o_que": x[3], "motivo": x[4][2]} for x in OUTRAS if isinstance(x[4], tuple)]}


def motivacoes():
    return {"motivacoes": [{"id": f"m-{i}", "item_mapa": i, "reconstruir": ITENS[i][2],
                            "por_que_dura": f"Item {ITENS[i][1]} cobrado em {ITENS[i][3]}; sem ele a questão correspondente da prova não se responde.",
                            "depois_de": "", "atendida_por": CARDS.get(i, [])} for i in ITENS]}


FAMILIA = [("Objetivos", "objetivos"), ("Apostila", "apostila"), ("De Nucci", "De Nucci"), ("orientadora", "orientadora"), ("Gilberto", "Gilberto")]


def inventario():
    """inventario.py para nebli.inventario: cada página da base com os itens que ela ensina (mesmo bloco e mesma fonte)."""
    ind = json.loads((HERE / "fontes" / "base-prova-indice.json").read_text(encoding="utf-8"))
    linhas, dmap = [], {}
    for pg in ind:
        ids = PASSOS[pg["bloco"] - 1][1]
        fam = next((f for r, f in FAMILIA if r.lower() in pg["titulo"].lower()), None)
        its = [i for i in ids if fam and fam.lower() in ITENS[i][3].lower()] or ids[:1]
        if pg["bloco"] == 5:
            its = ids
        regs = []
        for k, i in zip("abcdefghijklmnop", its):
            dmap[f"{pg['pagina']}{k}"] = i
            regs.append(f"(\"{k}\", {json.dumps(ITENS[i][2][:90], ensure_ascii=False)}, D.get(\"{pg['pagina']}{k}\", \"\"))")
        linhas.append(f" ({pg['pagina']}, \"conteudo\", {json.dumps(pg['titulo'][2:110], ensure_ascii=False)}, [{', '.join(regs)}]),")
    ex = []
    for x in matriz()["linhas"]:
        if x["tipo"] == "questao" and x.get("itens"):
            dmap[x["id"]] = x["itens"][0]
            ex.append(f"  (\"{x['id']}\", {json.dumps(x['trecho'][:80], ensure_ascii=False)}, D.get(\"{x['id']}\", \"\")),")
    cap = []
    for i in ("k1", "h1", "c3", "z1"):
        dmap["rang-" + i] = i
        cap.append(f"  (\"rang-{i}\", {json.dumps(ITENS[i][2][:90], ensure_ascii=False)}, D.get(\"rang-{i}\", \"\")),")
    D = {k: CARDS.get(i, []) for k, i in dmap.items() if CARDS.get(i)}
    return "\n".join([
        '"""Inventário atômico do deck-prova UC19 lote 3 (Farmacocinética quantitativa), gerado por planejar.py a partir da base da prova',
        '(fontes/slides.pdf: 13 páginas de excertos literais) e dos itens da E3. Destinos (D) preenchidos depois da busca."""',
        'PREFIXO = "dp3"', 'AULA = "Deck-prova 3 — Farmacocinética quantitativa (UC19 P1; Farmacologia; Prof. Gilberto)"', "EXC = \"EXC: \"",
        f"D = {json.dumps(D, ensure_ascii=False)}", "", "SLIDES = [", *linhas, "]", "JUSTIFICATIVAS = {}",
        'CAPITULO = [("Rang & Dale cap. 10: farmacocinética (modelos, meia-vida, saturação)", [', *cap, "])]",
        'EXERCICIOS = [("Questões de cálculo (orientadoras FC, apostila, Prof. Gilberto, banco)", [', *ex, "])]", ""])


HISTORIA = ("Depois de um bolus, o organismo elimina sempre a mesma fração do que tem: a curva cai em exponencial, e no gráfico log vira uma reta cuja "
            "inclinação é ke. Daí sai a meia-vida, constante, que diz quanto tempo leva para eliminar e para chegar ao equilíbrio. O Vd liga a dose à "
            "concentração e dá a dose de ataque; o clearance liga a concentração à saída e dá a manutenção e a infusão (R0 = Cl·Css). Pela via oral "
            "entra a absorção (ka, Cmáx, ASC); quando a enzima satura, a eliminação vira ordem zero e a meia-vida deixa de ser constante.")
LINHA = [("Bolus IV: queda exponencial, reta no semilog com inclinação −ke", "A inclinação dá a meia-vida", ["k1", "k2", "k3"]),
         ("Meia-vida: 0,693/ke; 5 meias-vidas para eliminar e para o equilíbrio", "Vd e clearance determinam a meia-vida e a dose", ["h1", "h2", "h3", "h4"]),
         ("Vd, clearance e infusão: dose de ataque, manutenção e R0 = Cl·Css", "Pela via oral entra a absorção, e na saturação a cinética muda", ["c1", "c2", "c3"]),
         ("Oral, doses repetidas e ordem zero", "", ["o1", "r1", "z1", "z4"])]
CONEXAO = ["mrt", "oscilacao", "saturacao-fenitoina"]

def escopo():
    linha = [{"passo": p, "mecanismo": True, "liga_ao_proximo": l, "cards": sorted({c for i in its for c in CARDS.get(i, [])})} for p, l, its in LINHA]
    return {"ciclo": "básico", "justificativa": "Deck-prova independente das aulas (F-20261029-CLAUDE-04): farmacocinética quantitativa do item f dos objetivos e os cálculos da prova; fármaco por nome só como exemplo de princípio (F-20261031-CLAUDE-01).",
            "clinica_lateral": [], "clinica_e_tema": False, "motivo_tema": "", "ordem_da_fala": [], "historia": HISTORIA, "linha_logica": linha,
            "cards_de_conexao": CONEXAO, "provas": [dict({"id": _qid(x), "cards": x.get("cards", [])}, **({"fora": x["porque"]} if x.get("fora") else {})) for x in matriz()["linhas"] if x["tipo"] == "questao"],
            "uso_das_fontes": {f: sorted({c for i in its for c in CARDS.get(i, [])}) for f, its in USO.items()}}


USO = {"aula": ["k2", "h2", "c1", "c3"],  # base da prova: apostila aula 3 e objetivos f
       "prova": ["x1", "x2", "x3", "z4"],  # orientadoras, exercícios, Prof. Gilberto e banco
       "bibliografia": ["k1", "z3"],  # Rang cap. 10
       "apostila": ["h1", "h4", "c4"]}  # apostila guia e De Nucci
FONTE_Q = {"fontes/orientadoras-fc.pdf": "FC", "fontes/apostila.pdf": "Apostila", "fontes/todas-questoes.pdf": "Banco", "fontes/objetivos.pdf": "Gilberto"}


def _qid(x):
    return f"{FONTE_Q[x['fonte']]} {x['id']}"


def indice_provas():
    """fontes/provas-deck-prova.txt no formato do índice de provas ('── [fonte] id texto'), lido pelo gate de calibragem."""
    return "\n".join(f"── [{FONTE_Q[x['fonte']]}] {x['id']} {x['trecho']}" for x in matriz()["linhas"] if x["tipo"] == "questao") + "\n"


if __name__ == "__main__":
    (HERE / "matriz-prova.json").write_text(json.dumps(matriz(), ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "mapa-de-profundidade.json").write_text(json.dumps(mapa(), ensure_ascii=False, indent=1), encoding="utf-8")
    mot = HERE / "motivacoes.json"
    congelado = HERE / "etapas" / "E3-motivacoes.json"
    if not congelado.exists():  # depois da E3 as motivações ficam congeladas; só 'atendida_por' muda
        mot.write_text(json.dumps(motivacoes(), ensure_ascii=False, indent=1), encoding="utf-8")
    else:
        d = json.loads(mot.read_text(encoding="utf-8"))
        for x in d["motivacoes"]:
            x["atendida_por"] = CARDS.get(x["item_mapa"], [])
        mot.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "inventario.py").write_text(inventario(), encoding="utf-8")
    (HERE / "fontes" / "provas-deck-prova.txt").write_text(indice_provas(), encoding="utf-8")
    esc = HERE / "escopo.json"
    e = escopo()
    if esc.exists():  # campos escritos à mão depois (uso_das_fontes, cards_de_conexao) ficam
        velho = json.loads(esc.read_text(encoding="utf-8"))
    esc.write_text(json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(ITENS)} itens; matriz com {len(matriz()['linhas'])} linhas")
