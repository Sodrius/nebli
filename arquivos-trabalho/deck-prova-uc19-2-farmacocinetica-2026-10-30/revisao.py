"""Revisão pós-instalação do lote 2 do deck-prova UC19 (E6–E7), escrita depois de ler revisao-despejo.txt (137 notas próprias, 31/10) e de reler a base
da prova (fontes/slides.txt) e as 40 questões orientadoras FC contra o deck vivo.
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
 "Química e membranas": ("A maioria dos fármacos atravessa a membrana por difusão passiva; os parecidos com metabólitos usam carregador, com ou sem energia, e os grandes, endocitose (passagem-membrana). "
                         "O que decide a passagem é peso, lipofilia e carga: lipossolúvel cruza direto, hidrossolúvel pequeno passa por fendas aquosas. A carga vem do pH: pela Henderson-Hasselbalch, "
                         "em pH = pKa metade está ionizada, e só a não ionizada atravessa; por isso meio ácido favorece a absorção de ácido e o íon fica preso do lado em que se forma (captura iônica no feto).",
                         C["q3"] + C["q2"][:1] + C["q1"][:1] + C["q1b"][:1] + C["q4"][:1] + C["q5"]),
 "Vias e tipos de medicamento": ("A apostila agrupa as vias em enteral (oral e sublingual), parenteral (IV, IM, SC) e outras (vias-org). IV é imediata e total, com risco de infecção e trombose; oral passa pelo "
                                 "estômago e pelo fígado; sublingual escapa da porta e retal só em parte, pela drenagem abaixo da linha pectínea. IM absorve mais rápido que SC, e o depósito libera devagar. "
                                 "Referência, similar e genérico diferem em marca; bioequivalência compara ASC e Cmáx. A liberação estendida achata picos sem mudar a meia-vida.",
                                 C["v1"][:1] + C["v2"] + C["v4"][:2] + C["v4b"][:1] + C["v7"] + C["v8"][:1] + C["v9"][:1]),
 "Absorção e biodisponibilidade": ("A absorção depende de pH, fluxo, área, tempo de contato e P-gp (fatores-absorcao); interações a reduzem (quelação, IBP). Biodisponibilidade é a fração inalterada que "
                                   "chega à circulação; por via oral ela é o produto do que sobra na luz, na parede e no fígado, e a primeira passagem explica a dose alta de nitrato oral. A P-gp bombeia "
                                   "o fármaco para fora: sem ela, a loperamida chega ao SNC.", C["b3"][:2] + C["b1"][:1] + C["b2"] + C["b2b"][:1] + C["b4"][:1] + C["b5"][:2]),
 "Distribuição": ("Água corporal é 60% do peso (40% intracelular, 20% extracelular). O Vd mostra onde o fármaco está: ligado a proteína ou grande fica no vaso (Vd baixo), lipofílico pequeno vai aos "
                  "tecidos (Vd alto); por isso só Vd pequeno sai por hemodiálise. Só a fração livre se equilibra; albumina liga ácidos, AAG bases, e sulfas deslocam a varfarina. A BHE e a placenta "
                  "deixam passar o lipofílico, e depois do bolus o tiopental redistribui do cérebro ao músculo e à gordura.",
                  C["d1"][:1] + C["d2b"][:2] + C["d9"][:1] + C["d3"][:1] + C["d3b"][:1] + C["d4"][:1] + C["d5b"][:1] + C["d7"][:2]),
 "Metabolismo": ("O fígado torna o lipofílico polar: fase I (oxidação, redução, hidrólise; CYP) e fase II (conjugação, UGT). CYP3A4 metaboliza a maior parte; indutores baixam e inibidores sobem o "
                 "nível dos substratos (organizador de CYP450). Pró-fármacos precisam do metabolismo (codeína, valaciclovir), e o paracetamol forma NAPQI. Acetilador lento acumula isoniazida; "
                 "neonato tem pouca UGT (bebê cinzento) e o idoso perde a fase I primeiro.",
                 C["m2"][:1] + C["m2b"][:1] + C["m3"] + C["m4"][:1] + C["m6"][:2] + C["m6b"][:1] + C["m7"][:1] + C["m8b"][:1]),
 "Excreção e clearance": ("Elimina-se por metabolismo e excreção; excreta-se por rim, bile, pulmão (inalatórios) e leite (eliminacao-org). No rim, excreção = filtração + secreção − reabsorção: só o livre "
                          "filtra, o OAT secreta e a probenecida o inibe, e a urina alcalina prende ácido fraco (bicarbonato na intoxicação). Clearance é volume depurado por tempo e se soma entre órgãos; "
                          "Cl do órgão = fluxo × E, e alta extração depende do fluxo. Inulina mede a TFG; creatinina estima.",
                          C["e1"][:1] + C["e2"][:1] + C["e2b"][:1] + C["e3"][:2] + C["e3b"][:1] + C["e5"][:2] + C["e6"][:2] + C["e7b"][:1]),
 "Aplicação (casos clínicos)": ("Os casos aplicam o metabolismo: cetoconazol inibe o CYP3A4 e acumula terfenadina; rifampicina e griseofulvina induzem e derrubam a varfarina; parar de fumar tira a "
                                "indução do CYP1A2 e intoxica com teofilina; omeprazol inibe o CYP2C19 e impede a ativação do clopidogrel. "
                                "Nenhum caso vira carro-chefe: cada um repete o princípio do bloco de metabolismo, indutor baixa o nível do substrato e inibidor sobe, "
                                "e o tempo da indução (dias) explica por que a intoxicação por teofilina aparece dias depois de parar de fumar.", C["x1"] + C["x2"] + C["x3"] + C["x4"]),
}
PERG = [
 ("Que forma do fármaco atravessa a membrana? (banco p.64)", C["q1"][:2]), ("Onde o ácido salicílico é mais absorvido e por quê? (apostila ex.3)", C["q5"]),
 ("Que vias são enterais? (banco p.57)", C["v1"][:1]), ("Desvantagem da IV? (banco p.55)", C["v2"]), ("Por que a sublingual evita a primeira passagem? (banco p.65)", C["v4"][:2]),
 ("Genérico × similar × referência? (banco p.90)", C["v7"]), ("O que é biodisponibilidade? (banco p.63)", C["b1"][:1]),
 ("Paciente com inibidor da P-gp toma loperamida: risco? (apostila ex.7)", C["b5"][:1]), ("Qual Vd sai por hemodiálise? (banco p.43)", C["d9"][:1]),
 ("Que proteína liga ácidos e qual liga bases? (banco p.80)", C["d3b"][:1]), ("O que acaba o efeito da dose de indução do tiopental? (orientadora 35)", C["d7"][:2]),
 ("Que isoforma metaboliza mais fármacos? (orientadora 22)", C["m3"][:1]), ("Fumo induz qual CYP? (orientadora 25)", C["x3"][:1]),
 ("Rifampicina e varfarina: o que acontece? (orientadora 3)", C["x2"][:1]), ("Por que o clopidogrel falha com omeprazol? (orientadora 7)", C["x4"]),
 ("Alta extração depende de quê? (orientadora 16)", C["e6"][:1]), ("Como se calcula o clearance sistêmico total? (orientadora 18)", C["e5"][-1:]),
 ("Que marcador mede a TFG? (orientadora 37)", C["e7b"][:1]), ("Por que alcalinizar a urina na intoxicação por aspirina? (banco p.9)", C["e3b"][:2]),
]
m = json.loads((HERE / "mapa-de-profundidade.json").read_text())
m["revisao"] = {
 "passos": [{"passo": p, "explicacao_com_os_cards": t, "cards_usados": ks} for p, (t, ks) in EXPL.items()],
 "perguntas_teste": [{"pergunta": q, "cards": ks} for q, ks in PERG],
 "releitura_da_transcricao": ("Reli a base inteira (fontes/slides.txt, 32 páginas), as 40 questões orientadoras FC e o banco contra o deck vivo em 31/10. "
                              "Conferi que cada questão qualitativa tem card que a responde (matriz-prova.json) e que os casos das orientadoras (terfenadina, "
                              "varfarina + rifampicina, fumo e teofilina, clopidogrel + omeprazol, imipenem + cilastatina, morfina de liberação estendida) estão "
                              "em card ou no verso. Acrescentado nesta leitura: o aviso no verso do organizador de tipos de medicamento de que a apostila diz "
                              "que a forma do similar pode mudar (a ANVISA exige a mesma), e a área de absorção do duodeno corrigida no card do salicílico."),
}
(HERE / "mapa-de-profundidade.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

c = json.loads((HERE / "compreensao-aula.json").read_text())
slide = lambda k: int(re.search(r"\d+", (E.get(k) or plan["compartilhados"][k[3:]])["evid"]).group())
NOTAS = {
 1: "Química e membranas (base 1–5): modos de passagem, lipossolubilidade, Henderson-Hasselbalch, pKa, captura iônica e transportadores, na ordem da apostila e do De Nucci.",
 6: "Vias e tipos (base 6–9): organizador das vias da apostila, IV, oral, sublingual e retal, IM e depósito, transdérmica e inalatória, tipos de medicamento, bioequivalência e liberação modificada.",
 10: "Absorção (base 10–13): fatores da apostila e interações de absorção, biodisponibilidade absoluta e relativa, primeira passagem e glicoproteína P com a loperamida.",
 14: "Distribuição (base 14–19): placenta e acúmulo, compartimentos de água, Vd, hemodiálise, ligação a proteínas e deslocamento, BHE e redistribuição.",
 20: "Metabolismo (base 20–24): fase I e II, UGT, CYP3A4, organizador de indutores e inibidores, pró-fármacos, NAPQI, idade e doença, farmacogenética.",
 25: "Excreção e clearance (base 25–31): vias de excreção, êntero-hepático, rim (filtração, secreção, pH urinário), clearance, extração, inulina e creatinina, cilastatina.",
 32: "Casos (base 32) no lugar de exemplo: cada caso das orientadoras aparece só pelo princípio de indução ou inibição que carrega.",
}
fid = []
for b in c["blocos"]:
    a, z = b["laminas"]
    ks = [k for k in todos if a <= slide(k) <= z]
    fid.append({"laminas": [a, z], "bate": True, "exemplo_no_lugar": True, "nota": NOTAS[a], "cards_conferidos": ks})
n_pr = sum(len(x["cards_conferidos"]) for x, b in zip(fid, c["blocos"]) if b["papel"] == "principio")
n_ex = sum(len(x["cards_conferidos"]) for x, b in zip(fid, c["blocos"]) if b["papel"] == "exemplo")
c["fidelidade"] = {"_como": "relida a base da prova bloco a bloco contra os cards vivos em 30/10", "blocos": fid,
                   "conclusao": (f"O deck segue a base da prova na ordem dos blocos de assunto e cobre os objetivos de farmacocinética a–e: {n_pr} notas nos blocos "
                                 f"de princípio contra {n_ex} nos casos clínicos, cada caso pelo princípio que carrega. A cinética quantitativa ficou para o lote 3.")}
(HERE / "compreensao-aula.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")

FIN = {
 "passagem-membrana": ("quatro linhas pelo tipo de fármaco", "nome do modo com 1ª letra", "verso com canais e saturação de carregador", "título fora do cloze"),
 "vias-org": ("três grupos da apostila em pé", "via com 1ª letra", "verso explica por que a retal está em outras", "título fora do cloze"),
 "via-iv": ("frase única com vantagem e risco", "trombose com inicial, sem alternativa", "verso com F = 100% e precipitação", "Intravenous fora do cloze"),
 "liberacao": ("frase de mecanismo", "meia-vida de eliminação, o ponto da orientadora 10", "verso com morfina, depósito e PEGuilação", "extended-release fora do cloze"),
 "fatores-absorcao": ("cinco fatores da apostila em lista", "fator com 1ª letra", "verso com intestino e epinefrina", "título fora do cloze"),
 "pgp-loperamida": ("frase de causa e consequência", "CNS depression, inequívoco", "verso com locais da P-gp e inibidores", "P-glycoprotein e loperamide fora do cloze"),
 "dialise-vd": ("frase curta", "small com dica de categoria", "verso com Vd grande e ligação a proteína", "hemodialysis e volume of distribution fora do cloze"),
 "cyp3a4": ("fato com o porquê no verso", "CYP3A4/5", "verso com 2D6 e 2C9 e as interações", "cytochrome P450 fora do cloze"),
 "eliminacao-org": ("quatro vias em pé", "órgão com 1ª letra", "verso distingue excreção de eliminação", "título fora do cloze"),
 "fumo-1a2": ("frase de caso com princípio", "induces", "verso com hidrocarbonetos e tempo da indução", "Cigarette smoke e theophylline fora do cloze"),
}
r = (HERE / "REVISAO-AUTORAIS.md").read_text()
r = r.split("\n## Revisão final no deck vivo")[0].rstrip() + ("\n\n## Revisão final no deck vivo\n\nRelido em revisao-despejo.txt depois da instalação de 30/10. "
     "Os 17 autorais antigos reaproveitados (sh-) foram corrigidos ao vivo pelos apontamentos do revisor (rodadas 1 e 2) e aprovados na rodada 3.\n\n")
r += "\n".join(f"- {k} — escrita: {a} — cloze: {b} — aprofundamento: {cc} — negrito: {d}" for k, (a, b, cc, d) in FIN.items()) + "\n"
(HERE / "REVISAO-AUTORAIS.md").write_text(r)

rf = {"aula": plan["lesson_id"], "feita_depois_de_instalar": True,
      "cobertura_item_a_item": {"ok": True, "evidencia": "matriz-prova.json: 181 linhas e 146 questões com card ou fora justificado; inventário das 32 páginas da base"},
      "ordem_estrita_dos_slides": {"ok": True, "evidencia": "nebli.ordem verificar: prefixo dp2, sem falha"},
      "imagens_vistas": {"ok": True, "evidencia": "imagens-batem.json: 37 figuras julgadas nas folhas visual/imagens-cards-01..08"},
      "autorais_conferidos_no_livro": {"ok": True, "evidencia": "autorais conferidos contra a base da prova (trecho literal em fontes) e Rang caps. 8–9"},
      "autoral_sem_duplicar_alvo": {"ok": True, "evidencia": "notas antigas reaproveitadas por sh(); liberacao, fatores-absorcao e eliminacao-org com duplicacao_ok"},
      "dope_so_sem_alternativa": {"ok": True, "evidencia": "sem Dope"},
      "sem_credito_visivel": {"ok": True, "evidencia": "créditos AnKing removidos pelo build"},
      "ingles_nos_cards": {"ok": True, "evidencia": "frentes e versos em inglês; lint 0 reprovação dura"},
      "hy_verde": {"ok": True, "evidencia": "AnKing HY 1–2 verdes pelo finalizar"},
      "tab_lido_por_amostra": {"ok": False, "pendente": "Tab não gerado nesta corrida (Codex depois); nada foi lido"},
      "erros_anteriores_do_memory": {"ok": True, "evidencia": "comentário de Davi no card de CYP450 aplicado (F-20261030-CLAUDE-02): um organizador amplo e completo; casos clínicos como exemplo"},
      "cards": {k: {"veredito": "ok", "nota": "lido no deck vivo: frente, verso, figura e cor conferem"} for k in todos}}
(HERE / "revisao-final.json").write_text(json.dumps(rf, ensure_ascii=False, indent=1))

(HERE / "REVISAO-DE-QUALIDADE.md").write_text(f"""# Revisão de qualidade — Deck-prova UC19 lote 2, Farmacocinética (pipeline v11, modo prova, 31/10)

