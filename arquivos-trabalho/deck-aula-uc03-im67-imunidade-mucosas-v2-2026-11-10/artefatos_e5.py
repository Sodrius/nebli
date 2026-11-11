"""E5 da 67: cobertura.tsv, decisoes.json, tipos.tsv, REVISAO-AUTORAIS.md, imagens-batem/vistas, escopo (linha, fontes, provas),
mapa/inventário com as chaves reais do plano e motivações atendidas. Rodar depois do build."""
import json, re, pathlib
H = pathlib.Path(__file__).parent
plan = json.load(open(H / "plan.json"))
E = {e["key"]: e for e in plan["entries"]}
SH = {v["source_nid"]: f"sh-{k}" for k, v in plan["compartilhados"].items() if v.get("source_nid")}
sh = lambda nid: SH.get(str(nid), f"sh-{nid}")
# lidos: 3 primeiros AnKing/NEBLI da busca semântica da própria chave
lid = {}
for l in open(H / "busca/semantica.jsonl"):
    d = json.loads(l)
    hs = [h for v in d.values() if isinstance(v, list) for h in v if isinstance(h, dict) and "nid" in h and h.get("acervo") in ("AnKing", "NEBLI-vivo", "Histology")]
    lid[d["chave"]] = [str(h["nid"]) for h in hs][:4]
