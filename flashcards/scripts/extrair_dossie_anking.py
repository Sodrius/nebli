#!/usr/bin/env python
"""
extrair_dossie_anking.py — monta o DOSSIE de estudo do discriminador:
50 cards de TEXTO variados (estratificados por prefixo de tag) + os 5 IO
originais AnKing com a imagem real exportada p/ disco (o card-mirror abre com Read).

Saida:
  flashcards/ANKING-DOSSIE-TEXTO.md
  flashcards/ANKING-DOSSIE-IO.md
  arquivos-trabalho/io/anking/<hash>.<ext>  (imagens dos IO reais)
"""
import json, urllib.request, random, re, html, os, base64

def call(a, **p):
    r = urllib.request.Request('http://localhost:8765',
        json.dumps({'action': a, 'version': 6, 'params': p}).encode(),
        {'Content-Type': 'application/json'})
    return json.load(urllib.request.urlopen(r, timeout=60))['result']

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s); s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

random.seed(42)
allids = call('findNotes', query='deck:"AnKing Step Deck" -note:"IO-one by one*"')
samp = random.sample(allids, 700)
info = call('notesInfo', notes=samp)
buckets = {}
for n in info:
    txt = n['fields'].get('Text', {}).get('value', '')
    if not txt:
        continue
    # bucket = tag de RECURSO/SISTEMA (variedade real), nao a #AK_Original_Decks generica
    cands = []
    for t in n['tags']:
        p = t.split('::')
        if len(p) >= 2 and p[0] in ('#AK_Step1_v12', '#AK_Step2_v12'):
            cands.append(p[0].replace('#AK_', '').replace('_v12', '') + '::' + p[1])
    pref = random.choice(cands) if cands else 'misc'
    buckets.setdefault(pref, []).append(n)

picked = []
for pref, ns in sorted(buckets.items(), key=lambda x: -len(x[1])):
    for n in ns[:3]:
        picked.append((pref, n))
picked = picked[:50]

out = [f'# DOSSIE ANKING — {len(picked)} cards de TEXTO variados (referencia do discriminador)\n',
       'Estude a DISTRIBUICAO real: comprimento de cloze, sintaxe de frente, verso telegrafico,',
       'idioma, formatacao. Isto e o que o AnKing E — julgue os candidatos contra isto.\n']
for i, (pref, n) in enumerate(picked, 1):
    f = n['fields']
    raw = f.get('Text', {}).get('value', '')
    text = clean(raw)
    extra = clean(f.get('Extra', {}).get('value', ''))[:450]
    nc = len(re.findall(r'{{c\d+::', raw))
    out.append(f'## AK-{i:02d}  [{pref}]  (clozes={nc})')
    out.append(f'TEXT: {text[:520]}')
    if extra:
        out.append(f'EXTRA: {extra}')
    out.append('')
with open('flashcards/ANKING-DOSSIE-TEXTO.md', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out))
print('TEXTO:', len(picked), 'cards ->', 'flashcards/ANKING-DOSSIE-TEXTO.md')

# ---- IO originais (exclui os meus NEBLI::io-calibracao) ----
os.makedirs('arquivos-trabalho/io/anking', exist_ok=True)
ioids = call('findNotes', query='note:"IO-one by one (AnKing Step Deck / AnKingMed)" -tag:NEBLI::*')
ioinfo = call('notesInfo', notes=ioids)
iout = ['# DOSSIE ANKING — cards de IMAGE OCCLUSION reais (referencia visual)\n',
        'Abra cada imagem com Read. Estude: fonte/render, geometria das caixas (I0),',
        'Header, Extra, higiene de asset.\n']
for i, n in enumerate(ioinfo, 1):
    f = n['fields']
    img_html = f.get('Image', {}).get('value', '')
    m = re.search(r'src="([^"]+)"', img_html)
    saved = '(sem src)'
    if m:
        fn = m.group(1)
        try:
            b64 = call('retrieveMediaFile', filename=fn)
            if b64:
                ext = os.path.splitext(fn)[1] or '.png'
                dest = f'arquivos-trabalho/io/anking/{i:02d}-{fn[:24]}{ext}'
                with open(dest, 'wb') as g:
                    g.write(base64.b64decode(b64))
                saved = dest
        except Exception as e:
            saved = f'(erro {e})'
    i0 = clean(f.get('I0', {}).get('value', ''))[:600]
    header = clean(f.get('Header', {}).get('value', ''))
    extra = clean(f.get('Extra', {}).get('value', ''))[:300]
    iout.append(f'## AK-IO-{i:02d}')
    iout.append(f'IMAGEM: {saved}   (src original: {m.group(1) if m else "?"})')
    iout.append(f'HEADER: {header}')
    iout.append(f'I0 (caixas): {i0}')
    if extra:
        iout.append(f'EXTRA: {extra}')
    iout.append('')
with open('flashcards/ANKING-DOSSIE-IO.md', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(iout))
print('IO:', len(ioinfo), 'cards ->', 'flashcards/ANKING-DOSSIE-IO.md')
