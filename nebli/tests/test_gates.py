import json
import copy
import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from nebli import gates


class GatesTests(unittest.TestCase):
    def test_high_authorship_requires_traceable_search_not_a_fixed_quota(self):
        native = {"origin": "AnKing", "cards": [{}]}
        authored = {"origin": "Autoral", "cards": [{}], "busca": "AnKing e externos sem equivalente",
                    "espelhos": [11, 22]}
        plan = {"busca_externos": "busca/ext.txt", "entries": [native, authored]}
        self.assertTrue(gates.author_volume_supported(plan))
        plan["entries"][1] = {**authored, "espelhos": []}
        self.assertFalse(gates.author_volume_supported(plan))
        plan["entries"][1] = authored
        plan.pop("busca_externos")
        self.assertFalse(gates.author_volume_supported(plan))

    def test_tres_guias_lidos_inteiros_na_versao_vigente(self):
        # F-20261029-CLAUDE-01: em corrida v9 a leitura obrigatória são os três guias, inteiros e na versão vigente.
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            (run / "spec.py").write_text("PIPELINE_VERSAO = 9\n")
            base = Path(gates.__file__).resolve().parent.parent / "flashcards" / "projeto"
            guia = base / "GUIA_CARDS.md"
            ap = ["aprendizado concreto com mais de cinquenta caracteres de comprimento %d" % i for i in range(5)]
            dados = {"guia_sha256": hashlib.sha256(guia.read_bytes()).hexdigest(), "aprendizados": ap}
            (run / "exemplares-lidos.json").write_text(json.dumps(dados))
            lido = lambda: next(ok for k, ok in gates.exemplares_lidos(run) if "três guias" in k)
            self.assertFalse(lido())
            dados["guias_sha256"] = {n: hashlib.sha256((base / n).read_bytes()).hexdigest() for n in gates.GUIAS}
            dados["guias_aprendizados"] = {n: ap[:2] for n in gates.GUIAS}
            (run / "exemplares-lidos.json").write_text(json.dumps(dados))
            self.assertTrue(lido())
            dados["guias_sha256"][gates.GUIAS[0]] = "0" * 64
            (run / "exemplares-lidos.json").write_text(json.dumps(dados))
            self.assertFalse(lido())

    def test_leitura_obrigatoria_v10_exige_todos_os_arquivos_e_feedbacks_novos(self):
        # F-20261029-CLAUDE-03: guias, guia da aula, MEMORY, pipeline, rubrica e calibração inteiros + FEEDBACKS até a mais recente.
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            (run / "spec.py").write_text("PIPELINE_VERSAO = 10\n")
            raiz = Path(gates.__file__).resolve().parent.parent
            ap = ["aprendizado concreto com mais de cinquenta caracteres de comprimento %d" % i for i in range(5)]
            dados = {}
            (run / "exemplares-lidos.json").write_text(json.dumps(dados))
            lido = lambda: next(ok for k, ok in gates.exemplares_lidos(run) if "leitura obrigatória" in k)
            self.assertFalse(lido())  # nunca passa no vazio
            dados = {"guias_sha256": {n: hashlib.sha256((raiz / "flashcards/projeto" / n).read_bytes()).hexdigest() for n in gates.GUIAS},
                     "guias_aprendizados": {n: ap[:2] for n in gates.GUIAS},
                     "leitura_sha256": {r: hashlib.sha256((raiz / r).read_bytes()).hexdigest() for r in gates.LEITURA_OBRIGATORIA},
                     "leitura_aprendizados": {r: ap[:2] for r in gates.LEITURA_OBRIGATORIA},
                     "feedbacks_lidos_ate": gates.ultimo_feedback()}
            (run / "exemplares-lidos.json").write_text(json.dumps(dados))
            self.assertTrue(lido())
            dados["leitura_sha256"]["MEMORY.md"] = "0" * 64
            (run / "exemplares-lidos.json").write_text(json.dumps(dados))
            self.assertFalse(lido())
            dados["leitura_sha256"]["MEMORY.md"] = hashlib.sha256((raiz / "MEMORY.md").read_bytes()).hexdigest()
            dados["feedbacks_lidos_ate"] = "F-20261001-CLAUDE-01"
            (run / "exemplares-lidos.json").write_text(json.dumps(dados))
            self.assertFalse(lido())

    def test_exemplo_do_professor_nao_vira_principio_nem_carro_chefe(self):
        # F-20261029-CLAUDE-03: a 61 v2 marcou “o exemplo da hepatite” como princípio e o deck virou de hepatite.
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            (run / "spec.py").write_text("PIPELINE_VERSAO = 10\n")
            (run / "fontes").mkdir()
            (run / "fontes" / "slides.txt").write_text(
                "===== página 1 =====\nx@usp.br\nEfeitos dos vírus sobre a célula\n\n"
                "===== página 2 =====\nx@usp.br\nA combinação de tudo… o exemplo da hepatite\n• Efeito Citopático\n")
            (run / "fontes" / "transcricao.txt").write_text("o professor fala da hepatite como caso para juntar tudo")
            pr = {"laminas": [1, 1], "papel": "principio", "aprender": ["efeito direto do vírus sobre a célula"]}
            ruim = {"laminas": [2, 2], "papel": "principio", "aprender": ["vidro fosco é HBsAg acumulado"]}
            comp = {"o_que_a_aula_ensina": "x" * 160, "blocos": [pr, ruim]}
            (run / "compreensao-aula.json").write_text(json.dumps(comp))
            from nebli import etapa
            self.assertTrue(any("exemplo" in p for p in etapa.problemas_compreensao(run)))  # a E2 recusa
            bom = {"laminas": [2, 2], "papel": "exemplo", "ilustra": 1, "aprender": ["proteína viral acumulada é efeito citopático"],
                   "principios_ilustrados": [{"principio": "componente viral feito em excesso se acumula na célula (efeito citopático)",
                                              "cards": ["au-vidro"]}]}
            comp["blocos"] = [pr, bom]
            (run / "compreensao-aula.json").write_text(json.dumps(comp))
            self.assertEqual(etapa.problemas_compreensao(run), [])
            plan = {"entries": [{"key": "au-ef", "evid": "slide 1"}, {"key": "au-ef2", "evid": "slide 1"},
                                {"key": "au-vidro", "evid": "slide 2"}]}
            self.assertTrue(gates.exemplo_da_aula(run, plan)[0][1])
            plan["entries"].append({"key": "ak-hbv", "evid": "slide 2"})  # ficha da doença sem princípio, e o exemplo empata
            msg, ok = gates.exemplo_da_aula(run, plan)[0]
            self.assertFalse(ok)
            self.assertIn("ak-hbv", msg)
            self.assertFalse(gates.exemplo_da_aula(run, {"entries": []})[0][1])

    def test_deck_prova_cobre_tudo_principalmente_anking(self):
        # F-20261029-CLAUDE-04: deck-prova independente das aulas, cobrindo tudo da apostila e dos extras e um pouco mais, principalmente AnKing.
        import fitz
        from nebli import base_prova
        with tempfile.TemporaryDirectory() as d:
            run = Path(d) / "deck-prova-uc19-1-teste"
            (run / "fontes").mkdir(parents=True)
            doc = fitz.open(); pg = doc.new_page()
            pg.insert_text((50, 72), "Agonista parcial tem eficacia menor que a do pleno.")
            pg.insert_text((50, 90), "1. Qual alternativa define potencia?")
            doc.save(run / "fontes" / "apostila.pdf")
            base = {"fontes_base": ["fontes/apostila.pdf"], "blocos": [{"titulo": "3 Agonismo", "excertos": [
                {"fonte": "fontes/apostila.pdf", "paginas": [1, 1], "de": "Agonista parcial", "ate": "do pleno."}]}]}
            (run / "base-prova.json").write_text(json.dumps(base))
            base_prova.montar(run)
            self.assertEqual(base_prova.conferir(run), [])
            linhas = [{"id": "ap1", "fonte": "fontes/apostila.pdf", "trecho": "Agonista parcial tem eficacia menor", "cards": ["ak-parcial"]},
                      {"id": "q1", "tipo": "questao", "fonte": "fontes/apostila.pdf", "trecho": "Qual alternativa define potencia?",
                       "cards": ["ak-potencia"]}]
            m = {"questoes_por_fonte": {"fontes/apostila.pdf": 1}, "linhas": linhas}
            (run / "matriz-prova.json").write_text(json.dumps(m))
            ak = lambda k, s: {"key": k, "origin": "AnKing", "src": s, "cards": [{}]}
            plan = {"modo": "prova", "secoes_da_aula": ["x.txt"], "entries": [ak("ak-parcial", 1111111111111), ak("ak-potencia", 2222222222222),
                    ak("ak-ec50", 3333333333333), ak("ak-emax", 4444444444444), {"key": "au-x", "origin": "Autoral", "cards": [{}]}],
                    "excluidos": [{"nid": 5555555555555, "motivo": "duplica 1111111111111 (mesmo fato, sem imagem)"}]}
            ok = lambda pl: [o for _, o in gates.deck_prova(run, pl)]
            self.assertEqual(ok(plan), [True, True, True, True, True])
            # F-20261030-CLAUDE-01: nota HY 1–2 da seção não sai por motivo de assunto, só por duplica ou lote-N
            (run / "busca" / "secoes").mkdir(parents=True)
            (run / "busca" / "secoes" / "x.txt").write_text("# sec\n5555555555555 1-HighYield nota Step\n")
            step = copy.deepcopy(plan); step["excluidos"][0]["motivo"] = "outra-uc: fisiologia"
            self.assertFalse(ok(step)[3])
            step["excluidos"][0]["motivo"] = "lote-2: farmacocinética"
            self.assertTrue(ok(step)[3])
            linhas[0]["cards"] = []  # item da apostila sem card
            (run / "matriz-prova.json").write_text(json.dumps(m))
            self.assertFalse(ok(plan)[1])
            linhas[0].update({"fora": "eco", "porque": "mesmo item que q1, respondido pelo mesmo card"})
            m["questoes_por_fonte"]["fontes/apostila.pdf"] = 2  # questão declarada que não está na matriz
            (run / "matriz-prova.json").write_text(json.dumps(m))
            self.assertFalse(ok(plan)[1])
            m["questoes_por_fonte"]["fontes/apostila.pdf"] = 1
            linhas[1]["trecho"] = "questão inventada que não está na fonte"
            (run / "matriz-prova.json").write_text(json.dumps(m))
            self.assertFalse(ok(plan)[1])
            (run / "matriz-prova.json").write_text(json.dumps({"linhas": []}))
            self.assertFalse(ok(plan)[1])  # matriz vazia não passa
            ruim = copy.deepcopy(plan); ruim["excluidos"][0]["motivo"] = "fora do material"  # o AnKing de princípio geral entra
            self.assertFalse(ok(ruim)[2])
            ruim = copy.deepcopy(plan); ruim["excluidos"][0]["motivo"] = "duplica 9999999999999"
            self.assertFalse(ok(ruim)[2])
            ruim = copy.deepcopy(plan); ruim["entries"] = ruim["entries"][1:]  # 1 autoral em 4 = 25%
            self.assertFalse(ok(ruim)[4])
            base["blocos"][0]["excertos"].append({"lamina": "fontes/apostila.pdf", "pagina": 1, "motivo": "curta"})
            (run / "base-prova.json").write_text(json.dumps(base))
            self.assertFalse(ok(plan)[0])  # lâmina sem motivo

    def test_compreensao_da_aula_blocks_example_before_principle_and_cards_outside_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            (run / "fontes.json").write_text(json.dumps({"n_laminas": 4}))
            comp = {"o_que_a_aula_ensina": "x" * 150, "onde_se_encaixa": "y" * 120, "o_que_lembrar": ["z" * 20] * 3,
                    "blocos": [{"laminas": [1, 1], "papel": "motivacao", "o_que_o_professor_ensina": "m" * 40},
                               {"laminas": [2, 4], "papel": "principio", "o_que_o_professor_ensina": "p" * 40, "cards_exemplo": ["ex"]}]}
            (run / "compreensao-aula.json").write_text(json.dumps(comp))
            plan = {"entries": [{"key": "pr", "order": 1, "evid": "slide 2"}, {"key": "ex", "order": 2, "evid": "slide 3"}]}
            self.assertTrue(gates.compreensao_aula(run, plan)[0][1])
            plan["entries"][1]["order"] = 0
            self.assertFalse(gates.compreensao_aula(run, plan)[0][1])
            plan["entries"][1].update(order=2, evid="slide 9")
            self.assertFalse(gates.compreensao_aula(run, plan)[0][1])
            self.assertFalse(gates.fidelidade_ao_slide(run, plan)[0][1])
            comp["fidelidade"] = {"blocos": [{"laminas": [1, 1], "bate": True, "nota": "n" * 30},
                                             {"laminas": [2, 4], "bate": True, "nota": "n" * 30}], "conclusao": "c" * 150}
            (run / "compreensao-aula.json").write_text(json.dumps(comp))
            self.assertTrue(gates.fidelidade_ao_slide(run, plan)[0][1])

    def test_compreensao_v6_requires_process_and_reconstructions(self):
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            (run / "fontes.json").write_text(json.dumps({"n_laminas": 2}))
            comp = {"o_que_a_aula_ensina": "x" * 150, "onde_se_encaixa": "y" * 120, "o_que_lembrar": ["z" * 20] * 3,
                    "blocos": [{"laminas": [1, 2], "papel": "principio", "o_que_o_professor_ensina": "p" * 40}]}
            (run / "compreensao-aula.json").write_text(json.dumps(comp))
            plan = {"pipeline_versao": 6, "entries": [{"key": "pr", "order": 1, "evid": "slide 1"}]}
            self.assertFalse(gates.compreensao_aula(run, plan)[0][1])
            comp["blocos"][0]["processo"] = "q" * 120
            comp["reconstrucoes"] = [{"o_que": "r" * 60, "cards": ["pr"]}]
            (run / "compreensao-aula.json").write_text(json.dumps(comp))
            self.assertTrue(gates.compreensao_aula(run, plan)[0][1])

    def test_inventory_requires_atomic_card_mapping_visual_evidence_and_review(self):
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            plan = {"entries": [{"key": "wall", "fields": {"Text": "x", "Extra": "specific"}, "origin": "AnKing"}]}
            inventory = {
                "lido_antes_da_selecao": True,
                "slides": [
                    {"numero": 1, "classe": "capa", "justificativa": "identificação"},
                    {"numero": 2, "classe": "conteudo", "itens": [
                        {"id": "s02-wall", "alvo": "wall", "visual": "necessaria"}
                    ]}
                ], "exercicios": [], "capitulo": []
            }
            coverage = {"itens": [{"id": "s02-wall", "cards": ["wall"], "sem_imagem": "relação verbal"}]}
            review = {"feita_depois_de_instalar": True,
                      "itens": {"s02-wall": {"veredito": "ok", "card_visto": "wall"}}}
            (run / "inventario-aula.json").write_text(json.dumps(inventory))
            (run / "cobertura.json").write_text(json.dumps(coverage))
            (run / "revisao-inventario.json").write_text(json.dumps(review))
            self.assertTrue(gates.inventory(run, plan)[1])
            coverage["itens"][0]["cards"] = ["ausente"]
            (run / "cobertura.json").write_text(json.dumps(coverage))
            self.assertFalse(gates.inventory(run, plan)[1])

    def test_rejects_generic_extra(self):
        plan = {"entries": [{"key": "generic", "origin": "AnKing", "fields": {
            "Extra": "Connect the fact to inhaled pollutants and the tissue response described in this lesson"}}]}
        self.assertFalse(gates.specific_extras(plan)[1])

    def test_authorial_bold_is_a_hard_gate(self):
        base = {"key": "au", "origin": "Autoral", "kind": "autoral", "bloco": "b",
                "fields": {"Text": "The receptor is {{c1::active}}", "Extra": "Mechanism explained."},
                "cards": [{"cor": "azul"}]}
        failed = dict(gates.past_errors({"entries": [base], "lesson_id": "bioquimica"}))
        self.assertFalse(next(ok for label, ok in failed.items() if "cloze autoral" in label))
        good = copy.deepcopy(base)
        good["fields"]["Text"] = "The <b>receptor</b> is {{c1::<b>active</b>}}"
        passed = dict(gates.past_errors({"entries": [good], "lesson_id": "bioquimica"}))
        self.assertTrue(next(ok for label, ok in passed.items() if "cloze autoral" in label))

    def test_organizer_is_vertical_and_uses_cloze_indices_deliberately(self):
        independent = {"key": "org", "origin": "Autoral", "organizador": True,
                       "fields": {"Text": "Partes:<br>{{c1::A}}<br>{{c2::B}}<br>{{c3::C}}"}}
        self.assertTrue(gates.inducao_clozes({"entries": [independent]})[-1][1])
        prose = copy.deepcopy(independent)
        prose["fields"]["Text"] = "Partes: {{c1::A}}, {{c2::B}} e {{c3::C}}"
        self.assertFalse(gates.inducao_clozes({"entries": [prose]})[-1][1])
        contrast = {"key": "contrast", "origin": "Autoral", "organizador": True,
                    "contraste_complementar": True,
                    "fields": {"Text": "Anterior — {{c1::eferente}}<br>Posterior — {{c1::aferente}}"}}
        self.assertTrue(gates.inducao_clozes({"entries": [contrast]})[-1][1])
        contrast["fields"]["Text"] = "Anterior — {{c1::eferente}}<br>Posterior — {{c2::aferente}}"
        self.assertFalse(gates.inducao_clozes({"entries": [contrast]})[-1][1])

    def test_cards_scope_does_not_require_e1_but_default_does(self):
        from nebli import entrega
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "Aula.apkg").write_text("package")
            (root / "Aula - slides.pdf").write_text("slides")
            data = {"nome": "Aula", "drive_pasta": ".", "escopo": "cards"}
            with patch.object(entrega, "ROOT", root):
                self.assertTrue(all(ok for _, ok in gates.drive_checks(data)))
                data.pop("escopo")
                self.assertEqual(sum(not ok for _, ok in gates.drive_checks(data)), 1)
                data["escopo"] = "typo"
                self.assertFalse(all(ok for _, ok in gates.drive_checks(data)))

    def test_sources_need_book_three_channels_and_recorded_searches(self):
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            for name in ("slides.pdf", "cap.txt", "a.txt", "b.txt", "c.txt"):
                (run / name).write_text("x")
            data = {"slides": {"arquivo": "slides.pdf", "todas_vistas": True}, "livros": [{"texto": "cap.txt", "lido": True}],
                    "ninja_nerd_busca": "não há vídeo específico para a aula",
                    "canais": [{"transcricao": n, "lido": "trechos", "calibracao": "confirmou o mecanismo"} for n in ("a.txt", "b.txt", "c.txt")],
                    "provas": {"estado": "não localizada", "busca": "pasta Provas"}, "exercicios": {"estado": "consultada"},
                    "caoc": {"estado": "não localizada"}}
            result = dict(gates.sources(run, data))
            self.assertFalse(result["caoc: consultado, ou busca no Drive registrada"])
            self.assertFalse(result["fonte obrigatória veteranos: leitura integral rastreável e contribuição ao plano"])
            self.assertFalse(next(v for k, v in result.items() if k.startswith("canais que Davi acompanha")))
            data["canais"].pop(); data["livros"][0]["lido"] = False
            failed = [k for k, ok in gates.sources(run, data) if not ok]
            self.assertIn("bibliografia da UC: capítulo da aula extraído e lido", failed)

    def test_source_evidence_blocks_missing_partial_fabricated_and_essential_sources(self):
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            (run / "read.txt").write_text("material efetivamente localizado")
            digest = hashlib.sha256((run / "read.txt").read_bytes()).hexdigest()
            (run / "planejamento.json").write_text(json.dumps({"alvos": [{"id": "a01"}]}))
            read = {"estado": "consultada", "arquivo": "read.txt", "sha256": digest,
                    "leitura": "integral", "localizador": "capítulo 15, páginas 300–310",
                    "contribuicao": "distinguir mucosa e submucosa", "alvos": ["a01"],
                    "lida_antes_da_selecao": True}
            data = {"evidencias": {k: [copy.deepcopy(read)] for k in gates.FONTES_PLANO},
                    "livros": [{"texto": "read.txt"}], "canais": []}
            data["evidencias"]["youtube"] = []
            for i in range(3):
                video = dict(read, canal="Ninja Nerd", url=f"https://youtube.com/watch?v={i}")
                data["evidencias"]["youtube"].append(video)
                data["canais"].append({"url": video["url"], "transcricao": "read.txt"})
            self.assertTrue(all(ok for _, ok in gates.source_evidence(run, data)))
            for key, value in (("arquivo", "missing.txt"), ("sha256", "falso"),
                               ("leitura", "trechos"), ("contribuicao", ""),
                               ("alvos", ["inexistente"]), ("lida_antes_da_selecao", False)):
                bad = copy.deepcopy(data)
                bad["evidencias"]["bibliografia"][0][key] = value
                self.assertFalse(all(ok for _, ok in gates.source_evidence(run, bad)), key)
            for family in gates.FONTES_PLANO:
                bad = copy.deepcopy(data)
                del bad["evidencias"][family]
                self.assertFalse(all(ok for _, ok in gates.source_evidence(run, bad)), family)
            absent = {"estado": "inacessível", "essencial": True, "busca": "Drive oficial", "impacto": "faltam questões"}
            data["evidencias"]["provas"] = [absent]
            self.assertFalse(all(ok for _, ok in gates.source_evidence(run, data)))
            absent["essencial"] = False
            self.assertTrue(all(ok for _, ok in gates.source_evidence(run, data)))
            data["provas"] = {"estado": "consultada"}
            self.assertFalse(all(ok for _, ok in gates.source_evidence(run, data)))

    def test_sources_reject_empty_transcript(self):
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            (run / "slides.pdf").write_text("x")
            (run / "cap.txt").write_text("x")
            (run / "empty.txt").touch()
            data = {
                "slides": {"arquivo": "slides.pdf", "todas_vistas": True},
                "livros": [{"texto": "cap.txt", "lido": True}],
                "canais": [{"transcricao": "empty.txt", "lido": "integral", "canal": "Ninja Nerd", "calibracao": "x"}] * 3,
                "provas": {"estado": "consultada"}, "exercicios": {"estado": "consultada"}, "caoc": {"estado": "consultada"}
            }
            result = dict(gates.sources(run, data))
            self.assertFalse(next(v for k, v in result.items() if k.startswith("canais que Davi acompanha")))


    def test_frontier_cases_required_only_with_percurso(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp)
            self.assertIsNone(gates.frontier_cases(run))
            (run / "percurso-aula.md").write_text("# Percurso\n\n| Bloco |\n")
            self.assertFalse(gates.frontier_cases(run)[1])
            (run / "percurso-aula.md").write_text("# Percurso\n\n## Casos de fronteira\n\nnenhum\n")
            self.assertTrue(gates.frontier_cases(run)[1])

    def test_passo_a_passo_v7(self):
        from nebli import etapa
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp)
            comp = {"o_que_a_aula_ensina": "x" * 160, "blocos": [
                {"laminas": [1, 5], "papel": "principio", "aprender": ["virulence is the relative ability to cause disease"]},
                {"laminas": [6, 9], "papel": "exemplo", "ilustra": 1, "aprender": ["rotavirus NSP4 raises calcium and causes diarrhea"]}]}
            (run / "compreensao-aula.json").write_text(json.dumps(comp))
            ent = lambda k, s: {"key": k, "evid": f"Slide {s}", "cards": [{"n": 1}]}
            plan = {"entries": [ent("a", 2)] + [ent(f"r{i}", 7) for i in range(5)], "compartilhados": {}}
            (run / "mapa-de-profundidade.json").write_text(json.dumps({"passos": [{"itens": [{"cards": ["a", "r0"]}]}]}))
            res = gates.passo_a_passo_pre(run, plan)[0]
            self.assertFalse(res[1])
            self.assertIn("supera o princípio", res[0]); self.assertIn("fora de qualquer item", res[0]); self.assertIn("etapas", res[0])
            with self.assertRaises(SystemExit):
                etapa.registrar(run, "E2", "compreensão escrita bloco a bloco conferindo cada lâmina")

    def test_v7_comentarios_23_10(self):
        from nebli import lint_cards
        self.assertTrue(any("símbolo" in m for _, m in lint_cards.check_v7('<div data-nebli-organizacao="true"><b>Clearance</b>:<br>- high E: {{c1::<b>flow</b>}}</div>')))
        self.assertTrue(any("negrito" in m for _, m in lint_cards.check_v7("The portal is the {{c1::<b>respiratory</b>}} tract")))
        self.assertTrue(any("tópicos" in m for _, m in lint_cards.check_v7("<b>Tube</b> gives {{c1::a}}, {{c2::b}} and {{c3::c}}")))
        self.assertEqual(lint_cards.check_v7("<b>Rotavirus</b> lowers Na+ and {{c1::<b>K+</b>}} in B cells of hepatitis B"), [])
        plan = {"lesson_id": "2026-uc08-biocel-10-embriologia", "pipeline_versao": 7,
                "entries": [{"key": "au-x", "origin": "Autoral", "fields": {"Text": "The <b>liver</b> forms the {{c1::<b>bud</b>}}", "Extra": "- x"}}]}
        with tempfile.TemporaryDirectory() as tmp:
            res = dict((m.split(":")[0], ok) for m, ok in gates.v7_pre(tmp, plan))
            self.assertFalse(res["[duro] aula visual (anatomia, embriologia, histologia)"])
            self.assertFalse(res["[duro] autoral de embriologia diz na frente que é desenvolvimento (embryo, bud, week, primitive…)"])
            self.assertFalse(all(ok for _, ok in gates.v7_pre(tmp, plan)))
            self.assertFalse(gates.v7_pos(tmp, plan)[0][1])
            Path(tmp, "REVISAO-AUTORAIS.md").write_text("## Revisão final no deck vivo\n- au-x — escrita: ok — cloze: ok — aprofundamento: ok — negrito: ok\n")
            self.assertTrue(gates.v7_pos(tmp, plan)[0][1])

    def test_v8_motivacao_e_qualidade(self):
        from nebli import etapa
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp)
            (run / "spec.py").write_text("PIPELINE_VERSAO = 8\n")
            (run / "mapa-de-profundidade.json").write_text(json.dumps({"passos": [{"itens": [{"id": "p1-1"}]}]}))
            mot = {"motivacoes": [{"id": "m1", "item_mapa": "p1-1", "reconstruir": "how Dicer and RISC turn a dsRNA into silencing of one mRNA",
                                   "por_que_dura": "RNA interference returns in pharmacology (siRNA drugs) and in viral defense", "depois_de": "ak1",
                                   "atendida_por": ["au-a"]}]}
            (run / "motivacoes.json").write_text(json.dumps(mot))
            self.assertEqual(etapa.problemas_motivacoes(run), [])
            plan = {"pipeline_versao": 8, "compartilhados": {}, "entries": [
                {"key": "ak1", "order": 1, "origin": "AnKing", "fields": {"Text": "x"}},
                {"key": "au-a", "order": 2, "origin": "Autoral", "motivacao": "m1",
                 "fields": {"Text": "<b>Dicer</b> cuts long dsRNA into {{c1::<b>siRNAs</b>}}", "Extra": "- RISC then uses one strand, so the mRNA is cleaved"}}]}
            res = gates.motivacao_autorais(run, plan)[0]
            self.assertFalse(res[1]); self.assertIn("E3", res[0])  # sem congelar na E3 reprova
            (run / "etapas").mkdir(); (run / "etapas" / "E3-motivacoes.json").write_text(json.dumps(mot))
            self.assertTrue(gates.motivacao_autorais(run, plan)[0][1])
            plan["entries"][1]["motivacao"] = "m9"  # justificado depois
            self.assertFalse(gates.motivacao_autorais(run, plan)[0][1])
            plan["entries"][1]["motivacao"] = "m1"
            self.assertFalse(gates.qualidade_autorais(run, plan)[0][1])  # sem análise de qualidade
            juiz = {c: f"{c}: julgamento próprio deste card sobre Dicer e siRNA" for c in gates.CRITERIOS_QUALIDADE}
            (run / "qualidade-autorais.json").write_text(json.dumps({"au-a": dict(juiz, veredito="aprovado")}))
            self.assertTrue(gates.qualidade_autorais(run, plan)[0][1])
            plan["entries"][1]["fields"]["Text"] = "<b>siRNAs</b> come from Dicer cutting dsRNA into {{c1::<b>siRNAs</b>}}"
            self.assertIn("visível", gates.qualidade_autorais(run, plan)[0][0])


if __name__ == "__main__":
    unittest.main()
