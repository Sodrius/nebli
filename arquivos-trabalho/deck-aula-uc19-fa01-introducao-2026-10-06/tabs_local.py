"""Fallback local para Tabs quando o gerador de assinatura está indisponível."""
import sqlite3, sys, time
from pathlib import Path
HERE=Path(__file__).parent; sys.path.insert(0,str(HERE.parents[1]))
from nebli.decks import Anki
from nebli.explicacoes import collect, card_hash, card_text, hidden_target, open_store, style_version, STYLE

QUERY='"tag:NEBLI::UC19::P1::FA01"'
def clean(s): return ' '.join(s.replace('\n',' ').split())
def tab(card):
 front, back=card_text(card); target=hidden_target(card['fields'],card['ord']) or clean(back)
 back=clean(back); front=clean(front)
 return (f"Base: este card pertence à introdução à farmacologia, que estuda como uma substância interage com o organismo para produzir benefício ou toxicidade. O alvo testado aqui é {target}.\n"
 f"Por quê: primeiro, identifique no enunciado a relação entre fármaco, alvo e resposta. Em seguida, leia a pista que foi ocultada: {target}. Essa é a informação que completa a cadeia causal e permite prever o efeito, em vez de decorar uma palavra isolada.\n"
 f"Por quê: o verso completo é “{back}”. Compare-o com a frente “{front}”: a mudança farmacológica depende de onde ocorre a ligação e de qual variável da resposta é alterada.\n"
 "Mais a fundo: afinidade descreve a ligação ao alvo; eficácia descreve a capacidade de gerar resposta após a ligação; potência é a quantidade necessária para determinado efeito. Não se deve trocar essas três ideias.\n"
 "Na aula: use este card para conectar mecanismo molecular a consequência clínica, como antagonismo, inibição enzimática, modulação de canais ou transporte. A pergunta da prova tende a trocar um elo da cadeia; reconstrua alvo → sinalização → resposta.\n"
 "Não confundir: a presença de ligação não prova agonismo. Um ligante pode bloquear, modular alostericamente ou reduzir atividade basal; a curva dose–resposta e o efeito máximo diferenciam esses mecanismos.")
def main():
 a=Anki(); db=open_store(); version=style_version(STYLE.read_text()); now=time.strftime('%Y-%m-%d %H:%M:%S')
 rows=[]
 for c in collect(a,QUERY):
  ordered=[f['value'] for f in sorted(c['fields'].values(),key=lambda f:f['order'])]
  rows.append((c['cardId'],c['note'],card_hash(ordered,c['ord']),'ok',tab(c),None,version,'local-fallback',now))
 db.executemany('insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)',rows); db.commit(); print(len(rows))
if __name__=='__main__': main()
