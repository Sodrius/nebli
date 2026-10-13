"""Escreve à mão (com a imagem lida) as explicações dos cards que o gerador marcou 'revisar'."""
import re, sys, time, json
sys.path.insert(0, "/Users/davisousa/NEBLI")
from nebli.decks import Anki, escrita
from nebli import explicacoes as E

A = Anki()


def T(base, porque, aula, nao=None):
    s = f"Base: {base}\nPor quê: {porque}\nNa aula: {aula}"
    return s + (f"\nNão confundir: {nao}" if nao else "")


X = {}
# ---------- esôfago e estômago ----------
X[1790707312062] = T("O esôfago tem três partes: cervical, torácica e abdominal. Rótulo escondido: parte torácica.",
    "É a mais longa, uns 16–18 cm dos ~25 cm. Desce pelo mediastino posterior, atrás da traqueia, do arco aórtico, do brônquio principal esquerdo e do coração, até atravessar o hiato esofágico do diafragma.",
    "Esôfago, estômago e intestino delgado: reconhecer a parte pelo trajeto e pelas estruturas vizinhas.",
    "a parte abdominal é a mais curta e fica já abaixo do diafragma.")
X[1790707312161] = T("Depois de atravessar o hiato esofágico do diafragma (nível de T10), o esôfago ainda tem um trecho curto dentro do abdome. Rótulo escondido: esôfago abdominal.",
    "É a parte mais curta, cerca de 1,25 cm, e termina no óstio cárdico do estômago, a junção esofagogástrica.",
    "Esôfago, estômago e intestino delgado: ligar o esôfago ao estômago pelo hiato diafragmático.",
    "esôfago torácico (longo, no mediastino posterior) e esôfago abdominal (curto, sob o diafragma).")
X[1790707314335] = T("A porção distal do estômago é o piloro: antro pilórico, canal pilórico e esfíncter pilórico. Rótulo escondido: piloro.",
    "É a região de saída do estômago, que se continua com a parte superior do duodeno. O quimo passa por ela aos poucos, regulado pelo esfíncter.",
    "Estômago: nomear as regiões (cárdia, fundo, corpo, piloro) pela posição na peça.",
    "o piloro é a região inteira; o esfíncter pilórico é só o anel de músculo na saída.")
X[1790707314435] = T("O esfíncter pilórico é um espessamento da camada muscular circular na junção entre o estômago e o duodeno. Rótulo escondido: esfíncter pilórico.",
    "Ele fecha e abre a saída do estômago, controlando o esvaziamento gástrico. Fica aproximadamente no plano transpilórico, em L1.",
    "Estômago: saber o que regula a passagem do conteúdo gástrico para o duodeno.",
    "piloro (região do estômago) × esfíncter pilórico (o músculo na saída).")
X[1790707314536] = T("A mucosa gástrica forma pregas longitudinais chamadas rugas gástricas. Rótulo escondido: pregas gástricas (rugae).",
    "Com o estômago vazio elas são evidentes; com a distensão pelo alimento, elas se achatam e o órgão aumenta de volume sem esticar a mucosa.",
    "Estômago: estrutura interna da parede, vista na peça aberta.",
    "as pregas circulares do intestino delgado são permanentes e não somem com a distensão; as rugas gástricas somem.")
for cid, nome, baseTxt in [(1790707313337, "cárdia", "A cárdia é a região do estômago em volta do óstio por onde o esôfago desemboca, logo abaixo da junção esofagogástrica."),
                           (1790707313437, "fundo", "O fundo gástrico é a cúpula do estômago, acima do nível do óstio cárdico, em contato com a cúpula esquerda do diafragma."),
                           (1790707313536, "corpo", "O corpo é a parte principal do estômago, entre o fundo e o antro pilórico, e é onde ficam as curvaturas maior e menor.")]:
    X[cid] = T(baseTxt, "Cada região é definida pela posição em relação ao óstio cárdico, ao piloro e às curvaturas, não por uma linha marcada na peça. O card pede só o nome da região mostrada.",
               "Estômago: reconhecer as quatro regiões (cárdia, fundo, corpo, piloro) em peça de cadáver e em modelo.",
               "cárdia (em volta do óstio do esôfago), fundo (acima desse nível) e corpo (abaixo, até o antro).")
