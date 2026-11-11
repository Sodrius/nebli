"""Gera os artefatos da E3 a partir de plano.py e compreensao-aula.json."""
import json
from pathlib import Path
import plano

HERE = Path(__file__).parent
# marcadores sh-* do plano → notas vivas já instaladas (Anatomia 01 e 03), associadas sem repetir
SH = {
 "sh-cerebro-partes": ["sh-1792697125350"], "sh-id-diencefalo": ["sh-1792572870657"], "sh-id-cerebro": ["sh-1792572870656"],
 "sh-id-ventriculo-lateral": ["sh-1792572870704"], "sh-id-corpo-caloso": ["sh-1792572870701"], "sh-id-talamo": ["sh-1792572870651"],
 "sh-id-hipotalamo": ["sh-1793966747232"], "sh-id-capsula-interna": ["sh-1792572870678"], "sh-id-sulco-central": ["sh-1792572870708"],
 "sh-id-lobo-frontal": ["sh-1792572870660"], "sh-id-lobo-parietal": ["sh-1793966747229"], "sh-id-lobo-occipital": ["sh-1793966747231"],
 "sh-id-lobo-temporal": ["sh-1793966747230"], "sh-id-insula": ["sh-1792572870662"], "sh-broca-local": ["sh-1793966747239"],
 "sh-broca-afasia": ["sh-1793889229460"],
}
EXTRA_SH = {}


def chaves(item):
    out = []
    for k in item[6]:
        out += SH.get(k, [k])
    return out + EXTRA_SH.get(item[1], [])


def main():
    comp = json.loads((HERE / "compreensao-aula.json").read_text())
    blocos = comp["blocos"]
    bloco_de = lambda u: next(b for b in blocos if b["laminas"][0] <= u <= b["laminas"][1])
    # ---- mapa ----
    passos = []
    for b in blocos:
        its = [i for i in plano.ITENS if b["laminas"][0] <= i[0] <= b["laminas"][1]]
        if not its:
            continue
        passos.append({"passo": b["titulo"], "laminas": b["laminas"], "itens": [
            {"id": i[1], "tipo": i[2], "o_que": i[3], "fonte": f"unidade {i[0]}; {i[4]}", "termos": i[5], "cards": chaves(i)} for i in its]})
    basicos = []
    for i in plano.ITENS:
        for k in chaves(i):
            if k.startswith("id-"):
                basicos.append({"alvo": k[3:].replace("-", " "), "fonte": f"unidade {i[0]}; {i[4]}", "cards": [k], "estado": "agora",
                                "modalidade": "identificacao", "kenhub_disponivel": True})
    mapa = {"objetivos_da_aula": comp["o_que_a_aula_ensina"],
            "cronograma": {"aulas_vizinhas": ["01 Construção morfofuncional (13/10)", "03 Medula, tronco, nervos cranianos e cerebelo (14/10)", "05 Fisiologia: sistemas neurovegetativos (03/11)",
                                               "06 Meninges, ventrículos e líquor (04/11)", "07 Cortes seriados (04/11)", "08 Sistema límbico e 09 Córtex (18/11)"],
                           "conferido": "Cronograma 2026 UC07 lido; AN01 (148 notas) e AN03 lidas para associar em vez de repetir; funções detalhadas de núcleos, sistema límbico, áreas corticais e síndromes vasculares ficam nas aulas próprias."},
            "passos": passos,
            "fora": [{"o_que": "Funções detalhadas dos núcleos do tálamo e do hipotálamo, vias e conexões", "motivo": "o professor remete à fisiologia ('vocês vão ter a fisiologia… eles vão falar desses núcleos')"},
                     {"o_que": "Circuito do sistema límbico (habênula, núcleos anteriores, úncus)", "motivo": "outra aula: 08 Sistema límbico (18/11)"},
                     {"o_que": "Áreas de Brodmann e mapas corticais além das áreas motora, somestésica, de Broca e visual", "motivo": "outra aula: 09 Organização morfofuncional do córtex (18/11)"},
                     {"o_que": "Circuitos dos núcleos da base (vias direta e indireta)", "motivo": "fisiologia; a aula é topografia dos núcleos"},
                     {"o_que": "Veias, seios venosos e barreiras encefálicas", "motivo": "o professor restringe a aula à irrigação arterial ('não é vascularização'); seios na aula 06"},
                     {"o_que": "Ventrículos, forame interventricular e circulação do líquor", "motivo": "outra aula: 06 Meninges, ventrículos e líquor"}],
            "extras_fora_da_aula": [],
            "uc07_basico_e_destino": {"basicos": basicos, "destinos_an01": plano.DESTINO_AN01}}
    (HERE / "mapa-de-profundidade.json").write_text(json.dumps(mapa, ensure_ascii=False, indent=1))
    # ---- inventário (SLIDES) ----
    titulos = {}
    for line in (HERE / "fontes" / "slides.txt").read_text().split("===== página ")[1:]:
        n, rest = line.split(" =====\n", 1)
        titulos[int(n)] = rest.split("\n", 1)[0]
    slides = []
    for u in range(1, 63):
        its = [i for i in plano.ITENS if i[0] == u]
        if u in plano.REPETICAO:
            slides.append((u, "repeticao", f"Unidade {u}: {titulos[u]}", []))
        else:
            slides.append((u, "conteudo", f"Unidade {u}: {titulos[u]}", [(i[1], i[3], chaves(i)) for i in its]))
    inv = (HERE / "inventario.py").read_text().split("SLIDES = [")[0]
    inv = inv.replace('"<curto>"', '"u7an04"').replace('"<Aula (UC Pn; professor)>"', '"UC07 Anatomia 04 — diencéfalo, núcleos da base, telencéfalo e irrigação (27/10/2026; Jacomo)"')
    body = "SLIDES = " + json.dumps(slides, ensure_ascii=False, indent=0) + "\nJUSTIFICATIVAS = {}\nFIGURA_SEM_CARD = {}\n"
    body += 'CAPITULO = [("Machado 3ed cap6, 7 e 9", [])]\nEXERCICIOS = [("Provas UC07: não localizadas (Davi 05/11)", []), ("Apostila guia aulas 4 e 6", []), ("Manuscrito dos veteranos p10–32", [])]\n'
    (HERE / "inventario.py").write_text(inv + body)
    # ---- motivações ----
    razoes = {"explicar": "Sem a causa, o nome vira decoreba que se perde; com ela Davi reconstrói a anatomia e prevê a consequência clínica nas aulas seguintes.",
              "e-se": "É a pergunta que a clínica topográfica faz (qual artéria, qual área, onde está a lesão); saber prever é o que dura além da prova.",
              "distinguir": "São vizinhos que se confundem na peça e na prova; o critério que separa precisa ser recuperado junto com os nomes.",
              "organizar": "O conjunto é cobrado como tabela/mapa; recuperar a composição inteira evita lembrar itens soltos sem lugar.",
              "decorar": "É marco anatômico que o médico usa para se orientar no SNC e nas imagens; precisa ser reconhecido de imediato."}
    mot = {"motivacoes": [{"id": f"m-{i[1]}", "item_mapa": i[1], "reconstruir": i[3], "por_que_dura": razoes[i[2]], "depois_de": "",
                           "atendida_por": []} for i in plano.ITENS]}
    (HERE / "motivacoes.json").write_text(json.dumps(mot, ensure_ascii=False, indent=1))
    print(len(passos), "passos;", sum(len(p["itens"]) for p in passos), "itens;", len(basicos), "identificações;", len(slides), "unidades")


if __name__ == "__main__":
    main()
