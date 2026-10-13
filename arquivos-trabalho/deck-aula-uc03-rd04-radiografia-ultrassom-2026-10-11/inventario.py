"""Inventário atômico de Radiografia e ultrassom (UC03 P1, Radiologia; Preceptoria Radiologia 2024/2023/2020; 45 lâminas remontadas).
Material de base lido inteiro: lâminas I (2024, 41), II (2023, 40, duplica I) e III (2020, 36; fontes/slides.pdf junta I com as lâminas de tubo, artefatos de III),
transcrição da aula (Material Complementar II, 68 páginas), bibliografias da aula (Mat. Compl. III e IV: física do RX e do US), e-book de graduação cap. 1 e 2,
monitoria P1 (aula 1), apostilas de veteranos, provas pelo índice rad-02 (63 subquestões).
Cada ideia aponta para o card que a pergunta (chave do spec, lista, "sh-<nid>" ou "EXC: motivo" só em lâmina). Menção no verso não conta.
Escopo (F-20261012-CLAUDE-01): aula de princípios de RX e US; TC (05), RM (12), contrastes (56), radioterapia (84) e correlações patológicas têm aula própria.
"""
PREFIXO = "rd04"
AULA = "Radiografia e ultrassom (UC03 P1; Radiologia; Preceptoria Radiologia 2024)"
EXC = "EXC: "
JUSTIFICATIVAS = {}
RD02 = dict(rx_leito=1791810584247, rx_inicial=1791810584997, rx_escuro=1791810584496, radiopaco=1791810584619, radiolucente=1791810584747,
            exogeno=1791810575245, cumulativa=1791810574247, gravidez=1791810574372, nao_seccional=1791810569222, inc_pa_lat=1791810586046,
            pa_costas=1791810586171, plano_sag=1791810569472, plano_cor=1791810569598, plano_ax=1791810569777, us_leito=1791810569898,
            us_sem_rad=1791810571022, us_doppler=1791810572322, us_operador=1791810571147, us_limites=1791810570272, us_hiper=1791810571947,
            us_hipo=1791810572071, cisto=1791810570147, us_biliar=1791810565995)
