import hashlib,json,re,sys
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-imunologia-31-sistema-complemento'
DECK='NEBLI::UC03::P2::Imunologia::Sistema complemento'
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
NOMENC='<br><br>Nos slides da aula (nomenclatura antiga do C2, em que C2a é o fragmento maior): '
SOURCES={
 1487640142103:('T1-sintese',None),
 1520299391760:('T1-inato',None),
 1487640144801:('T3-vias',None),
 1487640158306:('T3-vias',None),
 1487640169311:('T3-vias',None),
 1487640151914:('T4-classica',None),
 1487117187498:('T4-classica',None),
 1487640163185:('T5-alternativa',None),
 1500572318680:('T5-alternativa',None),
 1487640180743:('T4-T5-convertases',None),
 1487640191924:('T4-T5-convertases',None),
 1487640184312:('T4-T5-convertases',('Extra','append',NOMENC+'<b>C4b2a</b>.')),
 1487640188409:('T4-T5-convertases',None),
 1487640197206:('T4-T5-convertases',('Extra','append',NOMENC+'<b>C4b2a3b</b>.')),
 1487640200798:('T4-T5-convertases',None),
 1487640207727:('T7-MAC',None),
 1487640139590:('T8-anafilatoxinas',None),
 1487640222923:('T8-imunocomplexos',None),
 1503855271322:('T9-receptores',None),
 1478986720423:('T10-regulacao',None),
 1478995034893:('T11-deficiencias',('Text','replace','{{c3::<u>flow cytometry</u>}}','<u>flow cytometry</u>')),
 1487727789545:('T11-deficiencias',None),
 1517068230955:('T11-deficiencias',None),
 1487727803414:('T11-deficiencias',None),
 1501968263352:('T11-deficiencias',None),
 1487727812574:('T11-deficiencias',None),
 1487727820979:('T11-deficiencias',None),
 1487727814679:('T11-deficiencias',None),
 1500404833072:('bridge-encapsulados',None),
}
AUTHORED=[
 ('fragmentos-a-b','Most complement cleavage products are a small soluble {{c1::"a"}} fragment and a larger {{c1::"b"}} fragment that binds covalently to the activating surface','Ex.: C3 → C3a (anafilatoxina, solúvel) + C3b (opsonina, liga-se à superfície). Exceção: na nomenclatura antiga do C2, usada nos slides, C2a é o fragmento maior (C4b2a).','T2-principio'),
 ('c1-complexo','In the classical pathway, {{c1::C1q}} binds the Fc region of antigen-bound antibody, and activated {{c2::C1s}} cleaves C4 and C2','C1 = C1q + 2 C1r + 2 C1s (C1qr<sub>2</sub>s<sub>2</sub>), dependente de Ca<sup>2+</sup>; C1r ativado ativa C1s.','T4-classica'),
 ('igg-igm','Classical pathway activation requires {{c1::two or more}} antigen-bound IgG molecules but only {{c1::one}} antigen-bound IgM pentamer','C1q precisa se ligar a pelo menos duas porções Fc próximas; o pentâmero de IgM já as oferece. Sítios de ligação: CH2 (IgG) e CH3 (IgM).','T4-classica'),
 ('fator-b-d','In the alternative pathway, factor {{c1::B}} binds C3b and is then cleaved by factor {{c2::D}}, forming the C3 convertase C3bBb','O ponto de partida é a hidrólise espontânea do C3 [C3(H<sub>2</sub>O)], que forma uma convertase inicial em fase fluida; o fragmento Ba é liberado.','T5-alternativa'),
 ('properdina','{{c1::Properdin}} stabilizes the alternative pathway C3 convertase (C3bBb)','Cada C3bBb gera mais C3b, que forma mais convertase: alça de amplificação da via alternativa.','T5-alternativa'),
 ('mbl-masp','In the lectin pathway, {{c1::mannose-binding lectin (MBL)}} binds microbial carbohydrates and activates {{c2::MASP-1 and MASP-2}}, which cleave C4 and C2','MBL ≈ C1q e MASPs ≈ C1r/C1s; a C3 convertase formada é a mesma da via clássica (C4b2a).','T6-lectinas'),
 ('cr1-cr3','Phagocytes bind C3b through {{c1::CR1 (CD35)}} and iC3b through {{c2::CR3 (CD11b/CD18, Mac-1)}}','CR1 nas hemácias também transporta imunocomplexos cobertos por C3b/C4b até fígado e baço. CR4 (CD11c/CD18) também reconhece iC3b.','T9-receptores'),
 ('correceptor-b','Binding of C3d-coated antigen to CR2 (CD21), together with CD19 and CD81, {{c1::lowers the activation threshold}} of B cells','Elo entre imunidade inata e humoral; nas células dendríticas foliculares, CR2 retém antígeno nos centros germinativos.','T9-receptores'),
 ('c1-inh','C1 inhibitor (C1-INH) inactivates the C1 proteases {{c1::C1r and C1s}}','Também inibe calicreína e fator XIIa — por isso sua deficiência eleva a bradicinina.','T10-regulacao'),
 ('fator-i-h','Factor {{c1::I}}, with cofactor factor {{c1::H}} (or CR1/MCP), cleaves C3b into {{c2::iC3b}}','Clivagens seguintes: iC3b → C3dg (+ C3c); C4b → C4c + C4d. iC3b não forma convertase, mas continua opsonina (CR3).','T10-regulacao'),
 ('cd59','{{c1::CD59}} (MIRL) protects host cells by blocking C9 polymerization and membrane attack complex formation','Ancorado por GPI, como o DAF (CD55); a falta de ambos causa hemoglobinúria paroxística noturna.','T10-regulacao'),
 ('deficiencia-fator-h-i','Factor H or factor I deficiency allows uncontrolled alternative pathway activation that {{c1::consumes C3}}; factor H defects are also linked to {{c2::atypical hemolytic uremic syndrome}}','C3 baixo → pouca opsonização → infecções piogênicas recorrentes. Ativação descontrolada sobre o endotélio → microangiopatia trombótica e lesão renal.','T11-deficiencias'),
 ('ch50-ah50','The {{c1::CH50}} assay screens classical (and terminal) pathway function, whereas the {{c2::AH50}} assay screens alternative (and terminal) pathway function','CH50 normal + AH50 indetectável → defeito de componente exclusivo da via alternativa (fator B, fator D ou properdina). Ambos baixos → componente comum (C3) ou terminal (C5–C9).','A1-laboratorio'),
 ('c3-baixo-c4-normal','Low C3 with normal C4 suggests complement consumption through the {{c1::alternative}} pathway','C4 só é clivado pelas vias clássica e das lectinas. C3 e C4 baixos juntos apontam ativação clássica (ex.: imunocomplexos).','A2-laboratorio'),
]
ASSOCIATE={1790099856597:'T8-opsonizacao',1790080249786:'T8-quimiotaxia'}

