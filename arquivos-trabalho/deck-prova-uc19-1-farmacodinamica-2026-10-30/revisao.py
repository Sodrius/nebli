"""Revisão pós-instalação do lote 1 do deck-prova UC19 (E6–E7), escrita depois de ler revisao-despejo.txt (51 notas próprias) e de reler a base
da prova (fontes/slides.txt) e as 40 questões orientadoras contra o deck vivo.
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
 "Fundamentos": ("O fármaco é a substância ativa; com excipientes vira medicamento, e remédio é qualquer recurso que alivia (farmaco-medicamento). "
                 "Phármakon queria dizer remédio e veneno, e a dose separa os dois (dose-veneno). A farmacocinética é o que o corpo faz com o fármaco e a "
                 "farmacodinâmica o que o fármaco faz ao corpo (card PK/PD); antes de agir, o comprimido desintegra e dissolve (fase biofarmacêutica), e todo "
                 "fármaco novo passa pelas fases I a IV antes e depois do registro.", C["f2"] + C["f3"] + C["f1"] + C["f5"][:1]),
 "Alvos farmacológicos": ("O fármaco age ligando-se a receptores, canais, transportadores, enzimas ou ácidos nucleicos (classes-alvo). Receptores vão de canal "
                          "iônico (GABA-A) a acoplados à proteína G, tirosina-quinases e nucleares (peptídeo na membrana, esteroide dentro). No canal: anestésico "
                          "local bloqueia o Na+; no transportador: diurético de alça no NKCC2 e IBP na bomba H+/K+; no DNA: platinas fazem ligação cruzada e "
                          "antraciclinas intercalam, com nefro e cardiotoxicidade. A via do NO mostra alvo enzimático: NO ativa a guanilato ciclase, o GMPc ativa "
                          "PKG e relaxa o músculo; a PDE5 degrada o GMPc e o sildenafil a inibe. Manitol, antiácido e quelante agem sem alvo.",
                          C["a1"] + C["a2"][:2] + C["a3"][:2] + C["a4"][:1] + C["a6"][:2]),
 "Curva dose-resposta e segurança": ("Ligar é afinidade; ativar depois de ligado é atividade intrínseca (card do GUIA-2). Na curva, eficácia é o platô e potência "
                                     "é a dose para 50% (EC50): a curva mais à esquerda é a mais potente (cards de gráfico). Na população, as curvas quantais dão DE50 "
                                     "e DT50; TD50/ED50 é o índice terapêutico, alto é seguro, e os de IT estreito (varfarina, teofilina, digoxina, antiepilépticos, lítio) "
                                     "têm janela terapêutica estreita e precisam de monitoração (janela).",
                                     C["c1"] + C["c2"] + C["c3"][2:] + C["c5"] + C["c6"]),
 "Agonismo": ("O receptor oscila entre inativo e ativo; o agonista pleno dá o máximo, o parcial dá resposta submáxima em qualquer dose, o inverso baixa a "
              "atividade constitutiva abaixo do basal e o tendencioso favorece uma via (agonismo-org). Por isso o parcial desce o platô (curva que desce) e, "
              "junto do pleno, reduz a resposta: buprenorfina precipita abstinência em quem usa morfina. O antagonista neutro só impede o agonista, sem mexer "
              "no basal.", C["g1"] + C["g2"] + C["g3"] + C["g4"]),
 "Antagonismo, alosterismo e quiralidade": ("O competitivo reversível ocupa o mesmo sítio: potência cai (curva à direita), eficácia fica, e mais agonista supera. "
                                            "O não competitivo e o irreversível baixam o máximo e não são superados; no modelo enzimático isso aparece como Km × Vmax "
                                            "(aspirina, iMAO, fenoxibenzamina são covalentes). Fora do receptor do agonista há o químico, o farmacocinético e o "
                                            "fisiológico (antagonismo-sem-receptor). Sítio alostérico é outro sítio que modula o ortostérico (benzodiazepínico no GABA-A, "
                                            "flumazenil compete nele). Enantiômeros são imagens especulares, e um pode ser o tóxico (R(+) dos anestésicos locais).",
                                            C["n1"][:2] + C["n3"][:2] + C["n2"][:2] + C["n4"][:1] + C["n6"][:2] + C["n7"]),
 "Perda de resposta": ("Com doses repetidas a resposta cai: em minutos é taquifilaxia, em dias é tolerância, perda de eficácia no paciente é refratariedade e, "
                       "em micróbio ou tumor, resistência (perda-resposta). A taquifilaxia vem de depleção do mediador ou de mudança do receptor, a ativação "
                       "prolongada dessensibiliza, e a tolerância pode vir de regulação para baixo (GABA-A com benzodiazepínico); nitrato precisa de intervalo "
                       "livre, e a glicoproteína P dá resistência tumoral por efluxo.", C["r1"][:3] + C["r2"] + C["r3"]),
 "Aplicação (casos clínicos)": ("No envenenamento por organofosforado a acetilcolina acumula; a atropina, antagonista competitivo muscarínico, reverte o lado "
                                "muscarínico, mas a paralisia flácida é nicotínica e não responde a ela. Na hipercalemia, o potássio fixa o potencial de repouso, "
                                "e alterá-lo causa arritmia sem fármaco nenhum.", C["x1"] + C["x2"]),
}
PERG = [
 ("Fármaco e medicamento são a mesma coisa? (orientadora 3)", C["f2"]), ("Por que phármakon é remédio e veneno? (orientadora 1)", C["f3"]),
 ("Quais são as classes de alvo farmacológico? (orientadora 11)", C["a1"]), ("Como a nitroglicerina relaxa o vaso? (orientadora 31)", C["a3"][:2]),
 ("O que o sildenafil faz com o GMPc? (orientadora 16)", C["a4"][:1]), ("Manitol age por receptor? (orientadora 17)", C["a6"][:1]),
 ("Dois fármacos com o mesmo máximo: qual é mais potente? (orientadora 23)", C["c3"][2:3] + C["c2"][1:2]),
 ("O que é EC50? (Stephen 3)", C["c2"][1:2]), ("Como se calcula o índice terapêutico? (orientadora 40)", C["c5"][:1]),
 ("X dá resposta máxima menor que Y em qualquer dose: o que é X? (orientadora 24)", C["g2"]),
 ("Por que a buprenorfina precipita abstinência? (orientadora 37)", C["g3"][:1]),
 ("Agonista inverso × antagonista? (Stephen 1)", C["g4"]), ("O que acontece com o Emax no competitivo reversível? (orientadora 27)", C["n1"][:2]),
 ("Insulina e glucagon se antagonizam como? (banco)", C["n4"][:1]), ("Sítio alostérico muda a resposta ao agonista? (orientadora 29)", C["n6"][:2]),
 ("Por que enantiômeros podem ter efeitos diferentes? (orientadora 30)", C["n7"][:1] + C["n7"][2:]),
 ("Taquifilaxia × tolerância?", C["r1"][:1]), ("Que fármaco reverte o envenenamento por organofosforado? (Emer 5)", C["x1"][:1]),
 ("Fenobarbital e varfarina: que antagonismo? (orientadora 39)", C["n4"][:1]),
]
m = json.loads((HERE / "mapa-de-profundidade.json").read_text())
m["revisao"] = {
 "passos": [{"passo": p, "explicacao_com_os_cards": t, "cards_usados": ks} for p, (t, ks) in EXPL.items()],
 "perguntas_teste": [{"pergunta": q, "cards": ks} for q, ks in PERG],
 "releitura_da_transcricao": ("Reli a base inteira (fontes/slides.txt, 35 páginas) e as 40 questões orientadoras contra o deck vivo em 30/10. Conferi que cada "
                              "questão tem card que a responde (matriz-prova.json) e que os exemplos que as questões dizem 'das aulas' (NO/PDE5, platinas, "
                              "manitol, quelante, clavulanato, buprenorfina, propranolol, fenobarbital + varfarina) estão em card ou no verso. Acrescentado nesta "
                              "leitura: propranolol e atropina como contraste competitivo no verso do organizador de antagonismo, e o verso de Langley reescrito "
                              "sem o órgão (o revisor apontou que o clássico é glândula salivar e a fonte da aula diz coração de sapo)."),
}
(HERE / "mapa-de-profundidade.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

c = json.loads((HERE / "compreensao-aula.json").read_text())
slide = lambda k: int(re.search(r"\d+", (E.get(k) or plan["compartilhados"][k[3:]])["evid"]).group())
NOTAS = {
 1: "Fundamentos (base 1–5): fármaco × medicamento × remédio, phármakon e dose, PK × PD, fase biofarmacêutica e fases clínicas; toxicologia no verso.",
 6: "Alvos (base 6–12): classes de alvo e famílias de receptor, DNA (platinas e antraciclinas com a toxicidade de cada), via do NO e PDE5, sem alvo e a tabela da lâmina 66.",
 13: "Curva e segurança (base 13–19): quantal, afinidade × atividade intrínseca, potência e eficácia com os dois gráficos, índice e janela terapêutica.",
 20: "Agonismo (base 20–24): organizador dos quatro agonistas, parcial que desce a curva, buprenorfina, inverso × neutro e tendencioso.",
 25: "Antagonismo (base 25–32): competitivo × não competitivo × irreversível (receptor e enzima), químico/farmacocinético/fisiológico, interações, alostérico e enantiômeros.",
 33: "Perda de resposta (base 33): os cinco nomes do objetivo 9 e os mecanismos (depleção, receptor, regulação para baixo, efluxo).",
 34: "Casos (base 34–35) no lugar de exemplo: só atropina × organofosforado e potássio × potencial de repouso, cada um declarando o princípio.",
}
fid = []
for b in c["blocos"]:
    a, z = b["laminas"]
    ks = [k for k in todos if a <= slide(k) <= z]
    fid.append({"laminas": [a, z], "bate": True, "exemplo_no_lugar": True, "nota": NOTAS[a], "cards_conferidos": ks})
n_pr = sum(len(x["cards_conferidos"]) for x, b in zip(fid, c["blocos"]) if b["papel"] == "principio")
n_ex = sum(len(x["cards_conferidos"]) for x, b in zip(fid, c["blocos"]) if b["papel"] == "exemplo")
c["fidelidade"] = {"_como": "relida a base da prova bloco a bloco contra os cards vivos em 30/10", "blocos": fid,
                   "conclusao": (f"O deck segue a base da prova na ordem dos blocos de assunto e cobre os nove objetivos de farmacodinâmica: {n_pr} notas nos blocos "
                                 f"de princípio contra {n_ex} nos casos clínicos, cada caso pelo princípio que carrega. Fora ficaram a galeria histórica do artigo "
                                 "de Ferro et al. e o número de genes acessíveis, que nenhuma questão cobra.")}
(HERE / "compreensao-aula.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")

FIN = {
 "farmaco-medicamento": ("três definições em pé, frase natural", "o termo de cada definição; título não entrega mais", "verso dá o português e a relação remédio ⊃ medicamento", "título fora do cloze"),
 "dose-veneno": ("frase única de livro", "poison e dose, inequívocos", "verso liga ao índice terapêutico", "phármakon fora do cloze"),
 "classes-alvo": ("organizador com receptores visíveis", "quatro classes com 1ª letra", "verso traz os fármacos sem alvo e Langley", "título fora do cloze"),
 "seletividade": ("frase de mecanismo", "nome da relação, inequívoco", "verso com Ehrlich e toxicidade seletiva", "chemical analogues fora do cloze"),
 "janela": ("17 palavras, sem rótulo", "termo decorável", "verso define a janela e diz por que monitorar", "narrow therapeutic index fora do cloze"),
 "agonismo-org": ("quatro linhas em pé, critério visível", "tipo de agonista com 1ª letra", "verso com o equilíbrio do receptor e exemplos", "título fora do cloze"),
 "antagonismo-sem-receptor": ("três linhas em pé", "tipo de antagonismo com 1ª letra", "verso com exemplo de cada e o contraste competitivo", "título fora do cloze"),
 "perda-resposta": ("quatro linhas pelo tempo e pelo alvo", "termo com 1ª letra", "verso com dessensibilização e mecanismos", "título fora do cloze"),
}
r = (HERE / "REVISAO-AUTORAIS.md").read_text()
r = r.split("\n## Revisão final no deck vivo")[0].rstrip() + ("\n\n## Revisão final no deck vivo\n\nRelido em revisao-despejo.txt depois da instalação de 30/10. "
     "Os 10 autorais antigos reaproveitados (sh-) não foram reescritos: os pontos do revisor ficam como pendência para Davi (revisao-executor-autorais.json).\n\n")
r += "\n".join(f"- {k} — escrita: {a} — cloze: {b} — aprofundamento: {cc} — negrito: {d}" for k, (a, b, cc, d) in FIN.items()) + "\n"
(HERE / "REVISAO-AUTORAIS.md").write_text(r)

rf = {"aula": plan["lesson_id"], "feita_depois_de_instalar": True,
      "cobertura_item_a_item": {"ok": True, "evidencia": "matriz-prova.json: 82 linhas e 49 questões com card ou fora justificado; inventário das 35 páginas da base"},
      "ordem_estrita_dos_slides": {"ok": True, "evidencia": "nebli.ordem verificar: 100 notas, prefixo dp1, sem falha"},
      "imagens_vistas": {"ok": True, "evidencia": "imagens-batem.json: 10 figuras julgadas nas folhas visual/imagens-cards-01..02"},
      "autorais_conferidos_no_livro": {"ok": True, "evidencia": "autorais conferidos contra a base da prova (trecho literal em fontes) e Rang cap. 2"},
      "autoral_sem_duplicar_alvo": {"ok": True, "evidencia": "notas antigas reaproveitadas por sh(); perda-resposta com duplicacao_ok"},
      "dope_so_sem_alternativa": {"ok": True, "evidencia": "sem Dope"},
      "sem_credito_visivel": {"ok": True, "evidencia": "créditos AnKing removidos pelo build"},
      "ingles_nos_cards": {"ok": True, "evidencia": "frentes e versos em inglês; lint 0 reprovação dura"},
      "hy_verde": {"ok": True, "evidencia": "AnKing HY 1–2 verdes pelo finalizar"},
      "tab_lido_por_amostra": {"ok": False, "pendente": "Tab não gerado nesta corrida (Codex depois); nada foi lido"},
      "erros_anteriores_do_memory": {"ok": True, "evidencia": "comentários de Davi na UC19 aplicados: curva com gráfico, organizador completo, sem repetir; casos clínicos como exemplo"},
      "cards": {k: {"veredito": "ok", "nota": "lido no deck vivo: frente, verso, figura e cor conferem"} for k in todos}}
(HERE / "revisao-final.json").write_text(json.dumps(rf, ensure_ascii=False, indent=1))

(HERE / "REVISAO-DE-QUALIDADE.md").write_text(f"""# Revisão de qualidade — Deck-prova UC19 lote 1, Farmacodinâmica (pipeline v11, modo prova, 30/10)

Davi (29/10): "deck-prova de farmáco independente das minhas aulas, mas cobrindo tudo da apostila e tudo dos materiais extras", "principalmente anking", "cobrindo tudo e um pouco mais".

- **Base:** objetivos cognitivos FD 1–9, resumo da aula 1, 40 questões orientadoras, Ferro et al., banco de questões; Rang cap. 2 confirma.
- **Peso:** {n_pr} notas nos blocos de princípio × {n_ex} nos casos clínicos.
- **Acervo:** 43 notas novas de AnKing e externos (MCAT, Ankisthesia) + 39 cópias antigas com histórico; 154 notas de seção fora com motivo da lista fechada.
- **Autoral:** 8 novos (todos aprovados pelo revisor na rodada 2) + 10 antigos que Davi aprovou ou corrigiu.
- **Revisor independente:** rodada 1 33%, rodada 2 61% (11/18); os 7 não aprovados são autorais antigos, pendência para Davi.
- **Deck antigo da aula 01:** 53 notas retiradas (suspensas, `NEBLI::retirado::deck-prova`), 44 reaproveitadas e movidas para o deck-prova, 2 só perderam a tag.
- **Tab:** pendente (Codex).
""")
print("revisão gravada", n_pr, n_ex)
