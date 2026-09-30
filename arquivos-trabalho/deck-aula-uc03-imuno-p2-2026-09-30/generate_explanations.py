"""Retoma Imuno e Micro na assinatura disponível, sem refazer cache válido."""
import sys,time,json
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.explicacoes import generate
from nebli.decks import Anki
while datetime.now().hour==12 and datetime.now().minute<50:
 time.sleep(20)
A=Anki();queries=[('imuno',(R/'imuno-query.txt').read_text()),('micro','deck:*Microbiologia*')]
for name,query in queries:
 print('\nINÍCIO',name,datetime.now().isoformat(),flush=True)
 for attempt in range(3):
  try:generate(A,query);break
  except Exception as exc:
   print(name,'erro:',exc,flush=True)
   if 'limit' not in str(exc).lower() and '429' not in str(exc):raise
   if attempt==2:raise
   time.sleep(45)
 print('FIM',name,datetime.now().isoformat(),flush=True)
