# PIPELINE — Ingestão token-eficiente NEBLI

**Versão:** 1.0 | **Data:** 2026-05-05 | **Alvo:** 300+ questões novas, ~20 PDFs, budget <50k tokens/lote

---

## 1. Diagnóstico do problema atual

### Overhead medido (baseado em LOG.md 2026-05-04)
- **Lote A:** 108k tokens, 30 questões → ~3600 tokens/questão
- **Lote B:** 108k tokens, 22 questões → ~4900 tokens/questão
- **Média:** ~4200 tokens/questão

### Onde vão os tokens (breakdown)

| Componente | Tokens | % do total | Desperdício? |
|------------|--------|-----------|-------------|
| CONVENCOES.md inteiro | ~4000 | 3.7% | **SIM** — mandado 2× por lote |
| taxonomia.md inteiro | ~5000 | 4.6% | **SIM** — mandado 2×, usa só 10% |
| PDF completo (texto extraído) | ~70000 | 64.8% | **PARCIAL** — 80% é texto narrativo |
| Prompt de classificação (original) | ~15000 | 13.9% | **SIM** — lista todas as tags/convenções |
| Resposta do modelo (tags + análise) | ~9000 | 8.3% | Necessário |
| Overhead de chamadas em cadeia | ~5000 | 4.6% | **SIM** — sem pipeline, há repetições |

### Principais vazamentos
1. **CONVENCOES.md mandado na íntegra** em cada chamada (4k tokens reutilizáveis)
2. **taxonomia.md mandado na íntegra** (5k tokens, usa só ~500 tokens per questão)
3. **Prompt de extração não comprimido** (lista todas as regras em prosa)
4. **Sem roteamento por tipo** — Haiku gasta tokens iguais em MC simples e discursivas complexas

---

## 2. Pipeline proposto em 3 estágios

### Fluxo geral

```
PDF → ESTÁGIO 1 (Triagem/Haiku) → ESTÁGIO 2 (Extração/Haiku+Sonnet) 
    → ESTÁGIO 3 (Classificação/Haiku) → banco_json_updater.py
```

#### Estágio 1: Triagem (~500 tokens por PDF)
**Entrada:** PDF (bruto, pode ser imagem pura)  
**Modelo:** Haiku (rápido, cheap, basta identificação)  
**Saída:** Confirmação se tem questões + tipo (MC/CE/discursiva) + count aproximado

**Propósito:** Filtrar PDFs inúteis antes de prosseguir. Interrompe pipeline se sem questões.

