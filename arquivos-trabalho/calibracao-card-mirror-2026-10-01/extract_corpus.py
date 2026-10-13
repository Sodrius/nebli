#!/usr/bin/env python3
"""Read-only, deterministic, note-level extraction; never touches the Anki DB."""
import sqlite3,re,json,html,hashlib,random,statistics,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parent
DB=Path('/Users/davisousa/Library/Application Support/Anki2/User 1/collection.anki2')
rng=random.Random(20261001)
def plain(s):
 s=re.sub(r'<[^>]+>',' ',s)
 return re.sub(r'\s+',' ',html.unescape(s)).strip()
def normalized(s):
 s=re.sub(r'\{\{c\d+::','{{c::',plain(s).casefold())
 return re.sub(r'[^\w]+',' ',s).strip()
def family(text,tags):
 t=plain(text).casefold(); g=tags.casefold()
 if re.search(r'calculate|calcula|equation|equação|(?:parkland|henderson|fick|winter|cockcroft).{0,20}formula|\bsensitivity\b|\bspecificity\b|odds ratio|relative risk|compared to|versus|\bvs\.?\b|::increase[sd]?/decrease|::aumenta/diminui',t): return 'calculos_comparacoes'
 if re.search(r'histolog|histologia|microscopic|microscóp|epithel|epitél|goblet|paneth|keratin|camada|\bstain\b|\bstaining\b',t): return 'histologia'
 if re.search(r'innervat|inerva|artery|artéria|\bnerve\b|\bnervo\b|ligament|foramen|anatomic|anatomia|anatomy|insertion|origin of (?:the |a )?(?:muscle|artery|nerve)|origem do|drains into|drenagem|anterior to|posterior to|boundary|boundaries',t): return 'anatomia'
 if re.search(r'biochem|bioquím|::metabolism|metaboli|glycolysis|glicólise|krebs|operon|amino.acid|aminoácido|glycogen|glicogênio|\bdna\b|\brna\b',t): return 'bioquimica'
 if re.search(r'::microbiology|::immunology|::pharmacology|microbiolog|imunolog|antibiotic|antibiótico|bacteri|virus|vírus|cytokine|citocina|complement|immun|imun|drug|medicamento|antagonist|agonist',t+' '+g): return 'micro_imuno_farma'
 if re.search(r'diagnos|diagnós|patient|paciente|treatment|tratamento|clinical|clínic|present[s ]|most likely|management|first.line|therapy|terapia',t): return 'clinica_diagnostico'
 if re.search(r'physiol|fisiol|mechanism|mecanismo|increas|decreas|aument|dimin|secret|secre|absorp|absorç|stimulat|estimul|pressure|pressão|receptor|transport',t+' '+g): return 'mecanismos_fisiologia'
 return 'fatos_listas'
def stats(rows):
 def summary(v):
  v=sorted(v)
  return {'median':statistics.median(v) if v else 0,'p10':v[int(len(v)*.1)] if v else 0,'p90':v[min(len(v)-1,int(len(v)*.9))] if v else 0}
 return {'notes':len(rows),'families':dict(collections.Counter(r['family'] for r in rows)), 'front_words':summary([len(plain(r['text']).split()) for r in rows]),'extra_words':summary([len(plain(r['extra']).split()) for r in rows]),'cloze_occurrences':summary([len(re.findall(r'\{\{c\d+::',r['text'])) for r in rows]),'distinct_cloze_ordinals':summary([len(set(re.findall(r'\{\{c(\d+)::',r['text']))) for r in rows]),'question_front':sum('?' in plain(r['text']) for r in rows),'bold_front':sum(bool(re.search(r'<(?:b|strong)[ >]',r['text'])) for r in rows),'underline_front':sum('<u>' in r['text'] for r in rows),'hint_front':sum(bool(re.search(r'\{\{c\d+::(?:(?!\}\}).)*::',r['text'])) for r in rows),'front_image':sum('<img' in r['text'].lower() for r in rows),'extra_image':sum('<img' in r['extra'].lower() for r in rows),'extra_nonempty':sum(bool(plain(r['extra']) or '<img' in r['extra'].lower()) for r in rows)}
