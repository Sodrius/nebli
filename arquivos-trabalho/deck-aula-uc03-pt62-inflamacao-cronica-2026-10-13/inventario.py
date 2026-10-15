"""Inventário atômico de Inflamação crônica (UC03 P3, Patologia; lâminas I Mauad (30) e II Ferraz da Silva (20)), escrito antes da seleção.
Material de base lido inteiro: lâminas I e II (vistas em visual/I-NN e II-NN), exercícios (7 perguntas) e palavras-cruzadas, provas pelo índice
pat-10 (7 subquestões 2015–2025), monitoria P3 de Patologia (aula 10) e apostila de veteranos (cap. 8), Robbins cap. 2 (inflamação crônica).
Não há transcrição falada: o “PDF de transcrição” da pasta pessoal e o Material Complementar II são as próprias lâminas II.
Cada ideia aponta para o card que a pergunta (chave do spec, lista, "sh-<nid>" ou "EXC: motivo" só em lâmina/apoio). Menção no verso não conta.
"""
PREFIXO = "pt62"
AULA = "Inflamação crônica (UC03 P3; Patologia; Mauad e Ferraz da Silva)"
EXC = "EXC: "
JUSTIFICATIVAS = {}
S = lambda n: f"sh-{n}"
IFN, M1, M2, TH1, MBP = S(1791625430208), S(1791625434032), S(1791625434457), S(1791625422657), S(1791780353397)

