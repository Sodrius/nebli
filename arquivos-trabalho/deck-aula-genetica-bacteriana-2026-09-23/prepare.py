import hashlib,json,re,sys
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-microbiologia-34-genetica-bacteriana'
DECK='NEBLI::UC03::P2::Microbiologia::Genética bacteriana'
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'DNA Replication|DNA Mutations|Bacterial Gen|Recombinant DNA|Transduction|Transformation|Conjugation|Transposition|CRISPR|DNA Structures',re.I)
LATERAL=re.compile(r'Staph|Vancomycin|Fluoroquinolone|Topoisomerase Inhibitors|Repair Mechanisms|Single Stranded Repair|Xeroderma|Antibiotics|Glycopeptide|Transcription and RNA Processing|Organization of a Gene|Primary Structure',re.I)

# nid -> (objetivo, [edições])
# edições: ('replace', campo, antigo, novo) | ('append', campo, html) | ('uncloze', [n,...])
SOURCES={
 1500405795435:('G2-plasmideos',[]),
 1467771810893:('G3-superenovelamento',[('append','Extra','A girase usa ATP para introduzir supertorções <b>negativas</b> no DNA circular bacteriano; é alvo das quinolonas.')]),
 1509287317713:('G3-superenovelamento',[]),
 1508430090586:('G3-quinolonas-ponte',[]),
 1467771772782:('R1-origem',[]),
 1467771834622:('R2-maquinaria',[]),
 1467771842612:('R2-maquinaria',[]),
 1467771872364:('R2-maquinaria',[]),
 1522425325857:('R2-maquinaria',[]),
 1467771897291:('R2-maquinaria',[]),
 1467771968226:('M1-tipos',[]),
 1467771977177:('M1-tipos',[('replace','Extra','<div>e.g., sickle cell disease (substitution of glutamic acid with valine)</div><br>','')]),
 1467771988825:('M1-tipos',[]),
 1467771998020:('M1-tipos',[('replace','Extra','; examples include <b>Duchenne muscular dystrophy</b> and <b>Tay-Sachs disease</b>','')]),
 1496159950271:('M2-mutagenicos',[('replace','Text','causes carcinogenesis by generating','damages DNA by generating'),
                                    ('replace','Extra','- These are normally excised by the nucleotide excision repair (NER) pathway, but excess UV-B can overwhelm this system<br><br><div>- Patients who have xeroderma pigmentosum have a faulty NER pathway, thus are very susceptible to non-ionizing radiation</div>','<div>Radiação UV: dímeros de timina/pirimidina distorcem a dupla hélice e bloqueiam a replicação.</div>')]),
 1500673219562:('T1-transformacao',[('append','Extra','<br><br>Para captar DNA livre, a bactéria precisa estar em estado de <b>competência</b>.')]),
 1500673513536:('T1-transformacao',[]),
 1500738431745:('T2-transducao',[]),
 1500738726042:('T2-transducao',[]),
 1500738801391:('T2-transducao',[]),
 1500673825876:('T3-conjugacao',[('append','Extra','<br>O pilus sexual é codificado pelo plasmídeo F (fator F): a célula F<sup>+</sup> doa uma cópia do plasmídeo e a receptora F<sup>−</sup> se torna F<sup>+</sup>.')]),
 1500674235789:('T3-conjugacao',[]),
 1500673915770:('T3-conjugacao',[('uncloze',[2])]),
 1500674026608:('T3-conjugacao',[('uncloze',[1])]),
 1500740499801:('T4-transposons',[('uncloze',[1]),('append','Extra','<br>- Transposon composto (ex.: Tn<i>10</i>): gene de resistência (tet<sup>R</sup>) entre duas sequências de inserção (IS) com repetições invertidas.')]),
 1500740742100:('T4-transposons',[('uncloze',[1])]),
 1485883729339:('T4-transposons',[('uncloze',[2])]),
 1468549196500:('D1-recombinante',[]),
 1468549202187:('D1-recombinante',[]),
 1519849576725:('C1-crispr',[('replace','Extra',' - The gRNA can be designed to target ANY DNA sequence, which brings the endonuclease to that site to introduce a <u>gap</u>; PAM sequences are sites where Cas9 can bind ','')]),
}
AUTHORED=[
 ('nucleoide','Bacterial chromosomal DNA, usually a single circular molecule, is compacted in the {{c1::nucleoid}}, a region not enclosed by a membrane','Compactação por proteínas semelhantes a histonas (HU, H-NS), cátions e poliaminas; não há núcleo.','G1-nucleoide'),
 ('replicacao-theta','The circular bacterial chromosome is replicated from a {{c1::single origin (oriC)}} and proceeds {{c2::bidirectionally}}, forming a θ (theta) structure','oriC é rica em A-T e em sítios GATC metilados; as duas forquilhas se encontram na região terminal (ter).','R1-origem'),
 ('mutagenicos','Ionizing radiation mainly causes DNA {{c1::strand breaks}}, whereas planar molecules such as ethidium bromide {{c2::intercalate}} between base pairs','Outros mutagênicos químicos da aula: agentes alquilantes (ex.: EMS) e H<sub>2</sub>O<sub>2</sub> (dano oxidativo). UV forma dímeros de pirimidina.','M2-mutagenicos'),
 ('origem-resistencia','Bacteria acquire antibiotic resistance either by chromosomal {{c1::mutation}}, passed vertically, or by {{c2::horizontal gene transfer}} (transformation, transduction, conjugation)','Genes adquiridos costumam vir em plasmídeos R e transposons (ex.: <i>mecA</i> no SCCmec de <i>S. aureus</i>; <i>vanA</i>). Mutação: ex. alteração da girase na resistência a quinolonas.','M3-resistencia'),
 ('restricao-extremidades','Restriction enzymes cut {{c1::palindromic}} DNA sites; a staggered cut leaves {{c2::sticky (cohesive)}} ends, whereas a cut at the axis of symmetry leaves blunt ends','Ex.: EcoRI (G↓AATTC) gera extremidades coesivas; SmaI (CCC↓GGG) gera extremidades abruptas. A DNA ligase une fragmentos com extremidades compatíveis.','D1-recombinante'),
 ('crispr-espacadores','In bacteria, CRISPR arrays store {{c1::spacers}} copied from previously encountered phage DNA, which guide Cas nucleases to cut that phage on reinfection','Memória adaptativa bacteriana. Outras defesas contra fagos na aula: restrição-modificação (a bactéria metila o próprio DNA), bloqueio de adsorção/injeção e suicídio celular.','C1-crispr'),
]