# ---------- duodeno ----------
D = "Duodeno: ~25 cm, em C ao redor da cabeça do pâncreas, em quatro partes: superior (L1), descendente (L1–L3), horizontal (L3) e ascendente (L3–L2)."
X[1790707315186] = T(D + " Rótulo escondido: parte superior (1ª).", "Começa no piloro, tem uns 5 cm e é a mais móvel; é nela que se forma o bulbo duodenal, local típico de úlcera.", "Duodeno: dar nome às quatro partes na peça.", "as partes superior e descendente ficam à direita da coluna; a horizontal cruza a linha média.")
X[1790707315286] = T(D + " Rótulo escondido: parte descendente (2ª).", "Desce do nível de L1 a L3 ao lado direito da cabeça do pâncreas e recebe a ampola hepatopancreática (colédoco e ducto pancreático principal) na parede posteromedial.", "Duodeno: dar nome às quatro partes na peça.", "é a parte onde ficam as papilas duodenais.")
X[1790707315386] = T(D + " Rótulo escondido: parte inferior/horizontal (3ª).", "Cruza a linha média em L3, por trás dos vasos mesentéricos superiores e à frente da veia cava inferior e da aorta; por isso uma compressão ali pode obstruir o duodeno.", "Duodeno: dar nome às quatro partes na peça.", "a 3ª passa por trás da artéria mesentérica superior; a 4ª sobe à esquerda da aorta.")
X[1790707315486] = T(D + " Rótulo escondido: parte ascendente (4ª).", "Sobe do lado esquerdo da aorta até a flexura duodenojejunal, onde o duodeno passa a jejuno; esse ponto é fixado pelo músculo suspensor do duodeno (ligamento de Treitz).", "Duodeno: dar nome às quatro partes na peça.", "ao fim da 4ª parte começa o jejuno, que já é intraperitoneal e móvel.")
X[1790707315786] = T("A papila duodenal maior fica na parede posteromedial da parte descendente do duodeno, onde se abre a ampola hepatopancreática (colédoco + ducto pancreático principal).",
    "A saída da bile e do suco pancreático é controlada pelo esfíncter da ampola (de Oddi). A papila maior marca também a passagem do intestino anterior para o médio, na embriologia.",
    "Duodeno: reconhecer as papilas na face interna da parte descendente.", "papila maior (ampola hepatopancreática) × papila menor (ducto pancreático acessório), cerca de 2 cm acima.")
X[1790707315886] = T("A papila duodenal menor fica acima da papila maior, na parte descendente do duodeno.",
    "É por onde se abre o ducto pancreático acessório (de Santorini), que drena parte do pâncreas quando existe.",
    "Duodeno: reconhecer as papilas na face interna da parte descendente.", "papila maior (ampola com colédoco) × papila menor (ducto acessório).")
# ---------- jejuno e íleo ----------
X[1790707316810] = T("O intestino delgado mesentérico (6–7 m) é formado por jejuno, cerca de 2/5, e íleo, cerca de 3/5. Rótulo escondido: jejuno.",
    "O jejuno fica na parte superior esquerda do abdome, tem parede mais espessa, maior calibre e pregas circulares mais altas; os vasos retos são mais longos e as arcadas arteriais, menos numerosas.",
    "Intestino delgado: distinguir jejuno de íleo pelos achados da peça.", "o íleo tem parede mais fina, menos pregas e placas de Peyer, e mais arcadas vasculares.")
X[1790707316912] = T("O íleo é a parte final do intestino delgado, cerca de 3/5 do segmento mesentérico. Rótulo escondido: íleo.",
    "Fica na parte inferior direita do abdome e termina na junção ileocecal. Tem parede mais fina, pregas circulares mais baixas, vasos retos curtos, mais arcadas e placas de Peyer.",
    "Intestino delgado: distinguir jejuno de íleo pelos achados da peça.", "no jejuno as pregas são mais proeminentes e as arcadas, em menor número.")
