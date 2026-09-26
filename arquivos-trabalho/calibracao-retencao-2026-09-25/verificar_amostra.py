"""Reconcilia a escrita já feita; não reaplica flags."""
import json
import uuid
from datetime import datetime, timezone
from calibrar_amostra import OUT, LOCK, SAMPLE, ReadOnlyAnki, flags, mutation, write_once

token = str(uuid.uuid4())
with LOCK.open('x', encoding='utf-8') as f:
    json.dump(dict(token=token, executor='Codex', aula='verify-retencao'), f)
try:
    b = json.loads((OUT / 'before.json').read_text(encoding='utf-8'))
    c = ReadOnlyAnki()
    assert c('getActiveProfile') == 'Davi'
    after = flags(c)
    before = {int(k): v for k, v in b['flags'].items()}
    for cid, (old, new, why) in SAMPLE.items():
        assert after[cid] == new
    assert not {cid for cid in before.keys() & after.keys()
                if cid not in SAMPLE and before[cid] != after[cid]}
    cards = c('cardsInfo', cards=list(SAMPLE))
    stable = lambda xs: [{k: v for k, v in x.items() if k not in ('flags', 'mod')} for x in xs]
    assert stable(cards) == stable(b['cards'])
    notes = c('notesInfo', notes=sorted({x['note'] for x in cards}))
    assert notes == b['notes']
    assert set(c('findCards', query=b['shared']['query'])) == set(b['shared']['cards'])
    result = dict(time=datetime.now(timezone.utc).isoformat(), profile='Davi',
                  sample_size=9, changed=[k for k,v in SAMPLE.items() if v[0]!=v[1]],
                  green=7, blue=2, uncertain=0,
                  classifications={str(k):dict(before=v[0],after=v[1],reason=v[2]) for k,v in SAMPLE.items()},
                  shared=b['shared'], unchanged_notes_and_scheduling=True,
                  outside_sample_flags_changed=[], medical_before=len(before), medical_after=len(after),
                  initial_check_issue='Comparação incluía mod/flags, alterados legitimamente; reconciliação excluiu só esses campos.',
                  limit='Calibração pequena de retenção; não certifica todo conteúdo/autoria.')
    try:
        result['sync_result'] = mutation('sync')
        result['remote_device_verified'] = False
    except Exception as exc:
        result['sync_error'] = str(exc)
    write_once('receipt.json', result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
finally:
    if LOCK.exists() and json.loads(LOCK.read_text(encoding='utf-8')).get('token') == token:
        LOCK.unlink()
