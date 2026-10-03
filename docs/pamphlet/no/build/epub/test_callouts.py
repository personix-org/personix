import unittest
from callouts import convert


class CalloutTests(unittest.TestCase):
    def test_jednoduchy_callout_s_titulkem(self):
        src = "> [!note] Poznámka\n> Tělo textu.\n"
        out = convert(src)
        self.assertIn("{.callout .note}", out)
        self.assertIn("{.callout-title}\nPoznámka\n:::", out)
        self.assertIn("Tělo textu.", out)
        self.assertNotIn("[!note]", out)
        self.assertNotIn("> ", out)

    def test_vice_odstavcu_a_seznam(self):
        src = "> [!example] Příklady\n> Úvod:\n>\n> - a\n> - b\n\nPo callout.\n"
        out = convert(src)
        self.assertIn("Úvod:\n\n- a\n- b", out)
        self.assertTrue(out.rstrip().endswith("Po callout."))

    def test_callout_bez_titulku(self):
        out = convert("> [!idea]\n> Jen tělo\n")
        self.assertIn("{.callout .idea}", out)
        self.assertNotIn("callout-title", out)

    def test_skladaci_znacka_se_ignoruje(self):
        out = convert("> [!warning]- Pozor\n> x\n")
        self.assertIn("{.callout .warning}", out)
        self.assertIn("Pozor", out)

    def test_bug_se_zahodi(self):
        out = convert("Před\n\n> [!bug] Scratch\n> poznámka\n\nPo\n")
        self.assertNotIn("Scratch", out)
        self.assertNotIn("poznámka", out)
        self.assertIn("Před", out)
        self.assertIn("Po", out)

    def test_obycejny_citat_zustava(self):
        src = "> Obyčejný citát\n> druhý řádek\n"
        self.assertEqual(convert(src), src)

    def test_vnoreny_citat_uvnitr_calloutu(self):
        out = convert("> [!note] T\n> text\n>\n> > vnořený\n")
        self.assertIn("> vnořený", out)
        self.assertNotIn("> > ", out)

    def test_dva_callouty_po_sobe(self):
        out = convert("> [!note] A\n> a\n\n> [!danger] B\n> b\n")
        self.assertEqual(out.count("{.callout "), 2)
        self.assertIn(".danger", out)


if __name__ == "__main__":
    unittest.main()