S = lambda k: f"sh-{RD02[k]}"
EX_ILUS = "EXC: exemplo ilustrativo da lâmina (F-20261012-CLAUDE-01)"

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Por que ainda usar radiografias?",
  [("a1", "Rápida, barata, acessível e pode ir ao leito", [S("rx_leito"), S("rx_inicial")]),
   ("a2", "Radiografia normal ajuda a excluir doença grave (triagem)", "rx-triagem")]),
 (3, "conteudo", "Primórdios: Röntgen, 1895", [("a3", "Röntgen descobriu o raio X em 1895; raio X atravessa papel, madeira e corpo; Nobel de Física em 1901", "roentgen")]),
 (4, "conteudo", "Radiações", [("a4", "Radiação é energia em trânsito (partículas ou ondas eletromagnéticas); fontes naturais e artificiais", "radiacao-def")]),
 (5, "conteudo", "Raio X: onda eletromagnética", [("a5", "Onda eletromagnética de alta energia", "xray-em"), ("a6", "Comprimento de onda 10^-12 m e frequência 10^16 Hz; acima do UV", "xray-em")]),
 (6, "conteudo", "Tubo de raios X (esquema)",
  [("b1", "Filamento de tungstênio aquecido libera elétrons", "tubo-filamento"), ("b2", "Diferença de potencial acelera elétrons ao ânodo", "tubo-aceleracao"),
   ("b3", "Elétrons no alvo de tungstênio geram raios X", "tubo-colisao")]),
 (7, "conteudo", "Produção: tungstênio", [("b4", "Tungstênio: número atômico e ponto de fusão altos", "tungstenio")]),
 (8, "conteudo", "Produção: tubo de vidro, chumbo, óleo, vácuo e abertura única",
  [("b5", "Chumbo e abertura única", "tubo-chumbo"), ("b6", "Óleo resfria; vácuo interno", "tubo-oleo-vacuo")]),
 (9, "conteudo", "Produção: calor, radiação característica, frenagem e choque nuclear",
  [("b7", "Maior parte da energia vira calor", "tubo-calor"), ("b8", "Radiação de frenagem", "bremsstrahlung"), ("b9", "Radiação característica", "caracteristica"),
   ("b10", "Choque nuclear", "EXC: terceiro processo listado no slide sem explicação na aula nem no livro; pergunta ao Davi")]),
 (10, "conteudo", "Foto do tubo de raio X", [("b11", "Aparelho emite radiação só enquanto ligado (fala)", "rx-so-ligado")]),
 (11, "conteudo", "Arranjo fonte, paciente e detector",
  [("c0", "Paciente entre a fonte e o detector", "detector"), ("c0b", "Detector: filme/écran e depois digital", "film-digital")]),
 (12, "conteudo", "Analogia da sombra (fonte pontual)", [("c0c", "Sombra maior quando o objeto se afasta do anteparo (explicada na lâmina de magnificação)", ["magnificacao", "divergencia"])]),
 (13, "conteudo", "Produção da imagem: espessura e absorção",
  [("c1", "Imagem depende da interação do raio X com o objeto", "atenuacao-imagem"), ("c2", "Espessura e capacidade de absorção", "espessura"),
   ("c3", "Mais absorção, mais branco", S("rx_escuro"))]),
 (14, "conteudo", "Densidades radiológicas (ovo)",
  [("c4", "Cinco densidades: ar, gordura, água, cálcio, metal", "densidades"), ("c5", "Radiotransparente e radiopaco", [S("radiopaco"), S("radiolucente")]),
   ("c6", "Hiperatenuante para áreas brancas", "hiperatenuante"), ("c7", "Ovo: casca, clara, gema e ar", "EXC: exemplo ilustrativo (ovo); a sequência das densidades está no card de densidades")]),
 (15, "conteudo", "Densidades na radiografia de abdome", [("c8", "Radiografia de abdome com ar, gordura, osso e metal", "EXC: exemplo ilustrativo da sequência de densidades")]),
 (16, "conteudo", "E quando as densidades são iguais? (bário e vasos)",
  [("c9", "Densidades iguais pedem contraste exógeno", S("exogeno")),
   ("c10", "Bário no intestino e iodo nos vasos", "EXC: contrastes específicos são tema da aula 56 (Contrastes radiológicos); card exógeno associado")]),
 (17, "conteudo", "Efeito biológico",
  [("d0", "Radiação ionizante remove elétrons", "ionizante-def"), ("d1", "Efeito direto no DNA", "efeito-direto"), ("d2", "Efeito indireto por radicais livres", "efeito-indireto"),
   ("d3", "Uso em radioterapia", "radioterapia"), ("d4", "Nem sempre dose dependente (estocástico)", "estocastico"),
   ("d5", "Efeito cumulativo e teratogênico (slide III)", [S("cumulativa"), S("gravidez")]), ("d6", "Proteção radiológica e feixe divergente", "protecao")]),
 (18, "conteudo", "Exercício prático: a caixa", [("e0", "Caixa com pedras e sementes usada para entender a projeção", "EXC: introdução do exercício prático; o conceito está nos cards de projeção")]),
 (19, "conteudo", "PA = vista de cima",
  [("e1", "Radiografia é projeção: perde-se uma dimensão e as estruturas se sobrepõem", ["perda-dimensao", S("nao_seccional")])]),
 (20, "conteudo", "Perfil = vista de lado", [("e2", "O perfil mostra a profundidade que o PA não mostra", "perfil-profundidade")]),
 (21, "conteudo", "Planos e eixos do corpo", [("e3", "Planos sagital, frontal e horizontal", [S("plano_sag"), S("plano_cor"), S("plano_ax")]), ("e3b", "Eixos longitudinal, anteroposterior e laterolateral", "eixos-corpo")]),
 (22, "conteudo", "Incidência PA no tórax", [("e4", "Reconhecer a radiografia de tórax em PA", "io-pa"), ("e5", "PA: feixe entra pelas costas; tórax em PA e perfil", [S("pa_costas"), S("inc_pa_lat")]), ("e5b", "PA: paciente de frente para o detector", "pa-paciente")]),
 (23, "conteudo", "Incidência em perfil", [("e6", "Reconhecer a radiografia de tórax em perfil", "io-perfil"), ("e7", "Perfil: feixe de lado a lado", "perfil-feixe")]),
 (24, "conteudo", "Magnificação: três pedras do mesmo tamanho", [("f1", "Objeto afastado do detector é ampliado", "magnificacao")]),
 (25, "conteudo", "Esquema da magnificação", [("f2", "Divergência do feixe a partir de uma fonte pontual", "divergencia")]),
 (26, "conteudo", "PA × AP no tórax", [("f3", "Tórax em PA limita a magnificação do coração", "pa-magnificacao"), ("f4", "AP no leito aumenta falsamente o coração", "ap-coracao")]),
 (27, "conteudo", "Caixa: três compartimentos com quantidades diferentes de cimento",
  [("f5", "Quantidade e espessura de material influenciam a imagem (mamografia comprime a mama)", "mamografia"),
   ("f6", "A pedra some quando o cimento é mais denso ao redor (introdução da silhueta)", "silhueta-def")]),
 (28, "conteudo", "Radiografia de tórax e de abdome", [("f7", "Aorta visível no tórax, mas não no abdome", "aorta")]),
 (29, "conteudo", "Sinal da silhueta",
  [("f8", "Densidades semelhantes juntas perdem o contorno", "silhueta-def"), ("f9", "Separadas mantêm o contorno", "silhueta-separadas"),
   ("f10", "Pneumonia em contato com o coração apaga a silhueta", "silhueta-pneumonia")]),
 (30, "conteudo", "Orientação (DIR)", [("f11", "Lado direito da imagem é o direito do paciente", "orientacao-rx")]),
 (31, "conteudo", "Ultrassonografia (abertura)", [("g0", "Título da seção de ultrassonografia", "EXC: abertura de seção sem conteúdo próprio")]),
 (32, "conteudo", "Vantagens do ultrassom",
  [("g1", "Não invasivo ou minimamente invasivo (punções guiadas)", "minimamente-invasivo"), ("g2", "Não usa radiação ionizante", S("us_sem_rad")),
   ("g3", "Doppler: hemodinâmica", [S("us_doppler"), "doppler-def", "doppler-direcao", "doppler-cor", "doppler-estenose", "doppler-enxerto"]),
   ("g4", "Barato e portátil", "barato-portatil"), ("g5", "Pode ir ao leito, rápido e dinâmico", S("us_leito")),
   ("g6", "Primeira escolha para fígado e vesícula; ecocardiograma", ["figado-us", S("us_biliar"), "ecocardiograma"])]),
 (33, "conteudo", "Desvantagens do ultrassom", [("g7", "Operador dependente", S("us_operador")), ("g8", "Obesidade e distensão gasosa", S("us_limites"))]),
 (34, "conteudo", "Som: onda mecânica", [("h1", "Onda mecânica que precisa de um meio", "onda-mecanica"), ("h2", "Ultrassom acima de 20.000 Hz", "ultrassom-hz")]),
 (35, "conteudo", "Formação da imagem: transdutor e piezoelétrico",
  [("h3", "Material piezoelétrico no transdutor", "piezo"), ("h4", "Transdutor emite e recebe", "piezo-recebe"), ("h5", "Tempo do eco dá a profundidade", "tempo-profundidade"),
   ("h6", "Intensidade do eco dá o brilho", "intensidade-brilho"), ("h7", "Reflexão depende da diferença de impedância", ["impedancia-reflexao", "impedancia-def"]),
   ("h8", "Gel elimina o ar entre transdutor e pele (fala)", "gel")]),
 (36, "conteudo", "Ilustração da onda emitida e refletida", [("h9", "Onda emitida, refletida e captada", "piezo-recebe")]),
 (37, "conteudo", "Equipamentos e transdutores",
  [("h10", "Frequência alta: melhor qualidade e menor penetração", ["freq-resolucao", "atenuacao", "pgr"]), ("h11", "Atenuação: osso, ar, músculo, sangue", "bamb"),
   ("h12", "Alta frequência para estruturas superficiais e baixa para profundas", "freq-superficial"), ("h13", "Sonda cavitária de frequência maior (fala)", "cavitario"),
   ("h14", "Aparelhos de carrinho, portátil e de bolso", "EXC: fotos de aparelhos sem fato adicional")]),
 (38, "conteudo", "Orientação transversal (DIR, ANT)", [("i1", "Corte transversal gera imagem axial", "us-transversal"), ("i2", "Topo da tela é o mais próximo do transdutor", "us-topo-tela")]),
 (39, "conteudo", "Orientação longitudinal (SUP, ANT)", [("i3", "Corte longitudinal gera imagem sagital", "us-longitudinal")]),
 (40, "conteudo", "Descritores ecogênicos",
  [("i4", "Hiper e hipoecogênico", [S("us_hiper"), S("us_hipo")]), ("i5", "Isoecogênico", "isoecogenico"),
   ("i6", "Anecogênico: líquido (bexiga, vasos, ascite)", [S("cisto"), "anecoico-liquido"]), ("i7", "Descritor identifica a modalidade; gordura difere do RX", ["descritor-modalidade", "gordura-us"]),
   ("i8", "Fígado, nódulo hipoecoico e bexiga como exemplos", "EXC: imagens ilustrativas dos descritores (fígado, hemangioma, bexiga)")]),
 (41, "conteudo", "Artefatos (slide III)", [("i9", "Erros de apresentação por equipamento, interação som-tecido e técnica", "artefato-us")]),
 (42, "conteudo", "Sombra acústica posterior",
  [("i10", "Alta atenuação ou reflexão impede ver estruturas posteriores", "sombra-mec"), ("i11", "Cálculos biliares e renais, calcificações e osso", "calculo-us"),
   ("i12", "Gás intestinal: sombra suja", "sombra-suja"), ("i13", "Reconhecer a sombra na imagem", "io-sombra")]),
 (43, "conteudo", "Reforço acústico posterior",
  [("i14", "Estrutura líquida produz faixa mais clara posterior", "reforco-us"), ("i15", "Baixa atenuação explica o reforço", "reforco-mec"), ("i16", "Reconhecer o reforço na imagem", "io-reforco")]),
 (44, "conteudo", "FAST",
  [("j1", "FAST: avaliação rápida em trauma", "fast-def"), ("j2", "Líquido livre é anecoico entre fígado e rim", "fast-liquido"), ("j3", "Quatro janelas em sequência fixa", "fast-pontos"),
   ("j4", "FAST não vê retroperitônio (apoio do AnKing)", "fast-retroperitoneo")]),
 (45, "capa", "Encerramento", []),
]
CAPITULO = [
 ("E-book de graduação em radiologia, cap. 2 (Ultrassonografia) e Material Complementar IV (Física da ultrassonografia)",
  [("k1", "Cristais piezoelétricos emitem e recebem; efeito piezoelétrico inverso", ["piezo", "piezo-recebe"]),
   ("k2", "Tempo do eco dá a profundidade; intensidade dá o brilho", ["tempo-profundidade", "intensidade-brilho"]),
   ("k3", "Impedância acústica define a reflexão", ["impedancia-reflexao", "impedancia-def"]),
   ("k4", "Frequência alta: melhor resolução e maior atenuação; escolha de sondas", ["freq-resolucao", "atenuacao", "freq-superficial", "pgr"]),
   ("k5", "Sombra acústica e reforço acústico posterior", ["sombra-mec", "reforco-us", "reforco-mec"]),
   ("k6", "Efeito Doppler, Doppler colorido e usos (fluxo, estenose, torção)", ["doppler-def", "doppler-direcao", "doppler-cor", "doppler-estenose"]),
   ("k7", "Gel de acoplamento elimina o ar", "gel"), ("k8", "Pontos fortes e limites do ultrassom", [S("us_leito"), S("us_limites"), S("us_operador")])]),
 ("E-book de graduação em radiologia, cap. 1 (Radiologia convencional) e Material Complementar III (Física das radiografias)",
  [("l1", "Tubo de raios X: cátodo de tungstênio, ânodo, alvo e vácuo", ["tubo-filamento", "tubo-aceleracao", "tubo-colisao", "tungstenio", "tubo-oleo-vacuo"]),
   ("l2", "Frenagem e radiação característica; 1 a 2% do feixe vira raio X", ["bremsstrahlung", "caracteristica", "tubo-calor"]),
   ("l3", "Projeção e magnificação", ["perda-dimensao", "magnificacao", "divergencia"]),
   ("l4", "Densidades radiográficas: ar, gordura, partes moles e osso", "densidades")]),
]
EXERCICIOS = [
 ("Provas UC03 (índice rad-02, 2015–2025)",
  [("p1", "Mecanismo de formação da imagem na radiografia (tungstênio, atenuação, mais branco)", ["tubo-filamento", "atenuacao-imagem", S("rx_escuro")]),
   ("p2", "Por que o tórax é feito em PA (magnificação)", ["pa-magnificacao", "ap-coracao"]),
   ("p3", "Primeiro exame e vantagens da radiografia no leito", [S("rx_leito"), S("rx_inicial"), S("inc_pa_lat")]),
   ("p4", "Hiperatenuante e radiopaco na radiografia", ["hiperatenuante", S("radiopaco")]),
   ("p5", "Mecanismo de formação da imagem do ultrassom (transdutor, piezoelétrico, tempo e intensidade)", ["piezo", "piezo-recebe", "tempo-profundidade", "intensidade-brilho"]),
   ("p6", "Doppler: técnica, princípio e função", ["doppler-def", "doppler-direcao", "doppler-estenose", "doppler-enxerto"]),
   ("p7", "Vantagens do US frente a TC, RX e RM", [S("us_sem_rad"), S("us_leito"), "barato-portatil"]),
   ("p8", "US como exame inicial do fígado", ["figado-us", S("us_biliar")]),
   ("p9", "Aspecto do cálculo: hiperecogênico com sombra; mecanismo da sombra", ["calculo-us", "sombra-mec"]),
   ("p10", "Cisto anecoico com reforço acústico posterior", ["reforco-us", "anecoico-liquido", S("cisto")]),
   ("p11", "Descritores para inferir a modalidade", ["descritor-modalidade", "isoecogenico", S("us_hiper"), S("us_hipo")]),
   ("p12", "Ecocardiograma como ultrassom", "ecocardiograma")]),
 ("Monitoria P1, aula 1 (Princípios básicos das radiografias e ultrassonografias)",
  [("m1", "Tungstênio, chumbo, óleo, vácuo, três processos de produção", ["tungstenio", "tubo-chumbo", "tubo-oleo-vacuo", "bremsstrahlung", "caracteristica"]),
   ("m2", "Cinco densidades; contraste quando as densidades são iguais; efeito letal e teratogênico", ["densidades", S("exogeno"), S("gravidez")]),
   ("m3", "Sinal da silhueta; espessura; mamografia", ["silhueta-def", "silhueta-pneumonia", "espessura", "mamografia"]),
   ("m4", "US: vantagens, desvantagens, ondas mecânicas, transdutor, ecogenicidade, artefatos", ["onda-mecanica", "piezo", S("us_operador"), S("us_limites"), "anecoico-liquido", "artefato-us"])]),
 ("Apostilas de veteranos (guia de Radiologia e UC3, aula 2)",
  [("v1", "Doppler mede velocidade e ajuda em estenoses", "doppler-estenose"), ("v2", "US é ideal para líquido e bom para fígado e vesícula", [S("us_biliar"), "figado-us", "anecoico-liquido"]),
   ("v3", "Cristais piezoelétricos convertem pulsos em energia elétrica", ["piezo", "piezo-recebe"])]),
]


