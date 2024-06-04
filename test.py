from app import texto
import unittest

class TestCompararTextos(unittest.TestCase):
    def test_1(self):
        texto1A = "TextoA"
        texto2B = "TextoB"
        resul = texto(texto1A, texto2B)
    
        self.assertEqual(resul, False)


if __name__ == '__main__':
    unittest.main()

