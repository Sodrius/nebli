import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,OTHER,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-patologia-19-correlacao-patologica-radiologica-2'
DECK='NEBLI::UC03::P2::Patologia::Correlação patológica-radiológica 2'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
MEDIA=[]  # imagens já estão na coleção (cards AnKing); o slide não estava acessível
W='https://commons.wikimedia.org/wiki/File:'
IMG={'tc':('8bcfada6bbfe592e31486a23cd5c768c.webp',f'<a href="{W}LiverhemangiomaCT.PNG">James Heilman, MD</a>, CC BY-SA 3.0, via Wikimedia Commons'),
     'hist':('77c0229eed4796d32c798e34d593a64c.png','Nephron, CC BY-SA 3.0, via Wikimedia Commons'),
     'gordura':('2554698852d236c774a7dae9cce183c8.png',f'<a href="{W}Fatty_change_liver_-_Lipid_steatosis_10X.jpg">Calicut Medical College</a>, CC BY-SA 4.0, via Wikimedia Commons'),
     'tricromico':('0c57b029bcd91b6657833be2acf8aa76.png',f'<a href="{W}Trichrome_stain_of_chronic_alcoholic_cirrhosis.jpg">Mikael Häggström, M.D.</a>, CC0, via Wikimedia Commons'),
     'irrigacao':('ec11a021716f4a67bec7a88ac05b7b2a.webp','AnkiHub, LLC (ilustração)'),
     'chc':('9e92240f61b59d2446515d76e95f1e73.png',f'<a href="{W}Hepatocellular_carcinoma_1.jpg">See page for author</a>, Public domain, via Wikimedia Commons')}
def img(k):
    f,c=IMG[k]; return f'<br><br><img src="{f}"><br><i><span style="font-size: 10pt;">Photo credit: {c}</span></i>'
AUTHORED=[
 ('crp2-hemangioma-us','On ultrasound, a hepatic cavernous hemangioma is typically a well-defined, homogeneous {{c1::hyperechoic}} nodule',
  'Cada interface entre sangue e septo fibroso reflete o som, e a lesão tem milhares delas. É o achado incidental típico: mulher jovem e assintomática, como no caso 1.','H-imagem','hist'),
 ('crp2-hemangioma-tc','Triphasic CT of hepatic hemangioma: {{c1::peripheral nodular, discontinuous}} arterial enhancement, then {{c2::centripetal}} fill-in',
  'Na fase de equilíbrio a lesão está toda preenchida e retém o contraste, porque o sangue anda devagar nos lagos vasculares. Não faz washout.','H-imagem','tc'),
 ('crp2-fase-portal','The normal liver parenchyma enhances most in the {{c1::portal venous}} phase of contrast CT',
  'Cerca de 75% do sangue hepático chega pela veia porta, uns 30 s depois da onda arterial. Na fase arterial só chegou o quarto que vem pela artéria hepática.','N-imagem','irrigacao'),
 ('crp2-chc-washout','Hepatocellular carcinoma on multiphase CT: arterial {{c1::hyperenhancement}}, followed by {{c2::washout}} in later phases',
  'Ao virar carcinoma, o nódulo perde o suprimento portal e passa a ser nutrido por neovasos arteriais. Em fígado cirrótico, esse padrão num nódulo acima de 1 cm dispensa biópsia.','T-chc','chc'),
 ('crp2-esteatose-tc','On non-contrast CT, a fatty liver looks {{c1::hypodense}} (darker) relative to the spleen',
  'O normal é o contrário: fígado mais denso que o baço. A gordura (~−100 UH) puxa a densidade hepática para baixo; quanto mais gordura, maior a queda.','E-imagem',None),
 ('crp2-esteatose-us','Hepatic steatosis on ultrasound: diffusely {{c1::increased echogenicity}}, brighter than the renal cortex',
  'As gotículas de gordura multiplicam as interfaces refletoras. O som se gasta na entrada, e o fundo do fígado fica apagado (atenuação posterior).','E-imagem','gordura'),
 ('crp2-micronodular','Alcoholic cirrhosis is classically {{c1::micronodular}}: small, uniform nodules under 3 mm',
  'Nódulos maiores e desiguais (macronodular) lembram hepatite viral, com necrose em surtos. O padrão orienta, mas muda com os anos.','C-cirrose','tricromico'),
 ('crp2-colestase','A greenish cirrhotic liver at autopsy reflects retained {{c1::bile}} (intrahepatic cholestasis), not necrosis',
  'O hepatócito comprimido e mal perfundido não consegue excretar a bilirrubina conjugada, que se acumula na célula e nos canalículos.','C-cirrose',None),
 ('crp2-cirrose-tc','On CT, a cirrhotic liver shows an irregular, {{c1::nodular}} surface contour',
  'Os nódulos de regeneração empurram a cápsula. Na hipertensão portal somam-se esplenomegalia, ascite e colaterais tortuosas (hilo esplênico, esôfago distal, parede abdominal).','P-hipertensao',None),
]
ROSA_AUTH={'crp2-colestase'}
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
    for group,origin in ((SEL,'AnKing'),(OTHER,'Lightyear'),(MCAT,'AnKing-MCAT')):
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
        assoc.append({'nid':nid,'objective':obj,'fields_hash':digest(n['fields']),'text':re.sub(r'<[^>]+>',' ',next(iter(n['fields'].values()))['value'])[:120]})
    t=lambda o: sum(x['expected_cards'] for x in entries if x['origin']==o)
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-01','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'Lightyear':t('Lightyear'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