SLIDES = [
 (1, "capa", "Capa (Thais Mauad, 2020)", []),
 (2, "conteudo", "O problema da inflamação é falhar em resolver (Nathan & Ding)", [("a1", "Inflamação não resolvida contribui para aterosclerose, câncer, DPOC, artrite", "ic-nao-resolvida")]),
 (3, "conteudo", "Esquema: lesão tecidual → detecção → inflamação", [("a2", "Esquema da lesão e detecção", EXC + "ilustração do esquema geral; coberto pela inflamação início/resolução (aula 37)")]),
 (4, "conteudo", "Inflamação crônica: duração prolongada, destruição, tentativa de reparo, nem sempre após aguda", [
   ("a3", "Definição: duração prolongada, destruição tecidual e tentativa de reparo", "ic-def"),
   ("a4", "Estímulo que persiste ou resposta que se perpetua", "ic-persiste"),
   ("a5", "Nem sempre vem de uma inflamação aguda", "ic-sem-aguda")]),
 (5, "conteudo", "Causas mais comuns de inflamação crônica", [
   ("a6", "Infecções persistentes (TB, fungos, sífilis)", "ic-causa-infec"), ("a7", "Exposição prolongada a agentes tóxicos (sílica, aterosclerose)", "ic-causa-toxico"),
   ("a8", "Autoimunidade (artrite reumatoide)", "ic-causa-auto"), ("a9", "Doenças imunomediadas (alergia, asma)", "ic-causa-alergia")]),
 (6, "conteudo", "Histologia: células mononucleares, destruição, tentativa de cicatrização (tríade; polimorfonucleares; folículos; granulomas)", [
   ("a10", "Tríade histológica", "ic-triade"), ("a11", "Polimorfonucleares: atividade aguda ou lesão persistente", "ic-pmn"),
   ("a12", "Folículos linfoides", "terciario"), ("a13", "Granulomas", EXC + "tema da aula 47 Inflamação granulomatosa")]),
 (7, "conteudo", "Inflamação aguda × crônica (A × B, Robbins)", [("a14", "Reconhecer os dois padrões na histologia", "ic-img")]),
 (8, "conteudo", "Artrite reumatoide (mão e sinóvia)", [("a15", "Artrite reumatoide como inflamação crônica com folículos", "ra-foliculos"), ("a16", "Foto da mão", EXC + "foto clínica ilustrativa")]),
 (9, "conteudo", "Bronquiectasias (histologia e peça)", [("a17", "Bronquiectasia: inflamação crônica necrosante", "bronquiectasia")]),
 (10, "conteudo", "Minas de sericita no Paraná (Algranti 2005)", [("a18", "Exposição ocupacional e silicose", EXC + "exemplo ilustrativo; silicose tem cards na aula 47")]),
 (11, "conteudo", "Bronquite crônica pelo cigarro (histologia)", [("a19", "Inflamação crônica pelo cigarro", "neutro-fumo")]),
 (12, "conteudo", "Infiltrado inflamatório misto: plasmócitos, macrófagos e eosinófilos", [("a20", "Infiltrado misto", "ic-infiltrado")]),
 (13, "conteudo", "Células envolvidas: macrófago (principal, origem na medula)", [("a21", "Macrófago como principal célula", "mac-principal"), ("a22", "Origem: monócito da medula", "mac-origem")]),
 (14, "conteudo", "Macrófago: migra na aguda; ativado por TLR, IFN-γ, fibronectina; aumenta tamanho, enzimas, metabolismo, fagocitose", [
   ("a23", "Ativadores: IFN-γ", IFN), ("a24", "Efeitos da ativação", "mac-ativacao")]),
 (15, "conteudo", "Sistema fagocítico mononuclear; vida média 1 dia no sangue, meses no tecido", [("a25", "Sistema fagocítico mononuclear", "mac-sfm"), ("a26", "Vida média", "mac-vida")]),
 (16, "conteudo", "Tabela: localização anatômica dos macrófagos", [("a27", "Nomes dos macrófagos por órgão (Kupffer, micróglia...)", EXC + "nomes por tecido: histologia/UC02, detalhe fora da aula")]),
 (17, "conteudo", "Ativação clássica (M1) e alternativa (M2)", [("a28", "M1 vem de microrganismos/IFN-γ (Th1)", M1), ("a29", "Função do M1", "mac-m1"), ("a30", "M2 vem de IL-4/IL-13 (Th2)", M2), ("a31", "Função do M2", "mac-m2")]),
 (18, "conteudo", "Substâncias secretadas pelos macrófagos", [
   ("a32", "Elastase, proteases, colagenase: destruição tecidual", "mac-destroi"), ("a33", "Complemento e citocinas recrutam células", "mac-recruta"),
   ("a34", "Fatores de crescimento", "mac-cresc"), ("a35", "Fatores de coagulação, lipase, NO, ROS", EXC + "lista de mediadores já nos Extras do card de destruição")]),
 (19, "conteudo", "Destino do macrófago: inflamação limitada × persistente", [
   ("a36", "Inflamação limitada: morte e drenagem linfática", "mac-limitada"), ("a37", "Persistente: recrutamento, proliferação local, imobilização", "mac-persiste"), ("a38", "MIF", "mac-mif")]),
 (20, "conteudo", "Outras células: linfócitos B e T ativados via macrófagos, liberam IFN-γ", [("a39", "Ciclo de retroalimentação macrófago–linfócito", "lin-loop")]),
 (21, "conteudo", "Imunidade inata e adaptativa na inflamação crônica (esquema)", [("a40", "Esquema da interação", "lin-loop")]),
 (22, "conteudo", "Tipos de linfócitos (Th1, Th2, Th17)", [("a41", "Th1 ativa macrófagos", TH1), ("a42", "Th2 e asma/eosinófilos", "lin-th2"), ("a43", "Th17 e autoimunidade", "lin-th17")]),
 (23, "conteudo", "Interação macrófago–Th1: células epitelioides e gigantes (granuloma)", [("a44", "Formação do granuloma", EXC + "tema da aula 47 Inflamação granulomatosa")]),
 (24, "conteudo", "Plasmócitos", [("a45", "Células B terminais que produzem anticorpos", "plasmocitos"), ("a46", "Tecido linfoide-like em órgãos não linfoides", "terciario")]),
 (25, "conteudo", "Tecido linfoide na inflamação crônica (linfonodo e hepatite crônica)", [("a47", "Folículos em órgãos não linfoides", "terciario")]),
 (26, "conteudo", "Bronquiolite folicular", [("a48", "Folículos na bronquiolite", EXC + "ilustração do folículo linfoide já coberto no card de tecido linfoide terciário")]),
 (27, "conteudo", "Mastócito", [("a49", "Mastócito (histamina)", "mastocito")]),
 (28, "conteudo", "Asma (via do mastócito/eosinófilo e histologia)", [("a50", "Remodelamento da asma crônica", "asma-remodelamento"), ("a51", "Vias de sinalização da asma", EXC + "hipersensibilidade tipo I: aula 64")]),
 (29, "conteudo", "Eosinófilos: eotaxina/CCR3 e MBP", [("a52", "Eotaxina e CCR3", "eos-eotaxina"), ("a53", "MBP", MBP)]),
 (30, "conteudo", "E os neutrófilos? Podem aparecer na inflamação crônica persistente (fumo)", [("a54", "Neutrófilos no fumante", "neutro-fumo"), ("a55", "Polimorfonucleares na crônica", "ic-pmn")]),
]
CAPITULO = [("Robbins, Bases Patológicas, cap. 2 (inflamação crônica)", [
  ("l1", "Inflamação crônica: duração prolongada, três características histológicas", ["ic-def", "ic-triade"]),
  ("l2", "Causas: infecções persistentes, exposição tóxica, autoimunidade", ["ic-persiste", "ic-causa-infec", "ic-causa-toxico", "ic-causa-auto"]),
  ("l3", "Monócito → macrófago; vida média; ativação por TLR e IFN-γ", ["mac-origem", "mac-vida", IFN, "mac-ativacao"]),
  ("l4", "Produtos do macrófago ativado: destruição e reparo", ["mac-destroi", "mac-recruta", "mac-cresc"]),
  ("l5", "Populações de macrófagos M1 e M2", [M1, "mac-m1", M2, "mac-m2"]),
  ("l6", "Linfócitos T e B, plasmócitos, eosinófilos, mastócitos", ["lin-loop", "plasmocitos", "eos-eotaxina", MBP, "mastocito"]),
  ("l7", "Inflamação granulomatosa", EXC + "assunto da aula 47 Inflamação granulomatosa"),
])]
EXERCICIOS = [
 ("Provas UC03 (índice pat-10-inflamacao-cronica, 7 subquestões 2015–2025)", [
  ("p1", "2025 P3 3.5: alterações estruturais da inflamação crônica nas vias aéreas (infiltrado, dano, fibrose; remodelamento)", ["ic-triade", "asma-remodelamento"]),
  ("p2", "2019 P3 4.4: elementos da inflamação crônica, células e mecanismos", ["ic-triade", "mac-principal", "lin-loop", "plasmocitos"]),
  ("p3", "2018 P3 4.2: relação entre inflamação crônica e fibrose (M2, TGF-β, fibroblastos)", ["mac-m2", "mac-cresc"]),
  ("p4", "2017 P3 4.1: células mononucleares (linfócitos e macrófagos) na hepatite viral crônica", ["ic-infiltrado", "ic-triade"]),
  ("p5", "2015 P2 3.4 e P2sub 3.2: reparo por cicatrização, fibrose em rim e pulmão", ["ic-triade", "mac-cresc"]),
  ("p6", "2015 P2 1.1: célula gigante multinucleada e epitelioides do granuloma (macrófagos ativados)", S(1791716424523))]),
 ("Exercícios da aula (Perguntas para Discussão 62), monitoria P3 (aula 10) e apostila de veteranos (cap. 8)", [
  ("e1", "Por que a inflamação crônica não resolvida é deletéria", "ic-nao-resolvida"),
  ("e2", "Doenças não infecciosas e infecciosas com inflamação crônica; células e mediadores", ["ic-causa-infec", "ic-causa-toxico", "ic-causa-auto", "ic-causa-alergia"]),
  ("e3", "Tipos de linfócitos e patologias em que predominam", [TH1, "lin-th2", "lin-th17"]),
  ("e4", "Inflamação crônica induzida pelo cigarro e células envolvidas", "neutro-fumo"),
  ("e5", "Subtipos de macrófagos e atuação (M1 × M2)", ["mac-m1", "mac-m2"]),
  ("e6", "O que são tecidos linfoides associados às mucosas", EXC + "tema da aula 07 Organização do sistema imune"),
  ("e7", "Quadros característicos: artrite reumatoide e bronquiectasia; folículos como órgãos linfoides terciários", ["ra-foliculos", "bronquiectasia", "terciario"]),
  ("e8", "Palavras-cruzadas: parasitas, Th1, hipersensibilidade, reparo", EXC + "palavras-cruzadas de revisão, sem alvo novo")]),
]

