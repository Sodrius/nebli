"""Acrescenta imagem aos 6 autorais (pedido de Davi, 23/09/2026). Ordem de preferência: card AnKing > slide > internet."""
import base64,json,sys
from datetime import datetime,timezone
from pathlib import Path
from inventory import call
from prepare import ROOT
sys.stdout.reconfigure(encoding='utf-8')
CREDIT='<i><span style="font-size: 10pt;">{}</span></i>'
SLIDE=CREDIT.format('Fonte: slides da aula (Profa. Carla R. Taddei, ICB-USP)')
PLAN={
 'authored-nucleoide':(1790166177935,None,'92eb68430ae3f667d6a30e4979c8faa2.webp',
   CREDIT.format('Photo credit: <a href="https://openstax.org/books/biology-2e/pages/22-2-structure-of-prokaryotes-bacteria-and-archaea">OpenStax</a>, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>')),
 'authored-replicacao-theta':(1790166178285,'img/theta.png','nebli-genetica-theta.png',SLIDE),
 'authored-mutagenicos':(1790166178632,'img/intercalacao.png','nebli-genetica-intercalacao.png',
   'Esquerda: DNA normal; direita: intercalante (preto) entre pares de bases.<br>'+CREDIT.format('Photo credit: <a href="https://commons.wikimedia.org/wiki/File:DNA_intercalation.svg">Gigillo83</a>, public domain, via Wikimedia Commons')),
 'authored-origem-resistencia':(1790166178982,'img/p32_0.png','nebli-genetica-plasmideo-R.png',
   'Plasmídeo R: genes de resistência (cm<sup>R</sup>, kan<sup>R</sup>, tet<sup>R</sup>…) acumulados por transposons (Tn) flanqueados por IS.<br>'+SLIDE),
 'authored-restricao-extremidades':(1790166179295,'img/restricao-cortes.png','nebli-genetica-restricao-cortes.png',SLIDE),
 'authored-crispr-espacadores':(1790166179615,'img/p44_0.png','nebli-genetica-crispr.png',SLIDE),
}
def log(action,value):
    with (ROOT/'journal.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'action':action,'value':value},ensure_ascii=False)+'\n')
media=Path(call('getMediaDirPath'))
for key,(nid,src,name,caption) in PLAN.items():
    n=call('notesInfo',notes=[nid])[0]
    if f'NEBLI::author::{key}' not in n['tags']: raise RuntimeError(f'Identidade inesperada {nid}')
    if any(c['reps'] for c in call('cardsInfo',cards=n['cards'])): raise RuntimeError(f'Já estudado {nid}')
    extra=n['fields']['Extra']['value']
    if name in extra: print('já tem imagem',key); continue
    if src:
        call('storeMediaFile',filename=name,data=base64.b64encode((ROOT/src).read_bytes()).decode())
    if not (media/name).exists(): raise RuntimeError(f'Mídia ausente {name}')
    new=f'{extra}<br><br><img src="{name}"><br>{caption}'
    call('updateNoteFields',note={'id':nid,'fields':{'Extra':new}})
    if call('notesInfo',notes=[nid])[0]['fields']['Extra']['value']!=new: raise RuntimeError(f'Readback falhou {nid}')
    log('add_image_authored',{'key':key,'nid':nid,'media':name,'source':src or 'AnKing (1500404310045)','before':extra,'after':new})
    print('ok',key,name)
