"""Gates mínimos de documentação; não são avaliação semântica de curadoria."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


class HandoffTests(unittest.TestCase):
    def test_entrypoints_route_to_current_pipeline(self):
        for path in ("AGENTS.md", "CLAUDE.md", ".claude/commands/deck-aula.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            self.assertIn("CALIBRACAO-ESCALA-V4.md", text)
            self.assertIn("PUBLICACAO-POR-UC.md", text)

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


if __name__ == "__main__":
    unittest.main()
