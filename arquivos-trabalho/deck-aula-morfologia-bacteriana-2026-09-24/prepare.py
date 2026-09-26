import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
ALEM=set(); ALEM_AUTH=set()
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-microbiologia-26-morfologia-estrutura-bacterias'
DECK='NEBLI::UC03::P2::Microbiologia::Morfologia bacteriana'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'Fundamentals of Bacteriology',re.I)
IMG_GRAM='91090a9e85fa950cdf94a715f57d3e7f.webp'
IMG_ZN='5347c2d220767a367e08331944da0e56.jpg'
IMG_FLAGELO='157cb0b8b12e3f596bc231497c97ac56.webp'
IMG_ESPORO='a25758ba80f7879d230abfcec9da73e0.webp'
IMG_CELULA='68fd4ccb45fb0b92417a72354ba3f7b1.jpg'
SLIDE_IMG={}  # preenchido quando o PDF do slide estiver disponível: chave -> arquivo de mídia NEBLI
def img(name,credit=''): return f'<br><br><img src="{name}">'+(f'<br><i><span style="font-size: 10pt;">{credit}</span></i>' if credit else '')
AUTHORED=[
 ('gram-alcool','In the Gram stain, {{c1::alcohol}} washes crystal violet out of gram-negative cells, which then take up the red {{c2::fuchsin}}',
  'Ordem: cristal violeta → lugol (fixa o corante) → álcool (descora) → fucsina ou safranina (contracorante). No Gram-negativo, o álcool dissolve os lipídeos da membrana externa e a camada fina de peptidoglicano não segura o complexo cristal violeta-iodo; no Gram-positivo, a parede espessa retém o roxo.'+img(IMG_GRAM),'P-gram',None),
 ('gram-triagem','A Gram stain gives a fast first split of an isolate into gram-positive or gram-negative {{c1::cocci or bacilli}}, guiding the next tests',
  'É o primeiro passo depois do isolamento: orienta provas bioquímicas, antibiograma, sorologia e PCR. Algumas bactérias, porém, não aparecem no Gram (micobactérias, espiroquetas, <i>Chlamydia</i>, <i>Mycoplasma</i>).','P-gram',None),
 ('ziehl-neelsen','In Ziehl-Neelsen, mycobacteria resist {{c1::acid-alcohol}} decolorization and stay red, while the background takes {{c2::methylene blue}}',
  'Fucsina fenicada aquecida penetra a parede rica em ácido micólico; por resistirem ao álcool-ácido, são chamadas BAAR (bacilos álcool-ácido resistentes). O escarro de fundo fica azul.'+img(IMG_ZN),'C-naocoram',None),
 ('antigenos-ohk','In <i>E. coli</i> serotyping, O antigen sits on the LPS, K antigen on the capsule, and H antigen on the {{c1::flagellum}}',
  'Por isso "antígeno H positivo" indica bactéria móvel (tem flagelo), e "antígeno K positivo" indica cápsula.'+img(IMG_CELULA),'A-antigenos',None),
 ('flagelina','The bacterial flagellum has a basal body, a hook, and a long filament made of {{c1::flagellin}}',
  'O flagelo dá motilidade (quimiotaxia), chegando a 200–500 µm/s. Pili/fímbrias são mais curtos e servem para adesão e conjugação, não para nadar.'+img(IMG_FLAGELO),'D-flagelo',None),
 ('flagelo-arranjo','A single polar flagellum is {{c1::monotrichous}}; flagella spread over the whole cell are {{c2::peritrichous}}',
  'Os outros arranjos da aula: anfitríquio (um flagelo em cada polo) e lofotríquio (um tufo em um polo).','D-flagelo',None),
 ('endosporo','Endospores form when nutrients run out, mostly in gram-positive {{c1::<i>Bacillus</i>}} and {{c2::<i>Clostridium</i>}}',
  'O esporo resiste a calor, seca, radiação e desinfetantes, e germina anos depois em condições boas. Pode ser terminal (ex.: <i>C. tetani</i>), subterminal ou central. Exemplos da aula: <i>B. anthracis</i>, <i>B. cereus</i>, <i>C. tetani</i>, <i>C. botulinum</i>, <i>C. perfringens</i>, <i>C. difficile</i>.'+img(IMG_ESPORO),'D-esporo',None),
 ('tres-dominios','Woese split life into Bacteria, Archaea, and Eukarya by comparing {{c1::16S rRNA}} (ribosomal RNA) sequences',
  'O gene do rRNA é amplificado por PCR, sequenciado e alinhado; quanto menos diferenças, mais próximo o parentesco. As bactérias surgiram há cerca de 3,8 bilhões de anos.','M-dominios',None),
]
ROSA_AUTH={'flagelo-arranjo'}
def digest(v): return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def clozes(v): return sorted({int(x) for x in re.findall(r'{{c(\d+)::',v)})
CLOZE=re.compile(r'\{\{c(\d+)::((?:(?!\}\}).)*?)(?:::((?:(?!\}\}).)*?))?\}\}',re.S)
def uncloze(text,nums): return CLOZE.sub(lambda m: m.group(2) if int(m.group(1)) in nums else m.group(0),text)
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
    return changed
