import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-grand-round-21-grand-round-2-diabetes'
DECK='NEBLI::UC03::P2::Grand Round::Grand Round 2 (diabetes mellitus)'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides do Grand Round 2 — Diabetes mellitus (UC03)'
IMGS=['glicacao','rage','nefro-us','calcio','angiotc','charcot','dm1']
MEDIA=[(f'img/nebli-gr2-{k}.png',f'nebli-gr2-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-gr2-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('gr2-ages','Persistent hyperglycemia glycates proteins without enzymes: reversible Schiff bases become Amadori products and finally irreversible {{c1::advanced glycation end products (AGEs)}}',
  'É a base da maioria das complicações crônicas. AGEs no colágeno dificultam a cicatrização; LDL glicada é captada mais facilmente (aterosclerose); AGEs inativam o óxido nítrico e resistem à degradação proteica.','C-age','glicacao'),
 ('gr2-rage','AGEs binding their receptor {{c1::RAGE}} on monocytes and mesenchymal cells trigger cytokines, vascular leak and a procoagulant state',
  'Na aula: migração de monócitos, secreção de citocinas e fatores de crescimento, aumento da permeabilidade vascular, da atividade pró-coagulante, da proliferação celular e da matriz extracelular.','C-age','rage'),
 ('gr2-frutosamina','{{c1::Fructosamine}} (glycated albumin) reflects mean glucose over the last 2–3 weeks, a shorter window than HbA1c',
  'A HbA1c reflete cerca de 3 meses. A frutosamina serve quando a HbA1c pode estar falseada (hemoglobinopatias, hemólise) e para ver a resposta rápida ao tratamento, como no caso da aula (575 → 289 µmol/L).','L-exames','glicacao'),
 ('gr2-lada','Diabetes starting in an adult, with positive anti-GAD65 and still-detectable C-peptide, is autoimmune {{c1::LADA}} (latent type 1)',
  'Caso da aula: homem de 26 anos, IMC normal, poliúria/polidipsia, anti-GAD65 muito alto e peptídeo C ainda no normal (reserva de célula β). Tratado com insulina basal + bolus por contagem de carboidratos.','L-exames','dm1'),
 ('gr2-nefro-us','On ultrasound, diabetic kidneys are {{c1::enlarged}} early (hyperfiltration) and shrunken with a thin, echogenic cortex at end stage',
  'No estágio final perde-se também a diferenciação córtico-medular. Na histologia: espessamento da membrana basal, expansão mesangial e glomeruloesclerose.','R-nefro','nefro-us'),
 ('gr2-calcio','The coronary calcium score uses non-contrast, ECG-gated CT to quantify {{c1::calcified plaque}} and stratify risk in asymptomatic people',
  'Calcificação = área acima de 130 UH; o método de Agatston é a referência. Detecta aterosclerose subclínica, que tem longa fase assintomática.','R-coronarias','calcio'),
 ('gr2-angiotc','Coronary CT angiography has a negative predictive value near 100%, so it is best used to {{c1::rule out}} CAD in low- or intermediate-probability patients',
  'Usa contraste e radiação e quantifica mal as estenoses; lesão grave vai para o cateterismo. O cateterismo (angiocoronariografia invasiva) é o padrão-ouro e permite tratar.','R-coronarias','angiotc'),
 ('gr2-charcot','Diabetic neuropathy removes pain and proprioception, so repeated unnoticed trauma progressively destroys joints: {{c1::Charcot arthropathy}}',
  'Na radiografia: destruição e erosão articular, reabsorção óssea, osteófitos e esclerose desorganizada, típicas do médio e retropé. Diferencial com osteomielite (infecção da medular óssea), vista melhor na RM.','R-charcot','charcot'),
]
ROSA_AUTH=set()
def digest(v): return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def clozes(v): return sorted({int(x) for x in re.findall(r'{{c(\d+)::',v)})
CLOZE=re.compile(r'\{\{c(\d+)::((?:(?!\}\}).)*?)(?:::((?:(?!\}\}).)*?))?\}\}',re.S)
def uncloze(text,nums): return CLOZE.sub(lambda m: m.group(2) if int(m.group(1)) in nums else m.group(0),text)
KHAN=re.compile(r'(<br>\s*)*<a[^>]*khanacademy[^>]*>.*?</a>|Khan Academy Link',re.I|re.S)
def clean_resources(f):
    changed=[]
    for k in RESOURCE_FIELDS:
        v=f.get(k,'')
        if not v.strip(): continue
        if k=='Bootcamp':
            parts=[p for p in re.split(r'(?:\s*<br>\s*)+',v) if p.strip()]
            new='<br>'.join(p for p in parts if ON_TOPIC.search(p))
        else: new=''
        if new!=v: f[k]=new; changed.append(k)
    if 'Extra' in f and KHAN.search(f['Extra']): f['Extra']=KHAN.sub('',f['Extra']).rstrip(); changed.append('Extra:khan')
    return changed
