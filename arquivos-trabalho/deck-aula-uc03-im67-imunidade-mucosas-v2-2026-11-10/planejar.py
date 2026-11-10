"""E3 da 67: um só lugar para itens → inventário, mapa, motivações, escopo. Rodar antes da busca."""
import json, pathlib
H = pathlib.Path(__file__).parent
# (id, tipo, o_que, fonte, termos, cards, lamina)
PASSOS = [
 ("MALT e GALT: tecido linfoide próprio da mucosa", "1-2", [
  ("p1-1", "organizar", "O tecido linfoide associado às mucosas é o MALT; no intestino é o GALT e nos brônquios o BALT, sistema próprio porque o intestino tolera comida e comensais.", "lâmina 2; transcrição p. 4", ["MALT", "GALT", "BALT"], ["k-malt"], 2),
 ]),
 ("Onde ficam os linfócitos da mucosa", "3-8", [
  ("p2-1", "decorar", "Tonsilas e adenoides são agregados linfoides com folículos (T e B) sob o epitélio da entrada aerodigestiva.", "lâmina 3; transcrição p. 10", ["tonsila", "folículo"], ["k-tonsila"], 3),
  ("p2-2", "decorar", "Placas de Peyer são folículos linfoides na submucosa, concentrados no íleo.", "lâminas 4–5; transcrição p. 14–16", ["placas de Peyer", "íleo"], ["k-peyer-ileo"], 4),
  ("p2-3", "explicar", "A área clara da placa de Peyer é o centro germinativo, onde linfócitos B proliferam após encontrar antígeno.", "lâmina 6; transcrição p. 18", ["centro germinativo"], ["k-peyer-centro"], 6),
  ("p2-4", "decorar", "Há linfócitos dentro do epitélio (intraepiteliais) e muitos na lâmina própria, abaixo dele.", "lâmina 7", ["intraepiteliais", "lâmina própria"], ["k-iel-lp"], 7),
  ("p2-5", "distinguir", "O intestino grosso tem só nódulos linfoides solitários e escassos; o íleo concentra as placas de Peyer.", "lâmina 8; transcrição p. 22–24", ["nódulo solitário"], ["k-nodulo-colon"], 8),
 ]),
 ("Intestino saudável: inflamação fisiológica; infectado: neutrófilos", "9-10", [
  ("p3-1", "decorar", "Os linfócitos intraepiteliais do intestino delgado são principalmente T CD8 (TCR αβ ou γδ).", "lâmina 9; transcrição p. 14; apostila", ["CD8", "γδ"], ["k-iel-cd8"], 9),
  ("p3-2", "explicar", "A lâmina própria cheia de células é inflamação fisiológica contra antígenos inócuos (comida e comensais), não inflamação crônica.", "lâmina 9; transcrição p. 28", ["inflamação fisiológica"], ["k-infl-fisiologica"], 9),
  ("p3-3", "e-se", "Se um patógeno invade, aparecem rapidamente neutrófilos (polimorfonucleares).", "lâmina 10; transcrição p. 30", ["neutrófilos"], ["k-patogeno-pmn"], 10),
 ]),
 ("Barreiras, indução e retorno dos linfócitos", "11-13", [
  ("p4-1", "decorar", "Células caliciformes fazem o muco que separa microrganismos do epitélio e células de Paneth fazem defensinas.", "lâmina 12; transcrição p. 26, 32", ["Paneth", "defensinas", "caliciformes"], ["k-paneth", "k-caliciforme"], 12),
  ("p4-2", "explicar", "A microbiota comensal protege ocupando espaço e produzindo antimicrobianos (resistência à colonização).", "transcrição p. 6", ["microbiota", "colonização"], ["k-microbiota"], 12),
  ("p4-3", "explicar", "Células M do epitélio sobre a placa de Peyer transportam antígeno do lúmen às dendríticas do folículo.", "lâminas 12–13; transcrição p. 34; Janeway 12.4", ["células M"], ["k-celula-m"], 13),
  ("p4-4", "explicar", "Dendríticas da lâmina própria estendem dendritos ao lúmen, capturam antígeno e o levam pelo linfático ao linfonodo mesentérico.", "lâmina 13; transcrição p. 34; prova 2024", ["linfonodo mesentérico"], ["k-dc-mesenterico"], 13),
  ("p4-5", "explicar", "Linfócitos ativados na mucosa voltam à mucosa como efetores (endereçamento intestinal), com padrão funcional adequado ao tecido.", "lâmina 11; transcrição p. 36; Janeway 12.6", ["α4β7", "CCR9", "homing"], ["k-homing"], 11),
 ]),
 ("Tolerância: dendrítica soft", "14-17", [
  ("p5-1", "organizar", "O intestino precisa de tolerância à comida, tolerância aos comensais e resposta a patógenos.", "lâmina 14; transcrição p. 38", ["tolerância oral"], ["k-tres-tarefas"], 14),
  ("p5-2", "explicar", "Ácido retinoico, derivado da vitamina A feito pelo epitélio e pela dendrítica, torna a dendrítica da mucosa tolerogênica.", "lâminas 15–16; transcrição p. 40–42; Janeway (DC CD103+)", ["ácido retinoico", "vitamina A"], ["k-ac-retinoico"], 16),
  ("p5-3", "decorar", "A dendrítica tolerogênica produz IL-10 e IDO e induz Treg.", "lâmina 16; transcrição p. 42", ["IL-10", "IDO", "Treg"], ["k-dc-il10-ido"], 16),
  ("p5-4", "distinguir", "Uma minoria de dendríticas da mucosa é pró-inflamatória, para responder a patógeno.", "lâmina 17; transcrição p. 44", ["pró-inflamatórias"], ["k-dc-proinfl"], 17),
 ]),
 ("PRR fora da superfície apical", "18-19", [
  ("p6-1", "explicar", "O epitélio intestinal não tem PRR na face apical; TLR ficam na basolateral e NLR no citosol, então só a invasão ativa resposta.", "lâminas 18–19; transcrição p. 46–48; apostila", ["basolateral", "apical"], ["k-prr-basolateral"], 19),
 ]),
 ("IgA secretora", "20-21", [
  ("p7-1", "explicar", "A IgA da mucosa só neutraliza (bloqueia adesão de microrganismos e toxinas), sem complemento, opsonização ou inflamação.", "lâmina 20; transcrição p. 50, 58; apostila; prova", ["neutraliza"], ["k-iga-neutraliza"], 20),
  ("p7-2", "decorar", "TGF-β favorece a troca de classe para IgA na mucosa.", "transcrição p. 52; Janeway 12.11", ["TGF-β"], ["k-tgfb-iga"], 20),
  ("p7-3", "explicar", "IgA dimérica (cadeia J) liga o receptor de imunoglobulina polimérica na face basolateral e atravessa o epitélio por transcitose.", "transcrição p. 54; Janeway 12.11; Armando", ["pIgR", "transcitose", "cadeia J"], ["k-pigr"], 20),
  ("p7-4", "explicar", "O componente secretor (parte do pIgR) fica ligado à IgA e a protege das proteases do lúmen.", "transcrição p. 54", ["componente secretor"], ["k-componente-secretor"], 20),
  ("p7-5", "decorar", "Na mucosa intestinal predominam plasmócitos produtores de IgA, na lâmina própria.", "lâmina 21; transcrição p. 56", ["plasmócitos", "IgA"], ["k-plasmocitos-iga"], 21),
 ]),
 ("Células reguladoras e a troca Treg → Th17", "22-27", [
  ("p8-1", "organizar", "A mucosa induz Treg FoxP3+, Th3 produtoras de TGF-β e Tr1 produtoras de IL-10.", "lâmina 22; transcrição p. 58–60", ["FoxP3", "Th3", "Tr1"], ["k-reguladoras"], 22),
  ("p8-2", "e-se", "Sem IL-10 há inflamação intestinal grave (colite).", "transcrição p. 60", ["IL-10"], ["k-il10-colite"], 22),
  ("p8-3", "distinguir", "TGF-β sem IL-12 leva o CD4 a Th3/Treg; TGF-β com IL-6 leva a Th17: a IL-6 decide.", "lâminas 23–26; transcrição p. 62–66", ["IL-6", "Th17"], ["k-treg-th17"], 25),
  ("p8-4", "decorar", "Th17 produz IL-17, IL-21 e IL-22, que recrutam neutrófilos.", "lâmina 26; transcrição p. 68", ["IL-17", "neutrófilos"], ["k-th17-citocinas"], 26),
  ("p8-5", "e-se", "Na infecção o MALT induz Th1, ou Th2 contra helmintos; efetores da lâmina própria saudável ficam balanceados pelas Treg.", "lâmina 27; transcrição p. 70", ["Th1", "Th2", "helmintos"], ["k-infeccao-th1-th2"], 27),
  ("p8-6", "explicar", "Hipótese da higiene: menos exposição microbiana na infância deixa a regulação mal treinada e aumenta alergias.", "transcrição p. 72–74 (lâmina ausente do PDF)", ["hipótese da higiene"], ["k-higiene"], 27),
 ]),
 ("Olho imunoprivilegiado", "28-29", [
  ("p9-1", "organizar", "A câmara anterior do olho é imunoprivilegiada: poucos vasos (nenhum na córnea), humor com TGF-β e epitélio com FasL e PD-L1.", "lâmina 29; transcrição p. 78", ["imunoprivilegiado", "FasL", "PD-L1", "TGF-β"], ["k-olho"], 29),
  ("p9-2", "explicar", "FasL do epitélio induz apoptose do linfócito que chega; o privilégio existe porque inflamação comprometeria a visão.", "lâmina 29; transcrição p. 78", ["FasL"], ["k-olho-fasl"], 29),
 ]),
]
TITULOS = {1: "Capa: Imunidade das mucosas, regulação tecido-específica", 28: "Divisória: Locais imunoprivilegiados (regulação tecido-específica)"}
SLIDE_TIT = {2:"MALT, GALT e BALT",3:"Tonsila (histologia)",4:"Placas de Peyer no íleo, corte transversal",5:"Placas de Peyer, aumento médio",6:"Placa de Peyer, centro claro",7:"Linfócitos intraepiteliais e da lâmina própria",8:"Nódulo linfoide solitário do intestino grosso",9:"Intestino saudável",10:"Intestino infectado",11:"Retorno dos linfócitos à mucosa",12:"Esquema do GALT: Paneth, caliciforme, célula M, dendrítica",13:"Esquema: duas vias de indução",14:"Tolerância e resposta a patógenos",15:"Dendríticas soft",16:"Ácido retinoico, IL-10, IDO, Treg",17:"Dendríticas pró-inflamatórias",18:"Sem PRR apical",19:"Figura: PRR basolateral e citosólico",20:"IgA",21:"Figura: plasmócitos IgA × IgG no cólon",22:"Células reguladoras",23:"Transição Treg/Th17",24:"Figura: diversidade de CD4",25:"TGF-β sem IL-12 → Th3",26:"TGF-β + IL-6 → Th17",27:"Efetores balanceados; infecção Th1/Th2",29:"Olho: câmara anterior"}
FORA = [
 {"o_que": "Desenvolvimento da imunidade intestinal pré-natal, neonatal e após desmame (defensinas, TLR4, IgA do leite)", "motivo": "fala sobre lâmina ausente do PDF, sem objetivo cobrado; detalhe de desenvolvimento fora do núcleo"},
 {"o_que": "Número de bactérias (100 trilhões × 10 trilhões de células)", "motivo": "ilustração da magnitude; o princípio (tolerar comensais) tem card"},
 {"o_que": "Deficiência seletiva de IgA", "motivo": "outra aula: 51 Distúrbios do sistema imune (imunodeficiências)"},
 {"o_que": "Tolerância periférica geral (anergia, CTLA-4, deleção)", "motivo": "outra aula: 72 Regulação do sistema imune"},
]
mapa = {"objetivos_da_aula": json.load(open(H/"compreensao-aula.json"))["o_que_a_aula_ensina"],
 "cronograma": {"aulas_vizinhas": ["07 Organização do sistema imune", "08 Reconhecimento inato (PRR)", "45 Ativação de T (subsets)", "49 Ativação de B (troca de classe)", "51 Distúrbios do sistema imune", "64 Hipersensibilidade", "72 Regulação do sistema imune", "81 Imunologia dos tumores"],
  "conferido": "Pastas UC03/Imunologia do Drive e grade: 67 precede 72 (Regulação: tolerância geral, CTLA-4) e 81; deficiência de IgA é da 51; estrutura das Ig e troca de classe geral foram da 49; aqui só o que é próprio da mucosa."},
 "passos": [{"passo": p, "laminas": l, "itens": [{"id": i, "tipo": t, "o_que": o, "fonte": f, "termos": te, "cards": c} for i, t, o, f, te, c, _ in its]} for p, l, its in PASSOS],
 "fora": FORA, "extras_fora_da_aula": []}
