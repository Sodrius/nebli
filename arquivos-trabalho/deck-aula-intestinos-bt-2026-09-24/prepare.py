import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc08-biologia-tecidual-04-intestinos'
DECK='NEBLI::UC08::P1::Biologia Tecidual::Intestinos'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula de Intestinos (UC08, Profa. Patrícia Gama)'
IMGS=['plica-vilo', 'nicho', 'linhagens', 'wnt-bmp', 'ki67-tunel', 'celulas', 'lacteo', 'dcs']
MEDIA=[(f'img/nebli-intestinos-{k}.png',f'nebli-intestinos-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-intestinos-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('bt4-plica','Plicae circulares are folds of mucosa plus {{c1::submucosa}}, whereas villi are projections of the mucosa only',
  'Três níveis de aumento de superfície: plica (mucosa + submucosa) > vilo (mucosa) > microvilo (membrana do enterócito). As criptas de Lieberkühn abrem-se entre os vilos.','E-superficie','plica-vilo'),
 ('bt4-lgr5','Actively cycling crypt base columnar stem cells are marked by {{c1::Lgr5}} (with Ascl2 and Olfm4)',
  'Na posição +4 ficam células-tronco de reserva, mais quiescentes (Bmi1, Hopx, Tert), que repõem as Lgr5+ após lesão.','N-nicho','nicho'),
 ('bt4-ta','Stem cell daughters first divide in the crypt as {{c1::transit-amplifying}} progenitors, then differentiate as they migrate up the villus',
  'Duas linhagens: absortiva (enterócitos) e secretora (caliciformes, enteroendócrinas, Paneth). As Paneth são a exceção: descem para a base da cripta.','N-nicho','linhagens'),
 ('bt4-wnt','High {{c1::Wnt}} signaling at the crypt base keeps stem cells proliferating, while BMP toward the villus drives differentiation',
  'O gradiente vem do mesênquima em volta da cripta (telócitos, fibroblastos). É o eixo cripta–vilo da aula.','N-nicho','wnt-bmp'),
 ('bt4-ki67','In the small intestine, Ki67 marks proliferating cells in the {{c1::crypts}}, while TUNEL marks apoptotic cells at the villus tip',
  'O epitélio se renova em poucos dias: nasce na cripta, sobe pelo vilo e é eliminado no ápice.','N-nicho','ki67-tunel'),
 ('bt4-paneth','Besides secreting lysozyme and antimicrobial peptides, Paneth cells form the {{c1::niche}} that supports Lgr5+ stem cells',
  'Ficam intercaladas com as células-tronco na base da cripta, com grânulos eosinofílicos apicais.','C-celulas','celulas'),
 ('bt4-vilina','The enterocyte brush border carries lactase and sucrase and is built on actin bundled by {{c1::villin}}',
  'Caliciforme: mucina 2 (MUC2). Enteroendócrina: hormônios que regulam digestão, metabolismo e apetite. Paneth: lisozima e peptídeos antimicrobianos.','C-celulas','celulas'),
 ('bt4-lacteo','The core of each villus holds a blind lymphatic capillary, the {{c1::central lacteal}}, which takes up chylomicrons',
  'Ao lado: capilares sanguíneos fenestrados (monossacarídeos e aminoácidos vão à veia porta), músculo liso e células imunes da lâmina própria.','E-superficie','lacteo'),
 ('bt4-dcs','In colonic crypts, deep crypt secretory cells play the role that {{c1::Paneth cells}} play in the small intestine, supporting stem cells',
  'O nicho colônico também recebe sinais da imunidade tecidual (IL-13 de ILC2).','G-grosso','dcs'),
]
ROSA_AUTH={'bt4-dcs'}
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
        elif e[0]=='imgsonly': f[e[1]]='<br>'.join(re.findall(r'<img[^>]+>',f[e[1]]))
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-08-24','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
