"""fix_acentos.py — restaura acentos no body de questoes/q-*.md.

Aplica um dicionario curado de palavras portuguesas inequivocas (ASCII -> acentuado)
APENAS no body das questoes (apos o segundo '---'); preserva o frontmatter YAML
inteiro (onde slugs/tags vivem sem acento por design).

Regras:
- Word boundary regex preserva sub-strings (ex.: 'sao' nao toca 'saoismo' — nao
  existe, mas seguro).
- Case-sensitive: mapas separados para minusculo, Title, UPPER.
- Idempotente: roda quantas vezes quiser; se ja tem acento, nao mexe.
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

BANCO = Path(__file__).resolve().parent
QUESTOES = BANCO / "questoes"

# Dicionario de alta confianca: ASCII -> acentuado (todas em lowercase).
# Pulei propositalmente: e/a/as/por/ai/ao/aos (ambiguos), nomes proprios,
# termos cientificos que podem aparecer em ingles, e palavras corretas sem
# acento (carbono, fosfato, sulfato, membrana etc).
ACENTOS = {
    # advérbios / conectivos
    "sao": "são", "nao": "não", "tambem": "também",
    "ja": "já", "atraves": "através", "alem": "além",
    "porem": "porém", "apos": "após",
    "ate": "até", "voce": "você", "voces": "vocês",
    # -ção / -ções
    "acao": "ação", "acoes": "ações",
    "reacao": "reação", "reacoes": "reações",
    "funcao": "função", "funcoes": "funções",
    "producao": "produção", "producoes": "produções",
    "formacao": "formação", "formacoes": "formações",
    "liberacao": "liberação", "liberacoes": "liberações",
    "composicao": "composição", "composicoes": "composições",
    "informacao": "informação", "informacoes": "informações",
    "transmissao": "transmissão", "transmissoes": "transmissões",
    "concentracao": "concentração", "concentracoes": "concentrações",
    "regulacao": "regulação", "regulacoes": "regulações",
    "ativacao": "ativação", "ativacoes": "ativações",
    "inibicao": "inibição", "inibicoes": "inibições",
    "absorcao": "absorção", "absorcoes": "absorções",
    "associacao": "associação", "associacoes": "associações",
    "duracao": "duração",
    "exposicao": "exposição",
    "expansao": "expansão",
    "inversao": "inversão",
    "conversao": "conversão",
    "elevacao": "elevação",
    "manutencao": "manutenção",
    "operacao": "operação",
    "relacao": "relação", "relacoes": "relações",
    "renovacao": "renovação",
    "reproducao": "reprodução",
    "secrecao": "secreção", "secrecoes": "secreções",
    "selecao": "seleção",
    "sensacao": "sensação", "sensacoes": "sensações",
    "separacao": "separação",
    "situacao": "situação", "situacoes": "situações",
    "solucao": "solução", "solucoes": "soluções",
    "transformacao": "transformação", "transformacoes": "transformações",
    "utilizacao": "utilização",
    "variacao": "variação", "variacoes": "variações",
    "vibracao": "vibração",
    "visualizacao": "visualização",
    "interacao": "interação", "interacoes": "interações",
    "respiracao": "respiração",
    "polimerizacao": "polimerização", "despolimerizacao": "despolimerização",
    "polarizacao": "polarização", "despolarizacao": "despolarização", "repolarizacao": "repolarização",
    "hiperpolarizacao": "hiperpolarização",
    "fosforilacao": "fosforilação", "fosforilacoes": "fosforilações",
    "desfosforilacao": "desfosforilação",
    "carboxilacao": "carboxilação", "descarboxilacao": "descarboxilação",
    "metilacao": "metilação", "desmetilacao": "desmetilação",
    "acetilacao": "acetilação", "desacetilacao": "desacetilação",
    "glicosilacao": "glicosilação",
    "ubiquitinacao": "ubiquitinação",
    "ionizacao": "ionização",
    "oxidacao": "oxidação", "oxidacoes": "oxidações",
    "reducao": "redução", "reducoes": "reduções",
    "hidrolizacao": "hidrolisação", "hidratacao": "hidratação",
    "desidratacao": "desidratação",
    "esterificacao": "esterificação",
    "isomerizacao": "isomerização",
    "lateralizacao": "lateralização",
    "estabilizacao": "estabilização",
    "ionicao": "ionização",  # variante typo
    # músculo / cardíaco / esquelético
    "musculo": "músculo", "musculos": "músculos",
    "cardiaco": "cardíaco", "cardiaca": "cardíaca",
    "cardiacos": "cardíacos", "cardiacas": "cardíacas",
    "esqueletico": "esquelético", "esqueletica": "esquelética",
    "esqueleticos": "esqueléticos", "esqueleticas": "esqueléticas",
    "neuronios": "neurônios", "neuronio": "neurônio",
    # adjetivos -ica / -ico
    "enzimatica": "enzimática", "enzimatico": "enzimático",
    "enzimaticas": "enzimáticas", "enzimaticos": "enzimáticos",
    "quimica": "química", "quimico": "químico",
    "quimicas": "químicas", "quimicos": "químicos",
    "fisica": "física", "fisico": "físico",
    "fisicas": "físicas", "fisicos": "físicos",
    "genetica": "genética", "genetico": "genético",
    "geneticas": "genéticas", "geneticos": "genéticos",
    "basica": "básica", "basico": "básico",
    "basicas": "básicas", "basicos": "básicos",
    "biologica": "biológica", "biologico": "biológico",
    "biologicas": "biológicas", "biologicos": "biológicos",
    "organica": "orgânica", "organico": "orgânico",
    "organicas": "orgânicas", "organicos": "orgânicos",
    "inorganica": "inorgânica", "inorganico": "inorgânico",
    "metabolica": "metabólica", "metabolico": "metabólico",
    "metabolicas": "metabólicas", "metabolicos": "metabólicos",
    "fisiologica": "fisiológica", "fisiologico": "fisiológico",
    "fisiologicas": "fisiológicas", "fisiologicos": "fisiológicos",
    "patologica": "patológica", "patologico": "patológico",
    "patologicas": "patológicas", "patologicos": "patológicos",
    "histologica": "histológica", "histologico": "histológico",
    "anatomica": "anatômica", "anatomico": "anatômico",
    "anatomicas": "anatômicas", "anatomicos": "anatômicos",
    "iontica": "iônica",  # variante typo
    "ionica": "iônica", "ionico": "iônico",
    "ionicas": "iônicas", "ionicos": "iônicos",
    "celico": "celíaco",
    "alergico": "alérgico", "alergica": "alérgica",
    "endocrina": "endócrina", "endocrino": "endócrino",
    "endocrinas": "endócrinas",
    "exocrina": "exócrina", "exocrino": "exócrino",
    "elastica": "elástica", "elastico": "elástico",
    "estatica": "estática", "estatico": "estático",
    "dinamica": "dinâmica", "dinamico": "dinâmico",
    "antibiotico": "antibiótico", "antibioticos": "antibióticos",
    # célula / molécula / átomo / íon
    "celula": "célula", "celulas": "células",
    "molecula": "molécula", "moleculas": "moléculas",
    "atomo": "átomo", "atomos": "átomos",
    "atomica": "atômica", "atomico": "atômico",
    "ion": "íon", "ions": "íons",
    "anion": "ânion", "anions": "ânions",
    "cation": "cátion", "cations": "cátions",
    # ácido / base
    "acido": "ácido", "acida": "ácida",
    "acidos": "ácidos", "acidas": "ácidas",
    "alcali": "álcali",
    # proteína / aminoácido / lipídio / nucleotídeo
    "proteina": "proteína", "proteinas": "proteínas",
    "aminoacido": "aminoácido", "aminoacidos": "aminoácidos",
    "lipidio": "lipídio", "lipidios": "lipídios",
    "lipidica": "lipídica", "lipidico": "lipídico",
    "lipidicas": "lipídicas", "lipidicos": "lipídicos",
    "nucleotideo": "nucleotídeo", "nucleotideos": "nucleotídeos",
    "nucleo": "núcleo", "nucleos": "núcleos",
    "nucleolo": "nucléolo",
    "polipeptidica": "polipeptídica", "polipeptidico": "polipeptídico",
    "peptidica": "peptídica", "peptidico": "peptídico",
    # água / oxigênio / hidrogênio / nitrogênio
    "agua": "água", "aguas": "águas",
    "oxigenio": "oxigênio",
    "hidrogenio": "hidrogênio",
    "nitrogenio": "nitrogênio",
    "carbonico": "carbônico", "carbonica": "carbônica",
    "potassio": "potássio",
    "sodio": "sódio",
    "calcio": "cálcio",
    "magnesio": "magnésio",
    "fosforo": "fósforo",
    "manganes": "manganês",
    # tônico / hipotônico / isotônico
    "tonico": "tônico", "tonica": "tônica",
    "hipotonico": "hipotônico", "hipotonica": "hipotônica",
    "hipertonico": "hipertônico", "hipertonica": "hipertônica",
    "isotonico": "isotônico", "isotonica": "isotônica",
    # síntese / análise / hipótese
    "sintese": "síntese", "sinteses": "sínteses",
    "analise": "análise", "analises": "análises",
    "hipotese": "hipótese", "hipoteses": "hipóteses",
    # ordinais / qualificadores
    "primario": "primário", "primaria": "primária",
    "primarios": "primários", "primarias": "primárias",
    "secundario": "secundário", "secundaria": "secundária",
    "secundarios": "secundários", "secundarias": "secundárias",
    "terciario": "terciário", "terciaria": "terciária",
    "terciarios": "terciários", "terciarias": "terciárias",
    "quaternario": "quaternário", "quaternaria": "quaternária",
    "necessario": "necessário", "necessaria": "necessária",
    "necessarios": "necessários", "necessarias": "necessárias",
    "responsavel": "responsável", "responsaveis": "responsáveis",
    "disponivel": "disponível", "indisponivel": "indisponível",
    "compativel": "compatível", "compativeis": "compatíveis",
    "incompativel": "incompatível",
    "reversivel": "reversível", "reversiveis": "reversíveis",
    "irreversivel": "irreversível",
    "sensivel": "sensível", "sensiveis": "sensíveis",
    "insensivel": "insensível",
    "estavel": "estável", "estaveis": "estáveis",
    "instavel": "instável",
    "permeavel": "permeável", "permeaveis": "permeáveis",
    "impermeavel": "impermeável", "semipermeavel": "semipermeável",
    "soluvel": "solúvel", "soluveis": "solúveis",
    "insoluvel": "insolúvel",
    "viavel": "viável", "viaveis": "viáveis", "inviavel": "inviável",
    "variavel": "variável", "variaveis": "variáveis",
    "favoravel": "favorável", "desfavoravel": "desfavorável",
    "movel": "móvel", "moveis": "móveis", "imovel": "imóvel",
    "util": "útil", "uteis": "úteis", "inutil": "inútil",
    "facil": "fácil", "faceis": "fáceis",
    "dificil": "difícil", "dificeis": "difíceis",
    "fragil": "frágil", "habil": "hábil", "agil": "ágil",
    # período / método / técnico / critério
    "periodo": "período", "periodos": "períodos",
    "metodo": "método", "metodos": "métodos",
    "epoca": "época", "epocas": "épocas",
    "tecnica": "técnica", "tecnico": "técnico",
    "tecnicas": "técnicas", "tecnicos": "técnicos",
    "criterio": "critério", "criterios": "critérios",
    "principio": "princípio", "principios": "princípios",
    "publico": "público", "publica": "pública",
    "diametro": "diâmetro", "diametros": "diâmetros",
    "estagio": "estágio", "estagios": "estágios",
    "intermediario": "intermediário", "intermediaria": "intermediária",
    "intermediarios": "intermediários", "intermediarias": "intermediárias",
    "essencial": "essencial",  # já correto
    "memoria": "memória", "memorias": "memórias",
    "historia": "história", "historias": "histórias",
    "categoria": "categoria",  # já correto
    "teoria": "teoria",  # já correto
    "alergia": "alergia",  # já correto
    "anomalia": "anomalia",  # já correto
    "amino": "amino",  # já correto
    "embriao": "embrião", "embrioes": "embriões",
    "regiao": "região", "regioes": "regiões",
    "presenca": "presença", "ausencia": "ausência",
    "diferenca": "diferença", "diferencas": "diferenças",
    "consequencia": "consequência", "consequencias": "consequências",
    "frequencia": "frequência", "frequencias": "frequências",
    "experiencia": "experiência", "experiencias": "experiências",
    "evidencia": "evidência", "evidencias": "evidências",
    "incidencia": "incidência",
    "deficiencia": "deficiência", "deficiencias": "deficiências",
    "resistencia": "resistência", "resistencias": "resistências",
    "preferencia": "preferência",
    "potencia": "potência", "potencias": "potências",
    "permanencia": "permanência",
    "exigencia": "exigência",
    "essencia": "essência",
    "inteligencia": "inteligência",
    "intolerancia": "intolerância", "tolerancia": "tolerância",
    "constancia": "constância",
    "abundancia": "abundância",
    "fragilidade": "fragilidade",  # já correto
    # outros frequentes
    "rapido": "rápido", "rapida": "rápida",
    "lento": "lento",  # correto
    "proxima": "próxima", "proximo": "próximo",
    "proximas": "próximas", "proximos": "próximos",
    "ultima": "última", "ultimo": "último",
    "ultimas": "últimas", "ultimos": "últimos",
    "especie": "espécie", "especies": "espécies",
    "especifica": "específica", "especifico": "específico",
    "especificas": "específicas", "especificos": "específicos",
    "inespecifica": "inespecífica", "inespecifico": "inespecífico",
    "individuo": "indivíduo", "individuos": "indivíduos",
    "termino": "término",
    "comeco": "começo", "comecou": "começou",
    "introducao": "introdução", "conclusao": "conclusão", "conclusoes": "conclusões",
    "atencao": "atenção",
    "intencao": "intenção", "intencoes": "intenções",
    "tensao": "tensão", "tensoes": "tensões",
    "pressao": "pressão", "pressoes": "pressões",
    "vasao": "vazão",
    "decisao": "decisão",
    "circulacao": "circulação", "circulacoes": "circulações",
    "ventilacao": "ventilação",
    "transducao": "transdução",
    "traducao": "tradução", "traducoes": "traduções",
    "replicacao": "replicação", "replicacoes": "replicações",
    "transcricao": "transcrição", "transcricoes": "transcrições",
    "mutacao": "mutação", "mutacoes": "mutações",
    "expressao": "expressão", "expressoes": "expressões",
    "depressao": "depressão",
    "regressao": "regressão",
    "agressao": "agressão",
    "lesao": "lesão", "lesoes": "lesões",
    "tumor": "tumor",  # já correto
    "doenca": "doença", "doencas": "doenças",
    "epitelio": "epitélio",
    "epitelial": "epitelial",  # já correto
    "conjuntivo": "conjuntivo",  # correto
    "musculatura": "musculatura",  # correto
    "saude": "saúde",
    "patologia": "patologia",  # correto
    "matriz": "matriz",  # correto
    "matriciais": "matriciais",  # correto
    "extracelulares": "extracelulares",  # correto
    "intracelulares": "intracelulares",  # correto
    "energia": "energia",  # correto
    "energetica": "energética", "energetico": "energético",
    "energeticas": "energéticas", "energeticos": "energéticos",
    "cinetica": "cinética", "cinetico": "cinético",
    "termodinamica": "termodinâmica", "termodinamico": "termodinâmico",
    "isomerase": "isomerase",  # correto
    "permease": "permease",  # correto
    "ureia": "ureia",  # correto
    "aerobio": "aeróbio", "aerobia": "aeróbia",
    "anaerobio": "anaeróbio", "anaerobia": "anaeróbia",
    "alcool": "álcool", "alcoois": "álcoois",
    "familia": "família", "familias": "famílias",
    "polimero": "polímero", "polimeros": "polímeros",
    "monomero": "monômero", "monomeros": "monômeros",
    "dimero": "dímero", "dimeros": "dímeros",
    "polipeptidio": "polipeptídio",
    "isomeros": "isômeros", "isomero": "isômero",
    "enzima": "enzima",  # correto
    "enzimas": "enzimas",  # correto
    "globular": "globular",  # correto
    "fibroso": "fibroso",  # correto
    "lugar": "lugar",  # correto
    "facilita": "facilita",  # correto
    "mediadora": "mediadora",  # correto
    "atras": "atrás",
    "facilidade": "facilidade",  # correto
    "limiar": "limiar",  # correto
    "estimulo": "estímulo", "estimulos": "estímulos",
    "nivel": "nível", "niveis": "níveis",
    "limite": "limite",  # correto
    "espaco": "espaço", "espacos": "espaços",
    "tamanho": "tamanho",  # correto
    "cabeca": "cabeça",
    "coracao": "coração",
    "ossea": "óssea", "osseo": "ósseo", "osseas": "ósseas", "osseos": "ósseos",
    "sequiencia": "sequência",
    "sequencia": "sequência", "sequencias": "sequências",
    "afluencia": "afluência",
    "influencia": "influência",
    "ascendencia": "ascendência",
    "descendencia": "descendência",
    # caso comum em conclusoes
    "porisso": "por isso",
}

# Normaliza chave (assume lowercase) -> garante: mantem case-pattern do match.
def _apply_case(orig: str, repl: str) -> str:
    if orig.isupper():
        return repl.upper()
    if orig[0].isupper():
        return repl[0].upper() + repl[1:]
    return repl


SPLIT_FRONT = re.compile(r"^(---\n.*?\n---\n)(.*)$", re.DOTALL)


def fix_body(text: str) -> tuple[str, int]:
    """Retorna (texto_corrigido, n_substituicoes)."""
    n = 0
    # Compile uma vez (cache)
    if not hasattr(fix_body, "_pat"):
        # alternancia ordenada por tamanho desc -> casa "informacoes" antes de "informacao"
        keys = sorted(ACENTOS.keys(), key=len, reverse=True)
        pat = r"\b(" + "|".join(re.escape(k) for k in keys) + r")\b"
        fix_body._pat = re.compile(pat, re.IGNORECASE)  # type: ignore

    def repl(m):
        nonlocal n
        orig = m.group(0)
        key = orig.lower()
        out = ACENTOS.get(key)
        if not out:
            return orig
        n += 1
        return _apply_case(orig, out)

    return fix_body._pat.sub(repl, text), n


def fix_file(path: Path, dry_run: bool = False) -> int:
    text = path.read_text(encoding="utf-8")
    m = SPLIT_FRONT.match(text)
    if not m:
        # sem frontmatter — corrige tudo
        head, body = "", text
    else:
        head, body = m.group(1), m.group(2)
    new_body, n = fix_body(body)
    if n and not dry_run:
        path.write_text(head + new_body, encoding="utf-8")
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--glob", default="q-*.md")
    args = ap.parse_args()

    arquivos = sorted(QUESTOES.glob(args.glob))
    total_arq = 0
    total_subs = 0
    for p in arquivos:
        n = fix_file(p, dry_run=args.dry_run)
        if n:
            total_arq += 1
            total_subs += n
            print(f"  {p.name}: {n} substituicoes")
    verbo = "Seriam corrigidos" if args.dry_run else "Corrigidos"
    print(f"\n{verbo} {total_subs} acentos em {total_arq}/{len(arquivos)} arquivos.")


if __name__ == "__main__":
    main()
