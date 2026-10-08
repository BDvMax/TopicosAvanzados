import unittest

try:
    import tkinter as tk
    from guiutils.validated_entry import ValidatedEntry
except ImportError:  # Python sin Tk
    tk = None


class ValidatedEntryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if tk is None:
            raise unittest.SkipTest("tkinter no está instalado")
        try:
            cls.root = tk.Tk()
        except tk.TclError:
            raise unittest.SkipTest("No hay pantalla disponible para Tkinter")
        cls.root.withdraw()

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def test_sin_patron_es_valido_desde_el_inicio(self):
        self.assertTrue(ValidatedEntry(self.root).valid)

    def test_con_patron_inicia_invalido(self):
        self.assertFalse(ValidatedEntry(self.root, pattern=r"\d{4}").valid)

    def test_valida_en_vivo(self):
        e = ValidatedEntry(self.root, pattern=r"\d{4}")
        e.insert(0, "123")
        self.assertFalse(e.valid)
        e.insert("end", "4")
        self.assertTrue(e.valid)

    def test_respeta_textvariable(self):
        var = tk.StringVar(value="2024")
        e = ValidatedEntry(self.root, pattern=r"\d{4}", textvariable=var)
        self.assertTrue(e.valid)
        var.set("abc")
        self.assertFalse(e.valid)

    def test_foco_se_conserva_al_vaciar(self):
        e = ValidatedEntry(self.root, pattern=r"\d+")
        e.insert(0, "a")
        e.delete(0, "end")
        self.assertEqual(str(e.cget("highlightcolor")), e.focus_color)


if __name__ == "__main__":
    unittest.main()
