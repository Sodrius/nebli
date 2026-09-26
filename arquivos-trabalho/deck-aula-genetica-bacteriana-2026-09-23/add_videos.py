"""Vídeos dos canais preferidos de Davi no campo Additional Resources das cópias (pedido 23/09/2026).
Todos os links tiveram canal/título conferidos via oEmbed e capítulos via página do vídeo."""
import json,sys
from datetime import datetime,timezone
from inventory import call
from prepare import ROOT,DECK
sys.stdout.reconfigure(encoding='utf-8')
def yt(vid,t,label):
    url=f'https://www.youtube.com/watch?v={vid}'+(f'&t={t}s' if t else '')
    return f'<a href="{url}">{label}</a>'
NN='mg6tXQaiBaI'
V={
 'nn_overview':yt(NN,39,'Ninja Nerd — Bacterial Genetics (visão geral, 0:39)'),
 'nn_conj':yt(NN,147,'Ninja Nerd — Bacterial Genetics: conjugação (2:27)'),
 'nn_transf':yt(NN,869,'Ninja Nerd — Bacterial Genetics: transformação (14:29)'),
 'nn_transd':yt(NN,1171,'Ninja Nerd — Bacterial Genetics: transdução (19:31)'),
 'nn_transp':yt(NN,1832,'Ninja Nerd — Bacterial Genetics: transposição (30:32)'),
 'shomu_hfr':yt('Hio0Hys_UaU',0,"Shomu's Biology — Bacterial Conjugation: Hfr, F prime and F plasmid (16 min)"),
 'shomu_tn':yt('VD06Cx_RQe4',0,"Shomu's Biology — Composite and noncomposite transposons (10 min)"),
 'medicosis_rep':yt('_IIAeNgelaA',0,'Medicosis Perfectionalis — DNA replication in Prokaryotes & Eukaryotes (33 min)'),
 'dave_crispr':yt('IiPL5HgPehs',0,'Professor Dave Explains — CRISPR-Cas9 (14 min; início: origem na imunidade bacteriana)'),
}
BY_OBJ={
 'G1-nucleoide':['nn_overview'],'G2-plasmideos':['nn_overview'],
 'G3-superenovelamento':['medicosis_rep'],'G3-quinolonas-ponte':['medicosis_rep'],
 'R1-origem':['medicosis_rep'],'R2-maquinaria':['medicosis_rep'],
 'T1-transformacao':['nn_transf'],'T2-transducao':['nn_transd'],
 'T3-conjugacao':['nn_conj','shomu_hfr'],'T4-transposons':['nn_transp','shomu_tn'],
 'M3-resistencia':['nn_transp'],'C1-crispr':['dave_crispr'],
}
def log(action,value):
    with (ROOT/'journal.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'action':action,'value':value},ensure_ascii=False)+'\n')
r=json.load(open(ROOT/'receipt.json',encoding='utf-8'))
done=0
for x in r['results']:
    keys=BY_OBJ.get(x['objective'])
    if not keys: continue
    n=call('notesInfo',notes=[x['new_nid']])[0]
    if any(c['reps'] for c in call('cardsInfo',cards=n['cards'])): raise RuntimeError(f"Já estudado {x['new_nid']}")
    new='<br>'.join(V[k] for k in keys)
    old=n['fields']['Additional Resources']['value']
    if old==new: continue
    call('updateNoteFields',note={'id':x['new_nid'],'fields':{'Additional Resources':new}})
    if call('notesInfo',notes=[x['new_nid']])[0]['fields']['Additional Resources']['value']!=new: raise RuntimeError('readback')
    log('add_videos',{'nid':x['new_nid'],'objective':x['objective'],'before':old,'after':new}); done+=1
print('notas com vídeo:',done,'de',len(r['results']))
