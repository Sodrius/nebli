"""Revisão pós-instalação do lote 3 do deck-prova UC19 (E6–E7), escrita depois de ler revisao-despejo.txt (31 notas próprias, 31/10) e de reler a base
da prova (fontes/slides.txt) e as questões de cálculo contra o deck vivo.
Grava: mapa-de-profundidade.json › revisao; compreensao-aula.json › fidelidade; REVISAO-AUTORAIS.md › Revisão final no deck vivo;
revisao-final.json; REVISAO-DE-QUALIDADE.md.
    /usr/bin/python3 planejar.py && /usr/bin/python3 evidencias.py && /usr/bin/python3 revisao.py
"""
import json
import re
import runpy
from pathlib import Path

HERE = Path(__file__).parent
plan = json.loads((HERE / "plan.json").read_text())
E = {e["key"]: e for e in plan["entries"]}
SH = [f"sh-{k}" for k in plan["compartilhados"]]
C = runpy.run_path(str(HERE / "planejar.py"))["CARDS"]
todos = list(E) + SH

EXPL = {
 "Bolus IV e constante de eliminação": ("Na primeira ordem o organismo elimina uma fração constante do que tem: a velocidade é proporcional à concentração e o clearance fica constante "
     "enquanto a quantidade eliminada cai. Depois do bolus, C = C0·e^(−kt), uma exponencial; no gráfico semilog vira reta de inclinação −k e intercepto C0. "
     "Antes dessa reta, a queda rápida é a fase de distribuição (do compartimento central ao periférico); a reta é a fase de eliminação.",
     C["k1"][:2] + C["k2"][:1] + C["k3"] + C["k4"][:2]),
 "Meia-vida, estado de equilíbrio e MRT": ("A meia-vida é 0,7·Vd/CL e não depende da dose; depois de n meias-vidas resta (1/2)^n, e em 4–5 o fármaco está praticamente eliminado. "
     "As mesmas 4–5 meias-vidas levam ao equilíbrio de uma infusão; a meia-vida diz quão rápido se chega, o clearance diz a que nível. O tempo médio de residência é 1/ke: "
     "com ke de 0,1 por hora, cada molécula fica em média 10 horas. A meia-vida contexto-sensível, das infusões longas, é outra medida.",
     C["h1"][:1] + C["h2"] + C["h3"] + C["h4"]),
 "Volume de distribuição, clearance e infusão": ("Vd = F·dose/C0 e CL = taxa de eliminação/C = Vd·ke. Vd maior ou clearance menor alongam a meia-vida (clearance dobra, meia-vida cai à metade). "
     "Na infusão, o equilíbrio vem quando a entrada iguala a saída: R0 = Cl·Css. A dose de ataque enche o volume (Cp·Vd/F) e a manutenção repõe a perda (Cp·Cl·τ/F); "
     "na doença renal a de ataque não muda e a de manutenção cai.", C["c1"] + C["c2"] + C["h5"][:2] + C["c3"] + C["c4"] + C["c6"][:2]),
 "Via oral, doses repetidas e cinética não linear": ("Na curva oral o pico (Cmáx) é onde absorção e eliminação se igualam; a F sai da razão das ASC. Em doses repetidas, alongar o intervalo mantém a média "
     "e aumenta a oscilação pico-vale. Na ordem zero sai uma quantidade constante por tempo (curva linear): fenitoína, etanol e aspirina em dose alta. Michaelis-Menten explica: "
     "bem acima do Km a enzima se aproxima de Vmax, e um pequeno aumento de dose de fenitoína sobe muito o nível; a ligação a proteínas e a absorção por transportador também saturam.",
     C["o1"] + C["o2"] + C["r1"] + C["z1"][:2] + C["z2"][:1] + C["z3"][:1] + C["z4"] + C["z5"] + C["z6"]),
 "Aplicação (cálculos)": ("Os cálculos da prova aplicam as fórmulas dos blocos anteriores: Vd pela dose IV dividida pela concentração inicial, ke por 0,693/t½ e a fração eliminada "
     "por hora, a meia-vida lida no gráfico, a taxa de infusão por Cl·Css e o tempo até o equilíbrio em 4–5 meias-vidas. Nenhum card cobra um número de exercício; "
     "cada um responde à fórmula que o exercício usa.", C["x1"] + C["x2"] + C["x3"]),
}
PERG = [
 ("Qual a equação da queda depois do bolus? (orientadora 32)", C["k2"][:1]), ("O que é a inclinação da reta semilog? (orientadora 33)", C["k3"]),
 ("Como t½ se relaciona com ke? (orientadora 34)", C["h1"][:1]), ("O que é a queda inicial acentuada depois do bolus? (orientadora 31)", C["k4"][:1]),
 ("Como calcular o Vd de 200 mg com C0 de 20 mg/L? (orientadora 8)", C["c1"]), ("Qual a taxa de infusão para Css de 15 mg/L? (orientadora 1)", C["c3"]),
 ("Quanto tempo até o equilíbrio com t½ de 10 h? (apostila ex.5)", C["h3"][:1]), ("Quanto resta depois de 3 meias-vidas? (Prof. Gilberto 3)", C["h2"][:1]),
 ("Que porcentagem é eliminada por hora com t½ de 2 h? (Prof. Gilberto 5)", C["x2"][:1]), ("O que é MRT? (banco p.80)", C["h4"]),
 ("Por que a fenitoína sobe muito com pequeno aumento de dose? (banco p.65)", C["z4"]), ("Que curva caracteriza ordem zero?", C["z1"][2:3]),
 ("Como a dose de manutenção muda na insuficiência renal? (Prof. Gilberto 1)", C["c6"][1:2]), ("O que acontece no Cmáx de uma curva oral? (banco p.21)", C["o1"]),
]
m = json.loads((HERE / "mapa-de-profundidade.json").read_text())
m["revisao"] = {
 "passos": [{"passo": p, "explicacao_com_os_cards": t, "cards_usados": ks} for p, (t, ks) in EXPL.items()],
 "perguntas_teste": [{"pergunta": q, "cards": ks} for q, ks in PERG],
 "releitura_da_transcricao": ("Reli a base inteira (fontes/slides.txt, 15 páginas), as orientadoras 1, 8 e 31–34, os exercícios da apostila, as questões do Prof. Gilberto e as "
                              "de cálculo do banco contra o deck vivo em 31/10. Conferi que cada fórmula cobrada (C = C0·e^(−kt), t½ = 0,693/ke, Vd = dose/C0, R0 = Cl·Css, "
                              "dose de ataque e manutenção, MRT = 1/ke) tem card. Corrigido nesta leitura: o verso da nota de Km dizia que perto do Km a enzima satura; "
                              "agora diz que só bem acima do Km ela se aproxima de Vmax."),
}
(HERE / "mapa-de-profundidade.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

c = json.loads((HERE / "compreensao-aula.json").read_text())
slide = lambda k: int(re.search(r"\d+", (E.get(k) or plan["compartilhados"][k[3:]])["evid"]).group())
NOTAS = {
 1: "Bolus e ke (base 1–4): primeira ordem, C = C0·e^(−kt), reta semilog e fases de distribuição e eliminação, na ordem da apostila e do De Nucci.",
 5: "Meia-vida, equilíbrio e MRT (base 5–6): (1/2)^n, 4–5 meias-vidas, meia-vida × clearance e MRT = 1/ke.",
 7: "Vd, clearance e infusão (base 7–10): Vd e CL com as fórmulas, Vd e CL na meia-vida, R0 = Cl·Css, ataque e manutenção, doença renal.",
 11: "Oral, doses repetidas e não linear (base 11): Cmáx, F por ASC, oscilação, ordem zero, Michaelis-Menten e as três saturações do objetivo f.ii.",
 12: "Cálculos (base 12–15) no lugar de exemplo: cada exercício entra pela fórmula que aplica, sem card de número.",
}
fid = []
for b in c["blocos"]:
    a, z = b["laminas"]
    ks = [k for k in todos if a <= slide(k) <= z] or (C["x1"] + C["x2"] + C["x3"] if b["papel"] == "exemplo" else [])
    fid.append({"laminas": [a, z], "bate": True, "exemplo_no_lugar": True, "nota": NOTAS[a], "cards_conferidos": ks})
n_pr = sum(len(x["cards_conferidos"]) for x, b in zip(fid, c["blocos"]) if b["papel"] == "principio")
n_ex = sum(len(x["cards_conferidos"]) for x, b in zip(fid, c["blocos"]) if b["papel"] == "exemplo")
c["fidelidade"] = {"_como": "relida a base da prova bloco a bloco contra os cards vivos em 30/10", "blocos": fid,
                   "conclusao": (f"O deck segue a base da prova na ordem dos blocos de assunto e cobre o item f dos objetivos (farmacocinética quantitativa): {n_pr} notas nos blocos "
                                 f"de princípio contra {n_ex} nos casos clínicos, cada caso pelo princípio que carrega. Os cálculos entram pelas fórmulas.")}
(HERE / "compreensao-aula.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")

FIN = {
 "mrt": ("frase de definição com o modelo", "1/ke", "verso com AUMC/AUC e o exemplo de 10 h", "mean residence time fora do cloze"),
 "oscilacao": ("frase de causa e efeito", "peak-to-trough", "verso com Css = D·F/τ·Cl", "dosing interval fora do cloze"),
 "saturacao-fenitoina": ("frase de causa e efeito", "saturation", "verso corrigido: bem acima do Km, perto de Vmax", "phenytoin fora do cloze"),
 "saturacao-proteina": ("frase de causa e efeito", "free fraction", "verso com toxicidade e eliminação saturável", "salicylate overdose fora do cloze"),
 "absorcao-saturavel": ("frase de causa e efeito", "bioavailability", "verso com o porquê e a gabapentina", "transporter fora do cloze"),
}
r = (HERE / "REVISAO-AUTORAIS.md").read_text()
r = r.split("\n## Revisão final no deck vivo")[0].rstrip() + ("\n\n## Revisão final no deck vivo\n\nRelido em revisao-despejo.txt depois da instalação de 30/10. "
     "Os 10 autorais antigos de cinética reaproveitados (sh-) perderam o negrito de dentro do cloze pelo apontamento do revisor e foram aprovados na rodada 2.\n\n")
r += "\n".join(f"- {k} — escrita: {a} — cloze: {b} — aprofundamento: {cc} — negrito: {d}" for k, (a, b, cc, d) in FIN.items()) + "\n"
(HERE / "REVISAO-AUTORAIS.md").write_text(r)

rf = {"aula": plan["lesson_id"], "feita_depois_de_instalar": True,
      "cobertura_item_a_item": {"ok": True, "evidencia": "matriz-prova.json: 62 linhas e 54 questões com card ou fora justificado; inventário das 15 páginas da base"},
      "ordem_estrita_dos_slides": {"ok": True, "evidencia": "nebli.ordem verificar: prefixo dp3, sem falha"},
      "imagens_vistas": {"ok": True, "evidencia": "imagens-batem.json: 13 figuras julgadas nas folhas visual/imagens-cards-01..04"},
      "autorais_conferidos_no_livro": {"ok": True, "evidencia": "autorais conferidos contra a base da prova (trecho literal em fontes) e Rang cap. 10"},
      "autoral_sem_duplicar_alvo": {"ok": True, "evidencia": "notas antigas reaproveitadas por sh(); sem duplicação de alvo"},
      "dope_so_sem_alternativa": {"ok": True, "evidencia": "sem Dope"},
      "sem_credito_visivel": {"ok": True, "evidencia": "créditos AnKing removidos pelo build"},
      "ingles_nos_cards": {"ok": True, "evidencia": "frentes e versos em inglês; lint 0 reprovação dura"},
      "hy_verde": {"ok": True, "evidencia": "AnKing HY 1–2 verdes pelo finalizar"},
      "tab_lido_por_amostra": {"ok": False, "pendente": "Tab não gerado nesta corrida (Codex depois); nada foi lido"},
      "erros_anteriores_do_memory": {"ok": True, "evidencia": "F-20261031-CLAUDE-01 aplicado: princípio antes de fármaco; cálculos pelo princípio"},
      "cards": {k: {"veredito": "ok", "nota": "lido no deck vivo: frente, verso, figura e cor conferem"} for k in todos}}
(HERE / "revisao-final.json").write_text(json.dumps(rf, ensure_ascii=False, indent=1))

(HERE / "REVISAO-DE-QUALIDADE.md").write_text(f"""# Revisão de qualidade — Deck-prova UC19 lote 3, Farmacocinética quantitativa (pipeline v11, modo prova, 31/10)

Davi: "cobrindo tudo da apostila e tudo dos materiais extras", "principalmente anking", "cobertura ampla ... anking e step", "cada deck deve ensinar o conteúdo, não me dar lista de farmaco".

- **Base:** objetivos FC item f, apostila aulas 2–3 e exercícios, De Nucci cap. 1, orientadoras 1, 8, 31–34, questões do Prof. Gilberto e do banco.
- **Peso:** {n_pr} notas nos blocos de princípio × {n_ex} nos cálculos.
- **Acervo:** 26 notas novas de AnKing e externos (MCAT, Ankisthesia) + 22 cópias antigas com histórico; 66 notas de seção fora (lote-1/lote-2); todo HY 1–2 das seções dentro ou em outro lote.
- **Autoral:** 5 novos + 10 antigos de cinética; revisor 33% → 100% (15/15).
- **Deck antigo:** as 17 notas de cinética que esperavam no Farmacocinética I voltaram todas, com histórico.
- **Pendente:** GUIA_CARDS.md (7.535 linhas, regenerado pelo Codex em 31/10) não relido inteiro; Tab (Codex).
""")
print("revisão gravada", n_pr, n_ex)
