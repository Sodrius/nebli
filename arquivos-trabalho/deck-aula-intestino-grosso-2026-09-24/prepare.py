import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc08-anatomia-02-intestino-grosso-canal-anal'
DECK='NEBLI::UC08::P1::Anatomia::Intestino grosso e canal anal'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula de Intestino grosso e canal anal (UC08, Profa. Patricia Castelucci)'
IMGS=['tenias', 'apendice-posicao', 'labios', 'reto-sem-tenias', 'puborretal', 'pectinada', 'esfincteres', 'seios', 'escavacao', 'mcburney']
MEDIA=[(f'img/nebli-intgrosso-{k}.png',f'nebli-intgrosso-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-intgrosso-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('intg-tenias','The three taeniae coli, bands of longitudinal muscle, are the mesocolic, omental and {{c1::free}} taenia',
  'Mesocólica: na borda de inserção do mesocolo; omental: onde se prende o omento maior no colo transverso; livre: sem inserção. Vão do ceco até o início do reto; como são mais curtas que a parede, formam os haustros (saculações).','C-caracteristicas','tenias'),
 ('intg-apendice','The vermiform appendix (6–10 cm, rich in lymphoid tissue) most often lies in a {{c1::retrocecal}} position',
  'Na aula: retrocecal ~64%, pélvico ~34%, pré e pós-ileal raros. As três tênias convergem na base do apêndice.','I-apendice','apendice-posicao'),
 ('intg-labios','The ileocecal valve is formed by the ileocecal and {{c1::ileocolic}} lips around the ileal orifice (ileal papilla)',
  'A papila ileal é a projeção do íleo terminal dentro do ceco. Abaixo dela fica o óstio do apêndice.','I-ileocecal','labios'),
 ('intg-reto','Unlike the colon, the rectum has no {{c1::taeniae, haustra or epiploic appendages}}',
  'O reto (~15 cm) vai do colo sigmoide ao canal anal, com flexura sacral, pregas transversas e ampola retal.','R-reto','reto-sem-tenias'),
 ('intg-puborretal','The {{c1::puborectalis}} sling pulls the anorectal junction forward, creating the anorectal flexure that helps keep continence',
  'Na defecação o puborretal relaxa e a junção anorretal se retifica. Faz parte do músculo levantador do ânus.','R-reto','puborretal'),
 ('intg-escavacao','In men the rectum is separated from the bladder by the {{c1::rectovesical}} pouch; in women, from the uterus by the rectouterine pouch',
  'São os pontos mais baixos da cavidade peritoneal em cada sexo, onde líquido e pus se acumulam.','R-reto','escavacao'),
 ('intg-pectinada','The pectinate line separates the endoderm-derived upper anal canal from the {{c1::ectoderm}}-derived lower canal',
  'Acima: inervação visceral, drenagem para linfonodos ilíacos internos, vasos retais superiores. Abaixo: inervação parietal (somática), linfonodos inguinais, vasos retais inferiores.','A-pectinada','pectinada'),
 ('intg-seios','The small mucus-secreting recesses between the anal columns are the anal {{c1::sinuses}}, closed below by the anal valves',
  'As colunas anais contêm ramos dos vasos retais superiores (plexo venoso interno). A linha branca (anocutânea) fica abaixo da pectinada.','A-canal','seios'),
 ('intg-esfincteres','The internal anal sphincter is {{c1::smooth}} muscle (involuntary), while the external anal sphincter is skeletal muscle (voluntary)',
  'O interno é o espessamento da camada circular do reto. O externo trabalha com o puborretal/levantador do ânus. Funções do canal anal: continência, retenção e expulsão do bolo fecal.','A-canal','esfincteres'),
 ('intg-mcburney','McBurney\u2019s point, the surface projection of the appendix base, lies one-third of the way from the {{c1::anterior superior iliac spine}} to the umbilicus',
  'Na apendicite, a dor periumbilical migra para esse ponto na fossa ilíaca direita.','I-apendice','mcburney'),
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
        elif e[0]=='anato':
            imgs=re.findall(r'<img[^>]+>',f.get('Cadaver','') or f.get('Illustration','') or f.get('Model','') or f.get('Imaging',''))
            if not imgs: raise RuntimeError(f'Sem imagem AnatoKing {n["noteId"]}')
            f={k:('Identify the highlighted structure' if k=='Header' else imgs[0] if k=='Cadaver' else f[k] if k=='Text' else '') for k in f}
        elif e[0]=='resub':
            new=re.sub(e[2],e[3],f[e[1]],flags=re.S)
            if new==f[e[1]]: raise RuntimeError(f'resub sem efeito {n["noteId"]}')
            f[e[1]]=new
        elif e[0]=='uncloze':
            before=clozes(f['Text']); f['Text']=uncloze(f['Text'],set(e[1]))
            if set(clozes(f['Text']))!=set(before)-set(e[1]): raise RuntimeError(f'Uncloze {n["noteId"]}')
        log.append(list(e[:2]))
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-08-10','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
