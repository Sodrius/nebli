"""Gerador único das evidências do lote 2 do deck-prova UC19 (Farmacocinética), como na 61 v3: um script a partir do spec e do plano.
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
 "passagem-membrana": ("parcial", "Modos de atravessar a membrana", "o acervo tem difusão lipossolúvel e fendas aquosas em cards de capilar e GLUT como fisiologia; nenhum reúne os modos de absorção do fármaco como a apostila p.14 e o banco (p.62, p.74) cobram", ORGZ),
 "vias-org": ("lacuna", "Vias enterais, parenterais e outras", "o acervo só define vias soltas (MCAT: transdérmica, IM) e cita a via de fármacos específicos; nenhum agrupa enteral × parenteral × outras como a apostila, e o banco (p.57) cobra que enteral é oral + sublingual", ORGZ),
 "via-iv": ("lacuna", "Vantagens e riscos da via IV", "nenhum card dá a absorção imediata e o risco de trombose local e infecção da IV; os candidatos são reações de infusão de fármacos específicos", FATO),
 "liberacao": ("parcial", "Liberação prolongada muda a absorção", "o acervo tem glargina de ação longa e PEGuilação que prolonga a meia-vida; nenhum diz que a forma de liberação estendida muda a absorção sem mudar a meia-vida de eliminação (orientadora 10)", MEC),
 "fatores-absorcao": ("parcial", "Fatores da absorção", "o acervo tem fatores soltos (esvaziamento gástrico, quelação, IBP); nenhum lista os fatores da apostila p.14 (pH, fluxo, área, tempo de contato, P-gp)", ORGZ),
 "pgp-loperamida": ("parcial", "Inibir a P-gp põe a loperamida no SNC", "o acervo diz que a loperamida não cruza a BHE e onde fica a P-gp; nenhum liga a inibição da P-gp à depressão do SNC pela loperamida (apostila ex.7, banco p.3)", MEC),
 "dialise-vd": ("lacuna", "Hemodiálise só remove Vd pequeno", "o acervo tem o mnemônico dos dialisáveis, sem o princípio; nenhum card liga a hemodiálise ao Vd, que o banco cobra três vezes", MEC),
 "cyp3a4": ("lacuna", "CYP3A4 metaboliza a maior parte", "o acervo lista substratos e inibidores de várias isoformas; nenhum diz qual metaboliza a maior parte dos fármacos (orientadora 22)", FATO),
 "eliminacao-org": ("lacuna", "Vias de excreção", "o acervo tem a excreção renal e casos de bile e pulmão em anestesia; nenhum lista as vias de excreção do objetivo FC e.ii", ORGZ),
 "fumo-1a2": ("lacuna", "Fumo induz CYP1A2 (teofilina)", "o acervo diz que a teofilina passa pelo CYP e que macrolídeos a elevam; nenhum card diz que o fumo induz CYP1A2 (orientadoras 5 e 25)", MEC),
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
rev = ["# Revisão dos autorais — Deck-prova UC19 lote 2, Farmacocinética (pipeline v11, modo prova, 30/10)", "",
       "Leitura obrigatória v10 inteira, GUIAS 1–3 relidos em 30/10 e comentários de Davi nos cards UC19 lidos (curva com gráfico, deslocamento da "
       "curva em vez de definição solta, lista completa num organizador, nada repetido). Cada autoral nasce de uma motivação congelada na E3 e só "
       "existe onde o acervo não tem o item da prova; os autorais antigos que Davi aprovou ou corrigiu voltam por sh() com o histórico.", "",
       "Organizadores necessários: sim — a apostila e os objetivos listam conjuntos (modos de atravessar a membrana, vias, fatores da absorção, "
       "vias de excreção) e o banco cobra a distinção entre eles.", "",
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
 {"principio": "Um indutor enzimático aumenta o metabolismo de outro fármaco e reduz seu nível e efeito; retirar o indutor faz o nível subir.",
  "cards": CARDS["x2"] + CARDS["x3"]},
 {"principio": "Um inibidor enzimático reduz o clearance metabólico de outro fármaco ou impede a ativação de um pró-fármaco.",
  "cards": CARDS["x1"] + CARDS["x4"]}]
casos["cards_exemplo"] = []  # os cards dos casos ficam ligados pelos princípios ilustrados
REC = {0: CARDS["e3"][:4] + CARDS["q4"][:1], 1: CARDS["m4"][:3] + CARDS["m5"][:3] + CARDS["x2"][:1], 2: CARDS["e6"][:4], 3: CARDS["d9"] + CARDS["d2c"]}
for i, ks in REC.items():
    c["reconstrucoes"][i]["cards"] = ks
(HERE / "compreensao-aula.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"autorais {len(A)}; cobertura {len(linhas) - 1} linhas; imagens {len(IB)}")
