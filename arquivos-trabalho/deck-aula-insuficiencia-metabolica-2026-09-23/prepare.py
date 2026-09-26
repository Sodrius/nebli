import hashlib,json,re,sys
from pathlib import Path
from ak import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc21-p5-insuficiencia-metabolica'
BASE='NEBLI::UC21::P5::Insuficiência metabólica'
DECK_R=BASE+'::1 - Roteiro do caso'
DECK_X=BASE+'::2 - DM além do roteiro'
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ALEM_OBJ={'RX','GDM','HYPO'}
ROTEIRO_OVERRIDE={1524164649491,1539448229431}  # hipoglicemia e exercício (pergunta 11)
ALEM_OVERRIDE={1474164729347,1584135130853,1462206324429,1482971521846,1583352863014,
 1500918912753,1584135569745,1500920723465,1463176792455,
 1500925972834,1502846199357,1552131126029,1523243276095,
 1539460313520,1502564440992,1502564547478,1552260881200,1568856424118,1502564625891,1557425905993,1502647380072,1502414496794,1525305295646,
 1462327473707,1502846424371,1585334906873,1573310478617,
 1500333974625,1500334485985,1500333904310,1522594779687,1500235637454,1475452928405,1520458741002,1462327377004,
 1525378963748,1474686260264,1474686363427,1474686367174,1475364129715,1522546037015,1584389618617,1584395799101,1484603688155,1484603682428,
 1584395283495,1584395533879,1578293118238,1584392259000,1502484482346,1502483741339,1461600915818,1578931163024,1502576135467,1500922486145,
 1557518117356,1475353745252,1496607797915,1505746867430,1481771819827,1496699433704,1522550673436,1522550767866}
SEX='<i><span style="font-size: 10pt;">'
EDITS={
 1474165370026:[('uncloze',[1])],1474165374725:[('uncloze',[1])],1500333974625:[('uncloze',[3])],
 1482021920866:[('uncloze',[4])],1474253707546:[('uncloze',[3])],
 1475203898709:[('set','Extra','')],
 1686427339913:[('set','Extra','APS-1 (deficiência de AIRE) é outra síndrome: hipoparatireoidismo, insuficiência adrenal e candidíase mucocutânea crônica.')],
 1481771819827:[('set','Extra','Lipo-hialinose das pequenas artérias perfurantes, por hipertensão e diabetes.')],
 1462206324429:[('set','Extra','O GH antagoniza a ação da insulina (efeito diabetogênico).')],
 1475200506347:[('set','Extra','<img src="0e7e633ce068dc739fda90e4ffddcd3f.webp">')],
 1462913246058:[('regex','Extra',r'Not recommended with creatinine.*?treatment','Contraindicated if eGFR &lt; 30 mL/min/1.73 m² — check renal function before starting')],
}
AUTHORED=[
 ('pkc-dag','In hyperglycemia, de novo synthesis of {{c1::diacylglycerol (DAG)}} activates {{c2::protein kinase C}} in vascular cells',
  'A PKC ativada aumenta VEGF, TGF-β e PAI-1: mais permeabilidade vascular, espessamento da membrana basal e fibrose (retina, glomérulo).'
  '<br><br><img src="nebli-dm-pkc-dag.jpg"><br>'+SEX+'DAG ativando PKC (imagem de um card do AnKing, via receptor/PLC; na hiperglicemia o DAG vem de intermediários da glicólise).</span></i>','CX'),
 ('age-rage','AGEs bind {{c1::RAGE}} on endothelium and macrophages, triggering ROS and inflammatory cytokines',
  'AGE: glicose + grupo amino de proteína → base de Schiff (reversível) → produto de Amadori → AGE (irreversível). Os AGEs também fazem ligações cruzadas no colágeno e retêm LDL e albumina na parede do vaso.'
  '<br><br><img src="nebli-dm-glycation-amadori.png"><br>'+SEX+'Glicação via rearranjo de Amadori. Smokefoot, domínio público, via Wikimedia Commons.</span></i>','CX'),
]
MEDIA=[('img/pkc-anking.jpg','nebli-dm-pkc-dag.jpg'),('img/nebli-dm-glycation-amadori.png','nebli-dm-glycation-amadori.png')]
def digest(v): return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def clozes(v): return sorted({int(x) for x in re.findall(r'{{c(\d+)::',v)})
CLOZE=re.compile(r'\{\{c(\d+)::((?:(?!\}\}).)*?)(?:::((?:(?!\}\}).)*?))?\}\}',re.S)
def uncloze(text,nums): return CLOZE.sub(lambda m: m.group(2) if int(m.group(1)) in nums else m.group(0),text)
def load_decisions():
    rows=[]
    for fn in ['decisions1.txt','decisions2.txt','decisions3.txt']:
        for l in open(ROOT/fn,encoding='utf-8'):
            if l[0].isdigit():
                p=l.split(); rows.append((int(p[0]),p[1],'r' in p[2:]))
    return rows
