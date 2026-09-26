# GR2 v2 (25/09): refeito a partir do Drive (pasta "21 - Grand Round 2": slides + caso clínico da Dra. Sharon Admoni)
# + provas antigas UC03 (GR 2024 P1 2.9 AGEs; BQ 2023 DM1xDM2; BQ/BM 2017 sinalização da insulina; PT 2024 pé diabético).
# Atualização incremental do deck vivo (sem rodar scripts de criação antigos): +9 AnKing, +3 autorais, +2 associações, -1 autoral (LADA).
import argparse, hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from inventory import call

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).parent
LESSON = '2026-uc03-grand-round-21-grand-round-2-diabetes'
DECK = 'NEBLI::UC03::P2::Grand Round::Grand Round 2 (diabetes mellitus)'
TAG = f'NEBLI::{LESSON}'
LOCK = ROOT.parent / 'ANKI-ESCRITA.lock'
HY = '#AK_Step1_v12::#Low/HighYield::1-HighYield'
SRC = 'AnKingOverhaul (AnKing Step Deck / AnKingMed)'
TGT = 'NEBLI AnKing independente - v3'
RESOURCE_FIELDS = ['Lecture Notes', 'Missed Questions', 'Pathoma', 'Boards and Beyond', 'First Aid', 'Sketchy', 'Sketchy 2',
                   'Sketchy Extra', 'Picmonic', 'Pixorize', 'Physeo', 'Bootcamp', 'OME', 'Additional Resources']
ADD = {1487550549393: 'D-pancreas', 1462327031605: 'D-pancreas', 1584134939832: 'D-dm2', 1584133969374: 'D-dm2',
       1462327651340: 'C-osmotica', 1462128108324: 'D-insulina', 1472435639812: 'D-insulina', 1475452928405: 'C-nefro',
       1462913162803: 'T-tratamento'}
EDITS = {  # nid -> [(regex, repl)] aplicados ao Extra da cópia
    1487550549393: [(r'^Amylin is derived from <b>insulin<br></b>',
                     'Amylin is <b>co-secreted with insulin</b> by β cells (it is not derived from insulin)<br>')],
    1472435639812: [(r' Purchase full textbook <a href="https://physeo\.com/textbooks/">here</a>\.', '')],
}
ASSOC = {1790264484331: 'D-insulina', 1790266074877: 'D-dm2'}
DELETE = {1790266493982: 'LADA: nem o slide nem o caso do Drive falam em LADA; o paciente (26 a, anti-GAD65+, insulina desde o '
                         'diagnóstico) é DM1 autoimune. Anti-GAD e peptídeo C já têm cards AnKing.'}
SLIDE = 'Fonte: slides do Grand Round 2 (UC03)'
MEDIA = [('img/p9-0.png', 'nebli-gr2-lipotox.png'), ('img/p17-0.png', 'nebli-gr2-membrana-basal.png')]


def img(f):
    return f'<br><br><img src="{f}"><br><i><span style="font-size: 10pt;">{SLIDE}</span></i>'


AUTH = [
    ('gr2-lipotox', 'Lipotoxic muscle: DAG and ceramide activate {{c1::serine}} kinases that block insulin receptor signaling and GLUT4',
     'É o elo entre obesidade visceral (mais ácidos graxos circulando) e resistência à insulina no músculo, na DM2.' + img('nebli-gr2-lipotox.png'),
     'D-insulina'),
    ('gr2-age-colageno', 'AGE cross-links make collagen resist {{c1::proteolysis}}, thickening basement membranes and trapping plasma proteins',
     'Por isso a membrana basal capilar engrossa (rim, retina) e a cicatrização piora; na parede arterial, o colágeno glicado retém LDL.'
     + img('nebli-gr2-membrana-basal.png'), 'C-age'),
    ('gr2-age-no', 'AGEs {{c1::inactivate nitric oxide}}, impairing endothelium-dependent vasodilation in diabetes',
     'Somado à oxidação lipídica que os AGEs induzem, leva à disfunção endotelial que abre caminho para a aterosclerose.', 'C-age'),
]


