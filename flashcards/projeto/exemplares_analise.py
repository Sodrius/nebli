"""Análise de cada EXEMPLAR e ANTI-EXEMPLAR (F-20261023-CLAUDE-02: “deixa anotado em cada exemplar uma análise sobre ele, porque é bom
ou ruim, como pode funcionar pros próximos”). `nebli.exemplares` junta estas análises aos arquivos gerados; o gate `exemplares_lidos`
exige análise para todo exemplar e anti-exemplar (novos inclusive): ao aparecer um novo, analisá-lo aqui antes do deck seguinte."""

# ---- EXEMPLARES (X de Davi): por que funciona e como usar ----
EXEMPLARES = {
 1791557942606: "Função + consequência num card só: azol bloqueia lanosterol→ergosterol e o verso diz o efeito (membrana vaza, fungo para). Custo-efetividade alta: um card carrega o mecanismo de uma classe inteira. Usar para todo alvo de fármaco/enzima: passo bloqueado no cloze, efeito no verso.",
 1792166970014: "Contraste complementar no mesmo índice com dica innate/adaptive: um lado não entrega o outro e o par organiza um grupo inteiro de doenças. Verso explica o critério (antígeno próprio × freio da inflamação). Modelo para todo par confundível.",
 1791625434983: "Fato decorável (CTLA-4) dentro de um mecanismo (retira B7 da APC) e verso com a consequência (sem B7, não ativa efetora). Curto, uma lacuna, nome específico. Modelo de molécula + o que ela faz + por que importa.",
 1791023354943: "Número que se decora (dois terços da saliva) com contexto mínimo e figura que mostra a glândula; verso acrescenta o tipo de secreção. Modelo de card de 'qual é o principal X' com ganho visual.",
 1791575024195: "Explica um limiar (contrátil × elétrico) cobrando a palavra que distingue os dois; verso põe os dois lados lado a lado com a figura. Modelo de card de fisiologia que ensina o processo e não só o nome.",
 1790979869860: "Simples e útil: hormônio → efeito (aumenta o apetite) e verso com o quando (sobe antes das refeições). Prova que card básico bem escrito tem lugar.",
 1791762418274: "Pergunta curta com dica 'potency or efficacy' que desfaz a ambiguidade e figura das curvas no verso. Modelo de conceito de gráfico: cobrar a leitura, mostrar o gráfico atrás.",
 1791630904844: "Contraste levedura × bolor no mesmo índice, com dica, e verso com o porquê funcional (α-glucano resiste à glucanase). Modelo de diferença estrutural ligada à virulência.",
 1791630906493: "AnKing clínico curto que liga a doença a um par confundível (TB) com os achados que se cobram; verso traz o quadro geral. Mostra quando clínica vale: quando ensina a distinguir.",
 1792166970767: "Organizador em pé, três mecanismos com dica da 1ª letra no mesmo índice e verso que liga cada mecanismo à doença monogênica. Modelo de organizador: conjunto + critério + consequência.",
 1792166971544: "AnKing: função (tolerância periférica) de uma molécula com o verso situando no sistema (checkpoint além da tolerância central). Modelo de 'para que serve' com contexto.",
 1792166978741: "Dois clozes paralelos (B → bacterianas, T → fungos e vírus) num índice só e mnemônico curto no verso. Alto custo-efetividade: uma regra que resolve muitas questões.",
 1792166976595: "Doença + alvo do anticorpo com o mecanismo inteiro no verso (bloqueio do receptor → menor potencial de placa). Mostra que o verso pode aprofundar o processo sem pesar a frente.",
 1791575690369: "Contraste brotamento × fissão binária cobrando os nomes e verso com o termo técnico (blastoconídio) e figura. Modelo de comparação morfológica com imagem que ensina.",
 1790981523773: "Oclusão de imagem bem feita (estrutura destacada, nome escondido). Modelo para anatomia: a figura é o card, o nome é a resposta.",
 1790999270833: "Definição curta com o termo no cloze e verso que diz onde ocorre. Modelo de definição útil (não abstrata).",
 1792261811401: "Duas lacunas complementares (giro e área) num card de localização; comentário de Davi pede que o verso explique o termo (somestésica). Usar: em card de área/estrutura, verso diz o que o nome significa.",
 1790981516405: "Ramo arterial com o que ele origina e verso que fecha a anastomose (superior × inferior). Modelo de anatomia relacional: um vaso, seus ramos, e a ligação com o próximo.",
 1792328931894: "Estrutura do Kenhub com nome em português e figura destacada; frase curta com a função anatômica (divide a medula). Modelo de card de estrutura que ensina o que ela é.",
 1791629593673: "Doença + defeito molecular (CD40L) e verso com a consequência (falha da troca de classe). Duas lacunas que se apoiam. Modelo de defeito → mecanismo → nome.",
 1792330247661: "Localização com uma referência fácil (abaixo do cérebro, inferior ao occipital) e figura. Card simples de orientação espacial.",
 1791625424957: "Pergunta direta (que proteína se associa ao MHC I) e verso com o contraste (MHC II → cadeia invariante). Modelo: uma pergunta + o par no verso.",
 1791716422184: "Citocina responsável pela manutenção do granuloma com o contraste no verso (IFN-γ ativa, TNF mantém). Modelo de 'quem faz o quê' com o par confundível explicado.",
 1791625430208: "Pergunta funcional com a resposta específica (IFN-γ) e verso com o efeito adicional (inibe Th2). Bom custo-efetividade: um card, dois fatos ligados.",
 1791983679330: "Tríade em tópicos com índices escolhidos (o núcleo c1, os outros c2). Modelo de organizador de tríade: em pé, nomes curtos.",
 1791631345241: "Recrutamento sequencial (Swi5 abre, SBF entra) cobrando o segundo ativador; verso explica a ordem e por quê. Davi pediu imagem e storytelling: usar com figura e ligado ao princípio que ilustra.",
 1791762416971: "Fármaco → sítio de ligação, com o porquê no verso (BZD precisa de GABA). Modelo de farmacologia por mecanismo, não por lista.",
 1791631347092: "Enzima com nome completo no cloze, verso com o que ela reconhece (CpG hemimetilado). Davi reescreveu o cloze: o nome específico é o que se decora.",
 1792350094380: "Estrutura do Kenhub (artéria) com seta e nome; modelo para neuroanatomia vascular.",
 1792166969765: "Organizador das falhas do sistema imune com dica da 1ª letra e verso que distingue cada falha e aponta a aula vizinha. Modelo de mapa da aula em 3 linhas.",
 1792328879263: "Estrutura do Kenhub em português com figura e seta. Modelo de card de estrutura.",
 1791762418025: "Contraste afinidade × atividade intrínseca com o termo no cloze e verso que aplica (antagonista: afinidade sem atividade). Alto custo-efetividade: define dois conceitos e uma classe de fármacos.",
 1790974689880: "Organizador com três características que distinguem o intestino grosso, cada uma num índice, e verso com a exceção (reto) e figura do livro. Modelo de 'como reconhecer X'.",
 1791629593848: "Pergunta funcional (o que aumenta na resposta humoral) e verso com a consequência clínica mínima (linfadenomegalia) e figura. Modelo de histologia funcional.",
 1790981523225: "Doença com o vaso causal e o quadro clássico no verso; clínica mínima e ligada à anatomia da aula.",
 1792175047836: "Contraste ecto × endotrix no mesmo índice com dica e verso com exemplos de agentes. Modelo de par complementar.",
 1791000313954: "Deficiência + causa (falta de bactérias) com a conduta no verso. Card clínico que ensina fisiologia (quem produz vitamina K).",
 1792588686964: "Organizador das raízes do nervo espinal com o mesmo índice nos dois lados (anterior/eferente) depois da edição de Davi. Modelo: o par que se completa fica no mesmo índice.",
 1792572870692: "Estrutura do Kenhub em português (cerebelo) com seta e figura destacada. Modelo de estrutura.",
 1791000306802: "Pergunta curta com a resposta conjunta (três monossacarídeos) e verso com a regra (mesmo transportador basolateral) e figura. Custo-efetividade: um card resolve a saída de todos.",
 1791631347467: "Modelo de custo-efetividade citado por Davi: em vez de só 'o que faz HDAC', cobra o efeito de inibi-la e a consequência (supressores voltam a ser transcritos), com verso que aprofunda (uso em linfoma/mieloma). Usar: função + o que acontece se bloqueada + consequência, num card só.",
}

