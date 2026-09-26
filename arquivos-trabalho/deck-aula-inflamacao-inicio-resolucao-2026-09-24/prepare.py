import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-imunologia-37-inflamacao-inicio-resolucao'
DECK='NEBLI::UC03::P2::Imunologia::Inflamação: início e resolução'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(?!x)x')  # vídeo nunca no card: Bootcamp zerado
SLIDE='Fonte: slides da aula de Inflamação: início e resolução (UC03)'
IMGS=['prr', 'tlr', 'acido-urico', 'microcirculacao', 'fagocitose', 'neurogenica', 'resumo', 'quimiocinas']
MEDIA=[(f'img/nebli-inflam-{k}.png',f'nebli-inflam-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-inflam-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('inflam-pamp','Innate pattern recognition receptors are germline-encoded and recognize conserved microbial motifs called {{c1::PAMPs}}',
  'Especificidade limitada. Podem ser solúveis (PCR, MBL, complemento, IgM natural), de membrana (TLR, lectinas tipo C, scavengers) ou citoplasmáticos (NOD, RIG-I).','P-prr','prr'),
 ('inflam-tlr','Toll-like receptors: TLR4 senses {{c1::LPS}}, TLR5 senses {{c2::flagellin}}, and TLR3 senses viral {{c3::double-stranded RNA}}',
  'TLR2 (com TLR1/6): Gram-positivos e fungos. TLR7/8: RNA viral de fita simples. TLR9: DNA bacteriano (CpG). São 11 em humanos.','P-tlr','tlr'),
 ('inflam-endossomo','The nucleic-acid-sensing TLRs (TLR3, 7, 8 and 9) sit in {{c1::endosomes}}, not on the plasma membrane',
  'Assim encontram o material genético de micróbios fagocitados. Os que reconhecem componentes de parede (TLR1/2/4/5/6) ficam na membrana plasmática.','P-tlr','tlr'),
 ('inflam-citosol','In the cytosol, NOD-like receptors detect bacterial products, while {{c1::RIG-I}} detects viral RNA',
  'NOD, NALP e NAIP reconhecem produtos de bactérias Gram-positivas e negativas. A via TLR/MyD88 converge em NF-κB, que liga genes de citocinas, quimiocinas e moléculas de adesão.','P-prr','prr'),
 ('inflam-damp','Sterile injury triggers inflammation through {{c1::DAMPs}}, such as uric acid crystals or heat-shock proteins released by damaged cells',
  'Na aula: o cristal de ácido úrico ativa o inflamassoma (NLRP3), que libera IL-1β. Dano, isquemia e necrose também ativam TLR4.','P-inflamassoma','acido-urico'),
 ('inflam-vascular','In acute inflammation, a brief arteriolar {{c1::vasoconstriction}} is followed by arteriolar vasodilation and increased venular permeability',
  'Depois: saída de líquido (exsudato), hemoconcentração e estase, que favorecem a marginação e a adesão dos leucócitos.','A-vascular','microcirculacao'),
 ('inflam-net','Activated neutrophils can extrude DNA decorated with granule proteins as {{c1::NETs}}, which trap and kill microbes',
  'Ativação completa do neutrófilo: fagocitose, explosão oxidativa (espécies reativas de O₂), degranulação e NETs.','L-fagocitose','fagocitose'),
 ('inflam-neurogenica','Sensory nerve endings release neuropeptides that activate mast cells and dilate vessels: {{c1::neurogenic}} inflammation',
  'Estimulação antidrômica de fibras sensitivas: vasodilatação, aumento da permeabilidade e edema, sem agente infeccioso.','M-neurogenica','neurogenica'),
 ('inflam-mastocito','Mast cells release preformed {{c1::histamine and serotonin}} from granules, then newly synthesized lipid mediators and cytokines',
  'A histamina age em receptores H1 a H4. Os mediadores lipídicos (prostaglandinas, leucotrienos, PAF) e as citocinas são sintetizados após a ativação.','C-mastocito','resumo'),
 ('inflam-eotaxina','Eosinophils are recruited mainly by {{c1::eotaxin}} (with PAF and LTB4), while neutrophils follow IL-8 and LTB4',
  'Na cinética da aula: neutrófilos primeiro, macrófagos em 12–48 h, eosinófilos (inflamação alérgica) e linfócitos após ~72 h.','L-migracao','quimiocinas'),
]
ROSA_AUTH={'inflam-endossomo'}
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
