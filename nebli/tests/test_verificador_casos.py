import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from nebli import verificador_casos as v

BANCO = {"casos": [{"nid": 1792065031181, "uc": "uc03", "por_que_deu_certo": {"X": "gostei (x)"}}]}


def plano():
    return {"lesson_id": "2026-uc03-micro-99-teste", "entries": [
        {"key": "a", "origin": "AnKing", "fields": {"Text": "Azoles inhibit {{c1::lanosterol}} demethylase", "Extra": "Less ergosterol."}},
        {"key": "b", "origin": "Autoral", "fields": {"Text": "Yeasts bud by {{c1::budding}}", "Extra": '<img src="x.png">'}}]}


def tsv(run, linhas):
    (run / "tipos.tsv").write_text("\t".join(v.COLS) + "\n" + "\n".join("\t".join(l) for l in linhas) + "\n", encoding="utf-8")


class V12Tests(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.TemporaryDirectory(); self.run = Path(self.d.name)
        self.p = mock.patch.object(v._casos, "carregar", return_value=BANCO); self.p.start()

    def tearDown(self):
        self.p.stop(); self.d.cleanup()

    def ok(self, plan):
        return {n.split(":")[0]: ok for n, ok in v.verificar(self.run, plan)}

    def test_falta_tipo_e_imagem_e_parecer(self):
        tsv(self.run, [["a", "decoreba", "x", "sim", ""], ["b", "mecanismo", "budding gives unequal daughter cells", "não", ""]])
        r = v.verificar(self.run, plano())
        self.assertFalse(r[1][1])  # tipo inválido, princípio curto, autoral sem papel
        self.assertFalse(r[2][1])  # visual sem figura
        self.assertFalse(r[-1][1])  # sem parecer

    def test_tudo_aprovado(self):
        tsv(self.run, [["a", "mecanismo", "azoles block ergosterol synthesis", "não", ""],
                       ["b", "fato-chave", "yeasts reproduce asexually by budding", "sim", "lacuna"]])
        plan = plano()
        v.preparar(self.run, plan)
        pac = json.loads((self.run / v.ENTRADA).read_text())
        par = {"cards_sha": pac["cards_sha"], "banco_sha": pac["banco_sha"],
               "cards": {k: {"caso": 1792065031181, "veredito": "aprovado", "comparacao": f"{k}: mesmo formato causal do caso dos antifúngicos.",
                             "motivo": f"{k}: ensina o princípio declarado e a figura mostra o alvo."} for k in "ab"},
               "deck": {"fio_da_aula": "mecanismo antes do fato", "repetidos": "nenhum", "fora_do_principio": "nenhum"}}
        (self.run / v.PARECER).write_text(json.dumps(par))
        self.assertTrue(all(ok for _, ok in v.verificar(self.run, plan)))
        plan["entries"][0]["fields"]["Text"] += " now"
        self.assertFalse(dict(v.verificar(self.run, plan))["[duro] v12: parecer do verificador é do deck atual (hashes de cards e banco)"])

    def test_repetido(self):
        plan = plano(); plan["entries"][1]["fields"]["Text"] = "Azoles target {{c1::lanosterol}}"
        tsv(self.run, [])
        self.assertIn("a=b", " ".join(n for n, _ in v.verificar(self.run, plan)))


if __name__ == "__main__":
    unittest.main()
