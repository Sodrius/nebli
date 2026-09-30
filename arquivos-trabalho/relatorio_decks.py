"""Relatório somente leitura por deck-aula: cards/notas, origem, bandeiras, estado de estudo e compartilhados.
Uso: python3 arquivos-trabalho/relatorio_decks.py "NEBLI::UC08"  (qualquer ramo canônico)"""
import sys, re, collections
sys.path.insert(0, '/Users/davisousa/NEBLI')
from nebli.decks import Anki
A = Anki(); ramo = sys.argv[1] if len(sys.argv) > 1 else 'NEBLI::UC08'
canon = lambda d: re.sub(r' \(\d+\)', '', d)
FLAG = {0: 'sem', 1: 'vermelha', 2: 'laranja', 3: 'verde', 4: 'azul', 5: 'rosa', 6: 'turquesa', 7: 'roxa'}
raw = {canon(d): d for d in A('deckNames') if canon(d).startswith(ramo + '::')}  # nomes vivos podem ter totais do add-on
decks = sorted(raw)
folhas = [d for d in decks if not any(o.startswith(d + '::') for o in decks)]
def origem(tags, model):
    for t in tags:
        if t.startswith('NEBLI::origem::'): return t.split('::')[-1]
    if any(t.startswith('NEBLI::author::') for t in tags): return 'Autoral'
    return 'AnKing' if 'AnKing' in model else model
tot = collections.Counter(); totf = collections.Counter(); toto = collections.Counter()
print(f"{'Deck':62} {'notas':>5} {'cards':>5}  origem (cards)  |  bandeiras  |  novos/estudo/susp  |  assoc.")
for d in folhas:
    cids = A('findCards', query=f'"deck:{raw[d]}"')
    if not cids: continue
    cards = [c for c in A('cardsInfo', cards=cids) if canon(c['deckName']) == d]
    notes = {n['noteId']: n for n in A('notesInfo', notes=list({c['note'] for c in cards}))}
    o = collections.Counter(origem(notes[c['note']]['tags'], c['modelName']) for c in cards)
    f = collections.Counter(FLAG.get(c['flags'], c['flags']) for c in cards)
    novos = sum(c['type'] == 0 for c in cards); susp = sum(c['queue'] == -1 for c in cards)
    lt = collections.Counter(t for n in notes.values() for t in n['tags'] if re.match(r'NEBLI::2026-uc\d\d-', t))
    lesson = lt.most_common(1)[0][0] if lt else None  # tag da própria aula = a mais frequente no deck
    assoc = len(set(A('findNotes', query=f'"tag:{lesson}"')) - set(notes)) if lesson else 0
    print(f"{d.split('::',2)[-1][:62]:62} {len(notes):5} {len(cards):5}  " + ', '.join(f'{k} {v}' for k, v in o.most_common())
          + '  |  ' + ', '.join(f'{k} {v}' for k, v in f.most_common()) + f'  |  {novos}/{len(cards)-novos}/{susp}  |  {assoc}')
    tot.update(cards=len(cards), notas=len(notes), novos=novos, susp=susp, assoc=assoc); totf.update(f); toto.update(o)
print(f"\nTOTAL {ramo}: {tot['notas']} notas, {tot['cards']} cards · origem: " + ', '.join(f'{k} {v}' for k, v in toto.most_common())
      + ' · bandeiras: ' + ', '.join(f'{k} {v}' for k, v in totf.most_common()) + f" · novos {tot['novos']}, estudados {tot['cards']-tot['novos']}, suspensos {tot['susp']} · notas associadas de outras aulas {tot['assoc']}")