EXTRA_TRIM={}
def entry_from(n,obj,rosa,edits,origin):
    f={k:v['value'] for k,v in n['fields'].items()}
    log=[]
    for e in edits:
        if e[0]=='append': f[e[1]]=(f[e[1]]+'<br>' if f[e[1]].strip() else '')+e[2]
        elif e[0]=='set': f[e[1]]=e[2]
        elif e[0]=='uncloze':
            before=clozes(f['Text']); f['Text']=uncloze(f['Text'],set(e[1]))
            if set(clozes(f['Text']))!=set(before)-set(e[1]): raise RuntimeError(f'Uncloze {n["noteId"]}')
        log.append([e[0],e[1]])
    if n['noteId'] in EXTRA_TRIM: f['Extra']=EXTRA_TRIM[n['noteId']]; log.append(['set','Extra'])
    for k in ('NEBLI_Comentario','NEBLI_Resposta'):
        if f.get(k): f[k]=''; log.append(['cleared',k])
    res=clean_resources(f)
    if res: log.append(['resources_cleared',res])
    hy=HY in n['tags'] and origin=='AnKing'
    return {'key':f'source-{n["noteId"]}','source_nid':n['noteId'],'source_model':n['modelName'],'source_tags':n['tags'],'source_fields_hash':digest(n['fields']),
            'fields':f,'copy_changes':log,'objective':obj,'origin':origin,'expected_cards':len(clozes(f['Text'])),'high_yield':hy,
            'scope':'aula','pink':bool(rosa)}
def main():
    entries=[]; collisions={}
    for group,origin in ((SEL,'AnKing'),(MCAT,'AnKing-MCAT')):
        notes={n['noteId']:n for n in call('notesInfo',notes=list(group))}
        if set(notes)!=set(group): raise RuntimeError(f'Fonte ausente: {set(group)-set(notes)}')
        for nid,(obj,rosa,edits) in group.items():
            found=call('findNotes',query=f'tag:"NEBLI::source::nid-{nid}"')
            if found: collisions[nid]=found
            entries.append(entry_from(notes[nid],obj,rosa,edits,origin))
    for key,text,extra,obj,slide_key in AUTHORED:
        if slide_key and slide_key in SLIDE_IMG: extra+=img(SLIDE_IMG[slide_key],'Fonte: slides da aula de Antibióticos (UC03, Prof. Nilton Lincopan)')
        entries.append({'key':'authored-'+key,'source_nid':None,'source_model':None,'source_tags':[],'source_fields_hash':None,'fields':{'Text':text,'Extra':extra},
                        'copy_changes':[],'objective':obj,'origin':'Autoral','expected_cards':len(clozes(text)),'high_yield':False,
                        'scope':'alem' if key in ALEM_AUTH else 'aula','pink':key in ROSA_AUTH or key in ALEM_AUTH,'slide_image_pending':bool(slide_key and slide_key not in SLIDE_IMG)})
    assoc=[]
    for nid,obj in ASSOCIATE.items():
        n=call('notesInfo',notes=[nid])[0]
        assoc.append({'nid':nid,'objective':obj,'fields_hash':digest(n['fields']),'text':re.sub(r'<[^>]+>',' ',n['fields']['Text']['value'])[:120]})
    t=lambda o: sum(x['expected_cards'] for x in entries if x['origin']==o)
    plan={'lesson_id':LESSON,'target_deck':DECK,'lesson_date':'2026-09-10','profile_evidence':call('getMediaDirPath'),
      'source_manifest':'source-manifest.json','entries':entries,'associate_existing':assoc,'collisions':collisions,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),
                'HY_but_pink':sum(x['expected_cards'] for x in entries if x['high_yield'] and x['pink']),
                'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries if x['scope']=='aula'),
                'alem':sum(x['expected_cards'] for x in entries if x['scope']=='alem')}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'totals':plan['totals'],'collisions':collisions,'pending_slide_images':[e['key'] for e in entries if e.get('slide_image_pending')]},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