def digest(v): return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def clozes(v): return sorted({int(x) for x in re.findall(r'{{c(\d+)::',v)})

def main():
    notes={n['noteId']:n for n in call('notesInfo',notes=list(SOURCES))}
    if set(notes)!=set(SOURCES): raise RuntimeError('Fonte ausente')
    entries=[];collisions={}
    for nid,(obj,mod) in SOURCES.items():
        n=notes[nid]; f={k:v['value'] for k,v in n['fields'].items()}
        if not n['modelName'].startswith('AnKingOverhaul (AnKing'): raise RuntimeError(f'Modelo inesperado {nid}')
        found=call('findNotes',query=f'tag:"NEBLI::source::nid-{nid}"')
        if found: collisions[nid]=found
        change=None
        if mod:
            field,kind=mod[0],mod[1]
            before=f[field]
            if kind=='append': f[field]=before+mod[2]
            else:
                if mod[2] not in before: raise RuntimeError(f'Trecho ausente {nid}')
                f[field]=before.replace(mod[2],mod[3])
            change={'field':field,'kind':kind,'detail':list(mod[2:])}
        entries.append({'key':f'source-{nid}','source_nid':nid,'source_model':n['modelName'],'source_tags':n['tags'],'source_fields_hash':digest(n['fields']),'fields':f,'copy_change':change,'objective':obj,'origin':'AnKing','expected_cards':len(clozes(f['Text'])),'high_yield':HY in n['tags']})
    for key,text,extra,obj in AUTHORED:
        entries.append({'key':'authored-'+key,'source_nid':None,'source_model':None,'source_tags':[],'source_fields_hash':None,'fields':{'Text':text,'Extra':extra},'copy_change':None,'objective':obj,'origin':'Autoral','expected_cards':len(clozes(text)),'high_yield':False})
    assoc=[]
    for nid,obj in ASSOCIATE.items():
        n=call('notesInfo',notes=[nid])[0]
        assoc.append({'nid':nid,'objective':obj,'tags_before':n['tags'],'fields_hash':digest(n['fields']),'decks':sorted({c['deckName'] for c in call('cardsInfo',cards=n['cards'])})})
    t=lambda o: sum(x['expected_cards'] for x in entries if x['origin']==o)
    plan={'lesson_id':LESSON,'target_deck':DECK,'lesson_date':'2026-09-08','profile_evidence':call('getMediaDirPath'),
      'source_manifest':'source-manifest.json','entries':entries,'associate_existing':assoc,'collisions':collisions,
      'excluded_candidates':'candidate-decisions.md',
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'Autoral':t('Autoral'),'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield']),'associated_existing_notes':len(assoc)}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'totals':plan['totals'],'collisions':collisions,'assoc':[(a['nid'],a['decks']) for a in assoc]},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
