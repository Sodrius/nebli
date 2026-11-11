# Especificação curada — <AULA> (<UC> <Pn>, <componente>; <professor>; <N> lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral SÓ para lacuna provada em busca/cobertura.tsv (gate duro), último do último caso.
# Modelo vivo: arquivos-trabalho/deck-aula-uc03-rd02-diagnostico-radiologico-v2-2026-10-16/spec.py (16/10).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 17  # 17 = matriz de fontes cruzadas (matriz-fontes.json), revisor único e leitura por diferença (F-20261110-CLAUDE-01); 16 = cobertura por lâmina: ≤ 10% fora do recorte, motivo próprio, lâmina visual com figura (F-20261106-CLAUDE-01); 15 = alvo essencial por lacuna e avulsos cobertos; 14 = E7 antes de instalar, instalar por último (F-20261104-CLAUDE-02); 13 = auditoria de cobertura em dois sentidos no E7 (F-20261103-CODEX-02); 12 = tipos.tsv + verificador por casos que deram certo (F-20261101-CLAUDE-01); 11 = modo prova disponível; 10 = leitura obrigatória inteira e exemplo do professor como exemplo; 9 = revisor independente; 8 = motivação congelada na E3; 7 = passo a passo registrado
SECOES_MOTIVO = ""  # v7: se a aula é de princípio geral e nenhuma seção de recurso é do seu assunto, SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l] e o motivo aqui (≥ 60 caracteres)
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]  # arquivos de busca/secoes/ cujo assunto É o da aula (F-20261016-CLAUDE-06: todo AnKing do conteúdo entra, sem limite)
AUTORAL_EXCECAO = "Aula sem transcrição e de conceitos gerais (nomenclatura, cinética, critérios, metástase): o AnKing cobre fatos soltos, mas não os organizadores, a cinética (10^9 células, fração de crescimento) nem os conceitos da lâmina; cada autoral prova lacuna e está no mapa"  # só corridas com PIPELINE_VERSAO < 5; na 5 o autoral não tem teto, mas cada um prova lacuna em todos os acervos
MODO = "aula"  # "prova" = deck-prova independente das aulas (EXECUCAO › Modo prova)
PIPELINE = "anking-primeiro"  # F-20261015-CLAUDE-06: liga os gates duros (cobertura_anking, cores_rubrica, inducao_clozes); não remover
RUN_ID = "uc03-pt75-20261110a"
SHORT = "pt75"
LESSON = "2026-uc03-patologia-75-biologia-crescimento-tumores"
DECK = "NEBLI::UC03::P4::Patologia::75 Biologia e crescimento dos tumores"
CRITERIOS = "MEMORY.md + FEEDBACKS até F-20261110-CLAUDE-03 + pipeline v17 + GUIA-1 a GUIA-4, 10/11/2026"
_IMGS = ("cis", "clonal", "hallmarks", "prolif", "divisoes", "ciclo", "arvore")
MEDIA = {f"pt75-{n}.png": f"img/pt75-{n}.png" for n in _IMGS}
IMG = lambda n: f'<br><br><img src="pt75-{n}.png" style="width:100%;max-width:850px;height:auto">'
BUSCA = ("Três caminhos (10/11): seções de recurso do AnKing (busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt); "
         "significado em todos os acervos (busca/semantica.jsonl). ")
A_, B_, C_, D_, E_, F_, G_, H_, I_, J_, K_ = ("A-conceitos", "B-criterios", "C-anaplasia", "D-transformacao", "E-crescimento", "F-molecular", "G-invasao", "H-ciclo", "I-metastase", "J-predisposicao", "K-epidemiologia")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


def F(loc, trecho):
    return [{"localizador": loc, "trecho": trecho}]


EXCLUIDOS = [
 (1557670335053, "maiores incidências: fonte só Step 2 (gate); k-epi-ranking cobre com a lâmina da aula 74"),
 (1557670335329, "maiores mortalidades: fonte só Step 2 (gate); k-epi-ranking cobre"),
 (1518215368712, "displasia moderada cervical: frente lista as opções (resposta visível); k-sequencia-cis cobre a sequência com a figura da lâmina 6"),
 (1518218707562, "displasia grave/in situ cervical: lacuna longa e opções na frente; k-sequencia-cis e 1518218866119 cobrem"),
 (1488418638300, "lipossarcoma: repete verso e figura de 1496111000227 (lipoma × lipossarcoma) — revisor 11/11"),
 (1508802077152, "ovário semeia cavidades: repete 1508802208485 e 1518241882006 — revisor 11/11"),
 (1517720634146, "hamartoma não é neoplasia 'No*': o verso contradiz (muitos têm translocação clonal); 1517720929242 define hamartoma"),
 (1518215567480, "displasia pleomórfica: a lacuna esconde só o fragmento 'pleo' — revisor 11/11"),
 (1487461128880, "displasia reversível: a frente mostra as duas opções (resposta visível); k-displasia-anaplasia e o verso dizem que pode regredir"),
 (1518213589178, "grau de displasia cervical: frente lista as opções (resposta visível); 1518215368712 e 1518218707562 ficam com a figura"),
 (1518214486672, "displasia leve cervical: frente lista as opções (resposta visível)"),
 (1496111421676, "30 divisões: fundido em k-30-duplicacoes (30 e 1 g), que o revisor pediu"),
 (1518403036364, "pouco diferenciado é mais agressivo: resposta repete 1518402974215 (bem × pouco diferenciado)"),
 (1496164981778, "benigno não metastatiza (Não): resposta sim/não repete outros; k-criterios e 1518398337589 cobrem"),
 (1517720977040, "coristoma não é neoplasia (Não): mesma resposta de outros sim/não; 1517720994409 já define coristoma"),
 (1496164365674, "benigno bem diferenciado × maligno pouco: mesma resposta de 1518402974215"),
 (1791780359356, "outro assunto: leucócitos atravessam a membrana basal com colagenases (inflamação aguda, aula 37)"),
 (1791780363380, "outro assunto: inflamação crônica com infiltrado mononuclear e fibrose (aula 62)"),
 (1496110426551, "clonalidade por isoformas de G6PD: técnica laboratorial, não ensina a aula (basta saber que neoplasia é monoclonal)"),
 (1496110577714, "razão 1:1 de G6PD: técnica de clonalidade, fora da aula"),
 (1496110672620, "clonalidade pelo receptor de andrógeno: técnica, fora da aula"),
 (1496110698734, "clonalidade B por cadeia leve: hematologia (linfomas), outra UC"),
 (1496110724165, "cadeia kappa ou lambda: imunologia/hematologia, fora da aula"),
 (1496110744913, "razão kappa:lambda 3:1: hematologia, fora da aula"),
 (1496110779658, "kappa:lambda no linfoma: hematologia, fora da aula"),
 (1517714565997, "G6PD na hiperplasia: técnica de clonalidade, fora da aula"),
 (1517719483976, "G6PD na neoplasia: técnica de clonalidade, fora da aula"),
 (1517719509989, "G6PD e receptor de andrógeno no X: genética da técnica, fora da aula"),
 (1523570028468, "clonalidade T por rearranjo do TCR: hematologia, fora da aula"),
 (1518220691332, "mnemônico de tumores específicos que se disseminam por via hematogênica: ficha de órgãos, não ensina a via"),
 (1518220691333, "irmão do mnemônico acima: ficha de órgãos"),
 (1518241401324, "carcinomas semeiam o peritônio: repete 1518241882006 e 1508802077152"),
 (1517719786045, "tumores são benignos ou malignos: alvo trivial, sem conteúdo a decorar"),
 (1488418636531, "lipoma é o tumor benigno de partes moles mais comum: epidemiologia (aula 74)"),
 (1488418640215, "lipossarcoma é o maligno de partes moles mais comum: epidemiologia (aula 74)"),
 (1488418642113, "lipoblasto do lipossarcoma: histologia de sarcoma específico, fora do princípio de nomenclatura"),
 (1488418651374, "rabdomiossarcoma é o mais comum na criança: epidemiologia (aula 74)"),
 (1488418653159, "rabdomioblasto: histologia de sarcoma específico, fora do princípio"),
 (1516246417073, "mesênquima é o tecido conjuntivo embrionário: repete 1516246473563, que já liga mesênquima a conjuntivo"),
 (1518403445250, "espessura de Breslow no melanoma: estadiamento de um tumor específico"),
 (1518403598167, "estadiamento clínico ou patológico: alvo vago, sem ganho sobre o TNM"),
]
FORA_DO_RECORTE = []

