"""Gera dry-run do deck corrigido sem escrever no Anki."""
import hashlib, json, re, sys
from pathlib import Path
HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parents[1]))
from nebli.decks import Anki
from refacao_spec import SOURCES, AUTHORS

A=Anki(); LESSON='UC19::P1::FA01'; SHORT='uc19p1fa01'; RUN='2026-uc19-p1-fa01-refacao';
DECK='NEBLI::UC19::P1::Farmacologia::Introdução à farmacologia e mecanismos de ação'
MODEL='NEBLI AnKing independente - v3'
CLOZE=re.compile(r'\{\{c(\d+)::((?:(?!\}\}).)*?)(?:::((?:(?!\}\}).)*?))?\}\}',re.S)
def sha(x): return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:16]
def simplify(text,keep):
 return CLOZE.sub(lambda m:m.group(0) if int(m.group(1)) in keep else m.group(2),text)
def group(slide):
 if slide<=24:return 'fundamentos'
 if slide<=38:return 'alvos_mecanismos'
 if slide<=52:return 'agonismo_curvas'
 if slide<=60:return 'antagonismo_seguranca'
 return 'alvos_aplicados'
def main():
 nids=sorted({x[2] for x in SOURCES}|{m for x in AUTHORS for m in x[5]})
 info={n['noteId']:n for n in A('notesInfo',notes=nids)}
 errors=[]; rows=[]
 for slide,key,nid,keep,flag,extra in SOURCES:
  n=info.get(nid)
  if not n: errors.append(f'{key}: fonte ausente {nid}');continue
  orig=n['fields'].get('Text',{}).get('value','')
  text=simplify(orig,set(keep)); found=sorted({int(x) for x in re.findall(r'\{\{c(\d+)::',text)})
  if found!=sorted(keep):errors.append(f'{key}: clozes {found} != {keep}')
  if re.search(r'\bslide\s*\d+',text+' '+extra,re.I):errors.append(f'{key}: bastidor visível')
  if re.search(r'<img\b',text,re.I):errors.append(f'{key}: imagem de fonte precisa revisão')
  if len(re.sub('<[^>]+>',' ',text).split())>75:errors.append(f'{key}: frente longa')
  origin='AnKing' if 'Referências::Anking Step Deck' in A('cardsInfo',cards=n['cards'][:1])[0]['deckName'] else 'Externo'
  if len(A('findNotes',query=f'"tag:NEBLI::source::nid-{nid}"')): errors.append(f'{key}: cópia existente de {nid}')
  rows.append({'slide':slide,'key':key,'src':nid,'origin':origin,'model':MODEL,'evid':f'Slide {slide}',
      'alvo':key.replace('_',' '),'bloco':group(slide),'fields':{'Text':text,'Extra':extra,'NEBLI_Comentario':''},
      'mirror_text':orig,'source_fields_hash':sha({k:v['value'] for k,v in n['fields'].items()}),
      'source_tags':n['tags'],'flags':{i:flag for i in keep},'kind':'text'})
 for slide,key,text,extra,flag,mirrors in AUTHORS:
  found=sorted({int(x) for x in re.findall(r'\{\{c(\d+)::',text)})
  if found!=[1]:errors.append(f'{key}: autoral cloze {found}')
  if len(mirrors)<2 or any(x not in info for x in mirrors):errors.append(f'{key}: espelhos precisam conferência')
  if re.search(r'\bslide\s*\d+',text+' '+extra,re.I):errors.append(f'{key}: bastidor visível')
  rows.append({'slide':slide,'key':key,'origin':'Autoral','model':MODEL,'evid':f'Slide {slide}',
      'alvo':key.replace('_',' '),'bloco':group(slide),'fields':{'Text':text,'Extra':extra,'NEBLI_Comentario':''},
      'espelhos':mirrors,'autoria':'central' if flag==3 else 'prova',
      'busca':'AnKing Step (conceito e sinônimos), AnKing-MCAT e demais Referências Externas; cartões encontrados foram usados como espelhos, mas não cobriam este contraste específico da lâmina.',
      'flags':{1:flag},'kind':'autoral'})
 rows.sort(key=lambda x:x['slide'])
 entries=[]
 for order,row in enumerate(rows,1):
  slide,key,origin=row['slide'],row['key'],row['origin']; flags=row.pop('flags'); base=row.pop('source_tags',[]);row.pop('mirror_text',None)
  tags=[f'NEBLI::{LESSON}','NEBLI::escopo::aula',f'NEBLI::objetivo::{row["bloco"]}',f'NEBLI::ordem::{SHORT}-{order:03d}',f'NEBLI::run::{RUN}',f'NEBLI::origem::{origin}']
  tags.append(f'NEBLI::source::nid-{row["src"]}' if row.get('src') else f'NEBLI::author::{SHORT}-{key}')
  colors={3:'verde',4:'azul',5:'rosa'}
  tags += [f'NEBLI::cor::{LESSON}::{colors[v]}' for v in set(flags.values())]
  row.update(order=order,tags=sorted(set(base+tags)),fields_hash=sha(row['fields']),cards=[{'n':n,'ord':n-1,'flag':flag,'cor':colors[flag]} for n,flag in sorted(flags.items())])
  entries.append(row)
 n_cards=sum(len(x['cards']) for x in entries); n_aut=sum(len(x['cards']) for x in entries if x['origin']=='Autoral')
 if n_aut/n_cards>0.15:errors.append(f'Autoria {n_aut}/{n_cards} > 15%')
 if len({x['key'] for x in entries})!=len(entries):errors.append('chaves duplicadas')
 if A('findNotes',query=f'"tag:NEBLI::{LESSON}"'):errors.append('aula já instalada')
 totals={'notas':len(entries),'cards':n_cards,'verdes':sum(c['flag']==3 for e in entries for c in e['cards']),
  'azuis':sum(c['flag']==4 for e in entries for c in e['cards']), 'rosas':sum(c['flag']==5 for e in entries for c in e['cards']),
  'origens_notas':{v:sum(e['origin']==v for e in entries) for v in sorted(set(e['origin'] for e in entries))},
  'origens_cards':{v:sum(len(e['cards']) for e in entries if e['origin']==v) for v in sorted(set(e['origin'] for e in entries))}}
 plan={'run_id':RUN,'short':SHORT,'lesson_id':LESSON,'deck':DECK,'criterios':'Aula completa; exemplos ligados aos princípios; AnKing primeiro; bandeiras por valor longitudinal/prova; sem E1.',
  'busca_externos':'busca-externos.md',
  'E1':'não solicitada','entries':entries,'compartilhados':{},'excluidos':[], 'fora_do_recorte':['história 4–8 e 10–15 conforme pedido','farmacocinética quantitativa de aulas posteriores'],
  'media':{},'clones':{},'totais':totals}
 plan['selection_hash']=sha([(x['key'],x['fields_hash'],x['cards']) for x in entries])
 if not errors:(HERE/'plan-refacao.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
 print(json.dumps({'totais':totals,'autoral_pct':round(100*n_aut/n_cards,1),'errors':errors},ensure_ascii=False,indent=2))
 if errors:raise SystemExit(1)
if __name__=='__main__':main()