# Análise do deck-prova 2026-10-13: itens cujo card saiu desta aula passam a exclusão com o motivo.
_RETIRADOS = {"rx-triagem": "detalhe", "roentgen": "historia", "tubo-aceleracao": "detalhe-tecnico", "tungstenio": "detalhe-tecnico", "tubo-chumbo": "detalhe-tecnico", "tubo-oleo-vacuo": "detalhe-tecnico", "tubo-calor": "detalhe-numerico", "bremsstrahlung": "detalhe-tecnico", "caracteristica": "detalhe-tecnico", "film-digital": "detalhe", "eixos-corpo": "repetido", "divergencia": "detalhe-tecnico", "mamografia": "exemplo", "minimamente-invasivo": "detalhe", "barato-portatil": "repetido", "doppler-cor": "detalhe", "doppler-estenose": "clinica", "doppler-enxerto": "clinica", "figado-us": "repetido", "impedancia-def": "detalhe-tecnico", "bamb": "detalhe", "pgr": "detalhe", "cavitario": "detalhe", "sombra-suja": "detalhe", "fast-def": "clinica", "fast-pontos": "clinica", "fast-retroperitoneo": "clinica"}
def _remap(dest):
    ds = [dest] if isinstance(dest, str) else list(dest)
    if any(isinstance(d, str) and d.startswith('EXC') for d in ds): return dest
    keep = [d for d in ds if d not in _RETIRADOS]
    if keep: return keep[0] if isinstance(dest, str) else keep
    return 'EXC: ' + 'tirado na análise do deck-prova (' + _RETIRADOS[ds[0]] + '): além do nível de ciclo básico desta aula ou repetido em outra aula'