def dump(name,data): (ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def main():
 c=sqlite3.connect(DB.as_uri()+'?mode=ro',uri=True)
 c.create_collation('unicase',lambda a,b:(a.casefold()>b.casefold())-(a.casefold()<b.casefold()))
 c.execute('PRAGMA query_only=ON')
 fields=collections.defaultdict(dict)
 for mid,idx,name in c.execute('SELECT ntid,ord,name FROM fields'): fields[mid][name]=idx
 nt=dict(c.execute('SELECT id,name FROM notetypes'))
 decks=dict(c.execute('SELECT id,name FROM decks'))
 roots=[d for d,n in decks.items() if n=='NEBLI (1774)' or n.startswith('NEBLI (1774)\x1f')]
 populations={}; rawstats={}
 for origin,dids,tag in [('AnKing',[1782836097813],None),('Autoral',roots,'NEBLI::origem::Autoral')]:
  sql='SELECT DISTINCT n.id,n.mid,n.tags,n.flds FROM notes n JOIN cards c ON c.nid=n.id WHERE c.did IN ('+','.join('?'*len(dids))+')'
  rows=[]; io=[]
  for nid,mid,tags,flds in c.execute(sql,dids):
   if tag and tag not in tags.split(): continue
   f=flds.split('\x1f'); m=fields[mid]
   def val(*names):
    for name in names:
     if name in m and m[name]<len(f): return f[m[name]]
    return ''
   text=val('Text','Front','Header'); extra=val('Extra','Back','Remarks')
   isio='occlusion' in nt[mid].lower() or ('Image' in m and 'Question Mask' in m)
   row={'id':str(nid),'origin':origin,'family':'image_occlusion' if isio else family(text,tags),'text':text,'extra':extra,'group_id':hashlib.sha256(normalized(text).encode()).hexdigest()[:20],'source_tags':tags.split(),'notetype':nt[mid]}
   (io if isio else rows).append(row)
  populations[origin]=rows
  dump(('anking' if origin=='AnKing' else 'authors')+'-io-separated.json',io)
  rawstats[origin]={'all_text_types':stats(rows),'io_notes':len(io)}
 # Conservative: exclude all front media/deictic visuals, not just known IO note types.
 natives=[r for r in populations['AnKing'] if '{{c' in r['text'] and not re.search(r'<img|\[sound:|shown (?:below|above)|image (?:below|above)|following (?:image|figure)|pictured|shown here',r['text'],re.I)]
 unique={}
 for r in natives: unique.setdefault(r['group_id'],r)
 buckets=collections.defaultdict(list)
 for r in unique.values():buckets[r['family']].append(r)
 for b in buckets.values():rng.shuffle(b)
 # 60 per category = 480 examples. All splits note+normalized-text disjoint.
 allocations=[('calibration.json',16),('authoring-reference.json',10),('native-reserve.json',18),('untouched-validation.json',16)]
 sets={name:[] for name,_ in allocations}
 for fam,bucket in sorted(buckets.items()):
  assert len(bucket)>=60,(fam,len(bucket))
  offset=0
  for name,n in allocations:
   sets[name].extend(bucket[offset:offset+n]);offset+=n
 # Frozen v2 provenance repair: preserve original positions, no reseed after exposure.
 repair={'1474253654941':'1581193044398','1474253687945':'1467771968226','1472435681635':'1488680231742','1474253845687':'1581190590300','1474253729885':'1516929150126','1474253780893':'1509235247004','1474253821570':'1475704133477','1474253707546':'1467683854499','1472435698856':'1467833724957'}
 lookup={r['id']:r for r in populations['AnKing']}
 def local_modified(r): return 'nebli' in r['notetype'].lower() or any('nebli' in t.lower() for t in r['source_tags'])
 for name,rows in sets.items():
  rng.shuffle(rows)
  rows[:]=[lookup[repair[r['id']]] if r['id'] in repair else r for r in rows]
  assert not any(local_modified(r) for r in rows)
  dump(name,rows)
 rawstats['AnKing']['excluded_nebli_notetype_or_tags']=sum(local_modified(r) for r in populations['AnKing'])
 populations['AnKing']=[r for r in populations['AnKing'] if not local_modified(r)]
 rawstats['AnKing']['all_text_types']=stats(populations['AnKing'])
 natives=[r for r in natives if not local_modified(r)]
 unique={r['group_id']:r for r in natives}
 dev=[];holdout=[]
 for fam in sorted(buckets):
  rows=[r for r in sets['native-reserve.json'] if r['family']==fam]
  dev.extend(rows[:8]);holdout.extend(rows[8:])
 holdout.extend(sets['untouched-validation.json'])
 dump('native-dev.json',dev);dump('native-holdout.json',holdout)
 authors=populations['Autoral'];dump('authors-existing.json',authors)
 selected=[r for rows in sets.values() for r in rows];dump('corpus-anking-480.json',selected)
 rawstats['AnKing']['eligible_text_notes']=len(natives);rawstats['AnKing']['unique_eligible_groups']=len(unique)
 rawstats['AnKing']['eligible_family_population']=dict(collections.Counter(r['family'] for r in unique.values()))
 rawstats['sample_480']=stats(selected);rawstats['splits']={name:stats(rows) for name,rows in sets.items()}
 rawstats['scope']={'database':str(DB),'read_only':True,'native_card_dids':[1782836097813],'authors_deck_root':'NEBLI (1774)','authors_tag':'NEBLI::origem::Autoral','seed':20261001,'unit':'note; sibling cards never split','family_assignment':'heuristic; manual audit necessary','front_media_excluded':True}
 dump('population-statistics.json',rawstats)
 study=sets['authoring-reference.json'][:64]+authors[:40]
 (ROOT/'reading-sample.txt').write_text('\n\n'.join(f"{r['origin']} {r['id']} {r['family']}\nTEXT {plain(r['text'])}\nEXTRA {plain(r['extra'])[:1800]}" for r in study))
 print(json.dumps({k:len(v) for k,v in sets.items()}|{'authors':len(authors),'native_population':len(populations['AnKing']),'eligible':len(natives),'io_authors':rawstats['Autoral']['io_notes']},ensure_ascii=False))
 c.close()
if __name__=='__main__':main()