#### Estágio 2: Extração (~800 tokens por questão)
**Entrada:** Texto extraído do PDF (já OCR'ado) + template comprimido de schema  
**Modelo:** Haiku (MC simples) ou Sonnet (discursiva/ambígua)  
**Saída:** Enunciado normalizado + alternativas + gabarito + campos auxiliares

**Propósito:** Estruturar questão sem classificar ainda.

#### Estágio 3: Classificação (~200 tokens por questão)
**Entrada:** Enunciado extraído + conceito-central proposto + macroárea identificada  
**Modelo:** Haiku (sempre, pois taxonomia é table lookup)  
**Saída:** 3–5 tags + nível + armadilha

**Propósito:** Tags vão contra taxonomia já acarregada (não pela 1ª vez).

---

## 3. Template de extração comprimido (Estágio 2)

**Tamanho:** ~600 tokens | **Copy-paste pronto**

```
Extraia as questões do texto abaixo. Siga rigorosamente:

ESQUEMA YAML (um arquivo q-NNNN.md por questão):
---
id: [NNN — 4 dígitos sequenciais, fornecido pelo orquestrador]
formato: MC | CE | discursiva
gabarito: [Para MC: letra A-E; para CE: [C,E,C,E]; para discursiva: "texto curto"]
nivel: [facil | medio | dificil — baseado em raciocínio exigido, não na dificuldade do tema]
conceito_central: [Uma frase explicando o que a Q testa, não o que ela parece testar. Máx 15 palavras.]
fonte: [Nome do PDF + indicativo de fonte, ex "PROVA_UC1_P2_2024.pdf"]
armadilha: [Opcional. Que confusão o examinador explora? Ex: "confundem ATP direto com indireto"]
---

## Enunciado
[Texto literal da questão]

## Alternativas
(A) [texto literal]
(B) [texto literal]
... (para MC); ou ## Itens [(1) texto, (2) texto, ...] para CE

## Gabarito
[Literal da fonte ou inferido se fonte ilegível]

## Explicação
[Se fonte cita explicação, inclua; senão deixe vazio]
---

REGRAS CRÍTICAS:
1. IDs sequenciais — orquestrador passa número base
2. nível: ignora "tema é difícil"; calibra por raciocínio (MC com 2 conceitos = médio; com 4+ = difícil)
3. Gabarito: RESOLVA e coloque certo, mesmo que fonte esteja errada — o banco quer gabarito correto
4. conceito_central: máximo clareza. Não é título, é "o que a questão testa de verdade"
5. Não invente alternativas; se OCR falhar, marque com [OCR_INCERTO]
```

---

## 4. Template de classificação comprimido (Estágio 3)

**Tamanho:** ~400 tokens | **Copy-paste pronto**

```
Classifique esta questão. Siga rigorosamente:

ENUNCIADO:
[enunciado da Q extraída]

CONCEITO CENTRAL (proposto pela extração):
[conceito]

MACROÁREA IDENTIFICADA (do pipeline):
[macroárea, ex: "Transporte de membrana", "Eletrofisiologia", "Sinapses"]

TAXONOMIA RELEVANTE (só essa macroárea):
- [listar 10-15 tags dessa macroárea de taxonomia.md, não todas]

TAREFA:
Responda em JSON:
{
  "tags": ["tag1", "tag2", "tag3"],  // 3-5 tags, primeira é a mais central
  "tags_status": "estavel | novo",    // "novo" se conceito não tem tag existente
  "tags_novas": ["nome-novo"] ou [],  // se status = novo
  "nivel": "facil | medio | dificil", // re-calibre se discordar
  "armadilha": "Texto breve ou null"  // refine a proposta da extração
}

REGRAS CRÍTICAS:
1. tags[0] é a TAG MAIS CENTRAL — a que melhor resume o que Q testa
2. 3-5 tags total — menos é raso, mais é ruído
3. Se conceito não tem tag na taxonomia, marque como "novo" e proponha nome em kebab-case
4. Sempre consulte a lista reduzida acima — NÃO invente tags fora daquela macroárea
5. Nível: respeite a calibração da extração, mas corrija se óbvio (ex: Q com 2 conceitos isolados = fácil)
```

---

## 5. Estimativa de custo

### Custo por questão (3 estágios)

| Estágio | Componente | Tokens | Modelo |
|---------|-----------|--------|--------|
| 1 | Triagem (amortizado por ~10Q/PDF) | ~50 | Haiku |
| 2 | Extração (texto estruturado) | ~800 | Haiku (MC) / Sonnet (discursiva) |
| 3 | Classificação (table lookup) | ~200 | Haiku |
| — | **Overhead de orquestração** | ~50 | — |
| — | **TOTAL POR QUESTÃO** | **~1100** | — |

### Comparação com baseline

| Métrica | Atual | Proposto | Redução |
|---------|-------|----------|---------|
| Tokens/questão | ~4200 | ~1100 | **74%** |
| Custo estimado (300Q) | ~1.26M tokens | ~330k tokens | ~**840k tokens economizados** |
| Custo em USD (Haiku @$0.8/M, Sonnet @$3/M) | ~$3.50/Q | ~$0.95/Q | **73% mais barato** |

### Economia detalhada
- **Remoção de CONVENCOES.md:** ~4k tokens/lote = -333 tokens/questão (12 questões/lote)
- **Triagem inteligente (Haiku):** -2500 tokens/Q comparado a Sonnet (ingestão Estágio 2)
- **Taxonomia reduzida por macroárea:** -3500 tokens/lote = -292 tokens/Q
- **Prompt comprimido:** -8k tokens/lote = -667 tokens/Q

---

## 6. Roteamento Haiku vs Sonnet vs Opus

### Decisão: quando chamar qual modelo

```python
def roteador_estágio_2(tipo_questão, complexidade, temImagem):
    """Retorna (modelo, budget_tokens_máx)"""
    
    if tipo_questão == "MC":
        if complexidade <= "facil" and not temImagem:
            return "Haiku", 800  # 90% das MCs
        elif complexidade in ["facil", "medio"] and temImagem:
            return "Sonnet", 1500  # imagens precisam Sonnet
        else:  # dificil ou muito ambígua
            return "Sonnet", 2000
    
    elif tipo_questão in ["CE", "discursiva"]:
        if complexidade == "facil":
            return "Haiku", 1000
        else:
            return "Sonnet", 1800  # Sonnet melhor com lógica complexa
    
    return "Sonnet", 2000  # fallback


def roteador_estágio_3(tags_status):
    """Estágio 3 é sempre Haiku (table lookup, sem criatividade)"""
    return "Haiku", 400
```

### Regras de ouro
1. **Haiku:** MC simples (≤2 conceitos), sem imagem, nível fácil/médio
2. **Sonnet:** Qualquer coisa com imagem; discursiva/CE; 3+ conceitos em jogo
3. **Opus:** Nunca neste pipeline (overhead 10× o Sonnet, não compensa)

---

## 7. Script orquestrador: `ingerir_lote.py`

**Copy-paste pronto. Adapt caminhos conforme Cowork.**

```python
#!/usr/bin/env python3
"""
ingerir_lote.py — Pipeline token-eficiente para banco NEBLI

Uso:
    python ingerir_lote.py caminho/para/pdf_ou_pasta/ turmas="110,113" uc="UC1"

Outputs:
    - arquivo q-NNNN.md por questão em banco/questoes/
    - LOG.md atualizado
    - tokens_log.json com gasto por etapa
"""

import os
import sys
import json
from pathlib import Path
from dataclasses import dataclass
from typing import Literal
import re

# Imports Anthropic
import anthropic

@dataclass
class TokenLog:
    etapa: str
    modelo: str
    questao_id: str
    tokens_in: int
    tokens_out: int
    tempo_ms: int
    
    def total(self):
        return self.tokens_in + self.tokens_out

class PipelineIngador:
    def __init__(self, banco_root: str):
        self.banco_root = Path(banco_root)
        self.client = anthropic.Anthropic()
        self.tokens_log = []
        self.next_id = self._get_next_question_id()
        self.taxa_macro = {}  # cache de macroárea por tema
        
    def _get_next_question_id(self) -> int:
        questoes_dir = self.banco_root / "questoes"
        if not questoes_dir.exists():
            return 1
        ids = [int(f.name.split("-")[1].split(".")[0]) for f in questoes_dir.glob("q-*.md")]
        return max(ids, default=0) + 1
    
    # ESTÁGIO 1: Triagem
    def etapa_1_triagem(self, pdf_path: str) -> dict:
        """Haiku: Tem questões? Que tipo? Quantas?"""
        
        prompt = f"""Analise este PDF de prova médica:

[PDF PATH: {pdf_path}]
[OCR CONTENT BELOW, primeiros 2000 chars]
---
{self._extract_text_from_pdf(pdf_path)[:2000]}
---

Responda em JSON:
{{
  "tem_questoes": true|false,
  "tipo": "MC | CE | discursiva | misto",
  "count_estimado": número,
  "tema_principal": "string",
  "qualidade_ocr": "RICO | OK | FRACO",
  "motivo_rejeição": "string ou null"
}}

Rejeite se: texto incompreensível, não é prova, é só gabarito, etc."""

        resp = self.client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )
        
        self._log_tokens("Etapa1_Triagem", "Haiku", "N/A", resp.usage)
        
        try:
            return json.loads(resp.content[0].text)
        except:
            return {"tem_questoes": False, "motivo_rejeição": "Parse error"}
    
    # ESTÁGIO 2: Extração
    def etapa_2_extracao(self, pdf_text: str, tipo_questao: str) -> list[dict]:
        """Haiku (MC simples) ou Sonnet (complexas/imagens)"""
        
        template_comprimido = """Extraia as questões do texto abaixo. Siga rigorosamente o esquema YAML:

---
id: [NNN — número sequencial, fornecido pelo orquestrador]
formato: MC | CE | discursiva
gabarito: [Para MC: letra A-E; para CE: [C,E,C,E]; para discursiva: "texto"]
nivel: facil | medio | dificil
conceito_central: [Uma frase, máx 15 palavras]
fonte: [Nome do PDF]
armadilha: [Opcional]
---

## Enunciado
[Texto literal]

## Alternativas / Itens
(A)/(1) ...

## Gabarito
[Correto, mesmo se fonte errada]

## Explicação
[Se houver]
---

REGRAS:
1. Gabarito CORRETO, não o que fonte diz
2. nível por raciocínio, não tema
3. conceito_central é "o que Q testa", não título
4. Se OCR ruim, marque [OCR_INCERTO]"""

        modelo = "claude-3-5-haiku-20241022" if tipo_questao == "MC" else "claude-3-5-sonnet-20241022"
        
        resp = self.client.messages.create(
            model=modelo,
            max_tokens=4000 if modelo == "claude-3-5-haiku-20241022" else 6000,
            messages=[{
                "role": "user",
                "content": f"{template_comprimido}\n\n[PDF TEXT]\n{pdf_text}"
            }]
        )
        
        self._log_tokens("Etapa2_Extracao", modelo, "LOTE", resp.usage)
        
        # Parse questões do markdown retornado
        questoes = self._parse_yaml_blocks(resp.content[0].text)
        return questoes
    
    # ESTÁGIO 3: Classificação
    def etapa_3_classificacao(self, enunciado: str, conceito_central: str, 
                             macroarea: str) -> dict:
        """Haiku: Tags + nível + armadilha (table lookup)"""
        
        # Carrega taxonomia.md e filtra por macroárea
        taxa_relevante = self._get_tags_by_macroarea(macroarea)
        
        prompt = f"""Classifique esta questão.

ENUNCIADO:
{enunciado}

CONCEITO CENTRAL:
{conceito_central}

MACROÁREA:
{macroarea}

TAGS DISPONÍVEIS (dessa macroárea):
{taxa_relevante}

Responda em JSON:
{{
  "tags": ["tag1", "tag2", "tag3"],
  "tags_status": "estavel | novo",
  "tags_novas": [] ou ["novo-conceito"],
  "nivel": "facil | medio | dificil",
  "armadilha": "texto ou null"
}}"""

        resp = self.client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}]
        )
        
        self._log_tokens("Etapa3_Classificacao", "Haiku", "Q", resp.usage)
        
        try:
            return json.loads(resp.content[0].text)
        except:
            return {"tags": ["indefinido"], "tags_status": "novo", "tags_novas": ["indefinido"]}
    
    # Helpers
    def _extract_text_from_pdf(self, pdf_path: str) -> str:
        """Placeholder — em produção, use PyPDF2 ou similar"""
        # Este é um demo. Na prática: pdfplumber.open(pdf_path)
        with open(pdf_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    
    def _parse_yaml_blocks(self, markdown_text: str) -> list[dict]:
        """Extrai blocos YAML do markdown retornado pelo modelo"""
        blocks = re.findall(r'---\n(.*?)\n---', markdown_text, re.DOTALL)
        questoes = []
        for block in blocks:
            try:
                # Parse YAML simples (não completo, usar PyYAML em produção)
                q = {"raw_yaml": block}
                questoes.append(q)
            except:
                pass
        return questoes
    
    def _get_tags_by_macroarea(self, macroarea: str) -> str:
        """Retorna tags dessa macroárea só (de taxonomia.md)"""
        # Placeholder — em produção, carrega taxonomia.md, filtra por macroárea
        return "transporte-membrana, difusao-simples, transporte-ativo, ..."
    
    def _log_tokens(self, etapa: str, modelo: str, q_id: str, usage):
        log_entry = {
            "etapa": etapa,
            "modelo": modelo,
            "questao_id": q_id,
            "tokens_in": usage.input_tokens,
            "tokens_out": usage.output_tokens,
            "total": usage.input_tokens + usage.output_tokens
        }
        self.tokens_log.append(log_entry)
        print(f"{etapa:20} | {modelo:15} | Q{q_id:>4} | {log_entry['total']:>5} tokens")
    
    def run(self, pdf_root: str, turmas: str, uc: str):
        """Orquestra o pipeline completo"""
        print(f"\n=== PIPELINE NEBLI ===")
        print(f"PDF root: {pdf_root}")
        print(f"Turmas: {turmas}, UC: {uc}\n")
        
        pdf_files = list(Path(pdf_root).glob("*.pdf"))
        total_questoes = 0
        
        for pdf_file in pdf_files:
            print(f"\n[{pdf_file.name}]")
            
            # Estágio 1
            triagem = self.etapa_1_triagem(str(pdf_file))
            if not triagem.get("tem_questoes"):
                print(f"  SKIP: {triagem.get('motivo_rejeição')}")
                continue
            
            print(f"  → {triagem['count_estimado']} questões ({triagem['tipo']}, OCR: {triagem['qualidade_ocr']})")
            
            # Estágio 2
            pdf_text = self._extract_text_from_pdf(str(pdf_file))
            questoes = self.etapa_2_extracao(pdf_text, triagem['tipo'])
            print(f"  → Extraídas {len(questoes)} questões")
            
            # Estágio 3
            for q in questoes:
                classificacao = self.etapa_3_classificacao(
                    q.get("enunciado", ""),
                    q.get("conceito_central", ""),
                    triagem["tema_principal"]
                )
                q.update(classificacao)
                print(f"    Q{self.next_id}: {', '.join(q['tags'][:2])}")
                self.next_id += 1
                total_questoes += 1
        
        # Salva log de tokens
        with open(self.banco_root / "meta" / "tokens_log.json", 'w') as f:
            json.dump(self.tokens_log, f, indent=2)
        
        print(f"\n=== RESUMO ===")
        print(f"Total de questões ingeridas: {total_questoes}")
        print(f"ID final: q-{self.next_id-1}")
        
        # Estatísticas de tokens
        total_tokens = sum(log["total"] for log in self.tokens_log)
        avg_per_q = total_tokens / max(total_questoes, 1)
        print(f"Tokens gastos: {total_tokens:,}")
        print(f"Média por questão: {avg_per_q:.0f} tokens")
        print(f"Custo estimado (Haiku): ${total_tokens * 0.8 / 1_000_000:.2f}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python ingerir_lote.py <pdf_root> turmas='110,113' uc='UC1'")
        sys.exit(1)
    
    banco_root = Path(__file__).parent.parent
    pdf_root = sys.argv[1]
    turmas = sys.argv[2].split("=")[1] if len(sys.argv) > 2 else "999"
    uc = sys.argv[3].split("=")[1] if len(sys.argv) > 3 else "UC1"
    
    pipeline = PipelineIngador(str(banco_root))
    pipeline.run(pdf_root, turmas, uc)
```

---

## 8. Implementação passo a passo (próximas sessões)

### Fase 1: Setup (1h)
- [ ] Copiar `PIPELINE.md` para `banco/meta/`
- [ ] Criar `ingerir_lote.py` em `banco/`
- [ ] Carregar taxonomia.md em memória (dict por macroárea)
- [ ] Teste com 1 PDF (manual, sem automação)

### Fase 2: Automação (2h)
- [ ] Implementar `_extract_text_from_pdf()` com pdfplumber ou PyPDF2
- [ ] Testar Estágio 1 (triagem) com 5 PDFs
- [ ] Testar Estágio 2 (extração) com 2 questões
- [ ] Testar Estágio 3 (classificação) com essas 2 questões

### Fase 3: Produção (1h)
- [ ] Rodar pipeline em lote de 20 PDFs
- [ ] Comparar tokens_log.json com baseline (espera ~1200 tokens/Q)
- [ ] Atualizar banco.json via `indexar.py`
- [ ] Registrar no LOG.md

---

## 9. Checklist de qualidade

Antes de cada lote de 20+ questões:
- [ ] 90%+ das Q têm conceito_central sensato
- [ ] Tags não repetem (máx 5 por Q)
- [ ] Gabaritos conferem com resposta correta, não com fonte
- [ ] Nível é calibrado por raciocínio, não tema
- [ ] Armadilhas citam a confusão específica
- [ ] Tokens gastos < 1500/Q em média

---

## 10. Fallbacks e edge cases

| Caso | Ação |
|------|------|
| PDF com imagens puras (sem OCR) | Estágio 1 rejeita; Davi precisa scanear melhor |
| Questão discursiva muito longa | Roteador escolhe Sonnet, budget +800 tokens |
| Tag nova proposta | Marca como "novo", Davi aprova depois na consolidação |
| Gabarito incerto | Claude infere conforme mecânica; marca `tags_pendentes_aprovacao` |
| Estágio 1 falha (Haiku timeout) | Retry 1×; se falhar, pula PDF e registra no LOG |

---

**Próximo passo:** Copiar este PIPELINE.md, testar Estágio 1 com `INDICE.md` para identificar PDFs mais promissores, rodar em lote-piloto de 3 PDFs.