json.dump(mapa, open(H/"mapa-de-profundidade.json", "w"), ensure_ascii=False, indent=1)
mot = {"_como": "F-20261023-CLAUDE-04. Congelado pela E3.", "motivacoes": []}
n = 0
for p, l, its in PASSOS:
    for i, t, o, f, te, c, lam in its:
        n += 1
        mot["motivacoes"].append({"id": f"m{n}", "item_mapa": i, "reconstruir": o, "por_que_dura": f"Passo '{p}' da imunidade de mucosa, base para entender alergia alimentar, doença inflamatória intestinal e vacina oral nas próximas UCs; lâmina {lam}.", "depois_de": "", "atendida_por": []})
json.dump(mot, open(H/"motivacoes.json", "w"), ensure_ascii=False, indent=1)
# inventário
bylam = {}
for p, l, its in PASSOS:
    for i, t, o, f, te, c, lam in its:
        for k in c: bylam.setdefault(lam, []).append((i, o[:90], k))
EXTRA = {5: ('p2-2','placa de Peyer em aumento médio','k-peyer-ileo'), 15: ('p5-2','dendríticas soft pelo microambiente','k-ac-retinoico'), 18: ('p6-1','sem PRR apical','k-prr-basolateral'), 23: ('p8-3','transição Treg/Th17 por uma citocina','k-treg-th17'), 24: ('p8-3','esquema de diferenciação CD4','k-treg-th17')}
for s_, v_ in EXTRA.items(): bylam.setdefault(s_, []).append(v_)
S = []
for s in range(1, 30):
    if s in TITULOS: S.append((s, "capa", TITULOS[s], []))
    else: S.append((s, "conteudo", SLIDE_TIT[s], bylam.get(s, [])))
