"""Gates mínimos de documentação; não são avaliação semântica de curadoria."""
from pathlib import Path
import hashlib
import json
import unittest


ROOT = Path(__file__).resolve().parents[2]


class HandoffTests(unittest.TestCase):
    def test_entrypoints_route_to_current_pipeline(self):
        for path in ("AGENTS.md", "CLAUDE.md", ".claude/commands/deck-aula.md", ".claude/commands/resumo.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            self.assertIn("README.md", text)
            self.assertIn("FEEDBACKS.md", text)
            self.assertIn("BANDEIRAS-E-PROGRESSAO.md", text)
            self.assertIn("E1 + cards", text)
            self.assertNotIn("verde somente para `1-HighYield`", text)
            self.assertNotIn("até 35/aula", text)

    def test_required_public_context_exists(self):
        for name in ("README", "CALIBRACAO-ESCALA-V4", "CONTRATO-DE-QUALIDADE",
                     "OPERACAO-CODEX-CLAUDE", "EXECUCAO-DECK-AULA",
                     "ACERVOS-REFERENCIA", "PUBLICACAO-POR-UC", "HANDOFF-CLAUDE"):
            self.assertTrue((ROOT / "flashcards/projeto" / f"{name}.md").is_file())
        self.assertTrue((ROOT / "config/publicacoes-uc.example.json").is_file())

    def test_private_artifacts_are_not_required_for_unit_tests(self):
        text = (ROOT / "flashcards/projeto/HANDOFF-CLAUDE.md").read_text(encoding="utf-8")
        self.assertIn("Clone novo sozinho", text)
        self.assertIn("sem flags", text)
        self.assertIn("não ressuscitar", text.lower())

    def test_archived_context_preserved_byte_for_byte(self):
        archive = ROOT / "backups/contexto-2026-09-25"
        manifest = json.loads((archive / "manifest.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(manifest["files"]), 17)
        for item in manifest["files"]:
            data = (archive / item["path"]).read_bytes()
            self.assertEqual(len(data), item["bytes"], item["path"])
            self.assertEqual(hashlib.sha256(data).hexdigest(), item["sha256"], item["path"])

    def test_old_calibrations_are_history_not_parallel_policy(self):
        for name in ("CALIBRACAO-ESCALA-V4.md", "CALIBRACAO-2026-09-25.md"):
            text = (ROOT / "flashcards/projeto" / name).read_text(encoding="utf-8")
            self.assertIn("# Histórico", text)
            self.assertIn("backups/contexto-2026-09-25", text)
        summary = (ROOT / ".claude/commands/resumo.md").read_text(encoding="utf-8")
        self.assertNotIn("Redigir E2/E3", summary)
        self.assertNotIn("rm typst-build", summary)


if __name__ == "__main__":
    unittest.main()