def scope(nid,obj):
    if nid in ROTEIRO_OVERRIDE: return 'roteiro'
    if obj in ALEM_OBJ or nid in ALEM_OVERRIDE: return 'alem'
    return 'roteiro'
def main():
    rows=load_decisions()
    notes={n['noteId']:n for n in call('notesInfo',notes=[r[0] for r in rows])}
    entries=[]
    for nid,obj,rosa in rows:
        n=notes[nid]; f={k:v['value'] for k,v in n['fields'].items()}
        log=[]
        for e in EDITS.get(nid,[]):
            if e[0]=='set': f[e[1]]=e[2]
            elif e[0]=='regex':
                new=re.sub(e[2],e[3],f[e[1]],flags=re.S)
                if new==f[e[1]]: raise RuntimeError(f'regex sem efeito {nid}')
                f[e[1]]=new
            elif e[0]=='uncloze':
                before=clozes(f['Text']); f['Text']=uncloze(f['Text'],set(e[1]))
                if set(clozes(f['Text']))!=set(before)-set(e[1]): raise RuntimeError(f'Uncloze {nid}')
            log.append(list(e[:2]))
        cleared=[k for k in RESOURCE_FIELDS if k in f and f[k].strip()]
        for k in cleared: f[k]=''
        if cleared: log.append(['resources_cleared',cleared])
        sc=scope(nid,obj)
        corpus='AnKing-MCAT' if n['modelName'].startswith('AnKingMCAT') else 'AnKing'
        entries.append({'key':f'source-{nid}','source_nid':nid,'source_model':n['modelName'],'source_tags':n['tags'],
          'source_fields_hash':digest(n['fields']),'fields':f,'copy_changes':log,'objective':obj,'origin':corpus,'scope':sc,
          'deck':DECK_R if sc=='roteiro' else DECK_X,'expected_cards':len(clozes(f['Text'])),
          'high_yield':HY in n['tags'] and corpus=='AnKing','rosa':rosa})
    for key,text,extra,obj in AUTHORED:
        entries.append({'key':'authored-'+key,'source_nid':None,'source_model':None,'source_tags':[],'source_fields_hash':None,
          'fields':{'Text':text,'Extra':extra},'copy_changes':[],'objective':obj,'origin':'Autoral','scope':'roteiro','deck':DECK_R,
          'expected_cards':len(clozes(text)),'high_yield':False,'rosa':False})
    def cards(pred): return sum(e['expected_cards'] for e in entries if pred(e))
    totals={'notes':len(entries),'cards':cards(lambda e:True),
      'by_origin':{o:cards(lambda e,o=o:e['origin']==o) for o in ['AnKing','AnKing-MCAT','Autoral']},
      'by_scope':{s:cards(lambda e,s=s:e['scope']==s) for s in ['roteiro','alem']},
      'rosa':cards(lambda e:e['rosa']),'green':cards(lambda e:e['high_yield'] and not e['rosa']),
      'hy_total':cards(lambda e:e['high_yield'])}
    plan={'lesson_id':LESSON,'base_deck':BASE,'decks':[DECK_R,DECK_X],'profile_evidence':call('getMediaDirPath'),'media':MEDIA,
      'flag_rule':'rosa(5) prevalece sobre verde(3) na cópia nova; HY permanece na tag','entries':entries,'totals':totals}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1),encoding='utf-8')
    print(json.dumps(totals,ensure_ascii=False,indent=1))
if __name__=='__main__': main()
