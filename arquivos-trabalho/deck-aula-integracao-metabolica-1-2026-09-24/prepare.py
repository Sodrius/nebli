import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-bioquimica-25-integracao-metabolica-i'
DECK='NEBLI::UC03::P2::Bioquímica::Integração metabólica I'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula de Integração metabólica I (UC03)'
IMGS=['reservas','glut2','irreversiveis','musculo-epinefrina','cori','coracao','cerebro','porta','aminoacidos']
MEDIA=[(f'img/nebli-integ1-{k}.png',f'nebli-integ1-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-integ1-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('integ1-reservas','By far the body’s largest energy reserve is {{c1::triacylglycerol in adipose tissue}}; muscle holds the largest store of mobilizable protein',
  'Tabela de Cahill (kcal): tecido adiposo ~135.000 em TAG; músculo ~24.000 em proteína e ~1.200 em glicogênio; fígado ~400 em glicogênio. O glicogênio muscular é maior que o hepático, mas serve só ao próprio músculo.','R-reservas','reservas'),
 ('integ1-glut2','Liver GLUT2 has a high K<sub>m</sub> (~15–25 mM), so glucose inside the hepatocyte simply tracks {{c1::blood glucose}}',
  'GLUT1, 3 e 4 têm K<sub>m</sub> baixo (2–4 mM, alta afinidade); o GLUT4 depende de insulina. Com GLUT2 + glicoquinase (K<sub>m</sub> alto), o fígado só retém glicose quando ela está alta e a libera na hipoglicemia.','T-glut','glut2'),
 ('integ1-irreversiveis','Glycolysis and gluconeogenesis are controlled at their {{c1::irreversible}} steps, such as PFK-1 versus fructose-1,6-bisphosphatase',
  'Outros pares: piruvato quinase × piruvato carboxilase/PEPCK. As duas vias não podem correr juntas; a frutose-2,6-bisfosfato ativa a PFK-1 e inibe a frutose-1,6-bisfosfatase.','F-glicolise','irreversiveis'),
 ('integ1-musculo-epinefrina','Muscle glycogen breakdown is driven by {{c1::epinephrine}}, Ca<sup>2+</sup> and AMP, not by glucagon',
  'O músculo responde à sua demanda de energia; hormônios que o regulam: epinefrina (degradação) e insulina (síntese). A fosforilase muscular é ativada por AMP e inibida por ATP e glicose-6-fosfato; a hepática responde à glicose e ao glucagon.','M-glicogenio','musculo-epinefrina'),
 ('integ1-cori','In the Cori cycle, {{c1::lactate}} released by muscle and red cells is turned back into glucose by the liver',
  'O fígado gasta ATP na gliconeogênese para reciclar o lactato; o músculo ganha glicose de volta. Fibras brancas (glicolíticas) e hemácias (sem mitocôndria) produzem lactato.','M-cori','cori'),
 ('integ1-coracao','The heart runs aerobically, burning mainly {{c1::fatty acids}} (plus ketone bodies), with little stored glycogen',
  'Muito rico em mitocôndrias e com consumo constante de ATP; guarda um pouco de fosfocreatina. Recebe os ácidos graxos do tecido adiposo e os corpos cetônicos do fígado.','T-coracao','coracao'),
 ('integ1-cerebro','At rest the brain uses about {{c1::20%}} of the body’s oxygen, and its neurons burn glucose (ketone bodies only in prolonged fasting)',
  'Neurônios não usam ácidos graxos; a glia pode usar. Por isso manter a glicemia é prioridade. O PET com glicose marcada mostra as áreas cerebrais ativas.','T-cerebro','cerebro'),
 ('integ1-porta','The {{c1::hepatic portal vein}} carries absorbed nutrients (and toxins) from the intestine straight to the liver',
  'Circulação porta = uma veia entre duas redes de capilares (intestino → fígado). Os lipídios da dieta vão pelo sistema linfático (quilomícrons), sem passar primeiro pelo fígado.','R-porta','porta'),
 ('integ1-aminoacidos','Amino acids cannot be stored: the liver removes their amino group as {{c1::urea}} and turns the carbon skeletons into glucose or fat',
  'Os da dieta vão primeiro para síntese de proteínas; o excesso vira triacilglicerol. No jejum, os do músculo chegam como alanina e viram glicose (ciclo glicose-alanina) ou corpos cetônicos.','F-aminoacidos','aminoacidos'),
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-01','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
