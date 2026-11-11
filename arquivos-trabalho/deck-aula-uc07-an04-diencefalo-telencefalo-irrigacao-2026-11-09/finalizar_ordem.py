from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import json,time
from nebli.decks import Anki,escrita,em_tela
root=Path('/Users/davisousa/NEBLI');r=root/'arquivos-trabalho/deck-aula-uc07-an04-diencefalo-telencefalo-irrigacao-2026-11-09';a=Anki();p=json.loads((r/'reposicao-planejada.json').read_text());req=root/'arquivos-trabalho/anki-acao-pedido.json'
with escrita(a,'UC07 AN04: fila nativa dos novos, sem mudar revisões',sync=False):
 assert not req.exists(),'Há outro pedido pendente; não sobrescrever.'
 cfgp=root/'config/fila-novos.json';cfg=json.loads(cfgp.read_text());short=p['short']
 if short not in cfg['faixas']:
  cfg['faixas'][short]=max(cfg['faixas'].values())+20000;cfgp.write_text(json.dumps(cfg,ensure_ascii=False,indent=1))
 cards=a('cardsInfo',cards=p['cards']);protected=em_tela(a);assert not any(c['note'] in protected for c in cards)
 assert all(c['type']==0 and c['reps']==0 for c in cards),'Só novos sem histórico podem ser reposicionados.'
 req.write_text(json.dumps({'acao':'reposicionar','deck':p['deck'],'inicio':cfg['faixas'][short],'cards':p['cards']}))
 print('Pedido nativo:',len(cards),'cards; faixa',cfg['faixas'][short])