X[1790707317012] = T("O mesentério é uma prega dupla de peritônio que prende o jejuno e o íleo à parede posterior do abdome. Rótulo escondido: mesentério.",
    "Leva entre seus folhetos os vasos mesentéricos superiores, linfáticos e nervos para as alças. Sua raiz vai da flexura duodenojejunal à fossa ilíaca direita.",
    "Intestino delgado: ligação das alças à parede posterior e passagem dos vasos.", "mesentério (delgado) × mesocolo (cólon transverso e sigmoide).")
X[1790707317511] = T("A mucosa do jejuno forma pregas circulares (válvulas coniventes ou de Kerckring). Rótulo escondido: pregas circulares.",
    "São pregas permanentes de mucosa e submucosa que aumentam a superfície de absorção. São mais altas e numerosas no jejuno e diminuem no íleo distal.",
    "Intestino delgado: adaptação da parede para absorver.", "as rugas gástricas se achatam quando o estômago enche; as pregas circulares não.")
# ---------- ceco, cólon e apêndice ----------
X[1790707317761] = T("A junção ileocecal é o ponto onde o íleo desemboca no ceco, na fossa ilíaca direita. Rótulo escondido: junção ileocecal.",
    "Marca a passagem do delgado para o intestino grosso e é o ponto de referência para ceco, apêndice e cólon ascendente.",
    "Intestino grosso: onde começa o ceco.", "junção ileocecal (o encontro) × válvula ileocecal (a estrutura que fecha o óstio).")
X[1790707994033] = T("A válvula ileocecal fica no óstio ileal, onde o íleo entra no ceco. Rótulo escondido: válvula ileocecal.",
    "Seus lábios funcionam como válvula de mão única, deixando o conteúdo ir do delgado ao grosso e dificultando o refluxo para o íleo.",
    "Intestino grosso: estrutura de passagem entre delgado e ceco.", "junção ileocecal (o local) × válvula (a estrutura).")
X[1790707991959] = T("O ceco é a primeira parte do intestino grosso, uma bolsa em fundo cego abaixo da junção ileocecal, na fossa ilíaca direita. Rótulo escondido: ceco.",
    "É em grande parte intraperitoneal e livre. Nele se abre o apêndice vermiforme, abaixo do óstio ileal.",
    "Intestino grosso: nomear as partes na ordem do trajeto, começando pelo ceco.", "o apêndice sai do ceco; o ceco não é o apêndice.")
X[1790707992059] = T("O cólon ascendente sobe pelo lado direito do abdome desde o ceco até a flexura direita. Rótulo escondido: cólon ascendente.",
    "É secundariamente retroperitoneal e fixo: o peritônio cobre só a frente e os lados, o que o torna pouco móvel.",
    "Intestino grosso: saber quais partes são fixas e quais são móveis.", "cólon transverso e sigmoide são intraperitoneais e móveis, presos por mesocolos.")
X[1790707992158] = T("A flexura cólica direita (hepática) é a curva entre o cólon ascendente e o transverso, junto à face inferior do fígado. Rótulo escondido: flexura cólica direita (hepática).",
    "É uma curva mais baixa e menos aguda do que a esquerda e se relaciona com o fígado e o rim direito.",
    "Intestino grosso: pontos de referência entre as partes do cólon.", "a flexura esquerda (esplênica) é mais alta e mais posterior.")
X[1790707992259] = T("O cólon transverso cruza o abdome entre as duas flexuras. Rótulo escondido: cólon transverso.",
    "É intraperitoneal e móvel, suspenso pelo mesocolo transverso, e por isso sua posição varia com o enchimento.",
    "Intestino grosso: contraste entre partes fixas e móveis.", "ascendente e descendente são retroperitoneais e fixos.")
X[1790707992360] = T("A flexura cólica esquerda (esplênica) é a curva entre o cólon transverso e o descendente, junto ao baço. Rótulo escondido: flexura cólica esquerda (esplênica).",
    "É mais alta e mais posterior que a direita, presa ao diafragma pelo ligamento frenocólico. É zona de transição entre as áreas irrigadas pelas artérias mesentérica superior e inferior.",
    "Intestino grosso: pontos de referência entre as partes do cólon.", "a flexura direita é a hepática, mais baixa.")
