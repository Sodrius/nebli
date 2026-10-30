"""Gerador único das evidências do lote 1 do deck-prova UC19 (Farmacodinâmica), como na 61 v3: um script a partir do spec e do plano.
Escreve: busca/cobertura.tsv, decisoes.json, REVISAO-AUTORAIS.md (moldagem), imagens-batem.json e, em compreensao-aula.json,
principios_ilustrados do bloco de casos e os cards das reconstruções. Tudo o que é julgamento está escrito aqui, card a card.
    /usr/bin/python3 planejar.py && /usr/bin/python3 evidencias.py
"""
import json
import re
import runpy
from pathlib import Path

HERE = Path(__file__).parent
plan = json.loads((HERE / "plan.json").read_text())
E = {e["key"]: e for e in plan["entries"]}
SH = {f"sh-{k}": v for k, v in (plan.get("compartilhados") or {}).items()}
TODOS = list(E) + list(SH)
CARDS = runpy.run_path(str(HERE / "planejar.py"))["CARDS"]
cloze1 = lambda t: re.sub(r"<[^>]+>", "", re.search(r"\{\{c\d+::(.*?)(::|\}\})", t).group(1)).strip()

# ---------- autorais: lacuna, molde (EXEMPLAR × ANTI dos GUIAS 2 e 3) ----------
MEC, CON, ORGZ, FATO = ("1791631347467", "1791627549152"), ("1792166970014", "1791023819869"), ("1792166969765", "1792624459224"), ("1791023354943", "1791629587772")
A = {  # chave: (veredito, conceito, por que o acervo não cobre, molde)
 "farmaco-medicamento": ("lacuna", "Fármaco × medicamento × remédio", "o acervo não tem a distinção (é vocabulário da farmacologia brasileira); os candidatos falam de formulação de um fármaco específico ou de eficácia", ORGZ),
 "dose-veneno": ("lacuna", "Phármakon e a dose de Paracelso", "nenhum card de origem do termo nem da frase de Paracelso; os candidatos são de envenenamentos específicos", FATO),
 "classes-alvo": ("parcial", "Cinco classes de alvo", "o acervo tem exemplos de cada alvo (canais, transportadores, DNA) em cards soltos; nenhum agrupa as classes como a aula e as questões 6 e 11 pedem", ORGZ),
 "seletividade": ("lacuna", "Especificidade pela relação estrutura-atividade", "nenhum card de relação estrutura-atividade nem de toxicidade seletiva (Ehrlich); os candidatos são de toxicidade de fármacos específicos", MEC),
 "janela": ("parcial", "IT estreito → janela estreita", "o acervo dá a fórmula do IT e os fármacos de IT estreito; nenhum define janela terapêutica nem a liga ao IT (objetivo FD 4)", MEC),
 "agonismo-org": ("parcial", "Quatro tipos de agonista pelo efeito no receptor", "o acervo tem parcial × pleno; não tem agonista inverso nem tendencioso, e nenhum card organiza os quatro como o objetivo FD 5", ORGZ),
 "antagonismo-sem-receptor": ("lacuna", "Antagonismo químico, farmacocinético e fisiológico", "nenhum card define os três tipos (só exemplos soltos, como dimercaprol e indutores de CYP); a orientadora 39 e o banco cobram", ORGZ),
 "perda-resposta": ("parcial", "Cinco nomes da perda de resposta", "o acervo tem taquifilaxia, tolerância e resistência em cards soltos; nenhum define refratariedade nem organiza os cinco termos do objetivo FD 9", ORGZ),
}
assert set(A) == {k for k, e in E.items() if e.get("origin") == "Autoral"}, set(A) ^ {k for k, e in E.items() if e.get("origin") == "Autoral"}

SEM = {json.loads(l)["chave"]: [str(h["nid"]) for h in json.loads(l)["top"]] for l in (HERE / "busca/semantica.jsonl").read_text().splitlines()}
linhas = ["chave\tconceito\tfonte_aula\tveredito\tlidos\tdecora\tdecisao"]
dec = {}
for k in TODOS:
    e = E.get(k)
    if e and e.get("origin") == "Autoral":
        v, conc, porque, _ = A[k]
        lidos = ",".join(SEM.get(k, [])[:5])
        txt = ("Busca nos três caminhos (seções de recurso de farmacologia geral; palavra-chave com sinônimos em AnKing e externos; significado em "
               f"todos os acervos e no NEBLI vivo): {porque}. O card atende a motivação {e.get('motivacao')} e a fonte base citada.")
        linhas.append(f"{k}\t{conc}\t{e['motivo'].split(': ', 1)[-1]}\t{v}\t{lidos}\t{cloze1(e['fields']['Text'])}\t{txt}")
        dec[k] = [v, txt]
    else:
        x = e or SH[k]
        linhas.append(f"{k}\t{x.get('alvo', '')}\t{x.get('evid')}\tcoberto\t{x.get('src', x.get('source_nid', ''))}\t-\tacervo cobre o item da prova; entra "
                      + ("por cópia NEBLI viva (histórico preservado)" if k in SH else "como cópia do acervo"))