CARDS = [
 # ---------- Lâminas 1–2: conceitos gerais e nomenclatura ----------
 au("k-tumor-neoplasia-cancer", ORG("Three nested terms:<br><br>- <b>tumor</b>: any {{c1::mass}} that occupies space, neoplastic or not<br>- <b>neoplasia</b>: autonomous {{c1::clonal}} new growth<br>- <b>cancer</b>: a {{c1::malignant}} neoplasm"),
    "V-pilar", A_, "Tumor, neoplasia e câncer", 2, "lâmina 2; objetivo 1; palavras-cruzadas 22; Robbins p.260", motivacao="m1", organizador=True,
    organizacao_fonte="fontes/apostila-patologia-veteranos.txt", organizacao_trecho="Existem três conceitos importantes de serem diferenciados", fontes=F("lâmina 2", "Conceitos Gerais"),
    sem_imagem="definição verbal, sem figura na aula",
    extra="Every neoplasm is a tumor, but not every tumor is a neoplasm (an abscess or edema also swells).<br>Cancer comes from the Latin for crab: it clings to whatever it touches."),
 K(1496110201793, "V-hy", A_, "Neoplasia: três características", 2, "lâmina 2; Robbins p.260 (crescimento autônomo e excessivo)"),
 K(1496110605566, "V-pilar", A_, "Neoplasia monoclonal × hiperplasia policlonal", 2, "Robbins p.260: tumores são clonais; objetivo 9"),
 au("k-parenquima-estroma", "A <b>tumor's name</b> and behavior come from its {{c1::parenchyma}}, the neoplastic cells, not from its reactive stroma",
    "V-pilar", A_, "Parênquima × estroma", 2, "lâmina 2; Robbins p.260", motivacao="m3", fontes=F("lâmina 2", "Parênquima – importância na nomenclatura"),
    sem_imagem="conceito da lâmina 2, sem figura",
    extra="The stroma is connective tissue, vessels and inflammatory cells; the tumor needs it to grow.<br>Abundant collagenous stroma is desmoplasia, which makes some breast cancers stone hard."),
 K(1496110867291, "A-step", A_, "Adenoma × adenocarcinoma", 2, "objetivos 2–3: nomenclatura epitelial glandular"),
 K(1488680226241, "A-step", A_, "Carcinoma escamoso: pérolas de queratina", 2, "prova 2016 P3 2.2 (carcinoma epidermoide com queratina); objetivo 3"),
 K(1496110970215, "A-step", A_, "Papiloma × carcinoma papilar", 2, "objetivos 2–3: epitelial exofítico"),
 au("k-nomenclatura-orgaos", ORG("Malignant <b>epithelial tumors</b> named after the organ:<br><br>- <b>urothelium</b>: {{c1::transitional (urothelial)}} cell carcinoma<br>- <b>liver</b>: {{c1::hepatocellular}} carcinoma<br>- <b>kidney tubules</b>: {{c1::renal cell}} carcinoma<br>- <b>placenta</b>: {{c1::choriocarcinoma}}"),
    "A-aula", A_, "Carcinomas nomeados pelo órgão", 2, "aula 74 lâminas 10–11 (tabela de nomenclatura); Robbins tabela 7-1", motivacao="m5", organizador=True,
    organizacao_fonte="livros/robbins-cap7-neoplasia.txt", organizacao_trecho="Carcinoma de células transicionais Coriocarcinoma",
    fontes=F("aula 74 lâmina 9", "Adicionalmente incluindo organização tecidual"), sem_imagem="a tabela da lâmina é longa demais para o celular",
    extra="Benign counterparts: urothelial papilloma, liver cell adenoma, renal tubular adenoma and hydatidiform mole.<br>Bronchogenic carcinoma and basal cell carcinoma follow the same organ-based logic."),
 K(1517720363511, "V-pilar", A_, "Carcinoma epitelial × sarcoma mesenquimal", 2, "objetivo 2; Robbins p.261"),
 K(1516246515683, "A-step", A_, "Maligno mesenquimal = sarcoma", 2, "objetivo 2; palavras-cruzadas 3"),
 K(1516246473563, "R-detalhe", A_, "Mesênquima dá o conjuntivo", 2, "base da regra do sarcoma"),
 K(1496111000227, "A-step", A_, "Lipoma × lipossarcoma", 2, "objetivo 3; palavras-cruzadas 3"),
 K(1488418620676, "A-step", A_, "Lipoma encapsulado", 2, "objetivo 3; cápsula do benigno (lâmina 17)"),
 K(1517721078779, "A-step", A_, "Leiomioma × leiomiossarcoma", 2, "objetivo 3; palavras-cruzadas 20"),
 K(1488418643668, "R-detalhe", A_, "Rabdomioma", 2, "objetivo 3 (benigno não epitelial)"),
 K(1488418645713, "R-detalhe", A_, "Rabdomiossarcoma", 2, "objetivo 3 (maligno não epitelial)"),
 K(1517721704430, "R-detalhe", A_, "Fibroma × fibrossarcoma", 2, "Robbins tabela 7-1"),
 K(1517721729135, "R-detalhe", A_, "Osteoma × osteossarcoma", 2, "Robbins tabela 7-1"),
 K(1496111041884, "R-detalhe", A_, "Hemangioma × angiossarcoma", 2, "Robbins tabela 7-1"),
 K(1517721745386, "A-step", A_, "Nevo × melanoma", 2, "objetivo 4: melanoma é exceção; palavras-cruzadas 29"),
 K(1496111024111, "A-step", A_, "Linfoma × leucemia", 2, "objetivo 4: linfoma é exceção; palavras-cruzadas 11"),
 au("k-excecoes", ORG("Malignant tumors with a <b>benign-sounding -oma</b> name:<br><br>- of <b>lymphocytes</b>: {{c1::lymphoma}}<br>- of <b>melanocytes</b>: {{c1::melanoma}}<br>- of <b>mesothelium</b>: {{c1::mesothelioma}}<br>- of <b>germ cells</b>: {{c1::seminoma}}"),
    "V-pilar", A_, "Exceções da nomenclatura", 2, "objetivo 4; Robbins p.262; palavras-cruzadas 11 e 29", motivacao="m6", organizador=True,
    organizacao_fonte="fontes/objetivos-75.txt", organizacao_trecho="Citar corretamente 2 exceções à regra geral de nomenclatura dos tumores",
    fontes=F("objetivo 4", "Citar corretamente 2 exceções à regra geral de nomenclatura dos tumores"), sem_imagem="lista de nomes, sem figura",
    extra="The rule says benign = -oma, but these four are malignant by long usage.<br>The opposite also exists: hamartoma and choristoma sound like tumors but are not neoplasms."),
 K(1463187910218, "A-step", A_, "Teratoma: mais de um folheto", 2, "palavras-cruzadas 12; Robbins p.261–262"),
 K(1482191477668, "R-detalhe", A_, "Adenoma pleomórfico: tumor misto de um clone", 2, "Robbins p.261: tumor misto"),
 K(1517720929242, "A-step", A_, "Hamartoma: tecido desorganizado no próprio local", 2, "Robbins p.262"),
 K(1517720994409, "A-step", A_, "Coristoma: tecido normal em local estranho", 2, "Robbins p.262"),
 # ---------- Lâmina 3: os quatro eixos ----------
 au("k-criterios", ORG("Features that separate <b>benign</b> from <b>malignant</b> tumors:<br><br>- <b>cell aspect</b>: {{c1::differentiation}} and anaplasia<br>- <b>speed</b>: rate of {{c1::growth}}<br>- <b>edge</b>: local {{c1::invasion}}<br>- <b>distant spread</b>: {{c1::metastasis}}"),
    "V-pilar", B_, "Os quatro critérios", 3, "lâmina 3; objetivo 10; Robbins p.262", motivacao="m12", organizador=True,
    organizacao_fonte="fontes/objetivos-75.txt", organizacao_trecho="Apontar corretamente três características que podem ser consideradas definidoras de malignidade", fontes=F("lâmina 3", "Metástases à distância"),
    sem_imagem="lista da lâmina 3, sem figura",
    extra="They are also the four parts of tumor biology: transformation, growth, invasion and metastasis.<br>Metastasis is unequivocal; invasion is the next most reliable sign of malignancy."),
 K(1496164634302, "V-hy", B_, "Benigno organizado, maligno desorganizado", 3, "lâmina 4: perda de polaridade"),
 K(1518398337589, "A-step", B_, "Benigno: lento, circunscrito, móvel", 3, "lâmina 17; objetivo 11"),
 K(1518398362472, "A-step", B_, "Maligno: rápido, infiltrativo, fixo", 3, "lâmina 17; objetivo 11"),
 K(1518398388805, "A-step", B_, "Só biópsia ou excisão define benigno × maligno", 3, "prova 2018 1.2: o patologista decide"),
 K(1518402560522, "V-hy", B_, "Invasão da membrana basal no maligno", 3, "lâmina 6; prova 2016 1.4"),
 # ---------- Lâminas 4–6: diferenciação, anaplasia, displasia, carcinoma in situ ----------
 K(1518402922916, "V-hy", C_, "Diferenciação = semelhança com o tecido de origem", 4, "lâmina 4; objetivo 5; palavras-cruzadas 14"),
 K(1518402974215, "V-hy", C_, "Bem × pouco diferenciado", 4, "lâmina 4"),
 K(1518403080746, "V-hy", C_, "Anaplasia: falta completa de diferenciação", 4, "lâmina 4; objetivo 5; palavras-cruzadas 7"),
 K(1496164677268, "V-hy", C_, "Núcleo pleomórfico e hipercromático", 4, "lâmina 4: pleomorfismo e hipercromasia; prova 2018 1.2"),
 K(1496164741405, "V-hy", C_, "Relação núcleo-citoplasma alta", 4, "Robbins p.263 (1:1); provas 2017 1.4 e 2018 1.2"),
 K(1496164875478, "V-hy", C_, "Mitoses atípicas no maligno", 4, "lâmina 4: mitoses atípicas e bizarras; palavras-cruzadas 15"),
 K(1526251874337, "V-hy", C_, "Células gigantes tumorais", 4, "lâmina 4: células gigantes"),
 K(1496165216576, "A-step", C_, "Citoqueratina identifica tumor epitelial", 4, "apostila de veteranos: imuno-histoquímica rastreia a origem quando o tumor é anaplásico"),
 K(1496165337190, "A-step", C_, "Vimentina identifica sarcoma", 4, "apostila de veteranos: imuno-histoquímica"),
 K(1496164062309, "A-step", C_, "Polaridade basal-apical do tecido normal", 4, "lâmina 4: perda de polaridade; palavras-cruzadas 24"),
 au("k-funcao", "The better <b>differentiated</b> a tumor, the more it keeps the specialized {{c1::function}} of its tissue of origin",
    "A-aula", C_, "Diferenciação conserva função", 4, "lâmina 4 (conceito morfológico e funcional); Robbins p.265", motivacao="m23",
    fontes=F("lâmina 4", "Conceito morfológico e funcional"), sem_imagem="conceito funcional, sem figura",
    extra="Examples: endocrine adenomas secrete hormones, squamous carcinomas make keratin, hepatocellular carcinoma makes bile.<br>Endocrine adenomas raise blood hormone levels, used to follow them; hepatocellular carcinoma can make bile.<br>Anaplastic tumors lose these functions or gain unexpected ones (e.g., ectopic hormones)."),
 K(1487461112379, "V-pilar", C_, "Displasia: crescimento desordenado não neoplásico", 5, "lâmina 5; objetivo 6"),
 K(1487461120979, "V-hy", C_, "Displasia só em epitélio", 5, "lâmina 5"),
 K(1487461125395, "V-hy", C_, "Displasia é proliferação pré-cancerosa", 5, "lâmina 5: adjacente à neoplasia invasiva"),
 K(1518217637366, "A-step", C_, "Displasia: perda da orientação", 5, "lâmina 5: perda de orientação arquitetural"),
 K(1518217804217, "A-step", C_, "Displasia: N:C aumentada", 5, "lâmina 5"),
 au("k-displasia-anaplasia", ORG("Two different abnormalities:<br><br>- <b>dysplasia</b>: disordered {{c1::architecture}} of the tissue, not invasive<br>- <b>anaplasia</b>: loss of {{c1::differentiation}} of the cells"),
    "V-pilar", C_, "Displasia × anaplasia", 5, "objetivo 6; prova 2018 1.2 (celular × tecidual)", motivacao="m18", organizador=True,
    organizacao_fonte="fontes/provas-pt75.txt", organizacao_trecho="alterações celulares (anaplasia) ou teciduais (displasia)",
    fontes=F("prova 2018 P4 1.2", "alterações celulares (anaplasia) ou teciduais (displasia)"), sem_imagem="contraste conceitual; a figura da lâmina 6 está nos cards do in situ",
    extra="The pathologist looks for both: anaplasia in each cell, dysplasia in how cells are arranged.<br>Dysplastic cells can be anaplastic, but dysplasia names the tissue pattern and may still regress."),
 au("k-sequencia-cis", ORG("Progression of a <b>stratified epithelium</b> toward cancer:<br><br>- <b>more cells, normal order</b>: {{c1::hyperplasia}}<br>- <b>dysplasia</b>: atypia in part of the thickness<br>- <b>carcinoma in situ</b>: atypia in the {{c1::full thickness}}<br>- <b>invasive cancer</b>: breach of the {{c1::basement membrane}}"),
    "V-pilar", C_, "Sequência até o carcinoma invasor", 6, "lâmina 6 (normal → hiperplasia → displasia → in situ → invasor); prova 2016 P3 1.1 e 1.4", motivacao="m20", organizador=True,
    organizacao_fonte="fontes/slides.txt", organizacao_trecho="Adjacente a áreas de neoplasia invasiva",
    fontes=F("lâmina 6", "Transformação – Carcinoma in situ"),
    extra="Mild and moderate dysplasia can regress if the cause is removed; carcinoma in situ does not regress.<br>Only crossing the basement membrane makes it invasive and able to metastasize." + IMG("cis")),
 K(1518218866119, "V-hy", C_, "In situ ocupa toda a espessura", 6, "lâmina 6; palavras-cruzadas 4"),
 K(1518219030992, "V-hy", C_, "In situ não rompe a membrana basal", 6, "lâmina 6; prova 2016 1.4"),
 K(1518219389272, "V-hy", C_, "In situ não é reversível", 6, "lâmina 6: displasia severa"),
 # ---------- Lâminas 7–11: teorias, expansão clonal, progressão, hallmarks ----------
 au("k-teorias", ORG("Two theories of how cancer develops:<br><br>- <b>somatic mutation</b>: a {{c1::genetic}} change reprograms the cell<br>- <b>tissue organization field</b>: disturbed interaction with the {{c1::microenvironment}}"),
    "A-aula", D_, "Mutação somática × campo de organização", 7, "lâmina 7", motivacao="m24", organizador=True,
    organizacao_fonte="fontes/slides.txt", organizacao_trecho="Teoria do campo de organização tecidual", fontes=F("lâmina 7", "Teoria do campo de organização tecidual"),
    sem_imagem="lâmina 7 é texto",
    extra="The mutation theory explains why tumors are clonal and heritable; the field theory explains why stroma and inflammation matter.<br>The hallmarks model joins both: genetic changes plus a supportive microenvironment."),
 au("k-metilacao", "Besides mutation, <b>cancer genes</b> can be silenced without changing the DNA sequence, by promoter {{c1::methylation}}",
    "A-aula", D_, "Metilação: alteração epigenética", 8, "palavras-cruzadas 9 (efeito ambiental sobre o DNA: metilação); lâmina 16 (eventos fenotípicos e genéticos)", motivacao="m27",
    fontes=F("palavras-cruzadas 9", "Efeito ambiental sobre o DNA que tambem atua no processo de carcinogenese"), sem_imagem="conceito da cruzadinha, sem figura",
    extra="Hypermethylation of a tumor suppressor promoter turns the gene off as effectively as a mutation.<br>It is an epigenetic change: heritable by daughter cells, but potentially reversible."),
 K(1496158482771, "A-step", D_, "Mutações rompem a regulação: promoção e progressão", 8, "lâminas 8–10: iniciação → progressão"),
 au("k-celula-tronco", "<b>Tumors</b> keep growing because a small population of {{c1::cancer stem cells}} renews itself and feeds the rest of the tumor",
    "A-aula", D_, "Células-tronco tumorais", 4, "lâmina 4 (diferenciação a partir da stem cell tumoral); Robbins p.263 e 267", motivacao="m21",
    fontes=F("lâmina 4", "Diferenciação a partir da “stem cell” tumoral"), sem_imagem="conceito da lâmina 4, sem figura",
    extra="Their daughters differentiate (well-differentiated tumors) or not (anaplastic tumors).<br>They divide slowly and pump out drugs (MDR1), so therapy that spares them lets the tumor regrow."),
 au("k-progressao", "An <b>initiated cell</b> multiplies by {{c1::clonal expansion}}, and new mutations then create {{c2::subclones}}, making the tumor heterogeneous",
    "V-pilar", D_, "Progressão: subclones e heterogeneidade", 9, "lâminas 8–10; objetivo 9; palavras-cruzadas 8", motivacao="m26",
    fontes=F("lâmina 8", "acúmulo de novos eventos mutacionais"),
    extra="Some variants die, others need fewer growth factors, escape immunity, invade or metastasize.<br>Genomic instability speeds this up; it is why one tumor has cells with different behavior." + IMG("clonal")),
 au("k-hallmarks", ORG("<b>Hallmarks of cancer</b> (Hanahan & Weinberg):<br><br>- <b>sustained</b> {{c1::proliferative signaling}}<br>- <b>evading</b> growth suppressors<br>- <b>resisting</b> {{c1::cell death}}<br>- <b>replicative</b> {{c1::immortality}}<br>- <b>inducing</b> {{c1::angiogenesis}}<br>- <b>activating</b> invasion and metastasis"),
    "A-aula", D_, "Hallmarks do câncer", 11, "lâmina 11; Hanahan & Weinberg 2011", motivacao="m30", organizador=True,
    organizacao_fonte="livros/bibliografia-II.txt", organizacao_trecho="sustaining proliferative signaling, evading growth suppressors",
    fontes=F("Hanahan & Weinberg 2011", "sustaining proliferative signaling, evading growth suppressors"),
    extra="Enabling characteristics: genomic instability and tumor-promoting inflammation.<br>Emerging: reprogrammed energy metabolism and evasion of immune destruction." + IMG("hallmarks")),
 au("k-heterogeneidade-terapia", "Because subclones differ, a <b>metastasis</b> may carry mutations absent from the primary, so a {{c1::targeted}} drug works only partly",
    "A-aula", D_, "Heterogeneidade e resistência à terapia-alvo", 10, "lâminas 9–10 (árvore de mutações por sítio); prova 2025 P4 2.6", motivacao="m28",
    fontes=F("lâmina 8", "acúmulo de novos eventos mutacionais"),
    extra="A tumor mutation tree shows mutations shared by all sites, others only in the primary or only in metastases.<br>A drug aimed at one mutation spares subclones that lack it, and they regrow." + IMG("arvore")),
 K(1467771904154, "A-step", D_, "Telomerase adiciona TTAGGG", 11, "prova 2016 P3 2.5: telomerase alonga telômeros e evita a senescência"),
 K(1496163284718, "A-step", D_, "Hallmark: autossuficiência em sinais de crescimento", 11, "prova 2017 P4 4.1: um elemento por marca"),
 K(1518212434121, "A-step", D_, "Hallmark: insensibilidade a sinais inibitórios (TGF-β)", 11, "prova 2017 P4 4.1"),
 K(1496164030007, "A-step", D_, "Hallmark: potencial replicativo ilimitado", 11, "prova 2017 P4 4.1"),
 K(1496163026982, "A-step", D_, "Telomerase evita encurtamento", 11, "prova 2017 P4 4.1: imortalidade replicativa"),
 K(1496163125083, "A-step", D_, "Hallmark: angiogênese (VEGF/FGF)", 11, "prova 2017 P4 4.1"),
 K(1518214216086, "A-step", D_, "Hallmark: efeito Warburg", 11, "prova 2017 P4 4.1: metabolismo"),
 K(1496163225363, "A-step", D_, "Hallmark: escape imune (MHC I)", 11, "prova 2017 P4 4.1: evasão imune"),
 # ---------- Lâminas 12–15: ritmo e fração de crescimento ----------
 au("k-prolif-remocao", "A tumor grows only while cell <b>proliferation</b> {{c1::exceeds}} cell loss by death, shedding or differentiation",
    "V-pilar", E_, "Proliferação × remoção", 12, "lâmina 12", motivacao="m31", fontes=F("lâmina 12", "Proliferação > remoção"),
    extra="More cycling or less apoptosis enlarges it; balance keeps it stable; more loss shrinks it.<br>Fast-growing tumors often have both high proliferation and high apoptosis." + IMG("prolif")),
 au("k-30-duplicacoes", "One <b>transformed cell</b> needs about {{c1::30}} doublings to reach 10<sup>9</sup> cells, weighing {{c2::1 g}}, the smallest detectable mass",
    "V-pilar", E_, "10⁹ células = 1 g", 13, "lâmina 13; Robbins p.265", motivacao="m32", fontes=F("lâmina 13", "30 divisões"),
    extra="Only 10 more doublings reach 10<sup>12</sup> cells (1 kg), about the maximum compatible with life.<br>So a detectable tumor has already lived most of its life." + IMG("divisoes")),
 au("k-tres-fatores", ORG("The <b>growth rate</b> of a tumor depends on:<br><br>- <b>speed</b> of each division: {{c1::doubling time}}<br>- <b>proportion dividing</b>: {{c1::growth fraction}}<br>- <b>removal</b>: rate of cell {{c1::loss}}"),
    "V-pilar", E_, "Três fatores do ritmo", 14, "lâmina 14; objetivo 7; Robbins p.266", motivacao="m33", organizador=True,
    organizacao_fonte="fontes/slides.txt", organizacao_trecho="Percentual de células em proliferação – fração de crescimento", fontes=F("lâmina 14", "Tempo de duplicação"),
    sem_imagem="lista da lâmina 14",
    extra="Tumor cells do not cycle faster than normal cells; the excess comes from more cells entering the cycle and fewer dying.<br>In general malignant tumors grow faster than benign ones, but there are many exceptions (hormones, blood supply, aggressive subclones)."),
 au("k-fracao", "The proportion of <b>tumor cells</b> in the replicative pool is the {{c1::growth fraction}}, at most about 20% in a clinical tumor",
    "V-pilar", E_, "Fração de crescimento", 15, "lâmina 15; objetivo 8; Robbins p.266", motivacao="m34", fontes=F("lâmina 15", "Fração de Crescimento"),
    sem_imagem="lâmina 15 é texto",
    extra="Early, almost all transformed cells divide; as the mass grows, cells leave to G0, differentiate, starve or die.<br>Leukemias, lymphomas and small cell lung cancer keep a high fraction."),
 au("k-fc-quimio", "Tumors with a low <b>growth fraction</b> resist chemotherapy, so surgery or radiation first pushes G0 cells back into the {{c1::cell cycle}}",
    "V-pilar", E_, "Fração de crescimento e quimioterapia", 15, "lâmina 15; objetivo 8; Robbins p.266", motivacao="m35",
    fontes=F("lâmina 15", "Base da quimioterapia neoadjuvante"), sem_imagem="consequência terapêutica, sem figura",
    extra="Most anticancer drugs kill only cycling cells; colon and breast cancers have low fractions.<br>Debulking recruits survivors into the cycle, the basis of combined (neoadjuvant/adjuvant) therapy."),
 # ---------- Lâmina 16: bases moleculares ----------
 au("k-dano-nao-letal", "At the heart of <b>carcinogenesis</b> is {{c1::nonlethal}} genetic damage, passed on to the cell's progeny",
    "V-pilar", F_, "Dano genético não letal", 16, "lâmina 16; Robbins p.271; palavras-cruzadas 17", motivacao="m37",
    fontes=F("lâmina 16", "Alteração genética não letal"), sem_imagem="princípio da lâmina 16",
    extra="Lethal damage kills the cell and ends there; only damage the cell survives can expand clonally.<br>It may be acquired (chemicals, radiation, viruses) or inherited."),
 au("k-quatro-classes", ORG("Four classes of <b>regulatory genes</b> targeted in cancer:<br><br>- <b>growth drivers</b>: {{c1::proto-oncogenes}}<br>- <b>brakes</b>: {{c1::tumor suppressor}} genes<br>- <b>cell death</b>: genes that regulate {{c1::apoptosis}}<br>- <b>genome guardians</b>: {{c1::DNA repair}} genes"),
    "V-pilar", F_, "Quatro classes de genes", 16, "lâmina 16; objetivo 14; Robbins p.271", motivacao="m39", organizador=True,
    organizacao_fonte="fontes/slides.txt", organizacao_trecho="Alteração de genes regulatórios – Proto-oncogenes – Genes supressores de tumor", fontes=F("lâmina 16", "Proto-oncogenes"),
    sem_imagem="lista da lâmina 16",
    extra="Failed DNA repair adds mutations in the other three classes (genomic instability).<br>Lesson 76 details oncogenes and suppressors."),
 K(1517957674940, "A-step", F_, "Ganho de função: proto-oncogene → oncogene", 16, "lâmina 16: proto-oncogenes"),
 K(1517957746836, "A-step", F_, "Perda de função do supressor", 16, "lâmina 16: supressores"),
 # ---------- Lâmina 17: invasão local ----------
 au("k-capsula", "A <b>benign tumor</b> grows by expansion and is often surrounded by a fibrous {{c1::capsule}} from compressed host tissue",
    "V-pilar", G_, "Cápsula do benigno", 17, "lâmina 17; objetivo 11; Robbins p.268; palavras-cruzadas 16", motivacao="m40", fontes=F("lâmina 17", "Cápsula"),
    sem_imagem="lâmina 17 é texto",
    extra="The capsule comes from extracellular matrix of atrophied normal cells; it keeps the mass discrete, mobile and enucleable.<br>Hemangiomas are an exception: benign but unencapsulated."),
 au("k-invasao", "Apart from metastasis, the most reliable sign that a tumor is <b>malignant</b> is local {{c1::invasion}} without a cleavage plane",
    "V-pilar", G_, "Invasão: critério de malignidade", 17, "lâmina 17; objetivo 10; Robbins p.268; palavras-cruzadas 5", motivacao="m41",
    fontes=F("lâmina 17", "Critério de malignidade"), sem_imagem="lâmina 17 é texto",
    extra="Cancers infiltrate and destroy surrounding tissue, so resection needs a wide margin and may be impossible.<br>Even pseudo-encapsulated cancers send cords of cells through the edge."),
 K(1518219637289, "A-step", G_, "Perda de E-caderina", 17, "prova 2016 1.5; prova 2015 P3 2.4 (CD44)", extra_add="CD44 and other adhesion molecules also change, so cells detach, migrate and reach lymphatics (exam 2015)."),
 K(1518219881077, "R-detalhe", G_, "Ligação à membrana basal via laminina", 17, "prova 2016 1.5"),
 K(1518219442201, "A-step", G_, "Metaloproteinases rompem a membrana basal", 17, "prova 2016 1.5"),
 K(1518219949937, "R-detalhe", G_, "Fibronectina na disseminação local", 17, "prova 2016 1.5"),
 K(1518220197497, "A-step", G_, "Invadir linfático ou vaso torna metastático", 17, "lâmina 19; Robbins p.269"),
 # ---------- Lâmina 18: ciclo celular (exemplo RB) ----------
 K(1496162192905, "A-step", H_, "Ciclinas-CDK hiperfosforilam RB", 18, "lâmina 18: fosforilação de RB"),
 K(1496162245188, "A-step", H_, "RB fosforilado libera E2F: fase S", 18, "lâmina 18"),
 au("k-checkpoints", ORG("Cell cycle <b>checkpoints</b> and what each one checks:<br><br>- <b>before DNA synthesis</b>: {{c1::DNA damage}}, then repair or apoptosis<br>- <b>before mitosis</b>: whether DNA is fully {{c1::replicated}}"),
    "A-aula", H_, "Checkpoints G1/S e G2/M", 18, "lâmina 18", motivacao="m44", organizador=True,
    organizacao_fonte="fontes/slides.txt", organizacao_trecho="Fundamentais no controle dos check-points", fontes=F("lâmina 18", "G2/M"),
    extra="They are named the G1/S and G2/M checkpoints; p53 and RB guard the checkpoint before DNA synthesis; cancer cells that lose them divide with damaged DNA.<br>That feeds genomic instability and progression." + IMG("ciclo")),
 K(1496161616847, "A-step", H_, "G1 regulado por p53 e RB", 18, "lâmina 18: G1/S"),
 # ---------- Lâmina 19: metástases ----------
 au("k-metastase-def", "A <b>metastasis</b> is a tumor implant {{c1::discontinuous}} with the primary, unlike invasion of a neighboring organ by contiguity",
    "V-pilar", I_, "Metástase × contiguidade", 19, "lâmina 19; objetivo 12; Robbins p.269", motivacao="m45", fontes=F("lâmina 19", "Implantes descontínuos"),
    sem_imagem="lâmina 19 é texto",
    extra="Metastasis marks a tumor as malignant without doubt; about 30% of solid tumors already have it at diagnosis."),
 au("k-preditores", ORG("Features of the primary tumor that predict <b>metastasis</b>:<br><br>- <b>behavior</b>: {{c1::aggressiveness}}<br>- <b>speed</b>: rate of {{c1::growth}}<br>- <b>mass</b>: {{c1::size}}"),
    "A-aula", I_, "Preditores de metástase", 19, "lâmina 19; Robbins p.269", motivacao="m46", organizador=True,
    organizacao_fonte="fontes/slides.txt", organizacao_trecho="Malignos – relação com a velocidade de crescimento", fontes=F("lâmina 19", "Agressividade"),
    sem_imagem="lista da lâmina 19",
    extra="There are exceptions: small slow tumors may metastasize widely, and some large ones stay local for years."),
 au("k-vias-org", ORG("Three routes of <b>metastatic spread</b>:<br><br>- <b>carcinomas</b>, mostly: {{c1::lymphatic}}<br>- <b>sarcomas</b>, mostly: {{c1::hematogenous}}<br>- <b>ovarian carcinoma</b>, classically: seeding of body {{c1::cavities}}"),
    "V-pilar", I_, "Três vias de disseminação", 19, "lâmina 19; objetivo 13; palavras-cruzadas 28 e 31", motivacao="m48", organizador=True,
    organizacao_fonte="fontes/objetivos-75.txt", organizacao_trecho="Apontar corretamente 3 vias de disseminação metastática no organismo",
    fontes=F("lâmina 19", "Vias de disseminação"), sem_imagem="lista da lâmina 19",
    extra="Lymph first reaches the sentinel node; blood goes to the liver (portal) and lungs (caval).<br>The peritoneum is the cavity most often seeded, classically by ovarian carcinoma."),
 K(1496164110071, "V-hy", I_, "Carcinoma linfático, sarcoma hematogênico", 19, "lâmina 19; objetivo 13; palavras-cruzadas 28 e 31"),
 K(1518241346893, "A-step", I_, "Primeiro, linfonodos regionais", 19, "Robbins p.269–270; palavras-cruzadas 27", fields_override={"Text": "The initial <b>lymphatic spread</b> of a carcinoma is to {{c1::regional}} draining lymph nodes"}),
 au("k-sentinela", "The first <b>lymph node</b> in a basin to receive lymph from the <b>primary tumor</b> is the {{c1::sentinel}} node",
    "A-aula", I_, "Linfonodo sentinela", 19, "Robbins p.270; palavras-cruzadas 2", motivacao="m50",
    fontes=F("palavras-cruzadas 2", "primeiro linfonodo de drenagem") + F("Robbins p.270", "linfonodos sentinelas"), sem_imagem="definição, sem figura",
    extra="Its biopsy (mapped with dye or radiotracer) spares a full axillary dissection in breast cancer and melanoma."),
 K(1518226984913, "V-hy", I_, "Depois dos linfonodos: fígado e pulmão", 19, "Robbins p.270; palavras-cruzadas 6"),
 K(1486591340394, "A-step", I_, "Metástase hepática é mais comum que o primário", 19, "via hematogênica pela porta", fields_override={"Text": 'Most malignant tumors found in the <b>liver</b> are {{c1::metastases}}, not primary liver tumors'}),
 K(1518241882006, "A-step", I_, "Peritônio é a cavidade mais semeada", 19, "lâmina 19: via direta para cavidades"),
 K(1508802208485, "V-hy", I_, "Carcinomatose peritoneal no ovário", 19, "Robbins p.269"),
 K(1518220389435, "R-detalhe", I_, "Semente e solo: a semente é o êmbolo", 19, "Robbins p.270: distribuição das metástases"),
 K(1518220409981, "R-detalhe", I_, "Semente e solo: o solo é o primeiro leito capilar", 19, "Robbins p.270"),
 K(1488680222795, "A-step", I_, "Carcinoma basocelular raramente metastatiza", 19, "Robbins p.269: exceção"),
 K(1481944701192, "A-step", I_, "Tumores primários do SNC não metastatizam", 19, "Robbins p.269: gliomas"),
 K(1518403099278, "V-hy", I_, "Grau: diferenciação e mitoses", 19, "lâmina 19 (agressividade); Robbins graduação"),
 K(1518403188199, "V-hy", I_, "Baixo grau = bem diferenciado", 19, "lâmina 4"),
 K(1518403203594, "V-hy", I_, "Alto grau = pouco diferenciado", 19, "lâmina 4"),
 K(1518403144606, "V-hy", I_, "Estádio: extensão e disseminação", 19, "lâmina 19 (tamanho); prova 2017 1.9"),
 K(1518403259951, "V-hy", I_, "TNM", 19, "prova 2017 1.9", fields_override={"Text": 'Tumor <b>stage</b> uses the TNM system: T = tumor {{c1::size}}, N = lymph {{c1::node}} involvement, M = distant {{c1::metastases}}'}),
 K(1518403222894, "V-hy", I_, "Estádio prevê mais que grau", 19, "prova 2017 1.9", fields_override={"Text": 'Tumor {{c1::stage}} has more <b>prognostic value</b> than tumor <u>grade</u>'}),
 K(1496166103071, "V-hy", I_, "M é o fator prognóstico mais importante", 19, "lâmina 19"),
 K(1496166062248, "V-hy", I_, "N é o segundo fator prognóstico", 19, "lâmina 19", fields_override={"Text": 'Spread to regional {{c1::lymph nodes}} (N) is the second most important prognostic factor for a cancer'}),
 K(1496165964076, "A-step", I_, "Estadiamento após a ressecção", 19, "prova 2019 2.11 (estadiamento cirúrgico)"),
 # ---------- Lâmina 20: condições predisponentes ----------
 sh(1792240574547, "azul", J_, "Metaplasia é reversível", 20, "F-20261110-CLAUDE-03: suspenso em outra aula, vem dessuspenso para Davi reavaliar", reavaliar=True),
 K(1520440331083, "V-pilar", J_, "Displasia vem de metaplasia ou hiperplasia persistente", 20, "lâmina 20: solo fértil; palavras-cruzadas 19"),
 K(1487461083189, "V-hy", J_, "Metaplasia → displasia → câncer", 20, "lâmina 20"),
 au("k-inflamacao-cronica", "<b>Chronic inflammation</b> favors cancer by forcing progenitor cells to divide while {{c1::oxidative stress}} damages their DNA",
    "V-pilar", J_, "Inflamação crônica predispõe", 20, "lâmina 20; prova 2025 P4 3.3", motivacao="m55",
    fontes=F("lâmina 20", "Instabilidade gênica"), sem_imagem="lâmina 20 é texto",
    extra="Examples: chronic hepatitis with cirrhosis, ulcerative colitis, Barrett esophagus.<br>Each regenerative division is another chance for a replication error to stick."),
 K(1488680264064, "A-step", J_, "Queratose actínica precede carcinoma escamoso", 20, "Robbins p.271: condição pré-cancerosa"),
 K(1482191378467, "A-step", J_, "Leucoplasia e eritroplasia orais", 20, "Robbins p.271: leucoplasias"),
 # ---------- Aula 74 (Epidemiologia dos tumores), absorvida nesta aula a pedido de Davi (F-20261111-CLAUDE-01) ----------
 au("k-epi-fatores", ORG("Factors in the <b>epidemiology of cancer</b>:<br><br>- <b>place</b>: {{c1::geographic and environmental}} factors<br>- <b>time</b>: {{c1::age}}<br>- <b>family</b>: genetic {{c1::predisposition}}"),
    "V-pilar", K_, "Fatores epidemiológicos do câncer", 20, "aula 74 lâmina 7; cruzadas da aula 74 (2: fatores ambientais dominantes)", motivacao="m57", organizador=True,
    organizacao_fonte="fontes/aula74-slides.txt", organizacao_trecho="Fatores geográficos e ambientais • Idade • Predisposição genética",
    fontes=F("aula 74 lâmina 7", "Fatores geográficos e ambientais"), sem_imagem="lista da lâmina 7 da aula 74",
    extra="Migrants take on the cancer rates of their new country within a generation: environment outweighs heredity in most cancers.<br>Smoking, alcohol, diet, infections (H. pylori, HPV, hepatitis) and pollution are the main environmental factors."),
 au("k-epi-idade", "Cancer incidence rises with <b>age</b> because somatic mutations {{c1::accumulate}} in dividing cells over a lifetime",
    "A-aula", K_, "Idade e acúmulo de mutações", 20, "aula 74 lâmina 7 (idade); cruzadas da aula 74 (3: envelhecimento; 6: mutações que acumulam ao longo da vida)", motivacao="m58",
    fontes=F("cruzadas da aula 74", "Principais mutacoes que acumulam ao longo"), sem_imagem="conceito, sem figura",
    extra="Most cancers appear after 55; population aging explains much of the rise in cancer cases worldwide.<br>Childhood cancers (leukemias, CNS tumors, sarcomas) are the exception."),
 au("k-epi-diag-precoce", "<b>Breast cancer</b> is the most incident cancer in women but not the most lethal, largely thanks to {{c1::early diagnosis}} by screening",
    "A-aula", K_, "Diagnóstico precoce: incidência × mortalidade", 20, "aula 74 lâminas 2–6 (Siegel 2019); cruzadas da aula 74 (11 e 15)", motivacao="m59",
    fontes=F("cruzadas da aula 74", "Neoplasia de maior incidencia em mulheres"), sem_imagem="a tabela de Siegel 2019 é densa demais para o celular",
    extra="Cervical cancer fell with the Pap smear and will fall further with the anti-HPV vaccine.<br>Overall cancer mortality has fallen since about 1990 (less smoking, screening, better treatment): millions of deaths averted.<br>A detectable tumor has already lived most of its life (30 doublings), so screening aims to catch it earlier."),
 au("k-epi-ranking", ORG("Cancer <b>ranking</b> (United States, 2019):<br><br>- most incident in <b>men</b>: {{c1::prostate}}<br>- most incident in <b>women</b>: {{c1::breast}}<br>- most <b>deaths</b> in both sexes: {{c1::lung}}"),
    "V-pilar", K_, "Maiores incidência e mortalidade", 20, "aula 74 lâmina 2 (Siegel 2019); cruzadas da aula 74 (10, 11 e 15)", motivacao="m60", organizador=True,
    organizacao_fonte="fontes/aula74-cruzadas-gabarito.txt", organizacao_trecho="Neoplasia de maior incidencia em mulheres",
    fontes=F("cruzadas da aula 74", "Neoplasia de maior incidencia em mulheres"), sem_imagem="a tabela de Siegel 2019 é densa demais para o celular",
    extra="Colorectal cancer is third in both incidence and deaths.<br>Lung leads in deaths because it is usually found late; breast and prostate are often caught early by screening."),
 K(1496111214453, "A-step", K_, "Câncer é a 2ª causa de morte", 20, "aula 74 lâminas 2–6"),
 K(1517723202896, "A-step", K_, "Pulmão: 2º em incidência, 1º em mortalidade", 20, "aula 74 lâminas 2–3; cruzadas 10"),
 K(1508543664801, "A-step", K_, "Colorretal é o 3º", 20, "aula 74 lâmina 2"),
 K(1517722304153, "R-detalhe", K_, "Pele é o câncer mais comum", 20, "aula 74 lâmina 2 (melanoma na tabela)"),
 K(1517723603774, "A-step", K_, "Dois objetivos do rastreamento", 20, "cruzadas da aula 74 (4: rastreamento); queda da mortalidade (lâmina 6)"),
 K(1496111443409, "A-step", K_, "Papanicolau detecta a displasia antes do carcinoma", 20, "cruzadas da aula 74 (4: Papanicolau); prova 2017 P4 2.4"),
 K(1496111515047, "A-step", K_, "Mamografia detecta o in situ", 20, "cruzadas da aula 74 (11: diagnóstico precoce)"),
 K(1496111589277, "A-step", K_, "Colonoscopia detecta adenoma", 20, "aula 74: rastreamento"),
 K(1463443071372, "A-step", K_, "BRCA1 e BRCA2 no câncer de mama hereditário", 20, "aula 74 lâmina 7 (predisposição genética); cruzadas 1"),
 K(1482203956292, "A-step", K_, "Adenocarcinoma de esôfago vem do Barrett", 20, "cruzadas da aula 74 (7: esôfago de Barrett)"),
 K(1510261296535, "A-step", K_, "H. pylori: adenocarcinoma gástrico e MALT", 20, "cruzadas da aula 74 (12: estômago e H. pylori)"),
 K(1482203975258, "A-step", K_, "Álcool e fumo: carcinoma escamoso do esôfago", 20, "cruzadas da aula 74 (5 e 13: álcool, tabagismo)"),
]


