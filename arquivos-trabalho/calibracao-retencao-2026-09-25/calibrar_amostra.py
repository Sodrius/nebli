"""Amostra explicitamente autorizada: cinco flags, sem alterar conteúdo/agendamento.

Execução única. Recusa novo apply se houver recibo; não é gerador de aula.
"""
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from nebli.preflight import ReadOnlyAnki, chunks

OUT = Path(__file__).resolve().parent
LOCK = ROOT / 'arquivos-trabalho/ANKI-ESCRITA.lock'
SAMPLE = {
    1790264436916: (0, 3, 'Filtração supera drenagem: mecanismo causal reutilizável.'),
    1790264436915: (0, 3, 'Reconhecer a função da linfa agrega alvo distinto ao balanço de filtração.'),
    1790264437008: (0, 3, 'Obstrução venosa e pressão hidrostática: mecanismo central.'),
    1790264437101: (0, 3, 'Perda de albumina e pressão oncótica: mecanismo central distinto.'),
    1790264437196: (0, 3, 'Permeabilidade na inflamação: terceiro mecanismo, não outra redação dos anteriores.'),
    1790264437298: (3, 3, 'Território pulmonar da congestão esquerda: manter recomendação.'),
    1790264437299: (3, 3, 'Débito/perfusão adiante da falha: consequência distinta da congestão.'),
    1790264439334: (4, 4, 'Rótulo hidrotórax: menor ganho de revisão continuada que o mecanismo; formulação autoral ainda requer revisão.'),
    1790264439460: (4, 4, 'Rótulo hidropericárdio: menor ganho longitudinal; autoria/idioma não aprovados por esta cor.'),
}


def write_once(name, data):
    with (OUT / name).open('x', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def flags(call):
    return {cid: flag for flag in range(8)
            for cid in call('findCards', query=f'deck:NEBLI::UC* flag:{flag}')}


def mutation(action, **params):
    req = Request('http://127.0.0.1:8765',
                  json.dumps(dict(action=action, version=6, params=params)).encode(),
                  {'Content-Type': 'application/json'})
    with urlopen(req, timeout=60) as r:
        result = json.load(r)
    if result.get('error'):
        raise RuntimeError(result['error'])
    return result['result']


def main():
    if (OUT / 'receipt.json').exists() or (OUT / 'before.json').exists():
        raise RuntimeError('Execução já iniciada; reconciliar recibos, não repetir.')
    token = str(uuid.uuid4())
    with LOCK.open('x', encoding='utf-8') as f:
        json.dump(dict(executor='Codex', aula='amostra-retencao-edema', token=token,
                       time=datetime.now(timezone.utc).isoformat()), f)
    try:
        c = ReadOnlyAnki()
        assert c('getActiveProfile') == 'Davi'
        before_flags = flags(c)
        cards = c('cardsInfo', cards=list(SAMPLE))
        assert len(cards) == len(SAMPLE)
        for card in cards:
            cid = card['cardId']
            assert before_flags[cid] == SAMPLE[cid][0], (cid, 'flag mudou')
            assert card['deckName'].startswith('NEBLI::UC03::P2::Patologia::Edema')
        notes = c('notesInfo', notes=sorted({x['note'] for x in cards}))
        # Consulta compartilhada por IDs, não por tag de nota.
        shared_ids = [1790253536913, 1790253536914]
        query = 'cid:' + ','.join(map(str, shared_ids))
        assert set(c('findCards', query=query)) == set(shared_ids)
        shared = c('notesInfo', notes=[1790253536913])[0]
        associations = [t for t in shared['tags'] if t.startswith('NEBLI::2026-')]
        assert len(associations) == 2
        physical = c('cardsInfo', cards=shared_ids)
        audit = dict(query=query, cards=shared_ids, associations=associations,
                     physical_decks=sorted({x['deckName'] for x in physical}),
                     status='Identidade e consulta verificadas; não é botão de estudo por aula.')
        write_once('before.json', dict(time=datetime.now(timezone.utc).isoformat(),
                   flags=before_flags, cards=cards, notes=notes, shared=audit))
        changed = []
        for cid, (old, new, why) in SAMPLE.items():
            if old == new:
                continue
            # Revalidar imediatamente antes de cada escrita.
            assert c('findCards', query=f'cid:{cid} flag:{old}') == [cid]
            mutation('setSpecificValueOfCard', card=cid, keys=['flags'],
                     newValues=[new], warning_check=True)
            with (OUT / 'journal.jsonl').open('a', encoding='utf-8') as f:
                f.write(json.dumps(dict(cid=cid, before=old, after=new, reason=why),
                                   ensure_ascii=False) + '\n')
            changed.append(cid)
        after_flags = flags(c)
        for cid, (_, new, _) in SAMPLE.items():
            assert after_flags[cid] == new
        outside = [cid for cid, flag in before_flags.items()
                   if cid not in SAMPLE and cid in after_flags and after_flags[cid] != flag]
        assert not outside, ('mudança externa concorrente de flags', outside)
        stable = lambda xs: [{k: v for k, v in x.items() if k not in ('flags', 'mod')} for x in xs]
        assert stable(c('cardsInfo', cards=list(SAMPLE))) == stable(cards), 'Conteúdo/agendamento mudou'
        assert c('notesInfo', notes=sorted({x['note'] for x in cards})) == notes
        receipt = dict(time=datetime.now(timezone.utc).isoformat(), profile='Davi',
                       sample_size=9, changed=changed, green=7, blue=2, uncertain=0,
                       classifications={str(k): dict(before=v[0], after=v[1], reason=v[2])
                                        for k, v in SAMPLE.items()},
                       shared=audit, unchanged_notes_and_card_state=True,
                       outside_sample_flags_changed=outside,
                       medical_before=len(before_flags), medical_after=len(after_flags),
                       content_limit='Amostra de retenção, não revisão integral de conteúdo/autoria.')
        try:
            receipt['sync_result'] = mutation('sync')
            receipt['remote_device_verified'] = False
        except Exception as exc:
            receipt['sync_error'] = str(exc)
        write_once('receipt.json', receipt)
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
    finally:
        if LOCK.exists() and json.loads(LOCK.read_text(encoding='utf-8')).get('token') == token:
            LOCK.unlink()


if __name__ == '__main__':
    main()
