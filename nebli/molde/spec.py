# Especificação curada — <AULA> (<UC> <Pn>, <componente>; <professor>; <N> lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral SÓ para lacuna provada em busca/cobertura.tsv (gate duro), último do último caso.
# Modelo vivo: arquivos-trabalho/deck-aula-uc03-rd02-diagnostico-radiologico-v2-2026-10-16/spec.py (16/10).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 7  # 6 = processo por bloco + reconstruções + cloze não genérico; 7 = passo a passo registrado (nebli.etapa), aprender por bloco, GUIA_CARDS, lint v7, figura em aula visual, referência consultada (F-20261023-CLAUDE-01/02/03)
SECOES_DA_AULA = []  # arquivos de busca/secoes/ cujo assunto É o da aula (F-20261016-CLAUDE-06: todo AnKing do conteúdo entra, sem limite)
AUTORAL_EXCECAO = ""  # só corridas com PIPELINE_VERSAO < 5; na 5 o autoral não tem teto, mas cada um prova lacuna em todos os acervos
PIPELINE = "anking-primeiro"  # F-20261015-CLAUDE-06: liga os gates duros (cobertura_anking, cores_rubrica, inducao_clozes); não remover
RUN_ID = "<ucNN-curto-AAAAMMDDa>"
SHORT = "<curto>"
LESSON = "2026-<ucNN>-<componente>-<NN>-<slug>"
DECK = "NEBLI::<UC>::<Pn>::<Componente>::<Aula>"
CRITERIOS = "MEMORY.md + FEEDBACKS (último lido) + PLANO-ANKING-PRIMEIRO, <data>"
MEDIA = {}
BUSCA = ("Três caminhos (<data>): seções de recurso do AnKing (busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt); "
         "significado em todos os acervos (busca/semantica.jsonl). ")
EXCLUIDOS = []  # (nid, motivo) de candidatos lidos e recusados
FORA_DO_RECORTE = []
A_ = "A-<bloco>"

CARDS = [
 # Código de rubrica (MEMORY §8): V-pilar | V-prova | A-aula | A-step | R-detalhe | R-org — a cor sai daqui, não da tag HY.
 # ak("chave", nid, "A-step", A_, "alvo", slide, "por quê (lâmina/prova/HY)", origin="MCAT"|"Ankisthesia"|... se externo, extra_add="- linha"),
 # au("chave", "Frase AnKing com <b>contexto</b> e {{c1::nome}}", "A-aula", A_, "alvo", "slide; fonte", "por quê", extra="- porquê"),
 # sh(nid_nebli, "azul", A_, "alvo", slide, "motivo"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {}  # chave: "- linha curta" para nota de acervo sem Extra (gate de verso)
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}  # arquivo: "o que mostra e por que ensina" (toda imagem fora do AnKing, depois de ver)
REVISAO = {}
ESCOPO = {"objetivo": "", "centrais": [], "exemplos": [], "outras_aulas": []}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
