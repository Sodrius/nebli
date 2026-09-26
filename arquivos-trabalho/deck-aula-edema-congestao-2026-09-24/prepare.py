"""Curated X4 plan from current collection and the edema section of the shared slides."""
import json,re,hashlib
from pathlib import Path
from collections import Counter

HERE=Path(__file__).parent
INV=json.loads((HERE/'inventory.json').read_text(encoding='utf-8'))
BY={n['nid']:n for n in INV['notes']}
LESSON='2026-uc03-patologia-23-edema-congestao'
DECK='NEBLI::UC03::P2::Patologia::Edema e congestão'
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
SELECTED=[1471466881536,1471466884199,1471466893190,1471466900946,
          1471914938644,1471914999950,1471915047213,1474503768203,
          1474503771577,1475363769043,1475453437333,
          1521169448163,1521170206006,1532735591750,1577916403894]
PINK=set()
TEXT_OVERRIDE={
 1471466884199:'When venous outflow is blocked, edema can result from {{c1::increased}} capillary hydrostatic pressure.',
 1471466893190:'With substantial urinary albumin loss, edema can result from {{c1::decreased}} plasma oncotic pressure.',
 1471466900946:'At an inflamed site, edema can result from {{c1::increased}} vascular permeability.',
 1471914999950:'When the right ventricle fails, blood backs up in the {{c1::systemic}} venous circulation.',
 1521169448163:'In renal failure, retention of {{c1::sodium and water}} expands intravascular volume and can worsen edema.',
 1521170206006:'After axillary lymph node removal, arm edema may result from {{c1::lymphatic}} disruption.',
}
AUTHORIAL=[
 ('edema-def','No exame de um tecido inchado, edema é acúmulo de líquido no {{c1::interstício}} ou em cavidade serosa.','Não confundir com tumefação intracelular da lesão celular.'),
 ('hyperemia','Músculo em exercício fica vermelho vivo por {{c1::hiperemia}}: dilatação arteriolar ativa aumenta a entrada de sangue oxigenado.','Congestão, em contraste, é retenção venosa passiva.'),
 ('congestion','Um órgão azulado por dificuldade de drenagem venosa apresenta {{c1::congestão}}.','O sangue retido é relativamente desoxigenado; a pressão venosa pode favorecer edema.'),
 ('starling','No capilar, a pressão hidrostática favorece {{c1::filtração}} para o interstício, enquanto a oncótica plasmática se opõe à saída de água.','A drenagem linfática remove o excedente filtrado. A descrição clássica de reabsorção venosa ampla é simplificada e não é necessária aqui.'),
 ('venous','Uma trombose venosa em uma perna eleva a pressão {{c1::hidrostática}} capilar a montante e favorece edema local.','A distribuição unilateral ajuda a ligar o achado à obstrução do retorno venoso.'),
 ('raas','Na insuficiência cardíaca, menor perfusão renal ativa o SRAA: retenção de {{c1::sódio e água}} pode agravar o edema.','O volume retido aumenta a pressão hidrostática quando a bomba cardíaca continua falha.'),
 ('hydrothorax','Líquido de edema na cavidade pleural recebe o nome de {{c1::hidrotórax}}.','O nome indica a localização, não determina a causa do líquido.'),
 ('hydropericardium','Líquido de edema no saco pericárdico recebe o nome de {{c1::hidropericárdio}}.','O nome indica a localização, não determina a causa do líquido.'),
 ('ascites','Líquido de edema na cavidade peritoneal é {{c1::ascite}}.','Na cirrose, hipertensão portal e retenção renal de sódio contribuem para a coleção.'),
 ('anasarca','Edema subcutâneo grave e generalizado chama-se {{c1::anasarca}}.','O termo descreve extensão, não mecanismo.'),
 ('pitting','A pressão do dedo deixa uma depressão persistente no edema com {{c1::cacifo}}.','É comum em edema hidrostático ou por hipoalbuminemia; o linfedema crônico pode endurecer.'),
 ('pulm-micro','Na congestão pulmonar aguda por falência esquerda, capilares alveolares ficam {{c1::ingurgitados}} e pode haver líquido nos alvéolos.','O pulmão fica pesado e úmido; hemorragias focais também podem ocorrer.'),
 ('heart-failure-cells','Na congestão pulmonar crônica, hemácias extravasadas são fagocitadas; macrófagos alveolares acumulam {{c1::hemossiderina}}.','São as chamadas células da insuficiência cardíaca, junto a espessamento e fibrose septal.'),
 ('nutmeg','Na congestão hepática crônica, o fígado em noz-moscada alterna centros lobulares {{c1::escuros e congestos}} com periferia mais pálida.','A região centrolobular (zona 3) é mais vulnerável à hipóxia.'),
 ('pulm-vs-systemic','Falência do ventrículo esquerdo represa sangue nos {{c1::pulmões}}; a direita favorece congestão venosa sistêmica e hepática.','O território a montante da câmara falha aponta o órgão congesto.'),
]

def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def main():
    assert len(SELECTED)==len(set(SELECTED)) and set(SELECTED)<=BY.keys()
    entries=[]
    for nid in SELECTED:
        n=BY[nid]
        assert 'Anking Step Deck' in n['cards'][0]['deck'],nid
        f={k:(v if k in ('Text','Extra') else '') for k,v in n['fields'].items()}
        if nid in TEXT_OVERRIDE:f['Text']=TEXT_OVERRIDE[nid]
        # Keep useful explanatory extras but remove unrelated media or tangents.
        if nid in (1471915047213,1474503768203,1474503771577,1475363769043,1521170206006):f['Extra']=''
        count=len(set(re.findall(r'\{\{c(\d+)::',f['Text'])))
        assert count==len(n['cards']),nid
        entries.append(dict(source_nid=nid,source_model=n['model'],source_fields_hash=digest(n['fields']),source_deck=n['cards'][0]['deck'],source_tags=n['tags'],origin='AnKing',fields=f,expected_cards=count,pink=nid in PINK,high_yield=HY in n['tags']))
    template=BY[SELECTED[0]]
    for key,front,extra in AUTHORIAL:
        f={k:'' for k in template['fields']};f['Text']=front;f['Extra']=extra
        entries.append(dict(source_nid=None,key=key,source_model=template['model'],source_fields_hash=None,source_deck=None,source_tags=[],origin='Autoral',fields=f,expected_cards=1,pink=key in {'hydrothorax','hydropericardium','anasarca'},high_yield=False))
    totals=dict(notes=len(entries),cards=sum(e['expected_cards'] for e in entries),by_origin=dict(Counter({o:sum(e['expected_cards'] for e in entries if e['origin']==o) for o in {'AnKing','Autoral'}})),pink=sum(e['expected_cards'] for e in entries if e['pink']),green=sum(e['expected_cards'] for e in entries if e['high_yield'] and not e['pink']),shared_notes=1)
    out=dict(lesson_id=LESSON,target_deck=DECK,profile=INV['profile'],source_folder='https://drive.google.com/drive/folders/19ioIh10BJvh6nllTZfBcn0-2k8Auovrj',source_inventory='inventory.json',shared_note_id=1790253536913,entries=entries,totals=totals)
    (HERE/'plan.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(totals,ensure_ascii=False))
if __name__=='__main__':main()
