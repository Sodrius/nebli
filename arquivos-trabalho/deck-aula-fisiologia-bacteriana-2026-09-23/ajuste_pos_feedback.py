"""Ajuste pós-feedback de Davi (23/09/2026, tarde): vídeos saem dos cards (vão no chat),
entram cards AnKing recusados/perdidos na 1ª busca, autorais encolhem, +1 autoral de sal."""
import base64,hashlib,json,re,sys
from datetime import datetime,timezone
from inventory import call
from prepare import ROOT,DECK,LESSON,HY,img,clean_resources,uncloze,clozes,digest
sys.stdout.reconfigure(encoding='utf-8')
TAG=f'NEBLI::{LESSON}'; MODEL='NEBLI AnKing independente - v3'
J=ROOT/'journal.jsonl'
def log(a,v):
    with J.open('a',encoding='utf-8') as f: f.write(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'action':a,'value':v},ensure_ascii=False)+'\n')
def set_fields(nid,fields):
    call('updateNoteFields',note={'id':nid,'fields':fields})
    now={k:v['value'] for k,v in call('notesInfo',notes=[nid])[0]['fields'].items()}
    for k,v in fields.items():
        if now[k]!=v: raise RuntimeError(f'readback {nid} {k}')

# ---------- backup ----------
deck_nids=call('findNotes',query=f'"deck:{DECK}"')
video_nids=call('findNotes',query='deck:NEBLI* "Additional Resources:*youtu*"')
backup={'deck_notes':call('notesInfo',notes=deck_nids),'video_notes':call('notesInfo',notes=video_nids)}
(ROOT/'before-ajuste-2026-09-23.json').write_text(json.dumps(backup,ensure_ascii=False,indent=1),encoding='utf-8')
if any(c['reps'] for c in call('cardsInfo',cards=call('findCards',query=f'"deck:{DECK}"'))): raise RuntimeError('deck já estudado')

# ---------- 1. vídeos fora dos cards (Fisiologia + Genética) ----------
gen_before={}
for l in (ROOT.parent/'deck-aula-genetica-bacteriana-2026-09-23'/'journal.jsonl').open(encoding='utf-8'):
    j=json.loads(l)
    if j['action']=='add_videos': gen_before[j['value']['nid']]=j['value']['before']
for n in backup['video_notes']:
    old=n['fields']['Additional Resources']['value']
    new=gen_before.get(n['noteId'])
    if new is None:
        new=re.sub(r'<a [^>]*youtu[^>]*>.*?</a>','',old)
        new=re.sub(r'^(\s*<br\s*/?>)+|(<br\s*/?>\s*)+$','',new).strip()
    if 'youtu' in new: raise RuntimeError(n['noteId'])
    set_fields(n['noteId'],{'Additional Resources':new}); log('remove_video',{'nid':n['noteId'],'before':old,'after':new})

# ---------- 2. autorais menores ----------
AUTH={
 1790173050138:('Grouped by optimal temperature: cold → {{c1::psychrophiles}}; ~37 °C (most pathogens) → {{c1::mesophiles}}; hot → {{c1::thermophiles}}',
   'Acima de ~80 °C: hipertermófilos. A maioria dos patógenos também prefere pH neutro (~7).'+img('nebli-fisio-temperatura.png')),
 1790173050491:('Host sequestration of iron is called {{c1::nutritional immunity}}; bacteria counter it with {{c2::siderophores}}',
   'Ferro baixo ativa, via proteína Fur, genes de captação de ferro e de virulência.'+img('nebli-fisio-ferro.png')),
 1790173050816:('Final electron acceptor — anaerobic respiration: {{c1::inorganic (NO<sub>3</sub><sup>−</sup>, SO<sub>4</sub><sup>2−</sup>)}}; fermentation: {{c2::organic (e.g., pyruvate)}}',
   'Fermentação: ATP só por fosforilação no nível do substrato (2 ATP/glicose).'+img('nebli-fisio-fermentacao.png')),
 1790173051166:('Doubling time: <i>E. coli</i> ≈ {{c1::20 min}}; <i>M. tuberculosis</i> ≈ {{c2::18–24 h}}',
   'Por isso a cultura de <i>M. tuberculosis</i> leva semanas.'+img('nebli-fisio-curva.png')),
 1790173051524:('In <i>S. aureus</i>, secreted toxins peak in the {{c1::stationary}} phase (adhesins: exponential)',
   'Adesinas (fator <i>clumping</i>, proteína A) na fase log; coagulase e toxinas na transição para a estacionária.'+img('nebli-fisio-virulencia-fases.png')),
 1790173051815:('Streaking across successive areas of an agar plate yields {{c1::isolated colonies}}',
   'Cada colônia vem de uma única célula. Incubação típica: 37 °C por 24 h.'+img('nebli-fisio-esgotamento.png')),
}
for nid,(text,extra) in AUTH.items():
    n=call('notesInfo',notes=[nid])[0]
    if TAG not in n['tags'] or not any(t.startswith('NEBLI::author::') for t in n['tags']): raise RuntimeError(f'não é autoral desta aula {nid}')
    if set(clozes(text))-set(clozes(n['fields']['Text']['value'])): raise RuntimeError(f'cloze novo {nid}')
    set_fields(nid,{'Text':text,'Extra':extra,'Additional Resources':''})
    log('shrink_authored',{'nid':nid,'before':n['fields']['Text']['value'],'after':text})

# ---------- 3. mídia + autoral novo (sal) ----------
call('storeMediaFile',filename='nebli-fisio-sal.png',data=base64.b64encode((ROOT/'img'/'p9_sal.png').read_bytes()).decode())
NEW_AUTH=[('sal','Tolerates salt but does not need it: {{c1::halotolerant}} (e.g., <i>S. aureus</i>); requires salt: {{c1::halophile}}',
  'Halófilos extremos exigem 15–30% de NaCl; <i>E. coli</i> é não halófila.'+img('nebli-fisio-sal.png'),'N-ambiente')]