(HERE / "busca/cobertura.tsv").write_text("\n".join(linhas) + "\n", encoding="utf-8")
(HERE / "decisoes.json").write_text(json.dumps(dec, ensure_ascii=False, indent=1), encoding="utf-8")

nome = {MEC: ("mecanismo com consequência (HDAC)", "card solto sem processo (domínio de ativação)"),
        CON: ("contraste no mesmo índice (autoimune × autoinflamatória)", "resposta por oposição (peristalse)"),
        ORGZ: ("organizador em pé com critério visível (como o sistema imune falha)", "organizador com classificação sem fonte (ordem de perfusão)"),
        FATO: ("fato decorável com contexto e verso com ganho (submandibular)", "cloze genérico (apoptosis → negative selection)")}
rev = ["# Revisão dos autorais — Deck-prova UC19 lote 1, Farmacodinâmica (pipeline v11, modo prova, 30/10)", "",
       "Leitura obrigatória v10 inteira, GUIAS 1–3 relidos em 30/10 e comentários de Davi nos cards UC19 lidos (curva com gráfico, deslocamento da "
       "curva em vez de definição solta, lista completa num organizador, nada repetido). Cada autoral nasce de uma motivação congelada na E3 e só "
       "existe onde o acervo não tem o item da prova; os autorais antigos que Davi aprovou ou corrigiu voltam por sh() com o histórico.", "",
       "Organizadores necessários: sim — os objetivos cognitivos listam conjuntos (fármaco/medicamento/remédio, classes de alvo, tipos de agonista, "
       "tipos de antagonismo, nomes da perda de resposta) e as questões cobram a distinção entre eles.", "",
       "## Moldagem (antes de instalar)", ""]
for k, (_, _, _, molde) in A.items():
    rev.append(f"- {k} — par: EXEMPLAR {molde[0]} ({nome[molde][0]}) × ANTI {molde[1]} ({nome[molde][1]}) — decora: {cloze1(E[k]['fields']['Text'])} — ok")
(HERE / "REVISAO-AUTORAIS.md").write_text("\n".join(rev) + "\n", encoding="utf-8")

# ---------- imagens (vistas em 30/10 pela folha de imagens) ----------
IB = json.loads((HERE / "imagens-vistas-cards.json").read_text(encoding="utf-8")) if (HERE / "imagens-vistas-cards.json").exists() else {}
(HERE / "imagens-batem.json").write_text(json.dumps({k: {"veredito": "ok", "porque": v} for k, v in IB.items()}, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- compreensão: princípios dos casos e reconstruções ----------
c = json.loads((HERE / "compreensao-aula.json").read_text(encoding="utf-8"))
casos = next(b for b in c["blocos"] if b["papel"] == "exemplo")
casos["principios_ilustrados"] = [
 {"principio": "Excesso de acetilcolina num envenenamento é revertido por antagonista competitivo muscarínico (atropina), que ocupa o receptor sem ativá-lo; a placa motora, nicotínica, não responde.",
  "cards": CARDS["x1"]},
 {"principio": "A concentração extracelular de potássio fixa o potencial de repouso; alterá-la muda a excitabilidade cardíaca e causa arritmia sem fármaco nenhum.",
  "cards": CARDS["x2"]}]
casos["cards_exemplo"] = []  # os cards dos casos ficam ligados pelos princípios ilustrados
REC = {0: CARDS["c3"] + CARDS["c2"], 1: CARDS["g3"], 2: CARDS["n1"][:2] + CARDS["n3"][:2] + CARDS["n2"][:1], 3: CARDS["a3"] + CARDS["a4"][:1],
       4: CARDS["n4"][:1] + CARDS["n5"][:1]}
for i, ks in REC.items():
    c["reconstrucoes"][i]["cards"] = ks
(HERE / "compreensao-aula.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"autorais {len(A)}; cobertura {len(linhas) - 1} linhas; imagens {len(IB)}")