# ---- ANTI-EXEMPLARES: famílias de erro (por que é ruim / o que fazer) ----
FAMILIAS = {
 "etimologia": "Card de etimologia (prefixo, sufixo, radical): termo vago ou impreciso ('x ou y', definição errada, avançado sem explicação). Lição geral: uma palavra no cloze, definição exata e comparação quando ajuda a reter.",
 "imagem": "Imagem ausente, genérica, com informação demais ou fora do contexto do card. A figura tem de mostrar exatamente o que o card cobra, pequena e direcionada; em aula visual (anatomia, histologia, embriologia) todo card leva figura real (gate v7).",
 "negrito": "Autoral sem negrito de contexto. AnKing negrita 1–2 termos que situam a frase fora do cloze; gate duro desde 23/10 (lint v7).",
 "cloze_longo": "Cloze com palavras demais: difícil de lembrar e de conferir. No máximo 3 palavras no cloze; o resto fica visível ou vai para o verso.",
 "cloze_local": "Cloze no lugar errado: esconde palavra genérica ou o que se entende, não o que se decora, ou o resto da frase entrega a resposta. Antes de escrever, perguntar 'o que Davi tem de guardar desta frase?' e esconder só isso.",
 "porque": "Verso que não explica: repete a frente ou falta o porquê. Todo verso traz a razão, a consequência ou o contraste, em 1–2 linhas.",
 "estranho": "Card estranho que não ensina: frase abstrata, sem processo, decora um nome solto. Custo-efetividade baixa. Reescrever para carregar um processo compreensível (o que acontece, por quê, e a consequência), como os exemplares.",
 "organizador": "Falta organizador ou organizador mal feito (deitado, numerado em linha). Quando a aula compara ou enumera, um organizador em pé, uma linha por item, com índices deliberados (gate v7: 3+ itens em frase reprova).",
 "aula": "Card da aula errada, fora do escopo ou clínica demais. Cada assunto mora numa aula; clínica lateral ≤ 7%; o deck é o que a aula ensina.",
 "sigla": "Sigla sozinha no card ou no cloze. Escrever o nome por extenso com a sigla junto; card tem de fazer sentido sozinho.",
 "tab": "Comentário sobre o Tab (explicação do Codex): Tab vago, em lista ou sem o porquê. Vale para o Tab: do básico ao aprofundamento, em texto corrido.",
 "io": "Card de estrutura/oclusão mal feito: cloze cobrindo a estrutura, seta errada, informação demais. Basta seta na estrutura destacada e o nome no cloze ao lado.",
 "repetido": "Card repetido ou muito parecido com outro: confunde e gasta revisão. Um fato, um card; o outro aspecto vai no verso ou em card com ganho próprio.",
 "dica": "Falta dica no cloze quando a pergunta é ambígua (parte do duodeno, fase, ramo de qual artéria). Dica curta no próprio cloze, sem entregar.",
 "cor": "Cor errada para a importância (HY rosa, detalhe verde). A cor segue a rubrica: HY 1–2 e pilares verdes, detalhe rosa.",
 "cobertura": "Deck incompleto ou com repetição no conjunto: faltou cobrir o que a aula/quiz ensina ou sobrou o mesmo fato várias vezes. Planejar a cobertura pelo slide antes de escolher cards (pipeline v7).",
 "elogio": "Na verdade é elogio ou correção feita por Davi: usar a versão atual como modelo (o que Davi mudou mostra o padrão certo).",
 "outro": "Comentário pontual de Davi; ler o literal e aplicar a correção específica.",
}
REGRAS = [  # (família, regex no comentário literal) — a primeira que casar
 ("elogio", r"bom exemplo|ficou top|tab bom|ótimo card|melhorei|ajustei|ajeitei|aprende o que|bela imagem"),
 ("aula", r"aula errada|deck errado|outro deck|conteúdo errado|não era a aula|não veio da aula|excesso de card de clínica|clínica desse deck|away|não desse deck"),
 ("organizador", r"organizador|tópicos|em pé|tabela|organiza|agrupar"),
 ("sigla", r"sigla"),
 ("negrito", r"negrito"),
 ("cloze_longo", r"mt grande|mt info no mesmo|muitas palavras|mts palavras|cloze mt|com mt info|mais de 4 palavras"),
 ("cloze_local", r"cloze (num|no) (local|lugar)|cloze zuado|local terr|local ruim|resposta (nele|no card|por oposição|tava no card)|entrega|cloze aqui|cloze em algo|cloze .*fácil|abstrat"),
 ("dica", r"dica"),
 ("io", r"\bseta|cloze me atrapalha|cloze obstrui|(?-i:\bIO\b)|indicação da estrutura|cloze escondendo|cloze não tem seta"),
 ("imagem", r"imag|foto|IMAGEM|visual"),
 ("tab", r"\btab\b"),
 ("repetido", r"repetid|igual a esse|parecido|mesma coisa"),
 ("cor", r"rosa|verde"),
 ("porque", r"porqu|explica|\bcomentário|explicação|comparar"),
 ("cobertura", r"incompleto|não cobriu|faltou coisa|pensamento contínuo"),
 ("estranho", r"estranh|ruim|zuad|mal feito|mal escrito|não ensina|storytelling|não compreendi|o que isso|inutil|incoerente|melhorar|não ficou claro|bobo"),
 ("estranho", r"mal aplicada|pode melhorar|aprofundar|mais profundo|card que explica mais|mt info num card|fora da formatação|sentido sozinho|não compreendo|não sei o que é|avançado|baixa qualidade|ajudar num processo|impressão de que é só"),
 ("aula", r"sobre embrio|ao invés de sensitivo|cloze de forma manual|vasos curtos"),
 ("organizador", r"lista dos|card conexão|altura aqui no cloze|mais de um cloze por card"),
 ("cloze_longo", r"deveria ser um card só|forma manual|receptor coestimulador"),
 ("etimologia", r"\bx ou y\b|prefixo|sufixo|radical|-trofia|evaginação"),
 ("outro", r"."),
]
# Observação própria nos casos mais instrutivos (o literal de Davi está no arquivo gerado).
NOTAS = {
 1791762418521: "Cobra 'eficácia' numa curva sem ensinar a diferença potência × eficácia; o card bom pediria a relação (direita = menos potente, platô baixo = menos eficaz).",
 1791627549152: "Frase genérica sobre domínios do ativador, sem o experimento e sem por que importa: decorar 'activation domain' não ensina nada.",
 1791716432060: "Afirmação vaga ('cicatriza por fibrose') sem processo nem consequência concreta; Davi: 'o que isso sequer quer dizer?'.",
 1791628675323: "Cloze no local (membros inferiores) sem o porquê (trauma com solo e plantas); o card bom explica a causa e cobra o que se decora.",
 1792083296387: "A última parte da frase entrega o cloze; e o verso não explica por que a imunidade celular protege.",
 1791631344666: "Lista de modificações de histona sem pensamento contínuo: nomes soltos, sem dizer o que cada marca faz.",
 1791631343842: "Cloze em 'ATP' (genérico) e faltou o organizador que compara os mecanismos de remodelação.",
 1792624465974: "Símbolo 'E' sem definição: card não faz sentido sozinho (gate v7: símbolo de uma letra).",
 1792697128629: "Enumeração numerada em linha: devia ser organizador em pé (gate v7).",
 1792588686980: "Três itens em frase com três índices: virou organizador em pé com um índice e dica da 1ª letra.",
 1792659586974: "Organizador de embriologia sem dizer que é embriologia na frente (gate v7: contexto embriológico).",
 1792659598025: "Embriologia sem figura e sem aprofundamento; refeito com a figura do Langman (veias vitelinas → sinusoides).",
 1791627550702: "Fato isolado (FOXO1 fora do núcleo); Davi pediu a consequência em sequência: custo-efetividade é carregar o efeito (genes gliconeogênicos desligados) no mesmo card.",
 1791984889849: "Organizador deitado (1) ... 2) ... em linha): tem de ficar em pé, um item por linha.",
 1791762418773: "Expressão forte e ambígua ('zero efficacy'): quem não tem atividade? Escrever o sujeito e o conceito com precisão.",
}


def familia(comentario: str) -> str:
    import re
    for fam, rx in REGRAS:
        if re.search(rx, comentario or "", re.I):
            return fam
    return "outro"


def analise_anti(nid: int, comentario: str) -> str:
    fam = familia(comentario)
    nota = NOTAS.get(nid)
    return f"[{fam}] {FAMILIAS[fam]}" + (f" Aqui: {nota}" if nota else "")
