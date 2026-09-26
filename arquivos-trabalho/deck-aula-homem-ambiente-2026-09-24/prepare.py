import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-microbiologia-39-homem-ambiente-microrganismo'
DECK='NEBLI::UC03::P2::Microbiologia::Homem, ambiente e microrganismo'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula Microbiota humana (UC03, Profa. Carla Taddei)'
IMGS=['residente','funcoes','mapa','vias-aereas','lactobacilos','sucessao','bifido','composicao','probioticos','higiene','agcc','disfuncoes','ecossistemas']
MEDIA=[(f'img/nebli-microbiota-{k}.png',f'nebli-microbiota-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-microbiota-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('residente','Microbes that permanently colonize skin and mucosa are the {{c1::resident}} microbiota; those picked up from the environment and soon lost are {{c2::transient}}',
  'Lavar as mãos com água e sabão remove sobretudo a transitória; a residente se recompõe em cerca de 8 horas. Banho e suor não mudam a residente de modo significativo.','M-conceitos','residente'),
 ('antagonismo-microbiota','The main benefit of the resident microbiota is {{c1::bacterial antagonism}}: it outcompetes pathogens for adhesion sites and nutrients',
  'Também produz substâncias antimicrobianas. É a chamada resistência à colonização; quando antibióticos a destroem, patógenos ocupam o espaço.','M-conceitos','funcoes'),
 ('translocacao','<i>S. aureus</i> from the resident skin flora becomes pathogenic when a wound lets it {{c1::translocate}} into tissue or blood',
  'Microbiota "normal" não é inofensiva por natureza: é patogênica fora do seu sítio ou quando a barreira ou a imunidade falham (ex.: <i>E. coli</i> intestinal na via urinária).','M-conceitos','ecossistemas'),
 ('pele','Besides staphylococci, resident skin flora includes <i>Corynebacterium</i> and {{c1::<i>Cutibacterium</i> (<i>Propionibacterium</i>)}} in sebaceous glands',
  'Mais densa nas axilas e períneo (~10⁶ bactérias/cm²). O pH baixo, os ácidos graxos do sebo e a lisozima eliminam os microrganismos transitórios.','S-pele','mapa'),
 ('esteril','Below the larynx, the bronchioles and alveoli are normally {{c1::sterile}}',
  'Nariz: <i>Staphylococcus</i> e <i>Corynebacterium</i>; faringe: estreptococos α-hemolíticos, <i>Neisseria</i>, pneumococo, <i>Haemophilus</i>. A conjuntiva é mantida quase estéril pela lágrima, que contém lisozima.','S-vias-aereas','vias-aereas'),
 ('lactobacilos','Vaginal lactobacilli keep the pH acidic by turning epithelial glycogen, stored under estrogen, into {{c1::lactic acid}}',
  'Recém-nascida (estrogênio materno) e mulher em idade fértil: lactobacilos e pH ácido. Antes da puberdade e após a menopausa: flora mista. Se antimicrobianos suprimem os lactobacilos, leveduras e outras bactérias proliferam.','S-vagina','lactobacilos'),
 ('sucessao','A newborn’s gut, sterile in the uterus, is first colonized by {{c1::facultative anaerobes}} (<i>E. coli</i>, streptococci), which use up O<sub>2</sub> and open the way for obligate anaerobes',
  'Depois chegam <i>Bifidobacterium</i>, <i>Bacteroides</i> e outros anaeróbios estritos. A composição se estabiliza por volta dos 2 anos e depende do tipo de parto, da alimentação, do ambiente e de antibióticos.','I-colonizacao','sucessao'),
 ('bifido','Breast milk contains a "bifidus factor" that favors {{c1::<i>Bifidobacterium</i>}} in the infant gut',
  'Fator bífido = N-acetilglicosamina do leite materno. É um dos fatores externos (com tipo de parto e microbiota materna) que moldam a microbiota intestinal.','I-colonizacao','bifido'),
 ('composicao','The colon holds the densest microbiota (~10<sup>11</sup>–10<sup>12</sup> CFU/mL), dominated by the phyla {{c1::Bacteroidetes}} and {{c1::Firmicutes}}',
  'O estômago tem pouquíssimas bactérias por causa da acidez; a contagem sobe ao longo do intestino delgado. Predominam anaeróbios (<i>Bacteroides</i>, <i>Bifidobacterium</i>, <i>Clostridium</i>, <i>Eubacterium</i>).','I-composicao','composicao'),
 ('agcc','Colonic bacteria ferment dietary fiber into {{c1::short-chain fatty acids}}, an energy source for the colonic epithelium',
  'Outras funções metabólicas na aula: síntese de vitaminas K e do complexo B, metabolismo de ácidos biliares e de gluconato.','F-agcc','agcc'),
 ('probioticos','{{c1::Probiotics}} are live microbes that benefit health when ingested; {{c2::prebiotics}} are non-absorbed food ingredients that feed them',
  'Prebióticos (ex.: inulina, oligofrutose, fibras) estimulam seletivamente bifidobactérias e lactobacilos. Ex. de probiótico: <i>Lactobacillus casei</i> em leites fermentados.','F-probioticos','probioticos'),
 ('higiene','Too little microbial exposure early in life raises rates of allergy and autoimmune disease, the {{c1::hygiene hypothesis}}',
  'Os primeiros meses são uma janela para a regulação imune: a microbiota ajuda a equilibrar as respostas Th1/Th2 e a induzir tolerância.','F-imune','higiene'),
 ('disbiose','An imbalance of the gut microbiota, often after {{c1::antibiotics}}, is called dysbiosis',
  'Na aula: a curto prazo, enterocolite necrosante, colite pseudomembranosa e diarreia por antibiótico; a médio prazo, alergia; a longo prazo, doença inflamatória intestinal e câncer colorretal. Outros fatores: dieta, álcool, fumo, idade, estresse.','D-disbiose','disfuncoes'),
]
ROSA_AUTH={'bifido','composicao'}
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-17','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