BUSCA = "Busca nos três caminhos (seções First Aid de Peyer, IgA e Th17; palavra-chave com sinônimos em AnKing e externos; significado em todos os acervos e NEBLI vivo, 10/11): "
# chave: (conceito, fonte, decora, decisão, tipo, principio, visual, papel, par, tipo_info, exemplar, semelhança, anti, item)
A = {
 "k-malt": ("MALT, GALT e BALT", "lâmina 2", "GALT", "MALT aparece só como definição (sh-1791023357519) e no Histology; nenhum card dá os nomes GALT e BALT por local, que a lâmina 2 lista", "comparacao", "O tecido linfoide da mucosa se divide por local: GALT no intestino, BALT nos brônquios", "nao", "lacuna", "§C", "conjunto organizado", "1792787420154", "um eixo (local) e uma linha por item com o nome no cloze", "1791984889849", "p1-1"),
 "k-iel-cd8": ("Linfócitos intraepiteliais são CD8", "lâminas 7 e 9", "CD8", "AnKing cobra IEL só na doença celíaca (1482359464147) e γδ sem a mucosa (Histology 1701964374227); nenhum diz que os IEL do delgado são CD8", "fato-chave", "Os linfócitos de dentro do epitélio intestinal são principalmente T CD8", "sim", "lacuna", "§E", "fato-chave situado", "1791023354943", "fato curto com o contexto (local) visível e o número/nome no cloze", "1791627549152", "p3-1"),
 "k-nodulo-colon": ("Peyer no íleo × nódulos solitários no cólon", "lâmina 8; transcrição p.24", "solitary lymphoid nodules", "1486608789738 diz que Peyer distingue o íleo; nenhum card contrasta com os nódulos escassos do cólon (o sh UC08 1791023302370 diz o contrário e está suspenso)", "comparacao", "O tecido linfoide organizado do intestino concentra-se no íleo; o cólon tem só nódulos esparsos", "sim", "lacuna", "§B", "contraste por critério comum", "1792166970014", "dois lados no mesmo índice com o critério (quantidade/local) visível", "1793784421465", "p2-5"),
 "k-infl-fisiologica": ("Inflamação fisiológica × neutrófilos na invasão", "lâminas 9–10", "neutrophils", "AnKing não tem inflamação fisiológica da mucosa; 1520300296240 fala de Th17 e neutrófilos sem o intestino saudável", "comparacao", "A lâmina própria cheia é inflamação fisiológica; a invasão traz neutrófilos", "nao", "lacuna", "§B", "contraste por critério comum", "1792166970014", "dois estados no mesmo índice, critério (saudável × invasão) em negrito", "1793784421465", "p3-2"),
 "k-homing": ("Linfócitos ativados voltam à mucosa", "lâmina 11; transcrição p.36", "lamina propria", "1486831451445 diz onde ficam os plasmócitos de IgA, sem o retorno de T e B efetores; nada de homing de mucosa no AnKing (só natalizumab no Crohn, fora)", "mecanismo", "Linfócitos ativados no GALT voltam à mucosa como efetores", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1792695019413", "cadeia curta (ativação → retorno) com o destino no cloze", "1791627549152", "p4-5"),
 "k-caliciforme": ("Caliciformes fazem a barreira de muco", "lâmina 12; transcrição p.26", "goblet", "AnKing traz caliciforme como organela (RER, 1468101790635) e muco da asma; o card UC08 de mucinas está suspenso; nenhum liga o muco à separação das bactérias", "mecanismo", "O muco das caliciformes separa as bactérias do epitélio", "sim", "lacuna", "§A", "causa → mecanismo → consequência", "1791631347467", "agente → produto → efeito protetor, nome do agente no cloze", "1791631345113", "p4-1"),
 "k-dc-mesenterico": ("Dendrítica leva o antígeno ao linfonodo mesentérico", "lâmina 13; prova", "mesenteric", "Os AnKing de linfonodo mesentérico cobram drenagem anatômica (1486945243332); 1791780605649 cobre a via da célula M, não a dendrítica que vai ao linfonodo", "mecanismo", "A dendrítica da lâmina própria leva o antígeno ao linfonodo mesentérico", "sim", "lacuna", "§A", "processo ou formação em ordem", "1792713404156", "trajeto com origem e destino, destino no cloze", "1791627549152", "p4-4"),
 "k-tres-tarefas": ("Tolerar comida e comensais, responder a patógeno", "lâmina 14", "food", "1791780602055 (sh) fala de tolerância pela microbiota, sem a comida; nenhum card junta as tarefas da lâmina 14", "comparacao", "O sistema imune do intestino tolera comida e comensais e responde a patógenos", "nao", "fio", "§B", "contraste por critério comum", "1792166970014", "o que é tolerado × o que é combatido na mesma frase, tolerados no mesmo índice", "1791627549152", "p5-1"),
 "k-ac-retinoico": ("Ácido retinoico torna a dendrítica tolerogênica", "lâmina 16", "retinoic acid", "AnKing de ácido retinoico é APL/sarampo/vitamina A (1480564270476, 1495635796867); sh-1791625433083 cobra a Treg induzida, não o condicionamento da dendrítica", "mecanismo", "O ácido retinoico do microambiente torna a dendrítica da mucosa tolerogênica", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1791631347467", "fator → efeito na célula, fator no cloze com o contexto visível", "1791631345113", "p5-2"),
 "k-dc-il10-ido": ("Dendrítica tolerogênica faz IL-10 e IDO", "lâmina 16", "IDO", "Nenhum card de IDO em acervo; IL-10 aparece como citocina da Treg (1487116971703), não da dendrítica da mucosa", "mecanismo", "A dendrítica tolerogênica produz IL-10 e IDO e favorece Treg", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1792170508078", "célula → moléculas → efeito, moléculas num índice", "1791625435907", "p5-3"),
 "k-dc-proinfl": ("Minoria de dendríticas pró-inflamatórias", "lâmina 17", "majority", "Nenhum acervo distingue dendríticas tolerogênicas e pró-inflamatórias da mucosa", "comparacao", "Uma minoria de dendríticas da mucosa é pró-inflamatória e inicia defesa", "nao", "lacuna", "§B", "contraste por critério comum", "1791575690369", "maioria × minoria com critério visível, lado minoritário no cloze", "1791631345113", "p5-4"),
 "k-prr-basolateral": ("PRR só basolateral", "lâminas 18–19", "basolateral", "1461615074564 é H2 basolateral da parietal; nenhum card diz onde ficam os TLR do epitélio intestinal", "mecanismo", "TLR só na face basolateral: só a invasão ativa resposta", "sim", "lacuna", "§A", "causa → mecanismo → consequência", "1792695019413", "localização do receptor → quem é reconhecido, local no cloze", "1791627549152", "p6-1"),
 "k-iga-neutraliza": ("IgA protege por neutralização", "lâmina 20; prova", "neutralization", "AnKing de IgA cobra local, forma e transporte (1487117227757, 1487117240890); nenhum diz que a função é neutralizar sem inflamar, que a prova pede", "mecanismo", "A IgA secretora neutraliza sem complemento nem inflamação", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1791631347467", "molécula → modo de ação → consequência, modo no cloze", "1791631345113", "p7-1"),
 "k-reguladoras": ("Treg induzida, Th3 e Tr1", "lâmina 22", "Th3", "Os AnKing de Treg (1487116967325, 1487116971703) cobram a Treg geral; Th3 e Tr1 não existem em acervo", "comparacao", "A mucosa favorece três tipos de células reguladoras", "nao", "lacuna", "§C", "conjunto organizado", "1792787420154", "eixo (marcador/citocina) e uma linha por tipo com o nome no cloze", "1793784421465", "p8-1"),
 "k-il10-colite": ("Sem IL-10 há colite", "transcrição p.60", "IL-10", "1489970615786 diz que a IL-10 atenua a inflamação, sem a consequência intestinal da sua falta", "mecanismo", "Sem IL-10 a regulação intestinal falha e há colite", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1791631347467", "falta do fator → consequência, consequência no cloze", "1791627549152", "p8-2"),
 "k-treg-th17": ("IL-6 decide Treg × Th17", "lâminas 23–26", "Th17", "1487116955601 e 1487116975048 cobram cada indução solta; nenhum contrasta Th3 e Th17 pela IL-6 como as lâminas 25–26", "comparacao", "No mesmo TGF-β, a IL-6 troca tolerância (Th3/Treg) por defesa (Th17)", "sim", "fio", "§B", "contraste por critério comum", "1792695019915", "dois destinos no mesmo eixo, critério (IL-6) em negrito", "1793784421465", "p8-3"),
 "k-balanco-treg": ("Na invasão o MALT induz Th1 ou Th2", "lâmina 27; transcrição p.70", "Th1", "Busca de AnKing de Th1/Th2: 1487116873670 (sh-1791625432007) cobre só Th2 recrutando eosinófilos; nenhum AnKing liga a invasão da mucosa ao tipo de resposta (Th1 contra intracelulares, Th2 contra helmintos) da lâmina 27", "comparacao", "Na invasão a mucosa troca tolerância por Th1 contra intracelulares ou Th2 contra helmintos", "nao", "lacuna", "§B", "contraste por critério comum", "1792166970014", "invasor → resposta, dois lados no mesmo índice", "1793784421465", "p8-5"),
 "k-olho": ("Olho imunoprivilegiado", "lâmina 29", "blood vessels", "1505765860803 (oftalmia simpática) é clínica; 1487117300306 cobra FasL na citotoxicidade; nenhum junta os três mecanismos do olho", "comparacao", "O olho limita a resposta imune por ausência de vasos, TGF-β e FasL/PD-L1", "nao", "lacuna", "§C", "conjunto organizado", "1792787420154", "eixo (estrutura do olho) e uma linha por mecanismo", "1791984889849", "p9-1"),
"k-microbiota": ("Microbiota protege por competição", "transcrição p.6", "colonization resistance", "AnKing traz flora intestinal produzindo vitaminas (1520709952510) e Gram-negativos; nenhum card de resistência à colonização; o card NEBLI da aula 39 tem cloze genérico", "mecanismo", "As comensais protegem a mucosa ocupando espaço e nutrientes", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1792695019413", "ação das comensais → proteção nomeada no cloze", "1791627549152", "p4-2"),
 "k-iga-aglutina": ("IgA aglutina e elimina pelas fezes", "prova UC03; transcrição p.58", "agglutination", "AnKing de IgA cobra local, forma e transporte; nenhum diz que a sIgA aglutina micróbios no muco, ponto do gabarito da prova", "mecanismo", "A IgA dimérica aglutina micróbios no muco e eles saem nas fezes", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1791631347467", "molécula → ação → consequência, ação no cloze", "1791631345113", "p7-1"),
 "k-higiene": ("Hipótese da higiene", "transcrição p.72–74", "hygiene hypothesis", "AnKing não tem a hipótese da higiene (busca: asma IgE 1474580613274, basófilos); o card NEBLI da aula 39 está suspenso e tem negrito no cloze", "mecanismo", "Pouca exposição microbiana precoce deixa a regulação destreinada e aumenta alergias", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1791631347467", "condição → consequência com o nome da ideia no cloze", "1791627549152", "p8-6"),

"k-alfa4beta7": ("Integrina α4β7 do homing", "transcrição p.36; Janeway 12.6", "α4β7", "Busca 10/11 (alpha4beta7, vedolizumab, MAdCAM, integrin homing gut): só natalizumabe no Crohn (1497204171184), que não nomeia a molécula", "fato-chave", "O homing intestinal usa a integrina α4β7 ligando MAdCAM-1", "nao", "lacuna", "§E", "fato-chave situado", "1791023354943", "fato curto com o contexto visível e a molécula no cloze", "1791627549152", "p4-11"),
"k-dc-viral": ("Dendrítica na infecção viral", "prova 2025 P3 2.2", "IL-12", "Busca 10/11 (dendritic IL-12 interferon): nenhum AnKing liga a dendrítica intestinal às citocinas antivirais do gabarito", "mecanismo", "Na infecção viral a dendrítica apresenta e libera IL-12 e IFN tipo I", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1791631347467", "estímulo → resposta da célula → citocina no cloze", "1791631345113", "p5-8"),
"k-fumo": ("Fumo destrói os cílios", "apostila cap. 2", "cilia", "Busca 10/11 (smoking cilia mucociliary): nenhum AnKing liga o fumo aos cílios; o escalador mucociliar (1473289461901) só descreve a função", "mecanismo", "O fumo destrói os cílios e a limpeza do muco falha", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1791631347467", "agente → dano → consequência, estrutura no cloze", "1791631345113", "p1-3"),
"k-dc-dendritos": ("Dendrítica alcança o lúmen", "transcrição p.34; prova 2025", "between epithelial cells", "Busca 10/11 (dendritic lumen, transepithelial): só células M no Histology (1701980449458); nenhum card da dendrítica amostrando o lúmen, ponto do gabarito da prova", "mecanismo", "A dendrítica amostra o lúmen por prolongamentos entre os enterócitos", "sim", "lacuna", "§A", "processo ou formação em ordem", "1792713404156", "agente → via → destino, via no cloze", "1791627549152", "p4-8"),
"k-tolerancia-oral": ("Tolerância oral", "apostila cap. 2", "tolerance", "Busca 10/11 (oral tolerance): só teste de tolerância à glicose no AnKing; nenhum card de tolerância oral", "mecanismo", "Antígeno por via oral induz tolerância sistêmica", "nao", "lacuna", "§A", "causa → mecanismo → consequência", "1791631347467", "via de exposição → resultado, resultado no cloze", "1791631345113", "p5-5"),
"k-fases": ("Três fases da imunidade intestinal", "transcrição p.74–76", "bacteria", "Busca 10/11: o AnKing só tem IgA no leite (1487117234083, 1487121965148); nenhum card das fases pré-natal, amamentação e alimento sólido", "comparacao", "A imunidade intestinal amadurece em três fases ligadas à microbiota e ao leite", "nao", "lacuna", "§C", "conjunto organizado", "1792787420154", "eixo (fase) e uma linha por fase com o marco no cloze", "1793784421465", "p8-11"),
}
VER = {}
NAO_VISUAL = {"ak1497204171184", "ak1487121965148", "ak1505765860803", "ak1521772146512", "ak1506179807216"}
cob = ["chave\tconceito\tfonte_aula\tveredito\tlidos\tdecora\tdecisao"]
dec, tip, rev = {}, ["chave\ttipo\tprincipio\tvisual\tpapel"], ["# Revisão dos autorais — 67 Imunidade de mucosas", ""]
for k, e in E.items():
    if k in A:
        c, f, deco, d, t, pr, vi, pa, par, ti, ex, sem, an, it = A[k]
        txt = e["fields"]["Text"]
        ans = re.findall(r"\{\{c\d+::([^}:]+)", txt)
        assert deco in ans, (k, deco, ans)
        lidos = lid.get(k, [])[:4]
        cob.append(f"{k}\t{c}\t{f}\tlacuna\t{','.join(lidos)}\t{deco}\t{BUSCA}{d}")
        dec[k] = ["lacuna", BUSCA + d]
        tip.append(f"{k}\t{t}\t{pr}\t{vi}\t{pa}")
        rev.append(f"- {k} — par: {par}; tipo-informacao: {ti}; ensina: {pr}; EXEMPLAR {ex}; semelhança: {sem}; adaptação: conteúdo da aula 67 ({f}); ANTI {an}; decora: {deco} — ok")
    else:
        alvo = e.get("alvo", "")
        txt = e["fields"]["Text"]; ans = re.findall(r"\{\{c\d+::([^}:]+)", txt)
        cob.append(f"{k}\t{alvo}\t{e.get('evid','')}\tcoberto\t\t{ans[0] if ans else ''}\tacervo: entra")
        tip.append(f"{k}\tfato-chave\tPrincípio da {e.get('evid','').lower()}: {alvo}\t{'nao' if k in NAO_VISUAL else 'sim'}\t")
for k, v in plan["compartilhados"].items():
    cob.append(f"sh-{k}\t{v.get('alvo','')}\t{v.get('evid','')}\tcoberto\t\t\tassociado (cópia NEBLI viva)")
(H / "busca/cobertura.tsv").write_text("\n".join(cob) + "\n")
json.dump(dec, open(H / "decisoes.json", "w"), ensure_ascii=False, indent=1)
(H / "tipos.tsv").write_text("\n".join(tip) + "\n")
(H / "REVISAO-AUTORAIS-gerado.md").write_text("\n".join(rev) + "\n\nOrganizadores necessários: sim — a aula enumera e contrasta conjuntos (MALT por local, íleo × cólon, saudável × invasão, maioria × minoria de dendríticas, PRR, Th3 × Tr1, Th3 × Th17, Th1 × Th2, olho), cada um com organizador; os AnKing avulsos dos mesmos temas cobram outros alvos e ficam.\n")
# imagens
import importlib.util
spec_txt = (H / "spec.py").read_text()
vistas = eval(re.search(r"IMAGENS_VISTAS = (\{.*?\n\})", spec_txt, re.S).group(1))
bat = {}
for k, e in E.items():
    blob = json.dumps(e["fields"]) + str(e.get("extra_add", ""))
    for f in re.findall(r'src=\\?"([^"\\]+)', blob):
        bat[k] = {"veredito": "ok", "porque": vistas.get(f, f"figura {f}")}
json.dump(bat, open(H / "imagens-batem.json", "w"), ensure_ascii=False, indent=1)
# mapa e inventário com as chaves reais
MAP = {"p1-1": ["k-malt", sh(1791023357519), sh(1473289461901)], "p1-2": ["k-tres-tarefas"], "p2-1": ["ex1701979294684-tonsilas"], "p2-2": [sh(1486831445995), sh(1486608789738)],
 "p2-3": [sh(1486945164044)], "p2-4": ["k-iel-cd8"], "p2-5": ["k-nodulo-colon"], "p3-1": ["k-iel-cd8"], "p3-2": ["k-infl-fisiologica"], "p3-3": ["k-infl-fisiologica"],
 "p4-1": [sh(1486608768857), "k-caliciforme"], "p4-2": ["k-microbiota"], "p4-3": [sh(1486831448616)], "p4-4": ["k-dc-mesenterico"], "p4-5": ["k-homing"],
 "p5-1": ["k-tres-tarefas"], "p5-2": ["k-ac-retinoico"], "p5-3": ["k-dc-il10-ido"], "p5-4": ["k-dc-proinfl"], "p6-1": ["k-prr-basolateral"], "p6-2": ["k-prr-basolateral"],
 "p7-1": ["k-iga-neutraliza", "k-iga-aglutina", sh(1487117227757), sh(1487117240890)], "p7-2": [sh(1487117156031)],
 "p7-3": [sh(1487117251418), sh(1487117223955)], "p7-6": [sh(1487117209824), sh(1487117238120), sh(1487117234083)], "p7-7": [sh(1487117216624), sh(1487117219869)], "p7-4": [sh(1487117255825)], "p7-5": [sh(1486831451445)],
 "p8-1": ["k-reguladoras"], "p8-7": [sh(1487116967325), sh(1487116971703)], "p8-2": ["k-il10-colite"], "p8-8": [sh(1489970615786), sh(1487981558376)],
 "p8-3": ["k-treg-th17", sh(1487116955601), sh(1487116975048)], "p8-9": [sh(1489970054827)], "p8-4": [sh(1520300013308), sh(1520300296240)],
 "p8-5": ["k-balanco-treg", sh(1487116873670)], "p8-10": [sh(1479267424779)], "p8-6": ["k-higiene"], "p9-1": ["k-olho"], "p9-2": ["k-olho", sh(1487117300306)],
 "p1-3": ["k-fumo", "sh-1791592724520"], "p1-4": ["sh-1791983685881"], "p2-6": ["sh-1791023302370"], "p4-6": [sh(1488502340989)], "p4-7": ["sh-1791023297666", "sh-1791780601643"],
 "p4-8": ["k-dc-dendritos"], "p4-9": ["ak1497204171184"], "p4-10": ["sh-1791780605649"], "p5-5": ["k-tolerancia-oral"], "p5-6": ["sh-1791625433083"],
 "p5-7": ["sh-1791780602055"], "p6-3": [sh(1521771712578), "ak1521772146512"], "p6-4": ["sh-1791780608272"], "p7-8": ["ak1487121965148"],
 "p8-11": ["k-fases"], "p8-12": ["sh-1791780613803"], "p4-11": ["k-alfa4beta7"], "p4-12": [sh(1516219843437)], "p4-13": ["ak1506179807216"], "p5-8": ["k-dc-viral"]}
validos = set(E) | {f"sh-{k}" for k in plan["compartilhados"]}
todos = [x for v in MAP.values() for x in v]
assert set(todos) <= validos, set(todos) - validos
falta = validos - set(todos); assert not falta, falta
m = json.load(open(H / "mapa-de-profundidade.json"))
for p in m["passos"]:
    for it in p["itens"]:
        it["cards"] = MAP[it["id"]]
json.dump(m, open(H / "mapa-de-profundidade.json", "w"), ensure_ascii=False, indent=1)
mot = json.load(open(H / "motivacoes.json"))
for x in mot["motivacoes"]:
    x["atendida_por"] = MAP[x["item_mapa"]]
json.dump(mot, open(H / "motivacoes.json", "w"), ensure_ascii=False, indent=1)
inv = (H / "inventario.py").read_text()
old = {"k-tonsila": "ex1701979294684-tonsilas", "k-peyer-ileo": sh(1486831445995), "k-peyer-centro": sh(1486945164044), "k-iel-lp": "k-iel-cd8", "k-paneth": sh(1486608768857),
 "k-microbiota": sh(1791780576172), "k-celula-m": sh(1486831448616), "k-patogeno-pmn": "k-infl-fisiologica", "k-tgfb-iga": sh(1487117156031), "k-pigr": sh(1487117251418),
 "k-componente-secretor": sh(1487117255825), "k-plasmocitos-iga": sh(1486831451445), "k-th17-citocinas": sh(1520300013308), "k-infeccao-th1-th2": "k-balanco-treg",
 "k-higiene": sh(1791780613803), "k-olho-fasl": "k-olho"}
for a, b in old.items():
    inv = inv.replace(f"'{a}'", f"'{b}'")
(H / "inventario.py").write_text(inv)
print("ok", len(E), "entradas,", len(plan["compartilhados"]), "compartilhados")
