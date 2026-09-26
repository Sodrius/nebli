import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc08-fisiologia-08-motilidade-absorcao-intestinal-i'
DECK='NEBLI::UC08::P1::Fisiologia::Motilidade e absorção intestinal I'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula Motilidade do TGI (UC08, Profa. Fran Goulart da Silva)'
IMGS=['inervacao','reflexos','tonica-fasica','contracao']
MEDIA=[(f'img/nebli-motil-{k}.png',f'nebli-motil-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-motil-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('motil1-ach-vip','In the enteric plexuses, excitatory motor neurons release {{c1::acetylcholine}}, while inhibitory ones release VIP and NO',
  'Outros neuromediadores citados na aula: serotonina, catecolaminas, ATP e GABA. O neurônio sensorial detecta a distensão (mecanorreceptores) e fecha o reflexo.','I-neurotransmissores','reflexos'),
 ('motil1-reflexos','A gut reflex confined to the enteric plexuses is a {{c1::short (intramural)}} reflex; one routed through the brainstem via the vagus is a long reflex',
  'Reflexo longo = vago-vagal: aferente e eferente no nervo vago, integração no tronco encefálico. Os dois tipos se integram para contrair e relaxar o tubo.','I-reflexos','reflexos'),
 ('motil1-sna','Parasympathetic input generally {{c1::stimulates}} GI motility and secretion, whereas sympathetic input inhibits them',
  'Inervação extrínseca = SNA (parassimpático pelo vago e nervos pélvicos; simpático). Intrínseca = SNE: plexo submucoso (secreção) e mioentérico (motilidade).','I-extrinseca','inervacao'),
 ('motil1-chagas','<i>Trypanosoma cruzi</i> destroys the {{c1::myenteric}} plexus, so the gut dilates, mainly as megaesophagus and megacolon',
  'Sem os neurônios inibitórios (VIP/NO), o esfíncter não relaxa e o segmento acima não tem peristalse coordenada: o tubo dilata.','I-chagas','reflexos'),
 ('motil1-esfincter','Distension of the tube ahead of a bolus makes the downstream {{c1::sphincter relax}}',
  'Esfíncteres (EES, EEI, piloro, ileocecal, anais) têm contração tônica e só abrem quando o conteúdo chega. No piloro: o antro manda relaxar (regulação anterógrada) e o duodeno manda contrair (retrógrada).','C-padroes','tonica-fasica'),
 ('motil1-fasica','Contractions with rapid contract–relax cycles, as in peristalsis, are {{c1::phasic}}; sustained ones, as in sphincters, are tonic',
  'Fásica: esôfago, antro, intestino delgado. Tônica: esfíncteres, fundo gástrico, porção proximal do estômago.','C-padroes','tonica-fasica'),
 ('motil1-relaxamento','Smooth muscle relaxes when {{c1::myosin light-chain phosphatase}} removes the phosphate from myosin',
  'Relaxar também exige retirar o Ca²⁺ do citosol: Ca²⁺-ATPase da membrana e do retículo sarcoplasmático e trocadores. Contração: Ca²⁺-calmodulina ativa a MLCK.','C-contracao','contracao'),
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-14','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