results=[]
fields_all=call('modelFieldNames',modelName=MODEL)
for key,text,extra,obj in NEW_AUTH:
    k='authored-'+key
    if call('findNotes',query=f'tag:"NEBLI::author::{k}"'): raise RuntimeError('já existe '+k)
    f={x:'' for x in fields_all}; f.update({'Text':text,'Extra':extra})
    nid=call('addNote',note={'deckName':DECK,'modelName':MODEL,'fields':f,'tags':[TAG,f'NEBLI::objetivo::{obj}','NEBLI::origem::Autoral',f'NEBLI::author::{k}'],'options':{'allowDuplicate':True}})
    cards=call('notesInfo',notes=[nid])[0]['cards']
    r={'key':k,'source_nid':None,'new_nid':nid,'cards':cards,'origin':'Autoral','objective':obj,'high_yield':False}; results.append(r); log('created',r)

# ---------- 4. AnKing que deveriam ter entrado ----------
SRC={
 1487642782702:('N-ferro',[('set','Extra','Exemplo de imunidade nutricional: o hospedeiro sequestra o ferro (transferrina, lactoferrina, ferritina).')]),
 1478973207060:('N-ferro',[('set','Extra','Degrada a ferroportina e retém o ferro em macrófagos e enterócitos: outro braço da imunidade nutricional.')]),
 1487642726245:('O2-classes',[('replace','Text',' (oxidative burst)',''),('append','Extra','Anaeróbios estritos não têm SOD nem catalase; por isso o O<sub>2</sub> os mata.')]),
 1487470255062:('O2-classes',[]),
 1503250260788:('C-curva',[('set','Extra','Reflete o tempo de duplicação de ~18–24 h (<i>E. coli</i>: ~20 min).')]),
 1500673014315:('C-curva',[]),
 1500496166406:('M-meios',[]),
 1500498676105:('E-energia',[('uncloze',[1]),('set','Extra','Na aula: bactérias láticas convertem glicose → lactato (ou lactato + etanol).')]),
}
src=call('notesInfo',notes=list(SRC)); hashes={n['noteId']:digest(n['fields']) for n in src}
for n in src:
    nid=n['noteId']; obj,edits=SRC[nid]
    if call('findNotes',query=f'tag:"NEBLI::source::nid-{nid}"'): raise RuntimeError(f'cópia já existe {nid}')
    f={k:v['value'] for k,v in n['fields'].items()}
    for e in edits:
        if e[0]=='set': f[e[1]]=e[2]
        elif e[0]=='append': f[e[1]]=(f[e[1]]+'<br>' if f[e[1]].strip() else '')+e[2]
        elif e[0]=='replace':
            if e[2] not in f[e[1]]: raise RuntimeError(f'trecho ausente {nid}: {f[e[1]]}')
            f[e[1]]=f[e[1]].replace(e[2],e[3])
        elif e[0]=='uncloze': f['Text']=uncloze(f['Text'],set(e[1]))
    clean_resources(f)
    if 'ankihub_id' in f: f['ankihub_id']=''
    tags=list(dict.fromkeys(n['tags']+[TAG,f'NEBLI::objetivo::{obj}','NEBLI::origem::AnKing',f'NEBLI::source::nid-{nid}']))
    new=call('addNote',note={'deckName':DECK,'modelName':MODEL,'fields':f,'tags':tags,'options':{'allowDuplicate':True}})
    note=call('notesInfo',notes=[new])[0]
    if len(note['cards'])!=len(clozes(f['Text'])): raise RuntimeError(f'contagem {nid}')
    hy=HY in n['tags']
    if hy:
        for cid in note['cards']: call('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[3],warning_check=True)
    r={'key':f'source-{nid}','source_nid':nid,'new_nid':new,'cards':note['cards'],'origin':'AnKing','objective':obj,'high_yield':hy}; results.append(r); log('created',r)
for n in call('notesInfo',notes=list(SRC)):
    if digest(n['fields'])!=hashes[n['noteId']]: raise RuntimeError('fonte alterada')

# ---------- 5. recibo + APKG ----------
rc=json.loads((ROOT/'receipt.json').read_text(encoding='utf-8'))
rc['results']+=results
cards=call('findCards',query=f'"deck:{DECK}"')
pkg=ROOT/'Fisiologia bacteriana.apkg'
if not call('exportPackage',deck=DECK,path=str(pkg.resolve()),includeSched=True): raise RuntimeError('export')
green=call('findCards',query=f'"deck:{DECK}" flag:3')
rc.update({'at':datetime.now(timezone.utc).isoformat(),'notes':len(rc['results']),'cards':len(cards),'green':len(green),
           'package_sha256':hashlib.sha256(pkg.read_bytes()).hexdigest(),'ajuste_2026_09_23':'vídeos removidos; +8 AnKing; autorais encolhidos; +1 autoral sal'})
(ROOT/'receipt.json').write_text(json.dumps(rc,ensure_ascii=False,indent=2),encoding='utf-8')
p=json.loads((ROOT/'plan.json').read_text(encoding='utf-8'))
(ROOT/'plan-v1.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
p['totals'].update({'notes':len(rc['results']),'cards':len(cards),'HY_green':len(green)})
(ROOT/'plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
log('ajuste_complete',{'notes':len(rc['results']),'cards':len(cards),'green':len(green)})
print('notas',len(rc['results']),'cards',len(cards),'verdes',len(green),'vídeos restantes',len(call('findNotes',query='deck:NEBLI* "Additional Resources:*youtu*"')))
