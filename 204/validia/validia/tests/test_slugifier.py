import unittest

from guiutils.slugifier import slug


class SlugTests(unittest.TestCase):
    def test_basico(self):
        self.assertEqual(slug("Hola Mundo"), "hola-mundo")

    def test_acentos_y_enie(self):
        self.assertEqual(slug("Hola Mundo ¡Ñandú!"), "hola-mundo-nandu")

    def test_simbolos(self):
        self.assertEqual(slug("Canción Nueva!"), "cancion-nueva")

    def test_espacios_multiples(self):
        self.assertEqual(slug("  a   b  "), "a-b")

    def test_guiones_repetidos_y_bordes(self):
        self.assertEqual(slug("Hola -"), "hola")
        self.assertEqual(slug("--a -- b--"), "a-b")

    def test_vacio_y_solo_simbolos(self):
        self.assertEqual(slug(""), "")
        self.assertEqual(slug("¡¿?!"), "")

    def test_letras_sin_descomposicion(self):
        self.assertEqual(slug("Straße Ørsted"), "strasse-orsted")

    def test_numeros(self):
        self.assertEqual(slug("Top 10 de 2025"), "top-10-de-2025")


if __name__ == "__main__":
    unittest.main()
