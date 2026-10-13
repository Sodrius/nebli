"""Inventário atômico da aula (todas as 61 lâminas) e planejamento por alvo — escrito ANTES de selecionar os cards.

Fontes lidas antes: slides (61, folhas visual/folha-01..11), apresentação complementar do Prof. Benedito Correa
(fontes/transcricao.pdf, que no Drive se chama 'transcrição' mas é outra apresentação), monitoria P2/P3, apostila de
veteranos (Microbiologia, aula 8), Trabulsi cap. 64.1–64.2, provas UC03 (2015–2025, índice + PDFs), Professor Dave
(3 vídeos), Physeo, Strong Medicine e Ninja Nerd (antifúngicos). Gera inventario-aula.json e planejamento.json.

Item: (id, texto, destino) — destino é a chave do card no spec, ou "EXC: motivo" (só lâmina ilustrativa/curiosidade).
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
EXC = "EXC:"

SLIDES = [
 (1, "capa", "Capa (Taborda, ICB)", []),
 (2, "capa", "Abertura do bloco 'Fungos, vida humana e natureza'", []),
 (3, "conteudo", "Agentes fermentadores", [
   ("fermentacao", "Leveduras fermentam açúcar (pão, cerveja, vinho)", "fermentacao")]),
 (4, "conteudo", "Fungos comestíveis", [
   ("comestiveis", "Fungos comestíveis e queijos maturados", EXC + " ilustração de importância econômica (fotos), sem alvo recuperável que a prova cobre; citado no Extra de fermentacao")]),
 (5, "conteudo", "Antibióticos naturais", [
   ("antibioticos", "Fungos produzem antibióticos (penicilina, Penicillium)", "fermentacao")]),
 (6, "conteudo", "Fungos bioluminescentes", [
   ("bioluminescencia", "Bioluminescência com importância biotecnológica", EXC + " curiosidade ilustrativa (foto), sem conteúdo cobrado")]),
 (7, "conteudo", "Micorrizas e decomposição", [
   ("micorriza", "Associação com raiz de planta: micorrizas", "saprofita"),
   ("decompositor", "Decomposição de matéria orgânica", "saprofita")]),
 (8, "conteudo", "Síndrome dos edifícios doentes", [
   ("edificios", "Sintomas (fadiga, cefaleia, irritação de olhos/nariz/vias aéreas) em >20% dos ocupantes", EXC + " síndrome ambiental lateral, sem card nos acervos e sem ganho que justifique autoral (Davi: menos autorais); citada no Extra de aspergillus-inalacao e no Tab")]),
 (9, "conteudo", "Decomposição de alimentos (mofo do pão)", [
   ("mofo-pao", "Rhizopus como mofo do pão", "rhizopus-pao")]),
 (10, "conteudo", "Micotoxinas em alimentos", [
   ("micotoxina", "Micotoxinas em grãos (aflatoxina)", "aflatoxina-chc"),
   ("micotoxina-graos", "Exposição por grãos/nozes mal armazenados", "aflatoxina-graos")]),
 (11, "conteudo", "Doença do algodão (peixes) e nariz branco (morcegos)", [
   ("animais", "Fungos causam doença em animais", EXC + " exemplos ilustrativos (fotos) de doença animal, fora do recorte médico")]),
 (12, "conteudo", "Doenças de plantas", [
   ("plantas", "Fungos fitopatogênicos", EXC + " fotos de folhas, ilustrativas")]),
 (13, "conteudo", "Fungos entomopatogênicos", [
   ("insetos", "Fungos parasitam insetos", EXC + " fotos ilustrativas (Cordyceps)")]),
 (14, "conteudo", "Quitrídios em anfíbios", [
   ("quitridio", "Quitrídios (Chytridiomycota), aquáticos", "sexuada")]),
 (15, "conteudo", "Hipótese: fungos e extinção dos dinossauros", [
   ("dinossauros", "Endotermia e virulência fúngica (Casadevall)", EXC + " hipótese de artigo citada como curiosidade")]),
 (16, "conteudo", "Chernobyl: melanina e radiação", [
   ("melanina-radiacao", "Fungos melanizados crescem mais sob radiação ionizante", "melanina")]),
 (17, "conteudo", "Classificação histórica", [
   ("whittaker", "Antes de 1969 em Plantae; Whittaker 1969 cria o reino Fungi", "glicogenio"),
   ("woess", "Woese 1994: árvore filogenética por DNA", "animais")]),
 (18, "conteudo", "Árvore filogenética", [
   ("animais-proximos", "Fungos mais próximos de animais que de plantas", "animais")]),
 (19, "conteudo", "Aspectos macroscópicos das colônias", [
   ("colonia-bolor", "Bolores: colônia algodonosa, aveludada, pulverulenta", "colonias"),
   ("colonia-levedura", "Leveduras: colônia cremosa, pastosa, cerebriforme", "colonias")]),
 (20, "conteudo", "Diferenças em relação às plantas", [
   ("sem-clorofila", "Sem clorofila", "exoenzimas"),
   ("sem-celulose", "Sem celulose na parede (exceto aquáticos)", "quitina"),
   ("sem-amido", "Não armazenam amido", "glicogenio"),
   ("quitina-glicogenio", "Quitina e glicogênio os aproximam dos animais", "glicogenio")]),
 (21, "conteudo", "Características dos fungos", [
   ("eucariontes", "Eucariontes", "eucarioto"),
   ("parede-quitina-glucana", "Parede com quitina e β-glucana", "quitina"),
   ("imoveis", "Imóveis", "eucarioto"),
   ("absortivos", "Absortivos", "exoenzimas"),
   ("glicogenio", "Armazenam glicogênio", "glicogenio"),
   ("sem-tecido", "Não formam tecido verdadeiro; uni ou pluricelulares", "colonias"),
   ("lisina", "Lisina pela via do ácido aminoadípico; cristas achatadas", EXC + " detalhe bioquímico sem card nos acervos e sem ganho de recuperação própria; fica no Tab (MEMORY: detalhe sem card e sem ganho vai ao verso/Tab)")]),
 (22, "conteudo", "Estrutura da célula fúngica", [
   ("parede-protecao", "Parede (~5%): proteção e forma; melanina", "quitina"),
   ("ergosterol", "Membrana com ergosterol", "ergosterol"),
   ("nucleo-linear", "Núcleo com cromossomos lineares e membrana nuclear", "dna-linear"),
   ("organelas", "Mitocôndria, RE, Golgi, ribossomos 80S", "ribossomo-80s"),
   ("capsula", "Cápsula (Cryptococcus)", "capsula")]),
 (23, "conteudo", "Camadas da parede celular", [
   ("camadas-parede", "Externa: manana/proteínas; interna: β-1,6 e β-1,3-glucana e quitina junto à membrana", "quitina")]),
 (24, "conteudo", "Parede varia entre espécies (Candida, Aspergillus, Cryptococcus, Histoplasma)", [
   ("parede-especies", "Composição varia: cápsula, melanina, α-1,3-glucana", "alfa-glucana")]),
 (25, "revisao", "Modelo geral de membrana (revisão de biologia celular)", []),
 (26, "conteudo", "Membrana dos fungos (ergosterol)", [
   ("membrana-ergosterol", "Ergosterol na membrana fúngica", "ergosterol")]),
 (27, "conteudo", "Antifúngicos e seus alvos", [
   ("equinocandina", "Equinocandinas inibem a síntese de β-glucana", "equinocandina"),
   ("polieno", "Polienos ligam ergosterol e formam poros", "polienos"),
   ("polieno-eletrolitos", "Vazamento de K+ e Na+", "polienos-eletrolitos"),
   ("polieno-toxicidade", "Toxicidade em mamíferos", "anfo-toxicidade"),
   ("azois", "Azóis inibem a síntese de ergosterol", "azois"),
   ("flucitosina", "5-FC vira 5-FU e inibe síntese de DNA", "flucitosina-5fu"),
   ("flucitosina-medula", "Mielossupressão", "flucitosina-medula")]),
 (28, "capa", "Abertura do bloco 'Base da taxonomia'", []),
 (29, "revisao", "Hierarquia taxonômica (reino → espécie), revisão de biologia geral", []),
 (30, "conteudo", "Estados anamórfico e teleomórfico no ciclo", [
   ("anamorfo", "Estado anamórfico = assexuado", "teleomorfo"),
   ("teleomorfo", "Estado teleomórfico = sexuado", "teleomorfo")]),
 (31, "conteudo", "Dificuldades da taxonomia", [
   ("especies", "~100 mil espécies descritas, ~5,1 milhões estimadas", EXC + " números de inventário biológico, sem cobrança; citados no Extra de teleomorfo"),
   ("nomes-fases", "Fases sexuada e assexuada recebem nomes diferentes; sexuada tem prioridade", "teleomorfo"),
   ("molecular", "Técnicas moleculares essenciais à classificação", "teleomorfo")]),
 (32, "conteudo", "Filos clássicos (Zygo, Basidio, Asco, Deutero; Oomycota em Chromista)", [
   ("filos-classicos", "Filos clássicos e seus esporos", "basidio")]),
 (33, "conteudo", "Myxomycota × Eumycota", [
   ("myxo", "Fungos do lodo agora em Protista; Eumycota = fungos verdadeiros", EXC + " reclassificação histórica sem cobrança; no Extra do card animais")]),
 (34, "conteudo", "Taxonomia dos anos 2000 (Dikarya)", [
   ("dikarya", "Dikarya = Ascomycota + Basidiomycota", "asco")]),
 (35, "conteudo", "Proposta 2019: 9 filos; Asco/Basidio com a maioria dos fungos médicos", [
   ("medicos-asco-basidio", "Ascomycota e Basidiomycota têm a maior parte dos fungos de interesse médico", "asco"),
   ("mucoromycota", "Mucoromycota: Mucor, Rhizopus, Lichtheimia", "mucor-hifa")]),
 (36, "capa", "Abertura: reprodução das leveduras", []),
 (37, "conteudo", "Reprodução das leveduras", [
   ("brotamento", "Assexuada por brotamento", "brotamento"),
   ("cissiparidade", "Cissiparidade (fissão binária)", "brotamento"),
   ("pseudomicelio", "Pseudomicélio", "pseudohifa"),
   ("blastoconidio", "Blastoconídio", "brotamento"),
   ("clamidoconidio", "Clamidoconídio", "conidios"),
   ("ascos-levedura", "Sexuada: ascos com ascósporos", "asco")]),
 (38, "conteudo", "Etapas do brotamento", [
   ("etapas-brotamento", "Parede amolece, núcleo divide e migra para o broto, broto se separa", "brotamento")]),
 (39, "conteudo", "Levedura unicelular; pseudo-hifas na invasão por Candida", [
   ("candida-pseudohifa", "Pseudo-hifas comuns na invasão por Candida", "candida-pseudohifa")]),
 (40, "conteudo", "Reprodução blástica: gêmulas que não se separam = pseudo-hifas", [
   ("pseudohifa-def", "Brotos que não se separam formam cadeias (pseudo-hifas)", "pseudohifa")]),
 (41, "capa", "Abertura: reprodução dos bolores", []),
 (42, "conteudo", "Reprodução assexuada dos bolores (Penicillium, Aspergillus)", [
   ("assexuada-bolor", "Esporos assexuados em estruturas aéreas", "conidios")]),
 (43, "conteudo", "Conídios externos", [
   ("conidio", "Conídios formados externamente no conidióforo (vesícula em Aspergillus)", "conidios"),
   ("aspergillus-conidioforo", "Aspergillus: conidióforo com vesícula", "aspergillus-conidioforo"),
   ("macro-microconidio", "Macroconídios, microconídios, conídios sésseis", "conidios")]),
 (44, "conteudo", "Conídios internos (Rhizopus)", [
   ("esporangio", "Esporangiósporos dentro do esporângio, no esporangióforo", "esporangio"),
   ("hifa-vegetativa", "Hifa vegetativa", "septos")]),
 (45, "conteudo", "Dimorfismo térmico (Paracoccidioides)", [
   ("dimorfismo-temp", "35–37 °C levedura; 25–27 °C bolor", "dimorfismo-temperatura"),
   ("dimorfismo-ambiente", "Bolor no ambiente, levedura no hospedeiro", "dimorfismo"),
   ("paracocci", "Paracoccidioides brasiliensis é dimórfico", "paracocci-dimorfico")]),
 (46, "conteudo", "Reprodução sexuada", [
   ("gametas-flagelados", "Fungos aquáticos têm gametas flagelados", "sexuada"),
   ("plasmogamia", "Plasmogamia (fusão de citoplasmas)", "sexuada"),
   ("dicariotico", "Fase dicariótica n+n", "sexuada"),
   ("cariogamia", "Cariogamia gera diploide; meiose gera esporos sexuados", "sexuada")]),
 (47, "capa", "Abertura: estruturas reprodutivas usadas na classificação", []),
 (48, "conteudo", "Antigo filo Zygomycota", [
   ("zygo-sapro", "Sapróbios, eventualmente infecciosos", "mucor-hifa"),
   ("cenocitico", "Micélio ramificado e cenocítico", "septos"),
   ("zigosporo", "Reprodução sexuada por zigósporo", "mucor-hifa")]),
 (49, "conteudo", "Pilobolus (zigomiceto em fezes de gado)", [
   ("pilobolus", "Esporângios explosivos", EXC + " exemplo ilustrativo (foto)")]),
 (50, "conteudo", "Filo Basidiomycota", [
   ("basidio", "Cogumelos; basidiósporos produzidos no basídio (basidioma)", "basidio")]),
 (51, "conteudo", "Amanita venenosa; Geastrum liberando esporos", [
   ("amanita", "Algumas Amanita altamente venenosas", "amanitina")]),
 (52, "conteudo", "Filo Ascomycota", [
   ("ascomycota", "Micro a macroscópicos, filamentosos ou leveduriformes", "asco"),
   ("asco", "Ascósporos dentro do asco, em ascomas", "asco")]),
 (53, "conteudo", "Pezizaceae (apotécio em taça)", [
   ("apotecio", "Ascocarpo em forma de taça", EXC + " exemplo ilustrativo (foto); ascocarpos aparecem na figura do card asco")]),
 (54, "capa", "Abertura: ecologia e nutrição", []),
 (55, "conteudo", "Hábitat, vias de dispersão e fatores interferentes", [
   ("dispersao", "Dispersão pelo ar, água, homem, animais, insetos", "aspergillus-inalacao"),
   ("aspergillus-inalacao", "Infecção por inalação de propágulos (ex. Aspergillus)", "aspergillus-inalacao")]),
 (56, "conteudo", "Nutrição por absorção (osmotrofia)", [
   ("exoenzimas", "Exoenzimas degradam macromoléculas; transporte pela membrana", "exoenzimas"),
   ("queratinase", "Queratinases (ex. dermatófitos)", "queratinase")]),
 (57, "conteudo", "Nutrientes", [
   ("carbono-nitrogenio", "Carbono (glicose), nitrogênio (nitrato, amônio, peptonas), S, P", "exoenzimas"),
   ("oligoelementos", "Fe, Zn, Mn, Cu, Ca; vitaminas", EXC + " lista de micronutrientes sem cobrança própria; citada no Extra de exoenzimas")]),
 (58, "conteudo", "Fatores ambientais: temperatura", [
   ("mesofilos", "Fungos médicos mesófilos 20–30 °C", "mesofilos"),
   ("dimorficos-temp", "Dimórficos: 22–28 °C filamentosos, 33–37 °C leveduriformes", "dimorfismo-temperatura")]),
 (59, "conteudo", "Umidade relativa e atividade de água", [
   ("aw", "Aw 0,65: fungos não crescem", "atividade-agua")]),
 (60, "conteudo", "pH", [
   ("ph", "pH ótimo ~6,5; leveduras 2,5–8,5; filamentosos 1,5–11", "mesofilos")]),
 (61, "conteudo", "Liquens", [
   ("liquen", "Mutualismo fungo (micobionte) + alga (fotobionte)", "saprofita")]),
]

# Seções do livro (Trabulsi 64.1–64.2) e exercícios/provas que entram no inventário (sem lâmina)
CAPITULO = [
 ("cap-parede-dimorfica", "Trabulsi 64.1: fase M (25 °C) mais β-glucana; fase Y (37 °C) mais α-glucana", "alfa-glucana"),
 ("cap-hifas", "Trabulsi 64.1: hifa septada × cenocítica; micélio vegetativo × aéreo", "septos"),
 ("cap-clamidoconidio", "Trabulsi 64.1: clamidoconídio, estrutura de resistência", "conidios"),
 ("cap-dispersao-ar", "Trabulsi 64.2: ar atmosférico é a principal via; anemófilos e alergias", "aspergillus-inalacao"),
]
EXERCICIOS = [
 ("prova-fungo-bacteria", "Provas 2017 P2 2.5 e 2018 P2 1.3: fungo × bactéria (parede, 80S, mitocôndria, núcleo)", "quitina"),
 ("prova-fatores", "Prova 2018 P2 1.4: fatores ambientais (temperatura, umidade, pH)", "atividade-agua"),
 ("prova-brotamento", "Prova 2017 P2 2.4: brotamento como reprodução assexuada da levedura", "brotamento"),
 ("prova-capsula", "Prova 2024 P3 2.5: vantagens da cápsula", "capsula"),
]


def main():
    slides, alvos = [], []
    for n, classe, titulo, itens in SLIDES:
        s = {"numero": n, "classe": classe, "titulo": titulo}
        if classe == "conteudo":
            s["itens"] = []
            for k, texto, dest in itens:
                it = {"id": f"mb43-s{n:02d}-{k}", "texto": texto}
                if dest.startswith(EXC):
                    it.update(exclusao_permitida=True, exclusao=dest[len(EXC):].strip())
                else:
                    it["card"] = dest
                s["itens"].append(it)
                alvos.append({"id": it["id"], "slide": str(n), "alvo": texto, "fontes": [f"slide {n}"],
                              "origem_prevista": "exclusão" if dest.startswith(EXC) else dest})
        else:
            s["justificativa"] = {"capa": "capa ou abertura de bloco, sem conteúdo", "revisao": "revisão de conteúdo de outra disciplina (biologia celular/geral), sem alvo novo desta aula"}[classe]
        slides.append(s)
    def extra(lista, prefixo, fonte):
        out = []
        for k, texto, dest in lista:
            out.append({"id": f"mb43-{prefixo}-{k}", "texto": texto, "card": dest})
            alvos.append({"id": f"mb43-{prefixo}-{k}", "slide": "livro" if prefixo == "cap" else "prova", "alvo": texto, "fontes": [fonte], "origem_prevista": dest})
        return out
    inv = {"aula": "Biologia geral dos fungos (UC03, aula 43; Prof. Carlos P. Taborda)", "lido_antes_da_selecao": True,
           "slides": slides, "capitulo": [{"secao": "Trabulsi 64.1–64.2", "itens": extra(CAPITULO, "cap", "Trabulsi 64")}],
           "exercicios": [{"fonte": "provas UC03", "itens": extra(EXERCICIOS, "prova", "provas UC03")}]}
    (HERE / "inventario-aula.json").write_text(json.dumps(inv, ensure_ascii=False, indent=1))
    fontes_plano = {
     "slides": {"estado": "consultada", "contribuicao": "61 lâminas: definem blocos (importância, características, parede/membrana, antifúngicos, taxonomia, reprodução, ecologia/nutrição)"},
     "bibliografia": {"estado": "consultada", "contribuicao": "Trabulsi 64.1–64.2: parede (camadas; fase M × Y), tipos de hifa, propágulos, dispersão aérea"},
     "caoc": {"estado": "não localizada", "contribuicao": "sem material CAOC desta aula localizado; monitoria da turma usada como material de estudo"},
     "youtube": {"estado": "consultada", "contribuicao": "Physeo/Strong Medicine: ergosterol, β-glucana, levedura × bolor, 'mold in the cold'; Prof. Dave: fungos mais próximos de animais, Dikarya; Ninja Nerd: alvos dos antifúngicos"},
     "veteranos": {"estado": "consultada", "contribuicao": "Monitoria P2 e apostila guia: ênfase em ergosterol, quitina maior em bolores, hifas septada/cenocítica, brotamento × fissão, pleomorfismo × dimorfismo, mesófilos, pH, umidade"},
     "provas": {"estado": "consultada", "contribuicao": "2017/2018 P2 e 2024/2025 P3: dimorfismo (temperaturas e parede α/β-glucana), parede fungo × bactéria, fatores ambientais, brotamento, cápsula"},
     "exercicios": {"estado": "não localizada", "contribuicao": "sem lista de exercícios desta aula no drive da turma; questões de prova cumprem o papel"},
    }
    plan = {"aula": inv["aula"], "feito_antes_de_montar": True, "data": "2026-10-09", "fontes": fontes_plano, "alvos": alvos,
            "fora_do_recorte": ["micoses específicas (cutâneas, subcutâneas, sistêmicas): aulas seguintes da P3",
                                "farmacologia clínica dos antifúngicos (indicações, doses): fica para farmacologia/micoses",
                                "testes diagnósticos (tubo germinativo, tinta da China, KOH): aulas de micoses e micologia prática"]}
    (HERE / "planejamento.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
    print(len(slides), "lâminas;", len(alvos), "itens;", sum(1 for a in alvos if a["origem_prevista"] == "exclusão"), "exclusões")


if __name__ == "__main__":
    main()