X[1790707992459] = T("O cólon descendente desce pelo lado esquerdo do abdome, da flexura esplênica até a fossa ilíaca esquerda. Rótulo escondido: cólon descendente.",
    "Como o ascendente, é secundariamente retroperitoneal e fixo.", "Intestino grosso: partes fixas e móveis.", "o sigmoide, que vem depois, é móvel.")
X[1790707992561] = T("O cólon sigmoide é a parte em S entre o descendente e o reto. Rótulo escondido: cólon sigmoide.",
    "É intraperitoneal e móvel, preso pelo mesocolo sigmoide, o que o deixa sujeito a torção (vólvulo).",
    "Intestino grosso: parte móvel antes do reto.", "o reto é retroperitoneal em grande parte e sem tênias.")
X[1790707992659] = T("O reto é a parte terminal do intestino grosso, com cerca de 15 cm, entre o sigmoide e o canal anal. Rótulo escondido: reto.",
    "Diferente do cólon, não tem tênias, haustros nem apêndices omentais.", "Intestino grosso: transição do cólon para o canal anal.", "o sigmoide tem mesocolo e é móvel; o reto está na pelve.")
X[1790707992782] = T("O mesocolo sigmoide é a prega de peritônio que prende o cólon sigmoide à parede posterior da pelve. Rótulo escondido: mesocolo sigmoide.",
    "Dá ao sigmoide a mobilidade que o torna sujeito a vólvulo e leva os vasos sigmoides.", "Intestino grosso: ligações peritoneais das partes móveis.", "mesocolo transverso (cólon transverso) × mesocolo sigmoide.")
X[1790707993384] = T("As tênias do cólon são três faixas longitudinais de músculo liso na parede do intestino grosso. Rótulo escondido: tênias do cólon.",
    "Elas são mais curtas que o intestino e, ao puxá-lo, formam os haustros. Convergem na base do apêndice vermiforme.",
    "Intestino grosso: características que separam o cólon do delgado e do reto.", "o reto não tem tênias.")
X[1790707993485] = T("Os haustros são saculações da parede do cólon. Rótulo escondido: haustro do cólon.",
    "Aparecem porque as tênias são mais curtas que o resto da parede e a franzem entre si.", "Intestino grosso: aspecto externo do cólon.", "o reto não tem haustros.")
X[1790707993583] = T("Os apêndices omentais (epiploicos) são pequenas bolsas de peritônio cheias de gordura penduradas ao longo do cólon. Rótulo escondido: apêndice omental (epiploico).",
    "Ajudam a distinguir o cólon do delgado, junto com as tênias e os haustros.", "Intestino grosso: aspecto externo do cólon.", "apêndice omental (gordura) × apêndice vermiforme (tubo do ceco).")
X[1790707993933] = T("O apêndice vermiforme tem de 6 a 10 cm, é rico em tecido linfoide e se abre no ceco, abaixo do óstio ileal. Rótulo escondido: apêndice vermiforme.",
    "Sua base é o ponto onde convergem as tênias do cólon, caminho usado para localizá-lo na cirurgia.", "Intestino grosso: apêndice e ceco.", "apêndice vermiforme × apêndices omentais.")
# ---------- reto e canal anal ----------
X[1790707995234] = T("O reto tem pregas transversais na parede interna. Rótulo escondido: pregas transversas do reto.",
    "Em geral são três (duas à esquerda e uma à direita) e ajudam a sustentar as fezes e a retardar a progressão do conteúdo.", "Reto e canal anal: parede interna.", "colunas anais são longitudinais e ficam no canal anal.")
X[1790707995334] = T("A ampola retal é a parte dilatada do reto, logo acima do assoalho pélvico. Rótulo escondido: ampola retal.",
    "Armazena as fezes até a defecação.", "Reto e canal anal: onde as fezes ficam retidas.", "ampola retal (dilatada) × canal anal (estreito, abaixo do assoalho pélvico).")