from nebli.spec_lib import _call as _cl
def _limpa(nid):
    t = _cl("notesInfo", notes=[nid])[0]["fields"]["Text"]["value"]
    return _re.sub(r"\{\{c(\d+)::(.*?)\}\}", lambda m: "{{c" + m.group(1) + "::" + _re.sub(r"</?(b|u|i|strong|em)>", "", m.group(2)) + "}}", t)
for _c in CARDS:
    if _c["kind"] == "text" and "fields_override" not in _c:
        _c["fields_override"] = {"Text": _limpa(_c["src"])}
    if _c["kind"] == "text":
        _n = _cl("notesInfo", notes=[_c["src"]])[0]["fields"]
        _ov = _c.setdefault("fields_override", {})
        for _f in ("Text", "Extra"):
            _v = _ov.get(_f, _n.get(_f, {}).get("value", ""))
            if "<img" in _v:
                _v = _re.compile(r"(?:\s*<br\s*/?>\s*)*(?:<(?:em|span|i|div)[^>]*>\s*)*(?:Photo\s*cr(?:<[^>]*>)*edit|Image\s*cr(?:<[^>]*>)*edit|Image licensed)[\s\S]*?(?=<img|\Z)", _re.I).sub("", _v)
                _v = _re.sub(r'<span[^>]*>\s*<em>\s*Photo credit:.*?</em>\s*</span>', "", _v, flags=_re.S)
                _v = _re.sub(r'<i>\s*<span[^>]*>\s*Photo credit:.*?</span>\s*</i>', "", _v, flags=_re.S)
                _v = _re.sub(r'<span[^>]*>(?:(?!</span>).)*?Photo credit:.*?</span>', "", _v, flags=_re.S)
                _C1 = _re.compile(r"(?:\s*<br\s*/?>\s*)*(?:<(?:em|span|i|div)[^>]*>\s*)*(?:Photo\s*cr(?:<[^>]*>)*edit|Image\s*cr(?:<[^>]*>)*edit|Image licensed|Image\(s\) licensed|Image\(s\) provided)[\s\S]*?(?=<img|\Z)", _re.I)
                _C2 = _re.compile(r"(?:\s*<br\s*/?>\s*)*<(em|i|span)\b[^>]*>(?:(?!</\1>)[\s\S])*?(?:Wikimedia Commons|Public domain|CC BY)(?:(?!</\1>)[\s\S])*?</\1>", _re.I)
                _v = _C2.sub("", _C1.sub("", _v))
                _v = _re.sub(r'[^<>]*(?:<a[^>]*>[^<]*</a>,?\s*)+<a[^>]*creativecommons[^>]*>[^<]*</a>,?\s*via[^<]*', "", _v)
                _v = _re.sub(r'\swidth="\d+"', "", _v)
                _ov[_f] = _re.sub(r"<img(?![^>]*style=)", '<img style="width:100%;max-width:850px;height:auto"', _v)
    if _c["kind"] == "text" and not _c.get("sem_imagem"):
        _c["sem_imagem"] = "fato verbal do AnKing; a figura da lâmina está no autoral do mesmo bloco"

