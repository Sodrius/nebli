import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-patologia-24-patologia-ambiental'
DECK='NEBLI::UC03::P2::Patologia::Patologia ambiental'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula de Patologia ambiental (UC03, Prof. Luiz Fernando Ferraz da Silva)'
IMGS=['particulado', 'primarios', 'londres', 'iceberg', 'oms', 'mecanismos-sistemicos', 'ldl', 'biomassa']
MEDIA=[(f'img/nebli-ambiental-{k}.png',f'nebli-ambiental-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-ambiental-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('amb-particulado','Particulate matter is classed by aerodynamic diameter (PM10, PM2.5, ultrafine); the smaller the particle, the {{c1::deeper}} it reaches in the airways',
  'Partículas grandes param por impactação nas vias altas; as médias sedimentam nos brônquios; as ultrafinas chegam ao alvéolo por difusão (movimento browniano). Composição: nitratos, sulfatos, metais e HPA. Fontes: solo, vulcões e florestas; transporte, indústria e combustão incompleta.','P-particulado','particulado'),
 ('amb-secundario','Ozone is a {{c1::secondary}} pollutant: it forms in the air from NOx and hydrocarbons under sunlight, rather than being emitted directly',
  'Primários (emitidos pela fonte): material particulado, CO, NOx, SO₂, HPA, metais. Secundários (formados na atmosfera): O₃, H₂SO₄ e sulfatos de amônio.','P-poluentes','primarios'),
 ('amb-londres','The London fog of December 1952 killed about 4,000 people in one week, proof that {{c1::air pollution}} can kill acutely',
  'Mais de 8.000 em três semanas. As mortes subiram junto com a concentração de fumaça, dia a dia (Logan, Lancet 1953).','H-historia','londres'),
 ('amb-iceberg','Health effects of pollution form a pyramid: deaths at the top, then admissions and visits, and {{c1::subclinical inflammation}} in most exposed people at the base',
  'Quanto mais grave o desfecho, menos pessoas afetadas. Medir só mortalidade subestima o problema.','H-efeitos','iceberg'),
 ('amb-oms','São Paulo\u2019s mean PM2.5 (~28 µg/m³) is well above the WHO annual guideline, which was {{c1::10 µg/m³}} (tightened to 5 in 2021)',
  'Na aula: outras metrópoles brasileiras com 16 e 20 µg/m³. Nos EUA, a mortalidade ajustada sobe linearmente com o PM2.5 (Pope, 2000), sem limiar seguro evidente.','H-megacidades','oms'),
 ('amb-sistemico','Inhaled particles cause oxidative stress and lung inflammation that spill into the blood, causing endothelial dysfunction, platelet activation and {{c1::plaque instability}}',
  'Daí o aumento de infarto e AVC nos dias de poluição alta. Partículas ultrafinas também podem atravessar a barreira epitelial e chegar à circulação.','S-sistemico','mecanismos-sistemicos'),
 ('amb-ldl','In animal studies, polluted air increased {{c1::LDL oxidation}} and atherosclerotic plaque thickness without raising the plaque lipid content',
  'Também aumentou autoanticorpos contra LDL oxidada. É o elo entre poluição e doença coronariana.','S-aterosclerose','ldl'),
 ('amb-biomassa','Biomass smoke (e.g., indoor wood stoves) impairs {{c1::mucociliary clearance}} and alveolar macrophage activity, favoring respiratory infections',
  'Também: irritação química (olhos, coriza), menos antioxidantes, reações oxidativas, IL-6 e IL-8 elevadas com recrutamento de granulócitos, inflamação crônica, sibilância e queda da função pulmonar (DPOC). Gases indoor: CO, metano, NO₂.','M-biomassa','biomassa'),
]
ROSA_AUTH={'amb-londres','amb-oms'}
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-03','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
