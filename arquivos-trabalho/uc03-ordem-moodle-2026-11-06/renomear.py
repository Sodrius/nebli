"""UC03: prefixa cada subdeck-aula com o número da aula no Moodle (ordem oficial 02–85), F-20261106-CLAUDE-01.

    /usr/bin/python3 arquivos-trabalho/uc03-ordem-moodle-2026-11-06/renomear.py            # simula
    /usr/bin/python3 arquivos-trabalho/uc03-ordem-moodle-2026-11-06/renomear.py --aplicar  # janela única de escrita

Move os cards (changeDeck preserva IDs, histórico, bandeiras, suspensões), copia o preset do deck antigo para o novo,
confere que o antigo ficou vazio e só então o apaga (cardsToo=False). Recibo em recibo.json; desfazer = mapa invertido.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from nebli import decks  # noqa: E402

AQUI = Path(__file__).parent
NUM = {  # aula do Moodle (seções "NN - XX - título" da UC3-2026)
    "P1::Biologia Molecular::Recombinação V(D)J": 18, "P1::Bioquímica::Ação hormonal": 10,
    "P1::Bioquímica::Regulação hormonal e massa corpórea": 16, "P1::Grand Round::Grand Round 1": 15,
    "P1::Imunologia::MHC e apresentação de antígenos": 20, "P1::Imunologia::Mecanismos efetores imunes": 22,
    "P1::Imunologia::Organização do sistema imune": 7, "P1::Imunologia::Reconhecimento imune adaptativo": 17,
    "P1::Imunologia::Reconhecimento imune inato": 8, "P1::Patologia::Acúmulos e adaptação celular": 11,
    "P1::Patologia::Correlação patológica-radiológica 1": 6, "P1::Patologia::Declaração de óbito": 14,
    "P1::Patologia::Diagnóstico patológico": 3, "P1::Patologia::Envelhecimento celular e tecidual": 13,
    "P1::Patologia::Lesão celular, necrose e apoptose": 9, "P1::Radiologia::Diagnóstico radiológico": 2,
    "P1::Radiologia::Radiografia e ultrassom": 4, "P1::Radiologia::Ressonância magnética": 12,
    "P1::Radiologia::Tomografia computadorizada": 5,
    "P2::Biologia Molecular::Operon em procariotos": 29, "P2::Bioquímica::Integração metabólica I": 25,
    "P2::Bioquímica::Integração metabólica II": 33, "P2::Grand Round::Grand Round 2": 21,
    "P2::Imunologia::Inflamação: início e resolução": 37, "P2::Imunologia::Sistema complemento": 31,
    "P2::Microbiologia::Antibióticos e resistência": 32, "P2::Microbiologia::Controle microbiológico": 30,
    "P2::Microbiologia::Fisiologia bacteriana": 27, "P2::Microbiologia::Genética bacteriana": 34,
    "P2::Microbiologia::Homem, ambiente e microrganismo": 39, "P2::Microbiologia::Morfologia e estrutura das bactérias": 26,
    "P2::Microbiologia::Patogenicidade bacteriana": 35, "P2::Microbiologia::Prática 1 — morfologia e assepsia": 28,
    "P2::Microbiologia::Prática 3 — identificação bacteriana": 40, "P2::Patologia::Correlação patológica-radiológica 2": 19,
    "P2::Patologia::Edema e congestão": 23, "P2::Patologia::Inflamação aguda": 38, "P2::Patologia::Patologia ambiental": 24,
    "P3::Biologia Molecular::Expressão gênica em eucariotos I": 46, "P3::Biologia Molecular::Expressão gênica em eucariotos II": 52,
    "P3::Biologia Molecular::RNAs não codificadores": 54, "P3::Imunologia::Ativação de células B": 49,
    "P3::Imunologia::Ativação de linfócitos T": 45, "P3::Imunologia::Distúrbios do sistema imune": 51,
    "P3::Imunologia::Reações de hipersensibilidade": 64, "P3::Microbiologia::Biologia geral dos fungos": 43,
    "P3::Microbiologia::Micoses sistêmicas": 50, "P3::Microbiologia::Micoses subcutâneas": 48,
    "P3::Microbiologia::Micoses superficiais e cutâneas": 44, "P3::Microbiologia::Multiplicação viral e antivirais": 58,
    "P3::Microbiologia::Patogênese da infecção viral": 59, "P3::Microbiologia::Princípios gerais dos vírus": 57,
    "P3::Microbiologia::Virologia prática": 60, "P3::Patologia::Inflamação crônica": 62,
    "P3::Patologia::Inflamação granulomatosa": 47, "P3::Patologia::Patologia da infecção viral": 61,
    "P3::Patologia::Reparo tecidual e cicatrização": 65, "P3::Radiologia::Contrastes radiológicos": 56,
}
BASE = "NEBLI::UC03::"


def mapa():
    out = {}
    for resto, n in NUM.items():
        cab, nome = resto.rsplit("::", 1)
        out[BASE + resto] = f"{BASE}{cab}::{n:02d} {nome}"
    return out


def renomear_specs(m):
    """Atualiza DECK nos specs/planos das corridas, para que uma reaplicação futura use o nome novo."""
    mudados = []
    for f in list((ROOT / "arquivos-trabalho").glob("*/spec.py")) + list((ROOT / "arquivos-trabalho").glob("*/plan*.json")):
        t = f.read_text(encoding="utf-8")
        novo = t
        for a, b in m.items():
            novo = re.sub(re.escape(a) + r'(?=["\\])', b, novo)
        if novo != t:
            f.write_text(novo, encoding="utf-8")
            mudados.append(str(f.relative_to(ROOT)))
    return mudados


def main():
    aplicar = "--aplicar" in sys.argv
    m = mapa()
    call = decks.Anki()
    for a, b in m.items():
        print(f"{a.split('::', 2)[2]}  →  {b.rsplit('::', 1)[1]}")
    if not aplicar:
        return
    recibo = {"mapa": m, "movidos": {}, "apagados": []}
    with decks.escrita(call, "uc03-ordem-moodle", sync=True):
        tela = decks.em_tela(call)
        if tela:
            cs_tela = call("findCards", query=" OR ".join(f"nid:{n}" for n in tela))
            if any("::UC03" in i["deckName"] for i in call("cardsInfo", cards=cs_tela)):
                raise SystemExit("Davi está com um card da UC03 na tela: escrita adiada (nada mudou).")
        nomes = set(call("deckNames"))
        for a, b in m.items():
            if a not in nomes:
                print("ausente (já renomeado?)", a)
                continue
            cs = call("findCards", query=f'"deck:{a}" -"deck:{a}::*"')
            conf = call("getDeckConfig", deck=a)
            call("createDeck", deck=b)
            if cs:
                call("changeDeck", cards=cs, deck=b)
            call("setDeckConfigId", decks=[b], configId=conf["id"])
            sobra = call("findCards", query=f'"deck:{a}"')
            recibo["movidos"][a] = len(cs)
            if not sobra and not [d for d in call("deckNames") if d.startswith(a + "::")]:
                call("deleteDecks", decks=[a], cardsToo=True)  # vazio conferido: nenhum card é apagado
                recibo["apagados"].append(a)
    recibo["specs"] = renomear_specs(m)
    (AQUI / "recibo.json").write_text(json.dumps(recibo, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: (len(v) if isinstance(v, (list, dict)) else v) for k, v in recibo.items()}))


if __name__ == "__main__":
    main()
