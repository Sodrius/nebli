import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
ALEM=set(); ALEM_AUTH=set()
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-microbiologia-35-patogenicidade-bacteriana'
DECK='NEBLI::UC03::P2::Microbiologia::Patogenicidade bacteriana'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(Staphylococcus|Streptococcus|Enterococcus|Bacillus|Clostridium|Non-Spore|Lactose|Bacterial Toxins)',re.I)
SLIDE='<i><span style="font-size: 10pt;">Fonte: slides da aula de Patogenicidade bacteriana (UC03)</span></i>'
MEDIA=[(f'img/{n}',n) for n in ['nebli-pato-mscramm.png','nebli-pato-coagulase.png','nebli-pato-beta-hemolise.png','nebli-pato-lancefield.png','nebli-pato-tetano-neonatal.png','nebli-pato-quorum.png']]
SLIDE_IMG={}  # preenchido quando o PDF do slide estiver disponível: chave -> arquivo de mídia NEBLI
def img(name,credit=''): return f'<br><br><img src="{name}">'+(f'<br><i><span style="font-size: 10pt;">{credit}</span></i>' if credit else '')
AUTHORED=[
 ('patogenicidade-virulencia','Pathogenicity is the ability to cause disease; {{c1::virulence}} is how much disease a strain can cause',
  'Virulência é a medida quantitativa (ex.: dose infectante, gravidade). Oportunistas só causam doença quando a defesa do hospedeiro falha ou mudam de sítio.','V-conceitos',None),
 ('fases-infeccao','An infection runs through incubation, a {{c1::prodromal}} phase of vague symptoms, acute illness, and convalescence',
  'Pródromo: prostração, febre baixa, náusea, fraqueza, dores no corpo, antes dos sintomas específicos.','V-conceitos',None),
 ('quorum','Bacteria switch genes such as biofilm formation on when population density is high, via {{c1::quorum sensing}}',
  'Gram-negativos usam acil-homoserina lactonas; Gram-positivos, peptídeos; o sistema AI-2 serve a ambos. Controla biofilme e fatores de virulência, como em <i>Pseudomonas</i>.'+img('nebli-pato-quorum.png',SLIDE),'V-biofilme',None),
 ('mscramm','<i>S. aureus</i> sticks to host fibronectin and collagen through surface adhesins called {{c1::MSCRAMMs}}',
  'Proteínas de superfície ancoradas no peptidoglicano. Na aula: proteínas ligadoras de fibronectina (FnbpA/B), de colágeno (CNA) e a proteína A (liga Fc de IgG e fator de von Willebrand).'+img('nebli-pato-mscramm.png',SLIDE),'S-aureus',None),
 ('coagulase','<i>S. aureus</i> clots rabbit plasma in a tube because its coagulase turns {{c1::fibrinogen into fibrin}}',
  'É a prova que separa <i>S. aureus</i> (coagulase-positivo) dos estafilococos coagulase-negativos. A fibrina em volta da bactéria dificulta a fagocitose.'+img('nebli-pato-coagulase.png',SLIDE),'S-aureus',None),
 ('estreptolisinas','Streptolysin {{c1::O}} is oxygen-labile and immunogenic (anti-streptolysin O titers); streptolysin S is oxygen-stable and not immunogenic',
  'A estreptolisina S dá o halo de β-hemólise na superfície da placa, com ou sem O₂. A O só age sem oxigênio, lesa várias células e dissolve lisossomos de leucócitos.'+img('nebli-pato-beta-hemolise.png',SLIDE),'T-pyogenes',None),
 ('lancefield','Lancefield groups streptococci by the carbohydrate {{c1::C antigen}} of their cell wall (group A = <i>S. pyogenes</i>, B = <i>S. agalactiae</i>)',
  'Proposta por Rebecca Lancefield em 1933, com reações sorológicas. Grupo D inclui os enterococos (intestino grosso).'+img('nebli-pato-lancefield.png',SLIDE),'T-hemolise',None),
 ('tetano-neonatal','In neonatal tetanus, <i>C. tetani</i> spores enter through the {{c1::umbilical stump}}; the first sign is trouble sucking',
  'Aparece entre 5 e 13 dias de vida. A tetanospasmina bloqueia a liberação de GABA e glicina e causa hipertonia (paralisia espástica).'+img('nebli-pato-tetano-neonatal.png',SLIDE),'G-tetani',None),
 ('enterobacterias','Enterobacteriaceae are gram-negative rods that ferment glucose, reduce nitrate, and are {{c1::oxidase-negative}}',
  'São anaeróbios facultativos e não têm citocromo oxidase. <i>Pseudomonas</i>, ao contrário, é oxidase-positiva e não fermentadora.','N-enterobacterias',None),
 ('sorogrupo-sorotipo','For <i>E. coli</i>, the O antigen alone defines the {{c1::serogroup}}; O plus H defines the {{c2::serotype}} (e.g., O157:H7)',
  'O = LPS (O1–O173); H = flagelina (H1–H60). Pesquisa de antígenos serve para estudos epidemiológicos e para identificar cepas como a O157:H7.','N-antigenos',None),
 ('vi','<i>Salmonella</i> Typhi carries an extra capsular {{c1::Vi}} antigen that adds virulence',
  'Além dos antígenos O (LPS), H (flagelo) e K (cápsula) das enterobactérias.','N-salmonella',None),
 ('variacao-fase','<i>Salmonella</i> alternates between two flagellins (H1 and H2) by inverting a DNA segment, a switch called {{c1::phase variation}}',
  'A Hin invertase vira o promotor: numa orientação transcreve H2 e o repressor de H1; na outra, só H1. É um exemplo de variação antigênica para escapar do sistema imune.','N-salmonella',None),
 ('tsi','A black precipitate in TSI agar means the organism produces {{c1::H<sub>2</sub>S}}, as <i>Salmonella</i> does',
  'O TSI (tríplice açúcar ferro) mostra fermentação de glicose, lactose e sacarose (ácido = amarelo), gás e H₂S (tiossulfato → sulfeto de ferro preto).','N-identificacao',None),
]
ROSA_AUTH={'fases-infeccao','variacao-fase'}
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
            if found: ASSOCIATE[found[0]]=obj; continue
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-10','profile_evidence':call('getMediaDirPath'),
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