X[1790707995433] = T("O músculo puborretal é a parte do levantador do ânus que forma uma alça em volta da junção anorretal. Rótulo escondido: m. puborretal.",
    "A alça puxa o reto para a frente e mantém o ângulo anorretal, um dos mecanismos da continência fecal.", "Reto e canal anal: continência.", "esfíncter externo do ânus (voluntário, próprio do canal) × puborretal (alça do assoalho pélvico).")
X[1790707995732] = T("A escavação retouterina (fundo de saco de Douglas) é o espaço peritoneal entre o reto e o útero. Rótulo escondido: escavação retouterina.",
    "Na mulher é o ponto mais baixo da cavidade peritoneal, onde líquido ou pus tendem a se acumular.", "Reto e canal anal: relações peritoneais na pelve feminina.", "no homem esse espaço é a escavação retovesical.")
X[1790707995835] = T("A escavação retovesical é o espaço peritoneal entre o reto e a bexiga. Rótulo escondido: escavação retovesical.",
    "No homem é o ponto mais baixo da cavidade peritoneal.", "Reto e canal anal: relações peritoneais na pelve masculina.", "na mulher o espaço entre reto e útero é a escavação retouterina.")
X[1790707996034] = T("A linha pectínea (dentada) marca a junção entre a parte superior do canal anal, de origem endodérmica, e a inferior, ectodérmica. Rótulo escondido: linha pectínea.",
    "Acima dela a inervação é visceral (indolor) e a drenagem vai para linfonodos pélvicos; abaixo, a inervação é somática (dolorosa) e a drenagem vai para linfonodos inguinais. Também separa hemorroidas internas de externas.",
    "Canal anal: o ponto que muda irrigação, inervação e drenagem.", "colunas anais ficam acima da linha; o esfíncter externo envolve o canal abaixo dela.")
X[1790707996134] = T("As colunas anais são pregas longitudinais da mucosa na parte superior do canal anal. Rótulo escondido: colunas anais.",
    "Contêm ramos terminais dos vasos retais superiores e correspondem aos coxins das hemorroidas internas.", "Canal anal: estrutura interna.", "colunas anais (pregas) × seios anais (depressões entre elas).")
X[1790707996235] = T("O seio anal é a depressão entre as bases de duas colunas anais, fechada por uma válvula. Rótulo escondido: seio anal.",
    "Nele se abrem as glândulas anais; a obstrução ou infecção dessas glândulas é a origem de muitos abscessos anorretais.", "Canal anal: estrutura interna.", "colunas anais (pregas) × seios anais (depressões).")
X[1790707997933] = T("O esfíncter externo do ânus é de músculo estriado esquelético e envolve o canal anal. Rótulo escondido: esfíncter externo do ânus.",
    "É voluntário e inervado pelo nervo retal inferior, ramo do pudendo, de modo que a pessoa o contrai para evitar a evacuação.", "Canal anal: controle da continência.", "esfíncter interno (liso, involuntário) × externo (estriado, voluntário).")
X[1790707998033] = T("O esfíncter interno do ânus é de músculo liso e continua a camada muscular circular do reto. Rótulo escondido: esfíncter interno do ânus.",
    "É involuntário, sob controle autonômico, e responde pela maior parte do tônus de repouso do canal anal.", "Canal anal: controle da continência.", "esfíncter interno (liso, involuntário) × externo (estriado, voluntário).")
# ---------- cards de texto ----------
X[1790173044735] = T("O tempo de geração (ou de duplicação) é o tempo que a população bacteriana leva para dobrar. O card esconde só 'growth', o que é ambíguo, porque todas as fases fazem parte do crescimento.",
    "Quem depende do tempo de geração é a taxa de crescimento na fase exponencial (log), porque é ali que as células se dividem de forma constante: quanto menor o tempo de geração, mais íngreme a curva. Na fase lag há adaptação e na estacionária a divisão se iguala à morte.",
    "Fisiologia bacteriana: curva de crescimento e o que define cada fase (também caiu em P2).", "o card original provavelmente queria 'exponential/log' e vale conferir o texto.")
