#!/usr/bin/env python3
"""Inclui o aprofundamento Step 1 selecionado do AnKing na E1-teste."""
from pathlib import Path

path = Path(__file__).resolve().parents[2] / "typst-build/_par_bioq-20-pentoses-radicais-livres-teste/etapa1.typ"
text = path.read_text(encoding="utf-8")
marker = "#conclusao-box["
addition = r'''
#subtopico("3.5 — Dois usos adicionais do NADPH que explicam por que a via aparece em tantos tecidos")

O NADPH não serve apenas para fabricar lipídios ou manter a glutationa carregada. No fígado, ele alimenta o sistema do citocromo P450, que torna muitas moléculas lipossolúveis mais fáceis de metabolizar. Já nos neutrófilos, o mesmo poder redutor é entregue à NADPH oxidase durante o surto respiratório: a enzima transfere elétrons ao oxigênio para formar espécies reativas que ajudam a matar microrganismos no fagolisossomo. A mesma moeda, portanto, pode sustentar síntese, detoxificação ou defesa antimicrobiana; o contexto celular decide a enzima que recebe seus elétrons.

#subtopico("3.6 — O detalhe que integra vitaminas e rearranjo de carbonos")

A transcetolase da fase não-oxidativa precisa de pirofosfato de tiamina, a forma coenzimática da vitamina B1. Isso não muda a lógica da via, mas dá uma pista útil: quando uma enzima transfere uma unidade de dois carbonos entre açúcares, a tiamina ajuda a estabilizar esse fragmento durante a transferência. Assim, a fase não-oxidativa não é só uma coleção de nomes; ela combina uma ferramenta química específica com uma função precisa de contabilidade de carbonos.

'''
if addition not in text:
    if marker not in text:
        raise SystemExit("marcador da conclusão não encontrado")
    text = text.replace(marker, addition + marker, 1)
    path.write_text(text, encoding="utf-8")
print("OK: E1 enriquecida com P450, surto respiratório e tiamina/transcetolase")
