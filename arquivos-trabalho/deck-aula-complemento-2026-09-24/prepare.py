import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-imunologia-31-sistema-complemento'
DECK='NEBLI::UC03::P2::Imunologia::Sistema complemento'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula de Sistema complemento (UC03)'
IMGS=['c1q', 'alternativa', 'properdina', 'lectinas', 'receptores', 'fatores-ih', 'cd59', 'deficiencias']
MEDIA=[(f'img/nebli-complemento-{k}.png',f'nebli-complemento-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-complemento-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('comp-c1q','To start the classical pathway, C1q must bind at least {{c1::two}} antigen-bound IgG molecules (or a single pentameric IgM)',
  'C1q ativa C1r, que ativa C1s; C1s cliva C4 e C2 e forma a C3 convertase clássica (C4b2a na aula). Ig: IgG pela região CH2, IgM pela CH3.','V-classica','c1q'),
 ('comp-tickover','The alternative pathway starts with slow spontaneous hydrolysis of C3 into {{c1::C3(H2O)}}, which binds factor B for factor D to cleave',
  'Forma-se C3(H2O)Bb, uma convertase em fase fluida que gera os primeiros C3b. O C3b que cai numa superfície de micróbio (sem reguladores) amplifica a via: C3bBb.','V-alternativa','alternativa'),
 ('comp-properdina','{{c1::Properdin}} stabilizes the alternative-pathway C3 convertase (C3bBb) on microbial surfaces',
  'É o único regulador positivo do complemento. Deficiência de properdina, como de C3, fator D, H e I, aparece na aula entre as deficiências da via alternativa (infecções por Neisseria, pneumococo e Haemophilus).','V-alternativa','properdina'),
 ('comp-masp','In the lectin pathway, mannose-binding lectin bound to microbial sugars activates {{c1::MASP-1/MASP-2}}, which cleave C4 and C2 as C1s does',
  'A MBL é estruturalmente parecida com C1q. Reconhece manose e N-acetilglicosamina na superfície dos patógenos, sem anticorpo.','V-lectinas','lectinas'),
 ('comp-fatores-ih','Factor {{c1::I}} inactivates C3b (to iC3b, then C3dg), using factor H as its cofactor',
  'O mesmo sistema degrada C4b (C4c + C4d). Deficiência de fator H ou I deixa a via alternativa sem freio: consumo de C3, infecções piogênicas e doenças por imunocomplexos (glomerulonefrite, SHU atípica).','R-regulacao','fatores-ih'),
 ('comp-cd59','CD59 protects host cells by preventing {{c1::C9 polymerization}}, so the membrane attack complex cannot form',
  'Ancorado por GPI, como o DAF (CD55). Sem os dois, as hemácias sofrem lise pelo complemento: hemoglobinúria paroxística noturna.','R-regulacao','cd59'),
 ('comp-cr3','iC3b-coated microbes are phagocytosed through {{c1::CR3 (CD11b/CD18)}} and CR4 on phagocytes',
  'CR1 (CD35) liga C3b/C4b: fagocitose, transporte de imunocomplexos pelas hemácias até fígado e baço e cofator do fator I. CR2 (CD21) liga C3d e é correceptor do linfócito B.','F-opsonizacao','receptores'),
 ('comp-c3','C3 deficiency, which affects both classical and alternative pathways, causes severe recurrent {{c1::pyogenic}} infections and immune-complex disease',
  'Sem C3 não há opsonização por C3b, nem convertase C5, nem MAC. Nas questões da UC: criança com infecções bacterianas de repetição e C3 baixo; C3 baixo com síntese normal sugere consumo (falta de fator H ou I).','D-deficiencias','deficiencias'),
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-08','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