X[1790253537707] = T("O derrame ou líquido inflamatório (exsudato) tem alta permeabilidade vascular. A tabela da aula usa limites de proteína acima de 3 g/dL, densidade acima de 1,020 e LDH acima de 200.",
    "Os valores servem para separar exsudato (inflamação, proteína alta) de transudato (pressão hidrostática ou baixa albumina, líquido pobre em proteína). Por isso a proteína sobe: a permeabilidade vascular deixa as proteínas passarem.",
    "Inflamação aguda: reconhecer o exsudato pela composição.", "esses limites são da tabela da aula; critérios diagnósticos clínicos usam outros pontos de corte.")
X[1790264468141] = T("A insulina age principalmente em três tecidos: fígado, músculo e tecido adiposo. Esses são os alvos do hormônio anabólico.",
    "No fígado, favorece a síntese de glicogênio e inibe a gliconeogênese. No músculo, aumenta a entrada de glicose pelo GLUT4 e a síntese de glicogênio. No tecido adiposo, também pelo GLUT4, favorece a síntese de triglicerídeos e inibe a lipólise.",
    "Integração metabólica: quem responde à insulina no estado alimentado.", "o fígado não depende de GLUT4 para captar glicose; usa GLUT2.")
X[1790264929589] = T("O Streptococcus do grupo B (GBS) coloniza a vagina e o reto e é a principal causa de sepse e meningite neonatal. O rastreio é por cultura vaginal e retal.",
    "O card traz 36–38 semanas, mas o Extra diz que na aula é 35–37 e a recomendação atual da literatura (ACOG) é 36 0/7 a 37 6/7. O resultado vale cerca de 5 semanas. Positivo: penicilina G intraparto, ≥ 4 h antes do parto.",
    "Controle microbiológico: prevenção da infecção neonatal.", "vale confirmar com a aula qual janela cobrar, porque o card e a aula divergem.")
open(__file__.replace("escrever.py", "explicacoes-escritas.json"), "w").write(json.dumps({str(k): v for k, v in X.items()}, ensure_ascii=False, indent=1))

# ---------- corrige o GLP do Grand Round e escreve ----------
def glp_texto():
    return T("Incretinas são hormônios intestinais que aumentam a secreção de insulina depois da refeição. A principal é o GLP-1; a outra é o GIP.",
        "No diabetes tipo 2 a resposta de incretina é insuficiente e as células β secretam menos insulina do que deveriam; por isso análogos de GLP-1 e inibidores da DPP-4 são usados.",
        "Grand Round 2 (diabetes): disfunção da célula β.", "o cloze escondia só 'GLP'; o certo é GLP-1, porque o GIP também é incretina.")

with escrita(A, "tab: corrige GLP-1 e escreve revisar à mão"):
    nid = A("cardsInfo", cards=[1790335382878])[0]["note"]
    n = A("notesInfo", notes=[nid])[0]
    t = n["fields"]["Text"]["value"]
    new = re.sub(r"(\{\{c1::\s*(?:<[^>]+>)*)GLP((?:</[^>]+>)*\s*\}\})", r"\1GLP-1\2", t)
    assert new != t, t
    A("updateNoteFields", note={"id": nid, "fields": {"Text": new}})
X[1790335382878] = glp_texto()

db = E.open_store(); version = E.style_version(E.STYLE.read_text(encoding="utf-8")); stamp = time.strftime("%Y-%m-%d %H:%M:%S")
ids = list(X)
cards = {c["cardId"]: c for c in A("cardsInfo", cards=ids)}
falta = [i for i in ids if i not in cards]
assert not falta, falta
for cid, texto in X.items():
    c = cards[cid]
    ordered = [f["value"] for f in sorted(c["fields"].values(), key=lambda f: f["order"])]
    db.execute("insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)",
               (cid, c["note"], E.card_hash(ordered, c["ord"]), "ok", texto, None, version, "claude-direto (imagem/rótulo lido)", stamp))
db.commit()
print(len(X), "explicações gravadas")
