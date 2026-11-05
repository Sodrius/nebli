"""Inventário local e lote Whisper retomável; não escreve no Anki."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
SOURCE = ROOT / 'Aulas UC07'
OUTPUT = SOURCE / 'transcricoes'
MANIFEST = RUN / 'manifesto.json'
MODEL = 'mlx-community/whisper-large-v3-turbo'
FORMATS = ('txt', 'srt', 'vtt', 'tsv', 'json')
# Número do vídeo não é número da aula no cronograma.
LESSONS = {'MSP2061 - 01': ['03'], 'MSP2061 - 02': ['04'],
           'MSP2061 - 03': ['05'], 'MSP2061 - 04': ['02'],
           'MSP2061 - 05': ['06'], 'MSP2061 - 06': ['07'],
           'MSP2061 - 13': ['10'], 'UC7 - 03': ['08'], 'UC7 - 04': []}


def save(data):
    temporary = MANIFEST.with_suffix('.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(MANIFEST)


def inspect_outputs(stem):
    paths = [OUTPUT / f'{stem}.{suffix}' for suffix in FORMATS]
    if not all(p.is_file() and p.stat().st_size for p in paths):
        return None
    data = json.loads(paths[-1].read_text())
    segments = data.get('segments', [])
    if not data.get('text', '').strip() or not segments:
        raise ValueError(f'Transcrição vazia: {stem}')
    return {'segmentos': len(segments), 'ultimo_tempo': segments[-1]['end'],
            'caracteres': len(data['text']), 'revisao_humana': 'pendente'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--transcrever', action='store_true')
    args = parser.parse_args()
    probe = shutil.which('ffprobe') or '/Users/davisousa/homebrew/bin/ffprobe'
    old = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    prior = {r['arquivo']: r for r in old.get('aulas', [])}
    data = {'modelo_lote': MODEL, 'idioma': 'pt', 'aulas': []}
    videos = sorted(SOURCE.glob('*.mp4'))
    if not videos:
        raise SystemExit(f'Nenhum vídeo em {SOURCE}')
    for video in videos:
        relative = str(video.relative_to(ROOT))
        previous = prior.get(relative, {})
        fingerprint = {'bytes': video.stat().st_size, 'mtime_ns': video.stat().st_mtime_ns}
        if all(previous.get(k) == v for k, v in fingerprint.items()) and previous.get('sha256'):
            digest = previous['sha256']
        else:
            with video.open('rb') as handle:
                digest = hashlib.file_digest(handle, 'sha256').hexdigest()
        result = subprocess.run([probe, '-v', 'error', '-show_entries', 'format=duration',
                                 '-of', 'json', str(video)], check=True, capture_output=True, text=True)
        duration = float(json.loads(result.stdout)['format']['duration'])
        complete = inspect_outputs(video.stem)
        row = {'arquivo': relative, **fingerprint, 'sha256': digest,
               'duracao_segundos': duration,
               'aulas_cronograma': next(v for k, v in LESSONS.items() if video.name.startswith(k)),
               'destino': str((OUTPUT / video.stem).relative_to(ROOT)),
               'estado': 'existente' if complete else 'pendente',
               'modelo': previous.get('modelo', 'anterior; não inferido') if complete else MODEL,
               'idioma': 'pt'}
        if complete:
            row.update(complete)
            if previous.get('estado') == 'concluido':
                row['estado'] = 'concluido'
        data['aulas'].append(row)
    save(data)
    pending = [r for r in data['aulas'] if r['estado'] == 'pendente']
    print(f'{len(videos)} vídeos; {len(pending)} pendentes; '
          f'{sum(r["duracao_segundos"] for r in pending)/60:.1f} min pendentes', flush=True)
    if not args.transcrever:
        return
    OUTPUT.mkdir(exist_ok=True)
    environment = dict(os.environ, HF_HUB_OFFLINE='1')
    for row in pending:
        video = ROOT / row['arquivo']
        row['estado'] = 'transcrevendo'
        row['inicio_utc'] = datetime.now(timezone.utc).isoformat()
        save(data)
        print(f'INÍCIO: {video.name}', flush=True)
        log = RUN / f'{video.stem}.log'
        try:
            with log.open('a') as handle:
                subprocess.run([str(ROOT / 'whisper-local'), str(video), '--output-dir', str(OUTPUT)],
                               cwd=ROOT, env=environment, stdout=handle, stderr=subprocess.STDOUT, check=True)
            result = inspect_outputs(video.stem)
            if result is None:
                raise ValueError('Whisper terminou sem os cinco formatos')
            row.update(result, estado='concluido', fim_utc=datetime.now(timezone.utc).isoformat())
            save(data)
            print(f'CONCLUÍDO: {video.name}', flush=True)
        except Exception as error:
            row.update(estado='falha', erro=str(error))
            save(data)
            raise


if __name__ == '__main__':
    main()
