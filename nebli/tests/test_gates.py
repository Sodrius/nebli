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
            self.assertFalse(result["canais que Davi acompanha: pelo menos 3 aulas com transcrição lida"])
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
            self.assertFalse(result["canais que Davi acompanha: pelo menos 3 aulas com transcrição lida"])


if __name__ == "__main__":
    unittest.main()
