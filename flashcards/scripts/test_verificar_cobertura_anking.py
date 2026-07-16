import unittest
from verificar_cobertura_anking import parse_gap_analysis, validar_gates_novos


class CoverageRubricTests(unittest.TestCase):
    def row(self, text):
        return parse_gap_analysis(text)[0]

    def test_reads_new_columns(self):
        row = self.row("| 1.1 Mecanismo | COBERTO | 3 | — | 2 | nuclear | SIM | — |")
        self.assertEqual(row[5:], (2, "nuclear", "sim", "—"))

    def test_legacy_row_remains_readable_and_ungated(self):
        row = self.row("| 1.1 Mecanismo | PENDENTE-GERADO | 0 | slide | 0 | nuclear |")
        self.assertEqual(row[7:], ("", ""))
        self.assertEqual(validar_gates_novos([row], False), [])

    def test_source_missing_from_e1_blocks(self):
        row = self.row("| 1.1 Mecanismo | COBERTO | 2 | — | 3 | nuclear | NAO | — |")
        self.assertTrue(any("ausente da E1" in e for e in validar_gates_novos([row], True)))

    def test_pending_or_question_does_not_cover_nuclear(self):
        row = self.row("| 1.1 Mecanismo | PENDENTE-GERADO | 0 | slide | 2 | nuclear | SIM | — |")
        self.assertTrue(any("não substitui card" in e for e in validar_gates_novos([row], True)))

    def test_covered_with_zero_cards_blocks(self):
        row = self.row("| 1.1 Mecanismo | COBERTO | 0 | questão | 3 | nuclear | SIM | — |")
        self.assertTrue(any("sem card aprovado" in e for e in validar_gates_novos([row], True)))

    def test_neblicard_closes_nuclear(self):
        row = self.row("| 1.1 Mecanismo | COBERTO | 1 | NEBLIcard | 2 | nuclear | SIM | — |")
        self.assertEqual(validar_gates_novos([row], True), [])

    def test_peripheral_can_be_dispensado_with_reason(self):
        row = self.row("| 1.1 Detalhe | LACUNA | 0 | livro | 0 | acessório | DISPENSADO | fora do recorte |")
        self.assertEqual(validar_gates_novos([row], True), [])

    def test_empty_new_schema_blocks_when_header_activates_gate(self):
        row = self.row("| 1.1 Mecanismo | COBERTO | 1 | — | 3 | nuclear | | |")
        self.assertTrue(any("sem decisão" in e for e in validar_gates_novos([row], True)))


if __name__ == "__main__":
    unittest.main()