# O recorte final privilegia o mecanismo que se transfere entre doenças. Os
# detalhes retirados são ilustrações ou conteúdo de aulas específicas; se um
# item composto ainda tem alvo central, ele é mantido só com esses alvos.
_REMOVIDOS_MECANISMO = {'mac-sfm','mac-vida','mac-mif','lin-th17','mastocito',
                        'eos-eotaxina','neutro-fumo','ra-foliculos','bronquiectasia'}
_MOTIVO = EXC + 'F-20261013-CODEX-03: detalhe clínico ou de nomenclatura mantido como ilustração; mecanismo geral recuperado nesta aula e aprofundamento em aula própria'
def _recorte(d):
    if isinstance(d, (list, tuple)):
        kept = [x for x in d if x not in _REMOVIDOS_MECANISMO]
        return kept if kept else _MOTIVO
    return _MOTIVO if d in _REMOVIDOS_MECANISMO else d
SLIDES = [(n,c,t,[(i,x,_recorte(d)) for i,x,d in itens]) for n,c,t,itens in SLIDES]
CAPITULO = [(t,[(i,x,_recorte(d)) for i,x,d in itens]) for t,itens in CAPITULO]
EXERCICIOS = [(t,[(i,x,_recorte(d)) for i,x,d in itens]) for t,itens in EXERCICIOS]

