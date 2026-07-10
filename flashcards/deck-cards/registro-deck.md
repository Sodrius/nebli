<!-- Registro VIVO do deck Anki — o que está de fato dessuspendido agora.
     Puxado do AnkiConnect (localhost:8765), não do que o manifesto afirma.
     Refazer com o snippet no rodapé sempre que aplicar/podar um bloco.
     Padrão de curadoria: deck-cards/PADRAO.md -->

# Registro do deck — o que está no deck agora

**Snapshot: 2026-07-07** · deck `AnKing Step Deck` · coleção do container Docker `anki-nebli` (localhost:8765).

## Blocos NEBLI ativos

| Aula (tag-âncora `NEBLI::`) | total | ativos | novos | autorais | Contrato E1 |
|---|---:|---:|---:|---:|---|
| bioq-20-pentoses-radicais-livres | 63 | 63 | 18 | 0 | ⚠️ 7/13 subtópicos (fatos-chave a mapear) |
| bioq-glicogenio | 68 | 68 | 63 | 0 | — não auditado no padrão novo |
| bioq-21-lipideos-rotas | 106 | 106 | 30 | 0 | — não auditado no padrão novo |
| bioq-23-aminoacidos-ureia | 135 | 135 | 135 | 0 | — não auditado no padrão novo |
| biomol-25-mutacao-reparo-recombinacao | 55 | 55 | 26 | 0 | — não auditado no padrão novo |
| biomol-26-dna-recombinante-pcr | 34 | 34 | 34 | 0 | — não auditado no padrão novo |

**Totais:** 461 cards ativos · 306 novos · 0 autorais (ainda nenhum card escrito por mim).

## Ordem da fila (cronograma UC2, `due` crescente = estudado antes)

pentoses (23/jun) → lipídeos (23/jun T) → biomol-25/26 (24/jun) → glicogênio (26/jun) → aminoácidos (02/jul). Prova 4 = 13/jul.

## Leitura rápida

- Nenhum bloco foi ainda re-auditado no **padrão novo** (contrato de fatos-chave + autorais). Pentoses é o piloto do padrão novo.
- `autorais = 0` em todos: a autoria de buracos ainda não começou. Primeiro alvo = pentoses.

---
*Como refazer este snapshot (rodar quando aplicar/podar um bloco):*
```
python - <<'EOF'
import json,urllib.request
def call(a,p=None):
    r=urllib.request.Request("http://localhost:8765",data=json.dumps({"action":a,"version":6,"params":p or {}}).encode(),headers={"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(r,timeout=15))["result"]
for t in sorted({x for x in call("getTags") if x.startswith("NEBLI::") and "zerado" not in x and x!="NEBLI::autoral"}):
    tot=len(call("findCards",{"query":f'tag:{t}'}))
    if not tot: continue
    act=len(call("findCards",{"query":f'tag:{t} -is:suspended'}))
    new=len(call("findCards",{"query":f'tag:{t} is:new -is:suspended'}))
    aut=len(call("findCards",{"query":f'tag:{t} tag:NEBLI::autoral'}))
    print(f"{t}: total={tot} ativos={act} novos={new} autorais={aut}")
EOF
```
