from src.datos_pokemo import estadisticas
import unittest


class TestEstadisticas(unittest.TestCase):
    def test_health_point(self):
        self.assertEqual(estadisticas.health_point(80), 172.97642353760523)

    def test_other_stat(self):
        self.assertEqual(estadisticas.other_stat(80), 117.97642353760524)


if __name__ == "__main__":
    unittest.main()
