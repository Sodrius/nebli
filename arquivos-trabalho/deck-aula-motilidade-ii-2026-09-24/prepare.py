import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc08-fisiologia-09-motilidade-absorcao-intestinal-ii'
DECK='NEBLI::UC08::P1::Fisiologia::Motilidade e absorção intestinal II'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula Motilidade do TGI (UC08, Profa. Fran Goulart da Silva)'
IMGS=['ondas-lentas','degluticao','esvaziamento','delgado','colon','evacuacao','vomito']
MEDIA=[(f'img/nebli-motil-{k}.png',f'nebli-motil-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-motil-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('motil2-picos','Slow waves alone do not contract GI smooth muscle; contraction needs {{c1::spike potentials}} on their crests',
  'Quanto mais potenciais em pico na crista da onda, mais Ca²⁺ entra e mais forte a contração. A distensão e o SNE/SNA aumentam a amplitude das ondas lentas até o limiar. As ondas lentas dependem de canais catiônicos, não dos canais de Ca²⁺ tipo L.','E-ondas','ondas-lentas'),
 ('motil2-voluntaria','Swallowing begins with a {{c1::voluntary}} oral phase; the pharyngeal and esophageal phases are reflexes coordinated by the brainstem',
  'Na fase faríngea: sobe o palato mole, a laringe se fecha, a respiração é suprimida, o EES relaxa e começa a peristalse primária. O EEI e o fundo gástrico relaxam antes do bolo chegar.','D-degluticao','degluticao'),
 ('motil2-secundaria','Food left in the esophagus after a swallow is cleared by {{c1::secondary}} peristalsis, triggered by local distension',
  'A primária faz parte do reflexo da deglutição; a secundária não depende de nova deglutição, nasce da distensão do próprio esôfago (SNE + vago).','D-degluticao','degluticao'),
 ('motil2-retropropulsao','The antral contraction pushes chyme against a nearly closed pylorus; this {{c1::retropulsion}} grinds and mixes it',
  'Só uma pequena fração passa ao duodeno a cada onda. Ácido e nutrientes no duodeno liberam secretina, CCK e GIP, que contraem o piloro e relaxam o estômago: o esvaziamento acompanha a capacidade do duodeno.','G-esvaziamento','esvaziamento'),
 ('motil2-transito','Transit takes about {{c1::2–4 hours}} through the small intestine but up to 48 hours through the colon',
  'Delgado: segmentações (mistura) e peristalses curtas (propulsão), estimuladas por SNE, SNA, CCK e insulina. Cólon: haustrações e movimentos de massa.','T-delgado','delgado'),
 ('motil2-haustracoes','Slow {{c1::haustral}} contractions mix colonic contents, giving time for water and electrolyte absorption in the proximal colon',
  'A capacidade de absorver água é limitada. O cólon distal compacta e lubrifica as fezes.','T-colon','colon'),
 ('motil2-massa','A few times a day, {{c1::mass movements}} push feces into the rectum, often after a meal (gastrocolic reflex)',
  'O reflexo gastrocólico é mediado pelo SNA, CCK e gastrina. A distensão do reto dispara o reflexo da evacuação.','T-colon','colon'),
 ('motil2-evacuacao','Rectal distension triggers a spinal (S1–S4) reflex that relaxes the {{c1::internal}} anal sphincter, while the external sphincter relaxes voluntarily',
  'Aferência sensorial e eferência parassimpática pelo nervo pélvico. Na defecação, relaxam também o puborretal (voluntário) e contraem-se os músculos abdominais e respiratórios.','T-evacuacao','evacuacao'),
 ('motil2-vomito','In vomiting, deep inspiration and strong {{c1::abdominal muscle contraction}} raise intra-abdominal pressure while sphincters relax',
  'Estímulos: área postrema (fármacos, toxinas, quimioterapia), córtex e sistema límbico, sistema vestibular, distensão gástrica. O integrador fica no tronco; antes vem a salivação e há contração reversa do intestino proximal.','V-vomito','vomito'),
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-28','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
