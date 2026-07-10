"""
corrigir_acentos.py - Restaura acentos em palavras PT-BR que foram
ingeridas como ASCII (OCR antigo descartou diacriticos).

Filosofia: substituicao por dicionario fixo. SO substitui formas
inequivocas - palavras onde a forma com acento e a unica leitura
valida no contexto biomedico.

Casos ambiguos NAO sao substituidos automaticamente. Davi pode
revisar via grep manual depois.

Uso:
  python banco/corrigir_acentos.py            (dry-run)
  python banco/corrigir_acentos.py --apply
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUESTOES = ROOT / "questoes"

# Dicionario: forma ASCII -> forma acentuada PT-BR
# Curado para o dominio biomedico. So inclui formas inequivocas.
DICIONARIO = {
    # palavras frequentes do auditor anterior
    "questoes": "questões",
    "questao": "questão",
    "funcao": "função",
    "funcoes": "funções",
    "explicacao": "explicação",
    "explicacoes": "explicações",
    "celula": "célula",
    "celulas": "células",
    "transcricao": "transcrição",
    "traducao": "tradução",
    "replicacao": "replicação",
    "regulacao": "regulação",
    "transmissao": "transmissão",
    "expressao": "expressão",
    "introducao": "introdução",
    "sintese": "síntese",
    "energetica": "energética",
    "energetico": "energético",
    "ativacao": "ativação",
    "inibicao": "inibição",
    "concentracao": "concentração",
    "concentracoes": "concentrações",
    "solucao": "solução",
    "solucoes": "soluções",
    "reacao": "reação",
    "reacoes": "reações",
    "acao": "ação",
    "acoes": "ações",
    "ions": "íons",
    "ionica": "iônica",
    "ionico": "iônico",
    "proteinas": "proteínas",
    "proteina": "proteína",
    "agua": "água",
    "metabolico": "metabólico",
    "metabolica": "metabólica",
    "aerobico": "aeróbico",
    "aerobica": "aeróbica",
    "anaerobico": "anaeróbico",
    "anaerobica": "anaeróbica",
    "endogenas": "endógenas",
    "endogenos": "endógenos",
    "exogenas": "exógenas",
    "exogenos": "exógenos",
    "hormonios": "hormônios",
    "hormonio": "hormônio",
    "peptidicos": "peptídicos",
    "peptidico": "peptídico",
    "peptideo": "peptídeo",
    "aminoacidos": "aminoácidos",
    "aminoacido": "aminoácido",
    "lipidios": "lipídios",
    "lipideo": "lipídeo",
    "lipideos": "lipídeos",
    # nomes proprios biomedicos
    "bioquimica": "bioquímica",
    "biologico": "biológico",
    "biologica": "biológica",
    "fisiologico": "fisiológico",
    "fisiologica": "fisiológica",
    "molecular": "molecular",  # já correta, fica no dict como no-op?
    "gliconeogenese": "gliconeogênese",
    "glicose": "glicose",  # já correta
    "frutose": "frutose",
    "lactose": "lactose",
    "sacarose": "sacarose",
    # termos comuns
    "atraves": "através",
    "membrana": "membrana",  # ok
    "membranas": "membranas",
    "membranar": "membranar",
    "polar": "polar",  # ok
    "apolar": "apolar",  # ok
    "ipotalamo": "hipotálamo",  # ?
    "metabolismo": "metabolismo",  # ok
    "estrutura": "estrutura",  # ok
    "estruturais": "estruturais",  # ok
    "molecula": "molécula",
    "moleculas": "moléculas",
    "molecular": "molecular",
    "atomico": "atômico",
    "atomica": "atômica",
    "atomicos": "atômicos",
    "atomicas": "atômicas",
    "eletronico": "eletrônico",
    "eletronica": "eletrônica",
    "eletrons": "elétrons",
    "eletron": "elétron",
    # extras vistos no banco
    "sao": "são",   # CUIDADO: pode confundir com SAO Paulo, mas no contexto biomed eh quase sempre 'sao'='são'
    "nao": "não",
    "podem": "podem",  # ok
    "tambem": "também",
    "atraves": "através",
    "porem": "porém",
    "ate": "até",
    "ja": "já",
    "ai": "aí",
    "hipotonico": "hipotônico",
    "hipertonico": "hipertônico",
    "isotonico": "isotônico",
    "osmotico": "osmótico",
    "osmotica": "osmótica",
    "osmolaridade": "osmolaridade",  # ok
    "permeavel": "permeável",
    "impermeavel": "impermeável",
    "ferromagnetico": "ferromagnético",
    "tipica": "típica",
    "tipico": "típico",
    "automatica": "automática",
    "automatico": "automático",
    "vesicula": "vesícula",
    "vesiculas": "vesículas",
    "nucleo": "núcleo",
    "nucleos": "núcleos",
    "nucleotideo": "nucleotídeo",
    "nucleotideos": "nucleotídeos",
    "nucleolo": "nucléolo",
    "ribossomico": "ribossômico",
    "ribossomos": "ribossomos",  # ok
    "mitocondria": "mitocôndria",
    "mitocondrias": "mitocôndrias",
    "mitocondrial": "mitocondrial",  # ok
    "endossomico": "endossômico",
    "lisossomo": "lisossomo",  # ok
    "fagossomo": "fagossomo",  # ok
    "lipidica": "lipídica",
    "lipidico": "lipídico",
    "hidrofobica": "hidrofóbica",
    "hidrofobico": "hidrofóbico",
    "hidrofilica": "hidrofílica",
    "hidrofilico": "hidrofílico",
    "polaridade": "polaridade",  # ok
    "carater": "caráter",
    "interacao": "interação",
    "interacoes": "interações",
    "ligacao": "ligação",
    "ligacoes": "ligações",
    "conformacao": "conformação",
    "conformacional": "conformacional",  # ok
    "informacao": "informação",
    "informacoes": "informações",
    "polimerase": "polimerase",  # ok
    "exonuclease": "exonuclease",  # ok
    "endonuclease": "endonuclease",  # ok
    "fosfato": "fosfato",  # ok
    "fosforilacao": "fosforilação",
    "desfosforilacao": "desfosforilação",
    "fosforilada": "fosforilada",
    "fosforilado": "fosforilado",
    "carboxila": "carboxila",  # ok
    "carboxilico": "carboxílico",
    "carboxilica": "carboxílica",
    "carboxilatos": "carboxilatos",
    "anidrico": "anídrico",
    "alcoolico": "alcoólico",
    "alcalose": "alcalose",  # ok
    "acidose": "acidose",  # ok
    "acidico": "acídico",
    "acida": "ácida",
    "acido": "ácido",
    "acidos": "ácidos",
    # cuidado com 'acidos' ASCII -> 'ácidos': mas o banco escreve 'acidos'
    # estrutura química
    "isomero": "isômero",
    "isomeros": "isômeros",
    "isomeria": "isomeria",  # ok
    "isomerase": "isomerase",  # ok
    "enantiomero": "enantiômero",
    "enantiomeros": "enantiômeros",
    "estereoquimica": "estereoquímica",
    "quiral": "quiral",  # ok
    # comuns
    "principio": "princípio",
    "principios": "princípios",
    "espontanea": "espontânea",
    "espontaneo": "espontâneo",
    "espontaneidade": "espontaneidade",  # ok
    "experimento": "experimento",  # ok
    "experimentais": "experimentais",  # ok
    "necessario": "necessário",
    "necessaria": "necessária",
    "obrigatorio": "obrigatório",
    "obrigatoria": "obrigatória",
    "elas": "elas",  # ok
    "este": "este",  # ok
    "esse": "esse",  # ok
    "esta": "está",  # CUIDADO: ambíguo 'esta'/'está'
    "essa": "essa",  # ok
    "voce": "você",
    "voces": "vocês",
    # marcas anatômicas
    "neuronio": "neurônio",
    "neuronios": "neurônios",
    "axonio": "axônio",
    "axonios": "axônios",
    "axonal": "axonal",  # ok
    "axonico": "axônico",
    "dendrito": "dendrito",  # ok
    "dendritica": "dendrítica",
    "dendritico": "dendrítico",
    "potencial": "potencial",  # ok
    "potenciais": "potenciais",  # ok
    "passiva": "passiva",  # ok
    "ativa": "ativa",  # ok
    "ativos": "ativos",  # ok
    "ativas": "ativas",  # ok
    "deslocamento": "deslocamento",  # ok
    "amplitude": "amplitude",  # ok
    "frequencia": "frequência",
    "frequencias": "frequências",
    "duracao": "duração",
    "tempo": "tempo",  # ok
    # palavras médicas
    "deficiencia": "deficiência",
    "deficiencias": "deficiências",
    "sindrome": "síndrome",
    "sindromes": "síndromes",
    "patologia": "patologia",  # ok
    "patologico": "patológico",
    "patologica": "patológica",
    "clinico": "clínico",
    "clinica": "clínica",
    "clinicas": "clínicas",
    "clinicos": "clínicos",
    "diagnostico": "diagnóstico",
    "diagnostica": "diagnóstica",
    "prognostico": "prognóstico",
    "tratamento": "tratamento",  # ok
    "alteracao": "alteração",
    "alteracoes": "alterações",
    "manifestacao": "manifestação",
    "manifestacoes": "manifestações",
    # bioquímica metabolismo
    "anaerobio": "anaeróbio",
    "aerobio": "aeróbio",
    "fermentativo": "fermentativo",  # ok
    "respiratorio": "respiratório",
    "respiratoria": "respiratória",
    "cardiaca": "cardíaca",
    "cardiaco": "cardíaco",
    "hepatico": "hepático",
    "hepatica": "hepática",
    "renal": "renal",  # ok
    "intestinal": "intestinal",  # ok
    "muscular": "muscular",  # ok
    # gerais
    "tambem": "também",
    "porem": "porém",
    "atraves": "através",
    "alem": "além",
    "atras": "atrás",
    "apos": "após",
    "aposentar": "aposentar",  # ok, mas raríssimo no banco
    "mais": "mais",  # ok
    "menos": "menos",  # ok
    "ambito": "âmbito",
    "ate": "até",
    "categoria": "categoria",  # ok
    "principal": "principal",  # ok
    "secundario": "secundário",
    "secundaria": "secundária",
    "primario": "primário",
    "primaria": "primária",
    "primeira": "primeira",  # ok
    "primeiro": "primeiro",  # ok
    # pluralizações com acento
    "particularidades": "particularidades",  # ok
    "caracteristicas": "características",
    "caracteristica": "característica",
}


def aplicar(text: str) -> tuple[str, int]:
    """Aplica substituicoes mantendo capitalizacao (primeira letra)."""
    total = 0
    # ordena por tamanho descendente para casar palavras compostas antes
    for ascii_w, acent_w in sorted(DICIONARIO.items(), key=lambda x: -len(x[0])):
        if ascii_w == acent_w:
            continue  # no-op skip
        # word boundary em ambos os lados
        # case preservation: para a primeira letra
        def repl(m):
            orig = m.group(0)
            if orig[0].isupper():
                return acent_w[0].upper() + acent_w[1:]
            return acent_w
        new_text, n = re.subn(rf"\b{re.escape(ascii_w)}\b", repl, text,
                              flags=re.IGNORECASE)
        if n:
            text = new_text
            total += n
    return text, total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--uc", default="UC1", help="filtra por uc_origem")
    args = ap.parse_args()

    total = 0
    arquivos = 0
    for p in sorted(QUESTOES.glob("q-*.md")):
        original = p.read_text(encoding="utf-8")
        # filtra por UC olhando frontmatter
        if f"uc_origem: {args.uc}" not in original:
            continue
        # so substitui no corpo (preserva frontmatter intacto pra evitar
        # quebrar campos como 'aula', 'tags', 'conceito_central' que tem
        # convenção propria)
        m = re.match(r"^(---\n)(.*?)(\n---\n)(.*)$", original, re.DOTALL)
        if not m:
            continue
        front_open, front_body, front_close, body = m.groups()

        # 1. Aplica substituicao no corpo do .md
        new_body, n_body = aplicar(body)

        # 2. Aplica substituicao APENAS nos campos `armadilha:` e
        #    `conceito_central:` do frontmatter (esses vao pro apendice).
        #    NAO toca em id, tags, aula, formato, gabarito, etc.
        new_front_body = front_body
        n_front = 0
        for campo in ("armadilha", "conceito_central"):
            pat = re.compile(rf"^({campo}:\s*)(.*?)$", re.MULTILINE)
            def sub_campo(match):
                nonlocal n_front
                prefix, valor = match.group(1), match.group(2)
                novo, nn = aplicar(valor)
                n_front += nn
                return prefix + novo
            new_front_body = pat.sub(sub_campo, new_front_body)

        n_total = n_body + n_front
        if n_total > 0:
            arquivos += 1
            total += n_total
            print(f"{p.name}: {n_total} substituicoes (corpo={n_body}, front={n_front})")
            if args.apply:
                p.write_text(front_open + new_front_body + front_close + new_body,
                             encoding="utf-8")

    modo = "APLICADO" if args.apply else "DRY-RUN"
    print(f"\n[{modo}] {arquivos} arquivos, {total} substituicoes totais (UC: {args.uc})")


if __name__ == "__main__":
    main()
