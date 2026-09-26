import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE,ALEM,ALEM_AUTH
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-microbiologia-32-antibioticos-resistencia'
DECK='NEBLI::UC03::P2::Microbiologia::Antibióticos e resistência'
DECK_ALEM=DECK+'::Além da aula'
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'Antibiotics:',re.I)
# imagens reaproveitadas de cards AnKing/MCAT (já na coleção)
IMG_ANEL='f7e4274ec9851c031df8844f736be222.jpg'      # anel β-lactâmico (A5b, CC0)
IMG_CIM='4c64dc96f96c112c46362633a307886e.jpg'       # diluição em tubos até a CIM (J. DeCaussin, CC BY-SA 4.0)
IMG_HALO='fc6c409bbf3c677b8b1847c93ccc9f5a.webp'     # halo de inibição (S. Greenwood, CC BY-SA 4.0)
IMG_FOLATO='c3c61e1cce1d91fff42583b64768aba2.webp'   # via do folato (The AnKing)
SLIDE_IMG={}  # preenchido quando o PDF do slide estiver disponível: chave -> arquivo de mídia NEBLI
def img(name,credit=''): return f'<br><br><img src="{name}">'+(f'<br><i><span style="font-size: 10pt;">{credit}</span></i>' if credit else '')
AUTHORED=[
 ('fq-gyrA','A single point mutation in {{c1::<i>gyrA</i>}} can make <i>E. coli</i> resistant to ciprofloxacin',
  '<i>gyrA</i> codifica a DNA girase, o alvo da quinolona: o alvo muda e a droga deixa de se ligar. É o principal mecanismo de resistência a quinolonas em Gram+ e Gram−. Também contribuem as proteínas Qnr (plasmidiais), que protegem a girase, e as bombas de efluxo.','N-quinolonas','fq-gyrA'),
 ('carbapenemases','KPC and NDM are {{c1::carbapenemases}}: they destroy even the last-resort β-lactams',
  'Hidrolisam o anel β-lactâmico dos carbapenêmicos e de quase todos os outros β-lactâmicos. A KPC é inibida pelo avibactam (ceftazidima-avibactam); a NDM é uma metalo-β-lactamase e não é. Por isso a polimixina vira terapia de resgate.'+img(IMG_ANEL,'Anel β-lactâmico: a seta marca a ligação amida quebrada pelas β-lactamases.'),'R-enzima','betalactamases'),
 ('cim-halo','Antibiogram: broth dilution gives the {{c1::MIC}} in µg/mL, while disk diffusion gives the {{c2::zone of inhibition}} in mm',
  'Diluição em caldo = antibiograma quantitativo; disco-difusão = qualitativo. Os dois resultados são lidos contra pontos de corte: sensível, intermediário ou resistente. Meio padrão: Mueller-Hinton.'+img(IMG_CIM)+img(IMG_HALO),'Z-antibiograma',None),
 ('mdr-xdr','A strain resistant to ≥{{c1::3}} antibiotic classes is MDR; if only one or two classes still work, it is {{c2::XDR}}',
  'Definições de Magiorakis et al. (2012), usadas na aula: MDR = não sensível a ≥1 agente em ≥3 categorias; XDR = sensível a no máximo 2 categorias.','R-conceitos','mdr-xdr'),
 ('sulfa-seletividade','Sulfonamides spare our cells because humans take {{c1::folate from the diet}}, while bacteria must make it from PABA',
  'É a seletividade de Ehrlich aplicada: a sulfa imita o PABA e bloqueia a di-hidropteroato-sintase, uma enzima que nós não temos. Sozinhas, as sulfas são bacteriostáticas.'+img(IMG_FOLATO),'S-folato',None),
 ('antagonismo','Adding a bacteriostatic drug to penicillin can backfire: β-lactams kill only {{c1::actively growing}} bacteria',
  'O bacteriostático para a divisão; sem síntese de parede em curso, o β-lactâmico perde o efeito bactericida (antagonismo). Os antibióticos agem melhor na fase exponencial (log) da curva de crescimento.','A-conceitos',None),
 ('quimioterapico','Ciprofloxacin and sulfonamides are synthetic, so strictly they are {{c1::chemotherapeutic agents}}, not antibiotics',
  'Antibiótico, no sentido estrito, é produto de microrganismo (penicilina: <i>Penicillium</i>; estreptomicina: <i>Streptomyces</i>), um metabólito secundário da fase estacionária.','A-conceitos','quimioterapicos'),
]
ROSA_AUTH={'quimioterapico'}
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
EXTRA_TRIM={1503683672620:'3rd gen cephalosporins (ceftriaxone, cefotaxime, ceftazidime) penetrate the CNS and have broad-spectrum gram-negative coverage.'}
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
            'scope':'alem' if n['noteId'] in ALEM else 'aula','pink':n['noteId'] in ALEM}
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
