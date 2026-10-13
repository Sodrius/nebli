"""Plano curado desta manutenção. Não escreve no Anki; IDs vêm do snapshot vivo."""
import copy, html, json, re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).parent
S = json.loads((BASE/'snapshot.json').read_text())
IDS = json.loads((BASE/'index.json').read_text())
CARDS = {c['cardId']:c for c in S['cards']}
NOTES = {n['noteId']:n for n in S['notes']}
P = {'notes':[], 'models':[], 'flags':[]}
def val(nid, field): return NOTES[nid]['fields'][field]['value']
def nid(i): return CARDS[IDS[i]]['note']
def media_tail(n):
    extra=val(n,'Extra')
    match=re.search(r'<img\b', extra)
    return '<br><br>'+extra[match.start():] if match else ''
def change(n, reason, sources, **fields):
    before={f:val(n,f) for f in fields}
    if 'Text' in fields:
        assert set(re.findall(r'{{c(\d+)::',before['Text'])) == set(re.findall(r'{{c(\d+)::',fields['Text'])), n
    P['notes'].append({'noteId':n,'reason':reason,'sources':sources,'before':before,'after':fields})

IRON=['https://www.ncbi.nlm.nih.gov/books/NBK538257/', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6487204/']
FERM=['https://www.ncbi.nlm.nih.gov/sites/books/NBK7919/']
GROW=['https://openstax.org/books/microbiology/pages/9-1-how-microbes-grow']
HIST=['https://www.ncbi.nlm.nih.gov/books/NBK26875/']
change(1790173050491,'Comentário: explicar por que o hospedeiro retém ferro e como a bactéria o recupera.',IRON,
 Extra='Bactérias precisam de ferro para enzimas essenciais. O hospedeiro o mantém ligado a proteínas, dificultando o crescimento microbiano. Sideróforos capturam ferro com alta afinidade; receptores bacterianos recolhem o complexo.<br><br>Com pouco ferro, o repressor Fur perde sua ação: a bactéria aumenta a produção de sistemas de captação.'+media_tail(1790173050491),NEBLI_Comentario='')
change(1790190268556,'Comentário: ligar hepcidina, ferroportina e restrição de ferro, em duas frases.',IRON,
 Text='During inflammation, hepcidin lowers circulating {{c1::iron}}, limiting its availability to microbes.',
 Extra='A hepcidina induz a degradação da ferroportina, a porta de saída do ferro de enterócitos e macrófagos. Assim, menos ferro chega ao plasma para sustentar o crescimento de microrganismos extracelulares.',NEBLI_Comentario='')
change(1790173050816,'Vermelho/comentário: reduzir a lista e distinguir os aceptores sem afirmar que toda respiração anaeróbia usa molécula inorgânica.',FERM,
 Text='Anaerobic respiration can use an {{c1::inorganic}} electron acceptor; fermentation reduces an {{c2::organic}} molecule.',
 Extra='Na respiração anaeróbia, uma cadeia transportadora transfere elétrons para um aceptor diferente de O₂, como nitrato ou sulfato. Na fermentação, uma molécula orgânica recebe elétrons do NADH e regenera NAD⁺, permitindo que a glicólise continue produzindo ATP.<br><br>Há aceptores orgânicos também na respiração anaeróbia, como fumarato; a diferença principal é o uso da cadeia respiratória.'+media_tail(1790173050816),NEBLI_Comentario='')
change(1790190269338,'Vermelho sem comentário: exemplo concreto mantendo o alvo tempo de geração e c2.',GROW,
 Text='A bacterial population grows from 1,000 to 2,000 cells in one {{c2::generation (doubling) time}}.',
 Extra='É o tempo para a população dobrar durante o crescimento exponencial. Depende da espécie e das condições de cultivo; não é um valor fixo para todas as bactérias.')
change(1790190268210,'Vermelho: um alvo principal; contraste halófilo fica na explicação.', ['https://openstax.org/books/microbiology/pages/9-summary'],
 Text='<i>S. aureus</i> grows despite high salt without requiring it: it is {{c1::halotolerant}}.',
 Extra='Halotolerante suporta sal; halófilo precisa dele para crescer. Essa tolerância ajuda a explicar por que meios salgados selecionam estafilococos.'+media_tail(1790190268210))
change(1790190269721,'Comentário: explicar a produção de ácidos; corrigir os exemplos de AGCC sem criar outro card.',FERM+['https://www.ncbi.nlm.nih.gov/books/NBK7670/?report=reader'],
 Text='Bacterial fermentation in the colon produces gases and {{c2::short-chain fatty acids}}, such as acetate, propionate and butyrate.',
 Extra='Na fermentação, o carbono do substrato sai parcialmente oxidado em produtos como ácidos e álcoois. No cólon, a microbiota transforma carboidratos não digeridos em AGCC; o butirato alimenta os colonócitos.<br><br>Lactato é produto da fermentação lática; os principais AGCC colônicos são acetato, propionato e butirato.',NEBLI_Comentario='')
change(nid(1084),'Exemplo solicitado por Davi: sinal de Godet com mecanismo visível, mantendo a identificação do sinal.', ['https://www.ncbi.nlm.nih.gov/books/NBK348/'],
 Text='A persistent indentation after pressing edematous skin is {{c1::pitting edema (Godet sign)}}.',
 Extra='O dedo desloca o líquido intersticial, deixando uma depressão que demora a se preencher: o cacifo. É a mobilidade desse líquido que explica o sinal; fibrose pode tornar o edema pouco depressível.')
change(nid(219),'Correção factual: gliconeogênese desvia oxaloacetato; não é impedida pela cetogênese.', ['https://www.ncbi.nlm.nih.gov/books/NBK493179/?report=reader'],
 Text='During fasting, diversion of {{c1::oxaloacetate}} toward gluconeogenesis limits acetyl-CoA entry into the TCA cycle, favoring ketogenesis.',
 Extra='A β-oxidação fornece acetil-CoA ao fígado. Com menos oxaloacetato disponível para formar citrato, parte desse acetil-CoA é direcionada à produção de corpos cetônicos. Gliconeogênese e cetogênese podem ocorrer simultaneamente.')
change(nid(576),'Frente e figura devem concordar nas quatro fases; retirar a afirmação de esterilização inevitável.', GROW,
 Text='In a closed culture, bacterial growth follows {{c1::lag → log (exponential) → stationary → death}}.',
 Extra='Adaptação → divisões rápidas → divisão e morte se equilibram → morte supera divisão. O esgotamento de nutrientes e o acúmulo de resíduos explicam a mudança; a fase de declínio não garante eliminação de todas as células.'+media_tail(nid(576)))
change(nid(611),'Correção factual: catalase libera O₂; glutationa peroxidase reduz peróxido a água. Remover esquema linear incorreto.', ['https://openstax.org/books/microbiology/pages/9-2-oxygen-requirements-for-microbial-growth'],
 Text='Two enzymes that detoxify hydrogen peroxide are {{c1::catalase and glutathione peroxidase}}.',
 Extra='Catalase: 2 H₂O₂ → 2 H₂O + O₂.<br>Glutationa peroxidase: H₂O₂ + 2 GSH → 2 H₂O + GSSG.<br><br>Ambas removem peróxido; a peroxidase usa um doador de elétrons e não libera O₂.')
change(nid(826),'Correção factual: PVL é toxina formadora de poros, não protease.', ['https://wwwnc.cdc.gov/eid/article/12/7/05-0865_article'],
 Text='Some <i>S. aureus</i> strains produce {{c1::Panton-Valentine leukocidin (PVL)}}, a pore-forming toxin that damages leukocytes.')
change(nid(1062),'Separar congestão retrógrada da redução de fluxo à frente; preservar ambos os clozes.', ['https://pubmed.ncbi.nlm.nih.gov/32897746/'],
 Text='Left heart failure can cause {{c1::pulmonary}} venous congestion and {{c2::decreased}} systemic perfusion.',
 Extra='Para trás: a pressão elevada se transmite às veias e aos capilares pulmonares, favorecendo edema. Para a frente: menor débito pode reduzir a perfusão dos tecidos. São consequências distintas, que podem coexistir.')
change(nid(1430),'Condensar o card de criptas, preservar c1–c4 e corrigir pluripotente para multipotente.',HIST,
 Text='{{c1::Crypts of Lieberkühn}} are {{c2::short tubular glands between villi}}. Their {{c3::multipotent stem cells}} replenish {{c4::enterocytes}} and other intestinal epithelial cells.',
 Extra='As criptas são contínuas com o epitélio das vilosidades. Suas células-tronco renovam as linhagens epiteliais intestinais; enterócitos fazem absorção.'+media_tail(nid(1430)))
change(nid(1434),'Condensar o card de células caliciformes; separar mucinas de muco e preservar c1–c3.',HIST,
 Text='Intestinal {{c1::goblet cells}}, interspersed among {{c2::absorptive enterocytes}}, secrete {{c3::mucins}}.',
 Extra='As mucinas são glicoproteínas que se hidratam e formam o gel do muco. Esse gel lubrifica e protege a superfície intestinal.'+media_tail(nid(1434)))
change(nid(1202),'A imagem anterior destacava o canal (7), não o orifício. Usar a figura já existente da junção pilórica com pergunta que especifica a relação.', ['Acervo AnatoKing local: comparação visual dos cards 1201–1203 no snapshot'],
 Header='Name the opening controlled by the sphincter highlighted at 2.',
 Cadaver=val(nid(1203),'Cadaver'))
change(nid(1216),'O esquema não permite inferir o segmento intestinal; fornecê-lo como contexto da identificação de pregas.', ['Acervo AnatoKing local: figura inspecionada'],
 Header='In this ileum diagram, identify the folds indicated by the arrow.')

# Apresentação: somente tipos de nota clonados para NEBLI, conferidos novamente antes de gravar.
base_css=S['models']['NEBLI AnKing independente - v3']['styling']['css']
for model in ['NEBLI AnKingMCAT independente - v1','NEBLI UC08 AnatoKing V2 v1','NEBLI UC08 Visceral Anatomy v1']:
    before=copy.deepcopy(S['models'][model]); after=copy.deepcopy(before)
    if 'AnKingMCAT' in model:
        after['styling']['css']=base_css
    elif 'AnatoKing' in model:
        for side, template in after['templates']['Cloze'].items():
            template,n=re.subn(r'{{#Cadaver}}[\s\S]*?{{/Cadaver}}','{{#Cadaver}}<div id="cadaver" class="nebli-recognition">{{Cadaver}}</div>{{/Cadaver}}',template)
            assert n==1
            template=template.replace('var ScrollToButton = true;', 'var ScrollToButton = false;')
            if side=='Back':
                template,n=re.subn(r'{{#Extra}}[\s\S]*?{{/Extra}}','{{#Extra}}<div id="extra">{{Extra}}</div>{{/Extra}}',template)
                assert n==1
            after['templates']['Cloze'][side]=template
        after['styling']['css']+='''
/* NEBLI: a imagem é o enunciado da identificação. */
#cadaver img, .mobile #cadaver img {
  width: auto !important; height: auto !important;
  max-width: 100% !important; max-height: 72vh !important;
  object-fit: contain;
}
.nebli-recognition { margin: .6em auto; max-width: 1000px; }
#extra { margin: .8em auto; max-width: 48em; }
.nightMode #extra, .night_mode #extra { color: #c7dbef; }
'''
    else:
        after['styling']['css']+='''
/* NEBLI: contraste e leitura no tablet. */
.card { font-family: Arial, sans-serif; font-size: 24px; background: #D1CFCE; }
.card [id] { font-family: inherit; font-size: inherit; }
.card img { max-width: 100%; height: auto; }
.nightMode.card, .night_mode .card { color: #fffafa; background: #272828; }
.nightMode.card [id], .night_mode .card [id] { color: inherit; }
#answer, .nightMode.card #answer, .night_mode .card #answer { color: #4297f9; }
'''
    P['models'].append({'name':model,'before':before,'after':after})

(BASE/'plan.json').write_text(json.dumps(P,ensure_ascii=False,indent=1))
print(json.dumps({'notes':len(P['notes']),'cards_with_edited_notes':sum(c['note'] in {n['noteId'] for n in P['notes']} for c in S['cards']),'models':len(P['models'])}))