def entry_from(n,obj,rosa,edits,origin):
    f={k:v['value'] for k,v in n['fields'].items()}
    log=[]
    for e in edits:
        if e[0]=='append': f[e[1]]=(f[e[1]]+'<br><br>' if f[e[1]].strip() else '')+e[2]
        elif e[0]=='set': f[e[1]]=e[2]
        elif e[0]=='resub':
            new=re.sub(e[2],e[3],f[e[1]],flags=re.S)
            if new==f[e[1]]: raise RuntimeError(f'resub sem efeito {n["noteId"]}')
            f[e[1]]=new
        elif e[0]=='uncloze':
            before=clozes(f['Text']); f['Text']=uncloze(f['Text'],set(e[1]))
            if set(clozes(f['Text']))!=set(before)-set(e[1]): raise RuntimeError(f'Uncloze {n["noteId"]}')
        log.append([e[0],e[1]])
    res=clean_resources(f)
    if res: log.append(['resources_cleared',res])
    hy=HY in n['tags'] and origin=='AnKing'
    return {'key':f'source-{n["noteId"]}','source_nid':n['noteId'],'source_model':n['modelName'],'source_tags':n['tags'],'source_fields_hash':digest(n['fields']),
            'fields':f,'copy_changes':log,'objective':obj,'origin':origin,'expected_cards':len(clozes(f['Text'])),'high_yield':hy,'scope':'aula','pink':bool(rosa)}
def main():
    entries=[]
    for group,origin in ((SEL,'AnKing'),(MCAT,'AnKing-MCAT')):
        notes={n['noteId']:n for n in call('notesInfo',notes=list(group))}
        if set(notes)!=set(group): raise RuntimeError(f'Fonte ausente: {set(group)-set(notes)}')
        for nid,(obj,rosa,edits) in group.items():
            found=call('findNotes',query=f'tag:"NEBLI::source::nid-{nid}"')
            if found: ASSOCIATE[found[0]]=obj; continue
            entries.append(entry_from(notes[nid],obj,rosa,edits,origin))
    for key,text,extra,obj,ik in AUTHORED:
        entries.append({'key':'authored-'+key,'source_nid':None,'source_model':None,'source_tags':[],'source_fields_hash':None,'fields':{'Text':text,'Extra':extra+(img(ik) if ik else '')},
                        'copy_changes':[],'objective':obj,'origin':'Autoral','expected_cards':len(clozes(text)),'high_yield':False,'scope':'aula','pink':key in ROSA_AUTH})
    assoc=[]
    for nid,obj in ASSOCIATE.items():
        n=call('notesInfo',notes=[nid])[0]
        assoc.append({'nid':nid,'objective':obj,'fields_hash':digest(n['fields']),'text':re.sub(r'<[^>]+>',' ',n['fields']['Text']['value'])[:120]})
    t=lambda o: sum(x['expected_cards'] for x in entries if x['origin']==o)
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-29','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