vazias = [s for s, t, _, c in S if t == "conteudo" and not c]
inv = ['"""Inventário da 67 Imunidade de mucosas (UC03 P4, Imunologia), gerado por planejar.py a partir do material lido (E1)."""',
 'PREFIXO = "im67"', 'AULA = "67 Imunidade de mucosas (UC03 P4)"', 'EXC = "EXC: "', "SLIDES = ["] + [f" {x!r}," for x in S] + ["]",
 "JUSTIFICATIVAS = {'capa': 'capa ou divisória de seção, sem conteúdo'}",
 "CAPITULO = [('Janeway 8ª ed., cap. 12 Sistema Imune de Mucosa', [('j1', 'células M e captação', 'k-celula-m'), ('j2', 'pIgR e IgA secretora', 'k-pigr'), ('j3', 'DC CD103+ e ácido retinoico', 'k-ac-retinoico')])]",
 "EXERCICIOS = [('Provas UC03 (busca mucosa/IgA)', [('q1', 'sIgA neutraliza vírus entérico', 'k-iga-neutraliza'), ('q2', 'DC intestinal capta e apresenta', 'k-dc-mesenterico'), ('q3', 'geração de IgA de mucosa', 'k-pigr')]), ('Apostila guia de Imuno, Aula 11', [('a1', 'IgA neutraliza e bloqueia adesão', 'k-iga-neutraliza'), ('a2', 'TLR basolateral', 'k-prr-basolateral'), ('a3', 'IEL CD8 γδ', 'k-iel-cd8')])]"]
open(H/"inventario.py", "w").write("\n".join(inv) + "\n")
print("itens", n, "lâminas sem card:", vazias)
