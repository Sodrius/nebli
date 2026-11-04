import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from nebli import revisor_autorais as review


class ReviewerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.run = Path(self.temp.name)
        self.plan = {"entries": [{
            "key": "au-process", "origin": "Autoral", "order": 1,
            "fields": {"Text": "The <b>signal</b> opens {{c1::channel A}}.",
                       "Extra": "Opening allows ion entry, so the membrane response follows."},
            "motivacao": {"reconstruir": "Identify the channel that connects the signal to ion entry."},
            "contexto": {"aula": "The lecture explains signal, channel and response."},
            "fontes": [{"trecho": "Signal opens channel A; ions enter and change the membrane response.",
                        "localizador": "lecture p. 3"}],
            "busca": {"candidatos": [{"trecho": "Channel B in a different process", "decisao": "Different target"}]},
        }], "compartilhados": {}}

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, value):
        (self.run / name).parent.mkdir(parents=True, exist_ok=True)
        (self.run / name).write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def approve(self, blind=False):
        package = review.preparar(self.run, self.plan, blind=blind)
        report = {"schema_version": 1, "rubrica_sha256": package["rubrica_sha256"],
                  "pacote_sha256": package["pacote_sha256"],
                  "revisor": {"identidade": "test reviewer", "execucao": "test-01", "concluido_em": "2026-10-25T00:00:00Z"},
                  "independente_do_autor": True, "cards": []}
        for c in package["cards"]:
            report["cards"].append({
                "case_id": c["case_id"], "input_sha256": c["input_sha256"], "veredito": "aprovado",
                "alvo": "channel A is the useful link between signal and entry",
                "ambiguidade_alternativa": "Channel B serves another process, ruled out by signal context.",
                "ganho": "Extra carries the ion-entry consequence missing from the short target.",
                "encaixe": "Introduces the channel before its downstream membrane response.",
                "justificativa_formato": "A focal name connects the supplied signal with its consequence.",
                "teste_reconstrucao": "Signal opens channel, allowing entry and changing response.",
                "evidencias": [{"trecho": "Opening allows ion entry", "analise": "Provides causal continuation."}],
                "problemas": [],
            })
        self.write(review.REPORT, report)
        return package, report

    def passes(self):
        return all(ok for _, ok in review.verificar(self.run, self.plan))

    def test_v9_requires_executor_supervision_after_weak_calibration(self):
        self.plan["pipeline_versao"] = 9
        package, _ = self.approve()
        self.assertFalse(self.passes())
        case=package["cards"][0]
        self.write("revisao-executor-autorais.json", {"pacote_sha256":package["pacote_sha256"], "cards":[{
            "case_id":case["case_id"], "input_sha256":case["input_sha256"], "veredito":"aprovado",
            "julgamento":"The target recovers the transition from signal to entry.", "trecho":"Opening allows ion entry"}]})
        self.assertTrue(self.passes())

    def test_valid_complete_current_receipt(self):
        self.approve()
        self.assertTrue(self.passes())

    def test_front_extra_context_source_search_and_motive_edits_invalidate(self):
        variants = [lambda e: e["fields"].update(Text="A different target {{c1::channel B}}"),
                    lambda e: e["fields"].update(Extra="Different consequence."),
                    lambda e: e["contexto"].update(aula="Different lecture"),
                    lambda e: e["fontes"][0].update(trecho="Different source passage"),
                    lambda e: e["busca"]["candidatos"][0].update(decisao="Actually equivalent"),
                    lambda e: e["motivacao"].update(reconstruir="Another capability")]
        initial = copy.deepcopy(self.plan)
        for mutate in variants:
            self.plan = copy.deepcopy(initial)
            self.approve()
            mutate(self.plan["entries"][0])
            self.assertFalse(self.passes())

    def test_old_sidecar_cannot_mask_plan_field_change(self):
        self.write(review.CONTEXT, {"cards": {"au-process": {"fields": self.plan["entries"][0]["fields"]}}})
        self.approve()
        self.plan["entries"][0]["fields"]["Text"] = "Changed {{c1::target}}"
        self.assertFalse(self.passes())

    def test_search_result_or_source_file_change_invalidates(self):
        self.write("busca/semantica.jsonl", {"query": "channel A"})
        self.approve()
        self.write("busca/semantica.jsonl", {"query": "channel B"})
        self.assertFalse(self.passes())
        source = self.run / "source.txt"
        source.write_text("original source")
        self.write(review.CONTEXT, {"cards": {"au-process": {"fontes": [
            {"trecho": "original source", "localizador": "page 1", "arquivo": "source.txt"}]}}})
        self.approve()
        source.write_text("corrected source")
        self.assertFalse(self.passes())

    def test_changed_rubric_and_invalid_version_block(self):
        local = self.run / "rubric.md"
        local.write_text(review.RUBRICA.read_text())
        with patch.object(review, "RUBRICA", local):
            self.approve()
            local.write_text(local.read_text() + "\nNew criterion.\n")
            self.assertFalse(self.passes())
            local.write_text("Rubrica: old\n")
            self.assertFalse(self.passes())

    def test_rejected_or_insufficient_blocks_without_converting_to_pass(self):
        for verdict in ("revisar", "evidencia_insuficiente"):
            _, report = self.approve()
            report["cards"][0]["veredito"] = verdict
            report["cards"][0]["problemas"] = [{"criterio": "scope", "motivo": "missing context", "acao": "supply context"}]
            self.write(review.REPORT, report)
            self.assertFalse(self.passes())

    def test_empty_missing_duplicate_and_extra_reviews_block(self):
        for mutate in (lambda r: r.update(cards=[]),
                       lambda r: r["cards"].append(copy.deepcopy(r["cards"][0])),
                       lambda r: r["cards"][0].update(case_id="unknown")):
            _, report = self.approve()
            mutate(report)
            self.write(review.REPORT, report)
            self.assertFalse(self.passes())
        (self.run / review.REPORT).unlink()
        self.assertFalse(self.passes())

    def test_empty_plan_does_not_pass_and_real_all_acervo_is_not_applicable(self):
        self.plan = {"entries": [], "compartilhados": {}}
        self.assertFalse(self.passes())
        self.plan = {"entries": [{"key": "ak-one", "origin": "AnKing"}]}
        self.assertTrue(self.passes())

    def test_shared_author_is_included_and_needs_review(self):
        shared = copy.deepcopy(self.plan["entries"][0])
        shared.pop("key")
        self.plan["compartilhados"] = {"1234567890123": shared}
        package, report = self.approve()
        self.assertEqual(package["total_autorais"], 2)
        self.assertTrue(self.passes())
        report["cards"].pop()
        self.write(review.REPORT, report)
        self.assertFalse(self.passes())

    def test_shared_unknown_origin_requires_materialization_and_cannot_hide_author(self):
        self.plan["compartilhados"] = {"1234567890123": {"source_nid": "", "deck_proprio": True}}
        self.approve()
        self.assertFalse(self.passes())
        self.write(review.CONTEXT, {"cards": {"sh-1234567890123": {**self.plan["entries"][0]}}})
        package, _ = self.approve()
        self.assertEqual(package["total_autorais"], 2)
        self.assertTrue(self.passes())
        self.plan["compartilhados"]["1234567890123"]["origin"] = "Autoral"
        self.write(review.CONTEXT, {"cards": {"sh-1234567890123": {"origin": "AnKing"}}})
        package, _ = self.approve()
        self.assertEqual(package["total_autorais"], 2)
        self.assertFalse(self.passes())

    def test_duplicate_plan_keys_block(self):
        self.plan["entries"].append(copy.deepcopy(self.plan["entries"][0]))
        self.approve()
        self.assertFalse(self.passes())

    def test_blind_input_omits_labels_comments_ids_and_tags(self):
        entry = self.plan["entries"][0]
        entry.update(nid=1234567890123, tags=["NEBLI::origem::Autoral", "gostei"], expected_verdict="revisar", likes=10)
        entry["fields"].update(NEBLI_Comentario="BAD COMMENT SECRET", NEBLI_Resposta="OLD VERDICT SECRET")
        entry["contexto"].update(comentarios="COMMENT SECRET", labels={"gold": "LABEL SECRET"},
                                  nested={"note_id": 1234567890123, "feedback": "FEEDBACK SECRET", "processo": "Keep process"})
        package, _ = self.approve(blind=True)
        packed = json.dumps(package)
        for value in ("COMMENT SECRET", "VERDICT SECRET", "LABEL SECRET", "FEEDBACK SECRET", "1234567890123", "au-process", "gostei"):
            self.assertNotIn(value, packed)
        self.assertIn("Keep process", packed)
        self.assertTrue(self.passes())

    def test_missing_source_cannot_receive_full_approval(self):
        self.plan["entries"][0]["fontes"] = []
        self.approve()
        self.assertFalse(self.passes())

    def test_fabricated_quote_and_metadata_quote_block(self):
        for quote in ("This sentence was not supplied", "A-does-not-exist"):
            _, report = self.approve()
            report["cards"][0]["evidencias"][0]["trecho"] = quote
            self.write(review.REPORT, report)
            self.assertFalse(self.passes())
        package, report = self.approve()
        report["cards"][0]["evidencias"][0]["trecho"] = package["cards"][0]["input_sha256"]
        self.write(review.REPORT, report)
        self.assertFalse(self.passes())

    def test_approved_with_pending_problem_is_blocked(self):
        _, report = self.approve()
        report["cards"][0]["problemas"] = [{"criterio": "ambiguity", "motivo": "two valid answers", "acao": "qualify context"}]
        self.write(review.REPORT, report)
        self.assertFalse(self.passes())

    def test_format_reconstruction_and_independence_are_required(self):
        for field in ("justificativa_formato", "teste_reconstrucao", "ambiguidade_alternativa"):
            _, report = self.approve()
            del report["cards"][0][field]
            self.write(review.REPORT, report)
            self.assertFalse(self.passes())
        _, report = self.approve()
        report["independente_do_autor"] = False
        self.write(review.REPORT, report)
        self.assertFalse(self.passes())

    def test_malformed_report_fails_without_crashing(self):
        for report in ([], {"cards": [{}]}, {"cards": [{"case_id": []}]}):
            self.approve()
            self.write(review.REPORT, report)
            self.assertFalse(self.passes())


if __name__ == "__main__":
    unittest.main()