for _c in CARDS:
    if _c["kind"] == "autoral" and "pt75-" in _c.get("extra", ""):
        _c["slide_sem_alternativa"] = "figura da própria aula (esquema do professor/Robbins na lâmina); nenhum AnKing traz este esquema"
finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1496111214453": "- Cardiovascular disease is first; cancer deaths have been falling since the 1990s",
 "ak1508543664801": "- Colonoscopy screening removes adenomas before they turn malignant",
 "ak1517722304153": "- Most are basal cell and squamous cell carcinomas, which rarely kill",
 "ak1517723202896": "- Lung cancer is usually found late, so incidence translates into deaths",
 "ak1463443071372": "- Inherited mutation of one allele: the second hit is acquired (tumor suppressor genes)",
 "ak1517723603774": "- Catching dysplasia (Pap smear, colonoscopy) or early carcinoma is why mortality falls",
 "ak1496111443409": "- Cervical dysplasia found early is removed before it becomes invasive",
 "ak1496111515047": "- Mammography finds carcinoma in situ and small invasive tumors",
 "ak1496111589277": "- Removing the adenoma prevents the adenoma–carcinoma sequence",
 "ak1482203956292": "- Barrett is intestinal metaplasia from reflux: metaplasia → dysplasia → adenocarcinoma",
 "ak1510261296535": "- Chronic gastritis is the inflammatory soil for both",
 "ak1482203975258": "- Both act on the squamous epithelium of the upper and middle esophagus",
 "ak1516246515683": "- Sarcoma comes from Greek 'fleshy': little stroma, so the tumor is soft",
 "ak1517721078779": "- Benign -oma, malignant -sarcoma: the cell of origin names both",
 "ak1488418643668": "- Its malignant counterpart is rhabdomyosarcoma",
 "ak1517721704430": "- Same rule: tissue + -oma (benign) or + -sarcoma (malignant)",
 "ak1517721729135": "- Osteosarcoma is the classic malignant primary bone tumor",
 "ak1517721745386": "- Melanoma is malignant despite the -oma: an exception to the naming rule",
 "ak1518402560522": "- Basement membrane invasion is the defining criterion of malignancy in epithelial tumors",
 "ak1496164741405": "- Anaplastic nuclei can reach 1:1 (normal 1:4 to 1:6)",
 "ak1496164875478": "- Mitoses alone are not malignant (bone marrow, hyperplasia); atypical, multipolar ones are",
 "ak1526251874337": "- Unlike Langhans or foreign-body giant cells, tumor giant cells have huge pleomorphic nuclei",
 "ak1496164062309": "- Anaplastic cells lose this polarity and grow in disorganized sheets",
 "ak1518217637366": "- Dysplasia describes the tissue: loss of uniformity and architectural orientation",
 "ak1518213589178": "- Grade rises with how much of the epithelial thickness the atypical cells occupy",
 "ak1518214486672": "- Mild dysplasia: atypia limited to the lower third; may regress",
 "ak1518215368712": "- Moderate dysplasia: atypia up to two thirds of the thickness",
 "ak1518218707562": "- Full thickness with intact basement membrane = carcinoma in situ",
 "ak1518219030992": "- Breaching the basement membrane makes it invasive carcinoma",
 "ak1496158482771": "- Initiation (mutation) → promotion (proliferation) → progression (new mutations, subclones)",
 "ak1518220389435": "- The 'soil' is the first capillary bed or a favorable organ (liver, lung, bone)",
 "ak1496166103071": "- Lymph node spread (N) is the second most important prognostic factor",
 "ak1520440331083": "- Persistent stress turns adaptation into a fertile ground for neoplasia",
}
for c in CARDS:
    if c["key"] in VERSO and c.get("fields_override", {}).get("Extra") is not None:
        c["fields_override"]["Extra"] = VERSO[c["key"]] + "<br>" + c["fields_override"]["Extra"]
        continue
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
for c in CARDS:
    if c.get("extra_add") and c.get("fields_override", {}).get("Extra") is not None and c["extra_add"] not in c["fields_override"]["Extra"]:
        c["fields_override"]["Extra"] = c["fields_override"]["Extra"] + "<br>" + c["extra_add"]