def digest(v): return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def clozes(v): return sorted({int(x) for x in re.findall(r'{{c(\d+)::',v)})
CLOZE=re.compile(r'\{\{c(\d+)::((?:(?!\}\}).)*?)(?:::((?:(?!\}\}).)*?))?\}\}',re.S)
def uncloze(text,nums):
    return CLOZE.sub(lambda m: m.group(2) if int(m.group(1)) in nums else m.group(0),text)
def clean_resources(f):
    changed={}
    for k in RESOURCE_FIELDS:
        v=f.get(k,'')
        if not v.strip(): continue
        plain=re.sub(r'<[^>]+>',' ',v)
        if ON_TOPIC.search(plain) and not LATERAL.search(plain): continue
        if k=='Bootcamp':
            parts=[p for p in re.split(r'(?:\s*<br>\s*)+',v) if p.strip()]
            keep=[p for p in parts if ON_TOPIC.search(p) and not LATERAL.search(p)]
            new='<br><br>'.join(keep)
        else: new=''
        if new!=v: changed[k]=new; f[k]=new
    return changed

def main():
    notes={n['noteId']:n for n in call('notesInfo',notes=list(SOURCES))}
    if set(notes)!=set(SOURCES): raise RuntimeError('Fonte ausente')
    entries=[];collisions={}
    for nid,(obj,edits) in SOURCES.items():
        n=notes[nid]; f={k:v['value'] for k,v in n['fields'].items()}
        if not n['modelName'].startswith('AnKingOverhaul (AnKing'): raise RuntimeError(f'Modelo inesperado {nid}')
        found=call('findNotes',query=f'tag:"NEBLI::source::nid-{nid}"')
        if found: collisions[nid]=found
        log=[]
        for e in edits:
            if e[0]=='replace':
                if e[2] not in f[e[1]]: raise RuntimeError(f'Trecho ausente {nid} {e[1]}')
                f[e[1]]=f[e[1]].replace(e[2],e[3])
            elif e[0]=='append': f[e[1]]+=e[2]
            elif e[0]=='uncloze':
                before=clozes(f['Text']); f['Text']=uncloze(f['Text'],set(e[1]))
                if set(clozes(f['Text']))!=set(before)-set(e[1]): raise RuntimeError(f'Uncloze falhou {nid}')
            log.append(list(e))
        res=clean_resources(f)
        if res: log.append(['resources_cleared',sorted(res)])
        entries.append({'key':f'source-{nid}','source_nid':nid,'source_model':n['modelName'],'source_tags':n['tags'],'source_fields_hash':digest(n['fields']),'fields':f,'copy_changes':log,'objective':obj,'origin':'AnKing','expected_cards':len(clozes(f['Text'])),'high_yield':HY in n['tags']})
    for key,text,extra,obj in AUTHORED:
        entries.append({'key':'authored-'+key,'source_nid':None,'source_model':None,'source_tags':[],'source_fields_hash':None,'fields':{'Text':text,'Extra':extra},'copy_changes':[],'objective':obj,'origin':'Autoral','expected_cards':len(clozes(text)),'high_yield':False})
    t=lambda o: sum(x['expected_cards'] for x in entries if x['origin']==o)
    plan={'lesson_id':LESSON,'target_deck':DECK,'lesson_date':'2026-09-11','profile_evidence':call('getMediaDirPath'),
      'source_manifest':'source-manifest.json','entries':entries,'associate_existing':[],'collisions':collisions,
      'excluded_candidates':'candidate-decisions.md',
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'Autoral':t('Autoral'),'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield']),'associated_existing_notes':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'totals':plan['totals'],'collisions':collisions},ensure_ascii=False,indent=2))
    for e in entries:
        if e['copy_changes']: print(e['key'],'→',[c[0] if c[0]!='resources_cleared' else c for c in e['copy_changes']])

if __name__=='__main__': main()
