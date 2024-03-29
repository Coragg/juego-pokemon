# Este archivo sirve para testear las funciones del read document.

from src.lista_pokemon import read_document as read
import unittest

data = read.matriz_de_lectura_de_documento("../lista_pokemon/pokemon_data.csv")


class TestReadDocument(unittest.TestCase):
    def test_type_attack(self):
        assert read.type_attack("dark", "dark") == 1.2
        assert read.type_attack("dark", "normal") == 1.0

    def test_search_name(self):
        self.assertEqual(read.search_name("caterpie", data, 832), 9)
        self.assertEqual(read.search_name("ivysaur", data, 832), 1)

    def test_buscar_habilidad(self):
        self.assertEqual(read.buscar_habilidad_seleccionada(9, 1, data), "electroweb")

    def test_cantidad_de_habilidades(self):
        self.assertEqual(read.cantidad_habilidades(9, data), 4)
        self.assertEqual(read.cantidad_habilidades(378, data), 98)
        self.assertEqual(read.cantidad_habilidades(357, data), 109)


if __name__ == "__main__":
    unittest.main()
