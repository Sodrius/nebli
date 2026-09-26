import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from selection import SEL,MCAT,ASSOCIATE
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-biomol-29-operon-procariotos'
DECK='NEBLI::UC03::P2::Biologia Molecular::Operon em procariotos'
DECK_ALEM=DECK
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME','Additional Resources']
ON_TOPIC=re.compile(r'(Lac Operon|Organization of a Gene)',re.I)
SLIDE='Fonte: slides da aula de Operon em procariotos (UC03, Prof. Alexandre Bruni-Cardoso)'
IMGS=['niveis','cis-trans','correpressor','mapa-lac','lactose','nobel','tipos-mutacao','curvas-mutantes','diploide-lacI','diploide-Oc','iptg-merozigoto','xgal-placa','hth','basal','sigma','cap-rnap']
MEDIA=[(f'img/nebli-operon-{k}.png',f'nebli-operon-{k}.png') for k in IMGS]
def img(k): return f'<br><br><img src="nebli-operon-{k}.png"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'
AUTHORED=[
 ('niveis','Bacteria control most genes at {{c1::transcription initiation}}, so no energy is wasted making mRNA or protein that is not needed',
  'A expressão pode ser regulada em vários níveis (transcricional, pós-transcricional, traducional, pós-traducional), mas desligar no início é o mais econômico; as outras camadas ajustam a resposta com mais rapidez e precisão.','R-niveis','niveis'),
 ('cis-trans','The <i>lac</i> operator and promoter act only in {{c1::cis}}; the LacI repressor is a diffusible protein that acts in {{c2::trans}}',
  '<i>Cis</i>: sequência de DNA que só age na mesma molécula em que está. <i>Trans</i>: produto gênico difusível, que age à distância, até sobre outra molécula de DNA.','R-cis-trans','cis-trans'),
 ('correpressor','In a repressible operon like <i>trp</i>, the end product tryptophan acts as a {{c1::co-repressor}} that lets the repressor bind the operator',
  'Regulação negativa repressível: sem o co-repressor, o repressor fica solto e a via funciona; quando o produto se acumula, liga-se ao repressor e desliga a própria síntese. É o oposto do lac (negativo induzível).','R-tipos','correpressor'),
 ('genes-lac','In the <i>lac</i> operon, <i>lacZ</i> encodes {{c1::β-galactosidase}} and <i>lacY</i> encodes {{c2::lactose permease}}',
  '<i>lacA</i> codifica a transacetilase. Os três genes saem num único mRNA policistrônico a partir do promotor lac; o <i>lacI</i> (repressor) tem promotor próprio, logo antes.','L-genes','mapa-lac'),
 ('jacob-monod','Jacob and Monod proposed the operon model (1960) by studying {{c1::lactose}} metabolism in <i>E. coli</i>',
  'Nobel de Fisiologia ou Medicina de 1965, com André Lwoff. Chegaram ao modelo só com genética e lógica, analisando mutantes.','L-historia','nobel'),
 ('laci-menos','A <i>lacI</i><sup>−</sup> mutant makes β-galactosidase even without lactose, because its repressor cannot bind the operator: expression is {{c1::constitutive}}',
  'A mutação no operador (O<sup>c</sup>) dá o mesmo fenótipo constitutivo. Não induzíveis: <i>lacI</i><sup>S</sup> e <i>lacZ</i><sup>−</sup>.','M-mutantes','tipos-mutacao'),
 ('laci-s','A <i>lacI</i><sup>S</sup> (super-repressor) cannot bind the inducer, so lactose never switches the operon on: it is {{c1::non-inducible}}',
  'O repressor fica preso ao operador mesmo com alolactose ou IPTG. Por isso também é dominante num diploide parcial: o super-repressor difusível bloqueia as duas cópias.','M-mutantes','curvas-mutantes'),
 ('lacy-menos','A <i>lacY</i><sup>−</sup> mutant with a normal repressor is not induced by lactose in the medium, because {{c1::lactose cannot enter the cell}}',
  'Sem permease a lactose não entra, não vira alolactose e o repressor continua no operador. A β-galactosidase em si continua funcional.','M-mutantes','lactose'),
 ('diploide-laci','In a partial diploid, <i>lacI</i><sup>−</sup> is {{c1::recessive}}: the wild-type repressor diffuses and represses both copies of the operon',
  'Diploide parcial (merozigoto) = segunda cópia do operon num plasmídeo (F′), transferida por conjugação. A regulação volta ao normal, induzível: o repressor age em <i>trans</i>.','M-diploide','diploide-lacI'),
 ('diploide-oc','In a partial diploid, an O<sup>c</sup> operator mutation is {{c1::dominant}} but only switches on the genes on its {{c2::own DNA molecule}} (cis)',
  'O<sup>c</sup> não liga o repressor: a cópia com O<sup>c</sup> é constitutiva e a cópia O<sup>+</sup> segue induzível. Ex.: I<sup>+</sup> O<sup>c</sup> Z<sup>+</sup> / I<sup>+</sup> O<sup>+</sup> Z<sup>−</sup> faz β-gal sem indutor.','M-diploide','diploide-Oc'),
 ('iptg','Jacob–Monod-style experiments induce <i>lac</i> with IPTG, a lactose analog that is {{c1::not metabolized}} by the cell',
  'Como não é consumido, o IPTG mantém a indução constante e não vira glicose. Liga-se ao repressor como a alolactose.','M-ferramentas','iptg-merozigoto'),
 ('xgal','β-galactosidase cleaves X-gal into a blue product, so colonies expressing the <i>lac</i> operon turn {{c1::blue}}',
  'Colônias brancas = sem β-galactosidase ativa. Com IPTG + X-gal dá para ver na placa quem é induzível, constitutivo ou não induzível.','M-ferramentas','xgal-placa'),
 ('hth','The Lac repressor, a tetramer, grips the palindromic operator through an N-terminal {{c1::helix-turn-helix}} motif',
  'Cada dímero liga uma metade do palíndromo no sulco maior. O indutor liga-se no centro da proteína e desorganiza o HTH: o repressor é uma proteína alostérica sensora do ambiente.','L-repressor','hth'),
 ('basal','Even when repressed, the <i>lac</i> operon keeps a low {{c1::basal}} transcription, so a few permeases let the first lactose in',
  'O repressor se solta e volta ao operador de tempos em tempos. Sem essa expressão basal a lactose não entraria e nunca haveria alolactose para induzir.','L-repressor','basal'),
 ('sigma','The σ subunit of bacterial RNA polymerase recognizes the promoter boxes at {{c1::−10}} and {{c1::−35}}',
  'Consensos: −10 = TATAAT e −35 = TTGACA, separados por ~17 pb. Quanto mais o promotor se afasta do consenso, mais fraco ele é.','P-promotor','sigma'),
 ('cap-recruta','The <i>lac</i> promoter is weak, so CAP–cAMP activates it by {{c1::recruiting RNA polymerase}} to the promoter',
  'O promotor lac difere do consenso (−35 TTTACA; −10 TATGTT). A CAP liga-se logo acima (5′) do promotor e toca a subunidade α da RNA polimerase, mantendo-a no promotor.','L-cap','cap-rnap'),
]
ROSA_AUTH={'jacob-monod','hth'}
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
    plan={'lesson_id':LESSON,'target_deck':DECK,'media':MEDIA,'lesson_date':'2026-09-08','profile_evidence':call('getMediaDirPath'),
      'entries':entries,'associate_existing':assoc,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'AnKing-MCAT':t('AnKing-MCAT'),'Autoral':t('Autoral'),
                'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'] and not x['pink']),
                'pink':sum(x['expected_cards'] for x in entries if x['pink']),'associated_existing_notes':len(assoc),
                'aula':sum(x['expected_cards'] for x in entries),'alem':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(plan['totals'],ensure_ascii=False,indent=2))
    for e in entries: print(e['key'],e['expected_cards'],e['copy_changes'])
if __name__=='__main__': main()
