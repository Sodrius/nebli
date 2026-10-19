"""Atualiza os três Tabs alterados após a geração ter sido bloqueada por cota.

Os textos foram lidos e escritos manualmente no formato vigente: dois parágrafos,
do princípio para a recuperação, sem listas ou metacomentário.
"""
import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from nebli.decks import Anki
from nebli.explicacoes import STYLE, card_hash, collect, open_store, style_version

Q = '"tag:NEBLI::2026-uc03-patologia-47-inflamacao-granulomatosa"'
TEXT = {
 1791716419358: """Um microrganismo fagocitado só é eliminado se o fagossomo amadurecer e receber mecanismos microbicidas. A tuberculose ilustra o oposto: o bacilo consegue sobreviver no macrófago, portanto o próprio fagócito passa a ser o nicho onde ele permanece e pode se multiplicar.

Essa persistência mantém antígeno no tecido e explica por que é necessária uma resposta Th1 que ative o macrófago por IFN-γ. O granuloma organiza essa tentativa de controle, mas não garante que cada bacilo dentro dos macrófagos seja eliminado.""",
 1791910088374: """Granuloma descreve antes de tudo a organização de macrófagos ativados em torno de um estímulo persistente. O centro dessa estrutura pode sofrer lesão; necrose e células gigantes ajudam a caracterizar alguns padrões, mas não são necessárias para que exista um granuloma.

Quando o centro contém detritos necróticos secos e esbranquiçados, de aspecto semelhante a queijo, o padrão é chamado caseoso. A tuberculose é o exemplo clássico: a resposta que contém o bacilo também pode causar dano central, por isso a morfologia mostra ao mesmo tempo contenção e lesão.""",
 1791926820948: """TNF participa da organização e manutenção do granuloma porque favorece ativação e recrutamento de macrófagos. Se o sinal é insuficiente, o agregado perde capacidade de conter um estímulo persistente; por isso bloquear TNF pode desorganizar granulomas previamente estáveis.

Essa mesma resposta precisa ser limitada. TNF em excesso amplifica inflamação e pode contribuir para necrose, de modo que o resultado protetor depende de equilibrar contenção do agente com preservação do tecido.""",
}

cards = {c['cardId']: c for c in collect(Anki(), Q)}
db = open_store()
version = style_version(STYLE.read_text(encoding='utf-8'))
stamp = time.strftime('%Y-%m-%d %H:%M:%S')
for cid, text in TEXT.items():
    c = cards[cid]
    ordered = [f['value'] for f in sorted(c['fields'].values(), key=lambda f: f['order'])]
    db.execute('insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)',
               (cid, c['note'], card_hash(ordered, c['ord']), 'ok', text, None,
                version, 'revisão manual', stamp))
db.commit()
print(f'{len(TEXT)} Tabs atualizados')
