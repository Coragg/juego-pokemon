from src.lista_pokemon import read_document as leer
import unittest

data = leer.matriz_de_lectura_de_documento("../lista_pokemon/pokemon_data.csv")


class TestReadDocument(unittest.TestCase):
    def test_type_attack(self):
        assert leer.type_attack("dark", "dark") == 1.2
        assert leer.type_attack("dark", "normal") == 1.0

    def test_search_name(self):
        self.assertEqual(leer.search_name("caterpie", data, 832), 9)
        self.assertEqual(leer.search_name("ivysaur", data, 832), 1)

    def test_catidad_habilidades(self):
        assert leer.cantidad_habilidades(9, data) == 5

    def test_buscar_habilidad(self):
        self.assertEqual(leer.buscar_habilidad_seleccionada(9, 1, data), "electroweb")

    def test_cantidad_de_habilidades(self):
        self.assertEqual(leer.cantidad_habilidades(9, data), 4)


if __name__ == "__main__":
    unittest.main()
