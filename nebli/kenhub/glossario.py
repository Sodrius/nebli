"""Atestado de termos em português (F-20261018-CLAUDE-02: “pega tradução oficial de algum lugar”).

Termo traduzido por nós só passa se aparecer numa fonte oficial: os nomes em PT/sinônimos/latim que o próprio Kenhub devolve
(`locale=pt`, de todas as unidades coletadas) ou o texto do Ângelo Machado, Neuroanatomia Funcional (bibliografia da UC07, no Drive;
texto extraído em ~/NEBLI-privado/kenhub/glossario/machado.txt). O Machado vem de OCR: a comparação ignora acento, caixa e pontuação.
"""
import json
import re
import unicodedata
from pathlib import Path
from functools import lru_cache

from nebli.kenhub.caminhos import RAIZ

ARTIGOS = {"o", "a", "os", "as", "um", "uma", "do", "da", "dos", "das", "de", "no", "na"}


def _singular(w: str) -> str:
    for fim, novo in (("oes", "ao"), ("aes", "ao"), ("ais", "al"), ("eis", "el"), ("ois", "ol"), ("res", "r"), ("ns", "m")):
        if len(w) > len(fim) + 2 and w.endswith(fim):
            return w[:-len(fim)] + novo
    return w[:-1] if len(w) > 3 and w.endswith("s") else w


def norm(t: str) -> str:
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    pal = [_singular(w) for w in re.findall(r"[a-z0-9]+", t)]
    while pal and pal[0] in ARTIGOS:
        pal = pal[1:]
    return " ".join(pal)


@lru_cache(maxsize=1)
def _kenhub() -> set:
    out = set()
    for f in RAIZ.glob("*/*/itens.json"):
        for i in json.loads(f.read_text()).get("itens", []):
            for t in [i.get("nome_pt"), i.get("latim")] + list(i.get("sinonimos_pt", [])):
                if t:
                    out.add(norm(t))
    return out


@lru_cache(maxsize=1)
def _machado() -> str:
    arq = RAIZ / "glossario" / "machado.txt"
    if not arq.exists():
        return ""
    bruto = arq.read_text()
    juntado = re.sub(r"-\s*\n\s*|-\s+(?=[a-zà-ú])", "", bruto)   # sílaba hifenizada na quebra de linha (“an- terior”)
    return " " + norm(bruto) + " " + norm(juntado) + " "


CODIGO = re.compile(r"^[CTLSco]{1,2}\d+([/–-][CTLSco]{0,2}\d+)*$", re.I)


@lru_cache(maxsize=1)
def _aceitos() -> dict:
    """Termos confirmados à mão numa fonte oficial (com a fonte): nebli/kenhub/glossario_aceitos.json."""
    arq = Path(__file__).with_name("glossario_aceitos.json")
    return {norm(k): v for k, v in json.loads(arq.read_text()).items()} if arq.exists() else {}


@lru_cache(maxsize=1)
def _palavras() -> frozenset:
    return frozenset(w for w in (_machado() + " " + " ".join(_kenhub())).split() if len(w) >= 2)


def atestado(termo: str):
    """Fonte que atesta o termo ('Kenhub', 'Machado', 'aceito') ou None. “A e B” / “A ou B” / “A, B” / “A do B”: cada parte tem de constar."""
    partes = [x.strip(" ()") for x in re.split(r"\s+(?:e|ou|d[oa]s?|de)\s+|[,()]\s*", termo.strip()) if x.strip(" ()")]
    if len(partes) > 1:
        fontes = [atestado(x) for x in partes]
        return None if None in fontes else fontes[0]
    if CODIGO.match(termo.strip()):
        return "código"
    n = norm(termo)
    if not n:
        return "vazio"
    if n in _aceitos():
        return "aceito"
    if n in _kenhub() or any(n in k for k in _kenhub()):
        return "Kenhub"
    if f" {n} " in _machado():
        return "Machado"
    # palavra a palavra: nenhuma palavra pode ser desconhecida (pega calco e invenção; “bulbo caudal” = bulbo + caudal)
    palavras = _palavras()
    if all(w.isdigit() or w in palavras or (len(w) >= 4 and any(x.startswith(w) for x in palavras)) for w in n.split()):
        return "palavras"
    return None
