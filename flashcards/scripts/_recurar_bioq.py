#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Re-curadoria 2026-07-12 de bioq-23-aminoacidos-ureia e bioq-21-lipideos-rotas.
Pedido do Davi: decks COMPLETOS e NAO-REDUNDANTES, cientes das provas UC02 P1-P4.
Regua (decisao do Davi): manter passo enzimatico da via; cortar so patologia Step-1 pura
e cards fora do escopo da E1; deduplicar cloze que testam o mesmo fato.

Este script le o curado.json antigo (pool), aplica a cut-list por guid, e emite:
  - <slug>-curado.json  (novo, enxuto)   [sobrescreve]
  - arquivos-trabalho/recuradoria-<slug>.md  (relatorio de cortes com motivo)
Backup do antigo vai para backups/tecnicos/.
"""
import json, os, shutil, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CUR = os.path.join(ROOT, "flashcards", "curadoria")
WORK = os.path.join(ROOT, "arquivos-trabalho")
BAK = os.path.join(ROOT, "backups", "tecnicos")

# ---- CUT-LISTS por guid, com motivo ----
CUTS = {
 "bioq-23-aminoacidos-ureia": {
   "z53p~@7_o=": "dup ubiquitina-proteassomo (coberto por 2 cards)",
   "gKTeo9*L/f": "dup ubiquitina-proteassomo",
   "z`iFYf_4^m": "Step-1: mnemonico MEALS (fora da E1)",
   "NIu)2Tj/#w": "Step-1: apolipoproteina/figado gorduroso detalhe (fora da E1)",
   "K#Ok!2_(dc": "dup Marasmo (definicao ja coberta)",
   "jkH:E[(XCB": "dup B6 cofator aminotransferase",
   "OTs_MJW17!": "Step-1: lactulose nomeada (E1 nao nomeia farmaco)",
   "kKuEyBfvfn": "Step-1: benzoato/fenilacetato/fenilbutirato nomeados (fora da E1)",
   "jLQd{iNz8N": "dup classificacao glicogenico (met/val/his) - card 'both' cobre",
   "JKmW;$0N)~": "dup digestao comeca no estomago (pepsinogeno->pepsina cobre)",
   "oVP:_LrGvD": "dup ativacao tripsinogenio (card enteropeptidase cobre com mecanismo)",
   "p9vyBpTE;.": "dup padrao proenzima->enzima via tripsina (proelastase)",
   "FJv}xiJ(])": "dup padrao proenzima->enzima via tripsina (procarboxipeptidase)",
   "m6uBO)o[gc": "detalhe fenilcetonas na urina (redundante com def de PKU)",
   "u>Sl|iq*K6": "Step-1: odor musty (fora da E1)",
   "I./wW!(V3-": "Step-1: evitar aspartame (fora da E1)",
   "u12i4K[[]u": "Step-1: hipopigmentacao/eczema/convulsao lista clinica (fora da E1)",
   "yR{zY7^L5v": "dup transaminacao figado (card do musculo cobre a reacao)",
   "w}z+SX7MWd": "dup alanina->piruvato ALT (card gluconeogenica cobre)",
   "pcTd9j~;E9": "dup alanina=transporte N do musculo",
   "HW}[6lqtrv": "Step-1: razao ALT<AST hepatite alcoolica (fora da E1)",
   "l_?4W2sTp{": "dup insumos do ciclo da ureia (card CPS-I cobre)",
   "I,}oNREhR&": "dup localizacao mitocondrial da CPS-I",
   "rg$=p|zphB": "obvio: disturbio do ciclo -> nao elimina amonia",
   "xug|mzq!*8": "Step-1: deficiencia de CPS-I detalhe (OTC ja cobre a hiperamonemia herdada)",
   "A{iAN],dtA": "Step-1: heranca da deficiencia de CPS-I (fora da E1)",
 },
 "bioq-21-lipideos-rotas": {
   "s]x_>!v_w[": "fora da E1: polaridade de acido graxo (E1 ensina densidade energetica, nao polaridade)",
   "CCgzzTD1RL": "fora da E1: polaridade de TAG",
   "jF}^l!?kbB": "fora da E1: polaridade do glicerol",
   "bh(o`.f^@k": "dup glucagon aumenta AG/cetoacido no sangue (card de lipolise cobre)",
   "zO;eo}i&6y": "dup HSL quebra TAG do adiposo (card anterior cobre)",
   "evQ?N]cCh_": "dup passo intermediario do transportador de carnitina (CPT-1/CPT-2 cobrem)",
   "j~V9}wo3Y#": "dup malato->piruvato gera NADPH (card da enzima malica cobre)",
   "o%6#ThhAp[": "dup biotina cofator da ACC (card 'ACC requer ATP/biotina/CO2' cobre)",
   "i%-Bph=qn>": "generico: NADPH em anabolismo (coberto por card de fonte de NADPH)",
   "OBb:wslm-H": "dup DKA complicacao temida do DM1 (restatement)",
   "_K$vX1ah;": "dup 'dois corpos cetonicos maiores' (card dos 3 corpos cetonicos cobre)",
   "C&t8Zy;v>X": "dup halito de acetona no DKA (card acetoacetato->acetona cobre o mecanismo)",
 },
}

def recurar(slug):
    path = os.path.join(CUR, slug + "-curado.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    os.makedirs(BAK, exist_ok=True)
    shutil.copy(path, os.path.join(BAK, slug + "-curado.json.pre-recuradoria-20260712"))
    cuts = CUTS[slug]
    kept, cortados = [], []
    for c in data["kept"]:
        g = c.get("guid", "")
        if g in cuts:
            cortados.append((c, cuts[g]))
        else:
            kept.append(c)
    # guids esperados mas nao achados (sanidade)
    achados = {c.get("guid") for c in data["kept"]}
    faltando = [g for g in cuts if g not in achados]
    data["kept"] = kept
    data["n_kept"] = len(kept)
    data["recuradoria"] = "2026-07-12: enxugado (dedup + poda Step-1); regua = manter passo enzimatico"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    # relatorio
    rep = os.path.join(WORK, "recuradoria-" + slug + ".md")
    with open(rep, "w", encoding="utf-8") as f:
        f.write("# Re-curadoria %s (2026-07-12)\n\n" % slug)
        f.write("Antes: %d cards - Cortados: %d - Depois: %d\n\n" % (len(data["kept"])+len(cortados), len(cortados), len(kept)))
        f.write("## Cortados (guid | motivo | frente)\n\n")
        for c, motivo in cortados:
            f.write("- `%s` - %s - %s\n" % (c.get("guid"), motivo, c.get("front","")[:80]))
        if faltando:
            f.write("\n## AVISO: guids de corte nao encontrados no curado.json\n\n")
            for g in faltando:
                f.write("- `%s`\n" % g)
    return len(cortados), len(kept), faltando

if __name__ == "__main__":
    for slug in ["bioq-23-aminoacidos-ureia", "bioq-21-lipideos-rotas"]:
        n_cut, n_keep, faltando = recurar(slug)
        print("%-32s cortados=%d  kept=%d  guids_nao_achados=%s" % (slug, n_cut, n_keep, faltando or "-"))