SLIDES = [(n, t, tit, [(i, x, _remap(d)) for i, x, d in items]) for n, t, tit, items in SLIDES]
CAPITULO = [(t, [(i, x, _remap(d)) for i, x, d in items]) for t, items in globals().get('CAPITULO', [])]
EXERCICIOS = [(t, [(i, x, _remap(d)) for i, x, d in items]) for t, items in globals().get('EXERCICIOS', [])]


# Análise do deck-prova 2026-10-13: itens cujo card saiu desta aula passam a exclusão com o motivo.
_RETIRADOS = {"sh-1791810586171": "repetido"}
def _remap(dest):
    ds = [dest] if isinstance(dest, str) else list(dest)
    if any(isinstance(d, str) and d.startswith('EXC') for d in ds): return dest
    keep = [d for d in ds if d not in _RETIRADOS]
    if keep: return keep[0] if isinstance(dest, str) else keep
    return 'EXC: ' + 'tirado na análise do deck-prova (' + _RETIRADOS[ds[0]] + '): além do nível de ciclo básico desta aula ou repetido em outra aula'
SLIDES = [(n, t, tit, [(i, x, _remap(d)) for i, x, d in items]) for n, t, tit, items in SLIDES]
CAPITULO = [(t, [(i, x, _remap(d)) for i, x, d in items]) for t, items in globals().get('CAPITULO', [])]
EXERCICIOS = [(t, [(i, x, _remap(d)) for i, x, d in items]) for t, items in globals().get('EXERCICIOS', [])]