def digest(v):
    return hashlib.sha256(json.dumps(v, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def nclz(t):
    return len(set(re.findall(r'{{c(\d+)::', t)))


def build():
    out = []
    for n in call('notesInfo', notes=list(ADD)):
        if n['modelName'] != SRC:
            raise RuntimeError(f"modelo inesperado {n['noteId']}")
        f = {k: v['value'] for k, v in n['fields'].items()}
        for k in RESOURCE_FIELDS:
            if k in f:
                f[k] = ''
        f['ankihub_id'] = ''
        for rx, rp in EDITS.get(n['noteId'], []):
            new = re.sub(rx, rp, f['Extra'], flags=re.S)
            if new == f['Extra']:
                raise RuntimeError(f"edit sem efeito {n['noteId']}")
            f['Extra'] = new
        obj = ADD[n['noteId']]
        out.append({'key': f"source-{n['noteId']}", 'source_nid': n['noteId'], 'fields_hash': digest(n['fields']), 'fields': f,
                    'objective': obj, 'origin': 'AnKing', 'hy': HY in n['tags'], 'cards': nclz(f['Text']),
                    'tags': list(dict.fromkeys(n['tags'] + [TAG, f'NEBLI::objetivo::{obj}', 'NEBLI::origem::AnKing',
                                                            'NEBLI::escopo::aula', f"NEBLI::source::nid-{n['noteId']}"]))})
    names = call('modelFieldNames', modelName=TGT)
    for key, text, extra, obj in AUTH:
        f = {k: '' for k in names}
        f.update({'Text': text, 'Extra': extra})
        out.append({'key': key, 'source_nid': None, 'fields': f, 'objective': obj, 'origin': 'Autoral', 'hy': False, 'cards': nclz(text),
                    'tags': [TAG, f'NEBLI::objetivo::{obj}', 'NEBLI::origem::Autoral', 'NEBLI::escopo::aula', f'NEBLI::author::{key}']})
    return out


def check(entries):
    issues = []
    for e in entries:
        idt = f"NEBLI::source::nid-{e['source_nid']}" if e['source_nid'] else f"NEBLI::author::{e['key']}"
        if call('findNotes', query=f'tag:"{idt}"'):
            issues.append(f'já existe {idt}')
    for nid in ASSOC:
        if not call('notesInfo', notes=[nid]):
            issues.append(f'associada ausente {nid}')
    for nid in DELETE:
        n = call('notesInfo', notes=[nid])[0]
        cs = call('cardsInfo', cards=n['cards'])
        if any(c['reps'] or c['type'] for c in cs):
            issues.append(f'nota a excluir já estudada {nid}')
        if [t for t in n['tags'] if t.startswith('NEBLI::2026')] != [TAG]:
            issues.append(f'nota a excluir pertence a outra aula {nid}')
        if any(c['flags'] != 0 for c in cs):
            issues.append(f'nota a excluir tem bandeira {nid}')
    if issues:
        raise RuntimeError('\n'.join(issues))


def apply(entries):
    with LOCK.open('x', encoding='utf-8') as fh:
        fh.write(json.dumps({'executor': 'Claude', 'aula': LESSON, 'at': datetime.now(timezone.utc).isoformat()}))
    journal = ROOT / 'journal.jsonl'

    def log(a, v):
        with journal.open('a', encoding='utf-8') as fh:
            fh.write(json.dumps({'at': datetime.now(timezone.utc).isoformat(), 'action': a, 'value': v}, ensure_ascii=False) + '\n')

    try:
        check(entries)
        before_cards = call('findCards', query=f'"deck:{DECK}"')
        nids = call('findNotes', query=f'tag:"{TAG}"')
        (ROOT / 'before-update.json').write_text(json.dumps({
            'notes': call('notesInfo', notes=nids), 'cards': call('cardsInfo', cards=before_cards),
            'delete': call('notesInfo', notes=list(DELETE)), 'assoc': call('notesInfo', notes=list(ASSOC))}, ensure_ascii=False), encoding='utf-8')
        if not call('exportPackage', deck=DECK, path=str((ROOT / 'before-update.apkg').resolve()), includeSched=True):
            raise RuntimeError('backup apkg falhou')
        log('backup', {'cards': len(before_cards), 'notes': len(nids)})
        for src, name in MEDIA:
            call('storeMediaFile', filename=name, path=str((ROOT / src).resolve()))
        green, res = [], []
        for e in entries:
            nid = call('addNote', note={'deckName': DECK, 'modelName': TGT, 'fields': e['fields'], 'tags': e['tags'],
                                        'options': {'allowDuplicate': True}})
            n = call('notesInfo', notes=[nid])[0]
            if {k: v['value'] for k, v in n['fields'].items()} != e['fields']:
                raise RuntimeError(f"campos divergentes {e['key']}")
            cs = call('cardsInfo', cards=n['cards'])
            if len(cs) != e['cards'] or any(c['deckName'] != DECK for c in cs):
                raise RuntimeError(f"cards divergentes {e['key']}")
            if e['hy']:
                green += [c['cardId'] for c in cs]
            res.append({'key': e['key'], 'new_nid': nid, 'cards': [c['cardId'] for c in cs]})
            log('created', res[-1])
        for cid in green:
            call('setSpecificValueOfCard', card=cid, keys=['flags'], newValues=[3], warning_check=True)
        for nid, obj in ASSOC.items():
            call('addTags', notes=[nid], tags=f'{TAG} NEBLI::objetivo::{obj}')
            log('associated', nid)
        for nid, why in DELETE.items():
            call('deleteNotes', notes=[nid])
            log('deleted', {'nid': nid, 'why': why})
        after = call('findCards', query=f'"deck:{DECK}"')
        exp = len(before_cards) + sum(e['cards'] for e in entries) - len(DELETE)
        if len(after) != exp:
            raise RuntimeError(f'total {len(after)} != {exp}')
        if call('findCards', query=f'"deck:{DECK}" is:suspended'):
            raise RuntimeError('suspenso inesperado')
        pkg = ROOT / 'Grand Round 2 (diabetes mellitus).apkg'
        if not call('exportPackage', deck=DECK, path=str(pkg.resolve()), includeSched=True):
            raise RuntimeError('export falhou')
        fl = {k: len(call('findCards', query=f'"deck:{DECK}" flag:{k}')) for k in (1, 2, 3, 4, 5)}
        rec = {'at': datetime.now(timezone.utc).isoformat(), 'deck': DECK, 'cards_before': len(before_cards), 'cards_after': len(after),
               'added': res, 'green_new': len(green), 'associated': list(ASSOC), 'deleted': DELETE, 'flags': fl,
               'notes_with_tag': len(call('findNotes', query=f'tag:"{TAG}"')),
               'package': str(pkg.resolve()), 'package_sha256': hashlib.sha256(pkg.read_bytes()).hexdigest()}
        (ROOT / 'receipt.json').write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding='utf-8')
        log('complete', {k: v for k, v in rec.items() if k != 'added'})
        print(json.dumps({k: v for k, v in rec.items() if k != 'added'}, ensure_ascii=False, indent=2))
    finally:
        LOCK.unlink(missing_ok=True)


def show(e):
    strip = lambda s: re.sub(r'\s+', ' ', re.sub(r'<img[^>]*>', '[IMG]', re.sub(r'<(?!img)[^>]+>', ' ', s)))
    print(e['key'], e['cards'], 'HY' if e['hy'] else '', '|', strip(e['fields']['Text'])[:160])
    print('    EXTRA:', strip(e['fields'].get('Extra', ''))[:420])


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('mode', choices=['plan', 'check', 'apply'])
    a = p.parse_args()
    E = build()
    if a.mode == 'plan':
        for e in E:
            show(e)
        print('total cards novos', sum(e['cards'] for e in E))
    elif a.mode == 'check':
        check(E)
        print('check ok', len(E), 'notas', sum(e['cards'] for e in E), 'cards')
    else:
        if LOCK.exists():
            sys.exit('lock ativo: ' + LOCK.read_text(encoding='utf-8'))
        apply(E)
