"""Baixa somente os dois PDFs docentes identificados no Drive para inspeção das figuras."""
from pathlib import Path
import urllib.request
P=Path(__file__).parent/'fontes'
for name,id in [('complemento','1DOzPt5O51Zf5lpubkKKiQkEQlVWsGxHn'),('inflamacao','1qAeOJhQmlhkXPH1QFWreleIi5HS28Qu-')]:
 target=P/(name+'.pdf')
 if target.exists() and target.read_bytes()[:4]==b'%PDF': continue
 url='https://drive.usercontent.google.com/download?id='+id+'&export=download&confirm=t'
 data=urllib.request.urlopen(url,timeout=120).read()
 if data[:4]!=b'%PDF': raise RuntimeError('Drive não devolveu PDF: '+name)
 target.write_bytes(data);print(name,len(data),flush=True)