# F-20261013-CODEX-05: o inventário acompanha a sequência causal final. As
# quatro listas de causas passam a testar duas formas de perpetuação; detalhes
# retirados continuam rastreados como exemplos ou em sua aula própria.
_SUBSTITUI = {
 'ic-causa-toxico': 'ic-causa-infec',
 'ic-causa-auto': 'ic-causa-infec',
 'ic-causa-alergia': 'ic-causa-infec',
 'ic-infiltrado': 'ic-triade',
 'mac-limitada': 'mac-persiste',
 'lin-th17': S(1791625422039),
}
def _logica(d):
    if isinstance(d, list):
        out=[]
        for x in d:
            y=_SUBSTITUI.get(x,x)
            if y not in out: out.append(y)
        return out
    return _SUBSTITUI.get(d,d)
SLIDES = [(n,c,t,[(i,x,_logica(d)) for i,x,d in itens]) for n,c,t,itens in SLIDES]
CAPITULO = [(t,[(i,x,_logica(d)) for i,x,d in itens]) for t,itens in CAPITULO]
EXERCICIOS = [(t,[(i,x,_logica(d)) for i,x,d in itens]) for t,itens in EXERCICIOS]

# A pergunta de 2015 é coberta na aula específica de granulomas; não cria uma
# associação deslocada neste deck.
EXERCICIOS = [(t, [(i,x, EXC + 'questão coberta na aula 47 Inflamação granulomatosa' if i == 'p6' else d)
                   for i,x,d in itens]) for t,itens in EXERCICIOS]

# Alvos que completam o mecanismo final e reutilizam notas vivas.
SLIDES = [(n,c,t, itens + ([("a43b", "Th17 recruta neutrófilos", S(1791625422039))] if n == 22 else []))
          for n,c,t,itens in SLIDES]
CAPITULO = [(t, itens + ([("l8", "Fibrose substitui parênquima e pode reduzir a função", S(1791716432060))]
                         if "Robbins" in t else [])) for t,itens in CAPITULO]
EXERCICIOS = [(t, [(i,x, S(1791716424523) if i == 'p6' else d) for i,x,d in itens])
              for t,itens in EXERCICIOS]

# F-20261013-CODEX-06: lacunas encontradas na conferência fonte por fonte.
_AUDITA = {
 "a19": "neutro-fumo",
 "a25": "mac-sfm", "a26": "mac-longevo", "a49": "mast-cronica",
 "a52": S(1791743343634), "a54": "neutro-fumo",
 "e3": [TH1, "lin-th2", S(1791625422039)],
 "e4": "neutro-fumo", "e6": "malt",
}
def _audita(itens):
    return [(i, x, _AUDITA.get(i, d)) for i,x,d in itens]
SLIDES = [(n,c,t,_audita(itens)) for n,c,t,itens in SLIDES]
CAPITULO = [(t,_audita(itens)) for t,itens in CAPITULO]
EXERCICIOS = [(t,_audita(itens)) for t,itens in EXERCICIOS]

# O Robbins reúne estes alvos na mesma seção de células da inflamação crônica.
CAPITULO = [(t, itens + ([
    ("l9", "Sistema fagocítico mononuclear e sobrevida longa dos macrófagos", ["mac-sfm", "mac-longevo"]),
    ("l10", "Mastócitos modulam a inflamação crônica por citocinas", "mast-cronica"),
    ("l11", "Eotaxina recruta eosinófilos", S(1791743343634)),
    ("l12", "Neutrófilos persistem em dano pulmonar pelo tabagismo", "neutro-fumo"),
  ] if "Robbins" in t else [])) for t,itens in CAPITULO]