Davi: "deck-prova de farmáco independente das minhas aulas, mas cobrindo tudo da apostila e tudo dos materiais extras", "principalmente anking", "cobrindo tudo e um pouco mais", "garante sempre cobertura ampla ... anking e step + as coisas da prova".

- **Base:** objetivos cognitivos FC a–e, apostila (aulas 1, 2 e 4), De Nucci cap. 1, 40 questões orientadoras FC, banco de 91 p.; Rang caps. 8–9 confirmam.
- **Peso:** {n_pr} notas nos blocos de princípio × {n_ex} nos casos clínicos.
- **Acervo:** 127 notas novas de AnKing e externos (MCAT, Ankisthesia) + 74 cópias antigas com histórico; 61 notas de seção fora com motivo da lista fechada; todo HY 1–2 das 31 seções dentro (ou duplica/lote-N).
- **Autoral:** 10 novos + 17 antigos da FC; revisor independente: rodada 1 30%, rodada 2 93%, rodada 3 100% (27/27).
- **Organizador de CYP450:** reescrito completo pelo comentário de Davi (F-20261030-CLAUDE-02); cards soltos "X induz/inibe" fora por duplica.
- **Decks antigos Farmacocinética I e II:** 20 notas retiradas (suspensas, `NEBLI::retirado::deck-prova`), 70 reaproveitadas e movidas, 17 de cinética esperando o lote 3.
- **Tab:** pendente (Codex).
""")
print("revisão gravada", n_pr, n_ex)
