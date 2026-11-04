"""Análise de cada EXEMPLAR e ANTI-EXEMPLAR (F-20261023-CLAUDE-02: “deixa anotado em cada exemplar uma análise sobre ele, porque é bom
ou ruim, como pode funcionar pros próximos”). `nebli.exemplares` junta estas análises aos arquivos gerados; o gate `exemplares_lidos`
exige análise para todo exemplar e anti-exemplar (novos inclusive): ao aparecer um novo, analisá-lo aqui antes do deck seguinte."""

# ---- EXEMPLARES (X de Davi): por que funciona e como usar ----
EXEMPLARES = {
 1791575028298: "Contraste funcional curto: grelina relaxa o piloro e acelera o esvaziamento, em oposição à secretina e à CCK. O verso acrescenta contexto de jejum; conservar a relação, não transformar o X em aprovação de qualquer lista hormonal.",
 1792695019413: "Liga ligação ao receptor ao tropismo celular. O cloze recupera a consequência, e o verso dá exemplos de receptores sem tornar a lista o alvo. Modelo de mecanismo curto com consequência.",
 1792713409954: "Davi editou a frente em quatro linhas com uma pista inicial por região. O verso foi alinhado aos quatro itens em inglês e a figura real recortada; o elogio ao formato não dispensa conferir legibilidade móvel.",
 1792624465974: "Contrasta depuração hepática de alta extração, dependente do fluxo, com baixa extração, dependente da fração livre e capacidade intrínseca. A frente mantém contexto suficiente e o verso agora é curto.",
 1792065182152: "Davi elogiou explicitamente este organizador de micoses sistêmicas. A frente separa endêmicas e oportunistas, traz o critério do hospedeiro e agrupa agentes por categoria; o verso completa a diferença. Modelo para conjuntos com critério real, sem virar lista de nomes avulsos.",
 1792588686980: "Organizador refeito pelo comentário de Davi: três destinos da cavidade do tubo neural, um por linha, no mesmo índice com dica da 1ª letra, e o verso completa o quadro (prosencéfalo). Modelo de como um pedido de 'um só card em tópicos' vira um organizador que se lembra inteiro.",
 1791557942606: "Função + consequência num card só: azol bloqueia lanosterol→ergosterol e o verso diz o efeito (membrana vaza, fungo para). Custo-efetividade alta: um card carrega o mecanismo de uma classe inteira. Usar para todo alvo de fármaco/enzima: passo bloqueado no cloze, efeito no verso.",
 1792166970014: "Contraste complementar no mesmo índice com dica innate/adaptive: um lado não entrega o outro e o par organiza um grupo inteiro de doenças. Verso explica o critério (antígeno próprio × freio da inflamação). Modelo para todo par confundível.",
 1791625434983: "Fato decorável (CTLA-4) dentro de um mecanismo (retira B7 da APC) e verso com a consequência (sem B7, não ativa efetora). Curto, uma lacuna, nome específico. Modelo de molécula + o que ela faz + por que importa.",
 1791023354943: "Número que se decora (dois terços da saliva) com contexto mínimo e figura que mostra a glândula; verso acrescenta o tipo de secreção. Modelo de card de 'qual é o principal X' com ganho visual.",
 1791575024195: "Explica um limiar (contrátil × elétrico) cobrando a palavra que distingue os dois; verso põe os dois lados lado a lado com a figura. Modelo de card de fisiologia que ensina o processo e não só o nome.",
 1790979869860: "Simples e útil: hormônio → efeito (aumenta o apetite) e verso com o quando (sobe antes das refeições). Prova que card básico bem escrito tem lugar.",
 1791762418274: "Pergunta curta com dica 'potency or efficacy' que desfaz a ambiguidade e figura das curvas no verso. Modelo de conceito de gráfico: cobrar a leitura, mostrar o gráfico atrás.",
 1791630904844: "Contraste levedura × bolor no mesmo índice e verso com o porquê funcional: α-glucano externo mascara β-glucano do reconhecimento por dectina-1. A alegação antiga sobre β-glucanase foi retirada por falta de fonte.",
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
 ("elogio", r"bom exemplo|bom card|ficou top|tab bom|ótimo card|melhorei|ajustei|ajeitei|aprende o que|bela imagem"),
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
 1791627547475: "O contraste Mediator versus fatores gerais já estava na frente; o verso repetia demais. Encurtar para a ponte ativador–Mediator–complexo de pré-iniciação mantém o mecanismo e cabe na revisão rápida.",
 1791627549276: "Gal4 recruta coativadores; Mediator e modificadores da cromatina são exemplos, não uma camada obrigatória abaixo de outros coativadores. O verso agora diz isso sem lista longa.",
 1791628672497: "O pedido era comentar sintomas: edema crônico, fístulas e grãos na secreção, com a cor como pista para o agente. A figura fica no verso e ilustra o quadro.",
 1791631346842: "O verso passou a distinguir funções dos dois alvos: HDAC retira acetila e remodeladores reposicionam nucleossomos; ambos restringem acesso no contexto do promotor metilado.",
 1792175049737: "'Outra complicação' foi concretizada como fungemia por Malassezia furfur em imunocomprometido com cateter. O verso separa doença invasiva de pitiríase versicolor superficial e cita outros contextos.",
 1792624458027: "Os gráficos originais do AnKing foram mantidos com eixos distintos: primeira ordem lineariza ln[concentração], ordem zero lineariza concentração. O verso breve explica fração constante versus quantidade constante.",
 1792624465974: "O mecanismo de clearance hepático foi reduzido a fluxo na alta extração versus fração livre e capacidade intrínseca na baixa extração, sem repetir a frente nem perder o contraste.",
 1792657543181: "Um comentário longo sobre razão de extração foi condensado à equação clearance = fluxo × extração e sua consequência quando E se aproxima de 1.",
 1792677734151: "A frente e os índices editados por Davi foram preservados. O verso curto distingue critérios estruturais de genoma e classificação de Baltimore, sem voltar à lista confusa.",
 1792695026035: "A imagem comparativa já existia, mas era pequena. Ela foi ampliada; o verso só liga forquilha com primers de RNA a proteína terminal e hairpin como iniciações alternativas.",
 1792695026715: "O pedido de imagem foi atendido com recorte da figura da aula sobre a extremidade 5′. O verso explica a perda após retirar o último primer e situa as soluções sem afirmar que a figura mostre todas.",
 1792695030040: "O 'por quê' precisa diferenciar tarefas: Pol II celular transcreve genes no núcleo, enquanto a polimerase viral se adapta à replicação iniciada por proteína terminal.",
 1792695036313: "O organizador retroviral tinha frente e verso extensos. Ambos foram encurtados; tRNA e Pol II seguem como alvos distintos, negritos marcam etapas e RT/integrase ficam no card específico de HIV.",
 1792713409954: "A frente em português foi mantida como Davi a editou. O verso organiza quatro anastomoses em inglês, preservando preferência do deck, e a figura de Moore foi recortada para ler melhor no celular.",
 1792695024423: "Origin era alvo genérico de um card fraco. O processo útil é por que um vírus de DNA pequeno, mesmo usando polimerase celular, ainda precisa de iniciador viral que reconheça sua origem.",
 1792695052637: "A ideia mRNA versus genoma era boa, mas os clozes apenas repetiam nomes. A frente passou a contrastar a finalidade dos dois produtos; o verso qualifica o caso de RNA positivo.",
 1792695057292: "Why antivirals are few misturava desenvolvimento de fármacos e momento de tratamento. O título agora nomeia barreiras à terapia e as quatro causas formam dois grupos de dois clozes, como Davi pediu.",
 1791629587148: "Pedido de concentrar a maturação B num organizador com detalhes por etapa. O organizador 1792487516279 recupera os nomes e marcadores; esta nota avulsa foi suspensa, com histórico preservado.",
 1791716410077: "Repetia monócito → macrófago. A nota 1791983680358 já recupera o alvo e foi associada à aula de granuloma; a duplicata foi suspensa.",
 1792695018289: "A lista de suscetibilidade/permissividade não supria lacuna além do card 1792753617439. O formato de qualquer autoral deve ser justificado pela necessidade declarada antes da criação e pela comparação com os cards existentes.",
 1792787428653: "A lista genérica de fatores de infecção viral não acrescentava alvo útil ao organizador aprovado 1792787420154 nem aos cards específicos. A nota foi suspensa sem apagar comentário ou histórico.",
 1791627546552: "O comentário julga o conjunto BM46: autoral só se justifica quando cobre mecanismo da aula com alvo específico. Revisão individual dos autorais e correções de cards semelhantes; o gate de qualidade dessa corrida passou em 26/10.",
 1792117360419: "Elogio ao PT09 usado como padrão para P1. A cobrança concreta foi completar outras aulas: 19/19 inventários por lâmina e contagens vivas conferidos em 26/10, com seis cópias AnKing repostas em imunologia.",
 1792240186582: "Queixa de incompletude de IM08. Cinco notas ausentes foram repostas por cópias AnKing; o inventário por lâmina e a contagem do recibo passaram. Essa evidência mede presença e associação, enquanto o julgamento de suficiência didática depende do estudo.",
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


# Análises específicas da leva: cada nota guarda por que sua forma anterior falhou.
from pathlib import Path
import json
_analises_novas = Path(__file__).with_name("analises-feedback-20261027.json")
if _analises_novas.exists():
    NOTAS.update({int(nid): motivo for nid, motivo in json.loads(_analises_novas.read_text()).items()})
_analises_31 = Path(__file__).with_name("analises-feedback-20261031.json")
if _analises_31.exists():
    NOTAS.update({int(nid): motivo for nid, motivo in json.loads(_analises_31.read_text()).items()})


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


# F-20261023-CLAUDE-04: o que Davi suspendeu nos decks de Biomol (46, 52) e por quê — vale para todo autoral.
ANALISE_SUSPENSOS = ("Davi suspende o card que não o ajuda a gravar um mecanismo da aula a longo prazo. Os padrões: (1) moldura genérica sem "
    "mecanismo ('fígado e neurônio têm o mesmo genoma', 'a expressão é controlada em vários níveis', 'a maior parte da regulação é na "
    "iniciação', 'um gene tem dezenas de fatores'); (2) nome solto de uma cadeia picada em vários cards (TFIID, TFIIB, BRE, cauda da "
    "RNA pol II, cada um num card), em vez de um card que conta o processo; (3) detalhe de experimento ou de organismo-modelo sem o "
    "princípio que ele prova (Gal4/UAS, híbrido LexA, Pho4, geleia real, gêmeos, iPS); (4) número ou definição isolada (80% dos CpG, "
    "'HATs transferem acetil', constitutiva × facultativa, HP1, bromodomínio); (5) repetidos e AnKing fora do recorte (RNA pol I/II/III "
    "duplicados, 30 nm, lisina/arginina). O que ele mantém carrega função + consequência e se encaixa na história da aula: acetilação "
    "abre a cromatina, inibidor de HDAC volta a transcrever supressores, metiltransferase de manutenção copia a marca, repressor recruta "
    "HDAC, domínio de ligação × de ativação, FOXO1 fora do núcleo desliga a gliconeogênese. Regra: o autoral só nasce de um conceito "
    "que precisa durar (motivação) e carrega o processo, não o nome.")

# F-20261025-CODEX-02: X é preferência da versão vista, não certificado científico.
EXEMPLARES.update({
1791625436032: 'Contraste de destinos celulares sob TGF-β torna IL-6 uma condição discriminante. O comentário posterior ainda pede escrita melhor: conservar relação, melhorar formulação e Extra; X não encerra a crítica.',
1792659586974: 'Agrupa camadas por origem embrionária real, em duas linhas recuperáveis. A imagem foi explicitamente criticada por tamanho; formato aprovado não comprova legibilidade.',
1792166991941: 'Pergunta direta delimita o padrão mais comum, deixando a alternativa autossômica no verso. Exemplo de qualificador necessário, não de cortar palavras indiscriminadamente.',
1792175890134: 'Associa trajeto linfático e morfologia ao fungo; as direções de recuperação têm funções distintas. Não copiar fragmento lexical ou número de clozes sem avaliar a aula.',
1792677743147: 'Definição funcional induz vírion; Davi refez os destaques e aprovou a frente. Extra permaneceu criticado, portanto não apresentar o card inteiro como acabado.',
1791627547602: 'Conecta promotor, polimerase e fatores gerais; Davi elogiou especificamente a imagem. Conferir precisão da localização e reconhecer que Pol II depende dos fatores, sem atribuir reconhecimento direto à enzima.',
1791716432998: 'Necrose liga perda de contenção à liberação de bacilos e reinfecção. O alvo curto é parte de um processo, não exige trocar por nome mais raro.',
1792176896207: 'Morfologia ambiental liga artroconídio à entrada e mudança no hospedeiro. Conferir que cada irmão não entrega o outro; imagem não foi inspecionada nesta análise textual.',
1791627548028: 'Distingue fator específico de geral por local de ligação. A dica binária é legada: Q6B agora prefere categoria, sem desconsiderar a utilidade da distinção.',
1792677735547: 'Polaridade tem consequência imediata: servir de mensagem para tradução. Não generalizar infectividade de RNA positivo purificado para retrovírus; conferir contexto do grupo IV.',
1790981515127: 'Recupera ramo e origem arterial em contexto anatômico curto. Variações de origem precisam de qualificação quando relevantes; X não prova universalidade da anatomia descrita.',
1791625426108: 'Relaciona perfil imune à falha de controle celular, em vez de só nomear Th2. O contraste deve manter o foco de ciclo básico e evitar simplificação absoluta das respostas humanas.',
1791826286643: 'Pede interpretar gráfico e explica EC50 no verso, sem escrever a resposta na pergunta. Avaliação visual exige abrir a figura; texto sozinho não comprova a curva nem a resolução.',
1792677740101: 'Associa família à morfologia distintiva com figura. Não transformar a palavra “only” em regra geral sem o recorte de virologia médica; formato e exatidão são eixos separados.',
1792677742577: 'Relaciona genoma à capacidade de iniciar infecção, útil para distinguir necessidade de enzima transportada. As alternativas são legadas e o Extra tem texto colado; não copiar essa forma. Qualificar a afirmação sobre RNA positivo purificado.',
1792677740802: 'Liga RNA negativo à necessidade de polimerase viral antes da tradução. Explicitar que é RNA-dependente ajuda a reconstrução; presença em vírion e síntese posterior são elos distintos.',
1792677737476: 'Davi editou os polos visíveis para reduzir confusão: preservar esta escolha contextual. Quatro dimensões reais organizam o tema; não usar regra c1 automática para desfazer edição expressa.',
1792786398983: 'Template de reparo é requisito funcional para inserção dirigida; recupera o componente a partir do objetivo experimental. A recomendação do Extra sobre nickase depende do sistema e não fica validada pelo X.',
1791630175220: 'Resposta binária pode consolidar contraste conhecido, mas isolada não distingue junção precisa de indels após processamento de pontas. X registra preferência, não autoriza a generalização “HIGHLY error prone” como descrição de todo NHEJ.',
})

# Novos X recebidos até 26/10: registrar o aspecto aprovado e seu limite.
EXEMPLARES.update({
 1791000314427: 'Uma relação curta liga precursor cutâneo e luz UV; o verso completa a sequência hepática e renal. Modelo de etapa inicial com continuação no verso.',
 1791625426833: 'Apresentação por MHC I aparece como uma sequência de locais e transportadores, com cada etapa recuperada em um irmão. Usar para vias em que a ordem faz parte do mecanismo.',
 1791625431258: 'CD40–CD40L é discriminado pela função na célula B e comparado a B7–CD28 no verso. O comentário antigo sobre ambiguidade mostra por que indicar direção e resultado da interação.',
 1791625431383: 'Troca de classe é ligada à ajuda de T auxiliar, sem restringir indevidamente a Th2. O X aprova a versão editada por Davi; manter essa generalidade.',
 1792659591802: 'Organiza os destinos das alças do intestino médio por ramo e acrescenta o eixo da artéria mesentérica superior. A figura solicitada está no verso; conferir os índices dos irmãos ao imitar.',
 1792788317025: 'Recupera NLS a partir de um mecanismo de localização nuclear; o verso explica importina e qualifica que a fosforilação depende do sítio.',
 1791629595747: 'Pergunta direta recupera IgM e IgG, com o detalhe funcional da IgM no verso. É um par útil sem exigir duas notas independentes.',
 1791631346842: 'Liga leitores de CpG metilado a desacetilação e remodelação, com imagem do processo. O verso distingue leitura da marca de recrutamento direto; o X não dispensa o aprofundamento solicitado antes.',
 1792695051190: 'As duas enzimas do HIV aparecem em ordem causal: transcriptase reversa produz DNA e integrase o insere. Modelo de processo com verbos distintos, evitando nomes soltos.',
 1792695018715: 'Organiza o ciclo viral na ordem temporal em linhas curtas e distribui as lacunas pelos passos. O X aprovou a frente; depois da crítica à imagem, o gráfico de influenza e um esquema próprio provisório foram substituídos pelo slide 8 original da aula.',
 1792081475762: 'O X indica preferência por reunir causas de inflamação granulomatosa num organizador com exemplos por categoria; não atesta que cada exemplo tenha o mesmo peso.',
 1792787420154: 'Davi editou a formatação e elogiou o conjunto agudo, latente, persistente e progressivo. Modelo de organizador curto cujas categorias distinguem destinos da infecção.',
 1792677733803: 'O X aprovou uma versão anterior do contraste vírus versus células; a crítica posterior apontou critérios indevidos e verso ruim. A mudança atual exige novo julgamento de Davi.',
 1792787433932: 'O X marca preferência por agrupar funções de virulência com exemplos. Conservar a distinção entre replicar, espalhar e evadir; revisar a precisão de cada exemplo separadamente.',
 1791826286795: 'Davi escreveu melhorei e marcou X ao focar eficácia máxima no platô das curvas A e B. EC50 é potência e fica no verso.',
})

# 28/10: dois X novos (Davi marcou gostei)
EXEMPLARES.update({
1792713406304: 'X no card de identificação do colo da vesícula com seta e figura. O elogio se refere à identificação visual desta estrutura; conferir posição da seta antes de usar como modelo de outros alvos.',
1792659588552: 'A rotação do estômago desloca o mesogástrio dorsal e cria a bolsa omental atrás dele. O verso liga a bolsa ao forame epiploico e usa a figura de Langman; modelo de embriologia com movimento, consequência espacial e relação adulta.',
1791000308301: 'O X aprova uma cadeia clínica completa e curta: deficiência de enteropeptidase impede ativar tripsina, reduz digestão proteica e causa hipoproteinemia. Usar clínica quando ela testa uma consequência necessária do mecanismo; manter a imagem como apoio, não como a resposta.',
1792787231967: 'O X aprova organizar três modos de ação do RNA com um exemplo por linha. O comentário posterior reprova a palavra abstrata “scaffolding”: conservar a estrutura do organizador, mas escrever a ação observável — Xist recruta proteínas repressoras na cromatina.',
 1792659604802: "Sinusoide hepático ligado à permeabilidade do capilar: o cloze recupera 'descontínuo' e o verso ordena contínuo, fenestrado e sinusoidal por permeabilidade crescente, como Davi pediu em 26/10. O comentário de 27/10 pede o verso em tópicos; o X confirma a ordem, não dispensa o formato em tópicos.",
 1792173499322: "Forma de resistência dos fungos com nome decorável (clamidoconídio) e verso com o porquê (sobrevive a falta de nutriente, água ou temperatura ruim) e o exemplo concreto (Candida albicans em ágar fubá). Modelo de nome específico + função + onde se vê.",
})

# 04/11: X de 01–03/11 analisados antes do deck 64 (Claude).
EXEMPLARES.update({
 1791629595197: 'Neutralização como mecanismo: o anticorpo impede a ligação ao receptor da célula, cloze no alvo bloqueado. O verso diz qual classe neutraliza onde e traz o recorte do slide 43; modelo de função efetora de anticorpo com figura da aula.',
 1792713407379: 'Limites de um espaço anatômico no mesmo índice, com a estrutura que ele contém e a relevância cirúrgica no verso. O X veio depois de dois pedidos de imagem: a aprovação depende de figura que mostre o triângulo.',
 1793301692166: 'Contraste por mecanismo de formação: fusão viral dá sincício e fusão de macrófagos no granuloma dá célula gigante, cada linha com o critério visível. Modelo de organizador que separa dois achados parecidos pelo processo que os gera.',
 1790981526752: 'X num card de vascularização das vísceras cujo campo de texto aparece vazio no guia (card de imagem). O elogio vale para a identificação visual; conferir o card vivo antes de usá-lo como modelo.',
 1791000305576: 'Pergunta direta com resposta única e um princípio de absorção (só monossacarídeos atravessam o enterócito); o verso dá exemplos. Modelo de fato-chave que restringe uma regra geral.',
 1792659585353: 'Limites de um derivado embrionário em dois índices (início e fim), com os órgãos anexos no verso e figura. Modelo de fato situado em embriologia que delimita um território.',
 1792176893309: 'Nicho geográfico de um fungo com a dica de categoria Which fungus e mnemônico curto no verso. O X preserva o mnemônico e a figura; a pista dos vales de rios americanos foi depois considerada fora do Brasil e não deve se repetir na frente.',
 1793301690845: 'Consequência celular da infecção lítica: a maquinaria desviada para o vírus faz a célula parar de dividir. O verso corrige a ideia de síntese desligada, contrasta com vírus transformantes e liga ao acúmulo citopático; modelo de mecanismo com verso em três frases que puxam o vizinho.',
 1792695019915: 'Organizador de dois papéis sobre o mesmo eixo (ácido siálico): HA liga para entrar, NA cliva para sair, com o vírus nomeado. Davi chamou de top depois de pedir organizador para pares confundíveis; copiar o eixo comum e uma linha por papel.',
 1791000311352: 'Termo técnico decorável (solvent drag) definido pelo fenômeno na frente, com exemplos no verso. Modelo de nome de processo recuperado pela descrição mecânica.',
 1792753624591: 'AnKing que liga dois antígenos de superfície à variação antigênica, com drift e shift no verso. Davi escreveu ESSE FICOU TOP: a frente curta com o conjunto num índice e o verso que distingue os dois mecanismos é o atributo aprovado.',
 1792166977490: 'Base clínica de deficiência imune: o defeito (complemento precoce) prediz o local e o tipo de infecção, com dica de categoria location. Modelo de associação clínica que sai do mecanismo.',
 1793301694840: 'Evasão imune com causa e consequência: o vírus bloqueia MHC I e escapa do CD8; o verso traz o efeito oposto sobre NK. Modelo de mecanismo com contraponto no verso.',
 1791716425502: 'Contraste morfológico num índice com figura de cada tipo no verso, após dois comentários pedindo comparação e imagem. O verso limita a inferência (arranjo nuclear não prova causa); modelo de contraste visual com ressalva científica.',
 1792713404156: 'Formação de estrutura: componentes no mesmo índice e estrutura resultante em outro, frente em português, figura no verso. Davi melhorou e pediu que se aprenda; copiar a relação componentes → resultado.',
 1792659600102: 'Pergunta direta de embriologia sobre a origem de um ducto, com figura de Langman pedida por Davi. O verso herdado é tabela colada sem formatação; o X aprova a pergunta e a figura, não esse verso.',
 1792695052637: 'Dois produtos da replicação viral no mesmo índice (mRNA e cópias do genoma). Os comentários anteriores pediam escrita melhor e verso menor; o X aprova a versão encurtada, com a ressalva do RNA positivo no verso.',
 1792695056243: 'Mecanismo de saída do vírus da influenza com o vírus nomeado na frente, como Davi pediu. O último comentário ainda critica a imagem: o X aprova a frente, não a figura.',
 1792175888632: 'Organizador de conjunto com dica da primeira letra e o agente entre parênteses em cada linha; o verso distingue o achado tecidual e a via comum de entrada. Modelo de lista da aula declarada como principais.',
 1791630172795: 'Definição de uma classe de molécula pela função (regulação pós-transcricional), cloze no nome, verso com onde os genes ficam e figura. Modelo de fato-chave definido por função.',
})