DUPLICACAO = {"k-vias-org": "ganho: reúne as três vias do objetivo 13; ak1496164110071 só contrasta carcinoma × sarcoma", "ak1518403222894": "ganho: compara estádio com grau no prognóstico; 1518403144606 define o que é estádio (mesma palavra, perguntas diferentes)", "ak1518219389272": "ganho: este cobra a irreversibilidade do in situ; 1518219030992 cobra a membrana basal íntegra (ambos respondem Não, perguntas diferentes)", "ak1481944701192": "ganho: exceção de metástase (tumores do SNC), pergunta diferente das do in situ apesar do Não", "ak1520440331083": "ganho: este cobra o que precede a displasia (metaplasia/hiperplasia); 1487461112379 a define", "k-tumor-neoplasia-cancer": "ganho: encaixa os três termos; 'malignant' em outros cards responde outra pergunta",
 "k-excecoes": "ganho: reúne as exceções que os AnKing dão uma a uma", "k-criterios": "ganho: os quatro eixos juntos, que nenhum card reúne",
 "k-prolif-remocao": "ganho: o balanço como princípio; 'loss' em k-tres-fatores é um fator entre três", "k-tres-fatores": "ganho: lista dos três fatores; a fração tem card próprio de definição",
 "k-preditores": "ganho: os três preditores juntos; 'growth' em k-criterios é critério de benignidade"}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {"pt75-arvore.png": "lâmina 10: árvore de mutações (ubíquas, do primário, das metástases, únicas), recortada sem o desenho de Darwin", "pt75-cis.png": "lâmina 6: normal → hiperplasia → displasia → carcinoma in situ → invasor, recortada e legível",
 "pt75-clonal.png": "lâmina 9 (Robbins): expansão clonal e variantes que dão heterogeneidade", "pt75-hallmarks.png": "lâmina 11: roda dos hallmarks de Hanahan & Weinberg",
 "pt75-prolif.png": "lâmina 12: proliferação × remoção com as três situações", "pt75-divisoes.png": "lâmina 13: 30 divisões até 10^9 células (1 g) e mais 10 até 1 kg",
 "pt75-ciclo.png": "lâmina 18: ciclo celular com os checkpoints G1/S e G2/M"}  # arquivo: "o que mostra e por que ensina" (toda imagem fora do AnKing, depois de ver)
REVISAO = {}
ESCOPO = {"objetivo": "Neoplasia: conceito, nomenclatura, critérios benigno × maligno, transformação, crescimento, invasão e metástase", "centrais": [("pilares", *[c["key"] for c in CARDS if str(c.get("motivo", "")).startswith("V-")])], "exemplos": ["ak1496162192905", "ak1496162245188", "k-checkpoints", "ak1496161616847"], "outras_aulas": ["76 oncogenes", "84 metástase", "74 epidemiologia"]}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
