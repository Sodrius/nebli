"""Busca vídeos só nos canais preferidos de Davi e lista capítulos (timestamps reais).
Uso: python videos.py search "query" [n]   |   python videos.py chapters VIDEO_ID [VIDEO_ID...]
Canal/título vêm dos metadados do YouTube (equivalente ao oEmbed); nunca aceitar canal fora da lista."""
import json, sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')
CANAIS = ['Ninja Nerd', 'Medicosis Perfectionalis', 'Patologia Fácil', 'Dirty Medicine', 'Armando Hasudungan',
          'Osmosis from Elsevier', 'Osmosis', 'Professor Dave Explains', "Shomu's Biology"]
def ok(ch): return any(c.lower() in (ch or '').lower() for c in CANAIS)
def ytdlp(*args):
    r = subprocess.run([sys.executable, '-m', 'yt_dlp', '--no-warnings', *args], capture_output=True, text=True, encoding='utf-8')
    return [json.loads(l) for l in r.stdout.splitlines() if l.strip().startswith('{')]
def hms(s): s = int(s); return f'{s//3600}:{s%3600//60:02d}:{s%60:02d}' if s >= 3600 else f'{s//60}:{s%60:02d}'
if sys.argv[1] == 'search':
    q, n = sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 25
    for v in ytdlp('--flat-playlist', '-j', f'ytsearch{n}:{q}'):
        if ok(v.get('channel')): print(v['id'], '|', v.get('channel'), '|', v.get('title'), '|', hms(v.get('duration') or 0))
else:
    for vid in sys.argv[2:]:
        for v in ytdlp('-j', '--skip-download', f'https://www.youtube.com/watch?v={vid}'):
            print(f"## {vid} | {v.get('channel')} | {v.get('title')} | {hms(v.get('duration') or 0)} | canal ok={ok(v.get('channel'))}")
            for c in v.get('chapters') or []: print('  ', hms(c['start_time']), c['title'])
