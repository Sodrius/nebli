import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-microbiologia-30-controle-microbiologico'
DECK='NEBLI::UC03::P2::Microbiologia::Controle microbiológico'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula de Controle microbiológico (UC03, Prof. Nilton Lincopan)'
IMGS=['hierarquia','total-parcial','morte-exponencial','autoclave','forno','pasteurizacao','filtracao','uv','alcool','cloro','semmelweis']
MEDIA=[(f'img/nebli-controle-{k}.png',f'nebli-controle-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-controle-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('hierarquia','Against disinfectants and sterilization, bacterial {{c1::spores}} are the most resistant forms and {{c2::enveloped (lipid) viruses}} the least',
  'Ordem da aula, do mais ao menos resistente: esporos (<i>Bacillus subtilis</i>) > micobactérias > vírus pequenos não lipídicos (poliovírus) > fungos (<i>Candida</i>) > bactérias vegetativas (<i>Pseudomonas</i>) > vírus lipídicos médios (HBV, HIV).','C-resistencia','hierarquia'),
 ('antissepsia','Chemical disinfection of skin, mucosa or other living tissue is called {{c1::antisepsis}}',
  'Esterilização (100%, objeto ou meio) > desinfecção (até 99%, superfícies inanimadas) > antissepsia (tecido vivo) > limpeza. O produto para tecido vivo é o antisséptico; para objetos, o desinfetante.','C-definicoes','total-parcial'),
 ('morte-exponencial','Under a biocide, microbes die exponentially: each minute kills the same {{c1::fraction}} of the survivors',
  'Na aula: de 1 milhão para 100 mil, 10 mil, mil... uma casa decimal por minuto. Por isso uma carga inicial maior exige mais tempo de contato para chegar a zero.','C-cinetica','morte-exponencial'),
 ('autoclave','The autoclave sterilizes with pressurized steam at about {{c1::121 °C}} for 15–20 minutes, denaturing proteins',
  'Calor úmido + pressão mata formas vegetativas, esporos e vírus. Usada para meios de cultura, vidraria, material cirúrgico termorresistente e material contaminado (inclusive de micobactérias).','F-calor','autoclave'),
 ('forno','A Pasteur (dry-heat) oven sterilizes glassware and metal instruments at {{c1::180 °C for 1 hour}}',
  'Calor seco mata por oxidação e coagulação de proteínas, mais devagar que o vapor; por isso precisa de temperatura maior e mais tempo. Chama do bico de Bunsen (flambagem) = incineração da alça.','F-calor','forno'),
 ('pasteurizacao','Pasteurizing milk (e.g., 72 °C for 15 s) kills vegetative pathogens but is {{c1::not sterilization}}, because spores survive',
  'Calor úmido sem pressão: LTLT 65 °C × 30 min, HTST 72 °C × 15 s e resfriamento, UHT 130–150 °C × 5 s. Fervura e tindalização também ficam nesse grupo.','F-calor','pasteurizacao'),
 ('filtracao','Heat-sensitive liquids are sterilized by filtration through membranes with {{c1::0.22 µm}} pores',
  'O filtro retém a maioria das bactérias (0,45 µm só as maiores). Micoplasmas e vírus passam. Filtros HEPA do fluxo laminar retêm 99,97% das partículas de 0,3 µm, mas não esterilizam.','F-filtracao','filtracao'),
 ('uv','Germicidal UV-C light (~260 nm) kills microbes by linking adjacent {{c1::thymines}} into dimers in their DNA',
  'O dímero de timina bloqueia a replicação. A UV só age na superfície exposta (ambientes, água, fluxo laminar), sem penetrar em materiais.','F-radiacao','uv'),
 ('alcool','Ethanol disinfects best at {{c1::70%}}, not 100%: the water helps it enter the cell and slows evaporation',
  'Mata por desnaturação de proteínas e ação mecânica. Age sobre Gram-positivos e Gram-negativos, BAAR, fungos e vírus envelopados, mas não sobre esporos. Evapora sem deixar resíduo.','Q-alcool','alcool'),
 ('cloro','Chlorine (bleach) only kills after it forms {{c1::hypochlorous acid (HOCl)}} in water',
  'É oxidante. Usos: água potável e piscinas (cloro gasoso), hipoclorito 1% em casa e em alimentos. Vantagem: barato e com ação residual; desvantagem: irrita a pele e é corrosivo.','Q-mecanismos','cloro'),
 ('semmelweis','In 1846, Semmelweis cut deaths from puerperal fever by making doctors {{c1::wash their hands}} before deliveries',
  'Ele suspeitou de "partículas cadavéricas" levadas da sala de necropsia para as parturientes. Em 1865, Lister levou a ideia à cirurgia, usando fenol (ácido carbólico) nos instrumentos e feridas.','H-maos','semmelweis'),
]
ROSA_AUTH={'semmelweis','forno'}
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-10','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
